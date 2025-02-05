# Repository Information
Name: mikrotik-capsman-ipam

# Directory Structure
Directory structure:
└── github_repos/mikrotik-capsman-ipam/
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
    │   │       ├── pack-6bc489b4d3b902702ea3543b889dd81555868b2e.idx
    │   │       └── pack-6bc489b4d3b902702ea3543b889dd81555868b2e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── api.php
    ├── arp.php
    ├── config.php
    ├── db_connect.php
    ├── delete.php
    ├── edit.php
    ├── hostscan.php
    ├── index.php
    ├── insert.php
    ├── ipam_sqlite.db
    ├── maclookup.php
    ├── nmap.php
    ├── poll.php
    ├── README.md
    └── routeros-api/
        ├── composer.json
        ├── examples/
        │   ├── example1.php
        │   ├── example2.php
        │   ├── example3.php
        │   ├── example4.php
        │   ├── example5.php
        │   └── example6.php
        ├── README.md
        └── routeros_api.class.php


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
	url = https://github.com/germaguire/mikrotik-capsman-ipam.git
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
0000000000000000000000000000000000000000 011a4d82facaa303f66a51f113e5328126173748 vivek-dodia <vivek.dodia@icloud.com> 1738606087 -0500	clone: from https://github.com/germaguire/mikrotik-capsman-ipam.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 011a4d82facaa303f66a51f113e5328126173748 vivek-dodia <vivek.dodia@icloud.com> 1738606087 -0500	clone: from https://github.com/germaguire/mikrotik-capsman-ipam.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 011a4d82facaa303f66a51f113e5328126173748 vivek-dodia <vivek.dodia@icloud.com> 1738606087 -0500	clone: from https://github.com/germaguire/mikrotik-capsman-ipam.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
011a4d82facaa303f66a51f113e5328126173748 refs/remotes/origin/main


File: /.git\refs\heads\main
011a4d82facaa303f66a51f113e5328126173748


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /api.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
	<title>Mikrotik API</title>	
</head>
<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link active" aria-current="page">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link" >Poll Devices</a></li>
</ul>
</header>

<div style="width: 500px; margin: 20px auto;">
<h3>Mikrotik API Details</h3>

<?php
include "config.php";
include "db_connect.php";
	
require('routeros-api/routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = false;
 
$neigh = "0";
$added = "0";

if ($API->connect($mikrotik, $muser, $mpass)) {

//////////////////  Mikrotik Identity  //////////////////////////////

   $ARRAY = $API->comm("/system/identity/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));

	foreach($ARRAY as $row){

		$ip = $mikrotik;
		$mac = $row['mac-address'];
		$hostname = $row['name'];
		$arr = explode(".",$ip);
		$id = $arr[3];
		
		// Makes query with post data
		$queryid1 = "UPDATE devices set mac='$mac', hostname='$hostname', model='$model' WHERE ip='$ip'";
		$db->exec($queryid1);
		
		if($ip) {
			// Makes query with post data
			$queryid2 = "INSERT INTO devices (id, iptype, ip, mac, hostname, model) VALUES ('$id', 'M', '$ip', '$mac', '$hostname', '$model')";
			if( $db->exec($queryid2) ){
//				echo $ip."  - ".$mac."<br>";
			}
		}
	}
	echo "<P> Updated Mikrotik Identity Information";

//////////////////  Mikrotik Model  //////////////////////////////

   $ARRAY = $API->comm("/system/routerboard/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));

	foreach($ARRAY as $row){

		$ip = $mikrotik;
		$model = $row['model'];
		$arr = explode(".",$ip);
		$id = $arr[3];
		
		// Makes query with post data
		$querymodel = "UPDATE devices set mac='$mac', hostname='$hostname', model='$model' WHERE ip='$ip'";
		$db->exec($querymodel);
		
		if($ip) {
			// Makes query with post data
			$querymodel2 = "INSERT INTO devices (id, iptype, ip, mac, hostname, model) VALUES ('$id', 'M', '$ip', '$mac', '$hostname', '$model')";
			if( $db->exec($querymodel2) ){
//				echo $ip."  - ".$mac."<br>";
			}
		}
	}
	echo "<P> Updated Mikrotik Identity Information";

//////////////////  Neighbours  //////////////////////////////

   $ARRAY = $API->comm("/ip/neighbor/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));

	foreach($ARRAY as $row){

		$ip = $row['address'];
		$mac = $row['mac-address'];
		$hostname = $row['identity'];
		$model = $row['board'];
		$arr = explode(".",$ip);
		$id = $arr[3];
		
		// Makes query with post data
		$queryneigh = "UPDATE devices set mac='$mac', hostname='$hostname', model='$model' WHERE ip='$ip'";
		$db->exec($queryneigh);
		
		if($ip) {
			// Makes query with post data
			$queryneigh2 = "INSERT INTO devices (id, iptype, ip, mac, hostname, model) VALUES ('$id', 'M', '$ip', '$mac', '$hostname', '$model')";
			if( $db->exec($queryneigh2) ){
				$neigh = $neigh+1;
//				echo $ip."  - ".$mac."<br>";
			}
		}
	}
	echo "<P> Updated Neighbors Information";
	echo "<P>Added ".$neigh." devices to DB.<P>";

//////////////////  ARP  //////////////////////////////

   $ARRAY = $API->comm("/ip/arp/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));

	foreach($ARRAY as $row){

		$ip = $row['address'];
		$mac = $row['mac-address'];
		$arr = explode(".",$ip);
		$id = $arr[3];
		
		// Makes query with post data
		$query = "UPDATE devices set mac='$mac' WHERE ip='$ip'";
		$db->exec($query);
		
		if($mac) {
			// Makes query with post data
//			$queryi = "INSERT INTO devices (id, iptype, ip, mac) VALUES ('$id', 'M', '$ip', '$mac')";
//			if( $db->exec($queryi) ){
//				$added = $added+1;
//				echo $ip."  - ".$mac."<br>";
//			}
		}
	}
	echo "<P> Updated IP ARP Information";
	echo "<P>Added ".$added." devices to DB.<P>";

//////////////////  Clear WIFI Stats  //////////////////////////////

	// Clear WIFI and AP Stats from DB
	$querywd = "UPDATE devices set ap='', snr='' ";
	$db->exec($querywd);

//////////////////  CAPSMAN  //////////////////////////////

   $ARRAY = $API->comm("/caps-man/registration-table/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));

	$updated="0";
	
	foreach($ARRAY as $row){

//		print_r($row);
//		echo "<P>";
		
		$mac = $row['mac-address'];
		$ap = $row['interface'];
		$snr = $row['rx-signal'];		
		
		// Makes query with post data
		$queryw = "UPDATE devices set ap='$ap', snr='$snr' WHERE mac='$mac'";

		if( $db->exec($queryw) ){
			$updated = $updated+1;
//			echo $mac." - ".$ap."  - ".$snr."<br>";
		}
	}

		echo "<P>Updated CAPSMAN Information";
		echo "<P>Updated ".$updated." devices in DB.<P>";		


/////////////////  Wireless Registrations  //////////////////////////////


   $ARRAY = $API->comm("/interface/wireless/registration-table/print", array(
//      "value-list"=> "",
      "~active-address" => "1.1.",
   ));
	
	foreach($ARRAY as $row){
		
		$mac = $row['mac-address'];
//		$ap = $row['interface'];
		$ap = "ap";
		$signal = $row['signal-strength'];
		$arr = explode("@",$signal);
		$snr = $arr[0];
		
		// Makes query with post data
		$querywr = "UPDATE devices set ap='$ap', snr='$snr' WHERE mac='$mac'";

		if( $db->exec($querywr) ){
			$updated = $updated+1;
//			echo $mac."  ".$snr."<br>";
		}
	}

		echo "<P>Updated Wireless Registration Information";
		echo "<P>Updated ".$updated." devices in DB.<P>";


//////////////////  DHCP  //////////////////////////////

   $ARRAY = $API->comm("/ip/dhcp-server/lease/print", array(
//      "value-list"=> "",
//      "~active-address" => "1.1.",
   ));

	$updated="0";
	
	foreach($ARRAY as $row){
//		print_r($row);
//		echo "<P>";
		
		$ip = $row['address'];
		$hostname = $row['host-name'];
		$dhcp = $row['comment'];		

//		echo " --> ".$ip." ".$hostname." ".$dhcp;
//		echo "<P>";

		// Makes query with post data
		$queryd = "UPDATE devices set hostname='$hostname', dhcp='$dhcp' WHERE ip='$ip'";
//		$db->exec($queryd);
		if( $db->exec($queryd) ){
			$updated = $updated+1;
//			echo $ip." - ".$hostname."  - ".$dhcp."<br>";
		}
	}

		echo "<P> Updated DHCP Lease Information";
		echo "<P>Updated ".$updated." devices in DB.<P>";	
		
   $API->disconnect();

}



?>

	<P><a href="index.php">Back to Device List</a>

	</div>
</body>
</html>



File: /arp.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
	<title>ARP Scan</title>	
</head>

<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link active" aria-current="page">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

	<div style="width: 500px; margin: 20px auto;">
	
	<?php

	echo "<H3>ARP Scan</H3>";
	
	include "config.php";
	include "db_connect.php";
	
	exec("arp -n |grep :", $output, $status);

	$added = "0";
	$updated = "0";
	$count = "0";
	
	$arrlength = count($output);
	
	for($x = 0; $x < $arrlength; $x++) {

		$row = $output[$x];	
		
		$stripped = trim(preg_replace('/\s+/', ' ', $row));
		
		$a = explode(" ",$stripped);

		$ip = $a[0];
		$mac = $a[2];
		$mac = strtoupper($mac);

		$arr = explode(".",$ip);
		$id = $arr[3];

		// Update MAC Addresses
		$queryu = "UPDATE devices set mac='$mac' WHERE ip='$ip'";
		if( $db->exec($queryu) ){
			$updated = $updated+1;
//			echo "<BR>IP : ".$ip." MAC : ".$mac."<br>";	
		}

		// Makes query with post data
		$querya = "INSERT INTO devices (id, ip, iptype, mac) VALUES ('$id', '$ip', 'A', '$mac')";
		// Executes the query
		if( $db->exec($querya) ){
			$added = $added+1;		
			echo "<BR>IP : ".$ip." MAC : ".$mac."<br>";	
		}

	}

	echo "<P><BR>Updated ".$updated." devices to DB.";
	echo "<P>Added ".$added." devices to DB.";
	

	?>
	<P><a href="index.php">Back to Device List</a>
	

	</div>
</div>
</body>
</html>


File: /config.php
<?php

$mikrotik = "192.168.88.1";
$muser = "testuser";
$mpass = "testpassword";

$targetnet = "192.168.88.0/24";

?>




File: /db_connect.php
<?php
// Database name
$database_name = "ipam_sqlite.db";

// Database Connection
$db = new SQLite3($database_name);

// Create Table "devices" into Database if not exists 
$query = "CREATE TABLE IF NOT EXISTS devices (id string, ping STRING, iptype STRING, ip STRING PRIMARY KEY NOT NULL, name STRING, hostname STRING, dhcp STRING, model STRING, mac STRING, ap STRING, snr STRING)";
$db->exec($query);


?>

File: /delete.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
	<title>Delete Device</title>	
</head>
<body>
 
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link active" aria-current="page">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

<div style="width: 500px; margin: 20px auto;">
<h3>Device Delete</h3>

<?php

// Includs database connection
include "db_connect.php";

$id = $_GET['id']; // rowid from url

// Prepar the deleting query according to rowid
$query = "DELETE FROM devices WHERE id=$id";

// Run the query to delete record
if( $db->query($query) ){
	$message = "Record is deleted successfully.";
}else {
	$message = "Sorry, Record is not deleted.";
}

echo $message;
?>
<P><a href="index.php">Back to List</a>
</div>
</div>
</body>
</html>


File: /edit.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
	<title>Update Device</title>
</head>

<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link active" aria-current="page">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>


<div style="width: 500px; margin: 20px auto;">

<h3>Edit Device</h3>

<?php

$message = ""; // initial message 

include "db_connect.php";

// Updating the table row with submited data according to rowid once form is submited 
if( isset($_POST['submit_data']) ){

	// Gets the data from post
	$id = $_POST['id'];
	$iptype = $_POST['iptype'];
	$ip = $_POST['ip'];
	$name = $_POST['name'];
	$hostname = $_POST['hostname'];
	$dhcp = $_POST['dhcp'];
	$model = $_POST['model'];
	$mac = $_POST['mac'];

	$arr = explode(".",$ip);
	$id = $arr[3];
	
	// Makes query with post data
	$query = "UPDATE devices set iptype='$iptype', id='$id', ip='$ip', name='$name', hostname='$hostname', dhcp='$dhcp', model='$model', mac='$mac' WHERE id=$id";
	
	// Executes the query
	if( $db->exec($query) ){
		$message = "Data is updated successfully.";
	}else{
		$message = "Sorry, Data is not updated.";
	}
}

$id = $_GET['id']; // rowid from url
// Prepar the query to get the row data with rowid
$query = "SELECT rowid, * FROM devices WHERE id=$id";
$result = $db->query($query);
$data = $result->fetchArray(); // set the row in $data

?>

		<div><?php echo $message;?></div>
		
		<div class="table-responsive">
		<table class="table table-striped border-primary">
			<form action="" method="post">
			<input type="hidden" name="id" value="<?php echo $id;?>">
			<tr>
				<td>Type:</td>
				<td><input name="iptype" type="text" value="<?php echo $data['iptype'];?>"></td>
				</td>
			</tr>			
			<tr>
				<td>IP:</td>
				<td><input name="ip" type="text" value="<?php echo $data['ip'];?>"></td>
			</tr>
			<tr>
				<td>Name:</td>
				<td><input name="name" type="text" value="<?php echo $data['name'];?>"></td>
			</tr>
			<tr>
				<td>Hostame:</td>
				<td><input name="hostname" type="text" value="<?php echo $data['hostname'];?>"></td>
			</tr>			
			<tr>
				<td>DHCP:</td>
				<td><input name="dhcp" type="text" value="<?php echo $data['dhcp'];?>"></td>
			</tr>	
			<tr>
				<td>Model:</td>
				<td><input name="model" type="text" value="<?php echo $data['model'];?>"></td>
			</tr>
			<tr>
				<td>MAC:</td>
				<td><input name="mac" type="text" value="<?php echo $data['mac'];?>"></td>
			</tr>			
			<tr>
				<td></td>
				<td><button class="w-50 btn btn btn-primary" name="submit_data" type="submit">Update Data</button>
				</td>
			</tr>
			</form>
		</table>
		</div>	
	</div>
</div>	
</body>
</html>


File: /hostscan.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />	
	<title>Scan Device</title>	
</head>

<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

<?php

// Includs database connection
include "db_connect.php";

$id = $_GET['id']; // rowid from url

// Prepar the query to get the row data with rowid
$query = "SELECT rowid, * FROM devices WHERE id=$id";
$result = $db->query($query);

$data = $result->fetchArray(); // set the row in $data
?>

	<div style="width: 500px; margin: 20px auto;">

	<?php

	$ip = $data['ip'];
	$name = $data['name'];
	echo "<h3> ".$ip." Status</h3><P> Name: ".$name."<P>";

	$target = $data['ip'];

	// Required /etc/sudoers/nmap file (www-data ALL=(ALL) NOPASSWD: /usr/bin/nmap)
	exec("sudo nmap -O $target", $output, $status);
	echo "<P>";
	$arrlength = count($output);
	for($x = 0; $x < $arrlength; $x++) {
		echo " ".$output[$x]." <BR>";	
	}


	?>
	<P><a href="index.php">Back to Device List</a>

	</div>
</div>	
</body>
</html>


File: /index.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />	
	<title>Devices</title>
</head>
<body>
 
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link active" aria-current="page">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

 
<?php
include "config.php";
include "db_connect.php";

$sort = $_GET['sort'];

if( $sort == "snr" )
{
	$query = "SELECT rowid, * FROM devices ORDER BY snr";
}
elseif( $sort == "ap" )
{
	$query = "SELECT rowid, * FROM devices ORDER BY ap DESC";
}
elseif( $sort == "name" )
{
	$query = "SELECT rowid, * FROM devices ORDER BY name DESC";
}
elseif( $sort == "hostname" )
{
	$query = "SELECT rowid, * FROM devices ORDER BY hostname DESC";
}
else
{
	$query = "SELECT rowid, * FROM devices ORDER BY id";
}
	

// Run the query and set query result in $result
// Here $db comes from "db_connection.php"
$result = $db->query($query);
$count = "0";
?>
<!--	<div style="width: 900px; margin: 20px auto;"> -->
	<div>

		<div class="table-responsive">
		<table class="table table-striped border-primary">
			<tr>
				<td>Ping</td>
				<td><a href="index.php">IP Address</a></td>
				<td><a href="index.php?sort=name">Name</a></td>
				<td><a href="index.php?sort=hostname">Hostname</a></td>
				<td>DHCP Comment</td>
				<td>Model</td>
				<td>MAC</td>
				<td>Type</td>				
				<td><a href="index.php?sort=ap">AP</a></td>
				<td><a href="index.php?sort=snr">SNR</a></td>
				<td>Action</td>
				
			</tr>
			
			<?php while($row = $result->fetchArray()) {?>
			<?php $count = $count+1;?>
			<tr>
				<td>
					<?php
						$color = $row['ping'];
						if ($color == 'R') 
						{
							?><i class="fa fa-times-circle" style="color:red"><?php
						}
						elseif ($color == 'Y')
						{
							?><i class="fa fa-exclamation-circle" style="color:orange"><?php	
						}
						elseif ($color == 'G')
						{
							?><i class="fa fa-check-circle" style="color:green"><?php
						}	
						//echo $row['ping'];
					?>
				</td>
				<td><?php echo $row['ip'];?></td>
				<td><?php echo $row['name'];?></td>
				<td><?php echo $row['hostname'];?></td>
				<td><?php echo $row['dhcp'];?></td>
				<td><?php echo $row['model'];?></td>
				<td><a href="maclookup.php?id=<?php echo $row['id'];?>"><?php echo $row['mac'];?></a></td>
				<td><?php echo $row['iptype'];?></td>				
				<td><?php echo $row['ap'];?></td>
				<td><?php echo $row['snr'];?></td>
				<td>
					<a href="edit.php?id=<?php echo $row['id'];?>">Edit</a> 
					<a href="delete.php?id=<?php echo $row['id'];?>" onclick="return confirm('Are you sure?');">Delete</a> <BR>
					<a href="hostscan.php?id=<?php echo $row['id'];?>">Scan</a>
	
				</td>
			</tr>
			<?php } ?>
		</table>
		</div>
		<P>There are <?php echo $count;?> devices in DB.
	</div>  </div>
</body>
</html>


File: /insert.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
		<title>Add Device</title>
</head>
<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="index.php" class="nav-link active" aria-current="page">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

<div style="width: 500px; margin: 20px auto;">

<h3>Add Device</h3>

<?php
$message = ""; // initial message 

if( isset($_POST['submit_data']) ){

	// Includs database connection
	include "db_connect.php";

	// Gets the data from post
	$iptype = $_POST['iptype'];
	$ip = $_POST['ip'];
	$name = $_POST['name'];
	$model = $_POST['model'];
	$mac = $_POST['mac'];

	$arr = explode(".",$ip);
	$id = $arr[3];
	
	// Makes query with post data
	$query = "INSERT INTO devices (iptype, id, ip, name, model, mac) VALUES ('$iptype', '$id', '$ip', '$name', '$model', '$mac')";
	
	// Executes the query
	// If data inserted then set success message otherwise set error message
	// Here $db comes from "db_connection.php"
	if( $db->exec($query) ){
		$message = "Data is inserted successfully.";
	}else{
		$message = "Sorry, Data is not inserted.";
	}
}
?>

		<!-- showing the message here-->
		<div><?php echo $message;?></div>

		<div class="table-responsive">
		<table class="table table-striped border-primary">
			<form action="insert.php" method="post">
			<tr>
				<td>Type:</td>
				<td><input type="checkbox" id="iptype" name="iptype" value="S" checked><label for="iptype"> Static</label></td>
			</tr>
			<tr>
				<td>IP:</td>
				<td><input name="ip" type="text"></td>
			</tr>
			<tr>
				<td>Name:</td>
				<td><input name="name" type="text"></td>
			</tr>
			<tr>
				<td>Model:</td>
				<td><input name="model" type="text"></td>
			</tr>
			<tr>
				<td>MAC:</td>
				<td><input name="mac" type="text"></td>
			</tr>		
			<tr>
				<td></td>
				<td><button class="w-50 btn btn btn-primary" name="submit_data" type="submit">Update Data</button>
			</tr>
			</form>
		</table>
		</div>
	</div>
</div>
</body>
</html>


File: /maclookup.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />	
	<title>MAC Lookup</title>	
</head>
<body>
 
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link active" aria-current="page">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>


<div style="width: 500px; margin: 20px auto;">
<h3>MAC Lookup</h3>

<?php

// Includs database connection
include "db_connect.php";

$id = $_GET['id']; // rowid from url

// Prepar the query to get the row data with rowid
$query = "SELECT rowid, * FROM devices WHERE id=$id";
$result = $db->query($query);

$data = $result->fetchArray(); // set the row in $data

$mac_address = $data['mac'];

//  $mac_address = "FC:FB:FB:01:FA:21";

  $url = "https://api.macvendors.com/" . urlencode($mac_address);
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $response = curl_exec($ch);

  if($response) {
    echo "MAC Lookup: <P> $response";
  } else {
    echo "Not Found";
  }
?>

	<P><a href="index.php">Back to Device List</a>

	</div>
</div>	
</body>
</html>




File: /nmap.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />		
	<title>NMAP Scan</title>	
</head>

<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="#" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link active" aria-current="page">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link">Poll Devices</a></li>
</ul>
</header>

	<div style="width: 500px; margin: 20px auto;">

	<?php

	include "config.php";
	include "db_connect.php";
	
	echo "<H3>Scan ".$targetnet." </H3><br>";
	
	exec("nmap -sn -n -oG - $targetnet |grep Up|cut -d ' ' -f2", $output, $status);

	$added = "0";

	$arrlength = count($output);
	
	for($x = 0; $x < $arrlength; $x++) {

		$ip = $output[$x];
		$arr = explode(".",$ip);
		$id = $arr[3];

		// Makes query with post data
		$querya = "INSERT INTO devices (id, ip, iptype) VALUES ('$id', '$ip', 'N')";
		// Executes the query
		if( $db->exec($querya) ){
			$added = $added+1;		
			echo "<BR>IP : ".$ip."<br>";	
		}
	}

	echo "<P>Added ".$added." devices to DB."

	?>
	<P><a href="index.php">Back to Device List</a>

	</div>
</div>	
</body>
</html>


File: /poll.php
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="icon" type="image/png" href="favicon.png" />	
	<title>Poll Devices</title>
</head>

<body>
<div class="container">
<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
<a href="index.php" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
<svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
<span class="fs-4">Mikrotik IPAM</span>
</a>

<ul class="nav nav-pills">
<li class="nav-item"><a href="index.php" class="nav-link">Devices</a></li>
<li class="nav-item"><a href="insert.php" class="nav-link">Add Device</a></li>
<li class="nav-item"><a href="arp.php" class="nav-link">ARP Scan</a></li>
<li class="nav-item"><a href="nmap.php" class="nav-link">NMAP Scan</a></li>
<li class="nav-item"><a href="api.php" class="nav-link">Mikrotik API</a></li>
<li class="nav-item"><a href="poll.php" class="nav-link active" aria-current="page">Poll Devices</a></li>
</ul>
</header>

<div style="width: 500px; margin: 20px auto;">
<h3>Poll Details</h3><P>

<?php

// Includs database connection
include "db_connect.php";

// Makes query with rowid
//$query = "SELECT * FROM devices WHERE iptype='S'";
$query = "SELECT * FROM devices ";
$result = $db->query($query);

$online = 0;
$offline = 0;

	// Clear WIFI and AP Stats from DB
	$querywd = "UPDATE devices set ping='' ";
	$db->exec($querywd);

while($row = $result->fetchArray()) {

	$ip = $row['ip'];
	exec("fping $ip", $output, $status);
		
		if (strpos($output, 'alive') !== false) 
		  {
			$ping = 'G';
			$online = $online+1;
		  }
		else
		  {
			$ping = 'R';
			$offline = $offline+1;
		  }
//		echo $ip." - ".$ping."<BR>";

		// Update MAC Addresses
		$queryu = "UPDATE devices set ping='$ping' WHERE ip='$ip'";

		if( $db->query($queryu) ){
			$message = "Record is updated successfully.";
		}else {
			$message = "Sorry, Record is not udated.";	
		}
//		echo $message;

}

	echo "<P>Online : ".$online;
	echo "<P>Offline : ".$offline;

?>

	<P><a href="index.php">Back to Device List</a>

	</div>
</div>	
</body>
</html>


File: /README.md
mikrotik-capsman-ipam
=============

## Mikrotik CAPSMAN IPAM Features:
* Add/Edit/Delete IP address
* Add ARP Scan details (ip, mac)
* Add NMAP details (ip, mac)
* Add Mikrotik Neighbours details (ip, mac, hostname, model)
* Add Mikrotik DHCP details (ip, mac, hostname, DHCP Comment)
* Update Mikrotik CAPSMAN Registration details (ap, mac, snr)
* Update Mikrotik Wireless Registration details (mac, snr)
* Update Mikrotik Details
  * system identity (hostname)
  * routerboard model (model)
* NMAP hostscan
* MAC Address Lookup
* Fping device polling
* SQLite database.

## Requirements:
* Tested on ubuntu bionic with following packages.
  * apt-get install apache2 php7.2 libapache2-mod-php libapache2-mod-php7.2 php7.2-sqlite3 nmap fping

* Enable Mikrotik API service (create read only user for accessing API details).

* NMAP installed using sudo required for OS Scanning, create /etc/sudoers/nmap file 
  * www-data ALL=(ALL) NOPASSWD: /usr/bin/nmap


## Thanks to:
https://github.com/BenMenking/routeros-api

## Screenshot:
![alt text](https://github.com/germaguire/mikrotik-capsman-ipam/blob/main/devices.png?raw=true)



File: /routeros-api\composer.json
{
    "name": "BenMenking/routeros-api",
    "description": "Client API for RouterOS/Mikrotik",
    "keywords": [
        "routeros",
        "mikrotik"
    ],
    "type": "library",
    "support": {
        "issues": "https://github.com/BenMenking/routeros-api/issues",
        "wiki": "http://wiki.mikrotik.com/wiki/API_PHP_class",
        "source": "https://github.com/BenMenking/routeros-api"
    },
    "authors": [
        {
            "name": "Denis Basta",
            "email": "Denis.Basta@gmail.com"
        },
        {
            "name": "Nick Barnes"
        },
        {
            "name": "Ben Menking",
            "email": "ben@infotechsc.com"
        },
        {
            "name": "Jeremy Jefferson",
            "url": "http://jeremyj.com"
        },
        {
            "name": "Cristian Deluxe",
            "url": "djcristiandeluxe@gmail.com"
        },
        {
            "name": "Mikhail Moskalev",
            "url": "mmv.rus@gmail.com"
        }
    ],
    "autoload": {
        "classmap": [
            "routeros_api.class.php"
        ]
    }
}

File: /routeros-api\examples\example1.php
<?php

require('../routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = true;

if ($API->connect('111.111.111.111', 'LOGIN', 'PASSWORD')) {

   $API->write('/interface/getall');

   $READ = $API->read(false);
   $ARRAY = $API->parseResponse($READ);

   print_r($ARRAY);

   $API->disconnect();

}

?>


File: /routeros-api\examples\example2.php
<?php

require('../routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = true;

if ($API->connect('111.111.111.111', 'LOGIN', 'PASSWORD')) {

   $API->write('/interface/wireless/registration-table/print',false);
   $API->write('=stats=');
 
   $READ = $API->read(false);
   $ARRAY = $API->parseResponse($READ);

   print_r($ARRAY);

   $API->disconnect();

}

?>


File: /routeros-api\examples\example3.php
<?php

/* Example for adding a VPN user */

require('../routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = true;

if ($API->connect('111.111.111.111', 'LOGIN', 'PASSWORD')) {

   $API->comm("/ppp/secret/add", array(
      "name"     => "user",
      "password" => "pass",
      "remote-address" => "172.16.1.10",
      "comment"  => "{new VPN user}",
      "service"  => "pptp",
   ));

   $API->disconnect();

}

?>

File: /routeros-api\examples\example4.php
<?php

/* Example of finding registration-table ID for specified MAC */

require('../routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = true;

if ($API->connect('111.111.111.111', 'LOGIN', 'PASSWORD')) {

   $ARRAY = $API->comm("/interface/wireless/registration-table/print", array(
      ".proplist"=> ".id",
      "?mac-address" => "00:0E:BB:DD:FF:FF",
   ));
	
   print_r($ARRAY);

   $API->disconnect();

}

?>

File: /routeros-api\examples\example5.php
<?php

/* Example of counting leases from a specific IP Pool (using regexp) */

require('../routeros_api.class.php');

$API = new RouterosAPI();

$API->debug = false;

if ($API->connect('192.168.172.1', 'test', 'ardPWhash')) {

   $ARRAY = $API->comm("/ip/dhcp-server/lease/print", array(
      "count-only"=> "",
      "~active-address" => "1.1.",
   ));
   
   print_r($ARRAY);

   $API->disconnect();

}

?>

File: /routeros-api\examples\example6.php
<?php

/* 3 step action 
   1) fetch all static dns hosts
   2) remove all static dns hosts
   3) add example host
*/

require('../routeros_api.class.php');
$API = new RouterosAPI();

if ($API->connect('111.111.111.111', 'LOGIN', 'PASSWORD')) {
   # Get all current hosts
   $API->write('/ip/dns/static/print');
   $ips = $API->read();

   # delete them all !
   foreach($ips as $num => $ip_data) {
     $API->write('/ip/dns/static/remove', false);
     $API->write("=.id=" . $ip_data[".id"], true);
   }

  #add some new
   $API->comm("/ip/dns/static/add", array(
      "name"     => "jefkeklak",
      "address"  => "1.2.3.4",
      "ttl"      => "1m"
   ));

   #show me what you got
   $API->write('/ip/dns/static/print');
   $ips = $API->read();
   var_dump($ips);
   $API->disconnect();
}


File: /routeros-api\README.md
# routeros-api
Client API for RouterOS/Mikrotik

This class was originally written by Denis Basta and updated by several contributors.  It aims to give a simple interface to the RouterOS API in PHP.

Mikrotik Wiki page at http://wiki.mikrotik.com/wiki/API_PHP_class

## Contributors (before moving to Git)
* Nick Barnes
* Ben Menking (ben [at] infotechsc [dot] com)
* Jeremy Jefferson (http://jeremyj.com)
* Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
* Mikhail Moskalev (mmv.rus [at] gmail [dot] com)

## Changelog

Please see git logs.  Version 1.0 through current version have been preserved in this Git repo.



File: /routeros-api\routeros_api.class.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 5;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    public function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $ip.':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login', false);
                $this->write('=name=' . $login, false);
                $this->write('=password=' . $password);
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0])) {
                    if ($RESPONSE[0] == '!done') {
                        if (!isset($RESPONSE[1])) {
                            // Login method post-v6.43
                            $this->connected = true;
                            break;
                        } else {
                            // Login method pre-v6.43
                            $MATCHES = array();
                            if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                                if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                                    $this->write('/login', false);
                                    $this->write('=name=' . $login, false);
                                    $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                                    $RESPONSE = $this->read(false);
                                    if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                        $this->connected = true;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


