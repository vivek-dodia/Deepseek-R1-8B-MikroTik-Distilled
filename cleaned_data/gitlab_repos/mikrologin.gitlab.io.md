# Repository Information
Name: mikrologin.gitlab.io

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
	url = https://gitlab.com/ghoblin/mikrologin.gitlab.io.git
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
# This file is a template, and might need editing before it works on your project.
# Full project: https://gitlab.com/pages/plain-html
pages:
  stage: deploy
  script:
  - mkdir .public
  - cp -r * .public
  - mv .public public
  artifacts:
    paths:
    - public
  only:
  - master
================================================

File: index.html
================================================
Hello World! Welcome to my website
================================================

File: index.html
================================================
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
    <h1>Hello Gitlab Pages</h1>
    </body>
</html>
================================================

File: README.md
================================================
# mikrologin.gitlab.io
Mikrotik Login Page