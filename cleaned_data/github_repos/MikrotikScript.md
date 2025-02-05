# Repository Information
Name: MikrotikScript

# Directory Structure
Directory structure:
└── github_repos/MikrotikScript/
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
    │   │       ├── pack-9563fdd258e15c56fa1f9f9bda117aae5f1b446e.idx
    │   │       └── pack-9563fdd258e15c56fa1f9f9bda117aae5f1b446e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── LICENSE
    ├── messages/
    │   ├── 1.3.9.txt
    │   └── install.txt
    ├── MikrotikScript.tmLanguage
    ├── MikrotikScript.tmPreferences
    ├── MikrotikScript.YAML-tmLanguage
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
	url = https://github.com/Kentzo/MikrotikScript.git
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
0000000000000000000000000000000000000000 2eada48169771334a56c30c96fa2817d5afd672c vivek-dodia <vivek.dodia@icloud.com> 1738605809 -0500	clone: from https://github.com/Kentzo/MikrotikScript.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 2eada48169771334a56c30c96fa2817d5afd672c vivek-dodia <vivek.dodia@icloud.com> 1738605809 -0500	clone: from https://github.com/Kentzo/MikrotikScript.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 2eada48169771334a56c30c96fa2817d5afd672c vivek-dodia <vivek.dodia@icloud.com> 1738605809 -0500	clone: from https://github.com/Kentzo/MikrotikScript.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
2eada48169771334a56c30c96fa2817d5afd672c refs/remotes/origin/master
eafc6a58881c6c5656cbb9b8ab84675c498e6322 refs/tags/1.0.0
1a810bf110d3b1a4f338bcfea4124f42de82047d refs/tags/1.1.0
d15bb6f00529bae48b1bbd00bb526744ccd52d1a refs/tags/1.2.0
97a76de5016aa1c9a3b63811404fcb1ddca8cb9c refs/tags/1.3.0
a0fa1c4d91e641afbad607b92621fafad2e96e66 refs/tags/1.3.1
dae9af21eb9f7ae30b88b28f7f720efd54c7fd3a refs/tags/1.3.10
63dc9f4fdcae5b6dc221e02287b937f2d66493d9 refs/tags/1.3.11
3ceef385bb28cef6100c6ddfe09c3ccab7fbd07f refs/tags/1.3.2
08dacc8166e2e14cdf7f6e5184c294f4ca86ee83 refs/tags/1.3.3
a7eb991671aec1a5c0a686e9f90741cbdb104fde refs/tags/1.3.4
6b7881c5879f9df6651323c3e9f28abebd413906 refs/tags/1.3.5
8704dcd4fec73565fc6ffef45c08ecb80181e981 refs/tags/1.3.6
649b7a0e13abb9a94e7afba1562f257e90c553c8 refs/tags/1.3.7
58ec3d77463ac3584630189cf22596fed16db5c3 refs/tags/1.3.8
083001e8638156e5c124fa91d07f3e5866a0310c refs/tags/1.3.9


File: /.git\refs\heads\master
2eada48169771334a56c30c96fa2817d5afd672c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /LICENSE
The MIT License (MIT)

Copyright (c) 2014 Ilya Kulakov

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


File: /messages\1.3.9.txt
- Enable support for ST's Toggle Comment shortcut

File: /messages\install.txt
Thanks for installing. This package provides:

- Syntax highlighting for Mikrotik script
- Various static completions for common commands and parameters

File: /MikrotikScript.tmLanguage
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>fileTypes</key>
	<array>
		<string>rsc</string>
	</array>
	<key>name</key>
	<string>Mikrotik Script</string>
	<key>patterns</key>
	<array>
		<dict>
			<key>include</key>
			<string>#literal-string</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#comments</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#parameters-readwrite</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-constants</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-boolean</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-ip</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-mac</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-date</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#literal-number</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#variable</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#variable-definition</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#control-flow</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#commands</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#parameters-readonly</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#operators</string>
		</dict>
		<dict>
			<key>include</key>
			<string>#line-continuation</string>
		</dict>
	</array>
	<key>repository</key>
	<dict>
		<key>commands</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>match</key>
					<string>(?x) \b(?&lt;![\-=])( Neighbor| aaa| accept\-filter| access\-list| access| accounting| action| address\-list| address| add| advertise\-filter| advertisements| aggregate| alert| align| area| arp| bandwidth\-server| bandwidth\-test| beep| bfd| bgp\-vpls| bgp| binding| bonding| bridge| cache\-contents| cache| certificate| cisco\-bgp\-vpls| client| config| connect\-list| connections| connection| cookie| cpu| delay| detail| dhcp\-client| dhcp\-relay| dhcp\-server| direct| disable| discovery| dns\-update| e\-mail| edit| enable| environment| eoip| error| ethernet| export| fdb| fetch| file| filter| find| find| firewall| firmware| flush| get| gps| graphing| gre6| gre| group| host| hotspot| identity| inbox| info| inserts| installed\-sa| instance| interfaces| interface| interface| ip\-binding| ip\-scan| ipip| ipsec| ipv6| ip| ip| irq| keys| key| l2tp\-client| l2tp\-server| latency\-distribution| layer7\-protocol| lcd| ldp| lease| leds| len| logging| log| lookup| lsa| mac\-server| mac\-winbox| mangle| manual\-sa| manual\-tx\-power\-table| mesh| mirror| mme| mode\-cfg| monitor| mpls| nat| nbma\-neighbor| nd| neighbor| netwatch| network| note| nstreme\-dual| nstreme| ntp| option| originators| ospf\-router| ospf| ovpn\-client| ovpn\-server| packet\-generator| packet\-template| packet| parse| path\-state| pci| peer| pick| ping| policy| pool| port| ppp\-client| pppoe\-client| pppoe\-server| ppp| pptp\-client| pptp\-server| prefix\-list| prefix| print| profile| proposal| protocol| proxy| put| queue| range| raw| registration\-table| remote\-peers| remove| resolve| resource| resv\-state| rip| routerboard| route| routing| run| scan| scep| scheduler| script| security\-profiles| send| server| service| settings| set| set| sham\-link| shares| share| smb| sms| snapshot| sniffer| socks| sstp\-client| sstp\-server| statistics| stats| status| switch| system| target| terminal| time| toarray| tobool| toid| toip6| toip| tonum| tool| tostr| totime| typeof| tracking| traffic\-eng| traffic\-flow| traffic\-generator| traffic\-monitor| tunnel\-path| type| uncounted| upgrade| upnp| ups| usb| used| users| user| virtual\-link| vlan| vpls| vpnv4\-route| vrf| vrrp| walled\-garden| watchdog| wds| web\-access| wireless| return| caps\-man| console| disk| partitions| port| special\-login| radius| snmp| dude| agent| probe| device| ros| device\-type| service| notification| settings| simple| discovery\-settings| romon| service\-port )(?!-)\b
</string>
					<key>name</key>
					<string>support.function.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>comments</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.comment.mikrotik-script</string>
						</dict>
					</dict>
					<key>comment</key>
					<string>comments are ignored by syntax</string>
					<key>match</key>
					<string>(#).*$\n?</string>
					<key>name</key>
					<string>comment.line.number-sign.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>control-flow</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>keyword.control.flow.mikrotik-script</string>
						</dict>
						<key>2</key>
						<dict>
							<key>name</key>
							<string>invalid.illegal.whitespace.mikrotik-script</string>
						</dict>
						<key>3</key>
						<dict>
							<key>name</key>
							<string>keyword.operator.comparison.mikrotik-script</string>
						</dict>
					</dict>
					<key>match</key>
					<string>\b(from|to|step|in|do|else|while)\b([\s|\t]*)(=)</string>
				</dict>
				<dict>
					<key>match</key>
					<string>\b(while|for|foreach|on-error|if|do)\b</string>
					<key>name</key>
					<string>keyword.control.flow.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>line-continuation</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>punctuation.separator.continuation.line.mikrotik-script</string>
						</dict>
						<key>2</key>
						<dict>
							<key>name</key>
							<string>invalid.illegal.unexpected-text.mikrotik-script</string>
						</dict>
					</dict>
					<key>match</key>
					<string>(\\)(.*)$\n?</string>
				</dict>
			</array>
		</dict>
		<key>literal-boolean</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>boolean</string>
					<key>match</key>
					<string>\b(true|false)\b</string>
					<key>name</key>
					<string>constant.language.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>literal-date</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>1s, 2m, 3h, 4d</string>
					<key>match</key>
					<string>\b([1-9]+[0-9]*|0)(ms|s|m|h|d|w)\b</string>
					<key>name</key>
					<string>constant.other.time.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>1w5d12:20:59</string>
					<key>match</key>
					<string>\b(([1-9]+[0-9]*w)?([1-9]+[0-9]*d)?([0-9]{2}:[0-9]{2}:[0-9]{2}))\b</string>
					<key>name</key>
					<string>constant.other.time.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>\b((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\/[0-9]{2}\/[1-9]+[0-9]*)\b</string>
					<key>name</key>
					<string>constant.other.date.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>([\+\-]?[0-9]{2}:[0-9]{2})</string>
					<key>name</key>
					<string>constant.other.time.delta.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>literal-ip</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>IPv6 address, zero compressed IPv6 addresses, link-local IPv6 addresses with zone index, IPv4-Embedded IPv6 Address, IPv4-mapped IPv6 addresses, IPv4-translated addresses (http://stackoverflow.com/a/17871737/188530)</string>
					<key>match</key>
					<string>\b((\h{1,4}\:){7}\h{1,4}|(\h{1,4}\:){1,7}\:|(\h{1,4}\:){1,6}\:\h{1,4}|(\h{1,4}\:){1,5}(\:\h{1,4}){1,2}|(\h{1,4}\:){1,4}(\:\h{1,4}){1,3}|(\h{1,4}\:){1,3}(\:\h{1,4}){1,4}|(\h{1,4}\:){1,2}(\:\h{1,4}){1,5}|\h{1,4}\:((\:\h{1,4}){1,6})|\:((\:\h{1,4}){1,7}|\:)|fe80\:(\:\h{,4}){,4}\%[0-9a-zA-Z]{1,}|\:\:(ffff(\:0{1,4})?\:)?((25[0-5]|(2[0-4]|1?[0-9])?[0-9]).){3}(25[0-5]|(2[0-4]|1?[0-9])?[0-9])|(\h{1,4}\:){1,4}\:((25[0-5]|(2[0-4]|1?[0-9])?[0-9]).){3}(25[0-5]|(2[0-4]|1?[0-9])?[0-9]))\b</string>
					<key>name</key>
					<string>constant.other.ipv6.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>IPv4 address (http://stackoverflow.com/a/5284179/188530)</string>
					<key>match</key>
					<string>\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\/([0-9]|1[0-9]|2[0-4]))?\b</string>
					<key>name</key>
					<string>constant.other.ipv4.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>literal-mac</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>MAC address (http://stackoverflow.com/a/4260512/188530)</string>
					<key>match</key>
					<string>\b(\h{2}[:-]){5}(\h{2})\b</string>
					<key>name</key>
					<string>constant.other.mac.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>literal-number</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>64bit signed integer in hexadecimal form</string>
					<key>match</key>
					<string>\b(?i:(0x\h*))\b</string>
					<key>name</key>
					<string>constant.numeric.integer.hexadecimal.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>64bit signed integer in decimal form</string>
					<key>match</key>
					<string>\b([1-9]+[0-9]*|0)\b</string>
					<key>name</key>
					<string>constant.numeric.integer.decimal.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>literal-string</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>begin</key>
					<string>"</string>
					<key>beginCaptures</key>
					<dict>
						<key>0</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.string.begin.mikrotik-script</string>
						</dict>
					</dict>
					<key>end</key>
					<string>"</string>
					<key>endCaptures</key>
					<dict>
						<key>0</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.string.end.mikrotik-script</string>
						</dict>
					</dict>
					<key>name</key>
					<string>string.quoted.double.mikrotik-script</string>
					<key>patterns</key>
					<array>
						<dict>
							<key>include</key>
							<string>#string-escape</string>
						</dict>
						<dict>
							<key>include</key>
							<string>#string-expression</string>
						</dict>
						<dict>
							<key>include</key>
							<string>#line-continuation</string>
						</dict>
						<dict>
							<key>match</key>
							<string>\n</string>
							<key>name</key>
							<string>invalid.illegal.newline.mikrotik-script</string>
						</dict>
					</array>
				</dict>
			</array>
		</dict>
		<key>operators</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>comment</key>
					<string>arithmetic operators</string>
					<key>match</key>
					<string>\+|\-|\*|\/</string>
					<key>name</key>
					<string>keyword.operator.arithmetic.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>relational operators</string>
					<key>match</key>
					<string>&lt;|&gt;|&lt;=|&gt;=</string>
					<key>name</key>
					<string>keyword.operator.relational.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>comparison operators</string>
					<key>match</key>
					<string>=|!=</string>
					<key>name</key>
					<string>keyword.operator.comparison.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>logical operators</string>
					<key>match</key>
					<string>\!|&amp;&amp;|\|\|</string>
					<key>name</key>
					<string>keyword.operator.logical.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>bitwise operators</string>
					<key>match</key>
					<string>~|\||\^|\&amp;|&lt;&lt;|&gt;&gt;</string>
					<key>name</key>
					<string>keyword.operator.bitwise.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>concatenation operators</string>
					<key>match</key>
					<string>\.|\,</string>
					<key>name</key>
					<string>keyword.operator.concatenation.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>access array element by key</string>
					<key>match</key>
					<string>-&gt;</string>
					<key>name</key>
					<string>keyword.operator.other.mikrotik-script</string>
				</dict>
				<dict>
					<key>comment</key>
					<string>delimeters</string>
					<key>match</key>
					<string>:|\$|\/</string>
					<key>name</key>
					<string>keyword.operator.other.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>;</string>
					<key>name</key>
					<string>punctuation.terminator.statement.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>\(|\)</string>
					<key>name</key>
					<string>meta.brace.round.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>\{|\}</string>
					<key>name</key>
					<string>meta.brace.curly.mikrotik-script</string>
				</dict>
				<dict>
					<key>match</key>
					<string>\[|\]</string>
					<key>name</key>
					<string>meta.brace.square.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>parameters-readonly</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>match</key>
					<string>(?x) \b(?&lt;![\-=])( 802\.1x\-port\-enabled| ac\-mac| ack\-timeout| active\-address| active\-client\-id| active\-cpu| active\-interfaces| active\-links| active\-mac\-address| active\-server| actual\-interface| actual\-tx\-interval| addresses| adjacency| agent\-circuit\-id| agent\-remote\-id| aggregator| ap| architecture\-name| as\-path| as4\-capability| assured| atomic\-aggregate| authentication\-type| authority| backup\-dr\-address| bad\-blocks| bgp\-ext\-communities| bgp| blocked| board\-name| bytes\-in| bytes\-out| ca\-crl\-host| caller\-id| category| ca| checksum| cisco\-bgp\-signaled| client| cluster\-list| communities| cpu\-count| cpu\-frequency| cpu\-load| creation\-time| crl| data\-byte| db\-exchanges| db\-summaries| denied| desired\-tx\-interval| dhcp| dijkstras| disk| dr\-address| dsa| dst\-user| dst| dynamic| effective\-router\-id| egress| encoding| encryption| errors| established| evm\-ch0| evm\-ch1| evm\-ch2| expire\-time| expired| expires\-after| expires\-in| external\-imports| file\-size| file\ type| fingerprint| first\-header| frame\-bytes| frames| framing\-current\-size| framing\-limit| framing\-mode| free\-hdd\-space| free\-memory| gateway\-status| global| gre\-key| gre\-version| group\-encryption| header\-stack| hits| hw\-frame\-bytes| hw\-frames| icmp\-code| icmp\-id| icmp\-type| idle\-time| id| imposed\-label| in\-accepted| in\-dropped| in\-label| in\-previous\-hop| in\-transformed| inactive| info| inteface| invalid\-after| invalid\-before| invalid| io| ip\-dscp| ip\-dst| ip\-frag\-off| ip\-gateway| ip\-id| ip\-src| ip\-ttl| irq| issued| issuer| label| last\-accessed\-time| last\-accessed| last\-activity| last\-ip| last\-modified\-time| last\-modified| last\-seen| latency\-distribution\-measure\-interval| latency\-distribution\-samples| link\-local| local\-label| local\-pref| local\-transport| locally\-originated| ls\-requests| ls\-retransmits| mac\-dst| mac\-src| management\-protection| manufacture\-date| max\-entries| med| memory| message| model| mru| next\-hop| nexthop| no\-expiration\-info| no\-memory| nominal\-battery\-voltage| non\-cacheable| non\-output| not\-found| nstreme| offline\-after| operational| options| originator\-id| origin| ospf\-metric| ospf| out\-accepted| out\-dropped| out\-label| out\-next\-hop| out\-transformed| owner| p\-throughput| package\-architecture| package\-built\-time| package\-name| package\-version| packed\-bytes| packed\-frames| packets\-in| packets\-out| packets\-rx| path\-in\-explicit\-route| path\-in\-record\-route| path\-out\-explicit\-route| path\-out\-record\-route| peer| ph2\-state| pool| prefix\-count| primary\-dns| primary\-ntp| protocols| radius| raw\-header| received\-from| recorded\-route| refresh\-capability| remaining\-bw| remote\-group| remote\-hold\-time| remote\-id| remote\-label| remote\-min\-rx| remote\-status| reply\-dst\-address| reply\-src\-address| required\-min\-rx| resv\-bandwidth| resv\-out\-record\-route| revoked| rip| routeros\-version| router| running| rx\-1024\-1518| rx\-128\-255| rx\-1519\-max| rx\-256\-511| rx\-512\-1023| rx\-64| rx\-65\-127| rx\-align\-error| rx\-broadcast| rx\-bytes| rx\-ccq| rx\-fcs\-error| rx\-fragment| rx\-multicast| rx\-overflow| rx\-pause| rx\-rate| rx\-runt| rx\-too\-long| scep\-url| secondary\-dns| secondary\-ntp| seen\ reply| sending\-path| sending\-resv| sending\-targeted\-hello| sequence\-number| serial| service| shared| side| signal\-strength\-ch0| signal\-strength\-ch1| signal\-strength\-ch2| signal\-strength| signal\-to\-noise| since| slave| smart\-card\-key| src\-user| src| state\-changes| static| strength\-at\-rates| successes| switch| tcp\-state| tdma\-retx| tdma\-rx\-size| tdma\-timing\-offset| tdma\-tx\-size| tdma\-windfull| timestamp| too\-large| total\-entries| total\-hdd\-space| total\-memory| transport\-nexthop| tx\-1024\-1518| tx\-128\-255| tx\-1519\-max| tx\-256\-511| tx\-512\-1023| tx\-64| tx\-65\-127| tx\-align\-error| tx\-broadcast| tx\-bytes| tx\-ccq| tx\-evm\-ch0| tx\-evm\-ch1| tx\-evm\-ch2| tx\-fcs\-error| tx\-fragment| tx\-frames\-timed\-out| tx\-multicast| tx\-overflow| tx\-pause| tx\-rate| tx\-runt| tx\-signal\-strength\-ch0| tx\-signal\-strength\-ch1| tx\-signal\-strength\-ch2| tx\-signal\-strength| tx\-too\-long| udp\-dst\-port| udp\-src\-port| unknown\-server| unreachable| updates\-received| updates\-sent| up| uri| used\-hold\-time| used\-keepalive\-time| users| vlan\-protocol| vpls| wds| withdraws\-received| withdraws\-sent| wmm\-enabled| write\-sect\-since\-reboot| write\-sect\-total )(?!-)\b
</string>
					<key>name</key>
					<string>entity.other.attribute-name.readonly.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>parameters-readwrite</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>2</key>
						<dict>
							<key>name</key>
							<string>entity.other.attribute-name.readwrite.mikrotik-script</string>
						</dict>
						<key>4</key>
						<dict>
							<key>name</key>
							<string>invalid.illegal.unexpected-text.mikrotik-script</string>
						</dict>
						<key>5</key>
						<dict>
							<key>name</key>
							<string>keyword.operator.assigment.mikrotik-script</string>
						</dict>
					</dict>
					<key>match</key>
					<string>(?x) (\b(?&lt;![\/\-=])(?&lt;words&gt; 2ghz\-10mhz\-power\-channels| 2ghz\-11n\-channels| 2ghz\-5mhz\-power\-channels| 2ghz\-b\-channels| 2ghz\-g\-channels| 2ghz\-g\-turbo\-channels| 5ghz\-10mhz\-power\-channels| 5ghz\-11n\-channels| 5ghz\-5mhz\-power\-channels| 5ghz\-channels| 5ghz\-turbo\-channels| 6to4\-interface| 802\.3\-sap| 802\.3\-type| AH| DNS| ESP| NET\-BIOS| SNMP| ac\-name| accept\-dynamic\-neighbors| accept\-redirects| accept\-router\-advertisements| accept\-source\-route| accept| accessible\-via\-web| account\-local\-traffic| accounting| action| active\-flow\-timeout| active\-mode| active\-port\-type| active| adaptive\-noise\-immunity| add\-arp| add\-default\-route| add\-lifetime| add\-mac\-cookie| add\-relay\-info| address\-families| address\-family| address\-list\-timeout| address\-list| address\-pool| address\-prefix\-length| address6| addresses| address| addtime| adjacent\-neighbors| admin\-mac| advertise\-dns| advertise\-filter| advertise\-interval| advertise\-mac\-address| advertise\-timeout| advertise\-url| advertised\-l2mtu| advertise| affinity\-exclude| affinity\-include\-all| affinity\-include\-any| ageing\-time| age| ah\-algorithm| ah\-key| ah\-spi| alarm\-setting| alert\-timeout| allocate\-udp\-ports\-from| allow\-address| allow\-as\-in| allow\-disable\-external\-interface| allow\-fast\-path| allow\-guests| allow\-remote\-requests| allow\-sharedkey| allow\-target| allowed\-number| allow| always\-broadcast| always\-from\-cache| antenna\-gain| antenna\-mode| ap\-tx\-limit| apn| append\-bgp\-communities| append\-route\-targets| area\-id| area\-prefix| area| arp\-dst\-address| arp\-dst\-mac\-address| arp\-gratuitous| arp\-hardware\-type| arp\-interval| arp\-ip\-targets| arp\-opcode| arp\-packet\-type| arp\-ping| arp\-src\-address| arp\-src\-mac\-address| arp\-timeout| arp| as\-override| ascii| as| attribute\-filter| audio\-max| audio\-min| audio\-monitor| auth\-algorithms| auth\-algorithm| auth\-key| auth\-method| authenticate| authentication\-key\-id| authentication\-key| authentication\-password| authentication\-protocol| authentication\-types| authentication| authoritative| auth| auto\-bandwidth\-avg\-interval| auto\-bandwidth\-range| auto\-bandwidth\-reserve| auto\-bandwidth\-update\-interval| auto\-mac| auto\-negotiation| auto\-send\-supout| automatic\-supout| autonomous| backup\-designated\-router| bandwidth\-limit| bandwidth| band| basic\-rates\-a\/g| basic\-rates\-b| battery\-charge| battery\-voltage| baud\-rate| bearing| bgp\-as\-path\-length| bgp\-as\-path| bgp\-atomic\-aggregate| bgp\-communities| bgp\-local\-pref| bgp\-med| bgp\-origin| bgp\-prepend| bgp\-weight| bidirectional\-timeout| blink| block\-access| blockade\-k\-factor| board| body| boot\-device| boot\-file\-name| boot\-protocol| bootp\-support| bridge\-cost| bridge\-horizon| bridge\-mode| bridge\-path\-cost| bridge\-port\-priority| bridge| broadcast| bsd\-syslog| burst\-time| bytes| ca\-fingerprint| ca\-identity| cable\-setting| cable\-test| cache\-administrator| cache\-entries| cache\-hit\-dscp| cache\-max\-ttl| cache\-on\-disk| cache\-size| capabilities| cc| certificate| chain| challenge\-password| change\-tcp\-mss| channel\-time| channel\-width| channel| check\-certificate| check\-gateway| check\-interval| check\-status| chip\-info| cipher| cisco\-style\-id| cisco\-style| cisco\-vpls\-nlri\-len\-fmt| client\-id| client\-to\-client\-reflection| client\-tx\-limit| cluster\-id| code| comment| common\-name| compression| confederation\-peers| confederation| connect\-to| connection\-bytes| connection\-limit| connection\-mark| connection\-rate| connection\-state| connection\-type| connect| contact| contents| content| contrast| cost| country| count| cpu\-frequency| cpu| current\-bytes| current\-mac\-address| data\-bits| data\-channel| data| date\-and\-time| days\-valid| dead\-interval| default\-ap\-tx\-limit| default\-authentication| default\-cable\-settings| default\-client\-tx\-limit| default\-cost| default\-forwarding| default\-group| default\-name| default\-originate| default\-periodic\-calibration| default\-profile| default\-route\-distance| default\-vlan\-id| default| delay\-threshold| designated\-port\-count| designated\-router| device\-id| device| dfs\-mode| dh\-group| dhcp\-options| dhcp\-option| dhcp\-server| dial\-command| dial\-on\-demand| direction| directory| disable\-csma| disable\-running\-check| disabled| disconnect\-timeout| discover| disk\-file\-count| disk\-file\-name| disk\-lines\-per\-file| disk\-stop\-on\-full| distance| distribute\-default| distribute\-for\-default\-route| dns\-name| dns\-server| do\-not\-fragment| domain\-id| domain\-tag| domain| down\-delay| down\-flood\-thresholds| down\-script| dpd\-interval| dpd\-maximum\-failures| dscp| dst\-address\-list| dst\-address\-type| dst\-address| dst\-delta| dst\-end| dst\-host| dst\-limit| dst\-mac\-address| dst\-path| dst\-port| dst\-start| duid| duration| dynamic\-label\-range| eap\-methods| edge\-port\-discovery| edge\-port| edge| email\-to| email| enable\-nstreme| enable\-polling| enabled| enc\-algorithms| enc\-algorithm| encryption\-password| encryption\-protocol| engine\-id| esp\-auth\-algorithm| esp\-auth\-key| esp\-enc\-algorithm| esp\-enc\-key| esp\-spi| eui\-64| exchange\-mode| exclude\-groups| export\-pub\-key| export\-route\-target| external\-fdb| file\-limit| file\-name| file| filter\-direction| filter\-interface| filter\-ip\-address| filter\-ip\-protocol| filter\-mac\-address| filter\-mac\-protocol| filter\-mac| filter\-operator\-between\-entries| filter\-port| filter\-stream| fingerprint\-algorithm| firmware| flow\-control\-auto| flow\-control\-rx| flow\-control\-tx| flow\-control| force\-aes| force\-backup\-booter| forward\-delay| forwarding| forward| fragment\-offset| fragment| frame\-lifetime| frame\-size| framer\-limit| framer\-policy| frames\-per\-second| frequency\-mode| frequency\-offset| frequency| from\-address| from\-date| from\-pool| from\-time| from| full\-duplex| garbage\-timer| gateway\-class| gateway\-keepalive| gateway\-selection| gateway| generate\-key| generate\-policy| generic\-timeout| graph| group\-ciphers| group\-key\-update| group| hash\-algorithm| hello\-interval| hide\-ssid| hold\-time| holding\-priority| hop\-limit| hoplimit| hops| horizon| host\-name| host| hotspot\-address| hotspot| ht\-ampdu\-priorities| ht\-amsdu\-limit| ht\-amsdu\-threshold| ht\-basic\-mcs| ht\-chains| ht\-channel\-width| ht\-guard\-interval| ht\-rates| ht\-rxchains| ht\-streams| ht\-supported\-mcs| ht\-txchains| html\-directory| http\-cookie\-lifetime| http\-proxy| hw\-fragmentation\-threshold| hw\-protection\-mode| hw\-protection\-threshold| hw\-retries| hwmp\-default\-hoplimit| hwmp\-prep\-lifetime| hwmp\-preq\-destination\-only| hwmp\-preq\-reply\-and\-forward| hwmp\-preq\-retries| hwmp\-preq\-waiting\-time| hwmp\-rann\-interval| hwmp\-rann\-lifetime| hwmp\-rann\-propagation\-delay| iaid| icmp\-options| icmp\-rate\-limit| icmp\-rate\-mask| icmp\-timeout| identification| identity| idle\-timeout| ignore\-as\-path\-len| ignore\-directip\-modem| igp\-flood\-period| import\-route\-target| import| in\-bridge\-port| in\-bridge| in\-buffer\-errors| in\-errors| in\-filter| in\-header\-errors| in\-interface| in\-no\-policies| in\-no\-states| in\-policy\-blocked| in\-policy\-errors| in\-prefix\-list| in\-state\-expired| in\-state\-invalid| in\-state\-mismatches| in\-state\-mode\-errors| in\-state\-protocol\-errors| in\-state\-sequence\-errors| in\-template\-mismatches| inactive\-flow\-timeout| include\-igp| incoming\-filter| incoming\-packet\-mark| info\-channel| ingress\-priority| inherit\-attributes| inject\-summary\-lsas| insert\-queue\-before| instance| interface\-name| interface\-type| interfaces| interface| interim\-update| interval| invert\-math| ip\-address| ip\-forwarding| ip\-forward| ip\-header\-size| ip\-packet\-size| ip\-protocol| ipsec\-protocols| ipv4\-options| ipv6| jump\-target| k\-factor| keep\-max\-sms| keep\-result| keepalive\-timeout| keepalive\-time| keepalive| key\-bits| key\-chain| key\-id| key\-name| key\-size| key\-usage| key| kind| l2mtu| l2router\-id| lacp\-rate| last\-packet\-before| latency\-distribution\-max| latency\-distribution\-scale| latency| latitude| layer7\-protocol| learning| lease\-script| lease\-time| leds| level| life\-time| lifebytes| lifetime| limit\-bytes\-in| limit\-bytes\-out| limit\-bytes\-total| limit\-uptime| limit| line\-voltage| link\-monitoring| list| load| local\-address| local\-port| local\-tx\-speed| local\-udp\-tx\-size| locality| locally\-originated\-bgp| local| location| log\-prefix| login\-by| longitude| loop\-detect| low\-battery| lsr\-id| mac\-address| mac\-auth\-password| mac\-cookie\-timeout| mac\-protocol| make\-static| managed\-address\-configuration| management\-protection\-key| management\-protection| manual\-sa| manual\-tx\-powers| master\-interface| master\-port| match\-chain| max\-cache\-object\-size| max\-cache\-size| max\-client\-connections| max\-connections| max\-fresh\-time| max\-message\-age| max\-mru| max\-mtu| max\-prefix\-limit| max\-prefix\-restart\-time| max\-server\-connections| max\-sessions| max\-station\-count| max\-udp\-packet\-size| mbps| mdix\-enable| memory\-limit| memory\-lines| memory\-scroll| memory\-stop\-on\-full| mesh\-portal| mesh| messages\-rx| messages\-tx| method| metric\-bgp| metric\-connected| metric\-default| metric\-ospf| metric\-other\-ospf| metric\-rip| metric\-static| metric| mii\-interval| min\-runtime| min\-rx| mirror\-source| mirror\-target| mode\-cfg| modem\-init| modem\-signal\-treshold| mode| monitor| mpls\-mtu| mpls\-te\-area| mpls\-te\-router\-id| mq\-pfifo\-limit| mrru| mschapv2\-password| mschapv2\-username| mss| mtu| multicast\-buffering| multicast\-helper| multihop| multiple\-channels| multiplier| my\-id\-user\-fqdn| name| nas\-port\-type| nat\-traversal| neighbor\-id| neighbors| neighbor| netmask| network\-type| network| new\-connection\-mark| new\-dscp| new\-mss| new\-packet\-mark| new\-priority| new\-routing\-mark| new\-ttl| next\-server| nexthop\-choice| no\-ping\-delay| noise\-floor\-threshold| note| nth| ntp\-server| null\-modem| num| nv2\-cell\-radius| nv2\-noise\-floor\-offset| nv2\-preshared\-key| nv2\-qos| nv2\-queue\-count| nv2\-security| offline\-time| on\-alert| on\-backup| on\-battery| on\-event| on\-fail\-retry\-time| on\-interface| on\-line| on\-link| on\-login| on\-logout| on\-master| one\-session\-per\-host| only\-headers| only\-one| open\-status\-page| organization| organziation| orig\-mac\-address| origination\-interval| originator| ospf\-type| other\-configuration| out\-bridge\-port| out\-bridge| out\-bundle\-check\-errors| out\-bundle\-errors| out\-errors| out\-filter| out\-interface| out\-no\-states| out\-policy\-blocked| out\-policy\-dead| out\-policy\-errors| out\-prefix\-list| out\-state\-expired| out\-state\-mode\-errors| out\-state\-protocol\-errors| out\-state\-sequence\-errors| outgoing\-filter| outgoing\-packet\-mark| output\-voltage| overloaded\-output| p2p| packet\-mark| packet\-size| packet\-type| packets| page\-refresh| parent\-proxy\-port| parent\-proxy| parent\-queue| parity| passive| password| path\-cost| path\-vector\-limit| path| pci\-info| pcq\-burst\-rate| pcq\-burst\-threshold| pcq\-burst\-time| pcq\-classifier| pcq\-dst\-address\-mask| pcq\-dst\-address6\-mask| pcq\-limit| pcq\-rate| pcq\-src\-address\-mask| pcq\-src\-address6\-mask| pcq\-total\-limit| peek\-rate| per\-connection\-classifier| periodic\-calibration\-interval| periodic\-calibration| pfifo\-limit| pfs\-group| pfs| phone| phy\-regs| pin| platform| poe\-out| poe\-priority| point\-to\-point\-port| point\-to\-point| policy\-group| policy| poll\-interval| pool\-name| pool\-prefix\-length| port\-count| port\-number| port\-type| ports| port| pps| preamble\-mode| preemption\-mode| pref\-src| preferred\-gateway| preferred\-lifetime| prefix\-length| prefix| primary\-ntp| primary\-path| primary\-retry\-interval| primary\-server| primary| priority| prism\-cardtype| private\-algo| private\-key| private\-pre\-shared\-key| profile| propagate\-ttl| proposal\-check| proposal| proprietary\-extensions| proprietary\-extension| protocol\-mode| protocol| psd| pw\-mtu| pw\-type| query\-server\-timeout| query\-total\-timeout| queue\-type| queue| quick| ra\-delay| ra\-interval| ra\-lifetime| radio\-name| radius\-accounting| radius\-default\-domain| radius\-eap\-accounting| radius\-interim\-update| radius\-location\-name| radius\-mac\-authentication| radius\-mac\-caching| radius\-mac\-format| radius\-mac\-mode| random\-data| random| ranges| range| rate\-limit| rate\-selection| rate\-set| rates\-a\/g| rates\-b| rate| raw\-value| reachable\-time| read\-access| read\-only| receive\-all| receive\-enabled| receive\-errors| receive| record\-route| red\-avg\-packet| red\-burst| red\-limit| red\-max\-threshold| red\-min\-threshold| redirect\-to| redistribute\-bgp| redistribute\-connected| redistribute\-ospf| redistribute\-other\-bgp| redistribute\-other\-ospf| redistribute\-rip| redistribute\-static| refresh\-time| regexp| reject\-with| relay| release| remember| remote\-address| remote\-as| remote\-certificate| remote\-mac| remote\-peer| remote\-port| remote\-tx\-speed| remote\-udp\-tx\-size| remote| remove\-private\-as| renew| reoptimize\-interval| reoptimize\-paths| replace\-battery| replay| req\-fingerprint| require\-client\-certificate| resends| reset\-alert| reset\-counters\-all| reset\-counters| reset\-mac\-address| resource\-class| retransmit\-interval| role| root\-bridge\-id| root\-bridge| root\-path\-cost| root\-port| route\-comment| route\-distinguisher| route\-reflect| route\-tag| route\-target| router\-id| routes| routing\-mark| routing\-table| rp\-filter| rp_filter| runtime\-calibration\-running| runtime\-left| rx\-band| rx\-channel\-width| rx\-frequency| rx\-radio| sa\-dst\-address| sa\-src\-address| sa\-type| same\-not\-by\-dst| satellites| scan\-list| scope| secondary\-ntp| secondary\-paths| secondary\-server| secret| secure\-redirects| security\-profile| security| send\-dns| send\-email\-from| send\-email\-to| send\-initial\-contact| send\-redirects| send\-smtp\-server| send\-targeted| sending\-rstp| send| seq\-number| serial\-number| serialize\-connections| servers| server| service\-name| session\-timeout| set\-bgp\-communities| set\-bgp\-local\-pref| set\-bgp\-med| set\-bgp\-prepend\-path| set\-bgp\-prepend| set\-bgp\-weight| set\-check\-gateway| set\-disabled| set\-distance| set\-in\-nexthop\-direct| set\-in\-nexthop\-ipv6| set\-in\-nexthop\-linklocal| set\-in\-nexthop| set\-metric| set\-out\-nexthop\-ipv6| set\-out\-nexthop\-linklocal| set\-out\-nexthop| set\-pref\-src| set\-route\-comment| set\-route\-tag| set\-route\-targets| set\-routing\-mark| set\-scope| set\-site\-of\-origin| set\-system\-time| set\-target\-scope| set\-type| set\-use\-te\-nexthop| setup\-priority| setup| sfp\-rate\-select| sfq\-allot| sfq\-perturb| shared\-users| share| show\-at\-login| show\-dummy\-rule| signal\-range| silent\-boot| sim\-pin| simple\-queue| sip\-direct\-media| site\-id| site\-of\-origin| size| skin| slaves| smart\-boost\-mode| smart\-ssdd\-mode| smtp\-server| software\-id| source| speed| spi| split\-include| split\-user\-domain| src\-address\-list| src\-address\-type| src\-address| src\-mac\-address| src\-mac| src\-path| src\-port| ssid\-all| ssid| ssl\-certificate| start\-time| start| state| static\-algo\-0| static\-algo\-1| static\-algo\-2| static\-algo\-3| static\-key\-0| static\-key\-1| static\-key\-2| static\-key\-3| static\-sta\-private\-algo| static\-sta\-private\-key| static\-transmit\-key| station\-bridge\-clone\-mac| stats\-samples\-to\-keep| status\-autorefresh| status| stop\-bits| stop| store\-every| store\-leases\-disk| store\-name| store\-on\-disk| stp\-flags| stp\-forward\-delay| stp\-hello\-time| stp\-max\-age| stp\-msg\-age| stp\-port| stp\-root\-address| stp\-root\-cost| stp\-root\-priority| stp\-sender\-address| stp\-sender\-priority| stp\-type| streaming\-enabled| streaming\-max\-rate| streaming\-server| subject| summary\-only| supplicant\-identity| supported\-bands| supported\-rates\-a\/g| supported\-rates\-b| suppress\-filter| synchronize| syslog\-facility| syslog\-severity| syslog\-time\-format| target\-scope| target| tcp\-close\-timeout| tcp\-close\-wait\-timeout| tcp\-connection\-count| tcp\-established\-timeout| tcp\-fin\-wait\-timeout| tcp\-flags| tcp\-last\-ack\-timeout| tcp\-md5\-key| tcp\-mss| tcp\-syn\-received\-timeout| tcp\-syn\-sent\-timeout| tcp\-syncookies| tcp\-time\-wait\-timeout| tcp_syncookies| tdma\-debug| tdma\-hw\-test\-mode| tdma\-override\-rate| tdma\-override\-size| tdma\-period\-size| tdma\-test\-mode| te\-metric| template| test\-audio| test\-id| threshold| time\-zone\-name| time\-zone| timeout\-timer| timeout| time| tls\-certificate| tls\-mode| tls| to\-addresses| to\-address| to\-arp\-reply\-mac\-address| to\-dst\-mac\-address| to\-ports| to\-src\-mac\-address| top\-bits| topics| total| to| traffic| transfer\-cause| transit\-area| translator\-role| transmit\-delay| transmit\-hash\-policy| transmit\-hold\-count| transparent\-proxy| transport\-address| transport| trap\-generators| trap\-target| trap\-version| trial\-uptime| trial\-user\-profile| trigger| trusted| ttl| tunnel\-id| tunnel| tx\-band| tx\-channel\-width| tx\-frequency| tx\-power\-mode| tx\-power| tx\-radio| tx\-template| type| udp\-stream\-timeout| udp\-timeout| unicast\-ciphers| unit| unpack| up\-delay| up\-flood\-thresholds| up\-script| update\-source| update\-stats\-interval| update\-timer| upload| uptime| url| usb\-version| use\-bfd| use\-compression| use\-control\-word| use\-cspf| use\-dn| use\-encryption| use\-explicit\-null| use\-ip\-firewall\-for\-pppoe| use\-ip\-firewall\-for\-vlan| use\-ip\-firewall| use\-mpls| use\-peer\-dns| use\-peer\-ntp| use\-radius| use\-service\-tag| use\-src\-mac| use\-udp| use\-vj\-compression| username| user| v3\-protocol| v9\-template\-refresh| v9\-template\-timeout| valid\-lifetime| valid\-server| valid| value| vendor\-id| vendor| verify\-client\-certificate| verify\-server\-address\-from\-certificate| verify\-server\-certificate| version| vlan\-encap| vlan\-header| vlan\-id| vlan\-mode| vlan\-priority| vpls\-id| vrid| watch\-address| watchdog\-timer| wds\-address| wds\-cost\-range| wds\-default\-bridge| wds\-default\-cost| wds\-ignore\-ssid| wds\-mode| wins\-server| wireless\-protocol| wmm\-support| wpa\-pre\-shared\-key| wpa2\-pre\-shared\-key| write\-access| xauth\-login| xauth\-password| zone| max\-limit| connection\-nat\-state| in\-interface\-list| out\-interface\-list| tls\-host| station\-roaming| wps\-mode| discover\-interface\-list| ddns\-enabled| dont\-require\-permissions| passthrough| numbers)\b(?!-)(([\s\t]*?)(=))?)
</string>
				</dict>
			</array>
		</dict>
		<key>string-escape</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>match</key>
					<string>\\\"|\\\\|\\n|\\r|\\t|\\\$|\\\?|\\_|\\a|\\b|\\f|\\v|\\\h\h</string>
					<key>name</key>
					<string>constant.character.escape.mikrotik-script</string>
				</dict>
			</array>
		</dict>
		<key>string-expression</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>begin</key>
					<string>\$\(</string>
					<key>end</key>
					<string>\)</string>
					<key>patterns</key>
					<array>
						<dict>
							<key>include</key>
							<string>$self</string>
						</dict>
						<dict>
							<key>include</key>
							<string>#line-continuation</string>
						</dict>
						<dict>
							<key>match</key>
							<string>\n</string>
							<key>name</key>
							<string>invalid.illegal.newline.mikrotik-script</string>
						</dict>
					</array>
				</dict>
				<dict>
					<key>begin</key>
					<string>\$\[</string>
					<key>end</key>
					<string>\]</string>
					<key>patterns</key>
					<array>
						<dict>
							<key>include</key>
							<string>$self</string>
						</dict>
						<dict>
							<key>include</key>
							<string>#line-continuation</string>
						</dict>
						<dict>
							<key>match</key>
							<string>\n</string>
							<key>name</key>
							<string>invalid.illegal.newline.mikrotik-script</string>
						</dict>
					</array>
				</dict>
			</array>
		</dict>
		<key>variable</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.variable.mikrotik-script</string>
						</dict>
					</dict>
					<key>match</key>
					<string>(\$)([0-9a-zA-Z]+)</string>
					<key>name</key>
					<string>variable.other.mikrotik-script</string>
				</dict>
				<dict>
					<key>begin</key>
					<string>(\$)(\")</string>
					<key>beginCaptures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.variable.mikrotik-script</string>
						</dict>
						<key>2</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.variable.begin.mikrotik-script</string>
						</dict>
					</dict>
					<key>end</key>
					<string>\"</string>
					<key>endCaptures</key>
					<dict>
						<key>0</key>
						<dict>
							<key>name</key>
							<string>punctuation.definition.variable.end.mikrotik-script</string>
						</dict>
					</dict>
					<key>name</key>
					<string>variable.other.mikrotik-script</string>
					<key>patterns</key>
					<array>
						<dict>
							<key>include</key>
							<string>#string-escape</string>
						</dict>
						<dict>
							<key>include</key>
							<string>#line-continuation</string>
						</dict>
						<dict>
							<key>match</key>
							<string>\n</string>
							<key>name</key>
							<string>invalid.illegal.newline.mikrotik-script</string>
						</dict>
					</array>
				</dict>
			</array>
		</dict>
		<key>variable-definition</key>
		<dict>
			<key>patterns</key>
			<array>
				<dict>
					<key>captures</key>
					<dict>
						<key>1</key>
						<dict>
							<key>name</key>
							<string>keyword.operator.other.mikrotik-script</string>
						</dict>
						<key>2</key>
						<dict>
							<key>name</key>
							<string>storage.modifier.mikrotik-script</string>
						</dict>
					</dict>
					<key>match</key>
					<string>(\:)(global|local)\b</string>
				</dict>
			</array>
		</dict>
	</dict>
	<key>scopeName</key>
	<string>source.mikrotik-script</string>
	<key>uuid</key>
	<string>1a4e4c34-d9fb-4371-b819-9934ebed400c</string>
</dict>
</plist>


File: /MikrotikScript.tmPreferences
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>name</key>
   <string>Miscellaneous</string>
   <key>scope</key>
   <string>source.mikrotik-script</string>
   <key>settings</key>
   <dict>
      <key>shellVariables</key>
      <array>
         <dict>
            <key>name</key>
            <string>TM_COMMENT_START</string>
            <key>value</key>
            <string># </string>
         </dict>
      </array>
   </dict>
</dict>
</plist>


File: /MikrotikScript.YAML-tmLanguage
# [PackageDev] target_format: plist, ext: tmLanguage
---
name: Mikrotik Script
scopeName: source.mikrotik-script
fileTypes: [rsc]
uuid: 1a4e4c34-d9fb-4371-b819-9934ebed400c

patterns:
- include: '#literal-string'
- include: '#comments'
- include: '#parameters-readwrite'
- include: '#literal-constants'
- include: '#literal-boolean'
- include: '#literal-ip'
- include: '#literal-mac'
- include: '#literal-date'
- include: '#literal-number'
- include: '#variable'
- include: '#variable-definition'
- include: '#control-flow'
- include: '#commands'
- include: '#parameters-readonly'
- include: '#operators'
- include: '#line-continuation'

repository:
  literal-string:
    patterns:
    - name: string.quoted.double.mikrotik-script
      begin: '"'
      beginCaptures:
        '0': {name: punctuation.definition.string.begin.mikrotik-script}
      end: '"'
      endCaptures:
        '0': {name: punctuation.definition.string.end.mikrotik-script}
      patterns:
      - include: '#string-escape'
      - include: '#string-expression'
      - include: '#line-continuation'
      - name: invalid.illegal.newline.mikrotik-script
        match: \n

  comments:
    patterns:
    - name: comment.line.number-sign.mikrotik-script
      match: (#).*$\n?
      captures:
        '1': {name: punctuation.definition.comment.mikrotik-script}
      comment: comments are ignored by syntax

  parameters-readwrite:
    patterns:
    - match: >
        (?x)
        (\b(?<![\/\-=])(?<words>
        2ghz\-10mhz\-power\-channels|
        2ghz\-11n\-channels|
        2ghz\-5mhz\-power\-channels|
        2ghz\-b\-channels|
        2ghz\-g\-channels|
        2ghz\-g\-turbo\-channels|
        5ghz\-10mhz\-power\-channels|
        5ghz\-11n\-channels|
        5ghz\-5mhz\-power\-channels|
        5ghz\-channels|
        5ghz\-turbo\-channels|
        6to4\-interface|
        802\.3\-sap|
        802\.3\-type|
        AH|
        DNS|
        ESP|
        NET\-BIOS|
        SNMP|
        ac\-name|
        accept\-dynamic\-neighbors|
        accept\-redirects|
        accept\-router\-advertisements|
        accept\-source\-route|
        accept|
        accessible\-via\-web|
        account\-local\-traffic|
        accounting|
        action|
        active\-flow\-timeout|
        active\-mode|
        active\-port\-type|
        active|
        adaptive\-noise\-immunity|
        add\-arp|
        add\-default\-route|
        add\-lifetime|
        add\-mac\-cookie|
        add\-relay\-info|
        address\-families|
        address\-family|
        address\-list\-timeout|
        address\-list|
        address\-pool|
        address\-prefix\-length|
        address6|
        addresses|
        address|
        addtime|
        adjacent\-neighbors|
        admin\-mac|
        advertise\-dns|
        advertise\-filter|
        advertise\-interval|
        advertise\-mac\-address|
        advertise\-timeout|
        advertise\-url|
        advertised\-l2mtu|
        advertise|
        affinity\-exclude|
        affinity\-include\-all|
        affinity\-include\-any|
        ageing\-time|
        age|
        ah\-algorithm|
        ah\-key|
        ah\-spi|
        alarm\-setting|
        alert\-timeout|
        allocate\-udp\-ports\-from|
        allow\-address|
        allow\-as\-in|
        allow\-disable\-external\-interface|
        allow\-fast\-path|
        allow\-guests|
        allow\-remote\-requests|
        allow\-sharedkey|
        allow\-target|
        allowed\-number|
        allow|
        always\-broadcast|
        always\-from\-cache|
        antenna\-gain|
        antenna\-mode|
        ap\-tx\-limit|
        apn|
        append\-bgp\-communities|
        append\-route\-targets|
        area\-id|
        area\-prefix|
        area|
        arp\-dst\-address|
        arp\-dst\-mac\-address|
        arp\-gratuitous|
        arp\-hardware\-type|
        arp\-interval|
        arp\-ip\-targets|
        arp\-opcode|
        arp\-packet\-type|
        arp\-ping|
        arp\-src\-address|
        arp\-src\-mac\-address|
        arp\-timeout|
        arp|
        as\-override|
        ascii|
        as|
        attribute\-filter|
        audio\-max|
        audio\-min|
        audio\-monitor|
        auth\-algorithms|
        auth\-algorithm|
        auth\-key|
        auth\-method|
        authenticate|
        authentication\-key\-id|
        authentication\-key|
        authentication\-password|
        authentication\-protocol|
        authentication\-types|
        authentication|
        authoritative|
        auth|
        auto\-bandwidth\-avg\-interval|
        auto\-bandwidth\-range|
        auto\-bandwidth\-reserve|
        auto\-bandwidth\-update\-interval|
        auto\-mac|
        auto\-negotiation|
        auto\-send\-supout|
        automatic\-supout|
        autonomous|
        backup\-designated\-router|
        bandwidth\-limit|
        bandwidth|
        band|
        basic\-rates\-a\/g|
        basic\-rates\-b|
        battery\-charge|
        battery\-voltage|
        baud\-rate|
        bearing|
        bgp\-as\-path\-length|
        bgp\-as\-path|
        bgp\-atomic\-aggregate|
        bgp\-communities|
        bgp\-local\-pref|
        bgp\-med|
        bgp\-origin|
        bgp\-prepend|
        bgp\-weight|
        bidirectional\-timeout|
        blink|
        block\-access|
        blockade\-k\-factor|
        board|
        body|
        boot\-device|
        boot\-file\-name|
        boot\-protocol|
        bootp\-support|
        bridge\-cost|
        bridge\-horizon|
        bridge\-mode|
        bridge\-path\-cost|
        bridge\-port\-priority|
        bridge|
        broadcast|
        bsd\-syslog|
        burst\-time|
        bytes|
        ca\-fingerprint|
        ca\-identity|
        cable\-setting|
        cable\-test|
        cache\-administrator|
        cache\-entries|
        cache\-hit\-dscp|
        cache\-max\-ttl|
        cache\-on\-disk|
        cache\-size|
        capabilities|
        cc|
        certificate|
        chain|
        challenge\-password|
        change\-tcp\-mss|
        channel\-time|
        channel\-width|
        channel|
        check\-certificate|
        check\-gateway|
        check\-interval|
        check\-status|
        chip\-info|
        cipher|
        cisco\-style\-id|
        cisco\-style|
        cisco\-vpls\-nlri\-len\-fmt|
        client\-id|
        client\-to\-client\-reflection|
        client\-tx\-limit|
        cluster\-id|
        code|
        comment|
        common\-name|
        compression|
        confederation\-peers|
        confederation|
        connect\-to|
        connection\-bytes|
        connection\-limit|
        connection\-mark|
        connection\-rate|
        connection\-state|
        connection\-type|
        connect|
        contact|
        contents|
        content|
        contrast|
        cost|
        country|
        count|
        cpu\-frequency|
        cpu|
        current\-bytes|
        current\-mac\-address|
        data\-bits|
        data\-channel|
        data|
        date\-and\-time|
        days\-valid|
        dead\-interval|
        default\-ap\-tx\-limit|
        default\-authentication|
        default\-cable\-settings|
        default\-client\-tx\-limit|
        default\-cost|
        default\-forwarding|
        default\-group|
        default\-name|
        default\-originate|
        default\-periodic\-calibration|
        default\-profile|
        default\-route\-distance|
        default\-vlan\-id|
        default|
        delay\-threshold|
        designated\-port\-count|
        designated\-router|
        device\-id|
        device|
        dfs\-mode|
        dh\-group|
        dhcp\-options|
        dhcp\-option|
        dhcp\-server|
        dial\-command|
        dial\-on\-demand|
        direction|
        directory|
        disable\-csma|
        disable\-running\-check|
        disabled|
        disconnect\-timeout|
        discover|
        disk\-file\-count|
        disk\-file\-name|
        disk\-lines\-per\-file|
        disk\-stop\-on\-full|
        distance|
        distribute\-default|
        distribute\-for\-default\-route|
        dns\-name|
        dns\-server|
        do\-not\-fragment|
        domain\-id|
        domain\-tag|
        domain|
        down\-delay|
        down\-flood\-thresholds|
        down\-script|
        dpd\-interval|
        dpd\-maximum\-failures|
        dscp|
        dst\-address\-list|
        dst\-address\-type|
        dst\-address|
        dst\-delta|
        dst\-end|
        dst\-host|
        dst\-limit|
        dst\-mac\-address|
        dst\-path|
        dst\-port|
        dst\-start|
        duid|
        duration|
        dynamic\-label\-range|
        eap\-methods|
        edge\-port\-discovery|
        edge\-port|
        edge|
        email\-to|
        email|
        enable\-nstreme|
        enable\-polling|
        enabled|
        enc\-algorithms|
        enc\-algorithm|
        encryption\-password|
        encryption\-protocol|
        engine\-id|
        esp\-auth\-algorithm|
        esp\-auth\-key|
        esp\-enc\-algorithm|
        esp\-enc\-key|
        esp\-spi|
        eui\-64|
        exchange\-mode|
        exclude\-groups|
        export\-pub\-key|
        export\-route\-target|
        external\-fdb|
        file\-limit|
        file\-name|
        file|
        filter\-direction|
        filter\-interface|
        filter\-ip\-address|
        filter\-ip\-protocol|
        filter\-mac\-address|
        filter\-mac\-protocol|
        filter\-mac|
        filter\-operator\-between\-entries|
        filter\-port|
        filter\-stream|
        fingerprint\-algorithm|
        firmware|
        flow\-control\-auto|
        flow\-control\-rx|
        flow\-control\-tx|
        flow\-control|
        force\-aes|
        force\-backup\-booter|
        forward\-delay|
        forwarding|
        forward|
        fragment\-offset|
        fragment|
        frame\-lifetime|
        frame\-size|
        framer\-limit|
        framer\-policy|
        frames\-per\-second|
        frequency\-mode|
        frequency\-offset|
        frequency|
        from\-address|
        from\-date|
        from\-pool|
        from\-time|
        from|
        full\-duplex|
        garbage\-timer|
        gateway\-class|
        gateway\-keepalive|
        gateway\-selection|
        gateway|
        generate\-key|
        generate\-policy|
        generic\-timeout|
        graph|
        group\-ciphers|
        group\-key\-update|
        group|
        hash\-algorithm|
        hello\-interval|
        hide\-ssid|
        hold\-time|
        holding\-priority|
        hop\-limit|
        hoplimit|
        hops|
        horizon|
        host\-name|
        host|
        hotspot\-address|
        hotspot|
        ht\-ampdu\-priorities|
        ht\-amsdu\-limit|
        ht\-amsdu\-threshold|
        ht\-basic\-mcs|
        ht\-chains|
        ht\-channel\-width|
        ht\-guard\-interval|
        ht\-rates|
        ht\-rxchains|
        ht\-streams|
        ht\-supported\-mcs|
        ht\-txchains|
        html\-directory|
        http\-cookie\-lifetime|
        http\-proxy|
        hw\-fragmentation\-threshold|
        hw\-protection\-mode|
        hw\-protection\-threshold|
        hw\-retries|
        hwmp\-default\-hoplimit|
        hwmp\-prep\-lifetime|
        hwmp\-preq\-destination\-only|
        hwmp\-preq\-reply\-and\-forward|
        hwmp\-preq\-retries|
        hwmp\-preq\-waiting\-time|
        hwmp\-rann\-interval|
        hwmp\-rann\-lifetime|
        hwmp\-rann\-propagation\-delay|
        iaid|
        icmp\-options|
        icmp\-rate\-limit|
        icmp\-rate\-mask|
        icmp\-timeout|
        identification|
        identity|
        idle\-timeout|
        ignore\-as\-path\-len|
        ignore\-directip\-modem|
        igp\-flood\-period|
        import\-route\-target|
        import|
        in\-bridge\-port|
        in\-bridge|
        in\-buffer\-errors|
        in\-errors|
        in\-filter|
        in\-header\-errors|
        in\-interface|
        in\-no\-policies|
        in\-no\-states|
        in\-policy\-blocked|
        in\-policy\-errors|
        in\-prefix\-list|
        in\-state\-expired|
        in\-state\-invalid|
        in\-state\-mismatches|
        in\-state\-mode\-errors|
        in\-state\-protocol\-errors|
        in\-state\-sequence\-errors|
        in\-template\-mismatches|
        inactive\-flow\-timeout|
        include\-igp|
        incoming\-filter|
        incoming\-packet\-mark|
        info\-channel|
        ingress\-priority|
        inherit\-attributes|
        inject\-summary\-lsas|
        insert\-queue\-before|
        instance|
        interface\-name|
        interface\-type|
        interfaces|
        interface|
        interim\-update|
        interval|
        invert\-math|
        ip\-address|
        ip\-forwarding|
        ip\-forward|
        ip\-header\-size|
        ip\-packet\-size|
        ip\-protocol|
        ipsec\-protocols|
        ipv4\-options|
        ipv6|
        jump\-target|
        k\-factor|
        keep\-max\-sms|
        keep\-result|
        keepalive\-timeout|
        keepalive\-time|
        keepalive|
        key\-bits|
        key\-chain|
        key\-id|
        key\-name|
        key\-size|
        key\-usage|
        key|
        kind|
        l2mtu|
        l2router\-id|
        lacp\-rate|
        last\-packet\-before|
        latency\-distribution\-max|
        latency\-distribution\-scale|
        latency|
        latitude|
        layer7\-protocol|
        learning|
        lease\-script|
        lease\-time|
        leds|
        level|
        life\-time|
        lifebytes|
        lifetime|
        limit\-bytes\-in|
        limit\-bytes\-out|
        limit\-bytes\-total|
        limit\-uptime|
        limit|
        line\-voltage|
        link\-monitoring|
        list|
        load|
        local\-address|
        local\-port|
        local\-tx\-speed|
        local\-udp\-tx\-size|
        locality|
        locally\-originated\-bgp|
        local|
        location|
        log\-prefix|
        login\-by|
        longitude|
        loop\-detect|
        low\-battery|
        lsr\-id|
        mac\-address|
        mac\-auth\-password|
        mac\-cookie\-timeout|
        mac\-protocol|
        make\-static|
        managed\-address\-configuration|
        management\-protection\-key|
        management\-protection|
        manual\-sa|
        manual\-tx\-powers|
        master\-interface|
        master\-port|
        match\-chain|
        max\-cache\-object\-size|
        max\-cache\-size|
        max\-client\-connections|
        max\-connections|
        max\-fresh\-time|
        max\-message\-age|
        max\-mru|
        max\-mtu|
        max\-prefix\-limit|
        max\-prefix\-restart\-time|
        max\-server\-connections|
        max\-sessions|
        max\-station\-count|
        max\-udp\-packet\-size|
        mbps|
        mdix\-enable|
        memory\-limit|
        memory\-lines|
        memory\-scroll|
        memory\-stop\-on\-full|
        mesh\-portal|
        mesh|
        messages\-rx|
        messages\-tx|
        method|
        metric\-bgp|
        metric\-connected|
        metric\-default|
        metric\-ospf|
        metric\-other\-ospf|
        metric\-rip|
        metric\-static|
        metric|
        mii\-interval|
        min\-runtime|
        min\-rx|
        mirror\-source|
        mirror\-target|
        mode\-cfg|
        modem\-init|
        modem\-signal\-treshold|
        mode|
        monitor|
        mpls\-mtu|
        mpls\-te\-area|
        mpls\-te\-router\-id|
        mq\-pfifo\-limit|
        mrru|
        mschapv2\-password|
        mschapv2\-username|
        mss|
        mtu|
        multicast\-buffering|
        multicast\-helper|
        multihop|
        multiple\-channels|
        multiplier|
        my\-id\-user\-fqdn|
        name|
        nas\-port\-type|
        nat\-traversal|
        neighbor\-id|
        neighbors|
        neighbor|
        netmask|
        network\-type|
        network|
        new\-connection\-mark|
        new\-dscp|
        new\-mss|
        new\-packet\-mark|
        new\-priority|
        new\-routing\-mark|
        new\-ttl|
        next\-server|
        nexthop\-choice|
        no\-ping\-delay|
        noise\-floor\-threshold|
        note|
        nth|
        ntp\-server|
        null\-modem|
        num|
        nv2\-cell\-radius|
        nv2\-noise\-floor\-offset|
        nv2\-preshared\-key|
        nv2\-qos|
        nv2\-queue\-count|
        nv2\-security|
        offline\-time|
        on\-alert|
        on\-backup|
        on\-battery|
        on\-event|
        on\-fail\-retry\-time|
        on\-interface|
        on\-line|
        on\-link|
        on\-login|
        on\-logout|
        on\-master|
        one\-session\-per\-host|
        only\-headers|
        only\-one|
        open\-status\-page|
        organization|
        organziation|
        orig\-mac\-address|
        origination\-interval|
        originator|
        ospf\-type|
        other\-configuration|
        out\-bridge\-port|
        out\-bridge|
        out\-bundle\-check\-errors|
        out\-bundle\-errors|
        out\-errors|
        out\-filter|
        out\-interface|
        out\-no\-states|
        out\-policy\-blocked|
        out\-policy\-dead|
        out\-policy\-errors|
        out\-prefix\-list|
        out\-state\-expired|
        out\-state\-mode\-errors|
        out\-state\-protocol\-errors|
        out\-state\-sequence\-errors|
        outgoing\-filter|
        outgoing\-packet\-mark|
        output\-voltage|
        overloaded\-output|
        p2p|
        packet\-mark|
        packet\-size|
        packet\-type|
        packets|
        page\-refresh|
        parent\-proxy\-port|
        parent\-proxy|
        parent\-queue|
        parity|
        passive|
        password|
        path\-cost|
        path\-vector\-limit|
        path|
        pci\-info|
        pcq\-burst\-rate|
        pcq\-burst\-threshold|
        pcq\-burst\-time|
        pcq\-classifier|
        pcq\-dst\-address\-mask|
        pcq\-dst\-address6\-mask|
        pcq\-limit|
        pcq\-rate|
        pcq\-src\-address\-mask|
        pcq\-src\-address6\-mask|
        pcq\-total\-limit|
        peek\-rate|
        per\-connection\-classifier|
        periodic\-calibration\-interval|
        periodic\-calibration|
        pfifo\-limit|
        pfs\-group|
        pfs|
        phone|
        phy\-regs|
        pin|
        platform|
        poe\-out|
        poe\-priority|
        point\-to\-point\-port|
        point\-to\-point|
        policy\-group|
        policy|
        poll\-interval|
        pool\-name|
        pool\-prefix\-length|
        port\-count|
        port\-number|
        port\-type|
        ports|
        port|
        pps|
        preamble\-mode|
        preemption\-mode|
        pref\-src|
        preferred\-gateway|
        preferred\-lifetime|
        prefix\-length|
        prefix|
        primary\-ntp|
        primary\-path|
        primary\-retry\-interval|
        primary\-server|
        primary|
        priority|
        prism\-cardtype|
        private\-algo|
        private\-key|
        private\-pre\-shared\-key|
        profile|
        propagate\-ttl|
        proposal\-check|
        proposal|
        proprietary\-extensions|
        proprietary\-extension|
        protocol\-mode|
        protocol|
        psd|
        pw\-mtu|
        pw\-type|
        query\-server\-timeout|
        query\-total\-timeout|
        queue\-type|
        queue|
        quick|
        ra\-delay|
        ra\-interval|
        ra\-lifetime|
        radio\-name|
        radius\-accounting|
        radius\-default\-domain|
        radius\-eap\-accounting|
        radius\-interim\-update|
        radius\-location\-name|
        radius\-mac\-authentication|
        radius\-mac\-caching|
        radius\-mac\-format|
        radius\-mac\-mode|
        random\-data|
        random|
        ranges|
        range|
        rate\-limit|
        rate\-selection|
        rate\-set|
        rates\-a\/g|
        rates\-b|
        rate|
        raw\-value|
        reachable\-time|
        read\-access|
        read\-only|
        receive\-all|
        receive\-enabled|
        receive\-errors|
        receive|
        record\-route|
        red\-avg\-packet|
        red\-burst|
        red\-limit|
        red\-max\-threshold|
        red\-min\-threshold|
        redirect\-to|
        redistribute\-bgp|
        redistribute\-connected|
        redistribute\-ospf|
        redistribute\-other\-bgp|
        redistribute\-other\-ospf|
        redistribute\-rip|
        redistribute\-static|
        refresh\-time|
        regexp|
        reject\-with|
        relay|
        release|
        remember|
        remote\-address|
        remote\-as|
        remote\-certificate|
        remote\-mac|
        remote\-peer|
        remote\-port|
        remote\-tx\-speed|
        remote\-udp\-tx\-size|
        remote|
        remove\-private\-as|
        renew|
        reoptimize\-interval|
        reoptimize\-paths|
        replace\-battery|
        replay|
        req\-fingerprint|
        require\-client\-certificate|
        resends|
        reset\-alert|
        reset\-counters\-all|
        reset\-counters|
        reset\-mac\-address|
        resource\-class|
        retransmit\-interval|
        role|
        root\-bridge\-id|
        root\-bridge|
        root\-path\-cost|
        root\-port|
        route\-comment|
        route\-distinguisher|
        route\-reflect|
        route\-tag|
        route\-target|
        router\-id|
        routes|
        routing\-mark|
        routing\-table|
        rp\-filter|
        rp_filter|
        runtime\-calibration\-running|
        runtime\-left|
        rx\-band|
        rx\-channel\-width|
        rx\-frequency|
        rx\-radio|
        sa\-dst\-address|
        sa\-src\-address|
        sa\-type|
        same\-not\-by\-dst|
        satellites|
        scan\-list|
        scope|
        secondary\-ntp|
        secondary\-paths|
        secondary\-server|
        secret|
        secure\-redirects|
        security\-profile|
        security|
        send\-dns|
        send\-email\-from|
        send\-email\-to|
        send\-initial\-contact|
        send\-redirects|
        send\-smtp\-server|
        send\-targeted|
        sending\-rstp|
        send|
        seq\-number|
        serial\-number|
        serialize\-connections|
        servers|
        server|
        service\-name|
        session\-timeout|
        set\-bgp\-communities|
        set\-bgp\-local\-pref|
        set\-bgp\-med|
        set\-bgp\-prepend\-path|
        set\-bgp\-prepend|
        set\-bgp\-weight|
        set\-check\-gateway|
        set\-disabled|
        set\-distance|
        set\-in\-nexthop\-direct|
        set\-in\-nexthop\-ipv6|
        set\-in\-nexthop\-linklocal|
        set\-in\-nexthop|
        set\-metric|
        set\-out\-nexthop\-ipv6|
        set\-out\-nexthop\-linklocal|
        set\-out\-nexthop|
        set\-pref\-src|
        set\-route\-comment|
        set\-route\-tag|
        set\-route\-targets|
        set\-routing\-mark|
        set\-scope|
        set\-site\-of\-origin|
        set\-system\-time|
        set\-target\-scope|
        set\-type|
        set\-use\-te\-nexthop|
        setup\-priority|
        setup|
        sfp\-rate\-select|
        sfq\-allot|
        sfq\-perturb|
        shared\-users|
        share|
        show\-at\-login|
        show\-dummy\-rule|
        signal\-range|
        silent\-boot|
        sim\-pin|
        simple\-queue|
        sip\-direct\-media|
        site\-id|
        site\-of\-origin|
        size|
        skin|
        slaves|
        smart\-boost\-mode|
        smart\-ssdd\-mode|
        smtp\-server|
        software\-id|
        source|
        speed|
        spi|
        split\-include|
        split\-user\-domain|
        src\-address\-list|
        src\-address\-type|
        src\-address|
        src\-mac\-address|
        src\-mac|
        src\-path|
        src\-port|
        ssid\-all|
        ssid|
        ssl\-certificate|
        start\-time|
        start|
        state|
        static\-algo\-0|
        static\-algo\-1|
        static\-algo\-2|
        static\-algo\-3|
        static\-key\-0|
        static\-key\-1|
        static\-key\-2|
        static\-key\-3|
        static\-sta\-private\-algo|
        static\-sta\-private\-key|
        static\-transmit\-key|
        station\-bridge\-clone\-mac|
        stats\-samples\-to\-keep|
        status\-autorefresh|
        status|
        stop\-bits|
        stop|
        store\-every|
        store\-leases\-disk|
        store\-name|
        store\-on\-disk|
        stp\-flags|
        stp\-forward\-delay|
        stp\-hello\-time|
        stp\-max\-age|
        stp\-msg\-age|
        stp\-port|
        stp\-root\-address|
        stp\-root\-cost|
        stp\-root\-priority|
        stp\-sender\-address|
        stp\-sender\-priority|
        stp\-type|
        streaming\-enabled|
        streaming\-max\-rate|
        streaming\-server|
        subject|
        summary\-only|
        supplicant\-identity|
        supported\-bands|
        supported\-rates\-a\/g|
        supported\-rates\-b|
        suppress\-filter|
        synchronize|
        syslog\-facility|
        syslog\-severity|
        syslog\-time\-format|
        target\-scope|
        target|
        tcp\-close\-timeout|
        tcp\-close\-wait\-timeout|
        tcp\-connection\-count|
        tcp\-established\-timeout|
        tcp\-fin\-wait\-timeout|
        tcp\-flags|
        tcp\-last\-ack\-timeout|
        tcp\-md5\-key|
        tcp\-mss|
        tcp\-syn\-received\-timeout|
        tcp\-syn\-sent\-timeout|
        tcp\-syncookies|
        tcp\-time\-wait\-timeout|
        tcp_syncookies|
        tdma\-debug|
        tdma\-hw\-test\-mode|
        tdma\-override\-rate|
        tdma\-override\-size|
        tdma\-period\-size|
        tdma\-test\-mode|
        te\-metric|
        template|
        test\-audio|
        test\-id|
        threshold|
        time\-zone\-name|
        time\-zone|
        timeout\-timer|
        timeout|
        time|
        tls\-certificate|
        tls\-mode|
        tls|
        to\-addresses|
        to\-address|
        to\-arp\-reply\-mac\-address|
        to\-dst\-mac\-address|
        to\-ports|
        to\-src\-mac\-address|
        top\-bits|
        topics|
        total|
        to|
        traffic|
        transfer\-cause|
        transit\-area|
        translator\-role|
        transmit\-delay|
        transmit\-hash\-policy|
        transmit\-hold\-count|
        transparent\-proxy|
        transport\-address|
        transport|
        trap\-generators|
        trap\-target|
        trap\-version|
        trial\-uptime|
        trial\-user\-profile|
        trigger|
        trusted|
        ttl|
        tunnel\-id|
        tunnel|
        tx\-band|
        tx\-channel\-width|
        tx\-frequency|
        tx\-power\-mode|
        tx\-power|
        tx\-radio|
        tx\-template|
        type|
        udp\-stream\-timeout|
        udp\-timeout|
        unicast\-ciphers|
        unit|
        unpack|
        up\-delay|
        up\-flood\-thresholds|
        up\-script|
        update\-source|
        update\-stats\-interval|
        update\-timer|
        upload|
        uptime|
        url|
        usb\-version|
        use\-bfd|
        use\-compression|
        use\-control\-word|
        use\-cspf|
        use\-dn|
        use\-encryption|
        use\-explicit\-null|
        use\-ip\-firewall\-for\-pppoe|
        use\-ip\-firewall\-for\-vlan|
        use\-ip\-firewall|
        use\-mpls|
        use\-peer\-dns|
        use\-peer\-ntp|
        use\-radius|
        use\-service\-tag|
        use\-src\-mac|
        use\-udp|
        use\-vj\-compression|
        username|
        user|
        v3\-protocol|
        v9\-template\-refresh|
        v9\-template\-timeout|
        valid\-lifetime|
        valid\-server|
        valid|
        value|
        vendor\-id|
        vendor|
        verify\-client\-certificate|
        verify\-server\-address\-from\-certificate|
        verify\-server\-certificate|
        version|
        vlan\-encap|
        vlan\-header|
        vlan\-id|
        vlan\-mode|
        vlan\-priority|
        vpls\-id|
        vrid|
        watch\-address|
        watchdog\-timer|
        wds\-address|
        wds\-cost\-range|
        wds\-default\-bridge|
        wds\-default\-cost|
        wds\-ignore\-ssid|
        wds\-mode|
        wins\-server|
        wireless\-protocol|
        wmm\-support|
        wpa\-pre\-shared\-key|
        wpa2\-pre\-shared\-key|
        write\-access|
        xauth\-login|
        xauth\-password|
        zone
        )\b(?!-)(([\s\t]*?)(=))?)
      captures:
        '2': {name: entity.other.attribute-name.readwrite.mikrotik-script}
        '4': {name: invalid.illegal.unexpected-text.mikrotik-script}
        '5': {name: keyword.operator.assigment.mikrotik-script}

  commands:
    patterns:
    - name: support.function.mikrotik-script
      match: >
        (?x)
        \b(?<![\-=])(
        Neighbor|
        aaa|
        accept\-filter|
        access\-list|
        access|
        accounting|
        action|
        address\-list|
        address|
        add|
        advertise\-filter|
        advertisements|
        aggregate|
        alert|
        align|
        area|
        arp|
        bandwidth\-server|
        bandwidth\-test|
        beep|
        bfd|
        bgp\-vpls|
        bgp|
        binding|
        bonding|
        bridge|
        cache\-contents|
        cache|
        certificate|
        cisco\-bgp\-vpls|
        client|
        config|
        connect\-list|
        connections|
        connection|
        cookie|
        cpu|
        delay|
        detail|
        dhcp\-client|
        dhcp\-relay|
        dhcp\-server|
        direct|
        disable|
        discovery|
        dns\-update|
        e\-mail|
        edit|
        enable|
        environment|
        eoip|
        error|
        ethernet|
        export|
        fdb|
        fetch|
        file|
        filter|
        find|
        find|
        firewall|
        firmware|
        flush|
        get|
        gps|
        graphing|
        gre6|
        gre|
        group|
        host|
        hotspot|
        identity|
        inbox|
        info|
        inserts|
        installed\-sa|
        instance|
        interfaces|
        interface|
        interface|
        ip\-binding|
        ip\-scan|
        ipip|
        ipsec|
        ipv6|
        ip|
        ip|
        irq|
        keys|
        key|
        l2tp\-client|
        l2tp\-server|
        latency\-distribution|
        layer7\-protocol|
        lcd|
        ldp|
        lease|
        leds|
        len|
        logging|
        log|
        lookup|
        lsa|
        mac\-server|
        mac\-winbox|
        mangle|
        manual\-sa|
        manual\-tx\-power\-table|
        mesh|
        mirror|
        mme|
        mode\-cfg|
        monitor|
        mpls|
        nat|
        nbma\-neighbor|
        nd|
        neighbor|
        netwatch|
        network|
        note|
        nstreme\-dual|
        nstreme|
        ntp|
        option|
        originators|
        ospf\-router|
        ospf|
        ovpn\-client|
        ovpn\-server|
        packet\-generator|
        packet\-template|
        packet|
        parse|
        path\-state|
        pci|
        peer|
        pick|
        ping|
        policy|
        pool|
        port|
        ppp\-client|
        pppoe\-client|
        pppoe\-server|
        ppp|
        pptp\-client|
        pptp\-server|
        prefix\-list|
        prefix|
        print|
        profile|
        proposal|
        protocol|
        proxy|
        put|
        queue|
        range|
        raw|
        registration\-table|
        remote\-peers|
        remove|
        resolve|
        resource|
        resv\-state|
        rip|
        routerboard|
        route|
        routing|
        run|
        scan|
        scep|
        scheduler|
        script|
        security\-profiles|
        send|
        server|
        service|
        settings|
        set|
        set|
        sham\-link|
        shares|
        share|
        smb|
        sms|
        snapshot|
        sniffer|
        socks|
        sstp\-client|
        sstp\-server|
        statistics|
        stats|
        status|
        switch|
        system|
        target|
        terminal|
        time|
        toarray|
        tobool|
        toid|
        toip6|
        toip|
        tonum|
        tool|
        tostr|
        totime|
        typeof|
        tracking|
        traffic\-eng|
        traffic\-flow|
        traffic\-generator|
        traffic\-monitor|
        tunnel\-path|
        type|
        uncounted|
        upgrade|
        upnp|
        ups|
        usb|
        used|
        users|
        user|
        virtual\-link|
        vlan|
        vpls|
        vpnv4\-route|
        vrf|
        vrrp|
        walled\-garden|
        watchdog|
        wds|
        web\-access|
        wireless|
        return
        )(?!-)\b

  parameters-readonly:
    patterns:
    - name: entity.other.attribute-name.readonly.mikrotik-script
      match: >
        (?x)
        \b(?<![\-=])(
        802\.1x\-port\-enabled|
        ac\-mac|
        ack\-timeout|
        active\-address|
        active\-client\-id|
        active\-cpu|
        active\-interfaces|
        active\-links|
        active\-mac\-address|
        active\-server|
        actual\-interface|
        actual\-tx\-interval|
        addresses|
        adjacency|
        agent\-circuit\-id|
        agent\-remote\-id|
        aggregator|
        ap|
        architecture\-name|
        as\-path|
        as4\-capability|
        assured|
        atomic\-aggregate|
        authentication\-type|
        authority|
        backup\-dr\-address|
        bad\-blocks|
        bgp\-ext\-communities|
        bgp|
        blocked|
        board\-name|
        bytes\-in|
        bytes\-out|
        ca\-crl\-host|
        caller\-id|
        category|
        ca|
        checksum|
        cisco\-bgp\-signaled|
        client|
        cluster\-list|
        communities|
        cpu\-count|
        cpu\-frequency|
        cpu\-load|
        creation\-time|
        crl|
        data\-byte|
        db\-exchanges|
        db\-summaries|
        denied|
        desired\-tx\-interval|
        dhcp|
        dijkstras|
        disk|
        dr\-address|
        dsa|
        dst\-user|
        dst|
        dynamic|
        effective\-router\-id|
        egress|
        encoding|
        encryption|
        errors|
        established|
        evm\-ch0|
        evm\-ch1|
        evm\-ch2|
        expire\-time|
        expired|
        expires\-after|
        expires\-in|
        external\-imports|
        file\-size|
        file\ type|
        fingerprint|
        first\-header|
        frame\-bytes|
        frames|
        framing\-current\-size|
        framing\-limit|
        framing\-mode|
        free\-hdd\-space|
        free\-memory|
        gateway\-status|
        global|
        gre\-key|
        gre\-version|
        group\-encryption|
        header\-stack|
        hits|
        hw\-frame\-bytes|
        hw\-frames|
        icmp\-code|
        icmp\-id|
        icmp\-type|
        idle\-time|
        id|
        imposed\-label|
        in\-accepted|
        in\-dropped|
        in\-label|
        in\-previous\-hop|
        in\-transformed|
        inactive|
        info|
        inteface|
        invalid\-after|
        invalid\-before|
        invalid|
        io|
        ip\-dscp|
        ip\-dst|
        ip\-frag\-off|
        ip\-gateway|
        ip\-id|
        ip\-src|
        ip\-ttl|
        irq|
        issued|
        issuer|
        label|
        last\-accessed\-time|
        last\-accessed|
        last\-activity|
        last\-ip|
        last\-modified\-time|
        last\-modified|
        last\-seen|
        latency\-distribution\-measure\-interval|
        latency\-distribution\-samples|
        link\-local|
        local\-label|
        local\-pref|
        local\-transport|
        locally\-originated|
        ls\-requests|
        ls\-retransmits|
        mac\-dst|
        mac\-src|
        management\-protection|
        manufacture\-date|
        max\-entries|
        med|
        memory|
        message|
        model|
        mru|
        next\-hop|
        nexthop|
        no\-expiration\-info|
        no\-memory|
        nominal\-battery\-voltage|
        non\-cacheable|
        non\-output|
        not\-found|
        nstreme|
        offline\-after|
        operational|
        options|
        originator\-id|
        origin|
        ospf\-metric|
        ospf|
        out\-accepted|
        out\-dropped|
        out\-label|
        out\-next\-hop|
        out\-transformed|
        owner|
        p\-throughput|
        package\-architecture|
        package\-built\-time|
        package\-name|
        package\-version|
        packed\-bytes|
        packed\-frames|
        packets\-in|
        packets\-out|
        packets\-rx|
        path\-in\-explicit\-route|
        path\-in\-record\-route|
        path\-out\-explicit\-route|
        path\-out\-record\-route|
        peer|
        ph2\-state|
        pool|
        prefix\-count|
        primary\-dns|
        primary\-ntp|
        protocols|
        radius|
        raw\-header|
        received\-from|
        recorded\-route|
        refresh\-capability|
        remaining\-bw|
        remote\-group|
        remote\-hold\-time|
        remote\-id|
        remote\-label|
        remote\-min\-rx|
        remote\-status|
        reply\-dst\-address|
        reply\-src\-address|
        required\-min\-rx|
        resv\-bandwidth|
        resv\-out\-record\-route|
        revoked|
        rip|
        routeros\-version|
        router|
        running|
        rx\-1024\-1518|
        rx\-128\-255|
        rx\-1519\-max|
        rx\-256\-511|
        rx\-512\-1023|
        rx\-64|
        rx\-65\-127|
        rx\-align\-error|
        rx\-broadcast|
        rx\-bytes|
        rx\-ccq|
        rx\-fcs\-error|
        rx\-fragment|
        rx\-multicast|
        rx\-overflow|
        rx\-pause|
        rx\-rate|
        rx\-runt|
        rx\-too\-long|
        scep\-url|
        secondary\-dns|
        secondary\-ntp|
        seen\ reply|
        sending\-path|
        sending\-resv|
        sending\-targeted\-hello|
        sequence\-number|
        serial|
        service|
        shared|
        side|
        signal\-strength\-ch0|
        signal\-strength\-ch1|
        signal\-strength\-ch2|
        signal\-strength|
        signal\-to\-noise|
        since|
        slave|
        smart\-card\-key|
        src\-user|
        src|
        state\-changes|
        static|
        strength\-at\-rates|
        successes|
        switch|
        tcp\-state|
        tdma\-retx|
        tdma\-rx\-size|
        tdma\-timing\-offset|
        tdma\-tx\-size|
        tdma\-windfull|
        timestamp|
        too\-large|
        total\-entries|
        total\-hdd\-space|
        total\-memory|
        transport\-nexthop|
        tx\-1024\-1518|
        tx\-128\-255|
        tx\-1519\-max|
        tx\-256\-511|
        tx\-512\-1023|
        tx\-64|
        tx\-65\-127|
        tx\-align\-error|
        tx\-broadcast|
        tx\-bytes|
        tx\-ccq|
        tx\-evm\-ch0|
        tx\-evm\-ch1|
        tx\-evm\-ch2|
        tx\-fcs\-error|
        tx\-fragment|
        tx\-frames\-timed\-out|
        tx\-multicast|
        tx\-overflow|
        tx\-pause|
        tx\-rate|
        tx\-runt|
        tx\-signal\-strength\-ch0|
        tx\-signal\-strength\-ch1|
        tx\-signal\-strength\-ch2|
        tx\-signal\-strength|
        tx\-too\-long|
        udp\-dst\-port|
        udp\-src\-port|
        unknown\-server|
        unreachable|
        updates\-received|
        updates\-sent|
        up|
        uri|
        used\-hold\-time|
        used\-keepalive\-time|
        users|
        vlan\-protocol|
        vpls|
        wds|
        withdraws\-received|
        withdraws\-sent|
        wmm\-enabled|
        write\-sect\-since\-reboot|
        write\-sect\-total
        )(?!-)\b

  literal-boolean:
    patterns:
    - name: constant.language.mikrotik-script
      match: \b(true|false)\b
      comment: boolean

  literal-ip:
    patterns:
    - name: constant.other.ipv6.mikrotik-script
      match: \b((\h{1,4}\:){7}\h{1,4}|(\h{1,4}\:){1,7}\:|(\h{1,4}\:){1,6}\:\h{1,4}|(\h{1,4}\:){1,5}(\:\h{1,4}){1,2}|(\h{1,4}\:){1,4}(\:\h{1,4}){1,3}|(\h{1,4}\:){1,3}(\:\h{1,4}){1,4}|(\h{1,4}\:){1,2}(\:\h{1,4}){1,5}|\h{1,4}\:((\:\h{1,4}){1,6})|\:((\:\h{1,4}){1,7}|\:)|fe80\:(\:\h{,4}){,4}\%[0-9a-zA-Z]{1,}|\:\:(ffff(\:0{1,4})?\:)?((25[0-5]|(2[0-4]|1?[0-9])?[0-9]).){3}(25[0-5]|(2[0-4]|1?[0-9])?[0-9])|(\h{1,4}\:){1,4}\:((25[0-5]|(2[0-4]|1?[0-9])?[0-9]).){3}(25[0-5]|(2[0-4]|1?[0-9])?[0-9]))\b
      comment: IPv6 address, zero compressed IPv6 addresses, link-local IPv6 addresses with zone index, IPv4-Embedded IPv6 Address, IPv4-mapped IPv6 addresses, IPv4-translated addresses (http://stackoverflow.com/a/17871737/188530)

    - name: constant.other.ipv4.mikrotik-script
      match: \b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\/([0-9]|1[0-9]|2[0-4]))?\b
      comment: IPv4 address (http://stackoverflow.com/a/5284179/188530)

  literal-mac:
    patterns:
    - name: constant.other.mac.mikrotik-script
      match: \b(\h{2}[:-]){5}(\h{2})\b
      comment: MAC address (http://stackoverflow.com/a/4260512/188530)

  literal-date:
    patterns:
    - name: constant.other.time.mikrotik-script
      match: \b([1-9]+[0-9]*|0)(ms|s|m|h|d|w)\b
      comment: 1s, 2m, 3h, 4d

    - name: constant.other.time.mikrotik-script
      match: \b(([1-9]+[0-9]*w)?([1-9]+[0-9]*d)?([0-9]{2}:[0-9]{2}:[0-9]{2}))\b
      comment: 1w5d12:20:59

    - name: constant.other.date.mikrotik-script
      match: \b((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\/[0-9]{2}\/[1-9]+[0-9]*)\b

    - name: constant.other.time.delta.mikrotik-script
      match: ([\+\-]?[0-9]{2}:[0-9]{2})

  literal-number:
    patterns:
    - name: constant.numeric.integer.hexadecimal.mikrotik-script
      match: \b(?i:(0x\h*))\b
      comment: 64bit signed integer in hexadecimal form

    - name: constant.numeric.integer.decimal.mikrotik-script
      match: \b([1-9]+[0-9]*|0)\b
      comment: 64bit signed integer in decimal form

  variable:
    patterns:
    - name: variable.other.mikrotik-script
      match: (\$)([0-9a-zA-Z]+)
      captures:
        '1': {name: punctuation.definition.variable.mikrotik-script}

    - name: variable.other.mikrotik-script
      begin: (\$)(\")
      beginCaptures:
        '1': {name: punctuation.definition.variable.mikrotik-script}
        '2': {name: punctuation.definition.variable.begin.mikrotik-script}
      end: \"
      endCaptures:
        '0': {name: punctuation.definition.variable.end.mikrotik-script}
      patterns:
      - include: '#string-escape'

      - include: '#line-continuation'

      - name: invalid.illegal.newline.mikrotik-script
        match: \n

  variable-definition:
    patterns:
    - match: (\:)(global|local)\b
      captures:
        '1': {name: keyword.operator.other.mikrotik-script}
        '2': {name: storage.modifier.mikrotik-script}

  control-flow:
    patterns:
    - match: \b(from|to|step|in|do|else|while)\b([\s|\t]*)(=)
      captures:
        '1': {name: keyword.control.flow.mikrotik-script}
        '2': {name: invalid.illegal.whitespace.mikrotik-script}
        '3': {name: keyword.operator.comparison.mikrotik-script}

    - name: keyword.control.flow.mikrotik-script
      match: \b(while|for|foreach|on-error|if|do)\b

  operators:
    patterns:
    - name: keyword.operator.arithmetic.mikrotik-script
      match: \+|\-|\*|\/
      comment: arithmetic operators

    - name: keyword.operator.relational.mikrotik-script
      match: <|>|<=|>=
      comment: relational operators

    - name: keyword.operator.comparison.mikrotik-script
      match: =|!=
      comment: comparison operators

    - name: keyword.operator.logical.mikrotik-script
      match: \!|&&|\|\|
      comment: logical operators

    - name: keyword.operator.bitwise.mikrotik-script
      match: ~|\||\^|\&|<<|>>
      comment: bitwise operators

    - name: keyword.operator.concatenation.mikrotik-script
      match: \.|\,
      comment: concatenation operators

    - name: keyword.operator.other.mikrotik-script
      match: ->
      comment: access array element by key

    - name: keyword.operator.other.mikrotik-script
      match: :|\$|\/
      comment: delimeters

    - name: punctuation.terminator.statement.mikrotik-script
      match: ;

    - name: meta.brace.round.mikrotik-script
      match: \(|\)

    - name: meta.brace.curly.mikrotik-script
      match: \{|\}

    - name: meta.brace.square.mikrotik-script
      match: \[|\]

  string-escape:
    patterns:
    - name: constant.character.escape.mikrotik-script
      match: \\\"|\\\\|\\n|\\r|\\t|\\\$|\\\?|\\_|\\a|\\b|\\f|\\v|\\\h\h

  string-expression:
    patterns:
    - begin: \$\(
      end: \)
      patterns:
      - include: '$self'
      - include: '#line-continuation'
      - name: invalid.illegal.newline.mikrotik-script
        match: \n

    - begin: \$\[
      end: \]
      patterns:
      - include: '$self'
      - include: '#line-continuation'
      - name: invalid.illegal.newline.mikrotik-script
        match: \n

  line-continuation:
    patterns:
    - match: (\\)(.*)$\n?
      captures:
        '1': {name: punctuation.separator.continuation.line.mikrotik-script}
        '2': {name: invalid.illegal.unexpected-text.mikrotik-script}


File: /README.md
Syntax highlighting and completions for the [Mikrotik](http://mikrotik.com/) scripting language.


