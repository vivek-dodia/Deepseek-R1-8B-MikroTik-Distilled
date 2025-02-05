# Repository Information
Name: MikrotikBlockDangerAddresses

# Directory Structure
Directory structure:
└── github_repos/MikrotikBlockDangerAddresses/
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
    │   │       ├── pack-c226a93316abca0197662b6e8c84d10f295bcfbf.idx
    │   │       └── pack-c226a93316abca0197662b6e8c84d10f295bcfbf.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── danger.rsc
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
	url = https://github.com/drpioneer/MikrotikBlockDangerAddresses.git
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
0000000000000000000000000000000000000000 8719646c9550ac965cef8bd6c291d050ac088878 vivek-dodia <vivek.dodia@icloud.com> 1738605953 -0500	clone: from https://github.com/drpioneer/MikrotikBlockDangerAddresses.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 8719646c9550ac965cef8bd6c291d050ac088878 vivek-dodia <vivek.dodia@icloud.com> 1738605953 -0500	clone: from https://github.com/drpioneer/MikrotikBlockDangerAddresses.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 8719646c9550ac965cef8bd6c291d050ac088878 vivek-dodia <vivek.dodia@icloud.com> 1738605953 -0500	clone: from https://github.com/drpioneer/MikrotikBlockDangerAddresses.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8719646c9550ac965cef8bd6c291d050ac088878 refs/remotes/origin/master
236fed090e7928bb87cdb29aa61787a9e65ea843 refs/tags/v1.0.0
^cc9763bc431a390928d1c0531907777602144a36


File: /.git\refs\heads\master
8719646c9550ac965cef8bd6c291d050ac088878


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /danger.rsc
# Script for searching and blocking dangerous IPv4 addresses
# Script uses ideas by podarok66 evgeniy.demin Virtue tgrba denismikh MMAXSIM andrey-d GregoryGost Chupakabra303 Jotne rextended drPioneer
# https://github.com/drpioneer/MikrotikBlockDangerAddresses/blob/master/danger.rsc
# https://forummikrotik.ru/viewtopic.php?p=70410#p70410
# tested on ROS 6.49.17 & 7.16
# updated 2024/11/01

:global scriptBlckr; # flag of the running script (false=>in progress / true=>idle)
:global timeBlckr;   # time of the last log check (in unix time)
:do {
  :local timeout "8h";  # timeout of blacklist ("1w" "2d" "3h" "4m" "5s" "0w0d8h0m0s" etc...)
  :local wanLst  "";    # name of external interface list ("internet" "WAN" or others=>manual input value; ""=>automatic value selection)
  :local fwUsag  false; # checking & installing firewall rules (false or true)
  :local xtreme  false; # setting log scan level (false=>usual option or true=>extremal option)
  :local logEnt  false; # maintaining log entries (false or true)
  :local stcAdr  false; # converting blacklist from dynamic to static (false or true)
  :local nameBL  "BlockDangerAddress"; # name of blacklist
  :local nameWL  "WhiteList";          # name of whitelist
  :local cmntBL  "dropping dangerous addresses"; # comment for blacklist rule
  :local cmntWL  "white list of IP-addresses";   # comment for whitelist rule
  :local debug   false; # debug mode (true=>is active or false=>is inactive)

  # time translation function to UNIX time # https://forum.mikrotik.com/viewtopic.php?t=75555#p994849
  :global T2UDNG do={ # $1-date/time in any format: "hh:mm:ss","mmm/dd hh:mm:ss","mmm/dd/yyyy hh:mm:ss","yyyy-mm-dd hh:mm:ss","mm-dd hh:mm:ss"
    :local dTime [:tostr $1]; :local yesterDay false; /system clock
    :local cYear [get date]; :if ($cYear~"....-..-..") do={:set $cYear [:pick $cYear 0 4]} else={:set $cYear [:pick $cYear 7 11]}
    :if ([:len $dTime]=10 or [:len $dTime]=11) do={:set $dTime "$dTime 00:00:00"}
    :if ([:len $dTime]=15) do={:set $dTime "$[:pick $dTime 0 6]/$cYear $[:pick $dTime 7 15]"}
    :if ([:len $dTime]=14) do={:set $dTime "$cYear-$[:pick $dTime 0 5] $[:pick $dTime 6 14]"}
    :if ([:len $dTime]=8) do={:if ([:totime $1]>[get time]) do={:set $yesterDay true}; :set $dTime "$[get date] $dTime"}
    :if ([:tostr $1]="") do={:set $dTime ("$[get date] $[get time]")}
    :local vDate [:pick $dTime 0 [:find $dTime " " -1]]; :local vTime [:pick $dTime ([:find $dTime " " -1]+1) [:len $dTime]]
    :local vGmt [get gmt-offset]; :if ($vGmt>0x7FFFFFFF) do={:set $vGmt ($vGmt-0x100000000)}; :if ($vGmt<0) do={:set $vGmt ($vGmt*-1)}
    :local arrMn [:toarray "0,0,31,59,90,120,151,181,212,243,273,304,334"]; :local vdOff [:toarray "0,4,5,7,8,10"]
    :local month [:tonum [:pick $vDate ($vdOff->2) ($vdOff->3)]]
    :if ($vDate~".../../....") do={
      :set $vdOff [:toarray "7,11,1,3,4,6"]
      :set $month ([:find "xxanebarprayunulugepctovecANEBARPRAYUNULUGEPCTOVEC" [:pick $vDate ($vdOff->2) ($vdOff->3)] -1]/2)
      :if ($month>12) do={:set $month ($month-12)}}
    :local year [:pick $vDate ($vdOff->0) ($vdOff->1)]
    :if ((($year-1968)%4)=0) do={:set ($arrMn->1) -1; :set ($arrMn->2) 30}
    :local toTd ((($year-1970)*365)+(($year-1968)>>2)+($arrMn->$month)+([:pick $vDate ($vdOff->4) ($vdOff->5)]-1))
    :if ($yesterDay) do={:set $toTd ($toTd-1)};   # bypassing ROS6.xx time format problem after 00:00:00
    :return (((((($toTd*24)+[:pick $vTime 0 2])*60)+[:pick $vTime 3 5])*60)+[:pick $vTime 6 8]-$vGmt)}

  # time conversion function from UNIX time # https://forum.mikrotik.com/viewtopic.php?p=977170#p977170
  :global U2TDNG do={ # $1-UnixTime $2-OnlyTime
    :local ZeroFill do={:return [:pick (100+$1) 1 3]}
    :local prMntDays [:toarray "0,0,31,59,90,120,151,181,212,243,273,304,334"]
    :local vGmt [:tonum [/system clock get gmt-offset]]
    :if ($vGmt>0x7FFFFFFF) do={:set $vGmt ($vGmt-0x100000000)}
    :if ($vGmt<0) do={:set $vGmt ($vGmt*-1)}
    :local tzEpoch ($vGmt+[:tonum $1])
    :if ($tzEpoch<0) do={:set $tzEpoch 0}; # unsupported negative unix epoch
    :local yearStamp (1970+($tzEpoch/31536000))
    :local tmpLeap (($yearStamp-1968)>>2)
    :if ((($yearStamp-1968)%4)=0) do={:set ($prMntDays->1) -1; :set ($prMntDays->2) 30}
    :local tmpSec ($tzEpoch%31536000)
    :local tmpDays (($tmpSec/86400)-$tmpLeap)
    :if ($tmpSec<(86400*$tmpLeap) && (($yearStamp-1968)%4)=0) do={
      :set $tmpLeap ($tmpLeap-1); :set ($prMntDays->1) 0; :set ($prMntDays->2) 31; :set $tmpDays ($tmpDays+1)}
    :if ($tmpSec<(86400*$tmpLeap)) do={:set $yearStamp ($yearStamp-1); :set $tmpDays ($tmpDays+365)}
    :local mnthStamp 12; :while (($prMntDays->$mnthStamp)>$tmpDays) do={:set $mnthStamp ($mnthStamp-1)}
    :local dayStamp [$ZeroFill (($tmpDays+1)-($prMntDays->$mnthStamp))]
    :local timeStamp (00:00:00+[:totime ($tmpSec%86400)])
    :if ([:len $2]=0) do={:return "$yearStamp/$[$ZeroFill $mnthStamp]/$[$ZeroFill $dayStamp] $timeStamp"} else={:return "$timeStamp"}}

  # search of interface-list gateway
  :local GwFinder do={ # no input parameters
    :local routeISP [/ip route find dst-address=0.0.0.0/0 active=yes]; :if ([:len $routeISP]=0) do={:return ""}
    :set $routeISP "/ip route get $routeISP"
    :local routeGW {"[$routeISP vrf-interface]";"[$routeISP immediate-gw]";"[$routeISP gateway-status]"}
    /interface
    :foreach ifLstMmb in=[list member find] do={
      :local ifIfac [list member get $ifLstMmb interface]; :local ifList [list member get $ifLstMmb list]
      :local brName ""; :do {:set $brName [bridge port get [find interface=$ifIfac] bridge]} on-error={}
      :foreach answer in=$routeGW do={
        :local gw ""; :do {:set $gw [:tostr [[:parse $answer]]]} on-error={}
        :if ([:len $gw]>0 && $gw~$ifIfac or [:len $brName]>0 && $gw~$brName) do={:return $ifList}}}
    :return ""}

  # checking & installing optional firewall rules
  :local ChkFWRul do={ # $1-FWusage $2-wanLst $3-nameBL $4-nameWL $5-cmntRuleBL $6-cmntRuleWL $7-timeout

    # string parsing function 
    :local StrParser do={ # $1-string $2-desired parameter $3-separator
      :if ([:len [:find $1 $2 -1]]=0) do={:return ""}
      :local bgn ([:find $1 $2 -1]+[:len $2] +1); :local end [:find $1 "\"" $bgn]
      :if ([:len $3]!=0) do={
        :if ([:len [:find $1 $3 $bgn]]=0) do={:set $end [:find $1 "\"" $bgn]} else={:set $end [:find $1 $3 $bgn]}}
      :if ($end<$bgn) do={:set $end ($bgn+1)}
      :return [:pick $1 $bgn $end]}

    :global T2UDNG; :global U2TDNG
    :if ($1) do={
      /; /ip firewall layer7-protocol; find; :local cmnt ""
      :local fwL7prt [:toarray {
        "name=CVE-2023-28771 comment=\"IPsec payload missing: SA\" regexp=\";bash -c \\\"(curl|wget) (http:\\\\/\\\\/|)[0-9]+\\\\.[0-9]+\\\\.[0-9]+\\\\.[0-9]\""}]
      :foreach payLoad in=$fwL7prt do={
        :set $cmnt [$StrParser [:tostr $payLoad] "comment="]
        :if ([:len [/ip firewall layer7-protocol find comment=$cmnt]]=0) do={
          [:parse "/ip firewall layer7-protocol add $payLoad"]
          :put "$[$U2TDNG [$T2UDNG]]\tFirewall layer7 protocol with comment '$cmnt' not found.\r\n$[$U2TDNG [$T2UDNG]]\tAdded a regular expression"}}
      /; /ip firewall filter; find
      :local fwFltRul [:toarray {
        "action=accept chain=input comment=\"defconf: accept established,related,untracked\" connection-state=established,related,untracked";
        "action=drop chain=input comment=\"defconf: drop invalid\" connection-state=invalid";
        "action=accept chain=input comment=\"accept ICMP from external interface\" in-interface-list=$2 limit=50/5s,2:packet protocol=icmp";
        "action=accept chain=input comment=\"defconf: accept ICMP\" disabled=yes protocol=icmp";
        "action=accept chain=input comment=\"defconf: accept to local loopback (for CAPsMAN)\" dst-address=127.0.0.1";
        "action=accept chain=forward comment=\"defconf: accept in ipsec policy\" ipsec-policy=in,ipsec";
        "action=accept chain=forward comment=\"defconf: accept out ipsec policy\" ipsec-policy=out,ipsec";
        "action=fasttrack-connection chain=forward comment=\"defconf: fasttrack\" connection-state=established,related";
        "action=accept chain=forward comment=\"defconf: accept established,related, untracked\" connection-state=established,related,untracked";
        "action=drop chain=forward comment=\"defconf: drop invalid\" connection-state=invalid";
        "action=drop chain=forward comment=\"defconf: drop all from WAN not DSTNATed\" connection-nat-state=!dstnat connection-state=new in-interface-list=$2";
        "action=jump chain=input comment=\"packet analysis for attacks\" in-interface-list=$2 jump-target=TARPIT protocol=tcp src-address-list=$3";
        "action=tarpit chain=TARPIT comment=\"slow down attack to router\" limit=10,10:packet protocol=tcp";
        "action=drop chain=TARPIT comment=\"drop rest of TCP attack\" protocol=tcp";
        "action=drop chain=input comment=\"drop CVE-2023-28771\" connection-state=\"\" dst-port=500 in-interface-list=$2 layer7-protocol=CVE-2023-28771 protocol=udp";
        "action=accept chain=input comment=\"allow DNS request\" in-interface-list=$2 protocol=udp src-port=53";
        "action=accept chain=input comment=\"accept L2TP/IPSec connections\" connection-state=\"\" dst-port=500,1701,4500 in-interface-list=$2 protocol=udp";
        "action=accept chain=input comment=\"accept IPSec-esp connections\" connection-state=\"\" in-interface-list=$2 protocol=ipsec-esp";
        "action=accept chain=input comment=\"accept IPSec-ah connections\" connection-state=\"\" in-interface-list=$2 protocol=ipsec-ah";
        "action=accept chain=input comment=\"accept SSTP connections\" dst-port=443 in-interface-list=$2 protocol=tcp";
        "action=accept chain=input comment=\"accept PPTP TCP connections\" connection-state=\"\" dst-port=1723 in-interface-list=$2 protocol=tcp";
        "action=accept chain=input comment=\"accept PPTP GRE connections\" connection-state=\"\" in-interface-list=$2 protocol=gre";
        "action=accept chain=input comment=\"accept OVPN connections\" connection-state=\"\" disabled=yes dst-port=1194 in-interface-list=$2 protocol=tcp";
        "action=accept chain=forward comment=\"accept SIP UDP packets\" disabled=yes dst-port=5060-5061,5160-5161,10000-20000 in-interface-list=$2 protocol=udp";
        "action=accept chain=forward comment=\"accept SIP TCP packets\" disabled=yes dst-port=5060-5061,5160-5161,10000-20000 in-interface-list=$2 protocol=tcp";
        "action=accept chain=input comment=\"accept to Minecraft server\" disabled=yes dst-port=25565-25566 in-interface-list=$2 protocol=tcp";
        "action=jump chain=input comment=\"brute force protection on specified ports\" connection-state=new dst-port=8291 in-interface-list=$2 jump-target=BruteForce protocol=tcp";
        "action=return chain=BruteForce comment=\"packet analysis for brute force on the specified ports\" dst-limit=4/1m,1,src-address/1m40s";
        "action=add-src-to-address-list chain=BruteForce comment=\"add to BlackList attacker who used specified ports\" address-list=$3 address-list-timeout=$7";
        "action=accept chain=input comment=\"accept WinBox\" dst-port=8291 protocol=tcp in-interface-list=$2";
        "action=add-src-to-address-list chain=input comment=\"add to BlackList attacker who used unopened ports\" address-list=$3 address-list-timeout=$7 dst-address-type=!broadcast in-interface-list=$2";
        "action=drop chain=input comment=\"drop rest of packets\" in-interface-list=$2"}];
      :foreach payLoad in=$fwFltRul do={
        :set $cmnt [$StrParser [:tostr $payLoad] "comment="]
        :if ([:len [/ip firewall filter find comment=$cmnt]]=0) do={
          [:parse "/ip firewall filter add $payLoad"]
          :put "$[$U2TDNG [$T2UDNG]]\tFirewall filter rule with comment '$cmnt' not found, added a rule"}}
      /; /ip firewall raw; find
      :local fwRawRul [:toarray {
        "action=drop chain=prerouting comment=\"drop DNS parasit traffic\" dst-port=53 protocol=udp in-interface-list=$2"}]
      :foreach payLoad in=$fwRawRul do={
        :set $cmnt [$StrParser [:tostr $payLoad] "comment="]
        :if ([:len [/ip firewall raw find comment=$cmnt]]=0) do={
          [:parse "/ip firewall raw add $payLoad"]
          :put "$[$U2TDNG [$T2UDNG]]\tFirewall raw rule with comment '$cmnt' not found, added a rule"}}; /
    } else={
      :put "$[$U2TDNG [$T2UDNG]]\tATTENTION!!! Firewall rule checking is DISABLED (fwUsag  false)"
      :put "$[$U2TDNG [$T2UDNG]]\tRecommended to ENABLE (fwUsag  true)"}

    # checking & installing mandatory firewall rules
    :if ([/ip firewall address-list find list=$4]="") do={/ip firewall address-list add address="input_your_address" list=$4}
    /; /ip firewall filter; :local ruleID ""; :local fwFlt [find]
    :if ([:len $fwFlt]=0) do={
      add chain=input comment=$6 src-address-list=$4 disabled=no
    } else={
      :if ([find src-address-list=$4]="") do={
        :if ([find action~"passthrough" dynamic=yes]="") do={
          add chain=input comment=$6 src-address-list=$4 disabled=no place-before=($fwFlt->0)
        } else={
          :set $ruleID [$StrParser [:tostr [get [find action~"passthrough" dynamic=yes]]] ".nextid" ";"]
          :if ($ruleID!="") do={add chain=input comment=$6 src-address-list=$4 disabled=no place-before=$ruleID}}}}
    :if ([find src-address-list=$4 disabled=yes]!="") do={enable [find src-address-list=$4 disabled=yes]}
    /; /ip firewall raw; :local fwRaw [find]
    :if ([:len $fwRaw]=0) do={
      add action=accept chain=prerouting comment=$6 src-address-list=$4 disabled=no
    } else={
      :if ([find src-address-list=$4]="") do={
        :if ([find action~"passthrough" dynamic=yes]="") do={
          add action=accept chain=prerouting comment=$6 src-address-list=$4 disabled=no place-before=($fwRaw->0)
        } else={
          :set $ruleID [$StrParser [:tostr [get [find action~"passthrough" dynamic=yes]]] ".nextid" ";"]
          :if ($ruleID!="") do={add action=accept chain=prerouting comment=$6 src-address-list=$4 disabled=no place-before=$ruleID}}}}
    :if ([find src-address-list=$4 disabled=yes]!="") do={enable [find src-address-list=$4 disabled=yes]}
    :if ([find src-address-list=$3]="") do={add action=drop chain=prerouting comment=$5 src-address-list=$3 in-interface-list=$2 protocol=!tcp disabled=yes}
    :if ([find src-address-list=$3 disabled=yes]!="") do={
      :put "$[$U2TDNG [$T2UDNG]]\tATTENTION!!! RAW-rule for blocking dangerous IPv4 addresses is DISABLED"
      :put "$[$U2TDNG [$T2UDNG]]\tCheck rule properties in 'IP-Firewall-Raw'"
      /log warning "ATTENTION!!! Rule for blocking dangerous IPv4 addresses is DISABLED"
      /log warning "Check rule properties in 'IP-Firewall-Raw'"}; /}

  # device log analysis
  :local Analysis do={ # $1-NameBL $2-TimeoutBL $3-LogEntry $4-ExtremeScan $5-Debug

    # dangerous IPv4 addresses finder in log
    :local IpFinder do={ # $1-PrevStr $2-CurrStr $3-NextStr $4-BeginPtrn $5-EndPtrn $6-NameAttack $7-NameBL $8-TimeoutBL $9-LogEntry $10-Debug

      # checking correctness IPv4 address & blacklisting it
      :local IpCheck do={ # $1-IPaddr $2-NameBL $3-TimeoutBL $4-LogEntry $5-NameAttack $6-Debug
        :global T2UDNG; :global U2TDNG; :global numDNG
        :if ($1~"((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)[.]){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)") do={
          :if ($6) do={:put ">IpCheck__ip:$1<"}
          :if ([/ip firewall address-list find address=$1 list=$2]="") do={
            :set $numDNG ($numDNG+1)
            /ip firewall address-list add address=$1 list=$2 timeout=$3
            :put "$[$U2TDNG [$T2UDNG]]\tAdded in BlackList IPv4: $1 ($5)"
            :if ($4) do={/log warning ">>> Added in BlackList IPv4: $1 ($5)"}
            :return true}}
        :return false}

      # correcting characters of IPv4 addr
      :local CorrectIpV4 do={
        :if ([:typeof $1]!="str" or [:len $1]=0) do={:return ""}
        :local sym "0123456789."; :local res ""
        :for i from=0 to=([:len $1]-1) do={:local chr [:pick $1 $i]; :if ([:find $sym $chr]>-1) do={:set $res ($res.$chr)}}
        :return [:toip $res]}

      :if ($10) do={:put ">>>IpFinder1__Prev:$1__Curr:$2__Next:$3__Begin:$4__End:$5<<<"}
      :local prevLen [:len $1]; :local currLen [:len $2]; :local nextLen [:len $3]; :local isDng false; # sign of detected danger
      :if ($currLen=0 or $prevLen!=0 && $nextLen!=0) do={:return $isDng}; # quick exit with incorrect input parameters
      /log
      :local arrPrevId ""; :if ($prevLen!=0) do={:set $arrPrevId [find message~$1]}
      :local arrCurrId ""; :if ($currLen!=0) do={:set $arrCurrId [find message~$2]}
      :local arrNextId ""; :if ($nextLen!=0) do={:set $arrNextId [find message~$3]}
      :local lenPrevId [:len $arrPrevId]; :local lenCurrId [:len $arrCurrId]; :local lenNextId [:len $arrNextId]
      :if ($lenCurrId=0 or $prevLen!=0 && lenPrevId=0 or $nextLen!=0 && $lenNextId=0) do={:return $isDng}; # quick exit when specified string is not found
      :global timeBlckr; :global T2UDNG; :local bgnPtrn [:len $4]; :local endPtrn [:len $5]; :local dngIp ""; :local line 5
      :foreach currId in=$arrCurrId do={ # selecting current id string
        :local msg [/log get $currId message]; :local strLen [:len $msg]; :local tim [$T2UDNG [/log get $currId time]]
        :if ($tim>$timeBlckr && $strLen<200) do={ # filtering out old & very long strings
          :local currHexId ("0x".[:pick $currId ([:find $currId "*"] +1) [:len $currId]]); # hex id of current string
          :local findPrev false; :local findNext false; 
          :if ($lenPrevId>0) do={
            :foreach prevId in=$arrPrevId do={ # selecting previous id string
              :local prevHexId ("0x".[:pick $prevId ([:find $prevId "*"] +1) [:len $prevId]]); # hex id of previos string
              :local diff ($currHexId-$prevHexId); :if ($diff>0 && $diff<$line) do={:set $findPrev true}}}
          :if ($lenNextId>0) do={
            :foreach nextId in=$arrNextId do={ # selecting next id string
              :local nextHexId ("0x".[:pick $nextId ([:find $nextId "*"] +1) [:len $nextId]]); # hex id of next string
              :local diff ($nextHexId-$currHexId); :if ($diff>0 && $diff<$line) do={:set $findNext true}}}
          :if ($prevLen=0 && $lenCurrId!=0 && $nextLen=0 or $prevLen!=0 && $nextLen=0 && $findPrev or $prevLen=0 && $nextLen!=0 && $findNext) do={
            :if ($bgnPtrn!=0) do={:set $dngIp [:pick $msg ([:find $msg $4]+$bgnPtrn) $strLen]} else={:set $dngIp $msg}; # begin of dangerous IPv4 addr
            :if ($endPtrn!=0) do={:set $dngIp [:pick $dngIp 0 [:find $dngIp $5]]}; # end of dangerous ipAddr
            :set $dngIp [$CorrectIpV4 $dngIp]; # removing non-IPv4 characters
            :if ($10) do={:put ">>>IpFinder3__dngIp:$dngIp__findPrev:$findPrev__findNext:$findNext<<<"}
            :if ([$IpCheck $dngIp $7 $8 $9 $6 $10]) do={:set $isDng true}; # sending suspicious address to verification
          }}}
      :return $isDng}

    :if ($5) do={:put ">>>>Analysis__NameOfBL:$1__Timeout:$2__LogEntry:$3__ExtremeScan:$4<<<<<"}
    :local isDetected false; :local phraseBase {
      {name="login failure";prev="";curr="login failure for user";next="";bgn="from ";end=" via"};
      {name="denied connect";prev="";curr="denied winbox/dude connect from";next="";bgn="from ";end=""};
      {name="L2TP auth failed";prev="";curr="authentication failed";next="";bgn=" <";end=">"};
      {name="IPsec wrong passwd";prev="";curr="parsing packet failed, possible cause: wrong password";next="";bgn="";end=" parsing"};
      {name="IPSec failed proposal";prev="";curr="failed to pre-process ph1 packet";next="";bgn="";end=" failed"};
      {name="IPsec ph1 failed due to time up";prev="respond new phase 1 ";curr="phase1 negotiation failed due to time up";next="";bgn="<=>";end="["};
      {name="IKEv2 ident not found";prev="identity not found";curr="killing ike2 SA";next="";bgn="]-";end="["};
      {name="IKEv2 payload missing";prev="";curr="payload missing";next="";bgn="proto UDP, ";end=":"};
      {name="OVPN peer disconn";prev="TCP connection established from";curr="disconnected <peer disconnected>";next="";bgn="<";end=">:"};
      {name="OVPN unknown opcode";prev="unknown opcode received";curr="disconnected <bad packet received>";next="";bgn="<";end=">:"};
      {name="OVPN too short MSG";prev="msg too short";curr="TCP connection established from";next="";bgn="from ";end=""};
      {name="OVPN unknown MSG";prev="unknown msg";curr="TCP connection established from";next="";bgn="from ";end=""};
      {name="PPTP auth failed";prev="";curr="TCP connection established from";next="authentication failed";bgn="from ";end=""};
      {name="TCP conn establ";prev="";curr="TCP connection established from";next="";bgn="from ";end="";extr=true};
      {name="IPsec due to time up";prev="";curr="phase1 negotiation failed due to time up";next="";bgn="<=>";end="[";extr=true}}
    :foreach dangObj in=$phraseBase do={
      :if ([:len ($dangObj->"extr")]=0 or $4=($dangObj->"extr")) do={
        :if ([$IpFinder ($dangObj->"prev") ($dangObj->"curr") ($dangObj->"next") ($dangObj->"bgn") ($dangObj->"end") ($dangObj->"name") $1 $2 $3 $5]) do={:set isDetected true}}}
    :return $isDetected}

  # main body
  :global numDNG 0; :local startTime [$T2UDNG]; :local currTime [$U2TDNG $startTime];
  :put "$currTime\tStart of searching dangerous IPv4 addresses on '$[/system identity get name]' router"
  :if ([:len $scriptBlckr]=0) do={:set $scriptBlckr true}
  :if ($scriptBlckr) do={
    :set $scriptBlckr false; :set $timeout [:totime $timeout]
    :if ($debug) do={:put "$[$U2TDNG [$T2UDNG]]\tDebug mode is ENABLED"}
    :if ($xtreme) do={:put "$[$U2TDNG [$T2UDNG]]\tBE CAREFUL!!!!!! Extreme scanning mode is ENABLED!"}
    :if ($wanLst="") do={:set $wanLst [$GwFinder]; :put "$[$U2TDNG [$T2UDNG]]\tVariable 'wanLst' is empty -> so value '$wanLst' is automatically assigned"}
    :if ([:len [/interface list find name=$wanLst]]!=0) do={
      [$ChkFWRul $fwUsag $wanLst $nameBL $nameWL $cmntBL $cmntWL $timeout]
    } else={:put "$[$U2TDNG [$T2UDNG]]\tATTENTION!!! Not found list external interfaces named '$wanLst'."
      :put "$[$U2TDNG [$T2UDNG]]\tCheck it 'Interfaces-Interface List', firewall protection may not work!!!"}
    :if ($timeBlckr=0 or [:len $timeBlckr]=0) do={:put "$[$U2TDNG [$T2UDNG]]\tTime of the last log check was not found"; :set $timeBlckr 0
      } else={:put "$[$U2TDNG [$T2UDNG]]\tTime of the last log check $[$U2TDNG $timeBlckr]"}
    :if ([$Analysis $nameBL $timeout $logEnt $xtreme $debug]) do={
      :put "$[$U2TDNG [$T2UDNG]]\t$numDNG new dangerous IPv4 addresses were found"
    } else={:put "$[$U2TDNG [$T2UDNG]]\tNo new dangerous IPv4 addresses were found"}
    :set $timeBlckr $startTime
    :if ($stcAdr) do={
      /ip firewall address-list
      :foreach idx in=[find dynamic=yes list=$nameBL] do={
        :local ipaddress [get $idx address]; remove $idx; add list=$nameBL address=$ipaddress}}
    :set $currTime [$U2TDNG [$T2UDNG]]
    /system script environment remove [find name~"DNG"]
    :set $scriptBlckr true
  } else={:put "$currTime\tScript already being executed..."}
  :put "$currTime\tEnd of searching dangerous IPv4 addresses script"
} on-error={
  :set $scriptBlckr true
  :put "Script of blocking dangerous IPv4 addresses worked with errors"
  /system script environment remove [find name~"DNG"]
  /log warning "Script of blocking dangerous IPv4 addresses worked with errors"}
# finita la commedia


File: /README.md
# Cкрипт блокировки опасных IPv4 адресов, с которых пытались произвести подключение к роутеру.

Скрипт автоматически блокирует IPv4 адреса злоумышленников, прощупывающих маршрутизаторы Mikrotik из внешних сетей. Скрипт не имеет зависимостей от сторонних функций и скриптов. Настройка подразумевает правку значений локальных переменных в начале тела скрипта, краткое описание которых присутствует в комментариях. Тело скрипта необходимо закинуть в 'System/Scripts', запустить вручную из окна терминала командой '/system script run <имя скрипта>', ознакомиться с представленной информацией и при необходимости подправить рабочие настройки. Далее производится настройка запуска по расписанию из 'System/Scheduler' с необходимым периодом времени (типовое значение составляет единицы минут).

Работа скрипта сводится к формированию чёрного списка IPv4 адресов для их блокировки.
Формирование чёрного списка происходит двумя разными независимыми способами:
  1. на основе анализа записей журнала устройства
  2. при помощи преднастроенных правил Firewall

1й способ срабатывает каждый раз при запуске скрипта. При первом запуске проверяется весь журнал устройства, а при последующих запусках проверяется только непроверенная часть журнала. Так сделано для увеличения скорости последующих проверок журнала. 

2й способ изначально отключен, это сделано из соображения, что Firewall может быть уже настроен и вмешательство в его работу не желательно.
Активация 2го способа производится вручную, путём присвоения переменной 'fwUsag' значения 'true'.
После активации 2го способа скрипт настраивает Firewall по принципу: "запрещено всё, что не разрешено" и с этого момента, даже если скрипт не запущен, все попытки из вне прощупать роутер будут считаться несанкционированными.
Попутно, при задействовании 2го способа, при каждом запуске скрипт проверяет наличие преднастроенных правил Firewall и в случае их отсутствия производит установку недостающих. Поиск недостающих правил Firewall скрипт производит по комментариям в списках: 'Firewall/Filter Rules', 'Firewall/Raw', 'Firewall/Layer7 Protocols'. После установки правил Firewall пользователю необходимо расположить их вручную согласно своим предпочтениям. Для исключения неожиданной блокировки при установке новых правил, правила блокировки устанавливаются ОТКЛЮЧЕННЫМИ (!!!). Перемещение и активацию правил блокировки пользователь делает самостоятельно, вручную. Настройка правил FIREWALL производится в активном режиме 'Safe Mode' на случай неожиданной потери связи с роутером и для автоматического отката настроек в исходное состояние. По окончании настроек режим 'Safe Mode' необходимо деактивировать. Если правила блокировки оставить отключенными - скрипт будет об этом оповещать.

В итоге, все обращения к роутеру, не прошедшие проверку Firewall или отображённые в журнале устройства, как попытки несанкционированного доступа, попадают в черный список и блокируются на время, заданное в переменной 'timeout'. Типовое количество записей в чёрном списке при блокировке на 8 часов может составлять от нескольких сотен до нескольких тысяч (!!!) записей, и напрямую зависит от активности злоумышленников.

Обкатка скрипта проводилась на актуальных версиях RouterOS 6.49.++ и 7.16.++ .

Известные проблемы:
* работа скрипта может завершаться ошибкой, при включенном контроле правил Firewall и наличии в списке одинаковых правил с отличающимися комментариями.
* для предотвращения блокировки скриптом адресов, влияющих на работоспособность сетевого оборудования (DNS провайдера, адрес вышестоящего узла и т.п.), имеет смысл заранее внести их в белый список.

Ветка форума с обсуждением скрипта: https://forummikrotik.ru/viewtopic.php?t=11586

Используете скрипт - отметьте это звездочкой, Вам не сложно, а мне приятно!


