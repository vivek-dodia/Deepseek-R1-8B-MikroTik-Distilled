# Repository Information
Name: mikrotik-gps

# Directory Structure
Directory structure:
└── github_repos/mikrotik-gps/
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
    │   │       ├── pack-ce60efd4a8e7e32644c194bd5ce60886a103b6ba.idx
    │   │       └── pack-ce60efd4a8e7e32644c194bd5ce60886a103b6ba.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── gps-to-email
    ├── gps-to-url
    ├── MC7710-enable-gps.txt
    ├── mikrotikgps.php
    ├── mikrotiklocation.html
    ├── mikrotik_genxml.php
    ├── phpsqlajax_dbinfo.php
    ├── README.md
    ├── schedule-command
    └── usb-reset


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
	url = https://github.com/timmay2/mikrotik-gps.git
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
0000000000000000000000000000000000000000 518456b9103c68360c6fb43028657b2a48848ba2 vivek-dodia <vivek.dodia@icloud.com> 1738605960 -0500	clone: from https://github.com/timmay2/mikrotik-gps.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 518456b9103c68360c6fb43028657b2a48848ba2 vivek-dodia <vivek.dodia@icloud.com> 1738605960 -0500	clone: from https://github.com/timmay2/mikrotik-gps.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 518456b9103c68360c6fb43028657b2a48848ba2 vivek-dodia <vivek.dodia@icloud.com> 1738605960 -0500	clone: from https://github.com/timmay2/mikrotik-gps.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
518456b9103c68360c6fb43028657b2a48848ba2 refs/remotes/origin/master


File: /.git\refs\heads\master
518456b9103c68360c6fb43028657b2a48848ba2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /gps-to-email
# CHANGE BELOW E-MAIL ADDRESS
:local email "myuser@mydomain.com";

:system gps monitor file="gps.txt";
:global gpstext [/file get gps.txt contents];
:local longstart [:find $gpstext "longitude" -1];
:local longend [:find $gpstext "\n" $longstart];
:local latstart [:find $gpstext "latitude" -1];
:local latend [:find $gpstext "\n" $latstart];
:local validstart [:find $gpstext "valid" -1];
:local validend [:find $gpstext "\n" $validstart];
:local valid false;
:local zeros "";

:if ([:find $gpstext "yes" $validstart] > 0) do={:set valid true;};

:global longitude [:pick $gpstext ($longstart + 11) $longend];
:local degreestart [:find $longitude " " -1];
:local minutestart [:find $longitude " " $degreestart];
:local secondstart [:find $longitude "'" $minutestart];

:local secondend;
:local secfract;

:if ([:len [:find $longitude "." 0]] < 1) do={
    :set secondend [:find $longitude "'" $secondstart];
    :set secfract "0";
} else={
    :set secondend [:find $longitude "." $secondstart];
    :set secfract [:pick $longitude ($secondend + 1) ($secondend + 2)];
};

:local longdegree;
:local longdegreelink;

:if ([:pick $longitude 0 1] = "W") do={
    :set longdegree "-";
    :set longdegreelink "W";
} else={
    :set longdegree "+";
    :set longdegreelink "E";
};

:set longdegree ($longdegree . [:pick $longitude 2 $minutestart]);
:set longdegreelink ($longdegreelink . [:pick $longitude 2 $minutestart]);
:local longmin [:pick $longitude ($minutestart + 1) $secondstart];
:local longsec [:pick $longitude ($secondstart + 2) $secondend];
:local longfract ((([:tonum $longmin] * 6000) + ([:tonum $longsec] * 100) + ([:tonum $secfract] * 10) ) / 36);

:while (([:len $zeros] + [:len $longfract]) < 4) do={
    :set zeros ($zeros . "0");
};

:global newlong ($longdegree . "." . $zeros . $longfract);
:global newlonglink ($longdegreelink . "." . $zeros . $longfract);

:global latitude [:pick $gpstext (latstart + 10) $latend];
:set degreestart [:find $latitude " " -1];
:set minutestart [:find $latitude " " $degreestart];
:set secondstart [:find $latitude "'" $minutestart];

:if ([:len [:find $latitude "." 0]] < 1) do={
    :set secondend [:find $latitude "'" $secondstart];
    :set secfract "0";
} else={
    :set secondend [:find $latitude "." $secondstart];
    :set secfract [:pick $latitude ($secondend + 1) ($secondend +2)];
};

:local latdegree;
:local latdegreelink;

:if ([:pick $latitude 0 1] = "N") do={
    :set latdegree "+";
    :set latdegreelink "N";
} else={
    :set latdegree "-";
    :set latdegreelink "S";
};

:set latdegree ($latdegree . [:pick $latitude 2 $minutestart]);
:set latdegreelink ($latdegreelink . [:pick $latitude 2 $minutestart]);
:local latmin [:pick $latitude ($minutestart + 1) $secondstart];
:local latsec [:pick $latitude ($secondstart + 2) $secondend];
:local latfract ((([:tonum $latmin] * 6000) + ([:tonum $latsec] * 100) +([:tonum $secfract] * 10)) / 36);

:set zeros "";

:while (([:len $zeros] + [:len $latfract]) < 4) do={
    :set zeros ($zeros . "0");
};

:global newlat ($latdegree . "." . $zeros . $latfract);
:global newlatlink ($latdegreelink . "." . $zeros . $latfract);

:global coordinates ($newlong . "," . $newlat);

:global linkout "http://maps.google.com?q=$newlatlink+$newlonglink";
:global SMlinkout "http://www.openstreetmap.org/?lat=$newlat&lon=$newlong&zoom=8&layers=M";

:global kmlout "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://www.opengis.net/kml/2.2\">
  <Placemark>
    <name>My router</name>
    <description>My router's location</description>
    <Point>
      <coordinates>$coordinates</coordinates>
    </Point>
  </Placemark>
</kml>
";

:if (valid) do={
    :global oldpos;

    :if ($oldpos != $coordinates) do={
        /file set [/file find name=gps.kml] contents=$kmlout
        /tool e-mail
        send to=$email subject="Router move" body="Moved to $latitude $longitude\r\n$linkout\r\n$SMlinkout" file=gps.kml
        :set oldpos $coordinates;
     };
} else={
         /tool e-mail
         send to=$email subject="Router gps position invalid" body="Router gps position invalid"
};


File: /gps-to-url
# CHANGE BELOW SERVER BELOW TO YOUR SERVERS DOMAIN OR IP ADDRESS 
:local server "change.me.com";

# Get GPS info and find variables
:system gps monitor file="gps.txt";
:global gpstext [/file get gps.txt contents];
:local datestart [:find $gpstext "time: "];
:local dateend [:find $gpstext "latitude"];
:local date [:pick $gpstext ($datestart +6) ($dateend -14)]
:local longstart [:find $gpstext "longitude" -1];
:local longend [:find $gpstext "\n" $longstart];
:local latstart [:find $gpstext "latitude" -1];
:local latend [:find $gpstext "\n" $latstart];
:local validstart [:find $gpstext "valid" -1];
:local validend [:find $gpstext "\n" $validstart];
:local speedstart [:find $gpstext "speed"];
:local speedend [:find $gpstext "." $speedstart];
:local speed [;pick $gpstext ($speedstart +7) ($speedend +3)];
:local altitudestart [:find $gpstext "altitude"];
:local altitudeend [:find $gpstext "." $altitudestart];
:local altitude [;pick $gpstext ($altitudestart +10) ($altitudeend +3)];
:local satellitesstart [:find $gpstext "satellites"];
:local satellitesend [:find $gpstext "\n" $satellitesstart];
:local satellites [;pick $gpstext ($satellitesstart +12) ($satellitesend)];
:local valid false;
:local zeros "";

# Get Ethernet details and set mac variable
:interface ethernet print detail from=ether1 file=eth1details.txt
:global eth1details [/file get "eth1details.txt" contents];
:local macstart [:find $eth1details "orig"];
:local mac [:pick $eth1details ($macstart +17) ($macstart +34)];

# Get identity variable
:local identity [:system identity get value-name=name];

# Get LTE1 info, set signal and technology variables
:interface lte info lte1 file="lte1info.txt"
:local lte1info [:file get lte1info.txt contents];
:local sigstart [:find $lte1info "signal"];
:local sigend [:find $lte1info "dBm" $sigstart];
:local signal [:pick $lte1info ($sigstart +16) ($sigend -1)];
:local techstart [:find $lte1info "access"];
:local techend [:find $lte1info "\n" $techstart];
:local techno [:pick $lte1info ($techstart +19) ($techend)];

:local technology;
:if ($techno ="GSM compact") do={[:set technology "GSM";]}
:if ($techno ="3G") do={:set technology "UMTS";}
:if ($techno ="Evolved 3G (LTE)") do={[:set technology "LTE";]}

:if ([:find $gpstext "yes" $validstart] > 0) do={:set valid true;};

:global longitude [:pick $gpstext ($longstart + 11) $longend];
:local degreestart [:find $longitude " " -1];
:local minutestart [:find $longitude " " $degreestart];
:local secondstart [:find $longitude "'" $minutestart];

:local secondend;
:local secfract;

:if ([:len [:find $longitude "." 0]] < 1) do={
    :set secondend [:find $longitude "'" $secondstart];
    :set secfract "0";
} else={
    :set secondend [:find $longitude "." $secondstart];
    :set secfract [:pick $longitude ($secondend + 1) ($secondend + 2)];
};

:local longdegree;
:local longdegreelink;

:if ([:pick $longitude 0 1] = "W") do={
    :set longdegree "-";
    :set longdegreelink "W";
} else={
    :set longdegree "+";
    :set longdegreelink "E";
};

:set longdegree ($longdegree . [:pick $longitude 2 $minutestart]);
:set longdegreelink ($longdegreelink . [:pick $longitude 2 $minutestart]);
:local longmin [:pick $longitude ($minutestart + 1) $secondstart];
:local longsec [:pick $longitude ($secondstart + 2) $secondend];
:local longfract ((([:tonum $longmin] * 6000) + ([:tonum $longsec] * 100) + ([:tonum $secfract] * 10) ) / 36);

:while (([:len $zeros] + [:len $longfract]) < 4) do={
    :set zeros ($zeros . "0");
};

:global newlong ($longdegree . "." . $zeros . $longfract);
:global newlonglink ($longdegreelink . "." . $zeros . $longfract);

:global latitude [:pick $gpstext (latstart + 10) $latend];
:set degreestart [:find $latitude " " -1];
:set minutestart [:find $latitude " " $degreestart];
:set secondstart [:find $latitude "'" $minutestart];

:if ([:len [:find $latitude "." 0]] < 1) do={
    :set secondend [:find $latitude "'" $secondstart];
    :set secfract "0";
} else={
    :set secondend [:find $latitude "." $secondstart];
    :set secfract [:pick $latitude ($secondend + 1) ($secondend +2)];
};

:local latdegree;
:local latdegreelink;

:if ([:pick $latitude 0 1] = "N") do={
    :set latdegree "+";
    :set latdegreelink "N";
} else={
    :set latdegree "-";
    :set latdegreelink "S";
};

:set latdegree ($latdegree . [:pick $latitude 2 $minutestart]);
:set latdegreelink ($latdegreelink . [:pick $latitude 2 $minutestart]);
:local latmin [:pick $latitude ($minutestart + 1) $secondstart];
:local latsec [:pick $latitude ($secondstart + 2) $secondend];
:local latfract ((([:tonum $latmin] * 6000) + ([:tonum $latsec] * 100) +([:tonum $secfract] * 10)) / 36);

:set zeros "";

:while (([:len $zeros] + [:len $latfract]) < 4) do={
    :set zeros ($zeros . "0");
};

:global newlat ($latdegree . "." . $zeros . $latfract);
:global newlatlink ($latdegreelink . "." . $zeros . $latfract);

:global coordinates ($newlong . "," . $newlat);

# SEND TO SERVER IF THE COORDINATES HAVE CHANGED
:if (valid) do={
    :global oldpos;

    :if ($oldpos != $coordinates) do={
        {
        :local urlstring "http://$server/mikrotikgps.php\?identity=$identity&mac=$mac&latitude=$latitude&longitude=$longitude&lat=$newlat&lng=$newlong&date=$date&dbm=$signal&technology=$technology&speed=$speed&altitude=$altitude&satellites=$satellites";
        :local urlEncoded;
        :for i from=0 to=([:len $urlstring] - 1) do={ 
          :local char [:pick $urlstring $i]
          :if ($char = " ") do={
            :set $char "%20"
          }
          :if ($char = "-") do={
            :set $char "%2D"
          }
          :if ($char = "+") do={
            :set $char "%2B"
          }
          :set urlEncoded ($urlEncoded . $char)
        }
        :tool fetch url="$urlEncoded" mode=http dst-path=gps-to-url;
        }
        :set oldpos $coordinates;
        :global counter;
        :set counter 0;
     };
} else={
         :global counter;
         :set counter ($counter + 1);
         :log info "GPS not valid, count = $counter";
         :if ($counter = 12) do={
         :system routerboard usb power-reset duration=1;
         :set counter 0;
};


File: /MC7710-enable-gps.txt
1 - Turn off "DirectiIP" mode.
/port firmware set ignore-directip-modem=yes

2 - Restart RouterOS.
/system reboot

3 - Open a terminal to the modem on the 3 channel.
/system serial-terminal usb1 channel=3

4 - Run the following AT commands.
AT!ENTERCND="A710"
AT!GPSAUTOSTART=1,1,255,1000,1

5 - Close the terminal session
> Ctrl+A >>>> Q

6 - Turn on "DirectiIP" mode.
/port firmware set ignore-directip-modem=no

7 - Restart RouterOS.
/system reboot

8 - Enable GPS.
/system gps set port=usb1 channel=0 enabled=yes

9 - Test the GPS is working.
/system gps monitor

[admin@MikroTik] > system gps monitor                             
        date-and-time: jan/01/2015 23:24:54
             latitude: N XX XX' XX.XXX''
            longitude: E XX XX' XX.XXX''
             altitude: 20.600000m
                speed: 0.000000 km/h
  destination-bearing: none
         true-bearing: 180.699997 deg. True
     magnetic-bearing: 180.699997 deg. Mag
                valid: yes
           satellites: 7
-- [Q quit|D dump|C-z pause]

If you see the above with latitude and longitude coordinates then GPS is working.
Copy and paste these to Google maps to check the accuracy.

NOTE: You will need a GPS antenna connected to the middle "GPS" u.fl connector and the GPS antenna will need to be outside 
(with a clear view of the sky) to work.


File: /mikrotikgps.php
<?php
// Create connection & CHANGE THE USER, PASSWORD AND DATABASE DETAILS
$con=mysqli_connect("localhost","user","password","database");

// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

// escape variables for security
$identity = mysqli_real_escape_string($con, $_GET['identity']);
$mac = mysqli_real_escape_string($con, $_GET['mac']);
$latitude = mysqli_real_escape_string($con, $_GET['latitude']);
$longitude = mysqli_real_escape_string($con, $_GET['longitude']);
$lat = mysqli_real_escape_string($con, $_GET['lat']);
$lng = mysqli_real_escape_string($con, $_GET['lng']);
$date = mysqli_real_escape_string($con, $_GET['date']);
$dbm = mysqli_real_escape_string($con, $_GET['dbm']);
$technology = mysqli_real_escape_string($con, $_GET['technology']);
$speed = mysqli_real_escape_string($con, $_GET['speed']);
$altitude = mysqli_real_escape_string($con, $_GET['altitude']);
$satellites = mysqli_real_escape_string($con, $_GET['satellites']);

$sql="INSERT INTO gps (identity, mac, latitude, longitude, lat, lng, date, dbm, technology, speed, altitude, satellites)
VALUES ('$identity', '$mac', '$latitude', '$longitude', '$lat', '$lng', $date', '$dbm', '$technology', '$speed', '$altitude', '$satellites')";

if (!mysqli_query($con,$sql)) {
  die('Error: ' . mysqli_error($con));
}
echo "1 record added";

mysqli_close($con);

//close mysql connection
mysqli_close($con);
?>


File: /mikrotiklocation.html
<!DOCTYPE html >
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>Mikrotik Location</title>
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js"></script>
    <script type="text/javascript">
    //<![CDATA[

    var customIcons = {
      LTE: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_blue.png'
      },
      UMTS: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_green.png'
      },
      GSM: {
        icon: 'http://labs.google.com/ridefinder/images/mm_20_red.png'
      },
    };

    function load() {
      var map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(51.2932,0.7908),
        zoom: 11,
        mapTypeId: 'roadmap'
      });
      var infoWindow = new google.maps.InfoWindow;

      // Change this depending on the name of your PHP file
      downloadUrl("mikrotik_genxml.php", function(data) {
        var xml = data.responseXML;
        var markers = xml.documentElement.getElementsByTagName("marker");
        for (var i = 0; i < markers.length; i++) {
          var identity = markers[i].getAttribute("identity");
          var mac = markers[i].getAttribute("mac");
          var date = markers[i].getAttribute("date");
          var technology = markers[i].getAttribute("technology");
          var dbm = markers[i].getAttribute("dbm");
          var point = new google.maps.LatLng(
              parseFloat(markers[i].getAttribute("lat")),
              parseFloat(markers[i].getAttribute("lng")));
          var speed = markers[i].getAttribute("speed");
          var altitude = markers[i].getAttribute("altitude");
          var satellites = markers[i].getAttribute("satellites");
          var html = "<b>" + identity + "</b> <br/>" + mac + " <br/>" + date + " <br/>" + technology + "&nbsp;" + dbm + "&nbsp;dBm <br/> Speed:&nbsp;" + speed + "&nbsp;km/h<br/> Altitude:&nbsp;" + altitude + "&nbsp;meters<br/>Satellites in view:&nbsp" + satellites + "";
          var icon = customIcons[technology] || {};
          var marker = new google.maps.Marker({
            map: map,
            position: point,
            icon: icon.icon
          });
          bindInfoWindow(marker, map, infoWindow, html);
        }
      });
    }

    function bindInfoWindow(marker, map, infoWindow, html) {
      google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
      });
    }

    function downloadUrl(url, callback) {
      var request = window.ActiveXObject ?
          new ActiveXObject('Microsoft.XMLHTTP') :
          new XMLHttpRequest;

      request.onreadystatechange = function() {
        if (request.readyState == 4) {
          request.onreadystatechange = doNothing;
          callback(request, request.status);
        }
      };

      request.open('GET', url, true);
      request.send(null);
    }

    function doNothing() {}

    //]]>

  </script>
  
  </head>
  
  <body onload="load()">
    <div id="map" style="width: 1000px; height: 500px"></div>
  </body>
  
</html>


File: /mikrotik_genxml.php
<?php

require("phpsqlajax_dbinfo.php");

// Start XML file, create parent node

$dom = new DOMDocument("1.0");
$node = $dom->createElement("markers");
$parnode = $dom->appendChild($node);

// Opens a connection to a MySQL server

$connection=mysql_connect ('localhost', $username, $password);
if (!$connection) {  die('Not connected : ' . mysql_error());}

// Set the active MySQL database

$db_selected = mysql_select_db($database, $connection);
if (!$db_selected) {
  die ('Can\'t use db : ' . mysql_error());
}

// Select only markers that are less than a day old
 $query = "SELECT * FROM  `gps` WHERE `datetime` >= NOW() - INTERVAL 1 DAY";

$result = mysql_query($query);
if (!$result) {
  die('Invalid query: ' . mysql_error());
}

header("Content-type: text/xml");

// Iterate through the rows, adding XML nodes for each

while ($row = @mysql_fetch_assoc($result)){
  // ADD TO XML DOCUMENT NODE
  $node = $dom->createElement("marker");
  $newnode = $parnode->appendChild($node);
  $newnode->setAttribute("identity",$row['identity']);
  $newnode->setAttribute("mac", $row['mac']);
  $newnode->setAttribute("date", $row['datetime']);
  $newnode->setAttribute("lat", $row['lat']);
  $newnode->setAttribute("lng", $row['lng']);
  $newnode->setAttribute("dbm", $row['dbm']);
  $newnode->setAttribute("technology", $row['technology']);
  $newnode->setAttribute("speed", $row['speed']);
  $newnode->setAttribute("altitude", $row['altitude']);
  $newnode->setAttribute("satellites", $row['satellites']);
}

echo $dom->saveXML();

?>


File: /phpsqlajax_dbinfo.php
<?
$username="changeme";
$password="changeme";
$database="changeme";
?>


File: /README.md
mikrotik-gps
============

Scripts for tracking Mikrotik Routers by sending GPS coordinates to an e-mail address.

Requires a Mikrotik RoutherBoard + USB GPS device or LTE modem with built-in GPS receiver.

gps-to-email script originally from the Mikrotik Wiki:-
http://wiki.mikrotik.com/wiki/GPS_text_file_converter_to_Google_Earth/Maps

Testing done using a RB912UAG-2HPnD with Sierra Wireless MC7710 (FW version needs to be "03.05.24" and GPS autostart NMEA output needs to be enabled. See "MC7710-enable-gps.txt" for instructions.

/!\ PLEASE NOTE /!\
-------------

The GPS package doesn't work correctly in the current firmware release (RouterOS v6.24) you'll need to upgrade to "RouterOS v6.25rc" once available and the final release as soon as that is available.

gps-to-email
------------

Script to send the GPS coordinated to an e-mail address.
E-Mails are only sent when the position has changed.
The script has to be scheduled to run using "system scheduler". Depending on your requirements this could be scheduled to run the gps-to-email script every 20 seconds, 5 minutes, 30 minutes, hour or daily.

gps-to-url
----------

This script is a modified version of the above gps-to-email script. Instead of sending an e-mail it uses fetch to request a URL. This URL is the "mikrotikgps.php" file which uses php GET to get the data from the URL and push it into a database. This makes it possible to then use this data to build a map using the coordinates and other data. 


File: /schedule-command
system script run gps-to-email;


File: /usb-reset
system routerboard usb power-reset duration=1;


