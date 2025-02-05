# Repository Information
Name: Mikrotik_Clientrouters_config_builder

# Directory Structure
Directory structure:
└── github_repos/Mikrotik_Clientrouters_config_builder/
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
    │   │       ├── pack-9a1ecb603d666dd5cdc0b372744e6724297a7bc2.idx
    │   │       └── pack-9a1ecb603d666dd5cdc0b372744e6724297a7bc2.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    └── Mikrotik_Config_Builder.bat


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
	url = https://github.com/romawkafor/Mikrotik_Clientrouters_config_builder.git
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
0000000000000000000000000000000000000000 ae96fd9d44ae7f492180a0b8760ab02aa3b9c4a5 vivek-dodia <vivek.dodia@icloud.com> 1738606385 -0500	clone: from https://github.com/romawkafor/Mikrotik_Clientrouters_config_builder.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 ae96fd9d44ae7f492180a0b8760ab02aa3b9c4a5 vivek-dodia <vivek.dodia@icloud.com> 1738606385 -0500	clone: from https://github.com/romawkafor/Mikrotik_Clientrouters_config_builder.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ae96fd9d44ae7f492180a0b8760ab02aa3b9c4a5 vivek-dodia <vivek.dodia@icloud.com> 1738606385 -0500	clone: from https://github.com/romawkafor/Mikrotik_Clientrouters_config_builder.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ae96fd9d44ae7f492180a0b8760ab02aa3b9c4a5 refs/remotes/origin/main


File: /.git\refs\heads\main
ae96fd9d44ae7f492180a0b8760ab02aa3b9c4a5


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /Mikrotik_Config_Builder.bat
@echo off
chcp 65001
color 4F 
echo "IP Address","Port","Remote Channel","CAM NAME","Manufacturer","Username","Password">>%UserProfile%\Desktop\GV.csv
echo "IP Address","Port","Remote Channel","CAM NAME","Manufacturer","Username","Password">>%UserProfile%\Desktop\UP.csv
echo "IP Address","Port","Remote Channel","CAM NAME","Manufacturer","Username","Password">>%UserProfile%\Desktop\SC1.csv
echo "IP Address","Port","Remote Channel","CAM NAME","Manufacturer","Username","Password">>%UserProfile%\Desktop\SC2.csv
set DahuaDescript="Примечание: IP ссылается на IP-адрес,доменное имя, или RTSP-адрес. Значение порта  должно быть в пределах от 1 до 65535. Номер канала должен быть больше 1. Парматер IPC - введите 1. Производитель включает в себя:Dahua,Panasonic,Sony,Dynacolor,Samsung,AXIS,Sanyo,Pelco,Arecont,Onvif,Xunmei,LG,Watchnet,Canon,PSIA,RTSP,AirLive,JVC"
rem Задаю довжину паролю.
set PassLength=14
Rem Нижче генератор паролю
:START
cls
setlocal
set "set[1]=ABCDEFGHIJKLMNOPQRSTUVWXYZ"  &  set "len[1]=26"  &  set "num[1]=0"
set "set[2]=abcdefghijklmnopqrstuvwxyz"  &  set "len[2]=26"  &  set "num[2]=0"
set "set[3]=0123456789"                  &  set "len[3]=10"  &  set "num[3]=0"
setlocal EnableDelayedExpansion

rem Create a list of 10 random numbers between 1 and 4;
rem the condition is that it must be at least one digit of each one

rem Initialize the list with 10 numbers
set "list="
for /L %%i in (1,1,%PassLength%) do (
   set /A rnd=!random! %% 3 + 1
   set "list=!list!!rnd! "
   set /A num[!rnd!]+=1
)

:checkList
rem Check that all digits appear in the list at least one time
set /A mul=num[1]*num[2]*num[3]
if %mul% neq 0 goto listOK

   rem Change elements in the list until fulfill the condition

   rem Remove first element from list
   set /A num[%list:~0,1%]-=1
   set "list=%list:~2%"

   rem Insert new element at end of list
   set /A rnd=%random% %% 4 + 1
   set "list=%list%%rnd% "
   set /A num[%rnd%]+=1

goto checkList
:listOK

rem Generate the password with the sets indicated by the numbers in the list
set "RndAlphaNum="
for %%a in (%list%) do (
   set /A rnd=!random! %% len[%%a]
   for %%r in (!rnd!) do set "RndAlphaNum=!RndAlphaNum!!set[%%a]:~%%r,1!"
)
rem кінець генератора паролю


rem Задаю початкові змінні
set L2TPServer=vpn.company.com
set PassToRouter=1q2w3e4r5t
rem Запитую про змінні
set /p TempNameShop=Введіть ім'я магазину латиницею. Приклад: Kyiv_md_Nezalezhnosti_1 :
set /p ShotNameShop=Введіть коротке ім'я магазину латиницею. Приклад: Kyiv_md_Nezal_1:
set /p CurrilicName=Введіть ім'я магазину Кирилицею. Приклад: Київ Незалежності 1 :
set /p SubnetSufix=Введіть номер підмережі. 10.0.XXX.0 :
set L2TPLogin=%TempNameShop%
set L2TPPass=%RndAlphaNum%

rem Створюю Адресу тунелю (Адреса мережі + 1)
set /A AltSubnetSufix=%SubnetSufix%
set /A AltSubnetSufix=%AltSubnetSufix%+1
rem Генерую скрипт
echo user set admin password=%PassToRouter%>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system identity set name="%TempNameShop%">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system ntp client set enabled=yes primary-ntp=62.149.0.30 secondary-ntp=129.6.15.28>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system routerboard settings set auto-upgrade=yes>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system routerboard settings set force-backup-booter=yes>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge add name=WORK_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge add name=INTERNET_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dhcp-client add interface=ether1 add-default-route=yes use-peer-dns=yes use-peer-ntp=no disabled=no comment="Defoult from Roman Pereviznyk">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip address add address=10.0.%SubnetSufix%.1/24 interface=WORK_LAN network=10.0.%SubnetSufix%.0>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip address add address=192.168.10.1/24 interface=INTERNET_LAN network=192.168.10.0>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dns set allow-remote-requests=yes servers=8.8.8.8,194.44.214.214,208.67.222.222,8.8.4.4,194.44.214.40,208.67.220.220>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dhcp-server network add address=10.0.%SubnetSufix%.0/24 gateway=10.0.%SubnetSufix%.1 dns-server=10.0.%SubnetSufix%.1,8.8.8.8>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=192.168.10.1,8.8.8.8>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip pool add name=WORK_LAN_POOL ranges=10.0.%SubnetSufix%.100-10.0.%SubnetSufix%.200>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip pool add name=INTERNET_LAN_POOL ranges=192.168.10.100-192.168.10.200>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dhcp-server add name=DHCP_WORK interface=WORK_LAN lease-time=08:00:00 address-pool=WORK_LAN_POOL authoritative=yes bootp-support=static disabled=no>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip dhcp-server add name=DHCP_INTERNET interface=INTERNET_LAN lease-time=08:00:00 address-pool=INTERNET_LAN_POOL authoritative=yes bootp-support=static disabled=no>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface l2tp-client add name="l2tp_to_Office" connect-to=%L2TPServer% user="%L2TPLogin%@vpn.company.com" password="%L2TPPass%" allow=mschap2 disabled=no>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip route add dst-address=10.0.0.0/24 gateway=l2tp_to_Office type=unicast distance=1 scope=30 target-scope=10 comment="Route to General Office">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip route rule add src-address=192.168.10.0/24 dst-address=10.0.0.0/24 action=unreachable comment="Disable INTERNET_LAN to General Office">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip route rule add src-address=10.0.%SubnetSufix%.0/24 dst-address=192.168.10.0/24 action=unreachable comment="Disable WORK_LAN to INTERNET_LAN">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip route rule add src-address=192.168.10.0/24 dst-address=10.0.%SubnetSufix%.0/24 action=unreachable comment="Disable INTERNET_LAN to WORK_LAN">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall nat add out-interface=ether1 chain=srcnat action=masquerade comment="Defoult from Roman Pereviznyk">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall nat add out-interface=l2tp_to_Office chain=srcnat action=masquerade disabled=yes comment=NAT_to_Office>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=input action=accept protocol=icmp log=no comment="accept ICMP">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=input action=accept connection-state=established,related log=no comment="accept established,related">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=input action=drop in-interface=ether1 log=no comment="drop all from WAN">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=forward action=fasttrack-connection connection-state=established,related log=no comment=fasttrack>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=forward action=accept connection-state=established,related log=no comment="accept established,related">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=forward action=drop connection-state=invalid log=no comment="drop invalid">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip firewall filter add chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface=ether1 log=no comment="drop all from WAN not DSTNATed">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system package update set channel=long-term>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface eoip add disabled=yes name="EOIP_to_Office" tunnel-id=%SubnetSufix% local-address=172.16.0.%AltSubnetSufix% remote-address=172.16.0.1>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface list add exclude=dynamic name=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface list member add interface=WORK_LAN list=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface list member add interface=EOIP_to_Office list=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip neighbor discovery-settings set discover-interface-list=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /tool mac-server set allowed-interface-list=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /tool mac-server mac-winbox set allowed-interface-list=discover>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface wireless security-profiles add name=SECURITY_INTERNET_AP authentication-types=wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=freeinternet mode=dynamic-keys>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface wireless security-profiles add name=SECURITY_WORK_AP authentication-types=wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa2-pre-shared-key=Reelystrongpassword mode=dynamic-keys>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface wireless set wlan1 disabled=no mode=ap-bridge band=2ghz-b/g/n channel-width=20/40mhz-Ce frequency=2422 ssid=WORK_NETWORK security-profile=SECURITY_WORK_AP wireless-protocol=unspecified wmm-support=enabled country=ukraine default-authentication=yes default-forwarding=yes>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface wireless add master-interface=wlan1 mode=ap-bridge ssid=INTERNET disabled=no security-profile=SECURITY_INTERNET_AP;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo :delay 10;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=wlan1 bridge=WORK_LAN;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo :delay 5;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=wlan2 bridge=INTERNET_LAN;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo :delay 2;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip service disable numbers=0,1,5,7;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip service set ssh address=10.0.%SubnetSufix%.0/24,172.16.0.0/24;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip service set winbox address=10.0.%SubnetSufix%.0/24,172.16.0.0/24;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ip service set www address=10.0.%SubnetSufix%.0/24,172.16.0.0/24;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /tool bandwidth-server set enabled=no;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system script add name=reboot source="/system reboot";>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /system script add name=backup2ftp source=":local name value=[/system identity get name]; /system backup save name=\$name; /export file=\$name; /tool fetch address=10.0.0.9 user=MicrotikBackupUser password=mWvfJyxGFzia5Nzu mode=ftp dst-path=(\"/rsc/\".\$name.\".rsc\") src-path=(\$name.\".rsc\") upload=yes; /tool fetch address=10.0.0.9 user=MicrotikBackupUser password=mWvfJyxGFzia5Nzu mode=ftp dst-path=(\"/backup/\".\$name.\".backup\") src-path=(\$name.\".backup\") upload=yes; /file remove (\$name.\".backup\"); /file remove (\$name.\".rsc\");">>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo :delay 5;>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=ether2 bridge=WORK_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=ether3 bridge=WORK_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=ether4 bridge=WORK_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface bridge port add interface=ether5 bridge=WORK_LAN>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /interface ethernet poe set ether5 poe-out=off>>%UserProfile%\Desktop\MTSCRIPT-%TempNameShop%.txt
echo /ppp secret add name="%L2TPLogin%@vpn.company.com" password="%L2TPPass%" service=l2tp profile=L2TP local-address=172.16.0.1 remote-address=172.16.0.%AltSubnetSufix%>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /interface l2tp-server add name="Tunnel to %L2TPLogin%" user=%L2TPLogin%@vpn.company.com>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /interface eoip add name="EOIP tunnel to %TempNameShop%" tunnel-id=%SubnetSufix% local-address=172.16.0.1 remote-address=172.16.0.%AltSubnetSufix%>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /ip route add dst-address=10.0.%SubnetSufix%.0/24 gateway=172.16.0.%AltSubnetSufix% pref-src=172.16.0.1 comment="Route to %L2TPLogin%">>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /ip dns static add name=gv.%ShotNameShop%.cctv address=10.0.%SubnetSufix%.10>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /ip dns static add name=up.%ShotNameShop%.cctv address=10.0.%SubnetSufix%.20>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /ip dns static add name=sc1.%ShotNameShop%.cctv address=10.0.%SubnetSufix%.30>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
echo /ip dns static add name=sc2.%ShotNameShop%.cctv address=10.0.%SubnetSufix%.40>>%UserProfile%\Desktop\Core_MT_SCRIPT.txt
chcp 1251
echo "gv.%ShotNameShop%.cctv","37777","1","%CurrilicName%","Dahua","admin","1Q2W3E4R5T6Y">>%UserProfile%\Desktop\GV.csv
echo "up.%ShotNameShop%.cctv","37777","1","%CurrilicName%","Dahua","admin","1Q2W3E4R5T6Y">>%UserProfile%\Desktop\UP.csv
echo "sc1.%ShotNameShop%.cctv","37777","1","%CurrilicName%","Dahua","admin","1Q2W3E4R5T6Y">>%UserProfile%\Desktop\SC1.csv
echo "sc2.%ShotNameShop%.cctv","37777","1","%CurrilicName%","Dahua","admin","1Q2W3E4R5T6Y">>%UserProfile%\Desktop\SC2.csv
chcp 65001
cls
echo Конфігурація для клієнта та сервера успішно створена. Файли знаходяться на робочому столі.
echo Вам необхідно створити ще Користувачів на FTP та відповідні папки з ім'ям магазину:
echo Login FTP: %L2TPLogin% ; FTP Password: %L2TPPass%
echo.
echo.
echo Також не забудьте дописати скрипт на сервері який обробляє і складає фото на FTP.
CHOICE /N /C yn /M "Створити ще одну конфігурацію? Y - так, N - ні"
if %errorlevel%==1 GoTO START
if %errorlevel%==2 GoTo Exit
:Exit
chcp 1251
echo %DahuaDescript%>>%UserProfile%\Desktop\GV.csv
echo %DahuaDescript%>>%UserProfile%\Desktop\UP.csv
echo %DahuaDescript%>>%UserProfile%\Desktop\SC1.csv
echo %DahuaDescript%>>%UserProfile%\Desktop\SC2.csv
Exit



