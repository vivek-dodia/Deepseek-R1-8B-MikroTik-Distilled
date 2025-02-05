# Repository Information
Name: mikrotik-php

# Directory Structure
Directory structure:
└── github_repos/mikrotik-php/
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
    │   │       ├── pack-b3cdec322c4cafe76921aa4475f813368adc169f.idx
    │   │       └── pack-b3cdec322c4cafe76921aa4475f813368adc169f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── cookiecutter.php
    ├── fast_config.php
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
	url = https://github.com/jamenlang/mikrotik-php.git
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
0000000000000000000000000000000000000000 308014e706ed1aa2c498d380ddc7714678e9e0f3 vivek-dodia <vivek.dodia@icloud.com> 1738606339 -0500	clone: from https://github.com/jamenlang/mikrotik-php.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 308014e706ed1aa2c498d380ddc7714678e9e0f3 vivek-dodia <vivek.dodia@icloud.com> 1738606339 -0500	clone: from https://github.com/jamenlang/mikrotik-php.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 308014e706ed1aa2c498d380ddc7714678e9e0f3 vivek-dodia <vivek.dodia@icloud.com> 1738606339 -0500	clone: from https://github.com/jamenlang/mikrotik-php.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
308014e706ed1aa2c498d380ddc7714678e9e0f3 refs/remotes/origin/master


File: /.git\refs\heads\master
308014e706ed1aa2c498d380ddc7714678e9e0f3


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Custom for Visual Studio
*.cs     diff=csharp
*.sln    merge=union
*.csproj merge=union
*.vbproj merge=union
*.fsproj merge=union
*.dbproj merge=union

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain


File: /.gitignore
# Windows image file caches
Thumbs.db
ehthumbs.db

# Folder config file
Desktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msm
*.msp

# =========================
# Operating System Files
# =========================

# OSX
# =========================

File: /cookiecutter.php
<?php
include('Net/SFTP.php');

$logging = 'file'; //add in mysql if you'd like, default 'file';

$log_file_handle = 'mtlog.txt';
$admin_password = 'tacobravo'; //admin password for config file.
$time_zone = 'America/Denver';
$ntp_server = '64.202.112.75';

$architecture_types = array (
	'RB2011' => 'mipsbe',
	'RB750' => 'mipsbe',
	'RB1200' => 'ppc'
);

$firmware_directory = 'c:/mikrotik/firmware/';
//place custom backup files in this directory with the model name in the file name. e.g. RB750GL-NONAT-CONFIG.backup
//place routeros-npk files in this directory too. e.g. routeros-mipsbe-6.18.npk

$ethernet_forenaming_scheme = 'ether'; //make sure this matches your backup files. e.g. ether1 
$sfp_forenaming_scheme = 'sfp'; //make sure this matches your backup files. e.g. sfp1

$failure_location = 'index.html';
$finished_location = 'index.html';

if(!file_exists($firmware_directory))
	die($firmware_directory . ' does not exist.');
else{
	$filelist = scandir($firmware_directory);
	$config_file_found = 0;
	$firmware_file_found = 0;
	foreach($filelist as $filename)
	{
		if(stristr($filename, '.backup'))
			$config_file_found = 1;
		if(stristr($filename, 'routeros-') && stristr($filename, '.npk'))
			$firmware_file_found = 1;
	}
	if ($config_file_found != 1)
		die($firmware_directory . ' has no .backup files in it.');
	if ($firmware_file_found != 1)
		die($firmware_directory . ' has no .npk files in it.');
}

$todo = ini_get('max_execution_time');
if ($todo != 0){
	file_put_contents($log_file_handle, 'Warning: Max execution time not 0; timeout: ' . $todo );
}

while(1) {
	//wait for mt to respond on port 80.
	do {
		is_connected(0);
	} while (is_connected(0) != '1');
	
	//make double sure it's up before continuing.
	do {
		is_connected(0);
	} while (is_connected(0) != '1');
	
	//wait for ssh access.
	sleep(10);
	
	//set time.
	try{
		set_time();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//update firmware.
	try{
		$configfile = update_firmware();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//wait for the mt to reboot if it needs to.
	sleep(10);
	
	//wait for mt to respond on port 80.
	do {		
		is_connected(0);
	} while (is_connected(0) != '1');
	
	//wait for ssh access.
	sleep(10);
	
	//apply config file.
	try{
		$firstrun = load_blank_config($configfile);
		if($firstrun == 'blanked')
			sleep(90);
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}

	//wait for the mikrotik to reboot if it needs to.
	do {
		is_connected(0);
	}
	while (is_connected(0) != '1');
	
	//wait for ssh access.
	sleep(10);
	
	//fix mac addresses.
	try{
		fix_mac_addresses();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//make sure it's still reachable on port 80.
	do {
		is_connected(0);
	}
	while (is_connected(0) != '1');
	
	//wait for ssh access.
	sleep(10);
	
	//set time.
	try{
		set_time();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//update bootloader if it's not up to date.
	try{
		$bootloader_state = update_bootloader();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//if the bootloader was updated the mt has to reboot again. we'll check to see if it was updated and wait if necessary.
	if($bootloader_state == 'justnowupdated'){
		do {
			is_connected(0);
		}
		while (is_connected(0) != '1');
		sleep(10);
	}
	
	//sing if successful.
	try{
		task_complete();
	} catch (Exception $e) {
		header("Location: $GLOBALS[failure_location]");
		echo 'Caught exception: ',  $e->getMessage(), "\n";
	}
	
	//wait while user changes out mikrotiks so this can run again.
	sleep(22);
}

function logthis($entry){
	if($GLOBALS[logging] != 'file'){
		//add in mysql support
	}
	else{
		file_put_contents(date("M/j H:i:s.u") . ', ' . $GLOBALS['log_file_handle'], $entry . PHP_EOL, FILE_APPEND | LOCK_EX);	
	}
}

function is_connected($noloop)
{

    $connected = @fsockopen("192.168.88.1", "80"); //website and port
    if ($connected){
        $is_conn = true; //action when connected
        fclose($connected);
    }else{
        $is_conn = false; //action in connection failure
		if ($noloop != '1')
			$is_conn = second_connected();
    }
    return $is_conn;
}

function second_connected()
{
	for ($i = 5; $i > 0; $i--)
	{
		if (is_connected(1) != '1'){			
			if ($i == 1){
				logthis('no more mikrotiks. killing myself. ');
				sleep(4);
			}
			else{
				logthis('dying in : ' . ($i - 1) . ' cycles' );
			}
		}
		else{
			
			return 1;
		}
	}
	
	header('Location: ' . $GLOBALS['finished_location'] . '');
	exit;
}

function set_time(){
	
	$ssh = new Net_SSH2('192.168.88.1');
	if (!$ssh->login('admin', '')) {
		if ($ssh->login('admin', $GLOBALS['admin_password'])) {
			$ssh->exec('system clock set time-zone-name=' . $GLOBALS['time_zone']);
			$ssh->exec('system clock set date=' . date("M/j/Y"));
			$ssh->exec('system clock set time=' . date("G:i:s"));
			$ssh->exec('system ntp client set primary-ntp=' . $GLOBALS['ntp_server']);
			$ssh->exec('system ntp client set enabled yes');
			logthis('set time');
		}
		else{
			logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
		}
	}
	
}

function update_firmware(){	

	$ssh = new Net_SSH2('192.168.88.1');
	$current_firwmare_version = '';
	if ($ssh->login('admin', '')) {
		
		$routerboard = $ssh->exec('system resource print');
	
		preg_match_all('/([^:]*?):([^\r\n]*)\r\n?/', $routerboard, $matches);
		$output = array_combine(preg_replace('/\s/','',$matches[1]), $matches[2]);
		$current_firmware_version = preg_replace("/[^0-9.]/", "", $output['version']);
		logthis('current firmware version: ' . $current_firmware_version );
		$routerboard = $ssh->exec('system routerboard print');

		preg_match_all('/([^:]*?):([^\r\n]*)\r\n?/', $routerboard, $matches);
		$output = array_combine(preg_replace('/\s/','',$matches[1]), $matches[2]);
		$model = 'RB' . preg_replace("/[^0-9]/", "", $output['model']);
		$ssh->disconnect();

		$files = scandir($GLOBALS['firmware_directory']);
		
		$sftp = new Net_SFTP('192.168.88.1');
		if (!$sftp->login('admin', '')) {
			exit('Login Failed');
		}
		$routeros_file_found = 0;
		foreach ($files as $file){
			if (strstr($file, 'routeros-' . $GLOBALS['architecture_types'][$model] . '-'))
			{
				$routeros_file_found = 1;
				$newfw = preg_replace("/.npk/", "", $file);
				$newfw = preg_replace("/[^0-9.]/", "", $newfw);
				if ($current_firmware_version != $newfw){
					if($current_firmware_version > $newfw){
						logthis('current firmware is newer than ' . $newfw );
					}
					else{
						logthis('new firmware version: ' . $newfw );
					}
				}
				else{
					logthis('firmware already up to date' );
				}
			}
		}
		if($routeros_file_found == 0)
			die('no routeros for ' . $GLOBALS['architecture_types'][$model] . ' found.');
		$sftp->pwd();
		foreach ($files as $file){
			if ($file != '.' && $file != '..'){
				if (strstr($file, $GLOBALS['architecture_types'][$model]) || strstr($file, $model)){
					if (!strstr($file, $current_firmware_version . '-') && !strstr($file, $current_firmware_version . '.npk')){ //append a '-' here also check for npk...
						logthis('sftping file (not using a password): ' . $file);
						$sftp->put("$file", file_get_contents($GLOBALS['firmware_directory'] . $file));
						$ssh->exec(':beep frequency=137 length=2ms;');
					}
				}
				if (strstr($file, $model)){
					$configfile = $file;
				}
			}
		}
		if(!$configfile)
			die('no backup for ' . $model . ' found.');
		$ssh = new Net_SSH2('192.168.88.1');
		if ($ssh->login('admin', '')) {
			$todo = $ssh->exec('system reboot');
			logthis($todo );
			$ssh->disconnect();
			logthis('updated firmware (not using a password)');
		}
		
		return $configfile; 
	}
	
	if ($ssh->login('admin', $GLOBALS['admin_password'])) {
		$routerboard = $ssh->exec('system resource print');
	
		preg_match_all('/([^:]*?):([^\r\n]*)\r\n?/', $routerboard, $matches);
		$output = array_combine(preg_replace('/\s/','',$matches[1]), $matches[2]);
		$current_firmware_version = preg_replace("/[^0-9.]/", "", $output['version']);
		logthis('current firmware version: ' . $current_firmware_version );
		$routerboard = $ssh->exec('system routerboard print');

		preg_match_all('/([^:]*?):([^\r\n]*)\r\n?/', $routerboard, $matches);
		$output = array_combine(preg_replace('/\s/','',$matches[1]), $matches[2]);
		$model = 'RB' . preg_replace("/[^0-9]/", "", $output['model']);
		$ssh->disconnect();

		$files = scandir($GLOBALS['firmware_directory']);
	
		$sftp = new Net_SFTP('192.168.88.1');
		if (!$sftp->login('admin', $GLOBALS['admin_password'])) {
			exit('Login Failed');
		}
		
 		foreach ($files as $file){

			if (strstr($file, 'routeros-' . $GLOBALS['architecture_types'][$model] . '-'))
			{
				$routeros_file_found = 1;
				$newfw = preg_replace("/.npk/", "", $file);
				$newfw = preg_replace("/[^0-9.]/", "", $newfw);
				
				if ($current_firmware_version != $newfw){
					if($current_firmware_version > $newfw){
						logthis('current firmware is newer than ' . $newfw );
					}
					else{
						logthis('new firmware version: ' . $newfw );
					}
				}
				else{
					logthis('firmware already up to date' );
				}
			}
		}
		if($routeros_file_found == 0)
			die('no routeros for ' . $GLOBALS['architecture_types'][$model] . ' found.');
		$sftp->pwd();
		foreach ($files as $file){
			if ($file != '.' && $file != '..'){
				if (strstr($file, $GLOBALS['architecture_types'][$model]) || strstr($file, $model)){
					if (!strstr($file, $current_firmware_version . '-') && !strstr($file, $current_firmware_version . '.npk')){
						logthis('sftping file (using password): ' . $file );
						$sftp->put("$file", file_get_contents($GLOBALS['firmware_directory'] . $file));
						$ssh->exec(':beep frequency=137 length=2ms;');
					}
				}
				if (strstr($file, $model)){
					$configfile = $file;
				}
			}
		}
		
		if(!$configfile)
			die('no backup for ' . $model . ' found.');
			
		$ssh = new Net_SSH2('192.168.88.1');
		if ($ssh->login('admin', $GLOBALS['admin_password'])) {
			$todo = $ssh->exec('system reboot');
			logthis($todo );
			$ssh->disconnect();
			logthis('updated firmware (using password)');
		}
		else{
			logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
		}
		
		return $configfile; 
	}
	else{
		logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
	}
}

function load_blank_config($configfile) {
	$ssh = new Net_SSH2('192.168.88.1');
	for ($login = 0; $login <= 3; $login++)
	{
		if ($ssh->login('admin', '')) {
			$todo = $ssh->exec('system backup load name=' . $configfile . ' password="'. $GLOBALS['admin_password'] . '"'); //load the config file.
			logthis($todo );
			$todo = $ssh->exec('system reboot');
			logthis($todo );
			logthis('blanking : (' . $configfile . ')');
		
			return 'blanked';
		}
		logthis('skipped blanking: (attempt ' . $login . ') cannot log in without password; assuming blanked already.' );
	}
}

function fix_mac_addresses(){
	
	$ssh = new Net_SSH2('192.168.88.1');
	if (!$ssh->login('admin', '')) {
		if ($ssh->login('admin', $GLOBALS['admin_password'])) {
			$detail = $ssh->exec('int eth print');
			logthis($detail );
			if (preg_match_all("/$GLOBALS[ethernet_forenaming_scheme]/", $detail, $matches)) {
				$i=1;
				foreach($matches[0] as $match){					
					$todo = $ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['ethernet_forenaming_scheme'] . $i);
					logthis($todo .PHP_EOL, FILE_APPEND | LOCK_EX);
					$ssh->exec(':beep frequency=120 length=2ms;');
					if($i == '10'){
						$todo = $ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['sfp_forenaming_scheme'] . '1');
						logthis($todo .PHP_EOL, FILE_APPEND | LOCK_EX);
					}
					$i++;
				}
				$todo = $ssh->exec('int eth print');
				logthis($todo .PHP_EOL, FILE_APPEND | LOCK_EX);
				logthis('fixed mac addresses');
			}
		}
		else{
			logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
		}
	}
	
}

function update_bootloader(){
	
	$ssh = new Net_SSH2('192.168.88.1');
	if (!$ssh->login('admin', '')) {
		if ($ssh->login('admin', $GLOBALS['admin_password'])) {
			$todo = $ssh->exec('system routerboard print');
			echo $todo;
			$string = str_replace(PHP_EOL, ': ', $todo);
			$list = explode(': ', $string);
			$result = array();
			for ($i=0 ; $i<count($list) ; $i+=2) {
				$result[ trim($list[$i]) ] = trim($list[$i+1]);
			}
			$upgrade_firmware = $result['upgrade-firmware'];
			$current_firmware = $result['current-firmware'];
			if ($current_firmware != $upgrade_firmware){
				$todo = $ssh->exec('/system routerboard upgrade');
				$todo = 'upgrading bootloader ' . $current_firmware . ' -> ' . $upgrade_firmware; 
				$todo = $ssh->exec('/system reboot');
				logthis($todo );
				return 'justnowupdated';
			}
			else{
				$todo = 'bootloader firmware is up to date';
				logthis($todo );
				return 'alreadyuptodate';
			}
		}
		else{
			logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
		}
	}
}

function task_complete(){
	$ssh = new Net_SSH2('192.168.88.1');
	if (!$ssh->login('admin', '')) {
		if ($ssh->login('admin', $GLOBALS['admin_password'])) {
			logthis('initial configuration completed');
			$ssh->exec(':beep frequency=784 length=200ms;');
			$ssh->exec(':delay 200ms;');
			$ssh->exec(':beep frequency=740 length=200ms;');
			$ssh->exec(':delay 200ms;');
			$ssh->exec(':beep frequency=659 length=200ms;');
			$ssh->exec(':delay 200ms;');
			$ssh->exec(':beep frequency=659 length=200ms;');
			$ssh->exec(':delay 200ms;');
			$ssh->exec(':beep frequency=740 length=200ms;');
			$ssh->exec(':delay 1000ms;');
		}
		else{
			logthis('password ' . $GLOBALS['admin_password'] . ' is incorrect. ' );
		}
	}
}

?>

File: /fast_config.php
<?php
include('Net/SFTP.php');

$admin_password = 'tacobravo'; //admin password for router.

$ethernet_forenaming_scheme = 'ether'; //make sure this matches your router config. e.g. ether1 
$sfp_forenaming_scheme = 'sfp'; //make sure this matches your router config. e.g. sfp1
$vlan_forenaming_scheme = 'vlan'; //make sure this is set to what you want vlans to start with, e.g. vlan3309 


if(!isset($_POST) || $_POST != ''){
?>
<html>
<body style="background-color: e0e7f7";>
<form action="fast_config.php" method="POST"/>
<table border="0">
<tr><td style="border-left: dashed 1px; border-top: dashed 1px;">VLAN:</td><td style="border-right: dashed 1px; border-top: dashed 1px;"><input type="text" name="vlan"/></td></tr>
<tr><td style="border-left: dashed 1px; border-bottom: dashed 1px;">Interface: </td><td style="border-right: dashed 1px; border-bottom: dashed 1px;"><input type="text" name="interface"/></td></tr>
<tr><td>Subnet:</td><td><input type="text" name="subnet"/></td><td><input value="Apply" type="submit"/></td>
</table>
<?php
}

if(isset($_POST['subnet']) && $_POST['subnet'] != ''){
	do {
		is_connected();
	}
	while (is_connected() != '1');

	if($_POST['vlan'] != '')
		make_vlan($_POST['vlan'],$_POST['interface'] );
	set_addr($_POST['subnet'], $_POST['vlan']);
}

function is_connected()
{
	$connected = @fsockopen("192.168.88.1", "80"); //website and port
	if ($connected){
		$is_conn = true; //action when connected
		fclose($connected);
	}else{
		$is_conn = false; //action in connection failure
	}
	return $is_conn;
}

function make_vlan($vlan, $interface) {
	$interface = (($interface != '') ? $interface : 'ether1');
	$ssh = new Net_SSH2('192.168.88.1');
	if ($ssh->login('admin', $GLOBALS['admin_password'])) {
		$ssh->exec('interface ethernet print');
		$ssh->exec('interface vlan add name=' . $GLOBALS['vlan_forenaming_scheme'] . $vlan . ' vlan-id=' . $vlan . ' interface=' . $interface);//make a new vlan with the vlan# as the vlan name	
		$verify = $ssh->exec('interface vlan print');
	}
}

function set_addr($subnet, $interface) {
	$interface = (($interface != '') ? $interface : $GLOBALS['ethernet_forenaming_scheme'] . '1');
	$ip = explode('/',$subnet);
	$cidr = $ip[1];
	$ip_parts = explode('.',$ip[0]);
	$ip_parts[3] = $ip_parts[3] + 1;
	$gw = implode('.', $ip_parts);
	$ip_parts[3] = $ip_parts[3] + 1;
	$ip = implode('.', $ip_parts);

	$ssh = new Net_SSH2('192.168.88.1');
	if ($ssh->login('admin', $GLOBALS['admin_password'])) {
		//while we're here we might as well reset the mac addresses again.
		$detail = $ssh->exec('int eth print');
		if (preg_match_all("/$GLOBALS[ethernet_forenaming_scheme]/", $detail, $matches)) {
			$i=1;
			foreach($matches[0] as $match){
				$ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['ethernet_forenaming_scheme'] . $i);
				$ssh->exec(':beep frequency=120 length=2ms;');
				$i++;
				if($i == '10')
					$ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['sfp_forenaming_scheme'] . '1');
			}
		}
		
		$ssh->exec('ip address add address=' . $ip . '/' . $cidr . ' interface=' . $interface);//set the ip on the specified interface.
		$ssh->exec('ip route add dst-address=0.0.0.0/0 gateway=' . $gw); //add the default route
	}	
}

$ssh = new Net_SSH2('192.168.88.1');
if ($ssh->login('admin', $GLOBALS['admin_password'])) {
	//while we're here we might as well reset the mac addresses again.
	$detail = $ssh->exec('int eth print');
	if (preg_match_all("/$GLOBALS[ethernet_forenaming_scheme]/", $detail, $matches)) {
		$i=1;
		foreach($matches[0] as $match){
			$ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['ethernet_forenaming_scheme'] . $i);
			$ssh->exec(':beep frequency=120 length=2ms;');
			$i++;
			if($i == '10')
				$ssh->exec('int ethernet reset-mac-address ' . $GLOBALS['sfp_forenaming_scheme'] . '1');
		}
	}

	$verify = $ssh->exec('interface vlan print');
	$others = preg_match_all('/\d\s+[a-zA-Z]?\d+\s+1500\senabled\s+(\d+)\s([a-zA-Z0-9]+)/', $verify, $out);
	foreach ($out[1] as $double => $single){
		if (isset($vlan) && !strstr($vlan, $single) || !isset($vlan)){
			echo 'VLAN ' . $single . ' is on ' . $out[2][$double] . '<br />';
		}
	}

	$more = $ssh->exec('ip address print');
	$others = preg_match_all('/\d?\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\/\d+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+([a-zA-Z0-9]+)/', $more, $out);

	foreach ($out[1] as $double => $single){
		echo $single . ' is on ' . $out[2][$double] . '<br />';
	}
	if (isset($interface)){
		$verify = $ssh->exec('ip address print where interface=' . $interface);
		if(strstr($verify, $ip . '/' . $cidr))
		{
			echo $ip . ' is on ' . $interface . '<br />';
			$ssh->exec('beep');
		}
	}
		
	$verify = $ssh->exec('ip route print where dst-address=0.0.0.0/0');
	$others = preg_match_all('/0.0.0.0\/0\s+?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/', $verify, $out);
	foreach ($out[1] as $single){
		echo 'default gateway set as ' . $single . '<br />';
	}
	if (isset($gw)){
		if(strstr($verify, $gw))
		{
			echo 'for verification: last configured default route set as ' . $gw . '<br />';
			$ssh->exec('beep');
		}
	}
	echo '<br />';
	echo 'ip address print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('ip address print'));
	echo 'ip route print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('ip route print'));
	echo 'int eth print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('int eth print'));
	echo 'int vlan print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('int vlan print'));
	$ssh->exec('ip neighbor discovery set [find] discover=yes');
	$ssh->exec('tool mac-server set [find] disabled=no');
	echo 'tool mac-server print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('tool mac-server print'));
	echo 'system routerboard print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('system routerboard print'));
	echo 'system resource print:' . '<br />';
	echo preg_replace('/\r\n/', '<br />', $ssh->exec('system resource print'));
	$ssh->exec('beep');
	$ssh->exec('beep');
	$ssh->exec('beep');
	$ssh->exec('beep');
	$ssh->exec('beep');
}
else{
	die('password ' . $GLOBALS['admin_password'] . ' is incorrect.');
}
?>


File: /README.md
#mikrotik-php
a suite of php scripts 

If you experience problems with the following scripts:
be sure to fix them and let me know :)

##cookiecutter
make up to date copies of routers from backup files

##fast_config
quickly apply a /30 ip to an interface and generates a complete output for copy and pasting.

=============


## cookiecutter


routine to mass configure routers by updating router OS and applying config files using php.

###requirements

>cookiecutter requires phpseclib to function. 

>phpseclib is available from http://phpseclib.sourceforge.net/


###setup

change the entries in the config file accordingly.

at this point in time file is supported, monitor log with windows preview pane or notepadd++ with silent update enabled.

>$logging = 'file'; //add in mysql if you'd like, default 'file';

>$log_file_handle = 'mtlog.txt';

mikrotik now requires backup files with passwords to be applied using a password, modify this to reflect the backup file admin password. 

>$admin_password = 'tacobravo'; //admin password for config file.

because it's the best

>$time_zone = 'America/Denver';

no reason, others are available http://support.ntp.org/bin/view/Servers/StratumOneTimeServers

>$ntp_server = '64.202.112.75';

if you see a missing architecture type add it in

>$architecture_types = array (
>	'RB2011' => 'mipsbe',
>	'RBxxXx' => 'xxxXx',
>	'RB750' => 'mipsbe',
>	'RB1200' => 'ppc'
>);

place router OS in the following directory, it's not necessary to move the 18 smaller files, just routeros-xxxXx-6.18.npk for the architecture types listed above.

also place custom backup files in this directory with the model name in the file name. e.g. RB750GL-NONAT-CONFIG.backup

>$firmware_directory = 'c:/mikrotik/firmware/';

change these to match the default files. mikrotik default forenames are whack, ether1-gateway? ether10-slave-local?! just be sure to name them in your backup like you want them named and change the following accordingly.

make sure this matches your backup files. e.g. ether1,ether2,ether3 would be 'ether' GigabitEthern-1,GigabitEthern-2 would be 'GigabitEthern-'

>$ethernet_forenaming_scheme = 'ether'; 

>$sfp_forenaming_scheme = 'sfp'; //make sure this matches your backup files. e.g. sfp1

======================

## fast_config

routine to apply /30 subnet to interfaces or add them to new vlans using php.

###requirements

fast_config requires phpseclib to function. 

phpseclib is available from http://phpseclib.sourceforge.net/


###setup

change the entries in the config file accordingly.

>$admin_password = 'tacobravo'; //admin password for router.

>$ethernet_forenaming_scheme = 'ether'; //make sure this matches your router config. e.g. ether1 

>$sfp_forenaming_scheme = 'sfp'; //make sure this matches your router config. e.g. sfp1

>$vlan_forenaming_scheme = 'vlan'; //make sure this is set to what you want vlans to start with, e.g. vlan3309


