# Repository Information
Name: aws-mikrotik-api

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/ftsystems/aws-mikrotik-api.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
#
# deploy stack via gitlab ci
#
stages:
  - deploy
deploy:
  stage: deploy
  image: python:3.7
  script:
    - apt-get update -q -y
    - apt-get -y install zip
    - pip install -r requirements.txt
    - bash -c "echo $VAULTPASSWORD > .vault"
    # ansible doesnt accept the ansible cfg as it is executed in a word writeable dir.
    # we need to pass all config parameters via command line
    - ansible-playbook -i ./hosts --vault-password-file=./.vault playbook.yml
================================================

File: ddns-update.py
================================================
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import ipaddress
import boto3
import datetime
# weblinks:
# 2018-12-18: https://goonan.io/a-simple-python3-lambda-function-on-aws-with-an-api-gateway/
# 2018-12-18: https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
def arecord(zoneid, comment, name, ip):
    """ create or update the an A record """
    client = boto3.client('route53')
    print("Send route 53 request for A recors {} with ip {}".format(name,ip))
    response = client.change_resource_record_sets(
        HostedZoneId = zoneid,
        ChangeBatch = {
            'Comment': comment,
            'Changes': [{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': name,
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [
                        { 'Value': ip }
                    ]
                }
            }]
        }
    )
    print("Route53 response: {}".format(response))
def response(message, status_code, base64_encoded=False):
    """ send response to api gateway """
    return {
        'isBase64Encoded': base64_encoded,
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
def handler(event, context):
    """ 
        lambda event handler
    """ 
    print("Start ddns update process")
    try:
        # get the required variables in place
        source_ip = event['requestContext']['identity']['sourceIp']
        domain = os.environ['DOMAIN']
        zoneid = os.environ['ZONEID']
        blacklist = os.getenv('BLACKLIST','').split(',')
        body = json.loads(event['body'])
        # if no name is specified we cant create a dns entry
        if not body['name']:
            raise ValueError("invalid name")
        else:
            record_name = body['name']
        # check if the record name is in the blacklist
        if record_name in blacklist:
            print("Record {} is in blacklist {}. Abort.".format(record_name,blacklist))
            return response({'message': 'Invalid name specified. Abort.'}, 400) 
        # if no ip field is set in the message body we take
        # the public ip
        record_ip = source_ip
        if 'ip' in body:
            if body['ip']:
                record_ip = body['ip']
        # check if the ip address is valid
        try:
            ipaddress.ip_address(record_ip)
        except Exception as e:
            print("Invalid ip address sepcified - {}. Abort.".format(e))
            return response({'message': 'Invalid ip specified. Abort.'}, 400) 
        # create the comment string for the dns record
        record_comment = "Last update: {} UTC".format((datetime.datetime.utcnow()))
        # name and ip is valid. lets create or update the dns record
        arecord(zoneid, record_comment, "{}.{}.".format(record_name,domain), record_ip)
        # send a ok to the client
        return response({'message': 'Sent DNS update request. Finished.'}, 200)
    except Exception as e:
        print("Unhandled exception: {}".format(e))
        return response({'message': 'Invalid request'}, 500)
================================================

File: example_event.json
================================================
{
    'resource': '/ddns/update', 
    'path': '/ddns/update', 
    'httpMethod': 'POST', 
    'headers': {
        'Accept': '*/*', 
        'Accept-Encoding': 'gzip, deflate', 
        'Authorization': 'Basic YWRtaW46c2VjcmV0', 
        'cache-control': 'no-cache', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'CH', 'Host': 'api.mikrotik.ftscloud.ch', 'Postman-Token': '3bc079d3-2595-4698-87ec-755cbd49547a', 'User-Agent': 'PostmanRuntime/7.4.0', 'Via': '1.1 80b17b6368eead093138ee55fbbeb801.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': '54u6FHyVeCNt2xyR9avVk09lxgkLEY5x2m0y7-E-i0pfByCWJbtb8A==', 'X-Amzn-Trace-Id': 'Root=1-5c1d11d6-226410856e6b6f8499bc059f', 'X-Forwarded-For': '194.230.155.244, 52.46.13.93', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 
        'Accept-Encoding': ['gzip, deflate'], 
        'Authorization': ['Basic YWRtaW46c2VjcmV0'], 
        'cache-control': ['no-cache'], 
        'CloudFront-Forwarded-Proto': ['https'], 
        'CloudFront-Is-Desktop-Viewer': ['true'], 
        'CloudFront-Is-Mobile-Viewer': ['false'], 
        'CloudFront-Is-SmartTV-Viewer': ['false'], 
        'CloudFront-Is-Tablet-Viewer': ['false'], 
        'CloudFront-Viewer-Country': ['CH'], 
        'Host': ['api.mikrotik.ftscloud.ch'],
        'Postman-Token': ['3bc079d3-2595-4698-87ec-755cbd49547a'], 
        'User-Agent': ['PostmanRuntime/7.4.0'], 
        'Via': ['1.1 80b17b6368eead093138ee55fbbeb801.cloudfront.net (CloudFront)'], 
        'X-Amz-Cf-Id': ['54u6FHyVeCNt2xyR9avVk09lxgkLEY5x2m0y7-E-i0pfByCWJbtb8A=='], 
        'X-Amzn-Trace-Id': ['Root=1-5c1d11d6-226410856e6b6f8499bc059f'], 
        'X-Forwarded-For': ['194.230.155.244, 52.46.13.93'], 
        'X-Forwarded-Port': ['443'], 
        'X-Forwarded-Proto': ['https']
    }, 
    'queryStringParameters': {'': ''}, 
    'multiValueQueryStringParameters': {'': ['']}, 
    'pathParameters': None, 
    'stageVariables': {'LambdaAlias': 'public'}, 
    'requestContext': {
        'resourceId': 'oi2d8h', 
        'authorizer': {'principalId': 'admin'}, 
        'resourcePath': '/ddns/update', 
        'httpMethod': 'POST', 
        'extendedRequestId': 'SQ-5iHEmliAFYDA=', 
        'requestTime': '21/Dec/2018:16:16:22 +0000', 
        'path': '/ddns/update', 
        'accountId': '173135140553', 
        'protocol': 'HTTP/1.1', 
        'stage': 'public', 
        'domainPrefix': 'api', 
        'requestTimeEpoch': 1545408982606, 
        'requestId': 'c1ea073e-053b-11e9-b7c3-6b1f5d80197b', 
        'identity': {
            'cognitoIdentityPoolId': None, 
            'accountId': None, 
            'cognitoIdentityId': None,
             'caller': None, 
             'sourceIp': '194.230.155.244', 
             'accessKey': None, 
             'cognitoAuthenticationType': None, 
             'cognitoAuthenticationProvider': None,
             'userArn': None, 
             'userAgent': 'PostmanRuntime/7.4.0',
              'user': None
            }, 
        'domainName': 'api.mikrotik.ftscloud.ch', 
        'apiId': 'c6kj8869zh'
    }, 
    'body': '{\n\t"name": "mycnamerecord",\n\t"ip": ""\n}'
    'isBase64Encoded': False
}
================================================

File: ddns-update-authorizer.py
================================================
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import base64
# weblinks:
# 2018-12-18: https://goonan.io/a-simple-python3-lambda-function-on-aws-with-an-api-gateway/
# 2018-12-18: https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
# 2018-12-18: https://medium.com/@Da_vidgf/http-basic-auth-with-api-gateway-and-serverless-5ae14ad0a270
# 2018-12-22: https://stackoverflow.com/questions/41486130/aws-api-gateway-execution-failed-due-to-configuration-error-invalid-json-in-re
# 2018-12-22: https://github.com/awslabs/aws-apigateway-lambda-authorizer-blueprints/blob/master/blueprints/python/api-gateway-authorizer-python.py
def policy(event, principalId):
    """ create a policy document """
    tmp = event['methodArn'].split(':')
    awsAccountId = tmp[4]
    apiGatewayArnTmp = tmp[5].split('/')
    awsRegion = tmp[3]
    restApiId = apiGatewayArnTmp[0]
    stage = apiGatewayArnTmp[1]
    apiArn = 'arn:aws:execute-api:' + awsRegion + ':' + awsAccountId + ':' + restApiId + '/' + stage + '/*/*'
    policy = {
        'principalId': principalId,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': [
                        apiArn
                    ],
                }
            ]
        }
    }
    return policy
def handler(event, context):
    """ 
        lambda event handler
    """
    try:
        print("Start authorization process")
        # check if authorization header isnt set
        if 'Authorization' not in event['headers']:
            print("No Authorization header found. Abort.")
            raise Exception('Unauthorized')
        # get username and password from envrionment
        auth_username = os.environ['AUTH_USERNAME']
        auth_password = os.environ['AUTH_PASSWORD']
        # get password username and password from auth header
        authorizationHeader = event['headers']['Authorization']
        encodedCreds = authorizationHeader.split(' ')[1]
        plainCreds = base64.b64decode(encodedCreds).decode("utf-8").split(':')
        cred_username = plainCreds[0]
        cred_password = plainCreds[1]
        # check if credentials match
        if auth_username == cred_username and auth_password == cred_password:
            print("Authentication succeded. Continue.")
            principalId = "mikrotik|{}|{}".format(cred_username,event['requestContext']['identity']['sourceIp'])
            return policy(event, principalId)
        else:
            print("Wrong username or password. Abort.")
            raise Exception('Unauthorized')
    except Exception as e:
        print("Unhandled exception: {}".format(e))
        raise Exception('Unauthorized')
================================================

File: LICENSE
================================================
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/
   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
   1. Definitions.
      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.
      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.
      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.
      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.
      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.
      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.
      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).
      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.
      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."
      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.
   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.
   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.
   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:
      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and
      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and
      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and
      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.
      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.
   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.
   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.
   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.
   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.
   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.
   END OF TERMS AND CONDITIONS
   APPENDIX: How to apply the Apache License to your work.
      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.
   Copyright 2019 ft systems gmbh
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
================================================

File: playbook.yml
================================================
---
#
# setup an api gateway for mikrotik setup
#
# you need to have aws cli configured locally to use
# the playbooks.
- hosts: localhost
  gather_facts: false
  tasks:
    ###
    # GET METAINFORMATION
    ###
    - name: include variables for api gateway management
      include_vars: "{{item}}"
      loop:
       - variables.vault.yaml
       - variables.yaml
      tags: always
    - name: get aws caller identification
      aws_caller_facts:
      register: caller_facts
      tags: always
    ###
    # SETUP CLOUDFORMATION STACKS
    ###
    # ACM CERTIFICATE
    - block:
      - name: render cloudformation template
        template:
          src: templates/00_certificate.cloudformation.yml
          dest: templates/certificate.cloudformation
        changed_when: false
      - name: create cloudformation stack for api gateway certificate
        cloudformation:
          stack_name: "{{aws_mikrotik_api_stack_name_certificate}}"
          state: "present"
          # must be deployed in us east because acm doesnt
          # work anywhere else
          region: "{{aws_mikrotik_cloudformation_certificate_region}}"
          disable_rollback: false
          template: "templates/certificate.cloudformation"
      always:
      - name: remove rendered template
        file:
          path: "templates/certificate.cloudformation"
          state: absent
        changed_when: false
      tags: 
        - acm
    # RETRIEVE INFORMATION FROM ACM CERTIFICATE STACK
    - block:
      - cloudformation_facts:
          stack_name: "{{aws_mikrotik_api_stack_name_certificate}}"
          stack_resources: true
          region: "{{aws_mikrotik_cloudformation_certificate_region}}"
        register: certificate_stack_facts
      - set_fact: sslcertificatearn="{{certificate_stack_facts | json_query(query) }}"
        vars:
          query: "ansible_facts.cloudformation.{{aws_mikrotik_api_stack_name_certificate}}.stack_resources.SSLCertificate"
      tags:
        - gateway
    # API GATEWAY
    - block:
      - name: render cloudformation template
        template:
          src: templates/10_gateway.cloudformation.yml
          dest: templates/gateway.cloudformation
        changed_when: false
      - name: create cloudformation stack for api gateway
        cloudformation:
          stack_name: "{{ aws_mikrotik_api_stack_name_gateway }}"
          state: "present"
          # must be deployed in us east because acm doesnt
          # work anywhere else
          region: "{{aws_mikrotik_cloudformation_gateway_region}}"
          disable_rollback: false
          template: "templates/gateway.cloudformation"
      always:
      - name: remove rendered template
        file:
          path: "templates/gateway.cloudformation"
          state: absent
        changed_when: false
      tags:
        - gateway
    # LAMBDA DDNS UPDATE
    - block: 
      - name: render cloudformation template
        template:
          src: templates/20_ddns-lambda.cloudformation.yml
          dest: templates/ddns-lambda.cloudformation
        changed_when: false
      - name: create cloudformation stack for ddns lambda function
        cloudformation:
          stack_name: "{{ aws_mikrotik_api_stack_name_ddns_lambda }}"
          state: "present"
          # must be deployed in us east because acm doesnt
          # work anywhere else
          region: "{{aws_mikrotik_ddns_lambda_region}}"
          disable_rollback: false
          template: "templates/ddns-lambda.cloudformation"
      always:
      - name: remove rendered template
        file:
          path: "templates/ddns-lambda.cloudformation"
          state: absent
        changed_when: false
      tags:
        - lambda
        - ddns
    # LAMBDA DDNS UPDATE AUTHORIZER
    - block: 
      - name: render cloudformation template
        template:
          src: templates/20_ddns-lambda-authorizer.cloudformation.yml
          dest: templates/ddns-lambda-authorizer.cloudformation
        changed_when: false
      - name: create cloudformation stack for ddns authorizer lambda function
        cloudformation:
          stack_name: "{{ aws_mikrotik_api_stack_name_ddns_authorizer_lambda }}"
          state: "present"
          # must be deployed in us east because acm doesnt
          # work anywhere else
          region: "{{aws_mikrotik_ddns_authorizer_lambda_region}}"
          disable_rollback: false
          template: "templates/ddns-lambda-authorizer.cloudformation"
      always:
      - name: remove rendered template
        file:
          path: "templates/ddns-lambda-authorizer.cloudformation"
          state: absent
        changed_when: false
      tags:
        - lambda
        - authorizer
    # RETRIEVE INFORMATION FROM LAMBDA DDNS UPDATE STACK  
    # RETRIEVE INFORMATION FROM LAMBDA DDNS UPDATE AUTHORIZER STACK
    - block:
      - lambda_facts:
          query: all
          function_name: "{{aws_mikrotik_ddns_lambda_function_name}}"
          region: "{{aws_mikrotik_ddns_lambda_region}}"
        register: ddnsupdate_facts
      - set_fact: lambdaddnsupdatearn="{{ ddnsupdate_facts | json_query(query) }}"
        vars:
          query: "ansible_facts.lambda_facts.function.{{aws_mikrotik_ddns_lambda_function_name}}.function_arn"
      - set_fact: lambdaddnsupdaterole="{{ ddnsupdate_facts | json_query(query) }}"
        vars:
          query: "ansible_facts.lambda_facts.function.{{aws_mikrotik_ddns_lambda_function_name}}.role"
      - lambda_facts:
          query: all
          function_name: "{{ aws_mikrotik_ddns_authorizer_lambda_function_name }}"
          region: "{{aws_mikrotik_ddns_authorizer_lambda_region}}"
        register: ddnsupdateauthorizer_facts
      - set_fact: lambdaddnsupdateauhtorizerarn="{{ ddnsupdateauthorizer_facts | json_query(query) }}"
        vars:
          query: "ansible_facts.lambda_facts.function.{{aws_mikrotik_ddns_authorizer_lambda_function_name}}.function_arn"
      - set_fact: lambdaddnsupdateauhtorizerrole="{{ ddnsupdateauthorizer_facts | json_query(query) }}"
        vars:
          query: "ansible_facts.lambda_facts.function.{{aws_mikrotik_ddns_authorizer_lambda_function_name}}.role"
      tags:
        - restapi
        - code
        - ddns
        - lambda
        - authorizer
    # RESTAPI 
    - block:
      - name: render cloudformation template
        template:
          src: templates/30_mikrotik-api.cloudformation.yml
          dest: templates/mikrotik-api.cloudformation
        changed_when: false
      - name: create cloudformation stack for mikrotik api
        cloudformation:
          stack_name: "{{ aws_mikrotik_api_stack_name_api }}"
          state: "present"
          region: "{{aws_mikrotik_cloudformation_api_region}}"
          disable_rollback: false
          template: "templates/mikrotik-api.cloudformation"
      always:
      - name: remove rendered template
        file:
          path: "templates/mikrotik-api.cloudformation"
          state: absent
        changed_when: false
      tags:
        - restapi
    # BUILD AND DEPLOY DDNS UPDATE LAMBDA
    - block:
      - name: Retrieve commit id from gitlab runner 
        set_fact: ddns_commitid="{{ lookup('env','CI_COMMIT_SHORT_SHA') }}"
      # if we cant retrieve the commit id from the gitlab
      # env var we assume we run the script locally
      # and try to get the commit id from the local git repo 
      - name: Retrieve commit id from local git repo
        command: git rev-parse --short=8 HEAD
        register: git_local
        changed_when: false
        when: not ddns_commitid
      - set_fact: ddns_commitid="{{git_local.stdout}}"
        when: not ddns_commitid
      # set zip name
      - set_fact: ddns_code_zip="{{ddns_commitid}}.zip"
      - name: Retrieve s3 keys (max 1000)
        aws_s3:
          bucket: "{{aws_mikrotik_ddns_lambda_code_bucket}}"
          mode: list
          region: "{{aws_mikrotik_ddns_lambda_region}}"
        register: s3_list
      - name: Check if the commit id already exists in s3
        set_fact: ddns_code_is_uploaded=True
        when: ddns_code_zip in s3_list.s3_keys
      tags:
        - lambda
        - ddns
        - code
    - block:
      - name: dns update - create virtualenv for deployment
        command: "virtualenv -p python3.7 .deployment-update"
        args:
          creates: .deployment-update
      - name: dns update - check for requirements txt
        stat:
          path: "functions/ddns-update/requirements.txt"
        register: r
      - name: dns update - install requirements for deployment
        command: ".deployment/bin/pip3 install --upgrade -r functions/ddns-update/requirements.txt"
        args:
          # example package - change according to requirements
          creates: ".deployment/lib/python3*/site-packages/requests"
        when: r.stat.exists
      - name: "ddns update - create deployment zip file"
        shell: |
          cp functions/ddns-update/ddns-update.py .deployment-update/lib/python3*/site-packages
          cd .deployment-update/lib/python3*/site-packages
          zip -r9 ../../../../{{ddns_code_zip}} .
          rm ddns-update.py
        register: cmd
      - name: dns update - upload zip to s3
        aws_s3:
          bucket: "{{aws_mikrotik_ddns_lambda_code_bucket}}"
          mode: put
          object: "{{ddns_code_zip}}"
          src: "{{ddns_code_zip}}"
      - name: dns update - update lambda
        lambda:
            name: "{{aws_mikrotik_ddns_lambda_function_name}}" 
            s3_key: "{{ddns_code_zip}}"
            s3_bucket: "{{aws_mikrotik_ddns_lambda_code_bucket}}"
            runtime: "{{aws_mikrotik_ddns_lambda_runtime}}"
            handler: "{{aws_mikrotik_ddns_lambda_handler}}"
            role: "{{lambdaddnsupdaterole}}"
            region: "{{aws_mikrotik_ddns_lambda_region}}"            
            state: present
      always:
      - name: remove deployment zip
        file:
          path: "{{ddns_code_zip}}"
          state: absent
        changed_when: false
      tags:
        - lambda
        - ddns
        - code
      when: ddns_code_is_uploaded is not defined
    # BUILD AND DEPLOY DDNS UPDATE AUTHORIZER LAMBDA
    - block:
      - name: Retrieve commit id from gitlab runner 
        set_fact: ddns_commitid="{{ lookup('env','CI_COMMIT_SHORT_SHA') }}"
      # if we cant retrieve the commit id from the gitlab
      # env var we assume we run the script locally
      # and try to get the commit id from the local git repo 
      - name: Retrieve commit id from local git repo
        command: git rev-parse --short=8 HEAD
        register: git_local
        changed_when: false
        when: not ddns_commitid
      - set_fact: ddns_commitid="{{git_local.stdout}}"
        when: not ddns_commitid
      # set zip name
      - set_fact: authorizer_code_zip="{{ddns_commitid}}.zip"
      - name: Retrieve s3 keys (max 1000)
        aws_s3:
          bucket: "{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}"
          mode: list
          region: "{{ aws_mikrotik_ddns_authorizer_lambda_region}}"
        register: s3_list
      - name: Check if the commit id already exists in s3
        set_fact: authorizer_code_is_uploaded=True
        when: authorizer_code_zip in s3_list.s3_keys
      tags:
        - lambda
        - ddns
        - code
    - block:
      - name: dns authorizer - create virtualenv for deployment
        command: "virtualenv -p python3.7 .deployment-authorizer"
        args:
          creates: .deployment-authorizer
      - name: dns authorizer - check for requirements txt
        stat:
          path: "functions/ddns-update-authorizer/requirements.txt"
        register: r
      - name: dns authorizer - install requirements for deployment
        command: ".deployment-authorizer/bin/pip3 install --upgrade -r functions/ddns-update-authorizer/requirements.txt"
        args:
          # example package - change according to requirements
          creates: ".deployment-authorizer/lib/python3*/site-packages/requests"
        when: r.stat.exists
      - name: "ddns authorizer - create deployment zip file"
        shell: |
          cp functions/ddns-update-authorizer/ddns-update-authorizer.py .deployment-authorizer/lib/python3*/site-packages
          cd .deployment-authorizer/lib/python3*/site-packages
          zip -r9 ../../../../{{authorizer_code_zip}} .
          rm ddns-update-authorizer.py
      - name: dns authorizer - upload zip to s3
        aws_s3:
          bucket: "{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}"
          mode: put
          object: "{{authorizer_code_zip}}"
          src: "{{authorizer_code_zip}}"
      - name: dns authorizer - update lambda
        lambda:
            name: "{{aws_mikrotik_ddns_authorizer_lambda_function_name}}" 
            s3_key: "{{authorizer_code_zip}}"
            s3_bucket: "{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}"
            runtime: "{{aws_mikrotik_ddns_authorizer_lambda_fruntime}}"
            handler: "{{aws_mikrotik_ddns_authorizer_lambda_fhandler}}"
            role: "{{lambdaddnsupdateauhtorizerrole}}"
            region: "{{ aws_mikrotik_ddns_authorizer_lambda_region}}"
            state: present
      always:
      - name: remove deployment zip
        file:
          path: "{{authorizer_code_zip}}"
          state: absent
        changed_when: false
      tags:
        - lambda
        - ddns
        - code
      when: authorizer_code_is_uploaded is not defined
================================================

File: README.md
================================================
# mikrotik-api
Self-made mikrotik dyndns - based on AWS lambda and api gateway
The setup creates A records for the given public ips of a mikrotik router.
The records are created in the dns zone "mikrotik.ftscloud.ch".
## mikrotik fetch
To update the ip address from a mikrotik router you need to use the fetch command
```bash
/tool fetch http-method=post url="https://api.mikrotik.ftscloud.ch/ddns/update" user=admin password=secret http-content-type="application/json" http-data="{\"name\":\"publicdnsname\"}"
```
By default the api takes the source ip the request is sent from (aka the public ip of the router for the A record.
You can override the ip address to set with the ip field.
```bash
/tool fetch http-method=post url="https://api.mikrotik.ftscloud.ch/ddns/update" user=admin password=secret http-content-type="application/json" http-data="{\"name\":\"customiprecord\", \"ip\":\"192.168.1.1\"}"
```
The dns entries are available after a few seconds:
```bash
$ dig publicdnsname.mikrotik.ftscloud.ch
; <<>> DiG 9.10.6 <<>> publicdnsname.mikrotik.ftscloud.ch
...
;; ANSWER SECTION:
publicdnsname.mikrotik.ftscloud.ch. 300 IN A    212.51.159.27
$ dig customiprecord.mikrotik.ftscloud.ch
...
;; ANSWER SECTION:
customiprecord.mikrotik.ftscloud.ch. 300 IN A   192.168.1.1
```
## Requirements
- python3, pip
## Setup environment
First setup a local virtual env
```bash
virtualenv -p python3 .venv
```
Load the virtual env
```bash
source .venv/bin/activate
```
Now install the python requirements
```bash
pip install -r requirements.txt
```
Create the vault password file
```bash
# see keepass "api.mikrotik.ftscloud.ch vaultpass"
echo VAULTPASSWORD > .vault
```
## Usage
First - load the virtual environment 
```bash
source .venv/bin/activate
```
Now make sure you have your AWS credentials setup.
I am using named profiles in my AWS configuration - so I export the profile name when executing the ansible playbook.
Executing the playbook will setup all necessary cloudformation stacks and deploy an empty lambda
```bash
AWS_PROFILE=ftsystems ansible-playbook playbook.yml
```
### Tags
If you want to update a specific stack you can use ansible tags 
- acm : Update the certifficate stack
- gateway: Update the api gateway stack
- lambda: Update lambda stacks
- restapi: Update the restapi stacks
================================================

File: requirements.txt
================================================
requests
awscli 
boto3 
ansible
virtualenv
================================================

File: 00_certificate.cloudformation.yml
================================================
AWSTemplateFormatVersion: "2010-09-09"
Description: ACM Certificate for {{aws_mikrotik_gateway_fqdn}}
Resources:
  SSLCertificate:
    Type: "AWS::CertificateManager::Certificate"
    Properties: 
      DomainName: {{aws_mikrotik_gateway_fqdn}}
================================================

File: 10_gateway.cloudformation.yml
================================================
---
AWSTemplateFormatVersion: "2010-09-09"
Description: Api Gateway {{aws_mikrotik_gateway_fqdn}}
Resources:
  # create the custom domain name
  ApiCustomDomainName:
    Type: 'AWS::ApiGateway::DomainName'
    Properties:
      DomainName: {{aws_mikrotik_gateway_fqdn}}
      CertificateArn: {{sslcertificatearn}}
  # iam role to create logstreams for the apis
  ApiCloudWatchLogsRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "apigateway.amazonaws.com"
            Action:
              - "sts:AssumeRole"
  ApiCloudWatchLogsPolicy:
    Type: "AWS::IAM::Policy"
    Properties: 
      PolicyName: "root"
      PolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Action: 
              - "logs:CreateLogGroup"
              - "logs:CreateLogStream"
              - "logs:DescribeLogGroups"
              - "logs:DescribeLogStreams"
              - "logs:PutLogEvents"
              - "logs:GetLogEvents"
              - "logs:FilterLogEvents"
            Resource: "*"
      Roles: 
        - 
          Ref: "ApiCloudWatchLogsRole"
  # api gateway account with cloudwatch permissions
  ApiGatewayAccount:
    Type: "AWS::ApiGateway::Account"
    DependsOn: ApiCloudWatchLogsPolicy
    Properties:
      CloudWatchRoleArn: !GetAtt ApiCloudWatchLogsRole.Arn
  # add dns entry for api.pitastic.ch
  R53Entry:
    Type: "AWS::Route53::RecordSet"
    Properties: 
      AliasTarget: 
        # hosted zone for cloudfront
        # https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region
        HostedZoneId: {{aws_mikrotik_gateway_dns_zone}}
        DNSName: !GetAtt ApiCustomDomainName.DistributionDomainName
      Comment: Route to CloudFront distribution
      HostedZoneName: !Sub "{{aws_mikrotik_route53_domain}}."
      Name: !Sub "{{aws_mikrotik_gateway_fqdn}}."
      Type: A
================================================

File: 20_ddns-lambda-authorizer.cloudformation.yml
================================================
---
#
# POC fuer Basic Auth 
# nodejs source code von hier kopiret
# https://medium.com/@Da_vidgf/http-basic-auth-with-api-gateway-and-serverless-5ae14ad0a270
AWSTemplateFormatVersion: "2010-09-09"
Description: Lambda for ddns 
Resources:
  # create an s3 bucket which will be used to contain the code zips
  LambdaCodeBucket:
    Type: "AWS::S3::Bucket"
    Properties: 
      BucketName: {{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}
      AccessControl: Private
  # create the lambdahelper execution role and policies
  # the lambda helper function is used to automatically create
  # an empty zip file so we can create the lambda 
  # why a s3 zip file instead of inline you ask ?
  # inline code (ZipFile: | ...) is only supported for python and nodejs
  # this cf template should be as general as possible so we can also deploy java 
  # and go lambdas
  LambdaHelperExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  # https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html
  LambdaHelperPolicy: 
    Type: "AWS::IAM::Policy"
    Properties: 
      PolicyName: "root"
      PolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Action: "s3:ListBucket"
            Resource: "arn:aws:s3:::{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}"
          - 
            Effect: "Allow"
            Action: 
              - "s3:*"
            Resource: "arn:aws:s3:::{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}/*"
      Roles: 
        - 
          Ref: "LambdaHelperExecutionRole"
  # small helper function to create an empty "init.zip" file in the s3 bucket
  LambdaHelperFunction:
    Type: "AWS::Lambda::Function"
    DependsOn: LambdaCodeBucket
    Properties:
      Description: "Lambda Helper Function to create initial zip file in bucket"
      FunctionName: {{aws_mikrotik_ddns_authorizer_lambda_function_name}}Helper
      Runtime: "python3.6"
      Handler: "index.save_to_bucket"
      Role: !GetAtt LambdaHelperExecutionRole.Arn
      Code:
        # upload a zip file containing an empty text file to s3 (an empty zip file is not supported)
        # 2018-08-05: https://gist.github.com/tomfa/7bb519a34262353087a83712539eb6b0
        # 2018-08-05: https://stackoverflow.com/questions/25195495/how-to-create-an-empty-zip-file
        # 2018-08-05: https://stackoverflow.com/questions/43634640/cannot-add-code-to-aws-lambda-function-using-cloudformation
        # 2018-08-05: https://pprakash.me/tech/2015/12/20/sending-response-back-to-cfn-custom-resource-from-python-lambda-function/
        # 2018-08-05: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-cfnresponsemodule
        ZipFile: !Sub |
          import json
          import boto3
          import cfnresponse
          def save_to_bucket(event, context):
              if event['RequestType'] != 'Delete':
                  AWS_BUCKET_NAME = '{{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}'
                  s3 = boto3.resource('s3')
                  bucket = s3.Bucket(AWS_BUCKET_NAME)
                  path = 'init.zip'
                  data = b'PK\x03\x04\n\x00\x00\x00\x00\x00Yc\x05M\x07\xc7\xb6\xae\x06\x00\x00\x00\x06\x00\x00\x00\x05\x00\x1c\x00emptyUT\t\x00\x03\xe9\xd0f[\xe7\xd0f[ux\x0b\x00\x01\x04\xf5\x01\x00\x00\x04\x00\x00\x00\x00empty\nPK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00Yc\x05M\x07\xc7\xb6\xae\x06\x00\x00\x00\x06\x00\x00\x00\x05\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa4\x81\x00\x00\x00\x00emptyUT\x05\x00\x03\xe9\xd0f[ux\x0b\x00\x01\x04\xf5\x01\x00\x00\x04\x00\x00\x00\x00PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00K\x00\x00\x00E\x00\x00\x00\x00\x00'
                  bucket.put_object(
                      Key=path,
                      Body=data,
                  )
              cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Data':''}, "arn:aws:fake:{{aws_mikrotik_ddns_authorizer_lambda_function_name}}HelperZipFile")
  # with the lambda helper function in place we create a custom resource which will call the lambda 
  # and create the zip file
  # https://community.alfresco.com/community/platform/blog/2016/10/13/how-a-lambda-backed-custom-resource-saved-the-day
  LambdaCodeBucketZip:
    Type: Custom::LambdaDependency
    DependsOn: LambdaHelperFunction
    Properties:  
      ServiceToken: !Sub "arn:aws:lambda:{{aws_mikrotik_ddns_authorizer_lambda_region}}:{{caller_facts.account}}:{{aws_mikrotik_ddns_authorizer_lambda_function_name}}Helper"
  # create the lambda execution role and policies for the lambda containing our function code
  LambdaExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  # create the lambda function with the empty zip file
  # the code can be updated with the makefile targets
  LambdaFunction:
    Type: "AWS::Lambda::Function"
    DependsOn: LambdaCodeBucketZip
    Properties:
      Description: "manage mikrotik ddns entries"
      FunctionName: {{aws_mikrotik_ddns_authorizer_lambda_function_name}}
      Runtime: "{{aws_mikrotik_ddns_authorizer_lambda_fruntime}}"
      Handler: "{{aws_mikrotik_ddns_authorizer_lambda_fhandler}}"
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        S3Bucket: {{aws_mikrotik_ddns_authorizer_lambda_code_bucket}}
        S3Key: init.zip
      Environment:
        Variables:
          AUTH_USERNAME: "{{aws_mikrotik_ddns_authorizer_lambda_env_auth_username}}"
          AUTH_PASSWORD: "{{aws_mikrotik_ddns_authorizer_lambda_env_auth_password}}"
================================================

File: 20_ddns-lambda.cloudformation.yml
================================================
---
AWSTemplateFormatVersion: "2010-09-09"
Description: Lambda for ddns 
Resources:
  # create an s3 bucket which will be used to contain the code zips
  LambdaCodeBucket:
    Type: "AWS::S3::Bucket"
    Properties: 
      BucketName: {{aws_mikrotik_ddns_lambda_code_bucket}}
      AccessControl: Private
  # create the lambdahelper execution role and policies
  # the lambda helper function is used to automatically create
  # an empty zip file so we can create the lambda 
  # why a s3 zip file instead of inline you ask ?
  # inline code (ZipFile: | ...) is only supported for python and nodejs
  # this cf template should be as general as possible so we can also deploy java 
  # and go lambdas
  LambdaHelperExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  # https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html
  LambdaHelperPolicy: 
    Type: "AWS::IAM::Policy"
    Properties: 
      PolicyName: "root"
      PolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Action: "s3:ListBucket"
            Resource: "arn:aws:s3:::{{aws_mikrotik_ddns_lambda_code_bucket}}"
          - 
            Effect: "Allow"
            Action: 
              - "s3:*"
            Resource: "arn:aws:s3:::{{aws_mikrotik_ddns_lambda_code_bucket}}/*"
      Roles: 
        - 
          Ref: "LambdaHelperExecutionRole"
  # small helper function to create an empty "init.zip" file in the s3 bucket
  LambdaHelperFunction:
    Type: "AWS::Lambda::Function"
    DependsOn: LambdaCodeBucket
    Properties:
      Description: "Lambda Helper Function to create initial zip file in bucket"
      FunctionName: {{aws_mikrotik_ddns_lambda_function_name}}Helper
      Runtime: "python3.6"
      Handler: "index.save_to_bucket"
      Role: !GetAtt LambdaHelperExecutionRole.Arn
      Code:
        # upload a zip file containing an empty text file to s3 (an empty zip file is not supported)
        # 2018-08-05: https://gist.github.com/tomfa/7bb519a34262353087a83712539eb6b0
        # 2018-08-05: https://stackoverflow.com/questions/25195495/how-to-create-an-empty-zip-file
        # 2018-08-05: https://stackoverflow.com/questions/43634640/cannot-add-code-to-aws-lambda-function-using-cloudformation
        # 2018-08-05: https://pprakash.me/tech/2015/12/20/sending-response-back-to-cfn-custom-resource-from-python-lambda-function/
        # 2018-08-05: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-cfnresponsemodule
        ZipFile: !Sub |
          import json
          import boto3
          import cfnresponse
          def save_to_bucket(event, context):
              if event['RequestType'] != 'Delete':
                  AWS_BUCKET_NAME = '{{aws_mikrotik_ddns_lambda_code_bucket}}'
                  s3 = boto3.resource('s3')
                  bucket = s3.Bucket(AWS_BUCKET_NAME)
                  path = 'init.zip'
                  data = b'PK\x03\x04\n\x00\x00\x00\x00\x00Yc\x05M\x07\xc7\xb6\xae\x06\x00\x00\x00\x06\x00\x00\x00\x05\x00\x1c\x00emptyUT\t\x00\x03\xe9\xd0f[\xe7\xd0f[ux\x0b\x00\x01\x04\xf5\x01\x00\x00\x04\x00\x00\x00\x00empty\nPK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00Yc\x05M\x07\xc7\xb6\xae\x06\x00\x00\x00\x06\x00\x00\x00\x05\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa4\x81\x00\x00\x00\x00emptyUT\x05\x00\x03\xe9\xd0f[ux\x0b\x00\x01\x04\xf5\x01\x00\x00\x04\x00\x00\x00\x00PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00K\x00\x00\x00E\x00\x00\x00\x00\x00'
                  bucket.put_object(
                      Key=path,
                      Body=data,
                  )
              cfnresponse.send(event, context, cfnresponse.SUCCESS, {'Data':''}, "arn:aws:fake:{{aws_mikrotik_ddns_lambda_function_name}}HelperZipFile")
  # with the lambda helper function in place we create a custom resource which will call the lambda 
  # and create the zip file
  # https://community.alfresco.com/community/platform/blog/2016/10/13/how-a-lambda-backed-custom-resource-saved-the-day
  LambdaCodeBucketZip:
    Type: Custom::LambdaDependency
    DependsOn: LambdaHelperFunction
    Properties:  
      ServiceToken: !Sub "arn:aws:lambda:{{aws_mikrotik_ddns_lambda_region}}:{{caller_facts.account}}:{{aws_mikrotik_ddns_lambda_function_name}}Helper"
  # create the lambda execution role and policies for the lambda containing our function code
  LambdaExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          -
            Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  # https://gist.github.com/dfox/1677191
  # https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonroute53.html
  LambdaPolicy: 
    Type: "AWS::IAM::Policy"
    Properties: 
      PolicyName: "root"
      PolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Action: 
              - "route53:ChangeResourceRecordSets"
              - "route53:ListResourceRecordSets"
              - "route53:GetHostedZone"
            Resource: "arn:aws:route53:::hostedzone/{{aws_mikrotik_route53_id}}"
          - 
            Effect: "Allow"
            Action: 
              - "route53:ListHostedZones"
            Resource: "*"
          - 
            Effect: "Allow"
            Action: 
              - "route53:GetChange"
            Resource: "arn:aws:route53:::change/*"     
      Roles: 
        - 
          Ref: "LambdaExecutionRole"
  # create the lambda function with the empty zip file
  # the code can be updated with the makefile targets
  LambdaFunction:
    Type: "AWS::Lambda::Function"
    DependsOn: LambdaCodeBucketZip
    Properties:
      Description: "manage mikrotik ddns entries"
      FunctionName: {{aws_mikrotik_ddns_lambda_function_name}}
      Runtime: "{{aws_mikrotik_ddns_lambda_runtime}}"
      Handler: "{{aws_mikrotik_ddns_lambda_handler}}"
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        S3Bucket: {{aws_mikrotik_ddns_lambda_code_bucket}}
        S3Key: init.zip
      Environment:
        Variables:
          DOMAIN: "{{aws_mikrotik_ddns_lambda_env_domain}}"
          BLACKLIST: "{{aws_mikrotik_ddns_lambda_env_blacklist}}"
          ZONEID: "{{aws_mikrotik_ddns_lambda_env_zoneid}}"
  # create lambda alias for the public release
  LambdaAliasPublic:
    Type: AWS::Lambda::Alias
    DependsOn: LambdaFunction
    Properties:     
      Description: "public version of the function"         
      FunctionName: {{aws_mikrotik_ddns_lambda_function_name}}
      FunctionVersion: "$LATEST"
      Name: {{aws_mikrotik_ddns_lambda_public_alias}}
================================================

File: 30_mikrotik-api.cloudformation.yml
================================================
---
AWSTemplateFormatVersion: "2010-09-09"
Description: Api Definition for mikoritk api
Resources:
  mikrotikapi:
    Type: "AWS::ApiGateway::RestApi"
    Properties:
      Name: mikrotik
      Description: mikrotik api calls
      Body:
        swagger: '2.0'
        info:
          title: Mikrotik API
          description: mikrotik api calls
          version: 0.0.1
          contact:
            name: Sebastian Hutter
            url: https://ftsystems.ch
            email: s.hutter@ftsystems.ch
          license:
            name: Apache 2.0
            url: http://www.apache.org/licenses/LICENSE-2.0.html
        basePath : /
        schemes :
          - https
        # mikrotik cant do headers at the moment
        # in a future release in 2019 the fetch
        # tool should be able to support headers
        # until then we use a custom authorizer
        # securityDefinitions:
        #   api_key:
        #     type: apiKey
        #     name: x-api-key
        #     in: header
        securityDefinitions:
          basic:
            type: apiKey
            name: Authorization
            in: header
            x-amazon-apigateway-authtype: custom
            x-amazon-apigateway-authorizer:
              type: request
              identitySource: method.request.header.Authorization
              authorizerUri: arn:aws:apigateway:{{aws_mikrotik_cloudformation_gateway_region}}:lambda:path/2015-03-31/functions/{{lambdaddnsupdateauhtorizerarn}}/invocations
              authorizerResultTtlInSeconds: 5 
        paths:
          "/ddns/update":
            post:
              description: Set name record for machine
              requestBody:
                description: name and ip to setup
                requitred: true
              produces:
                - application/json
              # security:
              #   - api_key: []
              security:
                - basic: []
              x-amazon-apigateway-integration:
                type: aws_proxy
                responses:
                  default:
                    statusCode: '200'
                httpMethod: POST
                uri: arn:aws:apigateway:{{aws_mikrotik_cloudformation_gateway_region}}:lambda:path/2015-03-31/functions/{{lambdaddnsupdatearn}}:${stageVariables.LambdaAlias}/invocations
# Add Lambda Execution Permission
  LambdaApiPermission:
    Type: "AWS::Lambda::Permission"
    DependsOn: mikrotikapi
    Properties:
      Action: "lambda:invokeFunction"
      FunctionName: "{{lambdaddnsupdatearn}}"
      Principal: "apigateway.amazonaws.com"
      SourceArn: !Sub 
        - "arn:aws:execute-api:{{aws_mikrotik_cloudformation_api_region}}:{{caller_facts.account}}:${Api}/*"
        - Api: !Ref mikrotikapi
  LambdaApiPermissionPublic:
    Type: "AWS::Lambda::Permission"
    DependsOn: mikrotikapi
    Properties:
      Action: "lambda:invokeFunction"
      FunctionName: "{{ lambdaddnsupdatearn }}:{{ aws_mikrotik_ddns_lambda_public_alias }}"
      Principal: "apigateway.amazonaws.com"
      SourceArn: !Sub 
        - "arn:aws:execute-api:{{aws_mikrotik_cloudformation_api_region}}:{{caller_facts.account}}:${Api}/*"
        - Api: !Ref mikrotikapi
# add placeholder deployment
  MikrotikDeployment: 
    Type: AWS::ApiGateway::Deployment
    DependsOn: mikrotikapi
    Properties: 
      RestApiId: !Ref "mikrotikapi"
      StageName: "default"
# the default stage is automatically created 
# we cant configure that one so we create another one
  MikrotikStagePublic:
    Type: AWS::ApiGateway::Stage
    DependsOn: MikrotikDeployment
    Properties:
      DeploymentId: !Ref MikrotikDeployment
      RestApiId: !Ref mikrotikapi
      StageName: "{{ aws_mikrotik_ddns_lambda_public_alias }}"
      Variables:
        LambdaAlias: "{{ aws_mikrotik_ddns_lambda_public_alias }}"
      MethodSettings:
        - DataTraceEnabled: true
          HttpMethod: "*"
          LoggingLevel: "INFO"
          ResourcePath: "/*"
# add custom domain name to mikrotik aos_ip_pool:
  MikrotikBasePathMapping:
    Type: AWS::ApiGateway::BasePathMapping
    DependsOn: MikrotikStagePublic
    Properties:
      DomainName: {{aws_mikrotik_gateway_fqdn}}
      RestApiId: !Ref mikrotikapi
      Stage: "{{ aws_mikrotik_ddns_lambda_public_alias }}"
# add api key for mikrotik routers
  MikrotikApiKey: 
    Type: AWS::ApiGateway::ApiKey
    DependsOn: MikrotikStagePublic
    Properties: 
      Description: "API Key for Mikrotik Routers"
      Enabled: "true"
      StageKeys: 
        - RestApiId: 
            Ref: "mikrotikapi"
          StageName: "{{ aws_mikrotik_ddns_lambda_public_alias }}"
# add api key for mikrotik routers
  MikrotikApiKeyAdmin: 
    Type: AWS::ApiGateway::ApiKey
    DependsOn: MikrotikStagePublic
    Properties: 
      Description: "API Key for Mikrotik Routers - Admin key"
      Enabled: "true"
      StageKeys: 
        - RestApiId: 
            Ref: "mikrotikapi"
          StageName: "{{ aws_mikrotik_ddns_lambda_public_alias }}"
#
# api keys are currently not supported by mikrotik routes as they cant send custom headers.
# we therefore switched to basic auth - no usage plan and keys required
#
# # setup usage plan and keys  
#   MikrotikUsagePlan:
#     Type: AWS::ApiGateway::UsagePlan
#     DependsOn: MikrotikStagePublic
#     Properties:
#       ApiStages:
#       - ApiId: !Ref 'mikrotikapi'
#         Stage: !Ref 'MikrotikStagePublic'
#       Description: Usage plam
#       Quota:
#         Limit: 100000
#         Period: MONTH
#       Throttle:
#         BurstLimit: 50
#         RateLimit: 50
#       UsagePlanName: Mikrotik_API_Usage_Plan
#   MikrotikUsagePlanKey:
#     Type: AWS::ApiGateway::UsagePlanKey
#     DependsOn: 
#       - MikrotikUsagePlan
#       - MikrotikApiKey
#     Properties : 
#       KeyId: !Ref 'MikrotikApiKey'
#       KeyType: API_KEY
#       UsagePlanId: !Ref 'MikrotikUsagePlan'
#   MikrotikUsagePlanKeyAdmin:
#     Type: AWS::ApiGateway::UsagePlanKey
#     DependsOn: 
#       - MikrotikUsagePlan
#       - MikrotikApiKeyAdmin
#     Properties : 
#       KeyId: !Ref 'MikrotikApiKeyAdmin'
#       KeyType: API_KEY
#       UsagePlanId: !Ref 'MikrotikUsagePlan'
# setup custom api gateway response
  MikrotikApiGatewayResponse:
    Type: AWS::ApiGateway::GatewayResponse
    Properties:
      ResponseParameters:
        gatewayresponse.header.WWW-Authenticate: "'Basic'"
      ResponseType: UNAUTHORIZED
      RestApiId: !Ref mikrotikapi
      StatusCode: '401'
  AuthorizerLambdaApiPermission:
    Type: "AWS::Lambda::Permission"
    DependsOn: mikrotikapi
    Properties:
      Action: "lambda:invokeFunction"
      FunctionName: "{{lambdaddnsupdateauhtorizerarn}}"
      Principal: "apigateway.amazonaws.com"
      SourceArn: !Sub 
        - "arn:aws:execute-api:{{aws_mikrotik_cloudformation_api_region}}:{{caller_facts.account}}:${Api}/*"
        - Api: !Ref mikrotikapi
  # authorizer is created automatically by swagger definiton
  # MikrotikLambdaAuthorizer: 
  #   Type: AWS::ApiGateway::Authorizer
  #   DependsOn: AuthorizerLambdaApiPermission
  #   Properties: 
  #     AuthorizerResultTtlInSeconds: "300"
  #     AuthorizerUri: arn:aws:apigateway:{{aws_mikrotik_cloudformation_gateway_region}}:lambda:path/2015-03-31/functions/{{lambdaddnsupdateauhtorizerarn}}/invocations
  #     Type: "REQUEST"
  #     IdentitySource: "method.request.header.Authorization"
  #     Name: "MikrotikDDNSAUthorizer"
  #     RestApiId: 
  #       Ref: "mikrotikapi"
================================================

File: variables.vault.yaml
================================================
$ANSIBLE_VAULT;1.1;AES256
61336632313364326135333461343963333461373933633161386165316131623461616563356534
6131633963626635323435323032316634613833353431630a653231643430623763363536303866
38636665306439303565393966363435393361343330646265396564363832643332313031336139
3765643435373436330a643635626539393932663930303337363236653130396535633066376338
39323363346131643232363733373466666232313431396338393438306334623666323361353139
35393965393934326234356632626239656237653461333632636164356361323561306638633532
36376437323262663965646636363961663964383534653161633964633035363165323333323536
61383735623132343734343563326563313466343538633234653437633563343938376264316263
63663235383636643635663433366664376338623233343562373561383130343264376563643832
38353562303661636431353236383236323762303664316134316437396535303131333738636334
39376234323437346631313962356365323930303862646161356435313065396433353938383563
64366539353537613534663033303339613033393066643764323262666663646162336661303438
65656563346366333539316564656137373136653562326662613565313330656666383839323230
3263623564643163333331663432373666613230386462313666
================================================

File: variables.yaml
================================================
---
#
# variables for the api gateway management
#
##
# STACK configuration
##
# stack names
aws_mikrotik_api_stack_name_certificate: apimikrotikcertificate
aws_mikrotik_api_stack_name_gateway: apimikrotikgateway
aws_mikrotik_api_stack_name_api: apimikrotikapi
aws_mikrotik_api_stack_name_ddns_lambda: apimikrotikddnslambda
aws_mikrotik_api_stack_name_ddns_authorizer_lambda: apimikrotikddnsauthorizerlambda
# stack regions
aws_mikrotik_cloudformation_certificate_region: us-east-1
aws_mikrotik_cloudformation_gateway_region: eu-central-1
aws_mikrotik_cloudformation_api_region: eu-central-1
##
# Route 53 configuration
##
# route 53 zone for deployment
aws_mikrotik_route53_domain: mikrotik.ftscloud.ch
aws_mikrotik_route53_id: Z2A6C8O1POQXCB
aws_mikrotik_gateway_fqdn: "api.{{aws_mikrotik_route53_domain}}"
# https://docs.aws.amazon.com/general/latest/gr/rande.html#cf_region
aws_mikrotik_gateway_dns_zone: Z2FDTNDATAQYW2
##
# Lambda configuration
##
# ddns lambda
aws_mikrotik_ddns_lambda_code_bucket: ftsystemsmikrotikddnslambdacode
aws_mikrotik_ddns_lambda_function_name: MikrotikDDNSUpdate
aws_mikrotik_ddns_lambda_region: eu-central-1
aws_mikrotik_ddns_lambda_public_alias: public
aws_mikrotik_ddns_lambda_runtime: "python3.7"
aws_mikrotik_ddns_lambda_handler: ddns-update.handler
aws_mikrotik_ddns_lambda_env_domain: "{{aws_mikrotik_route53_domain}}"
aws_mikrotik_ddns_lambda_env_zoneid: "{{aws_mikrotik_route53_id}}"
aws_mikrotik_ddns_lambda_env_blacklist: "master,api"
# ddns authorizer lambda
aws_mikrotik_ddns_authorizer_lambda_code_bucket: ftsystemsmikrotikddnsauthorizerlambdacode
aws_mikrotik_ddns_authorizer_lambda_function_name: MikrotikDDNSUpdateAuthorizer
aws_mikrotik_ddns_authorizer_lambda_region: eu-central-1
aws_mikrotik_ddns_authorizer_lambda_fruntime: "python3.7"
aws_mikrotik_ddns_authorizer_lambda_fhandler: ddns-update-authorizer.handler
aws_mikrotik_ddns_authorizer_lambda_env_auth_username: "{{vault_aws_mikrotik_ddns_authorizer_lambda_env_auth_username}}"
aws_mikrotik_ddns_authorizer_lambda_env_auth_password: "{{vault_aws_mikrotik_ddns_authorizer_lambda_env_auth_password}}"