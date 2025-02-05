# Repository Information
Name: mikrotik-installer

# Directory Structure
Directory structure:
└── github_repos/mikrotik-installer/
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
    │   │       ├── pack-3b0ec5b3f7f75c173bc1fcddc862bf86fcdfa4e7.idx
    │   │       └── pack-3b0ec5b3f7f75c173bc1fcddc862bf86fcdfa4e7.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── install-mikrotik.sh
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
	url = https://github.com/LaKing/mikrotik-installer.git
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
0000000000000000000000000000000000000000 28eda151809028e73879be86088175662dca886d vivek-dodia <vivek.dodia@icloud.com> 1738606407 -0500	clone: from https://github.com/LaKing/mikrotik-installer.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 28eda151809028e73879be86088175662dca886d vivek-dodia <vivek.dodia@icloud.com> 1738606407 -0500	clone: from https://github.com/LaKing/mikrotik-installer.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 28eda151809028e73879be86088175662dca886d vivek-dodia <vivek.dodia@icloud.com> 1738606407 -0500	clone: from https://github.com/LaKing/mikrotik-installer.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
28eda151809028e73879be86088175662dca886d refs/remotes/origin/master


File: /.git\refs\heads\master
28eda151809028e73879be86088175662dca886d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /install-mikrotik.sh
#!/bin/bash
#
# Mikrotik installer script
#
# D250 Laboratories / D250.hu 2014-2019
# Author: István király
# LaKing@D250.hu
# 
## download, update with:
# curl http://d250.hu/scripts/install-mikrotik.sh > install.sh 
## run with bash 
# && bash install.sh
#

## Timestamp
readonly NOW="$(date +%Y.%m.%d-%H:%M:%S)"
## logfile
readonly LOG="$(pwd)/install-mikrotik.log"
## current dir
readonly DIR="$(pwd)"
## temporal backup and work directory
readonly TMP="/temp"
## A general message string 
readonly MSG="## D250 Laboratories $0 @ $NOW"
## Debugging helper
DEBUG=false
## constants

## constants for use everywhere
readonly RED='\e[31m'
readonly GREEN='\e[32m'
readonly YELLOW='\e[33m'
readonly BLUE='\e[34m'
readonly GRAY='\e[37m'
readonly CLEAR='\e[0m'

## Lablib functions

function msg {
    ## message for the user
    echo -e "${GREEN}$*${CLEAR}"
}

function ntc {
    ## notice for the user
    echo -e "${YELLOW}$*${CLEAR}"
}


function log {
    ## create a log entry
    echo -e "${YELLOW}$1${CLEAR}"
    echo "$NOW: $*" >> "$LOG"
}

## silent log
function logs {
    ## create a log entry
    echo "$NOW: $*" >> "$LOG"
}
dbgc=0
function dbg {
    ((dbgc++))
    ## short debug message if debugging is on
    if $DEBUG
    then
        echo -e "${YELLOW}DEBUG #$dbgc ${BASH_SOURCE[1]}#$BASH_LINENO ${FUNCNAME[1]} ${RED} $* ${CLEAR}"
    fi
}
function debug {
    ## tracing debug message
    echo -e "${YELLOW}DEBUG ${BASH_SOURCE[1]}#$BASH_LINENO ${FUNCNAME[1]} ${RED} $*${CLEAR}"
}
function err {
    ## error message
    echo -e "$NOW ERROR ${RED}$*${CLEAR}" >> "$LOG"
    echo -e "${RED}$*${CLEAR}" >&2
}

function run {
    local signum='$'
    if [ "$USER" == root ]
    then
        signum='#'
    fi
    local WDIR
    WDIR="$(basename "$PWD")"
    echo -e "${BLUE}[$USER@${HOSTNAME%%.*} ${WDIR/#$HOME/\~}]$signum ${YELLOW}$*${CLEAR}"

    # shellcheck disable=SC2048
    $*
    eyif "command '$*' returned with an error"
}

## exit if failed
function exif {
    local exif_code="$?"
    if [ "$exif_code" != "0" ]
    then
        if $DEBUG
        then
            ## the first in stack is what we are looking for. (0th is this function itself)
            err "ERROR $exif_code @ ${BASH_SOURCE[1]}#$BASH_LINENO ${FUNCNAME[1]} :: $*"
        else
            err "$*"
        fi
        exit "$exif_code";
    fi
}

## extra yell if failed
function eyif {
    local eyif_code="$?"
    if [ "$eyif_code" != "0" ]
    then
        if $DEBUG
        then
            err "ERROR $eyif_code @ ${BASH_SOURCE[1]}#$BASH_LINENO ${FUNCNAME[1]} :: $*"
        else
            err "$*"
        fi
    fi
}

## Any enemy in sight? :)
clear


msg "$MSG"
mkdir -p "$TMP"




a=0
n=0
h=0

## Basic helper functions

function question {
    ## Add to the question que asq, with counter a

    (( a++ ))
    asq[$a]=$1
    hlp[$a]=$2
    def[$a]=$3
}

function run_in_que {
    ## run the question que. Default answer is no, y is the only other option
    ## y-answered question are added to the executation que
    echo ''
    echo "${hlp[h]}"

    key=
    echo -n "$1? " | tr '_' ' '

    default_key=${def[h]:0:1}
    default_str="y/N"

    if [[ $default_key == y* ]]; then
      default_str="Y/n"
    else
      default_str="y/N"
    fi
     # shellcheck disable=SC2034
    read -s -r -p " [$default_str] " -n 1 -i "y" key

    ## Check for default action
    if [ ${#key} -eq 0 ]; then
     ## Enter was hit"
     key=$default_key
    fi

    ## Makre it an ordenary string
    if [[ $key == y ]]; then
     key="yes"
    else
     key="no";
    fi

    echo $key

    ## Que the action if yes
    if [[ $key == y* ]]; then
      echo "$1" >> "$LOG"
      (( n++ ))
      que[$n]=$1 
    fi
}

function bak {
    ## create a backup of the file, with the same name, same location .bak extension
    ## filename=$1
    echo "$MSG" >> "$1.bak"
    cat "$1" >> "$1.bak"
    #echo "$1 has a .bak file"
}

function set_file {
    ## cerate a file with the content overwriting everything
    ## filename=$1 content=$2

    if [[ -f $1 ]]
    then 
          bak "$1"
    fi
    echo "creating $1"
    echo "$2" > "$1"
}

function sed_file {
    ## used to replace a line in a file
    ## filename=$1 old line=$2 new line=$3
    bak "$1"
    cat "$1" > "$1.tmp"
    sed "s|$2|$3|" "$1.tmp" > "$1"
    rm "$1.tmp"
}

function add_conf {
    ## check if the content string is present, and add if necessery. Single-line content only.
    ## filename=$1 content=$2

    if [[ -f $1 ]]
    then 
          bak "$1"
    fi

    if grep -q "$2" "$1"
    then
     echo "$1 already has $2"
    else
     echo "adding $2"
     echo "$2" >> "$1"
    fi
}



function finalize {
## run the que's, and do the job's. This is the main function.
  msg "=== Confirmation for ${#asq[*]} commands. [Ctrl-C to abort] ==="
  for item in ${asq[*]}
  do
    (( h++ ))
    run_in_que "$item" #?
  done

  msg "=== Running the Que of ${#que[*]} commands. ==="
  for item in ${que[*]}
  do
    msg "== $item started! =="
    ntc "$item"
    $item
    msg "== $item finished =="
  done

  msg "=== Post-processing tasks ===";
  for item in ${que[*]}
  do
    if [ "$item" == "install_and_finetune_gnome_desktop" ] 
    then
     # run this graphical tool at the end
     if [ -z "$USER" ]; then echo "No user to tune gnome, skipping question." >> "$LOG"; else
        ntc "Starting the gnome Tweak tool."
        su "$USER" -c gnome-tweaks
     fi
    fi 
  done
  echo "Finished. $MSG" >> "$LOG"
}

ROUTEROS_USER=$(echo $1 | cut -d "@" -f 1)
ROUTEROS_HOST=$(echo $1 | cut -d "@" -f 2)

### You can override this here, especially if you use custom ports.
#ROUTEROS_USER=$1
#ROUTEROS_HOST=$2
#ROUTEROS_SSH_PORT=$3

if ! [[ $ROUTEROS_HOST ]]
then
    ROUTEROS_HOST="192.168.88.1"
fi

if ! [[ $ROUTEROS_USER ]]
then
    ROUTEROS_USER="admin"
fi

if ! [[ $ROUTEROS_SSH_PORT ]]
then
    ROUTEROS_SSH_PORT="22"
fi

log "Connecting to $ROUTEROS_HOST.."

echo "ssh $ROUTEROS_USER@$ROUTEROS_HOST -p $ROUTEROS_SSH_PORT system identity print"
echo ""
if ssh "$ROUTEROS_USER@$ROUTEROS_HOST" -p "$ROUTEROS_SSH_PORT" 'system identity print'
then
    ntc ".. Connected!"
else
    err "Could not connect to router."
    exit
fi

function execute_file() {
    FILE=$1
    ntc "Transfer and import file: $FILE"
    scp -P "$ROUTEROS_SSH_PORT" "$FILE" "$ROUTEROS_USER"@"$ROUTEROS_HOST":"$FILE"
    ssh "$ROUTEROS_USER@$ROUTEROS_HOST" -p "$ROUTEROS_SSH_PORT" /import verbose=yes "$FILE"
}

function execute() {
    ntc "# $1"
    ssh "$ROUTEROS_USER@$ROUTEROS_HOST" -p "$ROUTEROS_SSH_PORT" "$1"
}



## NOTE: question / function should be consistent
question enable-publickey 'Enable publickey access via RSA keys for user $ROUTEROS_USER.' yes
function enable-publickey {

if [[ -f ~/.ssh/id_rsa.pub ]]
then
    ntc "using public key from $USER for $ROUTEOS_USER"
else
    ssh-keygen -t rsa
fi

if [[ -f ~/.ssh/id_rsa.pub ]]
then
    ntc "upload publickey id_rsa.pub"
    scp -P "$ROUTEROS_SSH_PORT" ~/.ssh/id_rsa.pub "$ROUTEROS_USER"@"$ROUTEROS_HOST":"id_rsa.pub"
    execute "/user ssh-keys import public-key-file=id_rsa.pub user=$ROUTEROS_USER"
else
    err "No publickey"
fi
}

question enable-https 'Enable https port.' yes
function enable-https {

    FILE=enable-https
cat << EOF > "$FILE"
       certificate add name=root-cert common-name=root-certificate days-valid=3650 key-usage=key-cert-sign,crl-sign
       certificate sign root-cert
       certificate add name=https-cert common-name=https-certificate days-valid=3650
       certificate sign ca=root-cert https-cert
       ip service set www-ssl certificate=https-cert disabled=no
EOF
    execute_file "$FILE"
}


question https-on-8443 'Set https www-ssl to port 8443.' yes
function https-on-8443 {
    execute "ip service set www-ssl disabled=no port=8443"
}

## Windows is considered insecure, therfore winbox is too.
question disable-insecure-services 'Disable insecure services: http based www, api, ftp, telnet, winbox.' yes
function disable-insecure-services {

    FILE=disable-services
cat << EOF > "$FILE"
    ip service set api disabled=yes
    ip service set ftp disabled=yes
    ip service set telnet disabled=yes
    ip service set winbox disabled=yes
    ip service set www disabled=yes
EOF
    execute_file "$FILE"
}



question add-local-user "Use a local user $USER / or a custom user. Enable ssh key if present." yes
function add-local-user {

    # Read Username
    echo -n "Username ($USER):"
    read username

    # Read Password
    echo -n "Password: "
    read -s password
    echo ''

    if [[ ! $username ]]
    then
       username=$USER
    fi

    if [[ $password ]] 
    then
       execute "/user add name=$username password=$password group=full"
    else
       execute "/user add name=$username group=full"
    fi

    if [[ -f ~/.ssh/id_rsa.pub ]]
    then
        ntc "upload id_rsa.pub as $username-id_rsa.pub"
        scp -P "$ROUTEROS_SSH_PORT" ~/.ssh/id_rsa.pub "$ROUTEROS_USER"@"$ROUTEROS_HOST":"$username-id_rsa.pub"

        execute "/user ssh-keys import public-key-file=$username-id_rsa.pub user=$username"
    else
        err "No publickey"
    fi

    ntc "Continue as $username"
    ROUTEROS_USER=$username
}


question remove-admin "Remove default admin user." yes
function remove-admin {
        execute "/user remove admin"
}

for f in install-mikrotik-*.sh
do
    echo "Loading $f"
    if [[ -f $f ]]
    then
	source "$f"
    fi
done


## Finalize will do the job!
finalize
exit



File: /README.md
# mikrotik-installer
Scripts to install an army of routerboards - works over ssh with minimal interaction required.

## Start with
```bash
curl https://raw.githubusercontent.com/LaKing/mikrotik-installer/master/install-mikrotik.sh > install-mikrotik.sh \
&& bash install-mikrotik.sh
```

You may pass your username@ip-address-or-hostname as argument, if not it will take the default admin@192.168.88.1


Answer questions with yes or no - or leave the default value (capital letter) once all questions are answered, the script will execute the commands - wherby additional parameters might be asked.


