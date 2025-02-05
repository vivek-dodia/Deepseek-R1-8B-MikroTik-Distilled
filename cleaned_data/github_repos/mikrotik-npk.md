# Repository Information
Name: mikrotik-npk

# Directory Structure
Directory structure:
└── github_repos/mikrotik-npk/
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
    │   │       ├── pack-5d89ee136b3905a6f9e5641e0cc6c4f78fb0ab77.idx
    │   │       └── pack-5d89ee136b3905a6f9e5641e0cc6c4f78fb0ab77.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── createnpk.py
    ├── dumpnpk.py
    ├── LICENSE
    ├── README.md
    └── unpacknpk.py


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
	url = https://github.com/kost/mikrotik-npk.git
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
0000000000000000000000000000000000000000 d54e97caac9ea447e29939ca4176d17eeff856a9 vivek-dodia <vivek.dodia@icloud.com> 1738605805 -0500	clone: from https://github.com/kost/mikrotik-npk.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d54e97caac9ea447e29939ca4176d17eeff856a9 vivek-dodia <vivek.dodia@icloud.com> 1738605805 -0500	clone: from https://github.com/kost/mikrotik-npk.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d54e97caac9ea447e29939ca4176d17eeff856a9 vivek-dodia <vivek.dodia@icloud.com> 1738605805 -0500	clone: from https://github.com/kost/mikrotik-npk.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d54e97caac9ea447e29939ca4176d17eeff856a9 refs/remotes/origin/master


File: /.git\refs\heads\master
d54e97caac9ea447e29939ca4176d17eeff856a9


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
*.py[cod]

# C extensions
*.so

# Packages
*.egg
*.egg-info
dist
build
eggs
parts
bin
var
sdist
develop-eggs
.installed.cfg
lib
lib64
__pycache__

# Installer logs
pip-log.txt

# Unit test / coverage reports
.coverage
.tox
nosetests.xml

# Translations
*.mo

# Mr Developer
.mr.developer.cfg
.project
.pydevproject


File: /createnpk.py
#!/usr/bin/env python

DESC_SHORT = 'routing'
DESC_LONG = '\n    Quagga 0.98.6-5\n  '
VER = '\x1bf\t\x02' # 2.9.27

ONINSTALL = '\n    new-libs\n    update-console\n  '
ONUNINSTALL = '\n    dead-libs\n    update-console\n  '

import sys
import zlib
import os
import os.path
import stat

from struct import pack, unpack
from time import time

#BUILD = pack("I", int(time()))
BUILD = '\xf5\xf7\xa8D'

def create_part(type, data):

	if type == 4:
		data = zlib.compress(data)
	dsize = len(data)

	res = ""
	res += pack("H", type)
	res += pack("I", dsize)
	res += data

	return res

def get_contents(directory):
	if not os.path.isdir(directory):
		return
	res = []
	for i in os.listdir(directory):
		ii = os.path.join(directory, i)
		res.append(i)
		if os.path.isdir(ii) and not os.path.islink(ii):
			for j in get_contents(ii):
				res.append(os.path.join(i, j))
	return res

def create_data(directory):
	res = ""
	print directory
	contents = get_contents(directory)
	contents.sort()
	for i in contents:
		ii = os.path.join(directory, i)

		dsize = 0
		if os.path.isdir(ii):
			data = ""
			mode = os.stat(ii)[stat.ST_MODE]
			modestr = pack("H", mode)
			rtype = 65
			perm = 237
		elif os.path.islink(ii):
			data = os.readlink(ii)
			dsize = len(data)
			# type=161(A1), perm=255(FF)
			rtype = 161
			perm = 255
			modestr = '\xFF\xA1'
		else:
			f = open(ii, "r")
			data = f.read()
			f.close()
			dsize = len(data)
			mode = os.stat(ii)[stat.ST_MODE]
			rtype = 129
			if mode & stat.S_IXUSR:
				perm = 237
			else:
				perm = 164

		modestr = pack("BB", perm, rtype)
		
		try:
			tim = os.stat(ii)[stat.ST_MTIME]
		except OSError:
			tim = 0

		header = modestr + '\x00\x00'+ '\x00\x00\x00\x00' + pack("I", tim)
		header += VER + BUILD + '\x00\x00\x00\x00'
		header += pack("I", dsize) + pack("H", len(i))

		res += header + i + data
	return res

# Read files

if len(sys.argv) != 2:
	print "Usage: %s <dir>" % (sys.argv[0])
	sys.exit(2)

data = create_data(sys.argv[1])

# Create parts

parts = ""
parts += create_part(7, ONINSTALL) # Oninstall
parts += create_part(8, ONUNINSTALL) # Onuninstall
parts += create_part(4, data) # Data

# Create header

header = ""
header += '\x1e\xf1\xd0\xba'
header += '\x00\x00\x00\x00' # Size... fill it in later
header += '\x01\x00 \x00\x00\x00'
shortd = DESC_SHORT
while len(shortd) < 16:
	shortd += '\x00'
header += shortd
header += VER
header += BUILD
header += '\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x04\x00\x00\x00i386\x02\x00' # Unknown stuff
header += pack("I", len(DESC_LONG))
header += DESC_LONG
header += '\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
header += VER + '\x00\x00\x00\x00'
header += VER + '\x00\x00\x00\x00'

header = header[0:4] + pack("I", len(header) + len(parts) - 8) + header[8:]

f = open(sys.argv[1] + ".npk", "w")
f.write(header)
f.write(parts)
f.close()


File: /dumpnpk.py
#!/usr/bin/env python

# npk format
# ---
# 0-4  : '\x1e\xf1\xd0\xba'
# 4-8  : len(data - 8) ===> The size of the package
# 8-14 : '\x01\x00 \x00\x00\x00'
# 14-30: description ===> 16 chars to put a short name
# 30-34: ?? | ==> version #1 - used in this header again (revision, 'f' (102), minor, major)
# 34-38: ?? | ==> version #2 - used in the data part (epoch time of package build)
#           |  Actualy seems like header[30:42] == each_data_header[12:24]...
#           |  Both appear as integers in /var/pdb/.../version
# 38-42: 0
# 42-46: 0
# 46-48: 16
# 48-50: 4 |
# 50-52: 0 | ==> Maybe int size of the architecture identifier that follows
# 52-56: "i386"
# 56-58: 2
# 58-62: long description size ===> how many chars follow
# 62-x : long description text
#   +24: '\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#   +8 : '2f\t\x02\x00\x00\x00\x00' |
#   +8 : '2f\t\x02\x00\x00\x00\x00' | ==> two same headers (separators?)
#                                         first 4 like header[30:34]
#                                         last 4 always 0
# 
# what follows are headers of 1 short (type) and 1 int (size):
# type 7, 8: some kind of script
# type 4: data
# 
# the content is directly after the header
# 
# in case of data it is commpressed with zlib
# 
# uncompressed data has 30 byte headers:
# 
# 0-1  : permissions: 237 is executable (755), 164 is non executable (644) |
# 1-2  : file type: 65 dir, 129 file                                       | ==> ST_MODE from stat()
# 2-4  : 0 - could be user/group
# 4-8  : 0 - could be user/group
# 8-12 : last modification time (ST_MTIME) as reported by stat()
# 12-24: version stuff and a 0 (see above...)
# 24-28: data size
# 28-30: file name size
# 
# then comes the file name and after that the data

import sys
import zlib

from struct import pack, unpack
from time import ctime

def parse_npk(filename):

	f = open(filename, "r")
	data = f.read()
	f.close()

	header = data[:62]
	dsize = unpack("I", header[58:62])[0]	# Description size
	header += data[62:62+dsize+40]

	print repr(header[38:58])
	print "Magic:", repr(header[0:4]), "should be:", repr('\x1e\xf1\xd0\xba')
	print "Size after this:", unpack("I", header[4:8])[0], "Header size:", len(header), "Data size:", len(data)
	print "Unknown stuff:", repr(header[8:14]), "should be:", repr('\x01\x00 \x00\x00\x00')
	print "Short description:", header[14:30]
	print "Revision, unknown, Minor, Major:", repr(header[30:34]), unpack("BBBB", header[30:34])
	print "Build time:", repr(header[34:38]), ctime(unpack("I", header[34:38])[0])
	print "Some other numbers:", unpack("IIHHH", header[38:52]), "should be: (0, 0, 16, 4, 0)"
	print "Architecture:", header[52:56]
	print "Another number:", unpack("H", header[56:58]), "should be: (2,)"
	print "Long description:", repr(header[62:62+dsize])
	print "Next 24 chars:", repr(header[62+dsize:62+dsize+24])
	print "    should be:", repr('\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
	print "Separators:", repr(header[62+dsize+24:62+dsize+32]), repr(header[62+dsize+32:62+dsize+40])
	print "   first 4:", unpack("BBBB",header[62+dsize+24:62+dsize+28]), unpack("BBBB",header[62+dsize+32:62+dsize+36])
	print ""

	data = data[62+dsize:]
	res=[]
	while len(data)>6:
		type = unpack("H", data[:2])[0]
		size = unpack("I", data[2:6])[0]
		print "Found data of type:", type, "size:", size
		contents = data[6:6+size]
		if type == 4:
			contents = zlib.decompress(contents)
			print "   Uncompressing data..."
		if type == 7:
			print "   Contents (oninstall):", repr(contents)
		if type == 8:
			print "   Contents (onuninstall):", repr(contents)
		res.append({"type": type, "size": size, "contents": contents})
		data = data[6+size:]
	print ""

	print "Returning the raw header and the rest of the file (each part in a list)"
	print ""

	return header, res

def parse_data(data):
	res = []
	while len(data)>30:
		header = data[:30]
		dsize = unpack("I", header[24:28])[0]
		fsize = unpack("H", header[28:30])[0]
		if len(data) - 30 - fsize - dsize < 0:
			dsize = len(data) - 30 - fsize
		fstuff = data[30:30+fsize]
		dstuff = data[30+fsize:30+fsize+dsize]
		res.append({"header": header, "file": fstuff, "data": dstuff})
		data = data[30+fsize+dsize:]
	return res

if __name__ == "__main__":
	if len(sys.argv) > 1:
		for i in sys.argv[1:]:
			header, res = parse_npk(i)
			for j in res:
				if j["type"] == 4:
					print "Files in package:"
					data = parse_data(j["contents"])
					for k in data:
						add = ''
						perm, type, z1, z2, tim = unpack("BBHII", k["header"][:12])
						if perm == 255:
							perm = "al"
						if perm == 237:
							perm = "ex"
						if perm == 164:
							perm = "nx"
						if type == 65:
							type = "dir"
						if type == 129:
							type = "fil"
						if type == 161:
							type = "sym"
							add='=> '+k["data"]
						print type, perm, k["file"], add, tim


File: /README.md
mikrotik-npk
============

Python tools for manipulating Mikrotik NPK format

Source
======
Original scripts were found on:
http://routing.explode.gr/node/96



File: /unpacknpk.py
#!/usr/bin/env python

# npk format
# ---
# 0-4  : '\x1e\xf1\xd0\xba'
# 4-8  : len(data - 8) ===> The size of the package
# 8-14 : '\x01\x00 \x00\x00\x00'
# 14-30: description ===> 16 chars to put a short name
# 30-34: ?? | ==> version #1 - used in this header again (revision, 'f' (102), minor, major)
# 34-38: ?? | ==> version #2 - used in the data part (epoch time of package build)
#           |  Actualy seems like header[30:42] == each_data_header[12:24]...
#           |  Both appear as integers in /var/pdb/.../version
# 38-42: 0
# 42-46: 0
# 46-48: 16
# 48-50: 4 |
# 50-52: 0 | ==> Maybe int size of the architecture identifier that follows
# 52-56: "i386"
# 56-58: 2
# 58-62: long description size ===> how many chars follow
# 62-x : long description text
#   +24: '\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#   +8 : '2f\t\x02\x00\x00\x00\x00' |
#   +8 : '2f\t\x02\x00\x00\x00\x00' | ==> two same headers (separators?)
#                                         first 4 like header[30:34]
#                                         last 4 always 0
# 
# what follows are headers of 1 short (type) and 1 int (size):
# type 7, 8: some kind of script
# type 4: data
# 
# the content is directly after the header
# 
# in case of data it is commpressed with zlib
# 
# uncompressed data has 30 byte headers:
# 
# 0-1  : permissions: 237 is executable (755), 164 is non executable (644) |
# 1-2  : file type: 65 dir, 129 file                                       | ==> ST_MODE from stat()
# 2-4  : 0 - could be user/group
# 4-8  : 0 - could be user/group
# 8-12 : last modification time (ST_MTIME) as reported by stat()
# 12-24: version stuff and a 0 (see above...)
# 24-28: data size
# 28-30: file name size
# 
# then comes the file name and after that the data

import sys
import zlib
import os

from struct import pack, unpack
from time import ctime

def parse_npk(filename):

	f = open(filename, "r")
	data = f.read()
	f.close()

	if data[10] == "$":
		# Switch to newer npk format
		print "Version 6 npk reader"

		header = data[:66]
		dsize = unpack("I", header[62:66])[0]	# Description size
		header += data[66:66+dsize+40]

		
		print repr(header[38:58])
		print "Magic:", repr(header[0:4]), "should be:", repr('\x1e\xf1\xd0\xba')
		print "Size after this:", unpack("I", header[4:8])[0], "Header size:", len(header), "Data size:", len(data)
		print "Unknown stuff:", repr(header[8:14]), "should be:", repr('\x01\x00 \x00\x00\x00')
		print "Short description:", header[14:30]
		print "Revision, unknown, Minor, Major:", repr(header[30:34]), unpack("BBBB", header[30:34])
		print "Build time:", repr(header[34:38]), ctime(unpack("I", header[34:38])[0])
		print "Another number:", repr(header[38:42])
		print "Some other numbers:", unpack("IIHHH", header[42:56]), "should be: (0, 2, 16, 4, 0)"
		print "Architecture:", header[56:60]
		print "Another number:", unpack("H", header[60:62]), "should be: (2,)"
		print "Long description:", repr(header[66:66+dsize])
#		print "Next 24 chars:", repr(header[62+dsize:62+dsize+24])
#		print "    should be:", repr('\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
#		print "Separators:", repr(header[62+dsize+24:62+dsize+32]), repr(header[62+dsize+32:62+dsize+40])
#		print "   first 4:", unpack("BBBB",header[62+dsize+24:62+dsize+28]), unpack("BBBB",header[62+dsize+32:62+dsize+36])
#		print ""

		data = data[66+dsize:]
	else:
		# Older npk format
		print "Version 5 npk reader"
		header = data[:62]
		dsize = unpack("I", header[58:62])[0]	# Description size
		header += data[62:62+dsize+40]

		print repr(header[38:58])
		print "Magic:", repr(header[0:4]), "should be:", repr('\x1e\xf1\xd0\xba')
		print "Size after this:", unpack("I", header[4:8])[0], "Header size:", len(header), "Data size:", len(data)
		print "Unknown stuff:", repr(header[8:14]), "should be:", repr('\x01\x00 \x00\x00\x00')
		print "Short description:", header[14:30]
		print "Revision, unknown, Minor, Major:", repr(header[30:34]), unpack("BBBB", header[30:34])
		print "Build time:", repr(header[34:38]), ctime(unpack("I", header[34:38])[0])
		print "Some other numbers:", unpack("IIHHH", header[38:52]), "should be: (0, 0, 16, 4, 0)"
		print "Architecture:", header[52:56]
		print "Another number:", unpack("H", header[56:58]), "should be: (2,)"
		print "Long description:", repr(header[62:62+dsize])
#		print "Next 24 chars:", repr(header[62+dsize:62+dsize+24])
#		print "    should be:", repr('\x03\x00"\x00\x00\x00\x01\x00system\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
#		print "Separators:", repr(header[62+dsize+24:62+dsize+32]), repr(header[62+dsize+32:62+dsize+40])
#		print "   first 4:", unpack("BBBB",header[62+dsize+24:62+dsize+28]), unpack("BBBB",header[62+dsize+32:62+dsize+36])
#		print ""

	res=[]
	while len(data)>6:
		type = unpack("H", data[:2])[0]
		size = unpack("I", data[2:6])[0]
		print "Found data of type:", type, "size:", size
		contents = data[6:6+size]
		#print contents
		if type == 3:
			print "   Contents (system):", repr(contents)
		if type == 4:
			contents = zlib.decompress(contents)
			print "   Uncompressing data..."
		if type == 7:
			print "   Contents (oninstall):", repr(contents)
		if type == 8:
			print "   Contents (onuninstall):", repr(contents)
		if type == 21:
			print "   Squash File System"
		res.append({"type": type, "size": size, "contents": contents})
		data = data[6+size:]
	print ""

	print "Returning the raw header and the rest of the file (each part in a list)"
	print ""

	return header, res

def parse_data(data):
	res = []
	while len(data)>30:
		header = data[:30]
		dsize = unpack("I", header[24:28])[0]
		fsize = unpack("H", header[28:30])[0]
		if len(data) - 30 - fsize - dsize < 0:
			dsize = len(data) - 30 - fsize
		fstuff = data[30:30+fsize]
		dstuff = data[30+fsize:30+fsize+dsize]
		res.append({"header": header, "file": fstuff, "data": dstuff})
		data = data[30+fsize+dsize:]
	return res

if __name__ == "__main__":
	if len(sys.argv) > 1:
		for i in sys.argv[1:]:
			header, res = parse_npk(i)
			for j in res:
				if j["type"] == 21:
					print "SquashFS found in package, extract 'squashfs' by using unsquashfs."
					f = open("squashfs", "w")
					f.write(j["contents"])
					f.close()
				if j["type"] == 4:
					print "Files in package:"
					data = parse_data(j["contents"])
					for k in data:
						perm, type, z1, z2, tim = unpack("BBHII", k["header"][:12])
						if type == 65:
							type = "dir"
							if not os.access(k["file"], os.F_OK):
								os.makedirs(k["file"])
						if type == 129:
							type = "fil"
							f = open(k["file"], "w")
							f.write(k["data"])
							f.close()
							os.chmod(k["file"], int(perm))
						if type == 161:
							type = "sym"
							os.symlink(k["data"],k["file"])
							# os.chmod(k["file"], int(perm))
						if perm == 164:
							perm = "nx"
						if perm == 237:
							perm = "ex"
						print type, perm, k["file"], tim



