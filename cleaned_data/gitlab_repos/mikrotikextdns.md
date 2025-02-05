# Repository Information
Name: mikrotikextdns

# Files

File: .editorconfig
================================================
; https://editorconfig.org/
root = true
[*]
insert_final_newline = true
charset = utf-8
trim_trailing_whitespace = true
indent_style = space
indent_size = 2
[{Makefile,go.mod,go.sum,*.go,.gitmodules}]
indent_style = tab
indent_size = 4
[*.md]
indent_size = 4
trim_trailing_whitespace = false
eclint_indent_style = unset
[Dockerfile]
indent_size = 4
================================================

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
	url = https://gitlab.com/sebastianhutter/mikrotikextdns.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: build.yml
================================================
.golang:
  image: golang:1.16
  before_script:
    - mkdir -p ${GOPATH}/src/gitlab.com/sebastianhutter
    - ln -svf ${CI_PROJECT_DIR} ${GOPATH}/src/gitlab.com/sebastianhutter/${CI_PROJECT_NAME}
    - cd ${GOPATH}/src/gitlab.com/sebastianhutter/${CI_PROJECT_NAME}/
#  cache:
#    key: ${CI_COMMIT_REF_SLUG}
#    paths:
#      - go/pkg/mod/
  variables:
    CGO_ENABLED: 0
test:
  extends: .golang
  stage: test
  script:
    - go fmt $(go list ./... | grep -v /vendor/)
    - go vet $(go list ./... | grep -v /vendor/)
    - go test $(go list ./... | grep -v /vendor/)
compile:
  extends: .golang
  stage: build
  script:
    - GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o ${CI_PROJECT_DIR}/${CI_PROJECT_NAME}_linux_amd64
    - GOOS=darwin GOARCH=amd64 go build -ldflags="-w -s" -o ${CI_PROJECT_DIR}/${CI_PROJECT_NAME}_darwin_amd64
    - GOOS=windows GOARCH=amd64 go build -ldflags="-w -s" -o ${CI_PROJECT_DIR}/${CI_PROJECT_NAME}_windows_amd64
  needs:
    - test
  artifacts:
    paths:
      - ${CI_PROJECT_NAME}_linux_amd64
      - ${CI_PROJECT_NAME}_darwin_amd64
      - ${CI_PROJECT_NAME}_windows_amd64
    expire_in: 1 month
================================================

File: package.yml
================================================
.docker:
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
  script:
    - |
      if [[ "$CI_COMMIT_BRANCH" == "$CI_DEFAULT_BRANCH" ]]; then
        tag="latest"
        echo "Running on default branch '$CI_DEFAULT_BRANCH': tag = 'latest'"
      else
        tag="$CI_COMMIT_REF_NAME"
        echo "Running on branch '$CI_COMMIT_BRANCH': tag = $tag"
      fi
    - docker build --pull -t "$CI_REGISTRY_IMAGE:${tag}" .
    - docker tag "$CI_REGISTRY_IMAGE:${tag}" $CI_REGISTRY_IMAGE:${CI_COMMIT_SHORT_SHA}
    - docker push "$CI_REGISTRY_IMAGE:${tag}"
    - docker push "$CI_REGISTRY_IMAGE:${CI_COMMIT_SHORT_SHA}"
package:docker:
  extends: .docker
  stage: package
  needs:
    - job: compile
      artifacts: true
package:helm:
  stage: package
  needs:
    - job: compile
      artifacts: false
  script:
    - tar -czf charts.tar.gz charts
  artifacts:
    paths:
      - charts.tar.gz
    expire_in: 1 month
================================================

File: release.yml
================================================
prerelease:upload:
  stage: prerelease
  image: curlimages/curl:latest
  needs:
    - job: compile
      artifacts: true
    - job: "package:helm"
      artifacts: true
  rules:
    - if: $CI_COMMIT_TAG
  variables:
    PACKAGE_REGISTRY_URL: "${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/generic/${CI_PROJECT_NAME}/${CI_COMMIT_TAG}"
  script:
    - |
      curl --header "JOB-TOKEN: ${CI_JOB_TOKEN}" --upload-file ${CI_PROJECT_NAME}_linux_amd64 ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_linux_amd64
    - |
      curl --header "JOB-TOKEN: ${CI_JOB_TOKEN}" --upload-file ${CI_PROJECT_NAME}_darwin_amd64 ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_darwin_amd64
    - |
      curl --header "JOB-TOKEN: ${CI_JOB_TOKEN}" --upload-file ${CI_PROJECT_NAME}_windows_amd64 ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_windows_amd64
    - |
      curl --header "JOB-TOKEN: ${CI_JOB_TOKEN}" --upload-file charts.tar.gz ${PACKAGE_REGISTRY_URL}/charts.tar.gz
release:
  stage: release
  image: registry.gitlab.com/gitlab-org/release-cli:latest
  rules:
    - if: $CI_COMMIT_TAG                  # Run this job when a tag is created manually
  script:
    - echo 'running release_job'
  needs:
    - job: "prerelease:upload"
      artifacts: false
  variables:
    PACKAGE_REGISTRY_URL: "${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/generic/${CI_PROJECT_NAME}/${CI_COMMIT_TAG}"
  release:
    name: 'Release $CI_COMMIT_TAG'
    description: './CHANGELOG.md'
    tag_name: '$CI_COMMIT_TAG'
    ref: '$CI_COMMIT_TAG'
    assets: # Optional, multiple asset links
      links:
        - name: ${CI_PROJECT_NAME}_linux_amd64
          url: ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_linux_amd64
        - name: ${CI_PROJECT_NAME}_darwin_amd64
          url: ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_darwin_amd64
        - name: ${CI_PROJECT_NAME}_windows_amd64
          url: ${PACKAGE_REGISTRY_URL}/${CI_PROJECT_NAME}_windows_amd64
        - name: charts.tar.gz
          url: ${PACKAGE_REGISTRY_URL}/charts.tar.gz
================================================

File: .gitlab-ci.yml
================================================
include:
  - local: '.gitlab-ci/build.yml'
  - local: '.gitlab-ci/package.yml'
  - local: '.gitlab-ci/release.yml'
stages:
  - test
  - build
  - package
  - prerelease
  - release
================================================

File: CHANGELOG.md
================================================
# Changelog
## 0.2.0
* create mikrotik dns entries with comment to ensure service does not remove or overwrite *unmanaged* entries
* add prometheus instrumentation
  * add upserts and delete counters
* add prometheus service monitor (.Values.prometheus.enabled)
## 0.1.0
* initial working release
* helm chart for deployment
================================================

File: Chart.yaml
================================================
apiVersion: v2
name: mikrotikextdns
description: A Helm chart for Kubernetes
# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and therefore cannot be deployed.
type: application
# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
version: 0.2.1
# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application. Versions are not expected to
# follow Semantic Versioning. They should reflect the version the application is using.
# It is recommended to use it with quotes.
appVersion: "0.2.1"
================================================

File: deployment.yaml
================================================
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mikrotixextdns.fullname" . }}
  labels:
    {{- include "mikrotixextdns.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "mikrotixextdns.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      {{- with .Values.podAnnotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "mikrotixextdns.selectorLabels" . | nindent 8 }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "mikrotixextdns.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: metrics
              containerPort: 2112
              protocol: TCP
#          livenessProbe:
#            httpGet:
#              path: /
#              port: http
#          readinessProbe:
#            httpGet:
#              path: /
#              port: http
          env:
            - name: MIKROTIK_ADDRESS
              value: {{ .Values.app.mikrotik.address | quote }}
            - name: MIKROTIK_USERNAME
              value: {{ .Values.app.mikrotik.username | quote }}
            - name: MIKROTIK_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.app.mikrotik.secret | quote }}
                  key: mikrotik_password
            - name: NAMESPACES
              value: {{ .Values.app.namespaces | quote }}
            - name: LOGLEVEL
              value: {{ .Values.app.loglevel | quote }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
================================================

File: prometheus.yaml
================================================
{{- if .Values.prometheus.enabled }}
apiVersion: v1
kind: Service
metadata:
  name: {{ include "mikrotixextdns.fullname" . }}-prometheus
  labels:
    {{- include "mikrotixextdns.labels" . | nindent 4 }}
spec:
  selector:
    {{- include "mikrotixextdns.selectorLabels" . | nindent 6 }}
  ports:
    - name: metrics
      protocol: TCP
      port: 2112
      targetPort: 2112
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: {{ include "mikrotixextdns.fullname" . }}-prometheus
spec:
  selector:
    matchLabels:
      {{- include "mikrotixextdns.selectorLabels" . | nindent 6 }}
  endpoints:
    - port: "metrics"
      path: "/metrics"
{{- end }}
================================================

File: serviceaccount.yaml
================================================
{{- if .Values.serviceAccount.create -}}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ include "mikrotixextdns.serviceAccountName" . }}
  labels:
    {{- include "mikrotixextdns.labels" . | nindent 4 }}
  {{- with .Values.serviceAccount.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: {{ include "mikrotixextdns.clusterRoleName" . }}
rules:
  - apiGroups:
      - networking.k8s.io
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: {{ include "mikrotixextdns.clusterRoleName" . }}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: {{ include "mikrotixextdns.clusterRoleName" . }}
subjects:
  - kind: ServiceAccount
    name: {{ include "mikrotixextdns.serviceAccountName" . }}
    namespace: {{ .Release.Namespace }}
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: {{ include "mikrotixextdns.roleName" . }}
rules:
  - apiGroups:
      - ""
    resources:
      - secrets
    verbs:
      - get
      - list
      - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: {{ include "mikrotixextdns.roleName" . }}
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: {{ include "mikrotixextdns.roleName" . }}
subjects:
  - kind: ServiceAccount
    name: {{ include "mikrotixextdns.serviceAccountName" . }}
    namespace: {{ .Release.Namespace }}
{{- end }}
================================================

File: prometheus-connection.yaml
================================================
{{- if .Values.prometheus.enabled }}
apiVersion: v1
kind: Pod
metadata:
  name: "{{ .Release.Name }}-prometheus-test"
  annotations:
    "helm.sh/hook": test-success
spec:
  containers:
    - name: {{ .Release.Name }}-prometheus-test
      image: busybox
      imagePullPolicy: {{ .Values.image.pullPolicy | quote }}
      {{- if .Values.securityContext.enabled }}
      securityContext:
        runAsUser: {{ .Values.securityContext.runAsUser }}
      {{- end }}
      command:
        - /bin/sh
        - -ec
        - |
          wget --timeout=5 {{ include "mikrotixextdns.fullname" . }}-prometheus:2112/metrics
  restartPolicy: Never
  {{- end }}
================================================

File: values.yaml
================================================
# Default values for mikrotixextdns.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.
app:
  loglevel: info
  # listen for ingress changes in namespaces, "" = all namespaces
  namespaces: ""
  mikrotik:
    address: "192.168.0.1:8728"
    username: "admin"
    # please specify an existing secret name
    # the key in the secret needs to be "mikrotik_password"
    secret: ""
# assumption is prometheus controller is installed and service monitor crd is available
prometheus:
  enabled: true
replicaCount: 1
image:
  repository: registry.gitlab.com/sebastianhutter/mikrotikextdns
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: ""
imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""
serviceAccount:
  # Specifies whether a service account should be created
  create: true
  # Annotations to add to the service account
  annotations: {}
  # The name of the service account to use.
  # If not set and create is true, a name is generated using the fullname template
  name: ""
podAnnotations: {}
podSecurityContext: {}
  # fsGroup: 2000
securityContext: {}
  # capabilities:
  #   drop:
  #   - ALL
  # readOnlyRootFilesystem: true
  # runAsNonRoot: true
  # runAsUser: 1000
resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #   cpu: 100m
  #   memory: 128Mi
  # requests:
  #   cpu: 100m
  #   memory: 128Mi
autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 100
  targetCPUUtilizationPercentage: 80
  # targetMemoryUtilizationPercentage: 80
nodeSelector: {}
tolerations: []
affinity: {}
================================================

File: Dockerfile
================================================
FROM scratch
ADD mikrotikextdns_linux_amd64 /mikrotikextdns
ENTRYPOINT [ "/mikrotikextdns" ]
================================================

File: TODO.md
================================================
# TODO
* add health endpoints for liveness and readiness checks
* package helm chart and release in helm registry