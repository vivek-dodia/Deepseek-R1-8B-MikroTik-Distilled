# Repository Information
Name: mikrotik-easy-web-ui

# Directory Structure
Directory structure:
└── github_repos/mikrotik-easy-web-ui/
    ├── .env.sample
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
    │   │       ├── pack-70e17ad665dc06a9632519cde1e33581e085d6e3.idx
    │   │       └── pack-70e17ad665dc06a9632519cde1e33581e085d6e3.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── bandwitch_balancer.py
    ├── html/
    │   └── index.html
    ├── LICENSE.md
    ├── main.py
    ├── notification.sample.py
    ├── README.md
    ├── requirements.txt
    ├── router_api.py
    └── static/


# Content
File: /.env.sample
### [REQUIRED]
WEB_UI_PORT=8341

## Login credentials
ROUTER_USER=api
ROUTER_PASSWORD=

## Network information
ROUTER_ADDRESS=10.1.1.1
LOCAL_NETWORK=10.1.1.0/24

### [OPTIONAL]
# Throttle API requests by imposing a global limit
# API_SLEEP_TIME=0.5
# API_COMMAND_TIME_CACHE=commands.sqlite3

# Automatic setting of DoH DNS whenever possible
# AUTO_DoH_SERVER=https://1.1.1.1/dns-query
# also set this DNS together with this DNS servers:
# DNS_TRUSTED_SERVERS=1.1.1.1,1.0.0.1
# and when DNS is unaviable, fallback to theese DNS servers
# DNS_FALLBACK_SERVERS=8.8.8.8,4.4.4.4

## Address of this computer
# LOCAL_ADDRESS=10.1.1.10

## In this file a copy from the router's log is stored
File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/esoadamo/mikrotik-easy-web-ui.git
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
0000000000000000000000000000000000000000 3aa16b5f5c6c9443d846da45e9248a833d58d9ce vivek-dodia <vivek.dodia@icloud.com> 1738606307 -0500	clone: from https://github.com/esoadamo/mikrotik-easy-web-ui.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 3aa16b5f5c6c9443d846da45e9248a833d58d9ce vivek-dodia <vivek.dodia@icloud.com> 1738606307 -0500	clone: from https://github.com/esoadamo/mikrotik-easy-web-ui.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3aa16b5f5c6c9443d846da45e9248a833d58d9ce vivek-dodia <vivek.dodia@icloud.com> 1738606307 -0500	clone: from https://github.com/esoadamo/mikrotik-easy-web-ui.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3aa16b5f5c6c9443d846da45e9248a833d58d9ce refs/remotes/origin/main
7f73207d5778b6521a075785b09583d2cee8a575 refs/remotes/origin/master


File: /.git\refs\heads\main
3aa16b5f5c6c9443d846da45e9248a833d58d9ce


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
venv/
wenv/
File: /bandwitch_balancer.py
from threading import Thread
from time import sleep, time
from collections import deque
from typing import Iterator, Set, Tuple, NamedTuple, List, Optional, Dict, TypeVar, Generic

from dotenv import load_dotenv

from router_api import API, APISingleTread
from routeros_api.exceptions import RouterOsApiError

load_dotenv()

T = TypeVar('T')


class Limit(NamedTuple):
    id: Optional[str]
    ip: int
    rate: int
    max_rate: int

    def __str__(self):
        rate = self.rate // (1024**2)
        max_rate = self.max_rate // (1024 ** 2)
        usage = 0 if max_rate == 0 else int(100 * self.rate / self.max_rate)
        return f"Limit({self.ip=}, {usage=} %, {max_rate=}, {rate=})"


class DictWAverage(Generic[T]):
    def __init__(self, n: int) -> None:
        self.__n = n
        self.__data: Dict[T, deque[float]] = {}

    def __setitem__(self, key: T, value: float) -> None:
        if key not in self.__data:
            self.__data[key] = deque()
        if len(self.__data[key]) == self.__n:
            self.__data[key].popleft()
        while len(self.__data[key]) < self.__n:
            self.__data[key].append(value)

    def __getitem__(self, item: T) -> float:
        data = self.__data[item]
        return sum([(i + 1) * x for i, x in enumerate(data)]) / sum([(i + 1) for i, _ in enumerate(data)])

    def __iter__(self) -> Iterator[Tuple[T, float]]:
        return map(
            lambda x: (x, self[x]),
            self.__data.keys()
        )


class Balancer(Thread):
    def __init__(self, ip_prefix: str, max_bandwitch: int, min_bandwitch: int, threshold: int = 95,
                 api: APISingleTread = API, direction_upload: bool = False, suppress_output: bool = False) -> None:
        super().__init__(daemon=True)
        self.suppress_output = suppress_output
        self.__max_bandwitch = max_bandwitch - min_bandwitch
        self.__min_bandwitch = min_bandwitch
        self.__threshold = threshold / 100
        self.__ip_prefix = ip_prefix
        self.__name_prefix = f"balancer_{'download' if not direction_upload else 'upload'}_{self.__ip_prefix}"
        self.__direction_upload = direction_upload
        self.__api: API = api
        self.__queues_history: DictWAverage[int] = DictWAverage(n=3)
        self.__queues_history_long: DictWAverage[int] = DictWAverage(n=60)
        self.__queues_priority: Dict[int, int] = {}
        self.__watched_ips: Optional[Set[int]] = None

        self.__mark_cache: Dict[int, int] = {}
        self.__mark_cache_time: int = 0

        self.__init_marks()
        self.__init_queues()

    def get_rates(self) -> Iterator[Tuple[int, int]]:
        yield from self.__queues_history

    def set_queue_priority(self, ip: int, value: int) -> None:
        self.__queues_priority[ip] = value

    def get_queue_priority(self, ip: int) -> int:
        return self.__queues_priority.get(ip, 100)

    @property
    def watched_ips(self) -> Optional[Set[int]]:
        return set(self.__watched_ips) if self.__watched_ips is not None else None

    @watched_ips.setter
    def watched_ips(self, value: Optional[Set[int]]):
        if value == self.__watched_ips:
            return
        if value is None:
            self.__watched_ips = None
        else:
            self.__watched_ips = set(value)
        self.__init_marks()

    def __init_marks(self, ) -> None:
        existing_marks: Dict[str, Tuple[str, bool]] = {
            x['new-packet-mark']: (x['id'], x['disabled'] == 'false')
            for x in filter(
                lambda x: x.get('new-packet-mark'),
                self.__api.call('ip/firewall/mangle').get()
            )
        }

        for i in range(1, 255):
            ip, mark_name = self.__ip_mark_name(i)
            if mark_name in existing_marks:
                if self.__watched_ips is not None:
                    mark_id, mark_enabled = existing_marks[mark_name]
                    is_watched = i in self.__watched_ips
                    if is_watched and not mark_enabled:
                        self.__api.call('ip/firewall/mangle').set(id=mark_id, disabled="false")
                    elif not is_watched and mark_enabled:
                        self.__api.call('ip/firewall/mangle').set(id=mark_id, disabled="true")
                continue
            addr_local = f'{ip}/32' if i != 0 else f'{ip}/24'
            addr_lan = f'!{self.__ip_prefix}.0/24'
            self.__api.call('ip/firewall/mangle').exec('add', arguments={
                'chain': 'forward',
                'dst-address': addr_local if not self.__direction_upload else addr_lan,
                'src-address': addr_lan if not self.__direction_upload else addr_local,
                'action': 'mark-packet',
                'new-packet-mark': mark_name,
                'passthrough': 'no'
            })

    def __init_queues(self) -> None:
        queues = list(self.__get_queues(include_root=True))
        self.__create_queue(0, queues)
        for i in range(1, 255):
            self.__delete_queue(i, queues)

    def __create_queue(self,
                       ip: int,
                       queues: Optional[Iterator[Limit]] = None,
                       limit_at: Optional[int] = None,
                       max_limit: Optional[int] = None
                       ) -> None:
        queues = list(queues if queues else self.__get_queues(include_root=True))

        for q in queues:
            if q.ip == ip:
                if q.id is not None:
                    return
                break

        ip_full, mark_name = self.__ip_mark_name(ip)
        _, parent_name = self.__ip_mark_name(0)
        if ip == 0:
            parent_name = 'bridge'

        self.__api.call('queue/tree').exec('add', arguments={
            'name': mark_name,
            'max-limit': '999M' if limit_at is None else str(max_limit),
            'limit-at': '999M' if max_limit is None else str(limit_at),
            'packet-mark': mark_name if ip != 0 else '',
            'parent': parent_name
        })

    def __delete_queue(self, ip: int, queues: Optional[Iterator[Limit]] = None) -> None:
        queues = self.__get_queues(queues, include_root=True)
        _, mark_name = self.__ip_mark_name(ip)

        for q in queues:
            if q.ip != ip:
                continue
            if q.id is None:
                return
            self.__api.call('queue/tree').remove(id=q.id)
            return

    def __set_limit(self, ip: int, limit: int, queues: Optional[List[Limit]] = None) -> None:
        _, mark_name = self.__ip_mark_name(ip)
        limit_at = int(limit * self.__threshold)

        if queues is None:
            queue_data = self.__queue_data_to_limit(
                self.__api.call('queue/tree').exec('print', queries={'name': mark_name})[0]
            )
        else:
            queue_data = next(filter(lambda x: x.ip == ip, queues))

        if queue_data.max_rate == limit:
            return

        if queue_data.id is not None:
            if limit < self.__max_bandwitch:
                self.__api.call('queue/tree').set(id=queue_data.id, max_limit=str(limit), limit_at=str(limit_at))
            else:
                self.__delete_queue(ip, queues)
        else:
            self.__create_queue(ip, queues, limit_at=limit_at, max_limit=limit)

    def __ip_mark_name(self, ip: int) -> Tuple[str, str]:
        return f"{self.__ip_prefix}.{ip}", f"{self.__name_prefix}.{ip:03}"

    @staticmethod
    def __queue_data_to_limit(data: dict) -> Limit:
        return Limit(
            id=data['id'],
            ip=int(data['name'].rsplit('.', 1)[1]),
            rate=int(data['rate']),
            max_rate=int(data['max-limit'])
        )

    def __get_queues(self, existing: Optional[Iterator[Limit]] = None, include_root: bool = False) -> Iterator[Limit]:
        if existing is not None:
            yield from list(existing)
            return
        time_start = time()
        api_res = self.__api.call('ip/firewall/mangle')
        marks = list(filter(
            lambda x: x.get('new-packet-mark', '').startswith(self.__name_prefix),
            api_res.exec('print', arguments={'stats': ''})
        ))
        time_start += api_res.wait_time

        queues_map = {x.ip: x for x in map(
            self.__queue_data_to_limit,
            filter(
                lambda x: x['name'].startswith(self.__name_prefix) and (include_root or not x['name'].endswith('.000')),
                self.__api.call('queue/tree').exec('print', arguments={'stats': ''})
            )
        )}

        if include_root:
            q_root = queues_map.get(0)
            if q_root:
                yield q_root

        time_delta = time_start - self.__mark_cache_time
        for m in marks:
            ip = int(m['new-packet-mark'].rsplit('.', 1)[1])
            m_bytes = int(m['bytes'])
            if ip in self.__mark_cache:
                if ip in queues_map:
                    q_id = queues_map[ip].id
                    q_max_rate = queues_map[ip].max_rate
                else:
                    q_id = None
                    q_max_rate = self.__max_bandwitch
                bytes_delta = m_bytes - self.__mark_cache[ip]
                rate = int(8 * bytes_delta / time_delta)
                yield Limit(
                    id=q_id,
                    ip=ip,
                    rate=rate,
                    max_rate=q_max_rate
                )
            self.__mark_cache[ip] = m_bytes
        self.__mark_cache_time = time_start

    def __get_queue_root(self, queues: Optional[Iterator[Limit]] = None) -> Limit:
        queues = self.__get_queues(queues)

        for q in queues:
            if q.ip == 0:
                return q
        raise ValueError("Root queue not found")

    def __get_queues_limited(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = self.__get_queues(queues)

        return filter(
            lambda x: x.max_rate < self.__max_bandwitch,
            queues
        )

    def __get_queues_full(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = self.__get_queues(queues)

        return filter(
            lambda x: x.rate > x.max_rate * self.__threshold,
            self.__get_queues_limited(queues)
        )

    def __get_queues_used(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = list(self.__get_queues(queues))

        queues_nonzero_rate = filter(
            lambda x: x.rate > 0,
            queues
        )

        rate_used = 0

        def is_over_threshold_sum_rate(queue: Limit):
            nonlocal rate_used
            rate_used += queue.rate
            return rate_used >= self.__min_bandwitch * self.__threshold

        return filter(is_over_threshold_sum_rate, sorted(queues_nonzero_rate, key=lambda x: x.rate))

    def __get_queues_used_unlimited(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = self.__get_queues(queues)
        queues_used = list(self.__get_queues_used(queues))

        return filter(
            lambda x: x.id is None,
            queues_used
        )

    def __get_queues_used_limited(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = self.__get_queues(queues)
        queues_used = list(self.__get_queues_used(queues))

        return filter(
            lambda x: x.id is not None,
            queues_used
        )

    def __get_queues_unused_limited(self, queues: Optional[Iterator[Limit]] = None) -> Iterator[Limit]:
        queues = list(self.__get_queues(queues))
        queues_used_ip = set(map(lambda x: x.ip, self.__get_queues_used(queues)))
        queues_limited = list(self.__get_queues_limited(queues))

        return filter(
            lambda x: x.ip not in queues_used_ip,
            queues_limited
        )

    def __rebalance_queues(
            self, queues: Iterator[Limit], free_bandwitch: int, queues_all: Optional[Iterator[Limit]] = None
    ) -> None:
        queues = list(queues)
        queue_scores: Dict[int, float] = {
            q.ip: self.get_queue_priority(q.ip) * self.__max_bandwitch / self.__queues_history_long[q.ip] for q in queues
        }
        scores_sum = sum(queue_scores.values())
        for q in queues:
            queue_scores[q.ip] /= scores_sum

        for q in queues:
            self.__set_limit(q.ip, max(self.__min_bandwitch, int(free_bandwitch * queue_scores[q.ip])), queues_all)

    def run(self) -> None:
        while True:
            try:
                self.__perform_cycle()
            except RouterOsApiError:
                pass
            sleep(10)

    def __perform_cycle(self) -> None:
        queues = list(self.__get_queues())
        queues_used_unlimited = list(self.__get_queues_used_unlimited(queues))
        queues_used_limited = list(self.__get_queues_used_limited(queues))
        queues_unused_limited = list(self.__get_queues_unused_limited(queues))
        queues_limited = list(self.__get_queues_limited(queues))
        queues_limited_full = list(self.__get_queues_full(queues))

        for q in queues:
            self.__queues_history[q.ip] = q.rate
            self.__queues_history_long[q.ip] = q.rate

        bandwitch_used = sum(map(lambda x: x[1], self.__queues_history))
        bandwitch_free = self.__max_bandwitch - bandwitch_used
        threshold_free = self.__max_bandwitch * self.__threshold - bandwitch_used
        if not self.suppress_output:
            print()
            print("--------------------")
            if queues_limited:
                print('Limited:')
                print('\n'.join(['- ' + str(x) + (' (unused)' if x in queues_unused_limited else '')
                                 for x in queues_limited]))
            if queues_used_unlimited:
                print('Unlimited:')
                print('\n'.join(['- ' + str(x) for x in queues_used_unlimited]))
            print(
                f"Free total: {bandwitch_free / (1024 ** 2):2.02f}, "
                f"free threshold: {threshold_free / (1024 ** 2):2.02f}, "
                f"used: {bandwitch_used / (1024 ** 2):2.02f} "
                f"({int(100 * bandwitch_used / self.__max_bandwitch)} %)")
            print("--------------------")

        if threshold_free > 0:
            if queues_limited_full:
                bandwitch_to_rebalance = min(
                    sum(map(lambda x: x.rate, queues_limited_full)) + bandwitch_free,
                    self.__max_bandwitch - 1
                )
                self.__rebalance_queues(queues_limited_full, bandwitch_to_rebalance, queues)
            elif queues_used_limited:
                bandwitch_add = bandwitch_free / len(queues_used_limited)
                for q in queues_used_limited:
                    self.__set_limit(q.ip, min(q.max_rate + bandwitch_add, self.__max_bandwitch), queues)
            for q in queues_unused_limited:
                self.__set_limit(q.ip, self.__max_bandwitch, queues)
        else:
            bandwitch_reserved = 0

            for q in queues_used_unlimited:
                bandwitch_new = min(
                    max(self.__min_bandwitch, int(self.__queues_history[q.ip])),
                    int(self.__max_bandwitch * 0.99)
                )
                self.__set_limit(q.ip, bandwitch_new, queues)
                bandwitch_reserved += bandwitch_new
            if queues_used_limited:
                self.__rebalance_queues(queues_used_limited, self.__max_bandwitch - bandwitch_reserved, queues)


if __name__ == '__main__':
    def main() -> None:
        b = Balancer('10.1.1', 30 * (1024 ** 2), 3 * (1024 ** 2), threshold=93)
        b.start()
        while True:
            sleep(1000)


    main()


File: /html\index.html
<!DOCTYPE html>
<!--suppress HtmlFormInputWithoutLabel -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!--suppress HtmlUnknownTarget -->
    <link rel="stylesheet" href="static/bootstrap.min.css">
    <!--suppress HtmlUnknownTarget -->
    <script src="static/jquery-3.2.1.slim.min.js"></script>
    <!--suppress HtmlUnknownTarget -->
    <script src="static/bootstrap.min.js"></script>
    <!--suppress HtmlUnknownTarget -->
    <link rel="icon" type="image/png" href="static/icon.png">

    <title>Home net monitor</title>
</head>
<body>
<div class="container">
    <div class="col-lg-12">
            <h2>Active limits</h2>
            <!--suppress HtmlUnknownTarget -->
            <form method="post" action="api/new-limit">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                        <tr>
                            <th>Name</th>
                            <th>Download</th>
                            <th>Upload</th>
                            <th>Until</th>
                            <th>Cancel</th>
                        </tr>
                        </thead>
                        <tbody id="active-limits">
                        <tr id="row-new-limit" class="no-auto-gen">
                            <td><select name="target" class="form-control" id="newLimitTarget"></select></td>
                            <td><input name="download" class="form-control" type="number" style="width: 10ex"
                                       value="0.75" min="0" step="0.01">MiB
                            </td>
                            <td><input name="upload" class="form-control" type="number" style="width: 10ex" value="0.5"
                                       min="0" step="0.01">MiB
                            </td>
                            <td><input type="time" name="time"><input name="date" class="form-control" type="date"></td>
                            <td>
                                <button type="submit" class="btn btn-primary">Add</button>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </form>
        </div>
    <div class="row">
        <div class="col-lg-6">
            <h2>Usage per IP</h2>
            <div class="table-responsive">
                <table class="table">
                    <thead>
                    <tr>
                        <th>IP</th>
                        <th>Download</th>
                        <th>Upload</th>
                    </tr>
                    </thead>
                    <tbody id="net-usage-by-ip">
                    </tbody>
                </table>
            </div>
        </div>
        <div class="col-lg-6">
            <h2>Active clients</h2>
            <div class="table-responsive">
                <table class="table">
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th>IP</th>
                    </tr>
                    </thead>
                    <tbody id="active-clients">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!--suppress HtmlUnknownTarget -->
<script>
    window.onload = () => {
        /**
         * HTTP get for given URL
         * @param url {string} URL
         * @returns Promise<Object>
         */
        const httpGet = (url) => {
            return new Promise((resolve, reject) => {
                const req = new XMLHttpRequest();
                req.onreadystatechange = () => {
                    if (req.readyState === 4) {
                        if (req.status === 200) {
                            resolve(JSON.parse(req.responseText));
                        } else {
                            reject(`HTTP error status: ${req.status}`, req)
                        }
                    }
                };
                req.open("GET", url, true);
                req.send();
            });
        }

        const clientsCache = {'{{ router_address }}': 'Router'};

        /**
         * @type HTMLSelectElement
         */
        const elNewLimitTarget = document.getElementById('newLimitTarget');
        elNewLimitTarget.onchange = () => {
            elNewLimitTarget.querySelectorAll('.selected').forEach((x) => x.classList.remove('selected'));
            const option = elNewLimitTarget.selectedOptions[0];
            option.selected = true;
            option.classList.add('selected');
        }

        const elActiveLimits = document.getElementById('active-limits');
        const elRowNewLimit = document.getElementById('row-new-limit');
        const getActiveLimits = async () => {
            const data = await httpGet('api/limits');

            [...elActiveLimits.children]
                .filter((child) => !child?.classList.contains('no-auto-gen'))
                .forEach((child) => child?.parentElement.removeChild(child));

            for (let limit of data) {
                const [name, target, download, upload, until] = limit;
                let untilStr = 'Never';
                if (until !== null) {
                    const date = new Date(until * 1000);
                    const z = (x) => x < 10 ? `0${x}` : x;
                    untilStr = `${z(date.getDate())}/${z(date.getMonth() + 1)} ${z(date.getHours())}:${z(date.getMinutes())}`;
                }
                const friendlyName = (target === "EVERYONE" ? "Everyone" : clientsCache[target]) || target;

                const row = document.createElement('tr');
                row.innerHTML = `<td>${friendlyName}</td><td>${download}MiB</td><td>${upload}MiB</td><td>${untilStr}</td><td><form method="POST" action="api/limit-remove"><input style="display: none" name="name" type="text" value="${name}"><button class="btn btn-danger" type="submit">X</button></form></td>`;
                elActiveLimits.insertBefore(row, elRowNewLimit);
            }
        }

        const tBodyActiveClients = document.getElementById('active-clients');
        const getClients = async () => {
            const data = await httpGet('api/clients');
            // sort clients by name
            data.sort((a, b) => {
                const aName = a[1];
                const bName = b[1];
                if (aName === bName) {
                    return 0;
                }
                const names = [aName, bName];
                names.sort();
                return names[0] === aName ? -1 : 1;
            });
            const newLimitTargetValue = elNewLimitTarget.querySelector('.selected')?.value;
            tBodyActiveClients.innerHTML = '';

            const existingLimitTargetNames = new Set([...elNewLimitTarget.querySelectorAll('option')]
                .map((option) => option?.innerText).filter((name) => !!name));
            const newLimitTargetNames = new Set();

            /**
             * Adds a new limit target or updates it if already exists
             * @param name {string}
             * @param value {string}
             */
            function addLimitOption(name, value) {
                newLimitTargetNames.add(name);
                let existingTargetOption = [...elNewLimitTarget.querySelectorAll('option')].find((ch) => ch?.innerText === name);

                const elTargetOption = existingTargetOption || document.createElement('option');
                if (elTargetOption.innerText !== name) {
                    elTargetOption.innerText = name;
                }
                if (elTargetOption.value !== value) {
                    elTargetOption.value = value;
                }
                if (newLimitTargetValue && elTargetOption.value === newLimitTargetValue) {
                    elTargetOption.selected = true;
                    elTargetOption.classList.add('selected');
                }
                if (!existingTargetOption) {
                    elNewLimitTarget.appendChild(elTargetOption);
                }
            }

            addLimitOption('---', "");
            addLimitOption('@Everyone@', "EVERYONE");

            for (let client of data) {
                /**
                 * @type {string | null}
                 */
                const clientName = client[1];
                /**
                 * @type string
                 */
                const clientIP = client[0];
                /**
                 * @type boolean
                 */
                const clientIsActive = client[2];
                if (clientName !== null) {
                    clientsCache[clientIP] = clientName;
                    addLimitOption(clientName, clientIP);
                }
                if (clientIsActive) {
                    tBodyActiveClients.innerHTML += `<tr><td>${clientName}</td><td>${clientIP}</td></tr>`;
                }
            }

            // remove old target names
            existingLimitTargetNames.forEach((name) => {
                if (newLimitTargetNames.has(name)) {
                    return;
                }
                /**
                 * @type {HTMLElement}
                 */
                const el = [...elNewLimitTarget.querySelectorAll('option')].find((ch) => ch?.innerText === name);
                if (el) {
                    el.parentElement.removeChild(el);
                }
            });
        }

        getClients().then(() => getActiveLimits());
        setInterval(() => getClients(), 2600);
        setInterval(() => getActiveLimits(), 24000);

        const tBodyNetUsageByIp = document.getElementById('net-usage-by-ip')
        const getNetUsageByIp = async () => {
            let data = await httpGet('api/net-usage-by-ip');
            tBodyNetUsageByIp.innerHTML = '';
            for (let client of Object.keys(data)) {
                tBodyNetUsageByIp.innerHTML += `<tr><td>${clientsCache[client] || client}</td><td>${data[client][0]} kB/s</td><td>${data[client][1]} kB/s</td></tr>`;
            }
        }

        getNetUsageByIp();
        setInterval(() => getNetUsageByIp(), 2200);
    }
</script>
</body>
</html>


File: /LICENSE.md
MIT License

Copyright (c) 2021 [Adam Hlaváček](https://adamhlavacek.com/)

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


File: /main.py
import json
import os
import traceback
from datetime import datetime
from hashlib import md5
from pathlib import Path
from queue import Queue
from random import randint
from subprocess import call, PIPE
from threading import Thread, Lock
from time import sleep
from time import time
from types import SimpleNamespace
from typing import List, Tuple, Optional, Dict, Union, Callable, Any, Set, Iterable
from uuid import uuid4 as uuid
from dotenv import load_dotenv
from flask import Flask, Response, render_template, redirect, url_for, request
from gevent.pywsgi import WSGIServer
from flask_httpauth import HTTPBasicAuth

from bandwitch_balancer import Balancer
from router_api import API

try:
    import notification as notification_module
except ImportError:
    notification_module = None

load_dotenv()

# active IP, saved name, is active?, active mac, saved mac
CachedRequestActiveClientsCache = List[Tuple[str, Optional[str], bool, str, Optional[str]]]

# IP, down, up
CachedRequestNetUsageByIPCache = Dict[str, Tuple[int, int]]
RequestLimits = List[Tuple[str, str, float, float, Optional[int]]]


class CachedRequest(SimpleNamespace):
    cache: Union[CachedRequestActiveClientsCache, CachedRequestNetUsageByIPCache]
    nextRequestTime: float
    nextRequestDelay: float
    lock: Lock


CACHE: Dict[str, CachedRequest] = {
    'clients': CachedRequest(
        cache=[],
        nextRequestTime=0.0,
        nextRequestDelay=0.0,
        lock=Lock()
    ),
    'net-usage-by-ip': CachedRequest(
        cache={},
        nextRequestTime=0.0,
        nextRequestDelay=0.0,
        lock=Lock()
    ),
}

app = Flask(__name__, static_folder='static', template_folder='html')
auth = HTTPBasicAuth()

LOCAL_NETWORK = os.getenv('LOCAL_NETWORK')
LOCAL_ADDRESS = os.getenv('LOCAL_ADDRESS')
WEB_PORT = os.getenv('WEB_UI_PORT')
DoH_SERVER = os.getenv('AUTO_DoH_SERVER')
DNS_TRUSTED_SERVERS = os.getenv('DNS_TRUSTED_SERVERS')
DNS_FALLBACK_SERVERS = os.getenv('DNS_FALLBACK_SERVERS')
FILE_ROUTER_LOG = Path(os.getenv('ROUTER_LOG')) if os.getenv('ROUTER_LOG') is not None else None
LOCK_ROUTER_LOG = Lock()
FILE_SELF_LOG = Path(os.getenv('LOG')) if os.getenv('LOG') is not None else None
DNS_MONITOR_DOMAINS_FILE = os.getenv('DNS_MONITOR_DOMAINS_FILE')
UI_USER: Optional[str] = os.getenv('UI_USER')
UI_PASSWORD: Optional[str] = os.getenv('UI_PASSWORD')
SELF_LOG_QUEUE = Queue(maxsize=2048)
FILE_ARP_WATCH_DB = os.getenv('ARP_WATCH_DB')
ARP_WATCH_INTERFACE = os.getenv('ARP_WATCH_INTERFACE')
ARP_AUTO_REMOVE_TIME = (60 * int(os.getenv('ARP_AUTO_REMOVE_TIME'))) if os.getenv('ARP_AUTO_REMOVE_TIME')\
                                                                        is not None else None
CPU_NOTIFICATION_THRESHOLD = int(os.getenv('CPU_NOTIFICATION_THRESHOLD')) if os.getenv('CPU_NOTIFICATION_THRESHOLD') \
                                                                             is not None else None
BALANCER_ENABLED = os.getenv('BALANCER_ENABLED', 'no').lower() == 'yes'
BALANCER_DOWN_MAX = int(os.getenv('BALANCER_DOWN_MAX', '0'))
BALANCER_DOWN_MIN = int(os.getenv('BALANCER_DOWN_MIN', '0'))
BALANCER_DOWN_THRESHOLD = int(os.getenv('BALANCER_DOWN_THRESHOLD', '0'))
BALANCER_UP_MAX = int(os.getenv('BALANCER_UP_MAX', '0'))
BALANCER_UP_MIN = int(os.getenv('BALANCER_UP_MIN', '0'))
BALANCER_UP_THRESHOLD = int(os.getenv('BALANCER_UP_THRESHOLD', '0'))
BALANCER_IP_PREFIX = LOCAL_NETWORK.rsplit('.', 1)[0]

BALANCERS: Dict[str, Optional[Balancer]] = {
    'up': None,
    'down': None
}


def rt(data: any) -> Response:
    return Response(json.dumps(data), mimetype='application/json')


def retry_on_error(f: Callable) -> Callable:
    def i() -> Any:
        while True:
            # noinspection PyBroadException
            try:
                return f()
            except Exception:
                exc = traceback.format_exc()
                log('[ERROR] Retrying')
                log('[TRACEBACK]', exc.replace('\n', '\n           '))
                sleep(60)

    return i


def ping(host: str) -> bool:
    try:
        return call(['ping', '-c', '3', host], timeout=300, stdout=PIPE, stdin=PIPE, stderr=PIPE) == 0
    except TimeoutError:
        return False


def is_dns_healthy() -> bool:
    return (not ping("1.1.1.1") and not ping("8.8.8.8")) or ping(f"{uuid().hex}.local.devmonthor.eu")


def set_doh_enabled(enabled: bool, reset_after: Optional[int] = None) -> None:
    """
    Enables/disables DoH
    :param enabled: True if DoH should be enabled
    :param reset_after: if not None, then opposite state is set after given seconds
    :return: None
    """

    curr_is_enabled = API.call('/ip/dns').get()[0].get('use-doh-server', '') == DoH_SERVER

    if not curr_is_enabled and enabled:
        API.call('/ip/dns').exec('set', arguments={
            'use-doh-server': DoH_SERVER,
            'verify-doh-cert': 'yes',
            'servers': '' if DNS_TRUSTED_SERVERS is None else DNS_TRUSTED_SERVERS
        })
    elif curr_is_enabled is not enabled:
        API.call('/ip/dns').exec('set', arguments={
            'use-doh-server': '',
            'servers': '1.1.1.1,1.0.0.1,8.8.8.8,8.4.4.8' if DNS_FALLBACK_SERVERS is None else DNS_FALLBACK_SERVERS
        })

    if reset_after is not None:
        def reset() -> None:
            sleep(reset_after)
            set_doh_enabled(not enabled)

        Thread(target=reset, daemon=True).start()


def limit_get_names() -> Iterable[str]:
    r = map(lambda x: x['name'], API.call('/queue/simple').get())
    return r


def limit_remove(name: str) -> None:
    limits = API.call('/queue/simple')
    limit_id = limits.get(name=name)[0]['id']
    limits.remove(id=limit_id)


def limit_add(name: str, target: str, upload: float, download: float) -> None:
    """
    :param name: name of the queue
    :param target: IP address, /32 is added
    :param upload: in MiB
    :param download: in MiB
    :return: None
    """
    for existing_limit_name in limit_get_names():
        if existing_limit_name == name or existing_limit_name.startswith(f"_{target}"):
            limit_remove(existing_limit_name)
            break
    API.call('/queue/simple').exec('add', arguments={
        'name': name,
        'target': f"{target}/32" if target != "EVERYONE" else LOCAL_NETWORK,
        'max-limit': "%.2fM/%.2fM" % (upload * 8, download * 8)
    })


def limits_fetch() -> RequestLimits:
    r: RequestLimits = []
    for limit in API.call('/queue/simple').get():
        name: str = limit.get('name')
        if not name.startswith('_'):
            continue
        _, target, timeout = name.split('_')
        upload, download = limit.get('max-limit').split('/')
        timeout = int(timeout) if timeout != 'EVER' else None
        r.append((name, str(target), int(download) / 8000000, int(upload) / 8000000, timeout))
    return r


def log(*args) -> None:
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    line = ' '.join([str(x) for x in args])
    line_offset = " " * (len(date) + 1)

    line = line.replace('\n', '\n' + line_offset)

    line = f"{date}: {line}"
    print(line, flush=True)
    SELF_LOG_QUEUE.put(line)


@retry_on_error
def get_updates_available() -> bool:
    res = API.call('/system/package/update').exec('check-for-updates')
    return 'available' in res[-1]['status'].lower()


@retry_on_error
def get_log() -> List[Dict[str, str]]:
    res = API.call('/log').get()
    return res


@retry_on_error
def get_sniffer_running() -> bool:
    r = API.call('/tool/sniffer').get()[0]['running'] == 'true'
    return r


@retry_on_error
def get_arp_clients() -> Dict[str, str]:
    response_arp = API.call('/ip/arp').get()
    r: Dict[str, str] = {}
    for client in response_arp:
        if ARP_WATCH_INTERFACE is not None and client.get('interface') != ARP_WATCH_INTERFACE:
            continue
        if 'mac-address' not in client:
            continue
        if 'address' not in client:
            continue
        r[client['mac-address'].upper()] = client['address'].lower()
    return r


def remove_arp_client(mac: str) -> None:
    mac = mac.upper()

    for client in reversed(API.call('/ip/arp').get()):
        if client.get('mac-address', '').upper() != mac:
            continue
        API.call('/ip/arp').remove(numbers=client['id'])


@retry_on_error
def get_clients() -> CachedRequestActiveClientsCache:
    response_leases = API.call('/ip/dhcp-server/lease').get()
    arp_clients = get_arp_clients()
    r: CachedRequestActiveClientsCache = []
    for client in response_leases:
        if client.get('address', '') == API.address:
            continue
        if client.get('disabled', 'false') == 'true':
            continue

        client_address: str = client.get('address', '').lower()
        client_name: Optional[str] = client.get('comment')
        client_saved_mac = client.get('mac-address', '').upper()
        client_active_mac: str = client.get('active-mac-address', '').upper()
        client_active: bool = (
                client.get('status', '') == 'bound'
                or client_active_mac in arp_clients
                or client_saved_mac in arp_clients
                )
        client_imposter = (
                client_name
                and client_active
                and client_saved_mac != client_active_mac
                and (client_saved_mac not in arp_clients or arp_clients[client_saved_mac] != client_address)
        )

        if client_imposter:
            client_name += ' (IMPOSTER)'

        r.append((
            client_address,
            client_name,
            client_active,
            client_active_mac,
            client_saved_mac
        ))

        if client_active_mac in arp_clients:
            del arp_clients[client_active_mac]
        if client_saved_mac in arp_clients:
            del arp_clients[client_saved_mac]

    for arp_mac, arp_ip in arp_clients.items():
        r.append((
            arp_ip,
            None,
            True,
            arp_mac,
            None
        ))

    return r


@retry_on_error
def get_net_usage_by_ip() -> CachedRequestNetUsageByIPCache:
    ip_speed: Dict[str, Tuple[int, int]] = {}
    if not get_sniffer_running():
        API.call('/tool/sniffer').exec('start')
    packets = API.call('/tool/sniffer/host').get()
    for packet in packets:
        ip_from: str = packet.get('address', '')
        speed: Tuple[str, str] = tuple(packet.get('rate', '0/0').split('/'))
        if not ip_from.startswith('10.'):
            continue
        speed_down, speed_up = int(speed[0]) // (8 * 1024), int(speed[1]) // (8 * 1024)
        if speed_up + speed_down == 0:
            continue
        ip_speed[ip_from] = (speed_down, speed_up)

    router_ip = API.address
    if router_ip in ip_speed and LOCAL_ADDRESS in ip_speed:
        router_down, router_up = ip_speed[router_ip]
        server_down, server_up = ip_speed[LOCAL_ADDRESS]
        ip_speed[LOCAL_ADDRESS] = (max(0, server_down - router_up), max(0, server_up - router_down))
        ip_speed[router_ip] = (max(0, router_up - server_down), max(0, router_down - server_up))
        for ip in (LOCAL_ADDRESS, router_ip):
            if sum(ip_speed[ip]) <= 0:
                del ip_speed[ip]

    return ip_speed


@auth.verify_password
def verify_password(username: str, password: str):
    if UI_USER is not None and username != UI_USER:
        return False
    if UI_PASSWORD is not None and password != UI_PASSWORD:
        return False
    return True


@app.route('/')
@auth.login_required
def web_root() -> str:
    return render_template('index.html', router_address=API.address)


@app.route('/api/clients')
@auth.login_required
def api_clients() -> Response:
    entry = CACHE['clients']
    time_to_next_request = entry.nextRequestTime - time()
    lock: Lock = entry.lock
    if time_to_next_request < 0 and lock.acquire(blocking=False):
        if entry.nextRequestTime and time_to_next_request < -5 * 60:
            entry.nextRequestDelay = 5
        else:
            entry.nextRequestDelay = min(entry.nextRequestDelay + 0.2 + randint(0, 10) / 10, 15)
        entry.nextRequestTime = int(time()) + entry.nextRequestDelay

        def job():
            try:
                entry.cache = get_clients()
            finally:
                lock.release()

        Thread(target=job, daemon=True).start()

    return rt(entry.cache)


@app.route('/api/clients/all')
@auth.login_required
def api_clients_all() -> Response:
    r: CachedRequestActiveClientsCache = get_clients()
    if FILE_ARP_WATCH_DB is not None and os.path.isfile(FILE_ARP_WATCH_DB):
        with open(FILE_ARP_WATCH_DB, 'r') as f:
            ever_seen: List[str] = json.load(f)
        for mac in ever_seen:
            for client in r:
                if client[3] == mac or client[4] == mac:
                    break
            else:
                r.append(('', None, False, '', mac))
    return rt(r)


@app.route('/api/net-usage-by-ip')
@auth.login_required
def api_net_usage_by_ip() -> Response:
    if BALANCER_ENABLED:
        r = {}
        for ip, rate in BALANCERS['down'].get_rates():
            rate = int(rate / (8 * 1024))
            ip = f'{BALANCER_IP_PREFIX}.{ip}'
            if rate != 0:
                r[ip] = (rate, 0)
        for ip, rate in BALANCERS['up'].get_rates():
            ip = f'{BALANCER_IP_PREFIX}.{ip}'
            rate = int(rate / (8 * 1024))
            if rate != 0:
                r[ip] = (r[ip][0], rate) if ip in r else (0, rate)
        return rt(r)

    entry = CACHE['net-usage-by-ip']
    time_to_next_request = entry.nextRequestTime - time()
    lock: Lock = entry.lock
    if time_to_next_request < 0 and lock.acquire(blocking=False):
        if entry.nextRequestTime and time_to_next_request < -5 * 60:
            entry.nextRequestDelay = 5
        else:
            entry.nextRequestDelay = min(entry.nextRequestDelay + 0.5 + randint(0, 20) / 10, 30)
        entry.nextRequestTime = int(time()) + entry.nextRequestDelay

        def job():
            try:
                entry.cache = get_net_usage_by_ip()
            finally:
                lock.release()

        Thread(target=job, daemon=True).start()
    return rt(entry.cache)


@app.route('/api/new-limit', methods=['POST'])
@auth.login_required
def api_new_limit() -> Response:
    target = request.form.get('target')
    if not target:
        return rt({'error': 'No target specified'})
    upload = max(float(request.form.get('upload')), 0.1)
    download = max(float(request.form.get('download')), 0.1)
    until_date = request.form.get('date')
    until_time = request.form.get('time')

    if not until_date and not until_time:
        ttl = 'EVER'
    elif not until_time and until_date:
        ttl = str(int(datetime.strptime(until_date, '%Y-%m-%d').timestamp()))
    elif until_time and not until_date:
        hours, minutes = until_time.split(':')
        ttl = str(int(datetime.now().replace(hour=0, minute=0).timestamp() + (int(hours) * 3600) + (int(minutes) * 60)))
    else:
        ttl = str(int(datetime.strptime(f"{until_date} {until_time}", '%Y-%m-%d %H:%M').timestamp()))

    limit_add(f"_{target}_{ttl}", target, upload, download)

    return redirect(request.referrer if request.referrer else url_for('web_root'))


@app.route('/api/limit-remove', methods=['POST'])
@auth.login_required
def api_limit_remove() -> Response:
    name = request.form.get('name')
    assert name
    limit_remove(name)
    return redirect(request.referrer if request.referrer else url_for('web_root'))


@app.route('/api/limits')
@auth.login_required
def api_limits() -> Response:
    return rt(limits_fetch())


def send_notification(msg: str) -> bool:
    if notification_module is None:
        return False
    return notification_module.send_notification(msg)


@retry_on_error
def thread_stop_sniffer() -> None:
    while True:
        if CACHE['net-usage-by-ip'].nextRequestTime > 0 and \
                CACHE['net-usage-by-ip'].nextRequestTime - time() < -600 and get_sniffer_running():
            API.call('/tool/sniffer').exec('stop')
        sleep((5 + randint(0, 10)) * 60)


@retry_on_error
def thread_check_updates() -> None:
    while True:
        if get_updates_available():
            send_notification('Router updates available')
        sleep((24 + randint(0, 24)) * 3600)


@retry_on_error
def thread_notif_logged_errors() -> None:
    message_hashes: Set[str] = set()
    first_load = True
    while True:
        message_hashes_curr: Set[str] = set()
        for rec in get_log():
            rec_time: str = rec.get('time', '')
            rec_message: str = rec.get('message', '')

            rec_hash_input = (rec_message + (rec_time if ' ' not in rec_time else rec_time.split(' ', 1)[1]))
            rec_hash: str = md5(rec_hash_input.encode('utf8')).hexdigest()
            rec_id = int(rec.get('id', '*-1')[1:], 16)
            message_hashes_curr.add(rec_hash)
            if rec_hash in message_hashes or first_load:
                continue
            topics: List[str] = rec.get('topics', '').split(',')

            if FILE_ROUTER_LOG:
                with LOCK_ROUTER_LOG:
                    try:
                        with FILE_ROUTER_LOG.open('a') as f:
                            rec_log_data = {'timestamp': int(time())}
                            rec_log_data.update(rec)
                            f.write(json.dumps(rec_log_data) + '\n')
                    except PermissionError:
                        log('[FATAL] [LOG] cannot write log to a file')

            if 'error' not in topics:
                continue
            if 'DoH server connection error: ' in rec_message:
                log("[DNS]", "disabling DoH because of server failure")
                set_doh_enabled(False, 120)
                continue

            message = f"Router error {rec_id} @ {rec_time}: {rec_message}"
            log("[LOG]", message)
            send_notification(message)
        message_hashes = message_hashes_curr
        first_load = False
        sleep(600 + randint(0, 600))


@retry_on_error
def thread_test_dns() -> None:
    while True:
        if not is_dns_healthy():
            log('[DNS HEALTH] Restoring DNS')
            set_doh_enabled(False)

            sleep(5 * 60)
            if not is_dns_healthy():
                sleep(30)
                continue

            set_doh_enabled(True)

        sleep(30)


@retry_on_error
def thread_check_cpu() -> None:
    while True:
        sleep(5 * 60 + randint(30, 50))
        cpu_loads: List[float] = []

        for i in range(4):
            cpu_loads.append(float(API.call('/system/resource').get()[0]['cpu-load']))
            sleep(15)
        cpu_load = sum(cpu_loads) / len(cpu_loads)

        if cpu_load > CPU_NOTIFICATION_THRESHOLD:
            msg = f"High router CPU usage ({cpu_load:02.2f}%)"
            log("[CPU]", msg)
            send_notification(msg)


@retry_on_error
def thread_remove_old_limits() -> None:
    while True:
        limits_to_remove: List[str] = []
        for limit in limits_fetch():
            limit_name = limit[0]
            limit_timeout = limit[4]
            if limit_timeout and limit_timeout < time():
                limits_to_remove.append(limit_name)
        for limit_name in limits_to_remove:
            limit_remove(limit_name)
        sleep(60 + randint(30, 50))


@retry_on_error
def thread_write_log() -> None:
    if not FILE_SELF_LOG:
        return
    while True:
        line = SELF_LOG_QUEUE.get()
        try:
            with FILE_SELF_LOG.open('a') as f:
                f.write(line + '\n')
        except PermissionError:
            print(f'[LOG] Fatal: Cannot access log file "{FILE_SELF_LOG}"')


@retry_on_error
def thread_monitor_dns() -> None:
    if DNS_MONITOR_DOMAINS_FILE is None:
        return
    file_bad_domains = Path(DNS_MONITOR_DOMAINS_FILE)

    filtered_bad_domains: Set[str] = set()
    with file_bad_domains.open('r') as f:
        filtered_bad_domains.update(
            filter(
                lambda x: not not x and not x.startswith('#'),
                map(lambda x: x.strip().lower(), f.readlines())
            )
        )

    seen_bad_domains_last: Set[str] = set()

    while True:
        cache = API.call('/ip/dns/cache').get()
        seen_bad_domains_now: Set[str] = set()
        for record in cache:
            name: Optional[str] = record.get('name')
            data: Optional[str] = record.get('data')

            for bad_domain in filtered_bad_domains:
                if (name is not None and bad_domain in name.lower())\
                        or (data is not None and bad_domain in data.lower()):
                    seen_bad_domains_now.add(bad_domain)
                    if bad_domain in seen_bad_domains_last:
                        continue
                    message = f"[DNS MONITOR] Bad domain accessed '{name}' -> '{data}'"
                    log(message)
                    send_notification(message)
        seen_bad_domains_last = seen_bad_domains_now
        sleep(5 * 60 + randint(0, 280))


@retry_on_error
def thread_arp_watch() -> None:
    # mac: discovered_time
    arp_connected_clients: Dict[str, int] = {}

    known_mac_addresses: Set[str] = set()

    if FILE_ARP_WATCH_DB is not None and os.path.isfile(FILE_ARP_WATCH_DB):
        with open(FILE_ARP_WATCH_DB, 'r') as f:
            known_mac_addresses.update(map(lambda x: x.upper(), json.load(f)))

    while True:
        new_unknown_device = False
        for mac, ip in get_arp_clients().items():
            if mac in arp_connected_clients:
                continue
            arp_connected_clients[mac] = int(time())

            if FILE_ARP_WATCH_DB and mac not in known_mac_addresses:
                new_unknown_device = True
                log(f"[ARP WATCH] New device connected with MAC '{mac}' as '{ip}'")

        if ARP_AUTO_REMOVE_TIME is not None:
            removed_macs: Set[str] = set()
            for mac, connected_time in arp_connected_clients.items():
                if time() - connected_time < ARP_AUTO_REMOVE_TIME:
                    continue
                removed_macs.add(mac)
                remove_arp_client(mac)
            for mac in removed_macs:
                del arp_connected_clients[mac]

        if FILE_ARP_WATCH_DB is not None and new_unknown_device:
            with open(FILE_ARP_WATCH_DB, 'w') as f:
                json.dump(list(known_mac_addresses), f, indent=1)
        sleep(5 * 60 + randint(0, 280))


@retry_on_error
def thread_balancer_get_watched_ips():
    while True:
        active_ips = {int(x[0].rsplit('.', 1)[1]) for x in get_clients() if x[0].startswith(BALANCER_IP_PREFIX)}
        BALANCERS['up'].watched_ips = active_ips
        BALANCERS['down'].watched_ips = active_ips
        sleep(10 * 60 + randint(1, 10) * 60)


def main() -> int:
    log("[MAIN] starting up")
    if not API.is_ready:
        log("[MAIN] Error: Login credentials are missing!")
        return 1
    if not WEB_PORT or not LOCAL_NETWORK or not API.address:
        log("[MAIN] Error: Some required settings are missing")
        return 1
    Thread(target=thread_notif_logged_errors, daemon=True).start()
    Thread(target=thread_check_updates, daemon=True).start()
    Thread(target=thread_stop_sniffer, daemon=True).start()
    Thread(target=thread_write_log, daemon=True).start()
    Thread(target=thread_remove_old_limits, daemon=True).start()
    Thread(target=thread_monitor_dns, daemon=True).start()
    if CPU_NOTIFICATION_THRESHOLD is not None:
        Thread(target=thread_check_cpu, daemon=True).start()
    if DoH_SERVER is not None:
        set_doh_enabled(True)
        Thread(target=thread_test_dns, daemon=True).start()
    if FILE_ARP_WATCH_DB is not None or ARP_AUTO_REMOVE_TIME is not None:
        Thread(target=thread_arp_watch, daemon=True).start()
    if BALANCER_ENABLED:
        log("[MAIN] Using balancer as IP backend")
        BALANCERS['up'] = Balancer(
            BALANCER_IP_PREFIX,
            BALANCER_UP_MAX * (1024 ** 2),
            BALANCER_UP_MIN * (1024 ** 2),
            threshold=BALANCER_UP_THRESHOLD,
            direction_upload=True,
            suppress_output=True
        )
        BALANCERS['down'] = Balancer(
            BALANCER_IP_PREFIX,
            BALANCER_DOWN_MAX * (1024 ** 2),
            BALANCER_DOWN_MIN * (1024 ** 2),
            threshold=BALANCER_DOWN_THRESHOLD,
            suppress_output=True
        )
        BALANCERS['up'].start()
        sleep(2.5)
        BALANCERS['down'].start()
        Thread(target=thread_balancer_get_watched_ips, daemon=True).start()
    log(f"[MAIN] Starting web server @ http://127.0.0.1:{WEB_PORT}")
    http_server = WSGIServer(('127.0.0.1', int(WEB_PORT)), app)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        log("[MAIN] Shutting down")
    return 0


if __name__ == '__main__':
    try:
        exit_code = main()
    except Exception:
        exit_code = 1
        raise

    exit(exit_code)


File: /notification.sample.py
def send_notification(msg: str) -> bool:
    raise NotImplementedError("Somebody has forgot to implement notifications")
    # print("IMPORTANT! You got new notification:", msg)
    # return True


File: /README.md
# Mikrotik Easy-Web UI

![WEB UI screenshot](https://user-images.githubusercontent.com/15877754/119484457-55d82d80-bd56-11eb-9a3e-692a0c95e7ce.png)

## Features

- shows active clients
- shows current download/upload usage per client
- can limit maximal usage for whole network/single device
- automatic DoH heartbeat check
- local copy of router log
- router error notifications
- high CPU usage notification
- available update notification
- dns monitor for accessing bad domains

## Installation

### Account creation

1. create new user group (`api`) with following permissions: `reboot, read, write, policy, test, sniff, api`
2. create new user (`api`) and assign him to the created group

### Software installation

```bash
# 1. clone the repository
git clone https://github.com/esoadamo/mikrotik-easy-web-ui.git
cd mikrotik-easy-web-ui
# 2. (optional) create venv
python -m venv venv
# 3. install requirements
pip install -r requirements.txt
# 4. edit settings
cp .env.sample .env
nano .env
# 5. (optional) implement notification service
cp notification.sample.py notification.py  # and then edit function send_notification 
```

## Troubleshooting

### No client names (just IP adresses instead of them)

Client names should be set as comments inside `IP -> DHCP Server -> Leases -> {client}`

### Limits are not working

Disable fasttrack. `IP -> Firewall -> Filter Rules -> Fasttrack`

### DNS not working when AUTO_DOH is enabled

Make sure that you have downloaded and imported correct certificate for your DOH server

### Missing `bdist_wheel` during installation

On Ubuntu, you need to make sure that you have following packages installed:

```bash
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
```

File: /requirements.txt
Flask
Flask-HTTPAuth
RouterOS-api
requests
python-dotenv
gevent
git+https://github.com/esoadamo/Python-SQLiteDB.git


File: /router_api.py
import os
from pathlib import Path
from threading import Lock, get_ident, Thread
from time import sleep, time
from queue import Queue
from typing import TypedDict, Dict, Optional, Tuple, Set, NamedTuple, Any
from sys import stderr

from routeros_api.api import RouterOsApi, RouterOsApiPool
from routeros_api.exceptions import RouterOsApiError
from routeros_api.resource import RouterOsResource
from dotenv import load_dotenv
from sqlitedb.indexedb import IndexedDB, IndexedDBManager

load_dotenv()

API_SLEEP_TIME = float(os.getenv('API_SLEEP_TIME', '0'))
API_COMMAND_TIME_CACHE = os.getenv('API_COMMAND_TIME_CACHE')


class APICredentials(NamedTuple):
    username: str
    password: str
    address: str


class APIMultithread:
    class CacheContent(TypedDict):
        last_heartbeat_check: int
        api: RouterOsApi
        conn: RouterOsApiPool
        lock: Lock

    __thread_cache: Dict[int, CacheContent] = {}
    __cache_lock = Lock()
    __watchdog_running = False

    @classmethod
    def is_ready(cls) -> bool:
        return cls.__get_login_credentials() is not None

    @classmethod
    def get_address(cls) -> str:
        return cls.__get_login_credentials().address

    @staticmethod
    def __get_login_credentials() -> Optional[APICredentials]:
        username = os.getenv('ROUTER_USER')
        password = os.getenv('ROUTER_PASSWORD')
        address = os.getenv('ROUTER_ADDRESS')
        if not any((username, password, address)):
            return None
        return APICredentials(username=username, password=password, address=address)

    @classmethod
    def __create_new_connection(cls) -> Tuple[RouterOsApi, RouterOsApiPool]:
        username, password, address = cls.__get_login_credentials()
        conn = RouterOsApiPool(address,
                               username=username,
                               password=password,
                               use_ssl=True,
                               ssl_verify=False,
                               plaintext_login=True)
        return conn.get_api(), conn

    @classmethod
    def watchdog(cls) -> None:
        session_ttl_minutes = 100
        while True:
            sleep(max(session_ttl_minutes / 3, 0.5) * 60)
            with cls.__cache_lock:
                old_sessions: Set[int] = set()
                for session_id, data in cls.__thread_cache.items():
                    if time() - data['last_heartbeat_check'] > session_ttl_minutes * 60:
                        old_sessions.add(session_id)
                for session_id in old_sessions:
                    try:
                        cls.__thread_cache[session_id]['conn'].disconnect()
                    except RouterOsApiError:
                        pass
                    del cls.__thread_cache[session_id]

    @classmethod
    def watchdog_start(cls) -> None:
        if cls.__watchdog_running:
            return
        cls.__watchdog_running = True
        Thread(target=cls.watchdog, daemon=True).start()

    @classmethod
    def __get(cls) -> Tuple[RouterOsApi, Lock]:
        thread_id = get_ident()
        with cls.__cache_lock:
            if thread_id in cls.__thread_cache:
                if time() - cls.__thread_cache[thread_id]['last_heartbeat_check'] > 2 * 60:
                    cls.__thread_cache[thread_id]['last_heartbeat_check'] = int(time())
                    try:
                        api, conn = cls.__thread_cache[thread_id]['api'], cls.__thread_cache[thread_id]['conn']
                        api.get_resource('/system/resource').get()
                    except RouterOsApiError:
                        try:
                            conn.disconnect()
                            if API_SLEEP_TIME:
                                sleep(API_SLEEP_TIME)
                        except RouterOsApiError:
                            pass
                        del cls.__thread_cache[thread_id]
            if thread_id not in cls.__thread_cache:
                api, conn = cls.__create_new_connection()
                cls.__thread_cache[thread_id] = {
                    'api': api,
                    'conn': conn,
                    'last_heartbeat_check': time(),
                    'lock': Lock()
                }

            return cls.__thread_cache[thread_id]['api'], cls.__thread_cache[thread_id]['lock']

    @classmethod
    def disconnect(cls):
        with cls.__cache_lock:
            for data in cls.__thread_cache.values():
                data['conn'].disconnect()
                if API_SLEEP_TIME:
                    sleep(API_SLEEP_TIME)
            for key in list(cls.__thread_cache.keys()):
                del cls.__thread_cache[key]

    @classmethod
    def call(cls, path: str) -> RouterOsResource:
        api, lock = cls.__get()
        return api.get_resource(path)


APISingleThreadQIn = "Queue[APISingleTreadWorkerCommand]"
APISingleThreadQOut = "Queue[Tuple[Any, float]]"


class APISingleThreadPath:
    def __init__(
            self,
            path: str,
            queue_in: APISingleThreadQIn,
            queue_out: APISingleThreadQOut,
            lock_command: Lock,
            command_time_cache: Optional[IndexedDB] = None
    ):
        self.__path = path
        if not self.__path.startswith('/'):
            self.__path = "/" + self.__path
        self.__queue_in = queue_in
        self.__queue_out = queue_out
        self.__lock_command = lock_command
        self.__command_time_cache = command_time_cache
        self.__wait_time = 0.0
        self.__processing_time = 0.0

    @property
    def wait_time(self) -> float:
        return self.__wait_time

    def __call(self, action: str, args: Tuple[Any] = (), kwargs: Optional[Dict[str, Any]] = None) -> Any:
        kwargs = kwargs or {}
        command = APISingleTreadWorkerCommand(
            action=action,
            args=args,
            kwargs=kwargs,
            path=self.__path
        )
        time_start = time()
        with self.__lock_command:
            self.__queue_in.put(command)
            self.__wait_time = time() - time_start
            output, self.__processing_time = self.__queue_out.get()
            self.__save_call_to_time_cache(self.__processing_time, action, args, kwargs)
            if isinstance(output, Exception):
                raise output
            return output

    def get(self, *args, **kwargs) -> Any:
        return self.__call('get', args, kwargs)

    def remove(self, *args, **kwargs) -> Any:
        return self.__call('remove', args, kwargs)

    def set(self, *args, **kwargs) -> Any:
        return self.__call('set', args, kwargs)

    def exec(self,
             command: str,
             arguments: Optional[Dict[str, Any]] = None,
             queries: Optional[Dict[str, Any]] = None
             ) -> Any:
        kwargs = {}

        if arguments:
            kwargs['arguments'] = arguments
        if queries:
            kwargs['queries'] = queries
        return self.__call('call', args=(command,), kwargs=kwargs)

    def __save_call_to_time_cache(self, time_taken: float, action: str, args: Tuple[Any] = (),
                                  kwargs: Optional[Dict[str, Any]] = None) -> None:
        if self.__command_time_cache is None:
            return
        call_str = self.__call_to_str(action, args, kwargs)
        key_time = f"avg time of {call_str}"
        key_count = f"number of samples of {call_str}"

        avg_time: float = self.__command_time_cache.get(key_time, 0.0)
        avg_count: int = self.__command_time_cache.get(key_count, 0)

        if avg_count > 0:
            avg_time *= avg_count
        avg_time += time_taken
        avg_count += 1

        avg_time /= avg_count
        self.__command_time_cache[key_time] = avg_time
        self.__command_time_cache[key_count] = avg_count

    def __call_to_str(self, action: str, args: Tuple[Any] = (), kwargs: Optional[Dict[str, Any]] = None) -> str:
        return f"{self.__path}: {action}" + (
            ("  with" + (
                f" {len(args)} args" if args else ""
            ) + (
                 f" and {', '.join(sorted(kwargs.keys()))} params" if kwargs else ""
             )) if args or kwargs else ""
        )


class APISingleTreadWorkerCommand(NamedTuple):
    path: str
    action: str
    args: Tuple[Any]
    kwargs: Dict[str, Any]


class APISingleTreadWorker(Thread):
    def __init__(
            self,
            queue_in: APISingleThreadQIn,
            queue_out: APISingleThreadQOut,
    ):
        self.__queue_in = queue_in
        self.__queue_out = queue_out
        super().__init__(daemon=True)

    def run(self) -> None:
        while True:
            try:
                command = self.__queue_in.get()
                # print("[CALL]", command.path, command.action, command.args, command.kwargs, file=stderr)
                time_start = time()
                resource = APIMultithread.call(command.path)
                output = resource.__getattribute__(command.action)(*command.args, **command.kwargs)
                time_taken = time() - time_start
                # print('... ', output, file=stderr)
                self.__queue_out.put((output, time_taken))
                if API_SLEEP_TIME:
                    sleep(API_SLEEP_TIME)
            except Exception as e:
                self.__queue_out.put((e, 0.0))


class APISingleTread:
    def __init__(self, command_time_cache_path: Optional[Path] = None):
        self.__queue_in: APISingleThreadQIn = Queue(1)
        self.__queue_out: APISingleThreadQOut = Queue(1)
        self.__lock_command = Lock()
        self.__database_manager = IndexedDBManager(
            command_time_cache_path) if command_time_cache_path is not None else None
        self.__database = self.__database_manager['commands_time'] if self.__database_manager is not None else None
        APISingleTreadWorker(self.__queue_in, self.__queue_out).start()
        APIMultithread.watchdog_start()

    @property
    def address(self) -> str:
        return APIMultithread.get_address()

    @property
    def is_ready(self) -> bool:
        return APIMultithread.is_ready()

    def call(self, path: str) -> APISingleThreadPath:
        return APISingleThreadPath(path, self.__queue_in, self.__queue_out, self.__lock_command, self.__database)


API = APISingleTread(Path(API_COMMAND_TIME_CACHE) if API_COMMAND_TIME_CACHE is not None else None)


