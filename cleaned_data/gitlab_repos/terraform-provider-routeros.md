# Repository Information
Name: terraform-provider-routeros

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
	url = https://gitlab.com/github-ujstor/terraform-provider-routeros.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: dependabot.yml
================================================
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"
      time: "03:00"
    labels:
      - "dependencies"
  - package-ecosystem: gomod
    directory: /
    schedule:
      interval: daily
    labels:
      - "dependencies"
================================================

File: bug_report.md
================================================
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''
---
**Describe the bug**
A clear and concise description of what the bug is.
**To Reproduce**
Steps to reproduce the behavior and the problem section from the TF file, without sensitive information.
**Expected behavior**
A clear and concise description of what you expected to happen.
**Debug Information**
If needed, be ready to publish debug output of the provider (green lines after executing `TF_LOG=debug ROS_LOG_COLOR=1 terraform <command>`).
**Stack Trace**
If applicable, add the stack trace the crash produced.
**Additional context**
Add any other context about the problem here.
================================================

File: ci-pipeline-issue.md
================================================
---
name: CI Pipeline issue
about: Bugs with the CI pipeline, either release or testing
title: ''
labels: Non-functional
assignees: ''
---
**Which pipeline fails?:**
**What job does the pipeline fail on?:**
================================================

File: documentation-update.md
================================================
---
name: Documentation Update
about: Updates and modifications to the documentation
title: ''
labels: documentation, Non-functional
assignees: ''
---
**What documentation needs updating?:**
For example:
- README
- CHANGELOG
- Provider
**What needs to be added to the documentation?:**
For example:
Resource `routeros_interface_wireguard` needs to show how to set a public key.
================================================

File: feature_request.md
================================================
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''
---
**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
**Describe the solution you'd like**
A clear and concise description of what you want to happen.
**Documentation**
If there is [documentation](https://help.mikrotik.com/docs/display/ROS/RouterOS) describing the new resource, add it.
**Additional context**
Add any other context or screenshots about the feature request here.
================================================

File: setup_routeros.go
================================================
package main
import (
	"log"
	"os"
	"strings"
	"time"
	"github.com/go-routeros/routeros"
)
var (
	commands = []string{
		"/certificate/add name=ssl common-name=router key-size=prime256v1",
		"/certificate/sign .id=ssl",
		"/ip/service/set .id=www-ssl disabled=no certificate=ssl",
		"/ip/service/set .id=api-ssl disabled=no certificate=ssl",
		"/interface/bridge/add name=bridge",
		"/ip/pool/add name=dhcp ranges=192.168.88.100-192.168.88.200",
		"/interface/wireguard/add name=wg1",
		"/interface/list/add name=list",
	}
)
func main() {
	username := os.Getenv("ROS_USERNAME")
	password := os.Getenv("ROS_PASSWORD")
	host := os.Getenv("ROS_IP_ADDRESS")
	var err error
	var client *routeros.Client
	for i := 0; i < 12; i++ {
		log.Printf("Connection attempt #%v... ", i)
		client, err = routeros.Dial(host+":8728", username, password)
		if err == nil {
			break
		}
		log.Println(err)
		time.Sleep(5 * time.Second)
	}
	if err != nil {
		log.Fatal("Host is not available")
	}
	defer client.Close()
	for _, command := range commands {
		cmd := strings.Split(command, " ")
		for i, c := range cmd {
			if strings.ContainsRune(c, '=') && len(c) > 0 && c[0] != '=' {
				cmd[i] = "=" + c
			}
		}
		log.Println(cmd)
		res, err := client.RunArgs(cmd)
		if err != nil {
			log.Fatal(err)
		}
		log.Println(res)
	}
}
================================================

File: setup_routeros.py
================================================
#!/usr/bin/env python3
import routeros_api
import os
def main():
    user = os.environ.get("ROS_USERNAME")
    pswd = os.environ.get("ROS_PASSWORD")
    ip_addr = os.environ.get("ROS_IP_ADDRESS")
    connection = routeros_api.RouterOsApiPool(
        ip_addr, username=user, password=pswd, port=8728, plaintext_login=True)
    api = connection.get_api()
    # Set up bridge
    bridge = api.get_resource("/interface/bridge")
    bridge.add(name="bridge")
    # Set up certificates to allow use of REST API
    certificate = api.get_resource("/certificate")
    certificate.add(name="root-cert", common_name="MyRouter",
                    days_valid="3650", key_usage="key-cert-sign,crl-sign")
    certificate.add(name="https-cert",
                    common_name="MyRouter", days_valid="3650")
    certs = certificate.get()
    root_cert_id = [x['id'] for x in certs if x['name'] == "root-cert"][0]
    http_cert_id = [x['id'] for x in certs if x['name'] == "https-cert"][0]
    api.get_binary_resource("/").call("certificate/sign",
                                      {"id": bytes(root_cert_id, "utf-8")})
    api.get_binary_resource("/").call("certificate/sign",
                                      {"id": bytes(http_cert_id, "utf-8"), "ca": b"root-cert"})
    services = api.get_resource("/ip/service")
    for x in services.get():
        if x['name'] in ['www-ssl', 'api-ssl']:
            services.set(id=x['id'],certificate="https-cert", disabled="false")
    # Create a DHCP pool
    pools = api.get_resource("/ip/pool")
    pools.add(name="dhcp", ranges="192.168.88.100-192.168.88.200")
    wireguard = api.get_resource("/interface/wireguard")
    wireguard.add(name="wg1")
    # Create a interface list
    list = api.get_resource("/interface/list")
    list.add(name="list")
    # Output the list of interfaces
    print(api.get_resource("/interface").get())
if __name__ == "__main__":
    main()
================================================

File: module_testing.yml
================================================
name: Go Client Tests
on:
  pull_request:
    branches:
      - 'main'
      - 'devel'
    paths:
      - 'main.go'
      - 'routeros/*.go'
      - '.github/workflows/*.yml'
jobs:
  build:
    name: Build
    runs-on: ${{ matrix.os }}
    continue-on-error: ${{ matrix.experimental }}
    strategy:
      matrix:
        experimental: [false]
        go:
          - 1.21
        os: [ubuntu-latest]
        routeros_version:
          - "7.12"
          - "7.13"
          - "7.14"
    steps:
      - name: Check out code into the Go module directory
        uses: actions/checkout@v4
      - name: Setup Go environment
        uses: actions/setup-go@v5
        with:
          go-version: ${{ matrix.go }}
        id: go  
      - name: Get dependencies
        run: | 
          go mod download
      - name: Build
        run: go build -v .
      - name: Preparing RouterOS for testing
        run: |
          go run .github/scripts/setup_routeros.go
        env:
          ROS_USERNAME: admin
          ROS_PASSWORD: ''
          ROS_IP_ADDRESS: 127.0.0.1
      - name: Run client tests
        run: go test -timeout 30m -v ./routeros
        env:
          ROS_HOSTURL: https://127.0.0.1
          ROS_USERNAME: admin
          ROS_PASSWORD: ''
          ROS_INSECURE: true
          TF_ACC: 1
          ROS_VERSION: ${{ matrix.routeros_version }}
    services:
      routeros:
        image: vaerhme/routeros:v${{ matrix.routeros_version }}
        ports:
          - 443:443
          - 8728:8728
          - 8729:8729
        volumes:
          - /dev/net/tun:/dev/net/tun
        options: >-
          --cap-add=NET_ADMIN
          --entrypoint /routeros/entrypoint_with_four_interfaces.sh
================================================

File: release.yml
================================================
# This uses an action (crazy-max/ghaction-import-gpg) that assumes you set your
# private key in the `GPG_PRIVATE_KEY` secret and passphrase in the `PASSPHRASE`
# secret. If you would rather own your own GPG handling, please fork this action
# or use an alternative one for key handling.
#
# You will need to pass the `--batch` flag to `gpg` in your signing step
# in `goreleaser` to indicate this is being used in a non-interactive mode.
#
name: Release
on:
  workflow_dispatch:
  push:
    branches:
      - 'main'
      - 'devel'
    tags-ignore:
      - '**'
jobs:
  release:
    if: contains(github.event.head_commit.message, 'chore(release)') != true
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # otherwise, you will failed to push refs to dest repo
          persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
          token: ${{ secrets.ROUTEROS_ACTIONS }}
      - name: Import GPG key
        id: import_gpg
        uses: crazy-max/ghaction-import-gpg@v6
        with:
          # These secrets will need to be configured for the repository:
          gpg_private_key: ${{ secrets.TERRAFORM_GPG_SIGNING_KEY }}
          passphrase: ${{ secrets.TERRAFORM_GPG_SIGN_KEY_PW }}
      - name: Release
        id: release
        uses: cycjimmy/semantic-release-action@v4
        with:
          extra_plugins: |
            "@semantic-release/changelog@6.0.2"
            "@semantic-release/commit-analyzer@9.0.2"
            "@semantic-release/exec@6.0.3"
            "@semantic-release/git@10.0.1"
            "@semantic-release/github@8.0.7"
            "@semantic-release/release-notes-generator@10.0.3"
            "conventional-changelog-conventionalcommits@5.0.0"
        env:
          GITHUB_TOKEN: ${{ secrets.ROUTEROS_ACTIONS }}
          GPG_FINGERPRINT: ${{ steps.import_gpg.outputs.fingerprint }}
      - name: Set up Go
        if: steps.release.outputs.new_release_published == 'true'
        uses: actions/setup-go@v5
        with:
          go-version: 1.21
      - name: Run GoReleaser
        if: steps.release.outputs.new_release_published == 'true'
        uses: goreleaser/goreleaser-action@v6
        with:
          version: latest
          args: release --clean
        env:
          GPG_FINGERPRINT: ${{ steps.import_gpg.outputs.fingerprint }}
          # GitHub sets this automatically
          GITHUB_TOKEN: ${{ secrets.ROUTEROS_ACTIONS }}
================================================

File: .goreleaser.yml
================================================
# Visit https://goreleaser.com for documentation on how to customize this
# behavior.
before:
  hooks:
    # this is just an example and not a requirement for provider building/publishing
    - go mod tidy
builds:
  - env:
      # goreleaser does not work with CGO, it could also complicate
      # usage by users in CI/CD systems like Terraform Cloud where
      # they are unable to install libraries.
      - CGO_ENABLED=0
    mod_timestamp: "{{ .CommitTimestamp }}"
    flags:
      - -trimpath
    ldflags:
      - "-s -w -X main.version={{.Version}} -X main.commit={{.Commit}}"
    goos:
      - freebsd
      - windows
      - linux
      - darwin
    goarch:
      - amd64
      - "386"
      - arm
      - arm64
    ignore:
      - goos: darwin
        goarch: "386"
    binary: "{{ .ProjectName }}_v{{ .Version }}"
archives:
  - format: zip
    name_template: "{{ .ProjectName }}_{{ .Version }}_{{ .Os }}_{{ .Arch }}"
checksum:
  name_template: "{{ .ProjectName }}_{{ .Version }}_SHA256SUMS"
  algorithm: sha256
signs:
  - artifacts: checksum
    args:
      # if you are using this is a GitHub action or some other automated pipeline, you
      # need to pass the batch flag to indicate its not interactive.
      - "--batch"
      - "--local-user"
      - "{{ .Env.GPG_FINGERPRINT }}" # set this environment variable for your signing key
      - "--output"
      - "${signature}"
      - "--detach-sign"
      - "${artifact}"
release:
  prerelease: auto
================================================

File: CHANGELOG.md
================================================
## [1.59.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.59.2...v1.59.3) (2024-08-12)
### Bug Fixes
* Add missing attributes, add fields to ignore. Fix wrong `new_dst_ports` type ([c570002](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c570002b40171054b85b62a1e59b2dc907791100)), closes [#538](https://github.com/terraform-routeros/terraform-provider-routeros/issues/538)
* **netwatch:** Add `http_codes` attribute to skip fields. ([e7d0356](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e7d03563143c4a70e7052cb8652513f375e4bfb3))
## [1.59.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.59.1...v1.59.2) (2024-08-07)
### Bug Fixes
* Can not set rtt parameters in `routeros_tool_netwatch` ([afa971e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/afa971e337f6141c4dfa717c791807a52ffc0692)), closes [#535](https://github.com/terraform-routeros/terraform-provider-routeros/issues/535)
## [1.59.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.59.0...v1.59.1) (2024-08-07)
### Bug Fixes
* **bridge_port:** Fix the `priority` attribute type. ([4f342fb](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4f342fb0fcedce97f0dbff806f0c60a6ed072b8b)), closes [#528](https://github.com/terraform-routeros/terraform-provider-routeros/issues/528)
* **firewall_raw:** "no track" action in routeros_ip_firewall_raw needs tweaking ([9d46a55](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9d46a5503163b60534d63f414ddfd1b1a50ea631)), closes [#529](https://github.com/terraform-routeros/terraform-provider-routeros/issues/529)
* **wireguard_peer:** Need new filed 'is-responder' in resource 'routeros_interface_wireguard_peer' ([a31a394](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a31a394e3abd8bcab3af06d6ab35d4b4f0abc89a)), closes [#530](https://github.com/terraform-routeros/terraform-provider-routeros/issues/530)
## [1.59.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.58.2...v1.59.0) (2024-08-05)
### Features
* Add `routeros_routing_rule` resource ([a263193](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a26319308ae96b41fd0ffe291fb62073459378f7)), closes [#524](https://github.com/terraform-routeros/terraform-provider-routeros/issues/524)
* Add `routeros_tool_netwatch` resource ([2150241](https://github.com/terraform-routeros/terraform-provider-routeros/commit/215024137033233ab13a22ae731ef8a72f4a3612)), closes [#487](https://github.com/terraform-routeros/terraform-provider-routeros/issues/487)
## [1.58.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.58.1...v1.58.2) (2024-08-04)
### Bug Fixes
* **interface_lte:** Add missing attributes ([f67e8d9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f67e8d90242b0b1e0f9c630cf0ffd37a819bd049)), closes [#522](https://github.com/terraform-routeros/terraform-provider-routeros/issues/522)
* **ip_firewall:** Deleting routeros_ip_firewall_filter.in_interface tries to PATCH ([2189054](https://github.com/terraform-routeros/terraform-provider-routeros/commit/21890540901501e7f8da61eb23a452ad52791f44)), closes [#521](https://github.com/terraform-routeros/terraform-provider-routeros/issues/521)
* **ipv4_nat:** Need new filed 'randomise_ports' in action 'endpoint-independent-nat' ([51e161d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/51e161d5b090762fed7bd6f638d36f9d31564ddc)), closes [#520](https://github.com/terraform-routeros/terraform-provider-routeros/issues/520)
## [1.58.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.58.0...v1.58.1) (2024-08-02)
### Bug Fixes
* resource_system_logging missing topics and excluding Fixes [#518](https://github.com/terraform-routeros/terraform-provider-routeros/issues/518) ([2805dc3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/2805dc35453f8b8051bb9b612814d5fef34a31df))
* routeros_system_logging_action and default settings ([1a5d02c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1a5d02ce5a8b27bdb97ba38f241db24627621882)), closes [#517](https://github.com/terraform-routeros/terraform-provider-routeros/issues/517)
## [1.58.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.57.2...v1.58.0) (2024-07-31)
### Features
* **lte:** Add LTE resources ([fcaf349](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fcaf3495a50f3cabed77c240de9604d4d5347b3e)), closes [#464](https://github.com/terraform-routeros/terraform-provider-routeros/issues/464)
### Bug Fixes
* **ethernet:** Schema Error on SFP Ports ([01e4c11](https://github.com/terraform-routeros/terraform-provider-routeros/commit/01e4c119d86ade3cfaf040e3deb68749f14282b5)), closes [#514](https://github.com/terraform-routeros/terraform-provider-routeros/issues/514)
* **firewall_nat:** add NAT firewall action "endpoint-independent-nat" ([d55b30d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d55b30d07ef8f9c2d7c3b53088c8224e819907d9)), closes [#516](https://github.com/terraform-routeros/terraform-provider-routeros/issues/516)
* **system_logging:** Bugfix in routeros_system_logging ([aa1d376](https://github.com/terraform-routeros/terraform-provider-routeros/commit/aa1d3762000006aac00d13a7ae74ee5330c0245f)), closes [#515](https://github.com/terraform-routeros/terraform-provider-routeros/issues/515)
## [1.57.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.57.1...v1.57.2) (2024-07-30)
### Bug Fixes
* **certificate:** Certificate import ambiguous value of file-name ([01f4294](https://github.com/terraform-routeros/terraform-provider-routeros/commit/01f4294a2898ecdceb4772db048dd620fa9a221e)), closes [#511](https://github.com/terraform-routeros/terraform-provider-routeros/issues/511)
## [1.57.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.57.0...v1.57.1) (2024-07-30)
### Bug Fixes
* **ospf_interface_template:** RouterOS 7.x & OSPF Interface Template Auth Key ([995ba46](https://github.com/terraform-routeros/terraform-provider-routeros/commit/995ba46e8d8f8fc11c9d47a300f36879876c285f)), closes [#510](https://github.com/terraform-routeros/terraform-provider-routeros/issues/510)
## [1.57.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.56.0...v1.57.0) (2024-07-23)
### Features
* Update the `routeros_ovpn_server` resource to support multiple values ([668ef09](https://github.com/terraform-routeros/terraform-provider-routeros/commit/668ef0986404bea864150b64509b86f43e5b4494))
### Bug Fixes
* **ipv6_neighbor_discovery:** Change the schema attributes ([9688bab](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9688babe485e51b2acc981b6e8a8bb8edd26e98a)), closes [#509](https://github.com/terraform-routeros/terraform-provider-routeros/issues/509)
* Update the `routeros_ovpn_server` resource to handle default values correctly ([f377a26](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f377a2615219baed70ffc779f9be0fe022e42712))
## [1.56.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.55.0...v1.56.0) (2024-07-04)
### Features
* Add `enable_ipv6_accounting` introduced in 7.15 to the `routeros_ppp_aaa` resource ([4c792c7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4c792c74a4d5e5de43fc5c62176ea6f74925336c))
* Add `require_message_auth` introduced in 7.15 to the `routeros_radius` resource ([6946d95](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6946d95654b504dbc214d046dbab0723dbdb4e0d))
* Add `require_message_auth` introduced in 7.15 to the `routeros_user_manager_settings` resource ([91b41b7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/91b41b7b3c184ec1f0c2cede4e61fadc437171a2))
* Add `reselect_interval` introduced in 7.15 to the `routeros_wifi_channel` resource ([77186c0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/77186c0fbc478c2e8c4a06bc1b5e330e5db402ac))
* Add `sfp_ignore_rx_los` introduced in 7.15 to the `routeros_interface_ethernet` resource ([a361715](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a36171577d57a5af9050cf8e57639f962c5f4ae8))
* Add current CAPsMAN identity computed properties introduced in 7.15 to the `routeros_wifi_cap` resource ([f0fae7b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f0fae7baf1771b6f65665269794bc68a25b40e23))
### Bug Fixes
* Fix the `AlwaysPresentNotUserProvided` helper to ignore stored empty values as RouterOS started returning such in 7.15 ([c22e017](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c22e017534a6024a35d530d8da689a69ce07f360))
## [1.55.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.54.3...v1.55.0) (2024-07-02)
### Features
* Add state migrator helper to convert scalar values to lists ([858ecab](https://github.com/terraform-routeros/terraform-provider-routeros/commit/858ecab2b52c8933051c2ae992d272969b90c6be))
* Update properties in `routeros_interface_dot1x_client` and `routeros_interface_dot1x_server` to support multiple values ([66ab1d2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/66ab1d2cec80d8c677190315d258b47ca9fe50fa))
* Update properties in `routeros_ip_dhcp_server_network` to support multiple values ([bc1cf68](https://github.com/terraform-routeros/terraform-provider-routeros/commit/bc1cf68b5f3126f0f19bd3f4b4288cc269f25f67))
* Update the `servers` property in `routeros_dns` to support multiple values ([ea25f00](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ea25f0088d2da7dfaa001fab0b06c0bc67bbc847))
* Update the `service` property in `routeros_radius` to support multiple values ([a1becca](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a1beccacd612960abb27b4c66c4941e0e3f0cf4c))
* Update the `vlan_ids` property in `routeros_interface_bridge_vlan` to support multiple values ([3ec3d34](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3ec3d343d9ed0bf501624fae89aae5840da8fa8e))
* Update the frequency properties in `routeros_capsman_channel` to support multiple values ([14a6e4e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/14a6e4e45a91be4f4811f97a7696c25460e1313b))
### Bug Fixes
* Add state migrator to `routeros_snmp_community` to fix backward compatibility ([27c8588](https://github.com/terraform-routeros/terraform-provider-routeros/commit/27c858806bdf9f79bf96a4cd5e85746abc2b2e99))
* Fix `tagged` and `untagged` properties in `routeros_interface_bridge_vlan` to ignore values order ([eb8ff28](https://github.com/terraform-routeros/terraform-provider-routeros/commit/eb8ff28b6c125f20c45ebb783ed248a28f72b935))
* Fix `topics` property type in `routeros_system_logging` to ignore values order ([0e3c29f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0e3c29f62f587db7b340fee8299c6ec0a3622898))
## [1.54.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.54.2...v1.54.3) (2024-06-27)
### Features
* **no-release:** Added ipv6 filter data ([#496](https://github.com/terraform-routeros/terraform-provider-routeros/issues/496)) ([6d45e88](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6d45e88d0af4e99fd552754835d865a034bb54ac))
* **no-release:** Support Multiple VLAN Registration protocol (MVRP). ([#497](https://github.com/terraform-routeros/terraform-provider-routeros/issues/497)) ([0dc994a](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0dc994aed90ed6453dbe422b0ede093b1fae08c7)), closes [#492](https://github.com/terraform-routeros/terraform-provider-routeros/issues/492) [#493](https://github.com/terraform-routeros/terraform-provider-routeros/issues/493)
### Bug Fixes
* Field 'vrf' not found in the schema (introduced in 7.15) ([563401b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/563401bc8c8b8b980afdbd2ad36c424ad8134ebb)), closes [#490](https://github.com/terraform-routeros/terraform-provider-routeros/issues/490)
* **no-release:** Allow a set of `addresses` ([#498](https://github.com/terraform-routeros/terraform-provider-routeros/issues/498)) ([bcf417f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/bcf417f491090bad60cb4f2a9fe313c146259d19)), closes [#495](https://github.com/terraform-routeros/terraform-provider-routeros/issues/495)
* **no-release:** nil resources ([#486](https://github.com/terraform-routeros/terraform-provider-routeros/issues/486)) ([8571dea](https://github.com/terraform-routeros/terraform-provider-routeros/commit/8571dea493a5a22d167c083e65e744f97a50c05b))
* **routeros_interface_wireguard_peer:** Field 'name' not found in the schema (introduced in 7.15) ([9fb13ad](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9fb13ad7523be815ae41cd5b35c5d7e889e02a9e)), closes [#494](https://github.com/terraform-routeros/terraform-provider-routeros/issues/494)
* **routeros_ip_neighbor_discovery_settings:** Multiple fields not found in schema (introduced in 7.15) ([7f44443](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7f44443784cfe5b4372c7af7aee1da94acc0d1c1)), closes [#491](https://github.com/terraform-routeros/terraform-provider-routeros/issues/491)
## [1.54.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.54.1...v1.54.2) (2024-06-04)
### Bug Fixes
* **fw-mangle:** Fix `dst_address_list` validation ([0eb25c9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0eb25c973c2022704a1f85670f125fb5c772388b)), closes [#480](https://github.com/terraform-routeros/terraform-provider-routeros/issues/480)
## [1.54.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.54.0...v1.54.1) (2024-05-30)
### Bug Fixes
* **vrrp:** Add `group-authority` attribute handling to the `group-master` replacement ([58cf139](https://github.com/terraform-routeros/terraform-provider-routeros/commit/58cf139015490181973170d97d1e3931919b1af0)), closes [#446](https://github.com/terraform-routeros/terraform-provider-routeros/issues/446)
## [1.54.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.53.0...v1.54.0) (2024-05-29)
### Features
* Add bandwidth server resource ([#475](https://github.com/terraform-routeros/terraform-provider-routeros/issues/475)) ([d98ce0f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d98ce0f3aeb918ca02cbfc42eef6b9ba98ef7382)), closes [#474](https://github.com/terraform-routeros/terraform-provider-routeros/issues/474)
## [1.53.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.52.1...v1.53.0) (2024-05-29)
### Features
* **logging-action:** Support for logging actions setup ([f8b9824](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f8b9824a1f00ee456ab3a87793900922942daf42)), closes [#477](https://github.com/terraform-routeros/terraform-provider-routeros/issues/477)
### Bug Fixes
* **certificate-scep-server:** Rename the resource from "routeros_certificate_scep_server" to "routeros_system_certificate_scep_server" ([a9a8138](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a9a81385f2280fa1485d142b7c1e1d9dde541aff)), closes [#473](https://github.com/terraform-routeros/terraform-provider-routeros/issues/473)
## [1.52.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.52.0...v1.52.1) (2024-05-28)
### Bug Fixes
* **firewall-raw:** Fix resource name ([e956f9f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e956f9ff5d72478f65e4db3e86808f689d0b3a40))
## [1.52.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.51.0...v1.52.0) (2024-05-28)
### Features
* **firewall/raw:** Add new resource ([90eb2fa](https://github.com/terraform-routeros/terraform-provider-routeros/commit/90eb2fa762a92e61bdb408095f7c2ef5a1c03e8e)), closes [#462](https://github.com/terraform-routeros/terraform-provider-routeros/issues/462)
### Bug Fixes
* **dhcp-server:** Remove default values ([#470](https://github.com/terraform-routeros/terraform-provider-routeros/issues/470)) ([884e464](https://github.com/terraform-routeros/terraform-provider-routeros/commit/884e464d7f16f016b99c12371c2cbfca84a149fb)), closes [#466](https://github.com/terraform-routeros/terraform-provider-routeros/issues/466)
## [1.51.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.50.0...v1.51.0) (2024-05-21)
### Features
* **x509:** Datasource for PEM data normalization and common_name extraction ([5f29176](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5f29176d8109379bea87eeb65e8b49cbbc0ceffb))
* **x509:** Import certificates ([5a3bf8e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5a3bf8ed177e984a7b52322bd70a25431bfb42cd)), closes [#448](https://github.com/terraform-routeros/terraform-provider-routeros/issues/448)
## [1.50.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.49.0...v1.50.0) (2024-05-17)
### Features
* **ovpn:** Add routeros_interface_ovpn_client ([85fd6be](https://github.com/terraform-routeros/terraform-provider-routeros/commit/85fd6be76bfb5a474f419ff226a969a40bc90c92)), closes [#452](https://github.com/terraform-routeros/terraform-provider-routeros/issues/452)
## [1.49.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.48.3...v1.49.0) (2024-05-17)
### Features
* **clock:** Add routeros_system_clock ([e7b3131](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e7b3131606bb1fb6e957c3e4ed68f352f674fa23)), closes [#453](https://github.com/terraform-routeros/terraform-provider-routeros/issues/453)
### Bug Fixes
* **vrf:** Change import method ([915df28](https://github.com/terraform-routeros/terraform-provider-routeros/commit/915df28f7489e35b97c401f1ff4b8fbe1a223826))
* Warnings ([7fe815b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7fe815b91311a4b62ca0f42940b8cbdca938fbea))
## [1.48.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.48.2...v1.48.3) (2024-05-14)
### Bug Fixes
* Add comment to routeros_wifi resource ([#455](https://github.com/terraform-routeros/terraform-provider-routeros/issues/455)) ([5a2782c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5a2782c30e01ce2e7fa17944058a68eed03e9a2b))
## [1.48.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.48.1...v1.48.2) (2024-05-13)
### Bug Fixes
* **veth:** Remove deprecated options ([8565c5b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/8565c5b5325c5b6fd61bcf8a2e76aa53e586f4fa))
## [1.48.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.48.0...v1.48.1) (2024-05-09)
### Bug Fixes
* **dns-record:** resource "routeros_ip_dns_record" keeps updating ([a755ab0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a755ab090746e1456b1bb1b4060f240d4420de5e)), closes [#445](https://github.com/terraform-routeros/terraform-provider-routeros/issues/445)
* **TimeEquall:** Crash when using store_leases_disk in routeros_ip_dhcp_server_config ([ba8c5a9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ba8c5a92b31e25a134d369e400b2a883e774d692)), closes [#447](https://github.com/terraform-routeros/terraform-provider-routeros/issues/447)
## [1.48.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.47.0...v1.48.0) (2024-05-07)
### Features
* **vrf:** Added routeros_ip_vrf resource ([#443](https://github.com/terraform-routeros/terraform-provider-routeros/issues/443)) ([a091b7d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a091b7da83aa9a70d04e9c50c8e81c2b6286e8d3))
## [1.47.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.46.3...v1.47.0) (2024-05-04)
### Features
* add ability to sign certificates with scep ([1dce5af](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1dce5af9a010463974df011e8d530a792e29f8f2))
### Bug Fixes
* add challenge_password parameter for system_certificate resource ([d933589](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d933589a186f86afad0ba609c05101ce26111149))
* fix changing sign data in routeros_system_certificate resource ([83848f9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/83848f9dac2247c8b60ace492f62d448b85950cb))
## [1.46.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.46.2...v1.46.3) (2024-04-27)
### Bug Fixes
* properly unset firewall filter rule `protocol` field when removed ([#435](https://github.com/terraform-routeros/terraform-provider-routeros/issues/435)) ([03a017d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/03a017d40e59f7ba94b6ad1e8b0f5f3236f28f9b))
## [1.46.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.46.1...v1.46.2) (2024-04-26)
### Bug Fixes
* **bridge_port:** [Backward compatibility] routeros_interface_bridge_port  ([#436](https://github.com/terraform-routeros/terraform-provider-routeros/issues/436)) ([ad64040](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ad64040358e5da70e326ab70d353008f263eb7fc)), closes [#419](https://github.com/terraform-routeros/terraform-provider-routeros/issues/419) [#419](https://github.com/terraform-routeros/terraform-provider-routeros/issues/419)
## [1.46.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.46.0...v1.46.1) (2024-04-21)
### Bug Fixes
* **nat:** [Backward compatibility] resource "routeros_ip_firewall_nat" ([ee8f992](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ee8f992098efb9bfdc636b81a4912b302046c839)), closes [#431](https://github.com/terraform-routeros/terraform-provider-routeros/issues/431)
* **wg_peer:** Invalid syntax for 'client_keepalive' field ([df24de2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/df24de28b406a1e431056266f6d5b429447d9f62)), closes [#432](https://github.com/terraform-routeros/terraform-provider-routeros/issues/432)
## [1.46.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.45.0...v1.46.0) (2024-04-16)
### Features
* add routeros_certificate_scep_server resource ([#420](https://github.com/terraform-routeros/terraform-provider-routeros/issues/420)) ([b80b52d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b80b52d9ef5f8ce8d4b1396092ba1dc816765489))
### Bug Fixes
* **no-release:** [Backward compatibility] routeros_interface_bridge NOT WORKING as expected ([dd46e95](https://github.com/terraform-routeros/terraform-provider-routeros/commit/dd46e95ac82b18d3ff2f7ef5a2c1cba30dc6f2f1)), closes [#417](https://github.com/terraform-routeros/terraform-provider-routeros/issues/417)
* **no-release:** [Backward compatibility] routeros_interface_bridge_port ([dca44bc](https://github.com/terraform-routeros/terraform-provider-routeros/commit/dca44bc1c23246fc63d2310f8f2a7d9f15ec5519)), closes [#419](https://github.com/terraform-routeros/terraform-provider-routeros/issues/419)
* **no-release:** [Backward compatibility] routeros_ip_firewall_filter NOT WORKING AS EXPECTED ([6cc2072](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6cc2072110ca5d67501a65ce5cd69cbb25e4fe12)), closes [#418](https://github.com/terraform-routeros/terraform-provider-routeros/issues/418)
* **no-release:** Field 'tx_carrier_sense_error' not found in the schema ([c3d2eb2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c3d2eb2343e6593f673d57e2bbe80bd32fc863a9)), closes [#416](https://github.com/terraform-routeros/terraform-provider-routeros/issues/416)
* **no-release:** Fix comparison of time & hex not provided by user ([4f85ccf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4f85ccf3303e6b91e6c0aee6dc0b4602d04604a3))
## [1.45.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.44.3...v1.45.0) (2024-04-09)
### Features
* **dhcp-relay:** Add DHCP Relay support ([6eb5901](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6eb590183e2c67dc5f797bbfbe545d502f39a04c)), closes [#413](https://github.com/terraform-routeros/terraform-provider-routeros/issues/413)
* **upnp:** Add UPNP & UPNP Interfaces ([8fd3da6](https://github.com/terraform-routeros/terraform-provider-routeros/commit/8fd3da66a671e1e3e6e62a38749fa0b58f3c1595)), closes [#412](https://github.com/terraform-routeros/terraform-provider-routeros/issues/412)
### Bug Fixes
* Export/import certificates ([205a221](https://github.com/terraform-routeros/terraform-provider-routeros/commit/205a22110a712a123a6225ae0f71d9f763043c02)), closes [#404](https://github.com/terraform-routeros/terraform-provider-routeros/issues/404)
* **upnp:** Fix "unknown parameter forced-external-ip" ([74333f2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/74333f2ec7eeba08ff018084cf75003d102fac32))
## [1.44.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.44.2...v1.44.3) (2024-04-09)
### Bug Fixes
* **Importer:** Add extended resource import function ([713d9ee](https://github.com/terraform-routeros/terraform-provider-routeros/commit/713d9ee6318b0f71dea33207687b5062af605859)), closes [#403](https://github.com/terraform-routeros/terraform-provider-routeros/issues/403)
## [1.44.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.44.1...v1.44.2) (2024-04-04)
### Bug Fixes
* Fix for release ([3c54e07](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3c54e076d86ef551223c1d83b5fa72a0c5742db8))
## [1.44.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.44.0...v1.44.1) (2024-04-04)
### Bug Fixes
* routeros_ip_service  not working ([c896837](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c8968373e42e60bc1d0d53d23031ac8231086d7f)), closes [#407](https://github.com/terraform-routeros/terraform-provider-routeros/issues/407)
## [1.44.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.43.0...v1.44.0) (2024-04-04)
### Features
* Add `routeros_capsman_interface` resource to manage CAPsMAN interfaces ([65b9717](https://github.com/terraform-routeros/terraform-provider-routeros/commit/65b9717b8afa7d218012f613af88c53fe0a21063))
### Bug Fixes
* Fix inline configuration properties not to update when untouched in `routeros_capsman_configuration` resources ([e2a5b55](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e2a5b5527a77a99a84f35e8381a59add6ab63d11))
## [1.43.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.42.0...v1.43.0) (2024-04-01)
### Features
*  Add NTP client resource ([0a678cf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0a678cf09c3ff350857c89c7d86cfc8a6de7cf00)), closes [#386](https://github.com/terraform-routeros/terraform-provider-routeros/issues/386)
* Add IP neighbor discovery resource ([706bccb](https://github.com/terraform-routeros/terraform-provider-routeros/commit/706bccbec25c25f5be162f941664954769fe4cfd)), closes [#388](https://github.com/terraform-routeros/terraform-provider-routeros/issues/388)
* Add SSH Server resource ([99883e4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/99883e49dcd05ad9eca46c2042c2996c1225c938)), closes [#389](https://github.com/terraform-routeros/terraform-provider-routeros/issues/389)
* Add tool/mac-server support ([13b565c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/13b565c40f3178e57b475bdd85880d52c7f5eb3b)), closes [#387](https://github.com/terraform-routeros/terraform-provider-routeros/issues/387)
### Bug Fixes
* Fix `isEmpty` function for Lists with ObjectType ([dbbb710](https://github.com/terraform-routeros/terraform-provider-routeros/commit/dbbb710f1ef97e3fed2ef7477e73a78e91104901))
* Set "AlwaysPresentNotUserProvided" for PropVrfRw ([fd58ea1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fd58ea19ae18b6fd2fbd1d1945b45c0936f1f0b9))
* **v7.12.2:** Change `routeros_interface_wireguard_peer` schema ([3f937c1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3f937c1b44d4661212b8aad93ebef326d52dbb55))
* **v7.12.2:** Change `routeros_ipv6_neighbor_discovery` schema ([598319a](https://github.com/terraform-routeros/terraform-provider-routeros/commit/598319adc29a02a34f6e4c52a87a979cc36a4a0b))
* **v7.12.2:** Change `routeros_routing_bgp_connection` schema ([205e43d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/205e43dac4600fdf2e632380f9cd687c55cc06b4))
## [1.42.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.41.0...v1.42.0) (2024-03-29)
### Features
* Add `http` scheme support for the REST API ([c326052](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c3260525afad9dad0e92b37ed6bb409a13e32d2e))
## [1.41.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.40.0...v1.41.0) (2024-03-27)
### Features
* Add function to create skip metadata based on slices ([ac54292](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ac54292f53b6384efa5b7e4f2e1ce0761ce47b3e))
### Bug Fixes
* Fix fields in new commits ([205919f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/205919f49fdb522357db562def3518194c3b81e4))
* Simplify the procedure for generating field conversion lists. ([a67b772](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a67b772da55e9590390b92eb0e16b83041977058))
## [1.40.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.39.0...v1.40.0) (2024-03-26)
### Features
* Add `routeros_zerotier_controller` resource to manage ZeroTier controller ([68cb99a](https://github.com/terraform-routeros/terraform-provider-routeros/commit/68cb99a350261e5350f5bba987b5a42e8b6a637c))
* Add `routeros_zerotier_interface` resource to manage ZeroTier interface ([481709c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/481709cee5b3a4fe3122173909e3ae19e43ccc18))
* Add `routeros_zerotier` resource to manage ZeroTier instances ([f182f0c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f182f0c93ab0ada397db2305eacd868e4a9b837a))
## [1.39.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.38.0...v1.39.0) (2024-03-26)
### Features
* Add `routeros_interface_wireless_cap` resource to manage CAPsMAN client ([b1558f9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b1558f92722ab69ccfe9cba86dc509f5ca591819))
* Add `routeros_ip_cloud_advanced` resource to manage advanced cloud settings ([405827d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/405827d0d843431abe71fb303a65105ae29e86b0))
* Add `routeros_ppp_aaa` resource to manage authentication and accounting ([87f06c0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/87f06c01c2a5b1b33bada1e4d6c69bcc559a38d3))
## [1.38.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.37.2...v1.38.0) (2024-03-23)
### Features
* Add support for interface macvlan ([24d940b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/24d940b53e9b87487a19f7e7c44f7fe3a27e3c3f))
### Bug Fixes
* **no-release:** Resolve warnings due to some missing properties ([#381](https://github.com/terraform-routeros/terraform-provider-routeros/issues/381)) ([864ed27](https://github.com/terraform-routeros/terraform-provider-routeros/commit/864ed278e304e6789cb4401d4ef8ea33ca2e7bd2))
## [1.37.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.37.1...v1.37.2) (2024-03-18)
### Bug Fixes
* **dhcp-server:** Add a missing DHCP server option attribute ([c375754](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c375754f0651196cbdb3ec986149d60f16fa6847)), closes [#376](https://github.com/terraform-routeros/terraform-provider-routeros/issues/376)
## [1.37.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.37.0...v1.37.1) (2024-03-18)
### Bug Fixes
* Enable importing ethernet interfaces ([#379](https://github.com/terraform-routeros/terraform-provider-routeros/issues/379)) ([3676f3f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3676f3f210acaa51e6f0632369d8ba5f35f56b5e))
## [1.37.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.36.1...v1.37.0) (2024-03-18)
### Features
* Add `routeros_wifi` resource to manage WiFi interfaces ([5f234c4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5f234c456ca8c790e214d5b3e2dd8a8b1ab69b88))
### Bug Fixes
* Add reusable L2MTU property ([93a7495](https://github.com/terraform-routeros/terraform-provider-routeros/commit/93a749559aaf7df3235c8d9512cc7c5a1e417cea))
* Fix the `routeros_wifi_configuration` resource to suppress pristine inline parameters ([77d807c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/77d807c2fd1e8bfe8d67de011c2b3b4851477d41))
* Refactor `AlwaysPresentNotUserProvided` helper to self-contain empty value check ([669fd68](https://github.com/terraform-routeros/terraform-provider-routeros/commit/669fd689008aba4673205fcfca1252c5b1a7f795))
* Refactor `AlwaysPresentNotUserProvided` helper to support map type ([038fe7c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/038fe7c192ba87c46f1ed13334183f33d1cc6717))
## [1.36.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.36.0...v1.36.1) (2024-03-18)
### Bug Fixes
* stop using Int32MaxValue as upper bound for validation ([fcae1bd](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fcae1bdfb8ef0b3622133eab4b04822b122ed405))
## [1.36.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.35.1...v1.36.0) (2024-03-17)
### Features
* Add routeros_system_script ([bf72b32](https://github.com/terraform-routeros/terraform-provider-routeros/commit/bf72b327d25605216ba8a5a44cb2aed43775dd6f)), closes [#373](https://github.com/terraform-routeros/terraform-provider-routeros/issues/373)
## [1.35.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.35.0...v1.35.1) (2024-02-28)
### Bug Fixes
* **no-release:** Fix max value for MTU - Fix Main ([#365](https://github.com/terraform-routeros/terraform-provider-routeros/issues/365)) ([b2c57de](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b2c57de6967d92dfc1dd445566f711544913483e))
* Undo commit "Change l2mtu property " ([#367](https://github.com/terraform-routeros/terraform-provider-routeros/issues/367)) ([8657054](https://github.com/terraform-routeros/terraform-provider-routeros/commit/86570540ecf5a3cdcd1a7391074e6626bbef8bc0)), closes [#326](https://github.com/terraform-routeros/terraform-provider-routeros/issues/326)
## [1.35.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.34.0...v1.35.0) (2024-02-22)
### Features
* Add resource routeros_ipv6_neighbor_discovery ([#362](https://github.com/terraform-routeros/terraform-provider-routeros/issues/362)) ([13fb7b7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/13fb7b75ba398b97551b58ff7cd8f99e26a15e12))
### Bug Fixes
* **no-release:** Add gateway6 field to /interface/veth ([#358](https://github.com/terraform-routeros/terraform-provider-routeros/issues/358)) ([b0385f6](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b0385f66815ac1205606d64c3df80fcd9b315d08))
## [1.34.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.33.1...v1.34.0) (2024-02-15)
### Features
* **ipv6:** Add support for /ipv6/dhcp-client/option ([df43330](https://github.com/terraform-routeros/terraform-provider-routeros/commit/df43330ca7bed7e15d8a7f18d76adcacd3289fc0))
## [1.33.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.33.0...v1.33.1) (2024-02-14)
### Features
* **no-release:** Add support for /container ([#356](https://github.com/terraform-routeros/terraform-provider-routeros/issues/356)) ([afacc8f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/afacc8fa8d382cf1db23336d448f141f8cabea56))
### Bug Fixes
* **ipv6:** Add fields for /ipv6/dhcp-client ([#357](https://github.com/terraform-routeros/terraform-provider-routeros/issues/357)) ([17a26d9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/17a26d9a5c2f6a92415da688a64074f7bf97e9ce))
* **no-release:** Add missing ethernet interface fields to SkipFields ([#359](https://github.com/terraform-routeros/terraform-provider-routeros/issues/359)) ([55409c4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/55409c4f762d2664da7b5cef7169e36013e2f203))
## [1.33.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.6...v1.33.0) (2024-02-13)
### Features
* **file:** Add support for /file ([#355](https://github.com/terraform-routeros/terraform-provider-routeros/issues/355)) ([2a1d9fd](https://github.com/terraform-routeros/terraform-provider-routeros/commit/2a1d9fd7f866b427fcbff4589b6b19d42c9267a1))
### Bug Fixes
* **no-release:** Change the Name property for the ipip resource ([4899cf1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4899cf18fae8dd85a3df64ac7b75d0d7752f4c52))
## [1.32.6](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.5...v1.32.6) (2024-02-06)
### Features
* **no-release:** add interface/ipip ([#346](https://github.com/terraform-routeros/terraform-provider-routeros/issues/346)) ([e7bd8dd](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e7bd8ddaaf66ad101bd901d1c9045d52f69ab45b))
### Bug Fixes
* dhcp client add script string parameter ([#348](https://github.com/terraform-routeros/terraform-provider-routeros/issues/348)) ([3df2b69](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3df2b69b155368383af121ac51a86f0d7b9a2896))
* **no-release:** Mandatory use of ID as ipip resource identifier ([55f8a62](https://github.com/terraform-routeros/terraform-provider-routeros/commit/55f8a629297512a8d6397de6786b9b6fb3320a6c)), closes [#346](https://github.com/terraform-routeros/terraform-provider-routeros/issues/346)
## [1.32.5](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.4...v1.32.5) (2024-01-25)
### Bug Fixes
* Change l2mtu property ([9260354](https://github.com/terraform-routeros/terraform-provider-routeros/commit/92603541fd6b3f11dcbfd1ff2c1904f6687062a9)), closes [#326](https://github.com/terraform-routeros/terraform-provider-routeros/issues/326)
* **cloud:** Add missing field ([235e3b0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/235e3b07de33ca0b1edb82f728c0e3d241256a26)), closes [#331](https://github.com/terraform-routeros/terraform-provider-routeros/issues/331)
* **no-release:** Fix Delete. Not an system object ([#343](https://github.com/terraform-routeros/terraform-provider-routeros/issues/343)) ([89ee0ea](https://github.com/terraform-routeros/terraform-provider-routeros/commit/89ee0ea2934f923dbf99744bd7d455bbf95910d2))
* **no-release:** Fix Delete. Not an Systemresource ([#342](https://github.com/terraform-routeros/terraform-provider-routeros/issues/342)) ([e560128](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e560128554dd157b8b9a3399724baa2e5def521e))
* **wg peer:** Add missing fields ([48018c4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/48018c4d525319b48e77923d57b4816ceb53cd30)), closes [#332](https://github.com/terraform-routeros/terraform-provider-routeros/issues/332)
## [1.32.4](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.3...v1.32.4) (2024-01-24)
### Bug Fixes
* Removed all default values ([546764e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/546764e1a14795936cd6890aad6530942b104c3e)), closes [#326](https://github.com/terraform-routeros/terraform-provider-routeros/issues/326)
## [1.32.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.2...v1.32.3) (2024-01-19)
### Bug Fixes
* **switch:** Correct schema errors ([c4b3421](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c4b3421fc39b2b1984aeab00b36c475844c4edf4)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
## [1.32.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.1...v1.32.2) (2024-01-16)
### Bug Fixes
* **switch:** Incorrect procedure for deleting the resource ([1e2327c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1e2327c43d934da59fc2a6a36a485b4caf18db4d)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
## [1.32.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.32.0...v1.32.1) (2024-01-16)
### Bug Fixes
* Add missing `default` property in `routeros_routing_bgp_template` ([0a2863f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0a2863ff01cfc26a904dab246716b4c9a7610f81))
* Add missing generated certificate properties in `routeros_capsman_manager` ([e4378af](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e4378af30e5da4b1f4e6cb18cad5cb4b3ce61c2a))
* Add new `port_cost_mode` property to `routeros_interface_bridge` ([cab4fb6](https://github.com/terraform-routeros/terraform-provider-routeros/commit/cab4fb67e768b2e0b59c3ceac0edba07a1ba1138))
* Fix validator of the `address` property in `routeros_user_manager_router` ([1c7a46b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1c7a46b1bea703cafc5e1dd4782fce299d3383c6))
* Fix validator of the `advertise` property in `routeros_interface_ethernet` ([6c98bb7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6c98bb7360cbcaabbe3ef6d4688a0683577ef211))
## [1.32.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.31.0...v1.32.0) (2024-01-15)
### Features
* **switch:** Add support for /interface/ethernet/switch/host ([c267e5d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c267e5dbeab24578f3a7dbfcd9f5150b790391ba)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
* **switch:** Add support for /interface/ethernet/switch/port ([a3e7921](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a3e7921a1c59a6e4d79965ec3ec8bc1cf3f0ce09)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
* **switch:** Add support for /interface/ethernet/switch/vlan ([2690373](https://github.com/terraform-routeros/terraform-provider-routeros/commit/2690373800ca29672b3c279fda4e99128e9f0860)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
* **switch:** Add support for interface/ethernet/switch/rule ([163ebbe](https://github.com/terraform-routeros/terraform-provider-routeros/commit/163ebbe4d54e5a2d7444d015306ab0cdd4565055)), closes [#325](https://github.com/terraform-routeros/terraform-provider-routeros/issues/325)
## [1.31.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.30.0...v1.31.0) (2024-01-15)
### Features
* Add WiFi access list resource ([e5a213a](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e5a213abc3e10586471ddce5c0806a010997bcaa))
* Add Wifi accounting and authentication resource ([edd8299](https://github.com/terraform-routeros/terraform-provider-routeros/commit/edd8299edbad5b6c866d25659b262966d71fe09d))
* Add WiFi CAP resource ([d68fc6c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d68fc6c5c3d4207464446ee87451df00e4a885b1))
* Add WiFi CAPsMAN resource ([00197cf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/00197cfc130d8316a43c351a66c1c757aaeb3c2b))
* Add WiFi channel resource ([3fd1f34](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3fd1f34b040ee1e1eacce246a221a092315b8aea))
* Add WiFi configuration resource ([1505bff](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1505bffb0d19c27553f7614b352dfc1a087c9806))
* Add WiFi datapath resource ([4193151](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4193151e790ebe4b4b0074b3dd8e0cf5a4878ad8))
* Add WiFi interworking resource ([f748368](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f748368c3ec2262eea531a51ec34706a30842f24))
* Add WiFi provisioning resource ([7a80781](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7a80781f6bfe6bd1818c26a1f0f094317581fddc))
* Add WiFi security resource ([0c7e3af](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0c7e3af28d23b27eff730331f0589484eef88b6d))
* Add WiFi steering resource ([3794b0f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3794b0fbf8bbd847deea81e5fc0554ffb010355f))
## [1.30.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.29.1...v1.30.0) (2024-01-12)
### Features
* **routing:** Manage Route Filters ([0c29e53](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0c29e531be76e8c322062babd4c082d7e685ff7f)), closes [#330](https://github.com/terraform-routeros/terraform-provider-routeros/issues/330)
## [1.29.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.29.0...v1.29.1) (2024-01-11)
### Bug Fixes
* **helpers:** Fix the style of writing filter parameters ([adf342f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/adf342ff668cde440265fb34461d0d105602fc9f))
## [1.29.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.28.1...v1.29.0) (2024-01-05)
### Features
* Add system user authentication and accounting settings resource ([1899983](https://github.com/terraform-routeros/terraform-provider-routeros/commit/18999832de2ff864008b1f84cc0801fdfc9697c5))
* Add system user group resource ([c7cc658](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c7cc658b69c5e75033c4eddfebc42f928bccd4e2))
* Add system user settings resource ([f889b7b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f889b7bd95bf4f559888edcfb32640b8d4fd731a))
### Bug Fixes
* Change the validator ([0b1881f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0b1881ff69cd3bc56a30d9fd2e239e08ee480b0d))
* Fix the growth of the 'valid' slice ([206cfc2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/206cfc277a1ce5caaa9842d5b33503ee861745b1))
## [1.28.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.28.0...v1.28.1) (2023-12-25)
### Bug Fixes
* **firewall:** Fix the error of deleting field-lists ([3f2f7b1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3f2f7b1f6d335f99e3ff73e82f147a678325d4cf))
## [1.28.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.27.2...v1.28.0) (2023-12-15)
### Features
* Data source to list DHCP leases ([71f9571](https://github.com/terraform-routeros/terraform-provider-routeros/commit/71f95712255dcb1c1420c243c5a4426ba5328afd)), closes [#316](https://github.com/terraform-routeros/terraform-provider-routeros/issues/316)
### Bug Fixes
* Comparison of MAC addresses in different character cases ([9acc3cc](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9acc3cc705dd13a6e75d1487c1088eb7fea04609))
## [1.27.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.27.1...v1.27.2) (2023-12-06)
### Bug Fixes
* Firewall filter rules order ([#314](https://github.com/terraform-routeros/terraform-provider-routeros/issues/314)) ([3d32136](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3d321362445fcfd401317f9829b1a206326dbae9)), closes [#293](https://github.com/terraform-routeros/terraform-provider-routeros/issues/293)
## [1.27.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.27.0...v1.27.1) (2023-12-06)
### Bug Fixes
* Add 2.5Gbps to validation set ([#313](https://github.com/terraform-routeros/terraform-provider-routeros/issues/313)) ([47d6781](https://github.com/terraform-routeros/terraform-provider-routeros/commit/47d67811bc70776b9aea58f4f8ec0dc0166eed42)), closes [#311](https://github.com/terraform-routeros/terraform-provider-routeros/issues/311)
## [1.27.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.26.0...v1.27.0) (2023-12-02)
### Features
* Add float type support ([4cc485b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4cc485b316747c59dee7e7efc3ddda32ee1c83b9))
* Add user manager advanced settings resource ([287db08](https://github.com/terraform-routeros/terraform-provider-routeros/commit/287db0886c31dfb1a91a7193ea944ffccc30747a))
* Add user manager attribute resource ([fa7dd30](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fa7dd302356bafcb912d95eb41ec3ea339c4b78c))
* Add user manager database resource ([ca4e490](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ca4e490fe75c85f41023d16f5316adef06c5cc37))
* Add user manager limitation resource ([a97bc45](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a97bc45c75c99a525875046a01c2940069b624ba))
* Add user manager profile limitation resource ([733932c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/733932c5bbca367fb5f461f3508b485ed428fb14))
* Add user manager profile resource ([d95bed1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d95bed153373122ef958d96a606b9199fa3f01f5))
* Add user manager router resource ([162e01e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/162e01e556d9d92e0833ce470ff6486f645a0d34))
* Add user manager settings resource ([23761cf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/23761cf5d2b13b28f93c6d2f2bc064f7156d58ca))
* Add user manager user group resource ([fff1568](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fff156866c8f2a47edb52e407a4d129ad54a2185))
* Add user manager user profile resource ([9500635](https://github.com/terraform-routeros/terraform-provider-routeros/commit/95006359d071dc3c4ef2c3c19bf5847ab6f3dbbe))
* Add user manager user resource ([727cd9b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/727cd9b196680d3649cccd506a7f88530aa735a4))
### Bug Fixes
* Fix the `AlwaysPresentNotUserProvided` helper to handle lists and sets correctly ([7c68003](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7c68003df94e4fb3755101996e4418a41bb306b4))
## [1.26.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.25.1...v1.26.0) (2023-11-29)
### Features
* **/system/ntp/server:** Add NTP Server resource ([f7851ca](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f7851ca3af4d26c3ebff5677153213b44b2d4657)), closes [#306](https://github.com/terraform-routeros/terraform-provider-routeros/issues/306)
## [1.25.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.25.0...v1.25.1) (2023-11-27)
### Bug Fixes
* Add missing schema fields ([#303](https://github.com/terraform-routeros/terraform-provider-routeros/issues/303)) ([bd245b9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/bd245b91820bc3920b38cdc984c7332c36ce03d0))
* **no-release:** Fix incorrect addition of skip fields ([9ee6d70](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9ee6d70170d4c290609742ae27bac48228edaf7c))
## [1.25.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.24.0...v1.25.0) (2023-11-15)
### Features
* Add RADIUS incoming resource ([6fb0a23](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6fb0a23a98f6089493a35031d9722b978110bb41))
* Add RADIUS resource ([eb0b5c3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/eb0b5c38c0758efc866441fe630fc529f84af195))
### Bug Fixes
* Add compatibility layer for the VRF property in RADIUS incoming resource ([96a5354](https://github.com/terraform-routeros/terraform-provider-routeros/commit/96a5354b95f4f94d5198b55f0d017b8477c8f0b0))
* **no-release:** Skip computed stat fields ([#299](https://github.com/terraform-routeros/terraform-provider-routeros/issues/299)) ([579f0a0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/579f0a0ea9cc73ab4c038b8bf9a2721ce6a9f99f))
## [1.24.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.23.0...v1.24.0) (2023-11-13)
### Features
* **ds:** Add /ip/arp datasource ([6ecd622](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6ecd622973facf7296fd0009304c0249f1e3e369))
* **ds:** Add /system/resource datasource ([79a599e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/79a599eb980bd73b677098d0cc54505b66b6069e))
### Bug Fixes
* **REST:** Return possible error on JSON parsing ([7134eac](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7134eac723886d14214ef60de0faaa532387483c))
## [1.23.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.22.1...v1.23.0) (2023-11-10)
### Features
* Add 802.1X client resource ([db76369](https://github.com/terraform-routeros/terraform-provider-routeros/commit/db763696e4003399b76cb474ea32614a4e8028db))
* Add 802.1X server resource ([05894af](https://github.com/terraform-routeros/terraform-provider-routeros/commit/05894afc3145a8af232b3eb517c95ac224f2cfe4))
### Bug Fixes
* Bump Go version from 1.19 to 1.21 ([#297](https://github.com/terraform-routeros/terraform-provider-routeros/issues/297)) ([1a56503](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1a565038228d408d55d405423288a54f006e967c))
## [1.23.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.22.1...v1.23.0) (2023-11-10)
### Features
* Add 802.1X client resource ([db76369](https://github.com/terraform-routeros/terraform-provider-routeros/commit/db763696e4003399b76cb474ea32614a4e8028db))
* Add 802.1X server resource ([05894af](https://github.com/terraform-routeros/terraform-provider-routeros/commit/05894afc3145a8af232b3eb517c95ac224f2cfe4))
## [1.22.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.22.0...v1.22.1) (2023-11-09)
### Bug Fixes
* Unexpected value: aes256 for RouterOS v7.7 ([#294](https://github.com/terraform-routeros/terraform-provider-routeros/issues/294)) ([6fc8149](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6fc8149e77d45a53312e7d9c9b50b451d4791460)), closes [#291](https://github.com/terraform-routeros/terraform-provider-routeros/issues/291)
## [1.22.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.21.0...v1.22.0) (2023-11-07)
### Features
* Add DHCP server config resource ([#288](https://github.com/terraform-routeros/terraform-provider-routeros/issues/288)) ([0e9fbbf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0e9fbbf52484962789bd28b2caaab9be238bff86))
## [1.21.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.20.1...v1.21.0) (2023-11-06)
### Features
* Add ethernet switch settings ([162c1da](https://github.com/terraform-routeros/terraform-provider-routeros/commit/162c1da0233e2e909d98dd02f011e89513233c9a)), closes [#285](https://github.com/terraform-routeros/terraform-provider-routeros/issues/285) [#282](https://github.com/terraform-routeros/terraform-provider-routeros/issues/282)
* Add MLAG settings ([6b8cfd2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6b8cfd246d893abefc88ee3933e039f7cf1de508)), closes [#268](https://github.com/terraform-routeros/terraform-provider-routeros/issues/268)
### Bug Fixes
* **bridge:** Add Name-Id migration ([84a7f3c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/84a7f3c7cafeb700fe7fef8f367208b6d4ba2dc5))
* **CAPsMAN:** Add Name-Id migration ([5d0effa](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5d0effa4d24365671dcbf268da66460b4483c25f))
* **dhcp_server:** Add Name-Id migration ([c8c9ff8](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c8c9ff89d6b81253c7e8e8f020aba7cc47e03159))
* **eoip:** Add Name-Id migration ([fdbd68f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fdbd68f21f2ef5284b0e8529095a4cb5a3a76067))
* **eoip:** Fix the resource ID type ([7916c30](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7916c30fcf36899631dfb25a362c378dc3ebbac4))
* **gre:** Add Name-Id migration ([6e811c3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6e811c3c3aa054f0c91d554cc9814ed3ff032b62))
* **interface_list:** Add Name-Id migration ([6b326c0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6b326c0dd62241e7b70307ac6400421f44ff94b1))
* **ip_pool:** Add Name-Id migration ([98c17c2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/98c17c2130e798092a86e2e724b99c7a90980f15))
* **scheduler:** Add Name-Id migration ([c34b994](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c34b99483f96eb9d1b49552326883fe9190c3c93))
* **vlan:** Add Name-Id migration ([7592f2f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7592f2f2fba7ea7d3a7875906b71a75126fd0f90))
* **vrrp:** Add Name-Id migration ([30c8f37](https://github.com/terraform-routeros/terraform-provider-routeros/commit/30c8f37a004c0b3b67dce85965535a0836b57af7))
* **wg:** Add Name-Id migration ([d676b8b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d676b8b26c64e114caeb108191ed911319c0f4ab))
## [1.20.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.20.0...v1.20.1) (2023-11-02)
### Bug Fixes
* Fix empty value check to handle default numeric values correctly ([#286](https://github.com/terraform-routeros/terraform-provider-routeros/issues/286)) ([661e49c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/661e49ccbd0ca87eec024187e0e9ad6c2cb9890b))
* **no-release:** Some boolean params can't be reset and the provider does not understand the value ([#269](https://github.com/terraform-routeros/terraform-provider-routeros/issues/269)) ([678c9a4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/678c9a4c67d2553e3bc72dc6a29d14d415520fa6)), closes [#253](https://github.com/terraform-routeros/terraform-provider-routeros/issues/253)
## [1.20.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.19.0...v1.20.0) (2023-10-31)
### Features
* Add EoIP tunnel support ([#283](https://github.com/terraform-routeros/terraform-provider-routeros/issues/283)) ([bcab0fb](https://github.com/terraform-routeros/terraform-provider-routeros/commit/bcab0fb38634a992250ff92271543c5f0dd309cc))
## [1.19.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.18.4...v1.19.0) (2023-10-29)
### Features
* Add CAPsMAN access-list resource ([#281](https://github.com/terraform-routeros/terraform-provider-routeros/issues/281)) ([a0379c9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a0379c9b22edff87dc5dbedb1f74d8b30d010f09))
## [1.18.4](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.18.3...v1.18.4) (2023-10-26)
### Bug Fixes
* Fix enumerated values in CAPsMAN resources ([978576a](https://github.com/terraform-routeros/terraform-provider-routeros/commit/978576a59768e79369e1ba0fdff00044113260cd))
## [1.18.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.18.2...v1.18.3) (2023-10-09)
### Bug Fixes
* Fix double slash at the end of a hostname ([d33aa79](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d33aa79a78d4932d2c8f89c854d0aa8940e6642c)), closes [#275](https://github.com/terraform-routeros/terraform-provider-routeros/issues/275)
## [1.18.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.18.1...v1.18.2) (2023-10-01)
### Bug Fixes
* Improvements on the resource routeros_interface_ethernet ([#266](https://github.com/terraform-routeros/terraform-provider-routeros/issues/266)) ([099185b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/099185beff487b514379a8472c0c208bdb6a6215))
## [1.18.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.18.0...v1.18.1) (2023-09-27)
### Bug Fixes
* Move WG  keys from datasource to resource ([#265](https://github.com/terraform-routeros/terraform-provider-routeros/issues/265)) ([a4eaf8c](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a4eaf8c5fd00e56f7d69ddac5bfa575e8487ff60))
## [1.18.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.17.0...v1.18.0) (2023-09-24)
### Features
* Creating key sets for WireGuard tunnels ([e2d28a3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e2d28a3d8d1184ab2fb4118cb7b44147cb8fbbc3))
## [1.17.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.16.0...v1.17.0) (2023-09-22)
### Features
* Ip firewall connection tracking ([#260](https://github.com/terraform-routeros/terraform-provider-routeros/issues/260)) ([9d39bf8](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9d39bf82ebbff621888bb6535fe57148488f0215))
## [1.16.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.15.0...v1.16.0) (2023-09-21)
### Features
* Implement routeros_system_logging resource ([#261](https://github.com/terraform-routeros/terraform-provider-routeros/issues/261)) ([f8c89aa](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f8c89aa7a197ae765fbbaf3138dda06b1a8787e4))
## [1.15.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.14.0...v1.15.0) (2023-09-20)
### Features
* Add routeros_ip_dhcp_server_option and routeros_ip_dhcp_server_option_set ([#259](https://github.com/terraform-routeros/terraform-provider-routeros/issues/259)) ([3722afb](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3722afb8574250a7a7e3211f2e40f3b4acfdc56f))
## [1.14.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.13.3...v1.14.0) (2023-09-19)
### Features
* Implementation of routeos_interface_ethernet ([#256](https://github.com/terraform-routeros/terraform-provider-routeros/issues/256))([#255](https://github.com/terraform-routeros/terraform-provider-routeros/issues/255)) ([0d848bf](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0d848bf4b3d12b438bc9cbb137c91dca616b9d6a))
## [1.13.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.13.2...v1.13.3) (2023-09-18)
### Bug Fixes
* ip_service drift + failure ([#257](https://github.com/terraform-routeros/terraform-provider-routeros/issues/257)) ([b53b31b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b53b31bc4ada26245c272a3e597c3ff4e4ed5d6c)), closes [#254](https://github.com/terraform-routeros/terraform-provider-routeros/issues/254)
## [1.13.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.13.1...v1.13.2) (2023-07-20)
### Bug Fixes
* Add SNMP Settings ([#242](https://github.com/terraform-routeros/terraform-provider-routeros/issues/242)) ([e3a0d36](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e3a0d36acb60c98088a298a21220746db0259dc4)), closes [#232](https://github.com/terraform-routeros/terraform-provider-routeros/issues/232)
## [1.13.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.13.0...v1.13.1) (2023-07-19)
### Bug Fixes
* no updates when modifying the cod ([23d175b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/23d175bf6ea2361330900628696f9c31641aebdb)), closes [#240](https://github.com/terraform-routeros/terraform-provider-routeros/issues/240)
## [1.13.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.12.1...v1.13.0) (2023-07-13)
### Features
* Add an SNMP resource ([43c1ec9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/43c1ec9f53a40b96f9bc47d7446e86c6c724f3e2)), closes [#232](https://github.com/terraform-routeros/terraform-provider-routeros/issues/232)
* Add SNMP community resource ([eeea040](https://github.com/terraform-routeros/terraform-provider-routeros/commit/eeea04099b6431f508eb68cdd4d924653a7d17ff))
## [1.12.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.12.0...v1.12.1) (2023-07-12)
### Bug Fixes
* Fix the ParseDuration function ([1995d9e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1995d9ef8b8eac2808a34f3e433a24bd978e3bbc))
* Resource firewall filter ([fa04b82](https://github.com/terraform-routeros/terraform-provider-routeros/commit/fa04b820b7754d2e7cfdbab0d1064075415bf31d)), closes [#237](https://github.com/terraform-routeros/terraform-provider-routeros/issues/237)
## [1.12.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.11.0...v1.12.0) (2023-06-19)
### Features
* Add IP Cloud ([#234](https://github.com/terraform-routeros/terraform-provider-routeros/issues/234)) ([675e9f3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/675e9f3b57735ca035af34b43a0568fe2ee71c28)), closes [#231](https://github.com/terraform-routeros/terraform-provider-routeros/issues/231)
## [1.11.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.10.4...v1.11.0) (2023-06-19)
### Features
* New OSPF resource ([4d473ea](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4d473ea2e958a52f6544742cf47f0a1190e36508))
### Bug Fixes
* Add a helper for the attribute 'inactive' ([adca988](https://github.com/terraform-routeros/terraform-provider-routeros/commit/adca988ca08d36d6cab9a839fbad891827e72a81))
* Fix for error "no-summaries only valid for stubby areas" ([f222f71](https://github.com/terraform-routeros/terraform-provider-routeros/commit/f222f71691fd6e67b9967d66ef541e9d88376cea))
## [1.10.4](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.10.3...v1.10.4) (2023-05-30)
### Bug Fixes
* Patching firewall rules with place_before ([#224](https://github.com/terraform-routeros/terraform-provider-routeros/issues/224)) ([5ef738e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/5ef738e1d530bb0c2aeb0abdeb8fd71f535150b7)), closes [#223](https://github.com/terraform-routeros/terraform-provider-routeros/issues/223)
## [1.10.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.10.2...v1.10.3) (2023-05-27)
### Bug Fixes
* ci fix expired token ([#220](https://github.com/terraform-routeros/terraform-provider-routeros/issues/220)) ([e6a8585](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e6a85853e60c4fafd49d59a7e702a9bae53f4678))
* **docs:** Update release.yml ([#221](https://github.com/terraform-routeros/terraform-provider-routeros/issues/221)) ([44ba77d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/44ba77d1ffe8b9863a3e01a16379dea23406c8ee)), closes [#219](https://github.com/terraform-routeros/terraform-provider-routeros/issues/219)
* Wrong field names in example files ([#219](https://github.com/terraform-routeros/terraform-provider-routeros/issues/219)) ([b0105ef](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b0105ef1b295f7468debab14735e557e12eb01f3)), closes [#218](https://github.com/terraform-routeros/terraform-provider-routeros/issues/218)
## [1.10.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.10.1...v1.10.2) (2023-05-23)
### Bug Fixes
* Remove extra space after passthrough in validation ([#217](https://github.com/terraform-routeros/terraform-provider-routeros/issues/217)) ([3061910](https://github.com/terraform-routeros/terraform-provider-routeros/commit/306191072d3ceb57acc4e0533ed878e1f6a18646))
## [1.10.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.10.0...v1.10.1) (2023-05-19)
### Bug Fixes
* ipv6 addr-list addr w/o netmask adds /128 netmask [#216](https://github.com/terraform-routeros/terraform-provider-routeros/issues/216)  ([d6f7fad](https://github.com/terraform-routeros/terraform-provider-routeros/commit/d6f7fadfed9bac3e9bcc60640d935c08499053d2))
## [1.10.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.9.1...v1.10.0) (2023-05-17)
### Features
* Add support for /interface/pppoe-client ([#215](https://github.com/terraform-routeros/terraform-provider-routeros/issues/215)) ([a8cbe7d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a8cbe7d78ec868752f11184131c09b662e561a4c)), closes [#202](https://github.com/terraform-routeros/terraform-provider-routeros/issues/202)
## [1.9.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.9.0...v1.9.1) (2023-05-17)
### Bug Fixes
* Field 'comment' not found in the schema ([#214](https://github.com/terraform-routeros/terraform-provider-routeros/issues/214)) ([01a7f10](https://github.com/terraform-routeros/terraform-provider-routeros/commit/01a7f101ade024981f8c59a56775aa1f4bdae442)), closes [#213](https://github.com/terraform-routeros/terraform-provider-routeros/issues/213)
## [1.9.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.8.0...v1.9.0) (2023-05-17)
### Features
* Support ipv6 firewall address lists ([878fbf7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/878fbf70d8e78c8993105da01f41a8ce8b9df4cb)), closes [#212](https://github.com/terraform-routeros/terraform-provider-routeros/issues/212)
## [1.8.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.7.2...v1.8.0) (2023-05-16)
### Features
* Support bridge settings ([0bea447](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0bea447ceed39579b565cd9041fdb98769e21f46)), closes [#209](https://github.com/terraform-routeros/terraform-provider-routeros/issues/209)
## [1.7.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.7.1...v1.7.2) (2023-05-15)
### Bug Fixes
* nil pointer on bgp ([93cf45e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/93cf45e45352b09cf24e82273d6905e10c0b1f13)), closes [#207](https://github.com/terraform-routeros/terraform-provider-routeros/issues/207)
## [1.7.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.7.0...v1.7.1) (2023-05-15)
### Bug Fixes
* Fix resource names [#183](https://github.com/terraform-routeros/terraform-provider-routeros/issues/183) ([a4314d0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a4314d0c2765f7d6eea1cc672bf8c5dc633e9941))
* Fix the gateway field (veth) ([97b933b](https://github.com/terraform-routeros/terraform-provider-routeros/commit/97b933b2221005433cf249403086bce6d970c202))
## [1.7.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.6.0...v1.7.0) (2023-05-14)
### Features
* BGP connection ([3874d90](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3874d909ff245e5493368a4e3d472e45cdcad65c)), closes [#183](https://github.com/terraform-routeros/terraform-provider-routeros/issues/183)
* BGP templates ([7984574](https://github.com/terraform-routeros/terraform-provider-routeros/commit/7984574c9282019894e02b3f4b3fab04461c80a5)), closes [#183](https://github.com/terraform-routeros/terraform-provider-routeros/issues/183)
* Processing nested fields in a list ([23928a0](https://github.com/terraform-routeros/terraform-provider-routeros/commit/23928a02c724d40b533ef16ec07deb2551497fb2))
* Support for /interface/bonding [#203](https://github.com/terraform-routeros/terraform-provider-routeros/issues/203) ([a7de21f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a7de21fd630450590a08be5b94449f82c33e6bbf))
* Support for veth interfaces [#206](https://github.com/terraform-routeros/terraform-provider-routeros/issues/206) ([a6fdcf8](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a6fdcf80a2af0d2b14b66683fb578160e7555a99))
### Bug Fixes
* Changing the signature isEmpty + fixing the result for boolean values ([aedc90e](https://github.com/terraform-routeros/terraform-provider-routeros/commit/aedc90e5efbc6cc98adb558893cc17f727adeda9))
* Correct the logic of isEmpty ([18f4bf1](https://github.com/terraform-routeros/terraform-provider-routeros/commit/18f4bf19c58b4a5a8139e86946c254d7310ba013))
* Use helpers to process data for TypeMap ([280c994](https://github.com/terraform-routeros/terraform-provider-routeros/commit/280c994d060af676620cd592d26bcd988cc90405))
## [1.6.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.5.0...v1.6.0) (2023-05-05)
### Features
* Support creating users [#200](https://github.com/terraform-routeros/terraform-provider-routeros/issues/200) ([#201](https://github.com/terraform-routeros/terraform-provider-routeros/issues/201)) ([78191e2](https://github.com/terraform-routeros/terraform-provider-routeros/commit/78191e2038607af5081d06dfaabc208010f6d667))
## [1.5.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.4.0...v1.5.0) (2023-05-04)
### Features
* Add OpenVPN Server support ([6477fcd](https://github.com/terraform-routeros/terraform-provider-routeros/commit/6477fcdc61d5769a685fb32e551b41609f6f6aa6))
### Bug Fixes
* Rename the PropNameRw property and add a new one without forced re-creation ([a37f926](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a37f926d2a1d8ffbddfbf5e75c5a28591f33e44c))
## [1.4.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.9...v1.4.0) (2023-05-01)
### Features
* Support for ip/services ([#195](https://github.com/terraform-routeros/terraform-provider-routeros/issues/195)) ([591096d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/591096d4a249acb6f4484bc16a5aec691577453c)), closes [#182](https://github.com/terraform-routeros/terraform-provider-routeros/issues/182)
## [1.3.9](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.8...v1.3.9) (2023-05-01)
### Bug Fixes
* Fix the creation of resources when renaming them ([c229d27](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c229d27e27802507901381218585f27131db6c2a)), closes [#192](https://github.com/terraform-routeros/terraform-provider-routeros/issues/192)
## [1.3.8](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.7...v1.3.8) (2023-04-26)
### Bug Fixes
* Warnings for primary_ntp and secondary_ntp when using routeros_ip_dhcp_client ([#190](https://github.com/terraform-routeros/terraform-provider-routeros/issues/190)) ([a7fc49f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a7fc49f1899f441fabbc63148a1b5c075cbaf27c)), closes [#189](https://github.com/terraform-routeros/terraform-provider-routeros/issues/189)
## [1.3.7](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.6...v1.3.7) (2023-04-23)
### Bug Fixes
* Add `check_gateway` field to `routeros_ip_route` ([#187](https://github.com/terraform-routeros/terraform-provider-routeros/issues/187)) ([20b84ae](https://github.com/terraform-routeros/terraform-provider-routeros/commit/20b84aea4b4ce3af725ebd0f5165cca010f5692a)), closes [#186](https://github.com/terraform-routeros/terraform-provider-routeros/issues/186)
## [1.3.6](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.5...v1.3.6) (2023-04-22)
### Bug Fixes
* ip/route dst_address should not be mandatory ([#185](https://github.com/terraform-routeros/terraform-provider-routeros/issues/185)) ([9cf42c7](https://github.com/terraform-routeros/terraform-provider-routeros/commit/9cf42c7ced6b813a9c0cf8465d1814ab1a5bce98)), closes [#184](https://github.com/terraform-routeros/terraform-provider-routeros/issues/184)
## [1.3.5](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.4...v1.3.5) (2023-04-20)
### Bug Fixes
* Ability to set clamp-tcp-mss on mangle rule ([3226a91](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3226a91963be950ba4111fd133b5e4f104a4fbbe)), closes [#178](https://github.com/terraform-routeros/terraform-provider-routeros/issues/178)
* disabled mangle not seen ([ffb53d6](https://github.com/terraform-routeros/terraform-provider-routeros/commit/ffb53d66cb4edf8b7952f890c1d8e14f6f11b60b)), closes [#175](https://github.com/terraform-routeros/terraform-provider-routeros/issues/175)
## [1.3.4](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.3...v1.3.4) (2023-04-20)
### Bug Fixes
* dns servers cannot be removed ([#179](https://github.com/terraform-routeros/terraform-provider-routeros/issues/179)) ([3db9080](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3db9080137431e5031de9f27d53e8f022154f40a)), closes [#174](https://github.com/terraform-routeros/terraform-provider-routeros/issues/174)
## [1.3.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.2...v1.3.3) (2023-04-19)
### Bug Fixes
* dns servers cannot be removed ([#177](https://github.com/terraform-routeros/terraform-provider-routeros/issues/177)) ([34a73be](https://github.com/terraform-routeros/terraform-provider-routeros/commit/34a73bed579e84568bfc24a3ead4bf8c1c62bbe9)), closes [#174](https://github.com/terraform-routeros/terraform-provider-routeros/issues/174)
## [1.3.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.1...v1.3.2) (2023-04-18)
### Bug Fixes
* dns servers cannot be removed ([#176](https://github.com/terraform-routeros/terraform-provider-routeros/issues/176)) ([1ebc4d9](https://github.com/terraform-routeros/terraform-provider-routeros/commit/1ebc4d98072c86499bb972081ba1649e2af52ef0)), closes [#174](https://github.com/terraform-routeros/terraform-provider-routeros/issues/174)
## [1.3.1](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.3.0...v1.3.1) (2023-04-12)
### Bug Fixes
* Remove default for VRRP interface group ([0cd9b5d](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0cd9b5d41e10932ba631ae4d00b05c0ef948bbf0))
## [1.3.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.2.0...v1.3.0) (2023-04-10)
### Features
* Add support for a "certificate" resource ([898d2ad](https://github.com/terraform-routeros/terraform-provider-routeros/commit/898d2adf540ddcc04d4e535a36aee91fa3558fcd))
## [1.2.0](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.11...v1.2.0) (2023-04-03)
### Features
* Add support for CAPsMAN resources ([514b51f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/514b51fd39250569e4c4112f7d349f98f885d743))
* Add support for composite types (TypeMap), TypeList.Int, TypeSet.Int, TypeSet.String ([8698a18](https://github.com/terraform-routeros/terraform-provider-routeros/commit/8698a18aa3179b281156c4fc311ba0ed5f5692a8))
* Add support for transforming the composite fields of Mikrotik. ([47d9ad3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/47d9ad388753ff22eaee2bc83158920c37b60fd7))
* Add the default actions for system resources ([b3fb513](https://github.com/terraform-routeros/terraform-provider-routeros/commit/b3fb5138177b42e8dfb35a6d489f807fa8032be8))
### Bug Fixes
* Fix the import path ([a195c45](https://github.com/terraform-routeros/terraform-provider-routeros/commit/a195c45c1599b2e3f920c43cbc4e6dbabf8c895d))
* The 'disabled' property must be Computed (read-only) ([c4b85f6](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c4b85f6ae3580f557acc4eaa14cacc371638ebda))
## [1.1.11](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.10...v1.1.11) (2023-03-23)
### Bug Fixes
* routeros_ip_dns - new fields in 7.8 ([#170](https://github.com/terraform-routeros/terraform-provider-routeros/issues/170)) ([c3d3eb3](https://github.com/terraform-routeros/terraform-provider-routeros/commit/c3d3eb3bdb9ac21bded109717bdba5075a1720ee)), closes [#169](https://github.com/terraform-routeros/terraform-provider-routeros/issues/169)
## [1.1.10](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.9...v1.1.10) (2023-03-21)
### Bug Fixes
* Fix the order of document generation in CI ([3793cde](https://github.com/terraform-routeros/terraform-provider-routeros/commit/3793cde6785344aa9c5a092ed9142263a340949e))
## [1.1.9](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.8...v1.1.9) (2023-03-21)
### Bug Fixes
* Fix [#165](https://github.com/terraform-routeros/terraform-provider-routeros/issues/165) for REST responses containing escape sequences  ([#167](https://github.com/terraform-routeros/terraform-provider-routeros/issues/167)) ([646ba4f](https://github.com/terraform-routeros/terraform-provider-routeros/commit/646ba4f6843904ec0122eb89285044104b051aa2))
## [1.1.8](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.7...v1.1.8) (2023-03-12)
### Bug Fixes
* routeros_dns_record does not change resource type and data correctly after [#158](https://github.com/terraform-routeros/terraform-provider-routeros/issues/158) ([4d95e80](https://github.com/terraform-routeros/terraform-provider-routeros/commit/4d95e80e73f8f494be7d3ea5fca382cc4e3f2fc5)), closes [#159](https://github.com/terraform-routeros/terraform-provider-routeros/issues/159)
## [1.1.7](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.6...v1.1.7) (2023-03-11)
### Bug Fixes
* /ip/dns/static errors when trying to change the resource type ([0a935cd](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0a935cd4affd9effdd8c0e8190415d055e4aafa9)), closes [#156](https://github.com/terraform-routeros/terraform-provider-routeros/issues/156)
## [1.1.6](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.5...v1.1.6) (2023-03-10)
### Bug Fixes
* /ip/route - field disabled missing ([0baf464](https://github.com/terraform-routeros/terraform-provider-routeros/commit/0baf464ff8064fa38cf4458e4c56d3a0733f9865)), closes [#149](https://github.com/terraform-routeros/terraform-provider-routeros/issues/149)
## [1.1.5](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.4...v1.1.5) (2023-03-10)
### Bug Fixes
* /ip/dns/record - field type is missing ([2072d14](https://github.com/terraform-routeros/terraform-provider-routeros/commit/2072d1486c2c1ded8259a628dc2e447a519a2a92)), closes [#150](https://github.com/terraform-routeros/terraform-provider-routeros/issues/150)
## [1.1.4](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.3...v1.1.4) (2023-03-04)
### Bug Fixes
* Fix "post-test destroy" error ([38e79a4](https://github.com/terraform-routeros/terraform-provider-routeros/commit/38e79a497b1ff364ffc5c3b3a6e0d11c958d3616))
* Fix /ip/dhcp-server/network required field ([e9c69be](https://github.com/terraform-routeros/terraform-provider-routeros/commit/e9c69be9eca4b6791157c2a00bae0fdc436fec74))
## [1.1.3](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.2...v1.1.3) (2023-02-24)
## [1.1.2](https://github.com/terraform-routeros/terraform-provider-routeros/compare/v1.1.1...v1.1.2) (2023-02-24)
## [1.1.1](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.1.0...v1.1.1) (2023-02-23)
### Bug Fixes
* Set key correctly ([a299647](https://github.com/GNewbury1/terraform-provider-routeros/commit/a299647b7a23891bf6574bfe503bfa3b6d397cbd))
# [1.1.0](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.13...v1.1.0) (2023-02-23)
### Features
* Add new signing key for new org ([7c0364a](https://github.com/GNewbury1/terraform-provider-routeros/commit/7c0364aa3bdfe3905cc7f588f9a114e98cbc76c8))
## [1.0.13](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.12...v1.0.13) (2023-02-22)
### Bug Fixes
* **#122:** Add missing fields to interface list member ([3debe19](https://github.com/GNewbury1/terraform-provider-routeros/commit/3debe192f123463e85a00f0318f92f7996d06906)), closes [#122](https://github.com/GNewbury1/terraform-provider-routeros/issues/122)
## [1.0.12](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.11...v1.0.12) (2023-02-22)
### Bug Fixes
* **#106:** "root_path_cost" not found. ([4d568f5](https://github.com/GNewbury1/terraform-provider-routeros/commit/4d568f54db78297f3b71f4b1403f65214585c4ac)), closes [#106](https://github.com/GNewbury1/terraform-provider-routeros/issues/106)
## [1.0.11](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.10...v1.0.11) (2023-02-20)
### Bug Fixes
* **#106:** Fix internal validation (for release). ([fa3bb93](https://github.com/GNewbury1/terraform-provider-routeros/commit/fa3bb93f22b22dbb6c50296cf6b12f030920f8d6))
## [1.0.9](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.8...v1.0.9) (2023-02-20)
### Bug Fixes
* **#106:** Added "multicast_router" field. ([128efe1](https://github.com/GNewbury1/terraform-provider-routeros/commit/128efe12b91fd2bf6a16536bd618047d4d6200b8)), closes [#106](https://github.com/GNewbury1/terraform-provider-routeros/issues/106)
* **#110:** "host_name" set to Computed. ([d8c80dc](https://github.com/GNewbury1/terraform-provider-routeros/commit/d8c80dcc50dcee15f88aaa4a54574c4f5889a856)), closes [#110](https://github.com/GNewbury1/terraform-provider-routeros/issues/110)
## [1.0.8](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.7...v1.0.8) (2023-02-19)
### Bug Fixes
* **#110:** Typo in hostname field for dhcp lease ([1113a36](https://github.com/GNewbury1/terraform-provider-routeros/commit/1113a3641e44fed551245415f387f1db34690d52)), closes [#110](https://github.com/GNewbury1/terraform-provider-routeros/issues/110)
## [1.0.7](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.6...v1.0.7) (2023-02-17)
### Bug Fixes
* [#106](https://github.com/GNewbury1/terraform-provider-routeros/issues/106) /interface/bridge resource schema (IGMP snooping). ([dd9baaa](https://github.com/GNewbury1/terraform-provider-routeros/commit/dd9baaa9f81571c596c73f649919b6f475f6a327))
* [#109](https://github.com/GNewbury1/terraform-provider-routeros/issues/109) /interface/bridge/port resource schema (STP). ([182b067](https://github.com/GNewbury1/terraform-provider-routeros/commit/182b0679e0f9ec9996aff2cce170906c7cf5bf51))
* /ip/dhcp-server/lease resource schema. ([68a67d4](https://github.com/GNewbury1/terraform-provider-routeros/commit/68a67d48763e7bc8f7f5e9bd141044c5782637f4))
## [1.0.7](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.6...v1.0.7) (2023-02-17)
### Bug Fixes
* [#106](https://github.com/GNewbury1/terraform-provider-routeros/issues/106) /interface/bridge resource schema (IGMP snooping). ([dd9baaa](https://github.com/GNewbury1/terraform-provider-routeros/commit/dd9baaa9f81571c596c73f649919b6f475f6a327))
* [#109](https://github.com/GNewbury1/terraform-provider-routeros/issues/109) /interface/bridge/port resource schema (STP). ([182b067](https://github.com/GNewbury1/terraform-provider-routeros/commit/182b0679e0f9ec9996aff2cce170906c7cf5bf51))
* /ip/dhcp-server/lease resource schema. ([68a67d4](https://github.com/GNewbury1/terraform-provider-routeros/commit/68a67d48763e7bc8f7f5e9bd141044c5782637f4))
## [1.0.6](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.5...v1.0.6) (2023-02-17)
### Bug Fixes
* **#110:** Add missing fields to DhcpServerLease ([100af8f](https://github.com/GNewbury1/terraform-provider-routeros/commit/100af8f7da96ff38a879536f1894118fd9bc858d)), closes [#110](https://github.com/GNewbury1/terraform-provider-routeros/issues/110)
## [1.0.6](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.5...v1.0.6) (2023-02-17)
### Bug Fixes
* **#110:** Add missing fields to DhcpServerLease ([100af8f](https://github.com/GNewbury1/terraform-provider-routeros/commit/100af8f7da96ff38a879536f1894118fd9bc858d)), closes [#110](https://github.com/GNewbury1/terraform-provider-routeros/issues/110)
## [1.0.5](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.4...v1.0.5) (2023-02-17)
### Bug Fixes
* Spaces in resource names ([#102](https://github.com/GNewbury1/terraform-provider-routeros/issues/102) - [#104](https://github.com/GNewbury1/terraform-provider-routeros/issues/104)). ([6dafa4b](https://github.com/GNewbury1/terraform-provider-routeros/commit/6dafa4bd26ea406c5f4e481f201da1f16dd9b747))
## [1.0.4](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.3...v1.0.4) (2023-02-16)
### Bug Fixes
* Add gpg fingerprint to CI ([b315e13](https://github.com/GNewbury1/terraform-provider-routeros/commit/b315e130d338de82a1347c8f91cd4ba442d8d7c3))
## [1.0.2](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.1...v1.0.2) (2023-02-15)
### Bug Fixes
* Create multiple names for the same resource to aid compatibility ([5ed67a7](https://github.com/GNewbury1/terraform-provider-routeros/commit/5ed67a7e78cbf167320e2092c7c276e7410041bd))
* Interface child items had incorrect reference ([be14cb6](https://github.com/GNewbury1/terraform-provider-routeros/commit/be14cb6a2feec52cf5c34cc51924c1df09c90023))
## [1.0.1](https://github.com/GNewbury1/terraform-provider-routeros/compare/v1.0.0...v1.0.1) (2023-02-14)
### Bug Fixes
* IP validation fix ([12c1a23](https://github.com/GNewbury1/terraform-provider-routeros/commit/12c1a230aac5636b80636bd060c4024167d67f64))
================================================

File: files.md
================================================
# routeros_files (Data Source)
## Example Usage
```terraform
data "routeros_files" "files" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `files` (List of Object) (see [below for nested schema](#nestedatt--files))
- `id` (String) The ID of this resource.
<a id="nestedatt--files"></a>
### Nested Schema for `files`
Read-Only:
- `contents` (String)
- `creation_time` (String)
- `id` (String)
- `name` (String)
- `package_architecture` (String)
- `package_built_time` (String)
- `package_name` (String)
- `package_version` (String)
- `size` (Number)
- `type` (String)
================================================

File: firewall.md
================================================
# routeros_firewall (Data Source)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_firewall](ip_firewall.md)
================================================

File: interfaces.md
================================================
# routeros_interfaces (Data Source)
## Example Usage
```terraform
data "routeros_interfaces" "interfaces" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `id` (String) The ID of this resource.
- `interfaces` (List of Object) (see [below for nested schema](#nestedatt--interfaces))
<a id="nestedatt--interfaces"></a>
### Nested Schema for `interfaces`
Read-Only:
- `actual_mtu` (Number)
- `comment` (String)
- `default_name` (String)
- `disabled` (Boolean)
- `fp_rx_byte` (Number)
- `fp_rx_packet` (Number)
- `fp_tx_byte` (Number)
- `fp_tx_packet` (Number)
- `id` (String)
- `l2mtu` (Number)
- `last_link_down_time` (String)
- `last_link_up_time` (String)
- `link_downs` (Number)
- `mac_address` (String)
- `max_l2mtu` (Number)
- `mtu` (String)
- `name` (String)
- `running` (Boolean)
- `rx_byte` (Number)
- `rx_drop` (Number)
- `rx_error` (Number)
- `rx_packet` (Number)
- `slave` (Boolean)
- `tx_byte` (Number)
- `tx_drop` (Number)
- `tx_error` (Number)
- `tx_packet` (Number)
- `tx_queue_drop` (Number)
- `type` (String)
================================================

File: ipv6_addresses.md
================================================
# routeros_ipv6_addresses (Data Source)
## Example Usage
```terraform
data "routeros_ipv6_addresses" "addresses" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `addresses` (List of Object) (see [below for nested schema](#nestedatt--addresses))
- `id` (String) The ID of this resource.
<a id="nestedatt--addresses"></a>
### Nested Schema for `addresses`
Read-Only:
- `actual_interface` (String)
- `address` (String)
- `advertise` (Boolean)
- `comment` (String)
- `disabled` (Boolean)
- `dynamic` (Boolean)
- `eui_64` (Boolean)
- `from_pool` (String)
- `id` (String)
- `interface` (String)
- `invalid` (Boolean)
- `link_local` (Boolean)
- `no_dad` (Boolean)
================================================

File: ipv6_firewall.md
================================================
# routeros_ipv6_firewall (Data Source)
This datasource contains all supported firewall resources:
- rules (aka filter)
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `rules` (Block List) (see [below for nested schema](#nestedblock--rules))
### Read-Only
- `id` (String) The ID of this resource.
<a id="nestedblock--rules"></a>
### Nested Schema for `rules`
Optional:
- `filter` (Map of String) Additional request filtering options.
Read-Only:
- `action` (String)
- `bytes` (Number)
- `chain` (String)
- `comment` (String)
- `connection_bytes` (String)
- `connection_limit` (String)
- `connection_mark` (String)
- `connection_nat_state` (String)
- `connection_rate` (String)
- `connection_state` (String)
- `connection_type` (String)
- `content` (String)
- `disabled` (Boolean)
- `dscp` (Number)
- `dst_address` (String)
- `dst_address_list` (String)
- `dst_address_type` (String)
- `dst_limit` (String)
- `dst_port` (String)
- `dynamic` (Boolean)
- `icmp_options` (String)
- `id` (String)
- `in_bridge_port` (String)
- `in_bridge_port_list` (String)
- `in_interface` (String)
- `in_interface_list` (String)
- `ingress_priority` (Number)
- `invalid` (Boolean)
- `ipsec_policy` (String)
- `limit` (String)
- `log` (Boolean)
- `log_prefix` (String)
- `nth` (String)
- `out_bridge_port` (String)
- `out_bridge_port_list` (String)
- `out_interface` (String)
- `out_interface_list` (String)
- `packet_mark` (String)
- `packet_size` (String)
- `packets` (Number)
- `per_connection_classifier` (String)
- `port` (String)
- `priority` (Number)
- `protocol` (String)
- `random` (Number)
- `reject_with` (String)
- `routing_mark` (String)
- `routing_table` (String)
- `src_address` (String)
- `src_address_list` (String)
- `src_address_type` (String)
- `src_mac_address` (String)
- `src_port` (String)
- `tcp_flags` (String)
- `tcp_mss` (String)
- `time` (String)
- `tls_host` (String)
- `ttl` (String)
================================================

File: ip_addresses.md
================================================
# routeros_ip_addresses (Data Source)
## Example Usage
```terraform
data "routeros_ip_addresses" "ip_addresses" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `addresses` (List of Object) (see [below for nested schema](#nestedatt--addresses))
- `id` (String) The ID of this resource.
<a id="nestedatt--addresses"></a>
### Nested Schema for `addresses`
Read-Only:
- `actual_interface` (String)
- `address` (String)
- `comment` (String)
- `disabled` (Boolean)
- `dynamic` (Boolean)
- `id` (String)
- `interface` (String)
- `invalid` (Boolean)
- `network` (String)
================================================

File: ip_arp.md
================================================
# routeros_ip_arp (Data Source)
## Example Usage
```terraform
data "routeros_ip_arp" "data" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `data` (List of Object) (see [below for nested schema](#nestedatt--data))
- `id` (String) The ID of this resource.
<a id="nestedatt--data"></a>
### Nested Schema for `data`
Read-Only:
- `address` (String)
- `complete` (Boolean)
- `dhcp` (Boolean)
- `disabled` (Boolean)
- `dynamic` (Boolean)
- `id` (String)
- `interface` (String)
- `invalid` (Boolean)
- `mac_address` (String)
- `published` (Boolean)
================================================

File: ip_dhcp_server_leases.md
================================================
# routeros_ip_dhcp_server_leases (Data Source)
## Example Usage
```terraform
data "routeros_ip_dhcp_server_leases" "data" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `data` (List of Object) (see [below for nested schema](#nestedatt--data))
- `id` (String) The ID of this resource.
<a id="nestedatt--data"></a>
### Nested Schema for `data`
Read-Only:
- `address` (String)
- `address_lists` (String)
- `blocked` (Boolean)
- `comment` (String)
- `dhcp_option` (String)
- `disabled` (Boolean)
- `dynamic` (Boolean)
- `id` (String)
- `last_seen` (String)
- `mac_address` (String)
- `radius` (Boolean)
- `server` (String)
- `status` (String)
================================================

File: ip_firewall.md
================================================
# routeros_ip_firewall (Data Source)
This datasource contains all supported firewall resources:
- address_list
- nat
- mangle
- rules (aka filter)
## Example Usage
```terraform
data "routeros_ip_firewall" "fw" {
  rules {
    filter = {
      chain   = "input"
      comment = "rule_2"
    }
  }
  rules {
    filter = {
      chain = "forward"
    }
  }
  nat {}
}
output "rules" {
  value = [for value in data.routeros_ip_firewall.fw.rules : [value.id, value.src_address]]
}
output "nat" {
  value = [for value in data.routeros_ip_firewall.fw.nat : [value.id, value.comment]]
}
resource "routeros_ip_firewall" "rule_3" {
  action       = "accept"
  chain        = "input"
  comment      = "rule_3"
  src_address  = "192.168.0.5"
  place_before = data.routeros_ip_firewall_filter.fw.rules[0].id
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `address_list` (Block List) (see [below for nested schema](#nestedblock--address_list))
- `mangle` (Block List) (see [below for nested schema](#nestedblock--mangle))
- `nat` (Block List) (see [below for nested schema](#nestedblock--nat))
- `rules` (Block List) (see [below for nested schema](#nestedblock--rules))
### Read-Only
- `id` (String) The ID of this resource.
<a id="nestedblock--address_list"></a>
### Nested Schema for `address_list`
Optional:
- `filter` (Map of String) Additional request filtering options.
Read-Only:
- `address` (String)
- `comment` (String)
- `creation_time` (String)
- `disabled` (Boolean)
- `dynamic` (Boolean)
- `id` (String)
- `list` (String)
- `timeout` (String)
<a id="nestedblock--mangle"></a>
### Nested Schema for `mangle`
Optional:
- `filter` (Map of String) Additional request filtering options.
Read-Only:
- `action` (String)
- `address_list` (String)
- `address_list_timeout` (String)
- `bytes` (Number)
- `chain` (String)
- `comment` (String)
- `connection_bytes` (String)
- `connection_limit` (String)
- `connection_mark` (String)
- `connection_nat_state` (String)
- `connection_rate` (String)
- `connection_state` (String)
- `connection_type` (String)
- `content` (String)
- `disabled` (Boolean)
- `dscp` (Number)
- `dst_address` (String)
- `dst_address_list` (String)
- `dst_address_type` (String)
- `dst_limit` (String)
- `dst_port` (String)
- `dynamic` (Boolean)
- `fragment` (Boolean)
- `hotspot` (String)
- `icmp_options` (String)
- `id` (String)
- `in_bridge_port` (String)
- `in_bridge_port_list` (String)
- `in_interface` (String)
- `in_interface_list` (String)
- `ingress_priority` (Number)
- `invalid` (Boolean)
- `ipsec_policy` (String)
- `ipv4_options` (String)
- `jump_target` (String)
- `layer7_protocol` (String)
- `limit` (String)
- `log` (Boolean)
- `log_prefix` (String)
- `new_connection_mark` (String)
- `new_dscp` (Number)
- `new_mss` (Number)
- `new_packet_mark` (String)
- `new_priority` (String)
- `new_routing_mark` (String)
- `new_ttl` (String)
- `nth` (String)
- `out_bridge_port` (String)
- `out_bridge_port_list` (String)
- `out_interface` (String)
- `out_interface_list` (String)
- `packet_mark` (String)
- `packet_size` (String)
- `packets` (Number)
- `passthrough` (Boolean)
- `per_connection_classifier` (String)
- `port` (String)
- `protocol` (String)
- `psd` (String)
- `random` (Number)
- `route_dst` (String)
- `routing_mark` (String)
- `src_address` (String)
- `src_address_list` (String)
- `src_address_type` (String)
- `src_mac_address` (String)
- `src_port` (String)
- `tcp_flags` (String)
- `tcp_mss` (String)
- `time` (String)
- `tls_host` (String)
- `ttl` (String)
<a id="nestedblock--nat"></a>
### Nested Schema for `nat`
Optional:
- `filter` (Map of String) Additional request filtering options.
Read-Only:
- `action` (String)
- `address_list` (String)
- `address_list_timeout` (String)
- `bytes` (Number)
- `chain` (String)
- `comment` (String)
- `connection_bytes` (String)
- `connection_limit` (String)
- `connection_mark` (String)
- `connection_rate` (String)
- `connection_type` (String)
- `content` (String)
- `disabled` (Boolean)
- `dscp` (Number)
- `dst_address` (String)
- `dst_address_list` (String)
- `dst_address_type` (String)
- `dst_limit` (String)
- `dst_port` (String)
- `dynamic` (Boolean)
- `fragment` (Boolean)
- `hotspot` (String)
- `icmp_options` (String)
- `id` (String)
- `in_bridge_port` (String)
- `in_bridge_port_list` (String)
- `in_interface` (String)
- `in_interface_list` (String)
- `ingress_priority` (Number)
- `invalid` (Boolean)
- `ipsec_policy` (String)
- `ipv4_options` (String)
- `jump_target` (String)
- `layer7_protocol` (String)
- `limit` (String)
- `log` (Boolean)
- `log_prefix` (String)
- `nth` (String)
- `out_bridge_port` (String)
- `out_bridge_port_list` (String)
- `out_interface` (String)
- `out_interface_list` (String)
- `packet_mark` (String)
- `packet_size` (String)
- `packets` (Number)
- `per_connection_classifier` (String)
- `port` (String)
- `priority` (Number)
- `protocol` (String)
- `psd` (String)
- `random` (Number)
- `routing_mark` (String)
- `same_not_by_dst` (Boolean)
- `src_address` (String)
- `src_address_list` (String)
- `src_address_type` (String)
- `src_mac_address` (String)
- `src_port` (String)
- `tcp_mss` (String)
- `time` (String)
- `to_addresses` (String)
- `to_ports` (String)
- `ttl` (String)
<a id="nestedblock--rules"></a>
### Nested Schema for `rules`
Optional:
- `filter` (Map of String) Additional request filtering options.
Read-Only:
- `action` (String)
- `address_list_timeout` (String)
- `bytes` (Number)
- `chain` (String)
- `comment` (String)
- `connection_bytes` (String)
- `connection_limit` (String)
- `connection_mark` (String)
- `connection_nat_state` (String)
- `connection_rate` (String)
- `connection_state` (String)
- `connection_type` (String)
- `content` (String)
- `disabled` (Boolean)
- `dscp` (Number)
- `dst_address` (String)
- `dst_address_list` (String)
- `dst_address_type` (String)
- `dst_limit` (String)
- `dst_port` (String)
- `dynamic` (Boolean)
- `fragment` (Boolean)
- `hotspot` (String)
- `hw_offload` (Boolean)
- `icmp_options` (String)
- `id` (String)
- `in_bridge_port` (String)
- `in_bridge_port_list` (String)
- `in_interface` (String)
- `in_interface_list` (String)
- `ingress_priority` (Number)
- `invalid` (Boolean)
- `ipsec_policy` (String)
- `ipv4_options` (String)
- `jump_target` (String)
- `layer7_protocol` (String)
- `limit` (String)
- `log` (Boolean)
- `log_prefix` (String)
- `nth` (String)
- `out_bridge_port` (String)
- `out_bridge_port_list` (String)
- `out_interface` (String)
- `out_interface_list` (String)
- `packet_mark` (String)
- `packet_size` (String)
- `packets` (Number)
- `per_connection_classifier` (String)
- `port` (String)
- `priority` (Number)
- `protocol` (String)
- `psd` (String)
- `random` (Number)
- `reject_with` (String)
- `routing_mark` (String)
- `routing_table` (String)
- `src_address` (String)
- `src_address_list` (String)
- `src_address_type` (String)
- `src_mac_address` (String)
- `src_port` (String)
- `tcp_flags` (String)
- `tcp_mss` (String)
- `time` (String)
- `tls_host` (String)
- `ttl` (String)
================================================

File: ip_routes.md
================================================
# routeros_ip_routes (Data Source)
## Example Usage
```terraform
data "routeros_ip_routes" "ip_routes" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `id` (String) The ID of this resource.
- `routes` (List of Object) (see [below for nested schema](#nestedatt--routes))
<a id="nestedatt--routes"></a>
### Nested Schema for `routes`
Read-Only:
- `active` (Boolean)
- `blackhole` (Boolean)
- `comment` (String)
- `connect` (Boolean)
- `dhcp` (Boolean)
- `disabled` (Boolean)
- `distance` (Number)
- `dst_address` (String)
- `dynamic` (Boolean)
- `ecmp` (Boolean)
- `gateway` (String)
- `hw_offloaded` (Boolean)
- `id` (String)
- `immediate_gw` (String)
- `inactive` (Boolean)
- `local_address` (String)
- `pref_src` (String)
- `routing_table` (String)
- `scope` (Number)
- `static` (Boolean)
- `suppress_hw_offload` (Boolean)
- `target_scope` (Number)
- `vrf_interface` (String)
================================================

File: ip_services.md
================================================
# routeros_ip_services (Data Source)
## Example Usage
```terraform
data "routeros_ip_services" "router" {
  provider = routeros.router
}
resource "routeros_ip_service" "router-disabled" {
  provider = routeros.router
  for_each = { for s in data.routeros_ip_services.router.services : s.name => s if s.name != "www-ssl" }
  disabled = true
  numbers  = each.value.name
  port     = each.value.port
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `filter` (Map of String) Additional request filtering options.
### Read-Only
- `id` (String) The ID of this resource.
- `services` (List of Object) (see [below for nested schema](#nestedatt--services))
<a id="nestedatt--services"></a>
### Nested Schema for `services`
Read-Only:
- `address` (String)
- `certificate` (String)
- `disabled` (Boolean)
- `id` (String)
- `invalid` (String)
- `name` (String)
- `port` (Number)
- `tls_version` (String)
- `vrf` (String)
================================================

File: system_resource.md
================================================
# routeros_system_resource (Data Source)
## Example Usage
```terraform
data "routeros_system_resource" "data" {}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
### Read-Only
- `architecture_name` (String)
- `board_name` (String)
- `build_time` (String)
- `cpu` (String)
- `cpu_count` (Number)
- `cpu_frequency` (Number)
- `cpu_load` (Number)
- `factory_software` (String)
- `free_hdd_space` (Number)
- `free_memory` (Number)
- `id` (String) The ID of this resource.
- `platform` (String)
- `total_hdd_space` (Number)
- `total_memory` (Number)
- `uptime` (String)
- `version` (String)
- `write_sect_since_reboot` (Number)
- `write_sect_total` (Number)
================================================

File: x509.md
================================================
# routeros_x509 (Data Source)
## Example Usage
```terraform
# You can keep indents in front of the content lines of the certificate.
# The normalized certificate is available through the `pem` attribute
data "routeros_x509" "cert" {
  data = <<EOT
	-----BEGIN CERTIFICATE-----
	MIIBlTCCATugAwIBAgIINLsws71B5zIwCgYIKoZIzj0EAwIwHzEdMBsGA1UEAwwU
	RXh0ZXJuYWwgQ2VydGlmaWNhdGUwHhcNMjQwNTE3MjEyOTUzWhcNMjUwNTE3MjEy
	OTUzWjAfMR0wGwYDVQQDDBRFeHRlcm5hbCBDZXJ0aWZpY2F0ZTBZMBMGByqGSM49
	AgEGCCqGSM49AwEHA0IABKE1g0Qj4ujIold9tklu2z4BUu/K7xDFF5YmedtOfJyM
	1/80APNboqn71y4m4XNE1JNtQuR2bSZPHVrzODkR16ujYTBfMA8GA1UdEwEB/wQF
	MAMBAf8wDgYDVR0PAQH/BAQDAgG2MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEF
	BQcDAjAdBgNVHQ4EFgQUNXd5bvluIV9YAhGc5yMHc6OzXpMwCgYIKoZIzj0EAwID
	SAAwRQIhAODte/qS6CE30cvnQpxP/ObWBPIPZnHtkFHIIC1AOSXwAiBGCGQE+aJY
	W72Rw0Y1ckvlt6sU0urkzGuj5wxVF/gSYA==
	-----END CERTIFICATE-----
EOT
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `data` (String) X509 certificate in PEM format.
### Read-Only
- `akid` (String)
- `authority` (Boolean)
- `common_name` (String)
- `digest_algorithm` (String)
- `fingerprint` (String)
- `id` (String) The ID of this resource.
- `invalid_after` (String)
- `invalid_before` (String)
- `issuer` (String)
- `key_type` (String)
- `pem` (String)
- `serial_number` (String)
- `signature_algorithm` (String)
- `skid` (String)
- `subject` (String)
- `subject_alt_name` (String)
- `version` (Number)
================================================

File: easy_import.md
================================================
# Install package
Original [issue](https://github.com/terraform-routeros/terraform-provider-routeros/issues/488)
## Example
```shell
#!/bin/bash
USER=admin
PASS=
HOST=http://router.local
i=0
curl -s -u ${USER}:${PASS} ${HOST}/rest/ip/firewall/address-list | jq -c '.[] | select(.dynamic | ascii_downcase == "false") | {index: .".id", address: .address, comment: .comment, list: .list}'  | while read rec; do
  index=$(echo $rec | jq .index)
  idx=$(printf "%00004d" $i)
  # echo $rec
  bash -cv "tofu state rm 'module.dev-gw0.routeros_ip_firewall_addr_list.address_list[\"$idx\"]'"
  bash -cv "tofu import 'module.dev-gw0.routeros_ip_firewall_addr_list.address_list[\"$idx\"]' $index"
  let i=${i}+1
done
```
```terraform
variable "address_list" {
  type = list(object({
    address = string
    comment = optional(string)
    disabled = optional(bool, false)
    dynamic  = optional(bool, false)
    list     = string
  }))
  default = [
    { address="192.168.88.11", comment="example 2", list="srv" },
    { address="192.168.88.12", comment="example 2", list="srv" },
    { address="192.168.88.1", comment="example", list="routeros" },
]
locals {
  # https://discuss.hashicorp.com/t/does-map-sort-keys/12056/2
  # Map keys are always iterated in lexicographical order!
  address_list_map = { for idx, rule in var.address_list : format("%00004d", idx) => rule }
}
resource "routeros_ip_firewall_addr_list" "address_list" {
  for_each = local.address_list_map
  address  = each.value.address
  comment  = each.value.comment
  disabled = each.value.disabled
  list     = each.value.list
}
```
================================================

File: install_package.md
================================================
# Install package
The original example package installation is available in the [Schwitzd](https://github.com/Schwitzd/IaC-HomeRouter/blob/main/container_backend.tf) repository.
## Example
```terraform
resource "null_resource" "download_container_npk" {
  provisioner "local-exec" {
    command = <<EOT
      chmod +x ./helper/download_routeros_packages.sh
      ./helper/download_routeros_packages.sh ${local.system_architecture} "${local.system_version}" "container"
    EOT
  }
}
resource "null_resource" "upload_container_npk" {
  provisioner "local-exec" {
    command = "scp -i ${local.router_ssh_key} \"/tmp/routeros_packages/${local.container_npk_name}\" ${local.router_user}@${var.router_ip}:/${local.container_npk_name}"
  }
  depends_on = [ null_resource.download_container_npk ]
}
resource "null_resource" "install_container_npk" {
  provisioner "local-exec" {
      command = <<EOT
        ssh -i ${local.router_ssh_key} ${local.router_user}@${var.router_ip} '/system reboot'; sleep 3
        until ssh -i ${local.router_ssh_key} -o ConnectTimeout=2 ${local.router_user}@${var.router_ip} ':put True' 2> /dev/null
        do
          echo "Waiting for router to reboot and become available..."
          sleep 10
        done
      EOT
  }
  depends_on = [ null_resource.upload_container_npk ]
}
```
```shell
#!/bin/bash
# Input parameters
ARCHITECTURE_NAME=$1
VERSION=$2
PACKAGE_NAME_PREFIX=$3
# Define the base URL and package format
BASE_URL="https://download.mikrotik.com/routeros"
PACKAGE_FORMAT="all_packages-${ARCHITECTURE_NAME}-${VERSION}.zip"
# Construct the full URL
FULL_URL="${BASE_URL}/${VERSION}/${PACKAGE_FORMAT}"
# Define the download and extraction paths
DOWNLOAD_PATH="/tmp/${PACKAGE_FORMAT}"
EXTRACT_PATH="/tmp/routeros_packages"
# Download the package
echo "Downloading package from: ${FULL_URL}"
curl -o "${DOWNLOAD_PATH}" "${FULL_URL}"
# Verify download
if [ $? -ne 0 ]; then
  echo "Failed to download the package."
  exit 1
fi
# Create the extraction directory
mkdir -p "${EXTRACT_PATH}"
# List all files in the ZIP archive and filter by the PACKAGE_NAME_PREFIX
echo "Finding package that starts with: ${PACKAGE_NAME_PREFIX}"
MATCHED_FILES=$(unzip -l "${DOWNLOAD_PATH}" | awk '{print $4}' | grep "^${PACKAGE_NAME_PREFIX}")
# Check if any files were matched
if [ -z "$MATCHED_FILES" ]; then
  echo "No files found starting with '${PACKAGE_NAME_PREFIX}'."
  exit 1
fi
# Extract matched files
for FILE in $MATCHED_FILES; do
  echo "Extracting: ${FILE}"
  unzip -jo "${DOWNLOAD_PATH}" "${FILE}" -d "${EXTRACT_PATH}"
  if [ $? -ne 0 ]; then
    echo "Failed to extract: ${FILE}"
    exit 1
  fi
done
echo "Extraction completed successfully in: ${EXTRACT_PATH}"
```
================================================

File: index.md
================================================
---
# generated by https://github.com/hashicorp/terraform-plugin-docs
page_title: "RouterOS Provider"
subcategory: ""
description: |-
    A provider to integrate with the REST API introduced in RouterOS v7
---
# RouterOS Provider
To get started with the provider, you first need to enable the REST API on your router. [You can follow the Mikrotik documentation on this](https://help.mikrotik.com/docs/display/ROS/REST+API), but the gist is to create an SSL cert (in `/system/certificates`) and enable the `web-ssl` service (in `/ip/services`) which uses that certificate.
## Example Usage
```terraform
terraform {
  required_providers {
    routeros = {
      source = "terraform-routeros/routeros"
    }
  }
}
provider "routeros" {
  hosturl        = "https://router.local"        # env ROS_HOSTURL or MIKROTIK_HOST
  username       = "admin"                       # env ROS_USERNAME or MIKROTIK_USER
  password       = ""                            # env ROS_PASSWORD or MIKROTIK_PASSWORD
  ca_certificate = "/path/to/ca/certificate.pem" # env ROS_CA_CERTIFICATE or MIKROTIK_CA_CERTIFICATE
  insecure       = true                          # env ROS_INSECURE or MIKROTIK_INSECURE
}
resource "routeros_interface_gre" "gre_hq" {
  name           = "gre-hq-1"
  remote_address = "10.77.3.26"
  disabled       = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `hosturl` (String) URL of the ROS router. Include including the scheme:
  - `http` new REST API
  - `https` new REST API with TLS/SSL
  - `api` old API without TLS/SSL on port 8728
  - `apis` old API with TLS/SSL 8729
### Optional
- `insecure` (Boolean) Whether to verify the SSL certificate or not
- `password` (String, Sensitive) Password for the ROS user
- `username` (String) Username for the ROS user
================================================

File: bridge.md
================================================
# routeros_bridge (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_bridge](interface_bridge.md)
================================================

File: bridge_mlag.md
================================================
# routeros_bridge_mlag (Resource)
## Example Usage
```terraform
resource "routeros_bridge_mlag" "mlag" {
  bridge    = "bridge1"
  peer_port = "stack-link"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `bridge` (String) The bridge interface where MLAG is being created.
- `peer_port` (String) An interface that will be used as a peer port. Both peer devices are using inter-chassis communication over these peer ports to establish MLAG and update the host table. Peer port should be isolated on a different untagged VLAN using a pvid setting. Peer port can be configured as a bonding interface.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_cloud.test .
```
================================================

File: bridge_port.md
================================================
# routeros_bridge_port (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_bridge_port](interface_bridge_port.md)
================================================

File: bridge_vlan.md
================================================
# routeros_bridge_vlan (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_bridge_vlan](interface_bridge_vlan.md)
================================================

File: capsman_aaa.md
================================================
# routeros_capsman_aaa (Resource)
## Example Usage
```terraform
resource "routeros_capsman_aaa" "test_3a" {
  called_format = "ssid"
  mac_mode      = "as-username-and-password"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `called_format` (String) Format of how the 'called-id' identifier will be passed to RADIUS. When configuring radius server clients, you can specify 'called-id' in order to separate multiple entires.
- `interim_update` (String) When RADIUS accounting is used, Access Point periodically sends accounting information updates to the RADIUS server. This property specifies the default update interval that can be overridden by the RADIUS server using the Acct-Interim-Interval attribute.
- `mac_caching` (String) If this value is set to a time interval, the Access Point will cache RADIUS MAC authentication responses for a specified time, and will not contact the RADIUS server if matching cache entry already exists. The value disabled will disable the cache, Access Point will always contact the RADIUS server.
- `mac_format` (String) Controls how the MAC address of the client is encoded by Access Point in the User-Name attribute of the MAC authentication and MAC accounting RADIUS requests.
- `mac_mode` (String) By default Access Point uses an empty password, when sending Access-Request during MAC authentication. When this property is set to as-username-and-password, Access Point will use the same value for the User-Password attribute as for the User-Name attribute.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_capsman_aaa.test_3a .
```
================================================

File: capsman_access_list.md
================================================
# routeros_capsman_access_list (Resource)
## Example Usage
```terraform
resource "routeros_capsman_datapath" "test_rule" {
  comment                   = "Catch-all"
  interface                 = "cap1"
  signal_range              = "-120..-85"
  allow_signal_out_of_range = "20s"
  action                    = "reject"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `action` (String) An action to take when a client matches.
- `allow_signal_out_of_range` (String) An option that permits the client's signal to be out of the range always or for some time interval.
- `ap_tx_limit` (Number) Transmission speed limit in the direction of the client..
- `client_to_client_forwarding` (Boolean) An option that specifies whether to allow forwarding data between clients connected to the same interface.
- `client_tx_limit` (Number) Transmission speed limit in the direction of the access point.
- `comment` (String)
- `disabled` (Boolean)
- `interface` (String) Interface name to compare with an interface to which the client actually connects to.
- `mac_address` (String) MAC address of the client.
- `mac_mask` (String) MAC address mask to apply when comparing clients' addresses.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `private_passphrase` (String) PSK passphrase for the client if some PSK authentication algorithm is used.
- `radius_accounting` (Boolean) An option that specifies if RADIUS traffic accounting should be used in case of RADIUS authentication of the client.
- `signal_range` (String) The range in which the client signal must fall.
- `ssid_regexp` (String) The regular expression to compare the actual SSID the client connects to.
- `time` (String) Time of the day and days of the week when the rule is applicable.
- `vlan_id` (Number) VLAN ID to use if vlan-mode enables use of VLAN tagging.
- `vlan_mode` (String) VLAN tagging mode specifies if traffic coming from a client should get tagged and untagged when it goes back to the client.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/access-list get [print show-ids]]
terraform import routeros_capsman_access_list.test_rule "*1"
```
================================================

File: capsman_channel.md
================================================
# routeros_capsman_channel (Resource)
## Example Usage
```terraform
resource "routeros_capsman_channel" "test_channel" {
  name                  = "test_channel"
  comment               = "test_channel"
  band                  = "2ghz-b/g/n"
  control_channel_width = "10mhz"
  extension_channel     = "eCee"
  frequency             = [2412]
  reselect_interval     = "1h"
  save_selected         = true
  secondary_frequency   = ["disabled"]
  skip_dfs_channels     = true
  tx_power              = 20
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `band` (String) Define operational radio frequency band and mode taken from hardware capability of wireless card.
- `comment` (String)
- `control_channel_width` (String) Control channel width.
- `extension_channel` (String) Extension channel configuration. (E.g. Ce = extension channel is above Control channel, eC = extension channel is below Control channel)
- `frequency` (List of Number) Channel frequency value in MHz on which AP will operate. If left blank, CAPsMAN will automatically determine the best frequency that is least occupied.
- `reselect_interval` (String) The interval after which the least occupied frequency is chosen, can be defined as a random interval, ex. as '30m..60m'. Works only if channel.frequency is left blank.
- `save_selected` (Boolean) If channel frequency is chosen automatically and channel.reselect-interval is used, then saves the last picked frequency.
- `secondary_frequency` (List of String) Specifies the second frequency that will be used for 80+80MHz configuration. Set it to Disabled in order to disable 80+80MHz capability.
- `skip_dfs_channels` (Boolean) If channel.frequency is left blank, the selection will skip DFS channels.
- `tx_power` (Number) TX  Power for CAP interface (for the whole interface not for individual  chains) in dBm. It is not possible to set higher than allowed by country  regulations or interface. By default max allowed by country or  interface is used.
- `width` (String) Channel Width in MHz.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/channel get [print show-ids]]
terraform import routeros_capsman_channel.test_channel "*1"
```
================================================

File: capsman_configuration.md
================================================
# routeros_capsman_configuration (Resource)
## Example Usage
```terraform
resource "routeros_capsman_configuration" "test_configuration" {
  comment              = "Comment"
  country              = "no_country_set"
  disconnect_timeout   = "1s150ms"
  distance             = "indoors"
  frame_lifetime       = "0.12" // 120ms
  guard_interval       = "long"
  hide_ssid            = true
  hw_protection_mode   = "rts-cts"
  hw_retries           = 1
  installation         = "indoor"
  keepalive_frames     = "enabled"
  load_balancing_group = ""
  max_sta_count        = 1
  mode                 = "ap"
  multicast_helper     = "full"
  name                 = "test_configuration"
  rx_chains            = [1, 3]
  ssid                 = "SSID"
  tx_chains            = [0, 2]
}
resource "routeros_capsman_channel" "test_channel" {
  name = "test-channel-config"
}
resource "routeros_capsman_datapath" "test_datapath" {
  name = "test-datapath-config"
}
resource "routeros_capsman_rates" "test_rates" {
  name = "test-rates-config"
}
resource "routeros_capsman_security" "test_security" {
  name = "test-security-config"
}
resource "routeros_capsman_configuration" "test_configuration_2" {
  name = "test_configuration_name"
  channel = {
    config                = "${routeros_capsman_channel.test_channel.name}"
    band                  = "2ghz-b/g/n"
    control_channel_width = "10mhz"
    extension_channel     = "eCee"
    frequency             = 2412
    reselect_interval     = "1h"
    save_selected         = "true"
    secondary_frequency   = "disabled"
    skip_dfs_channels     = "true"
    tx_power              = 20
  }
  datapath = {
    config                      = "${routeros_capsman_datapath.test_datapath.name}"
    arp                         = "local-proxy-arp"
    bridge                      = "bridge"
    bridge_cost                 = "100"
    bridge_horizon              = "200"
    client_to_client_forwarding = "true"
    interface_list              = "static"
    l2mtu                       = "1450"
    local_forwarding            = "true"
    mtu                         = "1500"
    vlan_id                     = "101"
    vlan_mode                   = "no-tag"
    //   openflow_switch             = "aaa"
  }
  rates = {
    config            = "${routeros_capsman_rates.test_rates.name}"
    basic             = "1Mbps,5.5Mbps,6Mbps,18Mbps,36Mbps,54Mbps"
    ht_basic_mcs      = "mcs-0,mcs-7,mcs-11,mcs-14,mcs-16,mcs-21"
    ht_supported_mcs  = "mcs-3,mcs-8,mcs-10,mcs-13,mcs-17,mcs-18"
    supported         = "2Mbps,11Mbps,9Mbps,12Mbps,24Mbps,48Mbps"
    vht_basic_mcs     = "none"
    vht_supported_mcs = "mcs0-9,mcs0-7"
  }
  security = {
    config                = "${routeros_capsman_security.test_security.name}"
    authentication_types  = "wpa-psk,wpa-eap"
    disable_pmkid         = "true"
    eap_methods           = "eap-tls,passthrough"
    eap_radius_accounting = "true"
    encryption            = "aes-ccm,tkip"
    group_encryption      = "aes-ccm"
    group_key_update      = "1h"
    passphrase            = "AAAAAAAAA"
    tls_certificate       = "none"
    tls_mode              = "verify-certificate"
  }
  depends_on = [
    routeros_capsman_channel.test_channel,
    routeros_capsman_datapath.test_datapath,
    routeros_capsman_rates.test_rates,
    routeros_capsman_security.test_security
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `channel` (Map of String) Channel inline settings.
- `comment` (String)
- `country` (String) Limits available bands, frequencies and maximum transmit power for each frequency. Also specifies default value of scan-list. Value no_country_set is an FCC compliant set of channels.
- `datapath` (Map of String) Datapath inline settings.
- `disconnect_timeout` (String) This interval is measured from third sending failure on the lowest data rate. At this point 3 * (hw-retries + 1) frame transmits on the lowest data rate had failed. During disconnect-timeout packet transmission will be retried with on-fail-retry-time interval. If no frame can be transmitted successfully during disconnect-timeout, the connection is closed, and this event is logged as "extensive data loss". Successful frame transmission resets this timer.
- `distance` (String) How long to wait for confirmation of unicast frames (ACKs) before considering transmission unsuccessful, or in short ACK-Timeout.
- `frame_lifetime` (String) Discard frames that have been queued for sending longer than frame-lifetime. By default, when value of this property is 0, frames are discarded only after connection is closed (format: 0.00 sec).
- `guard_interval` (String) Whether to allow use of short guard interval (refer to 802.11n MCS specification to see how this may affect throughput). "any" will use either short or long, depending on data rate, "long" will use long.
- `hide_ssid` (Boolean) This property has effect only in AP mode. Setting it to yes can remove this network from the list of wireless networks that are shown by some client software. Changing this setting does not improve the security of the wireless network, because SSID is included in other frames sent by the AP.
- `hw_protection_mode` (String) Frame protection support property. [See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#Frame_protection_support_(RTS/CTS)).
- `hw_retries` (Number) Number of times sending frame is retried without considering it a transmission failure. [See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless)
- `installation` (String) Adjusts scan-list to use indoor, outdoor or all frequencies for the country that is set.
- `keepalive_frames` (String) If a client has not communicated for around 20 seconds, AP sends a "keepalive-frame".
- `load_balancing_group` (String) Tags the interface to the load balancing group. For a client to connect to interface in this group, the interface should have the same number of already connected clients as all other interfaces in the group or smaller. Useful in setups where ranges of CAPs mostly overlap.
- `max_sta_count` (Number) Maximum number of associated clients.
- `mode` (String) Set operational mode. Only **ap** currently supported.
- `multicast_helper` (String) When set to full multicast packets will be sent with unicast destination MAC address, resolving multicast problem on a wireless link. This option should be enabled only on the access point, clients should be configured in station-bridge mode.
- `rates` (Map of String) Rates inline settings.
- `rx_chains` (List of Number) Which antennas to use for receive.
- `security` (Map of String) Security inline settings.
- `ssid` (String) SSID (service set identifier) is a name broadcast in the beacons that identifies wireless network.
- `tx_chains` (List of Number) Which antennas to use for transmit.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/configuration get [print show-ids]]
terraform import routeros_capsman_configuration.test_configuration_2 "*1"
```
================================================

File: capsman_datapath.md
================================================
# routeros_capsman_datapath (Resource)
## Example Usage
```terraform
resource "routeros_capsman_datapath" "test_datapath" {
  name                        = "test_datapath"
  comment                     = "test_datapath"
  arp                         = "local-proxy-arp"
  bridge                      = "bridge"
  bridge_cost                 = 100
  bridge_horizon              = 200
  client_to_client_forwarding = true
  interface_list              = "static"
  l2mtu                       = 1450
  local_forwarding            = true
  mtu                         = 1500
  vlan_id                     = 101
  vlan_mode                   = "no-tag"
  //  openflow_switch             = "aaa"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `arp` (String) ARP mode. See [docs](https://wiki.mikrotik.com/wiki/Manual:IP/ARP#ARP_Modes) for info.
- `bridge` (String) Bridge to which particular interface should be automatically added as port. Required only when local-forwarding is not used.
- `bridge_cost` (Number) Bridge port cost to use when adding as bridge port.
- `bridge_horizon` (Number) Bridge horizon to use when adding as bridge port.
- `client_to_client_forwarding` (Boolean) Controls if client-to-client forwarding between wireless clients connected to interface should be allowed, in local forwarding mode this function is performed by CAP, otherwise it is performed by CAPsMAN.
- `comment` (String)
- `interface_list` (String) Interface list name.
- `l2mtu` (Number) Layer2 MTU size.
- `local_forwarding` (Boolean) Controls forwarding mode. If disabled, all L2 and L3 data will be forwarded to CAPsMAN, and further forwarding decisions will be made only then. See [docs](https://wiki.mikrotik.com/wiki/Manual:CAPsMAN#Local_Forwarding_Mode) for info.
- `mtu` (Number) MTU size.
- `openflow_switch` (String) OpenFlow switch to add interface to, as port when enabled.
- `vlan_id` (Number) VLAN ID to assign to interface if vlan-mode enables use of VLAN tagging.
- `vlan_mode` (String) VLAN tagging mode specifies if VLAN tag should be assigned to interface (causes all received data to get tagged with VLAN tag and allows interface to only send out data tagged with given tag)
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/datapath get [print show-ids]]
terraform import routeros_capsman_datapath.test_datapath "*1"
```
================================================

File: capsman_interface.md
================================================
# routeros_capsman_interface (Resource)
## Example Usage
```terraform
resource "routeros_capsman_channel" "channel1" {
  name      = "1"
  band      = "2ghz-g/n"
  frequency = [2412]
}
resource "routeros_capsman_interface" "cap1" {
  name = "cap1"
  channel = {
    config = routeros_capsman_channel.channel1.name
  }
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the interface.
### Optional
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `channel` (Map of String) Channel inline settings.
- `comment` (String)
- `configuration` (Map of String) Configuration inline settings.
- `datapath` (Map of String) Datapath inline settings.
- `disabled` (Boolean)
- `mac_address` (String) MAC address (BSSID) to use for the interface.
- `master_interface` (String) The corresponding master interface of the virtual one.
- `radio_mac` (String) The MAC address of the associated radio.
- `radio_name` (String) Name of the associated radio.
- `rates` (Map of String) Rates inline settings.
- `security` (Map of String) Security inline settings.
### Read-Only
- `bound` (Boolean) A flag whether the interface is currently available for the CAPsMAN.
- `id` (String) The ID of this resource.
- `inactive` (Boolean) A flag whether the interface is currently inactive.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `master` (Boolean) A flag whether the interface is not a virtual one.
- `running` (Boolean) A flag whether the interface has established a link to another device.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/interface get [print show-ids]]
terraform import routeros_capsman_interface.cap1 '*1'
```
================================================

File: capsman_manager.md
================================================
# routeros_capsman_manager (Resource)
## Example Usage
```terraform
resource "routeros_capsman_manager" "test_manager" {
  enabled        = true
  upgrade_policy = "require-same-version"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `ca_certificate` (String) Device CA certificate.
- `certificate` (String) Device certificate.
- `enabled` (Boolean) Disable or enable CAPsMAN functionality.
- `package_path` (String) Folder location for the RouterOS packages. For example, use '/upgrade' to specify the upgrade folder from the files section. If empty string is set, CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded.
- `require_peer_certificate` (Boolean) Require all connecting CAPs to have a valid certificate.
- `upgrade_policy` (String) Upgrade policy options.
### Read-Only
- `generated_ca_certificate` (String) Generated CA certificate.
- `generated_certificate` (String) Generated CAPsMAN certificate.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_capsman_manager.test_manager .
```
================================================

File: capsman_manager_interface.md
================================================
# routeros_capsman_manager_interface (Resource)
## Example Usage
```terraform
resource "routeros_capsman_manager_interface" "test_manager_interface" {
  interface = "ether1"
  forbid    = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `forbid` (Boolean) Disable interface listening.
### Read-Only
- `default` (Boolean)
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is ->  :put [/caps-man/manager/interface get [print show-ids]]
terraform import routeros_capsman_manager_interface.test_manager_interface "*6"
```
================================================

File: capsman_provisioning.md
================================================
# routeros_capsman_provisioning (Resource)
## Example Usage
```terraform
resource "routeros_capsman_configuration" "test_configuration" {
  name = "cfg1"
}
resource "routeros_capsman_provisioning" "test_provisioning" {
  master_configuration = "cfg1"
  action               = "create-disabled"
  name_prefix          = "cap-"
  depends_on = [
    routeros_capsman_configuration.test_configuration,
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `master_configuration` (String) If action specifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created
### Optional
- `action` (String) Provisioning action.
- `comment` (String)
- `common_name_regexp` (String) Regular expression to match radios by common name. Each CAP's common name identifier can be found under "/caps-man radio" as value "REMOTE-CAP-NAME"
- `disabled` (Boolean)
- `hw_supported_modes` (String) Match radios by supported wireless modes.
- `identity_regexp` (String) Regular expression to match radios by router identity.
- `ip_address_ranges` (String) Match CAPs with IPs within configured address range.
- `name_format` (String) Specify the syntax of the CAP interface name creation.
- `name_prefix` (String) Name prefix which can be used in the name-format for creating the CAP interface names.
- `radio_mac` (String) MAC address of radio to be matched, empty MAC (00:00:00:00:00:00) means match all MAC addresses.
- `slave_configurations` (String) If action specifies to create interfaces, then a new slave interface for each configuration profile in this list is created.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is ->  :put [/caps-man/provisioning get [print show-ids]]
terraform import routeros_capsman_provisioning.test_provisioning "*B"
```
================================================

File: capsman_rates.md
================================================
# routeros_capsman_rates (Resource)
## Example Usage
```terraform
resource "routeros_capsman_rates" "test_rates" {
  name              = "test_rates"
  comment           = "test_rates"
  basic             = ["1Mbps", "5.5Mbps", "6Mbps", "18Mbps", "36Mbps", "54Mbps"]
  ht_basic_mcs      = ["mcs-0", "mcs-7", "mcs-11", "mcs-14", "mcs-16", "mcs-21"]
  ht_supported_mcs  = ["mcs-3", "mcs-8", "mcs-10", "mcs-13", "mcs-17", "mcs-18"]
  supported         = ["2Mbps", "11Mbps", "9Mbps", "12Mbps", "24Mbps", "48Mbps"]
  vht_basic_mcs     = "none"
  vht_supported_mcs = "mcs0-9,mcs0-7"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `basic` (Set of String) List of basic rates. Client will connect to AP only if it supports all basic rates announced by the AP. AP will establish WDS link only if it supports all basic rates of the other AP.
- `comment` (String)
- `ht_basic_mcs` (Set of String) Modulation and Coding Schemes that every connecting client must support. Refer to 802.11n for MCS specification.
- `ht_supported_mcs` (Set of String) Modulation and Coding Schemes that this device advertises as supported. Refer to 802.11n for MCS specification.
- `supported` (Set of String) List of supported rates. Two devices will communicate only using rates that are supported by both devices.
- `vht_basic_mcs` (String) Modulation and Coding Schemes that every connecting client must support. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream none - will not use selected Spatial Stream MCS 0-7 - client must support MCS-0 to MCS-7 MCS 0-8 - client must support MCS-0 to MCS-8 MCS 0-9 - client must support MCS-0 to MCS-9
- `vht_supported_mcs` (String) Modulation and Coding Schemes that this device advertises as supported. Refer to 802.11ac for MCS specification. You can set MCS interval for each of Spatial Stream none - will not use selected Spatial Stream MCS 0-7 - devices will advertise as supported MCS-0 to MCS-7 MCS 0-8 - devices will advertise as supported MCS-0 to MCS-8 MCS 0-9 - devices will advertise as supported MCS-0 to MCS-9
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/rates get [print show-ids]]
terraform import routeros_capsman_rates.test_rates "*1"
```
================================================

File: capsman_security.md
================================================
# routeros_capsman_security (Resource)
## Example Usage
```terraform
resource "routeros_capsman_security" "test_security" {
  name                  = "test_security"
  comment               = "test_security"
  authentication_types  = ["wpa-psk", "wpa-eap", "wpa2-psk"]
  disable_pmkid         = true
  eap_methods           = "eap-tls,passthrough"
  eap_radius_accounting = true
  encryption            = ["tkip", "aes-ccm"]
  group_encryption      = "aes-ccm"
  group_key_update      = "1h"
  passphrase            = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDE"
  tls_certificate       = "none"
  tls_mode              = "verify-certificate"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `authentication_types` (Set of String) Specify the type of Authentication from wpa-psk, wpa2-psk, wpa-eap or wpa2-eap.
- `comment` (String)
- `disable_pmkid` (Boolean) Whether to include PMKID into the EAPOL frame sent out by the Access Point. Disabling PMKID can cause compatibility issues with devices that use the PMKID to connect to an Access Point.
- `eap_methods` (String) eap-tls - Use built-in EAP TLS authentication; passthrough - Access point will relay authentication process to the RADIUS server.
- `eap_radius_accounting` (Boolean) Specifies if RADIUS traffic accounting should be used if RADIUS authentication gets done for this client
- `encryption` (Set of String) Set type of unicast encryption algorithm used.
- `group_encryption` (String) Access Point advertises one of these ciphers, multiple values can be selected. Access Point uses it to encrypt all broadcast and multicast frames. Client attempts connection only to Access Points that use one of the specified group ciphers.
- `group_key_update` (String) Controls how often Access Point updates the group key. This key is used to encrypt all broadcast and multicast frames. property only has effect for Access Points. (30s..1h)
- `passphrase` (String, Sensitive) WPA or WPA2 pre-shared key.
- `tls_certificate` (String) Access Point always needs a certificate when security.tls-mode is set to value other than no-certificates.
- `tls_mode` (String) This property has effect only when security.eap-methods contains eap-tls.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/security get [print show-ids]]
terraform import routeros_capsman_security.test_security "*1"
```
================================================

File: certificate_scep_server.md
================================================
# routeros_certificate_scep_server (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_system_certificate_scep_server](system_certificate_scep_server.md)
================================================

File: container.md
================================================
# routeros_container (Resource)
## Example Usage
```terraform
resource "routeros_container" "busybox" {
  remote_image  = "library/busybox:1.35.0"
  cmd           = "/bin/httpd -f -p 8080"
  interface     = routeros_interface_veth.busybox.name
  logging       = true
  root_dir      = "/usb1-part1/containers/busybox/root"
  start_on_boot = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) veth interface to be used with the container
### Optional
- `cmd` (String) The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.
- `comment` (String)
- `dns` (String) Set custom DNS servers
- `domain_name` (String) Container NIS domain name
- `entrypoint` (String) An ENTRYPOINT allows to specify executable to run when starting container. Example: /bin/sh
- `envlist` (String) list of environmental variables (configured under /container envs ) to be used with container
- `file` (String) container *tar.gz tarball if the container is imported from a file
- `hostname` (String) Container host name
- `logging` (Boolean) if set to yes, all container-generated output will be shown in the RouterOS log
- `mounts` (Set of String) Mounts from /container/mounts/ sub-menu to be used with this container
- `remote_image` (String) The container image name to be installed if an external registry is used (configured under /container/config set registry-url=...)
- `root_dir` (String) Used to save container store outside main memory
- `start_on_boot` (Boolean) Start the container on boot
- `stop_signal` (String) Signal to stop the container.
- `timeouts` (Block, Optional) (see [below for nested schema](#nestedblock--timeouts))
- `user` (String) Sets the username used
- `workdir` (String) The working directory for cmd entrypoint
### Read-Only
- `arch` (String) The architecture of the container image
- `id` (String) The ID of this resource.
- `name` (String) Assign a name to the container
- `os` (String) The OS of the container image
- `status` (String) The status of the container
- `tag` (String) The tag of the container image
<a id="nestedblock--timeouts"></a>
### Nested Schema for `timeouts`
Optional:
- `create` (String)
- `delete` (String)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container get [print show-ids]]
terraform import routeros_container.busybox "*1"
```
================================================

File: container_config.md
================================================
# routeros_container_config (Resource)
## Example Usage
```terraform
resource "routeros_container_config" "config" {
  registry_url = "https://registry-1.docker.io"
  ram_high     = "0"
  tmpdir       = "/usb1-part1/containers/tmp"
  layer_dir    = "/usb1-part1/containers/layers"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `layer_dir` (String) Container layers directory.
- `password` (String, Sensitive) Specifies the password for authentication (starting from ROS 7.8)
- `ram_high` (String) RAM usage limit. (0 for unlimited)
- `registry_url` (String) External registry url from where the container will be downloaded.
- `tmpdir` (String) Container extraction directory.
- `username` (String) Specifies the username for authentication (starting from ROS 7.8)
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_container_config.config .
```
================================================

File: container_envs.md
================================================
# routeros_container_envs (Resource)
## Example Usage
```terraform
resource "routeros_container_envs" "test_envs" {
  name  = "test_envs"
  key   = "TZ"
  value = "UTC"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `key` (String) Key of the environment variable.
- `name` (String) Name of the environment variables list.
- `value` (String) Value of the environment variable.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container/envs get [print show-ids]]
terraform import routeros_container_envs.test_envs "*1"
```
================================================

File: container_mounts.md
================================================
# routeros_container_mounts (Resource)
## Example Usage
```terraform
resource "routeros_container_mounts" "caddyfile" {
  name = "Caddyfile"
  src  = "/usb1-part1/containers/caddy/Caddyfile"
  dst  = "/etc/caddy/Caddyfile"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `dst` (String) Specifies destination path of the mount, which points to defined location in container
- `name` (String) Name of the mount.
- `src` (String) Specifies source path of the mount, which points to a RouterOS location
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container/mounts get [print show-ids]]
terraform import routeros_container_mounts.caddyfile "*1"
```
================================================

File: dhcp_client.md
================================================
# routeros_dhcp_client (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dhcp_client](ip_dhcp_client.md)
================================================

File: dhcp_client_option.md
================================================
# routeros_dhcp_client_option (Resource)
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `code` (Number) The dhcp-client option code.
- `name` (String) The name that will be used in dhcp-client.
### Optional
- `raw_value` (String) raw_value is computed from value.
- `value` (String) The dhcp-client option
### Read-Only
- `id` (String) The ID of this resource.
================================================

File: dhcp_server.md
================================================
# routeros_dhcp_server (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dhcp_server](ip_dhcp_server.md)
================================================

File: dhcp_server_lease.md
================================================
# routeros_dhcp_server_lease (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dhcp_server_lease](ip_dhcp_server_lease.md)
================================================

File: dhcp_server_network.md
================================================
# routeros_dhcp_server_network (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dhcp_server_network](ip_dhcp_server_network.md)
================================================

File: dns.md
================================================
# routeros_dns (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dns](ip_dns.md)
================================================

File: dns_record.md
================================================
# routeros_dns_record (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dns_record](ip_dns_record.md)
================================================

File: file.md
================================================
# routeros_file (Resource)
## Example Usage
```terraform
resource "routeros_file" "test" {
  name     = "test"
  contents = "This is a test"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the file
### Optional
- `contents` (String) The actual content of the file
### Read-Only
- `creation_time` (String) A time when the file was created
- `id` (String) The ID of this resource.
- `package_architecture` (String) Architecture that package is built for. Applies only to RouterOS ".npk" files
- `package_built_time` (String) A time when the package was built. Applies only to RouterOS ".npk" files
- `package_name` (String) Name of the installable package. Applies only to RouterOS ".npk" files
- `package_version` (String) A version of the installable package. Applies only to RouterOS ".npk" files
- `size` (Number) File size in bytes
- `type` (String) Type of the file. For folders, the file type is the directory
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/file get [print show-ids]]
terraform import routeros_file.test "*1"
```
================================================

File: firewall_addr_list.md
================================================
# routeros_firewall_addr_list (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_firewall_addr_list](ip_firewall_addr_list.md)
================================================

File: firewall_filter.md
================================================
# routeros_firewall_filter (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_firewall_filter](ip_firewall_filter.md)
================================================

File: firewall_mangle.md
================================================
# routeros_firewall_mangle (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_firewall_mangle](ip_firewall_mangle.md)
================================================

File: firewall_nat.md
================================================
# routeros_firewall_nat (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_firewall_nat](ip_firewall_nat.md)
================================================

File: gre.md
================================================
# routeros_gre (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_gre](interface_gre.md)
================================================

File: identity.md
================================================
# routeros_identity (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_system_identity](system_identity.md)
================================================

File: interface_bonding.md
================================================
# routeros_interface_bonding (Resource)
## Example Usage
```terraform
resource "routeros_interface_bonding" "test" {
  name   = "bonding-test"
  slaves = ["ether3", "ether4"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the bonding interface.
- `slaves` (Set of String) At least two ethernet-like interfaces separated by a comma, which will be used for bonding
### Optional
- `arp` (String) Address Resolution Protocol for the interface. disabled - the interface will not use ARP enabled - the interface will use ARP proxy-arp - the interface will use the ARP proxy feature reply-only -the interface will only reply to requests originated from matching IPaddress/MAC address combinations which are entered as static entries inthe '/ip arp' table. No dynamic entries will be automatically stored inthe '/ip arp' table. Therefore for communications to be successful, avalid static entry must already exist.
- `arp_interval` (String) Time in milliseconds defines how often to monitor ARP requests.
- `arp_ip_targets` (String) IP target address which will be monitored if link-monitoring is set to arp. You can specify multiple IP addresses, separated by a comma.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `comment` (String)
- `disabled` (Boolean)
- `down_delay` (String) If a link failure has been detected, the bonding interface is disabled for a down-delay time. The value should be a multiple of mii-interval, otherwise, it will be rounded down to the nearest value. This property only has an effect when link-monitoring is set to mii.
- `forced_mac_address` (String) Bydefault, the bonding interface will use the MAC address of the firstselected slave interface. This property allows to configure static MACaddress for the bond interface (all zeros, broadcast or multicastaddresses will not apply). RouterOS will automatically change the MACaddress for slave interfaces and it will be visible in /interface ethernet configuration export.
- `lacp_rate` (String) LinkAggregation Control Protocol rate specifies how often to exchange withLACPDUs between bonding peers. Used to determine whether a link is up orother changes have occurred in the network. LACP tries to adapt tothese changes providing failover.
- `lacp_user_key` (Number) Specifiesthe upper 10 bits of the port key. The lower 6 bits are automaticallyassigned based on individual port link speed and duplex. The setting isavailable only since RouterOS v7.3.
- `link_monitoring` (String) Method to use for monitoring the link (whether it is up or down) arp - uses Address Resolution Protocol to determine whether the remote interface is reachable mii - uses Media Independent Interface to determine link status. Link status determination relies on the device driver. none - no method for link monitoring is used. Note: some bonding modes require specific link monitoring to work properly.
- `mii_interval` (String) How often to monitor the link for failures (the parameter used only if link-monitoring is mii)
- `min_links` (Number) How many active slave links needed for bonding to become active.
- `mlag_id` (Number) ChangesMLAG ID for bonding interface. The same MLAG ID should be used on bothpeer devices to successfully create a single MLAG. See more details on MLAG .
- `mode` (String) Specifies one of the bonding policies:
  * 802.3ad -IEEE 802.3ad dynamic link aggregation. In this mode, the interfaces areaggregated in a group where each slave shares the same speed. Itprovides fault tolerance and load balancing. Slave selection foroutgoing traffic is done according to the transmit-hash-policy
  * active-backup - provides link backup. Only one slave can be active at a time. Another slave only becomes active, if the first one fails.
  * balance-alb - adaptive load balancing. The same as balance-tlb but received traffic is also balanced. The device driver should have support for changing it's MAC address.
  * balance-rr -round-robin load balancing. Slaves in a bonding interface will transmitand receive data in sequential order. It provides load balancing andfault tolerance.
  * balance-tlb -Outgoing traffic is distributed according to the current load on eachslave. Incoming traffic is not balanced and is received by the currentslave. If receiving slave fails, then another slave takes the MACaddress of the failed slave.
  * balance-xor - Transmit based on the selected transmit-hash-policy. This mode provides load balancing and fault tolerance.
  * broadcast -Broadcasts the same data on all interfaces at once. This provides faulttolerance but slows down traffic throughput on some slow machines.
- `mtu` (Number) MaximumTransmit Unit in bytes. Must be smaller or equal to the smallest L2MTUvalue of a bonding slave. L2MTU of a bonding interface is determined bythe lowest L2MTU value among its slave interfaces.
- `primary` (String) Controlsthe primary interface between active slave ports, works only foractive-backup, balance-tlb and balance-alb modes. For active-backupmode, it controls which running interface is supposed to send andreceive the traffic. For balance-tlb mode, it controls which runninginterface is supposed to receive all the traffic, but for balance-albmode, it controls which interface is supposed to receive the unbalanced  traffic (the non-IPv4 traffic). When none of the interfaces are selectedas primary, device will automatically select the interface that isconfigured as the first one.
- `transmit_hash_policy` (String) Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes:
  * layer-2 -Uses XOR of hardware MAC addresses to generate the hash. This algorithm  will place all traffic to a particular network peer on the same slave.This algorithm is 802.3ad compliant.
  * layer-2-and-3 -This policy uses a combination of layer2 and layer3 protocolinformation to generate the hash. Uses XOR of hardware MAC addresses andIP addresses to generate the hash. This algorithm will place alltraffic to a particular network peer on the same slave. For non-IPtraffic, the formula is the same as for the layer2 transmit hash policy.This policy is intended to provide a more balanced distribution oftraffic than layer2 alone, especially in environments where a layer3gateway device is required to reach most destinations. This algorithm is802.3ad compliant.
  * layer-3-and-4 - This policyuses upper layer protocol information, when available, to generate thehash. This allows for traffic to a particular network peer to spanmultiple slaves, although a single connection will not span multipleslaves. For fragmented TCP or UDP packets and all other IP protocoltraffic, the source and destination port information is omitted. Fornon-IP traffic, the formula is the same as for the layer2 transmit hashpolicy. This algorithm is not fully 802.3ad compliant.
- `up_delay` (String) If a link has been brought up, the bonding interface is disabled for up-delay time and after this time it is enabled. The value should be a multiple of mii-interval , otherwise, it will be rounded down to the nearest value. This property only has an effect when link-monitoring is set to mii.
### Read-Only
- `id` (String) The ID of this resource.
- `mac_address` (String) Current mac address.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bonding get [print show-ids]]
terraform import routeros_interface_bonding.test "*0"
```
================================================

File: interface_bridge.md
================================================
# routeros_interface_bridge (Resource)
## Example Usage
```terraform
resource "routeros_interface_bridge" "bridge" {
  name           = "bridge"
  vlan_filtering = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `add_dhcp_option82` (Boolean) Whether to add DHCP Option-82 information (Agent Remote ID and Agent Circuit ID) to DHCP packets. Can be used together with Option-82 capable DHCP server to assign IP addresses and implement policies. This property only has effect when dhcp-snooping is set to yes.
- `admin_mac` (String) Static MAC address of the bridge. This property only has effect when auto-mac is set to no.
- `ageing_time` (String) How long a host's information will be kept in the bridge database.
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `auto_mac` (Boolean) Automatically select one MAC address of bridge ports as a bridge MAC address, bridge MAC will be chosen from the first added bridge port. After a device reboot, the bridge MAC can change depending on the port-number.
- `comment` (String)
- `dhcp_snooping` (Boolean)
- `disabled` (Boolean)
- `ether_type` (String) This property only has effect when vlan-filtering is set to yes.
- `fast_forward` (Boolean)
- `forward_delay` (String) Time which is spent during the initialization phase of the bridge interface (i.e., after router startup or enabling the interface) in listening/learning state before the bridge will start functioning normally.
- `frame_types` (String) Specifies allowed frame types on a bridge port. This property only has effect when vlan-filtering is set to yes.
- `igmp_snooping` (Boolean) Enables multicast group and port learning to prevent multicast traffic from flooding all interfaces in a bridge.
- `igmp_version` (Number) Selects the IGMP version in which IGMP general membership queries will be generated. This property only has effect when igmp-snooping is set to yes.
- `ingress_filtering` (Boolean) Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to yes.
- `last_member_interval` (String) If a port has fast-leave set to no and a bridge port receives a IGMP Leave message, then a IGMP Snooping enabled bridge will send a IGMP query to make sure that no devices has subscribed to a certain multicast stream on a bridge port.
- `last_member_query_count` (Number) How many times should last-member-interval pass until a IGMP Snooping bridge will stop forwarding a certain multicast stream. This property only has effect when igmp-snooping is set to yes.
- `max_hops` (Number) Bridge count which BPDU can pass in a MSTP enabled network in the same region before BPDU is being ignored. This property only has effect when protocol-mode is set to mstp.
- `max_message_age` (String) Changes the Max Age value in BPDU packets, which is transmitted by the root bridge. This property only has effect when protocol-mode is set to stp or rstp. Value: 6s..40s
- `membership_interval` (String) Amount of time after an entry in the Multicast Database (MDB) is removed if a IGMP membership report is not received on a certain port. This property only has effect when igmp-snooping is set to yes.
- `mld_version` (Number) Selects the MLD version. Version 2 adds support for source-specific multicast. This property only has effect when RouterOS IPv6 package is enabled and igmp-snooping is set to yes.
- `mtu` (String) The default bridge MTU value without any bridge ports added is 1500. The MTU value can be set manually, but it cannot exceed the bridge L2MTU or the lowest bridge port L2MTU. If a new bridge port is added with L2MTU which is smaller than the actual-mtu of the bridge (set by the mtu property), then manually set value will be ignored and the bridge will act as if mtu=auto is set.
- `multicast_querier` (Boolean) Multicast querier generates IGMP general membership queries to which all IGMP capable devices respond with an IGMP membership report, usually a PIM (multicast) router or IGMP proxy generates these queries. This property only has an effect when igmp-snooping is set to yes. Additionally, the igmp-snooping should be disabled/enabled after changing multicast-querier property.
- `multicast_router` (String) A multicast router port is a port where a multicast router or querier is connected. On this port, unregistered multicast streams and IGMP/MLD membership reports will be sent. This setting changes the state of the multicast router for a bridge interface itself. This property can be used to send IGMP/MLD membership reports and multicast traffic to the bridge interface for further multicast routing or proxying. This property only has an effect when igmp-snooping is set to yes.
- `mvrp` (Boolean) Enables MVRP for bridge (available since RouterOS 7.15). It ensures that the MAC address 01:80:C2:00:00:21 is trapped and not forwarded, the vlan-filtering must be enabled.
- `port_cost_mode` (String) An option that changes the port path cost and internal path cost mode for bridged ports, utilizing automatic values based on interface speed.
- `priority` (String) Bridge priority, used by STP to determine root bridge, used by MSTP to determine CIST and IST regional root bridge. This property has no effect when protocol-mode is set to none.
- `protocol_mode` (String) Select Spanning tree protocol (STP) or Rapid spanning tree protocol (RSTP) to ensure a loop-free topology for any bridged LAN.
- `pvid` (Number) Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. It applies e.g. to frames sent from bridge IP and destined to a bridge port. This property only has effect when vlan-filtering is set to yes.
- `querier_interval` (String) Used to change the interval how often a bridge checks if it is the active multicast querier. This property only has effect when igmp-snooping and multicast-querier is set to yes.
- `query_interval` (String) Used to change the interval how often IGMP general membership queries are sent out. This property only has effect when igmp-snooping and multicast-querier is set to yes.
- `query_response_interval` (String) Interval in which a IGMP capable device must reply to a IGMP query with a IGMP membership report. This property only has effect when igmp-snooping and multicast-querier is set to yes.
- `region_name` (String) MSTP region name. This property only has effect when protocol-mode is set to mstp.
- `region_revision` (Number) MSTP configuration revision number. This property only has effect when protocol-mode is set to mstp.
- `startup_query_count` (Number) Specifies how many times must startup-query-interval pass until the bridge starts sending out IGMP general membership queries periodically. This property only has effect when igmp-snooping and multicast-querier is set to yes.
- `startup_query_interval` (String) Used to change the amount of time after a bridge starts sending out IGMP general membership queries after the bridge is enabled. This property only has effect when igmp-snooping and multicast-querier is set to yes.
- `transmit_hold_count` (Number) The Transmit Hold Count used by the Port Transmit state machine to limit transmission rate.
- `vlan_filtering` (Boolean) Globally enables or disables VLAN functionality for bridge.
### Read-Only
- `actual_mtu` (Number)
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `mac_address` (String) Current mac address.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge get [print show-ids]]
terraform import routeros_interface_bridge.bridge "*1"
```
================================================

File: interface_bridge_port.md
================================================
# routeros_interface_bridge_port (Resource)
## Example Usage
```terraform
resource "routeros_interface_bridge_port" "bridge_port" {
  bridge    = "bridge"
  interface = "ether5"
  pvid      = "50"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `bridge` (String)
- `interface` (String) Name of the interface.
### Optional
- `auto_isolate` (Boolean) When enabled, prevents a port moving from discarding into forwarding state if no BPDUs are received from the neighboring bridge. The port will change into a forwarding state only when a BPDU is received. This property only has an effect when protocol-mode is set to rstp or mstp and edge is set to no.
- `bpdu_guard` (Boolean) This property has no effect when protocol-mode is set to none.
- `broadcast_flood` (Boolean) When enabled, bridge floods broadcast traffic to all bridge egress ports. When disabled, drops broadcast traffic on egress ports.
- `comment` (String)
- `disabled` (Boolean)
- `edge` (String) Set port as edge port or non-edge port, or enable edge discovery. Edge ports are connected to a LAN that has no other bridges attached.
- `fast_leave` (Boolean) Enables IGMP Fast leave feature on the port.
- `frame_types` (String) Specifies allowed ingress frame types on a bridge port. This property only has effect when vlan-filtering is set to yes.
- `horizon` (String) Use split horizon bridging to prevent bridging loops. Set the same value for group of ports, to prevent them from sending data to ports with the same horizon value. Split horizon is a software feature that disables hardware offloading. This value is integer '0'..'429496729' or 'none'.
- `hw` (Boolean) Enable or disable Hardware Offloading of the interface.
- `ingress_filtering` (Boolean) Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with frame-types to specify if the ingress traffic should be tagged or untagged. This property only has effect when vlan-filtering is set to yes.
- `internal_path_cost` (Number) Path cost to the interface for MSTI0 inside a region. This property only has effect when protocol-mode is set to mstp.
- `learn` (String) Changes MAC learning behaviour on a bridge port
- `multicast_router` (String) Changes the state of a bridge port whether IGMP membership reports are going to be forwarded to this port.
- `mvrp_applicant_state` (String) MVRP applicant options (available since RouterOS 7.15): - non-participant - port does not send any MRP messages; - normal-participant - port participates normally in MRP exchanges.
- `mvrp_registrar_state` (String) MVRP registrar options (available since RouterOS 7.15): - fixed - port ignores all MRP messages, and remains Registered (IN) in all configured vlans. - normal - port receives MRP messages and handles them according to the standard.
- `path_cost` (String) Path cost to the interface, used by STP to determine the "best" path, used by MSTP todetermine "best" path between regions. This property has no effect when protocol-mode is set to none.
- `point_to_point` (String) Specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. This property has no effect when protocol-mode is set to none.
- `priority` (String) The priority of the interface, used by STP to determine the root port, used by MSTP to determine root port between regions.
- `pvid` (Number) ort VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has effect when vlan-filtering is set to yes.
- `restricted_role` (Boolean) Enable the restricted role on a port, used by STP to forbid a port becoming a root port. This property only has effect when protocol-mode is set to mstp.
- `restricted_tcn` (Boolean) Disable topology change notification (TCN) sending on a port, used by STP to forbid network topology changes to propagate. This property only has effect when protocol-mode is set to mstp.
- `tag_stacking` (Boolean) Forces all packets to be treated as untagged packets. Packets on ingress port will be tagged with another VLAN tag regardless if a VLAN tag already exists, packets will be tagged with a VLAN ID that matches the pvid value and will use EtherType that is specified in ether-type. This property only has effect when vlan-filtering is set to yes.
- `trusted` (Boolean) When enabled, it allows to forward DHCP packets towards DHCP server through this port. Mainly used to limit unauthorized servers to provide malicious information for users. This property only has effect when dhcp-snooping is set to yes.
- `unknown_multicast_flood` (Boolean) When enabled, bridge floods unknown multicast traffic to all bridge egress ports.
- `unknown_unicast_flood` (Boolean) When enabled, bridge floods unknown unicast traffic to all bridge egress ports.
### Read-Only
- `designated_bridge` (String) Root bridge ID (bridge priority and the bridge MAC address).
- `designated_cost` (String) Designated cost.
- `designated_port_number` (Number) Designated port number.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `edge_port` (Boolean) Whether port is an edge port or not.
- `edge_port_discovery` (Boolean) Whether port is set to automatically detect edge ports.
- `external_fdb_status` (Boolean) Whether registration table is used instead of forwarding data base.
- `forwarding` (Boolean) Shows if the port is not blocked by (R/M)STP.
- `hw_offload` (Boolean) Hardware offloading state.
- `hw_offload_group` (String) Switch chip used by the port.
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
- `learning` (Boolean) Shows whether the port is capable of learning MAC addresses.
- `nextid` (String)
- `point_to_point_port` (Boolean) Whether the port is connected to a bridge port using full-duplex (true) or half-duplex (false).
- `role` (String) (R/M)STP algorithm assigned role of the port
- `root_path_cost` (Number) The total cost of the path to the root-bridge.
- `sending_rstp` (String) Whether the port is sending RSTP or MSTP BPDU types. A port will transit to STP type when RSTP/MSTP enabled port receives a STP BPDU
- `status` (String) Port status ('in-bridge' - port is enabled).
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge/port get [print show-ids]]
terraform import routeros_interface_bridge_port.bridge_port "*0"
```
================================================

File: interface_bridge_settings.md
================================================
# routeros_interface_bridge_settings (Resource)
## Example Usage
```terraform
resource "routeros_interface_bridge_settings" "settings" {
  use_ip_firewall = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `allow_fast_path` (Boolean) Whether to enable a bridge FastPath globally.
- `use_ip_firewall` (Boolean) Force bridged traffic to also be processed by prerouting, forward and postrouting sections of IP routing ( Packet Flow). This does not apply to routed traffic. This property is required in case you want to assign Simple Queues or global Queue Tree to traffic in a bridge. Property use-ip-firewall-for-vlan is required in case bridge vlan-filtering is used.
- `use_ip_firewall_for_pppoe` (Boolean) Send bridged un-encrypted PPPoE traffic to also be processed by IP/Firewall. This property only has effect when use-ip-firewall is set to yes. This property is required in case you want to assign Simple Queues or global Queue Tree to PPPoE traffic in a bridge.
- `use_ip_firewall_for_vlan` (Boolean) Send bridged VLAN traffic to also be processed by IP/Firewall. This property only has effect when use-ip-firewall is set to yes. This property is required in case you want to assign Simple Queues or global Queue Tree to VLAN traffic in a bridge.
### Read-Only
- `bridge_fast_forward_bytes` (Number) Shows byte count forwarded by Bridge Fast Forward.
- `bridge_fast_forward_packets` (Number) Shows packet count forwarded by Bridge Fast Forward.
- `bridge_fast_path_active` (Boolean) Shows whether a bridge FastPath is active globally, FastPatch status per bridge interface is not displayed.
- `bridge_fast_path_bytes` (Number) Shows byte count forwarded by Bridge Fast Path.
- `bridge_fast_path_packets` (Number) Shows packet count forwarded by Bridge FastPath.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_interface_bridge_settings.settings .
```
================================================

File: interface_bridge_vlan.md
================================================
# routeros_interface_bridge_vlan (Resource)
## Example Usage
```terraform
resource "routeros_interface_bridge_vlan" "bridge_vlan" {
  vlan_ids = ["50"]
  bridge   = "bridge"
  tagged = [
    "bridge",
    "ether1"
  ]
  untagged = [
    "ether5"
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `bridge` (String) The bridge interface which the respective VLAN entry is intended for.
- `vlan_ids` (Set of String) The list of VLAN IDs for certain port configuration. This setting accepts VLAN ID range as well as comma separated values. E.g. vlan-ids=100-115,120,122,128-130.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `mvrp_forbidden` (List of String) Ports that ignore all MRP messages and remains Not Registered (MT), as well as disables applicant from declaring specific VLAN ID (available since RouterOS 7.15).
- `tagged` (Set of String) Interface list with a VLAN tag adding action in egress. This setting accepts comma separated values. E.g. tagged=ether1,ether2.
- `untagged` (Set of String) Interface list with a VLAN tag removing action in egress. This setting accepts comma separated values. E.g. untagged=ether3,ether4
### Read-Only
- `current_tagged` (List of String)
- `current_untagged` (List of String)
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge/vlan get [print show-ids]]
terraform import routeros_interface_bridge_vlan.bridge_vlan "*0"
```
================================================

File: interface_dot1x_client.md
================================================
# routeros_interface_dot1x_client (Resource)
## Example Usage
```terraform
resource "routeros_interface_dot1x_client" "ether2" {
  eap_methods = ["eap-peap", "eap-mschapv2"]
  identity    = "router"
  interface   = "ether2"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `eap_methods` (Set of String) A set of EAP methods used for authentication: `eap-tls`, `eap-ttls`, `eap-peap`, `eap-mschapv2`.
- `identity` (String) The supplicant identity that is used for EAP authentication.
- `interface` (String) Name of the interface.
### Optional
- `anon_identity` (String) Identity for outer layer EAP authentication. Used only with `eap-ttls` and `eap-peap` methods. If not set, the value from the identity parameter will be used for outer layer EAP authentication.
- `certificate` (String) Name of a certificate. Required when the `eap-tls` method is used.
- `comment` (String)
- `disabled` (Boolean)
- `password` (String, Sensitive) Cleartext password for the supplicant.
### Read-Only
- `id` (String) The ID of this resource.
- `status` (String)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/dot1x/client get [print show-ids]]
terraform import routeros_interface_dot1x_client.ether2 *1
```
================================================

File: interface_dot1x_server.md
================================================
# routeros_interface_dot1x_server (Resource)
## Example Usage
```terraform
resource "routeros_interface_dot1x_server" "ether2" {
  auth_types = ["mac-auth"]
  interface  = "ether2"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
### Optional
- `accounting` (Boolean) Whether to send RADIUS accounting requests to the authentication server.
- `auth_timeout` (String) Total time available for EAP authentication.
- `auth_types` (Set of String) Used authentication type on a server interface. Comma-separated list of `dot1x` and `mac-auth`.
- `comment` (String)
- `disabled` (Boolean)
- `guest_vlan_id` (Number) Assigned VLAN when end devices do not support dot1x authentication and no mac-auth fallback is configured.
- `interim_update` (String) Interval between scheduled RADIUS Interim-Update messages.
- `mac_auth_mode` (String) An option that allows to control User-Name and User-Password RADIUS attributes when using MAC authentication.
- `radius_mac_format` (String) An option that controls how the MAC address of the client is encoded in the User-Name and User-Password attributes when using MAC authentication.
- `reauth_timeout` (String) An option that enables server port re-authentication.
- `reject_vlan_id` (Number) Assigned VLAN when authentication failed, and a RADIUS server responded with an Access-Reject message.
- `retrans_timeout` (String) The time interval between message re-transmissions if no response is received from the supplicant.
- `server_fail_vlan_id` (Number) Assigned VLAN when RADIUS server is not responding and request timed out.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/dot1x/server get [print show-ids]]
terraform import routeros_interface_dot1x_server.ether2 *1
```
================================================

File: interface_eoip.md
================================================
# routeros_interface_eoip (Resource)
## Example Usage
```terraform
resource "routeros_interface_eoip" "eoip_tunnel1" {
  name           = "eoip-tunnel1"
  local_address  = "192.168.88.1"
  remote_address = "192.168.88.2"
  disabled       = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `allow_fast_path` (Boolean) Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `clamp_tcp_mss` (Boolean) Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
- `comment` (String)
- `disabled` (Boolean)
- `dont_fragment` (String)
- `dscp` (String) Set dscp value in GRE header to a fixed value '0..63' or 'inherit' from dscp value taken from tunnelled traffic.
- `ipsec_secret` (String, Sensitive) When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
- `keepalive` (String) Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format: KeepaliveInterval,KeepaliveRetries where KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. KeepaliveInterval is integer 0..4294967295
- `local_address` (String) Source address of the tunnel packets, local on the router.
- `loop_protect` (String)
- `loop_protect_disable_time` (String)
- `loop_protect_send_interval` (String)
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `remote_address` (String) IP address of the remote end of the tunnel.
- `tunnel_id` (Number) Unique tunnel identifier, which must match the other side of the tunnel.
### Read-Only
- `actual_mtu` (Number)
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `loop_protect_status` (String)
- `mac_address` (String) Current mac address.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/eoip get [print show-ids]]
terraform import routeros_interface_eoip.eoip_tunnel1 *B
```
================================================

File: interface_ethernet.md
================================================
# routeros_interface_ethernet (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet" "test" {
  factory_name = "sfp-sfpplus8"
  name         = "swtich-eth0"
  mtu          = 9000
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `factory_name` (String) The factory name of the identifier, serves as resource identifier. Determines which interface will be updated.
- `name` (String) Name of the ethernet interface.
### Optional
- `advertise` (String) Advertised speed and duplex modes for Ethernet interfaces over twisted pair, 
				only applies when auto-negotiation is enabled. Advertising higher speeds than 
				the actual interface supported speed will have no effect, multiple options are allowed.
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `auto_negotiation` (Boolean) When enabled, the interface "advertises" its maximum capabilities to achieve the best connection possible.
					Note1: Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly.
					Note2: Gigabit Ethernet and NBASE-T Ethernet links cannot work with auto-negotiation disabled.
- `bandwidth` (String) Sets max rx/tx bandwidth in kbps that will be handled by an interface. TX limit is supported on all Atheros switch-chip ports. 
				RX limit is supported only on Atheros8327/QCA8337 switch-chip ports.
- `cable_settings` (String) Changes the cable length setting (only applicable to NS DP83815/6 cards)
- `combo_mode` (String) When auto mode is selected, the port that was first connected will establish the link. In case this link fails, the other port will try to establish a new link. If both ports are connected at the same time (e.g. after reboot), 
				the priority will be the SFP/SFP+ port. When sfp mode is selected, the interface will only work through SFP/SFP+ cage.
				When copper mode is selected, the interface will only work through RJ45 Ethernet port.
- `comment` (String)
- `disable_running_check` (Boolean) Disable running check. If this value is set to 'no', the router automatically detects whether the NIC is connected with a device in the network or not.
			Default value is 'yes' because older NICs do not support it. (only applicable to x86)
- `disabled` (Boolean)
- `fec_mode` (String) Changes Forward Error Correction (FEC) mode for SFP28, QSFP+ and QSFP28 interfaces. Same mode should be used on both link ends, otherwise FEC mismatch could result in non-working link or even false link-ups.
- `full_duplex` (Boolean) Defines whether the transmission of data appears in two directions simultaneously, only applies when auto-negotiation is disabled.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `loop_protect` (String)
- `loop_protect_disable_time` (String)
- `loop_protect_send_interval` (String)
- `mac_address` (String) Media Access Control number of an interface.
- `mdix_enable` (Boolean) Whether the MDI/X auto cross over cable correction feature is enabled for the port (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to 'yes' on other hardware.)
- `mtu` (Number) Layer3 Maximum transmission unit
- `poe_lldp_enabled` (Boolean) An option that enables LLDP for managing devices.
- `poe_out` (String) PoE settings: (https://wiki.mikrotik.com/wiki/Manual:PoE-Out)
- `poe_priority` (Number) PoE settings: (https://wiki.mikrotik.com/wiki/Manual:PoE-Out)
- `poe_voltage` (String) An option that allows us to manually control the voltage outputs on the PoE port.
- `power_cycle_interval` (String) An options that disables PoE-Out power for 5s between the specified intervals.
- `power_cycle_ping_address` (String) An address to monitor.
- `power_cycle_ping_enabled` (Boolean) An option that enables ping watchdog of power cycles on the port if a host does not respond to ICMP or MAC-Telnet packets.
- `power_cycle_ping_timeout` (String) If the host does not respond over the specified period, the PoE-Out port is switched off for 5s.
- `rx_flow_control` (String) When set to on, the port will process received pause frames and suspend transmission if required.
					auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
- `sfp_ignore_rx_los` (Boolean) An option to ignore RX LOS (Loss of Signal) status of the SFP module.
- `sfp_rate_select` (String) Allows to control rate select pin for SFP ports. Values: high | low
- `sfp_shutdown_temperature` (Number) The temperature in Celsius at which the interface will be temporarily turned off due to too high detected SFP module temperature (introduced v6.48).The default value for SFP/SFP+/SFP28 interfaces is 95, and for QSFP+/QSFP28 interfaces 80 (introduced v7.6).
- `speed` (String) Sets interface data transmission speed which takes effect only when ```auto_negotiation``` is disabled.
- `tx_flow_control` (String) When set to on, the port will generate pause frames to the upstream device to temporarily stop the packet transmission. 
					Pause frames are only generated when some routers output interface is congested and packets cannot be transmitted anymore. 
					Auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises.
### Read-Only
- `default_name` (String) The default name for an interface.
- `id` (String) The ID of this resource.
- `loop_protect_status` (String)
- `orig_mac_address` (String) Original Media Access Control number of an interface. (read only)
- `running` (Boolean) Whether interface is running. Note that some interface does not have running check and they are always reported as "running"
- `slave` (Boolean) Whether interface is configured as a slave of another interface (for example Bonding)
- `switch` (String) ID to which switch chip interface belongs to.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet get [print show-ids]]
terraform import routeros_interface_ethernet.test "*0"
```
================================================

File: interface_ethernet_switch.md
================================================
# routeros_interface_ethernet_switch (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch" "sw0" {
  switch_id = 0 # Optional
  name      = "new switch"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the switch.
### Optional
- `cpu_flow_control` (Boolean) All switch chips have a special port that is called switchX-cpu, this is the CPU port for a switch chip, it is meant to forward traffic from a switch chip to the CPU, such a port is required for management traffic and for routing features. By default the switch chip ensures that this special CPU port is not congested and sends out Pause Frames when link capacity is exceeded to make sure the port is not oversaturated, this feature is called CPU Flow Control. Without this feature packets that might be crucial for routing or management purposes might get dropped.
- `l3_hw_offloading` (Boolean) Layer 3 Hardware Offloading (L3HW, otherwise known as IP switching or HW routing) allows to offload some router features onto the switch chip. This allows reaching wire speeds when routing packets, which simply would not be possible with the CPU.
- `mirror_egress_target` (String) Selects a single mirroring egress target port, only available on 88E6393X, 88E6191X and 88E6190 switch chips. Mirrored packets from `mirror-egress` (see the property in port menu) will be sent to the selected port.
- `mirror_source` (String) Selects a single mirroring source port. Ingress and egress traffic will be sent to the mirror-target port. Note that mirror-target port has to belong to the same switch (see which port belongs to which switch in /interface ethernet menu).
- `mirror_target` (String) Selects a single mirroring target port. Mirrored packets from mirror-source and mirror (see the property in rule and host table) will be sent to the selected port.
- `switch_id` (String) Switch-chip id. Default .id = *0
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `type` (String) Switch-chip type.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch get [print show-ids]]
terraform import routeros_interface_ethernet_switch.sw0 *0
```
================================================

File: interface_ethernet_switch_host.md
================================================
# routeros_interface_ethernet_switch_host (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch_host" "test" {
  switch      = "switch1"
  mac_address = "00:00:00:00:00:00"
  ports       = ["ether1"]
  mirror      = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `mac_address` (String) Host's MAC address.
- `ports` (List of String) Name of the interface, static MAC address can be mapped to more that one port, including switch CPU port.
- `switch` (String) Name of the switch to which the MAC address is going to be assigned to.
### Optional
- `copy_to_cpu` (Boolean) Whether to send a frame copy to switch CPU port from a frame with matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `drop` (Boolean) Whether to drop a frame with matching MAC source address received on a certain port (matching destination or source address for CRS3xx series switches).
- `mirror` (Boolean) Whether to send a frame copy to mirror-target port from a frame with matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `redirect_to_cpu` (Boolean) Whether to redirect a frame to switch CPU port from a frame with matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `share_vlan_learned` (Boolean) Whether the static host MAC address lookup is used with shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL). The SVL mode is used for those VLAN entries that do not support IVL or IVL is disabled (independent-learning=no).
- `vlan_id` (String) VLAN ID for the statically added MAC address entry.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/host get [print show-ids]]
terraform import routeros_interface_ethernet_switch_host.test *0
```
================================================

File: interface_ethernet_switch_port.md
================================================
# routeros_interface_ethernet_switch_port (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch_port" "test" {
  name      = "ether1"
  vlan_mode = "check"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Port name.
### Optional
- `default_vlan_id` (String) Adds a VLAN tag with the specified VLAN ID on all untagged ingress traffic on a port, should be used with ```vlan-header``` set to ```always-strip``` on a port to configure the port to be the access port. For hybrid ports ```default-vlan-id``` is used to tag untagged traffic. If two ports have the same ```default-vlan-id```, then VLAN tag is not added since the switch chip assumes that traffic is being forwarded between access ports.
- `mirror_egress` (Boolean) Whether to send egress packet copy to the `mirror-egress-target` port, only available on 88E6393X, 88E6191X and 88E6190 switch chips.
- `mirror_ingress` (Boolean) Whether to send ingress packet copy to the `mirror-ingress-target` port, only available on 88E6393X, 88E6191X and 88E6190 switch chips.
- `mirror_ingress_target` (String) Selects a single mirroring ingress target port, only available on  88E6393X, 88E6191X and 88E6190 switch chips. Mirrored packets from `mirror-ingress` will be sent to the selected port.
- `vlan_header` (String) Sets action which is performed on the port for egress traffic.
- `vlan_mode` (String) Changes the VLAN lookup mechanism against the VLAN Table for ingress traffic.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `running` (Boolean)
- `switch` (String) Name of the switch.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/port get [print show-ids]]
terraform import routeros_interface_ethernet_switch_port.test *1
```
================================================

File: interface_ethernet_switch_port_isolation.md
================================================
# routeros_interface_ethernet_switch_port_isolation (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch_port_isolation" "test" {
  name                = "ether1"
  forwarding_override = "ether1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Port name.
### Optional
- `forwarding_override` (String) Forces ingress traffic to be forwarded to a specific interface. Multiple interfaces can be specified by separating them with a comma.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `switch` (String) Name of the switch.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/port-isolation get [print show-ids]]
terraform import routeros_interface_ethernet_switch_port_isolation.test *1
```
================================================

File: interface_ethernet_switch_rule.md
================================================
# routeros_interface_ethernet_switch_rule (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch_rule" "test" {
  switch      = "switch1"
  ports       = ["ether1"]
  copy_to_cpu = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `ports` (List of String) Name of the interface on which the rule will apply on the received traffic, multiple ports are allowed.
- `switch` (String) Matching switch group on which will the rule apply.
### Optional
- `comment` (String)
- `copy_to_cpu` (Boolean) Whether to send a frame copy to switch CPU port from a frame with matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `disabled` (Boolean)
- `dscp` (Number) Matching DSCP field of the packet.
- `dst_address` (String) Matching destination IP address and mask.
- `dst_address6` (String) Matching destination IPv6 address and mask.
- `dst_mac_address` (String) Matching destination MAC address and mask.
- `dst_port` (Number) Matching destination protocol port number or range.
- `flow_label` (Number) Matching IPv6 flow label.
- `mac_protocol` (String) Matching particular MAC protocol specified by protocol name or number (skips VLAN tags if any).
- `mirror` (Boolean) Whether to send a frame copy to mirror-target port from a frame with matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `mirror_ports` (Set of String) Selects multiple mirroring target ports, only available on 88E6393X switch chip. Matched packets in the ACL rule will be copied and sent to selected ports.
- `new_dst_ports` (Set of String) Changes the destination port as specified, multiple ports allowed, including a switch CPU port. An empty setting will drop the packet. When the parameter is not used, the packet will be accepted.
- `new_vlan_id` (Number) Changes the VLAN ID to the specified value or adds a new VLAN tag if one was not already present (the property only applies to the Atheros8316, and 88E6393X switch chips).
- `new_vlan_priority` (Number) Changes the VLAN priority field (priority code point, the property only applies to Atheros8327, QCA8337 and Atheros8316 switch chips).
- `protocol` (String) Matching particular IP protocol specified by protocol name or number.
- `rate` (Number) Sets ingress traffic limitation (bits per second) for matched traffic, can only be applied to the first 32 rule slots (the property only applies to Atheros8327/QCA8337 switch chips).
- `redirect_to_cpu` (Boolean) Changes the destination port of a matching packet to the switch CPU.
- `src_address` (String) Matching source IP address and mask.
- `src_address6` (String) Matching source IPv6 address and mask.
- `src_mac_address` (String) Matching source MAC address and mask.
- `src_port` (Number) Matching source protocol port number or range.
- `traffic_class` (Number) Matching IPv6 traffic class.
- `vlan_header` (String) Matching VLAN header, whether the VLAN header is present or not (the property only applies to the Atheros8316, Atheros8327, QCA8337, 88E6393X switch chips).
- `vlan_id` (Number) Matching VLAN ID (the property only applies to the Atheros8316, Atheros8327, QCA8337, 88E6393X switch chips).
- `vlan_priority` (Number) Matching VLAN priority (priority code point).
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/rule get [print show-ids]]
terraform import routeros_interface_ethernet_switch_rule.test *0
```
================================================

File: interface_ethernet_switch_vlan.md
================================================
# routeros_interface_ethernet_switch_vlan (Resource)
## Example Usage
```terraform
resource "routeros_interface_ethernet_switch_vlan" "test" {
  switch               = "switch1"
  ports                = ["ether1"]
  vlan_id              = 10
  independent_learning = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `ports` (List of String) Interface member list for the respective VLAN.
- `switch` (String) Name of the switch for which the respective VLAN entry is intended for.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `independent_learning` (Boolean) Whether to use shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL).
- `vlan_id` (Number) The VLAN ID for certain switch port configurations.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/vlan get [print show-ids]]
terraform import routeros_interface_ethernet_switch_vlan.test *0
```
================================================

File: interface_gre.md
================================================
# routeros_interface_gre (Resource)
## Example Usage
```terraform
resource "routeros_interface_gre" "gre_hq" {
  name           = "gre-hq-1"
  remote_address = "10.77.3.26"
  disabled       = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `allow_fast_path` (Boolean) Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
- `clamp_tcp_mss` (Boolean) Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
- `comment` (String)
- `disabled` (Boolean)
- `dont_fragment` (String)
- `dscp` (String) Set dscp value in GRE header to a fixed value '0..63' or 'inherit' from dscp value taken from tunnelled traffic.
- `ipsec_secret` (String, Sensitive) When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
- `keepalive` (String) Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format: KeepaliveInterval,KeepaliveRetries where KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. KeepaliveInterval is integer 0..4294967295
- `local_address` (String) Source address of the tunnel packets, local on the router.
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `remote_address` (String) IP address of the remote end of the tunnel.
### Read-Only
- `actual_mtu` (Number)
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/gre get [print show-ids]]
terraform import routeros_interface_gre.gre_hq "*1"
```
================================================

File: interface_ipip.md
================================================
# routeros_interface_ipip (Resource)
## Example Usage
```terraform
resource "routeros_interface_ipip" "ipip_hq" {
  name           = "ipip-hq-1"
  remote_address = "10.77.3.26"
  disabled       = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the ipip interface.
### Optional
- `allow_fast_path` (Boolean) Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
- `clamp_tcp_mss` (Boolean) Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
- `comment` (String)
- `disabled` (Boolean)
- `dont_fragment` (String)
- `dscp` (String) Set dscp value in GRE header to a fixed value '0..63' or 'inherit' from dscp value taken from tunnelled traffic.
- `ipsec_secret` (String, Sensitive) When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
- `keepalive` (String) Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format: KeepaliveInterval,KeepaliveRetries where KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. KeepaliveInterval is integer 0..4294967295
- `local_address` (String) Source address of the tunnel packets, local on the router.
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `remote_address` (String) IP address of the remote end of the tunnel.
### Read-Only
- `actual_mtu` (Number)
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ipip get [print show-ids]]
terraform import routeros_interface_ipip.ipip_hq "*1"
```
================================================

File: interface_list.md
================================================
# routeros_interface_list (Resource)
## Example Usage
```terraform
resource "routeros_interface_list" "list" {
  name = "my-list"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `comment` (String)
- `exclude` (String)
- `include` (String)
### Read-Only
- `builtin` (Boolean)
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/list get [print show-ids]]
terraform import routeros_interface_list.list "*2000010"
```
================================================

File: interface_list_member.md
================================================
# routeros_interface_list_member (Resource)
## Example Usage
```terraform
resource "routeros_interface_list_member" "list_member" {
  interface = "ether1"
  list      = "my-list"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String)
- `list` (String)
### Optional
- `comment` (String)
- `disabled` (Boolean)
### Read-Only
- `dynamic` (Boolean)
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/list/member get [print show-ids]]
terraform import routeros_interface_list_member.list_member "*0"
```
================================================

File: interface_lte.md
================================================
# routeros_interface_lte (Resource)
## Example Usage
```terraform
resource "routeros_interface_lte" "test" {
  allow_roaming = false
  apn_profiles  = "default"
  band          = []
  default_name  = "lte1"
  disabled      = false
  mtu           = "1500"
  name          = "lte1"
  network_mode  = ["3g", "lte"]
  sms_protocol  = null
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Descriptive name of the interface.
### Optional
- `allow_roaming` (Boolean) Enable data roaming for connecting to other countries data-providers. Not all LTE modems support this feature. Some modems, that do not fully support this feature, will connect to the network but will not establish an IP data connection with allow-roaming set to no.
- `apn_profiles` (String) Which APN profile to use for this interface.
- `band` (Set of Number) LTE Frequency band used in communication [LTE Bands and bandwidths](https://en.wikipedia.org/wiki/LTE_frequency_bands#Frequency_bands_and_channel_bandwidths).
- `comment` (String)
- `disabled` (Boolean)
- `modem_init` (String) Modem init string (AT command that will be executed at modem startup).
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `network_mode` (Set of String) Select/force mode for LTE interface to operate with.
- `nr_band` (Set of Number) 5G NR Frequency band used in communication [5G NR Bands and bandwidths](https://en.wikipedia.org/wiki/5G_NR_frequency_bands).
- `operator` (Number) Used to lock the device to a specific operator full PLMN number is used for the lock consisting of MCC+MNC. [PLMN codes](https://en.wikipedia.org/wiki/Public_land_mobile_network).
- `pin` (String) SIM Card's PIN code.
- `sms_protocol` (String) SMS functionality. `mbim`: uses MBIM driver. `at`: uses AT-Commands. `auto`: selects the appropriate option depending on the modem.
- `sms_read` (Boolean)
### Read-Only
- `default_name` (String) The default name for an interface.
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ get [print show-ids]]
terraform import routeros_interface_lte.test *3
```
================================================

File: interface_lte_apn.md
================================================
# routeros_interface_lte_apn (Resource)
## Example Usage
```terraform
resource "routeros_interface_lte_apn" "test" {
  name           = "apn1"
  apn            = "internet"
  authentication = "pap"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) APN profile name
### Optional
- `add_default_route` (Boolean) Whether to add a default route to forward all traffic over the LTE interface.
- `apn` (String) Service Provider's Access Point Name.
- `authentication` (String) Allowed protocol to use for authentication.
- `comment` (String)
- `default_route_distance` (Number) Sets distance value applied to auto-created default route, if add-default-route is also selected. LTE route by default is with distance 2 to prefer wired routes over LTE.
- `ip_type` (String) Requested PDN type.
- `ipv6_interface` (String) Interface on which to advertise IPv6 prefix.
- `number` (Number) APN profile number.
- `passthrough_interface` (String) Interface to passthrough IP configuration (activates passthrough).
- `passthrough_mac` (String) If set to auto, then will learn MAC from the first packet.
- `passthrough_subnet_selection` (String) `auto` selects the smallest possible subnet to be used for the passthrough interface. `p2p` sets the passthrough interface subnet as `/32` and picks gateway address from `10.177.0.0/16` range. The gateway address stays the same until the apn configuration is changed.
- `password` (String) Password used if any of the authentication protocols are active.
- `use_network_apn` (Boolean) Parameter is available starting from RouterOS v7 and used only for MBIM modems. If set to yes, uses network provided APN.
- `use_peer_dns` (Boolean) If set to yes, uses DNS received from LTE interface.
- `user` (String) Username used if any of the authentication protocols are active.
### Read-Only
- `default` (Boolean)
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ get [print show-ids]]
terraform import routeros_interface_lte_apn.test *3
```
================================================

File: interface_macvlan.md
================================================
# routeros_interface_macvlan (Resource)
## Example Usage
```terraform
resource "routeros_interface_macvlan" "test" {
  interface = "ether1"
  name      = "macvlan1"
  disabled  = false
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `comment` (String)
- `disabled` (Boolean)
- `loop_protect` (String)
- `loop_protect_disable_time` (String)
- `loop_protect_send_interval` (String)
- `mac_address` (String) Static MAC address of the interface. A randomly generated MAC address will be assigned when not specified.
- `mode` (String) Sets MACVLAN interface mode:
	private - does not allow communication between MACVLAN instances on the same parent interface.
	bridge - allows communication between MACVLAN instances on the same parent interface.
### Read-Only
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/macvlan get [print show-ids]]
terraform import routeros_interface_macvlan.test "*0"
```
================================================

File: interface_ovpn_client.md
================================================
# routeros_interface_ovpn_client (Resource)
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `connect_to` (String) Remote address of the OVPN server.
- `name` (String) Descriptive name of the interface.
- `user` (String) User name used for authentication.
### Optional
- `add_default_route` (Boolean) Whether to add OVPN remote address as a default route.
- `auth` (String) Authentication methods that the server will accept.
- `certificate` (String) Name of the client certificate.
- `cipher` (String) Allowed ciphers.
- `comment` (String)
- `disabled` (Boolean)
- `mac_address` (String) Mac address of OVPN interface. Will be automatically generated if not specified.
- `max_mtu` (Number) Maximum Transmission Unit. Max packet size that the OVPN interface will be able to send without packet fragmentation.
- `mode` (String) Layer3 or layer2 tunnel mode (alternatively tun, tap)
- `password` (String, Sensitive) Password used for authentication.
- `port` (Number) Port to connect to.
- `profile` (String) Specifies which PPP profile configuration will be used when establishing the tunnel.
- `protocol` (String) Indicates the protocol to use when connecting with the remote endpoint.
- `route_nopull` (Boolean) Specifies whether to allow the OVPN server to add routes to the OVPN client instance routing table.
- `tls_version` (String) Specifies which TLS versions to allow.
- `use_peer_dns` (Boolean) Whether to add DNS servers provided by the OVPN server to IP/DNS configuration.
- `verify_server_certificate` (Boolean) Checks the certificates CN or SAN against the "connect-to" parameter. The IP or hostname must be present in the server's certificate.
### Read-Only
- `hw_crypto` (Boolean)
- `id` (String) The ID of this resource.
- `running` (Boolean)
================================================

File: interface_ovpn_server.md
================================================
# routeros_interface_ovpn_server (Resource)
## Example Usage
```terraform
resource "routeros_interface_ovpn_server" "user1" {
  name       = "ovpn-in1"
  user       = "user1"
  depends_on = [routeros_ovpn_server.server]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Interface name (Example: ovpn-in1).
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `user` (String) User name used for authentication.
### Read-Only
- `client_address` (String) The address of the remote side.
- `encoding` (String) Encryption characteristics.
- `id` (String) The ID of this resource.
- `mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `running` (Boolean)
- `uptime` (String) Connection uptime.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ovpn-server get [print show-ids]]
terraform import routeros_interface_ovpn_server.user1 *29
```
================================================

File: interface_pppoe_client.md
================================================
# routeros_interface_pppoe_client (Resource)
## Example Usage
```terraform
resource "routeros_interface_pppoe_client" "test" {
  interface    = "ether1"
  password     = "StrongPass"
  service_name = "pppoeservice"
  name         = "PPPoE-Out"
  disabled     = false
  user         = "MT-User"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Interface name on which client will run.
- `name` (String) Name of the PPPoE interface.
### Optional
- `ac_name` (String) Access Concentrator name, this may be left blank and the client will connect to any access concentrator on the broadcast domain.
- `add_default_route` (Boolean) Enable/Disable whether to add default route automatically.
- `allow` (Set of String) Allowed authentication methods, by default all methods are allowed.
- `comment` (String)
- `default_route_distance` (Number) sets distance value applied to auto created default route, if add-default-route is also selected.
- `dial_on_demand` (Boolean) connects to AC only when outbound traffic is generated. If selected, then route with gateway address from 10.112.112.0/24 network will be added while connection is not established.
- `disabled` (Boolean)
- `keepalive_timeout` (Number) Sets keepalive timeout in seconds.
- `max_mru` (String) Maximum Receive Unit.
- `max_mtu` (String) Maximum Transmission Unit.
- `mrru` (String) Maximum packet size (512..65535 or disabled) that can be received on the link. If a packet is bigger than tunnel MTU, it will be split into multiple packets, allowing full size IP or Ethernet packets to be sent over the tunnel.
- `password` (String, Sensitive) Password used to authenticate.
- `profile` (String) Specifies which PPP profile configuration will be used when establishing the tunnel.
- `service_name` (String) Specifies the service name set on the access concentrator, can be left blank to connect to any PPPoE server.
- `use_peer_dns` (Boolean) Enable/disable getting DNS settings from the peer.
- `user` (String) Username used for authentication.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/pppoe-client get [print show-ids]]
terraform import routeros_interface_pppoe_client.test "*0"
```
================================================

File: interface_veth.md
================================================
# routeros_interface_veth (Resource)
## Example Usage
```terraform
resource "routeros_interface_veth" "test" {
  name    = "veth-test"
  address = "192.168.120.2/24"
  gateway = "192.168.120.1"
  comment = "Virtual interface"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Interface name.
### Optional
- `address` (String) IP address.
- `comment` (String)
- `disabled` (Boolean)
- `gateway` (String) Gateway IP address.
- `gateway6` (String) Gateway IPv6 address.
### Read-Only
- `id` (String) The ID of this resource.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/veth get [print show-ids]]
terraform import routeros_interface_veth.test "*0"
```
================================================

File: interface_vlan.md
================================================
# routeros_interface_vlan (Resource)
## Example Usage
```terraform
resource "routeros_interface_vlan" "interface_vlan" {
  interface = "bridge"
  name      = "VLAN_TEST"
  vlan_id   = 50
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
- `vlan_id` (Number)
### Optional
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `comment` (String)
- `disabled` (Boolean)
- `loop_protect` (String)
- `loop_protect_disable_time` (String)
- `loop_protect_send_interval` (String)
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `mvrp` (Boolean) Specifies whether this VLAN should declare its attributes through Multiple VLAN Registration Protocol (MVRP) as an applicant (available since RouterOS 7.15). It can be used to register the VLAN with connected bridges that support MVRP. This property only has an effect when use-service-tag is disabled.
- `use_service_tag` (Boolean)
### Read-Only
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `loop_protect_status` (String)
- `mac_address` (String) Current mac address.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/vlan get [print show-ids]]
terraform import routeros_interface_vlan.interface_vlan "*1"
```
================================================

File: interface_vrrp.md
================================================
# routeros_interface_vrrp (Resource)
## Example Usage
```terraform
resource "routeros_interface_vrrp" "interface_vrrp" {
  interface = "bridge"
  name      = "lan_vrrp"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `authentication` (String) Authentication method to use for VRRP advertisement packets.
- `comment` (String)
- `disabled` (Boolean)
- `group_authority` (String) Allows combining multiple VRRP interfaces to maintain the same VRRP status within the group. `group_authority` was previously called `group_master`, `group_master` is kept for compatibility with scripts, but if both are set only `group_authority` will be taken into account.
- `group_master` (String) Allows combining multiple VRRP interfaces to maintain the same VRRP status within the group. `group_authority` was previously called `group_master`, `group_master` is kept for compatibility with scripts, but if both are set only `group_authority` will be taken into account.
- `interval` (String) VRRP update interval in seconds. Defines how often master sends advertisement packets.
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `on_backup` (String) Script to execute when the node is switched to the backup state.
- `on_fail` (String) Script to execute when the node fails.
- `on_master` (String) Script to execute when the node is switched to master state.
- `password` (String, Sensitive) Password required for authentication. Can be ignored if authentication is not used.
- `preemption_mode` (Boolean) Whether the master node always has the priority. When set to 'no' the backup node will not be elected to be a master until the current master fails, even if the backup node has higher priority than the current master. This setting is ignored if the owner router becomes available
- `priority` (Number) Priority of VRRP node used in Master election algorithm. A higher number means higher priority. '255' is reserved for the router that owns VR IP and '0' is reserved for the Master router to indicate that it is releasing responsibility.
- `remote_address` (String) Specifies the remote address of the other VRRP router for syncing connection tracking. If not set, the system autodetects the remote address via VRRP. The remote address is used only if sync-connection-tracking=yes.Sync connection tracking uses UDP port 8275.
- `sync_connection_tracking` (Boolean) Synchronize connection tracking entries from Master to Backup device.
- `v3_protocol` (String) A protocol that will be used by VRRPv3. Valid only if the version is 3.
- `version` (Number) Which VRRP version to use.
- `vrid` (Number) Virtual Router identifier. Each Virtual router must have a unique id number.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `mac_address` (String) Current mac address.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/vrrp get [print show-ids]]
terraform import routeros_interface_vrrp.interface_vrrp "*0"
```
================================================

File: interface_wireguard.md
================================================
# routeros_interface_wireguard (Resource)
## Example Usage
```terraform
resource "routeros_interface_wireguard" "test_wg_interface" {
  name        = "test_wg_interface"
  listen_port = "13231"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `listen_port` (Number) Port for WireGuard service to listen on for incoming sessions.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `private_key` (String, Sensitive) A base64 private key. If not specified, it will be automatically generated upon interface creation.
### Read-Only
- `id` (String) The ID of this resource.
- `public_key` (String) A base64 public key is calculated from the private key.
- `running` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wireguard get [print show-ids]]
terraform import routeros_interface_wireguard.test_wg_interface "*1"
```
================================================

File: interface_wireguard_peer.md
================================================
# routeros_interface_wireguard_peer (Resource)
## Example Usage
```terraform
resource "routeros_interface_wireguard" "test_wg_interface" {
  name        = "test_wg_interface"
  listen_port = "13231"
}
resource "routeros_interface_wireguard_peer" "wg_peer" {
  interface  = routeros_interface_wireguard.test_wg_interface.name
  public_key = "MY_BASE_64_PUBLIC_KEY"
  allowed_address = [
    "192.168.0.0/16",
    "172.16.0.0/12",
    "10.0.0.0/8",
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `allowed_address` (List of String) List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. The catch-all 0.0.0.0/0 may be specified for matching all IPv4 addresses, and ::/0 may be specified for matching all IPv6 addresses.
- `interface` (String) Name of the interface.
- `public_key` (String) The remote peer's calculated public key.
### Optional
- `client_address` (String) When imported using a qr code for a client (for example, a phone), then this address for the wg interface is set on that device.
- `client_dns` (String) Specify when using WireGuard Server as a VPN gateway for peer traffic.
- `client_endpoint` (String) The IP address and port number of the WireGuard Server.
- `client_keepalive` (String) Same as persistent-keepalive but from peer side.
- `client_listen_port` (Number) The local port upon which this WireGuard tunnel will listen for incoming traffic from peers, and the port from which it will source outgoing packets.
- `comment` (String)
- `disabled` (Boolean)
- `endpoint_address` (String) An endpoint IP or hostname can be left blank to allow remote connection from any address.
- `endpoint_port` (String) An endpoint port can be left blank to allow remote connection from any port.
- `is_responder` (Boolean) Specifies if peer is intended to be connection initiator or only responder. Should be used on WireGuard devices that are used as `servers` for other devices as clients to connect to. Otherwise router will all repeatedly try to connect `endpoint-address` or `current-endpoint-address` causing unnecessary system logs to be written.
- `name` (String) Name of the tunnel.
- `persistent_keepalive` (String) A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from a peer, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds.
- `preshared_key` (String, Sensitive) A **base64** preshared key. Optional, and may be omitted. This option adds an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance.
- `private_key` (String) A base64 private key. If not specified, it will be automatically generated upon interface creation.
### Read-Only
- `current_endpoint_address` (String) The most recent source IP address of correctly authenticated packets from the peer.
- `current_endpoint_port` (Number) The most recent source IP port of correctly authenticated packets from the peer.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `last_handshake` (String) Time in seconds after the last successful handshake.
- `rx` (String) The total amount of bytes received from the peer.
- `tx` (String) The total amount of bytes transmitted to the peer.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wireguard/peers get [print show-ids]]
terraform import routeros_interface_wireguard_peer.wg_peer "*0"
```
================================================

File: interface_wireless_cap.md
================================================
# routeros_interface_wireless_cap (Resource)
## Example Usage
```terraform
resource "routeros_interface_wireless_cap" "settings" {
  discovery_interfaces = ["bridge1"]
  enabled              = true
  interfaces           = ["wlan1", "wlan2"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `bridge` (String) Bridge interface to add the interface as a bridge port.
- `caps_man_addresses` (List of String) List of Manager IP addresses that CAP will attempt to contact during discovery.
- `caps_man_certificate_common_names` (List of String) List of manager certificate common names that CAP will connect to.
- `caps_man_names` (List of String) An ordered list of CAPs Manager names that the CAP will connect to.
- `certificate` (String) Certificate to use for authentication.
- `discovery_interfaces` (Set of String) List of interfaces over which CAP should attempt to discover CAPs Manager.
- `enabled` (Boolean) Disable or enable the CAP functionality.
- `interfaces` (Set of String) List of interfaces managed by CAPs Manager.
- `lock_to_caps_man` (Boolean) Lock CAP to the first CAPsMAN it connects to.
- `static_virtual` (Boolean) An option that creates static virtual interfaces.
### Read-Only
- `id` (String) The ID of this resource.
- `locked_caps_man_common_name` (String) Common name of the CAPsMAN that the CAP is locked to.
- `requested_certificate` (String) Requested certificate.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_interface_wireless_cap.settings .
```
================================================

File: ipip.md
================================================
# routeros_ipip (Resource)
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the ipip interface.
### Optional
- `allow_fast_path` (Boolean) Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
- `clamp_tcp_mss` (Boolean) Controls whether to change MSS size for received TCP SYN packets. When enabled, a router will change the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet will still contain the original MSS, and only after decapsulation the MSS is changed.
- `comment` (String)
- `disabled` (Boolean)
- `dont_fragment` (String)
- `dscp` (String) Set dscp value in GRE header to a fixed value '0..63' or 'inherit' from dscp value taken from tunnelled traffic.
- `ipsec_secret` (String, Sensitive) When secret is specified, router adds dynamic IPsec peer to remote-address with pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
- `keepalive` (String) Tunnel keepalive parameter sets the time interval in which the tunnel running flag will remain even if the remote end of tunnel goes down. If configured time,retries fail, interface running flag is removed. Parameters are written in following format: KeepaliveInterval,KeepaliveRetries where KeepaliveInterval is time interval and KeepaliveRetries - number of retry attempts. KeepaliveInterval is integer 0..4294967295
- `local_address` (String) Source address of the tunnel packets, local on the router.
- `mtu` (String) Layer3 Maximum transmission unit ('auto', 0 .. 65535)
- `remote_address` (String) IP address of the remote end of the tunnel.
### Read-Only
- `actual_mtu` (Number)
- `id` (String) The ID of this resource.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `running` (Boolean)
================================================

File: ipv6_address.md
================================================
# routeros_ipv6_address (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_address" "ipv6_address" {
  address   = "fd55::1/64"
  interface = "ether1"
  disabled  = false
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
### Optional
- `address` (String) IPv6 address. Using the eui_64 and from_pool options can transform the original address! [See docs](https://wiki.mikrotik.com/wiki/Manual:IPv6/Address#Properties)
- `advertise` (Boolean) Whether to enable stateless address configuration. The prefix of that address is automatically advertised to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64.
- `comment` (String)
- `disabled` (Boolean)
- `eui_64` (Boolean) Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address.
- `from_pool` (String) Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address from address property.
- `no_dad` (Boolean) If set indicates that address is anycast address and Duplicate Address Detection should not be performed.
### Read-Only
- `actual_interface` (String) Name of the actual interface the logical one is bound to.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `global` (Boolean) Whether address is global.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `link_local` (Boolean) Whether address is link local.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/address get [print show-ids]]
terraform import routeros_ipv6_address.ipv6_address "*0"
```
================================================

File: ipv6_dhcp_client.md
================================================
# routeros_ipv6_dhcp_client (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_dhcp_client" "inet_provider" {
  pool_name          = "pub-add-pool"
  interface          = "ether1"
  add_default_route  = true
  pool_prefix_length = 64
  request            = ["prefix"]
  disabled           = false
}
resource "routeros_ipv6_dhcp_client" "client" {
  pool_name          = "pub-add-pool"
  interface          = "ether1"
  add_default_route  = true
  pool_prefix_length = 64
  request            = ["prefix"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
- `request` (List of String) To choose if the DHCPv6 request will ask for the address, info or the IPv6 prefix.
### Optional
- `add_default_route` (Boolean) Whether to add default IPv6 route after a client connects.
- `comment` (String)
- `default_route_distance` (Number) Distance of default route. Applicable if add-default-route is set to yes.
- `dhcp_options` (Set of String) Options that are sent to the DHCP server.
- `disabled` (Boolean)
- `pool_name` (String) Name of the IPv6 pool in which received IPv6 prefix will be added
- `pool_prefix_length` (Number) Prefix length parameter that will be set for IPv6 pool in which received IPv6 prefix is added. Prefix length must be greater than the length of the received prefix, otherwise, prefix-length will be set to received prefix length + 8 bits.
- `prefix_hint` (String) Include a preferred prefix length.
- `rapid_commit` (Boolean) Enable DHCP rapid commit (fast address assignment)
- `script` (String) Run this script on the DHCP-client status change. Available variables:
			- pd-valid - if the prefix is acquired by the client;
			- pd-prefix - the prefix acquired by the client if any;
			- na-valid - if the address is acquired by the client;
			- na-address - the address acquired by the client if any.
			- options - array of received options (only ROSv7)
- `use_interface_duid` (Boolean) Specifies the MAC address of the specified interface as the DHCPv6 client DUID.
- `use_peer_dns` (Boolean) Whether to accept the DNS settings advertised by the IPv6 DHCP Server.
### Read-Only
- `address` (String) IPv6 address, which is assigned to DHCPv6 Client from the Server.
- `dhcp_server_v6` (String) The IPv6 address of the DHCP server
- `duid` (String) Auto-generated DUID that is sent to the server. DUID is generated using one of the MAC addresses available on the router.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `expires_after` (String) A time when the IPv6 prefix expires (specified by the DHCPv6 server).
- `gateway` (String) The IP address of the gateway which is assigned by DHCP server.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `prefix` (String) Shows received IPv6 prefix from DHCPv6-PD server
- `status` (String) Shows the status of DHCPv6 Client:
			- stopped - dhcpv6 client is stopped
			- searching - sending "solicit" and trying to get "advertise"  Shows actual (resolved) gateway and interface that will be used for packet forwarding.requesting - sent "request" waiting for "reply"
			- bound - received "reply". Prefix assigned.
			- renewing - sent "renew", waiting for "reply"
			- rebinding - sent "rebind", waiting for "reply"
			- error - reply was not received in time or some other error occurred.
			- stopping - sent "release"
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/dhcp-client/  get [print show-ids]]
terraform import routeros_ipv6_dhcp_client.inet_provider "*1"
```
================================================

File: ipv6_dhcp_client_option.md
================================================
# routeros_ipv6_dhcp_client_option (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_dhcp_client_option" "option" {
  name = "my-dhcp-option"
  code = 60
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `code` (Number) The dhcp-client option code.
- `name` (String) The name that will be used in dhcp-client.
### Optional
- `value` (String) The dhcp-client option
### Read-Only
- `id` (String) The ID of this resource.
- `raw_value` (String) raw_value is computed from value.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/dhcp-client/option get [print show-ids]]
terraform import routeros_ipv6_dhcp_client_option.option "*0"
```
================================================

File: ipv6_firewall_addr_list.md
================================================
# routeros_ipv6_firewall_addr_list (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_firewall_addr_list" "example_list" {
  address = "123:dead:beaf::/64"
  list    = "Example List"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) A single IPv6 address or IPv6 CIDR subnet
- `list` (String) Name for the address list of the added IPv6 address.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `timeout` (String) Time after address will be removed from address list. If timeout is not specified,
the address will be stored into the address list permanently.  
	> Please plan your work logic based on the fact that after the timeout    
	> the resource has been destroyed outside of Terraform.
### Read-Only
- `creation_time` (String) Rule creation time
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/firewall/address-list get [print show-ids]]
terraform import routeros_ipv6_firewall_addr_list.example_list "*0"
```
================================================

File: ipv6_firewall_filter.md
================================================
# routeros_ipv6_firewall_filter (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_firewall_filter" "rule" {
  action      = "accept"
  chain       = "forward"
  src_address = "2001:DB8:1000::1"
  dst_address = "2001:DB8:2000::1"
  dst_port    = "443"
  protocol    = "tcp"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) Action to take if a packet is matched by the rule
- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
### Optional
- `address_list_timeout` (String) Time interval after which the address will be removed from the address list specified by address-list parameter. Used in conjunction with add-dst-to-address-list or add-src-to-address-list actions.
- `comment` (String)
- `connection_bytes` (String) Matches packets only if a given amount of bytes has been transfered through the particular connection.
- `connection_limit` (String) Matches connections per address or address block after given value is reached. Should be used together with connection-state=new and/or with tcp-flags=syn because matcher is very resource intensive.
- `connection_mark` (String) Matches packets marked via mangle facility with particular connection mark. If no-mark is set, rule will match any unmarked connection.
- `connection_rate` (String) Connection Rate is a firewall matcher that allow to capture traffic based on present speed of the connection (0..4294967295).
- `connection_state` (String) Interprets the connection tracking analysis data for a particular packet.
- `connection_type` (String) Matches packets from related connections based on information from their connection tracking helpers.
- `content` (String) Match packets that contain specified text.
- `disabled` (Boolean)
- `dscp` (Number) Matches DSCP IP header field.
- `dst_address` (String) Matches packets which destination is equal to specified IP or falls into specified IP range.
- `dst_address_list` (String) Matches destination address of a packet against user-defined address list.
- `dst_address_type` (String) Matches destination address type.
- `dst_limit` (String) Matches packets until a given rate is exceeded.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `headers` (String) Extension headers. Look at the Extras tab in the v6 filter rules.
- `hop_limit` (String) IPv6 TTL. Look at the Extras tab in the v6 filter rules.
- `icmp_options` (String) Matches ICMP type: code fields.
- `in_bridge_port` (String) Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `in_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as in-bridge-port.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `ingress_priority` (Number) Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `ipsec_policy` (String) Matches the policy used by IPsec. Value is written in the following format: direction, policy.
- `jump_target` (String) Name of the target chain to jump to. Applicable only if action=jump.
- `limit` (String) Matches packets up to a limited rate (packet rate or bit rate). A rule using this matcher will match until this limit is reached. Parameters are written in the following format: rate[/time],burst:mode.
- `log` (Boolean) Add a message to the system log.
- `log_prefix` (String) Adds specified text at the beginning of every log message. Applicable if action=log or log=yes configured.
- `nth` (String) Matches every nth packet: nth=2,1 rule will match every first packet of 2, hence, 50% of all the traffic that is matched by the rule
- `out_bridge_port` (String) Actual interface the packet is leaving the router if the outgoing interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `out_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as out-bridge-port.
- `out_interface` (String) Interface the packet is leaving the router.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `packet_mark` (String) Matches packets marked via mangle facility with particular packet mark. If no-mark is set, the rule will match any unmarked packet.
- `packet_size` (String) Matches packets of specified size or size range in bytes.
- `per_connection_classifier` (String) PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `port` (String) Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if protocol is TCP or UDP
- `priority` (Number) Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority that has been set using the set-priority action.
- `protocol` (String) Matches particular IP protocol specified by protocol name or number.
- `random` (Number) Matches packets randomly with a given probability.
- `reject_with` (String) Specifies ICMP error to be sent back if the packet is rejected. Applicable if action=reject.
- `routing_mark` (String) Matches packets marked by mangle facility with particular routing mark.
- `src_address` (String) Matches packets which source is equal to specified IP or falls into a specified IP range.
- `src_address_list` (String) Matches source address of a packet against user-defined address list.
- `src_address_type` (String) Matches source address type.
- `src_mac_address` (String) Matches source MAC address of the packet.
- `src_port` (String) List of source ports and ranges of source ports. Applicable only if a protocol is TCP or UDP.
- `tcp_flags` (String) Matches specified TCP flags.
- `tcp_mss` (String) Matches TCP MSS value of an IP packet.
- `time` (String) Allows to create a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date.
- `tls_host` (String) Allows matching HTTPS traffic based on TLS SNI hostname.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/firewall/filter get [print show-ids]]
terraform import routeros_ipv6_firewall_filter.rule "*0"
```
================================================

File: ipv6_neighbor_discovery.md
================================================
# routeros_ipv6_neighbor_discovery (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_neighbor_discovery" "test" {
  interface                     = "ether1"
  hop_limit                     = 33
  advertise_dns                 = false
  advertise_mac_address         = true
  disabled                      = false
  managed_address_configuration = true
  mtu                           = 9000
  other_configuration           = true
  pref64_prefixes               = []
  ra_delay                      = "3s"
  ra_interval                   = "3m20s-10m"
  ra_lifetime                   = "30m"
  ra_preference                 = "high"
  reachable_time                = "10m"
  retransmit_interval           = "12m"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) The interface on which to run neighbor discovery.all - run ND on all running interfaces.
### Optional
- `___drop_val___` (String) <em>A list of values when generated by RouterOs will be dropped, useful to default values as 'unspecified' for null</em>
- `advertise_dns` (Boolean) Option to redistribute DNS server information using RADVD. You will need a running client-side software with Router Advertisement DNS support to take advantage of the advertised DNS information.
- `advertise_mac_address` (Boolean) When set, the link-layer address of the outgoing interface is included in the RA.
- `comment` (String)
- `disabled` (Boolean)
- `dns` (String) Specify a single IPv6 address or comma separated list of addresses that will be provided to hosts for DNS server configuration.
- `dns_servers` (String) Specify a single IPv6 address or list of addresses that will be provided to hosts for DNS server configuration.
- `hop_limit` (Number) The default value that should be placed in the Hop Count field of the IP header for outgoing (unicast) IP packets.
- `managed_address_configuration` (Boolean) Name of the IPv6 pool in which received IPv6 prefix will be added
- `mtu` (Number) The flag indicates whether hosts should use stateful autoconfiguration (DHCPv6) to obtain addresses
- `other_configuration` (Boolean) The flag indicates whether hosts should use stateful autoconfiguration to obtain additional information (excluding addresses).
- `pref64` (List of String) Specify IPv6 prefix or list of prefixes within /32, /40. /48, /56, /64, or /96 subnet that will be provided to hosts as NAT64 prefixes.
- `ra_delay` (String) The minimum time allowed between sending multicast router advertisements from the interface.
- `ra_interval` (String) The min-max interval allowed between sending unsolicited multicast router advertisements from the interface.
- `ra_lifetime` (String) Specify the router preference that is communicated to IPv6 hosts through router advertisements.The preference value in the router advertisements enables IPv6 hosts to select a default router to reach a remote destination
- `ra_preference` (String) Specify the router preference that is communicated to IPv6 hosts through router advertisements.The preference value in the router advertisements enables IPv6 hosts to select a default router to reach a remote destination
- `reachable_time` (String) Specify the router preference that is communicated to IPv6 hosts through router advertisements.The preference value in the router advertisements enables IPv6 hosts to select a default router to reach a remote destination
- `retransmit_interval` (String) The time between retransmitted Neighbor Solicitation messages.Used by address resolution and the Neighbor Unreachability Detection algorithm (see Sections 7.2 and 7.3 of RFC 2461)
### Read-Only
- `default` (Boolean) Neighbor discovery entry is the default configuration.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/nd get [print show-ids]]
terraform import routeros_ipv6_neighbor_discovery.ndether1 "*0"
```
================================================

File: ipv6_route.md
================================================
# routeros_ipv6_route (Resource)
## Example Usage
```terraform
resource "routeros_ipv6_route" "a_route" {
  dst_address = "::/0"
  gateway     = "2001:DB8:1000::1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `dst_address` (String) IP prefix of route, specifies destination addresses that this route can be used for.
- `gateway` (String) Array of IP addresses or interface names. Specifies which host or interface packets should be sent to (IP | interface | IP%interface | IP@table[, IP | string, [..]]).
### Optional
- `blackhole` (Boolean) It's a blackhole route. If you need to cancel route marking, then simply delete the parameter from the configuration of the TF. The value of the parameter (true or false) has no effect on the MT processing logic.
- `comment` (String)
- `disabled` (Boolean)
- `distance` (Number) Value used in route selection. Routes with smaller distance value are given preference.
- `pref_src` (String) Which of the local IP addresses to use for locally originated packets that are sent via this route. Value of this property has no effect on forwarded packets. If value of this property is set to IP address that is not local address of this router then the route will be inactive (in ROS v6, ROS v7 allows IP spoofing).
- `routing_table` (String) Routing table this route belongs to.
- `scope` (Number) Used in nexthop resolution. Route can resolve nexthop only through routes that have scope less than or equal to the target-scope of this route.
- `target_scope` (Number) Used in nexthop resolution. This is the maximum value of scope for a route through which a nexthop of this route can be resolved.
- `vrf_interface` (String) VRF interface name.
### Read-Only
- `active` (Boolean) A flag indicates whether the route is elected as Active and eligible to be added to the FIB.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `ecmp` (Boolean) A flag indicates whether the route is added as an Equal-Cost Multi-Path route in the FIB.
- `hw_offloaded` (Boolean) Indicates whether the route is eligible to be hardware offloaded on supported hardware.
- `id` (String) The ID of this resource.
- `immediate_gw` (String) Shows actual (resolved) gateway and interface that will be used for packet forwarding.
- `inactive` (Boolean)
- `static` (Boolean)
- `suppress_hw_offload` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/route get [print show-ids]]
terraform import routeros_ipv6_route.a_route "*0"
```
================================================

File: ip_address.md
================================================
# routeros_ip_address (Resource)
## Example Usage
```terraform
resource "routeros_ip_address" "address" {
  address   = "10.0.0.1/24"
  interface = "bridge"
  network   = "10.0.0.0"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) IP address.
- `interface` (String) Name of the interface.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `network` (String) IP address for the network. For point-to-point links it should be the address of the remote end. Starting from v5RC6 this parameter is configurable only for addresses with /32 netmask (point to point links)
### Read-Only
- `actual_interface` (String) Name of the actual interface the logical one is bound to.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/address get [print show-ids]]
terraform import routeros_ip_address.address "*0"
```
================================================

File: ip_cloud.md
================================================
# routeros_ip_cloud (Resource)
## Example Usage
```terraform
resource "routeros_ip_cloud" "test" {
  ddns_enabled         = true
  update_time          = false
  ddns_update_interval = "11m"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `back_to_home_vpn` (String) Enables or revokes and disables the Back to Home service. ddns-enabled has to be set to yes, for BTH to function.
- `ddns_enabled` (Boolean) If set to yes, then the device will send an encrypted message to the MikroTik's Cloud server. The server will then decrypt the message and verify that the sender is an authentic MikroTik device. If all is OK, then the MikroTik's Cloud server will create a DDNS record for this device and send a response to the device. Every minute the IP/Cloud service on the router will check if WAN IP address matches the one sent to MikroTik's Cloud server and will send encrypted update to cloud server if IP address changes.
- `ddns_update_interval` (String) If set DDNS will attempt to connect IP Cloud servers at the set interval. If set to none it will continue to internally check IP address update and connect to IP Cloud servers as needed. Useful if IP address used is not on the router itself and thus, cannot be checked as a value internal to the router.
- `update_time` (Boolean) If set to yes then router clock will be set to time, provided by cloud server IF there is no NTP or SNTP client enabled. If set to no, then IP/Cloud service will never update the device's clock. If update-time is set to yes, Clock will be updated even when ddns-enabled is set to no.
### Read-Only
- `dns_name` (String) Shows DNS name assigned to the rdevice. Name consists of 12 character serial number appended by .sn.mynetname.net. This field is visible only after at least one ddns-request is successfully completed.
- `id` (String) The ID of this resource.
- `public_address` (String) Shows device's IPv4 address that was sent to cloud server. This field is visible only after at least one IP Cloud request was successfully completed.
- `public_address_ipv6` (String) Shows device's IPv6 address that was sent to cloud server. This field is visible only after at least one IP Cloud request was successfully completed.
- `status` (String) Contains text string that describes current dns-service state. The messages are self explanatory  updating... updated Error: no Internet connection Error: request timed out Error: REJECTED. Contact MikroTik support Error: internal error - should not happen. One possible cause is if router runs out of memory.
- `warning` (String) Shows a warning message if IP address sent by the device differs from the IP address in UDP packet header as visible by the MikroTik's Cloud server. Typically this happens if the device is behind NAT. Example: 'DDNS server received request from IP 123.123.123.123 but your local IP was 192.168.88.23; DDNS service might not work'
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_cloud.test .
```
================================================

File: ip_cloud_advanced.md
================================================
# routeros_ip_cloud_advanced (Resource)
## Example Usage
```terraform
resource "routeros_ip_cloud_advanced" "settings" {
  use_local_address = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `use_local_address` (Boolean) An option whether to assign an internal router address to the dynamic DNS name.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_cloud_advanced.settings .
```
================================================

File: ip_dhcp_client.md
================================================
# routeros_ip_dhcp_client (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_client" "client" {
  interface = "bridge"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
### Optional
- `add_default_route` (String) Whether to install default route in routing table received from DHCP server.
- `comment` (String)
- `default_route_distance` (Number) Distance of default route. Applicable if add-default-route is set to yes.
- `dhcp_options` (String) Options that are sent to the DHCP server.
- `disabled` (Boolean)
- `script` (String) A script.
- `use_peer_dns` (Boolean) Whether to accept the DNS settings advertised by DHCP Server (will override the settings put in the /ip dns submenu).
- `use_peer_ntp` (Boolean) Whether to accept the NTP settings advertised by DHCP Server (will override the settings put in the /system ntp client submenu).
### Read-Only
- `address` (String) IP address and netmask, which is assigned to DHCP Client from the Server.
- `dhcp_server` (String) The IP address of the DHCP server.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `expires_after` (String) A time when the lease expires (specified by the DHCP server).
- `gateway` (String) The IP address of the gateway which is assigned by DHCP server.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `primary_dns` (String) The IP address of the first DNS resolver, that was assigned by the DHCP server.
- `primary_ntp` (String) The IP address of the primary NTP server, assigned by the DHCP server.
- `secondary_dns` (String) The IP address of the second DNS resolver, assigned by the DHCP server.
- `secondary_ntp` (String) The IP address of the secondary NTP server, assigned by the DHCP server.
- `status` (String)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-client get [print show-ids]]
terraform import routeros_ip_dhcp_client.client "*0"
```
================================================

File: ip_dhcp_client_option.md
================================================
# routeros_ip_dhcp_client_option (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_client_option" "option" {
  name = "my-dhcp-option"
  code = 60
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `code` (Number) The dhcp-client option code.
- `name` (String) The name that will be used in dhcp-client.
### Optional
- `raw_value` (String) raw_value is computed from value.
- `value` (String) The dhcp-client option
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-client/option get [print show-ids]]
terraform import routeros_ip_dhcp_client_option.option "*0"
```
================================================

File: ip_dhcp_relay.md
================================================
# routeros_ip_dhcp_relay (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_relay" "relay" {
  name        = "test relay"
  interface   = "ether1"
  dhcp_server = "0.0.0.1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `dhcp_server` (String) List of DHCP servers' IP addresses which should the DHCP requests be forwarded to.
- `interface` (String) Interface name the DHCP relay will be working on.
- `name` (String) Descriptive name for the relay.
### Optional
- `add_relay_info` (Boolean) Adds DHCP relay agent information if enabled according to RFC 3046. Agent Circuit ID Sub-option contains mac address of an interface, Agent Remote ID Sub-option contains MAC address of the client from which request was received.
- `delay_threshold` (String) If secs field in DHCP packet is smaller than delay-threshold, then this packet is ignored.
- `disabled` (Boolean)
- `local_address` (String) The unique IP address of this DHCP relay needed for DHCP server to distinguish relays. If set to 0.0.0.0 - the IP address will be chosen automatically
- `relay_info_remote_id` (String) Specified string will be used to construct Option 82 instead of client's MAC address. Option 82 consist of: interface from which packets was received + client mac address or relay-info-remote-id
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-relay get [print show-ids]]
terraform import routeros_ip_dhcp_relay.relay "*0"
```
================================================

File: ip_dhcp_server.md
================================================
# routeros_ip_dhcp_server (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_server" "server" {
  address_pool = "my_address_pool"
  interface    = "bridge"
  name         = "bridge_dhcp"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Name of the interface.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `add_arp` (Boolean) Whether to add dynamic ARP entry.
- `address_pool` (String) IP pool, from which to take IP addresses for the clients. If set to static-only, then only the clients that have a static lease (added in lease submenu) will be allowed.
- `allow_dual_stack_queue` (Boolean) Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the MAC address and DUID for identification. Requires IPv6 DHCP Server to have this option enabled as well to work properly.
- `always_broadcast` (Boolean) Always send replies as broadcasts even if destination IP is known.
- `authoritative` (String) Option changes the way how a server responds to DHCP requests.
- `bootp_lease_time` (String) Accepts two predefined options or time value: * forever - lease never expires * lease-time - use time from lease-time parameter
- `bootp_support` (String) Support for BOOTP clients.
- `client_mac_limit` (Number) Specifies whether to limit specific number of clients per single MAC address.
- `comment` (String)
- `conflict_detection` (Boolean) Allows to disable/enable conflict detection. If option is enabled, then whenever server tries to assign a lease it will send ICMP and ARP messages to detect whether such address in the network already exist. If any of above get reply address is considered already used. Conflict detection must be disabled when any kind of DHCP client limitation per port or per mac is used.
- `delay_threshold` (String) If secs field in DHCP packet is smaller than delay-threshold, then this packet is ignored. If set to none - there is no threshold (all DHCP packets are processed).
- `dhcp_option_set` (String) Use custom set of DHCP options defined in option sets menu.
- `disabled` (Boolean)
- `insert_queue_before` (String) Specify where to place dynamic simple queue entries for static DCHP leases with rate-limit parameter set.
- `lease_script` (String) A script that will be executed after a lease is assigned or de-assigned.
- `lease_time` (String) The time that a client may use the assigned address. The client will try to renew this address after half of this time and will request a new address after the time limit expires.
- `parent_queue` (String)
- `relay` (String) The IP address of the relay this DHCP server.
- `src_address` (String) The address which the DHCP client must send requests to in order to renew an IP address lease.
- `use_framed_as_classless` (Boolean) Forward RADIUS Framed-Route as a DHCP Classless-Static-Route to DHCP-client.
- `use_radius` (String) Whether to use RADIUS server.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server get [print show-ids]]
terraform import routeros_ip_dhcp_server.server "*1"
```
================================================

File: ip_dhcp_server_config.md
================================================
# routeros_ip_dhcp_server_config (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_server_config" "settings" {
  accounting        = true
  interim_update    = "1m"
  radius_password   = "same-as-user"
  store_leases_disk = "10m"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `accounting` (Boolean) An option that enables accounting for DHCP leases.
- `interim_update` (String) An option determining whether the DHCP server sends periodic updates to the accounting server during a lease.
- `radius_password` (String) An option to set the password parameter for the RADIUS server. This option is available in RouterOS starting from version 7.0.
- `store_leases_disk` (String) An option of how often the DHCP leases will be stored on disk.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_dhcp_server_config.settings .
```
================================================

File: ip_dhcp_server_lease.md
================================================
# routeros_ip_dhcp_server_lease (Resource)
Creates a DHCP lease on the mikrotik device.
## Example Usage
```terraform
resource "routeros_ip_dhcp_server_lease" "dhcp_lease" {
  address     = "10.0.0.2"
  mac_address = "AA:BB:CC:DD:11:22"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) The IP address of the DHCP lease to be created.
- `mac_address` (String) The MAC addreess of the DHCP lease to be created.
### Optional
- `address_lists` (String) Address list to which address will be added if lease is bound.
- `allow_dual_stack_queue` (Boolean) Creates a single simple queue entry for both IPv4 and IPv6 addresses, uses the MAC address and DUID for identification.
- `always_broadcast` (Boolean) Send all replies as broadcasts.
- `block_access` (Boolean) Whether to block access for this DHCP client (true|false).
- `client_id` (String) If specified, must match DHCP 'client identifier' option of the request.
- `comment` (String)
- `dhcp_option` (String) Add additional DHCP options.
- `dhcp_option_set` (String) Add additional set of DHCP options.
- `disabled` (Boolean)
- `insert_queue_before` (String) Specify where to place dynamic simple queue entries for static DCHP leases with rate-limit parameter set.
- `lease_time` (String) Time that the client may use the address. If set to 0s lease will never expire.
- `rate_limit` (String) Adds a dynamic simple queue to limit IP's bandwidth to a specified rate. Requires the lease to be static.
- `server` (String) Server name which serves this client.
- `use_src_mac` (Boolean) When this option is set server uses source MAC address instead of received CHADDR to assign address.
### Read-Only
- `active_address` (String) The IP address of the machine currently holding the DHCP lease.
- `active_client_id` (String) Actual client-id of the client.
- `active_hostname` (String) The hostname of the machine currently holding the DHCP lease.
- `active_mac_address` (String) The MAC address of of the machine currently holding the DHCP lease.
- `active_server` (String) Actual dhcp server, which serves this client.
- `agent_circuit_id` (String) Circuit ID of DHCP relay agent. If each character should be valid ASCII text symbol or else this value is displayed as hex dump.
- `agent_remote_id` (String) Remote ID, set by DHCP relay agent.
- `blocked` (Boolean) Whether the lease is blocked.
- `dynamic` (Boolean) Whether the dhcp lease is static or dynamic. Dynamic leases are not guaranteed to continue to be assigned to that specific device.
- `expires_after` (String) Time until lease expires.
- `host_name` (String) The hostname of the device
- `id` (String) The ID of this resource.
- `last_seen` (String)
- `radius` (String) Shows if this dynamic lease is authenticated by RADIUS or not.
- `src_mac_address` (String) Source MAC address.
- `status` (String) Lease status.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/lease get [print show-ids]]
terraform import routeros_ip_dhcp_server_lease.dhcp_lease "*0"
```
================================================

File: ip_dhcp_server_network.md
================================================
# routeros_ip_dhcp_server_network (Resource)
## Example Usage
```terraform
resource "routeros_ip_dhcp_server_network" "dhcp_server_network" {
  address    = "10.0.0.0/24"
  gateway    = "10.0.0.1"
  dns_server = ["1.1.1.1"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) The network DHCP server(s) will lease addresses from.
### Optional
- `boot_file_name` (String) Boot filename.
- `caps_manager` (List of String) A list of IP addresses for one or more CAPsMAN system managers. DHCP Option 138 (capwap) will be used.
- `comment` (String)
- `dhcp_option` (List of String) Add additional DHCP options from the option list.
- `dhcp_option_set` (String) Add an additional set of DHCP options.
- `dns_none` (Boolean) If set, then DHCP Server will not pass dynamic DNS servers configured on the router to the DHCP clients if no DNS Server in DNS-server is set.
- `dns_server` (List of String) The DHCP client will use these as the default DNS servers. Two DNS servers can be specified to be used by the DHCP client as primary and secondary DNS servers.
- `domain` (String) The DHCP client will use this as the 'DNS domain' setting for the network adapter.
- `gateway` (String) The default gateway to be used by DHCP Client.
- `netmask` (Number) The actual network mask is to be used by the DHCP client. If set to '0' - netmask from network address will be used.
- `next_server` (String) The IP address of the next server to use in bootstrap.
- `ntp_server` (List of String) The DHCP client will use these as the default NTP servers. Two NTP servers can be specified to be used by the DHCP client as primary and secondary NTP servers
- `wins_server` (List of String) The Windows DHCP client will use these as the default WINS servers. Two WINS servers can be specified to be used by the DHCP client as primary and secondary WINS servers
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/network get [print show-ids]]
terraform import routeros_ip_dhcp_server_network.dhcp_server_network "*0"
```
================================================

File: ip_dhcp_server_option.md
================================================
# routeros_ip_dhcp_server_option (Resource)
Creates a DHCP lease on the mikrotik device.
## Example Usage
```terraform
resource "routeros_ip_dhcp_server_option" "jumbo_frame_opt" {
  code  = 77
  name  = "jumbo-mtu-opt"
  value = "0x2336"
}
resource "routeros_ip_dhcp_server_option" "tftp_option" {
  code  = 66
  name  = "tftpserver-66"
  value = "s'10.10.10.22'"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `code` (Number) The number of the DHCP option
- `name` (String) The name of the DHCP option
- `value` (String) The value with formatting using Mikrotik settings https://wiki.mikrotik.com/wiki/Manual:IP/DHCP_Server#DHCP_Options
### Optional
- `force` (Boolean) Force the DHCP option from the server-side even if the DHCP-client does not request such parameter.
### Read-Only
- `id` (String) The ID of this resource.
- `raw_value` (String) The computed value of the option as an hex value
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/option/get [print show-ids]]
terraform import routeros_ip_dhcp_server_option.tftp_option "*1"
```
================================================

File: ip_dhcp_server_option_set.md
================================================
# routeros_ip_dhcp_server_option_set (Resource)
Creates a DHCP lease on the mikrotik device.
## Example Usage
```terraform
resource "routeros_ip_dhcp_server_option" "jumbo_frame_opt" {
  code  = 77
  name  = "jumbo-mtu-opt"
  value = "0x2336"
}
resource "routeros_ip_dhcp_server_option" "tftp_option" {
  code  = 66
  name  = "tftpserver-66"
  value = "s'10.10.10.22'"
}
resource "routeros_ip_dhcp_server_option_set" "lan_option_set" {
  name    = "lan-option-set"
  options = join(",", [routeros_ip_dhcp_server_option.jumbo_frame_opt.name, routeros_ip_dhcp_server_option.tftp_option.name])
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) The name of the DHCP option
- `options` (String) The comma sepparated list of options
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/option/sets/get [print show-ids]]
terraform import routeros_ip_dhcp_server_option_set.lan_option_set "*1"
```
================================================

File: ip_dns.md
================================================
# routeros_ip_dns (Resource)
A MikroTik router with DNS feature enabled can be set as a DNS server for any DNS-compliant client.
## Example Usage
```terraform
resource "routeros_dns" "dns-server" {
  allow_remote_requests = true
  servers = [
    "2606:4700:4700::1111,1.1.1.1",
    "2606:4700:4700::1001,1.0.0.1",
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `address_list_extra_time` (String)
- `allow_remote_requests` (Boolean) Specifies whether to allow network requests.
- `cache_max_ttl` (String) Maximum time-to-live for cache records. In other words, cache records will expire unconditionally after cache-max-ttl time. Shorter TTL received from DNS servers are respected. *Default: 1w*
- `cache_size` (Number) Specifies the size of DNS cache in KiB (64..4294967295). *Default: 2048*
- `doh_max_concurrent_queries` (Number) Specifies how many DoH concurrent queries are allowed.
- `doh_max_server_connections` (Number) Specifies how many concurrent connections to the DoH server are allowed.
- `doh_timeout` (String) Specifies how long to wait for query response from the DoH server.
- `max_concurrent_queries` (Number) Specifies how much concurrent queries are allowed. *Default: 100*
- `max_concurrent_tcp_sessions` (Number) Specifies how much concurrent TCP sessions are allowed. *Default: 20*
- `max_udp_packet_size` (Number) Maximum size of allowed UDP packet. *Default: 4096*
- `query_server_timeout` (String) Specifies how long to wait for query response from one server. Time can be specified in milliseconds. *Default: 2s*
- `query_total_timeout` (String) Specifies how long to wait for query response in total. Note that this setting must be configured taking into account query_server_timeout and number of used DNS server. Time can be specified in milliseconds. *Default: 10s*
- `servers` (List of String) List of DNS server IPv4/IPv6 addresses.
- `use_doh_server` (String) DNS over HTTPS (DoH) server URL.
	> Mikrotik strongly suggest not use third-party download links for certificate fetching. 
	Use the Certificate Authority's own website.
	> RouterOS prioritize DoH over DNS server if both are configured on the device.
- `verify_doh_cert` (Boolean) DoH certificate verification. [See docs](https://wiki.mikrotik.com/wiki/Manual:IP/DNS#DNS_over_HTTPS).
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `cache_used` (Number) Shows the currently used cache size in KiB.
- `dynamic_servers` (String) List of dynamically added DNS server from different services, for example, DHCP.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The DNS Settings can not be imported. 
#Terraform will ignore the current settings and will overwrite the current settings with the settings defined in Terraform.
```
================================================

File: ip_dns_record.md
================================================
# routeros_ip_dns_record (Resource)
Creates a DNS record on the MikroTik device.
## Example Usage
```terraform
resource "routeros_ip_dns_record" "name_record" {
  name    = "router.lan"
  address = "192.168.88.1"
  type    = "A"
}
resource "routeros_ip_dns_record" "regexp_record" {
  regexp  = ".*pool.ntp.org"
  address = "192.168.88.1"
  type    = "A"
}
resource "routeros_dns_record" "aaaa_record" {
  name    = "ipv6.lan"
  address = "ff00::1"
  type    = "AAAA"
}
resource "routeros_dns_record" "cname_record" {
  name  = "cname.lan"
  cname = "ipv4.lan"
  type  = "CNAME"
}
resource "routeros_dns_record" "fwd_record" {
  name       = "fwd.lan"
  forward_to = "127.0.0.1"
  type       = "FWD"
}
resource "routeros_dns_record" "mx_record" {
  name          = "mx.lan"
  mx_exchange   = "127.0.0.1"
  mx_preference = 10
  type          = "MX"
}
resource "routeros_dns_record" "ns_record" {
  name = "ns.lan"
  ns   = "127.0.0.1"
  type = "NS"
}
resource "routeros_dns_record" "nxdomain_record" {
  name = "nxdomain.lan"
  type = "NXDOMAIN"
}
resource "routeros_dns_record" "srv_record" {
  name         = "srv.lan"
  srv_port     = 8080
  srv_priority = 10
  srv_target   = "127.0.0.1"
  srv_weight   = 100
  type         = "SRV"
}
resource "routeros_dns_record" "txt_record" {
  name = "_acme-challenge.yourwebsite.com"
  text = "dW6MrI3nBy3eJgYWH3QAg1Cwk_TvjFESOuKo+mp6nm1"
  type = "TXT"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `type` (String) Type of the DNS record. Available values are: A, AAAA, CNAME, FWD, MX, NS, NXDOMAIN, SRV, TXT
### Optional
- `address` (String) The A record to be returend from the DNS hostname.
- `address_list` (String) Name of the Firewall address list to which address must be dynamically added when some request matches the entry.
- `cname` (String) Alias name for a domain name.
- `comment` (String)
- `disabled` (Boolean)
- `forward_to` (String) The IP address of a domain name server to which a particular DNS request must be forwarded.
- `match_subdomain` (Boolean) Whether the record will match requests for subdomains.
- `mx_exchange` (String) The domain name of the MX server.
- `mx_preference` (Number) Preference of the particular MX record.
- `name` (String) The name of the DNS hostname to be created.
- `ns` (String) Name of the authoritative domain name server for the particular record.
- `regexp` (String) DNS regexp. Regexp entries are case sensitive, but since DNS requests are not case sensitive, RouterOS converts DNS names to lowercase, you should write regex only with lowercase letters.
- `srv_port` (Number) The TCP or UDP port on which the service is to be found.
- `srv_priority` (Number) Priority of the particular SRV record.
- `srv_target` (String) The canonical hostname of the machine providing the service ends in a dot.
- `srv_weight` (String) Weight of the particular SRC record.
- `text` (String) Textual information about the domain name.
- `ttl` (String) The ttl of the DNS record.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dns/static get [print show-ids]]
terraform import routeros_ip_dns_record.name_record "*0"
```
================================================

File: ip_firewall_addr_list.md
================================================
# routeros_ip_firewall_addr_list (Resource)
## Example Usage
```terraform
resource "routeros_ip_firewall_addr_list" "example_list" {
  address = "1.1.1.1"
  list    = "Example List"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) A single IP address or range of IPs to add to address list or DNS name. You can input for example, '192.168.0.0-192.168.1.255' and it will auto modify the typed entry to 192.168.0.0/23 on saving.
- `list` (String) Name for the address list of the added IP address.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `timeout` (String) Time after address will be removed from address list. If timeout is not specified,
the address will be stored into the address list permanently.  
	> Please plan your work logic based on the fact that after the timeout    
	> the resource has been destroyed outside of Terraform.
### Read-Only
- `creation_time` (String) Rule creation time
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/address-list get [print show-ids]]
terraform import routeros_ip_firewall_addr_list.example_list "*0"
```
================================================

File: ip_firewall_connection_tracking.md
================================================
# routeros_ip_firewall_connection_tracking (Resource)
## Example Usage
```terraform
resource "routeros_ip_firewall_connection_tracking" "data" {
  enabled                  = "yes"
  generic_timeout          = "3m"
  icmp_timeout             = "3m"
  loose_tcp_tracking       = "false"
  tcp_close_timeout        = "3m"
  tcp_close_wait_timeout   = "3m"
  tcp_established_timeout  = "3m"
  tcp_fin_wait_timeout     = "3m"
  tcp_last_ack_timeout     = "3m"
  tcp_max_retrans_timeout  = "3m"
  tcp_syn_received_timeout = "3m"
  tcp_syn_sent_timeout     = "3m"
  tcp_time_wait_timeout    = "3m"
  tcp_unacked_timeout      = "3m"
  udp_stream_timeout       = "3m"
  udp_timeout              = "3m"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `enabled` (String) Allows to disable or enable connection tracking. Disabling connection tracking will cause several firewall features to stop working. 
				          See the list of affected features. Starting from v6.0rc2 default value is auto. This means that connection tracing is disabled until at least one firewall rule is added.
- `generic_timeout` (String) Timeout for all other connection entries
- `icmp_timeout` (String) ICMP connection timeout
- `loose_tcp_tracking` (String) Disable picking up already established connections
- `tcp_close_timeout` (String) No documentation
- `tcp_close_wait_timeout` (String) No documentation
- `tcp_established_timeout` (String) Time when established TCP connection times out.
- `tcp_fin_wait_timeout` (String) No documentation
- `tcp_last_ack_timeout` (String) No documentation
- `tcp_max_retrans_timeout` (String) No documentation
- `tcp_syn_received_timeout` (String) TCP SYN timeout.
- `tcp_syn_sent_timeout` (String) TCP SYN timeout.
- `tcp_time_wait_timeout` (String) No documentation
- `tcp_unacked_timeout` (String) No documentation
- `udp_stream_timeout` (String) Specifies the timeout of UDP connections that has seen packets in both directions
- `udp_timeout` (String) Specifies the timeout for UDP connections that have seen packets in one direction
### Read-Only
- `active_ipv4` (Boolean) documentation is missing
- `active_ipv6` (Boolean) documentation is missing
- `id` (String) The ID of this resource.
- `max_entries` (String) Max amount of entries that the connection tracking table can hold. This value depends on the installed amount of RAM.
                          Note that the system does not create a maximum_size connection tracking table when it starts, it may increase if the situation demands it and the system still has free ram, but size will not exceed 1048576
================================================

File: ip_firewall_filter.md
================================================
# routeros_ip_firewall_filter (Resource)
## Example Usage
```terraform
resource "routeros_ip_firewall_filter" "rule" {
  action      = "accept"
  chain       = "forward"
  src_address = "10.0.0.1"
  dst_address = "10.0.1.1"
  dst_port    = "443"
  protocol    = "tcp"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) Action to take if a packet is matched by the rule
- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
### Optional
- `address_list` (String) Name of the address list used in 'add-dst-to-address-list' and 'add-src-to-address-list' actions.
- `address_list_timeout` (String) Time interval after which the address will be removed from the address list specified by address-list parameter. Used in conjunction with add-dst-to-address-list or add-src-to-address-list actions.
- `comment` (String)
- `connection_bytes` (String) Matches packets only if a given amount of bytes has been transfered through the particular connection.
- `connection_limit` (String) Matches connections per address or address block after given value is reached. Should be used together with connection-state=new and/or with tcp-flags=syn because matcher is very resource intensive.
- `connection_mark` (String) Matches packets marked via mangle facility with particular connection mark. If no-mark is set, rule will match any unmarked connection.
- `connection_nat_state` (String) Can match connections that are srcnatted, dstnatted or both.
- `connection_rate` (String) Connection Rate is a firewall matcher that allow to capture traffic based on present speed of the connection (0..4294967295).
- `connection_state` (String) Interprets the connection tracking analysis data for a particular packet.
- `connection_type` (String) Matches packets from related connections based on information from their connection tracking helpers.
- `content` (String) Match packets that contain specified text.
- `disabled` (Boolean)
- `dscp` (Number) Matches DSCP IP header field.
- `dst_address` (String) Matches packets which destination is equal to specified IP or falls into specified IP range.
- `dst_address_list` (String) Matches destination address of a packet against user-defined address list.
- `dst_address_type` (String) Matches destination address type.
- `dst_limit` (String) Matches packets until a given rate is exceeded.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `fragment` (Boolean) Matches fragmented packets. First (starting) fragment does not count. If connection tracking is enabled there will be no fragments as system automatically assembles every packet
- `hotspot` (String) Matches packets received from HotSpot clients against various HotSpot matchers.
- `hw_offload` (Boolean) Connection offloading for Fasttrack.
- `icmp_options` (String) Matches ICMP type: code fields.
- `in_bridge_port` (String) Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `in_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as in-bridge-port.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `ingress_priority` (Number) Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `ipsec_policy` (String) Matches the policy used by IPsec. Value is written in the following format: direction, policy.
- `ipv4_options` (String) Matches IPv4 header options.
- `jump_target` (String) Name of the target chain to jump to. Applicable only if action=jump.
- `layer7_protocol` (String) Layer7 filter name.
- `limit` (String) Matches packets up to a limited rate (packet rate or bit rate). A rule using this matcher will match until this limit is reached. Parameters are written in the following format: rate[/time],burst:mode.
- `log` (Boolean) Add a message to the system log.
- `log_prefix` (String) Adds specified text at the beginning of every log message. Applicable if action=log or log=yes configured.
- `nth` (String) Matches every nth packet: nth=2,1 rule will match every first packet of 2, hence, 50% of all the traffic that is matched by the rule
- `out_bridge_port` (String) Actual interface the packet is leaving the router if the outgoing interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `out_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as out-bridge-port.
- `out_interface` (String) Interface the packet is leaving the router.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `packet_mark` (String) Matches packets marked via mangle facility with particular packet mark. If no-mark is set, the rule will match any unmarked packet.
- `packet_size` (String) Matches packets of specified size or size range in bytes.
- `per_connection_classifier` (String) PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `port` (String) Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if protocol is TCP or UDP
- `priority` (Number) Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority that has been set using the set-priority action.
- `protocol` (String) Matches particular IP protocol specified by protocol name or number.
- `psd` (String) Attempts to detect TCP and UDP scans. Parameters are in the following format WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight.
- `random` (Number) Matches packets randomly with a given probability.
- `reject_with` (String) Specifies ICMP error to be sent back if the packet is rejected. Applicable if action=reject.
- `routing_mark` (String) Matches packets marked by mangle facility with particular routing mark.
- `routing_table` (String) Matches packets which destination address is resolved in specific a routing table.
- `src_address` (String) Matches packets which source is equal to specified IP or falls into a specified IP range.
- `src_address_list` (String) Matches source address of a packet against user-defined address list.
- `src_address_type` (String) Matches source address type.
- `src_mac_address` (String) Matches source MAC address of the packet.
- `src_port` (String) List of source ports and ranges of source ports. Applicable only if a protocol is TCP or UDP.
- `tcp_flags` (String) Matches specified TCP flags.
- `tcp_mss` (String) Matches TCP MSS value of an IP packet.
- `time` (String) Allows to create a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date.
- `tls_host` (String) Allows matching HTTPS traffic based on TLS SNI hostname.
- `ttl` (String) Matches packets TTL value.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/filter get [print show-ids]]
terraform import routeros_ip_firewall_filter.rule "*0"
```
================================================

File: ip_firewall_mangle.md
================================================
# routeros_ip_firewall_mangle (Resource)
## Example Usage
```terraform
resource "routeros_ip_firewall_mangle" "rule" {
  action        = "change-mss"
  chain         = "forward"
  out_interface = "pppoe-out"
  protocol      = "tcp"
  tcp_flags     = "syn"
  new_mss       = "1130"
  tcp_mss       = "1301-65535"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) Action to take if a packet is matched by the rule.
- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
### Optional
- `address_list` (String) Name of the address list to be used. Applicable if action is add-dst-to-address-list or add-src-to-address-list.
- `address_list_timeout` (String) Time interval after which the address will be removed from the address list specified by address-list parameter. Used in conjunction with add-dst-to-address-list or add-src-to-address-list actions.
- `comment` (String)
- `connection_bytes` (String) Matches packets only if a given amount of bytes has been transfered through the particular connection.
- `connection_limit` (String) Matches connections per address or address block after given value is reached. Should be used together with connection-state=new and/or with tcp-flags=syn because matcher is very resource intensive.
- `connection_mark` (String) Matches packets marked via mangle facility with particular connection mark. If no-mark is set, rule will match any unmarked connection.
- `connection_nat_state` (String) Can match connections that are srcnatted, dstnatted or both.
- `connection_rate` (String) Connection Rate is a firewall matcher that allow to capture traffic based on present speed of the connection (0..4294967295).
- `connection_state` (String) Interprets the connection tracking analysis data for a particular packet.
- `connection_type` (String) Matches packets from related connections based on information from their connection tracking helpers.
- `content` (String) Match packets that contain specified text.
- `disabled` (Boolean)
- `dscp` (Number) Matches DSCP IP header field.
- `dst_address` (String) Matches packets which destination is equal to specified IP or falls into specified IP range.
- `dst_address_list` (String) Matches destination address of a packet against user-defined address list.
- `dst_address_type` (String) Matches destination address type.
- `dst_limit` (String) Matches packets until a given rate is exceeded.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `fragment` (Boolean) Matches fragmented packets. First (starting) fragment does not count. If connection tracking is enabled there will be no fragments as system automatically assembles every packet
- `hotspot` (String) Matches packets received from HotSpot clients against various HotSpot matchers.
- `icmp_options` (String) Matches ICMP type: code fields.
- `in_bridge_port` (String) Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `in_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as in-bridge-port.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `ingress_priority` (Number) Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `ipsec_policy` (String) Matches the policy used by IPsec. Value is written in the following format: direction, policy.
- `ipv4_options` (String) Matches IPv4 header options.
- `jump_target` (String) Name of the target chain to jump to. Applicable only if action=jump.
- `layer7_protocol` (String) Layer7 filter name.
- `limit` (String) Matches packets up to a limited rate (packet rate or bit rate). A rule using this matcher will match until this limit is reached. Parameters are written in the following format: rate[/time],burst:mode.
- `log` (Boolean) Add a message to the system log.
- `log_prefix` (String) Adds specified text at the beginning of every log message. Applicable if action=log or log=yes configured.
- `new_connection_mark` (String) Sets a new connection-mark value.
- `new_dscp` (Number) Sets a new DSCP value for a packet.
- `new_mss` (String) Sets a new MSS for a packet.  
	> clamp-to-pmtu feature sets (DF) bit in the IP header to dynamically discover the PMTU of a path.  
	> Host sends all datagrams on that path with the DF bit set until receives ICMP.  
	> Destination Unreachable messages with a code meaning "fragmentation needed and DF set".    
	> Upon receipt of such a message, the source host reduces its assumed PMTU for the path.
- `new_packet_mark` (String) Sets a new packet-mark value.
- `new_priority` (String) Sets a new priority for a packet. This can be the VLAN, WMM, DSCP or MPLS EXP priority. This property can also be used to set an internal priority.
- `new_routing_mark` (String) Sets a new routing-mark value.
- `new_ttl` (String) Sets a new TTL for a packet.
- `nth` (String) Matches every nth packet: nth=2,1 rule will match every first packet of 2, hence, 50% of all the traffic that is matched by the rule
- `out_bridge_port` (String) Actual interface the packet is leaving the router if the outgoing interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `out_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as out-bridge-port.
- `out_interface` (String) Interface the packet is leaving the router.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `packet_mark` (String) Matches packets marked via mangle facility with particular packet mark. If no-mark is set, the rule will match any unmarked packet.
- `packet_size` (String) Matches packets of specified size or size range in bytes.
- `passthrough` (Boolean) Whether to let the packet to pass further (like action passthrough) into the firewall or not (property only valid some actions).
- `per_connection_classifier` (String) PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `port` (String) Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if protocol is TCP or UDP
- `protocol` (String) Matches particular IP protocol specified by protocol name or number.
- `psd` (String) Attempts to detect TCP and UDP scans. Parameters are in the following format WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight.
- `random` (Number) Matches packets randomly with a given probability.
- `route_dst` (String) Matches packets with a specific gateway.
- `routing_mark` (String) Matches packets marked by mangle facility with particular routing mark.
- `src_address` (String) Matches packets which source is equal to specified IP or falls into a specified IP range.
- `src_address_list` (String) Matches source address of a packet against user-defined address list.
- `src_address_type` (String) Matches source address type.
- `src_mac_address` (String) Matches source MAC address of the packet.
- `src_port` (String) List of source ports and ranges of source ports. Applicable only if a protocol is TCP or UDP.
- `tcp_flags` (String) Matches specified TCP flags.
- `tcp_mss` (String) Matches TCP MSS value of an IP packet.
- `time` (String) Allows to create a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date.
- `tls_host` (String) Allows matching HTTPS traffic based on TLS SNI hostname.
- `ttl` (String) Matches packets TTL value.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/mangle get [print show-ids]]
terraform import routeros_ip_firewall_mangle.rule "*0"
```
================================================

File: ip_firewall_nat.md
================================================
# routeros_ip_firewall_nat (Resource)
## Example Usage
```terraform
resource "routeros_ip_firewall_nat" "rule" {
  action        = "masquerade"
  chain         = "srcnat"
  out_interface = "ether16"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) Action to take if a packet is matched by the rule
- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
### Optional
- `address_list` (String) Name of the address list to be used. Applicable if action is add-dst-to-address-list or add-src-to-address-list.
- `address_list_timeout` (String) Time interval after which the address will be removed from the address list specified by address-list parameter. Used in conjunction with add-dst-to-address-list or add-src-to-address-list actions.
- `comment` (String)
- `connection_bytes` (String) Matches packets only if a given amount of bytes has been transfered through the particular connection.
- `connection_limit` (String) Matches connections per address or address block after given value is reached. Should be used together with connection-state=new and/or with tcp-flags=syn because matcher is very resource intensive.
- `connection_mark` (String) Matches packets marked via mangle facility with particular connection mark. If no-mark is set, rule will match any unmarked connection.
- `connection_rate` (String) Connection Rate is a firewall matcher that allow to capture traffic based on present speed of the connection (0..4294967295).
- `connection_type` (String) Matches packets from related connections based on information from their connection tracking helpers.
- `content` (String) Match packets that contain specified text.
- `disabled` (Boolean)
- `dscp` (Number) Matches DSCP IP header field.
- `dst_address` (String) Matches packets which destination is equal to specified IP or falls into specified IP range.
- `dst_address_list` (String) Matches destination address of a packet against user-defined address list.
- `dst_address_type` (String) Matches destination address type.
- `dst_limit` (String) Matches packets until a given rate is exceeded.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `fragment` (Boolean) Matches fragmented packets. First (starting) fragment does not count. If connection tracking is enabled there will be no fragments as system automatically assembles every packet
- `hotspot` (String) Matches packets received from HotSpot clients against various HotSpot matchers.
- `icmp_options` (String) Matches ICMP type: code fields.
- `in_bridge_port` (String) Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `in_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as in-bridge-port.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `ingress_priority` (Number) Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `ipsec_policy` (String) Matches the policy used by IPsec. Value is written in the following format: direction, policy.
- `ipv4_options` (String) Matches IPv4 header options.
- `jump_target` (String) Name of the target chain to jump to. Applicable only if action=jump.
- `layer7_protocol` (String) Layer7 filter name.
- `limit` (String) Matches packets up to a limited rate (packet rate or bit rate). A rule using this matcher will match until this limit is reached. Parameters are written in the following format: rate[/time],burst:mode.
- `log` (Boolean) Add a message to the system log.
- `log_prefix` (String) Adds specified text at the beginning of every log message. Applicable if action=log or log=yes configured.
- `nth` (String) Matches every nth packet: nth=2,1 rule will match every first packet of 2, hence, 50% of all the traffic that is matched by the rule
- `out_bridge_port` (String) Actual interface the packet is leaving the router if the outgoing interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `out_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as out-bridge-port.
- `out_interface` (String) Interface the packet is leaving the router.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `packet_mark` (String) Matches packets marked via mangle facility with particular packet mark. If no-mark is set, the rule will match any unmarked packet.
- `packet_size` (String) Matches packets of specified size or size range in bytes.
- `per_connection_classifier` (String) PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `port` (String) Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if protocol is TCP or UDP
- `priority` (Number) Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority that has been set using the set-priority action.
- `protocol` (String) Matches particular IP protocol specified by protocol name or number.
- `psd` (String) Attempts to detect TCP and UDP scans. Parameters are in the following format WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight.
- `random` (Number) Matches packets randomly with a given probability.
- `randomise_ports` (Boolean) Randomize to which public port connections will be mapped.
- `routing_mark` (String) Matches packets marked by mangle facility with particular routing mark.
- `same_not_by_dst` (Boolean) Specifies whether to take into account or not destination IP address when selecting a new source IP address. Applicable if action=same
- `src_address` (String) Matches packets which source is equal to specified IP or falls into a specified IP range.
- `src_address_list` (String) Matches source address of a packet against user-defined address list.
- `src_address_type` (String) Matches source address type.
- `src_mac_address` (String) Matches source MAC address of the packet.
- `src_port` (String) List of source ports and ranges of source ports. Applicable only if a protocol is TCP or UDP.
- `tcp_mss` (String) Matches TCP MSS value of an IP packet.
- `time` (String) Allows to create a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date.
- `to_addresses` (String) Replace original address with specified one. Applicable if action is dst-nat, netmap, same, src-nat.
- `to_ports` (String) Replace the original port with the specified one. Applicable if action is dst-nat, redirect, masquerade, netmap, same, src-nat.
- `ttl` (String) Matches packets TTL value.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/nat get [print show-ids]]
terraform import routeros_ip_firewall_nat.rule "*0"
```
================================================

File: ip_firewall_raw.md
================================================
# routeros_ip_firewall_raw (Resource)
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) Action to take if a packet is matched by the rule
- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
### Optional
- `address_list` (String) Name of the address list used in 'add-dst-to-address-list' and 'add-src-to-address-list' actions.
- `address_list_timeout` (String) Time interval after which the address will be removed from the address list specified by address-list parameter. Used in conjunction with add-dst-to-address-list or add-src-to-address-list actions.
- `comment` (String)
- `content` (String) Match packets that contain specified text.
- `disabled` (Boolean)
- `dscp` (Number) Matches DSCP IP header field.
- `dst_address` (String) Matches packets which destination is equal to specified IP or falls into specified IP range.
- `dst_address_list` (String) Matches destination address of a packet against user-defined address list.
- `dst_address_type` (String) Matches destination address type.
- `dst_limit` (String) Matches packets until a given rate is exceeded.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `fragment` (Boolean) Matches fragmented packets. First (starting) fragment does not count. If connection tracking is enabled there will be no fragments as system automatically assembles every packet
- `hotspot` (String) Matches packets received from HotSpot clients against various HotSpot matchers.
- `icmp_options` (String) Matches ICMP type: code fields.
- `in_bridge_port` (String) Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `in_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as in-bridge-port.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `ingress_priority` (Number) Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `ipsec_policy` (String) Matches the policy used by IPsec. Value is written in the following format: direction, policy.
- `ipv4_options` (String) Matches IPv4 header options.
- `jump_target` (String) Name of the target chain to jump to. Applicable only if action=jump.
- `limit` (String) Matches packets up to a limited rate (packet rate or bit rate). A rule using this matcher will match until this limit is reached. Parameters are written in the following format: rate[/time],burst:mode.
- `log` (Boolean) Add a message to the system log.
- `log_prefix` (String) Adds specified text at the beginning of every log message. Applicable if action=log or log=yes configured.
- `nth` (String) Matches every nth packet: nth=2,1 rule will match every first packet of 2, hence, 50% of all the traffic that is matched by the rule
- `out_bridge_port` (String) Actual interface the packet is leaving the router if the outgoing interface is a bridge. Works only if use-ip-firewall is enabled in bridge settings.
- `out_bridge_port_list` (String) Set of interfaces defined in interface list. Works the same as out-bridge-port.
- `out_interface` (String) Interface the packet is leaving the router.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `packet_mark` (String) Matches packets marked via mangle facility with particular packet mark. If no-mark is set, the rule will match any unmarked packet.
- `packet_size` (String) Matches packets of specified size or size range in bytes.
- `per_connection_classifier` (String) PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `port` (String) Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if protocol is TCP or UDP
- `priority` (Number) Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority that has been set using the set-priority action.
- `protocol` (String) Matches particular IP protocol specified by protocol name or number.
- `psd` (String) Attempts to detect TCP and UDP scans. Parameters are in the following format WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight.
- `random` (Number) Matches packets randomly with a given probability.
- `src_address` (String) Matches packets which source is equal to specified IP or falls into a specified IP range.
- `src_address_list` (String) Matches source address of a packet against user-defined address list.
- `src_address_type` (String) Matches source address type.
- `src_mac_address` (String) Matches source MAC address of the packet.
- `src_port` (String) List of source ports and ranges of source ports. Applicable only if a protocol is TCP or UDP.
- `tcp_flags` (String) Matches specified TCP flags.
- `tcp_mss` (String) Matches TCP MSS value of an IP packet.
- `time` (String) Allows to create a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date.
- `tls_host` (String) Allows matching HTTPS traffic based on TLS SNI hostname.
- `ttl` (String) Matches packets TTL value.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
================================================

File: ip_neighbor_discovery_settings.md
================================================
# routeros_ip_neighbor_discovery_settings (Resource)
## Example Usage
```terraform
resource "routeros_ip_neighbor_discovery_settings" "test" {
  discover_interface_list  = "static"
  lldp_med_net_policy_vlan = "1"
  mode                     = "tx-and-rx"
  protocol                 = []
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `discover_interface_list` (String) Interface list on which members the discovery protocol will run on.
- `lldp_mac_phy_config` (Boolean) Whether to send MAC/PHY Configuration/Status TLV in LLDP, which indicates the interface capabilities, current setting of the duplex status, bit rate, and auto-negotiation. Only applies to the Ethernet interfaces. While TLV is optional in LLDP, it is mandatory when sending LLDP-MED, meaning this TLV will be included when necessary even though the property is configured as disabled.
- `lldp_max_frame_size` (Boolean) Whether to send Maximum Frame Size TLV in LLDP, which indicates the maximum frame size capability of the interface in bytes (`l2mtu + 18`). Only applies to the Ethernet interfaces.
- `lldp_med_net_policy_vlan` (String) Advertised VLAN ID for LLDP-MED Network Policy TLV. This allows assigning a VLAN ID for 
			LLDP-MED capable devices, such as VoIP phones. The TLV will only be added to interfaces where LLDP-MED 
			capable devices are discovered. Other TLV values are predefined and cannot be changed:
			- Application Type - Voice
			- VLAN Type - Tagged
			- L2 Priority - 0
			- DSCP Priority - 0
		When used together with the bridge interface, the (R/M)STP protocol should be enabled with protocol-mode setting. 
		Additionally, other neighbor discovery protocols (e.g. CDP) should be excluded using protocol setting to 
		avoid LLDP-MED misconfiguration.
- `lldp_poe_power` (Boolean) Two specific TLVs facilitate Power over Ethernet (PoE) management between Power Sourcing Equipment (PSE) and Powered Devices (PD).
- `mode` (String) Selects the neighbor discovery packet sending and receiving mode. The setting is available since RouterOS version 7.7.
- `protocol` (Set of String) List of used discovery protocols.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_neighbor_discovery_settings.test .
```
================================================

File: ip_pool.md
================================================
# routeros_ip_pool (Resource)
## Example Usage
```terraform
resource "routeros_ip_pool" "pool" {
  name   = "my_ip_pool"
  ranges = ["10.0.0.100-10.0.0.200"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
- `ranges` (List of String) IP address list of non-overlapping IP address ranges in form of: ["from1-to1", "from2-to2", ..., "fromN-toN"]. For example, ["10.0.0.1-10.0.0.27", "10.0.0.32-10.0.0.47"]
### Optional
- `comment` (String)
- `next_pool` (String) When address is acquired from pool that has no free addresses, and next-pool property is set to another pool, then next IP address will be acquired from next-pool.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/pool get [print show-ids]]
terraform import routeros_ip_pool.pool "*1"
```
================================================

File: ip_route.md
================================================
# routeros_ip_route (Resource)
## Example Usage
```terraform
resource "routeros_ip_route" "a_route" {
  dst_address = "0.0.0.0/0"
  gateway     = "10.0.0.1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `gateway` (String) Array of IP addresses or interface names. Specifies which host or interface packets should be sent to (IP | interface | IP%interface | IP@table[, IP | string, [..]]).
### Optional
- `blackhole` (Boolean) It's a blackhole route. If you need to cancel route marking, then simply delete the parameter from the configuration of the TF. The value of the parameter (true or false) has no effect on the MT processing logic.
- `check_gateway` (String) Currently used check-gateway option.
- `comment` (String)
- `disabled` (Boolean)
- `distance` (Number) Value used in route selection. Routes with smaller distance value are given preference.
- `dst_address` (String) IP prefix of route, specifies destination addresses that this route can be used for.
- `pref_src` (String) Which of the local IP addresses to use for locally originated packets that are sent via this route. Value of this property has no effect on forwarded packets. If value of this property is set to IP address that is not local address of this router then the route will be inactive (in ROS v6, ROS v7 allows IP spoofing).
- `routing_table` (String) Routing table this route belongs to.
- `scope` (Number) Used in nexthop resolution. Route can resolve nexthop only through routes that have scope less than or equal to the target-scope of this route.
- `suppress_hw_offload` (Boolean)
- `target_scope` (Number) Used in nexthop resolution. This is the maximum value of scope for a route through which a nexthop of this route can be resolved.
- `vrf_interface` (String) VRF interface name.
### Read-Only
- `active` (Boolean) A flag indicates whether the route is elected as Active and eligible to be added to the FIB.
- `dhcp` (Boolean) A flag indicates whether the route was added by the DHCP service.
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `ecmp` (Boolean) A flag indicates whether the route is added as an Equal-Cost Multi-Path route in the FIB.
- `hw_offloaded` (Boolean) Indicates whether the route is eligible to be hardware offloaded on supported hardware.
- `id` (String) The ID of this resource.
- `immediate_gw` (String) Shows actual (resolved) gateway and interface that will be used for packet forwarding.
- `inactive` (Boolean)
- `static` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/route get [print show-ids]]
terraform import routeros_ip_route.a_route "*0"
```
================================================

File: ip_service.md
================================================
# routeros_ip_service (Resource)
## Example Usage
```terraform
locals {
  tls_service     = { "api-ssl" = 8729, "www-ssl" = 443 }
  disable_service = { "api" = 8728, "ftp" = 21, "telnet" = 23, "www" = 80 }
  enable_service  = { "ssh" = 22, "winbox" = 8291 }
}
resource "routeros_system_certificate" "tls_cert" {
  name        = "tls-cert"
  common_name = "Mikrotik Router"
  days_valid  = 3650
  key_usage   = ["key-cert-sign", "crl-sign", "digital-signature", "key-agreement", "tls-server"]
  key_size    = "prime256v1"
  sign {
  }
}
# terraform state rm 'routeros_ip_service.tls["www-ssl"]'
# terraform import 'routeros_ip_service.tls["www-ssl"]' www-ssl
resource "routeros_ip_service" "tls" {
  for_each    = local.tls_service
  numbers     = each.key
  port        = each.value
  certificate = routeros_system_certificate.tls_cert.name
  tls_version = "only-1.2"
  disabled    = false
}
resource "routeros_ip_service" "disabled" {
  for_each = local.disable_service
  numbers  = each.key
  port     = each.value
  disabled = true
}
resource "routeros_ip_service" "enabled" {
  for_each = local.enable_service
  numbers  = each.key
  port     = each.value
  disabled = false
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `numbers` (String) The name of the service whose settings will be changed ( api, api-ssl, ftp, ssh, telnet, winbox, www, www-ssl ).
- `port` (Number) The port particular service listens on.
### Optional
- `address` (String) List of IP/IPv6 prefixes from which the service is accessible.
- `certificate` (String) The name of the certificate used by a particular service. Applicable only for services that depend on certificates ( www-ssl, api-ssl ).
- `disabled` (Boolean)
- `tls_version` (String) Specifies which TLS versions to allow by a particular service.
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `name` (String) Service name.
## Import
Import is supported using the following syntax:
```shell
# Import with the name of the ip service in case of the example use www-ssl
terraform import routeros_ip_service.www_ssl www-ssl
```
================================================

File: ip_ssh_server.md
================================================
# routeros_ip_ssh_server (Resource)
## Example Usage
```terraform
resource "routeros_ip_ssh_server" "test" {
  strong_crypto      = true
  forwarding_enabled = "local"
  host_key_size      = 4096
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `allow_none_crypto` (Boolean) Whether to allow connection if cryptographic algorithms are set to none.
- `always_allow_password_login` (Boolean) Whether to allow password login at the same time when public key authorization is configured for a user.
- `forwarding_enabled` (String) Allows to control which SSH forwarding method to allow:
			* no - SSH forwarding is disabled;
			* local - Allow SSH clients to originate connections from the server(router), this setting controls also dynamic forwarding;
			* remote - Allow SSH clients to listen on the server(router) and forward incoming connections;
			* both - Allow both local and remote forwarding methods.
- `host_key_size` (Number) RSA key size when host key is being regenerated.
- `host_key_type` (String) Select host key type.
- `strong_crypto` (Boolean) Use stronger encryption.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_ssh_server.test .
```
================================================

File: ip_upnp.md
================================================
# routeros_ip_upnp (Resource)
*<span style="color:red">If you do not disable the `allow-disable-external-interface`, any user from the local network will be able (without any authentication procedures) to disable the router's external interface.</span>*
## Example Usage
```terraform
resource "routeros_ip_upnp" "test" {
  allow_disable_external_interface = true
  enabled                          = true
  show_dummy_rule                  = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `allow_disable_external_interface` (Boolean) Whether or not should the users are allowed to disable the router's external interface. This functionality (for users to be able to turn the router's external interface off without any authentication procedure) is required by the standard, but as it is sometimes not expected or unwanted in UPnP deployments which the standard was not designed for (it was designed mostly for home users to establish their own local networks), you can disable this behavior
- `enabled` (Boolean) Enable UPnP service.
- `show_dummy_rule` (Boolean) nable a workaround for some broken implementations, which are handling the absence of UPnP rules incorrectly (for example, popping up error messages). This option will instruct the server to install a dummy (meaningless) UPnP rule that can be observed by the clients, which refuse to work correctly otherwise
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ip_upnp.test .
```
================================================

File: ip_upnp_interfaces.md
================================================
# routeros_ip_upnp_interfaces (Resource)
## Example Usage
```terraform
resource "routeros_ip_upnp_interfaces" "test" {
  interface          = "ether1"
  type               = "external"
  forced_external_ip = "0.0.0.0"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interface` (String) Interface name on which uPnP will be running.
### Optional
- `disabled` (Boolean)
- `forced_ip` (String) Allow specifying what public IP to use if the external interface has more than one IP available.
- `type` (String) UPnP interface type:
			external - the interface a global IP address is assigned to
			internal - router's local interface the clients are connected to
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/upnp/interfaces get [print show-ids]]
terraform import routeros_ip_upnp_interfaces.test '*1'
```
================================================

File: ip_vrf.md
================================================
# routeros_ip_vrf (Resource)
## Example Usage
```terraform
resource "routeros_interface_veth" "veth1" {
  name = "veth1"
}
resource "routeros_interface_veth" "veth2" {
  name = "veth2"
}
resource "routeros_ip_vrf" "test_vrf_a" {
  disabled   = true
  name       = "vrf_1"
  comment    = "Custom routing"
  interfaces = ["veth1", "veth2"]
  depends_on = [routeros_interface_veth.veth1, routeros_interface_veth.veth2]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `interfaces` (Set of String) At least one interface must be added to the VRF.
- `name` (String) Unique name of the VRF.
### Optional
- `comment` (String)
- `disabled` (Boolean)
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/vrf get [print show-ids]]
terraform import routeros_ip_vrf.test_vrf_a "*0"
# or
terraform import routeros_ip_vrf.test_vrf_a "vrf_1"
# or
terraform import routeros_ip_vrf.test_vrf_a `"comment=Custom routing"`
```
================================================

File: move_items.md
================================================
# routeros_move_items (Resource)
## Example Usage
```terraform
variable "rule" {
  type = list(object({
    chain              = string
    action             = string
    connection_state   = optional(string)
    in_interface_list  = optional(string, "all")
    out_interface_list = optional(string)
    src_address        = optional(string, "0.0.0.0/0")
    dst_address        = optional(string)
    src_port           = optional(string)
    dst_port           = optional(string)
    protocol           = optional(string)
    comment            = optional(string, "(terraform-defined)")
    log                = optional(bool, false)
    disabled           = optional(bool, true)
  }))
  default = [
    { chain = "input", action = "accept", comment = "00" },
    { chain = "input", action = "accept", comment = "01" },
    { chain = "input", action = "accept", comment = "02" },
    { chain = "input", action = "accept", comment = "03" },
    { chain = "input", action = "accept", comment = "04" },
    { chain = "input", action = "accept", comment = "05" },
    { chain = "input", action = "accept", comment = "06" },
    { chain = "input", action = "accept", comment = "07" },
    { chain = "input", action = "accept", comment = "08" },
    { chain = "input", action = "accept", comment = "09" },
    { chain = "input", action = "accept", comment = "10" },
    { chain = "input", action = "accept", comment = "11" },
    { chain = "input", action = "accept", comment = "12" },
    { chain = "input", action = "accept", comment = "13" },
    { chain = "input", action = "accept", comment = "14" },
    { chain = "input", action = "accept", comment = "15" },
    { chain = "input", action = "accept", comment = "16" },
    { chain = "input", action = "accept", comment = "17" },
    { chain = "input", action = "accept", comment = "18" },
    { chain = "input", action = "accept", comment = "19" },
    { chain = "input", action = "accept", comment = "20" },
    { chain = "input", action = "accept", comment = "21" },
    { chain = "input", action = "accept", comment = "22" },
    { chain = "input", action = "accept", comment = "23" },
    { chain = "input", action = "accept", comment = "24" },
    { chain = "input", action = "accept", comment = "25" },
    { chain = "input", action = "accept", comment = "26" },
    { chain = "input", action = "accept", comment = "27" },
    { chain = "input", action = "accept", comment = "28" },
    { chain = "input", action = "accept", comment = "29" },
    { chain = "input", action = "accept", comment = "30" },
    { chain = "input", action = "accept", comment = "31" },
  ]
}
locals {
  # https://discuss.hashicorp.com/t/does-map-sort-keys/12056/2
  # Map keys are always iterated in lexicographical order!
  rule_map = { for idx, rule in var.rule : format("%03d", idx) => rule }
}
resource "routeros_ip_firewall_filter" "rules" {
  for_each          = local.rule_map
  chain             = each.value.chain
  action            = each.value.action
  comment           = each.value.comment
  log               = each.value.log
  disabled          = each.value.disabled
  connection_state  = each.value.connection_state
  in_interface_list = each.value.in_interface_list
  src_address       = each.value.src_address
  dst_port          = each.value.dst_port
  protocol          = each.value.protocol
}
resource "routeros_move_items" "fw_rules" {
  #  resource_name = "routeros_ip_firewall_filter"
  resource_path = "/ip/firewall/filter"
  sequence      = [for i, _ in local.rule_map : routeros_ip_firewall_filter.rules[i].id]
  depends_on    = [routeros_ip_firewall_filter.rules]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `sequence` (List of String) List identifiers in the required sequence. To locate the ```sequence``` before an existing rule, add its ```id``` to the last element of the ```sequence```.
### Optional
- `resource_name` (String) Resource name in the notation ```routeros_ip_firewall_filter```.
- `resource_path` (String) URL path of the resource in the notation ```/ip/firewall/filter```.
### Read-Only
- `id` (String) The ID of this resource.
================================================

File: ovpn_server.md
================================================
# routeros_ovpn_server (Resource)
##### *<span style="color:red">This resource requires a minimum version of RouterOS 7.8!</span>*
## Example Usage
```terraform
resource "routeros_ip_pool" "ovpn-pool" {
  name   = "ovpn-pool"
  ranges = ["192.168.77.2-192.168.77.254"]
}
resource "routeros_system_certificate" "ovpn_ca" {
  name        = "OpenVPN-Root-CA"
  common_name = "OpenVPN Root CA"
  key_size    = "prime256v1"
  key_usage   = ["key-cert-sign", "crl-sign"]
  trusted     = true
  sign {
  }
}
resource "routeros_system_certificate" "ovpn_server_crt" {
  name        = "OpenVPN-Server-Certificate"
  common_name = "Mikrotik OpenVPN"
  key_size    = "prime256v1"
  key_usage   = ["digital-signature", "key-encipherment", "tls-server"]
  sign {
    ca = routeros_system_certificate.ovpn_ca.name
  }
}
resource "routeros_ppp_profile" "test" {
  name           = "ovpn"
  local_address  = "192.168.77.1"
  remote_address = "ovpn-pool"
  use_upnp       = "no"
}
resource "routeros_ppp_secret" "test" {
  name     = "user-test"
  password = "123"
  profile  = routeros_ppp_profile.test.name
}
resource "routeros_ovpn_server" "server" {
  enabled         = true
  certificate     = routeros_system_certificate.ovpn_server_crt.name
  auth            = ["sha256", "sha512"]
  tls_version     = "only-1.2"
  default_profile = routeros_ppp_profile.test.name
}
# The resource should be created only after the OpenVPN server is enabled!
resource "routeros_interface_ovpn_server" "user1" {
  name       = "ovpn-in1"
  user       = "user1"
  depends_on = [routeros_ovpn_server.server]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `auth` (Set of String) Authentication methods that the server will accept.
- `certificate` (String) Name of the certificate that the OVPN server will use.
- `cipher` (Set of String) Allowed ciphers.
- `default_profile` (String) Default profile to use.
- `enable_tun_ipv6` (Boolean) Specifies if IPv6 IP tunneling mode should be possible with this OVPN server.
- `enabled` (Boolean) Defines whether the OVPN server is enabled or not.
- `ipv6_prefix_len` (Number) Length of IPv6 prefix for IPv6 address which will be used when generating OVPN interface on the server side.
- `keepalive_timeout` (String) Defines  the time period (in seconds) after which the router is starting to send  keepalive packets every second. If no traffic and no keepalive  responses have come for that period of time (i.e. 2 *  keepalive-timeout), not responding client is proclaimed disconnected
- `mac_address` (String) Automatically generated MAC address of the server.
- `max_mtu` (Number) Maximum Transmission Unit. Max packet size that the OVPN interface will be able to send without packet fragmentation.
- `mode` (String) Layer3 or layer2 tunnel mode (alternatively tun, tap)
- `netmask` (Number) Subnet mask to be applied to the client.
- `port` (Number) Port to run the server on.
- `protocol` (String) indicates the protocol to use when connecting with the remote endpoint.
- `push_routes` (Set of String) Push routes to the VPN client (available since RouterOS 7.14).
- `redirect_gateway` (Set of String) Specifies what kind of routes the OVPN client must add to the routing table. def1 – Use this flag to override the default gateway by using 0.0.0.0/1 and  128.0.0.0/1 rather than 0.0.0.0/0. This has the benefit of overriding  but not wiping out the original default gateway. disabled - Do not send redirect-gateway flags to the OVPN client. ipv6 - Redirect IPv6 routing into the tunnel on the client side. This works  similarly to the def1 flag, that is, more specific IPv6 routes are added  (2000::/4 and 3000::/4), covering the whole IPv6 unicast space.
- `reneg_sec` (Number) Renegotiate data channel key after n seconds (default=3600).
- `require_client_certificate` (Boolean) If set to yes, then the server checks whether the client's certificate belongs to the same certificate chain.
- `tls_version` (String) Specifies which TLS versions to allow.
- `tun_server_ipv6` (String) IPv6 prefix address which will be used when generating the OVPN interface on the server side.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_openvpn_server.server .
```
================================================

File: ppp_aaa.md
================================================
# routeros_ppp_aaa (Resource)
## Example Usage
```terraform
resource "routeros_ppp_aaa" "settings" {
  use_radius = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `accounting` (Boolean) An option that enables accounting for users.
- `enable_ipv6_accounting` (Boolean) An option that enables IPv6 separate accounting.
- `interim_update` (String) Interval between scheduled RADIUS Interim-Update messages.
- `use_circuit_id_in_nas_port_id` (Boolean)
- `use_radius` (Boolean) An option whether to use RADIUS server.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_ppp_aaa.settings .
```
================================================

File: ppp_profile.md
================================================
# routeros_ppp_profile (Resource)
## Example Usage
```terraform
resource "routeros_ppp_profile" "test" {
  name           = "ovpn"
  local_address  = "192.168.77.1"
  remote_address = "ovpn-pool"
  use_upnp       = "no"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) PPP profile name.
### Optional
- `address_list` (String) Address list name to which ppp assigned (on server) or received (on client) address will be added.
- `bridge` (String) Name of the bridge interface to which ppp interface will be added as a slave port. Both  tunnel endpoints (server and client) must be in bridge in order to make  this work, see more details on the BCP bridging manual.
- `bridge_horizon` (Number) Used  split-horizon value for the dynamically created bridge port. Can be  used to prevent bridging loops and isolate traffic. Set the same value  for a group of ports, to prevent them from sending data to ports with  the same horizon value.
- `bridge_learning` (String) Changes MAC learning behavior on the dynamically created bridge port: yes - enables MAC learning no - disables MAC learning default - derive this value from the interface default profile; same as yes if this is the interface default profile.
- `bridge_path_cost` (Number) Used  path cost for the dynamically created bridge port, used by STP/RSTP to  determine the best path, used by MSTP to determine the best path between  regions. This property has no effect when a bridge protocol-mode is set to none.
- `bridge_port_priority` (Number) Used  priority for the dynamically created bridge port, used by STP/RSTP to  determine the root port, used by MSTP to determine root port between  regions. This property has no effect when a bridge protocol-mode is set  to none.
- `change_tcp_mss` (String) Modifies connection MSS settings (applies only for IPv4): yes - adjust connection MSS value no - do not adjust connection MSS value default - derive this value from the interface default profile; same as no if this is the interface default profile.
- `comment` (String)
- `dhcpv6_pd_pool` (String) Name of the IPv6 pool which will be used by dynamically created DHCPv6-PD server when client connects. [Read more >>](https://wiki.mikrotik.com/wiki/Manual:IPv6_PD_over_PPP)
- `dns_server` (Set of String) IP address of the DNS server that is supplied to ppp clients.
- `idle_timeout` (String) Specifies  the amount of time after which the link will be terminated if there are  no activity present. Timeout is not set by default.
- `incoming_filter` (String) Firewall  chain name for incoming packets. Specified chain gets control for each  packet coming from the client. The ppp chain should be manually added  and rules with action=jump jump-target=ppp should be added to other  relevant chains in order for this feature to work. For more information  look at the examples section.
- `insert_queue_before` (String) Specify where to place dynamic simple queue entries for static DCHP leases with rate-limit parameter set.
- `interface_list` (String) Interface list name.
- `local_address` (String) Tunnel address or name of the pool from which address is assigned to ppp interface locally.
- `on_down` (String) Execute script on user logging off. See on-up for more details.
- `on_up` (String) Execute script on user login-event. These are available variables that are accessible for the event script: *user *local-address *remote-address *caller-id *called-id *interface.
- `only_one` (String) Defines whether a user is allowed to have more than one ppp session at a time yes - a user is not allowed to have more than one ppp session at a time no - the user is allowed to have more than one ppp session at a time default - derive this value from the interface default profile; same as no if this is the interface default profile.
- `outgoing_filter` (String) Firewall  chain name for outgoing packets. The specified chain gets control for  each packet going to the client. The PPP chain should be manually added  and rules with action=jump jump-target=ppp should be added to other  relevant chains in order for this feature to work. For more information  look at the Examples section.
- `parent_queue` (String) Name of parent simple queue.
- `queue_type` (String) Queue types.
- `rate_limit` (String) Rate limitation in form of rx-rate[/tx-rate]  [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold]  [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]] from the point of view of the router (so 'rx' is client upload, and  'tx' is client download). All rates are measured in bits per second,  unless followed by optional 'k' suffix (kilobits per second) or 'M'  suffix (megabits per second). If tx-rate is not specified, rx-rate  serves as tx-rate too. The same applies for tx-burst-rate,  tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and  tx-burst-threshold are not specified (but burst-rate is specified),  rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time  and tx-burst-time are not specified, 1s is used as default. Priority  takes values 1..8, where 1 implies the highest priority, but 8 - the  lowest. If rx-rate-min and tx-rate-min are not specified rx-rate and  tx-rate values are used. The rx-rate-min and tx-rate-min values can not  exceed rx-rate and tx-rate values.
- `remote_address` (String) Tunnel address or name of the pool from which address is assigned to remote ppp interface.
- `remote_ipv6_prefix_pool` (String) Assign prefix from IPv6 pool to the client and install corresponding IPv6 route.
- `session_timeout` (String) Maximum time the connection can stay up. By default no time limit is set.
- `use_compression` (String) Specifies whether to use data compression or not. yes - enable data compression no - disable data compression default - derive this value from the interface default profile; same as no if this is the interface default profile This setting does not affect OVPN tunnels.
- `use_encryption` (String) Specifies whether to use data encryption or not. yes - enable data encryption no - disable data encryption default - derive this value from the interface default profile; same as no if this is the interface default profile require - explicitly requires encryption This setting does not work on OVPN and SSTP tunnels.
- `use_ipv6` (String) Specifies whether to allow IPv6. By default is enabled if IPv6 package is installed. yes - enable IPv6 support no - disable IPv6 support default - derive this value from the interface default profile; same as no if this is the interface default profile require - explicitly requires IPv6 support.
- `use_mpls` (String) Specifies whether to allow MPLS over PPP. yes - enable MPLS support no - disable MPLS support default - derive this value from the interface default profile; same as no if this is the interface default profile require - explicitly requires MPLS support
- `use_upnp` (String) Specifies whether to allow UPnP.
- `wins_server` (Set of String) IP address of the WINS server to supply to Windows clients.
### Read-Only
- `default` (String) Default profile sign.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ppp/profile get [print show-ids]]
terraform import routeros_ppp_profile.test *6
```
================================================

File: ppp_secret.md
================================================
# routeros_ppp_secret (Resource)
## Example Usage
```terraform
resource "routeros_ppp_secret" "test" {
  name     = "user-test"
  password = "123"
  profile  = "default"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name used for authentication.
### Optional
- `caller_id` (String) For PPTP and L2TP it is the IP address a client must connect from. For PPPoE it is the MAC address (written in CAPITAL letters) a client must  connect from. For ISDN it is the caller's number (that may or may not be  provided by the operator) the client may dial-in from.
- `comment` (String)
- `disabled` (Boolean)
- `ipv6_routes` (Set of String) IPv6 routes.
- `limit_bytes_in` (Number) Maximal amount of bytes for a session that client can upload.
- `limit_bytes_out` (Number) Maximal amount of bytes for a session that client can download.
- `local_address` (String) IP address that will be set locally on ppp interface.
- `password` (String, Sensitive) Password used for authentication.
- `profile` (String) Which user profile to use.
- `remote_address` (String) IP address that will be assigned to remote ppp interface.
- `remote_ipv6_prefix` (String) IPv6 prefix assigned to ppp client. Prefix is added to ND prefix list enabling stateless address auto-configuration on ppp interface.Available starting from v5.0.
- `routes` (Set of String) Routes  that appear on the server when the client is connected. The route  format is: dst-address gateway metric (for example, 10.1.0.0/ 24  10.0.0.1 1). Other syntax is not acceptable since it can be represented  in incorrect way. Several routes may be specified separated with commas.  This parameter will be ignored for OpenVPN.
- `service` (String) Specifies the services that particular user will be able to use.
### Read-Only
- `id` (String) The ID of this resource.
- `last_caller_id` (String)
- `last_disconnect_reason` (String)
- `last_logged_out` (String)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ppp/secret get [print show-ids]]
terraform import routeros_ppp_secret.test *6
```
================================================

File: radius.md
================================================
# routeros_radius (Resource)
## Example Usage
```terraform
resource "routeros_radius" "user_manager" {
  address = "127.0.0.1"
  service = ["ppp", "login"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) IPv4 or IPv6 address of RADIUS server.
### Optional
- `accounting_backup` (Boolean) An option whether the configuration is for the backup RADIUS server.
- `accounting_port` (Number) RADIUS server port used for accounting.
- `authentication_port` (Number) RADIUS server port used for authentication.
- `called_id` (String) RADIUS calling station identifier.
- `certificate` (String) Certificate to use for communication with RADIUS Server with RadSec enabled.
- `comment` (String)
- `disabled` (Boolean)
- `domain` (String) Microsoft Windows domain of client passed to RADIUS servers that require domain validation.
- `protocol` (String) An option specifies the protocol to use when communicating with the RADIUS Server.
- `realm` (String) Explicitly stated realm (user domain), so the users do not have to provide proper ISP domain name in the user name.
- `require_message_auth` (String) An option whether to require `Message-Authenticator` in received Access-Accept/Challenge/Reject messages.
- `secret` (String, Sensitive) The shared secret to access the RADIUS server.
- `service` (Set of String) A set of router services that will use the RADIUS server. Possible values: `hotspot`, `login`, `ppp`, `wireless`, `dhcp`, `ipsec`, `dot1x`.
- `src_address` (String) Source IPv4/IPv6 address of the packets sent to the RADIUS server.
- `timeout` (String) A timeout, after which the request should be resent.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/radius get [print show-ids]]
terraform import routeros_radius.user_manager *1
```
================================================

File: radius_incoming.md
================================================
# routeros_radius_incoming (Resource)
## Example Usage
```terraform
resource "routeros_radius_incoming" "settings" {
  accept = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `accept` (Boolean) An option whether to accept the unsolicited messages.
- `port` (Number) The port number to listen for the requests on.
- `vrf` (String) VRF on which service is listening for incoming connections. This option is available in RouterOS starting from version 7.4.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_radius_incoming.settings .
```
================================================

File: routing_bgp_connection.md
================================================
# routeros_routing_bgp_connection (Resource)
> [!WARNING] Using this resource you may happen unexpected behavior, for example, some of the attributes may not be removable after adding them to the TF configuration. Please report this to GitHub and it may be possible to fix it. Use the resource at your own risk as it is!
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `as` (String) 32-bit BGP autonomous system number. Value can be entered in AS-Plain and AS-Dot formats. The parameter is also used to set up the BGP confederation, in the following format: confederation_as/as . For example, if your AS is 34 and your confederation AS is 43, then as configuration should be as =43/34.
- `name` (String) Name of the BGP connection.
### Optional
- `add_path_out` (String)
- `address_families` (String) List of address families about which this peer will exchange routing information. The remote peer must support (they usually do) BGP capabilities optional parameter to negotiate any other families than IP.
- `cisco_vpls_nlri_len_fmt` (String) VPLS NLRI length format type. Used for compatibility with Cisco VPLS.
- `cluster_id` (String) In case this instance is a route reflector: the cluster ID of the router reflector cluster to this instance belongs. This attribute helps to recognize routing updates that come from another route reflector in this cluster and avoid routing information looping. Note that normally there is only one route reflector in a cluster; in this case, 'cluster-id' does not need to be configured and BGP router ID is used instead.
- `comment` (String)
- `connect` (Boolean) Whether to allow the router to initiate the connection.
- `disabled` (Boolean)
- `hold_time` (String) Specifies the BGP Hold Time value to use when negotiating with peers. According to the BGP specification, if the router does not receive successive KEEPALIVE and/or UPDATE and/or NOTIFICATION messages within the period specified in the Hold Time field of the OPEN message, then the BGP connection to the peer will be closed. The minimal hold-time value of both peers will be actually used (note that the special value 0 or 'infinity' is lower than any other value) infinity - never expire the connection and never send keepalive messages.
- `input` (Block List, Max: 1) A group of parameters associated with BGP input. (see [below for nested schema](#nestedblock--input))
- `keepalive_time` (String) How long to keep the BGP session open after the last received 'keepalive' message.
- `listen` (Boolean) Whether to listen for incoming connections.
- `local` (Block List, Max: 1) A group of parameters associated with BGP input. (see [below for nested schema](#nestedblock--local))
- `multihop` (Boolean) Specifies whether the remote peer is more than one hop away. This option affects outgoing next-hop selection as described in RFC 4271 (for EBGP only, excluding EBGP peers local to the confederation). It also affects: whether to accept connections from peers that are not in the same network (the remote address of the connection is used for this check); whether to accept incoming routes with NEXT_HOP attribute that is not in the same network as the address used to establish the connection; the target-scope of the routes installed from this peer; routes from multi-hop or IBGP peers resolve their next-hops through IGP routes by default.
- `nexthop_choice` (String) Affects the outgoing NEXT_HOP attribute selection. Note that next-hops set in filters always take precedence. Also note that the next-hop is not changed on route reflection, except when it's set in the filter. default - select the next-hop as described in RFC 4271 force-self - always use a local address of the interface that is used to connect to the peer as the next-hop; propagate - try to propagate further the next-hop received; i.e. if the route has BGP NEXT_HOP attribute, then use it as the next-hop, otherwise, fall back to the default case.
- `output` (Block List, Max: 1) A group of parameters associated with BGP output. (see [below for nested schema](#nestedblock--output))
- `remote` (Block List, Max: 1) A group of parameters associated with BGP input. (see [below for nested schema](#nestedblock--remote))
- `router_id` (String) BGP Router ID to be used. Use the ID from the /routing/router-id configuration by specifying the reference name, or set the ID directly by specifying IP. Equal router-ids are also used to group peers into one instance.
- `routing_table` (String) Name of the routing table, to install routes in.
- `save_to` (String) Filename to be used to save BGP protocol-specific packet content (Exported PDU) into pcap file. This method allows much simpler peer-specific packet capturing for debugging purposes. Pcap files in this format can also be loaded to create virtual BGP peers to recreate conditions that happened at the time when packet capture was running.
- `tcp_md5_key` (String, Sensitive) The key used to authenticate the connection with TCP MD5 signature as described in RFC 2385. If not specified, authentication is not used.
- `templates` (Set of String) List of the template names, to inherit parameters from. Useful for dynamic BGP peers.
- `use_bfd` (Boolean) Whether to use the BFD protocol for faster connection state detection.
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
<a id="nestedblock--input"></a>
### Nested Schema for `input`
Optional:
- `accept_communities` (String) A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_ext_communities` (String) A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_large_communities` (String) A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_nlri` (String) Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session restart.
- `accept_unknown` (String) A quick way to filter incoming updates with specific 'unknown' attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `affinity` (String) Configure input multi-core processing. Read more in Routing Protocol Multi-core Support article. alone - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers afi, instance, vrf, remote-as - try to run input/output of new session in process with similar parameters main - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores) input - run output in the same process as input (can be set only for output affinity)
- `allow_as` (Number) Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.
- `filter` (String) Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.
- `ignore_as_path_len` (Boolean) Whether to ignore the AS_PATH attribute in the BGP route selection algorithm
- `limit_process_routes_ipv4` (Number) Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session 'clear' command must be used to reset the flag if the limit is reached.
- `limit_process_routes_ipv6` (Number) Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session 'clear' command must be used to reset the flag if the limit is reached.
<a id="nestedblock--local"></a>
### Nested Schema for `local`
Required:
- `role` (String) BGP role, in most common scenarios it should be set to iBGP or eBGP. More information on BGP roles can be found in the corresponding [RFC draft](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-open-policy/?include_text=1)
Optional:
- `address` (String) Local connection IPv4/6 address.
- `port` (Number) Local connection port.
- `ttl` (Number) Time To Live (hop limit) that will be recorded in sent TCP packets.
Read-Only:
- `default_address` (String)
<a id="nestedblock--output"></a>
### Nested Schema for `output`
Optional:
- `affinity` (String) Configure output multicore processing. Read more in Routing Protocol Multi-core Support article. alone - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers afi, instance, vrf, remote-as - try to run input/output of new session in process with similar parameters main - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores) input - run output in the same process as input (can be set only for output affinity).
- `as_override` (Boolean) If set, then all instances of the remote peer's AS number in the BGP AS-PATH attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepending.
- `default_originate` (String) Specifies default route (0.0.0.0/0) distribution method.
- `default_prepend` (Number) The count of AS prepended to the AS path.
- `filter_chain` (String) Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.
- `filter_select` (String) Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.
- `keep_sent_attributes` (Boolean) Store in memory sent prefix attributes, required for ' dump-saved-advertisements ' command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.
- `network` (String) Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table.
- `no_client_to_client_reflection` (Boolean) Disable client-to-client route reflection in Route Reflector setups.
- `no_early_cut` (Boolean) The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NPLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then then this option should be used to disable the early cut feature.
- `redistribute` (String) Enable redistribution of specified route types.
- `remove_private_as` (Boolean) If set, then the BGP AS-PATH attribute is removed before sending out route updates if the attribute contains only private AS numbers. The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.
<a id="nestedblock--remote"></a>
### Nested Schema for `remote`
Optional:
- `address` (String) Remote IPv4/6 address used to connect and/or listen to.
- `allowed_as` (String) List of remote AS numbers that are allowed to connect. Useful for dynamic peer configuration.
- `as` (String) Remote AS number. If not specified BGP will determine remote AS automatically from the OPEN message.
- `port` (Number) Local connection port.
- `ttl` (Number) Acceptable minimum Time To Live, the hop limit for this TCP connection. For example, if 'ttl=255' then only single-hop neighbors will be able to establish the connection. This property only affects EBGP peers.
================================================

File: routing_bgp_template.md
================================================
# routeros_routing_bgp_template (Resource)
> [!WARNING] Using this resource you may happen unexpected behavior, for example, some of the attributes may not be removable after adding them to the TF configuration. Please report this to GitHub and it may be possible to fix it. Use the resource at your own risk as it is!
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `as` (String) 32-bit BGP autonomous system number. Value can be entered in AS-Plain and AS-Dot formats. The parameter is also used to set up the BGP confederation, in the following format: confederation_as/as . For example, if your AS is 34 and your confederation AS is 43, then as configuration should be as =43/34.
- `name` (String) Name of the BGP template.
### Optional
- `add_path_out` (String)
- `address_families` (String) List of address families about which this peer will exchange routing information. The remote peer must support (they usually do) BGP capabilities optional parameter to negotiate any other families than IP.
- `as_override` (Boolean) If set, then all instances of the remote peer's AS number in the BGP AS-PATH attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepending.
- `cisco_vpls_nlri_len_fmt` (String) VPLS NLRI length format type. Used for compatibility with Cisco VPLS.
- `cluster_id` (String) In case this instance is a route reflector: the cluster ID of the router reflector cluster to this instance belongs. This attribute helps to recognize routing updates that come from another route reflector in this cluster and avoid routing information looping. Note that normally there is only one route reflector in a cluster; in this case, 'cluster-id' does not need to be configured and BGP router ID is used instead.
- `comment` (String)
- `disabled` (Boolean)
- `hold_time` (String) Specifies the BGP Hold Time value to use when negotiating with peers. According to the BGP specification, if the router does not receive successive KEEPALIVE and/or UPDATE and/or NOTIFICATION messages within the period specified in the Hold Time field of the OPEN message, then the BGP connection to the peer will be closed. The minimal hold-time value of both peers will be actually used (note that the special value 0 or 'infinity' is lower than any other value) infinity - never expire the connection and never send keepalive messages.
- `input` (Block List, Max: 1) A group of parameters associated with BGP input. (see [below for nested schema](#nestedblock--input))
- `keepalive_time` (String) How long to keep the BGP session open after the last received 'keepalive' message.
- `multihop` (Boolean) Specifies whether the remote peer is more than one hop away. This option affects outgoing next-hop selection as described in RFC 4271 (for EBGP only, excluding EBGP peers local to the confederation). It also affects: whether to accept connections from peers that are not in the same network (the remote address of the connection is used for this check); whether to accept incoming routes with NEXT_HOP attribute that is not in the same network as the address used to establish the connection; the target-scope of the routes installed from this peer; routes from multi-hop or IBGP peers resolve their next-hops through IGP routes by default.
- `nexthop_choice` (String) Affects the outgoing NEXT_HOP attribute selection. Note that next-hops set in filters always take precedence. Also note that the next-hop is not changed on route reflection, except when it's set in the filter. default - select the next-hop as described in RFC 4271 force-self - always use a local address of the interface that is used to connect to the peer as the next-hop; propagate - try to propagate further the next-hop received; i.e. if the route has BGP NEXT_HOP attribute, then use it as the next-hop, otherwise, fall back to the default case.
- `output` (Block List, Max: 1) A group of parameters associated with BGP output. (see [below for nested schema](#nestedblock--output))
- `remove_private_as` (Boolean) If set, then the BGP AS-PATH attribute is removed before sending out route updates if the attribute contains only private AS numbers. The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.
- `router_id` (String) BGP Router ID to be used. Use the ID from the /routing/router-id configuration by specifying the reference name, or set the ID directly by specifying IP. Equal router-ids are also used to group peers into one instance.
- `routing_table` (String) Name of the routing table, to install routes in.
- `save_to` (String) Filename to be used to save BGP protocol-specific packet content (Exported PDU) into pcap file. This method allows much simpler peer-specific packet capturing for debugging purposes. Pcap files in this format can also be loaded to create virtual BGP peers to recreate conditions that happened at the time when packet capture was running.
- `templates` (Set of String) List of template names from which to inherit parameters. Useful feature, to easily configure groups with overlapping configuration options.
- `use_bfd` (Boolean) Whether to use the BFD protocol for faster connection state detection.
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `default` (Boolean)
- `id` (String) The ID of this resource.
<a id="nestedblock--input"></a>
### Nested Schema for `input`
Optional:
- `accept_comunities` (String) A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_ext_communities` (String) A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_large_comunities` (String) A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `accept_nlri` (String) Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session restart.
- `accept_unknown` (String) A quick way to filter incoming updates with specific 'unknown' attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as 'not active, filtered'. Changes to be applied required session refresh.
- `affinity` (String) Configure input multi-core processing. Read more in Routing Protocol Multi-core Support article. alone - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers afi, instance, vrf, remote-as - try to run input/output of new session in process with similar parameters main - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores) input - run output in the same process as input (can be set only for output affinity)
- `allow_as` (Number) Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.
- `filter` (String) Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.
- `ignore_as_path_len` (Boolean) Whether to ignore the AS_PATH attribute in the BGP route selection algorithm
- `limit_process_routes_ipv4` (Number) Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session 'clear' command must be used to reset the flag if the limit is reached.
- `limit_process_routes_ipv6` (Number) Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session 'clear' command must be used to reset the flag if the limit is reached.
<a id="nestedblock--output"></a>
### Nested Schema for `output`
Optional:
- `affinity` (String) Configure output multicore processing. Read more in Routing Protocol Multi-core Support article. alone - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers afi, instance, vrf, remote-as - try to run input/output of new session in process with similar parameters main - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores) input - run output in the same process as input (can be set only for output affinity).
- `default_originate` (String) Specifies default route (0.0.0.0/0) distribution method.
- `default_prepend` (Number) The count of AS prepended to the AS path.
- `filter_chain` (String) Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.
- `filter_select` (String) Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.
- `keep_sent_attributes` (Boolean) Store in memory sent prefix attributes, required for ' dump-saved-advertisements ' command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.
- `network` (String) Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table.
- `no_client_to_client_reflection` (Boolean) Disable client-to-client route reflection in Route Reflector setups.
- `no_early_cut` (Boolean) The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NPLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then then this option should be used to disable the early cut feature.
- `redistribute` (String) Enable redistribution of specified route types.
================================================

File: routing_filter_rule.md
================================================
# routeros_routing_filter_rule (Resource)
## Example Usage
```terraform
resource "routeros_routing_filter_rule" "test" {
  chain    = "testChain"
  rule     = "if (dst in 192.168.1.0/24 && dst-len>24) {set distance +1; accept} else {set distance -1; accept}"
  comment  = "comment"
  disabled = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `chain` (String) Chain name.
- `rule` (String) Filter rule.
### Optional
- `comment` (String)
- `disabled` (Boolean)
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/filter/rule/print show-ids
terraform import routeros_routing_filter_rule.test "*0"
```
================================================

File: routing_ospf_area.md
================================================
# routeros_routing_ospf_area (Resource)
## Example Usage
```terraform
resource "routeros_routing_ospf_instance" "test_routing_ospf_instance" {
  name = "test_routing_ospf_instance"
}
resource "routeros_routing_ospf_area" "test_routing_ospf_area" {
  name     = "test_routing_ospf_area"
  instance = routeros_routing_ospf_instance.test_routing_ospf_instance.name
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `instance` (String) Name of the OSPF instance this area belongs to.
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `area_id` (String) OSPF area identifier.
- `comment` (String)
- `default_cost` (Number) Default cost of injected LSAs into the area.
- `disabled` (Boolean)
- `no_summaries` (Boolean) If set then the area will not flood summary LSAs in the stub area. <em>The correct value of this attribute may not be displayed in Winbox. Please check the parameters in the console!</em>
- `nssa_translate` (String) The parameter indicates which ABR will be used as a translator from type7 to type5 LSA.
- `type` (String) The area type.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/area/print show-ids
terraform import routeros_routing_ospf_area.test_routing_ospf_area "*0"
```
================================================

File: routing_ospf_instance.md
================================================
# routeros_routing_ospf_instance (Resource)
## Example Usage
```terraform
resource "routeros_routing_ospf_instance" "test_routing_ospf_instance" {
  name = "test_routing_ospf_instance"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `domain_id` (String) MPLS-related parameter.
- `domain_tag` (Number) if set, then used in route redistribution (as route-tag in all external LSAs generated by this router), and in route calculation (all external LSAs having this route tag are ignored). Needed for interoperability with older Cisco systems. By default not set.
- `in_filter_chain` (String) name of the routing filter chain used for incoming prefixes
- `mpls_te_address` (String) the area used for MPLS traffic engineering.
- `mpls_te_area` (String) the area used for MPLS traffic engineering.
- `originate_default` (String) Specifies default route (0.0.0.0/0) distribution method.
- `out_filter_chain` (String) name of the routing filter chain used for outgoing prefixes filtering.
- `out_filter_select` (String) name of the routing filter select chain, used for output selection.
- `redistribute` (Set of String) Enable redistribution of specific route types.
- `router_id` (String) OSPF Router ID. Can be set explicitly as an IP address, or as the name of the router-id instance.
- `routing_table` (String) Name of the routing table in use.
- `version` (Number) OSPF version this instance will be running (v2 for IPv4, v3 for IPv6).
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/instance/print show-ids
terraform import routeros_routing_ospf_instance.test_routing_ospf_instance "*0"
```
================================================

File: routing_ospf_interface_template.md
================================================
# routeros_routing_ospf_interface_template (Resource)
## Example Usage
```terraform
resource "routeros_routing_ospf_instance" "test_routing_ospf_instance" {
  name = "test_routing_ospf_instance"
}
resource "routeros_routing_ospf_area" "test_routing_ospf_area" {
  name     = "test_routing_ospf_area"
  instance = routeros_routing_ospf_instance.test_routing_ospf_instance.name
}
resource "routeros_routing_ospf_interface_template" "test_routing_ospf_interface_template" {
  area = routeros_routing_ospf_area.test_routing_ospf_area.name
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `area` (String) The OSPF area to which the matching interface will be associated.
### Optional
- `auth` (String) Specifies authentication method for OSPF protocol messages.
- `auth_id` (Number) The key id is used to calculate message digest (used when MD5 or SHA authentication is enabled).
- `auth_key` (String, Sensitive) The authentication key to be used, should match on all the neighbors of the network segment (available since RouterOS 7.x).
- `authentication_key` (String, Sensitive) The authentication key to be used, should match on all the neighbors of the network segment (for versions before RouterOS 7.x).
- `comment` (String)
- `cost` (Number) Interface cost expressed as link state metric.
- `dead_interval` (String) Specifies the interval after which a neighbor is declared dead.
- `disabled` (Boolean)
- `hello_interval` (String) The interval between HELLO packets that the router sends out this interface.
- `instance_id` (Number) Interface cost expressed as link state metric.
- `interfaces` (Set of String) Interfaces to match.
- `network` (String) The network prefix associated with the area.
- `passive` (Boolean) If enabled, then do not send or receive OSPF traffic on the matching interfaces. <em>The correct value of this attribute may not be displayed in Winbox. Please check the parameters in the console!</em>
- `prefix_list` (String) Name of the address list containing networks that should be advertised to the v3 interface.
- `priority` (Number) Router's priority. Used to determine the designated router in a broadcast network.
- `retransmit_interval` (String) Time interval the lost link state advertisement will be resent.
- `transmit_delay` (String) Link-state transmit delay is the estimated time it takes to transmit a link-state update packet on the interface.
- `type` (String) The OSPF network type on this interface.
- `vlink_neighbor_id` (String) Specifies the router-id of the neighbor which should be connected over the virtual link.
- `vlink_transit_area` (String) A non-backbone area the two routers have in common over which the virtual link will be established.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/interface-template/print show-ids
terraform import routeros_routing_ospf_interface_template.test_routing_ospf_interface_template "*0"
```
================================================

File: routing_rule.md
================================================
# routeros_routing_rule (Resource)
## Example Usage
```terraform
resource "routeros_routing_rule" "test" {
  dst_address = "192.168.1.0/24"
  action      = "lookup-only-in-table"
  interface   = "ether1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `action` (String) An action to take on the matching packet:drop - silently drop the packet.lookup - perform a lookup in routing tables.lookup-only-in-table - perform lookup only in the specified routing table (see table parameter).unreachable - generate ICMP unreachable message and send it back to the source.
- `comment` (String)
- `disabled` (Boolean)
- `dst_address` (String) The destination address of the packet to match.
- `interface` (String) Incoming interface to match.
- `min_prefix` (Number) Equivalent to Linux IP rule `suppress_prefixlength`. For example to suppress the default route in the routing decision set the value to 0.
- `routing_mark` (String) Match specific routing mark.
- `src_address` (String) The source address of the packet to match.
- `table` (String) Name of the routing table to use for lookup.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/rule get [print show-ids]]
terraform import routeros_routing_rule.test *3
```
================================================

File: routing_table.md
================================================
# routeros_routing_table (Resource)
## Example Usage
```terraform
resource "routeros_routing_table" "test_table" {
  name = "to_ISP1"
  fib  = false
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `fib` (Boolean) fib parameter should be specified if the routing table is intended to push routes to the FIB.
- `name` (String) Routing table name.
### Read-Only
- `dynamic` (Boolean) Configuration item created by software, not by management interface. It is not exported, and cannot be directly modified.
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/table get [print show-ids]]
terraform import routeros_routing_table.test_table "*0"
```
================================================

File: scheduler.md
================================================
# routeros_scheduler (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_system_scheduler](system_scheduler.md)
================================================

File: snmp.md
================================================
# routeros_snmp (Resource)
## Example Usage
```terraform
resource "routeros_snmp" "test" {
  contact          = "John D."
  enabled          = true
  engine_id_suffix = "8a3c"
  location         = "Backyard"
  trap_community   = "private"
  trap_generators  = "start-trap"
  trap_version     = 3
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `contact` (String) Contact information.
- `enabled` (Boolean) Used to disable/enable SNMP service
- `engine_id_suffix` (String) Unique identifier for an SNMPv3 engine by configuring the suffix of the engine ID.
- `location` (String) Location information.
- `src_address` (String) Force the router to always use the same IP source address for all of the SNMP messages.
- `trap_community` (String, Sensitive) Which communities configured in community menu to use when sending out the trap. This name must be present in the community list.
- `trap_generators` (String) What action will generate traps: interfaces - interface changes; start-trap - snmp server starting on the router.
- `trap_interfaces` (String) List of interfaces that traps are going to be sent out.
- `trap_target` (Set of String) IP (IPv4 or IPv6) addresses of SNMP data collectors that have to receive the trap.
- `trap_version` (Number) Version of SNMP protocol to use for trap.
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `engine_id` (String) For SNMP v3, used as part of identifier. You can configure suffix part of engine id using this argument. If SNMP client is not  capable to detect set engine-id value then this prefix hex have to be  used 0x80003a8c04
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_snmp.test .
```
================================================

File: snmp_community.md
================================================
# routeros_snmp_community (Resource)
## Example Usage
```terraform
resource "routeros_snmp_community" "test" {
  authentication_password = "authpasswd"
  authentication_protocol = "MD5"
  comment                 = "Comment"
  disabled                = true
  encryption_password     = "encpassword"
  encryption_protocol     = "DES"
  name                    = "private"
  read_access             = true
  security                = "private"
  write_access            = true
}
resource "routeros_snmp_community" "mything" {
  addresses = ["10.0.1.12", "10.10.0.129"]
  name      = "mything"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `addresses` (Set of String) Set of IP (v4 or v6) addresses or CIDR networks from which connections to SNMP server are allowed.
- `authentication_password` (String, Sensitive) Password used to authenticate the connection to the server (SNMPv3).
- `authentication_protocol` (String) The protocol used for authentication (SNMPv3).
- `comment` (String)
- `disabled` (Boolean)
- `encryption_password` (String, Sensitive) The password used for encryption (SNMPv3).
- `encryption_protocol` (String) encryption protocol to be used to encrypt the communication (SNMPv3). AES (see rfc3826) available since v6.16.
- `name` (String) Community Name.
- `read_access` (Boolean) Whether read access is enabled for this community.
- `security` (String) Security features.
- `write_access` (Boolean) Whether write access is enabled for this community.
### Read-Only
- `default` (Boolean) It's a default community.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/snmp/community get [print show-ids]]
terraform import routeros_snmp_community.test "*0"
```
================================================

File: system_certificate.md
================================================
# routeros_system_certificate (Resource)
Certificate resource management consists of two independent processes:
* key creation and certificate signing request (`key` + `csr`)
* certificate signing by the issuer (`crt`)
For a complete certificate creation cycle, both of the above steps must be performed. In this case the `sign {}` block must be specified in the configuration.
If you need to import the current state of the certificate resource, then do not specify the `sign{}` block.
Importing an external certificate is also done without specifying the `sign{}` block, because the certificate should have already been signed by the issuer at this step.
---
## Example Usage
```terraform
resource "routeros_system_certificate" "root_ca" {
  name        = "Test-Root-CA"
  common_name = "RootCA"
  key_usage   = ["key-cert-sign", "crl-sign"]
  trusted     = true
  # Sign Root CA.
  sign {
  }
}
# digitalSignature: Used for entity and data origin authentication with integrity.
# keyEncipherment:  Used to encrypt symmetric key, which is then transferred to target.
# keyAgreement:     Enables use of key agreement to establish symmetric key with target. 
resource "routeros_system_certificate" "server_crt" {
  name        = "Server-Certificate"
  common_name = "server.crt"
  #  KUs: igitalSignature, keyEncipherment or keyAgreement
  key_usage = ["digital-signature", "key-encipherment", "tls-server"]
  sign {
    ca = routeros_system_certificate.root_ca.name
  }
}
resource "routeros_system_certificate" "client_crt" {
  name        = "Client-Certificate"
  common_name = "client.crt"
  key_size    = "prime256v1"
  #  KUs: digitalSignature and/or keyAgreement
  key_usage = ["digital-signature", "key-agreement", "tls-client"]
  sign {
    ca = routeros_system_certificate.root_ca.name
  }
}
resource "routeros_system_certificate" "unsigned_crt" {
  name             = "Unsigned-Certificate"
  common_name      = "unsigned.crt"
  key_size         = "1024"
  subject_alt_name = "DNS:router.lan,DNS:myrouter.lan,IP:192.168.88.1"
}
resource "routeros_system_certificate" "scep_client" {
  name        = "SCEP-Client"
  common_name = "scep-client.crt"
  key_usage   = ["digital-signature", "key-agreement", "tls-client"]
  sign_via_scep {
    scep_url = "http://scep.server/scep/test"
  }
}
#  Import certificate
data "routeros_x509" "cert" {
  data = <<EOT
	-----BEGIN CERTIFICATE-----
	MIIBlTCCATugAwIBAgIINLsws71B5zIwCgYIKoZIzj0EAwIwHzEdMBsGA1UEAwwU
	RXh0ZXJuYWwgQ2VydGlmaWNhdGUwHhcNMjQwNTE3MjEyOTUzWhcNMjUwNTE3MjEy
	OTUzWjAfMR0wGwYDVQQDDBRFeHRlcm5hbCBDZXJ0aWZpY2F0ZTBZMBMGByqGSM49
	AgEGCCqGSM49AwEHA0IABKE1g0Qj4ujIold9tklu2z4BUu/K7xDFF5YmedtOfJyM
	1/80APNboqn71y4m4XNE1JNtQuR2bSZPHVrzODkR16ujYTBfMA8GA1UdEwEB/wQF
	MAMBAf8wDgYDVR0PAQH/BAQDAgG2MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEF
	BQcDAjAdBgNVHQ4EFgQUNXd5bvluIV9YAhGc5yMHc6OzXpMwCgYIKoZIzj0EAwID
	SAAwRQIhAODte/qS6CE30cvnQpxP/ObWBPIPZnHtkFHIIC1AOSXwAiBGCGQE+aJY
	W72Rw0Y1ckvlt6sU0urkzGuj5wxVF/gSYA==
	-----END CERTIFICATE-----
EOT
}
resource "routeros_file" "key" {
  name = "external.key"
  # The lines of the certificate must not contain indentation.
  contents = <<EOT
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIHeMEkGCSqGSIb3DQEFDTA8MBsGCSqGSIb3DQEFDDAOBAiy/wEW6/MglgICCAAw
HQYJYIZIAWUDBAEqBBD6v8dLA2FjPn62Xz57pcu9BIGQhclivPw1eC2b14ea58Tw
nzDdbYN6/yUiMqapW2xZaT7ZFnbEai4n9/utgtEDnfKHlZvZj2kRhvYoWrvTkt/W
1mkd5d/runsn+B5GO+CMHFHh4t41WMpZysmg+iP8FiiehOQEsWyEZFaedxfYYtSL
Sk+abxJ+NMQoh+S5d73niu1CO8uqQjOd8BoSOurURsOh
-----END ENCRYPTED PRIVATE KEY-----
EOT
}
resource "routeros_file" "cert" {
  name = "external.crt"
  # Normalized certificate
  contents = data.routeros_x509.cert.pem
}
resource "routeros_system_certificate" "external" {
  name        = "external.crt"
  common_name = data.routeros_x509.cert.common_name
  import {
    cert_file_name = routeros_file.cert.name
    key_file_name  = routeros_file.key.name
    passphrase     = "11111111"
  }
  depends_on = [routeros_file.key, routeros_file.cert]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `common_name` (String) Common Name (e.g. server FQDN or YOUR name).
- `name` (String) Name of the certificate. Name can be edited.
### Optional
- `copy_from` (String)
- `country` (String) Country Name (2 letter code).
- `days_valid` (Number) Certificate lifetime.
- `import` (Block Set) (see [below for nested schema](#nestedblock--import))
- `key_size` (String)
- `key_usage` (Set of String) Detailed key usage descriptions can be found in RFC 5280.
- `locality` (String) Locality Name (eg, city).
- `organization` (String) Organizational Unit Name (eg, section)
- `sign` (Block Set) (see [below for nested schema](#nestedblock--sign))
- `sign_via_scep` (Block Set) (see [below for nested schema](#nestedblock--sign_via_scep))
- `state` (String) State or Province Name (full name).
- `subject_alt_name` (String) SANs (subject alternative names).
- `trusted` (Boolean) If set to yes certificate is included 'in trusted certificate chain'.
- `unit` (String) Organizational Unit Name (eg, section).
### Read-Only
- `akid` (String) Authority Key Identifier.
- `authority` (String)
- `ca` (String)
- `ca_crl_host` (String)
- `ca_fingerprint` (String)
- `challenge_password` (String, Sensitive) A challenge password for scep client.
- `crl` (String)
- `digest_algorithm` (Boolean)
- `dsa` (Boolean)
- `expired` (Boolean) Set to true if certificate is expired.
- `expires_after` (String)
- `fingerprint` (String)
- `id` (String) The ID of this resource.
- `invalid_after` (String) The date after which certificate wil be invalid.
- `invalid_before` (String) The date before which certificate is invalid.
- `issued` (String)
- `issuer` (String)
- `key_type` (String)
- `private_key` (Boolean)
- `req_fingerprint` (String)
- `revoked` (String)
- `scep_url` (String)
- `serial_number` (String)
- `skid` (String) Subject Key Identifier.
- `smart_card_key` (String)
- `status` (String) Shows current status of scep client.
<a id="nestedblock--import"></a>
### Nested Schema for `import`
Required:
- `cert_file_name` (String) Certificate file name that will be imported.
Optional:
- `key_file_name` (String) Key file name that will be imported.
- `passphrase` (String, Sensitive) File passphrase if there is such.
<a id="nestedblock--sign"></a>
### Nested Schema for `sign`
Optional:
- `ca` (String) Which CA to use if signing issued certificates.
- `ca_crl_host` (String) CRL host if issuing CA certificate.
<a id="nestedblock--sign_via_scep"></a>
### Nested Schema for `sign_via_scep`
Required:
- `scep_url` (String) HTTP URL to the SCEP server.
Optional:
- `ca_identity` (String) SCEP CA identity.
- `challenge_password` (String, Sensitive) A challenge password.
- `on_smart_card` (Boolean) Whether to store a private key on smart card if hardware supports it.
- `refresh` (Boolean) Check certificate expiration and refresh it if expired.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/certificate get [print show-ids]]
#If you plan to manipulate the certificate requiring signing, you need to correctly fill in the sign{} section.
#Changes in the sign{} section will not cause changes in the certificate. It's not a bug, it's a feature!
terraform import routeros_system_certificate.client *9D
```
================================================

File: system_certificate_scep_server.md
================================================
# routeros_system_certificate_scep_server (Resource)
## Example Usage
```terraform
resource "routeros_system_certificate" "example_root_ca" {
  name        = "example_root_ca"
  common_name = "Example Root CA"
  key_usage   = ["key-cert-sign", "crl-sign"]
  trusted     = true
  sign {
  }
}
# You can also use the alias "routeros_certificate_scep_server"
resource "routeros_system_certificate_scep_server" "example_scep_server" {
  ca_cert    = routeros_system_certificate.example_root_ca.name
  path       = "/scep/example_scep_server"
  days_valid = 30
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `ca_cert` (String) Name of the CA certificate to use.
- `path` (String) HTTP path starting with `/scep/`.
### Optional
- `days_valid` (Number) The number of days to sign certificates for.
- `disabled` (Boolean)
- `next_ca_cert` (String) Name of the next CA certificate or `none`.
- `request_lifetime` (String) Request lifetime (5m minimum).
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
# The ID can be found via API or the terminal
# The command for the terminal is -> /certificate/scep-server/print show-ids
terraform import routeros_system_certificate_scep_server.example_scep_server "*1"
```
================================================

File: system_clock.md
================================================
# routeros_system_clock (Resource)
## Example Usage
```terraform
resource "routeros_system_clock" "set" {
  date           = "2024-05-15"
  time           = "17:58:11"
  time_zone_name = "EST"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `date` (String) Date.
- `time` (String) Time.
- `time_zone_autodetect` (Boolean) Feature available from v6.27. If enabled, the time zone will be set automatically.
- `time_zone_name` (String) Name of the time zone. As most of the text values in RouterOS, this value is case sensitive. Special value manual applies [manually configured GMT offset](https://wiki.mikrotik.com/wiki/Manual:System/Time#Manual_time_zone_configuration), which by default is 00:00 with no daylight saving time.
### Read-Only
- `dst_active` (Boolean) This property has the value yes while daylight saving time of the current time zone is active.
- `gmt_offset` (String) This is the current value of GMT offset used by the system, after applying base time zone offset and active daylight saving time offset.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_clock.set .
```
================================================

File: system_identity.md
================================================
# routeros_system_identity (Resource)
## Example Usage
```terraform
resource "routeros_system_identity" "identity" {
  name = "My Router"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Device name.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_identity.identity .
```
================================================

File: system_logging.md
================================================
# routeros_system_logging (Resource)
## Example Usage
```terraform
resource "routeros_system_logging" "log_snmp_disk" {
  action = "disk"
  topics = ["snmp"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `action` (String) specifies one of the system default actions or user specified action listed in actions menu
### Optional
- `disabled` (Boolean) Whether or not this logging should be disabled
- `prefix` (String) prefix added at the beginning of log messages
- `topics` (Set of String) log all messages that falls into specified topic or list of topics.
						  '!' character can be used before topic to exclude messages falling under this topic. For example, we want to log NTP debug info without too much details:
						  /system logging add topics=ntp,debug,!packet
### Read-Only
- `default` (String)
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
## Import
Import is supported using the following syntax:
```shell
# The ID can be found via API or the terminal
# The command for the terminal is -> :put [/system/logging/print  get [print show-ids]]
terraform import routeros_system_logging.log_snmp_disk "*4"
```
================================================

File: system_logging_action.md
================================================
# routeros_system_logging_action (Resource)
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of an action.
- `target` (String) Storage facility or target of log messages.
### Optional
- `bsd_syslog` (Boolean) Whether to use bsd-syslog as defined in RFC 3164.
- `disk_file_count` (Number) Specifies number of files used to store log messages, applicable only if `action=disk`.
- `disk_file_name` (String) Name of the file used to store log messages, applicable only if `action=disk`.
- `disk_lines_per_file` (Number) Specifies maximum size of file in lines, applicable only if `action=disk`.
- `disk_stop_on_full` (Boolean) Whether to stop to save log messages to disk after the specified disk-lines-per-file and disk-file-count number is reached, applicable only if `action=disk`.
- `email_start_tls` (Boolean) Whether to use tls when sending email, applicable only if `action=email`.
- `email_to` (String) Email address where logs are sent, applicable only if `action=email`.
- `memory_lines` (Number) Number of records in local memory buffer, applicable only if `action=memory`.
- `memory_stop_on_full` (Boolean) Whether to stop to save log messages in local buffer after the specified memory-lines number is reached.
- `remember` (Boolean) Whether to keep log messages, which have not yet been displayed in console, applicable if `action=echo`.
- `remote` (String) Remote logging server's IP/IPv6 address, applicable if `action=remote`.
- `remote_port` (Number) Remote logging server's UDP port, applicable if `action=remote`.
- `src_address` (String) Source address used when sending packets to remote server, applicable if `action=remote`.
- `syslog_facility` (String) SYSLOG facility, applicable if `action=remote`.
- `syslog_severity` (String) Severity level indicator defined in RFC 3164, applicable if `action=remote`.
- `syslog_time_format` (String) SYSLOG time format (`bsd-syslog` or `iso8601`).
### Read-Only
- `default` (Boolean) This is a default action.
- `id` (String) The ID of this resource.
================================================

File: system_ntp_client.md
================================================
# routeros_system_ntp_client (Resource)
## Example Usage
```terraform
resource "routeros_system_ntp_client" "test" {
  enabled = true
  mode    = "unicast"
  servers = ["146.59.35.38", "167.235.201.139"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `enabled` (Boolean) Enable NTP client.
- `mode` (String) Mode that the NTP client will operate in
- `servers` (Set of String) The list of NTP servers. It is possible to add static entries.
			The following formats are accepted:
			- FQDN ("Resolved Address" will appear in the "Servers"- window in an appropriate column if the address is 
			resolved) or IP address can be used. If DHCP-Client property `use-peer-ntp=yes` - the dynamic entries 
			advertised by DHCP
			- ipv4
			- ipv4@vrf
			- ipv6
			- ipv6@vrf
			- ipv6-linklocal%interface
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `freq_drift` (String) The fractional frequency drift per unit time.
- `id` (String) The ID of this resource.
- `status` (String) Current status of the NTP client.
- `synced_server` (String) The IP address of the NTP Server.
- `synced_stratum` (String) The accuracy of each server is defined by a number called the stratum, with the topmost level (primary servers) assigned as one and each level downwards (secondary servers) in the hierarchy assigned as one greater than the preceding level.
- `system_offset` (String) This is a signed, fixed-point number indicating the offset of the NTP server's clock relative to the local clock, in seconds.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_ntp_client.test .
```
================================================

File: system_ntp_server.md
================================================
# routeros_system_ntp_server (Resource)
## Example Usage
```terraform
resource "routeros_system_ntp_server" "test" {
  enabled             = true
  broadcast           = true
  multicast           = true
  manycast            = true
  use_local_clock     = true
  local_clock_stratum = 3
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `auth_key` (String) NTP symmetric key, used for authentication between the NTP client and server. Key Identifier (Key ID) - an integer identifying the cryptographic key used to generate the message-authentication code.
- `broadcast` (Boolean) Enable certain NTP server mode, for this mode to work you have to set up broadcast-addresses field.
- `broadcast_addresses` (String) Set broadcast address to use for NTP server broadcast mode.
- `enabled` (Boolean) Enable NTP server.
- `local_clock_stratum` (Number) Manually set stratum if ```use_local_clock = true```.
- `manycast` (Boolean) Enable certain NTP server mode.
- `multicast` (Boolean) Enable certain NTP server mode.
- `use_local_clock` (Boolean) The server will supply its local system time as valid if others are not available.
- `vrf` (String) The VRF table this resource operates on.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_ntp_server.test .
```
================================================

File: system_scheduler.md
================================================
# routeros_system_scheduler (Resource)
## Example Usage
```terraform
resource "routeros_system_scheduler" "schedule1" {
  name     = "schedule1"
  on_event = "script name"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Changing the name of this resource will force it to be recreated.
	> The links of other configuration properties to this resource may be lost!
	> Changing the name of the resource outside of a Terraform will result in a loss of control integrity for that resource!
- `on_event` (String) Name of the script to execute. It must be presented at /system script.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `interval` (String) Interval between two script executions, if time interval is set to zero, the script is only executed at its start time, otherwise it is executed repeatedly at the time interval is specified.
- `policy` (List of String) List of applicable policies:
    * dude - Policy that grants rights to log in to dude server.  
    * ftp - Policy that grants full rights to log in remotely via FTP, to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.  
    * password - Policy that grants rights to change the password.  
    * policy - Policy that grants user management rights. Should be used together with the write policy. Allows also to see global variables created by other users (requires also 'test' policy).  
    * read - Policy that grants read access to the router's configuration. All console commands that do not alter router's configuration are allowed. Doesn't affect FTP.  
    * reboot - Policy that allows rebooting the router.  
    * romon - Policy that grants rights to connect to RoMon server.  
    * sensitive - Policy that grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed.  
    * sniff - Policy that grants rights to use packet sniffer tool.  
    * test - Policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, and other test commands.  
    * write - Policy that grants write access to the router's configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as well.  
policy = ["ftp", "read", "write"]
- `start_date` (String) Date of the first script execution.
- `start_time` (String) Time of the first script execution. If scheduler item has start-time set to startup, it behaves as if start-time and start-date were set to time 3 seconds after console starts up. It means that all scripts having start-time is startup and interval is 0 will be executed once each time router boots. If the interval is set to value other than 0 scheduler will not run at startup.
### Read-Only
- `id` (String) The ID of this resource.
- `next_run` (String)
- `owner` (String)
- `run_count` (String) This counter is incremented each time the script is executed.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/system/scheduler get [print show-ids]]
terraform import routeros_system_scheduler.schedule1 "*0"
```
================================================

File: system_script.md
================================================
# routeros_system_script (Resource)
## Example Usage
```terraform
resource "routeros_system_script" "script" {
  name   = "my_script"
  source = <<EOF
    :log info "This is a test script created by Terraform."
    EOF
  policy = ["read", "write", "test", "policy"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the script.
- `source` (String) Script source code.
### Optional
- `comment` (String)
- `dont_require_permissions` (Boolean) Bypass permissions check when the script is being executed, useful when scripts are being executed from services that have limited permissions, such as Netwatch.
- `policy` (Set of String) List of applicable policies:
	* ftp - Policy that grants full rights to log in remotely via FTP, to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.  
	* password - Policy that grants rights to change the password.  
	* policy - Policy that grants user management rights. Should be used together with the write policy. Allows also to see global variables created by other users (requires also 'test' policy).  
	* read - Policy that grants read access to the router's configuration. All console commands that do not alter router's configuration are allowed. Doesn't affect FTP.  
	* reboot - Policy that allows rebooting the router.  
	* sensitive - Policy that grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed.  
	* sniff - Policy that grants rights to use packet sniffer tool.  
	* test - Policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, and other test commands.  
	* write - Policy that grants write access to the router's configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as well.  
policy = ["ftp", "read", "write"]
### Read-Only
- `id` (String) The ID of this resource.
- `invalid` (Boolean)
- `last_started` (String) Date and time when the script was last invoked.
- `owner` (String)
- `run_count` (String) This counter is incremented each time the script is executed.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/system/script get [print show-ids]]
terraform import routeros_system_script.script "*0"
```
================================================

File: system_user.md
================================================
# routeros_system_user (Resource)
## Example Usage
```terraform
resource "routeros_system_user" "test" {
  name     = "test-user-1"
  address  = "0.0.0.0/0"
  group    = "read"
  password = "secret"
  comment  = "Test User"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `group` (String) Name of the group the user belongs to.
- `name` (String) User name. Although it must start with an alphanumeric character, it may contain '*', '_', '.' and '@' symbols.
### Optional
- `address` (String) Host or network address from which the user is allowed to log in.
- `comment` (String)
- `disabled` (Boolean)
- `password` (String, Sensitive) User  password. If not specified, it is left blank (hit [Enter] when logging  in). It conforms to standard Unix characteristics of passwords and may  contain letters, digits, '*' and '_' symbols.
### Read-Only
- `expired` (Boolean) Password expired.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user get [print show-ids]]
terraform import routeros_system_user.test *1
```
================================================

File: system_user_aaa.md
================================================
# routeros_system_user_aaa (Resource)
## Example Usage
```terraform
resource "routeros_system_user_aaa" "settings" {
  use_radius = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `accounting` (Boolean) An option that enables accounting for users.
- `default_group` (String) The user group that is used by default for users authenticated via a RADIUS server.
- `exclude_groups` (Set of String) A set of groups that are not allowed for users authenticated by RADIUS.
- `interim_update` (String) Interval between scheduled RADIUS Interim-Update messages.
- `use_radius` (Boolean) An option whether to use RADIUS server.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_user_aaa.settings .
```
================================================

File: system_user_group.md
================================================
# routeros_system_user_group (Resource)
## Example Usage
```terraform
resource "routeros_system_user_group" "terraform" {
  name   = "terraform"
  policy = ["api", "!ftp", "!local", "password", "policy", "read", "!reboot", "!rest-api", "!romon", "sensitive", "!sniff", "!ssh", "!telnet", "!test", "!web", "!winbox", "write"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) The name of the user group
### Optional
- `comment` (String)
- `policy` (Set of String) A set of allowed policies.
- `skin` (String) The name of the skin that will be used for WebFig.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user/group get [print show-ids]]
terraform import routeros_system_user_group.terraform *1
```
================================================

File: system_user_settings.md
================================================
# routeros_system_user_settings (Resource)
## Example Usage
```terraform
resource "routeros_system_user_settings" "settings" {
  minimum_categories      = 2
  minimum_password_length = 8
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `minimum_categories` (Number) An option specifies the complexity requirements of the password, with categories being uppercase, lowercase, digit, and symbol.
- `minimum_password_length` (Number) An option specifies the minimum length of the password.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_system_user_settings.settings .
```
================================================

File: tool_bandwidth_server.md
================================================
# routeros_tool_bandwidth_server (Resource)
## Example Usage
```terraform
resource "routeros_tool_bandwidth_server" "test" {
  enabled                 = true
  authenticate            = false
  max_sessions            = 100
  allocate_udp_ports_from = 2000
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `allocate_udp_ports_from` (Number) Beginning of UDP port range.
- `authenticate` (Boolean) Communicate only with authenticated clients.
- `enabled` (Boolean) Defines whether bandwidth server is enabled or not.
- `max_sessions` (Number) Maximal simultaneous test count.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_tool_bandwidth_server.test .
```
================================================

File: tool_mac_server.md
================================================
# routeros_tool_mac_server (Resource)
## Example Usage
```terraform
resource "routeros_tool_mac_server" "test" {
  allowed_interface_list = "LAN"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `allowed_interface_list` (String) List of interfaces for MAC Telnet access.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_tool_mac_server.test .
```
================================================

File: tool_mac_server_winbox.md
================================================
# routeros_tool_mac_server_winbox (Resource)
## Example Usage
```terraform
resource "routeros_tool_mac_server_winbox" "test" {
  allowed_interface_list = "LAN"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `allowed_interface_list` (String) List of interfaces for MAC WinBox access.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_tool_mac_server_winbox.test .
```
================================================

File: tool_netwatch.md
================================================
# routeros_tool_netwatch (Resource)
## Example Usage
```terraform
resource "routeros_tool_netwatch" "test" {
  name      = "watch-google-pdns"
  type      = "icmp"
  host      = "8.8.8.8"
  interval  = "30s"
  up_script = ":log info \"Ping to 8.8.8.8 successful\""
  thr_max   = "400ms"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `host` (String) The IP address of the server to be probed. Formats:
			- ipv4
			- ipv4@vrf
			- ipv6 
			- ipv6@vrf
			- ipv6-linklocal%interface
- `name` (String) Task name.
### Optional
- `accept_icmp_time_exceeded` (Boolean) If the ICMP `time exceeded` message should be considered a valid response.
- `comment` (String)
- `disabled` (Boolean)
- `dns_server` (String) The DNS server that the probe should send its requests to, if not specified it will use the value from `/ip dns`.
- `down_script` (String) Script to execute on the event of probe state change `OK` --> `fail`.
- `http_code_max` (Number) Response in the range [http-code-min , http-code-max] is a probe pass/OK; outside - a probe fail. See [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) or [rfc7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6).
- `http_code_min` (Number) OK/fail criteria for HTTP response code.
- `interval` (String) The time interval between probe tests.
- `packet_count` (Number) Total count of ICMP packets to send out within a single test.
- `packet_interval` (String) The time between ICMP-request packet send.
- `packet_size` (Number) The total size of the IP ICMP packet.
- `port` (Number) TCP port (for both tcp-conn and http-get probes)
- `record_type` (String) Record type that will be used for DNS probe.
- `src_address` (String) Source IP address which the Netwatch will try to use in order to reach the host. If address is not present, then the host will be considered as `down`.
- `start_delay` (String) Time to wait before starting probe (on add, enable, or system start).
- `startup_delay` (String) Time to wait until starting Netwatch probe after system startup.
- `test_script` (String) Script to execute at the end of every probe test.
- `thr_avg` (String) Fail threshold for rtt-avg.
- `thr_http_time` (String) Fail threshold for http-resp-time.
- `thr_jitter` (String) Fail threshold for rtt-jitter.
- `thr_loss_count` (Number) Fail threshold for loss-count.
- `thr_loss_percent` (Number) Fail threshold for loss-percent.
- `thr_max` (String) Fail threshold for rtt-max (a value above thr-max is a probe fail).
- `thr_stdev` (String) Fail threshold for rtt-stdev.
- `thr_tcp_conn_time` (String) Fail threshold for tcp-connect-time, the configuration uses microseconds, if the time unit is not specified (s/m/h), log and status pages display the same value in milliseconds.
- `timeout` (String) Max time limit to wait for a response.
- `ttl` (Number) Manually set time to live value for ICMP packet.
- `type` (String) Type of the probe:
			- icmp - (ping-style) series of ICMP request-response with statistics
			- tcp-conn - test TCP connection (3-way handshake) to a server specified by IP and port
			- http-get - do an HTTP Get request and test for a range of correct replies
			- simple - simplified ICMP probe, with fewer options than **ICMP** type, used for backward compatibility with the older Netwatch version
- `up_script` (String) Script to execute on the event of probe state change `fail` --> `OK`.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/tool/netwatch get [print show-ids]]
terraform import routeros_tool_netwatch.test *3
```
================================================

File: user_manager_advanced.md
================================================
# routeros_user_manager_advanced (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_advanced" "settings" {
  web_private_password = "password"
  web_private_username = "admin"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `paypal_allow` (Boolean) An option whether to enable PayPal functionality for User Manager.
- `paypal_currency` (String) The currency related to price setting in which users will be billed.
- `paypal_password` (String) The password of the PayPal API account.
- `paypal_signature` (String) The signature of the PayPal API account.
- `paypal_use_sandbox` (Boolean) An option whether to use PayPal's sandbox environment for testing purposes.
- `paypal_user` (String) The username of the PayPal API account.
- `web_private_password` (String) The password for accessing `/um/PRIVATE/` section over HTTP.
- `web_private_username` (String) The username for accessing `/um/PRIVATE/` section over HTTP.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_user_manager_advanced.settings .
```
================================================

File: user_manager_attribute.md
================================================
# routeros_user_manager_attribute (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_attribute" "mikrotik_wireless_comment" {
  name         = "Mikrotik-Wireless-Comment"
  packet_types = ["access-accept"]
  type_id      = 21
  value_type   = "string"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) The attribute's name.
- `type_id` (Number) Attribute identification number from the specific vendor's attribute database.
### Optional
- `packet_types` (Set of String) A set of `access-accept` and `access-challenge`.
- `value_type` (String) The attribute's value type.
- `vendor_id` (String) IANA allocated a specific enterprise identification number.
### Read-Only
- `default` (Boolean)
- `default_name` (String) The attribute's default name.
- `id` (String) The ID of this resource.
- `standard_name` (String)
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/attribute get [print show-ids]]
terraform routeros_user_manager_attribute.mikrotik_wireless_comment '*1'
```
================================================

File: user_manager_database.md
================================================
# routeros_user_manager_database (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_database" "settings" {
  db_path = "/flash/user-manager5"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `db_path` (String) Path to the location where database files will be stored.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_user_manager_database.settings .
```
================================================

File: user_manager_limitation.md
================================================
# routeros_user_manager_limitation (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_limitation" "test" {
  name           = "test"
  download_limit = 1024
  upload_limit   = 1024
  uptime_limit   = "10d"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Unique name of the limitation.
### Optional
- `download_limit` (Number) The total amount of traffic a user can download in bytes.
- `rate_limit_burst_rx` (Number)
- `rate_limit_burst_threshold_rx` (Number)
- `rate_limit_burst_threshold_tx` (Number)
- `rate_limit_burst_time_rx` (String)
- `rate_limit_burst_time_tx` (String)
- `rate_limit_burst_tx` (Number)
- `rate_limit_min_rx` (Number)
- `rate_limit_min_tx` (Number)
- `rate_limit_priority` (Number)
- `rate_limit_rx` (Number)
- `rate_limit_tx` (Number)
- `reset_counters_interval` (String) The interval from `reset_counters_start_time` when all associated user statistics are cleared.
- `reset_counters_start_time` (String) Static date and time value from which `reset_counters_interval` is calculated.
- `transfer_limit` (Number) The total amount of aggregated (download+upload) traffic in bytes.
- `upload_limit` (Number) The total amount of traffic a user can upload in bytes.
- `uptime_limit` (String) The total amount of uptime a user can stay active.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/limitation get [print show-ids]]
terraform import routeros_user_manager_limitation.test '*1'
```
================================================

File: user_manager_profile.md
================================================
# routeros_user_manager_profile (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_profile" "test" {
  name           = "test"
  name_for_users = "Test"
  price          = 0.02
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Unique name of the profile.
### Optional
- `name_for_users` (String) The name that will be shown to users in the web interface.
- `override_shared_users` (String) An option whether to allow multiple sessions with the same user name.
- `price` (Number) The price of the profile.
- `starts_when` (String) The time when the profile becomes active (`assigned` - immediately when the profile entry is created, `first-auth` - upon first authentication request).
- `validity` (String) The total amount of time a user can use this profile.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/profile get [print show-ids]]
terraform import routeros_user_manager_profile.test '*1'
```
================================================

File: user_manager_profile_limitation.md
================================================
# routeros_user_manager_profile_limitation (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_limitation" "test" {
  name           = "test"
  download_limit = 1024
  upload_limit   = 1024
  uptime_limit   = "10d"
}
resource "routeros_user_manager_profile" "test" {
  name           = "test"
  name_for_users = "Test"
  price          = 0.02
}
resource "routeros_user_manager_profile_limitation" "weekend_night" {
  limitation = routeros_user_manager_limitation.test.name
  profile    = routeros_user_manager_profile.test.name
  from_time  = "0s"
  till_time  = "6h"
  weekdays = [
    "sunday",
    "saturday",
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `limitation` (String) The limitation name.
- `profile` (String) The profile name.
### Optional
- `from_time` (String) Time of the day when the limitation should take place.
- `till_time` (String) Time of the day when the limitation should end.
- `weekdays` (Set of String) Days of the week when the limitation is active.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/profile-limitation get [print show-ids]]
terraform import routeros_user_manager_profile_limitation.weekend_night '*1'
```
================================================

File: user_manager_router.md
================================================
# routeros_user_manager_router (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_router" "test" {
  address       = "127.0.0.1"
  name          = "test"
  shared_secret = "password"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `address` (String) IP address of the RADIUS client.
- `name` (String) Unique name of the RADIUS client.
### Optional
- `coa_port` (Number) Port number of CoA (Change of Authorization) communication.
- `disabled` (Boolean)
- `shared_secret` (String, Sensitive) The shared secret to secure communication.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/router get [print show-ids]]
terraform import routeros_user_manager_router.test '*1'
```
================================================

File: user_manager_settings.md
================================================
# routeros_user_manager_settings (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_settings" "settings" {
  enabled = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `accounting_port` (Number) Port to listen for RADIUS accounting requests.
- `authentication_port` (Number) Port to listen for RADIUS authentication requests.
- `certificate` (String) Certificate for use in EAP TLS-type authentication methods.
- `enabled` (Boolean) An option whether the User Manager functionality is enabled.
- `require_message_auth` (String) An option whether to require `Message-Authenticator` in received Access-Accept/Challenge/Reject messages.
- `use_profiles` (Boolean) An option whether to use Profiles and Limitations. When set to `false`, only User configuration is required to run User Manager.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_user_manager_settings.settings .
```
================================================

File: user_manager_user.md
================================================
# routeros_user_manager_user (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_attribute" "mikrotik_wireless_comment" {
  name       = "Mikrotik-Wireless-Comment"
  type_id    = 21
  value_type = "string"
}
resource "routeros_user_manager_attribute" "mikrotik_wireless_vlanid" {
  name       = "Mikrotik-Wireless-VLANID"
  type_id    = 26
  value_type = "uint32"
}
resource "routeros_user_manager_user_group" "test" {
  name = "test"
}
resource "routeros_user_manager_user" "test" {
  attributes = [
    "${routeros_user_manager_attribute.mikrotik_wireless_comment.name}:Test Group",
    "${routeros_user_manager_attribute.mikrotik_wireless_vlanid.name}:100",
  ]
  group    = routeros_user_manager_user_group.test.name
  name     = "test"
  password = "password"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Username for session authentication.
### Optional
- `attributes` (List of String) A custom set of colon-separated attributes with their values will be added to `Access-Accept` messages for users in this group.
- `caller_id` (String) Allow user's authentication with a specific Calling-Station-Id value.
- `comment` (String)
- `disabled` (Boolean)
- `group` (String) Name of the group the user is associated with.
- `otp_secret` (String) A token of a one-time code that will be attached to the password.
- `password` (String) The password of the user for session authentication.
- `shared_users` (Number) The total amount of sessions the user can simultaneously establish.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user get [print show-ids]]
terraform import routeros_user_manager_user.test '*1'
```
================================================

File: user_manager_user_group.md
================================================
# routeros_user_manager_user_group (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_attribute" "mikrotik_wireless_comment" {
  name       = "Mikrotik-Wireless-Comment"
  type_id    = 21
  value_type = "string"
}
resource "routeros_user_manager_attribute" "mikrotik_wireless_vlanid" {
  name       = "Mikrotik-Wireless-VLANID"
  type_id    = 26
  value_type = "uint32"
}
resource "routeros_user_manager_user_group" "test" {
  name = "test"
  attributes = [
    "${routeros_user_manager_attribute.mikrotik_wireless_comment.name}:Test Group",
    "${routeros_user_manager_attribute.mikrotik_wireless_vlanid.name}:100",
  ]
  inner_auths = [
    "ttls-chap",
    "ttls-pap",
  ]
  outer_auths = [
    "chap",
    "pap",
  ]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Unique name of the group.
### Optional
- `attributes` (List of String) A custom set of colon-separated attributes with their values will be added to `Access-Accept` messages for users in this group.
- `inner_auths` (Set of String) A set of allowed authentication methods for tunneled authentication methods (`ttls-pap`, `ttls-chap`, `ttls-mschap1`, `ttls-mschap2`, `peap-mschap2`).
- `outer_auths` (Set of String) A set of allowed authentication methods (`pap`, `chap`, `mschap1`, `mschap2`, `eap-tls`, `eap-ttls`, `eap-peap`, `eap-mschap2`).
### Read-Only
- `default` (Boolean)
- `default_name` (String) The default name of the group.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user/group get [print show-ids]]
terraform import routeros_user_manager_user_group.test '*1'
```
================================================

File: user_manager_user_profile.md
================================================
# routeros_user_manager_user_profile (Resource)
## Example Usage
```terraform
resource "routeros_user_manager_profile" "test" {
  name = "test"
}
resource "routeros_user_manager_user" "test" {
  name = "test"
}
resource "routeros_user_manager_user_profile" "test" {
  profile = routeros_user_manager_profile.test.name
  user    = routeros_user_manager_user.test.name
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `profile` (String) Name of the profile to assign to the user.
- `user` (String) Name of the user to use the specified profile.
### Optional
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user-profile get [print show-ids]]
terraform import routeros_user_manager_user_profile.test '*1'
```
================================================

File: vlan.md
================================================
# routeros_vlan (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_vlan](interface_vlan.md)
================================================

File: vrrp.md
================================================
# routeros_vrrp (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_vrrp](interface_vrrp.md)
================================================

File: wifi.md
================================================
# routeros_wifi (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi" "wifi1" {
  configuration = {
    manager = "capsman"
  }
  name = "wifi1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the interface.
### Optional
- `aaa` (Map of String) AAA inline settings.
- `arp` (String) Address Resolution Protocol mode:
		* disabled - the interface will not use ARP
		* enabled - the interface will use ARP
		* local-proxy-arp - the router performs proxy ARP on the interface and sends replies to the same interface
		* proxy-arp - the router performs proxy ARP on the interface and sends replies to other interfaces
		* reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `channel` (Map of String) Channel inline settings.
- `comment` (String)
- `configuration` (Map of String) Configuration inline settings.
- `datapath` (Map of String) Datapath inline settings.
- `disable_running_check` (Boolean) An option to set the running property to true if it is not disabled.
- `disabled` (Boolean)
- `interworking` (Map of String) Interworking inline settings.
- `l2mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `mac_address` (String) MAC address (BSSID) to use for the interface.
- `master_interface` (String) The corresponding master interface of the virtual one.
- `mtu` (Number) Layer3 maximum transmission unit
- `security` (Map of String) Security inline settings.
- `steering` (Map of String) Steering inline settings.
### Read-Only
- `bound` (Boolean) A flag whether the interface is currently available for the WiFi manager.
- `default_name` (String) The interface's default name.
- `id` (String) The ID of this resource.
- `inactive` (Boolean) A flag whether the interface is currently inactive.
- `master` (Boolean) A flag whether the interface is not a virtual one.
- `radio_mac` (String) The MAC address of the associated radio.
- `running` (Boolean) A flag whether the interface has established a link to another device.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi get [print show-ids]]
terraform import routeros_wifi.wifi1 '*1'
```
================================================

File: wifi_aaa.md
================================================
# routeros_wifi_aaa (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_aaa" "aaa1" {
  called_format   = "S"
  name            = "aaa1"
  password_format = ""
  username_format = "AA:AA:AA:AA:AA:AA"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the AAA profile.
### Optional
- `called_format` (String) Format of the `Called-Station-Id` RADIUS attribute.
- `calling_format` (String) Format of the `Calling-Station-Id` RADIUS attribute.
- `comment` (String)
- `disabled` (Boolean)
- `interim_update` (String) Interval at which to send interim updates about traffic accounting to the RADIUS server.
- `mac_caching` (String) Time to cache RADIUS server replies when MAC address authentication is enabled.
- `nas_identifier` (String) Value of the `NAS-Identifier` RADIUS attribute.
- `password_format` (String) Format of the `User-Password` RADIUS attribute.
- `username_format` (String) Format of the `User-Name` RADIUS attribute.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/aaa get [print show-ids]]
terraform import routeros_wifi_aaa.aaa1 '*1'
```
================================================

File: wifi_access_list.md
================================================
# routeros_wifi_access_list (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_access_list" "radius" {
  action            = "query-radius"
  comment           = "RADIUS"
  radius_accounting = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `action` (String) An action to take when a client matches.
- `allow_signal_out_of_range` (String) An option that permits the client's signal to be out of the range always or for some time interval.
- `client_isolation` (Boolean) An option that specifies whether to deny forwarding data between clients connected to the same interface.
- `comment` (String)
- `disabled` (Boolean)
- `interface` (String) Interface name to compare with an interface to which the client actually connects to.
- `mac_address` (String) MAC address of the client.
- `mac_address_mask` (String) MAC address mask to apply when comparing clients' addresses.
- `passphrase` (String) PSK passphrase for the client if some PSK authentication algorithm is used.
- `place_before` (String) Before which position the rule will be inserted.  
	> Please check the effect of this option, as it does not work as you think!  
	> Best way to use in conjunction with a data source. See [example](../data-sources/firewall.md#example-usage).
- `radius_accounting` (Boolean) An option that specifies if RADIUS traffic accounting should be used in case of RADIUS authentication of the client.
- `signal_range` (String) The range in which the client signal must fall.
- `ssid_regexp` (String) The regular expression to compare the actual SSID the client connects to.
- `time` (String) Time of the day and days of the week when the rule is applicable.
- `vlan_id` (String) VLAN ID to use for VLAN tagging or `none`.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/access-list get [print show-ids]]
terraform import routeros_wifi_access_list.radius '*1'
```
================================================

File: wifi_cap.md
================================================
# routeros_wifi_cap (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_cap" "settings" {
  enabled              = true
  discovery_interfaces = ["bridge1"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `caps_man_addresses` (List of String) List of Manager IP addresses that CAP will attempt to contact during discovery.
- `caps_man_certificate_common_names` (List of String) List of manager certificate common names that CAP will connect to.
- `caps_man_names` (List of String) An ordered list of CAPs Manager names that the CAP will connect to.
- `certificate` (String) Certificate to use for authentication.
- `discovery_interfaces` (Set of String) List of interfaces over which CAP should attempt to discover CAPs Manager.
- `enabled` (Boolean) Disable or enable the CAP functionality.
- `lock_to_caps_man` (Boolean) Lock CAP to the first CAPsMAN it connects to.
- `slaves_datapath` (String) Name of the bridge interface the CAP will be added to.
- `slaves_static` (Boolean) An option that creates static virtual interfaces.
### Read-Only
- `current_caps_man_address` (String) Currently used CAPsMAN address.
- `current_caps_man_identity` (String) Currently used CAPsMAN identity.
- `id` (String) The ID of this resource.
- `locked_caps_man_common_name` (String) Common name of the CAPsMAN that the CAP is locked to.
- `requested_certificate` (String) Requested certificate.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_wifi_cap.settings .
```
================================================

File: wifi_capsman.md
================================================
# routeros_wifi_capsman (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_capsman" "settings" {
  enabled        = true
  interfaces     = ["bridge1"]
  upgrade_policy = "suggest-same-version"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `ca_certificate` (String) Device CA certificate.
- `certificate` (String) Device certificate.
- `enabled` (Boolean) Disable or enable CAPsMAN functionality.
- `interfaces` (List of String) List of interfaces on which CAPsMAN will listen for CAP connections.
- `package_path` (String) Folder location for the RouterOS packages. For example, use '/upgrade' to specify the upgrade folder from the files section. If empty string is set, CAPsMAN can use built-in RouterOS packages, note that in this case only CAPs with the same architecture as CAPsMAN will be upgraded.
- `require_peer_certificate` (Boolean) Require all connecting CAPs to have a valid certificate.
- `upgrade_policy` (String) Upgrade policy options.
### Read-Only
- `generated_ca_certificate` (String) Generated CA certificate.
- `generated_certificate` (String) Generated CAPsMAN certificate.
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
terraform import routeros_wifi_capsman.settings .
```
================================================

File: wifi_channel.md
================================================
# routeros_wifi_channel (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_channel" "channel1" {
  name                = "1"
  band                = "2ghz-n"
  frequency           = [2412]
  secondary_frequency = ["disabled"]
  skip_dfs_channels   = "disabled"
  width               = "20mhz"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the channel.
### Optional
- `band` (String) Frequency band and wireless standard that will be used by the AP.
- `comment` (String)
- `disabled` (Boolean)
- `frequency` (List of String) Channel frequency value or range in MHz on which AP or station will operate.
- `reselect_interval` (String) An option that specifies when the interface should rescan channel availability and select the most appropriate one to use.
- `secondary_frequency` (List of String) Specifies the second frequency that will be used for 80+80MHz configuration. Set it to `disabled` in order to disable 80+80MHz capability.
- `skip_dfs_channels` (String) An option to avoid using channels on which channel availability check (listening for the presence of radar signals) is required.
- `width` (String) Channel width.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/channel get [print show-ids]]
terraform import routeros_wifi_channel.channel1 '*1'
```
================================================

File: wifi_configuration.md
================================================
# routeros_wifi_configuration (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_aaa" "aaa1" {
  called_format   = "S"
  name            = "aaa1"
  password_format = ""
  username_format = "AA:AA:AA:AA:AA:AA"
}
resource "routeros_wifi_channel" "channel1" {
  name                = "1"
  band                = "2ghz-n"
  frequency           = [2412]
  secondary_frequency = ["disabled"]
  skip_dfs_channels   = "disabled"
  width               = "20mhz"
}
resource "routeros_wifi_datapath" "datapath1" {
  name             = "datapath1"
  bridge           = "bridge1"
  client_isolation = false
}
resource "routeros_wifi_security" "security1" {
  name                 = "security1"
  authentication_types = ["wpa2-psk", "wpa3-psk"]
  ft                   = true
  ft_preserve_vlanid   = true
  passphrase           = "password"
}
resource "routeros_wifi_configuration" "configuration1" {
  country = "Netherlands"
  manager = "capsman"
  mode    = "ap"
  name    = "configuration1"
  ssid    = "my-network"
  aaa = {
    config = routeros_wifi_aaa.aaa1.name
  }
  channel = {
    config = routeros_wifi_channel.channel1.name
  }
  datapath = {
    config = routeros_wifi_datapath.datapath1.name
  }
  security = {
    config = routeros_wifi_security.security1.name
  }
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the configuration.
### Optional
- `aaa` (Map of String) AAA inline settings.
- `antenna_gain` (Number) An option overrides the default antenna gain.
- `beacon_interval` (String) Time interval between beacon frames.
- `chains` (Set of Number) Radio chains to use for receiving signals.
- `channel` (Map of String) Channel inline settings.
- `comment` (String)
- `country` (String) An option determines which regulatory domain restrictions are applied to an interface.
- `datapath` (Map of String) Datapath inline settings.
- `disabled` (Boolean)
- `dtim_period` (Number) A period at which to transmit multicast traffic, when there are client devices in power save mode connected to the AP.
- `hide_ssid` (Boolean) This property has effect only in AP mode. Setting it to yes can remove this network from the list of wireless networks that are shown by some client software. Changing this setting does not improve the security of the wireless network, because SSID is included in other frames sent by the AP.
- `interworking` (Map of String) Interworking inline settings.
- `manager` (String) An option to specify the remote CAP mode.
- `mode` (String) An option to specify the access point operational mode.
- `multicast_enhance` (String) An option to enable converting every multicast-address IP or IPv6 packet into multiple unicast-addresses frames for each connected station.
- `qos_classifier` (String) An option to specify the QoS classifier.
- `security` (Map of String) Security inline settings.
- `ssid` (String) SSID (service set identifier) is a name broadcast in the beacons that identifies wireless network.
- `steering` (Map of String) Steering inline settings.
- `tx_chains` (Set of Number) Radio chains to use for transmitting signals.
- `tx_power` (Number) A limit on the transmit power (in dBm) of the interface.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/configuration get [print show-ids]]
terraform import routeros_wifi_configuration.configuration1 '*1'
```
================================================

File: wifi_datapath.md
================================================
# routeros_wifi_datapath (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_datapath" "datapath1" {
  name             = "datapath1"
  bridge           = "bridge1"
  client_isolation = false
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the datapath.
### Optional
- `bridge` (String) Bridge interface to add the interface as a bridge port.
- `bridge_cost` (String) Spanning tree protocol cost of the bridge port.
- `bridge_horizon` (String) Bridge horizon to use when adding as a bridge port.
- `client_isolation` (Boolean) An option to toggle communication between clients connected to the same AP.
- `comment` (String)
- `disabled` (Boolean)
- `interface_list` (String) List to which add the interface as a member.
- `vlan_id` (String) Default VLAN ID to assign to client devices connecting to this interface.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/datapath get [print show-ids]]
terraform import routeros_wifi_datapath.datapath1 '*1'
```
================================================

File: wifi_interworking.md
================================================
# routeros_wifi_interworking (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_interworking" "interworking1" {
  name     = "interworking1"
  internet = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the interworking profile.
### Optional
- `3gpp_info` (List of String) Cellular network advertisement information - country and network codes.
- `3gpp_raw` (String) Cellular network advertisement information - country and network codes.
- `asra` (Boolean) An option to enable Additional Steps Required for Access.
- `authentication_types` (List of String) A list of authentication types that is only effective when `asra` is set to yes.
- `comment` (String)
- `connection_capabilities` (List of String) A list to provide information about the allowed IP protocols and ports.
- `disabled` (Boolean)
- `domain_names` (List of String) A list of fully qualified domain names (FQDN) that indicate the entity operating the Hotspot.
- `esr` (Boolean) An option to enable Emergency Services Reachability.
- `hessid` (String) Homogenous extended service set identifier (HESSID).
- `hotspot20` (Boolean) An option to indicate Hotspot 2.0 capability of the Access Point.
- `hotspot20_dgaf` (Boolean) An option to indicate Downstream Group-Addressed Forwarding (DGAF) capability.
- `internet` (Boolean) An option to indicate Internet availability.
- `ipv4_availability` (String) An option to indicate IPv4 availability.
- `ipv6_availability` (String) An option to indicate IPv6 availability.
- `network_type` (String) Information about network access type.
- `operational_classes` (List of Number) A list with information about other available bands.
- `operator_names` (List of String) A list of colon-separated operator names and language codes.
- `realms` (List of String) A list of colon-separated realm names and EAP methods.
- `realms_raw` (List of String) A list of 'NAI Realm Tuple' excluding 'NAI Realm Data Field Length' field.
- `roaming_ois` (List of String) A list of Organization Identifiers (OI).
- `uesa` (Boolean) An option to enable Unauthenticated Emergency Service Accessibility.
- `venue` (String) Information about the venue in which the Access Point is located.
- `venue_names` (List of String) A list of colon-separated venue names and language codes.
- `wan_at_capacity` (Boolean) An option to indicate that the Access Point or the network is at its max capacity.
- `wan_downlink` (Number) The downlink speed of the WAN connection set in kbps.
- `wan_downlink_load` (Number) The downlink load of the WAN connection measured over `wan_measurement_duration`.
- `wan_measurement_duration` (Number) The duration during which `wan_downlink_load` and `wan_uplink_load` are measured.
- `wan_status` (String) Information about the status of the Access Point's WAN connection.
- `wan_symmetric` (Boolean) An option to indicate that the WAN link is symmetric (upload and download speeds are the same).
- `wan_uplink` (Number) The uplink speed of the WAN connection set in kbps.
- `wan_uplink_load` (Number) The uplink load of the WAN connection measured over `wan_measurement_duration`.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/interworking get [print show-ids]]
terraform import routeros_wifi_interworking.interworking1 '*1'
```
================================================

File: wifi_provisioning.md
================================================
# routeros_wifi_provisioning (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_configuration" "configuration1" {
  country = "Netherlands"
  manager = "capsman"
  mode    = "ap"
  name    = "configuration1"
  ssid    = "my-network"
}
resource "routeros_wifi_provisioning" "provisioning1" {
  action               = "create-enabled"
  master_configuration = routeros_wifi_configuration.configuration1.name
  name_format          = "cap1:"
  radio_mac            = "00:11:22:33:44:55"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `action` (String) Provisioning action.
- `address_ranges` (List of String) Match CAPs by IPs within configured address ranges.
- `comment` (String)
- `common_name_regexp` (String) Regular expression to match radios by common name.
- `disabled` (Boolean)
- `identity_regexp` (String) Regular expression to match radios by router identity.
- `master_configuration` (String) If action specifies to create interfaces, then a new master interface with its configuration set to this configuration profile will be created.
- `name_format` (String) Specify the format of the CAP interface name creation.
- `radio_mac` (String) MAC address of radio to be matched, empty MAC (00:00:00:00:00:00) means match all MAC addresses.
- `slave_configurations` (List of String) If action specifies to create interfaces, then a new slave interface for each configuration profile in this list is created.
- `supported_bands` (List of String) Match CAPs by supported modes.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/provisioning get [print show-ids]]
terraform import routeros_wifi_provisioning.provisioning1 '*1'
```
================================================

File: wifi_security.md
================================================
# routeros_wifi_security (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_security" "security1" {
  name                 = "security1"
  authentication_types = ["wpa2-psk", "wpa3-psk"]
  ft                   = true
  ft_preserve_vlanid   = true
  passphrase           = "password"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the security profile.
### Optional
- `authentication_types` (Set of String) Authentication types to enable on the interface.
- `comment` (String)
- `connect_group` (String) APs within the same connect group do not allow more than 1 client device with the same MAC address.
- `connect_priority` (String) An option to determine how a connection is handled if the MAC address of the client device is the same as that of another active connection to another AP.
- `dh_groups` (Set of Number) Identifiers of elliptic curve cryptography groups to use in SAE (WPA3) authentication.
- `disable_pmkid` (Boolean) An option to disable inclusion of a PMKID in EAPOL frames.
- `disabled` (Boolean)
- `eap_accounting` (Boolean) An option to send accounting information to RADIUS server for EAP-authenticated peers.
- `eap_anonymous_identity` (String) An option to specify anonymous identity for EAP outer authentication.
- `eap_certificate_mode` (String) A policy for handling the TLS certificate of the RADIUS server.
- `eap_methods` (Set of String) A set of EAP methods to consider for authentication.
- `eap_password` (String) Password to use when the chosen EAP method requires one.
- `eap_tls_certificate` (String) Name or id of a certificate in the device's certificate store to use when the chosen EAP authentication method requires one.
- `eap_username` (String) Username to use when the chosen EAP method requires one.
- `encryption` (Set of String) A list of ciphers to support for encrypting unicast traffic.
- `ft` (Boolean) An option to enable 802.11r fast BSS transitions (roaming).
- `ft_mobility_domain` (Number) The fast BSS transition mobility domain ID.
- `ft_nas_identifier` (String) Fast BSS transition PMK-R0 key holder identifier.
- `ft_over_ds` (Boolean) An option to enable fast BSS transitions over DS (distributed system).
- `ft_preserve_vlanid` (Boolean) An option to preserve VLAN ID when roaming.
- `ft_r0_key_lifetime` (String) The lifetime of the fast BSS transition PMK-R0 encryption key.
- `ft_reassociation_deadline` (String) Fast BSS transition reassociation deadline.
- `group_encryption` (String) A cipher to use for encrypting multicast traffic.
- `group_key_update` (String) The interval at which the group temporal key (key for encrypting broadcast traffic) is renewed.
- `management_encryption` (String) A cipher to use for encrypting protected management frames.
- `management_protection` (String) An option to enable 802.11w management frame protection.
- `owe_transition_interface` (String) Name or internal ID of an interface which MAC address and SSID to advertise as the matching AP when running in OWE transition mode.
- `passphrase` (String) Passphrase to use for PSK authentication types.
- `sae_anti_clogging_threshold` (String) A parameter to mitigate DoS attacks by specifying a threshold of in-progress SAE authentications.
- `sae_max_failure_rate` (String) Rate of failed SAE (WPA3) associations per minute, at which the AP will stop processing new association requests.
- `sae_pwe` (String) Methods to support for deriving SAE password element.
- `wps` (String) An option to enable WPS (Wi-Fi Protected Setup).
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/security get [print show-ids]]
terraform import routeros_wifi_security.security1 '*1'
```
================================================

File: wifi_steering.md
================================================
# routeros_wifi_steering (Resource)
*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*
## Example Usage
```terraform
resource "routeros_wifi_steering" "steering1" {
  name           = "steering1"
  neighbor_group = ["something"]
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the steering profile.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `neighbor_group` (List of String) Neighbor group of potential roaming candidates.
- `rrm` (Boolean) An option to enable sending 802.11k neighbor reports.
- `wnm` (Boolean) An option to enable sending 802.11v BSS transition management requests.
### Read-Only
- `id` (String) The ID of this resource.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/steering get [print show-ids]]
terraform import routeros_wifi_steering.steering1 '*1'
```
================================================

File: wireguard.md
================================================
# routeros_wireguard (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_wireguard](interface_wireguard.md)
================================================

File: wireguard_keys.md
================================================
# routeros_wireguard_keys (Resource)
Creating key sets for WireGuard tunnels.
## Example Usage
```terraform
resource "routeros_wireguard_keys" "wgk" {
  number = 3
}
output "wg_keys" {
  value     = routeros_wireguard_keys.wgk.keys[*]
  sensitive = true
}
output "wg_key" {
  value = nonsensitive(routeros_wireguard_keys.wgk.keys[1].public)
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Optional
- `number` (Number) The number of key sets.
### Read-Only
- `id` (String) The ID of this resource.
- `keys` (List of Object, Sensitive) (see [below for nested schema](#nestedatt--keys))
<a id="nestedatt--keys"></a>
### Nested Schema for `keys`
Read-Only:
- `preshared` (String)
- `private` (String)
- `public` (String)
================================================

File: wireguard_peer.md
================================================
# routeros_wireguard_peer (Resource)
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_interface_wireguard_peer](interface_wireguard_peer.md)
================================================

File: zerotier.md
================================================
# routeros_zerotier (Resource)
## Example Usage
```terraform
resource "zerotier_identity" "identity" {}
resource "routeros_zerotier" "zt1" {
  comment    = "ZeroTier Central"
  identity   = zerotier_identity.identity.private_key
  interfaces = ["all"]
  name       = "zt1"
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `name` (String) Name of the ZeroTier instance.
### Optional
- `comment` (String)
- `disabled` (Boolean)
- `identity` (String) The 40-bit unique instance address.
- `interfaces` (Set of String) The interfaces to discover ZeroTier peers by ARP and IP type connections.
- `port` (Number) The port number the instance listens to.
- `route_distance` (Number) The route distance for routes obtained from the planet/moon server.
### Read-Only
- `id` (String) The ID of this resource.
- `identity_public` (String) The public identity of the ZeroTier instance.
- `online` (Boolean) A flag whether the ZeroTier instance is currently online.
- `state` (String) The state of the ZeroTier instance.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier get [print show-ids]]
terraform import routeros_zerotier.zt1 '*1'
```
================================================

File: zerotier_controller.md
================================================
# routeros_zerotier_controller (Resource)
## Example Usage
```terraform
resource "zerotier_identity" "identity" {}
resource "routeros_zerotier" "zt1" {
  comment    = "ZeroTier Central"
  identity   = zerotier_identity.identity.private_key
  interfaces = ["all"]
  name       = "zt1"
}
resource "routeros_zerotier_controller" "test" {
  instance = routeros_zerotier.zt1.name
  name     = "test"
  network  = "1234567812345678"
  private  = true
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `instance` (String) The ZeroTier instance name.
- `name` (String) Name of the ZeroTier controller.
- `network` (String) The ZeroTier network identifier.
### Optional
- `broadcast` (Boolean) An option to allow receiving broadcast packets.
- `comment` (String)
- `disabled` (Boolean)
- `ip6_6plane` (Boolean) An option to assign every member a `/80` address within a `/40` network with using NDP emulation.
- `ip6_range` (String) The IPv6 range of the ZeroTier network.
- `ip6_rfc4193` (Boolean) An option to assign every member a `/128` address within a `/88` network.
- `ip_range` (String) The IP range of the ZeroTier network.
- `mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `multicast_limit` (Number) An option to limit the maximum recipients of a multicast packet.
- `private` (Boolean) The ZeroTier network access control.
- `routes` (Set of String) The routes list that will be pushed to the client.
### Read-Only
- `id` (String) The ID of this resource.
- `inactive` (Boolean) A flag whether the ZeroTier network is inactive.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier/controller get [print show-ids]]
terraform import routeros_zerotier_controller.test '*1'
```
================================================

File: zerotier_interface.md
================================================
# routeros_zerotier_interface (Resource)
## Example Usage
```terraform
resource "zerotier_identity" "identity" {}
resource "zerotier_network" "network" {
  name = "test"
}
resource "zerotier_member" "member" {
  authorized              = true
  member_id               = zerotier_identity.identity.id
  name                    = "test"
  network_id              = zerotier_network.network.id
  hidden                  = false
  allow_ethernet_bridging = true
  no_auto_assign_ips      = true
}
resource "routeros_zerotier" "zt1" {
  comment    = "ZeroTier Central"
  identity   = zerotier_identity.identity.private_key
  interfaces = ["all"]
  name       = "zt1"
}
resource "routeros_zerotier_interface" "zerotier1" {
  allow_default = false
  allow_global  = false
  allow_managed = false
  instance      = routeros_zerotier.zt1.name
  name          = "zerotier1"
  network       = zerotier_network.network.id
}
```
<!-- schema generated by tfplugindocs -->
## Schema
### Required
- `instance` (String) The ZeroTier instance name.
- `name` (String) Name of the ZeroTier interface.
- `network` (String) The ZeroTier network identifier.
### Optional
- `allow_default` (Boolean) An option to override the default route.
- `allow_global` (Boolean) An option to allow overlapping public IP space by the ZeroTier routes. .
- `allow_managed` (Boolean) An option to allow assignment of managed IPs.
- `arp_timeout` (String) ARP timeout is time how long ARP record is kept in ARP table after no packets are received from IP. Value auto equals to the value of arp-timeout in IP/Settings, default is 30s. Can use postfix ms, s, M, h, d for milliseconds, seconds, minutes, hours or days. If no postfix is set then seconds (s) is used.
- `comment` (String)
- `disable_running_check` (Boolean) An option to force the `running` property to true.
- `disabled` (Boolean)
### Read-Only
- `bridge` (Boolean) A flag whether the ZeroTier interface is bridged.
- `dhcp` (Boolean) A flag whether the ZeroTier interface obtained an IP address.
- `id` (String) The ID of this resource.
- `mac_address` (String) Current mac address.
- `mtu` (Number) Layer2 Maximum transmission unit. [See](https://wiki.mikrotik.com/wiki/Maximum_Transmission_Unit_on_RouterBoards).
- `network_name` (String) The ZeroTier network name.
- `running` (Boolean)
- `status` (String) The status of the ZeroTier connection.
- `type` (String) The ZeroTier network type.
## Import
Import is supported using the following syntax:
```shell
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier/interface get [print show-ids]]
terraform import routeros_zerotier_interface.zerotier1 '*1'
```
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/bgp/connection get [print show-ids]]
terraform import routeros_bgp_connection.test *3
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/bgp/template get [print show-ids]]
terraform import routeros_bgp_template.test *3
================================================

File: import.sh
================================================
terraform import routeros_ip_cloud.test .
================================================

File: import.sh
================================================
terraform import routeros_capsman_aaa.test_3a .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/access-list get [print show-ids]]
terraform import routeros_capsman_access_list.test_rule "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/channel get [print show-ids]]
terraform import routeros_capsman_channel.test_channel "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/configuration get [print show-ids]]
terraform import routeros_capsman_configuration.test_configuration_2 "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/datapath get [print show-ids]]
terraform import routeros_capsman_datapath.test_datapath "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/interface get [print show-ids]]
terraform import routeros_capsman_interface.cap1 '*1'
================================================

File: import.sh
================================================
terraform import routeros_capsman_manager.test_manager .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is ->  :put [/caps-man/manager/interface get [print show-ids]]
terraform import routeros_capsman_manager_interface.test_manager_interface "*6"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is ->  :put [/caps-man/provisioning get [print show-ids]]
terraform import routeros_capsman_provisioning.test_provisioning "*B"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/rates get [print show-ids]]
terraform import routeros_capsman_rates.test_rates "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/caps-man/security get [print show-ids]]
terraform import routeros_capsman_security.test_security "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container get [print show-ids]]
terraform import routeros_container.busybox "*1"
================================================

File: import.sh
================================================
terraform import routeros_container_config.config .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container/envs get [print show-ids]]
terraform import routeros_container_envs.test_envs "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/container/mounts get [print show-ids]]
terraform import routeros_container_mounts.caddyfile "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/file get [print show-ids]]
terraform import routeros_file.test "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bonding get [print show-ids]]
terraform import routeros_interface_bonding.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge get [print show-ids]]
terraform import routeros_interface_bridge.bridge "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge/port get [print show-ids]]
terraform import routeros_interface_bridge_port.bridge_port "*0"
================================================

File: import.sh
================================================
terraform import routeros_interface_bridge_settings.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/bridge/vlan get [print show-ids]]
terraform import routeros_interface_bridge_vlan.bridge_vlan "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/dot1x/client get [print show-ids]]
terraform import routeros_interface_dot1x_client.ether2 *1
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/dot1x/server get [print show-ids]]
terraform import routeros_interface_dot1x_server.ether2 *1
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/eoip get [print show-ids]]
terraform import routeros_interface_eoip.eoip_tunnel1 *B
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet get [print show-ids]]
terraform import routeros_interface_ethernet.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch get [print show-ids]]
terraform import routeros_interface_ethernet_switch.sw0 *0
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/host get [print show-ids]]
terraform import routeros_interface_ethernet_switch_host.test *0
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/port get [print show-ids]]
terraform import routeros_interface_ethernet_switch_port.test *1
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/port-isolation get [print show-ids]]
terraform import routeros_interface_ethernet_switch_port_isolation.test *1
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/rule get [print show-ids]]
terraform import routeros_interface_ethernet_switch_rule.test *0
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ethernet/switch/vlan get [print show-ids]]
terraform import routeros_interface_ethernet_switch_vlan.test *0
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/gre get [print show-ids]]
terraform import routeros_interface_gre.gre_hq "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ipip get [print show-ids]]
terraform import routeros_interface_ipip.ipip_hq "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/list get [print show-ids]]
terraform import routeros_interface_list.list "*2000010"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/list/member get [print show-ids]]
terraform import routeros_interface_list_member.list_member "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ get [print show-ids]]
terraform import routeros_interface_lte.test *3
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ get [print show-ids]]
terraform import routeros_interface_lte_apn.test *3
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/macvlan get [print show-ids]]
terraform import routeros_interface_macvlan.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/ovpn-server get [print show-ids]]
terraform import routeros_interface_ovpn_server.user1 *29
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/pppoe-client get [print show-ids]]
terraform import routeros_interface_pppoe_client.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/veth get [print show-ids]]
terraform import routeros_interface_veth.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/vlan get [print show-ids]]
terraform import routeros_interface_vlan.interface_vlan "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/vrrp get [print show-ids]]
terraform import routeros_interface_vrrp.interface_vrrp "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wireguard get [print show-ids]]
terraform import routeros_interface_wireguard.test_wg_interface "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wireguard/peers get [print show-ids]]
terraform import routeros_interface_wireguard_peer.wg_peer "*0"
================================================

File: import.sh
================================================
terraform import routeros_interface_wireless_cap.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/address get [print show-ids]]
terraform import routeros_ipv6_address.ipv6_address "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/dhcp-client/  get [print show-ids]]
terraform import routeros_ipv6_dhcp_client.inet_provider "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/dhcp-client/option get [print show-ids]]
terraform import routeros_ipv6_dhcp_client_option.option "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/firewall/address-list get [print show-ids]]
terraform import routeros_ipv6_firewall_addr_list.example_list "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/firewall/filter get [print show-ids]]
terraform import routeros_ipv6_firewall_filter.rule "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/nd get [print show-ids]]
terraform import routeros_ipv6_neighbor_discovery.ndether1 "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ipv6/route get [print show-ids]]
terraform import routeros_ipv6_route.a_route "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/address get [print show-ids]]
terraform import routeros_ip_address.address "*0"
================================================

File: import.sh
================================================
terraform import routeros_ip_cloud.test .
================================================

File: import.sh
================================================
terraform import routeros_ip_cloud_advanced.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-client get [print show-ids]]
terraform import routeros_ip_dhcp_client.client "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-client/option get [print show-ids]]
terraform import routeros_ip_dhcp_client_option.option "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-relay get [print show-ids]]
terraform import routeros_ip_dhcp_relay.relay "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server get [print show-ids]]
terraform import routeros_ip_dhcp_server.server "*1"
================================================

File: import.sh
================================================
terraform import routeros_ip_dhcp_server_config.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/lease get [print show-ids]]
terraform import routeros_ip_dhcp_server_lease.dhcp_lease "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/network get [print show-ids]]
terraform import routeros_ip_dhcp_server_network.dhcp_server_network "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/option/get [print show-ids]]
terraform import routeros_ip_dhcp_server_option.tftp_option "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dhcp-server/option/sets/get [print show-ids]]
terraform import routeros_ip_dhcp_server_option_set.lan_option_set "*1"
================================================

File: import.sh
================================================
#The DNS Settings can not be imported. 
#Terraform will ignore the current settings and will overwrite the current settings with the settings defined in Terraform.
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/dns/static get [print show-ids]]
terraform import routeros_ip_dns_record.name_record "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/address-list get [print show-ids]]
terraform import routeros_ip_firewall_addr_list.example_list "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/filter get [print show-ids]]
terraform import routeros_ip_firewall_filter.rule "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/mangle get [print show-ids]]
terraform import routeros_ip_firewall_mangle.rule "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/firewall/nat get [print show-ids]]
terraform import routeros_ip_firewall_nat.rule "*0"
================================================

File: import.sh
================================================
terraform import routeros_ip_neighbor_discovery_settings.test .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/pool get [print show-ids]]
terraform import routeros_ip_pool.pool "*1"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/route get [print show-ids]]
terraform import routeros_ip_route.a_route "*0"
================================================

File: import.sh
================================================
# Import with the name of the ip service in case of the example use www-ssl
terraform import routeros_ip_service.www_ssl www-ssl
================================================

File: import.sh
================================================
terraform import routeros_ip_ssh_server.test .
================================================

File: import.sh
================================================
terraform import routeros_ip_upnp.test .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/upnp/interfaces get [print show-ids]]
terraform import routeros_ip_upnp_interfaces.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ip/vrf get [print show-ids]]
terraform import routeros_ip_vrf.test_vrf_a "*0"
# or
terraform import routeros_ip_vrf.test_vrf_a "vrf_1"
# or
terraform import routeros_ip_vrf.test_vrf_a `"comment=Custom routing"`
================================================

File: import.sh
================================================
terraform import routeros_openvpn_server.server .
================================================

File: import.sh
================================================
terraform import routeros_ppp_aaa.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ppp/profile get [print show-ids]]
terraform import routeros_ppp_profile.test *6
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/ppp/secret get [print show-ids]]
terraform import routeros_ppp_secret.test *6
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/radius get [print show-ids]]
terraform import routeros_radius.user_manager *1
================================================

File: import.sh
================================================
terraform import routeros_radius_incoming.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/filter/rule/print show-ids
terraform import routeros_routing_filter_rule.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/area/print show-ids
terraform import routeros_routing_ospf_area.test_routing_ospf_area "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/instance/print show-ids
terraform import routeros_routing_ospf_instance.test_routing_ospf_instance "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> /routing/ospf/interface-template/print show-ids
terraform import routeros_routing_ospf_interface_template.test_routing_ospf_interface_template "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/rule get [print show-ids]]
terraform import routeros_routing_rule.test *3
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/routing/table get [print show-ids]]
terraform import routeros_routing_table.test_table "*0"
================================================

File: import.sh
================================================
terraform import routeros_snmp.test .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/snmp/community get [print show-ids]]
terraform import routeros_snmp_community.test "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/certificate get [print show-ids]]
#If you plan to manipulate the certificate requiring signing, you need to correctly fill in the sign{} section.
#Changes in the sign{} section will not cause changes in the certificate. It's not a bug, it's a feature!
terraform import routeros_system_certificate.client *9D
================================================

File: import.sh
================================================
# The ID can be found via API or the terminal
# The command for the terminal is -> /certificate/scep-server/print show-ids
terraform import routeros_system_certificate_scep_server.example_scep_server "*1"
================================================

File: import.sh
================================================
terraform import routeros_system_clock.set .
================================================

File: import.sh
================================================
terraform import routeros_system_identity.identity .
================================================

File: import.sh
================================================
# The ID can be found via API or the terminal
# The command for the terminal is -> :put [/system/logging/print  get [print show-ids]]
terraform import routeros_system_logging.log_snmp_disk "*4"
================================================

File: import.sh
================================================
terraform import routeros_system_ntp_client.test .
================================================

File: import.sh
================================================
terraform import routeros_system_ntp_server.test .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/system/scheduler get [print show-ids]]
terraform import routeros_system_scheduler.schedule1 "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/system/script get [print show-ids]]
terraform import routeros_system_script.script "*0"
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user get [print show-ids]]
terraform import routeros_system_user.test *1
================================================

File: import.sh
================================================
terraform import routeros_system_user_aaa.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user/group get [print show-ids]]
terraform import routeros_system_user_group.terraform *1
================================================

File: import.sh
================================================
terraform import routeros_system_user_settings.settings .
================================================

File: import.sh
================================================
terraform import routeros_tool_bandwidth_server.test .
================================================

File: import.sh
================================================
terraform import routeros_tool_mac_server.test .
================================================

File: import.sh
================================================
terraform import routeros_tool_mac_server_winbox.test .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/tool/netwatch get [print show-ids]]
terraform import routeros_tool_netwatch.test *3
================================================

File: import.sh
================================================
terraform import routeros_user_manager_advanced.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/attribute get [print show-ids]]
terraform routeros_user_manager_attribute.mikrotik_wireless_comment '*1'
================================================

File: import.sh
================================================
terraform import routeros_user_manager_database.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/limitation get [print show-ids]]
terraform import routeros_user_manager_limitation.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/profile get [print show-ids]]
terraform import routeros_user_manager_profile.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/profile-limitation get [print show-ids]]
terraform import routeros_user_manager_profile_limitation.weekend_night '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/router get [print show-ids]]
terraform import routeros_user_manager_router.test '*1'
================================================

File: import.sh
================================================
terraform import routeros_user_manager_settings.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user get [print show-ids]]
terraform import routeros_user_manager_user.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user/group get [print show-ids]]
terraform import routeros_user_manager_user_group.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/user-manager/user-profile get [print show-ids]]
terraform import routeros_user_manager_user_profile.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi get [print show-ids]]
terraform import routeros_wifi.wifi1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/aaa get [print show-ids]]
terraform import routeros_wifi_aaa.aaa1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/access-list get [print show-ids]]
terraform import routeros_wifi_access_list.radius '*1'
================================================

File: import.sh
================================================
terraform import routeros_wifi_cap.settings .
================================================

File: import.sh
================================================
terraform import routeros_wifi_capsman.settings .
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/channel get [print show-ids]]
terraform import routeros_wifi_channel.channel1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/configuration get [print show-ids]]
terraform import routeros_wifi_configuration.configuration1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/datapath get [print show-ids]]
terraform import routeros_wifi_datapath.datapath1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/interworking get [print show-ids]]
terraform import routeros_wifi_interworking.interworking1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/provisioning get [print show-ids]]
terraform import routeros_wifi_provisioning.provisioning1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/security get [print show-ids]]
terraform import routeros_wifi_security.security1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/interface/wifi/steering get [print show-ids]]
terraform import routeros_wifi_steering.steering1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier get [print show-ids]]
terraform import routeros_zerotier.zt1 '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier/controller get [print show-ids]]
terraform import routeros_zerotier_controller.test '*1'
================================================

File: import.sh
================================================
#The ID can be found via API or the terminal
#The command for the terminal is -> :put [/zerotier/interface get [print show-ids]]
terraform import routeros_zerotier_interface.zerotier1 '*1'
================================================

File: LICENSE.md
================================================
Mozilla Public License Version 2.0
==================================
1. Definitions
--------------
1.1. "Contributor"
    means each individual or legal entity that creates, contributes to
    the creation of, or owns Covered Software.
1.2. "Contributor Version"
    means the combination of the Contributions of others (if any) used
    by a Contributor and that particular Contributor's Contribution.
1.3. "Contribution"
    means Covered Software of a particular Contributor.
1.4. "Covered Software"
    means Source Code Form to which the initial Contributor has attached
    the notice in Exhibit A, the Executable Form of such Source Code
    Form, and Modifications of such Source Code Form, in each case
    including portions thereof.
1.5. "Incompatible With Secondary Licenses"
    means
    (a) that the initial Contributor has attached the notice described
        in Exhibit B to the Covered Software; or
    (b) that the Covered Software was made available under the terms of
        version 1.1 or earlier of the License, but not also under the
        terms of a Secondary License.
1.6. "Executable Form"
    means any form of the work other than Source Code Form.
1.7. "Larger Work"
    means a work that combines Covered Software with other material, in
    a separate file or files, that is not Covered Software.
1.8. "License"
    means this document.
1.9. "Licensable"
    means having the right to grant, to the maximum extent possible,
    whether at the time of the initial grant or subsequently, any and
    all of the rights conveyed by this License.
1.10. "Modifications"
    means any of the following:
    (a) any file in Source Code Form that results from an addition to,
        deletion from, or modification of the contents of Covered
        Software; or
    (b) any new file in Source Code Form that contains any Covered
        Software.
1.11. "Patent Claims" of a Contributor
    means any patent claim(s), including without limitation, method,
    process, and apparatus claims, in any patent Licensable by such
    Contributor that would be infringed, but for the grant of the
    License, by the making, using, selling, offering for sale, having
    made, import, or transfer of either its Contributions or its
    Contributor Version.
1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU
    Lesser General Public License, Version 2.1, the GNU Affero General
    Public License, Version 3.0, or any later versions of those
    licenses.
1.13. "Source Code Form"
    means the form of the work preferred for making modifications.
1.14. "You" (or "Your")
    means an individual or a legal entity exercising rights under this
    License. For legal entities, "You" includes any entity that
    controls, is controlled by, or is under common control with You. For
    purposes of this definition, "control" means (a) the power, direct
    or indirect, to cause the direction or management of such entity,
    whether by contract or otherwise, or (b) ownership of more than
    fifty percent (50%) of the outstanding shares or beneficial
    ownership of such entity.
2. License Grants and Conditions
--------------------------------
2.1. Grants
Each Contributor hereby grants You a world-wide, royalty-free,
non-exclusive license:
(a) under intellectual property rights (other than patent or trademark)
    Licensable by such Contributor to use, reproduce, make available,
    modify, display, perform, distribute, and otherwise exploit its
    Contributions, either on an unmodified basis, with Modifications, or
    as part of a Larger Work; and
(b) under Patent Claims of such Contributor to make, use, sell, offer
    for sale, have made, import, and otherwise transfer either its
    Contributions or its Contributor Version.
2.2. Effective Date
The licenses granted in Section 2.1 with respect to any Contribution
become effective for each Contribution on the date the Contributor first
distributes such Contribution.
2.3. Limitations on Grant Scope
The licenses granted in this Section 2 are the only rights granted under
this License. No additional rights or licenses will be implied from the
distribution or licensing of Covered Software under this License.
Notwithstanding Section 2.1(b) above, no patent license is granted by a
Contributor:
(a) for any code that a Contributor has removed from Covered Software;
    or
(b) for infringements caused by: (i) Your and any other third party's
    modifications of Covered Software, or (ii) the combination of its
    Contributions with other software (except as part of its Contributor
    Version); or
(c) under Patent Claims infringed by Covered Software in the absence of
    its Contributions.
This License does not grant any rights in the trademarks, service marks,
or logos of any Contributor (except as may be necessary to comply with
the notice requirements in Section 3.4).
2.4. Subsequent Licenses
No Contributor makes additional grants as a result of Your choice to
distribute the Covered Software under a subsequent version of this
License (see Section 10.2) or under the terms of a Secondary License (if
permitted under the terms of Section 3.3).
2.5. Representation
Each Contributor represents that the Contributor believes its
Contributions are its original creation(s) or it has sufficient rights
to grant the rights to its Contributions conveyed by this License.
2.6. Fair Use
This License is not intended to limit any rights You have under
applicable copyright doctrines of fair use, fair dealing, or other
equivalents.
2.7. Conditions
Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted
in Section 2.1.
3. Responsibilities
-------------------
3.1. Distribution of Source Form
All distribution of Covered Software in Source Code Form, including any
Modifications that You create or to which You contribute, must be under
the terms of this License. You must inform recipients that the Source
Code Form of the Covered Software is governed by the terms of this
License, and how they can obtain a copy of this License. You may not
attempt to alter or restrict the recipients' rights in the Source Code
Form.
3.2. Distribution of Executable Form
If You distribute Covered Software in Executable Form then:
(a) such Covered Software must also be made available in Source Code
    Form, as described in Section 3.1, and You must inform recipients of
    the Executable Form how they can obtain a copy of such Source Code
    Form by reasonable means in a timely manner, at a charge no more
    than the cost of distribution to the recipient; and
(b) You may distribute such Executable Form under the terms of this
    License, or sublicense it under different terms, provided that the
    license for the Executable Form does not attempt to limit or alter
    the recipients' rights in the Source Code Form under this License.
3.3. Distribution of a Larger Work
You may create and distribute a Larger Work under terms of Your choice,
provided that You also comply with the requirements of this License for
the Covered Software. If the Larger Work is a combination of Covered
Software with a work governed by one or more Secondary Licenses, and the
Covered Software is not Incompatible With Secondary Licenses, this
License permits You to additionally distribute such Covered Software
under the terms of such Secondary License(s), so that the recipient of
the Larger Work may, at their option, further distribute the Covered
Software under the terms of either this License or such Secondary
License(s).
3.4. Notices
You may not remove or alter the substance of any license notices
(including copyright notices, patent notices, disclaimers of warranty,
or limitations of liability) contained within the Source Code Form of
the Covered Software, except that You may alter any license notices to
the extent required to remedy known factual inaccuracies.
3.5. Application of Additional Terms
You may choose to offer, and to charge a fee for, warranty, support,
indemnity or liability obligations to one or more recipients of Covered
Software. However, You may do so only on Your own behalf, and not on
behalf of any Contributor. You must make it absolutely clear that any
such warranty, support, indemnity, or liability obligation is offered by
You alone, and You hereby agree to indemnify every Contributor for any
liability incurred by such Contributor as a result of warranty, support,
indemnity or liability terms You offer. You may include additional
disclaimers of warranty and limitations of liability specific to any
jurisdiction.
4. Inability to Comply Due to Statute or Regulation
---------------------------------------------------
If it is impossible for You to comply with any of the terms of this
License with respect to some or all of the Covered Software due to
statute, judicial order, or regulation then You must: (a) comply with
the terms of this License to the maximum extent possible; and (b)
describe the limitations and the code they affect. Such description must
be placed in a text file included with all distributions of the Covered
Software under this License. Except to the extent prohibited by statute
or regulation, such description must be sufficiently detailed for a
recipient of ordinary skill to be able to understand it.
5. Termination
--------------
5.1. The rights granted under this License will terminate automatically
if You fail to comply with any of its terms. However, if You become
compliant, then the rights granted under this License from a particular
Contributor are reinstated (a) provisionally, unless and until such
Contributor explicitly and finally terminates Your grants, and (b) on an
ongoing basis, if such Contributor fails to notify You of the
non-compliance by some reasonable means prior to 60 days after You have
come back into compliance. Moreover, Your grants from a particular
Contributor are reinstated on an ongoing basis if such Contributor
notifies You of the non-compliance by some reasonable means, this is the
first time You have received notice of non-compliance with this License
from such Contributor, and You become compliant prior to 30 days after
Your receipt of the notice.
5.2. If You initiate litigation against any entity by asserting a patent
infringement claim (excluding declaratory judgment actions,
counter-claims, and cross-claims) alleging that a Contributor Version
directly or indirectly infringes any patent, then the rights granted to
You by any and all Contributors for the Covered Software under Section
2.1 of this License shall terminate.
5.3. In the event of termination under Sections 5.1 or 5.2 above, all
end user license agreements (excluding distributors and resellers) which
have been validly granted by You or Your distributors under this License
prior to termination shall survive termination.
************************************************************************
*                                                                      *
*  6. Disclaimer of Warranty                                           *
*  -------------------------                                           *
*                                                                      *
*  Covered Software is provided under this License on an "as is"       *
*  basis, without warranty of any kind, either expressed, implied, or  *
*  statutory, including, without limitation, warranties that the       *
*  Covered Software is free of defects, merchantable, fit for a        *
*  particular purpose or non-infringing. The entire risk as to the     *
*  quality and performance of the Covered Software is with You.        *
*  Should any Covered Software prove defective in any respect, You     *
*  (not any Contributor) assume the cost of any necessary servicing,   *
*  repair, or correction. This disclaimer of warranty constitutes an   *
*  essential part of this License. No use of any Covered Software is   *
*  authorized under this License except under this disclaimer.         *
*                                                                      *
************************************************************************
************************************************************************
*                                                                      *
*  7. Limitation of Liability                                          *
*  --------------------------                                          *
*                                                                      *
*  Under no circumstances and under no legal theory, whether tort      *
*  (including negligence), contract, or otherwise, shall any           *
*  Contributor, or anyone who distributes Covered Software as          *
*  permitted above, be liable to You for any direct, indirect,         *
*  special, incidental, or consequential damages of any character      *
*  including, without limitation, damages for lost profits, loss of    *
*  goodwill, work stoppage, computer failure or malfunction, or any    *
*  and all other commercial damages or losses, even if such party      *
*  shall have been informed of the possibility of such damages. This   *
*  limitation of liability shall not apply to liability for death or   *
*  personal injury resulting from such party's negligence to the       *
*  extent applicable law prohibits such limitation. Some               *
*  jurisdictions do not allow the exclusion or limitation of           *
*  incidental or consequential damages, so this exclusion and          *
*  limitation may not apply to You.                                    *
*                                                                      *
************************************************************************
8. Litigation
-------------
Any litigation relating to this License may be brought only in the
courts of a jurisdiction where the defendant maintains its principal
place of business and such litigation shall be governed by laws of that
jurisdiction, without reference to its conflict-of-law provisions.
Nothing in this Section shall prevent a party's ability to bring
cross-claims or counter-claims.
9. Miscellaneous
----------------
This License represents the complete agreement concerning the subject
matter hereof. If any provision of this License is held to be
unenforceable, such provision shall be reformed only to the extent
necessary to make it enforceable. Any law or regulation which provides
that the language of a contract shall be construed against the drafter
shall not be used to construe this License against a Contributor.
10. Versions of the License
---------------------------
10.1. New Versions
Mozilla Foundation is the license steward. Except as provided in Section
10.3, no one other than the license steward has the right to modify or
publish new versions of this License. Each version will be given a
distinguishing version number.
10.2. Effect of New Versions
You may distribute the Covered Software under the terms of the version
of the License under which You originally received the Covered Software,
or under the terms of any subsequent version published by the license
steward.
10.3. Modified Versions
If you create software not governed by this License, and you want to
create a new license for such software, you may create and use a
modified version of this License if you rename the license and remove
any references to the name of the license steward (except to note that
such modified license differs from this License).
10.4. Distributing Source Code Form that is Incompatible With Secondary
Licenses
If You choose to distribute Source Code Form that is Incompatible With
Secondary Licenses under the terms of this version of the License, the
notice described in Exhibit B of this License must be attached.
Exhibit A - Source Code Form License Notice
-------------------------------------------
  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.
If it is not possible or desirable to put the notice in a particular
file, then You may include the notice in a location (such as a LICENSE
file in a relevant directory) where a recipient would be likely to look
for such a notice.
You may add additional accurate notices of copyright ownership.
Exhibit B - "Incompatible With Secondary Licenses" Notice
---------------------------------------------------------
  This Source Code Form is "Incompatible With Secondary Licenses", as
  defined by the Mozilla Public License, v. 2.0.
================================================

File: package.json
================================================
{
    "name": "terraform-provider-routeros",
    "version": "1.59.3",
    "repository": {
        "type": "git",
        "url": "https://github.com/terraform-routeros/terraform-provider-routeros"
    },
    "dependencies": {
        "@semantic-release/changelog": "^6.0.2",
        "@semantic-release/commit-analyzer": "^9.0.2",
        "@semantic-release/exec": "^6.0.3",
        "@semantic-release/git": "^10.0.1",
        "@semantic-release/github": "^8.0.7",
        "conventional-changelog-conventionalcommits": "^5.0.0"
    },
    "devDependencies": {
        "semantic-release": "^19.0.5"
    }
}
================================================

File: README.md
================================================
# Terraform Provider RouterOS
![module testing workflow](https://github.com/GNewbury1/terraform-provider-routeros/actions/workflows/release.yml/badge.svg?branch=main)
**Note**: In release 1.43, the resource schemas have been changed:
* `routeros_routing_bgp_connection`
* `routeros_ipv6_neighbor_discovery`
* `routeros_interface_wireguard_peer`
For the first two to work correctly, you must remove the resource state (`terraform state rm <name>`) and import it again (`terraform import [options] <name> <id>`).
## Purpose
This provider allows you to configure Mikrotik routers using [old API](https://help.mikrotik.com/docs/display/ROS/API) or [REST API](https://help.mikrotik.com/docs/display/ROS/REST+API), using or not using TLS.
Compatibility testing is only performed within ROS version 7.x.
From version 1.0.0, the provider has been rewritten by [vaerh](https://github.com/vaerh), and their [fork](https://github.com/vaerh/terraform-provider-routeros) has now been merged. This version drastically improves adding new endpoints to the provider, enabling significantly easier development. [vaerh](https://github.com/vaerh) has been added as a maintainer to this project.
_We are not affiliated in any way with Mikrotik or the development of RouterOS_
## Using the provider
To get started with the provider, you first need to enable the REST API on your router. [You can follow the Mikrotik documentation on this](https://help.mikrotik.com/docs/display/ROS/REST+API), but the gist is to create an SSL cert (in `/system/certificates`) and enable the `web-ssl` service (in `/ip/services`) which uses that certificate. After that, include the following in your Terraform manifests:
```terraform
terraform {
  required_providers {
    routeros = {
      source = "terraform-routeros/routeros"
    }
  }
}
provider "routeros" {
  hosturl  = "(http|https|api|apis)://my.router.local[:port]"
  username = "my_username"
  password = "my_super_secret_password"
}
```
For more in-depth documentation about each of the resources and datasources, please read the [documentation on Hashicorp's Provider registry](https://registry.terraform.io/providers/terraform-routeros/routeros/latest/docs)
### Versions tested
- go 1.21 and ROS 7.12, 7.13, 7.14 (stable)
## Changelog
For a detailed changelog, please see the [changelog.md](CHANGELOG.md).
## Contributing
This version of the module greatly simplifies the process of adding new resources.
You are welcome!
================================================

File: mikrotik.go
================================================
package routeros
type TransportType int
// Using numbering from 1 to control type values.
const (
	TransportAPI TransportType = 1 + iota
	TransportREST
)
type IdType int
const (
	Id IdType = 1 + iota
	Name
	// ... and maybe ssh?!
)
type ItemId struct {
	Type  IdType
	Value string
}
func (t IdType) String() string {
	switch t {
	case Id:
		return ".id"
	case Name:
		return "name"
	}
	return "error: undefined id type"
}
// MikrotikItemMetadata This information must travel from the schema to the resource polling function.
type MikrotikItemMetadata struct {
	IdType IdType            // The field contains ID.
	Path   string            // Resource URL.
	Meta   map[string]string // Additional metadata that may be present in the schema.
}
// MikrotikItem Contains only data.
type MikrotikItem map[string]string
func (m MikrotikItem) GetID(t IdType) string {
	switch t {
	case Id:
		// REST
		if id, ok := m[".id"]; ok {
			return id
		}
		// API
		if id, ok := m["ret"]; ok {
			return id
		}
	case Name:
		if id, ok := m["name"]; ok {
			return id
		}
	default:
		panic("[MikrotikItem.GetID] wrong IdType")
	}
	return ""
}
// KebabToSnake Convert Mikrotik JSON names to TF schema names: some-filed to some_field.
func KebabToSnake(name string) string {
	res := []byte(name)
	for i := range res {
		if res[i] == '-' {
			res[i] = '_'
		}
	}
	return string(res)
}
// SnakeToKebab Convert IF schema names to Mikrotik JSON names: some_filed to some-field.
func SnakeToKebab(name string) string {
	res := []byte(name)
	for i := range res {
		if res[i] == '_' {
			res[i] = '-'
		}
	}
	return string(res)
}
func BoolToMikrotikJSON(b bool) string {
	if b {
		return "yes"
	}
	return "no"
}
func BoolFromMikrotikJSON(s string) bool {
	if s == "true" || s == "yes" {
		return true
	}
	return false
}
// Map helpers.
func BoolToMikrotikJSONStr(s string) string {
	if s == "true" {
		return "yes"
	}
	if s == "false" {
		return "no"
	}
	return s
}
func BoolFromMikrotikJSONStr(s string) string {
	if s == "yes" {
		return "true"
	}
	if s == "no" {
		return "false"
	}
	return s
}
================================================

File: mikrotik_client.go
================================================
package routeros
import (
	"context"
	"crypto/tls"
	"crypto/x509"
	"encoding/hex"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
	"github.com/go-routeros/routeros"
	"github.com/hashicorp/terraform-plugin-log/tflog"
	"github.com/hashicorp/terraform-plugin-sdk/v2/diag"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)
type Client interface {
	GetTransport() TransportType
	SendRequest(method crudMethod, url *URL, item MikrotikItem, result interface{}) error
}
type crudMethod int
const (
	crudCreate crudMethod = iota
	crudRead
	crudUpdate
	crudDelete
	crudPost
	crudImport
	crudSign
	crudSignViaScep
	crudRemove
	crudRevoke
	crudMove
	crudStart
	crudStop
)
func NewClient(ctx context.Context, d *schema.ResourceData) (interface{}, diag.Diagnostics) {
	tlsConf := tls.Config{
		InsecureSkipVerify: d.Get("insecure").(bool),
	}
	caCertificate := d.Get("ca_certificate").(string)
	if tlsConf.InsecureSkipVerify && caCertificate != "" {
		return nil, diag.Errorf("You have selected mutually exclusive options: " +
			"ca_certificate and insecure connection. Please check the ENV variables and TF files.")
	}
	if caCertificate != "" {
		if _, err := os.Stat(caCertificate); err != nil {
			tflog.Debug(ctx, "Failed to read CA file '"+caCertificate+"', error: "+err.Error())
			return nil, diag.FromErr(err)
		}
		certPool := x509.NewCertPool()
		file, err := os.ReadFile(caCertificate)
		if err != nil {
			tflog.Debug(ctx, "Failed to read CA file '"+caCertificate+"', error: "+err.Error())
			return nil, diag.Errorf("Failed to read CA file '%s', %v", caCertificate, err)
		}
		certPool.AppendCertsFromPEM(file)
		tlsConf.RootCAs = certPool
	}
	routerUrl, err := url.Parse(d.Get("hosturl").(string))
	if err != nil || routerUrl.Host == "" {
		routerUrl, err = url.Parse("https://" + d.Get("hosturl").(string))
	}
	if err != nil {
		return nil, diag.Diagnostics{
			{
				Severity: diag.Error,
				Summary:  err.Error(),
				Detail:   "Error while parsing the router URL: '" + d.Get("hosturl").(string) + "'",
			},
		}
	}
	routerUrl.Path = strings.TrimSuffix(routerUrl.Path, "/")
	var useTLS = true
	var transport = TransportREST
	// Parse URL.
	switch routerUrl.Scheme {
	case "http":
	case "https":
	case "apis":
		routerUrl.Scheme = ""
		if routerUrl.Port() == "" {
			routerUrl.Host += ":8729"
		}
		transport = TransportAPI
	case "api":
		routerUrl.Scheme = ""
		if routerUrl.Port() == "" {
			routerUrl.Host += ":8728"
		}
		useTLS = false
		transport = TransportAPI
	default:
		panic("[NewClient] wrong transport type: " + routerUrl.Scheme)
	}
	if transport == TransportAPI {
		api := &ApiClient{
			ctx:       ctx,
			HostURL:   routerUrl.Host,
			Username:  d.Get("username").(string),
			Password:  d.Get("password").(string),
			Transport: TransportAPI,
		}
		if useTLS {
			api.Client, err = routeros.DialTLS(api.HostURL, api.Username, api.Password, &tlsConf)
		} else {
			api.Client, err = routeros.Dial(api.HostURL, api.Username, api.Password)
		}
		if err != nil {
			return nil, diag.FromErr(err)
		}
		// The synchronous client has an infinite wait issue
		// when an error occurs while creating multiple resources.
		api.Async()
		return api, nil
	}
	rest := &RestClient{
		ctx:       ctx,
		HostURL:   routerUrl.String(),
		Username:  d.Get("username").(string),
		Password:  d.Get("password").(string),
		Transport: TransportREST,
	}
	rest.Client = &http.Client{
		Timeout: time.Minute,
		Transport: &http.Transport{
			TLSClientConfig: &tlsConf,
		},
	}
	return rest, nil
}
type URL struct {
	Path  string   // URL path without '/rest'.
	Query []string // Query values.
}
// GetApiCmd Returns the set of commands for the API client.
func (u *URL) GetApiCmd() []string {
	res := []string{u.Path}
	//if len(u.Query) > 0 && u.Query[len(u.Query) - 1] != "?#|" {
	//	u.Query = append(u.Query, "?#|")
	//}
	return append(res, u.Query...)
}
// GetRestURL Returns the URL for the client
func (u *URL) GetRestURL() string {
	q := strings.Join(u.Query, "&")
	if len(q) > 0 && q[0] != '?' {
		q = "?" + q
	}
	return u.Path + q
}
// EscapeChars peterGo https://groups.google.com/g/golang-nuts/c/NiQiAahnl5E/m/U60Sm1of-_YJ
func EscapeChars(data []byte) []byte {
	var u = []byte(`\u0000`)
	//var u = []byte(`U+0000`)
	var res = make([]byte, 0, len(data))
	for i, ch := range data {
		if ch < 0x20 {
			res = append(res, u...)
			hex.Encode(res[len(res)-2:], data[i:i+1])
			continue
		}
		res = append(res, ch)
	}
	return res
}
================================================

File: mikrotik_client_api.go
================================================
package routeros
import (
	"context"
	"fmt"
	"reflect"
	"strings"
	"github.com/go-routeros/routeros"
)
type ApiClient struct {
	ctx       context.Context
	HostURL   string
	Username  string
	Password  string
	Transport TransportType
	*routeros.Client
}
var (
	apiMethodName = map[crudMethod]string{
		crudCreate:      "/add",
		crudRead:        "/print",
		crudUpdate:      "/set",
		crudDelete:      "/remove",
		crudPost:        "/set",
		crudImport:      "/import",
		crudSign:        "/sign",
		crudSignViaScep: "/add-scep",
		crudRemove:      "/remove",
		crudRevoke:      "/issued-revoke",
		crudMove:        "/move",
		crudStart:       "/start",
		crudStop:        "/stop",
	}
)
func (c *ApiClient) GetTransport() TransportType {
	return c.Transport
}
func (c *ApiClient) SendRequest(method crudMethod, url *URL, item MikrotikItem, result interface{}) error {
	// https://help.mikrotik.com/docs/display/ROS/API
	// /interface/vlan/print + '?.id=*39' + '?type=vlan'
	cmd := url.GetApiCmd()
	// The first element is the Path
	cmd[0] += apiMethodName[method]
	// Marshal
	for fieldName, fieldValue := range item {
		cmd = append(cmd, fmt.Sprintf("=%s=%s", fieldName, fieldValue))
	}
	ColorizedDebug(c.ctx, "request body:  "+strings.Join(cmd, " "))
	resp, err := c.RunArgs(cmd)
	if err != nil {
		return err
	}
	ColorizedDebug(c.ctx, "response body: "+resp.String())
	if result == nil {
		return nil
	}
	// Unmarshal
	switch r := result.(type) {
	case *MikrotikItem:
		// Only ID returned.
		// !done @ [{`ret` `*7F`}]
		if len(resp.Re) == 0 {
			for k, v := range resp.Done.Map {
				(*r)[k] = v
			}
			break
		}
		// Fill in only one item.
		for k, v := range resp.Re[0].Map {
			(*r)[k] = v
		}
	case *[]MikrotikItem:
		// !re
		for _, sentence := range resp.Re {
			m := MikrotikItem{}
			for k, v := range sentence.Map {
				m[k] = v
			}
			*r = append(*r, m)
		}
		// !done @ [] is empty...
	default:
		panic("[SendRequest] type " + reflect.TypeOf(result).String() + " is not supported for API response unmarshaling.")
	}
	return nil
}
================================================

File: mikrotik_client_rest.go
================================================
package routeros
import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
)
type RestClient struct {
	ctx       context.Context
	HostURL   string
	Username  string
	Password  string
	Transport TransportType
	*http.Client
}
type errorResponse struct {
	Detail  string `json:"detail"`
	Error   int    `json:"error"`
	Message string `json:"message"`
}
var (
	restMethodName = map[crudMethod]string{
		crudCreate:      "PUT",
		crudRead:        "GET",
		crudUpdate:      "PATCH",
		crudDelete:      "DELETE",
		crudPost:        "POST",
		crudImport:      "POST",
		crudSign:        "POST",
		crudSignViaScep: "POST",
		crudRemove:      "POST",
		crudRevoke:      "POST",
		crudMove:        "POST",
		crudStart:       "POST",
		crudStop:        "POST",
	}
)
func (c *RestClient) GetTransport() TransportType {
	return c.Transport
}
func (c *RestClient) SendRequest(method crudMethod, url *URL, item MikrotikItem, result interface{}) error {
	var data io.Reader
	if item != nil {
		b, err := json.Marshal(&item)
		if err != nil {
			return err
		}
		ColorizedDebug(c.ctx, "request body:  "+string(b))
		data = bytes.NewBuffer(b)
	}
	// https://mikrotik + /rest + /interface/vlan + ? + .id=*39
	// Escaping spaces!
	requestUrl := c.HostURL + "/rest" + strings.Replace(url.GetRestURL(), " ", "%20", -1)
	ColorizedDebug(c.ctx, restMethodName[method]+" request URL:  "+requestUrl)
	req, err := http.NewRequest(restMethodName[method], requestUrl, data)
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", "application/json")
	req.SetBasicAuth(c.Username, c.Password)
	res, err := c.Do(req)
	if err != nil {
		return err
	}
	defer func() { _ = res.Body.Close() }()
	body, _ := io.ReadAll(res.Body)
	if res.StatusCode < http.StatusOK || res.StatusCode >= http.StatusBadRequest {
		var errRes errorResponse
		ColorizedDebug(c.ctx, fmt.Sprintf("error response body:\n%s", body))
		if err = json.Unmarshal(body, &errRes); err != nil {
			return fmt.Errorf("json.Unmarshal - %v", err)
		} else {
			return fmt.Errorf("%v '%v' returned response code: %v, message: '%v', details: '%v'",
				restMethodName[method], requestUrl, res.StatusCode, errRes.Message, errRes.Detail)
		}
	}
	ColorizedDebug(c.ctx, "response body: "+string(body))
	if len(body) != 0 && result != nil {
		if err = json.Unmarshal(body, &result); err != nil {
			if e, ok := err.(*json.SyntaxError); ok {
				ColorizedDebug(c.ctx, fmt.Sprintf("json.Unmarshal(response body): syntax error at byte offset %d", e.Offset))
				if err = json.Unmarshal(EscapeChars(body), &result); err != nil {
					return fmt.Errorf("json.Unmarshal(response body): %v", err)
				}
			} else {
				return err
			}
		}
	}
	return nil
}
================================================

File: mikrotik_client_transport_test.go
================================================
package routeros
import (
	"context"
	"crypto/tls"
	"fmt"
	"github.com/go-routeros/routeros"
	"net/http"
	"os"
	"testing"
	"time"
)
func newApiClient(ctx context.Context, hostUrl, user, pass string, useTLS bool) (*ApiClient, error) {
	api := &ApiClient{
		ctx:       ctx,
		HostURL:   hostUrl,
		Username:  user,
		Password:  pass,
		Transport: TransportAPI,
	}
	tlsConf := tls.Config{
		InsecureSkipVerify: true,
	}
	var err error
	if useTLS {
		api.Client, err = routeros.DialTLS(api.HostURL, api.Username, api.Password, &tlsConf)
	} else {
		api.Client, err = routeros.Dial(api.HostURL, api.Username, api.Password)
	}
	if err != nil {
		return nil, err
	}
	api.Async()
	return api, nil
}
func newRestClient(ctx context.Context, hostUrl, user, pass string) *RestClient {
	return &RestClient{
		ctx:       ctx,
		HostURL:   hostUrl,
		Username:  user,
		Password:  pass,
		Transport: TransportREST,
		Client: &http.Client{
			Timeout: time.Minute,
			Transport: &http.Transport{
				TLSClientConfig: &tls.Config{
					InsecureSkipVerify: true,
				},
			},
		},
	}
}
func TestClientTransport_SendRequest(t *testing.T) {
	testAccPreCheck(t)
	ctx := context.Background()
	host := reHost.FindStringSubmatch(os.Getenv("ROS_HOSTURL"))[1]
	user := os.Getenv("ROS_USERNAME")
	pass := os.Getenv("ROS_PASSWORD")
	api, err := newApiClient(ctx, host+":8728", user, pass, false)
	if err != nil {
		t.Fatal(err)
	}
	apis, err := newApiClient(ctx, host+":8729", user, pass, true)
	if err != nil {
		t.Fatal(err)
	}
	rest := newRestClient(ctx, "https://"+host+":443", user, pass)
	type fields struct {
		Transport TransportType
		Client    interface{}
	}
	type args struct {
		method crudMethod
		url    *URL
		item   MikrotikItem
		result interface{}
	}
	tests := []struct {
		name    string
		fields  fields
		args    args
		wantErr bool
	}{
		{
			name:    "Test API connection",
			fields:  fields{TransportAPI, api},
			args:    args{crudRead, &URL{Path: "/system/resource"}, nil, &[]MikrotikItem{}},
			wantErr: false,
		},
		{
			name:    "Test APIs connection",
			fields:  fields{TransportAPI, apis},
			args:    args{crudRead, &URL{Path: "/system/resource"}, nil, &[]MikrotikItem{}},
			wantErr: false,
		},
		{
			name:    "Test REST connection",
			fields:  fields{TransportREST, rest},
			args:    args{crudRead, &URL{Path: "/system/resource"}, nil, &MikrotikItem{}},
			wantErr: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := tt.fields.Client.(Client)
			if err := c.SendRequest(tt.args.method, tt.args.url, tt.args.item, tt.args.result); (err != nil) != tt.wantErr {
				t.Fatalf("SendRequest() error = %v, wantErr %v", err, tt.wantErr)
			}
			var info MikrotikItem
			if tt.fields.Transport == TransportAPI {
				if len(*tt.args.result.(*[]MikrotikItem)) == 0 {
					t.Fatalf("Response is empty.")
				}
				info = (*tt.args.result.(*[]MikrotikItem))[0]
			} else {
				info = *tt.args.result.(*MikrotikItem)
			}
			fmt.Printf("\t\t::: %v %v, RouterOS: %v at %v :::\n", info["platform"], info["board-name"], info["version"], info["build-time"])
		})
	}
}
================================================

File: mikrotik_crud.go
================================================
package routeros
import (
	"fmt"
)
// resource path is '/interface/vlan' etc.
// resource query is '/id' or '?.id=*39'.
var (
	errEmptyId   = fmt.Errorf("the resource id not defined")
	errEmptyItem = fmt.Errorf("the item is null")
	errEmptyPath = fmt.Errorf("the resource path not defined")
)
// https://help.mikrotik.com/docs/display/ROS/REST+API
func CreateItem(item MikrotikItem, resourcePath string, c Client) (MikrotikItem, error) {
	if item == nil {
		return nil, errEmptyItem
	}
	if resourcePath == "" {
		return nil, errEmptyPath
	}
	res := MikrotikItem{}
	err := c.SendRequest(crudCreate, &URL{Path: resourcePath}, item, &res)
	return res, err
}
func ReadItems(id *ItemId, resourcePath string, c Client) (*[]MikrotikItem, error) {
	// id can be empty.
	if resourcePath == "" {
		return nil, errEmptyPath
	}
	url := &URL{Path: resourcePath}
	// If the 'id' is nil, then this is a Datasource reading (resource Path only).
	if id != nil {
		// REST: prevent 404 'Not Found' error by direct resource request (/interface/vlan/*39).
		// Error occurs when a resource has been deleted outside terraform control.
		// But in the case below we have an empty [] or non-empty array [{...}].
		// /interface/vlan?.id=*39
		url.Query = []string{"?" + id.Type.String() + "=" + id.Value}
	}
	var res []MikrotikItem
	err := c.SendRequest(crudRead, url, nil, &res)
	return &res, err
}
func ReadItemsFiltered(filter []string, resourcePath string, c Client) (*[]MikrotikItem, error) {
	if resourcePath == "" {
		return nil, errEmptyPath
	}
	// Filter format: name=value
	// REST query: name=value; name=value
	// API  query: ?=name=value; ?=name=value
	if c.GetTransport() == TransportAPI {
		for i, s := range filter {
			filter[i] = "?=" + s
		}
	}
	url := &URL{Path: resourcePath, Query: filter}
	var res []MikrotikItem
	err := c.SendRequest(crudRead, url, nil, &res)
	return &res, err
}
func UpdateItem(id *ItemId, resourcePath string, item MikrotikItem, c Client) (MikrotikItem, error) {
	if id.Value == "" {
		return nil, errEmptyId
	}
	if resourcePath == "" {
		return nil, errEmptyPath
	}
	if c.GetTransport() == TransportREST {
		// /interface/vlan/*39
		resourcePath += "/" + id.Value
	} else {
		item[".id"] = id.Value
	}
	res := MikrotikItem{}
	err := c.SendRequest(crudUpdate, &URL{Path: resourcePath}, item, &res)
	return res, err
}
func DeleteItem(id *ItemId, resourcePath string, c Client) error {
	if id.Value == "" {
		return errEmptyId
	}
	if resourcePath == "" {
		return errEmptyPath
	}
	url := &URL{Path: resourcePath}
	if c.GetTransport() == TransportREST {
		// This method is used to delete the record with a specified ID from the menu encoded in the URL.
		// If the deletion has been succeeded, the server responds with an empty response.
		// For example, call to delete the record twice, on second call router will return 404 error.
		// /interface/vlan/*39
		url.Path += "/" + id.Value
	} else {
		url.Query = []string{"=.id=" + id.Value}
	}
	return c.SendRequest(crudDelete, url, nil, &MikrotikItem{})
}
================================================

File: mikrotik_serialize.go
================================================
package routeros
import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"
	"github.com/hashicorp/go-cty/cty"
	"github.com/hashicorp/terraform-plugin-sdk/v2/diag"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)
var reMetadataFields = regexp.MustCompile(`^___\S+___$`)
var reTransformSet = regexp.MustCompile(`"\s*?(\S+?)\s*?\s*?:\s*?\s*?(\S+?)\s*?"`)
var reSkipFields = regexp.MustCompile(`"\s*?(\S+?)\s*?"\s*?`)
// GetMetadata Get item metadata fields from resource schema.
func GetMetadata(s map[string]*schema.Schema) *MikrotikItemMetadata {
	meta := &MikrotikItemMetadata{}
	// Schema map iteration.
	for terraformSnakeName, terraformMetadata := range s {
		if reMetadataFields.MatchString(terraformSnakeName) {
			switch terraformSnakeName {
			case MetaId:
				meta.IdType = IdType(terraformMetadata.Default.(int))
			case MetaResourcePath:
				meta.Path = terraformMetadata.Default.(string)
			default:
				if meta.Meta == nil {
					meta.Meta = make(map[string]string)
				}
				meta.Meta[terraformSnakeName] = terraformMetadata.Default.(string)
			}
		}
	}
	return meta
}
func isEmpty(propName string, schemaProp *schema.Schema, d *schema.ResourceData, confValue cty.Value) bool {
	v := d.Get(propName)
	switch schemaProp.Type {
	case schema.TypeString:
		if schemaProp.Default != nil {
			return v.(string) == "" && schemaProp.Default.(string) == ""
		}
		return v.(string) == "" && confValue.IsNull()
	case schema.TypeFloat, schema.TypeInt:
		return confValue.IsNull() && schemaProp.Default == nil
	case schema.TypeBool:
		// If true, it is always not empty:
		if v.(bool) {
			return false
		}
		// Use the default value:
		if schemaProp.Default != nil {
			return false
		}
		return confValue.IsNull()
	case schema.TypeList:
		if confValue.Type().ElementType().IsObjectType() {
			return len(v.([]interface{})) == 0
		}
		return len(v.([]interface{})) == 0 && confValue.IsNull()
	case schema.TypeSet:
		return v.(*schema.Set).Len() == 0 && confValue.IsNull()
	case schema.TypeMap:
		return len(v.(map[string]interface{})) == 0
	default:
		panic("[isEmpty] wrong resource type: " + schemaProp.Type.String())
	}
}
// loadTransformSet Converting the metadata of the 'MetaTransformSet' field into a map for forward and reverse
// transformation. This map should be applied before the logical processing of fields at the beginning of
// serialization/deserialization.
// Forward transformation for use in the 'MikrotikResourceDataToTerraform' function, reverse transformation for use
// in the 'TerraformResourceDataToMikrotik' function.
// s: "channel: channel.config","datapath: datapath.config"` in the Mikrotik (kebab) notation!
func loadTransformSet(s string, reverse bool) (m map[string]string) {
	m = make(map[string]string)
	for _, b := range reTransformSet.FindAllStringSubmatch(s, -1) {
		if !reverse {
			m[b[1]] = b[2]
		} else {
			m[b[2]] = b[1]
		}
	}
	return
}
// loadSkipFields A list of fields that will not be serialized and transferred to Mikrotik.
func loadSkipFields(s string) (m map[string]struct{}) {
	m = make(map[string]struct{})
	for _, b := range reSkipFields.FindAllStringSubmatch(s, -1) {
		m[b[1]] = struct{}{}
	}
	return
}
// ListToString Convert List and Set to a delimited string.
func ListToString(v any) (res string) {
	for i, elem := range v.([]interface{}) {
		if i > 0 {
			res += fmt.Sprintf(",%v", elem)
		} else {
			res = fmt.Sprint(elem)
		}
	}
	return
}
// TerraformResourceDataToMikrotik Marshal Mikrotik resource from TF resource schema.
func TerraformResourceDataToMikrotik(s map[string]*schema.Schema, d *schema.ResourceData) (MikrotikItem, *MikrotikItemMetadata) {
	item := MikrotikItem{}
	meta := &MikrotikItemMetadata{}
	rawConfig := d.GetRawConfig()
	var transformSet map[string]string
	var skipFields, setUnsetFields map[string]struct{}
	// {"channel.config": "channel", "schema-field-name": "mikrotik-field-name"}
	if ts, ok := s[MetaTransformSet]; ok {
		transformSet = loadTransformSet(ts.Default.(string), true)
	}
	// "field_first", "field_second", "field_third"
	if sf, ok := s[MetaSkipFields]; ok {
		skipFields = loadSkipFields(sf.Default.(string))
	}
	if suf, ok := s[MetaSetUnsetFields]; ok {
		setUnsetFields = loadSkipFields(suf.Default.(string))
	}
	// Schema map iteration.
	for terraformSnakeName, terraformMetadata := range s {
		// Fill in the metadata fields.
		if reMetadataFields.MatchString(terraformSnakeName) {
			switch terraformSnakeName {
			case MetaId:
				meta.IdType = IdType(terraformMetadata.Default.(int))
			case MetaResourcePath:
				meta.Path = terraformMetadata.Default.(string)
			case MetaTransformSet, MetaSkipFields, MetaSetUnsetFields, MetaDropByValue:
				continue
			default:
				meta.Meta[terraformSnakeName] = terraformMetadata.Default.(string)
			}
			continue
		}
		// Skip the fields specified in the schema.
		if _, ok := skipFields[terraformSnakeName]; ok {
			continue
		}
		// Skip all read-only properties.
		if terraformMetadata.Computed && !terraformMetadata.Optional {
			continue
		}
		/*
			Skip all empty Optional fields.
			This logic may be broken, but I don't have enough examples to test it.
			All fields checked in Winbox must be Optional: true & Computed: true.
			Otherwise, there will be an error: "After applying this test step, the plan was not empty."
			        Terraform will perform the following actions:
			          # routeros_interface_bridge.test_bridge will be updated in-place
			          ~ resource "routeros_interface_bridge" "test_bridge" {
			              - fast_forward        = true -> null
			                id                  = "*DD"
			                name                = "test_bridge"
			                # (22 unchanged attributes hidden)
			            }
		*/
		/*
			old, new := d.GetChange(terraformSnakeName)
			conf := d.GetRawConfig().GetAttr(terraformSnakeName).IsNull()
			fmt.Println(rawConfig.GetAttr(terraformSnakeName).IsKnown())
			fmt.Printf("%25s - old: '%10v', new: '%10v', isNull: %v", terraformSnakeName, old, new, conf)
		*/
		if terraformMetadata.Optional && !d.HasChange(terraformSnakeName) &&
			isEmpty(terraformSnakeName, s[terraformSnakeName], d, rawConfig.GetAttr(terraformSnakeName)) {
			// fmt.Println(" ... skipped")
			continue
		}
		// fmt.Println()
		// terraformSnakeName = fast_forward, schemaPropData = true
		// NewMikrotikItem.Fields["fast-forward"] = "true"
		mikrotikKebabName := SnakeToKebab(terraformSnakeName)
		value := d.Get(terraformSnakeName)
		switch terraformMetadata.Type {
		case schema.TypeString:
			if _, ok := setUnsetFields[terraformSnakeName]; ok && value.(string) == "" {
				// Unset
				item["!"+mikrotikKebabName] = ""
				continue
			}
			item[mikrotikKebabName] = value.(string)
		case schema.TypeFloat:
			item[mikrotikKebabName] = strconv.FormatFloat(value.(float64), 'f', -1, 64)
		case schema.TypeInt:
			item[mikrotikKebabName] = strconv.Itoa(value.(int))
		case schema.TypeBool:
			// true:  {...,"interfaces":"ether3","passive":"","priority":"128",...}
			// false: {...,"interfaces":"ether3",             "priority":"128",...}
			if _, ok := setUnsetFields[terraformSnakeName]; ok {
				if value.(bool) {
					item[mikrotikKebabName] = ""
				} else {
					// Unset
					item["!"+mikrotikKebabName] = ""
				}
				continue
			}
			item[mikrotikKebabName] = BoolToMikrotikJSON(value.(bool))
		// Used to represent an ordered collection of items.
		case schema.TypeList:
			switch terraformMetadata.Elem.(type) {
			case *schema.Schema:
				item[mikrotikKebabName] = ListToString(value)
			case *schema.Resource:
				// skip if object is empty
				if value.([]interface{})[0] == nil {
					continue
				}
				list := value.([]interface{})[0].(map[string]interface{})
				ctyList := rawConfig.GetAttr(terraformSnakeName).AsValueSlice()[0]
				for fieldName, value := range list {
					// "output.0.affinity"
					filedNameInState := fmt.Sprintf("%v.%v.%v", terraformSnakeName, 0, fieldName)
					fieldSchema := terraformMetadata.Elem.(*schema.Resource).Schema[fieldName]
					// Skip all read-only properties.
					if fieldSchema.Computed && !fieldSchema.Optional {
						continue
					}
					if fieldSchema.Optional && !d.HasChange(filedNameInState) &&
						isEmpty(filedNameInState, fieldSchema, d, ctyList.GetAttr(fieldName)) {
						continue
					}
					fieldName = SnakeToKebab(mikrotikKebabName + "." + fieldName)
					switch value := value.(type) {
					case string:
						item[fieldName] = value
					case int:
						item[fieldName] = strconv.Itoa(value)
					case bool:
						item[fieldName] = BoolToMikrotikJSON(value)
					}
				}
			}
			// Used to represent an unordered collection of items.
		case schema.TypeSet:
			item[mikrotikKebabName] = ListToString(value.(*schema.Set).List())
		case schema.TypeMap:
			for k, v := range value.(map[string]interface{}) {
				// channel + "." + config
				k = SnakeToKebab(mikrotikKebabName + "." + k)
				// Field transformation: "channel.config" ---> "channel".
				if transformSet != nil {
					if new, ok := transformSet[k]; ok {
						k = new
					}
				}
				// Conversion of boolean values.
				s := BoolToMikrotikJSONStr(v.(string))
				item[k] = s
			}
		default:
			panic(fmt.Sprintf("[TerraformResourceDataToMikrotik] resource type not implemented: %v for '%v'",
				terraformMetadata.Type, terraformSnakeName))
		}
	}
	return item, meta
}
// MikrotikResourceDataToTerraform Unmarshal Mikrotik resource (incoming data: JSON, etc.) to TF resource schema.
func MikrotikResourceDataToTerraform(item MikrotikItem, s map[string]*schema.Schema, d *schema.ResourceData) diag.Diagnostics {
	var diags diag.Diagnostics
	var err error
	var transformSet map[string]string
	var setUnsetFields, skipFields, dropByValue map[string]struct{}
	// {"channel": "channel.config", "mikrotik-field-name": "schema-field-name"}
	if ts, ok := s[MetaTransformSet]; ok {
		transformSet = loadTransformSet(ts.Default.(string), false)
	}
	// "field_first", "field_second", "field_third"
	if suf, ok := s[MetaSetUnsetFields]; ok {
		setUnsetFields = loadSkipFields(suf.Default.(string))
	}
	if sf, ok := s[MetaSkipFields]; ok {
		skipFields = loadSkipFields(sf.Default.(string))
	}
	if dbv, ok := s[MetaDropByValue]; ok {
		dropByValue = loadSkipFields(dbv.Default.(string))
	}
	// TypeMap,TypeSet initialization information storage.
	var maps = make(map[string]map[string]interface{})
	var nestedLists = make(map[string]map[string]interface{})
	// Incoming map iteration.
	for mikrotikKebabName, mikrotikValue := range item {
		// Set the ID.
		//if mikrotikKebabName == ".id" {
		//	if err = d.Set(KeyId, mikrotikValue); err != nil {
		//		diags = append(diags, diag.FromErr(err)...)
		//	}
		//	continue
		//}
		// Skip all service fields (i.e. `.id`, `.nextid`, `ret` ...).
		if mikrotikKebabName[0:1] == "." || mikrotikKebabName == "ret" {
			continue
		}
		if _, ok := dropByValue[mikrotikValue]; ok {
			continue
		}
		// Mikrotik fields transformation: "channel" ---> "channel.config".
		// For further use in the map.
		if transformSet != nil {
			if new, ok := transformSet[mikrotikKebabName]; ok {
				mikrotikKebabName = new
			}
		}
		// field-name => field_name
		terraformSnakeName := KebabToSnake(mikrotikKebabName)
		if skipFields != nil {
			if _, ok := skipFields[terraformSnakeName]; ok {
				continue
			}
		}
		// Composite fields.
		var subFieldSnakeName string
		if strings.Contains(terraformSnakeName, ".") {
			f := strings.SplitN(terraformSnakeName, ".", 2)
			terraformSnakeName, subFieldSnakeName = f[0], f[1]
		}
		if _, ok := s[terraformSnakeName]; !ok {
			// For development.
			// panic("[MikrotikResourceDataToTerraform] The field was lost during the Schema development: " + terraformSnakeName)
			diags = append(diags, diag.Diagnostic{
				// TODO Waiting for TestStep.ExpectWarning https://github.com/hashicorp/terraform-plugin-testing/pull/17
				// The test response to Warnings has not yet been implemented.
				Severity: diag.Warning,
				Summary:  "Field '" + terraformSnakeName + "' not found in the schema",
				Detail: fmt.Sprintf("[MikrotikResourceDataToTerraform] The field was lost during the Schema development: ▷ '%s': '%s' ◁",
					terraformSnakeName, mikrotikValue),
			})
			// Catch all fields.
			continue
		}
		switch s[terraformSnakeName].Type {
		case schema.TypeString:
			err = d.Set(terraformSnakeName, mikrotikValue)
		case schema.TypeFloat:
			f, e := strconv.ParseFloat(mikrotikValue, 64)
			if e != nil {
				diags = diag.Errorf("%v for '%v' field", e, terraformSnakeName)
				break
			}
			err = d.Set(terraformSnakeName, f)
		case schema.TypeInt:
			i, e := strconv.Atoi(mikrotikValue)
			if e != nil {
				diags = diag.Errorf("%v for '%v' field", e, terraformSnakeName)
				break
			}
			err = d.Set(terraformSnakeName, i)
		case schema.TypeBool:
			if _, ok := setUnsetFields[terraformSnakeName]; ok {
				err = d.Set(terraformSnakeName, true)
				break
			}
			err = d.Set(terraformSnakeName, BoolFromMikrotikJSON(mikrotikValue))
		case schema.TypeList, schema.TypeSet:
			var l []interface{}
			// Don't fill in empty strings (preventing a non-empty plan).
			// |   # routeros_interface_wireguard_peer.wg_peer will be updated in-place
			// |   ~ resource "routeros_interface_wireguard_peer" "wg_peer" {
			// |       ~ allowed_address       = [
			// |           - "",
			// |         ]
			// |         id                    = "*2"
			// |         # (7 unchanged attributes hidden)
			// |     }
			// Flat Lists & Sets:
			if _, ok := s[terraformSnakeName].Elem.(*schema.Schema); mikrotikValue != "" && ok {
				for _, v := range strings.Split(mikrotikValue, ",") {
					switch s[terraformSnakeName].Elem.(*schema.Schema).Type {
					case schema.TypeFloat:
						f, err := strconv.ParseFloat(v, 64)
						if err != nil {
							diags = diag.Errorf("%v for '%v' field", err, terraformSnakeName)
							continue
						}
						l = append(l, f)
					case schema.TypeInt:
						i, err := strconv.Atoi(v)
						if err != nil {
							diags = diag.Errorf("%v for '%v' field", err, terraformSnakeName)
							continue
						}
						l = append(l, i)
					default:
						l = append(l, v)
					}
				}
				if err != nil {
					break // case
				}
			}
			if s[terraformSnakeName].Type == schema.TypeList {
				switch s[terraformSnakeName].Elem.(type) {
				case *schema.Schema:
					err = d.Set(terraformSnakeName, l)
				case *schema.Resource:
					var v any
					if _, ok := s[terraformSnakeName].Elem.(*schema.Resource).Schema[subFieldSnakeName]; !ok {
						diags = append(diags, diag.Diagnostic{
							Severity: diag.Warning,
							Summary:  "Field '" + terraformSnakeName + "." + subFieldSnakeName + "' not found in the schema",
							Detail: fmt.Sprintf("[MikrotikResourceDataToTerraform] the datasource Schema sub-field was lost during development: ▷ '%s.%s' ◁",
								terraformSnakeName, subFieldSnakeName),
						})
						continue
					}
					switch s[terraformSnakeName].Elem.(*schema.Resource).Schema[subFieldSnakeName].Type {
					case schema.TypeString:
						v = mikrotikValue
					case schema.TypeFloat:
						v, err = strconv.ParseFloat(mikrotikValue, 64)
						if err != nil {
							diags = diag.Errorf("%v for '%v.%v' field", err, terraformSnakeName, subFieldSnakeName)
						}
					case schema.TypeInt:
						v, err = strconv.Atoi(mikrotikValue)
						if err != nil {
							diags = diag.Errorf("%v for '%v.%v' field", err, terraformSnakeName, subFieldSnakeName)
						}
					case schema.TypeBool:
						v = BoolFromMikrotikJSON(mikrotikValue)
					}
					if err != nil {
						break
					}
					if list, ok := nestedLists[terraformSnakeName]; !ok {
						nestedLists[terraformSnakeName] = map[string]interface{}{subFieldSnakeName: v}
					} else {
						list[subFieldSnakeName] = v
					}
				}
			} else {
				err = d.Set(terraformSnakeName,
					schema.NewSet(schema.HashSchema(s[terraformSnakeName].Elem.(*schema.Schema)), l))
			}
		case schema.TypeMap:
			// "yes" -> "true"; "no" -> "false"
			mikrotikValue = BoolFromMikrotikJSONStr(mikrotikValue)
			if m, ok := maps[terraformSnakeName]; !ok {
				// Create a new map when processing the first incoming field.
				maps[terraformSnakeName] = map[string]interface{}{subFieldSnakeName: mikrotikValue}
			} else {
				m[subFieldSnakeName] = mikrotikValue
			}
		default:
			// For development.
			//panic(fmt.Sprintf("[MikrotikResourceDataToTerraform] resource type not implemented: %v for '%v'",
			//	s[terraformSnakeName].Type.String(), mikrotikValue))
			diags = append(diags, diag.Diagnostic{
				Severity: diag.Warning,
				Summary:  "Can't fill the schema field",
				Detail: fmt.Sprintf("Resource type not implemented: '%v' for '%v'",
					s[terraformSnakeName].Type.String(), terraformSnakeName),
			})
		}
		if err != nil {
			diags = append(diags, diag.FromErr(err)...)
		}
	}
	// Lists processing.
	for name, list := range nestedLists {
		if err = d.Set(name, []interface{}{list}); err != nil {
			diags = append(diags, diag.FromErr(err)...)
		}
	}
	// Maps processing.
	for name, m := range maps {
		if err = d.Set(name, m); err != nil {
			diags = append(diags, diag.FromErr(err)...)
		}
	}
	return diags
}
func MikrotikResourceDataToTerraformDatasource(items *[]MikrotikItem, resourceDataKeyName string, s map[string]*schema.Schema, d *schema.ResourceData) diag.Diagnostics {
	var diags diag.Diagnostics
	var dsItems []map[string]interface{}
	// System resource have an empty 'resourceDataKeyName'.
	var isSystemDatasource bool = (resourceDataKeyName == "")
	// Checking the schema.
	if !isSystemDatasource {
		sv, ok := s[resourceDataKeyName]
		if !ok {
			// For development.
			//panic("[MikrotikResourceDataToTerraformDatasource] the datasource Schema field was lost during development: " + resourceDataKeyName)
			diags = append(diags, diag.Diagnostic{
				Severity: diag.Warning,
				Summary:  "Field '" + resourceDataKeyName + "' not found in the schema",
				Detail: fmt.Sprintf("[MikrotikResourceDataToTerraformDatasource] the datasource Schema field was lost during development: ▷ '%s' ◁",
					resourceDataKeyName),
			})
			// Or panic.
			return diags
		}
		s = sv.Elem.(*schema.Resource).Schema
	}
	if isSystemDatasource && len(*items) != 1 {
		diags = append(diags, diag.Diagnostic{
			Severity: diag.Error,
			Summary:  "System resources should not return an array of values",
			Detail: fmt.Sprintf("[MikrotikResourceDataToTerraformDatasource] system resource '%s' polling returned %d values",
				s[MetaResourcePath].Default.(string), len(*items)),
		})
		return diags
	}
	// Array of Mikrotik items iteration.
	for _, item := range *items {
		dsItem := map[string]interface{}{}
		// Incoming map iteration.
		for mikrotikKebabName, mikrotikValue := range item {
			// MT can return the field name in uppercase format.
			mikrotikKebabName = strings.ToLower(mikrotikKebabName)
			// In this case the ID must be a string.
			if mikrotikKebabName == ".id" {
				dsItem["id"] = mikrotikValue
				continue
			}
			// Skip all service fields.
			if mikrotikKebabName[0:1] == "." {
				continue
			}
			// field-name => field_name
			terraformSnakeName := KebabToSnake(mikrotikKebabName)
			if _, ok := s[terraformSnakeName]; !ok {
				// For development.
				//panic("[MikrotikResourceDataToTerraformDatasource] the field was lost during development.: " + terraformSnakeName)
				diags = append(diags, diag.Diagnostic{
					Severity: diag.Warning,
					Summary:  "Field '" + terraformSnakeName + "' not found in the schema",
					Detail: fmt.Sprintf("[MikrotikResourceDataToTerraformDatasource] the field was lost during the Schema development: ▷ '%s': '%s' ◁",
						terraformSnakeName, mikrotikValue),
				})
				// Catch all fields.
				continue
			}
			var propValue interface{}
			switch s[terraformSnakeName].Type {
			case schema.TypeString:
				propValue = mikrotikValue
			case schema.TypeFloat:
				f, err := strconv.ParseFloat(mikrotikValue, 64)
				if err != nil {
					diags = append(diags, diag.Errorf("%v for '%v' field", err, terraformSnakeName)...)
					continue
				}
				propValue = f
			case schema.TypeInt:
				i, err := strconv.Atoi(mikrotikValue)
				if err != nil {
					diags = append(diags, diag.Errorf("%v for '%v' field", err, terraformSnakeName)...)
					continue
				}
				propValue = i
			case schema.TypeBool:
				// TODO Add support for set/unset fields?
				propValue = BoolFromMikrotikJSON(mikrotikValue)
			case schema.TypeList:
				var l []interface{}
				if mikrotikValue != "" {
					for _, s := range strings.Split(mikrotikValue, ",") {
						l = append(l, s)
					}
				}
				propValue = l
			// TODO Add processing of missing types: List(int), Set, Map
			case schema.TypeSet:
				var l []interface{}
				if mikrotikValue != "" {
					for _, s := range strings.Split(mikrotikValue, ",") {
						l = append(l, s)
					}
				}
				// String sets only (schema.HashString)!
				propValue = schema.NewSet(schema.HashString, l)
			default:
				// For development.
				//panic(fmt.Sprintf("Resource type not implemented: %v for '%v'",
				//	s[terraformSnakeName].Type.String(), mikrotikValue))
				diags = append(diags, diag.Diagnostic{
					Severity: diag.Warning,
					Summary:  "Can't fill the schema field",
					Detail: fmt.Sprintf("Resource type not implemented: %v for '%v'",
						s[terraformSnakeName].Type.String(), mikrotikValue),
				})
			}
			dsItem[terraformSnakeName] = propValue
		}
		dsItems = append(dsItems, dsItem)
	}
	d.SetId(UniqueId())
	if !isSystemDatasource {
		if err := d.Set(resourceDataKeyName, dsItems); err != nil {
			diags = append(diags, diag.FromErr(err)...)
		}
	} else {
		for k, v := range dsItems[0] {
			if err := d.Set(k, v); err != nil {
				diags = append(diags, diag.FromErr(err)...)
			}
		}
	}
	return diags
}
// Copied from terraform-plugin-testing@v1.2.0/helper/resource/id.go
// Because this functionality is marked deprecated.
const UniqueIdPrefix = `terraform-`
// idCounter is a monotonic counter for generating ordered unique ids.
var idMutex sync.Mutex
var idCounter uint32
func UniqueId() string {
	return PrefixedUniqueId(UniqueIdPrefix)
}
func PrefixedUniqueId(prefix string) string {
	// Be precise to 4 digits of fractional seconds, but remove the dot before the
	// fractional seconds.
	timestamp := strings.Replace(
		time.Now().UTC().Format("20060102150405.0000"), ".", "", 1)
	idMutex.Lock()
	defer idMutex.Unlock()
	idCounter++
	return fmt.Sprintf("%s%s%08x", prefix, timestamp, idCounter)
}
================================================

File: mikrotik_serialize_test.go
================================================
package routeros
import (
	"reflect"
	"testing"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)
var (
	testResource = schema.Resource{
		Schema: map[string]*schema.Schema{
			MetaResourcePath: PropResourcePath("/test/resource"),
			MetaId:           PropId(Id),
			"string": {
				Type: schema.TypeString,
			},
			"float": {
				Type: schema.TypeFloat,
			},
			"int": {
				Type: schema.TypeInt,
			},
			"bool": {
				Type: schema.TypeBool,
			},
			"computed": {
				Type:     schema.TypeBool,
				Computed: true,
			},
		},
	}
	testDatasource = schema.Resource{
		Schema: map[string]*schema.Schema{
			"test_name": {
				Type:     schema.TypeList,
				Computed: true,
				Elem: &schema.Resource{
					Schema: map[string]*schema.Schema{
						MetaResourcePath: PropResourcePath("/test/resource"),
						MetaId:           PropId(Id),
						"string": {
							Type: schema.TypeString,
						},
						"float": {
							Type: schema.TypeFloat,
						},
						"int": {
							Type: schema.TypeInt,
						},
						"bool": {
							Type: schema.TypeBool,
						},
					},
				},
			},
		},
	}
)
func Test_mikrotikResourceDataToTerraform(t *testing.T) {
	testItem := MikrotikItem{".id": "*39", "string": "string12345", "float": "0.01", "int": "10", "bool": "true"}
	testResourceData := testResource.TestResourceData()
	expectedRes := map[string]interface{}{"string": "string12345", "float": 0.01, "int": 10, "bool": true}
	err := MikrotikResourceDataToTerraform(testItem, testResource.Schema, testResourceData)
	if err != nil {
		t.Errorf("decoding err: %v", err)
	}
	for key, expected := range expectedRes {
		actual := testResourceData.Get(key)
		if !reflect.DeepEqual(actual, expected) {
			t.Fatalf("bad: expected:%#v\nactual:%#v", expected, actual)
		}
	}
}
func Test_terraformResourceDataToMikrotik(t *testing.T) {
	expected := MikrotikItem{"string": "string12345", "float": "0.01", "int": "10", "bool": "yes"}
	testResourceData := testResource.TestResourceData()
	testResourceData.SetId("*39")
	testResourceData.Set("string", "string12345")
	testResourceData.Set("float", 0.01)
	testResourceData.Set("int", 10)
	testResourceData.Set("bool", true)
	actual, _ := TerraformResourceDataToMikrotik(testResource.Schema, testResourceData)
	if !reflect.DeepEqual(actual, expected) {
		t.Fatalf("bad: expected:%#v\nactual:%#v", expected, actual)
	}
}
func Test_mikrotikResourceDataToTerraformDatasource(t *testing.T) {
	testItems := []MikrotikItem{
		{"string": "string12345", "float": "0.01", "int": "10", "bool": "yes"},
		{"string": "12345string", "float": "0.02", "int": "20", "bool": "no"},
	}
	testResourceData := testDatasource.TestResourceData()
	expectedRes := []map[string]interface{}{
		{MetaResourcePath: "", MetaId: 0, "string": "string12345", "float": 0.01, "int": 10, "bool": true},
		{MetaResourcePath: "", MetaId: 0, "string": "12345string", "float": 0.02, "int": 20, "bool": false},
	}
	err := MikrotikResourceDataToTerraformDatasource(&testItems, "test_name", testDatasource.Schema, testResourceData)
	if err != nil {
		t.Errorf("decoding err: %v", err)
	}
	for i, rec := range testResourceData.Get("test_name").([]interface{}) {
		for key, actual := range rec.(map[string]interface{}) {
			if !reflect.DeepEqual(actual, expectedRes[i][key]) {
				t.Fatalf("bad: (key: %v) expected:%#v\tactual:%#v", key, expectedRes[i][key], actual)
			}
		}
	}
}
func Test_loadTransformSet(t *testing.T) {
	testData := []struct {
		s       string
		reverse bool
	}{
		{toQuotedCommaSeparatedString("channel: channel.config","datapath: datapath.config"), false},
		{toQuotedCommaSeparatedString("mikrotik-field-name : schema-field-name"), false},
		{toQuotedCommaSeparatedString("channel: channel.config","datapath: datapath.config"), true},
		{toQuotedCommaSeparatedString("mikrotik-field-name:schema-field-name"), true},
	}
	expected := []map[string]string{
		{"channel": "channel.config", "datapath": "datapath.config"},
		{"mikrotik-field-name": "schema-field-name"},
		{"channel.config": "channel", "datapath.config": "datapath"},
		{"schema-field-name": "mikrotik-field-name"},
	}
	for i, actual := range testData {
		if !reflect.DeepEqual(loadTransformSet(actual.s, actual.reverse), expected[i]) {
			t.Fatalf("bad: (item: %v) expected:%#v\tactual:%#v", i, expected[i], loadTransformSet(actual.s, actual.reverse))
		}
	}
}
func Test_loadSkipFields(t *testing.T) {
	testData := []struct {
		s       string
	}{
		{toQuotedCommaSeparatedString("name")},
		{toQuotedCommaSeparatedString("name", "rx_1024_1518", "rx_128_255", "rx_1519_max", "rx_256_511", "rx_512_1023", "rx_64")},
	}
	expected := []map[string]struct{}{
		{"name": struct{}{}},
		{"name": struct{}{}, "rx_1024_1518": struct{}{}, "rx_128_255": struct{}{}, "rx_1519_max": struct{}{}, 
			"rx_256_511": struct{}{}, "rx_512_1023": struct{}{}, "rx_64": struct{}{}},
	}
	for i, actual := range testData {
		if !reflect.DeepEqual(loadSkipFields(actual.s), expected[i]) {
			t.Fatalf("bad: (item: %v) expected:%#v\tactual:%#v", i, expected[i], loadSkipFields(actual.s))
		}
	}
}
================================================

File: mikrotik_test.go
================================================
package routeros
import (
	"testing"
)
func TestBoolFromMikrotikJSON(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			`Go bool from Mikrotik JSON - "true"`,
			args{"true"},
			true,
		},
		{
			`Go bool from Mikrotik JSON - "false"`,
			args{"false"},
			false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BoolFromMikrotikJSON(tt.args.s); got != tt.want {
				t.Errorf("BoolFromMikrotikJSON() = %v, want %v", got, tt.want)
			}
		})
	}
}
func TestBoolToMikrotikJSON(t *testing.T) {
	type args struct {
		b bool
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			`Go bool to Mikrotik JSON - "true"`,
			args{true},
			"yes",
		},
		{
			`Go bool to Mikrotik JSON - "false"`,
			args{false},
			"no",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BoolToMikrotikJSON(tt.args.b); got != tt.want {
				t.Errorf("BoolToMikrotikJSON() = %v, want %v", got, tt.want)
			}
		})
	}
}
func TestMikrotikItem_GetID(t *testing.T) {
	tests := []struct {
		name string
		mi   MikrotikItem
		want string
	}{
		{
			"Get Mikrotik Item ID",
			MikrotikItem{".id": "*39"},
			"*39",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.mi.GetID(Id); got != tt.want {
				t.Errorf("GetID() = %v, want %v", got, tt.want)
			}
		})
	}
}
func Test_kebabToSnake(t *testing.T) {
	type args struct {
		name string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			"Kebab to snake case",
			args{"kebab-to-snake"},
			"kebab_to_snake",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := KebabToSnake(tt.args.name); got != tt.want {
				t.Errorf("KebabToSnake() = %v, want %v", got, tt.want)
			}
		})
	}
}
func Test_snakeToKebab(t *testing.T) {
	type args struct {
		name string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			"Snake to kebab case",
			args{"snake_to_kebab"},
			"snake-to-kebab",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SnakeToKebab(tt.args.name); got != tt.want {
				t.Errorf("SnakeToKebab() = %v, want %v", got, tt.want)
			}
		})
	}
}
================================================

File: resource_capsman_configuration.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
/*
  {
    ".id": "*1",
    "channel": "channel-cfg",
    "comment": "Comment",
    "country": "no_country_set",
    "datapath": "datapath-cfg",
    "disconnect-timeout": "1s150ms",
    "distance": "indoors",
    "frame-lifetime": "120ms",
    "guard-interval": "long",
    "hide-ssid": "true",
    "hw-protection-mode": "rts-cts",
    "hw-retries": "1",
    "installation": "indoor",
    "keepalive-frames": "enabled",
    "load-balancing-group": "",
    "max-sta-count": "1",
    "mode": "ap",
    "multicast-helper": "full",
    "name": "cfg1",
    "rates": "rate-cfg",
    "rx-chains": "1,3",
    "security": "security-cfg",
    "ssid": "SSID",
    "tx-chains": "0,2"
  }
*/
// https://help.mikrotik.com/docs/display/ROS/CAPsMAN
func ResourceCapsManConfiguration() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/caps-man/configuration"),
		MetaId:           PropId(Id),
		MetaTransformSet: PropTransformSet("channel: channel.config", "datapath: datapath.config",
			"rates: rates.config", "security: security.config"),
		"channel": {
			Type:        schema.TypeMap,
			Optional:    true,
			Description: "Channel inline settings.",
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		KeyComment: PropCommentRw,
		"country": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "Limits available bands, frequencies and maximum transmit power for each frequency. Also " +
				"specifies default value of scan-list. Value no_country_set is an FCC compliant set of channels.",
		},
		"datapath": {
			Type:        schema.TypeMap,
			Optional:    true,
			Description: "Datapath inline settings.",
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"disconnect_timeout": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "This interval is measured from third sending failure on the lowest data rate. At this point " +
				"3 * (hw-retries + 1) frame transmits on the lowest data rate had failed. During disconnect-timeout packet " +
				"transmission will be retried with on-fail-retry-time interval. If no frame can be transmitted successfully " +
				`during disconnect-timeout, the connection is closed, and this event is logged as "extensive data loss". ` +
				"Successful frame transmission resets this timer.",
			DiffSuppressFunc: TimeEquall,
		},
		"distance": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "How long to wait for confirmation of unicast frames (ACKs) before considering transmission " +
				"unsuccessful, or in short ACK-Timeout.",
		},
		"frame_lifetime": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "Discard frames that have been queued for sending longer than frame-lifetime. By default, when " +
				"value of this property is 0, frames are discarded only after connection is closed (format: 0.00 sec).",
			DiffSuppressFunc: TimeEquall,
		},
		"guard_interval": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "Whether to allow use of short guard interval (refer to 802.11n MCS specification to see how " +
				`this may affect throughput). "any" will use either short or long, depending on data rate, "long" will ` +
				"use long.",
			ValidateFunc: validation.StringInSlice([]string{"any ", "long"}, false),
		},
		"hide_ssid": {
			Type:     schema.TypeBool,
			Optional: true,
			Computed: true,
			Description: "This property has effect only in AP mode. Setting it to yes can remove this network from " +
				"the list of wireless networks that are shown by some client software. Changing this setting does not " +
				"improve the security of the wireless network, because SSID is included in other frames sent by the AP.",
		},
		"hw_protection_mode": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "Frame protection support property. " +
				"[See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#Frame_protection_support_(RTS/CTS)).",
			ValidateFunc: validation.StringInSlice([]string{"cts-to-self", "none", "rts-cts"}, false),
		},
		"hw_retries": {
			Type:     schema.TypeInt,
			Optional: true,
			Description: "Number of times sending frame is retried without considering it a transmission failure. " +
				"[See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless)",
			ValidateFunc: validation.IntBetween(0, 15),
		},
		"installation": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "Adjusts scan-list to use indoor, outdoor or all frequencies for the country that is set.",
			ValidateFunc: validation.StringInSlice([]string{"any", "indoor", "outdoor"}, false),
		},
		"keepalive_frames": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  `If a client has not communicated for around 20 seconds, AP sends a "keepalive-frame".`,
			ValidateFunc: validation.StringInSlice([]string{"enabled", "disabled"}, false),
		},
		"load_balancing_group": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "Tags the interface to the load balancing group. For a client to connect to interface in this " +
				"group, the interface should have the same number of already connected clients as all other interfaces " +
				"in the group or smaller. Useful in setups where ranges of CAPs mostly overlap.",
		},
		"max_sta_count": {
			Type:         schema.TypeInt,
			Optional:     true,
			Description:  "Maximum number of associated clients.",
			ValidateFunc: validation.IntBetween(1, 2007),
		},
		"mode": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "Set operational mode. Only **ap** currently supported.",
			ValidateFunc: validation.StringInSlice([]string{"ap"}, false),
		},
		KeyName: PropNameForceNewRw,
		"multicast_helper": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "When set to full multicast packets will be sent with unicast destination MAC address, " +
				"resolving multicast problem on a wireless link. This option should be enabled only on the access " +
				"point, clients should be configured in station-bridge mode.",
			ValidateFunc: validation.StringInSlice([]string{"default", "disabled", "full"}, false),
		},
		"rates": {
			Type:        schema.TypeMap,
			Optional:    true,
			Description: "Rates inline settings.",
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"rx_chains": {
			Type:        schema.TypeList,
			Optional:    true,
			Description: "Which antennas to use for receive.",
			Elem: &schema.Schema{
				Type:         schema.TypeInt,
				ValidateFunc: validation.IntBetween(0, 3),
			},
		},
		"security": {
			Type:        schema.TypeMap,
			Optional:    true,
			Description: "Security inline settings.",
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"ssid": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "SSID (service set identifier) is a name broadcast in the beacons that identifies " +
				"wireless network.",
			ValidateFunc: validation.StringLenBetween(0, 32),
		},
		"tx_chains": {
			Type:        schema.TypeList,
			Optional:    true,
			Description: "Which antennas to use for transmit.",
			Elem: &schema.Schema{
				Type:         schema.TypeInt,
				ValidateFunc: validation.IntBetween(0, 3),
			},
		},
	}
	return &schema.Resource{
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		SchemaVersion: 1,
		StateUpgraders: []schema.StateUpgrader{
			{
				Type:    ResourceCapsManConfigurationV0().CoreConfigSchema().ImpliedType(),
				Upgrade: stateMigrationNameToId(resSchema[MetaResourcePath].Default.(string)),
				Version: 0,
			},
		},
		Schema: resSchema,
	}
}
================================================

File: resource_capsman_configuration_test.go
================================================
package routeros
import (
	"testing"
	"github.com/hashicorp/terraform-plugin-testing/helper/resource"
)
const testCapsManConfigurationMaxVersion = "7.12.2"
const testCapsManConfigurationAddress = "routeros_capsman_configuration.test_configuration"
func TestAccCapsManConfigurationTest_basic(t *testing.T) {
	if !testCheckMaxVersion(t, testCapsManConfigurationMaxVersion) {
		t.Logf("Test skipped, the maximum supported version is %v", testCapsManConfigurationMaxVersion)
		return
	}
	for _, name := range testNames {
		t.Run(name, func(t *testing.T) {
			resource.Test(t, resource.TestCase{
				PreCheck: func() {
					testAccPreCheck(t)
					testSetTransportEnv(t, name)
				},
				ProviderFactories: testAccProviderFactories,
				CheckDestroy:      testCheckResourceDestroy("/caps-man/configuration", "routeros_capsman_configuration"),
				Steps: []resource.TestStep{
					{
						Config: testAccCapsManConfigurationConfig(0),
						Check: resource.ComposeTestCheckFunc(
							testResourcePrimaryInstanceId(testCapsManConfigurationAddress),
							resource.TestCheckResourceAttr(testCapsManConfigurationAddress, "name", "test_configuration"),
						),
					},
					{
						Config: testAccCapsManConfigurationConfig(1),
						Check: resource.ComposeTestCheckFunc(
							resource.TestCheckResourceAttr("routeros_capsman_configuration.test_configuration_2",
								"name", "test_configuration_2"),
							resource.TestCheckResourceAttrSet("routeros_capsman_configuration.test_configuration_2",
								"channel.config"),
							resource.TestCheckResourceAttrSet("routeros_capsman_configuration.test_configuration_2",
								"datapath.config"),
							resource.TestCheckResourceAttrSet("routeros_capsman_configuration.test_configuration_2",
								"rates.config"),
							resource.TestCheckResourceAttrSet("routeros_capsman_configuration.test_configuration_2",
								"security.config"),
						),
						Destroy: false,
					},
				},
			})
		})
	}
}
func testAccCapsManConfigurationConfig(n int) string {
	tests := []string{`
resource "routeros_capsman_configuration" "test_configuration" {
	comment              = "Comment"
	country              = "no_country_set"
	disconnect_timeout   = "1s150ms"
	distance             = "indoors"
	frame_lifetime       = "0.12" // 120ms
	guard_interval       = "long"
	hide_ssid            = true
	hw_protection_mode   = "rts-cts"
	hw_retries           = 1
	installation         = "indoor"
	keepalive_frames     = "enabled"
	load_balancing_group = ""
	max_sta_count        = 1
	mode                 = "ap"
	multicast_helper     = "full"
	name                 = "test_configuration"
	rx_chains            = [1, 3]
	ssid                 = "SSID"
	tx_chains            = [0, 2]
 }`, `
resource "routeros_capsman_channel" "test_channel" {
	name = "test-channel-config"
}
resource "routeros_capsman_datapath" "test_datapath" {
	name = "test-datapath-config"
}
resource "routeros_capsman_rates" "test_rates" {
	name = "test-rates-config"
}
resource "routeros_capsman_security" "test_security" {
	name = "test-security-config"
}
resource "routeros_capsman_configuration" "test_configuration_2" {
	name = "test_configuration_2"
	channel = {
	  config                = "${routeros_capsman_channel.test_channel.name}"
	  band                  = "2ghz-b/g/n"
	  control_channel_width = "10mhz"
	  extension_channel     = "eCee"
	  frequency             = 2412
	  reselect_interval     = "1h"
	  save_selected         = "true"
	  secondary_frequency   = "disabled"
	  skip_dfs_channels     = "true"
	  tx_power              = 20
	}
	datapath = {
	  config                      = "${routeros_capsman_datapath.test_datapath.name}"
	  arp                         = "local-proxy-arp"
	  bridge                      = "bridge"
	  bridge_cost                 = "100"
	  bridge_horizon              = "200"
	  client_to_client_forwarding = "true"
	  interface_list              = "static"
	  l2mtu                       = "1450"
	  local_forwarding            = "true"
	  mtu                         = "1500"
	  vlan_id                     = "101"
	  vlan_mode                   = "no-tag"
	//   openflow_switch             = "aaa"
	  }
	rates = {
	  config            = "${routeros_capsman_rates.test_rates.name}"
	  basic             = "1Mbps,5.5Mbps,6Mbps,18Mbps,36Mbps,54Mbps"
	  ht_basic_mcs      = "mcs-0,mcs-7,mcs-11,mcs-14,mcs-16,mcs-21"
	  ht_supported_mcs  = "mcs-3,mcs-8,mcs-10,mcs-13,mcs-17,mcs-18"
	  supported         = "2Mbps,11Mbps,9Mbps,12Mbps,24Mbps,48Mbps"
	  vht_basic_mcs     = "none"
	  vht_supported_mcs = "mcs0-9,mcs0-7"
	}
	security = {
	  config                = "${routeros_capsman_security.test_security.name}"
	  authentication_types  = "wpa-psk,wpa-eap"
	  disable_pmkid         = "true"
	  eap_methods           = "eap-tls,passthrough"
	  eap_radius_accounting = "true"
	  encryption            = "aes-ccm,tkip"
	  group_encryption      = "aes-ccm"
	  group_key_update      = "1h"
	  passphrase            = "AAAAAAAAA"
	  tls_certificate       = "none"
	  tls_mode              = "verify-certificate"
	}
	depends_on = [
	  routeros_capsman_channel.test_channel,
	  routeros_capsman_datapath.test_datapath,
	  routeros_capsman_rates.test_rates,
	  routeros_capsman_security.test_security
	]
}`,
	}
	return providerConfig + tests[n]
}
================================================

File: resource_capsman_configuration_v0.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
func ResourceCapsManConfigurationV0() *schema.Resource {
	return &schema.Resource{
		Schema: map[string]*schema.Schema{
			MetaResourcePath: PropResourcePath("/caps-man/configuration"),
			MetaId:           PropId(Name),
			MetaTransformSet: PropTransformSet("channel: channel.config", "datapath: datapath.config",
				"rates: rates.config", "security: security.config"),
			"channel": {
				Type:        schema.TypeMap,
				Optional:    true,
				Description: "Channel inline settings.",
				Elem: &schema.Schema{
					Type: schema.TypeString,
				},
			},
			KeyComment: PropCommentRw,
			"country": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "Limits available bands, frequencies and maximum transmit power for each frequency. Also " +
					"specifies default value of scan-list. Value no_country_set is an FCC compliant set of channels.",
			},
			"datapath": {
				Type:        schema.TypeMap,
				Optional:    true,
				Description: "Datapath inline settings.",
				Elem: &schema.Schema{
					Type: schema.TypeString,
				},
			},
			"disconnect_timeout": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "This interval is measured from third sending failure on the lowest data rate. At this point " +
					"3 * (hw-retries + 1) frame transmits on the lowest data rate had failed. During disconnect-timeout packet " +
					"transmission will be retried with on-fail-retry-time interval. If no frame can be transmitted successfully " +
					`during disconnect-timeout, the connection is closed, and this event is logged as "extensive data loss". ` +
					"Successful frame transmission resets this timer.",
				DiffSuppressFunc: TimeEquall,
			},
			"distance": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "How long to wait for confirmation of unicast frames (ACKs) before considering transmission " +
					"unsuccessful, or in short ACK-Timeout.",
			},
			"frame_lifetime": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "Discard frames that have been queued for sending longer than frame-lifetime. By default, when " +
					"value of this property is 0, frames are discarded only after connection is closed (format: 0.00 sec).",
				DiffSuppressFunc: TimeEquall,
			},
			"guard_interval": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "Whether to allow use of short guard interval (refer to 802.11n MCS specification to see how " +
					`this may affect throughput). "any" will use either short or long, depending on data rate, "long" will ` +
					"use long.",
				ValidateFunc: validation.StringInSlice([]string{"any ", "long"}, false),
			},
			"hide_ssid": {
				Type:     schema.TypeBool,
				Optional: true,
				Computed: true,
				Description: "This property has effect only in AP mode. Setting it to yes can remove this network from " +
					"the list of wireless networks that are shown by some client software. Changing this setting does not " +
					"improve the security of the wireless network, because SSID is included in other frames sent by the AP.",
			},
			"hw_protection_mode": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "Frame protection support property. " +
					"[See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#Frame_protection_support_(RTS/CTS)).",
				ValidateFunc: validation.StringInSlice([]string{"cts-to-self", "none", "rts-cts"}, false),
			},
			"hw_retries": {
				Type:     schema.TypeInt,
				Optional: true,
				Description: "Number of times sending frame is retried without considering it a transmission failure. " +
					"[See docs](https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless)",
				ValidateFunc: validation.IntBetween(0, 15),
			},
			"installation": {
				Type:         schema.TypeString,
				Optional:     true,
				Description:  "Adjusts scan-list to use indoor, outdoor or all frequencies for the country that is set.",
				ValidateFunc: validation.StringInSlice([]string{"any", "indoor", "outdoor"}, false),
			},
			"keepalive_frames": {
				Type:         schema.TypeString,
				Optional:     true,
				Description:  `If a client has not communicated for around 20 seconds, AP sends a "keepalive-frame".`,
				ValidateFunc: validation.StringInSlice([]string{"enabled", "disabled"}, false),
			},
			"load_balancing_group": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "Tags the interface to the load balancing group. For a client to connect to interface in this " +
					"group, the interface should have the same number of already connected clients as all other interfaces " +
					"in the group or smaller. Useful in setups where ranges of CAPs mostly overlap.",
			},
			"max_sta_count": {
				Type:         schema.TypeInt,
				Optional:     true,
				Description:  "Maximum number of associated clients.",
				ValidateFunc: validation.IntBetween(1, 2007),
			},
			"mode": {
				Type:         schema.TypeString,
				Optional:     true,
				Description:  "Set operational mode. Only **ap** currently supported.",
				ValidateFunc: validation.StringInSlice([]string{"ap"}, false),
			},
			KeyName: PropNameForceNewRw,
			"multicast_helper": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "When set to full multicast packets will be sent with unicast destination MAC address, " +
					"resolving multicast problem on a wireless link. This option should be enabled only on the access " +
					"point, clients should be configured in station-bridge mode.",
				ValidateFunc: validation.StringInSlice([]string{"default", "disabled", "full"}, false),
			},
			"rates": {
				Type:        schema.TypeMap,
				Optional:    true,
				Description: "Rates inline settings.",
				Elem: &schema.Schema{
					Type: schema.TypeString,
				},
			},
			"rx_chains": {
				Type:        schema.TypeList,
				Optional:    true,
				Description: "Which antennas to use for receive.",
				Elem: &schema.Schema{
					Type:         schema.TypeInt,
					ValidateFunc: validation.IntBetween(0, 3),
				},
			},
			"security": {
				Type:        schema.TypeMap,
				Optional:    true,
				Description: "Security inline settings.",
				Elem: &schema.Schema{
					Type: schema.TypeString,
				},
			},
			"ssid": {
				Type:     schema.TypeString,
				Optional: true,
				Description: "SSID (service set identifier) is a name broadcast in the beacons that identifies " +
					"wireless network.",
				ValidateFunc: validation.StringLenBetween(0, 32),
			},
			"tx_chains": {
				Type:        schema.TypeList,
				Optional:    true,
				Description: "Which antennas to use for transmit.",
				Elem: &schema.Schema{
					Type:         schema.TypeInt,
					ValidateFunc: validation.IntBetween(0, 3),
				},
			},
		},
	}
}
================================================

File: resource_container_config.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)
// https://help.mikrotik.com/docs/display/ROS/Container#Container-Containerconfiguration
func ResourceContainerConfig() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/container/config"),
		MetaId:           PropId(Name),
		"registry_url": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "External registry url from where the container will be downloaded.",
		},
		"username": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Specifies the username for authentication (starting from ROS 7.8)",
		},
		"password": {
			Type:        schema.TypeString,
			Sensitive:   true,
			Optional:    true,
			Description: "Specifies the password for authentication (starting from ROS 7.8)",
		},
		"ram_high": {
			Type:        schema.TypeString,
			Optional:    true,
			Default:     "0",
			Description: "RAM usage limit. (0 for unlimited)",
		},
		"tmpdir": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Container extraction directory.",
		},
		"layer_dir": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Container layers directory.",
		},
	}
	return &schema.Resource{
		CreateContext: DefaultSystemCreate(resSchema),
		ReadContext:   DefaultSystemRead(resSchema),
		UpdateContext: DefaultSystemUpdate(resSchema),
		DeleteContext: DefaultSystemDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: resource_ip_dhcp_server_config.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
// ResourceDhcpServerConfig https://help.mikrotik.com/docs/display/ROS/DHCP#DHCP-StoreConfiguration
func ResourceDhcpServerConfig() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/ip/dhcp-server/config"),
		MetaId:           PropId(Id),
		"accounting": {
			Type:        schema.TypeBool,
			Optional:    true,
			Default:     true,
			Description: "An option that enables accounting for DHCP leases.",
		},
		"interim_update": {
			Type:             schema.TypeString,
			Optional:         true,
			Default:          "0s",
			Description:      "An option determining whether the DHCP server sends periodic updates to the accounting server during a lease.",
			DiffSuppressFunc: TimeEquall,
		},
		"radius_password": {
			Type:         schema.TypeString,
			Optional:     true,
			Default:      "empty",
			Description:  "An option to set the password parameter for the RADIUS server. This option is available in RouterOS starting from version 7.0.",
			ValidateFunc: validation.StringInSlice([]string{"empty", "same-as-user"}, false),
		},
		"store_leases_disk": {
			Type:             schema.TypeString,
			Optional:         true,
			Default:          "5m",
			Description:      "An option of how often the DHCP leases will be stored on disk.",
			DiffSuppressFunc: TimeEquall,
		},
	}
	return &schema.Resource{
		CreateContext: DefaultSystemCreate(resSchema),
		ReadContext:   DefaultSystemRead(resSchema),
		UpdateContext: DefaultSystemUpdate(resSchema),
		DeleteContext: DefaultSystemDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: resource_ip_dhcp_server_network.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
// ResourceDhcpServerNetwork https://wiki.mikrotik.com/wiki/Manual:IP/DHCP_Server#Networks
func ResourceDhcpServerNetwork() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/ip/dhcp-server/network"),
		MetaId:           PropId(Id),
		"address": {
			Type:        schema.TypeString,
			Required:    true,
			Description: "The network DHCP server(s) will lease addresses from.",
		},
		"boot_file_name": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Boot filename.",
		},
		"caps_manager": {
			Type:     schema.TypeList,
			Optional: true,
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			Description: "A list of IP addresses for one or more CAPsMAN system managers. " +
				"DHCP Option 138 (capwap) will be used.",
		},
		KeyComment: PropCommentRw,
		"dhcp_option": {
			Type:     schema.TypeList,
			Optional: true,
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			Description: "Add additional DHCP options from the option list.",
		},
		"dhcp_option_set": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Add an additional set of DHCP options.",
		},
		"dns_none": {
			Type:     schema.TypeBool,
			Optional: true,
			Description: "If set, then DHCP Server will not pass dynamic DNS servers configured on the router to the " +
				"DHCP clients if no DNS Server in DNS-server is set.",
		},
		"dns_server": {
			Type:     schema.TypeList,
			Optional: true,
			Elem: &schema.Schema{
				Type: schema.TypeString,
			},
			Description: "The DHCP client will use these as the default DNS servers. Two DNS servers " +
				"can be specified to be used by the DHCP client as primary and secondary DNS servers.",
		},
		"domain": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "The DHCP client will use this as the 'DNS domain' setting for the network adapter.",
		},
		KeyDynamic: PropDynamicRo,
		"gateway": {
			Type:         schema.TypeString,
			Optional:     true,
			Default:      "0.0.0.0",
			Description:  "The default gateway to be used by DHCP Client.",
			ValidateFunc: validation.IsIPv4Address,
		},
		"netmask": {
			Type:     schema.TypeInt,
			Optional: true,
			Default:  0,
			Description: "The actual network mask is to be used by the DHCP client. If set to '0' - netmask from " +
				"network address will be used.",
			ValidateFunc: validation.IntBetween(0, 32),
		},
		"next_server": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "The IP address of the next server to use in bootstrap.",
			ValidateFunc: validation.IsIPv4Address,
		},
		"ntp_server": {
			Type:     schema.TypeList,
			Optional: true,
			Elem: &schema.Schema{
				Type:         schema.TypeString,
				ValidateFunc: validation.IsIPv4Address,
			},
			Description: "The DHCP client will use these as the default NTP servers. Two NTP servers " +
				"can be specified to be used by the DHCP client as primary and secondary NTP servers",
		},
		"wins_server": {
			Type:     schema.TypeList,
			Optional: true,
			Elem: &schema.Schema{
				Type:         schema.TypeString,
				ValidateFunc: validation.IsIPv4Address,
			},
			Description: "The Windows DHCP client will use these as the default WINS servers. Two WINS servers " +
				"can be specified to be used by the DHCP client as primary and secondary WINS servers",
		},
	}
	return &schema.Resource{
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
		SchemaVersion: 1,
		StateUpgraders: []schema.StateUpgrader{
			{
				Type: ResourceDhcpServerNetworkV0().CoreConfigSchema().ImpliedType(),
				Upgrade: stateMigrationScalarToList("caps_manager", "dhcp_option", "dns_server", "ntp_server", "wins_server"),
				Version: 0,
			},
		},
	}
}
================================================

File: resource_ip_dhcp_server_network_test.go
================================================
package routeros
import (
	"testing"
	"github.com/hashicorp/terraform-plugin-testing/helper/resource"
)
const testIpDhcpServerNetworkAddress = "routeros_ip_dhcp_server_network.test_dhcp"
func TestAccIpDhcpServerNetworkTest_basic(t *testing.T) {
	for _, name := range testNames {
		t.Run(name, func(t *testing.T) {
			resource.Test(t, resource.TestCase{
				PreCheck: func() {
					testAccPreCheck(t)
					testSetTransportEnv(t, name)
				},
				ProviderFactories: testAccProviderFactories,
				CheckDestroy:      testCheckResourceDestroy("/ip/dhcp-server/network", "routeros_ip_dhcp_server_network"),
				Steps: []resource.TestStep{
					{
						Config: testAccIpDhcpServerNetworkConfig(),
						Check: resource.ComposeTestCheckFunc(
							testResourcePrimaryInstanceId(testIpDhcpServerNetworkAddress),
							resource.TestCheckResourceAttr(testIpDhcpServerNetworkAddress, "address", "192.168.1.0/24"),
						),
					},
				},
			})
		})
	}
}
func testAccIpDhcpServerNetworkConfig() string {
	return providerConfig + `
resource "routeros_ip_dhcp_server_network" "test_dhcp" {
	address    = "192.168.1.0/24"
  }
`
}
================================================

File: resource_ip_dhcp_server_network_v0.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
// ResourceDhcpServerNetwork https://wiki.mikrotik.com/wiki/Manual:IP/DHCP_Server#Networks
func ResourceDhcpServerNetworkV0() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/ip/dhcp-server/network"),
		MetaId:           PropId(Id),
		"address": {
			Type:        schema.TypeString,
			Required:    true,
			Description: "The network DHCP server(s) will lease addresses from.",
		},
		"boot_file_name": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Boot filename.",
		},
		"caps_manager": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "A comma-separated list of IP addresses for one or more CAPsMAN system managers. " +
				"DHCP Option 138 (capwap) will be used.",
		},
		KeyComment: PropCommentRw,
		"dhcp_option": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Add additional DHCP options from the option list.",
		},
		"dhcp_option_set": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "Add an additional set of DHCP options.",
		},
		"dns_none": {
			Type:     schema.TypeBool,
			Optional: true,
			Description: "If set, then DHCP Server will not pass dynamic DNS servers configured on the router to the " +
				"DHCP clients if no DNS Server in DNS-server is set.",
		},
		"dns_server": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "the DHCP client will use these as the default DNS servers. Two comma-separated DNS servers " +
				"can be specified to be used by the DHCP client as primary and secondary DNS servers.",
		},
		"domain": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "The DHCP client will use this as the 'DNS domain' setting for the network adapter.",
		},
		KeyDynamic: PropDynamicRo,
		"gateway": {
			Type:         schema.TypeString,
			Optional:     true,
			Default:      "0.0.0.0",
			Description:  "The default gateway to be used by DHCP Client.",
			ValidateFunc: validation.IsIPv4Address,
		},
		"netmask": {
			Type:     schema.TypeInt,
			Optional: true,
			Default:  0,
			Description: "The actual network mask is to be used by the DHCP client. If set to '0' - netmask from " +
				"network address will be used.",
			ValidateFunc: validation.IntBetween(0, 32),
		},
		"next_server": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "The IP address of the next server to use in bootstrap.",
			ValidateFunc: validation.IsIPv4Address,
		},
		"ntp_server": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "The DHCP client will use these as the default NTP servers. Two comma-separated NTP servers " +
				"can be specified to be used by the DHCP client as primary and secondary NTP servers",
			ValidateFunc: validation.IsIPv4Address,
		},
		"wins_server": {
			Type:     schema.TypeString,
			Optional: true,
			Description: "The Windows DHCP client will use these as the default WINS servers. Two comma-separated " +
				"WINS servers can be specified to be used by the DHCP client as primary and secondary WINS servers",
			ValidateFunc: validation.IsIPv4Address,
		},
	}
	return &schema.Resource{
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: resource_system_script.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
/*
  {
    ".id": "*1",
    "dont-require-permissions": "false",
    "invalid": "false",
    "last-started": "jan/13/2023 00:16:01",
    "name": "unreg_died",
    "owner": "admin",
    "policy": "read,write,policy,password,sensitive",
    "run-count": "47",
    "source": ":log info \"TEST\";\r\n"
  }
*/
// ResourceSystemScript https://help.mikrotik.com/docs/display/ROS/Scripting#Scripting-Scriptrepository
func ResourceSystemScript() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/system/script"),
		MetaId:           PropId(Id),
		KeyComment: PropCommentRw,
		"dont_require_permissions": {
			Type:     schema.TypeBool,
			Optional: true,
			Description: "Bypass permissions check when the script is being executed, useful when scripts are being executed " +
				"from services that have limited permissions, such as Netwatch.",
		},
		KeyInvalid: PropInvalidRo,
		"last_started": {
			Type:        schema.TypeString,
			Computed:    true,
			Description: "Date and time when the script was last invoked.",
		},
		KeyName: PropName("Name of the script."),
		"owner": {
			Type:     schema.TypeString,
			Computed: true,
		},
		"policy": {
			Type:     schema.TypeSet,
			Computed: true,
			Optional: true,
			Elem: &schema.Schema{
				Type: schema.TypeString,
				ValidateFunc: validation.StringInSlice([]string{"ftp", "reboot", "read", "write", "policy", "test",
					"password", "sniff", "sensitive"}, false),
			},
			Description: `List of applicable policies:
	* ftp - Policy that grants full rights to log in remotely via FTP, to read/write/erase files and to transfer files from/to the router. Should be used together with read/write policies.  
	* password - Policy that grants rights to change the password.  
	* policy - Policy that grants user management rights. Should be used together with the write policy. Allows also to see global variables created by other users (requires also 'test' policy).  
	* read - Policy that grants read access to the router's configuration. All console commands that do not alter router's configuration are allowed. Doesn't affect FTP.  
	* reboot - Policy that allows rebooting the router.  
	* sensitive - Policy that grants rights to change "hide sensitive" option, if this policy is disabled sensitive information is not displayed.  
	* sniff - Policy that grants rights to use packet sniffer tool.  
	* test - Policy that grants rights to run ping, traceroute, bandwidth-test, wireless scan, snooper, and other test commands.  
	* write - Policy that grants write access to the router's configuration, except for user management. This policy does not allow to read the configuration, so make sure to enable read policy as well.  
policy = ["ftp", "read", "write"]
`,
		},
		"run_count": {
			Type:        schema.TypeString,
			Computed:    true,
			Description: "This counter is incremented each time the script is executed.",
		},
		"source": {
			Type:        schema.TypeString,
			Required:    true,
			Description: "Script source code.",
		},
	}
	return &schema.Resource{
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: resource_system_script_test.go
================================================
package routeros
import (
	"testing"
	"github.com/hashicorp/terraform-plugin-testing/helper/resource"
)
const testSystemScriptTask = "routeros_system_script.script"
func TestAccSystemScriptTest_basic(t *testing.T) {
	for _, name := range testNames {
		t.Run(name, func(t *testing.T) {
			resource.Test(t, resource.TestCase{
				PreCheck: func() {
					testAccPreCheck(t)
					testSetTransportEnv(t, name)
				},
				ProviderFactories: testAccProviderFactories,
				CheckDestroy:      testCheckResourceDestroy("/system/script", "routeros_script"),
				Steps: []resource.TestStep{
					{
						Config: testAccSystemScriptConfig(),
						Check: resource.ComposeTestCheckFunc(
							testResourcePrimaryInstanceId(testSystemScriptTask),
							resource.TestCheckResourceAttr(testSystemScriptTask, "name", "my_script"),
							resource.TestCheckTypeSetElemAttr(testSystemScriptTask, "policy.*", "read"),
							resource.TestCheckTypeSetElemAttr(testSystemScriptTask, "policy.*", "write"),
							resource.TestCheckTypeSetElemAttr(testSystemScriptTask, "policy.*", "test"),
							resource.TestCheckTypeSetElemAttr(testSystemScriptTask, "policy.*", "policy"),
						),
					},
				},
			})
		})
	}
}
func testAccSystemScriptConfig() string {
	return providerConfig + `
resource "routeros_system_script" "script" {
	name   = "my_script"
	source = <<EOF
	:log info "This is a test script created by Terraform."
	EOF
	policy = ["read", "write", "test", "policy"]
}
`
}
================================================

File: resource_user_manager_router.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)
/*
{
    ".id": "*1",
    "address": "127.0.0.1",
    "coa-port": "3799",
    "disabled": "false",
    "name": "test",
    "shared-secret": "password"
}
*/
// https://help.mikrotik.com/docs/display/ROS/User+Manager#UserManager-Routers
func ResourceUserManagerRouter() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/user-manager/router"),
		MetaId:           PropId(Id),
		"address": {
			Type:         schema.TypeString,
			Required:     true,
			Description:  "IP address of the RADIUS client.",
			ValidateFunc: ValidationIpAddress,
		},
		"coa_port": {
			Type:         schema.TypeInt,
			Optional:     true,
			Default:      3799,
			Description:  "Port number of CoA (Change of Authorization) communication.",
			ValidateFunc: Validation64k,
		},
		KeyDisabled: PropDisabledRw,
		KeyName:     PropName("Unique name of the RADIUS client."),
		"shared_secret": {
			Type:        schema.TypeString,
			Optional:    true,
			Sensitive:   true,
			Description: "The shared secret to secure communication.",
		},
	}
	return &schema.Resource{
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: resource_wifi_configuration.go
================================================
package routeros
import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/validation"
)
/*
{
    ".id": "*3",
    "aaa": "aaa1",
    "antenna-gain": "10",
    "beacon-interval": "1s",
    "chains": "0,1,2,3",
    "channel": "channel1",
    "country": "Netherlands",
    "datapath": "datapath1",
    "disabled": "false",
    "dtim-period": "1",
    "hide-ssid": "true",
    "interworking": "interworking1",
    "manager": "capsman",
    "mode": "ap",
    "multicast-enhance": "disabled",
    "name": "cfg1",
    "qos-classifier": "priority",
    "security": "security1",
    "security.connect-priority": "0",
    "ssid": "test",
    "steering": "steering1",
    "tx-chains": "4,5,6,7",
    "tx-power": "10"
}
*/
// https://help.mikrotik.com/docs/display/ROS/WiFi#WiFi-Configurationproperties
func ResourceWifiConfiguration() *schema.Resource {
	resSchema := map[string]*schema.Schema{
		MetaResourcePath: PropResourcePath("/interface/wifi/configuration"),
		MetaId:           PropId(Id),
		MetaTransformSet: PropTransformSet("aaa: aaa.config", "channel: channel.config", "datapath: datapath.config",
			"interworking: interworking.config", "security: security.config", "steering: steering.config"),
		"aaa": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "AAA inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"antenna_gain": {
			Type:         schema.TypeInt,
			Optional:     true,
			Description:  "An option overrides the default antenna gain.",
			ValidateFunc: validation.IntBetween(0, 30),
		},
		"beacon_interval": {
			Type:             schema.TypeString,
			Optional:         true,
			Description:      "Time interval between beacon frames.",
			DiffSuppressFunc: TimeEquall,
		},
		"chains": {
			Type:     schema.TypeSet,
			Optional: true,
			Elem: &schema.Schema{
				Type:         schema.TypeInt,
				ValidateFunc: validation.IntBetween(0, 7),
			},
			Description: "Radio chains to use for receiving signals.",
		},
		"channel": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "Channel inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		KeyComment: PropCommentRw,
		"country": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "An option determines which regulatory domain restrictions are applied to an interface.",
		},
		"datapath": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "Datapath inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		KeyDisabled: PropDisabledRw,
		"dtim_period": {
			Type:         schema.TypeInt,
			Optional:     true,
			Description:  "A period at which to transmit multicast traffic, when there are client devices in power save mode connected to the AP.",
			ValidateFunc: validation.IntBetween(1, 255),
		},
		"hide_ssid": {
			Type:     schema.TypeBool,
			Optional: true,
			Description: "This property has effect only in AP mode. Setting it to yes can remove this network from " +
				"the list of wireless networks that are shown by some client software. Changing this setting does not " +
				"improve the security of the wireless network, because SSID is included in other frames sent by the AP.",
		},
		"interworking": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "Interworking inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"manager": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "An option to specify the remote CAP mode.",
			ValidateFunc: validation.StringInSlice([]string{"capsman", "capsman-or-local", "local"}, false),
		},
		"mode": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "An option to specify the access point operational mode.",
			ValidateFunc: validation.StringInSlice([]string{"ap", "station", "station-bridge"}, false),
		},
		"multicast_enhance": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "An option to enable converting every multicast-address IP or IPv6 packet into multiple unicast-addresses frames for each connected station.",
			ValidateFunc: validation.StringInSlice([]string{"disabled", "enabled"}, false),
		},
		KeyName: PropName("Name of the configuration."),
		"qos_classifier": {
			Type:         schema.TypeString,
			Optional:     true,
			Description:  "An option to specify the QoS classifier.",
			ValidateFunc: validation.StringInSlice([]string{"dscp-high-3-bits", "priority"}, false),
		},
		"security": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "Security inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"ssid": {
			Type:        schema.TypeString,
			Optional:    true,
			Description: "SSID (service set identifier) is a name broadcast in the beacons that identifies wireless network.",
		},
		"steering": {
			Type:             schema.TypeMap,
			Optional:         true,
			Elem:             &schema.Schema{Type: schema.TypeString},
			Description:      "Steering inline settings.",
			DiffSuppressFunc: AlwaysPresentNotUserProvided,
		},
		"tx_chains": {
			Type:     schema.TypeSet,
			Optional: true,
			Elem: &schema.Schema{
				Type:         schema.TypeInt,
				ValidateFunc: validation.IntBetween(0, 7),
			},
			Description: "Radio chains to use for transmitting signals.",
		},
		"tx_power": {
			Type:         schema.TypeInt,
			Optional:     true,
			Description:  "A limit on the transmit power (in dBm) of the interface.",
			ValidateFunc: validation.IntBetween(0, 40),
		},
	}
	return &schema.Resource{
		Description:   `*<span style="color:red">This resource requires a minimum version of RouterOS 7.13.</span>*`,
		CreateContext: DefaultCreate(resSchema),
		ReadContext:   DefaultRead(resSchema),
		UpdateContext: DefaultUpdate(resSchema),
		DeleteContext: DefaultDelete(resSchema),
		Importer: &schema.ResourceImporter{
			StateContext: schema.ImportStatePassthroughContext,
		},
		Schema: resSchema,
	}
}
================================================

File: easy_import.md
================================================
# Install package
Original [issue](https://github.com/terraform-routeros/terraform-provider-routeros/issues/488)
## Example
```shell
#!/bin/bash
USER=admin
PASS=
HOST=http://router.local
i=0
curl -s -u ${USER}:${PASS} ${HOST}/rest/ip/firewall/address-list | jq -c '.[] | select(.dynamic | ascii_downcase == "false") | {index: .".id", address: .address, comment: .comment, list: .list}'  | while read rec; do
  index=$(echo $rec | jq .index)
  idx=$(printf "%00004d" $i)
  # echo $rec
  bash -cv "tofu state rm 'module.dev-gw0.routeros_ip_firewall_addr_list.address_list[\"$idx\"]'"
  bash -cv "tofu import 'module.dev-gw0.routeros_ip_firewall_addr_list.address_list[\"$idx\"]' $index"
  let i=${i}+1
done
```
```terraform
variable "address_list" {
  type = list(object({
    address = string
    comment = optional(string)
    disabled = optional(bool, false)
    dynamic  = optional(bool, false)
    list     = string
  }))
  default = [
    { address="192.168.88.11", comment="example 2", list="srv" },
    { address="192.168.88.12", comment="example 2", list="srv" },
    { address="192.168.88.1", comment="example", list="routeros" },
]
locals {
  # https://discuss.hashicorp.com/t/does-map-sort-keys/12056/2
  # Map keys are always iterated in lexicographical order!
  address_list_map = { for idx, rule in var.address_list : format("%00004d", idx) => rule }
}
resource "routeros_ip_firewall_addr_list" "address_list" {
  for_each = local.address_list_map
  address  = each.value.address
  comment  = each.value.comment
  disabled = each.value.disabled
  list     = each.value.list
}
```
================================================

File: install_package.md
================================================
# Install package
The original example package installation is available in the [Schwitzd](https://github.com/Schwitzd/IaC-HomeRouter/blob/main/container_backend.tf) repository.
## Example
```terraform
resource "null_resource" "download_container_npk" {
  provisioner "local-exec" {
    command = <<EOT
      chmod +x ./helper/download_routeros_packages.sh
      ./helper/download_routeros_packages.sh ${local.system_architecture} "${local.system_version}" "container"
    EOT
  }
}
resource "null_resource" "upload_container_npk" {
  provisioner "local-exec" {
    command = "scp -i ${local.router_ssh_key} \"/tmp/routeros_packages/${local.container_npk_name}\" ${local.router_user}@${var.router_ip}:/${local.container_npk_name}"
  }
  depends_on = [ null_resource.download_container_npk ]
}
resource "null_resource" "install_container_npk" {
  provisioner "local-exec" {
      command = <<EOT
        ssh -i ${local.router_ssh_key} ${local.router_user}@${var.router_ip} '/system reboot'; sleep 3
        until ssh -i ${local.router_ssh_key} -o ConnectTimeout=2 ${local.router_user}@${var.router_ip} ':put True' 2> /dev/null
        do
          echo "Waiting for router to reboot and become available..."
          sleep 10
        done
      EOT
  }
  depends_on = [ null_resource.upload_container_npk ]
}
```
```shell
#!/bin/bash
# Input parameters
ARCHITECTURE_NAME=$1
VERSION=$2
PACKAGE_NAME_PREFIX=$3
# Define the base URL and package format
BASE_URL="https://download.mikrotik.com/routeros"
PACKAGE_FORMAT="all_packages-${ARCHITECTURE_NAME}-${VERSION}.zip"
# Construct the full URL
FULL_URL="${BASE_URL}/${VERSION}/${PACKAGE_FORMAT}"
# Define the download and extraction paths
DOWNLOAD_PATH="/tmp/${PACKAGE_FORMAT}"
EXTRACT_PATH="/tmp/routeros_packages"
# Download the package
echo "Downloading package from: ${FULL_URL}"
curl -o "${DOWNLOAD_PATH}" "${FULL_URL}"
# Verify download
if [ $? -ne 0 ]; then
  echo "Failed to download the package."
  exit 1
fi
# Create the extraction directory
mkdir -p "${EXTRACT_PATH}"
# List all files in the ZIP archive and filter by the PACKAGE_NAME_PREFIX
echo "Finding package that starts with: ${PACKAGE_NAME_PREFIX}"
MATCHED_FILES=$(unzip -l "${DOWNLOAD_PATH}" | awk '{print $4}' | grep "^${PACKAGE_NAME_PREFIX}")
# Check if any files were matched
if [ -z "$MATCHED_FILES" ]; then
  echo "No files found starting with '${PACKAGE_NAME_PREFIX}'."
  exit 1
fi
# Extract matched files
for FILE in $MATCHED_FILES; do
  echo "Extracting: ${FILE}"
  unzip -jo "${DOWNLOAD_PATH}" "${FILE}" -d "${EXTRACT_PATH}"
  if [ $? -ne 0 ]; then
    echo "Failed to extract: ${FILE}"
    exit 1
  fi
done
echo "Extraction completed successfully in: ${EXTRACT_PATH}"
```
================================================

File: dhcp_server_network.md.tmpl
================================================
# {{.Name}} ({{.Type}})
---
#### This is an alias for backwards compatibility between plugin versions. 
Please see documentation for [routeros_ip_dhcp_server_network](ip_dhcp_server_network.md)
================================================