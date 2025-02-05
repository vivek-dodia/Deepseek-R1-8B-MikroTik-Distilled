# Repository Information
Name: MikrotikSSHPiano

# Directory Structure
Directory structure:
└── github_repos/MikrotikSSHPiano/
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
    │   │       ├── pack-de7cc1b9b6e8e68c63ac5b936ea6f3d86dc48576.idx
    │   │       └── pack-de7cc1b9b6e8e68c63ac5b936ea6f3d86dc48576.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── CMakeLists.txt
    ├── include/
    │   ├── KeyToNote.hpp
    │   ├── Mikrotik.hpp
    │   ├── ssh/
    │   │   ├── SshChannel.hpp
    │   │   ├── SshSession.hpp
    │   │   └── SshSocket.hpp
    │   └── SshWrapper.hpp
    ├── MikrotikSSHPiano.sln
    ├── README.md
    └── src/
        ├── KeyToNote.cpp
        ├── mikrotik-ssh-piano.cpp
        ├── Mikrotik.cpp
        ├── ssh/
        │   ├── SshChannel.cpp
        │   ├── SshSession.cpp
        │   └── SshSocket.cpp
        └── SshWrapper.cpp


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
	url = https://github.com/altucor/MikrotikSSHPiano.git
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
0000000000000000000000000000000000000000 d364e75aa855eb6a03714501d5b394ca8e58e476 vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/altucor/MikrotikSSHPiano.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d364e75aa855eb6a03714501d5b394ca8e58e476 vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/altucor/MikrotikSSHPiano.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d364e75aa855eb6a03714501d5b394ca8e58e476 vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/altucor/MikrotikSSHPiano.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d364e75aa855eb6a03714501d5b394ca8e58e476 refs/remotes/origin/master
2bde7b87495a91973a982a919ec12a76c4d38e63 refs/tags/1.0
2bde7b87495a91973a982a919ec12a76c4d38e63 refs/tags/1.0-static-link


File: /.git\refs\heads\master
d364e75aa855eb6a03714501d5b394ca8e58e476


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /CMakeLists.txt
cmake_minimum_required(VERSION 3.15.2)

project(mikrotik-ssh-piano C CXX)

IF(MSVC)
  set(PROJECT_NAME "${PROJECT_NAME}-win")
ELSEIF(APPLE)
  set(PROJECT_NAME "${PROJECT_NAME}-osx")
ELSEIF(UNIX)
  set(PROJECT_NAME "${PROJECT_NAME}-linux")
ENDIF()

set(REQUIRED_LIBSSH_VERSION 1.10.0)
IF(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc /MT")
ELSE()
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -static-libstdc++")
ENDIF(MSVC)

IF(CMAKE_BUILD_TYPE MATCHES Debug)
  message("Debug build.")
ELSEIF(CMAKE_BUILD_TYPE MATCHES Release)
  message("Release build.")
ELSE()
  message(" ! ! ! Unknown build type.")
ENDIF()

message("CMAKEFLAGS DUMP: ${CMAKE_CXX_FLAGS}")

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
  message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
  file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/v0.16.1/conan.cmake"
                "${CMAKE_BINARY_DIR}/conan.cmake"
                EXPECTED_HASH SHA256=396e16d0f5eabdc6a14afddbcfff62a54a7ee75c6da23f32f7a31bc85db23484
                TLS_VERIFY ON)
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_configure(REQUIRES libssh2/${REQUIRED_LIBSSH_VERSION}
                      GENERATORS cmake_find_package)

conan_cmake_autodetect(settings)

conan_cmake_install(PATH_OR_REFERENCE .
                    BUILD missing
                    REMOTE conancenter
                    SETTINGS ${settings})

find_package(Libssh2 REQUIRED)

include_directories("./")
include_directories("./include")

file(GLOB SOURCES 
    "./include/ssh/SshSocket.hpp"
    "./include/ssh/SshSession.hpp"
    "./include/ssh/SshChannel.hpp"
    "./include/KeyToNote.hpp"
    "./include/SshWrapper.hpp"
    "./include/Mikrotik.hpp"
    "./src/ssh/SshSocket.cpp"
    "./src/ssh/SshSession.cpp"
    "./src/ssh/SshChannel.cpp"
    "./src/KeyToNote.cpp"
    "./src/SshWrapper.cpp"
    "./src/Mikrotik.cpp"
    "./src/mikrotik-ssh-piano.cpp"
)

add_executable(${PROJECT_NAME} ${SOURCES})

IF(MSVC)
    set_property(
        TARGET 
        ${PROJECT_NAME} 
        PROPERTY 
        MSVC_RUNTIME_LIBRARY 
        "MultiThreaded$<$<CONFIG:>:>"
    )
ENDIF(MSVC)

include_directories(${Libssh2_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} Libssh2::libssh2)


File: /include\KeyToNote.hpp
#ifndef KEY_TO_NOTE_HPP
#define KEY_TO_NOTE_HPP

class KeyToNote
{
public:
	explicit KeyToNote();
	~KeyToNote();
	float keyToFreq(unsigned char key);
	void octaveUp();
	void octaveDown();
	int getCurOctave() { return m_octave; };

private:
	int m_octave = 5;
};

#endif // KEY_TO_NOTE_HPP


File: /include\Mikrotik.hpp
#ifndef MIKROTIK_HPP
#define MIKROTIK_HPP

#include "ssh/SshSession.hpp"

class Mikrotik
{
public:
	Mikrotik(
		std::string hostname, 
		const uint16_t port, 
		std::string username, 
		std::string password
	);
	int playNote(float freq, float length);
private:
	SshSession m_sshSession;
};


#endif // MIKROTIK_HPP


File: /include\ssh\SshChannel.hpp
#ifndef SSH_CHANNEL_HPP
#define SSH_CHANNEL_HPP

#include "libssh2.h"
#include "ssh/SshSession.hpp"

class SshChannel
{
public:
	SshChannel(SshSession &session, std::string ip, std::string port);
	~SshChannel();
private:
	LIBSSH2_CHANNEL *channel;
};

#endif // SSH_CHANNEL_HPP


File: /include\ssh\SshSession.hpp
#ifndef SSH_SESSION_HPP
#define SSH_SESSION_HPP

#include "libssh2.h"
#include <string>

class SshSession
{
public:
	SshSession(std::string hostname, const uint16_t port, std::string username, std::string password);
	~SshSession();
	int runCmd(std::string cmd, std::string &response);
private:
	int m_sock = 0;
	LIBSSH2_SESSION *m_session = NULL;
};

#endif // SSH_SESSION_HPP


File: /include\ssh\SshSocket.hpp
#ifndef SSH_SOCKET_HPP
#define SSH_SOCKET_HPP

class SshSocket
{
public:
	SshSocket(/* args */);
	~SshSocket();
private:
	/* data */
};

SshSocket::SshSocket(/* args */)
{
}

SshSocket::~SshSocket()
{
}

#endif // SSH_SOCKET_HPP


File: /include\SshWrapper.hpp
#ifndef SSH_WRAPPER_HPP
#define SSH_WRAPPER_HPP

#include "libssh2.h"

class SshWrapper
{
public:
	explicit SshWrapper(std::string &user, std::string &ip, uint16_t port = 22);
	~SshWrapper();
	void playNote(float freq, float length);

private:
	std::string m_user = "";
	std::string m_ip = "";
	uint16_t m_port = 22;
	LIBSSH2_SESSION *m_session;

private:
	std::string m_getpass(const char *prompt, bool show_asterisk = true);
	int m_runCmd(std::string &cmd);
};

#endif // SSH_WRAPPER_HPP


File: /MikrotikSSHPiano.sln
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio 15
VisualStudioVersion = 15.0.27130.2003
MinimumVisualStudioVersion = 10.0.40219.1
Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "MikrotikSSHPiano", "MikrotikSSHPiano\MikrotikSSHPiano.vcxproj", "{27568AC1-DB41-472D-8F35-F062F9B8BBE2}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|x64 = Debug|x64
		Debug|x86 = Debug|x86
		Release|x64 = Release|x64
		Release|x86 = Release|x86
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Debug|x64.ActiveCfg = Debug|x64
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Debug|x64.Build.0 = Debug|x64
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Debug|x86.ActiveCfg = Debug|Win32
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Debug|x86.Build.0 = Debug|Win32
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Release|x64.ActiveCfg = Release|x64
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Release|x64.Build.0 = Release|x64
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Release|x86.ActiveCfg = Release|Win32
		{27568AC1-DB41-472D-8F35-F062F9B8BBE2}.Release|x86.Build.0 = Release|Win32
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {5A35074E-EC56-497A-AB43-172152FFA996}
	EndGlobalSection
EndGlobal


File: /README.md
# Mikrotik SSH Piano

That program allows you play on mikrotik beeper like on piano or one voice synth. All is works over SSH session.

## Requirements
That project uses libssh for windows. So you need dll's from libssh. Precompiled dll's are available in Debug folder, also u can download Debug folder and enjoy using it!

## Arguments 
* First argument - username
* Second argument - router ip
* Third - ssh port on router
* Example: **MikrotikSSHPiano.exe admin 192.168.0.1 22** 

## Keyboard markdown
Keyboard markdown same as in FL Studio. In FL you can use it, when you turn on feature "Typing keyboard to piano keyboard".
http://flstudio.image-line.com/help/html/img_glob/qwerty_keyboard.jpg

		+--------------------------------------------------------------------------+
		|  Octave N+1                                                              |
		|       +---+       +---+             +---+       +---+       +---+        |
		| +---+ | 2 | +---+ | 3 | +---+ +---+ | 5 | +---+ | 6 | +---+ | 7 | +---+  |
		| ||Q|| +---+ ||W|| +---+ ||E|| ||R|| +---+ ||T|| +---+ ||Y|| +---+ ||U||  |
		| +---+       +---+       +---+ +---+       +---+       +---+       +---+  |
		|                                                                          |
		+--------------------------------------------------------------------------+
		|  Octave N                                                                |
		|       +---+       +---+             +---+       +---+       +---+        |
		| +---+ | S | +---+ | D | +---+ +---+ | G | +---+ | H | +---+ | J | +---+  |
		| ||Z|| +---+ ||X|| +---+ ||C|| ||V|| +---+ ||B|| +---+ ||N|| +---+ ||M||  |
		| +---+       +---+       +---+ +---+       +---+       +---+       +---+  |
		+--------------------------------------------------------------------------+
		|                                                                          |
		| +----------------------------------+      +-+-+ Current +-+-+            |
		| |               Exit               |      | + |    4    | - |            |
		| +----------------------------------+      +-+-+         +-+-+            |
		|                                                                          |
		|                                         Octave Up    Octave Down         |
		|                                                                          |
		+--------------------------------------------------------------------------+


File: /src\KeyToNote.cpp
#include "KeyToNote.hpp"

#include <iostream>
#include <string>
#include <vector>
#include <map>

const unsigned int notesInOctave = 12;

enum Notes{
	KEY_C,
	KEY_C_SHARP,
	KEY_D,
	KEY_Eb,
	KEY_E,
	KEY_F,
	KEY_F_SHARP,
	KEY_G,
	KEY_G_SHARP,
	KEY_A,
	KEY_Bb,
	KEY_B
};

std::vector<std::string> m_symbolicNotes = { 
	"C 0", "C# 0", "D 0", "Eb 0", "E 0", "F 0", "F# 0", "G 0", "G# 0", "A 0", "Bb 0", "B 0",  /* #0 */
	"C 1", "C# 1", "D 1", "Eb 1", "E 1", "F 1", "F# 1", "G 1", "G# 1", "A 1", "Bb 1", "B 1",  /* #1 */
	"C 2", "C# 2", "D 2", "Eb 2", "E 2", "F 2", "F# 2", "G 2", "G# 2", "A 2", "Bb 2", "B 2",  /* #2 */
	"C 3", "C# 3", "D 3", "Eb 3", "E 3", "F 3", "F# 3", "G 3", "G# 3", "A 3", "Bb 3", "B 3",  /* #3 */
	"C 4", "C# 4", "D 4", "Eb 4", "E 4", "F 4", "F# 4", "G 4", "G# 4", "A 4", "Bb 4", "B 4",  /* #4 */
	"C 5", "C# 5", "D 5", "Eb 5", "E 5", "F 5", "F# 5", "G 5", "G# 5", "A 5", "Bb 5", "B 5",  /* #5 */
	"C 6", "C# 6", "D 6", "Eb 6", "E 6", "F 6", "F# 6", "G 6", "G# 6", "A 6", "Bb 6", "B 6",  /* #6 */
	"C 7", "C# 7", "D 7", "Eb 7", "E 7", "F 7", "F# 7", "G 7", "G# 7", "A 7", "Bb 7", "B 7",  /* #7 */
	"C 8", "C# 8", "D 8", "Eb 8", "E 8", "F 8", "F# 8", "G 8", "G# 8", "A 8", "Bb 8", "B 8",  /* #8 */
	"C 9", "C# 9", "D 9", "Eb 9", "E 9", "F 9", "F# 9", "G 9", "G# 9", "A 9", "Bb 9", "B 9"   /* #9 */
};

std::vector<double> m_freqNotes = {
	8.18,    8.66,    9.18,    9.72,    10.30,   10.91,     11.56,    12.25,   12.98,   13.75,  14.57,   15.43,    /* #0 */
	16.35,   17.32,   18.35,   19.45,   20.60,   21.83,     23.12,    24.50,   25.96,   27.50,  29.14,   30.87,    /* #1 */
	32.70,   34.65,   36.71,   38.89,   41.20,   43.65,     46.25,    49.0,    51.91,   55.0,   58.27,   61.74,    /* #2 */
	65.41,   69.30,   73.42,   77.78,   82.41,   87.31,     92.50,    98.0,    103.83,  110.0,  116.54,  123.47,   /* #3 */
	130.81,  138.59,  146.83,  155.56,  164.81,  174.61,    185.0,    196.0,   207.65,  220.0,  233.08,  246.94,   /* #4 */
	261.63,  277.18,  293.66,  311.13,  329.63,  349.23,    369.99,   392.0,   415.30,  440.0,  466.16,  493.88,   /* #5 */
	523.25,  554.37,  587.33,  622.25,  659.25,  698.46,    739.99,   783.99,  830.61,  880.0,  932.33,  987.77,   /* #6 */
	1046.5,  1108.73, 1174.66, 1244.51, 1318.51, 1396.91,   1479.98,  1567.98, 1661.22, 1760.0, 1864.66, 1975.53,  /* #7 */
	2093.0,  2217.46, 2349.32, 2489.02, 2637.02, 2793.83,   2959.96,  3135.96, 3322.44, 3520.0, 3729.31, 3951.07,  /* #8 */
	4186.01, 4434.92, 4698.63, 4978.03, 5274.04, 5587.65,   5919.91,  6271.93, 6644.88, 7040.0, 7458.62, 7902.13   /* #9 */
};

std::map<unsigned char, int> octaveMapLow = {
	{ 122, KEY_C, },		// "z" btn
	{ 115, KEY_C_SHARP, },	// "s" btn
	{ 120, KEY_D, },		// "x" btn
	{ 100, KEY_Eb, },		// "d" btn
	{ 99,  KEY_E, },		// "c" btn
	{ 118, KEY_F, },		// "v" btn
	{ 103, KEY_F_SHARP, },	// "g" btn
	{ 98,  KEY_G, },		// "b" btn
	{ 104, KEY_G_SHARP, },	// "h" btn
	{ 110, KEY_A, },		// "n" btn
	{ 106, KEY_Bb, },		// "j" btn
	{ 109, KEY_B },			// "m" btn
};

std::map<unsigned char, int> octaveMapHigh = {
	{ 113, KEY_C, },		// "q" btn
	{ 50,  KEY_C_SHARP, },	// "2" btn
	{ 119, KEY_D, },		// "w" btn
	{ 51,  KEY_Eb, },		// "3" btn
	{ 101, KEY_E, },		// "e" btn
	{ 114, KEY_F, },		// "r" btn
	{ 53,  KEY_F_SHARP, },	// "5" btn
	{ 116, KEY_G, },		// "t" btn
	{ 54,  KEY_G_SHARP, },	// "6" btn
	{ 121, KEY_A, },		// "y" btn
	{ 55,  KEY_Bb, },		// "7" btn
	{ 117, KEY_B },			// "u" btn
};

KeyToNote::KeyToNote()
{
}


KeyToNote::~KeyToNote()
{
}

float KeyToNote::keyToFreq(unsigned char key)
{
	float freq = 0.0f;
	int noteKey = 0;
	int freqPos = 0;
	auto itOctLow = octaveMapLow.find(key);
	auto itOctHigh = octaveMapHigh.find(key);
	
	if (itOctLow == octaveMapLow.end() && itOctHigh == octaveMapHigh.end())
		return 0.0f;

	if (itOctLow != octaveMapLow.end()) {
		noteKey = itOctLow->second;
		freqPos = noteKey + (notesInOctave * m_octave);
	} else if (itOctHigh != octaveMapHigh.end()) {
		noteKey = itOctHigh->second;
		freqPos = noteKey + (notesInOctave * (m_octave + 1));
	}

	
	if(freqPos < m_freqNotes.size())
		freq = m_freqNotes[freqPos];

	return freq;
}

void KeyToNote::octaveUp()
{
	if(m_octave < 9)
		m_octave++;
}

void KeyToNote::octaveDown()
{
	if(m_octave > 1)
		m_octave--;
}


File: /src\Mikrotik.cpp
#include "Mikrotik.hpp"

Mikrotik::Mikrotik(
		std::string hostname, 
		const uint16_t port, 
		std::string username, 
		std::string password
) : m_sshSession(hostname, port, username, password)
{
	
}

int Mikrotik::playNote(float freq, float length)
{
	std::string cmd = "beep";
	cmd.append(" frequency=" + std::to_string(freq));
	cmd.append(" length=" + std::to_string(length));

	std::string reposnse;
	return m_sshSession.runCmd(cmd, reposnse);
}


File: /src\ssh\SshChannel.cpp
#include "ssh/SshChannel.hpp"

SshChannel::SshChannel(SshSession &session, std::string ip, std::string port)
{
	
}


File: /src\ssh\SshSession.cpp
#include "ssh/SshSession.hpp"

#include <stdexcept>

static int waitsocket(int socket_fd, LIBSSH2_SESSION *session)
{
	struct timeval timeout;
	int rc;
	fd_set fd;
	fd_set *writefd = NULL;
	fd_set *readfd = NULL;
	int dir;

	timeout.tv_sec = 10;
	timeout.tv_usec = 0;
	FD_ZERO(&fd);
	FD_SET(socket_fd, &fd);

	/* now make sure we wait in the correct direction */
	dir = libssh2_session_block_directions(session);
	if(dir & LIBSSH2_SESSION_BLOCK_INBOUND)
		readfd = &fd;
	if(dir & LIBSSH2_SESSION_BLOCK_OUTBOUND)
		writefd = &fd;
	rc = select(socket_fd + 1, readfd, writefd, NULL, &timeout);
	return rc;
}

SshSession::SshSession(std::string hostname, const uint16_t port, std::string username, std::string password)
{
#ifdef WIN32
	WSADATA wsadata;
	int err = WSAStartup(MAKEWORD(2, 0), &wsadata);
	if(err != 0)
		throw std::runtime_error("WSAStartup failed");
#endif
	uint32_t hostaddr = inet_addr(hostname.data());
	m_sock = socket(AF_INET, SOCK_STREAM, 0);

	struct sockaddr_in sin;
	sin.sin_family = AF_INET;
	sin.sin_port = htons(port);
	sin.sin_addr.s_addr = hostaddr;
	if(connect(m_sock, (struct sockaddr*)(&sin), sizeof(struct sockaddr_in)) != 0)
	{
		throw std::runtime_error("Error failed to connect to socket");
	}

	m_session = libssh2_session_init();
	if(!m_session)
		throw std::runtime_error("Error libssh2_session_init");
	libssh2_session_set_blocking(m_session, 0);
	int rc = 0;
	while((rc = libssh2_session_handshake(m_session, m_sock)) == LIBSSH2_ERROR_EAGAIN);
	if(rc)
		throw std::runtime_error("Failure establishing SSH session");
	
	LIBSSH2_KNOWNHOSTS *nh = libssh2_knownhost_init(m_session);
	if(!nh)
		throw std::runtime_error("Failure libssh2_knownhost_init");

	/* read all hosts from here */
	libssh2_knownhost_readfile(nh, "known_hosts", LIBSSH2_KNOWNHOST_FILE_OPENSSH);

	/* store all known hosts to here */
	libssh2_knownhost_writefile(nh, "dumpfile", LIBSSH2_KNOWNHOST_FILE_OPENSSH);

	int type;
	std::size_t len;
	const char *fingerprint = libssh2_session_hostkey(m_session, &len, &type);
	if(fingerprint)
	{
		struct libssh2_knownhost *host;
		int check = libssh2_knownhost_checkp(
			nh,
			hostname.data(), 
			port,
			fingerprint, 
			len,
			LIBSSH2_KNOWNHOST_TYPE_PLAIN | LIBSSH2_KNOWNHOST_KEYENC_RAW,
			&host
		);

		//fprintf(stderr, "Host check: %d, key: %s\n", check,
		//		(check <= LIBSSH2_KNOWNHOST_CHECK_MISMATCH)?
		//		host->key:"<none>");

		/*****
		 * At this point, we could verify that 'check' tells us the key is
		 * fine or bail out.
		 *****/
	}
	else
	{
		throw std::runtime_error("Failure libssh2_session_hostkey");
	}
	libssh2_knownhost_free(nh);

	if(password.size() != 0) {
		/* We could authenticate via password */
		while((rc = libssh2_userauth_password(m_session, username.data(), password.data())) ==
			   LIBSSH2_ERROR_EAGAIN);
		if(rc) {
			throw std::runtime_error("Authentication by password failed");
		}
	}
	else {
		/* Or by public key */
		while((rc = libssh2_userauth_publickey_fromfile(
			m_session, username.data(),
			"/home/user/"
			".ssh/id_rsa.pub",
			"/home/user/"
			".ssh/id_rsa",
			password.data())) == LIBSSH2_ERROR_EAGAIN);
		if(rc) {
			throw std::runtime_error("Authentication by public key failed");
		}
	}

}

SshSession::~SshSession()
{
	libssh2_session_disconnect(m_session, "Normal Shutdown, Thank you for playing");
	libssh2_session_free(m_session);
#ifdef WIN32
	closesocket(m_sock);
#else
	close(m_sock);
#endif
}

int SshSession::runCmd(std::string cmd, std::string &response)
{
	char *exitsignal = (char *)"none";
	int exitcode = 0;
	LIBSSH2_CHANNEL *channel;
	while((channel = libssh2_channel_open_session(m_session)) == NULL &&
		  libssh2_session_last_error(m_session, NULL, NULL, 0) ==
		  LIBSSH2_ERROR_EAGAIN) {
		waitsocket(m_sock, m_session);
	}
	if(channel == NULL) {
		fprintf(stderr, "Error\n");
		exit(1);
	}
	int rc = 0;
	while((rc = libssh2_channel_exec(channel, cmd.data())) ==
		   LIBSSH2_ERROR_EAGAIN) {
		waitsocket(m_sock, m_session);
	}
	if(rc != 0) {
		fprintf(stderr, "Error\n");
		exit(1);
	}
	int bytecount = 0;
	for(;;) {
		/* loop until we block */
		int rc;
		do {
			char buffer[0x4000];
			rc = libssh2_channel_read(channel, buffer, sizeof(buffer) );
			if(rc > 0) {
				int i;
				bytecount += rc;
				fprintf(stderr, "We read:\n");
				for(i = 0; i < rc; ++i)
					fputc(buffer[i], stderr);
				fprintf(stderr, "\n");
			}
			else {
				if(rc != LIBSSH2_ERROR_EAGAIN)
					/* no need to output this for the EAGAIN case */
					fprintf(stderr, "libssh2_channel_read returned %d\n", rc);
			}
		}
		while(rc > 0);

		/* this is due to blocking that would occur otherwise so we loop on
		   this condition */
		if(rc == LIBSSH2_ERROR_EAGAIN) {
			waitsocket(m_sock, m_session);
		}
		else
			break;
	}
	exitcode = 127;
	while((rc = libssh2_channel_close(channel)) == LIBSSH2_ERROR_EAGAIN)
		waitsocket(m_sock, m_session);

	if(rc == 0) {
		exitcode = libssh2_channel_get_exit_status(channel);
		libssh2_channel_get_exit_signal(channel, &exitsignal,
										NULL, NULL, NULL, NULL, NULL);
	}

	if(exitsignal)
		fprintf(stderr, "\nGot signal: %s\n", exitsignal);
	else
		fprintf(stderr, "\nEXIT: %d bytecount: %d\n", exitcode, bytecount);

	libssh2_channel_free(channel);
	channel = NULL;
	return 0;
}


File: /src\SshWrapper.cpp
#include <iostream>
#include <string>

#include <io.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>


#include "SshWrapper.hpp"

SshWrapper::SshWrapper(std::string &user, std::string &ip, uint16_t port)
	: m_user(user),
	m_ip(ip),
	m_port(port)
{

}


SshWrapper::~SshWrapper()
{

}


std::string SshWrapper::m_getpass(const char *prompt, bool show_asterisk)
{
	const char BACKSPACE = 8;
	const char RETURN = 13;

	std::string password;
	unsigned char ch = 0;

	std::cout << prompt << std::endl;

	DWORD con_mode;
	DWORD dwRead;

	HANDLE hIn = GetStdHandle(STD_INPUT_HANDLE);

	GetConsoleMode(hIn, &con_mode);
	SetConsoleMode(hIn, con_mode & ~(ENABLE_ECHO_INPUT | ENABLE_LINE_INPUT));

	while (ReadConsoleA(hIn, &ch, 1, &dwRead, NULL) && ch != RETURN)
	{
		if (ch == BACKSPACE)
		{
			if (password.length() != 0)
			{
				if (show_asterisk)
					std::cout << "\b \b";
				password.resize(password.length() - 1);
			}
		}
		else
		{
			password += ch;
			if (show_asterisk)
				std::cout << '*';
		}
	}
	std::cout << std::endl;
	return password;
}

int SshWrapper::m_runCmd(std::string &cmd)
{
	return -1;
}

void SshWrapper::playNote(float freq, float length)
{
	std::string cmd = "beep";
	cmd.append(" frequency=" + std::to_string(freq));
	cmd.append(" length=" + std::to_string(length));

	std::cout << cmd << std::endl;
	m_runCmd(cmd);
}






