# Repository Information
Name: mikrotik

# Directory Structure
Directory structure:
└── github_repos/mikrotik/
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
    │   │       ├── pack-dc26311021309ead045d5be3799a6f702b97e8d3.idx
    │   │       └── pack-dc26311021309ead045d5be3799a6f702b97e8d3.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── auto-upgrade.rsc
    ├── backup-config.rsc
    ├── dhcp-notify-slack.rsc
    ├── failover_without_scripts.src.rsc
    ├── message-to-slack.rsc
    ├── README.md
    └── TODO.md


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
	url = https://github.com/massimo-filippi/mikrotik.git
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
0000000000000000000000000000000000000000 546a40c31ade11255259585cd8b53429e32bd794 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/massimo-filippi/mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 546a40c31ade11255259585cd8b53429e32bd794 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/massimo-filippi/mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 546a40c31ade11255259585cd8b53429e32bd794 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/massimo-filippi/mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
546a40c31ade11255259585cd8b53429e32bd794 refs/remotes/origin/master


File: /.git\refs\heads\master
546a40c31ade11255259585cd8b53429e32bd794


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/work


File: /auto-upgrade.rsc
##
##   Automatically upgrade RouterOS and Firmware
##   https://github.com/massimo-filippi/mikrotik
##
##   script by Maxim Krusina, maxim@mfcc.cz
##   based on: http://wiki.mikrotik.com/wiki/Manual:Upgrading_RouterOS
##   created: 2014-12-05
##   updated: 2019-01-26
##   tested on: RouterOS 6.43.8 / multiple HW devices
##


########## Set variables

## Update channel can take values before 6.43.8: bugfix    | current | development | release-candidate
## Update channel can take values after  6.43.8: long-term | stable  | development | testing
:local updChannel       "stable"

## Notify via Slack
:local notifyViaSlack   true
:global SlackChannel    "#log"

## Notify via E-mail
:local notifyViaMail    true
:local email            "your@email.com"


########## Upgrade firmware

## Let's check for updated firmware

:local rebootRequired false
/system routerboard

:if ( [get current-firmware] != [get upgrade-firmware]) do={

   ## New version of firmware available, let's upgrade

   ## Notify via Log
   :log info ("Upgrading firmware on router $[/system identity get name] from $[/system routerboard get current-firmware] to $[/system routerboard get upgrade-firmware]")

   ## Notify via Slack
   :if ($notifyViaSlack) do={
       :global SlackMessage "Upgrading firmware on router *$[/system identity get name]* from $[/system routerboard get current-firmware] to *$[/system routerboard get upgrade-firmware]*";
       :global SlackMessageAttachements  "";
       /system script run "Message To Slack";
   }

   ## Notify via E-mail
   :if ($notifyViaMail) do={
       /tool e-mail send to="$email" subject="Upgrading firmware on router $[/system identity get name]" body="Upgrading firmware on router $[/system identity get name] from $[/system routerboard get current-firmware] to $[/system routerboard get upgrade-firmware]"
   }

   ## Upgrade (it will no reboot, we'll do it later)
   upgrade
   :set rebootRequired true

}


########## Upgrade RouterOS

## Check for update
/system package update
set channel=$updChannel
check-for-updates

## Wait on slow connections
:delay 15s;

## Important note: "installed-version" was "current-version" on older Roter OSes
:if ([get installed-version] != [get latest-version]) do={

   ## Notify via Log
   :log info ("Upgrading RouterOS on router $[/system identity get name] from $[/system package update get installed-version] to $[/system package update get latest-version] (channel:$[/system package update get channel])")

   ## Notify via Slack
   :if ($notifyViaSlack) do={
       :global SlackMessage "Upgrading RouterOS on router *$[/system identity get name]* from $[/system package update get installed-version] to *$[/system package update get latest-version] (channel:$[/system package update get channel])*";
       :global SlackMessageAttachements  "";
       /system script run "Message To Slack";
   }

   ## Notify via E-mail
   :if ($notifyViaMail) do={
       /tool e-mail send to="$email" subject="Upgrading RouterOS on router $[/system identity get name]" body="Upgrading RouterOS on router $[/system identity get name] from $[/system package update get installed-version] to $[/system package update get latest-version] (channel:$[/system package update get channel])"
   }

   ## Wait for mail to be sent & upgrade
   :delay 15s;
   install

} else={

    :if ($rebootRequired) do={
        # Firmware was upgraded, but not RouterOS, so we need to reboot to finish firmware upgrade

        ## Notify via Slack
        :if ($notifyViaSlack) do={
            :global SlackMessage "Rebooting...";
            :global SlackMessageAttachements  "";
            /system script run "Message To Slack";
        }

        /system reboot

    } else={

        # No firmware nor RouterOS upgrade available, nothing to do, just log info
        :log info ("No firmware nor RouterOS upgrade found.")

        ## Notify via Slack
        :if ($notifyViaSlack) do={
            :global SlackMessage "No firmware nor RouterOS upgrade found.";
            :global SlackMessageAttachements  "";
            /system script run "Message To Slack";
        }
    }
}


File: /backup-config.rsc
##
##   Automatically backup router's config and upload it to FTP server(s)
##   https://github.com/massimo-filippi/mikrotik
##
##   script by Maxim Krusina, maxim@mfcc.cz
##   created: 2014-03-09
##   updated: 2019-01-26
##   tested on: RouterOS 6.43.8 / multiple HW devices
##


########## Set variables

## Base filename
:local filename         "daily-backup-myroutername"

## FTP server 1 for upload
:local ftp1Address      "ftp-1-hostname"
:local ftp1User         "ftp-1-username"
:local ftp1Password     "ftp-1-password"
:local ftp1Path         "ftp-1-path"

## FTP server 2 for upload - if second server is not used, just comment lines bellow
:local ftp2Address      "ftp-2-hostname"
:local ftp2User         "ftp-2-username"
:local ftp2Password     "ftp-2-password"
:local ftp2Path         "ftp-2-path"

## Log to Slack
:local notifyViaSlack   true
:global SlackChannel    "#log"


########## Message to Slack

:if ($notifyViaSlack) do={
    :global SlackMessage "Creating configuration backup on router *$[/system identity get name]*";
    :global SlackMessageAttachements  "";
    /system script run "Message To Slack";
}


########## Do the stuff

## Get currrent RouterOS version
:local myVer [/system package update get installed-version];

## Append version number to filename (to not overwrite backups from older RouterOS versions)
:set filename ($filename . "-" . $myVer);

## Backup & Export config to local file
/system backup save name="$filename"
/export file="$filename"

## Upload to .backup to FTP 1
/tool fetch address=$ftp1Address src-path="$filename.backup" user=$ftp1User  mode=ftp password=$ftp1Password dst-path=($ftp1Path . $filename . ".backup") upload=yes port=21

## Upload to .rsc to FTP 1
/tool fetch address=$ftp1Address src-path="$filename.rsc" user=$ftp1User  mode=ftp password=$ftp1Password dst-path=($ftp1Path . $filename . ".rsc") upload=yes port=21


########## Message to Slack

:if ($notifyViaSlack) do={
    :global SlackMessage "Backup upload to FTP *$ftp1Address*";
    :global SlackMessageAttachements  "";
    /system script run "Message To Slack";
}


########## Upload to secondary FTP

:if ([:len $ftp2Address] != 0)  do={

    ## Upload to .backup to FTP 2
    /tool fetch address=$ftp2Address src-path="$filename.backup" user=$ftp2User  mode=ftp password=$ftp2Password dst-path=($ftp2Path . $filename . ".backup") upload=yes port=21

    ## Upload to .rsc to FTP 2
    /tool fetch address=$ftp2Address src-path="$filename.rsc" user=$ftp2User  mode=ftp password=$ftp2Password dst-path=($ftp2Path . $filename . ".rsc") upload=yes port=21

    :if ($notifyViaSlack) do={
        :global SlackMessage "Backup upload to FTP *$ftp2Address*";
        :global SlackMessageAttachements  "";
        /system script run "Message To Slack";
    }
}


## Log
:log info ("Configuration backup created on router $[/system identity get name].")


########## Message to Slack

:if ($notifyViaSlack) do={
    :global SlackMessage "Configuration backup on router *$[/system identity get name]* done";
    :global SlackMessageAttachements  "";
    /system script run "Message To Slack";
}


File: /dhcp-notify-slack.rsc
##
##   Send a message to Slack on DHCP Bound
##   https://github.com/massimo-filippi/mikrotik
##
##   script by Maxim Krusina, maxim@mfcc.cz
##   based on: http://jeremyhall.com.au/mikrotik-routeros-slack-messaging-hack/
##   created: 2018-09-23
##   updated: 2018-09-23
##
##  usage:
##  use this script as DHCP Lease Script
##


:global leaseBound
:global leaseServerName
:global leaseActMAC
:global leaseActIP


# Do the stuff on Bind

:if ($leaseBound = 1) do={
  /ip dhcp-server lease {
    :foreach i in [find dynamic address=$leaseActIP] do={

      :local hostName [/ip dhcp-server lease get $i host-name];

      :global SlackChannel "#my-channel"
      :global SlackMessage "New guest connected to *My wifi name*"
      :global SlackMessageAttachements "[{\"fields\": [{\"title\": \"Host name\",\"value\": \"$hostName\",\"short\": false},{\"title\": \"IP\",\"value\": \"$leaseActIP\",\"short\": false},{\"title\": \"MAC\",\"value\": \"$leaseActMAC\",\"short\": false}],\"color\": \"#F35A00\",\"mrkdwn_in\":[\"text\",\"pretext\"]}]";

      /system script run "Message To Slack";

    }
  }
}


File: /failover_without_scripts.src.rsc
#####################################################################
#                                                                   #
#                   Failover Withouth Scripts                       #
#                                                                   #
#####################################################################
#                      Global Vars                                  #
# Gateway ISP 1 and 2
:global Gateway1 "192.168.0.1"
:global Gateway2 "11.11.11.1"
# Host 1 (Any IP, Used OpenDNS)
:global Host1 "208.67.222.222"
# Host 1 (Any IP, Used OpenDNS)
:global Host2 "208.67.220.220"
## Show Message
:global Msg "Ok"
#####################################################################
/ip route
add dst-address=0.0.0.0/0 gateway=$Gateway1 distance=1 \
check-gateway=ping
add dst-address=0.0.0.0/0 gateway=$Gateway2 distance=2

/ip route
add dst-address=$Host1 gateway=$Gateway1 scope=10
add dst-address=$Host2 gateway=$Gateway2 scope=10

/ip route
add distance=1 gateway=$Host1 routing-mark=ISP1 check-gateway=ping
add distance=2 gateway=$Host2 routing-mark=ISP1 check-gateway=ping

/ip route
add distance=1 gateway=$Host1 routing-mark=ISP2 check-gateway=ping
add distance=2 gateway=$Host2 routing-mark=ISP2 check-gateway=ping

/ip route
add dst-address=$Host1 type=blackhole distance=20
add dst-address=$Host2 type=blackhole distance=20


File: /message-to-slack.rsc
##
##   Send message to Slack
##   https://github.com/massimo-filippi/mikrotik
##
##   script by Maxim Krusina, maxim@mfcc.cz
##   based on: http://jeremyhall.com.au/mikrotik-routeros-slack-messaging-hack/
##   created: 2017-08-21
##   updated: 2018-09-22
##
##  usage:
##  in another script, first setup global variable then call this script:
##
##  :global SlackMessage "my message"
##  :global SlackChannel "#my-channel"
##  :global SlackMessageAttachements "url encoded attachements or empty string for none"
##  /system script run MessageToSlack;
##
##  PS: unfortunately, right now there is no better way to pass script parameters than via global variables
##


:global SlackChannel;
:global SlackMessage;
:global SlackMessageAttachements;

:local botname [/system identity get name];
:local token "xoxp-your-token-here"
:local iconurl https://s3-us-west-2.amazonaws.com/slack-files2/avatars/2015-12-08/16227284950_0c4cfc4b66e68c6273ad_48.jpg


## Replace ASCII characters with URL encoded characters
## Call this function:  $urlEncode "string to encode"

:global urlEncode do={

  :local string $1;
  :local stringEncoded "";

  :for i from=0 to=([:len $string] - 1) do={
    :local char [:pick $string $i]
    :if ($char = " ")  do={ :set $char "%20" }
    :if ($char = "\"") do={ :set $char "%22" }
    :if ($char = "#")  do={ :set $char "%23" }
    :if ($char = "\$") do={ :set $char "%24" }
    :if ($char = "%")  do={ :set $char "%25" }
    :if ($char = "&")  do={ :set $char "%26" }
    :if ($char = "+")  do={ :set $char "%2B" }
    :if ($char = ",")  do={ :set $char "%2C" }
    :if ($char = "-")  do={ :set $char "%2D" }
    :if ($char = ":")  do={ :set $char "%3A" }
    :if ($char = "[")  do={ :set $char "%5B" }
    :if ($char = "]")  do={ :set $char "%5D" }
    :if ($char = "{")  do={ :set $char "%7B" }
    :if ($char = "}")  do={ :set $char "%7D" }
    :set stringEncoded ($stringEncoded . $char)
  }
  :return $stringEncoded;
}

:local channel [$urlEncode $SlackChannel];
:local message [$urlEncode $SlackMessage];
:local attachements [$urlEncode $SlackMessageAttachements];


## Send the message to Slack

/tool fetch url="https://slack.com/api/chat.postMessage?token=$token&channel=$channel&text=$message&icon_url=$iconurl&as_user=false&username=$botname&attachments=$SlackMessageAttachements";


File: /README.md
# MikrtoTik / RouterOS Scripts



## auto-upgrade.rsc

This script is for automatic upgrading of MikroTik routers.
In our environment, I have one MikroTik (at my home) scheduled to upgrade every night,
and all other routers scheduled to upgrade once per week. This is useful to catch possible
troubles on one router and not on all routers at the same time.

Auto-upgrade script will look for a new release in current-channel (production releases),
if there is a new version available, it upgrade itself. When there is no new Router OS available,
it checks for a new firmware - when available, it upgrades firmware.

### Installation

Using Winbox / Web admin (if you are familiar with command line, you already know how to do it :)
- Go to *System / Scripts, Add new*
- Name it, ie. "Auto Upgrade", select required policies (if you are lazy like me, select all boxes)
- Paste source code to *Source* field
- Replace :local email "your@email.com" with your own e-mail
- Save script
- Check, if your MikroTik is configured to send e-mail correctly
- Go to *System / Scheduler, Add New*
- Schedule script regarding your needs. *OnEvent* field should be something like this: */system script run "Auto Upgrade"*



## backup-config.rsc

This script backups your MikroTik's configuration and uploads it to FTP server (or optionally to two FTP servers).
Backup is saved in two different file formats:
- .backup is binary format, useful for restoring config to same hardware (model).
- .rsc is plain text format, useful for editing and possible restoring to a different MikroTik hardware.
Version number is attached to all files, so you always have latest backup from each RouterOS version.
This is very useful when you need to downgrade Router OS for some reason - you have latest working backup for each Router OS version.

### Installation

Using Winbox / Web admin (if you are familiar with command line, you already know how to do it :)
- Go to *System / Scripts, Add new*
- Name it, ie. "Backup Config", select required policies (if you are lazy like me, select all boxes)
- Paste source code to *Source* field
- Edit variables in section *Set variables* regarding your needs
- Save script
- Go to *System / Scheduler, Add New*
- Schedule script regarding your needs. *OnEvent* field should be something like this: */system script run "Backup Config"*
- Test it, your backup files should appear on your FTP(s) servers

Warning: FTP protocol is not encrypted, so all information is transmitted unencrypted! I don't care in my case,
because all data are pushed thru encrypted VPN channels, but the security can be improved here!



## message-to-slack.rsc

This script allow to send messages from RouterOS to Slack channel.
There is no way how to call webhooks from RouterOS, so it uses workaround using /tool fetch command.

### Installation

Slack
- Generate your API token here: https://api.slack.com/docs/oauth-test-tokens
- More information here: http://jeremyhall.com.au/mikrotik-routeros-slack-messaging-hack/

Using Winbox / Web admin (if you are familiar with command line, you already know how to do it :)
- Go to *System / Scripts, Add new*
- Name it, ie. "Message To Slack", select required policies (if you are lazy like me, select all boxes)
- Paste source code to *Source* field
- Edit variables *botname* and *token* in section *Set variables* regarding your needs
- Save script
- Call it from another scripts using:
```
:global SlackMessage "my message"
:global SlackChannel "my-channel"
/system script run "Message To Slack";
```



## dhcp-notify-slack.rsc

This script will send Slack message each time someone (or something) will get lease from your specific DHCP server - like when guest connects to Guests WiFi.

### Installation

Slack
- Generate your API token here: https://api.slack.com/docs/oauth-test-tokens
- More information here: http://jeremyhall.com.au/mikrotik-routeros-slack-messaging-hack/

Using Winbox / Web admin (if you are familiar with command line, you already know how to do it :)
- If not already done, install the *message-to-slack.rsc* script from this repository
- Go to *IP / DHCP Server*
- Click on DHCP server where you want notifications
- Paste source code to *Lease Script* field
- Edit variables *SlackChannel* and *SlackMessage* regarding your needs
- Save settings



Nice MikroTik'ing
Maxim Krušina, Massimo Filippi, s.r.o.
maxim@mfcc.cz


File: /TODO.md
ToDo
====

- Send messages to Slack via POST + JSON (not possible now because there is no support for sending auth headers with /fetch)


