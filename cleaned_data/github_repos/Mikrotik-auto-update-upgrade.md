# Repository Information
Name: Mikrotik-auto-update-upgrade

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-auto-update-upgrade/
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
    │   │       ├── pack-c5bf28347ffdc8eb2b79c09947b1f169d47a7bb5.idx
    │   │       └── pack-c5bf28347ffdc8eb2b79c09947b1f169d47a7bb5.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── autoinstall.rsc
    ├── CHR/
    │   ├── autoinstall.rsc
    │   ├── install.rsc
    │   ├── script.rsc
    │   ├── SendBackup.rsc
    │   ├── Update.rsc
    │   └── WakeUp.rsc
    ├── install.rsc
    ├── README.md
    ├── script.rsc
    ├── SendBackup.rsc
    ├── Update.rsc
    └── WakeUp.rsc


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
	url = https://github.com/maximmum521/Mikrotik-auto-update-upgrade.git
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
0000000000000000000000000000000000000000 c008167b3d57a0b29fd847d174e77e618310d772 vivek-dodia <vivek.dodia@icloud.com> 1738606034 -0500	clone: from https://github.com/maximmum521/Mikrotik-auto-update-upgrade.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 c008167b3d57a0b29fd847d174e77e618310d772 vivek-dodia <vivek.dodia@icloud.com> 1738606034 -0500	clone: from https://github.com/maximmum521/Mikrotik-auto-update-upgrade.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c008167b3d57a0b29fd847d174e77e618310d772 vivek-dodia <vivek.dodia@icloud.com> 1738606034 -0500	clone: from https://github.com/maximmum521/Mikrotik-auto-update-upgrade.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c008167b3d57a0b29fd847d174e77e618310d772 refs/remotes/origin/main


File: /.git\refs\heads\main
c008167b3d57a0b29fd847d174e77e618310d772


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /autoinstall.rsc
:local delname;
:local wakeup "no";
:local sendback "no";
:local mail "NO";
##### make backup
:local readinput do={:return};
:put "\ndo you want make backup ??? [y or n] \n\r\ndefault set \"n\"\n";
:local makebackup [$readinput];
:if ("y" = $makebackup or "Y" = $makebackup) do={
/export file=installbackup;
:delay 2s;
/system backup save name=installbackup;
:delay 2s;
:local readinput do={:return};
:put "\nyou can download backup file \"installbackup.backup\" and \"installbackup.rsc\" \r\npress any key to continue";
:local tmp [$readinput];
};
##### remove old script
:local funDelScr do={
:local tmp [:len [/system/script/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del script $delname";
/system script remove $delname;
};
};
$funDelScr delname="ScriptSetings";
$funDelScr delname="SendBackup";
$funDelScr delname="Update";
$funDelScr delname="WakeUp";
$funDelScr delname="UpdateStat";
$funDelScr delname="UpgradeStat";
##### remove old scheduler
:local funDelSch do={
:local tmp [:len [/system/scheduler/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del scheduler $delname";
/system scheduler remove $delname;
};
};
$funDelSch delname="WakeUp";
$funDelSch delname="Update";
##### send wakeup 
:local readinput do={:return};
:put "\nsend wakeup messages [y or n] \n\r\ndefault set \"n\"\n";
:local sendwake [$readinput];
##### send backup 
:local readinput do={:return};
:put "\nsend backup to mail [y or n] \n\r\ndefault set \"n\"\n";
:local backmail [$readinput];
##### chat ID 
:local readinput do={:return};
:put "\nInsert a chat ID\n";
:local chat [$readinput];
##### bot ID
:local readinput do={:return};
:put "\nInsert a bot ID\n";
:local bot [$readinput];
##### mail
:if ("y" = $backmail or "Y" = $backmail) do={
:set sendback "yes";
:local readinput do={:return};
:put "\nInsert a mail\n";
:set mail [$readinput];
};
##### test messages
:local readinput do={:return};
:put "\nSend test messages [y or n]\n\r\ndefault set \"n\"\n";
:local testmessages [$readinput];
##### test messages func
:local messages "test messages from MikroTik %0achatID $chat %0abotID $bot %0amail $mail";
:local sendFunc do={
	/tool fetch url="https://api.telegram.org/bot$bot/sendMessage\?chat_id=$chat&text=$messages" keep-result=no;
};
##### output
:local outputFUNC do={
:put "\nCheck \r\nchat ID : $chat \r\nbot ID : $bot \r\nmail : $mail";
};
##### add settings script func
:local ADDscriptFUNC do={
/system script add name=ScriptSetings source="\
:global BotId \"$bot\";\
\r\n:global ChatId \"$chat\";\
\r\n:global Mail \"$mail\";\
\r\n:global sendbackupupgrade \"no\";\
\r\n:global wakeup \"$wakeup\";\
\r\n:global sendbackup \"$sendback\";"
};
#####
:local ADDscriptFUNCup do={
/system script add name=UpdateStat source="\
\r\n:global updatestatus \"no\";"
};
#####
:local ADDscriptUpgradeStat do={
/system script add name=UpgradeStat source="\
:global upgradestatus \"no\";"
};
##### del file
:local funDelFile do={
:local tmp [:len [/file/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del file $delname";
/file remove $delname;
};
};
##### run
:if ("y" = $sendwake or "Y" = $sendwake) do={
:set wakeup "yes";
};
$outputFUNC bot=[$bot] chat=[$chat] mail=[$mail];
$ADDscriptFUNC bot=[$bot] chat=[$chat] mail=[$mail] wakeup=[$wakeup] sendback=[$sendback];
$ADDscriptFUNCup;
$ADDscriptUpgradeStat;
:if ("y" = $testmessages or "Y" = $testmessages) do={
$sendFunc bot=[$bot] chat=[$chat] mail=[$mail] messages=[$messages];
};
/tool fetch url="https://raw.githubusercontent.com/maximmum521/Mikrotik-auto-update-upgrade/main/script.rsc";
:import script.rsc;
:delay 2s;
$funDelFile delname="script.rsc";
:delay 1s;
$funDelFile delname="install.rsc";
:delay 1s;
$funDelScr delname="install";
:put "\nEND";

File: /CHR\autoinstall.rsc
:local delname;
:local wakeup "no";
:local sendback "no";
:local mail "NO";
##### make backup
:local readinput do={:return};
:put "\ndo you want make backup ??? [y or n] \n\r\ndefault set \"n\"\n";
:local makebackup [$readinput];
:if ("y" = $makebackup or "Y" = $makebackup) do={
/export file=installbackup;
:delay 2s;
/system backup save name=installbackup;
:delay 2s;
:local readinput do={:return};
:put "\nyou can download backup file \"installbackup.backup\" and \"installbackup.rsc\" \r\npress any key to continue";
:local tmp [$readinput];
};
##### remove old script
:local funDelScr do={
:local tmp [:len [/system/script/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del script $delname";
/system script remove $delname;
};
};
$funDelScr delname="ScriptSetings";
$funDelScr delname="SendBackup";
$funDelScr delname="Update";
$funDelScr delname="WakeUp";
$funDelScr delname="UpdateStat";
##### remove old scheduler
:local funDelSch do={
:local tmp [:len [/system/scheduler/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del scheduler $delname";
/system scheduler remove $delname;
};
};
$funDelSch delname="WakeUp";
$funDelSch delname="Update";
##### send wakeup 
:local readinput do={:return};
:put "\nsend wakeup messages [y or n] \n\r\ndefault set \"n\"\n";
:local sendwake [$readinput];
##### send backup 
:local readinput do={:return};
:put "\nsend backup to mail [y or n] \n\r\ndefault set \"n\"\n";
:local backmail [$readinput];
##### chat ID 
:local readinput do={:return};
:put "\nInsert a chat ID\n";
:local chat [$readinput];
##### bot ID
:local readinput do={:return};
:put "\nInsert a bot ID\n";
:local bot [$readinput];
##### mail
:if ("y" = $backmail or "Y" = $backmail) do={
:set sendback "yes";
:local readinput do={:return};
:put "\nInsert a mail\n";
:set mail [$readinput];
};
##### test messages
:local readinput do={:return};
:put "\nSend test messages [y or n]\n\r\ndefault set \"n\"\n";
:local testmessages [$readinput];
##### test messages func
:local messages "test messages from MikroTik %0achatID $chat %0abotID $bot %0amail $mail";
:local sendFunc do={
	/tool fetch url="https://api.telegram.org/bot$bot/sendMessage\?chat_id=$chat&text=$messages" keep-result=no;
};
##### output
:local outputFUNC do={
:put "\nCheck \r\nchat ID : $chat \r\nbot ID : $bot \r\nmail : $mail";
};
##### add settings script func
:local ADDscriptFUNC do={
/system script add name=ScriptSetings source="\
:global BotId \"$bot\";\
\r\n:global ChatId \"$chat\";\
\r\n:global Mail \"$mail\";\
\r\n:global wakeup \"$wakeup\";\
\r\n:global sendbackup \"$sendback\";"
};
:local ADDscriptFUNCup do={
/system script add name=UpdateStat source="\
\r\n:global updatestatus \"no\";"
};
##### del file
:local funDelFile do={
:local tmp [:len [/file/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del file $delname";
/file remove $delname;
};
};
##### run
:if ("y" = $sendwake or "Y" = $sendwake) do={
:set wakeup "yes";
};
$outputFUNC bot=[$bot] chat=[$chat] mail=[$mail];
$ADDscriptFUNC bot=[$bot] chat=[$chat] mail=[$mail] wakeup=[$wakeup] sendback=[$sendback];
$ADDscriptFUNCup;
:if ("y" = $testmessages or "Y" = $testmessages) do={
$sendFunc bot=[$bot] chat=[$chat] mail=[$mail] messages=[$messages];
};
/tool fetch url="https://raw.githubusercontent.com/maximmum521/Mikrotik-auto-update-upgrade/main/CHR/script.rsc";
:import script.rsc;
:delay 2s;
$funDelFile delname="script.rsc";
:delay 1s;
$funDelFile delname="install.rsc";
:delay 1s;
$funDelScr delname="install";
:put "\nEND";

File: /CHR\install.rsc
/system script
add dont-require-permissions=no name=install policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    local delname;\r\
    \n:local wakeup \"no\";\r\
    \n:local sendback \"no\";\r\
    \n:local mail \"NO\";\r\
    \n##### make backup\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\ndo you want make backup \?\?\? [y or n] \\n\\r\\ndefault set \
    \\\"n\\\"\\n\";\r\
    \n:local makebackup [\$readinput];\r\
    \n:if (\"y\" = \$makebackup or \"Y\" = \$makebackup) do={\r\
    \n/export file=installbackup;\r\
    \n:delay 2s;\r\
    \n/system backup save name=installbackup;\r\
    \n:delay 2s;\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nyou can download backup file \\\"installbackup.backup\\\" and \
    \\\"installbackup.rsc\\\" \\r\\npress any key to continue\";\r\
    \n:local tmp [\$readinput];\r\
    \n};\r\
    \n##### remove old script\r\
    \n:local funDelScr do={\r\
    \n:local tmp [:len [/system/script/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del script \$delname\";\r\
    \n/system script remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n\$funDelScr delname=\"ScriptSetings\";\r\
    \n\$funDelScr delname=\"SendBackup\";\r\
    \n\$funDelScr delname=\"Update\";\r\
    \n\$funDelScr delname=\"WakeUp\";\r\
    \n\$funDelScr delname=\"UpdateStat\";\r\
    \n##### remove old scheduler\r\
    \n:local funDelSch do={\r\
    \n:local tmp [:len [/system/scheduler/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del scheduler \$delname\";\r\
    \n/system scheduler remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n\$funDelSch delname=\"WakeUp\";\r\
    \n\$funDelSch delname=\"Update\";\r\
    \n##### send wakeup \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nsend wakeup messages [y or n] \\n\\r\\ndefault set \\\"n\\\"\\\
    n\";\r\
    \n:local sendwake [\$readinput];\r\
    \n##### send backup \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nsend backup to mail [y or n] \\n\\r\\ndefault set \\\"n\\\"\\n\
    \";\r\
    \n:local backmail [\$readinput];\r\
    \n##### chat ID \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a chat ID\\n\";\r\
    \n:local chat [\$readinput];\r\
    \n##### bot ID\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a bot ID\\n\";\r\
    \n:local bot [\$readinput];\r\
    \n##### mail\r\
    \n:if (\"y\" = \$backmail or \"Y\" = \$backmail) do={\r\
    \n:set sendback \"yes\";\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a mail\\n\";\r\
    \n:set mail [\$readinput];\r\
    \n};\r\
    \n##### test messages\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nSend test messages [y or n]\\n\\r\\ndefault set \\\"n\\\"\\n\"\
    ;\r\
    \n:local testmessages [\$readinput];\r\
    \n##### test messages func\r\
    \n:local messages \"test messages from MikroTik %0achatID \$chat %0abotID \
    \$bot %0amail \$mail\";\r\
    \n:local sendFunc do={\r\
    \n\t/tool fetch url=\"https://api.telegram.org/bot\$bot/sendMessage\\\?cha\
    t_id=\$chat&text=\$messages\" keep-result=no;\r\
    \n};\r\
    \n##### output\r\
    \n:local outputFUNC do={\r\
    \n:put \"\\nCheck \\r\\nchat ID : \$chat \\r\\nbot ID : \$bot \\r\\nmail :\
    \_\$mail\";\r\
    \n};\r\
    \n##### add settings script func\r\
    \n:local ADDscriptFUNC do={\r\
    \n/system script add name=ScriptSetings source=\"\\\r\
    \n:global BotId \\\"\$bot\\\";\\\r\
    \n\\r\\n:global ChatId \\\"\$chat\\\";\\\r\
    \n\\r\\n:global Mail \\\"\$mail\\\";\\\r\
    \n\\r\\n:global wakeup \\\"\$wakeup\\\";\\\r\
    \n\\r\\n:global sendbackup \\\"\$sendback\\\";\"\r\
    \n};\r\
    \n:local ADDscriptFUNCup do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n\\r\\n:global updatestatus \\\"no\\\";\"\r\
    \n};\r\
    \n##### del file\r\
    \n:local funDelFile do={\r\
    \n:local tmp [:len [/file/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del file \$delname\";\r\
    \n/file remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n##### run\r\
    \n:if (\"y\" = \$sendwake or \"Y\" = \$sendwake) do={\r\
    \n:set wakeup \"yes\";\r\
    \n};\r\
    \n\$outputFUNC bot=[\$bot] chat=[\$chat] mail=[\$mail];\r\
    \n\$ADDscriptFUNC bot=[\$bot] chat=[\$chat] mail=[\$mail] wakeup=[\$wakeup\
    ] sendback=[\$sendback];\r\
    \n\$ADDscriptFUNCup;\r\
    \n:if (\"y\" = \$testmessages or \"Y\" = \$testmessages) do={\r\
    \n\$sendFunc bot=[\$bot] chat=[\$chat] mail=[\$mail] messages=[\$messages]\
    ;\r\
    \n};\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/maximmum521/Mikrotik\
    -auto-update-upgrade/main/CHR/script.rsc\";\r\
    \n:import script.rsc;\r\
    \n:delay 2s;\r\
    \n\$funDelFile delname=\"script.rsc\";\r\
    \n:delay 1s;\r\
    \n\$funDelFile delname=\"install.rsc\";\r\
    \n:delay 1s;\r\
    \n\$funDelScr delname=\"install\";\r\
    \n:put \"\\nEND\";"

File: /CHR\script.rsc
/system scheduler
add name=WakeUp on-event="/system script run WakeUp " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
add interval=1w name=Update on-event="/system script run Update " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jan/17/2022 start-time=10:00:00
/system script
add dont-require-permissions=no name=WakeUp policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    delay 120s;\r\
    \n#####\r\
    \n# settings\r\
    \n#####\r\
    \n:local text \"ROUTER WAKE UP\";\r\
    \n:local Tag \"WakeUp\";\r\
    \n/system script run ScriptSetings;\r\
    \n:global BotId;\r\
    \n:global ChatId;\r\
    \n:global wakeup;\r\
    \n/system script run UpdateStat;\r\
    \n:global updatestatus;\r\
    \n:local Cheking [/system package update check-for-updates as-value];\r\
    \n:local CurrentVer (\$Cheking -> \"installed-version\");\r\
    \n:local NewVer (\$Cheking -> \"latest-version\");\r\
    \n#####\r\
    \n:local sendFunc do={\r\
    \n  /tool fetch url=\"https://api.telegram.org/bot\$BotId/sendMessage\\\?c\
    hat_id=\$ChatId&text=\\\r\
    \n  \$[/system identity get name] \\\r\
    \n  %0a\$text\\\r\
    \n  %0a\$[/system resource get board-name]\\ \r\
    \n  %0a%23\$Tag\" keep-result=no;\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpdateStat do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n:global updatestatus \\\"no\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n:if ( \$updatestatus = \"yes\" ) do={\r\
    \n  :if (\$CurrentVer = \$NewVer) do={  \r\
    \n  :set text \"ROUTER WAKE UP %0aUPDATE OK\"   \r\
    \n  :set Tag \"UPDATE_OK\";\r\
    \n  } else={\r\
    \n  :set text \"ROUTER WAKE UP %0aUPDATE FAILED\"   \r\
    \n  :set Tag \"UPDATE_FAILED\";\r\
    \n  };\r\
    \n  /system script remove UpdateStat;\r\
    \n  \$ADDscriptUpdateStat \r\
    \n  \$sendFunc text=[\$text] BotId=[\$BotId] ChatId=[\$ChatId] Tag=[\$Tag]\
    \r\
    \n  } else={\r\
    \n:if ( \$wakeup = \"yes\" ) do={\r\
    \n  \$sendFunc text=[\$text] BotId=[\$BotId] ChatId=[\$ChatId] Tag=[\$Tag]\
    \_\r\
    \n  };\r\
    \n};"
add dont-require-permissions=no name=Update policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    ####\r\
    \n# telegram setings \r\
    \n#####\r\
    \n/system script run ScriptSetings;\r\
    \n:global BotId;\r\
    \n:global ChatId;\r\
    \n:global sendbackup;\r\
    \n#####\r\
    \n# router info\r\
    \n#####\r\
    \n:local Tag \"%23UpdateRouterOS\";\r\
    \n:local TagStat;\r\
    \n:local Name [/system identity get name];\r\
    \n:local Cheking [/system package update check-for-updates as-value];\r\
    \n:local Stat (\$Cheking -> \"status\");\r\
    \n:local CurrentVer (\$Cheking -> \"installed-version\");\r\
    \n:local NewVer (\$Cheking -> \"latest-version\");\r\
    \n:local Model [/system resource get board-name];\r\
    \n#####\r\
    \n# send status\r\
    \n#####\r\
    \n:local sendFunc do={\r\
    \n\t/tool fetch url=\"https://api.telegram.org/bot\$BotId/sendMessage\\\?c\
    hat_id=\$ChatId&text=\\\r\
    \n\t\$Name\\\r\
    \n\t%0a\$Model\\\r\
    \n\t%0a\$Stat\\\r\
    \n\t%0aCurrent version=\$CurrentVer\\\r\
    \n\t%0aAvailable version=\$NewVer\\  \r\
    \n\t%0a\$Tag \$TagStat\" keep-result=no;\r\
    \n};\r\
    \n:local ADDscriptUpdateStat do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n:global updatestatus \\\"yes\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n:if (\"New version is available\" = \$Stat ) do={\r\
    \n    /system script remove UpdateStat;\r\
    \n\t\$ADDscriptUpdateStat   \r\
    \n\t\$sendFunc ChatId=[\$ChatId] BotId=[\$BotId] Name=[\$Name] Model=[\$Mo\
    del] Stat=[\$Stat] CurrentVer=[\$CurrentVer] NewVer=[\$NewVer] Tag=[\$Tag]\
    \_TagStat=\"%23NeedUpdate\"\t\r\
    \n\t:if ( \$sendbackup = \"yes\") do={\r\
    \n\t:global BackText \"UPDATE PACKAGE RUN BACKUP\";\r\
    \n\t/system script run SendBackup;\r\
    \n\t};\r\
    \n\t/system package update install;\r\
    \n} else={\r\
    \n\t\$sendFunc ChatId=[\$ChatId] BotId=[\$BotId] Name=[\$Name] Model=[\$Mo\
    del] Stat=[\$Stat] CurrentVer=[\$CurrentVer] NewVer=[\$NewVer] Tag=[\$Tag]\
    \_TagStat=\"%23NoNeedUpdate\"\r\
    \n}"
add dont-require-permissions=no name=SendBackup policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    ####\r\
    \n# e-mail setings\r\
    \n#####\r\
    \n/system script run ScriptSetings;\r\
    \n:global Mail;\r\
    \n:global BackText;\r\
    \n#####\r\
    \n:local funDelFile do={\r\
    \n:local tmp [:len [/file/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del file \$delname\";\r\
    \n/file remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n/export file=backup;\r\
    \n/system backup save name=backup;\r\
    \n:delay 5s;\r\
    \n/tool e-mail send to=\$Mail \\\r\
    \nsubject=\"BACKUP \$[/system clock get date]\" \\\r\
    \nbody=\"\$[/system identity get name] \\n\$[/system resource get board-na\
    me] \\n\$BackText\"\\\r\
    \nfile=backup.backup,backup.rsc;\r\
    \n:delay 5s;\r\
    \n\$funDelFile delname=\"backup.backup\";\r\
    \n\$funDelFile delname=\"backup.rsc\";"

File: /CHR\SendBackup.rsc
#####
# e-mail setings
#####
/system script run ScriptSetings;
:global Mail;
:global BackText;
#####
:local funDelFile do={
:local tmp [:len [/file/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del file $delname";
/file remove $delname;
};
};
#####
# run
#####
/export file=backup;
/system backup save name=backup;
:delay 5s;
/tool e-mail send to=$Mail \
subject="BACKUP $[/system clock get date]" \
body="$[/system identity get name] \n$[/system resource get board-name] \n$BackText"\
file=backup.backup,backup.rsc;
:delay 5s;
$funDelFile delname="backup.backup";
$funDelFile delname="backup.rsc";

File: /CHR\Update.rsc
#####
# telegram setings 
#####
/system script run ScriptSetings;
:global BotId;
:global ChatId;
:global sendbackup;
#####
# router info
#####
:local Tag "%23UpdateRouterOS";
:local TagStat;
:local Name [/system identity get name];
:local Cheking [/system package update check-for-updates as-value];
:local Stat ($Cheking -> "status");
:local CurrentVer ($Cheking -> "installed-version");
:local NewVer ($Cheking -> "latest-version");
:local Model [/system resource get board-name];
#####
# send status
#####
:local sendFunc do={
	/tool fetch url="https://api.telegram.org/bot$BotId/sendMessage\?chat_id=$ChatId&text=\
	$Name\
	%0a$Model\
	%0a$Stat\
	%0aCurrent version=$CurrentVer\
	%0aAvailable version=$NewVer\  
	%0a$Tag $TagStat" keep-result=no;
};
:local ADDscriptUpdateStat do={
/system script add name=UpdateStat source="\
:global updatestatus \"yes\";"
};
#####
# run
#####
:if ("New version is available" = $Stat ) do={
    /system script remove UpdateStat;
	$ADDscriptUpdateStat   
	$sendFunc ChatId=[$ChatId] BotId=[$BotId] Name=[$Name] Model=[$Model] Stat=[$Stat] CurrentVer=[$CurrentVer] NewVer=[$NewVer] Tag=[$Tag] TagStat="%23NeedUpdate"	
	:if ( $sendbackup = "yes") do={
	:global BackText "UPDATE PACKAGE RUN BACKUP";
	/system script run SendBackup;
	};
	/system package update install;
} else={
	$sendFunc ChatId=[$ChatId] BotId=[$BotId] Name=[$Name] Model=[$Model] Stat=[$Stat] CurrentVer=[$CurrentVer] NewVer=[$NewVer] Tag=[$Tag] TagStat="%23NoNeedUpdate"
}

File: /CHR\WakeUp.rsc
:delay 120s;
#####
# settings
#####
:local text "ROUTER WAKE UP";
:local Tag "WakeUp";
/system script run ScriptSetings;
:global BotId;
:global ChatId;
:global wakeup;
/system script run UpdateStat;
:global updatestatus;
:local Cheking [/system package update check-for-updates as-value];
:local CurrentVer ($Cheking -> "installed-version");
:local NewVer ($Cheking -> "latest-version");
#####
:local sendFunc do={
  /tool fetch url="https://api.telegram.org/bot$BotId/sendMessage\?chat_id=$ChatId&text=\
  $[/system identity get name] \
  %0a$text\
  %0a$[/system resource get board-name]\ 
  %0a%23$Tag" keep-result=no;
};
#####
:local ADDscriptUpdateStat do={
/system script add name=UpdateStat source="\
:global updatestatus \"no\";"
};
#####
# run
#####
:if ( $updatestatus = "yes" ) do={
  :if ($CurrentVer = $NewVer) do={  
  :set text "ROUTER WAKE UP %0aUPDATE OK"   
  :set Tag "UPDATE_OK";
  } else={
  :set text "ROUTER WAKE UP %0aUPDATE FAILED"   
  :set Tag "UPDATE_FAILED";
  };
  /system script remove UpdateStat;
  $ADDscriptUpdateStat;
  $sendFunc text=[$text] BotId=[$BotId] ChatId=[$ChatId] Tag=[$Tag]
  } else={
:if ( $wakeup = "yes" ) do={
  $sendFunc text=[$text] BotId=[$BotId] ChatId=[$ChatId] Tag=[$Tag] 
  };
};

File: /install.rsc
/system script
add dont-require-permissions=no name=install policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    local delname;\r\
    \n:local wakeup \"no\";\r\
    \n:local sendback \"no\";\r\
    \n:local mail \"NO\";\r\
    \n##### make backup\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\ndo you want make backup \?\?\? [y or n] \\n\\r\\ndefault set \
    \\\"n\\\"\\n\";\r\
    \n:local makebackup [\$readinput];\r\
    \n:if (\"y\" = \$makebackup or \"Y\" = \$makebackup) do={\r\
    \n/export file=installbackup;\r\
    \n:delay 2s;\r\
    \n/system backup save name=installbackup;\r\
    \n:delay 2s;\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nyou can download backup file \\\"installbackup.backup\\\" and \
    \\\"installbackup.rsc\\\" \\r\\npress any key to continue\";\r\
    \n:local tmp [\$readinput];\r\
    \n};\r\
    \n##### remove old script\r\
    \n:local funDelScr do={\r\
    \n:local tmp [:len [/system/script/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del script \$delname\";\r\
    \n/system script remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n\$funDelScr delname=\"ScriptSetings\";\r\
    \n\$funDelScr delname=\"SendBackup\";\r\
    \n\$funDelScr delname=\"Update\";\r\
    \n\$funDelScr delname=\"WakeUp\";\r\
    \n\$funDelScr delname=\"UpdateStat\";\r\
    \n\$funDelScr delname=\"UpgradeStat\";\r\
    \n##### remove old scheduler\r\
    \n:local funDelSch do={\r\
    \n:local tmp [:len [/system/scheduler/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del scheduler \$delname\";\r\
    \n/system scheduler remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n\$funDelSch delname=\"WakeUp\";\r\
    \n\$funDelSch delname=\"Update\";\r\
    \n##### send wakeup \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nsend wakeup messages [y or n] \\n\\r\\ndefault set \\\"n\\\"\\\
    n\";\r\
    \n:local sendwake [\$readinput];\r\
    \n##### send backup \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nsend backup to mail [y or n] \\n\\r\\ndefault set \\\"n\\\"\\n\
    \";\r\
    \n:local backmail [\$readinput];\r\
    \n##### chat ID \r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a chat ID\\n\";\r\
    \n:local chat [\$readinput];\r\
    \n##### bot ID\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a bot ID\\n\";\r\
    \n:local bot [\$readinput];\r\
    \n##### mail\r\
    \n:if (\"y\" = \$backmail or \"Y\" = \$backmail) do={\r\
    \n:set sendback \"yes\";\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nInsert a mail\\n\";\r\
    \n:set mail [\$readinput];\r\
    \n};\r\
    \n##### test messages\r\
    \n:local readinput do={:return};\r\
    \n:put \"\\nSend test messages [y or n]\\n\\r\\ndefault set \\\"n\\\"\\n\"\
    ;\r\
    \n:local testmessages [\$readinput];\r\
    \n##### test messages func\r\
    \n:local messages \"test messages from MikroTik %0achatID \$chat %0abotID \
    \$bot %0amail \$mail\";\r\
    \n:local sendFunc do={\r\
    \n\t/tool fetch url=\"https://api.telegram.org/bot\$bot/sendMessage\\\?cha\
    t_id=\$chat&text=\$messages\" keep-result=no;\r\
    \n};\r\
    \n##### output\r\
    \n:local outputFUNC do={\r\
    \n:put \"\\nCheck \\r\\nchat ID : \$chat \\r\\nbot ID : \$bot \\r\\nmail :\
    \_\$mail\";\r\
    \n};\r\
    \n##### add settings script func\r\
    \n:local ADDscriptFUNC do={\r\
    \n/system script add name=ScriptSetings source=\"\\\r\
    \n:global BotId \\\"\$bot\\\";\\\r\
    \n\\r\\n:global ChatId \\\"\$chat\\\";\\\r\
    \n\\r\\n:global Mail \\\"\$mail\\\";\\\r\
    \n\\r\\n:global sendbackupupgrade \\\"no\\\";\\\r\
    \n\\r\\n:global wakeup \\\"\$wakeup\\\";\\\r\
    \n\\r\\n:global sendbackup \\\"\$sendback\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptFUNCup do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n\\r\\n:global updatestatus \\\"no\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpgradeStat do={\r\
    \n/system script add name=UpgradeStat source=\"\\\r\
    \n:global upgradestatus \\\"no\\\";\"\r\
    \n};\r\
    \n##### del file\r\
    \n:local funDelFile do={\r\
    \n:local tmp [:len [/file/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del file \$delname\";\r\
    \n/file remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n##### run\r\
    \n:if (\"y\" = \$sendwake or \"Y\" = \$sendwake) do={\r\
    \n:set wakeup \"yes\";\r\
    \n};\r\
    \n\$outputFUNC bot=[\$bot] chat=[\$chat] mail=[\$mail];\r\
    \n\$ADDscriptFUNC bot=[\$bot] chat=[\$chat] mail=[\$mail] wakeup=[\$wakeup\
    ] sendback=[\$sendback];\r\
    \n\$ADDscriptFUNCup;\r\
    \n\$ADDscriptUpgradeStat;\r\
    \n:if (\"y\" = \$testmessages or \"Y\" = \$testmessages) do={\r\
    \n\$sendFunc bot=[\$bot] chat=[\$chat] mail=[\$mail] messages=[\$messages]\
    ;\r\
    \n};\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/maximmum521/Mikrotik\
    -auto-update-upgrade/main/script.rsc\";\r\
    \n:import script.rsc;\r\
    \n:delay 2s;\r\
    \n\$funDelFile delname=\"script.rsc\";\r\
    \n:delay 1s;\r\
    \n\$funDelFile delname=\"install.rsc\";\r\
    \n:delay 1s;\r\
    \n\$funDelScr delname=\"install\";\r\
    \n:put \"\\nEND\";"

File: /README.md
# Mikrotik auto update upgrade

### Automate install from console 

```
/tool fetch url="https://raw.githubusercontent.com/maximmum521/Mikrotik-auto-update-upgrade/main/install.rsc"
```
```
import install.rsc
```
```
/system/script/run install
```

### Setings script
Change in script BotId, ChatId, Email address

```
:global BotId "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
:global ChatId "xxxxxx";
:global Mail xxxxxxxxxxxxxxx;
```


File: /script.rsc
/system scheduler
add name=WakeUp on-event="/system script run WakeUp " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
add interval=1w name=Update on-event="/system script run Update " policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jan/17/2022 start-time=10:00:00
/system script
add dont-require-permissions=no name=WakeUp policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    delay 120s;\r\
    \n#####\r\
    \n# settings\r\
    \n#####\r\
    \n:local text \"ROUTER WAKE UP\";\r\
    \n:local Tag \"WakeUp\"\r\
    \n/system script run ScriptSetings;\r\
    \n:global BotId;\r\
    \n:global ChatId;\r\
    \n:global wakeup;\r\
    \n:global sendbackup;\r\
    \n:global sendbackupupgrade;\r\
    \n:local Current [/system routerboard get current-firmware];\r\
    \n:local Upgrade [/system routerboard get upgrade-firmware];\r\
    \n/system script run UpdateStat;\r\
    \n:global updatestatus;\r\
    \n/system script run UpgradeStat;\r\
    \n:global upgradestatus;\r\
    \n:local Cheking [/system package update check-for-updates as-value];\r\
    \n:local CurrentVer (\$Cheking -> \"installed-version\");\r\
    \n:local NewVer (\$Cheking -> \"latest-version\");\r\
    \n######\r\
    \n:local sendFunc do={\r\
    \n  /tool fetch url=\"https://api.telegram.org/bot\$BotId/sendMessage\\\?c\
    hat_id=\$ChatId&text=\\\r\
    \n  \$[/system identity get name]\\\r\
    \n  %0a\$[/system routerboard get model]\\\r\
    \n  %0a\$[/system resource get board-name]\\ \r\
    \n  %0a\$text\\\r\
    \n  %0a%23\$Tag\" keep-result=no;\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpdateStat do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n:global updatestatus \\\"no\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpgradeStatNO do={\r\
    \n/system script add name=UpgradeStat source=\"\\\r\
    \n:global upgradestatus \\\"no\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpgradeStatYES do={\r\
    \n/system script add name=UpgradeStat source=\"\\\r\
    \n:global upgradestatus \\\"yes\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n:if ( \$updatestatus = \"yes\" ) do={\r\
    \n :if (\$CurrentVer = \$NewVer) do={  \r\
    \n  :set text \"ROUTER WAKE UP %0aUPDATE OK\"   \r\
    \n  :set Tag \"UPDATE_OK\";\r\
    \n  } else={\r\
    \n   :set text \"ROUTER WAKE UP %0aUPDATE FAILED\"   \r\
    \n   :set Tag \"UPDATE_FAILED\";\r\
    \n   };\r\
    \n   /system script remove UpdateStat;\r\
    \n   \$ADDscriptUpdateStat;\r\
    \n   \$sendFunc text=[\$text] BotId=[\$BotId] ChatId=[\$ChatId] Tag=[\$Tag\
    ]\r\
    \n   :delay 10s;\r\
    \n   :if (\$Current != \$Upgrade) do={\r\
    \n    :if ( \$sendbackupupgrade = \"yes\") do={\r\
    \n\t  :global BackText \"UPGRADE FIRMWARE RUN BACKUP\";\r\
    \n\t  /system script run SendBackup;\r\
    \n\t  :delay 2s;\r\
    \n\t};\r\
    \n   /system script remove UpgradeStat;\r\
    \n   \$ADDscriptUpgradeStatYES;\r\
    \n   /system routerboard upgrade;\r\
    \n   /system reboot;\r\
    \n  }; \r\
    \n} else={\r\
    \n\t:if ( \$upgradestatus = \"yes\" ) do={\r\
    \n\t :if (\$Current != \$Upgrade) do={\r\
    \n\t  :set text \"ROUTER WAKE UP %0aUPGRADE FAILED\"   \r\
    \n      :set Tag \"UPGRADE_FAILED\";\r\
    \n\t } else={\r\
    \n\t  :set text \"ROUTER WAKE UP %0aUPGRADE OK\"   \r\
    \n      :set Tag \"UPGRADE_OK\";\r\
    \n\t  };\r\
    \n\t/system script remove UpgradeStat;\r\
    \n    \$ADDscriptUpgradeStatNO;\r\
    \n\t\$sendFunc text=[\$text] BotId=[\$BotId] ChatId=[\$ChatId] Tag=[\$Tag]\
    \r\
    \n\t} else={\r\
    \n\t:if ( \$wakeup = \"yes\" ) do={\r\
    \n\t\$sendFunc text=[\$text] BotId=[\$BotId] ChatId=[\$ChatId] Tag=[\$Tag]\
    \r\
    \n\t};\t\r\
    \n\t};\r\
    \n};"
add dont-require-permissions=no name=Update policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    ####\r\
    \n# telegram setings \r\
    \n#####\r\
    \n/system script run ScriptSetings;\r\
    \n:global BotId;\r\
    \n:global ChatId;\r\
    \n:global sendbackup;\r\
    \n#####\r\
    \n# router info\r\
    \n#####\r\
    \n:local Tag \"%23UpdateRouterOS\";\r\
    \n:local TagStat;\r\
    \n:local Name [/system identity get name];\r\
    \n:local board [/system resource get board-name];\r\
    \n:local Cheking [/system package update check-for-updates as-value];\r\
    \n:local Stat (\$Cheking -> \"status\");\r\
    \n:local CurrentVer (\$Cheking -> \"installed-version\");\r\
    \n:local NewVer (\$Cheking -> \"latest-version\");\r\
    \n:local Model [/system routerboard get model];\r\
    \n:local CurrentFirmware [/system routerboard get current-firmware];\r\
    \n:local UpgradeFirmware [/system routerboard get upgrade-firmware];\r\
    \n:local Factory  [/system routerboard get factory-firmware];\r\
    \n#####\r\
    \n# send status\r\
    \n#####     \r\
    \n:local sendFunc do={\r\
    \n\t/tool fetch url=\"https://api.telegram.org/bot\$BotId/sendMessage\\\?c\
    hat_id=\$ChatId&text=\\\r\
    \n\t\$Name\\\r\
    \n\t%0a\$Model\\\r\
    \n\t%0a\$board\\\r\
    \n\t%0a\$Stat\\\r\
    \n\t%0aCurrent version=\$CurrentVer\\\r\
    \n\t%0aAvailable version=\$NewVer\\  \r\
    \n\t%0aCurrent firmware=\$CurrentFirmware\\\r\
    \n\t%0aUpgrade firmware=\$UpgradeFirmware\\\r\
    \n\t%0aFactory firmware=\$Factory\\ \r\
    \n\t%0a\$Tag \$TagStat\" keep-result=no;\r\
    \n};\r\
    \n#####\r\
    \n:local ADDscriptUpdateStat do={\r\
    \n/system script add name=UpdateStat source=\"\\\r\
    \n:global updatestatus \\\"yes\\\";\"\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n:if (\"New version is available\" = \$Stat ) do={\r\
    \n\t/system script remove UpdateStat;\r\
    \n\t\$ADDscriptUpdateStat\r\
    \n\t:delay 5s;\r\
    \n\t\$sendFunc ChatId=[\$ChatId] BotId=[\$BotId] Name=[\$Name] Model=[\$Mo\
    del] board=[\$board] Stat=[\$Stat] CurrentVer=[\$CurrentVer] NewVer=[\$New\
    Ver] CurrentFirmware=[\$CurrentFirmware] UpgradeFirmware=[\$UpgradeFirmwar\
    e] Factory=[\$Factory] Tag=[\$Tag] TagStat=\"%23NeedUpdate\"\r\
    \n\t:if ( \$sendbackup = \"yes\") do={\r\
    \n\t:global BackText \"UPDATE PACKAGE RUN BACKUP\";\r\
    \n\t/system script run SendBackup;\r\
    \n\t};\r\
    \n\t:delay 5s;\r\
    \n\t/system package update install;\r\
    \n} else={\r\
    \n\t\$sendFunc ChatId=[\$ChatId] BotId=[\$BotId] Name=[\$Name] Model=[\$Mo\
    del] board=[\$board] Stat=[\$Stat] CurrentVer=[\$CurrentVer] NewVer=[\$New\
    Ver] CurrentFirmware=[\$CurrentFirmware] UpgradeFirmware=[\$UpgradeFirmwar\
    e] Factory=[\$Factory] Tag=[\$Tag] TagStat=\"%23NoNeedUpdate\"\r\
    \n}"
add dont-require-permissions=no name=SendBackup policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    ####\r\
    \n# e-mail setings\r\
    \n#####\r\
    \n/system script run ScriptSetings;\r\
    \n:global Mail;\r\
    \n:global BackText;\r\
    \n#####\r\
    \n:local funDelFile do={\r\
    \n:local tmp [:len [/file/find name=\"\$delname\"]];\r\
    \n:if ( \$tmp > 0 ) do={\r\
    \n:put \"\\n del file \$delname\";\r\
    \n/file remove \$delname;\r\
    \n};\r\
    \n};\r\
    \n#####\r\
    \n# run\r\
    \n#####\r\
    \n/export file=backup;\r\
    \n/system backup save name=backup;\r\
    \n:delay 5s;\r\
    \n/tool e-mail send to=\$Mail \\\r\
    \nsubject=\"BACKUP \$[/system clock get date]\" \\\r\
    \nbody=\"\$[/system identity get name] \\n\$[/system resource get board-na\
    me] \\n\$[/system routerboard get model] \\n\$BackText\"\\\r\
    \nfile=backup.backup,backup.rsc;\r\
    \n:delay 20s;\r\
    \n\$funDelFile delname=\"backup.backup\";\r\
    \n\$funDelFile delname=\"backup.rsc\";"

File: /SendBackup.rsc
#####
# e-mail setings
#####
/system script run ScriptSetings;
:global Mail;
:global BackText;
#####
:local funDelFile do={
:local tmp [:len [/file/find name="$delname"]];
:if ( $tmp > 0 ) do={
:put "\n del file $delname";
/file remove $delname;
};
};
#####
# run
#####
/export file=backup;
/system backup save name=backup;
:delay 5s;
/tool e-mail send to=$Mail \
subject="BACKUP $[/system clock get date]" \
body="$[/system identity get name] \n$[/system resource get board-name] \n$[/system routerboard get model] \n$BackText"\
file=backup.backup,backup.rsc;
:delay 20s;
$funDelFile delname="backup.backup";
$funDelFile delname="backup.rsc";

File: /Update.rsc
#####
# telegram setings 
#####
/system script run ScriptSetings;
:global BotId;
:global ChatId;
:global sendbackup;
#####
# router info
#####
:local Tag "%23UpdateRouterOS";
:local TagStat;
:local Name [/system identity get name];
:local board [/system resource get board-name];
:local Cheking [/system package update check-for-updates as-value];
:local Stat ($Cheking -> "status");
:local CurrentVer ($Cheking -> "installed-version");
:local NewVer ($Cheking -> "latest-version");
:local Model [/system routerboard get model];
:local CurrentFirmware [/system routerboard get current-firmware];
:local UpgradeFirmware [/system routerboard get upgrade-firmware];
:local Factory  [/system routerboard get factory-firmware];
#####
# send status
#####     
:local sendFunc do={
	/tool fetch url="https://api.telegram.org/bot$BotId/sendMessage\?chat_id=$ChatId&text=\
	$Name\
	%0a$Model\
	%0a$board\
	%0a$Stat\
	%0aCurrent version=$CurrentVer\
	%0aAvailable version=$NewVer\  
	%0aCurrent firmware=$CurrentFirmware\
	%0aUpgrade firmware=$UpgradeFirmware\
	%0aFactory firmware=$Factory\ 
	%0a$Tag $TagStat" keep-result=no;
};
#####
:local ADDscriptUpdateStat do={
/system script add name=UpdateStat source="\
:global updatestatus \"yes\";"
};
#####
# run
#####
:if ("New version is available" = $Stat ) do={
	/system script remove UpdateStat;
	$ADDscriptUpdateStat
	:delay 5s;
	$sendFunc ChatId=[$ChatId] BotId=[$BotId] Name=[$Name] Model=[$Model] board=[$board] Stat=[$Stat] CurrentVer=[$CurrentVer] NewVer=[$NewVer] CurrentFirmware=[$CurrentFirmware] UpgradeFirmware=[$UpgradeFirmware] Factory=[$Factory] Tag=[$Tag] TagStat="%23NeedUpdate"
	:if ( $sendbackup = "yes") do={
	:global BackText "UPDATE PACKAGE RUN BACKUP";
	/system script run SendBackup;
	};
	:delay 5s;
	/system package update install;
} else={
	$sendFunc ChatId=[$ChatId] BotId=[$BotId] Name=[$Name] Model=[$Model] board=[$board] Stat=[$Stat] CurrentVer=[$CurrentVer] NewVer=[$NewVer] CurrentFirmware=[$CurrentFirmware] UpgradeFirmware=[$UpgradeFirmware] Factory=[$Factory] Tag=[$Tag] TagStat="%23NoNeedUpdate"
}

File: /WakeUp.rsc
:delay 120s;
#####
# settings
#####
:local text "ROUTER WAKE UP";
:local Tag "WakeUp"
/system script run ScriptSetings;
:global BotId;
:global ChatId;
:global wakeup;
:global sendbackup;
:global sendbackupupgrade;
:local Current [/system routerboard get current-firmware];
:local Upgrade [/system routerboard get upgrade-firmware];
/system script run UpdateStat;
:global updatestatus;
/system script run UpgradeStat;
:global upgradestatus;
:local Cheking [/system package update check-for-updates as-value];
:local CurrentVer ($Cheking -> "installed-version");
:local NewVer ($Cheking -> "latest-version");
######
:local sendFunc do={
  /tool fetch url="https://api.telegram.org/bot$BotId/sendMessage\?chat_id=$ChatId&text=\
  $[/system identity get name]\
  %0a$[/system routerboard get model]\
  %0a$[/system resource get board-name]\ 
  %0a$text\
  %0a%23$Tag" keep-result=no;
};
#####
:local ADDscriptUpdateStat do={
/system script add name=UpdateStat source="\
:global updatestatus \"no\";"
};
#####
:local ADDscriptUpgradeStatNO do={
/system script add name=UpgradeStat source="\
:global upgradestatus \"no\";"
};
#####
:local ADDscriptUpgradeStatYES do={
/system script add name=UpgradeStat source="\
:global upgradestatus \"yes\";"
};
#####
# run
#####
:if ( $updatestatus = "yes" ) do={
 :if ($CurrentVer = $NewVer) do={  
  :set text "ROUTER WAKE UP %0aUPDATE OK"   
  :set Tag "UPDATE_OK";
  } else={
   :set text "ROUTER WAKE UP %0aUPDATE FAILED"   
   :set Tag "UPDATE_FAILED";
   };
   /system script remove UpdateStat;
   $ADDscriptUpdateStat;
   $sendFunc text=[$text] BotId=[$BotId] ChatId=[$ChatId] Tag=[$Tag]
   :delay 10s;
   :if ($Current != $Upgrade) do={
    :if ( $sendbackupupgrade = "yes") do={
	  :global BackText "UPGRADE FIRMWARE RUN BACKUP";
	  /system script run SendBackup;
	  :delay 2s;
	};
   /system script remove UpgradeStat;
   $ADDscriptUpgradeStatYES;
   /system routerboard upgrade;
   /system reboot;
  }; 
} else={
	:if ( $upgradestatus = "yes" ) do={
	 :if ($Current != $Upgrade) do={
	  :set text "ROUTER WAKE UP %0aUPGRADE FAILED"   
      :set Tag "UPGRADE_FAILED";
	 } else={
	  :set text "ROUTER WAKE UP %0aUPGRADE OK"   
      :set Tag "UPGRADE_OK";
	  };
	/system script remove UpgradeStat;
    $ADDscriptUpgradeStatNO;
	$sendFunc text=[$text] BotId=[$BotId] ChatId=[$ChatId] Tag=[$Tag]
	} else={
	:if ( $wakeup = "yes" ) do={
	$sendFunc text=[$text] BotId=[$BotId] ChatId=[$ChatId] Tag=[$Tag]
	};	
	};
};


