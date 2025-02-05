# Repository Information
Name: login-page-mikrotik

# Directory Structure
Directory structure:
└── github_repos/login-page-mikrotik/
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
    │   │       ├── pack-870180483303692f1b1b5ddeada9601df323ffcf.idx
    │   │       └── pack-870180483303692f1b1b5ddeada9601df323ffcf.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── alogin.html
    ├── css/
    │   ├── colors/
    │   │   └── theme-color-1.css
    │   ├── custom.css
    │   ├── responsive.css
    │   └── style.css
    ├── errors.txt
    ├── img/
    │   ├── icons/
    │   ├── img-web/
    │   │   ├── Thumbs.db
    │   │   └── wp.icmp.my.id.url
    │   └── wp.icmp.my.id.url
    ├── js/
    │   ├── custom.js
    │   └── scripts.js
    ├── login.html
    ├── logout.html
    ├── md5.js
    ├── plugins/
    │   ├── parallax/
    │   ├── parsley/
    │   ├── particles.js/
    │   │   └── particles.settings.js
    │   ├── retinajs/
    │   ├── swiper/
    │   ├── typed.js/
    │   └── waypoints/
    ├── redirect.html
    ├── rlogin.html
    └── status.html


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
	url = https://github.com/xzennt/login-page-mikrotik.git
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
0000000000000000000000000000000000000000 43195ff1da503f7b19bec4d45de1ab77846d0b29 vivek-dodia <vivek.dodia@icloud.com> 1738606357 -0500	clone: from https://github.com/xzennt/login-page-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 43195ff1da503f7b19bec4d45de1ab77846d0b29 vivek-dodia <vivek.dodia@icloud.com> 1738606357 -0500	clone: from https://github.com/xzennt/login-page-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 43195ff1da503f7b19bec4d45de1ab77846d0b29 vivek-dodia <vivek.dodia@icloud.com> 1738606357 -0500	clone: from https://github.com/xzennt/login-page-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
43195ff1da503f7b19bec4d45de1ab77846d0b29 refs/remotes/origin/master
e63835d20be603852e99cd142732ddd1e4ac7530 refs/remotes/origin/ver2


File: /.git\refs\heads\master
43195ff1da503f7b19bec4d45de1ab77846d0b29


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /alogin.html
﻿<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Teras HOTSPOT</title>
    <link rel="shortcut icon" type="image/png" href="favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,400i,500i,700%7CRoboto:400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="css\bootstrap.min.css">
    <link rel="stylesheet" href="plugins\swiper\swiper.min.css">
    <link rel="stylesheet" href="plugins\magnific-popup\magnific-popup.min.css">
    <link rel="stylesheet" href="plugins\color-switcher\color-switcher.css">
    <link rel="stylesheet" href="css\style.css">
    <link rel="stylesheet" href="css\responsive.css">
    <link rel="stylesheet" href="css\colors\theme-color-1.css">
    <link rel="stylesheet" href="css\custom.css">
</head>

<body>
    <div class="preLoader"></div>
    <header class="header">
        <div class="main-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-3 col-sm-3 col-9">
                        <div class="logo" data-animate="fadeInUp" data-delay=".7">
                            <a href="login.html"> <img src="img/icon.png"> </a>
                        </div>
                    </div>
                    <div class="col-lg-7 col-md-5 col-sm-3 col-3">
                        <nav data-animate="fadeInUp" data-delay=".9">
                            <div class="header-menu">
                                <ul>
                                    <li class="active"><a href="login.html">Home</a></li>
                                    <li><a href="status.html">Status</a></li>
                                    <li><a href="logout.html?erase-cookie=true">Logout</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section class="position-relative bg-light pt-4 pb-4">
        <div id="particles_js"></div>
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="banner-content">
                        <h5>
                            <p>Selamat datang di layanan Teras Hotspot</p>
                        </h5>
                        <h1>Teras Hotspot Landing Page</h1>
                        <h4 data-animate="fadeInUp" data-delay="1.3">Selamat datang $(username) ! di layanan Hotspot
                        </h4></br>
                    </div>
                    <div class="row" data-animate="fadeInUp" data-delay="1.4">
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://google.com" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/google.png" alt="Google">
                                    <p align=center style="padding-bottom: 20px;">Google</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://youtube.com" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/youtube.png" alt="Youtube">
                                    <p align=center style="padding-bottom: 20px;">Youtube</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://facebook.com" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/facebook.png" alt="Facebook">
                                    <p align=center style="padding-bottom: 20px;">Facebook</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://tokopedia.com" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/tokopedia.png" alt="Tokopedia">
                                    <p align=center style="padding-bottom: 20px;">Tokopedia</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="https://shopee.co.id" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/shopee.png" alt="Shopee">
                                    <p align=center style="padding-bottom: 20px;">Shopee</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="https://wa.me/6283861270513" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/whatsapp.png" alt="Whatsapp">
                                    <p align=center style="padding-bottom: 20px;">Whatsapp</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://twitter.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/twitter.png" alt="Twitter">
                                    <p align=center style="padding-bottom: 20px;">Twitter</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://www.instagram.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/instagram.png" alt="Instagram">
                                    <p align=center style="padding-bottom: 20px;">Instagram</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://maps.google.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/maps.png" alt="Maps">
                                    <p align=center style="padding-bottom: 20px;">Maps</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://play.google.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/playstore.png" alt="Playstore">
                                    <p align=center style="padding-bottom: 20px;">Playstore</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://drive.google.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/drive.png" alt="Drive">
                                    <p align=center style="padding-bottom: 20px;">Drive</p>
                                </a></div>
                        </div>
                        <div class="col-md-3 col-4">
                            <div class="form-group mb-0"><a href="http://mail.google.com/" target="_blank"><img
                                        class="iconbox-media-img" src="img/img-web/gmail.png" alt="Gmail">
                                    <p align=center style="padding-bottom: 20px;">Gmail</p>
                                </a></div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="banner-image"> <img src="img\saber.png" alt="" data-animate="fadeInUp" data-delay="1.4"
                            data-depth="0.2"></div>
                </div>
            </div>
        </div>
    </section>
    <section>
        <div class="services-title position-relative pt-7" data-bg-img="img/buildings.jpg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title text-center">
                            <h2 class="text-white" data-animate="fadeInUp" data-delay=".1">Service</h2>
                            <p class="text-white" data-animate="fadeInUp" data-delay=".3">Internet Unlimated
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="services-wrap bg-white position-relative pt-5 pb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-md-4 col-sm-6">

                        <div class="roboto text-center font-weight-medium" data-animate="fadeInUp" data-delay=".65">
                            <p>Jika ada pertanyaan silakan <a href="https://www.facebook.com/xzennt"
                                    target="_blank">Edwin Ageng</a> atau
                                <br>Whatsapp <a href="https://wa.me/6283861270513?text=ping"
                                    target="_blank">083861270513</a></p>
                        </div>
                    </div>
                </div>
    </section>

    <footer class="main-footer bg-primary pt-2">
        <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col-md-12">
                    <div class="footer-info">
                        <h3 class="text-white" data-animate="fadeInUp" data-delay="0">Kontak</h3>
                        <br>
                        <ul class="footer-contacts list-unstyled">
                            <p data-animate="fadeInUp" data-delay=".15">email: <a href="mailto:edwinageng48@gmail.com"
                                    target="_blank">edwinageng48@gmail.com</a></p>
                            <p data-animate="fadeInUp" data-delay=".2">alamat: <a
                                    href="https://goo.gl/maps/sEz658HtSmonfzD3A" target="_blank">Susukan Ngemplak
                                    RT1/6,Kabupaten Semarang</a></p>
                        </ul>
                        <ul class="social-links list-inline mb-0">
                            <li data-animate="fadeInUp" data-delay=".25"><a href="https://www.facebook.com/xzennt"
                                    target="_blank"><i class="fab fa-facebook-f"></i></a></li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="bottom-footer">
                <div class="row">
                    <div class="col-md-5 order-last order-md-first">

                    </div>
                    <div class="col-md-7 order-first order-md-last">
                        <ul class="footer-menu list-inline text-md-right mb-md-0" data-animate="fadeInDown"
                            data-delay=".95">

                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="back-to-top">
        <a href="#"> <i class="fas fa-arrow-up"></i></a>
    </div>
    <script src="js\jquery-3.2.1.min.js"></script>
    <script>
        FontAwesomeConfig = {
            searchPseudoElements: true
        };
    </script>
    <script src="js\fontawesome-all.min.js"></script>
    <script src="js\bootstrap.bundle.min.js"></script>
    <script src="plugins\typed.js\typed.min.js"></script>
    <script src="plugins\waypoints\jquery.waypoints.min.js"></script>
    <script src="plugins\waypoints\sticky.min.js"></script>
    <script src="plugins\swiper\swiper.min.js"></script>
    <script src="plugins\particles.js\particles.min.js"></script>
    <script src="plugins\particles.js\particles.settings.js"></script>
    <script src="plugins\magnific-popup\jquery.magnific-popup.min.js"></script>
    <script src="plugins\parsley\parsley.min.js"></script>
    <script src="plugins\parallax\parallax.min.js"></script>
    <script src="plugins\retinajs\retina.min.js"></script>
    <script src="js\menu.min.js"></script>
    <script src="js\scripts.js"></script>
    <script src="js\custom.js"></script>

</body>

</html>

File: /css\colors\theme-color-1.css
/*========================================================

[Theme Color Stylesheet]

Project     : VPNet
Version     : 1.0
Author      : ThemeLooks
Author URI  : https://themeforest.net/user/themelooks


/* Main Color */
.ColorSwitcher__control {
	color: #7cd273;
}

File: /css\custom.css
/*==================================================================================
    Custom Stylesheet (Any custom styling you want to apply should be defined here).



File: /css\responsive.css
@media (min-width: 1220px){.container{max-width:1200px}}@media (max-width: 1219.98px){.banner-content h2{font-size:1.4rem}.swiper-slide-active .single-pricing-plan{border:1px solid #e0e1e0}.single-pricing-plan{border:none}}@media (max-width: 1199.98px){.banner-content h2{font-size:1.1rem}.client-area .btn{padding:0.6rem 1rem}.header-menu>ul>li+li{margin-left:1.5rem}.pricing-features li{font-size:0.875rem}.image-hover-content .list-inline:not(.text-right)>li:not(:last-child){margin-right:0.3rem}.subscribe-submit .btn{padding:0.6rem 1.3rem}.single-widget{padding:15px}.follow-us a{font-size:0.625rem}}@media (max-width: 991.98px){.pt-7,.pt-5{padding-top:4rem !important}.pb-7,.pb-5{padding-bottom:4rem !important}.pb-5-5{padding-bottom:2.125rem !important}.main-header .row{position:relative}.main-header .row>div:nth-child(2){position:static}.header-menu ul ul li a:hover:before, .header-menu ul ul li.active a:before, .header-menu ul ul li:hover>a:before{opacity:0}.header-menu>ul>li{padding-top:0px;padding-bottom:0px;margin-left:0px !important}.header-menu>ul>li:first-child{border-top:0px !important}.header-menu ul li a{color:#1b435d;padding:12px 15px !important}.header-menu ul ul li a{padding-left:30px !important;width:auto}.header-menu{text-align:right;position:initial}.header-menu>ul{position:absolute !important;top:60px !important;left:15px !important;width:calc(100% - 30px) !important;background:#fff;box-shadow:0 0 10px rgba(0,0,0,0.1);max-height:350px;overflow-y:auto}.header-menu ul, .header-menu ul ul, .header-menu ul ul ul, .header-menu > ul, .header-menu.align-center > ul, .header-menu > ul > li > ul, .header-menu > ul > li:hover > ul, .header-menu ul ul li:hover>ul{position:relative;left:0;right:auto;top:0;width:100%;display:none;padding:0;opacity:1;text-align:left;z-index:99999}.header-menu ul li{width:100%;border-top:1px solid rgba(120, 120, 120, 0.2)}.header-menu > ul > li > a, .header-menu ul ul li a, .header-menu ul ul li:first-child > a, .header-menu ul ul li:last-child>a{border-radius:0;box-shadow:none;background:none}.header-menu ul li a svg{display:none}.header-menu ul ul ul li a{color:#000;padding-left:45px !important}.header-menu #menu-button{color:#7cd273;font-size:28px;display:inline-block;cursor:pointer}.header-menu .submenu-button{position:absolute;right:0;display:block;width:50px;height:40px;border-left:1px solid rgba(120, 120, 120, 0.2);z-index:10;cursor:pointer}.header-menu ul ul .submenu-button{height:44px}.header-menu .submenu-button:before{content:'';position:absolute;right:22.5px;top:18px;display:block;width:0;height:0;border:4px solid transparent;border-top-color:#1b435d;z-index:99}.header-menu .submenu-opened:before{-webkit-transform:rotate(180deg);transform:rotate(180deg);top:14px}.header-menu ul ul .submenu-button:before{top:19.5px}.header-menu ul ul .submenu-button.submenu-opened:before{top:15.5px}.header-menu #menu-button.menu-opened:before, .header-menu .submenu-button.submenu-opened:before{border-top-color:#1b435d}.header-menu>ul>li:not(.active):hover>a,.header-menu>ul>li:not(.active)>a:hover{color:#1b435d}.header-menu > ul > li > ul, .header-menu ul ul ul{box-shadow:none;border-bottom:0}.header-menu > ul > li > ul:before, .header-menu ul ul ul:before{display:none}.header-menu ul ul ul li:first-child{padding-top:0}.header-menu ul ul ul li:last-child{padding-bottom:0}.header-menu ul ul li:hover > a, .header-menu ul ul li>a:hover{color:#757575}.sticking .header-menu>ul>li:hover:not(.active)>a{color:#1b435d}.header-menu ul ul ul:after{display:none}.header-menu>ul>li>a:after,.header-menu>ul>li.active>a:after,.header-menu>ul>li:hover>a:after{display:none}.services-wrap{margin:-19rem auto 0 auto}.pricing-features li{width:33.3333%}.data-centers li{width:33.3333%;margin-bottom:0.5rem}.subscribe-submit span{margin-left:0;margin-top:0.5rem}.servers{padding-bottom:4rem}.why-us{margin-bottom:2rem}.single-step{padding-right:0}.single-step svg{display:none}.follow-us a span{display:none}.contact-form-wrap{padding:20px}}@media (max-width: 767.98px){.header-info{text-align:center;margin:0}.header-menu>ul{top:56px !important}.banner-content h1{font-size:2rem}.single-feature h3{margin:1rem 0}.pricing-features li, .data-centers li{width:50%}.pricing-features h3{margin:2rem 0}.single-service{margin-bottom:2.5rem}.pricing-features{margin-bottom:1rem}.our-clients{text-align:center}.our-clients li{display:inline-block}.our-clients li+li{margin-left:13px}.footer-info,.footer-posts,.footer-newsletter{margin-bottom:2.5rem}.subscribe-submit span{margin-top:0.25rem;margin-left:0.625rem}.single-footer-post:not(:last-of-type){padding-bottom:2.2rem}.copyright,.footer-menu{text-align:center}.footer-menu{margin-top:1rem}.single-about-us-info{margin-top:2rem}.why-us ul li{font-size:0.875rem;margin-bottom: .4rem}.follow-us a span{display:block}.post-details{padding:15px}.queries-wrap{margin-bottom:0}}@media (max-width: 575.98px){.main-header{padding:0.5rem}.header-menu>ul{top:52px !important}.header-info{padding: .5rem 0}.header-info li{padding:0}.header-info li:not(:first-child){padding-left:0}.header-info li:not(:first-child):before{display:none}.banner-content h2{height:42px}.services-wrap{margin:-16rem auto 0 auto}.single-service{margin-bottom:2rem}.pricing-features li, .data-centers li{float:none;width:100%;margin-bottom:0.3rem}.apps-list img{max-width:135px}.our-clients li{margin-top:7.5px;margin-bottom:7.5px}.single-footer-post:not(:last-of-type){padding-bottom:1.4rem}.footer-newsletter .btn{padding:0.6rem 1rem}.world-map svg{right:-155px}.page-title h1{font-size:2rem}.post-content blockquote{padding-right:0}.post-content blockquote span{display:none}.social-share li a{width:38px}.prev-next span{display:none}.comment-content a{position:static}.sub-comment{padding-left:30px}} .iconbox-media-img {display: block;align: center;max-width: 100%;height: auto;width: 3.75rem;height: 3.75rem;margin-right: auto;margin-left: auto;}

File: /css\style.css
input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}input[type="number"]{-moz-appearance:textfield}::-moz-selection{background:#262e26;color:#fff;text-shadow:none}::selection{background:#262e26;color:#fff;text-shadow:none}::-webkit-input-placeholder{color:#717271 !important;opacity:1 !important}::-moz-placeholder{color:#717271 !important;opacity:1 !important}textarea{resize:none}img{max-width:100%;height:auto}p:last-child{margin-bottom:0}a{color:#ff8a26}a:hover{color:#7cd273}a,a:hover,a:active,a:focus{text-decoration:none}h1,h2,h3,h4,h5,h6{font-family:'Roboto',sans-serif;color:#262e26}h1{font-size:2.25rem}h2{font-size:1.875rem;font-weight:bold}h3{font-size:1.125rem}h4{font-size:1rem}h5,h6{font-size:0.875rem}body{font-family:'Cabin',sans-serif;font-size:0.875rem;line-height:1.5rem;color:#717271;background:#fff}.btn{font-family:'Roboto',sans-serif;font-size:0.875rem;font-weight:500;text-transform:uppercase;border-radius:1.25rem;border:0;padding:0.6rem 1.875rem;position:relative;overflow:hidden}.btn:before,.btn:after{content:'';width:100%;height:50px;position:absolute;background:rgba(255,255,255,0.2);top:0;-webkit-transform:rotate(-45deg);transform:rotate(-45deg);-webkit-transition:all .5s;transition:all .5s}.btn:before{left:100%}.btn:after{left:-100%}.btn:hover:before{left:-100%}.btn:hover:after{left:100%}.btn-square{border-radius:0 !important}.btn:focus,.form-control:focus{box-shadow:none !important}.btn-primary,.btn-primary:focus,.btn-primary.focus,.btn-primary.disabled,.btn-primary:disabled,.btn-primary:not(:disabled):not(.disabled):active,.btn-primary:not(:disabled):not(.disabled).active,.show>.btn-primary.dropdown-toggle,.btn-primary:not(:disabled):not(.disabled):active:focus,.btn-primary:not(:disabled):not(.disabled).active:focus,.show>.btn-primary.dropdown-toggle:focus,.btn-primary:hover{color:#fff;background-color:#ff6c00;border-color:transparent;box-shadow:none}.btn-secondary,.btn-secondary:focus,.btn-secondary.focus,.btn-secondary.disabled,.btn-secondary:disabled,.btn-secondary:not(:disabled):not(.disabled):active,.btn-secondary:not(:disabled):not(.disabled).active,.show>.btn-secondary.dropdown-toggle,.btn-secondary:not(:disabled):not(.disabled):active:focus,.btn-secondary:not(:disabled):not(.disabled).active:focus,.show>.btn-secondary.dropdown-toggle:focus,.btn-secondary:hover{color:#fff;background-color:#7cd273;border-color:transparent;box-shadow:none}.bg-primary{background-color:#262E26 !important}.bg-light{background-color:#f8f8f8 !important}.roboto{font-family:'Roboto',sans-serif}.cabin{font-family:'Cabin',sans-serif}.font-weight-medium{font-weight:500}.list-inline>li{display:inline-block}.list-inline:not(.text-right)>li:not(:last-child){margin-right:1rem}.list-inline.text-right>li:not(:first-child){margin-left:1rem}.form-control{font-size:0.875rem}.form-control:focus{border-color:#ff8a26}input.parsley-error,textarea.parsley-error,select.parsley-error{border:1px solid red !important}.half-gutters{margin-right:-7.5px;margin-left:-7.5px}.half-gutters>.col,.half-gutters>[class*="col-"]{padding-right:7.5px;padding-left:7.5px}.border-bottom{border-bottom:1px solid #e0e1e0 !important}.list-item li svg{color:#ff6c00;margin-right:0.625rem}.pt-7{padding-top:7.5rem !important}.pb-7{padding-bottom:7.5rem !important}.pt-5{padding-top:5rem !important}.pb-5{padding-bottom:5rem !important}.pb-5-5{padding-bottom:5.625rem !important}.pt-4{padding-top:4rem !important}.pb-4{padding-bottom:4rem !important}.pt-2{padding-top:2rem !important}.pb-2{padding-bottom:2rem !important}.mb-5{margin-bottom:4rem !important}.animated{-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-fill-mode:backwards;animation-fill-mode:backwards}.animated.infinite{-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}@-webkit-keyframes spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes spin{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.spin{-webkit-animation:spin 2s linear infinite;animation:spin 1s linear infinite}@-webkit-keyframes blink{0%{opacity:1}50%{opacity:0}100%{opacity:1}}@keyframes blink{0%{opacity:1}50%{opacity:0}100%{opacity:1}}.blink{-webkit-animation:blink 0.7s infinite;animation:blink 0.7s infinite}@-webkit-keyframes ripple{100%{top:-20px;right:-20px;bottom:-20px;left:-20px;opacity:0}}@keyframes ripple{100%{top:-20px;right:-20px;bottom:-20px;left:-20px;opacity:0}}.ripple:before,.ripple:after{content:'';position:absolute;border:#56ac4c solid 15px;top:0;right:0;bottom:0;left:0;border-radius:100%;-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.ripple:hover:before,.ripple:focus:before,.ripple:active:before,.ripple:hover:after,.ripple:focus:after,.ripple:active:after{-webkit-animation-name:ripple;animation-name:ripple}.ripple:hover:after,.ripple:focus:after,.ripple:active:after{-webkit-animation-delay: .5s;animation-delay: .5s}@-webkit-keyframes shake{0%,to{-webkit-transform:translateZ(0);transform:translateZ(0)}10%,30%,50%,70%,90%{-webkit-transform:translate3d(-10px,0,0);transform:translate3d(-10px,0,0)}20%,40%,60%,80%{-webkit-transform:translate3d(10px,0,0);transform:translate3d(10px,0,0)}}@keyframes shake{0%,to{-webkit-transform:translateZ(0);transform:translateZ(0)}10%,30%,50%,70%,90%{-webkit-transform:translate3d(-10px,0,0);transform:translate3d(-10px,0,0)}20%,40%,60%,80%{-webkit-transform:translate3d(10px,0,0);transform:translate3d(10px,0,0)}}.shake{-webkit-animation-name:shake;animation-name:shake}@-webkit-keyframes fadeInDown{0%{opacity:0;-webkit-transform:translate3d(0,-40px,0);transform:translate3d(0,-40px,0)}to{opacity:1;-webkit-transform:translateZ(0);transform:translateZ(0)}}@keyframes fadeInDown{0%{opacity:0;-webkit-transform:translate3d(0,-40px,0);transform:translate3d(0,-40px,0)}to{opacity:1;-webkit-transform:translateZ(0);transform:translateZ(0)}}.fadeInDown{-webkit-animation-name:fadeInDown;animation-name:fadeInDown}@-webkit-keyframes fadeInUp{0%{opacity:0;-webkit-transform:translate3d(0,40px,0);transform:translate3d(0,40px,0)}to{opacity:1;-webkit-transform:translateZ(0);transform:translateZ(0)}}@keyframes fadeInUp{0%{opacity:0;-webkit-transform:translate3d(0,40px,0);transform:translate3d(0,40px,0)}to{opacity:1;-webkit-transform:translateZ(0);transform:translateZ(0)}}.fadeInUp{-webkit-animation-name:fadeInUp;animation-name:fadeInUp}.page-title-wrap{overflow:hidden}.page-title{z-index:1}.custom-breadcrumb li{float:left}.custom-breadcrumb a{color:#555c55;font-weight:500;text-transform:uppercase;margin-bottom:3px;display:block}.custom-breadcrumb a:hover{color:#5dbd53}.custom-breadcrumb li:last-child a{pointer-events:none}.custom-breadcrumb svg{font-size:0.75rem;color:#5dbd53;margin:0 0.5rem}.page-title h1{font-size:3rem;font-weight:700;margin:0}.world-map svg{position:absolute;right:0;top:-11px}.section-title{margin-bottom:3rem}.section-title h2{text-transform:capitalize}.section-title p{margin-top:1.5rem;color:#919491}.header-top{}.header-info{}.header-info li{font-size:0.75rem;line-height:1.25rem;padding:0.625rem 0}.header-info li:not(:first-child){padding-left:1rem;position:relative}.header-info li:not(:first-child):before{content:'';position:absolute;left:0;top:0;width:1px;height:100%;background:#fff;opacity: .1}.header-info li span{color:#ff8a26}.social-icons a{color:#fff;font-size:0.75rem}.social-icons a:hover{color:#7cd273}.main-header{padding:1rem 0;box-shadow:none;-webkit-transition:all .2s;transition:all .2s;position:relative;z-index:999}.main-header.stuck{background:#fff;position:fixed;top:0;box-shadow:0 0 0.625rem rgba(0,0,0,0.15);width:100%}.header-menu, .header-menu ul, .header-menu ul li, .header-menu ul li a, .header-menu #menu-button{margin:0;padding:0;border:0;list-style:none;line-height:1;display:block;position:relative}.header-menu #menu-button{display:none}.header-menu>ul{}.header-menu > ul ul{text-align:left;z-index:99999}.header-menu>ul>li{display:inline-block}.header-menu>ul>li.has-sub:hover:after{content:'';position:absolute;width:100%;height:2em;bottom:-2em;cursor:pointer;left:0}.header-menu>ul>li+li{margin-left:2.5rem}.header-menu>ul>li>a{padding:0.375rem 0;color:#555c55;font-size:1rem}.header-menu>ul>li:hover>a,.header-menu>ul>li.active>a{color:#5dbd53}.header-menu>ul>li>a:after,.header-menu>ul>li.active>a:after,.header-menu>ul>li:hover>a:after{content:' ';position:absolute;width:0;height:2px;background:#5dbd53;left:0;right:0;bottom:-1.4375rem;margin:auto;-webkit-transition:all .2s;transition:all .2s}.header-menu>ul>li>a:hover:after,.header-menu>ul>li.active>a:after,.header-menu>ul>li:hover>a:after{width:100%}.header-menu>ul>li>a>svg{font-size:0.625rem}.header-menu ul ul{position:absolute;left:-9999px;opacity:0;border-bottom:2px solid #5dbd53;-webkit-transition:top .2s ease, opacity .2s ease;transition:top .2s ease, opacity .2s ease}.header-menu>ul>li>ul{top:5rem;background:#fff;padding:0.625rem 0;box-shadow:0 0 0.625rem rgba(0,0,0,0.1)}.header-menu>ul>li:hover>ul{left:auto;top:3.1875rem;opacity:1}.header-menu.align-right>ul>li:hover>ul{right:0}.header-menu ul ul ul{top:2rem;box-shadow:0 0 0.625rem rgba(0,0,0,0.1)}.header-menu ul ul ul:before{content:"";position:absolute;left:-7px;top:7px;width:0;height:0;border-right:7px solid #fff;border-top:7px solid transparent;border-bottom:7px solid transparent;z-index:99}.header-menu ul ul ul:after{content:"";position:absolute;left:-10px;top:0;width:10px;height:100%;z-index:-1}.header-menu ul ul ul li{background:#fff}.header-menu ul ul ul li:first-child{padding-top:0.625rem}.header-menu ul ul ul li:last-child{padding-bottom:0.625rem}.header-menu ul ul>li:hover>ul{top:0;left:188px;opacity:1}.header-menu.align-right ul ul>li:hover>ul{left:auto;right:178px;padding-left:0;padding-right:10px;opacity:1}.header-menu ul ul li a{width:180px;padding:0.3125rem 1.25rem;color:#555c55;font-size:0.875rem;line-height:1.3rem;position:relative;-webkit-transition:all .2s;transition:all .2s}.header-menu ul ul li a svg{position:absolute;right:15px;top:8px}.header-menu ul ul li:hover > a, .header-menu ul ul li > a:hover, .header-menu ul ul li.active>a{color:#5dbd53}.client-area .dropdown a svg{font-size:0.75rem}.client-area .dropdown a{color:#555c55}.client-area .dropdown a:hover{color:#5dbd53}.client-links{border:0;padding:0.5rem 1.25rem;border-bottom:2px solid #5dbd53;box-shadow:0 0 0.625rem rgba(0,0,0,0.1);border-radius:0;margin-top:0.5rem;font-size:0.875rem}.client-links a{line-height:1.5rem;margin:0.3125rem 0;display:block}canvas{display:block;vertical-align:bottom}#particles_js{position:absolute;width:100%;height:100%;top:0;left:0;background-color:#f8f8f8;background-repeat:no-repeat;background-size:cover;background-position:50% 50%;opacity: .3}.banner-content{}.banner-content h1{font-size:3rem;font-weight:700}.banner-content h2{font-size:1.5rem;font-weight:700;color:#555c55;border-left:0.1875rem solid #5dbd53;padding-left:0.4375rem;margin-top:1rem;margin-bottom:1.5rem;text-transform:capitalize}.typed-cursor{-webkit-animation:blink 0.7s infinite;animation:blink 0.7s infinite;position:relative;top:-0.125rem;color:#000}.banner-content li:last-child a{padding:0;color:#262e26}.banner-content li:last-child a:hover{color:#5dbd53}.banner-content li a svg{margin-left:3px}.single-feature{margin-bottom:1.875rem}.single-feature h3{font-weight:700;margin:1.5rem 0}.services-title{height:540px}.services-title:before{content:'';position:absolute;background:rgba(0,0,0,0.8);width:100%;height:100%;left:0;top:0}.services-wrap{max-width:1360px;margin:-15rem auto 0 auto;box-shadow:0 0 0.625rem rgba(0,0,0,0.1)}.single-service{margin-bottom:3.5rem}.single-service h4{margin-top:0.625rem}.pricing-plans .section-title{margin-bottom:0}.pricing-features h3{line-height:1.75rem;margin-bottom:3rem}.pricing-features ul{}.pricing-features li{font-size:1rem;float:left;width:50%;margin-bottom:0.625rem}.pricing-features li svg{font-size:0.875rem}.pricing-features .btn{padding-left:0;padding-right:0}.pricing-slider{padding:3.125rem 0}.single-pricing-plan{padding:1.875rem;width:270px;border:1px solid #e0e1e0;background:#fff;box-shadow:none;-webkit-transition:box-shadow .5s;transition:box-shadow .5s}.swiper-slide-active.single-pricing-slide{z-index:1}.swiper-slide-active .single-pricing-plan{position:absolute;left:-999px;right:-999px;margin-left:auto;margin-right:auto;width:270px;background:#fff;padding:3.75rem 1.875rem;margin-top:-1.875rem;box-shadow:0 0 1.25rem rgba(0,0,0,0.15)}.swiper-slide-active .single-pricing-plan svg path{fill:#5dbd53 !important}.single-pricing-plan h4{letter-spacing:5px;border-bottom:1px solid #e0e1e0;margin-top:1.25rem;padding-bottom:2rem;margin-bottom:1.5rem}.single-pricing-plan .time{display:block;color:#ff6c00;margin-bottom:1.75rem}.single-pricing-plan strong{font-size:2.25rem;color:#262e26;display:block;margin-bottom:1.5rem}.single-pricing-plan strong sub{font-size:0.875rem;color:#919491;font-weight:400;bottom:0;left:-0.25rem}.single-pricing-plan p{margin-bottom:1.5rem}.single-pricing-plan p span{}.swiper-slide-active .single-pricing-plan .btn{background:#5dbd53}.swiper-slide-next .single-pricing-plan{position:absolute;right:0}.swiper-pagination-bullet{background:#e0e1e0;width:0.625rem;height:0.625rem;opacity:1;margin:0 5px}.swiper-pagination-bullet-active{background:#5dbd53}.review-slider{margin-bottom:1.25rem}.single-review-slide h4 svg{color:#ff8a26;font-size:0.5rem;position:relative;top:-3px;left:1rem}.single-review-slide span{color:#919491;display:block;margin-bottom:1.25rem}.single-review-slide p{}.servers{overflow:hidden}.data-centers{}.data-centers li{float:left;width:50%;font-size:1rem;color:#555c55;margin-bottom:1rem}.server-map{width:1145px}.server-btn{padding-left:0;padding-right:0;color:#919491}.server-btn svg{margin-left:0.5rem}.main-footer h3{margin-bottom:1.25rem}.footer-contacts{font-size:0.75rem}.footer-contacts li{position:relative;padding-left:1.5rem;margin:5px 0}.footer-contacts svg{position:absolute;left:0;top:0.4375rem;font-size:0.6875rem;color:#fff}.footer-contacts li a{color:#919491}.footer-contacts li a:hover{color:#fff}.social-links a svg{color:#919491}.social-links a:hover svg{color:#fff}.footer-posts a{color:#919491}.footer-posts a:hover{color:#fff}.footer-posts a svg{margin-left:3px;position:relative;top:2px}.single-footer-post{margin-bottom:1.5rem}.single-footer-post:not(:last-of-type){margin-bottom:1rem;padding-bottom:1.4rem;border-bottom:1px solid #3c433c}.single-footer-post>a{margin-right:1rem;margin-bottom:0.7rem;position:relative;top:0.5625rem}.single-footer-post span{font-size:0.75rem;color:#919491}.single-footer-post p a{display:block}.footer-newsletter{}.footer-newsletter .form-group{position:relative}.footer-newsletter input{border-radius:0;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.05);height:45px;-webkit-transition:all .2s;transition:all .2s;margin-bottom:1.25rem;margin-top:2rem;color:#fff}.footer-newsletter input:focus{background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.05);color:#fff}.subscribe-submit span{font-size:0.75rem;line-height:1rem;display:inline-block;margin-top:0.25rem;margin-left:0.625rem}.bottom-footer{border-top:1px solid #464d46;padding:1rem 0 3rem}.copyright a{color:#919491}.footer-menu a{color:#919491}.footer-menu a:hover{color:#fff}.about-us-title{border-bottom:1px solid #e0e1e0;padding-bottom:3.5rem}.about-us-title h2{margin-bottom:1rem}.about-us-title p, .write-about-us p{font-size:1.125rem;font-weight:500;font-style:italic;line-height:1.75rem}.single-about-us-info{margin-top:3.5rem}.single-about-us-info h3{font-weight:700;margin-bottom:1.25rem}.write-about-us{box-shadow:0 0 0.625rem rgba(0,0,0,0.1);padding:3.5rem 1rem 4rem 1rem;margin-top:3.5rem}.write-about-us h2{margin-bottom:1rem}.single-member{background:#fff;margin-bottom:30px}.single-member-info{padding:1.625rem 1rem}.single-member-info span{display:block;border-left:3px solid #5dbd53;padding-left:0.5rem}.single-member:hover .image-hover-content{bottom:0}.single-member:hover img{-webkit-transform:scale(1.2);transform:scale(1.2)}.youtube-video:before{content:'';position:absolute;left:0;right:0;top:0;bottom:0;background:rgba(0,0,0,0.3)}.play-btn{color:#fff;font-size:1.125rem;width:60px;height:60px;display:block;position:absolute;left:0;right:0;top:0;bottom:0;margin:auto;text-align:center;background:#56ac4c;border-radius:100%;line-height:60px;outline:none !important}.play-btn:hover{color:#fff}.back-to-top{position:fixed;right:25px;bottom:10px;opacity:0;visibility:hidden;-webkit-transition:all 0.2s;transition:all 0.2s}.back-to-top.show{bottom:25px;opacity:1;visibility:visible;z-index:999}.back-to-top a{font-size:0.75rem;text-align:center;line-height:2.5rem;border-radius:100%;color:#fff;width:40px;height:40px;display:inline-block;background:#7cd273;-webkit-transition:all 0.2s;transition:all 0.2s}.back-to-top a:hover{background:#22c111;color:#fff}.single-faq-wrap{}.single-faq-wrap h2{font-size:1.5rem;margin-bottom:3.25rem}.single-faq-wrap h4{margin-top:1.5rem}.single-faq-wrap h4 svg{margin-right:0.375rem;color:#ff6c00;font-size:0.875rem}.not-found span{display:block;font-size:4.5rem;font-weight:bold;color:#ff6c00;line-height:5rem;margin-bottom:2.25rem;margin-top:1.25rem}.not-found p{font-size:1.5rem;font-weight:500;margin-bottom:3rem}.blog{margin-bottom:-30px}.single-post{padding:15px;border:1px solid #e0e1e0;margin-bottom:30px}.single-post span{font-size:0.75rem;color:#919491;display:block;margin-top:0.5rem}.single-post h4{line-height:1.625rem}.single-post a{color:#919491;font-size:0.75rem;text-transform:uppercase}.single-post a:hover{color:#5dbd53}.single-post > a svg{margin-left:0.3rem}.single-post:hover .image-hover-content{bottom:0}.single-post:not(.post-details):hover img{-webkit-transform:scale(1.2);transform:scale(1.2)}.post-details{padding:30px;border:1px solid #e0e1e0;margin-bottom:30px}.post-content h2{font-size:1.5rem;font-weight:500;line-height:1.5}.post-content span{margin-top:1rem;margin-bottom: .5rem;display:block;font-size:0.75rem;color:#919491}.post-content span a{color:#919491}.post-content span a:hover{color:#5dbd53}.post-content span a:not(:last-child){margin-right:8px}.post-content blockquote{border-top:1px solid #e0e1e0;border-bottom:1px solid #e0e1e0;font-size:1.125rem;font-style:italic;padding:1.25rem 0;padding-right:90px;margin-bottom:1.25rem;position:relative}.post-content blockquote span{position:absolute;right:0;top:0;bottom:0;margin:auto;width:80px;height:80px;border-radius:100%;background:#5dbd53;color:#fff;font-size:18px;text-align:center;line-height:80px}.custom-pagination{margin-bottom:30px}.custom-pagination a{color:#919491}.custom-pagination .active a, .custom-pagination a:hover{color:#5dbd53}.custom-pagination .disabled a{color:#e0e1e0;pointer-events:none}.tag-and-share{margin-top:3.25rem}.social-share.text-lg-right>li{margin-right:0 !important}.social-share.text-lg-right>li:not(:first-child){margin-left:2px}.social-share li a{width:40px;height:40px;border-width:1px;border-style:solid;display:block;text-align:center;line-height:38px;font-size:12px;-webkit-transition:all .2s;transition:all .2s}.social-share li a.pinterest{border-color:#c8232a;color:#c8232a}.social-share li a.pinterest:hover{background-color:#c8232a;color:#fff}.social-share li a.rss{border-color:#f4b45a;color:#f4b45a}.social-share li a.rss:hover{background-color:#f4b45a;color:#fff}.social-share li a.linkedin{border-color:#0c76a8;color:#0c76a8}.social-share li a.linkedin:hover{background-color:#0c76a8;color:#fff}.social-share li a.google{border-color:#dd4a38;color:#dd4a38}.social-share li a.google:hover{background-color:#dd4a38;color:#fff}.social-share li a.twitter{border-color:#25a6d0;color:#25a6d0}.social-share li a.twitter:hover{background-color:#25a6d0;color:#fff}.social-share li a.facebook{border-color:#3a5898;color:#3a5898}.social-share li a.facebook:hover{background-color:#3a5898;color:#fff}.author-info-wrap{border-top:1px solid #e0e1e0;border-bottom:1px solid #e0e1e0;padding:1.75rem 0 1.5rem}.author-info-wrap img{border-radius:100%}.author-info>a{font-size:0.75rem}.author-info a{color:inherit}.author-info a:hover{color:#5dbd53}.prev-next li:first-child svg{margin-right:0.3125rem}.prev-next li:last-child svg{margin-left:0.3125rem}.prev-next a{font-size:12px;text-transform:uppercase;color:#919491}.prev-next a:hover{color:#5dbd53}.prev-next span{display:block;max-width:250px;color:#555c55;margin-top:0.3125rem}.comments>h3{font-weight:700;margin-bottom:2rem}.main-comment>li:not(:first-child),.sub-comment>li{border-top:1px solid #e0e1e0;margin-top:1.5rem;padding-top:1.5rem}.single-comment{}.comment-author img{margin-right:1rem;border-radius:100%}.comment-content{overflow:hidden;position:relative}.comment-content h4{margin-bottom:0}.comment-content a{position:absolute;text-transform:uppercase;font-size:0.75rem;top:0;right:0;font-family:'Roboto'}.comment-content span{font-size:0.75rem;color:#919491;display:block;margin-bottom:0.25rem}.sub-comment{padding-left:66px}.comment-form .parsley-errors-list{display:none !important}.comment-form textarea, .comment-form input{margin-bottom:10px;border-radius:0;background:#f8f8f8;height:40px;border-color:#f8f8f8}.comment-form textarea{height:120px}.single-widget{border:1px solid #e0e1e0;padding:30px;margin-bottom:30px}.single-widget h3{font-weight:700;margin-bottom:1.5rem}.single-widget input[type=text]{background:#f8f8f8;border-radius:0;height:45px;border:1px solid transparent}.single-widget input[type=text]:focus{border:1px solid #e0e1e0}.single-widget button[type=submit]{border:none;background:transparent;position:absolute;right:0;font-size:0.875rem;color:#ff6c00;padding:0 1rem;top:0;bottom:0}.widget-categories li{margin-top:0.5rem;position:relative}.widget-categories li:before{content:'';position:absolute;width:100%;border-bottom:1px dotted #919491;bottom:0.4375rem;z-index:-1}.widget-categories li:hover:before{border-bottom:1px dotted #5dbd53}.widget-categories span{background:#fff;display:inline-block;padding-right:0.25rem}.widget-categories span+span{float:right;padding-right:0;padding-left:0.25rem}.widget-categories a{display:block;color:#717271}.widget-categories a:hover{color:#5dbd53}.recent-posts li{margin-top:0.5rem}.recent-posts li:not(:last-child){border-bottom:1px dotted #919491;padding-bottom:0.5rem}.recent-posts li a{display:block;color:#555c55}.recent-posts li a:hover{color:#5dbd53}.follow-us{margin-bottom:-15px}.follow-us li{margin-bottom:15px}.follow-us a{color:#fff;font-size:0.75rem;text-align:center;text-transform:uppercase;padding:1.625rem 0 1.25rem;display:block;-webkit-transition:all .2s;transition:all .2s}.follow-us a:hover{color:#fff}.follow-us .facebook{background:#3a5898}.follow-us .facebook:hover{background:#22499c}.follow-us .twitter{background:#25a6d0}.follow-us .twitter:hover{background:#1081a6}.follow-us .google{background:#dd4a38}.follow-us .google:hover{background:#d32d19}.follow-us .pinterest{background:#c8232a}.follow-us .pinterest:hover{background:#ad0e15}.follow-us .rss{background:#f4b45a}.follow-us .rss:hover{background:#eda137}.follow-us .linkedin{background:#0c76a8}.follow-us .linkedin:hover{background:#0d658f}.follow-us a svg{font-size:1.125rem}.follow-us a span{display:block}.tags:not(.text-right)>li:not(:last-child){margin-right:0.8rem}.tags a{font-size:0.75rem;color:#919491}.tags a:hover{color:#5dbd53}.queries-wrap{margin-bottom:-30px}.single-query{padding:26px 30px;box-shadow:0 0 5px rgba(0,0,0,0.1);margin-bottom:30px;height:calc(100% - 30px);-webkit-transition:all .2s;transition:all .2s}.single-query:hover{-webkit-transform:scale(1.1);transform:scale(1.1);box-shadow:0 0 20px rgba(0,0,0,0.15)}.query-icon{min-width:60px}.query-info span{display:block;margin-bottom:0.5rem}.query-info a{color:#919491}.single-query:hover .query-info a{color:#ff6c00}.single-query:hover .query-icon svg path{fill:#5dbd53 !important}.contact-form-wrap{box-shadow:0 0 20px rgba(0,0,0,0.15);padding:30px}.contact-form-wrap h2{margin-bottom:1rem}.contact-form-wrap p{padding-bottom:0.5rem}.contact-form>div{margin-top:20px}.contact-form input, .contact-form textarea{border-radius:0;height:40px;border:1px solid #e0e1e0}.contact-form textarea{height:180px}.contact-form button{margin-top:30px}.image-hover-wrap{overflow:hidden;position:relative}.image-hover-content{position:absolute;width:100%;height:100%;bottom:-100%;-webkit-transition:all .4s;transition:all .4s;z-index:0}.image-hover-content:before{content:'';position:absolute;left:0;right:0;top:0;bottom:0;background:#7cd273;opacity:0.75;z-index:-1}.image-hover-content ul{margin:0}.image-hover-content ul li a{display:block;width:2rem;height:2rem;line-height:2rem;color:#7cd273;background:#fff;border-radius:100%;-webkit-transition:all .2s;transition:all .2s}.image-hover-content ul li a:hover{color:#fff;background:#262e26}.image-hover-content .list-inline:not(.text-right)>li:not(:last-child){margin-right:0.5rem}.image-hover-wrap:hover .image-hover-content{bottom:0}.image-hover-wrap img{-webkit-transition:all .4s;transition:all .4s}.image-hover-wrap:hover>img{-webkit-transform:scale(1.2);transform:scale(1.2)}.why-us ul li{font-size:1rem;margin-bottom:0.875rem}.single-step{margin-bottom:2rem;padding-right:50px;position:relative}.single-step h4 span{color:#ff6c00}.single-step svg{position:absolute;right:10px;top:50%;margin-top:-10px}.app-info p{font-size:1.125rem;margin-top:2.125rem;margin-bottom:2.25rem}.clients-wrap{border-top:1px solid #e9eae9}.our-clients img{filter:url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feColorMatrix type="matrix" color-interpolation-filters="sRGB" values="0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0.2126 0.7152 0.0722 0 0 0 0 0 1 0" /></filter></svg>#filter');-webkit-filter:grayscale(1);filter:grayscale(1);-webkit-transition:all .2s;transition:all .2s}.our-clients img:hover{filter:url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg"><filter id="filter"><feColorMatrix type="matrix" color-interpolation-filters="sRGB" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0" /></filter></svg>#filter');-webkit-filter:grayscale(0);filter:grayscale(0)}.preLoader{position:fixed;top:0;left:0;width:100%;height:100%;background:#7cd273;z-index:99999;overflow:hidden}.preLoader:before{content:'';-webkit-animation:spin 2s linear infinite;animation:spin 1s linear infinite;width:70px;height:70px;position:absolute;border:5px solid #fff;border-bottom:5px solid #7cd273;border-radius:100%;left:0;right:0;top:0;bottom:0;margin:auto}.parsley-errors-list{list-style:none;padding:0;position:absolute;left:0;margin:0;bottom:-20px;text-align:center;-webkit-transition:all .2s;transition:all .2s}.parsley-errors-list li{display:inline-block;font-size:0.8125rem;line-height:1.125rem;background:red;color:#fff;padding:0 0.625rem}[data-animate]{visibility:hidden;-webkit-animation-duration:0.6s;animation-duration:0.6s}[data-animate].animated{visibility:visible}.page-item{margin-bottom:30px;border:1px solid #ddd;-webkit-transition:all .2s;transition:all .2s}.page-item:hover{box-shadow:0 0 15px rgba(0,0,0,0.2)}.single-theme-feature{font-size:1.25rem;line-height:1.5;color:#000;margin:0.25rem 0;text-transform:capitalize}.single-theme-feature svg{color:#5dbd53;margin-right:0.5rem;font-size:1rem}

File: /errors.txt
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

not-logged-in = Anda belum login (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = Tidak dapat mengalokasikan identitas IP

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = BSH-Hotspot dalam perawatan

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = Maaf User ID $(username) sudah digunakan (sedang login di perangkat lain)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = Batas sesi telah tercapai  ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = invalid username ($(username)): MAC address ini bukan milik anda

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

chap-missing = Silahkan reload dan coba lagi

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = Maaf, User ID atau Password Anda salah dan jika belum terdaftar silahkan daftar dulu

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = user $(username) is not allowed to log in from this MAC address

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = user $(username), waktu pemakaian sudah habis
traffic-limit = user $(username), kuota anda sudah habis

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server is not responding (Silahkan hubungi Admin IT-BTH)

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = already authorizing, retry later

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /img\img-web\wp.icmp.my.id.url
[InternetShortcut]
URL=http://wp.icmp.my.id/
HotKey=0
IDList=
IconFile=C:\Windows\System32\shell32.dll
IconIndex=14
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,2


File: /img\wp.icmp.my.id.url
[InternetShortcut]
URL=http://wp.icmp.my.id/
HotKey=0
IDList=
IconFile=C:\Windows\System32\shell32.dll
IconIndex=14
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,2


File: /js\custom.js
/*==================================================================================
    Custom JS (Any custom js code you want to apply should be defined here).



File: /js\scripts.js
(function($){"use strict";$(function(){$('.header-menu a[href="#"]').on('click',function(event){event.preventDefault();});$(".header-menu").menumaker({title:'<i class="fas fa-bars"></i>',format:"multitoggle"});var mainHeader=$('.main-header');if(mainHeader.length){var sticky=new Waypoint.Sticky({element:mainHeader[0]});} var moveableImage=$('.banner-image');if(moveableImage.length){var parallaxImage=new Parallax(moveableImage[0]);} var bgImg=$('[data-bg-img]');bgImg.css('background',function(){return'url('+$(this).data('bg-img')+') center top';});$('form').parsley();var $commentContent=$('.comment-content > a');$commentContent.on('click',function(event){event.preventDefault();var $target=$('.comment-form');if($target.length){$('html, body').animate({scrollTop:$target.offset().top-120},500);$target.find('textarea').focus();}});var pricingSlider=new Swiper('.pricing-slider',{slidesPerView:3,loop:true,centeredSlides:true,spaceBetween:2,allowTouchMove:false,speed:500,autoplay:{delay:5000,disableOnInteraction:true,},pagination:{el:'.pricing-pagination',clickable:true,},breakpoints:{575:{slidesPerView:1}}});var reviewSlider=new Swiper('.review-slider',{slidesPerView:3,spaceBetween:30,speed:500,autoplay:{delay:5000,disableOnInteraction:true,},pagination:{el:'.review-pagination',clickable:true,},breakpoints:{575:{slidesPerView:1},991:{slidesPerView:2}}});var $youtubePopup=$('.youtube-popup');if($youtubePopup.length){$youtubePopup.magnificPopup({type:'iframe'});} var $backToTopBtn=$('.back-to-top');if($backToTopBtn.length){var scrollTrigger=400,backToTop=function(){var scrollTop=$(window).scrollTop();if(scrollTop>scrollTrigger){$backToTopBtn.addClass('show');}else{$backToTopBtn.removeClass('show');}};backToTop();$(window).on('scroll',function(){backToTop();});$backToTopBtn.on('click',function(e){e.preventDefault();$('html,body').animate({scrollTop:0},700);});} jQuery('img.svg').each(function(){var $img=jQuery(this);var imgID=$img.attr('id');var imgClass=$img.attr('class');var imgURL=$img.attr('src');jQuery.get(imgURL,function(data){var $svg=jQuery(data).find('svg');if(typeof imgID!=='undefined'){$svg=$svg.attr('id',imgID);} if(typeof imgClass!=='undefined'){$svg=$svg.attr('class',imgClass+' replaced-svg');} $svg=$svg.removeAttr('xmlns:a');if(!$svg.attr('viewBox')&&$svg.attr('height')&&$svg.attr('width')){$svg.attr('viewBox','0 0 '+$svg.attr('height')+' '+$svg.attr('width'));} $img.replaceWith($svg);},'xml');});var typedElement='.typed',typedTarget=$(typedElement);if(typedTarget.length){var typed=new Typed(typedElement,{strings:['MI-Oreo fastest internet provider.','MI-Oreo unlimited internet provider.','MI-Oreo low cost internet provider.'],typeSpeed:50,backSpeed:10,loop:true});} var typedElementSecond='.typed-second',typedTargetSecond=$(typedElementSecond);if(typedTargetSecond.length){var typed=new Typed(typedElementSecond,{strings:['Responsive.','Retina Ready.','Bootstrap 4 Supported.'],typeSpeed:50,backSpeed:10,loop:true});} var colorSheets=[{color:"#7cd273",title:"Switch to color-1",href:"css/colors/theme-color-1.css"},{color:"#ff6c00",title:"Switch to color-2",href:"css/colors/theme-color-2.css"},{color:"#905f36",title:"Switch to color-3",href:"css/colors/theme-color-3.css"},{color:"#ea9926",title:"Switch to color-4",href:"css/colors/theme-color-4.css"},{color:"#303030",title:"Switch to color-5",href:"css/colors/theme-color-5.css"},{color:"#dd1b1b",title:"Switch to color-6",href:"css/colors/theme-color-6.css"},{color:"#7d1935",title:"Switch to color-7",href:"css/colors/theme-color-7.css"},{color:"#31135c",title:"Switch to color-8",href:"css/colors/theme-color-8.css"},{color:"#005a31",title:"Switch to color-9",href:"css/colors/theme-color-9.css"},{color:"#1b435d",title:"Switch to color-10",href:"css/colors/theme-color-10.css"}];ColorSwitcher.init(colorSheets);});$(window).on('load',function(){function removePreloader(){var preLoader=$('.preLoader');preLoader.fadeOut();} setTimeout(removePreloader,250);});$(window).on('load',function(){var $animateEl=$('[data-animate]');$animateEl.each(function(){var $el=$(this),$name=$el.data('animate'),$duration=$el.data('duration'),$delay=$el.data('delay');$duration=typeof $duration==='undefined'?'0.6':$duration;$delay=typeof $delay==='undefined'?'0':$delay;$el.waypoint(function(){$el.addClass('animated '+$name).css({'animation-duration':$duration+'s','animation-delay':$delay+'s'});},{offset:'93%'});});});})(jQuery);

File: /login.html
﻿<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Teras HOTSPOT</title>
    <link rel="shortcut icon" type="image/png" href="favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,400i,500i,700%7CRoboto:400,500,700" rel="stylesheet">
    <link rel="stylesheet" href=".\css\bootstrap.min.css">
    <link rel="stylesheet" href=".\plugins\swiper\swiper.min.css">
    <link rel="stylesheet" href=".\plugins\magnific-popup\magnific-popup.min.css">
    <link rel="stylesheet" href=".\plugins\color-switcher\color-switcher.css">
    <link rel="stylesheet" href=".\css\style.css">
    <link rel="stylesheet" href=".\css\responsive.css">
    <link rel="stylesheet" href=".\css\colors\theme-color-1.css">
    <link rel="stylesheet" href=".\css\custom.css">
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
        //
        -->
    </script>
    $(endif)
    <div class="preLoader"></div>
    <header class="header">
        <div class="main-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-3 col-sm-3 col-9">
                        <div class="logo" data-animate="fadeInUp" data-delay=".7">
                            <a href="login.html"> <img src="img/icon.png"> </a>
                        </div>
                    </div>
                    <div class="col-lg-7 col-md-5 col-sm-3 col-3">
                        <nav data-animate="fadeInUp" data-delay=".9">
                            <div class="header-menu">
                                <ul>
                                    <li class="active"><a href="login.html">Home</a></li>
                                    <li><a href="status.html">Status</a></li>
                                    <li><a href="logout.html?erase-cookie=true">Logout</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section class="position-relative bg-light pt-4 pb-4">
        <div id="particles_js"></div>
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="banner-content">
                        <div class="section-heading">
                            <h5>
                                <p>Selamat datang di layanan Teras Hotspot</p>
                            </h5>
                            <h1>Teras Hotspot Landing Page</h1>

                        </div> <!-- .section-heading -->
                    </div>
                    <div class="card-block py-lg px-md" data-animate="fadeInUp" data-delay="1.4">
                        <form id="loginForm" class="md-form form-light" role="form" action="$(link-login-only)"
                            method="post">
                            <input type="hidden" name="dst" value="$(link-orig)" />
                            <input type="hidden" name="popup" value="true" />
                            <div class="row">
                                <div class="col-md-4">
                                    <div class="form-group">
                                        <label for="inputUser" class="form-label">Username</label>
                                        <div class="md-form-line-wrap">
                                            <input id="inputUser" type="text" name="username" placeholder="username"
                                                class="form-control" autofocus required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-4">
                                    <div class="form-group">
                                        <label for="inputPassword" class="form-label">Password</label>
                                        <div class="md-form-line-wrap">
                                            <input id="inputPassword" type="password" name="password"
                                                placeholder="password" class="form-control" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-8">
                                    <div class="form-group">
                                        $(if error)
                                        <p>Terjadi kesalahan: $(error)</p>
                                        $(endif)
                                    </div>
                                </div>
                                <div class="col-md-8">
                                    <div class="form-group mb-0">
                                        <button type="submit" class="btn btn-block btn-primary"><span
                                                class="btn-elem-wrap"><span
                                                    class="text">LOGIN</span></span></button><span
                                            style="display: none;" class="form-notify help-block mb-0"></span>
                                    </div>
                                </div>
                                <div class="col-md-8">
                                    <div class="form-group">
                                        <div style="font-size: 10px" align=center>Powered by MikroTik RouterOS</div>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-lg-6 ">
                    <div class="banner-image"> <img src="img\saber.png" alt="" data-animate="fadeInUp" data-delay="1.4"
                            data-depth="0.2"></div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="services-title position-relative pt-7" data-bg-img="img/buildings.jpg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title text-center">
                            <h2 class="text-white" data-animate="fadeInUp" data-delay=".1">Service</h2>
                            <p class="text-white" data-animate="fadeInUp" data-delay=".3">Internet Unlimated
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="services-wrap bg-white position-relative pt-5 pb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-md-4 col-sm-6">

                        <div class="roboto text-center font-weight-medium" data-animate="fadeInUp" data-delay=".65">
                            <p>Jika ada pertanyaan silakan <a href="https://www.facebook.com/xzennt"
                                    target="_blank">Edwin Ageng</a> atau
                                <br>Whatsapp <a href="https://wa.me/6283861270513?text=ping"
                                    target="_blank">083861270513</a></p>
                        </div>
                    </div>
                </div>
    </section>

    <footer class="main-footer bg-primary pt-2">
        <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col-md-12">
                    <div class="footer-info">
                        <h3 class="text-white" data-animate="fadeInUp" data-delay="0">Kontak</h3>
                        <br>
                        <ul class="footer-contacts list-unstyled">
                            <p data-animate="fadeInUp" data-delay=".15">email: <a href="mailto:edwinageng48@gmail.com"
                                    target="_blank">edwinageng48@gmail.com</a></p>
                            <p data-animate="fadeInUp" data-delay=".2">alamat: <a
                                    href="https://goo.gl/maps/sEz658HtSmonfzD3A" target="_blank">Susukan Ngemplak
                                    RT1/6,Kabupaten Semarang</a></p>
                        </ul>
                        <ul class="social-links list-inline mb-0">
                            <li data-animate="fadeInUp" data-delay=".25"><a href="https://www.facebook.com/xzennt"
                                    target="_blank"><i class="fab fa-facebook-f"></i></a></li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="bottom-footer">
                <div class="row">
                    <div class="col-md-5 order-last order-md-first">

                    </div>
                    <div class="col-md-7 order-first order-md-last">
                        <ul class="footer-menu list-inline text-md-right mb-md-0" data-animate="fadeInDown"
                            data-delay=".95">

                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="back-to-top">
        <a href="#"> <i class="fas fa-arrow-up"></i></a>
    </div>
    <script src="js\jquery-3.2.1.min.js"></script>
    <script>
        FontAwesomeConfig = {
            searchPseudoElements: true
        };
    </script>
    <script src="js\fontawesome-all.min.js"></script>
    <script src="js\bootstrap.bundle.min.js"></script>
    <script src="plugins\typed.js\typed.min.js"></script>
    <script src="plugins\waypoints\jquery.waypoints.min.js"></script>
    <script src="plugins\waypoints\sticky.min.js"></script>
    <script src="plugins\swiper\swiper.min.js"></script>
    <script src="plugins\particles.js\particles.min.js"></script>
    <script src="plugins\particles.js\particles.settings.js"></script>
    <script src="plugins\magnific-popup\jquery.magnific-popup.min.js"></script>
    <script src="plugins\parsley\parsley.min.js"></script>
    <script src="plugins\parallax\parallax.min.js"></script>
    <script src="plugins\retinajs\retina.min.js"></script>
    <script src="js\menu.min.js"></script>
    <script src="js\scripts.js"></script>
    <script src="js\custom.js"></script>

    $(if chap-id)
    <script type="text/javascript" src="md5.js"></script>
    <script type="text/javascript">
        $('#loginForm').submit(function () {
            var password = $('#inputPassword');
            password.val(hexMD5('$(chap-id)' + password.val() + '$(chap-challenge)'));
        });
    </script>
    $(endif)
    <script>
        $("#menu-toggle").click(function (e) {
            e.preventDefault();
            $("#wrapper").toggleClass("toggled");
        });
    </script>
    <script type="text/javascript">
        <!--
        document.login.username.focus();
        //
        -->
    </script>
</body>

</html>

File: /logout.html
﻿<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Teras HOTSPOT</title>
    <link rel="shortcut icon" type="image/png" href="favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,400i,500i,700%7CRoboto:400,500,700" rel="stylesheet">
    <link rel="stylesheet" href=".\css\bootstrap.min.css">
    <link rel="stylesheet" href=".\plugins\swiper\swiper.min.css">
    <link rel="stylesheet" href=".\plugins\magnific-popup\magnific-popup.min.css">
    <link rel="stylesheet" href=".\plugins\color-switcher\color-switcher.css">
    <link rel="stylesheet" href=".\css\style.css">
    <link rel="stylesheet" href=".\css\responsive.css">
    <link rel="stylesheet" href=".\css\colors\theme-color-1.css">
    <link rel="stylesheet" href=".\css\custom.css">
</head>

<body>
    <div class="preLoader"></div>
    <header class="header">
        <div class="main-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-3 col-sm-3 col-9">
                        <div class="logo" data-animate="fadeInUp" data-delay=".7">
                            <a href="login.html"> <img src="img/icon.png"> </a>
                        </div>
                    </div>
                    <div class=" col-lg-7 col-md-5 col-sm-3 col-3">
                        <nav data-animate="fadeInUp" data-delay=".9">
                            <div class="header-menu">
                                <ul>
                                    <li><a href="login.html">Home</a></li>
                                    <li><a href="status.html">Status</a></li>
                                    <li class="active"><a href="logout.html?erase-cookie=true">Logout</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section class="position-relative bg-light pt-4 pb-4">
        <div id="particles_js"></div>
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="banner-content">
                        <div class="section-heading">
                            <h5>
                                <p>Selamat datang di layanan Teras Hotspot</p>
                            </h5>
                            <h1>Teras Hotspot Landing Page</h1>

                        </div> <!-- .section-heading -->
                        <h4 data-animate="fadeInUp" data-delay="1.4">Anda sudah Keluar dari layanan Hotspot</h4>
                        </br>
                    </div>
                    <table class="table" data-animate="fadeInUp" data-delay="1.4">
                        <tbody class="align-l">
                            <tr>
                                <td>Username</td>
                                <td>$(username)</td>
                            </tr>
                            <tr>
                                <td>IP Address</td>
                                <td>$(ip)</td>
                            </tr>
                            <tr>
                                <td>MAC Address</td>
                                <td>$(mac)</td>
                            </tr>
                            $(if session-time-left)
                            <tr>
                                <td>Connected / left</td>
                                <td>$(uptime) / $(session-time-left)</td>
                            </tr>
                            $(else)
                            <tr>
                                <td>Connected</td>
                                <td>$(uptime)</td>
                            </tr>
                            $(endif)
                            <tr>
                                <td>Download / Upload</td>
                                <td>$(bytes-out-nice) / $(bytes-in-nice)</td>
                            </tr>
                            $(if limit-bytes-total)
                            <tr>
                                <td>Sisa Kuota</td>
                                <td>$(if limit-bytes-total)
                                    <script language=javascript>
                                        result = ($(limit - bytes - total) / 1000000).toFixed(2)
                                        document.write(result)
                                    </script> MiB
                                    $(endif)
                                    $(if limit-bytes-total == '')Unlimited$(endif)</td>
                            </tr>
                            $(else)
                            <tr>
                                <td>Sisa Kuota</td>
                                <td>$(if limit-bytes-out)
                                    <script language=javascript>
                                        result = ($(limit - bytes - out) / 1000000).toFixed(2)
                                        document.write(result)
                                    </script> MiB
                                    $(endif)
                                    $(if limit-bytes-out == '')Unlimited$(endif)</td>
                            </tr>
                            $(endif)
                        </tbody>
                    </table>
                </div>
                <div class="col-lg-6 ">
                    <div class="banner-image"> <img src="img\saber.png" alt="" data-animate="fadeInUp" data-delay="1.4"
                            data-depth="0.2"></div>
                </div>
            </div>
        </div>
    </section>
    <section>
        <div class="services-title position-relative pt-7" data-bg-img="img/buildings.jpg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title text-center">
                            <h2 class="text-white" data-animate="fadeInUp" data-delay=".1">Service</h2>
                            <p class="text-white" data-animate="fadeInUp" data-delay=".3">Internet Unlimated
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="services-wrap bg-white position-relative pt-5 pb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-md-4 col-sm-6">

                        <div class="roboto text-center font-weight-medium" data-animate="fadeInUp" data-delay=".65">
                            <p>Jika ada pertanyaan silakan <a href="https://www.facebook.com/xzennt"
                                    target="_blank">Edwin Ageng</a> atau
                                <br>Whatsapp <a href="https://wa.me/6283861270513?text=ping"
                                    target="_blank">083861270513</a></p>
                        </div>
                    </div>
                </div>
    </section>

    <footer class="main-footer bg-primary pt-2">
        <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col-md-12">
                    <div class="footer-info">
                        <h3 class="text-white" data-animate="fadeInUp" data-delay="0">Kontak</h3>
                        <br>
                        <ul class="footer-contacts list-unstyled">
                            <p data-animate="fadeInUp" data-delay=".15">email: <a href="mailto:edwinageng48@gmail.com"
                                    target="_blank">edwinageng48@gmail.com</a></p>
                            <p data-animate="fadeInUp" data-delay=".2">alamat: <a
                                    href="https://goo.gl/maps/sEz658HtSmonfzD3A" target="_blank">Susukan Ngemplak
                                    RT1/6,Kabupaten Semarang</a></p>
                        </ul>
                        <ul class="social-links list-inline mb-0">
                            <li data-animate="fadeInUp" data-delay=".25"><a href="https://www.facebook.com/xzennt"
                                    target="_blank"><i class="fab fa-facebook-f"></i></a></li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="bottom-footer">
                <div class="row">
                    <div class="col-md-5 order-last order-md-first">

                    </div>
                    <div class="col-md-7 order-first order-md-last">
                        <ul class="footer-menu list-inline text-md-right mb-md-0" data-animate="fadeInDown"
                            data-delay=".95">

                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="back-to-top">
        <a href="#"> <i class="fas fa-arrow-up"></i></a>
    </div>
    <script src="js\jquery-3.2.1.min.js"></script>
    <script>
        FontAwesomeConfig = {
            searchPseudoElements: true
        };
    </script>
    <script src="js\fontawesome-all.min.js"></script>
    <script src="js\bootstrap.bundle.min.js"></script>
    <script src="plugins\typed.js\typed.min.js"></script>
    <script src="plugins\waypoints\jquery.waypoints.min.js"></script>
    <script src="plugins\waypoints\sticky.min.js"></script>
    <script src="plugins\swiper\swiper.min.js"></script>
    <script src="plugins\particles.js\particles.min.js"></script>
    <script src="plugins\particles.js\particles.settings.js"></script>
    <script src="plugins\magnific-popup\jquery.magnific-popup.min.js"></script>
    <script src="plugins\parsley\parsley.min.js"></script>
    <script src="plugins\parallax\parallax.min.js"></script>
    <script src="plugins\retinajs\retina.min.js"></script>
    <script src="js\menu.min.js"></script>
    <script src="js\scripts.js"></script>
    <script src="js\custom.js"></script>

    <script>
        $("#menu-toggle").click(function (e) {
            e.preventDefault();
            $("#wrapper").toggleClass("toggled");
        });
    </script>
    <script type="text/javascript">
        <!--
        document.login.username.focus();
        //
        -->
    </script>
</body>

</html>

File: /md5.js
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


File: /plugins\particles.js\particles.settings.js
var particlesJs='particles_js',particleTarget=$('#'+particlesJs);if(particleTarget.length){particlesJS(particlesJs,{"particles":{"number":{"value":80,"density":{"enable":true,"value_area":800}},"color":{"value":"#000000"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":0.4,"random":false,"anim":{"enable":false,"speed":1,"opacity_min":0.1,"sync":false}},"size":{"value":3,"random":true,"anim":{"enable":false,"speed":40,"size_min":0.1,"sync":false}},"line_linked":{"enable":true,"distance":150,"color":"#000000","opacity":0.5,"width":1},"move":{"enable":true,"speed":6,"direction":"none","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":false,"mode":"repulse"},"onclick":{"enable":true,"mode":"push"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});}

File: /redirect.html
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


File: /rlogin.html
﻿$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Teras HOTSPOT</title>
    <link rel="shortcut icon" type="image/png" href="favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,400i,500i,700%7CRoboto:400,500,700" rel="stylesheet">
    <link rel="stylesheet" href=".\css\bootstrap.min.css">
    <link rel="stylesheet" href=".\plugins\swiper\swiper.min.css">
    <link rel="stylesheet" href=".\plugins\magnific-popup\magnific-popup.min.css">
    <link rel="stylesheet" href=".\plugins\color-switcher\color-switcher.css">
    <link rel="stylesheet" href=".\css\style.css">
    <link rel="stylesheet" href=".\css\responsive.css">
    <link rel="stylesheet" href=".\css\colors\theme-color-1.css">
    <link rel="stylesheet" href=".\css\custom.css">
</head>

<body>
    <div class="preLoader"></div>
    <header class="header">
        <div class="main-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-3 col-sm-3 col-9">
                        <div class="logo" data-animate="fadeInUp" data-delay=".7">
                            <a href="login.html"> <img src="img/icon.png"> </a>
                        </div>
                    </div>
                    <div class="col-lg-7 col-md-5 col-sm-3 col-3">
                        <nav data-animate="fadeInUp" data-delay=".9">
                            <div class="header-menu">
                                <ul>
                                    <li class="active"><a href="login.html">Home</a></li>
                                    <li><a href="status.html">Status</a></li>
                                    <li><a href="logout.html?erase-cookie=true">Logout</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section>
        <div class="services-title position-relative pt-7" data-bg-img="img/buildings.jpg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title text-center">
                            <h2 class="text-white" data-animate="fadeInUp" data-delay=".1">Service</h2>
                            <p class="text-white" data-animate="fadeInUp" data-delay=".3">Internet Unlimated
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="services-wrap bg-white position-relative pt-5 pb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-md-4 col-sm-6">

                        <div class="roboto text-center font-weight-medium" data-animate="fadeInUp" data-delay=".65">
                            <p>Jika ada pertanyaan silakan <a href="https://www.facebook.com/xzennt"
                                    target="_blank">Edwin Ageng</a> atau
                                <br>Whatsapp <a href="https://wa.me/6283861270513?text=ping"
                                    target="_blank">083861270513</a></p>
                        </div>
                    </div>
                </div>
    </section>

    <footer class="main-footer bg-primary pt-2">
        <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col-md-12">
                    <div class="footer-info">
                        <h3 class="text-white" data-animate="fadeInUp" data-delay="0">Kontak</h3>
                        <br>
                        <ul class="footer-contacts list-unstyled">
                            <p data-animate="fadeInUp" data-delay=".15">email: <a href="mailto:edwinageng48@gmail.com"
                                    target="_blank">edwinageng48@gmail.com</a></p>
                            <p data-animate="fadeInUp" data-delay=".2">alamat: <a
                                    href="https://goo.gl/maps/sEz658HtSmonfzD3A" target="_blank">Susukan Ngemplak
                                    RT1/6,Kabupaten Semarang</a></p>
                        </ul>
                        <ul class="social-links list-inline mb-0">
                            <li data-animate="fadeInUp" data-delay=".25"><a href="https://www.facebook.com/xzennt"
                                    target="_blank"><i class="fab fa-facebook-f"></i></a></li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="bottom-footer">
                <div class="row">
                    <div class="col-md-5 order-last order-md-first">

                    </div>
                    <div class="col-md-7 order-first order-md-last">
                        <ul class="footer-menu list-inline text-md-right mb-md-0" data-animate="fadeInDown"
                            data-delay=".95">

                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="back-to-top">
        <a href="#"> <i class="fas fa-arrow-up"></i></a>
    </div>
    <script src="js\jquery-3.2.1.min.js"></script>
    <script>
        FontAwesomeConfig = {
            searchPseudoElements: true
        };
    </script>
    <script src="js\fontawesome-all.min.js"></script>
    <script src="js\bootstrap.bundle.min.js"></script>
    <script src="plugins\typed.js\typed.min.js"></script>
    <script src="plugins\waypoints\jquery.waypoints.min.js"></script>
    <script src="plugins\waypoints\sticky.min.js"></script>
    <script src="plugins\swiper\swiper.min.js"></script>
    <script src="plugins\particles.js\particles.min.js"></script>
    <script src="plugins\particles.js\particles.settings.js"></script>
    <script src="plugins\magnific-popup\jquery.magnific-popup.min.js"></script>
    <script src="plugins\parsley\parsley.min.js"></script>
    <script src="plugins\parallax\parallax.min.js"></script>
    <script src="plugins\retinajs\retina.min.js"></script>
    <script src="js\menu.min.js"></script>
    <script src="js\scripts.js"></script>
    <script src="js\custom.js"></script>
</body>

</html>

File: /status.html
﻿<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Teras HOTSPOT</title>
    $(if refresh-timeout)
    <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
    $(endif)
    <link rel="shortcut icon" type="image/png" href="favicon.png">
    <link href="https://fonts.googleapis.com/css?family=Cabin:400,400i,500i,700%7CRoboto:400,500,700" rel="stylesheet">
    <link rel="stylesheet" href=".\css\bootstrap.min.css">
    <link rel="stylesheet" href=".\plugins\swiper\swiper.min.css">
    <link rel="stylesheet" href=".\plugins\magnific-popup\magnific-popup.min.css">
    <link rel="stylesheet" href=".\plugins\color-switcher\color-switcher.css">
    <link rel="stylesheet" href=".\css\style.css">
    <link rel="stylesheet" href=".\css\responsive.css">
    <link rel="stylesheet" href=".\css\colors\theme-color-1.css">
    <link rel="stylesheet" href=".\css\custom.css">
</head>

<body>
    <div class="preLoader"></div>
    <header class="header">
        <div class="main-header">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-2 col-md-3 col-sm-3 col-9">
                        <div class="logo" data-animate="fadeInUp" data-delay=".7">
                            <a href="login.html"> <img src="img/icon.png"> </a>
                        </div>
                    </div>
                    <div class="col-lg-7 col-md-5 col-sm-3 col-3">
                        <nav data-animate="fadeInUp" data-delay=".9">
                            <div class="header-menu">
                                <ul>
                                    <li><a href="login.html">Home</a></li>
                                    <li class="active"><a href="status.html">Status</a></li>
                                    <li><a href="logout.html?erase-cookie=true">Logout</a></li>
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section class="position-relative bg-light pt-4 pb-4">
        <div id="particles_js"></div>
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="banner-content">
                        <div class="section-heading">
                            <h5>
                                <p>Selamat datang di layanan Teras Hotspot</p>
                            </h5>
                            <h1>Teras Hotspot Landing Page</h1>

                        </div> <!-- .section-heading -->
                    </div>
                    <table class="table" data-animate="fadeInUp" data-delay="1.4">
                        <tbody class="align-l">
                            <tr>
                                <td>Username</td>
                                <td>$(username)</td>
                            </tr>
                            <tr>
                                <td>IP Address</td>
                                <td>$(ip)</td>
                            </tr>
                            <tr>
                                <td>MAC Address</td>
                                <td>$(mac)</td>
                            </tr>
                            $(if session-time-left)
                            <tr>
                                <td>Connected / left</td>
                                <td>$(uptime) / $(session-time-left)</td>
                            </tr>
                            $(else)
                            <tr>
                                <td>Connected</td>
                                <td>$(uptime)</td>
                            </tr>
                            $(endif)
                            <tr>
                                <td>Download / Upload</td>
                                <td>$(bytes-out-nice) / $(bytes-in-nice)</td>
                            </tr>
                            $(if limit-bytes-total)
                            <tr>
                                <td>Sisa Kuota</td>
                                <td>$(if limit-bytes-total)
                                    <script language=javascript>
                                        result = ($(limit - bytes - total) / 1000000).toFixed(2)
                                        document.write(result)
                                    </script> MiB
                                    $(endif)
                                    $(if limit-bytes-total == '')Unlimited$(endif)</td>
                            </tr>
                            $(else)
                            <tr>
                                <td>Sisa Kuota</td>
                                <td>$(if limit-bytes-out)
                                    <script language=javascript>
                                        result = ($(limit - bytes - out) / 1000000).toFixed(2)
                                        document.write(result)
                                    </script> MiB
                                    $(endif)
                                    $(if limit-bytes-out == '')Unlimited$(endif)</td>
                            </tr>
                            $(endif)
                            $(if refresh-timeout)
                            <tr>
                                <td>Status refresh</td>
                                <td>$(refresh-timeout)</td>
                            </tr>
                            $(endif)
                        </tbody>
                    </table>
                </div>
                <div class="col-lg-6 ">
                    <div class="banner-image"> <img src="img\saber.png" alt="" data-animate="fadeInUp" data-delay="1.4"
                            data-depth="0.2"></div>
                </div>
            </div>
        </div>
    </section>
    <section>
        <div class="services-title position-relative pt-7" data-bg-img="img/buildings.jpg">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title text-center">
                            <h2 class="text-white" data-animate="fadeInUp" data-delay=".1">Service</h2>
                            <p class="text-white" data-animate="fadeInUp" data-delay=".3">Internet Unlimated
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="services-wrap bg-white position-relative pt-5 pb-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-md-4 col-sm-6">

                        <div class="roboto text-center font-weight-medium" data-animate="fadeInUp" data-delay=".65">
                            <p>Jika ada pertanyaan silakan <a href="https://www.facebook.com/xzennt"
                                    target="_blank">Edwin Ageng</a> atau
                                <br>Whatsapp <a href="https://wa.me/6283861270513?text=ping"
                                    target="_blank">083861270513</a></p>
                        </div>
                    </div>
                </div>
    </section>

    <footer class="main-footer bg-primary pt-2">
        <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col-md-12">
                    <div class="footer-info">
                        <h3 class="text-white" data-animate="fadeInUp" data-delay="0">Kontak</h3>
                        <br>
                        <ul class="footer-contacts list-unstyled">
                            <p data-animate="fadeInUp" data-delay=".15">email: <a href="mailto:edwinageng48@gmail.com"
                                    target="_blank">edwinageng48@gmail.com</a></p>
                            <p data-animate="fadeInUp" data-delay=".2">alamat: <a
                                    href="https://goo.gl/maps/sEz658HtSmonfzD3A" target="_blank">Susukan Ngemplak
                                    RT1/6,Kabupaten Semarang</a></p>
                        </ul>
                        <ul class="social-links list-inline mb-0">
                            <li data-animate="fadeInUp" data-delay=".25"><a href="https://www.facebook.com/xzennt"
                                    target="_blank"><i class="fab fa-facebook-f"></i></a></li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="bottom-footer">
                <div class="row">
                    <div class="col-md-5 order-last order-md-first">

                    </div>
                    <div class="col-md-7 order-first order-md-last">
                        <ul class="footer-menu list-inline text-md-right mb-md-0" data-animate="fadeInDown"
                            data-delay=".95">

                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="back-to-top">
        <a href="#"> <i class="fas fa-arrow-up"></i></a>
    </div>
    <script src="js\jquery-3.2.1.min.js"></script>
    <script>
        FontAwesomeConfig = {
            searchPseudoElements: true
        };
    </script>
    <script src="js\fontawesome-all.min.js"></script>
    <script src="js\bootstrap.bundle.min.js"></script>
    <script src="plugins\typed.js\typed.min.js"></script>
    <script src="plugins\waypoints\jquery.waypoints.min.js"></script>
    <script src="plugins\waypoints\sticky.min.js"></script>
    <script src="plugins\swiper\swiper.min.js"></script>
    <script src="plugins\particles.js\particles.min.js"></script>
    <script src="plugins\particles.js\particles.settings.js"></script>
    <script src="plugins\magnific-popup\jquery.magnific-popup.min.js"></script>
    <script src="plugins\parsley\parsley.min.js"></script>
    <script src="plugins\parallax\parallax.min.js"></script>
    <script src="plugins\retinajs\retina.min.js"></script>
    <script src="js\menu.min.js"></script>
    <script src="js\scripts.js"></script>
    <script src="js\custom.js"></script>

    <script>
        $("#menu-toggle").click(function (e) {
            e.preventDefault();
            $("#wrapper").toggleClass("toggled");
        });
    </script>
    <script type="text/javascript">
        <!--
        document.login.username.focus();
        //
        -->
    </script>
</body>

</html>

