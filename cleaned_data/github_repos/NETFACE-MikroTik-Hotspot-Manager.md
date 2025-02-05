# Repository Information
Name: NETFACE-MikroTik-Hotspot-Manager

# Directory Structure
Directory structure:
└── github_repos/NETFACE-MikroTik-Hotspot-Manager/
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
    │   │       ├── pack-40f4afa7646dcf9e0ca994d53868cf1a9af0f7aa.idx
    │   │       └── pack-40f4afa7646dcf9e0ca994d53868cf1a9af0f7aa.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── configure_hotspot.php
    ├── disabler.php
    ├── freerad/
    │   ├── default
    │   ├── inner-tunnel
    │   ├── radiusd.conf
    │   ├── sql
    │   └── sqlcounter
    ├── general_settings.php
    ├── hotspots.php
    ├── index.php
    ├── init/
    │   └── login.html
    ├── login.php
    ├── logout.php
    ├── make_vouchers.php
    ├── menu.php
    ├── README.md
    ├── remove_router.php
    ├── routeros_api.class.php
    ├── routers.php
    ├── script.js
    ├── scripts/
    │   ├── central_router_config.rsc
    │   └── hotspot_config.rsc
    ├── setup_one_hotspot.php
    ├── tutorial.php
    ├── upload_logo.php
    └── vouchers.php


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
	url = https://github.com/radman13666/NETFACE-MikroTik-Hotspot-Manager.git
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
0000000000000000000000000000000000000000 71bb9bc4368f0aef5c4f950ab5485177d4a9f502 vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/radman13666/NETFACE-MikroTik-Hotspot-Manager.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 71bb9bc4368f0aef5c4f950ab5485177d4a9f502 vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/radman13666/NETFACE-MikroTik-Hotspot-Manager.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 71bb9bc4368f0aef5c4f950ab5485177d4a9f502 vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/radman13666/NETFACE-MikroTik-Hotspot-Manager.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
71bb9bc4368f0aef5c4f950ab5485177d4a9f502 refs/remotes/origin/master


File: /.git\refs\heads\master
71bb9bc4368f0aef5c4f950ab5485177d4a9f502


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /configure_hotspot.php
<?php

require "routeros_api.class.php";

/*function checkUsers($num_users) {
  $final_num_users = 0;
  if ($num_users > 251) {
    $final_num_users = 251;
  } else if ($num_users < 10) {
    $final_num_users = 10;
  } else {
    $final_num_users = $num_users;
  }
  return $final_num_users;
}*/

function checkOctet($octet) {
  $final_octet = 0;
  if ($octet > 255) {
    $final_octet = 255;
  } else if ($octet < 0) {
    $final_octet = 0;
  } else {
    $final_octet = $octet;
  }
  return $final_octet;
}

function multiexplode ($delimiters, $string) { 
  $ready = str_replace($delimiters, $delimiters[0], $string);
  $launch = explode($delimiters[0], $ready);
  return  $launch;
}

function genPool($oct1, $oct2, $oct3, $oct4, $mask) {
  $oct = 3;
  $du = 24;
  $dl = 16;
  $first_host = "";
  $last_host = "";

  $pool = "";
  #find the octet we are working in
  if ($mask >= 16 and $mask <= 24) {
    $oct = 3; 
    $du = 24; 
    $dl = 16;
  } else if ($mask >= 24 and $mask < 32) {
    $oct = 4;
    $du = 32;
    $dl = 24;
  }
  #get the subnet increment
  $inc = 2 ** ($du - $mask);

  #get the number of hosts
  $hosts = (2 ** (32 - $mask)) - 2;

  #validate network address and get the pool range
  if ($oct == 3 and ($oct3 % $inc == 0)) {
    $serv = "$oct1.$oct2.$oct3.1";
    $first_host = "$oct1.$oct2.$oct3.2";
    $last_host = "$oct1.$oct2." . ($oct3 + ($inc - 1)) . ".254";
  } else if ($oct == 4 and ($oct4 % $inc == 0)) {
    $serv = "$oct1.$oct2.$oct3." . ($oct4 + 1);
    $first_host = "$oct1.$oct2.$oct3." . ($oct4 + 2);
    $last_host = "$oct1.$oct2.$oct3." . (($oct4 + $inc) - 2);
  } 
#  else {
#    echo "bad network\n";
#    exit;
#  }

  #output results
  return array("pool" => "$first_host-$last_host", "server" => $serv);
}

/*function reset_router($router_addr, $username, $password) {
	$API = new RoutersAPI();
	$API->debug = true;

	if ($API->connect($router_addr, $username, $password) {
		$API->write("/system/reset-configuration", false);
		#$API->write("=no-defaults=yes");
		$READ = $API->read(false);
	}
}*/

function setup($router_addr, $username, $password) { 
	$API = new RouterosAPI();
	$API->debug = true;
	$poolName = randomString() . randomString() . randomString();
	$dhcpName = randomString() . randomString() . randomString(); 
	$profName = randomString() . randomString() . randomString();
	
  $net = $_POST["hs_net"];
  $octs = multiexplode(array(".", "/"), $net);
  $mask = $octs[4];
  
  $pool_array = genPool($octs[0], $octs[1], $octs[2], $octs[3], $mask);
  $serv = $pool_array["server"];
  $pool = $pool_array["pool"];
  
  if ($API->connect($router_addr, $username, $password)) {

		$API->write("/interface/wireless/set", false);
		$API->write("=.id=*6", false);
		$API->write("=ssid=" . $_POST["hs_ssid"], false);
    $API->write("=mode=ap-bridge", false);
    $API->write("=wireless-protocol=802.11", false);
    $API->write("=disabled=no");
		$READ = $API->read(false);
/*
		$API->write("/interface/bridge/add", false);
    $API->write("=name=bridge-hotspot", false);
    $API->write("=arp=enabled", false);
    $API->write("protocol-mode=stp", false);
  	$API->write("=disabled=no");
		$READ = $API->read(false);

		$API->write("/interface/bridge/port/add", false);
		$API->write("=interface=wlan1", false);
		$API->write("=bridge=bridge-hotspot");
		$READ = $API->read(false);
*/
		$API->write("/ip/address/add", false);
		$API->write("=address=$serv/$mask", false);
		$API->write("=interface=wlan1");
		$READ = $API->read(false);

		$API->write("/ip/pool/add", false);
		$API->write("=name=" . $poolName, false);
		$API->write("=ranges=$pool");
		$READ = $API->read(false);
				
		$API->write("/ip/dhcp-server/add", false);
		$API->write("=name=" . $dhcpName, false);
		$API->write("=interface=wlan1", false);
		$API->write("=address-pool=" . $poolName, false);
		$API->write("=lease-time=3d", false);
		$API->write("=disabled=no");
		$READ = $API->read(false);

		$API->write("/ip/dhcp-server/network/add", false);
		$API->write("=address=$net", false);
		$API->write("=gateway=$serv");
		$READ = $API->read(false);

    $API->write("/routing/ospf/network/add", false);
    $API->write("=network=$net", false);
    $API->write("=area=backbone");
    $READ = $API->read(false);

		$API->write("/ip/hotspot/profile/add", false);
		$API->write("=name=" . $profName, false);
		$API->write("=dns-name=" . $_POST["hs_dns"], false);
		$API->write("=hotspot-address=$serv", false);
		$API->write("=use-radius=yes", false);
		$API->write("=radius-accounting=yes", false);
		$API->write("=login-by=http-pap");
		$READ = $API->read(false);
		
		$API->write("/ip/hotspot/add", false);
		$API->write("=profile=" . $profName, false);
		$API->write("=name=" . $_POST["hs_ssid"], false);
		$API->write("=address-pool=" . $poolName, false);
		$API->write("=interface=wlan1", false);
		$API->write("=addresses-per-mac=1", false);
		$API->write("=disabled=no");
		$READ = $API->read(false);

//		$API->write("/ip/firewall/nat/set", false);
//		$API->write("=.id=*1", false);
//		$API->write("=src-address=$net");
//		$READ = $API->read(false);

    $conn = new mysqli("localhost", "mgt", "admin_mgt", "manager_db");
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }
    $sql = "select * from radlogin where id = 1";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();

		$API->write("/radius/add", false);
		$API->write("=address=" . $row["radaddress"], false);
		$API->write("=secret=" . $row["radsecret"], false);
		$API->write("=service=hotspot", false);
		$API->write("=disabled=no");
		$READ = $API->read(false);

		$API->write("/radius/incoming/set", false);
		$API->write("=accept=yes");
		$READ = $API->read(false);

    $conn->close();
	}
}

function randomString() {
	$characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
	$randString = '';
	for ($i = 0; $i < 10; $i++) {
		$randString = $characters[rand(0, strlen($characters))];
	}
	return $randString;
}

function checkOctet_bool($octet) {
  $octet_ok = TRUE;
  if ($octet > 255 or $octet < 0) {
    $octet_ok = FALSE;
  } else {
    $octet = TRUE;
  }
  return $octet_ok;
}

?>



File: /disabler.php
<?php 
if (!isset($_SERVER['HTTP_REFERER'])){
    header('location:../login.php');
    exit;
}
?>




File: /freerad\default
######################################################################
#
#	As of 2.0.0, FreeRADIUS supports virtual hosts using the
#	"server" section, and configuration directives.
#
#	Virtual hosts should be put into the "sites-available"
#	directory.  Soft links should be created in the "sites-enabled"
#	directory to these files.  This is done in a normal installation.
#
#	If you are using 802.1X (EAP) authentication, please see also
#	the "inner-tunnel" virtual server.  You will likely have to edit
#	that, too, for authentication to work.
#
#	$Id: 083407596aa5074d665adac9606e7de655b634aa $
#
######################################################################
#
#	Read "man radiusd" before editing this file.  See the section
#	titled DEBUGGING.  It outlines a method where you can quickly
#	obtain the configuration you want, without running into
#	trouble.  See also "man unlang", which documents the format
#	of this file.
#
#	This configuration is designed to work in the widest possible
#	set of circumstances, with the widest possible number of
#	authentication methods.  This means that in general, you should
#	need to make very few changes to this file.
#
#	The best way to configure the server for your local system
#	is to CAREFULLY edit this file.  Most attempts to make large
#	edits to this file will BREAK THE SERVER.  Any edits should
#	be small, and tested by running the server with "radiusd -X".
#	Once the edits have been verified to work, save a copy of these
#	configuration files somewhere.  (e.g. as a "tar" file).  Then,
#	make more edits, and test, as above.
#
#	There are many "commented out" references to modules such
#	as ldap, sql, etc.  These references serve as place-holders.
#	If you need the functionality of that module, then configure
#	it in radiusd.conf, and un-comment the references to it in
#	this file.  In most cases, those small changes will result
#	in the server being able to connect to the DB, and to
#	authenticate users.
#
######################################################################

server default {
#
#  If you want the server to listen on additional addresses, or on
#  additional ports, you can use multiple "listen" sections.
#
#  Each section make the server listen for only one type of packet,
#  therefore authentication and accounting have to be configured in
#  different sections.
#
#  The server ignore all "listen" section if you are using '-i' and '-p'
#  on the command line.
#
listen {
	#  Type of packets to listen for.
	#  Allowed values are:
	#	auth	listen for authentication packets
	#	acct	listen for accounting packets
	#	proxy   IP to use for sending proxied packets
	#	detail  Read from the detail file.  For examples, see
	#               raddb/sites-available/copy-acct-to-home-server
	#	status  listen for Status-Server packets.  For examples,
	#		see raddb/sites-available/status
	#	coa     listen for CoA-Request and Disconnect-Request
	#		packets.  For examples, see the file
	#		raddb/sites-available/coa
	#
	type = auth

	#  Note: "type = proxy" lets you control the source IP used for
	#        proxying packets, with some limitations:
	#
	#    * A proxy listener CANNOT be used in a virtual server section.
	#    * You should probably set "port = 0".
	#    * Any "clients" configuration will be ignored.
	#
	#  See also proxy.conf, and the "src_ipaddr" configuration entry
	#  in the sample "home_server" section.  When you specify the
	#  source IP address for packets sent to a home server, the
	#  proxy listeners are automatically created.

	#  ipaddr/ipv4addr/ipv6addr - IP address on which to listen.
	#  Out of several options the first one will be used.
	#
	#  Allowed values are:
	#	IPv4 address (e.g. 1.2.3.4, for ipv4addr/ipaddr)
	#	IPv6 address (e.g. 2001:db8::1, for ipv6addr/ipaddr)
	#	hostname     (radius.example.com,
	#			A record for ipv4addr,
	#       		AAAA record for ipv6addr,
	#			A or AAAA record for ipaddr)
	#       wildcard     (*)
	#
	# ipv4addr = *
	# ipv6addr = *
	ipaddr = *

	#  Port on which to listen.
	#  Allowed values are:
	#	integer port number (1812)
	#	0 means "use /etc/services for the proper port"
	port = 0

	#  Some systems support binding to an interface, in addition
	#  to the IP address.  This feature isn't strictly necessary,
	#  but for sites with many IP addresses on one interface,
	#  it's useful to say "listen on all addresses for eth0".
	#
	#  If your system does not support this feature, you will
	#  get an error if you try to use it.
	#
#	interface = eth0

	#  Per-socket lists of clients.  This is a very useful feature.
	#
	#  The name here is a reference to a section elsewhere in
	#  radiusd.conf, or clients.conf.  Having the name as
	#  a reference allows multiple sockets to use the same
	#  set of clients.
	#
	#  If this configuration is used, then the global list of clients
	#  is IGNORED for this "listen" section.  Take care configuring
	#  this feature, to ensure you don't accidentally disable a
	#  client you need.
	#
	#  See clients.conf for the configuration of "per_socket_clients".
	#
#	clients = per_socket_clients

	#
	#  Connection limiting for sockets with "proto = tcp".
	#
	#  This section is ignored for other kinds of sockets.
	#
	limit {
	      #
	      #  Limit the number of simultaneous TCP connections to the socket
	      #
	      #  The default is 16.
	      #  Setting this to 0 means "no limit"
	      max_connections = 16

	      #  The per-socket "max_requests" option does not exist.

	      #
	      #  The lifetime, in seconds, of a TCP connection.  After
	      #  this lifetime, the connection will be closed.
	      #
	      #  Setting this to 0 means "forever".
	      lifetime = 0

	      #
	      #  The idle timeout, in seconds, of a TCP connection.
	      #  If no packets have been received over the connection for
	      #  this time, the connection will be closed.
	      #
	      #  Setting this to 0 means "no timeout".
	      #
	      #  We STRONGLY RECOMMEND that you set an idle timeout.
	      #
	      idle_timeout = 30
	}
}

#
#  This second "listen" section is for listening on the accounting
#  port, too.
#
listen {
	ipaddr = *
#	ipv6addr = ::
	port = 0
	type = acct
#	interface = eth0
#	clients = per_socket_clients

	limit {
		#  The number of packets received can be rate limited via the
		#  "max_pps" configuration item.  When it is set, the server
		#  tracks the total number of packets received in the previous
		#  second.  If the count is greater than "max_pps", then the
		#  new packet is silently discarded.  This helps the server
		#  deal with overload situations.
		#
		#  The packets/s counter is tracked in a sliding window.  This
		#  means that the pps calculation is done for the second
		#  before the current packet was received.  NOT for the current
		#  wall-clock second, and NOT for the previous wall-clock second.
		#
		#  Useful values are 0 (no limit), or 100 to 10000.
		#  Values lower than 100 will likely cause the server to ignore
		#  normal traffic.  Few systems are capable of handling more than
		#  10K packets/s.
		#
		#  It is most useful for accounting systems.  Set it to 50%
		#  more than the normal accounting load, and you can be sure that
		#  the server will never get overloaded
		#
#		max_pps = 0

		# Only for "proto = tcp". These are ignored for "udp" sockets.
		#
#		idle_timeout = 0
#		lifetime = 0
#		max_connections = 0
	}
}

# IPv6 versions of the above - read their full config to understand options
listen {
	type = auth
	ipv6addr = ::	# any.  ::1 == localhost
	port = 0
#	interface = eth0
#	clients = per_socket_clients
	limit {
	      max_connections = 16
	      lifetime = 0
	      idle_timeout = 30
	}
}

listen {
	ipv6addr = ::
	port = 0
	type = acct
#	interface = eth0
#	clients = per_socket_clients

	limit {
#		max_pps = 0
#		idle_timeout = 0
#		lifetime = 0
#		max_connections = 0
	}
}

#  Authorization. First preprocess (hints and huntgroups files),
#  then realms, and finally look in the "users" file.
#
#  Any changes made here should also be made to the "inner-tunnel"
#  virtual server.
#
#  The order of the realm modules will determine the order that
#  we try to find a matching realm.
#
#  Make *sure* that 'preprocess' comes before any realm if you
#  need to setup hints for the remote radius server
authorize {
	#
	#  Take a User-Name, and perform some checks on it, for spaces and other
	#  invalid characters.  If the User-Name appears invalid, reject the
	#  request.
	#
	#  See policy.d/filter for the definition of the filter_username policy.
	#
	filter_username

	#
	#  Some broken equipment sends passwords with embedded zeros.
	#  i.e. the debug output will show
	#
	#	User-Password = "password\000\000"
	#
	#  This policy will fix it to just be "password".
	#
#	filter_password

	#
	#  The preprocess module takes care of sanitizing some bizarre
	#  attributes in the request, and turning them into attributes
	#  which are more standard.
	#
	#  It takes care of processing the 'raddb/mods-config/preprocess/hints' 
	#  and the 'raddb/mods-config/preprocess/huntgroups' files.
	preprocess

	#  If you intend to use CUI and you require that the Operator-Name
	#  be set for CUI generation and you want to generate CUI also
	#  for your local clients then uncomment the operator-name
	#  below and set the operator-name for your clients in clients.conf
#	operator-name

	#
	#  If you want to generate CUI for some clients that do not
	#  send proper CUI requests, then uncomment the
	#  cui below and set "add_cui = yes" for these clients in clients.conf
#	cui

	#
	#  If you want to have a log of authentication requests,
	#  un-comment the following line.
#	auth_log

	#
	#  The chap module will set 'Auth-Type := CHAP' if we are
	#  handling a CHAP request and Auth-Type has not already been set
#	chap

	#
	#  If the users are logging in with an MS-CHAP-Challenge
	#  attribute for authentication, the mschap module will find
	#  the MS-CHAP-Challenge attribute, and add 'Auth-Type := MS-CHAP'
	#  to the request, which will cause the server to then use
	#  the mschap module for authentication.
#	mschap

	#
	#  If you have a Cisco SIP server authenticating against
	#  FreeRADIUS, uncomment the following line, and the 'digest'
	#  line in the 'authenticate' section.
	digest

	#
	#  The WiMAX specification says that the Calling-Station-Id
	#  is 6 octets of the MAC.  This definition conflicts with
	#  RFC 3580, and all common RADIUS practices.  Un-commenting
	#  the "wimax" module here means that it will fix the
	#  Calling-Station-Id attribute to the normal format as
	#  specified in RFC 3580 Section 3.21
#	wimax

	#
	#  Look for IPASS style 'realm/', and if not found, look for
	#  '@realm', and decide whether or not to proxy, based on
	#  that.
#	IPASS

	#
	#  If you are using multiple kinds of realms, you probably
	#  want to set "ignore_null = yes" for all of them.
	#  Otherwise, when the first style of realm doesn't match,
	#  the other styles won't be checked.
	#
	suffix
#	ntdomain

	#
	#  This module takes care of EAP-MD5, EAP-TLS, and EAP-LEAP
	#  authentication.
	#
	#  It also sets the EAP-Type attribute in the request
	#  attribute list to the EAP type from the packet.
	#
	#  The EAP module returns "ok" if it is not yet ready to
	#  authenticate the user.  The configuration below checks for
	#  that code, and stops processing the "authorize" section if
	#  so.
	#
	#  Any LDAP and/or SQL servers will not be queried for the
	#  initial set of packets that go back and forth to set up
	#  TTLS or PEAP.
	#
	eap {
		ok = return
	}

	#
	#  Pull crypt'd passwords from /etc/passwd or /etc/shadow,
	#  using the system API's to get the password.  If you want
	#  to read /etc/passwd or /etc/shadow directly, see the
	#  mods-available/passwd module.
	#
#	unix

	#
	#  Read the 'users' file.  In v3, this is located in
	#  raddb/mods-config/files/authorize
	files

	#
	#  Look in an SQL database.  The schema of the database
	#  is meant to mirror the "users" file.
	#
	#  See "Authorization Queries" in mods-available/sql
	-sql

	#
	#  If you are using /etc/smbpasswd, and are also doing
	#  mschap authentication, the un-comment this line, and
	#  configure the 'smbpasswd' module.
#	smbpasswd

	#
	#  The ldap module reads passwords from the LDAP database.
	-ldap

	#
	#  Enforce daily limits on time spent logged in.
#	daily

	#
	expiration
	logintime

	#
	#  If no other module has claimed responsibility for
	#  authentication, then try to use PAP.  This allows the
	#  other modules listed above to add a "known good" password
	#  to the request, and to do nothing else.  The PAP module
	#  will then see that password, and use it to do PAP
	#  authentication.
	#
	#  This module should be listed last, so that the other modules
	#  get a chance to set Auth-Type for themselves.
	#
	pap

	#
	#  If "status_server = yes", then Status-Server messages are passed
	#  through the following section, and ONLY the following section.
	#  This permits you to do DB queries, for example.  If the modules
	#  listed here return "fail", then NO response is sent.
	#
#	Autz-Type Status-Server {
#
#	}
#---------------->>> the counter for voucher expiry
  noresetcounter
}


#  Authentication.
#
#
#  This section lists which modules are available for authentication.
#  Note that it does NOT mean 'try each module in order'.  It means
#  that a module from the 'authorize' section adds a configuration
#  attribute 'Auth-Type := FOO'.  That authentication type is then
#  used to pick the appropriate module from the list below.
#

#  In general, you SHOULD NOT set the Auth-Type attribute.  The server
#  will figure it out on its own, and will do the right thing.  The
#  most common side effect of erroneously setting the Auth-Type
#  attribute is that one authentication method will work, but the
#  others will not.
#
#  The common reasons to set the Auth-Type attribute by hand
#  is to either forcibly reject the user (Auth-Type := Reject),
#  or to or forcibly accept the user (Auth-Type := Accept).
#
#  Note that Auth-Type := Accept will NOT work with EAP.
#
#  Please do not put "unlang" configurations into the "authenticate"
#  section.  Put them in the "post-auth" section instead.  That's what
#  the post-auth section is for.
#
authenticate {
	#
	#  PAP authentication, when a back-end database listed
	#  in the 'authorize' section supplies a password.  The
	#  password can be clear-text, or encrypted.
	Auth-Type PAP {
		pap
	}

	#
	#  Most people want CHAP authentication
	#  A back-end database listed in the 'authorize' section
	#  MUST supply a CLEAR TEXT password.  Encrypted passwords
	#  won't work.
	Auth-Type CHAP {
		chap
	}

	#
	#  MSCHAP authentication.
	Auth-Type MS-CHAP {
		mschap
	}

	#
	#  For old names, too.
	#
	mschap

	#
	#  If you have a Cisco SIP server authenticating against
	#  FreeRADIUS, uncomment the following line, and the 'digest'
	#  line in the 'authorize' section.
	digest

	#
	#  Pluggable Authentication Modules.
#	pam

	#  Uncomment it if you want to use ldap for authentication
	#
	#  Note that this means "check plain-text password against
	#  the ldap database", which means that EAP won't work,
	#  as it does not supply a plain-text password.
	#
	#  We do NOT recommend using this.  LDAP servers are databases.
	#  They are NOT authentication servers.  FreeRADIUS is an
	#  authentication server, and knows what to do with authentication.
	#  LDAP servers do not.
	#
#	Auth-Type LDAP {
#		ldap
#	}

	#
	#  Allow EAP authentication.
	eap

	#
	#  The older configurations sent a number of attributes in
	#  Access-Challenge packets, which wasn't strictly correct.
	#  If you want to filter out these attributes, uncomment
	#  the following lines.
	#
#	Auth-Type eap {
#		eap {
#			handled = 1
#		}
#		if (handled && (Response-Packet-Type == Access-Challenge)) {
#			attr_filter.access_challenge.post-auth
#			handled  # override the "updated" code from attr_filter
#		}
#	}
}


#
#  Pre-accounting.  Decide which accounting type to use.
#
preacct {
	preprocess

	#
	#  Merge Acct-[Input|Output]-Gigawords and Acct-[Input-Output]-Octets
	#  into a single 64bit counter Acct-[Input|Output]-Octets64.
	#
#	acct_counters64

	#
	#  Session start times are *implied* in RADIUS.
	#  The NAS never sends a "start time".  Instead, it sends
	#  a start packet, *possibly* with an Acct-Delay-Time.
	#  The server is supposed to conclude that the start time
	#  was "Acct-Delay-Time" seconds in the past.
	#
	#  The code below creates an explicit start time, which can
	#  then be used in other modules.  It will be *mostly* correct.
	#  Any errors are due to the 1-second resolution of RADIUS,
	#  and the possibility that the time on the NAS may be off.
	#
	#  The start time is: NOW - delay - session_length
	#

#	update request {
#	  	FreeRADIUS-Acct-Session-Start-Time = "%{expr: %l - %{%{Acct-Session-Time}:-0} - %{%{Acct-Delay-Time}:-0}}"
#	}


	#
	#  Ensure that we have a semi-unique identifier for every
	#  request, and many NAS boxes are broken.
	acct_unique

	#
	#  Look for IPASS-style 'realm/', and if not found, look for
	#  '@realm', and decide whether or not to proxy, based on
	#  that.
	#
	#  Accounting requests are generally proxied to the same
	#  home server as authentication requests.
#	IPASS
	suffix
#	ntdomain

	#
	#  Read the 'acct_users' file
	files
}

#
#  Accounting.  Log the accounting data.
#
accounting {
	#  Update accounting packet by adding the CUI attribute
	#  recorded from the corresponding Access-Accept
	#  use it only if your NAS boxes do not support CUI themselves
#	cui
	#
	#  Create a 'detail'ed log of the packets.
	#  Note that accounting requests which are proxied
	#  are also logged in the detail file.
	detail
#	daily

	#  Update the wtmp file
	#
	#  If you don't use "radlast", you can delete this line.
	unix

	#
	#  For Simultaneous-Use tracking.
	#
	#  Due to packet losses in the network, the data here
	#  may be incorrect.  There is little we can do about it.
#	radutmp
#	sradutmp

	#  Return an address to the IP Pool when we see a stop record.
#	main_pool

	#
	#  Log traffic to an SQL database.
	#
	#  See "Accounting queries" in mods-available/sql
	-sql

	#
	#  If you receive stop packets with zero session length,
	#  they will NOT be logged in the database.  The SQL module
	#  will print a message (only in debugging mode), and will
	#  return "noop".
	#
	#  You can ignore these packets by uncommenting the following
	#  three lines.  Otherwise, the server will not respond to the
	#  accounting request, and the NAS will retransmit.
	#
#	if (noop) {
#		ok
#	}

	#
	#  Instead of sending the query to the SQL server,
	#  write it into a log file.
	#
#	sql_log

	#  Cisco VoIP specific bulk accounting
#	pgsql-voip

	# For Exec-Program and Exec-Program-Wait
	exec

	#  Filter attributes from the accounting response.
	attr_filter.accounting_response

	#
	#  See "Autz-Type Status-Server" for how this works.
	#
#	Acct-Type Status-Server {
#
#	}
}


#  Session database, used for checking Simultaneous-Use. Either the radutmp
#  or rlm_sql module can handle this.
#  The rlm_sql module is *much* faster
session {
#	radutmp

	#
	#  See "Simultaneous Use Checking Queries" in mods-available/sql
#	sql
}


#  Post-Authentication
#  Once we KNOW that the user has been authenticated, there are
#  additional steps we can take.
post-auth {
	#
	#  If you need to have a State attribute, you can
	#  add it here.  e.g. for later CoA-Request with
	#  State, and Service-Type = Authorize-Only.
	#
#	if (!&reply:State) {
#		update reply {
#			State := "0x%{randstr:16h}"
#		}
#	}

	#
	#  For EAP-TTLS and PEAP, add the cached attributes to the reply.
	#  The "session-state" attributes are automatically cached when
	#  an Access-Challenge is sent, and automatically retrieved
	#  when an Access-Request is received.
	#
	#  The session-state attributes are automatically deleted after
	#  an Access-Reject or Access-Accept is sent.
	#
	update {
		&reply: += &session-state:
	}

	#  Get an address from the IP Pool.
#	main_pool


	#  Create the CUI value and add the attribute to Access-Accept.
	#  Uncomment the line below if *returning* the CUI.
#	cui

	#
	#  If you want to have a log of authentication replies,
	#  un-comment the following line, and enable the
	#  'detail reply_log' module.
#	reply_log

	#
	#  After authenticating the user, do another SQL query.
	#
	#  See "Authentication Logging Queries" in mods-available/sql
	-sql

	#
	#  Instead of sending the query to the SQL server,
	#  write it into a log file.
	#
#	sql_log

	#
	#  Un-comment the following if you want to modify the user's object
	#  in LDAP after a successful login.
	#
#	ldap

	# For Exec-Program and Exec-Program-Wait
	exec

	#
	#  Calculate the various WiMAX keys.  In order for this to work,
	#  you will need to define the WiMAX NAI, usually via
	#
	#	update request {
	#	       WiMAX-MN-NAI = "%{User-Name}"
	#	}
	#
	#  If you want various keys to be calculated, you will need to
	#  update the reply with "template" values.  The module will see
	#  this, and replace the template values with the correct ones
	#  taken from the cryptographic calculations.  e.g.
	#
	# 	update reply {
	#		WiMAX-FA-RK-Key = 0x00
	#		WiMAX-MSK = "%{EAP-MSK}"
	#	}
	#
	#  You may want to delete the MS-MPPE-*-Keys from the reply,
	#  as some WiMAX clients behave badly when those attributes
	#  are included.  See "raddb/modules/wimax", configuration
	#  entry "delete_mppe_keys" for more information.
	#
#	wimax


	#  If there is a client certificate (EAP-TLS, sometimes PEAP
	#  and TTLS), then some attributes are filled out after the
	#  certificate verification has been performed.  These fields
	#  MAY be available during the authentication, or they may be
	#  available only in the "post-auth" section.
	#
	#  The first set of attributes contains information about the
	#  issuing certificate which is being used.  The second
	#  contains information about the client certificate (if
	#  available).
#
#	update reply {
#	       Reply-Message += "%{TLS-Cert-Serial}"
#	       Reply-Message += "%{TLS-Cert-Expiration}"
#	       Reply-Message += "%{TLS-Cert-Subject}"
#	       Reply-Message += "%{TLS-Cert-Issuer}"
#	       Reply-Message += "%{TLS-Cert-Common-Name}"
#	       Reply-Message += "%{TLS-Cert-Subject-Alt-Name-Email}"
#
#	       Reply-Message += "%{TLS-Client-Cert-Serial}"
#	       Reply-Message += "%{TLS-Client-Cert-Expiration}"
#	       Reply-Message += "%{TLS-Client-Cert-Subject}"
#	       Reply-Message += "%{TLS-Client-Cert-Issuer}"
#	       Reply-Message += "%{TLS-Client-Cert-Common-Name}"
#	       Reply-Message += "%{TLS-Client-Cert-Subject-Alt-Name-Email}"
#	}

	#  Insert class attribute (with unique value) into response,
	#  aids matching auth and acct records, and protects against duplicate
	#  Acct-Session-Id. Note: Only works if the NAS has implemented
	#  RFC 2865 behaviour for the class attribute, AND if the NAS
	#  supports long Class attributes.  Many older or cheap NASes
	#  only support 16-octet Class attributes.
#	insert_acct_class

	#  MacSEC requires the use of EAP-Key-Name.  However, we don't
	#  want to send it for all EAP sessions.  Therefore, the EAP
	#  modules put required data into the EAP-Session-Id attribute.
	#  This attribute is never put into a request or reply packet.
	#
	#  Uncomment the next few lines to copy the required data into
	#  the EAP-Key-Name attribute
#	if (&reply:EAP-Session-Id) {
#		update reply {
#			EAP-Key-Name := &reply:EAP-Session-Id
#		}
#	}

	#  Remove reply message if the response contains an EAP-Message
	remove_reply_message_if_eap

	#
	#  Access-Reject packets are sent through the REJECT sub-section of the
	#  post-auth section.
	#
	#  Add the ldap module name (or instance) if you have set
	#  'edir_account_policy_check = yes' in the ldap module configuration
	#
	#  The "session-state" attributes are not available here.
	#
	Post-Auth-Type REJECT {
		# log failed authentications in SQL, too.
		-sql
		attr_filter.access_reject

		# Insert EAP-Failure message if the request was
		# rejected by policy instead of because of an
		# authentication failure
		eap

		#  Remove reply message if the response contains an EAP-Message
		remove_reply_message_if_eap
	}
}

#
#  When the server decides to proxy a request to a home server,
#  the proxied request is first passed through the pre-proxy
#  stage.  This stage can re-write the request, or decide to
#  cancel the proxy.
#
#  Only a few modules currently have this method.
#
pre-proxy {
	# Before proxing the request add an Operator-Name attribute identifying
	# if the operator-name is found for this client.
	# No need to uncomment this if you have already enabled this in
	# the authorize section.
#	operator-name

	#  The client requests the CUI by sending a CUI attribute
	#  containing one zero byte.
	#  Uncomment the line below if *requesting* the CUI.
#	cui

	#  Uncomment the following line if you want to change attributes
	#  as defined in the preproxy_users file.
#	files

	#  Uncomment the following line if you want to filter requests
	#  sent to remote servers based on the rules defined in the
	#  'attrs.pre-proxy' file.
#	attr_filter.pre-proxy

	#  If you want to have a log of packets proxied to a home
	#  server, un-comment the following line, and the
	#  'detail pre_proxy_log' section, above.
#	pre_proxy_log
}

#
#  When the server receives a reply to a request it proxied
#  to a home server, the request may be massaged here, in the
#  post-proxy stage.
#
post-proxy {

	#  If you want to have a log of replies from a home server,
	#  un-comment the following line, and the 'detail post_proxy_log'
	#  section, above.
#	post_proxy_log

	#  Uncomment the following line if you want to filter replies from
	#  remote proxies based on the rules defined in the 'attrs' file.
#	attr_filter.post-proxy

	#
	#  If you are proxying LEAP, you MUST configure the EAP
	#  module, and you MUST list it here, in the post-proxy
	#  stage.
	#
	#  You MUST also use the 'nostrip' option in the 'realm'
	#  configuration.  Otherwise, the User-Name attribute
	#  in the proxied request will not match the user name
	#  hidden inside of the EAP packet, and the end server will
	#  reject the EAP request.
	#
	eap

	#
	#  If the server tries to proxy a request and fails, then the
	#  request is processed through the modules in this section.
	#
	#  The main use of this section is to permit robust proxying
	#  of accounting packets.  The server can be configured to
	#  proxy accounting packets as part of normal processing.
	#  Then, if the home server goes down, accounting packets can
	#  be logged to a local "detail" file, for processing with
	#  radrelay.  When the home server comes back up, radrelay
	#  will read the detail file, and send the packets to the
	#  home server.
	#
	#  With this configuration, the server always responds to
	#  Accounting-Requests from the NAS, but only writes
	#  accounting packets to disk if the home server is down.
	#
#	Post-Proxy-Type Fail-Accounting {
#			detail
#	}
}
}


File: /freerad\inner-tunnel
# -*- text -*-
######################################################################
#
#	This is a virtual server that handles *only* inner tunnel
#	requests for EAP-TTLS and PEAP types.
#
#	$Id: 2c6f9611bfc7b4b782aeb9764e47e832690739c4 $
#
######################################################################

server inner-tunnel {

#
#  This next section is here to allow testing of the "inner-tunnel"
#  authentication methods, independently from the "default" server.
#  It is listening on "localhost", so that it can only be used from
#  the same machine.
#
#	$ radtest USER PASSWORD 127.0.0.1:18120 0 testing123
#
#  If it works, you have configured the inner tunnel correctly.  To check
#  if PEAP will work, use:
#
#	$ radtest -t mschap USER PASSWORD 127.0.0.1:18120 0 testing123
#
#  If that works, PEAP should work.  If that command doesn't work, then
#
#	FIX THE INNER TUNNEL CONFIGURATION SO THAT IT WORKS.
#
#  Do NOT do any PEAP tests.  It won't help.  Instead, concentrate
#  on fixing the inner tunnel configuration.  DO NOTHING ELSE.
#
listen {
       ipaddr = 127.0.0.1
       port = 18120
       type = auth
}


#  Authorization. First preprocess (hints and huntgroups files),
#  then realms, and finally look in the "users" file.
#
#  The order of the realm modules will determine the order that
#  we try to find a matching realm.
#
#  Make *sure* that 'preprocess' comes before any realm if you
#  need to setup hints for the remote radius server
authorize {
	#
	#  Take a User-Name, and perform some checks on it, for spaces and other
	#  invalid characters.  If the User-Name appears invalid, reject the
	#  request.
	#
	#  See policy.d/filter for the definition of the filter_username policy.
	#
	filter_username

	#
	#  Do checks on outer / inner User-Name, so that users
	#  can't spoof us by using incompatible identities
	#
#	filter_inner_identity

	#
	#  The chap module will set 'Auth-Type := CHAP' if we are
	#  handling a CHAP request and Auth-Type has not already been set
#	chap

	#
	#  If the users are logging in with an MS-CHAP-Challenge
	#  attribute for authentication, the mschap module will find
	#  the MS-CHAP-Challenge attribute, and add 'Auth-Type := MS-CHAP'
	#  to the request, which will cause the server to then use
	#  the mschap module for authentication.
#	mschap

	#
	#  Pull crypt'd passwords from /etc/passwd or /etc/shadow,
	#  using the system API's to get the password.  If you want
	#  to read /etc/passwd or /etc/shadow directly, see the
	#  passwd module, above.
	#
#	unix

	#
	#  Look for IPASS style 'realm/', and if not found, look for
	#  '@realm', and decide whether or not to proxy, based on
	#  that.
#	IPASS

	#
	#  If you are using multiple kinds of realms, you probably
	#  want to set "ignore_null = yes" for all of them.
	#  Otherwise, when the first style of realm doesn't match,
	#  the other styles won't be checked.
	#
	#  Note that proxying the inner tunnel authentication means
	#  that the user MAY use one identity in the outer session
	#  (e.g. "anonymous", and a different one here
	#  (e.g. "user@example.com").  The inner session will then be
	#  proxied elsewhere for authentication.  If you are not
	#  careful, this means that the user can cause you to forward
	#  the authentication to another RADIUS server, and have the
	#  accounting logs *not* sent to the other server.  This makes
	#  it difficult to bill people for their network activity.
	#
	suffix
#	ntdomain

	#
	#  The "suffix" module takes care of stripping the domain
	#  (e.g. "@example.com") from the User-Name attribute, and the
	#  next few lines ensure that the request is not proxied.
	#
	#  If you want the inner tunnel request to be proxied, delete
	#  the next few lines.
	#
	update control {
		&Proxy-To-Realm := LOCAL
	}

	#
	#  This module takes care of EAP-MSCHAPv2 authentication.
	#
	#  It also sets the EAP-Type attribute in the request
	#  attribute list to the EAP type from the packet.
	#
	#  The example below uses module failover to avoid querying all
	#  of the following modules if the EAP module returns "ok".
	#  Therefore, your LDAP and/or SQL servers will not be queried
	#  for the many packets that go back and forth to set up TTLS
	#  or PEAP.  The load on those servers will therefore be reduced.
	#
	eap {
		ok = return
	}

	#
	#  Read the 'users' file
	files

	#
	#  Look in an SQL database.  The schema of the database
	#  is meant to mirror the "users" file.
	#
	#  See "Authorization Queries" in sql.conf
	-sql

	#
	#  If you are using /etc/smbpasswd, and are also doing
	#  mschap authentication, the un-comment this line, and
	#  enable the "smbpasswd" module.
#	smbpasswd

	#
	#  The ldap module reads passwords from the LDAP database.
	-ldap

	#
	#  Enforce daily limits on time spent logged in.
#	daily

	expiration
	logintime

	#
	#  If no other module has claimed responsibility for
	#  authentication, then try to use PAP.  This allows the
	#  other modules listed above to add a "known good" password
	#  to the request, and to do nothing else.  The PAP module
	#  will then see that password, and use it to do PAP
	#  authentication.
	#
	#  This module should be listed last, so that the other modules
	#  get a chance to set Auth-Type for themselves.
	#
	pap
  #-------------------->>> the counter for voucher expiry
  noresetcounter
}


#  Authentication.
#
#
#  This section lists which modules are available for authentication.
#  Note that it does NOT mean 'try each module in order'.  It means
#  that a module from the 'authorize' section adds a configuration
#  attribute 'Auth-Type := FOO'.  That authentication type is then
#  used to pick the appropriate module from the list below.
#

#  In general, you SHOULD NOT set the Auth-Type attribute.  The server
#  will figure it out on its own, and will do the right thing.  The
#  most common side effect of erroneously setting the Auth-Type
#  attribute is that one authentication method will work, but the
#  others will not.
#
#  The common reasons to set the Auth-Type attribute by hand
#  is to either forcibly reject the user, or forcibly accept him.
#
authenticate {
	#
	#  PAP authentication, when a back-end database listed
	#  in the 'authorize' section supplies a password.  The
	#  password can be clear-text, or encrypted.
	Auth-Type PAP {
		pap
	}

	#
	#  Most people want CHAP authentication
	#  A back-end database listed in the 'authorize' section
	#  MUST supply a CLEAR TEXT password.  Encrypted passwords
	#  won't work.
	Auth-Type CHAP {
		chap
	}

	#
	#  MSCHAP authentication.
	Auth-Type MS-CHAP {
		mschap
	}

	#
	#  For old names, too.
	#
	mschap

	#
	#  Pluggable Authentication Modules.
#	pam

	# Uncomment it if you want to use ldap for authentication
	#
	# Note that this means "check plain-text password against
	# the ldap database", which means that EAP won't work,
	# as it does not supply a plain-text password.
	#
	#  We do NOT recommend using this.  LDAP servers are databases.
	#  They are NOT authentication servers.  FreeRADIUS is an
	#  authentication server, and knows what to do with authentication.
	#  LDAP servers do not.
	#
#	Auth-Type LDAP {
#		ldap
#	}

	#
	#  Allow EAP authentication.
	eap
}

######################################################################
#
#	There are no accounting requests inside of EAP-TTLS or PEAP
#	tunnels.
#
######################################################################


#  Session database, used for checking Simultaneous-Use. Either the radutmp
#  or rlm_sql module can handle this.
#  The rlm_sql module is *much* faster
session {
	radutmp

	#
	#  See "Simultaneous Use Checking Queries" in sql.conf
#	sql
}


#  Post-Authentication
#  Once we KNOW that the user has been authenticated, there are
#  additional steps we can take.
#
#  Note that the last packet of the inner-tunnel authentication
#  MAY NOT BE the last packet of the outer session.  So updating
#  the outer reply MIGHT work, and sometimes MIGHT NOT.  The
#  exact functionality depends on both the inner and outer
#  authentication methods.
#
#  If you need to send a reply attribute in the outer session,
#  the ONLY safe way is to set "use_tunneled_reply = yes", and
#  then update the inner-tunnel reply.
post-auth {
	#  If you want privacy to remain, see the
	#  Chargeable-User-Identity attribute from RFC 4372.
	#  If you want to use it just uncomment the line below.
#       cui-inner

	#
	#  If you want to have a log of authentication replies,
	#  un-comment the following line, and enable the
	#  'detail reply_log' module.
#	reply_log

	#
	#  After authenticating the user, do another SQL query.
	#
	#  See "Authentication Logging Queries" in sql.conf
	-sql

	#
	#  Instead of sending the query to the SQL server,
	#  write it into a log file.
	#
#	sql_log

	#
	#  Un-comment the following if you have set
	#  'edir_account_policy_check = yes' in the ldap module sub-section of
	#  the 'modules' section.
	#
#	ldap


	#
	#  Un-comment the following if you want to generate Moonshot (ABFAB) TargetedIds
	#  IMPORTANT: This requires the UUID package to be installed!
	#
#	moonshot_host_tid
#	moonshot_realm_tid
#	moonshot_coi_tid

	#
	#  Instead of "use_tunneled_reply", uncomment the
	#  next two "update" blocks.
	#
#	update {
#		&outer.session-state: += &reply:
#	}

	#
	#  These attributes are for the inner session only.
	#  They MUST NOT be sent in the outer reply.
	#
	#  If you uncomment the previous block and leave
	#  this one commented out, WiFi WILL NOT WORK,
	#  because the client will get two MS-MPPE-keys
	#
#	update outer.session-state {
#		MS-MPPE-Encryption-Policy !* ANY
#		MS-MPPE-Encryption-Types !* ANY
#		MS-MPPE-Send-Key !* ANY
#		MS-MPPE-Recv-Key !* ANY
#		Message-Authenticator !* ANY
#		EAP-Message !* ANY
#		Proxy-State !* ANY
#	}

	#
	#  Access-Reject packets are sent through the REJECT sub-section of the
	#  post-auth section.
	#
	#  Add the ldap module name (or instance) if you have set
	#  'edir_account_policy_check = yes' in the ldap module configuration
	#
	Post-Auth-Type REJECT {
		# log failed authentications in SQL, too.
		-sql
		attr_filter.access_reject

		#
		#  Let the outer session know which module failed, and why.
		#
		update outer.session-state {
			&Module-Failure-Message := &request:Module-Failure-Message
		}
	}
}

#
#  When the server decides to proxy a request to a home server,
#  the proxied request is first passed through the pre-proxy
#  stage.  This stage can re-write the request, or decide to
#  cancel the proxy.
#
#  Only a few modules currently have this method.
#
pre-proxy {
	#  Uncomment the following line if you want to change attributes
	#  as defined in the preproxy_users file.
#	files

	#  Uncomment the following line if you want to filter requests
	#  sent to remote servers based on the rules defined in the
	#  'attrs.pre-proxy' file.
#	attr_filter.pre-proxy

	#  If you want to have a log of packets proxied to a home
	#  server, un-comment the following line, and the
	#  'detail pre_proxy_log' section, above.
#	pre_proxy_log
}

#
#  When the server receives a reply to a request it proxied
#  to a home server, the request may be massaged here, in the
#  post-proxy stage.
#
post-proxy {

	#  If you want to have a log of replies from a home server,
	#  un-comment the following line, and the 'detail post_proxy_log'
	#  section, above.
#	post_proxy_log

	#  Uncomment the following line if you want to filter replies from
	#  remote proxies based on the rules defined in the 'attrs' file.
#	attr_filter.post-proxy

	#
	#  If you are proxying LEAP, you MUST configure the EAP
	#  module, and you MUST list it here, in the post-proxy
	#  stage.
	#
	#  You MUST also use the 'nostrip' option in the 'realm'
	#  configuration.  Otherwise, the User-Name attribute
	#  in the proxied request will not match the user name
	#  hidden inside of the EAP packet, and the end server will
	#  reject the EAP request.
	#
	eap
}

} # inner-tunnel server block


File: /freerad\radiusd.conf
# -*- text -*-
##
## radiusd.conf	-- FreeRADIUS server configuration file - 3.0.12
##
##	http://www.freeradius.org/
##	$Id: c62f4ffed53a073a885f243b728129f5c482fad7 $
##

######################################################################
#
#	Read "man radiusd" before editing this file.  See the section
#	titled DEBUGGING.  It outlines a method where you can quickly
#	obtain the configuration you want, without running into
#	trouble.
#
#	Run the server in debugging mode, and READ the output.
#
#		$ radiusd -X
#
#	We cannot emphasize this point strongly enough.  The vast
#	majority of problems can be solved by carefully reading the
#	debugging output, which includes warnings about common issues,
#	and suggestions for how they may be fixed.
#
#	There may be a lot of output, but look carefully for words like:
#	"warning", "error", "reject", or "failure".  The messages there
#	will usually be enough to guide you to a solution.
#
#	If you are going to ask a question on the mailing list, then
#	explain what you are trying to do, and include the output from
#	debugging mode (radiusd -X).  Failure to do so means that all
#	of the responses to your question will be people telling you
#	to "post the output of radiusd -X".

######################################################################
#
#  	The location of other config files and logfiles are declared
#  	in this file.
#
#  	Also general configuration for modules can be done in this
#  	file, it is exported through the API to modules that ask for
#  	it.
#
#	See "man radiusd.conf" for documentation on the format of this
#	file.  Note that the individual configuration items are NOT
#	documented in that "man" page.  They are only documented here,
#	in the comments.
#
#	The "unlang" policy language can be used to create complex
#	if / else policies.  See "man unlang" for details.
#

prefix = /usr
exec_prefix = /usr
sysconfdir = /etc
localstatedir = /var
sbindir = ${exec_prefix}/sbin
logdir = /var/log/freeradius
raddbdir = /etc/freeradius/3.0
radacctdir = ${logdir}/radacct

#
#  name of the running server.  See also the "-n" command-line option.
name = freeradius

#  Location of config and logfiles.
confdir = ${raddbdir}
modconfdir = ${confdir}/mods-config
certdir = ${confdir}/certs
cadir   = ${confdir}/certs
run_dir = ${localstatedir}/run/${name}

# Should likely be ${localstatedir}/lib/radiusd
db_dir = ${raddbdir}

#
# libdir: Where to find the rlm_* modules.
#
#   This should be automatically set at configuration time.
#
#   If the server builds and installs, but fails at execution time
#   with an 'undefined symbol' error, then you can use the libdir
#   directive to work around the problem.
#
#   The cause is usually that a library has been installed on your
#   system in a place where the dynamic linker CANNOT find it.  When
#   executing as root (or another user), your personal environment MAY
#   be set up to allow the dynamic linker to find the library.  When
#   executing as a daemon, FreeRADIUS MAY NOT have the same
#   personalized configuration.
#
#   To work around the problem, find out which library contains that symbol,
#   and add the directory containing that library to the end of 'libdir',
#   with a colon separating the directory names.  NO spaces are allowed.
#
#   e.g. libdir = /usr/local/lib:/opt/package/lib
#
#   You can also try setting the LD_LIBRARY_PATH environment variable
#   in a script which starts the server.
#
#   If that does not work, then you can re-configure and re-build the
#   server to NOT use shared libraries, via:
#
#	./configure --disable-shared
#	make
#	make install
#
libdir = /usr/lib/freeradius

#  pidfile: Where to place the PID of the RADIUS server.
#
#  The server may be signalled while it's running by using this
#  file.
#
#  This file is written when ONLY running in daemon mode.
#
#  e.g.:  kill -HUP `cat /var/run/radiusd/radiusd.pid`
#
pidfile = ${run_dir}/${name}.pid

#
#  correct_escapes: use correct backslash escaping
#
#  Prior to version 3.0.5, the handling of backslashes was a little
#  awkward, i.e. "wrong".  In some cases, to get one backslash into
#  a regex, you had to put 4 in the config files.
#
#  Version 3.0.5 fixes that.  However, for backwards compatibility,
#  the new method of escaping is DISABLED BY DEFAULT.  This means
#  that upgrading to 3.0.5 won't break your configuration.
#
#  If you don't have double backslashes (i.e. \\) in your configuration,
#  this won't matter to you.  If you do have them, fix that to use only
#  one backslash, and then set "correct_escapes = true".
#
#  You can check for this by doing:
#
#	$ grep '\\\\' $(find raddb -type f -print)
#
correct_escapes = true

#  panic_action: Command to execute if the server dies unexpectedly.
#
#  FOR PRODUCTION SYSTEMS, ACTIONS SHOULD ALWAYS EXIT.
#  AN INTERACTIVE ACTION MEANS THE SERVER IS NOT RESPONDING TO REQUESTS.
#  AN INTERACTICE ACTION MEANS THE SERVER WILL NOT RESTART.
#
#  THE SERVER MUST NOT BE ALLOWED EXECUTE UNTRUSTED PANIC ACTION CODE
#  PATTACH CAN BE USED AS AN ATTACK VECTOR.
#
#  The panic action is a command which will be executed if the server
#  receives a fatal, non user generated signal, i.e. SIGSEGV, SIGBUS,
#  SIGABRT or SIGFPE.
#
#  This can be used to start an interactive debugging session so
#  that information regarding the current state of the server can
#  be acquired.
#
#  The following string substitutions are available:
#  - %e   The currently executing program e.g. /sbin/radiusd
#  - %p   The PID of the currently executing program e.g. 12345
#
#  Standard ${} substitutions are also allowed.
#
#  An example panic action for opening an interactive session in GDB would be:
#
#panic_action = "gdb %e %p"
#
#  Again, don't use that on a production system.
#
#  An example panic action for opening an automated session in GDB would be:
#
#panic_action = "gdb -silent -x ${raddbdir}/panic.gdb %e %p 2>&1 | tee ${logdir}/gdb-${name}-%p.log"
#
#  That command can be used on a production system.
#

#  max_request_time: The maximum time (in seconds) to handle a request.
#
#  Requests which take more time than this to process may be killed, and
#  a REJECT message is returned.
#
#  WARNING: If you notice that requests take a long time to be handled,
#  then this MAY INDICATE a bug in the server, in one of the modules
#  used to handle a request, OR in your local configuration.
#
#  This problem is most often seen when using an SQL database.  If it takes
#  more than a second or two to receive an answer from the SQL database,
#  then it probably means that you haven't indexed the database.  See your
#  SQL server documentation for more information.
#
#  Useful range of values: 5 to 120
#
max_request_time = 30

#  cleanup_delay: The time to wait (in seconds) before cleaning up
#  a reply which was sent to the NAS.
#
#  The RADIUS request is normally cached internally for a short period
#  of time, after the reply is sent to the NAS.  The reply packet may be
#  lost in the network, and the NAS will not see it.  The NAS will then
#  re-send the request, and the server will respond quickly with the
#  cached reply.
#
#  If this value is set too low, then duplicate requests from the NAS
#  MAY NOT be detected, and will instead be handled as separate requests.
#
#  If this value is set too high, then the server will cache too many
#  requests, and some new requests may get blocked.  (See 'max_requests'.)
#
#  Useful range of values: 2 to 10
#
cleanup_delay = 5

#  max_requests: The maximum number of requests which the server keeps
#  track of.  This should be 256 multiplied by the number of clients.
#  e.g. With 4 clients, this number should be 1024.
#
#  If this number is too low, then when the server becomes busy,
#  it will not respond to any new requests, until the 'cleanup_delay'
#  time has passed, and it has removed the old requests.
#
#  If this number is set too high, then the server will use a bit more
#  memory for no real benefit.
#
#  If you aren't sure what it should be set to, it's better to set it
#  too high than too low.  Setting it to 1000 per client is probably
#  the highest it should be.
#
#  Useful range of values: 256 to infinity
#
max_requests = 16384

#  hostname_lookups: Log the names of clients or just their IP addresses
#  e.g., www.freeradius.org (on) or 206.47.27.232 (off).
#
#  The default is 'off' because it would be overall better for the net
#  if people had to knowingly turn this feature on, since enabling it
#  means that each client request will result in AT LEAST one lookup
#  request to the nameserver.   Enabling hostname_lookups will also
#  mean that your server may stop randomly for 30 seconds from time
#  to time, if the DNS requests take too long.
#
#  Turning hostname lookups off also means that the server won't block
#  for 30 seconds, if it sees an IP address which has no name associated
#  with it.
#
#  allowed values: {no, yes}
#
hostname_lookups = no

#
#  Logging section.  The various "log_*" configuration items
#  will eventually be moved here.
#
log {
	#
	#  Destination for log messages.  This can be one of:
	#
	#	files - log to "file", as defined below.
	#	syslog - to syslog (see also the "syslog_facility", below.
	#	stdout - standard output
	#	stderr - standard error.
	#
	#  The command-line option "-X" over-rides this option, and forces
	#  logging to go to stdout.
	#
	destination = files

	#
	#  Highlight important messages sent to stderr and stdout.
	#
	#  Option will be ignored (disabled) if output if TERM is not
	#  an xterm or output is not to a TTY.
	#
	colourise = yes

	#
	#  The logging messages for the server are appended to the
	#  tail of this file if destination == "files"
	#
	#  If the server is running in debugging mode, this file is
	#  NOT used.
	#
File: /freerad\sql
# -*- text -*-
##
## sql.conf -- SQL modules
##
##	$Id: 4a59483c35c77f573fb177919e19ba4434cc3da1 $

######################################################################
#
#  Configuration for the SQL module
#
#  The database schemas and queries are located in subdirectories:
#
#	sql/<DB>/main/schema.sql	Schema
#	sql/<DB>/main/queries.conf	Authorisation and Accounting queries
#
#  Where "DB" is mysql, mssql, oracle, or postgresql.
#
#

sql {
	# The sub-module to use to execute queries. This should match
	# the database you're attempting to connect to.
	#
	#    * rlm_sql_mysql
	#    * rlm_sql_mssql
	#    * rlm_sql_oracle
	#    * rlm_sql_postgresql
	#    * rlm_sql_sqlite
	#    * rlm_sql_null (log queries to disk)
	#
	driver = "rlm_sql_mysql"

#
#	Several drivers accept specific options, to set them, a
#	config section with the the name as the driver should be added
#	to the sql instance.
#
#	Driver specific options are:
#
#	sqlite {
#		# Path to the sqlite database
#		filename = "/tmp/freeradius.db"
#
#		# How long to wait for write locks on the database to be
#		# released (in ms) before giving up.
#		busy_timeout = 200
#
#		# If the file above does not exist and bootstrap is set
#		# a new database file will be created, and the SQL statements
#		# contained within the bootstrap file will be executed.
#		bootstrap = "${modconfdir}/${..:name}/main/sqlite/schema.sql"
# 	}
#
	mysql {
		# If any of the files below are set, TLS encryption is enabled
#		tls {
#			ca_file = "/etc/ssl/certs/my_ca.crt"
#			ca_path = "/etc/ssl/certs/"
#			certificate_file = "/etc/ssl/certs/private/client.crt"
#			private_key_file = "/etc/ssl/certs/private/client.key"
#			cipher = "DHE-RSA-AES256-SHA:AES128-SHA"
#		}

		# If yes, (or auto and libmysqlclient reports warnings are
		# available), will retrieve and log additional warnings from
		# the server if an error has occured. Defaults to 'auto'
		warnings = auto
	}
#
#	postgresql {
#
#		# unlike MySQL, which has a tls{} connection configuration, postgresql
#		# uses its connection parameters - see the radius_db option below in
#		# this file
#
#		# Send application_name to the postgres server
#		# Only supported in PG 9.0 and greater. Defaults to no.
#		send_application_name = yes
#	}
#

	# The dialect of SQL you want to use, this should usually match
	# the driver you selected above.
	#
	# If you're using rlm_sql_null, then it should be the type of
	# database the logged queries are going to be executed against.
	dialect = "mysql"

	# Connection info:
	#
	server = "localhost"
	port = 3306
	login = "radius"
	password = "radpass"

	# Database table configuration for everything except Oracle
	radius_db = "radius"

	# If you are using Oracle then use this instead
#	radius_db = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=your_sid)))"

	# If you're using postgresql this can also be used instead of the connection info parameters
#	radius_db = "dbname=radius host=localhost user=radius password=raddpass"

        # Postgreql doesn't take tls{} options in its module config like mysql does - if you want to
        # use SSL connections then use this form of connection info parameter
#	radius_db = "host=localhost port=5432 dbname=radius user=radius password=raddpass sslmode=verify-full sslcert=/etc/ssl/client.crt sslkey=/etc/ssl/client.key sslrootcert=/etc/ssl/ca.crt" 

	# If you want both stop and start records logged to the
	# same SQL table, leave this as is.  If you want them in
	# different tables, put the start table in acct_table1
	# and stop table in acct_table2
	acct_table1 = "radacct"
	acct_table2 = "radacct"

	# Allow for storing data after authentication
	postauth_table = "radpostauth"

	# Tables containing 'check' items
	authcheck_table = "radcheck"
	groupcheck_table = "radgroupcheck"

	# Tables containing 'reply' items
	authreply_table = "radreply"
	groupreply_table = "radgroupreply"

	# Table to keep group info
	usergroup_table = "radusergroup"

	# If set to 'yes' (default) we read the group tables unless Fall-Through = no in the reply table.
	# If set to 'no' we do not read the group tables unless Fall-Through = yes in the reply table.
	read_groups = yes

	# If set to 'yes' (default) we read profiles unless Fall-Through = no in the groupreply table.
	# If set to 'no' we do not read profiles unless Fall-Through = yes in the groupreply table.
	read_profiles = yes

	# Remove stale session if checkrad does not see a double login
	delete_stale_sessions = yes

	# Write SQL queries to a logfile. This is potentially useful for tracing
	# issues with authorization queries.  See also "logfile" directives in
	# mods-config/sql/main/*/queries.conf.  You can enable per-section logging
	# by enabling "logfile" there, or global logging by enabling "logfile" here.
	#
	# Per-section logging can be disabled by setting "logfile = ''"
	logfile = ${logdir}/sqllog.sql

	#  Set the maximum query duration and connection timeout
	#  for rlm_sql_mysql.
#	query_timeout = 5

	#  As of version 3.0, the "pool" section has replaced the
	#  following configuration items:
	#
	#  num_sql_socks
	#  connect_failure_retry_delay
	#  lifetime
	#  max_queries

	#
	#  The connection pool is new for 3.0, and will be used in many
	#  modules, for all kinds of connection-related activity.
	#
	# When the server is not threaded, the connection pool
	# limits are ignored, and only one connection is used.
	#
	# If you want to have multiple SQL modules re-use the same
	# connection pool, use "pool = name" instead of a "pool"
	# section.  e.g.
	#
	#	sql1 {
	#	    ...
	#	    pool {
	#	    	 ...
	#	    }
	#	}
	#
	#	# sql2 will use the connection pool from sql1
	#	sql2 {
	#	     ...
	#	     pool = sql1
	#	}
	#
	pool {
		#  Connections to create during module instantiation.
		#  If the server cannot create specified number of
		#  connections during instantiation it will exit.
		#  Set to 0 to allow the server to start without the
		#  database being available.
		start = ${thread[pool].start_servers}

		#  Minimum number of connections to keep open
		min = ${thread[pool].min_spare_servers}

		#  Maximum number of connections
		#
		#  If these connections are all in use and a new one
		#  is requested, the request will NOT get a connection.
		#
		#  Setting 'max' to LESS than the number of threads means
		#  that some threads may starve, and you will see errors
		#  like 'No connections available and at max connection limit'
		#
		#  Setting 'max' to MORE than the number of threads means
		#  that there are more connections than necessary.
		max = ${thread[pool].max_servers}

		#  Spare connections to be left idle
		#
		#  NOTE: Idle connections WILL be closed if "idle_timeout"
		#  is set.  This should be less than or equal to "max" above.
		spare = ${thread[pool].max_spare_servers}

		#  Number of uses before the connection is closed
		#
		#  0 means "infinite"
		uses = 0

		#  The number of seconds to wait after the server tries
		#  to open a connection, and fails.  During this time,
		#  no new connections will be opened.
		retry_delay = 30

		# The lifetime (in seconds) of the connection
		lifetime = 0

		#  idle timeout (in seconds).  A connection which is
		#  unused for this length of time will be closed.
		idle_timeout = 60

		#  NOTE: All configuration settings are enforced.  If a
		#  connection is closed because of "idle_timeout",
		#  "uses", or "lifetime", then the total number of
		#  connections MAY fall below "min".  When that
		#  happens, it will open a new connection.  It will
		#  also log a WARNING message.
		#
		#  The solution is to either lower the "min" connections,
		#  or increase lifetime/idle_timeout.
	}

	# Set to 'yes' to read radius clients from the database ('nas' table)
	# Clients will ONLY be read on server startup.
	read_clients = yes

	# Table to keep radius client info
	client_table = "nas"

	#
	# The group attribute specific to this instance of rlm_sql
	#

	# This entry should be used for additional instances (sql foo {})
	# of the SQL module.
#	group_attribute = "${.:instance}-SQL-Group"

	# This entry should be used for the default instance (sql {})
	# of the SQL module.
	group_attribute = "SQL-Group"

	# Read database-specific queries
	$INCLUDE ${modconfdir}/${.:name}/main/${dialect}/queries.conf
}


File: /freerad\sqlcounter
#  Rather than maintaining separate (GDBM) databases of
#  accounting info for each counter, this module uses the data
#  stored in the raddacct table by the sql modules. This
#  module NEVER does any database INSERTs or UPDATEs.  It is
#  totally dependent on the SQL module to process Accounting
#  packets.
#
#  The sql-module-instance' parameter holds the instance of the sql
#  module to use when querying the SQL database. Normally it
#  is just "sql".  If you define more and one SQL module
#  instance (usually for failover situations), you can
#  specify which module has access to the Accounting Data
#  (radacct table).
#
#  The 'reset' parameter defines when the counters are all
#  reset to zero.  It can be hourly, daily, weekly, monthly or
#  never.  It can also be user defined. It should be of the
#  form:
#  	num[hdwm] where:
#  	h: hours, d: days, w: weeks, m: months
#  	If the letter is ommited days will be assumed. In example:
#  	reset = 10h (reset every 10 hours)
#  	reset = 12  (reset every 12 days)
#
#  The 'key' parameter specifies the unique identifier for the
#  counter records (usually 'User-Name').
#
#  The 'query' parameter specifies the SQL query used to get
#  the current Counter value from the database. There are 2
#  parameters that can be used in the query:
#		%%b	unix time value of beginning of reset period
#		%%e	unix time value of end of reset period
#
#  The 'check_name' parameter is the name of the 'check'
#  attribute to use to access the counter in the 'users' file
#  or SQL radcheck or radcheckgroup tables.
#
#  DEFAULT  Max-Daily-Session > 3600, Auth-Type = Reject
#      Reply-Message = "You've used up more than one hour today"
#
#sqlcounter dailycounter {
#	sql_module_instance = sql
#	dialect = ${modules.sql.dialect}
#
#	counter_name = Daily-Session-Time
#	check_name = Max-Daily-Session
#	reply_name = Session-Timeout
#
#	key = User-Name
#	reset = daily
#
#	$INCLUDE ${modconfdir}/sql/counter/${dialect}/${.:instance}.conf
#}

#sqlcounter monthlycounter {
#	sql_module_instance = sql
#	dialect = ${modules.sql.dialect}
#
#	counter_name = Monthly-Session-Time
#	check_name = Max-Monthly-Session
#	reply_name = Session-Timeout
#	key = User-Name
#	reset = monthly
#
#	$INCLUDE ${modconfdir}/sql/counter/${dialect}/${.:instance}.conf
#}

sqlcounter noresetcounter {
	sql_module_instance = sql
	dialect = ${modules.sql.dialect}

	counter_name = Max-All-Session-Time
	check_name = Max-All-Session
	key = User-Name
	reset = never

	$INCLUDE ${modconfdir}/sql/counter/${dialect}/${.:instance}.conf
}

#
#  Set an account to expire T seconds after first login.
#  Requires the Expire-After attribute to be set, in seconds.
#  You may need to edit raddb/dictionary to add the Expire-After
#  attribute.
#sqlcounter expire_on_login {
#	sql_module_instance = sql
#	dialect = ${modules.sql.dialect}
#
#	counter_name = Expire-After-Initial-Login
#	check_name = Expire-After
#	key = User-Name
#	reset = never
#
#	$INCLUDE ${modconfdir}/sql/counter/${dialect}/${.:instance}.conf
#}


File: /general_settings.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>
<head>
<style>
h2{text-align:center;}
ul {
    list-style-type: none;
    margin: 0;
    margin-top: 120px;
    padding: 0;
    width: 250px;
    background-color: #f1f1f1;
    height:auto;
    overflow:auto;
    position:fixed;
    border:1px solid;
    font-weight:bold;
    text-transform:uppercase;
}

li a {
    display:block;
    color: #000;
    padding: 8px 0 8px 16px;
    text-decoration: none;
    text-align:left;
    border-bottom:1px solid;
}

 /*Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}

li a:.active {
    background-color: #4CAF50;
    color: white;
}
li:last-child {
    border-bottom: none;
}
    
*{font-family:Arial;}
label{
width:180px;
clear:left;
padding-right:0px;
}

input,label {
float:left;
border-radius:10px;
}
body {
background-color:#DFE2DB; 
}
input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:50px;
width:100px

}

fieldset {
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: left;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}
</style>
</head>

<body>
<p id="script">
<?php
require 'routeros_api.class.php';
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $username = "mgt";
	$servername = "localhost";
  $password = "admin_mgt";
  $dbname = "manager_db";

  $new_username = isset($_POST["new_admin_username"]) ? 
                  $_POST["new_admin_username"] : '';
  $new_password = isset($_POST["new_admin_password"]) ? 
                  $_POST["new_admin_password"] : '';

  $old_username = isset($_POST["old_admin_username"]) ? 
                  $_POST["old_admin_username"] : '';
  $old_password = isset($_POST["old_admin_password"]) ?
                  $_POST["old_admin_password"] : '';

  $new_radaddr = isset($_POST["new_radaddress"]) ? 
                 $_POST["new_radaddress"] : '';
  $new_radsecret = isset($_POST["new_radsecret"]) ? 
                   $_POST["new_radsecret"] : '';
  
  $conn_1 = new mysqli($servername, $username, $password, $dbname);

  if ($conn_1->connect_error) {
    die("Connection failed: " . $conn_1->connect_error);
  }

  $sql_1 = "update login set username=\"$new_username\",".
            " password=\"$new_password\" where id = 1";
  $sql_2 = "select * from login where id = 1";
  $sql_3 = "update radlogin set radaddress=\"$new_radaddr\",".
            " radsecret=\"$new_radsecret\" where id = 1";
  
  #get the old credentials
  $result = $conn_1->query($sql_2);
  $row = $result->fetch_assoc();
  $db_username = $row["username"];
  $db_password = $row["password"];

  #validate the user with the credentials
  if ($old_username === $db_username and $old_password === $db_password) {
    if ($conn_1->query($sql_1) === FALSE) {
      die("Query \"$sql_1\" failed!");
    } else {
      #change the credentials of the routers
      $conn_2 = new mysqli($servername, "radius", "radpass", "radius");
      if ($conn_2->connect_error) {
        die("Connection failed: " . $conn_2->connect_error);
      }
      $sql_4 = "select nasname from nas";
      $result_2 = $conn_2->query($sql_4);
      if ($result_2->num_rows > 0) {
        $API = new RouterosAPI();
        $API->debug = true; # hope this doesn't mess stuff up
        while ($row = $result_2->fetch_assoc()) {
          if ($API->connect($row["nasname"], $old_username, $old_password)) {
            $API->write("/user/set", false);
            $API->write("=.id=*1", false);
            $API->write("=name=$new_username", false);
            $API->write("=password=$new_password");
            $READ = $API->read(false);
          }
        } 
        $msg_1 = "<br><p>
                  <span style=\"color:green;\">
                  Credentials saved</span>
                  </p><br>";
      } else {
        $msg_1 = "<br><p>
                  <span style=\"color:green;\">
                  Credentials saved </span>
                  <span style=\"color:red;\">
                  but no routers added</span>
                  </p><br>";
      }
      $conn_2->close();
    }
    if ($conn_1->query($sql_3) === FALSE) {
      die("Query \"$sql_3\" failed!");
    } else {
      $msg_2 = "<br><p>
      <span style=\"color:green;\">RADIUS settings saved</p><br>";
    }
  }

  $conn_1->close();

}
?>
</p>
<?php require 'menu.php';?>
<h2>GENERAL SETTINGS</h2>
<div class="form">
<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" 
      method="post">
<fieldset>
<legend><b>RADIUS<b></legend>
<label>New IP Address:</label>
<input type="text" name="new_radaddress" required="required"><br><br>
<label>New Secret:</label>
<input type="password" name="new_radsecret" required="required"><br><br>
</fieldset>

<fieldset>
<legend><b>ADMIN<b></legend>
<label>New Username:</label>
<input type="text" name="new_admin_username" required="required"><br><br>
<label>New Password:</label>
<input type="password" name="new_admin_password" required="required"><br><br>
</fieldset>

<fieldset>
<legend><b>CONFIRM YOUR IDENTITY<b></legend>
<label>Current Username:</label>
<input type="text" name="old_admin_username" required="required"><br><br>
<label>Current Password:</label>
<input type="password" name="old_admin_password" required="required"><br><br>
<input type="submit" value="SUBMIT"><br><br>
</fieldset>
</form>

<form action="<?php echo htmlspecialchars('upload_Logo.php');?>"
      method="post" enctype="multipart/form-data">
<fieldset>
<legend><b>CUSTOM LOGO<b></legend>
<label>PNG Image (500 KB Max)</label>
<input type="file" name="fileToUpload" id="fileToUpload"><br><br>
<input type="submit" value="UPLOAD"><br><br>
</fieldset>
</form>
<?php if(isset($msg_1)) {echo $msg_1;}
      if(isset($msg_2)) {echo $msg_2;} ?>
</div>

<script>
document.getElementById("script").innerHTML = "";
</script>

</body>

</html>


File: /hotspots.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>
<head>
<style>
table {width:43%;}
table, th, td {
	border:1px solid grey; border-collapse:collapse; padding:5px;	}

h2{text-align:center;}
ul {
    list-style-type: none;
    margin: 0;
    margin-top: 120px;
    padding: 0;
    width: 250px;
    background-color: #f1f1f1;
    height:auto;
    position:fixed;
    overflow:auto;
    border:1px solid;
    font-weight:bold;
    text-transform:uppercase;
}

li a {
    display:block;
    color: #000;
    padding: 8px 0 8px 16px;
    text-decoration: none;
    text-align:left;
    border-bottom:1px solid;
}

/* Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}

li a:.active {
    background-color: #4CAF50;
    color: white;
}
li:last-child {
    border-bottom: none;
}
    
*{font-family:Arial;}
label{
width:180px;
clear:left;

padding-right:0px;
}

input,label {
float:left;
border-radius:10px;
}
body {
background-color:#DFE2DB; 
}
input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:50px;
width:100px;
}

fieldset {
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: left;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}
</style>
</head>

<body>
<p id="script">
<?php
require "configure_hotspot.php";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $net = $_POST["hs_net"];
  $octs = multiexplode(array(".", "/"), $net);
  if (count($octs) == 5 and $octs[4] >= 22 and $octs[4] <= 29 
      and checkOctet_bool($octs[0]) and checkOctet_bool($octs[1]) 
      and checkOctet_bool($octs[2]) and checkOctet_bool($octs[3])) {
    $servername = "localhost";
    $username = "radius";
    $password = "radpass";
    $dbname = "radius";
  
    $conn_1 = new mysqli($servername, $username, $password, $dbname);
    $conn_2 = new mysqli($servername, "mgt", "admin_mgt", "manager_db");
    if ($conn_1->connect_error or $conn_2->connection_error) {
      die("Connection failed: " . $conn_1->connect_error . " " 
            .$conn_2->connection_error);
    }
  
    $sql_1 = "select nasname from nas";
    $result = $conn_1->query($sql_1);
    
    $sql_2 = "select * from login where id = 1";
    $login = ($conn_2->query($sql_2))->fetch_assoc();

    if ($result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        setup($row["nasname"], $login["username"], $login["password"]);
      }
    } 
    $conn_1->close(); 
    $conn_2->close();
  } else {
    //$msg = "<p><span style=\"color:red;\">
    //        Invalid subnet mask or network</span></p>";
  }
}
?>
</p>
<?php require 'menu.php'; ?>
<div id="form" class="form">
<h2>HOTSPOTS</h2>
<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" 
      method="post">
<fieldset>
<legend><b>SETTINGS FOR ALL HOTSPOTS<b></legend>
<label>SSID:</label>
<input type="text" name="hs_ssid" required="required"><br><br>
<label>Network:</label>
<input type="text" name="hs_net" required="required">
<?php if(isset($msg)) { echo $msg; }?><br><br>
<label>DNS name:</label>
<input type="text" name="hs_dns" required="required"><br><br>
<input type="submit" value="SETUP ALL">
</fieldset>
</form>

<form action="<?php echo htmlspecialchars('setup_one_hotspot.php');?>" 
      method="post">
<fieldset>
<legend><b>SETTINGS FOR ONE HOTSPOT<b></legend>
<label>SSID:</label>
<input type="text" name="hs_ssid" required="required"><br><br>
<label>Network:</label>
<input type="text" name="hs_net" required="required">
<?php if(isset($msg)) { echo $msg; }?>
<br><br>
<label>DNS name:</label>
<input type="text" name="hs_dns" required="required"><br><br>
<label>Router IP Address:</label>
<input type="text" name="router_addr"><br><br> <!--make a dropdown list-->
<input type="submit" value="SETUP">
</fieldset>
</form>
<!--
<form action="<?php echo htmlspecialchars('reset_all_hotspots.php');?>" 
      method="post">
<fieldset>
<legend><b>RESET ONE HOTSPOT<b></legend>
<label>IP address:</label>
<input type="text" name="hs_addr" required="required"><br><br>
<input type="submit" value="RESET">
</fieldset>
</form>
-->
</div>

<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	echo "<h2>HOTSPOT CREATED WITH THE FOLLOWING SETTINGS</h2>";
	echo "<table align='center'>";

	echo "<tr>";
	echo "<th>HOTSPOT NAME</th>";
	echo "<th>HOTSPOT ADDRESS</th>";
	echo "</tr>";

	echo "<tr>";
	echo "<td>" . $_POST["hs_ssid"] . "</td>";
	echo "<td>" . $_POST["hs_net"] . "</td>";
	echo "</tr>";

	echo "</table>";

	echo '<script src="script.js">';
}

?>
<script>
document.getElementById("script").innerHTML = "";
</script>


</body>

</html>


File: /index.php
<?php session_start(); /* Starts the session */

if(!isset($_SESSION['UserData']['Username'])){
	header("location:login.php");
	
	exit;
}
?>
require 'voucher.php';
Congratulation! You have logged into password protected page. <a href="logout.php">Click here</a> to Logout.


File: /init\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>internet hotspot > login</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />
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
<a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
	<tr>
	<td align="center" valign="middle">
		<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br />$(if trial == 'yes')Free trial available, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)</div><br />
		<table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
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
								<tr><td align="right">password</td>
										<td><input style="width: 80px" name="password" type="password"/></td>
								</tr>
								<tr><td>&nbsp;</td>
										<td><input type="submit" value="OK" /></td>
								</tr>
							</table>
					</form>
				</td>
			</tr>
			<tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="company_logo.png" alt="logo" width="95" height="95"/></a></td></tr>
		</table>
	
	<br /><div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
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


File: /login.php
<!DOCTYPE html>
<html>
<head>
<style>
body{
background-image:url("imgback.jpg");
}
fieldset, legend{font-family:Arial;}

h1,h3{
text-align:center;
font-family:oblique;

}
div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}

input,label {
float:left;
border-radius:10px;
}
fieldset {
width:350px;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: right;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:40px;
}
</style>
</head>
<?php session_start(); /* Starts the session */

	
	/* Check Login form submitted */	
	if(isset($_POST['Submit'])){
		/* Define username and associated password array */
//$logins = array('netface' => '123456','username1' => 'password1','username2' => 'password2');
		$username = "mgt";
    $password = "admin_mgt";
    $server = "localhost";
    $db = "manager_db";

    $conn = new mysqli($server, $username, $password, $db);

    if ($conn->connect_error) {
      die("Connection failed: " . $conn->conncet_error);
    }

    $sql_1 = "select * from login where id = 1";
    $result = $conn->query($sql_1);
    $row = $result->fetch_assoc();
    $db_username = $row["username"];
    $db_password = $row["password"];

		/* Check and assign submitted Username and Password to new variable */
		$Username = isset($_POST['Username']) ? $_POST['Username'] : '';
		$Password = isset($_POST['Password']) ? $_POST['Password'] : '';
		
		/* Check Username and Password existence in defined array */		
		if ($Username === $db_username & $Password === $db_password){
			/* Success: Set session variables and redirect to Protected page  */
		    
			$_SESSION['UserData']['Username']=$db_password;
			
			header("location:routers.php");
			
			exit;
		} else {
			/*Unsuccessful attempt: Set error message */
			$msg="<span style='color:red'>Invalid Login Details</span>";
		}
	}
?>

<img src="logo/company_logo.png" alt="Company Logo" width=100 height=100>

<h1>WELCOME TO NETFACE</h1>
<h3>Your configurations partner</h3>
<div class="form">
<form action="" method="post" name="Login_Form">
<fieldset>
<legend><b>LOGIN DETAILS</b></legend>
  <table width="400" border="0" align"center" cellpadding="5" cellspacing="1" class="Table">
    <?php if(isset($msg)){?>
    <tr>
      <td colspan="2" align="center" valign="top"><?php echo $msg;?></td>
    </tr>
    <?php } ?>
   
    <tr>
      <td align="right" valign="top"><b>Username</b></td>
      <td><input name="Username" type="text" class="Input"></td>
    </tr>
    <tr>
      <td align="right"><b>Password</b></td>
      <td><input name="Password" type="password" class="Input"></td>
    </tr>
    <tr>
      <td> </td>
      <td><input name="Submit" type="submit" value="LOGIN" class="Button3"></td>
    </tr>
  </table>
</fieldset>

</form>
</div>
<script type="text/javascript">
  function noBack() {
    window.history.forward()
  }
  noBack();
  window.onload = noBack;
  window.onpageshow = function(evt) { if (evt.persisted) noBack() }
  window.onunload = function() { void (0) }
</script>
<script>
window.location.hash="no-back-button";
window.location.hash="Again-No-back-button";//again because google chrome don't insert first hash into history
window.onhashchange=function(){window.location.hash="no-back-button";}
</script>
</html>


File: /logout.php
<?php session_start(); /* Starts the session */
session_destroy(); /* Destroy started session */
header("location:login.php");  /* Redirect to login page */
exit;
?>

File: /make_vouchers.php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $servername = "localhost"; 
  $username = "radius";
  $password = "radpass";
  $dbname = "radius";
  
  $voucher_prefix = $_POST["voucher_prefix"];
  $num_vouchers = $_POST["num_vouchers"];
  $time_limit = (int) (((float) $_POST["time_limit"]) * 3600); #seconds
  $group_name = "group_" . $_POST["time_limit"] . "_hours";

  #file to download
  $voucher_file_name = "$group_name" . "_vouchers.txt";
  $vouchers_str = "";

  #set header
  header("Content-Type: text/plain");
  header("Content-disposition: attachment; filename=$voucher_file_name");
  header("Content-Transfer-Encoding: binary");
  header("Pragma: no-cache");
  header("Expires: 0");

  $conn = new mysqli($servername, $username, $password, $dbname);
  
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  #make vouchers
  for ($x = 0; $x < $num_vouchers; $x++) {
    $randu = substr(md5(microtime()), rand(0, 26), 5);
    $voucher_login = $voucher_prefix . "_" . $randu;
    $randpw = substr(md5(microtime()), rand(0, 26), 5);
    $voucher_pw = $randpw;

    $sql_1 = "insert into radcheck (username, attribute, op, value) values " .
            "(\"$voucher_login\", \"MD5-Password\", \":=\"," . 
            " MD5(\"$voucher_pw\"))";
    if ($conn->query($sql_1) == FALSE) {
      echo "Error :" . $sql_1 . "\n" .  $conn->error . "\n";
    }

    $vouchers_str =  $vouchers_str . 
            "Username: " . $voucher_login . "\nPassword: " 
            . $voucher_pw . "\n\n";

    $sql_2 = "insert into radusergroup (username, groupname, priority)" .
              " values (\"$voucher_login\", \"$group_name\", \"1\")";
    if ($conn->query($sql_2) == FALSE) {
      echo "Error :" . $sql_2 . "\n" . $conn->error . "\n";
    }

  }
  
  $sql_groupcheck = "select attribute from radgroupcheck " . 
                      "where groupname = \"$group_name\"";
  $sql_groupreply = "select attribute from radgroupreply " . 
                      "where groupname = \"$group_name\"";
  $result_1 = $conn->query($sql_groupcheck);
  $result_2 = $conn->query($sql_groupreply);
  
  if ($result_1->num_rows == 0 && $result_2->num_rows == 0) {
    #create group attributes
  
    #in radgroupcheck
    $sql_3 = "insert into radgroupcheck (groupname, attribute, op, value)" . 
              " values (\"$group_name\", \"Max-All-Session\"," . 
              " \":=\", \"$time_limit\")";
    if ($conn->query($sql_3) == FALSE) {
        echo "Error :" . $sql_3 . "\n" . $conn->error . "\n";
    }
  
    #in radgroupreply
    $sql_4 = "insert into radgroupreply (groupname, attribute, op, value)" .
              " values (\"$group_name\", \"Session-Timeout\"," . 
              " \":=\", \"$time_limit\"), " .
              "(\"$group_name\", \"Framed-Compression\"," .
              " \":=\", \"Van-Jacobsen-TCP-IP\"), " .
              "(\"$group_name\", \"Framed-Protocol\"," .
              " \":=\", \"PPP\"), " .
              "(\"$group_name\", \"Framed-MTU\"," .
              " \":=\", \"1500\"), " .
              "(\"$group_name\", \"Service-Type\"," .
              " \":=\", \"Login-User\")";
    if ($conn->query($sql_4) == FALSE) {
        echo "Error :" . $sql_4 . "\n" . $conn->error . "\n";
    }
  }
  
  $conn->close();
  
  #write file
  echo "$vouchers_str";
}

?>


File: /menu.php
<?php
  echo 
  ' <img src="logo/company_logo.png" alt="Company Logo" 
               width=100 height=100 style="position:fixed"> 
  <ul>
         <li><a href="routers.php">Routers</a></li>
      <li><a href="general_settings.php">General Settings</a></li>
      <li><a href="hotspots.php">Hotspots</a></li>
         <li><a href="vouchers.php">Vouchers</a></li>
         <li><a href="logout.php">Log out</a></li>
  </ul>
  

  ';
?>




File: /README.md
# NETFACE-MikroTik-Hotspot-Manager

This project aims to create a user-friendly interface for regular business owners to use MikroTik routers as hotspots in their businesses. The server-side is implemented in PHP. It basically utilises a RADIUS server (<a href="https://freeradius.org/">FreeRADIUS</a>), used for authenticating, authorisation and accounting, of users connecting to the MikroTik hotspots. The system creates vouchers with MD5 passwords. These vouchers are then authenticated with <a href="https://www.tldp.org/LDP/nag/node120.html">PAP</a> via the RADIUS server, since it accepts both clear-text and encrypted passwords. 


File: /remove_router.php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $servername = "localhost";
  $username = "radius";
  $password = "radpass";
  $dbname = "radius";
  
  $addr = $_POST["router_addr"];

  $conn = new mysqli($servername, $username, $password, $dbname);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql_1 = "delete from nas where nasname = \"$addr\"";
  if ($conn->query($sql_1) == FALSE) {
    echo "Error: " . $sql_1 . "\h" . $conn->error . "\n";
  } else {
    header("Location: routers.php");
    //echo "Router removed!";
  }

  $conn->close();
}
?>




File: /routeros_api.class.php
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
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
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


File: /routers.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>

<head>

<style>

table {width:43%;}

table, th, td {
	border:1px solid grey; border-collapse:collapse; padding:5px;
} 

h2{text-align:center;}
ul {
    list-style-type: none;
    margin: 0;
    margin-top: 120px;
    padding: 0;
    width: 250px;
    background-color: #f1f1f1;
    height:auto;
    position:fixed;
    overflow:auto;
    border:1px solid;
    font-weight:bold;
    text-transform:uppercase;
}

li a {
    display:block;
    color: #000;
    padding: 8px 0 8px 16px;
    text-decoration: none;
    text-align:left;
    border-bottom:1px solid;
}

/* Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}

li a:.active {
    background-color: #4CAF50;
    color: white;
}
li:last-child {
    border-bottom: none;
}
    
*{font-family:Arial;}
label{
width:180px;
clear:left;

padding-right:0px;
}

input,label {
float:left;
border-radius:10px;
}
body {
background-color:#DFE2DB; 
/*background-image:url("wi-fi-img.png");
background-repeat:no-repeat;*/
}
input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:50px;
width:100px;
}

fieldset {
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: left;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}
</style>
</head>

<body>
<p>
<?php
//require 'mik_loginpage_upload.php';
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $servername = "localhost";
  $username = "radius";
  $password = "radpass";
  $dbname = "radius";
  
  $addr = $_POST["router_addr"];
  $name = $_POST["router_name"];
  
  $conn_1 = new mysqli($servername, "mgt", "admin_mgt", "manager_db");
  $conn_2 = new mysqli($servername, $username, $password, $dbname);

  if ($conn_1->connect_error or $conn_2->connect_error) {
    die("Connection failed: " . $conn_1->connect_error . " " 
          . $conn_2->connect_error);
  }

  $sql_1 = "select radsecret from radlogin where id = 1";
  $result = $conn_1->query($sql_1);
  $row = $result->fetch_assoc();
  $secret = $row["radsecret"];
  $sql_2 = "insert into nas (nasname, secret, shortname) values " .
           "(\"$addr\", \"$secret\", \"$name\")";

  if ($conn_2->query($sql_2) == FALSE) {
    $msg = "<p><span style=\"color:red\">Error adding router</span></p>";
  } else {
    $msg = "<p><span style=\"color:green\">Router added</span></p>";
  }

  $conn_1->close();
  $conn_2->close();
}
?>
</p>
<?php require 'menu.php'; ?>

<h2>ROUTERS</h2>
<div class="form">
<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" 
      method="post">
<fieldset>
<legend><b>ADD ROUTER<b></legend>
<label>IP Address:</label>
<input type="text" name="router_addr" required="required"><br><br>
<label>Name:</label>
<input type="text" name="router_name" required="required"><br><br>
<input type="submit" value="ADD">
</fieldset>
</form>
</div>
<br>
<div class="form">
<form action="<?php echo htmlspecialchars('remove_router.php');?>"
      method="post">
<fieldset>
<legend><b>REMOVE ROUTER<b></legend>
<label>IP address:</label>
<input type="text" name="router_addr" required="required"><br><br>
<input type="submit" value="REMOVE"> <!--make a dropdown list-->
</fieldset>
</form>
</div>
<?php
function uploadMikLoginPage($router_addr, $login_file) { 
  $trg_file_path = "/hotspot/$login_file";
  $conn_id = ftp_connect($router_addr);
  $conn_1 = new mysqli("localhost", "mgt", "admin_mgt", "manager_db");
  if ($conn_1->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  $sql_2 = "select * from login where id = 1";
  $result = $conn_1->query($sql_2);
  $row = $result->fetch_assoc();
  $login_result = ftp_login($conn_id, $row["username"], $row["password"]);
  if (ftp_put($conn_id, $trg_file_path, 
              "/var/www/html/init/" . $login_file, FTP_ASCII)) {
    echo "<p><span style=\"color:green\">
          Successfully uploaded your login page to router</span></p>";
  } else {
    echo "<p><span style=\"color:red\">
          There was a problem while uploading your login page to router
          </span></p>";
  }
  $conn_1->close();
  ftp_close($conn_id);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $addr = $_POST["router_addr"];
  if(isset($msg)) {echo $msg;}
  uploadMikLoginPage($addr, "login.html");
}
	$servername = "localhost";
  $username = "radius";
  $password = "radpass";
  $dbname = "radius";
  

  $conn = new mysqli($servername, $username, $password, $dbname);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql_2 = "select nasname, shortname from nas";
  $result = $conn->query($sql_2);

	echo "<h2>ROUTERS ADDED</h2>";

	echo "<table align='center'>";

	echo "<tr>";
	echo "<th>ROUTER NAME</th>";
	echo "<th>ROUTER ADDRESS</th>";
	echo "</tr>";

  if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
      echo "<tr>";
      echo "<td>" . $row["shortname"] . "</td>";
	    echo "<td>" . $row["nasname"] . "</td>";
      echo "</tr>";
    }
  } else {
    echo "<tr>";
    echo "<td> --- </td>";
    echo "<td> --- </td>";
    echo "</tr>";
  }

	echo "</table>";

  $conn->close();

?>

</body>

</html>


File: /script.js
document.getElementById("form").innerHTML = "";
document.getElementById("script").innerHTML = "";


File: /scripts\central_router_config.rsc
/system identity set name=Central_Router
/ip dhcp-client add interface=ether1 disabled=no use-peer-dns=yes \
use-peer-ntp=yes add-default-route=yes
/interface bridge add name=Central-Bridge disabled=no arp=enabled \
protocol-mode=stp
/interface ethernet set 2,3,4 master-port=ether2
/interface bridge port add interface=ether2 bridge=Central-Bridge
/ip address add address=<bridge addr w/ mask> interface=Central-Bridge
/ip pool add name=Central-Pool ranges=<pool range>
/ip dhcp-server add name=dhcp-srv-1 disabled=no address-pool=Central-Pool \
lease-time=3d interface=Central-Bridge
/ip dhcp-server network add address=<HS network w/ mask> gateway=<bridge addr w/o mask>
/routing ospf instance set default router-id=<bridge addr w/o mask> \
redistribute-connected=as-type-1 redistribute-other-ospf=as-type-1
/routing ospf network add network=<HS net w/ mask> area=backbone
/routing ospf network add network=<ISP net w/ mask> area=backbone
/ip firewall nat add action=dst-nat protocol=tcp dst-address=<ether1 addr w/o mask> \
dst-port=80 to-address=<web server addr w/o mask> to-port=80 chain=dstnat disabled=no
/user set 0 password=<user password>


File: /scripts\hotspot_config.rsc
/system identity set name=HSn
/ip dhcp-client add interface=ether1 add-default-route=yes disabled=no \
use-peer-dns=yes use-peer-ntp=yes
/interface bridge add name=loopback1 disabled=no arp=disabled \
protocol-mode=none
/ip address add address=<loopback addr w/ mask> interface=loopback1
/routing ospf instance set 0 router-id=<loopback addr w/o mask> \
redistribute-connected=as-type-1 redistribute-other-ospf=as-type-1
/routing ospf network add network=<HS net w/ mask> area=backbone
/ip service set 5 disabled=no
/user set 0 password=<user password>


File: /setup_one_hotspot.php
<?php //require "disabler.php"?>;
<!DOCTYPE html>
<html>
<head>
<style>
table {width:43%;}
table, th, td {
	border:1px solid grey; border-collapse:collapse; padding:5px;	} </style>
</head>
<!--<head>
<style>
a:link, a:visited {
	background-color: #f44336;
	color:white;
	padding:14px 25px;
	text-align:center;
	text-decoration:none;
	display:inline-block;
}
a:hover, a:active {
	background-color:red;
}
</style>
</head>-->

<body>
<p id="script">
<?php
require "configure_hotspot.php";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $net = $_POST["hs_net"];
  $octs = multiexplode(array(".", "/"), $net);
  if (count($octs) == 5 and $octs[4] >= 22 and $octs[4] <= 29 
      and checkOctet_bool($octs[0]) and checkOctet_bool($octs[1]) 
      and checkOctet_bool($octs[2]) and checkOctet_bool($octs[3])) {
    $conn = new mysqli("localhost", "mgt", "admin_mgt", "manager_db");
    if ($conn->connection_error) {
      die("Connection failed: " . $conn->connection_error);
    }
    $result = $conn->query("select * from login where id = 1");
    $row = $result->fetch_assoc();
    setup($_POST["router_addr"], $row["username"], $row["password"]);
    $conn->close();
  } else {
    $msg = "<p><span style=\"color:red\">
            Invalid subnet mask or network</span></p>";
  }
}
?>
</p>

<?php //require 'menu.php'; ?>

<!--<div id="form">
<form action="<?php //echo htmlspecialchars($_SERVER['PHP_SELF']);?>" 
      method="post">

<h2>SETUP HOTSPOT</h2>

<fieldset>
<legend><b>HOTSPOT SETTINGS<b></legend>
SSID:
<input type="text" name="hs_ssid"><br><br>
Network:
<input type="text" name="hs_net">
<br><br>
DNS name:
<input type="text" name="hs_dns"><br><br>
</fieldset>

<br><br>
<fieldset>
<legend><b>ROUTER<b></legend>
IP Address:
<input type="text" name="router_addr"><br><br>
</fieldset>

<br>
<input type="submit" value="SETUP">
</form>
</div>-->
<?php if(isset($msg)) { echo $msg; }?>
<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST'and !isset($msg)) {
	echo "<h2>HOTSPOT CREATED WITH THE FOLLOWING SETTINGS</h2>";
	echo "<table align='center'>";

	echo "<tr>";
	echo "<th>HOTSPOT NAME</th>";
	echo "<th>HOTSPOT ADDRESS</th>";
	echo "</tr>";

	echo "<tr>";
	echo "<td>" . $_POST["hs_ssid"] . "</td>";
	echo "<td>" . $_POST["hs_net"]. "</td>";
	echo "</tr>";

	echo "</table>";

	echo '<script src="script.js">';
}

?>
<script>
document.getElementById("script").innerHTML = "";
</script>


</body>

</html>


File: /tutorial.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>
<head>
<style>
h2, h3, h4, p{text-align:center;}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 250px;
    background-color: #f1f1f1;
    height:auto;
    position:fixed;
    overflow:auto;
    border:1px solid;
    font-weight:bold;
    text-transform:uppercase;
}

li a {
    display:block;
    color: #000;
    padding: 8px 0 8px 16px;
    text-decoration: none;
    text-align:left;
    border-bottom:1px solid;
}

/* Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}

li a:.active {
    background-color: #4CAF50;
    color: white;
}
li:last-child {
    border-bottom: none;
}
    
*{font-family:Arial;}
label{
width:180px;
clear:left;

padding-right:0px;
}

input,label {
float:left;
border-radius:10px;
}
body {
background-color:#DFE2DB; 
}
input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:40px;


}

fieldset {
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: left;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}
</style>
</head>

<body>
<p></p>
<?php require 'menu.php';?>
<h2>TUTORIAL</h2>
<h3>HOW TO SETUP A HOTSPOT</h3>
<p></p>
<h4>STEP 1: ADD A MIKROTIK ROUTER TO THIS WEB INTERFACE</h4>
<p> Click "Routers" on the menu above. Go to the "ADD ROUTER" section. 
<p> Type in the <b>IP address</b> of the router you want to add, 
    for example 10.10.1.1. </p>
<p> Next, type in the <b>Name</b> of that router. 
    This could be anything you want, for example "Conference Hall Hotspot".</p>
<p> Lastly, type in the <b>RADIUS secret</b>. This is a secret password which 
    your router uses for authentication from the RADIUS server. Without it, 
    your router will not be able to provide internet to your users. 
    We recommend setting a secure password. </p>
<p> Click <b>ADD</b> when done. 
    You will see your added router at the bottom of that page.</p>
<p></p>

</body>

</html>


File: /upload_logo.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>
<head>
<style>
a:link, a:visited {
    background-color: #f44336;
    color: white;
    padding: 14px 25px;
    text-align: center;	
    text-decoration: none;
    display: inline-block;
}
a:hover, a:active {
    background-color: red;
}
</style>
</head>

<body>
<p></p>
<?php require 'menu.php';?>
<h2>UPLOAD CUSTOM LOGO</h2>
<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>"
      method="post" enctype="multipart/form-data">
Select image to upload (PNG format only):
<input type="file" name="fileToUpload" id="fileToUpload"><br><br>
<input type="submit" value="UPLOAD" name="submit"><br><br>
</form>

<?php
function uploadMikLogo($router_addr, $logo_file) { 
  $trg_file_path = "/hotspot/$logo_file";
  $conn_id = ftp_connect($router_addr);
  $login_result = ftp_login($conn_id, "admin", "");
  if (ftp_put($conn_id, $trg_file_path, "/var/www/html/logo/" . $logo_file,
              FTP_BINARY)) {
    echo "Successfully uploaded your logo to router " . $router_addr;
  } else {
    echo "There was a problem uploading your logo to router " . $router_addr;
  }
  ftp_close($conn_id);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $target_dir = "logo/";
  $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
  $uploadOk = 1;
  $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
  // Check if image file is a actual image or fake image
  if(isset($_POST["submit"])) {
      $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
      if($check !== false) {
          echo "File is an image - " . $check["mime"] . ".";
          $uploadOk = 1;
      } else {
          echo "File is not an image.";
          $uploadOk = 0;
      }
  }
  // Check if file already exists
  if (file_exists($target_file)) {
      echo "Sorry, the logo already exists.";
      $uploadOk = 0;
  }
  // Check file size
  $KiB = 1024;
  if ($_FILES["fileToUpload"]["size"] > (500 * $KiB)) {
      echo "Sorry, your file is too large.";
      $uploadOk = 0;
  }
  // Allow only PNG file format
  if($imageFileType != "png") {
      echo "Sorry, only PNG files are allowed.";
      $uploadOk = 0;
  }
  // Check if $uploadOk is set to 0 by an error
  if ($uploadOk == 0) {
      echo "Sorry, your logo was not uploaded.";
  // if everything is ok, try to upload file
  } else {
      if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"],
                              $target_file)) {
          rename($target_file, $target_dir . "company_logo.png");
          $conn = new mysqli("localhost", "radius", "radpass", "radius");
          if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
          }
          $sql_1 = "select nasname from nas";
          $result = $conn->query($sql_1);
          if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
              uploadMikLogo($row["nasname"], "company_logo.png");
            }
          }
          echo "Successfully uploaded your logo to Web UI.";
          $conn->close();
      } else {
          echo "There was an problem while uploading your logo to Web UI.";
      }
  }

}
?> 
</body>
</html> 


File: /vouchers.php
<?php require "disabler.php";?>
<!DOCTYPE html>
<html>
<head>
<style>
h2{text-align:center;}
ul {
    list-style-type: none;
    margin: 0;
    margin-top: 120px;
    padding: 0;
    width: 250px;
    background-color: #f1f1f1;
    height:auto;
    position:fixed;
    overflow:auto;
    border:1px solid;
    font-weight:bold;
    text-transform:uppercase;
}

li a {
    display:block;
    color: #000;
    padding: 8px 0 8px 16px;
    text-decoration: none;
    text-align:left;
    border-bottom:1px solid;
}

/* Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}

li a:.active {
    background-color: #4CAF50;
    color: white;
}
li:last-child {
    border-bottom: none;
}
    
*{font-family:Arial;}
label{
width:180px;
clear:left;

padding-right:0px;
}

input,label {
float:left;
border-radius:10px;
}
body {
background-color:#DFE2DB; 
}
input[type=submit]{
color:white;
text-shadow: 0px 1px 1px #ffffff;
border-bottom: 2px solid #b2b2b2;
background-color: #333;
height:50px;
width:100px;
}

fieldset {
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 20px;
text-align: left;}
legend {
background-color: #efefef;
border: 1px solid #dcdcdc;
border-radius: 10px;
padding: 10px 20px;
text-align: left;
}

div.form
{
display:block;
text-align:center;
}
form
{
display:inline-block;
margin-left:auto;
margin-right:auto;
text-align:left;
}
</style>
</head>

<body>
<p></p>
<?php require 'menu.php';?>
<h2>VOUCHERS</h2>
<div class="form">
<form action="<?php echo htmlspecialchars('make_vouchers.php');?>" 
      method="post">
<fieldset>
<legend><b>MAKE NEW VOUCHERS<b></legend>
<label>Voucher prefix:</label>
<input type="text" name="voucher_prefix" required="required"><br><br>
<label>Number of Vouchers:</label>
<input type="text" name="num_vouchers" required="required"><br><br>
<label>Time Limit (in hours):</label>
<input type="text" name="time_limit" required="required"><br><br>
<input type="submit" value="SUBMIT">
</fieldset>
</form>

<br>
<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>"
      method="post">
<fieldset>
<legend><b>FLUSH OLD VOUCHERS<b></legend>
<input type=submit value="FLUSH"><br><br>
</fieldset>
</form>
</div>
<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	$servername = "localhost";
  $username = "radius";
  $password = "radpass";
  $dbname = "radius";
  
  $conn = new mysqli($servername, $username, $password, $dbname);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql_1 = "drop table radcheck";
  $sql_2 = "drop table radusergroup";

  if ($conn->query($sql_1) == FALSE & $conn->query($sql_2) == FALSE) {
    die("Query \"$sql_1\" or \"$sql_2\" failed!");
  } else {
    $sql_3 = "CREATE TABLE radcheck (
                id int(11) unsigned NOT NULL auto_increment,
                username varchar(64) NOT NULL default '',
                attribute varchar(64)  NOT NULL default '',
                op char(2) NOT NULL DEFAULT '==',
                value varchar(253) NOT NULL default '',
                PRIMARY KEY  (id),
                KEY username (username(32))
              )";
    $sql_4 = "CREATE TABLE radusergroup (
                username varchar(64) NOT NULL default '',
                groupname varchar(64) NOT NULL default '',
                priority int(11) NOT NULL default '1',
                KEY username (username(32))
              )";
    if ($conn->query($sql_3) == FALSE & $conn->query($sql_4) == FALSE) {
     die("Query \"$sql_3\" or \"$sql_4\" failed!"); 
    } else {
      echo "<br><br><p>
      <span style=\"color:green\">Vouchers flushed!</span>
      </p><br><br>";
    }
  }

  $conn->close();

}
?>

</body>

</html>


