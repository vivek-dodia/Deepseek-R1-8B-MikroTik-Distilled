# Repository Information
Name: mikrotik-hotspot-sms

# Directory Structure
Directory structure:
└── github_repos/mikrotik-hotspot-sms/
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
    │   │       │   └── master
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-1c6101dda23b780a4cd90160da06431aed5cbe0f.idx
    │   │       └── pack-1c6101dda23b780a4cd90160da06431aed5cbe0f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── Hotspot + asterisk/
    │   ├── asteriks dial.txt
    │   ├── config.php
    │   ├── hotspot/
    │   │   │   ├── mikrotik.iml
    │   │   │   ├── modules.xml
    │   │   │   └── workspace.xml
    │   │   ├── css/
    │   │   │   ├── form.css
    │   │   │   └── modal.css
    │   │   ├── img/
    │   │   ├── js/
    │   │   ├── login.html
    │   │   └── login_old.html
    │   ├── hotspot.rsc
    │   ├── Log-in script on hotspot profile.txt
    │   ├── Log-out script on hotspot profile.txt
    │   ├── MGuide.php
    │   ├── script backup.txt
    │   └── соглашение.txt
    ├── Hotspot + asterisk + sms/
    │   ├── asteriks dial.txt
    │   ├── cpe.rsc
    │   ├── hotspot/
    │   │   │   ├── mikrotik.iml
    │   │   │   ├── modules.xml
    │   │   │   └── workspace.xml
    │   │   ├── alogin.html
    │   │   ├── by_call/
    │   │   │   ├── css/
    │   │   │   │   ├── form.css
    │   │   │   │   └── modal.css
    │   │   │   ├── img/
    │   │   │   ├── js/
    │   │   │   ├── login.html
    │   │   │   └── login_old.html
    │   │   ├── by_sms/
    │   │   │   │   ├── mikrotik.iml
    │   │   │   │   ├── modules.xml
    │   │   │   │   └── workspace.xml
    │   │   │   ├── css/
    │   │   │   │   ├── form.css
    │   │   │   │   └── modal.css
    │   │   │   ├── img/
    │   │   │   ├── js/
    │   │   │   ├── login.html
    │   │   │   └── login_old.html
    │   │   ├── css/
    │   │   │   ├── finish_page.css
    │   │   │   ├── form.css
    │   │   │   └── modal.css
    │   │   ├── error.html
    │   │   ├── errors.txt
    │   │   ├── fonts/
    │   │   │   ├── LICENSE.txt
    │   │   │   ├── OpenSans-Bold.ttf
    │   │   │   ├── OpenSans-BoldItalic.ttf
    │   │   │   ├── OpenSans-ExtraBold.ttf
    │   │   │   ├── OpenSans-ExtraBoldItalic.ttf
    │   │   │   ├── OpenSans-Italic.ttf
    │   │   │   ├── OpenSans-Light.ttf
    │   │   │   ├── OpenSans-LightItalic.ttf
    │   │   │   ├── OpenSans-Regular.ttf
    │   │   │   ├── OpenSans-SemiBold.ttf
    │   │   │   └── OpenSans-SemiBoldItalic.ttf
    │   │   ├── img/
    │   │   ├── js/
    │   │   ├── login.html
    │   │   ├── login_old.html
    │   │   ├── logout.html
    │   │   ├── lv/
    │   │   │   ├── alogin.html
    │   │   │   ├── errors.txt
    │   │   │   ├── login.html
    │   │   │   ├── logout.html
    │   │   │   ├── radvert.html
    │   │   │   └── status.html
    │   │   ├── md5.js
    │   │   ├── radvert.html
    │   │   ├── redirect.html
    │   │   ├── rlogin.html
    │   │   ├── status.html
    │   │   └── xml/
    │   │       ├── alogin.html
    │   │       ├── css/
    │   │       │   ├── form.css
    │   │       │   └── modal.css
    │   │       ├── error.html
    │   │       ├── flogout.html
    │   │       ├── fonts/
    │   │       │   ├── LICENSE.txt
    │   │       │   ├── OpenSans-Bold.ttf
    │   │       │   ├── OpenSans-BoldItalic.ttf
    │   │       │   ├── OpenSans-ExtraBold.ttf
    │   │       │   ├── OpenSans-ExtraBoldItalic.ttf
    │   │       │   ├── OpenSans-Italic.ttf
    │   │       │   ├── OpenSans-Light.ttf
    │   │       │   ├── OpenSans-LightItalic.ttf
    │   │       │   ├── OpenSans-Regular.ttf
    │   │       │   └── OpenSans-SemiBold.ttf
    │   │       ├── login.html
    │   │       ├── logout.html
    │   │       ├── rlogin.html
    │   │       └── WISPAccessGatewayParam.xsd
    │   ├── Log-in script on hotspot profile.txt
    │   ├── Log-out script on hotspot profile.txt
    │   ├── script backup.txt
    │   ├── script on userman server.txt
    │   ├── userman-server.rsc
    │   └── соглашение.txt
    ├── Hotspot sms/
    │   ├── hotspot/
    │   │   │   ├── mikrotik.iml
    │   │   │   ├── modules.xml
    │   │   │   └── workspace.xml
    │   │   ├── css/
    │   │   │   ├── form.css
    │   │   │   └── modal.css
    │   │   ├── img/
    │   │   ├── js/
    │   │   ├── login.html
    │   │   └── login_old.html
    │   ├── hotspot.rsc
    │   ├── Log-in script on hotspot profile.txt
    │   ├── Log-out script on hotspot profile.txt
    │   ├── script backup.txt
    │   ├── script.txt
    │   └── соглашение.txt
    └── README.md


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
	url = https://github.com/soriel/mikrotik-hotspot-sms.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/master


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
0000000000000000000000000000000000000000 6f1558d21002dd8190ec5aa42ffb011abcdb178c vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/soriel/mikrotik-hotspot-sms.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 6f1558d21002dd8190ec5aa42ffb011abcdb178c vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/soriel/mikrotik-hotspot-sms.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 6f1558d21002dd8190ec5aa42ffb011abcdb178c vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/soriel/mikrotik-hotspot-sms.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
6f1558d21002dd8190ec5aa42ffb011abcdb178c refs/remotes/origin/master


File: /.git\refs\heads\master
6f1558d21002dd8190ec5aa42ffb011abcdb178c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /Hotspot + asterisk\asteriks dial.txt
exten => 0002,1,Noop(MGuide)
same  => n,System(ssh -oStrictHostKeyChecking=no admin@ip-mikrotik /ip hotspot user add name=${CALLERID(num)} password=${CALLERID(num)})
same  => n,Hangup()

File: /Hotspot + asterisk\config.php
<?php

/*Connect to Mikrotik __OLD_CONFIG*/
/*$mik_logon = array(
			array('ip_addr' => '192.168.170.198', 'login' => 'admin', 'pass' => '', 'name' => '367'),
			array('ip_addr' => '192.168.170.196', 'login' => 'admin', 'pass' => '', 'name' => '368')
);*/

// array MAC autogenerate
//$arr_automac = array("DA:A1:19");

/*Config Mikrotik*/
define('DURATION', '30');
//define('INTERFACE_WIRELESS', 'wlan1');
define('MAX_BEACON_STRENGTH', -110);
define('START_WORK_TIME','10:00');
define('END_WORK_TIME','19:00');

define('HOST','localhost');
define('DB_NAME','wiflow');
define('DB_USER','root');
define('DB_PASSWORD','mozc__WSZOL5');

/*Config Mikrotik Guide*/
$arr_logon = array(
	'ip_addr' => '192.168.170.198',
	'login' => 'admin',
	'pass' => ''
);

?>

File: /Hotspot + asterisk\hotspot\.idea\mikrotik.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$" />
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>

File: /Hotspot + asterisk\hotspot\.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /Hotspot + asterisk\hotspot\.idea\workspace.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ChangeListManager">
    <list default="true" id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
    <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />
    <option name="TRACKING_ENABLED" value="true" />
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="FileEditorManager">
    <leaf SIDE_TABS_SIZE_LIMIT_KEY="300">
      <file leaf-file-name="login.html" pinned="false" current-in-tab="true">
        <entry file="file://$PROJECT_DIR$/login.html">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="239">
              <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
              <folding>
                <element signature="e#1605#1819#0" expanded="false" />
                <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
              </folding>
            </state>
          </provider>
        </entry>
      </file>
      <file leaf-file-name="form.css" pinned="false" current-in-tab="false">
        <entry file="file://$PROJECT_DIR$/css/form.css">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="135">
              <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
              <folding />
            </state>
          </provider>
        </entry>
      </file>
    </leaf>
  </component>
  <component name="FileTemplateManagerImpl">
    <option name="RECENT_TEMPLATES">
      <list>
        <option value="CSS File" />
        <option value="HTML File" />
      </list>
    </option>
  </component>
  <component name="FindInProjectRecents">
    <findStrings>
      <find>wid</find>
    </findStrings>
  </component>
  <component name="GradleLocalSettings">
    <option name="externalProjectsViewState">
      <projects_view />
    </option>
  </component>
  <component name="IdeDocumentHistory">
    <option name="CHANGED_PATHS">
      <list>
        <option value="$PROJECT_DIR$/css.css" />
        <option value="$PROJECT_DIR$/img/arrow.svg" />
        <option value="$PROJECT_DIR$/img/number.svg" />
        <option value="$PROJECT_DIR$/css/form.css" />
        <option value="$PROJECT_DIR$/index.html" />
        <option value="$PROJECT_DIR$/login.html" />
      </list>
    </option>
  </component>
  <component name="JsBuildToolGruntFileManager" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsBuildToolPackageJson" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsGulpfileManager">
    <detection-done>true</detection-done>
    <sorting>DEFINITION_ORDER</sorting>
  </component>
  <component name="PhpWorkspaceProjectConfiguration" backward_compatibility_performed="true" />
  <component name="ProjectFrameBounds">
    <option name="x" value="248" />
    <option name="y" value="22" />
    <option name="width" value="949" />
    <option name="height" value="731" />
  </component>
  <component name="ProjectInspectionProfilesVisibleTreeState">
    <entry key="Project Default">
      <profile-state>
        <expanded-state>
          <State>
            <id />
          </State>
          <State>
            <id>Abstraction issuesJava</id>
          </State>
          <State>
            <id>ActionScript specificJavaScript</id>
          </State>
          <State>
            <id>Android</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Accessibility</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Chrome OS</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Messages</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization &gt; Bidirectional Text</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Lint</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Performance</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Security</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Icons</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Typography</id>
          </State>
          <State>
            <id>Android Lint for Kotlin</id>
          </State>
          <State>
            <id>Ant inspections</id>
          </State>
          <State>
            <id>Application Server Specific Inspections</id>
          </State>
          <State>
            <id>ArquillianJava</id>
          </State>
          <State>
            <id>BashSupport</id>
          </State>
          <State>
            <id>Batch Applications Issues</id>
          </State>
          <State>
            <id>Bean Validation issues</id>
          </State>
          <State>
            <id>CDI(Contexts and Dependency Injection) issues</id>
          </State>
          <State>
            <id>CSS</id>
          </State>
          <State>
            <id>Class metricsJava</id>
          </State>
          <State>
            <id>Class structureJava</id>
          </State>
          <State>
            <id>Cloning issuesJava</id>
          </State>
          <State>
            <id>Code SmellPHP</id>
          </State>
          <State>
            <id>Code StylePHP</id>
          </State>
          <State>
            <id>Code quality toolsCSS</id>
          </State>
          <State>
            <id>Code quality toolsJavaScript</id>
          </State>
          <State>
            <id>Code style issuesGo</id>
          </State>
          <State>
            <id>Code style issuesJava</id>
          </State>
          <State>
            <id>Code style issuesJavaScript</id>
          </State>
          <State>
            <id>CodeSpring CoreSpring</id>
          </State>
          <State>
            <id>CoffeeScript</id>
          </State>
          <State>
            <id>Control flow issuesGroovy</id>
          </State>
          <State>
            <id>Control flow issuesJava</id>
          </State>
          <State>
            <id>Control flow issuesJavaScript</id>
          </State>
          <State>
            <id>CorrectnessLintAndroid</id>
          </State>
          <State>
            <id>Cucumber Java</id>
          </State>
          <State>
            <id>DOM issuesJavaScript</id>
          </State>
          <State>
            <id>Data flow issuesJava</id>
          </State>
          <State>
            <id>Data flow issuesJavaScript</id>
          </State>
          <State>
            <id>Declaration redundancyGo</id>
          </State>
          <State>
            <id>Declaration redundancyJava</id>
          </State>
          <State>
            <id>Dependency issuesJava</id>
          </State>
          <State>
            <id>Encapsulation issuesJava</id>
          </State>
          <State>
            <id>Error handlingGroovy</id>
          </State>
          <State>
            <id>Error handlingJava</id>
          </State>
          <State>
            <id>Error handlingJavaScript</id>
          </State>
          <State>
            <id>Error handlingPHP</id>
          </State>
          <State>
            <id>Finalization issuesJava</id>
          </State>
          <State>
            <id>FlexUnit inspections</id>
          </State>
          <State>
            <id>GPathGroovy</id>
          </State>
          <State>
            <id>General</id>
          </State>
          <State>
            <id>GeneralGo</id>
          </State>
          <State>
            <id>GeneralJavaScript</id>
          </State>
          <State>
            <id>GeneralPHP</id>
          </State>
          <State>
            <id>Go</id>
          </State>
          <State>
            <id>Google App Engine</id>
          </State>
          <State>
            <id>Google Web Toolkit issues</id>
          </State>
          <State>
            <id>GrailsGroovy</id>
          </State>
          <State>
            <id>Groovy</id>
          </State>
          <State>
            <id>Guice Inspections</id>
          </State>
          <State>
            <id>HTML</id>
          </State>
          <State>
            <id>Haml</id>
          </State>
          <State>
            <id>Ignore</id>
          </State>
          <State>
            <id>Inheritance issuesJava</id>
          </State>
          <State>
            <id>Initialization issuesJava</id>
          </State>
          <State>
            <id>Internationalization issues</id>
          </State>
          <State>
            <id>Internationalization issuesJava</id>
          </State>
          <State>
            <id>Invalid elementsCSS</id>
          </State>
          <State>
            <id>J2ME issuesJava</id>
          </State>
          <State>
            <id>JBoss Seam issues</id>
          </State>
          <State>
            <id>JPA issues</id>
          </State>
          <State>
            <id>JSON</id>
          </State>
          <State>
            <id>JSP Inspections</id>
          </State>
          <State>
            <id>JUnit issuesJava</id>
          </State>
          <State>
            <id>Java</id>
          </State>
          <State>
            <id>Java 5Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 7Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 8Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 9Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java EE issues</id>
          </State>
          <State>
            <id>Java interop issuesKotlin</id>
          </State>
          <State>
            <id>Java language level migration aidsJava</id>
          </State>
          <State>
            <id>JavaScript</id>
          </State>
          <State>
            <id>JavaScript validity issuesJavaScript</id>
          </State>
          <State>
            <id>Javadoc issuesJava</id>
          </State>
          <State>
            <id>Kotlin</id>
          </State>
          <State>
            <id>Kotlin Android</id>
          </State>
          <State>
            <id>Language Injection</id>
          </State>
          <State>
            <id>LintAndroid</id>
          </State>
          <State>
            <id>Logging issuesJava</id>
          </State>
          <State>
            <id>Manifest</id>
          </State>
          <State>
            <id>Maven</id>
          </State>
          <State>
            <id>Memory issuesJava</id>
          </State>
          <State>
            <id>Method metricsGroovy</id>
          </State>
          <State>
            <id>Modularization issuesJava</id>
          </State>
          <State>
            <id>Naming conventionsGroovy</id>
          </State>
          <State>
            <id>Naming conventionsJava</id>
          </State>
          <State>
            <id>Naming conventionsKotlin</id>
          </State>
          <State>
            <id>Node.jsJavaScript</id>
          </State>
          <State>
            <id>Numeric issuesJava</id>
          </State>
          <State>
            <id>OSGi</id>
          </State>
          <State>
            <id>Other problemsKotlin</id>
          </State>
          <State>
            <id>PHP</id>
          </State>
          <State>
            <id>Pattern Validation</id>
          </State>
          <State>
            <id>Performance issuesJava</id>
          </State>
          <State>
            <id>Plugin DevKit</id>
          </State>
          <State>
            <id>Portability issuesJava</id>
          </State>
          <State>
            <id>Potentially confusing code constructsGroovy</id>
          </State>
          <State>
            <id>Potentially confusing code constructsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsCSS</id>
          </State>
          <State>
            <id>Probable bugsCoffeeScript</id>
          </State>
          <State>
            <id>Probable bugsGo</id>
          </State>
          <State>
            <id>Probable bugsJava</id>
          </State>
          <State>
            <id>Probable bugsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsKotlin</id>
          </State>
          <State>
            <id>Probable bugsPHP</id>
          </State>
          <State>
            <id>Properties Files</id>
          </State>
          <State>
            <id>Properties FilesJava</id>
          </State>
          <State>
            <id>RESTful Web Service</id>
          </State>
          <State>
            <id>Redundant constructsKotlin</id>
          </State>
          <State>
            <id>RegExp</id>
          </State>
          <State>
            <id>SQL</id>
          </State>
          <State>
            <id>Security issuesJava</id>
          </State>
          <State>
            <id>Serialization issuesJava</id>
          </State>
          <State>
            <id>SetupSpring CoreSpring</id>
          </State>
          <State>
            <id>Spelling</id>
          </State>
          <State>
            <id>Spring</id>
          </State>
          <State>
            <id>Spring BootSpring</id>
          </State>
          <State>
            <id>Spring CoreSpring</id>
          </State>
          <State>
            <id>Spring DataSpring</id>
          </State>
          <State>
            <id>Spring OSGiSpring</id>
          </State>
          <State>
            <id>Struts</id>
          </State>
          <State>
            <id>Struts 1Struts</id>
          </State>
          <State>
            <id>Struts 2Struts</id>
          </State>
          <State>
            <id>Style issuesKotlin</id>
          </State>
          <State>
            <id>StyleGroovy</id>
          </State>
          <State>
            <id>TestNGJava</id>
          </State>
          <State>
            <id>Threading issuesGroovy</id>
          </State>
          <State>
            <id>Threading issuesJava</id>
          </State>
          <State>
            <id>Thymeleaf</id>
          </State>
          <State>
            <id>Type compatibilityPHP</id>
          </State>
          <State>
            <id>TypeScript</id>
          </State>
          <State>
            <id>UI Form Problems</id>
          </State>
          <State>
            <id>UndefinedPHP</id>
          </State>
          <State>
            <id>Validity issuesGroovy</id>
          </State>
          <State>
            <id>Visibility issuesJava</id>
          </State>
          <State>
            <id>Web Services</id>
          </State>
          <State>
            <id>WebSocket issues</id>
          </State>
          <State>
            <id>XML</id>
          </State>
          <State>
            <id>XMLSpring CoreSpring</id>
          </State>
          <State>
            <id>XPath</id>
          </State>
        </expanded-state>
      </profile-state>
    </entry>
  </component>
  <component name="ProjectView">
    <navigator currentView="ProjectPane" proportions="" version="1">
      <flattenPackages />
      <showMembers />
      <showModules />
      <showLibraryContents />
      <hideEmptyPackages />
      <abbreviatePackageNames />
      <autoscrollToSource />
      <autoscrollFromSource />
      <sortByType />
      <manualOrder />
      <foldersAlwaysOnTop value="true" />
    </navigator>
    <panes>
      <pane id="Scratches" />
      <pane id="PackagesPane" />
      <pane id="ProjectPane">
        <subPane>
          <expand>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
            </path>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
              <item name="img" type="462c0819:PsiDirectoryNode" />
            </path>
          </expand>
          <select />
        </subPane>
      </pane>
      <pane id="AndroidView" />
      <pane id="Scope" />
    </panes>
  </component>
  <component name="PropertiesComponent">
    <property name="nodejs_interpreter_path.stuck_in_default_project" value="undefined stuck path" />
    <property name="settings.editor.selected.configurable" value="editor.preferences.fonts.default" />
    <property name="WebServerToolWindowFactoryState" value="false" />
    <property name="aspect.path.notification.shown" value="true" />
    <property name="last_opened_file_path" value="$PROJECT_DIR$" />
    <property name="list.type.of.created.stylesheet" value="CSS" />
    <property name="DefaultHtmlFileTemplate" value="HTML File" />
  </component>
  <component name="RecentsManager">
    <key name="MoveFile.RECENT_KEYS">
      <recent name="$PROJECT_DIR$/js" />
      <recent name="$PROJECT_DIR$/img" />
    </key>
  </component>
  <component name="RunDashboard">
    <option name="ruleStates">
      <list>
        <RuleState>
          <option name="name" value="ConfigurationTypeDashboardGroupingRule" />
        </RuleState>
        <RuleState>
          <option name="name" value="StatusDashboardGroupingRule" />
        </RuleState>
      </list>
    </option>
  </component>
  <component name="RunManager">
    <configuration default="true" type="Applet" factoryName="Applet">
      <option name="HTML_USED" value="false" />
      <option name="WIDTH" value="400" />
      <option name="HEIGHT" value="300" />
      <option name="POLICY_FILE" value="$APPLICATION_HOME_DIR$/bin/appletviewer.policy" />
      <module />
    </configuration>
    <configuration default="true" type="Application" factoryName="Application">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <option name="MAIN_CLASS_NAME" />
      <option name="VM_PARAMETERS" />
      <option name="PROGRAM_PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="ENABLE_SWING_INSPECTOR" value="false" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <module name="" />
      <envs />
    </configuration>
    <configuration default="true" type="JUnit" factoryName="JUnit">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="TEST_OBJECT" value="class" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <envs />
      <patterns />
    </configuration>
    <configuration name="login_old.html" type="JavascriptDebugType" factoryName="JavaScript Debug" temporary="true" nameIsGenerated="true" uri="http://localhost:63343/mikrotik/login_old.html" />
    <configuration default="true" type="Remote" factoryName="Remote">
      <option name="USE_SOCKET_TRANSPORT" value="true" />
      <option name="SERVER_MODE" value="false" />
      <option name="SHMEM_ADDRESS" value="javadebug" />
      <option name="HOST" value="localhost" />
      <option name="PORT" value="5005" />
    </configuration>
    <configuration default="true" type="TestNG" factoryName="TestNG">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="SUITE_NAME" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="GROUP_NAME" />
      <option name="TEST_OBJECT" value="CLASS" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="OUTPUT_DIRECTORY" />
      <option name="ANNOTATION_TYPE" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <option name="USE_DEFAULT_REPORTERS" value="false" />
      <option name="PROPERTIES_FILE" />
      <envs />
      <properties />
      <listeners />
    </configuration>
    <configuration default="true" type="#org.jetbrains.idea.devkit.run.PluginConfigurationType" factoryName="Plugin">
      <module name="" />
      <option name="VM_PARAMETERS" value="-Xmx512m -Xms256m -XX:MaxPermSize=250m -ea" />
      <option name="PROGRAM_PARAMETERS" />
      <predefined_log_file id="idea.log" enabled="true" />
    </configuration>
    <recent_temporary>
      <list size="1">
        <item index="0" class="java.lang.String" itemvalue="JavaScript Debug.login_old.html" />
      </list>
    </recent_temporary>
  </component>
  <component name="ShelveChangesManager" show_recycled="false">
    <option name="remove_strategy" value="false" />
  </component>
  <component name="SvnConfiguration">
    <configuration />
  </component>
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
      <created>1521018748772</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1521018748772</updated>
      <workItem from="1521018751184" duration="14087000" />
      <workItem from="1521057296181" duration="563000" />
      <workItem from="1521058090953" duration="1147000" />
      <workItem from="1521059914099" duration="565000" />
    </task>
    <servers />
  </component>
  <component name="TimeTrackingManager">
    <option name="totallyTimeSpent" value="16362000" />
  </component>
  <component name="ToolWindowManager">
    <frame x="248" y="22" width="949" height="731" extended-state="0" />
    <editor active="true" />
    <layout>
      <window_info id="Palette" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />
      <window_info id="Palette&#9;" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Image Layers" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Analysis" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="true" content_ui="tabs" />
      <window_info id="Maven Projects" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Run" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="false" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Tool" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.26571113" sideWeight="0.5" order="0" side_tool="false" content_ui="combo" />
      <window_info id="Docker" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Database" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Learn" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="Ant Build" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="UI Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Theme Preview" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.39937106" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="true" content_ui="tabs" />
      <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />
      <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Commander" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Hierarchy" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="combo" />
      <window_info id="Inspection" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="5" side_tool="false" content_ui="tabs" />
      <window_info id="Find" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
    </layout>
  </component>
  <component name="TypeScriptGeneratedFilesManager">
    <option name="version" value="1" />
  </component>
  <component name="VcsContentAnnotationSettings">
    <option name="myLimit" value="2678400000" />
  </component>
  <component name="XDebuggerManager">
    <breakpoint-manager>
      <option name="time" value="1" />
    </breakpoint-manager>
    <watches-manager />
  </component>
  <component name="editorHistoryManager">
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css.css" />
    <entry file="file://$PROJECT_DIR$/img/arrow.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/number.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/integrasky.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$APPLICATION_HOME_DIR$/plugins/JavaScriptLanguage/jsLanguageServicesImpl/external/lib.dom.d.ts">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="119">
          <caret line="12227" column="4" lean-forward="false" selection-start-line="12227" selection-start-column="4" selection-end-line="12227" selection-end-column="4" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login_old.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="-545">
          <caret line="71" column="9" lean-forward="true" selection-start-line="60" selection-start-column="0" selection-end-line="71" selection-end-column="9" />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="239">
          <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
  </component>
  <component name="masterDetails">
    <states>
      <state key="ProjectJDKs.UI">
        <settings>
          <last-edited>ruby-2.5.0-p0</last-edited>
          <splitter-proportions>
            <option name="proportions">
              <list>
                <option value="0.2" />
              </list>
            </option>
          </splitter-proportions>
        </settings>
      </state>
    </states>
  </component>
</project>

File: /Hotspot + asterisk\hotspot\css\form.css
html, body {
    background: url("../img/background.png");
    height: 100%;
    min-height: 100px;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.logo {
    margin-bottom: 42px;
}

label {
    font-size: 12px;
    font-family: "Opium";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    background: #fff;
    border: solid 1px rgb(220, 224, 226);
    border-radius: 15px;
    padding: 42px;

}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    background-color: rgb(237, 245, 255);
    border: none;
    padding: 17px;
    margin: 7px;
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

.code input[type="text"], .form.already input[type="text"]{
    text-align: center !important;
}

.btn {

    font-size: 12px;
    font-family: "Roboto";
    color: rgb(255, 255, 255);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;

    border-radius: 5px;
    border: none;
    background-color: rgb(77, 161, 255);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;

    margin: 0 auto;

}

.disabled, .disabled:hover{
    background: #eee !important;
    cursor: auto;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.form_description {
    font-size: 16px;
    font-family: "Opium";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_group img {
    margin-right: 14px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: #0421EA !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk\hotspot\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot + asterisk\hotspot\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Alexander A Kusakin <alexander.a.kusakin@gmail.com>">

    <link rel="stylesheet" href="./css/form.css">
    <link rel="stylesheet" href="./css/modal.css">

    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>

        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }

        jQuery(document).ready(function () {

            jQuery('#login').mask('+7-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');
                    jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            /*CHANGE*/

            jQuery('#login2').mask('+7-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {

                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {

                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                

            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 3)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 3) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });
            /*END_CHANGE*/

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }
            });

            jQuery('#code').on('keyup', function (event) {

                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 3) {
                    jQuery(this).addClass('disabled').removeClass('active');
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                }
            });

            jQuery('#has_code').on('click', function () {
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500)
                });
            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }
        });

    function Connect()
    {
        jQuery('#code').val(document.getElementById('username2').value);
        jQuery('#password').val(hexMD5('$(chap-id)' + jQuery('#code').val() + '$(chap-challenge)'));
        return jQuery('.code .btn.active').click();
    }

    </script>
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="./img/integrasky.svg" alt="integrasky" width="200px" style="width:200px">
    </div>
    <!--<small class="form_description">Please log on to use the internet hotspot service</small>-->
    <form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="$(link-login-only)" method="post">
        <label for="login">Введите номер</label>
        <br>
        <div class="input_group tel">
            <img src="./img/number.svg" alt="number">
            <input type="hidden" name="username" id="username1">
            <input type="text" id="login" placeholder="+7-(XXX)-XXX-XX-XX">
        </div>
        <br>
        <button class="btn next">
            Далее
        </button>
    </form>

    <form class="form code" style="display: none" name="sendin" action="" method="post">
        <!--<label for="code">Введите код</label>-->
        <label for="code">Для получения доступа необходимо позвонить на номер 84959898533</label>
        <br>
        <div class="input_group">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <!--<input type="text" id="code" maxlength="16" placeholder="********">-->
            <input type="hidden" id="code">
        </div>
        <br>
        <input type="submit" class="btn" value="Далее" onclick="Connect()" />
    </form>

    <!--<form class="form already" style="display: none" name="sendin" action="" method="post">
        <label for="login2">Введите номер</label>
        <br>
        <div class="input_group tel">
            <input type="text" id="login2" placeholder="+7-(XXX)-XXX-XX-XX">
        </div>
        
        <br>
        <div class="input_group">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" id="code2" maxlength="16" placeholder="********">
        </div>
        <br>
        <input type="submit" class="btn" value="Далее"/>
    </form>-->

    <br><br>
    <small>Powered by MikroTik RouterOS</small>
    <a id="has_code" href="#">У меня уже есть код</a>
    <label id="modal_trigger" for="modal-trigger">Политика конфиденциальности</label>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</body>
</html>

File: /Hotspot + asterisk\hotspot\login_old.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>internet hotspot > login</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="pragma" content="no-cache"/>
    <meta http-equiv="expires" content="-1"/>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>

    <link rel="stylesheet" href="./css/form.css">

    <style type="text/css">
        body {
            color: #737373;
            font-size: 10px;
            font-family: verdana;
        }

        textarea, input, select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active {
            color: #AAAAAA;
            text-decoration: none;
            font-size: 10px;
        }

        a:hover {
            border-bottom: 1px dotted #c1c1c1;
            color: #AAAAAA;
        }

        img {
            border: none;
        }

        td {
            font-size: 14px;
            color: #7A7A7A;
        }
    </style>

</head>

<body>
$(if chap-id)
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username"/>
    <input type="hidden" name="password"/>
    <input type="hidden" name="dst" value="$(link-orig)"/>
    <input type="hidden" name="popup" value="true"/>
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    <!--
    function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
        document.sendin.submit();
        return false;
    }

    //-->
</script>
$(endif)

<div align="center">
    <a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <!--<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br/>$(if-->
                <!--trial == 'yes')Free trial available, <a style="color: #FF8080"-->
                                                        <!--href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click-->
                    <!--here</a>.$(endif)-->
            <!--</div>-->
            <div>
                <small>Please log on to use the internet hotspot service</small>
            </div>
            <br/>
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0"
                   cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form name="login" action="$(link-login-only)" method="post"
                              $(if chap-id) onSubmit="return doLogin()" $(endif)>
                            <input type="hidden" name="dst" value="$(link-orig)"/>
                            <input type="hidden" name="popup" value="true"/>

                            <table width="100" style="background-color: #ffffff">
                                <tr>
                                    <td align="right">login</td>
                                    <td><input style="width: 80px" name="username" type="text" value="$(username)"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right">password</td>
                                    <td><input style="width: 80px" name="password" type="password"/></td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                    <td><input type="submit" value="OK"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr>
                    <td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img
                            src="/img/logobottom.png" alt="mikrotik"/></a></td>
                </tr>
            </table>

            <br/>
            <div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            $(if error)<br/>
            <div style="color: #FF8080; font-size: 9px">$(error)</div>
            $(endif)
        </td>
    </tr>
</table>

<script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
</script>
</body>
</html>


File: /Hotspot + asterisk\hotspot.rsc
/interface bridge
add fast-forward=no name=bridge1
add comment=Hotspot fast-forward=no name=bridge2
add fast-forward=no name=lo
/interface wireless
set [ find default-name=wlan2 ] ssid=MikroTik
/interface list
add name=WAN
add name=local
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk eap-methods="" management-protection=\
    allowed mode=dynamic-keys name=guest supplicant-identity="" \
    wpa2-pre-shared-key=PassWord123
/interface wireless
set [ find default-name=wlan1 ] adaptive-noise-immunity=ap-and-client-mode \
    band=2ghz-onlyn country=russia3 default-forwarding=no disabled=no \
    distance=indoors hw-protection-mode=cts-to-self max-station-count=30 \
    mode=ap-bridge preamble-mode=long radio-name=Mikrotik-Training.ru-Guest \
    security-profile=guest ssid=Mikrotik-Training.ru-Guest
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot
add hotspot-address=10.5.50.1 html-directory=flash/hotspot name=hsprof1 \
    use-radius=yes
/ip hotspot user profile
set [ find default=yes ] on-login=":local nas [/system identity get name];\r\
    \n:local today [/system clock get date];\r\
    \n:local time1 [/system clock get time ];\r\
    \n:local ipuser [/ip hotspot active get [find user=\$user] address];\r\
    \n:local usermac [/ip hotspot active get [find user=\$user] mac-address]\r\
    \n:put \$today\r\
    \n:put \$time1\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n:local min [:pick \$time1 3 5]; \r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n:local mac1 [:pick \$usermac 0 2];\r\
    \n:local mac2 [:pick \$usermac 3 5];\r\
    \n:local mac3 [:pick \$usermac 6 8];\r\
    \n:local mac4 [:pick \$usermac 9 11];\r\
    \n:local mac5 [:pick \$usermac 12 14];\r\
    \n:local mac6 [:pick \$usermac 15 17];\r\
    \n:set \$usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6\
    })]\r\
    \n:put \$time1\r\
    \n/ip firewall address-list add list=\$today address=\"log-in.\$time1.\$us\
    er.\$usermac.\$ipuser\"\r\
    \n\r\
    \ndo {/tool e-mail send to=\"email@gmail.com\" subject=\"Login number:\
    \_\$user on \$nas\" body=\"Login number: \$user mac-address: \$usermac tim\
    e: \$time1 ip-address: \$ipuser\"} on-error={};" on-logout=":local nas [/s\
    ystem identity get name];\r\
    \n:local today [/system clock get date];\r\
    \n:local time1 [/system clock get time ];\r\
    \n:put \$today\r\
    \n:put \$time1\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n:local min [:pick \$time1 3 5];\r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n:put \$time1\r\
    \n/ip firewall address-list add list=\$today address=\"log-out.\$time1.\$u\
    ser\"\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=\"Logout number: \$\
    user on \$nas\" body=\"Logout number: \$user time: \$time1\""
/ip pool
add name=hs-pool-9 ranges=10.5.50.2-10.5.50.254
/ip dhcp-server
add address-pool=hs-pool-9 disabled=no interface=bridge2 lease-time=1h name=\
    dhcp1
/ip hotspot
add address-pool=hs-pool-9 disabled=no interface=bridge2 name=hotspot1 \
    profile=hsprof1
/system logging action
add name=hotspot target=memory
/tool user-manager customer
set admin access=\
    own-routers,own-users,own-profiles,own-limits,config-payment-gw
/tool user-manager profile
add name=hotspot name-for-users="" override-shared-users=off owner=admin \
    price=0 starts-at=logon validity=0s
/tool user-manager profile limitation
add address-list="" download-limit=0B group-name="" ip-pool="" name=unlimited \
    owner=admin transfer-limit=0B upload-limit=0B uptime-limit=0s
/interface bridge port
add bridge=bridge2 interface=wlan1
/ip neighbor discovery-settings
set discover-interface-list=WAN
/interface list member
add interface=ether1 list=WAN
add interface=ether2 list=local
add interface=bridge1 list=local
/ip address
add address=10.5.50.1/24 comment="hotspot network" interface=bridge2 network=\
    10.5.50.0
add address=10.11.11.1 interface=lo network=10.11.11.1
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=10.5.50.0/24 comment="hotspot network" gateway=10.5.50.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip firewall address-list
add address=log-in.165846.9067634683.60F1894825C4.10.5.50.254 list=\
    mar/14/2018
add address=log-out.170409.9067634683 list=mar/14/2018
add address=log-in.170543.9067634683.60F1894825C4.10.5.50.254 list=\
    mar/14/2018
/ip firewall filter
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
add action=accept chain=forward comment=Established/related connection-state=\
    established,related
add action=accept chain=input connection-state=established,related
add action=drop chain=input comment=Invalid connection-state=invalid \
    in-interface-list=WAN
add action=drop chain=forward connection-state=invalid in-interface-list=WAN
add action=accept chain=input comment=Icmp in-interface-list=WAN protocol=\
    icmp
add action=accept chain=input comment=Winbox dst-port=8291 in-interface-list=\
    WAN protocol=tcp
add action=accept chain=input comment=Webfig dst-port=80 in-interface-list=\
    WAN protocol=tcp
add action=drop chain=input comment=Drop in-interface-list=WAN
add action=drop chain=forward in-interface-list=WAN
/ip firewall nat
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
add action=masquerade chain=srcnat comment="masquerade hotspot network" \
    out-interface-list=WAN src-address=10.5.50.0/24
add action=masquerade chain=srcnat out-interface-list=WAN
/ip hotspot user
add name=admin
add name=9067634683 password=1879
/radius
add accounting-backup=yes address=10.11.11.1 secret=PassWord123! service=\
    hotspot src-address=10.11.11.1
/system clock
set time-zone-name=Europe/Moscow
/system identity
set name=Mikrotik-Training.ru-Guest
/system logging
add action=hotspot topics=hotspot,debug,info,!account
/system scheduler
add interval=1d name=backup on-event="/system script run backup " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=mar/14/2018 start-time=13:41:01
add interval=30s name=hotspot on-event="/system script run hotspot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=mar/14/2018 start-time=13:59:23
/system script
add name=hotspot owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    Search number in log hotspot\
    \n\
    \n:foreach line in=[/log find buffer=hotspot message~\"login failed\"] do=\
    {\
    \n :do {:local content [/log get \$line message];\
    \n  :put \$content;\
    \n  :local pos1 [:find \$content \" (\" 0];\
    \n  :put \$pos1;\
    \n  :if (\$pos1 != \" \") do={ \
    \n   :local uname \"\"; \
    \n   :local uname7 \"\";\
    \n   :local uname8 \"\";\
    \n   :local uname9 \"\";\
    \n   :local phone \"\"; \
    \n   :if ([:pick \$content (\$pos1-11)] = \"8\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time]; \
    \n    :local hour [:pick \$date 0 2]; \
    \n    :local min [:pick \$date 3 5]; \
    \n    :local sec [:pick \$date 6 8]; \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-5)];\
    \n    :put \$usernumber;\
    \n    :global pass 27394; \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber); \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524;\
    \n     }\
    \n    :put \$pass;\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={}; \
    \n    ##SMS.ru\
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool fetch url=\"https://gate.smsaero.ru/send/\\\?user=info@ast\"https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\\"} on-error={};\
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;    \
    \n    }\
    \n   :if ([:pick \$content (\$pos1-10)] = \"9\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time]; \
    \n    :local hour [:pick \$date 0 2]; \
    \n    :local min [:pick \$date 3 5]; \
    \n    :local sec [:pick \$date 6 8]; \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-5)];\
    \n    :put \$usernumber;\
    \n    :global pass 27394; \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber); \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524;\
    \n     }\
    \n    :put \$pass;\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname7;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={}; \
    \n    ##SMS.ru\
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool fetch url=\"https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\"} on-error={};\
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;    \
    \n    }\
    \n\
    \n   :if ([:pick \$content (\$pos1-11)] = \"7\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time] \
    \n    :local hour [:pick \$date 0 2] \
    \n    :local min [:pick \$date 3 5] \
    \n    :local sec [:pick \$date 6 8] \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-4)];\
    \n    :global pass 27394 \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber) \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524 \
    \n     } \
    \n    :put \$pass\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={};\
    \n    ##SMS \
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    do {/tool fetch url=\""https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;  \
    \n\
    \n    }\
    \n  }\
    \n }\
    \n}\
    \n\
    \n\
    \n\
    \n# Clear hostpot log\
    \n\
    \n/system logging action set hotspot memory-lines=1;\
    \n/system logging action set hotspot memory-lines=1000;"
add name=backup owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    export compact file=auto_backup_user-manager;\r\
    \n/system backup save name=auto_backup_user-manager.backup;\r\
    \n:if ( [ /file find name=auto_backup_user-manager.umb ] != \"\" ) do={\r\
    \n/file remove auto_backup_user-manager.umb;\r\
    \n};\r\
    \n/tool user-manager database save name=auto_backup_user-manager;\r\
    \n/delay delay-time=60;\r\
    \n\r\
    \n\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Export Script Us\
    er Manager \".[ /system clock get date ].\" \".[ /system clock get time ])\
    \_file=auto_backup_user-manager.rsc;\r\
    \n/delay delay-time=60;\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Backup Config Us\
    er Manager \".[ /system clock get date ].\" \".[ /system clock get time ])\
    \_file=auto_backup_user-manager.backup;\r\
    \n/delay delay-time=60;\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Backup Database \
    User Manager \".[ /system clock get date ].\" \".[ /system clock get time \
    ]) file=auto_backup_user-manager.umb;\r\
    \n/delay delay-time=60;"
/tool e-mail
set address=smtp.gmail.com from=email@gmail.com password=\
    PassWord port=587 start-tls=yes user=email@gmail.com
/tool mac-server
set allowed-interface-list=local
/tool mac-server mac-winbox
set allowed-interface-list=local
/tool user-manager database
set db-path=flash/user-manager
/tool user-manager profile profile-limitation
add from-time=0s limitation=unlimited profile=hotspot till-time=23h59m59s \
    weekdays=sunday,monday,tuesday,wednesday,thursday,friday,saturday
/tool user-manager router
add coa-port=1700 customer=admin disabled=no ip-address=10.11.11.1 log=\
    auth-fail name=Mikrotik-Training.ru-Guest shared-secret=PassWord123! \
    use-coa=no
/tool user-manager user
add customer=admin disabled=no password=test121212313123132312 shared-users=1 \
    username=test wireless-enc-algo=none wireless-enc-key="" wireless-psk=""
add customer=admin disabled=no password=1879 phone=79067634683 shared-users=1 \
    username=9011111111 wireless-enc-algo=none wireless-enc-key="" \
    wireless-psk=""


File: /Hotspot + asterisk\Log-in script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-login 

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:local ipuser [/ip hotspot active get [find user=$user] address];

:local usermac [/ip hotspot active get [find user=$user] mac-address]

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5]; 

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:local mac1 [:pick $usermac 0 2];

:local mac2 [:pick $usermac 3 5];

:local mac3 [:pick $usermac 6 8];

:local mac4 [:pick $usermac 9 11];

:local mac5 [:pick $usermac 12 14];

:local mac6 [:pick $usermac 15 17];

:set $usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6})]

:put $time1

/ip firewall address-list add list=$today address="log-in.$time1.$user.$usermac.$ipuser"



do {/tool e-mail send to="email@gmail.com" subject="Login number: $user on $nas" body="Login number: $user mac-address: $usermac time: $time1 ip-address: $ipuser"} on-error={};


File: /Hotspot + asterisk\Log-out script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-logout

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5];

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:put $time1

/ip firewall address-list add list=$today address="log-out.$time1.$user"

/tool e-mail send to="email@gmail.com" subject="Logout number: $user on $nas" body="Logout number: $user time: $time1"

File: /Hotspot + asterisk\MGuide.php
<?php

use PEAR2\Net\RouterOS;
date_default_timezone_set('Europe/Moscow');

require_once 'config.php';
require_once 'includes/PEAR2_Net_RouterOS-1.0.0b6/src/PEAR2/Autoload.php';

if (!isset($argv[1]) || empty($argv[1]) || !is_numeric($argv[1])) die("No CallerID's found! Aborted!\n");

try {
        $client = new RouterOS\Client($arr_logon['ip_addr'], $arr_logon['login'], $arr_logon['pass']);
    }

    catch (Exception $e) {
        echo ('Unable to connect to the router with message: '.$e);
        return false;
    }

// Bring the string to the form
    $num = trim($argv[1]);
    $len = strlen($num);
    if ($len > 10) $num = substr($num, -10);
    
// Send Request
    $request = new RouterOS\Request('/ip/hotspot/user/add');
    $request->setArgument('name', $num);
    $request->setArgument('password', $num);

    $responses = $client->sendSync($request);

    //echo "Done!\n";
?>

File: /Hotspot + asterisk\script backup.txt
/export compact file=auto_backup_user-manager;
/system backup save name=auto_backup_user-manager.backup;
:if ( [ /file find name=auto_backup_user-manager.umb ] != "" ) do={
/file remove auto_backup_user-manager.umb;
};
/tool user-manager database save name=auto_backup_user-manager;
/delay delay-time=60;


/tool e-mail send to="email@gmail.com" subject=("Export Script User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.rsc;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Config User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.backup;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Database User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.umb;
/delay delay-time=60;

File: /Hotspot + asterisk\соглашение.txt
Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. 

Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других пользователей сети Интернет. 

Правила пользования Услугами

Принимаемые обозначения

"Исполнитель" - оператор ЗАО «Максима Телеком» 

"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие техническую возможность их получать. 
ООО "Компания"
1.При пользовании Услугами запрещается: 

1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании Услуг. 

1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. 

1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого не предназначенные. 

Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов или сообщений.

Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее ограничение никоим образом не имеет отношения к системе электронной подписки.

1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159 "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".

1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или иначе, противоречит российскому или международному праву.

1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие вредные компоненты.

1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения или другой продукции).

1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами Услуги также являются объектом авторских и других прав.

1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или владельцами этих ресурсов.

1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного Исполнителем.

1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом виде в рамках пользования Услуг.

Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно отказаться от его использования.

2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной почты (за исключением случаев, предусмотренных законом).

Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом, требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг, либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были или могут быть нарушены.

3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя, являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.

4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством Российской Федерации для отдельных категорий граждан.

© ООО "Компания", 2018

File: /Hotspot + asterisk + sms\asteriks dial.txt
[from-trunk-hotspot]
exten => 74951111111,1,NoOp(TEST Mikrotik AUTH)
same  => n,System("/usr/bin/ssh -oStrictHostKeyChecking=no admin@mikrotik-ip-or-dns-name /tool user-manager user add username=${CALLERID(num):-10:10} password=${CALLERID(num):-10:10} customer=admin copy-from=test disabled=no phone=${CALLERID(num):-10:10}")
same  => n,System("/usr/bin/ssh -oStrictHostKeyChecking=no admin@192.168.50.21 /tool user-manager user set password=${CALLERID(num):-10:10} number=[find username=${CALLERID(num):-10:10}]")
same  => n,Busy()
same  => n,Hangup()


File: /Hotspot + asterisk + sms\cpe.rsc
/interface bridge add admin-mac=C1:2D:E1:F9:11:11 auto-mac=no comment=Hotspot fast-forward=no name=bridge2
/ip hotspot profile set [ find default=yes ] hotspot-address=10.5.50.1 html-directory=flash/hotspot use-radius=yes
/ip hotspot profile add hotspot-address=10.5.50.1 html-directory=flash/hotspot http-cookie-lifetime=1h login-by=cookie,http-chap,http-pap,mac-cookie name=hsprof2 use-radius=yes
/ip hotspot user profile set [ find default=yes ] on-login=":local nas [/system identity get name];\r\
    \n\r\
    \n:local today [/system clock get date];\r\
    \n\r\
    \n:local time1 [/system clock get time ];\r\
    \n\r\
    \n:local ipuser [/ip hotspot active get [find user=\$user] address];\r\
    \n\r\
    \n:local usermac [/ip hotspot active get [find user=\$user] mac-address]\r\
    \n\r\
    \n:put \$today\r\
    \n\r\
    \n:put \$time1\r\
    \n\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n\r\
    \n:local min [:pick \$time1 3 5]; \r\
    \n\r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n\r\
    \n:local mac1 [:pick \$usermac 0 2];\r\
    \n\r\
    \n:local mac2 [:pick \$usermac 3 5];\r\
    \n\r\
    \n:local mac3 [:pick \$usermac 6 8];\r\
    \n\r\
    \n:local mac4 [:pick \$usermac 9 11];\r\
    \n\r\
    \n:local mac5 [:pick \$usermac 12 14];\r\
    \n\r\
    \n:local mac6 [:pick \$usermac 15 17];\r\
    \n\r\
    \n:set \$usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6})]\r\
    \n\r\
    \n:put \$time1\r\
    \n\r\
    \n/ip firewall address-list add list=\$today address=\"log-in.\$time1.\$user.\$usermac.\$ipuser\"\r\
    \n\r\
    \n\r\
    \n\r\
    \n#do {/tool e-mail send to=\"@gmail.com\" subject=\"Login number: \$user on \$nas\" body=\"Login number: \$user mac-address: \$usermac time: \$time1 ip-address: \$ipuser\"} on-error={};\r\
    \n" on-logout=":local nas [/system identity get name];\r\
    \n\r\
    \n:local today [/system clock get date];\r\
    \n\r\
    \n:local time1 [/system clock get time ];\r\
    \n\r\
    \n:put \$today\r\
    \n\r\
    \n:put \$time1\r\
    \n\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n\r\
    \n:local min [:pick \$time1 3 5];\r\
    \n\r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n\r\
    \n:put \$time1\r\
    \n\r\
    \n/ip firewall address-list add list=\$today address=\"log-out.\$time1.\$user\"\r\
    \n\r\
    \n#/tool e-mail send to=\"@gmail.com\" subject=\"Logout number: \$user on \$nas\" body=\"Logout number: \$user time: \$time1\""
/ip pool add name=hs-pool-5 ranges=10.5.50.2-10.5.50.254
/ip dhcp-server add address-pool=hs-pool-5 disabled=no interface=bridge2 lease-time=1h name=dhcp1
/interface bridge port add bridge=bridge2 interface=wlan1
/ip address add address=10.5.50.1/24 comment="hotspot network" interface=bridge2 network=10.5.54.0
/ip dhcp-server network add address=10.5.50.0/24 comment="hotspot network" gateway=10.5.50.1
/ip dns set allow-remote-requests=yes servers=8.8.8.8,1.1.1.1
/radius add address=10.1.1.2 secret=PassWord123 service=hotspot src-address=10.1.1.1
/radius incoming set accept=yes


File: /Hotspot + asterisk + sms\hotspot\.idea\mikrotik.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$" />
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>

File: /Hotspot + asterisk + sms\hotspot\.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /Hotspot + asterisk + sms\hotspot\.idea\workspace.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ChangeListManager">
    <list default="true" id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
    <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />
    <option name="TRACKING_ENABLED" value="true" />
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="FileEditorManager">
    <leaf SIDE_TABS_SIZE_LIMIT_KEY="300">
      <file leaf-file-name="login.html" pinned="false" current-in-tab="true">
        <entry file="file://$PROJECT_DIR$/login.html">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="239">
              <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
              <folding>
                <element signature="e#1605#1819#0" expanded="false" />
                <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
              </folding>
            </state>
          </provider>
        </entry>
      </file>
      <file leaf-file-name="form.css" pinned="false" current-in-tab="false">
        <entry file="file://$PROJECT_DIR$/css/form.css">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="135">
              <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
              <folding />
            </state>
          </provider>
        </entry>
      </file>
    </leaf>
  </component>
  <component name="FileTemplateManagerImpl">
    <option name="RECENT_TEMPLATES">
      <list>
        <option value="CSS File" />
        <option value="HTML File" />
      </list>
    </option>
  </component>
  <component name="FindInProjectRecents">
    <findStrings>
      <find>wid</find>
    </findStrings>
  </component>
  <component name="GradleLocalSettings">
    <option name="externalProjectsViewState">
      <projects_view />
    </option>
  </component>
  <component name="IdeDocumentHistory">
    <option name="CHANGED_PATHS">
      <list>
        <option value="$PROJECT_DIR$/css.css" />
        <option value="$PROJECT_DIR$/img/arrow.svg" />
        <option value="$PROJECT_DIR$/img/number.svg" />
        <option value="$PROJECT_DIR$/css/form.css" />
        <option value="$PROJECT_DIR$/index.html" />
        <option value="$PROJECT_DIR$/login.html" />
      </list>
    </option>
  </component>
  <component name="JsBuildToolGruntFileManager" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsBuildToolPackageJson" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsGulpfileManager">
    <detection-done>true</detection-done>
    <sorting>DEFINITION_ORDER</sorting>
  </component>
  <component name="PhpWorkspaceProjectConfiguration" backward_compatibility_performed="true" />
  <component name="ProjectFrameBounds">
    <option name="x" value="248" />
    <option name="y" value="22" />
    <option name="width" value="949" />
    <option name="height" value="731" />
  </component>
  <component name="ProjectInspectionProfilesVisibleTreeState">
    <entry key="Project Default">
      <profile-state>
        <expanded-state>
          <State>
            <id />
          </State>
          <State>
            <id>Abstraction issuesJava</id>
          </State>
          <State>
            <id>ActionScript specificJavaScript</id>
          </State>
          <State>
            <id>Android</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Accessibility</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Chrome OS</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Messages</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization &gt; Bidirectional Text</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Lint</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Performance</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Security</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Icons</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Typography</id>
          </State>
          <State>
            <id>Android Lint for Kotlin</id>
          </State>
          <State>
            <id>Ant inspections</id>
          </State>
          <State>
            <id>Application Server Specific Inspections</id>
          </State>
          <State>
            <id>ArquillianJava</id>
          </State>
          <State>
            <id>BashSupport</id>
          </State>
          <State>
            <id>Batch Applications Issues</id>
          </State>
          <State>
            <id>Bean Validation issues</id>
          </State>
          <State>
            <id>CDI(Contexts and Dependency Injection) issues</id>
          </State>
          <State>
            <id>CSS</id>
          </State>
          <State>
            <id>Class metricsJava</id>
          </State>
          <State>
            <id>Class structureJava</id>
          </State>
          <State>
            <id>Cloning issuesJava</id>
          </State>
          <State>
            <id>Code SmellPHP</id>
          </State>
          <State>
            <id>Code StylePHP</id>
          </State>
          <State>
            <id>Code quality toolsCSS</id>
          </State>
          <State>
            <id>Code quality toolsJavaScript</id>
          </State>
          <State>
            <id>Code style issuesGo</id>
          </State>
          <State>
            <id>Code style issuesJava</id>
          </State>
          <State>
            <id>Code style issuesJavaScript</id>
          </State>
          <State>
            <id>CodeSpring CoreSpring</id>
          </State>
          <State>
            <id>CoffeeScript</id>
          </State>
          <State>
            <id>Control flow issuesGroovy</id>
          </State>
          <State>
            <id>Control flow issuesJava</id>
          </State>
          <State>
            <id>Control flow issuesJavaScript</id>
          </State>
          <State>
            <id>CorrectnessLintAndroid</id>
          </State>
          <State>
            <id>Cucumber Java</id>
          </State>
          <State>
            <id>DOM issuesJavaScript</id>
          </State>
          <State>
            <id>Data flow issuesJava</id>
          </State>
          <State>
            <id>Data flow issuesJavaScript</id>
          </State>
          <State>
            <id>Declaration redundancyGo</id>
          </State>
          <State>
            <id>Declaration redundancyJava</id>
          </State>
          <State>
            <id>Dependency issuesJava</id>
          </State>
          <State>
            <id>Encapsulation issuesJava</id>
          </State>
          <State>
            <id>Error handlingGroovy</id>
          </State>
          <State>
            <id>Error handlingJava</id>
          </State>
          <State>
            <id>Error handlingJavaScript</id>
          </State>
          <State>
            <id>Error handlingPHP</id>
          </State>
          <State>
            <id>Finalization issuesJava</id>
          </State>
          <State>
            <id>FlexUnit inspections</id>
          </State>
          <State>
            <id>GPathGroovy</id>
          </State>
          <State>
            <id>General</id>
          </State>
          <State>
            <id>GeneralGo</id>
          </State>
          <State>
            <id>GeneralJavaScript</id>
          </State>
          <State>
            <id>GeneralPHP</id>
          </State>
          <State>
            <id>Go</id>
          </State>
          <State>
            <id>Google App Engine</id>
          </State>
          <State>
            <id>Google Web Toolkit issues</id>
          </State>
          <State>
            <id>GrailsGroovy</id>
          </State>
          <State>
            <id>Groovy</id>
          </State>
          <State>
            <id>Guice Inspections</id>
          </State>
          <State>
            <id>HTML</id>
          </State>
          <State>
            <id>Haml</id>
          </State>
          <State>
            <id>Ignore</id>
          </State>
          <State>
            <id>Inheritance issuesJava</id>
          </State>
          <State>
            <id>Initialization issuesJava</id>
          </State>
          <State>
            <id>Internationalization issues</id>
          </State>
          <State>
            <id>Internationalization issuesJava</id>
          </State>
          <State>
            <id>Invalid elementsCSS</id>
          </State>
          <State>
            <id>J2ME issuesJava</id>
          </State>
          <State>
            <id>JBoss Seam issues</id>
          </State>
          <State>
            <id>JPA issues</id>
          </State>
          <State>
            <id>JSON</id>
          </State>
          <State>
            <id>JSP Inspections</id>
          </State>
          <State>
            <id>JUnit issuesJava</id>
          </State>
          <State>
            <id>Java</id>
          </State>
          <State>
            <id>Java 5Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 7Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 8Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 9Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java EE issues</id>
          </State>
          <State>
            <id>Java interop issuesKotlin</id>
          </State>
          <State>
            <id>Java language level migration aidsJava</id>
          </State>
          <State>
            <id>JavaScript</id>
          </State>
          <State>
            <id>JavaScript validity issuesJavaScript</id>
          </State>
          <State>
            <id>Javadoc issuesJava</id>
          </State>
          <State>
            <id>Kotlin</id>
          </State>
          <State>
            <id>Kotlin Android</id>
          </State>
          <State>
            <id>Language Injection</id>
          </State>
          <State>
            <id>LintAndroid</id>
          </State>
          <State>
            <id>Logging issuesJava</id>
          </State>
          <State>
            <id>Manifest</id>
          </State>
          <State>
            <id>Maven</id>
          </State>
          <State>
            <id>Memory issuesJava</id>
          </State>
          <State>
            <id>Method metricsGroovy</id>
          </State>
          <State>
            <id>Modularization issuesJava</id>
          </State>
          <State>
            <id>Naming conventionsGroovy</id>
          </State>
          <State>
            <id>Naming conventionsJava</id>
          </State>
          <State>
            <id>Naming conventionsKotlin</id>
          </State>
          <State>
            <id>Node.jsJavaScript</id>
          </State>
          <State>
            <id>Numeric issuesJava</id>
          </State>
          <State>
            <id>OSGi</id>
          </State>
          <State>
            <id>Other problemsKotlin</id>
          </State>
          <State>
            <id>PHP</id>
          </State>
          <State>
            <id>Pattern Validation</id>
          </State>
          <State>
            <id>Performance issuesJava</id>
          </State>
          <State>
            <id>Plugin DevKit</id>
          </State>
          <State>
            <id>Portability issuesJava</id>
          </State>
          <State>
            <id>Potentially confusing code constructsGroovy</id>
          </State>
          <State>
            <id>Potentially confusing code constructsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsCSS</id>
          </State>
          <State>
            <id>Probable bugsCoffeeScript</id>
          </State>
          <State>
            <id>Probable bugsGo</id>
          </State>
          <State>
            <id>Probable bugsJava</id>
          </State>
          <State>
            <id>Probable bugsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsKotlin</id>
          </State>
          <State>
            <id>Probable bugsPHP</id>
          </State>
          <State>
            <id>Properties Files</id>
          </State>
          <State>
            <id>Properties FilesJava</id>
          </State>
          <State>
            <id>RESTful Web Service</id>
          </State>
          <State>
            <id>Redundant constructsKotlin</id>
          </State>
          <State>
            <id>RegExp</id>
          </State>
          <State>
            <id>SQL</id>
          </State>
          <State>
            <id>Security issuesJava</id>
          </State>
          <State>
            <id>Serialization issuesJava</id>
          </State>
          <State>
            <id>SetupSpring CoreSpring</id>
          </State>
          <State>
            <id>Spelling</id>
          </State>
          <State>
            <id>Spring</id>
          </State>
          <State>
            <id>Spring BootSpring</id>
          </State>
          <State>
            <id>Spring CoreSpring</id>
          </State>
          <State>
            <id>Spring DataSpring</id>
          </State>
          <State>
            <id>Spring OSGiSpring</id>
          </State>
          <State>
            <id>Struts</id>
          </State>
          <State>
            <id>Struts 1Struts</id>
          </State>
          <State>
            <id>Struts 2Struts</id>
          </State>
          <State>
            <id>Style issuesKotlin</id>
          </State>
          <State>
            <id>StyleGroovy</id>
          </State>
          <State>
            <id>TestNGJava</id>
          </State>
          <State>
            <id>Threading issuesGroovy</id>
          </State>
          <State>
            <id>Threading issuesJava</id>
          </State>
          <State>
            <id>Thymeleaf</id>
          </State>
          <State>
            <id>Type compatibilityPHP</id>
          </State>
          <State>
            <id>TypeScript</id>
          </State>
          <State>
            <id>UI Form Problems</id>
          </State>
          <State>
            <id>UndefinedPHP</id>
          </State>
          <State>
            <id>Validity issuesGroovy</id>
          </State>
          <State>
            <id>Visibility issuesJava</id>
          </State>
          <State>
            <id>Web Services</id>
          </State>
          <State>
            <id>WebSocket issues</id>
          </State>
          <State>
            <id>XML</id>
          </State>
          <State>
            <id>XMLSpring CoreSpring</id>
          </State>
          <State>
            <id>XPath</id>
          </State>
        </expanded-state>
      </profile-state>
    </entry>
  </component>
  <component name="ProjectView">
    <navigator currentView="ProjectPane" proportions="" version="1">
      <flattenPackages />
      <showMembers />
      <showModules />
      <showLibraryContents />
      <hideEmptyPackages />
      <abbreviatePackageNames />
      <autoscrollToSource />
      <autoscrollFromSource />
      <sortByType />
      <manualOrder />
      <foldersAlwaysOnTop value="true" />
    </navigator>
    <panes>
      <pane id="Scratches" />
      <pane id="PackagesPane" />
      <pane id="ProjectPane">
        <subPane>
          <expand>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
            </path>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
              <item name="img" type="462c0819:PsiDirectoryNode" />
            </path>
          </expand>
          <select />
        </subPane>
      </pane>
      <pane id="AndroidView" />
      <pane id="Scope" />
    </panes>
  </component>
  <component name="PropertiesComponent">
    <property name="nodejs_interpreter_path.stuck_in_default_project" value="undefined stuck path" />
    <property name="settings.editor.selected.configurable" value="editor.preferences.fonts.default" />
    <property name="WebServerToolWindowFactoryState" value="false" />
    <property name="aspect.path.notification.shown" value="true" />
    <property name="last_opened_file_path" value="$PROJECT_DIR$" />
    <property name="list.type.of.created.stylesheet" value="CSS" />
    <property name="DefaultHtmlFileTemplate" value="HTML File" />
  </component>
  <component name="RecentsManager">
    <key name="MoveFile.RECENT_KEYS">
      <recent name="$PROJECT_DIR$/js" />
      <recent name="$PROJECT_DIR$/img" />
    </key>
  </component>
  <component name="RunDashboard">
    <option name="ruleStates">
      <list>
        <RuleState>
          <option name="name" value="ConfigurationTypeDashboardGroupingRule" />
        </RuleState>
        <RuleState>
          <option name="name" value="StatusDashboardGroupingRule" />
        </RuleState>
      </list>
    </option>
  </component>
  <component name="RunManager">
    <configuration default="true" type="Applet" factoryName="Applet">
      <option name="HTML_USED" value="false" />
      <option name="WIDTH" value="400" />
      <option name="HEIGHT" value="300" />
      <option name="POLICY_FILE" value="$APPLICATION_HOME_DIR$/bin/appletviewer.policy" />
      <module />
    </configuration>
    <configuration default="true" type="Application" factoryName="Application">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <option name="MAIN_CLASS_NAME" />
      <option name="VM_PARAMETERS" />
      <option name="PROGRAM_PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="ENABLE_SWING_INSPECTOR" value="false" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <module name="" />
      <envs />
    </configuration>
    <configuration default="true" type="JUnit" factoryName="JUnit">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="TEST_OBJECT" value="class" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <envs />
      <patterns />
    </configuration>
    <configuration name="login_old.html" type="JavascriptDebugType" factoryName="JavaScript Debug" temporary="true" nameIsGenerated="true" uri="http://localhost:63343/mikrotik/login_old.html" />
    <configuration default="true" type="Remote" factoryName="Remote">
      <option name="USE_SOCKET_TRANSPORT" value="true" />
      <option name="SERVER_MODE" value="false" />
      <option name="SHMEM_ADDRESS" value="javadebug" />
      <option name="HOST" value="localhost" />
      <option name="PORT" value="5005" />
    </configuration>
    <configuration default="true" type="TestNG" factoryName="TestNG">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="SUITE_NAME" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="GROUP_NAME" />
      <option name="TEST_OBJECT" value="CLASS" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="OUTPUT_DIRECTORY" />
      <option name="ANNOTATION_TYPE" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <option name="USE_DEFAULT_REPORTERS" value="false" />
      <option name="PROPERTIES_FILE" />
      <envs />
      <properties />
      <listeners />
    </configuration>
    <configuration default="true" type="#org.jetbrains.idea.devkit.run.PluginConfigurationType" factoryName="Plugin">
      <module name="" />
      <option name="VM_PARAMETERS" value="-Xmx512m -Xms256m -XX:MaxPermSize=250m -ea" />
      <option name="PROGRAM_PARAMETERS" />
      <predefined_log_file id="idea.log" enabled="true" />
    </configuration>
    <recent_temporary>
      <list size="1">
        <item index="0" class="java.lang.String" itemvalue="JavaScript Debug.login_old.html" />
      </list>
    </recent_temporary>
  </component>
  <component name="ShelveChangesManager" show_recycled="false">
    <option name="remove_strategy" value="false" />
  </component>
  <component name="SvnConfiguration">
    <configuration />
  </component>
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
      <created>1521018748772</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1521018748772</updated>
      <workItem from="1521018751184" duration="14087000" />
      <workItem from="1521057296181" duration="563000" />
      <workItem from="1521058090953" duration="1147000" />
      <workItem from="1521059914099" duration="565000" />
    </task>
    <servers />
  </component>
  <component name="TimeTrackingManager">
    <option name="totallyTimeSpent" value="16362000" />
  </component>
  <component name="ToolWindowManager">
    <frame x="248" y="22" width="949" height="731" extended-state="0" />
    <editor active="true" />
    <layout>
      <window_info id="Palette" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />
      <window_info id="Palette&#9;" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Image Layers" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Analysis" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="true" content_ui="tabs" />
      <window_info id="Maven Projects" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Run" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="false" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Tool" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.26571113" sideWeight="0.5" order="0" side_tool="false" content_ui="combo" />
      <window_info id="Docker" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Database" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Learn" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="Ant Build" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="UI Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Theme Preview" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.39937106" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="true" content_ui="tabs" />
      <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />
      <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Commander" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Hierarchy" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="combo" />
      <window_info id="Inspection" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="5" side_tool="false" content_ui="tabs" />
      <window_info id="Find" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
    </layout>
  </component>
  <component name="TypeScriptGeneratedFilesManager">
    <option name="version" value="1" />
  </component>
  <component name="VcsContentAnnotationSettings">
    <option name="myLimit" value="2678400000" />
  </component>
  <component name="XDebuggerManager">
    <breakpoint-manager>
      <option name="time" value="1" />
    </breakpoint-manager>
    <watches-manager />
  </component>
  <component name="editorHistoryManager">
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css.css" />
    <entry file="file://$PROJECT_DIR$/img/arrow.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/number.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/integrasky.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$APPLICATION_HOME_DIR$/plugins/JavaScriptLanguage/jsLanguageServicesImpl/external/lib.dom.d.ts">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="119">
          <caret line="12227" column="4" lean-forward="false" selection-start-line="12227" selection-start-column="4" selection-end-line="12227" selection-end-column="4" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login_old.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="-545">
          <caret line="71" column="9" lean-forward="true" selection-start-line="60" selection-start-column="0" selection-end-line="71" selection-end-column="9" />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="239">
          <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
  </component>
  <component name="masterDetails">
    <states>
      <state key="ProjectJDKs.UI">
        <settings>
          <last-edited>ruby-2.5.0-p0</last-edited>
          <splitter-proportions>
            <option name="proportions">
              <list>
                <option value="0.2" />
              </list>
            </option>
          </splitter-proportions>
        </settings>
      </state>
    </states>
  </component>
</project>

File: /Hotspot + asterisk + sms\hotspot\alogin.html
<html>
<head>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > redirect</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = unescape('$(link-redirect-esc)');
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	You are logged in
	<br><br>
	If nothing happens, click <a href="$(link-redirect)">here</a></td>
</tr>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\by_call\css\form.css
html, body {
    background: url("../img/background.png");
    height: 100%;
    min-height: 100px;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.logo {
    margin-bottom: 42px;
}

label {
    font-size: 12px;
    font-family: "Opium";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    background: #fff;
    border: solid 1px rgb(220, 224, 226);
    border-radius: 15px;
    padding: 42px;

}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    background-color: rgb(237, 245, 255);
    border: none;
    padding: 17px;
    margin: 7px;
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

.code input[type="text"], .form.already input[type="text"]{
    text-align: center !important;
}

.btn {

    font-size: 12px;
    font-family: "Roboto";
    color: rgb(255, 255, 255);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;

    border-radius: 5px;
    border: none;
    background-color: rgb(77, 161, 255);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;

    margin: 0 auto;

}

.disabled, .disabled:hover{
    background: #eee !important;
    cursor: auto;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.form_description {
    font-size: 16px;
    font-family: "Opium";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_group img {
    margin-right: 14px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: #0421EA !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk + sms\hotspot\by_call\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot + asterisk + sms\hotspot\by_call\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="IntegraSky - team@integrasky.ru">

    <link rel="stylesheet" href="../css/form.css">
    <link rel="stylesheet" href="../css/modal.css">

    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>

        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }

        jQuery(document).ready(function () {

            jQuery('#login').mask('+7-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');
                    jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    //jQuery('#login_form').attr('action', '#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));

                    jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, '') + 'd');
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            /*CHANGE*/

            //alert(jQuery('#login').height);

            jQuery('#login2').mask('+7-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {

                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {

                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));


            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 3)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 3) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });
            /*END_CHANGE*/

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }
            });

            jQuery('#code').on('keyup', function (event) {

                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 3) {
                    jQuery(this).addClass('disabled').removeClass('active');
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                }
            });

            jQuery('#has_code').on('click', function () {
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500)
                });
            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }
        });

    function Connect()
    {
        jQuery('#code').val(document.getElementById('username2').value);
        jQuery('#password').val(hexMD5('$(chap-id)' + jQuery('#code').val() + '$(chap-challenge)'));
        return jQuery('.code .btn.active').click();
    }

    </script>
</head>
<body>
<div class="container">
<div>
    <div class="logo">
        <img src="../img/integrasky.svg" alt="IntegraSky" width="350px" style="width:350px">
    </div>
    <!--<small class="form_description">Please log on to use the internet hotspot service</small>-->
    <form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="$(link-login-only)" method="post">
    <!--<form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="" method="post">-->
        <p class='upper-label' id='text-phone'>Для подключения к бесплатному WiFi введите номер телефона</p>
        <!--<label for="login">Введите номер</label>-->
        <div class="input_group tel">
            <img src="../img/phone.png" alt="number">
            <input type="hidden" name="username" id="username1">
            <!--<input type="text" class='round-corner' id="login" placeholder="+7-(XXX)-XXX-XX-XX">-->
            <input type="text" class='round-right-corner phone' id="login" placeholder="+7....">
        </div>
        <br>
        <button class="btn next round-corner disabled">
            Отправить
        </button>
    </form>

    <form class="form code" style="display: none" name="sendin" action="" method="post">
        <!--<label for="code">Введите код</label>-->
        <!--<label for="code">Для получения доступа необходимо позвонить на номер <a href="tel:84991111111">84991111111</a></label>-->
        <p class='upper-label'>Для получения доступа необходимо позвонить на номер <a class="phone_to_call" href="tel:84991111111">84991111111</a></p>
        <div class="input_group">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <!--<input type="text" id="code" maxlength="16" placeholder="********">-->
            <input type="hidden" id="code">
        </div>
        <input type="submit" class="btn" value="Далее" onclick="Connect()" />
    </form>

    <form class="form already" style="display: none" name="sendin" action="" method="post">
        <p class='upper-label'>Введите номер</p>
        <div class="input_group tel">
            <img src="../img/phone.png" alt="number">
            <input type="text" class='round-right-corner phone' id="login2" placeholder="+7....">
        </div>
        <p class='upper-label'>Введите код</p>
        <div class="input_group">
            <img src="../img/key.png" alt="number">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" class='round-right-corner code' id="code2" maxlength="8">
        </div>
        <br />
        <input type="submit" class="btn disabled" value="Отправить">
    </form>

    <br>

    <div class="input_group bottom_btn_group">
    	<button class="bottom-btn round-corner redirect" onclick="window.location.href='../login.html'">Авторизация<br />по SMS</button>
    	<button id="has_code" class="bottom-btn round-corner">У меня<br />есть код</button>
    </div>

    <label id="modal_trigger" for="modal-trigger">Политика конфиденциальности</label> <!--class="bottom-btn round-corner"-->

</div>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\by_call\login_old.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>internet hotspot > login</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="pragma" content="no-cache"/>
    <meta http-equiv="expires" content="-1"/>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>

    <link rel="stylesheet" href="./css/form.css">

    <style type="text/css">
        body {
            color: #737373;
            font-size: 10px;
            font-family: verdana;
        }

        textarea, input, select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active {
            color: #AAAAAA;
            text-decoration: none;
            font-size: 10px;
        }

        a:hover {
            border-bottom: 1px dotted #c1c1c1;
            color: #AAAAAA;
        }

        img {
            border: none;
        }

        td {
            font-size: 14px;
            color: #7A7A7A;
        }
    </style>

</head>

<body>
$(if chap-id)
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username"/>
    <input type="hidden" name="password"/>
    <input type="hidden" name="dst" value="$(link-orig)"/>
    <input type="hidden" name="popup" value="true"/>
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    <!--
    function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
        document.sendin.submit();
        return false;
    }

    //-->
</script>
$(endif)

<div align="center">
    <a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <!--<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br/>$(if-->
                <!--trial == 'yes')Free trial available, <a style="color: #FF8080"-->
                                                        <!--href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click-->
                    <!--here</a>.$(endif)-->
            <!--</div>-->
            <div>
                <small>Please log on to use the internet hotspot service</small>
            </div>
            <br/>
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0"
                   cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form name="login" action="$(link-login-only)" method="post"
                              $(if chap-id) onSubmit="return doLogin()" $(endif)>
                            <input type="hidden" name="dst" value="$(link-orig)"/>
                            <input type="hidden" name="popup" value="true"/>

                            <table width="100" style="background-color: #ffffff">
                                <tr>
                                    <td align="right">login</td>
                                    <td><input style="width: 80px" name="username" type="text" value="$(username)"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right">password</td>
                                    <td><input style="width: 80px" name="password" type="password"/></td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                    <td><input type="submit" value="OK"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr>
                    <td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img
                            src="/img/logobottom.png" alt="mikrotik"/></a></td>
                </tr>
            </table>

            <br/>
            <div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            $(if error)<br/>
            <div style="color: #FF8080; font-size: 9px">$(error)</div>
            $(endif)
        </td>
    </tr>
</table>

<script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
</script>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\by_sms\.idea\mikrotik.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$" />
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>

File: /Hotspot + asterisk + sms\hotspot\by_sms\.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /Hotspot + asterisk + sms\hotspot\by_sms\.idea\workspace.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ChangeListManager">
    <list default="true" id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
    <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />
    <option name="TRACKING_ENABLED" value="true" />
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="FileEditorManager">
    <leaf SIDE_TABS_SIZE_LIMIT_KEY="300">
      <file leaf-file-name="login.html" pinned="false" current-in-tab="true">
        <entry file="file://$PROJECT_DIR$/login.html">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="239">
              <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
              <folding>
                <element signature="e#1605#1819#0" expanded="false" />
                <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
              </folding>
            </state>
          </provider>
        </entry>
      </file>
      <file leaf-file-name="form.css" pinned="false" current-in-tab="false">
        <entry file="file://$PROJECT_DIR$/css/form.css">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="135">
              <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
              <folding />
            </state>
          </provider>
        </entry>
      </file>
    </leaf>
  </component>
  <component name="FileTemplateManagerImpl">
    <option name="RECENT_TEMPLATES">
      <list>
        <option value="CSS File" />
        <option value="HTML File" />
      </list>
    </option>
  </component>
  <component name="FindInProjectRecents">
    <findStrings>
      <find>wid</find>
    </findStrings>
  </component>
  <component name="GradleLocalSettings">
    <option name="externalProjectsViewState">
      <projects_view />
    </option>
  </component>
  <component name="IdeDocumentHistory">
    <option name="CHANGED_PATHS">
      <list>
        <option value="$PROJECT_DIR$/css.css" />
        <option value="$PROJECT_DIR$/img/arrow.svg" />
        <option value="$PROJECT_DIR$/img/number.svg" />
        <option value="$PROJECT_DIR$/css/form.css" />
        <option value="$PROJECT_DIR$/index.html" />
        <option value="$PROJECT_DIR$/login.html" />
      </list>
    </option>
  </component>
  <component name="JsBuildToolGruntFileManager" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsBuildToolPackageJson" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsGulpfileManager">
    <detection-done>true</detection-done>
    <sorting>DEFINITION_ORDER</sorting>
  </component>
  <component name="PhpWorkspaceProjectConfiguration" backward_compatibility_performed="true" />
  <component name="ProjectFrameBounds">
    <option name="x" value="248" />
    <option name="y" value="22" />
    <option name="width" value="949" />
    <option name="height" value="731" />
  </component>
  <component name="ProjectInspectionProfilesVisibleTreeState">
    <entry key="Project Default">
      <profile-state>
        <expanded-state>
          <State>
            <id />
          </State>
          <State>
            <id>Abstraction issuesJava</id>
          </State>
          <State>
            <id>ActionScript specificJavaScript</id>
          </State>
          <State>
            <id>Android</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Accessibility</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Chrome OS</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Messages</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization &gt; Bidirectional Text</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Lint</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Performance</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Security</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Icons</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Typography</id>
          </State>
          <State>
            <id>Android Lint for Kotlin</id>
          </State>
          <State>
            <id>Ant inspections</id>
          </State>
          <State>
            <id>Application Server Specific Inspections</id>
          </State>
          <State>
            <id>ArquillianJava</id>
          </State>
          <State>
            <id>BashSupport</id>
          </State>
          <State>
            <id>Batch Applications Issues</id>
          </State>
          <State>
            <id>Bean Validation issues</id>
          </State>
          <State>
            <id>CDI(Contexts and Dependency Injection) issues</id>
          </State>
          <State>
            <id>CSS</id>
          </State>
          <State>
            <id>Class metricsJava</id>
          </State>
          <State>
            <id>Class structureJava</id>
          </State>
          <State>
            <id>Cloning issuesJava</id>
          </State>
          <State>
            <id>Code SmellPHP</id>
          </State>
          <State>
            <id>Code StylePHP</id>
          </State>
          <State>
            <id>Code quality toolsCSS</id>
          </State>
          <State>
            <id>Code quality toolsJavaScript</id>
          </State>
          <State>
            <id>Code style issuesGo</id>
          </State>
          <State>
            <id>Code style issuesJava</id>
          </State>
          <State>
            <id>Code style issuesJavaScript</id>
          </State>
          <State>
            <id>CodeSpring CoreSpring</id>
          </State>
          <State>
            <id>CoffeeScript</id>
          </State>
          <State>
            <id>Control flow issuesGroovy</id>
          </State>
          <State>
            <id>Control flow issuesJava</id>
          </State>
          <State>
            <id>Control flow issuesJavaScript</id>
          </State>
          <State>
            <id>CorrectnessLintAndroid</id>
          </State>
          <State>
            <id>Cucumber Java</id>
          </State>
          <State>
            <id>DOM issuesJavaScript</id>
          </State>
          <State>
            <id>Data flow issuesJava</id>
          </State>
          <State>
            <id>Data flow issuesJavaScript</id>
          </State>
          <State>
            <id>Declaration redundancyGo</id>
          </State>
          <State>
            <id>Declaration redundancyJava</id>
          </State>
          <State>
            <id>Dependency issuesJava</id>
          </State>
          <State>
            <id>Encapsulation issuesJava</id>
          </State>
          <State>
            <id>Error handlingGroovy</id>
          </State>
          <State>
            <id>Error handlingJava</id>
          </State>
          <State>
            <id>Error handlingJavaScript</id>
          </State>
          <State>
            <id>Error handlingPHP</id>
          </State>
          <State>
            <id>Finalization issuesJava</id>
          </State>
          <State>
            <id>FlexUnit inspections</id>
          </State>
          <State>
            <id>GPathGroovy</id>
          </State>
          <State>
            <id>General</id>
          </State>
          <State>
            <id>GeneralGo</id>
          </State>
          <State>
            <id>GeneralJavaScript</id>
          </State>
          <State>
            <id>GeneralPHP</id>
          </State>
          <State>
            <id>Go</id>
          </State>
          <State>
            <id>Google App Engine</id>
          </State>
          <State>
            <id>Google Web Toolkit issues</id>
          </State>
          <State>
            <id>GrailsGroovy</id>
          </State>
          <State>
            <id>Groovy</id>
          </State>
          <State>
            <id>Guice Inspections</id>
          </State>
          <State>
            <id>HTML</id>
          </State>
          <State>
            <id>Haml</id>
          </State>
          <State>
            <id>Ignore</id>
          </State>
          <State>
            <id>Inheritance issuesJava</id>
          </State>
          <State>
            <id>Initialization issuesJava</id>
          </State>
          <State>
            <id>Internationalization issues</id>
          </State>
          <State>
            <id>Internationalization issuesJava</id>
          </State>
          <State>
            <id>Invalid elementsCSS</id>
          </State>
          <State>
            <id>J2ME issuesJava</id>
          </State>
          <State>
            <id>JBoss Seam issues</id>
          </State>
          <State>
            <id>JPA issues</id>
          </State>
          <State>
            <id>JSON</id>
          </State>
          <State>
            <id>JSP Inspections</id>
          </State>
          <State>
            <id>JUnit issuesJava</id>
          </State>
          <State>
            <id>Java</id>
          </State>
          <State>
            <id>Java 5Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 7Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 8Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 9Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java EE issues</id>
          </State>
          <State>
            <id>Java interop issuesKotlin</id>
          </State>
          <State>
            <id>Java language level migration aidsJava</id>
          </State>
          <State>
            <id>JavaScript</id>
          </State>
          <State>
            <id>JavaScript validity issuesJavaScript</id>
          </State>
          <State>
            <id>Javadoc issuesJava</id>
          </State>
          <State>
            <id>Kotlin</id>
          </State>
          <State>
            <id>Kotlin Android</id>
          </State>
          <State>
            <id>Language Injection</id>
          </State>
          <State>
            <id>LintAndroid</id>
          </State>
          <State>
            <id>Logging issuesJava</id>
          </State>
          <State>
            <id>Manifest</id>
          </State>
          <State>
            <id>Maven</id>
          </State>
          <State>
            <id>Memory issuesJava</id>
          </State>
          <State>
            <id>Method metricsGroovy</id>
          </State>
          <State>
            <id>Modularization issuesJava</id>
          </State>
          <State>
            <id>Naming conventionsGroovy</id>
          </State>
          <State>
            <id>Naming conventionsJava</id>
          </State>
          <State>
            <id>Naming conventionsKotlin</id>
          </State>
          <State>
            <id>Node.jsJavaScript</id>
          </State>
          <State>
            <id>Numeric issuesJava</id>
          </State>
          <State>
            <id>OSGi</id>
          </State>
          <State>
            <id>Other problemsKotlin</id>
          </State>
          <State>
            <id>PHP</id>
          </State>
          <State>
            <id>Pattern Validation</id>
          </State>
          <State>
            <id>Performance issuesJava</id>
          </State>
          <State>
            <id>Plugin DevKit</id>
          </State>
          <State>
            <id>Portability issuesJava</id>
          </State>
          <State>
            <id>Potentially confusing code constructsGroovy</id>
          </State>
          <State>
            <id>Potentially confusing code constructsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsCSS</id>
          </State>
          <State>
            <id>Probable bugsCoffeeScript</id>
          </State>
          <State>
            <id>Probable bugsGo</id>
          </State>
          <State>
            <id>Probable bugsJava</id>
          </State>
          <State>
            <id>Probable bugsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsKotlin</id>
          </State>
          <State>
            <id>Probable bugsPHP</id>
          </State>
          <State>
            <id>Properties Files</id>
          </State>
          <State>
            <id>Properties FilesJava</id>
          </State>
          <State>
            <id>RESTful Web Service</id>
          </State>
          <State>
            <id>Redundant constructsKotlin</id>
          </State>
          <State>
            <id>RegExp</id>
          </State>
          <State>
            <id>SQL</id>
          </State>
          <State>
            <id>Security issuesJava</id>
          </State>
          <State>
            <id>Serialization issuesJava</id>
          </State>
          <State>
            <id>SetupSpring CoreSpring</id>
          </State>
          <State>
            <id>Spelling</id>
          </State>
          <State>
            <id>Spring</id>
          </State>
          <State>
            <id>Spring BootSpring</id>
          </State>
          <State>
            <id>Spring CoreSpring</id>
          </State>
          <State>
            <id>Spring DataSpring</id>
          </State>
          <State>
            <id>Spring OSGiSpring</id>
          </State>
          <State>
            <id>Struts</id>
          </State>
          <State>
            <id>Struts 1Struts</id>
          </State>
          <State>
            <id>Struts 2Struts</id>
          </State>
          <State>
            <id>Style issuesKotlin</id>
          </State>
          <State>
            <id>StyleGroovy</id>
          </State>
          <State>
            <id>TestNGJava</id>
          </State>
          <State>
            <id>Threading issuesGroovy</id>
          </State>
          <State>
            <id>Threading issuesJava</id>
          </State>
          <State>
            <id>Thymeleaf</id>
          </State>
          <State>
            <id>Type compatibilityPHP</id>
          </State>
          <State>
            <id>TypeScript</id>
          </State>
          <State>
            <id>UI Form Problems</id>
          </State>
          <State>
            <id>UndefinedPHP</id>
          </State>
          <State>
            <id>Validity issuesGroovy</id>
          </State>
          <State>
            <id>Visibility issuesJava</id>
          </State>
          <State>
            <id>Web Services</id>
          </State>
          <State>
            <id>WebSocket issues</id>
          </State>
          <State>
            <id>XML</id>
          </State>
          <State>
            <id>XMLSpring CoreSpring</id>
          </State>
          <State>
            <id>XPath</id>
          </State>
        </expanded-state>
      </profile-state>
    </entry>
  </component>
  <component name="ProjectView">
    <navigator currentView="ProjectPane" proportions="" version="1">
      <flattenPackages />
      <showMembers />
      <showModules />
      <showLibraryContents />
      <hideEmptyPackages />
      <abbreviatePackageNames />
      <autoscrollToSource />
      <autoscrollFromSource />
      <sortByType />
      <manualOrder />
      <foldersAlwaysOnTop value="true" />
    </navigator>
    <panes>
      <pane id="Scratches" />
      <pane id="PackagesPane" />
      <pane id="ProjectPane">
        <subPane>
          <expand>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
            </path>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
              <item name="img" type="462c0819:PsiDirectoryNode" />
            </path>
          </expand>
          <select />
        </subPane>
      </pane>
      <pane id="AndroidView" />
      <pane id="Scope" />
    </panes>
  </component>
  <component name="PropertiesComponent">
    <property name="nodejs_interpreter_path.stuck_in_default_project" value="undefined stuck path" />
    <property name="settings.editor.selected.configurable" value="editor.preferences.fonts.default" />
    <property name="WebServerToolWindowFactoryState" value="false" />
    <property name="aspect.path.notification.shown" value="true" />
    <property name="last_opened_file_path" value="$PROJECT_DIR$" />
    <property name="list.type.of.created.stylesheet" value="CSS" />
    <property name="DefaultHtmlFileTemplate" value="HTML File" />
  </component>
  <component name="RecentsManager">
    <key name="MoveFile.RECENT_KEYS">
      <recent name="$PROJECT_DIR$/js" />
      <recent name="$PROJECT_DIR$/img" />
    </key>
  </component>
  <component name="RunDashboard">
    <option name="ruleStates">
      <list>
        <RuleState>
          <option name="name" value="ConfigurationTypeDashboardGroupingRule" />
        </RuleState>
        <RuleState>
          <option name="name" value="StatusDashboardGroupingRule" />
        </RuleState>
      </list>
    </option>
  </component>
  <component name="RunManager">
    <configuration default="true" type="Applet" factoryName="Applet">
      <option name="HTML_USED" value="false" />
      <option name="WIDTH" value="400" />
      <option name="HEIGHT" value="300" />
      <option name="POLICY_FILE" value="$APPLICATION_HOME_DIR$/bin/appletviewer.policy" />
      <module />
    </configuration>
    <configuration default="true" type="Application" factoryName="Application">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <option name="MAIN_CLASS_NAME" />
      <option name="VM_PARAMETERS" />
      <option name="PROGRAM_PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="ENABLE_SWING_INSPECTOR" value="false" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <module name="" />
      <envs />
    </configuration>
    <configuration default="true" type="JUnit" factoryName="JUnit">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="TEST_OBJECT" value="class" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <envs />
      <patterns />
    </configuration>
    <configuration name="login_old.html" type="JavascriptDebugType" factoryName="JavaScript Debug" temporary="true" nameIsGenerated="true" uri="http://localhost:63343/mikrotik/login_old.html" />
    <configuration default="true" type="Remote" factoryName="Remote">
      <option name="USE_SOCKET_TRANSPORT" value="true" />
      <option name="SERVER_MODE" value="false" />
      <option name="SHMEM_ADDRESS" value="javadebug" />
      <option name="HOST" value="localhost" />
      <option name="PORT" value="5005" />
    </configuration>
    <configuration default="true" type="TestNG" factoryName="TestNG">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="SUITE_NAME" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="GROUP_NAME" />
      <option name="TEST_OBJECT" value="CLASS" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="OUTPUT_DIRECTORY" />
      <option name="ANNOTATION_TYPE" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <option name="USE_DEFAULT_REPORTERS" value="false" />
      <option name="PROPERTIES_FILE" />
      <envs />
      <properties />
      <listeners />
    </configuration>
    <configuration default="true" type="#org.jetbrains.idea.devkit.run.PluginConfigurationType" factoryName="Plugin">
      <module name="" />
      <option name="VM_PARAMETERS" value="-Xmx512m -Xms256m -XX:MaxPermSize=250m -ea" />
      <option name="PROGRAM_PARAMETERS" />
      <predefined_log_file id="idea.log" enabled="true" />
    </configuration>
    <recent_temporary>
      <list size="1">
        <item index="0" class="java.lang.String" itemvalue="JavaScript Debug.login_old.html" />
      </list>
    </recent_temporary>
  </component>
  <component name="ShelveChangesManager" show_recycled="false">
    <option name="remove_strategy" value="false" />
  </component>
  <component name="SvnConfiguration">
    <configuration />
  </component>
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
      <created>1521018748772</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1521018748772</updated>
      <workItem from="1521018751184" duration="14087000" />
      <workItem from="1521057296181" duration="563000" />
      <workItem from="1521058090953" duration="1147000" />
      <workItem from="1521059914099" duration="565000" />
    </task>
    <servers />
  </component>
  <component name="TimeTrackingManager">
    <option name="totallyTimeSpent" value="16362000" />
  </component>
  <component name="ToolWindowManager">
    <frame x="248" y="22" width="949" height="731" extended-state="0" />
    <editor active="true" />
    <layout>
      <window_info id="Palette" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />
      <window_info id="Palette&#9;" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Image Layers" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Analysis" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="true" content_ui="tabs" />
      <window_info id="Maven Projects" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Run" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="false" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Tool" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.26571113" sideWeight="0.5" order="0" side_tool="false" content_ui="combo" />
      <window_info id="Docker" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Database" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Learn" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="Ant Build" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="UI Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Theme Preview" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.39937106" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="true" content_ui="tabs" />
      <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />
      <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Commander" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Hierarchy" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="combo" />
      <window_info id="Inspection" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="5" side_tool="false" content_ui="tabs" />
      <window_info id="Find" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
    </layout>
  </component>
  <component name="TypeScriptGeneratedFilesManager">
    <option name="version" value="1" />
  </component>
  <component name="VcsContentAnnotationSettings">
    <option name="myLimit" value="2678400000" />
  </component>
  <component name="XDebuggerManager">
    <breakpoint-manager>
      <option name="time" value="1" />
    </breakpoint-manager>
    <watches-manager />
  </component>
  <component name="editorHistoryManager">
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css.css" />
    <entry file="file://$PROJECT_DIR$/img/arrow.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/number.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/integrasky.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$APPLICATION_HOME_DIR$/plugins/JavaScriptLanguage/jsLanguageServicesImpl/external/lib.dom.d.ts">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="119">
          <caret line="12227" column="4" lean-forward="false" selection-start-line="12227" selection-start-column="4" selection-end-line="12227" selection-end-column="4" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login_old.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="-545">
          <caret line="71" column="9" lean-forward="true" selection-start-line="60" selection-start-column="0" selection-end-line="71" selection-end-column="9" />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="239">
          <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
  </component>
  <component name="masterDetails">
    <states>
      <state key="ProjectJDKs.UI">
        <settings>
          <last-edited>ruby-2.5.0-p0</last-edited>
          <splitter-proportions>
            <option name="proportions">
              <list>
                <option value="0.2" />
              </list>
            </option>
          </splitter-proportions>
        </settings>
      </state>
    </states>
  </component>
</project>

File: /Hotspot + asterisk + sms\hotspot\by_sms\css\form.css
html, body {
    background: url("../img/background.png");
    height: 100%;
    min-height: 100px;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.logo {
    margin-bottom: 42px;
}

label {
    font-size: 12px;
    font-family: "Opium";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    background: #fff;
    border: solid 1px rgb(220, 224, 226);
    border-radius: 15px;
    padding: 42px;

}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    background-color: rgb(237, 245, 255);
    border: none;
    padding: 17px;
    margin: 7px;
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

.code input[type="text"], .form.already input[type="text"]{
    text-align: center !important;
}

.btn {

    font-size: 12px;
    font-family: "Roboto";
    color: rgb(255, 255, 255);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;

    border-radius: 5px;
    border: none;
    background-color: rgb(77, 161, 255);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;

    margin: 0 auto;

}

.disabled, .disabled:hover{
    background: #eee !important;
    cursor: auto;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.form_description {
    font-size: 16px;
    font-family: "Opium";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_group img {
    margin-right: 14px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: #0421EA !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk + sms\hotspot\by_sms\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot + asterisk + sms\hotspot\by_sms\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="IntegraSky - team@integrasky.ru">

    <link rel="stylesheet" href="../css/form.css">
    <link rel="stylesheet" href="../css/modal.css">
    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>

        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }

        jQuery(document).ready(function () {

            jQuery('#login').mask('+7-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');

                    //jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    jQuery('#login_form').attr('action', '#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, '') + document.getElementById('postfix').value);
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            jQuery('#login2').mask('+7-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {
                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));

            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 3)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 3) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }

            });

            jQuery('#code').on('keyup', function (event) {
                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 3) {
                    jQuery(this).addClass('disabled').removeClass('active');
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                }
            });

            jQuery('#has_code').on('click', function () {
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500)
                });
            });

            jQuery('#pass_remember').on('click', function () {
                jQuery('form.code, form.already').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.login').fadeIn()
                    }, 500)
                });
                jQuery('#postfix').val('d');
                jQuery('#text-phone').text('Напомнить пароль для номера:')
            });


            jQuery('#submit_code').on('click', function(e){
                e.preventDefault();
                var username = jQuery('#username2').val();
                jQuery('form.code').attr('action', "?username=" + username + "#" + username).submit();
            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }

        });
    </script>
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="../img/integrasky.svg" alt="integrasky" width="350px" style="width:350px">
    </div>

    <!--<small class="form_description">Please log on to use the internet hotspot service</small>-->
    <input type="text" name="postfix" id="postfix" value="" hidden />
    <!--<form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="$(link-login-only)" method="post">-->
    <form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="" method="post">
        <p class='upper-label' id='text-phone'>Для подключения к бесплатному WiFi введите номер телефона</p>
        <!--<p>Для подключения к бесплатному WiFi введите номер телефона</p>-->
        <!--<label id="first_label" for="login">Для подключения к бесплатному WiFi введите номер телефона</label>-->
        <div class="input_group tel">
            <img src="../img/phone.png" alt="number">
            <input type="hidden" name="username" id="username1">
            <input type="text" class='round-right-corner phone' id="login" placeholder="+7....">
        </div>
        <br>
        <button class="btn next disabled">
            Отправить
        </button>
    </form>

    <form class="form code" style="display: none" name="sendin" action="" method="post">
        <p class="upper-label">Введите код из SMS-сообщения, которое пришло Вам на телефон</p>
        <div class="input_group">
            <img src="../img/key.png" alt="number">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <input type="text" class='round-right-corner' id="code" maxlength="8">
        </div>
        <br>
        <input type="submit" id="submit_code" class="btn disabled" value="Далее">
    </form>

    <form class="form already" style="display: none" name="sendin" action="" method="post">
        <p class='upper-label'>Введите номер</p>
        <div class="input_group tel">
            <img src="../img/phone.png" alt="number">
            <input type="text" class='round-right-corner phone' id="login2" placeholder="+7....">
        </div>
        <p class='upper-label'>Введите код</p>
        <div class="input_group">
            <img src="../img/key.png" alt="number">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" class='round-right-corner code' id="code2" maxlength="8">
        </div>
        <br />
        <input type="submit" class="btn disabled" value="Отправить">
    </form>

    <br><br>
    <!--<small>Powered by MikroTik RouterOS</small>-->
    <button class="bottom-btn round-corner" onclick="window.location.href='../login.html'">Авторизация по звонку</button>
    <button id="has_code" class="bottom-btn round-corner">У меня уже есть код</button>
    <button id="pass_remember" class="bottom-btn round-corner">Напомнить пароль</button>

    <label id="modal_trigger" for="modal-trigger">Политика конфиденциальности</label>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\by_sms\login_old.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>internet hotspot > login</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="pragma" content="no-cache"/>
    <meta http-equiv="expires" content="-1"/>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>

    <link rel="stylesheet" href="./css/form.css">

    <style type="text/css">
        body {
            color: #737373;
            font-size: 10px;
            font-family: verdana;
        }

        textarea, input, select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active {
            color: #AAAAAA;
            text-decoration: none;
            font-size: 10px;
        }

        a:hover {
            border-bottom: 1px dotted #c1c1c1;
            color: #AAAAAA;
        }

        img {
            border: none;
        }

        td {
            font-size: 14px;
            color: #7A7A7A;
        }
    </style>

</head>

<body>
$(if chap-id)
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username"/>
    <input type="hidden" name="password"/>
    <input type="hidden" name="dst" value="$(link-orig)"/>
    <input type="hidden" name="popup" value="true"/>
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    <!--
    function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
        document.sendin.submit();
        return false;
    }

    //-->
</script>
$(endif)

<div align="center">
    <a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <!--<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br/>$(if-->
                <!--trial == 'yes')Free trial available, <a style="color: #FF8080"-->
                                                        <!--href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click-->
                    <!--here</a>.$(endif)-->
            <!--</div>-->
            <div>
                <small>Please log on to use the internet hotspot service</small>
            </div>
            <br/>
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0"
                   cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form name="login" action="$(link-login-only)" method="post"
                              $(if chap-id) onSubmit="return doLogin()" $(endif)>
                            <input type="hidden" name="dst" value="$(link-orig)"/>
                            <input type="hidden" name="popup" value="true"/>

                            <table width="100" style="background-color: #ffffff">
                                <tr>
                                    <td align="right">login</td>
                                    <td><input style="width: 80px" name="username" type="text" value="$(username)"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right">password</td>
                                    <td><input style="width: 80px" name="password" type="password"/></td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                    <td><input type="submit" value="OK"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr>
                    <td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img
                            src="/img/logobottom.png" alt="mikrotik"/></a></td>
                </tr>
            </table>

            <br/>
            <div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            $(if error)<br/>
            <div style="color: #FF8080; font-size: 9px">$(error)</div>
            $(endif)
        </td>
    </tr>
</table>

<script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
</script>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\css\finish_page.css
@font-face {
    font-family: Open Sans;
    src: local(Open Sans), url(../fonts/OpenSans-Regular.ttf);
}

html, body {
    background: url("../img/background.jpg");
    height: 100%;
    min-height: 100px;
}

.container {
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    font-family: "Open Sans";
    font-size: 13px;
    line-height: 1.2;
    color: rgb(232,232,232);
    width: 300px;
}

.logo {
    margin-bottom: 42px;
}

label {
    color: rgb(50, 60, 71);
}

.upper-label {
    font-size: 26px;
    margin-bottom: 3px;
    margin-top: 15px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: rgb(187,188,206) !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk + sms\hotspot\css\form.css
@font-face {
    font-family: Open Sans;
    src: local(Open Sans), url(../fonts/OpenSans-Regular.ttf);
}

html, body {
    background: url("../img/background.jpg");
    height: 100%;
    min-height: 100px;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: "Open Sans";
}

.logo {
    margin-bottom: 42px;
}

label {
    font-size: 12px;
    font-family: "Open Sans";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    /*background: #fff;
    border: solid 1px rgb(220, 224, 226);*/
    border-radius: 15px;
    padding: 42px;

}
.bottom_btn_group {
    padding: 24px;
}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    /*background-color: rgb(237, 245, 255);*/
    background-color: rgb(102, 112, 137);
    color: rgb(232, 232, 232);
    border: none;
    padding: 17px;
    /*margin: 7px;*/
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

/* webkit */
input::-webkit-input-placeholder {
    color: rgb(232, 232, 232);
    opacity:1;
}

/* Firefox 19+ */
input::-moz-placeholder {
    color: rgb(232, 232, 232);
    opacity:1;
}

/* Firefox 18- */
input:-moz-placeholder {
    color: rgb(232, 232, 232);
    opacity:1;
}

/* IE */
input:-ms-input-placeholder {
    color: rgb(232, 232, 232);
    opacity:1;
}

.code input[type="text"], .code{
    text-align: center !important;
}

.btn, .bottom-btn {
    font-family: "Open Sans";
    color: rgb(255, 255, 255);
    /*text-transform: uppercase;*/
    line-height: 1.2;
    text-align: center;

    /*background-color: rgb(77, 161, 255);*/
    /*display: flex;
    flex-direction: row;
    flex-wrap: nowrap;*/
}

.btn {
    width: 100%;
    font-size: 20px;
    border-radius: 5px;
    height: 55px;
    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;
    margin: 0 auto;
    background-color: rgb(56, 197, 214);
    border: none;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.bottom-btn {
    width: 50%;
    font-size: 16px;
    padding: 3px 0px;
    background-color: inherit;
    color: rgb(56, 197, 214);
    border: 1px solid rgb(56, 197, 214);
}

.bottom-btn:hover {
    cursor: pointer;
    background-color: rgb(56, 197, 214);
    color: rgb(255, 255, 255);
}

.bottom-btn:focus {
    outline: none;
}

.redirect {
    margin-right: 7px;
}

.disabled, .disabled:hover{
    /*background: #eee !important;*/
    cursor: auto;
}

.form_description {
    font-size: 16px;
    font-family: "Open Sans";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 55px;
}

.phone_to_call {
    color: rgb(56, 197, 214);
}

.input_group img {
    height: 100%;
}

.bottom-links {
    color: rgb(187,188,206);
}

.upper-label {
    width: 300px;
    color: rgb(232,232,232);
}

.round-right-corner {
    -moz-border-radius: 0px 3px 3px 0px; /* Firefox */
    -webkit-border-radius: 0px 3px 3px 0px; /* Safari 4 */
    border-radius: 0px 3px 3px 0px; /* IE 9, Safari 5, Chrome */
}

/*.phone {
    height: 100%;
}*/

.round-corner {
    -moz-border-radius: 3px; /* Firefox */
    -webkit-border-radius: 3px; /* Safari 4 */
    border-radius: 3px; /* IE 9, Safari 5, Chrome */
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: rgb(187,188,206) !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk + sms\hotspot\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot + asterisk + sms\hotspot\error.html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > error</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
</head>
<body>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
Hotspot ERROR: $(error)<br>
<br>
Login page: <a href="$(link-login)">$(link-login)</a>
</td>
</tr>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\errors.txt
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in

# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)

internal-error = internal error ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = configuration error ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = you are not logged in (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = cannot assign ip address - no more free addresses from pool

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot service is shutting down

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = no more sessions are allowed for user $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = session limit reached ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = invalid username ($(username)): this MAC address is not yours

# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.

chap-missing = web browser did not send challenge response (try again, enable JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = invalid username or password

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = user $(username) is not allowed to log in from this MAC address

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = user $(username) has reached uptime limit
traffic-limit = user $(username) has reached traffic limit

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server is not responding

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = already authorizing, retry later

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /Hotspot + asterisk + sms\hotspot\fonts\LICENSE.txt

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


File: /Hotspot + asterisk + sms\hotspot\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="IntegraSky - team@integrasky.ru">

    <link rel="stylesheet" href="./css/form.css">
    <link rel="stylesheet" href="./css/modal.css">

    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>

        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }

        jQuery(document).ready(function () {

            jQuery('#login').mask('+7-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');

                    jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    //jQuery('#login_form').attr('action', '#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));

                    //jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, '') + document.getElementById('postfix').value);
                    jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, '') + 'd');
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            jQuery('#login2').mask('+7-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {
                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));

            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 3)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 3) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }

            });

            jQuery('#code').on('keyup', function (event) {
                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 3) {
                    jQuery(this).addClass('disabled').removeClass('active');
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                }
            });

            jQuery('#has_code').on('click', function () {
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500)
                });
            });

            /*jQuery('#pass_remember').on('click', function () {
                jQuery('form.code, form.already').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.login').fadeIn()
                    }, 500)
                });
                jQuery('#postfix').val('d');
                jQuery('#text-phone').text('Напомнить пароль для номера:')
            });*/


            jQuery('#submit_code').on('click', function(e){
                e.preventDefault();
                var username = jQuery('#username2').val();
                jQuery('form.code').attr('action', "?username=" + username + "#" + username).submit();
            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }

        });
    </script>
</head>
<body>
<div class="container">
<div>
    <div class="logo">
        <img src="./img/integrasky.svg" alt="IntegraSky" width="350px" style="width:350px">
    </div>

    <!--<small class="form_description">Please log on to use the internet hotspot service</small>-->
    <!--<input type="text" name="postfix" id="postfix" value="" hidden />-->
    <form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="$(link-login-only)" method="post">
    <!--<form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="" method="post">-->
        <p class='upper-label' id='text-phone'>Для подключения к бесплатному WiFi введите номер телефона</p>
        <!--<p>Для подключения к бесплатному WiFi введите номер телефона</p>-->
        <!--<label id="first_label" for="login">Для подключения к бесплатному WiFi введите номер телефона</label>-->
        <div class="input_group tel">
            <img src="./img/phone.png" alt="number">
            <input type="hidden" name="username" id="username1">
            <input type="text" class='round-right-corner phone' id="login" placeholder="+7....">
        </div>
        <br>
        <button class="btn next disabled">
            Отправить
        </button>
    </form>

    <form class="form code" style="display: none" name="sendin" action="" method="post">
        <p class="upper-label">Введите код из SMS-сообщения, которое пришло Вам на телефон</p>
        <div class="input_group">
            <img src="./img/key.png" alt="number">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <input type="text" class='round-right-corner' id="code" maxlength="8">
        </div>
        <br>
        <input type="submit" id="submit_code" class="btn disabled" value="Далее">
    </form>

    <form class="form already" style="display: none" name="sendin" action="" method="post">
        <p class='upper-label'>Введите номер</p>
        <div class="input_group tel">
            <img src="./img/phone.png" alt="number">
            <input type="text" class='round-right-corner phone' id="login2" placeholder="+7....">
        </div>
        <p class='upper-label'>Введите код</p>
        <div class="input_group">
            <img src="./img/key.png" alt="number">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" class='round-right-corner code' id="code2" maxlength="8">
        </div>
        <br />
        <input type="submit" class="btn disabled" value="Отправить">
    </form>

    <br>
    <!--<small>Powered by MikroTik RouterOS</small>-->

    <div class="input_group bottom_btn_group">
        <button class="bottom-btn round-corner redirect" onclick="window.location.href='by_call/login.html'">Авторизация<br />по звонку</button>
        <button id="has_code" class="bottom-btn round-corner">У меня<br />есть код</button>
    </div>
    <!--<button id="pass_remember" class="bottom-btn round-corner">Напомнить пароль</button>-->

    <label id="modal_trigger" for="modal-trigger">Политика конфиденциальности</label>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</div>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\login_old.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>internet hotspot > login</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="pragma" content="no-cache"/>
    <meta http-equiv="expires" content="-1"/>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>

    <link rel="stylesheet" href="./css/form.css">

    <style type="text/css">
        body {
            color: #737373;
            font-size: 10px;
            font-family: verdana;
        }

        textarea, input, select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active {
            color: #AAAAAA;
            text-decoration: none;
            font-size: 10px;
        }

        a:hover {
            border-bottom: 1px dotted #c1c1c1;
            color: #AAAAAA;
        }

        img {
            border: none;
        }

        td {
            font-size: 14px;
            color: #7A7A7A;
        }
    </style>

</head>

<body>
$(if chap-id)
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username"/>
    <input type="hidden" name="password"/>
    <input type="hidden" name="dst" value="$(link-orig)"/>
    <input type="hidden" name="popup" value="true"/>
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    <!--
    function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
        document.sendin.submit();
        return false;
    }

    //-->
</script>
$(endif)

<div align="center">
    <a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <!--<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br/>$(if-->
                <!--trial == 'yes')Free trial available, <a style="color: #FF8080"-->
                                                        <!--href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click-->
                    <!--here</a>.$(endif)-->
            <!--</div>-->
            <div>
                <small>Please log on to use the internet hotspot service</small>
            </div>
            <br/>
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0"
                   cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form name="login" action="$(link-login-only)" method="post"
                              $(if chap-id) onSubmit="return doLogin()" $(endif)>
                            <input type="hidden" name="dst" value="$(link-orig)"/>
                            <input type="hidden" name="popup" value="true"/>

                            <table width="100" style="background-color: #ffffff">
                                <tr>
                                    <td align="right">login</td>
                                    <td><input style="width: 80px" name="username" type="text" value="$(username)"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right">password</td>
                                    <td><input style="width: 80px" name="password" type="password"/></td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                    <td><input type="submit" value="OK"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr>
                    <td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img
                            src="/img/logobottom.png" alt="mikrotik"/></a></td>
                </tr>
            </table>

            <br/>
            <div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            $(if error)<br/>
            <div style="color: #FF8080; font-size: 9px">$(error)</div>
            $(endif)
        </td>
    </tr>
</table>

<script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
</script>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\logout.html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > logout</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{
 
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
</head>

<body>
<script language="JavaScript">
<!--
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
//-->
</script>

<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<b>you have just logged out</b> <br><br>
<table class="tabula" border="1">  
<tr><td align="right">user name</td><td>$(username)</td></tr>
<tr><td align="right">IP address</td><td>$(ip)</td></tr>
<tr><td align="right">MAC address</td><td>$(mac)</td></tr>
<tr><td align="right">session time</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">time left</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">bytes up/down:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="log in">
</form>
</td>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\lv\alogin.html
<html>
<head>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > novirzt</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = '$(link-redirect)';
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Js esat piesldzies
	<br><br>
	Ja nekas nenotiek, klikiniet <a href="$(link-redirect)">eit</a></td>
</tr>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\lv\errors.txt
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in

# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)

internal-error = sistēmas kļūda ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = konfigurācijas kļūda ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Jūs neesat pieslēdzies (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = nevaru piešķirt IP adresi - nav vairāk brīvu adrešu krātuvē

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot serviss tiek apstādināts, mēģiniet pēc brīža vēlreiz

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = lietotājam $(username) vairāk sessijas nav atļautas

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = ir sasniegts maksimālais sessiju skaits ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = nepareizs lietotāja vārds ($(username)): šī MAC adrese nav tava

# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.

chap-missing = problēmas ar kodu (mēģiniet vēlreiz, atļaujiet JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = nepareizs lietotāja vārds vai parole

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = lietotājam $(username) nav atļauts pieslēgties no šīs MAC adreses

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = lietotāja $(username) atļautasi pieslēguma laiks ir beidzies
traffic-limit = lietotāja $(username) atļautais datu pārraides apjoms ir sasniegts

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = autorizācijas serveris neatbild (mēģiniet vēlreiz)

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = notiek autorizācija (mēģiniet vēlāk)

# radius-reply
# Radius server returned some custom error message

radius-reply = autorizācijas kļūda ($(error-orig))


File: /Hotspot + asterisk + sms\hotspot\lv\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />
<title>mikrotik hotspot > ieeja </title>
<style type="text/css">
body {color: #737373; font-size: 10px; font-family: verdana;}

textarea,input,select {
background-color: #FDFBFB;
border: 1px solid #BBBBBB;
padding: 2px;
margin: 1px;
font-size: 14px;
color: #808080;
}

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 14px; color: #7A7A7A; }
</style>

</head>

<body>
$(if chap-id)
	<form name="sendin" action="$(link-login-only)" method="post">
		<input type="hidden" name="username" />
		<input type="hidden" name="password" />
		<input type="hidden" name="dst" value="$(link-orig)" />
		<input type="hidden" name="popup" value="true" />
	</form>
	
	<script type="text/javascript" src="/md5.js"></script>
	<script type="text/javascript">
	<!--
	    function doLogin() {
		document.sendin.username.value = document.login.username.value;
		document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
		document.sendin.submit();
		return false;
	    }
	//-->
	</script>
$(endif)

<div align="center">
<a href="$(link-login-only)?target=%2F&amp;dst=$(link-orig-esc)">English</a>
</div>

<table width="100%" style="margin-top: 10%;">
	<tr>
	<td align="center" valign="middle">
		<div class="notice" style="color: #c1c1c1; font-size: 9px">Lūdzu pieslēdzieties, lai lietotu mikrotik hotspot servisu.<br />$(if trial == 'yes')Lai izmēģinātu bez maksas, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">spiediet šeit.</a>.$(endif)</div><br />
		<table width="240" height="240" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
			<tr>
				<td align="center" valign="bottom" height="175" colspan="2">
					<form name="login" action="$(link-login-only)" method="post"
					    $(if chap-id) onSubmit="return doLogin()" $(endif)>
						<input type="hidden" name="dst" value="$(link-orig)" />
						<input type="hidden" name="popup" value="true" />
						
							<table width="100" style="background-color: #ffffff">
								<tr><td align="right">login</td>
										<td><input style="width: 80px" name="username" type="text" value="$(username)"/></td>
								</tr>
								<tr><td align="right">parole</td>
										<td><input style="width: 80px" name="password" type="password"/></td>
								</tr>
								<tr><td>&nbsp;</td>
										<td><input type="submit" value="OK" /></td>
								</tr>
							</table>
					</form>
				</td>
			</tr>
			<tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
		</table>
	
	<br /><div style="color: #c1c1c1; font-size: 9px">nodrošina mikrotik routeros &copy; 2005 mikrotik</div>
	$(if error)<br /><div style="color: #FF8080; font-size: 9px">$(error)</div>$(endif)
	</td>
	</tr>
</table>

<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\lv\logout.html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > atsldzies</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{
 
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
</head>

<body>
<script language="JavaScript">
<!--
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
//-->
</script>

<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<b>sessija ir aizvrta</b> <br><br>
<table class="tabula" border="1">  
<tr><td align="right">lietotja vrds</td><td>$(username)</td></tr>
<tr><td align="right">IP adrese</td><td>$(ip)</td></tr>
<tr><td align="right">MAC adrese</td><td>$(mac)</td></tr>
<tr><td align="right">sesijas ilgums</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">atlikuais laiks</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="pieslgties no jauna">
</form>
</td>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\lv\radvert.html
<html>
<head>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > advertisement</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = '$(link-orig)';
    }
    function openAd() {
	location.href = '$(link-redirect)';
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Reklma.
	<br><br>
	Ja nekas nenotiek, atveriet
	<a href="$(link-redirect)" target="hotspot_advert">reklmu</a>
	parocgi.
	</td>
</tr>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\lv\status.html
<html>
<head>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > statuss</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{
 
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
<script language="JavaScript">
<!--
$(if advert-pending == 'yes')
    var popup = '';
    function focusAdvert() {
	if (window.focus) popup.focus();
    }
    function openAdvert() {
	popup = open('$(link-advert)', 'hotspot_advert', '');
	setTimeout("focusAdvert()", 1000);
    }
$(endif)
    function openLogout() {
	if (window.name != 'hotspot_status') return true;
        open('$(link-logout)', 'hotspot_logout', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=280,height=250');
	window.close();
	return false;
    }
//-->
</script>
</head>
<body bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0"
$(if advert-pending == 'yes')
	onLoad="openAdvert()"
$(endif)
>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
<table border="1" class="tabula">
$(if login-by == 'trial')
	<br><div style="text-align: center;">Sveiks!</div><br>
$(elif login-by != 'mac')
	<br><div style="text-align: center;">Sveiks $(username)!</div><br>
$(endif)
	<tr><td align="right">IP adrese:</td><td>$(ip)</td></tr>
	<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
$(if session-time-left)
	<tr><td align="right">ilgums / atlicis:</td><td>$(uptime) / $(session-time-left)</td></tr>
$(else)
	<tr><td align="right">ilgums:</td><td>$(uptime)</td></tr>
$(endif)
$(if blocked == 'yes')
	<tr><td align="right">statuss:</td><td><div style="color: #FF8080">
nepiecieama <a href="$(link-advert)" target="hotspot_advert">reklma</a></div></td>
$(elif refresh-timeout)
	<tr><td align="right">intervls:</td><td>$(refresh-timeout)</td>
$(endif)

</table>
$(if login-by-mac != 'yes')
<br>
<input type="submit" value="atslgties">
$(endif)
</form>
</td>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\md5.js
/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 1.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Code also contributed by Greg Holt
 * See http://pajhome.org.uk/site/legal.html for details.
 */

/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt))
}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t)
{
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t)
{
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t)
{
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t)
{
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t)
{
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}

/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x)
{
  var a =  1732584193
  var b = -271733879
  var c = -1732584194
  var d =  271733878

  for(i = 0; i < x.length; i += 16)
  {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d

    a = ff(a, b, c, d, x[i+ 0], 7 , -680876936)
    d = ff(d, a, b, c, x[i+ 1], 12, -389564586)
    c = ff(c, d, a, b, x[i+ 2], 17,  606105819)
    b = ff(b, c, d, a, x[i+ 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i+ 4], 7 , -176418897)
    d = ff(d, a, b, c, x[i+ 5], 12,  1200080426)
    c = ff(c, d, a, b, x[i+ 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i+ 7], 22, -45705983)
    a = ff(a, b, c, d, x[i+ 8], 7 ,  1770035416)
    d = ff(d, a, b, c, x[i+ 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i+10], 17, -42063)
    b = ff(b, c, d, a, x[i+11], 22, -1990404162)
    a = ff(a, b, c, d, x[i+12], 7 ,  1804603682)
    d = ff(d, a, b, c, x[i+13], 12, -40341101)
    c = ff(c, d, a, b, x[i+14], 17, -1502002290)
    b = ff(b, c, d, a, x[i+15], 22,  1236535329)

    a = gg(a, b, c, d, x[i+ 1], 5 , -165796510)
    d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632)
    c = gg(c, d, a, b, x[i+11], 14,  643717713)
    b = gg(b, c, d, a, x[i+ 0], 20, -373897302)
    a = gg(a, b, c, d, x[i+ 5], 5 , -701558691)
    d = gg(d, a, b, c, x[i+10], 9 ,  38016083)
    c = gg(c, d, a, b, x[i+15], 14, -660478335)
    b = gg(b, c, d, a, x[i+ 4], 20, -405537848)
    a = gg(a, b, c, d, x[i+ 9], 5 ,  568446438)
    d = gg(d, a, b, c, x[i+14], 9 , -1019803690)
    c = gg(c, d, a, b, x[i+ 3], 14, -187363961)
    b = gg(b, c, d, a, x[i+ 8], 20,  1163531501)
    a = gg(a, b, c, d, x[i+13], 5 , -1444681467)
    d = gg(d, a, b, c, x[i+ 2], 9 , -51403784)
    c = gg(c, d, a, b, x[i+ 7], 14,  1735328473)
    b = gg(b, c, d, a, x[i+12], 20, -1926607734)

    a = hh(a, b, c, d, x[i+ 5], 4 , -378558)
    d = hh(d, a, b, c, x[i+ 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i+11], 16,  1839030562)
    b = hh(b, c, d, a, x[i+14], 23, -35309556)
    a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060)
    d = hh(d, a, b, c, x[i+ 4], 11,  1272893353)
    c = hh(c, d, a, b, x[i+ 7], 16, -155497632)
    b = hh(b, c, d, a, x[i+10], 23, -1094730640)
    a = hh(a, b, c, d, x[i+13], 4 ,  681279174)
    d = hh(d, a, b, c, x[i+ 0], 11, -358537222)
    c = hh(c, d, a, b, x[i+ 3], 16, -722521979)
    b = hh(b, c, d, a, x[i+ 6], 23,  76029189)
    a = hh(a, b, c, d, x[i+ 9], 4 , -640364487)
    d = hh(d, a, b, c, x[i+12], 11, -421815835)
    c = hh(c, d, a, b, x[i+15], 16,  530742520)
    b = hh(b, c, d, a, x[i+ 2], 23, -995338651)

    a = ii(a, b, c, d, x[i+ 0], 6 , -198630844)
    d = ii(d, a, b, c, x[i+ 7], 10,  1126891415)
    c = ii(c, d, a, b, x[i+14], 15, -1416354905)
    b = ii(b, c, d, a, x[i+ 5], 21, -57434055)
    a = ii(a, b, c, d, x[i+12], 6 ,  1700485571)
    d = ii(d, a, b, c, x[i+ 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i+10], 15, -1051523)
    b = ii(b, c, d, a, x[i+ 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i+ 8], 6 ,  1873313359)
    d = ii(d, a, b, c, x[i+15], 10, -30611744)
    c = ii(c, d, a, b, x[i+ 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i+13], 21,  1309151649)
    a = ii(a, b, c, d, x[i+ 4], 6 , -145523070)
    d = ii(d, a, b, c, x[i+11], 10, -1120210379)
    c = ii(c, d, a, b, x[i+ 2], 15,  718787259)
    b = ii(b, c, d, a, x[i+ 9], 21, -343485551)

    a = safe_add(a, olda)
    b = safe_add(b, oldb)
    c = safe_add(c, oldc)
    d = safe_add(d, oldd)
  }
  return [a, b, c, d]
}

/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = "0123456789abcdef"
  var str = ""
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8)) & 0xF)
  }
  return str
}

/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for(var i = 0; i < binarray.length * 32; i += 6)
  {
    str += tab.charAt(((binarray[i>>5] << (i%32)) & 0x3F) |
                      ((binarray[i>>5+1] >> (32-i%32)) & 0x3F))
  }
  return str
}

/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str)
{
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>2] |= (str.charCodeAt(i) & 0xFF) << ((i%4) * 8)
  blks[i>>2] |= 0x80 << ((i%4) * 8)
  blks[nblk*16-2] = str.length * 8
  return blks
}

/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str)
{
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>1] |= str.charCodeAt(i) << ((i%2) * 16)
  blks[i>>1] |= 0x80 << ((i%2) * 16)
  blks[nblk*16-2] = str.length * 16
  return blks
}

/*
 * External interface
 */
function hexMD5 (str) { return binl2hex(coreMD5( str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5 (str) { return binl2b64(coreMD5( str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5( str2binl(str))) }


File: /Hotspot + asterisk + sms\hotspot\radvert.html
<html>
<head>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>mikrotik hotspot > advertisement</title>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = unescape('$(link-orig-esc)');
    }
    function openAd() {
	location.href = unescape('$(link-redirect-esc)');
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Advertisement.
	<br><br>
	If nothing happens, open
	<a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
	manually.
	</td>
</tr>
</table>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\redirect.html
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\rlogin.html
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)?target=xml</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
-->
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\status.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="./css/finish_page.css">
    <link rel="stylesheet" href="./css/modal.css">

    <!--<script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>-->
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="./img/integrasky.svg" alt="integrasky" width="350px" style="width:350px">
    </div>
    <img src="./img/icon_done.png" width="75px" style="width:75px">
    <p class='upper-label'>Соединение<br />успешно установлено.</p>
    <p>Вы подключились к бесплатному интернету</p>

    <br /><br />

    <label id="modal_trigger" for="modal-trigger">Условия пользовательского соглашения</label>

<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</div>
</body>
</html>


File: /Hotspot + asterisk + sms\hotspot\xml\alogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>50</ResponseCode>
	<LogoffURL>$(link-logout)</LogoffURL>
	<RedirectionURL>$(link-redirect)</RedirectionURL>
$(if radius18[0])	<ReplyMessage>$(radius18[0])</ReplyMessage>	$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\css\form.css
@font-face {
    font-family: Open Sans;
    src: local(Open Sans), url(../fonts/OpenSans-Regular.ttf);
}

html, body {
    background: url("../img/background.jpg");
    height: 100%;
    min-height: 100px;
}

.container {
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    font-family: "Open Sans";
    font-size: 13px;
    line-height: 1.2;
    color: rgb(232,232,232);
    width: 300px;
}

.logo {
    margin-bottom: 42px;
}

label {
    color: rgb(50, 60, 71);
}

.upper-label {
    font-size: 26px;
    margin-bottom: 3px;
    margin-top: 15px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: rgb(187,188,206) !important;
    text-decoration: underline;
}


File: /Hotspot + asterisk + sms\hotspot\xml\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot + asterisk + sms\hotspot\xml\error.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>255</ResponseCode>
	<ReplyMessage>$(error)</ReplyMessage>
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\flogout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\fonts\LICENSE.txt

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


File: /Hotspot + asterisk + sms\hotspot\xml\login.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>
$(if error-type == 'radius-timeout')
		102
$(else)
		100
$(endif)
	</ResponseCode>
$(if error)		<ReplyMessage>$(error)</ReplyMessage>		$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\logout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
<WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\rlogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
--> </HTML>


File: /Hotspot + asterisk + sms\hotspot\xml\WISPAccessGatewayParam.xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="WISPAccessGatewayParam">
		<xs:complexType>
			<xs:choice>
				<xs:element name="Redirect" type="RedirectType"/>
				<xs:element name="Proxy" type="ProxyType"/>
				<xs:element name="AuthenticationReply" type="AuthenticationReplyType"/>
				<xs:element name="AuthenticationPollReply" type="AuthenticationPollReplyType"/>
				<xs:element name="LogoffReply" type="LogoffReplyType"/>
				<xs:element name="AbortLoginReply" type="AbortLoginReplyType"/>
			</xs:choice>
		</xs:complexType>
	</xs:element>
	<xs:simpleType name="AbortLoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="NextURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="AccessProcedureType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="AccessLocationType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LocationNameType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="MessageTypeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ResponseCodeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ReplyMessageType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginResultsURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="LogoffURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="DelayType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:complexType name="RedirectType">
		<xs:all>
			<xs:element name="AccessProcedure" type="AccessProcedureType"/>
			<xs:element name="AccessLocation" type="AccessLocationType"/>
			<xs:element name="LocationName" type="LocationNameType"/>
			<xs:element name="LoginURL" type="LoginURLType"/>
			<xs:element name="AbortLoginURL" type="AbortLoginURLType"/>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="ProxyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="NextURL" type="NextURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LoginResultsURL" type="LoginResultsURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationPollReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="LogoffReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AbortLoginReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:sequence>
	</xs:complexType>
</xs:schema>


File: /Hotspot + asterisk + sms\Log-in script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-login 

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:local ipuser [/ip hotspot active get [find user=$user] address];

:local usermac [/ip hotspot active get [find user=$user] mac-address]

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5]; 

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:local mac1 [:pick $usermac 0 2];

:local mac2 [:pick $usermac 3 5];

:local mac3 [:pick $usermac 6 8];

:local mac4 [:pick $usermac 9 11];

:local mac5 [:pick $usermac 12 14];

:local mac6 [:pick $usermac 15 17];

:set $usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6})]

:put $time1

/ip firewall address-list add list=$today address="log-in.$time1.$user.$usermac.$ipuser"



do {/tool e-mail send to="email@gmail.com" subject="Login number: $user on $nas" body="Login number: $user mac-address: $usermac time: $time1 ip-address: $ipuser"} on-error={};


File: /Hotspot + asterisk + sms\Log-out script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-logout

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5];

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:put $time1

/ip firewall address-list add list=$today address="log-out.$time1.$user"

/tool e-mail send to="email@gmail.com" subject="Logout number: $user on $nas" body="Logout number: $user time: $time1"

File: /Hotspot + asterisk + sms\script backup.txt
/export compact file=auto_backup_user-manager;
/system backup save name=auto_backup_user-manager.backup;
:if ( [ /file find name=auto_backup_user-manager.umb ] != "" ) do={
/file remove auto_backup_user-manager.umb;
};
/tool user-manager database save name=auto_backup_user-manager;
/delay delay-time=60;


/tool e-mail send to="email@gmail.com" subject=("Export Script User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.rsc;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Config User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.backup;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Database User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.umb;
/delay delay-time=60;

File: /Hotspot + asterisk + sms\script on userman server.txt
# You need install userman packedge from extra packetges and you need create log:
# /system logging action add name=userman target=memory
# /system logging add action=userman topics=manager

# User manager config and user profile limitation
# Profile
# /tool user-manager profile add name=guest name-for-users="" override-shared-users=5 owner=admin price=0 starts-at=logon validity=0s
# Profile limit
# /tool user-manager profile limitation add address-list="" download-limit=0B group-name="" ip-pool="" ip-pool6="" name=guest owner=admin rate-limit-burst-rx=5242880B rate-limit-burst-time-rx=16s rate-limit-burst-time-tx=16s rate-limit-burst-treshold-rx=2097152B rate-limit-burst-treshold-tx=2097152B rate-limit-burst-tx=5242880B rate-limit-min-rx=2097152B rate-limit-min-tx=2097152B rate-limit-priority=8 rate-limit-rx=2097152B rate-limit-tx=2097152B transfer-limit=0B upload-limit=0B uptime-limit=0s
# User template
# /tool user-manager user add customer=admin disabled=no ipv6-dns=:: password=PassWord123 shared-users=5 username=test wireless-enc-algo=none wireless-enc-key="" wireless-psk=""
# Router add to usermanager - change ip router and password for radius server
# /tool user-manager router add coa-port=1700 customer=admin disabled=no ip-address=10.1.1.1 log=auth-ok,auth-fail,acct-ok,acct-fail name=cpe34 shared-secret=PassWord123 use-coa=no


:local Lines { 0="" }

:local LineI 1

:foreach line in=[/log find buffer=userman message~"Reply-Message = \"user "] do={

  :set ($Lines->"$LineI") [ /log get $line message ]

  :set LineI ($LineI + 1)

}

/system logging action set userman memory-lines=1;

delay 300ms

/system logging action set userman memory-lines=1000;



:foreach key,content in=$Lines do={
 :set ($Lines->"$key") ""

 :do {
#  :put $content;
  :local pos1 [:find $content "<" 0];
#  :put $pos1
  :if ($pos1 != " ") do={ 
   :local uname ""; 
   :local uname7 "";
   :local uname8 "";
   :local uname9 "";
   :local unameD "";
   :local phone ""; 
   :if ([:pick $content ($pos1+1)] = "9") do={ 
    :set uname [:pick $content ($pos1+1) ($pos1+11)];  
#    :put $uname;
    :set uname7 [:put ("7" . {$uname})]
    :set uname8 [:put ("8" . {$uname})]
    :set unameD [:pick $content ($pos1+11)];
#    :put $unameD 
    #SendTest

    :local sendtest true;
    :foreach i in=[/ip fi ad print as-value where list=sendsms] do={
    :if (($i->"address")=$uname7) do={
    :set sendtest false;
#    :put "sendtest=$sendtest";
     }
    }

    :local numberd [:pick $content ($pos1+11)];
    #Add user to user-manager  

    :if ($sendtest=true and $numberd = "d") do={ 

      #Password generation 

    :local date [/system clock get time]; 

    :local hour [:pick $date 0 2]; 

    :local min [:pick $date 3 5]; 

    :local sec [:pick $date 6 8]; 

    :local usernumber [:pick $content ($pos1+5) ($pos1+7)];

#    :put $usernumber;

    :global pass 27394; 

    :set pass ($hour * $min * $sec - $usernumber); 

    :if ($pass <= 0) do={ 

     :set pass 6524;

     }

#    :put $pass;

    :local changepassword [:do {/tool user-manager user set password=$pass number=[find username=$uname]} on-error={}];
    :local timeoutsendsms [:do {/ip firewall address-list add list="sendsms" address="$uname7" timeout="3m"} on-error={}];
    :local sendsms [:do {/tool fetch url="http://cab.websms.ru/http_in5.asp?http_username=USER&http_password=Pass&Phone_list=$uname7&Message=$pass" keep-result=no} on-error={}];
    :local newuser [:do {/tool user-manager user add username=$uname password=$pass customer=admin copy-from=test disabled=no phone=$uname7} on-error={:do {($changepassword&&$timeoutsendsms&&$sendsms)} on-error={}}];

#    :put TRUE

          }
         }
        }
       }
      }



File: /Hotspot + asterisk + sms\userman-server.rsc
/system logging action add name=userman target=memory
/tool user-manager customer set admin access=own-routers,own-users,own-profiles,own-limits,config-payment-gw password=PassWord
/tool user-manager profile add name=guest name-for-users="" override-shared-users=5 owner=admin price=0 starts-at=logon validity=0s
/tool user-manager profile limitation add address-list="" download-limit=0B group-name="" ip-pool="" ip-pool6="" name=guest owner=admin rate-limit-burst-rx=5242880B rate-limit-burst-time-rx=16s rate-limit-burst-time-tx=16s rate-limit-burst-treshold-rx=2097152B rate-limit-burst-treshold-tx=2097152B rate-limit-burst-tx=5242880B rate-limit-min-rx=2097152B rate-limit-min-tx=2097152B rate-limit-priority=8 rate-limit-rx=2097152B rate-limit-tx=2097152B transfer-limit=0B upload-limit=0B uptime-limit=0s
/system scheduler add interval=10s name=schedule1 on-event="/system script run userman" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=feb/20/2020 start-time=09:28:22
/system script add dont-require-permissions=no name=userman owner=admin77 policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":foreach line in=[/log find buffer=userman message~\"Reply-Message = \\\"user \"] do={\
    \n\
    \n :do {:local content [/log get \$line message];\
    \n\
    \n  :put \$content;\
    \n\
    \n  :local pos1 [:find \$content \"<\" 0];\
    \n\
    \n  :put \$pos1;\
    \n\
    \n  :if (\$pos1 != \" \") do={ \
    \n\
    \n   :local uname \"\"; \
    \n\
    \n   :local uname7 \"\";\
    \n\
    \n   :local uname8 \"\";\
    \n\
    \n   :local uname9 \"\";\
    \n\
    \n   :local unameD \"\";\
    \n\
    \n   :local phone \"\"; \
    \n\
    \n   :if ([:pick \$content (\$pos1+1)] = \"9\") do={ \
    \n\
    \n    :set uname [:pick \$content (\$pos1+1) (\$pos1+11)];  \
    \n\
    \n    :put \$uname;\
    \n\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n\
    \n    :set unameD [:pick \$content (\$pos1+11)];\
    \n\
    \n    :put \$unameD \
    \n\
    \n    #SendTest\
    \n\
    \n\
    \n\
    \n    :local sendtest yes;\
    \n\
    \n    :foreach i in=[/ip fi ad print as-value where list=sendsms] do={\
    \n\
    \n    :if ((\$i->\"address\")=\$uname7) do={\
    \n\
    \n    :set \$sendtest no;\
    \n\
    \n     }\
    \n\
    \n    }\
    \n\
    \n     #Password generation \
    \n\
    \n\
    \n\
    \n    :local date [/system clock get time]; \
    \n\
    \n\
    \n\
    \n    :local hour [:pick \$date 0 2]; \
    \n\
    \n\
    \n\
    \n    :local min [:pick \$date 3 5]; \
    \n\
    \n\
    \n\
    \n    :local sec [:pick \$date 6 8]; \
    \n\
    \n\
    \n\
    \n    :local usernumber [:pick \$content (\$pos1+5) (\$pos1+7)];\
    \n\
    \n\
    \n\
    \n    :put \$usernumber;\
    \n\
    \n\
    \n\
    \n    :global pass 27394; \
    \n\
    \n\
    \n\
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber); \
    \n\
    \n\
    \n\
    \n    :if (\$pass = 0) do={ \
    \n\
    \n\
    \n\
    \n     :set pass 6524;\
    \n\
    \n\
    \n\
    \n     }\
    \n\
    \n\
    \n\
    \n    :put \$pass;\
    \n\
    \n\
    \n\
    \n    :local changepassword [:do {/tool user-manager user set password=\$pass number=[find username=\$uname]} on-error={}];\
    \n\
    \n    :local timeoutsendsms [:do {/ip firewall address-list add list=\"sendsms\" address=\"\$uname7\" timeout=\"3m\"} on-error={}];\
    \n\
    \n    :local putpasschange [:put \"PAASScange\"]\
    \n\
    \n    :local putpassnew [:put \"Pass New\"]\
    \n\
    \n    :local sendsms [/tool fetch url=\"https://gate.smsaero.ru/send/\\\?user=EMAIL&password=PASSWORD&to=\$uname7&text=\$pass&from=FROM\" keep-result=no];\
    \n\
    \n    :local newuser [:do {/tool user-manager user add username=\$uname password=\$pass customer=admin copy-from=test disabled=no phone=\$uname7} on-error={}];   \
    \n\
    \n\
    \n    #Add user to user-manager  \
    \n\
    \n\
    \n\
    \n    :if ((\$sendtest=yes)&&[:pick \$content (\$pos1+11)] != \"d\") do={ \
    \n\
    \n    :do {(\$newuser&&\$timeoutsendsms&&\$sendsms)} on-error={};\
    \n\
    \n\
    \n\
    \n    }\
    \n\
    \n  \
    \n\
    \n     :if ((\$sendtest=yes)&&[:pick \$content (\$pos1+11)] = \"d\") do={\
    \n\
    \n\
    \n\
    \n     :do {(\$changepassword&&\$timeoutsendsms&&\$sendsms&&\$putpasschange)} on-error={};\
    \n\
    \n        \
    \n\
    \n         }\
    \n\
    \n        }\
    \n\
    \n\
    \n\
    \n       }\
    \n\
    \n\
    \n\
    \n      }\
    \n\
    \n     }\
    \n\
    \n\
    \n\
    \n      /system logging action set userman memory-lines=1;\
    \n\
    \n      :delay 1\
    \n\
    \n      /system logging action set userman memory-lines=1000;"
/tool user-manager database set db-path=user-manager
/tool user-manager router add coa-port=1700 customer=admin disabled=no ip-address=10.1.1.1 log=auth-ok,auth-fail,acct-ok,acct-fail name=testhotspot shared-secret=PassWord123 use-coa=no
/tool user-manager user add customer=admin disabled=no ipv6-dns=:: password=PassWord123 shared-users=5 username=test wireless-enc-algo=none wireless-enc-key="" wireless-psk=""


File: /Hotspot + asterisk + sms\соглашение.txt
Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. 

Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других пользователей сети Интернет. 

Правила пользования Услугами

Принимаемые обозначения

"Исполнитель" - оператор ЗАО «Максима Телеком» 

"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие техническую возможность их получать. 
ООО "Компания"
1.При пользовании Услугами запрещается: 

1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании Услуг. 

1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. 

1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого не предназначенные. 

Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов или сообщений.

Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее ограничение никоим образом не имеет отношения к системе электронной подписки.

1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159 "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".

1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или иначе, противоречит российскому или международному праву.

1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие вредные компоненты.

1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения или другой продукции).

1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами Услуги также являются объектом авторских и других прав.

1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или владельцами этих ресурсов.

1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного Исполнителем.

1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом виде в рамках пользования Услуг.

Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно отказаться от его использования.

2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной почты (за исключением случаев, предусмотренных законом).

Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом, требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг, либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были или могут быть нарушены.

3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя, являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.

4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством Российской Федерации для отдельных категорий граждан.

© ООО "Компания", 2018

File: /Hotspot sms\hotspot\.idea\mikrotik.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$" />
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>

File: /Hotspot sms\hotspot\.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /Hotspot sms\hotspot\.idea\workspace.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ChangeListManager">
    <list default="true" id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
    <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />
    <option name="TRACKING_ENABLED" value="true" />
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="FileEditorManager">
    <leaf SIDE_TABS_SIZE_LIMIT_KEY="300">
      <file leaf-file-name="login.html" pinned="false" current-in-tab="true">
        <entry file="file://$PROJECT_DIR$/login.html">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="239">
              <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
              <folding>
                <element signature="e#1605#1819#0" expanded="false" />
                <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
                <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
              </folding>
            </state>
          </provider>
        </entry>
      </file>
      <file leaf-file-name="form.css" pinned="false" current-in-tab="false">
        <entry file="file://$PROJECT_DIR$/css/form.css">
          <provider selected="true" editor-type-id="text-editor">
            <state relative-caret-position="135">
              <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
              <folding />
            </state>
          </provider>
        </entry>
      </file>
    </leaf>
  </component>
  <component name="FileTemplateManagerImpl">
    <option name="RECENT_TEMPLATES">
      <list>
        <option value="CSS File" />
        <option value="HTML File" />
      </list>
    </option>
  </component>
  <component name="FindInProjectRecents">
    <findStrings>
      <find>wid</find>
    </findStrings>
  </component>
  <component name="GradleLocalSettings">
    <option name="externalProjectsViewState">
      <projects_view />
    </option>
  </component>
  <component name="IdeDocumentHistory">
    <option name="CHANGED_PATHS">
      <list>
        <option value="$PROJECT_DIR$/css.css" />
        <option value="$PROJECT_DIR$/img/arrow.svg" />
        <option value="$PROJECT_DIR$/img/number.svg" />
        <option value="$PROJECT_DIR$/css/form.css" />
        <option value="$PROJECT_DIR$/index.html" />
        <option value="$PROJECT_DIR$/login.html" />
      </list>
    </option>
  </component>
  <component name="JsBuildToolGruntFileManager" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsBuildToolPackageJson" detection-done="true" sorting="DEFINITION_ORDER" />
  <component name="JsGulpfileManager">
    <detection-done>true</detection-done>
    <sorting>DEFINITION_ORDER</sorting>
  </component>
  <component name="PhpWorkspaceProjectConfiguration" backward_compatibility_performed="true" />
  <component name="ProjectFrameBounds">
    <option name="x" value="248" />
    <option name="y" value="22" />
    <option name="width" value="949" />
    <option name="height" value="731" />
  </component>
  <component name="ProjectInspectionProfilesVisibleTreeState">
    <entry key="Project Default">
      <profile-state>
        <expanded-state>
          <State>
            <id />
          </State>
          <State>
            <id>Abstraction issuesJava</id>
          </State>
          <State>
            <id>ActionScript specificJavaScript</id>
          </State>
          <State>
            <id>Android</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Accessibility</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Chrome OS</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Correctness &gt; Messages</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Internationalization &gt; Bidirectional Text</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Lint</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Performance</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Security</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Icons</id>
          </State>
          <State>
            <id>Android &gt; Lint &gt; Usability &gt; Typography</id>
          </State>
          <State>
            <id>Android Lint for Kotlin</id>
          </State>
          <State>
            <id>Ant inspections</id>
          </State>
          <State>
            <id>Application Server Specific Inspections</id>
          </State>
          <State>
            <id>ArquillianJava</id>
          </State>
          <State>
            <id>BashSupport</id>
          </State>
          <State>
            <id>Batch Applications Issues</id>
          </State>
          <State>
            <id>Bean Validation issues</id>
          </State>
          <State>
            <id>CDI(Contexts and Dependency Injection) issues</id>
          </State>
          <State>
            <id>CSS</id>
          </State>
          <State>
            <id>Class metricsJava</id>
          </State>
          <State>
            <id>Class structureJava</id>
          </State>
          <State>
            <id>Cloning issuesJava</id>
          </State>
          <State>
            <id>Code SmellPHP</id>
          </State>
          <State>
            <id>Code StylePHP</id>
          </State>
          <State>
            <id>Code quality toolsCSS</id>
          </State>
          <State>
            <id>Code quality toolsJavaScript</id>
          </State>
          <State>
            <id>Code style issuesGo</id>
          </State>
          <State>
            <id>Code style issuesJava</id>
          </State>
          <State>
            <id>Code style issuesJavaScript</id>
          </State>
          <State>
            <id>CodeSpring CoreSpring</id>
          </State>
          <State>
            <id>CoffeeScript</id>
          </State>
          <State>
            <id>Control flow issuesGroovy</id>
          </State>
          <State>
            <id>Control flow issuesJava</id>
          </State>
          <State>
            <id>Control flow issuesJavaScript</id>
          </State>
          <State>
            <id>CorrectnessLintAndroid</id>
          </State>
          <State>
            <id>Cucumber Java</id>
          </State>
          <State>
            <id>DOM issuesJavaScript</id>
          </State>
          <State>
            <id>Data flow issuesJava</id>
          </State>
          <State>
            <id>Data flow issuesJavaScript</id>
          </State>
          <State>
            <id>Declaration redundancyGo</id>
          </State>
          <State>
            <id>Declaration redundancyJava</id>
          </State>
          <State>
            <id>Dependency issuesJava</id>
          </State>
          <State>
            <id>Encapsulation issuesJava</id>
          </State>
          <State>
            <id>Error handlingGroovy</id>
          </State>
          <State>
            <id>Error handlingJava</id>
          </State>
          <State>
            <id>Error handlingJavaScript</id>
          </State>
          <State>
            <id>Error handlingPHP</id>
          </State>
          <State>
            <id>Finalization issuesJava</id>
          </State>
          <State>
            <id>FlexUnit inspections</id>
          </State>
          <State>
            <id>GPathGroovy</id>
          </State>
          <State>
            <id>General</id>
          </State>
          <State>
            <id>GeneralGo</id>
          </State>
          <State>
            <id>GeneralJavaScript</id>
          </State>
          <State>
            <id>GeneralPHP</id>
          </State>
          <State>
            <id>Go</id>
          </State>
          <State>
            <id>Google App Engine</id>
          </State>
          <State>
            <id>Google Web Toolkit issues</id>
          </State>
          <State>
            <id>GrailsGroovy</id>
          </State>
          <State>
            <id>Groovy</id>
          </State>
          <State>
            <id>Guice Inspections</id>
          </State>
          <State>
            <id>HTML</id>
          </State>
          <State>
            <id>Haml</id>
          </State>
          <State>
            <id>Ignore</id>
          </State>
          <State>
            <id>Inheritance issuesJava</id>
          </State>
          <State>
            <id>Initialization issuesJava</id>
          </State>
          <State>
            <id>Internationalization issues</id>
          </State>
          <State>
            <id>Internationalization issuesJava</id>
          </State>
          <State>
            <id>Invalid elementsCSS</id>
          </State>
          <State>
            <id>J2ME issuesJava</id>
          </State>
          <State>
            <id>JBoss Seam issues</id>
          </State>
          <State>
            <id>JPA issues</id>
          </State>
          <State>
            <id>JSON</id>
          </State>
          <State>
            <id>JSP Inspections</id>
          </State>
          <State>
            <id>JUnit issuesJava</id>
          </State>
          <State>
            <id>Java</id>
          </State>
          <State>
            <id>Java 5Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 7Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 8Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java 9Java language level migration aidsJava</id>
          </State>
          <State>
            <id>Java EE issues</id>
          </State>
          <State>
            <id>Java interop issuesKotlin</id>
          </State>
          <State>
            <id>Java language level migration aidsJava</id>
          </State>
          <State>
            <id>JavaScript</id>
          </State>
          <State>
            <id>JavaScript validity issuesJavaScript</id>
          </State>
          <State>
            <id>Javadoc issuesJava</id>
          </State>
          <State>
            <id>Kotlin</id>
          </State>
          <State>
            <id>Kotlin Android</id>
          </State>
          <State>
            <id>Language Injection</id>
          </State>
          <State>
            <id>LintAndroid</id>
          </State>
          <State>
            <id>Logging issuesJava</id>
          </State>
          <State>
            <id>Manifest</id>
          </State>
          <State>
            <id>Maven</id>
          </State>
          <State>
            <id>Memory issuesJava</id>
          </State>
          <State>
            <id>Method metricsGroovy</id>
          </State>
          <State>
            <id>Modularization issuesJava</id>
          </State>
          <State>
            <id>Naming conventionsGroovy</id>
          </State>
          <State>
            <id>Naming conventionsJava</id>
          </State>
          <State>
            <id>Naming conventionsKotlin</id>
          </State>
          <State>
            <id>Node.jsJavaScript</id>
          </State>
          <State>
            <id>Numeric issuesJava</id>
          </State>
          <State>
            <id>OSGi</id>
          </State>
          <State>
            <id>Other problemsKotlin</id>
          </State>
          <State>
            <id>PHP</id>
          </State>
          <State>
            <id>Pattern Validation</id>
          </State>
          <State>
            <id>Performance issuesJava</id>
          </State>
          <State>
            <id>Plugin DevKit</id>
          </State>
          <State>
            <id>Portability issuesJava</id>
          </State>
          <State>
            <id>Potentially confusing code constructsGroovy</id>
          </State>
          <State>
            <id>Potentially confusing code constructsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsCSS</id>
          </State>
          <State>
            <id>Probable bugsCoffeeScript</id>
          </State>
          <State>
            <id>Probable bugsGo</id>
          </State>
          <State>
            <id>Probable bugsJava</id>
          </State>
          <State>
            <id>Probable bugsJavaScript</id>
          </State>
          <State>
            <id>Probable bugsKotlin</id>
          </State>
          <State>
            <id>Probable bugsPHP</id>
          </State>
          <State>
            <id>Properties Files</id>
          </State>
          <State>
            <id>Properties FilesJava</id>
          </State>
          <State>
            <id>RESTful Web Service</id>
          </State>
          <State>
            <id>Redundant constructsKotlin</id>
          </State>
          <State>
            <id>RegExp</id>
          </State>
          <State>
            <id>SQL</id>
          </State>
          <State>
            <id>Security issuesJava</id>
          </State>
          <State>
            <id>Serialization issuesJava</id>
          </State>
          <State>
            <id>SetupSpring CoreSpring</id>
          </State>
          <State>
            <id>Spelling</id>
          </State>
          <State>
            <id>Spring</id>
          </State>
          <State>
            <id>Spring BootSpring</id>
          </State>
          <State>
            <id>Spring CoreSpring</id>
          </State>
          <State>
            <id>Spring DataSpring</id>
          </State>
          <State>
            <id>Spring OSGiSpring</id>
          </State>
          <State>
            <id>Struts</id>
          </State>
          <State>
            <id>Struts 1Struts</id>
          </State>
          <State>
            <id>Struts 2Struts</id>
          </State>
          <State>
            <id>Style issuesKotlin</id>
          </State>
          <State>
            <id>StyleGroovy</id>
          </State>
          <State>
            <id>TestNGJava</id>
          </State>
          <State>
            <id>Threading issuesGroovy</id>
          </State>
          <State>
            <id>Threading issuesJava</id>
          </State>
          <State>
            <id>Thymeleaf</id>
          </State>
          <State>
            <id>Type compatibilityPHP</id>
          </State>
          <State>
            <id>TypeScript</id>
          </State>
          <State>
            <id>UI Form Problems</id>
          </State>
          <State>
            <id>UndefinedPHP</id>
          </State>
          <State>
            <id>Validity issuesGroovy</id>
          </State>
          <State>
            <id>Visibility issuesJava</id>
          </State>
          <State>
            <id>Web Services</id>
          </State>
          <State>
            <id>WebSocket issues</id>
          </State>
          <State>
            <id>XML</id>
          </State>
          <State>
            <id>XMLSpring CoreSpring</id>
          </State>
          <State>
            <id>XPath</id>
          </State>
        </expanded-state>
      </profile-state>
    </entry>
  </component>
  <component name="ProjectView">
    <navigator currentView="ProjectPane" proportions="" version="1">
      <flattenPackages />
      <showMembers />
      <showModules />
      <showLibraryContents />
      <hideEmptyPackages />
      <abbreviatePackageNames />
      <autoscrollToSource />
      <autoscrollFromSource />
      <sortByType />
      <manualOrder />
      <foldersAlwaysOnTop value="true" />
    </navigator>
    <panes>
      <pane id="Scratches" />
      <pane id="PackagesPane" />
      <pane id="ProjectPane">
        <subPane>
          <expand>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
            </path>
            <path>
              <item name="mikrotik" type="b2602c69:ProjectViewProjectNode" />
              <item name="mikrotik" type="462c0819:PsiDirectoryNode" />
              <item name="img" type="462c0819:PsiDirectoryNode" />
            </path>
          </expand>
          <select />
        </subPane>
      </pane>
      <pane id="AndroidView" />
      <pane id="Scope" />
    </panes>
  </component>
  <component name="PropertiesComponent">
    <property name="nodejs_interpreter_path.stuck_in_default_project" value="undefined stuck path" />
    <property name="settings.editor.selected.configurable" value="editor.preferences.fonts.default" />
    <property name="WebServerToolWindowFactoryState" value="false" />
    <property name="aspect.path.notification.shown" value="true" />
    <property name="last_opened_file_path" value="$PROJECT_DIR$" />
    <property name="list.type.of.created.stylesheet" value="CSS" />
    <property name="DefaultHtmlFileTemplate" value="HTML File" />
  </component>
  <component name="RecentsManager">
    <key name="MoveFile.RECENT_KEYS">
      <recent name="$PROJECT_DIR$/js" />
      <recent name="$PROJECT_DIR$/img" />
    </key>
  </component>
  <component name="RunDashboard">
    <option name="ruleStates">
      <list>
        <RuleState>
          <option name="name" value="ConfigurationTypeDashboardGroupingRule" />
        </RuleState>
        <RuleState>
          <option name="name" value="StatusDashboardGroupingRule" />
        </RuleState>
      </list>
    </option>
  </component>
  <component name="RunManager">
    <configuration default="true" type="Applet" factoryName="Applet">
      <option name="HTML_USED" value="false" />
      <option name="WIDTH" value="400" />
      <option name="HEIGHT" value="300" />
      <option name="POLICY_FILE" value="$APPLICATION_HOME_DIR$/bin/appletviewer.policy" />
      <module />
    </configuration>
    <configuration default="true" type="Application" factoryName="Application">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <option name="MAIN_CLASS_NAME" />
      <option name="VM_PARAMETERS" />
      <option name="PROGRAM_PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="ENABLE_SWING_INSPECTOR" value="false" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <module name="" />
      <envs />
    </configuration>
    <configuration default="true" type="JUnit" factoryName="JUnit">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="TEST_OBJECT" value="class" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <envs />
      <patterns />
    </configuration>
    <configuration name="login_old.html" type="JavascriptDebugType" factoryName="JavaScript Debug" temporary="true" nameIsGenerated="true" uri="http://localhost:63343/mikrotik/login_old.html" />
    <configuration default="true" type="Remote" factoryName="Remote">
      <option name="USE_SOCKET_TRANSPORT" value="true" />
      <option name="SERVER_MODE" value="false" />
      <option name="SHMEM_ADDRESS" value="javadebug" />
      <option name="HOST" value="localhost" />
      <option name="PORT" value="5005" />
    </configuration>
    <configuration default="true" type="TestNG" factoryName="TestNG">
      <extension name="coverage" enabled="false" merge="false" sample_coverage="true" runner="idea" />
      <module name="" />
      <option name="ALTERNATIVE_JRE_PATH_ENABLED" value="false" />
      <option name="ALTERNATIVE_JRE_PATH" />
      <option name="SUITE_NAME" />
      <option name="PACKAGE_NAME" />
      <option name="MAIN_CLASS_NAME" />
      <option name="METHOD_NAME" />
      <option name="GROUP_NAME" />
      <option name="TEST_OBJECT" value="CLASS" />
      <option name="VM_PARAMETERS" value="-ea" />
      <option name="PARAMETERS" />
      <option name="WORKING_DIRECTORY" value="%MODULE_WORKING_DIR%" />
      <option name="OUTPUT_DIRECTORY" />
      <option name="ANNOTATION_TYPE" />
      <option name="ENV_VARIABLES" />
      <option name="PASS_PARENT_ENVS" value="true" />
      <option name="TEST_SEARCH_SCOPE">
        <value defaultName="singleModule" />
      </option>
      <option name="USE_DEFAULT_REPORTERS" value="false" />
      <option name="PROPERTIES_FILE" />
      <envs />
      <properties />
      <listeners />
    </configuration>
    <configuration default="true" type="#org.jetbrains.idea.devkit.run.PluginConfigurationType" factoryName="Plugin">
      <module name="" />
      <option name="VM_PARAMETERS" value="-Xmx512m -Xms256m -XX:MaxPermSize=250m -ea" />
      <option name="PROGRAM_PARAMETERS" />
      <predefined_log_file id="idea.log" enabled="true" />
    </configuration>
    <recent_temporary>
      <list size="1">
        <item index="0" class="java.lang.String" itemvalue="JavaScript Debug.login_old.html" />
      </list>
    </recent_temporary>
  </component>
  <component name="ShelveChangesManager" show_recycled="false">
    <option name="remove_strategy" value="false" />
  </component>
  <component name="SvnConfiguration">
    <configuration />
  </component>
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="7562136b-f76e-4121-a488-1152bad563f6" name="Default" comment="" />
      <created>1521018748772</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1521018748772</updated>
      <workItem from="1521018751184" duration="14087000" />
      <workItem from="1521057296181" duration="563000" />
      <workItem from="1521058090953" duration="1147000" />
      <workItem from="1521059914099" duration="565000" />
    </task>
    <servers />
  </component>
  <component name="TimeTrackingManager">
    <option name="totallyTimeSpent" value="16362000" />
  </component>
  <component name="ToolWindowManager">
    <frame x="248" y="22" width="949" height="731" extended-state="0" />
    <editor active="true" />
    <layout>
      <window_info id="Palette" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />
      <window_info id="Palette&#9;" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Image Layers" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Analysis" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="true" content_ui="tabs" />
      <window_info id="Maven Projects" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Run" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="false" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Capture Tool" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.26571113" sideWeight="0.5" order="0" side_tool="false" content_ui="combo" />
      <window_info id="Docker" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32861635" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
      <window_info id="Database" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Learn" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="Ant Build" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
      <window_info id="UI Designer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
      <window_info id="Theme Preview" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.39937106" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
      <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="true" content_ui="tabs" />
      <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />
      <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Commander" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
      <window_info id="Hierarchy" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="combo" />
      <window_info id="Inspection" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="5" side_tool="false" content_ui="tabs" />
      <window_info id="Find" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
    </layout>
  </component>
  <component name="TypeScriptGeneratedFilesManager">
    <option name="version" value="1" />
  </component>
  <component name="VcsContentAnnotationSettings">
    <option name="myLimit" value="2678400000" />
  </component>
  <component name="XDebuggerManager">
    <breakpoint-manager>
      <option name="time" value="1" />
    </breakpoint-manager>
    <watches-manager />
  </component>
  <component name="editorHistoryManager">
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="0">
          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css.css" />
    <entry file="file://$PROJECT_DIR$/img/arrow.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/number.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/img/integrasky.svg">
      <provider selected="true" editor-type-id="images">
        <state />
      </provider>
    </entry>
    <entry file="file://$APPLICATION_HOME_DIR$/plugins/JavaScriptLanguage/jsLanguageServicesImpl/external/lib.dom.d.ts">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="119">
          <caret line="12227" column="4" lean-forward="false" selection-start-line="12227" selection-start-column="4" selection-end-line="12227" selection-end-column="4" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/css/form.css">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="135">
          <caret line="9" column="0" lean-forward="false" selection-start-line="9" selection-start-column="0" selection-end-line="9" selection-end-column="0" />
          <folding />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login_old.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="-545">
          <caret line="71" column="9" lean-forward="true" selection-start-line="60" selection-start-column="0" selection-end-line="71" selection-end-column="9" />
        </state>
      </provider>
    </entry>
    <entry file="file://$PROJECT_DIR$/login.html">
      <provider selected="true" editor-type-id="text-editor">
        <state relative-caret-position="239">
          <caret line="30" column="128" lean-forward="false" selection-start-line="30" selection-start-column="128" selection-end-line="30" selection-end-column="128" />
          <folding>
            <element signature="e#1605#1819#0" expanded="false" />
            <element signature="n#style#0;n#img#0;n#div#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#0;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
            <element signature="n#style#0;n#form#1;n#div#0;n#body#0;n#html#0;n#!!top" expanded="true" />
          </folding>
        </state>
      </provider>
    </entry>
  </component>
  <component name="masterDetails">
    <states>
      <state key="ProjectJDKs.UI">
        <settings>
          <last-edited>ruby-2.5.0-p0</last-edited>
          <splitter-proportions>
            <option name="proportions">
              <list>
                <option value="0.2" />
              </list>
            </option>
          </splitter-proportions>
        </settings>
      </state>
    </states>
  </component>
</project>

File: /Hotspot sms\hotspot\css\form.css
html, body {
    background: url("../img/background.png");
    height: 100%;
    min-height: 100px;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.logo {
    margin-bottom: 42px;
}

label {
    font-size: 12px;
    font-family: "Opium";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    background: #fff;
    border: solid 1px rgb(220, 224, 226);
    border-radius: 15px;
    padding: 42px;

}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    background-color: rgb(237, 245, 255);
    border: none;
    padding: 17px;
    margin: 7px;
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

.code input[type="text"], .form.already input[type="text"]{
    text-align: center !important;
}

.btn {

    font-size: 12px;
    font-family: "Roboto";
    color: rgb(255, 255, 255);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;

    border-radius: 5px;
    border: none;
    background-color: rgb(77, 161, 255);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;

    margin: 0 auto;

}

.disabled, .disabled:hover{
    background: #eee !important;
    cursor: auto;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.form_description {
    font-size: 16px;
    font-family: "Opium";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_group img {
    margin-right: 14px;
}

#modal_trigger {
    padding: 4px;
    cursor: pointer;
    color: #0421EA !important;
    text-decoration: underline;
}


File: /Hotspot sms\hotspot\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /Hotspot sms\hotspot\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Alexander A Kusakin <alexander.a.kusakin@gmail.com>">

    <link rel="stylesheet" href="./css/form.css">
    <link rel="stylesheet" href="./css/modal.css">

    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>

        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }

        jQuery(document).ready(function () {

            jQuery('#login').mask('+7-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');
                    jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                    jQuery('#username1').val(document.getElementById('login').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            jQuery('#login2').mask('+7-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {

                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/\+7/g, '').replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {

                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));

            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 3)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 3) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }

            });

            jQuery('#code').on('keyup', function (event) {

                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 3) {
                    jQuery(this).addClass('disabled').removeClass('active');
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
                }
            });

            jQuery('#has_code').on('click', function () {
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500)
                });
            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }

        });

    </script>
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="./img/integrasky.svg" alt="integrasky" width="200px" style="width:200px">
    </div>
    <!--<small class="form_description">Please log on to use the internet hotspot service</small>-->
    <form class="form login" id="login_form" style="display: none" method="get" name="sendin"
          action="$(link-login-only)" method="post">
        <label for="login">Введите номер</label>
        <br>
        <div class="input_group tel">
            <img src="./img/number.svg" alt="number">
            <input type="hidden" name="username" id="username1">
            <input type="text" id="login" placeholder="+7-(XXX)-XXX-XX-XX">
        </div>
        <br>
        <button class="btn next disabled">
            Далее
        </button>
    </form>

    <form class="form code" style="display: none" name="sendin" action="" method="post">
        <label for="code">Введите код</label>
        <br>
        <div class="input_group">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <input type="text" id="code" maxlength="8" placeholder="****">
        </div>
        <br>
        <input type="submit" class="btn disabled" value="Далее">
    </form>

    <form class="form already" style="display: none" name="sendin" action="" method="post">
        <label for="login2">Введите номер</label>
        <br>
        <div class="input_group tel">
            <input type="text" id="login2" placeholder="+7-(XXX)-XXX-XX-XX">
        </div>
        <label for="code">Введите код</label>
        <br>
        <div class="input_group">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" id="code2" maxlength="8" placeholder="****">
        </div>
        <br>
        <input type="submit" class="btn disabled" value="Далее">
    </form>

    <br><br>
    <small>Powered by MikroTik RouterOS</small>
    <a id="has_code" href="#">У меня уже есть код</a>
    <label id="modal_trigger" for="modal-trigger">Политика конфиденциальности</label>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
            <label for="modal-trigger" class="close">&#10006;</label>
            <h2>Политика конфиденциальности</h2>
            <p>Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь
                предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам
                доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. </p>
            <p>Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на
                пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других
                пользователей сети Интернет. </p>
            <p>Правила пользования Услугами</p>
            <p>Принимаемые обозначения</p>
            <p>"Исполнитель" - оператор ООО "компания" </p>
            <p>"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с
                любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие
                техническую возможность их получать. </p>
            <p>ООО "Компания"</p>
            <p>1.При пользовании Услугами запрещается: </p>
            <p>1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании
                Услуг. </p>
            <p>1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со
                стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. </p>
            <p>1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим
                пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес
                персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого
                не предназначенные. </p>
            <p>Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов
                или сообщений.</p>
            <p>Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса
                сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее
                ограничение никоим образом не имеет отношения к системе электронной подписки.</p>
            <p>1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты
                (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду
                действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную
                ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159
                "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный
                доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных
                программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
            <p>1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или
                иначе, противоречит российскому или международному праву.</p>
            <p>1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие
                вредные компоненты.</p>
            <p>1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих
                целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные
                посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения
                или другой продукции).</p>
            <p>1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг
                программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими
                правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять
                любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами
                Услуги также являются объектом авторских и других прав.</p>
            <p>1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или
                владельцами этих ресурсов.</p>
            <p>1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях
                получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного
                Исполнителем.</p>
            <p>1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия
                настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом
                виде в рамках пользования Услуг.</p>
            <p>Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно
                отказаться от его использования.</p>
            <p>2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной
                почты (за исключением случаев, предусмотренных законом).</p>
            <p>Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако
                Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через
                Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом,
                требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг,
                либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были
                или могут быть нарушены.</p>
            <p>3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую
                информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя,
                являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.</p>
            <p>4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством
                Российской Федерации для отдельных категорий граждан.</p>
            <p>© ООО "Компания", 2018</p>
        </div>
    </div>
</div>
</body>
</html>

File: /Hotspot sms\hotspot\login_old.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <title>internet hotspot > login</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="pragma" content="no-cache"/>
    <meta http-equiv="expires" content="-1"/>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>

    <link rel="stylesheet" href="./css/form.css">

    <style type="text/css">
        body {
            color: #737373;
            font-size: 10px;
            font-family: verdana;
        }

        textarea, input, select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active {
            color: #AAAAAA;
            text-decoration: none;
            font-size: 10px;
        }

        a:hover {
            border-bottom: 1px dotted #c1c1c1;
            color: #AAAAAA;
        }

        img {
            border: none;
        }

        td {
            font-size: 14px;
            color: #7A7A7A;
        }
    </style>

</head>

<body>
$(if chap-id)
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username"/>
    <input type="hidden" name="password"/>
    <input type="hidden" name="dst" value="$(link-orig)"/>
    <input type="hidden" name="popup" value="true"/>
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    <!--
    function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
        document.sendin.submit();
        return false;
    }

    //-->
</script>
$(endif)

<div align="center">
    <a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <!--<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br/>$(if-->
                <!--trial == 'yes')Free trial available, <a style="color: #FF8080"-->
                                                        <!--href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click-->
                    <!--here</a>.$(endif)-->
            <!--</div>-->
            <div>
                <small>Please log on to use the internet hotspot service</small>
            </div>
            <br/>
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0"
                   cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form name="login" action="$(link-login-only)" method="post"
                              $(if chap-id) onSubmit="return doLogin()" $(endif)>
                            <input type="hidden" name="dst" value="$(link-orig)"/>
                            <input type="hidden" name="popup" value="true"/>

                            <table width="100" style="background-color: #ffffff">
                                <tr>
                                    <td align="right">login</td>
                                    <td><input style="width: 80px" name="username" type="text" value="$(username)"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right">password</td>
                                    <td><input style="width: 80px" name="password" type="password"/></td>
                                </tr>
                                <tr>
                                    <td>&nbsp;</td>
                                    <td><input type="submit" value="OK"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr>
                    <td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img
                            src="/img/logobottom.png" alt="mikrotik"/></a></td>
                </tr>
            </table>

            <br/>
            <div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            $(if error)<br/>
            <div style="color: #FF8080; font-size: 9px">$(error)</div>
            $(endif)
        </td>
    </tr>
</table>

<script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
</script>
</body>
</html>


File: /Hotspot sms\hotspot.rsc
/interface bridge
add fast-forward=no name=bridge1
add comment=Hotspot fast-forward=no name=bridge2
add fast-forward=no name=lo
/interface wireless
set [ find default-name=wlan2 ] ssid=MikroTik
/interface list
add name=WAN
add name=local
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk eap-methods="" management-protection=\
    allowed mode=dynamic-keys name=guest supplicant-identity="" \
    wpa2-pre-shared-key=PassWord123
/interface wireless
set [ find default-name=wlan1 ] adaptive-noise-immunity=ap-and-client-mode \
    band=2ghz-onlyn country=russia3 default-forwarding=no disabled=no \
    distance=indoors hw-protection-mode=cts-to-self max-station-count=30 \
    mode=ap-bridge preamble-mode=long radio-name=Mikrotik-Training.ru-Guest \
    security-profile=guest ssid=Mikrotik-Training.ru-Guest
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot
add hotspot-address=10.5.50.1 html-directory=flash/hotspot name=hsprof1 \
    use-radius=yes
/ip hotspot user profile
set [ find default=yes ] on-login=":local nas [/system identity get name];\r\
    \n:local today [/system clock get date];\r\
    \n:local time1 [/system clock get time ];\r\
    \n:local ipuser [/ip hotspot active get [find user=\$user] address];\r\
    \n:local usermac [/ip hotspot active get [find user=\$user] mac-address]\r\
    \n:put \$today\r\
    \n:put \$time1\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n:local min [:pick \$time1 3 5]; \r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n:local mac1 [:pick \$usermac 0 2];\r\
    \n:local mac2 [:pick \$usermac 3 5];\r\
    \n:local mac3 [:pick \$usermac 6 8];\r\
    \n:local mac4 [:pick \$usermac 9 11];\r\
    \n:local mac5 [:pick \$usermac 12 14];\r\
    \n:local mac6 [:pick \$usermac 15 17];\r\
    \n:set \$usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6\
    })]\r\
    \n:put \$time1\r\
    \n/ip firewall address-list add list=\$today address=\"log-in.\$time1.\$us\
    er.\$usermac.\$ipuser\"\r\
    \n\r\
    \ndo {/tool e-mail send to=\"email@gmail.com\" subject=\"Login number:\
    \_\$user on \$nas\" body=\"Login number: \$user mac-address: \$usermac tim\
    e: \$time1 ip-address: \$ipuser\"} on-error={};" on-logout=":local nas [/s\
    ystem identity get name];\r\
    \n:local today [/system clock get date];\r\
    \n:local time1 [/system clock get time ];\r\
    \n:put \$today\r\
    \n:put \$time1\r\
    \n:local hour [:pick \$time1 0 2]; \r\
    \n:local min [:pick \$time1 3 5];\r\
    \n:local sec [:pick \$time1 6 8];\r\
    \n:set \$time1 [:put ({hour} . {min} . {sec})] \r\
    \n:put \$time1\r\
    \n/ip firewall address-list add list=\$today address=\"log-out.\$time1.\$u\
    ser\"\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=\"Logout number: \$\
    user on \$nas\" body=\"Logout number: \$user time: \$time1\""
/ip pool
add name=hs-pool-9 ranges=10.5.50.2-10.5.50.254
/ip dhcp-server
add address-pool=hs-pool-9 disabled=no interface=bridge2 lease-time=1h name=\
    dhcp1
/ip hotspot
add address-pool=hs-pool-9 disabled=no interface=bridge2 name=hotspot1 \
    profile=hsprof1
/system logging action
add name=hotspot target=memory
/tool user-manager customer
set admin access=\
    own-routers,own-users,own-profiles,own-limits,config-payment-gw
/tool user-manager profile
add name=hotspot name-for-users="" override-shared-users=off owner=admin \
    price=0 starts-at=logon validity=0s
/tool user-manager profile limitation
add address-list="" download-limit=0B group-name="" ip-pool="" name=unlimited \
    owner=admin transfer-limit=0B upload-limit=0B uptime-limit=0s
/interface bridge port
add bridge=bridge2 interface=wlan1
/ip neighbor discovery-settings
set discover-interface-list=WAN
/interface list member
add interface=ether1 list=WAN
add interface=ether2 list=local
add interface=bridge1 list=local
/ip address
add address=10.5.50.1/24 comment="hotspot network" interface=bridge2 network=\
    10.5.50.0
add address=10.11.11.1 interface=lo network=10.11.11.1
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1
/ip dhcp-server network
add address=10.5.50.0/24 comment="hotspot network" gateway=10.5.50.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip firewall address-list
add address=log-in.165846.9067634683.60F1894825C4.10.5.50.254 list=\
    mar/14/2018
add address=log-out.170409.9067634683 list=mar/14/2018
add address=log-in.170543.9067634683.60F1894825C4.10.5.50.254 list=\
    mar/14/2018
/ip firewall filter
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
add action=accept chain=forward comment=Established/related connection-state=\
    established,related
add action=accept chain=input connection-state=established,related
add action=drop chain=input comment=Invalid connection-state=invalid \
    in-interface-list=WAN
add action=drop chain=forward connection-state=invalid in-interface-list=WAN
add action=accept chain=input comment=Icmp in-interface-list=WAN protocol=\
    icmp
add action=accept chain=input comment=Winbox dst-port=8291 in-interface-list=\
    WAN protocol=tcp
add action=accept chain=input comment=Webfig dst-port=80 in-interface-list=\
    WAN protocol=tcp
add action=drop chain=input comment=Drop in-interface-list=WAN
add action=drop chain=forward in-interface-list=WAN
/ip firewall nat
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
add action=masquerade chain=srcnat comment="masquerade hotspot network" \
    out-interface-list=WAN src-address=10.5.50.0/24
add action=masquerade chain=srcnat out-interface-list=WAN
/ip hotspot user
add name=admin
add name=9067634683 password=1879
/radius
add accounting-backup=yes address=10.11.11.1 secret=PassWord123! service=\
    hotspot src-address=10.11.11.1
/system clock
set time-zone-name=Europe/Moscow
/system identity
set name=Mikrotik-Training.ru-Guest
/system logging
add action=hotspot topics=hotspot,debug,info,!account
/system scheduler
add interval=1d name=backup on-event="/system script run backup " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=mar/14/2018 start-time=13:41:01
add interval=30s name=hotspot on-event="/system script run hotspot" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=mar/14/2018 start-time=13:59:23
/system script
add name=hotspot owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    Search number in log hotspot\
    \n\
    \n:foreach line in=[/log find buffer=hotspot message~\"login failed\"] do=\
    {\
    \n :do {:local content [/log get \$line message];\
    \n  :put \$content;\
    \n  :local pos1 [:find \$content \" (\" 0];\
    \n  :put \$pos1;\
    \n  :if (\$pos1 != \" \") do={ \
    \n   :local uname \"\"; \
    \n   :local uname7 \"\";\
    \n   :local uname8 \"\";\
    \n   :local uname9 \"\";\
    \n   :local phone \"\"; \
    \n   :if ([:pick \$content (\$pos1-11)] = \"8\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time]; \
    \n    :local hour [:pick \$date 0 2]; \
    \n    :local min [:pick \$date 3 5]; \
    \n    :local sec [:pick \$date 6 8]; \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-5)];\
    \n    :put \$usernumber;\
    \n    :global pass 27394; \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber); \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524;\
    \n     }\
    \n    :put \$pass;\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={}; \
    \n    ##SMS.ru\
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool fetch url=\"https://gate.smsaero.ru/send/\\\?user=info@ast\"https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\\"} on-error={};\
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;    \
    \n    }\
    \n   :if ([:pick \$content (\$pos1-10)] = \"9\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time]; \
    \n    :local hour [:pick \$date 0 2]; \
    \n    :local min [:pick \$date 3 5]; \
    \n    :local sec [:pick \$date 6 8]; \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-5)];\
    \n    :put \$usernumber;\
    \n    :global pass 27394; \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber); \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524;\
    \n     }\
    \n    :put \$pass;\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname7;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={}; \
    \n    ##SMS.ru\
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool fetch url=\"https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\"} on-error={};\
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;    \
    \n    }\
    \n\
    \n   :if ([:pick \$content (\$pos1-11)] = \"7\") do={ \
    \n    :set uname [:pick \$content (\$pos1-10) (\$pos1-0)];  \
    \n    :put \$uname;\
    \n    :set uname7 [:put (\"7\" . {\$uname})]\
    \n    :set uname8 [:put (\"8\" . {\$uname})]\
    \n    :put \$uname7\
    \n    :put \$uname8\
    \n    #Password generation \
    \n    :local date [/system clock get time] \
    \n    :local hour [:pick \$date 0 2] \
    \n    :local min [:pick \$date 3 5] \
    \n    :local sec [:pick \$date 6 8] \
    \n    :local usernumber [:pick \$content (\$pos1-7) (\$pos1-4)];\
    \n    :global pass 27394 \
    \n    :set pass (\$hour * \$min * \$sec - \$usernumber) \
    \n    :if (\$pass = 0) do={ \
    \n     :set pass 6524 \
    \n     } \
    \n    :put \$pass\
    \n    #Add user to hotspot / user-manager \
    \n\
    \n    do {/ip hotspot user add name=\$uname} on-error={};\
    \n    do {/ip hotspot user set password=\$pass numbers=[find name=\$uname]\
    } on-error={};\
    \n    do {/tool user-manager user add username=\$uname password=\$pass cus\
    tomer=admin copy-from=test disabled=no phone=\$uname;} on-error={};\
    \n    do {/tool user-manager user set password=\$pass number=[find usernam\
    e=\$uname]} on-error={};\
    \n    ##SMS \
    \n    #do {/tool fetch url=\"http://sms.ru/sms/send\?api_id=!!!!!!!!!!!!!!\
    !!!!!!!!!!!!!!!!!!!!&to=\$uname&text=\$pass\"} on-error={}; \
    \n    do {/tool sms send usb1 phone-number=\"\$uname7\" message=\"login \$\
    uname password \$pass\"} on-error={};\
    \n    do {/tool fetch url=\""https://gate.smsaero.ru/send/\\\?user=login&password=UID&to=\$uname7&text=password+\
    \$pass&from=name\"} on-error={};\
    \n    #Email\
    \n    do {/tool e-mail send to=\"email@gmail.com\" subject=\"Login \$u\
    name password \$pass\" body=\"Login \$uname password \$pass\"} on-error={}\
    ;  \
    \n\
    \n    }\
    \n  }\
    \n }\
    \n}\
    \n\
    \n\
    \n\
    \n# Clear hostpot log\
    \n\
    \n/system logging action set hotspot memory-lines=1;\
    \n/system logging action set hotspot memory-lines=1000;"
add name=backup owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    export compact file=auto_backup_user-manager;\r\
    \n/system backup save name=auto_backup_user-manager.backup;\r\
    \n:if ( [ /file find name=auto_backup_user-manager.umb ] != \"\" ) do={\r\
    \n/file remove auto_backup_user-manager.umb;\r\
    \n};\r\
    \n/tool user-manager database save name=auto_backup_user-manager;\r\
    \n/delay delay-time=60;\r\
    \n\r\
    \n\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Export Script Us\
    er Manager \".[ /system clock get date ].\" \".[ /system clock get time ])\
    \_file=auto_backup_user-manager.rsc;\r\
    \n/delay delay-time=60;\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Backup Config Us\
    er Manager \".[ /system clock get date ].\" \".[ /system clock get time ])\
    \_file=auto_backup_user-manager.backup;\r\
    \n/delay delay-time=60;\r\
    \n/tool e-mail send to=\"email@gmail.com\" subject=(\"Backup Database \
    User Manager \".[ /system clock get date ].\" \".[ /system clock get time \
    ]) file=auto_backup_user-manager.umb;\r\
    \n/delay delay-time=60;"
/tool e-mail
set address=smtp.gmail.com from=email@gmail.com password=\
    PassWord port=587 start-tls=yes user=email@gmail.com
/tool mac-server
set allowed-interface-list=local
/tool mac-server mac-winbox
set allowed-interface-list=local
/tool user-manager database
set db-path=flash/user-manager
/tool user-manager profile profile-limitation
add from-time=0s limitation=unlimited profile=hotspot till-time=23h59m59s \
    weekdays=sunday,monday,tuesday,wednesday,thursday,friday,saturday
/tool user-manager router
add coa-port=1700 customer=admin disabled=no ip-address=10.11.11.1 log=\
    auth-fail name=Mikrotik-Training.ru-Guest shared-secret=PassWord123! \
    use-coa=no
/tool user-manager user
add customer=admin disabled=no password=test121212313123132312 shared-users=1 \
    username=test wireless-enc-algo=none wireless-enc-key="" wireless-psk=""
add customer=admin disabled=no password=1879 phone=79067634683 shared-users=1 \
    username=9011111111 wireless-enc-algo=none wireless-enc-key="" \
    wireless-psk=""


File: /Hotspot sms\Log-in script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-login 

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:local ipuser [/ip hotspot active get [find user=$user] address];

:local usermac [/ip hotspot active get [find user=$user] mac-address]

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5]; 

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:local mac1 [:pick $usermac 0 2];

:local mac2 [:pick $usermac 3 5];

:local mac3 [:pick $usermac 6 8];

:local mac4 [:pick $usermac 9 11];

:local mac5 [:pick $usermac 12 14];

:local mac6 [:pick $usermac 15 17];

:set $usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6})]

:put $time1

/ip firewall address-list add list=$today address="log-in.$time1.$user.$usermac.$ipuser"



do {/tool e-mail send to="email@gmail.com" subject="Login number: $user on $nas" body="Login number: $user mac-address: $usermac time: $time1 ip-address: $ipuser"} on-error={};


File: /Hotspot sms\Log-out script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-logout

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:put $today

:put $time1

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5];

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})] 

:put $time1

/ip firewall address-list add list=$today address="log-out.$time1.$user"

/tool e-mail send to="email@gmail.com" subject="Logout number: $user on $nas" body="Logout number: $user time: $time1"

File: /Hotspot sms\script backup.txt
/export compact file=auto_backup_user-manager;
/system backup save name=auto_backup_user-manager.backup;
:if ( [ /file find name=auto_backup_user-manager.umb ] != "" ) do={
/file remove auto_backup_user-manager.umb;
};
/tool user-manager database save name=auto_backup_user-manager;
/delay delay-time=60;


/tool e-mail send to="email@gmail.com" subject=("Export Script User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.rsc;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Config User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.backup;
/delay delay-time=60;
/tool e-mail send to="email@gmail.com" subject=("Backup Database User Manager ".[ /system clock get date ]." ".[ /system clock get time ]) file=auto_backup_user-manager.umb;
/delay delay-time=60;

File: /Hotspot sms\script.txt
#Search number in log hotspot

:foreach line in=[/log find buffer=hotspot message~"login failed"] do={
 :do {:local content [/log get $line message];
  :put $content;
  :local pos1 [:find $content " (" 0];
  :put $pos1;
  :if ($pos1 != " ") do={ 
   :local uname ""; 
   :local uname7 "";
   :local uname8 "";
   :local uname9 "";
   :local phone ""; 
   :if ([:pick $content ($pos1-11)] = "8") do={ 
    :set uname [:pick $content ($pos1-10) ($pos1-0)];  
    :put $uname;
    :set uname7 [:put ("7" . {$uname})]
    :set uname8 [:put ("8" . {$uname})]
    :put $uname7
    :put $uname8
    #Password generation 
    :local date [/system clock get time]; 
    :local hour [:pick $date 0 2]; 
    :local min [:pick $date 3 5]; 
    :local sec [:pick $date 6 8]; 
    :local usernumber [:pick $content ($pos1-7) ($pos1-5)];
    :put $usernumber;
    :global pass 27394; 
    :set pass ($hour * $min * $sec - $usernumber); 
    :if ($pass = 0) do={ 
     :set pass 6524;
     }
    :put $pass;
    #Add user to hotspot / user-manager 

    do {/ip hotspot user add name=$uname} on-error={};
    do {/ip hotspot user set password=$pass numbers=[find name=$uname]} on-error={};
    do {/tool user-manager user add username=$uname password=$pass customer=admin copy-from=test disabled=no phone=$uname;} on-error={};
    do {/tool user-manager user set password=$pass number=[find username=$uname]} on-error={}; 
    ##SMS.ru
    #do {/tool fetch url="http://sms.ru/sms/send?api_id=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&to=$uname&text=$pass"} on-error={}; 
    do {/tool fetch url="https://gate.smsaero.ru/send/\?user=info@1.ru&password=1212121212das&to=$uname7&text=password+$pass&from=name=Asterconf"} on-error={};
    do {/tool sms send usb1 phone-number="$uname7" message="login $uname password $pass"} on-error={};
    #Email
    do {/tool e-mail send to="email@gmail.com" subject="Login $uname password $pass" body="Login $uname password $pass"} on-error={};    
    }
   :if ([:pick $content ($pos1-10)] = "9") do={ 
    :set uname [:pick $content ($pos1-10) ($pos1-0)];  
    :put $uname;
    :set uname7 [:put ("7" . {$uname})]
    :set uname8 [:put ("8" . {$uname})]
    :put $uname7
    :put $uname8
    #Password generation 
    :local date [/system clock get time]; 
    :local hour [:pick $date 0 2]; 
    :local min [:pick $date 3 5]; 
    :local sec [:pick $date 6 8]; 
    :local usernumber [:pick $content ($pos1-7) ($pos1-5)];
    :put $usernumber;
    :global pass 27394; 
    :set pass ($hour * $min * $sec - $usernumber); 
    :if ($pass = 0) do={ 
     :set pass 6524;
     }
    :put $pass;
    #Add user to hotspot / user-manager 

    do {/ip hotspot user add name=$uname} on-error={};
    do {/ip hotspot user set password=$pass numbers=[find name=$uname]} on-error={};
    do {/tool user-manager user add username=$uname password=$pass customer=admin copy-from=test disabled=no phone=$uname7;} on-error={};
    do {/tool user-manager user set password=$pass number=[find username=$uname]} on-error={}; 
    ##SMS.ru
    #do {/tool fetch url="http://sms.ru/sms/send?api_id=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&to=$uname&text=$pass"} on-error={}; 
    do {/tool fetch url="https://gate.smsaero.ru/send/\?user=info@1.ru&password=1212121212das&to=$uname7&text=password+$pass&from=name"} on-error={};
    do {/tool sms send usb1 phone-number="$uname7" message="login $uname password $pass"} on-error={};
    #Email
    do {/tool e-mail send to="email@gmail.com" subject="Login $uname password $pass" body="Login $uname password $pass"} on-error={};    
    }

   :if ([:pick $content ($pos1-11)] = "7") do={ 
    :set uname [:pick $content ($pos1-10) ($pos1-0)];  
    :put $uname;
    :set uname7 [:put ("7" . {$uname})]
    :set uname8 [:put ("8" . {$uname})]
    :put $uname7
    :put $uname8
    #Password generation 
    :local date [/system clock get time] 
    :local hour [:pick $date 0 2] 
    :local min [:pick $date 3 5] 
    :local sec [:pick $date 6 8] 
    :local usernumber [:pick $content ($pos1-7) ($pos1-4)];
    :global pass 27394 
    :set pass ($hour * $min * $sec - $usernumber) 
    :if ($pass = 0) do={ 
     :set pass 6524 
     } 
    :put $pass
    #Add user to hotspot / user-manager 

    do {/ip hotspot user add name=$uname} on-error={};
    do {/ip hotspot user set password=$pass numbers=[find name=$uname]} on-error={};
    do {/tool user-manager user add username=$uname password=$pass customer=admin copy-from=test disabled=no phone=$uname;} on-error={};
    do {/tool user-manager user set password=$pass number=[find username=$uname]} on-error={};
    ##SMS 
    #do {/tool fetch url="http://sms.ru/sms/send?api_id=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&to=$uname&text=$pass"} on-error={}; 
    do {/tool sms send usb1 phone-number="$uname7" message="login $uname password $pass"} on-error={};
    do {/tool fetch url="https://gate.smsaero.ru/send/\?user=info@1.ru&password=1212121212das&to=$uname7&text=password+$pass&from=name=Asterconf"} on-error={};
    #Email
    do {/tool e-mail send to="email@gmail.com" subject="Login $uname password $pass" body="Login $uname password $pass"} on-error={};  

    }
  }
 }
}



# Clear hostpot log

/system logging action set hotspot memory-lines=1;
/system logging action set hotspot memory-lines=1000;

File: /Hotspot sms\соглашение.txt
Вы подключились к сети беспроводного доступа к Интернет, развернутой компанией ООО "Компания". Стремясь предоставить своим клиентам широкий спектр услуг высочайшего качества, ООО "Компания" предлагает Вам доступ к сети Интернет и различным приложениям, на базе сети Интернет, по технологии Wi-Fi. 

Оказание услуг осуществляется на основании "Правил пользования услугами", накладывающих ограничения на пользователей по совершению действий, которые могут ограничить или ущемить свободы и права других пользователей сети Интернет. 

Правила пользования Услугами

Принимаемые обозначения

"Исполнитель" - оператор ЗАО «Максима Телеком» 

"Пользователь" - любое совершеннолетнее лицо (группа таких лиц) или организация (учреждение, фирма с любой формой собственности и т.п.), являющиеся юридическими лицами, нуждающиеся в Услугах и имеющие техническую возможность их получать. 
ООО "Компания"
1.При пользовании Услугами запрещается: 

1.1. Ограничивать доступ других Пользователей или препятствовать другим Пользователям в использовании Услуг. 

1.2. Посылать рекламные, информационные и другие материалы без согласия (или при отсутствии заявки) со стороны адресатов, а также в несоответствующие по тематике электронные издания и конференции. 

1.3. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим пользователям сети интернет, кроме случаев, когда адресаты согласны получить эти материалы, как на адрес персональной электронной почты, так и через электронные издания и конференции общего доступа, для этого не предназначенные. 

Примечание 1. Исполнитель оставляет за собой право на показ рекламных, информационных и других материалов или сообщений.

Примечание 2. Под "веерной" (массовой) рассылкой понимается отправка одновременно в два и более адреса сообщений, на получение которых у Пользователя не имеется согласия владельцев этих адресов. Настоящее ограничение никоим образом не имеет отношения к системе электронной подписки.

1.4. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты (узлы), программы, базы данных и иные составляющие элементы сети Исполнителя, интернет, имея в виду действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159 "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".

1.5. Посылать или делать доступной по сети интернет любую информацию, распространение которой, так или иначе, противоречит российскому или международному праву.

1.6. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие вредные компоненты.

1.7. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные посредством Услуг (если это явно не разрешено поставщиком подобной информации, программного обеспечения или другой продукции).

1.8. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством Услуг программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими правами, без разрешения владельца или законного правообладателя; посылать, передавать или распространять любым способом любую составляющую предоставляемой Услуг или созданные на их основе работы, так как сами Услуги также являются объектом авторских и других прав.

1.9. Нарушать правила использования любых ресурсов сети интернет, установленные Исполнителем и/или владельцами этих ресурсов.

1.10. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях получения Услуги, за исключением программного обеспечения, предоставленного либо одобренного Исполнителем.

1.11. В соответствии с требованиями действующего законодательства Пользователем, принимая условия настоящего Соглашения выражает предварительное согласие на получение рекламы в любой форме и в любом виде в рамках пользования Услуг.

Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно отказаться от его использования.

2. Исполнитель не будет преднамеренно просматривать или разглашать любые частные сообщения электронной почты (за исключением случаев, предусмотренных законом).

Исполнитель не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако Пользователь принимает условие, что Исполнитель имеет право периодически отслеживать проходящую через Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом, требованиями уполномоченных государственных учреждений, либо для нормального функционирования Услуг, либо для защиты Исполнителя, иных Пользователей, а равно третьих лиц, чьи законные права и интересы были или могут быть нарушены.

3. Исполнитель оставляет за собой право отказать в пересылке или удалять со своих серверов любую информацию или материалы полностью или частично, если они, исключительно с точки зрения Исполнителя, являются неприемлемыми, нежелательными или нарушают настоящее Соглашение.

4. Пользователи при получении Услуг пользуются льготами, предусмотренными действующим законодательством Российской Федерации для отдельных категорий граждан.

© ООО "Компания", 2018

File: /README.md
# mikrotik-hotspot-sms

**Hotspot для соблюдения законодательства РФ на mikrotik**
*  Hotspot SMS - отправка SMS с mikroikt для авторизации по sms // Вебинар по теме - https://youtu.be/1wFJbZl0bFE
*  Hotspot + asterisk - авторизация с помощью звонка на asterisk // Вебинар по теме - https://www.youtube.com/watch?v=gplWwlvnl_I

Самый новый и полный скрипт находится в папке Hotspot + asterisk + sms.  Требуется usermanager. Возможно использовать без asterisk - просто удалите кнопку авторизации через asterisk из login.html 


