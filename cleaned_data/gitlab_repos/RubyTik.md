# Repository Information
Name: RubyTik

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
	url = https://gitlab.com/HyperBit-IT/RubyGems/RubyTik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: gem-push.yml
================================================
name: Ruby Gem
on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]
jobs:
  build:
    name: Build + Publish
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
    - uses: actions/checkout@v3
    - name: Set up Ruby 2.6
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: 3.2.0
        bundler-cache: true
    - name: Publish to GPR
      run: |
        mkdir -p $HOME/.gem
        touch $HOME/.gem/credentials
        chmod 0600 $HOME/.gem/credentials
        printf -- "---\n:github: ${GEM_HOST_API_KEY}\n" > $HOME/.gem/credentials
        gem build *.gemspec
        gem push --KEY github --host https://rubygems.pkg.github.com/${OWNER} *.gem
      env:
        GEM_HOST_API_KEY: "Bearer ${{secrets.GITHUB_TOKEN}}"
        OWNER: ${{ github.repository_owner }}
================================================

File: .gitlab-ci.yml
================================================
default:
  image: ruby:3.1.3
  before_script:
    - gem install bundler -v 2.3.26
    - bundle install
    - mkdir ~/.gem
    - echo "---" > ~/.gem/credentials
    - |
      echo "${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/rubygems: '${CI_JOB_TOKEN}'" >> ~/.gem/credentials
    - chmod 0600 ~/.gem/credentials
Build:
  script:
    - gem build *.gemspec
================================================

File: .rubocop.yml
================================================
AllCops:
  TargetRubyVersion: 2.6
Style/StringLiterals:
  Enabled: true
  EnforcedStyle: double_quotes
Style/StringLiteralsInInterpolation:
  Enabled: true
  EnforcedStyle: double_quotes
Layout/LineLength:
  Max: 120
================================================

File: CHANGELOG.md
================================================
## [Unreleased]
## [0.1.0] - 2023-01-22
- Initial release
================================================

File: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct
## Our Pledge
We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.
We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.
## Our Standards
Examples of behavior that contributes to a positive environment for our community include:
* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall community
Examples of unacceptable behavior include:
* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting
## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any behavior that they deem inappropriate, threatening, offensive, or harmful.
Community leaders have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, and will communicate reasons for moderation decisions when appropriate.
## Scope
This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public spaces. Examples of representing our community include using an official e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event.
## Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible for enforcement at mail@francescomasala.me. All complaints will be reviewed and investigated promptly and fairly.
All community leaders are obligated to respect the privacy and security of the reporter of any incident.
## Enforcement Guidelines
Community leaders will follow these Community Impact Guidelines in determining the consequences for any action they deem in violation of this Code of Conduct:
### 1. Correction
**Community Impact**: Use of inappropriate language or other behavior deemed unprofessional or unwelcome in the community.
**Consequence**: A private, written warning from community leaders, providing clarity around the nature of the violation and an explanation of why the behavior was inappropriate. A public apology may be requested.
### 2. Warning
**Community Impact**: A violation through a single incident or series of actions.
**Consequence**: A warning with consequences for continued behavior. No interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, for a specified period of time. This includes avoiding interactions in community spaces as well as external channels like social media. Violating these terms may lead to a temporary or permanent ban.
### 3. Temporary Ban
**Community Impact**: A serious violation of community standards, including sustained inappropriate behavior.
**Consequence**: A temporary ban from any sort of interaction or public communication with the community for a specified period of time. No public or private interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, is allowed during this period. Violating these terms may lead to a permanent ban.
### 4. Permanent Ban
**Community Impact**: Demonstrating a pattern of violation of community standards, including sustained inappropriate behavior,  harassment of an individual, or aggression toward or disparagement of classes of individuals.
**Consequence**: A permanent ban from any sort of public interaction within the community.
## Attribution
This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 2.0,
available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.
Community Impact Guidelines were inspired by [Mozilla's code of conduct enforcement ladder](https://github.com/mozilla/diversity).
[homepage]: https://www.contributor-covenant.org
For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at https://www.contributor-covenant.org/translations.
================================================

File: LICENSE.txt
================================================
The MIT License (MIT)
Copyright (c) 2023 Francesco Masala - HyperBit SRLs
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
================================================

File: README-IT.md
================================================
# RubyTik - 🇮🇹
## Informazioni su RubyTik
RubyTik è un client API per la gestione di router Mikrotik con un endpoint HTTPS.
## Installazione
Installare la gem e aggiungerla al Gemfile dell'applicazione eseguendo:
    $ bundle add RubyBill
Se bundler non viene utilizzato per gestire le dipendenze, installare la gem eseguendo:
    $ gem install RubyBill
## Utilizzo
Software attualmente in fase di sviluppo, non ancora pronto per l'uso.
## Sviluppo
Dopo aver effettuato il `git clone` della repository, eseguire `bin/setup` per installare le dipendenze. Poi,
eseguire `rake test` per eseguire i test. È anche possibile eseguire `bin/console` per un prompt interattivo che
consente di esperimentare.
Per installare questa gem sul proprio computer, eseguire `bundle exec rake install`. Per rilasciare una nuova versione,
aggiornare il numero di versione in `version.rb`, quindi eseguire `bundle exec rake release`, che creerà un tag git per
la versione, invierà i commit git e il tag creato e invierà il file `.gem` a [rubygems.org](https://rubygems.org).
## Contribuire
Eventuali issue e pull request sono benvenute su GitLab all'indirizzo https://gitlab.com/HyperBit-IT/RubyGems/RubyTik.
Questo progetto è inteso come un luogo sicuro e accogliente per la comunità, e gli sviluppatori sono invitati ad
adottare il [codice di condotta](https://gitlab.com/HyperBit-IT/RubyGems/RubyBill/blob/master/CODE_OF_CONDUCT.md).
## Licenza
La gem è disponibile come open source sotto i termini della [Licenza MIT](https://opensource.org/licenses/MIT).
## Codice di Condotta
Tutti coloro che interagiscono con il codice sorgente del progetto RubyTik, i bug-tracker e le chat sono tenuti a
seguire il [codice di condotta](https://gitlab.com/HyperBit-IT/RubyGems/RubyTik/blob/master/CODE_OF_CONDUCT.md).
================================================

File: README.md
================================================
# RubyTik - 🇬🇧
Per la versione 🇮🇹 premi [qui](https://gitlab.com/HyperBit-IT/RubyGems/RubyTik/blob/master/README-IT.md).
## About RubyTik
RubyTik is a API client for managing Mikrotik routers with an HTTPS endpoint.
## Installation
Install the gem and add to the application's Gemfile by executing:
    $ bundle add RubyTik
If bundler is not being used to manage dependencies, install the gem by executing:
    $ gem install RubyTik
## Usage
Software currently in development, not yet ready for use.
## Development
After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake test` to run the tests. You can
also run `bin/console` for an interactive prompt that will allow you to experiment.
To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the
version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version,
push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).
## Contributing
Bug reports and pull requests are welcome on GitLab at https://gitlab.com/HyperBit-IT/RubyGems/RubyTik. This project is intended
to be a safe, welcoming space for collaboration, and contributors are expected to adhere to
the [code of conduct](https://gitlab.com/HyperBit-IT/RubyGems/RubyTik/blob/master/CODE_OF_CONDUCT.md).
## License
The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
## Code of Conduct - 🇬🇧
Everyone interacting in the RubyBill project's codebases, issue trackers, chat rooms and mailing lists is expected to
follow the [code of conduct](https://gitlab.com/HyperBit-IT/RubyGems/RubyTik/blob/master/CODE_OF_CONDUCT.md).
================================================