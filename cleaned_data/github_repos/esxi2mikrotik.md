# Repository Information
Name: esxi2mikrotik

# Directory Structure
Directory structure:
└── github_repos/esxi2mikrotik/
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
    │   │       ├── pack-79dd14b07a753e0a0ffc899aa4a0a95917baaac9.idx
    │   │       └── pack-79dd14b07a753e0a0ffc899aa4a0a95917baaac9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── LICENSE
    ├── mvnvm.properties
    ├── pom.xml
    ├── README.md
    └── src/
        └── main/
            ├── java/
            │   └── com/
            │       └── github/
            │           └── nmichas/
            │               └── esxi2mikrotik/
            │                   ├── App.java
            │                   ├── commander/
            │                   │   ├── ESXiCommander.java
            │                   │   ├── MikrotikCommander.java
            │                   │   └── SSHCommander.java
            │                   └── dto/
            │                       ├── CredentialsDTO.java
            │                       └── TargetVMDTO.java
            └── resources/
                └── log4j.properties


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
	url = https://github.com/NMichas/esxi2mikrotik.git
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
0000000000000000000000000000000000000000 4ac4b0d4496adc45b965f8588f68ed57b4778a04 vivek-dodia <vivek.dodia@icloud.com> 1738606430 -0500	clone: from https://github.com/NMichas/esxi2mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 4ac4b0d4496adc45b965f8588f68ed57b4778a04 vivek-dodia <vivek.dodia@icloud.com> 1738606430 -0500	clone: from https://github.com/NMichas/esxi2mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 4ac4b0d4496adc45b965f8588f68ed57b4778a04 vivek-dodia <vivek.dodia@icloud.com> 1738606430 -0500	clone: from https://github.com/NMichas/esxi2mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4ac4b0d4496adc45b965f8588f68ed57b4778a04 refs/remotes/origin/master


File: /.git\refs\heads\master
4ac4b0d4496adc45b965f8588f68ed57b4778a04


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
target


File: /LICENSE
MIT License

Copyright (c) 2017 Nassos A. Michas

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


File: /mvnvm.properties
3.3.9


File: /pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.github.nmichas</groupId>
  <artifactId>esxi2mikrotik</artifactId>
  <version>1.0.0-SNAPSHOT</version>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.6.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>1.6.0</version>
        <configuration>
          <mainClass>com.github.nmichas.esxi2mikrotik.App</mainClass>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>3.0.0</version>
        <configuration>
          <transformers>
            <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
              <mainClass>com.github.nmichas.esxi2mikrotik.App</mainClass>
            </transformer>
          </transformers>
        </configuration>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>

  <dependencies>
    <dependency>
      <groupId>com.toastcoders</groupId>
      <artifactId>yavijava</artifactId>
      <version>6.0.05</version>
    </dependency>
    <dependency>
      <groupId>me.legrange</groupId>
      <artifactId>mikrotik</artifactId>
      <version>3.0.3</version>
    </dependency>
    <dependency>
      <groupId>commons-cli</groupId>
      <artifactId>commons-cli</artifactId>
      <version>1.4</version>
    </dependency>
    <dependency>
      <groupId>com.jcraft</groupId>
      <artifactId>jsch</artifactId>
      <version>0.1.54</version>
    </dependency>
  </dependencies>

</project>

File: /README.md
![vCenter](http://images.locanto.net/vmware-online-training/gallery_2521531850.jpg)
![mikrotik](http://www.observium.org/vendor_images/mikrotik.png)

# ESXi2Mikrotik

This is a handy little utility created to speedup the workflow on
my home ESXi/vCenter lab. If you have a similarly operated lab it may
save you some time while testing multiple VMs.

## Prerequisites
* Tested on vCenter 6.5.0
* Tested on Mikrotik 6.39.2
* VM image: Ubuntu 16.04.2 server 64bit

## Usual test-workflow
1. Create a VM in ESXi/vCenter (usually, cloning a template with a
generic image)
2. Find the VM's MAC address on ESXi/vCenter console.
3. Create a DHCP entry in Mikrotik for the new VM
4. Create a DNS entry in Mikrotik for the new VM
5. Modify VM's /etc/hostname
6. Modify VM's /etc/hosts
7. Reboot the VM
8. Check the VM is accessible on the new IP address

This script automates all steps but #1. #1 could be easily automated
too, however providing VM-level configuration options would be far
outside the scope of this script.

## Usage

### Running

Usage instructions:

    java -jar target/esxi2mikrotik-1.0.0-SNAPSHOT.jar

Example:
```
java -jar esxi2mikrotik-1.0.0-SNAPSHOT.jar \
    -eh vcenter.domain \
    -eu admin@vcenter.domain \
    -ep secret \
    -mh mikrotik.domain \
    -mu admin \
    -mp secret2 \
    -vn MyTestVM \
    -vh my-test-vm.domain \
    -vi 1.2.3.4 \
    -vu superuser \
    -vp secret3
```

### Parameters
```
usage: help
 -eh,--esxiHostname <arg>       ESXi/vCenter hostname
 -ep,--esxiPassword <arg>       ESXi/vCenter password
 -eu,--esxiUsername <arg>       ESXi/vCenter username
 -mh,--mikrotikHostname <arg>   Mikrotik hostname
 -mp,--mikrotikPassword <arg>   Mikrotik password
 -mu,--mikrotikUsername <arg>   Mikrotik username
 -vh,--vmHostname <arg>         The hostname to be assigned to the VM
 -vi,--vmIP <arg>               The new IP for the VM
 -vn,--vmName <arg>             The name of the VM in ESXi/vCenter
 -vp,--vmPassword <arg>         The password to connect to the VM via SSH
 -vu,--vmUsername <arg>         The username to connect to the VM via SSH
```



## Development
### Building
To build this script you need Java 1.8.x, Maven 3.2.x, an Internet
connection and running the following command:

    mvn clean install

### Testing while building
```
mvn install exec:java \-Dexec.args="\
    -eh vcenter.domain \
    -eu admin@vcenter.domain \
    -ep secret \
    -mh mikrotik.domain \
    -mu admin \
    -mp secret2 \
    -vn MyTestVM \
    -vh my-test-vm.domain \
    -vi 1.2.3.4 \
    -vu superuser \
    -vp secret3"
```


File: /src\main\java\com\github\nmichas\esxi2mikrotik\App.java
package com.github.nmichas.esxi2mikrotik;


import com.github.nmichas.esxi2mikrotik.commander.ESXiCommander;
import com.github.nmichas.esxi2mikrotik.commander.MikrotikCommander;
import com.github.nmichas.esxi2mikrotik.commander.SSHCommander;
import com.github.nmichas.esxi2mikrotik.dto.CredentialsDTO;
import com.github.nmichas.esxi2mikrotik.dto.TargetVMDTO;
import com.jcraft.jsch.JSchException;
import me.legrange.mikrotik.MikrotikApiException;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.net.InetAddress;
import java.text.MessageFormat;
import java.time.Instant;

public class App {

  private static final Logger LOG = Logger.getLogger(App.class);

  /**
   * CLI options
   */
  private static Options cliOptions;

  private CredentialsDTO esxiCredentials;
  private CredentialsDTO mikrotikCredentials;
  private TargetVMDTO targetVMDTO;

  static {
    /** Setup CLI options */
    cliOptions = new Options();
    cliOptions.addOption(
        Option.builder("eh").longOpt("esxiHostname").required().hasArg().numberOfArgs(1)
            .desc("ESXi/vCenter hostname").build());
    cliOptions.addOption(
        Option.builder("eu").longOpt("esxiUsername").required().hasArg().numberOfArgs(1)
            .desc("ESXi/vCenter username").build());
    cliOptions.addOption(
        Option.builder("ep").longOpt("esxiPassword").required().hasArg().numberOfArgs(1)
            .desc("ESXi/vCenter password").build());

    cliOptions.addOption(
        Option.builder("mh").longOpt("mikrotikHostname").required().hasArg()
            .numberOfArgs(1)
            .desc("Mikrotik hostname").build());
    cliOptions.addOption(
        Option.builder("mu").longOpt("mikrotikUsername").required().hasArg()
            .numberOfArgs(1)
            .desc("Mikrotik username").build());
    cliOptions.addOption(
        Option.builder("mp").longOpt("mikrotikPassword").required().hasArg()
            .numberOfArgs(1)
            .desc("Mikrotik password").build());

    cliOptions.addOption(
        Option.builder("vn").longOpt("vmName").required().hasArg()
            .numberOfArgs(1)
            .desc("The name of the VM in ESXi/vCenter").build());
    cliOptions.addOption(
        Option.builder("vh").longOpt("vmHostname").required().hasArg()
            .numberOfArgs(1)
            .desc("The hostname to be assigned to the VM").build());
    cliOptions.addOption(
        Option.builder("vi").longOpt("vmIP").required().hasArg()
            .numberOfArgs(1)
            .desc("The new IP for the VM").build());
    cliOptions.addOption(
        Option.builder("vu").longOpt("vmUsername").required().hasArg()
            .numberOfArgs(1)
            .desc("The username to connect to the VM via SSH").build());
    cliOptions.addOption(
        Option.builder("vp").longOpt("vmPassword").required().hasArg()
            .numberOfArgs(1)
            .desc("The password to connect to the VM via SSH").build());

  }

  public App(CredentialsDTO esxiCredentials, CredentialsDTO mikrotikCredentials,
      TargetVMDTO targetVMDTO) {
    this.esxiCredentials = esxiCredentials;
    this.mikrotikCredentials = mikrotikCredentials;
    this.targetVMDTO = targetVMDTO;
  }

  private static void cliHelp() {
    HelpFormatter formatter = new HelpFormatter();
    formatter.printHelp("help", cliOptions);
  }

  public void process()
      throws IOException, MikrotikApiException, JSchException, InterruptedException {
    /** Create commander instances of underlying resources */
    ESXiCommander esxiCommander = new ESXiCommander(esxiCredentials);
    MikrotikCommander mikrotikCommander = new MikrotikCommander(mikrotikCredentials);
    SSHCommander sshCommander = new SSHCommander(targetVMDTO);

    /** Find the MAC address of the VM */
    LOG.info("Finding the MAC address of the VM.");
    String macAddress = esxiCommander.getMACAddress(targetVMDTO.getName());

    /** Find the current IP address of the VM */
    LOG.info("Finding the current IP address of the VM.");
    String currentIPAddress = esxiCommander.getIpAddress(targetVMDTO.getName());

    /** Create a DHCP entry */
    LOG.info(MessageFormat.format("Creating a DHCP entry with IP {0} for MAC address {1}.",
        new Object[]{targetVMDTO.getNewIp(), macAddress}));
    mikrotikCommander.createDHCPEntry(macAddress, targetVMDTO.getNewIp(), targetVMDTO.getName());

    /** Create a DNS entry */
    LOG.info(MessageFormat.format("Creating a DNS entry with IP {0} for hostname {1}.",
        new Object[]{targetVMDTO.getNewIp(), targetVMDTO.getHostname()}));
    mikrotikCommander.createDNSEntry(targetVMDTO.getNewIp(), targetVMDTO.getHostname(), targetVMDTO.getName());

    /** Update the linux VM */
    LOG.info("Updating /etc/hostname");
    sshCommander.updateHostname(currentIPAddress);
    LOG.info("Updating /etc/hosts");
    sshCommander.updateHosts(currentIPAddress);

    /** Reboot the VM to pickup new IP address from DHCP */
    LOG.info(MessageFormat.format("Rebooting {0}.", targetVMDTO.getHostname()));
    sshCommander.reboot(currentIPAddress);

    /** Wait for the VM to be back alive with its new ip address */
    LOG.info(MessageFormat.format("Waiting for the VM to be back online with is new IP adddress {0}.",
        targetVMDTO.getNewIp()));
    InetAddress inetAddress = InetAddress.getByName(targetVMDTO.getNewIp());
    long startTimer = Instant.now().toEpochMilli();
    while (Instant.now().toEpochMilli() - startTimer < 60*1000) {
      try {
        if (inetAddress.isReachable(1000)) {
          break;
        }
      } catch (Exception e) {

      }
      Thread.sleep(1000);
    }
  }

  public static void main(String[] args) throws Exception {
    /** Show help if no arguments passed */
    if (args.length == 0) {
      cliHelp();
      System.exit(0);
    }

    /** Parse cli and create App instance */
    CommandLine cmd = new DefaultParser().parse(cliOptions, args);

    App app = new App(
        new CredentialsDTO(cmd.getOptionValue("eh"), cmd.getOptionValue("eu"),
            cmd.getOptionValue("ep")),
        new CredentialsDTO(cmd.getOptionValue("mh"), cmd.getOptionValue("mu"),
            cmd.getOptionValue("mp")),
        new TargetVMDTO(cmd.getOptionValue("vh"), cmd.getOptionValue("vu"),
            cmd.getOptionValue("vp"), cmd.getOptionValue("vn"), cmd.getOptionValue("vi")));

    /** Start processing */
    app.process();

    LOG.info("ESXi2Mikrotik terminated.");
  }
}


File: /src\main\java\com\github\nmichas\esxi2mikrotik\commander\ESXiCommander.java
package com.github.nmichas.esxi2mikrotik.commander;

import com.github.nmichas.esxi2mikrotik.dto.CredentialsDTO;
import com.vmware.vim25.GuestNicInfo;
import com.vmware.vim25.mo.InventoryNavigator;
import com.vmware.vim25.mo.ServiceInstance;
import com.vmware.vim25.mo.VirtualMachine;
import org.apache.log4j.Logger;

import java.net.MalformedURLException;
import java.net.URL;
import java.rmi.RemoteException;
import java.text.MessageFormat;

public class ESXiCommander {

  private static final Logger LOG = Logger.getLogger(MikrotikCommander.class);
  private CredentialsDTO credentials;

  public ESXiCommander(CredentialsDTO credentials) {
    LOG.debug(MessageFormat
        .format("Initialising ESXiCommander with credentials: {0}", credentials.toString()));
    this.credentials = credentials;
  }

  private ServiceInstance login() throws MalformedURLException, RemoteException {
    return new ServiceInstance(new URL("https://" + credentials.getHostname() + "/sdk"),
        credentials.getUsername(), credentials.getPassword(), true);
  }

  private void logout(ServiceInstance esxi) {
    esxi.getServerConnection().logout();
  }

  private VirtualMachine getVM(ServiceInstance esxi, String vmName) throws RemoteException {
    return (VirtualMachine) new InventoryNavigator(esxi.getRootFolder())
        .searchManagedEntity("VirtualMachine", vmName);
  }

  public String getMACAddress(String vmName) throws MalformedURLException, RemoteException {
    /** Login to ESXi/vCenter. */
    ServiceInstance esxi = login();

    /** Get the VM */
    final VirtualMachine vm = getVM(esxi, vmName);

    /** Find network info. Currently, only first NIC/IPv4 is scanned/supported. */
    final GuestNicInfo net = vm.getGuest().getNet()[0];

    /** Logout from ESXi/vCenter. */
    logout(esxi);

    return net.getMacAddress();
  }

  public String getIpAddress(String vmName) throws MalformedURLException, RemoteException {
    /** Login to ESXi/vCenter. */
    ServiceInstance esxi = login();

    /** Get the VM */
    final VirtualMachine vm = getVM(esxi, vmName);

    /** Find network info. Currently, only first NIC/IPv4 is scanned/supported. */
    final GuestNicInfo net = vm.getGuest().getNet()[0];

    /** Logout from ESXi/vCenter. */
    logout(esxi);

    return net.getIpAddress()[0];
  }

}


File: /src\main\java\com\github\nmichas\esxi2mikrotik\commander\MikrotikCommander.java
package com.github.nmichas.esxi2mikrotik.commander;

import com.github.nmichas.esxi2mikrotik.dto.CredentialsDTO;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;
import org.apache.log4j.Logger;

import java.text.MessageFormat;

public class MikrotikCommander {

  private static final Logger LOG = Logger.getLogger(MikrotikCommander.class);
  private CredentialsDTO credentials;

  public MikrotikCommander(CredentialsDTO credentials) {
    LOG.debug(MessageFormat
        .format("Initialising MikrotikCommander with credentials: {0}", credentials.toString()));
    this.credentials = credentials;
  }

  public ApiConnection getConnection() throws MikrotikApiException {
    return ApiConnection.connect(credentials.getHostname());
  }

  public void createDHCPEntry(String macAddress, String ipAddress, String comment) throws MikrotikApiException {
    ApiConnection mikrotik = getConnection();
    mikrotik.login(credentials.getUsername(), credentials.getPassword());

    String cmd = "/ip/dhcp-server/lease/add address=" + ipAddress +
        " mac-address=" + macAddress +
        " comment=" + comment;
    LOG.debug(MessageFormat.format("Executing Mikrotik command: {0}.", cmd));
    mikrotik.execute(cmd.toString());

    mikrotik.close();
  }

  public void createDNSEntry(String ipAddress, String hostname, String comment) throws MikrotikApiException {
    ApiConnection mikrotik = getConnection();
    mikrotik.login(credentials.getUsername(), credentials.getPassword());

    String cmd = "/ip/dns/static/add address=" + ipAddress +
        " name=" + hostname +
        " comment=" + comment;
    LOG.info(MessageFormat.format("Executing Mikrotik command: {0}.", cmd));
    mikrotik.execute(cmd.toString());

    mikrotik.close();
  }
}


File: /src\main\java\com\github\nmichas\esxi2mikrotik\commander\SSHCommander.java
package com.github.nmichas.esxi2mikrotik.commander;

import com.github.nmichas.esxi2mikrotik.dto.TargetVMDTO;
import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import org.apache.log4j.Logger;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.text.MessageFormat;

public class SSHCommander {
  private static final Logger LOG = Logger.getLogger(SSHCommander.class);
  private TargetVMDTO targetVMDTO;

  private Session login(String ipAddress) throws JSchException {
    return new JSch().getSession(targetVMDTO.getUsername(), ipAddress, 22);
  }

  private void logout(Session ssh) {
    ssh.disconnect();
  }

  public SSHCommander(TargetVMDTO targetVMDTO) {
    LOG.debug(MessageFormat
        .format("Initialising SSHCommander with credentials: {0}", targetVMDTO.toString()));
    this.targetVMDTO = targetVMDTO;
  }

  public void updateHostname(String ipAddress) throws JSchException, IOException {
    Session ssh = login(ipAddress);
    java.util.Properties config = new java.util.Properties();
    config.put("StrictHostKeyChecking", "no");
    ssh.setConfig(config);
    ssh.setPassword(targetVMDTO.getPassword());
    ssh.connect();

    Channel channel = ssh.openChannel("exec");
    ((ChannelExec)channel).setCommand("sudo -S -p '' sed -i 's/.*/" + targetVMDTO.getHostname() + "/g' /etc/hostname");
    InputStream in=channel.getInputStream();
    OutputStream out=channel.getOutputStream();
    ((ChannelExec)channel).setErrStream(System.err);
    channel.connect();
    out.write((targetVMDTO.getPassword() + "\n").getBytes());
    out.flush();

    //TODO refactor channel read-back...
    byte[] tmp=new byte[1024];
    while(true){
      while(in.available()>0){
        int i=in.read(tmp, 0, 1024);
        if(i<0)break;
        System.out.print(new String(tmp, 0, i));
      }
      if(channel.isClosed()){
        break;
      }
      try{Thread.sleep(1000);}catch(Exception ee){}
    }
    channel.disconnect();

    logout(ssh);
  }

  public void updateHosts(String ipAddress) throws JSchException, IOException {
    Session ssh = login(ipAddress);
    java.util.Properties config = new java.util.Properties();
    config.put("StrictHostKeyChecking", "no");
    ssh.setConfig(config);
    ssh.setPassword(targetVMDTO.getPassword());
    ssh.connect();

    Channel channel = ssh.openChannel("exec");
    ((ChannelExec)channel).setCommand("sudo -S -p '' sed -i 's/127.0.1.1.*/127.0.1.1\\t'\"" + targetVMDTO.getHostname() + "\"'/g' /etc/hosts");
    InputStream in=channel.getInputStream();
    OutputStream out=channel.getOutputStream();
    ((ChannelExec)channel).setErrStream(System.err);
    channel.connect();
    out.write((targetVMDTO.getPassword() + "\n").getBytes());
    out.flush();

    //TODO refactor channel read-back...
    byte[] tmp=new byte[1024];
    while(true){
      while(in.available()>0){
        int i=in.read(tmp, 0, 1024);
        if(i<0)break;
        System.out.print(new String(tmp, 0, i));
      }
      if(channel.isClosed()){
        break;
      }
      try{Thread.sleep(1000);}catch(Exception ee){}
    }
    channel.disconnect();

    logout(ssh);
  }

  public void reboot(String ipAddress) throws JSchException, IOException {
    Session ssh = login(ipAddress);
    java.util.Properties config = new java.util.Properties();
    config.put("StrictHostKeyChecking", "no");
    ssh.setConfig(config);
    ssh.setPassword(targetVMDTO.getPassword());
    ssh.connect();

    Channel channel = ssh.openChannel("exec");
    ((ChannelExec)channel).setCommand("sudo -S -p '' reboot");
    InputStream in=channel.getInputStream();
    OutputStream out=channel.getOutputStream();
    ((ChannelExec)channel).setErrStream(System.err);
    channel.connect();
    out.write((targetVMDTO.getPassword() + "\n").getBytes());
    out.flush();

    //TODO refactor channel read-back...
    byte[] tmp=new byte[1024];
    while(true){
      while(in.available()>0){
        int i=in.read(tmp, 0, 1024);
        if(i<0)break;
        System.out.print(new String(tmp, 0, i));
      }
      if(channel.isClosed()){
        break;
      }
      try{Thread.sleep(1000);}catch(Exception ee){}
    }
    channel.disconnect();

    logout(ssh);
  }


}


File: /src\main\java\com\github\nmichas\esxi2mikrotik\dto\CredentialsDTO.java
package com.github.nmichas.esxi2mikrotik.dto;

public class CredentialsDTO {
  private String hostname;
  private String username;
  private String password;

  public CredentialsDTO(String hostname, String username, String password) {
    this.hostname = hostname;
    this.username = username;
    this.password = password;
  }

  public CredentialsDTO(String hostname, String username) {
    this(hostname, username, null);
  }

  public String getHostname() {
    return hostname;
  }

  public void setHostname(String hostname) {
    this.hostname = hostname;
  }

  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }

  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }

  @Override
  public String toString() {
    return "CredentialsDTO{" +
        "hostname='" + hostname + '\'' +
        ", username='" + username + '\'' +
        ", password='" + password + '\'' +
        '}';
  }
}


File: /src\main\java\com\github\nmichas\esxi2mikrotik\dto\TargetVMDTO.java
package com.github.nmichas.esxi2mikrotik.dto;

public class TargetVMDTO extends CredentialsDTO {

  /**
   * The name of the VM in ESXi/vCenter
   */
  private String name;

  /**
   * The new IP for this VM.
   */
  private String newIp;

  public TargetVMDTO(String hostname, String username, String password, String name, String newIp) {
    super(hostname, username, password);
    this.name = name;
    this.newIp = newIp;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getNewIp() {
    return newIp;
  }

  public void setNewIp(String newIp) {
    this.newIp = newIp;
  }

}


File: /src\main\resources\log4j.properties
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target=System.out
log4j.appender.stdout.layout=org.apache.log4j.SimpleLayout
log4j.rootLogger=info, stdout

