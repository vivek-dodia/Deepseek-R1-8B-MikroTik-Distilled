# Repository Information
Name: Mikrotik-RouterOS-automatic-backup-and-update

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-RouterOS-automatic-backup-and-update/
    ├── .editorconfig
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
    │   │       ├── pack-ac2e4f6c1a25c1c375bbaa3a8964c3f8b313833b.idx
    │   │       └── pack-ac2e4f6c1a25c1c375bbaa3a8964c3f8b313833b.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .github/
    │   └── FUNDING.yml
    ├── .gitignore
    ├── BackupAndUpdate.rsc
    ├── howto/
    ├── LICENSE.md
    └── README.md


# Content
File: /.editorconfig
# EditorConfig is awesome: http://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
charset = utf-8
end_of_line = lf
indent_style = space
trim_trailing_whitespace = true
insert_final_newline = true

[*.rsc]
indent_style = space
indent_size = 4

[*.{yml,yaml,sls}]
indent_style = space
indent_size = 2

[*.{md,txt}]
indent_style = space
indent_size = 4
trim_trailing_whitespace = false


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update.git
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
0000000000000000000000000000000000000000 6aafe7d8c3e7814fd90b6fe24931d34607beaa5a vivek-dodia <vivek.dodia@icloud.com> 1738605783 -0500	clone: from https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 6aafe7d8c3e7814fd90b6fe24931d34607beaa5a vivek-dodia <vivek.dodia@icloud.com> 1738605783 -0500	clone: from https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 6aafe7d8c3e7814fd90b6fe24931d34607beaa5a vivek-dodia <vivek.dodia@icloud.com> 1738605783 -0500	clone: from https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
6aafe7d8c3e7814fd90b6fe24931d34607beaa5a refs/remotes/origin/master
29426e96e7a94716dcd713ef323f5698c7eeef62 refs/tags/22.11.12
4fde387224a7abff59ffca30a2b0b6273932e32b refs/tags/23.11.11
b149ed57a4102606a1a7d919c7b77a255bcea49e refs/tags/23.11.25
c47e747c27decc9be94e68f2160a775e88bfc3b5 refs/tags/24.06.04


File: /.git\refs\heads\master
6aafe7d8c3e7814fd90b6fe24931d34607beaa5a


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
* text=auto eol=lf
*.md diff=markdown
/.github export-ignore


File: /.github\FUNDING.yml
# These are supported funding model platforms
custom: https://buymeacoffee.com/beeyev


File: /.gitignore
/ignore

File: /BackupAndUpdate.rsc
# Script name: BackupAndUpdate
#
#----------SCRIPT INFORMATION---------------------------------------------------
#
# Script:  Mikrotik RouterOS automatic backup & update
# Version: 24.06.04
# Created: 07/08/2018
# Updated: 04/06/2024
# Author:  Alexander Tebiev
# Website: https://github.com/beeyev
# You can contact me by e-mail at tebiev@mail.com
#
# IMPORTANT!
# Minimum supported RouterOS version is v6.43.7
#
#----------MODIFY THIS SECTION AS NEEDED----------------------------------------
## Notification e-mail
## (Make sure you have configurated Email settings in Tools -> Email)
:local emailAddress "yourmail@example.com";

## Script mode, possible values: backup, osupdate, osnotify.
# backup    -   Only backup will be performed. (default value, if none provided)
#
# osupdate  -   The script will install a new RouterOS version if it is available.
#               It will also create backups before and after update process (it does not matter what value `forceBackup` is set to)
#               Email will be sent only if a new RouterOS version is available.
#               Change parameter `forceBackup` if you need the script to create backups every time when it runs (even when no updates were found).
#
# osnotify  -   The script will send email notifications only (without backups) if a new RouterOS update is available.
#               Change parameter `forceBackup` if you need the script to create backups every time when it runs.
:local scriptMode "osupdate";

## Additional parameter if you set `scriptMode` to `osupdate` or `osnotify`
# Set `true` if you want the script to perform backup every time it's fired, whatever script mode is set.
:local forceBackup false;

## Backup encryption password, no encryption if no password.
:local backupPassword ""

## If true, passwords will be included in exported config.
:local sensitiveDataInConfig true;

## Update channel. Possible values: stable, long-term, testing, development
:local updateChannel "stable";

## Installs only patch versions of RouterOS updates.
## Works only if you set scriptMode to "osupdate"
## Means that new update will be installed only if MAJOR and MINOR version numbers remained the same as currently installed RouterOS.
## Example: v6.43.6 => major.minor.PATCH
## Script will send information if new version is greater than just patch.
:local installOnlyPatchUpdates false;

## If true, device public IP address information will be included into the email message
:local detectPublicIpAddress true;

## Allow anonymous statistics collection. (script mode, device model, OS version)
:local allowAnonymousStatisticsCollection true;

##------------------------------------------------------------------------------------------##
#  !!!! DO NOT CHANGE ANYTHING BELOW THIS LINE, IF YOU ARE NOT SURE WHAT YOU ARE DOING !!!!  #
##------------------------------------------------------------------------------------------##

#Script messages prefix
:local SMP "Bkp&Upd:"

:log info "\r\n$SMP script \"Mikrotik RouterOS automatic backup & update\" started.";
:log info "$SMP Script Mode: $scriptMode, forceBackup: $forceBackup";

# Check email settings
:if ([:len $emailAddress] = 0) do={
    :log error ("$SMP \$emailAddress variable is empty. Script stopped.");
    :error "$SMP bye!";
}
:local emailServer ""
:do {
    :set emailServer [/tool e-mail get server];
} on-error={
    # Old of getting email server before the RouterOS v7.12
    :log info "$SMP Checking email server using old command `/tool e-mail get address`";
    :set emailServer [/tool e-mail get address];
}
:if ($emailServer = "0.0.0.0") do={
    :log error ("$SMP Email server address is not correct, please check Tools -> Email. Script stopped.");
    :error "$SMP bye!";
}
:if ([:len [/tool e-mail get from]] = 0 or [/tool e-mail get from] = "<>") do={
    :log error ("$SMP Email configuration FROM address is not correct, please check Tools -> Email. Script stopped.");
    :error "$SMP bye!";
}


#Check if proper identity name is set
if ([:len [/system identity get name]] = 0 or [/system identity get name] = "MikroTik") do={
    :log warning ("$SMP Please set identity name of your device (System -> Identity), keep it short and informative.");
};

############### vvvvvvvvv GLOBALS vvvvvvvvv ###############
# Function converts standard mikrotik build versions to the number.
# Possible arguments: paramOsVer
# Example:
# :put [$buGlobalFuncGetOsVerNum paramOsVer=[/system routerboard get current-RouterOS]];
# Result will be: 64301, because current RouterOS version is: 6.43.1
:global buGlobalFuncGetOsVerNum do={
    :local osVer $paramOsVer;
    :local osVerNum;
    :local osVerMicroPart;
    :local zro 0;
    :local tmp;

    # Replace word `beta` with dot
    :local isBetaPos [:tonum [:find $osVer "beta" 0]];
    :if ($isBetaPos > 1) do={
        :set osVer ([:pick $osVer 0 $isBetaPos] . "." . [:pick $osVer ($isBetaPos + 4) [:len $osVer]]);
    }
    # Replace word `rc` with dot
    :local isRcPos [:tonum [:find $osVer "rc" 0]];
    :if ($isRcPos > 1) do={
        :set osVer ([:pick $osVer 0 $isRcPos] . "." . [:pick $osVer ($isRcPos + 2) [:len $osVer]]);
    }

    :local dotPos1 [:find $osVer "." 0];

    :if ($dotPos1 > 0) do={

        # AA
        :set osVerNum  [:pick $osVer 0 $dotPos1];

        :local dotPos2 [:find $osVer "." $dotPos1];
                #Taking minor version, everything after first dot
        :if ([:len $dotPos2] = 0) do={:set tmp [:pick $osVer ($dotPos1+1) [:len $osVer]];}
        #Taking minor version, everything between first and second dots
        :if ($dotPos2 > 0) do={:set tmp [:pick $osVer ($dotPos1+1) $dotPos2];}

        # AA 0B
        :if ([:len $tmp] = 1) do={:set osVerNum "$osVerNum$zro$tmp";}
        # AA BB
        :if ([:len $tmp] = 2) do={:set osVerNum "$osVerNum$tmp";}

        :if ($dotPos2 > 0) do={
            :set tmp [:pick $osVer ($dotPos2+1) [:len $osVer]];
            # AA BB 0C
            :if ([:len $tmp] = 1) do={:set osVerNum "$osVerNum$zro$tmp";}
            # AA BB CC
            :if ([:len $tmp] = 2) do={:set osVerNum "$osVerNum$tmp";}
        } else={
            # AA BB 00
            :set osVerNum "$osVerNum$zro$zro";
        }
    } else={
        # AA 00 00
        :set osVerNum "$osVer$zro$zro$zro$zro";
    }

    :return $osVerNum;
}


# Function creates backups (system and config) and returns array with names
# Possible arguments:
#    `backupName`               | string    | backup file name, without extension!
#    `backupPassword`           | string    |
#    `sensitiveDataInConfig`    | boolean   |
# Example:
# :put [$buGlobalFuncCreateBackups name="daily-backup"];
:global buGlobalFuncCreateBackups do={
    :log info ("$SMP Global function \"buGlobalFuncCreateBackups\" was fired.");

    :local backupFileSys "$backupName.backup";
    :local backupFileConfig "$backupName.rsc";
    :local backupNames {$backupFileSys;$backupFileConfig};

    ## Make system backup
    :if ([:len $backupPassword] = 0) do={
        /system backup save dont-encrypt=yes name=$backupName;
    } else={
        /system backup save password=$backupPassword name=$backupName;
    }
    :log info ("$SMP System backup created. $backupFileSys");

    ## Export config file
    :if ($sensitiveDataInConfig = true) do={
        # Since RouterOS v7 it needs to be explicitly set that we want to export sensitive data
        :if ([:pick [/system package update get installed-version] 0 1] < 7) do={
            :execute "/export compact terse file=$backupName";
        } else={
            :execute "/export compact show-sensitive terse file=$backupName";
        }
    } else={
        /export compact hide-sensitive terse file=$backupName;
    }
    :log info ("$SMP Config file was exported. $backupFileConfig, the script execution will be paused for a moment.");

    #Delay after creating backups
    :delay 20s;
    :return $backupNames;
}

:global buGlobalVarUpdateStep;
############### ^^^^^^^^^ GLOBALS ^^^^^^^^^ ###############

:local scriptVersion "24.06.04";

# Current time `hh-mm-ss`
:local currentTime ([:pick [/system clock get time] 0 2] . "-" . [:pick [/system clock get time] 3 5] . "-" . [:pick [/system clock get time] 6 8]);

:local currentDateTime ("-" . $currentTime);

# Detect old date format, Example: `nov/11/2023`
:if ([:len [:tonum [:pick [/system clock get date] 0 1]]] = 0) do={
    :set currentDateTime ([:pick [/system clock get date] 7 11] . [:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6] . "-" . $currentTime);
} else={
    # New date format, Example: `2023-11-11`
    :set currentDateTime ([/system clock get date] . "-" . $currentTime);
};

:local isSoftBased false;
:if ([:pick [/system resource get board-name] 0 3] = "CHR" or [:pick [/system resource get board-name] 0 3] = "x86") do={
    :set isSoftBased true;
};

:local deviceOsVerInst          [/system package update get installed-version];
:local deviceOsVerInstNum       [$buGlobalFuncGetOsVerNum paramOsVer=$deviceOsVerInst];
:local deviceOsVerAvail         "";
:local deviceOsVerAvailNum      0;
:local deviceIdentityName       [/system identity get name];
:local deviceIdentityNameShort  [:pick $deviceIdentityName 0 18]
:local deviceUpdateChannel      [/system package update get channel];


:local deviceRbModel            "CloudHostedRouter";
:local deviceRbSerialNumber     "--";
:local deviceRbCurrentFw        "--";
:local deviceRbUpgradeFw        "--";

:if ($isSoftBased = false) do={
    :set deviceRbModel          [/system routerboard get model];
    :set deviceRbSerialNumber   [/system routerboard get serial-number];
    :set deviceRbCurrentFw      [/system routerboard get current-firmware];
    :set deviceRbUpgradeFw      [/system routerboard get upgrade-firmware];
};

:local isOsUpdateAvailable false;
:local isOsNeedsToBeUpdated false;

:local isSendEmailRequired true;

:local mailSubject  "$SMP Device - $deviceIdentityNameShort.";
:local mailBody     "";

:local mailBodyDeviceInfo   "\r\n\r\nDevice information: \r\nIdentity: $deviceIdentityName \r\nModel: $deviceRbModel \r\nSerial number: $deviceRbSerialNumber \r\nCurrent RouterOS: $deviceOsVerInst ($[/system package update get channel]) $[/system resource get build-time] \r\nCurrent routerboard FW: $deviceRbCurrentFw \r\nDevice uptime: $[/system resource get uptime]";
:local mailBodyCopyright    "\r\n\r\nMikrotik RouterOS automatic backup & update (ver. $scriptVersion) \r\nhttps://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update";
:local changelogUrl         ("Check RouterOS changelog: https://mikrotik.com/download/changelogs/" . $updateChannel . "-release-tree");

:local backupName           "v$deviceOsVerInst_$deviceUpdateChannel_$currentDateTime";
:local backupNameBeforeUpd  "backup_before_update_$backupName";
:local backupNameAfterUpd   "backup_after_update_$backupName";

:local backupNameFinal  $backupName;
:local mailAttachments  [:toarray ""];


:local ipAddressDetectServiceDefault "https://ipv4.mikrotik.ovh/"
:local ipAddressDetectServiceFallback "https://api.ipify.org/"
:local publicIpAddress "not detected";
:local telemetryDataQuery "";

:local updateStep $buGlobalVarUpdateStep;
:do {/system script environment remove buGlobalVarUpdateStep;} on-error={}
:if ([:len $updateStep] = 0) do={
    :set updateStep 1;
}

## IP address detection & anonymous statistics collection
:if ($updateStep = 1 or $updateStep = 3) do={
    :if ($updateStep = 3) do={
        :log info ("$SMP Waiting for one minute before continuing to the final step.");
        :delay 1m;
    }

    :if ($detectPublicIpAddress = true or $allowAnonymousStatisticsCollection = true) do={
        :if ($allowAnonymousStatisticsCollection = true) do={
            :set telemetryDataQuery ("\?mode=" . $scriptMode . "&osver=" . $deviceOsVerInst . "&model=" . $deviceRbModel);
        }

        :do {:set publicIpAddress ([/tool fetch http-method="get" url=($ipAddressDetectServiceDefault . $telemetryDataQuery) output=user as-value]->"data");} on-error={

            :if ($detectPublicIpAddress = true) do={
                :log warning "$SMP Could not detect public IP address using default detection service."
                :log warning "$SMP Trying to detect public ip using fallback detection service."

                :do {:set publicIpAddress ([/tool fetch http-method="get" url=$ipAddressDetectServiceFallback output=user as-value]->"data");} on-error={
                    :log warning "$SMP Could not detect public IP address using fallback detection service."
                }
            }
        }

        :if ($detectPublicIpAddress = true) do={
            # Always truncate the string for safety measures
            :set publicIpAddress ([:pick $publicIpAddress 0 15])
            :set mailBodyDeviceInfo ($mailBodyDeviceInfo . "\r\nPublic IP address: " . $publicIpAddress);
        }
    }
}


## STEP ONE: Creating backups, checking for new RouterOs version and sending email with backups,
## Steps 2 and 3 are fired only if script is set to automatically update device and if a new RouterOs version is available.
:if ($updateStep = 1) do={
    :log info ("$SMP Performing the first step.");

    # Checking for new RouterOS version
    if ($scriptMode = "osupdate" or $scriptMode = "osnotify") do={
        log info ("$SMP Checking for new RouterOS version. Current version is: $deviceOsVerInst");
        /system package update set channel=$updateChannel;
        /system package update check-for-updates;
        :delay 5s;
        :set deviceOsVerAvail [/system package update get latest-version];

        # If there is a problem getting information about available RouterOS versions from server
        :if ([:len $deviceOsVerAvail] = 0) do={
            :log warning ("$SMP There is a problem getting information about new RouterOS from server.");
            :set mailSubject    ($mailSubject . " Error: No data about new RouterOS!")
            :set mailBody         ($mailBody . "Error occured! \r\nMikrotik couldn't get any information about new RouterOS from server! \r\nWatch additional information in device logs.")
        } else={
            #Get numeric version of OS
            :set deviceOsVerAvailNum [$buGlobalFuncGetOsVerNum paramOsVer=$deviceOsVerAvail];

            # Checking if OS on server is greater than installed one.
            :if ($deviceOsVerAvailNum > $deviceOsVerInstNum) do={
                :set isOsUpdateAvailable true;
                :log info ("$SMP New RouterOS is available! $deviceOsVerAvail");
            } else={
                :set isSendEmailRequired false;
                :log info ("$SMP System is already up to date.");
                :set mailSubject ($mailSubject . " No new OS updates.");
                :set mailBody      ($mailBody . "Your system is up to date.");
            }
        };
    } else={
        :set scriptMode "backup";
    };

    if ($forceBackup = true) do={
        # In this case the script will always send an email, because it has to create backups
        :set isSendEmailRequired true;
    }

    # If a new OS version is available to install
    if ($isOsUpdateAvailable = true and $isSendEmailRequired = true) do={
        # If we only need to notify about a new available version
        if ($scriptMode = "osnotify") do={
            :set mailSubject    ($mailSubject . " New RouterOS is available! v.$deviceOsVerAvail.")
            :set mailBody       ($mailBody . "New RouterOS version is available to install: v.$deviceOsVerAvail ($updateChannel) \r\n$changelogUrl")
        }

        # If we need to initiate RouterOS update process
        if ($scriptMode = "osupdate") do={
            :set isOsNeedsToBeUpdated true;
            # If we need to install only patch updates
            :if ($installOnlyPatchUpdates = true) do={
                #Check if Major and Minor builds are the same.
                :if ([:pick $deviceOsVerInstNum 0 ([:len $deviceOsVerInstNum]-2)] = [:pick $deviceOsVerAvailNum 0 ([:len $deviceOsVerAvailNum]-2)]) do={
                    :log info ("$SMP New patch version of RouterOS firmware is available.");
                } else={
                    :log info           ("$SMP New major or minor version of RouterOS firmware is available. You need to update it manually.");
                    :set mailSubject    ($mailSubject . " New RouterOS: v.$deviceOsVerAvail needs to be installed manually.");
                    :set mailBody       ($mailBody . "New major or minor RouterOS version is available to install: v.$deviceOsVerAvail ($updateChannel). \r\nYou chose to automatically install only patch updates, so this major update you need to install manually. \r\n$changelogUrl");
                    :set isOsNeedsToBeUpdated false;
                }
            }

            #Check again, because this variable could be changed during checking for installing only patch updats
            if ($isOsNeedsToBeUpdated = true) do={
                :log info           ("$SMP New RouterOS is going to be installed! v.$deviceOsVerInst -> v.$deviceOsVerAvail");
                :set mailSubject    ($mailSubject . " New RouterOS is going to be installed! v.$deviceOsVerInst -> v.$deviceOsVerAvail.");
                :set mailBody       ($mailBody . "Your Mikrotik will be updated to the new RouterOS version from v.$deviceOsVerInst to v.$deviceOsVerAvail (Update channel: $updateChannel) \r\nA final report with detailed information will be sent once the update process is completed. \r\nIf you do not receive a second email within the next 10 minutes, there may be an issue. Please check your device logs for further information.");
                #!! There is more code connected to this part and first step at the end of the script.
            }

        }
    }

    ## Checking If the script needs to create a backup
    :log info ("$SMP Checking If the script needs to create a backup.");
    if ($forceBackup = true or $scriptMode = "backup" or $isOsNeedsToBeUpdated = true) do={
        :log info ("$SMP Creating system backups.");
        if ($isOsNeedsToBeUpdated = true) do={
            :set backupNameFinal $backupNameBeforeUpd;
        };
        if ($scriptMode != "backup") do={
            :set mailBody ($mailBody . "\r\n\r\n");
        };

        :set mailSubject    ($mailSubject . " Backup was created.");
        :set mailBody       ($mailBody . "System backups were created and attached to this email.");

        :set mailAttachments [$buGlobalFuncCreateBackups backupName=$backupNameFinal backupPassword=$backupPassword sensitiveDataInConfig=$sensitiveDataInConfig];
    } else={
        :log info ("$SMP Creating a backup is not necessary.");
    }

    # Combine first step email
    :set mailBody ($mailBody . $mailBodyDeviceInfo . $mailBodyCopyright);
}

## STEP TWO: (after first reboot) routerboard firmware upgrade
## Steps 2 and 3 are fired only if script is set to automatically update device and if new RouterOs is available.
:if ($updateStep = 2) do={
    :log info ("$SMP Performing the second step.");
    ## RouterOS is the latest, let's check for upgraded routerboard firmware
    if ($deviceRbCurrentFw != $deviceRbUpgradeFw) do={
        :set isSendEmailRequired false;
        :delay 10s;
        :log info "$SMP Upgrading routerboard firmware from v.$deviceRbCurrentFw to v.$deviceRbUpgradeFw";
        ## Start the upgrading process
        /system routerboard upgrade;
        ## Wait until the upgrade is completed
        :delay 5s;
        :log info "$SMP routerboard upgrade process was completed, going to reboot in a moment!";
        ## Set scheduled task to send final report on the next boot, task will be deleted when it is done. (That is why you should keep original script name)
        /system scheduler add name=BKPUPD-FINAL-REPORT-ON-NEXT-BOOT on-event=":delay 5s; /system scheduler remove BKPUPD-FINAL-REPORT-ON-NEXT-BOOT; :global buGlobalVarUpdateStep 3; :delay 10s; /system script run BackupAndUpdate;" start-time=startup interval=0;
        ## Reboot system to boot with new firmware
        /system reboot;
    } else={
        :log info "$SMP It appears that your routerboard is already up to date, skipping this step.";
        :set updateStep 3;
    };
}

## STEP THREE: Last step (after second reboot) sending final report
## Steps 2 and 3 are fired only if script is set to automatically update device and if new RouterOs is available.
## This step is executed after some delay
:if ($updateStep = 3) do={
    :log info ("$SMP Performing the third step.");
    :log info "Bkp&Upd: RouterOS and routerboard upgrade process was completed. New RouterOS version: v.$deviceOsVerInst, routerboard firmware: v.$deviceRbCurrentFw.";
    ## Small delay in case mikrotik needs some time to initialize connections
    :log info "$SMP Sending the final email with report and backups.";
    :set mailSubject    ($mailSubject . " RouterOS Upgrade is completed, new version: v.$deviceOsVerInst!");
    :set mailBody       "RouterOS and routerboard upgrade process was completed. \r\nNew RouterOS version: v.$deviceOsVerInst, routerboard firmware: v.$deviceRbCurrentFw. \r\n$changelogUrl \r\n\r\nBackups of the upgraded system are in the attachment of this email.  $mailBodyDeviceInfo $mailBodyCopyright";
    :set mailAttachments [$buGlobalFuncCreateBackups backupName=$backupNameAfterUpd backupPassword=$backupPassword sensitiveDataInConfig=$sensitiveDataInConfig];
}

# Remove functions from global environment to keep it fresh and clean.
:do {/system script environment remove buGlobalFuncGetOsVerNum;} on-error={}
:do {/system script environment remove buGlobalFuncCreateBackups;} on-error={}

##
## SENDING EMAIL
##
# Trying to send email with backups as attachments.

:if ($isSendEmailRequired = true) do={
    :log info "$SMP Dispatching email message; estimated completion within 30 seconds.";
    :do {/tool e-mail send to=$emailAddress subject=$mailSubject body=$mailBody file=$mailAttachments;} on-error={
        :delay 5s;
        :log error "$SMP could not send email message ($[/tool e-mail get last-status]). Will attempt redelivery shortly."

        :delay 5m;

        :do {/tool e-mail send to=$emailAddress subject=$mailSubject body=$mailBody file=$mailAttachments;} on-error={
            :delay 5s;
            :log error "$SMP failed to send email message ($[/tool e-mail get last-status]) for the second time."

            if ($isOsNeedsToBeUpdated = true) do={
                :set isOsNeedsToBeUpdated false;
                :log warning "$SMP script is not going to initialise update process due to inability to send backups to email."
            }
        }
    }

    :delay 30s;

    :if ([:len $mailAttachments] > 0 and [/tool e-mail get last-status] = "succeeded") do={
        :log info "$SMP File system cleanup."
        /file remove $mailAttachments;
        :delay 2s;
    }

}


# Fire RouterOS update process
if ($isOsNeedsToBeUpdated = true) do={

    :if ($isSoftBased = false) do={
        ## Set scheduled task to upgrade routerboard firmware on the next boot, task will be deleted when upgrade is done. (That is why you should keep original script name)
        /system scheduler add name=BKPUPD-UPGRADE-ON-NEXT-BOOT on-event=":delay 5s; /system scheduler remove BKPUPD-UPGRADE-ON-NEXT-BOOT; :global buGlobalVarUpdateStep 2; :delay 10s; /system script run BackupAndUpdate;" start-time=startup interval=0;
    } else= {
        ## If the script is executed on CHR, step 2 will be skipped
        /system scheduler add name=BKPUPD-UPGRADE-ON-NEXT-BOOT on-event=":delay 5s; /system scheduler remove BKPUPD-UPGRADE-ON-NEXT-BOOT; :global buGlobalVarUpdateStep 3; :delay 10s; /system script run BackupAndUpdate;" start-time=startup interval=0;
    };


    :log info "$SMP everything is ready to install new RouterOS, going to reboot in a moment!"
    ## Command is reincarnation of the "upgrade" command - doing exactly the same but under a different name
    /system package update install;
}

:log info "$SMP script \"Mikrotik RouterOS automatic backup & update\" completed it's job.\r\n";


File: /LICENSE.md
MIT License

Copyright (c) Alexander Tebiev tebiev@mail.com

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


File: /README.md
# Mikrotik RouterOS automatic backup and update

This script allows you to generate daily backups of MikroTik and send them to an email address. You can also choose to enable automatic RouterOS upgrades or receive notifications exclusively for new firmware versions.


> 💡 If you have any ideas about the script or you just want to share your opinion, you are welcome to [Discussions](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/discussions), or you can open an [issue](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/issues) if you found a bug.


## Features:
- Select the script's operational mode according to your specific needs (details provided below). 
- This script is designed to create full system backups and export configurations. 
- Customize the update channel according to your preference. 
- With automatic updates activated, the script can be set to apply only patch updates for RouterOS. For instance, should the current RouterOS version be v6.43.6, the script will autonomously upgrade to v6.43.7 (a patch update), while avoiding v6.44.0 (a minor update).*
- The script also incorporates vital device details in the email alerts, facilitating easy identification of the necessary backup among several devices. 
- For added security, the script is programmed to stop the automatic update process if it fails to dispatch backups via email. 
- Routerboard firmware can be upgraded automatically based on the installed RouterOS version.

## Script operating modes:
**Backups only** - The script generates system and configuration backups and forwards them to a specified email as attachments. It uses your email account as a storage for these backups.  
**Backups and notifications about new RouterOS release** -  In addition to creating backups, the script also monitors for any new releases of RouterOS firmware and communicates this information via email.  
**Backups and automatic RouterOS upgrade** - The script begins by creating a backup, followed by a check for any new versions of RouterOS. If a newer firmware version is detected, the script initiates the upgrade process. Upon completion, two emails are sent: the first includes the system backups from the prior RouterOS version, and the second, sent post-upgrade, contains backups of the updated system.

## How to use
> ❗️ **Important**  
> Ensure your device identity does not contain spaces and special characters! `System -> Identity`

##### 1. Configure parameters
Take the  [script](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/raw/master/BackupAndUpdate.rsc) and configure it's parameters at the begining of the file.  
This step is straightforward as all parameters are well-commented.
**Important!** Don't forget to provide correct email address for backups and pay attention to `scriptMode` variable.

##### 2. Create new script
System -> Scripts [Add]  

**Important!** Script name must be `BackupAndUpdate`   
Insert the script which you configured earlier into the source area.  
![](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/raw/master/howto/script-name.png)  

##### 3. Configure mail server
Tools -> Email  
Configure your email server parameters. If you don't have one, i recommend using the [smtp2go.com](https://smtp2go.com "smtp2go.com") service, which allows sending a thousand emails per month for free.  
![](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/raw/master/howto/email-config.png)  

To check email settings, send a test message by running the following command in terminal:
```
/tool e-mail send to="yourMail@example.com" subject="backup & update test!" body="It works!";
```

##### 4. Create scheduled task
System -> Scheduler [Add]  
Name: `Backup And Update`  
Start Time: `03:10:00` (the start time has to be different for all your mikrotik devices in a chain)  
Interval: `1d 00:00:00`  
On Event: `/system script run BackupAndUpdate;`  
![](https://github.com/beeyev/Mikrotik-RouterOS-automatic-backup-and-update/raw/master/howto/scheduler-task.png)  
  
Or you can use this command to create the task:
```
/system scheduler add name="Firmware Updater" on-event="/system script run BackupAndUpdate;" start-time=03:10:00 interval=1d comment="" disabled=no
```
##### 5. Test the script
Once everything is set up, it's important to verify that the script is functioning properly. 
To do this, open a New Terminal and a Log window in your WinBox, then manually execute the script by typing `/system script run BackupAndUpdate;` in the Terminal.
You will see the script the script's operation in the log window. If the script completes without any errors, check your email. You'll find a new message with backups from your MikroTik awaiting you. 🎉






## Acknowledgements
I would like to extend my sincere gratitude to the following individuals who have contributed to this project:
 - DJ5KP, website: [dj5kp.de](http://dj5kp.de/)

Special thanks to the talented people who are working at [MikroTik](https://mikrotik.com) for their contributions in creating such outstanding products.

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

---
If you love this project, please buy more mikrotiks ;) and consider giving me a ⭐

[__Buy me a coffee! :coffee:__](https://www.buymeacoffee.com/beeyev)

![](https://visitor-badge.laobi.icu/badge?page_id=beeyev.Mikrotik-RouterOS-automatic-backup-and-update)


