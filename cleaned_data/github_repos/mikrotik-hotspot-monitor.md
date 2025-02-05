# Repository Information
Name: mikrotik-hotspot-monitor

# Directory Structure
Directory structure:
└── github_repos/mikrotik-hotspot-monitor/
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
    │   │       ├── pack-a4d772f1db3378ffa8680b8f1f1eb248cad7dd99.idx
    │   │       └── pack-a4d772f1db3378ffa8680b8f1f1eb248cad7dd99.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── LICENSE
    ├── mikhmon/
    │   ├── app/
    │   │   ├── config.php
    │   │   ├── conntest.php
    │   │   ├── css/
    │   │   │   ├── fonts/
    │   │   │   │   ├── material.woff2
    │   │   │   │   └── Roboto-Regular.woff
    │   │   │   ├── index.php
    │   │   │   ├── style.css
    │   │   │   └── vcolors.php
    │   │   ├── dnsstaticadd.php
    │   │   ├── dnsstaticrm.php
    │   │   ├── genkv.php
    │   │   ├── genkvs.php
    │   │   ├── genupm.php
    │   │   ├── history.php
    │   │   ├── hotspotlog.php
    │   │   ├── img/
    │   │   │   └── index.php
    │   │   ├── index.php
    │   │   ├── lib/
    │   │   │   ├── api.php
    │   │   │   └── index.php
    │   │   ├── login.php
    │   │   ├── logout.php
    │   │   ├── otaupdate.php
    │   │   ├── penjualan.php
    │   │   ├── reboot.php
    │   │   ├── resetcolor.php
    │   │   ├── resetconfig.php
    │   │   ├── setup.php
    │   │   ├── uprofileadd.php
    │   │   ├── userlist.php
    │   │   ├── vcolorconf.php
    │   │   └── vouchers/
    │   │       ├── index.php
    │   │       ├── printkvs.php
    │   │       ├── printkvsqr.php
    │   │       ├── printvs.php
    │   │       └── printvsqr.php
    │   ├── index.php
    │   ├── install/
    │   │   ├── mikhmon-server
    │   │   └── mikhmon.desktop
    │   └── status/
    │       ├── api.php
    │       ├── config.php
    │       └── index.php
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
	url = https://github.com/laksa19/mikrotik-hotspot-monitor.git
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
0000000000000000000000000000000000000000 5aba990609ab16482c2b6482a3d18fe6ca74cd47 vivek-dodia <vivek.dodia@icloud.com> 1738605962 -0500	clone: from https://github.com/laksa19/mikrotik-hotspot-monitor.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5aba990609ab16482c2b6482a3d18fe6ca74cd47 vivek-dodia <vivek.dodia@icloud.com> 1738605962 -0500	clone: from https://github.com/laksa19/mikrotik-hotspot-monitor.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5aba990609ab16482c2b6482a3d18fe6ca74cd47 vivek-dodia <vivek.dodia@icloud.com> 1738605962 -0500	clone: from https://github.com/laksa19/mikrotik-hotspot-monitor.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5aba990609ab16482c2b6482a3d18fe6ca74cd47 refs/remotes/origin/master


File: /.git\refs\heads\master
5aba990609ab16482c2b6482a3d18fe6ca74cd47


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.


File: /mikhmon\app\config.php
<?php $iphost=""; $userhost=""; $passwdhost=""; $useradm="admin"; $passadm="1234"; $reloadindex="15"; $profile1="Voucher3Jam"; $profile2="Voucher1Hari"; $profile3="Voucher2Hari"; $profile4="Voucher7Hari"; $profile5="Voucher30Hari"; $profile6=""; $profile7=""; $profile8=""; $profile9=""; $profile10=""; $profile11=""; $profile12=""; $profile13=""; $profile14=""; $profile15=""; $uactive1="3h"; $uactive2="1d"; $uactive3="2d"; $uactive4="7d"; $uactive5="30d"; $uactive6=""; $uactive7=""; $uactive8=""; $uactive9=""; $uactive10=""; $uactive11=""; $uactive12=""; $uactive13=""; $uactive14=""; $uactive15=""; $vname1="3Jam"; $vname2="1Hari"; $vname3="2Hari"; $vname4="7Hari"; $vname5="30Hari"; $vname6=""; $vname7=""; $vname8=""; $vname9=""; $vname10="";  $vname11=""; $vname12=""; $vname13=""; $vname14=""; $vname15=""; $utimelimit1="1h"; $utimelimit2="2h"; $utimelimit3="5h"; $utimelimit4="10h"; $utimelimit5="12h"; $utimelimit6=""; $utimelimit7="";  $utimelimit8=""; $utimelimit9=""; $utimelimit10=""; $utimelimit1t="1Jam"; $utimelimit2t="2Jam"; $utimelimit3t="5Jam"; $utimelimit4t="10Jam"; $utimelimit5t="12Jam"; $utimelimit6t=""; $utimelimit7t=""; $utimelimit8t=""; $utimelimit9t=""; $utimelimit10t=""; $ubytelimit1="500000000"; $ubytelimit2="1000000000"; $ubytelimit3="2000000000"; $ubytelimit4="5000000000"; $ubytelimit5="10000000000"; $ubytelimit6=""; $ubytelimit7="";  $ubytelimit8=""; $ubytelimit9=""; $ubytelimit10=""; $ubytelimit1t="500MB"; $ubytelimit2t="1GB"; $ubytelimit3t="2GB"; $ubytelimit4t="5GB"; $ubytelimit5t="10GB"; $ubytelimit6t=""; $ubytelimit7t=""; $ubytelimit8t=""; $ubytelimit9t=""; $ubytelimit10t=""; $price1="Rp1.000"; $price2="Rp3.000"; $price3="Rp5.000"; $price4="Rp15.000"; $price5="Rp35.000"; $price6=""; $price7=""; $price8=""; $price9=""; $price10="";  $price11=""; $price12=""; $price13=""; $price14=""; $price15=""; $headerv="Kemangi 41"; $notev="k41.net"; ?>


File: /mikhmon\app\conntest.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$ARRAY = $API->comm("/system/resource/print");
	$ARRAY1 = $API->comm("/system/routerboard/print");
	$ARRAY2 = $API->comm("/system/identity/print");
    $API->disconnect();
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="refresh" content="" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
				</tr>
				<tr>
					<td>Tes Koneksi ke Mikrotik</td>
					<td>
						<button class="material-icons" onclick="Reload()"	title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./setup.php';" 	title="Edit Config">settings</button>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
					</td>
				</tr>
			</table>
			<table class="tnav" >
				<tr>
					<td>
							<?php
								$cek = ($ARRAY[0]['platform']);
								if ($cek == ""){
									 ?><meta http-equiv="refresh" content="0; url=setup.php"><?php
								}
										$regtable = $ARRAY2[0];echo "Identity <td>:</td><td>" . $regtable['name'] . "<br />";echo "</td><tr><td>";
										$regtable = $ARRAY[0];echo "Platform <td>:</td><td>" . $regtable['platform'] . "<br />";echo "</td><tr><td>";
										$regtable = $ARRAY[0];echo "Board Name <td>:</td><td>" . $regtable['board-name'] . "<br />";echo "</td></tr><td>";
										$regtable = $ARRAY1[0];echo "Model <td>:</td><td>" . $regtable['model'] . "<br />";echo "</td><tr><td>";
										$regtable = $ARRAY[0];echo "Version <td>:</td><td>" . $regtable['version'] . "<br />";echo "</td></tr><td>";
										$regtable = $ARRAY[0];echo "CPU Load<td>:</td><td>" . $regtable['cpu-load'] . "%<br />";echo "</td></tr><td>";
										$regtable = $ARRAY[0];echo "Free Memory <td>:</td><td>" . formatBytes2($regtable['free-memory'],0) . "<br />";echo "</td></tr><td>";
										$regtable = $ARRAY[0];echo "Free HDD Space <td>:</td><td>" . formatBytes2($regtable['free-hdd-space'],0) . "<br />";echo "</td>";
							?>
				</tr>
			</table>
		</div>
	</body>
<?php

function formatBytes($bytes, $precision = 2) {
$units = array('B', 'KB', 'MB', 'GB', 'TB');

$bytes = max($bytes, 0);
$pow = floor(($bytes ? log($bytes) : 0) / log(1024));
$pow = min($pow, count($units) - 1);

// Uncomment one of the following alternatives
// $bytes /= pow(1024, $pow);
// $bytes /= (1 << (10 * $pow));

return round($bytes, $precision) . ' ' . $units[$pow];
}

function formatBytes2($size, $decimals = 0){
$unit = array(
'0' => 'Byte',
'1' => 'KiB',
'2' => 'MiB',
'3' => 'GiB',
'4' => 'TiB',
'5' => 'PiB',
'6' => 'EiB',
'7' => 'ZiB',
'8' => 'YiB'
);

for($i = 0; $size >= 1024 && $i <= count($unit); $i++){
$size = $size/1024;
}

return round($size, $decimals).' '.$unit[$i];
}

?>
</html>



File: /mikhmon\app\css\index.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
echo "<meta http-equiv='refresh' content='0;url=../' />";
?>



File: /mikhmon\app\css\style.css

@font-face {
  font-family: 'Material Icons';
  font-style: normal;
  font-weight: 400;
  src: url(fonts/material.woff2) format('woff2');
}
@font-face {
  font-family: Roboto;
  src: url('fonts/Roboto-Regular.woff');
  font-weight: normal;
  font-style: normal;
}
.material-icons {
  font-family: 'Material Icons';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -moz-font-feature-settings: 'liga';
  -moz-osx-font-smoothing: grayscale;
  background-color: #008CCA;
  border: none;
  padding: 2px 2px;
  color: white;
  display: inline-block;
  cursor: pointer;
  margin: 2px 2px;
  border-radius: 5px;
  float: right;
}

body {
  background: url('../img/textures.png');
  background-color: #3D4241;
  font-family: Roboto;
  font-size: 14px;
}

.main {
  background-color: #FFFFFF;
  border: 1px solid #3D4241;
  border-radius: 5px;
  padding-top: 5px;
  padding-right: 5px;
  padding-bottom: 5px;
  padding-left: 5px;
  width:750px;
  height: 100%;
  margin-top:auto;
  margin-bottom:auto;
  margin-left:auto;
  margin-right:auto;
}

#login {
  background-color: #FFFFFF;
  border: 1px solid #3D4241;
  border-radius: 5px;
  width:300px;
  height: 100%;
  margin-top:5%;
  margin-left:auto;
  margin-right:auto;
}

/* Zebra striping */
table.zebra{
  margin-left:auto;
  margin-right:auto;
  width: 100%;
  border-collapse: collapse;
}
table.zebra tr:nth-of-type(odd) {
  background: #f1f1f1;
}
table.zebra th {
  background: #008CCA;
  color: white;
  font-weight: bold;
}
table.zebra td, th {
  padding: 2px;
  border: 1px solid #ccc;
  text-align: left;
}

table.tprint {
  margin-left:auto;
  margin-right:auto;
  width: 100%;
  border-collapse: collapse;
}
table.tprint th {
  background: #008CCA;
  color: white;
  font-weight: bold;
}
table.tprint td, th {
  padding: 3px;
  border: 1px solid #ccc;
  text-align: left;
}

table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 100%;
  border-collapse: collapse;
}
table.tprinta th {
  background: #008CCA;
  color: white;
  font-weight: bold;
  text-align: center;
  padding: 3px;
}
table.tprinta td {
  padding: 3px;
  border: 1px solid #ccc;
  text-align: center;
}

table.tnav {
  margin-left:auto;
  margin-right:auto;
  width: 100%;
  border-collapse: collapse;
}
table.tnav td {
  padding: 3px;
  border: 0px;
  text-align: left;
  font-weight: bold;
}

.btnsubmit {
  background-color: #008CCA;
  border: none;
  padding: 5px 5px;
  color: white;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  cursor: pointer;
  margin: 2px 2px;
  border-radius: 5px;
  float: left;
}

textarea,input,select {
  background-color: #FDFBFB;
  border: 1px solid #008CCA;
  padding: 2px;
  margin: 2px;
  font-size: 12px;
  color: #808080;
  outline: none;
}

/* Style the tab */
div.tab {
  overflow: hidden;
  width: 100%;
  margin-top:7px;
  margin-left:auto;
  margin-right:auto;
  height: 100%;
  background-color: #008CCA;
  border: 1px solid #ccc;
}

/* Style the buttons inside the tab */
div.tab button {
  background-color: #008CCA;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 5px 5px;
  transition: 0.5s;
  font-size: 14px;
  font-weight: bold;
  color:#000000;
  width:50%;
}

div.tab button:hover {
  background-color: #F1F1F1;
  color: #000000;
}

div.tab button.active {
  background-color: #008CCA;
  color: #FFFFFF;
}

.tabcontent {
  display: none;
  padding: 0px 0px;
  border-top: none;
}

.dropbtn {
    background-color: #008CCA;
    color: white;
    padding: 2px;
    font-size: px;
    border: none;
    cursor: pointer;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    right: 0;
    background-color: #008CCA;
    min-width: 140px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 5px 5px;
    text-decoration: none;
    display: block;
}


.dropdown-content a:hover {background-color: #3D4241}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #008CCA;
}

@media only screen and (max-width:450px) {
  /* For mobile phones: */
  .main  {
    width:330px;
  }
}

a:link {
  color: #FFFFFF;
}
a:visited {
  color: #FFFFFF;
}
a:hover {
  color: #FFFFFF;
}
a:active {
  color: #FFFFFF;
}

.modal-window {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.15);
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 999;
  opacity: 0;
  pointer-events: none;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
}

.modal-window:target {
  opacity: 1;
  pointer-events: auto;
}

.modal-window>div {
  width: 300px;
  position: relative;
  margin: 10% auto;
  padding: 1rem;
  background: #3D4241;
  color: #FFFFFF;
}

.modal-window header {
  font-weight: bold;
}

.modal-close {
  color: #ffffff;
  line-height: 25px;
  position: absolute;
  right: 0;
  text-align: center;
  top: 0;
  width: 50px;
  text-decoration: none;
  background-color: red;
}

.modal-window h1 {
  font-size: 150%;
  margin: 0 0 15px;
}


File: /mikhmon\app\css\vcolors.php
<?php $header=""; $note=""; $userpass=""; $details=""; $price=""; $font1=""; $font2=""; $font3=""; $font4=""; $font5=""; ?>


File: /mikhmon\app\dnsstaticadd.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/dns/static/print', false);
	$API->write('?=address=127.0.0.1');
	$ARRAY = $API->read();

	$API->disconnect();
}
?>
<?php
	if(isset($_POST['name'])){
			
			$dnsname = ($_POST['name']);

			if ($API->connect($iphost, $userhost, $passwdhost)) {
			}
			$API->comm("/ip/dns/static/add", array(
					  "name" => "$dnsname",
					  "address" => "127.0.0.1",
			));
			
			header('Location: dnsstaticadd.php');
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
	<div class="main">
	<table class="tnav">
		<tr>
			<td style="text-align: center;" colspan=2>Daftar DNS Static</td>
		</tr>
		<tr>
			<td>
				<button class="material-icons" onclick="Reload()" title="Reload">autorenew</button>
				<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
				<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
			</td>
		</tr>
	</table>
		<form autocomplete="off" method="post" action="">
				<table class="tnav" align="center"  >
				<!--<tr><td>ID</td><td><td>:</td><input type="text" size="20" maxlength="20" name="id" required="1"/></td></tr>-->
				<tr><td>DNS Name</td><td>:</td><td><input type="text" size="20"  name="name" placeholder="DNS name" required="1"/></td></tr>
				<tr><td></td><td></td><td><input type="submit" class="btnsubmit" value="Add"/></td></tr>
			</table>
		</form>

		<div style="overflow-x:auto;">
			<table style="white-space: nowrap;" class="zebra" >
				<tr>
				  <th style='text-align:center;'>X</th>
					<th >Name</th>
				</tr>
				<?php
					$TotalReg = count($ARRAY);

						for ($i=0; $i<$TotalReg; $i++){
						  echo "<tr>";
						  $regtable = $ARRAY[$i];echo "<td style='text-align:center;'><a style='color:#000;' href=dnsstaticrm.php?id=".$regtable['.id'] . ">X</a></td>";
							$regtable = $ARRAY[$i];echo "<td>" . $regtable['name'];echo "</td>";
							echo"</tr>";
							}
					?>
			</table>
		</div>
	</div>
	</body>
</html>


File: /mikhmon\app\dnsstaticrm.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;

$id = $_GET['id'];

if ($API->connect( $iphost, $userhost, $passwdhost )) {

$API->comm("/ip/dns/static/remove", array(
".id"=> "$id",));

$API->disconnect();

header("Location:./dnsstaticadd.php");

}
?>

File: /mikhmon\app\genkv.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$srvlist = $API->comm("/ip/hotspot/print");
	$API->disconnect();
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Generate Voucher</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<style>
table.tusera {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tusera td {
  padding: 4px;
  border: 2px solid #000000;
  font-size: 14px;
  text-align: left;
  font-weight: bold;
}
table.tuserb {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tuserb td {
  padding-left: 20px;
  padding-top: 17px;
  padding-bottom: 20px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}

table.tuserc {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tuserc td {
  padding: 4px;
  border: 2px solid #000000;
  font-size: 14px;
  text-align: left;
  font-weight: bold;
}
table.tuserd {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tuserd td {
  padding-left: 20px;
  border: 0px;
  font-size: 16px;
  text-align: left;
}
		</style>
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Generate 1 Voucher</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="location.href='genkv.php';" title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./uprofileadd.php';"	title="User Profile">local_library</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">find_in_page</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">User by profile</a>
									<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}
								?>
								</div>
						</div>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
					</td>
				</tr>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tnav" align="center"  >
					<tr><td>Jenis Voucher</td><td>:</td><td>
						<select name="genall" required="1">
							<option value="">Pilih...</option>
							<option value="kv">Kode Voucher</option>
							<option value="up">User Password</option>
						</select>
						</td>
					</tr>
					<tr><td>Server Hotspot</td><td>:</td><td>
						<select name="server" required="1">
							<option value="all">all</option>
							
							<?php
							$TotalReg = count($srvlist);

							for ($i=0; $i<$TotalReg; $i++){
							$regtable = $srvlist[$i];echo "<option>" . $regtable['name'];echo "</option>";
							}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Panjang Username</td><td>:</td><td>
						<select name="pjguser" required="1">
							<option value="">Pilih...</option>
							<option>3</option>
							<option>4</option>
							<option>5</option>
							<option>6</option>
						</select>
						</td>
					</tr>
					<tr><td>Huruf</td><td>:</td><td>
						<select name="huruf" required="1">
							<option value="lower">abcd</option>
							<option Value="upper">ABCD</option>
							<option Value="upplow">aBcD</option>
						</select>
						</td>
					</tr>
					<tr><td>Profile | Masa Aktif</td><td>:</td><td>
						<select name="uprofile" required="1">
							<option value="">Pilih...</option>
							<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Durasi</td><td>:</td><td>
						<select name="utimelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$timelist = array ('1'=>$utimelimit1,$utimelimit2,$utimelimit3,$utimelimit4,$utimelimit5,$utimelimit6,$utimelimit7,$utimelimit8,$utimelimit9,$utimelimit10);
								
								$timetlist = array ('1'=>$utimelimit1t,$utimelimit2t,$utimelimit3t,$utimelimit4t,$utimelimit5t,$utimelimit6t,$utimelimit7t,$utimelimit8t,$utimelimit9t,$utimelimit10t);
								
									if($utimelimit1 == ""){
									}elseif ($utimelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Kuota</td><td>:</td><td>
						<select name="ubytelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$bytelist = array ('1'=>$ubytelimit1,$ubytelimit2,$ubytelimit3,$ubytelimit4,$ubytelimit5,$ubytelimit6,$ubytelimit7,$ubytelimit8,$ubytelimit9,$ubytelimit10);
								
								$bytetlist = array ('1'=>$ubytelimit1t,$ubytelimit2t,$ubytelimit3t,$ubytelimit4t,$ubytelimit5t,$ubytelimit6t,$ubytelimit7t,$ubytelimit8t,$ubytelimit9t,$ubytelimit10t);
								
									if($ubytelimit1 == ""){
									}elseif ($ubytelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<!--<tr><td>Harga</td><td>:</td><td>
						<select name="uprice" required="1">
							<option value="">Pilih...</option>
							<option>Free</option>
							<?php
								$pricelist = array ('1'=>$price1,$price2,$price3,$price4,$price5,$price6,$price7,$price8,$price9,$price10,$price11,$price12,$price13,$price14,$price15);
								
									if($price1 == ""){
									}elseif ($price2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>-->
					<td></td>
						<td colspan=3>
							<input type="submit" class="btnsubmit" value="Generate"/>
						</td>
					</tr>
					</tr>
					<tr><td colspan=3><p style="color:green;">Catatan:<br>Kode Voucher 2x panjang Username.</td></tr>
			<br>
			<!--<table>
				<tr>
					<td colspan=3>
						<button class="btnsubmit" onclick="window.open('./vouchers/kvoucher.html','_blank');">Cetak</button>
						</td>
				</tr>
			<br>
			</table>-->

<?php
	if(isset($_POST['uprofile'])){
		$API = new RouterosAPI();
		$API->debug = false;
		if ($API->connect($iphost, $userhost, $passwdhost)) {
		}
		$profname = ($_POST['uprofile']);
		$uprofile = $profname;
			if ($uprofile == $profile1){
				$vprofile = $vname1;
			}elseif ($uprofile == $profile2){
				$vprofile = $vname2;
			}elseif ($uprofile == $profile3){
				$vprofile = $vname3;
			}elseif ($uprofile == $profile4){
				$vprofile = $vname4;
			}elseif ($uprofile == $profile5){
				$vprofile = $vname5;
			}elseif ($uprofile == $profile6){
				$vprofile = $vname6;
			}elseif ($uprofile == $profile7){
				$vprofile = $vname7;
			}elseif ($uprofile == $profile8){
				$vprofile = $vname8;
			}elseif ($uprofile == $profile9){
				$vprofile = $vname9;
			}elseif ($uprofile == $profile10){
				$vprofile = $vname10;
			}elseif ($uprofile == $profile11){
				$vprofile = $vname11;
			}elseif ($uprofile == $profile12){
				$vprofile = $vname12;
			}elseif ($uprofile == $profile13){
				$vprofile = $vname13;
			}elseif ($uprofile == $profile14){
				$vprofile = $vname14;
			}elseif ($uprofile == $profile15){
				$vprofile = $vname15;
			}else {
				$vprofile= "";
			}
		$timelimit = ($_POST['utimelimit']);
		$tlimit = $timelimit;
			if ($tlimit == $utimelimit1){
				$vtimelimit = "Durasi:$utimelimit1t";
			}elseif ($tlimit == $utimelimit2){
				$vtimelimit = "Durasi:$utimelimit2t";
			}elseif ($tlimit == $utimelimit3){
				$vtimelimit = "Durasi:$utimelimit3t";
			}elseif ($tlimit == $utimelimit4){
				$vtimelimit = "Durasi:$utimelimit4t";
			}elseif ($tlimit == $utimelimit5){
				$vtimelimit = "Durasi:$utimelimit5t";
			}elseif ($tlimit == $utimelimit6){
				$vtimelimit = "Durasi:$utimelimit6t";
			}elseif ($tlimit == $utimelimit7){
				$vtimelimit = "Durasi:$utimelimit7t";
			}elseif ($tlimit == $utimelimit8){
				$vtimelimit = "Durasi:$utimelimit8t";
			}elseif ($tlimit == $utimelimit9){
				$vtimelimit = "Durasi:$utimelimit9t";
			}elseif ($tlimit == $utimelimit10){
				$vtimelimit = "Durasi:$utimelimit10t";
			}else {
				$vtimelimit= "";
		}
		$bytelimit = ($_POST['ubytelimit']);
		$blimit = $bytelimit;
			if ($blimit == $ubytelimit1){
				$vbytelimit = "Kuota:$ubytelimit1t";
			}elseif ($blimit == $ubytelimit2){
				$vbytelimit = "Kuota:$ubytelimit2t";
			}elseif ($blimit == $ubytelimit3){
				$vbytelimit = "Kuota:$ubytelimit3t";
			}elseif ($blimit == $ubytelimit4){
				$vbytelimit = "Kuota:$ubytelimit4t";
			}elseif ($blimit == $ubytelimit5){
				$vbytelimit = "Kuota:$ubytelimit5t";
			}elseif ($blimit == $ubytelimit6){
				$vbytelimit = "Kuota:$ubytelimit6t";
			}elseif ($blimit == $ubytelimit7){
				$vbytelimit = "Kuota:$ubytelimit7t";
			}elseif ($blimit == $ubytelimit8){
				$vbytelimit = "Kuota:$ubytelimit8t";
			}elseif ($blimit == $ubytelimit9){
				$vbytelimit = "Kuota:$ubytelimit9t";
			}elseif ($blimit == $ubytelimit10){
				$vbytelimit = "Kuota:$ubytelimit10t";
			}else {
				$vbytelimit= "";
			}
		$price = ($_POST['uprice']);
		$serverh = ($_POST['server']);
		$genall = ($_POST['genall']);
		$pjguser = ($_POST['pjguser']);
		$huruf = ($_POST['huruf']);
		$kkv = "--" . $serverh . "-" . $vprofile . "-" . $timelimit . "-" . $bytelimit . "-" . $price . "-" . date("d.m.y") . "-" . rand(100,999);
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$uprofile.'');
	$cekprice = $API->read();

	$regtable = $cekprice[0];
	$getprice = explode(",",$regtable['on-login']);
	$price = $getprice[2];
	$cur = "Rp";
	if($price == "" ){
	  $vprice = "Free";
	}elseif(strlen($price) == 4){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
	}elseif(strlen($price) == 5){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
	}elseif(strlen($price) == 6){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
	}elseif(strlen($price) == 7){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
	}elseif(strlen($price) == 8){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
	}elseif(strlen($price) == 9){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
	}else{
	  $vprice = $price;
	}

	if($genall=="kv"){

			if($huruf == "lower"){
			$a = substr(str_shuffle("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), -$pjguser);
		  }elseif($huruf == "upper"){
		  $a = substr(str_shuffle("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }elseif($huruf == "upplow"){
		  $a = substr(str_shuffle("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }
			if($pjguser == 3){
				$n = rand(100,999);
			}elseif($pjguser == 4){
				$n = rand(1000,9999);
			}elseif($pjguser == 5){
				$n = rand(10000,99999);
			}elseif($pjguser == 6){
				$n = rand(100000,999999);
			}
			$u = "$a$n";
			
			$API->comm("/ip/hotspot/user/add", array(
				"server" => "$serverh",
				"name" => "$u",
				"password" => "$u",
				"profile" => "$profname",
				"limit-uptime" => "$timelimit",
				"limit-bytes-out" => "$bytelimit",
				"comment" => "$kkv",
			));
		
		$my_file = 'vouchers/kvoucher.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $vkkv="' . $kkv . '"; $vserver="' . $serverh . '"; $vprofname="' . $vprofile . '"; $uptimelimit="' . $timelimit . '"; $upbytelimit="' . $bytelimit . '"; $vprice="' . $price . '"; ?>';
		fwrite($handle, $data);
		
		echo	"<table>";
		echo			"<table class='tusera' id='preview-table'>";
		echo				"<tr>";
		echo					"<tr>";
		echo						"<td style='text-align: right;'><?php print_r($headerv);? font-size: 16px;'>$headerv</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='font-size: 12px;'>Login dan Logout buka http://$notev</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td>";
		echo							"<table class='tuserb'>";
		echo								"<tr><td>Kode Voucher : $u </td></tr>";
		echo							"</table>";
		echo						"</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='text-align: center; '>Aktif:$vprofile $vtimelimit $vbytelimit</td></tr><tr><td style='text-align: center; '>$serverh $vprice</td>";
		echo					"</tr>";
		echo				"<tr>";
		echo			"</table>";
		echo	"</table>";
		echo	"<br>";
	}
	if($genall=="up"){
			if($huruf == "lower"){
			$a = substr(str_shuffle("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), -$pjguser);
		  }elseif($huruf == "upper"){
		  $a = substr(str_shuffle("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }elseif($huruf == "upplow"){
		  $a = substr(str_shuffle("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }
			if($pjguser == 3){
				$n = rand(100,999);
			}elseif($pjguser == 4){
				$n = rand(1000,9999);
			}elseif($pjguser == 5){
				$n = rand(10000,99999);
			}elseif($pjguser == 6){
				$n = rand(100000,999999);
			}
			
			$API->comm("/ip/hotspot/user/add", array(
			"server" => "$serverh",
			"name" => "$a",
			"password" => "$n",
			"profile" => "$profname",
			"limit-uptime" => "$timelimit",
			"limit-bytes-out" => "$bytelimit",
			"comment" => "$kkv",
			));
		
		$my_file = 'vouchers/voucher.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $vkkv="' . $kkv . '"; $vserver="' . $serverh . '"; $vprofname="' . $vprofile . '"; $uptimelimit="' . $timelimit . '"; $upbytelimit="' . $bytelimit . '"; $vprice="' . $price . '"; ?>';
		fwrite($handle, $data);

		echo	"<table>";
		echo			"<table class='tuserc' id='preview-table'>";
		echo				"<tr>";
		echo					"<tr>";
		echo						"<td style='text-align: right;'><?php print_r($headerv);? font-size: 16px;'>$headerv</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='font-size: 12px;'>Login dan Logout buka http://$notev</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td>";
		echo							"<table class='tuserd'>";
		echo								"<tr><td>Username : $a </td></tr>";
		echo								"<tr><td>Password : $n </td></tr>";
		echo							"</table>";
		echo						"</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='text-align: center; '>Aktif:$vprofile $vtimelimit $vbytelimit</td></tr><tr><td style='text-align: center; '>$serverh $vprice</td>";
		echo					"</tr>";
		echo				"<tr>";
		echo			"</table>";
		echo	"</table>";
		echo	"<br>";
		
	}
		
		$API->disconnect();
		
		
		
}
?>
	</body>
</html>


File: /mikhmon\app\genkvs.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


include('./vouchers/kvouchers.php');

$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$srvlist = $API->comm("/ip/hotspot/print");
	$API->disconnect();

}

?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Generate Kode Vouchers</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Generate Voucher</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="location.href='genkvs.php';" title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./uprofileadd.php';"	title="User Profile">local_library</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">find_in_page</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">User by profile</a>
									<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}
								?>
								</div>
						</div>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
					</td>
				</tr>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tnav" align="center"  >
					<tr><td>Jenis Voucher</td><td>:</td><td>
						<select name="genall" required="1">
							<option value="">Pilih...</option>
							<option value="kv">Kode Voucher</option>
							<option value="up">User Password</option>
						</select>
						</td>
					</tr>
					<tr><td>Server Hotspot</td><td>:</td><td>
						<select name="server" required="1">
							<option value="all">all</option>
							
							<?php
							$TotalReg = count($srvlist);

							for ($i=0; $i<$TotalReg; $i++){
							$regtable = $srvlist[$i];echo "<option>" . $regtable['name'];echo "</option>";
							}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Panjang Username</td><td>:</td><td>
						<select name="pjguser" required="1">
							<option value="">Pilih...</option>
							<option>3</option>
							<option>4</option>
							<option>5</option>
							<option>6</option>
						</select>
						</td>
					</tr>
					<tr><td>Huruf</td><td>:</td><td>
						<select name="huruf" required="1">
							<option value="lower">abcd</option>
							<option Value="upper">ABCD</option>
							<option Value="upplow">aBcD</option>
						</select>
						</td>
					</tr>
					<tr><td>Profile | Masa Aktif</td><td>:</td><td>
						<select name="uprofile" required="1">
							<option value="">Pilih...</option>
							<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Durasi</td><td>:</td><td>
						<select name="utimelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$timelist = array ('1'=>$utimelimit1,$utimelimit2,$utimelimit3,$utimelimit4,$utimelimit5,$utimelimit6,$utimelimit7,$utimelimit8,$utimelimit9,$utimelimit10);
								
								$timetlist = array ('1'=>$utimelimit1t,$utimelimit2t,$utimelimit3t,$utimelimit4t,$utimelimit5t,$utimelimit6t,$utimelimit7t,$utimelimit8t,$utimelimit9t,$utimelimit10t);
								
									if($utimelimit1 == ""){
									}elseif ($utimelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Kuota</td><td>:</td><td>
						<select name="ubytelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$bytelist = array ('1'=>$ubytelimit1,$ubytelimit2,$ubytelimit3,$ubytelimit4,$ubytelimit5,$ubytelimit6,$ubytelimit7,$ubytelimit8,$ubytelimit9,$ubytelimit10);
								
								$bytetlist = array ('1'=>$ubytelimit1t,$ubytelimit2t,$ubytelimit3t,$ubytelimit4t,$ubytelimit5t,$ubytelimit6t,$ubytelimit7t,$ubytelimit8t,$ubytelimit9t,$ubytelimit10t);
								
									if($ubytelimit1 == ""){
									}elseif ($ubytelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<!--<tr><td>Harga</td><td>:</td><td>
						<select name="uprice" required="1">
							<option value="">Pilih...</option>
							<option>Free</option>
							<?php
								$pricelist = array ('1'=>$price1,$price2,$price3,$price4,$price5,$price6,$price7,$price8,$price9,$price10,$price11,$price12,$price13,$price14,$price15);
								
									if($price1 == ""){
									}elseif ($price2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>-->
					<tr>
						<td>Jumlah Voucher</td>
						<td>:</td>
						<td><input type="text" name="jumlahv" required="1" size="3" maxlength="2"></td>
					</tr>
					<tr>
						<td></td>
						<td colspan=3>
							<input type="submit" class="btnsubmit" value="Generate"/>
						</td>
					</tr>
					<tr>
						<td colspan=3>
							<p>Catatan:</p>
							<ol>
								<li >Kode Voucher 2x panajang Username.</li>
								<li>Sebelum cetak sesuaikan margin agar hasil maksimal.</li>
							</ol>
						</td>
					</tr>
				</table>
			</form>
				<table class="tprinta">
					<tr>
						<th colspan=2>Cetak</th>
					</tr>
					<tr>
						<td style="text-align:center;">
							<button class="btnsubmit" onclick="window.open('./vouchers/printkvs.php','_blank');">Kode Voucher</button>
							<button class="btnsubmit" onclick="window.open('./vouchers/printkvsqr.php','_blank');">Kode Voucher QR</button>
						</td>
						<td style="text-align:center;">
							<button class="btnsubmit" onclick="window.open('./vouchers/printvs.php','_blank');">User Password</button>
							<button class="btnsubmit" onclick="window.open('./vouchers/printvsqr.php','_blank');">User Password QR</button>
						</td>
					</tr>
					<tr>
						<td colspan=2 style="text-align:center;"><button class="btnsubmit" onclick="location.href='./vcolorconf.php';">Ganti Warna</button></td>
					</tr>
				</table>
				<br>
<?php
	if(isset($_POST['uprofile'])){
		$API = new RouterosAPI();
		$API->debug = false;
		if ($API->connect($iphost, $userhost, $passwdhost)) {
		}
		$profname = ($_POST['uprofile']);
		$uprofile = $profname;
			if ($uprofile == $profile1){
				$vprofile = $vname1;
			}elseif ($uprofile == $profile2){
				$vprofile = $vname2;
			}elseif ($uprofile == $profile3){
				$vprofile = $vname3;
			}elseif ($uprofile == $profile4){
				$vprofile = $vname4;
			}elseif ($uprofile == $profile5){
				$vprofile = $vname5;
			}elseif ($uprofile == $profile6){
				$vprofile = $vname6;
			}elseif ($uprofile == $profile7){
				$vprofile = $vname7;
			}elseif ($uprofile == $profile8){
				$vprofile = $vname8;
			}elseif ($uprofile == $profile9){
				$vprofile = $vname9;
			}elseif ($uprofile == $profile10){
				$vprofile = $vname10;
			}elseif ($uprofile == $profile11){
				$vprofile = $vname11;
			}elseif ($uprofile == $profile12){
				$vprofile = $vname12;
			}elseif ($uprofile == $profile13){
				$vprofile = $vname13;
			}elseif ($uprofile == $profile14){
				$vprofile = $vname14;
			}elseif ($uprofile == $profile15){
				$vprofile = $vname15;
			}else {
				$vprofile= "";
			}
		$timelimit = ($_POST['utimelimit']);
		$tlimit = $timelimit;
			if ($tlimit == $utimelimit1){
				$vtimelimit = "Durasi:$utimelimit1t";
			}elseif ($tlimit == $utimelimit2){
				$vtimelimit = "Durasi:$utimelimit2t";
			}elseif ($tlimit == $utimelimit3){
				$vtimelimit = "Durasi:$utimelimit3t";
			}elseif ($tlimit == $utimelimit4){
				$vtimelimit = "Durasi:$utimelimit4t";
			}elseif ($tlimit == $utimelimit5){
				$vtimelimit = "Durasi:$utimelimit5t";
			}elseif ($tlimit == $utimelimit6){
				$vtimelimit = "Durasi:$utimelimit6t";
			}elseif ($tlimit == $utimelimit7){
				$vtimelimit = "Durasi:$utimelimit7t";
			}elseif ($tlimit == $utimelimit8){
				$vtimelimit = "Durasi:$utimelimit8t";
			}elseif ($tlimit == $utimelimit9){
				$vtimelimit = "Durasi:$utimelimit9t";
			}elseif ($tlimit == $utimelimit10){
				$vtimelimit = "Durasi:$utimelimit10t";
			}else {
				$vtimelimit= "";
		}
		$bytelimit = ($_POST['ubytelimit']);
		$blimit = $bytelimit;
			if ($blimit == $ubytelimit1){
				$vbytelimit = "Kuota:$ubytelimit1t";
			}elseif ($blimit == $ubytelimit2){
				$vbytelimit = "Kuota:$ubytelimit2t";
			}elseif ($blimit == $ubytelimit3){
				$vbytelimit = "Kuota:$ubytelimit3t";
			}elseif ($blimit == $ubytelimit4){
				$vbytelimit = "Kuota:$ubytelimit4t";
			}elseif ($blimit == $ubytelimit5){
				$vbytelimit = "Kuota:$ubytelimit5t";
			}elseif ($blimit == $ubytelimit6){
				$vbytelimit = "Kuota:$ubytelimit6t";
			}elseif ($blimit == $ubytelimit7){
				$vbytelimit = "Kuota:$ubytelimit7t";
			}elseif ($blimit == $ubytelimit8){
				$vbytelimit = "Kuota:$ubytelimit8t";
			}elseif ($blimit == $ubytelimit9){
				$vbytelimit = "Kuota:$ubytelimit9t";
			}elseif ($blimit == $ubytelimit10){
				$vbytelimit = "Kuota:$ubytelimit10t";
			}else {
				$vbytelimit= "";
			}
		$price = ($_POST['uprice']);
		$serverh = ($_POST['server']);
		$jmlv = ($_POST['jumlahv']);
		$genall = ($_POST['genall']);
		$pjguser = ($_POST['pjguser']);
		$huruf = ($_POST['huruf']);
		$kkv = $genall . "-" . $serverh . "-" . $vprofile . "-" . $timelimit . "-" . $bytelimit . "-" . $uprofile . "-" . date("d.m.y") . "-" . rand(100,999);
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$uprofile.'');
	$cekprice = $API->read();
	
	$regtable = $cekprice[0];
	$getprice = explode(",",$regtable['on-login']);
	$price = $getprice[2];
	$cur = "Rp";
	if($price == "" ){
	  $vprice = "Free";
	}elseif(strlen($price) == 4){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
	}elseif(strlen($price) == 5){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
	}elseif(strlen($price) == 6){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
	}elseif(strlen($price) == 7){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
	}elseif(strlen($price) == 8){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
	}elseif(strlen($price) == 9){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
	}else{
	  $vprice = $price;
	}
	if($genall=="kv"){
		for($i=1;$i<=$jmlv;$i++){
		  if($huruf == "lower"){
			$a[$i]= substr(str_shuffle("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), -$pjguser);
		  }elseif($huruf == "upper"){
		  $a[$i]= substr(str_shuffle("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }elseif($huruf == "upplow"){
		  $a[$i]= substr(str_shuffle("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }
			if($pjguser == 3){
				$n[$i]= rand(100,999);
			}elseif($pjguser == 4){
				$n[$i]= rand(1000,9999);
			}elseif($pjguser == 5){
				$n[$i]= rand(10000,99999);
			}elseif($pjguser == 6){
				$n[$i]= rand(100000,999999);
			}
			$u[$i] = "$a[$i]$n[$i]";
		}
		for($i=1;$i<=$jmlv;$i++){
			$API->comm("/ip/hotspot/user/add", array(
				"server" => "$serverh",
				"name" => "$u[$i]",
				"password" => "$u[$i]",
				"profile" => "$profname",
				"limit-uptime" => "$timelimit",
				"limit-bytes-out" => "$bytelimit",
				"comment" => "$kkv",
			));
		}
		$my_file = 'vouchers/kvouchers.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $vkkv="' . $kkv . '"; $vserver="' . $serverh . '"; $vprofname="' . $vprofile . '"; $uptimelimit="' . $timelimit . '"; $upbytelimit="' . $bytelimit . '"; $profv="' . $uprofile . '"; ?>';
	}
	if($genall=="up"){
		for($i=1;$i<=$jmlv;$i++){
			if($huruf == "lower"){
			$a[$i]= substr(str_shuffle("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), -$pjguser);
		  }elseif($huruf == "upper"){
		  $a[$i]= substr(str_shuffle("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }elseif($huruf == "upplow"){
		  $a[$i]= substr(str_shuffle("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), -$pjguser);
		  }
			if($pjguser == 3){
				$n[$i]= rand(100,999);
			}elseif($pjguser == 4){
				$n[$i]= rand(1000,9999);
			}elseif($pjguser == 5){
				$n[$i]= rand(10000,99999);
			}elseif($pjguser == 6){
				$n[$i]= rand(100000,999999);
			}
		}
		for($i=1;$i<=$jmlv;$i++){
			$API->comm("/ip/hotspot/user/add", array(
			"server" => "$serverh",
			"name" => "$a[$i]",
			"password" => "$n[$i]",
			"profile" => "$profname",
			"limit-uptime" => "$timelimit",
			"limit-bytes-out" => "$bytelimit",
			"comment" => "$kkv",
			));
		}
		
		$my_file = 'vouchers/vouchers.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $vkkv="' . $kkv . '"; $vserver="' . $serverh . '"; $vprofname="' . $vprofile . '"; $uptimelimit="' . $timelimit . '"; $upbytelimit="' . $bytelimit . '"; $profv="' . $uprofile . '"; ?>';
	}
		
		$API->disconnect();
		
		
		fwrite($handle, $data);
		
		echo	"<table class='tprinta'>";
		echo				"<tr>";
		echo					"<th>Generated</th>";
		echo				"<tr>";
		echo					"<td style='text-align: center; '>$genall Aktif:$vprofile $vtimelimit $vbytelimit</td></tr><tr><td style='text-align: center; '>$serverh $price</td>";
		echo				"</tr>";
		echo	"</table>";
		echo	"<br>";
	}
?>
	</body>
</html>


File: /mikhmon\app\genupm.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$srvlist = $API->comm("/ip/hotspot/print");
	$API->disconnect();
}

?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Generate Custom User Password</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<style>
table.tusera {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tusera td {
  padding: 4px;
  border: 2px solid #000000;
  font-size: 14px;
  text-align: left;
  font-weight: bold;
}
table.tuserb {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tuserb td {
  padding-left: 20px;
  border: 0px;
  font-size: 16px;
  text-align: left;
}
		</style>
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Generate Custom User Password</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="location.href='genupm.php';" title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./uprofileadd.php';"	title="User Profile">local_library</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">find_in_page</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">User by profile</a>
									<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}
								?>
								</div>
						</div>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
					</td>
				</tr>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tnav" align="center"  >
					<tr><td>Server Hotspot</td><td>:</td><td>
						<select name="server" required="1">
							<option value="all">all</option>
							
							<?php
							$TotalReg = count($srvlist);

							for ($i=0; $i<$TotalReg; $i++){
							$regtable = $srvlist[$i];echo "<option>" . $regtable['name'];echo "</option>";
							}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Profile | Masa Aktif</td><td>:</td><td>
						<select name="uprofile" required="1">
							<option value="">Pilih...</option>
							<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Durasi</td><td>:</td><td>
						<select name="utimelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$timelist = array ('1'=>$utimelimit1,$utimelimit2,$utimelimit3,$utimelimit4,$utimelimit5,$utimelimit6,$utimelimit7,$utimelimit8,$utimelimit9,$utimelimit10);
								
								$timetlist = array ('1'=>$utimelimit1t,$utimelimit2t,$utimelimit3t,$utimelimit4t,$utimelimit5t,$utimelimit6t,$utimelimit7t,$utimelimit8t,$utimelimit9t,$utimelimit10t);
								
									if($utimelimit1 == ""){
									}elseif ($utimelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}elseif ($utimelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$timelist[$i]>$timetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<tr><td>Kuota</td><td>:</td><td>
						<select name="ubytelimit" required="1">
							<option value="0">Pilih...</option>
							<?php
								$bytelist = array ('1'=>$ubytelimit1,$ubytelimit2,$ubytelimit3,$ubytelimit4,$ubytelimit5,$ubytelimit6,$ubytelimit7,$ubytelimit8,$ubytelimit9,$ubytelimit10);
								
								$bytetlist = array ('1'=>$ubytelimit1t,$ubytelimit2t,$ubytelimit3t,$ubytelimit4t,$ubytelimit5t,$ubytelimit6t,$ubytelimit7t,$ubytelimit8t,$ubytelimit9t,$ubytelimit10t);
								
									if($ubytelimit1 == ""){
									}elseif ($ubytelimit2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}elseif ($ubytelimit10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 10; $i++) {
										echo "<option value=$bytelist[$i]>$bytetlist[$i]</option>";
									}
									}
								?>
						</select>
						</td>
					</tr>
					<!--<tr><td>Harga</td><td>:</td><td>
						<select name="uprice" required="1">
							<option value="">Pilih...</option>
							<option>Free</option>
							<?php
								$pricelist = array ('1'=>$price1,$price2,$price3,$price4,$price5,$price6,$price7,$price8,$price9,$price10,$price11,$price12,$price13,$price14,$price15);
								
									if($price1 == ""){
									}elseif ($price2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}elseif ($price15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$pricelist[$i]</option>";
									}
									}
								?>
						</select>
						</td>-->
					</tr>
					<tr><td>Username</td><td>:</td><td><input type="text" size="10" maxlength="10" name="uname" required="1"/></td></tr>
					<tr><td>Password</td><td>:</td><td><input type="text" size="10" maxlength="10" name="passwd" required="1"/></td></tr>
					<td></td>
						<td colspan=3>
							<input type="submit" class="btnsubmit" value="Generate"/>
							</td>
					</tr>
			</form>
			<br>
			<!--<table>
				<tr>
					<td colspan=3>
						<button class="btnsubmit" onclick="window.open('./vouchers/userpass.html','_blank');">Cetak</button>
						</td>
				</tr>
			<br>
			</table>-->

<?php
	if(isset($_POST['uprofile'])){
		$API = new RouterosAPI();
		if ($API->connect($iphost, $userhost, $passwdhost)) {
		}
		$profname = ($_POST['uprofile']);
		$uprofile = $profname;
			if ($uprofile == $profile1){
				$vprofile = $vname1;
			}elseif ($uprofile == $profile2){
				$vprofile = $vname2;
			}elseif ($uprofile == $profile3){
				$vprofile = $vname3;
			}elseif ($uprofile == $profile4){
				$vprofile = $vname4;
			}elseif ($uprofile == $profile5){
				$vprofile = $vname5;
			}elseif ($uprofile == $profile6){
				$vprofile = $vname6;
			}elseif ($uprofile == $profile7){
				$vprofile = $vname7;
			}elseif ($uprofile == $profile8){
				$vprofile = $vname8;
			}elseif ($uprofile == $profile9){
				$vprofile = $vname9;
			}elseif ($uprofile == $profile10){
				$vprofile = $vname10;
			}elseif ($uprofile == $profile11){
				$vprofile = $vname11;
			}elseif ($uprofile == $profile12){
				$vprofile = $vname12;
			}elseif ($uprofile == $profile13){
				$vprofile = $vname13;
			}elseif ($uprofile == $profile14){
				$vprofile = $vname14;
			}elseif ($uprofile == $profile15){
				$vprofile = $vname15;
			}else {
				$vprofile= "";
			}
		$timelimit = ($_POST['utimelimit']);
		$tlimit = $timelimit;
			if ($tlimit == $utimelimit1){
				$vtimelimit = "Durasi:$utimelimit1t";
			}elseif ($tlimit == $utimelimit2){
				$vtimelimit = "Durasi:$utimelimit2t";
			}elseif ($tlimit == $utimelimit3){
				$vtimelimit = "Durasi:$utimelimit3t";
			}elseif ($tlimit == $utimelimit4){
				$vtimelimit = "Durasi:$utimelimit4t";
			}elseif ($tlimit == $utimelimit5){
				$vtimelimit = "Durasi:$utimelimit5t";
			}elseif ($tlimit == $utimelimit6){
				$vtimelimit = "Durasi:$utimelimit6t";
			}elseif ($tlimit == $utimelimit7){
				$vtimelimit = "Durasi:$utimelimit7t";
			}elseif ($tlimit == $utimelimit8){
				$vtimelimit = "Durasi:$utimelimit8t";
			}elseif ($tlimit == $utimelimit9){
				$vtimelimit = "Durasi:$utimelimit9t";
			}elseif ($tlimit == $utimelimit10){
				$vtimelimit = "Durasi:$utimelimit10t";
			}else {
				$vtimelimit= "";
		}
		$bytelimit = ($_POST['ubytelimit']);
		$blimit = $bytelimit;
			if ($blimit == $ubytelimit1){
				$vbytelimit = "Kuota:$ubytelimit1t";
			}elseif ($blimit == $ubytelimit2){
				$vbytelimit = "Kuota:$ubytelimit2t";
			}elseif ($blimit == $ubytelimit3){
				$vbytelimit = "Kuota:$ubytelimit3t";
			}elseif ($blimit == $ubytelimit4){
				$vbytelimit = "Kuota:$ubytelimit4t";
			}elseif ($blimit == $ubytelimit5){
				$vbytelimit = "Kuota:$ubytelimit5t";
			}elseif ($blimit == $ubytelimit6){
				$vbytelimit = "Kuota:$ubytelimit6t";
			}elseif ($blimit == $ubytelimit7){
				$vbytelimit = "Kuota:$ubytelimit7t";
			}elseif ($blimit == $ubytelimit8){
				$vbytelimit = "Kuota:$ubytelimit8t";
			}elseif ($blimit == $ubytelimit9){
				$vbytelimit = "Kuota:$ubytelimit9t";
			}elseif ($blimit == $ubytelimit10){
				$vbytelimit = "Kuota:$ubytelimit10t";
			}else {
				$vbytelimit= "";
			}
		$price = ($_POST['uprice']);
		$serverh = ($_POST['server']);
		$u1 = ($_POST['uname']);
		$p1 = ($_POST['passwd']);
		$kkv = "--" . $serverh . "-" . $vprofile . "-" . $timelimit . "-" . $bytelimit . "-" . $price . "-" . date("d.m.y") . "-" . rand(100,999);
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$uprofile.'');
	$cekprice = $API->read();

	$regtable = $cekprice[0];
	$getprice = explode(",",$regtable['on-login']);
	$price = $getprice[2];
	$cur = "Rp";
	if($price == "" ){
	  $vprice = "Free";
	}elseif(strlen($price) == 4){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
	}elseif(strlen($price) == 5){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
	}elseif(strlen($price) == 6){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
	}elseif(strlen($price) == 7){
	  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
	}elseif(strlen($price) == 8){
	  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
	}elseif(strlen($price) == 9){
	  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
	}else{
	  $vprice = $price;
	}
		
		$API->comm("/ip/hotspot/user/add", array(
		  "server" => "$serverh",
		  "name" => "$u1",
		  "password" => "$p1",
		  "profile" => "$profname",
		  "limit-uptime" => "$timelimit",
		  "limit-bytes-out" => "$bytelimit",
		  "comment" => "$kkv",
		));

		$API->disconnect();
		
		$my_file = 'vouchers/voucher.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $user1="' . $u1. '";$pass1="' . $p1. '";$vprofname="' . $profname. '";$vptimelimit="' . $vtimelimit. '"; $vpbytelimit="' . $vbytelimit. '"; $vprice="' . $price. '"; ?>';
		fwrite($handle, $data);

		$my_file1 = 'vouchers/userpass.html';
		fwrite($handle1, $data1);
	
		echo	"<table>";
		echo			"<table class='tusera' id='preview-table'>";
		echo				"<tr>";
		echo					"<tr>";
		echo						"<td style='text-align: right;'><?php print_r($headerv);? font-size: 16px;'>$headerv</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='font-size: 12px;'>Login dan Logout buka http://$notev</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td>";
		echo							"<table class='tuserb'>";
		echo								"<tr><td>Username : $u1 </td></tr>";
		echo								"<tr><td>Password : $p1 </td></tr>";
		echo							"</table>";
		echo						"</td>";
		echo					"</tr>";
		echo					"<tr>";
		echo						"<td style='text-align: center; '>Aktif:$vprofile $vtimelimit $vbytelimit</td></tr><tr><td style='text-align: center; '>$serverh $vprice</td>";
		echo					"</tr>";
		echo				"<tr>";
		echo			"</table>";
		echo	"</table>";
		echo	"<br>";

}
?>
	</body>
</html>


File: /mikhmon\app\history.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}

$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/history/print', false);
	$API->write('?=by=');
	$ARRAY = $API->read();
	$API->disconnect();
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
	<div class="main">
	<table class="tnav">
		<tr>
			<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
		</tr>
		<tr>
			<td>History</td>
			<td>
				<button class="material-icons" onclick="Reload()" title="Reload">autorenew</button>
				<button class="material-icons"	onclick="location.href='./hotspotlog.php';" 	title="Log Hotspot">subject</button>
				<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
				<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
			</td>
		</tr>
	</table>
		<div style="overflow-x:auto;">
			<table style="white-space: nowrap;" class="zebra" >
				<tr>
					<th >Time</th>
					<th >Action</th>
				</tr>
				<?php
					$TotalReg = count($ARRAY);

						for ($i=0; $i<$TotalReg; $i++){
							$regtable = $ARRAY[$i];echo "<tr><td>" . $regtable['time'];echo "</td>";
							$regtable = $ARRAY[$i];echo "<td>" . $regtable['action'];echo "</td> </tr>";
							}
				?>
			</table>
		</div>
	</div>
	</body>
</html>


File: /mikhmon\app\hotspotlog.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/log/print', false);
	$API->write('?=topics=hotspot,info,debug');
	$ARRAY = $API->read();
	$log = array_reverse($ARRAY);
	$API->disconnect();
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
	<div class="main">
	<table class="tnav">
		<tr>
			<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
		</tr>
		<tr>
			<td>Hotspot Log</td>
			<td>
				<button class="material-icons" onclick="Reload()" title="Reload">autorenew</button>
				<button class="material-icons"	onclick="location.href='./history.php';" 	title="History">toc</button>
				<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
				<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
			</td>
		</tr>
	</table>
		<div style="overflow-x:auto;">
			<table id="tLog" style="white-space: nowrap;" class="zebra" >
				<tr>
					<th >Time</th>
					<th >
					  <div style="width:50%;">
					    <input style="width:50%;" type="text" id="Mess" size="auto" onkeyup="fMess()" placeholder="Messages" title="Filter log messages.">
					  </div>
					</th>
				</tr>
				<?php
					$TotalReg = count($log);

						for ($i=0; $i<$TotalReg; $i++){
							$regtable = $log[$i];echo "<tr><td>" . $regtable['time'];echo "</td>";
							$regtable = $log[$i];echo "<td>" . $regtable['message'];echo "</td> </tr>";
							}
				?>
			</table>
		</div>
	</div>
	<script>
	function fMess() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("Mess");
  filter = input.value.toUpperCase();
  table = document.getElementById("tLog");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
	</script>
	</body>
</html>


File: /mikhmon\app\img\index.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
echo "<meta http-equiv='refresh' content='0;url=../' />";
?>



File: /mikhmon\app\index.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}



$oldbuild = 2055;
$build = file_get_contents('build.txt');
				$getbuild = explode("\n",$build);
				$newbuild = $getbuild[0];

$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$ARRAY = $API->comm("/ip/hotspot/active/print");

	$ARRAY1 = $API->comm("/system/schedule/print");

	$API->write('/ip/hotspot/active/print', false);
	$API->write('=count-only=', false);
	$API->write('~active-address~"1.1."');
	$ARRAY2 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile1.'');
	$ARRAY3 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile2.'');
	$ARRAY4 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile3.'');
	$ARRAY5 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile4.'');
	$ARRAY6 = $API->read();
	
	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile5.'');
	$ARRAY7 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile6.'');
	$ARRAY8 = $API->read();
	
	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile7.'');
	$ARRAY9 = $API->read();
	
	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile8.'');
	$ARRAY10 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile9.'');
	$ARRAY11 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile10.'');
	$ARRAY12 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile11.'');
	$ARRAY13 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile12.'');
	$ARRAY14 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile13.'');
	$ARRAY15 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile14.'');
	$ARRAY16 = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$profile15.'');
	$ARRAY17 = $API->read();

	$ARRAY18 = $API->comm("/system/clock/print");
	$ARRAY19 = $API->comm("/system/resource/print");
	$ARRAY20 = $API->comm("/system/routerboard/print");
	
    $API->disconnect();
    
	$a=array($ARRAY3,$ARRAY4,$ARRAY5,$ARRAY6,$ARRAY7,$ARRAY8,$ARRAY9,$ARRAY10,$ARRAY11,$ARRAY12,$ARRAY13,$ARRAY14,$ARRAY15,$ARRAY16,$ARRAY17);
	$aa = array_sum($a);
}
?>
<?php
  if(isset($_POST['btnupdate'])){
   copy("http://laksa.mooo.com/ota-update/app/build.txt","build.txt");
   copy("http://laksa.mooo.com/ota-update/app/otaupdate.dat","otaupdate.php");
   echo "<script>location.href='';</script>";
  }

?>
<?php
if ($reloadindex == ""){
} else
$url1=$_SERVER['REQUEST_URI'];
header("Refresh: $reloadindex ; url='$url1'");

// Kick User
$id = $_GET['id'];
if(isset($id)){
if ($API->connect( $iphost, $userhost, $passwdhost )) {
$API->comm("/ip/hotspot/active/remove", array(
".id"=> "$id",));
$API->disconnect();
header("Location:./");
}
}
// Get User
$name = $_GET['usr'];
	if(isset($name)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/scheduler/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY1 = $API->read();
	$regtable = $ARRAY1[0];
	      $user = $regtable['name'];
				$exp = $regtable['next-run'];
				$strd = $regtable['start-date'];
				$strt = $regtable['start-time'];
				$cek = $regtable['interval'];
					$ceklen = strlen(substr($cek,0));
					$cekw = substr($cek, 0,2);
					$cekw1 = substr($cekw, 0,1) ."Minggu";
					$cekd = substr($cek, 2,2);
					$cekd1 = substr($cek, 2,1) ."Hari";
				if ($ceklen > 3){
					$cekall = $cekw1 ." ".$cekd1;
				}elseif (substr($cek, -1) == "h"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Jam";
				}elseif (substr($cek, -1) == "d"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Hari";
				}elseif (substr($cek, -1) == "w"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Minggu";
				}elseif($cekall == ""){
					}
				 $cekall;
				 $API->disconnect();
	}}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="refresh" content="" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="Reload()"	title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='logout.php';" 	title="Logout">lock</button>
						<button class="material-icons"	onclick="location.href='./setup.php';" 	title="Setup Edit Config">settings</button>
						<button class="material-icons"	onclick="location.href='./hotspotlog.php';" 	title="Log Hotspot">subject</button>
						<button class="material-icons" onclick="location.href='./dnsstaticadd.php';" title="Add DNS Static">cloud_queue</button>
						<button class="material-icons"	onclick="location.href='./uprofileadd.php';"	title="User Profile">local_library</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<button class="material-icons"	onclick="location.href='../status';"	title="Status User">account_box</button>
						<button class="material-icons"	onclick="location.href='./penjualan.php';"	title="Penjualan">monetization_on</button>
						<form  method="post"><input type="submit" name="btnupdate" class="material-icons"	title="Cek Update" value="system_update_alt"></form>
						<!-- -->
					</td>
				</tr>
				<tr>
				<td colspan=2>Mikrotik System Date :
				
							<?php
								$regtable = $ARRAY18[0]; echo " " . $regtable['date']; echo " " . $regtable['time'] . "<br />"; echo "</td>";
								$timemk = ($ARRAY18[0]['time']);
								if($timemk == ""){
								?><meta http-equiv="refresh" content="0; url=logout.php"><?php
								}
							?>
				</tr>
				<td>
							<?php
									$regtable = $ARRAY20[0];echo "" . $regtable['model'] . " ";
									$regtable = $ARRAY19[0];echo "" . $regtable['version'] . "<br>";
									$regtable = $ARRAY19[0];echo "Free Memory : " . formatBytes2($regtable['free-memory'], 0); echo "<br>";
									echo "</td>";
							?>
				<td style="text-align:right;"><?php if($newbuild > $oldbuild){echo "<a href='otaupdate.php' title='Download update, klik di sini!'><i style='color:red;'>New update! | Build : $newbuild</i></a>";}else{echo "Mikhmon Build : $oldbuild";} ?></td>
				</tr>
			</table>
			<table class="tnav">
				<tr>
					<td><p>Sisa Voucher Aktif : <?php	echo $aa;	?></p></td>
					<td style="text-align: right;"><?php print_r($_SESSION['usermikhmon']);?></td>
				</tr>
			</table>
              <?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								$sisa = array('1'=>$ARRAY3,$ARRAY4,$ARRAY5,$ARRAY6,$ARRAY7,$ARRAY8,$ARRAY9,$ARRAY10,$ARRAY11,$ARRAY12,$ARRAY13,$ARRAY14,$ARRAY15,$ARRAY16,$ARRAY17);
								
								echo "<div style='overflow-x:auto;'><table class='tprinta' ><tr>";
				            
									if($profile1 == ""){
									}elseif ($profile2 == ""){
									  ?>
									  <?php for ($i = 1; $i <= 1; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 1; $i <= 1; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									
									}elseif ($profile3 == ""){
									  ?>
										<?php for ($i = 1; $i <= 2; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 1; $i <= 2; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile4 == ""){
									  ?>
										<?php for ($i = 1; $i <= 3; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 1; $i <= 3; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile5 == ""){
									  ?>
										<?php for ($i = 1; $i <= 4; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 1; $i <= 4; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}else{
									  ?>
									  <?php for ($i = 1; $i <= 5; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 1; $i <= 5; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";?>
				            <?php
									}
									  echo "</table></div><div style='overflow-x:auto;padding-top:5px;'><table class='tprinta' ><tr>";
									?>
									<?php if ($profile6 == ""){
									}elseif ($profile7 == ""){
										?>
									  <?php for ($i = 6; $i <= 6; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 6; $i <= 6; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									
									}elseif ($profile8 == ""){
									  ?>
										<?php for ($i = 6; $i <= 7; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 6; $i <= 7; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile9 == ""){
									  ?>
										<?php for ($i = 6; $i <= 8; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 6; $i <= 8; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile10 == ""){
									  ?>
										<?php for ($i = 6; $i <= 9; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 6; $i <= 9; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}else{
									  ?>
									  <?php for ($i = 6; $i <= 10; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 6; $i <= 10; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";?>
				            <?php
									}
									  echo "</table></div><div style='overflow-x:auto;padding-top:5px;'><table class='tprinta' ><tr>";
									?>
									<?php if ($profile11 == ""){
									}elseif ($profile12 == ""){
										?>
									  <?php for ($i = 11; $i <= 11; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 11; $i <= 11; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									
									}elseif ($profile13 == ""){
									  ?>
										<?php for ($i = 11; $i <= 12; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 11; $i <= 12; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile14 == ""){
									  ?>
										<?php for ($i = 11; $i <= 13; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 11; $i <= 13; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}elseif ($profile15 == ""){
									  ?>
										<?php for ($i = 11; $i <= 14; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 11; $i <= 14; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";
									}else{
									  ?>
									  <?php for ($i = 11; $i <= 15; $i++) {echo "	<th><a href='userlist.php?profile=$proflist[$i]'>$proflist[$i]</a></th>";}?>
				            <?php echo "</tr> <tr>";?>
				            <?php for ($i = 11; $i <= 15; $i++) {echo "	<td>$sisa[$i]</td>";}?>
				            <?php echo "</tr>";?>
				            <?php
									}
									  echo "</table></div>";
								?>
			<table class="tnav">
				<tr>
					<td>User Aktif : <?php print_r($ARRAY2);?></td>
				</tr>
			</table>

			<div style="overflow-x:auto;">
			<table style="white-space: nowrap;" class="zebra" >
				<tr>
					<th style='text-align:center;'>X</th>
					<th >User</th>
					<th >Server</th>
					<th >IP</th>
					<th >MAC Address</th>
					<th >Uptime</th>
					<th >Bytes Out</th>
					<th >Login By</th>
					</tr>
							<?php
								$TotalReg = count($ARRAY);

										for ($i=0; $i<$TotalReg; $i++){
										echo "<tr>";
										$regtable = $ARRAY[$i];echo "<td style='text-align:center;'><a style='color:#000;' title='Klik X untuk disconnect user' href=index.php?id=".$regtable['.id'] . "&name=" . $regtable['user']. ">X</a></td>";
										$regtable = $ARRAY[$i];echo "<td><a style='color:#000;' title='Klik user untuk melihat masa aktifnya' href=?usr=" . $regtable['user'] . "#cekuser>". $regtable['user']. "</a></td>";
										$regtable = $ARRAY[$i];echo "<td>" . $regtable['server'];echo "</td>";
										$regtable = $ARRAY[$i];echo "<td>" . $regtable['address'];echo "</td>";
										$regtable = $ARRAY[$i];echo "<td>" . $regtable['mac-address'];echo "</td>";
										$regtable = $ARRAY[$i];echo "<td>" . $regtable['uptime'];echo "</td>";
										$regtable = $ARRAY[$i];echo "<td style='text-align:right;'>" . formatBytes2($regtable['bytes-out'], 0) ;echo "</td>";
										$regtable = $ARRAY[$i];echo "<td>" . $regtable['login-by'];echo "</td>";
										echo "</tr>";
										}
							?>
			</table>
			</div>
			
	  <div id="cekuser" class="modal-window">
		<div>
			<a style="font-wight:bold;"href="#x" title="Close" class="modal-close">X</a>
			<h3>Masa Aktif Voucher</h3>
	<?php
	echo "<div style='overflow-x:auto;'>";
	echo "<table>";
	echo "	<tr>";
	echo "		<td >User/Kode Voucher</td>";
	echo "		<td >:</td>";
	echo "		<td > $user</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Masa Aktif</td>";
	echo "		<td >:</td>";
	echo "		<td >$cekall</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Dari</td>";
	echo "		<td >:</td>";
	echo "		<td >$strd $strt</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Sampai</td>";
	echo "		<td >:</td>";
	echo "		<td >$exp</td>";
	echo "	</tr>";
	echo "</table>";
	echo "</div>";
  ?>
    </div>
    </div>
	</div>
<?php

function formatBytes($bytes, $precision = 2) {
$units = array('B', 'KB', 'MB', 'GB', 'TB');

$bytes = max($bytes, 0);
$pow = floor(($bytes ? log($bytes) : 0) / log(1024));
$pow = min($pow, count($units) - 1);

// Uncomment one of the following alternatives
// $bytes /= pow(1024, $pow);
// $bytes /= (1 << (10 * $pow));

return round($bytes, $precision) . ' ' . $units[$pow];
}

function formatBytes2($size, $decimals = 0){
$unit = array(
'0' => 'Byte',
'1' => 'KiB',
'2' => 'MiB',
'3' => 'GiB',
'4' => 'TiB',
'5' => 'PiB',
'6' => 'EiB',
'7' => 'ZiB',
'8' => 'YiB'
);

for($i = 0; $size >= 1024 && $i <= count($unit); $i++){
$size = $size/1024;
}

return round($size, $decimals).' '.$unit[$i];
}

?>

	</body>
</html>



File: /mikhmon\app\lib\api.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 5;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    public function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $ip.':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


File: /mikhmon\app\lib\index.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
echo "<meta http-equiv='refresh' content='0;url=../' />";
?>



File: /mikhmon\app\login.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
include('./config.php');
if(isset($_SESSION['usermikhmon'])){
	header("Location: ./");
}

if(isset($_POST['login'])){
	$user = $_POST['user'];
	$pass = $_POST['pass'];
		if($user == $userhost && $pass == $passwdhost){
			$_SESSION['usermikhmon']=$user;
				header("Location:./");
		}elseif ($user == $useradm && $pass == $passadm){
			$_SESSION['usermikhmon']=$user;
			header("Location:setup.php");
		}else{
			$error = "Username atau Password tidak sesuai.";
	}
}
 ?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<style>
table.tlogin {
  margin-left:auto;
  margin-right:auto;
  width: 200px;
  border: 1px solid #ccc;
}
table.tlogin th {
  background: #008CCA;
  color: white;
  font-weight: bold;
  text-align: center;
}
table.tlogin td {
  padding: 6px;
  text-align: center;
}
table.tsub {
  margin-left:auto;
  margin-right:auto;
  width: 200px;
  border: 1px solid #ccc;
}
table.tsub th {
  background: #008CCA;
  color: white;
  font-weight: bold;
  text-align: center;
}
table.tsub td {
  padding: 6px;
  text-align: center;
}
.btnlogin {
  background-color: #008CCA;
  border: none;
  padding: 5px 5px;
  color: white;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  cursor: pointer;
  width:95%;
  margin-left:auto;
  margin-right:auto;
  border-radius: 5px;
}

textarea,input,select {
  background-color: #FDFBFB;
  border: 1px solid #008CCA;
  padding: 2px;
  margin: 2px;
  font-size: 14px;
  color: #808080;
  outline: none;
}
		</style>
	</head>
		<body>
			<div id="login">
				<form autocomplete="off" action="" method="post">
					<br>
					<table style="border:0px;" class="tlogin">
					<td><img src="./img/favicon.png" alt="mikhmon" /></td>
					</table>
					<table class="tlogin">
						<tr>
							<th>MIKHMON</th>
						</tr>
						<tr>
							<td><input type="text" name="user" placeholder="Username" required="1" autofocus></td>
						</tr>
						<tr>
							<td><input type="password" name="pass" placeholder="Password" required="1" ></td>
						</tr>
						<tr>
							<td style="font-size: 14px; color:red; " ><input class="btnlogin" type="submit" name="login" value="Login"><p><?php if(isset($_POST['login'])){ print_r($error);}?></p></td>
						</tr>
					</table>
				</form>
				<br>
			</div>
		</body>
</html>


File: /mikhmon\app\logout.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
 
 	session_start();
 	session_destroy();

 	header("Location: login.php");
?>


File: /mikhmon\app\otaupdate.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}

?>
<?php
error_reporting(0);
copy("http://laksa.mooo.com/ota-update/app/build.txt","build.txt");
copy("http://laksa.mooo.com/ota-update/app/otaupdate.dat","otaupdate.php");
$build = file_get_contents('build.txt');
				$getbuild = explode("\n",$build);
				$newbuild = $getbuild[0];
// server
$srcpath1 ="http://laksa.mooo.com/ota-update/app/";
$srcpath2 ="http://laksa.mooo.com/ota-update/status/";
// local
$dstpath2 ="./css/";
$dstpath3 ="./vouchers/";
$dstpath4 ="../status/";
//array server
$src = array ('1'=>
// path1
$srcpath1."conntest.dat",
$srcpath1."dnsstaticadd.dat",
$srcpath1."dnsstaticrm.dat",
$srcpath1."genkv.dat",
$srcpath1."genkvs.dat",
$srcpath1."genupm.dat",
$srcpath1."history.dat",
$srcpath1."hotspotlog.dat",
$srcpath1."login.dat",
$srcpath1."logout.dat",
$srcpath1."reboot.dat",
$srcpath1."resetcolor.dat",
$srcpath1."resetconfig.dat",
$srcpath1."setup.dat",
$srcpath1."uprofileadd.dat",
$srcpath1."vcolorconf.dat",
$srcpath1."userlist.dat",
$srcpath1."otaupdate.dat",
$srcpath1."penjualan.dat",
$srcpath1."style.css",
$srcpath1."vcolors.dat",
$srcpath1."printkvs.dat",
$srcpath1."printkvsqr.dat",
$srcpath1."printvs.dat",
$srcpath1."printvsqr.dat",
$srcpath1."index.dat",
// path2
$srcpath2."index.dat"
);
// array local
$dst = array ('1'=>
"./conntest.php",
"./dnsstaticadd.php",
"./dnsstaticrm.php",
"./genkv.php",
"./genkvs.php",
"./genupm.php",
"./history.php",
"./hotspotlog.php",
"./login.php",
"./logout.php",
"./reboot.php",
"./resetcolor.php",
"./resetconfig.php",
"./setup.php",
"./uprofileadd.php",
"./vcolorconf.php",
"./userlist.php",
"./otaupdate.php",
"./penjualan.php",
// path2
$dstpath2."style.css",
$dstpath2."vcolors.php",
// path3
$dstpath3."printkvs.php",
$dstpath3."printkvsqr.php",
$dstpath3."printvs.php",
$dstpath3."printvsqr.php",
// final
"./index.php",
// path4
$dstpath4."index.php"
);
if(isset($_POST['btnupdate'])){
  for ($i = 1; $i <= count($src); $i++) {
	copy($src[$i],$dst[$i]);
    }
  /*for ($i = 1; $i <= count($src); $i++) {
  if(!file_exists($src[$i])) {
  die("OTA Update gagal, file tidak ditemukan!");
  }
  }*/
  header("Location:./");
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="refresh" content="" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="Reload()"	title="Reload">autorenew</button>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
					</td>
				</tr>
      </table>
      <div style='padding:10px;'>
        <h3 style="text-align:center;">Mikhmon OTA Update<br>
        <form  method="post"><input type="submit" name="btnupdate" class="btnsubmit"	title="OTA Update" value="Update Mikhmon"></form>
        </h3>
        <br>
			<?php
					echo "<p><b style='font-size:16px;'>Changelog | Build : $newbuild</b></p>";
				for ($i=1;$i<count($getbuild);$i++) {
					echo  $getbuild[$i].'<br> ';
					}
			?>
    </div>
    <div style='padding:10px;'>
				<h3>Update Manual</h3>
				<ol>
				<li>Download <a style="color:#000;" title="Download update.zip" href="https://laksa19.github.io/download/update.zip" target="_blank">update.zip</a></li>
				<li>Extract update.zip.</li>
				<li>Copy folder mikhmon.</li>
				<li>Paste folder root webserver, timpa folder mikhmon yang lama.</li>
				</ol>
			</div>
    </div>
  </body>
</html>


File: /mikhmon\app\penjualan.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}

$API = new RouterosAPI();
$API->debug = false;

$idhr = $_GET['idhr'];
$idbl = $_GET['idbl'];
$remdata = ($_POST['remdata']);

if(isset($remdata)){
  if(strlen($idhr) > "0"){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->write('/system/script/print', false);
	  $API->write('?source='.$idhr.'', false);
	  $API->write('=.proplist=.id');
	  $ARREMD = $API->read();
	  for ($i=0;$i<count($ARREMD);$i++) {
	  $API->write('/system/script/remove', false);
	  $API->write('=.id=' . $ARREMD[$i]['.id']);
	  $READ = $API->read();
	    header("Location:#");
	}
	}
  }elseif(strlen($idbl) > "0"){
  if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->write('/system/script/print', false);
	  $API->write('?owner='.$idbl.'', false);
	  $API->write('=.proplist=.id');
	  $ARREMD = $API->read();
	  for ($i=0;$i<count($ARREMD);$i++) {
	  $API->write('/system/script/remove', false);
	  $API->write('=.id=' . $ARREMD[$i]['.id']);
	  $READ = $API->read();
	    header("Location:#");
	}
	}
  
}}


if(strlen($idhr) > "0"){
  if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/script/print', false);
	$API->write('?=source='.$idhr.'');
	$ARRAY = $API->read();
	$API->disconnect();
  }
	$filedownload = $idhr;
	$shf = "hidden";
	$shd = "text";
}elseif(strlen($idbl) > "0"){
  if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/script/print', false);
	$API->write('?=owner='.$idbl.'');
	$ARRAY = $API->read();
	$API->disconnect();
  }
	$filedownload = $idbl;
	$shf = "hidden";
	$shd = "text";
}elseif($idhr == "" || $idbl == ""){
  if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/script/print', false);
	$API->write('?=comment=mikhmon');
	$ARRAY = $API->read();
	$API->disconnect();
}
$filedownload = "all";
$shf = "text";
$shd = "hidden";
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
			function downloadCSV(csv, filename) {
			  var csvFile;
			  var downloadLink;
			  // CSV file
			  csvFile = new Blob([csv], {type: "text/csv"});
			  // Download link
			  downloadLink = document.createElement("a");
			  // File name
			  downloadLink.download = filename;
			  // Create a link to the file
			  downloadLink.href = window.URL.createObjectURL(csvFile);
			  // Hide download link
			  downloadLink.style.display = "none";
			  // Add the link to DOM
			  document.body.appendChild(downloadLink);
			  // Click download link
			  downloadLink.click();
			  }
			  
			  function exportTableToCSV(filename) {
			    var csv = [];
			    var rows = document.querySelectorAll("#laporan tr");
			    
			   for (var i = 0; i < rows.length; i++) {
			      var row = [], cols = rows[i].querySelectorAll("td, th");
			   for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);
        csv.push(row.join(","));
        }
        // Download CSV file
        downloadCSV(csv.join("\n"), filename);
        }
        
        window.onload=function() {
          var sum = 0;
          var dataTable = document.getElementById("laporan");
          
          // use querySelector to find all second table cells
          var cells = document.querySelectorAll("td + td + td + td");
          for (var i = 0; i < cells.length; i++)
          sum+=parseFloat(cells[i].firstChild.data);
          
          var th = document.getElementById('total');
          th.innerHTML = th.innerHTML + (sum) ;
        }
		</script>
	</head>
	<body>
	<div class="main">
	<table class="tnav">
		<tr>
			<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
		</tr>
		<tr>
			<td>Penjualan</td>
			<td>
				<button class="material-icons" onclick="Reload()" title="Reload">autorenew</button>
				
				<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
				<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
			</td>
		</tr>
	</table>
		<div style="overflow-x:auto;">
		  <div>
		    <p>Bantuan
		      <ol>
		        <li>"CSV" berfungsi untuk mengunduh semua data penjualan.</li>
		        <li>Untuk mengunduh laporan penjualan per "Hari",<br> silahkan klik salah satu tanggal yang diinginkan (19/2018) kemudian klik "CSV".</li>
		        <li>Untuk mengunduh laporan penjualan per "Bulan",<br> silahkan klik salah satu tanggal yang diinginkan (jan/) kemudian klik "CSV".</li>
		      </lo>
		    </p>
		  </div>
		  <input style="float:left;" type="<?php echo $shf;?>" id="filterData" size="15" onkeyup="fTgl()" placeholder="Filter Tanggal" title="Filter tanggal penjualan">
		  <button class="btnsubmit" onclick="exportTableToCSV('laporan-mikhmon-<?php echo $filedownload;?>.csv')" title="Download laporan penjualan">CSV</button>
		  <button class="btnsubmit" onclick="location.href='./penjualan.php';" title="Reload semua data penjualan">ALL</button>
		  <input style="float:left;" type="<?php echo $shd;?>" name="remdata" class="btnsubmit" onclick="location.href='#remdata';" title="Hapus Data <?php echo $filedownload;?>" value="Hapus data <?php echo $filedownload;?>"><br>
			<table id="laporan" style="white-space: nowrap;" class="zebra" >
				<tr>
				  <th colspan=2 >Laporan Penjualan <?php echo $filedownload;?><b style="font-size:0;">,</b></th>
				  <th style="text-align:right;">Total</b></th>
				  <th style="text-align:right;" id="total"></th>
				</tr>
				<tr>
					<th >Tanggal</th>
					<th >Pukul</th>
					<th >User</th>
					<th style="text-align:right;">Harga</th>
				</tr>
				<?php
					$TotalReg = count($ARRAY);

						for ($i=0; $i<$TotalReg; $i++){
						  $regtable = $ARRAY[$i];
						  echo "<tr>";
							echo "<td>";
							$getname = explode("-|-",$regtable['name']);
							$getowner = $regtable['owner'];
							$tgl = $getname[0];
							$getdy = explode("/",$tgl);
							$m = $getdy[0];
							$dy = $getdy[1]."/".$getdy[2];
							echo "<a style='color:#000;' href=?idbl=".$getowner ." title='Filter penjualan bulan : ".$getowner."'>$m/</a><a style='color:#000;' href=?idhr=".$tgl ." title='Filter penjualan tangal : ".$tgl."'>$dy</a>";
							echo "</td>";
							echo "<td>";
							$ltime = $getname[1];
							echo $ltime;
							echo "</td>";
							echo "<td>";
							$username = $getname[2];
							echo $username;
							echo "</td>";
							echo "<td style='text-align:right;'>";
							$price = $getname[3];
							echo $price;
							echo "</td>";
							echo "</tr>";
							}
				?>
			</table>
		</div>
	</div>
	<div id="remdata" class="modal-window">
		  <div>
			<a style="font-wight:bold;"href="#" title="Close" class="modal-close">X</a>
			<h3>Peringatan</h3>
	<?php
	echo "<div style='overflow-x:auto;'>";
	echo "<p>Yakin akan menghapus data penjualan<br> $filedownload</p>";

	echo "<form autocomplete='off' method='post' action=''>";
	echo "<center>";
	echo "<input type='submit' name='remdata' title='Yes' class='btnsubmit' value='Yes'/>";
	echo "<a class='btnsubmit' href='#' title='No'>No</a>";
	echo "</center>";
	echo "</form>";
	
	echo "</div>";

  ?>
    </div>
	<script>
	function fTgl() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("filterData");
  filter = input.value.toUpperCase();
  table = document.getElementById("laporan");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
	</script>
	</body>
</html>


File: /mikhmon\app\reboot.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/reboot');
  $API->read();
	$API->disconnect();
}
session_destroy();
header("Location: login.php");
?>


File: /mikhmon\app\resetcolor.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");



}else{
$my_file = 'css/vcolors.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $header=""; $note=""; $userpass=""; $details=""; $price=""; $font1=""; $font2=""; $font3=""; $font4=""; $font5=""; ?>';
		fwrite($handle, $data);
		header("Location:vcolorconf.php");
}
?>


File: /mikhmon\app\resetconfig.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");


}else{
$my_file = 'config.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data ='<?php $iphost=""; $userhost=""; $passwdhost=""; $useradm="admin"; $passadm="1234"; $reloadindex="15"; $profile1="Voucher3Jam"; $profile2="Voucher1Hari"; $profile3="Voucher2Hari"; $profile4="Voucher7Hari"; $profile5="Voucher30Hari"; $profile6=""; $profile7=""; $profile8=""; $profile9=""; $profile10=""; $profile11=""; $profile12=""; $profile13=""; $profile14=""; $profile15=""; $uactive1="3h"; $uactive2="1d"; $uactive3="2d"; $uactive4="7d"; $uactive5="30d"; $uactive6=""; $uactive7=""; $uactive8=""; $uactive9=""; $uactive10=""; $uactive11=""; $uactive12=""; $uactive13=""; $uactive14=""; $uactive15=""; $vname1="3Jam"; $vname2="1Hari"; $vname3="2Hari"; $vname4="7Hari"; $vname5="30Hari"; $vname6=""; $vname7=""; $vname8=""; $vname9=""; $vname10="";  $vname11=""; $vname12=""; $vname13=""; $vname14=""; $vname15=""; $utimelimit1="1h"; $utimelimit2="2h"; $utimelimit3="5h"; $utimelimit4="10h"; $utimelimit5="12h"; $utimelimit6=""; $utimelimit7="";  $utimelimit8=""; $utimelimit9=""; $utimelimit10=""; $utimelimit1t="1Jam"; $utimelimit2t="2Jam"; $utimelimit3t="5Jam"; $utimelimit4t="10Jam"; $utimelimit5t=""; $utimelimit6t=""; $utimelimit7t=""; $utimelimit8t=""; $utimelimit9t=""; $utimelimit10t=""; $ubytelimit1="500000000"; $ubytelimit2="1000000000"; $ubytelimit3="2000000000"; $ubytelimit4="5000000000"; $ubytelimit5="10000000000"; $ubytelimit6=""; $ubytelimit7="";  $ubytelimit8=""; $ubytelimit9=""; $ubytelimit10=""; $ubytelimit1t="500MB"; $ubytelimit2t="1GB"; $ubytelimit3t="2GB"; $ubytelimit4t="5GB"; $ubytelimit5t="10GB"; $ubytelimit6t=""; $ubytelimit7t=""; $ubytelimit8t=""; $ubytelimit9t=""; $ubytelimit10t=""; $price1="Rp1.000"; $price2="Rp3.000"; $price3="Rp5.000"; $price4="Rp15.000"; $price5="Rp35.000"; $price6=""; $price7=""; $price8=""; $price9=""; $price10="";  $price11=""; $price12=""; $price13=""; $price14=""; $price15=""; $headerv="Kemangi 41"; $notev="k41.net"; ?>';
		fwrite($handle, $data);
		$my_file1 = '../status/config.php';
		$handle1 = fopen($my_file1, 'w') or die('Cannot open file:  '.$my_file1);
		$data1 = '<?php $iphost=""; $userhost=""; $passwdhost=""; $headerv="Kemangi41"; ?>';
		fwrite($handle1, $data1);
 	session_destroy();
 	header("Location: login.php");
}
?>


File: /mikhmon\app\setup.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}

$API = new RouterosAPI();
$API->debug = false;

?>
<?php
  // Cek OTA Update
  if(isset($_POST['btnupdate'])){
   copy("http://laksa.mooo.com/ota-update/app/build.txt","build.txt");
   copy("http://laksa.mooo.com/ota-update/app/otaupdate.dat","otaupdate.php");
   echo "<script>location.href='otaupdate.php';</script>";
  }
  

?>
<?php

	if(isset($_POST['setup'])){
	  $setupdata = ($_POST['setupdata']);
		$siphost = ($_POST['ipmik']);
		$suserhost = ($_POST['usermik']);
		$spasswdhost = ($_POST['passmik']);
		$suseradm = ($_POST['useradm']);
		$spassadm = ($_POST['passadm']);
		$sprofile1 = ($_POST['prof1']);
		$sprofile2 = ($_POST['prof2']);
		$sprofile3 = ($_POST['prof3']);
		$sprofile4 = ($_POST['prof4']);
		$sprofile5 = ($_POST['prof5']);
		$sprofile6 = ($_POST['prof6']);
		$sprofile7 = ($_POST['prof7']);
		$sprofile8 = ($_POST['prof8']);
		$sprofile9 = ($_POST['prof9']);
		$sprofile10 = ($_POST['prof10']);
		$sprofile11 = ($_POST['prof11']);
		$sprofile12 = ($_POST['prof12']);
		$sprofile13 = ($_POST['prof13']);
		$sprofile14 = ($_POST['prof14']);
		$sprofile15 = ($_POST['prof15']);
		$sheaderv = ($_POST['namahotspot']);
		$snotev = ($_POST['notev']);
		$sreloadindex = ($_POST['reloadindex']);
		$h="Jam";
		$d="Hari";
// Title Masa Aktif
		$active1 = ($_POST['active1']);
			if (substr($active1, -1) == "h"){
				$uactiv = substr($active1, 0,-1);
				$suactive1t = $uactiv ."". $h;
			}elseif (substr($active1, -1) == "d"){
				$uactiv = substr($active1, 0,-1);
				$suactive1t = $uactiv ."". $d;
			}
		$active2 = ($_POST['active2']);
			if (substr($active2, -1) == "h"){
				$uactiv = substr($active2, 0,-1);
				$suactive2t = $uactiv ."". $h;
			}elseif (substr($active2, -1) == "d"){
				$uactiv = substr($active2, 0,-1);
				$suactive2t = $uactiv ."". $d;
			}
		$active3 = ($_POST['active3']);
			if (substr($active3, -1) == "h"){
				$uactiv = substr($active3, 0,-1);
				$suactive3t = $uactiv ."". $h;
			}elseif (substr($active3, -1) == "d"){
				$uactiv = substr($active3, 0,-1);
				$suactive3t = $uactiv ."". $d;
			}
		$active4 = ($_POST['active4']);
			if (substr($active4, -1) == "h"){
				$uactiv = substr($active4, 0,-1);
				$suactive4t = $uactiv ."". $h;
			}elseif (substr($active4, -1) == "d"){
				$uactiv = substr($active4, 0,-1);
				$suactive4t = $uactiv ."". $d;
			}
		$active5 = ($_POST['active5']);
			if (substr($active5, -1) == "h"){
				$uactiv = substr($active5, 0,-1);
				$suactive5t = $uactiv ."". $h;
			}elseif (substr($active5, -1) == "d"){
				$uactiv = substr($active5, 0,-1);
				$suactive5t = $uactiv ."". $d;
			}
		$active6 = ($_POST['active6']);
			if (substr($active6, -1) == "h"){
				$uactiv = substr($active6, 0,-1);
				$suactive6t = $uactiv ."". $h;
			}elseif (substr($active6, -1) == "d"){
				$uactiv = substr($active6, 0,-1);
				$suactive6t = $uactiv ."". $d;
			}
		$active7 = ($_POST['active7']);
			if (substr($active7, -1) == "h"){
				$uactiv = substr($active7, 0,-1);
				$suactive7t = $uactiv ."". $h;
			}elseif (substr($active7, -1) == "d"){
				$uactiv = substr($active7, 0,-1);
				$suactive7t = $uactiv ."". $d;
			}
		$active8 = ($_POST['active8']);
			if (substr($active8, -1) == "h"){
				$uactiv = substr($active8, 0,-1);
				$suactive8t = $uactiv ."". $h;
			}elseif (substr($active8, -1) == "d"){
				$uactiv = substr($active8, 0,-1);
				$suactive8t = $uactiv ."". $d;
			}
		$active9 = ($_POST['active9']);
			if (substr($active9, -1) == "h"){
				$uactiv = substr($active9, 0,-1);
				$suactive9t = $uactiv ."". $h;
			}elseif (substr($active9, -1) == "d"){
				$uactiv = substr($active9, 0,-1);
				$suactive9t = $uactiv ."". $d;
			}
		$active10 = ($_POST['active10']);
			if (substr($active10, -1) == "h"){
				$uactiv = substr($active10, 0,-1);
				$suactive10t = $uactiv ."". $h;
			}elseif (substr($active10, -1) == "d"){
				$uactiv = substr($active10, 0,-1);
				$suactive10t = $uactiv ."". $d;
			}
		$active11 = ($_POST['active11']);
			if (substr($active11, -1) == "h"){
				$uactiv = substr($active11, 0,-1);
				$suactive11t = $uactiv ."". $h;
			}elseif (substr($active11, -1) == "d"){
				$uactiv = substr($active11, 0,-1);
				$suactive11t = $uactiv ."". $d;
			}
		$active12 = ($_POST['active12']);
			if (substr($active12, -1) == "h"){
				$uactiv = substr($active12, 0,-1);
				$suactive12t = $uactiv ."". $h;
			}elseif (substr($active12, -1) == "d"){
				$uactiv = substr($active12, 0,-1);
				$suactive12t = $uactiv ."". $d;
			}
		$active13 = ($_POST['active13']);
			if (substr($active13, -1) == "h"){
				$uactiv = substr($active13, 0,-1);
				$suactive13t = $uactiv ."". $h;
			}elseif (substr($active13, -1) == "d"){
				$uactiv = substr($active13, 0,-1);
				$suactive13t = $uactiv ."". $d;
			}
		$active14 = ($_POST['active14']);
			if (substr($active14, -1) == "h"){
				$uactiv = substr($active14, 0,-1);
				$suactive14t = $uactiv ."". $h;
			}elseif (substr($active14, -1) == "d"){
				$uactiv = substr($active14, 0,-1);
				$suactive14t = $uactiv ."". $d;
			}
		$active15 = ($_POST['active15']);
			if (substr($active15, -1) == "h"){
				$uactiv = substr($active15, 0,-1);
				$suactive15t = $uactiv ."". $h;
			}elseif (substr($active15, -1) == "d"){
				$uactiv = substr($active15, 0,-1);
				$suactive15t = $uactiv ."". $d;
			}
// Title Durasi
		$tlimit1 = ($_POST['durasi1']);
			if (substr($tlimit1, -1) == "h"){
				$timel = substr($tlimit1, 0,-1);
				$stimelimit1t = $timel ."". $h;
			}elseif (substr($tlimit1, -1) == "d"){
				$timel = substr($tlimit1, 0,-1);
				$stimelimit1t = $timel ."". $d;
			}
		$tlimit2 = ($_POST['durasi2']);
			if (substr($tlimit2, -1) == "h"){
				$timel = substr($tlimit2, 0,-1);
				$stimelimit2t = $timel ."". $h;
			}elseif (substr($tlimit2, -1) == "d"){
				$timel = substr($tlimit2, 0,-1);
				$stimelimit2t = $timel ."". $d;
			}
		$tlimit3 = ($_POST['durasi3']);
			if (substr($tlimit3, -1) == "h"){
				$timel = substr($tlimit3, 0,-1);
				$stimelimit3t = $timel ."". $h;
			}elseif (substr($tlimit3, -1) == "d"){
				$timel = substr($tlimit3, 0,-1);
				$stimelimit3t = $timel ."". $d;
			}
		$tlimit4 = ($_POST['durasi4']);
			if (substr($tlimit4, -1) == "h"){
				$timel = substr($tlimit4, 0,-1);
				$stimelimit4t = $timel ."". $h;
			}elseif (substr($tlimit4, -1) == "d"){
				$timel = substr($tlimit4, 0,-1);
				$stimelimit4t = $timel ."". $d;
			}
		$tlimit5 = ($_POST['durasi5']);
			if (substr($tlimit5, -1) == "h"){
				$timel = substr($tlimit5, 0,-1);
				$stimelimit5t = $timel ."". $h;
			}elseif (substr($tlimit5, -1) == "d"){
				$timel = substr($tlimit5, 0,-1);
				$stimelimit5t = $timel ."". $d;
			}
		$tlimit6 = ($_POST['durasi6']);
			if (substr($tlimit6, -1) == "h"){
				$timel = substr($tlimit6, 0,-1);
				$stimelimit6t = $timel ."". $h;
			}elseif (substr($tlimit6, -1) == "d"){
				$timel = substr($tlimit6, 0,-1);
				$stimelimit6t = $timel ."". $d;
			}
		$tlimit7 = ($_POST['durasi7']);
			if (substr($tlimit7, -1) == "h"){
				$timel = substr($tlimit7, 0,-1);
				$stimelimit7t = $timel ."". $h;
			}elseif (substr($tlimit7, -1) == "d"){
				$timel = substr($tlimit7, 0,-1);
				$stimelimit7t = $timel ."". $d;
			}
		$tlimit8 = ($_POST['durasi8']);
			if (substr($tlimit8, -1) == "h"){
				$timel = substr($tlimit8, 0,-1);
				$stimelimit8t = $timel ."". $h;
			}elseif (substr($tlimit8, -1) == "d"){
				$timel = substr($tlimit8, 0,-1);
				$stimelimit8t = $timel ."". $d;
			}
		$tlimit9 = ($_POST['durasi9']);
			if (substr($tlimit9, -1) == "h"){
				$timel = substr($tlimit9, 0,-1);
				$stimelimit9t = $timel ."". $h;
			}elseif (substr($tlimit9, -1) == "d"){
				$timel = substr($tlimit9, 0,-1);
				$stimelimit9t = $timel ."". $d;
			}
		$tlimit10 = ($_POST['durasi10']);
			if (substr($tlimit10, -1) == "h"){
				$timel = substr($tlimit10, 0,-1);
				$stimelimit10t = $timel ."". $h;
			}elseif (substr($tlimit10, -1) == "d"){
				$timel = substr($tlimit10, 0,-1);
				$stimelimit10t = $timel ."". $d;
			}
// Kuota
		$MB="000000";
		$GB="000000000";
		$blimit1 = ($_POST['kuota1']);
			if (substr($blimit1, -2) == "MB"){
				$bytel = substr($blimit1, 0,-2);
				$bytelimit1 = $bytel."". $MB;
			}elseif (substr($blimit1, -2) == "GB"){
				$bytel = substr($blimit1, 0,-2);
				$bytelimit1 = $bytel ."". $GB;
			}
		$blimit2 = ($_POST['kuota2']);
			if (substr($blimit2, -2) == "MB"){
				$bytel = substr($blimit2, 0,-2);
				$bytelimit2 = $bytel."". $MB;
			}elseif (substr($blimit2, -2) == "GB"){
				$bytel = substr($blimit2, 0,-2);
				$bytelimit2 = $bytel ."". $GB;
			}
		$blimit3 = ($_POST['kuota3']);
			if (substr($blimit3, -2) == "MB"){
				$bytel = substr($blimit3, 0,-2);
				$bytelimit3 = $bytel."". $MB;
			}elseif (substr($blimit3, -2) == "GB"){
				$bytel = substr($blimit3, 0,-2);
				$bytelimit3 = $bytel ."". $GB;
			}
		$blimit4 = ($_POST['kuota4']);
			if (substr($blimit4, -2) == "MB"){
				$bytel = substr($blimit4, 0,-2);
				$bytelimit4 = $bytel."". $MB;
			}elseif (substr($blimit4, -2) == "GB"){
				$bytel = substr($blimit4, 0,-2);
				$bytelimit4 = $bytel ."". $GB;
			}
		$blimit5 = ($_POST['kuota5']);
			if (substr($blimit5, -2) == "MB"){
				$bytel = substr($blimit5, 0,-2);
				$bytelimit5 = $bytel."". $MB;
			}elseif (substr($blimit5, -2) == "GB"){
				$bytel = substr($blimit5, 0,-2);
				$bytelimit5 = $bytel ."". $GB;
			}
		$blimit6 = ($_POST['kuota6']);
			if (substr($blimit6, -2) == "MB"){
				$bytel = substr($blimit6, 0,-2);
				$bytelimit6 = $bytel."". $MB;
			}elseif (substr($blimit6, -2) == "GB"){
				$bytel = substr($blimit6, 0,-2);
				$bytelimit6 = $bytel ."". $GB;
			}
		$blimit7 = ($_POST['kuota7']);
			if (substr($blimit7, -2) == "MB"){
				$bytel = substr($blimit7, 0,-2);
				$bytelimit7 = $bytel."". $MB;
			}elseif (substr($blimit7, -2) == "GB"){
				$bytel = substr($blimit7, 0,-2);
				$bytelimit7 = $bytel ."". $GB;
			}
		$blimit8 = ($_POST['kuota8']);
			if (substr($blimit8, -2) == "MB"){
				$bytel = substr($blimit8, 0,-2);
				$bytelimit8 = $bytel."". $MB;
			}elseif (substr($blimit8, -2) == "GB"){
				$bytel = substr($blimit8, 0,-2);
				$bytelimit8 = $bytel ."". $GB;
			}
		$blimit9 = ($_POST['kuota9']);
			if (substr($blimit9, -2) == "MB"){
				$bytel = substr($blimit9, 0,-2);
				$bytelimit9 = $bytel."". $MB;
			}elseif (substr($blimit9, -2) == "GB"){
				$bytel = substr($blimit9, 0,-2);
				$bytelimit9 = $bytel ."". $GB;
			}
		$blimit10 = ($_POST['kuota10']);
			if (substr($blimit10, -2) == "MB"){
				$bytel = substr($blimit10, 0,-2);
				$bytelimit10 = $bytel."". $MB;
			}elseif (substr($blimit10, -2) == "GB"){
				$bytel = substr($blimit10, 0,-2);
				$bytelimit10 = $bytel ."". $GB;
			}
		// Simpan Local
		if($setupdata == "local"){
		$my_file = 'config.php';
		$my_file1 = '../status/config.php';
		
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$handle1 = fopen($my_file1, 'w') or die('Cannot open file:  '.$my_file1);
		
		$data = '<?php $iphost="'.$siphost.'"; $userhost="'.$suserhost.'"; $passwdhost="'.$spasswdhost.'"; $useradm="'.$suseradm.'"; $passadm="'.$spassadm.'"; $reloadindex="'.$sreloadindex.'"; $profile1="'.$sprofile1.'"; $profile2="'.$sprofile2.'"; $profile3="'.$sprofile3.'"; $profile4="'.$sprofile4.'"; $profile5="'.$sprofile5.'"; $profile6="'.$sprofile6.'"; $profile7="'.$sprofile7.'"; $profile8="'.$sprofile8.'"; $profile9="'.$sprofile9.'"; $profile10="'.$sprofile10.'"; $profile11="'.$sprofile11.'"; $profile12="'.$sprofile12.'"; $profile13="'.$sprofile13.'"; $profile14="'.$sprofile14.'"; $profile15="'.$sprofile15.'"; $uactive1="'.$active1.'"; $uactive2="'.$active2.'"; $uactive3="'.$active3.'"; $uactive4="'.$active4.'"; $uactive5="'.$active5.'"; $uactive6="'.$active6.'"; $uactive7="'.$active7.'"; $uactive8="'.$active8.'"; $uactive9="'.$active9.'"; $uactive10="'.$active10.'"; $uactive11="'.$active11.'"; $uactive12="'.$active12.'"; $uactive13="'.$active13.'"; $uactive14="'.$active14.'"; $uactive15="'.$active15.'"; $vname1="'.$suactive1t.'"; $vname2="'.$suactive2t.'"; $vname3="'.$suactive3t.'"; $vname4="'.$suactive4t.'"; $vname5="'.$suactive5t.'"; $vname6="'.$suactive6t.'"; $vname7="'.$suactive7t.'"; $vname8="'.$suactive8t.'"; $vname9="'.$suactive9t.'"; $vname10="'.$suactive10t.'";  $vname11="'.$suactive11t.'"; $vname12="'.$suactive12t.'"; $vname13="'.$suactive13t.'"; $vname14="'.$suactive14t.'"; $vname15="'.$suactive15t.'"; $utimelimit1="'.$tlimit1.'"; $utimelimit2="'.$tlimit2.'"; $utimelimit3="'.$tlimit3.'"; $utimelimit4="'.$tlimit4.'"; $utimelimit5="'.$tlimit5.'"; $utimelimit6="'.$tlimit6.'"; $utimelimit7="'.$tlimit7.'";  $utimelimit8="'.$tlimit8.'"; $utimelimit9="'.$tlimit9.'"; $utimelimit10="'.$tlimit10.'"; $utimelimit1t="'.$stimelimit1t.'"; $utimelimit2t="'.$stimelimit2t.'"; $utimelimit3t="'.$stimelimit3t.'"; $utimelimit4t="'.$stimelimit4t.'"; $utimelimit5t="'.$stimelimit5t.'"; $utimelimit6t="'.$stimelimit6t.'"; $utimelimit7t="'.$stimelimit7t.'"; $utimelimit8t="'.$stimelimit8t.'"; $utimelimit9t="'.$stimelimit9t.'"; $utimelimit10t="'.$stimelimit10t.'"; $ubytelimit1="'.$bytelimit1.'"; $ubytelimit2="'.$bytelimit2.'"; $ubytelimit3="'.$bytelimit3.'"; $ubytelimit4="'.$bytelimit4.'"; $ubytelimit5="'.$bytelimit5.'"; $ubytelimit6="'.$bytelimit6.'"; $ubytelimit7="'.$bytelimit7.'";  $ubytelimit8="'.$bytelimit8.'"; $ubytelimit9="'.$bytelimit9.'"; $ubytelimit10="'.$bytelimit10.'"; $ubytelimit1t="'.$blimit1.'"; $ubytelimit2t="'.$blimit2.'"; $ubytelimit3t="'.$blimit3.'"; $ubytelimit4t="'.$blimit4.'"; $ubytelimit5t="'.$blimit5.'"; $ubytelimit6t="'.$blimit6.'"; $ubytelimit7t="'.$blimit7.'"; $ubytelimit8t="'.$blimit8.'"; $ubytelimit9t="'.$blimit9.'"; $ubytelimit10t="'.$blimit10.'"; $headerv="'.$sheaderv.'"; $notev="'.$snotev.'"; ?>';
		
		$data1 = '<?php  $iphost="'.$siphost.'"; $userhost="'.$suserhost.'"; $passwdhost="'.$spasswdhost.'"; $headerv="'.$sheaderv.'";?>';
		
	
		fwrite($handle, $data);
		fwrite($handle1, $data1);
	// Export ke Mikrotik
	}elseif($setupdata == "export"){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	   $arrID=$API->comm("/system/script/getall",
						  array(
				  ".proplist"=> ".id",
				  "?name" => "mikhmon",
				  ));
	  $API->comm("/system/script/remove", array(
	    ".id" => $arrID[0][".id"],
	    ));
	    $API->disconnect();
	}
	  
  $export = "$sreloadindex-|-$sheaderv-|-$snotev-|-$sprofile1-|-$sprofile2-|-$sprofile3-|-$sprofile4-|-$sprofile5-|-$sprofile6-|-$sprofile7-|-$sprofile8-|-$sprofile9-|-$sprofile10-|-$sprofile11-|-$sprofile12-|-$sprofile13-|-$sprofile14-|-$sprofile15-|-$active1-|-$active2-|-$active3-|-$active4-|-$active5-|-$active6-|-$active7-|-$active8-|-$active9-|-$active10-|-$active11-|-$active12-|-$active13-|-$active14-|-$active15-|-$tlimit1-|-$tlimit2-|-$tlimit3-|-$tlimit4-|-$tlimit5-|-$tlimit6-|-$tlimit7-|-$tlimit8-|-$tlimit9-|-$tlimit10-|-$bytelimit1-|-$bytelimit2-|-$bytelimit3-|-$bytelimit4-|-$bytelimit5-|-$bytelimit6-|-$bytelimit7-|-$bytelimit8-|-$bytelimit9-|-$bytelimit10-|-$blimit1-|-$blimit2-|-$blimit3-|-$blimit4-|-$blimit5-|-$blimit6-|-$blimit7-|-$blimit8-|-$blimit9-|-$blimit10-|-$suactive1t-|-$suactive2t-|-$suactive3t-|-$suactive4t-|-$suactive5t-|-$suactive6t-|-$suactive7t-|-$suactive8t-|-$suactive9t-|-$suactive10t-|-$suactive11t-|-$suactive12t-|-$suactive13t-|-$suactive14t-|-$suactive15t-|-$stimelimit1t-|-$stimelimit2t-|-$stimelimit3t-|-$stimelimit4t-|-$stimelimit5t-|-$stimelimit6t-|-$stimelimit7t-|-$stimelimit8t-|-$stimelimit9t-|-$stimelimit10t";
  
  if ($API->connect($iphost, $userhost, $passwdhost)) {
  $API->comm("/system/script/add", array(
					  "name" => "mikhmon",
					  "source" => "$export",
			));
  }
//Import dari Mikrotik
	}elseif($setupdata == "import"){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/script/print', false);
	$API->write('?=name=mikhmon');
	$ARRAY = $API->read();
	}
  $regtable = $ARRAY[0];
  $import = $regtable['source'];
  if($import == ""){}else{
  $importl = explode("-|-",$import);
   $sreloadindex = $importl[0];
   $sheaderv = $importl[1];
   $snotev = $importl[2];
   $sprofile1 = $importl[3];
   $sprofile2 = $importl[4];
   $sprofile3 = $importl[5];
   $sprofile4 = $importl[6];
   $sprofile5 = $importl[7];
   $sprofile6 = $importl[8];
   $sprofile7 = $importl[9];
   $sprofile8 = $importl[10];
   $sprofile9 = $importl[11];
   $sprofile10 = $importl[12];
   $sprofile11 = $importl[13];
   $sprofile12 = $importl[14];
   $sprofile13 = $importl[15];
   $sprofile14 = $importl[16];
   $sprofile15 = $importl[17];
   $active1 = $importl[18];
   $active2 = $importl[19];
   $active3 = $importl[20];
   $active4 = $importl[21];
   $active5 = $importl[22];
   $active6 = $importl[23];
   $active7 = $importl[24];
   $active8 = $importl[25];
   $active9 = $importl[26];
   $active10 = $importl[27];
   $active11 = $importl[28];
   $active12 = $importl[29];
   $active13 = $importl[30];
   $active14 = $importl[31];
   $active15 = $importl[32];
   $tlimit1 = $importl[33];
   $tlimit2 = $importl[34];
   $tlimit3 = $importl[35];
   $tlimit4 = $importl[36];
   $tlimit5 = $importl[37];
   $tlimit6 = $importl[38];
   $tlimit7 = $importl[39];
   $tlimit8 = $importl[40];
   $tlimit9 = $importl[41];
   $tlimit10 = $importl[42];
   $bytelimit1 = $importl[43];
   $bytelimit2 = $importl[44];
   $bytelimit3 = $importl[45];
   $bytelimit4 = $importl[46];
   $bytelimit5 = $importl[47];
   $bytelimit6 = $importl[48];
   $bytelimit7 = $importl[49];
   $bytelimit8 = $importl[50];
   $bytelimit9 = $importl[51];
   $bytelimit10 = $importl[52];
   $blimit1 = $importl[53];
   $blimit2 = $importl[54];
   $blimit3 = $importl[55];
   $blimit4 = $importl[56];
   $blimit5 = $importl[57];
   $blimit6 = $importl[58];
   $blimit7 = $importl[59];
   $blimit8 = $importl[60];
   $blimit9 = $importl[61];
   $blimit10 = $importl[62];
   $suactive1t = $importl[63];
   $suactive2t = $importl[64];
   $suactive3t = $importl[65];
   $suactive4t = $importl[66];
   $suactive5t = $importl[67];
   $suactive6t = $importl[68];
   $suactive7t = $importl[69];
   $suactive8t = $importl[70];
   $suactive9t = $importl[71];
   $suactive10t = $importl[72];
   $suactive11t = $importl[73];
   $suactive12t = $importl[74];
   $suactive13t = $importl[75];
   $suactive14t = $importl[76];
   $suactive15t = $importl[77];
   $stimelimit1t = $importl[78];
   $stimelimit2t = $importl[70];
	 $stimelimit3t = $importl[80];
	 $stimelimit4t = $importl[81];
	 $stimelimit5t = $importl[82];
	 $stimelimit6t = $importl[83];
	 $stimelimit7t = $importl[84];
	 $stimelimit8t = $importl[85];
	 $stimelimit9t = $importl[86];
	 $stimelimit10t = $importl[87];
	  $my_file = 'config.php';
		$my_file1 = '../status/config.php';
		
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);

		$data = '<?php $iphost="'.$siphost.'"; $userhost="'.$suserhost.'"; $passwdhost="'.$spasswdhost.'"; $useradm="'.$suseradm.'"; $passadm="'.$spassadm.'"; $reloadindex="'.$sreloadindex.'"; $profile1="'.$sprofile1.'"; $profile2="'.$sprofile2.'"; $profile3="'.$sprofile3.'"; $profile4="'.$sprofile4.'"; $profile5="'.$sprofile5.'"; $profile6="'.$sprofile6.'"; $profile7="'.$sprofile7.'"; $profile8="'.$sprofile8.'"; $profile9="'.$sprofile9.'"; $profile10="'.$sprofile10.'"; $profile11="'.$sprofile11.'"; $profile12="'.$sprofile12.'"; $profile13="'.$sprofile13.'"; $profile14="'.$sprofile14.'"; $profile15="'.$sprofile15.'"; $uactive1="'.$active1.'"; $uactive2="'.$active2.'"; $uactive3="'.$active3.'"; $uactive4="'.$active4.'"; $uactive5="'.$active5.'"; $uactive6="'.$active6.'"; $uactive7="'.$active7.'"; $uactive8="'.$active8.'"; $uactive9="'.$active9.'"; $uactive10="'.$active10.'"; $uactive11="'.$active11.'"; $uactive12="'.$active12.'"; $uactive13="'.$active13.'"; $uactive14="'.$active14.'"; $uactive15="'.$active15.'"; $vname1="'.$suactive1t.'"; $vname2="'.$suactive2t.'"; $vname3="'.$suactive3t.'"; $vname4="'.$suactive4t.'"; $vname5="'.$suactive5t.'"; $vname6="'.$suactive6t.'"; $vname7="'.$suactive7t.'"; $vname8="'.$suactive8t.'"; $vname9="'.$suactive9t.'"; $vname10="'.$suactive10t.'";  $vname11="'.$suactive11t.'"; $vname12="'.$suactive12t.'"; $vname13="'.$suactive13t.'"; $vname14="'.$suactive14t.'"; $vname15="'.$suactive15t.'"; $utimelimit1="'.$tlimit1.'"; $utimelimit2="'.$tlimit2.'"; $utimelimit3="'.$tlimit3.'"; $utimelimit4="'.$tlimit4.'"; $utimelimit5="'.$tlimit5.'"; $utimelimit6="'.$tlimit6.'"; $utimelimit7="'.$tlimit7.'";  $utimelimit8="'.$tlimit8.'"; $utimelimit9="'.$tlimit9.'"; $utimelimit10="'.$tlimit10.'"; $utimelimit1t="'.$stimelimit1t.'"; $utimelimit2t="'.$stimelimit2t.'"; $utimelimit3t="'.$stimelimit3t.'"; $utimelimit4t="'.$stimelimit4t.'"; $utimelimit5t="'.$stimelimit5t.'"; $utimelimit6t="'.$stimelimit6t.'"; $utimelimit7t="'.$stimelimit7t.'"; $utimelimit8t="'.$stimelimit8t.'"; $utimelimit9t="'.$stimelimit9t.'"; $utimelimit10t="'.$stimelimit10t.'"; $ubytelimit1="'.$bytelimit1.'"; $ubytelimit2="'.$bytelimit2.'"; $ubytelimit3="'.$bytelimit3.'"; $ubytelimit4="'.$bytelimit4.'"; $ubytelimit5="'.$bytelimit5.'"; $ubytelimit6="'.$bytelimit6.'"; $ubytelimit7="'.$bytelimit7.'";  $ubytelimit8="'.$bytelimit8.'"; $ubytelimit9="'.$bytelimit9.'"; $ubytelimit10="'.$bytelimit10.'"; $ubytelimit1t="'.$blimit1.'"; $ubytelimit2t="'.$blimit2.'"; $ubytelimit3t="'.$blimit3.'"; $ubytelimit4t="'.$blimit4.'"; $ubytelimit5t="'.$blimit5.'"; $ubytelimit6t="'.$blimit6.'"; $ubytelimit7t="'.$blimit7.'"; $ubytelimit8t="'.$blimit8.'"; $ubytelimit9t="'.$blimit9.'"; $ubytelimit10t="'.$blimit10.'"; $headerv="'.$sheaderv.'"; $notev="'.$snotev.'"; ?>';
		
		fwrite($handle, $data);
	}
	}
  
  header('Location: setup.php');
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Setup Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<style>
table.tsetup {
  margin-left:auto;
  margin-right:auto;
  width: 100%;
  border-collapse: collapse;
}
table.tsetup th {
  background: #008CCA;
  color: white;
  font-weight: bold;
  text-align: center;
}
table.tsetup td {
  padding: 2px;
  border: 1px solid #ccc;
  text-align: center;
}
		</style>
		<script>
			function Reload() {
				location.reload();
			}
		</script>
		<script>
		function resetConfig() {
		var txt;
		var r = confirm("Yakin akan me-reset config?\n Username | Password default (admin | 1234)");
		if (r == true) {
			window.open("./resetconfig.php", "_self");
		} else {
			
		}
		}
		</script>
		<script>
		function rebootMikrotik() {
		var txt;
		var r = confirm("Mikrotik akan di-Reboot!\nYakin melakukannya?");
		if (r == true) {
			window.open("./reboot.php", "_self");
		} else {
			
		}
		}
		</script>
	</head>
	<body>
		<div class="main">
			<div style="overflow-x:auto;">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
				</tr>
				<tr>
					<td>Setup</td>
					<td>
						<button class="material-icons" onclick="Reload()"	title="Reload">autorenew</button>
						<button class="material-icons" onclick="rebootMikrotik()" title="Reboot Mikrotik">power_settings_new</button>
						<button class="material-icons"	onclick="location.href='logout.php';" 	title="Logout">lock</button>
						<button class="material-icons" onclick="resetConfig()" title="Reset Config">history</button>
						<button class="material-icons" onclick="location.href='conntest.php';" title="Tes Koneksi ke Mikrotik">settings_ethernet</button>
						<button class="material-icons"	onclick="location.href='./uprofileadd.php';"	title="User Profile">local_library</button>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<form  method="post"><input type="submit" name="btnupdate" class="material-icons"	title="Cek Update" value="system_update_alt"></form>
						<!--<button class="material-icons"	onclick="window.open('https://github.com/laksa19/mikrotik-hotspot-monitor','_blank');" 	title="Check Update">system_update_alt</button>-->
					</td>
				</tr>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tnav">
					<tr>
					  <td>
					  <select style="float:left;" name="setupdata" required="1">
							<option value="local">Local Server</option>
							<option value="export">Export ke Mikrotik</option>
							<option value="import">Import dari Mikrotik</option>
						</select>
						<input type="submit" class="btnsubmit" name="setup" value="Simpan"/>
					  </td>
					</tr>
				</table>
				<div style="overflow-x:auto;">
				<table class="tsetup" align="center"  >
					<tr>
						<th>IP</th>
						<th>Username</th>
						<th>Password</th>
					</tr>
					<tr>
					<td><input type="text" size="15" name="ipmik" placeholder="IP Mikrotik" value="<?php print_r($iphost);?>" required="1"/></td>
					<td><input type="text" size="10" name="usermik" placeholder="User Mikrotik" value="<?php print_r($userhost);?>" required="1"/></td>
					<td><input type="password" size="10" name="passmik" placeholder="Password Mikrotik" value="<?php print_r($passwdhost);?>" required="1"/></td>
					</tr>
					<tr>
					<td style="color:white; font-weight:bold; background:#008CCA;">User Pass Admin ==></td>
					<td><input type="text" size="10" name="useradm" placeholder="User Admin" value="<?php print_r($useradm);?>" required="1"/></td>
					<td><input type="password" size="10" name="passadm" placeholder="Password Admin" value="<?php print_r($passadm);?>" required="1"/></td>
					</tr>
					<tr>
						<td style="text-align:left" colspan=3>
						Ganti Username Password Admin untuk keamanan. <b style="color:red;">Disarankan  user Admin berbeda dengan user Mikrotik.</b>
						</td>
					</tr>
				</table>
				</div>
				<br>
				<div style="overflow-x:auto;">
				<table class="tsetup" align="center"  >
					<tr>
						<th>NAMA HOTSPOT</th>
						<th>DNS NAME</th>
						<th>AUTO RELOAD</th>
					</tr>
					<tr>
					<td><input type="text" size="15" maxlength="50" name="namahotspot" placeholder="Nama Hotspot" value="<?php print_r($headerv);?>" required="1"/></td>
					<td><input type="text" size="17" maxlength="500" name="notev" placeholder="Catatan Voucher" value="<?php print_r($notev);?>" required="1"/></td>
					<td><input type="text" size="3" maxlength="4" name="reloadindex" placeholder="Auto Reload Page" title="Reload otomatis laman index, dengan satuan detik" value="<?php print_r($reloadindex);?>" required="1"/></td>
					</tr>
					<tr>
						<td style="text-align:left" colspan=3>
						Auto Reload berfungsi untuk auto reload pada laman Dashbord, ditulis dalam satuan detik. Jika tidak dibutuhkan isi huruf [x] pada kolom Auto Reload.
						</td>
					</tr>
				</table>
				</div>
				<br>
				<div style="overflow-x:auto;">
				<table class="tsetup" align="center"  >
					<tr>
						<th colspan=2>USER PROFILE</th>
						<th colspan=2>USER LIMIT</th>
					</tr>
					<tr>
						<th>NAMA PROFILE</th>
						<th>MASA AKTIF</th>
						<!--<th>HARGA VOUCHER</th>-->
						<th>DURASI</th>
						<th>KUOTA</th>
					</tr>
					<tr>
						<td style="text-align:left" colspan=2>Profile Baris ke 1 di Dashboard</td>
						<td colspan=2></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof1" placeholder="Profile1" value="<?php print_r($profile1);?>" required="1"/></td>
						<td><input type="text" size="3" maxlength="3" name="active1" placeholder="Masa Aktif1" value="<?php print_r($uactive1);?>" required="1"/></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga1" placeholder="Harga Voucher1" value="<?php print_r($price1);?>" required="1"/></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi1"  value="<?php print_r($utimelimit1);?>" required="1"/></td>
						<td><input type="text" size="5" maxlength="5" name="kuota1"  value="<?php print_r($ubytelimit1t);?>" required="1"/></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof2" value="<?php print_r($profile2);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active2" value="<?php print_r($uactive2);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga2" value="<?php print_r($price2);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi2"  value="<?php print_r($utimelimit2);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota2"  value="<?php print_r($ubytelimit2t);?>" /></td>
						
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof3" value="<?php print_r($profile3);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active3" value="<?php print_r($uactive3);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga3" value="<?php print_r($price3);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi3"  value="<?php print_r($utimelimit3);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota3"  value="<?php print_r($ubytelimit3t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof4" value="<?php print_r($profile4);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active4" value="<?php print_r($uactive4);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga4" value="<?php print_r($price4);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi4"  value="<?php print_r($utimelimit4);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota4"  value="<?php print_r($ubytelimit4t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof5" value="<?php print_r($profile5);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active5" value="<?php print_r($uactive5);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga5" value="<?php print_r($price5);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi5"  value="<?php print_r($utimelimit5);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota5"  value="<?php print_r($ubytelimit5t);?>" /></td>
					</tr>
					<tr>
						<td style="text-align:left" colspan=2>Profile Baris ke 2 di Dashboard</td>
						<td colspan=2></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof6" value="<?php print_r($profile6);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active6" value="<?php print_r($uactive6);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga6" value="<?php print_r($price6);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi6"  value="<?php print_r($utimelimit6);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota6"  value="<?php print_r($ubytelimit6t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof7" value="<?php print_r($profile7);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active7" value="<?php print_r($uactive7);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga7" value="<?php print_r($price7);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi7"  value="<?php print_r($utimelimit7);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota7"  value="<?php print_r($ubytelimit7t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof8" value="<?php print_r($profile8);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active8" value="<?php print_r($uactive8);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga8" value="<?php print_r($price8);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi8"  value="<?php print_r($utimelimit8);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota8"  value="<?php print_r($ubytelimit8t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof9" value="<?php print_r($profile9);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active9" value="<?php print_r($uactive9);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga9" value="<?php print_r($price9);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi9"  value="<?php print_r($utimelimit9);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota9" value="<?php print_r($ubytelimit9t);?>" /></td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof10" value="<?php print_r($profile10);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active10" value="<?php print_r($uactive10);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga10" value="<?php print_r($price10);?>" /></td>-->
						<td><input type="text" size="5" maxlength="3" name="durasi10"  value="<?php print_r($utimelimit10);?>" /></td>
						<td><input type="text" size="5" maxlength="5" name="kuota10"  value="<?php print_r($ubytelimit10t);?>" /></td>
					</tr>
					<tr>
						<td style="text-align:left" colspan=2>Profile Baris ke 3 di Dashboard</td>
						<td style="text-align:left" valign="top" colspan=2 rowspan=7>
							Durasi dan Kuota adalah adalah opsi tambahan pada saat generate voucher. <br>Satuan Durasi : (h atau d) <br>Satuan Kuota : (MB atau GB).
						</td>
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof11" value="<?php print_r($profile11);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active11" value="<?php print_r($uactive11);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga11" value="<?php print_r($price11);?>" /></td>-->
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof12" value="<?php print_r($profile12);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active12" value="<?php print_r($uactive12);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga12" value="<?php print_r($price12);?>" /></td>-->
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof13" value="<?php print_r($profile13);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active13" value="<?php print_r($uactive13);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga13" value="<?php print_r($price13);?>" /></td>-->
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof14" value="<?php print_r($profile14);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active14" value="<?php print_r($uactive14);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga14" value="<?php print_r($price14);?>" /></td>-->
					</tr>
					<tr>
						<td><input type="text" size="15" maxlength="20" name="prof15" value="<?php print_r($profile15);?>" /></td>
						<td><input type="text" size="3" maxlength="3" name="active15" value="<?php print_r($uactive15);?>" /></td>
						<!--<td><input type="text" size="15" maxlength="20" name="harga15" value="<?php print_r($price15);?>" /></td>-->
					</tr>
					<tr>
						<td style="text-align:left" colspan=2>
							Nama Profile dan Masa Aktif dibuat linier, agar dapat mengnali masa aktif Profile dengan mudah. <br>Contoh: Profile 3Jam, Masa Aktif 3h (h=jam d=hari).<br><b style="color:red">Nama Profle tidak menggunakan spasi</b>
						</td>
						
					</tr>
			</table>
      </div>
			<br>
			</form>
	</body>
</html>


File: /mikhmon\app\uprofileadd.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$ARRAY = $API->comm("/ip/hotspot/user/profile/print");
	$API->disconnect();
}
// Remove Profile
  $id = $_GET['id'];
	if(isset($id)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->comm("/ip/hotspot/user/profile/remove", array(
	    ".id"=> "$id",));
	    $API->disconnect();
	    header("Location:uprofileadd.php");
	}
	}
	// Get Profile
  $name = $_GET['name'];
	if(isset($name)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY1 = $API->read();
	$regtable = $ARRAY1[0];
	  $profn = $regtable['name'];
	  $sharedu = $regtable['shared-users'];
	  $ratel = $regtable['rate-limit'];
	  
							$getmodeexp = explode(",",$regtable['on-login']);
							$modeexpu = $getmodeexp[1];
							if($modeexpu == "rem"){
							  $mdexpt = "Hapus";
							}elseif($modeexpu == "ntf"){
							  $mdexpt = "Notifikasi";
							}elseif($modeexpu == "remc"){
							  $mdexpt = "Hapus + Data";
							}elseif($modeexpu == "ntfc"){
							  $mdexpt = "Notifikasi + Data";
							}else{
							  $mdexpt = "No Expired";
							}
							
							$getonlogin = explode(",",$regtable['on-login']);
							$checkonlogin = $getonlogin[5];
							
							$getteng = explode(",",$regtable['on-login']);
							$tengu = $getteng[4];
							if(substr($tengu,-1) == "m"){
							  $tengut = substr($tengu,0,-1)."Menit";
							}elseif(substr($tengu,-1) == "h"){
							  $tengut = substr($tengu,0,-1)."Jam";
							}elseif(substr($tengu,-1) == "d"){
							  $tengut = substr($tengu,0,-1)."Hari";
							}else{
							  $tengu = "5m";
							}

							$getprice = explode(",",$regtable['on-login']);
							$priceu = trim($getprice[2]);

	  $API->disconnect();
	}
	}
	//Update Profile
  if(isset($_POST['profupdate'])){
  $nsharuser=($_POST['nsharedu']);
	$nrxtx = ($_POST['nupdown']);
	$mode = ($_POST['expmodeu']);
	$tenggangu = ($_POST['tengremu']);
	$priceu = ($_POST['nprice']);
	$id = $_GET['idp'];
	
	if ($profn == $profile1){
				$exptime = $uactive1;
			}elseif ($profn == $profile2){
				$exptime = $uactive2;
			}elseif ($profn == $profile3){
				$exptime = $uactive3;
			}elseif ($profn == $profile4){
				$exptime = $uactive4;
			}elseif ($profn == $profile5){
				$exptime = $uactive5;
			}elseif ($profn == $profile6){
				$exptime = $uactive6;
			}elseif ($profn == $profile7){
				$exptime = $uactive7;
			}elseif ($profn == $profile8){
				$exptime = $uactive8;
			}elseif ($profn == $profile9){
				$exptime = $uactive9;
			}elseif ($profn == $profile10){
				$exptime = $uactive10;
			}elseif ($profn == $profile11){
				$exptime = $uactive11;
			}elseif ($profn == $profile12){
				$exptime = $uactive12;
			}elseif ($profn == $profile13){
				$exptime = $uactive13;
			}elseif ($profn == $profile14){
				$exptime = $uactive14;
			}elseif ($profn == $profile15){
				$exptime = $uactive15;
			}else {
				$exptime = "x";
			}
	    $onlogin1 = ':put (",rem,'.$priceu.','.$exptime.','.$tenggangu.',"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$tenggangu.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"] }}';
			$onlogin2 = ':put (",ntf,'.$priceu.','.$exptime.',,"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time] }}';
			$onlogin3 = ':put (",remc,'.$priceu.','.$exptime.','.$tenggangu.',"); {:local price ('.$priceu.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$tenggangu.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[/system script add name="$date-|-$time-|-$user-|-$price" owner="$bln$thn" source=$date comment=mikhmon] }}';
			$onlogin4 = ':put (",ntfc,'.$priceu.','.$exptime.',,"); {:local price ('.$priceu.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[/system script add name="$date-|-$time-|-$user-|-$price" owner="$bln$thn" source=$date comment=mikhmon] }}';
			if($mode == "rem"){
			$onlogin = "$onlogin1";
			}elseif($mode == "ntf"){
			$onlogin = "$onlogin2";
			}elseif($mode == "remc"){
			$onlogin = "$onlogin3";
			}elseif($mode == "ntfc"){
			$onlogin = "$onlogin4";
			}else{
			$onlogin = ':put (",,,,,noexp,")';
			}
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  if($exptime == "x"){
	$arrID=$API->comm("/ip/hotspot/user/profile/getall",
						  array(
				  ".proplist"=> ".id",
				  "?name" => "$profn",
				  ));

			$API->comm("/ip/hotspot/user/profile/set",
				  array(
						  ".id" => $arrID[0][".id"],
						  /*"add-mac-cookie" => "yes",*/
						  "rate-limit" => "$nrxtx",
						  "shared-users" => "$nsharuser",
						 ));
	}else{
	  $arrID=$API->comm("/ip/hotspot/user/profile/getall",
						  array(
				  ".proplist"=> ".id",
				  "?name" => "$profn",
				  ));

			$API->comm("/ip/hotspot/user/profile/set",
				  array(
						  ".id" => $arrID[0][".id"],
						  /*"add-mac-cookie" => "yes",*/
						  "rate-limit" => "$nrxtx",
						  "shared-users" => "$nsharuser",
						  "on-login" => "$onlogin",
						 ));
	}
	}
	header("Location:uprofileadd.php#x");
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot User Profile</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>User Profile</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="location.href='uprofileadd.php';" title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./setup.php';" 	title="Edit Config">settings</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">find_in_page</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">User by profile</a>
									<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}
								?>
								</div>
						</div>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
					</td>
				</tr>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tnav" align="center"  >
					<tr><td>Profile | Masa Aktif</td><td>:</td><td>
					  <input type="text" placeholder="Pilih / Manual" name="nama" required="1" list="profilename">
					  <datalist id="profilename">
							<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<option>$proflist[$i]</option>";
									}
									}
								?>
						</datalist>
					</td></tr>
					<tr><td>Shared Users</td><td>:</td><td><input type="text" size="3" maxlength="3" name="sharedu" value="1" required="1"/></td></tr>
					<tr><td>Upload/Download</td><td>:</td><td><input type="text" size="12"  name="updown" placeholder="contoh:512k/1M" required="1"/></td></tr>
					<tr><td>Harga*</td><td>:</td><td><input type="text" size="12"  name="harga" placeholder="contoh:10000"/></td></tr>
					<tr><td>Mode Expired*</td><td>:</td><td>
						<select name="expmode" required="1">
							<option value="0">No Expired</option>
							<option value="rem">Hapus</option>
							<option value="ntf">Notifikasi</option>
							<option value="remc">Hapus + Data</option>
							<option value="ntfc">Notifikasi + Data</option>
						</select>
						</td>
						</tr>
						<tr><td>Tenggang Penghapusan*</td><td>:</td><td>
						<select name="tengrem" required="1">
						  <option value="5m">5Menit</option>
						  <option value="10m">10Menit</option>
							<option value="15m">15Menit</option>
							<option value="30m">30Menit</option>
							<option value="1h">1Jam</option>
							<option value="2Jam">2Jam</option>
						</select>
						</td>
						</tr>
					<tr><td></td><td></td><td><input type="submit" class="btnsubmit" value="Simpan"/></td></tr>
				</table>
			</form>
<?php
	if(isset($_POST['nama'])){
			$profname = ($_POST['nama']);
			$uprofile = $profname;
			if ($uprofile == $profile1){
				$exptime = $uactive1;
			}elseif ($uprofile == $profile2){
				$exptime = $uactive2;
			}elseif ($uprofile == $profile3){
				$exptime = $uactive3;
			}elseif ($uprofile == $profile4){
				$exptime = $uactive4;
			}elseif ($uprofile == $profile5){
				$exptime = $uactive5;
			}elseif ($uprofile == $profile6){
				$exptime = $uactive6;
			}elseif ($uprofile == $profile7){
				$exptime = $uactive7;
			}elseif ($uprofile == $profile8){
				$exptime = $uactive8;
			}elseif ($uprofile == $profile9){
				$exptime = $uactive9;
			}elseif ($uprofile == $profile10){
				$exptime = $uactive10;
			}elseif ($uprofile == $profile11){
				$exptime = $uactive11;
			}elseif ($uprofile == $profile12){
				$exptime = $uactive12;
			}elseif ($uprofile == $profile13){
				$exptime = $uactive13;
			}elseif ($uprofile == $profile14){
				$exptime = $uactive14;
			}elseif ($uprofile == $profile15){
				$exptime = $uactive15;
			}else {
				$exptime = "";
			}
			//$exptime = ($_POST['aktif']);
			$sharuser=($_POST['sharedu']);
			$rxtx = ($_POST['updown']);
			$price = ($_POST['harga']);
			$mode = ($_POST['expmode']);
			$tenggang = ($_POST['tengrem']);
			$onlogin1 = ':put (",rem,'.$price.','.$exptime.','.$tenggang.',"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$tenggang.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"] }}';
			$onlogin2 = ':put (",ntf,'.$price.','.$exptime.',,"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time] }}';
			$onlogin3 = ':put (",remc,'.$price.','.$exptime.','.$tenggang.',"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$tenggang.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[/system script add name="$date-|-$time-|-$user-|-$price" owner="$bln$thn" source=$date comment=mikhmon] }}';
			$onlogin4 = ':put (",ntfc,'.$price.','.$exptime.',,"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$exptime.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[/system script add name="$date-|-$time-|-$user-|-$price" owner="$bln$thn" source=$date comment=mikhmon] }}';
			if($mode == "rem"){
			$onlogin = "$onlogin1";
			}elseif($mode == "ntf"){
			$onlogin = "$onlogin2";
			}elseif($mode == "remc"){
			$onlogin = "$onlogin3";
			}elseif($mode == "ntfc"){
			$onlogin = "$onlogin4";
			}else{
			$onlogin = ':put (",,,,,noexp,")';
			}
			if ($API->connect($iphost, $userhost, $passwdhost)) {
			if($exptime == ""){
			$API->comm("/ip/hotspot/user/profile/add", array(
			  
					  /*"add-mac-cookie" => "yes",*/
					  "name" => "$profname",
					  "rate-limit" => "$rxtx",
					  "shared-users" => "$sharuser",
					  "status-autorefresh" => "15",
					  "transparent-proxy" => "yes",
			));
			}else{
			 $API->comm("/ip/hotspot/user/profile/add", array(
			  		  /*"add-mac-cookie" => "yes",*/
					  "name" => "$profname",
					  "rate-limit" => "$rxtx",
					  "shared-users" => "$sharuser",
					  "status-autorefresh" => "15",
					  "transparent-proxy" => "yes",
					  "on-login" => "$onlogin",
			));
			}
			}
			$ARRAY = $API->comm("/ip/hotspot/user/profile/print");
			$API->disconnect();
			}
?>
			<div style="overflow-x:auto;">
				<table style="white-space: nowrap;" class="zebra" align="center"  >
					<tr>
				    <th style='text-align:center;'>X</th>
						<th >Name</th>
						<th >Shared Users</th>
						<th >Rate Limit</th>
						<th >Mode Expired</th>
						<th >Masa Aktif</th>
						<th >Tenggang</th>
						<th >Harga</th>
					</tr>
					<?php
					$TotalReg = count($ARRAY);

						for ($i=0; $i<$TotalReg; $i++){
						  echo "<tr>";
							$regtable = $ARRAY[$i];
							echo "<td style='text-align:center;'><a style='color:#000;' href=?id=".$regtable['.id'] . ">X</a></td>";
							echo "<td><a style='color:#000;' title='Klik untuk edit Profile' href=?idp=".$regtable['.id']."&name=" . $regtable['name'] . "#edit-profile>". $regtable['name']. "</a></td>";
							//$regtable = $ARRAY[$i];echo "<td>" . $regtable['name'];echo "</td>";
							echo "<td>" . $regtable['shared-users'];echo "</td>";
							echo "<td>" . $regtable['rate-limit'];echo "</td>";
							
							
							echo "<td>";
							$getmodeexp = explode(",",$regtable['on-login']);
							$modeexp = $getmodeexp[1];
							if($modeexp == "rem"){
							  echo "Hapus";
							}elseif($modeexp == "ntf"){
							  echo "Notifikasi";
							}elseif($modeexp == "remc"){
							  echo "Hapus + Data";
							}elseif($modeexp == "ntfc"){
							  echo "Notifikasi + Data";
							}else{
							  
							}
							echo "</td>";
							
							echo "<td>";
							$getvalid = explode(",",$regtable['on-login']);
							$valid = $getvalid[3];
							
							if(substr($valid,-1) == "m"){
							  echo substr($valid,0,-1)."Menit";
							}elseif(substr($valid,-1) == "h"){
							  echo substr($valid,0,-1)."Jam";
							}elseif(substr($valid,-1) == "d"){
							  echo substr($valid,0,-1)."Hari";
							}
							echo "</td>";
							
							echo "<td>";
							$getteng = explode(",",$regtable['on-login']);
							$teng = $getteng[4];
							if(substr($teng,-1) == "m"){
							  echo substr($teng,0,-1)."Menit";
							}elseif(substr($teng,-1) == "h"){
							  echo substr($teng,0,-1)."Jam";
							}elseif(substr($teng,-1) == "d"){
							  echo substr($teng,0,-1)."Hari";
							}
							echo "</td>";
							
							echo "<td>";
							$getprice = explode(",",$regtable['on-login']);
							$price = trim($getprice[2]);
							$cur = "Rp";
							if($price == "" ){
							  $vprice = "Free";
							}elseif(strlen($price) == 4){
							  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
							}elseif(strlen($price) == 5){
							  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
							}elseif(strlen($price) == 6){
							  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
							}elseif(strlen($price) == 7){
							  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
							}elseif(strlen($price) == 8){
							  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
							}elseif(strlen($price) == 9){
							  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
							}else{
							  $vprice = $price;
							}
							echo $vprice. "</td>";
							
							echo "</tr>";
							}
					?>
				</table>
				</div>
				<div>
				  <tr>
				    <td>
				      <p>Catatan:</p>
							<ol>
							  <li>Mode Expired "Hapus" akan  menampilkan notifikasi expired di laman login hotspot untuk user yang sudah habis masa aktifnya, dan  menghapus data user sesuai dengan tenggang penghapusan.</li>
							  <li>Mode Expired "Notifikasi" tdak akan menghapus data user, namun akan menampilkan notifikasi expired di laman login hotspot untuk user yang sudah habis masa aktifnya.<br>(Gunakan template hotspot3 dari Mikhmon atau template hospot yang menggunakan meode yang sama).</li>
							  <li>Mode Expired "Hapus + Data dan Notifikasi + Data" akan menyimpan data (tanggal, waktu dan harga) user saat login.</li>
							  <li>Profile yang bisa mengubah mode expired menjadi "Hapus" atau "Notifikasi" adalah profile yang terdaftar di laman Setup.</li>
								<li>Profile yang dibuat manual silahkan pilih "No Expired" pada kolom Mode Expired.</li>
								<li>Profile yang dibuat manual tidak akan bisa mengubah mode expired menjadi "Hapus" atau "Notifikasi".</li>
							</ol>
				    </td>
				  </tr>
				</div>
			<div id="edit-profile" class="modal-window">
		  <div>
			<a style="font-wight:bold;"href="uprofileadd.php#" title="Close" class="modal-close">X</a>
			<h3>Edit Profile</h3>
	<?php
	echo "<div style='overflow-x:auto;'>";
	echo "<form autocomplete='off' method='post' action=''>";
	echo "<table>";
	echo "	<tr>";
	echo "		<td >Profile</td>";
	echo "		<td >:</td>";
	echo "		<td>$profn</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Shared User</td>";
	echo "		<td >:</td>";
	echo "		<td ><input type='text' size='3' maxlength='3' name='nsharedu' value=$sharedu></td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Upload/Download</td>";
	echo "		<td >:</td>";
	echo "		<td ><input type='text' size='15'  name='nupdown' placeholder='contoh:512k/1M' value=$ratel ></td>";
	echo "	</tr>";
	echo "	<tr>";
	/*if($checkonlogin == ""){
	echo "	<tr>";
	echo "		<td ></td>";
	echo "		<td ></td>";
	echo "		<td ><input type='submit' name='profupdate' class='btnsubmit' value='Update'/></td>";
	echo "	</tr>";
	echo "</table>";
	echo "</form>";
	echo "</div>";
	}else{*/
	echo "		<td >Harga</td>";
	echo "		<td >:</td>";
	echo "		<td ><input type='text' size='12'  name='nprice' placeholder='contoh:10000' value=$priceu ></td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Mode Expired</td>";
	echo "		<td >:</td>";
	echo "		<td >";
	echo "	  <select name='expmodeu' required='1'>";
	echo "						<option value='$modeexpu'>$mdexpt</option>";
	echo "						<option value='0'>No Expired</option>";
	echo "						<option value='rem'>Hapus</option>";
	echo "						<option value='ntf'>Notifikasi</option>";
	echo "						<option value='remc'>Hapus + Data</option>";
	echo "						<option value='ntfc'>Notifikasi + Data</option>";
	echo "		</select>";
	echo "		</td >";
	echo "	</tr>";
	echo "	<tr>";
	echo "	<tr>";
	echo "		<td >Tenggang Penghapusan</td>";
	echo "		<td >:</td>";
	echo "		<td >";
	echo "	  <select name='tengremu' required='1'>";
	echo "						<option value='$tengu'>$tengut</option>";
	echo "						<option value='5m'>5Menit</option>";
	echo "						<option value='10m'>10Menit</option>";
	echo "						<option value='15m'>15Menit</option>";
	echo "						<option value='30m'>30Menit</option>";
	echo "						<option value='1h'>1Jam</option>";
	echo "						<option value='2h'>2Jam</option>";
	echo "		</select>";
	echo "		</td >";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td ></td>";
	echo "		<td ></td>";
	echo "		<td ><input type='submit' name='profupdate' class='btnsubmit' value='Update'/></td>";
	echo "	</tr>";
	echo "</table>";
	echo "</form>";
	echo "</div>";
	/*}*/
  ?>
    </div>
    </div>
		</div>
	</body>
</html>



File: /mikhmon\app\userlist.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}


$prof = $_GET['profile'];
$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=profile='.$prof.'');
	$ARRAY = $API->read();

	$API->write('/ip/hotspot/user/print', false);
	$API->write('=count-only=', false);
	$API->write('?=profile='.$prof.'');
	$ARRAY2 = $API->read();

	$API->disconnect();
}
$listphp = "userlist.php";
?>
<?php
	//remove user
	$id = $_GET['id'];
	$prof = $_GET['profile'];
	if(isset($id)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->comm("/ip/hotspot/user/remove", array(
	    ".id"=> "$id",));
	    $API->disconnect();
	    header("Location:userlist.php?profile=$prof#");
	}
	}
	// disable user
	$id = $_GET['d'];
	if(isset($id)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->write('/ip/hotspot/user/set', false);
	  $API->write('=.id='.$id, false);
	  $API->write('=disabled=yes');
	  $API->read();
	  $API->disconnect();
	  header("Location:userlist.php?profile=$prof#");
	}
	}
	//enable user
	$id = $_GET['e'];
	if(isset($id)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->write('/ip/hotspot/user/set', false);
	  $API->write('=.id='.$id, false);
	  $API->write('=disabled=no');
	  $API->read();
	  $API->disconnect();
	  header("Location:userlist.php?profile=$prof#");
	}
	}
	//reset user
	$id = $_GET['idr'];
	$sname = $_GET['usr'];
	if(isset($_POST['resetuser'])){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	  $API->write('/ip/hotspot/user/set', false);
	  $API->write('=.id='.$id, false);
	  $API->write('=limit-uptime=0');
	  $API->read();
	  $API->disconnect();
	}
	header("Location:userlist.php?profile=$prof#");
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
			
		</script>
	</head>
	<body>
	<div class="main">
	<table class="tnav">
		<tr>
			<td style="text-align: center;" colspan=2>Mikrotik Hotspot Monitor</td>
		</tr>
		<tr>
			<td><?php print_r($prof);?> Aktif  : <?php print_r($ARRAY2);?></td>
			<td>
				<button class="material-icons" onclick="Reload()" title="Reload">autorenew</button>
				<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">find_in_page</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">User by profile</a>
									<?php
								$proflist = array ('1'=>$profile1,$profile2,$profile3,$profile4,$profile5,$profile6,$profile7,$profile8,$profile9,$profile10,$profile11,$profile12,$profile13,$profile14,$profile15);
								
									if($profile1 == ""){
									}elseif ($profile2 == ""){
										for ($i = 1; $i <= 1; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile3 == ""){
										for ($i = 1; $i <= 2; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile4 == ""){
										for ($i = 1; $i <= 3; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile5 == ""){
										for ($i = 1; $i <= 4; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile6 == ""){
										for ($i = 1; $i <= 5; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile7 == ""){
										for ($i = 1; $i <= 6; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile8 == ""){
										for ($i = 1; $i <= 7; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile9 == ""){
										for ($i = 1; $i <= 8; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile10 == ""){
										for ($i = 1; $i <= 9; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile11 == ""){
										for ($i = 1; $i <= 10; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile12 == ""){
										for ($i = 1; $i <= 11; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile13 == ""){
										for ($i = 1; $i <= 12; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile14 == ""){
										for ($i = 1; $i <= 13; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}elseif ($profile15 == ""){
										for ($i = 1; $i <= 14; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}else{
										for ($i = 1; $i <= 15; $i++) {
										echo "<a href='./userlist.php?profile=$proflist[$i]'>$proflist[$i]</a>";
									}
									}
								?>
								</div>
				</div>
				<button class="material-icons" onclick="location.href='../';" title="Dashboard">dashboard</button>
				<button class="material-icons" onclick="goBack()" title="Back">arrow_back</button>
			</td>
		</tr>
	</table>
		<div style="overflow-x:auto;">
		  
		  
			<table id="tUser" style="white-space: nowrap;" class="zebra" >
				<tr>
				  <th title="Hapus User" style="text-align:center;">X</th>
				  <th title="Disable | Enable User" style='text-align:center;'>D/E</th>
					<th >
					  <div style="width:90%;">
					    <input style="width:90%;" type="text" id="CariU" size="auto" onkeyup="fCariU()" placeholder="User" title="Filter User berdasarkan Username">
					  </div>
					</th>
					<th >Password</th>
					<th >
					  <div style="width:90%;">
					    <input style="width:90%;" type="text" id="CariS" onkeyup="fCariS()" placeholder="Server" title="Filter User berdasarkan Server">
					  </div>
					</th>
					<th >Profile</th>
					<th >Uptime</th>
					<th >
					  <div style="width:90%;">
					    <input style="width:90%;" type="text" id="CariG" onkeyup="fCariG()" placeholder="Generated" title="Filter User berdasarkan tanggal Generate">
					  </div>
					</th>
				</tr>
				
				<?php
					$TotalReg = count($ARRAY);

						for ($i=0; $i<$TotalReg; $i++){
						  echo "<tr>";
						  $regtable = $ARRAY[$i];
						  echo "<td style='text-align:center;'><a title='Hapus User' style='color:#000;' href=userlist.php?profile=$prof&id=".$regtable['.id'] . ">X</a></td>";
						  if($regtable['disabled'] == "true"){echo "<td style='text-align:center;'><a title='Enable User'style='color:#000;' href=userlist.php?profile=$prof&e=".$regtable['.id'] . ">E</a></td>";}else{echo "<td style='text-align:center;'><a title='Disable User' style='color:#000;' href=userlist.php?profile=$prof&d=".$regtable['.id'] . ">D</a></td>";}
							echo "<td><a style='color:#000;' title='Klik untuk melihat masa aktifnya' href=userlist.php?profile=$prof&usr=" . $regtable['name'] . "&idr=" . $regtable['.id'] . "#cekuser>". $regtable['name']. "</a></td>";
							echo "<td><input disabled style='border:none; clolor:black;' type='password' value='" . $regtable['password'];
							echo "' id='".$regtable['name'] ."'><input title='Show/Hide Password' type='checkbox' onclick='".$regtable['name'] ."()'><script>function ".$regtable['name'] ."(){var x = document.getElementById('".$regtable['name'] ."');if (x.type === 'password') {x.type = 'text';} else {x.type = 'password';}}</script></td>";
							echo "<td>" . $regtable['server'];echo "</td>";
							echo "<td>" . $regtable['profile'];echo "</td>";
							echo "<td>" . $regtable['uptime'];echo "</td>";
							$vt = substr($regtable['comment'],0,2); echo "<td>" . substr($regtable['comment'],strlen($regtable['comment'],0) - 12,12) . "-" . $vt;
							if($vt == "kv"){
							  echo " | <a style='color:#000;' title='Cetak' href=vouchers/printkvs.php?id=" . $regtable['comment'] . " target='_blank'>Cetak</a>";echo " | <a style='color:#000;' title='Cetak QR' href=vouchers/printkvsqr.php?id=" . $regtable['comment'] . " target='_blank'> QR</a>";
							  
							}elseif($vt == "up"){
							  echo " | <a style='color:#000;' title='Klik untuk melihat masa aktifnya' href=vouchers/printvs.php?id=" . $regtable['comment'] . " target='_blank'>Cetak</a>";echo " | <a style='color:#000;' title='Klik untuk melihat masa aktifnya' href=vouchers/printvsqr.php?id=" . $regtable['comment'] . " target='_blank'> QR</a>";
							  
							}echo " |</td>";
							
							echo"</tr>";
							}
					?>
			</table>
		</div>
		<div id="cekuser" class="modal-window">
		<div>
			<a style="font-wight:bold;"href="userlist.php?profile=<?php echo $prof;?>#" title="Close" class="modal-close">X</a>
			<h3>Info User</h3>
	<?php
	$name = $_GET['usr'];
	if(isset($name)){
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/scheduler/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY1 = $API->read();
	$regtable = $ARRAY1[0];
				$exp = $regtable['next-run'];
				$strd = $regtable['start-date'];
				$strt = $regtable['start-time'];
				$cek = $regtable['interval'];
					$ceklen = strlen(substr($cek,0));
					$cekw = substr($cek, 0,2);
					$cekw1 = substr($cekw, 0,1) ."Minggu";
					$cekd = substr($cek, 2,2);
					$cekd1 = substr($cek, 2,1) ."Hari";
				if ($ceklen > 3){
					$cekall = $cekw1 ." ".$cekd1;
				}elseif (substr($cek, -1) == "h"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Jam";
				}elseif (substr($cek, -1) == "d"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Hari";
				}elseif (substr($cek, -1) == "w"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Minggu";
				}elseif($cekall == ""){
					}
				 $cekall;

	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY2 = $API->read();
	$regtable = $ARRAY2[0];
	  $uptime = $regtable['uptime'];
	  $uptimelimit = $regtable['limit-uptime'];
	  if($uptimelimit == "1s"){
	    $uplimit = "Expired";
	    $uplimitt = "Status";
	    $resetuser = "<td ><input type='submit' name='resetuser' class='btnsubmit' value='Reset'/></td>";
	  }else{
	    $uplimit = "$uptimelimit";
	    $uplimitt = "Limit Uptime";
	    $resetuser = "";
	  }
	  $byteo =  formatBytes2($regtable['bytes-out'],0);
	  $byteolimit = formatBytes2($regtable['limit-bytes-out'],0);

	echo "<div style='overflow-x:auto;'>";
	echo "<form autocomplete='off' method='post' action=''>";
	echo "<table>";
	echo "	<tr>";
	echo "		<td >User/Kode Voucher</td>";
	echo "		<td >:</td>";
	echo "		<td > $name</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Masa Aktif</td>";
	echo "		<td >:</td>";
	echo "		<td >$cekall</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Dari</td>";
	echo "		<td >:</td>";
	echo "		<td >$strd $strt</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Sampai</td>";
	echo "		<td >:</td>";
	echo "		<td >$exp</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >$uplimitt</td>";
	echo "		<td >:</td>";
	echo "		<td >$uplimit</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Uptime</td>";
	echo "		<td >:</td>";
	echo "		<td >$uptime</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Limit Bytes Out</td>";
	echo "		<td >:</td>";
	echo "		<td >$byteolimit</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Bytes Out</td>";
	echo "		<td >:</td>";
	echo "		<td >$byteo</td>";
	echo "	</tr>";
	echo "		<td ></td>";
	echo "		<td ></td>";
	echo "		$resetuser";
	echo "	</tr>";
	echo "</table>";
	echo "</form>";
	echo "</div>";
	
	$API->disconnect();
}
}
?>
    </div>
    </div>
	</div>
<script>
function fCariU() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("CariU");
  filter = input.value.toUpperCase();
  table = document.getElementById("tUser");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
function fCariS() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("CariS");
  filter = input.value.toUpperCase();
  table = document.getElementById("tUser");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[4];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
function fCariG() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("CariG");
  filter = input.value.toUpperCase();
  table = document.getElementById("tUser");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[7];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
</script>
<?php

function formatBytes($bytes, $precision = 2) {
$units = array('B', 'KB', 'MB', 'GB', 'TB');

$bytes = max($bytes, 0);
$pow = floor(($bytes ? log($bytes) : 0) / log(1024));
$pow = min($pow, count($units) - 1);

// Uncomment one of the following alternatives
// $bytes /= pow(1024, $pow);
// $bytes /= (1 << (10 * $pow));

return round($bytes, $precision) . ' ' . $units[$pow];
}

function formatBytes2($size, $decimals = 0){
$unit = array(
'0' => 'Byte',
'1' => 'KiB',
'2' => 'MiB',
'3' => 'GiB',
'4' => 'TiB',
'5' => 'PiB',
'6' => 'EiB',
'7' => 'ZiB',
'8' => 'YiB'
);

for($i = 0; $size >= 1024 && $i <= count($unit); $i++){
$size = $size/1024;
}

return round($size, $decimals).' '.$unit[$i];
}

?>
	</body>
</html>


File: /mikhmon\app\vcolorconf.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('./lib/api.php');
include('./config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:login.php");
}

include('css/vcolors.php');
include('vouchers/kvouchers.php');

$tlimit = $uptimelimit;
if ($tlimit == $utimelimit1){
	$vtimelimit = "Durasi:$utimelimit1t";
}elseif ($tlimit == $utimelimit2){
	$vtimelimit = "Durasi:$utimelimit2t";
}elseif ($tlimit == $utimelimit3){
	$vtimelimit = "Durasi:$utimelimit3t";
}elseif ($tlimit == $utimelimit4){
	$vtimelimit = "Durasi:$utimelimit4t";
}elseif ($tlimit == $utimelimit5){
	$vtimelimit = "Durasi:$utimelimit5t";
}else {
	$vtimelimit= "";
}

$blimit = $upbytelimit;
if ($blimit == $ubytelimit1){
	$vbytelimit = "Kuota:$ubytelimit1t";
}elseif ($blimit == $ubytelimit2){
	$vbytelimit = "Kuota:$ubytelimit2t";
}elseif ($blimit == $ubytelimit3){
	$vbytelimit = "Kuota:$ubytelimit3t";
}elseif ($blimit == $ubytelimit4){
	$vbytelimit = "Kuota:$ubytelimit4t";
}elseif ($blimit == $ubytelimit5){
	$vbytelimit = "Kuota:$ubytelimit5t";
}else {
	$vbytelimit= "";
}
?>
<?php
	if(isset($_POST['headerc'])){
		$headerc=($_POST['headerc']);
		$notec=($_POST['notec']);
		$userpassc=($_POST['userpassc']);
		$detailsc=($_POST['detc']);
		$pricec=($_POST['pricec']);
		$fontc1=($_POST['font1']);
		$fontc2=($_POST['font2']);
		$fontc3=($_POST['font3']);
		$fontc4=($_POST['font4']);
		$fontc5=($_POST['font5']);
		$my_file = 'css/vcolors.php';
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		$data = '<?php $header="' . $headerc . '"; $note="' . $notec . '"; $userpass="' . $userpassc . '"; $details="' . $detailsc . '"; $price="' . $pricec. '"; $font1="' . $fontc1. '"; $font2="' . $fontc2. '"; $font3="' . $fontc3. '"; $font4="' . $fontc4. '"; $font5="' . $fontc5. '"; ?>';
		fwrite($handle, $data);
		header('Location: vcolorconf.php');
	}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="refresh" content="" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="icon" href="./img/favicon.png" />
		<link rel="stylesheet" href="css/style.css" media="screen">
		<style>
table.tclists {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tclists td {
  padding: 4px;
  font-size: 12px;
  text-align: left;
  font-weight: bold;
}
table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tprinta td {
  padding: 4px;
  border: 2px solid BLACK;
  font-size: 16px;
  text-align: left;
  font-weight: bold;
}
table.tprintb {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tprintb td {
  padding-left: 20px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}
		</style>
		<script>
			function Reload() {
				location.reload();
			}
			function goBack() {
				window.history.back();
			}
		</script>
	</head>
	<body>
		<div class="main">
			<table class="tnav">
				<tr>
					<td style="text-align: center;" colspan=2>Pengaturan Warna Voucher</td>
				</tr>
				<tr>
					<td colspan=2>
						<button class="material-icons" onclick="Reload()"	title="Reload">autorenew</button>
						<button class="material-icons"	onclick="location.href='./setup.php';" 	title="Edit Config">settings</button>
						<button class="material-icons" onclick="location.href='resetcolor.php';" title="Reset Warna Voucher">history</button>
						<button class="material-icons" onclick="location.href='./';" title="Dashboard">dashboard</button>
						<div class="dropdown" style="float:right;">
							<button class="material-icons dropbtn">local_play</button>
								<div class="dropdown-content">
									<a style="border-bottom: 1px solid #ccc;" href="#">Ganerate</a>
									<a href="genkv.php">1 Voucher</a>
									<a href="genkvs.php">1-99 Voucher</a>
									<a href="genupm.php">1 Custom User Pass</a>
								</div>
						</div>
					</td>
				</tr>
			</table>
			</table>
			<form autocomplete="off" method="post" action="">
				<table class="tclists" align="center"  >
					<tr><td>Header</td><td>
						<select name="headerc" >
							<option value="<?php print_r($header);?>"><?php print_r($header);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
						<td>Font</td><td>
						<select name="font1" >
							<option value="<?php print_r($font1);?>"><?php print_r($font1);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
					</tr>
					<tr><td>Catatan</td><td>
						<select name="notec" >
							<option value="<?php print_r($note);?>"><?php print_r($note);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
						<td>Font</td><td>
						<select name="font2" >
							<option value="<?php print_r($font2);?>"><?php print_r($font2);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
					</tr>
					<tr><td>User Pass</td><td>
						<select name="userpassc" >
							<option value="<?php print_r($userpass);?>"><?php print_r($userpass);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
						<td>Font</td><td>
						<select name="font3" >
							<option value="<?php print_r($font3);?>"><?php print_r($font3);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
					</tr>
					</tr>
					<tr><td>Keterangan</td><td>
						<select name="detc" >
							<option value="<?php print_r($details);?>"><?php print_r($details);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
						<td>Font</td><td>
						<select name="font4" >
							<option value="<?php print_r($font4);?>"><?php print_r($font4);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
					</tr>
					<tr><td>Harga</td><td>
						<select name="pricec" >
							<option value="<?php print_r($price);?>"><?php print_r($price);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
						<td>Font</td><td>
						<select name="font5" >
							<option value="<?php print_r($font5);?>"><?php print_r($font5);?></option>
							<option style="color:WHITE;" value=WHITE	>WHITE</option>
							<option style="color:SILVER;" value=SILVER	>SILVER</option>
							<option style="color:GRAY;" value=GRAY	>GRAY</option>
							<option style="color:BLACK;" value=BLACK	>BLACK</option>
							<option style="color:RED;" value=RED	>RED</option>
							<option style="color:MAROON;" value=MAROON	>MAROON</option>
							<option style="color:YELLOW;" value=YELLOW	>YELLOW</option>
							<option style="color:OLIVE;" value=OLIVE	>OLIVE</option>
							<option style="color:LIME;" value=LIME	>LIME</option>
							<option style="color:GREEN;" value=GREEN	>GREEN</option>
							<option style="color:AQUA;" value=AQUA	>AQUA	</option>
							<option style="color: TEAL;" value=TEAL	>TEAL</option>
							<option style="color:BLUE;" value=BLUE	>BLUE	</option>
							<option style="color:NAVI;" value=NAVI	>NAVY</option>
							<option style="color:FUCHSIA;" value=FUCHSIA	>FUCHSIA</option>
							<option style="color:PURPLE;" value=PURPLE	>PURPLE</option>
						</select>
						</td>
					</tr>
					<tr>
						<td></td>
						<td>
							<input type="submit" class="btnsubmit" value="Simpan"/>
						</td>
					</tr>
			</table>
			<br>
			<table class="tprinta">
					<tr>
						<td style="text-align: left; background-color:<?php print_r($header);?>"><img src="./img/logo.png" alt="logo" style="height:43px;border:0;"></td>
						<td style="text-align: right; color:<?php print_r($font1);?>; background-color:<?php print_r($header);?>"><?php print_r($headerv);?>  [1]</td>
					</tr>
					<tr>
						<td colspan=2 style="font-size: 12px; color:<?php print_r($font2);?>; background-color:<?php print_r($note);?>">Login dan Logout buka http://<?php print_r($notev);?> </td>
					</tr>
					<tr>
						<td colspan=2 style="color:<?php print_r($font3);?>; background-color:<?php print_r($userpass);?>">
							<table class="tprintb">
								<tr><td>Username : MIKHMON</td></tr>
								<tr><td>Password : MIKHMON</td></tr>
							</table>
						</td>
					</tr>
					<tr>
						<td colspan=2 style="text-align: center; color:<?php print_r($font4);?>; background-color:<?php print_r($details);?>">Aktif:<?php print_r($vprofname);?> <?php print_r($vtimelimit);?> <?php print_r($vbytelimit);?></td>
					</tr>
					<tr>
						<td colspan=2 style="text-align: center; color:<?php print_r($font5);?>; background-color:<?php print_r($price);?>"><?php print_r($vserver);?> <?php print_r($vprice);?></td>
					</tr>
			</table>
			<br>
		</form>
			<table class="tnav">
				<tr>
					<td style="color:green;">
						Logo dapat diganti, diletakkan di folder img dalam folder app dengan format (logo.png).
						<!--<button class="btnsubmit" onclick="window.open('./vouchers/printvs.php','_blank');">Cetak Vouchers</button>-->
					</td>
				</tr>
			</table>
</body>
</html>


File: /mikhmon\app\vouchers\index.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
echo "<meta http-equiv='refresh' content='0;url=../' />";
?>



File: /mikhmon\app\vouchers\printkvs.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('../lib/api.php');
include('../config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:../login.php");
}
$id = $_GET['id'];
if($id == ""){
include('./kvouchers.php');
}else{
  $detv = explode('-', $id);
  for ($i=0;$i<count($detv);$i++) {
  $vkkv=$id;
  $vserver=$detv[1];
  $vprofname=$detv[2];
  $uptimelimit=$detv[3];
  $upbytelimit=$detv[4];
  $profv=$detv[5];
  }
}
   
include('../css/vcolors.php');
$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=comment='.$vkkv.'');
	$ARRAY = $API->read();
	
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$profv.'');
	$ARRAY2 = $API->read();
	
	$API->disconnect();
}
$TotalReg = count($ARRAY);

$regtable = $ARRAY2[0];
$getprice = explode(",",$regtable['on-login']);
$price = $getprice[2];
$cur = "Rp";
if($price == "" ){
  $vprice = "Free";
}elseif(strlen($price) == 4){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
}elseif(strlen($price) == 5){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
}elseif(strlen($price) == 6){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
}elseif(strlen($price) == 7){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
}elseif(strlen($price) == 8){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
}elseif(strlen($price) == 9){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
}else{
  $vprice = $price;
}

$tlimit = $uptimelimit;
if ($tlimit == $utimelimit1){
	$vtimelimit = "Durasi:$utimelimit1t";
}elseif ($tlimit == $utimelimit2){
	$vtimelimit = "Durasi:$utimelimit2t";
}elseif ($tlimit == $utimelimit3){
	$vtimelimit = "Durasi:$utimelimit3t";
}elseif ($tlimit == $utimelimit4){
	$vtimelimit = "Durasi:$utimelimit4t";
}elseif ($tlimit == $utimelimit5){
	$vtimelimit = "Durasi:$utimelimit5t";
}elseif ($tlimit == $utimelimit6){
	$vtimelimit = "Durasi:$utimelimit6t";
}elseif ($tlimit == $utimelimit7){
	$vtimelimit = "Durasi:$utimelimit7t";
}elseif ($tlimit == $utimelimit8){
	$vtimelimit = "Durasi:$utimelimit8t";
}elseif ($tlimit == $utimelimit9){
	$vtimelimit = "Durasi:$utimelimit9t";
}elseif ($tlimit == $utimelimit10){
	$vtimelimit = "Durasi:$utimelimit10t";
}else {
	$vtimelimit= "";
}
$blimit = $upbytelimit;
if ($blimit == $ubytelimit1){
	$vbytelimit = "Kuota:$ubytelimit1t";
}elseif ($blimit == $ubytelimit2){
	$vbytelimit = "Kuota:$ubytelimit2t";
}elseif ($blimit == $ubytelimit3){
	$vbytelimit = "Kuota:$ubytelimit3t";
}elseif ($blimit == $ubytelimit4){
	$vbytelimit = "Kuota:$ubytelimit4t";
}elseif ($blimit == $ubytelimit5){
	$vbytelimit = "Kuota:$ubytelimit5t";
}elseif ($blimit == $ubytelimit6){
	$vbytelimit = "Kuota:$ubytelimit6t";
}elseif ($blimit == $ubytelimit7){
	$vbytelimit = "Kuota:$ubytelimit7t";
}elseif ($blimit == $ubytelimit8){
	$vbytelimit = "Kuota:$ubytelimit8t";
}elseif ($blimit == $ubytelimit9){
	$vbytelimit = "Kuota:$ubytelimit9t";
}elseif ($blimit == $ubytelimit10){
	$vbytelimit = "Kuota:$ubytelimit10t";
}else {
	$vbytelimit= "";
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="icon" href="../img/favicon.png" />
		<style>
@font-face {
  font-family: Roboto;
  src: url('../css/fonts/Roboto-Regular.woff');
  font-weight: normal;
  font-style: normal;
}
body {
  color: #000000;
  background-color: #FFFFFF;
  font-size: 14px;
  font-family: Roboto;
}
table.tprint {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
  page-break-inside:auto;
}
table.tprint tr {
  page-break-inside:avoid;
  page-break-after:auto;
}
table.tprint td {
  padding: 10px;
  border: 1px solid #000000;
  font-size: 14px;
  text-align: left;
}
table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tprinta td {
  padding: 4px;
  border: 2px solid #000000;
  font-size: 16px;
  text-align: left;
  font-weight: bold;
}
table.tprintb {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tprintb td {
  padding-left: 20px;
  padding-top: 17px;
  padding-bottom: 20px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}
		</style>
	</head>
	<body>

<table class="tprint">
	<?php $jml = $TotalReg / 3; for($bar=0;$bar<$jml;$bar++){ if($bar==0) $indx = 0; else $indx = 3 * $bar;?>
			<tr> <!--baris 1 -->
					<?php for($kol=0;$kol<3;$kol++){ ?>
				<td>
					<table class="tprinta">
						<tr>
							<td style="text-align: left; background-color:<?php print_r($header);?>"><img src="../img/logo.png" alt="logo" style="height:43px;border:0;"></td>
							<td style="text-align: right; color:<?php print_r($font1);?>; background-color:<?php print_r($header);?>"><?php print_r($headerv); $no = $indx+1; echo "  [$no]";?></td>
						</tr>
						<tr>
							<td colspan=2 style="font-size: 12px; color:<?php print_r($font2);?>; background-color:<?php print_r($note);?>">Login dan Logout buka http://<?php print_r($notev);?> </td>
						</tr>
						<tr>
							<td colspan=2 style="color:<?php print_r($font3);?>; background-color:<?php print_r($userpass);?>">
								<table class="tprintb">
									<tr><td>Kode Voucher : <?php $regtable = $ARRAY[$indx];echo "" . $regtable['name'];?></td></tr>
								</table>
							</td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font4);?>; background-color:<?php print_r($details);?>">Aktif:<?php print_r($vprofname);?> <?php print_r($vtimelimit);?> <?php print_r($vbytelimit);?></td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font5);?>; background-color:<?php print_r($price);?>"><?php print_r($vserver);?> <?php print_r($vprice);?></td>
						</tr>
					</table>
				</td>
					<?php $indx++; } ?>
			</tr>
	<?php } ?>
</body>
</html>


File: /mikhmon\app\vouchers\printkvsqr.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('../lib/api.php');
include('../config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:../login.php");
}
$id = $_GET['id'];
if($id == ""){
include('./kvouchers.php');
}else{
  $detv = explode('-', $id);
  for ($i=0;$i<count($detv);$i++) {
  $vkkv=$id;
  $vserver=$detv[1];
  $vprofname=$detv[2];
  $uptimelimit=$detv[3];
  $upbytelimit=$detv[4];
  $profv=$detv[5];
  }
}
   
include('../css/vcolors.php');
$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=comment='.$vkkv.'');
	$ARRAY = $API->read();
	
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$profv.'');
	$ARRAY2 = $API->read();
	
	$API->disconnect();
}
$TotalReg = count($ARRAY);

$regtable = $ARRAY2[0];
$getprice = explode(",",$regtable['on-login']);
$price = $getprice[2];
$cur = "Rp";
if($price == "" ){
  $vprice = "Free";
}elseif(strlen($price) == 4){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
}elseif(strlen($price) == 5){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
}elseif(strlen($price) == 6){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
}elseif(strlen($price) == 7){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
}elseif(strlen($price) == 8){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
}elseif(strlen($price) == 9){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
}else{
  $vprice = $price;
}

$tlimit = $uptimelimit;
if ($tlimit == $utimelimit1){
	$vtimelimit = "Durasi:$utimelimit1t";
}elseif ($tlimit == $utimelimit2){
	$vtimelimit = "Durasi:$utimelimit2t";
}elseif ($tlimit == $utimelimit3){
	$vtimelimit = "Durasi:$utimelimit3t";
}elseif ($tlimit == $utimelimit4){
	$vtimelimit = "Durasi:$utimelimit4t";
}elseif ($tlimit == $utimelimit5){
	$vtimelimit = "Durasi:$utimelimit5t";
}elseif ($tlimit == $utimelimit6){
	$vtimelimit = "Durasi:$utimelimit6t";
}elseif ($tlimit == $utimelimit7){
	$vtimelimit = "Durasi:$utimelimit7t";
}elseif ($tlimit == $utimelimit8){
	$vtimelimit = "Durasi:$utimelimit8t";
}elseif ($tlimit == $utimelimit9){
	$vtimelimit = "Durasi:$utimelimit9t";
}elseif ($tlimit == $utimelimit10){
	$vtimelimit = "Durasi:$utimelimit10t";
}else {
	$vtimelimit= "";
}
$blimit = $upbytelimit;
if ($blimit == $ubytelimit1){
	$vbytelimit = "Kuota:$ubytelimit1t";
}elseif ($blimit == $ubytelimit2){
	$vbytelimit = "Kuota:$ubytelimit2t";
}elseif ($blimit == $ubytelimit3){
	$vbytelimit = "Kuota:$ubytelimit3t";
}elseif ($blimit == $ubytelimit4){
	$vbytelimit = "Kuota:$ubytelimit4t";
}elseif ($blimit == $ubytelimit5){
	$vbytelimit = "Kuota:$ubytelimit5t";
}elseif ($blimit == $ubytelimit6){
	$vbytelimit = "Kuota:$ubytelimit6t";
}elseif ($blimit == $ubytelimit7){
	$vbytelimit = "Kuota:$ubytelimit7t";
}elseif ($blimit == $ubytelimit8){
	$vbytelimit = "Kuota:$ubytelimit8t";
}elseif ($blimit == $ubytelimit9){
	$vbytelimit = "Kuota:$ubytelimit9t";
}elseif ($blimit == $ubytelimit10){
	$vbytelimit = "Kuota:$ubytelimit10t";
}else {
	$vbytelimit= "";
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="icon" href="../img/favicon.png" />
		<style>
@font-face {
  font-family: Roboto;
  src: url('../css/fonts/Roboto-Regular.woff');
  font-weight: normal;
  font-style: normal;
}
body {
  color: #000000;
  background-color: #FFFFFF;
  font-size: 14px;
  font-family: Roboto;
}
table.tprint {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
  page-break-inside:auto;
}
table.tprint tr {
  page-break-inside:avoid;
  page-break-after:auto;
}
table.tprint td {
  padding: 10px;
  border: 1px solid #000000;
  font-size: 14px;
  text-align: left;
}
table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tprinta td {
  padding: 2px 4px;
  border: 2px solid #000000;
  font-size: 16px;
  text-align: left;
  font-weight: bold;
}
table.tprintb {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tprintb td {
  padding-top: 2px;
  padding-left: 30px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}
div{
  padding:2px;
  border: 1px solid #000000;
  border-radius:5px;
}
		</style>
	</head>
	<body>

<table class="tprint">
	<?php $jml = $TotalReg / 3; for($bar=0;$bar<$jml;$bar++){ if($bar==0) $indx = 0; else $indx = 3 * $bar;?>
			<tr> <!--baris 1 -->
					<?php for($kol=0;$kol<3;$kol++){ ?>
				<td>
					<table class="tprinta">
						<tr>
							<td style="text-align: left; background-color:<?php print_r($header);?>"><img src="../img/logo.png" alt="logo" style="height:43px;border:0;"></td>
							<td style="text-align: right; color:<?php print_r($font1);?>; background-color:<?php print_r($header);?>"><?php print_r($headerv); $no = $indx+1; echo "  [$no]";?></td>
						</tr>
						<tr>
							<td colspan=2 style="font-size: 12px; color:<?php print_r($font2);?>; background-color:<?php print_r($note);?>">Login dan Logout buka http://<?php print_r($notev);?> </td>
						</tr>
						<tr>
							<td colspan=2 style="color:<?php print_r($font3);?>; background-color:<?php print_r($userpass);?>">
								<table class="tprintb">
									<tr>
										<td style="font-size: 14px;">Kode Voucher :<br><div style="font-size: 18px;"><?php $regtable = $ARRAY[$indx];echo "" . $regtable['name'];?></div></td>
										<td rowspan=2 style="text-align:right;">
										<?php
										$regtable = $ARRAY[$indx]; $uname = $regtable['name'];
										// Source: http://stackoverflow.com/questions/5943368/dynamically-generating-a-qr-code-with-php
										// Google Charts Documentation: https://developers.google.com/chart/infographics/docs/qr_codes?csw=1#overview
										// CHart Type
										$cht = "qr";
										// CHart Size
										$chs = "80x80";
										// CHart Link
										// the url-encoded string you want to change into a QR code
										$chl = urlencode("http://$notev/login?username=$uname&password=$uname");
										// CHart Output Encoding (optional)
										// default: UTF-8
										$choe = "UTF-8";
										$qrcode = 'https://chart.googleapis.com/chart?cht=' . $cht . '&chs=' . $chs . '&chld=|0&chl=' . $chl . '&choe=' . $choe;
										//echo $qrcode . '<br>';
										?>
											<img src="<?php echo $qrcode ?>" alt="vcrqrcode">
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font4);?>; background-color:<?php print_r($details);?>">Aktif:<?php print_r($vprofname);?> <?php print_r($vtimelimit);?> <?php print_r($vbytelimit);?></td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font5);?>; background-color:<?php print_r($price);?>"><?php print_r($vserver);?> <?php print_r($vprice);?></td>
						</tr>
					</table>
				</td>
					<?php $indx++; } ?>
			</tr>
	<?php } ?>
</table>
</body>
</html>


File: /mikhmon\app\vouchers\printvs.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('../lib/api.php');
include('../config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:../login.php");
}
$id = $_GET['id'];
if($id == ""){
include('./vouchers.php');
}else{
  $detv = explode('-', $id);
  for ($i=0;$i<count($detv);$i++) {
  $vkkv=$id;
  $vserver=$detv[1];
  $vprofname=$detv[2];
  $uptimelimit=$detv[3];
  $upbytelimit=$detv[4];
  $profv=$detv[5];
  }
}
   
include('../css/vcolors.php');
$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=comment='.$vkkv.'');
	$ARRAY = $API->read();
	
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$profv.'');
	$ARRAY2 = $API->read();
	
	$API->disconnect();
}
$TotalReg = count($ARRAY);

$regtable = $ARRAY2[0];
$getprice = explode(",",$regtable['on-login']);
$price = $getprice[2];
$cur = "Rp";
if($price == "" ){
  $vprice = "Free";
}elseif(strlen($price) == 4){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
}elseif(strlen($price) == 5){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
}elseif(strlen($price) == 6){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
}elseif(strlen($price) == 7){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
}elseif(strlen($price) == 8){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
}elseif(strlen($price) == 9){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
}else{
  $vprice = $price;
}
$tlimit = $uptimelimit;
if ($tlimit == $utimelimit1){
	$vtimelimit = "Durasi:$utimelimit1t";
}elseif ($tlimit == $utimelimit2){
	$vtimelimit = "Durasi:$utimelimit2t";
}elseif ($tlimit == $utimelimit3){
	$vtimelimit = "Durasi:$utimelimit3t";
}elseif ($tlimit == $utimelimit4){
	$vtimelimit = "Durasi:$utimelimit4t";
}elseif ($tlimit == $utimelimit5){
	$vtimelimit = "Durasi:$utimelimit5t";
}elseif ($tlimit == $utimelimit6){
	$vtimelimit = "Durasi:$utimelimit6t";
}elseif ($tlimit == $utimelimit7){
	$vtimelimit = "Durasi:$utimelimit7t";
}elseif ($tlimit == $utimelimit8){
	$vtimelimit = "Durasi:$utimelimit8t";
}elseif ($tlimit == $utimelimit9){
	$vtimelimit = "Durasi:$utimelimit9t";
}elseif ($tlimit == $utimelimit10){
	$vtimelimit = "Durasi:$utimelimit10t";
}else {
	$vtimelimit= "";
}
$blimit = $upbytelimit;
if ($blimit == $ubytelimit1){
	$vbytelimit = "Kuota:$ubytelimit1t";
}elseif ($blimit == $ubytelimit2){
	$vbytelimit = "Kuota:$ubytelimit2t";
}elseif ($blimit == $ubytelimit3){
	$vbytelimit = "Kuota:$ubytelimit3t";
}elseif ($blimit == $ubytelimit4){
	$vbytelimit = "Kuota:$ubytelimit4t";
}elseif ($blimit == $ubytelimit5){
	$vbytelimit = "Kuota:$ubytelimit5t";
}elseif ($blimit == $ubytelimit6){
	$vbytelimit = "Kuota:$ubytelimit6t";
}elseif ($blimit == $ubytelimit7){
	$vbytelimit = "Kuota:$ubytelimit7t";
}elseif ($blimit == $ubytelimit8){
	$vbytelimit = "Kuota:$ubytelimit8t";
}elseif ($blimit == $ubytelimit9){
	$vbytelimit = "Kuota:$ubytelimit9t";
}elseif ($blimit == $ubytelimit10){
	$vbytelimit = "Kuota:$ubytelimit10t";
}else {
	$vbytelimit= "";
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="icon" href="../img/favicon.png" />
		<style>
@font-face {
  font-family: Roboto;
  src: url('../css/fonts/Roboto-Regular.woff');
  font-weight: normal;
  font-style: normal;
}
body {
  color: #000000;
  background-color: #FFFFFF;
  font-size: 14px;
  font-family: Roboto;
}
table.tprint {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
  page-break-inside:auto;
}
table.tprint tr {
  page-break-inside:avoid;
  page-break-after:auto;
}
table.tprint td {
  padding: 10px;
  border: 1px solid #000000;
  font-size: 14px;
  text-align: left;
}
table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tprinta td {
  padding: 4px;
  border: 2px solid #000000;
  font-size: 16px;
  text-align: left;
  font-weight: bold;
}
table.tprintb {
  table-layout:fixed;
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tprintb td {
  padding-left: 30px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}
		</style>
	</head>
	<body>

<table class="tprint">
	<?php $jml = $TotalReg / 3; for($bar=0;$bar<$jml;$bar++){ if($bar==0) $indx = 0; else $indx = 3 * $bar;?>
			<tr> <!--baris 1 -->
					<?php for($kol=0;$kol<3;$kol++){ ?>
				<td>
					<table class="tprinta">
						<tr>
							<td style="text-align: left; background-color:<?php print_r($header);?>"><img src="../img/logo.png" alt="logo" style="height:43px;border:0;"></td>
							<td style="text-align: right; color:<?php print_r($font1);?>; background-color:<?php print_r($header);?>"><?php print_r($headerv); $no = $indx+1; echo "  [$no]";?></td>
						</tr>
						<tr>
							<td colspan=2 style="font-size: 12px; color:<?php print_r($font2);?>; background-color:<?php print_r($note);?>">Login dan Logout buka http://<?php print_r($notev);?> </td>
						</tr>
						<tr>
							<td colspan=2 style="color:<?php print_r($font3);?>; background-color:<?php print_r($userpass);?>">
								<table class="tprintb">
									<tr><td>Username : <?php $regtable = $ARRAY[$indx];echo "" . $regtable['name'];?></td></tr>
									<tr><td>Password : <?php $regtable = $ARRAY[$indx];echo "" . $regtable['password'];?></td></tr>
								</table>
							</td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font4);?>; background-color:<?php print_r($details);?>">Aktif:<?php print_r($vprofname);?> <?php print_r($vtimelimit);?> <?php print_r($vbytelimit);?></td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font5);?>; background-color:<?php print_r($price);?>"><?php print_r($vserver);?> <?php print_r($vprice);?></td>
						</tr>
					</table>
				</td>
					<?php $indx++; } ?>
			</tr>
	<?php } ?>
</table>
</body>
</html>


File: /mikhmon\app\vouchers\printvsqr.php
<?php
/*
 *  Copyright (C) 2017, 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>
<?php
error_reporting(0);
require('../lib/api.php');
include('../config.php');

if(!isset($_SESSION['usermikhmon'])){
	header("Location:../login.php");
}
$id = $_GET['id'];
if($id == ""){
include('./vouchers.php');
}else{
  $detv = explode('-', $id);
  for ($i=0;$i<count($detv);$i++) {
  $vkkv=$id;
  $vserver=$detv[1];
  $vprofname=$detv[2];
  $uptimelimit=$detv[3];
  $upbytelimit=$detv[4];
  $profv=$detv[5];
  }
}
   
include('../css/vcolors.php');
$API = new RouterosAPI();
$API->debug = false;
if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=comment='.$vkkv.'');
	$ARRAY = $API->read();
	
	$API->write('/ip/hotspot/user/profile/print', false);
	$API->write('?=name='.$profv.'');
	$ARRAY2 = $API->read();
	
	$API->disconnect();
}
$TotalReg = count($ARRAY);

$regtable = $ARRAY2[0];
$getprice = explode(",",$regtable['on-login']);
$price = $getprice[2];
$cur = "Rp";
if($price == "" ){
  $vprice = "Free";
}elseif(strlen($price) == 4){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3);
}elseif(strlen($price) == 5){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3);
}elseif(strlen($price) == 6){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3);
}elseif(strlen($price) == 7){
  $vprice = $cur.substr($price,0,1).".".substr($price,1,3).".".substr($price,4,3);
}elseif(strlen($price) == 8){
  $vprice = $cur.substr($price,0,2).".".substr($price,2,3).".".substr($price,5,3);
}elseif(strlen($price) == 9){
  $vprice = $cur.substr($price,0,3).".".substr($price,3,3).".".substr($price,6,3);
}else{
  $vprice = $price;
}

$tlimit = $uptimelimit;
if ($tlimit == $utimelimit1){
	$vtimelimit = "Durasi:$utimelimit1t";
}elseif ($tlimit == $utimelimit2){
	$vtimelimit = "Durasi:$utimelimit2t";
}elseif ($tlimit == $utimelimit3){
	$vtimelimit = "Durasi:$utimelimit3t";
}elseif ($tlimit == $utimelimit4){
	$vtimelimit = "Durasi:$utimelimit4t";
}elseif ($tlimit == $utimelimit5){
	$vtimelimit = "Durasi:$utimelimit5t";
}elseif ($tlimit == $utimelimit6){
	$vtimelimit = "Durasi:$utimelimit6t";
}elseif ($tlimit == $utimelimit7){
	$vtimelimit = "Durasi:$utimelimit7t";
}elseif ($tlimit == $utimelimit8){
	$vtimelimit = "Durasi:$utimelimit8t";
}elseif ($tlimit == $utimelimit9){
	$vtimelimit = "Durasi:$utimelimit9t";
}elseif ($tlimit == $utimelimit10){
	$vtimelimit = "Durasi:$utimelimit10t";
}else {
	$vtimelimit= "";
}
$blimit = $upbytelimit;
if ($blimit == $ubytelimit1){
	$vbytelimit = "Kuota:$ubytelimit1t";
}elseif ($blimit == $ubytelimit2){
	$vbytelimit = "Kuota:$ubytelimit2t";
}elseif ($blimit == $ubytelimit3){
	$vbytelimit = "Kuota:$ubytelimit3t";
}elseif ($blimit == $ubytelimit4){
	$vbytelimit = "Kuota:$ubytelimit4t";
}elseif ($blimit == $ubytelimit5){
	$vbytelimit = "Kuota:$ubytelimit5t";
}elseif ($blimit == $ubytelimit6){
	$vbytelimit = "Kuota:$ubytelimit6t";
}elseif ($blimit == $ubytelimit7){
	$vbytelimit = "Kuota:$ubytelimit7t";
}elseif ($blimit == $ubytelimit8){
	$vbytelimit = "Kuota:$ubytelimit8t";
}elseif ($blimit == $ubytelimit9){
	$vbytelimit = "Kuota:$ubytelimit9t";
}elseif ($blimit == $ubytelimit10){
	$vbytelimit = "Kuota:$ubytelimit10t";
}else {
	$vbytelimit= "";
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>Mikrotik Hotspot Monitor</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="icon" href="../img/favicon.png" />
		<style>
@font-face {
  font-family: Roboto;
  src: url('../css/fonts/Roboto-Regular.woff');
  font-weight: normal;
  font-style: normal;
}
body {
  color: #000000;
  background-color: #FFFFFF;
  font-size: 14px;
  font-family: Roboto;
}
table.tprint {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
  page-break-inside:auto;
}
table.tprint tr {
  page-break-inside:avoid;
  page-break-after:auto;
}
table.tprint td {
  padding: 10px;
  border: 1px solid #000000;
  font-size: 14px;
  text-align: left;
}
table.tprinta {
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  height: 180px;
  border-collapse: collapse;
}
table.tprinta td {
  padding: 2px 4px;
  border: 2px solid #000000;
  font-size: 16px;
  text-align: left;
  font-weight: bold;
}
table.tprintb {
  table-layout:fixed;
  margin-left:auto;
  margin-right:auto;
  width: 300px;
  border-collapse: collapse;
}
table.tprintb td {
  padding-top: 1px;
  padding-left: 30px;
  border: 0px;
  font-size: 18px;
  text-align: left;
}
div{
  padding:2px;
  border: 1px solid #000000;
  border-radius:5px;
}
		</style>
	</head>
	<body>

<table class="tprint">
	<?php $jml = $TotalReg / 3; for($bar=0;$bar<$jml;$bar++){ if($bar==0) $indx = 0; else $indx = 3 * $bar;?>
			<tr> <!--baris 1 -->
					<?php for($kol=0;$kol<3;$kol++){ ?>
				<td>
					<table class="tprinta">
						<tr>
							<td style="text-align: left; background-color:<?php print_r($header);?>"><img src="../img/logo.png" alt="logo" style="height:43px;border:0;"></td>
							<td style="text-align: right; color:<?php print_r($font1);?>; background-color:<?php print_r($header);?>"><?php print_r($headerv); $no = $indx+1; echo "  [$no]";?></td>
						</tr>
						<tr>
							<td colspan=2 style="font-size: 12px; color:<?php print_r($font2);?>; background-color:<?php print_r($note);?>">Login dan Logout buka http://<?php print_r($notev);?> </td>
						</tr>
						<tr>
							<td colspan=2 style="color:<?php print_r($font3);?>; background-color:<?php print_r($userpass);?>">
								<table class="tprintb">
									<tr><td style="font-size: 12px;">Username :<br><div style="font-size: 18px;"><?php $regtable = $ARRAY[$indx];echo "" . $regtable['name'];?></div></td>
									<td rowspan=2 style="text-align:right;">
										<?php
										$regtable = $ARRAY[$indx]; $uname = $regtable['name']; $upass = $regtable['password'];
										// Source: http://stackoverflow.com/questions/5943368/dynamically-generating-a-qr-code-with-php
										// Google Charts Documentation: https://developers.google.com/chart/infographics/docs/qr_codes?csw=1#overview
										// CHart Type
										$cht = "qr";
										// CHart Size
										$chs = "80x80";
										// CHart Link
										// the url-encoded string you want to change into a QR code
										$chl = urlencode("http://$notev/login?username=$uname&password=$upass");
										// CHart Output Encoding (optional)
										// default: UTF-8
										$choe = "UTF-8";
										$qrcode = 'https://chart.googleapis.com/chart?cht=' . $cht . '&chs=' . $chs . '&chld=L|0&chl=' . $chl . '&choe=' . $choe;
										//echo $qrcode . '<br>';
										?>
											<img src="<?php echo $qrcode ?>" alt="vcrqrcode">
										</td>
									<tr><td style="font-size: 12px;">Password :<br><div style="font-size: 18px;"><?php $regtable = $ARRAY[$indx];echo "" . $regtable['password'];?></div>
									</td>
									
									</tr>
								</table>
							</td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font4);?>; background-color:<?php print_r($details);?>">Aktif:<?php print_r($vprofname);?> <?php print_r($vtimelimit);?> <?php print_r($vbytelimit);?></td>
						</tr>
						<tr>
							<td colspan=2 style="text-align: center; color:<?php print_r($font5);?>; background-color:<?php print_r($price);?>"><?php print_r($vserver);?> <?php print_r($vprice);?></td>
						</tr>
					</table>
				</td>
					<?php $indx++; } ?>
			</tr>
	<?php } ?>
</table>
</body>
</html>


File: /mikhmon\index.php
<?php
header('Location: ./app/login.php');
exit;
?>



File: /mikhmon\install\mikhmon-server
#!/bin/bash
php -S 0.0.0.0:8080 -t ~/mikhmon


File: /mikhmon\install\mikhmon.desktop
[Desktop Entry]
Name=mikhmon-server
Comment=Mikrotik Hotspot Monitor
Exec=mikhmon-server
Icon=web-browser
Terminal=true
Type=Application
Categories=Network;
MimeType=text/html;text/xml;application/xhtml+xml;


File: /mikhmon\status\api.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 5;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    public function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $ip.':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


File: /mikhmon\status\config.php
<?php $iphost=""; $userhost=""; $passwdhost=""; $headerv="Kemangi41"; ?>

File: /mikhmon\status\index.php
<?php
error_reporting(0);
require('./api.php');
include('./config.php');
$API = new RouterosAPI();
$API->debug = false;

?>
<!DOCTYPE html>
<html>
<head>
<title>Cek Voucher <?php print_r($headerv);?></title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
<link rel="icon" href="../app/img/favicon.png" />
<script>
function goBack() {
    window.history.back();
}
</script>
<style>
table {
  table-layout: fixed;
  width: 330;
  border-collapse: collapse;
  margin-left:auto;
  margin-right:auto;
}
/* Zebra striping */
tr:nth-of-type(odd) {
  background: #eee;
}
th {
  background: #333;
  color: white;
  font-weight: bold;
}
td, th {
  padding: 6px;
  border: 1px solid #ccc;
  text-align: left;
}
.button {
    background-color: #008CCA;
    border: none;
    padding: 5px 5px;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    cursor: pointer;
    border-radius: 5px;
}
table.tnav {
  table-layout: fixed;
  white-space: nowrap;
  width: 200;
  border-collapse: collapse;
  
}
table.tnav td {
  padding: 3px;
  border: 0px;
  text-align: left;
}
textarea,input,select {
  padding: 2px;
  margin: 2px;
  font-size: 14px;
}
</style>
</head>
<body align="center">
<h3 style="text-align:center;">Cek Voucher<br><?php print_r($headerv);?></h3>
<p style="text-align:center;" id="date1"><?php echo "Tanggal : " . date("d-m-Y") . "<br>";?></p>
<form autocomplete="off" method="post" action="">
	<table class="tnav">
		<tr><td>User/Kode Voucher :</td><td><input type="text" size="15" name="nama" required="1"/></td></tr>
		<tr><td></td><td><input type="submit" class="button" value="Cek Voucher"/></td></tr>
	</table>
</form>
<?php
	if(isset($_POST['nama'])){
	$name = ($_POST['nama']);
	if ($API->connect( $iphost, $userhost, $passwdhost )) {
	$API->write('/system/scheduler/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY1 = $API->read();
	$regtable = $ARRAY1[0];
				$exp = $regtable['next-run'];
				$strd = $regtable['start-date'];
				$strt = $regtable['start-time'];
				$cek = $regtable['interval'];
					$ceklen = strlen(substr($cek,0));
					$cekw = substr($cek, 0,2);
					$cekw1 = substr($cekw, 0,1) ."Minggu";
					$cekd = substr($cek, 2,2);
					$cekd1 = substr($cek, 2,1) ."Hari";
				if ($ceklen > 3){
					$cekall = $cekw1 ." ".$cekd1;
				}elseif (substr($cek, -1) == "h"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Jam";
				}elseif (substr($cek, -1) == "d"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Hari";
				}elseif (substr($cek, -1) == "w"){
					$cek1 = substr($cek, 0,-1);
					$cekall = $cek1 ."Minggu";
				}elseif($cekall == ""){
					}
				 $cekall;
				

	$API->write('/ip/hotspot/user/print', false);
	$API->write('?=name='.$name.'');
	$ARRAY2 = $API->read();
	$regtable = $ARRAY2[0];
	$user = $regtable['name'];
	if($user == $pass){
		$pass1 = "";
	}else{
		$pass1 = $pass;
	}

	echo "<div style='overflow-x:auto;'>";
	echo "<table>";
	echo "	<tr>";
	echo "		<td >User/Kode Voucher</td>";
	echo "		<td > $user</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Masa Aktif</td>";
	echo "		<td >$cekall</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Dari</td>";
	echo "		<td >$strd $strt</td>";
	echo "	</tr>";
	echo "	<tr>";
	echo "		<td >Sampai</td>";
	echo "		<td >$exp</td>";
	echo "	</tr>";
	echo "</table>";
	echo "</div>";
	
	$API->disconnect();
}
}
?>
</div>
</body>
</html>


File: /README.md
## Discontinued. New build [MIKHMON V2](https://github.com/laksa19/mikhmonv2)

# MIKROTIK HOTSPOT MONITOR (MIKHMON)
Mikrotik Hotspot Monitor adalah aplikasi web PHP untuk menggantikan User Manager yang tidak didukung dibeberapa tipe RB Mikrotik.

## TENTANG  

1. Aplikasi ini menggunakan port API untuk terhubung ke Mikrotik
    - API port 8728 
      ([routeros-api](https://wiki.mikrotik.com/wiki/API_PHP_class))

2. Pastikan port API sudah aktif dan Jam Tanggal di Mikrotik sudah update sesuai wilayah masing-masing. Untuk pengaturan Jam dan Tanggal bisa baca [di sini](http://www.mikrotik.co.id/artikel_lihat.php?id=55).

3. Sudah dites di Router OS 3.25, 5.22, 6.3+

## FITUR  
1. Multi platform (Windows, GNU/Linux, Android, OpenWRT)
2. Menampilkan User Hotspot yang aktif dan masa aktifnya.
3. Menambah, edit dan hapus User Profile.
4. Tersedia dua mode expired (Hapus dan Notifikasi)
    - Mode Expired "Hapus" akan menghapus data user yang sudah habis masa aktifnya.
    - Mode Expired "Notifikasi" tdak akan menghapus data user.
    - Mode Expired Hapus dan Notifikasi akan menampilkan notifikasi expired di laman login hotspot, untuk user yang sudah habis masa aktifnya.
    - Mode Expired (Hapus + Data dan Notifikasi +Data). + Data artinya data user yang login akan disimpan di Mikrotik, meliputi Tanggal dan waktu login serta harga voucher.
    - Gunakan template hotspot3 dari Mikhmon atau template hospot yang menggunakan metode yang sama. Tutorial login hotspot dengan expired bisa di cek di  [Video](https://goo.gl/hVUnjD).
5. Menampilkan daftar User Hotspot berdasarkan User Profile.
    - Filter berdasarkan Username, Server, dan Tanggal/Kode Generate.
    - Hapus User.
    - Disable/Enable User.
    - Show/Hide Password.
6. Generate Voucher.
    - Generate Kode Voucher.
    - Generate User Password.
    - Generate Custom User Password.
7. Cetak Voucher. (Ukuran kertas A4 atau F4)
    - Generate Kode Voucher.
    - Generate User Password.
    - Generate Custom User Password.
    - Pilihan Huruf untuk Kode Voucher dan User Password [abcd, ABCD, aBcD].
    - Generate Kode Voucher/User Password maksimal 99 untuk sekali generate, bisa diulangi lagi.
8. Custom warna Voucher.
9. Pencatatan data penjualan
10. Tools :
    - Add Remove DNS Static untuk blok website.
    - Log Hotspot Mikrotik.
    - History.
    - Status, untuk cek voucher dari sisi client.
    
## PENGGUNAAN  
1. Aplikasi ini bisa dijalankan menggunakan web server dengan PHP.

    Download web server :
    - Windows Web Server [USBWebserver](http://www.usbwebserver.net/downloads/USBWebserver%20v8.6.zip "USBWebserver")
    - Android Web Server [PlayStore Bit Web Server](https://play.google.com/store/apps/details?id=com.andi.serverweb&hl=en "Bit Web Server") (berbayar), [allfreeapk.com Bit Web Server](https://m.allfreeapk.com/search.html?q=bit-web-server-php-mysql-pma "Bit Web Server") (gratis)
    

2. Install Web Server

    Web Server Windows
    - Download USBWebserver, buat folder webserver di drive D:, extract USBWebserver ke folder tersebut.
    - Download Mikrotik Hotspot Monitor, extract folder mikhmon ke folder root webserver.
    - Jalankan USBWebserver kemudian buka di browser http://localhost:8080/mikhmon/
    
    Web Server Android
    - Download Bit Web Server, install di Android.
    - Download Mikrotik Hotspot Monitor, extract folder mikhmon ke folder www memory internal Android.
    - Jalankan Bit Web Server kemudian buka di browser http://localhost:8080/mikhmon/
    
3. Login dengan user admin Mikhmon (user: admin | pass:  1234).

4. Sesuaikan User Profile, nama usaha harga voucher di laman setup.

5. Tambahkan User Profile ke Mikrotik dari aplikasi Mikhmon. Setelah itu aplikasi siap untuk generate voucher.

    Tutorial lebih lengkap kunungi [laksa19.github.io](https://laksa19.github.io/)
     
6. Logo di cetak voucher di letakkan di folder img dalam folder app dengan format (logo.png).

## Changelog 

### Versi 2018


4-3-2018

Penting!!Yang harus dilakuman setelah update.
1. Simpan Setup mikhmon dan export lagi ke mikrotik.
2. Update User Profile (sesuai kebutuhan)
3. Clear cache browser.
Perubahan
1. Perbaikan dan penambahan opsi User Profile.
    - Penamabahan Mode Expired (Hapus + Data dan Notifikasi +Data). + Data artinya data user yang login akan disimpan di Mikrotik, meliputi Tanggal dan waktu login serta harga voucher.
    - Penambahan kolom Harga. Harga sekarang akan menempel pada User Profile, jadi ini memungkinkan jika suatu saat ingin merubah harga voucher yang sudah digenerate.
2. Penghapusan opsi Harga di laman generate voucher. Tidak pelu lagi mengingat-ingat harga voucher.
3. Penamabahan Pencatatan Penjualan, bisa diakses dari tombol ($).
4. Penambahan Filter di log hotspot.

23-2-2018

1. Pembaruan User Profile mode expired Hapus.
    - Sekarang diambahkan  jeda atau tenggang untuk menghapus user dari Mikrotik, default 5menit. Jadi ada kesempatan untuk notifikasi Expired saat user mencoba login kembali.
    - Tutorial Membuat Login Hotspot dengan notifikasi Expired : [YouTube Laksa19](https://goo.gl/uuFZfd)
    - Template jadi dengan notifikasi Expired [hotspot3](https://goo.gl/Qw88vK)
2. Penambahan opsi Huruf saat generate. Sekarang ada 3 pilihan [abcd, ABCD, aBcD]
3. Penambahan Show/Hide Passworddi user list.
4. Penambahan opsi Export/Import Setup Mikhmon. Export ke Mikrotik/Import dari Mikrotik.

20-2-2018

Penambahan Mode Expired, menjadi mode Hapus dan Notifikasi.
1. Mode Expired "Hapus" akan menghapus data user yang sudah habis masa aktifnya.
2. Mode Expired "Notifikasi" tdak akan menghapus data user, namun akan menampilkan notifikasi expired di laman login hotspot untuk user yang sudah habis masa aktifnya.(Gunakan template hotspot3 dari Mikhmon atau template hospot yang menggunakan metode yang sama).
3. Profile yang bisa mengubah mode expired menjadi "Hapus" atau "Notifikasi" adalah profile yang terdaftar di laman Setup.
4. Profile yang dibuat manual silahkan pilih "No Expired" pada kolom Mode Expired.
5. Profile yang dibuat manual tidak akan bisa mengubah mode expired menjadi "Hapus" atau "Notifikasi".
6. Untuk mengaktifkan kembali user expired cukup klik tombol Reset di info user, ini bisa diakses dari user list.

17-2-2018

Penambahan fitur cetak voucher yang digenerate sebelumnya. Diakses melalui userlist. <br> Fitur ini hanya bisa digunakan setelah generate voucher dari Mikhmon build 2052. <br> Cetak kembali berdasarkan tanggal dan kode unik saat genetare.

7-2-2018

Perbaikan update profile.

7-2-2018

1. Perubahan edit User Profile.
2. Penambahan Disable/Enable user di userlist.
3. Penambahan filter berdasarkan server hotspot dan tanggal generate.

4-2-2018

Perbaikan userlist dan penambahan tombol filter user berdasarkan profile.

3-2-2018

1. Remove tab User Aktif dan Masa Aktif di laman Dashboard.
2. Menambahkan modal untuk cek massa aktif user, dengan klik/tap user yang aktif.
3. Remove folder userlist (merampingkan aplikasi)
4. Perbaikan laman Dahsboard.
5. Penambahan modal untuk info user di laman userlist.

1-2-2018

1. Perbaikan OTA Update.
2. Dukungan untuk RouterOS v3.25 dan v5.22.

26-1-2018

1. Perbaikan OTA Update. Catatan hak akses penuh pada flder root web server.
2. Penambahan filter di userlist.

23-1-2018

1. Perbaikan remove user aktif di laman dashboard.
2. Perubahan mode update menjadi OTA update.

22-1-2018

Menghilangkan baris password di laman status (cek detail voucher).

21-1-2018

Penambahan kolom X untuk menghapus user, user acive, profile, dan dns di dns static.

20-1-2018

1. Perubahan cek update Mikhmon dan perbaikan performa.
2. Penambahan kolom MAC Address dan Login By di laman dashboard.
3. Perbaikan cek masa aktif di laman dashboard dan status.
4. Penambahan tombol reboot Mikrotik di laman setup.


19-1-2018

Perbaikan laman setup (durasi kolom kedua). Setelah update klik Simpan dilaman setup.

14-1-2018

Perbaikan cetak voucher. (Tidak ada voucher yang terpotong ke laman berikutnya).

13-1-2018

1. Perbaikan Generate Voucher (Penambahan pilihan panajang Username). Untuk Kode Voucher 2x panjang Username.
2. Perubahan Setup Voucher Note menjadi DNS NAME. (Sesuaikan DNS Name di laman Setup).
3. Perbaikan Cetak Voucher.
4. Penambahan QR Code di cetak Voucher

10-1-2018

Perbaikan untuk dukungan login by mac. Setelah update Mikhmon, silahkan update user profile dari Mikhmon.

9-1-2018

1. Perubahan form user profile. Rate limit Upload/Downlod menjadi input manual. Bertujuan agar lebih leluasa membuat rate limit.
2. Perubahan Log Hotspot. Sekarang menampilkan log terbaru diuruan teratas.

1-7-2018

1. Penambahan Byte Out di laman Dashboard.
2. Penambahan 5 User Profile.
3. Penambahan Durasi dan Kuota masing-masing 5.
4. Penambahan Sisa Kuota di status dan logout template hotspot.

5-1-2018

1. Penambahan notifikasi update.
2. Perbaikan laman status.
3. Drop support mikhmon-standalone.

4-1-2018

Perbaikan cetak voucher (perbaikan detail voucher dan penambahan logo).

1-1-2018

Perbaikan laman status untuk cek voucher.

29-12-2017
    
   1. Full menggunakan RouterOS API (Tidak memerlukan koneksi SSH lagi).
   2. Perbaikan di generate voucher. (custom jumlah voucher 1-99 untuk sekali generate).
   3. Perbaikan di cetak voucher.
   4. Perbaikan Setup.
   5. Perbaikan laman dashboard.
   6. Perbaikan laman status (untuk cek masa aktif voucher)

### Versi 2017

16-12-2017

   1. Penambahan 5 profile, total 10 profile yang bisa digunakan untuk berbagai macam paket hotspot wifi.
   2. Penambahan kolom server hotspot ditiap form generate voucher, ini memungkinkan untuk membuat voucher atau user hotspot dengan batasan server hotspot. Jadi voucher hanya bisa digunakan di server hotspot tertentu. Catatan: Sesuaikan nama server  hotspot Mikrotik di laman setup mikhmon.
   3. Perbaikan tampilan desktop, kini dibuat lebih lebar untuk tampilan desktop dan menyesuakan layar saat digunakan di Android.
   4. Perubahan laman dashboard, Header tabel sisa voucher sekarang menggunakan nama profile, bertujuan untuk memudahkan admin mengenali sisa voucher.

29-11-2017

   Perbaikan form setup, konfirmasi pada saat reset config.

28-11-2017

   1. Penambahan form Log Hotspot.
   2. Penambahan form History Remove User, untuk melacak user yang telah dihapus.

26-11-2017

   1. Update setting warna voucher agar tetap menyimpan settingan sebelumnya.
   2. Penambahan cetak di setiap form generate 1 voucher.
   
21-11-2017

   1. Drop operator dan perbaikan resetconfig.
   2. Add Remove DNS Static untuk blok website.
   
10-11-2017

   Penambahan generate user password manual input. (Perubahan di mikhmon: index.php, genkv.php, genkvs.php, genupm.php, genvoucher.php, genvouchers.php, profileadd.php, profilerm.php, profileset.php, vcolorconf.php).

09-11-2017

   Perubahan struktur menu.

07-11-2017

   Perbaikan tamplate hotspot. Penjelasan dibagian [PENGGUNAAN](https://github.com/laksa19/mikrotik-hotspot-monitor#penggunaan) poin 6.

05-11-2017

   Penambahan laman status untuk cek masa aktif vouvher pelanggan. (Perubahan di status: index.php, api.php).

04-11-2017

   1. Penambahan fitur ganerate kode voucher, jadi pelanggan hanya memasukkan kode login saja untuk login. (Perubahan di mikhmon: index.php, file baru: genkv.php, genkvs.php, kvouchers.php, printkvs.php).
   2. Upload template hotspot untuk mendukung login menggunakan kode voucher.

28-10-2017

   1. Perbaikan di file setup.php.
   2. Penambahan jam Mikrotik, untuk mengetahui apakah jam di Mikrotik sudah sesuai. (Perubahan: index.php).

10-10-2017

   Penambahan form untuk pengaturan warna di cetak voucher (Perubahan: printv.php, genvouchers.php, vcolorconf.php, vcolors.php).

09-10-2017

   Perbaikan Setup (perubahan : index.php, setup.php).

07-10-2017

   1. Menambahkan opsi untuk auto reload laman index (perubahan: index.php).
   2. Perbaikan dan penambahan setup aplikasi (perubahan : config.php, login.php, setup.php, conntest.php, resetconfig.php).

06-10-2017

   Menambahkan hak akses user :  1. Administrator,  2. Operator.
   
05-10-2017

  1. Penambahan setup.php untuk memudahkan edit file config.php
  2. Penambahan halaman login.
  3. Beberapa penyesuaian lainnya.  
  
04-10-2017

  1. Penyesuaian config.php
  2. Penyesuaian index.php
  3. Penambahan User Lists, sekarang menjadi 5
  4. Penyederhanaan pembuatan Profile
  5. Penambahan fitur pada generate voucher
       - Batasan Durasi (Limit Uptime)
       - Batasan Kuota (Limit Bytes Out)
  6. Penyesuaian cetak voucher

03-10-2017

  1. Upload pertama.


