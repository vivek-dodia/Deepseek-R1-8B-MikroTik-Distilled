# Repository Information
Name: simple-mikrotik-script

# Directory Structure
Directory structure:
└── github_repos/simple-mikrotik-script/
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
    │   │       ├── pack-6129cf3bd2731adc3913685e83af79b696ec174e.idx
    │   │       └── pack-6129cf3bd2731adc3913685e83af79b696ec174e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── cpu-monitoring
    ├── data-usage-to-telegram
    ├── dns-to-address-list
    ├── firewall-raw-video-stream.rsc
    ├── first-setup
    ├── get-random-string
    ├── LICENSE
    ├── list-port-game
    ├── quad9-doh.rsc
    ├── README.md
    ├── scheduler.rsc
    └── secure-your-router


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
	url = https://github.com/furaihan/simple-mikrotik-script.git
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
0000000000000000000000000000000000000000 eacf8dc40951bfcdac5c344272e315a88e199b0b vivek-dodia <vivek.dodia@icloud.com> 1738606028 -0500	clone: from https://github.com/furaihan/simple-mikrotik-script.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 eacf8dc40951bfcdac5c344272e315a88e199b0b vivek-dodia <vivek.dodia@icloud.com> 1738606028 -0500	clone: from https://github.com/furaihan/simple-mikrotik-script.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 eacf8dc40951bfcdac5c344272e315a88e199b0b vivek-dodia <vivek.dodia@icloud.com> 1738606028 -0500	clone: from https://github.com/furaihan/simple-mikrotik-script.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8745549c1563972fe935f18d6ec68022efcb386d refs/remotes/origin/experiment
eacf8dc40951bfcdac5c344272e315a88e199b0b refs/remotes/origin/master


File: /.git\refs\heads\master
eacf8dc40951bfcdac5c344272e315a88e199b0b


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /cpu-monitoring
﻿local cpuarray 
local rebootIfHigh false
set cpuarray ([/system resource get value-name=cpu-load])
#Change the value below to change the number of CPU load sample to average
local cpusample 20
for i from=1 to=[$cpusample -1] do={
	delay 950ms;
	set cpuarray ([/system resource get value-name=cpu-load],$cpuarray)
}
put $cpuarray
local totalcpuarray 0
#calculating the average
foreach value in=$cpuarray do={ set totalcpuarray ($totalcpuarray + $value)}
:put $totalcpuarray
local avgcpu ($totalcpuarray / [:len $cpuarray])
if ($avgcpu > 65) do={
	:global ConnectionAvailable
	$ConnectionAvailable
	if ($ConnectionAvailable=true) do={
		global CHATID
		global BOTID
		local maxcpu ($cpuarray->0)
		local mincpu ($cpuarray->0)
		foreach i in=$cpuarray do={
			if ($i > $maxcpu) do={ set maxcpu $i}
			if ($i < $mincpu) do={ set mincpu $i}
		}
		local sendToTelegram ("Mikrotik ".[/system resource get value-name=board-name]."(".[/sy id get value-name=name].") :%0A\E2\9A\A0 \E2\9A\A0 <b>CPU Load Report</b>%0AMax: $maxcpu%0AMin: $mincpu%0AAverage: $avgcpu%25%0ACPU Samples: $cpusample%0AReboot if CPU sample show highload: $rebootIfHigh")
		/tool fetch url="https://api.telegram.org/bot$BOTID/sendMessage\?chat_id=$CHATID&text=$sendToTelegram&parse_mode=html" keep-result=no;
	} else={
		log warning message="Cannot send message to telegram. is internet connected?"
	}
	if ($rebootIfHigh = true) do={/system reboot}
} else={
	nothing
}


File: /data-usage-to-telegram
:global ConnectionAvailable
$ConnectionAvailable
if ($ConnectionAvailable=true) do={
	global CHATID
	global BOTID
	local wan [/ip arp get number=[find where address=[/ip route get number=[find where dst-address="0.0.0.0/0" && active=yes ] gateway]] interface]
	local SendTelegram ("<b>Daily Data Usage Report:</b>%0A"."WAN Interface: $wan%0A"."Upload Usage:".([/interface get $wan tx-byte] / 1024 / 1024 / 1024)." GB%0ADownload Usage: ".([/interface get $wan rx-byte] / 1024 / 1024 / 1024)." GB%0ATotal: ".(([/interface get $wan tx-byte] / 1024 / 1024 / 1024) + ([/interface get $wan rx-byte] / 1024 / 1024 / 1024))." GB")
	/tool fetch url="https://api.telegram.org/bot$BOTID/sendMessage\?chat_id=$CHATID&text=$SendTelegram&parse_mode=html" keep-result=no;
} else={
	log warning message="Cannot send message to telegram. is internet connected?"
}


File: /dns-to-address-list
#PLEASE BE ADVISED THAT THIS SCRIPT MAY CAUSE HIGH CPU LOAD ON YOUR ROUTER
#=============================================== DNS Monitor Information ================================================
#
#                  COPYRIGHT MIKROTIK ROUTEROS SCRIPT PROVIDED BY FURAIHAN
#
#=============================================== DNS Monitor by furaihan ================================================
#
#                  THE SCRIPT FILE LOADED SUCCESFULLY.
#                  DETECTED VERSION:  1.0 BETA
#
#=============================================== DNS Monitor by furaihan ================================================

foreach 11g in=[/ip dns cache all find where (name~"zynga" or name~"kojima" or name~"konami" or name~"projektred" or name~"rockstar" or name~"ubisoft" or name~"gameloft" or name~"superevil" or name~"mojang" or name~"game" or name~"steampowered" or name~"garena" or name~"freefire" or name~"supercell" or name~"moonton" or name~"dragonraja" or name~"activision" or name~"bandai" or name~"codmobile") && (type="CNAME")] do={
	:local 22g [/ip dns cache all get value-name=name $11g]
	:local 33g [/ip dns cache all get value-name=data $11g]
	:local 44g [:resolve "$33g"]
	:local 55g [:len [/ip fir ad find where address=$44g]]
	:put  message="Address $22g - $44g found, checking availability on firewall address list"
	:if ($55g=0) do={
		/ip fir ad add address=$44g list=GAME
		:local sms ("DNS game $22g has been added succesfully")
		:put $sms
		:log info message="$sms"
		/ip fir ad set [find where address=$44g] comment=[]
	}
}
delay 2s;
foreach 11gg in=[/ip dns cache all find where (name~"zynga" or name~"kojima" or name~"konami" or name~"projektred" or name~"rockstar" or name~"ubisoft" or name~"gameloft" or name~"superevil" or name~"mojang" or name~"game" or name~"steampowered" or name~"garena" or name~"freefire" or name~"supercell" or name~"moonton" or name~"dragonraja" or name~"activision" or name~"bandai" or name~"codmobile") && (type="A")] do={
	:local 22gg [/ip dns cache all get value-name=name $11gg]
	:local 33gg [/ip dns cache all get value-name=data $11gg]
	:local 55gg [:len [/ip fir ad find where address=$33gg]]
	:put  message="Address $22gg - $33gg found, checking availability on firewall address list"
	:if ($55gg=0) do={
		/ip fir ad add address=$33gg list=GAME
		:local sms ("DNS game $22gg has been added succesfully")
		:put $sms
		:log info message="$sms"
		/ip fir ad set [find where address=$33gg] comment=[]
	}
}
delay 1s;
foreach 11s in=[/ip dns cache all find where (name~"tiktok" or name~"instagram" or name~"fbcdn" or name~"whatsapp" or name~"telegram" or name~"wa.me" or name~"today.line" or name~"likee" or name~"twitter" or name~"twimg" or name~"pinterest" or name~"pinimg" or name~"snapchat" or name~"appspot.com" or name~"linkedin" or name~"licdn" or name~"line-scdn" or name~"tumblr" or name~"reddit" or name~"facebook" or name~"1cak.com" or name~"redd.it") && (type="CNAME")] do={
	:local 22s [/ip dns cache all get value-name=name $11s]
	:local 33s [/ip dns cache all get value-name=data $11s]
	:local 44s [:resolve "$33s"]
	:local 55s [:len [/ip fir ad find where address=$44s]]
	:put  message="Address $22s - $44s found, checking availability on firewall address list"
	:if ($55s=0) do={
		/ip fir ad add address=$44s list=SOSMED
		:local sms ("DNS sosmed $22s has been added succesfully")
		:put $sms
		:log info message="$sms"
		/ip fir ad set [find where address=$44s] comment=[]
	}
}
delay 1s;
foreach 11ss in=[/ip dns cache all find where (name~"tiktok" or name~"instagram" or name~"fbcdn" or name~"whatsapp" or name~"telegram" or name~"wa.me" or name~"today.line" or name~"likee" or name~"twitter" or name~"twimg" or name~"pinterest" or name~"pinimg" or name~"snapchat" or name~"appspot.com" or name~"linkedin" or name~"licdn" or name~"line-scdn" or name~"tumblr" or name~"reddit" or name~"facebook" or name~"1cak.com" or name~"redd.it") && (type="A")] do={
	:local 22ss [/ip dns cache all get value-name=name $11ss]
	:local 33ss [/ip dns cache all get value-name=data $11ss]
	:local 55ss [:len [/ip fir ad find where address=$33ss]]
	:put  message="Address $22ss - $33ss found, checking availability on firewall address list"
	:if ($55ss=0) do={
		/ip fir ad add address=$33ss list=SOSMED
		:local sms ("DNS sosmed $22ss has been added succesfully")
		:put $sms
		:log info message="$sms"
		/ip fir ad set [find where address=$33ss] comment=[]
	}
}


File: /firewall-raw-video-stream.rsc
/ip firewall raw
add action=add-dst-to-address-list address-list=VIDEO-STREAMING \
    address-list-timeout=5d chain=prerouting comment=TWITCH content=\
    .twitchcdn.com disabled=no !dscp !dst-address !dst-address-list \
    !dst-address-type !dst-limit !dst-port !fragment !hotspot !icmp-options \
    !in-interface !in-interface-list !ingress-priority !ipsec-policy \
    !ipv4-options !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=add-dst-to-address-list address-list=VIDEO-STREAMING \
    address-list-timeout=5d chain=prerouting comment=TIKTOK content=\
    .tiktokcdn.com disabled=yes !dscp !dst-address !dst-address-list \
    !dst-address-type !dst-limit !dst-port !fragment !hotspot !icmp-options \
    !in-interface !in-interface-list !ingress-priority !ipsec-policy \
    !ipv4-options !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=add-dst-to-address-list address-list=VIDEO-STREAMING \
    address-list-timeout=5d chain=prerouting comment=YOUTUBE content=\
    .googlevideo.com disabled=yes !dscp !dst-address !dst-address-list \
    !dst-address-type !dst-limit !dst-port !fragment !hotspot !icmp-options \
    !in-interface !in-interface-list !ingress-priority !ipsec-policy \
    !ipv4-options !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=add-dst-to-address-list address-list=VIDEO-STREAMING \
    address-list-timeout=5d chain=prerouting comment="NIMO TV" content=\
    .nimo.tv disabled=no !dscp !dst-address !dst-address-list \
    !dst-address-type !dst-limit !dst-port !fragment !hotspot !icmp-options \
    !in-interface !in-interface-list !ingress-priority !ipsec-policy \
    !ipv4-options !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=jump chain=prerouting comment="GO TO VIDEO CHAIN" content=video \
    disabled=no !dscp !dst-address !dst-address-list !dst-address-type \
    !dst-limit !dst-port !fragment !hotspot !icmp-options !in-interface \
    !in-interface-list !ingress-priority !ipsec-policy !ipv4-options \
    jump-target=video !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=add-dst-to-address-list address-list=VIDEO-STREAMING \
    address-list-timeout=5d chain=video comment="FACEBOOK VIDEO" content=\
    .fbcdn.net disabled=no !dscp !dst-address !dst-address-list \
    !dst-address-type !dst-limit !dst-port !fragment !hotspot !icmp-options \
    !in-interface !in-interface-list !ingress-priority !ipsec-policy \
    !ipv4-options !limit log=no log-prefix="" !nth !out-interface \
    !out-interface-list !packet-size !per-connection-classifier !port \
    !priority !protocol !psd !random !src-address !src-address-list \
    !src-address-type !src-mac-address !src-port !tcp-flags !tcp-mss !time \
    !tls-host !ttl
add action=return chain=video comment="RETURN TO BEFORE VIDEO CHAIN" !content \
    disabled=no !dscp !dst-address !dst-address-list !dst-address-type \
    !dst-limit !dst-port !fragment !hotspot !icmp-options !in-interface \
    !in-interface-list !ingress-priority !ipsec-policy !ipv4-options !limit \
    log=no log-prefix="" !nth !out-interface !out-interface-list !packet-size \
    !per-connection-classifier !port !priority !protocol !psd !random \
    !src-address !src-address-list !src-address-type !src-mac-address \
    !src-port !tcp-flags !tcp-mss !time !tls-host !ttl


File: /first-setup
#Add a new scheduler setting with following event:
#Change telegram chat id below with your own
:global CHATID ("-4936xxx")
#Change telegram bot id below with your own
:global BOTID ("62xxxxxxxx:AAExxxx")
:global GetMacVendor do={
	:do {
		return ([/tool fetch mode=https http-method=get url=("https://api.macvendors.com/".[:pick [:tostr $1] 0 8 ]) as-value output=user ]->"data")
	} on-error={
		return "vendor not found"
	}
}
#source: https://s.id/q4f-O
:global ConvertLowerCase do={
	:local alphabet {"A"="a";"B"="b";"C"="c";"D"="d";"E"="e";"F"="f";"G"="g";"H"="h";"I"="i";"J"="j";"K"="k";"L"="l";"M"="m";"N"="n";"O"="o";"P"="p";"Q"="q";"R"="r";"S"="s";"T"="t";"U"="u";"V"="v";"X"="x";"Z"="z";"Y"="y";"W"="w"};
	:local result
	:local character
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings]
		:set character ($alphabet->$single)
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single)
	}
	:return $result
}

:global ConvertUpperCase do={
	:local alphabet {"a"="A";"b"="B";"c"="C";"d"="D";"e"="E";"f"="F";"g"="G";"h"="H";"i"="I";"j"="J";"k"="K";"l"="L";"m"="M";"n"="N";"o"="O";"p"="P";"q"="Q";"r"="R";"s"="S";"t"="T";"u"="U";"v"="V";"x"="X";"z"="Z";"y"="Y";"w"="W"};
	:local result
	:local character
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings]
		:set character ($alphabet->$single)
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single)
	}
	:return $result
}
:global ConnectionAvailable do={
	:local internet
	/tool flood-ping 8.8.8.8 count=10 do={
		/if ($received > 8) do={
			:set $internet true;
		} else={
			:set internet false;
		}
	}
	:return $internet
}
#This script is inspired by TSOKOTSA's script published in the Mikrotik forum
:global GenerateRandomString do={
	:local hour [:pick [/system clock get time] 0 2]
	:local hourx
	:local minute [:pick [/system clock get time] 3 5]
	:local minutex
	:local second [:pick [/system clock get time] 6 8]
	:local secondx
	:local hundred ("1$second")
	:local hundred2 ("1$minute")
	:local hundred3 ("1$hour")
	:local utsec
	:local uthour
	:local utmin
	:local uptime [/system resource get uptime]
	:if ([:len $uptime] = 10) do={:set utsec [:pick $uptime 8 10]; :set utmin [:pick $uptime 5 7]; :set uthour [:pick $uptime 2 4]}
	:if ([:len $uptime] = 11) do={:set utsec [:pick $uptime 9 11]; :set utmin [:pick $uptime 6 8]; :set uthour [:pick $uptime 3 5]}
	:if ([:len $uptime] = 12) do={:set utsec [:pick $uptime 10 12]; :set utmin [:pick $uptime 7 9]; :set uthour [:pick $uptime 4 6]}
	:if ([:len $uptime] = 8) do={:set utsec [:pick $uptime 6 8]; :set utmin [:pick $uptime 3 5]; :set uthour [:pick $uptime 0 2]}
	:if (([:len $uptime] != 12) and ([:len $uptime] != 10) and ([:len $uptime] != 11) and ([:len $uptime] != 8)) do={
		/log error message="Script error please contact the creator"
	}
	:if (([:pick $hour 1] = [:pick $hour 0]) or ([:pick $minute 1] = [:pick $minute 0]) or ([:pick $second 1] = [:pick $second 0])) do={
		:set hourx (([:pick $hour 1].[:pick $hour 0]) + 1)
		:set minutex (([:pick $minute 1].[:pick $minute 0]) + 1)
		:set secondx (([:pick $second 1].[:pick $second 0]) + 8)
	} else={
		:set hourx ([:pick $hour 1].[:pick $hour 0])
		:set minutex ([:pick $minute 1].[:pick $minute 0])
		:set secondx ([:pick $second 1].[:pick $second 0])
	}
	:if ($hundred2 = $hundred) do={:set hundred2 ($hundred2 + $hour + 1)}
	:if (($hundred3 = $hundred) or ($hundred3 = $hundred2)) do={ :set hundred3 ($hundred3 + $second)}
	:if ($minute + $utsec - $hour < 5) do={
		:set utsec ($utsec + 25)
		:set minute ($minute + 60)
	}
	:local string ("fmIHMh52a2sSFIkSCxXkazAiBN09ypjm8F7fK0TxwTGXzaf054139uXhkEwF13Byi58JoA3lvfQr4Y6Ff257Nn5j06FI4eyzskfZybp9KjTnF9YATlBlTfP5j9uzTHspdnY6GfdQA4ekCl83qX2h382FlJv2iQFQPVZfFl15zBcqiV6TQlG3ytdQNyYJWEFy61305atf965w39iP4k6CCM5Ol0wdYZHFfcc0xFpr1ONybU9Dc3FtMCiDaGIzHu9BW4faZE2s938qs9j07pPiCfuD8OWqFEX9ukPkLl4kuNq3VjYJ1Av7W5n2")
	:local RandomString
	:set RandomString ([:pick $string ($second + uthour)].[:pick $string ($secondx + $uthour)].[:pick $string ($minute + $utsec - $hour)].[:pick $string ($minute + $uthour + $secondx)].[:pick $string [:tonum ($hundred + $uthour)]].[:pick $string [:tonum ($hundred2 + $utsec)]].[:pick $string [:tonum $hundred3]].[:pick $string ($utmin + $hourx + $second)].[:pick $string ($hourx + $hour + $second)].[:pick $string ($secondx + $utsec)])
	:return $RandomString
}



File: /get-random-string
#This script is inspired by TSOKOTSA's script published in the Mikrotik forum
:local hour [:pick [/system clock get time] 0 2]
:local hourx
:local minute [:pick [/system clock get time] 3 5]
:local minutex
:local second [:pick [/system clock get time] 6 8]
:local secondx
:local hundred ("1$second")
:local hundred2 ("1$minute")
:local hundred3 ("1$hour")
:local utsec
:local uthour
:local utmin
:local uptime [/system resource get uptime]
:if ([:len $uptime] = 10) do={:set utsec [:pick $uptime 8 10]; :set utmin [:pick $uptime 5 7]; :set uthour [:pick $uptime 2 4]}
:if ([:len $uptime] = 11) do={:set utsec [:pick $uptime 9 11]; :set utmin [:pick $uptime 6 8]; :set uthour [:pick $uptime 3 5]}
:if ([:len $uptime] = 12) do={:set utsec [:pick $uptime 10 12]; :set utmin [:pick $uptime 7 9]; :set uthour [:pick $uptime 4 6]}
:if ([:len $uptime] = 8) do={:set utsec [:pick $uptime 6 8]; :set utmin [:pick $uptime 3 5]; :set uthour [:pick $uptime 0 2]}
:if (([:len $uptime] != 12) and ([:len $uptime] != 10) and ([:len $uptime] != 11) and ([:len $uptime] != 8)) do={
	/log error message="Script error please contact the creator"
}

:if (([:pick $hour 1] = [:pick $hour 0]) or ([:pick $minute 1] = [:pick $minute 0]) or ([:pick $second 1] = [:pick $second 0])) do={
	:set hourx (([:pick $hour 1].[:pick $hour 0]) + 1)
	:set minutex (([:pick $minute 1].[:pick $minute 0]) + 1)
	:set secondx (([:pick $second 1].[:pick $second 0]) + 8)
} else={
	:set hourx ([:pick $hour 1].[:pick $hour 0])
	:set minutex ([:pick $minute 1].[:pick $minute 0])
	:set secondx ([:pick $second 1].[:pick $second 0])
}
:if ($hundred2 = $hundred) do={:set hundred2 ($hundred2 + $hour + 1)}
:if (($hundred3 = $hundred) or ($hundred3 = $hundred2)) do={ :set hundred3 ($hundred3 + $second)}
:if ($minute + $utsec - $hour < 5) do={
	:set utsec ($utsec + 25)
	:set minute ($minute + 60)
} else={
	:nothing
}

:local string ("H","3","N","J","L","g","R","b","O","i","9","U","F","G","G","7","k","M","q","F","u","5","w","v","o","O","Q","V","r","6","9","l","u","n","Q","l","M","C","9","j","a","s","Y","h","K","S","N","T","d","H","i","f","E","f","q","0","7","0","w","s","X","h","9","b","X","b","n","n","R","E","z","q","r","w","7","Z","N","5","d","2","P","4","q","V","o","T","b","H","X","I","f","K","6","b","x","y","t","B","E","c","S","m","f","A","9","J","V","H","s","W","l","m","V","Z","p","u","c","r","1","Q","A","Z","2","h","E","P","t","M","c","K","V","B","g","z","J","x","k","y","q","W","K","p","i","R","Z","R","7","A","5","Y","a","A","o","H","X","4","6","9","R","Z","A","d","c","i","L","K","5","T","g","f","W","M","Y","S","J","v","V","t","N","O","F","T","v","6","y","u","p","0","H","W","Y","i","G","I","X","A","W","P","u","l","9","t","1","s","Q","a","e","I","N","E","5","K","O","l","E","m","3","L","P","2","4","s","O","y","Y","V","l","3","y","T","D","b","3","6","N","F","x","4","7","f","9","6","1","R","1","q","T","Z","3","U","W","M","X","H","z","o","T","V","e","O","G","m","0","Q","t","c","8","9","6","g","8","X","f","l","Y","V","a","t","O","5","e","z","C","2","S","K","6","e","Q","d","K","v","j","j")

:global RandomString
:set RandomString ([:pick $string ($second + uthour)].[:pick $string ($secondx + $uthour)].[:pick $string ($minute + $utsec - $hour)].[:pick $string ($minute + $uthour + $secondx)].[:pick $string [:tonum ($hundred + $uthour)]].[:pick $string [:tonum ($hundred2 + $utsec)]].[:pick $string [:tonum $hundred3]].[:pick $string ($utmin + $hourx + $second)].[:pick $string ($hourx + $hour + $second)].[:pick $string ($secondx + $utsec)])
:put message="Here are your random strings: $RandomString"
:put message=([/system clock get time]." - ".[/system clock get date])




File: /LICENSE
MIT License

Copyright (c) 2020 furaihan

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


File: /list-port-game
#SOURCE: INTERNET
{/ip firewall raw
add action=add-dst-to-address-list address-list=virus address-list-timeout=1d \
chain=prerouting comment=Virus dst-address-list=!not_in_internet dst-port=\
67,135-139,445,520,3389,20004,7533,5678,20561 protocol=udp \
src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Vainglory dst-address-list=!not_in_internet dst-port=\
7000-8020 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Vainglory content=.superevil.net \
dst-address-list=!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Mobile Legends" dst-address-list=!not_in_internet \
dst-port=30000-30150 protocol=tcp 
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Mobile Legends" dst-address-list=!not_in_internet \
dst-port=44590-44610 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="PUBG Mobile" dst-address-list=!not_in_internet \
dst-port=10012-17500 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="PUBG Mobile" dst-address-list=!not_in_internet \
dst-port=7086-7995,12070-12460,41182-42474 protocol=udp src-address-list=\
not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="PUBG Mobile" content=tencentgames.helpshift.com \
dst-address-list=!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Garena" content=.garenanow.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=FM19 content=.amazonaws.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=FM19 content=fm19 dst-address-list=!not_in_internet \
src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Roblox content=roblox dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Roblox content=roblox.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Roblox dst-address-list=!not_in_internet dst-port=\
56849-57729,60275-64632 protocol=udp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Minecraft content=mojang dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Minecraft content=.mojang.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Minecraft content=unity dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Amazonaws content=.amazonaws.com \
dst-address-list=!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Gameloft content=.gameloft.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Xboxlive content=.xboxlive.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Friv.COM content=.friv.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Asphalt 9" dst-address-list=!not_in_internet \
dst-port=420,36323,45125,46339,43393 protocol=tcp src-address-list=\
not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Asphalt 9" dst-address-list=!not_in_internet \
dst-port=3544 protocol=udp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=Gameloop content=.qq.com dst-address-list=\
!not_in_internet src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="Free Fire" dst-address-list=!not_in_internet \
dst-port=10000-10007 protocol=udp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=DOTA2 dst-address-list=!not_in_internet dst-port=\
27000-28998 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=DOTA2 dst-address-list=!not_in_internet dst-port=\
27000-28998 protocol=udp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=PALADINS dst-address-list=!not_in_internet dst-port=\
9000-9999 protocol=udp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment=PALADINS dst-address-list=!not_in_internet dst-port=\
9000-9999 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="FIFA ONLINE" dst-address-list=!not_in_internet \
dst-port=7770-7790 protocol=tcp src-address-list=not_in_internet
add action=add-dst-to-address-list address-list=GAME address-list-timeout=1d \
chain=prerouting comment="FIFA ONLINE" dst-address-list=!not_in_internet \
dst-port=16300-16350 protocol=udp src-address-list=not_in_internet
}


File: /quad9-doh.rsc
/ip dns
set allow-remote-requests=yes cache-max-ttl=2d cache-size=8192KiB \
    query-server-timeout=4s query-total-timeout=20s servers=\
    9.9.9.9,149.112.112.112,2620:fe::fe,2620:fe::fe:9 use-doh-server=\
    https://dns.quad9.net/dns-query
/ip dns static
add address=104.16.248.249 name=cloudflare-dns.com type=A
add address=104.16.249.249 name=cloudflare-dns.com type=A
/ip firewall nat
add action=redirect chain=dstnat comment=DNS dst-port=53 protocol=udp \
    to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=tcp to-ports=53


File: /README.md
# simple-mikrotik-script [WORK IN PROGRESS]
simple mikrotik script to maximize the performance of your router


File: /scheduler.rsc
/system scheduler
add name=schedule1 on-event=first-setup policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup


File: /secure-your-router
{
#SOURCE https://help.mikrotik.com/docs/display/ROS/Building+Your+First+Firewall
#Protect the router itself
#	work with new connections to decrease load on a router;
#	create address-list for IP addresses, that are allowed to access your router;
#	enable ICMP access (optionally);
#	drop everything else, log=yes might be added to log packets that hit the specific rule;

/ip firewall filter
add action=accept chain=input comment="default configuration" connection-state=established,related
add action=accept chain=input src-address-list=allowed_to_router
add action=accept chain=input protocol=icmp
add action=drop chain=input
/ip firewall address-list
add address=192.168.88.2-192.168.88.254 list=allowed_to_router

#Protect the LAN devices
#We will create address-list with name "not_in_internet" which we will use for the future firewall rules:

/ip firewall address-list
add address=0.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=172.16.0.0/12 comment=RFC6890 list=not_in_internet
add address=192.168.0.0/16 comment=RFC6890 list=not_in_internet
add address=10.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=169.254.0.0/16 comment=RFC6890 list=not_in_internet
add address=127.0.0.0/8 comment=RFC6890 list=not_in_internet
add address=224.0.0.0/4 comment=Multicast list=not_in_internet
add address=198.18.0.0/15 comment=RFC6890 list=not_in_internet
add address=192.0.0.0/24 comment=RFC6890 list=not_in_internet
add address=192.0.2.0/24 comment=RFC6890 list=not_in_internet
add address=198.51.100.0/24 comment=RFC6890 list=not_in_internet
add address=203.0.113.0/24 comment=RFC6890 list=not_in_internet
add address=100.64.0.0/10 comment=RFC6890 list=not_in_internet
add address=240.0.0.0/4 comment=RFC6890 list=not_in_internet
add address=192.88.99.0/24 comment="6to4 relay Anycast [RFC 3068]" list=not_in_internet

#jump to ICMP chain to drop unwanted ICMP messages

/ip firewall filter
  add chain=icmp protocol=icmp icmp-options=0:0 action=accept \
    comment="echo reply"
  add chain=icmp protocol=icmp icmp-options=3:0 action=accept \
    comment="net unreachable"
  add chain=icmp protocol=icmp icmp-options=3:1 action=accept \
    comment="host unreachable"
  add chain=icmp protocol=icmp icmp-options=3:4 action=accept \
    comment="host unreachable fragmentation required"
  add chain=icmp protocol=icmp icmp-options=8:0 action=accept \
    comment="allow echo request"
  add chain=icmp protocol=icmp icmp-options=11:0 action=accept \
    comment="allow time exceed"
  add chain=icmp protocol=icmp icmp-options=12:0 action=accept \
    comment="allow parameter bad"
  add chain=icmp action=drop comment="deny all other types"
  
#set policy for read user so they cant reboot your router without permission
/user group set read policy=!reboot

local DisableService do={
/ip service
set ftp disabled=yes
set www disabled=yes
set ssh disabled=yes
set api disabled=yes
set api-ssl disabled=yes
}

#DISABLE UNUSED SERVICES (Remove the hashtag # below to disable unused services)
#$DisableService
}


