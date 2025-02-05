# Repository Information
Name: MikrotikManager

# Directory Structure
Directory structure:
└── github_repos/MikrotikManager/
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
    │   │       ├── pack-741a2d4b797229b59b39777904235150502b2149.idx
    │   │       └── pack-741a2d4b797229b59b39777904235150502b2149.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── LICENCE
    ├── MikrotikManager/
    │   ├── Exception.cpp
    │   ├── Exception.h
    │   ├── librouteros.cpp
    │   ├── librouteros.h
    │   ├── main.cpp
    │   ├── main.h
    │   ├── MikrotikManager.1
    │   ├── Socket.cpp
    │   ├── Socket.h
    │   ├── Terminal.cpp
    │   ├── Terminal.h
    │   ├── Util.cpp
    │   ├── Util.h
    │   ├── Variant.cpp
    │   ├── Variant.h
    │   ├── whois.cpp
    │   └── whois.h
    ├── MikrotikManager.xcodeproj/
    │   ├── project.pbxproj
    │   ├── project.xcworkspace/
    │   │   └── contents.xcworkspacedata
    │   └── xcuserdata/
    │       └── gustavocampos.xcuserdatad/
    │           └── xcschemes/
    │               ├── MikrotikManager.xcscheme
    │               └── xcschememanagement.plist
    └── README


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
	url = https://github.com/solariun/MikrotikManager.git
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
0000000000000000000000000000000000000000 de6c4ae429c91fdced6a3855b000465a62de16c2 vivek-dodia <vivek.dodia@icloud.com> 1738606088 -0500	clone: from https://github.com/solariun/MikrotikManager.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 de6c4ae429c91fdced6a3855b000465a62de16c2 vivek-dodia <vivek.dodia@icloud.com> 1738606088 -0500	clone: from https://github.com/solariun/MikrotikManager.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 de6c4ae429c91fdced6a3855b000465a62de16c2 vivek-dodia <vivek.dodia@icloud.com> 1738606088 -0500	clone: from https://github.com/solariun/MikrotikManager.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
de6c4ae429c91fdced6a3855b000465a62de16c2 refs/remotes/origin/master


File: /.git\refs\heads\master
de6c4ae429c91fdced6a3855b000465a62de16c2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /LICENCE
MIT License

Copyright (c) 2017 Luiz Gustavo de Campos

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


File: /MikrotikManager\Exception.cpp
/*
 *  Exception.cpp
 *  thread
 *
 *  Created by Gustavo Campos on 24/04/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */

#include <Exception.h>
#include <Util.h>


void Exception::SetExceptionCode (int nExceptionCode)
{
    this->nExceptionCode = nExceptionCode;
}

int Exception::GetThrownExceptionCode ()
{
    return nExceptionCode;
}


char* Exception::GetExceptionMessage ()
{
	snprintf (pszExceptionMessage, EXCEPTION_MESSAGE_SIZE, "%s(%u) Func: [%s] Comm: [%s] Msg: %s", this->pszFile, this->nFileLine, this->pszFunction, this->pszCode, this->pszMessage);
	
	return pszExceptionMessage;
}


void Exception::IfException ()
{
    TRACE ("Default Exception treatement risen.\n");
}


bool Exception::GetExceptionData (const char* pszFile, const char* pszFunction, int* nFileLine, const char* pszCode, const char* pszMessage)
{
	
	if (pszFile != NULL) pszFile = this->pszFile;
	if (pszFunction != NULL) pszFunction = this->pszFunction;
	if (pszCode != NULL) pszCode = this->pszCode;
	if (pszMessage != NULL) pszMessage = (const char*) &this->pszMessage;
	if (nFileLine != NULL) *nFileLine = this->nFileLine;
	
	return true;
}


void Exception::ExceptionHandle (const char* pszFile, const char* pszFunction, int nFileLine, const char* pszCode,  const char* pszFormat, ...)
{
		va_list   vaArgs;
        long int nLen;
                        
        va_start (vaArgs, pszFormat);
        
        VERIFY ((nLen = vsnprintf ((char*) this->pszMessage, EXCEPTION_MESSAGE2_SIZE, pszFormat, vaArgs)) _ERROR, "Erro ao processar a string a ser enviada.");
        
        this->pszMessage [nLen] ='\0';
        
        va_end (vaArgs);

	  this->pszFile				= pszFile;
	  this->pszFunction			= pszFunction;
	  this->nFileLine           = nFileLine;
	  this->pszCode             = pszCode;
	  
	  //YYTRACE  ("this->Msg: [%s]\n\n", this->pszMessage);
}




File: /MikrotikManager\Exception.h
/*
 *  Exception.h
 *  thread
 *
 *  Created by Gustavo Campos on 24/04/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */


#ifndef EXCEPTION_H_CPP
#define EXCEPTION_H_CPP 1


//#include <iostream.h>
#include <string.h>
#include <string>
#include <Exception.h>
#include <errno.h>

using namespace std;


#if defined _WIN32 || defined __CYGWIN__
#define _IMPORT __declspec(dllimport)
#define API_EXPORT __declspec(dllexport)
#define API_LOCAL
#else
#include <stdarg.h>
#if __GNUC__ >= 4
#define API_IMPORT __attribute__ ((visibility("default")))
#define API_EXPORT __attribute__ ((visibility("default")))
#define API_LOCAL  __attribute__ ((visibility("hidden")))
#else
#define API_IMPORT
#define API_EXPORT
#define API_LOCAL
#endif
#endif


#define STRINGIZE(x) STRINGIZE2(x)
#define STRINGIZE2(x) #x

static string strGlobalStrError = "";

#define strLastException strGlobalStrError


#define YYTRACE(x,z...) {fprintf (stderr, "YMSG: %s(%u):", __FUNCTION__, __LINE__); fprintf (stderr, x, ##z);}

#ifdef _DEBUG
#define TRACE(x,z...) { fprintf (stderr, "DMSG: %s(%u):", __FUNCTION__, __LINE__); fprintf (stderr, x, ##z);}
#else
#define TRACE(x,z...) 1 ? (void) 0 : (void)fprintf (stderr, x, ##z)
#endif

#define NOTRACE(x,z...) 1 ? (void) 0 : (void)fprintf 

#define EXCEPTION_MESSAGE_SIZE		512
#define EXCEPTION_MESSAGE2_SIZE		320

#define NULL_VERIFY(x, y) Verify (x != NULL, "Obejto "#x" esta nulo.", y);

//ExceptionHandle (char* pszFile, char* pszFunction, int nFileLine, int nCode, char* pszMessage);
#define VERIFYC(x,c,y,z...) if (!(x)) { SetExceptionCode (c); VERIFY (x,y,##z); } else { errno = 0; }
#define VERIFY(x,y, z...) if (!(x)) { ExceptionHandle (__FILE__, __PRETTY_FUNCTION__, __LINE__, #x, y [0] == '\0' ? strerror (errno) : y, ##z); IfException (); throw this;  } else { errno = 0; }

//Exception by throwing a char* instead
#define CHECK(x,y) if (!(x)) { _EX_GENERATEGLOBALERROR (x,y); throw strGlobalStrError; }


#define _EX_GENERATEGLOBALERROR(x,y) strGlobalStrError.clear (); strGlobalStrError = strLastException  + __FILE__ + "(" + STRINGIZE(__LINE__) + ") Func: [" + __PRETTY_FUNCTION__ + "] Comm: [" + #x + "] Msg: ["; strGlobalStrError = strGlobalStrError + "" + (const char*)(y [0] == '\0' ? strerror (errno) : y) + "] ";

#define Verify(x,y,z) if (!(x)) { _EX_GENERATEGLOBALERROR (x,y);  YYTRACE ("%s", strGlobalStrError.c_str ()); fputc ('\n', stderr); return z; } else { errno = 0; }

#define Verify2(x,y) if (!(x)) { _EX_GENERATEGLOBALERROR (x,y); throw strGlobalStrError; }

#define Assert(x,y,z) if (!(x)) { TRACE ("%s(%u) Func: %s Comm: %s Msg: %s (Errno: [%u])\n", __FILE__, __LINE__, __PRETTY_FUNCTION__, #x, y [0] == '\0' ? strerror (errno) : y, errno); exit (z); } else { errno = 0; }


#define ExceptionWhith(){\
		char* pszFile;\
		char* pszFunction;\
		int   nFileLine;\
		char* pszCode;\
		char* pszMessage;\
\
		pSocket->GetExceptionData (pszFile, pszFunction, &nFileLine, pszCode, pszMessage);\
		ExceptionHandle (pszFile, pszFunction, nFileLine, pszCode, pszMessage);\
	}

#define SAFENEW(NewAlloc, y, z...) try { NewAlloc; } catch (Exception& pException) { ExceptionHandle (__FILE__, __PRETTY_FUNCTION__, __LINE__, #NewAlloc, y [0] == '\0' ? strerror (errno) : y, ##z); IfException (); throw this; }
#define SafeNew(NewAlloc, y) try { NewAlloc; } catch (Exception& pException) { throw y [0] == '\0' ? strerror (errno) : y; }


class API_EXPORT Exception
{
private:
	long unsigned int nExceptionCode;
	const char*		pszFunction;
	const char*		pszFile;
	int				nFileLine;
	const char*		pszCode;	
	char            pszExceptionMessage [EXCEPTION_MESSAGE_SIZE + 1];
	char			pszMessage [EXCEPTION_MESSAGE2_SIZE + 1];

public:

    void SetExceptionCode (int nExceptionCode);
    int GetThrownExceptionCode ();

	void ExceptionHandle (const char* pszFile, const char* pszFunction, int nFileLine, const char* pszCode,  const char* pszFormat, ...);
	
	bool GetExceptionData (const char* pszFile, const char* pszFunction, int* nFileLine, const char* pszCode, const char* pszMessage);

	//bool  GetExceptionData (char* pszFile, char* pszFunction, int* nFileLine, char* pszCode, char* pszMessage);
	char* GetExceptionMessage ();
    void IfException ();
    
    API_EXPORT Exception () {  return; }
};

#endif


File: /MikrotikManager\librouteros.cpp
/*
    librouteros-api - Connect to RouterOS devices using official API protocol
    Copyright (C) 2012-2013, Håkon Nessjøen <haakon.nessjoen@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*/
#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32
#  define strdup _strdup
#  include <winsock2.h>
#else
#  include <sys/types.h>
#  include <sys/socket.h>
#  include <netinet/in.h>
#  include <arpa/inet.h>
#  include <unistd.h>
#  include <errno.h>
#  include <sys/uio.h>
#  include <fcntl.h>
#endif
#include <string.h>
#include <stdarg.h>
#include "Util.h"
#include "Exception.h"
#include "librouteros.h"

static void ros_remove_event(struct ros_connection *conn, int index);

static int debug = 0;

#ifdef _WIN32
#define snprintf _snprintf
static int is_connected (SOCKET socket) {
	char data;
	int len = recv(socket, &data, 1, MSG_PEEK);
	if (len < 0) {
		return WSAGetLastError() == WSAEWOULDBLOCK ? 1 : 0;
	}
	return len > 0 ? 1 : 0;
}
static int _read (SOCKET socket, char *data, int len) {
	int rlen = recv(socket, data, len, 0);
	if (rlen == SOCKET_ERROR) return -1;
	return rlen;
}
static int _write(SOCKET socket, char *data, int len) {
	int wlen = send(socket, data, len, 0);
	if (wlen == SOCKET_ERROR) return -1;
	return wlen;
}
#else
static int is_connected (int socket) {
	char data;
	int len = (int) recv(socket, &data, 1, MSG_PEEK);
	if (len < 0) {
		return errno == EWOULDBLOCK ? 1 : 0;
	}
	return len > 0 ? 1 : 0;
}
#define _read(s,d,l) read(s,d,l)
#define _write(s,d,l) write(s,d,l)
#endif

static int send_length(struct ros_connection *conn, int len) {
	char data[4];
	int written;
	int towrite;

	if (len < 0x80) {
		data[0] = (char)len;
		written = (int) _write(conn->socket, data, 1);
		towrite = 1;
	}
	else if (len < 0x4000) {

		len = htons(len);
		memcpy(data, &len, 2);
		data[0] |= 0x80;

		written = (int) _write(conn->socket, data, 2);
		towrite = 2;
	}
 	else if (len < 0x200000)
	{
		len = htonl(len);
		memcpy(data, &len, 3);
		data[0] |= 0xc0;
		written = (int) _write(conn->socket, data, 3);
		towrite = 3;
	}
	else if (len < 0x10000000)
	{
		len = htonl(len);
		memcpy(data, &len, 4);
		data[0] |= 0xe0;
		written = (int) _write(conn->socket, data, 4);
		towrite = 4;
	}
	else  // this should never happen
	{
		printf("length of word is %d\n", len);
		printf("word is too long.\n");
		exit(1);
	}
	return written == towrite ? 1 : 0;
}

static int readLen(struct ros_connection *conn)
{
	char data[4];

	memset(data, 0, 4);
	if (_read(conn->socket, data, 1) != 1) {
		return -1;
	}

	if ((data[0] & 0xE0) == 0xE0) {
		if (_read(conn->socket, data + 1, 3) != 3) {
			return -1;
		}
		printf("Giant packet: %d\n", *((int *)data));
		return *((int *)data);
	}
	else if ((data[0] & 0xC0) == 0XC0) {
		data[0] &= 0x3f;        // mask out the 1st 2 bits
		if (_read(conn->socket, data + 1, 2) != 2) {
			return -1;
		}
		printf("Lesser small packet: %d\n", *((int *)data));
		return *((int *)data);
	}
	else if ((data[0] & 0x80) == 0x80) {
		data[0] &= 0x7f;        // mask out the 1st bit
		if (_read(conn->socket, data + 1, 1) != 1) {
			return -1;
		}
		printf("Less small packet: %d\n", *((int *)data));
		return *((int *)data);
	}
	else {
		return *((int *)data);
	}
	return 0;
}

static int md5toBin(unsigned char *dst, char *hex) {
	int i;
	char convert[3];
	unsigned int data;

	if (strlen(hex) != 32)
		return 0;

	convert[2] = 0;
	for(i = 0; i < 32; i+=2) {
		memcpy(convert, hex + i, 2);
		sscanf(convert, "%x", &data);
		dst[i/2] = data & 0xff;
	}
	dst[i] = 0;

	return 1;
}

static int bintomd5(char *dst, unsigned char *bin) {
	int i;

	for (i = 0; i < 16; ++i) {
		sprintf(dst+(i<<1), "%02x", bin[i] & 0xFF);
	}
	dst[i<<1] = 0;
	return 1;
}

void ros_set_type(struct ros_connection *conn, enum ros_type type)
{
	int blocking = 0;
	int flags;

	conn->type = type;

	if (type == ROS_EVENT) {
		blocking = 1;
	}

#ifndef _WIN32
	flags = fcntl(conn->socket, F_GETFL, 0);
	if (flags < 0) {
		fprintf(stderr, "Error getting socket flags\n");
		exit(1);
	}

	flags = blocking ? (flags & ~O_NONBLOCK) : (flags | O_NONBLOCK);
#endif

#ifdef _WIN32
	if (ioctlsocket(conn->socket, FIONBIO, &blocking) == SOCKET_ERROR) {
#else
	if (fcntl(conn->socket, F_SETFL, flags) != 0) {
#endif
		fprintf(stderr, "Could not set socket to non-blocking mode\n");
		exit(1);
	}
}

static void ros_handle_events(struct ros_connection *conn, struct ros_result *result) {
	if (conn->max_events > 0) {
		int i;
		char *key = ros_get_tag(result);
		if (key == NULL) {
			/* Event with no tag */
			return;
		}
		key = strdup(key);
		if (key == NULL) {
			fprintf(stderr, "Cannot allocate memory\n");
			exit(1);
		}
		for (i = 0; i < conn->max_events; ++i) {
			if (conn->events[i]->inuse && strcmp(key, conn->events[i]->tag) == 0) {
				if (result->done) {
					ros_remove_event(conn, i);
				}
				conn->events[i]->callback(result);
				free(key);
				return;
			}
		}
		fprintf(stderr, "warning: unhandeled event with tag: %s\n", key);
		ros_result_free(result);
		free(key);
	}
}

int ros_runloop_once(struct ros_connection *conn, void (*callback)(struct ros_result *result)) {
	/* Make sure the connection/instance is event based */
	if (conn->type != ROS_EVENT) {
		fprintf(stderr, "Warning! Connection type was not set to ROS_EVENT. Forcing change.\n");
		ros_set_type(conn, ROS_EVENT);
	}

	if (!is_connected(conn->socket)) {
		return 0;
	}

	if (conn->expected_length == 0)
    {
		conn->expected_length = readLen(conn);
		if (conn->expected_length > 0) {
			conn->length = 0;
			//conn->buffer = (unsigned char*)malloc(sizeof(char) * (conn->expected_length + 1));

            /*
			if (conn->buffer == NULL) {
				fprintf(stderr, "Could not allocate memory for packet\n");
				exit(1);
			}
            */
            
			/* Check for more data at once */
			ros_runloop_once(conn, callback);
		}
        else if (conn->expected_length == 0)
        {
			// Sentence done
			// call callback
			struct ros_result *res = conn->event_result;
			if (res->sentence->words > 0) {
				if (strcmp(res->sentence->word[0], "!done") == 0) {
					res->done = 1;
				}
				if (strcmp(res->sentence->word[0], "!re") == 0) {
					res->re = 1;
				}
				if (strcmp(res->sentence->word[0], "!trap") == 0) {
					res->trap = 1;
				}
				if (strcmp(res->sentence->word[0], "!fatal") == 0) {
					res->fatal = 1;
				}
			}
			if (debug) {
				int i;
				for (i = 0; i < res->sentence->words; ++i) {
					TRACE ("< %s\n", res->sentence->word[i]);
				}
			}
			if (callback != NULL) {
				callback(res);
			} else {
				ros_handle_events(conn, res);
			}
			conn->event_result = NULL;
		}
	}
    else

    {
		int to_read = conn->expected_length - conn->length;
		int got = (int) _read(conn->socket, conn->buffer + conn->length, to_read);

		if (got < 0)
        {
			return 0;
		}

        if (got == to_read)
        {
			struct ros_result *res;

            if (conn->event_result == NULL)
            {
				conn->event_result = (struct ros_result*) malloc(sizeof(struct ros_result));

                if (conn->event_result == NULL)
                {
					fprintf(stderr, "Error allocating memory for event result\n");
					exit(1);
				}

				memset(conn->event_result, 0, sizeof(struct ros_result));

                conn->event_result->sentence = ros_sentence_new();
				conn->event_result->done = 0;
				conn->event_result->re = 0;
				conn->event_result->trap = 0;
				conn->event_result->fatal = 0;
			}
			res = conn->event_result;
			conn->buffer[conn->length+to_read] = '\0';
			ros_sentence_add(res->sentence, (char *)conn->buffer);

			//free(conn->buffer);
			//conn->buffer = NULL;
            
			conn->expected_length = 0;
			conn->length = 0;
		}
	}
	return 1;
}



struct ros_connection *ros_connect(char *address, int port)
{
	struct sockaddr_in s_address;
	struct ros_connection *conn = (struct ros_connection*) malloc(sizeof(struct ros_connection));

#ifdef _WIN32
	WSADATA wsaData;
	int retval;
#endif

	if (conn == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		exit(1);
	}

#ifdef _WIN32
	if ((retval = WSAStartup(0x202, &wsaData)) != 0) {
		fprintf(stderr,"Server: WSAStartup() failed with error %d\n", retval);
		free(conn);
		return NULL;
	}
#endif

	conn->expected_length = 0;
	conn->length = 0;
	conn->event_result = NULL;
	conn->events = NULL;
	conn->max_events = 0;

	conn->socket = socket(AF_INET, SOCK_STREAM, 0);
	if (conn->socket < 0) {
#ifdef _WIN32
		WSACleanup();
#endif
		free(conn);
		return NULL;
	}

	s_address.sin_family = AF_INET;
	s_address.sin_addr.s_addr = inet_addr(address);
	s_address.sin_port = htons(port);

	if (
		connect(conn->socket, (struct sockaddr *)&s_address, sizeof(s_address)) ==
#ifdef _WIN32
		SOCKET_ERROR
#else
		-1
#endif
	) {
#ifdef _WIN32
		closesocket(conn->socket);
		WSACleanup();
#else
		close(conn->socket);
#endif
		free(conn);
		return NULL;
	}

	return conn;
}

int ros_disconnect(struct ros_connection *conn) {
	int result = 0;
#ifdef _WIN32
	if (closesocket(conn->socket) == SOCKET_ERROR) {
		result = -1;
	}
#else
	result = close(conn->socket);
#endif

	if (conn->max_events > 0) {
		int i;
		for (i = 0; i < conn->max_events; ++i) {
			free(conn->events[i]);
			conn->events[i] = NULL;
		}
		free(conn->events);
		conn->events = NULL;
	}
	free(conn);
#ifdef _WIN32
	WSACleanup();
#endif

	return result;
}

void ros_result_free(struct ros_result *result) {
	ros_sentence_free(result->sentence);
	result->sentence = NULL;
	free(result);
}

int strcmp2(char *a, char *b) {
	int i = 0;
	while (1) {
		if (a[i] == 0) {
			return 1;
		}
		if (a[i] != b[i]) {
			return 0;
		}
		i++;
	}
}

char *ros_get_tag(struct ros_result *result) {
	return ros_get(result, (char*) ".tag");
}

char *ros_get(struct ros_result *result, char *key) {
	int i,keylen;
	char *search;
	if (result == NULL)
		return NULL;

	keylen = (int) strlen(key);
	search = (char*) malloc(sizeof(char) * (keylen + 2));
	if (search == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		exit(1);
	}
	memcpy(search, key, keylen);
	search[keylen] = '=';
	search[keylen+1] = '\0';

	for (i = 0; i < result->sentence->words; ++i) {
		if (strcmp2(search, result->sentence->word[i])) {
			free(search);
			return result->sentence->word[i] + keylen + 1;
		}
	}
	free(search);
	return NULL;
}

struct ros_result *ros_read_packet(struct ros_connection *conn) {
	struct ros_result *ret = (ros_result *) malloc(sizeof(struct ros_result));
	int len;

	if (ret == 0) {
		fprintf(stderr, "Could not allocate memory.");
		exit(1);
	}

	memset(ret, 0, sizeof(struct ros_result));
	ret->done = 0;
	ret->re = 0;
	ret->trap = 0;
	ret->fatal = 0;
	ret->sentence = ros_sentence_new();

	do {
		char *buffer;
		len = readLen(conn);
		if (len < 0) return NULL;

		buffer = (char *) malloc(sizeof(char) * (len + 1));
		if (buffer == NULL) {
			fprintf(stderr, "Could not allocate memory.");
			exit(1);
		}

		if (len > 0) {
			_read(conn->socket, buffer, len);
			buffer[len] = '\0';

            //TRACE ("\nRECV: [%s]\n", buffer);

			ros_sentence_add(ret->sentence, buffer);
		}
		free(buffer);

	} while (len > 0);
	if (ret->sentence->words > 0) {
		if (strcmp(ret->sentence->word[0], "!done") == 0) {
			ret->done = 1;
		}
		if (strcmp(ret->sentence->word[0], "!re") == 0) {
			ret->re = 1;
		}
		if (strcmp(ret->sentence->word[0], "!trap") == 0) {
			ret->trap = 1;
		}
		if (strcmp(ret->sentence->word[0], "!fatal") == 0) {
			ret->fatal = 1;
		}
	}
	if (debug) {
		int i;
		for (i = 0; i < ret->sentence->words; ++i) {
			TRACE ("< %s\n", ret->sentence->word[i]);
		}
	}

	return ret;
}

struct ros_sentence *ros_sentence_new() {
	struct ros_sentence *res = (struct ros_sentence *) malloc(sizeof(struct ros_sentence));
	res->words = 0;
	res->word = (char **) malloc(sizeof(char *) * 100);
	memset(res->word, 0, sizeof(char *) * 100);
	if (res->word == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		exit(1);
	}
	return res;
}

void ros_sentence_free(struct ros_sentence *sentence) {
	int i;
	if (sentence == NULL) return;

	for (i = 0; i < sentence->words; ++i) {
		free(sentence->word[i]);
		sentence->word[i] = NULL;
	}
	free(sentence->word);
	sentence->word = NULL;
	free(sentence);
}

void ros_sentence_add(struct ros_sentence *sentence, char *word) {
	if ((sentence->words+1) / 100 > sentence->words / 100) {
		sentence->word = (char **) realloc(sentence->word, sizeof(char *) * ((((sentence->words+1)/100) + 1)*100));
		if (sentence->word == NULL) {
			fprintf(stderr, "Error allocating memory\n");
			exit(1);
		}
	}

	sentence->word[sentence->words] = strdup(word);
	if (sentence->word[sentence->words] == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		exit(1);
	}
	sentence->words++;
}

static struct ros_sentence *ros_va_to_sentence(va_list ap, char *first, char *second) {
	int i = 0;
	struct ros_sentence *res = ros_sentence_new();

	while (1) {
		char *word;
		if (i == 0) {
			word = first;
		}
		else if (i == 1) {
			if (second != NULL) {
				word = second;
			} else {
				++i;
				continue;
			}
		} else {
			word = va_arg(ap, char *);
			if (word == NULL) {
				break;
			}
		}

		ros_sentence_add(res, word);
		++i;
	}
	return res;
}


int ros_send_command_args(struct ros_connection *conn, char **args, int num) {
	int i = 0, len = 0;
	char *arg;
	if (num == 0) return 0;

	arg = args[i];
	while (arg != 0 && (len = (int) strlen(arg)) != 0) {
		if (send_length(conn, len) == 0) {
			return 0;
		}
		if (_write(conn->socket, arg, len) != len) {
			return 0;
		}
		if (debug) {
			TRACE ("> %s\n", arg);
		}
		arg = args[++i];
	}

	/* Packet termination */
	if (send_length(conn, 0) == 0) {
	  return 0;
	}

	return 1;
}

int ros_send_sentence(struct ros_connection *conn, struct ros_sentence *sentence) {
	if (conn == NULL || sentence == NULL) {
		return 0;
	}

	return ros_send_command_args(conn, sentence->word, sentence->words);
}

static int ros_send_command_va(struct ros_connection *conn, char *extra, char *command, va_list ap) {
	struct ros_sentence *sentence;
	int result;
	
	sentence = ros_va_to_sentence(ap, command, extra);
	result = ros_send_sentence(conn, sentence);
	ros_sentence_free(sentence);
	return result;
}

void ros_add_event(struct ros_connection *conn, struct ros_event *event) {
	int idx = 0;
	char isnew = 0;

	if (conn->events == NULL) {
		conn->max_events = 1;
		conn->events = (struct ros_event**) malloc(sizeof(struct ros_event **));
		idx = 0;
		isnew = 1;
	} else {
		int i;
		idx = -1;
		for (i = 0; i < conn->max_events; ++i) {
			if (conn->events[i]->inuse == 0) {
				idx = i;
				break;
			}
		}
		if (idx == -1) {
			isnew = 1;
			idx = conn->max_events++;
			conn->events = (struct ros_event**) realloc(conn->events, sizeof(struct ros_event **) * conn->max_events);
			if (conn->events == NULL) {
				fprintf(stderr, "Error allocating memory\n");
				exit(1);
			}
		}
	}
	if (isnew) {
		conn->events[idx] = (struct ros_event*) malloc(sizeof(struct ros_event));
		if (conn->events[idx] == NULL) {
			fprintf(stderr, "Error allocating memory\n");
		}
	}
	memcpy(conn->events[idx], event, sizeof(struct ros_event));
	conn->events[idx]->inuse = 1;
}

static void ros_remove_event(struct ros_connection *conn, int index) {
	if (index < conn->max_events) {
		conn->events[index]->inuse = 0;
	}
}

/* NB! Blocking call. TODO: Fix */
int ros_cancel(struct ros_connection *conn, int id) {
	char iddata[1024];
	int returnval;
	struct ros_result *res;
	int was_event = conn->type == ROS_EVENT;
	
	snprintf(iddata, 1024, "=tag=%d", id);
	if (was_event) {
		ros_set_type(conn, ROS_SIMPLE);
	}
	res = ros_send_command_wait(conn, (char*) "/cancel", iddata, NULL);
	if (was_event) {
		ros_set_type(conn, ROS_EVENT);
	}
	if (res == NULL) {
		return 0;
	}
	if (res->done) {
		returnval = 1;
	} else {
		returnval = 0;
	}
	ros_result_free(res);
	return returnval;
}

/* Returns .tag id */
int ros_send_command_cb(struct ros_connection *conn, void (*callback)(struct ros_result *result), char *command, ...) {
	int result;
	int id;
	struct ros_event *event = (ros_event *) malloc(sizeof(struct ros_event));
	char extra[120];
	va_list ap;

	if (event == NULL) {
		fprintf(stderr, "Error allocating memory\n");
		exit(1);
	}

	id = rand();
	sprintf(event->tag, "%d", id);
	sprintf(extra, ".tag=%s", event->tag);
	event->callback = callback;

	ros_add_event(conn, event);
	free(event);

	va_start(ap, command);
	result = ros_send_command_va(conn, extra, command, ap);
	va_end(ap);

	return result > 0 ? id : 0;
}

int ros_send_sentence_cb(struct ros_connection *conn, void (*callback)(struct ros_result *result), struct ros_sentence *sentence, uint32_t nTag) {
	int result;
	int id;
	struct ros_event *event = (ros_event *) malloc(sizeof(struct ros_event));
	char extra[120];

	if (event == NULL) {
		TRACE ("Error allocating memory\n");
		return -1;
	}

	id = nTag;

	sprintf(event->tag, "%d", id);
	sprintf(extra, ".tag=%s", event->tag);
	event->callback = callback;

	ros_add_event(conn, event);
	free(event);

	ros_sentence_add(sentence, extra);
	result = ros_send_sentence(conn, sentence);

	return result > 0 ? id : 0;
}


int ros_send_command(struct ros_connection *conn, char *command, ...) {
	int result;
	va_list ap;
	va_start(ap, command);
	result = ros_send_command_va(conn, NULL, command, ap);
	va_end(ap);
	return result;
}

struct ros_result *ros_send_command_wait(struct ros_connection *conn, char *command, ...) {
	int result;

	va_list ap;
	va_start(ap, command);
	result = ros_send_command_va(conn, NULL, command, ap);
	va_end(ap);

	if (result == 0) {
		return NULL;
	}
	/* Read packet */
	return ros_read_packet(conn);
}

/* TODO: write with events */
int ros_login(struct ros_connection *conn, char *username, char *password) {
	int result;
	unsigned char buffer[1024];
	char *userWord;
	char passWord[45];
	char *challenge;
	struct ros_result *res;
	char md5sum[17];
	md5_state_t state;

	res = ros_send_command_wait(conn, (char*) "/login", NULL);

	memset(buffer, 0, sizeof(buffer));

	challenge = ros_get(res, (char*) "=ret");
	if (challenge == NULL) {
		fprintf(stderr, "Error logging in. No challenge received\n");
		exit(1);
	}
	md5toBin(buffer + 1, challenge);

	md5_init(&state);
	md5_append(&state, buffer, 1);
	md5_append(&state, (unsigned char *)password, (int) strlen(password));
	md5_append(&state, buffer + 1, 16);
	md5_finish(&state, (md5_byte_t *)md5sum);
	ros_result_free(res);

	strcpy((char *)buffer, "00");
	bintomd5((char *)buffer + 2, (unsigned char *)md5sum);

	strcpy(passWord, "=response=");
	strcat(passWord, (char *)buffer);
	passWord[44] = '\0';

	userWord = (char *) malloc(sizeof(char) * (6 + strlen(username) + 1));
	strcpy(userWord, "=name=");
	strcat(userWord, username);
	userWord[6+strlen(username)] = 0;

	res = ros_send_command_wait(conn, (char*) "/login",
		userWord,
		passWord,
		NULL
	);

	free(userWord);

	// '!done' flag == successful login
	if (res != NULL) {
		result = res->done;
		ros_result_free(res);
	} else {
		result = 0;
	}

	return result;
}

    
    
    
    
/* This class was consolidated within a original librouteros provided by Mirotik site. */
    
MikrotikLib::MikrotikLib (const char* pszServerAddress, uint nPortServer, const char* pszUser, const char* pszPassword)
{
    Assert (pszServerAddress != NULL, "pszServerAddress as define NULL.", 100);
    Assert (pszUser != NULL, "pszUser define as NULL.", 100);
    Assert (pszPassword != NULL, "pszPassword defined as NULL.", 100);
    

    
	Assert ((conn = ros_connect ((char*) pszServerAddress, nPortServer)) != NULL, "Error connection to the Server.", 101);

    //TRACE ("Connection stablished.\n");
	
	ros_set_type(conn, ROS_EVENT);

    Assert ((ros_login (conn, (char*) pszUser, (char*) pszPassword)) == true, "Error logging in.", 100);

    //TRACE ("Login done.\n");

    strServer = pszServerAddress;
    nPort = nPortServer;
    strUser = pszUser;
    strPasswd = pszPassword;

}




MikrotikLib::~MikrotikLib()
{
    ros_disconnect (conn);
}




//Default exception caller just info.
void MikrotikLib::IfException()
{
    YYTRACE ("Exception being throw by MikrotikLib class.\n");
}



    

uint32_t MikrotikLib::SendCommand (const char *pszCommand, void (*pHandle)(struct ros_result*), uint32_t nTag)
{
    uint32_t nAssignTag;
    string strCommand = "";
    char chrCurrentChar;
    bool bStringData = false;
    uint nDataCount = 0;

    //VERIFY (is_connected(conn->socket) == true, "Error, Server disconected.");

    Sentence = ros_sentence_new ();
    //Command Parser
    while (*pszCommand != '\0')
    {
        chrCurrentChar = *pszCommand; pszCommand++;

        //Processing a new term
        if (chrCurrentChar == ' ' && bStringData == false)
        {
            if (nDataCount == 0)
            {
                //Mikrotik Command
                //TRACE ("Command: [%s]\n", strCommand.c_str());

                ros_sentence_add (Sentence, (char*) strCommand.c_str());
            }
            else
            {
                //Mikrotik arguments
                //TRACE ("Arguments: =[%s]\n", strCommand.c_str());

                ros_sentence_add (Sentence, (char*) strCommand.c_str());
            }

            strCommand.clear();
            nDataCount++;

            // stripping off spaces.
            while (*pszCommand == ' ') pszCommand++;
            continue;
        }
        else if (chrCurrentChar == '"' && bStringData == false)
        {
            bStringData = true;
        }
        else if (chrCurrentChar == '"' && bStringData == true)
        {
            bStringData = false;
        }

        strCommand.push_back (chrCurrentChar);
    }

    VERIFY (bStringData == false, "Error, argument [%s] no closed.\n", strCommand.c_str());

    if (strCommand.length() > 0)
    {
        ros_sentence_add (Sentence, (char*) strCommand.c_str ());
        strCommand.clear ();
    }
    //Sending command and releasing SentenceData used.

    VERIFY ((nAssignTag = ros_send_sentence_cb (conn, pHandle, Sentence, nTag)) > 0, "Error sending sentence data to Mikrotik.");

    ros_sentence_free (Sentence);

    //VERIFY (is_connected(conn->socket) == true, "Error, Server disconected.");

    return nAssignTag;
}



void MikrotikLib::ProcessLoopOnce()
{
    //debug = 1;

    timeout.tv_sec = 1;
    timeout.tv_usec = 0;

    FD_ZERO(&read_fds);
    FD_SET(conn->socket, &read_fds);

    int reads;

    reads = select(conn->socket + 1, &read_fds, NULL, NULL, &timeout);
    if (FD_ISSET(conn->socket, &read_fds))
    {
        timeout.tv_sec = 0;
        timeout.tv_usec = 500;

        FD_ZERO(&read_fds);
        FD_SET(conn->socket, &read_fds);

        while (select(conn->socket + 1, &read_fds, NULL, NULL, &timeout))
        {
            VERIFY (is_connected(conn->socket) == true, "Error, Server disconected.");

            /* handle incoming data with specified callback */
            VERIFY (ros_runloop_once(conn, NULL) != 0, "Error, executing loop transaction. reconnect.");
        }
    }

    //debug = 0;
}
    
    
void MikrotikLib::SetDebug (bool bdebug)
{
    debug = bdebug == true ? 1 : 0;
}



File: /MikrotikManager\librouteros.h
 /*
    librouteros-api - Connect to RouterOS devices using official API protocol
    Copyright (C) 2012-2013, Håkon Nessjøen <haakon.nessjoen@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*/

#ifndef MIKROTIKLIB
#define MIKROTIKLIB

#define ROS_PORT 8728

#include <Util.h>
#include <Exception.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>


struct ros_sentence {
	char **word;
	int words;
};

struct ros_result {
	struct ros_sentence *sentence;
	char done;
	char re;
	char trap;
	char fatal;
};

struct ros_event {
	char tag[100];
	void (*callback)(struct ros_result *result);
	char inuse;
};

enum ros_type {
    ROS_SIMPLE,
    ROS_EVENT
};


struct ros_connection {
	enum ros_type type;
#ifdef _WIN32
	SOCKET socket;
#else
	int socket;
#endif
	unsigned char buffer [512];
	struct ros_event **events;
	int max_events;
	struct ros_result *event_result;
	int expected_length;
	int length;
};

#ifdef __cplusplus
extern "C"
{
#endif
    /* event based functions */
    int ros_send_command(struct ros_connection *conn, char *command, ...);
    void ros_set_type(struct ros_connection *conn, enum ros_type type);
    int ros_runloop_once(struct ros_connection *conn, void (*callback)(struct ros_result *result));
    int ros_send_command_cb(struct ros_connection *conn, void (*callback)(struct ros_result *result), char *command, ...);
    int ros_send_sentence_cb(struct ros_connection *conn, void (*callback)(struct ros_result *result), struct ros_sentence *sentence, uint32_t nTag);
    
    /* blocking functions */
    struct ros_result *ros_send_command_wait(struct ros_connection *conn, char *command, ...);
    struct ros_result *ros_read_packet(struct ros_connection *conn);
    int ros_login(struct ros_connection *conn, char *username, char *password);
    int ros_cancel(struct ros_connection *conn, int id);
    
    /* common functions */
    struct ros_connection *ros_connect(char *address, int port);
    int ros_disconnect(struct ros_connection *conn);
    void ros_result_free(struct ros_result *result);
    char *ros_get(struct ros_result *result, char *key);
    char *ros_get_tag(struct ros_result *result);
    
    /* sentence functions */
    struct ros_sentence *ros_sentence_new();
    void ros_sentence_free(struct ros_sentence *sentence);
    void ros_sentence_add(struct ros_sentence *sentence, char *word);
    
#ifdef __cplusplus
}
#endif


class MikrotikLib : Exception
{
private:
    struct ros_connection *conn;
    struct ros_sentence *Sentence;
    fd_set read_fds;

    string strServer;
    uint   nPort;
    string strUser;
    string strPasswd;

    struct timeval timeout;

protected:
    
public:
    MikrotikLib (const char* pszServerAddress, uint nPortServer, const char* pszUser, const char* pszPassword);
    ~MikrotikLib ();

    void IfException ();
    
    /* Send command to Mikrotik and return the .tag given. */
    uint32_t SendCommand (const char* pszCommand, void (*pHandle)(struct ros_result*), uint32_t nTag);

    void ProcessLoopOnce ();
    
    void SetDebug (bool bdebug);
};

#endif






File: /MikrotikManager\main.cpp
//
//  main.cpp
//  MikrotikManager
//
//  Created by Gustavo Campos on 6/6/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
//
/*
MIT License

Copyright (c) 2017 Luiz Gustavo de Campos

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
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
#include <string>
#include <unistd.h>
#include <Terminal.h>
#include <Variant.h>
#include "librouteros.h"
#include "main.h"
#include <algorithm>
#include <whois.h>

#include <stdio.h>

using namespace std;

map<string,string> mapHostDictionary;

map<string, struct IPUsage> pHostList;
string strIPInterfaceMonitoring;
bool bIPMonitoringConnected = false;
bool bIPMonitoringIP = false;
bool bProfileMonitor = false;


map<string, struct MktProfile *> mapProfiling;

vector<struct MktProfile*> vProfilling, vShowProfile;
uint32_t  nTotalProfiling;




map<string, struct Interfaces*> mapInterfaces;

extern char **environ;

uint nColumns;
uint nLines;

struct ros_connection *conn;
volatile int do_continue = 0;




map<string, struct IPMonitoring> mapMonitoring;
/* ------------------------------------- */



void handledata(struct ros_result *result) {
	int i;
    static string strData = "";

	if (result->re)
    {
		//printf("--\n");
        printf ("Line: %s\n", strData.c_str());
        strData.clear();
	}
	if (result->trap)
    {
		printf("!trap Error following: \n");
	}
	if (result->fatal)
    {
		printf("!fatal: \n");
	}

	for (i = 1; i < result->sentence->words; ++i)
    {
		//printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
	}
	if (result->done) {
		printf("== Ending command.\n\n");
        strData.clear();
	}
    
	ros_result_free(result);
}



struct IPUsage* ClainIPUsage (string strHost)
{
    map<string, struct IPUsage> pHost;
    map<string, struct IPUsage>::iterator pHosti;

    struct IPUsage* classIPusage;

    //Finding if the data exists
    pHosti = pHostList.find (strHost);

    
    if (pHosti == pHostList.end())
    {
        //TRACE ("Creating new memory for %s\n", strHost.c_str());
        classIPusage = new struct IPUsage;
        memset ((void*) classIPusage, 0, sizeof (struct IPUsage));
    }
    else
    {
        //TRACE ("Returning alread stored [%X] Key: [%s]\n", (*pHosti).second, (*pHosti).first.c_str());
        classIPusage = &(*pHosti).second;
    }

    return classIPusage;
}




void IPUsageHandle (struct ros_result *result)
{
	int i;
    static string strData = "";
    static char szNumber [30] = "";


	if (result->trap)
    {
		printf("!trap Error following: \n");
        bIPMonitoringIP = false;
	}
	if (result->fatal)
    {
		printf("!fatal: \n");
	}

	for (i = 1; i < result->sentence->words; ++i)
    {
		//printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
	}

    if (result->re)
    {
        static char szSrcAddress [40];
        static bool bFirst = true;

        szSrcAddress [0] = '\0';

        if (TUtil_GetValueFromResponse2 (strData.c_str(), "src-address", szSrcAddress, sizeof (szSrcAddress) - 1, ';', '=') == false)
        {
            snprintf (szSrcAddress, sizeof (szSrcAddress) - 1, "TOTAL");

            bFirst = false;
        }

        if (bFirst == true)
        {
            bFirst = false;

            /* Populating data */
            map<string, struct IPUsage>::iterator pHostListi;

            for (pHostListi = pHostList.begin(); pHostListi != pHostList.end(); pHostListi++)
            {
                pHostListi->second.nTXbps = 0;
                pHostListi->second.nTXPackets = 0;
                pHostListi->second.nRXbps = 0;
                pHostListi->second.nRXPackets = 0;
                pHostListi->second.nCountConnections = 0;
                pHostListi->second.pvecConnections.clear();
            }
        }



        struct IPUsage* pIPUsage = ClainIPUsage ((const char*) szSrcAddress);


        snprintf (pIPUsage->szSrcAddress, sizeof (pIPUsage->szSrcAddress) - 1, "%s", szSrcAddress);


        TUtil_GetValueFromResponse2 (strData.c_str(), "tx", szNumber, sizeof (szNumber) - 1, ';', '=');
        pIPUsage->nRXbps = strtod (szNumber, NULL) / 1024;

        TUtil_GetValueFromResponse2 (strData.c_str(), "tx-packets", szNumber, sizeof (szNumber) - 1, ';', '=');
        pIPUsage->nRXPackets = strtod (szNumber, NULL) / 1024;

        TUtil_GetValueFromResponse2 (strData.c_str(), "rx", szNumber, sizeof (szNumber) - 1, ';', '=');
        pIPUsage->nTXbps = strtod (szNumber, NULL) / 1024;

        TUtil_GetValueFromResponse2 (strData.c_str(), "rx-packets", szNumber, sizeof (szNumber) - 1, ';', '=');
        pIPUsage->nTXPackets = strtod (szNumber, NULL) / 1024;



        //printf("\n%s\n", strData.c_str());

        //TRACE ("Src-Address....: [%s]\n", pIPUsage->szSrcAddress);
        //TRACE ("TX: [%.2f] kbps - TX-packets: [%u]\n", (float) pIPUsage->nTXPackets / 8, pIPUsage->nTXPackets);
        //TRACE ("RX: [%.2f] kbps - RX-packets: [%u]\n", (float) pIPUsage->nRXPackets / 8, pIPUsage->nRXPackets);


        strData = pIPUsage->szSrcAddress ;

        //pIPUsage->pvecConnections = NULL;

        pHostList [strData] = *pIPUsage;

        //delete pIPUsage;

        strData.clear();
	}


    if (result->done)
    {
		printf("== Ending command.\n\n");
        strData.clear();
	}
    
	ros_result_free(result);
}



void IPNameStructure (struct ros_result *result)
{
	int i;
    static string strData = "";
    bool bFirst = true;



	if (result->trap)
    {
		printf("!trap Error following: \n");
	}
	if (result->fatal)
    {
		printf("!fatal: \n");
	}

	for (i = 1; i < result->sentence->words; ++i)
    {
		//printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
	}

    if (result->re)
    {
        static char szSrcAddress [40];
        static string strAddress;

        if (bFirst == true)
        {
            //pHostList.clear();
            bFirst = false;
        }

        TUtil_GetValueFromResponse2 (strData.c_str(), "address", szSrcAddress, sizeof (szSrcAddress) - 1, ';', '=');

        strAddress = szSrcAddress;


        struct IPUsage* pIPUsage = ClainIPUsage ((const char*) szSrcAddress);

        snprintf (pIPUsage->szSrcAddress, sizeof (pIPUsage->szSrcAddress) - 1, "%s", szSrcAddress);
        //TUtil_GetValueFromResponse2 (strData.c_str(), "address", pIPUsage->szSrcAddress, sizeof (pIPUsage->szSrcAddress) - 1, ';', '=');

        TUtil_GetValueFromResponse2 (strData.c_str(), "mac-address", pIPUsage->szMacAddress, sizeof (pIPUsage->szMacAddress) - 1, ';', '=');

        TUtil_GetValueFromResponse2 (strData.c_str(), "host-name", pIPUsage->szHostName, sizeof (pIPUsage->szHostName) - 1, ';', '=');

/*
		printf("\n%s\n", strData.c_str());
        
        TRACE  ("Src-Address....: [%s]\n", pIPUsage->szSrcAddress);
        TRACE  ("Mac-Address....: [%s]\n", pIPUsage->szMacAddress);
        TRACE  ("Host.Name......: [%s]\n", pIPUsage->szHostName);
*/

        strData = pIPUsage->szSrcAddress ;

        pHostList [strData] = *pIPUsage;


        strData.clear();
	}


    if (result->done)
    {
        strData.clear();
        bFirst = true;
	}

	ros_result_free(result);
}


bool ShowIPMonitoringSortby (const struct IPConnectionMonitor& pA, const struct IPConnectionMonitor& pB)
{
    return (pA.nTX + pA.nTX > pB.nTX + pB.nRX);
}



bool ShowUsageBoxesSortby (const struct IPUsage& pA, const struct IPUsage& pB)
{
    if (pA.szSrcAddress [0] == 'T') return true;

    if ((pA.nTXbps * pA.nCountConnections) > (pB.nTXbps * pB.nCountConnections))
    {
        return true;
    }

    return false;
}



void ShowUsageBoxes (map<string, struct IPUsage>& pHostList)
{
    vector <struct IPUsage>  pVector;
    vector <struct IPUsage>::iterator  pVectori;

    /* Populating data */
    map<string, struct IPUsage>::iterator pHostListi;

    for (pHostListi = pHostList.begin(); pHostListi != pHostList.end(); pHostListi++)
    {
        pVector.push_back ((*pHostListi).second);
    }

    /* Sorting data */
    sort (pVector.begin(), pVector.end(), ShowUsageBoxesSortby);

    uint nColumns;
    uint nLines;
    uint32_t nCount;
    Term.GetTermSize (&nColumns, &nLines);

    nColumns -= 63;
    nLines   -= (mapInterfaces.size() + 2);



    //TRACE ("Collumns: [%u]  Lines: [%u]\n", nColumns, nLines);

    Term.ResetAttr();
    Term.Box (3, 2, nLines, nColumns, "Live trafic monitoring");

    uint nX, nY;

    nX  = 5; nY = 4;

#define BOXX 7
#define BOXY 20

    struct IPUsage* pHost;
    uint  nBGColor;

    for (pVectori = pVector.begin(); pVectori != pVector.end(); pVectori++)
    {
        //printf ("%10X: Host: [%-20s] MAC: [%s] - [%s] TX: [%-.2f] RX: [%-.2f] \n", &(*pVectori), (*pVectori).szSrcAddress, (*pVectori).szMacAddress, (*pVectori).szHostName, (float) (*pVectori).nRXbps / 8, (float) (*pVectori).nTXbps / 8);

        pHost = (struct IPUsage*) (&(*pVectori));

        if (pHost->nRXbps == 0 && pHost->nTXbps == 0 && pHost->nCountConnections == 0)
        {
            continue;
        }


        if (pHost->nTXbps > ServerAttr.nTXLimit || pHost->nCountConnections > 20)
        {
            nBGColor = 1;
        }
        else if ((float)  (pHost->nTXbps) > ((uint) ServerAttr.nTXLimit * 0.70))
        {
            nBGColor = 3;
        }
        else if (pHost->nRXbps > ServerAttr.nRXLimit)
        {
            nBGColor = 6;
        }
        else
        {
            nBGColor = 2;
        }


        Term.Color (0, 7, nBGColor);

        Term.ClearBox (nX, nY, nX + BOXX, nY + BOXY);

        Term.ColorBright();
        Term.Locate (nX + 1, nY + 2);
        printf ("%s", pHost->szSrcAddress);


        Term.Color (0, 3, nBGColor);
        Term.Locate (nX + 2, nY + 2);
        Term.ColorBright ();
        printf ("%.15s\n", mapHostDictionary.find (pHost->szHostName) == mapHostDictionary.end () ? pHost->szHostName : mapHostDictionary [pHost->szHostName].c_str());

        Term.Color (0, 7, nBGColor);

        Term.Locate (nX + 3, nY + 2);

        if (pHost->nCountConnections > 10) Term.ColorBlink();

        Term.ColorBright ();
        printf ("SOK: %u",  pHost->nCountConnections);


        Term.Color (0, 7, nBGColor);

        Term.Locate (nX + 4, nY + 3); Term.ColorBright ();
        printf ("TX: %u kbps",  pHost->nTXbps);

        Term.Locate (nX + 5, nY + 3); Term.ColorBright ();
        printf ("RX: %u kbps", pHost->nRXbps);

        Term.Color (0, 4, nBGColor); Term.Locate (nX + 7, nY + 2);
        printf ("%s", pHost->szMacAddress);


        nY += (BOXY + 2);

        if (nY + (BOXY + 2) > nColumns) { nY = 4; nX += (BOXX + 2); }

        if (nX + (BOXX + 2) > nLines) break;
    }





    {
        uint nX = 5;

        whois objWhois;
        objWhois.SetCacheTimeout (86400);

        Term.Locate (nX-2, nColumns + 1);
        Term.ColorInvert(); printf ("%-31s", "IP Address     TX Kbps  RX Kbps");

        Term.Color (0,2,0); Term.ColorNormal();

        bool bInfo = false;

        for (pVectori = pVector.begin(); pVectori != pVector.end() && nX < nLines + 2; pVectori++)
        {
            if (pVectori->pvecConnections.size() > 0)
            {
                Term.Locate (nX++, nColumns + 1);

                if (mapHostDictionary.find (pVectori->szHostName) == mapHostDictionary.end())
                {
                    Term.ColorInvert(); printf ("IP: %-27s", pVectori->szSrcAddress);
                }
                else
                {
                    Term.ColorInvert(); printf ("IP: %-27s", mapHostDictionary [(const char*) pVectori->szHostName].c_str());
                }

                if (pVectori->pvecConnections.size() > 1)
                {
                    sort (pVectori->pvecConnections.begin(), pVectori->pvecConnections.end(), ShowIPMonitoringSortby);
                }

                nCount = 0;
                for (vector <struct IPConnectionMonitor>::iterator iteMon = pVectori->pvecConnections.begin(); iteMon != pVectori->pvecConnections.end() && nX < nLines + 2; iteMon++)
                {
                    {
                        Term.Locate (nX++, nColumns + 1);
                        Term.ColorNormal ();
                        if ((iteMon->nRX / 1024) > ServerAttr.nRXLimit / 0.5)
                        {
                            Term.Color (0, 7, 1);
                            Term.ColorBright();
                            Term.ColorBlink();

                            bInfo = true;
                        }
                        else if  ((iteMon->nTX / 1024) > ServerAttr.nRXLimit / 0.5)
                        {
                            Term.Color (0, 7, 6);
                            Term.ColorBright();
                            Term.ColorBlink();

                            bInfo = true;
                        }

                        printf ("%-15s %7.1f %7.1f", iteMon->szDstAddress.c_str(),(double)iteMon->nRX / 1024 , (double)iteMon->nTX /1024);

                        if (bInfo == true)
                        {
                            Term.Color (0, 7, 4);

                            string strCommand = "";
                            bInfo = false;

                            fflush (stdout);
                            try
                            {
                                if ((objWhois.Lookup (iteMon->szDstAddress.c_str(), iteMon->szDstAddress.length())) ==true)
                                {
                                    if (objWhois ["OrgName"] != NULL)
                                    {
                                        Term.Locate (nX, nColumns + 1); printf ("%-31s", " "); Term.Locate (nX++, nColumns + 1);printf ("%.31s", objWhois ["OrgName"]);
                                    }

                                    if (objWhois ["owner"] != NULL)
                                    {
                                        Term.Locate (nX, nColumns + 1); printf ("%-31s", " ");Term.Locate (nX++, nColumns + 1); printf ("%.31s", objWhois ["owner"]);
                                    }

                                    if (objWhois ["person"] != NULL)
                                    {
                                        Term.Locate (nX, nColumns + 1); printf ("%-31s", " ");Term.Locate (nX++, nColumns + 1); printf ("%.31s", objWhois ["person"]);
                                    }

                                    if (objWhois ["country"] != NULL)
                                    {
                                        Term.Locate (nX, nColumns + 1); printf ("%-31s", " ");Term.Locate (nX++, nColumns + 1); printf ("%.31s", objWhois ["country"]);
                                    }
                                }
                            }
                            catch (Exception *pEx)
                            {
                                //Just catch and follow from there, no need to do anything, it will be carried out automatically.
                            }

                        }

                        Term.ColorNormal();
                    }
                }
            }
        }

        /*
         for (map<string, struct IPUsage*>::iterator iteIP = pHostList.begin(); iteIP != pHostList.end() && nX < nLines; iteIP++)
         {
         if (iteIP->second->pvecConnections != NULL && iteIP->second->pvecConnections->size() > 0)
         {
         Term.Locate (nX++, nColumns + 1);
         Term.ColorInvert(); printf ("%-29s", iteIP->second->szSrcAddress);


         for (vector <struct IPConnectionMonitor>::iterator iteMon = iteIP->second->pvecConnections->begin(); iteMon != iteIP->second->pvecConnections->end() && nX < nLines; iteMon++)
         {
         if (&(*iteMon) != NULL)
         {
         Term.Locate (nX++, nColumns + 1);
         Term.ColorInvert(); printf ("  %-29s %8u %8u", "", iteMon->nTX, iteMon->nRX);
         }
         }
         
         }
         }
         */
    }

    fflush (stdout);

    Term.ResetAttr();

    Term.Locate (1, 1);

    fflush (stdout);
}



/* Sorting procedures for Router Usage Profile */
bool ProfileSort (struct MktProfile* pA, struct MktProfile* pB)
{
    return pA->nUsage > pB->nUsage;
}


/* BEST WAY TO PROCESS A ONLINE REQUEST SO FAR */
void ProfileHandler (struct ros_result *result)
{
    int i;
    static string strData = "";
    static Variant objVar;
    static bool bFirst = true;

    bool bOK = false;

    if (result->trap)
    {
        printf("!trap Error following: \n");
        bProfileMonitor = false;
    }
    
    if (result->fatal)
    {
        printf("!fatal: \n");
    }
    else
    {
        bOK = true;
    }

    //printf ("bOK: [%s] - Fatal: [%s] Words: [%d]\n", bOK ? "true" : "false", result->fatal ? "true" : "false", result->sentence->words);
    
    for (i =1; i < result->sentence->words; ++i)
    {
        //printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
    }

    
    if (bOK == true)
    {
        objVar = strData;

        //TRACE ("data: [%s] objVar=[%d]\n", strData.c_str(), objVar.GetCounter());
        
        try
        {

            if (bFirst == true)
            {
                map<string, struct MktProfile*>::iterator mapProfilei;
                //Zeroing data for next collecting event.
                for (mapProfilei = mapProfiling.begin(); mapProfilei != mapProfiling.end(); mapProfilei ++)
                {
                    mapProfilei->second->nUsage = 0;
                }
                
                bFirst = false;
            }

            struct MktProfile* pProfile;


            string strType = objVar ["name"];

            if (mapProfiling.find(strType.c_str()) == mapProfiling.end())
            {
                pProfile = new struct MktProfile;
                pProfile->nUsage = 0;
            }
            else
            {
                pProfile = mapProfiling.find (strType)->second;
            }


            pProfile->strType = objVar ["name"];
            pProfile->nUsage += objVar.GetInteger ("usage");

            //TRACE ("Counter: [%u] [%s]\n", objVar.GetCounter(), objVar["name"]);

            strData = "";

            mapProfiling [strType] = pProfile;

            
            if (strcmp(objVar["name"], "total") == 0)
            {
                /* Sorting procedures */
                vShowProfile.clear();

                map<string, struct MktProfile*>::iterator mapProfilei;

                nTotalProfiling = 1;
                
                for (mapProfilei = mapProfiling.begin(); mapProfilei != mapProfiling.end(); mapProfilei ++)
                {
                    vShowProfile.push_back  (mapProfilei->second);
                    nTotalProfiling += mapProfilei->second->nUsage;
                }


                /* Sorting data */
                sort (vShowProfile.begin(), vShowProfile.end(), ProfileSort);


                vector<struct MktProfile*>::iterator vProfilei;

                for (vProfilei = vShowProfile.begin(); vProfilei != vShowProfile.end(); vProfilei++)
                {
                    //TRACE ("Total: [%d] Name: %-40s %u\n",nTotalProfiling,  (*vProfilei)->strType.c_str(), (*vProfilei)->nUsage);
                }
                
            }

        }
        catch (string& pEx)
        {
            YYTRACE ("Error: [%s]\n", pEx.c_str());
        }
    }


    if (result->re)
    {

    }

    if (result->done)
    {
        strData = "";
        bFirst = true;
    }

    ros_result_free(result);

}




void HealthHandler (struct ros_result *result)
{
    int nCount;
    static string strData = "";
    static Variant objVar;
    static bool bFirst = true;
    bool bOK = false;

    if (ServerAttr.bHealthSupport == true)
    {

        if (result->trap)
        {
            printf("!trap Error following: \n");
        }
        if (result->fatal)
        {
            printf("!fatal: \n");
        }
        else
        {
            bOK = true;
        }

        for (nCount = 1; nCount < result->sentence->words; ++nCount)
        {
            if (result->trap || result->fatal)
            {
                printf ("%s\n", result->sentence->word [nCount]);
            }
            else
            {
                strData = strData + ((char *) &result->sentence->word [nCount][1]) + ";";
            }
        }


        if (bOK == true)
        {
            objVar = strData;


            try
            {
                if (objVar.GetCounter() > 1)
                {

                    if (bFirst == true)
                    {
                        bFirst = false;
                    }


                    ServerAttr.nCPUVoltage = objVar.GetInteger ("voltage");
                    ServerAttr.nAmbienteTemp = objVar.GetInteger ("temperature");
                    ServerAttr.nCPUTemp = objVar.GetInteger ("cpu-temperature");

                    ServerAttr.bHealthSupport = true;
                }
                else //Ending
                {
                    //TRACE ("End procedures");
                }

            }
            catch (string& pEx)
            {
                ServerAttr.bHealthSupport = false;
                return;
            }
        }


        if (result->re)
        {
            
        }
        
        if (result->done)
        {
            strData = "";
            bFirst = true;
        }
    }

    ros_result_free(result);
}




void DefaultHandler (struct ros_result *result)
{
    int i;
    static string strData = "";
    static Variant objVar;

    if (result->trap)
    {
        printf("!trap Error following: \n");
    }
    if (result->fatal)
    {
        printf("!fatal: \n");
    }

    for (i =1; i < result->sentence->words; ++i)
    {
        //printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
    }

    objVar = strData;

    if (result->re)
    {
        //none to do
        //strData.clear();
        TRACE ("RE - OBJ: [%u] - Data: [%s]\n\n", objVar.GetCounter(),  strData.c_str() );

        strData.clear();
    }
    else if (result->done)
    {
        //TRACE ("DATA: [%s]\n", strData.c_str());

        TRACE ("DONE\n");
        strData.clear ();
    }
    else
    {
        TRACE ("OBJVAR: [%u]\n\n", objVar.GetCounter());
    }

    ros_result_free(result);

}



void ResourceHandler (struct ros_result *result)
{
    int i;
    static string strData = "";
    static Variant objVar;

    if (result->trap)
    {
        printf("!trap Error following: \n");
    }
    if (result->fatal)
    {
        printf("!fatal: \n");
    }

    for (i =1; i < result->sentence->words; ++i)
    {
        //printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
    }

    if (result->re)
    {
        //none to do
        //strData.clear();
    }

    if (result->done)
    {
        //TRACE ("DATA: [%s]\n", strData.c_str());
        
        objVar = strData;
        try
        {
            ServerAttr.nRouterCPULoad = objVar.GetInteger ("cpu-load");
            //TRACE ("CPU: [%s]\n", objVar ["cpu-load"]);

            ServerAttr.strUpTime = objVar ["uptime"];
            ServerAttr.strRouterVersion = objVar ["version"];
            ServerAttr.nFreeMemory = objVar.GetInteger  ("free-memory");
            ServerAttr.nTotalMemory = objVar.GetInteger ("total-memory");
            ServerAttr.strCPU = objVar ["cpu"];
            ServerAttr.nCPUCounting = objVar.GetInteger ("cpu-count");
            ServerAttr.nCPUFrequence = objVar.GetInteger("cpu-frequency");
            ServerAttr.strArchitecture = objVar ["architecture-name"];
            ServerAttr.strBoardName = objVar ["board-name"];
            ServerAttr.strPlatform  = objVar ["platform"];

            ServerAttr.nFreeHDDSpace = objVar.GetInteger  ("free-hdd-space");
            ServerAttr.nTotalHDDSpace = objVar.GetInteger ("total-hdd-space");

        }
        catch (const string& pEx)
        {
            YYTRACE ("Error, recovering cpu-load. Error: [%s]\n", pEx.c_str ());
        }
        
        strData.clear ();
    }
    
    ros_result_free(result);
}





void Render ()
{
    uint32_t nCount;

    static Terminal::TGraph objCPUGraph, objMemGraph;

    Term.ResetAttr();

    //Term.Cls ();

    Term.GetTermSize (&nColumns, &nLines);


    Term.Color (0, 4, 7); Term.ColorBright();
    
    Term.Locate (3, nColumns - 30);
    printf ("%-30s", "CPU Load (Porcentage)");
    
    Term.ResetAttr();
    Term.Color (0, 0, 7);
    Term.Box (4, nColumns-30, 10, nColumns, NULL);

    objCPUGraph = (float) ServerAttr.nRouterCPULoad;

    objCPUGraph.PlotGraphics (11, nColumns - 30, 30, 7, 100);
    
    if (ServerAttr.nRouterCPULoad > 70)
    {
        Term.Color (5, 1, 7);
    }
    else if (ServerAttr.nRouterCPULoad > 50)
    {
        Term.Color (0, 3, 7); Term.ColorBright();
    }
    else
    {
        Term.Color (0, 4, 7); Term.ColorBright();
    }
    
    Term.PrintBigNum (5, nColumns-25, (float) ServerAttr.nRouterCPULoad, true);

    Term.Color ( 0, 0, 7);

    Term.Box (19, nColumns - 30, 36, nColumns, NULL);

    Term.Locate(20, nColumns - 28); printf ("CPU    : [%-.16s]", ServerAttr.strCPU.c_str());
    Term.Locate(21, nColumns - 28); printf ("Core   : [%u - %uMhz]", ServerAttr.nCPUCounting, ServerAttr.nCPUFrequence);
    Term.Locate(22, nColumns - 28); printf ("Archit.: [%-.16s]", ServerAttr.strArchitecture.c_str());
    Term.Locate(23, nColumns - 28); printf ("Router : [%-.16s]", ServerAttr.strBoardName.c_str());
    Term.Locate(24, nColumns - 28); printf ("Version: [%-.16s]", ServerAttr.strRouterVersion.c_str());

    Term.Locate(26, nColumns - 28); printf ("Memory : [%.1f M]", (float) ServerAttr.nTotalMemory / 1048576);
    Term.Locate(27, nColumns - 28); printf ("Free   : [%.1f M]", (float) ServerAttr.nFreeMemory / 1048576);


    Term.Locate (35, nColumns - 28);
    if (ServerAttr.bHealthSupport == true)
        printf ("V: %uV Amb: %uC CPU: %uC", ServerAttr.nCPUVoltage, ServerAttr.nAmbienteTemp, ServerAttr.nCPUTemp);
    else
        printf ("  Health not supported.");

    objMemGraph = (float) (ServerAttr.nTotalMemory - ServerAttr.nFreeMemory) ;
    objMemGraph.PlotGraphics (28, nColumns-28, 26, 6, (float) ServerAttr.nTotalMemory);


    Term.Color (1, 4 , 4);

    Term.Box (37, nColumns - 30,(int) vShowProfile.size() + 37 + 1, nColumns, "Processing usage");

    vector<struct MktProfile*>::iterator vProfilei;


    {
        nCount = 0;
        uint32_t nPorcentage;

        Term.Locate ((int)vShowProfile.size() + 37 + 2, nColumns-30); printf ("Cycle:%-24u", nTotalProfiling);

        if (nTotalProfiling > 0) for (vProfilei = vShowProfile.begin(); vProfilei != vShowProfile.end(); vProfilei++)
        {
            Term.Locate (38 + nCount++, nColumns - 28);

            nPorcentage =  ((*vProfilei)->nUsage * 100) / nTotalProfiling;

            if (nPorcentage > 70)
            {
                Term.Color (5, 1, 4);
            }
            else if (nPorcentage > 50)
            {
                Term.Color (1, 3, 4);
            }
            else
            {
                Term.Color (0, 7, 4);
            }

            printf ("%-20s %u%%\n", (*vProfilei)->strType.c_str(), nPorcentage);

        }

        Term.ResetAttr();
    }


    Term.Locate (1, 1);
    Term.BigChar();
    Term.Color (0, 3, 4);

    printf ("%*s\rMikrotik Monitorig", (uint)(nColumns / 2), " ");
    Term.ResetAttr();
    Term.Locate (2, 1);
    printf ("Roteador: [%s] Interface: [%s] Thresholds TX: [%u] RX: [%u] WhoisCache: [%u]", ServerAttr.pszRouterAddress, ServerAttr.pszInterface, ServerAttr.nTXLimit, ServerAttr.nRXLimit, whois::GetCacheSize ());
    
    ShowUsageBoxes (pHostList);

    map<string, struct Interfaces*>::iterator mapInterfacei;
    nCount = 0;

    if (mapInterfaces.size() > 0)
    {
        Term.Color (0, 0, 7);
        Term.Locate ((int) (nCount++ + nLines - mapInterfaces.size() - 1), 1); printf ("%*s\n", (nColumns - 32) * -1, "ACT| Interface Name       | Type     | TX           | RX           | TX Errors |RX Errors |TX Drops  | RX Drops");


        fflush (stdout);
        printf ("\n");
        Term.ColorUnderScore();

        for (mapInterfacei = mapInterfaces.begin(); mapInterfacei != mapInterfaces.end(); mapInterfacei++)
        {
            if (mapInterfacei->second->strDisable [0] == 't')
            {
                Term.Color (0, 4, 3);
            }
            else if ((nCount % 2) == 0)
            {
                Term.Color (0, 7, 4);
            }
            else
            {
                Term.Color (0, 7, 0);
            }


            Term.Locate ((int)(nCount++ + nLines - mapInterfaces.size() - 1), 1); printf ("%*s\r %c | %-20s | %-8s | %8.1f Kbps| %8.1f Kbps| %8u  | %8u | %8u | %8u", nColumns - 32, "",
                                                             mapInterfacei->second->strDisable [0] == 'f' ? 'R' : 'X',
                                                             mapInterfacei->second->strName.c_str(),
                                                             mapInterfacei->second->strType.c_str(),
                                                             (float) mapInterfacei->second->nTX_bits_seconds / 1024,
                                                             (float) mapInterfacei->second->nRX_bits_seconds / 1024,
                                                             mapInterfacei->second->nTX_error_seconds / 1024,
                                                             mapInterfacei->second->nRX_error_seconds / 1024,
                                                             mapInterfacei->second->nTX_drops_seconds / 1024,
                                                             mapInterfacei->second->nRX_drops_seconds / 1024);

        }
    }
}



void InterfacesDiscoverHandler (struct ros_result *result)
{
    uint nCount;
    static string strData = "";
    static Variant objVar;
    static bool bFirst = true;
    bool bOK = false;

    if (result->trap)
    {
        printf("!trap Error following: \n");
    }
    if (result->fatal)
    {
        printf("!fatal: \n");
    }
    else
    {
        bOK = true;
    }

    for (nCount = 1; nCount < result->sentence->words; ++nCount)
    {
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [nCount]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [nCount][1]) + ";";
        }
    }

    if (bOK == true)
    {
        objVar = strData;


        try
        {
            if (objVar.GetCounter() > 1)
            {

                if (bFirst == true)
                {
                    bFirst = false;
                }

                //TRACE ("STRDATA: [%s]\n\n", strData.c_str());

                struct Interfaces* pstInterface;

                if (mapInterfaces.find (objVar ["name"]) == mapInterfaces.end ())
                {
                    pstInterface = new struct Interfaces;

                    pstInterface->nTX_bits_seconds = 0;
                    pstInterface->nRX_bits_seconds = 0;

                    pstInterface->nTX_error_seconds = 0;
                    pstInterface->nRX_error_seconds = 0;

                    pstInterface->nTX_drops_seconds = 0;
                    pstInterface->nRX_drops_seconds = 0;

                    pstInterface->strName = objVar ["name"];
                }
                else
                {
                    pstInterface = mapInterfaces.find (objVar ["name"])->second;
                }

                pstInterface->strType = objVar ["type"];
                pstInterface->strRunning = objVar ["running"];
                pstInterface->strDisable = objVar ["disabled"];

                //TRACE ("Processing: [%s]\n", pstInterface->strName.c_str());

                mapInterfaces [pstInterface->strName] = pstInterface;
            }
            else //Ending
            {

            }

            strData = "";

        }
        catch (string& pEx)
        {
            YYTRACE ("Error: [%s]\n", pEx.c_str());

            strData = "";
        }
    }


    if (result->re)
    {
        
    }
    
    if (result->done)
    {
        strData = "";
        bFirst = true;
    }

    ros_result_free(result);
}



void NullHandler (struct ros_result *result)
{
    return;
}



void InterfaceDataHandler (struct ros_result *result)
{
    uint nCount;
    static string strData = "";
    static Variant objVar;
    static bool bFirst = true;
    bool bOK = false;

    if (result->trap)
    {
        //printf("!trap Error following: \n");
    }
    if (result->fatal)
    {
        printf("!fatal: \n");
    }
    else
    {
        bOK = true;
    }

    for (nCount = 1; nCount < result->sentence->words; ++nCount)
    {
        if (result->trap || result->fatal)
        {
            //printf ("%s\n", result->sentence->word [nCount]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [nCount][1]) + ";";
        }
    }

    if (bOK == true)
    {
        objVar = strData;


        try
        {
            if (objVar.GetCounter() > 1)
            {

                if (bFirst == true)
                {

                    bFirst = false;
                }

                struct Interfaces* pstInterface;

                if (mapInterfaces.find (objVar ["name"]) == mapInterfaces.end ())
                {
                    //Discarting till it existis on the map object
                    strData = "";
                    return;
                }
                else
                {
                    pstInterface = mapInterfaces.find (objVar ["name"])->second;
                }

                pstInterface->nTX_bits_seconds = objVar.GetInteger ("tx-bits-per-second");
                pstInterface->nTX_drops_seconds = objVar.GetInteger ("tx-drops-per-second");
                pstInterface->nTX_error_seconds = objVar.GetInteger ("tx-errors-per-second");

                pstInterface->nRX_bits_seconds = objVar.GetInteger ("rx-bits-per-second");
                pstInterface->nRX_drops_seconds = objVar.GetInteger ("rx-drops-per-second");
                pstInterface->nRX_error_seconds = objVar.GetInteger ("rx-errors-per-second");

                //TRACE ("STRDATA: [%s]\n", strData.c_str());
            }
            else //Ending
            {

            }

            strData = "";
        }
        catch (string& pEx)
        {
            YYTRACE ("Error: [%s]\n", pEx.c_str());
        }
    }


    if (result->re)
    {
        
    }
    
    if (result->done)
    {
        strData = "";
        bFirst = true;
    }

    ros_result_free(result);
}




void IPMonitoringHandler (struct ros_result *result)
{
    int i;
    static string strData = "";
    static Variant objVar;
    static uint32_t nTotal = 0;

    if (result->trap)
    {
        printf("!trap Error following: \n");
        bIPMonitoringConnected = false;
        strData.clear();
    }
    if (result->fatal)
    {
        printf("!fatal: \n");
    }

    for (i =1; i < result->sentence->words; ++i)
    {
        //printf(">%s\n", result->sentence->word[i]);
        if (result->trap || result->fatal)
        {
            printf ("%s\n", result->sentence->word [i]);
        }
        else
        {
            strData = strData + ((char *) &result->sentence->word [i][1]) + ";";
        }
    }

    objVar = strData;

    if (result->re)
    {
        //none to do
        //strData.clear();
        //TRACE ("RE - OBJ: [%u] - Data: [%s]\n\n", objVar.GetCounter(),  strData.c_str() );

        try
        {
            if (objVar.IsAvailable ("src-address") == true)
            {
                struct IPMonitoring stMonitor;
                struct IPMonitoring* pMonitor;

                stMonitor.szSrcAddress = objVar ["src-address"];

                if (mapMonitoring.find (stMonitor.szSrcAddress.c_str()) == mapMonitoring.end())
                {
                    stMonitor.nRX = 0;
                    stMonitor.nRXPacket = 0;

                    stMonitor.nTX = 0;
                    stMonitor.nTXPacket = 0;

                    mapMonitoring [stMonitor.szSrcAddress.c_str()] = stMonitor;
                }

                pMonitor =  &(mapMonitoring.find (stMonitor.szSrcAddress.c_str())->second);

                struct IPConnectionMonitor stIPConn;

                stIPConn.szDstAddress = objVar ["dst-address"];

                stIPConn.nTX = objVar.GetInteger ("tx");
                pMonitor->nTX = pMonitor->nTX + stIPConn.nTX;

                stIPConn.nTXPacket = objVar.GetInteger ("tx-packets");
                pMonitor->nTXPacket += stIPConn.nTXPacket;



                stIPConn.nRX = objVar.GetInteger ("rx");
                pMonitor->nRX = pMonitor->nRX + stIPConn.nRX;

                stIPConn.nRXPacket = objVar.GetInteger ("rx-packets");
                pMonitor->nRXPacket += stIPConn.nRXPacket;

                nTotal++;

                pMonitor->vecConnections.push_back (stIPConn);

                //printf  ("ADD data: [%s]\n", strData.c_str());
                //printf  ("  -> TX: [%u] kbps RX: [%u] kbps\n\n", stIPConn.nTX, stIPConn.nRX );
            }
            else if (objVar.IsAvailable ("tx") == true)
            {
                /* First lets show for developing procedures */

                struct IPMonitoring* pIPMonitor;
                //struct IPConnectionMonitor* pIPConn;

                struct IPUsage* pIPUsage = NULL;


                {
                    struct IPMonitoring stMonitor;
                    struct IPMonitoring* pMonitor;

                    stMonitor.szSrcAddress = "TOTAL";

                    if (mapMonitoring.find (stMonitor.szSrcAddress.c_str()) == mapMonitoring.end())
                    {
                        stMonitor.nRX = 0;
                        stMonitor.nRXPacket = 0;

                        stMonitor.nTX = 0;
                        stMonitor.nTXPacket = 0;

                        mapMonitoring [stMonitor.szSrcAddress.c_str()] = stMonitor;
                    }

                    pMonitor =  &(mapMonitoring.find (stMonitor.szSrcAddress.c_str())->second);

                    struct IPConnectionMonitor stIPConn;

                    stIPConn.nTX = objVar.GetInteger ("tx");
                    pMonitor->nTX = pMonitor->nTX + stIPConn.nTX;

                    stIPConn.nTXPacket = objVar.GetInteger ("tx-packets");
                    pMonitor->nTXPacket += stIPConn.nTXPacket;


                    stIPConn.nRX = objVar.GetInteger ("rx");
                    pMonitor->nRX = pMonitor->nRX + stIPConn.nRX;

                    stIPConn.nRXPacket = objVar.GetInteger ("rx-packets");
                    pMonitor->nRXPacket += stIPConn.nRXPacket;
                    
                    pMonitor->vecConnections.push_back (stIPConn);

                }

                nTotal = 0;

                /*
                for (map<string, struct IPUsage*>::iterator iteItem = pHostList.begin(); iteItem != pHostList.end(); iteItem++)
                {
                    iteItem->second->nCountConnections = 0;
                    //iteItem->second->nTXbps = 0;
                    //iteItem->second->nRXbps = 0;
                    //iteItem->second->nTXPackets = 0;
                    //iteItem->second->nRXPackets = 0;
                }
                 */

                for (map<string, struct IPMonitoring>::iterator iteIP = mapMonitoring.begin(); iteIP != mapMonitoring.end(); iteIP++)
                {
                    nTotal = nTotal + (uint32_t) iteIP->second.vecConnections.size ();
                }


                for (map<string, struct IPMonitoring>::iterator iteIP = mapMonitoring.begin(); iteIP != mapMonitoring.end(); iteIP++)
                {
                    pIPMonitor = &(*iteIP).second;

                    if (pIPMonitor->vecConnections.size() > 0)
                    {

                        /*
                        printf  ("IP [%s] TX: [%u - %u Kbps] RX: [%u - %u Kbps] Connections: TotalL [%u] \n", pIPMonitor->szSrcAddress.c_str(), (uint32_t)pIPMonitor->nTX , (uint32_t) ((float) pIPMonitor->nTX /1024) , (uint32_t) pIPMonitor->nRX , (uint32_t) ((float) pIPMonitor->nRX / 1024) , pIPMonitor->vecConnections.size());

                        for (vector <struct IPConnectionMonitor>::iterator iteItem = pIPMonitor->vecConnections.begin(); iteItem != pIPMonitor->vecConnections.end(); iteItem++)
                        {
                            pIPConn = & (*iteItem);

                            printf ("\t IP:[%-15s] TX %10u bps RX %10u bps Pkts: TX %10u RX %10u \n", pIPConn->szDstAddress.c_str(), pIPConn->nTX, pIPConn->nRX, pIPConn->nTXPacket, pIPConn->nRXPacket);
                        }
                        */

                        // =======================================================
                        // Processing current data to populate HostList
                        // adding or updating the total traffic data by IP
                        // =======================================================
                        if (pHostList.find (pIPMonitor->szSrcAddress.c_str()) == pHostList.end())
                        {
                            struct IPUsage pIPUsage;

                            // Make sure everything will be initilizaed as 0 or null
                            memset ((void*) &pIPUsage, 0, sizeof (pIPUsage));

                            //Naming the source of the request
                            snprintf (pIPUsage.szSrcAddress, sizeof (pIPUsage.szSrcAddress), "%s", pIPMonitor->szSrcAddress.c_str());

                            snprintf (pIPUsage.szHostName, sizeof (pIPUsage.szHostName), "Unkown");

                            snprintf (pIPUsage.szMacAddress, sizeof (pIPUsage.szMacAddress), "-- NOT MANAGED --");

                            //Adding to the back of the vector array object
                            pHostList [pIPMonitor->szSrcAddress.c_str()] = pIPUsage;
                        }


                        //Independent if added will reclain the pointer again.
                        pIPUsage = &(pHostList.find (pIPMonitor->szSrcAddress.c_str())->second);

                        //Starting populating data to the ongoing data.

                        if (pIPUsage->szSrcAddress [0] == 'T')
                        {
                            pIPUsage->nCountConnections = nTotal;
                            //pIPUsage->pvecConnections;
                            nTotal = 0;
                        }
                        else
                        {
                            pIPUsage->nCountConnections = (uint32_t) pIPMonitor->vecConnections.size();
                            pIPUsage->pvecConnections = pIPMonitor->vecConnections;
                        }



                        /*
                        //Addind data by nativily converting to kbps instead bps collected from the stream.
                        //This approuch will make a more accurate data

                        pIPUsage->nRXbps = (uint32_t) ((float) pIPMonitor->nTX /1024);
                        pIPUsage->nRXPackets = pIPMonitor->nTXPacket;

                        pIPUsage->nTXbps = (uint32_t) ((float) pIPMonitor->nRX / 1024);
                        pIPUsage->nTXPackets = pIPMonitor->nRXPacket;
                        */
                    }
                }


                mapMonitoring.clear();

            }


        }
        catch (string& pEx)
        {
            YYTRACE ("Error processing data: [%s] - DATA: [%s]\n", pEx.c_str(), strData.c_str());
        }



        strData.clear();
    }
    else if (result->done)
    {
        //TRACE ("DATA: [%s]\n", strData.c_str());

        TRACE ("DONE\n");
        strData.clear ();
    }
    else
    {
        TRACE ("OBJVAR: [%u]\n\n", objVar.GetCounter());

        //sleep (5);

        strData.clear();
    }
    
    ros_result_free(result);
}


void PrintWelcomeMessage ()
{
    Term.ResetAttr();
    Term.BigChar();
    Term.ColorBright();
    printf ("Mikrotik Monitoring and Management.\n");
    Term.ColorNormal();
    printf ("by Gustavo Campos, 2014.\n\n");
}



void LoadingHostTranslation ()
{
    FILE* pFile = NULL;

    if ((pFile = fopen ("/etc/MktHostTranslation.list", "r")) == NULL)
    {
        YYTRACE ("No /etc/MktHostTranslation.list found.")
        return;
    }

    char szData [1024];
    char szTemp [1024];
    string strHost, strValue;

    while (feof (pFile) == false)
    {
        fgets (szData, sizeof (szData) - 1, pFile);
        TUtil_StripEOL (szData, (int) strlen (szData));

        //TRACE ("Read: [%s]\n", szData);

        TUtil_GetToken (';', (const char*) szData, szTemp, sizeof (szTemp) - 1, 0);
        strHost = szTemp;

        TUtil_GetToken (';', (const char*) szData, szTemp, sizeof (szTemp) - 1, 1);
        strValue = szTemp;

        TRACE ("HOST: [%s] = [%s]\n", strHost.c_str(), strValue.c_str());

        mapHostDictionary [strHost] = strValue;
    }

    fclose (pFile);
}







int main(int nArgs, char *pszArgs [])
{

    whois objWhois;

    objWhois.SetCacheTimeout (10);


    string strData = "201.17.30.152";

    /*
    try
    {
        TRACE ("Answer: [%s]\n\n", objWhois.Lookup (strData.c_str(), strData.length()) == true ? "TRUE":"FALSE");

        TRACE ("Owner:   [%s]\n", objWhois ["owner"]);
        TRACE ("Contact: [%s]\n", objWhois ["person"]);
        TRACE ("Country: [%s]\n", objWhois ["country"]);
        
    } catch (Exception* pEx)
    {
        YYTRACE ("Error: [%s]\n", pEx->GetExceptionMessage());
    }
*/

    //exit (0);

    PrintWelcomeMessage ();
    
    if (nArgs != 8)
    {
        Term.ColorBright();
        printf ("(%u)Use: <Router IP> <Router port - nothig is default> <Router user> <Router user password> <Transnitting Kbps Threshold> <Receiving Kbps Threshold> <Router Interface>\n\n", nArgs);
        Term.ResetAttr();
        
        exit (1);
    }

    LoadingHostTranslation ();

    Term.GetTermSize (&nColumns, &nLines);

    ServerAttr.nTXLimit = strtod (pszArgs [5], NULL);
    ServerAttr.nRXLimit = strtod (pszArgs [6], NULL);
    ServerAttr.pszInterface = pszArgs [7];
    ServerAttr.pszRouterAddress = pszArgs [1];
    
    class MikrotikLib pRouter (pszArgs [1], pszArgs [2][0] == '\0' ? 8728 : atoi (pszArgs [2]), pszArgs [3], pszArgs [4]);

    /*
    pRouter.SendCommand ("/interface/print  ", handledata, 1);

    pRouter.SendCommand ("/interface/monitor-traffic =interface=bridge-local", handledata, 100);
    */
    
    //pRouter.SendCommand ("/ip/dhcp-server/lease/print ", IPNameStructure, 101);
   


    string strInterfaceMonitorCmd = "";

    ServerAttr.bHealthSupport = true;


    strIPInterfaceMonitoring = "";
    strIPInterfaceMonitoring = strIPInterfaceMonitoring + "/tool/torch =dst-address=0.0.0.0/0 =freeze-frame-interval=4 =interface=" + pszArgs [7] + " =src-address=0.0.0.0/0 =ip-protocol=tcp ";

    string strTouchString;

    strTouchString = strTouchString + "/tool/torch =src-address=0.0.0.0/0 =interface=" + pszArgs [7] + "  =freeze-frame-interval=5 ";


    map<string, struct IPUsage*>::iterator it;

    pHostList.clear();

    Term.Color (0, 7, 0);
    Term.Cls ();

    Term.GetTermSize (&nColumns, &nLines);

    //pRouter.SetDebug (true);


    map<string, struct Interfaces*>::iterator mapInterfacei;


    TRACE ("STARTING....\n\n");

    while (true)
    {
        //Term.SetScroll (nLines - 10, nLines);
        pRouter.ProcessLoopOnce();
        //Term.EndScroll ();

        
        if (bIPMonitoringIP == false)
        {
            pRouter.SendCommand ((const char*) strTouchString.c_str(), IPUsageHandle , 200);
            bIPMonitoringIP = true;
        }


        if (bIPMonitoringConnected == false)
        {
            pRouter.SendCommand (strIPInterfaceMonitoring.c_str(), IPMonitoringHandler, 150);
            bIPMonitoringConnected = true;
        }

        
        if(bProfileMonitor == false)
        {
             pRouter.SendCommand ("/tool/profile =freeze-frame-interval=5", ProfileHandler, 106);
            bProfileMonitor = true;
        }

        pRouter.SendCommand ("/ip/dhcp-server/lease/print ", IPNameStructure, 101);

        pRouter.SendCommand ("/system/resource/print ", ResourceHandler, 105);

        pRouter.SendCommand ("/system/health/print ", HealthHandler, 110);

        pRouter.SendCommand ("/interface/print  ", InterfacesDiscoverHandler, 210);

        strInterfaceMonitorCmd = "/interface/monitor-traffic =interface=";

        for (mapInterfacei = mapInterfaces.begin(); mapInterfacei != mapInterfaces.end(); mapInterfacei++)
        {
            strInterfaceMonitorCmd = strInterfaceMonitorCmd + (*mapInterfacei).second->strName + ",";
        }

        pRouter.SendCommand (strInterfaceMonitorCmd.c_str(), InterfaceDataHandler, 220);

        //TRACE ("Processando: [%s]\n", strInterfaceMonitorCmd.c_str());


        Render ();
        fflush (stdout);


        sleep (5);

        Term.ResetAttr();
        Term.Cls ();

        pRouter.SendCommand ("/cancel =tag=220 ", NullHandler, 22);
        Term.ResetAttr();

    }
    
	return 0;
}



File: /MikrotikManager\main.h
//
//  main.h
//  MikrotikManager
//
//  Created by Gustavo Campos on 09/06/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
//
/*
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
*/

#ifndef MikrotikManager_main_h
#define MikrotikManager_main_h

#include <Util.h>
#include <map>
#include <vector>

struct
{
    uint nTXLimit;
    uint nRXLimit;

    const char* pszInterface;
    const char* pszRouterAddress;

    uint  nRouterCPULoad;
    uint  nCPUCounting;
    uint  nCPUFrequence;

    string strCPU;
    string strUpTime;
    string strRouterVersion;
    uint32_t  nTotalMemory;
    uint32_t  nFreeMemory;
    string strArchitecture;
    string strBoardName;
    string strPlatform;

    uint32_t   nFreeHDDSpace;
    uint32_t   nTotalHDDSpace;

    uint32_t nCPUVoltage;
    uint32_t nAmbienteTemp;
    uint32_t nCPUTemp;
    bool     bHealthSupport;

} ServerAttr;

struct MktProfile
{
    string strType;
    uint32_t  nUsage;
};


struct Interfaces
{
    string strName;
    string strType;
    string strRunning;
    string strDisable;

    uint32_t nTX_bits_seconds;
    uint32_t nTX_drops_seconds;
    uint32_t nTX_error_seconds;

    uint32_t nRX_bits_seconds;
    uint32_t nRX_drops_seconds;
    uint32_t nRX_error_seconds;
};


/* Dual layer Monitoring Structure */
struct IPConnectionMonitor
{
    string szDstAddress;
    uint32_t nTX;
    uint32_t nTXPacket;
    uint32_t nRX;
    uint32_t nRXPacket;
};

struct IPMonitoring
{
    string szSrcAddress;

    uint32_t nTX;
    uint32_t nTXPacket;

    uint32_t nRX;
    uint32_t nRXPacket;

    vector <struct IPConnectionMonitor> vecConnections;
};



struct IPUsage
{
    char        szSrcAddress [20];
    char        szDstAddress [20];
    uint32_t    nRXbps;
    uint32_t    nTXbps;
    uint32_t    nTXPackets;
    uint32_t    nRXPackets;
    char        szMacAddress [20];
    char        szHostName [50];

    uint32_t    nCountConnections;

    vector <struct IPConnectionMonitor> pvecConnections;
};



#endif


File: /MikrotikManager\MikrotikManager.1
.\"Modified from man(1) of FreeBSD, the NetBSD mdoc.template, and mdoc.samples.
.\"See Also:
.\"man mdoc.samples for a complete listing of options
.\"man mdoc for the short list of editing options
.\"/usr/share/misc/mdoc.template
.Dd 6/6/14               \" DATE 
.Dt MikrotikManager 1      \" Program name and manual section number 
.Os Darwin
.Sh NAME                 \" Section Header - required - don't modify 
.Nm MikrotikManager,
.\" The following lines are read in generating the apropos(man -k) database. Use only key
.\" words here as the database is built based on the words here and in the .ND line. 
.Nm Other_name_for_same_program(),
.Nm Yet another name for the same program.
.\" Use .Nm macro to designate other names for the documented program.
.Nd This line parsed for whatis database.
.Sh SYNOPSIS             \" Section Header - required - don't modify
.Nm
.Op Fl abcd              \" [-abcd]
.Op Fl a Ar path         \" [-a path] 
.Op Ar file              \" [file]
.Op Ar                   \" [file ...]
.Ar arg0                 \" Underlined argument - use .Ar anywhere to underline
arg2 ...                 \" Arguments
.Sh DESCRIPTION          \" Section Header - required - don't modify
Use the .Nm macro to refer to your program throughout the man page like such:
.Nm
Underlining is accomplished with the .Ar macro like this:
.Ar underlined text .
.Pp                      \" Inserts a space
A list of items with descriptions:
.Bl -tag -width -indent  \" Begins a tagged list 
.It item a               \" Each item preceded by .It macro
Description of item a
.It item b
Description of item b
.El                      \" Ends the list
.Pp
A list of flags and their descriptions:
.Bl -tag -width -indent  \" Differs from above in tag removed 
.It Fl a                 \"-a flag as a list item
Description of -a flag
.It Fl b
Description of -b flag
.El                      \" Ends the list
.Pp
.\" .Sh ENVIRONMENT      \" May not be needed
.\" .Bl -tag -width "ENV_VAR_1" -indent \" ENV_VAR_1 is width of the string ENV_VAR_1
.\" .It Ev ENV_VAR_1
.\" Description of ENV_VAR_1
.\" .It Ev ENV_VAR_2
.\" Description of ENV_VAR_2
.\" .El                      
.Sh FILES                \" File used or created by the topic of the man page
.Bl -tag -width "/Users/joeuser/Library/really_long_file_name" -compact
.It Pa /usr/share/file_name
FILE_1 description
.It Pa /Users/joeuser/Library/really_long_file_name
FILE_2 description
.El                      \" Ends the list
.\" .Sh DIAGNOSTICS       \" May not be needed
.\" .Bl -diag
.\" .It Diagnostic Tag
.\" Diagnostic informtion here.
.\" .It Diagnostic Tag
.\" Diagnostic informtion here.
.\" .El
.Sh SEE ALSO 
.\" List links in ascending order by section, alphabetically within a section.
.\" Please do not reference files that do not exist without filing a bug report
.Xr a 1 , 
.Xr b 1 ,
.Xr c 1 ,
.Xr a 2 ,
.Xr b 2 ,
.Xr a 3 ,
.Xr b 3 
.\" .Sh BUGS              \" Document known, unremedied bugs 
.\" .Sh HISTORY           \" Document history if command behaves in a unique manner

File: /MikrotikManager\Socket.cpp
/*
 *  Socket.cpp
 *  thread
 *
 *  Created by Gustavo Campos on 16/04/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
     
     MIT License
     
     Copyright (c) 2017 Luiz Gustavo de Campos
     
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
     
 */

#include "Util.h"
#include "Exception.h"
#include <iostream>
#include "Socket.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/socket.h>
#include <openssl/rand.h>

//static void sigpipe_handle(int x);

//static char* pass;


void Socket::DefaultInicialization ()
{
	nDomain = 0;
    nType =0;
    nSocket = 0;
    isListen = 0;
    isConnected = 0;
	pFile = NULL;
	
	bio_err = NULL;	
	
	bSecure = false;
		
    ctx = NULL;
    ssl = NULL;
    sbio = NULL;
	
}



Socket::~Socket ()
{
	//if (isListen == false)
    Close ();
}



Socket::Socket ()
{
	DefaultInicialization ();
	
 #ifdef WIN32
    static bool bWStart = false;
    
    if (bWStart == false)
    {
        WSADATA wsaData;
        WSAStartup(0x0101, &wsaData); /* Winsock Startup function. DEFAULT... to all source files that will use Winsock **only WIN32  */
        bWStart = true;
    }

	pFile = NULL;

    nLastReading = 0;
    nLastWritting = 0;

#endif
}




bool Socket::IsReady (int nTimeoutSeconds, int nTimeoutUSeconds)
{
    fd_set            fdSet;
    struct timeval    tmVal;
    bool              bReturn;
    unsigned int      nReturn;

	VERIFY (this != NULL, "DEEP LOGIC ERROR... COMPILING ERROR.");
	VERIFY (nSocket _ERROR, "Error, Socket not defined.");

    tmVal.tv_sec  = nTimeoutSeconds;
    tmVal.tv_usec = nTimeoutUSeconds;
    
    FD_ZERO (& fdSet);
    FD_SET  (this->nSocket, &fdSet);
        
    
#ifndef _HPUX_
    VERIFY ((nReturn = select (this->nSocket + 1, &fdSet, NULL, NULL, &tmVal)) _ERROR, "");
#else
    VERIFY ((nReturn = select (this->nSocket + 1, &fdSet, NULL, NULL, &tmVal)) _ERROR, ""); 
#endif

    VERIFY ((nReturn = FD_ISSET (this->nSocket, &fdSet)) >= 0, "");
    
	//TRACE ("%s: Result: %u  %us %us\n", __FUNCTION__, nReturn, nTimeoutSeconds, nTimeoutUSeconds);
	
    if (nReturn > 0)
    {
        bReturn = true;
    }
    else
    {
        bReturn = false;
    }

    return bReturn;
}




bool Socket::IsWriteReady (int nTimeoutSeconds, int nTimeoutUSeconds)
{
    fd_set            fdSet;
    struct timeval    tmVal;
    bool              bReturn;
    int               nReturn;
     
    tmVal.tv_sec  = nTimeoutSeconds;
    tmVal.tv_usec = nTimeoutUSeconds;
    
	Assert  (this != NULL, "DEEP LOGIC ERROR... COMPILING OR LOGIC ERROR.", 100);
	VERIFY (nSocket _ERROR, "Error, Socket not defined.");
	
    FD_ZERO (& fdSet);

    FD_SET  (nSocket, &fdSet);
        


#ifndef _HPUX_
    VERIFY (select (this->nSocket + 1, NULL, &fdSet, NULL, &tmVal) > 0, "");
#else
    VERIFY (select (this->nSocket + 1, NULL, (int*) &fdSet, NULL, &tmVal) > 0, "");
#endif

    VERIFY ((nReturn = FD_ISSET (this->nSocket, &fdSet)) _ERROR, "");


    if (nReturn)
    {
        bReturn = true;
    }
    else
    {
        bReturn = false;
    }

    return bReturn;
}





bool Socket::Close ()
{
    /* 
       For better performance and compatibilitie this
       proceadure is totally safety, throwing no warnnings
    */
    
    //VERIFY (this->isListen != true, "Socket was defined as LISTEN and could not be closed.");
    
		/* Disabilita send and receive */
		shutdown  (this->nSocket, SHUT_RDWR); 
		
		/* Close connection with the remote peer*/
		close (this->nSocket);

    isListen = false;
    isConnected = false;

    return true;
}




bool Socket::Printf (long int nStrLen, const char* pszFormat, ...)
{
        va_list   vaArgs;
        char      pszTemp [nStrLen + 1];
        long int nLen;
        
        //signal (SIGPIPE, Socket::PipeReceive);
        
        if (nStrLen > SOCKET_MAX_PRINTF_LINE) nStrLen = SOCKET_MAX_PRINTF_LINE;
                
        va_start (vaArgs, pszFormat);
        
        VERIFY ((nLen = vsnprintf ((char*) pszTemp, nStrLen-1, pszFormat, vaArgs)) _ERROR, "Erro ao processar a string a ser enviada.");
        
        pszTemp [nLen] ='\0';
        
        va_end (vaArgs);
        
		TRACE ("PRINTF: (%lu) %s\n", nLen, pszTemp);
		
		Send (nLen, pszTemp);

        nLastWritting = time (NULL);

        return true;
}




bool Socket::Send (long int nStrLen, const char* pszData)
{        
        //signal (SIGPIPE, Socket::PipeReceive);


        //TRACE ("Sending: %s\n", pszData);
        
		VERIFY (IsWriteReady (15, 100), "Timeout de envio.");
		
        VERIFY (send (this->nSocket, (char*) pszData, nStrLen, 0) _ERROR, "Erro ao Enviar os dados ao Socket destino");

        nLastWritting = time (NULL);
    
        return true;
}




long int Socket::Read (int nStrLen, char* pszReceive)
{
    return Read (nStrLen, pszReceive, 10);
}




long int Socket::Read (int nStrLen, char* pszReceive, uint nTimeout)
{
    long int nLen;
    
    if (IsReady (nTimeout, 0) == true)
    {
        try
        {
            VERIFY ((nLen = recv (this->nSocket, pszReceive, nStrLen, MSG_WAITALL)) > 0, strerror (errno));
        }
        catch (Socket* pSocket)
        {
            pSocket->Close ();
            throw;
        }
    }
    else
    {
        return 0;
    }
    
    //TRACE ("Socket::SafeRead: Readed %ld \n", nLen);

    nLastReading = time (NULL);

    return nLen;
}




long int Socket::Gets (char* pszReturn, long int nLen, long int nTimeout)
{
    long int nCount     = 0;
            
    pszReturn [0] = '\0';
    
    if (IsReady ((int) nTimeout, 0))
    {
        char     chChar [2] = " ";
        long     nReceive;

        while (chChar [0] != '\n')
        {
            if (IsReady  ((int) nTimeout, 0))
            {
				if ((nReceive = Read (1, &chChar[0])) != 1)
                {
                    //TRACE ("ERRNO: [%lu]\n", nReceive);
                    pszReturn [nCount] = _EOS;                    
                }
            }
            else
            {
                break;
            }
            
            
            /* 
            A cada 10 ciclo de processamento e direcionado uma 
             pausa de 10 mile segundos 
             */
                        
            if (chChar [0] >= ' ')
            {
                if (nCount < nLen - 1)
                {
                    pszReturn [nCount] = chChar [0];
                    nCount++;
                    pszReturn [nCount] = _EOS;
                }
                else
                {
                    pszReturn [nCount] = _EOS;
					//TRACE ("GETS:  %s\n", pszReturn);
                    return nCount;
                }
            }
        }        
    }
    else
    {
        return 0;
    }
    
    /* Retorna o dado encontrado */ 
    pszReturn [nCount] = _EOS;
	//TRACE ("GETS:  %s\n", pszReturn);

    return nCount;
}




bool Socket::Listen (int nPorta, int nBacklog)
{
    int nTrue = 1;
    struct addrinfo hints, *res;
	int nRet;
	struct timeval tmVal; 
	char   szPorta [16];
		    
	tmVal.tv_sec = 10;
	tmVal.tv_usec = 900000;
	
	snprintf (szPorta, 15, "%u", nPorta);
	
	memset (&hints, 0, sizeof (struct addrinfo));
	hints.ai_flags    = AI_PASSIVE;
	hints.ai_family   = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	 
	if ((nRet = getaddrinfo ("0.0.0.0", szPorta, &hints, &res)) != 0)
	{
		//TRACE ("TCP Listen Error: %s\n", gai_strerror (nRet));
		return false;
	}
		
	VERIFY ((this->nSocket = socket (res->ai_family, res->ai_socktype, 0)) _ERROR, "");
    
    VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_REUSEADDR, (int*) &nTrue, sizeof (int)) _ERROR, "");

    VERIFY (setsockopt (this->nSocket, IPPROTO_TCP, TCP_NODELAY, &nTrue, sizeof (int)) _ERROR, "");

    //VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_ERROR, &nTrue, sizeof (int)) _ERROR, "");

    VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_SNDTIMEO, &tmVal, sizeof (struct timeval)) _ERROR, "");
    //VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_SNDBUF, &nTrue, sizeof (int)) _ERROR, "", false);

    int set = 1;

#ifdef SO_NOSIGPIPE
    VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_NOSIGPIPE, (void *)&set, sizeof(int)) _ERROR, "");
#endif

    nTrue = 10;
    
    VERIFY ((::bind (this->nSocket, res->ai_addr, res->ai_addrlen)) >= 0, "");
    
    this->isListen = true;

    VERIFY (listen (this->nSocket, nBacklog) _ERROR, "");

    this->nType   = SOCK_STREAM; 
    this->nDomain = AF_INET;
    
    return true;
}





Socket* Socket::Accept (uint nTimeout)
{
    Socket*      pNSocket = NULL;
    int          nSocket;
    sockaddr_in  SocketAddr;
    socklen_t    sin_size = sizeof (struct sockaddr);
    
    VERIFY (this->isListen == true, "O Socket n„o est· em modo Listen");
 
    VERIFY (this->nDomain == AF_INET && this->nType == SOCK_STREAM, "Tipo de socket invalido.");
    
    if (IsReady (nTimeout, 0) == false)
    {
        return NULL;
    }
    
    try
    {		
        VERIFY ((nSocket = accept(this->nSocket, (struct sockaddr *) &SocketAddr, &sin_size)) _ERROR, "");
        
        //TRACE ("[%s] conectado FD: [%d] \n", inet_ntoa (SocketAddr.sin_addr), nSocket);
        
        VERIFY ((pNSocket = new Socket (nSocket, SocketAddr)) != NULL, "Erro na criacao do socket de conexao.");
        
    }
    catch (Socket* pSocket)
    {
        //TRACE ("%s\n", pSocket->GetExceptionMessage ());
        
        if (pNSocket != NULL)
        {
            delete pNSocket;
        }
		
		throw pSocket;
    }
    
    return pNSocket; 
}




Socket::Socket (int nSocket, sockaddr_in stSocketAddr)
{        
	
	DefaultInicialization ();
	
		{
            this->nSocket = nSocket;

            int nLen;

			//VERIFY (setsockopt (this->nSocket, IPPROTO_TCP, TCP_NODELAY, &nNDelay, sizeof (int)) _ERROR, "");
			//VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_DONTROUTE, &nNDelay, sizeof (int)) _ERROR, "", false);

            nLen = 20048;
			VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_RCVBUF, &nLen, sizeof (nLen)) _ERROR, "");

            nLen = 20048;
			VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_SNDBUF, &nLen, sizeof (nLen)) _ERROR, "");

#ifdef SO_NOSIGPIPE
            int set = 1;
            VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_NOSIGPIPE, (void *)&set, sizeof(int)) _ERROR, "");
#endif

            {
                struct timeval tv;

                tv.tv_sec = 30;  /* 30 Secs Timeout */

                setsockopt(this->nSocket, SOL_SOCKET, SO_RCVTIMEO,(struct timeval *)&tv,sizeof(struct timeval));

                setsockopt(this->nSocket, SOL_SOCKET, SO_SNDTIMEO,(struct timeval *)&tv,sizeof(struct timeval));

                int optval;
                socklen_t optlen = sizeof(optval);

                optval = 10;
                optlen = sizeof(optval);

                VERIFY (setsockopt(this->nSocket, SOL_SOCKET, SO_KEEPALIVE, &optval, optlen) >= 0, "", false);
            }

		}

        memcpy (&this->SocketAddr, &stSocketAddr, sizeof (sockaddr_in));

    isConnected = true;

    nLastReading = time (NULL);
    nLastWritting = time (NULL);

}




bool Socket::Connect (const char* pszHost, unsigned int nPort, int nTimeout)
{
	return Connect2 (pszHost, nPort, nTimeout, false);
}




bool Socket::SSLConnect (const char* pszHost, unsigned int nPort, int nTimeout)
{
	return Connect2 (pszHost, nPort, nTimeout, true);
}




bool Socket::Connect2 (const char* pszHost, unsigned int nPort, int nTimeout, bool bSSLCom)
{  
    struct hostent* pHostEnt;
	
    static int s_server_session_id_context = 0;

    s_server_session_id_context++;

    //Requisita um novo socket ao sistema operacioal
	VERIFY ((this->nSocket = socket(AF_INET, SOCK_STREAM, 0)) _ERROR, "");

	bSecure = bSSLCom;
	
    //Converte o DNS / Host entrado. (realize o DNS)
    pHostEnt = GetHostByName (pszHost);
  
    memset(&this->SocketAddr, 0, sizeof(struct sockaddr_in));
    this->SocketAddr.sin_family = AF_INET;
    this->SocketAddr.sin_addr.s_addr = ((struct in_addr*)(pHostEnt->h_addr))->s_addr;
    this->SocketAddr.sin_port = htons(nPort);                                                                   

    int nLen = 20048;
    VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_RCVBUF, &nLen, sizeof (nLen)) _ERROR, "");

    nLen = 20048;
    VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_SNDBUF, &nLen, sizeof (nLen)) _ERROR, "");


    {
        struct timeval tv;

        tv.tv_sec = nTimeout;  /* 30 Secs Timeout */

        setsockopt(this->nSocket, SOL_SOCKET, SO_RCVTIMEO,(struct timeval *)&tv,sizeof(struct timeval));

        setsockopt(this->nSocket, SOL_SOCKET, SO_SNDTIMEO,(struct timeval *)&tv,sizeof(struct timeval));

        /* Set the option active */

        int optval;
        socklen_t optlen = sizeof(optval);

        optval = 10;
        optlen = sizeof(optval);

        VERIFY (setsockopt(this->nSocket, SOL_SOCKET, SO_KEEPALIVE, &optval, optlen) >= 0, "", false);
    }



    //Connecta ao host destino
    VERIFY (connect(this->nSocket,(struct sockaddr *)  &this->SocketAddr, sizeof(struct sockaddr)) _ERROR, "Erro ao se conectar ao host destino");    
	
	{
		//int window = 1024 * 1;  // 1.0M
		//VERIFY (setsockopt (this->nSocket, SOL_SOCKET, SO_RCVBUF, &window, sizeof (window)) _ERROR, "")
	}
	


    nLastReading = time (NULL);
    nLastWritting = time (NULL);

	return true;
}




struct hostent* Socket::GetHostByName (const char* pszHost)
{
  struct hostent* pHostEnt;
  
  //TRACE ("Procurando host: %s\n", pszHost);

  VERIFY ((pHostEnt = gethostbyname (pszHost)) != NULL, "O DNS entrado nao foi encontrado.\n");

  return pHostEnt;
}




FILE* Socket::GetNewFILE (char* szFileMode)
{	
	VERIFY ((pFile = fdopen (nSocket, szFileMode)) != NULL, "");
	
	return pFile;
}




void Socket::GetLocalAddress (struct sockaddr_in* cliaddr)
{ 
        int     sockfd; 
        socklen_t len; 
        struct sockaddr_in servaddr; 
        
        sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
        bzero(&servaddr, sizeof(servaddr)); 
        
        servaddr.sin_family = AF_INET; 
        servaddr.sin_port = htons(1); 
        
        inet_pton(AF_INET, "255.255.255.255", &servaddr.sin_addr); 
        
        connect(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr)); 
        
        len = sizeof(cliaddr); 
        getsockname(sockfd, (struct sockaddr *) cliaddr, &len); 
		
        ////TRACE ("local address %s\n", inet_ntoa (cliaddr->sin_addr));
} 




void Socket::IfException ()
{
	////TRACE ("EXCEPTION RISED FROM SOCKET\n");
}






/* A simple error and exit routine*/
int err_exit(char* string)
{
    fprintf(stderr,"%s\n",string);
    exit(0);
}


/*
static void sigpipe_handle(int x)
{
}
*/


#define GetIP(x) inet_ntoa (x.sin_addr)
#define GetPort(x) ntohs (x.sin_port)

const char* Socket::GetRemoteIP ()
{
    if (isConnected == true)
    {
        return inet_ntoa (this->SocketAddr.sin_addr);
    }

    return NULL;
}




uint16_t Socket::GetRemotePort ()
{
    if (isConnected == true)
    {
        return ntohs (this->SocketAddr.sin_port);
    }

    return 0;
}




int Socket::GetSockfd()
{
    return nSocket;
}




uint Socket::GetFdSetFromArray (Socket** pSockets, uint nMaxSockets, fd_set* objFdSet, uint* nMaxFd)
{
    Verify (pSockets != NULL, "Error no data stored over pSocket pointer variable.", false);
    Verify (objFdSet != NULL, "Error no fd_set data provided, the variable is NULL.", false);

    FD_ZERO(objFdSet);

    uint nCount;
    uint nFDCount=0;

    *nMaxFd = 0;

    for (nCount=0; nCount < nMaxSockets; nCount++)
    {
        if (pSockets [nCount] != NULL)
        {
            //TRACE ("Adding [%u] FD:[%u] to the objFDSet given at [%08X]\n", nCount, pSockets [nCount]->GetSockfd(), objFdSet);
            FD_SET (pSockets [nCount]->GetSockfd(), objFdSet);
            nFDCount++;

            if (pSockets [nCount]->GetSockfd() > *nMaxFd) *nMaxFd = pSockets [nCount]->GetSockfd();
        }
        else
        {
            //YYTRACE ("FdSet: Socket Index [%u] is NULL\n", nCount);
        }
    }

    //TRACE ("\n");
    //TRACE ("\n");

    return nFDCount;
}




/*
   CheckDataForReading ()
 
    This function will return how much data ready for being read
    from the current connection, if if return zero, it may means 
    the socket has gone disconnected but yet undetected from the current
    functions.
 */

uint32_t Socket::CheckDataForReading ()
{
    int n = 0;

    ioctl(nSocket, FIONREAD, &n);
    
    return n;
}



/*
    CheckIfIsClosed ()
 
    This function will get the amount of data on the Kernel's current Socket's pipeline
    and case it is zero will return that the connection is already broken. but 
    will not take action to close it, just to inform.
 
    Even though it may look a non sence, it will give to the programmer
    the hability to proper act before closing the connection, what is highly wised
    and good-practive. 
 
    For closing use ->close () directive whereabouts it is ready in your code.
 */

bool Socket::CheckIfIsClosed ()
{
    fd_set rfd;
    FD_ZERO(&rfd);
    FD_SET(nSocket, &rfd);

    timeval tv = { 0 };




    VERIFY (select(nSocket+1, &rfd, NULL, NULL, &tv) >= 0, "", true);

    if (FD_ISSET (nSocket, &rfd))
    {
        int l_sock_optval=-1;
        int l_sock_optval_len=sizeof(l_sock_optval);

        if(getsockopt(nSocket, SOL_SOCKET, SO_ERROR, (int*)&l_sock_optval, (socklen_t*)&l_sock_optval_len) !=0)
        {
            return true;
        }
    }

    int n = 0;

    ioctl(nSocket, FIONREAD, &n);

    return n >= 0 ? false : true;
}



/*
    CheckReadingIdelTimeout (uint nSecTimeout)
 
   Will return true if the elipsed time between last reading 
   to now is greatter than nSecTimeout.
 
   This functions only say if the give timout has been reached, it
   will not take any action, this in inteded to allow programmer
   to logical enrich applications.
*/

bool Socket::CheckReadingIdelTimeout (uint nSecTimeout)
{
    time_t nCurrentTime = time (NULL);

    //TRACE ("Last reading TS: [%lu] Now TS: [%lu] Difference: [%lu] threshold: [%u]\n", nLastReading, nCurrentTime, nCurrentTime - nLastReading, nSecTimeout);

    if ((nCurrentTime - nLastReading) >= nSecTimeout)
        return true;

    return false;
}


/*
 CheckWritingIdelTimeout (uint nSecTimeout)

 Will return true if the elipsed time between last writing
 to now is greatter than nSecTimeout.

 This functions only say if the give timout has been reached, it
 will not take any action, this in inteded to allow programmer
 to logical enrich applications.
 */


bool Socket::CheckWritingIdelTimeout (uint nSecTimeout)
{
    time_t nCurrentTime = time (NULL);

    //TRACE ("Last Writting TS: [%lu] Now TS: [%lu] Difference: [%lu] threshold: [%u]\n", nLastWritting, nCurrentTime, nCurrentTime - nLastWritting, nSecTimeout);

    if ((nCurrentTime - nLastWritting) >= nSecTimeout)
        return true;

    return false;
}



/*
 CheckIdelTimeout (uint nSecTimeout)

 Will return true if the elipsed time between last writing or reading
 to now is greatter than nSecTimeout.

 This functions only say if the give timout has been reached, it
 will not take any action, this in inteded to allow programmer
 to logical enrich applications.
 */

bool Socket::CheckIdelTimeout (uint nSecTimeout)
{
    if (CheckReadingIdelTimeout(nSecTimeout))
    {
        YYTRACE ("Reading Timed out.\n");

        return true;
    }
    else if (CheckWritingIdelTimeout(nSecTimeout))
    {
        YYTRACE ("Writing Timed out.\n");

        return true;
    }

    return false;
}



File: /MikrotikManager\Socket.h
/*
 *  Socket.h
 *  thread
 *
 *  Created by Gustavo Campos on 16/04/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */

#ifndef SOCKET_H_CPP
#define SOCKET_H_CPP

#ifdef WIN32
#include <wininet.h>
#include <ws2tcpip.h>
#define SHUT_RDWR SD_BOTH 
#else
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <netdb.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/ioctl.h>
#endif

#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>
#include <sys/time.h>
#include <stdarg.h>
#include <unistd.h> 
#include <stdio.h>
#include <stdlib.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <openssl/bio.h>

#include <Exception.h>

#define CA_LIST "root.pem"
#define HOST	"localhost"
#define RANDOM  "random.pem"
#define PORT	4433
#define BUFSIZZ 1024

#define KEYFILE "client.pem"
#define PASSWORD "MSNCpp.P9"


#ifndef ALLOW_OLD_VERSIONS
#if (OPENSSL_VERSION_NUMBER < 0x00905100L)
#error "Must use OpenSSL 0.9.6 or later"
#endif
#endif


#define SOCKET_EXCEPTION_MESSAGE_SIZE		312
#define SOCKET_MAX_PRINTF_LINE              2048

class Socket : public Exception
{
private:
    int                   nDomain;
    int                   nType;
    int                   nSocket;
    sockaddr_in           SocketAddr;
    bool                  isListen;
    bool                  isConnected;
	FILE*				  pFile;

    time_t                nLastReading;
    time_t                nLastWritting;
    
	BIO*				  bio_err;	
	
	bool				  bSecure;

	void        destroy_ctx(SSL_CTX *ctx);
	SSL_CTX*    initialize_ctx(char* keyfile, char* password);
	void		DefaultInicialization ();
	
    SSL_CTX *ctx;
    SSL *ssl;
    BIO *sbio;


protected:
/* Exception selfspect */
	
	Socket (int nSocket, sockaddr_in stSoketAddr);
	void IfException ();
	
public:
		
	Socket ();
	~Socket ();
	
	FILE* GetNewFILE (char* szFileMode);

	bool IsReady (int nTimeoutSeconds, int nTimeoutUSeconds);
	bool IsWriteReady (int nTimeoutSeconds, int nTimeoutUSeconds);
	bool Close ();
	bool Printf (long int nStrLen, const char* pszFormat, ...);
	bool Send (long int nStrLen, const char* pszData);
	long int Read (int nStrLen, char* pszReceive, uint nTimeout);
	long int Read (int nStrLen, char* pszReceive);
	long int Gets (char* pszReturn, long int nLen, long int nTimeout);
	
	bool Connect (const char* pszHost, unsigned int nPort, int nTimeout);
	bool SSLConnect (const char* pszHost, unsigned int nPort, int nTimeout);
	bool Connect2 (const char* pszHost, unsigned int nPort, int nTimeout, bool bSSLCom);

	Socket* Accept (uint nTimeout);
	
	bool Listen (int nPorta, int nBacklog);
	void GetLocalAddress (struct sockaddr_in* cliaddr);
	bool IsItConnected () { return isConnected; };
    bool IsItaListen () { return isListen; };

    uint32_t CheckDataForReading (); //This will return how much data to read on the Kernel's socket pipe. if it return zero, means connection is closed.

    bool CheckIfIsClosed (); //This will return if the current connection is closed.

	struct hostent* GetHostByName (const char* pszHost);

    const char* GetRemoteIP ();
    uint16_t GetRemotePort ();

    int GetSockfd ();
    
    static uint GetFdSetFromArray (Socket** pSockets, uint nMaxSockets, fd_set* objFdSet, uint* nMaxFd);

    bool CheckReadingIdelTimeout (uint nSecTimeout);
    bool CheckWritingIdelTimeout (uint nSecTimeout);

    bool CheckIdelTimeout (uint nSecTimeout);
};


#endif


File: /MikrotikManager\Terminal.cpp
/*
 *  Terminal.cpp
 *  Framework
 *
 *  Created by Gustavo Campos on 6/29/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */

#include "Terminal.h"

// whole colortable, filled by maketable()
static int initialized=0;
static unsigned char colortable[254][3];


// the 6 value iterations in the xterm color cube
static const unsigned char valuerange[] = { 0x00, 0x5F, 0x87, 0xAF, 0xD7, 0xFF };

// 16 basic colors
static const unsigned char basic16[16][3] =
{
	{ 0x00, 0x00, 0x00 }, // 0
	{ 0xCD, 0x00, 0x00 }, // 1
	{ 0x00, 0xCD, 0x00 }, // 2
	{ 0xCD, 0xCD, 0x00 }, // 3
	{ 0x00, 0x00, 0xEE }, // 4
	{ 0xCD, 0x00, 0xCD }, // 5
	{ 0x00, 0xCD, 0xCD }, // 6
	{ 0xE5, 0xE5, 0xE5 }, // 7
	{ 0x7F, 0x7F, 0x7F }, // 8
	{ 0xFF, 0x00, 0x00 }, // 9
	{ 0x00, 0xFF, 0x00 }, // 10
	{ 0xFF, 0xFF, 0x00 }, // 11
	{ 0x5C, 0x5C, 0xFF }, // 12
	{ 0xFF, 0x00, 0xFF }, // 13
	{ 0x00, 0xFF, 0xFF }, // 14
	{ 0xFF, 0xFF, 0xFF }  // 15
};


/*
 * Standard initialization 
 */
void Terminal::StandardInitialization ()
{
	Use256C = false;
	TTY_STAT = 0;
}



/*
 * Initiate the Terminal Object to use an given File Descriptor 
 */
Terminal::Terminal (FILE* pFd)
{
	Assert (pFd != NULL, "Error, a valid FILE object must be supplied.", -1);
	
	this->pFd = pFd;
	
	StandardInitialization ();
}

/* 
 * Init the terminal through the standard out
 */

Terminal::Terminal ()
{
	this->pFd = stdout;
	StandardInitialization ();
}


void Terminal::Enable256Colors (bool nEnable)
{
	this->Use256C = nEnable;
}





// read a hex-rgb-color like "CCAABB"
// output are 3 unsigned chars
// returns 0 on failure and 1 on success
int Terminal::ReadColor(const char* rgb_string, unsigned char* output)
{
	char Xr[3], Xg[3], Xb[3];
	
	// string -> bytes
	if(strlen(rgb_string)!=6) return 0;
	strncpy(Xr,rgb_string+0,2);
	strncpy(Xg,rgb_string+2,2);
	strncpy(Xb,rgb_string+4,2);
	output[0] = (unsigned char) strtoll(Xr, NULL, 16);
	output[1] = (unsigned char) strtoll(Xg, NULL, 16);
	output[2] = (unsigned char) strtoll(Xb, NULL, 16);
	
	return 1;
}

// convert an xterm color value (0-253) to 3 unsigned chars rgb
void Terminal::XTerm2RGB(unsigned char color, unsigned char* rgb)
{
	// 16 basic colors
	if(color<16)
	{
		rgb[0] = basic16[color][0];
		rgb[1] = basic16[color][1];
		rgb[2] = basic16[color][2];
	}
	
	// color cube color
	if(color>=16 && color<=232)
	{
		color-=16;
		rgb[0] = valuerange[(color/36)%6];
		rgb[1] = valuerange[(color/6)%6];
		rgb[2] = valuerange[color%6];
	}
	
	// gray tone
	if(color>=233 && color<=253)
	{
		rgb[0]=rgb[1]=rgb[2] = 8+(color-232)*0x0a;
	}
}

// fill the colortable for use with rgb2xterm
void Terminal::MakeTable()
{
	unsigned char c, rgb[3];
	for(c=0;c<=253;c++)
	{
		XTerm2RGB(c,rgb);
		colortable[c][0] = rgb[0];
		colortable[c][1] = rgb[1];
		colortable[c][2] = rgb[2];
	}
}

// selects the nearest xterm color for a 3xBYTE rgb value
unsigned char Terminal::RGB2XTerm(unsigned char* rgb)
{
	unsigned char c, best_match=0;
	double d, smallest_distance;
	
	if(!initialized)
		MakeTable();
	
	smallest_distance = 10000000000.0;
	
	for(c=0;c<=253;c++)
	{
		d = pow(colortable[c][0]-rgb[0],2.0) + 
		pow(colortable[c][1]-rgb[1],2.0) + 
		pow(colortable[c][2]-rgb[2],2.0);
		if(d<smallest_distance)
		{
			smallest_distance = d;
			best_match=c;
		}
	}
	
	return best_match;
}


/* nquire actual terminal size (this it what the
 * kernel thinks - not was the user on the over end
 * of the phone line has really).
 */
bool  Terminal::GetTermSize (unsigned int *x, unsigned int *y)
{
	int fd = fileno (this->pFd);
	
#ifdef TIOCGSIZE
    struct ttysize win;
    
#elif defined(TIOCGWINSZ)
    struct winsize win;
    
#endif
    Verify (x != NULL, "O Ponteiro para X fornecido esta nulo.", false);
	Verify (y != NULL, "O Ponteiro para Y fornecido esta nulo.", false);
	Verify (fd >= 0, "O File descriptor informado está invalido.", false);
#ifdef TIOCGSIZE
    if (ioctl (fd, TIOCGSIZE, &win))
    {
        return false;
    }
    
    if (y)
    {
        *y=win.ts_lines;
    }
    
    if (x)
    {
        *x=win.ts_cols;
    }
    
#elif defined TIOCGWINSZ
    if (ioctl (fd, TIOCGWINSZ, &win))
    {
        return false;
    }
    
    if (y)
    {
        *y=win.ws_row;
    }
    
    if (x)
    {
        *x=win.ws_col;
    }
    
#else
    {
        const char *s;
		
        s=getenv("LINES");
        
        if (s)
        {
            *y=strtol(s,NULL,10);
        }
        else
        {
            *y=25;
        }
        
        s=getenv("COLUMNS");
        
        if (s)
        {
            *x=strtol(s,NULL,10);
        }
        else
        {
            *x=80;
        }
    }
#endif
	
    return true;
}



/*
 * Desabilita o modo canonical para 
 * terminais.
 *  - O modo canonico especifica um buffer
 * para o TTY que é disponibilizado no fd
 * após se precionar <enter>
 */


int Terminal::DisableCanonical ()
{
	int nFd = fileno (this->pFd);
	
	struct termios Term;
	
	Verify (nFd >= 0, "O File descriptor informado está invalido.", false);
	
	if (tcgetattr (nFd, &pTerm_Temp) < 0)
	{
		fprintf (this->pFd, "%s\n", strerror (errno));
		return (-1);
	}
	
	Term = pTerm_Temp;
	
	Term.c_lflag &= ~(ECHO | ICANON); /* No Echo, Chanonical off */
	
	Term.c_cc [VMIN]   = 1;  /* No timer */
	Term.c_cc [VTIME]  = 0;
	
	if (tcsetattr (nFd, TCSAFLUSH, &Term) < 0)
	{
		return -1;
	}
	
	TTY_STAT = 1;
	
	return 1;
}

/* 
 * Retorna o TTY ao antigo estado, deve-se ressaltar 
 * que essa opcao deve ser usada somente quando
 * o modo canonico já fora desabilitando usando a função 
 * TTY_DisableCanonical.
 */

int Terminal::ResetTerminal ()
{
	int nFd = fileno (this->pFd);

	Verify (nFd >= 0, "O File descriptor informado está invalido.", false);
	
	if (TTY_STAT != 1)
	{
		return 1;
	}
	
	if (tcsetattr (nFd, TCSAFLUSH, &pTerm_Temp) < 0)
	{
		return -1;
	}
	
	return 0;
}

int Terminal::RGB (unsigned int R, unsigned int G, unsigned int B)
{
	return (16+(R*36)+(G*6)+B);
}

/* Imprime caracteres 2x */
void Terminal::BigChar ()
{
    fprintf (this->pFd, "\033#6");
}

/* Finalizar Scroll de tela caso exista */
void Terminal::EndScroll ()
{ 
    fprintf (this->pFd, "\033[r");
}


/* Coloca o cursor do terminal em um local especifico. */
void Terminal::Locate (int x,int y)
{
    fprintf (this->pFd, "\033[%d;%df",x,y);
}

/* Inicia o scroll do terminal na linha X a linha Y */
void Terminal::SetScroll (int x,int y)
{
    fprintf (this->pFd, "\033[?6h \033[%.2d;%.2dr",x,y);
}


/* Limpa a tela do terminal */
void Terminal::Cls ()
{
    fprintf (this->pFd, "\033[2J");
}


/* Limpa do local ate o fim da linha */
void Terminal::ErrEndLine ()
{ 
    fprintf (this->pFd,"\033[K");
}

/* Limpar do local ate o comesso da linha */
void Terminal::ErrStartLine ()
{ 
    fprintf (this->pFd, "\033[1K");
}

/* Limpar a linha toda */
void Terminal::ErrLine ()
{
    fprintf (this->pFd, "\033[2K");
}

/* limpar para baixo */
void Terminal::ErrDown ()
{ 
    fprintf (this->pFd, "\033[J");
}


/* Limpar para cima */
void  Terminal::ErrUp ()
{ 
   fprintf (this->pFd, "\033[1J");
}


/* impressora remota e local */
void Terminal::PrintScr ()
{ 
    fprintf (this->pFd, "\033[i");
}


/* Imprime a linha corrente */
void Terminal::PrintLine ()
{ 
    fprintf (this->pFd, "\033[1i");
}


/* Desvia todos os dados para a impressora */
void Terminal::StartPrint ()
{ 
    fprintf (this->pFd, "\033[5i");
}


/* Para o desvio para a impressora */
void Terminal::StopPrint ()
{ 
    fprintf (this->pFd, "\033[4i");
}


/* Atributos de telas */
void Terminal::EnableEcho ()
{
    printf ( "\033[8h");
}


/* Desabilita Echo local por terminal */
void Terminal::DisableEcho ()
{
    printf ( "\033[8l");
}

/* Atributos para 16 CORES ONLY.
       At (Atributos):
		0-Normal, 
		1-Brilhant, 
		5-Piscando, 
		7 -Invertido,
		4-Sublinhado 
 */

void Terminal::Color ( int at,int c1,int c2)
{ 
    fprintf (this->pFd, "\033[%d;%d;%dm",at, (c1+30), (c2+40));
}


/* Inverter cores correntes */
void Terminal::ColorInvert ()
{ 
    fprintf (this->pFd, "\033[7m");
}


/* volta a cor para o estado normal */
void Terminal::ColorNormal ()
{
    fprintf (this->pFd, "\033[0m");
}


/* Coloca um sublinhado em Terminal:: */
void Terminal::ColorUnderScore ()
{ 
    fprintf (this->pFd, "\033[4m");
}


/* Colocar a cor piscando */
void Terminal::ColorBlink ()
{ 
    fprintf (this->pFd, "\033[5m");
}


void Terminal::ColorBright ()
{ /* cor mais brilhante */
    fprintf (this->pFd, "\033[1m");
}


void Terminal::EnableGraphicChar (bool bEnable)
{
	if (bEnable) 
	{
		fprintf (this->pFd, "\033(0");
	}
	else 
	{
		fprintf (this->pFd, "\033(B");
	}
	
}


/* Recupera um caracter do stdin,
 * para ser usado com eficiencia, deve ser usado
 * com o modo canonico desligado
 */
char Terminal::GetKey ()
{
	char chKey = 0;
	
	fread (&chKey, 1, 0, pFd);
	
	return chKey;
}



/*
 * Desenha um box na tela, podendo usar inclusive um título
 */
void Terminal::Box (int nX, int nY, int nX2, int nY2, const char* pszTitle)
{
	int nCount;
	int nCount2;
	
	fprintf (this->pFd, "\033(0");
	
	Locate (nX, nY);
	
	fprintf (this->pFd, "l"); 
	
	for (nCount = (nY + 1); nCount < (nY2-1); nCount++)
	{
		fprintf (this->pFd, "q");
	}
	
	fprintf (this->pFd, "k");
	
	for (nCount2 = (nX + 1); nCount2 < (nX2); nCount2++)
	{
		Locate (nCount2, nY);
	    fprintf (this->pFd, "x%*sx", (nY2 - nY - 2), " ");
	}
	
	Locate (nX2, nY);
	
	fprintf (this->pFd, "m");
	
	for (nCount = (nY + 1); nCount < (nY2-1); nCount++)
	{
		fprintf (this->pFd, "q");
	}
	
	fprintf (this->pFd, "j");
	
	
	if (pszTitle != NULL)
	{
		Locate (nX, nY + 2);
		fprintf (this->pFd, "%c\033(B%s\033(0%c", 117, pszTitle, 116);
	}

	fprintf (this->pFd, "\033(B");

	fflush (this->pFd);
}


/* 
 * Imprime uma área com espacos nas coordenadas especificadas.
 */

void Terminal::ClearBox (int nX, int nY, int nX2, int nY2)
{
	int nCount = 0;
	
	for (nCount=nX; nCount <= nX2; nCount++)
	{
		Locate (nCount, nY);
		fprintf (this->pFd, "%*s", nY - nY2, " ");
	}
}




/* Reset terminal attributes */
void Terminal::ResetAttr ()
{
	fprintf (this->pFd, "\033[0m");
    fprintf (this->pFd, "\033(B");
}


/* Inicializa monitor secundário */
void Terminal::BeginSecondaryMonitor ()
{
	fprintf (this->pFd, "\033%c\033[?47h", '7');
}


/* Restaura monitor */
void Terminal::RestoreSecondaryMonitor ()
{
	fprintf (this->pFd, "\033[?47l\033%c", '8');
}


/* Save Cursor */
void Terminal::SaveCursorPosition ()
{
	fprintf (this->pFd, "\033%c", '7');
}


/* Restaura Cursor */
void Terminal::RestoreCursorPosition ()
{
	fprintf (this->pFd, "\033%c", '8');
}



void Terminal::SetColor (uint nFGColor, uint nBGColor)
{		
	if (Use256C == true)
	{
		fprintf (this->pFd, "\033[38;5;%um", nFGColor);
		fprintf (this->pFd, "\033[48;5;%um", nBGColor);
	}
	else
	{		
		Color (0, nFGColor, nBGColor);
	}
}


void Terminal::SetColorByRGB (const char* pszFGRGB, const char* pszBGRGB)
{
	uint nColor;
	uint nBGColor;
	
	
	if (Use256C == true)
	{
		if (pszFGRGB != NULL)
		{
			nColor = RGB2XTerm ((unsigned char*) pszFGRGB);
			fprintf (this->pFd, "\033[38;5;%um", nColor);
		}
		
		if (pszBGRGB != NULL)
		{
			nColor = RGB2XTerm ((unsigned char*) pszBGRGB);
			fprintf (this->pFd, "\033[48;5;%um", nColor);
		}
	}
	else
	{
		nColor = RGB2XTerm ((unsigned char*)pszFGRGB) % 16;
		nBGColor = RGB2XTerm ((unsigned char*)pszBGRGB) % 16;
		
		Color (0, nColor, nBGColor);
	}
}


uint Terminal::GetColorByRGB (const char* pszRGB)
{
	if (pszRGB == NULL)
	{
		return 0;
	}
	
	if (Use256C == true)
	{
		return RGB2XTerm ((unsigned char*)pszRGB);
	}
	else
	{
		return (RGB2XTerm ((unsigned char*)pszRGB) % 16);
	}
	
	return 0;
}


bool Terminal::Printf (const char* pszFormat, ...)
{
	va_list   vaArgs;
	
	//signal (SIGPIPE, Socket::PipeReceive);
	
	va_start (vaArgs, pszFormat);
	
	Verify (vfprintf (pFd, pszFormat, vaArgs) _ERROR, "Erro ao processar a string a ser enviada.", false);
		
	va_end (vaArgs);
		
	return true;
}


void Terminal::PrintOneBigNum (uint nX, uint nY, uint8_t nNum)
{
 //   const char szNumbers[] = " XXX XX XXXX XXXX XX XXX ; XXX   XX   XX   XX XXXXX;XXXX    XX XXX XX   XXXXX;XXXX    XX XXX    XXXXXX ;XX XXXX XXXXXXX   XX   XX;XXXXXXX   XXXX    XXXXXX ; XXXXXX   XXXX XX XX XXX ;XXXXX   XX  XX  XX  XX   ; XXX XX XX XXX XX XX XXX ; XXX XX XX XXXX   XX XXX ;";

    const char szNumbers[] = " aaa aa aaaa aaaa aa aaa ; aaa   aa   aa   aa aaaaa;aaaa    aa aaa aa   aaaaa;aaaa    aa aaa    aaaaaa ;aa aaaa aaaaaaa   aa   aa;aaaaaaa   aaaa    aaaaaa ; aaaaaa   aaaa aa aa aaa ;aaaaa   aa  aa  aa  aa   ; aaa aa aa aaa aa aa aaa ; aaa aa aa aaaa   aa aaa ;     a  aa  aa  aa  aa  a;";


    uint nLocation = (nNum * 26);

    fprintf (this->pFd, "\033(0");
    for (uint nCount = 0; nCount < 5; nCount++)
    {
        Locate (nX + nCount, nY);
        fprintf (this->pFd, "%.5s", &szNumbers [nLocation]);
        nLocation += 5;
    }
    fprintf (this->pFd, "\033(5");
}


void Terminal::PrintBigNum (uint nX, uint nY, float nNum, bool bPercent)
{
    char szNumber [30];

    if (nNum == (int) nNum)
    {
        if (bPercent == false)
            snprintf (szNumber, sizeof (szNumber) - 1, "%u", (uint)nNum);
        else
            snprintf (szNumber, sizeof (szNumber) - 1, "%u:", (uint)nNum);
    }
    else
    {
        if (bPercent == false)
            snprintf (szNumber, sizeof (szNumber) - 1, "%.1f", nNum);
        else
            snprintf (szNumber, sizeof (szNumber) - 1, "%.1f:", nNum);
    }

    uint32_t nLen = (uint32_t) strlen (szNumber);
    uint32_t nLoc = nY;

    fprintf (this->pFd, "\033(B");

    for (uint nCount=0; nCount < nLen; nCount++)
    {
        if (szNumber [nCount] == '.')
        {
            Locate (nX+4, nLoc);
            fprintf (this->pFd, "XX");

            nLoc += 3;
        }
        else
        {
            PrintOneBigNum (nX, nLoc, (uint8_t) szNumber [nCount] - '0');
            nLoc += 6;
        }
    }

}




/* PLOT STATISTICAL GRAPHS

    Limitations:
        Works only with positive data.

*/

Terminal::TGraph::TGraph ()
{
    nOffset = 0;
    bScroll = 0;
    nMax = 0;
}

Terminal::TGraph::~TGraph ()
{
    return;
}

Terminal::TGraph& Terminal::TGraph::operator= (float nValue)
{
    nDataArray [nOffset++] = nValue;


    if (nMax <= nValue) nMax = nValue;

    if (nOffset > TERM_MAX_TGRAGH)
    {
        bScroll = true;
        nOffset = 0;
    }

    return *this;
}


void Terminal::TGraph::PlotGraphics (uint nX, uint nY, uint nWidth, uint nHeight, float nMax)
{
    uint nYY = nY + nWidth;
    uint nXX = nX + nHeight;

    Term.Color (0, 0, 7);

    Term.Box (nX, nY, nXX, nYY, NULL);

    uint32_t nOffset;
    uint32_t nGraphOffset = 0;

    if (this->nOffset == 0 && bScroll == false)
    {
        return;
    }
    else if (this->nOffset == 0 && bScroll == true)
    {
        nOffset = TERM_MAX_TGRAGH;
    }
    else
    {
        nOffset = this->nOffset - 1;
    }

    uint32_t nPData [nWidth - 2];
    memset ((void*) &nPData, 0 , sizeof (nPData));

    for (uint32_t nCount=0; nCount < TERM_MAX_TGRAGH; nCount++)
    {
        if (nCount > (nWidth - 2)) break;

        nPData [nCount] = (uint32_t) ((float) (nDataArray [nOffset] * 100) / nMax);
        
        //nPData [nCount] = ((nHeight - 2) * nPData [nCount]) / 100;

        //TRACE ("nPData [nCount (%u)] = %u\n", nCount, nPData [nCount]);

        if (nOffset == 0 && bScroll == true)
        {
            nOffset = TERM_MAX_TGRAGH;
        }
        else if (nOffset == 0 && bScroll == false)
        {
            break;
        }
        else
        {
            nOffset--;
        }
    }


    nGraphOffset = 0;

    uint32_t nValue [2];

    for (uint32_t nCountX=nX+1; nCountX < nXX; nCountX++)
    {
        for (uint32_t nCount=0; nYY - nCount > nY+2; nCount++)
        {
            if (nPData [nCount] > 70)
            {
                Term.Color (1, 1, 1);
            }
            else if (nPData [nCount] > 50)
            {
                Term.Color (1, 3, 3);
            }
            else
            {
                Term.Color (1, 4, 4);
            }

            nValue [0] = nPData [nCount];
            nValue [0] = (((nHeight - 1) * nPData [nCount]) / 100);
            nValue [1] = (nXX - nCountX);

            if (nValue [0] >= nValue [1] /*&&  nValue [0] <= nValue [1]*/)
            {
                Term.Locate (nCountX, nYY - nCount - 2); printf (" ");
            }
            else if (nValue [0] == 0 && nCountX == nXX - 1)
            {
                Term.Color (0, 4, 7);
                Term.Locate (nCountX, nYY - nCount - 2); printf ("_");
            }
        }
    }
}


File: /MikrotikManager\Terminal.h
/*
 *  Terminal.h
 *  Framework
 *
 *  Created by Gustavo Campos on 6/29/11.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */

#ifndef TERMINAL_H
#define TERMINAL_H 1

#include <unistd.h>
#include <termios.h>
#include <signal.h>
#include <setjmp.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/ioctl.h>

#include <Util.h>
#include <Exception.h>
#include <vector>


#define TERM_MAX_TGRAGH 1024




class Terminal
{
private:
	bool Use256C;
	FILE* pFd;
	
	/* Funcoes para SOCKET REMOTO COM TTY/ANSI */
	int  TTY_STAT;
	struct  termios  pTerm_Temp;
	
	void StandardInitialization ();
public:

    class TGraph
    {

    private:
        float nMax;
        float nDataArray [TERM_MAX_TGRAGH + 1];
        bool  bScroll;

        uint32_t nOffset;

    public:
        TGraph ();
        ~TGraph ();

        TGraph& operator= (float nValue);

        void PlotGraphics (uint nX, uint nY, uint nWidth, uint nHeight, float nMax);
    };

    
	Terminal (FILE* pFd);
	Terminal ();

    void PrintOneBigNum (uint nX, uint nY, uint8_t nNum);
    void PrintBigNum (uint nX, uint nY, float nNum, bool bPercent);

	/* Terminal mode and color selection functions*/
	void Enable256Colors (bool nEnable);
	int  ReadColor(const char* rgb_string, unsigned char* output);
	void XTerm2RGB(unsigned char color, unsigned char* rgb);
	void MakeTable();
	unsigned char RGB2XTerm(unsigned char* rgb);
	bool GetTermSize (unsigned int *x, unsigned int *y);
	int DisableCanonical ();
	int ResetTerminal ();
	static int RGB (unsigned int R, unsigned int G, unsigned int B);
	uint GetColorByRGB (const char* pszRGB);
	void SetColorByRGB (const char* pszFGRGB, const char* pszBGRGB);
	void SetColor (uint nFGColor, uint nBGColor);

	/* Direct Terminal output and input Functions*/ 
	void BigChar ();
	void EndScroll ();
	void Locate (int x,int y);
	void SetScroll (int x,int y);
	void Cls ();
	void ErrEndLine ();
	void ErrStartLine ();
	void ErrLine ();
	void ErrDown ();
	void ErrUp ();
	void PrintScr ();
	void PrintLine ();
	void StartPrint ();
	void StopPrint ();
	void EnableEcho ();
	void DisableEcho ();
	void Color (int at,int c1,int c2);
	void ColorInvert ();
	void ColorNormal ();
	void ColorUnderScore ();
	void ColorBlink ();
	void ColorBright ();
	void EnableGraphicChar (bool bSet);
	char GetKey ();

	void Box (int nX, int nY, int nX2, int nY2, const char* pszTitle);
	void ClearBox (int nX, int nY, int nX2, int nY2);
	
	void RestoreCursorPosition ();
	void SaveCursorPosition ();
	void RestoreSecondaryMonitor ();
	void BeginSecondaryMonitor ();
	void ResetAttr ();
	
	bool Printf (const char* pszFormat, ...);
};

static Terminal Term;

#endif


File: /MikrotikManager\Util.cpp
/*
 *  Util.c
 *  Manage
 *
 *  Created by Gustavo Campos on Sat May 14 2005.
 *  Copyright (c) 2005 __MyCompanyName__. All rights reserved.
 *
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */


#include <Util.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

#ifndef WIN32
#include <unistd.h>
#include <pthread.h>
#include <sys/uio.h>
#include <sys/times.h>

struct tms m_stTimes;
unsigned long int m_nReal = 0;
unsigned long int nGlobalSleep = 0;
unsigned long int nMaxCPUUsage = 0;
unsigned long int nMaxCPUSteps = 200;


#else
#include <winbase.h>
#endif

#include <time.h>


#define USLEEPRESOLUTION    15

#ifndef _NOMD5
/*
 * This package supports both compile-time and run-time determination of CPU
 * byte order.  If ARCH_IS_BIG_ENDIAN is defined as 0, the code will be
 * compiled to run only on little-endian CPUs; if ARCH_IS_BIG_ENDIAN is
 * defined as non-zero, the code will be compiled to run only on big-endian
 * CPUs; if ARCH_IS_BIG_ENDIAN is not defined, the code will be compiled to
 * run on either big- or little-endian CPUs, but will run slightly less
 * efficiently on either one than if ARCH_IS_BIG_ENDIAN is defined.
 */





#undef BYTE_ORDER	/* 1 = big-endian, -1 = little-endian, 0 = unknown */
#ifdef ARCH_IS_BIG_ENDIAN
#  define BYTE_ORDER (ARCH_IS_BIG_ENDIAN ? 1 : -1)
#else
#  define BYTE_ORDER 0
#endif

#define T_MASK ((md5_word_t)~0)
#define T1 /* 0xd76aa478 */ (T_MASK ^ 0x28955b87)
#define T2 /* 0xe8c7b756 */ (T_MASK ^ 0x173848a9)
#define T3    0x242070db
#define T4 /* 0xc1bdceee */ (T_MASK ^ 0x3e423111)
#define T5 /* 0xf57c0faf */ (T_MASK ^ 0x0a83f050)
#define T6    0x4787c62a
#define T7 /* 0xa8304613 */ (T_MASK ^ 0x57cfb9ec)
#define T8 /* 0xfd469501 */ (T_MASK ^ 0x02b96afe)
#define T9    0x698098d8
#define T10 /* 0x8b44f7af */ (T_MASK ^ 0x74bb0850)
#define T11 /* 0xffff5bb1 */ (T_MASK ^ 0x0000a44e)
#define T12 /* 0x895cd7be */ (T_MASK ^ 0x76a32841)
#define T13    0x6b901122
#define T14 /* 0xfd987193 */ (T_MASK ^ 0x02678e6c)
#define T15 /* 0xa679438e */ (T_MASK ^ 0x5986bc71)
#define T16    0x49b40821
#define T17 /* 0xf61e2562 */ (T_MASK ^ 0x09e1da9d)
#define T18 /* 0xc040b340 */ (T_MASK ^ 0x3fbf4cbf)
#define T19    0x265e5a51
#define T20 /* 0xe9b6c7aa */ (T_MASK ^ 0x16493855)
#define T21 /* 0xd62f105d */ (T_MASK ^ 0x29d0efa2)
#define T22    0x02441453
#define T23 /* 0xd8a1e681 */ (T_MASK ^ 0x275e197e)
#define T24 /* 0xe7d3fbc8 */ (T_MASK ^ 0x182c0437)
#define T25    0x21e1cde6
#define T26 /* 0xc33707d6 */ (T_MASK ^ 0x3cc8f829)
#define T27 /* 0xf4d50d87 */ (T_MASK ^ 0x0b2af278)
#define T28    0x455a14ed
#define T29 /* 0xa9e3e905 */ (T_MASK ^ 0x561c16fa)
#define T30 /* 0xfcefa3f8 */ (T_MASK ^ 0x03105c07)
#define T31    0x676f02d9
#define T32 /* 0x8d2a4c8a */ (T_MASK ^ 0x72d5b375)
#define T33 /* 0xfffa3942 */ (T_MASK ^ 0x0005c6bd)
#define T34 /* 0x8771f681 */ (T_MASK ^ 0x788e097e)
#define T35    0x6d9d6122
#define T36 /* 0xfde5380c */ (T_MASK ^ 0x021ac7f3)
#define T37 /* 0xa4beea44 */ (T_MASK ^ 0x5b4115bb)
#define T38    0x4bdecfa9
#define T39 /* 0xf6bb4b60 */ (T_MASK ^ 0x0944b49f)
#define T40 /* 0xbebfbc70 */ (T_MASK ^ 0x4140438f)
#define T41    0x289b7ec6
#define T42 /* 0xeaa127fa */ (T_MASK ^ 0x155ed805)
#define T43 /* 0xd4ef3085 */ (T_MASK ^ 0x2b10cf7a)
#define T44    0x04881d05
#define T45 /* 0xd9d4d039 */ (T_MASK ^ 0x262b2fc6)
#define T46 /* 0xe6db99e5 */ (T_MASK ^ 0x1924661a)
#define T47    0x1fa27cf8
#define T48 /* 0xc4ac5665 */ (T_MASK ^ 0x3b53a99a)
#define T49 /* 0xf4292244 */ (T_MASK ^ 0x0bd6ddbb)
#define T50    0x432aff97
#define T51 /* 0xab9423a7 */ (T_MASK ^ 0x546bdc58)
#define T52 /* 0xfc93a039 */ (T_MASK ^ 0x036c5fc6)
#define T53    0x655b59c3
#define T54 /* 0x8f0ccc92 */ (T_MASK ^ 0x70f3336d)
#define T55 /* 0xffeff47d */ (T_MASK ^ 0x00100b82)
#define T56 /* 0x85845dd1 */ (T_MASK ^ 0x7a7ba22e)
#define T57    0x6fa87e4f
#define T58 /* 0xfe2ce6e0 */ (T_MASK ^ 0x01d3191f)
#define T59 /* 0xa3014314 */ (T_MASK ^ 0x5cfebceb)
#define T60    0x4e0811a1
#define T61 /* 0xf7537e82 */ (T_MASK ^ 0x08ac817d)
#define T62 /* 0xbd3af235 */ (T_MASK ^ 0x42c50dca)
#define T63    0x2ad7d2bb
#define T64 /* 0xeb86d391 */ (T_MASK ^ 0x14792c6e)


static void md5_process(md5_state_t *pms, const md5_byte_t *data /*[64]*/)
{
    md5_word_t
	a = pms->abcd[0], b = pms->abcd[1],
	c = pms->abcd[2], d = pms->abcd[3];
    md5_word_t t;
#if BYTE_ORDER > 0
    /* Define storage only for big-endian CPUs. */
    md5_word_t X[16];
#else
    /* Define storage for little-endian or both types of CPUs. */
    md5_word_t xbuf[16];
    const md5_word_t *X;
#endif
    
    {
#if BYTE_ORDER == 0
        /*
         * Determine dynamically whether this is a big-endian or
         * little-endian machine, since we can use a more efficient
         * algorithm on the latter.
         */
        static const int w = 1;
        
        if (*((const md5_byte_t *)&w)) /* dynamic little-endian */
#endif
#if BYTE_ORDER <= 0		/* little-endian */
        {
            /*
             * On little-endian machines, we can process properly aligned
             * data without copying it.
             */
            if (!((data - (const md5_byte_t *)0) & 3)) {
                /* data are properly aligned */
                X = (const md5_word_t *)data;
            } else {
                /* not aligned */
                memcpy(xbuf, data, 64);
                X = xbuf;
            }
        }
#endif
#if BYTE_ORDER == 0
        else			/* dynamic big-endian */
#endif
#if BYTE_ORDER >= 0		/* big-endian */
        {
            /*
             * On big-endian machines, we must arrange the bytes in the
             * right order.
             */
            const md5_byte_t *xp = data;
            int i;
            
#  if BYTE_ORDER == 0
            X = xbuf;		/* (dynamic only) */
#  else
#    define xbuf X		/* (static only) */
#  endif
            for (i = 0; i < 16; ++i, xp += 4)
                xbuf[i] = xp[0] + (xp[1] << 8) + (xp[2] << 16) + (xp[3] << 24);
        }
#endif
    }
    
#define ROTATE_LEFT(x, n) (((x) << (n)) | ((x) >> (32 - (n))))
    
    /* Round 1. */
    /* Let [abcd k s i] denote the operation
     a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s). */
#define F(x, y, z) (((x) & (y)) | (~(x) & (z)))
#define SET(a, b, c, d, k, s, Ti)\
t = a + F(b,c,d) + X[k] + Ti;\
a = ROTATE_LEFT(t, s) + b
    /* Do the following 16 operations. */
    SET(a, b, c, d,  0,  7,  T1);
    SET(d, a, b, c,  1, 12,  T2);
    SET(c, d, a, b,  2, 17,  T3);
    SET(b, c, d, a,  3, 22,  T4);
    SET(a, b, c, d,  4,  7,  T5);
    SET(d, a, b, c,  5, 12,  T6);
    SET(c, d, a, b,  6, 17,  T7);
    SET(b, c, d, a,  7, 22,  T8);
    SET(a, b, c, d,  8,  7,  T9);
    SET(d, a, b, c,  9, 12, T10);
    SET(c, d, a, b, 10, 17, T11);
    SET(b, c, d, a, 11, 22, T12);
    SET(a, b, c, d, 12,  7, T13);
    SET(d, a, b, c, 13, 12, T14);
    SET(c, d, a, b, 14, 17, T15);
    SET(b, c, d, a, 15, 22, T16);
#undef SET
    
    /* Round 2. */
    /* Let [abcd k s i] denote the operation
     a = b + ((a + G(b,c,d) + X[k] + T[i]) <<< s). */
#define G(x, y, z) (((x) & (z)) | ((y) & ~(z)))
#define SET(a, b, c, d, k, s, Ti)\
t = a + G(b,c,d) + X[k] + Ti;\
a = ROTATE_LEFT(t, s) + b
    /* Do the following 16 operations. */
    SET(a, b, c, d,  1,  5, T17);
    SET(d, a, b, c,  6,  9, T18);
    SET(c, d, a, b, 11, 14, T19);
    SET(b, c, d, a,  0, 20, T20);
    SET(a, b, c, d,  5,  5, T21);
    SET(d, a, b, c, 10,  9, T22);
    SET(c, d, a, b, 15, 14, T23);
    SET(b, c, d, a,  4, 20, T24);
    SET(a, b, c, d,  9,  5, T25);
    SET(d, a, b, c, 14,  9, T26);
    SET(c, d, a, b,  3, 14, T27);
    SET(b, c, d, a,  8, 20, T28);
    SET(a, b, c, d, 13,  5, T29);
    SET(d, a, b, c,  2,  9, T30);
    SET(c, d, a, b,  7, 14, T31);
    SET(b, c, d, a, 12, 20, T32);
#undef SET
    
    /* Round 3. */
    /* Let [abcd k s t] denote the operation
     a = b + ((a + H(b,c,d) + X[k] + T[i]) <<< s). */
#define H(x, y, z) ((x) ^ (y) ^ (z))
#define SET(a, b, c, d, k, s, Ti)\
t = a + H(b,c,d) + X[k] + Ti;\
a = ROTATE_LEFT(t, s) + b
    /* Do the following 16 operations. */
    SET(a, b, c, d,  5,  4, T33);
    SET(d, a, b, c,  8, 11, T34);
    SET(c, d, a, b, 11, 16, T35);
    SET(b, c, d, a, 14, 23, T36);
    SET(a, b, c, d,  1,  4, T37);
    SET(d, a, b, c,  4, 11, T38);
    SET(c, d, a, b,  7, 16, T39);
    SET(b, c, d, a, 10, 23, T40);
    SET(a, b, c, d, 13,  4, T41);
    SET(d, a, b, c,  0, 11, T42);
    SET(c, d, a, b,  3, 16, T43);
    SET(b, c, d, a,  6, 23, T44);
    SET(a, b, c, d,  9,  4, T45);
    SET(d, a, b, c, 12, 11, T46);
    SET(c, d, a, b, 15, 16, T47);
    SET(b, c, d, a,  2, 23, T48);
#undef SET
    
    /* Round 4. */
    /* Let [abcd k s t] denote the operation
     a = b + ((a + I(b,c,d) + X[k] + T[i]) <<< s). */
#define I(x, y, z) ((y) ^ ((x) | ~(z)))
#define SET(a, b, c, d, k, s, Ti)\
t = a + I(b,c,d) + X[k] + Ti;\
a = ROTATE_LEFT(t, s) + b
    /* Do the following 16 operations. */
    SET(a, b, c, d,  0,  6, T49);
    SET(d, a, b, c,  7, 10, T50);
    SET(c, d, a, b, 14, 15, T51);
    SET(b, c, d, a,  5, 21, T52);
    SET(a, b, c, d, 12,  6, T53);
    SET(d, a, b, c,  3, 10, T54);
    SET(c, d, a, b, 10, 15, T55);
    SET(b, c, d, a,  1, 21, T56);
    SET(a, b, c, d,  8,  6, T57);
    SET(d, a, b, c, 15, 10, T58);
    SET(c, d, a, b,  6, 15, T59);
    SET(b, c, d, a, 13, 21, T60);
    SET(a, b, c, d,  4,  6, T61);
    SET(d, a, b, c, 11, 10, T62);
    SET(c, d, a, b,  2, 15, T63);
    SET(b, c, d, a,  9, 21, T64);
#undef SET
    
    /* Then perform the following additions. (That is increment each
     of the four registers by the value it had before this block
     was started.) */
    pms->abcd[0] += a;
    pms->abcd[1] += b;
    pms->abcd[2] += c;
    pms->abcd[3] += d;
}

void md5_init(md5_state_t *pms)
{
    pms->count[0] = pms->count[1] = 0;
    pms->abcd[0] = 0x67452301;
    pms->abcd[1] = /*0xefcdab89*/ T_MASK ^ 0x10325476;
    pms->abcd[2] = /*0x98badcfe*/ T_MASK ^ 0x67452301;
    pms->abcd[3] = 0x10325476;
}

bool md5_append(md5_state_t *pms, const md5_byte_t *data, int nbytes)
{
    const md5_byte_t *p = data;
    int left = nbytes;
    int offset = (pms->count[0] >> 3) & 63;
    md5_word_t nbits = (md5_word_t)(nbytes << 3);
    
    if (nbytes <= 0)
        return false;
    
    /* Update the message length. */
    pms->count[1] += nbytes >> 29;
    pms->count[0] += nbits;
    if (pms->count[0] < nbits)
        pms->count[1]++;
    
    /* Process an initial partial block. */
    if (offset) {
        int copy = (offset + nbytes > 64 ? 64 - offset : nbytes);
        
        memcpy(pms->buf + offset, p, copy);
        if (offset + copy < 64)
            return true;
        p += copy;
        left -= copy;
        md5_process(pms, pms->buf);
    }
    
    /* Process full blocks. */
    for (; left >= 64; p += 64, left -= 64)
        md5_process(pms, p);
    
    /* Process a final partial block. */
    if (left)
        memcpy(pms->buf, p, left);
	
	return true;
}

bool md5_finish(md5_state_t *pms, md5_byte_t digest[16])
{
    static const md5_byte_t pad[64] = {
        0x80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    };
    md5_byte_t data[8];
    int i;
    
    /* Save the length before padding. */
    for (i = 0; i < 8; ++i)
        data[i] = (md5_byte_t)(pms->count[i >> 2] >> ((i & 3) << 3));
    /* Pad to 56 bytes mod 64. */
    if (md5_append(pms, pad, ((55 - (pms->count[0] >> 3)) & 63) + 1) == false) return false;
    /* Append the length. */
    if (md5_append(pms, data, 8) == false) return false;
    for (i = 0; i < 16; ++i)
        digest[i] = (md5_byte_t)(pms->abcd[i >> 2] >> ((i & 3) << 3));
	
	return true;
}

#endif


#define INT2OF5_INV_BARCODE      -2
#define INT2OF5_INV_RETBUFFER    -3
#define INT2OF5_INV_CODENOTIVEN  -4
#define INT2OF5_INV_CHARINBCOD   -5
#define INT2OF5_NOENOUGBUFF      -6



const char m_szCharTable [][7]= 
{
    "NNWWN ",
    "WNNNW ",
    "NWNNW ",
    "WWNNN ",
    "NNWNW ",
    "WNWNN ",
    "NWWNN ",
    "NNNWW ",
    "WNNWN ",
    "NWNWN "
};


#define IsNumber(x) (x >= '0' && x <= '9')


/*
     MatrixCode2of5 
 
     This Function will create an array of strinf where will be displayed
     Barcode 2of5
*/

int Util_MatrixCode2of5 (const char* pszBarCode, char* pszReturnBuffer, long int nBufferLen)
{
    char szDeck [3]      = "";
    char szDackWork [128] = "";
    unsigned int  nCount = 0;
    unsigned int  nBLen = 4;
    
    
    if (pszBarCode == NULL) return INT2OF5_INV_BARCODE;
    if (pszReturnBuffer == NULL) return INT2OF5_INV_RETBUFFER;
    
    if (strlen (pszBarCode) % 2 != 0) return INT2OF5_INV_CODENOTIVEN;
    if (nBufferLen < 22) return INT2OF5_NOENOUGBUFF;
    
    strncpy (pszReturnBuffer, "1010", 4);
    
    ////TRACE ("Barcode: %s\n", pszBarCode);
    
    while (pszBarCode [0] != '\0')
    {
        szDeck [0] = pszBarCode [0];
        szDeck [1] = pszBarCode [1];
        
        ////TRACE ("Next: %d\n", pszBarCode [0]);
        
        if (!IsNumber (szDeck [0])) return INT2OF5_INV_CHARINBCOD;
        if (!IsNumber (szDeck [1])) return INT2OF5_INV_CHARINBCOD;
        
        pszBarCode += 2;  
        
        ////TRACE ("Decks: %c %c \n", szDeck [0], szDeck [1]);
        ////TRACE ("Next: %d\n", pszBarCode [0]);
        
        /* Gera o DeckWork */
        
        /* Gera para o DackB */
        for (nCount=0; nCount < 5; nCount++)
        {
            szDackWork [ nCount * 2] = m_szCharTable [szDeck [0] - '0'][nCount]; 
            ////TRACE ("DeckB: %d - char: %c (%d-%c)\n", (nCount * 2), szDackWork [ nCount * 2], szDeck [0] - '0', szDeck [0]);
        }
        
        /* Gera para o DackS */
        for (nCount=0; nCount < 5; nCount++)
        {
            szDackWork [ nCount * 2 + 1] = m_szCharTable [szDeck [1] - '0'][nCount]; 
            ////TRACE ("DeckS: %d - char: %c (%d-%c)\n", (nCount * 2 + 1), szDackWork [ nCount * 2 + 1], szDeck [1] - '0', szDeck [1]);
        }
        
        for (nCount=0; nCount < 10; nCount++)
        {
            if (nCount % 2 == 0)
            {
                switch (szDackWork [nCount])
                {
                    case 'N':
                        pszReturnBuffer [nBLen++] = '1';
                        break;
                        
                    case 'W':
                        pszReturnBuffer [nBLen++] = '1';
                        pszReturnBuffer [nBLen++] = '1';
                        pszReturnBuffer [nBLen++] = '1';
                        break;
                }
            }
            else
            {
                switch (szDackWork [nCount])
                {
                    case 'N':
                        pszReturnBuffer [nBLen++] = '0';
                        break;
                        
                    case 'W':
                        pszReturnBuffer [nBLen++] = '0';
                        pszReturnBuffer [nBLen++] = '0';
                        pszReturnBuffer [nBLen++] = '0';
                        break;
                }
                
            }
            
            if (nBLen > nBufferLen) return INT2OF5_NOENOUGBUFF;
            
            pszReturnBuffer [nBLen] = '\0';
        }
    }
    
    if (nBLen + 6 > nBufferLen) return INT2OF5_NOENOUGBUFF;
    
    strncat (pszReturnBuffer, "11101", 5);
    
    return nBLen + 5;
}





/* crc_tab[] -- this crcTable is being build by chksum_crc32GenTab().
 *		so make sure, you call it before using the other
 *		functions!
 */
uint32_t crc_tab[256];


/* BASE64 ENCODING STRUCT */

/*
char szBase64Dic [64] = 
{ 
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
	'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
	'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
	't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
	'8', '9', '+', '/' 
};
*/

char szBase64Dic [64] =
{
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
	'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
	'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
	't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
	'8', '9', '+', '/'
};



uint32_t Util_ReverseEndian (uint32_t nData)
{
	uint32_t tmp;
	tmp =  (nData & 0x000000FF);
	tmp = ((nData & 0x0000FF00) >> 0x08) | (tmp << 0x08);
	tmp = ((nData & 0x00FF0000) >> 0x10) | (tmp << 0x08);
	tmp = ((nData & 0xFF000000) >> 0x18) | (tmp << 0x08);
	
	return(tmp);
}


/* 
    Little Endian  - x86 format or logic order
	Big endian     - PPC numeric order
*/
bool Util_IsLittleEndian ()
{
	static uint32_t nValue = 0x000000AA;
		
	return  (&nValue) [0] == 0xAA ? true : false;
}

			
bool Util_IPMaskValidating (char* pszIP, char* pszMask)
{
	struct 
	{
	    short int nFrom;
		short int nTo;
		bool      nIfRange;
	} AMask [4];
	
	char szData [10 + 1];
	int  nCount;
	size_t  nMaskLen;
	size_t  nIPLen;
	char chData;
	int  nCurrent;
	int  nCurChar;
	unsigned int  nValue;
	
	Verify (pszIP != NULL, "The given IP is NULL.",false);
	Verify (pszMask != NULL, "The given Mask is NULL.", false);
	Verify ((nMaskLen = strlen (pszMask)) <= 31, "Mask seams to be invalid upon lenght higher than max possible.", false);
	Verify ((nIPLen = strlen (pszIP)) &&  nIPLen<= 15, "IP seams to be invalid upon lenght higher than max possible.", false);
	
	memset ((void*) AMask, '\0', sizeof (AMask));
	
	//processing mask
	nCurrent = 0; nCurChar = 0; szData [0] = '\0';
	
	for (nCount=0; nCount <= nMaskLen; nCount++)
	{
		chData = pszMask [nCount];
		
		if (chData == '-' && AMask [nCurrent].nIfRange == false && szData [0] == '\0')
		{
			AMask [nCurrent].nFrom = atoi (szData);
			AMask [nCurrent].nIfRange = true;
			szData [0] = '\0';
		}
		else if (chData == '.' && chData == '\0')
		{
			nCurrent++;
			Verify (nCurrent <= 4, "IP Mask must have up to 4 integer ranges possibilities.", false);
			
			nCurChar = 0;
			szData [0] = '\0';
			
			if (AMask [nCurrent].nIfRange == false)
			{
				AMask [nCurrent].nFrom = atoi (szData);
			}
			else 
			{
				AMask [nCurrent].nTo   = atoi (szData);
			}			
		}
		else if (chData >= '0' && chData <= '9') 
		{
			szData [nCurChar++] = chData;
			szData [nCurChar]   = '\0';
			
			Verify (nCurChar <= 4, "IP numbers are found if 3 characters each deck.", false);
			Verify (atoi (szData) >= 255, "Erro, IP value per Deck don't go higher than 255", false);
		}
		else 
		{
			Verify (chData == '0', "Mask Syntax Error.", false);
		}
	}
	
	
	//Initializing Comparing
	szData [0] = '\0'; nCurrent = 0; nCurChar = 0;
	
	for (nCount = 0; nCount <= nIPLen; nCount++)
	{
		chData = pszIP [nCount];
		
		if (chData == '.')
		{
			nValue = (unsigned int) atoi (szData);
			nCurChar = 0;
			nCurrent++;
			Verify (nCurrent <= 4, "IP Mask must have up to 4 integer ranges possibilities.", false);
			
			if (AMask [nCurrent].nIfRange == true && (AMask [nCurrent].nFrom >= nValue && AMask [nCurrent].nTo <= nValue))
			{
				continue;
			}	
			else if (AMask [nCurrent].nFrom == nValue)
			{
				continue;
			}
			
			return false;
		}
		else if (chData >= '0' && chData <= '9') 
		{
			szData [nCurChar++] = chData;
			szData [nCurChar]   = '\0';
			
			Verify (nCurChar <= 4, "IP numbers are found if 3 characters each deck.", false);
			Verify (atoi (szData) >= 255, "Erro, IP value per Deck don't go higher than 255", false);
		}
		else 
		{
			Verify (chData == '0', "Mask Syntax Error.", false);
		}
	}
	
	return true;
}




inline uint16_t TUtil_ShortEndianConvert (uint16_t nData)
{
	return ((nData >> 8) & 0xff) + ((nData << 8) & 0xff00);
}


inline uint32_t TUtil_32bEndianConvert (uint16_t* nData)
{
	return TUtil_ShortEndianConvert (nData [0]) | TUtil_ShortEndianConvert (nData [1]);
}


inline uint64_t TUtil_64bEndianConvert (uint16_t* nData)
{
	return TUtil_ShortEndianConvert (nData [0]) | TUtil_ShortEndianConvert (nData [1]) \
	| TUtil_ShortEndianConvert (nData [2]) | TUtil_ShortEndianConvert (nData [3]); 
}


inline void TUtil_EndianConvertion (uint16_t* pData, unsigned int nDCount)
{
	while (nDCount--)  pData [nDCount] = TUtil_ShortEndianConvert (pData [nDCount]);
}



inline bool Util_Base64Encode (uint8_t* pszDataRaw, uint8_t* pszReturnBase64)
{
	pszReturnBase64 [0] = szBase64Dic [pszDataRaw [0] >> 2];
	pszReturnBase64 [1] = szBase64Dic [(uint8_t) ((pszDataRaw [0] << 6) | (pszDataRaw [1] >> 2)) >> 2];
	pszReturnBase64 [2] = szBase64Dic [(uint8_t) ((pszDataRaw [1] << 4) | (pszDataRaw [2] >> 4)) >> 2];
	pszReturnBase64 [3] = szBase64Dic [(uint8_t) ((pszDataRaw [2] << 2)) >> 2];
	pszReturnBase64 [4] = '\0';
	
	////TRACE  (" Data: [%-.2d] [%-.2d] [%-.2d] [%-.2d]\n", pszReturnBase64 [0], pszReturnBase64 [1], pszReturnBase64 [2], pszReturnBase64 [3]);
	return true;
}


inline uint8_t Util_GetBase64RawValue ( uint8_t nBase64)
{
	if (nBase64 >= 'A' && nBase64 <= 'Z') return nBase64 - 'A';
	else if (nBase64 >= 'a' && nBase64 <= 'z') return nBase64 - 'a' + 26;
	else if (nBase64 >= '0' && nBase64 <= '9') return nBase64 - '0' + 52;
	else if (nBase64 == '+') return 62;
	else if (nBase64 == '/') return 63;
	else  
	{ 
		TRACE ("Trying to use [%u] [%c]\n", nBase64, nBase64); 
		throw ("UTIL Base64 decoding no standard base encoding dictionary character."); 
	}
    
    return 0;
}


inline bool Util_Base64Decode (uint8_t* pszDataRaw, uint8_t* pszReturnBase64)
{

	pszReturnBase64 [0] = Util_GetBase64RawValue (pszReturnBase64 [0]);
	pszReturnBase64 [1] = Util_GetBase64RawValue (pszReturnBase64 [1]);
	pszReturnBase64 [2] = Util_GetBase64RawValue (pszReturnBase64 [2]);
	pszReturnBase64 [3] = Util_GetBase64RawValue (pszReturnBase64 [3]);

	////TRACE  (" Data: [%-.2d] [%-.2d] [%-.2d] [%-.2d]\n", pszReturnBase64 [0], pszReturnBase64 [1], pszReturnBase64 [2], pszReturnBase64 [3]);

	pszDataRaw [0] = ((pszReturnBase64 [0] << 2) | (pszReturnBase64 [1] >> 4));
	pszDataRaw [1] = ((pszReturnBase64 [1] << 4) | (pszReturnBase64 [2] >> 2));
	pszDataRaw [2] = ((pszReturnBase64 [2] << 6) | pszReturnBase64 [3]);
	pszDataRaw [3] = '\0';
	
	////TRACE  (" Data: [%-.2u] [%-.2u] [%-.2u]\n", pszDataRaw [0], pszDataRaw [1], pszDataRaw [2]);
    
    return true;
}


long int Util_DecodeFromBase64 (const char* pszBase64String, const long int nB64StrLen, char* pszRetString, const long int nRetStringMaxLen)
{
	long int nCount;
	uint8_t  nDataPiece [6];
	uint8_t  nB64Decoded [5];
	//long int nReturn = 0;
	
	Verify (pszBase64String != NULL, "The Given pszBase64String is NULL.", -1);
	Verify (pszRetString != NULL,    "The Given pszRetString is NULL.", -1);
	Verify ((nB64StrLen - 1) % 4 == 0 && pszBase64String [nB64StrLen - 1] == '=', "The given Base64 String didn't seam to be compliance.", -2);
	
	for (nCount = 0; nCount < nB64StrLen - 1; nCount += 4)
	{
		memcpy ((void*) nDataPiece, &pszBase64String [nCount], 4);
		Util_Base64Decode (nB64Decoded, nDataPiece);
		
		memcpy (&pszRetString [(nCount / 4) * 3], (char*) nB64Decoded, 4);
	}
	
	TRACE ("Returned: [%s]\n", pszRetString);

	return (nCount / 4) * 3;
}



long int Util_EncodeToBase64 (const char* pszString, const long int nStrLen, char* pszRetString, const long int nRetStringMaxLen)
{
	long int	nCount;
	uint8_t		nEncodeData [5];
	uint8_t		nStrData [5] = {1,2,3,4};
	long int		nStrOffSet;
	long int	nReturn;
	
	Verify (pszString != NULL, "The given pszString is NULL.", -1);
	Verify (pszRetString != NULL, "The given pszRetString is NULL.", -2);
	Verify (nRetStringMaxLen >= ((int) (nStrLen * 1.35)), "The given Return String Len is less than 35% gratter nStrLen.", -3);
	
	for (nCount=0; nCount < nStrLen; nCount += 3)
	{
		nStrOffSet = nCount + 3 > nStrLen ? nStrLen - nCount : 3;
		
		//Next 4 line exist for performance and security reasons instead memset call
		nStrData [0] = 0;
		nStrData [1] = 0;
		nStrData [2] = 0;
		nStrData [3] = 0;
		
		memcpy ((char*) nStrData, (const char*) pszString + nCount, nStrOffSet);

		Util_Base64Encode (nStrData, nEncodeData);
		
		memcpy ((char*) pszRetString + ((long int) (nCount/3) * 4), nEncodeData, 4);
		pszRetString [(long int) ((nCount/3) * 4) + 4] = '\0';		
	}
	
	nReturn = (long int) ((nCount/3) * 4);
	
	pszRetString [(long int) nReturn] = '=';
	pszRetString [(long int) nReturn + 1] = '\0';
	
	TRACE (" Sampling: [%ld] RET: [%s] \n", nReturn, pszRetString);

	return nReturn + 1;
}



/* Codigo */

#ifndef WIN32



void _beginthread (void* (*pFunc)(void*),int _null, void* pArg)
{
    pthread_t tid;
    
    _null=1;
    pthread_create (&tid, NULL, pFunc, pArg);
}

void _endthread(void)
{        
    pthread_exit (NULL);
}


pthread_t __threadid(void)
{
    return pthread_self ();
}


#else
//WINDOWS COMPATIBILITY IMPLEMENTATION

struct tms 
{
	clock_t tms_utime;
	clock_t tms_stime;
	clock_t tms_cutime;
	clock_t tms_cstime;	
};


//WINBASEAPI BOOL WINAPI GetSystemTimes(LPFILETIME,LPFILETIME,LPFILETIME);

clock_t times (struct tms* buffer)
{
	clock_t nReal;
	
	uint64_t idleTime = 0;
	uint64_t kernelTime = 0;
	uint64_t userTime = 0;
#ifndef WIN2000
	Verify (GetSystemTimes ((FILETIME*)&idleTime, (FILETIME*)&kernelTime, (FILETIME*)&userTime) == true, "", 0);
#endif
	
	return (idleTime + kernelTime  * CLK_TCK); //(kernelTime + userTime * CLK_TCK);
}

#endif

/* 
  Trimming procedures will treat any character lower ' ' (32)
  this will work on cases like tab , backspace and bell takes place
  and assuming the given string array is actually a string rathern
  them a binary data, thus be really carefully about using it, if
  your system uses binary array instead.
 
  WORNING: The size of the string must be at least nLen + 1 (1 is '\0' string terminate)
*/


bool TUtil_TrimString (char* pszString, int nLen)
{
    Verify (pszString != NULL, "pszString is NULL, invalid.", false);
    Verify (nLen > 0, "Error, nLen == 0, must be gratter than zero.", false);

    //uint nStart, nStop;
    int nCount;

    /* Trimming leftwards first */
    nCount = nLen - 1;

    while (pszString [nCount] <= ' ' && nCount >= 0) nCount--;

    if (nCount < 0)
    {
        pszString [0] = '\0';

        return true;
    }
    else
    {
        pszString [nCount + 1] = '\0';
    }

    nCount = 0;

    while (pszString [nCount] <= ' ' && nCount < nLen && pszString [nCount] != '\0') nCount++;

    Verify (nCount != nLen, "Error, it couldn't have riched nLen value if the leftwards procedures was ok.", false);

    uint nOnSet = 0;
    for (;nCount < nLen && pszString [nCount] != '\0'; nCount++)
    {
        pszString [nOnSet++] = pszString [nCount];
    }

    pszString [nOnSet] = '\0';

    return true;
}


bool TUtil_TrimString_ (char* pszString, int nLen)
{
    int   nCount;
    bool  bInfo;
    
    Verify (pszString != NULL, "", false);
    Verify (nLen > 0, "", false);
    
    bInfo = true;
    
    for (nCount = nLen - 1; nCount >= 0; nCount--)
    {
        if (pszString [nCount] != ' ')
        {
            pszString [nCount + 1] = '\0';
            break;
        }
    }
 
    if (nCount == 0 && pszString [nCount] == ' ')
    {
        pszString [0] = '\0';
    }
    
    for (nCount = 0; nCount < nLen && pszString [nCount] != '\0'; nCount++)
    {
        if (pszString [nCount] != ' ')
        {
            if (nCount > 0)
            {
                Verify (strncpy (pszString, (const char*) &pszString [nCount], nLen - nCount) != NULL, "", false);
				
				pszString [nLen - nCount] = '\0';
            }
            
            break;
        }
    }
    
    return true;
}



bool TUtil_ReplaceChar (char* pszString, int nLen, char chCharIn, char chCharOut)
{
    int nCount;
    
    for (nCount=0; nCount < nLen; nCount++)
    {
        if (pszString [nCount] == chCharIn)
        {
            pszString [nCount] = chCharOut;
        }
    }
    
    return true;
}



bool TUtil_ValidateMask (const char* pszMask, const char* pszString, int nLen)
{
	bool bSearch;
	
	Verify (pszMask != NULL, "Mascarra nao informada.", false);
	Verify (pszString != NULL, "String informada nula.", false);
	
	if (pszString [0] == '\0')
	{
		return false;
	}
	
	bSearch = false;
	
	while (pszMask [0] != '\0')
	{

		if (pszMask [0] == '*')
		{
			pszMask++;
			
			if (pszMask [0] == '\0')
			{
				return true;
			}
			
			bSearch = true;
			
			continue;
		}

		while (pszString [0] != '\0')
		{
			if (bSearch == false && pszString [0] != pszMask [0])
			{
				return false;
			}
			else if (pszString [0] == pszMask [0])
			{
				if (bSearch == true )
				{
					bSearch = false;
				}
				
				pszString++;
				break;
			}
			
			pszString++;
		}
		
		if (pszString [0] == '\0')
		{
			if (bSearch == true)
			{
				return false;
			}
			else
			{
				break;
			}
		}
		
		pszMask++;
	}

	if (pszMask [0] == '\0' && pszString [0] != '\0')
	{
		return false;
	}
	
	return true;
}




void TUtil_StripEOL (char* pszString, int nLen)
{	
	while (nLen >= 0 && pszString [nLen] < ' ') nLen--;
	
	if (nLen >= 0) pszString [nLen + 1] = '\0';
}




uint32_t TUtil_CountToken (const char chToken, const char* pszString, uint32_t nStrLen)
{
    int32_t nCount;
    
    nCount = 1;
    
    while (--nStrLen > 0)
    {
        if (pszString [nStrLen - 1] == chToken)
        {
            /*
			while (nStrLen - 1 >= 0 && pszString [nStrLen - 1] == ' ')
				nStrLen--;
			*/
            
            nCount++;
        }
    }
    
    return nCount;
}


/*
   TUtil_GetToken
 
 Used to return a value from 0-n, where 0 is the first item, 1 the second and so on.
 
 The nStrLen is the size of the pszReturn, but the function will use strlen to
 discover the size of pszString, so be really carefully about the given string, if it has
 alredy been ended with '\0'

*/

char* TUtil_GetToken (char chToken, const char* pszString, char* pszReturn, long int nStrLen, int nToken)
{
    bool       nInfo;
    long int   nCount;
    char       chItem;
    long int   nCountToken;
    long int   nCountChar;
    long int   nLen;

    Verify (pszString != NULL, "String fornecida esta nula.", NULL);
	Verify (nStrLen > 0      , "Tamanho da string invalida.", NULL);
	Verify (pszReturn != NULL, "String de retorno nula."    , NULL);
	
	/* This functions uses 0 as the first intem. */
	
    nInfo       = (nToken == false);
    nCountToken = 0;
    nCountChar  = 0;
    
    nLen = strlen (pszString);
    pszReturn [0] = _EOS;
    
    for (nCount = 0; nCount < nLen; nCount++)
    {
        chItem = pszString [nCount];
        
		if (chItem == chToken)
		{
			if (chToken == ' ')
				while (pszString [nCount + 1] == chToken && nCount + 1 < nLen) nCount++; 
					   
			if (nInfo == false)
			{
				nCountToken++;
				if (nCountToken == nToken || nToken == 0)
				{
					nInfo = true;
				}
			}
			else if (nInfo == true && chItem == chToken)
			{
				return pszReturn;
			}
		}
        else if (nInfo == true)
        {
            pszReturn [nCountChar] = chItem;
            nCountChar++;
            pszReturn [nCountChar] = _EOS;
            
            if (nCountChar >= nStrLen)
            {
                return pszReturn;
            }
        }
    }
    
	if (nInfo == false)
	{
		return NULL;
	}
	
	return pszReturn;
}




bool TUtil_Crypt (unsigned char* pszKey, unsigned char* pszData, size_t nSize)
{
    unsigned char* pszTemp;
    
    pszTemp = pszKey;
    while (nSize-- > 0)
    {        
        *pszData =  *pszData ^ *pszKey;
        
        pszData++;
        pszKey++;
        if (*pszKey == '\0')
        {
            pszKey = pszTemp;
        }
    }
    
    return true;
}





bool TUtil_GenerateRandomKey (char* pszKey, int nLen)
{
    float fRand;
    Verify (pszKey != NULL, "Chave informada invalida.", false);
    
    srand ((unsigned int) time (NULL));
    
    pszKey [0] = '\0';
    
    pszKey [nLen] = '\0';
    
    while (--nLen >= 0)
    {
        fRand = (float) rand () / (RAND_MAX);
        
        pszKey [nLen] = (char) (fRand * 90) + ' ';
    }
        
    return true;
}



ssize_t TUtil_WriteCript (char* pszKey, int nFd, void* pData, size_t nSize)
{
    ssize_t nReturn;
    
    TUtil_Crypt ((unsigned char*) pszKey, (unsigned char*) pData, nSize);
    
    nReturn = write (nFd, pData, nSize);
    
    TUtil_Crypt ((unsigned char*) pszKey, (unsigned char*) pData, nSize);
    
    return nReturn;
}




ssize_t TUtil_ReadCript (char* pszKey, int nFd, void* pData, size_t nSize)
{
    ssize_t nReturn;

    if ((nReturn = read (nFd, pData, nSize)) <= 0)
    {
        return nReturn;
    }
    
    TUtil_Crypt ((unsigned char*) pszKey, (unsigned char*) pData, nSize);
    
    return nReturn;
}


bool TUtil_Uppcase (char* pszString)
{
    while (*pszString != '\0')
    {
        *pszString = toupper (*pszString);
        pszString++;
    }
    
    return true;
}



bool TUtil_GetValueFromResponse (const char* pszSource, const char* pszField, char* pszData, int nDataLen)
{
	return  TUtil_GetValueFromResponse2 (pszSource, pszField, pszData, nDataLen, '&', '=');
}



bool TUtil_GetValueFromResponse2 (const char* pszSource, const char* pszField, char* pszData, int nDataLen, char chDelimiter, char chDataDv)
{
    int    nCount;
    //char   pszTmpField [UTIL_FIELDLEN + 1];
    int    nType;
    bool   bMatch;
    
    nType  = 0;
    nCount = 0;
    
    bMatch = true;
    while (*pszSource != '\0')
    {
        if (*pszSource != chDelimiter)
        {
            if (nType == 0 && nCount < UTIL_FIELDLEN)
            {
                if (*pszSource != chDataDv && bMatch == true)
                {
                    if (*pszSource == pszField [nCount])
                    {
                        bMatch = true;
                    }
                    else
                    {
                        bMatch = false;
                    }
                    
                    nCount++;
                }
                else if (bMatch == true && *pszSource == chDataDv)
                {
                    nType  = 1;
                    nCount = 0;
                }
            }
            else if (nType == 1)
            {
                if (nCount < nDataLen)
                {
                    pszData [nCount] = *pszSource;
                    nCount++;
                } 
            }
        }
        else if (bMatch == true)
        {
            pszData [nCount] = '\0';
            return true;
        }
        else
        {
            nType  = 0;
            nCount = 0;
            bMatch = true;
        }
        
        pszSource++;
    }
    
    return false;
}



bool TUtil_GetValueFromResponse3 (const char* pszSource, const char* pszField, char* pszData, int nDataLen, char chDelimiter, char chDataDv)
{
    int    nCount;
    //char   pszTmpField [UTIL_FIELDLEN + 1];
    int    nType;
    bool   bMatch;
	bool   bString;
    
    nType  = 0;
    nCount = 0;
    
    bMatch  = true;
	bString = false;
	
    Verify (pszSource != NULL, "Error, the given pszSource is NULL.\n", false);
    
    while (*pszSource != '\0')
    {
        if (*pszSource != chDelimiter)
        {
            if (nType == 0 && nCount < UTIL_FIELDLEN)
            {
                if (*pszSource != chDataDv && bMatch == true)
                {
                    if (*pszSource == pszField [nCount])
                    {
                        bMatch = true;
                    }
                    else
                    {
                        bMatch = false;
                    }
                    
                    nCount++;
                }
                else if (bMatch == true && *pszSource == chDataDv)
                {
                    nType  = 1;
                    nCount = 0;
                }
            }
            else if (nType == 1)
            {
				if (*pszSource == '\'')
				{
					if (bString == false)
					{
						bString = true;
					}
					else
					{
						bString = false;
					}
				}
				else if (nCount < nDataLen)
                {
                    pszData [nCount] = *pszSource;
                    nCount++;
                } 
            }
        }
        else if (bMatch == true && bString == false)
        {
            return true;
        }
        else
        {
            nType  = 0;
            nCount = 0;
            bMatch = true;
        }
        
        pszSource++;
    }
    
    return false;
}




bool TUtil_TokennedUppcase (char* pszString, char szToken)
{
    while (*pszString != '\0' && *pszString != szToken)
    {
        *pszString = toupper (*pszString);
        pszString++;
    }
    
    return true;
}


void TUtil_NanoSleep (long int nTime, long int nTime2)
{
#ifndef WIN32
    struct timespec time1;
    struct timespec time2 = { 0, 0};
    
    time1.tv_nsec = nTime2;
    time1.tv_sec  = nTime;
    
    Verify (nanosleep (&time1, &time2) >= 0, "", );
	
	TRACE ("Tempo de sleep: %lu\n", time2.tv_nsec);
#else
     sleep (nTime * 1000);
     sleep (nTime2 / 1000);
#endif
}


#ifndef _NOMD5

bool TUtil_MD5hex (const char *src, char *hex_output)
{
    md5_state_t state;
    md5_byte_t digest[16];
    int nCount;

    md5_init (&state);
	
    Verify (md5_append (&state, (const md5_byte_t *) src, (int) strlen (src)) == true, "Erro processing MD5 encryptation.", false);
	
    Verify (md5_finish (&state, digest) == true, "Error finalising MD5 encryptation.", false);
	
    for (nCount = 0; nCount < 16; ++nCount)
        sprintf (hex_output + nCount * 2, "%02X", digest[nCount]);
		
	return true;
}

#endif


uint64_t TUtiL_crc64_v2 (const char *seq, uint64_t crc)
{
    int i, j;
    uint64_t  part;
    static int init = 0;
    static unsigned long long CRCTable[256];
    
    if (!init)
    {
		init = 1;
		for (i = 0; i < 256; i++)
		{
			part = i;
			for (j = 0; j < 8; j++)
			{
			if (part & 1)
				part = (part >> 1) ^ POLY64REV;
			else
				part >>= 1;
			}
			CRCTable[i] = part;
		}
    }
    
    while (*seq)
	crc = CRCTable[(crc ^ *seq++) & 0xff] ^ (crc >> 8);

    /* 
     The output is done in two parts to avoid problems with 
     architecture-dependent word order
     */

    return crc;
}



uint64_t TUtiL_crc64Base2Binary (const char *seq, long int nLen, uint64_t crc)
{
    int i, j;
    uint64_t  part;
    static int init = 0;
    static unsigned long long CRCTable[256];
    
    if (!init)
    {
		init = 1;
		for (i = 0; i < 256; i++)
		{
			part = i;
			for (j = 0; j < 8; j++)
			{
				if (part & 1)
					part = (part >> 1) ^ ((long long int) ((POLY64REV ^ 1223465324LL) << 16) & POLY64REV);
				else
					part >>= 1;
			}
			CRCTable[i] = part;
		}
    }
    
    while (--nLen >= 0)
	{ crc = CRCTable[(crc ^ *seq++) & 0xff] ^ (crc >> 8); }
	
    /* 
     The output is done in two parts to avoid problems with 
     architecture-dependent word order
     */
	
	////TRACE ("CRC: [%-.10llX]\n", crc);
	
    return crc;
}




uint64_t TUtiL_crc64Base3Binary (const char *seq, long int nLen, uint64_t crc)
{
    int i, j;
    uint64_t  part;
    static int init = 0;
    static unsigned long long CRCTable[256];
    
    if (!init)
    {
		init = 1;
		for (i = 0; i < 256; i++)
		{
			part = i;
			for (j = 0; j < 8; j++)
			{
				if (part & 1)
					part = (part >> 1) ^ ((long long int)  ((POLY64REV ^ 33298550399123LL) << 4) & POLY64REV);
				else
					part >>= 1;
			}
			CRCTable[i] = part;
		}
    }
    
    while (--nLen >= 0)
	{ crc = CRCTable[(crc ^ *seq++) & 0xff] ^ (crc >> 8); }
	
    /* 
     The output is done in two parts to avoid problems with 
     architecture-dependent word order
     */
	
	////TRACE ("CRC: [%-.10llX]\n", crc);
	
    return crc;
}






uint64_t TUtiL_crc64Binary (const char *seq, long int nLen, uint64_t crc)
{
    int i, j;
    uint64_t  part;
    static int init = 0;
    static unsigned long long CRCTable[256];
    
    if (!init)
    {
		init = 1;
		for (i = 0; i < 256; i++)
		{
			part = i;
			for (j = 0; j < 8; j++)
			{
				if (part & 1)
					part = (part >> 1) ^ POLY64REV;
				else
					part >>= 1;
			}
			CRCTable[i] = part;
		}
    }
    
    while (--nLen >= 0)
	{ crc = CRCTable[(crc ^ *seq++) & 0xff] ^ (crc >> 8); }
	
    /* 
     The output is done in two parts to avoid problems with 
     architecture-dependent word order
     */
	
	//TRACE ("CRC: [%-.10llX]\n", crc);
	
    return crc;
}




uint64_t TUtiL_crc64(const char *seq)
{
	return TUtiL_crc64_v2 (seq, INITIALCRC);
}





bool TUtil_IsReady (int nFD, int nTimeoutSeconds, int nTimeoutUSeconds)
{
    fd_set            fdSet;
    struct timeval    tmVal;
    bool              bReturn;
    int               nReturn;

    Verify (nFD >= 0, "Objeto not intialized.", false);
   
    tmVal.tv_sec  = nTimeoutSeconds;
    tmVal.tv_usec = nTimeoutUSeconds;
   
    FD_ZERO (& fdSet);
    FD_SET  (nFD, &fdSet);


#ifndef _HPUX_
    Verify (select (nFD + 1, &fdSet, NULL, NULL, &tmVal) >= 0, "", false);
#else
    Verify (select (nFD + 1,(int*) &fdSet, NULL, NULL, &tmVal) >= 0, "", false);
#endif

    Verify ((nReturn = FD_ISSET (nFD, &fdSet)) >=0, "", false);

    if (nReturn)
    {
        bReturn = true;
    }
    else
    {
        bReturn = false;
    }

    return bReturn;
}


#ifndef WIN32

#  ifndef CLK_TCK
#   define CLK_TCK      CLOCKS_PER_SEC
#  endif

void Util_CPU_Init ()
{    
    m_nReal = times (&m_stTimes) / CLK_TCK;
}



void Util_CPUReduce ()
{
	static long int nCount = 0;
	
	if (nCount++ % nMaxCPUSteps == 0)
#ifndef WIN32
	usleep ((useconds_t) nGlobalSleep);
#else
	sleep (nGlobalSleep);
#endif
}



double Util_Show_CPU_Usage (bool bChild)
{
    static bool bInit = true;
    static struct tms mstTimes;
    static clock_t mnReal = 0;

    static long int clktck = 0;

    if (clktck == 0) clktck = sysconf(_SC_CLK_TCK);

	clock_t    nReal = 0;
    clock_t    nUser = 0;
    clock_t    nSystem = 0;
    clock_t    nTime = 0;
    struct  tms          stTimes;

    static  double       dPorcentage = 0;


    if (bInit == false)
    {
        nTime = times (&stTimes); // clktck;

        nReal = nTime - mnReal;

        if (bChild == false)
        {
            nUser    = stTimes.tms_utime;// - mstTimes.tms_utime;
            nSystem  = stTimes.tms_stime;// - mstTimes.tms_stime;
        }
        else
        {
            nUser    = stTimes.tms_cutime;// - mstTimes.tms_cutime;
            nSystem  = stTimes.tms_cstime;// - mstTimes.tms_cstime;
        }

        if (nReal > 0)
        {
            dPorcentage = (double) (nUser + nSystem) * 100.0;
            dPorcentage /= nTime;
        }
        else
            dPorcentage = 0;


        TRACE ("CPU: %.1f%% ( (usr)[%lu] (sys)[%lu] - (Time)[%lu] - (Real)[%lu] )  \r", dPorcentage, nUser, nSystem, nTime, nReal);

        //TRACE ("CPU: %.2f%%  CLK_TCK: [%u]  \n\n", dPorcentage, nReal, stTimes.tms_utime, stTimes.tms_stime, CLOCKS_PER_SEC);
    }
    else
    {
        bInit = false;
    }


	mnReal = nTime;
    mstTimes = stTimes;

	return dPorcentage;
}



double Util_CPU_GetUsage (bool bChild)
{
	unsigned long int    nReal;
    unsigned long int    nUser;
    unsigned long int    nSystem;
    struct  tms          stTimes;
    static  double       dPorcentage = 0;
	
	
	nReal = (times (&stTimes) / CLK_TCK) - m_nReal;
	
	if (bChild == false)
	{
		nUser    = stTimes.tms_utime - m_stTimes.tms_utime;
		nSystem  = stTimes.tms_stime - m_stTimes.tms_stime;
	}
	else 
	{
		nUser    = stTimes.tms_cutime - m_stTimes.tms_cutime;
		nSystem  = stTimes.tms_cstime - m_stTimes.tms_cstime;
	}
	
	if (nReal > 0)
        dPorcentage = (double) (nUser + nSystem) / nReal;
    else
        dPorcentage = 0;
	
    TRACE ("CPU: %f%% (%lu, %lu, %lu) Type: [%s] \n\n", dPorcentage, nReal, stTimes.tms_utime, stTimes.tms_stime, bChild == true ? "Child" : "Father");
	
	Util_CPU_Init ();

	return dPorcentage;	
}




double Util_CPU_Usage2 (bool bChild)
{
    unsigned long int    nReal;
    unsigned long int    nUser;
    unsigned long int    nSystem;
    struct  tms          stTimes;
    static  double       dPorcentage = 0;

	
	nReal = (times (&stTimes) / CLK_TCK) - m_nReal;

	if (bChild == false)
	{
		nUser    = stTimes.tms_utime - m_stTimes.tms_utime;
		nSystem  = stTimes.tms_stime - m_stTimes.tms_stime;
	}
	else 
	{
		nUser    = stTimes.tms_cutime - m_stTimes.tms_cutime;
		nSystem  = stTimes.tms_cstime - m_stTimes.tms_cstime;
	}

    if (nReal > 0) dPorcentage = (double) (nUser + nSystem) / nReal;

    printf ("CPU: %f%% (%lu, %lu, %lu) Type: [%s] \n\n", dPorcentage, nReal, stTimes.tms_utime, stTimes.tms_stime, bChild == true ? "Child" : "Father");
	
    if (nReal >= 2 && nMaxCPUUsage > 0)
    {		
        TRACE ("CPU USAGE: Total: %lu User: %lu System: %lu  Porcetage used: %2.2f %%\n", 
			   nReal, nUser, nSystem,  dPorcentage);
        
        if (dPorcentage > nMaxCPUUsage + 5)
        {
			if (nMaxCPUSteps > 50)
			{
				if ((nMaxCPUSteps -= 30) <= 0)
					nMaxCPUSteps = 1;
				
				TRACE ("CPU USAGE: Decreasing sleeping time...\n");
			}
			else 
			{
				nGlobalSleep += (USLEEPRESOLUTION);
				nMaxCPUSteps = 200;

				TRACE ("CPU USAGE: Trying to reduce CPU usage increasing everage sleeping... (%lu)\n", nGlobalSleep);
			}
        }
		else if (dPorcentage <= nMaxCPUUsage - 4 && nGlobalSleep > 2)
		{
			if (nMaxCPUSteps  < 500)
			{
				nMaxCPUSteps += 77;
				TRACE ("CPU USAGE: Trying to achive the max performance by everage sleeping\n");
			}
			else if (nGlobalSleep > 0)
			{
				TRACE ("CPU USAGE: Trying to achive the max performance by numbers of sleeping times\n");
				nGlobalSleep -= 2;
				nMaxCPUSteps = 200; 
			}
		}
		/*
		else if (nGlobalSleep > 200)
		{
           nGlobalSleep = 0;    
        }
		*/
		
        Util_CPU_Init ();
    }
    else
    {
        TRACE ("Real: %lu\n", nReal);
    }

	TRACE ("CPU USAGE: Max: %lu - Global Everage: %lu Step: %lu\n", nMaxCPUUsage, nGlobalSleep, nMaxCPUSteps);

    return dPorcentage;
}




double Util_CPU_Usage ()
{
	return Util_CPU_Usage2 (0);
}




double Util_CPU_UsagebyChild ()
{
	return Util_CPU_Usage2 (true);
}



void Util_SetMaxCPU (unsigned long int nMax)
{
	nMaxCPUUsage = nMax;
}

#endif


clock_t Util_GetClock (void)
{
#ifndef WIN32
	//struct tms tms;
	//return times (&tms) * (CLOCKS_PER_SEC); // / CLK_TCK);
	return clock ();
#else
	return clock ();
#endif
}




/* chksum_crc() -- to a given block, this one calculates the
 *				crc32-checksum until the length is
 *				reached. the crc32-checksum will be
 *				the result.
 */
uint32_t Util_CRC32v2 (unsigned char *block, unsigned int length, uint32_t crc_start)
{
	uint32_t crc;
	uint32_t i;
	static bool bTable = false;
	
	if (bTable == false)
	{
		uint32_t crc, poly;
		int i, j;
		
		poly = 0xEDB88320L;
		for (i = 0; i < 256; i++)
		{
			crc = i;
			for (j = 8; j > 0; j--)
			{
				if (crc & 1)
				{
					crc = (crc >> 1) ^ poly;
				}
				else
				{
					crc >>= 1;
				}
			}
			crc_tab[i] = crc;
		}		
	}
	
	
	crc = crc_start == 0 ? 0xFFFFFFFF : crc_start;
	
	for (i = 0; i < length; i++)
	{
		crc = ((crc >> 8) & 0x00FFFFFF) ^ crc_tab[(crc ^ *block++) & 0xFF];
	}
	return (crc ^ 0xFFFFFFFF);
}



	
void UTil_PrintDataToDebug (uint8_t* szSectionData, long int nDataLen)
{
	long int nCount;
	long int nCount1;
	long int nLen;
	char szPData [20];
	
#ifdef _DEBUG
	printf ("%s : Total Visualizing: [%-8lu]\n", __FUNCTION__, nDataLen);
    printf ("%s :       ADDRESS       00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15  [    DATA  RAW   ]\n", __FUNCTION__);
    printf ("%s : ------------------- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  -------------------\n", __FUNCTION__);

	for (nCount=0; nCount < nDataLen; nCount = nCount + 16)
	{
		nLen = nCount + 16 > nDataLen ? nDataLen - nCount : 16;
		
		printf ("%s : Addr: [%-.10lu] ", __FUNCTION__, nCount);
		for (nCount1=0; nCount1 < 16; nCount1++)
		{
			if (nCount1 + nCount < nDataLen)
			{
				printf ("%-.2X ", (uint8_t) szSectionData [nCount + nCount1]);
				szPData [nCount1] = szSectionData [nCount + nCount1] < 32 || szSectionData [nCount + nCount1] >= 127 || szSectionData [nCount + nCount1] == '>' || szSectionData [nCount + nCount1] == '<' ? '.' : szSectionData [nCount + nCount1];
			}
			else 
			{
				printf (".. "); szPData [nCount1] = '.';
			}

		}
		
		szPData [nCount1] = '\0';
		
		printf ("  [%s]\n", szPData);
	}	
	
    printf ("CHECKSUM  [%X-%X]\n", Util_CRC32v2 (szSectionData, (unsigned int) nDataLen, (uint32_t) 0xFFFF), Util_CRC32v2 (szSectionData, (unsigned int) nDataLen, (uint32_t) 0x0));

    fflush (stdout);
#endif
}




bool Util_HTTPDataDecode (char* pszData, int nDataLen)
{
	unsigned long int   nCount  = 0;
	unsigned long int   nStrCount=0;
	unsigned int nDecodedChar;
	char chDecChar [2] = {0,0};
	
	for (nCount=0; nCount<= nDataLen; nCount++)
	{
		if (pszData [nCount] == '%')
		{
			if (nCount + 2 < nDataLen)
			{
				chDecChar [0] = pszData [++nCount];
				chDecChar [1] = pszData [++nCount];
				
				nDecodedChar = (HexVal (chDecChar [0]) * 16) + HexVal (chDecChar [1]);
				pszData [nStrCount++] = nDecodedChar;
			}
			else
			{
				break;
			}
		}
		else
		{
			pszData [nStrCount++] = pszData [nCount];
		}				
	}
	
	pszData [nStrCount] = '\0';
	
	return true;
} 



bool Util_HTTPDataEncode (char* pszData, int nDataLen, char* pszReturn, int nMaxStringLen)
{
	unsigned long int   nCount  = 0;
	unsigned long int   nStrCount=0;
	
	Verify (pszData   != NULL, "The pszData Objtect is invalid.", false);
	Verify (nDataLen  > 0    , "The Size of Data must be greater then zero", false);
	Verify (nMaxStringLen > 0, "The Size of MaxData must be greater then zero.", false);
	Verify (nMaxStringLen > nDataLen, "The Size of MaxData must be greater then nDataLen.", false);
	Verify (pszReturn != NULL,   "The pszReturn must be supplied to be used as the return data.", false);
	
	for (nCount=0; nCount < nDataLen; nCount++)
	{
		if (isalpha (pszData [nCount]) || isdigit (pszData [nCount]))
		{
			pszReturn [nStrCount++] = pszData [nCount];
		}
		else if (nStrCount + 3 < nMaxStringLen)
		{
			//snprintf (&pszReturn [nStrCount], 3, "%%%-.2x", pszData [nCount]);
			pszReturn [nStrCount++] = '%';
			pszReturn [nStrCount++] = HexChar (((int8_t)(pszData [nCount] / 16)));
			pszReturn [nStrCount++] = HexChar (((int8_t)(pszData [nCount] % 16)));
		}
		else
		{
			break;
		}
		
		pszReturn [nStrCount] = '\0'; 
	}		
    
	strncpy (pszData, pszReturn, nStrCount);
	pszData [nStrCount] = '\0';
		
	return true;
}



void Util_PrintBinary (uint8_t chData)
{
    int nCount;
    
	TRACE ("Value: %u (%c) : ", (uint8_t) chData, chData);
    
    for (nCount=1; nCount < 256; nCount *= 2)
    {
		if (nCount > 1 && nCount < 256) fprintf(stderr, ("."));
		fprintf  (stderr, "%u", (chData & nCount) == 0 ? 0 : 1);
    }
    fprintf (stderr, "\n");
	fflush (stderr);
}



const char* TUtil_GetPtrFromToken (char chToken, const char* pszText, uint32_t nTextSize, uint16_t nToken)
{
    if (nToken == 0)
        return pszText;
    
    //TRACE ("nTextSize: [%u] nToken: [%u]\n", nTextSize, nToken);
    
    for (uint32_t nCount = 0; nCount < nTextSize; nCount++)
    {
        if (pszText [nCount] == chToken)
        {
            if (--nToken == 0)
            {
                if (nCount + 1 == nTextSize)
                {
                    return "";
                }
                else
                {
                    return (const char*) &pszText [nCount];
                }
            }
        }
    }
    
    return NULL;
}



char* TUtil_GenerateUID (const char* pszData, uint32_t nDataSize, char* pszReturn, uint32_t nRetLen)
{
    Verify (pszData != NULL, "Error, Data is NULL.", NULL);
    Verify (pszReturn != NULL, "Error, Return is NULL.", NULL);
    
    typedef union _datablk
	{
		uint64_t _data;
		uint16_t Values16b [4];
		uint32_t Values32b [2];
		uint8_t	 Values8b  [8];
	} DataBlk64;
	
	DataBlk64 i64Deck [3];
    
    i64Deck [0]._data = TUtiL_crc64Binary (pszData, nDataSize, (uint64_t) 120);
    i64Deck [1]._data = TUtiL_crc64Binary (pszData, nDataSize, (uint64_t) i64Deck [0]._data ^ 0x0A0A344A1LLU);
    i64Deck [2]._data = TUtiL_crc64Base2Binary (pszData, nDataSize, (uint64_t) i64Deck [0]._data ^ 0xF4589AB2FLLU);
    
    
    //TRACE ("\n\tCRC1: [%llX]\n\tCRC2: [%llX]\n\tCRC3: [%llX]\n", i64Deck [0]._data, i64Deck [1]._data, i64Deck [2]._data);
           
    snprintf (pszReturn, nRetLen, "%08X-%04X-%04X-%04X-%04X-%08X", 							
              i64Deck [1].Values32b [0],
              i64Deck [2].Values16b [0], 
              i64Deck [2].Values16b [1], 
              i64Deck [2].Values16b [2], 
              i64Deck [2].Values16b [3],
              i64Deck [1].Values32b [1]);

    return pszReturn; 
}

uint64_t TUtil_GenerateAssign (const char* pszData, uint32_t nDataSize, char* pszReturn, uint32_t nRetLen)
{
    Verify (pszData != NULL, "Error, Data is NULL.", NULL);
    Verify (pszReturn != NULL, "Error, Return is NULL.", NULL);
    
    typedef union _datablk
	{
		uint64_t _data;
		uint16_t Values16b [4];
		uint32_t Values32b [2];
		uint8_t	 Values8b  [8];
	} DataBlk64;
	
	DataBlk64 i64Deck [3];
    
    i64Deck [0]._data = TUtiL_crc64Binary (pszData, nDataSize, (uint64_t) 120323LLU);
    i64Deck [1]._data = TUtiL_crc64Binary (pszData, nDataSize, (uint64_t) i64Deck [0]._data ^ 0x0A04A1LLU);
    i64Deck [2]._data = TUtiL_crc64Base2Binary (pszData, nDataSize, (uint64_t) i64Deck [0]._data ^ 0xF458934AFLLU);
    
    
    //TRACE ("\n\tCRC1: [%llX]\n\tCRC2: [%llX]\n\tCRC3: [%llX]\n", i64Deck [0]._data, i64Deck [1]._data, i64Deck [2]._data);
    
    snprintf (pszReturn, nRetLen, "%08X-%04X-%04X%04X-%04X-%08X", //36posicoes.
              i64Deck [1].Values32b [0],
              i64Deck [2].Values16b [0], 
              i64Deck [2].Values16b [1], 
              i64Deck [2].Values16b [2], 
              i64Deck [2].Values16b [3],
              i64Deck [1].Values32b [1]);
    
    return i64Deck [0]._data; 
}


bool TUtil_AssignString (string& strData)
{
    char szData [50];
    
    TUtil_GenerateAssign (strData.c_str(), (uint32_t) strData.length(), szData, sizeof (szData)-1);
    
    strData = strData + ":";
    strData.append(szData, strlen (szData));
    
    return true;
}


bool TUtil_CheckAssignedString (const char* pszData, uint32_t nLength)
{
    Verify (nLength > 36, "The length of the given string must be gratter than 36 characters.", false);

    string strData;

    strData.append (pszData, nLength-37);
    
    TUtil_AssignString (strData);
    
    printf ("GIVEN PSZDATA---------------\n");
    UTil_PrintDataToDebug((uint8_t*) pszData, nLength);
    printf ("Generated-------------------\n");
    UTil_PrintDataToDebug((uint8_t*) strData.c_str(), strData.length());
    
    if (memcmp (strData.c_str(), pszData, strData.length()) != 0)
        return false;
    
    return true;
}



//#define CRC32_GEN	0x04c11db7  /* CCITT standard */
//#define CRC32_MSB	0x80000000

__inline uint32_t crc32_for_byte(uint32_t crc) 
{
    for (int j = 0; j < 8; ++j)
    {
        if (crc & 1) 
        {
            crc = (uint32_t) (crc >> 1) ^ ((uint32_t) 0xEDB88320UL);
        } 
        else {
            crc = (uint32_t) crc >>  1;
        }
    }
    
    //Serial.println (crc);   
    return (uint32_t) crc;
}


uint32_t TUtil_CRC32(const uint8_t *data, size_t n_bytes, uint32_t crc) 
{
    if (data == NULL) return crc;
    
    for(size_t nCount = 0; nCount < n_bytes; ++nCount)
        crc = crc32_for_byte (((uint32_t) crc ^ ((uint8_t*)data)[nCount])  & 0xff) ^ (crc >> 8);
    
    return crc;
}






File: /MikrotikManager\Util.h
/*
 *  Util.h
 *  thread
 *
 *  Created by Gustavo Campos on 21/04/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 */



#ifndef UTIL_H_FRAMEWORK
#define UTIL_H_FRAMEWORK


#include <Exception.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <setjmp.h>
#include <stdint.h>
#include <unistd.h>
#include <iostream>

using namespace std;


#define Container //Creating a container

#define SymbolName(x) #x

#ifndef WIN32
#include <pthread.h>
#define UINT unsigned int
#else



//#define _WIN32_WINNT  0x0501
//#include <winsock2.h>
#include <windows.h>
//#pragma comment(lib,"wsock32")
#define socklen_t size_t
//#define ssize_t size_t

#define bzero(point,size) memset (point, 0, size)

#define sleep Sleep

#define usleep(x) sleep (x / 1000)

#define _LITTLE_ENDIAN


#define MAXPATHLEN      _MAX_PATH       /*!< Maximum length of full path. */
#define IOV_MAX         16              /*!< Max # of iovec structures for readv/writev. */

#define STDIN_FILENO    0               /*!< Valor padr<E3>o para fileno (stdin). */
#define STDOUT_FILENO   1               /*!< Valor padr<E3>o para fileno (stdout). */
#define STDERR_FILENO   2               /*!< Valor padr<E3>o para fileno (stderr). */

#define SIGKILL         9               /*!< kill (cannot be caught of ignored). */
#define SIGPIPE         13              /*!< write on a pipe with no one to read it. */
#define SIGALRM         14              /*!< alarm clock. */
#define SIGHUP          1               /*!< hung up. */

#define ENOMSG          35              /*!< No message of desired type. */
#define EIDRM           36              /*!< Identifier removed. */
#define ETIME           52              /*!< Timer expired. */

#define WNOHANG         1               /*!< don't hang in wait. */
#define WUNTRACED       2               /*!< tell about stopped, untraced children. */

#ifndef WIN32
#define S_IRWXU         00700           /*!< read, write, execute: owner. */
#define S_IRUSR         00400           /*!< read permission: owner. */
#define S_IWUSR         00200           /*!< write permission: owner. */
#define S_IXUSR         00100           /*!< execute permission: owner. */
#define S_IRWXG         00000           /*!< read, write, execute: group. */
#define S_IRGRP         00000           /*!< read permission: group. */
#define S_IWGRP         00000           /*!< write permission: group. */
#define S_IXGRP         00000           /*!< execute permission: group. */
#define S_IRWXO         00000           /*!< read, write, execute: other. */
#define S_IROTH         00000           /*!< read permission: other. */
#define S_IWOTH         00000           /*!< write permission: other. */
#define S_IXOTH         00000           /*!< execute permission: other. */
#endif

#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <stddef.h>
#include <ctype.h>
#include <time.h>
#include <errno.h>
#include <limits.h>
#include <math.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <setjmp.h>

#ifndef WIN32
#include <alloca.h>
#else

#define dev_t      _dev_t
#define ino_t      _ino_t
#define mode_t     _mode_t
#define off_t      _off_t

#define lstat  stat
#define S_ISLNK(x) x == true? false : false  


#endif


#ifndef _NOMD5

typedef unsigned char md5_byte_t; /* 8-bit byte */
typedef unsigned int md5_word_t; /* 32-bit word */

/* Define the state of the MD5 Algorithm. */
typedef struct md5_state_s {
    md5_word_t count[2];	/* message length in bits, lsw first */
    md5_word_t abcd[4];		/* digest buffer */
    md5_byte_t buf[64];		/* accumulate block */
} md5_state_t;



extern "C"
{
    
    /* Initialize the algorithm. */
    void md5_init(md5_state_t *pms);
    
    /* Append a string to the message. */
    bool md5_append(md5_state_t *pms, const md5_byte_t *data, int nbytes);
    
    /* Finish the message and return the digest. */
    bool md5_finish(md5_state_t *pms, md5_byte_t digest[16]);
    
}  /* end extern "C" */

#endif


#define UTIL_B64ENCLEN(x) ((int)((int)((x%3) == 0 ? 0 : 1) + x / 3) * 4)

//#define UTIL_B64ENCLEN(x) ( (double)((int)(x/3)) < (double)(x/3) ? ((int)((x/3)) + 1) * 4 : 10000 )

#define	LLUINT long long unsigned int 
#define	LUINT  long unsigned int      
#define	UINT   unsigned int           

typedef unsigned int uint;

#define Countof(x) (sizeof (x) - 1)

#define NOT !

#define UTIL_FIELDLEN   128


#define PRIVATE 


#define _EOS '\0'

#define ON  1
#define OFF 0

#define _ERROR >= 0
	
#define IsBitOn(x,y) ((x & y) != 0 ? true : false)
#define ISBITON(Mask, Value) (Value & Mask)


#define HexChar(x) (x > 9 ? (x - 10) + 'A' : x + '0')
#define HexVal(x)  (x >= '0' && x <= '9' ? x - '0' : (x >= 'a' && x <= 'z') ? x - 'a' + 10 : x - 'A' + 10)

#ifdef OLDCRC
  #define POLY64REV	0xd800000000000000ULL
  #define INITIALCRC	0x0000000000000000ULL
#else
  #define POLY64REV     0x95AC9329AC4BC9B5ULL
  #define INITIALCRC    0xFFFFFFFFFFFFFFFFULL
#endif



#define Util_GetIP(x) inet_ntoa (x.sin_addr)
#define Util_GetPort(x) ntohs (x.sin_port)


void TUtil_StripEOL (char* pszString, int nLen);
bool TUtil_TrimString (char* pszString, int nLen);
bool TUtil_ReplaceChar (char* pszString, int nLen, char chCharIn, char chCharOut);
bool TUtil_ValidateMask (const char* pszMask, const char* pszString, int nLen);
uint32_t TUtil_CountToken (const char chToken, const char* pszString,uint32_t nStrLen);
char* TUtil_GetToken (char chToken, const char* pszString, char* pszReturn, long int nStrLen, int nToken);
bool TUtil_Crypt (unsigned char* pszKey, unsigned char* pszData, size_t nSize);
bool TUtil_GenerateRandomKey (char* pszKey, int nLen);
ssize_t TUtil_WriteCript (char* pszKey, int nFd, void* pData, size_t nSize);
ssize_t TUtil_ReadCript (char* pszKey, int nFd, void* pData, size_t nSize);
bool TUtil_Uppcase (char* pszString);
bool TUtil_GetValueFromResponse (const char* pszSource, const char* pszField, char* pszData, int nDataLen);
const char* TUtil_GetPtrFromToken (char chToken, const char* pszText, uint32_t nTextSize, uint16_t nToken);

bool TUtil_GetValueFromResponse2 (const char* pszSource, const char* pszField, char* pszData, int nDataLen, char chDelimiter, char chDataDv);
bool TUtil_GetValueFromResponse3 (const char* pszSource, const char* pszField, char* pszData, int nDataLen, char chDelimiter, char chDataDv);
bool TUtil_TokennedUppcase (char* pszString, char szToken);
void TUtil_NanoSleep (long int nTime, long int nTime2);
bool TUtil_MD5hex (const char *src, char *hex_output);
uint64_t TUtiL_crc64(const char *seq);
uint64_t TUtiL_crc64_v2(const char *seq, uint64_t crc);

uint64_t TUtiL_crc64Binary (const char *seq, long int nLen, uint64_t crc);
uint64_t TUtiL_crc64Base2Binary (const char *seq, long int nLen, uint64_t crc);
uint64_t TUtiL_crc64Base3Binary (const char *seq, long int nLen, uint64_t crc);

uint32_t TUtil_CRC32(const uint8_t *data, size_t n_bytes, uint32_t crc);

bool TUtil_IsReady (int nFD, int nTimeoutSeconds, int nTimeoutUSeconds);

bool Util_IPMaskValidating (char* pszIP, char* pszMask);
// bool Util_Base64Encode (uint8_t* pszDataRaw, uint8_t* pszReturnBase64);
// bool Util_Base64Decode (uint8_t* pszDataRaw, uint8_t* pszReturnBase64);

long int Util_EncodeToBase64 (const char* pszString, const long int nStrLen, char* pszRetString, const long int nRetStringMaxLen);
long int Util_DecodeFromBase64 (const char* pszBase64String, const long int nB64StrLen, char* pszRetString, const long int nRetStringMaxLen);

int Util_MatrixCode2of5 (const char* pszBarCode, char* pszReturnBuffer, long int nBufferLen);

#ifndef WIN32
void Util_CPU_Init ();
void Util_CPUReduce ();
double Util_CPU_Usage ();
double Util_CPU_UsagebyChild ();
double Util_CPU_GetUsage (bool bChild);

void Util_SetMaxCPU (unsigned long int nMax);
#endif

clock_t Util_GetClock (void);

uint32_t Util_CRC32v2 (unsigned char *block, unsigned int length, uint32_t crc_start);

void UTil_PrintDataToDebug (uint8_t* szSectionData, long int nDataLen);

void Util_PrintBinary (uint8_t chData);

bool Util_IsLittleEndian ();
uint32_t Util_ReverseEndian (uint32_t nData);

char* TUtil_GenerateUID (const char* pszData, uint32_t nDataSize, char* pszReturn, uint32_t nRetLen);
uint64_t TUtil_GenerateAssign (const char* pszData, uint32_t nDataSize, char* pszReturn, uint32_t nRetLen);

bool TUtil_AssignString (string& strData);
bool TUtil_CheckAssignedString (const char* pszData, uint32_t nLength);

double Util_Show_CPU_Usage (bool bChild);

#endif



File: /MikrotikManager\Variant.cpp
//
//  Variant.cpp
//  MikrotikManager
//
//  Created by Gustavo Campos on 6/12/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
/*
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
*/

#include "Variant.h"



Variant::Variant ()
{
    return;
}



Variant::~Variant ()
{
    return;
}



Variant& Variant::operator=(const string &strData)
{
    this->strValues = strData;

    //Counting variables
    nCounter  = 0;
    bool bText = false;
    char chChar;

    for (uint32_t nCount=0; nCount < strData.length(); nCount++)
    {
        chChar = strData.c_str() [nCount];

        if (chChar == '=' && bText == false)
        {
            nCounter++;
            bText = true;
        }
        else if (chChar == ';' && bText == true)
        {
            bText = false;
        }
    }

    //Returning;
    return *this;
}



bool Variant::IsAvailable (const char* pszVariable)
{
    return VariableFinder (pszVariable, this->strReturn, ';', '=');
}



const char* Variant::operator[] (const char* pszVariable)
{
    strError = ""; strError = strError +  "Variable [" + pszVariable + "] does not exist.";

    CHECK (VariableFinder (pszVariable, this->strReturn, ';', '=') == true, strError.c_str());
    
    return strReturn.c_str();
}



int32_t Variant::GetInteger (const char* pszVariable)
{
    int32_t nValue;
    const char* pszValue = (*this) [pszVariable];
    
    nValue = strtod (pszValue, NULL);
    
    return nValue;
}



float Variant::GetFloat (const char* pszVariable)
{
    float nValue;
    const char* pszValue = (*this) [pszVariable];

    nValue = strtof (pszValue, NULL);

    return nValue;
}



bool Variant::VariableFinder (const char* pszField, string& strWork, char chDelimiter, char chDataDv)
{
    int    nCount;
    //char   pszTmpField [UTIL_FIELDLEN + 1];
    int    nType;
    bool   bMatch;
    
    const char* pszSource = this->strValues.c_str();
    uint32_t nSourceLen = (uint32_t) this->strValues.length();
    uint nFildOffSet = 0;
    
    nType  = 0;
    nCount = 0;
    
    bMatch = true;
    
    strWork.clear();
    
    for (nCount = 0; nCount < nSourceLen || *pszSource != '\0'; nCount++)
    {
        if (*pszSource != chDelimiter)
        {
            if (nType == 0)
            {
                if (*pszSource != chDataDv && bMatch == true)
                {
                    if (*pszSource == pszField [nFildOffSet])
                    {
                        nFildOffSet++;
                        bMatch = true;
                    }
                    else
                    {
                        nFildOffSet = 0;
                        bMatch = false;
                    }
                }
                else if (bMatch == true && *pszSource == chDataDv)
                {
                    nType  = 1;
                }

            }
            else if (nType == 1)
            {
                strWork.push_back(*pszSource);
                //pszData [nCount] = *pszSource;
            }
        }
        else if (bMatch == true && nFildOffSet == strlen (pszField))
        {
            return true;
        }
        else
        {
            strWork.clear();
            nFildOffSet = 0;
            nType  = 0;
            bMatch = true;
        }
        
        pszSource++;
    }
    
    return false;
}


uint32_t Variant::GetCounter ()
{
    return nCounter;
}




File: /MikrotikManager\Variant.h
//
//  Variant.h
//  MikrotikManager
//
//  Created by Gustavo Campos on 6/12/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
//
/*
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
*/

#ifndef __MikrotikManager__Variant__
#define __MikrotikManager__Variant__

#include <iostream>
#include <string>
#include <Util.h>
#include <Exception.h>

class Variant
{
private:
    string strValues;
    string strReturn;

    uint32_t nCounter;

    string strError;

    bool VariableFinder (const char* pszField, string& strWork, char chDelimiter, char chDataDv);

protected:
    
public:
    
    Variant ();
    ~Variant ();
    
    Variant& operator= (const string& strData);

    const char* operator[] (const char* pszVariable);
    
    int32_t GetInteger (const char* pszVariable);
    float   GetFloat (const char* pszVariable);
    

    bool IsAvailable (const char* pszVariable);
    
    uint32_t GetCounter ();
};

#endif /* defined(__MikrotikManager__Variant__) */


File: /MikrotikManager\whois.cpp
//
//  whois.cpp
//  MikrotikManager
//
//  Created by Gustavo Campos on 08/07/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
/*
     MIT License
     
     Copyright (c) 2017 Luiz Gustavo de Campos
     
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
*/

#define DEBUG 1
#define _DEBUG 1

#include "whois.h"

//Global cache;
static map<string, struct WhoisCache> mapWhoisCache;


void whois::IfException()
{
    NOTRACE ("Whois, Error handler activated.");
}

whois::whois ()
{
    nCacheTimeout = 0;
}

whois::~whois()
{

}


bool whois::ProcessWhois (const char* pszHost, const char* pszLookup)
{
    objSocket.Close();
    char szName [1024], szValue [1024];

    mapWhoisFields.clear();

    Verify (objSocket.Connect (pszHost, 43, 5) == true, "Error  handling connection", false);

    //TRACE ("Connected...\n");

    string strData = "";

    strData = strData + pszLookup + "\n";

    objSocket.Send (strData.length(), strData.c_str());

    //TRACE ("Data sent...\n");
    static char szLine [1024 + 1];
    try
    {
        while (true)
        {
            objSocket.Gets (szLine, sizeof (szLine), 2);
            //TRACE ("Line: [%s]\n", szLine);

            if (isalpha (szLine [0]) && strchr (szLine, ':'))
            {
                //Do not take this line, it exists for secure reasons
                szLine [strlen (szLine)] = '\0';

                //TRACE ("\n\n %s \n", szLine);

                TUtil_GetToken (':', szLine, szName, sizeof (szName), 0);
                TUtil_GetToken (':', szLine, szValue, sizeof (szValue), 1);

                TUtil_TrimString (szName, sizeof (szName));
                TUtil_TrimString (szValue, sizeof (szValue));

                TUtil_Uppcase (szName);

                mapWhoisFields [(const char*)szName] = (const char*) szValue;

                //TRACE ("(%u) Name [%s] - Value [%s]\n", mapWhoisFields.size(), szName, (*this) [szName]);
            }
        }

    } catch (Exception* pEx)
    {
        //TRACE ("Error: [%s]\n", pEx->GetExceptionMessage());
        objSocket.Close();
    }

    if (mapWhoisFields.size() == 0)
    {
        return false;
    }

    return true;
}





bool whois::Lookup (const char* pszValue, uint16_t nStrLen)
{

    const char* pszDtValue;

    //Processing Cache first of all
    if (nCacheTimeout > 0)
    {
        string strValue;
        map<string, struct WhoisCache>::iterator mapIterator;

        strValue.append (pszValue, nStrLen);

        NOTRACE ("Value: [%s]\n", strValue.c_str());

        mapIterator = mapWhoisCache.find (strValue.c_str());

        if (mapIterator != mapWhoisCache.end())
        {
            NOTRACE (" *** CACHE ***"); //sleep (1);
            mapWhoisFields = mapIterator->second.mapWhoisFields;

            return true;
        }
    }

    //ProcessWhois ("www.google.com", pszValue, objVariables);
    if (ProcessWhois (WHOIS_DEFAULT, pszValue) == false)
    {
        return false;
    }

    ;

    if ((pszDtValue = (*this) ["status"])== NULL && strcmp (pszDtValue, "ALLOCATED") != 0)
    {
        return false;
    }

    if ((pszDtValue = (*this) ["refer"])== NULL)
    {
        return false;
    }

    string strValue = pszDtValue;

    if (ProcessWhois (strValue.c_str(), pszValue) == false)
    {
        return false;
    }

    NOTRACE ("CACHE: [%u]\n", nCacheTimeout);

    if (nCacheTimeout > 0) ProcessCache (pszValue, nStrLen, mapWhoisFields);
    
    return true;
}








const char* whois::operator[] (const char* pszVariable)
{
    //Fist lets check if the Attribute is available

    string str = pszVariable;

    std::transform(str.begin(), str.end(),str.begin(), ::toupper);

    map<string,string>::iterator mapI;

    if ((mapI = mapWhoisFields.find (str.c_str())) == mapWhoisFields.end())
    {
        return NULL;
    }


    return mapI->second.c_str();
}




void whois::SetCacheTimeout (uint32_t nCacheTimeout)
{
    this->nCacheTimeout = nCacheTimeout;
}



void whois::ProcessCache (const char* pszValue, uint16_t nStrLen, map<string,string>& mapWhoisFields)
{
    map<string, struct WhoisCache>::iterator mapInterator;
    time_t timeNow;

    for (mapInterator = mapWhoisCache.begin(); mapInterator != mapWhoisCache.end(); mapInterator++)
    {
        //processing old entries
        timeNow = time (NULL);

        if ((timeNow  - mapInterator->second.tEntrytime) > nCacheTimeout)
        {
            //TRACE ("Cache Erasing: [%s]\n", mapInterator->first.c_str());

            mapWhoisCache.erase(mapInterator);

            continue;
        }
        else if (mapInterator->first.compare (1, nStrLen, pszValue) == 0)
        {
            return;
        }

        //TRACE ("List: [%s]\n", mapInterator->first.c_str());
    }

    //If the loop has retch here, means pszValue must be stored.


    struct WhoisCache stWhoisCache;

    //stWhoisCache.strValue.append(pszValue, nStrLen);
    stWhoisCache.mapWhoisFields = mapWhoisFields;
    stWhoisCache.tEntrytime = time (NULL);

    string strValue;

    strValue.append (pszValue, nStrLen);

    //TRACE ("Adding: [%s]\n", strValue.c_str());

    mapWhoisCache [strValue] = stWhoisCache;
}



uint32_t whois::GetCacheSize ()
{
    return (uint32_t) mapWhoisCache.size();
}


File: /MikrotikManager\whois.h
//
//  whois.h
//  MikrotikManager
//
//  Created by Gustavo Campos on 08/07/14.
//  Copyright (c) 2014 Gustavo Campos. All rights reserved.
//
/*
 
 MIT License
 
 Copyright (c) 2017 Luiz Gustavo de Campos
 
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
 
*/

#ifndef __MikrotikManager__whois__
#define __MikrotikManager__whois__

#include <Exception.h>
#include <iostream>
#include <Socket.h>
#include <Variant.h>
#include <stdio.h>
#include <ctype.h>
#include <map>
#include <string>
#include <algorithm>
#include <time.h>

#endif /* defined(__MikrotikManager__whois__) */


struct WhoisCache
{
    map<string,string> mapWhoisFields;
    time_t tEntrytime;
};



#define WHOIS_DEFAULT  "whois.iana.org"

class whois : Exception
{
protected:

    bool ProcessWhois (const char* pszHost, const char* pszLookup);

    map<string,string> mapWhoisFields;

    void ProcessCache (const char* pszValue, uint16_t nStrLen, map<string,string>& mapWhoisFields);

private:
    Socket  objSocket;
    string strError;

    uint32_t nCacheTimeout;

public:

    whois ();
    ~whois ();

    bool Lookup (const char* pszValue, uint16_t nStrLen);

    const char* operator[] (const char* pszVariable);

    void SetCacheTimeout (uint32_t nCacheTimeout);

    void IfException ();

    static uint32_t GetCacheSize ();

};




File: /MikrotikManager.xcodeproj\project.pbxproj
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 46;
	objects = {

/* Begin PBXBuildFile section */
		670568761F532E0C00A3ACD1 /* Terminal.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 670568741F532E0C00A3ACD1 /* Terminal.cpp */; };
		670568791F532E2100A3ACD1 /* Variant.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 670568771F532E2100A3ACD1 /* Variant.cpp */; };
		6705687C1F532E5800A3ACD1 /* Util.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 6705687A1F532E5800A3ACD1 /* Util.cpp */; };
		6705687F1F532E6F00A3ACD1 /* Exception.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 6705687D1F532E6F00A3ACD1 /* Exception.cpp */; };
		670568821F532E8C00A3ACD1 /* whois.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 670568801F532E8C00A3ACD1 /* whois.cpp */; };
		670568851F532EA900A3ACD1 /* Socket.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 670568831F532EA900A3ACD1 /* Socket.cpp */; };
		67235B9919424CF100733EC0 /* librouteros.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 67235B9819424CF100733EC0 /* librouteros.cpp */; };
		67CC03F219420C3500260E1C /* main.cpp in Sources */ = {isa = PBXBuildFile; fileRef = 67CC03F119420C3500260E1C /* main.cpp */; };
		67CC03F419420C3500260E1C /* MikrotikManager.1 in CopyFiles */ = {isa = PBXBuildFile; fileRef = 67CC03F319420C3500260E1C /* MikrotikManager.1 */; };
/* End PBXBuildFile section */

/* Begin PBXCopyFilesBuildPhase section */
		67CC03EC19420C3500260E1C /* CopyFiles */ = {
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = /usr/share/man/man1;
			dstSubfolderSpec = 0;
			files = (
				67CC03F419420C3500260E1C /* MikrotikManager.1 in CopyFiles */,
			);
			runOnlyForDeploymentPostprocessing = 1;
		};
/* End PBXCopyFilesBuildPhase section */

/* Begin PBXFileReference section */
		0FEC5EAB19461E2300D8EECB /* main.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = main.h; sourceTree = "<group>"; };
		670568741F532E0C00A3ACD1 /* Terminal.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = Terminal.cpp; sourceTree = "<group>"; };
		670568751F532E0C00A3ACD1 /* Terminal.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = Terminal.h; sourceTree = "<group>"; };
		670568771F532E2100A3ACD1 /* Variant.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = Variant.cpp; sourceTree = "<group>"; };
		670568781F532E2100A3ACD1 /* Variant.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = Variant.h; sourceTree = "<group>"; };
		6705687A1F532E5800A3ACD1 /* Util.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = Util.cpp; sourceTree = "<group>"; };
		6705687B1F532E5800A3ACD1 /* Util.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = Util.h; sourceTree = "<group>"; };
		6705687D1F532E6F00A3ACD1 /* Exception.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = Exception.cpp; sourceTree = "<group>"; };
		6705687E1F532E6F00A3ACD1 /* Exception.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = Exception.h; sourceTree = "<group>"; };
		670568801F532E8C00A3ACD1 /* whois.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = whois.cpp; sourceTree = "<group>"; };
		670568811F532E8C00A3ACD1 /* whois.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = whois.h; sourceTree = "<group>"; };
		670568831F532EA900A3ACD1 /* Socket.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = Socket.cpp; sourceTree = "<group>"; };
		670568841F532EA900A3ACD1 /* Socket.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = Socket.h; sourceTree = "<group>"; };
		670568861F53301000A3ACD1 /* LICENCE */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text; path = LICENCE; sourceTree = "<group>"; };
		67235B9619424B9600733EC0 /* librouteros.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = librouteros.h; sourceTree = "<group>"; };
		67235B9819424CF100733EC0 /* librouteros.cpp */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.cpp; path = librouteros.cpp; sourceTree = "<group>"; };
		675DBF7220E4928F00552722 /* README */ = {isa = PBXFileReference; lastKnownFileType = text; path = README; sourceTree = "<group>"; };
		67CC03EE19420C3500260E1C /* MikrotikManager */ = {isa = PBXFileReference; explicitFileType = "compiled.mach-o.executable"; includeInIndex = 0; path = MikrotikManager; sourceTree = BUILT_PRODUCTS_DIR; };
		67CC03F119420C3500260E1C /* main.cpp */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.cpp.cpp; path = main.cpp; sourceTree = "<group>"; };
		67CC03F319420C3500260E1C /* MikrotikManager.1 */ = {isa = PBXFileReference; lastKnownFileType = text.man; path = MikrotikManager.1; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		67CC03EB19420C3500260E1C /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		67235B9419424B0E00733EC0 /* MikrotikLib */ = {
			isa = PBXGroup;
			children = (
				67235B9819424CF100733EC0 /* librouteros.cpp */,
				67235B9619424B9600733EC0 /* librouteros.h */,
			);
			name = MikrotikLib;
			sourceTree = "<group>";
		};
		67CC03E519420C3500260E1C = {
			isa = PBXGroup;
			children = (
				675DBF7220E4928F00552722 /* README */,
				670568861F53301000A3ACD1 /* LICENCE */,
				67CC03F019420C3500260E1C /* MikrotikManager */,
				67CC03EF19420C3500260E1C /* Products */,
			);
			sourceTree = "<group>";
		};
		67CC03EF19420C3500260E1C /* Products */ = {
			isa = PBXGroup;
			children = (
				67CC03EE19420C3500260E1C /* MikrotikManager */,
			);
			name = Products;
			path = /desenv/MikrotikManger/MikrotikManager;
			sourceTree = "<absolute>";
		};
		67CC03F019420C3500260E1C /* MikrotikManager */ = {
			isa = PBXGroup;
			children = (
				670568831F532EA900A3ACD1 /* Socket.cpp */,
				670568841F532EA900A3ACD1 /* Socket.h */,
				670568801F532E8C00A3ACD1 /* whois.cpp */,
				670568811F532E8C00A3ACD1 /* whois.h */,
				6705687D1F532E6F00A3ACD1 /* Exception.cpp */,
				6705687E1F532E6F00A3ACD1 /* Exception.h */,
				6705687A1F532E5800A3ACD1 /* Util.cpp */,
				6705687B1F532E5800A3ACD1 /* Util.h */,
				670568771F532E2100A3ACD1 /* Variant.cpp */,
				670568781F532E2100A3ACD1 /* Variant.h */,
				670568741F532E0C00A3ACD1 /* Terminal.cpp */,
				670568751F532E0C00A3ACD1 /* Terminal.h */,
				67235B9419424B0E00733EC0 /* MikrotikLib */,
				67CC03F119420C3500260E1C /* main.cpp */,
				0FEC5EAB19461E2300D8EECB /* main.h */,
				67CC03F319420C3500260E1C /* MikrotikManager.1 */,
			);
			path = MikrotikManager;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		67CC03ED19420C3500260E1C /* MikrotikManager */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 67CC03F719420C3500260E1C /* Build configuration list for PBXNativeTarget "MikrotikManager" */;
			buildPhases = (
				67CC03EA19420C3500260E1C /* Sources */,
				67CC03EB19420C3500260E1C /* Frameworks */,
				67CC03EC19420C3500260E1C /* CopyFiles */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = MikrotikManager;
			productName = MikrotikManager;
			productReference = 67CC03EE19420C3500260E1C /* MikrotikManager */;
			productType = "com.apple.product-type.tool";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		67CC03E619420C3500260E1C /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastUpgradeCheck = 0940;
				ORGANIZATIONNAME = "Gustavo Campos";
			};
			buildConfigurationList = 67CC03E919420C3500260E1C /* Build configuration list for PBXProject "MikrotikManager" */;
			compatibilityVersion = "Xcode 3.2";
			developmentRegion = English;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
			);
			mainGroup = 67CC03E519420C3500260E1C;
			productRefGroup = 67CC03EF19420C3500260E1C /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				67CC03ED19420C3500260E1C /* MikrotikManager */,
			);
		};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		67CC03EA19420C3500260E1C /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				670568821F532E8C00A3ACD1 /* whois.cpp in Sources */,
				670568761F532E0C00A3ACD1 /* Terminal.cpp in Sources */,
				6705687F1F532E6F00A3ACD1 /* Exception.cpp in Sources */,
				670568791F532E2100A3ACD1 /* Variant.cpp in Sources */,
				670568851F532EA900A3ACD1 /* Socket.cpp in Sources */,
				67235B9919424CF100733EC0 /* librouteros.cpp in Sources */,
				67CC03F219420C3500260E1C /* main.cpp in Sources */,
				6705687C1F532E5800A3ACD1 /* Util.cpp in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		67CC03F519420C3500260E1C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_CXX_LANGUAGE_STANDARD = "c++98";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_ENABLE_OBJC_EXCEPTIONS = YES;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_SYMBOLS_PRIVATE_EXTERN = NO;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				"HEADER_SEARCH_PATHS[arch=*]" = /opt/local/include;
				"LIBRARY_SEARCH_PATHS[arch=*]" = /opt/local/lib;
				MACOSX_DEPLOYMENT_TARGET = 10.9;
				OBJROOT = "$(SYMROOT)";
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = macosx;
				SYMROOT = /desenv/bin;
			};
			name = Debug;
		};
		67CC03F619420C3500260E1C /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_CXX_LANGUAGE_STANDARD = "c++98";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = YES;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_ENABLE_OBJC_EXCEPTIONS = YES;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				"HEADER_SEARCH_PATHS[arch=*]" = /opt/local/include;
				"LIBRARY_SEARCH_PATHS[arch=*]" = /opt/local/lib;
				MACOSX_DEPLOYMENT_TARGET = 10.9;
				OBJROOT = "$(SYMROOT)";
				SDKROOT = macosx;
				SYMROOT = /desenv/bin;
			};
			name = Release;
		};
		67CC03F819420C3500260E1C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++98";
				CLANG_CXX_LIBRARY = "compiler-default";
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include,
					../../Framework,
				);
				OTHER_CPLUSPLUSFLAGS = (
					"-lc",
					"-DDEBUG",
					"-D_DEBUG",
				);
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
			};
			name = Debug;
		};
		67CC03F919420C3500260E1C /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++98";
				CLANG_CXX_LIBRARY = "compiler-default";
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include,
					../../Framework,
				);
				OTHER_CPLUSPLUSFLAGS = "-lc";
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		67CC03E919420C3500260E1C /* Build configuration list for PBXProject "MikrotikManager" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				67CC03F519420C3500260E1C /* Debug */,
				67CC03F619420C3500260E1C /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		67CC03F719420C3500260E1C /* Build configuration list for PBXNativeTarget "MikrotikManager" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				67CC03F819420C3500260E1C /* Debug */,
				67CC03F919420C3500260E1C /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 67CC03E619420C3500260E1C /* Project object */;
}


File: /MikrotikManager.xcodeproj\project.xcworkspace\contents.xcworkspacedata
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:MikrotikManager.xcodeproj">
   </FileRef>
</Workspace>


File: /MikrotikManager.xcodeproj\xcuserdata\gustavocampos.xcuserdatad\xcschemes\MikrotikManager.xcscheme
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "0940"
   version = "1.3">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "67CC03ED19420C3500260E1C"
               BuildableName = "MikrotikManager"
               BlueprintName = "MikrotikManager"
               ReferencedContainer = "container:MikrotikManager.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      shouldUseLaunchSchemeArgsEnv = "NO">
      <Testables>
      </Testables>
      <MacroExpansion>
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "67CC03ED19420C3500260E1C"
            BuildableName = "MikrotikManager"
            BlueprintName = "MikrotikManager"
            ReferencedContainer = "container:MikrotikManager.xcodeproj">
         </BuildableReference>
      </MacroExpansion>
      <CommandLineArguments>
         <CommandLineArgument
            argument = "192.168.88.3"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "admin"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = ""
            isEnabled = "YES">
         </CommandLineArgument>
      </CommandLineArguments>
      <AdditionalOptions>
      </AdditionalOptions>
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "67CC03ED19420C3500260E1C"
            BuildableName = "MikrotikManager"
            BlueprintName = "MikrotikManager"
            ReferencedContainer = "container:MikrotikManager.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
      <CommandLineArguments>
         <CommandLineArgument
            argument = "192.168.88.1"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "8728"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "admin"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "163841"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "250"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "500"
            isEnabled = "YES">
         </CommandLineArgument>
         <CommandLineArgument
            argument = "wlan1_WiFi"
            isEnabled = "YES">
         </CommandLineArgument>
      </CommandLineArguments>
      <AdditionalOptions>
      </AdditionalOptions>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Release"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "67CC03ED19420C3500260E1C"
            BuildableName = "MikrotikManager"
            BlueprintName = "MikrotikManager"
            ReferencedContainer = "container:MikrotikManager.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>


File: /MikrotikManager.xcodeproj\xcuserdata\gustavocampos.xcuserdatad\xcschemes\xcschememanagement.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>SchemeUserState</key>
	<dict>
		<key>MikrotikManager.xcscheme</key>
		<dict>
			<key>orderHint</key>
			<integer>0</integer>
		</dict>
	</dict>
	<key>SuppressBuildableAutocreation</key>
	<dict>
		<key>67CC03ED19420C3500260E1C</key>
		<dict>
			<key>primary</key>
			<true/>
		</dict>
	</dict>
</dict>
</plist>


File: /README
Compiling:

g++ -o MikrotikManager -I. -I /opt/local/include -L /opt/local/lib/ -lssl *.cpp

Executing example:

./MikrotikManager 10.10.0.1 "" "<admin user>" "<passwd>" <TX in K> <RX in K> "<interface>"

Pooling every 5 seconds.

Written in C++98 for compatibility reasons.




