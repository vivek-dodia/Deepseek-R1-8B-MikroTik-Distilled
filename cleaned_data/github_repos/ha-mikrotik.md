# Repository Information
Name: ha-mikrotik

# Directory Structure
Directory structure:
└── github_repos/ha-mikrotik/
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
    │   │       ├── pack-32b2f570d1e5fc06a458bac484258ec9e376cba4.idx
    │   │       └── pack-32b2f570d1e5fc06a458bac484258ec9e376cba4.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── generate
    ├── HA_init.rsc
    ├── README.md
    ├── scripts/
    │   ├── ha_checkchanges.script
    │   ├── ha_config.script
    │   ├── ha_functions.script
    │   ├── ha_install.script
    │   ├── ha_loop_push_standby.script
    │   ├── ha_onbackup.script
    │   ├── ha_onmaster.script
    │   ├── ha_pushbackup.script
    │   ├── ha_report_startup.script
    │   ├── ha_setconfigver.script
    │   ├── ha_setidentity.script
    │   ├── ha_startup.script
    │   └── ha_switchrole.script
    ├── VERSION
    └── VERSION.checksum


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
	url = https://github.com/svlsResearch/ha-mikrotik.git
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
0000000000000000000000000000000000000000 0bd917e25139740c1d0654fb1a8d95c753a8f54c vivek-dodia <vivek.dodia@icloud.com> 1738605800 -0500	clone: from https://github.com/svlsResearch/ha-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 0bd917e25139740c1d0654fb1a8d95c753a8f54c vivek-dodia <vivek.dodia@icloud.com> 1738605800 -0500	clone: from https://github.com/svlsResearch/ha-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0bd917e25139740c1d0654fb1a8d95c753a8f54c vivek-dodia <vivek.dodia@icloud.com> 1738605800 -0500	clone: from https://github.com/svlsResearch/ha-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
657a0ac2f94edc56b5c2cc10091d7ef725474c40 refs/remotes/origin/bbs2webtest
c5e782ebc5c9ca2a14fa66e175f52cf17b89319b refs/remotes/origin/flashtest
0bd917e25139740c1d0654fb1a8d95c753a8f54c refs/remotes/origin/master
909c290212243a1a9ee2072cd5a9b954801b3b28 refs/remotes/origin/v7-test
df55fa366d7a5b31508877b5f78ed9c9f331a917 refs/tags/v0.6
3179e112b9fe94ad9755a2c6b1f6849c1cf20bc6 refs/tags/v0.6rc1
7a2f3e64495ca0c62e20d3ca8f8dc24a423e74a9 refs/tags/v6.39


File: /.git\refs\heads\master
0bd917e25139740c1d0654fb1a8d95c753a8f54c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /generate
#!/bin/bash
set -e -u
version="$(cat VERSION)"
code_checksum="$(cat scripts/*.script | openssl sha1 | awk '{print $2}')"
ha_version="$version - $code_checksum"
ha_password="$(egrep 'haMacA|haMacB' scripts/ha_config.script | awk '{print $3}' | cut -d '"' -f2 | openssl sha1 | awk '{print $2}')"
(
echo ":do {"
cd scripts
echo "/system script"
   for i in *.script; do
      script=$(echo "$i" | cut -d '.' -f1)
      echo "remove [find name=${script}_new]"
      echo -e -n "add name=${script}_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=\""
      cat "$i" | perl -p -e 's/\\/\\\\/g,s/\$/\\\$/g,s/\n/\\\n\t\\n/g,s/"/\\"/g'
      echo '"'
   done
   for i in *.script; do
      script=$(echo "$i" | cut -d '.' -f1)
      echo "remove [find name=${script}_old]"
      echo "remove [find name=${script}]"
      echo "set name=${script} [find name=${script}_new]"
   done
   echo "/system script run [find name=ha_functions]"
   echo "}"
) | sed "s/%%%HA_VERSION%%%/$ha_version/gi" | sed "s/%%%HA_PASSWORD%%%/$ha_password/gi" > HA_init.rsc
echo "Please upload HA_init.rsc to the master and run /import HA_init.rsc"
echo 'You can then do $HAInstall'


File: /HA_init.rsc
:do {
/system script
remove [find name=ha_checkchanges_new]
add name=ha_checkchanges_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":if ([:len [/system script job find where script=\"ha_checkchanges\"]] > 1) do={:error \"already running checkchanges\"; }\
	\n:global isMaster\
	\n:global isStandbyInSync\
	\n:global haPassword\
	\n:global haAddressOther\
	\n:global haCheckLastCheckTS  \"\$[/system clock get date] \$[/system clock get time] \$[/system clock get time-zone-name]\"\
	\n:global haCheckStandbyVer\
	\n:global haCheckMasterVer\
	\n:do {\
	\n   :if (\$isMaster) do={\
	\n      /file print file=HA_get-version.txt; /file set [find name=\"HA_get-version.txt\"] contents=\":global haConfigVer\\n[:put \\\"XXX \\\$haConfigVer YYYY\\\"]\\n\\n\\n\\n\"\
	\n         /tool fetch upload=yes src-path=HA_get-version.txt dst-path=HA_get-version.auto.rsc address=\$haAddressOther user=ha password=\$haPassword mode=ftp \
	\n         /file remove [find name=\"HA_standby-haConfigVer.txt\"]\
	\n         /tool fetch upload=no src-path=HA_get-version.auto.log dst-path=HA_standby-haConfigVer.txt address=\$haAddressOther user=ha password=\$haPassword mode=ftp \
	\n         :local haCheckStandbyVerTmp [/file get [find name=\"HA_standby-haConfigVer.txt\"] contents]\
	\n         :local xxxOffset [:find \$haCheckStandbyVerTmp \"XXX \"]\
	\n         :local yyyOffset [:find \$haCheckStandbyVerTmp \" YYYY\"]\
	\n         #Safety check that auto is running.\
	\n         #:put \$haCheckStandbyVerTmp\
	\n         :if (([:typeof \$xxxOffset] = \"nil\") || ([:typeof \$yyyOffset] = \"nil\")) do={\
	\n            :put \"ha_checkchanges: unable to find xxx/yyy! is auto working on this platform? xxxOffset: \$xxxOffset yyyOffset: \$yyyOffset\"\
	\n            :error \"ha_checkchanges: unable to find xxx/yyy! is auto working on this platform? xxxOffset: \$xxxOffset yyyOffset: \$yyyOffset \$haCheckStandbyVerTmp\"\
	\n         }\
	\n         :global haCheckStandbyVer [:pick \$haCheckStandbyVerTmp (\$xxxOffset+4) \$yyyOffset]\
	\n         :global haMasterConfigVer\
	\n         [/system script run [find name=\"ha_setconfigver\"]]\
	\n         :global haCheckMasterVer \$haMasterConfigVer\
	\n         /file remove [find name=\"HA_standby-haConfigVer.txt\"]\
	\n         :put \"MASTER VERSION: ! \$haCheckMasterVer !\"\
	\n         :put \"STANDB VERSION: ! \$haCheckStandbyVer !\"\
	\n         :if (\$haCheckStandbyVer != \$haCheckMasterVer) do={\
	\n            :put \"NEED TO PUSH\"\
	\n            :global isStandbyInSync false\
	\n            /system script run [find name=\"ha_pushbackup\"]\
	\n         } else={\
	\n            :global isStandbyInSync true\
	\n            :put \"GOOD\"\
	\n         }\
	\n   }\
	\n} on-error={\
	\n   :put \"GOT ERROR\"\
	\n   :global isStandbyInSync false\
	\n}\
	\n"
remove [find name=ha_config_new]
add name=ha_config_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source="/system script run [find name=\"ha_config_base\"]\
	\n:global haNetwork \"169.254.23.0\"\
	\n:global haNetmask \"255.255.255.0\"\
	\n:global haNetmaskBits \"24\"\
	\n:global haAddressA \"169.254.23.1\"\
	\n:global haAddressB \"169.254.23.2\"\
	\n:global haAddressVRRP \"169.254.23.10\"\
	\n"
remove [find name=ha_functions_new]
add name=ha_functions_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global HADebug do={\
	\n   :put \$1\
	\n   /log warning \$1\
	\n}\
	\n\
	\n:global HAPushStandby do={\
	\n   /system script run [find name=\"ha_pushbackup\"]\
	\n}\
	\n\
	\n:global HASyncStandby do={\
	\n   /system script run [find name=\"ha_checkchanges\"]\
	\n}\
	\n\
	\n:global HAInstall do={\
	\n   #\$HAInstall interface=\"ether8\" macA=\"E1:81:8C:35:13:8C\" macB=\"E1:81:8C:35:10:08\" password=\"a25d89ba41236c40726ff9e7ffee1d202992f61c\"\
	\n   :if ([:typeof \$interface] = \"nothing\") do={:error \"interface missing\"};\
	\n   :if ([:typeof \$macA] = \"nothing\") do={:error \"macA missing\"};\
	\n   :if ([:typeof \$macB] = \"nothing\") do={:error \"macB missing\"};\
	\n   :if ([:typeof \$password] = \"nothing\") do={:error \"password missing\"};\
	\n   /system script remove [find name=ha_config_base]\
	\n   /system script add name=ha_config_base owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=\":global haPassword \\\"\$password\\\"\\\
	\n   \\n:global haInterface \\\"\$interface\\\"\\\
	\n   \\n:global haMacA \\\"\$macA\\\"\\\
	\n   \\n:global haMacB \\\"\$macB\\\"\\\
	\n   \\n:global haPreferMac \\\"\\\"\"\
	\n   /system script run [find name=\"ha_install\"]\
	\n}\
	\n\
	\n:global HASwitchRole do={\
	\n   /system script run [find name=\"ha_switchrole\"]\
	\n}\
	\n\
	\n:global HALoopPushStandby do={\
	\n   /system script run [find name=\"ha_loop_push_standby\"]\
	\n}\
	\n"
remove [find name=ha_install_new]
add name=ha_install_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source="/system script run [find name=\"ha_config\"]\
	\n:global haPassword\
	\n:global haInterface\
	\n:global haMacA\
	\n:global haMacB\
	\n:global haNetmaskBits\
	\n:global haAddressOther\
	\n:global isMaster\
	\n:global haMacOther\
	\n\
	\n:if ([:len [/interface find where default-name=\"\$haInterface\" name=\"\$haInterface\"]] != 1) do={\
	\n   :error \"Unable to find interface named \$haInterface with default-name that matches name. Make sure you don't rename these interfaces, leave default-name as-is.\"\
	\n}\
	\n\
	\n:local mac [[/interface ethernet get [find default-name=\"\$haInterface\"] orig-mac-address]]\
	\n:if (\$mac != \$haMacA and \$mac != \$haMacB) do={\
	\n   :error \"Interface \$haInterface MAC \$mac does not match (A=\$haMacA or B=\$haMacB) - please check config\\r\\nUse orig-mac address!\"\
	\n}\
	\n\
	\n:local pingMac \$haMacA\
	\n:if (\$mac = \$haMacA) do={\
	\n   :set pingMac \$haMacB\
	\n}\
	\n\
	\n:put \$mac\
	\n:put \$pingMac\
	\n\
	\n:if ([/ping \$pingMac count=1] = 0) do={\
	\n   :error \"Are you sure the other device is configured properly? I am unable to ping MAC \$pingMac\"\
	\n}\
	\n\
	\n:if ([:len [/ip address find where interface=\"\$haInterface\" and comment!=\"HA_AUTO\"]] > 0) do={\
	\n   :error \"Interface \$haInterface has IP addresses. HA should completely own the interface and it cannot be used by anything else. Please correct\"\
	\n}\
	\n\
	\n:if ([:len [/file find name=HA_backup_beforeHA.backup]] = 0) do={\
	\n   system backup save name=HA_backup_beforeHA dont-encrypt=yes\
	\n   /export file=HA_backup_beforeHA.rsc\
	\n}\
	\n\
	\n:if (!\$isMaster) do={\
	\n   :put \"I am not master - running ha_startup first\"\
	\n   :global haAllowBootstrap\
	\n   :set haAllowBootstrap true\
	\n   /system script run \"ha_startup\"\
	\n} else={\
	\n   :put \"I am already master! Skipping my own bootstrap...\"\
	\n}\
	\n\
	\n:put \"###\"\
	\n:put \"#Maybe try: /tool mac-telnet \$haMacOther\"\
	\n:put \"###PASTE THIS ON THE OTHER DEVICE - YOUR CONFIG WILL BE RESET AND LOST!!!###\"\
	\n:put \":global mac [[/interface ethernet get [find default-name=\\\"\$haInterface\\\"] orig-mac-address]]\"\
	\n:put \":if (\\\$mac != \\\"\$haMacA\\\" and \\\$mac != \\\"\$haMacB\\\") do={\"\
	\n:put \"   :error \\\"Interface \$haInterface MAC \\\$mac does not match (A=\$haMacA or B=\$haMacB) - please check config\\\\r\\\\nUse orig-mac address!\\\"\"\
	\n:put \"}\"\
	\n#Try to backup the local device before HA, just in case.\
	\n:put \":if ([:len [/file find name=HA_backup_beforeHA.backup]] = 0) do={\"\
	\n:put \"   /system backup save name=HA_backup_beforeHA dont-encrypt=yes\"\
	\n:put \"   /export file=HA_backup_beforeHA.rsc\"\
	\n:put \"}\"\
	\n#Oh this is ridicullous, we can't create a file that doesn't end in .txt any other way. Use export to create a rsc file extension.\
	\n:put \"/export file=HA_bootstrap.rsc\"\
	\n#Seems to be a race condition between the export and the visibility, delay a bit.\
	\n:put \"/delay 2\"\
	\n:put \"/file print file=HA_bootstrap.rsc\"\
	\n#Need delays here similar to ha_startup, sometimes the interfaces arent ready when this runs.\
	\n:put \"/file set [find name=HA_bootstrap.rsc] contents=\\\":local haBootstrapOK false; :while (!\\\\\\\$haBootstrapOK) do={:do { /ip address add address=\\\\\\\"\$haAddressOther/\$haNetmaskBits\\\\\\\" interface=\$haInterface; /user add name=ha group=full password=\\\\\\\"\$haPassword\\\\\\\"; :set haBootstrapOK true;} on-error={/log warning \\\\\\\"ha_startup: 0.0 B bootstrap failed...waiting\\\\\\\"; :delay 5};}\\\"\"\
	\n:put \"/system reset-configuration no-defaults=yes keep-users=no skip-backup=yes run-after-reset=HA_bootstrap.rsc\"\
	\n:put \"###END OF PASTE FOR OTHER DEVICE###\"\
	\n:put \"###\"\
	\n"
remove [find name=ha_loop_push_standby_new]
add name=ha_loop_push_standby_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source="#Debugging stress test tool for new RouterOS testing\
	\n###Helper note for testing (disable automatic schedule, import, loop push):\
	\n# /system scheduler disable [find name=\"ha_checkchanges\"]; /system scheduler disable [find name=\"ha_auto_pushbackup\"]; \$HALoopPushStandby\
	\n###\
	\n:for pushCount from=1 to=10000 do={\
	\n   :put \"\$pushCount pushing\"\
	\n   /system script run [find name=\"ha_pushbackup\"]\
	\n   :put \"\$pushCount push done\"\
	\n   :delay 200\
	\n   /system script run [find name=\"ha_checkchanges\"]\
	\n   :put \"\$pushCount sync ok\"\
	\n   :delay 10\
	\n}\
	\n"
remove [find name=ha_onbackup_new]
add name=ha_onbackup_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global isMaster false\
	\n:global haNetmaskBits\
	\n:global haInterface\
	\n:execute \"/routing bgp peer disable [find]\"\
	\n:execute \"/interface bonding disable [find]\"\
	\n:execute \"/interface ethernet disable [find where default-name!=\\\"\$haInterface\\\" and comment!=\\\"HA_RESCUE\\\"]\"\
	\n:execute \"ha_setidentity\"\
	\n:do { :local k [/system script find name=\"on_backup\"]; if ([:len \$k] = 1) do={ /system script run \$k } } on-error={ :put \"on_backup failed\" }\
	\n"
remove [find name=ha_onmaster_new]
add name=ha_onmaster_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global isMaster true\
	\n:global haNetmaskBits\
	\n:global haInterface\
	\n:execute \"/interface ethernet enable [find]\"\
	\n:execute \"/interface bonding enable [find]\"\
	\n:execute \"/routing bgp peer enable [find]\"\
	\n:execute \"ha_setidentity\"\
	\n:do { :local k [/system script find name=\"on_master\"]; if ([:len \$k] = 1) do={ /system script run \$k } } on-error={ :put \"on_master failed\" }\
	\n"
remove [find name=ha_pushbackup_new]
add name=ha_pushbackup_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":if ([:len [/system script job find where script=\"ha_pushbackup\"]] > 1) do={:error \"already running pushbackup\"; }\
	\n:global haPassword\
	\n:global isMaster\
	\n:global haAddressOther\
	\n:if (!\$isMaster) do={\
	\n   :error \"NOT MASTER\"\
	\n} else={\
	\n   #Really? this is the only way to create directories?\
	\n   :local mkdirCode \":do { /ip smb shares add comment=HA_AUTO name=mkdir disabled=yes directory=/skins } on-error={}\"\
	\n\
	\n   :foreach k in=[/file find type=\"directory\"] do={\
	\n      :local xferfile [/file get \$k name]\
	\n      if ([:pick \"\$xferfile\" 0 3] != \"HA_\") do={\
	\n         :set mkdirCode \"\$mkdirCode\\r\\n/ip smb shares set [find comment=HA_AUTO] directory=\\\"\$xferfile\\\"\"\
	\n      }\
	\n   }\
	\n\
	\n   :set mkdirCode \"\$mkdirCode\\r\\n/ip smb shares remove [find comment=HA_AUTO]\\r\\n\"\
	\n   #eh - good chance to keep files in sync, just delete everything, we will reupload. is this going to reduce life of nvram?\
	\n   :local purgeFilesCode \":foreach k in=[/file find type!=\\\"directory\\\"] do={ :local xferfile [/file get \\\$k name]; if ([:pick \\\"\\\$xferfile\\\" 0 3] != \\\"HA_\\\") do={ :put \\\"removing \\\$xferfile\\\"; /file remove \\\$k; } }\"\
	\n   :set mkdirCode \"\$purgeFilesCode;\\r\\n/delay 2;\\r\\n\$mkdirCode\"\
	\n\
	\n   /file print file=HA_mkdirs.txt\
	\n   /file set [find name=\"HA_mkdirs.txt\"] contents=\$mkdirCode\
	\n   :put \"mkdirCode: \$mkdirCode end_mkDirCode\"\
	\n   /tool fetch upload=yes src-path=HA_mkdirs.txt dst-path=HA_mkdirs.auto.rsc address=\$haAddressOther user=ha password=\$haPassword mode=ftp \
	\n   \
	\n   :foreach k in=[/file find type!=\"directory\"] do={\
	\n      :local xferfile [/file get \$k name]\
	\n      if ([:pick \"\$xferfile\" 0 3] != \"HA_\") do={\
	\n         :put \"Transferring: \$xferfile\"\
	\n         :do {\
	\n            /tool fetch upload=yes src-path=\$xferfile dst-path=\$xferfile address=\$haAddressOther user=ha password=\$haPassword mode=ftp\
	\n         } on-error={\
	\n            :put \"Failed to transfer \$xferfile\"\
	\n         }\
	\n      }\
	\n   }\
	\n\
	\n   :if ([:len [/file find name=HA_dsa]] <= 0) do={ \
	\n      /ip ssh export-host-key key-file-prefix=\"HA\"\
	\n   }\
	\n\
	\n   /tool fetch upload=yes src-path=HA_dsa dst-path=HA_dsa address=\$haAddressOther user=ha password=\$haPassword mode=ftp  \
	\n   /tool fetch upload=yes src-path=HA_rsa dst-path=HA_rsa address=\$haAddressOther user=ha password=\$haPassword mode=ftp  \
	\n\
	\n\
	\n   :global haMasterConfigVer\
	\n   [/system script run [find name=\"ha_setconfigver\"]]\
	\n   /file print file=HA_run-after-hastartup.txt\
	\n   /file set [find name=HA_run-after-hastartup.txt] contents=\":global haConfigVer \\\"\$haMasterConfigVer\\\"\"\
	\n   /tool fetch upload=yes src-path=HA_run-after-hastartup.txt dst-path=HA_run-after-hastartup.rsc address=\$haAddressOther user=ha password=\$haPassword mode=ftp \
	\n\
	\n   /export file=HA_b2s.rsc\
	\n   /system backup save name=HA_b2s.backup password=p\
	\n   /tool fetch upload=yes src-path=HA_b2s.rsc dst-path=HA_b2s.rsc address=\$haAddressOther user=ha password=\$haPassword mode=ftp  \
	\n   /tool fetch upload=yes src-path=HA_b2s.backup dst-path=HA_b2s.backup address=\$haAddressOther user=ha password=\$haPassword mode=ftp  \
	\n   /file print file=HA_restore-backup.rsc; /file set [find name=\"HA_restore-backup.rsc.txt\"] contents=\"/system backup load name=HA_b2s.backup password=p\"\
	\n   :do {\
	\n      /tool fetch upload=yes src-path=HA_restore-backup.rsc.txt dst-path=HA_restore-backup.auto.rsc address=\$haAddressOther user=ha password=\$haPassword mode=ftp \
	\n   } on-error={\
	\n      :put \"OK - status failed is OK from last fetch, standby is rebooting.\"\
	\n   }\
	\n}\
	\n"
remove [find name=ha_report_startup_new]
add name=ha_report_startup_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source="#Attempt to kick the timing clients into a forced update so we get accurate timestamps to syslog on the report.\
	\n:do {/ip cloud force-update} on-error={};\
	\n:if ([/system ntp client get enabled]) do={\
	\n   /system ntp client set enabled=no\
	\n   :delay 16\
	\n   /system ntp client set enabled=yes\
	\n}\
	\n\
	\n:delay 65\
	\n\
	\n:local badCount [:len [/log find where message~\"ha_startup.*(FAILED)\"]]\
	\n:local goodCount [:len [/log find where message~\"ha_startup.*(DONE)\"]]\
	\n:local delay1Count [:len [/log find where message~\"ha_startup.*(delaying1)\"]]\
	\n:local delay2Count [:len [/log find where message~\"ha_startup.*(delaying2)\"]]\
	\n:local uptime [/system resource get uptime]\
	\n:local routerVersion [/system resource get version]\
	\n:local firmwareVersion [/system routerboard get current-firmware]\
	\n\
	\n:global isMaster\
	\n:global haStartupHasRun\
	\n:global haStartupHAVersion\
	\n:global haInitTries\
	\n:global haPreferMac\
	\n/log info \"ha_startup: ha_report_startup debug version=\$routerVersion firmware=\$firmwareVersion badC=\$badCount goodC=\$goodCount delay1C=\$delay1Count delay2C=\$delay2Count uptime=\$uptime isMaster=\$isMaster haPreferMac=\$haPreferMac haInitTries=\$haInitTries haStartupHasRun=\$haStartupHasRun haStartupHAVersion=\$haStartupHAVersion\"\
	\n:execute \"/log print\" file=\"HA_boot_log.txt\"\
	\n\
	\n#Debugging helper for spinning reboots of the standby - you probably don't want to mess with this.\
	\n:if (false) do={\
	\n   :if (\$isMaster) do={\
	\n      #Just because we are master doesnt mean we really are, we could have a failed startup but it is too risky to do anything else.\
	\n      :put \"I am master - do nothing\"\
	\n   } else={\
	\n      :if (\$goodCount = 1) do={\
	\n         :put \"REBOOT\"\
	\n         /system reboot\
	\n      } else={\
	\n         :put \"STAY\"\
	\n         #Disable all interfaces if they havent already, so the primary doesnt sneak in and we lose the failed state.\
	\n         /interface bonding disable [find]\
	\n         /interface ethernet disable [find]\
	\n      }\
	\n   }\
	\n}\
	\n"
remove [find name=ha_setconfigver_new]
add name=ha_setconfigver_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":local verHistory [:tostr [:pick [/system history print detail as-value] 1]]\
	\n:local verCertificate [:tostr [/certificate find]]\
	\n:local verFile [:tostr [/file find name~\"^[^H][^A][^_]\"]]\
	\n:local haVer \"history=\$verHistory file=\$verFile certificate=\$verCertificate\"\
	\n:global haMasterConfigVer \$haVer\
	\n"
remove [find name=ha_setidentity_new]
add name=ha_setidentity_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global haIdentity\
	\n:global isMaster\
	\n:local sysIdentity [/system identity get name]\
	\n:local haPos [:find \$sysIdentity \"_HA_\" 0]\
	\nif (\$haPos > 0) do={\
	\n   :set sysIdentity [:pick \$sysIdentity 0 \$haPos]\
	\n}\
	\n:if (\$isMaster) do={\
	\n   /system identity set name=\"\$sysIdentity_HA_\$haIdentity_ACTIVE\"\
	\n} else={\
	\n   /system identity set name=\"\$sysIdentity_HA_\$haIdentity_STANDBY\"\
	\n}\
	\n"
remove [find name=ha_startup_new]
add name=ha_startup_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source="#:do {\
	\n#Prevent double running of the startup. Is there a bug in the scheduler? It seems that sometimes our start-time=startup ha_startup\
	\n#fires again on newer versions of RouterOS.\
	\n:global haAllowBootstrap\
	\n:global haStartupHasRun\
	\n:global uptime [/system resource get uptime]\
	\n:if (!\$haAllowBootstrap && ([:typeof \$haStartupHasRun] != \"nothing\" || uptime > 2m)) do={\
	\n   /log warning \"ha_startup: ERROR ATTEMPTED TO RUN AGAIN!!! \$haStartupHasRun \$uptime\"\
	\n   :error \"ha_startup: ERROR ATTEMPTED TO RUN AGAIN!!! \$haStartupHasRun \$uptime\"\
	\n} else={\
	\n:set haStartupHasRun [/system resource get uptime]\
	\n:set haAllowBootstrap false\
	\n:execute \"/interface print detail\" file=\"HA_boot_interface_print.txt\"\
	\n/log warning \"ha_startup: START\"\
	\n/system script run [find name=ha_functions]\
	\n/log warning \"ha_startup: 0.1\"\
	\n/system script run [find name=\"ha_config\"]\
	\n/log warning \"ha_startup: 0.2\"\
	\n:global haInterface\
	\n#Sometimes the hardware isn't initialized by the time we get here. Wait until we can see the interface.\
	\n#https://github.com/svlsResearch/ha-mikrotik/issues/1\
	\n:while ([:len [/interface find default-name=\"\$haInterface\"]] != 1) do={\
	\n   /log error \"ha_startup: delaying1 for hardware...cant find \$haInterface\"\
	\n   #Avoid HA_VRRP becoming Master on CCR equipment during slow hardware initialization\
	\n   /interface vrrp disable [find where name=\"HA_VRRP\" and disabled=no]\
	\n   #Avoid bonding flapping on CCR equipment during slow hardware initialization\
	\n   /interface bonding disable [find disabled=no]\
	\n   :delay .05\
	\n}\
	\n/log warning \"ha_startup: 0.2b\"\
	\n#Disable HA_VRRP on startup to avoid this interface becoming master on slave device before \$haInterface\
	\n#has been initialized successfully\
	\n/interface vrrp disable [find where name=\"HA_VRRP\" and disabled=no]\
	\n#Disable bonding to avoid flapping during startup\
	\n/interface bonding disable [find disabled=no]\
	\n/log warning \"ha_startup: 0.3\"\
	\n#Finally take care about all ethernet interfaces\
	\n/interface ethernet disable [find disabled=no]\
	\n:global haStartupHAVersion \"0.7test15 - 7a36ae066ee95b1d83b75577f98bce7afb8fb40d\"\
	\n:global isStandbyInSync false\
	\n:global isMaster false\
	\n:global haPassword\
	\n:global haMacA\
	\n:global haMacB\
	\n:global haAddressA\
	\n:global haAddressB\
	\n:global haAddressVRRP\
	\n:global haNetmask\
	\n:global haNetmaskBits\
	\n:global haNetwork\
	\n:global haMacOther\
	\n:global haMacMe\
	\n:global haAddressOther\
	\n:global haAddressMe\
	\n:global haPreferMac\
	\n\
	\n/log warning \"ha_startup: version \$haStartupHAVersion\"\
	\n\
	\n/log warning \"ha_startup: 1 \$haInterface\"\
	\n/system scheduler remove [find comment=\"HA_AUTO\"]\
	\n\
	\n#Pause on-error just in case we error out before the spin loop - hope 5 seconds is enough.\
	\n/system scheduler add comment=HA_AUTO name=ha_startup on-event=\":do {:global haInterface; /system script run [find name=ha_startup]; } on-error={ :delay 5; /interface bonding disable [find disabled=no]; /interface ethernet disable [find where disabled=no and default-name!=\\\"\\\$haInterface\\\" and comment!=\\\"HA_RESCUE\\\"]; /log error \\\"ha_startup: FAILED - DISABLED ALL INTERFACES\\\" }\" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=startup\
	\n/system scheduler add comment=HA_AUTO name=ha_report_startup on-event=\"ha_report_startup\" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=startup\
	\n\
	\n/log warning \"ha_startup: 2\"\
	\n\
	\n#Spin this initialization code until we succeed. Sometimes RouterOS gives us an error when we try to find an interface\
	\n#that is in some sort of transient state, unclear why.\
	\n#https://github.com/svlsResearch/ha-mikrotik/issues/7\
	\n:global haTmpMac \"\"\
	\n:global haTmpInterfaceName \"\"\
	\n:global haTmpMaxInitTries 120\
	\n:global haInitTries 0\
	\n#Used to be backwards compatible with pre-bridge config.\
	\n:global haInterfaceLogical\
	\n:while (\$haTmpMac = \"\" && \$haInitTries <= \$haTmpMaxInitTries) do={\
	\n   :do {\
	\n      :set haInitTries (\$haInitTries+1)\
	\n      #Reset the MAC on the single HA interface - if they are connected via a switch, they need to be unique.\
	\n      /interface ethernet reset-mac-address [find default-name=\"\$haInterface\"]\
	\n      /ip address remove [find interface=\"\$haInterface\"]\
	\n      /ip address remove [find comment=\"HA_AUTO\"]\
	\n      /interface bridge port remove [find comment=\"HA_AUTO\"]\
	\n      /interface bridge remove [find comment=\"HA_AUTO\"]\
	\n      /interface vrrp remove [find name=\"HA_VRRP\"]\
	\n      /ip address remove [find interface=\"HA_VRRP\"]\
	\n      /ip firewall filter remove [find comment=\"HA_AUTO\"]\
	\n      /ip service set [find name=\"ftp\"] disabled=yes\
	\n      /interface ethernet enable [find where disabled=yes and default-name=\"\$haInterface\"]\
	\n      /interface ethernet enable [find where disabled=yes and comment=\"HA_RESCUE\"]\
	\n      /log warning \"ha_startup: 2.1 \$haInitTries\"\
	\n      /interface ethernet get [find default-name=\"\$haInterface\"] orig-mac-address\
	\n      /log warning \"ha_startup: 2.2 \$haInitTries\"\
	\n      :set haTmpMac [[/interface ethernet get [find default-name=\"\$haInterface\"] orig-mac-address]]\
	\n      :set haTmpInterfaceName [[/interface ethernet get [find default-name=\"\$haInterface\"] name]]\
	\n      /log warning \"ha_startup: 2.3\"\
	\n      /interface bridge add name=\"bridge-\$haInterface\" protocol-mode=none fast-forward=yes comment=\"HA_AUTO\"\
	\n      /interface bridge port add bridge=\"bridge-\$haInterface\" interface=\"\$haTmpInterfaceName\" comment=\"HA_AUTO\"\
	\n      :set haInterfaceLogical \"bridge-\$haInterface\"\
	\n      /log warning \"ha_startup: 3 \$haTmpMac \$haInitTries\"\
	\n   } on-error={\
	\n      /log error \"ha_startup: delaying2 for hardware...\$haInitTries\"\
	\n      :delay 1\
	\n   }\
	\n}\
	\n\
	\n/log warning \"ha_startup: 3.1 \$haTmpMac \$haInitTries\"\
	\n\
	\n:local mac \"\$haTmpMac\"\
	\n\
	\n:if (\"\$mac\" = \"\$haMacA\") do={\
	\n   :global haIdentity \"A\"\
	\n   /log warning \"I AM A\"\
	\n   /ip address add interface=\"bridge-\$haInterface\" address=\$haAddressA netmask=\$haNetmask comment=\"HA_AUTO\"\
	\n   :global haAddressMe \$haAddressA\
	\n   :global haAddressOther \$haAddressB\
	\n   :global haMacMe \$haMacA\
	\n   :global haMacOther \$haMacB\
	\n} else={\
	\n   :if (\"\$mac\" = \"\$haMacB\") do={\
	\n      :global haIdentity \"B\"\
	\n      /log warning \"I AM B\"\
	\n      /ip address add interface=\"bridge-\$haInterface\" address=\$haAddressB netmask=\$haNetmask comment=\"HA_AUTO\"\
	\n      :global haAddressMe \$haAddressB\
	\n      :global haAddressOther \$haAddressA\
	\n      :global haMacMe \$haMacB\
	\n      :global haMacOther \$haMacA\
	\n   } else={\
	\n      #This is a very strange bug...maybe just in the CCR? Sometimes when the unit comes up, ethernet interfaces sometimes have swapped positions?\
	\n      #A reboot clears this error - it is very odd, I don't know if it is a race condition in hardware initialization or something.\
	\n      #I'm not sure this covers ALL cases, since it only checks the MAC of the one interface our HA runs over. It might not right now :(\
	\n      #Do we need to track all MACs to make sure they are in the right order? This seems like a general problem with the platform but I don't understand the extent of it.\
	\n      #Am I causing this?\
	\n      :global haIdentity \"UKNOWN\"\
	\n      /log warning \"I AM UNKNOWN - WRONG MAC\"\
	\n      /delay 15\
	\n      :execute \"/system reboot\"\
	\n      /delay 1000\
	\n   }\
	\n}\
	\n\
	\n:local vrrpPriority 100\
	\n\
	\n:if (\"\$haMacMe\" = \"\$haPreferMac\") do={\
	\n   :set vrrpPriority 150\
	\n   /log warning \"ha_startup: 3.5 haPreferMac=\$haPreferMac is me! new vrrpPriority=\$vrrpPriority\"\
	\n}\
	\n\
	\n/ip route remove [find comment=\"HA_AUTO\"]\
	\n/ip route add gateway=\$haAddressOther distance=250 comment=HA_AUTO\
	\n\
	\n/log warning \"ha_startup: 4\"\
	\n\
	\n#If firewall is empty, place-before=0 won't work. Add first rule.\
	\n:if ([:len [/ip firewall filter find]] = 0) do={\
	\n   /log warning \"ha_startup: 4.1\"\
	\n   /ip firewall filter add chain=output action=accept out-interface=\"bridge-\$haInterface\" comment=\"HA_AUTO\"\
	\n   /ip firewall filter add chain=input action=accept in-interface=\"bridge-\$haInterface\" comment=\"HA_AUTO\"\
	\n} else={\
	\n   /log warning \"ha_startup: 4.2\"\
	\n   /ip firewall filter add chain=output action=accept out-interface=\"bridge-\$haInterface\" comment=\"HA_AUTO\" place-before=0\
	\n   /ip firewall filter add chain=input action=accept in-interface=\"bridge-\$haInterface\" comment=\"HA_AUTO\" place-before=0\
	\n}\
	\n/log warning \"ha_startup: 4.3\"\
	\n\
	\n/log warning \"ha_startup: 5\"\
	\n/interface vrrp add interface=\"bridge-\$haInterface\" version=3 interval=1 priority=\"\$vrrpPriority\" name=HA_VRRP on-backup=\"ha_onbackup\" on-master=\"ha_onmaster\" disabled=yes\
	\n/ip address add address=\$haAddressVRRP netmask=255.255.255.255 interface=HA_VRRP comment=\"HA_AUTO\"\
	\n\
	\n/log warning \"ha_startup: 6\"\
	\n/system scheduler add comment=HA_AUTO interval=10m name=ha_exportcurrent on-event=\"/export file=\\\"HA_current.rsc\\\"\" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=00:05:00\
	\n/system scheduler add interval=10m name=ha_checkchanges on-event=ha_checkchanges policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=00:10:00 comment=HA_AUTO\
	\n#Still need this - things like DHCP leases dont cause a system config change, we want to backup periodically.\
	\n/system scheduler add comment=HA_AUTO interval=24h name=ha_auto_pushbackup on-event=ha_pushbackup policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=05:00:00\
	\n/log warning \"ha_startup: 7\"\
	\n:if ([:len [/file find name=\"HA_dsa\"]] = 1) do={\
	\n   /ip ssh import-host-key private-key-file=HA_rsa\
	\n}\
	\n:if ([:len [/file find name=\"HA_rsa\"]] = 1) do={\
	\n   /ip ssh import-host-key private-key-file=HA_rsa\
	\n}\
	\n/user remove [find comment=HA_AUTO]\
	\n/user add address=\"\$haNetwork/\$haNetmaskBits\" comment=HA_AUTO group=full name=ha password=\"\$haPassword\"\
	\n/log warning \"ha_startup: 8\"\
	\n\
	\n#So you dont get annoyed with constant beeping - try catch because this may fail on some platforms (x86).\
	\n:do {/system routerboard settings set silent-boot=yes} on-error={};\
	\n\
	\n:foreach service in=[:toarray \"ftp\"] do={\
	\n   :local serviceAddresses \"\"\
	\n   :foreach k in=[/ip service get [find name=\$service] address] do={\
	\n      :if (\$k != \"\$haAddressA/32\" and \$k != \"\$haAddressB/32\" and \$k != \"\$haAddressVRRP/32\") do={\
	\n         :set serviceAddresses \"\$serviceAddresses,\$k\"\
	\n      }\
	\n   }\
	\n   :set serviceAddresses \"\$serviceAddresses,\$haAddressA,\$haAddressB,\$haAddressVRRP\"\
	\n   /ip service set [find name=\$service] address=[:toarray \$serviceAddresses]\
	\n}\
	\n\
	\n:if ([:len [/file find where name=\"HA_run-after-hastartup.rsc\"]] > 0) do={\
	\n   /import HA_run-after-hastartup.rsc\
	\n}\
	\n/delay 5\
	\n#We need FTP to do our HA work\
	\n/ip service set [find name=\"ftp\"] disabled=no\
	\n\
	\n/log warning \"ha_startup: 9\"\
	\n/interface vrrp set [find interface=\"bridge-\$haInterface\"] disabled=no\
	\n/log warning \"ha_startup: 9.1\"\
	\n\
	\n/log warning \"ha_startup: DONE\"\
	\n:put \"ha_startup: DONE\"\
	\n\
	\n#} on-error={\
	\n#   /log warning \"ha_startup: FAILED got error! disabling all interfaces!\"\
	\n#   /interface bonding disable [find]\
	\n#   /interface ethernet disable [find]\
	\n#}\
	\n\
	\n:do { :local k [/system script find name=\"on_startup\"]; if ([:len \$k] = 1) do={ /system script run \$k } } on-error={ :put \"on_startup failed\" }\
	\n}\
	\n"
remove [find name=ha_switchrole_new]
add name=ha_switchrole_new owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global isMaster\
	\n:global haAddressOther\
	\n:global haInterface\
	\n:global haInterfaceLogical\
	\n:global haPreferMac\
	\n\
	\n:local haPingInterface\
	\n:if ([:typeof \$haInterfaceLogical] = \"nothing\") do={\
	\n   :set haPingInterface \"\$haInterface\"\
	\n} else={\
	\n   :set haPingInterface \"\$haInterfaceLogical\"\
	\n}\
	\n\
	\n:put \"Using ping interface \$haPingInterface\"\
	\n\
	\n:if (([:typeof \$haPreferMac] != \"nothing\") && (\$haPreferMac != \"\")) do={\
	\n   :put \"You are using haPreferMac (\$haPreferMac) - switch role does not make sense.\"\
	\n   return 0\
	\n}\
	\n\
	\n:if (\$isMaster) do={\
	\n   :put \"I am master - switching role\"\
	\n   /system script run [find name=\"ha_pushbackup\"]\
	\n   :delay 5\
	\n   :local haWaitCount 0\
	\n   while ([/ping \$haAddressOther count=1 interface=\$haPingInterface ttl=1]  = 0) do={\
	\n      :set haWaitCount (\$haWaitCount+1)\
	\n      :put \"Still waiting for standby \$haWaitCount...\"\
	\n      :delay 1\
	\n   }\
	\n   :put \"Standby available \$haWaitCount...delaying 10s\"\
	\n   /delay 10\
	\n   :if (\$isMaster && [/ping \$haAddressOther count=1 interface=\$haPingInterface ttl=1]  >= 1) do={\
	\n      :put \"REBOOTING MYSELF\"\
	\n      :execute \"/system reboot\"\
	\n   } else={\
	\n      :put \"NOT REBOOTING MYSELF! SLAVE IS NOT UP OR I AM NOT MASTER!\"\
	\n   }\
	\n} else={\
	\n   :put \"I am NOT master - nothing to do\"\
	\n}\
	\n"
remove [find name=ha_checkchanges_old]
remove [find name=ha_checkchanges]
set name=ha_checkchanges [find name=ha_checkchanges_new]
remove [find name=ha_config_old]
remove [find name=ha_config]
set name=ha_config [find name=ha_config_new]
remove [find name=ha_functions_old]
remove [find name=ha_functions]
set name=ha_functions [find name=ha_functions_new]
remove [find name=ha_install_old]
remove [find name=ha_install]
set name=ha_install [find name=ha_install_new]
remove [find name=ha_loop_push_standby_old]
remove [find name=ha_loop_push_standby]
set name=ha_loop_push_standby [find name=ha_loop_push_standby_new]
remove [find name=ha_onbackup_old]
remove [find name=ha_onbackup]
set name=ha_onbackup [find name=ha_onbackup_new]
remove [find name=ha_onmaster_old]
remove [find name=ha_onmaster]
set name=ha_onmaster [find name=ha_onmaster_new]
remove [find name=ha_pushbackup_old]
remove [find name=ha_pushbackup]
set name=ha_pushbackup [find name=ha_pushbackup_new]
remove [find name=ha_report_startup_old]
remove [find name=ha_report_startup]
set name=ha_report_startup [find name=ha_report_startup_new]
remove [find name=ha_setconfigver_old]
remove [find name=ha_setconfigver]
set name=ha_setconfigver [find name=ha_setconfigver_new]
remove [find name=ha_setidentity_old]
remove [find name=ha_setidentity]
set name=ha_setidentity [find name=ha_setidentity_new]
remove [find name=ha_startup_old]
remove [find name=ha_startup]
set name=ha_startup [find name=ha_startup_new]
remove [find name=ha_switchrole_old]
remove [find name=ha_switchrole]
set name=ha_switchrole [find name=ha_switchrole_new]
/system script run [find name=ha_functions]
}


File: /README.md
# ha-mikrotik (Tested stable)
High availability code for Mikrotik routers

# Status: December 10th 2019
**RouterOS 6.44.6** is the only version that the author runs and tests with as of now. Anything newer is unknown and not recommended until tested extensively. Do not just upgrade RouterOS expecting it to work, Mikrotik has broken a series of features that ha-mikrotik relies on at various points in time. If you are not comfortable testing new versions that make break your entire setup, wait for the author or another party to confirm compatibility.

This has been tested stable across 6 different pairs of CCR1009s for over a year, there have been multiple adminstrative failover events and a few cases of hardware failovers. Please ensure you are using compatible hardware, RouterOS, and ha-mikrotik releases.

# Warning
Please do not test this on production routers. This should be tested in a lab setup with complete out of band serial access.
This was developed on the CCR1009-8g-1s-1s+ and is in use in our production environment. Proceed at your own risk, the code can potentionally wipe out 
all of your configuration and files on your device.

Extensive documentation is still needed. This is being delivered as a proof of concept.
You will need to do a bit of code reading and testing to figure out how it works.

# Issues
The #1 issue is a race condition during the startup of the secondary after it gets an updated configuration. It needs to quickly disable all of the interfaces
so that it doesn't end up taking traffic (MACs are cloned) from the active router. If you use spanning tree on your switches, it is likely that this
will happen fast enough and the Layer2/3 won't have time to come up and cause issues. Test this very carefully, you will get very strange results if your ports
start forwarding instantly from your upstream switch.

# Concept
Using a dedicated interface, VRRP, scripts, and backups, we can make a pair of Mikrotik routers highly available.
Configuration and files are actively synchronized to the standby and the standby remains ready to takeover when the VRRP heartbeat fails.

# Hardware originally developed for
Pair of CCR1009-8g-1s-1s+
RouterOS v6.33.5
Routerboard firmware 3.27
Bootstrapped from complete erased routers and then config built up once HA installed.

# Video demonstrating/explaining ha-mikrotik by The Network Berg
[MIkrotik - REAL HA Configuration](https://www.youtube.com/watch?v=GEef9P8wwxs)

# Installing
1. Source a pair of matching routers, ideally CCR1009-8g-1s-1s+.
2. Install RouterOS v6.44.6 and make sure the Routerboard firmware is up date.
3. Ensure you have serial connections to both devices.
4. Reset both routers using the command:
`/file remove [find]; /system reset-configuration keep-users=no no-defaults=yes skip-backup=yes`
5. Connect an ethernet cable between ether8 and ether8.
6. On one router, configure a basic network interface on ether1 with an IP address of your choosing. Just enough to be able to copy a file.
7. Upload HA_init.rsc and import it:
`/import HA_init.rsc`
8. Install HA (note to replace the fields of macA, macB, and password. I suggest a sha1 hex hash for the password.
`$HAInstall interface="ether8" macA="[MAC_OF_A_ETHER8]" macB="[MAC_OF_B_ETHER_8]" password="[A RANDOM PASSWORD OF YOUR CHOOSING]"`
9. Follow the instructions given by $HAInstall to bootstrap the secondary. I use the MAC telnet that is suggested at the top but any other method is sufficient.
10. Once router B is bootstrapped, it will reboot itself into a basic networking mode. It needs to be pushed the current configuration.
`$HASyncStandby`
11. B will now reboot and when it returns, it should be in standby mode. A should be the active router. You can now reboot A and B will takeover.

# Upgrading ha-mikrotik
1. Download a new release of ha-mikrotik
2. Upload HA_init.rsc to the active and import it:
`/import HA_init.rsc`
3. Run `$HAPushStandby` on the active, this should push the new code and reboot the standby.
4. Wait for the standby to come back, login and make sure everythig looks good. (/log print).
5. Run `$HASyncStandby` on the active, there should be no changes (unless something else changed on the active inbetween).
6. **THIS WILL REBOOT THE ACTIVE** Run `$HASwitchRole` on the active.
7. Your active is now the previous standby and both are upgraded once the standby boots.

# Rebuilding a hardware failed standby
Rebuilding failed hardware is similar to a new installation except that we don't need to reset both and don't need to bring in a new HA_init, assuming both RouterOS are compatible.

Install a compatible version of RouterOS on the new hardware and factory reset the configuration. Connect your new hardware the same exact way the old one was. We assume you have used the default of ether8 for the $haInterface.

**If A is active, run from A:**
1. `$HAInstall interface=$haInterface macA=$haMacMe macB="[NEW_MAC_OF_B_ETHER8]" password=$haPassword`
2. Follow on screen instructions just like original install.
3. Once the standby comes back, `$HASyncStandby`.
4. Done.

**If B is active, run from B:**
1. `$HAInstall interface=$haInterface macB=$haMacMe macA="[NEW_MAC_OF_A_ETHER8]" password=$haPassword`
2. Follow on screen instructions just like original install.
3. Once the standby comes back, `$HASyncStandby`.
4. Done.


File: /scripts\ha_checkchanges.script
:if ([:len [/system script job find where script="ha_checkchanges"]] > 1) do={:error "already running checkchanges"; }
:global isMaster
:global isStandbyInSync
:global haPassword
:global haAddressOther
:global haCheckLastCheckTS  "$[/system clock get date] $[/system clock get time] $[/system clock get time-zone-name]"
:global haCheckStandbyVer
:global haCheckMasterVer
:do {
   :if ($isMaster) do={
      /file print file=HA_get-version.txt; /file set [find name="HA_get-version.txt"] contents=":global haConfigVer\n[:put \"XXX \$haConfigVer YYYY\"]\n\n\n\n"
         /tool fetch upload=yes src-path=HA_get-version.txt dst-path=HA_get-version.auto.rsc address=$haAddressOther user=ha password=$haPassword mode=ftp 
         /file remove [find name="HA_standby-haConfigVer.txt"]
         /tool fetch upload=no src-path=HA_get-version.auto.log dst-path=HA_standby-haConfigVer.txt address=$haAddressOther user=ha password=$haPassword mode=ftp 
         :local haCheckStandbyVerTmp [/file get [find name="HA_standby-haConfigVer.txt"] contents]
         :local xxxOffset [:find $haCheckStandbyVerTmp "XXX "]
         :local yyyOffset [:find $haCheckStandbyVerTmp " YYYY"]
         #Safety check that auto is running.
         #:put $haCheckStandbyVerTmp
         :if (([:typeof $xxxOffset] = "nil") || ([:typeof $yyyOffset] = "nil")) do={
            :put "ha_checkchanges: unable to find xxx/yyy! is auto working on this platform? xxxOffset: $xxxOffset yyyOffset: $yyyOffset"
            :error "ha_checkchanges: unable to find xxx/yyy! is auto working on this platform? xxxOffset: $xxxOffset yyyOffset: $yyyOffset $haCheckStandbyVerTmp"
         }
         :global haCheckStandbyVer [:pick $haCheckStandbyVerTmp ($xxxOffset+4) $yyyOffset]
         :global haMasterConfigVer
         [/system script run [find name="ha_setconfigver"]]
         :global haCheckMasterVer $haMasterConfigVer
         /file remove [find name="HA_standby-haConfigVer.txt"]
         :put "MASTER VERSION: ! $haCheckMasterVer !"
         :put "STANDB VERSION: ! $haCheckStandbyVer !"
         :if ($haCheckStandbyVer != $haCheckMasterVer) do={
            :put "NEED TO PUSH"
            :global isStandbyInSync false
            /system script run [find name="ha_pushbackup"]
         } else={
            :global isStandbyInSync true
            :put "GOOD"
         }
   }
} on-error={
   :put "GOT ERROR"
   :global isStandbyInSync false
}


File: /scripts\ha_config.script
/system script run [find name="ha_config_base"]
:global haNetwork "169.254.23.0"
:global haNetmask "255.255.255.0"
:global haNetmaskBits "24"
:global haAddressA "169.254.23.1"
:global haAddressB "169.254.23.2"
:global haAddressVRRP "169.254.23.10"


File: /scripts\ha_functions.script
:global HADebug do={
   :put $1
   /log warning $1
}

:global HAPushStandby do={
   /system script run [find name="ha_pushbackup"]
}

:global HASyncStandby do={
   /system script run [find name="ha_checkchanges"]
}

:global HAInstall do={
   #$HAInstall interface="ether8" macA="E1:81:8C:35:13:8C" macB="E1:81:8C:35:10:08" password="a25d89ba41236c40726ff9e7ffee1d202992f61c"
   :if ([:typeof $interface] = "nothing") do={:error "interface missing"};
   :if ([:typeof $macA] = "nothing") do={:error "macA missing"};
   :if ([:typeof $macB] = "nothing") do={:error "macB missing"};
   :if ([:typeof $password] = "nothing") do={:error "password missing"};
   /system script remove [find name=ha_config_base]
   /system script add name=ha_config_base owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive source=":global haPassword \"$password\"\
   \n:global haInterface \"$interface\"\
   \n:global haMacA \"$macA\"\
   \n:global haMacB \"$macB\"\
   \n:global haPreferMac \"\""
   /system script run [find name="ha_install"]
}

:global HASwitchRole do={
   /system script run [find name="ha_switchrole"]
}

:global HALoopPushStandby do={
   /system script run [find name="ha_loop_push_standby"]
}


File: /scripts\ha_install.script
/system script run [find name="ha_config"]
:global haPassword
:global haInterface
:global haMacA
:global haMacB
:global haNetmaskBits
:global haAddressOther
:global isMaster
:global haMacOther

:if ([:len [/interface find where default-name="$haInterface" name="$haInterface"]] != 1) do={
   :error "Unable to find interface named $haInterface with default-name that matches name. Make sure you don't rename these interfaces, leave default-name as-is."
}

:local mac [[/interface ethernet get [find default-name="$haInterface"] orig-mac-address]]
:if ($mac != $haMacA and $mac != $haMacB) do={
   :error "Interface $haInterface MAC $mac does not match (A=$haMacA or B=$haMacB) - please check config\r\nUse orig-mac address!"
}

:local pingMac $haMacA
:if ($mac = $haMacA) do={
   :set pingMac $haMacB
}

:put $mac
:put $pingMac

:if ([/ping $pingMac count=1] = 0) do={
   :error "Are you sure the other device is configured properly? I am unable to ping MAC $pingMac"
}

:if ([:len [/ip address find where interface="$haInterface" and comment!="HA_AUTO"]] > 0) do={
   :error "Interface $haInterface has IP addresses. HA should completely own the interface and it cannot be used by anything else. Please correct"
}

:if ([:len [/file find name=HA_backup_beforeHA.backup]] = 0) do={
   system backup save name=HA_backup_beforeHA dont-encrypt=yes
   /export file=HA_backup_beforeHA.rsc
}

:if (!$isMaster) do={
   :put "I am not master - running ha_startup first"
   :global haAllowBootstrap
   :set haAllowBootstrap true
   /system script run "ha_startup"
} else={
   :put "I am already master! Skipping my own bootstrap..."
}

:put "###"
:put "#Maybe try: /tool mac-telnet $haMacOther"
:put "###PASTE THIS ON THE OTHER DEVICE - YOUR CONFIG WILL BE RESET AND LOST!!!###"
:put ":global mac [[/interface ethernet get [find default-name=\"$haInterface\"] orig-mac-address]]"
:put ":if (\$mac != \"$haMacA\" and \$mac != \"$haMacB\") do={"
:put "   :error \"Interface $haInterface MAC \$mac does not match (A=$haMacA or B=$haMacB) - please check config\\r\\nUse orig-mac address!\""
:put "}"
#Try to backup the local device before HA, just in case.
:put ":if ([:len [/file find name=HA_backup_beforeHA.backup]] = 0) do={"
:put "   /system backup save name=HA_backup_beforeHA dont-encrypt=yes"
:put "   /export file=HA_backup_beforeHA.rsc"
:put "}"
#Oh this is ridicullous, we can't create a file that doesn't end in .txt any other way. Use export to create a rsc file extension.
:put "/export file=HA_bootstrap.rsc"
#Seems to be a race condition between the export and the visibility, delay a bit.
:put "/delay 2"
:put "/file print file=HA_bootstrap.rsc"
#Need delays here similar to ha_startup, sometimes the interfaces arent ready when this runs.
:put "/file set [find name=HA_bootstrap.rsc] contents=\":local haBootstrapOK false; :while (!\\\$haBootstrapOK) do={:do { /ip address add address=\\\"$haAddressOther/$haNetmaskBits\\\" interface=$haInterface; /user add name=ha group=full password=\\\"$haPassword\\\"; :set haBootstrapOK true;} on-error={/log warning \\\"ha_startup: 0.0 B bootstrap failed...waiting\\\"; :delay 5};}\""
:put "/system reset-configuration no-defaults=yes keep-users=no skip-backup=yes run-after-reset=HA_bootstrap.rsc"
:put "###END OF PASTE FOR OTHER DEVICE###"
:put "###"


File: /scripts\ha_loop_push_standby.script
#Debugging stress test tool for new RouterOS testing
###Helper note for testing (disable automatic schedule, import, loop push):
# /system scheduler disable [find name="ha_checkchanges"]; /system scheduler disable [find name="ha_auto_pushbackup"]; $HALoopPushStandby
###
:for pushCount from=1 to=10000 do={
   :put "$pushCount pushing"
   /system script run [find name="ha_pushbackup"]
   :put "$pushCount push done"
   :delay 200
   /system script run [find name="ha_checkchanges"]
   :put "$pushCount sync ok"
   :delay 10
}


File: /scripts\ha_onbackup.script
:global isMaster false
:global haNetmaskBits
:global haInterface
:if ([:pick [/system resource get version] 0 ] = 6) do={
   :execute "/routing bgp peer disable [find]"
}
:if ([:pick [/system resource get version] 0 ] = 7) do={
   :execute "/routing bgp connection disable [find]"
}
:execute "/interface bonding disable [find]"
:execute "/interface ethernet disable [find where default-name!=\"$haInterface\" and comment!=\"HA_RESCUE\"]"
:execute "ha_setidentity"
:do { :local k [/system script find name="on_backup"]; if ([:len $k] = 1) do={ /system script run $k } } on-error={ :put "on_backup failed" }


File: /scripts\ha_onmaster.script
:global isMaster true
:global haNetmaskBits
:global haInterface
:execute "/interface ethernet enable [find]"
:execute "/interface bonding enable [find]"
:if ([:pick [/system resource get version] 0 ] = 6) do={
   :execute "/routing bgp peer enable [find]"
}
:if ([:pick [/system resource get version] 0 ] = 7) do={
   :execute "/routing bgp connection enable [find]"
}
:execute "ha_setidentity"
:do { :local k [/system script find name="on_master"]; if ([:len $k] = 1) do={ /system script run $k } } on-error={ :put "on_master failed" }


File: /scripts\ha_pushbackup.script
:if ([:len [/system script job find where script="ha_pushbackup"]] > 1) do={:error "already running pushbackup"; }
:global haPassword
:global isMaster
:global haAddressOther
:if (!$isMaster) do={
   :error "NOT MASTER"
} else={
   #Really? this is the only way to create directories?
   :local mkdirCode ":do { /ip smb shares add comment=HA_AUTO name=mkdir disabled=yes directory=/skins } on-error={}"

   :foreach k in=[/file find type="directory"] do={
      :local xferfile [/file get $k name]
      if ([:pick "$xferfile" 0 3] != "HA_") do={
         :set mkdirCode "$mkdirCode\r\n/ip smb shares set [find comment=HA_AUTO] directory=\"$xferfile\""
      }
   }

   :set mkdirCode "$mkdirCode\r\n/ip smb shares remove [find comment=HA_AUTO]\r\n"
   #eh - good chance to keep files in sync, just delete everything, we will reupload. is this going to reduce life of nvram?
   :local purgeFilesCode ":foreach k in=[/file find type!=\"directory\"] do={ :local xferfile [/file get \$k name]; if ([:pick \"\$xferfile\" 0 3] != \"HA_\") do={ :put \"removing \$xferfile\"; /file remove \$k; } }"
   :set mkdirCode "$purgeFilesCode;\r\n/delay 2;\r\n$mkdirCode"

   /file print file=HA_mkdirs.txt
   /file set [find name="HA_mkdirs.txt"] contents=$mkdirCode
   :put "mkdirCode: $mkdirCode end_mkDirCode"
   /tool fetch upload=yes src-path=HA_mkdirs.txt dst-path=HA_mkdirs.auto.rsc address=$haAddressOther user=ha password=$haPassword mode=ftp 
   
   :foreach k in=[/file find type!="directory"] do={
      :local xferfile [/file get $k name]
      if ([:pick "$xferfile" 0 3] != "HA_") do={
         :put "Transferring: $xferfile"
         :do {
            /tool fetch upload=yes src-path=$xferfile dst-path=$xferfile address=$haAddressOther user=ha password=$haPassword mode=ftp
         } on-error={
            :put "Failed to transfer $xferfile"
         }
      }
   }

   :if ([:len [/file find name=HA_dsa]] <= 0) do={ 
      /ip ssh export-host-key key-file-prefix="HA"
   }

:if ([:len [/file find name="HA_dsa"]] = 1) do={
   /tool fetch upload=yes src-path=HA_dsa dst-path=HA_dsa address=$haAddressOther user=ha password=$haPassword mode=ftp
}
:if ([:len [/file find name="HA_rsa"]] = 1) do={
   /tool fetch upload=yes src-path=HA_rsa dst-path=HA_rsa address=$haAddressOther user=ha password=$haPassword mode=ftp
}
# bugfix v7
:if ([:len [/file find name="HA_dsa.pem"]] = 1) do={
   /tool fetch upload=yes src-path=HA_dsa.pem dst-path=HA_dsa.pem address=$haAddressOther user=ha password=$haPassword mode=ftp
}
:if ([:len [/file find name="HA_rsa.pem"]] = 1) do={
   /tool fetch upload=yes src-path=HA_rsa.pem dst-path=HA_rsa.pem address=$haAddressOther user=ha password=$haPassword mode=ftp
}

   :global haMasterConfigVer
   [/system script run [find name="ha_setconfigver"]]
   /file print file=HA_run-after-hastartup.txt
   /file set [find name=HA_run-after-hastartup.txt] contents=":global haConfigVer \"$haMasterConfigVer\""
   /tool fetch upload=yes src-path=HA_run-after-hastartup.txt dst-path=HA_run-after-hastartup.rsc address=$haAddressOther user=ha password=$haPassword mode=ftp 

   /export file=HA_b2s.rsc
   /system backup save name=HA_b2s.backup password=p
   /tool fetch upload=yes src-path=HA_b2s.rsc dst-path=HA_b2s.rsc address=$haAddressOther user=ha password=$haPassword mode=ftp  
   /tool fetch upload=yes src-path=HA_b2s.backup dst-path=HA_b2s.backup address=$haAddressOther user=ha password=$haPassword mode=ftp  
   /file print file=HA_restore-backup.rsc; /file set [find name="HA_restore-backup.rsc.txt"] contents="/system backup load name=HA_b2s.backup password=p"
   :do {
      /tool fetch upload=yes src-path=HA_restore-backup.rsc.txt dst-path=HA_restore-backup.auto.rsc address=$haAddressOther user=ha password=$haPassword mode=ftp 
   } on-error={
      :put "OK - status failed is OK from last fetch, standby is rebooting."
   }
}


File: /scripts\ha_report_startup.script
#Attempt to kick the timing clients into a forced update so we get accurate timestamps to syslog on the report.
:do {/ip cloud force-update} on-error={};
:if ([/system ntp client get enabled]) do={
   /system ntp client set enabled=no
   :delay 16
   /system ntp client set enabled=yes
}

:delay 65

:local badCount [:len [/log find where message~"ha_startup.*(FAILED)"]]
:local goodCount [:len [/log find where message~"ha_startup.*(DONE)"]]
:local delay1Count [:len [/log find where message~"ha_startup.*(delaying1)"]]
:local delay2Count [:len [/log find where message~"ha_startup.*(delaying2)"]]
:local uptime [/system resource get uptime]
:local routerVersion [/system resource get version]
:local firmwareVersion [/system routerboard get current-firmware]

:global isMaster
:global haStartupHasRun
:global haStartupHAVersion
:global haInitTries
:global haPreferMac
/log info "ha_startup: ha_report_startup debug version=$routerVersion firmware=$firmwareVersion badC=$badCount goodC=$goodCount delay1C=$delay1Count delay2C=$delay2Count uptime=$uptime isMaster=$isMaster haPreferMac=$haPreferMac haInitTries=$haInitTries haStartupHasRun=$haStartupHasRun haStartupHAVersion=$haStartupHAVersion"
:execute "/log print" file="HA_boot_log.txt"

#Debugging helper for spinning reboots of the standby - you probably don't want to mess with this.
:if (false) do={
   :if ($isMaster) do={
      #Just because we are master doesnt mean we really are, we could have a failed startup but it is too risky to do anything else.
      :put "I am master - do nothing"
   } else={
      :if ($goodCount = 1) do={
         :put "REBOOT"
         /system reboot
      } else={
         :put "STAY"
         #Disable all interfaces if they havent already, so the primary doesnt sneak in and we lose the failed state.
         /interface bonding disable [find]
         /interface ethernet disable [find]
      }
   }
}


File: /scripts\ha_setconfigver.script
:local verHistory [:tostr [:pick [/system history print as-value] 1]]
:local verCertificate [:tostr [/certificate find]]
:local verFile [:tostr [/file find name~"^[^H][^A][^_]"]]
:local haVer "history=$verHistory file=$verFile certificate=$verCertificate"
:global haMasterConfigVer $haVer


File: /scripts\ha_setidentity.script
:global haIdentity
:global isMaster
:local sysIdentity [/system identity get name]
:local haPos [:find $sysIdentity "_HA_" 0]
if ($haPos > 0) do={
   :set sysIdentity [:pick $sysIdentity 0 $haPos]
}
:if ($isMaster) do={
   /system identity set name="$sysIdentity_HA_$haIdentity_ACTIVE"
} else={
   /system identity set name="$sysIdentity_HA_$haIdentity_STANDBY"
}


File: /scripts\ha_startup.script
#:do {
#Prevent double running of the startup. Is there a bug in the scheduler? It seems that sometimes our start-time=startup ha_startup
#fires again on newer versions of RouterOS.
:global haAllowBootstrap
:global haStartupHasRun
:global uptime [/system resource get uptime]
:if (!$haAllowBootstrap && ([:typeof $haStartupHasRun] != "nothing" || uptime > 2m)) do={
   /log warning "ha_startup: ERROR ATTEMPTED TO RUN AGAIN!!! $haStartupHasRun $uptime"
   :error "ha_startup: ERROR ATTEMPTED TO RUN AGAIN!!! $haStartupHasRun $uptime"
} else={
:set haStartupHasRun [/system resource get uptime]
:set haAllowBootstrap false
:execute "/interface print detail" file="HA_boot_interface_print.txt"
/log warning "ha_startup: START"
/system script run [find name=ha_functions]
/log warning "ha_startup: 0.1"
/system script run [find name="ha_config"]
/log warning "ha_startup: 0.2"
:global haInterface
#Sometimes the hardware isn't initialized by the time we get here. Wait until we can see the interface.
#https://github.com/svlsResearch/ha-mikrotik/issues/1
:while ([:len [/interface find default-name="$haInterface"]] != 1) do={
   /log error "ha_startup: delaying1 for hardware...cant find $haInterface"
   #Avoid HA_VRRP becoming Master on CCR equipment during slow hardware initialization
   /interface vrrp disable [find where name="HA_VRRP" and disabled=no]
   #Avoid bonding flapping on CCR equipment during slow hardware initialization
   /interface bonding disable [find disabled=no]
   :delay .05
}
/log warning "ha_startup: 0.2b"
#Disable HA_VRRP on startup to avoid this interface becoming master on slave device before $haInterface
#has been initialized successfully
/interface vrrp disable [find where name="HA_VRRP" and disabled=no]
#Disable bonding to avoid flapping during startup
/interface bonding disable [find disabled=no]
/log warning "ha_startup: 0.3"
#Finally take care about all ethernet interfaces
/interface ethernet disable [find disabled=no]
:global haStartupHAVersion "%%%HA_VERSION%%%"
:global isStandbyInSync false
:global isMaster false
:global haPassword
:global haMacA
:global haMacB
:global haAddressA
:global haAddressB
:global haAddressVRRP
:global haNetmask
:global haNetmaskBits
:global haNetwork
:global haMacOther
:global haMacMe
:global haAddressOther
:global haAddressMe
:global haPreferMac

/log warning "ha_startup: version $haStartupHAVersion"

/log warning "ha_startup: 1 $haInterface"
/system scheduler remove [find comment="HA_AUTO"]

#Pause on-error just in case we error out before the spin loop - hope 5 seconds is enough.
/system scheduler add comment=HA_AUTO name=ha_startup on-event=":do {:global haInterface; /system script run [find name=ha_startup]; } on-error={ :delay 5; /interface bonding disable [find disabled=no]; /interface ethernet disable [find where disabled=no and default-name!=\"\$haInterface\" and comment!=\"HA_RESCUE\"]; /log error \"ha_startup: FAILED - DISABLED ALL INTERFACES\" }" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=startup
/system scheduler add comment=HA_AUTO name=ha_report_startup on-event="ha_report_startup" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=startup

/log warning "ha_startup: 2"

#Spin this initialization code until we succeed. Sometimes RouterOS gives us an error when we try to find an interface
#that is in some sort of transient state, unclear why.
#https://github.com/svlsResearch/ha-mikrotik/issues/7
:global haTmpMac ""
:global haTmpInterfaceName ""
:global haTmpMaxInitTries 120
:global haInitTries 0
#Used to be backwards compatible with pre-bridge config.
:global haInterfaceLogical
:while ($haTmpMac = "" && $haInitTries <= $haTmpMaxInitTries) do={
   :do {
      :set haInitTries ($haInitTries+1)
      #Reset the MAC on the single HA interface - if they are connected via a switch, they need to be unique.
      /interface ethernet reset-mac-address [find default-name="$haInterface"]
      /ip address remove [find interface="$haInterface"]
      /ip address remove [find comment="HA_AUTO"]
      /interface bridge port remove [find comment="HA_AUTO"]
      /interface bridge remove [find comment="HA_AUTO"]
      /interface vrrp remove [find name="HA_VRRP"]
      /ip address remove [find interface="HA_VRRP"]
      /ip firewall filter remove [find comment="HA_AUTO"]
      /ip service set [find name="ftp"] disabled=yes
      /interface ethernet enable [find where disabled=yes and default-name="$haInterface"]
      /interface ethernet enable [find where disabled=yes and comment="HA_RESCUE"]
      /log warning "ha_startup: 2.1 $haInitTries"
      /interface ethernet get [find default-name="$haInterface"] orig-mac-address
      /log warning "ha_startup: 2.2 $haInitTries"
      :set haTmpMac [[/interface ethernet get [find default-name="$haInterface"] orig-mac-address]]
      :set haTmpInterfaceName [[/interface ethernet get [find default-name="$haInterface"] name]]
      /log warning "ha_startup: 2.3"
      /interface bridge add name="bridge-$haInterface" protocol-mode=none fast-forward=yes comment="HA_AUTO"
      /interface bridge port add bridge="bridge-$haInterface" interface="$haTmpInterfaceName" comment="HA_AUTO"
      :set haInterfaceLogical "bridge-$haInterface"
      /log warning "ha_startup: 3 $haTmpMac $haInitTries"
   } on-error={
      /log error "ha_startup: delaying2 for hardware...$haInitTries"
      :delay 1
   }
}

/log warning "ha_startup: 3.1 $haTmpMac $haInitTries"

:local mac "$haTmpMac"

:if ("$mac" = "$haMacA") do={
   :global haIdentity "A"
   /log warning "I AM A"
   /ip address add interface="bridge-$haInterface" address=$haAddressA netmask=$haNetmask comment="HA_AUTO"
   :global haAddressMe $haAddressA
   :global haAddressOther $haAddressB
   :global haMacMe $haMacA
   :global haMacOther $haMacB
} else={
   :if ("$mac" = "$haMacB") do={
      :global haIdentity "B"
      /log warning "I AM B"
      /ip address add interface="bridge-$haInterface" address=$haAddressB netmask=$haNetmask comment="HA_AUTO"
      :global haAddressMe $haAddressB
      :global haAddressOther $haAddressA
      :global haMacMe $haMacB
      :global haMacOther $haMacA
   } else={
      #This is a very strange bug...maybe just in the CCR? Sometimes when the unit comes up, ethernet interfaces sometimes have swapped positions?
      #A reboot clears this error - it is very odd, I don't know if it is a race condition in hardware initialization or something.
      #I'm not sure this covers ALL cases, since it only checks the MAC of the one interface our HA runs over. It might not right now :(
      #Do we need to track all MACs to make sure they are in the right order? This seems like a general problem with the platform but I don't understand the extent of it.
      #Am I causing this?
      :global haIdentity "UKNOWN"
      /log warning "I AM UNKNOWN - WRONG MAC"
      /delay 15
      :execute "/system reboot"
      /delay 1000
   }
}

:local vrrpPriority 100

:if ("$haMacMe" = "$haPreferMac") do={
   :set vrrpPriority 150
   /log warning "ha_startup: 3.5 haPreferMac=$haPreferMac is me! new vrrpPriority=$vrrpPriority"
}

/ip route remove [find comment="HA_AUTO"]
/ip route add gateway=$haAddressOther distance=250 comment=HA_AUTO

/log warning "ha_startup: 4"

#If firewall is empty, place-before=0 won't work. Add first rule.
:if ([:len [/ip firewall filter find]] = 0) do={
   /log warning "ha_startup: 4.1"
   /ip firewall filter add chain=output action=accept out-interface="bridge-$haInterface" comment="HA_AUTO"
   /ip firewall filter add chain=input action=accept in-interface="bridge-$haInterface" comment="HA_AUTO"
} else={
   /log warning "ha_startup: 4.2"
   /ip firewall filter add chain=output action=accept out-interface="bridge-$haInterface" comment="HA_AUTO" place-before=0
   /ip firewall filter add chain=input action=accept in-interface="bridge-$haInterface" comment="HA_AUTO" place-before=0
}
/log warning "ha_startup: 4.3"

/log warning "ha_startup: 5"
/interface vrrp add interface="bridge-$haInterface" version=3 interval=1 priority="$vrrpPriority" name=HA_VRRP on-backup="ha_onbackup" on-master="ha_onmaster" disabled=yes
/ip address add address=$haAddressVRRP netmask=255.255.255.255 interface=HA_VRRP comment="HA_AUTO"

/log warning "ha_startup: 6"
/system scheduler add comment=HA_AUTO interval=10m name=ha_exportcurrent on-event="/export file=\"HA_current.rsc\"" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=00:05:00
/system scheduler add interval=10m name=ha_checkchanges on-event=ha_checkchanges policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=00:10:00 comment=HA_AUTO
#Still need this - things like DHCP leases dont cause a system config change, we want to backup periodically.
/system scheduler add comment=HA_AUTO interval=24h name=ha_auto_pushbackup on-event=ha_pushbackup policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive start-date=Jan/01/1970 start-time=05:00:00
/log warning "ha_startup: 7"
:if ([:len [/file find name="HA_dsa"]] = 1) do={
   /ip ssh import-host-key private-key-file=HA_dsa
}
:if ([:len [/file find name="HA_rsa"]] = 1) do={
   /ip ssh import-host-key private-key-file=HA_rsa
}
# bugfix v7
:if ([:len [/file find name="HA_dsa.pem"]] = 1) do={
   /ip ssh import-host-key private-key-file=HA_dsa.pem
}
:if ([:len [/file find name="HA_rsa.pem"]] = 1) do={
   /ip ssh import-host-key private-key-file=HA_rsa.pem
}
/user remove [find comment=HA_AUTO]
/user add address="$haNetwork/$haNetmaskBits" comment=HA_AUTO group=full name=ha password="$haPassword"
/log warning "ha_startup: 8"

#So you dont get annoyed with constant beeping - try catch because this may fail on some platforms (x86).
:do {/system routerboard settings set silent-boot=yes} on-error={};

:foreach service in=[:toarray "ftp"] do={
   :local serviceAddresses ""
   :foreach k in=[/ip service get [find name=$service] address] do={
      :if ($k != "$haAddressA/32" and $k != "$haAddressB/32" and $k != "$haAddressVRRP/32") do={
         :set serviceAddresses "$serviceAddresses,$k"
      }
   }
   :set serviceAddresses "$serviceAddresses,$haAddressA,$haAddressB,$haAddressVRRP"
   /ip service set [find name=$service] address=[:toarray $serviceAddresses]
}

:if ([:len [/file find where name="HA_run-after-hastartup.rsc"]] > 0) do={
   /import HA_run-after-hastartup.rsc
}
/delay 5
#We need FTP to do our HA work
/ip service set [find name="ftp"] disabled=no

/log warning "ha_startup: 9"
/interface vrrp set [find interface="bridge-$haInterface"] disabled=no
/log warning "ha_startup: 9.1"

/log warning "ha_startup: DONE"
:put "ha_startup: DONE"

#} on-error={
#   /log warning "ha_startup: FAILED got error! disabling all interfaces!"
#   /interface bonding disable [find]
#   /interface ethernet disable [find]
#}

:do { :local k [/system script find name="on_startup"]; if ([:len $k] = 1) do={ /system script run $k } } on-error={ :put "on_startup failed" }
}


File: /scripts\ha_switchrole.script
:global isMaster
:global haAddressOther
:global haInterface
:global haInterfaceLogical
:global haPreferMac

:local haPingInterface
:if ([:typeof $haInterfaceLogical] = "nothing") do={
   :set haPingInterface "$haInterface"
} else={
   :set haPingInterface "$haInterfaceLogical"
}

:put "Using ping interface $haPingInterface"

:if (([:typeof $haPreferMac] != "nothing") && ($haPreferMac != "")) do={
   :put "You are using haPreferMac ($haPreferMac) - switch role does not make sense."
   return 0
}

:if ($isMaster) do={
   :put "I am master - switching role"
   /system script run [find name="ha_pushbackup"]
   :delay 5
   :local haWaitCount 0
   if ([:pick [/system resource get version] 0 ] = 6) do={
      while ([/ping $haAddressOther count=1 interface=$haPingInterface ttl=1] = 0) do={
         :set haWaitCount ($haWaitCount+1)
         :put "Still waiting for standby $haWaitCount..."
         :delay 1
      }
      :put "Standby available $haWaitCount...delaying 22s"
      /delay 22
      :if ($isMaster && [/ping $haAddressOther count=1 interface=$haPingInterface ttl=1] >= 1) do={
         :put "REBOOTING MYSELF"
         :execute "/system reboot"
      } else={
         :put "NOT REBOOTING MYSELF! SLAVE IS NOT UP OR I AM NOT MASTER!"
      }
   }
   if ([:pick [/system resource get version] 0 ] = 7) do={
      while (([/ping $haAddressOther count=1 interface=$haPingInterface ttl=1 as-value ]->"time") = nil ) do={
         :set haWaitCount ($haWaitCount+1)
         :put "Still waiting for standby $haWaitCount..."
         :delay 1
      }
      :put "Standby available $haWaitCount...delaying 22s"
      /delay 22
      :if ($isMaster && (([/ping $haAddressOther count=1 interface=$haPingInterface ttl=1 as-value ]->"time") > 0 ) ) do={
         :put "REBOOTING MYSELF"
         :execute "/system reboot"
      } else={
         :put "NOT REBOOTING MYSELF! SLAVE IS NOT UP OR I AM NOT MASTER!"
      }
   }
} else={
   :put "I am NOT master - nothing to do"
}


File: /VERSION
0.8dev20220621210200


File: /VERSION.checksum
0.7test15 - de3cd22b6c4882782ab0c7bf2903cdce9668264c


