# Repository Information
Name: mikrotik-router-management

# Directory Structure
Directory structure:
└── github_repos/mikrotik-router-management/
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
    │   │       ├── pack-c205a3164f54d7d01f56251cf624b241a9d7a0ea.idx
    │   │       └── pack-c205a3164f54d7d01f56251cf624b241a9d7a0ea.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── Api Mikrotik/
    │   ├── FormMain.frm
    │   ├── MD5.cls
    │   ├── MicrotikTest.vbp
    │   └── MicrotikTest.vbw
    ├── Form2.frm
    ├── Form_Instrucciones.frm
    ├── Form_Instrucciones.frx
    ├── Instrucciones.rtf
    ├── Jenkinsfile
    ├── mensajeAPI.txt
    ├── Pin.ctl
    ├── Pin.ctx
    ├── Planos/
    │   ├── PE-ID-01.wmf
    │   └── PE-ID-02.wmf
    ├── prueba.txt
    ├── README.md
    ├── Registros/
    │   └── Registro_Datos.txt
    ├── TFG ejecutable.exe
    ├── TFG.exe
    ├── TFG.frm
    ├── TFG.vbp
    └── TFG.vbw


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
	url = https://github.com/AdrMS/mikrotik-router-management.git
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
0000000000000000000000000000000000000000 e7d482e992d3336a0f8987411beb84ae1c5feb0d vivek-dodia <vivek.dodia@icloud.com> 1738606438 -0500	clone: from https://github.com/AdrMS/mikrotik-router-management.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 e7d482e992d3336a0f8987411beb84ae1c5feb0d vivek-dodia <vivek.dodia@icloud.com> 1738606438 -0500	clone: from https://github.com/AdrMS/mikrotik-router-management.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e7d482e992d3336a0f8987411beb84ae1c5feb0d vivek-dodia <vivek.dodia@icloud.com> 1738606438 -0500	clone: from https://github.com/AdrMS/mikrotik-router-management.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e7d482e992d3336a0f8987411beb84ae1c5feb0d refs/remotes/origin/master


File: /.git\refs\heads\master
e7d482e992d3336a0f8987411beb84ae1c5feb0d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /Api Mikrotik\FormMain.frm
VERSION 5.00
Object = "{248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0"; "MSWINSCK.OCX"
Begin VB.Form FormMain 
   Caption         =   "Microtik API Test"
   ClientHeight    =   5160
   ClientLeft      =   1860
   ClientTop       =   2085
   ClientWidth     =   6615
   LinkTopic       =   "Form1"
   ScaleHeight     =   5160
   ScaleWidth      =   6615
   Begin VB.TextBox txtOut 
      Height          =   3615
      Left            =   0
      MultiLine       =   -1  'True
      ScrollBars      =   2  'Vertical
      TabIndex        =   12
      Top             =   1560
      Width           =   6615
   End
   Begin VB.CommandButton btnSend 
      Caption         =   "Send"
      Height          =   255
      Left            =   5760
      TabIndex        =   10
      Top             =   960
      Width           =   855
   End
   Begin VB.TextBox txtCommand 
      Height          =   285
      Left            =   120
      TabIndex        =   9
      Text            =   "/system/resource/print"
      Top             =   960
      Width           =   5535
   End
   Begin VB.TextBox txtPass 
      Height          =   285
      IMEMode         =   3  'DISABLE
      Left            =   3240
      PasswordChar    =   "*"
      TabIndex        =   7
      Top             =   360
      Width           =   1455
   End
   Begin VB.TextBox txtUser 
      Height          =   285
      Left            =   1680
      TabIndex        =   5
      Top             =   360
      Width           =   1455
   End
   Begin VB.CommandButton btnDisconnect 
      Caption         =   "Disc"
      Height          =   255
      Left            =   5760
      TabIndex        =   3
      Top             =   360
      Width           =   855
   End
   Begin VB.CommandButton btnConnect 
      Caption         =   "Connect"
      Height          =   255
      Left            =   4800
      TabIndex        =   2
      Top             =   360
      Width           =   855
   End
   Begin VB.TextBox txtIP 
      Height          =   285
      Left            =   120
      TabIndex        =   0
      Top             =   360
      Width           =   1455
   End
   Begin MSWinsockLib.Winsock ws 
      Left            =   720
      Top             =   0
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   393216
   End
   Begin VB.Label Label5 
      Caption         =   "Output"
      Height          =   255
      Left            =   120
      TabIndex        =   11
      Top             =   1320
      Width           =   1215
   End
   Begin VB.Label Label4 
      Caption         =   "Command:"
      Height          =   255
      Left            =   120
      TabIndex        =   8
      Top             =   720
      Width           =   1335
   End
   Begin VB.Label Label3 
      Caption         =   "Pass"
      Height          =   255
      Left            =   3240
      TabIndex        =   6
      Top             =   120
      Width           =   615
   End
   Begin VB.Label Label2 
      Caption         =   "User"
      Height          =   255
      Left            =   1680
      TabIndex        =   4
      Top             =   120
      Width           =   735
   End
   Begin VB.Label Label1 
      Caption         =   "IP"
      Height          =   255
      Left            =   120
      TabIndex        =   1
      Top             =   120
      Width           =   255
   End
End
Attribute VB_Name = "FormMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private inbuf1() As Byte ' 1st stage inbound data
Private inbuf2$ ' 2nd stage ( decoded ) inbound data
Private bErr As Boolean
Private Enum MyState_e
    CONNECTING
    WAITING_KEY
    AUTHENTICATING
    CONNECTED
End Enum
Dim MyState As MyState_e
Dim md5 As New CMD5

Private Sub Out(ByVal s$)
    txtOut.text = txtOut.text & s & vbCrLf
End Sub

Private Function GetReply$()
    Dim tmp&
    tmp = InStr(inbuf2, vbLf)
    If 0 = tmp Then Exit Function
    GetReply = Left(inbuf2, tmp - 1)
    inbuf2 = Mid(inbuf2, tmp + 1)
End Function

Private Sub btnConnect_Click()
    bErr = False
    ws.Protocol = sckTCPProtocol
    MyState = CONNECTING
    Out "(Connecting)"
    ws.Connect txtIP.text, 8728
End Sub

Private Function Hexlify$(ByVal s$)
    Dim i&, n&
    For i = 1 To Len(s)
        n = Asc(Mid(s, i, 1))
        Hexlify = Hexlify & LCase(Right("0" & Hex(n), 2))
    Next
End Function

Private Function Unhexlify$(ByVal s$)
    Dim i&, n&
    For i = 1 To Len(s) Step 2
        n = CLng("&H" & Mid(s, i, 2))
        Unhexlify = Unhexlify & Chr(n)
    Next
End Function

Private Sub btnSend_Click()
SendCommand txtCommand.text
End Sub

Private Sub Form_Resize()
    txtOut.Width = Me.ScaleWidth - txtOut.Left
    txtOut.Height = Me.ScaleHeight - txtOut.Top
End Sub

Private Sub Form_Unload(Cancel As Integer)
    bErr = True
    ws.Close
    End
End Sub

Private Sub ws_Connect()
    MyState = WAITING_KEY
    Out "(connected - sending /login)"
    SendCommand ("/login")
End Sub

Private Sub ws_DataArrival(ByVal bytesTotal As Long)
    If bErr Then Exit Sub
    Dim ar() As Byte, i&, inbuf1_len&
    ReDim ar(0 To bytesTotal - 1)
    ws.GetData ar, vbByte, bytesTotal
    On Error Resume Next
    Err.Clear
    inbuf1_len = UBound(inbuf1)
    If Err Then
        inbuf1_len = 0
        ReDim inbuf1(0)
    Else
        inbuf1_len = inbuf1_len + 1
    End If
    On Error GoTo 0
    If inbuf1_len > 0 Then
        Dim off&
        off = inbuf1_len
        ReDim Preserve inbuf1(inbuf1_len + bytesTotal - 1)
        For i = 0 To bytesTotal - 1
            inbuf1(off + i) = ar(i)
        Next
    Else
        inbuf1 = ar
    End If
    Dim WordLen&, StartIdx&, Idx&
    StartIdx = 0
    Do While True
        Idx = StartIdx
        WordLen = CalcWordLen(inbuf1, Idx)
        If WordLen < 0 Then
            Exit Do
        End If
        If WordLen = 0 Then
            SentenceArrived (inbuf2)
            inbuf2 = ""
        Else
            If inbuf1(Idx) = Asc("=") Then
                inbuf2 = inbuf2 & " "
            End If
            For i = 0 To WordLen - 1
                inbuf2 = inbuf2 & Chr(inbuf1(Idx + i))
            Next
        End If
        StartIdx = Idx + WordLen
    Loop
End Sub

Private Sub SentenceArrived(ByVal sent$)
    Dim ar$(), tmp$, i&, re As New RegExp, chal$
    Out "I " & Replace(sent & " <<EOS>>", " ", vbCrLf & "I ")
    Select Case MyState
    Case CONNECTING
        ' this shouldn't happen!
        Out "(connected w/ packet - sending /login)"
        SendCommand "/login"
        MyState = WAITING_KEY
    Case WAITING_KEY
        Out "(got key sending credentials)"
        re.Global = False
        re.Pattern = "^!done =ret=([a-fA-F0-9]+)$"
        On Error Resume Next
        Err.Clear
        If re.Test(sent) Then
            chal = re.Replace(sent, "$1")
        Else
            bErr = True
        End If
        If Err Or bErr Then
            Out "Got error response to initial /login"
            bErr = True
            Exit Sub
        End If
        On Error GoTo 0
        Out md5.MD5Hex(Chr(0))
        Out md5.MD5Hex(Chr(0) & txtPass.text)
        tmp = md5.MD5Hex(Chr(0) & txtPass.text & Unhexlify(chal))
        tmp = "/login =name=" & txtUser.text & " =response=00" & tmp
        SendCommand tmp
        MyState = AUTHENTICATING
    Case AUTHENTICATING
        If Left(sent, 5) <> "!done" Then
            Out "Authentication failure"
            bErr = True
            Exit Sub
        End If
        MyState = CONNECTED
    Case CONNECTED
        ' do nothing - we're already sending output to text box
    End Select
End Sub

Private Function CalcWordLen&(ByRef ar() As Byte, ByRef Idx&)
    Dim tmp&
    CalcWordLen = -1 ' return error by default
    
    ' is there a single byte to begin decoding?
    If Idx > UBound(inbuf1) Then Exit Function
    
    tmp = inbuf1(Idx)
    If tmp < &H80 Then
        Idx = Idx + 1
    ElseIf tmp < &HC0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 1) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HC0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        Idx = Idx + 2
    ElseIf tmp < &HE0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 2) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HE0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        Idx = Idx + 3
    ElseIf tmp < &HF0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 3) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HF0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        tmp = tmp * 256 + inbuf1(Idx + 3)
        Idx = Idx + 4
    ElseIf tmp < &HF8& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 4) > UBound(inbuf1) Then Exit Function
        tmp = inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        tmp = tmp * 256 + inbuf1(Idx + 3)
        tmp = tmp * 256 + inbuf1(Idx + 4)
        Idx = Idx + 5
    Else
        bErr = True
        Out "ERROR: Received reserved control byte (0x" & Hex(inbuf1(0)) & ") - connection is indeterminate"
        Exit Function
    End If
    ' is the entire buffer here for which we are asking the length?
    If (Idx + tmp - 1) > UBound(inbuf1) Then Exit Function
    CalcWordLen = tmp
End Function

Private Sub ws_Error(ByVal Number As Integer, Description As String, ByVal Scode As Long, ByVal Source As String, ByVal HelpFile As String, ByVal HelpContext As Long, CancelDisplay As Boolean)
    Out "ws_Error: " & Description
    bErr = True
End Sub

Private Sub EncodeWord(ByRef buf() As Byte, ByVal sWord$)
    Dim DataLen&, HdrLen&, Idx&, tmp&, i&
    DataLen = Len(sWord)
    'If 0 = DataLen Then
    '    DataLen = 1
    '    sWord = Chr(0)
    'End If
    
    On Error Resume Next
    Err.Clear
    Idx = UBound(buf)
    If Err Then
        On Error GoTo 0
        ReDim buf(0)
        Idx = 0
    Else
        Idx = Idx + 1
    End If
    On Error GoTo 0
    If DataLen < &H80& Then
        HdrLen = 1
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        buf(Idx) = DataLen
    ElseIf DataLen < &H4000& Then
        HdrLen = 2
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &H8000&
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    ElseIf DataLen < &H200000 Then
        HdrLen = 3
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &HC00000
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    ElseIf DataLen < &H10000000 Then
        HdrLen = 4
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &HE0000000
        buf(Idx + 3) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    Else
        HdrLen = 5
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        buf(Idx) = &HF0&
        buf(Idx + 4) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 3) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp
    End If
    Idx = Idx + HdrLen - 1 ' Idx is one-less, to make math easier below
    For i = 1 To DataLen
        buf(Idx + i) = Asc(Mid$(sWord, i, 1))
    Next
End Sub

Private Sub SendCommand(ByVal sCmd$)
    Dim ar$(), i&, buf() As Byte
    Out "O " & Replace(sCmd & " <<EOS>>", " ", vbCrLf & "O ")
    ar = Split(sCmd, " ")
    For i = 0 To UBound(ar)
        EncodeWord buf, ar(i)
    Next
    EncodeWord buf, ""
    ws.SendData buf
End Sub


File: /Api Mikrotik\MD5.cls
VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
  Persistable = 0  'NotPersistable
  DataBindingBehavior = 0  'vbNone
  DataSourceBehavior  = 0  'vbNone
  MTSTransactionMode  = 0  'NotAnMTSObject
END
Attribute VB_Name = "CMD5"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
'*******************************************************************************
' MODULE:       CMD5
' FILENAME:     C:\My Code\vb\md5\CMD5.cls
' AUTHOR:       Phil Fresle
' CREATED:      16-Feb-2001
' COPYRIGHT:    Copyright 2001 Frez Systems Limited. All Rights Reserved.
'
' DESCRIPTION:
' Derived from the RSA Data Security, Inc. MD5 Message-Digest Algorithm,
' as set out in the memo RFC1321.
'
' This class is used to generate an MD5 'digest' or 'signature' of a string. The
' MD5 algorithm is one of the industry standard methods for generating digital
' signatures. It is generically known as a digest, digital signature, one-way
' encryption, hash or checksum algorithm. A common use for MD5 is for password
' encryption as it is one-way in nature, that does not mean that your passwords
' are not free from a dictionary attack. If you are using the
' routine for passwords, you can make it a little more secure by concatenating
' some known random characters to the password before you generate the signature
' and on subsequent tests, so even if a hacker knows you are using MD5 for
' your passwords, the random characters will make it harder to dictionary attack.
'
' *** CAUTION ***
' See the comment attached to the MD5 method below regarding use on systems
' with different character sets.
'
' This is 'free' software with the following restrictions:
'
' You may not redistribute this code as a 'sample' or 'demo'. However, you are free
' to use the source code in your own code, but you may not claim that you created
' the sample code. It is expressly forbidden to sell or profit from this source code
' other than by the knowledge gained or the enhanced value added by your own code.
'
' Use of this software is also done so at your own risk. The code is supplied as
' is without warranty or guarantee of any kind.
'
' Should you wish to commission some derivative work based on this code provided
' here, or any consultancy work, please do not hesitate to contact us.
'
' Web Site:  http://www.frez.co.uk
' E-mail:    sales@frez.co.uk
'
' MODIFICATION HISTORY:
' 1.0       16-Feb-2001
'           Phil Fresle
'           Initial Version
'*******************************************************************************
Option Explicit

Private Const BITS_TO_A_BYTE  As Long = 8
Private Const BYTES_TO_A_WORD As Long = 4
Private Const BITS_TO_A_WORD  As Long = BYTES_TO_A_WORD * BITS_TO_A_BYTE

Private m_lOnBits(0 To 30) As Long
Private m_l2Power(0 To 30) As Long

'*******************************************************************************
' Class_Initialize (SUB)
'
' DESCRIPTION:
' We will usually get quicker results by preparing arrays of bit patterns and
' powers of 2 ahead of time instead of calculating them every time, unless of
' course the methods are only ever getting called once per instantiation of the
' class.
'*******************************************************************************
Private Sub Class_Initialize()
    ' Could have done this with a loop calculating each value, but simply
    ' assigning the values is quicker - BITS SET FROM RIGHT
    m_lOnBits(0) = 1            ' 00000000000000000000000000000001
    m_lOnBits(1) = 3            ' 00000000000000000000000000000011
    m_lOnBits(2) = 7            ' 00000000000000000000000000000111
    m_lOnBits(3) = 15           ' 00000000000000000000000000001111
    m_lOnBits(4) = 31           ' 00000000000000000000000000011111
    m_lOnBits(5) = 63           ' 00000000000000000000000000111111
    m_lOnBits(6) = 127          ' 00000000000000000000000001111111
    m_lOnBits(7) = 255          ' 00000000000000000000000011111111
    m_lOnBits(8) = 511          ' 00000000000000000000000111111111
    m_lOnBits(9) = 1023         ' 00000000000000000000001111111111
    m_lOnBits(10) = 2047        ' 00000000000000000000011111111111
    m_lOnBits(11) = 4095        ' 00000000000000000000111111111111
    m_lOnBits(12) = 8191        ' 00000000000000000001111111111111
    m_lOnBits(13) = 16383       ' 00000000000000000011111111111111
    m_lOnBits(14) = 32767       ' 00000000000000000111111111111111
    m_lOnBits(15) = 65535       ' 00000000000000001111111111111111
    m_lOnBits(16) = 131071      ' 00000000000000011111111111111111
    m_lOnBits(17) = 262143      ' 00000000000000111111111111111111
    m_lOnBits(18) = 524287      ' 00000000000001111111111111111111
    m_lOnBits(19) = 1048575     ' 00000000000011111111111111111111
    m_lOnBits(20) = 2097151     ' 00000000000111111111111111111111
    m_lOnBits(21) = 4194303     ' 00000000001111111111111111111111
    m_lOnBits(22) = 8388607     ' 00000000011111111111111111111111
    m_lOnBits(23) = 16777215    ' 00000000111111111111111111111111
    m_lOnBits(24) = 33554431    ' 00000001111111111111111111111111
    m_lOnBits(25) = 67108863    ' 00000011111111111111111111111111
    m_lOnBits(26) = 134217727   ' 00000111111111111111111111111111
    m_lOnBits(27) = 268435455   ' 00001111111111111111111111111111
    m_lOnBits(28) = 536870911   ' 00011111111111111111111111111111
    m_lOnBits(29) = 1073741823  ' 00111111111111111111111111111111
    m_lOnBits(30) = 2147483647  ' 01111111111111111111111111111111
    
    ' Could have done this with a loop calculating each value, but simply
    ' assigning the values is quicker - POWERS OF 2
    m_l2Power(0) = 1            ' 00000000000000000000000000000001
    m_l2Power(1) = 2            ' 00000000000000000000000000000010
    m_l2Power(2) = 4            ' 00000000000000000000000000000100
    m_l2Power(3) = 8            ' 00000000000000000000000000001000
    m_l2Power(4) = 16           ' 00000000000000000000000000010000
    m_l2Power(5) = 32           ' 00000000000000000000000000100000
    m_l2Power(6) = 64           ' 00000000000000000000000001000000
    m_l2Power(7) = 128          ' 00000000000000000000000010000000
    m_l2Power(8) = 256          ' 00000000000000000000000100000000
    m_l2Power(9) = 512          ' 00000000000000000000001000000000
    m_l2Power(10) = 1024        ' 00000000000000000000010000000000
    m_l2Power(11) = 2048        ' 00000000000000000000100000000000
    m_l2Power(12) = 4096        ' 00000000000000000001000000000000
    m_l2Power(13) = 8192        ' 00000000000000000010000000000000
    m_l2Power(14) = 16384       ' 00000000000000000100000000000000
    m_l2Power(15) = 32768       ' 00000000000000001000000000000000
    m_l2Power(16) = 65536       ' 00000000000000010000000000000000
    m_l2Power(17) = 131072      ' 00000000000000100000000000000000
    m_l2Power(18) = 262144      ' 00000000000001000000000000000000
    m_l2Power(19) = 524288      ' 00000000000010000000000000000000
    m_l2Power(20) = 1048576     ' 00000000000100000000000000000000
    m_l2Power(21) = 2097152     ' 00000000001000000000000000000000
    m_l2Power(22) = 4194304     ' 00000000010000000000000000000000
    m_l2Power(23) = 8388608     ' 00000000100000000000000000000000
    m_l2Power(24) = 16777216    ' 00000001000000000000000000000000
    m_l2Power(25) = 33554432    ' 00000010000000000000000000000000
    m_l2Power(26) = 67108864    ' 00000100000000000000000000000000
    m_l2Power(27) = 134217728   ' 00001000000000000000000000000000
    m_l2Power(28) = 268435456   ' 00010000000000000000000000000000
    m_l2Power(29) = 536870912   ' 00100000000000000000000000000000
    m_l2Power(30) = 1073741824  ' 01000000000000000000000000000000
End Sub

'*******************************************************************************
' LShift (FUNCTION)
'
' PARAMETERS:
' (In) - lValue     - Long    - The value to be shifted
' (In) - iShiftBits - Integer - The number of bits to shift the value by
'
' RETURN VALUE:
' Long - The shifted long integer
'
' DESCRIPTION:
' A left shift takes all the set binary bits and moves them left, in-filling
' with zeros in the vacated bits on the right. This function is equivalent to
' the << operator in Java and C++
'*******************************************************************************
Private Function LShift(ByVal lValue As Long, _
                        ByVal iShiftBits As Integer) As Long
    ' NOTE: If you can guarantee that the Shift parameter will be in the
    ' range 1 to 30 you can safely strip of this first nested if structure for
    ' speed.
    '
    ' A shift of zero is no shift at all.
    If iShiftBits = 0 Then
        LShift = lValue
        Exit Function
        
    ' A shift of 31 will result in the right most bit becoming the left most
    ' bit and all other bits being cleared
    ElseIf iShiftBits = 31 Then
        If lValue And 1 Then
            LShift = &H80000000
        Else
            LShift = 0
        End If
        Exit Function
        
    ' A shift of less than zero or more than 31 is undefined
    ElseIf iShiftBits < 0 Or iShiftBits > 31 Then
        Err.Raise 6
    End If
    
    ' If the left most bit that remains will end up in the negative bit
    ' position (&H80000000) we would end up with an overflow if we took the
    ' standard route. We need to strip the left most bit and add it back
    ' afterwards.
    If (lValue And m_l2Power(31 - iShiftBits)) Then
    
        ' (Value And OnBits(31 - (Shift + 1))) chops off the left most bits that
        ' we are shifting into, but also the left most bit we still want as this
        ' is going to end up in the negative bit marker position (&H80000000).
        ' After the multiplication/shift we Or the result with &H80000000 to
        ' turn the negative bit on.
        LShift = ((lValue And m_lOnBits(31 - (iShiftBits + 1))) * _
            m_l2Power(iShiftBits)) Or &H80000000
    
    Else
    
        ' (Value And OnBits(31-Shift)) chops off the left most bits that we are
        ' shifting into so we do not get an overflow error when we do the
        ' multiplication/shift
        LShift = ((lValue And m_lOnBits(31 - iShiftBits)) * _
            m_l2Power(iShiftBits))
        
    End If
End Function

'*******************************************************************************
' RShift (FUNCTION)
'
' PARAMETERS:
' (In) - lValue     - Long    - The value to be shifted
' (In) - iShiftBits - Integer - The number of bits to shift the value by
'
' RETURN VALUE:
' Long - The shifted long integer
'
' DESCRIPTION:
' The right shift of an unsigned long integer involves shifting all the set bits
' to the right and in-filling on the left with zeros. This function is
' equivalent to the >>> operator in Java or the >> operator in C++ when used on
' an unsigned long.
'*******************************************************************************
Private Function RShift(ByVal lValue As Long, _
                        ByVal iShiftBits As Integer) As Long
    
    ' NOTE: If you can guarantee that the Shift parameter will be in the
    ' range 1 to 30 you can safely strip of this first nested if structure for
    ' speed.
    '
    ' A shift of zero is no shift at all
    If iShiftBits = 0 Then
        RShift = lValue
        Exit Function
        
    ' A shift of 31 will clear all bits and move the left most bit to the right
    ' most bit position
    ElseIf iShiftBits = 31 Then
        If lValue And &H80000000 Then
            RShift = 1
        Else
            RShift = 0
        End If
        Exit Function
        
    ' A shift of less than zero or more than 31 is undefined
    ElseIf iShiftBits < 0 Or iShiftBits > 31 Then
        Err.Raise 6
    End If
    
    ' We do not care about the top most bit or the final bit, the top most bit
    ' will be taken into account in the next stage, the final bit (whether it
    ' is an odd number or not) is being shifted into, so we do not give a jot
    ' about it
    RShift = (lValue And &H7FFFFFFE) \ m_l2Power(iShiftBits)
    
    ' If the top most bit (&H80000000) was set we need to do things differently
    ' as in a normal VB signed long integer the top most bit is used to indicate
    ' the sign of the number, when it is set it is a negative number, so just
    ' deviding by a factor of 2 as above would not work.
    ' NOTE: (lValue And  &H80000000) is equivalent to (lValue < 0), you could
    ' get a very marginal speed improvement by changing the test to (lValue < 0)
    If (lValue And &H80000000) Then
        ' We take the value computed so far, and then add the left most negative
        ' bit after it has been shifted to the right the appropriate number of
        ' places
        RShift = (RShift Or (&H40000000 \ m_l2Power(iShiftBits - 1)))
    End If
End Function

'*******************************************************************************
' RShiftSigned (FUNCTION)
'
' PARAMETERS:
' (In) - lValue     - Long    -
' (In) - iShiftBits - Integer -
'
' RETURN VALUE:
' Long -
'
' DESCRIPTION:
' The right shift of a signed long integer involves shifting all the set bits to
' the right and in-filling on the left with the sign bit (0 if positive, 1 if
' negative. This function is equivalent to the >> operator in Java or the >>
' operator in C++ when used on a signed long integer. Not used in this class,
' but included for completeness.
'*******************************************************************************
Private Function RShiftSigned(ByVal lValue As Long, _
                              ByVal iShiftBits As Integer) As Long
    
    ' NOTE: If you can guarantee that the Shift parameter will be in the
    ' range 1 to 30 you can safely strip of this first nested if structure for
    ' speed.
    '
    ' A shift of zero is no shift at all
    If iShiftBits = 0 Then
        RShiftSigned = lValue
        Exit Function
    
    ' A shift of 31 will clear all bits if the left most bit was zero, and will
    ' set all bits if the left most bit was 1 (a negative indicator)
    ElseIf iShiftBits = 31 Then
        
        ' NOTE: (lValue And  &H80000000) is equivalent to (lValue < 0), you
        ' could get a very marginal speed improvement by changing the test to
        ' (lValue < 0)
        If (lValue And &H80000000) Then
            RShiftSigned = -1
        Else
            RShiftSigned = 0
        End If
        Exit Function
    
    ' A shift of less than zero or more than 31 is undefined
    ElseIf iShiftBits < 0 Or iShiftBits > 31 Then
        Err.Raise 6
    End If
    
    ' We get the same result by dividing by the appropriate power of 2 and
    ' rounding in the negative direction
    RShiftSigned = Int(lValue / m_l2Power(iShiftBits))
End Function

'*******************************************************************************
' RotateLeft (FUNCTION)
'
' PARAMETERS:
' (In) - lValue     - Long    - Value to act on
' (In) - iShiftBits - Integer - Bits to move by
'
' RETURN VALUE:
' Long - Result
'
' DESCRIPTION:
' Rotates the bits in a long integer to the left, those bits falling off the
' left edge are put back on the right edge
'*******************************************************************************
Private Function RotateLeft(ByVal lValue As Long, _
                            ByVal iShiftBits As Integer) As Long
    RotateLeft = LShift(lValue, iShiftBits) Or RShift(lValue, (32 - iShiftBits))
End Function

'*******************************************************************************
' AddUnsigned (FUNCTION)
'
' PARAMETERS:
' (In) - lX - Long - First value
' (In) - lY - Long - Second value
'
' RETURN VALUE:
' Long - Result
'
' DESCRIPTION:
' Adds two potentially large unsigned numbers without overflowing
'*******************************************************************************
Private Function AddUnsigned(ByVal lX As Long, _
                             ByVal lY As Long) As Long
    Dim lX4     As Long
    Dim lY4     As Long
    Dim lX8     As Long
    Dim lY8     As Long
    Dim lResult As Long
 
    lX8 = lX And &H80000000
    lY8 = lY And &H80000000
    lX4 = lX And &H40000000
    lY4 = lY And &H40000000
 
    lResult = (lX And &H3FFFFFFF) + (lY And &H3FFFFFFF)
 
    If lX4 And lY4 Then
        lResult = lResult Xor &H80000000 Xor lX8 Xor lY8
    ElseIf lX4 Or lY4 Then
        If lResult And &H40000000 Then
            lResult = lResult Xor &HC0000000 Xor lX8 Xor lY8
        Else
            lResult = lResult Xor &H40000000 Xor lX8 Xor lY8
        End If
    Else
        lResult = lResult Xor lX8 Xor lY8
    End If
 
    AddUnsigned = lResult
End Function

'*******************************************************************************
' F (FUNCTION)
'
' DESCRIPTION:
' MD5's F function
'*******************************************************************************
Private Function f(ByVal x As Long, _
                   ByVal y As Long, _
                   ByVal z As Long) As Long
    f = (x And y) Or ((Not x) And z)
End Function

'*******************************************************************************
' G (FUNCTION)
'
' DESCRIPTION:
' MD5's G function
'*******************************************************************************
Private Function G(ByVal x As Long, _
                   ByVal y As Long, _
                   ByVal z As Long) As Long
    G = (x And z) Or (y And (Not z))
End Function

'*******************************************************************************
' H (FUNCTION)
'
' DESCRIPTION:
' MD5's H function
'*******************************************************************************
Private Function H(ByVal x As Long, _
                   ByVal y As Long, _
                   ByVal z As Long) As Long
    H = (x Xor y Xor z)
End Function

'*******************************************************************************
' I (FUNCTION)
'
' DESCRIPTION:
' MD5's I function
'*******************************************************************************
Private Function i(ByVal x As Long, _
                   ByVal y As Long, _
                   ByVal z As Long) As Long
    i = (y Xor (x Or (Not z)))
End Function

'*******************************************************************************
' FF (SUB)
'
' DESCRIPTION:
' MD5's FF procedure
'*******************************************************************************
Private Sub FF(a As Long, _
               ByVal b As Long, _
               ByVal c As Long, _
               ByVal d As Long, _
               ByVal x As Long, _
               ByVal s As Long, _
               ByVal ac As Long)
    a = AddUnsigned(a, AddUnsigned(AddUnsigned(f(b, c, d), x), ac))
    a = RotateLeft(a, s)
    a = AddUnsigned(a, b)
End Sub

'*******************************************************************************
' GG (SUB)
'
' DESCRIPTION:
' MD5's GG procedure
'*******************************************************************************
Private Sub GG(a As Long, _
               ByVal b As Long, _
               ByVal c As Long, _
               ByVal d As Long, _
               ByVal x As Long, _
               ByVal s As Long, _
               ByVal ac As Long)
    a = AddUnsigned(a, AddUnsigned(AddUnsigned(G(b, c, d), x), ac))
    a = RotateLeft(a, s)
    a = AddUnsigned(a, b)
End Sub

'*******************************************************************************
' HH (SUB)
'
' DESCRIPTION:
' MD5's HH procedure
'*******************************************************************************
Private Sub HH(a As Long, _
               ByVal b As Long, _
               ByVal c As Long, _
               ByVal d As Long, _
               ByVal x As Long, _
               ByVal s As Long, _
               ByVal ac As Long)
    a = AddUnsigned(a, AddUnsigned(AddUnsigned(H(b, c, d), x), ac))
    a = RotateLeft(a, s)
    a = AddUnsigned(a, b)
End Sub

'*******************************************************************************
' II (SUB)
'
' DESCRIPTION:
' MD5's II procedure
'*******************************************************************************
Private Sub II(a As Long, _
               ByVal b As Long, _
               ByVal c As Long, _
               ByVal d As Long, _
               ByVal x As Long, _
               ByVal s As Long, _
               ByVal ac As Long)
    a = AddUnsigned(a, AddUnsigned(AddUnsigned(i(b, c, d), x), ac))
    a = RotateLeft(a, s)
    a = AddUnsigned(a, b)
End Sub

'*******************************************************************************
' ConvertToWordArray (FUNCTION)
'
' PARAMETERS:
' (In/Out) - sMessage - String - String message
'
' RETURN VALUE:
' Long() - Converted message as long array
'
' DESCRIPTION:
' Takes the string message and puts it in a long array with padding according to
' the MD5 rules.
'*******************************************************************************
Private Function ConvertToWordArray(sMessage As String) As Long()
    Dim lMessageLength  As Long
    Dim lNumberOfWords  As Long
    Dim lWordArray()    As Long
    Dim lBytePosition   As Long
    Dim lByteCount      As Long
    Dim lWordCount      As Long
    
    Const MODULUS_BITS      As Long = 512
    Const CONGRUENT_BITS    As Long = 448
    
    lMessageLength = Len(sMessage)
    
    ' Get padded number of words. Message needs to be congruent to 448 bits,
    ' modulo 512 bits. If it is exactly congruent to 448 bits, modulo 512 bits
    ' it must still have another 512 bits added. 512 bits = 64 bytes
    ' (or 16 * 4 byte words), 448 bits = 56 bytes. This means lMessageSize must
    ' be a multiple of 16 (i.e. 16 * 4 (bytes) * 8 (bits))
    lNumberOfWords = (((lMessageLength + _
        ((MODULUS_BITS - CONGRUENT_BITS) \ BITS_TO_A_BYTE)) \ _
        (MODULUS_BITS \ BITS_TO_A_BYTE)) + 1) * _
        (MODULUS_BITS \ BITS_TO_A_WORD)
    ReDim lWordArray(lNumberOfWords - 1)
    
    ' Combine each block of 4 bytes (ascii code of character) into one long
    ' value and store in the message. The high-order (most significant) bit of
    ' each byte is listed first. However, the low-order (least significant) byte
    ' is given first in each word.
    lBytePosition = 0
    lByteCount = 0
    Do Until lByteCount >= lMessageLength
        ' Each word is 4 bytes
        lWordCount = lByteCount \ BYTES_TO_A_WORD
        
        ' The bytes are put in the word from the right most edge
        lBytePosition = (lByteCount Mod BYTES_TO_A_WORD) * BITS_TO_A_BYTE
        lWordArray(lWordCount) = lWordArray(lWordCount) Or _
            LShift(Asc(Mid(sMessage, lByteCount + 1, 1)), lBytePosition)
        lByteCount = lByteCount + 1
    Loop

    ' Terminate according to MD5 rules with a 1 bit, zeros and the length in
    ' bits stored in the last two words
    lWordCount = lByteCount \ BYTES_TO_A_WORD
    lBytePosition = (lByteCount Mod BYTES_TO_A_WORD) * BITS_TO_A_BYTE

    ' Add a terminating 1 bit, all the rest of the bits to the end of the
    ' word array will default to zero
    lWordArray(lWordCount) = lWordArray(lWordCount) Or _
        LShift(&H80, lBytePosition)

    ' We put the length of the message in bits into the last two words, to get
    ' the length in bits we need to multiply by 8 (or left shift 3). This left
    ' shifted value is put in the first word. Any bits shifted off the left edge
    ' need to be put in the second word, we can work out which bits by shifting
    ' right the length by 29 bits.
    lWordArray(lNumberOfWords - 2) = LShift(lMessageLength, 3)
    lWordArray(lNumberOfWords - 1) = RShift(lMessageLength, 29)
    
    ConvertToWordArray = lWordArray
End Function

'*******************************************************************************
' WordToHex (FUNCTION)
'
' PARAMETERS:
' (In) - lValue - Long - Long value to convert
'
' RETURN VALUE:
' String - Hex value to return
'
' DESCRIPTION:
' Takes a long integer and due to the bytes reverse order it extracts the
' individual bytes and converts them to hex appending them for an overall hex
' value
'*******************************************************************************
Private Function WordToHex(ByVal lValue As Long) As String
    Dim lByte As Long
    Dim lCount As Long
    
    For lCount = 0 To 3
        lByte = RShift(lValue, lCount * BITS_TO_A_BYTE) And _
            m_lOnBits(BITS_TO_A_BYTE - 1)
        WordToHex = WordToHex & Right("0" & Hex(lByte), 2)
    Next
End Function

'*******************************************************************************
' MD5 (FUNCTION)
'
' PARAMETERS:
' (In/Out) - sMessage - String - String to be digested
'
' RETURN VALUE:
' String - The MD5 digest
'
' DESCRIPTION:
' This function takes a string message and generates an MD5 digest for it.
' sMessage can be up to the VB string length limit of 2^31 (approx. 2 billion)
' characters.
'
' NOTE: Due to the way in which the string is processed the routine assumes a
' single byte character set. VB passes unicode (2-byte) character strings, the
' ConvertToWordArray function uses on the first byte for each character. This
' has been done this way for ease of use, to make the routine truely portable
' you could accept a byte array instead, it would then be up to the calling
' routine to make sure that the byte array is generated from their string in
' a manner consistent with the string type.
'*******************************************************************************
Public Function MD5Hex(sMessage As String) As String
    Dim x() As Long
    Dim k   As Long
    Dim AA  As Long
    Dim BB  As Long
    Dim CC  As Long
    Dim DD  As Long
    Dim a   As Long
    Dim b   As Long
    Dim c   As Long
    Dim d   As Long
    
    Const S11 As Long = 7
    Const S12 As Long = 12
    Const S13 As Long = 17
    Const S14 As Long = 22
    Const S21 As Long = 5
    Const S22 As Long = 9
    Const S23 As Long = 14
    Const S24 As Long = 20
    Const S31 As Long = 4
    Const S32 As Long = 11
    Const S33 As Long = 16
    Const S34 As Long = 23
    Const S41 As Long = 6
    Const S42 As Long = 10
    Const S43 As Long = 15
    Const S44 As Long = 21

    ' Steps 1 and 2.  Append padding bits and length and convert to words
    x = ConvertToWordArray(sMessage)
    
    ' Step 3.  Initialise
    a = &H67452301
    b = &HEFCDAB89
    c = &H98BADCFE
    d = &H10325476

    ' Step 4.  Process the message in 16-word blocks
    For k = 0 To UBound(x) Step 16
        AA = a
        BB = b
        CC = c
        DD = d
    
        ' The hex number on the end of each of the following procedure calls is
        ' an element from the 64 element table constructed with
        ' T(i) = Int(4294967296 * Abs(Sin(i))) where i is 1 to 64.
        '
        ' However, for speed we don't want to calculate the value every time.
        FF a, b, c, d, x(k + 0), S11, &HD76AA478
        FF d, a, b, c, x(k + 1), S12, &HE8C7B756
        FF c, d, a, b, x(k + 2), S13, &H242070DB
        FF b, c, d, a, x(k + 3), S14, &HC1BDCEEE
        FF a, b, c, d, x(k + 4), S11, &HF57C0FAF
        FF d, a, b, c, x(k + 5), S12, &H4787C62A
        FF c, d, a, b, x(k + 6), S13, &HA8304613
        FF b, c, d, a, x(k + 7), S14, &HFD469501
        FF a, b, c, d, x(k + 8), S11, &H698098D8
        FF d, a, b, c, x(k + 9), S12, &H8B44F7AF
        FF c, d, a, b, x(k + 10), S13, &HFFFF5BB1
        FF b, c, d, a, x(k + 11), S14, &H895CD7BE
        FF a, b, c, d, x(k + 12), S11, &H6B901122
        FF d, a, b, c, x(k + 13), S12, &HFD987193
        FF c, d, a, b, x(k + 14), S13, &HA679438E
        FF b, c, d, a, x(k + 15), S14, &H49B40821
    
        GG a, b, c, d, x(k + 1), S21, &HF61E2562
        GG d, a, b, c, x(k + 6), S22, &HC040B340
        GG c, d, a, b, x(k + 11), S23, &H265E5A51
        GG b, c, d, a, x(k + 0), S24, &HE9B6C7AA
        GG a, b, c, d, x(k + 5), S21, &HD62F105D
        GG d, a, b, c, x(k + 10), S22, &H2441453
        GG c, d, a, b, x(k + 15), S23, &HD8A1E681
        GG b, c, d, a, x(k + 4), S24, &HE7D3FBC8
        GG a, b, c, d, x(k + 9), S21, &H21E1CDE6
        GG d, a, b, c, x(k + 14), S22, &HC33707D6
        GG c, d, a, b, x(k + 3), S23, &HF4D50D87
        GG b, c, d, a, x(k + 8), S24, &H455A14ED
        GG a, b, c, d, x(k + 13), S21, &HA9E3E905
        GG d, a, b, c, x(k + 2), S22, &HFCEFA3F8
        GG c, d, a, b, x(k + 7), S23, &H676F02D9
        GG b, c, d, a, x(k + 12), S24, &H8D2A4C8A
            
        HH a, b, c, d, x(k + 5), S31, &HFFFA3942
        HH d, a, b, c, x(k + 8), S32, &H8771F681
        HH c, d, a, b, x(k + 11), S33, &H6D9D6122
        HH b, c, d, a, x(k + 14), S34, &HFDE5380C
        HH a, b, c, d, x(k + 1), S31, &HA4BEEA44
        HH d, a, b, c, x(k + 4), S32, &H4BDECFA9
        HH c, d, a, b, x(k + 7), S33, &HF6BB4B60
        HH b, c, d, a, x(k + 10), S34, &HBEBFBC70
        HH a, b, c, d, x(k + 13), S31, &H289B7EC6
        HH d, a, b, c, x(k + 0), S32, &HEAA127FA
        HH c, d, a, b, x(k + 3), S33, &HD4EF3085
        HH b, c, d, a, x(k + 6), S34, &H4881D05
        HH a, b, c, d, x(k + 9), S31, &HD9D4D039
        HH d, a, b, c, x(k + 12), S32, &HE6DB99E5
        HH c, d, a, b, x(k + 15), S33, &H1FA27CF8
        HH b, c, d, a, x(k + 2), S34, &HC4AC5665
    
        II a, b, c, d, x(k + 0), S41, &HF4292244
        II d, a, b, c, x(k + 7), S42, &H432AFF97
        II c, d, a, b, x(k + 14), S43, &HAB9423A7
        II b, c, d, a, x(k + 5), S44, &HFC93A039
        II a, b, c, d, x(k + 12), S41, &H655B59C3
        II d, a, b, c, x(k + 3), S42, &H8F0CCC92
        II c, d, a, b, x(k + 10), S43, &HFFEFF47D
        II b, c, d, a, x(k + 1), S44, &H85845DD1
        II a, b, c, d, x(k + 8), S41, &H6FA87E4F
        II d, a, b, c, x(k + 15), S42, &HFE2CE6E0
        II c, d, a, b, x(k + 6), S43, &HA3014314
        II b, c, d, a, x(k + 13), S44, &H4E0811A1
        II a, b, c, d, x(k + 4), S41, &HF7537E82
        II d, a, b, c, x(k + 11), S42, &HBD3AF235
        II c, d, a, b, x(k + 2), S43, &H2AD7D2BB
        II b, c, d, a, x(k + 9), S44, &HEB86D391
    
        a = AddUnsigned(a, AA)
        b = AddUnsigned(b, BB)
        c = AddUnsigned(c, CC)
        d = AddUnsigned(d, DD)
    Next
    
    ' Step 5.  Output the 128 bit digest
    MD5Hex = LCase(WordToHex(a) & WordToHex(b) & WordToHex(c) & WordToHex(d))
End Function

Public Function MD5Bin(sMessage As String) As String
    Dim md5$, i&
    md5 = MD5Hex(sMessage)
    For i = 1 To 32 Step 2
        MD5Bin = MD5Bin & Chr(CLng("&H" & Mid(md5, i, 2)))
    Next
    'For i = 1 To 16
    '    Debug.Print Hex(Asc(Mid(MD5Bin, i, 1)))
    'Next
End Function

Private Sub pr_md5(ByVal tag$, ByVal s$)
    Dim i&, n&, pr$
    For i = 1 To Len(s)
        n = Asc(Mid(s, i, 1))
        pr = pr & Hex(n \ 16 And 15) & Hex(n And 15)
    Next
    Debug.Print tag & ": {" & LCase(pr) & "}"
End Sub

Public Function HMAC_MD5$(ByVal text$, ByVal key$)
    Dim k_ipad$ ' inner padding - key XORd with ipad
    Dim k_opad$ ' outer padding - key XORd with opad
    Dim tmp$
    Dim i&
    ' if key is longer than 64 bytes reset it to key=MD5(key)
    If Len(key) > 64 Then
        tmp = MD5Bin(key)
    Else
        tmp = key
    End If

    '
    ' the HMAC_MD5 transform looks like:
    '
    ' MD5(K XOR opad, MD5(K XOR ipad, text))
    '
    ' where K is an n byte key
    ' ipad is the byte 0x36 repeated 64 times
    ' opad is the byte 0x5c repeated 64 times
    ' and text is the data being protected
    '

    For i = 1 To Len(tmp)
        Dim t&
        t = Asc(Mid(tmp, i, 1))
        k_ipad = k_ipad & Chr(t Xor &H36&)
        k_opad = k_opad & Chr(t Xor &H5C&)
    Next
    For i = Len(tmp) + 1 To 64
        k_ipad = k_ipad & Chr(&H36&)
        k_opad = k_opad & Chr(&H5C&)
    Next
    
    pr_md5 "k_ipad", k_ipad
    pr_md5 "k_opad", k_opad
    Debug.Print "text: (" & Len(text) & ") " & text

    ' "inner" MD5
    tmp = MD5Bin(k_ipad & text)
    
    pr_md5 "inner", tmp
    
    Dim tmp2$
    tmp2 = MD5Bin(k_opad & tmp)
    'pr_md5 tmp2
    ' "outer" MD5
    HMAC_MD5 = MD5Hex(k_opad & tmp)
    
    Debug.Print "result: {" & HMAC_MD5 & "}"
End Function

Public Function CRAM_MD5$(ByVal username$, ByVal password$, ByVal greeting$)
    Dim chal$, hmac$
    chal = Base64Decode(greeting)
    hmac = HMAC_MD5(chal, password)
    CRAM_MD5 = Base64Encode(username & " " & hmac)
End Function



File: /Api Mikrotik\MicrotikTest.vbp
Type=Exe
Reference=*\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\WINDOWS\system32\stdole2.tlb#OLE Automation
Reference=*\G{3F4DACA7-160D-11D2-A8E9-00104B365C9F}#5.5#0#C:\WINDOWS\system32\vbscript.dll\3#Microsoft VBScript Regular Expressions 5.5
Object={248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0; MSWINSCK.OCX
Form=FormMain.frm
Class=CMD5; MD5.cls
IconForm="FormMain"
Startup="FormMain"
Command32=""
Name="MicrotikTest"
HelpContextID="0"
CompatibleMode="0"
MajorVer=1
MinorVer=0
RevisionVer=0
AutoIncrementVer=0
ServerSupportFiles=0
VersionCompanyName="Hunterbt.com"
CompilationType=0
OptimizationType=0
FavorPentiumPro(tm)=0
CodeViewDebugInfo=0
NoAliasing=0
BoundsCheck=0
OverflowCheck=0
FlPointCheck=0
FDIVCheck=0
UnroundedFP=0
StartMode=0
Unattended=0
Retained=0
ThreadPerObject=0
MaxNumberOfThreads=1

[MS Transaction Server]
AutoRefresh=1


File: /Api Mikrotik\MicrotikTest.vbw
FormMain = 406, 115, 1331, 782, , 0, 0, 0, 0, C
CMD5 = 187, 109, 675, 776, 


File: /Form2.frm
VERSION 5.00
Object = "{248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0"; "MSWINSCK.OCX"
Object = "{5E9E78A0-531B-11CF-91F6-C2863C385E30}#1.0#0"; "MSFLXGRD.OCX"
Begin VB.Form Form_MikroTik 
   Caption         =   "Conexin a Puntos de Acceso"
   ClientHeight    =   6165
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   9870
   LinkTopic       =   "Form2"
   ScaleHeight     =   6165
   ScaleWidth      =   9870
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton GetData 
      Caption         =   "Obtener datos"
      Height          =   615
      Left            =   360
      TabIndex        =   12
      Top             =   4080
      Width           =   1455
   End
   Begin VB.TextBox txtIP 
      Height          =   375
      Left            =   840
      TabIndex        =   7
      Top             =   360
      Width           =   1695
   End
   Begin VB.TextBox txtUser 
      Height          =   375
      Left            =   840
      TabIndex        =   6
      Top             =   1080
      Width           =   1695
   End
   Begin VB.TextBox txtPass 
      Height          =   375
      IMEMode         =   3  'DISABLE
      Left            =   840
      MultiLine       =   -1  'True
      PasswordChar    =   ""
      TabIndex        =   5
      Top             =   1560
      Width           =   1575
   End
   Begin VB.TextBox TextCommand 
      Height          =   375
      Left            =   720
      TabIndex        =   4
      Top             =   2160
      Width           =   2655
   End
   Begin VB.CommandButton btnConnect 
      Caption         =   "Conectar"
      Height          =   375
      Left            =   2640
      TabIndex        =   3
      Top             =   1560
      Width           =   1095
   End
   Begin VB.CommandButton btnDisconnect 
      Caption         =   "Desconectar"
      Height          =   375
      Left            =   3840
      TabIndex        =   2
      Top             =   1560
      Width           =   1215
   End
   Begin VB.CommandButton btnSend 
      Caption         =   "Enviar"
      Height          =   375
      Left            =   3480
      TabIndex        =   1
      Top             =   2160
      Width           =   975
   End
   Begin VB.TextBox txtOut 
      Height          =   3255
      Left            =   6360
      Locked          =   -1  'True
      TabIndex        =   0
      Top             =   120
      Width           =   3255
   End
   Begin MSWinsockLib.Winsock ws 
      Left            =   600
      Top             =   0
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   393216
   End
   Begin MSFlexGridLib.MSFlexGrid Grid1 
      Height          =   2775
      Left            =   1920
      TabIndex        =   13
      Top             =   3480
      Visible         =   0   'False
      Width           =   4935
      _ExtentX        =   8705
      _ExtentY        =   4895
      _Version        =   393216
   End
   Begin VB.Label Label4 
      BackColor       =   &H00FFFFFF&
      BackStyle       =   0  'Transparent
      Caption         =   "IP"
      Height          =   255
      Left            =   360
      TabIndex        =   11
      Top             =   480
      Width           =   495
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "SSID"
      Height          =   255
      Left            =   240
      TabIndex        =   10
      Top             =   1200
      Width           =   735
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "Contrasea"
      Height          =   255
      Left            =   0
      TabIndex        =   9
      Top             =   1680
      Width           =   975
   End
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Caption         =   "Comando"
      Height          =   255
      Left            =   0
      TabIndex        =   8
      Top             =   2160
      Width           =   855
   End
End
Attribute VB_Name = "Form_MikroTik"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
'''''''''''''''''CDIGO API````````````````````
Option Explicit

Private inbuf1() As Byte ' 1st stage inbound data
Private inbuf2$ ' 2nd stage ( decoded ) inbound data
Private bErr As Boolean
Private Enum MyState_e
    CONNECTING
    WAITING_KEY
    AUTHENTICATING
    CONNECTED
End Enum
Dim MyState As MyState_e
Dim md5 As New CMD5

Private Sub Out(ByVal s$)
    txtOut.text = txtOut.text & s & vbCrLf
    
End Sub

Private Function GetReply$()
    Dim tmp&
    tmp = InStr(inbuf2, vbLf)
    If 0 = tmp Then Exit Function
    GetReply = Left(inbuf2, tmp - 1)
    inbuf2 = Mid(inbuf2, tmp + 1)
End Function

Private Sub btnConnect_Click()
    bErr = False
    ws.Protocol = sckTCPProtocol
    MyState = CONNECTING
    Out "(Connecting)"
    ws.Connect txtIP.text, 8728
End Sub

Private Function Hexlify$(ByVal s$)
    Dim i&, n&
    For i = 1 To Len(s)
        n = Asc(Mid(s, i, 1))
        Hexlify = Hexlify & LCase(Right("0" & Hex(n), 2))
    Next
End Function

Private Function Unhexlify$(ByVal s$)
    Dim i&, n&
    For i = 1 To Len(s) Step 2
        n = CLng("&H" & Mid(s, i, 2))
        Unhexlify = Unhexlify & Chr(n)
    Next
End Function

Private Sub btnSend_Click()
SendCommand txtCommand.text
End Sub

Private Sub Form_Resize()
    txtOut.Width = Me.ScaleWidth - txtOut.Left
    txtOut.Height = Me.ScaleHeight - txtOut.Top
End Sub

Private Sub Form_Unload(Cancel As Integer)
    bErr = True
    ws.Close
    End
End Sub

Private Sub ws_Connect()
    MyState = WAITING_KEY
    Out "(connected - sending /login)"
    SendCommand ("/login")
End Sub

Private Sub ws_DataArrival(ByVal bytesTotal As Long)
    If bErr Then Exit Sub
    Dim ar() As Byte, i&, inbuf1_len&
    ReDim ar(0 To bytesTotal - 1)
    ws.GetData ar, vbByte, bytesTotal
    On Error Resume Next
    Err.Clear
    inbuf1_len = UBound(inbuf1)
    If Err Then
        inbuf1_len = 0
        ReDim inbuf1(0)
    Else
        inbuf1_len = inbuf1_len + 1
    End If
    On Error GoTo 0
    If inbuf1_len > 0 Then
        Dim off&
        off = inbuf1_len
        ReDim Preserve inbuf1(inbuf1_len + bytesTotal - 1)
        For i = 0 To bytesTotal - 1
            inbuf1(off + i) = ar(i)
        Next
    Else
        inbuf1 = ar
    End If
    Dim WordLen&, StartIdx&, Idx&
    StartIdx = 0
    Do While True
        Idx = StartIdx
        WordLen = CalcWordLen(inbuf1, Idx)
        If WordLen < 0 Then
            Exit Do
        End If
        If WordLen = 0 Then
            SentenceArrived (inbuf2)
            inbuf2 = ""
        Else
            If inbuf1(Idx) = Asc("=") Then
                inbuf2 = inbuf2 & " "
            End If
            For i = 0 To WordLen - 1
                inbuf2 = inbuf2 & Chr(inbuf1(Idx + i))
            Next
        End If
        StartIdx = Idx + WordLen
    Loop
End Sub

Private Sub SentenceArrived(ByVal sent$)
    Dim ar$(), tmp$, i&, re As New RegExp, chal$
    Out "I " & Replace(sent & " <<EOS>>", " ", vbCrLf & "I ")
    Select Case MyState
    Case CONNECTING
        ' this shouldn't happen!
        Out "(connected w/ packet - sending /login)"
        SendCommand "/login"
        MyState = WAITING_KEY
    Case WAITING_KEY
        Out "(got key sending credentials)"
        re.Global = False
        re.Pattern = "^!done =ret=([a-fA-F0-9]+)$"
        On Error Resume Next
        Err.Clear
        If re.Test(sent) Then
            chal = re.Replace(sent, "$1")
        Else
            bErr = True
        End If
        If Err Or bErr Then
            Out "Got error response to initial /login"
            bErr = True
            Exit Sub
        End If
        On Error GoTo 0
        Out md5.MD5Hex(Chr(0))
        Out md5.MD5Hex(Chr(0) & txtPass.text)
        tmp = md5.MD5Hex(Chr(0) & txtPass.text & Unhexlify(chal))
        tmp = "/login =name=" & txtUser.text & " =response=00" & tmp
        SendCommand tmp
        MyState = AUTHENTICATING
    Case AUTHENTICATING
        If Left(sent, 5) <> "!done" Then
            Out "Authentication failure"
            bErr = True
            Exit Sub
        End If
        MyState = CONNECTED
    Case CONNECTED
        ' do nothing - we're already sending output to text box
    End Select
End Sub

Private Function CalcWordLen&(ByRef ar() As Byte, ByRef Idx&)
    Dim tmp&
    CalcWordLen = -1 ' return error by default
    
    ' is there a single byte to begin decoding?
    If Idx > UBound(inbuf1) Then Exit Function
    
    tmp = inbuf1(Idx)
    If tmp < &H80 Then
        Idx = Idx + 1
    ElseIf tmp < &HC0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 1) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HC0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        Idx = Idx + 2
    ElseIf tmp < &HE0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 2) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HE0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        Idx = Idx + 3
    ElseIf tmp < &HF0& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 3) > UBound(inbuf1) Then Exit Function
        tmp = tmp And Not &HF0&
        tmp = tmp * 256 + inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        tmp = tmp * 256 + inbuf1(Idx + 3)
        Idx = Idx + 4
    ElseIf tmp < &HF8& Then
        ' are there enough bytes to fully decode length?
        If (Idx + 4) > UBound(inbuf1) Then Exit Function
        tmp = inbuf1(Idx + 1)
        tmp = tmp * 256 + inbuf1(Idx + 2)
        tmp = tmp * 256 + inbuf1(Idx + 3)
        tmp = tmp * 256 + inbuf1(Idx + 4)
        Idx = Idx + 5
    Else
        bErr = True
        Out "ERROR: Received reserved control byte (0x" & Hex(inbuf1(0)) & ") - connection is indeterminate"
        Exit Function
    End If
    ' is the entire buffer here for which we are asking the length?
    If (Idx + tmp - 1) > UBound(inbuf1) Then Exit Function
    CalcWordLen = tmp
End Function

Private Sub ws_Error(ByVal Number As Integer, Description As String, ByVal Scode As Long, ByVal Source As String, ByVal HelpFile As String, ByVal HelpContext As Long, CancelDisplay As Boolean)
    Out "ws_Error: " & Description
    bErr = True
End Sub

Private Sub EncodeWord(ByRef buf() As Byte, ByVal sWord$)
    Dim DataLen&, HdrLen&, Idx&, tmp&, i&
    DataLen = Len(sWord)
    'If 0 = DataLen Then
    '    DataLen = 1
    '    sWord = Chr(0)
    'End If
    
    On Error Resume Next
    Err.Clear
    Idx = UBound(buf)
    If Err Then
        On Error GoTo 0
        ReDim buf(0)
        Idx = 0
    Else
        Idx = Idx + 1
    End If
    On Error GoTo 0
    If DataLen < &H80& Then
        HdrLen = 1
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        buf(Idx) = DataLen
    ElseIf DataLen < &H4000& Then
        HdrLen = 2
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &H8000&
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    ElseIf DataLen < &H200000 Then
        HdrLen = 3
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &HC00000
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    ElseIf DataLen < &H10000000 Then
        HdrLen = 4
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        tmp = DataLen Or &HE0000000
        buf(Idx + 3) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 0) = tmp
    Else
        HdrLen = 5
        ReDim Preserve buf(0 To Idx + HdrLen + DataLen - 1)
        buf(Idx) = &HF0&
        buf(Idx + 4) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 3) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 2) = tmp And &HFF&
        tmp = tmp \ 256
        buf(Idx + 1) = tmp
    End If
    Idx = Idx + HdrLen - 1 ' Idx is one-less, to make math easier below
    For i = 1 To DataLen
        buf(Idx + i) = Asc(Mid$(sWord, i, 1))
    Next
End Sub

Private Sub SendCommand(ByVal sCmd$)
    Dim ar$(), i&, buf() As Byte
    Out "O " & Replace(sCmd & " <<EOS>>", " ", vbCrLf & "O ")
    ar = Split(sCmd, " ")
    For i = 0 To UBound(ar)
        EncodeWord buf, ar(i)
    Next
    EncodeWord buf, ""
    ws.SendData buf
End Sub

''''''''''''''''''''''FIN CDIGO API''''''''''''''''''

'''''''''''''''''''''''''''SELECCIND DE LOS DATOS'''''''''''''''''''''''''''''
Private Sub GetData_Click()
Grid1.Rows = 10  'filas de la tabla
Grid1.Clear
Grid1.TextMatrix(0, 0) = "Parmetro"    'Ttulos de las columnas
Grid1.TextMatrix(0, 1) = "Valor actual"
Grid1.Visible = True 'Que se muestre la tabla de resultados slo cuando se haga click en el botn
Dim sString As String
Dim fileNum As Integer
fileNum = FreeFile
Open App.Path & "\mensajeAPI.txt" For Input As #fileNum  'Abre el fichero donde estn los datos
Dim y As Integer
Do While Not EOF(fileNum)       'Leer fichero
Line Input #fileNum, sString
If Mid(sString, 4, 4) = "mac-" Then

y = InStrRev(sString, "=")
Grid1.TextMatrix(1, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(1, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 4) = "rx-r" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(2, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(2, 1) = Mid(sString, y + 1)


End If
If Mid(sString, 4, 4) = "tx-r" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(3, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(3, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 4) = "pack" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(4, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(4, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 4) = "upti" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(5, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(5, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 4) = "last" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(6, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(6, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 16) = "signal-strength=" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(7, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(7, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 8) = "signal-t" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(8, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(8, 1) = Mid(sString, y + 1)
End If
If Mid(sString, 4, 16) = "signal-strength-" Then
y = InStrRev(sString, "=")
Grid1.TextMatrix(9, 0) = Mid(sString, 4, y - 4)
Grid1.TextMatrix(9, 1) = Mid(sString, y + 1)
End If
Loop
Grid1.ColAlignment(1) = 2
Close fileNum
End Sub

Private Sub Form_Load()
Grid1.Cols = 2
Grid1.ColWidth(0) = 3000
Grid1.ColWidth(1) = 3000
End Sub



File: /Form_Instrucciones.frm
VERSION 5.00
Object = "{3B7C8863-D78F-101B-B9B5-04021C009402}#1.2#0"; "RICHTX32.OCX"
Begin VB.Form Form_Instrucciones 
   BackColor       =   &H8000000D&
   Caption         =   "Instrucciones"
   ClientHeight    =   6675
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   9405
   LinkTopic       =   "Form1"
   ScaleHeight     =   6675
   ScaleWidth      =   9405
   StartUpPosition =   3  'Windows Default
   Begin RichTextLib.RichTextBox Texto_Instrucciones 
      Height          =   6135
      Left            =   1440
      TabIndex        =   0
      Top             =   240
      Width           =   7455
      _ExtentX        =   13150
      _ExtentY        =   10821
      _Version        =   393217
      ReadOnly        =   -1  'True
      ScrollBars      =   3
      TextRTF         =   $"Form_Instrucciones.frx":0000
   End
End
Attribute VB_Name = "Form_Instrucciones"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Form_Load()
Texto_Instrucciones.FileName = "C:\Documents and Settings\Administrador\Escritorio\TFG\Instrucciones.rtf"
End Sub

Private Sub Form_Resize()

'Primer y segundo parmetro es el valor Left y Top

'Parmetro 3 y 4, el ancho y alto del text _
 que en este caso es el ancho y alto del formulario

Texto_Instrucciones.Move 0, 0, Me.ScaleWidth, Me.ScaleHeight
End Sub



File: /Instrucciones.rtf
{\rtf1\adeflang1025\ansi\ansicpg1252\uc1\adeff38\deff0\stshfdbch0\stshfloch41\stshfhich41\stshfbi41\deflang3082\deflangfe3082\themelang3082\themelangfe0\themelangcs0{\fonttbl{\f0\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\f2\fbidi \fmodern\fcharset0\fprq1{\*\panose 02070309020205020404}Courier New;}
{\f3\fbidi \froman\fcharset2\fprq2{\*\panose 05050102010706020507}Symbol;}{\f10\fbidi \fnil\fcharset2\fprq2{\*\panose 05000000000000000000}Wingdings;}{\f10\fbidi \fnil\fcharset2\fprq2{\*\panose 05000000000000000000}Wingdings;}
{\f38\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0302020204030204}Calibri Light;}{\f41\fbidi \fmodern\fcharset0\fprq2{\*\panose 00000000000000000000}LM Roman 10;}{\f45\fbidi \froman\fcharset0\fprq2{\*\panose 02030602050306030303}Constantia;}
{\flomajor\f31500\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fdbmajor\f31501\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\fhimajor\f31502\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0302020204030204}Calibri Light;}{\fbimajor\f31503\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\flominor\f31504\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fdbminor\f31505\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\fhiminor\f31506\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0502020204030204}Calibri;}{\fbiminor\f31507\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\f46\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\f47\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\f49\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\f50\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\f51\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\f52\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\f53\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\f54\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\f66\fbidi \fmodern\fcharset238\fprq1 Courier New CE;}
{\f67\fbidi \fmodern\fcharset204\fprq1 Courier New Cyr;}{\f69\fbidi \fmodern\fcharset161\fprq1 Courier New Greek;}{\f70\fbidi \fmodern\fcharset162\fprq1 Courier New Tur;}{\f71\fbidi \fmodern\fcharset177\fprq1 Courier New (Hebrew);}
{\f72\fbidi \fmodern\fcharset178\fprq1 Courier New (Arabic);}{\f73\fbidi \fmodern\fcharset186\fprq1 Courier New Baltic;}{\f74\fbidi \fmodern\fcharset163\fprq1 Courier New (Vietnamese);}{\f426\fbidi \fswiss\fcharset238\fprq2 Calibri Light CE;}
{\f427\fbidi \fswiss\fcharset204\fprq2 Calibri Light Cyr;}{\f429\fbidi \fswiss\fcharset161\fprq2 Calibri Light Greek;}{\f430\fbidi \fswiss\fcharset162\fprq2 Calibri Light Tur;}{\f431\fbidi \fswiss\fcharset177\fprq2 Calibri Light (Hebrew);}
{\f432\fbidi \fswiss\fcharset178\fprq2 Calibri Light (Arabic);}{\f433\fbidi \fswiss\fcharset186\fprq2 Calibri Light Baltic;}{\f434\fbidi \fswiss\fcharset163\fprq2 Calibri Light (Vietnamese);}{\f456\fbidi \fmodern\fcharset238\fprq2 LM Roman 10 CE;}
{\f460\fbidi \fmodern\fcharset162\fprq2 LM Roman 10 Tur;}{\f463\fbidi \fmodern\fcharset186\fprq2 LM Roman 10 Baltic;}{\f464\fbidi \fmodern\fcharset163\fprq2 LM Roman 10 (Vietnamese);}{\f496\fbidi \froman\fcharset238\fprq2 Constantia CE;}
{\f497\fbidi \froman\fcharset204\fprq2 Constantia Cyr;}{\f499\fbidi \froman\fcharset161\fprq2 Constantia Greek;}{\f500\fbidi \froman\fcharset162\fprq2 Constantia Tur;}{\f503\fbidi \froman\fcharset186\fprq2 Constantia Baltic;}
{\f504\fbidi \froman\fcharset163\fprq2 Constantia (Vietnamese);}{\flomajor\f31508\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\flomajor\f31509\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\flomajor\f31511\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\flomajor\f31512\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\flomajor\f31513\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\flomajor\f31514\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\flomajor\f31515\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\flomajor\f31516\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\fdbmajor\f31518\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fdbmajor\f31519\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\fdbmajor\f31521\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\fdbmajor\f31522\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fdbmajor\f31523\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\fdbmajor\f31524\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\fdbmajor\f31525\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fdbmajor\f31526\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fhimajor\f31528\fbidi \fswiss\fcharset238\fprq2 Calibri Light CE;}
{\fhimajor\f31529\fbidi \fswiss\fcharset204\fprq2 Calibri Light Cyr;}{\fhimajor\f31531\fbidi \fswiss\fcharset161\fprq2 Calibri Light Greek;}{\fhimajor\f31532\fbidi \fswiss\fcharset162\fprq2 Calibri Light Tur;}
{\fhimajor\f31533\fbidi \fswiss\fcharset177\fprq2 Calibri Light (Hebrew);}{\fhimajor\f31534\fbidi \fswiss\fcharset178\fprq2 Calibri Light (Arabic);}{\fhimajor\f31535\fbidi \fswiss\fcharset186\fprq2 Calibri Light Baltic;}
{\fhimajor\f31536\fbidi \fswiss\fcharset163\fprq2 Calibri Light (Vietnamese);}{\fbimajor\f31538\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbimajor\f31539\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\fbimajor\f31541\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fbimajor\f31542\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbimajor\f31543\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\fbimajor\f31544\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fbimajor\f31545\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbimajor\f31546\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\flominor\f31548\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\flominor\f31549\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\flominor\f31551\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\flominor\f31552\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\flominor\f31553\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\flominor\f31554\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\flominor\f31555\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\flominor\f31556\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fdbminor\f31558\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\fdbminor\f31559\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\fdbminor\f31561\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fdbminor\f31562\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}
{\fdbminor\f31563\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\fdbminor\f31564\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fdbminor\f31565\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}
{\fdbminor\f31566\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fhiminor\f31568\fbidi \fswiss\fcharset238\fprq2 Calibri CE;}{\fhiminor\f31569\fbidi \fswiss\fcharset204\fprq2 Calibri Cyr;}
{\fhiminor\f31571\fbidi \fswiss\fcharset161\fprq2 Calibri Greek;}{\fhiminor\f31572\fbidi \fswiss\fcharset162\fprq2 Calibri Tur;}{\fhiminor\f31573\fbidi \fswiss\fcharset177\fprq2 Calibri (Hebrew);}
{\fhiminor\f31574\fbidi \fswiss\fcharset178\fprq2 Calibri (Arabic);}{\fhiminor\f31575\fbidi \fswiss\fcharset186\fprq2 Calibri Baltic;}{\fhiminor\f31576\fbidi \fswiss\fcharset163\fprq2 Calibri (Vietnamese);}
{\fbiminor\f31578\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbiminor\f31579\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\fbiminor\f31581\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\fbiminor\f31582\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbiminor\f31583\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\fbiminor\f31584\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\fbiminor\f31585\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbiminor\f31586\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}}{\colortbl;\red0\green0\blue0;\red0\green0\blue255;\red0\green255\blue255;\red0\green255\blue0;
\red255\green0\blue255;\red255\green0\blue0;\red255\green255\blue0;\red255\green255\blue255;\red0\green0\blue128;\red0\green128\blue128;\red0\green128\blue0;\red128\green0\blue128;\red128\green0\blue0;\red128\green128\blue0;\red128\green128\blue128;
\red192\green192\blue192;\red0\green112\blue192;}{\*\defchp \f41\fs22\lang3082\langfe1033\langfenp1033 }{\*\defpap \ql \fi624\li0\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 }\noqfpromote {\stylesheet{
\ql \li0\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 \rtlch\fcs1 \af38\afs22\alang1025 \ltrch\fcs0 \f41\fs22\lang2057\langfe1033\cgrid\langnp2057\langfenp1033 \snext0 \sqformat \spriority0 Normal;}{\*
\cs10 \additive \ssemihidden \sunhideused \spriority1 Default Paragraph Font;}{\*
\ts11\tsrowd\trftsWidthB3\trpaddl108\trpaddr108\trpaddfl3\trpaddft3\trpaddfb3\trpaddfr3\trcbpat1\trcfpat1\tblind0\tblindtype3\tsvertalt\tsbrdrt\tsbrdrl\tsbrdrb\tsbrdrr\tsbrdrdgl\tsbrdrdgr\tsbrdrh\tsbrdrv \ql \fi624\li0\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 \rtlch\fcs1 \af41\afs22\alang1025 \ltrch\fcs0 \f41\fs22\lang3082\langfe1033\cgrid\langnp3082\langfenp1033 \snext11 \ssemihidden \sunhideused Normal Table;}{
\s15\ql \li720\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin720\itap0\contextualspace \rtlch\fcs1 \af38\afs22\alang1025 \ltrch\fcs0 \f41\fs22\lang2057\langfe1033\cgrid\langnp2057\langfenp1033 
\sbasedon0 \snext15 \sqformat \spriority34 \styrsid11950777 List Paragraph;}}{\*\listtable{\list\listtemplateid1293875080\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\leveltext
\leveltemplateid201981953\'01\u-3913 ?;}{\levelnumbers;}\f3\fbias0\hres0\chhres0 \fi-360\li1500\lin1500 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext
\leveltemplateid201981955\'01o;}{\levelnumbers;}\f2\fbias0\hres0\chhres0 \fi-360\li2220\lin2220 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981957
\'01\u-3929 ?;}{\levelnumbers;}\f10\fbias0\hres0\chhres0 \fi-360\li2940\lin2940 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981953
\'01\u-3913 ?;}{\levelnumbers;}\f3\fbias0\hres0\chhres0 \fi-360\li3660\lin3660 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981955
\'01o;}{\levelnumbers;}\f2\fbias0\hres0\chhres0 \fi-360\li4380\lin4380 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981957
\'01\u-3929 ?;}{\levelnumbers;}\f10\fbias0\hres0\chhres0 \fi-360\li5100\lin5100 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981953
\'01\u-3913 ?;}{\levelnumbers;}\f3\fbias0\hres0\chhres0 \fi-360\li5820\lin5820 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981955
\'01o;}{\levelnumbers;}\f2\fbias0\hres0\chhres0 \fi-360\li6540\lin6540 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace360\levelindent0{\leveltext\leveltemplateid201981957
\'01\u-3929 ?;}{\levelnumbers;}\f10\fbias0\hres0\chhres0 \fi-360\li7260\lin7260 }{\listname ;}\listid770903581}{\list\listtemplateid1320550536\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace0
\levelindent0{\leveltext\leveltemplateid201981969\'02\'00);}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \fbias0\hres0\chhres0 \fi-360\li720\lin720 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'01.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li1440\lin1440 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'02.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li2160\lin2160 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'03.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li2880\lin2880 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'04.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li3600\lin3600 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'05.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li4320\lin4320 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'06.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5040\lin5040 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'07.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5760\lin5760 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative
\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'08.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li6480\lin6480 }{\listname ;}\listid1081559595}{\list\listtemplateid329185174\listhybrid{\listlevel\levelnfc0
\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace0\levelindent0{\leveltext\leveltemplateid201981969\'02\'00);}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \fbias0\hres0\chhres0 \fi-360\li720\lin720 }{\listlevel\levelnfc4\levelnfcn4
\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'01.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li1440\lin1440 }{\listlevel\levelnfc2\levelnfcn2
\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'02.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li2160\lin2160 }{\listlevel\levelnfc0\levelnfcn0
\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'03.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li2880\lin2880 }{\listlevel\levelnfc4\levelnfcn4
\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'04.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li3600\lin3600 }{\listlevel\levelnfc2\levelnfcn2
\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'05.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li4320\lin4320 }{\listlevel\levelnfc0\levelnfcn0
\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'06.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5040\lin5040 }{\listlevel\levelnfc4\levelnfcn4
\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'07.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5760\lin5760 }{\listlevel\levelnfc2\levelnfcn2
\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'08.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li6480\lin6480 }{\listname ;}\listid1236624600}
{\list\listtemplateid-1093911298\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace0\levelindent0{\leveltext\leveltemplateid833275900\'02\'00);}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 
\fbias0\hres0\chhres0 \fi-360\li1080\lin1080 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'01.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-360\li1800\lin1800 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'02.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-180\li2520\lin2520 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'03.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-360\li3240\lin3240 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'04.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-360\li3960\lin3960 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'05.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-180\li4680\lin4680 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981967\'02\'06.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-360\li5400\lin5400 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981977\'02\'07.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-360\li6120\lin6120 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0\levelindent0{\leveltext\leveltemplateid201981979\'02\'08.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 
\ltrch\fcs0 \hres0\chhres0 \fi-180\li6840\lin6840 }{\listname ;}\listid1656841374}{\list\listtemplateid637938556\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace0\levelindent0{\leveltext
\leveltemplateid-1494943510\'02\'00);}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \ulnone\fbias0\ulc0\hres0\chhres0 \fi-360\li720\lin720 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981977\'02\'01.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li1440\lin1440 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981979\'02\'02.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li2160\lin2160 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981967\'02\'03.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li2880\lin2880 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981977\'02\'04.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li3600\lin3600 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981979\'02\'05.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li4320\lin4320 }{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981967\'02\'06.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5040\lin5040 }{\listlevel\levelnfc4\levelnfcn4\leveljc0\leveljcn0\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981977\'02\'07.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-360\li5760\lin5760 }{\listlevel\levelnfc2\levelnfcn2\leveljc2\leveljcn2\levelfollow0\levelstartat1\lvltentative\levelspace0
\levelindent0{\leveltext\leveltemplateid201981979\'02\'08.;}{\levelnumbers\'01;}\rtlch\fcs1 \af0 \ltrch\fcs0 \hres0\chhres0 \fi-180\li6480\lin6480 }{\listname ;}\listid1774786337}}{\*\listoverridetable{\listoverride\listid1081559595\listoverridecount0\ls1
}{\listoverride\listid1774786337\listoverridecount0\ls2}{\listoverride\listid1656841374\listoverridecount0\ls3}{\listoverride\listid1236624600\listoverridecount0\ls4}{\listoverride\listid770903581\listoverridecount0\ls5}}{\*\rsidtbl \rsid2380049
\rsid2558454\rsid5443677\rsid6835374\rsid8589231\rsid10691267\rsid10958009\rsid11601838\rsid11950777\rsid12734117\rsid13461597}{\mmathPr\mmathFont34\mbrkBin0\mbrkBinSub0\msmallFrac0\mdispDef1\mlMargin0\mrMargin0\mdefJc1\mwrapIndent1440\mintLim0\mnaryLim1}
{\info{\author MONGE SAINZ, ADRIAN}{\operator MONGE SAINZ, ADRIAN}{\creatim\yr2017\mo9\dy1\hr19\min22}{\revtim\yr2017\mo9\dy2\hr18\min4}{\version3}{\edmins41}{\nofpages1}{\nofwords302}{\nofchars1661}{\nofcharsws1960}{\vern39}}{\*\xmlnstbl {\xmlns1 http://
schemas.microsoft.com/office/word/2003/wordml}}\paperw11906\paperh16838\margl1701\margr1701\margt1417\margb1417\gutter0\ltrsect 
\deftab708\widowctrl\ftnbj\aenddoc\hyphhotz425\trackmoves0\trackformatting1\donotembedsysfont1\relyonvml0\donotembedlingdata0\grfdocevents0\validatexml1\showplaceholdtext0\ignoremixedcontent0\saveinvalidxml0
\showxmlerrors1\noxlattoyen\expshrtn\noultrlspc\dntblnsbdb\nospaceforul\formshade\horzdoc\dgmargin\dghspace180\dgvspace180\dghorigin1701\dgvorigin1417\dghshow1\dgvshow1
\jexpand\viewkind1\viewscale100\pgbrdrhead\pgbrdrfoot\splytwnine\ftnlytwnine\htmautsp\nolnhtadjtbl\useltbaln\alntblind\lytcalctblwd\lyttblrtgr\lnbrkrule\nobrkwrptbl\snaptogridincell\allowfieldendsel\wrppunct
\asianbrkrule\rsidroot11950777\newtblstyruls\nogrowautofit\usenormstyforlist\noindnmbrts\felnbrelev\nocxsptable\indrlsweleven\noafcnsttbl\afelev\utinl\hwelev\spltpgpar\notcvasp\notbrkcnstfrctbl\notvatxbx\krnprsnet\cachedcolbal \nouicompat \fet0
{\*\wgrffmtfilter 2450}\nofeaturethrottle1\ilfomacatclnup0\ltrpar \sectd \ltrsect\linex0\headery708\footery708\colsx708\endnhere\sectlinegrid360\sectdefaultcl\sftnbj {\*\pnseclvl1\pnucrm\pnstart1\pnindent720\pnhang {\pntxta .}}{\*\pnseclvl2
\pnucltr\pnstart1\pnindent720\pnhang {\pntxta .}}{\*\pnseclvl3\pndec\pnstart1\pnindent720\pnhang {\pntxta .}}{\*\pnseclvl4\pnlcltr\pnstart1\pnindent720\pnhang {\pntxta )}}{\*\pnseclvl5\pndec\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl6
\pnlcltr\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl7\pnlcrm\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl8\pnlcltr\pnstart1\pnindent720\pnhang {\pntxtb (}{\pntxta )}}{\*\pnseclvl9\pnlcrm\pnstart1\pnindent720\pnhang 
{\pntxtb (}{\pntxta )}}\pard\plain \ltrpar\qc \li0\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0\pararsid11950777 \rtlch\fcs1 \af38\afs22\alang1025 \ltrch\fcs0 
\f41\fs22\lang2057\langfe1033\cgrid\langnp2057\langfenp1033 {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 Instrucciones de uso}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid11950777 
\par }{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid5443677\charrsid5443677 Para la creaci\'f3n de un nuevo proyecto siga las siguientes instrucciones:}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid5443677 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af0\afs22 \ltrch\fcs0 \b\f45\insrsid10958009 \hich\af45\dbch\af0\loch\f45 1)\tab}}\pard\plain \ltrpar\s15\qj \fi-360\li720\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls4\adjustright\rin0\lin720\itap0\pararsid11950777\contextualspace \rtlch\fcs1 \af38\afs22\alang1025 \ltrch\fcs0 \f41\fs22\lang2057\langfe1033\cgrid\langnp2057\langfenp1033 {\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 Seleccionar mapa (entornos I}{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 ndoor): }{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 pulse el bot\'f3n }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 Seleccionar Mapa}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777  para cargar un mapa desde el archivo. Se admi}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 ten formatos de imagen jpg, bmp, gif, png y wmf, p}{
\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 ero se recomienda utilizar mapas en formato wmf ya que se ajustan al tama\'f1o de la ventana que contiene la imagen sin perder calidad. Los mapas de interiores se 
cargan en las tres pes}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 ta\'f1as en el siguiente}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777  orden}{\rtlch\fcs1 \af38 
\ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 :   Mapa 1}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 ,}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009  2\'ba: }{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777  Mapa}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009  }{
\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 2 y}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009  3\'ba:  Mapa 3}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 . }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 
\par }\pard \ltrpar\s15\qj \li720\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin720\itap0\pararsid11950777\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af0\afs22 \ltrch\fcs0 \b\f45\insrsid11950777 \hich\af45\dbch\af0\loch\f45 2)\tab}}\pard \ltrpar\s15\qj \fi-360\li720\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls4\adjustright\rin0\lin720\itap0\pararsid11950777\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 Mapas Outdoor: }{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 en el caso de que se quiera trabajar sobre mapas en entornos exteriores, }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid5443677 
no es necesario utilizar la acci\'f3n }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 Seleccionar Mapa}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777 .}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777  }{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid11950777 
En este caso, se trabajar\'e1 directamente sobre la pesta\'f1a llamada }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid11950777 Mapa Outdoor}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid13461597 . Haciendo uso del buscador situado a la izquierda se puede buscar la ubicaci\'f3n del entorno en el que se van a situar los puntos de acceso con la ayuda de la tecnolog\'eda de Google Maps ya 
sea mediante una direcci\'f3n o mediante coordenada (altitud y longitud).}{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid11950777\charrsid10958009 
\par }\pard \ltrpar\s15\ql \li720\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin720\itap0\pararsid10958009\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af0\afs22 \ltrch\fcs0 \b\f45\insrsid10958009 \hich\af45\dbch\af0\loch\f45 3)\tab}}\pard \ltrpar\s15\qj \fi-360\li720\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls4\adjustright\rin0\lin720\itap0\pararsid10958009\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 A\'f1adir Puntos de Acceso (entornos Indoor): }{
\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 una vez cargado el mapa o los mapas del edificio, se pueden a\'f1adir sobre \'e9ste tantos puntos de acceso como se desee. Para ello se deben seguir los siguiente}{
\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 s}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009  pasos:}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 
\par }\pard \ltrpar\s15\ql \li720\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin720\itap0\pararsid10958009\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af38\afs22 \ltrch\fcs0 \f3\insrsid10958009 \loch\af3\dbch\af0\hich\f3 \'b7\tab}}\pard \ltrpar\s15\qj \fi-360\li1500\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls5\adjustright\rin0\lin1500\itap0\pararsid10958009\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009 P}{\rtlch\fcs1 \af38 \ltrch\fcs0 
\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 ulsar el bot\'f3n }{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10691267 A\'f1adir Punto de Acceso}{\rtlch\fcs1 \af38 
\ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af38\afs22 \ltrch\fcs0 \f3\insrsid10691267 \loch\af3\dbch\af0\hich\f3 \'b7\tab}}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 
Hacer click izquierdo en un punto del mapa sobre el que se situar\'e1 el punto de acceso.}{\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10691267 
\par }\pard \ltrpar\s15\qj \li1500\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin1500\itap0\pararsid10691267\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10691267\charrsid10691267 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af0\afs22 \ltrch\fcs0 \b\f45\insrsid10691267\charrsid10691267 \hich\af45\dbch\af0\loch\f45 4)\tab}}\pard \ltrpar\s15\qj \fi-360\li720\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls4\adjustright\rin0\lin720\itap0\pararsid10691267\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267\charrsid10691267 Etiquetar Puntos de Acceso}{
\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 :  }{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 una vez a\'f1
adidos los puntos de acceso se pueden etiquetar con su direcci\'f3n MAC haciendo click derecho sobre el punto de acceso. Aparecer\'e1 entonces una ventana que nos permitir\'e1 a\'f1adir dicha informaci\'f3n.  Una vez modificada dicha informaci\'f3
n, al desplazar el cursor por encima del punto de acceso aparecer\'e1 dicha etiqueta del router. Adem\'e1s, al hacer doble click sobre el punto de acceso, se mostrar\'e1 una ventana emergente con informaci\'f3n ampliada sobre este.}{\rtlch\fcs1 \af38 
\ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 
\par }\pard \ltrpar\s15\qj \li720\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin720\itap0\pararsid10691267\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267\charrsid10691267 
\par {\listtext\pard\plain\ltrpar \s15 \rtlch\fcs1 \af0\afs22 \ltrch\fcs0 \b\f45\insrsid10691267 \hich\af45\dbch\af0\loch\f45 5)\tab}}\pard \ltrpar\s15\qj \fi-360\li720\ri0\sa160\sl259\slmult1
\widctlpar\wrapdefault\aspalpha\aspnum\faauto\ls4\adjustright\rin0\lin720\itap0\pararsid10691267\contextualspace {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267 Eliminar Puntos de Acceso:}{\rtlch\fcs1 \af38 
\ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid5443677  }{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid5443677 para eliminar un punto de acceso se debe }{\rtlch\fcs1 \af38 \ltrch\fcs0 
\b\f45\fs24\cf17\lang3082\langfe1033\langnp3082\insrsid5443677\charrsid5443677 pulsar la tecla Shift y hacer click izquierdo}{\rtlch\fcs1 \af38 \ltrch\fcs0 \f45\fs24\lang3082\langfe1033\langnp3082\insrsid5443677  sobre el punto de acceso a eliminar. }{
\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\lang3082\langfe1033\langnp3082\insrsid10691267\charrsid10691267 
\par }\pard\plain \ltrpar\qj \li0\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0\pararsid10691267 \rtlch\fcs1 \af38\afs22\alang1025 \ltrch\fcs0 \f41\fs22\lang2057\langfe1033\cgrid\langnp2057\langfenp1033 {
\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10691267\charrsid10691267 
\par }\pard \ltrpar\qj \li0\ri0\sa160\sl259\slmult1\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0\pararsid10958009 {\rtlch\fcs1 \af38 \ltrch\fcs0 \b\f45\fs24\ul\lang3082\langfe1033\langnp3082\insrsid10958009\charrsid10958009 
\par }{\*\themedata 504b030414000600080000002100e9de0fbfff0000001c020000130000005b436f6e74656e745f54797065735d2e786d6cac91cb4ec3301045f748fc83e52d4a
9cb2400825e982c78ec7a27cc0c8992416c9d8b2a755fbf74cd25442a820166c2cd933f79e3be372bd1f07b5c3989ca74aaff2422b24eb1b475da5df374fd9ad
5689811a183c61a50f98f4babebc2837878049899a52a57be670674cb23d8e90721f90a4d2fa3802cb35762680fd800ecd7551dc18eb899138e3c943d7e503b6
b01d583deee5f99824e290b4ba3f364eac4a430883b3c092d4eca8f946c916422ecab927f52ea42b89a1cd59c254f919b0e85e6535d135a8de20f20b8c12c3b0
0c895fcf6720192de6bf3b9e89ecdbd6596cbcdd8eb28e7c365ecc4ec1ff1460f53fe813d3cc7f5b7f020000ffff0300504b030414000600080000002100a5d6
a7e7c0000000360100000b0000005f72656c732f2e72656c73848fcf6ac3300c87ef85bd83d17d51d2c31825762fa590432fa37d00e1287f68221bdb1bebdb4f
c7060abb0884a4eff7a93dfeae8bf9e194e720169aaa06c3e2433fcb68e1763dbf7f82c985a4a725085b787086a37bdbb55fbc50d1a33ccd311ba548b6309512
0f88d94fbc52ae4264d1c910d24a45db3462247fa791715fd71f989e19e0364cd3f51652d73760ae8fa8c9ffb3c330cc9e4fc17faf2ce545046e37944c69e462
a1a82fe353bd90a865aad41ed0b5b8f9d6fd010000ffff0300504b0304140006000800000021006b799616830000008a0000001c0000007468656d652f746865
6d652f7468656d654d616e616765722e786d6c0ccc4d0ac3201040e17da17790d93763bb284562b2cbaebbf600439c1a41c7a0d29fdbd7e5e38337cedf14d59b
4b0d592c9c070d8a65cd2e88b7f07c2ca71ba8da481cc52c6ce1c715e6e97818c9b48d13df49c873517d23d59085adb5dd20d6b52bd521ef2cdd5eb9246a3d8b
4757e8d3f729e245eb2b260a0238fd010000ffff0300504b030414000600080000002100a7259ef29c070000cb200000160000007468656d652f7468656d652f
7468656d65312e786d6cec59cd8b1bc915bf07f23f347d97f5d5ad8fc1f2a24fcfda33b6b164873dd648a5eef2547789aad28cc56208de532e81c026e49085bd
ed21842cecc22eb9e48f31d8249b3f22afaa5bdd5552c99e191c3061463074977eefd5afde7bf5de53d5ddcf5e26d4bbc05c1096f6fcfa9d9aefe174ce16248d
7afeb3d9a4d2f13d2151ba4094a5b8e76fb0f03fbbf7eb5fdd454732c609f6403e1547a8e7c752ae8eaa5531876124eeb0154ee1bb25e30992f0caa3ea82a34b
d09bd06aa3566b55134452df4b51026a6720e32db0f778b92473ecdfdbaa1f53982395420dcc299f2ae5389731b08bf3ba42888d1852ee5d20daf361a605bb9c
e197d2f7281212bee8f935fde757efddada2a35c88ca03b286dc44ffe572b9c0e2bca1e7e4d1593169108441ab5fe8d7002af771e3f6b8356e15fa3400cde7b0
d28c8badb3dd180639d600658f0edda3f6a859b7f086fee61ee77ea83e165e8332fdc11e7e321982152dbc0665f8700f1f0eba8391ad5f83327c6b0fdfaef547
41dbd2af413125e9f91eba16b69ac3ed6a0bc892d16327bc1b06937623575ea2201a8ae852532c592a0fc55a825e303e018002522449eac9cd0a2fd11ce27888
2839e3c43b21510c81b7422913305c6bd426b526fc579f403f698fa2238c0c69c50b9888bd21c5c713734e56b2e73f00adbe0179fbf3cf6f5efff8e6f54f6fbe
faeacdebbfe7736b5596dc314a2353ee97effef09f6f7eebfdfb876f7ff9fa8fd9d4bb7861e2dffded77effef1cff7a9871597a678fba7efdffdf8fddb3ffffe
5f7ffddaa1bdcfd199099f91040bef11bef49eb20416e8e08fcff8f524663122a6443f8d044a919ac5a17f2c630bfd68832872e006d8b6e3730ea9c605bcbf7e
61119ec67c2d8943e3c338b180a78cd101e34e2b3c547319669eadd3c83d395f9bb8a7085db8e61ea2d4f2f278bd821c4b5c2a8731b6683ea1289528c229969e
fa8e9d63ec58dd178458763d2573ce045b4aef0be20d10719a6446ceac682a858e49027ed9b80882bf2ddb9c3ef7068cba563dc2173612f606a20ef2334c2d33
de476b891297ca194aa869f013246317c9e986cf4ddc5848f0748429f3c60b2c844be63187f51a4e7f0869c6edf653ba496c2497e4dca5f30431662247ec7c18
a364e5c24e491a9bd8cfc5398428f29e30e9829f327b87a877f0034a0fbafb39c196bb3f9c0d9e418635299501a2be5973872fef6366c5ef74439708bb524d9f
27568aed73e28c8ec13ab242fb04638a2ed10263efd9e70e0603b6b26c5e927e10435639c6aec07a80ec5855ef2916d8d3cdcd7e9e3c21c20ad9298ed8013ea7
9b9dc4b3416982f821cd8fc0eba6cdc750ea1257003ca6f37313f888401708f1e234ca63013a8ce03ea8f5498cac02a6de853b5e37dcf2df55f618eccb17168d
2bec4b90c1d79681c46ecabcd7363344ad09ca809921e8325ce916442cf79722aab86ab1b5536e696fdad20dd01d594d4f42d20f76403bbd4ff8bfeb7da0c378
fb976f1c9bede3f43b6ec556b2ba66a77328991ceff4378770bb5dcd90f105f9f49b9a115aa74f30d491fd8c75dbd3dcf634feff7d4f73683fdf763287fa8ddb
4ec6870ee3b693c90f573e4e2753362fd0d7a8038feca0471ffb24074f7d9684d2a9dc507c22f4c18f80df338b090c2a397de6898b53c0550c8faaccc104162e
e248cb789cc9df10194f63b482d3a1baaf944422571d096fc5041c1ae961a76e85a7ebe4942db2c3ce7a5d1d6c66955520598ed7c2621c0eaa64866eb5cb03bc
42bd661be983d62d01257b1d12c6643689a683447b3ba88ca48f75c1680e127a651f8545d7c1a2a3d46f5db5c702a8155e811fdc1efc4ceff96100222004e771
d09c2f949f32576fbdab9df9313d7dc89856044083bd8d80d2d35dc5f5e0f2d4eab250bb82a72d1246b8d924b46574832762f8199c47a71abd0a8debfaba5bba
d4a2a74ca1e783d02a69b43bef6371535f83dc6e6ea0a9992968ea5df6fc5633849099a355cf5fc2a1313c262b881da17e73211ac1ddcb5cf26cc3df24b3acb8
902324e2cce03ae964d9202112738f92a4e7abe5176ea0a9ce219a5bbd0109e19325d785b4f2a99103a7db4ec6cb259e4bd3edc688b274f60a193ecb15ce6fb5
f8cdc14a92adc1ddd37871e99dd1357f8a20c4c2765d19704104dc1dd4336b2e085c861589ac8cbf9dc294a75df3364ac750368ee82a46794531937906d7a9bc
a0a3df0a1b186ff99ac1a08649f2427816a9026b1ad5aaa645d5c8381cacba1f1652963392665933adaca2aaa63b8b59336ccbc08e2d6f56e40d565b13434e33
2b7c96ba77536e779beb76fa84a24a80c10bfb39aaee150a8241ad9ccca2a618efa76195b3f351bb766c17f8016a57291246d66f6dd5eed8ada811cee960f046
951fe476a3168696dbbe525b5adf9b9b17dbecec05248f1174b96b2a8576255c5b73040dd154f72459da802df252e65b039ebc35273dffcb5ad80f868d7058a9
75c271256806b54a27ec372bfd306cd6c761bd361a345e41619171520fb33bfb095c60d04d7e73afc7f76eef93ed1dcd9d394baa4cdfca5735717d7b5f6f58b7
f7d94dbc375397f3be4720e97cd96a4cbacdeea055e936fb934a301a742add616b5019b586edd164340c3bddc92bdfbbd0e0a0df1c06ad71a7d2aa0f8795a055
53f43bdd4a3b6834fa41bbdf1907fd57791b032bcfd2476e0b30afe675efbf000000ffff0300504b0304140006000800000021000dd1909fb60000001b010000
270000007468656d652f7468656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73848f4d0ac2301484f78277086f6fd3ba109126dd88
d0add40384e4350d363f2451eced0dae2c082e8761be9969bb979dc9136332de3168aa1a083ae995719ac16db8ec8e4052164e89d93b64b060828e6f37ed1567
914b284d262452282e3198720e274a939cd08a54f980ae38a38f56e422a3a641c8bbd048f7757da0f19b017cc524bd62107bd5001996509affb3fd381a89672f
1f165dfe514173d9850528a2c6cce0239baa4c04ca5bbabac4df000000ffff0300504b01022d0014000600080000002100e9de0fbfff0000001c020000130000
0000000000000000000000000000005b436f6e74656e745f54797065735d2e786d6c504b01022d0014000600080000002100a5d6a7e7c0000000360100000b00
000000000000000000000000300100005f72656c732f2e72656c73504b01022d00140006000800000021006b799616830000008a0000001c0000000000000000
0000000000190200007468656d652f7468656d652f7468656d654d616e616765722e786d6c504b01022d0014000600080000002100a7259ef29c070000cb2000
001600000000000000000000000000d60200007468656d652f7468656d652f7468656d65312e786d6c504b01022d00140006000800000021000dd1909fb60000
001b0100002700000000000000000000000000a60a00007468656d652f7468656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73504b050600000000050005005d010000a10b00000000}
{\*\colorschememapping 3c3f786d6c2076657273696f6e3d22312e302220656e636f64696e673d225554462d3822207374616e64616c6f6e653d22796573223f3e0d0a3c613a636c724d
617020786d6c6e733a613d22687474703a2f2f736368656d61732e6f70656e786d6c666f726d6174732e6f72672f64726177696e676d6c2f323030362f6d6169
6e22206267313d226c743122207478313d22646b3122206267323d226c743222207478323d22646b322220616363656e74313d22616363656e74312220616363
656e74323d22616363656e74322220616363656e74333d22616363656e74332220616363656e74343d22616363656e74342220616363656e74353d22616363656e74352220616363656e74363d22616363656e74362220686c696e6b3d22686c696e6b2220666f6c486c696e6b3d22666f6c486c696e6b222f3e}
{\*\latentstyles\lsdstimax375\lsdlockeddef0\lsdsemihiddendef0\lsdunhideuseddef0\lsdqformatdef0\lsdprioritydef99{\lsdlockedexcept \lsdqformat1 \lsdpriority0 \lsdlocked0 Normal;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 1;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 2;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 3;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 4;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 5;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 6;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 7;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 8;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 9;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 1;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 5;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 6;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 7;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 8;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 9;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 1;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 2;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 3;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 4;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 5;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 6;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 7;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 8;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 9;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Normal Indent;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footnote text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 header;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footer;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index heading;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority35 \lsdlocked0 caption;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 table of figures;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 envelope address;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 envelope return;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footnote reference;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation reference;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 line number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 page number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 endnote reference;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 endnote text;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 table of authorities;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 macro;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 toa heading;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 5;\lsdqformat1 \lsdpriority10 \lsdlocked0 Title;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Closing;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Signature;\lsdsemihidden1 \lsdunhideused1 \lsdpriority1 \lsdlocked0 Default Paragraph Font;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 4;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Message Header;\lsdqformat1 \lsdpriority11 \lsdlocked0 Subtitle;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Salutation;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Date;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text First Indent;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text First Indent 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Note Heading;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Block Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Hyperlink;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 FollowedHyperlink;\lsdqformat1 \lsdpriority22 \lsdlocked0 Strong;
\lsdqformat1 \lsdpriority20 \lsdlocked0 Emphasis;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Document Map;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Plain Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 E-mail Signature;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Top of Form;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Bottom of Form;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Normal (Web);\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Acronym;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Address;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Cite;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Code;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Definition;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Keyboard;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Preformatted;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Sample;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Typewriter;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Variable;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation subject;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 No List;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 1;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Balloon Text;\lsdpriority39 \lsdlocked0 Table Grid;
\lsdsemihidden1 \lsdlocked0 Placeholder Text;\lsdqformat1 \lsdpriority1 \lsdlocked0 No Spacing;\lsdpriority60 \lsdlocked0 Light Shading;\lsdpriority61 \lsdlocked0 Light List;\lsdpriority62 \lsdlocked0 Light Grid;
\lsdpriority63 \lsdlocked0 Medium Shading 1;\lsdpriority64 \lsdlocked0 Medium Shading 2;\lsdpriority65 \lsdlocked0 Medium List 1;\lsdpriority66 \lsdlocked0 Medium List 2;\lsdpriority67 \lsdlocked0 Medium Grid 1;\lsdpriority68 \lsdlocked0 Medium Grid 2;
\lsdpriority69 \lsdlocked0 Medium Grid 3;\lsdpriority70 \lsdlocked0 Dark List;\lsdpriority71 \lsdlocked0 Colorful Shading;\lsdpriority72 \lsdlocked0 Colorful List;\lsdpriority73 \lsdlocked0 Colorful Grid;\lsdpriority60 \lsdlocked0 Light Shading Accent 1;
\lsdpriority61 \lsdlocked0 Light List Accent 1;\lsdpriority62 \lsdlocked0 Light Grid Accent 1;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 1;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 1;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 1;
\lsdsemihidden1 \lsdlocked0 Revision;\lsdqformat1 \lsdpriority34 \lsdlocked0 List Paragraph;\lsdqformat1 \lsdpriority29 \lsdlocked0 Quote;\lsdqformat1 \lsdpriority30 \lsdlocked0 Intense Quote;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 1;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 1;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 1;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 1;\lsdpriority70 \lsdlocked0 Dark List Accent 1;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 1;
\lsdpriority72 \lsdlocked0 Colorful List Accent 1;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 1;\lsdpriority60 \lsdlocked0 Light Shading Accent 2;\lsdpriority61 \lsdlocked0 Light List Accent 2;\lsdpriority62 \lsdlocked0 Light Grid Accent 2;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 2;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 2;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 2;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 2;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 2;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 2;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 2;\lsdpriority70 \lsdlocked0 Dark List Accent 2;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 2;
\lsdpriority72 \lsdlocked0 Colorful List Accent 2;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 2;\lsdpriority60 \lsdlocked0 Light Shading Accent 3;\lsdpriority61 \lsdlocked0 Light List Accent 3;\lsdpriority62 \lsdlocked0 Light Grid Accent 3;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 3;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 3;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 3;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 3;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 3;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 3;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 3;\lsdpriority70 \lsdlocked0 Dark List Accent 3;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 3;
\lsdpriority72 \lsdlocked0 Colorful List Accent 3;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 3;\lsdpriority60 \lsdlocked0 Light Shading Accent 4;\lsdpriority61 \lsdlocked0 Light List Accent 4;\lsdpriority62 \lsdlocked0 Light Grid Accent 4;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 4;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 4;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 4;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 4;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 4;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 4;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 4;\lsdpriority70 \lsdlocked0 Dark List Accent 4;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 4;
\lsdpriority72 \lsdlocked0 Colorful List Accent 4;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 4;\lsdpriority60 \lsdlocked0 Light Shading Accent 5;\lsdpriority61 \lsdlocked0 Light List Accent 5;\lsdpriority62 \lsdlocked0 Light Grid Accent 5;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 5;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 5;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 5;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 5;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 5;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 5;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 5;\lsdpriority70 \lsdlocked0 Dark List Accent 5;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 5;
\lsdpriority72 \lsdlocked0 Colorful List Accent 5;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 5;\lsdpriority60 \lsdlocked0 Light Shading Accent 6;\lsdpriority61 \lsdlocked0 Light List Accent 6;\lsdpriority62 \lsdlocked0 Light Grid Accent 6;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 6;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 6;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 6;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 6;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 6;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 6;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 6;\lsdpriority70 \lsdlocked0 Dark List Accent 6;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 6;
\lsdpriority72 \lsdlocked0 Colorful List Accent 6;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 6;\lsdqformat1 \lsdpriority19 \lsdlocked0 Subtle Emphasis;\lsdqformat1 \lsdpriority21 \lsdlocked0 Intense Emphasis;
\lsdqformat1 \lsdpriority31 \lsdlocked0 Subtle Reference;\lsdqformat1 \lsdpriority32 \lsdlocked0 Intense Reference;\lsdqformat1 \lsdpriority33 \lsdlocked0 Book Title;\lsdsemihidden1 \lsdunhideused1 \lsdpriority37 \lsdlocked0 Bibliography;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority39 \lsdlocked0 TOC Heading;\lsdpriority41 \lsdlocked0 Plain Table 1;\lsdpriority42 \lsdlocked0 Plain Table 2;\lsdpriority43 \lsdlocked0 Plain Table 3;\lsdpriority44 \lsdlocked0 Plain Table 4;
\lsdpriority45 \lsdlocked0 Plain Table 5;\lsdpriority40 \lsdlocked0 Grid Table Light;\lsdpriority46 \lsdlocked0 Grid Table 1 Light;\lsdpriority47 \lsdlocked0 Grid Table 2;\lsdpriority48 \lsdlocked0 Grid Table 3;\lsdpriority49 \lsdlocked0 Grid Table 4;
\lsdpriority50 \lsdlocked0 Grid Table 5 Dark;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 1;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 1;
\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 1;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 1;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 1;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 1;
\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 1;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 2;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 2;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 2;
\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 2;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 2;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 2;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 2;
\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 3;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 3;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 3;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 3;
\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 3;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 3;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 3;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 4;
\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 4;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 4;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 4;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 4;
\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 4;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 4;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 5;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 5;
\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 5;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 5;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 5;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 5;
\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 5;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 6;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 6;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 6;
\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 6;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 6;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 6;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 6;
\lsdpriority46 \lsdlocked0 List Table 1 Light;\lsdpriority47 \lsdlocked0 List Table 2;\lsdpriority48 \lsdlocked0 List Table 3;\lsdpriority49 \lsdlocked0 List Table 4;\lsdpriority50 \lsdlocked0 List Table 5 Dark;
\lsdpriority51 \lsdlocked0 List Table 6 Colorful;\lsdpriority52 \lsdlocked0 List Table 7 Colorful;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 1;\lsdpriority47 \lsdlocked0 List Table 2 Accent 1;\lsdpriority48 \lsdlocked0 List Table 3 Accent 1;
\lsdpriority49 \lsdlocked0 List Table 4 Accent 1;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 1;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 1;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 1;
\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 2;\lsdpriority47 \lsdlocked0 List Table 2 Accent 2;\lsdpriority48 \lsdlocked0 List Table 3 Accent 2;\lsdpriority49 \lsdlocked0 List Table 4 Accent 2;
\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 2;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 2;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 2;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 3;
\lsdpriority47 \lsdlocked0 List Table 2 Accent 3;\lsdpriority48 \lsdlocked0 List Table 3 Accent 3;\lsdpriority49 \lsdlocked0 List Table 4 Accent 3;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 3;
\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 3;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 3;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 4;\lsdpriority47 \lsdlocked0 List Table 2 Accent 4;
\lsdpriority48 \lsdlocked0 List Table 3 Accent 4;\lsdpriority49 \lsdlocked0 List Table 4 Accent 4;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 4;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 4;
\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 4;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 5;\lsdpriority47 \lsdlocked0 List Table 2 Accent 5;\lsdpriority48 \lsdlocked0 List Table 3 Accent 5;
\lsdpriority49 \lsdlocked0 List Table 4 Accent 5;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 5;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 5;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 5;
\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 6;\lsdpriority47 \lsdlocked0 List Table 2 Accent 6;\lsdpriority48 \lsdlocked0 List Table 3 Accent 6;\lsdpriority49 \lsdlocked0 List Table 4 Accent 6;
\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 6;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 6;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 6;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Mention;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Smart Hyperlink;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Hashtag;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Unresolved Mention;}}{\*\datastore 010500000200000018000000
4d73786d6c322e534158584d4c5265616465722e362e3000000000000000000000060000
d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff090006000000000000000000000001000000010000000000000000100000feffffff00000000feffffff0000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffdfffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffffffffffff0c6ad98892f1d411a65f0040963251e500000000000000000000000060c1
63360524d301feffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000105000000000000}}

File: /Jenkinsfile
pipeline {
  agent any
  stages {
    stage('Parallel execution') {
      parallel {
        stage('Say Hello') {
          steps {
            sh 'echo "hello world"'
          }
        }

        stage('build app') {
          agent {
            docker {
              image 'gradle:6.8.3-jdk11'
            }

          }
          steps {
            sh 'ci/build-app.sh'
            archiveArtifacts 'app/build/libs/'
          }
        }

      }
    }

  }
}

File: /mensajeAPI.txt
(Connecting)
(connected - sending /login)
O /login
O <<EOS>>
I !done
I =ret=4fbdf0ed87c5d39c635f734f83b4162c
I <<EOS>>
(got key sending credentials)
93b885adfe0da089cdf634904fd59f71
2c3cd2a44be10b9689cd3faa7617a345
O /login
O =name=admin
O =response=006464ed7bd335b5ce531b0c29bcf9c672
O <<EOS>>
I !done
I =ret=4fbdf0ed87c5d39c635f734f83b4162c
I <<EOS>>
I !done
O /interface/wireless/registration-table/print
O <<EOS>>
I !done
I =ret=10d70e14c3ab58dffddfbe534af5cfa0
I <<EOS>>
I !done
I <<EOS>>
I !re
I =.id=*2
I =interface=wlan1
I =mac-address=B8:64:91:68:1C:50
I =ap=false
I =wds=false
I =bridge=false
I =rx-rate=65Mbps-20MHz/1S
I =tx-rate=11Mbps
I =packets=122,172
I =bytes=13265,14518
I =frames=122,172
I =frame-bytes=12533,13486
I =hw-frames=123,206
I =hw-frame-bytes=15584,18430
I =tx-frames-timed-out=0
I =uptime=46s
I =last-activity=190ms
I =signal-strength=-38@HT20-7
I =signal-to-noise=49
I =signal-strength-ch0=-38
I =evm-ch0=29
I =strength-at-rates=-33@1Mbps
I 2s910ms,-38@6Mbps
I 2s520ms,-36@HT20-1
I 20s160ms,-38@HT20-6
I 7s330ms,-38@HT20-7
I 190ms
I =tx-ccq=105
I =p-throughput=6199
I =distance=1
I =last-ip=192.168.100.253
I =802.1x-port-enabled=true
I =management-protection=false
I =wmm-enabled=true
I =tx-rate-set=CCK:1-11
I OFDM:6-54
I BW:1x
I HT:0-7
I <<EOS>>
I !done
I <<EOS>>


File: /Pin.ctl
VERSION 5.00
Begin VB.UserControl Pin 
   BackColor       =   &H00C0C0C0&
   BackStyle       =   0  'Transparent
   CanGetFocus     =   0   'False
   ClientHeight    =   480
   ClientLeft      =   0
   ClientTop       =   0
   ClientWidth     =   480
   MaskColor       =   &H00C0C0C0&
   MaskPicture     =   "Pin.ctx":0000
   MouseIcon       =   "Pin.ctx":008C
   Picture         =   "Pin.ctx":02AA
   ScaleHeight     =   480
   ScaleWidth      =   480
End
Attribute VB_Name = "Pin"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit

'We rely on mask transparency, so Picture must be our image and MaskPicture must
'be a "cutout" image with transparent areas = BackColor.

Private Const DEFAULT_COLOR = vbRed 'This must match the color of our background Picture
                                    'bitmap's areas to be recolored when Color is assigned
                                    'a new value.

Private Const DIB_RGB_COLORS As Long = 0&
Private Const BI_RGB As Long = 0&

Private Type BITMAPINFOHEADER
    biSize As Long
    biWidth As Long
    biHeight As Long
    biPlanes As Integer
    biBitCount As Integer
    biCompression As Long
    biSizeImage As Long
    biXPelsPerMeter As Long
    biYPelsPerMeter As Long
    biClrUsed As Long
    biClrImportant As Long
End Type
'
'Private Type RGBQUAD
'    rgbBlue As Byte
'    rgbGreen As Byte
'    rgbRed As Byte
'    rgbReserved As Byte
'End Type

Private Type BITMAPINFO
    bmiHeader As BITMAPINFOHEADER
    'bmiColors(255) As RGBQUAD 'Not used here, we work with 24-bit color.
End Type

Private Declare Function GetDIBits Lib "gdi32" ( _
    ByVal hDC As Long, _
    ByVal hBitmap As Long, _
    ByVal nStartScan As Long, _
    ByVal nNumScans As Long, _
    ByRef Bits As Byte, _
    ByRef BI As BITMAPINFO, _
    ByVal wUsage As Long) As Long

Private Declare Function GetSysColor Lib "user32" (ByVal nIndex As Long) As Long

Private Declare Function SetDIBits Lib "gdi32" ( _
    ByVal hDC As Long, _
    ByVal hBitmap As Long, _
    ByVal nStartScan As Long, _
    ByVal nNumScans As Long, _
    ByRef Bits As Byte, _
    ByRef BI As BITMAPINFO, _
    ByVal wUsage As Long) As Long

Private ColorR As Byte
Private ColorG As Byte
Private ColorB As Byte

Private mColor As Long

Public Event Click()

Public Property Get Color() As OLE_COLOR
    Color = mColor
End Property

Public Property Let Color(ByVal RHS As OLE_COLOR)
    Dim RGBQUAD As Long
    Dim NewR As Byte
    Dim NewG As Byte
    Dim NewB As Byte
    Dim WidthPx As Long
    Dim HeightPx As Long
    Dim bmi As BITMAPINFO
    Dim Stride As Long
    Dim Triples() As Byte
    Dim Line As Long
    Dim Pixel As Long
    
    mColor = RHS
    If mColor And &H80000000 Then
        RGBQUAD = GetSysColor(mColor And &HFFFF&)
    Else
        RGBQUAD = mColor
    End If
    NewR = RGBQUAD And &HFF&
    NewG = (RGBQUAD And &HFF00&) \ &H100&
    NewB = RGBQUAD \ &H10000

    With UserControl
        WidthPx = ScaleX(.Picture.Width, vbHimetric, vbPixels)
        HeightPx = ScaleY(.Picture.Height, vbHimetric, vbPixels)
        With bmi.bmiHeader
            .biSize = Len(bmi.bmiHeader)
            .biWidth = WidthPx
            .biHeight = HeightPx
            .biPlanes = 1
            .biCompression = BI_RGB
            .biBitCount = 24
        End With
        Stride = ((3 * WidthPx + 3) \ 4) * 4
        ReDim Triples(Stride * HeightPx - 1)
        .AutoRedraw = True
        GetDIBits .hDC, .Image.Handle, 0, HeightPx, Triples(0), bmi, DIB_RGB_COLORS
        For Line = 0 To (HeightPx - 1) * Stride Step Stride
            For Pixel = Line To Line + (WidthPx - 1) * 3 Step 3
                If Triples(Pixel + 2) = ColorR And _
                   Triples(Pixel + 1) = ColorG And _
                   Triples(Pixel) = ColorB Then
                        Triples(Pixel + 2) = NewR
                        Triples(Pixel + 1) = NewG
                        Triples(Pixel) = NewB
                End If
            Next
        Next
        SetDIBits .hDC, .Image.Handle, 0, HeightPx, Triples(0), bmi, DIB_RGB_COLORS
        .AutoRedraw = False
    End With

    ColorR = NewR
    ColorG = NewG
    ColorB = NewB

    PropertyChanged "Color"
End Property

Private Sub SetUpDefaultColor()
    Dim RGBQUAD As Long
    'These must match the parts of the original Picture bitmap that we recolorize via our
    'Color property, i.e. they are the default Color:
    mColor = DEFAULT_COLOR
    If mColor And &H80000000 Then
        RGBQUAD = GetSysColor(mColor And &HFFFF&)
    Else
        RGBQUAD = mColor
    End If
    ColorR = RGBQUAD And &HFF&
    ColorG = (RGBQUAD And &HFF00&) \ &H100&
    ColorB = RGBQUAD \ &H10000
End Sub

Private Sub UserControl_Click()
    RaiseEvent Click
End Sub

Private Sub UserControl_InitProperties()
    SetUpDefaultColor
End Sub

Private Sub UserControl_MouseDown(Button As Integer, Shift As Integer, X As Single, Y As Single)
    Dim NewText As String
    
    If Button = vbLeftButton Then
        MousePointer = vbCustom
    ElseIf Button = vbRightButton Then
        With Extender
            'This could be fancier, but we'll just use InputBox() for this:
            NewText = InputBox("Edit toolltip text", _
                               , _
                               .ToolTipText, _
                               .Parent.Left + X, _
                               .Parent.Top + Y)
            If StrPtr(NewText) <> 0 Then .ToolTipText = NewText
        End With
    End If
End Sub

Private Sub UserControl_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
    If Button = vbLeftButton Then
        With Extender
            .Move .Left + X - .Width / 2, .Top + Y - .Height / 2
        End With
    End If
End Sub

Private Sub UserControl_MouseUp(Button As Integer, Shift As Integer, X As Single, Y As Single)
    MousePointer = vbDefault
End Sub

Private Sub UserControl_Paint()
    Size 480, 480
End Sub

Private Sub UserControl_ReadProperties(PropBag As PropertyBag)
    SetUpDefaultColor 'We need to do this here to assign the initial ColorR, ColorG, and ColorB values.
    With PropBag
        Color = .ReadProperty("Color", DEFAULT_COLOR)
    End With
End Sub

Private Sub UserControl_WriteProperties(PropBag As PropertyBag)
    With PropBag
        .WriteProperty "Color", Color, DEFAULT_COLOR
    End With
End Sub


File: /prueba.txt
Parmetro;Valor actual
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;
;


File: /README.md
# mikrotik-router-management
A simple MikroTik access points management App developed during my Final Degree Project.


File: /Registros\Registro_Datos.txt
#MAC; RbRx; RbTx; PKTs; Tact; LastAct; RSSI; SNR; CCQtx; Throughput; IP; Mod#
;40:B8:9A:5B:C8:8B;58.5Mbps-20MHz/1S;65Mbps-20MHz/1S;1902,3993;27m38s;0ms;-42@HT20-6;46 dB;100%;61197Kbps;192.168.100.250;CCK:1-11;;

B8:64:91:68:1C:50;65Mbps-20MHz/1S;65Mbps-20MHz/1S;1046,1149;21m57s;960ms;-32@6Mbps;56 dB;100%;61197Kbps;192.168.100.253;CCK:1-11;;40:B8:9A:5B:C8:8B;

58.5Mbps-20MHz/1S;65Mbps-20MHz/1S;1905,3998;27m39s;10ms;-42@HT20-6;46 dB;100%;61197Kbps;192.168.100.250;CCK:1-11;;B8:64:91:68:1C:50;65Mbps-20MHz/1S;

65Mbps-20MHz/1S;1047,1150;21m58s;500ms;-32@6Mbps;56 dB;100%;61197Kbps;192.168.100.253;CCK:1-11;;40:B8:9A:5B:C8:8B;65Mbps-20MHz/1S;65Mbps-20MHz/1S;

1917,4036;27m49s;0ms;-42@HT20-6;46 dB;100%;61197Kbps;192.168.100.250;CCK:1-11;;B8:64:91:68:1C:50;65Mbps-20MHz/1S;65Mbps-20MHz/1S;1051,1154;

22m9s;60ms;-34@6Mbps;54 dB;100%;61197Kbps;192.168.100.253;CCK:1-11;;40:B8:9A:5B:C8:8B;65Mbps-20MHz/1S;65Mbps-20MHz/1S;1937,4079;28m7s;

0ms;-39@HT20-6;49 dB;100%;61197Kbps;192.168.100.250;CCK:1-11;;;;;;;;

;

File: /TFG.frm
VERSION 5.00
Begin VB.Form Form_Inicio 
   BackColor       =   &H8000000D&
   Caption         =   "Inicio"
   ClientHeight    =   3210
   ClientLeft      =   165
   ClientTop       =   855
   ClientWidth     =   7875
   LinkTopic       =   "Form1"
   ScaleHeight     =   3210
   ScaleWidth      =   7875
   StartUpPosition =   3  'Windows Default
   Begin VB.Frame Frame1 
      BackColor       =   &H8000000D&
      Caption         =   "Seleccione una opcin para comenzar"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   7080
      TabIndex        =   0
      Top             =   3360
      Width           =   5055
      Begin VB.CommandButton abrirAPI_Mikrotik 
         Caption         =   "Conectarse a un punto de acceso"
         Height          =   735
         Left            =   2520
         TabIndex        =   2
         Top             =   480
         Width           =   1815
      End
      Begin VB.CommandButton NuevoProyecto 
         Caption         =   "Comenzar un nuevo proyecto"
         Height          =   735
         Left            =   240
         TabIndex        =   1
         Top             =   480
         Width           =   1935
      End
   End
   Begin VB.Menu Opciones 
      Caption         =   "Opciones"
      Begin VB.Menu Opcion1 
         Caption         =   "Opcin 1"
      End
      Begin VB.Menu Salir 
         Caption         =   "Salir"
      End
   End
   Begin VB.Menu Herramientas 
      Caption         =   "Herramientas"
      Begin VB.Menu CrearMapa 
         Caption         =   "Crear nuevo mapa"
      End
      Begin VB.Menu Herramienta2 
         Caption         =   "Herramienta 2"
      End
   End
End
Attribute VB_Name = "Form_Inicio"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub abrirAPI_Mikrotik_Click()
Form_MikroTik.Show
End Sub




' Private xo!, yo! ' Orig X&Y of Mouse on Drag Object
' Private Sub AccessPoint_MouseMove(Button As Integer, Shift As Integer, x As Single, y As Single)

  ' -- Save Orig X&Y of Obj..
  ' xo! = x: yo! = y
  ' If Shift = 0 Then AccessPoint.DragMode = 0: Exit Sub
  ' AccessPoint.DragMode = 1
 
' End Sub
 
' Private Sub Form1_DragDrop(Source As Control, x As Single, y As Single)
  ' If Source.Name = "AccessPoint" Then AccesPoint.Move x - xo!, y - yo!: AccesPoint.DragMode = 0
 
' End Sub



Private Sub Command1_Click()

Dim RutaMapa1, RutaMapa2, RutaMapa3 As String   'esta declaracion debes ponerla al principio del codigo de tu form (no en el evento click del command. Notaras que es una variable publica por lo que debe estar disponible en cualquier momento)

With CommonDialog1
     .DialogTitle = "SELECCIONE UN MAPA"
     .Filter = "Imagenes (*.jpg, *.bmp, *.gif, *.png, *.wmf) |*.jpg; *.bmp; *.gif; *.png; *.wmf|"
     .ShowOpen
End With

If CommonDialog1.FileName <> "" Then

    If picMap.Picture = 0 Then
        picMap.Picture = LoadPicture(CommonDialog1.FileName)
        RutaMapa1 = CommonDialog1.FileName  'FileName trae, ademas del nombre del archivo, la ruta completa de alojamiento del archivo
    ElseIf Picture2.Picture = 0 Then
        Picture2.Picture = LoadPicture(CommonDialog1.FileName)
        RutaMapa2 = CommonDialog1.FileName
    ElseIf Picture3.Picture = 0 Then
        Picture3.Picture = LoadPicture(CommonDialog1.FileName)
        RutMapa3 = CommonDialog1.FileName
    End If
     
Else
     MsgBox "No seleccion ninguna imagen"
     RutaImagen = ""
End If

End Sub

Private Sub CrearMapa_Click()

Dim AbrirGenCDB

AbrirGenCDB = Shell("C:\Archivos de programa\GenCDB v4.0\GenCDB.EXE", 1)

End Sub




Private Sub FiltroDatos_Click()
Dim aux As String
Dim aux2 As String
Dim nombre As String
Dim poblacion As String
nombre = Text1.text
poblacion = Text2.text
Adodc1.Recordset.MoveFirst
    Do While Not Adodc1.Recordset.EOF
        aux = Adodc1.Recordset.Fields("NombreVendedor")
        aux2 = Adodc1.Recordset.Fields("Poblacion")
        If nombre = aux And poblacion = aux2 Then
            MsgBox "El grupo que busca es " & nombre & " " & poblacion & " ", vbOKOnly
        Exit Sub
        Else
        Adodc1.Recordset.MoveNext
        End If
        Loop
        MsgBox ("La persona no existe")
        Adodc1.Recordset.MoveFirst
        
End Sub


Private Sub NuevoProyecto_Click()
Form_Mapas.Show
End Sub


'Private Sub Form_Load()
'SSTab1.Tab = 0 'Aparece por defecto la primera pestaa seleccionada
'SaveSizes
'PinColorIndex = -1
'NewPinIndex = -1
'End Sub



Private Sub Salir_Click()

If MsgBox("Est seguro de que quiere salir de la aplicacin?", vbQuestion + vbYesNo, "Cerrar aplicacin") = vbYes Then
    End
End If

End Sub

''''''''''''''''''''''''''''''''''''''
'API GOOGLE MAPS'
''''''''''''''''''''''''''''''''''''''

'Private Type ControlPositionType
    'Left As Single
    'Top As Single
    'Width As Single
    'Height As Single
    'FontSize As Single
'End Type

'Private m_ControlPositions() As ControlPositionType
'Private m_FormWid As Single
'Private m_FormHgt As Single

'Private Sub SaveSizes()
'Dim i As Integer
'Dim ctl As Control
' Save the controls' positions and sizes.
'ReDim m_ControlPositions(1 To Controls.Count)
'i = 1
'For Each ctl In Controls
    'With m_ControlPositions(i)
        'If TypeOf ctl Is Line Then
            '.Left = ctl.X1
            '.Top = ctl.Y1
            '.Width = ctl.X2 - ctl.X1
            '.Height = ctl.Y2 - ctl.Y1
        'Else
            '.Left = ctl.Left
            '.Top = ctl.Top
            '.Width = ctl.Width
            '.Height = ctl.Height
            'On Error Resume Next
            '.FontSize = ctl.Font.Size
            'On Error GoTo 0
        'End If
    'End With
    'i = i + 1
'Next ctl
' Save the form's size.
'm_FormWid = ScaleWidth
'm_FormHgt = ScaleHeight
'End Sub

Private Sub BuscarDireccion_Click()
Dim street As String
Dim city As String
Dim state As String
Dim zip As String
Dim queryAddress As String
queryAddress = "http://maps.google.com/maps?q="
' build street part of query string
If txtStreet.text <> "" Then
    street = txtStreet.text
    queryAddress = queryAddress & street + "," & "+"
End If
' build city part of query string
If txtCity.text <> "" Then
    city = txtCity.text
    queryAddress = queryAddress & city + "," & "+"
End If
' build state part of query string
If txtState.text <> "" Then
    state = txtState.text
    queryAddress = queryAddress & state + "," & "+"
End If
' build zip code part of query string
If txtZipCode.text <> "" Then
    zip = txtZipCode.text
    queryAddress = queryAddress & zip
End If
' pass the url with the query string to web browser control
'WebBrowser1.Navigate queryAddress
End Sub

Private Sub BuscarCoordenadas_Click()
If txtLat.text = "" Or txtLong.text = "" Then
    MsgBox "Supply a latitude and longitude value.", "Missing Data"
End If
Dim lat As String
Dim lon As String
Dim queryAddress As String
queryAddress = "http://maps.google.com/maps?q="
If txtLat.text <> "" Then
    lat = txtLat.text
    queryAddress = queryAddress & lat + "%2C"
End If
' build longitude part of query string
If txtLong.text <> "" Then
    lon = txtLong.text
    queryAddress = queryAddress & lon
End If
'WebBrowser1.Navigate queryAddress
End Sub


'Private Sub Form_Resize()
'ResizeControls
'End Sub

'Private Sub ResizeControls()
'Dim i As Integer
'Dim ctl As Control
'Dim x_scale As Single
'Dim y_scale As Single
' Don't bother if we are minimized.
'If WindowState = vbMinimized Then Exit Sub
'Get the form's current scale factors.
'x_scale = ScaleWidth / m_FormWid
'y_scale = ScaleHeight / m_FormHgt
' Position the controls.
'i = 1
'For Each ctl In Controls
    'With m_ControlPositions(i)
        'If TypeOf ctl Is Line Then
            'ctl.X1 = x_scale * .Left
            'ctl.Y1 = y_scale * .Top
            'ctl.X2 = ctl.X1 + x_scale * .Width
            'ctl.Y2 = ctl.Y1 + y_scale * .Height
        'Else
            'ctl.Left = x_scale * .Left
            'ctl.Top = y_scale * .Top
            'ctl.Width = x_scale * .Width
            'If Not (TypeOf ctl Is ComboBox) Then
                ' Cannot change height of ComboBoxes.
                'ctl.Height = y_scale * .Height
            'End If
            'On Error Resume Next
            'ctl.Font.Size = y_scale * .FontSize
            'On Error GoTo 0
        'End If
    'End With
    'i = i + 1
'Next ctl
'End Sub






File: /TFG.vbp
Type=Exe
Reference=*\G{00020430-0000-0000-C000-000000000046}#2.0#0#..\..\..\..\WINDOWS\system32\stdole2.tlb#OLE Automation
Reference=*\G{00025E01-0000-0000-C000-000000000046}#4.0#0#..\..\..\..\Archivos de programa\Archivos comunes\Microsoft Shared\DAO\DAO350.DLL#Microsoft DAO 3.51 Object Library
Object={410381CD-AF42-11D1-8F10-00C04FC2C17B}#1.0#0; comsnap.dll
Reference=*\G{CD3386A5-DBB9-11D1-B58F-00C04FB68DF3}#b.0#0#..\..\..\..\Archivos de programa\Archivos comunes\Microsoft Shared\Repostry\MIGV2.DLL#ActiveX DLL to perform Migration of MS Repository V1 to V2
Reference=*\G{00000300-0000-0010-8000-00AA006D2EA4}#2.8#0#..\..\..\..\Archivos de programa\Archivos comunes\system\ado\msador15.dll#Microsoft ActiveX Data Objects Recordset 2.8 Library
Reference=*\G{2A75196C-D9EB-4129-B803-931327F72D5C}#2.8#0#..\..\..\..\Archivos de programa\Archivos comunes\system\ado\msado15.dll#Microsoft ActiveX Data Objects 2.8 Library
Reference=*\G{56BF9020-7A2F-11D0-9482-00A0C91110ED}#1.0#0#..\..\..\..\WINDOWS\system32\MSBIND.DLL#Microsoft Data Binding Collection
Reference=*\G{3F4DACA7-160D-11D2-A8E9-00104B365C9F}#5.5#0#..\..\..\..\WINDOWS\system32\vbscript.dll\3#Microsoft VBScript Regular Expressions 5.5
Object={F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0; COMDLG32.OCX
Object={BDC217C8-ED16-11CD-956C-0000C04E4C0A}#1.1#0; TABCTL32.OCX
Object={CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0; MSDATGRD.OCX
Object={67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0; MSADODC.OCX
Object={248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0; MSWINSCK.OCX
Object={5E9E78A0-531B-11CF-91F6-C2863C385E30}#1.0#0; MSFLXGRD.OCX
Object={3B7C8863-D78F-101B-B9B5-04021C009402}#1.2#0; RICHTX32.OCX
Form=TFG.frm
UserControl=..\drag and drop\Pin.ctl
Form=..\drag and drop\Form1.frm
Form=Form_Instrucciones.frm
Form=..\Api mikrotik\FormMain.frm
Class=CMD5; ..\Api mikrotik\MD5.cls
Object={65E121D4-0C60-11D2-A9FC-0000F8754DA1}#2.0#0; MSCHRT20.OCX
Object={02B5E320-7292-11CF-93D5-0020AF99504A}#1.0#0; MSCHART.OCX
Form=..\graficos\Form1.frm
Module=Module1; ..\graficos\Module1.bas
IconForm="Form_Inicio"
Startup="Form_Inicio"
HelpFile=""
Title="TFG"
ExeName32="TFG ejecutable.exe"
Command32=""
Name="Project1"
HelpContextID="0"
CompatibleMode="0"
MajorVer=1
MinorVer=0
RevisionVer=0
AutoIncrementVer=0
ServerSupportFiles=0
CompilationType=0
OptimizationType=0
FavorPentiumPro(tm)=0
CodeViewDebugInfo=0
NoAliasing=0
BoundsCheck=0
OverflowCheck=0
FlPointCheck=0
FDIVCheck=0
UnroundedFP=0
StartMode=0
Unattended=0
Retained=0
ThreadPerObject=0
MaxNumberOfThreads=1
DebugStartupOption=0

[MS Transaction Server]
AutoRefresh=1


File: /TFG.vbw
Form_Inicio = 44, 58, 929, 446, C, 22, 29, 907, 410, C
AccessPoint = 66, 87, 952, 468, C, 88, 116, 974, 504, C
Form_Mapas = -165, 67, 721, 448, Z, 22, 29, 908, 417, C
Form_Instrucciones = 0, 0, 870, 372, C, 88, 116, 958, 481, C
Form_MikroTik = -160, 85, 804, 399, , 38, 44, 908, 480, C
CMD5 = 88, 116, 958, 481, C
Form_Estadisticas = 66, 87, 1090, 401, , 0, 0, 946, 388, C
Module1 = 66, 87, 1012, 475, 


