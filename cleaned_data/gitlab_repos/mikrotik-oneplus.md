# Repository Information
Name: mikrotik-oneplus

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
	url = https://gitlab.com/the-creators2/mikrotik-oneplus.git
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
stages:
  - environment
  - build
  - test
  - internal
  - alpha
  - beta
  - production
.updateContainerJob:
  image: docker:stable
  stage: environment
  services:
    - docker:dind
  script:
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN $CI_REGISTRY
    - docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG || true
    - docker build --cache-from $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG -t $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
updateContainer:
  extends: .updateContainerJob
  only:
    changes:
      - Dockerfile
ensureContainer:
  extends: .updateContainerJob
  allow_failure: true
  before_script:
    - "mkdir -p ~/.docker && echo '{\"experimental\": \"enabled\"}' > ~/.docker/config.json"
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN $CI_REGISTRY
    # Skip update container `script` if the container already exists
    # via https://gitlab.com/gitlab-org/gitlab-ce/issues/26866#note_97609397 -> https://stackoverflow.com/a/52077071/796832
    - docker manifest inspect $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG > /dev/null && exit || true
  except:
    changes:
      - Dockerfile
.build_job:
  image: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
  stage: build
  before_script:
    - chmod +x gradlew
    - "export VERSION_CODE=$(($CI_PIPELINE_IID)) && echo $VERSION_CODE"
    - "export VERSION_SHA=`echo ${CI_COMMIT_SHA:0:8}` && echo $VERSION_SHA"
  artifacts:
    paths:
      - app/build/outputs
buildDebug:
  extends: .build_job
  script:
    - bundle exec fastlane buildDebug
buildRelease:
  extends: .build_job
  script:
    - bundle exec fastlane buildRelease
  environment:
    name: production
testDebug:
  image: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
  stage: test
  dependencies:
    - buildDebug
  script:
    - chmod +x gradlew
    - bundle exec fastlane test
.promote_job:
  image: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
  when: manual
  dependencies: [ ]
  before_script:
    - echo You need to add your google_play_api_key.json file for this to work. Please see project's README.md. && false
    - chmod +x gradlew
  after_script:
    - rm -f ~/google_play_api_key.json
publishInternal:
  extends: .promote_job
  image: $CI_REGISTRY_IMAGE:$CI_COMMIT_REF_SLUG
  stage: internal
  dependencies:
    - buildRelease
  when: manual
  script:
    - bundle exec fastlane internal
promoteAlpha:
  extends: .promote_job
  stage: alpha
  script:
    - bundle exec fastlane promote_internal_to_alpha
promoteBeta:
  extends: .promote_job
  stage: beta
  script:
    - bundle exec fastlane promote_alpha_to_beta
promoteProduction:
  extends: .promote_job
  stage: production
  # We only allow production promotion on master because
  # in this way you can protect production scoped secret variables
  only:
    - master
  script:
    - bundle exec fastlane promote_beta_to_production
================================================

File: CONTRIBUTING.md
================================================
## Developer Certificate of Origin and License
By contributing to GitLab B.V., you accept and agree to the following terms and
conditions for your present and future contributions submitted to GitLab B.V.
Except for the license granted herein to GitLab B.V. and recipients of software
distributed by GitLab B.V., you reserve all right, title, and interest in and to
your Contributions.
All contributions are subject to the Developer Certificate of Origin and license set out at [docs.gitlab.com/ce/legal/developer_certificate_of_origin](https://docs.gitlab.com/ce/legal/developer_certificate_of_origin).
_This notice should stay as the first item in the CONTRIBUTING.md file._
## Code of conduct
As contributors and maintainers of this project, we pledge to respect all people
who contribute through reporting issues, posting feature requests, updating
documentation, submitting pull requests or patches, and other activities.
We are committed to making participation in this project a harassment-free
experience for everyone, regardless of level of experience, gender, gender
identity and expression, sexual orientation, disability, personal appearance,
body size, race, ethnicity, age, or religion.
Examples of unacceptable behavior by participants include the use of sexual
language or imagery, derogatory comments or personal attacks, trolling, public
or private harassment, insults, or other unprofessional conduct.
Project maintainers have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct. Project maintainers who do not follow the
Code of Conduct may be removed from the project team.
This code of conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community.
Instances of abusive, harassing, or otherwise unacceptable behavior can be
reported by emailing contact@gitlab.com.
This Code of Conduct is adapted from the [Contributor Covenant](https://contributor-covenant.org), version 1.1.0,
available at [https://contributor-covenant.org/version/1/1/0/](https://contributor-covenant.org/version/1/1/0/).
================================================

File: Dockerfile
================================================
# This Dockerfile creates a static build image for CI
FROM eclipse-temurin:17
# Just matched `app/build.gradle.kts`
ENV ANDROID_COMPILE_SDK "33"
# Just matched `app/build.gradle.kts`
ENV ANDROID_BUILD_TOOLS "33.0.2"
ENV ANDROID_HOME /android-sdk-linux
ENV PATH="${PATH}:/android-sdk-linux/platform-tools/"
# install OS packages
RUN apt-get --quiet update --yes
RUN apt-get --quiet install --yes wget apt-utils tar unzip lib32stdc++6 lib32z1 build-essential ruby ruby-dev
# We use this for xxd hex->binary
RUN apt-get --quiet install --yes vim-common
# install Android SDK
RUN wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
RUN unzip android-sdk.zip -d android-sdk-linux/
RUN mkdir android-sdk-linux/cmdline-tools/latest
RUN mv android-sdk-linux/cmdline-tools/* android-sdk-linux/cmdline-tools/latest || true
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}"
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "platform-tools"
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}"
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "extras;android;m2repository"
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "extras;google;google_play_services"
RUN echo y | android-sdk-linux/cmdline-tools/latest/bin/sdkmanager "extras;google;m2repository"
# install FastLane
COPY Gemfile.lock .
COPY Gemfile .
RUN gem install bundler
RUN bundle install
RUN bundle update fastlane
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2019-Present GitLab B.V.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
# Introduction
This is a template for doing Android development using GitLab and [fastlane](https://fastlane.tools/).
It is based on the tutorial for Android apps in general that can be found [here](https://developer.android.com/training/basics/firstapp/). 
If you're learning Android at the same time, you can also follow along that
tutorial and learn how to do everything all at once.
# Reference links
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)
- [Blog post: Android publishing with GitLab and fastlane](https://about.gitlab.com/2019/01/28/android-publishing-with-gitlab-and-fastlane/)
You'll definitely want to read through the blog post since that walks you in detail
through a working production configuration using this model.
# Getting started
First thing is to follow the [Android tutorial](https://developer.android.com/training/basics/firstapp/) and
get Android Studio installed on your machine, so you can do development using
the Android IDE. Other IDE options are possible, but not directly described or
supported here. If you're using your own IDE, it should be fairly straightforward
to convert these instructions to use with your preferred toolchain.
## What's contained in this project
### Android code
The state of this project is as if you followed the first few steps in the linked
[Android tutorial](https://developer.android.com/training/basics/firstapp/) and
have created your project. You're definitely going to want to open up the
project and change the settings to match what you plan to build. In particular,
you're at least going to want to change the following:
- Application Name: "My First App"
- Company Domain: "example.com"
### Fastlane files
It also has fastlane setup per our [blog post](https://about.gitlab.com/2019/01/28/android-publishing-with-gitlab-and-fastlane/) on
getting GitLab CI set up with fastlane. Note that you may want to update your
fastlane bundle to the latest version; if a newer version is available, the pipeline
job output will tell you.
### Dockerfile build environment
In the root there is a Dockerfile which defines a build environment which will be
used to ensure consistent and reliable builds of your Android application using
the correct Android SDK and other details you expect. Feel free to add any
build-time tools or whatever else you need here.
We generate this environment as needed because installing the Android SDK
for every pipeline run would be very slow.
### Gradle configuration
The gradle configuration is exactly as output by Android Studio except for the
version name being updated to 
Instead of:
`versionName "1.0"`
It is now set to:
`versionName "1.0-${System.env.VERSION_SHA}"`
You'll want to update this for whatever versioning scheme you prefer.
### Build configuration (`.gitlab-ci.yml`)
The sample project also contains a basic `.gitlab-ci.yml` which will successfully 
build the Android application.
Note that for publishing to the test channels or production, you'll need to set
up your secret API key. The stub code is here for that, but please see our
[blog post](https://about.gitlab.com/2019/01/28/android-publishing-with-gitlab-and-fastlane/) for
details on how to set this up completely. In the meantime, publishing steps will fail.
The build script also handles automatic versioning by relying on the CI pipeline
ID to generate a unique, ever increasing number. If you have a different versioning
scheme you may want to change this.
```yaml
    - "export VERSION_CODE=$(($CI_PIPELINE_IID)) && echo $VERSION_CODE"
    - "export VERSION_SHA=`echo ${CI_COMMIT_SHA:0:8}` && echo $VERSION_SHA"
```
================================================