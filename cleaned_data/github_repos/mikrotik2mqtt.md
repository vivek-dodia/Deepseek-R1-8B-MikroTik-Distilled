# Repository Information
Name: mikrotik2mqtt

# Directory Structure
Directory structure:
└── github_repos/mikrotik2mqtt/
    ├── .dockerignore
    ├── .editorconfig
    ├── .env
    │   ├── config
    │   ├── description
    │   ├── HEAD
    │   ├── hooks/
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   ├── push-to-checkout.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info/
    │   │   └── exclude
    │   ├── logs/
    │   │   ├── HEAD
    │   │   └── refs/
    │   │       ├── heads/
    │   │       │   └── main
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-e501b46982e96f4ac1061e04e4206ee3050d7972.idx
    │   │       └── pack-e501b46982e96f4ac1061e04e4206ee3050d7972.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── bin/
    │   ├── composer
    │   └── console
    ├── composer.json
    ├── composer.lock
    ├── config/
    │   ├── bundles.php
    │   ├── packages/
    │   │   ├── cache.yaml
    │   │   ├── dev/
    │   │   │   └── monolog.yaml
    │   │   ├── framework.yaml
    │   │   ├── prod/
    │   │   │   ├── deprecations.yaml
    │   │   │   ├── monolog.yaml
    │   │   │   └── routing.yaml
    │   │   ├── routing.yaml
    │   │   └── test/
    │   │       ├── framework.yaml
    │   │       └── monolog.yaml
    │   ├── preload.php
    │   └── services.yaml
    ├── docker-compose.yml
    ├── docker-image-generator.sh
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── src/
    │   ├── Application/
    │   │   └── Mikrotik/
    │   │       ├── Get/
    │   │       │   ├── GetMikrotikCommand.php
    │   │       │   └── GetMikrotikCommandHandler.php
    │   │       └── Save/
    │   │           ├── SaveMikrotikCommand.php
    │   │           └── SaveMikrotikCommandHandler.php
    │   ├── Domain/
    │   │   └── Model/
    │   │       └── Mikrotik/
    │   │           └── MikrotikRepository.php
    │   ├── Entrypoint/
    │   │   └── Console/
    │   │       └── Command/
    │   │           └── RunCommand.php
    │   ├── Infrastructure/
    │   │   ├── Domain/
    │   │   │   └── Model/
    │   │   │       └── Mikrotik/
    │   │   │           ├── MqttMikrotikRepository.php
    │   │   │           └── RouterOsMikrotikRepository.php
    │   │   └── Service/
    │   │       ├── FormatMikrotikDuration.php
    │   │       ├── MqttClient.php
    │   │       ├── MqttClientFactory.php
    │   │       ├── RouterOsClient.php
    │   │       └── RouterOsClientFactory.php
    │   └── Kernel.php
    ├── symfony.lock
    └── tests/
        └── .gitkeep


# Content
File: /.dockerignore
/.git
/.idea
/tests
/var
/vendor
/.editorconfig
/.env.local.php
/.gitignore
/docker-compose.yml
/docker-image-generator.sh
/Dockerfile
/Makefile
/README.md


File: /.editorconfig
[*.{yml,yaml}]
indent_size = 2
indent_style = space


File: /.env
# In all environments, the following files are loaded if they exist,
# the latter taking precedence over the former:
#
#  * .env                contains default values for the environment variables needed by the app
#  * .env.local          uncommitted file with local overrides
#  * .env.$APP_ENV       committed environment-specific defaults
#  * .env.$APP_ENV.local uncommitted environment-specific overrides
#
# Real environment variables win over .env files.
#
# DO NOT DEFINE PRODUCTION SECRETS IN THIS FILE NOR IN ANY OTHER COMMITTED FILES.
#
# Run "composer dump-env prod" to compile .env files for production use (requires symfony/flex >=1.2).
# https://symfony.com/doc/current/best_practices.html#use-environment-variables-for-infrastructure-configuration

###> symfony/framework-bundle ###
APP_ENV=dev
APP_SECRET=43379aa3ab57465faa6c1aa3e24caee4
###< symfony/framework-bundle ###

UPDATE_TIME=60

###> evilfreelancer/routeros-api-php ###
MIKROTIK_HOST=192.168.88.1
MIKROTIK_USE_SSL=0
MIKROTIK_USER=mikrotik2mqtt
MIKROTIK_PASSWORD=mikrotik2mqtt
###< evilfreelancer/routeros-api-php ###

###> php-mqtt/client ###
MQTT_HOST=192.168.88.2
MQTT_PORT=1883
MQTT_USE_TLS=0
MQTT_USERNAME=
MQTT_PASSWORD=
MQTT_CLIENT_ID=mikrotik2mqtt
MQTT_TOPIC_BASE=mikrotik2mqtt
###< php-mqtt/client ###


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/zoilomora/mikrotik2mqtt.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/main


File: /.git\hooks\applypatch-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:


File: /.git\hooks\commit-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}


File: /.git\hooks\fsmonitor-watchman.sample
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
File: /.git\hooks\post-update.sample
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info


File: /.git\hooks\pre-applypatch.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:


File: /.git\hooks\pre-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --


File: /.git\hooks\pre-merge-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:


File: /.git\hooks\pre-push.sample
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0


File: /.git\hooks\pre-rebase.sample
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END


File: /.git\hooks\pre-receive.sample
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi


File: /.git\hooks\prepare-commit-msg.sample
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi


File: /.git\hooks\push-to-checkout.sample
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi


File: /.git\hooks\update.sample
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0


File: /.git\info\exclude
File: /.git\logs\HEAD
0000000000000000000000000000000000000000 f6ca23dda1591129debd5b66367386feb8768908 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/zoilomora/mikrotik2mqtt.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 f6ca23dda1591129debd5b66367386feb8768908 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/zoilomora/mikrotik2mqtt.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 f6ca23dda1591129debd5b66367386feb8768908 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/zoilomora/mikrotik2mqtt.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
f6ca23dda1591129debd5b66367386feb8768908 refs/remotes/origin/main
6c1958db3100fe5a5dd4b286b930aebd4bc02fbd refs/tags/1.0.0
f6ca23dda1591129debd5b66367386feb8768908 refs/tags/1.0.1


File: /.git\refs\heads\main
f6ca23dda1591129debd5b66367386feb8768908


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
# phpstorm project files
.idea

# netbeans project files
nbproject/*

# zend studio for eclipse project files
.buildpath
.project
.settings

# windows thumbnail cache
Thumbs.db

# Mac DS_Store Files
File: /bin\console
#!/usr/bin/env php
<?php

use App\Kernel;
use Symfony\Bundle\FrameworkBundle\Console\Application;
use Symfony\Component\Console\Input\ArgvInput;
use Symfony\Component\Dotenv\Dotenv;
use Symfony\Component\ErrorHandler\Debug;

if (!in_array(PHP_SAPI, ['cli', 'phpdbg', 'embed'], true)) {
    echo 'Warning: The console should be invoked via the CLI version of PHP, not the '.PHP_SAPI.' SAPI'.PHP_EOL;
}

set_time_limit(0);

require dirname(__DIR__).'/vendor/autoload.php';

if (!class_exists(Application::class) || !class_exists(Dotenv::class)) {
    throw new LogicException('You need to add "symfony/framework-bundle" and "symfony/dotenv" as Composer dependencies.');
}

$input = new ArgvInput();
if (null !== $env = $input->getParameterOption(['--env', '-e'], null, true)) {
    putenv('APP_ENV='.$_SERVER['APP_ENV'] = $_ENV['APP_ENV'] = $env);
}

if ($input->hasParameterOption('--no-debug', true)) {
    putenv('APP_DEBUG='.$_SERVER['APP_DEBUG'] = $_ENV['APP_DEBUG'] = '0');
}

(new Dotenv())->bootEnv(dirname(__DIR__).'/.env');

if ($_SERVER['APP_DEBUG']) {
    umask(0000);

    if (class_exists(Debug::class)) {
        Debug::enable();
    }
}

$kernel = new Kernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$application = new Application($kernel);
$application->run($input);


File: /composer.json
{
    "name": "zoilomora/mikrotik2mqtt",
    "description": "MikroTik (RouterOS) to MQTT",
    "type": "project",
    "license": "Apache-2.0",
    "authors": [
        {
            "name": "Zoilo Mora",
            "email": "zoilo.mora@hotmail.com"
        }
    ],
    "require": {
        "php": ">=8.0",
        "ext-ctype": "*",
        "ext-iconv": "*",
        "evilfreelancer/routeros-api-php": "^1.4",
        "php-mqtt/client": "^1.1",
        "symfony/console": "5.2.*",
        "symfony/dotenv": "5.2.*",
        "symfony/flex": "^1.3.1",
        "symfony/framework-bundle": "5.2.*",
        "symfony/monolog-bundle": "^3.7",
        "symfony/yaml": "5.2.*"
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": {
            "*": "dist"
        },
        "sort-packages": true
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "App\\Tests\\": "tests/"
        }
    },
    "replace": {
        "symfony/polyfill-ctype": "*",
        "symfony/polyfill-iconv": "*",
        "symfony/polyfill-php72": "*"
    },
    "scripts": {
        "auto-scripts": {
            "cache:clear": "symfony-cmd"
        },
        "post-install-cmd": [
            "@auto-scripts"
        ],
        "post-update-cmd": [
            "@auto-scripts"
        ]
    },
    "conflict": {
        "symfony/symfony": "*"
    },
    "extra": {
        "symfony": {
            "allow-contrib": false,
            "require": "5.2.*"
        }
    }
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "6a76711c89f8630ff817a6a153bf66fc",
    "packages": [
        {
            "name": "divineomega/php-ssh-connection",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/DivineOmega/php-ssh-connection.git",
                "reference": "d6c8326cf376777df828372e494dc1b6a1be2a89"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/DivineOmega/php-ssh-connection/zipball/d6c8326cf376777df828372e494dc1b6a1be2a89",
                "reference": "d6c8326cf376777df828372e494dc1b6a1be2a89",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "phpseclib/phpseclib": "^2.0"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.0",
                "phpunit/phpunit": "^7.0||^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DivineOmega\\SSHConnection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-3.0-only"
            ],
            "authors": [
                {
                    "name": "Jordan Hall",
                    "email": "jordan@hall05.co.uk"
                }
            ],
            "description": "Provides an elegant syntax to connect to SSH servers and execute commands.",
            "support": {
                "issues": "https://github.com/DivineOmega/php-ssh-connection/issues",
                "source": "https://github.com/DivineOmega/php-ssh-connection/tree/v2.2.0"
            },
            "time": "2020-05-27T22:58:17+00:00"
        },
        {
            "name": "evilfreelancer/routeros-api-php",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/EvilFreelancer/routeros-api-php.git",
                "reference": "dd687894add2bc82c6db6b903022329a3db07641"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/EvilFreelancer/routeros-api-php/zipball/dd687894add2bc82c6db6b903022329a3db07641",
                "reference": "dd687894add2bc82c6db6b903022329a3db07641",
                "shasum": ""
            },
            "require": {
                "divineomega/php-ssh-connection": "^2.2",
                "ext-sockets": "*",
                "php": "^7.2|^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.16",
                "larapack/dd": "^1.1",
                "limedeck/phpunit-detailed-printer": "^5.0",
                "orchestra/testbench": "^4.0|^5.0",
                "phpunit/phpunit": "^8.0",
                "rector/rector": "^0.7|^0.8|^0.9",
                "roave/security-advisories": "dev-master",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "RouterOS\\Laravel\\ServiceProvider"
                    ],
                    "aliases": {
                        "RouterOS": "RouterOS\\Laravel\\Facade"
                    }
                }
            },
            "autoload": {
                "psr-4": {
                    "RouterOS\\": "./src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paul Rock",
                    "email": "paul@drteam.rocks",
                    "homepage": "http://drteam.rocks/",
                    "role": "Developer"
                }
            ],
            "description": "Modern Mikrotik RouterOS API PHP client for your applications (with Laravel support)",
            "keywords": [
                "PSR-4",
                "facade",
                "laravel",
                "mikrotik",
                "plugin",
                "routeros",
                "socket-client"
            ],
            "support": {
                "issues": "https://github.com/EvilFreelancer/routeros-api-php/issues",
                "source": "https://github.com/EvilFreelancer/routeros-api-php/tree/1.4.0"
            },
            "funding": [
                {
                    "url": "https://streamlabs.com/evilfreelancer/tip",
                    "type": "custom"
                },
                {
                    "url": "https://www.donationalerts.com/r/evilfreelancer",
                    "type": "custom"
                },
                {
                    "url": "https://ko-fi.com/efreelancer",
                    "type": "ko_fi"
                },
                {
                    "url": "https://www.patreon.com/efreelancer",
                    "type": "patreon"
                }
            ],
            "time": "2021-01-30T14:29:35+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "1cb1cde8e8dd0f70cc0fe51354a59acad9302084"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/1cb1cde8e8dd0f70cc0fe51354a59acad9302084",
                "reference": "1cb1cde8e8dd0f70cc0fe51354a59acad9302084",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2",
                "psr/log": "^1.0.1"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "elasticsearch/elasticsearch": "^7",
                "graylog2/gelf-php": "^1.4.2",
                "mongodb/mongodb": "^1.8",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpspec/prophecy": "^1.6.1",
                "phpstan/phpstan": "^0.12.59",
                "phpunit/phpunit": "^8.5",
                "predis/predis": "^1.1",
                "rollbar/rollbar": "^1.3",
                "ruflin/elastica": ">=0.90 <7.0.1",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "elasticsearch/elasticsearch": "Allow sending log messages to an Elasticsearch server via official client",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mbstring": "Allow to work properly with unicode symbols",
                "ext-mongodb": "Allow sending log messages to a MongoDB server (via driver)",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server (via library)",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Monolog\\": "src/Monolog"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "https://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "https://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "support": {
                "issues": "https://github.com/Seldaek/monolog/issues",
                "source": "https://github.com/Seldaek/monolog/tree/2.2.0"
            },
            "funding": [
                {
                    "url": "https://github.com/Seldaek",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/monolog/monolog",
                    "type": "tidelift"
                }
            ],
            "time": "2020-12-14T13:15:25+00:00"
        },
        {
            "name": "myclabs/php-enum",
            "version": "1.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/php-enum.git",
                "reference": "46cf3d8498b095bd33727b13fd5707263af99421"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/php-enum/zipball/46cf3d8498b095bd33727b13fd5707263af99421",
                "reference": "46cf3d8498b095bd33727b13fd5707263af99421",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.3 || ^8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.5",
                "squizlabs/php_codesniffer": "1.*",
                "vimeo/psalm": "^4.5.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "MyCLabs\\Enum\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP Enum contributors",
                    "homepage": "https://github.com/myclabs/php-enum/graphs/contributors"
                }
            ],
            "description": "PHP Enum implementation",
            "homepage": "http://github.com/myclabs/php-enum",
            "keywords": [
                "enum"
            ],
            "support": {
                "issues": "https://github.com/myclabs/php-enum/issues",
                "source": "https://github.com/myclabs/php-enum/tree/1.8.0"
            },
            "funding": [
                {
                    "url": "https://github.com/mnapoli",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/php-enum",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-15T16:11:48+00:00"
        },
        {
            "name": "php-mqtt/client",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-mqtt/client.git",
                "reference": "85fe51d44a75a4e6a46c31137e94538c810515f1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-mqtt/client/zipball/85fe51d44a75a4e6a46c31137e94538c810515f1",
                "reference": "85fe51d44a75a4e6a46c31137e94538c810515f1",
                "shasum": ""
            },
            "require": {
                "myclabs/php-enum": "^1.7",
                "php": "^7.4|^8.0",
                "psr/log": "^1.1"
            },
            "require-dev": {
                "phpunit/php-invoker": "^3.0",
                "phpunit/phpunit": "^9.0",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "suggest": {
                "ext-redis": "Required for the RedisRepository"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "PhpMqtt\\Client\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marvin Mall",
                    "email": "marvin-mall@msn.com",
                    "role": "developer"
                }
            ],
            "description": "An MQTT client written in and for PHP.",
            "keywords": [
                "client",
                "mqtt",
                "publish",
                "subscribe"
            ],
            "support": {
                "issues": "https://github.com/php-mqtt/client/issues",
                "source": "https://github.com/php-mqtt/client/tree/v1.1.0"
            },
            "time": "2021-03-21T19:23:51+00:00"
        },
        {
            "name": "phpseclib/phpseclib",
            "version": "2.0.31",
            "source": {
                "type": "git",
                "url": "https://github.com/phpseclib/phpseclib.git",
                "reference": "233a920cb38636a43b18d428f9a8db1f0a1a08f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpseclib/phpseclib/zipball/233a920cb38636a43b18d428f9a8db1f0a1a08f4",
                "reference": "233a920cb38636a43b18d428f9a8db1f0a1a08f4",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phing/phing": "~2.7",
                "phpunit/phpunit": "^4.8.35|^5.7|^6.0|^9.4",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "suggest": {
                "ext-gmp": "Install the GMP (GNU Multiple Precision) extension in order to speed up arbitrary precision integer arithmetic operations.",
                "ext-libsodium": "SSH2/SFTP can make use of some algorithms provided by the libsodium-php extension.",
                "ext-mcrypt": "Install the Mcrypt extension in order to speed up a few other cryptographic operations.",
                "ext-openssl": "Install the OpenSSL extension in order to speed up a wide variety of cryptographic operations."
            },
            "type": "library",
            "autoload": {
                "files": [
                    "phpseclib/bootstrap.php"
                ],
                "psr-4": {
                    "phpseclib\\": "phpseclib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jim Wigginton",
                    "email": "terrafrost@php.net",
                    "role": "Lead Developer"
                },
                {
                    "name": "Patrick Monnerat",
                    "email": "pm@datasphere.ch",
                    "role": "Developer"
                },
                {
                    "name": "Andreas Fischer",
                    "email": "bantu@phpbb.com",
                    "role": "Developer"
                },
                {
                    "name": "Hans-Jürgen Petrich",
                    "email": "petrich@tronic-media.com",
                    "role": "Developer"
                },
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com",
                    "role": "Developer"
                }
            ],
            "description": "PHP Secure Communications Library - Pure-PHP implementations of RSA, AES, SSH2, SFTP, X.509 etc.",
            "homepage": "http://phpseclib.sourceforge.net",
            "keywords": [
                "BigInteger",
                "aes",
                "asn.1",
                "asn1",
                "blowfish",
                "crypto",
                "cryptography",
                "encryption",
                "rsa",
                "security",
                "sftp",
                "signature",
                "signing",
                "ssh",
                "twofish",
                "x.509",
                "x509"
            ],
            "support": {
                "issues": "https://github.com/phpseclib/phpseclib/issues",
                "source": "https://github.com/phpseclib/phpseclib/tree/2.0.31"
            },
            "funding": [
                {
                    "url": "https://github.com/terrafrost",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/phpseclib",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpseclib/phpseclib",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-06T13:56:45+00:00"
        },
        {
            "name": "psr/cache",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/cache.git",
                "reference": "213f9dbc5b9bfbc4f8db86d2838dc968752ce13b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/cache/zipball/213f9dbc5b9bfbc4f8db86d2838dc968752ce13b",
                "reference": "213f9dbc5b9bfbc4f8db86d2838dc968752ce13b",
                "shasum": ""
            },
            "require": {
                "php": ">=8.0.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Cache\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for caching libraries",
            "keywords": [
                "cache",
                "psr",
                "psr-6"
            ],
            "support": {
                "source": "https://github.com/php-fig/cache/tree/2.0.0"
            },
            "time": "2021-02-03T23:23:37+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/8622567409010282b7aeebe4bb841fe98b58dcaf",
                "reference": "8622567409010282b7aeebe4bb841fe98b58dcaf",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/1.1.1"
            },
            "time": "2021-03-05T17:36:06+00:00"
        },
        {
            "name": "psr/event-dispatcher",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/event-dispatcher.git",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/event-dispatcher/zipball/dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\EventDispatcher\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Standard interfaces for event handling.",
            "keywords": [
                "events",
                "psr",
                "psr-14"
            ],
            "support": {
                "issues": "https://github.com/php-fig/event-dispatcher/issues",
                "source": "https://github.com/php-fig/event-dispatcher/tree/1.0.0"
            },
            "time": "2019-01-08T18:20:26+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "0f73288fd15629204f9d42b7055f72dacbe811fc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/0f73288fd15629204f9d42b7055f72dacbe811fc",
                "reference": "0f73288fd15629204f9d42b7055f72dacbe811fc",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "Psr/Log/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "support": {
                "source": "https://github.com/php-fig/log/tree/1.1.3"
            },
            "time": "2020-03-23T09:12:05+00:00"
        },
        {
            "name": "symfony/cache",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache.git",
                "reference": "093d69bb10c959553c8beb828b8d4ea250a247dd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache/zipball/093d69bb10c959553c8beb828b8d4ea250a247dd",
                "reference": "093d69bb10c959553c8beb828b8d4ea250a247dd",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/cache": "^1.0|^2.0",
                "psr/log": "^1.1",
                "symfony/cache-contracts": "^1.1.7|^2",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "conflict": {
                "doctrine/dbal": "<2.10",
                "symfony/dependency-injection": "<4.4",
                "symfony/http-kernel": "<4.4",
                "symfony/var-dumper": "<4.4"
            },
            "provide": {
                "psr/cache-implementation": "1.0|2.0",
                "psr/simple-cache-implementation": "1.0",
                "symfony/cache-implementation": "1.0|2.0"
            },
            "require-dev": {
                "cache/integration-tests": "dev-master",
                "doctrine/cache": "^1.6",
                "doctrine/dbal": "^2.10|^3.0",
                "predis/predis": "^1.1",
                "psr/simple-cache": "^1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Cache\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides an extended PSR-6, PSR-16 (and tags) implementation",
            "homepage": "https://symfony.com",
            "keywords": [
                "caching",
                "psr6"
            ],
            "support": {
                "source": "https://github.com/symfony/cache/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-16T09:10:13+00:00"
        },
        {
            "name": "symfony/cache-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache-contracts.git",
                "reference": "c0446463729b89dd4fa62e9aeecc80287323615d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache-contracts/zipball/c0446463729b89dd4fa62e9aeecc80287323615d",
                "reference": "c0446463729b89dd4fa62e9aeecc80287323615d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/cache": "^1.0|^2.0|^3.0"
            },
            "suggest": {
                "symfony/cache-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Cache\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to caching",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/cache-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/config",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/config.git",
                "reference": "212d54675bf203ff8aef7d8cee8eecfb72f4a263"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/config/zipball/212d54675bf203ff8aef7d8cee8eecfb72f4a263",
                "reference": "212d54675bf203ff8aef7d8cee8eecfb72f4a263",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/finder": "<4.4"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/yaml": "To use the yaml reference dumper"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Config\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Helps you find, load, combine, autofill and validate configuration values of any kind",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/config/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-23T23:58:19+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "35f039df40a3b335ebf310f244cb242b3a83ac8d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/35f039df40a3b335ebf310f244cb242b3a83ac8d",
                "reference": "35f039df40a3b335ebf310f244cb242b3a83ac8d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/string": "^5.1"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4",
                "symfony/dotenv": "<5.1",
                "symfony/event-dispatcher": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/process": "<4.4"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Eases the creation of beautiful and testable command line interfaces",
            "homepage": "https://symfony.com",
            "keywords": [
                "cli",
                "command line",
                "console",
                "terminal"
            ],
            "support": {
                "source": "https://github.com/symfony/console/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-28T09:42:18+00:00"
        },
        {
            "name": "symfony/dependency-injection",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dependency-injection.git",
                "reference": "1e66194bed2a69fa395d26bf1067e5e34483afac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dependency-injection/zipball/1e66194bed2a69fa395d26bf1067e5e34483afac",
                "reference": "1e66194bed2a69fa395d26bf1067e5e34483afac",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.0",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1.6|^2"
            },
            "conflict": {
                "symfony/config": "<5.1",
                "symfony/finder": "<4.4",
                "symfony/proxy-manager-bridge": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "provide": {
                "psr/container-implementation": "1.0",
                "symfony/service-implementation": "1.0|2.0"
            },
            "require-dev": {
                "symfony/config": "^5.1",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "",
                "symfony/expression-language": "For using expressions in service container configuration",
                "symfony/finder": "For using double-star glob patterns or when GLOB_BRACE portability is required",
                "symfony/proxy-manager-bridge": "Generate service proxies to lazy load them",
                "symfony/yaml": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DependencyInjection\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Allows you to standardize and centralize the way objects are constructed in your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dependency-injection/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-22T11:10:24+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "reference": "5f38c8804a9e97d23e0c8d63341088cd8a22d627",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/dotenv",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dotenv.git",
                "reference": "783f12027c6b40ab0e93d6136d9f642d1d67cd6b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dotenv/zipball/783f12027c6b40ab0e93d6136d9f642d1d67cd6b",
                "reference": "783f12027c6b40ab0e93d6136d9f642d1d67cd6b",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1"
            },
            "require-dev": {
                "symfony/process": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Dotenv\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Registers environment variables from a .env file",
            "homepage": "https://symfony.com",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "support": {
                "source": "https://github.com/symfony/dotenv/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:01:46+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "bdb7fb4188da7f4211e4b88350ba0dfdad002b03"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/bdb7fb4188da7f4211e4b88350ba0dfdad002b03",
                "reference": "bdb7fb4188da7f4211e4b88350ba0dfdad002b03",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "^1.0",
                "symfony/polyfill-php80": "^1.15",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.1",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\ErrorHandler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools to manage errors and ease debugging PHP code",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/error-handler/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-16T09:07:47+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "d08d6ec121a425897951900ab692b612a61d6240"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/d08d6ec121a425897951900ab692b612a61d6240",
                "reference": "d08d6ec121a425897951900ab692b612a61d6240",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/event-dispatcher-contracts": "^2",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "2.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/stopwatch": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\EventDispatcher\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools that allow your application components to communicate with each other by dispatching events and listening to them",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/event-dispatcher/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-18T17:12:37+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "reference": "69fee1ad2332a7cbab3aca13591953da9cdb7a11",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/event-dispatcher": "^1"
            },
            "suggest": {
                "symfony/event-dispatcher-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-23T23:28:01+00:00"
        },
        {
            "name": "symfony/filesystem",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/filesystem.git",
                "reference": "8c86a82f51658188119e62cff0a050a12d09836f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/filesystem/zipball/8c86a82f51658188119e62cff0a050a12d09836f",
                "reference": "8c86a82f51658188119e62cff0a050a12d09836f",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Filesystem\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides basic utilities for the filesystem",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/filesystem/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-28T14:30:26+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "0d639a0943822626290d169965804f79400e6a04"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/0d639a0943822626290d169965804f79400e6a04",
                "reference": "0d639a0943822626290d169965804f79400e6a04",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Finder\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Finds files and directories via an intuitive fluent interface",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/finder/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-15T18:55:04+00:00"
        },
        {
            "name": "symfony/flex",
            "version": "v1.12.2",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/flex.git",
                "reference": "e472606b4b3173564f0edbca8f5d32b52fc4f2c9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/flex/zipball/e472606b4b3173564f0edbca8f5d32b52fc4f2c9",
                "reference": "e472606b4b3173564f0edbca8f5d32b52fc4f2c9",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.0|^2.0",
                "php": ">=7.1"
            },
            "require-dev": {
                "composer/composer": "^1.0.2|^2.0",
                "symfony/dotenv": "^4.4|^5.0",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/phpunit-bridge": "^4.4|^5.0",
                "symfony/process": "^3.4|^4.4|^5.0"
            },
            "type": "composer-plugin",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.12-dev"
                },
                "class": "Symfony\\Flex\\Flex"
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Flex\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien.potencier@gmail.com"
                }
            ],
            "description": "Composer plugin for Symfony",
            "support": {
                "issues": "https://github.com/symfony/flex/issues",
                "source": "https://github.com/symfony/flex/tree/v1.12.2"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-16T14:05:05+00:00"
        },
        {
            "name": "symfony/framework-bundle",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/framework-bundle.git",
                "reference": "8889da18c6faa76c6149a90e6542be4afe723f2f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/framework-bundle/zipball/8889da18c6faa76c6149a90e6542be4afe723f2f",
                "reference": "8889da18c6faa76c6149a90e6542be4afe723f2f",
                "shasum": ""
            },
            "require": {
                "ext-xml": "*",
                "php": ">=7.2.5",
                "symfony/cache": "^5.2",
                "symfony/config": "^5.0",
                "symfony/dependency-injection": "^5.2",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/error-handler": "^4.4.1|^5.0.1",
                "symfony/event-dispatcher": "^5.1",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/http-foundation": "^5.2.1",
                "symfony/http-kernel": "^5.2.1",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.15",
                "symfony/routing": "^5.2"
            },
            "conflict": {
                "doctrine/persistence": "<1.3",
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "phpunit/phpunit": "<5.4.3",
                "symfony/asset": "<5.1",
                "symfony/browser-kit": "<4.4",
                "symfony/console": "<5.2.5",
                "symfony/dom-crawler": "<4.4",
                "symfony/dotenv": "<5.1",
                "symfony/form": "<5.2",
                "symfony/http-client": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/mailer": "<5.2",
                "symfony/messenger": "<4.4",
                "symfony/mime": "<4.4",
                "symfony/property-access": "<5.2",
                "symfony/property-info": "<4.4",
                "symfony/serializer": "<5.2",
                "symfony/stopwatch": "<4.4",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<4.4",
                "symfony/twig-bundle": "<4.4",
                "symfony/validator": "<5.2",
                "symfony/web-profiler-bundle": "<4.4",
                "symfony/workflow": "<5.2"
            },
            "require-dev": {
                "doctrine/annotations": "^1.10.4",
                "doctrine/cache": "~1.0",
                "doctrine/persistence": "^1.3|^2.0",
                "paragonie/sodium_compat": "^1.8",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/asset": "^5.1",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/console": "^5.2",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/dotenv": "^5.1",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/form": "^5.2",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/mailer": "^5.2",
                "symfony/messenger": "^5.2",
                "symfony/mime": "^4.4|^5.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/property-info": "^4.4|^5.0",
                "symfony/security-bundle": "^5.1",
                "symfony/security-core": "^4.4|^5.2",
                "symfony/security-csrf": "^4.4|^5.0",
                "symfony/security-http": "^4.4|^5.0",
                "symfony/serializer": "^5.2",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/string": "^5.0",
                "symfony/translation": "^5.0",
                "symfony/twig-bundle": "^4.4|^5.0",
                "symfony/validator": "^5.2",
                "symfony/web-link": "^4.4|^5.0",
                "symfony/workflow": "^5.2",
                "symfony/yaml": "^4.4|^5.0",
                "twig/twig": "^2.10|^3.0"
            },
            "suggest": {
                "ext-apcu": "For best performance of the system caches",
                "symfony/console": "For using the console commands",
                "symfony/form": "For using forms",
                "symfony/property-info": "For using the property_info service",
                "symfony/serializer": "For using the serializer service",
                "symfony/validator": "For using validation",
                "symfony/web-link": "For using web links, features such as preloading, prefetching or prerendering",
                "symfony/yaml": "For using the debug:config and lint:yaml commands"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\FrameworkBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides a tight integration between Symfony components and the Symfony full-stack framework",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/framework-bundle/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-22T14:43:01+00:00"
        },
        {
            "name": "symfony/http-client-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-client-contracts.git",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-client-contracts/zipball/7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "reference": "7e82f6084d7cae521a75ef2cb5c9457bbda785f4",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5"
            },
            "suggest": {
                "symfony/http-client-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\HttpClient\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to HTTP clients",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/http-client-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-11T23:07:08+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "54499baea7f7418bce7b5ec92770fd0799e8e9bf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/54499baea7f7418bce7b5ec92770fd0799e8e9bf",
                "reference": "54499baea7f7418bce7b5ec92770fd0799e8e9bf",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-mbstring": "~1.1",
                "symfony/polyfill-php80": "^1.15"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/mime": "To use the file extension guesser"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpFoundation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Defines an object-oriented layer for the HTTP specification",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-foundation/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-25T17:16:57+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "f34de4c61ca46df73857f7f36b9a3805bdd7e3b2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/f34de4c61ca46df73857f7f36b9a3805bdd7e3b2",
                "reference": "f34de4c61ca46df73857f7f36b9a3805bdd7e3b2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/log": "~1.0",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/event-dispatcher": "^5.0",
                "symfony/http-client-contracts": "^1.1|^2",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-php73": "^1.9",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/browser-kit": "<4.4",
                "symfony/cache": "<5.0",
                "symfony/config": "<5.0",
                "symfony/console": "<4.4",
                "symfony/dependency-injection": "<5.1.8",
                "symfony/doctrine-bridge": "<5.0",
                "symfony/form": "<5.0",
                "symfony/http-client": "<5.0",
                "symfony/mailer": "<5.0",
                "symfony/messenger": "<5.0",
                "symfony/translation": "<5.0",
                "symfony/twig-bridge": "<5.0",
                "symfony/validator": "<5.0",
                "twig/twig": "<2.13"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/browser-kit": "^4.4|^5.0",
                "symfony/config": "^5.0",
                "symfony/console": "^4.4|^5.0",
                "symfony/css-selector": "^4.4|^5.0",
                "symfony/dependency-injection": "^5.1.8",
                "symfony/dom-crawler": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/routing": "^4.4|^5.0",
                "symfony/stopwatch": "^4.4|^5.0",
                "symfony/translation": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "twig/twig": "^2.13|^3.0.4"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpKernel\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides a structured process for converting a Request into a Response",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-kernel/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-29T05:16:58+00:00"
        },
        {
            "name": "symfony/monolog-bridge",
            "version": "v5.2.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bridge.git",
                "reference": "8a330ab86c4bdf3983b26abf64bf85574edf0d52"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bridge/zipball/8a330ab86c4bdf3983b26abf64bf85574edf0d52",
                "reference": "8a330ab86c4bdf3983b26abf64bf85574edf0d52",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "^1.25.1|^2",
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/http-kernel": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2"
            },
            "conflict": {
                "symfony/console": "<4.4",
                "symfony/http-foundation": "<4.4"
            },
            "require-dev": {
                "symfony/console": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/mailer": "^4.4|^5.0",
                "symfony/mime": "^4.4|^5.0",
                "symfony/security-core": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/console": "For the possibility to show log messages in console commands depending on verbosity settings.",
                "symfony/http-kernel": "For using the debugging handlers together with the response life cycle of the HTTP kernel.",
                "symfony/var-dumper": "For using the debugging handlers like the console handler or the log server handler."
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Monolog\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides integration for Monolog with various Symfony components",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/monolog-bridge/tree/v5.2.5"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-06T07:59:01+00:00"
        },
        {
            "name": "symfony/monolog-bundle",
            "version": "v3.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bundle.git",
                "reference": "4054b2e940a25195ae15f0a49ab0c51718922eb4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bundle/zipball/4054b2e940a25195ae15f0a49ab0c51718922eb4",
                "reference": "4054b2e940a25195ae15f0a49ab0c51718922eb4",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "~1.22 || ~2.0",
                "php": ">=7.1.3",
                "symfony/config": "~4.4 || ^5.0",
                "symfony/dependency-injection": "^4.4 || ^5.0",
                "symfony/http-kernel": "~4.4 || ^5.0",
                "symfony/monolog-bridge": "~4.4 || ^5.0"
            },
            "require-dev": {
                "symfony/console": "~4.4 || ^5.0",
                "symfony/phpunit-bridge": "^5.1",
                "symfony/yaml": "~4.4 || ^5.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\MonologBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony MonologBundle",
            "homepage": "https://symfony.com",
            "keywords": [
                "log",
                "logging"
            ],
            "support": {
                "issues": "https://github.com/symfony/monolog-bundle/issues",
                "source": "https://github.com/symfony/monolog-bundle/tree/v3.7.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-31T07:20:47+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "5601e09b69f26c1828b13b6bb87cb07cddba3170"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/5601e09b69f26c1828b13b6bb87cb07cddba3170",
                "reference": "5601e09b69f26c1828b13b6bb87cb07cddba3170",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Grapheme\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's grapheme_* functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "grapheme",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.22.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-22T09:19:47+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "43a0283138253ed1d48d352ab6d0bdb3f809f248"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/43a0283138253ed1d48d352ab6d0bdb3f809f248",
                "reference": "43a0283138253ed1d48d352ab6d0bdb3f809f248",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.22.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-22T09:19:47+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "5232de97ee3b75b0360528dae24e73db49566ab1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/5232de97ee3b75b0360528dae24e73db49566ab1",
                "reference": "5232de97ee3b75b0360528dae24e73db49566ab1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.22.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-22T09:19:47+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "v1.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php73/tree/v1.22.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.22.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "31fba555f178afd04d54fd26953501b2c3f0c6e6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/31fba555f178afd04d54fd26953501b2c3f0c6e6",
                "reference": "31fba555f178afd04d54fd26953501b2c3f0c6e6",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/config": "<5.0",
                "symfony/dependency-injection": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "^1.10.4",
                "psr/log": "~1.0",
                "symfony/config": "^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "doctrine/annotations": "For using the annotation loader",
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Routing\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Maps an HTTP request to a set of configuration variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "support": {
                "source": "https://github.com/symfony/routing/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-14T13:53:33+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v2.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "reference": "f040a30e04b57fbcc9c6cbcf4dbaa96bd318b9bb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.1"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.4-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/v2.4.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-04-01T10:43:52+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "ad0bd91bce2054103f5eaa18ebeba8d3bc2a0572"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/ad0bd91bce2054103f5eaa18ebeba8d3bc2a0572",
                "reference": "ad0bd91bce2054103f5eaa18ebeba8d3bc2a0572",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.0",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "~1.15"
            },
            "require-dev": {
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\String\\": ""
                },
                "files": [
                    "Resources/functions.php"
                ],
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides an object-oriented API to strings and deals with bytes, UTF-8 code points and grapheme clusters in a unified way",
            "homepage": "https://symfony.com",
            "keywords": [
                "grapheme",
                "i18n",
                "string",
                "unicode",
                "utf-8",
                "utf8"
            ],
            "support": {
                "source": "https://github.com/symfony/string/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-17T17:12:15+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v5.2.6",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "89412a68ea2e675b4e44f260a5666729f77f668e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/89412a68ea2e675b4e44f260a5666729f77f668e",
                "reference": "89412a68ea2e675b4e44f260a5666729f77f668e",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "twig/twig": "^2.13|^3.0.4"
            },
            "suggest": {
                "ext-iconv": "To convert non-UTF-8 strings to UTF-8 (or symfony/polyfill-iconv in case ext-iconv cannot be used).",
                "ext-intl": "To show region name in time zone dump",
                "symfony/console": "To use the ServerDumpCommand and/or the bin/var-dump-server script"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides mechanisms for walking through any arbitrary PHP variable",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/v5.2.6"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-28T09:42:18+00:00"
        },
        {
            "name": "symfony/var-exporter",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-exporter.git",
                "reference": "5aed4875ab514c8cb9b6ff4772baa25fa4c10307"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-exporter/zipball/5aed4875ab514c8cb9b6ff4772baa25fa4c10307",
                "reference": "5aed4875ab514c8cb9b6ff4772baa25fa4c10307",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-php80": "^1.15"
            },
            "require-dev": {
                "symfony/var-dumper": "^4.4.9|^5.0.9"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\VarExporter\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Allows exporting any serializable PHP data structure to plain PHP code",
            "homepage": "https://symfony.com",
            "keywords": [
                "clone",
                "construct",
                "export",
                "hydrate",
                "instantiate",
                "serialize"
            ],
            "support": {
                "source": "https://github.com/symfony/var-exporter/tree/v5.2.4"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:01:46+00:00"
        },
        {
            "name": "symfony/yaml",
            "version": "v5.2.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/yaml.git",
                "reference": "298a08ddda623485208506fcee08817807a251dd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/yaml/zipball/298a08ddda623485208506fcee08817807a251dd",
                "reference": "298a08ddda623485208506fcee08817807a251dd",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "symfony/console": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/console": "For validating YAML files using the lint command"
            },
            "bin": [
                "Resources/bin/yaml-lint"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Yaml\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Loads and dumps YAML files",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/yaml/tree/v5.2.5"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-03-06T07:59:01+00:00"
        }
    ],
    "packages-dev": [],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": [],
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": ">=8.0",
        "ext-ctype": "*",
        "ext-iconv": "*"
    },
    "platform-dev": [],
    "plugin-api-version": "2.0.0"
}


File: /config\bundles.php
<?php

return [
    Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
    Symfony\Bundle\MonologBundle\MonologBundle::class => ['all' => true],
];


File: /config\packages\cache.yaml
framework:
  cache:
    # Unique name of your app: used to compute stable namespaces for cache keys.
    #prefix_seed: your_vendor_name/app_name

    # The "app" cache stores to the filesystem by default.
    # The data in this cache should persist between deploys.
    # Other options include:

    # Redis
    #app: cache.adapter.redis
    #default_redis_provider: redis://localhost

    # APCu (not recommended with heavy random-write workloads as memory fragmentation can cause perf issues)
    #app: cache.adapter.apcu

    # Namespaced pools use the above "app" backend by default
    #pools:
      #my.dedicated.cache: null


File: /config\packages\dev\monolog.yaml
monolog:
  handlers:
    main:
      type: stream
      path: "%kernel.logs_dir%/%kernel.environment%.log"
      level: debug
      channels: [ "!event" ]
    # uncomment to get logging in your browser
    # you may have to allow bigger header sizes in your Web server configuration
    #firephp:
    #  type: firephp
    #  level: info
    #chromephp:
    #  type: chromephp
    #  level: info
    console:
      type: console
      process_psr_3_messages: false
      channels: [ "!event", "!doctrine", "!console" ]


File: /config\packages\framework.yaml
# see https://symfony.com/doc/current/reference/configuration/framework.html
framework:
  secret: '%env(APP_SECRET)%'
  #csrf_protection: true
  #http_method_override: true

  # Enables session support. Note that the session will ONLY be started if you read or write from it.
  # Remove or comment this section to explicitly disable session support.
  session:
    handler_id: null
    cookie_secure: auto
    cookie_samesite: lax

  #esi: true
  #fragments: true
  php_errors:
    log: true


File: /config\packages\prod\deprecations.yaml
# As of Symfony 5.1, deprecations are logged in the dedicated "deprecation" channel when it exists
#monolog:
#  channels: [deprecation]
#  handlers:
#    deprecation:
#      type: stream
#      channels: [deprecation]
#      path: php://stderr


File: /config\packages\prod\monolog.yaml
monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            buffer_size: 50 # How many messages should be saved? Prevent memory leaks
        nested:
            type: stream
            path: php://stderr
            level: debug
            formatter: monolog.formatter.json
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine"]


File: /config\packages\prod\routing.yaml
framework:
  router:
    strict_requirements: null


File: /config\packages\routing.yaml
framework:
  router:
    utf8: true

    # Configure how to generate URLs in non-HTTP contexts, such as CLI commands.
    # See https://symfony.com/doc/current/routing.html#generating-urls-in-commands
    #default_uri: http://localhost


File: /config\packages\test\framework.yaml
framework:
  test: true
  session:
    storage_id: session.storage.mock_file


File: /config\packages\test\monolog.yaml
monolog:
  handlers:
    main:
      type: fingers_crossed
      action_level: error
      handler: nested
      excluded_http_codes: [ 404, 405 ]
      channels: [ "!event" ]
    nested:
      type: stream
      path: "%kernel.logs_dir%/%kernel.environment%.log"
      level: debug


File: /config\preload.php
<?php

if (file_exists(dirname(__DIR__).'/var/cache/prod/App_KernelProdContainer.preload.php')) {
    require dirname(__DIR__).'/var/cache/prod/App_KernelProdContainer.preload.php';
}


File: /config\services.yaml
# Put parameters here that don't need to change on each machine where the app is deployed
# https://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:
  app.update_time: '%env(int:UPDATE_TIME)%'

  mikrotik.host: '%env(string:MIKROTIK_HOST)%'
  mikrotik.use_ssl: '%env(bool:MIKROTIK_USE_SSL)%'
  mikrotik.user: '%env(string:MIKROTIK_USER)%'
  mikrotik.password: '%env(string:MIKROTIK_PASSWORD)%'

  mqtt.host: '%env(string:MQTT_HOST)%'
  mqtt.port: '%env(int:MQTT_PORT)%'
  mqtt.use_tls: '%env(bool:MQTT_USE_TLS)%'
  mqtt.username: '%env(string:MQTT_USERNAME)%'
  mqtt.password: '%env(string:MQTT_PASSWORD)%'
  mqtt.client_id: '%env(string:MQTT_CLIENT_ID)%'
  mqtt.topic_base: '%env(string:MQTT_TOPIC_BASE)%'

services:
  _defaults:
    autowire: true
    autoconfigure: true
    bind:
      App\Domain\Model\Mikrotik\MikrotikRepository $readRepository: '@App\Infrastructure\Domain\Model\Mikrotik\RouterOsMikrotikRepository'
      App\Domain\Model\Mikrotik\MikrotikRepository $writeRepository: '@App\Infrastructure\Domain\Model\Mikrotik\MqttMikrotikRepository'
      string $mqttTopicBase: '%mqtt.topic_base%'
      int $updateTime: '%app.update_time%'

  App\Application\:
    resource: '../src/Application/'

  App\Entrypoint\Console\Command\:
    resource: '../src/Entrypoint/Console/Command/'

  App\Infrastructure\Service\RouterOsClientFactory:
    class: 'App\Infrastructure\Service\RouterOsClientFactory'
    arguments:
      $host: '%mikrotik.host%'
      $useSsl: '%mikrotik.use_ssl%'
      $user: '%mikrotik.user%'
      $password: '%mikrotik.password%'

  App\Infrastructure\Service\MqttClientFactory:
    class: 'App\Infrastructure\Service\MqttClientFactory'
    arguments:
      $host: '%mqtt.host%'
      $port: '%mqtt.port%'
      $clientId: '%mqtt.client_id%'
      $username: '%mqtt.username%'
      $password: '%mqtt.password%'
      $useTls: '%mqtt.use_tls%'

  App\Infrastructure\Service\RouterOsClient:
    class: 'App\Infrastructure\Service\RouterOsClient'

  App\Infrastructure\Domain\Model\Mikrotik\RouterOsMikrotikRepository:
    class: 'App\Infrastructure\Domain\Model\Mikrotik\RouterOsMikrotikRepository'

  App\Infrastructure\Domain\Model\Mikrotik\MqttMikrotikRepository:
    class: 'App\Infrastructure\Domain\Model\Mikrotik\MqttMikrotikRepository'


File: /docker-compose.yml
version: '3.8'

services:
  php:
    build:
      context: .
      target: build
    volumes:
      - .:/var/www/html
      - ~/.composer:/.composer


File: /docker-image-generator.sh
#!/usr/bin/env bash

docker build \
  --target "production" \
  --tag "zoilomora/mikrotik2mqtt" \
  --tag "zoilomora/mikrotik2mqtt:$1" \
  .

docker push "zoilomora/mikrotik2mqtt"
docker push "zoilomora/mikrotik2mqtt:$1"


File: /Dockerfile
FROM php:8.0-cli-alpine AS build
RUN apk update && \
    apk add --no-cache \
        libzip-dev \
        openssl-dev && \
    docker-php-ext-install -j$(nproc) \
        zip \
        sockets && \
    adduser -D -g '' mikrotik2mqtt
ENV PATH /var/www/html/bin:/var/www/html/vendor/bin:$PATH
WORKDIR /var/www/html
USER mikrotik2mqtt

FROM build AS compilation
USER root
ENV APP_ENV prod
COPY . .
RUN composer install --no-dev -o && \
    rm .dockerignore && \
    chown -R mikrotik2mqtt:mikrotik2mqtt .

FROM build AS production
ENV APP_ENV prod
COPY --from=compilation /var/www/html .
USER mikrotik2mqtt
CMD sh -c "console app:run"


File: /LICENSE
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
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


File: /Makefile
UID=$(shell id -u)
GID=$(shell id -g)
DOCKER_PHP_SERVICE=php

start: erase cache-folders build composer-install bash

erase:
	docker-compose down -v
build:
	docker-compose build && docker-compose pull
cache-folders:
	mkdir -p ~/.composer && chown ${UID}:${GID} ~/.composer
composer-install:
	docker-compose run --rm -u ${UID}:${GID} ${DOCKER_PHP_SERVICE} composer install
bash:
	docker-compose run --rm -u ${UID}:${GID} ${DOCKER_PHP_SERVICE} sh
logs:
	docker-compose logs -f ${DOCKER_PHP_SERVICE}


File: /README.md
# MikroTik (RouterOS) to MQTT
![Docker Image Size](https://img.shields.io/docker/image-size/zoilomora/mikrotik2mqtt/latest?label=Docker%20Image%20Size&style=flat-square)
![GitHub Last Release](https://img.shields.io/github/v/release/zoilomora/mikrotik2mqtt?style=flat-square)
![GitHub License](https://img.shields.io/github/license/zoilomora/mikrotik2mqtt?style=flat-square)

## TL;DR
Sends structured information from a [MikroTik] router to an [MQTT] Server.

## Usage
Here are some example snippets to help you get started creating a container.

### docker-compose ([recommended](https://docs.docker.com/compose/))
Compatible with docker-compose v2 schemas.

```yaml
version: "2.1"
services:
  mikrotik2mqtt:
    image: zoilomora/mikrotik2mqtt
    container_name: mikrotik2mqtt
    environment:
      - MIKROTIK_HOST=192.168.88.1
      - MIKROTIK_USER=mikrotik2mqtt
      - MIKROTIK_PASSWORD=mikrotik2mqtt
      - MQTT_HOST=192.168.88.2
    restart: unless-stopped
```

### docker cli

```bash
docker run -d \
  --name=mikrotik2mqtt \
  -e MIKROTIK_HOST=192.168.88.1 \
  -e MIKROTIK_USER=mikrotik2mqtt \
  -e MIKROTIK_PASSWORD=mikrotik2mqtt \
  -e MQTT_HOST=192.168.88.2 \
  --restart unless-stopped \
  zoilomora/mikrotik2mqtt
```

## Parameters
Container images are configured using parameters passed at runtime (such as those above).

| Parameter                            | Function                                                       |
| :----------------------------------: | -------------------------------------------------------------- |
| `-e UPDATE_TIME=60`                  | Time interval (seconds) between data collection                |
| `-e MIKROTIK_HOST=192.168.88.1`      | IP Address of your MikroTik router                             |
| `-e MIKROTIK_USE_SSL=0`              | Enable (1) or disable (0) the use of SSL from the MikroTik API |
| `-e MIKROTIK_USER=mikrotik2mqtt`     | User with read permission of his MikroTik                      |
| `-e MIKROTIK_PASSWORD=mikrotik2mqtt` | Password of your user with read permissions of your MikroTik   |
| `-e MQTT_HOST=192.168.88.2`          | IP Address of your MQTT Server                                 |
| `-e MQTT_PORT=1883`                  | Port of your MQTT server                                       |
| `-e MQTT_USE_TLS=0`                  | Enable (1) or disable (0) the use of TLS on your MQTT Server   |
| `-e MQTT_USERNAME=mikrotik2mqtt`     | User of your MQTT Server                                       |
| `-e MQTT_PASSWORD=mikrotik2mqtt`     | Password of your MQTT Server                                   |
| `-e MQTT_CLIENT_ID=mikrotik2mqtt`    | Client identifier for your MQTT Server                         |
| `-e MQTT_TOPIC_BASE=mikrotik2mqtt`   | Base of the topic in which the information will be published   |

## Updating Info
Below are the instructions for updating containers:

### Via Docker Compose
- Update all images: `docker-compose pull`
    - or update a single image: `docker-compose pull mikrotik2mqtt`
- Let compose update all containers as necessary: `docker-compose up -d`
    - or update a single container: `docker-compose up -d mikrotik2mqtt`
- You can also remove the old dangling images: `docker image prune`

### Via Docker Run
- Update the image: `docker pull zoilomora/mikrotik2mqtt`
- Stop the running container: `docker stop mikrotik2mqtt`
- Delete the container: `docker rm mikrotik2mqtt`
- Recreate a new container with the same docker run parameters as instructed above
- You can also remove the old dangling images: `docker image prune`

## Building locally
If you want to make local modifications to these images for development purposes or just to customize the logic:

```bash
git clone https://github.com/zoilomora/mikrotik2mqtt.git
cd mikrotik2mqtt
docker build \
  --no-cache \
  --pull \
  --target production \
  --tag zoilomora/mikrotik2mqtt:latest .
```

## Dependencies
We must give thanks to these dependencies for which this project would not be in operation:
- [EvilFreelancer/routeros-api-php](https://github.com/EvilFreelancer/routeros-api-php)
- [php-mqtt/client](https://github.com/php-mqtt/client)

## License
Licensed under the [Apache-2.0]

Read [LICENSE] for more information

[Apache-2.0]: https://opensource.org/licenses/Apache-2.0
[LICENSE]: LICENSE
[MikroTik]: https://mikrotik.com/
[MQTT]: https://mqtt.org/


File: /src\Application\Mikrotik\Get\GetMikrotikCommand.php
<?php
declare(strict_types=1);

namespace App\Application\Mikrotik\Get;

final class GetMikrotikCommand
{
}



File: /src\Application\Mikrotik\Get\GetMikrotikCommandHandler.php
<?php
declare(strict_types=1);

namespace App\Application\Mikrotik\Get;

use App\Domain\Model\Mikrotik\MikrotikRepository;

final class GetMikrotikCommandHandler
{
    public function __construct(
        private MikrotikRepository $readRepository,
    )
    {}

    public function execute(GetMikrotikCommand $command): array
    {
        return $this->readRepository->get();
    }
}


File: /src\Application\Mikrotik\Save\SaveMikrotikCommand.php
<?php
declare(strict_types=1);

namespace App\Application\Mikrotik\Save;

final class SaveMikrotikCommand
{
    public function __construct(
        private array $data,
    )
    {}

    public function data(): array
    {
        return $this->data;
    }
}


File: /src\Application\Mikrotik\Save\SaveMikrotikCommandHandler.php
<?php
declare(strict_types=1);

namespace App\Application\Mikrotik\Save;

use App\Domain\Model\Mikrotik\MikrotikRepository;

final class SaveMikrotikCommandHandler
{
    public function __construct(
        private MikrotikRepository $writeRepository,
    )
    {}

    public function execute(SaveMikrotikCommand $command): void
    {
        $this->writeRepository->save(
            $command->data()
        );
    }
}


File: /src\Domain\Model\Mikrotik\MikrotikRepository.php
<?php
declare(strict_types=1);

namespace App\Domain\Model\Mikrotik;

interface MikrotikRepository
{
    public function get(): array;
    public function save(array $mikrotik): void;
}


File: /src\Entrypoint\Console\Command\RunCommand.php
<?php
declare(strict_types=1);

namespace App\Entrypoint\Console\Command;

use App\Application\Mikrotik\Get\GetMikrotikCommand;
use App\Application\Mikrotik\Get\GetMikrotikCommandHandler;
use App\Application\Mikrotik\Save\SaveMikrotikCommand;
use App\Application\Mikrotik\Save\SaveMikrotikCommandHandler;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

final class RunCommand extends Command
{
    protected static $defaultName = 'app:run';

    public function __construct(
        private int $updateTime,
        private GetMikrotikCommandHandler $getMikrotikCommandHandler,
        private SaveMikrotikCommandHandler $saveMikrotikCommandHandler,
    ) {
        parent::__construct();
    }

    protected function configure()
    {
        $this->setDescription('Run Application!');
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $output->writeln('MikroTik to MQTT initialized.' . PHP_EOL);

        while (true) {
            $output->writeln('Getting data from MikroTik API (RouterOS)...');
            $mikrotik = $this->getMikrotikCommandHandler->execute(
                new GetMikrotikCommand()
            );

            $output->writeln('Publishing the data to MQTT...');
            $this->saveMikrotikCommandHandler->execute(
                new SaveMikrotikCommand($mikrotik)
            );

            $output->writeln('Process completed successfully!' . PHP_EOL);
            $output->writeln(
                \sprintf(
                    'Waiting %d seconds for the next iteration...%s',
                    $this->updateTime,
                    PHP_EOL,
                ),
            );
            \sleep($this->updateTime);
        }
    }
}


File: /src\Infrastructure\Domain\Model\Mikrotik\MqttMikrotikRepository.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Domain\Model\Mikrotik;

use App\Domain\Model\Mikrotik\MikrotikRepository;
use App\Infrastructure\Service\MqttClientFactory;
use PhpMqtt\Client\MqttClient;

final class MqttMikrotikRepository implements MikrotikRepository
{
    private ?MqttClient $client = null;

    public function __construct(
        private MqttClientFactory $clientFactory,
        private string $mqttTopicBase,
    )
    {}

    public function get(): array
    {
        throw new \Exception('This method is not implemented.');
    }

    public function save(array $mikrotik): void
    {
        $this->buildClient();

        $this->client->connect();

        $this->client->publish(
            $this->topicGenerate($mikrotik),
            \json_encode($mikrotik),
            0
        );

        $this->client->disconnect();
    }

    private function buildClient(): void
    {
        if (null === $this->client) {
            $this->client = $this->clientFactory->build();
        }
    }

    private function topicGenerate(array $mikrotik): string
    {
        return $this->mqttTopicBase . '/' . $mikrotik['routerBoard']['serialNumber'];
    }
}


File: /src\Infrastructure\Domain\Model\Mikrotik\RouterOsMikrotikRepository.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Domain\Model\Mikrotik;

use App\Domain\Model\Mikrotik\MikrotikRepository;
use App\Infrastructure\Service\FormatMikrotikDuration;
use App\Infrastructure\Service\RouterOsClient;
use App\Infrastructure\Service\RouterOsClientFactory;
use JetBrains\PhpStorm\ArrayShape;

final class RouterOsMikrotikRepository implements MikrotikRepository
{
    private ?RouterOsClient $client = null;

    public function __construct(
        private RouterOsClientFactory $clientFactory,
    )
    {}

    #[ArrayShape(['identity' => "string", 'routerBoard' => "array", 'resources' => "array", 'health' => "array", 'interfaces' => "array", 'devices' => "array"])]
    public function get(): array
    {
        $this->buildClient();

        return [
            'identity' => $this->getIdentity(),
            'routerBoard' => $this->getRouterBoard(),
            'resources' => $this->getResources(),
            'health' => $this->getHealth(),
            'interfaces' => $this->getInterfaces(),
            'devices' => $this->getDevices(),
        ];
    }

    public function save(array $mikrotik): void
    {
        throw new \Exception('This method is not implemented.');
    }

    private function buildClient(): void
    {
        if (null === $this->client) {
            $this->client = $this->clientFactory->build();
        }
    }

    private function getIdentity(): string
    {
        return $this->client->getIdentity();
    }

    #[ArrayShape(['boardName' => "string", 'model' => "string", 'serialNumber' => "string", 'firmware' => "string[]"])]
    private function getRouterBoard(): array
    {
        $data = $this->client->getRouterBoard();

        return [
            'boardName' => (string) $data['board-name'],
            'model' => (string) $data['model'],
            'serialNumber' => (string) $data['serial-number'],
            'firmware' => [
                'factory' => (string) $data['factory-firmware'],
                'current' => (string) $data['current-firmware'],
                'upgrade' => (string) $data['upgrade-firmware'],
            ],
        ];
    }

    #[ArrayShape(["upTime" => "int", "architecture" => "string", "cpu" => "array", "memory" => "int[]", "hdd" => "int[]"])]
    private function getResources(): array
    {
        $data = $this->client->getResources();

        return [
            "upTime" => FormatMikrotikDuration::fromStringToInt($data['uptime']),
            "architecture" => \strtoupper($data['architecture-name']),
            "cpu" => [
                "model" => (string) $data['cpu'],
                "numCores" => (int) $data['cpu-count'],
                "frequencyMhz" => (int) $data['cpu-frequency'],
                "load" => (float) $data['cpu-load'],
            ],
            "memory" => [
                "free" => (int) $data['free-memory'],
                "total" => (int) $data['total-memory'],
            ],
            "hdd" => [
                "free" => (int) $data['free-hdd-space'],
                "total" => (int) $data['total-hdd-space'],
            ]
        ];
    }

    #[ArrayShape(['voltage' => "float", 'temperature' => "int"])]
    private function getHealth(): array
    {
        $data = $this->client->getHealth();

        return [
            'voltage' => floatval($data['voltage']),
            'temperature' => intval($data['temperature']),
        ];
    }

    private function getInterfaces(): array
    {
        $ipAddress = $this->client->getIpAddress();

        $ipAddressOrdered = [];
        foreach ($ipAddress as $ip) {
            if (false === \array_key_exists($ip['interface'], $ipAddressOrdered)) {
                $ipAddressOrdered[$ip['interface']] = [];
            }

            $address = \explode('/', $ip['address']);

            $ipAddressOrdered[$ip['interface']][] = $address[0];
        }

        $interfaces = $this->client->getInterfaces();

        $result = [];
        foreach ($interfaces as $interface) {
            $name = (string) $interface['name'];

            $address = \array_key_exists($name, $ipAddressOrdered)
                ? $ipAddressOrdered[$name]
                : [];

            $monitoring = $this->client->getMonitoring($name);

            $result[] = [
                'name' => $name,
                'comment' => \array_key_exists('comment', $interface)
                    ? \utf8_encode($interface['comment'])
                    : '',
                'type' => (string) $interface['type'],
                'lastLinkUpTime' => \array_key_exists('last-link-up-time', $interface)
                    ? $this->formatLastLinkUpTime($interface['last-link-up-time'])
                    : '',
                'address' => [
                    'mac' => (string) $interface['mac-address'],
                    'ip' => $address,
                ],
                'running' => 'true' === $interface['running'],
                'disabled' => 'true' === $interface['disabled'],
                'traffic' => [
                    'rxBitsPerSecond' => (int) $monitoring['rx-bits-per-second'],
                    "txBitsPerSecond" => (int) $monitoring['tx-bits-per-second'],
                ],
            ];
        }

        return $result;
    }

    private function formatLastLinkUpTime($lastLinkUpTime): string
    {
        $datetime = \DateTime::createFromFormat('M/d/Y H:i:s', $lastLinkUpTime);

        return $datetime->format('Y-m-d H:i:s');
    }

    private function getDevices(): array
    {
        $leases = $this->client->getDhcpLeases();

        $leasesOrdered = [];
        foreach ($leases as $lease) {
            $leasesOrdered[$lease['mac-address']] = [
                'comment' => \array_key_exists('comment', $lease)
                    ? \utf8_encode($lease['comment'])
                    : '',
            ];
        }

        $arps = $this->client->getArp();

        $result = [];
        foreach ($arps as $arp) {
            if (false === \array_key_exists('mac-address', $arp)) {
                continue;
            }

            $ipAddress = $arp['address'];
            $macAddress = $arp['mac-address'];

            $lease = \array_key_exists($macAddress, $leasesOrdered)
                ? $leasesOrdered[$macAddress]
                : ['comment' => ''];

            $result[] = [
                'comment' => (string) $lease['comment'],
                'address' => [
                    'ip' => (string) $ipAddress,
                    'mac' => (string) $macAddress,
                ],
            ];
        }

        return $result;
    }
}


File: /src\Infrastructure\Service\FormatMikrotikDuration.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Service;

final class FormatMikrotikDuration
{
    public static function fromStringToInt(string $duration): int
    {
        $text = \str_replace(
            ['s', 'm', 'h', 'd', 'w'],
            '|',
            $duration
        );

        $timeCode = \explode('|', $text);
        $timeCode = \array_reverse($timeCode);

        $timeCodeClear = [];
        foreach ($timeCode as $number) {
            if ('' === $number) {
                continue;
            }

            $timeCodeClear[] = $number;
        }

        $multiples = [
            0 => 1,                // Seconds
            1 => 60,               // Minutes
            2 => 60 * 60,          // Hours
            3 => 24 * 60 * 60,     // Days
            4 => 7 * 24 * 60 * 60, // Weeks
        ];

        $seconds = 0;
        foreach ($timeCodeClear as $key => $value) {
            $multiple = $multiples[$key];
            $seconds += $multiple * $value;
        }

        return $seconds;
    }
}


File: /src\Infrastructure\Service\MqttClient.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Service;

use PhpMqtt\Client\ConnectionSettings;

class MqttClient extends \PhpMqtt\Client\MqttClient
{
    private ConnectionSettings $settingsSaved;

    public function connect(ConnectionSettings $settings = null, bool $useCleanSession = false): void
    {
        if (null !== $settings) {
            $this->settingsSaved = $settings;
        }

        parent::connect($this->settingsSaved, $useCleanSession);
    }
}


File: /src\Infrastructure\Service\MqttClientFactory.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Service;

use PhpMqtt\Client\ConnectionSettings;

final class MqttClientFactory
{
    public function __construct(
        private string $host,
        private int $port,
        private string $clientId,
        private string $username,
        private string $password,
        private bool $useTls,
    )
    {}

    public function build(): MqttClient
    {
        $client = new MqttClient(
            $this->host,
            $this->port,
            $this->clientId,
        );

        $settings = new ConnectionSettings();
        $settings = $settings->setUseTls($this->useTls);

        if ('' !== $this->username && '' !== $this->password) {
            $settings = $settings
                ->setUsername($this->username)
                ->setPassword($this->password);
        }

        $client->connect($settings);
        $client->disconnect();

        return $client;
    }
}


File: /src\Infrastructure\Service\RouterOsClient.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Service;

use RouterOS\Client;
use RouterOS\Query;

final class RouterOsClient
{
    public function __construct(
        private Client $client,
    )
    {}

    public function getIdentity(): string
    {
        return $this->client->qr('/system/identity/print')[0]['name'];
    }

    public function getRouterBoard(): array
    {
        return $this->client->qr('/system/routerboard/print')[0];
    }

    public function getHealth(): array
    {
        return $this->client->qr('/system/health/print')[0];
    }

    public function getResources(): array
    {
        return $this->client->qr('/system/resource/print')[0];
    }

    public function getInterfaces(): array|string
    {
        return $this->client->qr('/interface/print');
    }

    public function getIpAddress(): array|string
    {
        return $this->client->qr('/ip/address/print');
    }

    public function getMonitoring(string $interfaceName): array|string
    {
        $query = new Query('/interface/monitor-traffic');
        $query
            ->equal('interface', $interfaceName)
            ->equal('once');

        return $this->client->qr($query)[0];
    }

    public function getArp(): array|string
    {
        return $this->client->qr('/ip/arp/print');
    }

    public function getDhcpLeases(): array|string
    {
        return $this->client->qr('/ip/dhcp-server/lease/print');
    }
}


File: /src\Infrastructure\Service\RouterOsClientFactory.php
<?php
declare(strict_types=1);

namespace App\Infrastructure\Service;

use RouterOS\Client;
use RouterOS\Config;

final class RouterOsClientFactory
{
    public function __construct(
        private string $host,
        private bool $useSsl,
        private string $user,
        private string $password,
    )
    {}

    public function build(): RouterOsClient
    {
        $config = new Config();
        $config
            ->set('host', $this->host)
            ->set('ssl', $this->useSsl)
            ->set('user', $this->user)
            ->set('pass', $this->password);

        return new RouterOsClient(
            new Client($config),
        );
    }
}


File: /src\Kernel.php
<?php

namespace App;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;
use Symfony\Component\HttpKernel\Kernel as BaseKernel;
use Symfony\Component\Routing\Loader\Configurator\RoutingConfigurator;

class Kernel extends BaseKernel
{
    use MicroKernelTrait;

    protected function configureContainer(ContainerConfigurator $container): void
    {
        $container->import('../config/{packages}/*.yaml');
        $container->import('../config/{packages}/'.$this->environment.'/*.yaml');

        if (is_file(\dirname(__DIR__).'/config/services.yaml')) {
            $container->import('../config/services.yaml');
            $container->import('../config/{services}_'.$this->environment.'.yaml');
        } elseif (is_file($path = \dirname(__DIR__).'/config/services.php')) {
            (require $path)($container->withPath($path), $this);
        }
    }

    protected function configureRoutes(RoutingConfigurator $routes): void
    {
        $routes->import('../config/{routes}/'.$this->environment.'/*.yaml');
        $routes->import('../config/{routes}/*.yaml');

        if (is_file(\dirname(__DIR__).'/config/routes.yaml')) {
            $routes->import('../config/routes.yaml');
        } elseif (is_file($path = \dirname(__DIR__).'/config/routes.php')) {
            (require $path)($routes->withPath($path), $this);
        }
    }
}


File: /symfony.lock
{
    "divineomega/php-ssh-connection": {
        "version": "v2.2.0"
    },
    "evilfreelancer/routeros-api-php": {
        "version": "1.4.0"
    },
    "monolog/monolog": {
        "version": "2.2.0"
    },
    "myclabs/php-enum": {
        "version": "1.8.0"
    },
    "php-mqtt/client": {
        "version": "v1.1.0"
    },
    "phpseclib/phpseclib": {
        "version": "2.0.31"
    },
    "psr/cache": {
        "version": "2.0.0"
    },
    "psr/container": {
        "version": "1.1.1"
    },
    "psr/event-dispatcher": {
        "version": "1.0.0"
    },
    "psr/log": {
        "version": "1.1.3"
    },
    "symfony/cache": {
        "version": "v5.2.6"
    },
    "symfony/cache-contracts": {
        "version": "v2.4.0"
    },
    "symfony/config": {
        "version": "v5.2.4"
    },
    "symfony/console": {
        "version": "5.1",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "5.1",
            "ref": "c6d02bdfba9da13c22157520e32a602dbee8a75c"
        },
        "files": [
            "bin/console"
        ]
    },
    "symfony/dependency-injection": {
        "version": "v5.2.6"
    },
    "symfony/deprecation-contracts": {
        "version": "v2.4.0"
    },
    "symfony/dotenv": {
        "version": "v5.2.4"
    },
    "symfony/error-handler": {
        "version": "v5.2.6"
    },
    "symfony/event-dispatcher": {
        "version": "v5.2.4"
    },
    "symfony/event-dispatcher-contracts": {
        "version": "v2.4.0"
    },
    "symfony/filesystem": {
        "version": "v5.2.6"
    },
    "symfony/finder": {
        "version": "v5.2.4"
    },
    "symfony/flex": {
        "version": "1.0",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "1.0",
            "ref": "c0eeb50665f0f77226616b6038a9b06c03752d8e"
        },
        "files": [
            ".env"
        ]
    },
    "symfony/framework-bundle": {
        "version": "5.2",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "5.2",
            "ref": "6ec87563dcc85cd0c48856dcfbfc29610506d250"
        },
        "files": [
            "config/packages/cache.yaml",
            "config/packages/framework.yaml",
            "config/packages/test/framework.yaml",
            "config/preload.php",
            "config/routes/dev/framework.yaml",
            "config/services.yaml",
            "public/index.php",
            "src/Controller/.gitignore",
            "src/Kernel.php"
        ]
    },
    "symfony/http-client-contracts": {
        "version": "v2.4.0"
    },
    "symfony/http-foundation": {
        "version": "v5.2.4"
    },
    "symfony/http-kernel": {
        "version": "v5.2.6"
    },
    "symfony/monolog-bridge": {
        "version": "v5.2.5"
    },
    "symfony/monolog-bundle": {
        "version": "3.7",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "3.7",
            "ref": "329f6a5ef2e7aa033f802be833ef8d1268dd0848"
        },
        "files": [
            "config/packages/dev/monolog.yaml",
            "config/packages/prod/deprecations.yaml",
            "config/packages/prod/monolog.yaml",
            "config/packages/test/monolog.yaml"
        ]
    },
    "symfony/polyfill-intl-grapheme": {
        "version": "v1.22.1"
    },
    "symfony/polyfill-intl-normalizer": {
        "version": "v1.22.1"
    },
    "symfony/polyfill-mbstring": {
        "version": "v1.22.1"
    },
    "symfony/polyfill-php73": {
        "version": "v1.22.1"
    },
    "symfony/polyfill-php80": {
        "version": "v1.22.1"
    },
    "symfony/routing": {
        "version": "5.1",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "master",
            "version": "5.1",
            "ref": "b4f3e7c95e38b606eef467e8a42a8408fc460c43"
        },
        "files": [
            "config/packages/prod/routing.yaml",
            "config/packages/routing.yaml",
            "config/routes.yaml"
        ]
    },
    "symfony/service-contracts": {
        "version": "v2.4.0"
    },
    "symfony/string": {
        "version": "v5.2.6"
    },
    "symfony/var-dumper": {
        "version": "v5.2.6"
    },
    "symfony/var-exporter": {
        "version": "v5.2.4"
    },
    "symfony/yaml": {
        "version": "v5.2.5"
    }
}


