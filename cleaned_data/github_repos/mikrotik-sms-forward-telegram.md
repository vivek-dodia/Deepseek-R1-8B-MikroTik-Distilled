# Repository Information
Name: mikrotik-sms-forward-telegram

# Directory Structure
Directory structure:
└── github_repos/mikrotik-sms-forward-telegram/
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
    │   │       ├── pack-fcde82c04a010d8085f88b740c9bcf0d9949b8ec.idx
    │   │       └── pack-fcde82c04a010d8085f88b740c9bcf0d9949b8ec.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── README.MD
    ├── tgbot-notify.rsc
    ├── tgbot-smsfwd.rsc
    └── tgbot-startup.rsc


# Content
File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/filimonic/mikrotik-sms-forward-telegram.git
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
0000000000000000000000000000000000000000 3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/filimonic/mikrotik-sms-forward-telegram.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/filimonic/mikrotik-sms-forward-telegram.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/filimonic/mikrotik-sms-forward-telegram.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e refs/remotes/origin/main
3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e refs/tags/21.06.11.12
3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e refs/tags/21.07.11.12


File: /.git\refs\heads\main
3dbee7618ba1f2cc17ac9d01c9af278dc2e4754e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /README.MD
## mikrotik-sms-forward-telegram

Set of scripts to forward SMS messages to Telegram for Mikrotik

Tested on Mikrotik LGH LTE6 Kit

### Features

* Works directly with modem
* Supports UCS2 (non-ASCII) messages

### Setup

* Create a telegram bot using @botfather
* Get chat id or group id using https://api.telegram.org/botXXX:YYYY/getUpdates 
* Fill in bot token and chat id in `tgbot-notify.rsc`
* Save all 3 scripts on your mikrotik device

### Create schedules

* `tgbot_notify_robot`   : `/system script run tgbot_notify.rsc`  at startup, interval `1m`
* `tgbot_smsfwd_robot`   : `/system script run tgbot-smsfwd.rsc`  at startup, interval `3m`
* `tgbot_notify_startup` : `/system script run tgbot-startup.rsc` at startup once

### Dusable SMS processing

* Disable SMS processing `/tool sms set receive-enabled=no auto-erase=no`

### Workflow

* Messages queued to send are stored in `TGBOTMQ` array of messages. Each message is array with mandatory `Message(str)` field and `Sent(str)` fields and any optional fields.
* `tgbot_notify_robot` task runs every minute. It looks for global `TGBOTMQ` array of messages for messages with `Sent = "no"`. It rties to send message, and if message is sent OK, message's `Sent` is set to `yes`
* `tgbot_smsfwd_robot` task runs every 3 minutes. It looks for SMS stored in SIM card, decodes them into text format and puts into `TGBOTMQ` array. Messages with `Sent` = `yes` are removed from both `TGBOTMQ` and SIM card.
* `tgbot_notify_startup` task runs at startup, waits for NTP time to be synced and sends message with boot event to `TGBOTMQ`


File: /tgbot-notify.rsc
# Alexey D. Filimonov
# MIT License
# Source code at https://github.com/filimonic/mikrotik-sms-forward-telegram
# Version 21.06.11.12

:global TGBOTMQ

# Fill with bot key
:local TGBOTTOKEN "0000000000:AAAAAAA_AAAAAAAAAA_AAAAAAAAAAAAAAAA"
# Fill with chat_id
:local TGBOTCHATID "-123456789"

:if ([:typeof $TGBOTMQ] = "nothing") do={
	:set TGBOTMQ [:toarray ""]
}

:local TGBOTURL ( "https://api.telegram.org/bot$TGBOTTOKEN/sendMessage")

:foreach idx,msg in=$TGBOTMQ do={
    :if ($msg->"Sent" = "no") do={
        :local result ""
        :local msgBody ("{\"chat_id\":\"" . $TGBOTCHATID . "\", \"text\":\"". $msg->"Message" ."\", \"disable_web_page_preview\":true, \"parse_mode\": \"MarkdownV2\"}")
        :do {:set result [/tool fetch output=user url="$TGBOTURL" http-method=post http-data=$msgBody http-header-field="content-type: application/json" as-value]} on-error={:put ("Error sending Telegram: " . [:tostr $result])}
        :if ( ($result->"status" = "finished") and ("." . [:find ($result->"data") "\"ok\":true"] . "." != "..") ) do={
            :put "MARK message $idx as Sent"
            :set ($TGBOTMQ->$idx->"Sent") "yes"
        }
    } else={
        :if ($msg->"Sent" != "yes") do={
            :put "Message TGBOTMQ[$idx] has wrong \"Sent\" value"
        }
    }
}


File: /tgbot-smsfwd.rsc
# Alexey D. Filimonov
# MIT License
# Source code at https://github.com/filimonic/mikrotik-sms-forward-telegram
# Version 21.06.11.12


:global TGBOTMQ
while ([:typeof $TGBOTMQ] = "nothing") do={
	:delay delay-time=2s
    :put "waiting TGBOTMQ ..."
}
# function hexToNum
# @param <hex> hex string
:local hexToNum do={
    :local result 0
    :local lastIdx ([:len $hex] - 1)
    :for idx from=$lastIdx to=0 step=-1 do={
        :local dec [:find "0123456789ABCDEFabcdef" [:pick $hex $idx]]
        :if ([:typeof $dec] = "nil") do={
            :set result -1
        }
        :if ($dec > 15) do={
            :set dec (dec - 6)
        }
        for pow from=$lastIdx to=($idx + 1) step=-1 do={
            :set dec (dec * 16)
        }
        :if ($result >= 0) do={
            :set result ($result + $dec)
        }
    }
    #:log info message=("hexToNum: [" . $hex . "] = [" . $result . "]")
    :return $result
}

# sms7toJSONStr converts hex string taken from TP-UD PDU SMS to JSON \uXXXX notation
#     @param <hexstr> - hex string from TP-UD part of PDU message in upper case
#     @returns hex string of 8-bit ascii characters
#     @example [$sms7toJSONStr hexstr="C8329BFD06"] => "48656C6C6F" ("Hello")
:local sms7toJSONStr do={
    # Alexey D. Filimonov <alexey@filimonic.net>
    # @param <hexstr> - hex string from TP-UD
    # 2021-06-27
    # @ref "GSM 03.38"

    #:put "sms7toJSONStr called"

    :local asciiChars ( \
        "\\u0000",  "\\u0001",  "\\u0002",  "\\u0003",  "\\u0004",  "\\u0005",  "\\u0006",  "\\u0007", \
            "\\b",      "\\t",      "\\n",  "\\u000b",      "\\f",      "\\r",  "\\u000e",  "\\u000f", \
        "\\u0010",  "\\u0011",  "\\u0012",  "\\u0013",  "\\u0014",  "\\u0015",  "\\u0016",  "\\u0017", \
        "\\u0018",  "\\u0019",  "\\u001a",  "\\u001b",  "\\u001c",  "\\u001d",  "\\u001e",  "\\u001f", \
            "\20",      "\21",       "\"",      "\23",      "\24",      "\25",  "\\u0026",  "\\u0027", \
            "\28",      "\29",      "\2A",      "\2B",      "\2C",      "\2D",      "\2E",    "\\\2F", \
            "\30",      "\31",      "\32",      "\33",      "\34",      "\35",      "\36",      "\37", \
        "\\u0038",      "\39",      "\3A",      "\3B",      "\3C",      "\3D",  "\\u003e",      "\3F", \
            "\40",      "\41",      "\42",      "\43",      "\44",      "\45",      "\46",      "\47", \
            "\48",      "\49",      "\4A",      "\4B",      "\4C",      "\4D",      "\4E",      "\4F", \
            "\50",      "\51",      "\52",      "\53",      "\54",      "\55",      "\56",      "\57", \
            "\58",      "\59",      "\5A",      "\5B",       "\\",      "\5D",      "\5E",      "\5F", \
            "\60",      "\61",      "\62",      "\63",      "\64",      "\65",      "\66",      "\67", \
            "\68",      "\69",      "\6A",      "\6B",      "\6C",      "\6D",      "\6E",      "\6F", \
            "\70",      "\71",      "\72",      "\73",      "\74",      "\75",      "\76",      "\77", \
            "\78",      "\79",      "\7A",      "\7B",      "\7C",      "\7D",      "\7E",  "\\u007F"  )

    :if ([:typeof $hexstr] = "nil") do={
        :log error "sms7toJSONStr MUST have a `hexstr` parameter!"
        :return ""
    }
    :local hs $hexstr
    
    

    # make even number of characters
    :if (([:len $hs] & 1) > 0) do={
        :set hs ($hs . "0")
    }

    :local hexVocabulary "0123456789ABCDEF"
    :local result ""
    :local prevDec 0
    :local prevDecBits 0
    :local lastIdx ([:len $hs] - 1)
    :local idx 0

    :while ((idx <= $lastIdx) || ($prevDecBits = 7)) do={
        :local byteToAdd 0
        :if ($prevDecBits = 7) do={
            :set byteToAdd (($prevDec >> 1) & 127)
            :set prevDec 0
            :set prevDecBits 0
        } else={
            :local newDec (([:find $hexVocabulary [:pick $hs $idx]] * 16) + ([:find $hexVocabulary [:pick $hs ($idx+1)]]))
            :set byteToAdd ((($newDec << $prevDecBits) & 127) + ($prevDec >> (8 - $prevDecBits)))
            :set prevDecBits ($prevDecBits + 1)
            :set prevDec $newDec
            :set idx ($idx + 2)
        }
        :local textToAdd  [:pick $asciiChars $byteToAdd]

        #:local hexToAdd ([:pick $hexVocabulary ($byteToAdd >> 4)] . [:pick $hexVocabulary ($byteToAdd & 15)])
        :set result ($result . $textToAdd)
    }
    #:put ("sms7toJSONStr result [" . $result . "]")
    :return $result
} 
#end of sms7toJSONStr


# smsGetOA converts hex string from beginning to JSON string of sms sender (TP-OA)
#     @param <hexstr> - hex string starting from TP-OA (first byte is length byte)
#     @returns object (array) with fields:
#       numberText - JSON string 
#       passChars - how many nibbles(symbols) of message should be skipped
#     @example [$smsGetOA hexstr="0B919701119905F8"] => {numberHex=3739313031313939353038 ("79101199508"); passChars=12}
:local smsGetOA do={
    :if ([:typeof $hexstr] = "nil") do={
        :log error "smsGetOA MUST have a `hexstr` parameter!"
        :return ""
    }
    :local hs $hexstr
    #:put ("smsGetOA [" . $hexstr . "]")
    :local hexVocabulary "0123456789ABCDEF"

    :local txtpos 0
    :local numberText ""
    
    :local numLen    (([:find $hexVocabulary [:pick $hs 0]] * 16) + ([:find $hexVocabulary [:pick $hs 1]]))
    :local numFormat (([:find $hexVocabulary [:pick $hs 2]] * 16) + ([:find $hexVocabulary [:pick $hs 3]]))
    :set txtpos ($txtpos + 4)

    :local realNumLen $numLen
    # Increase real num len to even number of nibbles
    :if (($realNumLen & 1) > 0) do={
        :set realNumLen ($realNumLen + 1)
    }

    #numFormat 
    #
    #    [ 7 | 6   5   4 | 3   2   1   0]
    #    [ 1 |    TON    |      NPI     ]
    #    
    #    1   = Always 1
    #    TON = Type of number. 
    #    NPI = Numbering plan identification (We are not interested in NPI)
    #
    # We are interested in TON "101" bits indicating that number is alfanumeric and should be decoded using `sms7toJSONStr`
    #:put ("numFormat: " . $numFormat)
    # If TON = 101
    if ((($numFormat >> 4) & 7) = 5 ) do={
        #:put "DECODE USING sms7toJSONStr"
        :local numBytes [:pick $hs $txtpos ($txtpos + $realNumLen)]
        #:put ("numBytes [" . $numBytes . "]")
        #:put ("sms7toJSONStr type: " . [:typeof $sms7toJSONStr])
        :set numberText [$sms7toJSONStr hexstr=$numBytes]
        #:put ("numberText [" . $numberText . "]")
    } else={
        #:put "DECODE USING normal"
        :local numTxt ""
        :for bytePos from=$txtpos to=($txtpos + $realNumLen) step=2 do={
            :set numTxt ($numTxt . [:pick $hs ($bytePos+1)] . [:pick $hs ($bytePos+0)])
        }
        :set numTxt [:pick $numTxt 0 $numLen]
        #:put ("numTxt [$numTxt] [" . [:typeof $numTxt] . "]")
        #:for digitPos from=0 to=([:len $numTxt] - 1) step=1 do={
        #    # Numbers 0-9 are 0x30-0x39 in ASCII, so "0" is 0x30 and "9" is 0x39
        #    :set numberText ($numberText . ("\\u003" . [:pick $numTxt $digitPos]))
        #}
        :set numberText $numTxt
    }
    :return {"numberText"=$numberText; "passChars"=($realNumLen + 4)}
}
#end of smsGetOA

#Remove sent messages
:foreach k,v in=$TGBOTMQ do={
    :if (([:pick $k 0 6] = "smstg#") and ($v->"Sent" = "yes")) do={
        :put ("Remove SMS #" . $TGBOTMQ->$k->"SmsIndex")
        /interface lte at-chat lte1 wait=yes input=("AT+CMGD=" . $TGBOTMQ->$k->"SmsIndex")
        :set ($TGBOTMQ->$k) 
    }
}

#get new messages
:local rawmsg ([/interface lte at-chat lte1 wait=yes input="AT+CMGL=4" as-value]->"output")
:local smsList [:toarray ""]
:local smsData
:local pos 0

:while ($pos < ([:len $rawmsg])) do={
	local newlinepos [:find $rawmsg "\n" ($pos - 1)]
	:local line
	:if ([:typeof $newlinepos] = "nil") do={
		:set newlinepos ([:len $rawmsg] )
	}
	
	:local line [:pick $rawmsg $pos ($newlinepos + 1)]
    # Trim \r \n
	:while (([:pick $line ([:len $line] - 1)] = "\r") or ([:pick $line ([:len $line] - 1)] = "\n")) do={
		:set line [:pick $line 0 ([:len $line] - 2)]
	}
	:set pos ($newlinepos + 1)
	:if ( [pick $line 0 2] != "OK" ) do={
		:if ([:pick $line 0] = "+") do={
			:local smsHeaderTemp [:toarray [:pick $line ([:find $line ":"] + 1) [:len $line]]]
			:set smsData { 
				"SmsIdx"=[:pick $smsHeaderTemp 0];
				"Status"=[:pick $smsHeaderTemp 1];
                "FwdOk"=0
#				"Length"=[:pick $smsHeaderTemp 2];
			}
		} else={
            :if ( [typeof [:find "0123456789ABCDEFabcdef" [:pick $line 0]]] != "nil" ) do={
                :local txtpos 0
                #$line = TP-SCA | TP-MTI & Co | TP-OA | TP-PID | TP-DCS | TP-SCTS | TP-UDL | TP-UD
                #:put "X"
                :local "pdu-tp-uhdi-exists" false
                :local "pdu-tp-dcs-value" -1
                :local "pdu-tp-mti-normal" false

                # *TP-SCA (Service Center address)
                ### Get length of record in bytes 
                :local "pdu-tp-sca-length" [$hexToNum hex=[:pick $line $txtpos ($txtpos +2)]]
                :set txtpos ($txtpos + 2)
                ### Skip to end of TP-SCA
                :set txtpos ($txtpos + ($"pdu-tp-sca-length" * 2))

                # *TP-MTI
                ### Get TP-MTI byte
                :local "pdu-tp-mti-data" [$hexToNum hex=[:pick $line $txtpos ($txtpos +2)]]
                :set txtpos ($txtpos + 2)
                ### Set if user data header exists
                :if ((($"pdu-tp-mti-data" >> 6) & 1) > 0) do={
                    :set "pdu-tp-uhdi-exists" true
                }
                :put ("pdu-tp-uhdi-exists " . $"pdu-tp-uhdi-exists")
                ### Set if SMS is SMS-DELIVER
                if (($"pdu-tp-mti-data" & 3) = 0) do={
                    :set "pdu-tp-mti-normal" true
                }
                :put ("pdu-tp-mti-normal " . $"pdu-tp-mti-normal")

                # *TP-OA (Originating Address)
                # We use special function for parsing this
                :set $sender [$smsGetOA hexstr=[:pick $line $txtpos ([:len $line])] sms7toJSONStr=$sms7toJSONStr]
                :set txtpos ($txtpos + ($sender->"passChars"))
                :set $sender ($sender->"numberText")
                

                # *TP-PID
                ### Ignore this byte
                :set txtpos ($txtpos + 2)

                # *TP-DCS (Data Coding Scheme)
                ###  One byte for data coding scheme
                :local "pdu-tp-dcs-value" [$hexToNum hex=[:pick $line $txtpos ($txtpos +2)]]
                :set txtpos ($txtpos + 2)
                :put ("pdu-tp-dcs-value " . $"pdu-tp-dcs-value")

                # *TP-SCTS (Service Center Time Stamp)
                ### Time when SC received message.
                ### 7 Bytes, will ignore them
                :set txtpos ($txtpos + 14)

                # *TP-UDL (User data length)
                ### Depends on message encoding (See TP-DCS)
                ### Message contains length for TP-UDH + TP-UD
                ### If message is encoded using 7-bit encoding, this shows number of 7-BIT characters.
                ###   In this case, there should be 9 bytes for 10-character message,
                ###   because of 10 7-bit characters take 70 bits, and 70 bits take 9 (ceil(70 / 8) = ceil(8.75) = 9) bytes
                ### If message is encoded using UCS-2, this shows number of BYTES
                :local udLenBytes [$hexToNum hex=[:pick $line $txtpos ($txtpos + 2)]]
                :set txtpos ($txtpos + 2)
                ### If encoding is 7-bit. we need to recalculate $udLenBytes value
                :if (($"pdu-tp-dcs-value" & 8) = 0) do={
                    :local udLenBits ($udLenBytes * 7)
                    :set udLenBytes ($udLenBits / 8)
                    :if (($udLenBits % 8) > 0) do={
                        :set udLenBytes ($udLenBytes + 1)
                    }
                }

                # *TP-UDH (User data header)
                ### If TP-MTI:bit6 is 1, this field exists
                :if ($"pdu-tp-uhdi-exists") do={
                    #NOT IMPLEMENTED!
                    :local udhLen 0
                }
                
                # *TP-UD (User data)
                ### The rest of the message is text
                :local msg [:pick $line $txtpos ($txtpos + ($udLenBytes * 2))]
                ### If encoding is 0 (TP-DCS, bits 1 and 2) then we should convert from 7 bit to 8 bit
                :if (($"pdu-tp-dcs-value" & 8) = 0) do={
                    :put "Converting using sms7toJSONStr"
                    :set msg [$sms7toJSONStr hexstr=$msg]
                } else {
                    if (([:len $msg] % 4) = 0) do={
                        :put "Converting using UTF16BE to JSONStr"
                        :local msg2 $msg
                        :set msg ""
                        for i from=0 to=([:len $msg2] - 1) step=4 do={
                            set msg ($msg . "\\u" . [:pick $msg2 $i ($i+4)])
                        }
                    } else={
                        :put "WARNING! MSG not conforms anything"
                    }
                }

                :set smsData ($smsData, {"Sender"=$sender})
                :set smsData ($smsData, {"Message"=$msg})

                :local smsIdx ($smsData->"SmsIdx")
                :set ($smsList->$smsIdx) $smsData
                :set smsData 
            }
		}
	}
	
}



:foreach k,v in=$smsList do={
    :local smsKey ("smstg#" . $k)
    #:put "smsKey $smsKey"

    :if ([:typeof ($TGBOTMQ->$smsKey)] = "nothing") do={
        :put "Enqueue sms with key $smsKey"
        :local message {"Message"=("SMS from `" . $v->"Sender" . "` :\\n```\\n" . $v->"Message" . "\\n```\\n"); "Sent"="no"; "SmsIndex"=$v->"SmsIdx"}
	    :set ($TGBOTMQ->$smsKey) $message
    } 
}


File: /tgbot-startup.rsc
# Alexey D. Filimonov
# MIT License
# Source code at https://github.com/filimonic/mikrotik-sms-forward-telegram
# Version 21.06.11.12


:global TGBOTMQ
while ([:typeof $TGBOTMQ] = "nothing") do={
	:delay delay-time=2s
    :put "waiting TGBOTMQ ..."
}

while ([:typeof [/system ntp client get last-update-from ]] = "nil") do={
    :delay delay-time=2s
    :put "waiting NTP Sync ..."
}

:local bootdate [/system clock print as-value]
:local bootmessage {"Message"=("Boot at `". $bootdate->"date" . "@" . $bootdate->"time" . "`");"Sent"="no"}; 
:set ($TGBOTMQ->"startummsg") $bootmessage;


