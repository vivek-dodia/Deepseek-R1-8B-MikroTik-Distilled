# Repository Information
Name: mikrotik-mtcna

# Directory Structure
Directory structure:
└── github_repos/mikrotik-mtcna/
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
    │   │       ├── pack-31b5cef306e7e43c1641b7693d3bc03ac8462d60.idx
    │   │       └── pack-31b5cef306e7e43c1641b7693d3bc03ac8462d60.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitbook/
    │   └── assets/
    ├── changelog.md
    ├── m1-intro.md
    ├── m2-routing.md
    ├── m3-bridging.md
    ├── m4-wireless.md
    ├── m5-network-management.md
    ├── m6-firewall.md
    ├── m7-qos.md
    ├── m8-tunnels.md
    ├── pics/
    ├── README.md
    └── SUMMARY.md


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
	url = https://github.com/translaster/mikrotik-mtcna.git
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
0000000000000000000000000000000000000000 5a841e942ba0777fef1a9c6d9d609e5793e68943 vivek-dodia <vivek.dodia@icloud.com> 1738605955 -0500	clone: from https://github.com/translaster/mikrotik-mtcna.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5a841e942ba0777fef1a9c6d9d609e5793e68943 vivek-dodia <vivek.dodia@icloud.com> 1738605955 -0500	clone: from https://github.com/translaster/mikrotik-mtcna.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5a841e942ba0777fef1a9c6d9d609e5793e68943 vivek-dodia <vivek.dodia@icloud.com> 1738605955 -0500	clone: from https://github.com/translaster/mikrotik-mtcna.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5a841e942ba0777fef1a9c6d9d609e5793e68943 refs/remotes/origin/master


File: /.git\refs\heads\master
5a841e942ba0777fef1a9c6d9d609e5793e68943


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /changelog.md
# Change Log

## 14.01.20

Закончил перевод М4, немного начал М5

## 27.08.19

Закончил перевод М2

Да и перевел М3

## 26.08.2019

Переведен М1

## 1.0.0 - 2019-08-22

### Changed

* Залил все 8 модулей


File: /m1-intro.md
# M1 Intro

## **Для чего нужен курс MTCNA?**

* Знакомство с RouterOS и продуктами RouterBoard.
* Вы получите представление, что можно сделать с помощью RouterOS и продуктов RouterBOARD
* Всё это даст Вам прочную базу и важные знания, которые помогут Вам в работе.

## Цели данного курса:

После изучения курса Вы:

* Будете знакомы с возможностями RouterOS и RouterBoard
* Сможете настраивать, управлять, проводить основную отладку роутеров MikroTik
* Сможете предоставлять основные сервисы клиентам

## Введение

### **Модуль 1**

#### **RouterOS и RouterBoard**

Что такое RouterOS?

* MikroTik RouterOS - это операционная система, на которой работают все продукты MikroTik RouterBOARD.
* Содержит все необходимые возможности для провайдеров и сетевых администраторов: роутинг, фаервол, контроль скорости доступа, резервирование канала, точка доступа, хотспот, VPN сервер и другие.
* RouterOS - операционная система с простым и удобым интерфейсом. Она основана на ядре Linux и её установка не составит сложностей и не займёт много времени.

![](.gitbook/assets/0.jpeg)

Что такое RouterBOARD?

* Семейство оборудования, созданное MikroTik. Оно покрывает нужды пользователей по всему миру.
* Все RouterBOARDы работают на RouterOS.

![](.gitbook/assets/1%20%284%29.jpeg)

routerboard.com

### Готовые решения

* Это оборудование поставляется в собранном виде, в корпусе и с блоком питания
* Готово к использованию и преднастроенно для большинства конфигураций
* Всё, что нужно сделать - включить его в розетку и подключить к интернету или корпроративной сети.

#### RouterBOARD \(только платы\)

* Небольшие материнские платы, которые продаются "как есть". Вам нужно покупать для них корпус, блок питания и интерфейсы по отдельности. Подходят для сбора индивидуальной конфигурации, т.к. предлагается огромное количество вариантов кастомизации.

#### Корпуса

* Внутренние и внешние корпуса для Ваших RouterBOARDs.

Выбирайте, исходя из:

* места размещения роутера
* модели RouterBOARD
* типов подключения \(USB, антенны и т.д.\).

#### Интерфейсы

* Модули Ethernet, SFP или беспроводные интерфейсы, чтобы расширить функционал RouterBOARD и компьютеров с RouterOS.
* Опять же, выбирайте, отталкиваясь от Ваших нужд и задач.

#### Аксессуары

* Продукты, которые сделаны для MikroTik - блоки питания, крепежи, антенны и PoE инжекторы.

#### MFM

* С программой MFM \(Made for Mikrotik\), сторонние организации предоставляют возможности улучшить Ваш роутер

Почему готовые решения?

* Подходят под большинство запросов
* Некоторые возможности расширения
* Фиксированная конфигурация
* Простое, но надёжное решение для многих задач.

#### Готовые решения. Примеры:

**RB951G-2HnD**

\*\*\*\*![](.gitbook/assets/2%20%282%29.jpeg)\*\*\*\*

* Подходит для дома и малого офиса
* 5 Gig ports
* Встроенный Wi-Fi \(2,4GHz\)
* Лицензия: level 4

**SXT Sixpack**

![](.gitbook/assets/3%20%282%29.jpeg)

\(1 OmniTIK U-5HnD with 5 SXT-5HPnD\)

* Good for WISP or company with branch offices
* 5 100Mbps ports \(OmniTik\)
* 5GHz 802.11a/n radios
* Can cover 5Km between central and satellite sites

**CCR1036-12G-4S Cloud Router**

![](.gitbook/assets/image%20%288%29.png)

_**Флагманская модель**_

* Роутер для провайдеров или корпоративных сетей
* Rack mount корпус высотой в 1 юнит
* 12 Gig портов
* Serial console, USB и цветной сенсорный экран
* Изначально 4G RAM, расширяется с помощью модулей SO-DIMM RAM

На заметку:

* Название соответствует возможностям роутера. Примеры:
  * CCR : Cloud Core Router
  * RB : RouterBoard
  * 2, 5 : 2,4GHZ or 5GHz wifi radio
  * H : High powered radio
  * S : SFP
  * U : USB
  * i : Injector
  * G : Gigabit ethernet

Зачем создавать свой собственный маршрутизатор?

* Сможете адресовать большое разнообразие потребностей
* Множество дополнительных опций/расширений
* Настраиваемая конфигурация
* Может быть встроено в оборудование или шкаф клиента
* Более полное решение для конкретных потребностей

Собственный роутер. Пример:

#### **Гибкое CPE**

![](.gitbook/assets/4%20%282%29.jpeg)

* **RB411UAHR**
  * – 1 порт 100Mbps
  * – 1 2,4GHz radio \(b/g\)
  * – Лицензия Level 4
* Добавим блок питания
* Добавим корпус 3rd ****party
* Добавим miniPCIe-3g-модем

#### **Мощный хотспот**

* Запустите

![](.gitbook/assets/image%20%283%29.png)

![](.gitbook/assets/image%20%2811%29.png)

* **RB493G**
  * 9 gig портов
  * лицензия Level 5
* Добавим электропитание или модуль PoE
* Добавим R2SHPn \(радиокарта 2,4GHz\)
* Добавим R5SHPn \(радиокарта 5GHz\)
* Добавим стороннее приложение
* Добавим карту microSD

## **Первоначальный доступ на роутер**

### Через интернет-браузер

* "Интуитивно понятный" способ доступа к роутеру

Доступ через интернет-браузер

* Подключитесь к роутеру патчкордом
* Запустите браузер
* Введите IP-адрес роутера
* Если потребуется, введите данные для входа. По умолчанию пользователь "admin", пароля нет



* Вы увидите:

![](.gitbook/assets/6.jpeg)

### WinBox и MAC-Winbox

* WinBox – проприеритарный интерфейс MikroTik для настройки RouterOS.
* Доступен для загрузке на сайте mikrotik.com/download либо непосредственно с роутера.
* Использует IP \(3 уровень OSI\) или MAC \(2 уровень OSI\) для доступа к роутеру.
* Находясь в веб-интерфейсе, нажмите “logout”
* Нажмите на “Winbox”
* Сохраните “winbox.exe”

![](.gitbook/assets/7%20%283%29.jpeg)

* Запустите WinBox.
* Введите IP 192.168.88.1 и нажмите "Connect".
* Вы увидите окно первого запуска

![](.gitbook/assets/image%20%289%29.png)

Меню WinBox’а

* Потратьте 5 минут, чтобы пройтись по меню
* Обратите особое внимание на:
  * – IP -&gt; Addresses
  * – IP -&gt; Routes
  * – System -&gt; SNTP
  * – System -&gt; Packages
  * – System -&gt; Routerboard

### Console port

![](.gitbook/assets/image%20%281%29.png)

* Обязательно изучите статью: [http://wiki.mikrotik.com/wiki/Serial\_Port\_Usage](http://wiki.mikrotik.com/wiki/Serial_Port_Usage)
* Необходим для подключения к роутеру через нуль-модемный кабель \(RS-232 port\).
  * Значение по-умолчанию 115200 бит/с, данные 8 bit, 1 stop bit, no parity \(отсутствие четности\)

### SSH и Telnet

* Стандартные IP утилиты для доступа к роутеру
* Telnet соединения не шифруются
  * – Доступно на большинстве ОС
  * – Незащищено!!
* SSH соединения зашифрованы
  * – Безопасно!!
  * – Много Open Source утилит доступно, например, PuTTY \([http://www.putty.org/](http://www.putty.org/)\)

### CLI

* Сокращение от **C**ommand **L**ine **I**nterface
* Мы его видим, когда подключаемся через консоль, SSH, Telnet, или нажимаем New Terminal \(в Winbox\)
* Если планируете использовать скрипты и автоматизацию – обязательно к изучению.

## **Первоначальная конфигурация \(Internet access\)**

### Basic или blank конфигурация?

* После распаковки роутера у вас стандартная конфигурация, но её может и не быть \(зависит от модели\)
* Можно отказаться от применения стандартной конфигурации
* Узнать, что настроено по умолчанию на вашем роутере можно по ссылке:
  * [http://wiki.mikrotik.com/wiki/Manual:Default\_Configurations](http://wiki.mikrotik.com/wiki/Manual:Default_Configurations)

### Базовая конфигурация

* В зависимости от модели, будет стандартная конфигурация, которая может включать в себя:

  * WAN порт
  * LAN порт\(ы\)
  * DHCP клиент \(WAN\) и сервер \(LAN\)
  * Базовая настройка фаервола
  * Правило NAT
  * Стандартный LAN IP адрес

* Подключаясь впервые по Winbox'у, нажмите “OK”
* Роутер применит конфигурацию по умолчанию.

![](.gitbook/assets/10%20%281%29.jpeg)

### Blank-конфигурация

* Используется в тех случаях, когда стандартная конфигурация не требуется
  * Не нужен фаервол
  * Не нужен NAT
* Минимальная настройка для доступа в интернет \(если на роутере нет default-конфигурации\):
  * LAN IP адрес, ДНС-сервер
  * WAN IP адрес, маршрут по-умолчанию
  * Правило NAT \(masquerade\)
  * SNTP клиент и часовой пояс

## **Обновление роутера**

### Когда необходимо обновление

* Исправлен известный баг.
* Нужна новая функция.
* Улучшена производительность.

{% hint style="info" %}
**ПРИМЕЧАНИЕ: ПОЖАЛУЙСТА, прочитайте список изменений!!**
{% endhint %}

Что нового в 5.25 \(2013-Apr-25 15:59\):

\*\) web proxy - ускорен запуск;

\*\) metarouter - исправлены случайные блокировки на платах mipsbe;

\*\) wireless - обновление требуется при использовании канала малой ширины RB2011 RB9xx

предостережение: обновите удаленный конец\(цы\) перед обновлением AP, поскольку обе стороны должны использовать новую/ту же версию для ссылки

### Порядок

* Требует планирования.
  * Шаги должны быть выполнены в точном порядке.
* Требует тестирования
  *  И тестирования…
  * И, да, тестирования!

#### Перед обновлением

* Знайте какую архитектуру \(_mipsbe, ppc,_ _x86, mipsle, tile_\) вы обновляете.
  * Если вы сомневаетесь, Winbox указывает на архитектуру в верхнем левом углу!
* Знайте, какие файлы вам нужны:
  * _NPK : базовый образ RouterOS со стандартными пакетами \(всегда\)_
  * _ZIP : дополнительные пакеты \(в зависимости от потребностей\)_
  * _Changelog : указывает что как изменилось и специальные показатели \(всегда\)_

#### Как обновить

* Получить файлы пакета с сайта MikroTik
  * Страница загрузки

![](.gitbook/assets/11%20%281%29.jpeg)

* Три пути
  * Скачать файл\(ы\) и скопировать на маршрутизатор.
  * “Check for updates” \(System -&gt; Packages\)
  * Auto Upgrade \(System -&gt; Auto Upgrade\) \(Автообновление\)

Загрузка файлов

* Скопируйте файлы на маршрутизатор через окно "Files". Примеры:
  * _routeros-mipsbe-5.25.npk_
  * _ntp-5.25-mipsbe.npk_
* Перезагрузить
* Проверить состояние маршрутизатора

#### Проверка наличия обновлений \(с пакетами /system\)

* Через меню “System -&gt; Packages”
* Кликните “Check for Updates”, затем “Download & Upgrade”
* Перезагружается автоматически
* Проверка пакетов и состояния маршрутизатора

![](.gitbook/assets/12.jpeg)

#### Автообновление

* Копирование необходимых файлов всеми маршрутизаторами на внутренний маршрутизатор \(источник\).
* Настройка всех маршрутизаторов для указания исходного маршрутизатора
* Отображение доступных пакетов
* Выбор и загрузка пакетов
* Перезагрузка и проверка маршрутизатора

![](.gitbook/assets/13.jpeg)

#### Обновление прошивки RouterBOOT

* Проверьте текущую версию
* \[admin@MikroTik\] &gt; /system routerboard print
*     routerboard: yes
*         model: 951-2n
*     serial-number: 35F60246052A
*   current-firmware: 3.02
*   upgrade-firmware: 3.05
* \[admin@MikroTik\] &gt;



* Обновление при необходимости \(_в данном примере_\)

```text
[admin@MikroTik] > /system routerboard upgrade 
Do you really want to upgrade firmware? [y/n] y
firmware upgraded successfully, please reboot for changes to take effect!
[admin@MikroTik] > /system reboot
Reboot, yes? [y/N]:
```

## **Управление логинами RouterOS**

### Учетные записи пользователей

* Создание учетных записей пользователей для
  * Управления привилегиями
  * Логирования действий пользователя
* Создание групп пользователей для
  * Обладают большей гибкостью при назначении привилегий

![](.gitbook/assets/14.jpeg)

## **Управление службами RouterOS**

### Службы IP

* Управление службами IP:
  * Ограничение использования ресурсов \(ЦП, память\)
  * Ограничение угроз безопасности \(открытые порты\)
  * Изменение TCP-портов
  * Ограничение одобренных IP-адресов/IP-подсетей
* Для управления службами перейдите в раздел “IP -&gt; Services”
* Отключите или включите необходимые службы.

![](.gitbook/assets/15%20%281%29.jpeg)

### Доступ к службам IP

* Дважды щелкните на службе
* При необходимости укажите, какие узлы или подсети могут получить доступ к службе
  * Хорошая практика, чтобы ограничить определенные сервисы для сетевых администраторов

![](.gitbook/assets/16.jpeg)

## Управление резервными копиями конфигурации

### Типы резервных копий

* двоичное резервное копирования
* экспорт конфигурации

### Двоичное резервное копирование

* Полное резервное копирование системы
* Включает пароли
* Предполагается, что восстановление будет на том же маршрутизаторе

![](.gitbook/assets/17.jpeg)

### Export files

![](.gitbook/assets/m1-export.png)

* Полная или частичная конфигурация
* Создает файл скрипта или отправляет на экран
* Используйте " compact” для отображения только нестандартных конфигураций \(по умолчанию на ROS 6\)
* Используйте "verbose", чтобы показать конфигурации по умолчанию

### Архивирование файлов резервных копий

* После создания скопируйте их на сервер
  * Через SFTP \(безопасный метод\)
  * Через FTP, если он включен в IP Services
  * Используя перетаскивание из окна “Files”
* Оставлять резервные копии файлов на маршрутизаторе не очень хорошая стратегия архивирования
  * No tape or CD backups are made of routers

## **Лицензии RouterOS**

### Уровни лицензий

* 6 уровней лицензий
  * 0 : Демо \(24 часа\)
  * 1 : Free \(весьма ограничена\)
  * 3 : WISP CPE \(Wi-Fi клиент\)
  * 4 : WISP \(требуется для запуска точки доступа\)
  * 5 : WISP \(более производительная\)
  * 6 : Controller \(неограниченные возможности\)

### Лицензии

* Определяет допустимую производительность маршрутизатора.
* RouterBOARD поставляется с предустановленной лицензией.
  * Уровни варьируются
* Лицензии должны быть приобретены для системы X86.
  * Одна лицензия действительна только для одной машины.

### Обновление лицензий

* Уровни описаны на веб-странице

[http://wiki.mikrotik.com/wiki/Manual:License](http://wiki.mikrotik.com/wiki/Manual:License)

* Типовое применение
  * Level 3: CPE, беспроводной клиент
  * Level 4: WISP
  * Level 5: Большой WISP
  * Level 6: внутренняя инфраструктура интернет-провайдера \(ядро облака\)

### Использование лицензий

* Купите нужное устройство/лицензию с самого начала.
* Лицензия привязана к диску, на котором она установлена. Будьте осторожны, чтобы не отформатировать диск с помощью инструментов не Mikrotik.
* Прочитайте веб-страницу лицензии для получения более подробной информации!

## **Сетевая установка**

### Использование сетевой установки

* Переустановка RouterOS если исходный образ был поврежден
* Переустановка RouterOS, если пароль ”admin" был потерян
* Вы можете найти на веб-сайте MikroTik на вкладке загрузки

### Процедура без COM-порта

Для RB без COM-порта.

* Подключите компьютер к **порту Ethernet 1**
  * Дайте компьютеру статический IP-адрес и маску
* Запустите Netinstall
  * Нажмите на кнопку " Net booting” и напишите случайный IP-адрес в той же подсети, что и компьютер
* В разделе “Packages”, нажмите “Browse” и выберите каталог, содержащий допустимые файлы NPK
* Нажмите кнопку "reset", пока светодиод " ACT " не погаснет
  * Маршрутизатор появится в разделе "Routers/Drives"
  * Выберите его!
* Выберите необходимую версию RouterOS из раздела "Packages"
  * Кнопка “Install” станет доступной; нажмите её!
* Прогресс-бар будет закрашиваться в синий цвет пока файл NPK будет передаваться
* После завершения подсоедините компьютерный кабель к одному из допустимых портов и кабель доступа в Интернет к порту 1
* Используйте MAC-Winbox для подключения, поскольку конфигурация будет пустой
  * Даже если было выбрано "Keep old configuration"!!
* Загрузите резервную копию конфигурации и перезагрузите
  * \(вот в чем важность правильного управления резервным копированием!\)
* Если проблема заключалась в утерянном пароле, переделайте конфигурацию с нуля, так как при резервном копировании будет использоваться тот же _**забытый**_ пароль \(при этом важна правильность управления доступом!\)

### Процедура с COM-портом

Для RB с COM-портом

* Она начинается \(почти\) так же
  * ПК в **порт Ethernet 1** со статическим адресом
  * Подключить серийный порт ПК к консольному \(COM\) порту RouterBOARD
  * Запустите Netinstall \(и настройте параметр "Net Booting"\)
  * Выберите каталог с файлами NPK
* Перезагрузите маршрутизатор
* Нажмите кнопку "Enter", когда появится запрос, чтобы войти в настройки
* Нажмите “o” для загрузочного устройства
* Нажмите “e” для Ethernet
* Нажмите “x” для выхода из установок \(что перезагрузит маршрутизатор\)
  * Маршрутизатор появится в разделе “Routers/Drives”
  * Select it
* Выберите пакет RouterOS, который будет установлен
  * Нажмите кнопку **“Keep old configuration” \(Сохранить старую конфигурацию\)**
  * Кнопка “Install” становится доступной; нажмите её!
* Прогресс-бар будет закрашиваться в синий цвет пока файл NPK будет передаваться
* После завершения подсоедините компьютерный кабель к одному из допустимых портов и кабель доступа в Интернет к порту 1
* Вы можете использовать Winbox для подключения
  * Опция “Keep old configuration” здесь работает!!
* Перезагрузите маршрутизатор
* Нажмите кнопку "Enter", когда появится запрос, для входа в настройки
* Нажмите “o” для загрузки устройства
* Нажмите “n” для NAND затем Ethernet при сбое
  * **Если вы забыли, вы всегда будете загружаться из Ethernet**
* Нажмите “x” для выхода из настроек \(что перезагрузит маршрутизатор\)

## **Дополнительные ресурсы**

### Wiki

[http://wiki.mikrotik.com/wiki/Manual:TOC](http://wiki.mikrotik.com/wiki/Manual:TOC)

* RouterOS главная страница Вики
* Документация по всем командам маршрутизаторов
  * Пояснение
  * Синтаксис
  * Примеры
* Дополнительные советы и рекомендации

### Tiktube

[http://www.tiktube.com/](http://www.tiktube.com/)

* Видео ресурсы на различные темы
* Представления тренеров, партнеров, интернет-провайдеров и др.
* Может включать в себя презентации слайдов
* Различные языки

### Форум

[http://forum.mikrotik.com/](http://forum.mikrotik.com/)

* Модерируется сотрудниками Mikrotik
* Дискуссии по различным темам
* Много информации можно найти здесь
  * Вы можете найти решение своей проблемы!
* Пожалуйста, воспользуйтесь поиском ПЕРЕД размещением вопроса
  * Стандартный этикет форума

### Поддержка Mikrotik

[support@mikrotik.com](mailto:support@mikrotik.com)

* Процедуры поддержки описанны в [http://](http://www.mikrotik.com/support.html) [www.mikrotik.com/support.html](http://www.mikrotik.com/support.html)
* Поддержка от Mikrotik в течение 15 дней \(уровень лицензии 4\) и 30 дней \(уровень лицензии 5 и уровень 6\), если маршрутизатор куплен у них

### Дистрибьюторская/консультационная поддержка

* Поддержка предоставляется дистрибьютором при покупке маршрутизатора у них
* Сертифицированные консультанты могут быть наняты для особых нужд. Посетите [http://](http://www.mikrotik.com/consultants.html) [www.mikrotik.com/consultants.html](http://www.mikrotik.com/consultants.html) для получения дополнительной информации

Время для практических занятий

## Лабораторка

* Цель лабораторной работы
  * Ознакомление студентов с методами доступа
  * Настройка доступа в интернет
  * Обновление маршрутизатора на текущую RouterOS
  * Создание группы ограниченного доступа, назначение ей пользователя
  * Управление IP-службами
  * Создание резервной копии текущей конфигурации и восстановление ее после сброса настроек

Лабораторка: Установка

![](.gitbook/assets/19.jpeg)

Лабораторка: шаг 1

* Настройка компьютера со статическим IP-адресом вашего модуля
  * Укажите маску подсети
  * Укажите шлюз по умолчанию \(ваш маршрутизатор\)
  * Укажите DNS-сервер \(маршрутизатор\)
* Сделайте Netinstall на ROS 6
* После перезагрузки подключиться к нему таким образом, что позволит вам полный доступ

![](.gitbook/assets/8%20%281%29.jpeg)

Лабораторка: шаг 2

* Настройка LAN IP-адреса маршрутизатора
* Настройка WAN IP-адреса маршрутизатора
* Настройка правила NAT маршрутизатора
* Настройка DNS-сервера маршрутизатора
* Настройка маршрута по умолчанию для маршрутизатора\*

Лабораторка: шаг 3

* Добавить группу под названием “minimal”
  * Дайте ей права” telnet“, ”read“ и ”winbox"
  * Объясните эти права
* Добавьте пользователя и дайте ему свое имя
  * Назначьте ему группу "minimal"
  * Назначьте ему пароль
* Назначьте пароль для “администратора”
  * Дайте ему "pod_X_“, где "_X_" - номер вашего модуля
  * Откройте новый терминал. Что произошло?

Лабораторка: шаг 4

* Убедитесь, что прошивка RouterBOARD обновлена.
* Скопируйте пакет NTP \(файл NPK\)
  * Check System -&gt; SNTP Client
  * Check System -&gt; NTP Client and NTP Server
  * Что произошло
* Как только перезагрзится
  * Check System -&gt; SNTP Client
  * Check System -&gt; NTP Client and NTP Server
* Настройка NTP-клиента и часового пояса

Лабораторка: шаг 5

* Студенты подключатся через телнет к маршрутизатору
* Студенты отключат эти IP-сервисы:
  * Telnet
  * WWW
* Студенты будут подключаться к маршрутизатору с помощью Telnet, веб-браузера и SSH
  * Объясните результаты

Лабораторка: шаг 6

* Откройте “New Terminal” и окно “Files”
* Экспортируйте конфигурацию из корня в файл с именем “module1-pod_X_”
* Сделайте двоичное резервное копирование
* Скопируйте оба файла на компьютер
  * Откройте их оба и просмотрите содержимое
  * Удалите правило NAT и используйте ”экспортированный" файл, чтобы быстро его воссоздать

Лабораторка: шаг 7

* Просмотр лицензии routerBOARD
  * Проверьте уровень маршрутизатора и укажите его назначение
  * Как группа обсудите потенциальные возможности использования этого уровня лицензии



File: /m2-routing.md
# M2 Routing

## **Обзор маршрутизации**

Концепции маршрутизации

* Маршрутизация-это процесс уровня 3 в модели OSI ISO.
* Маршрутизация определяет, куда перенаправляется \(отправляется\) трафик.
* Она необходима чтобы разрешить различные подсети для обмена данными.
  * Даже если они должны быть на одном “проводе”

### Концепции маршрутизации, пример 1

* Компьютеры не будут взаимодействовать

![](.gitbook/assets/0%20%281%29.jpeg)

### Концепции маршршутизации, пример 2

* Компьютеры теперь могут взаимодействовать

![](.gitbook/assets/1.jpeg)

Флаги маршрута

* Маршруты имеют статусы. В этом курсе мы ознакомимся со следующим:
  * X: Disabled \(отключен\)
  * A : Active \(активен\)
  * D : Dynamic \(динамический\)
  * C : Connected \(подключен\)
  * S : Static \(статичен\)

![](.gitbook/assets/2%20%285%29.jpeg)

Флаги маршрута

* **Disabled** : маршрут отключен. Не имеет никакого влияния на процесс маршрутизации.
* **Active** : маршрут активен и используется в процессе маршрутизации.
* **Dynamic** : маршрут был создан процессом маршрутизации, а не через интерфейс управления.
* **Connected** : маршруты создаются для каждой IP-подсети, которая имеет активный интерфейс на маршрутизаторе.
* **Static** : маршрут, созданный для принудительной пересылки пакетов через определенный .

## **Статическая маршрутизация**

Статический маршрут

* Маршруты к подсетям, которые существуют на маршрутизаторе, автоматически создаются и известны **этим** маршрутизаторам. Но что произойдет, если вам нужно добраться до подсети, которая существует на другом маршрутизаторе? Вы создаете статический маршрут!
* Статический маршрут-это ручной способ пересылки трафика в неизвестные подсети.

![](.gitbook/assets/3%20%281%29.jpeg)

Статический маршрут

* Понимание полей
  * **Flags** : состояние каждого маршрута, как описано в предыдущих слайдах
  * **Dst. Address** : адреса назначения, для которых используется этот маршрут.
  * **Gateway** : как правило, IP-адрес следующего маршрутизатора, который будет получать пакеты, предназначенные для “_**Dst. Address**_”.
  * **Distance** : значение, используемое для выбора маршрута. В конфигурациях, где возможны различные дистанции, выбирается маршрут с наименьшим значением.

### Зачем использовать статическую маршрутизацию

* Делает конфигурацию проще для очень маленькой сети, которая, скорее всего, не будет расти.
* Ограничивает использование ресурсов маршрутизатора \(память, процессор\)

![](.gitbook/assets/4%20%281%29.jpeg)

### Ограничения статической маршрутизации

* Не очень хорошо масштабируется.
* Ручная настройка требуется каждый раз, когда требуется достичь новой подсети.

#### Ограничения статической маршрутизации, пример

Ваша сеть растет, и вам нужно добавить ссылки на удаленные маршрутизаторы \(и подсети\).

* Предположим, что все маршрутизаторы имеют 2 подсети LAN и 1 или более подсетей WAN

Сколько статических маршрутов добавить на роутер-1?

* Маршрутизаторы с 3 по 5 : 9
* Маршрутизатор 2 : 2
* Маршрутизатор 6 и 7 : 4

**Всего 15 статических маршрутов для добавления вручную!!**

![](.gitbook/assets/image%20%2826%29.png)

### Создание маршрутов

![](.gitbook/assets/image%20%287%29.png)

![](.gitbook/assets/m2-create.png)

* Добавление статического маршрута :
  * IP -&gt; Routes
  * \(Add\)
  * Укажите подсеть назначения и маску
  * Укажите “Gateway” \(следующий маршрутизатор\)

### Установка маршрута по-умолчанию

* Маршрут 0.0.0.0/0
  * Известен как **Default route \(Маршрут по-умолчанию\)**.
  * Это место назначения, куда будет перенаправляться весь трафик в неизвестные подсети.
  * Это также статический маршрут.

### Управление динамическими маршрутами

* Как упоминалось ранее, динамические маршруты добавляются процессом маршрутизации, а не администратором.
* Это делается автоматически.
* Вы не можете управлять динамическими маршрутами. Если интерфейс, с которым связан динамический маршрут, отключается, тоже самое происходит и с маршрутом!

#### Управление динамическими маршрутами, пример

![](.gitbook/assets/image%20%2822%29.png)

![](.gitbook/assets/image%20%2823%29.png)

Реализация статической маршрутизации в простых сетях

Рассмотрим следующий пример.

![](.gitbook/assets/image%20%2818%29.png)

* Упражнение:
  * Предполагая, что ip-адреса были правильно введены, какие команды вы бы использовали для включения полной связи для обеих подсетей \(LAN1 и LAN2\)?
  * \(Ответ на следующем слайде. Не расстраивайтесь 🙂\)



* router-1
  * /ip route
  * add gateway=172.22.0.18
  * add dst-address=10.1.2.0/24 gateway=10.0.0.2
* router-2
  * /ip route
  * add gateway=10.0.0.1

## Лабораторка

* Цели лабораторки
  * Получить возможность подключения к другим локальным сетям
  * Проверка использования маршрута по умолчанию
  * Просмотр и объяснение флагов маршрута

Лабораторка: установка

![](.gitbook/assets/9%20%282%29.jpeg)

### Лабораторка: шаг 1

* Удалите маршрут по умолчанию, созданный в модуле 1
* Пингуйте компьютеры других POD. Отметьте результаты
* Создайте статические маршруты к подсетям других POD локальной сети
* Пингуйте компьютеры других POD. Отметьте результаты

### Лабораторка: шаг 2

* Откройте веб-браузер и попробуйте получить доступ к веб-странице Mikrotik. Отметьте результаты
* Создайте маршрут по умолчанию, используя маршрутизатор-тренажер в качестве шлюза
* Откройте веб-браузер и попробуйте получить доступ к веб-странице Mikrotik. Отметьте результаты

![](.gitbook/assets/6%20%283%29.jpeg)


File: /m3-bridging.md
# M3 Bridging

## Обзор **Bridging (Моста)**

Концепция Моста

* Мосты - это устройства 2 уровня OSI.
* Традиционно они использовались для объединения двух сегментов различных \(или похожих\) технологий.

![](.gitbook/assets/0%20%281%29.png)

* Мосты также использовались для создания меньших доменов колизий.
  * Целью было повышение производительности за счет уменьшения размера подсети. Особенно полезно перед появлением коммутаторов.
* Коммутаторы известны как многопортовые мосты.
  * **Каждый порт** является доменом колизий одного устройства!

Пример 1

* Все компьютеры могут взаимодействовать друг с другом.
* Все должны ждать, пока все успокоятся, прежде чем начать передачу!

![](.gitbook/assets/1%20%283%29.png)

Пример 2

* Все компьютеры по-прежнему ”слышат" друг друга.
* Все компьютеры теперь разделяют только половину "полосы".
* Все еще должны ждать, пока все успокоятся, прежде чем можно будет начать передачу, но сейчас группа в два раза меньше.
  * Лучшая производительность для всех устройств!

![](.gitbook/assets/2%20%281%29.png)

## Использование мостов

* По умолчанию в маршрутизаторах MikroTik порты Ethernet связаны \(slave\) с master портом.
  * Преимущество: скорость переключения полосы \(через чип коммутатора, а не программное обеспечение\).
  * Недостаток: отсутствие видимости трафика slave портов. Не желательно при использовании SNMP для мониторинга использования портов.
* Удаляя конфигурацию master и slave, вы должны использовать интерфейс моста для связывания с ним необходимых портов в одной локальной сети.
  * Преимущество: полная видимость всей статистики портов для этих портов.
  * Недостаток: переключение осуществляется через программное обеспечение. Некий удар по ЦП. Скорость передачи пакетов меньше оптимальной

    .

## Создание мостов

* Используя меню
  * Bridge
  * Add \(**+**\)
  * Задание имя моста
  * Нажать “OK” и всё готово!

Создание моста, пример

![](.gitbook/assets/image%20%2819%29.png)

![](.gitbook/assets/image%20%285%29.png)

### Добавление портов к мостам

* Добавление портов определяет, какие из них принадлежат к той же подсети.
* Различные технологии могут быть добавлены, как например интерфейс Wi-Fi.
* Путь меню для добавления порта
  * Bridge
  * Ports tab
  * Add \(**+**\)
  * Choose the interface and the bridge
  * Click “OK” and you’re done!

#### Добавление портов к мостам, пример

![](.gitbook/assets/image%20%2810%29.png)

![](.gitbook/assets/image%20%2825%29.png)

Мост беспроводных сетей

* То же самое можно сделать с беспроводными интерфейсами.
* Мы увидим это в следующем модуле. Будьте терпеливы! 🙂

## Лабораторка

* Цель лабораторки
  * Создание моста
  * Назначение портов мосту
  * Убедитесь, что, выполнив следующие действия, можно назначить все свободные порты одной подсети

Лабораторка: Установка

![](.gitbook/assets/5%20%282%29.png)

### Лабораторка: шаг 1

* Запустите “ping –t –w 500 192.168.0.254”.
* Отсоедините сетевой кабель от текущего порта \(\#5\) и подключите его к другому порту.
* Обсудить результаты.
* Оставьте командное окно включенным и работающим и видимым во всей этой лаборатории.

### Лабораторка: шаг 2

* Подключитесь к маршрутизатору любым способом, который будет работать.
* Создайте интерфейс моста. Назовите его "LAN" и оставьте другие значения по умолчанию.
* Назначьте IP-адрес локальной сети модуля \(192.168.X.1\) интерфейсу моста.
* Что-нибудь изменилось?

### Лабораторка: шаг 3

* Откройте окно "Interface List" и проверьте, какие интерфейсы запущены.
* Назначьте порты с\#2 по \#5 для интерфейса моста "LAN".
* Обсудить результаты. Когда ваш пинг вернулся?
* Переключите кабель к портам №2 - 5. Что происходит? Обсудите, почему. Посмотрите на столбец статуса. Что означает "I"?


File: /m4-wireless.md
# M4 Wireless

## Концепция **802.11**

### Частоты

* 802.11b
  * 2.4GHz (ширина полосы 22MHz), 11Mbps
* 802.11g
  * 2.4GHz (ширина полосы 22MHz), 54Mbps
* 802.11a
  * 5GHz (ширина полосы 20MHz), 54Mbps
* 802.11n
  * 2.4GHz или 5GHz до 300Mbps, если используется канал 40MHz и 2 радио (каналы)

![&#x414;&#x438;&#x430;&#x433;&#x440;&#x430;&#x43C;&#x43C;&#x430; &#x41C;&#x430;&#x439;&#x43A;&#x43B;&#x430; &#x413;&#x43E;&#x442;&#x44C;&#x435;](.gitbook/assets/0%20%283%29.jpeg)

* 802.11b,g диапазон частот
* Каналы 1, 6 и 11 неперекрывающиеся

![](.gitbook/assets/1%20%283%29.jpeg)

* 802.11a частотный диапазон
* 12 каналов с шириной 20MHz и 5 с шириной 40MHz
* Диапазон
  * Mikrotik поддерживает оба 5GHz (802.11a/n) и 2.4GHz (802.11b/g/n)
* Функция “Advanced Channels” предоставляет расширенные возможности в конфигурации беспроводного интерфейса:
  * скан-список, который охватывает несколько полос и широт каналов;
  * нестандартные центральные частоты канала \(заданные с детализацией кГц\) для аппаратных средств, которые позволяют это;
  * нестандартные широты канала \(заданные с детализацией кГц\) для аппаратного обеспечения, которое позволяет это.
* Базовые скорости - это скорости, которые клиент ДОЛЖЕН поддерживать для подключения к точке доступа.
* Поддерживаемые скорости - это скорости, которые могут быть достигнуты после того, как соединение было принято \(факторы могут влиять на максимальную скорость, достигнутую\)
* Скорость передачи данных - это поддерживаемая скорость в соответствии с используемым стандартом.
  * 802.11b: от 1 до 11Mbps
  * 802.11a/g: от 6 до 54Mbps
  * в зависимости от таких факторов, как пропускная способность канала \(20 или 40 МГц\), защитный интервал \(GI\) и цепи
* HT цепи
  * Есть антенны для одного радио
  * Используется для 802.11n и является фактором пропускной способности
* Частотный режим
  * Regulatory-domain: ограничение каналов и мощность передатчика на основе положения страны.
  * Manual-txpower: то же самое, что и выше, но без ограничения мощности TX.
  * Superchannel: будет игнорировать все ограничения
* Параметр “Country”: частоты и ограничения мощности основаны на правилах ”_country_". Использование "_no\_country\_set_" настроит одобренный FCC набор каналов.

## Настройка простой беспроводной связи

![](.gitbook/assets/2%20%281%29.jpeg)

* Конфигурация точки доступа
  * Mode : ap bridge
  * Band : основанный на возможностях маршрутизатора и клиентов. Если AP поддерживает несколько полос \(например. B/G/ N\) выберите тот, который лучше всего соответствует вашим потребностям
  * Frequency : любой из доступных каналов \(мы поговорим об этом позже!!\)
  * SSID : идентификатор беспроводной сети для поиска клиентами
  * Wireless protocol : основан на возможностях маршрутизатора и клиентов. Для ”нормальных" соединений AP на ПК используйте 802.11

![](.gitbook/assets/3.jpeg)

* **ПОЖАЛУЙСТА**, НАСТРОЙТЕ ПРОФИЛЬ БЕЗОПАСНОСТИ!
  * Не делать этого - полное нарушение безопасности. Это оставляет вашу сеть широко открытой!
* Добавление профиля безопасности
  * Нажмите кнопку “Add” \(+\)
  * Name: Имя профиля
  * Mode: используемый тип аутентификации
  * Authentication types: методы, используемые для проверки подлинности соединения
  * Ciphers: методы шифрования

![](.gitbook/assets/image%20%2812%29.png)

* Теперь вы можете использовать свой новый профиль безопасности и чувствовать себя в безопасности в своей беспроводной сети

![](.gitbook/assets/image%20%2821%29.png)

* Вернемся к частотам! Какую из них использовать?
  * Кликните “Snooper”
  * Опасно! Это отключит интерфейс wlan и подключенных клиентов
  * У вас будет полное представление об используемых диапазонах и частотах
  * Выберите свободный канал или, по крайней мере, канал с низким уровнем загруженности

![](.gitbook/assets/image%20%2813%29.png)

* Конфгурация станции
  * Mode : station
  * Band : В соответствии с вашей точкой доступа
  * Frequency : для клиентов неважно

![](.gitbook/assets/9.jpeg)

* Конфигурация станции
  * SSID : должно соответствовать точке доступа, к которой подключаетесь
  * Wireless protocol : должен соответствовать точке доступа, к которой подключаетесь
  * Создайте профиль безопасности, как показано в конфигурации "точка доступа", и примените его здесь. Параметры ДОЛЖНЫ совпадать.

![](.gitbook/assets/image%20%2816%29.png)

## Фильтрация MAC-адресов

* Фильтрация MAC-адресов является дополнительным способом ограничения соединения с клиентами.
* Чтобы добавить запись в список доступа \(на ТД!!\), выберите зарегистрированный узел и нажмите кнопку “Copy to Access list”

![](.gitbook/assets/image%20%284%29.png)

* Теперь у Вас есть новая запись!

![](.gitbook/assets/11.jpeg)

Фильтрация MAC-адресов

![](.gitbook/assets/12%20%281%29.jpeg)

* Списки доступа используются **на ТД** для ограничения подключений к определенным клиентам и управления их параметрами подключения.
  * Правила проверяются последовательно
  * Применяется только первое совпадающее правило
  * Если параметр “Default Authenticate” \(вкладка _”Wireless“_ на экране _”Interface -&gt; wlan"_\) снята, устройства, не соответствующие правилу списка доступа, отклоняются

![](.gitbook/assets/13%20%281%29.jpeg)

* Параметр **Authentication** укажет маршрутизатору проверить "security-profile", чтобы определить, должно ли соединение быть разрешено. Если флажок снят, проверка подлинности всегда завершается ошибкой.
* Параметр Forwarding укажет маршрутизатору, чтобы позволил клиентам ТД связаться друг с другом без помощи ТД \(таким образом, минуя правила брандмауэра, которые у вас могут быть\). Для дополнительной безопасности отключите.
* AP TX Limit ограничивает скорость передачи данных от ТД к клиенту
  * Установка слишком низкого уровня может вызвать проблемы с подключением. Сперва протестируйте!
* Client TX Limit ограничивает скорость передачи данных от клиента к точке доступа
  * Собственное расширение, которое поддерживается только клиентами RouterOS
  * Опять же, вы должны протестировать, чтобы увидеть приемлимое значение

![](.gitbook/assets/15.jpeg)

* Connect List \(cписки соединений\) \(на клиентских станциях\) назначают приоритеты на основе параметров уровня сигнала и безопасности, которые определяют, к каким точкам доступа клиент может подключиться
  * Правила проверяются последовательно
  * Применяется только первое совпадающее правило
  * Если опция ”Deafult Authentificate“ \(вкладка _”Wireless“_ на экране _”Interface -&gt; wlan"_\) проверена и не соответствует правилам списка соединений, клиент попытается подключиться на основе лучшей совместимости сигнала и безопасности

![](.gitbook/assets/16%20%281%29.jpeg)

* Пример: У этой станции не определены **SSID** или **Security** **profile**, но поскольку у нее есть соответствие списка соединений, соединение было установлено

![](.gitbook/assets/17.png)

* **Интересное замечание**: Если поле SSID \(_в правилах подключения станции_\) пусто, клиент подключится к любому SSID с соответствующим **Security profile**.
* Поле SSID интерфейса так же должно быть пустым!



* Default-authentication : задает поведение после проверки списков доступа и подключения.
  * Для точек доступа, если установлено в yes - разрешит соединение, если нет соответствия в списке доступа, предоставленного интерфейсу SSID и соответствия профиля безопасности. В противном случае никакие соединения не допускаются.
  * Для станций, если задано значение yes, будут разрешены соединения, если нет совпадения в списке соединений, предоставленного интерфейсу SSID и профиля безопасности. В противном случае никакие связи не допускаются.
  * Если у ТД нет списка доступа и default-authenticate не установлено, клиенты никогда не смогут подключиться
  * Если у станции нет списка подключений и default-authenticate не установлен, она никогда не подключится к точке доступа
* Default-forwarding : задает поведение переадресации клиентов после проверки списков доступа.
  * Если установлено значение да, будет разрешена связь 2 уровня между клиентами.
  * Если установлено нет - клиенты будут по-прежнему видеть друг друга \(на уровне 3\), ЕСЛИ это разрешено правилами брандмауэра.

## Безопасность и шифрование беспроводного соединения

* WPA, WPA2
  * Wi-Fi защищенный доступ \(I и II\)
  * Протокол аутентификации, созданный после обнаружения слабых мест в WEP
  * При правильной настройке WPA весьма безопасен
    * Слабые места для атак брутфорсом были обнаружены при использовании WPS \(Wi-Fi Protected Setup\)
    * WPS не используется Mikrotik
* WPA
  * Используется для замены WEP \(найдены слабые места\)
  * Использует TKIP в качестве протокола шифрования
    * Генерирует новый ключ для каждого пакета
* WPA2
  * Использует CCMP в качестве протокола шифрования
    * Основан на AES
    * Сильнее чем TKIP
  * Является обязательным в Wi-Fi сертифицированных устройствах с 2006 года
  * Должен использоваться для достижения более высокой скорости передачи данных, иначе ограничивается 54 Мбит/с \([_http://www.intel.com/support/wireless/wlan/4965agn/sb/cs-025643.htm_](http://www.intel.com/support/wireless/wlan/4965agn/sb/cs-025643.htm)\)
* WPA-Personal
  * Также известен как WPA-PSK, предназначен для небольших офисов и дома
  * Не требует сервера аутентификации
  * Аутентификация клиента на ТД основана на 256-битном ключе, созданном из предварительно общедоступного ключа \(PSK\), который может быть паролем или парольной фразой, известной обоим
* WPA-Enterprise
  * Также упоминается как режим WPA-802.1X, предназначен для корпоративных сетей
  * Использует EAP для аутентификации
  * Требуется сервер проверки подлинности RADIUS
  * Более сложное развертывание, но предоставляет дополнительные функции, такие как защита от атак по словарю на более слабые пароли

## Протоколы беспроводных соединений MikroTik

* NV2 \(Nstreme Version 2\)
  * Проприетарный протокол Mikrotik во второй версии
  * Для использования с беспроводным чипом Atheros 802.11.
  * На основе TDMA \(_Множественный доступ с разделением по времени_\) вместо CSMA \(_Множественный доступ с контролем несущей_\)\(_Carrier Sense Multiple Access_\)
  * Используется для повышения производительности на больших расстояниях
* Преимущества NV2
  * Увеличенная скорость
  * Больше клиентских подключений в многопользовательских средах \(ограничение в 511 клиентов\)
  * Снижение задержек
  * Отсутствие ограничений по расстоянию
  * Нет штрафов за большие расстояния

## Инструменты мониторинга

* Существуют различные инструменты, которые помогут вам проанализировать, что находится в воздухе, так что вы можете выбрать частоту без \(или с наименьшим количеством\) помех
* Беспроводное сканирование: два варианта
  * Frequency Usage
  * Scan

![](.gitbook/assets/image%20%2824%29.png)

* Wireless scan : Frequency Usage
  * Показывает все поддерживаемые частоты и их использование соседними точками доступа
  * **Удаляет подключенных беспроводных клиентов!**

![](.gitbook/assets/image%20%2817%29.png)

* Wireless scan : Scan
  * Дает информацию о соседних точках доступа
  * **Удаляет подключенных беспроводных клиентов!**

![](.gitbook/assets/20.jpeg)

* Snooper
  * Предоставляет более подробную информацию о других точках доступа и клиентах
  * **Удаляет подключенных беспроводных клиентов!**

![](.gitbook/assets/21.png)

* Snooper
  * Дает более подробную информацию о других AP и станций, дважды щелкнув
* Registration table : Используется для получения информации о подключенных клиентских станциях.
  * Полезно только на точках доступа.

![](.gitbook/assets/22.jpeg)

![](.gitbook/assets/image%20%2827%29.png)

* Registration table
  * Мы можем видеть текущее состояние соединения станции
  * Примечание: комментарии, появляющиеся над станциями, находятся на вкладке "Access List". Полезно посмотреть, по каким критериям станция была авторизована

## Соединение беспроводвных сетей

* Station-bridge : проприетарный режим Mikrotik для создания безопасного L2-моста между маршрутизаторами Mikrotik
* Может использоваться для расширения беспроводной подсети для большего количества клиентов

Время для практических занятий

## Лабораторка

* Цель лабораторки
  * Используйте различные инструменты для анализа используемых каналов и характеристик беспроводных сетей, точек доступа и станций
  * Настройте под маршрутизаторы как беспроводные клиенты к маршрутизатору учителя
  * Настройте под маршрутизаторы как беспроводные точки доступа
  * Ознакомьтесь со списками подключений и списками доступа

Лабораторка: Установка

![](.gitbook/assets/24.jpeg)

Лабораторка: Предварительная подготовка

* **ПРЕЖДЕ ЧЕМ МЫ ЧТО-НИБУДЬ СДЕЛАЕМ!!!**
  * Сделайте бинарную резервную копию текущей конфигурации под именем:
    * Module3-pod<i>X</i> где _X_ это ваш подномер
  * Как бы вы это сделали?
  * Какие окна вы бы открыли?

### Лабораторка: шаг 1

* Запустите один за другим:
  * Frequency Usage
    * Запишите наиболее используемые каналы
  * Scan
    * Создайте связь между частотами и видимыми SSID
  * Snooper
    * Что вы можете сказать о видимых сетях?
    * Что представляют собой символы в левом столбце?

### Лабораторка: шаг 2

* Откройте окно “Bridge” и перейдите во вкладку the “Ports”
* Используя процедуры, которые мы видели в предыдущих модулях, добавьте интерфейс “wlan1” к подключению “LAN”.
* Закройте окно “Bridge”

### Лабораторка: шаг 3

* Откройте окно “Wireless” и убедитесь что интерфейс “wlan1” включен

### Лабораторка: шаг 4

* Кликните дважды на интерфейсе и перейдите на вкладку Wireless”. Нажмите кнопку "Advanced Mode”, затем введите следующие параметры:
  - Mode: ap bridge
  - Band: 2GHz-B/G/N
  - Channel width: 20MHz
  - Frequency: Odd pods use 2437, even pods use 2462
  - SSID: pod<i>X</i>
  - Wireless protocol: 802.11
  - Security Profile: default **(что было бы _ПЛОХОЙ_ идеей в любое другое время)**
  - Frequency Mode: Regulatory-domain
  - Country: _<где_вы_сейчас_находитесь>_
  - Default Authenticate is checked

### Лабораторка: шаг 5

* Отключите сетевой кабель между ноутбуком и маршрутизатором. Кабель от вашего маршрутизатора к маршрутизатору учителя должен остаться
* Настройте Ваш ноутбук для использования параметров wi-fi вашего маршрутизатора
* Убедитесь, что у вас есть подключение wi-fi
* Подключитесь к Интернету

### Лабораторка: шаг 6

* Сделайте двоичную резервную копию текущей конфигурации под именем:
  - Module4a-pod<i>X</i>, где _X_ - номер вашего модуля
* В окне "File List" выберите module3-pod<i>X</i> и нажмите на кнопку "Restore" в верхней части окна
* Ответьте “Yes”, чтобы перезагрузить маршрутизатор.

### Лабораторка: шаг 7

* Подключите сетевой кабель вашего ноутбука к маршрутизатору.
* Отсоедините сетевой кабель вашего маршрутизатора от маршрутизатора преподавателя.
* Теперь у вас не должно быть доступа в Интернет

### Лабораторка: шаг 8

**Предварительная подготовка**

* IP-адрес для WLAN1
  - 192.168.252.pod<i>X</i>
* Включите интерфейс wlan1, если он не включен
* Профиль безопасности
  - Name: WPA2
  - Authentication types: WPA2 PSK
  - Unicast and group ciphers: aes ccm
  - WPA2 pre-shared key: mtcna123!

### Лабораторка: шаг 9

* Активируйте “Advanced Mode” во вкладке "Wireless" раздела "Interface <wlan1>"
* Нам нужно подключиться к точке доступа класса. Следующие параметры должны быть совместимы с параметрами точки доступа для подключения.
  - Mode: Station
  - Band: 2GHz-only-N
  - SSID: WISP
  - Radio name: WISP-POD<i>X</i>
  - Wireless protocol: 802.11
  - Security profile: WPA2

### Лабораторка: шаг 10

* Frequency Mode: regulatory-domain
* Country: выбирите страну, в которой будет установлена ТД.
* Оставьте пока флажок “Default Authenticate”
* Кликните OK и выберите вкладку “Registration” в окне “Wireless Tables”
* Вы должны видеть, как появляется ТД учителя. Если это так, то вы подключены!
  - **Но подождите!!!**

### Лабораторка: шаг 11

* Прежде чем просмотр сможет работать, давайте исправим наши таблицы маршрутизации.
  - Переопределите шлюз по умолчанию на 192.168.252.254
  - Переопределите маршрут к локальному интерфейсу модуля вашего соседа (192.168._Y_.1) через 192.168.252._Y_
  - Проверьте пинг до сетевого интерфейса модуля вашего соседа (192. 168._Y_.1)
    - Каков же результат?

**Конец 4 лабораторки**


File: /m5-network-management.md
# M5 Network Management

## ARP

* Означает “Address Resolution Protocol” - "Протокол определения адреса”
* Механизм, который связывает IP-адрес уровня 3 с MAC-адресом уровня 2
* Обычно используется как динамический процесс, но может быть сконфигурирован статически в определенных ситуациях, когда этого требует безопасность

### Режимы ARP

* "Режимы ARP" расскажут RouterOS, как должен работать ARP
  - Режимы настраиваются по принципу "на интерфейсе".
* "Режимы" могут быть
  - **Enabled**: режим по умолчанию. На запросы ARP будут даны ответы и таблица ARP будет заполнена автоматически
  - **Disabled**: интерфейс не будет отправлять или отвечать на запросы ARP. Другим хостам необходимо сообщить MAC-адрес маршрутизатора
  - **Proxy ARP**: маршрутизатор отвечает на запрос ARP, поступающий для его непосредственно подключенной сети (независимо от источника)
  - **Reply only**: маршрутизатор отвечает на запросы ARP. Таблица ARP маршрутизатора должна быть заполнена статически

### Таблица ARP RouterOS

* Таблица ARP отображает все записи ARP и интерфейс, из которого они извлекаются
* Таблица ARP предоставляет:
  - IP-адрес известных устройств
  - MAC-адреса, связанные с IP-адресами
  - Интерфейсы, с которых они были извлечены
* Вы можете добавить статические записи в таблицу ARP, чтобы защитить свою сеть
  - Может избежать заражения/подмены ARP
  - Требует много работы и планирования

### Синтаксис ARP

* Просмотр таблицы ARP:
  - `/ip arp print`
* Добавить статическую запись:
  -  `/ip arp add address=172.16.2.222 macaddress=11:22:33:44:55:66 interface=Bridge-PC`
* Настройка режима ARP:
  - `/interface ethernet set ether04 arp=proxyarp`

## DHCP сервер и клиент

### DHCP сервер

* Расшифровывается как Dynamic Host Configuration Protocol - протокол динамической настройки узла
* Он используется для автоматического выделения IP-адреса, маски сети, шлюза по умолчанию и, возможно, других параметров запрашиваемых узлом

#### Настройки DHCP-сервера

* Интерфейс, на котором размещается DHCP-сервер, должен иметь собственный IP-адрес, отсутствующий в пуле адресов
  - Пул - это диапазон IP-адресов, которые будут доступны клиентам.

* В окне DHCP-сервера просто нажмите на кнопку "DHCP Setup" и ответьте на вопросы
  - DHCP Server Interface - интерфейс DHCP-сервера
  - DHCP Address Space - адресное пространство dhcp
  - Gateway for DHCP Network - шлюз для DHCP-сети
  - Addresses to Give Out - адреса для выдачи
  - DNS Servers (можно ввести более одного)
  - Lease Time - время аренды

* Автоматическая настройка:
  - Создаем пул IP-адресов:
    - Пул IP-адресов для назначения
  - Создаем DHCP-сервер
    - Его имя и параметры (например, интерфейс, от которого он будет принимать запросы)
  - Создаем адресное пространство:
    - IP-сеть и различные параметры

* Результаты автоматизированной настройки

![](/pics/m5_dhcp_server.png)

* DHCP можно использовать для настройки таких параметров, как:
  - 42: серверы NTP
  - 70: POP3-сервер
  - Посетите для получения дополнительных параметров DHCP
* **Важное примечание**
  - Если у вас есть бриджевое пространство, DHCP-сервер должен быть установлен на интерфейсе бриджа. Если он установлен на порту бриджа, DHCP-сервер не будет работать.

#### Синтаксис DHCP-сервера

  * Настройка области DHCP
    - `/ip dhcp-server setup`
  * Настройка параметра DHCP
    - `/ip dhcp-server option add name=46-node-type code=46 value=0x0008`
  * Назначить параметр DHCP для сети
    - `/ip dhcp-server network print` (для просмотра доступных сетей)
    - `/ip dhcp-server network set dhcp-option=46-node-type numbers=1`
  * Назначение WINS-сервера сети
    - `/ip dhcp-server network set wins-server=172.16.2.100 numbers=1`

#### Конфигурация DHCP-сервера “Networks”

* Пример базовой конфигурации

![](/pics/m5_dhcp_server_basic.png)

* Пример расширенной конфигурации

![](/pics/m5_dhcp_server_advance.png)

### DHCP-клиент

* Позволяет Ethernet-подобным интерфейсам запрашивать IP-адрес.
  * Удаленный DHCP-сервер будет предоставлять:
    * Адрес
    * Маска
    * Шлюз по умолчанию
    * Два DNS-сервера (если удаленный DHCP-сервер настроен таким образом)
  * DHCP-клиент предоставляет настраиваемые параметры:
    * Имя хоста
    * Clientid (в виде его MAC-адреса)
* Обычно используется на интерфейсах, обращенных к Интернету, например


#### Синтаксис DHCP-клиента

* Настройка интерфейса DHCP-клиента
  * `/ip dhcp-client add interface=ether5 dhcp-options=clientid,hostname`
* Просмотр и включение DHCP-клиента
  * `/ip dhcp-client print`
  * `/ip dhcp-client enable numbers=1`
* Просмотр адресов DHCP-клиентов
  * `/ip address print`

#### Управление арендой

* Раздел "/ip dhcp-server lease" содержит информацию о DHCP-клиентах и арендах
* Показывает динамическую и статическую аренду.
* Может превратить динамическую аренду в статическую
  - Может быть очень полезно, когда устройство должно получать один и тот же IP-адрес
  - Осторожно! Если вы замените сетевую карту - она получит новый адрес
* DHCP-сервер можно заставить работать только со статическими адресами
* Клиенты будут получать только предварительно настроенные IP-адреса
* **Оцените свою ситуацию и необходимость в этом прежде, чем делать таким образом. Это потребует много работы для крупных сетей**

##### Синтаксис управления арендой

* Просмотр аренд DHCP
  * `/ip dhcp-server lease print`
  * `/ip dhcp-server lease print detail` \(_gives more_ _detailed information_\)
* Чтобы сделать динамический IP-адрес - статическим
  * `/ip dhcp-server lease make-static numbers=0`
* Изменение назначенного IP-адреса предыдущей записи
  * `/ip dhcp-server lease set address=192.168.3.100 numbers=0`

## Инструменты RouterOS

### E-mail

* Инструмент, позволяющий отправлять электронную почту с маршрутизатора
* Его, например, можно использовать, наряду с другими инструментами, для отправки администратору сети регулярных резервных копий конфигурации
* Путь к инструменту в CLI
  * /tools e-mail

#### E-mail, пример

* Настройка SMTP-сервера
  - `/tool e-mail set address=172.31.2.1 from=mymail@gmail.com last-status=succeeded password=never123! \`
  - `port=587 start-tls=yes user=mymail@gmail.com`
* Отправить конфигурационный файл по электронной почте
  - `/export file=export`
  - `/tool e-mail send to=home@gmail.com subject="$[/system identity get name] export"\`
  - `body="$\[/system clock get date] configuration file" file=export.rsc`

### Netwatch

* Инструмент, позволяющий контролировать состояние сетевых устройств
* Для каждой записи вы можете указать
  - IP-адрес
  - Интервал пинга
  - Скрипты подъема и/или падения
* ОЧЕНЬ полезно
  - Будьте в курсе сетевых сбоев
  - Автоматизировать изменение шлюза по умолчанию, например, в случае сбоя основного маршрутизатора
  - Просто чтобы быстро увидеть, что происходит
- Все, что вы можете придумать, чтобы упростить и ускорить вашу работу (и заставить вас выглядеть эффективно!)

### Ping

* Базовый инструмент связи, использующий эхо-сообщения ICMP для определения доступности удаленного хоста и задержки обратного хода.
* Один из первых инструментов для устранения неполадок. Если он пингует - хост жив _(с точки зрения сети)_
* Используйте его с другими инструментами при устранении неполадок. Это не самый лучший инструмент, но хорошее начало.

#### Синтаксис Ping

* CLI

```
[admin@MikroAC1] > ping www.mikrotik.com
HOST                     SIZE TTL TIME STATUS
159.148.147.196             56 50 163ms
159.148.147.196             56 50 156ms
159.148.147.196             56 50 156ms
159.148.147.196             56 50 160ms
  sent=4 received=4 packet-loss=0% min-rtt=156ms avg-rtt=158ms max-rtt=163ms


You’ll need to hit “CTRL-C” to stop the ping
```

### Traceroute

* Используется для отображения всех маршрутизаторов, пройденных до места назначения
* Указывает на задержку при достижении каждого маршрутизатора в пути по достижению пункта назначения
* Хорош для обнаружения сбоя или медленного узла
* CLI

```
– /tools traceroute www.mikrotik.com
– [admin@GateWay] > tool traceroute www.mikrotik.com
– # ADDRESS             LOSS  SENT  LAST AVG BEST WORST STD-DEV STATUS
– 1 89.179.48.140       0%    20  6.7ms  4.5 1.7 11.6 2.2
– 2 89.179.48.166       0%    20  5ms    5.3 2.7 10.6 2.4
– 3 213.33.229.109      0%    20  5ms    6.9 1.4 35.9 8.1
– 4 213.221.4.132       0%    20  31.6ms 34.5 30.9 39.5 2.1
– 5 195.13.224.86       0%    19  30.8ms 33.4 30.4 39.4 2.4
– 6               100% 19 timeout
– 7 159.148.147.196     0%    19  33.4ms 32.9 30.9 37.1 1.7
```

### Profiler (загрузка ЦП)

* Инструмент, показывающий загрузку процессора
* Показывает процессы и их нагрузку на ЦП
* Примечание: “**idle**” (бездействие) - это не процесс. Это означает именно это; процент неиспользуемого процессора

* CLI

```
– /tool profile
– [admin@MikroAC1] > /tool profile
– NAME        CPU   USAGE
– console     all   0%
– flash       all   0%
– networking  all   0%
– radius      all   0%
– management  all   0.5%
– telnet      all   0.5%
– idle        all   99%
– profiling   all   0%
– unclassified  all 0%
– -- [Q quit|D dump|C-z continue]
```

### Система идентификации

* Хотя это не инструмент, важно установить идентичность системы
  - Вы не можете управлять 100 маршрутизаторами, которые все имеют имя "MikroTik". Это делает устранение неполадок практически невозможным.
  - После установки он значительно упростит идентификацию маршрутизатора, с которым вы работаете.
* Синтаксис
  - `/system identity print` _(показать текущее имя)_
  - `/system identity set name=my-router` (задать имя маршрутизатора)

## Обращение в службу поддержки Mikrotik

### Supout.rif

* Supout.rif это файл поддержки, используемый для отладки RouterOS и помогающий персоналу службы поддержки Mikrotik быстрее решать проблемы
* Синтаксис
  - CLI: `/system sup-output`
* После генерации файл "supout.rif" будет найден в File List

![](/pics/m5_supout_rif.jpeg)

### Supout.rif Viewer

* Чтобы получить доступ к "supout.rif viewer", необходимо иметь доступ к учетной записи Mikrotik
  - У вас должен быть аккаунт _(это хорошая идея, чтобы иметь его в любом случае)_

![](/pics/m5_supout_account.png)

* Первые шаги - найти и загрузить созданный файл.
* Начните просматривать все аспекты вашей конфигурации.
  - Просмотр по умолчанию - “ресурсы”

![](/pics/m5_supout_resource.png)

### Autosupout.rif

* Файл может быть сгенерирован автоматически при программном сбое (напр. kernel panic или the system becomes unresponsive for a minute)
* Сделано через watchdog (сторожевого пса) (системно)

### Системное логирование и журналы отладки

* Логирование важно для обеспечения истории событий маршрутизатора (постоянной или нет)
* Самый простой способ просмотра журналов - через окно "log" (Меню).
* Эквивалент CLI:
  - /log print

![](/pics/m5_log.png)

#### Системный журнал

* Действия
  - Задачи, которые маршрутизатор будет выполнять с определенными событиями
  - Правила указывающие маршрутизатору, какое "действие" предпринять
  - Существует пять типов действий, поэтому вы можете иметь очень гибкую систему ведения журнала
* Предложения
  - Вы должны сначала определить новые "действия", поскольку пользовательские действия не будут доступны вашим "правилам", пока они не будут созданы

* Действия, примеры

```
[admin@MikroAC5] > /system logging action print
Flags: * - default
# NAME              TARGET REMOTE
0 * memory          memory
1 * disk            disk
2 * echo            echo
3 * remote          remote 172.16.1.105
4 webproxy          remote 172.16.1.105
5 firewallJournal   remote 172.16.1.105
```
* Правила
  - Они указывают RouterOS, какое "действие" предпринять с данным событием (которое называется "темой")
  - Вы можете иметь несколько правил для одной и той же темы, каждое правило выполняет различное "действие"
  - Вы можете иметь одно правило с двумя или более темами, выполняя "действие"
  - Добавить правило просто: выберите одну или несколько тем, назовите правило, выберите одно действие. (Именно поэтому предлагается сначала создать действия)

* Правила, пример

```
[admin@MikroAC5] > /system logging print
Flags: X - disabled, I - invalid, * - default
# TOPICS          ACTION          PREFIX
0 * info          memory          INF
!firewall
1 * error         memory          ERR
2 * warning       memory          WRN
3 * critical      memory          CRT
4 firewall        memory          FW
5 firewall        firewallJournal FW
6 info            remote          INF
  !firewall
7 error           remote          ERR
8 warning         remote          WRN
9 critical        remote          CRT
10 X snmp         memory          SNMP
11 web-proxy      webproxy        PROXY
  !debug
```

#### Синтаксис системного журнала

* Просмотр правил
  - `/system logging print`
* Просмотр действий
  - `/system logging action print`
* Хранить сообщения брандмауэра на сервере syslog
  - `/system logging action`
  - `add bsd-syslog=yes name=firewallJournal remote=172.16.1.105 src-address=10.5.5.5 syslog-facility=local5 target=remote`
* Создать правило для разделов брандмауэра, в котором будет использоваться предыдущее действие
  - `/system logging`
  - `add action=firewallJournal prefix=FW topics=firewall`

#### Куда отправляются журналы

* Как указано в разделе "actions"(действия), журналы можно найти в пяти местах:
  - Диск: Жесткий диск на маршрутизаторе
  - Эхо: консоль маршрутизатора (если присутствует)
  - Электронная почта: предопределенная учетная запись электронной почты
  - Память: внутренняя память маршрутизатора (как показано в окне "log")
  - Удаленный syslog-сервер

#### Чтение конфигурации

* АКА "Сделайте это ясно(чисто)!”
* Неизвестность - ваш злейший враг. Держите ваши конфигурации ясными и читаемыми через **комментарии**, **имена** и **единообразие**
  - Комментарии: дайте простое описание предмету
  - Имена: сделайте его значимым
  - Единообразие: делайте все одинаково везде
* Зачем вам все это делать?
  - Для себя. В долгосрочной перспективе это упростит вашу работу и заставит вас выглядеть эффективным (снова)

* Пример

![](/pics/m5_configuration.png)

Сетевая диаграмма

* Хорошо нарисованная диаграмма - это обязательно! Даже если вы начнете со скромного начала, ваша сеть будет расти
* Определить все ключевые компоненты
* Держите диаграмму в актуальном состоянии
* Это основной инструмент устранения неполадок
  - Используйте его для выявления потенциальных проблемных мест
  - Используя инструменты, отмеченные в этом модуле (ping, traceroute), запишите возможные проблемы

* Пример
  - Все порты помечены, даже доступные
  - Идентифицируются устройства
  - Ревизия \# является актуальной

![](/pics/m5_network_diagram.png)

Время для практических занятий

**Конец 5 модуля**

## Лабораторка

* Цели лабораторки
  - Практика ARP концепций, показанных в этом модуле
  - Добавление DHCP (клиент и сервер) функциональных возможностей маршрутизатора
  - Использование различных инструментов для устранения неполадок

Лабораторка: Установка

![](/pics/m5_lab_setup.jpeg)

### Лабораторка: шаг 1

* Display the ARP entries of your router
  * Identify each entry
  * Based on the network diagram, does it make sense? Compare with the port the MAC address was learned
* Validate in which ARP mode your interfaces are
* Add a fake MAC address as if it was learned from the bridge named “LAN”

### Лабораторка: шаг 2

* Add a DHCP client on WLAN1 interface
* Ask the trainer to make a static reservation on his DHCP server. The fourth digit of your IP address must match your pod
* Give the trainer your wlan’s interface MAC address since your router hasn’t been named yet
* Delete your static IP address
* Renew your DHCP client address
* What’s the final address?

### Лабораторка: шаг 3

* Cleanup
  * When creating the DHCP client, the option “Add default route” was set to yes. This means that the DHCP client gets a default route dynamically
  * Display your routes. What do you see for the default route?
  * What should be done now to cleanup this table?

### Лабораторка: шаг 4

* Set up DHCP server for the computers of the “LAN” bridge
  * Create the configuration that will ensure
    * that clients will get an IP address
    * The DNS server is at the same address as the default gateway \(your router\)
  * Reconfigure your computer so that it receives an IP address from your router
  * Configure your router so that your computer always gets the .20X address \(where X is your pod’s address\)
  * What do you have to do to get that address?

### Лабораторка: шаг 5

* Cleanup
  * Add a comment to your static address to indicate what the reservation is for
  * In the DHCP tab of DHCP Server, give a meaningful name to the DHCP server \(currently named dhcp 1\)

### Лабораторка: шаг 6

* E-mail setup
  * Configure your e-mail settings as to allow you to send e-mails to a personal e-mail address.
    * You can use your own e-mail account to test this out
  * Test your configuration with a test e-mail

### Лабораторка: шаг 7

* Netwatch
  * Use this tool to monitor a test node supplied by the trainer
  * To speed things up, configure monitoring interval at 30 seconds

### Лабораторка: шаг 8

* Netwatch
  * Use these scripts:

**Down**

```text
/tool e-mail send to=“<your-e-mail-address>" subject="$[/system identity get name] Netwatch status" \
body="$[/system clock get date] $[/system clock get time] Node down."
```

**Up**

```text
/tool e-mail send to="<your-e-mail-address>" subject="$[/system identity get name] Netwatch status" \
body="$[/system clock get date] $[/system clock get time] Node up."
```

![](/pics/m5_lab_netwatch.jpeg)

### Лабораторка: шаг 9

* Netwatch
  * Turn off the test node. Verify that you receive an e- mail indicating the change of status. It should look something like this

![](/pics/m5_lab_netwatch_status.png)

### Лабораторка: шаг 10

* Ping
  * Use the ping tool to validate that the test node answers ICMP echo packets
* Traceroute
  * Use the traceroute tool to see which hops are between you and the test node. Validate that what you see is what is in the class’ network diagram

### Лабораторка: шаг 11

* Profiler
  * Launch the profiling tool and view the various processes running on your router
  * What does the highest percentage represent?
    * Sort tasks by “usage”

### Лабораторка: шаг 12

* Supout.rif
  * Create a supout.rif file. Where is it?
  * Upload it and take a look at the various sections of your router as viewed by the supout.rif viewer. It’s interesting to see that such a small file can go a long way to help Mikrotik help you.
  * Important note : If you don't have a MikroTik account, please create one now as it is required to take the certification exam!!

### Лабораторка: шаг 13

* Logging
  * Create an action:
    * Type is “memory”
  * Create a rule:
    * topics “e-mail” and “debug”
    * Action “action1”
  * Open the “log” window
  * Go back to the e-mail tool and send yourself a test e-mail. What do you see in the log window?

### Лабораторка: шаг 14

* Cleaning up our configuration
  * Go to the logging window, actions tab and rename “action1” to “E-mail-Debug”
  * What happened? Rename “action1” to “EmailDebug”
  * Switch back to the rules tab. What do you notice about the “e-mail,debug” entry?
* Do a binary backup of your configuration that respects the previous file name structure from the previous module

### Лабораторка: шаг 15

* Lastly, rename your router so that:
  * it is named after your pod
  * The first letter is capitalized
* Create two backups named Module5-Pod_x_
  * one must be binary
  * one must be an export


File: /m6-firewall.md
# M6 Firewall

## Принципы брандмауэра (фаерволла)

* Брандмауэр - это служба, которая пропускает или блокирует пакеты данных, идущие к нему или через него на основе определенных пользователем правил.
* Брандмауэр действует как барьер между двумя сетями.
* Общий пример - ваша локальная сеть (доверенная) и Интернет (не доверенная).

### Как работает брандмауэр

* Брандмауэр работает по правилам. Они состоят из двух частей
  - Совпадение: _условия, которые нужны для совпадения_
  - Действие: _что я буду делать, когда у меня будет совпадение_
* Сопоставитель смотрит на такие параметры, как:
  - MAC-адрес источника
  - IP-адреса (сеть или список) и типы адресов (широковещательный, локальный, многоадресный, одноадресный)
  - Порт или диапазон портов
  - Протокол
  - Параметры протокола (поля типа и кода ICMP, флаги TCP, параметры IP)
  - Интерфейс: пакет приходит от или через
  * Байт DSCP
  * _**И многое другое…**_

### Потоки пакетов

* MikroTik создал диаграммы потока пакетов, чтобы помочь нам в создании более продвинутых конфигураций.
* Хорошо быть знакомым с ними, чтобы знать, что происходит с пакетами и в каком порядке
* Для этого курса мы будем держать его простым

* Общие диаграммы

![](/pics/m6_diagram_1.jpeg)

![](/pics/m6_diagram_2.jpeg)

![](/pics/m6_diagram_3.jpeg)

#### Потоки пакетов, пример*

* Сложно? Добро пожаловать в клуб!
* Этот следующий пример может помочь проиллюстрировать простой поток пакетов: Pinging a (несуществующий узел) на интерфейсе локальной сети маршрутизатора через его интерфейс WAN
  - IP узла, выполняющего пинг : 172.16.2.100
  - IP-адрес узла, который пингуется : 192.168.3.2
  - IP WAN маршрутизатора (ether1): 192.168.0.3

**Ping in**

```text
===PREROUTING===
Mangle-prerouting prerouting: in:ether1 out:(none), src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0),
172.16.2.100->192.168.3.2, len 60
dstnat dstnat: in:ether1 out:(none), src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0), 172.16.2.100-
>192.168.3.2, len 60
===FORWARD===
Mangle-forward forward: in:ether1 out:Bridge-PC, src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0),
172.16.2.100->192.168.3.2, len 60
Filter-forward forward: in:ether1 out:Bridge-PC, src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0),
172.16.2.100->192.168.3.2, len 60
===POSTROUTING===
Mangle-postrouting postrouting: in:(none) out:Bridge-PC, src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0),
172.16.2.100->192.168.3.2, len 60
srcnat srcnat: in:(none) out:Bridge-PC, src-mac d4:ca:6d:33:b5:ef, proto ICMP (type 8, code 0), 172.16.2.100-
>192.168.3.2, len 60
```

**Reply out**

```text
===OUTPUT===
Mangle-output output: in:(none) out:ether1, proto ICMP (type 3, code 1), 192.168.0.3->172.16.2.100, len 88
Filter-output output: in:(none) out:ether1, proto ICMP (type 3, code 1), 192.168.0.3->172.16.2.100, len 88
===POSTROUTING===
Mangle-postrouting postrouting: in:(none) out:ether1, proto ICMP (type 3, code 1), 192.168.0.3->172.16.2.100, len 88
```

#### Потоки пакетов, объяснение примера

```text
/ip firewall filter
add action=log chain=input log-prefix=Filter-input protocol=icmp
add action=log chain=output log-prefix=Filter-output protocol=icmp
add action=log chain=forward log-prefix=Filter-forward protocol=icmp
/ip firewall mangle
add action=log chain=prerouting log-prefix=Mangle-prerouting protocol=icmp
add action=log chain=output log-prefix=Mangle-output protocol=icmp
add action=log chain=input log-prefix=Mangle-input protocol=icmp
add action=log chain=forward log-prefix=Mangle-forward protocol=icmp
add action=log chain=postrouting log-prefix=Mangle-postrouting protocol=icmp
/ip firewall nat
add action=log chain=srcnat log-prefix=srcnat protocol=icmp
add action=log chain=dstnat log-prefix=dstnat protocol=icmp
```

#### Отслеживание соединений и состояний

* Отслеживание соединений управляет информацией обо всех активных соединениях.
* Прежде чем создавать фильтры брандмауэра (или правила), полезно знать какой трафик проходит через ваш маршрутизатор. Отслеживание соединений покажет вам именно это.

```
1 ospf 172.16.0.6 224.0.0.5 5m49s
2 SA tcp 172.16.2.100:49164 172.16.9.254:445 established 23h42m51s
3 SA tcp 172.16.2.122:61739 206.53.159.211:443 established 23h44m8s
4 SA tcp 172.16.2.130:58171 17.149.36.108:443 established 23h43m41s
5 SA gre 172.16.0.254 172.16.0.1 4h44m11s
6 SA udp 172.16.0.254:4569 209.217.98.158:4569 13m9s
7 SA tcp 172.16.2.130:58174 173.252.103.16:443 established 23h42m40s
8 SA tcp 172.16.2.140:52032 69.171.235.48:443 established 23h43m27s
9 SA tcp 172.16.2.107:47318 173.252.79.23:443 established 23h43m26s
10 SA tcp 172.16.2.102:57632 173.252.102.241:443 established 23h44m15s
11 ospf 172.16.0.5 224.0.0.5 5m49s
12 SA tcp 172.16.2.102:56774 65.54.167.16:12350 established 23h35m28s
13 SA tcp 172.16.2.102:56960 173.194.76.125:5222 established 23h43m57s
14 SA tcp 172.16.0.254:37467 172.16.0.1:1723 established 4h44m11s
15 SA tcp 172.16.2.107:39374 79.125.114.47:5223 established 23h29m1s
```

* Если вы отключите отслеживание по какой-либо причине, следующие функции не будут работать:
  - NAT
  - Брандмауэр
    - connection-bytes connection-mark
    - connection-type connection-state
    - connection-limit connection-rate
    - layer7-protocol p2p
    - new-connection-mark tarpit
  - p2p matching in simple queues
* Прежде чем отключить отслеживание подключений, удостоверьтесь в том, какую цель вы хотите достичь!

Состояния соединения являются _(предполагая, что клиент-A инициирует соединение с клиентом-B)_:

| Состояние | Описание |
| :-------- | :------- |
| Established | Устанавливается сеанс TCP для удаленного хоста, обеспечивающий открытое соединение, в котором можно обмениваться данными |
| Time-wait | Время, потраченное на ожидание, чтобы убедиться, что удаленный хост получил подтверждение запроса на завершение соединения (после "close") |
| Close | Представляет собой ожидание запроса на завершение соединения от удаленного компьютера. |
| Syn-sent | Клиент-A ожидает соответствующего запроса на соединение после его отправки |
| Syn-received | Клиент-B ожидает подтверждения запроса на соединение после получения и отправки запроса на соединение. |

* Использование отслеживания соединений позволяет отслеживать соединения UDP, даже если UDP не имеет состояния. Таким образом, брандмауэр MikroTik может фильтровать по UDP "состояниям".

## Структура: цепочки и действия

* Цепочка - это группировка правил, основанная на одних и тех же критериях. Существует три цепочки по умолчанию, основанные на предопределенных критериях.
  - Input: _Трафик идущий к маршрутизатору_
  - Forward: _Трафик идущий через маршрутизатор_
  - Output: _Трафик, исходящий от маршрутизатора_

* Вы можете иметь пользовательские цепочки, основанные на пользовательских критериях. Например:
  - _Весь icmp-трафик_
  - _Трафик приходящий из Ether2 и идущий к интерфейсу моста "LAN"_

* Определенные пользователем цепочки создаются путем выбора желаемых "сопоставлений" и выбора действия "прыжок". Вы дадите определяемой пользователем цепочке имя в поле "jump target" (цель прыжка).
  - После этого вы можете начать создавать правила фильтрации, используя новую цепочку, введя ее в поле "Chain" нового фильтра брандмауэра.
* Действие определяет, что будет делать фильтр, когда пакеты будут сопоставлены с ним.
* Пакеты последовательно проверяются на соответствие существующим правилам в текущей цепочке брандмауэра до тех пор, пока не произойдет совпадение. Когда это происходит, это правило применяется.
* Знайте, что определенные действия могут потребовать или не потребовать дальнейшей обработки пакета.
* Другие действия могут потребовать дальнейшей обработки пакета в другой цепочке. Мы увидим это на последующих страницах.

### Фильтры брандмауэра в действии

Основная философия безопасности

* Вы можете подходить к безопасности по-разному.
  - Мы доверяем внутреннему миру, правила влияют на то, что приходит извне.
  - Мы блокируем все и разрешаем то, о чем договариваемся.
  - Мы разрешаем все и блокируем то, что, как мы знаем, подозрительно.

Основные советы и рекомендации

* Перед настройкой или изменением правил активируйте "safe mode".
* После настройки или изменения правил протестируйте их с помощью такого инструмента, как ShieldsUP.(https://www.grc.com/x/ne.dll?bh0bkyd2)
  - Это даст вам отчет о слабых сторонах.
* Прежде чем вы начнете, установите политику.
* Запишите простым текстом на своем языке основные правила, которые вам нужны.
  - Как только вы поймете их и согласитесь с ними, введите их в маршрутизатор.
* Постепенно добавляйте другие правила, как только вы будете удовлетворены основными из них.
  - Если вы новичок в безопасности, это не поможет вам стрелять во всех направлениях. Делайте основы, но делайте их хорошо.
  - Просто не ждите слишком долго, чтобы добавить следующие правила. Одно дело - хорошо работать, но совсем другое - оставлять дыры открытыми, потому что вы хотите проверить первые правила.
* Это хорошая идея, чтобы закончить ваши цепочки правилом "поймать все" и посмотреть, что вы, возможно, пропустили.
* Вам понадобятся два правила "поймать все", одно для "регистрации" и одно для "отбрасывания" несовпадающего трафика. Оба должны быть основаны на одних и тех же сопоставлениях, чтобы быть полезными для вас.
* Как только вы увидите, что достигает правил "catch-all", вы можете добавить новые правила, основанные на желаемом поведении брандмауэра.

### Фильтр соответствий

* Перед выполнением "действия" над пакетом его необходимо идентифицировать.
* Совпадений много!

![](/pics/m6_firewall_rule.png)

### Действия фильтра

* Как только пакет сопоставлен с правилом, к нему будет применено действие.
* Фильтры брандмауэра MikroTik имеют 10 действий.

|            |                      |
| :--------- | :------------------- |
| **Accept** | Принимает пакет. Пакет не передается следующему правилу брандмауэра. |
| **Add-dst-to-address-list** | Добавляет адрес получателя в список адресов, указанный параметром address-list. Пакет передается следующему правилу брандмауэра. |
| **Add-src-to-address-list** | Добавить адрес источника в список адресов, указанный параметром address-list. Пакет передается следующему правилу брандмауэра. |
| **Drop** | Молча отбрасывает пакет. Пакет не передается следующему правилу брандмауэра. |
| **Jump** | Перейти к пользовательской цепочке, заданной значением параметра jump-target. Пакет передается следующему правилу брандмауэра (в пользовательской цепочке). |
| **Log** | Добавьте сообщение в системный журнал, содержащее следующие данные: _**in-interface**_, _**out-interface**_, _**src-mac**_, _**protocol**_, _**src-ip:port->dst-ip:port**_ and _**length of the packet**_ (длина пакета). Пакет передается в следующее правило брандмауэра. |
| **Passthrough** | Проигнорируйте это правило и перейдите к следующему (полезно для статистики). |
| **Reject** | Отбросить пакет и отправить сообщение ICMP reject. Пакет не передается следующему правилу брандмауэра. |
| **Return** | Передать управление обратно в цепочку, откуда произошел прыжок. Пакет передается следующему правилу брандмауэра (в исходной цепочке, если не было предыдущего совпадения для остановки анализа пакетов). |
| **Tarpit** | Захват и удержание TCP-соединений (ответы с помощью SYN/ACK на входящий пакет TCP SYN). Пакет не передается следующему правилу брандмауэра. |

**Защита вашего маршрутизатора (вход)**

* Входная цепочка смотрит на трафик, направленный на маршрутизатор.
* Правила, которые вы добавляете во входную цепочку, должны предотвращать доступ хакеров к маршрутизатору, не мешая ему выполнять свою работу.

**Защита вашего маршрутизатора (пример)**

* Ниже приведены предложения!
  - Предположим, что _ether01_ подключен к WAN (ненадежной сети), и мы используем политику "доверяй внутреннему".
    - Принимайте ICMP эхо-ответы (_Возможно, вы захотите проверить связь с сервером в Интернете. Это было бы полезно для вас, чтобы получать ответы!_)
    - Отбрасывайте эхо-запросы icmp (_Вы не хотите чтобы другие пинговали вас. Оставайтесь под радаром!_)
    - Принимайте весь "established" и "related" входящий трафик (_Вам понадобятся ответы на все запросы маршрутизатора, такие как запросы NTP и DNS_)
    - Отбрасывайте весь "invalid" входящий трафик (_Когда маршрутизатор получает то, что он не запрашивал_)
    - Протоколируйте остальной входящий трафик (_Я пропустил что-нибудь важное?_)
    - Отбрасывайте остальной входящий трафик (_Я хочу быть в безопасности!_)

**Защита ваших клиентов (forward)**

* Как указывалось ранее, цепочка forward смотрит на трафик, проходящий через маршрутизатор.
* Правила, которые вы добавляете в цепочку forward, должны препятствовать проникновению хакеров в вашу "безопасную" сеть, не мешая вам выполнять свою работу.

**Защита ваших клиентов (пример)**

* Ниже приведены предложения!
  - Опять же, предположим, что _ether01_ подключен к WAN (ненадежной сети), и мы используем политику "доверяй внутреннему".
    - Принимаем все "established" и "related" проходящий трафик (_вам понадобятся ответы на все, что вы запросили, например HTTP и запросы электронной почты_)
    - Отбрасываем весь "invalid" проходящий трафик (_Все, что вы получаете, вы не запрашивали_)
    - Протоколируем остаток прямого трафика (_Я пропустил что-нибудь важное?_)
    - Отбросим остальную часть проходящего трафика (_Я хочу быть в безопасности!_)

**Как это выглядит в конце концов**

![](/pics/m6_firewall.jpeg)

**Синтаксис фильтра брандмауэра**

* Просмотр существующих правил фильтрации
  -/ip firewall filter print _(производит более четкий, читаемый вывод)_
  - /ip firewall filter export _(показывает полный синтаксис)_

* Создание различных правил _(от /ip firewall filter)_
  - add chain=input comment="Established-Related (in)" connection-state=established in-interface=ether01
  - add chain=forward comment="Established-Related (fwd)" connection-state=established in-interface=ether01
  - add action=log chain=input comment="===CATCH-ALL==" in-interface=ether01 log-prefix="CATCH-ALL(in)"
  - add action=drop chain=input in-interface=ether01
  - add action=add-dst-to-address-list address-list=temp-list address-list-timeout=3d1h1m1s chain=input protocol=tcp src-address=172.16.2.0/24

## Основы адрес-листа

* Списки адресов - это группы IP-адресов.
* Их можно использовать для упрощения правил фильтрации.
  - Например, вы можете создать 100 правил для блокировки 100 адресов, или!!
  - Вы можете создать одну группу с этими 100 адресами и создать только одно правило фильтра.
* Группы (списки адресов) могут представлять
  - IT-администраторы с особыми правами
  - Хакеры
  - Что-нибудь еще ты можешь придумать…

* Их можно использовать в фильтрах брандмауэра, средствах mangle и NAT.
* Создание адрес-листов может быть автоматизировано с помощью действия **add-src-to-address-list** или **add-dst-to-address-list** в фильтре брандмауэра, mangle или NAT объектов.
  - Это отличный способ автоматической блокировки IP-адресов без необходимости вводить их по одному
  - Пример: `add action=add-src-to-address-list address-list=BLACKLIST chain=input comment=psd in-interface=ether1-Internet psd=21,3s,3,1`

### Синтаксис адрес-листов

* Просмотр существующих списков адресов
  - /ip firewall address-list print
* Создание списка постоянных адресов
  - /ip firewall address-list add address=1.2.3.4 list=hackers
* Создание списка адресов с помощью правила фильтра брандмауэра
  - /ip firewall filter add action=add-dst-to-address-list address-list=temp-list address-list-timeout=3d1h1m1s chain=input protocol=tcp src-address=172.16.2.0/24
  - /ip firewall nat add action=add-src-to-address-list address-list=NAT-AL chain=srcnat
  - /ip firewall mangle add action=add-dst-to-address-list address-list=DST-AL address-list-timeout=10m chain=prerouting protocol=tcp

## NAT

### Source NAT

* Преобразование сетевых адресов (NAT) позволяет хостам использовать один набор IP-адресов на стороне локальной сети и другой набор IP-адресов при доступе к внешним сетям.
* Source NAT преобразует частные IP-адреса (в локальной сети) в публичные IP-адреса при доступе к интернету. Обратное делается для возвращаемого трафика. Это иногда называют "скрытием" вашего адресного пространства (вашей сети) за адресом, предоставленным провайдером.

#### Маскарадинг и действие src-nat

* Первая цепочка для NATинга - "srcnat". Она используется трафиком, выходящим из маршрутизатора.
* Как и фильтры брандмауэра, правила NAT имеют множество свойств и действий (_13 действий!_).
* Первое, и самое основное из правил NAT, использует только действие "masquerade".
* Masquerade заменяет исходный IP-адрес в пакетах на другой, определенный средством маршрутизации.

- Как правило, IP-адрес источника пакетов, идущих в Интернет, будет заменен адресом внешнего (WAN) интерфейса. Это необходимо для возврата трафика на "_найти дорогу домой_".

* Действие "src-nat" заменяет исходный IP-адрес и порт пакетов на указанные администратором сети.
  - **Пример использования**: две компании (Альфа и Бета) объединились, и обе используют одно и то же адресное пространство (напр. 172.16.0.0/16). Они настраивают сегмент, используя в качестве буфера совершенно другое адресное пространство, и обе сети будут требовать правила src-nat и dst-nat.

### Destination NAT

Действие Dst-nat и перенаправления

* "Dst-nat" - это действие, используемое с цепочкой "dstnat" для перенаправления входящего трафика на другой IP-адрес или порт.
  - **Пример использования**: в нашем предыдущем примере Альфа и Бета мы видим, что правила dst-nat потребуются для повторного преобразования "буферного IP-адреса" в адрес сервера Бета.
* "Redirect" меняет порт назначения, указанный "до порта" маршрутизатора.
  - **Пример использования**: весь http-трафик (TCP, порт 80) должен быть направлен в службу веб-прокси на TCP-порт 8080.
Dst-nat and redirection action

### Синтаксис NAT

* Source NAT (от /ip firewall nat)
  - Добавьте правило маскарадинга
    - add action=masquerade chain=srcnat
  - Изменение исходного IP-адреса
    - add chain=srcnat src-address=192.168.0.109 action=src-nat to-addresses=10.5.8.200
* Destination NAT
  - Перенаправить весь веб-трафик (TCP, порт 80) на веб-прокси маршрутизатора на порту 8080
    - add action=redirect chain=dstnat dst-port=80 protocol=tcp to-ports=8080

Время для практических упражнений

**Конец 6 модуля**

## Лабораторка

* Цели лабораторки
  - Настройка основных правил брандмауэра
  - Настройка базового адрес-листа
  - Применение основных правил Source NAT и их проверка
  - Применение основных правил destination NAT и их проверка

Лабораторка: Установка

![](/pics/m6_lab_setup.jpeg)

Лабораторка: шаг 1

* Прежде чем перейти к правилам брандмауэра, мы протестируем правило NAT: Masquerading
  - Посмотрите в свои настройки, чтобы увидеть, есть ли у вас правило NAT "masquerading". Создайте его, если это ещё не сделано, НО оставьте его отключенным. Если оно у вас уже есть убедитесь что оно отключено
  - Запустите Winbox и подключитесь к соседнему модулю
  - В разделе IP FIREWALL CONNECTION просмотрите активные соединения. Что Вы видите? Почему?
  - Установите параметр конфигурации, который позволит вам отслеживать соединения. Проверьте результаты.
  - Включите правило masquerade NAT и снова проверьте отслеживание соединений.

Лабораторка: шаг 2

* Let's make things more interesting by adding filter rules. Apply the following rules to incoming traffic on your WAN interface.
  - Accept icmp echo replies
  - Drop icmp echo requests
  - Accept all "established" and "related" input and forward traffic
  - Drop all "invalid" input and forward traffic
  - Log the rest of input and forward traffic
  - Drop the rest of input and forward traffic
  - Add meaningful comments to all rules.
  - Do the same for the "log" rules' prefixes.

Лабораторка: шаг 3

* Now that you have rules, check your logs. Look at the messages and their format
* Seeing what you see now, do you think troubleshooting connection problems would be easier? Why?

Лабораторка: шаг 4

* Create Address Lists representing all pods
* Use the following format:
  - Name : Pod1
  - Address : &lt;_network/mask_&gt; of the LAN
  - Name : Pod1
  - Address : &lt;_IP_&gt; of the WAN interface

* Do so for all pods, even your own

Лабораторка: шаг 5

* Pods should be matched in pairs for the following tests
* Close your WinBox window and reopen it, connecting to your peer pod. What's happening?
* With one filter rule ONLY, allow all IP addresses from you peer pod to connect to your router with WinBox (TCP, 8291)
  - Make sure that it's in the right spot so that it works
  - And DON'T forget comments!

Лабораторка: шаг 6

* To test port redirection, we'll need to make a small change to the IP SERVICES of your pod.
  - In the IP Services section, change the WinBox port to 8111.

Лабораторка: шаг 7

* Close and reopen the WinBox interface without adding any special parameters. What result do you get?
* Log into the WinBox using port 8111.
* Create a dst-nat rule with a redirect action to port 8111 on all TCP port 8291 traffic.
* Close and reopen WinBox without the port after the IP address. Does it work now?
* Log into you peer pod's router. What's happening?

Лабораторка: шаг 8

* Return the WinBox port to it's normal value of 8291.
* Disable (don't delete) the dstnat rule of "redirect".
* Close WinBox and validate that you can log into your router and your peer's router normally.

Лабораторка: шаг 9

* Create a dst-nat rule with a redirect action to port 8291 on all TCP port 1313 traffic coming into the WAN port.
* Open WinBox and log into your router using port 1313.
* Open WinBox and log into your peer's router using port 1313.
* Explain the different results.

Лабораторка: шаг 10

* Do an export AND a binary backup under the file name module6-pod_x_.


File: /m7-qos.md
# M7 QoS

## Простая очередь

### Введение

* QoS (quality of service) - это искусство управления ресурсами полосы пропускания, а не просто "слепое" ограничение полосы пропускания определенными узлами.
* QoS может определять приоритетность трафика на основе метрик. Полезно для
  - Критически важных приложений
  - Чувствительному трафику, такой как голосовые и видеопотоки
* Простые очереди-это... простой ... способ ограничить пропускную способность до
  - Загрузки клиента (исходящей)
  - Закачки клиента (входящей)
  - Совокупно для клиента (загрузка и закачка)

### Цель

* Цель, к которой применяется простая очередь
* Цель должна быть определена. Это может быть
  - IP-адрес
  - Подсеть
  - Взаимодействие

* Порядок очередей очень важен. Каждый пакет должен пройти через каждую простую очередь, пока не произойдет совпадение

### Назначения

* IP-адрес, на который направлен целевой трафик, или
* Интерфейс, через который будет проходить целевой трафик;
* Не обязательно, как поле "цель"
* Может использоваться для ограничения очереди

### Max-limit и limit-at

* Параметр "max-limit" - это максимальная скорость передачи данных, которую может достичь цель
  - Рассматривается как MIR _(maximum information rate - максимальная скорость передачи)_
  - лучший вариант развития событий
* Параметр "limit-at" является гарантированной минимальной скоростью передачи данных для цели
  - Рассматривается как CIR _(committed information rate - совершенная скорость передачи информации)_
  - Худший вариант развития событий

### Bursting

* Bursting позволяет пользователям на короткое время получить большую пропускную способность, чем позволяет параметр "max-limit".
* Полезно для увеличения трафика, который не использует пропускную способность слишком часто. Например, HTTP. Получите быструю загрузку страницы, затем прочитайте ее за несколько секунд.

* Определения
  - **Burst-limit** : максимальная скорость передачи данных, в то время как burst разрешен.
  - **Burst-time** : время в секундах, в течение которого производится выборка. Это НЕ период, в течение которого трафик будет burst.
  - **Burst-threshold** : значение, которое определит, будет ли пользователю разрешен burst
  - **Average-rate** : среднее значение передачи данных, рассчитанное в 1/16 части "burst-time".
  - **Actual-rate** : Текущая (реальная) скорость передачи данных.

* Как это работает.
  - Bursting разрешен, пока **average-rate** остается ниже **burst-threshold**.
  - Bursting будет ограничен по скорости, указанной **burst-limit**.
  - **Average-rate** вычисляется путем усреднения 16 выборок (**actual-rate**) в течение **burst-time** секунд.
    - Если **burst-time** составляет 16 секунд, то образец берется каждую секунду.
    - Если **burst-time** составляет 8 секунд, то образец берется каждые ½ секунды. И так далее…
    - Когда начнется bursting, он будет разрешен на **longest-burst-time** секунд, что составляет
      - (burst-threshold x burst-time) / burst-limit.

![С burst-time 16 секунд](/pics/m7_bursting_16.png)

_С burst-time 16 секунд_

![С burst-time 8 секунд](/pics/m7_bursting_8.jpeg)

_С burst-time 8 секунд_

#### Синтаксис

* Простая очередь
  - `add max-limit=2M/2M name=queue1 target=192.168.3.0/24`
* The same queue with bursting
  - `add burst-limit=4M/4M burst-threshold=1500k/1500k burst-time=8s/8s limit-at=\`
  `1M/1M max-limit=2M/2M name=queue1 target=192.168.3.0/24`

**Подсказка**

* Возможно, вы заметили, что значки очереди меняют цвет в зависимости от использования. Цвет имеет значение.
  - Зеленый: 0-50% от используемой полосы пропускания
  - Желтый: 51-75% используется от доступной полосы пропускания используется
  - Красный: 76-100% от доступной полосы пропускания

## Одна простая очередь для всей сети (PCQ)

**Зачем иметь очередь на всех?**

* Per Connection Queue (PCQ) - это динамический способ формирования трафика для нескольких пользователей с использованием более простой конфигурации.
* Определите параметры, тогда каждый подпоток (например, определенные IP-адреса) будет иметь те же ограничения.

**Конфигурация Pcq-rate**

* Параметр **pcq-rate** ограничивает допустимую скорость передачи данных типа очереди.
* Классификатор - это то, что маршрутизатор проверяет, чтобы увидеть, как он будет применять это ограничение. Это может быть адрес источника или назначения, или порт источника или назначения. Таким образом, можно ограничить трафик пользователей или приложений (например, HTTP).

**Конфигурации Pcq-limit**

* Этот параметр измеряется в пакетах.

* Большое значение pcq-limit
  - Создаст больший буфер, таким образом уменьшая отброшенные пакеты
  - Увеличится задержка

* Малое значение pcq-limit
  - Увеличит количество отбрасываемых пакетов (так как буфер меньше) и заставит источник повторно отправить пакет, тем самым сократив задержку
  - Приведет к корректировке размера окна TCP, сообщая источнику уменьшить скорость передачи

* Какое значение я должен использовать? Здесь нет простого ответа.
  - Если часто начинается на основе "проб и ошибок" для каждого приложения
  - Если пользователи жалуются на задержку, уменьшите значение pcq-limit (длина очереди)
  - Если пакеты должны проходить через сложный брандмауэр, то вам, возможно, придется увеличить длину очереди, так как это может привести к задержкам
  - Быстрые интерфейсы (как Gig) требуют меньших очередей, поскольку они уменьшают задержки

### PCQ, пример

* Предположим, что у нас есть пользователи, совместно использующие ограниченное WAN-соединение. Мы дадим им следующие скорости передачи данных:
  - Скачивание: 2 Мбит/с
  - Отдача : 1 Мбит/с
  - WAN находится на ether1
  - Подсеть локальной сети 192.168.3.0/24

**/ip firewall mangle**
```
add action=mark-packet chain=forward new-packet-mark=client_upload \
  out-interface=ether1 src-address=192.168.3.0/24

add action=mark-packet chain=forward dst-address=192.168.3.0/24 \
  in-interface=ether1 new-packet-mark=client_download
```
**/queue type**
```
add kind=pcq name=PCQ_download pcq-classifier=dst-address pcq-rate=2M \
add kind=pcq name=PCQ\_upload pcq-classifier=src-address pcq-rate=1M
```
**queue tree**
```
add name=queue_upload packet-mark=client_upload parent=global queue=\
  PCQ_upload

add name=queue_download packet-mark=client_download parent=global queue=\
  PCQ_download
```

Наш пример объяснил

* **Mangle**: мы говорим маршрутизатору помечать пакеты с помощью "_**client_upload**_" или "_**client_download**_", в зависимости от того, если
  - Пакеты поступают из локальной сети и уходят из ether1 (upload - отдача) или,
  - Пакеты поступают из ether1 и отправляются в локальную сеть (загрузка).

* **Queue types**: мы определяем скорости передачи данных и классификаторы, используемые для дифференциации подпотоков (источник или назначение)
* **Queue tree**: комбинации, которые проверяются, чтобы увидеть, подходят ли пакеты для формирования трафика и что применять.
  - Например, в случае загруженного трафика мы проверяем входные и выходные интерфейсы (**global**) для пакетов с "**client_upload**" и применяем тип очереди "**PCQ_upload**".

## Мониторинг

Мониторинг траффика интерфейса

![](/pics/m7_monitor.jpeg)

Средство мониторинга трафика используется для запуска сценариев, когда трафик интерфейса достигает определенного порогового значения.

**Пример**

**/tool traffic-monitor**
```
add interface=ether1 name=TrafficMon1 on-event=script1 threshold=1500000 \
  traffic=received
```
**/system script**
```
add name=script1 policy=ftp,read,test,winbox,api source="/tool e-mail send to=\"\
  YOU@DOMAIN.CA\" subject=([/system identity get name] . \"Log \
  \" . [/system clock get date\]\) body=\"Hello World. You're going too fast!\""
```

### Torch

* Torch is a real-time traffic monitoring tool that can be used to monitor the traffic going through an interface.
* Although CLI is VERY flexible, the Torch interface in Winbox is very intuitive.

Torch, CLI

| \[admin@Pod3\] /tool&gt; torch interface=ether2 | port=winbox |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SRC-PORT | DST-PORT | TX | RX TX-PACKETS RX-PACKETS |  |  |  |  |
| 53217 | 8291 \(winbox\) | 12.0kbps | 4.7kbps | 7 | 6 |  |  |
|  |  | 12.0kbps | 4.7kbps | 7 | 6 |  |  |
| \[admin@Pod3\] /tool&gt; torch interface=ether2 | port=any |  |  |  |  |  |  |
| SRC-PORT | DST-PORT |  | TX | RX TX- |  |  |  |
| PACKETS RX-PACK |  |  |  |  |  |  |  |
| 53217 | 8291 \(winbox\) |  | 15.2kbps | 5.1kbps |  |  |  |
| 7 |  |  |  |  |  |  |  |
| 62414 | 53 | \(dns\) |  | 728bps | 600bps |  |  |
| 1 |  |  |  |  |  |  |  |
| 53538 | 80 | \(http\) |  | 92.8kbps | 5.3kbps |  |  |
| 12 |  |  |  |  |  |  |  |
| 62437 | 53 | \(dns\) |  | 744bps | 616bps |  |  |
| 1 |  |  |  |  |  |  |  |
| 53540 | 80 | \(http\) |  | 182.2kbps | 8.4kbps |  |  |
| 18 |  |  |  |  |  |  |  |
| 53541 | 80 | \(http\) |  | 191.1kbps | 8.6kbps |  |  |
| 19 |  |  |  |  |  |  |  |
| 59150 | 53 | \(dns\) |  | 760bps | 632bps |  |  |
| 1 |  |  |  |  |  |  |  |
| 53542 | 80 | \(http\) |  | 112.9kbps | 7.0kbps |  |  |
| 12 |  |  |  |  |  |  |  |
| 53543 | 443 \(https\) |  | 34.8kbps | 6.3kbps |  |  |  |

Torch, Winbox

![](.gitbook/assets/3%20%283%29.jpeg)

Graphs

* Graphing is a tool used to monitor various RouterOS parameters over time and put the collected data in graphs.
* The following parameters can be captured.

– Voltage and temperature

– CPU, memory and disk usage

– Interface traffic

– Queue traffic

* Graphs can be accessed by typing **http://&lt;router-IP-address&gt;/graphs**

Graphs

First steps

\[admin@Pod3\] /tool graphing&gt; set store-every=5min page-refresh=300 \[admin@Pod3\] /tool graphing&gt; print

store-every: 5min

page-refresh: 300

\[admin@Pod3\] /tool graphing&gt;

Then we add values to be graphed.

\[admin@Pod3\] /tool graphing&gt; interface add allow-address=0.0.0.0/0 interface=all \[admin@Pod3\] /tool graphing&gt; queue add allow-address=0.0.0.0/0 simple-queue=test-queue1 \[admin@Pod3\] /tool graphing&gt; resource add

Graphs

![](.gitbook/assets/4.png)

SNMP

* SNMP, which stands for Simple Network Management Protocol, is an Internet-standard protocol used for managing devices on IP networks.
* Many tools, both open source and commercial, are available to manage your networks and automate many tasks.
* Like all things, configuration must be thought out since one could use SNMP to hack your network.

SNMP

First steps.

\[admin@Pod3\] /snmp&gt; set enabled=yes

\[admin@Pod3\] /snmp&gt; set contact=YOU

\[admin@Pod3\] /snmp&gt; set location=OFFICE

\[admin@Pod3\] /snmp&gt; print

enabled: yes

contact: YOU

location: OFFICE

engine-id:

trap-target:

trap-community: \(unknown\)

trap-version: 1

trap-generators:

\[admin@Pod3\] /snmp&gt;

SNMP

* Special attention should be given to communities.
* They dictate privileges.

\[admin@Pod3\] /snmp community&gt; print detail

Flags: \* - default

0 \* name="public" addresses=0.0.0.0/0 security=none read-access=yes write-access=no authentication-protocol=MD5 encryption-protocol=DES authentication-password="" encryption-password=""

\[admin@Pod3\] /snmp community&gt;

SNMP

![](.gitbook/assets/5%20%284%29.jpeg)

Time for a practical exercise

**End of module 7**

Laboratory

* Goals of the lab

– Setting up and testing a simple queue.

– Setting up and testing a PCQ based queuing configuration.

– Being able to tell the pros and cons of both.

– Test out monitoring tools and see how they can help in everyday situations.

Laboratory : Setup

![](.gitbook/assets/6%20%282%29.jpeg)

Laboratory : step 1

* Before going any further, install a MIB browser of your computers.
* Also, pods should pair up for this lab as many steps will require that more than one computer be connected to the routers.

Laboratory : step 2

* Test throughput using a speed testing web site. Note the results.
* Configure a simple queue \(call it "lab7"\) that will limit your entire LAN to 4Mbps download and 2Mbps upload.
* Test throughput again.
* Ask a fellow student to plug into your router and repeat the speed test. What do you get? Does your fellow student get the same results when you connect to his router?

Laboratory : step 3

* Add bursting in the "lab7" queue. Parameters are :

– Burst limit 4M \(upload\), 6M \(download\)

– Burst-threshold 3M \(upload\), 5M \(download\)

– Burst-time 16 seconds for both

* Repeat the same tests as before and view results.
* Once done, disable the simple queue.

Laboratory : step 4

* Create a PCQ based system so that all computers on the same LAN have a limit of 4Mbps for downloads and 2Mbps for uploads.
* Make sure that the names that you use are meaningful!
* Test throughput using a speed testing web site. Note the results.
* Ask a fellow student to plug into your router and repeat the speed test. What do you get? Does your fellow student get the same results when you connect to his router?

Laboratory : step 5

* Configure traffic monitoring in such a way that it will send you an e-mail if inbound traffic exceeds 3Mbps on your wireless interface.

Laboratory : step 6

* Use the torch tool in such a way that you can see the source address of nodes doing any IP traffic on any port through the wireless interface.

– Experiment with the CLI and Winbox approaches.

Laboratory : step 7

* Enable graphs on :

– Wireless interface

– Hardware resources

* View them on your browser

Laboratory : step 8

* Enable SNMP, and supply these parameters :

– Your name as contact info.

– Your pod number as location \(Podx\).

– Keep the rest at default value.

* Using a MIB Browser, walk through your router's MIBs. Can you see your name and location?

Laboratory : step 9

* As usual, save the current configuration in binary and text format using the same name format that has been used in previous labs.


File: /m8-tunnels.md
# M8 Tunnels

## Tunnels

* Tunnels are a way of expanding your private network across a public network, such as the Internet.
* They are also referred to as VPNs \(virtual private networks\).
* The concept of security is associated with VPNs. They're used since it's not desirable to allow the users' traffic to go through unsecured and not privately owned \(by the client\) networks.

**PPP settings**

PPP profile

* PPP profiles represent configuration parameters to be used by PPP clients such as, but not limited to :

–

–

–

Local and remote IP addresses or pools

Compression

Encryption

**/ppp profile** \(example from a client\)

add change-tcp-mss=yes name=Profile-external use-compression=\

yes use-encryption=yes use-vj-compression=no

**/ppp profile** \(example from a server\)

add change-tcp-mss=yes local-address=192.168.222.1 name=Profile-external \

remote-address=192.168.222.2 use-compression=yes use-encryption=yes \

use-vj-compression=no

add change-tcp-mss=no dns-server=192.168.5.1 local-address=192.168.5.1 name=\

| Profile-internal remote-address=Pool-VPN use-compression=yes \ |  |  |
| :--- | :--- | :--- |
| use-encryption=yes use-vj-compression=no |  |  |
|  |  |  |

PPP secret

* PPP secrets are found on PPP servers and they specify the basic parameters required to authenticate a client, such as:

–

–

Name : The user's identification

Password : The user’s password

– Service : The protocol being serviced \(If left to "any", the PPP secret will authenticate the user through any service \(PPPoE, L2TP, PPTP, etc.\)\)

– Profile : The configuration subset to be used by this user. Profiles allow parameters to be used by many users without having to retype everything every time.

* Clients do not use PPP secrets as their authentication credentials. They are specified in the PPP client's interface under the "user" and "password" parameters.

**/ppp secret**

add name=Pod4-external password=pod4-123 profile=Profile-external routes=\

192.168.4.0/24

add name=alain password=alain!! profile=Profile-internal

PPP status

* It represents the connections' current status. Useful to debug and verify proper operations of your tunnels.

\[admin@Pod5\] &gt; **/ppp active print detail**

Flags: R - radius

* name="alain" service=pppoe caller-id="28:D2:44:2C:06:EE" address=192.168.5.100 uptime=3m56s encoding="MPPE128 statefull" session-id=0x81B00044 limit-bytes-in=0 limit-bytes-out=0
* name="Pod4-external" service=pppoe caller-id="D4:CA:6D:8E:1A:97" address=192.168.222.2 uptime=37s encoding="MPPE128 stateless" session-id=0x81B00045 limit-bytes-in=0 limit-bytes-out=0

| \[admin@Pod5\] &gt; **/ppp active print** |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Flags: R - radius |  |  |  |  |  |  |  |
| \# | NAME | SERVICE CALLER-ID | ADDRESS | UPTIME | ENCODING |  |  |
| 0 | alain | pppoe | 28:D2:44:2C:06:EE | 192.168.5.100 | 4m12s | MPPE128 | statefull |
| 1 | Pod4-exte... | pppoe | D4:CA:6D:8E:1A:97 | 192.168.222.2 | 53s | MPPE128 | stateless |

**IP pool**

Creating a pool

* IP pools define a range of IP addresses for clients.
* Not only is it used for DHCP, as we saw earlier in this course, but it can be used for PPP and Hotspot clients.
* Useful when an interface can service many clients. Addresses are assigned from the pool automatically.

Managing ranges

* IP pool ranges are lists of non-overlapping IP addresses that can be assigned to clients through services \(DHCP, PPP, hotspots\).
* Let's demonstrate with an example. You have 50 computers on the corporate LAN and 50 coming in from you VPN.

**/ip pool**

add name=Pool-PC ranges=192.168.5.50-192.168.5.99

add name=Pool-VPN ranges=192.168.5.100-192.168.5.149

Managing ranges

* You need to add 50 more computers in the LAN's pool.

| **/ip pool print** |  |  |
| :--- | :--- | :--- |
| \# NAME | RANGES |  |
| 0 | Pool-PC | 192.168.5.50-192.168.5.99 |
| 1 | Pool-VPN | 192.168.5.100-192.168.5.149 |

**/ip pool**

set 0 ranges=192.168.5.50-192.168.5.99,192.168.5.150-192.168.5.199

| **/ip pool&gt; print** |  |  |
| :--- | :--- | :--- |
| \# NAME | RANGES |  |
| 0 | Pool-PC | 192.168.5.50-192.168.5.99 |
|  |  | 192.168.5.150-192.168.5.199 |
| 1 | Pool-VPN | 192.168.5.100-192.168.5.149 |

Assigning to a service

•

•

Pools can be assigned to services such as DHCP, PPP and hotspot.

We'll see the syntax in the slides to come.

**Secure local networks**

PPPoE

* Point-to-point over Ethernet is a layer 2 protocol.
* It is often used by ISP’s to control access to their networks.
* It can be used as a method of access on any layer 2 technology, such as 802.11 or Ethernet.

PPPoE service-name

* The service-name can be seen as the SSID of 802.11, meaning that it’s the network name that the client is looking for.
* Unlike the SSID, if the client doesn’t specify one, the access concentrator \(PPPoE server\) will send all service-names that it services. The client will respond to the first one it gets.

Creating a PPPoE server

* A PPPoE server is the device that is offering the tunneling service.
* It allows clients to get a secured layer 3 VPN service over a layer 2 infrastructure.
* You CANNOT reach a PPPoE server through routers. Since it's a layer 2 protocol, the server can only be reached through the same Ethernet broadcast domain on which the clients are.

Creating a PPPoE server

* Before creating the server itself, create the configuration parameters that you require \(for values other than default\), such as :

–

–

–

IP pools

1. profiles PPP secrets

* Create the server interface on the physical interface facing the clients.

Creating a PPPoE server, example

**/ip pool**

add name=Pool-PC ranges=192.168.5.50-192.168.5.99,192.168.5.150-192.168.5.199 add name=Pool-VPN ranges=192.168.5.100-192.168.5.149

**/ppp profile**

add change-tcp-mss=yes local-address=192.168.222.1 name=Profile-external \ remote-address=192.168.222.2 use-compression=yes use-encryption=yes \ use-vj-compression=no

add change-tcp-mss=no dns-server=192.168.5.1 local-address=192.168.5.1 name=\ Profile-internal remote-address=Pool-VPN use-compression=yes use-encryption=\ yes use-vj-compression=no

Creating a PPPoE server, example

**/ppp secret**

add name=Pod4-external password=pod4-123 profile=Profile-external routes=\ 192.168.4.0/24

add name=alain password=alain!! profile=Profile-internal

**/interface pppoe-server server**

add authentication=mschap2 default-profile=Profile-external disabled=no \ interface=ether1 mrru=1600 service-name=PPPoE-external

add authentication=mschap2 default-profile=Profile-internal disabled=no \ interface=ether5 mrru=1600 service-name=PPPoE-internal

Creating a PPPoE server

Tip :

You can leave an Ethernet port without a master port, a bridge or an IP address and the client that is connected to this port can still get Internet access if your PPPoE server \(and the PPPoE client\) is properly configured.

Point-to-point addresses

* The easiest way of setting up addresses is hardcoding them in the configuration.
* Address from /ppp secret has precedence over /ppp profile, and they take precedence over /ip pool.
* Both local and remote addresses can be unique or from a pool.
* Static IP addresses or DHCP should not be used on PPPoE client interfaces. Let the infrastructure control what is given out!

Creating PPPoE clients on RouterOS

* If you wish to use a different profile than the default ones, create it first. You won't have to come back to it later.

•

•

Create the client interface on the interface facing the ISP.

You're done!

Tip :

Your router would not have to be configured with a DHCP client on the WAN interface and it would still work if the PPPoE server is on the same layer 2 infrastructure as the WAN port.

PPPoE client on RouterOS, example

**/ppp profile**

add change-tcp-mss=yes name=Profile-external use-compression=yes \ use-encryption=yes use-vj-compression=no

**/interface pppoe-client**

add ac-name="" add-default-route=yes allow=mschap2 \ default-route-distance=1 dial-on-demand=no disabled=no \ interface=ether1 keepalive-timeout=60 max-mru=1480 max-mtu=1480 \ mrru=disabled name=Client-PPPoE password=pod4-123 profile=\ Profile-external service-name="" use-peer-dns=no user=\ Pod4-external

* Enable the client interface.

**Secure remote networks communication**

PPTP clients and servers

* PPTP is a layer 3 tunneling protocol and uses IP routing information and addresses to bind clients to servers.
* Defining the PPTP server is almost the same thing as for PPPoE, except that no interface has to be specified.
* The client is defined almost the same way as a PPPoE client, except that an IP address has to be specified for the server.
* Tip : You must permit TCP, port 1723 in the router's firewall \(the PPTP server\) for your tunnel to come up.

**/interface pptp-server server**

set authentication=mschap2 default-profile=Profile-external enabled=yes

**/interface pptp-client**

add add-default-route=yes allow=mschap2 connect-to=192.168.0.5 \

default-route-distance=1 dial-on-demand=no disabled=no keepalive-timeout=60 \

max-mru=1450 max-mtu=1450 mrru=1600 name=Client-PPTP password=pod4-123 profile=\

Profile-external user=Pod4-external

SSTP clients and servers without certificates

•

•

•

Defining the SSTP server is almost the same thing as for PPTP, except that you specify a TCP port to connect to \(443 by default\).

The client is defined almost the same way as a PPTP client, except that you specify a TCP port to use to establish a connection \(443 by default\).

Tip : You must permit TCP, port 443 for your tunnel to come up. Also, leave the port at 443 to ensure SSL is used for your communications.

**/interface sstp-server server**

set authentication=mschap2 enabled=yes

**/interface sstp-client**

add add-default-route=no authentication=mschap2 certificate=none connect-to=\

192.168.0.5:443 dial-on-demand=no disabled=no http-proxy=0.0.0.0:443 \

keepalive-timeout=60 max-mru=1500 max-mtu=1500 mrru=1600 name=Client-SSTP \

password=pod4-123 profile=Profile-external user=Pod4-external \

verify-server-address-from-certificate=no verify-server-certificate=n

Setup routes between networks

* Once your tunnel is up, you need routes to move packets back and forth.
* The first way, for a single client tunnel, is the route that is automatically

created for that tunnel.

**/ip route print**

| Flags: X - disabled, A - active, D - dynamic, |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, |  |  |  |  |  |
| B - blackhole, U - unreachable, P - prohibit |  |  |  |  |  |
| \# |  | DST-ADDRESS | PREF-SRC | GATEWAY | DISTANCE |
| 0 | ADS | 0.0.0.0/0 |  | 192.168.0.254 | 0 |
| 1 | ADC | 192.168.0.0/24 | 192.168.0.5 | ether1 | 0 |
| 2 | ADC | 192.168.5.0/24 | 192.168.5.1 | Bridge-PC | 0 |
| **3** | **ADC** | **192.168.5.101/32** | **192.168.5.1** | **&lt;pptp-alain&gt;** | **0** |

Setup routes between networks

* The second way is to specify one or multiple routes within the PPP

secret for a client.

**/ppp secret export**

add name=Pod4-external password=pod4-123 profile=Profile-external routes=192.168.4.0/24 add name=alain password=alain!! profile=Profile-internal

**/ppp secret print**

Flags: X - disabled

| \# | NAME | SERVICE CALLER-ID | PASSWORD | PROFILE | REMOTE-ADDRESS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | Pod4-external | any | pod4-123 | Profile-external |  |
| 1 | alain | any | alain!! | Profile-internal |  |

**/ppp secret**

set 0 routes=192.168.4.0/24,10.10.2.0/24

**/ppp secret export**

add name=Pod4-external password=pod4-123 profile=Profile-external routes=192.168.4.0/24,10.10.2.0/24 add name=alain password=alain!! profile=Profile-internal

Setup routes between networks

* The third way is to add static routes to one or multiple networks across a tunnel.
* This method is useful if both routers must have their own default route, but it implies more maintenance and parameters.

**/ip route**

add comment="TO OFFICE LOOPBACKS" distance=1 dst-address=10.10.2.0/24 gateway=192.168.254.10

add comment="TO OFFICE NETWORKS" distance=1 dst-address=172.16.8.0/21 gateway=192.168.254.10

Closing note

![](.gitbook/assets/0%20%282%29.png)

| **VPN Protocol** | **Encryption** | **Ports** | **Compatible with** | **Notes** |
| :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |
| PPTP | MPPE with RC4 | 1723 TCP | Windows XP, Vista, 7 | PPTP is the most widely used VPN protocol today. |
|  | 128 bit key |  | Mac OS X | It is easy to setup and can be used to bypass all Internet restrictions. |
|  |  |  | iPhone OS | PPTP is considered less secure. |
|  |  |  | Android |  |
|  |  |  |  |  |
| SSTP |  |  | Windows 7 |  |
|  | SSL with AES |  |  | SSTP uses a generic port that is never blocked by firewalls. |
|  | 2048 bit key certificate | 443 TCP |  | You can use SSTP to bypass corporate or school firewalls. |
|  | 256 bit key for encryption |  |  | SSTP is considered a very secure protocol. |
|  |  |  |  |  |

Want to learn more?

[http://wiki.mikrotik.com/wiki/Manual:Interface/PPTP](http://wiki.mikrotik.com/wiki/Manual:Interface/PPTP) [http://wiki.mikrotik.com/wiki/Manual:Interface/SSTP](http://wiki.mikrotik.com/wiki/Manual:Interface/SSTP) [http://www.highspeedvpn.net/PPTP-L2TP-SSTP-OpenVPN.aspx](http://www.highspeedvpn.net/PPTP-L2TP-SSTP-OpenVPN.aspx) [http://www.squidoo.com/advantages-and-disadvantages-of-vpn-protocols](http://www.squidoo.com/advantages-and-disadvantages-of-vpn-protocols) [http://www.vpnonline.pl/en/protokoly-vpn-porownanie](http://www.vpnonline.pl/en/protokoly-vpn-porownanie) \(good table here!\)

Time for a practical exercise

**End of module 8**

Laboratory

* Goals of the lab

– Create PPP profiles and secrets

– Create and assign IP pools to services

– Create a PPPoE VPN between a computer and a router

– Create PPTP and SSTP tunnels between pods

– Insure proper routing

Laboratory : Setup

![](.gitbook/assets/1%20%282%29.png)

Laboratory : step 1

Students will pair up again for this laboratory.

* Students will create three PPP profiles

– Two to use with the neighbor pod.

•

•

One for the server service.

One for the client service.

– One to use for locally connected clients.

* Students will create two PPP secrets

– One to allow the neighbor pod to connect to the local pod.

– One to connect the locally connected clients.

* Paired students will agree on syntax and content for the parameters. For length's sake, please keep it simple!

Laboratory : step 2

* Create an IP pool to be used by clients wanting to connect by VPN.

– Your pool will be on a different network than your existing LAN.

– Assign the pool to the profile to be used by your future "corporate" VPN.

Laboratory : step 3

* Select a free port on your router and remove it from any bridge group or master port that it may be assigned to. It must not have an IP address or any DHCP configured on it.
* Configure a PPPoE server on your router to use that port. You should use the profile that you created for your VPN clients. Enable only MSChap2 for authentication. Look at the course material for compression and encryption settings.

Laboratory : step 4

•

•

Configure your computer to connect to your router with a PPPoE client connection.

Connect and browse away!

**Warnings!**

– Check the interface on which you configure your server \(and on which you plug your computer\).

– Check the profile setting in your PPPoE server and PPP secret.

Laboratory : step 5

* Connect your computer back on a normal Ethernet interface.
* The even numbered pods will create a PPTP server and a SSTP client.
* The odd numbered pods will create a PPTP client and a SSTP server.
* Use the profiles and secrets previously created.
* SSTP must not use certificates!
* Bring the VPN tunnels up and look at what's happening.

Laboratory : step 6

* Nothing? What did we forget?

– Hint : A new firewall filter maybe?

* Once the tunnels are up, look at the active connections' statuses.

Laboratory : step 7

* Remove static routes from your routing table. You should only have one to your peer pod.
* Ping your peer pod's LAN IP address. Does it work? But the tunnel is still up? How can that be? \(Leave the ping running\)
* Can you ping the remote address of your tunnel? All is not lost then.

Laboratory : step 8

* Open the PPP secret from your router and, in the "Routes" field, add the other pod's network and mask.
* Once this is done on both pods, restart your client tunnels.
* Notice the effect it has in your routing table. Your peer's subnet has appeared once the peer pod logged in. Once both tunnels are up, both will be able to ping.
* Notice also the addresses in IP address list.

Laboratory : step 9

* As usual, save the current configuration in binary and text format using the same name format that has been used in previous labs.

**Best of luck with the certification exam!!**



File: /README.md
# Начальная страница
[Оглавление](SUMMARY.md)


File: /SUMMARY.md
# Оглавление

* [M1 Intro](m1-intro.md)
* [M2 Routing](m2-routing.md)
* [M3 Bridging](m3-bridging.md)
* [M4 Wireless](m4-wireless.md)
* [M5 Network Management](m5-network-management.md)
* [M6 Firewall](m6-firewall.md)
* [M7 QoS](m7-qos.md)
* [M8 Tunnels](m8-tunnels.md)
* [Change Log перевода](changelog.md)


