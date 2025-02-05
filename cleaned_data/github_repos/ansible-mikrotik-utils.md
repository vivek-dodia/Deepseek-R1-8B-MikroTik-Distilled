# Repository Information
Name: ansible-mikrotik-utils

# Directory Structure
Directory structure:
└── github_repos/ansible-mikrotik-utils/
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
    │   │       ├── pack-0a6aa2fe2dc2f37572aeee03f22f83d844338ed2.idx
    │   │       └── pack-0a6aa2fe2dc2f37572aeee03f22f83d844338ed2.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── LICENSE.txt
    ├── mkr/
    │   ├── mkr_command.py
    │   ├── mkr_config.py
    │   └── module.py
    ├── README.md
    ├── setup.cfg
    ├── setup.py
    └── src/
        ├── ansible_mikrotik_utils/
        │   ├── base.py
        │   ├── commands/
        │   │   ├── backup.py
        │   │   ├── base.py
        │   │   ├── config.py
        │   │   ├── mixins.py
        │   │   ├── scheduler.py
        │   │   ├── script.py
        │   │   └── __init__.py
        │   ├── common.py
        │   ├── device/
        │   │   └── __init__.py
        │   ├── exceptions.py
        │   ├── mixins.py
        │   ├── objects.py
        │   ├── script.py
        │   ├── sections/
        │   │   ├── base.py
        │   │   ├── config.py
        │   │   ├── mixins.py
        │   │   ├── paths.py
        │   │   ├── scheduler.py
        │   │   ├── script.py
        │   │   └── __init__.py
        │   └── __init__.py
        └── tests/
            ├── test_config_compare.py
            └── __init__.py


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
	url = https://github.com/eden3d/ansible-mikrotik-utils.git
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
0000000000000000000000000000000000000000 de4f6d3221f5dad9a6446ec46052cb0f796af3fc vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/eden3d/ansible-mikrotik-utils.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 de4f6d3221f5dad9a6446ec46052cb0f796af3fc vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/eden3d/ansible-mikrotik-utils.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 de4f6d3221f5dad9a6446ec46052cb0f796af3fc vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/eden3d/ansible-mikrotik-utils.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
de4f6d3221f5dad9a6446ec46052cb0f796af3fc refs/remotes/origin/master
f89070b1c2a1459a0cfcc98a9571e15b10179edc refs/tags/v0.0.3


File: /.git\refs\heads\master
de4f6d3221f5dad9a6446ec46052cb0f796af3fc


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# Byte-compiled / optimized / DLL files
File: /LICENSE.txt
GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {one line to give the program's name and a brief idea of what it does.}
    Copyright (C) {year}  {name of author}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.



File: /mkr\mkr_command.py
#!/usr/bin/env python

# Main module handler
# =============================================================================

def main():
    argument_spec = dict(
        commands=dict(type='list', required=True),
        before=dict(type='list'),
        after=dict(type='list'),
    )
    module = MikrotikModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    commands = module.params['commands']
    before = module.params['before']
    after = module.params['after']

    with module:
        result = dict(changed=False)

        response, changes = module.execute(commands, before, after)

        if module.backup_name:
            result['backup_name'] = str(module.backup_name)
        result['history'] = list(module.history)

        result['response'] = str(response)
        result['changed'] = bool(changes)

        module.exit_json(**result)

# Imports
# =============================================================================

from ansible.module_utils.basic import *  # NOQA
from ansible_mikrotik_utils import MikrotikModule


if __name__ == '__main__':
    main()


File: /mkr\mkr_config.py
#!/usr/bin/env python

# Main module handler
# =============================================================================

def main():
    argument_spec = dict(
        config=dict(required=True),
        before=dict(type='list'),
        after=dict(type='list'),
    )
    module = MikrotikModule(
        argument_spec=argument_spec,
        supports_check_mode=True # oh yeah
    )
    config = module.params['config']
    before = module.params['before']
    after = module.params['after']

    result = dict(changed=False)

    response, changes = module.configure(config, before, after)
    updates = changes.export(pretty=True, header=False, blank=False)

    result['backup_name'] = str(module.backup_name)
    result['history'] = list(module.history)

    result['response'] = str(response)
    result['changed'] = bool(changes)
    result['updates'] = list(updates)

    module.exit_json(**result)

# Imports
# =============================================================================

from ansible.module_utils.basic import *  # NOQA
from ansible_mikrotik_utils import MikrotikModule


if __name__ == '__main__':
    main()


File: /mkr\module.py
import paramiko
import sys
import socket

from re import compile as compile_regex

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import env_fallback, get_exception
from ansible.module_utils.shell import Shell, ShellError

from ansible_mikrotik_utils.config import MikrotikConfig

from paramiko import AuthenticationException, SSHException, util
from getpass import getuser

if __debug__:
    paramiko.util.log_to_file('/dev/stderr')

# Constants
# =============================================================================

CLI_PROMPTS_RE = [
    compile_regex(r"\[([\w\-]+)@([\.\w\-]+)\]\s(\/(\w+\s?)*)?\>"),
]

CLI_ERRORS_RE = [
    compile_regex(r"failure: (.*)"),
    compile_regex(r"bad command name ([\w\-]+) \(line \d+ column \d+\)"),
    compile_regex(r"syntax error \(line \d+ column \d+\)"),
    compile_regex(r"expected end of command \(line \d+ column \d+\)"),
    compile_regex(r"expected command name \(line \d+ column \d+\)"),

]

NET_COMMON_ARGS = dict(
    host=dict(required=True),
    port=dict(default=22, type='int'),
    username=dict(fallback=(env_fallback, ['ANSIBLE_NET_USERNAME'])),
    password=dict(no_log=True, fallback=(env_fallback, ['ANSIBLE_NET_PASSWORD'])),
    ssh_keyfile=dict(fallback=(env_fallback, ['ANSIBLE_NET_SSH_KEYFILE']), type='path'),
    authorize=dict(default=False, fallback=(env_fallback, ['ANSIBLE_NET_AUTHORIZE']), type='bool'),
    auth_pass=dict(no_log=True, fallback=(env_fallback, ['ANSIBLE_NET_AUTH_PASS'])),
    provider=dict(),
    timeout=dict(default=10, type='int')
)

BACKUP_ARGS = dict(
    backup_name=dict(fallback=(env_fallback, ['MIKROTIK_BACKUP_NAME'])),
    backup_key=dict(no_log=True, fallback=(env_fallback, ['MIKROTIK_BACKUP_KEY'])),
)

RESTORE_ARGS = dict(
    restore_on_error=dict(default=False, fallback=(env_fallback, ['MIKROTIK_RESTORE_ON_ERROR']), type='bool'),
    restore_on_reboot=dict(default=False, fallback=(env_fallback, ['MIKROTIK_RESTORE_ON_REBOOT']), type='bool'),
    restore_on_timeout=dict(default=0, fallback=(env_fallback, ['MIKROTIK_RESTORE_ON_TIMEOUT']), type='int'),
)

# Utilities
# =============================================================================

def make_random_text(length=12):
    return ''.join(
        SystemRandom().choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(length)
    )

def make_random_name():
    return make_random_text(length=6)

def make_random_password():
    return make_random_text(length=16)


# Ansible module implementation
# =============================================================================

class MikrotikModule(AnsibleModule):

    # Class attributes and initializer
    # -------------------------------------------------------------------------
    config_class = MikrotikConfig
    catched_exceptions = SSHException, ShellError, IOError
    backup_extension = '.backup'
    pruned_sections = '/system scheduler',
    ssh_username_suffix = '+ct'

    def __init__(self, *args, **kwargs):
        kwargs['argument_spec'].update(NET_COMMON_ARGS)
        kwargs['argument_spec'].update(BACKUP_ARGS)
        kwargs['argument_spec'].update(RESTORE_ARGS)

        super(MikrotikModule, self).__init__(*args, **kwargs)

        self.__ssh = None
        self.__config = None
        self.__connected = False
        self.__protected = False
        self.__failed = False
        self.__disconnecting = False
        self.__history = list()
        self.___backup_name = None
        self.___backup_key = None

    # Public properties
    # -------------------------------------------------------------------------

    @property
    def connected(self):
        return self.__connected

    @property
    def protected(self):
        return self.__protected

    @property
    def history(self):
        return self.__history

    @property
    def backedup(self):
        return self.__backedup

    @property
    def config(self):
        if self.__config is None:
            self.__config = self.__export()
        return self.__config

    @property
    def backup_name(self):
        return self.___backup_name

    # Internal properties
    # -------------------------------------------------------------------------

    # SSH parameters

    @property
    def __ssh_host(self):
        return self.params['host']

    @property
    def __ssh_port(self):
        return self.params['port']

    @property
    def __ssh_username(self):
        username = self.params['username'] or getuser()
        if not username.endswith(self.ssh_username_suffix):
            username = ''.join((username, self.ssh_username_suffix))
        return username

    @property
    def __ssh_password(self):
        return self.params['password']

    @property
    def __ssh_timeout(self):
        return self.params['timeout']

    @property
    def __ssh_keyfile(self):
        return self.params['ssh_keyfile']

    # Backup

    @property
    def __protection_required(self):
        return any in (
            self.params['restore_on_error'],
            self.params['restore_on_reboot'],
            self.params['restore_on_timeout'],
        )

    @property
    def __backup_required(self):
        return self.__protection_required or self.params['backup_name']

    @property
    def __backup_name(self):
        if self.__backup_required and self.___backup_name is None:
            try:
                self.___backup_name = self.params['backup_name']
            except KeyError:
                self.___backup_name = make_random_name()
        return self.___backup_name

    @property
    def __backup_key(self):
        if self.__backup_required and self.___backup_key is None:
            try:
                self.___backup_key = self.params['backup_key']
            except KeyError:
                self.___backup_key = make_random_password()
        return self.___backup_key

    @property
    def __backup_path(self):
        if not self.__backup_name.endswith(self.backup_extension):
            return ''.join((self.__backup_name, self.backup_extension))
        else:
            return self.__backup_name

    @property
    def __backup_save_command(self):
        return SaveBackup(self.__backup_name, self.__backup_key)

    @property
    def __backup_load_command(self):
        return LoadBackup(self.__backup_name, self.__backup_key)

    @property
    def __backup_cleanup_command(self):
        return RemoveBackup(self.__backup_name)

    # Restore

    @property
    def __restore_tasks(self):
        if self.__restore_on_reboot:
            yield (
                'restore_on_reboot',
                'startup-time=reboot source="{}"'
                ''.format(self.__backup_load_command)
            )
        if self.__restore_on_timeout:
            yield (
                'restore_on_reboot',
                'interval={} source="{}"'
                ''.format(
                    timedelta(self.restore_on_timeout),
                    self.__backup_load_command
                )
            )


    # Module parameters handling
    # -------------------------------------------------------------------------

    def _load_params(self):
        super(MikrotikModule, self)._load_params()
        provider = self.params.get('provider') or dict()
        for key, value in provider.items():
            if key in NET_COMMON_ARGS:
                if self.params.get(key) is None and value is not None:
                    self.params[key] = value

    # Connection handling
    # -------------------------------------------------------------------------

    def __connect(self):
        if not self.__connected:
            self.__ssh = ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            look_for_keys = self.__ssh_password is None
            try:
                ssh.connect(
                        hostname=self.__ssh_host,
                        port=self.__ssh_port,
                        username=self.__ssh_username,
                        password=self.__ssh_password,
                        key_filename=self.__ssh_keyfile,
                        timeout=self.__ssh_timeout,
                        allow_agent=True, look_for_keys=False
                    )
                stdin, stdout, stderr = ssh.exec_command('test', timeout=self.__ssh_timeout)
                if "bad command name test (line 1 column 1)\n" not in stdout.readlines():
                    self.__fail("Connection test failed. (result:{})".format(stdout.readlines()))
            except socket.gaierror:
                self.__fail("Unable to resolve hostname. (host:{})".format(self.__ssh_host))
            except AuthenticationException:
                self.__fail("Unable to authenticate (user:{})".format(self.__ssh_user))
            except (SSHException, IOError) as ex:
                self.__fail("Unable to connect ({})".format(str(ex)))
            else:
                self.__connected = True
                self.__backedup = False

    def __disconnect(self):
        if self.__connected:
            self.__unprotect()
            self.__ssh.close()
            self.__ssh = None

    def __log_command(self, command):
        text = command.make_command_history_text()
        if text:
            self.__history.append("command: {}".format(text))

    def __log_response(self, command, response, error=False):
        text = command.make_response_history_text(response, error=error)
        if text:
            self.__history.append("{}: {}".format(
                'response' if not error else 'error', text
            ))

    def __fail_command(self, command, error):
        self.__log_response(command, error, error=True)
        if command.log_error_message:
            self.__fail(
                "Error detected in standard error.",
                command=command.history_text, error=error
            )
        else:
            self.__fail(
                "Error detected in standard error.",
                command=command.history_text
            )

    def __send(self, command):
        if not isinstance(command, ScriptCommand):
            command = RawCommand.parse(command)
        self.__connect()
        self.__log_command(command)
        stdin, stdout, stderr = self.__ssh.exec_command(command)
        stderr_read = stderr.read()
        if error:
            self.__fail_command(command, error)
        stdout_read = stdout.read()
        for pattern in CLI_ERRORS_RE:
            if pattern.match(stdout_read):
                self.__fail_command(command, response)
        self.__log_response(response)
        return response

    # Device protection handling
    # -------------------------------------------------------------------------

    def __protect(self):
        if self.__protection_required and not self.__protected:
            self.__backup()
            for name, args in self.__restore_tasks:
                self.__send('/system scheduler add name={} {}'.format(name, args))
            self.__protected = True

    def __unprotect(self):
        if self.__protection_required and not self.__protected:
            for name, args in self.__restore_tasks:
                self.__send('/system scheduler remove {}'.format(name, args))
            self.__protected = False
            self.__cleanup()

    # Backup handling
    # -------------------------------------------------------------------------

    def __backup(self):
        if self.__backup_required and not self.__backedup:
            self.__cleanup()
            self.__send(self.__backup_save_command)
            self.__backedup = True

    def __cleanup(self):
        if self.__backup_required and self.__backedup:
            self.__unprotect()
            self.__send(self.__backup_cleanup_command)
            self.__backedup = False

    # Restore
    # -------------------------------------------------------------------------

    def __restore(self):
        self.__send((self.__backup_load_command,))

    # Foobar
    # -------------------------------------------------------------------------

    def __fail(self, message, **kwargs):
        released, disconnected = False, False
        if not self.__failed:
            self.__failed = True
            self.__unprotect()
            self.__cleanup()
            released = True
        else:
            if not self.__disconnecting:
                self.__disconnecting = True
                self.__disconnect()
                disconnected = True
        self.fail_json(
            msg=message,
            released=released,
            disconnected=disconnected,
            **kwargs
        )

    # Configuration export by device
    # -------------------------------------------------------------------------

    def __export(self):
        self.__unprotect()
        text = self.__send(Export())
        return MikrotikConfig.parse(text, prune=self.pruned_sections)

    # Public methods (used by implemented CM modules)
    # -------------------------------------------------------------------------

    def execute(self, commands, before=None, after=None, no_log=False):
        commands, result = list(commands), None

        if commands and not self.check_mode:
            pre = self.config.copy()
            if before:
                for command in before:
                    self.__send(command)
            response = '\n'.join(map(self.__send, commands))
            if after:
                for command in after:
                    self.__send(command)
            self.__clear()
            post = self.config.copy()
            changes = pre.difference(post)
        else:
            response, changes = None, []

        return response, changes

    def configure(self, target, **kwargs):
        if not isinstance(target, MikrotikConfig):
            target = MikrotikConfig.parse(target)
        response = None

        original = self.config
        copy = original.copy()
        script = copy.merge(target)

        if script and not self.check_mode:
            response, changes = self.execute(script.commands, **kwargs)
            missing = original.apply(changes).difference(copy)
            if missing:
                self.__fail(
                    "Failed to reach target configuration",
                    history=self.history,
                    changes=list(changes.commands),
                    missing=list(missing.commands)
                )

        return response, changes

    def disconnect(self):
        self.__disconnect()

    # Context manager implementation
    # -------------------------------------------------------------------------

    def __enter__(self):
        self.__protect()
        self.__backup()

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_value is not None and False:
            self.__fail("Unknown {} error : {}".format(exc_type.__name__, str(exc_type)))
        self.__disconnect()


File: /README.md
ansible-mikrotik-utils
======================

This library provides a way to represent Mikrotik devices configuration and
determine the changes required to get the device to another configuration. This
makes it possible to properly manage Mikrotik devices from configuration
management tools, such as Ansible.

Current status
--------------

 - This is still a WIP, as indicated by the version number.
 - Two example modules are provided in `mkr`: mkr_config, and mkr_command
 - mkr_config provides a good example of the features of this library

 - the library uses a Python object structure to store the configuration, 
   and is able to merge and compare them.

More notes:

 - Mikrotik does not use a configuration file
 - The only way to completely configure a device (API has too much limitations) is by a sequence of commands passed to the interpreter
 - This is how export/import works

 - This means that the only way to represent a device's configuration is the sequence of commands that executed on it since the default configuration.
 - So, in order to make idempotent changes, we need to parse the existing sequence of commands, compare it to a target configuration, and determine the required commands to apply the change.
 - In order to do this, we need to parse some parts of the Mikrotik shell syntax (add/remove/move/set) and simulate its execution.

Install
-------

`pip install ansible-mikrotik-utils`

Documentation
-------------

TODO

License
-------

See `LICENSE.txt`.

Unit tests
----------

There is currently only a single unit test located in `src/test`.




File: /setup.cfg
[flake8]
ignore = E402

[pytest]
addopts= --doctest-modules -vvv --cov-config .coveragerc --cov=ansible_mikrotik_utils -s src/

[aliases]
test=pytest

[metadata]
description-file = README.md


File: /setup.py
#!/usr/bin/env python
from setuptools import setup, find_packages

# Root package meta-data
# ----------------------
_name = 'ansible-mikrotik-utils'
_version = '0.0.3'
_keywords = ['mikrotik', 'ansible', 'configuration']

# Pwackages
# --------

_packages = find_packages('src', exclude=("tests", "tests.*"))
_package_dir = {'ansible_mikrotik_utils': 'src/ansible_mikrotik_utils'}

# Additional meta-data
# --------------------
_codename = 'mikroshit'
_release = '-'.join([_version, _codename])
_description = (
    """This module provides code that can parse exported configurations from
    Mikrotik devices, and create the script that represents the necessary
    commands to reach a target configuration.

    This code is used by the `mkr_config` Ansible module, so that it can
    idempotently manage the configuration of Mikrotik routers.
    """
)
_author = 'EDEN 3D Engineering'
_author_email = 'contact@eden-3d.org'
_url = 'https://github.com/eden3d/ansible-mikrotik-utils'
_download_url = 'https://github.com/eden3d/ansible-mikrotik-utils/zipball/master'
_copyright = '2016, EDEN 3D Engineering'
_licence = 'GNU General Public Licence V3.0'
_classifiers = [
    'Development Status :: 4 - Beta',
    ('License :: OSI Approved :: '
     'GNU General Public License v3 or later (GPLv3+)'),
    'Programming Language :: Python :: 2.7',
]

# Tests
# -----

_setup_requires = [
    'pytest-runner',
]
_tests_require = [
    'pytest',
    'pytest-cov',
]

# Package setup
# -------------

setup(
    name=_name,
    version=_version,
    keywords=_keywords,
    packages=_packages,
    package_dir=_package_dir,
    description=_description,
    author=_author,
    author_email=_author_email,
    url=_url,
    download_url=_download_url,
    license=_licence,
    classifiers=_classifiers,
    setup_requires=_setup_requires,
    tests_require=_tests_require,
)


File: /src\ansible_mikrotik_utils\commands\backup.py
from ansible_mikrotik_utils.common import VALUES_RE, FILE_ID_RE
from ansible_mikrotik_utils.common import parse_values, format_values

from .base import BaseScriptCommand
from .mixins import StaticPathMixin, StaticCommandMixin


class BaseBackupCommand(StaticPathMixin, BaseScriptCommand):
    no_log_options = True

    path = '/system backup'
    options_pattern = VALUES_RE

    @classmethod
    def parse_match(cls, match):
        kwargs = super(BaseBackupCommand, cls).parse_match(match)
        kwargs['name'] = values['name']
        kwargs['key'] = values.get('key')
        return kwargs

    def __init__(self, name, key, *args, **kwargs):
        self.__name = name
        self.__key = key
        super().__init__(BaseBackupCommand, self)

    @property
    def name(self):
        return self.__name

    @property
    def key(self):
        return self.__key

    @property
    def options(self):
        values = dict(name=self.name)
        if self.key is not None:
            values[key] = self.key
        return ' '.join(format_values(values))


class SaveBackup(BaseBackupCommand):
    command = 'save'

    def apply(self, section):
        return section.device.add_backup(ConfigBackup(name=self.name, key=self.key))


class LoadBackup(BaseBackupCommand):
    command = 'load'

    def apply(self, section):
        return section.device.remove_backup(self.name)


class ClearBackup(StaticPathMixin, StaticCommandMixin, BaseScriptCommand):
    path = '/file'
    command = 'remove'
    options_re = FILE_ID_RE

    @classmethod
    def parse_match(cls, matched):
        for kwarg in super(ClearBackup, ).parse_match(matched):
            yield kwarg
        yield 'name', matched['filename']

    def __init__(self, name, *args, **kwargs):
        self.__name = name
        super(BackupCommand, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return self.__name

    @property
    def options(self, section):
        return self.name

    def apply(self, section):
        return section.device.remove_backup(self.name)


File: /src\ansible_mikrotik_utils\commands\base.py
from functools import partial
from inspect import isabstract
from abc import ABCMeta, abstractproperty, abstractmethod
from re import compile as compile_regex, MULTILINE, VERBOSE, DOTALL

from ansible_mikrotik_utils.common import format_censored, classproperty
from ansible_mikrotik_utils.common import abstractclassproperty
from ansible_mikrotik_utils.common import PATH_RE, COMMAND_RE, OPTIONS_RE, optional_re
from ansible_mikrotik_utils.mixins import SubclassStoreMixin

from .mixins import BaseCommandMixin, StaticCommandMixin

__all__ = [
    'CommandMeta',
    'BaseCommand',
    'BaseScriptCommand',
    'BaseConfigCommand',
]


class CommandMeta(SubclassStoreMixin, ABCMeta):
    static_path = False
    static_command = False
    static_options = False

    config_command = False
    script_command = False

    def get_type_sort_keys(cls, **kwargs):
        yield cls.static_path
        yield cls.static_command
        yield cls.static_options
        for key in super(CommandMeta, cls).get_type_sort_keys(**kwargs):
            yield key

    def get_type_filter_key(cls, **kwargs):
        try:
            only_script = kwargs.pop('only_script')
        except KeyError:
            only_script = False
        try:
            only_config = kwargs.pop('only_config')
        except KeyError:
            only_config = False
        if not super(CommandMeta, cls).get_type_filter_key(**kwargs):
            return False
        if only_script and not cls.sript_command:
            return False
        if only_config and not cls.config_command:
            return False
        return True


class BaseCommand(BaseCommandMixin):
    __metaclass__ = CommandMeta

    multiline = False
    hide = False

    no_log = False
    no_log_command = False
    no_log_options = False
    no_log_response = False
    no_log_error = False
    no_history = False

    default_path = '/'

    command_pattern = COMMAND_RE
    options_pattern = optional_re(OPTIONS_RE)

    # Matching/parsing
    # -------------------------------------------------------------------------

    @classproperty
    def pattern(cls):
        options = VERBOSE,
        if cls.multiline:
            options += MULTILINE, DOTALL
        return compile_regex("^(?P<text>{}\s*{})$".format(
            cls.command_pattern, cls.options_pattern
        ), *options)

    @classmethod
    def match(cls, text):
        return cls.pattern.match(text)

    @classmethod
    def parse_match(cls, match):
        return dict()

    @classmethod
    def parse(cls, match, **kwargs):
        matched = match.groupdict()
        parsed = dict(cls.parse_match(matched))
        parsed.update({key: value for key, value in kwargs.items() if value is not None})
        return cls(**parsed)

    # Initializer
    # -------------------------------------------------------------------------

    def __init__(self, path):
        super(BaseCommand, self).__init__(path)

    # Special methods
    # -------------------------------------------------------------------------

    def __str__(self):
        return self.text

    def __eq__(self, other):
        return self.full_command == other.full_command

    # History handling methods
    # -------------------------------------------------------------------------

    def make_command_history_text(self):
        if not self.no_history:
            if self.no_log or self.no_log_command:
                return format_censored(self.full_command)
            else:
                if self.no_log_options:
                    return ' '.join((
                        self.path,
                        self.command,
                        format(format_censored(self.options))
                    ))
                else:
                    return self.full_command

    def make_response_history_text(self, response, error=False):
        if not self.no_history:
            no_log = self.no_log_error if error else self.no_log_response
            if self.no_log or no_log:
                return format_censored(response)
            else:
                return response

    # Public properties
    # -------------------------------------------------------------------------

    @property
    def full_command(self):
        return ' '.join(filter(None, (self.command, self.options)))

    @property
    def text(self):
        return ' '.join(filter(None, (self.path, self.full_command)))

    # Implementation-dependent methods & properties
    # -------------------------------------------------------------------------

    @abstractproperty
    def command(self):
        pass

    @abstractproperty
    def options(self):
        pass

    @abstractproperty
    def options(self):
        pass


class BaseScriptCommand(BaseCommand):
    pass


class BaseConfigCommand(StaticCommandMixin, BaseCommand):
    @abstractclassproperty
    def entity_type(cls):
        pass

    @abstractmethod
    def apply(self, section):
        pass



File: /src\ansible_mikrotik_utils\commands\config.py
from itertools import chain
from shlex import split

from ansible_mikrotik_utils.common import VALUES_RE, INDEX_RE
from ansible_mikrotik_utils.common import DESTINATION_RE, IDENTIFIER_RE
from ansible_mikrotik_utils.common import parse_values, format_values, format_add_destination

from .base import BaseConfigCommand
from .mixins import InsertionMixin, DeletionMixin, MoveMixin, SettingMixin

__all__ = [
    'AddCommand',
    'RemoveCommand',
    'MoveCommand',
    'SetCommand'
]



class AddCommand(InsertionMixin, BaseConfigCommand):

    command = 'add'
    options_pattern = VALUES_RE

    @classmethod
    def parse_match(cls, matched):
        values = parse_values(split(matched['values']))
        try:
            destination = values.pop('place-before')
        except KeyError:
            destination = None
        kwargs = super(AddCommand, cls).parse_match(matched)
        kwargs['values'] = values
        kwargs['destination'] = destination
        return kwargs

    @property
    def require_numeric_ids(self):
        return self.destination is not None

    @property
    def options(self):
        return ' '.join(filter(None, chain(
            format_values(self.values),
            [format_add_destination(self.destination)]
        )))

    def apply(self, section):
        super(AddCommand, self).apply(section)
        section.insert_item(self.entity_type(self.values), destination=self.destination)

class RemoveCommand(DeletionMixin, BaseConfigCommand):
    command = 'remove'
    options_pattern = INDEX_RE

    @classmethod
    def parse_match(cls, matched):
        kwargs = super(RemoveCommand, cls).parse_match(matched)
        kwargs['index'] = int(matched['index'])
        return kwargs

    @property
    def options(self):
        return str(self.index)

    def apply(self, section):
        super(RemoveCommand, self).apply(section)
        return section.delete_item(section.items[self.index])

class MoveCommand(MoveMixin, BaseConfigCommand):
    command = 'move'
    options_pattern = '{}(\s{})?'.format(INDEX_RE, DESTINATION_RE)

    @classmethod
    def parse_match(cls, matched):
        kwargs = super(MoveCommand, cls).parse_match(matched)
        kwargs['index'] = int(matched['index'])
        kwargs['destination'] = int(matched['destination']) - 1
        return kwargs

    @property
    def options(self):
        if self.destination is not None:
            return ' '.join(map(str, (self.index, self.destination + 1)))
        else:
            return str(self.index)

    def apply(self, section):
        super(MoveCommand, self).apply(section)
        section.move_item(section.items[self.index], destination=self.destination)

class SetCommand(SettingMixin, BaseConfigCommand):
    command = 'set'
    options_pattern = '{}(\s{})'.format(IDENTIFIER_RE, VALUES_RE)

    @classmethod
    def parse_match(cls, matched):
        kwargs = super(SetCommand, cls).parse_match(matched)
        if matched['numeric_identifier']:
            kwargs['identifier'] = int(matched['numeric_identifier'])
        else:
            kwargs['identifier'] = matched['identifier']
        kwargs['values'] = parse_values(split(matched['values']))
        return kwargs

    @property
    def options(self):
        return ' '.join(filter(None, chain(
            [self.identifier],
            format_values(self.values)
        )))

    def apply(self, section):
        super(SetCommand, self).apply(section)
        section.set_settings(self.entity_type(self.identifier, self.values))


File: /src\ansible_mikrotik_utils\commands\mixins.py
from re import escape

from ansible_mikrotik_utils.common import classproperty, abstractclassmethod, abstractclassproperty
from ansible_mikrotik_utils.common import PATH_RE
from ansible_mikrotik_utils.mixins import BasePathMixin
from ansible_mikrotik_utils.mixins import StaticPathMixin as BaseStaticPathMixin
from ansible_mikrotik_utils.objects import ConfigItem, ConfigSetting


class BaseCommandMixin(BasePathMixin):

    static_command = False
    static_options = False

    @classproperty
    def greedy(cls):
        return not cls.static_path and not cls.static_command
    


class StaticPathMixin(BaseStaticPathMixin, BaseCommandMixin):
    pass


class StaticCommandMixin(BaseCommandMixin):

    static_command = True

    @abstractclassproperty
    def command(cls):
        pass

    @classproperty
    def command_pattern(cls):
        return '(?P<command>{})'.format(escape(cls.command))


class StaticOptionsMixin(BaseCommandMixin):

    static_options = True

    @abstractclassproperty
    def options(cls):
        pass

    @classproperty
    def options_pattern(cls):
        return '(?P<options>{})'.format(escape(cls.options))


class NoCommandMixin(StaticCommandMixin):
    command = ''


class NoOptionsMixin(StaticOptionsMixin):
    options = ''


class KeyValuePairsMixin(BaseCommandMixin):

    def __init__(self, values, *args, **kwargs):
        self.__values = values.copy()
        super(KeyValuePairsMixin, self).__init__(*args, **kwargs)

    @property
    def values(self):
        return self.__values


class ExistingItemMixin(BaseCommandMixin):

    require_numeric_ids = True

    def __init__(self, index, *args, **kwargs):
        self.__index = index
        super(ExistingItemMixin, self).__init__(*args, **kwargs)

    @property
    def index(self):
        return self.__index


class PositionedItemMixin(BaseCommandMixin):

    require_numeric_ids = True

    def __init__(self, *args, **kwargs):
        try:
            self.__destination = kwargs.pop('destination')
        except KeyError:
            self.__destination = None
        super(PositionedItemMixin, self).__init__(*args, **kwargs)

    @property
    def destination(self):
        return self.__destination


class DynamicIdentifierMixin(BaseCommandMixin):

    def __init__(self, identifier, *args, **kwargs):
        self.__identifier = identifier
        super(DynamicIdentifierMixin, self).__init__(*args, **kwargs)

    @property
    def identifier(self):
        return self.__identifier

    @property
    def require_numeric_ids(self):
        return isinstance(self.__identifier, int)


class InsertionMixin(PositionedItemMixin, KeyValuePairsMixin):
    entity_type = ConfigItem


class DeletionMixin(ExistingItemMixin):
    entity_type = ConfigItem


class MoveMixin(ExistingItemMixin, PositionedItemMixin):
    entity_type = ConfigItem


class SettingMixin(DynamicIdentifierMixin, KeyValuePairsMixin):
    entity_type = ConfigSetting


File: /src\ansible_mikrotik_utils\commands\scheduler.py
from ansible_mikrotik_utils.common import VALUES_RE, FILE_ID_RE
from ansible_mikrotik_utils.common import parse_values, format_values

from .base import BaseConfigCommand
from .mixins import StaticPathMixin
from .config import AddCommand, RemoveCommand


class BaseSchedulerCommand(StaticPathMixin, BaseConfigCommand):
    path = '/system scheduler'


class AddScheduledTask(AddCommand, BaseSchedulerCommand):

    def apply(self, section):
        section.device.add_task(
            name=self.name, source=self.source,
            start_time=self.start_time, interval=self.interval
        )
        return super(AddScheduledTask, self).apply(section)

    @property
    def name(self):
        return self.__values['name']

    @property
    def source(self):
        return self.__values['source']

    @property
    def start_time(self):
        return self.__values.get('start-time')

    @property
    def interval(self):
        return self.__values.get('interval')


class RemoveScheduledTask(RemoveCommand, BaseSchedulerCommand):

    def apply(self, section):
        section.device.remove_task(
            section.items[self.index].name
        )
        return super(RemoveScheduledTask, self).apply(section)


File: /src\ansible_mikrotik_utils\commands\script.py
from .mixins import StaticCommandMixin, StaticOptionsMixin
from .mixins import NoCommandMixin, NoOptionsMixin
from .base import BaseScriptCommand

__all__ = [
    'RawCommand',
    'Export',
    'Enumerate',
    'ChangeSection',
]

class RawCommand(BaseScriptCommand):
    @classmethod
    def parse_match(cls, matched):
        for kwarg in super(RawCommand, cls).parse_match(matched):
            yield kwarg
        yield 'command', matched['command']
        yield 'options', matched['options']

    def __init__(self, command, options, **kwargs):
        self.__command = command
        self.__options = options
        super(RawCommand, self).__init__(**kwargs)

    @property
    def command(self):
        return self.__command

    @property
    def options(self):
        return self.__options


class Export(StaticCommandMixin, BaseScriptCommand):
    no_log_response = True
    command = 'export'


class Enumerate(NoOptionsMixin, StaticCommandMixin, BaseScriptCommand):
    hide = True
    command = 'print'


File: /src\ansible_mikrotik_utils\commands\__init__.py
from .base import BaseCommand, BaseScriptCommand, BaseConfigCommand
from .script import RawCommand, Export, Enumerate
from .backup import SaveBackup, LoadBackup, ClearBackup
from .config import AddCommand, RemoveCommand, MoveCommand, SetCommand
from .scheduler import BaseSchedulerCommand, AddScheduledTask, RemoveScheduledTask






File: /src\ansible_mikrotik_utils\common.py
from collections import OrderedDict
from inspect import isabstract
from string import printable
from shlex import shlex
from enum import Enum
from abc import abstractproperty, abstractmethod


# Utilities
# -----------------------------------------------------------------------------

class AbstractMethodMixin(object):
    __isabstractmethod__ = True

    def __init__(self, func):
        func.__isabstractmethod__ = True
        super(AbstractMethodMixin, self).__init__(func)


class classproperty(object):
    def __init__(self, getter):
        self.getter = getter
        super(classproperty, self).__init__()

    def __get__(self, instance, owner):
        return self.getter(owner)


class abstractclassmethod(classmethod):

    __isabstractmethod__ = True

    def __init__(self, func):
        func.__isabstractmethod__ = True
        super(abstractclassmethod, self).__init__(func)


class abstractclassproperty(classmethod):

    __isabstractmethod__ = True

    def __init__(self, func):
        func = classproperty(func)
        func.__isabstractmethod__ = True
        super(abstractclassproperty, self).__init__(func)


def lookup_implementation(base, target, *args, **kwargs):
    # try base class first
    if not isabstract(base):
        return base
    # specific implementations are first, need to try generic first
    for klass in reversed(base.lookup_subclasses(*args, **kwargs)):
        if issubclass(klass, target):
            return klass
    # try target class
    if not isabstract(target):
        return target
    # oops
    raise TypeError("No implementation found.")


def join(*args):
    return ' '.join(map(str, args))


# Ordering handdling
# -----------------------------------------------------------------------------

class OrderMode(Enum):
    UNORDERED = 0
    ORDERED = 1
    ORDERED_APPEND = 2

    @property
    def ordered(self):
        return self in (self.ORDERED, self.ORDERED_APPEND)

    @property
    def ordered_insertion(self):
        return self == self.ORDERED

UNORDERED, ORDERED = OrderMode.UNORDERED, OrderMode.ORDERED
ORDERED_APPEND = OrderMode.ORDERED_APPEND


# Raw text parsing & formatting
# -----------------------------------------------------------------------------

def split_lines(text):
    line_lexer = shlex(text, posix=True)
    line_lexer.quotes = '"'
    line_lexer.whitespace = '\n;'
    line_lexer.wordchars = set(printable) - set(
        line_lexer.quotes + line_lexer.whitespace + line_lexer.escape
    )
    return list(line_lexer)

def parse_path(text):
    if text.startswith('/'):
        return text.lstrip('/'), True
    else:
        return text, False

def format_path(words):
    return '/{}'.format(' '.join(words))


def parse_value(word):
    parts = word.split('=')
    return parts[0], '='.join(parts[1:]).strip()

def parse_values(words):
    return OrderedDict(map(parse_value, words))

def format_value(value):
    return '='.join(value)

def format_values(values):
    return list(map(format_value, values.items()))

def format_add_destination(destination):
    if destination is not None:
        return 'place-before={}'.format(destination)
    else:
        return ''

def format_censored(text):
    lines = split_lines(text)
    if len(lines) > 1:
        return '<{} censored lines>'.format(len(lines))
    else:
        return '<{} censord characters>'.format(len(lines[0]))

# Patterns
# -----------------------------------------------------------------------------
TEXT_RE = "(?P<text>.*)"
NAME_RE = "(?P<name>[\w\-]+)"
NAMES_RE = "(?P<names>(\s?{})*)".format(NAME_RE)
VALUES_RE = "(?P<values>(([\w\-0-9]+)=(.*)\s?)+)"
INDEX_RE = "(?P<index>\d+)"
COMMAND_RE = "(?P<command>{}+)".format(NAME_RE)
OPTIONS_RE = "(?P<options>.+)"
DESTINATION_RE = "(?P<destination>\d+)"
NUMERIC_ID_RE = "(?P<numeric_identifier>[0-9]+)"
STRING_ID_RE = "(?P<string_identifier>[\w\-0-9_]+)"
FILE_ID_RE = "(?P<filename>[\w\-0-9_\.\@\=\+]+)"
DYNAMIC_CRITERIA_RE = "(?P<dynamic_criteria>([\w\-0-9]+)=(.*))"
ABSOLUTE_PATH_RE = "(?P<absolute>\/)"
PATH_RE = "(?P<path>{}?{})".format(ABSOLUTE_PATH_RE, NAMES_RE)
DYNAMIC_ID_RE = "(?P<dynamic_identifier>\[\s?find\s+({}\s?)+\s?\])".format(DYNAMIC_CRITERIA_RE)
IDENTIFIER_RE = "(?P<identifier>{}|{}|{})".format(NUMERIC_ID_RE, STRING_ID_RE, DYNAMIC_ID_RE)


optional_re = '({})?'.format


File: /src\ansible_mikrotik_utils\device\__init__.py
from ansible_mikrotik_utils.commands import SaveBackup, ClearBackup

from ansible_mikrotik_utils.sections import ConfigSection


class Device(object):
    def __init__(self):
        self.__section = ConfigSection(device=self)
        self.__backups = dict()
        self.__tasks = list()
        super(Device, self).__init__()

    # Backup handling
    # -------------------------------------------------------------------------

    def add_backup(self, backup):
        assert backup.name not in self.__backups, (
            "Cannot insert backup with existing name."
        )
        self.__backups[name] = backup.name
        return SaveBackup(name=backup.name, key=backup.key)

    def remove_backup(self, name):
        assert name in self.__backups.keys(), (
            "Cannot remove non-existing backup."
        )
        del self.__backups[name]
        return ClearBackup(name=name)

    # Task scheduler handling
    # -------------------------------------------------------------------------

    def add_scheduled_task(self, task):
        assert task.name in self.__backups.keys(), (
            "Cannot insert scheduled task with existing name."
        )
        self.__tasks[task.name] = task

    def remove_scheduled_task(self, name):
        assert name in self.__backups.keys(), (
            "Cannot remove non-existing scheduled task."
        )
        del self.__tasks[task.name]

    # Configuration input methods
    # -------------------------------------------------------------------------

    def load_text(self, text):
        return self.__section.load_text(text)

    def merge_text(self, text):
        return self.__section.load_text(text)

    def compare_text(self, text):
        other = ConfigSection.from_text(text, device=self)
        return self.__section.difference(other)

    def apply_script(self, script):
        self.__section.apply(script)

    # Public properties
    # -------------------------------------------------------------------------

    @property
    def root(self):
        return self.__section

    @property
    def sections(self):
        return {
            section.path: section for section in self.root.traverse()

        }





File: /src\ansible_mikrotik_utils\exceptions.py
class ParseError(ValueError):
    pass



File: /src\ansible_mikrotik_utils\mixins.py
from functools import partial
from itertools import chain
from weakref import ref, WeakSet
from inspect import isabstract
from abc import ABCMeta

from ansible_mikrotik_utils.common import NAME_RE, PATH_RE, UNORDERED
from ansible_mikrotik_utils.common import abstractclassproperty


class SubclassStoreMixin(type):
    __subclasses = None

    def get_type_filter_key(cls, **kwargs):
        return True

    def get_type_sort_keys(cls, **kwargs):
        yield - len(cls.mro())

    @property
    def _subclasses(cls):
        if cls.__subclasses is not None:
            for klass in cls.__subclasses:
                if issubclass(klass, cls):
                    yield klass

    def lookup_subclasses(cls, **kwargs):
        _filter = partial(filter, lambda x: bool(x.get_type_filter_key()))
        _sorted = partial(sorted, key=lambda x: tuple(x.get_type_sort_keys()), reverse=True)
        return list(_sorted(_filter(cls._subclasses)))

    def __init__(cls, name, bases, attrs):
        super(SubclassStoreMixin, cls).__init__(name, bases, attrs)
        if cls.__subclasses is None:
            cls.__subclasses = WeakSet()
        if not isabstract(cls):
            cls.__subclasses.add(cls)


class BaseMixin(object):
    __metaclass__ = ABCMeta

    @property
    def copy_kwargs(self):
        return {}

    @property
    def copy_args(self):
        return []


class OrderedMixin(BaseMixin):

    ordering_mode = UNORDERED

    # -------------------------------------------------------------------------

    @property
    def ordered(cls):
        return cls.ordering_mode.ordered

    @property
    def ordered_insertion(cls):
        return cls.ordering_mode.ordered_insertion


class CopiableMixin(BaseMixin):
    def copy(self, *args, **kwargs):
        combined_args = list(chain(args, self.copy_args))
        combined_kwargs = dict(self.copy_kwargs)
        combined_kwargs.update(kwargs)
        return type(self)(*combined_args, **combined_kwargs)


class BasePathMixin(BaseMixin):
    path_pattern = PATH_RE
    name_pattern = NAME_RE

    static_path = False
    __path = None

    def __init__(self, *args, **kwargs):
        args = list(args)
        try:
            path = args.pop(0)
        except IndexError:
            try:
                path = kwargs.pop('path')
            except KeyError:
                path = None
        if path is not None:
            if self.path is None:
                self.__path = path
            elif path != self.path:
                raise ValueError(
                    "The {} class already defines path as {}, cannot override to {}."
                    "".format(type(self).__name__, self.path, path)
                )
        elif self.path is None:
            raise ValueError("No path given")
        super(BasePathMixin, self).__init__(*args, **kwargs)

    @property
    def path(self):
        return self.__path

    @property
    def copy_kwargs(self):
        kwargs = super(BasePathMixin, self).copy_kwargs
        kwargs['path'] = self.path
        return kwargs


class StaticPathMixin(BasePathMixin):

    static_path = True

    @abstractclassproperty
    def path(cls):
        pass

    @abstractclassproperty
    def path_pattern(cls):
        return make_path_re(cls.path)






File: /src\ansible_mikrotik_utils\objects.py
from collections import OrderedDict
from itertools import chain

from ansible_mikrotik_utils.mixins import CopiableMixin
from ansible_mikrotik_utils.common import format_values


class ConfigItem(CopiableMixin):

    def __init__(self, values, *args, **kwargs):
        self.__values = values
        super(ConfigItem, self).__init__(*args, **kwargs)

    def __str__(self):
        return ' - {}'.format(format_values(self.values))

    def __repr__(self):
        return '<ConfigItem: {}>'.format(
            ' '.join(format_values(self.values))
        )

    def __eq__(self, other):
        return (
            other is not None and
            self.__values == other.values
        )

    def __ne__(self, other):
        return not self == other

    @property
    def copy_kwargs(self):
        kwargs = super(ConfigItem, self).copy_kwargs
        kwargs['values'] = self.values.copy()
        return kwargs

    @property
    def values(self):
        return self.__values


class ConfigSetting(ConfigItem):

    def __init__(self, identifier, *args, **kwargs):
        self.__identifier = identifier
        super(ConfigSetting, self).__init__(*args, **kwargs)

    def __str__(self):
        return '- {}: {}'.format(self.identifier, format_values(self.values))

    def __repr__(self):
        return '<ConfigSetting: {} {}>'.format(
            self.identifier, ' '.join(format_values(self.values))
        )

    def __eq__(self, other):
        return (
            super(ConfigSetting, self).__eq__(other) and
            other is not None and
            self.__identifier == other.identifier
        )

    @property
    def copy_args(self):
        args = super(ConfigSetting, self).copy_args
        args.append(self.identifier)
        return args

    @property
    def identifier(self):
        return self.__identifier


class ConfigBackup(CopiableMixin):

    def __init__(self, name, key, *args, **kwargs):
        self.__name = name
        self.__key = key
        super(ConfigBackup, self).__init__(*args, **kwargs)

    def __str__(self):
        return '@ backup: {}'.format(self.name)

    def __repr__(self):
        return '<ConfigBackup: {}>'.format(self.name)

    def __eq__(self, other):
        return self.__name == other.name

    @property
    def name(self):
        return self.__name

    @property
    def key(self):
        return self.__key

    @property
    def copy_kwargs(self):
        kwargs = super(ConfigBackup, self).copy_kwargs
        kwargs['name'] = self.name
        kwargs['key'] = self.key
        return kwargs


class ConfigTask(CopiableMixin):
    def __init__(self, name, source, *args, **kwargs):
        self.__name = name
        self.__source = source
        try:
            self.__interval = kwargs.pop('interval')
        except KeyError:
            self.__interval = None
        try:
            self.__start_time = kwargs.pop('start_time')
        except KeyError:
            self.__start_time = None
        if self.__interval is None and self.__start_time is None:
            raise TypeError("Scheduled task need an interval or start time.")
        super(ConfigTask, self).__init__(*args, **kwargs)

    def __str__(self):
        return '@ scheduled task: {}'.format(self.name)

    def __repr__(self):
        return '<ConfigTask: {}>'.format(self.name)

    def __eq__(self, other):
        return self.__name == other.name

    @property
    def copy_args(self):
        args = super(ConfigTask, self).copy_args
        args.append(self.name)
        args.append(self.source)
        return args

    @property
    def copy_kwargs(self):
        kwargs = super(ConfigTask, self).copy_args
        kwargs['interval'] = self.name
        kwargs['start_time'] = self.key
        return kwargs

    @property
    def name(self):
        return self.__name

    @property
    def source(self):
        return self.__source

    @property
    def interval(self):
        return self.__interval

    @property
    def start_time(self):
        return self.__start_time



File: /src\ansible_mikrotik_utils\sections\base.py
from collections import OrderedDict
from itertools import chain
from weakref import ref
from shlex import split
from abc import ABCMeta
from re import compile as compile_regex

from ansible_mikrotik_utils.exceptions import ParseError
from ansible_mikrotik_utils.mixins import SubclassStoreMixin
from ansible_mikrotik_utils.common import PATH_RE, classproperty, lookup_implementation
from ansible_mikrotik_utils.common import abstractclassproperty
from ansible_mikrotik_utils.common import format_path, split_lines, join
from ansible_mikrotik_utils.commands import BaseCommand

from .mixins import BaseSectionMixin


class SectionMeta(SubclassStoreMixin, ABCMeta):
    def get_type_sort_keys(cls, **kwargs):
        for key in super(SectionMeta, cls).get_type_sort_keys(**kwargs):
            yield key
        yield - len(cls.command_classes)

    def get_type_filter_key(cls, **kwargs):
        if not super(SectionMeta, cls).get_type_filter_key(**kwargs):
            return False
        return True


class BaseSection(BaseSectionMixin):
    __metaclass__ = SectionMeta

    # Implementation-defined types
    # -------------------------------------------------------------------------

    @abstractclassproperty
    def base_command_class(cls):
        pass

    @abstractclassproperty
    def base_section_class(cls):
        pass


    # Parsing
    # -------------------------------------------------------------------------

    @classmethod
    def parse_command(cls, text, *args, **kwargs):
        for cmd_cls in cls.command_classes:
            if not cmd_cls.greedy:
                match = cmd_cls.match(text)
                if match:
                    return cmd_cls.parse(match, *args, **kwargs)
        else:
            raise ParseError("Unknown command")

    @classmethod
    def from_text(cls, text, *args, **kwargs):
        new = cls(*args, **kwargs)
        new.load_text(text)
        return new

    # Specialization handling
    # -------------------------------------------------------------------------

    @classproperty
    def __path_pattern(cls):
        return compile_regex('^{}$'.format(cls.path_pattern))

    @classproperty
    def __name_pattern(cls):
        return compile_regex('^{}$'.format(cls.name_pattern))

    @classproperty
    def __base_section_class(cls):
        if cls.base_section_class is None:
            return cls
        else:
            return cls.base_section_class

    @classmethod
    def match_path(cls, text):
        return cls.__path_pattern.match(text)

    @classmethod
    def match_name(cls, text):
        return cls.__name_pattern.match(text)

    @classmethod
    def lookup_section_class(cls, path):
        for klass in reversed(cls.__base_section_class.lookup_subclasses()):
            if klass.match_path(path):
                return klass
        else:
            return cls

    # Command classes
    # -------------------------------------------------------------------------

    @classmethod
    def lookup_command_class(cls, target_klass, *args, **kwargs):
        return lookup_implementation(cls.base_command_class, target_klass, *args, **kwargs)

    @classproperty
    def command_class(cls):
        return cls.lookup_command_class(cls.base_command_class)

    @classproperty
    def command_classes(cls):
        return cls.base_command_class.lookup_subclasses()

    # Initializer
    # -------------------------------------------------------------------------

    def __init__(self, parent=None, name=None, commands=None,
                 children=None, device=None, path=None):
        if parent is not None:
            self.__parent_ref = ref(parent)
        else:
            self.__parent_ref = ref(self)

        if name is not None:
            self.__name = name
        elif self.static_path:
            self.__name = split(self.path)[0]
        else:
            self.__name = ''

        if self.path and not self.match_path(self.path):
            raise ValueError("Non-matching section path: {}".format(self.path))

        if device is not None:
            self.__device_ref = ref(device)
        elif parent is not None:
            self.__device_ref = None
        else:
            raise ValueError("Root section must be given a device.")

        if commands is not None:
            self.__commands = list(commands)
        else:
            self.__commands = list()

        if children is not None:
            self.__children = OrderedDict(
                (name, child.copy(parent=self))
                for name, child in children.items()
            )
        else:
            self.__children = OrderedDict()

        super(BaseSection, self).__init__(path=path)

    # Special methods
    # -------------------------------------------------------------------------

    def __str__(self):
        return '\n'.join(map(str, self.all_commands))

    def __nonzero__(self):
        return len(self.__commands)

    def __bool__(self):
        return self.__nonzero__()

    def __getitem__(self, name):
        try:
            child = self.__children[name]
        except KeyError as ex:
            if self.match_name(name):
                path = format_path(self.ascendant_names + [name])
                child = self.__children[name] = self.lookup_section_class(path)(self, name)
            else:
                raise
        return child

    def __iter__(self):
        return iter(self.all_commands)

    def __contains__(self, name):
        return name in self.__children

    # Copy protocol
    # -------------------------------------------------------------------------

    @property
    def copy_kwargs(self):
        kwargs = super(BaseSection, self).copy_kwargs
        kwargs['name'] = self.__name
        kwargs['commands'] = self.__commands
        if self.parent is self:
            kwargs['device'] = self.device
        kwargs['children'] = self.__children
        return kwargs

    # Input text
    # -------------------------------------------------------------------------

    def load_lines(self, lines):
        current = self

        for line in lines:
            if line.startswith('/'):
                current = self
                line = line.lstrip('/')
            words = list(split(line))
            while words:
                word = words.pop(0)
                try:
                    current = current.children[word]
                except KeyError:
                    pass
                else:
                    continue
                try:
                    command = current.parse_command(join(word, *words), path=current.path)
                except ParseError:
                    pass
                else:
                    current.load_command(command)
                    break
                try:
                    current = current[word]
                except KeyError:
                    pass
                else:
                    continue
                raise ParseError("Could not parse line: {} (in {})".format(repr(line), current.path))

    def load_text(self, text):
        return self.load_lines(map(str.strip, filter(None, split_lines(text))))

    def load_command(self, command):
        self.commands.append(command)

    # Tree traversal
    # -------------------------------------------------------------------------

    def traverse(self):
        yield self
        for child in self.__children.values():
            for grandchild in child.traverse():
                yield grandchild

    # Public properties
    # -------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name

    @property
    def commands(self):
        return self.__commands

    @property
    def all_commands(self):
        return list(chain(*(section.commands for section in self.traverse())))

    @property
    def children(self):
        return self.__children

    @property
    def parent(self):
        return self.__parent_ref()

    @property
    def device(self):
        if self.__device_ref is not None:
            return self.__device_ref()
        else:
            return self.parent.device

    # Public methods
    # -------------------------------------------------------------------------

    @property
    def ascendants(self):
        if self.parent is not None:
            if self.parent is not self:
                for ascendant in self.parent.ascendants:
                    yield ascendant
            yield self.parent

    @property
    def ascendant_names(self):
        return list(ascendant.name for ascendant in self.ascendants if ascendant.name)

    @property
    def path(self):
        return format_path(self.ascendant_names + [self.name])



File: /src\ansible_mikrotik_utils\sections\config.py
from collections import OrderedDict
from itertools import chain
from weakref import ref

from ansible_mikrotik_utils.common import classproperty, ORDERED

from ansible_mikrotik_utils.commands import BaseConfigCommand
from ansible_mikrotik_utils.commands import AddCommand, RemoveCommand
from ansible_mikrotik_utils.commands import MoveCommand, SetCommand

from .base import BaseSection
from .mixins import StaticPathMixin
from .script import ScriptSection



class ConfigSection(BaseSection):

    ordering_mode = ORDERED
    base_section_class = None
    base_command_class = BaseConfigCommand
    base_insertion_command_class = AddCommand
    base_deletion_command_class = RemoveCommand
    base_move_command_class = MoveCommand
    base_set_command_class = SetCommand

    # Command classes
    # -------------------------------------------------------------------------

    @classproperty
    def insertion_command_class(cls):
        return cls.lookup_command_class(cls.base_insertion_command_class)

    @classproperty
    def deletion_command_class(cls):
        return cls.lookup_command_class(cls.base_deletion_command_class)

    @classproperty
    def move_command_class(cls):
        return cls.lookup_command_class(cls.base_move_command_class)

    @classproperty
    def set_command_class(cls):
        return cls.lookup_command_class(cls.base_set_command_class)


    # Initializer
    # -------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        try:
            items = kwargs.pop('items')
        except KeyError:
            self.__items = list()
        else:
            self.__items = [item.copy() for item in items]
        try:
            settings = kwargs.pop('settings')
        except KeyError:
            self.__settings = OrderedDict()
        else:
            self.__settings = OrderedDict(
                (key, value.copy())
                for key, value in settings.items()
            )
        super(ConfigSection, self).__init__(*args, **kwargs)

    # Copy protocol
    # -------------------------------------------------------------------------

    @property
    def copy_kwargs(self):
        kwargs = super(ConfigSection, self).copy_kwargs
        kwargs['settings'] = OrderedDict(self.__settings)
        kwargs['items'] = list(self.__items)
        return kwargs

    # Raw change methods
    # -------------------------------------------------------------------------

    def __insert_item(self, item, destination=None):
        if destination is not None:
            self.__items.insert(destination, item)
        else:
            self.__items.append(item)

    def __delete_item(self, item):
        index = self.__items.index(item)
        self.__items.pop(index)
        return index

    def __move_item(self, item, destination=None):
        index = self.__delete_item(item)
        if destination is not None and index > destination:
            destination += 1
        self.__insert_item(item, destination)
        return index

    def __set_settings(self, settings):
        identifier = settings.identifier
        try:
            ours = self.settings[identifier]
        except KeyError:
            self.settings[identifier] = settings.copy()
            difference = settings.values
        else:
            difference = {
                key: value
                for key, value in settings.values.items()
                if ours.values.get(key) != value
            }
            ours.values.update(difference)
        return difference

    # Change methods
    # -------------------------------------------------------------------------

    def insert_item(self, item, destination=None):
        if destination is not None:
            assert self.ordered and self.ordered_insertion, (
                "Cannot use place-before if ordered insertion is disabled."
            )
            assert destination <= len(self.__items), (
                "Cannot insert at out of range destination: {} ({})"
                "".format(destination, len(self.__items))
            )
            if destination + 1 >= len(self.__items):
                destination = None
        assert item not in self.__items, (
            "Cannot insert duplicate item."
        )
        self.__insert_item(item, destination)
        return self.insertion_command_class(
            path=self.path,
            values=item.values,
            destination=destination
        )

    def delete_item(self, item):
        assert item in self.__items, (
            "Cannot delete non-existing item."
        )
        index = self.__delete_item(item)
        return self.deletion_command_class(
            path=self.path,
            index=index
        )

    def move_item(self, item, destination=None):
        if destination is not None:
            assert self.ordered, (
                "Cannot use move item if non-ordered section."
            )
            assert destination <= len(self.__items), (
                "Cannot move to out of range destination: {}"
                "".format(destination)
            )
            if destination + 1 >= len(self.__items):
                destination = None
        assert item in self.__items, (
            "Cannot move non-existing item."
        )
        index = self.__move_item(item, destination)
        return self.move_command_class(
            path=self.path,
            index=index,
            destination=destination
        )

    def set_settings(self, settings):
        values = self.__set_settings(settings)
        return self.set_command_class(
            path=self.path,
            identifier=settings.identifier,
            values=values
        )

    # Change application method
    # -------------------------------------------------------------------------

    def load_command(self, command):
        command.apply(self)
        super(ConfigSection, self).load_command(command)

    # Merging methods
    # -------------------------------------------------------------------------

    def __update_settings(self, target):
        for identifier, settings in target.__settings.items():
            if self.settings.get(identifier) != settings:
                yield self.set_settings(settings)

    def __delete_removed(self, target):
        index = 0
        while index < len(self.items):
            item = self.items[index]
            if item not in target.items:
                yield self.delete_item(item)
            else:
                index += 1

    def __insert_added(self, target):
        for index, item in enumerate(target.items):
            if item not in self.items:
                if self.ordered_insertion:
                    yield self.insert_item(item, index)
                else:
                    yield self.insert_item(item)

    def __update_positions(self, target):
        index = 0
        while index < len(self.items):
            item = self.items[index]
            destination = target.items.index(item)
            if index != destination:
                yield self.move_item(item, destination)
                if destination < (index - 1):
                    index += 1
            else:
                index += 1

    # Diff methods
    # -------------------------------------------------------------------------

    def __merge(self, target):
        for change in self.__update_settings(target):
            yield change
        for change in self.__delete_removed(target):
            yield change
        for change in self.__insert_added(target):
            yield change
        if self.ordered:
            for change in self.__update_positions(target):
                yield change

    def merge(self, section, parent=None):
        if parent is not None:
            script = ScriptSection(name=self.name, parent=parent)
        else:
            script = ScriptSection(name=self.name, device=self.device)
        for change in self.__merge(section):
            script.load_command(change)
        for name, child in section.children.items():
            script.children[name] = self[name].merge(child, parent=script)
        return script

    def difference(self, section):
        return self.copy().merge(section)

    def apply(self, script):
        for command in script.commands:
            command.apply(self)
        for name, child in section.children:
            self[name].apply(child)

    # Public properties
    # -------------------------------------------------------------------------

    @property
    def items(self):
        return self.__items

    @property
    def settings(self):
        return self.__settings


File: /src\ansible_mikrotik_utils\sections\mixins.py
from ansible_mikrotik_utils.common import abstractclassproperty
from ansible_mikrotik_utils.mixins import OrderedMixin, CopiableMixin
from ansible_mikrotik_utils.mixins import BasePathMixin
from ansible_mikrotik_utils.mixins import StaticPathMixin as BaseStaticPathMixin


class BaseSectionMixin(OrderedMixin, CopiableMixin, BasePathMixin):
    pass


class StaticPathMixin(BaseStaticPathMixin, BaseSectionMixin):
    pass



File: /src\ansible_mikrotik_utils\sections\scheduler.py
from ansible_mikrotik_utils.commands import BaseSchedulerCommand

from .mixins import StaticPathMixin
from . import BaseSection


class SchedulerSection(StaticPathMixin, BaseSection):
    path = '/system scheduler'
    base_command_class = BaseSchedulerCommand



File: /src\ansible_mikrotik_utils\sections\script.py
from ansible_mikrotik_utils.commands import BaseCommand


from .base import BaseSection

class ScriptSection(BaseSection):
    base_section_class = None
    base_command_class = BaseCommand


File: /src\ansible_mikrotik_utils\sections\__init__.py
from .base import BaseSection
from .script import ScriptSection
from .config import ConfigSection
from .scheduler import SchedulerSection


File: /src\ansible_mikrotik_utils\__init__.py




File: /src\tests\test_config_compare.py
from pytest import fixture

from ansible_mikrotik_utils.device import Device
from ansible_mikrotik_utils.sections import ConfigSection, ScriptSection

# Assets
# =============================================================================

CONFIG_BASE = """
/ip address
add address=192.168.88.1/24
add address=10.0.0.1 network=10.0.0.2

/ip firewall filter
add chain=test comment="1"
add chain=test comment="2"
add chain=test comment="3"
add chain=test comment="A"
add chain=test comment="B"
add chain=test comment="C"
add chain=test comment="D"
add chain=test comment="E"
add chain=test comment="4"
add chain=test comment="5"
add chain=test comment="6"

/interface bridge
set 0 wat=foo

"""

CONFIG_TARGET = """
/ip address
add address=192.168.88.1/24
add address=10.0.0.1 network=10.0.0.2

/ip firewall filter
add chain=test comment="foo"
add chain=test comment="C"
add chain=test comment="D"
add chain=test comment="A"
add chain=test comment="E"
add chain=test comment="B"
add chain=test comment="bar"

/interface bridge
set 0 wat=foo

"""

CONFIG_CHANGES = """
/ip firewall filter

remove 0
remove 0
remove 0
remove 5
remove 5
remove 5
add chain=test comment=foo place-before=0
add chain=test comment=bar
move 1 4
move 1 6
move 2 4
"""


# Fixtures
# =============================================================================

@fixture
def device():
    return Device()

@fixture
def config_base(device):
    return ConfigSection.from_text(CONFIG_BASE, device=device)

@fixture
def config_target(device):
    return ConfigSection.from_text(CONFIG_TARGET, device=device)

@fixture
def config_changes(device):
    return ScriptSection.from_text(CONFIG_CHANGES, device=device)

# Tests
# =============================================================================

def test_compare(config_base, config_target, config_changes):
    assert list(map(str, config_base.difference(config_target))) == list(map(str, config_changes))


