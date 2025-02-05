# Repository Information
Name: mibs-snmp-mikrotik

# Directory Structure
Directory structure:
└── github_repos/mibs-snmp-mikrotik/
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
    │   │       ├── pack-3d524d5062f22c4de69b45b99ac6e030e9a719e7.idx
    │   │       └── pack-3d524d5062f22c4de69b45b99ac6e030e9a719e7.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── mikrotik.mib
    ├── oid_lib.oidlib
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
	url = https://github.com/Full-Monitoring/mibs-snmp-mikrotik.git
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
0000000000000000000000000000000000000000 1206e7e3a0a16c6d43e3968ec14d884848717bfb vivek-dodia <vivek.dodia@icloud.com> 1738606376 -0500	clone: from https://github.com/Full-Monitoring/mibs-snmp-mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 1206e7e3a0a16c6d43e3968ec14d884848717bfb vivek-dodia <vivek.dodia@icloud.com> 1738606376 -0500	clone: from https://github.com/Full-Monitoring/mibs-snmp-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 1206e7e3a0a16c6d43e3968ec14d884848717bfb vivek-dodia <vivek.dodia@icloud.com> 1738606376 -0500	clone: from https://github.com/Full-Monitoring/mibs-snmp-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
1206e7e3a0a16c6d43e3968ec14d884848717bfb refs/remotes/origin/main


File: /.git\refs\heads\main
1206e7e3a0a16c6d43e3968ec14d884848717bfb


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto


File: /mikrotik.mib
MIKROTIK-MIB DEFINITIONS ::= BEGIN

IMPORTS
InetAddressType, InetAddress, InetPortNumber FROM INET-ADDRESS-MIB
MODULE-IDENTITY, OBJECT-TYPE, Integer32, Counter32, Gauge32, IpAddress,
Counter64, enterprises, NOTIFICATION-TYPE, TimeTicks FROM SNMPv2-SMI
TEXTUAL-CONVENTION, DisplayString, MacAddress, DateAndTime FROM SNMPv2-TC
OBJECT-GROUP, NOTIFICATION-GROUP FROM SNMPv2-CONF;

mikrotikExperimentalModule MODULE-IDENTITY
  LAST-UPDATED "202106180000Z"
  ORGANIZATION "MikroTik"
  CONTACT-INFO "support@mikrotik.com"
  DESCRIPTION ""
  REVISION "202106180000Z"
  DESCRIPTION ""
  ::= { mikrotik 1 }

mikrotik OBJECT IDENTIFIER ::= { enterprises 14988 }
mtXMetaInfo OBJECT IDENTIFIER ::= { mikrotikExperimentalModule 2 }
mtXRouterOsGroups OBJECT IDENTIFIER ::= { mtXMetaInfo 1 }

mtXRouterOs OBJECT IDENTIFIER ::= { mikrotikExperimentalModule 1 }
mtxrWireless OBJECT IDENTIFIER ::= { mtXRouterOs 1 }
mtxrQueues OBJECT IDENTIFIER ::= { mtXRouterOs 2 }
mtxrHealth OBJECT IDENTIFIER ::= { mtXRouterOs 3 }
mtxrLicense OBJECT IDENTIFIER ::= { mtXRouterOs 4 }
mtxrHotspot OBJECT IDENTIFIER ::= { mtXRouterOs 5 }
mtxrDHCP OBJECT IDENTIFIER ::= { mtXRouterOs 6 }
mtxrSystem OBJECT IDENTIFIER ::= { mtXRouterOs 7 }
mtxrScripts OBJECT IDENTIFIER ::= { mtXRouterOs 8 }
mtxrTraps OBJECT IDENTIFIER ::= { mtXRouterOs 9 }
mtxrNstremeDual OBJECT IDENTIFIER ::= { mtXRouterOs 10 }
mtxrNeighbor OBJECT IDENTIFIER ::= { mtXRouterOs 11 }
mtxrGps OBJECT IDENTIFIER ::= { mtXRouterOs 12 }
mtxrWirelessModem OBJECT IDENTIFIER ::= { mtXRouterOs 13 }
mtxrInterfaceStats OBJECT IDENTIFIER ::= { mtXRouterOs 14 }
mtxrPOE OBJECT IDENTIFIER ::= { mtXRouterOs 15 }
mtxrLTEModem OBJECT IDENTIFIER ::= { mtXRouterOs 16 }
mtxrPartition OBJECT IDENTIFIER ::= { mtXRouterOs 17 }
mtxrScriptRun OBJECT IDENTIFIER ::= { mtXRouterOs 18 }
mtxrOptical OBJECT IDENTIFIER ::= { mtXRouterOs 19 }
mtxrIPSec OBJECT IDENTIFIER ::= { mtXRouterOs 20 }

ObjectIndex ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "x"
    STATUS current
    DESCRIPTION "Internal "
    SYNTAX Integer32 (0..2147483647)
-- Note that actually in RouterOs index values can be in range 0..4294967294,
-- this can sometimes make them negative. Any of the following syntaxes would
-- be more appropriate, but since Integer32 is used for InterfaceIndex in
-- IF-MIB, where it can also take negative values in RouterOs, it is used
-- here for consistency.
-- Also note that ObjectIndex value is not related to item numbers that are
-- used by console and shown by console print command.
--
-- SYNTAX Integer32 (-2147483648..2147483647)
-- SYNTAX Unsigned32 (0..4294967295)

HexInt ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "x"
    STATUS current
    DESCRIPTION "Hex"
    SYNTAX Integer32 (-2147483648..2147483647)

Voltage ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-1"
    STATUS current
    DESCRIPTION ""
    SYNTAX Integer32 (-2147483648..2147483647)

Temperature ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-1"
    STATUS current
    DESCRIPTION ""
    SYNTAX Integer32 (-2147483648..2147483647)

Power ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-1"
    STATUS current
    DESCRIPTION ""
    SYNTAX Integer32 (-2147483648..2147483647)

GDiv100 ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-2"
    STATUS current
    DESCRIPTION "/100"
    SYNTAX Gauge32

GDiv1000 ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-3"
    STATUS current
    DESCRIPTION "/1000"
    SYNTAX Gauge32

IDiv1000 ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-3"
    STATUS current
    DESCRIPTION "/1000"
    SYNTAX Integer32 (-2147483648..2147483647)

BoolValue ::= TEXTUAL-CONVENTION
    STATUS       current
    DESCRIPTION
    "Boolean value."
    SYNTAX       INTEGER { false(0), true(1) }

IsakmpCookie ::= TEXTUAL-CONVENTION
    DISPLAY-HINT    "16a"
    STATUS          current
    DESCRIPTION "ISAKMP cookie string"
    SYNTAX  OCTET STRING (SIZE (16))

-- WIRELESS ********************************************************************

mtxrWlStatTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlStatEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 1 }

mtxrWlStatEntry OBJECT-TYPE
    SYNTAX MtxrWlStatEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Wireless station mode interface"
    INDEX { mtxrWlStatIndex }
    ::= { mtxrWlStatTable 1 }

MtxrWlStatEntry ::= SEQUENCE {
    mtxrWlStatIndex ObjectIndex,
    mtxrWlStatTxRate Gauge32,
    mtxrWlStatRxRate Gauge32,
    mtxrWlStatStrength Integer32,
    mtxrWlStatSsid DisplayString,
    mtxrWlStatBssid MacAddress,
    mtxrWlStatFreq Integer32,
    mtxrWlStatBand DisplayString,
    mtxrWlStatTxCCQ Counter32,
    mtxrWlStatRxCCQ Counter32
}

mtxrWlStatIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 1 }

mtxrWlStatTxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlStatEntry 2 }

mtxrWlStatRxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlStatEntry 3 }

mtxrWlStatStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrWlStatEntry 4 }

mtxrWlStatSsid OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 5 }

mtxrWlStatBssid OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 6 }

mtxrWlStatFreq OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "megahertz"
    ::= { mtxrWlStatEntry 7 }

mtxrWlStatBand OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 8 }

mtxrWlStatTxCCQ OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 9 }

mtxrWlStatRxCCQ OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlStatEntry 10 }

-- WlRtabTable
mtxrWlRtabTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlRtabEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 2 }

mtxrWlRtabEntry OBJECT-TYPE
    SYNTAX MtxrWlRtabEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Wireless registration table. It is indexed by remote
        mac-address and local interface index"
    INDEX { mtxrWlRtabAddr, mtxrWlRtabIface }
    ::= { mtxrWlRtabTable 1 }

MtxrWlRtabEntry ::= SEQUENCE {
    mtxrWlRtabAddr MacAddress,
    mtxrWlRtabIface ObjectIndex,
    mtxrWlRtabStrength Integer32,
    mtxrWlRtabTxBytes Counter32,
    mtxrWlRtabRxBytes Counter32,
    mtxrWlRtabTxPackets Counter32,
    mtxrWlRtabRxPackets Counter32,
    mtxrWlRtabTxRate Gauge32,
    mtxrWlRtabRxRate Gauge32,
    mtxrWlRtabRouterOSVersion DisplayString,
    mtxrWlRtabUptime TimeTicks,
    mtxrWlRtabSignalToNoise Integer32,
    mtxrWlRtabTxStrengthCh0 Integer32,
    mtxrWlRtabRxStrengthCh0 Integer32,
    mtxrWlRtabTxStrengthCh1 Integer32,
    mtxrWlRtabRxStrengthCh1 Integer32,
    mtxrWlRtabTxStrengthCh2 Integer32,
    mtxrWlRtabRxStrengthCh2 Integer32,
    mtxrWlRtabTxStrength Integer32,
    mtxrWlRtabRadioName DisplayString
}

mtxrWlRtabAddr OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 1 }

mtxrWlRtabIface OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 2 }

mtxrWlRtabStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrWlRtabEntry 3 }

mtxrWlRtabTxBytes OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 4 }

mtxrWlRtabRxBytes OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 5 }

mtxrWlRtabTxPackets OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 6 }

mtxrWlRtabRxPackets OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 7 }

mtxrWlRtabTxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlRtabEntry 8 }

mtxrWlRtabRxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlRtabEntry 9 }

mtxrWlRtabRouterOSVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "RouterOS version"
    ::= { mtxrWlRtabEntry 10 }

mtxrWlRtabUptime OBJECT-TYPE
    SYNTAX TimeTicks
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "uptime"
    ::= { mtxrWlRtabEntry 11 }

mtxrWlRtabSignalToNoise OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Measured in dB, if value does not exist it is indicated with 0"
    ::= { mtxrWlRtabEntry 12 }

mtxrWlRtabTxStrengthCh0 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 13 }

mtxrWlRtabRxStrengthCh0 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 14 }

mtxrWlRtabTxStrengthCh1 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 15 }

mtxrWlRtabRxStrengthCh1 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 16 }

mtxrWlRtabTxStrengthCh2 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 17 }

mtxrWlRtabRxStrengthCh2 OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 18 }

mtxrWlRtabTxStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 19 }

mtxrWlRtabRadioName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlRtabEntry 20 }

mtxrWlRtabEntryCount OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Wireless registration table entry count"
    ::= { mtxrWireless 4 }

mtxrWlApTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlApEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 3 }

mtxrWlApEntry OBJECT-TYPE
    SYNTAX MtxrWlApEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Wireless access point mode interface"
    INDEX { mtxrWlApIndex }
    ::= { mtxrWlApTable 1 }

MtxrWlApEntry ::= SEQUENCE {
    mtxrWlApIndex ObjectIndex,
    mtxrWlApTxRate Gauge32,
    mtxrWlApRxRate Gauge32,
    mtxrWlApSsid DisplayString,
    mtxrWlApBssid MacAddress,
    mtxrWlApClientCount Counter32,
    mtxrWlApFreq Integer32,
    mtxrWlApBand DisplayString,
    mtxrWlApNoiseFloor Integer32,
    mtxrWlApOverallTxCCQ Counter32,
    mtxrWlApAuthClientCount Counter32
}

mtxrWlApIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 1 }

mtxrWlApTxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlApEntry 2 }

mtxrWlApRxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlApEntry 3 }

mtxrWlApSsid OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 4 }

mtxrWlApBssid OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 5 }

mtxrWlApClientCount OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 6 }

mtxrWlApFreq OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "megahertz"
    ::= { mtxrWlApEntry 7 }

mtxrWlApBand OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 8 }

mtxrWlApNoiseFloor OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 9 }

mtxrWlApOverallTxCCQ OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 10 }

mtxrWlApAuthClientCount OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlApEntry 11 }

mtxrWlCMRtabTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlCMRtabEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 5 }

mtxrWlCMRtabEntry OBJECT-TYPE
    SYNTAX MtxrWlCMRtabEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Wireless CAPSMAN registration table. It is indexed by remote
        mac-address and local interface index"
    INDEX { mtxrWlCMRtabAddr, mtxrWlCMRtabIface }
    ::= { mtxrWlCMRtabTable 1 }

MtxrWlCMRtabEntry ::= SEQUENCE {
    mtxrWlCMRtabAddr MacAddress,
    mtxrWlCMRtabIface ObjectIndex,
    mtxrWlCMRtabUptime TimeTicks,
    mtxrWlCMRtabTxBytes Counter32,
    mtxrWlCMRtabRxBytes Counter32,
    mtxrWlCMRtabTxPackets Counter32,
    mtxrWlCMRtabRxPackets Counter32,
    mtxrWlCMRtabTxRate Gauge32,
    mtxrWlCMRtabRxRate Gauge32,
    mtxrWlCMRtabTxStrength Integer32,
    mtxrWlCMRtabRxStrength Integer32,
    mtxrWlCMRtabSsid DisplayString,
    mtxrWlCMRtabEapIdent DisplayString
}

mtxrWlCMRtabAddr OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 1 }
    -- should not be accessible in SMIv2

mtxrWlCMRtabIface OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 2 }

mtxrWlCMRtabUptime OBJECT-TYPE
    SYNTAX TimeTicks
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "uptime"
    ::= { mtxrWlCMRtabEntry 3 }

mtxrWlCMRtabTxBytes OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 4 }

mtxrWlCMRtabRxBytes OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 5 }

mtxrWlCMRtabTxPackets OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 6 }

mtxrWlCMRtabRxPackets OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 7 }

mtxrWlCMRtabTxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlCMRtabEntry 8 }

mtxrWlCMRtabRxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrWlCMRtabEntry 9 }

mtxrWlCMRtabTxStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 10 }

mtxrWlCMRtabRxStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 11 }

mtxrWlCMRtabSsid OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 12 }

mtxrWlCMRtabEapIdent OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRtabEntry 13 }

mtxrWlCMRtabEntryCount OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Wireless CAPSMAN registration table entry count"
    ::= { mtxrWireless 6 }

mtxrWlCMREntryCount OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Wireless CAPSMAN remote-cap entry count"
    ::= { mtxrWireless 10 }

mtxrWlCMTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlCMEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 7 }

mtxrWlCMEntry OBJECT-TYPE
    SYNTAX MtxrWlCMEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "CAPS-MAN mode interface"
    INDEX { mtxrWlCMIndex }
    ::= { mtxrWlCMTable 1 }

MtxrWlCMEntry ::= SEQUENCE {
    mtxrWlCMIndex ObjectIndex,
    mtxrWlCMRegClientCount Counter32,
    mtxrWlCMAuthClientCount Counter32,
    mtxrWlCMState DisplayString,
    mtxrWlCMChannel DisplayString
}

mtxrWlCMIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMEntry 1 }

mtxrWlCMRegClientCount OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMEntry 2 }

mtxrWlCMAuthClientCount OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMEntry 3 }

mtxrWlCMState OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMEntry 4 }

mtxrWlCMChannel OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "for master only"
    ::= { mtxrWlCMEntry 5 }

--
mtxrWlCMRemoteTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWlCMRemoteEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 11 }

mtxrWlCMRemoteEntry OBJECT-TYPE
    SYNTAX MtxrWlCMRemoteEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "CAPSMAN remote-cap list"
    INDEX { mtxrWlCMRemoteIndex }
    ::= { mtxrWlCMRemoteTable 1 }

MtxrWlCMRemoteEntry ::= SEQUENCE {
    mtxrWlCMRemoteIndex ObjectIndex,
    mtxrWlCMRemoteName DisplayString,
    mtxrWlCMRemoteState DisplayString,
    mtxrWlCMRemoteAddress DisplayString,
    mtxrWlCMRemoteRadios Counter32
}

mtxrWlCMRemoteIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRemoteEntry 1 }

mtxrWlCMRemoteName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRemoteEntry 2 }

mtxrWlCMRemoteState OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRemoteEntry 3 }

mtxrWlCMRemoteAddress OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRemoteEntry 4 }

mtxrWlCMRemoteRadios OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWlCMRemoteEntry 5 }

-- W60G
mtxrWl60GTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWl60GEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 8 }

mtxrWl60GEntry OBJECT-TYPE
    SYNTAX MtxrWl60GEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "W60G interface"
    INDEX { mtxrWl60GIndex }
    ::= { mtxrWl60GTable 1 }

MtxrWl60GEntry ::= SEQUENCE {
    mtxrWl60GIndex ObjectIndex,
    mtxrWl60GMode INTEGER,
    mtxrWl60GSsid DisplayString,
    mtxrWl60GConnected BoolValue,
    mtxrWl60GRemote MacAddress,
    mtxrWl60GFreq Integer32,
    mtxrWl60GMcs Integer32,
    mtxrWl60GSignal Integer32,
    mtxrWl60GTxSector Integer32,
    mtxrWl60GTxSectorInfo DisplayString,
    mtxrWl60GRssi Integer32,
    mtxrWl60GPhyRate Gauge32
}

mtxrWl60GIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 1 }

mtxrWl60GMode OBJECT-TYPE
    SYNTAX INTEGER {
        apBridge(0),
        stationBridge(1),
        sniff(2),
        bridge(3)
    }
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 2 }

mtxrWl60GSsid OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 3 }

mtxrWl60GConnected OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 4 }

mtxrWl60GRemote OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 5 }

mtxrWl60GFreq OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Mhz"
    ::= { mtxrWl60GEntry 6 }

mtxrWl60GMcs OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 7 }

mtxrWl60GSignal OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 8 }

mtxrWl60GTxSector OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 9 }

mtxrWl60GTxSectorInfo OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 11 }

mtxrWl60GRssi OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 12 }

mtxrWl60GPhyRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GEntry 13 }

-- W60GSta
mtxrWl60GStaTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrWl60GStaEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWireless 9 }

mtxrWl60GStaEntry OBJECT-TYPE
    SYNTAX MtxrWl60GStaEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "W60G stations"
    INDEX { mtxrWl60GStaIndex }
    ::= { mtxrWl60GStaTable 1 }

MtxrWl60GStaEntry ::= SEQUENCE {
    mtxrWl60GStaIndex ObjectIndex,
    mtxrWl60GStaConnected BoolValue,
    mtxrWl60GStaRemote MacAddress,
    mtxrWl60GStaMcs Integer32,
    mtxrWl60GStaSignal Integer32,
    mtxrWl60GStaTxSector Integer32,
    mtxrWl60GStaPhyRate Gauge32,
    mtxrWl60GStaRssi Integer32,
    mtxrWl60GStaDistance Integer32
}

mtxrWl60GStaIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 1 }

mtxrWl60GStaConnected OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 2 }

mtxrWl60GStaRemote OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 3 }

mtxrWl60GStaMcs OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 4 }

mtxrWl60GStaSignal OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 5 }

mtxrWl60GStaTxSector OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 6 }

mtxrWl60GStaPhyRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Mbits per second"
    ::= { mtxrWl60GStaEntry 8 }

mtxrWl60GStaRssi OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrWl60GStaEntry 9 }

mtxrWl60GStaDistance OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "meters"
    ::= { mtxrWl60GStaEntry 10 }


mtxrWirelessGroup OBJECT-GROUP OBJECTS {
        mtxrWlStatTxRate,
	mtxrWlStatRxRate,
	mtxrWlStatStrength,
	mtxrWlStatSsid,
        mtxrWlStatBssid,
	mtxrWlStatFreq,
	mtxrWlStatBand,
        mtxrWlStatTxCCQ,
        mtxrWlStatRxCCQ,
	mtxrWlRtabStrength,
	mtxrWlRtabTxBytes,
        mtxrWlRtabRxBytes,
	mtxrWlRtabTxPackets,
	mtxrWlRtabRxPackets,
        mtxrWlRtabTxRate,
	mtxrWlRtabRxRate,
	mtxrWlRtabEntryCount,
        mtxrWlRtabRouterOSVersion,
        mtxrWlRtabUptime,
        mtxrWlRtabSignalToNoise,
        mtxrWlRtabTxStrengthCh0,
        mtxrWlRtabRxStrengthCh0,
        mtxrWlRtabTxStrengthCh1,
        mtxrWlRtabRxStrengthCh1,
        mtxrWlRtabTxStrengthCh2,
        mtxrWlRtabRxStrengthCh2,
        mtxrWlRtabTxStrength,
        mtxrWlRtabRadioName,
        mtxrWlApTxRate,
	mtxrWlApRxRate,
	mtxrWlApSsid,
        mtxrWlApBssid,
        mtxrWlApClientCount,
        mtxrWlApBand,
        mtxrWlApFreq,
        mtxrWlApNoiseFloor,
        mtxrWlApOverallTxCCQ,
        mtxrWlApAuthClientCount,
        mtxrWlCMRtabAddr,
        mtxrWlCMRtabTxBytes,
        mtxrWlCMRtabRxBytes,
        mtxrWlCMRtabTxPackets,
        mtxrWlCMRtabRxPackets,
        mtxrWlCMRtabTxRate,
        mtxrWlCMRtabRxRate,
        mtxrWlCMRtabUptime,
        mtxrWlCMRtabTxStrength,
        mtxrWlCMRtabRxStrength,
        mtxrWlCMRtabSsid,
        mtxrWlCMRtabEntryCount,
        mtxrWlCMREntryCount,
        mtxrWlCMRegClientCount,
        mtxrWlCMAuthClientCount,
        mtxrWl60GMode,
        mtxrWl60GSsid,
        mtxrWl60GConnected,
        mtxrWl60GRemote,
        mtxrWl60GFreq,
        mtxrWl60GMcs,
        mtxrWl60GSignal,
        mtxrWl60GTxSector,
        mtxrWl60GTxSectorInfo,
        mtxrWl60GRssi,
        mtxrWl60GPhyRate,
        mtxrWl60GStaConnected,
        mtxrWl60GStaRemote,
        mtxrWl60GStaMcs,
        mtxrWl60GStaSignal,
        mtxrWl60GStaTxSector
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 1 }

-- QUEUES ********************************************************************

mtxrQueueSimpleTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrQueueSimpleEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueues 1 }

mtxrQueueSimpleEntry OBJECT-TYPE
    SYNTAX MtxrQueueSimpleEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Simple queue"
    INDEX { mtxrQueueSimpleIndex }
    ::= { mtxrQueueSimpleTable 1 }

MtxrQueueSimpleEntry ::= SEQUENCE {
    mtxrQueueSimpleIndex ObjectIndex,
    mtxrQueueSimpleName DisplayString,
    mtxrQueueSimpleSrcAddr IpAddress,
    mtxrQueueSimpleSrcMask IpAddress,
    mtxrQueueSimpleDstAddr IpAddress,
    mtxrQueueSimpleDstMask IpAddress,
    mtxrQueueSimpleIface ObjectIndex,
    mtxrQueueSimpleBytesIn Counter64,
    mtxrQueueSimpleBytesOut Counter64,
    mtxrQueueSimplePacketsIn Counter32,
    mtxrQueueSimplePacketsOut Counter32,
    mtxrQueueSimplePCQQueuesIn Counter32,
    mtxrQueueSimplePCQQueuesOut Counter32,
    mtxrQueueSimpleDroppedIn Counter32,
    mtxrQueueSimpleDroppedOut Counter32
}

mtxrQueueSimpleIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 1 }

mtxrQueueSimpleName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 2 }

mtxrQueueSimpleSrcAddr OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 3 }

mtxrQueueSimpleSrcMask OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 4 }

mtxrQueueSimpleDstAddr OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 5 }

mtxrQueueSimpleDstMask OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 6 }

mtxrQueueSimpleIface OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "interface index"
    ::= { mtxrQueueSimpleEntry 7 }

mtxrQueueSimpleBytesIn OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 8 }

mtxrQueueSimpleBytesOut OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 9 }

mtxrQueueSimplePacketsIn OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 10 }

mtxrQueueSimplePacketsOut OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 11 }

mtxrQueueSimplePCQQueuesIn OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 12 }

mtxrQueueSimplePCQQueuesOut OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 13 }

mtxrQueueSimpleDroppedIn OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 14 }

mtxrQueueSimpleDroppedOut OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueSimpleEntry 15 }

mtxrQueueTreeTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrQueueTreeEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueues 2 }

mtxrQueueTreeEntry OBJECT-TYPE
    SYNTAX MtxrQueueTreeEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Tree queue"
    INDEX { mtxrQueueTreeIndex }
    ::= { mtxrQueueTreeTable 1 }

MtxrQueueTreeEntry ::= SEQUENCE {
    mtxrQueueTreeIndex ObjectIndex,
    mtxrQueueTreeName DisplayString,
    mtxrQueueTreeFlow DisplayString,
    mtxrQueueTreeParentIndex ObjectIndex,
    mtxrQueueTreeBytes Counter32,
    mtxrQueueTreePackets Counter32,
    mtxrQueueTreeHCBytes Counter64,
    mtxrQueueTreePCQQueues Counter32,
    mtxrQueueTreeDropped Counter32
}

mtxrQueueTreeIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 1 }

mtxrQueueTreeName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 2 }

mtxrQueueTreeFlow OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "flowmark"
    ::= { mtxrQueueTreeEntry 3 }

mtxrQueueTreeParentIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "index of parent tree queue or parent interface"
    ::= { mtxrQueueTreeEntry 4 }

mtxrQueueTreeBytes OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 5 }

mtxrQueueTreePackets OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 6 }

mtxrQueueTreeHCBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 7 }

mtxrQueueTreePCQQueues OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 8 }

mtxrQueueTreeDropped OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrQueueTreeEntry 9 }

mtxrQueueGroup OBJECT-GROUP OBJECTS {
        mtxrQueueSimpleName, mtxrQueueSimpleSrcAddr, mtxrQueueSimpleSrcMask,
        mtxrQueueSimpleDstAddr, mtxrQueueSimpleDstMask, mtxrQueueSimpleIface,
        mtxrQueueSimpleBytesIn, mtxrQueueSimpleBytesOut,
        mtxrQueueSimplePacketsIn, mtxrQueueSimplePacketsOut, mtxrQueueTreeName,
        mtxrQueueSimplePCQQueuesIn,
        mtxrQueueSimplePCQQueuesOut,
        mtxrQueueSimpleDroppedIn,
        mtxrQueueSimpleDroppedOut,
        mtxrQueueTreeFlow, mtxrQueueTreeParentIndex, mtxrQueueTreeBytes,
        mtxrQueueTreePackets,
        mtxrQueueTreeHCBytes,
        mtxrQueueTreePCQQueues,
        mtxrQueueTreeDropped
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 2 }

-- HEALTH ********************************************************************

mtxrHlCoreVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "core voltage"
    ::= { mtxrHealth 1 }

mtxrHlThreeDotThreeVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "3.3V voltage"
    ::= { mtxrHealth 2 }

mtxrHlFiveVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "5V voltage"
    ::= { mtxrHealth 3 }

mtxrHlTwelveVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "12V voltage"
    ::= { mtxrHealth 4 }

mtxrHlSensorTemperature OBJECT-TYPE
    SYNTAX Temperature
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "temperature at sensor chip"
    ::= { mtxrHealth 5 }

mtxrHlCpuTemperature OBJECT-TYPE
    SYNTAX Temperature
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "temperature near cpu"
    ::= { mtxrHealth 6 }

mtxrHlBoardTemperature OBJECT-TYPE
    SYNTAX Temperature
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 7 }

mtxrHlVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 8 }

mtxrHlActiveFan OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 9 }

mtxrHlTemperature OBJECT-TYPE
    SYNTAX Temperature
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 10 }

mtxrHlProcessorTemperature OBJECT-TYPE
    SYNTAX Temperature
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 11 }

mtxrHlPower OBJECT-TYPE
    SYNTAX Power
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Watts"
    ::= { mtxrHealth 12 }

mtxrHlCurrent OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "mA"
    ::= { mtxrHealth 13 }

mtxrHlProcessorFrequency OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Mhz"
    ::= { mtxrHealth 14 }

mtxrHlPowerSupplyState OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "PSU state ok"
    ::= { mtxrHealth 15 }

mtxrHlBackupPowerSupplyState OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "backup PSU state ok"
    ::= { mtxrHealth 16 }

mtxrHlFanSpeed1 OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "rpm"
    ::= { mtxrHealth 17 }

mtxrHlFanSpeed2 OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "rpm"
    ::= { mtxrHealth 18 }

mtxrGaugeTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrGaugeTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHealth 100 }

mtxrGaugeTableEntry OBJECT-TYPE
    SYNTAX MtxrGaugeTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrGaugeIndex }
    ::= { mtxrGaugeTable 1 }

MtxrGaugeTableEntry ::= SEQUENCE {
    mtxrGaugeIndex ObjectIndex,
    mtxrGaugeName DisplayString,
    mtxrGaugeValue Gauge32,
    mtxrGaugeUnit INTEGER
}

mtxrGaugeIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrGaugeTableEntry 1 }

mtxrGaugeName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrGaugeTableEntry 2 }

mtxrGaugeValue OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrGaugeTableEntry 3 }

mtxrGaugeUnit OBJECT-TYPE
    SYNTAX INTEGER {
        celsius(1),
        rpm(2),
        dV(3),
        dA(4),
        dW(5),
        status(6)
    }
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "units"
    ::= { mtxrGaugeTableEntry 4 }

mtxrHealthGroup OBJECT-GROUP OBJECTS {
        mtxrHlCoreVoltage, mtxrHlThreeDotThreeVoltage, mtxrHlFiveVoltage,
        mtxrHlTwelveVoltage, mtxrHlSensorTemperature, mtxrHlCpuTemperature,
        mtxrHlBoardTemperature, mtxrHlVoltage, mtxrHlActiveFan, 
	mtxrHlTemperature, mtxrHlProcessorTemperature,
        mtxrHlCurrent, mtxrHlPower,
        mtxrHlProcessorFrequency,
        mtxrHlPowerSupplyState, mtxrHlBackupPowerSupplyState,
        mtxrHlFanSpeed1, mtxrHlFanSpeed2,
        mtxrGaugeName, mtxrGaugeValue, mtxrGaugeUnit
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 3 }

-- LICENSE ********************************************************************

mtxrLicSoftwareId OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "software id"
    ::= { mtxrLicense 1 }

mtxrLicUpgrUntil OBJECT-TYPE
    SYNTAX DateAndTime
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "current key allows upgrading until this date"
    ::= { mtxrLicense 2 }

mtxrLicLevel OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "current key level"
    ::= { mtxrLicense 3 }

mtxrLicVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "software version"
    ::= { mtxrLicense 4 }

mtxrLicUpgradableTo OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "upgradable to"
    ::= { mtxrLicense 5 }

mtxrLincenseGroup OBJECT-GROUP OBJECTS {
        mtxrLicSoftwareId, mtxrLicUpgrUntil, mtxrLicLevel, mtxrLicVersion, mtxrLicUpgradableTo
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 4 }

-- HOTSPOT ***************************************************************

mtxrHotspotActiveUsersTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrHotspotActiveUsersTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspot 1 }

mtxrHotspotActiveUsersTableEntry OBJECT-TYPE
    SYNTAX MtxrHotspotActiveUsersTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrHotspotActiveUserIndex }
    ::= { mtxrHotspotActiveUsersTable 1 }

MtxrHotspotActiveUsersTableEntry ::= SEQUENCE {
	mtxrHotspotActiveUserIndex ObjectIndex,
	mtxrHotspotActiveUserServerID Integer32,
	mtxrHotspotActiveUserName DisplayString,
	mtxrHotspotActiveUserDomain DisplayString,
	mtxrHotspotActiveUserIP IpAddress,
	mtxrHotspotActiveUserMAC MacAddress,
	mtxrHotspotActiveUserConnectTime Integer32,
	mtxrHotspotActiveUserValidTillTime Integer32,
	mtxrHotspotActiveUserIdleStartTime Integer32,
	mtxrHotspotActiveUserIdleTimeout Integer32,
	mtxrHotspotActiveUserPingTimeout Integer32,
	mtxrHotspotActiveUserBytesIn Counter64,
	mtxrHotspotActiveUserBytesOut Counter64,
	mtxrHotspotActiveUserPacketsIn Counter64,
	mtxrHotspotActiveUserPacketsOut Counter64,
	mtxrHotspotActiveUserLimitBytesIn Counter64,
	mtxrHotspotActiveUserLimitBytesOut Counter64,
	mtxrHotspotActiveUserAdvertStatus Integer32,
	mtxrHotspotActiveUserRadius Integer32,
	mtxrHotspotActiveUserBlockedByAdvert Integer32
}

mtxrHotspotActiveUserIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 1 }

mtxrHotspotActiveUserServerID OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 2 }

mtxrHotspotActiveUserName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 3 }

mtxrHotspotActiveUserDomain OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 4 }

mtxrHotspotActiveUserIP OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 5 }

mtxrHotspotActiveUserMAC OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 6 }

mtxrHotspotActiveUserConnectTime OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 7 }

mtxrHotspotActiveUserValidTillTime OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 8 }

mtxrHotspotActiveUserIdleStartTime OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 9 }

mtxrHotspotActiveUserIdleTimeout OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 10 }

mtxrHotspotActiveUserPingTimeout OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 11 }

mtxrHotspotActiveUserBytesIn OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 12 }

mtxrHotspotActiveUserBytesOut OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 13 }

mtxrHotspotActiveUserPacketsIn OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 14 }

mtxrHotspotActiveUserPacketsOut OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 15 }

mtxrHotspotActiveUserLimitBytesIn OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 16 }

mtxrHotspotActiveUserLimitBytesOut OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 17 }

mtxrHotspotActiveUserAdvertStatus OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 18 }

mtxrHotspotActiveUserRadius OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 19 }

mtxrHotspotActiveUserBlockedByAdvert OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrHotspotActiveUsersTableEntry 20 }

mtxrHotspotActiveUserGroup OBJECT-GROUP OBJECTS {
	mtxrHotspotActiveUserServerID,
	mtxrHotspotActiveUserName,
	mtxrHotspotActiveUserDomain,
	mtxrHotspotActiveUserIP,
	mtxrHotspotActiveUserMAC,
	mtxrHotspotActiveUserConnectTime,
	mtxrHotspotActiveUserValidTillTime,
	mtxrHotspotActiveUserIdleStartTime,
	mtxrHotspotActiveUserIdleTimeout,
	mtxrHotspotActiveUserPingTimeout,
	mtxrHotspotActiveUserBytesIn,
	mtxrHotspotActiveUserBytesOut,
	mtxrHotspotActiveUserPacketsIn,
	mtxrHotspotActiveUserPacketsOut,
	mtxrHotspotActiveUserLimitBytesIn,
	mtxrHotspotActiveUserLimitBytesOut,
	mtxrHotspotActiveUserAdvertStatus,
	mtxrHotspotActiveUserRadius,
	mtxrHotspotActiveUserBlockedByAdvert
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 5 }

-- DHCP ********************************************************************

mtxrDHCPLeaseCount OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrDHCP 1 }

mtxrDHCPGroup OBJECT-GROUP OBJECTS {
        mtxrDHCPLeaseCount
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 12 }

-- SYSTEM ********************************************************************

mtxrSystemReboot OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-write
    STATUS current
    DESCRIPTION "set non zero to reboot"
    ::= { mtxrSystem 1 }

mtxrUSBPowerReset OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-write
    STATUS current
    DESCRIPTION "switches off usb power for specified amout of seconds"
    ::= { mtxrSystem 2 }

mtxrSerialNumber OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "RouterBOARD serial number"
    ::= { mtxrSystem 3 }

mtxrFirmwareVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Current firmware version"
    ::= { mtxrSystem 4 }

mtxrNote OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "note"
    ::= { mtxrSystem 5 }

mtxrBuildTime OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "build time"
    ::= { mtxrSystem 6 }

mtxrFirmwareUpgradeVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "Upgrade firmware version"
    ::= { mtxrSystem 7 }

mtxrDisplayName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "display name"
    ::= { mtxrSystem 8 }

mtxrBoardName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "board name"
    ::= { mtxrSystem 9 }

mtxrSystemGroup OBJECT-GROUP OBJECTS {
        mtxrSystemReboot,
        mtxrUSBPowerReset,
        mtxrSerialNumber,
        mtxrFirmwareVersion,
        mtxrNote,
        mtxrBuildTime,
        mtxrFirmwareUpgradeVersion,
        mtxrBoardName
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 13 }

-- SCRIPTS ********************************************************************

mtxrScriptTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrScriptTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrScripts 1 }

mtxrScriptTableEntry OBJECT-TYPE
    SYNTAX MtxrScriptTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrScriptIndex }
    ::= { mtxrScriptTable 1 }

MtxrScriptTableEntry ::= SEQUENCE {
	mtxrScriptIndex ObjectIndex,
	mtxrScriptName DisplayString,
	mtxrScriptRunCmd Integer32
}

mtxrScriptIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrScriptTableEntry 1 }

mtxrScriptName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrScriptTableEntry 2 }

mtxrScriptRunCmd OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-write
    STATUS current
    DESCRIPTION "set non zero to run"
    ::= { mtxrScriptTableEntry 3 }

mtxrScriptGroup OBJECT-GROUP OBJECTS {
	mtxrScriptName, mtxrScriptRunCmd
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 8 }

-- SCRIPT RUN *****************************************************************

mtxrScriptRunTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrScriptRunTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "invisible to getnext, accesible only with get request and write premission"
    ::= { mtxrScriptRun 1 }

mtxrScriptRunTableEntry OBJECT-TYPE
    SYNTAX MtxrScriptRunTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrScriptRunIndex }
    ::= { mtxrScriptRunTable 1 }

MtxrScriptRunTableEntry ::= SEQUENCE {
	mtxrScriptRunIndex ObjectIndex,
	mtxrScriptRunOutput DisplayString
}

mtxrScriptRunIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrScriptRunTableEntry 1 }

mtxrScriptRunOutput OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "this oid on get request will run script and return it's output"
    ::= { mtxrScriptRunTableEntry 2 }

mtxrScriptRunGroup OBJECT-GROUP OBJECTS {
	mtxrScriptRunOutput
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 21 }

-- Dual Nstreme ***************************************************************

mtxrDnStatTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrDnStatEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNstremeDual 1 }

mtxrDnStatEntry OBJECT-TYPE
    SYNTAX MtxrDnStatEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Nstreme Dual interface"
    INDEX { mtxrDnStatIndex }
    ::= { mtxrDnStatTable 1 }

MtxrDnStatEntry ::= SEQUENCE {
    mtxrDnStatIndex ObjectIndex,
    mtxrDnStatTxRate Gauge32,
    mtxrDnStatRxRate Gauge32,
    mtxrDnStatTxStrength Integer32,
    mtxrDnStatRxStrength Integer32,
    mtxrDnConnected Integer32
}	

mtxrDnStatIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrDnStatEntry 1 }

mtxrDnStatTxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrDnStatEntry 2 }

mtxrDnStatRxRate OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "bits per second"
    ::= { mtxrDnStatEntry 3 }

mtxrDnStatTxStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrDnStatEntry 4 }

mtxrDnStatRxStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrDnStatEntry 5 }

mtxrDnConnected OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "0 - not connected, connected otherwise"
    ::= { mtxrDnStatEntry 6 }

mtxrNstremeDualGroup OBJECT-GROUP OBJECTS {
	mtxrDnStatTxRate, mtxrDnStatRxRate,
	mtxrDnStatTxStrength, mtxrDnStatRxStrength, mtxrDnConnected
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 10 }

-- NEIGHBOR *******************************************************************

mtxrNeighborTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrNeighborTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighbor 1 }

mtxrNeighborTableEntry OBJECT-TYPE
    SYNTAX MtxrNeighborTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrNeighborIndex }
    ::= { mtxrNeighborTable 1 }

MtxrNeighborTableEntry ::= SEQUENCE {
	mtxrNeighborIndex ObjectIndex,
	mtxrNeighborIpAddress IpAddress,
	mtxrNeighborMacAddress MacAddress,
	mtxrNeighborVersion DisplayString,
	mtxrNeighborPlatform DisplayString,
	mtxrNeighborIdentity DisplayString,
	mtxrNeighborSoftwareID DisplayString,
        mtxrNeighborInterfaceID ObjectIndex
}

mtxrNeighborIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 1 }

mtxrNeighborIpAddress OBJECT-TYPE
    SYNTAX IpAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 2 }

mtxrNeighborMacAddress OBJECT-TYPE
    SYNTAX MacAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 3 }

mtxrNeighborVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 4 }

mtxrNeighborPlatform OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 5 }

mtxrNeighborIdentity OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 6 }

mtxrNeighborSoftwareID OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 7 }

mtxrNeighborInterfaceID OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrNeighborTableEntry 8 }

mtxrNeighborGroup OBJECT-GROUP OBJECTS {
	mtxrNeighborIpAddress,
	mtxrNeighborMacAddress,
	mtxrNeighborVersion,
	mtxrNeighborPlatform,
	mtxrNeighborIdentity,
	mtxrNeighborSoftwareID,
	mtxrNeighborInterfaceID
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 11 }

-- GPS ************************************************************************

mtxrDate OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "UNIX time"
    ::= { mtxrGps 1 }

mtxrLongtitude OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "longtitude"
    ::= { mtxrGps 2 }

mtxrLatitude OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "latitude"
    ::= { mtxrGps 3 }

mtxrAltitude OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "altitude"
    ::= { mtxrGps 4 }

mtxrSpeed OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "speed"
    ::= { mtxrGps 5 }

mtxrSattelites OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "visible sattelite count"
    ::= { mtxrGps 6 }

mtxrValid OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "is the data valid"
    ::= { mtxrGps 7 }

mtxrGPSGroup OBJECT-GROUP OBJECTS {
        mtxrDate,
        mtxrLongtitude,
        mtxrLatitude,
        mtxrAltitude,
        mtxrSpeed,
        mtxrSattelites,
        mtxrValid
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 15 }

-- Wireless Modem ************************************************************

mtxrWirelessModemSignalStrength OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "signal strength in dBm (if first ppp-client modem supports)"
    ::= { mtxrWirelessModem 1 }

mtxrWirelessModemSignalECIO OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "signal EC/IO in dB (if first ppp-client modem supports)"
    ::= { mtxrWirelessModem 2 }

mtxrWirelessModemGroup OBJECT-GROUP OBJECTS {
        mtxrWirelessModemSignalStrength,
        mtxrWirelessModemSignalECIO
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 16 }

-- Interface Stats ************************************************************

mtxrInterfaceStatsTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrInterfaceStatsEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Extended interface statistics.
    Some interfaces may have only parts of this table
    with unavailable values set to zero."
    ::= { mtxrInterfaceStats 1 }

mtxrInterfaceStatsEntry OBJECT-TYPE
    SYNTAX MtxrInterfaceStatsEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrInterfaceStatsIndex }
    ::= { mtxrInterfaceStatsTable 1 }

MtxrInterfaceStatsEntry ::= SEQUENCE {
    mtxrInterfaceStatsIndex ObjectIndex,
    mtxrInterfaceStatsName DisplayString,

    mtxrInterfaceStatsDriverRxBytes Counter64,
    mtxrInterfaceStatsDriverRxPackets Counter64,
    mtxrInterfaceStatsDriverTxBytes Counter64,
    mtxrInterfaceStatsDriverTxPackets Counter64,

    mtxrInterfaceStatsTxRx64 Counter64,
    mtxrInterfaceStatsTxRx65To127 Counter64,
    mtxrInterfaceStatsTxRx128To255 Counter64,
    mtxrInterfaceStatsTxRx256To511 Counter64,
    mtxrInterfaceStatsTxRx512To1023 Counter64,
    mtxrInterfaceStatsTxRx1024To1518 Counter64,
    mtxrInterfaceStatsTxRx1519ToMax Counter64,

    mtxrInterfaceStatsRxBytes Counter64,
    mtxrInterfaceStatsRxPackets Counter64,
    mtxrInterfaceStatsRxTooShort Counter64,
    mtxrInterfaceStatsRx64 Counter64,
    mtxrInterfaceStatsRx65To127 Counter64,
    mtxrInterfaceStatsRx128To255 Counter64,
    mtxrInterfaceStatsRx256To511 Counter64,
    mtxrInterfaceStatsRx512To1023 Counter64,
    mtxrInterfaceStatsRx1024To1518 Counter64,
    mtxrInterfaceStatsRx1519ToMax Counter64,
    mtxrInterfaceStatsRxTooLong Counter64,
    mtxrInterfaceStatsRxBroadcast Counter64,
    mtxrInterfaceStatsRxPause Counter64,
    mtxrInterfaceStatsRxMulticast Counter64,
    mtxrInterfaceStatsRxFCSError Counter64,
    mtxrInterfaceStatsRxAlignError Counter64,
    mtxrInterfaceStatsRxFragment Counter64,
    mtxrInterfaceStatsRxOverflow Counter64,
    mtxrInterfaceStatsRxControl Counter64,
    mtxrInterfaceStatsRxUnknownOp Counter64,
    mtxrInterfaceStatsRxLengthError Counter64,
    mtxrInterfaceStatsRxCodeError Counter64,
    mtxrInterfaceStatsRxCarrierError Counter64,
    mtxrInterfaceStatsRxJabber Counter64,
    mtxrInterfaceStatsRxDrop Counter64,

    mtxrInterfaceStatsTxBytes Counter64,
    mtxrInterfaceStatsTxPackets Counter64,
    mtxrInterfaceStatsTxTooShort Counter64,
    mtxrInterfaceStatsTx64 Counter64,
    mtxrInterfaceStatsTx65To127 Counter64,
    mtxrInterfaceStatsTx128To255 Counter64,
    mtxrInterfaceStatsTx256To511 Counter64,
    mtxrInterfaceStatsTx512To1023 Counter64,
    mtxrInterfaceStatsTx1024To1518 Counter64,
    mtxrInterfaceStatsTx1519ToMax Counter64,
    mtxrInterfaceStatsTxTooLong Counter64,
    mtxrInterfaceStatsTxBroadcast Counter64,
    mtxrInterfaceStatsTxPause Counter64,
    mtxrInterfaceStatsTxMulticast Counter64,
    mtxrInterfaceStatsTxUnderrun Counter64,
    mtxrInterfaceStatsTxCollision Counter64,
    mtxrInterfaceStatsTxExcessiveCollision Counter64,
    mtxrInterfaceStatsTxMultipleCollision Counter64,
    mtxrInterfaceStatsTxSingleCollision Counter64,
    mtxrInterfaceStatsTxExcessiveDeferred Counter64,
    mtxrInterfaceStatsTxDeferred Counter64,
    mtxrInterfaceStatsTxLateCollision Counter64,
    mtxrInterfaceStatsTxTotalCollision Counter64,
    mtxrInterfaceStatsTxPauseHonored Counter64,
    mtxrInterfaceStatsTxDrop Counter64,
    mtxrInterfaceStatsTxJabber Counter64,
    mtxrInterfaceStatsTxFCSError Counter64,
    mtxrInterfaceStatsTxControl Counter64,
    mtxrInterfaceStatsTxFragment Counter64,
    mtxrInterfaceStatsLinkDowns Counter32
}

mtxrInterfaceStatsIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 1 }

mtxrInterfaceStatsName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 2 }

mtxrInterfaceStatsDriverRxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 11 }

mtxrInterfaceStatsDriverRxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 12 }

mtxrInterfaceStatsDriverTxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 13 }

mtxrInterfaceStatsDriverTxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 14 }

mtxrInterfaceStatsTxRx64 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 15 }

mtxrInterfaceStatsTxRx65To127 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 16 }

mtxrInterfaceStatsTxRx128To255 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 17 }

mtxrInterfaceStatsTxRx256To511 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 18 }

mtxrInterfaceStatsTxRx512To1023 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 19 }

mtxrInterfaceStatsTxRx1024To1518 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 20 }

mtxrInterfaceStatsTxRx1519ToMax OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 21 }

mtxrInterfaceStatsRxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 31 }
 
mtxrInterfaceStatsRxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 32 }

mtxrInterfaceStatsRxTooShort OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 33 }

mtxrInterfaceStatsRx64 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 34 }

mtxrInterfaceStatsRx65To127 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 35 }

mtxrInterfaceStatsRx128To255 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 36 }

mtxrInterfaceStatsRx256To511 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 37 }

mtxrInterfaceStatsRx512To1023 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 38 }

mtxrInterfaceStatsRx1024To1518 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 39 }

mtxrInterfaceStatsRx1519ToMax OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 40 }

mtxrInterfaceStatsRxTooLong OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 41 }

mtxrInterfaceStatsRxBroadcast OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 42 }

mtxrInterfaceStatsRxPause OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 43 }

mtxrInterfaceStatsRxMulticast OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 44 }

mtxrInterfaceStatsRxFCSError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 45 }

mtxrInterfaceStatsRxAlignError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 46 }

mtxrInterfaceStatsRxFragment OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 47 }

mtxrInterfaceStatsRxOverflow OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 48 }

mtxrInterfaceStatsRxControl OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 49 }

mtxrInterfaceStatsRxUnknownOp OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 50 }

mtxrInterfaceStatsRxLengthError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 51 }

mtxrInterfaceStatsRxCodeError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 52 }

mtxrInterfaceStatsRxCarrierError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 53 }

mtxrInterfaceStatsRxJabber OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 54 }

mtxrInterfaceStatsRxDrop OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 55 }

mtxrInterfaceStatsTxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 61 }

mtxrInterfaceStatsTxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 62 }

mtxrInterfaceStatsTxTooShort OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 63 }

mtxrInterfaceStatsTx64 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 64 }

mtxrInterfaceStatsTx65To127 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 65 }

mtxrInterfaceStatsTx128To255 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 66 }

mtxrInterfaceStatsTx256To511 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 67 }

mtxrInterfaceStatsTx512To1023 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 68 }

mtxrInterfaceStatsTx1024To1518 OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 69 }

mtxrInterfaceStatsTx1519ToMax OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 70 }

mtxrInterfaceStatsTxTooLong OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 71 }

mtxrInterfaceStatsTxBroadcast OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 72 }

mtxrInterfaceStatsTxPause OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 73 }

mtxrInterfaceStatsTxMulticast OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 74 }

mtxrInterfaceStatsTxUnderrun OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 75 }

mtxrInterfaceStatsTxCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 76 }

mtxrInterfaceStatsTxExcessiveCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 77 }

mtxrInterfaceStatsTxMultipleCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 78 }

mtxrInterfaceStatsTxSingleCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 79 }

mtxrInterfaceStatsTxExcessiveDeferred OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 80 }

mtxrInterfaceStatsTxDeferred OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 81 }

mtxrInterfaceStatsTxLateCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 82 }

mtxrInterfaceStatsTxTotalCollision OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 83 }

mtxrInterfaceStatsTxPauseHonored OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 84 }

mtxrInterfaceStatsTxDrop OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 85 }

mtxrInterfaceStatsTxJabber OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 86 }

mtxrInterfaceStatsTxFCSError OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 87 }

mtxrInterfaceStatsTxControl OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 88 }

mtxrInterfaceStatsTxFragment OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 89 }

mtxrInterfaceStatsLinkDowns OBJECT-TYPE
    SYNTAX Counter32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrInterfaceStatsEntry 90 }

mtxrInterfaceStatsGroup OBJECT-GROUP OBJECTS {
        mtxrInterfaceStatsName,
        mtxrInterfaceStatsDriverRxBytes,
        mtxrInterfaceStatsDriverRxPackets,
        mtxrInterfaceStatsDriverTxBytes,
        mtxrInterfaceStatsDriverTxPackets,

        mtxrInterfaceStatsTxRx64,
        mtxrInterfaceStatsTxRx65To127,
        mtxrInterfaceStatsTxRx128To255,
        mtxrInterfaceStatsTxRx256To511,
        mtxrInterfaceStatsTxRx512To1023,
        mtxrInterfaceStatsTxRx1024To1518,
        mtxrInterfaceStatsTxRx1519ToMax,

        mtxrInterfaceStatsRxBytes,
        mtxrInterfaceStatsRxPackets,
        mtxrInterfaceStatsRxTooShort,
        mtxrInterfaceStatsRx64,
        mtxrInterfaceStatsRx65To127,
        mtxrInterfaceStatsRx128To255,
        mtxrInterfaceStatsRx256To511,
        mtxrInterfaceStatsRx512To1023,
        mtxrInterfaceStatsRx1024To1518,
        mtxrInterfaceStatsRx1519ToMax,
        mtxrInterfaceStatsRxTooLong,
        mtxrInterfaceStatsRxBroadcast,
        mtxrInterfaceStatsRxPause,
        mtxrInterfaceStatsRxMulticast,
        mtxrInterfaceStatsRxFCSError,
        mtxrInterfaceStatsRxAlignError,
        mtxrInterfaceStatsRxFragment,
        mtxrInterfaceStatsRxOverflow,
        mtxrInterfaceStatsRxControl,
        mtxrInterfaceStatsRxUnknownOp,
        mtxrInterfaceStatsRxLengthError,
        mtxrInterfaceStatsRxCodeError,
        mtxrInterfaceStatsRxCarrierError,
        mtxrInterfaceStatsRxJabber,
        mtxrInterfaceStatsRxDrop,

        mtxrInterfaceStatsTxBytes,
        mtxrInterfaceStatsTxPackets,
        mtxrInterfaceStatsTxTooShort,
        mtxrInterfaceStatsTx64,
        mtxrInterfaceStatsTx65To127,
        mtxrInterfaceStatsTx128To255,
        mtxrInterfaceStatsTx256To511,
        mtxrInterfaceStatsTx512To1023,
        mtxrInterfaceStatsTx1024To1518,
        mtxrInterfaceStatsTx1519ToMax,
        mtxrInterfaceStatsTxTooLong,
        mtxrInterfaceStatsTxBroadcast,
        mtxrInterfaceStatsTxPause,
        mtxrInterfaceStatsTxMulticast,
        mtxrInterfaceStatsTxUnderrun,
        mtxrInterfaceStatsTxCollision,
        mtxrInterfaceStatsTxExcessiveCollision,
        mtxrInterfaceStatsTxMultipleCollision,
        mtxrInterfaceStatsTxSingleCollision,
        mtxrInterfaceStatsTxExcessiveDeferred,
        mtxrInterfaceStatsTxDeferred,
        mtxrInterfaceStatsTxLateCollision,
        mtxrInterfaceStatsTxTotalCollision,
        mtxrInterfaceStatsTxPauseHonored,
        mtxrInterfaceStatsTxDrop,
        mtxrInterfaceStatsTxJabber,
        mtxrInterfaceStatsTxFCSError,
        mtxrInterfaceStatsTxControl,
        mtxrInterfaceStatsTxFragment,
        mtxrInterfaceStatsLinkDowns
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 17 }

-- POE ************************************************************************

mtxrPOETable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrPOEEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "Power Over Ethernet"
    ::= { mtxrPOE 1 }

mtxrPOEEntry OBJECT-TYPE
    SYNTAX MtxrPOEEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrPOEInterfaceIndex }
    ::= { mtxrPOETable 1 }

MtxrPOEEntry ::= SEQUENCE {
    mtxrPOEInterfaceIndex ObjectIndex,
    mtxrPOEName DisplayString,
    mtxrPOEStatus INTEGER,
    mtxrPOEVoltage Voltage,
    mtxrPOECurrent Integer32,
    mtxrPOEPower Power
}

mtxrPOEInterfaceIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPOEEntry 1 }

mtxrPOEName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPOEEntry 2 }

mtxrPOEStatus OBJECT-TYPE
    SYNTAX INTEGER {
        disabled(1),
        waitingForLoad(2),
        poweredOn(3),
        overload(4)
    }
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPOEEntry 3 }

mtxrPOEVoltage OBJECT-TYPE
    SYNTAX Voltage
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "V"
    ::= { mtxrPOEEntry 4 }

mtxrPOECurrent OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "mA"
    ::= { mtxrPOEEntry 5 }

mtxrPOEPower OBJECT-TYPE
    SYNTAX Power
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "W"
    ::= { mtxrPOEEntry 6 }

mtxrPOEGroup OBJECT-GROUP OBJECTS {
        mtxrPOEName,
        mtxrPOEStatus,
        mtxrPOEVoltage,
        mtxrPOECurrent,
        mtxrPOEPower
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 18 }

-- LTE Modem ************************************************************

mtxrLTEModemTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrLTEModemEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "LTE Modems"
    ::= { mtxrLTEModem 1 }

mtxrLTEModemEntry OBJECT-TYPE
    SYNTAX MtxrLTEModemEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrLTEModemInterfaceIndex }
    ::= { mtxrLTEModemTable 1 }

MtxrLTEModemEntry ::= SEQUENCE {
    mtxrLTEModemInterfaceIndex ObjectIndex,
    mtxrLTEModemSignalRSSI Integer32,
    mtxrLTEModemSignalRSRQ Integer32,
    mtxrLTEModemSignalRSRP Integer32,
    mtxrLTEModemCellId HexInt,
    mtxrLTEModemAccessTechnology INTEGER,
    mtxrLTEModemSignalSINR Integer32,
    mtxrLTEModemEnbId Integer32,
    mtxrLTEModemSectorId Integer32,
    mtxrLTEModemLac Integer32,
    mtxrLTEModemIMEI DisplayString,
    mtxrLTEModemIMSI DisplayString,
    mtxrLTEModemUICC DisplayString,
    mtxrLTEModemRAT DisplayString
}

mtxrLTEModemInterfaceIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 1 }

mtxrLTEModemSignalRSSI OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrLTEModemEntry 2 }

mtxrLTEModemSignalRSRQ OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dB"
    ::= { mtxrLTEModemEntry 3 }

mtxrLTEModemSignalRSRP OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dBm"
    ::= { mtxrLTEModemEntry 4 }

mtxrLTEModemCellId OBJECT-TYPE
    SYNTAX HexInt
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "current cell ID"
    ::= { mtxrLTEModemEntry 5 }

mtxrLTEModemAccessTechnology OBJECT-TYPE
    SYNTAX INTEGER {
        unknown(-1),
        gsmcompact(0),
        gsm(1),
        utran(2),
        egprs(3),
        hsdpa(4),
        hsupa(5),
        hsdpahsupa(6),
        eutran(7),
        nr-sa(11),
        nr-nsa(13)
    }
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "as reported by +CREG"
    ::= { mtxrLTEModemEntry 6 }

mtxrLTEModemSignalSINR OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dB"
    ::= { mtxrLTEModemEntry 7 }

mtxrLTEModemEnbId OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 8 }

mtxrLTEModemSectorId OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 9 }

mtxrLTEModemLac OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 10 }

mtxrLTEModemIMEI OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 11 }

mtxrLTEModemIMSI OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 12 }

mtxrLTEModemUICC OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 13 }

mtxrLTEModemRAT OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrLTEModemEntry 14 }

mtxrLTEModemGroup OBJECT-GROUP OBJECTS {
        mtxrLTEModemSignalRSSI,
        mtxrLTEModemSignalRSRQ,
        mtxrLTEModemSignalRSRP,
        mtxrLTEModemCellId,
        mtxrLTEModemAccessTechnology,
        mtxrLTEModemSignalSINR,
        mtxrLTEModemEnbId,
        mtxrLTEModemSectorId,
        mtxrLTEModemLac,
        mtxrLTEModemIMEI,
        mtxrLTEModemIMSI,
        mtxrLTEModemUICC,
        mtxrLTEModemRAT
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 19 }

-- Partition ************************************************************

mtxrPartitionTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrPartitionEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "system partitions"
    ::= { mtxrPartition 1 }

mtxrPartitionEntry OBJECT-TYPE
    SYNTAX MtxrPartitionEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrPartitionIndex }
    ::= { mtxrPartitionTable 1 }

MtxrPartitionEntry ::= SEQUENCE {
    mtxrPartitionIndex ObjectIndex,
    mtxrPartitionName DisplayString,
    mtxrPartitionSize Integer32,
    mtxrPartitionVersion DisplayString,
    mtxrPartitionActive BoolValue,
    mtxrPartitionRunning BoolValue
}

mtxrPartitionIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPartitionEntry 1 }

mtxrPartitionName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPartitionEntry 2 }

mtxrPartitionSize OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "MB"
    ::= { mtxrPartitionEntry 3 }

mtxrPartitionVersion OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPartitionEntry 4 }

mtxrPartitionActive OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPartitionEntry 5 }

mtxrPartitionRunning OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrPartitionEntry 6 }

mtxrPartitionGroup OBJECT-GROUP OBJECTS {
        mtxrPartitionName,
        mtxrPartitionSize,
        mtxrPartitionVersion,
        mtxrPartitionActive,
        mtxrPartitionRunning
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 20 }

-- OPTICAL *****************************************************************

mtxrOpticalTable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrOpticalTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "SFP and GPON information"
    ::= { mtxrOptical 1 }

mtxrOpticalTableEntry OBJECT-TYPE
    SYNTAX MtxrOpticalTableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX { mtxrOpticalIndex }
    ::= { mtxrOpticalTable 1 }

MtxrOpticalTableEntry ::= SEQUENCE {
	mtxrOpticalIndex ObjectIndex,
        mtxrOpticalName DisplayString,
        mtxrOpticalRxLoss BoolValue,
        mtxrOpticalTxFault BoolValue,
        mtxrOpticalWavelength GDiv100,
        mtxrOpticalTemperature Gauge32,
        mtxrOpticalSupplyVoltage GDiv1000,
        mtxrOpticalTxBiasCurrent Gauge32,
        mtxrOpticalTxPower IDiv1000,
        mtxrOpticalRxPower IDiv1000
}

mtxrOpticalGroup OBJECT-GROUP OBJECTS {
        mtxrOpticalName,
        mtxrOpticalRxLoss,
        mtxrOpticalTxFault,
        mtxrOpticalWavelength,
        mtxrOpticalTemperature,
        mtxrOpticalSupplyVoltage,
        mtxrOpticalTxBiasCurrent,
        mtxrOpticalTxPower,
        mtxrOpticalRxPower
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 6 }

mtxrOpticalIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 1 }

mtxrOpticalName OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 2 }

mtxrOpticalRxLoss OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 3 }

mtxrOpticalTxFault OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 4 }

mtxrOpticalWavelength OBJECT-TYPE
    SYNTAX GDiv100
    UNITS "nm"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 5 }

mtxrOpticalTemperature OBJECT-TYPE
    SYNTAX Gauge32
    UNITS "C"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 6 }

mtxrOpticalSupplyVoltage OBJECT-TYPE
    SYNTAX GDiv1000
    UNITS "V"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 7 }

mtxrOpticalTxBiasCurrent OBJECT-TYPE
    SYNTAX Gauge32
    UNITS "mA"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 8 }

mtxrOpticalTxPower OBJECT-TYPE
    SYNTAX IDiv1000
    UNITS "dBm"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 9 }

mtxrOpticalRxPower OBJECT-TYPE
    SYNTAX IDiv1000
    UNITS "dBm"
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrOpticalTableEntry 10 }

-- IPSec *****************************************************************

mtxrIkeSACount OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "IKE SA count"
    ::= { mtxrIPSec 1 }

mtxrIkeSATable OBJECT-TYPE
    SYNTAX SEQUENCE OF MtxrIkeSATableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION "IKE SA table"
    ::= { mtxrIPSec 2 }

mtxrIkeSATableEntry OBJECT-TYPE
    SYNTAX MtxrIkeSATableEntry
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    INDEX {
        mtxrIkeSAIndex
    }
    ::= { mtxrIkeSATable 1 }

MtxrIkeSATableEntry ::= SEQUENCE {
        mtxrIkeSAIndex ObjectIndex,
        mtxrIkeSAInitiatorCookie IsakmpCookie,
        mtxrIkeSAResponderCookie IsakmpCookie,
        mtxrIkeSAResponder BoolValue,
        mtxrIkeSANatt BoolValue,
        mtxrIkeSAVersion Gauge32,
        mtxrIkeSAState INTEGER,
        mtxrIkeSAUptime TimeTicks,
        mtxrIkeSASeen TimeTicks,
        mtxrIkeSAIdentity DisplayString,
        mtxrIkeSAPh2Count Gauge32,
        mtxrIkeSALocalAddressType InetAddressType,
        mtxrIkeSALocalAddress InetAddress,
        mtxrIkeSALocalPort InetPortNumber,
        mtxrIkeSAPeerAddressType InetAddressType,
        mtxrIkeSAPeerAddress InetAddress,
        mtxrIkeSAPeerPort InetPortNumber,
        mtxrIkeSADynamicAddressType InetAddressType,
        mtxrIkeSADynamicAddress InetAddress,
        mtxrIkeSATxBytes Counter64,
        mtxrIkeSARxBytes Counter64,
        mtxrIkeSATxPackets Counter64,
        mtxrIkeSARxPackets Counter64
}

mtxrIkeSAGroup OBJECT-GROUP OBJECTS {
        mtxrIkeSACount,
        mtxrIkeSAInitiatorCookie,
        mtxrIkeSAResponderCookie,
        mtxrIkeSAResponder,
        mtxrIkeSANatt,
        mtxrIkeSAVersion,
        mtxrIkeSAState,
        mtxrIkeSAUptime,
        mtxrIkeSASeen,
        mtxrIkeSAIdentity,
        mtxrIkeSAPh2Count,
        mtxrIkeSALocalAddressType,
        mtxrIkeSALocalAddress,
        mtxrIkeSALocalPort,
        mtxrIkeSAPeerAddressType,
        mtxrIkeSAPeerAddress,
        mtxrIkeSAPeerPort,
        mtxrIkeSADynamicAddressType,
        mtxrIkeSADynamicAddress,
        mtxrIkeSATxBytes,
        mtxrIkeSARxBytes,
        mtxrIkeSATxPackets,
        mtxrIkeSARxPackets
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 7 }

mtxrIkeSAIndex OBJECT-TYPE
    SYNTAX ObjectIndex
    MAX-ACCESS not-accessible
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 1 }

mtxrIkeSAInitiatorCookie OBJECT-TYPE
    SYNTAX IsakmpCookie
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "initiator SPI"
    ::= { mtxrIkeSATableEntry 2 }

mtxrIkeSAResponderCookie OBJECT-TYPE
    SYNTAX IsakmpCookie
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "responder SPI"
    ::= { mtxrIkeSATableEntry 3 }

mtxrIkeSAResponder OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "IKE side"
    ::= { mtxrIkeSATableEntry 4 }

mtxrIkeSANatt OBJECT-TYPE
    SYNTAX BoolValue
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "NAT is detected"
    ::= { mtxrIkeSATableEntry 5 }

mtxrIkeSAVersion OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "protocol version"
    ::= { mtxrIkeSATableEntry 6 }

mtxrIkeSAState OBJECT-TYPE
    SYNTAX INTEGER {
        exchange(1),
        established(2),
        expired(3),
        eap(4)
    }
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 7 }

mtxrIkeSAUptime OBJECT-TYPE
    SYNTAX TimeTicks
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 8 }

mtxrIkeSASeen OBJECT-TYPE
    SYNTAX TimeTicks
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "time elapsed since last valid IKE packet"
    ::= { mtxrIkeSATableEntry 9 }

mtxrIkeSAIdentity OBJECT-TYPE
    SYNTAX DisplayString
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "peer identity"
    ::= { mtxrIkeSATableEntry 10 }

mtxrIkeSAPh2Count OBJECT-TYPE
    SYNTAX Gauge32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "total ph2 SA pairs"
    ::= { mtxrIkeSATableEntry 11 }

mtxrIkeSALocalAddressType OBJECT-TYPE
    SYNTAX InetAddressType
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 12 }

mtxrIkeSALocalAddress OBJECT-TYPE
    SYNTAX InetAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 13 }

mtxrIkeSALocalPort OBJECT-TYPE
    SYNTAX InetPortNumber
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 14 }

mtxrIkeSAPeerAddressType OBJECT-TYPE
    SYNTAX InetAddressType
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 15 }

mtxrIkeSAPeerAddress OBJECT-TYPE
    SYNTAX InetAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 16 }

mtxrIkeSAPeerPort OBJECT-TYPE
    SYNTAX InetPortNumber
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 17 }

mtxrIkeSADynamicAddressType OBJECT-TYPE
    SYNTAX InetAddressType
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION ""
    ::= { mtxrIkeSATableEntry 18 }

mtxrIkeSADynamicAddress OBJECT-TYPE
    SYNTAX InetAddress
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "dynamic address allocated by mode config"
    ::= { mtxrIkeSATableEntry 19 }

mtxrIkeSATxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "ph2 SA tx bytes"
    ::= { mtxrIkeSATableEntry 20 }

mtxrIkeSARxBytes OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "ph2 SA rx bytes"
    ::= { mtxrIkeSATableEntry 21 }

mtxrIkeSATxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "ph2 SA tx packets"
    ::= { mtxrIkeSATableEntry 22 }

mtxrIkeSARxPackets OBJECT-TYPE
    SYNTAX Counter64
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "ph2 SA rx packets"
    ::= { mtxrIkeSATableEntry 23 }

-- TRAPS **********************************************************************

mtxrNotifications OBJECT IDENTIFIER ::= { mtxrTraps 0 }

mtxrTrap NOTIFICATION-TYPE
    STATUS  current
    DESCRIPTION "Mikrotik trap OID"
    ::= { mtxrNotifications 1 }

mtxrTemperatureException NOTIFICATION-TYPE
    STATUS current
    DESCRIPTION "Mikrotik CPU temperature exception trap"
    ::= { mtxrNotifications 2 }

mtxrTrapGroup NOTIFICATION-GROUP NOTIFICATIONS {
        mtxrTrap,
        mtxrTemperatureException
    }
    STATUS current
    DESCRIPTION ""
    ::= { mtXRouterOsGroups 14 }

-- ***************************************************************************

END



File: /oid_lib.oidlib
﻿<?xml version="1.0" encoding="UTF-8"?>
  <oidlist>
    <system>
      <version>
        2
      </version>
    </system>
    <list>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat tx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat tx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatTxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat rx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat rx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatRxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat strength
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat ssid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.5
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat ssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatSsid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat bssid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.6
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat bssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatBssid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat freq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat freq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          megahertz
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatFreq
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat band
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.8
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat band
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatBand
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat txccq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.9
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat txccq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatTxCCQ
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl stat: #[1.3.6.1.4.1.14988.1.1.1.1.1.1]|mtxr wl stat rxccq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.1.1.10
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl stat rxccq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWlStatRxCCQ
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab addr: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.1
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab addr
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabAddr
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab iface: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab iface
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabIface
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab strength: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx bytes: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.4
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr wl rtab tx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx bytes: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.5
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr wl rtab rx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx packets: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.6
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx packets: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.7
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab rx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx rate: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx rate: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab rx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab routeros version: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.10
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab routeros version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          RouterOS version
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRouterOSVersion
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab uptime: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.11
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab uptime
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          uptime
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabUptime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          TimeTicks
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab signal to noise: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.12
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab signal to noise
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Measured in dB, if value does not exist it is indicated with 0
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabSignalToNoise
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx strength ch0: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.13
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx strength ch0
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxStrengthCh0
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx strength ch0: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.14
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab rx strength ch0
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.14
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxStrengthCh0
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx strength ch1: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.15
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx strength ch1
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.15
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxStrengthCh1
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx strength ch1: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.16
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab rx strength ch1
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.16
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxStrengthCh1
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx strength ch2: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.17
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx strength ch2
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.17
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxStrengthCh2
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab rx strength ch2: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.18
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab rx strength ch2
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.18
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRxStrengthCh2
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab tx strength: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.19
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab tx strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.19
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabTxStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl rtab: #[1.3.6.1.4.1.14988.1.1.1.2.1.1]|mtxr wl rtab radio name: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.2.1.20
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab radio name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.2.1.20
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabRadioName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.2.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wireless|mtxr wl rtab entry count: #[1.3.6.1.4.1.14988.1.1.1.2.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.4.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl rtab entry count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Wireless registration table entry count
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlRtabEntryCount
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap tx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap tx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApTxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap rx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap rx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApRxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap ssid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap ssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApSsid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap bssid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.5
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap bssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApBssid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap client count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.6
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap client count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApClientCount
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap freq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap freq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          megahertz
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApFreq
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap band
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.8
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap band
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApBand
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap noise floor
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap noise floor
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApNoiseFloor
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap overall txccq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.10
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap overall txccq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApOverallTxCCQ
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl ap: #[1.3.6.1.4.1.14988.1.1.1.3.1.1]|mtxr wl ap auth client count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.3.1.11
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl ap auth client count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.3.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrWlApAuthClientCount
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.3.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab addr: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.1
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab addr
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabAddr
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab iface: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab iface
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabIface
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab uptime: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab uptime
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          uptime
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabUptime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          TimeTicks
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab tx bytes: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.4
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr wlcmrtab tx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabTxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab rx bytes: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.5
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr wlcmrtab rx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabRxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab tx packets: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.6
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab tx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabTxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab rx packets: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.7
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab rx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabRxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab tx rate: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab tx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabTxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab rx rate: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab rx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabRxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab tx strength: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.10
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab tx strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabTxStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab rx strength: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.11
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab rx strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabRxStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab ssid: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.12
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab ssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabSsid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmrtab: #[1.3.6.1.4.1.14988.1.1.1.5.1.1]|mtxr wlcmrtab eap ident: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.5.1.13
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab eap ident
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.5.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabEapIdent
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.5.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wireless|mtxr wlcmrtab entry count: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.6.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrtab entry count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Wireless CAPSMAN registration table entry count
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRtabEntryCount
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wireless|mtxr wlcmrentry count: #[1.3.6.1.4.1.14988.1.1.1.5.1.2]
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.10.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmrentry count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Wireless CAPSMAN remote-cap entry count
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMREntryCount
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcm: #[1.3.6.1.4.1.14988.1.1.1.7.1.1]|mtxr wlcmindex
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.7.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmindex
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.7.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.7.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcm: #[1.3.6.1.4.1.14988.1.1.1.7.1.1]|mtxr wlcmreg client count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.7.1.2
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmreg client count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.7.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRegClientCount
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.7.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcm: #[1.3.6.1.4.1.14988.1.1.1.7.1.1]|mtxr wlcmauth client count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.7.1.3
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmauth client count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.7.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMAuthClientCount
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.7.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcm: #[1.3.6.1.4.1.14988.1.1.1.7.1.1]|mtxr wlcmstate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.7.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmstate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.7.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMState
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.7.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcm: #[1.3.6.1.4.1.14988.1.1.1.7.1.1]|mtxr wlcmchannel
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.7.1.5
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmchannel
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          for master only
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.7.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMChannel
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.7.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmremote: #[1.3.6.1.4.1.14988.1.1.1.11.1.1]|mtxr wlcmremote index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.11.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmremote index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.11.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRemoteIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.11.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmremote: #[1.3.6.1.4.1.14988.1.1.1.11.1.1]|mtxr wlcmremote name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.11.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmremote name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.11.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRemoteName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.11.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmremote: #[1.3.6.1.4.1.14988.1.1.1.11.1.1]|mtxr wlcmremote state
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.11.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmremote state
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.11.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRemoteState
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.11.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmremote: #[1.3.6.1.4.1.14988.1.1.1.11.1.1]|mtxr wlcmremote address
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.11.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmremote address
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.11.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRemoteAddress
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.11.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wlcmremote: #[1.3.6.1.4.1.14988.1.1.1.11.1.1]|mtxr wlcmremote radios
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.11.1.5
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wlcmremote radios
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.11.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWlCMRemoteRadios
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.11.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gindex
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gindex
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gmode
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrwl60g.mtxrwl60gmode
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gmode
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GMode
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gssid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gssid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GSsid
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gconnected
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrwl60g.mtxrwl60gconnected
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gconnected
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GConnected
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gremote
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.5
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gremote
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GRemote
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gfreq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gfreq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Mhz
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GFreq
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gmcs
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gmcs
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GMcs
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gsignal
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsignal
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GSignal
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gtx sector
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gtx sector
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GTxSector
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gtx sector info
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.11
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gtx sector info
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GTxSectorInfo
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60grssi
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.12
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60grssi
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GRssi
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60g: #[1.3.6.1.4.1.14988.1.1.1.8.1.1]|mtxr wl60gphy rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.8.1.13
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gphy rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.8.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GPhyRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.8.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta connected
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrwl60gsta.mtxrwl60gstaconnected
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta connected
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaConnected
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta remote
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta remote
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaRemote
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta mcs
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta mcs
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaMcs
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta signal
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta signal
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaSignal
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta tx sector
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta tx sector
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaTxSector
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta phy rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta phy rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Mbits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaPhyRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta rssi
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta rssi
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaRssi
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wl60gsta: #[1.3.6.1.4.1.14988.1.1.1.9.1.1]|mtxr wl60gsta distance
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.1.9.1.10
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wl60gsta distance
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          meters
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.1.9.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrWl60GStaDistance
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.1.9.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple iface
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple iface
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          interface index
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleIface
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple bytes in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.8
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr queue simple in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleBytesIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple bytes out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.9
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr queue simple out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleBytesOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple packets in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.10
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple packets in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimplePacketsIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple packets out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.11
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple packets out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimplePacketsOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simplepcqqueues in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.12
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simplepcqqueues in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimplePCQQueuesIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simplepcqqueues out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.13
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simplepcqqueues out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimplePCQQueuesOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple dropped in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.14
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple dropped in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.14
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleDroppedIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue simple: #[1.3.6.1.4.1.14988.1.1.2.1.1.1]|mtxr queue simple dropped out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.1.1.15
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue simple dropped out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.1.1.15
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueSimpleDroppedOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree flow
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree flow
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          flowmark
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeFlow
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree parent index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree parent index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          index of parent tree queue or parent interface
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeParentIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.5
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr queue tree
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.6
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreePackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue treehcbytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.7
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr queue treehc
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeHCBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue treepcqqueues
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.8
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue treepcqqueues
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreePCQQueues
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr queue tree: #[1.3.6.1.4.1.14988.1.1.2.2.1.1]|mtxr queue tree dropped
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.2.2.1.9
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr queue tree dropped
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.2.2.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrQueueTreeDropped
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.2.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl core voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl core voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          core voltage
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.1
        </OriginalOID>
        <OriginalLabel>
          mtxrHlCoreVoltage
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl three dot three voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.2.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl three dot three voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          3.3V voltage
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.2
        </OriginalOID>
        <OriginalLabel>
          mtxrHlThreeDotThreeVoltage
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl five voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.3.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl five voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          5V voltage
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.3
        </OriginalOID>
        <OriginalLabel>
          mtxrHlFiveVoltage
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl twelve voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.4.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl twelve voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          12V voltage
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.4
        </OriginalOID>
        <OriginalLabel>
          mtxrHlTwelveVoltage
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl sensor temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.5.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl sensor temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          temperature at sensor chip
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.5
        </OriginalOID>
        <OriginalLabel>
          mtxrHlSensorTemperature
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Temperature
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl cpu temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.6.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl cpu temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          temperature near cpu
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.6
        </OriginalOID>
        <OriginalLabel>
          mtxrHlCpuTemperature
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Temperature
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl board temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.7.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl board temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.7
        </OriginalOID>
        <OriginalLabel>
          mtxrHlBoardTemperature
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Temperature
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.8.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.8
        </OriginalOID>
        <OriginalLabel>
          mtxrHlVoltage
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl active fan
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.9.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl active fan
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.9
        </OriginalOID>
        <OriginalLabel>
          mtxrHlActiveFan
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.10.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.10
        </OriginalOID>
        <OriginalLabel>
          mtxrHlTemperature
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Temperature
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl processor temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.11.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl processor temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.11
        </OriginalOID>
        <OriginalLabel>
          mtxrHlProcessorTemperature
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Temperature
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl power
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.12.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl power
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Watts
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.12
        </OriginalOID>
        <OriginalLabel>
          mtxrHlPower
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Power
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl current
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.13.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl current
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          mA
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.13
        </OriginalOID>
        <OriginalLabel>
          mtxrHlCurrent
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl processor frequency
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.14.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl processor frequency
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Mhz
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.14
        </OriginalOID>
        <OriginalLabel>
          mtxrHlProcessorFrequency
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl power supply state
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrhealth.mtxrhlpowersupplystate
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.15.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl power supply state
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          PSU state ok
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.15
        </OriginalOID>
        <OriginalLabel>
          mtxrHlPowerSupplyState
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl backup power supply state
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrhealth.mtxrhlbackuppowersupplystate
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.16.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl backup power supply state
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          backup PSU state ok
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.16
        </OriginalOID>
        <OriginalLabel>
          mtxrHlBackupPowerSupplyState
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl fan speed1
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.17.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl fan speed1
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          rpm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.17
        </OriginalOID>
        <OriginalLabel>
          mtxrHlFanSpeed1
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr health|mtxr hl fan speed2
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.18.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hl fan speed2
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          rpm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.18
        </OriginalOID>
        <OriginalLabel>
          mtxrHlFanSpeed2
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gauge: #[1.3.6.1.4.1.14988.1.1.3.100.1.1]|mtxr gauge index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.100.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr gauge index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.100.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrGaugeIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.3.100.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gauge: #[1.3.6.1.4.1.14988.1.1.3.100.1.1]|mtxr gauge name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.100.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr gauge name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.100.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrGaugeName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.3.100.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gauge: #[1.3.6.1.4.1.14988.1.1.3.100.1.1]|mtxr gauge value
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.100.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr gauge value
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.100.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrGaugeValue
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.3.100.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gauge: #[1.3.6.1.4.1.14988.1.1.3.100.1.1]|mtxr gauge unit
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrgauge.mtxrgaugeunit
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.3.100.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr gauge unit
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          units
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.3.100.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrGaugeUnit
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.3.100.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr license|mtxr lic software id
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.4.1.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr lic software id
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          software id
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.4.1
        </OriginalOID>
        <OriginalLabel>
          mtxrLicSoftwareId
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr license|mtxr lic upgr until
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.4.2.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr lic upgr until
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          current key allows upgrading until this date
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.4.2
        </OriginalOID>
        <OriginalLabel>
          mtxrLicUpgrUntil
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          2d-1d-1d,1d:1d:1d.1d,1a1d:1d
        </DisplayHint>
        <DataType>
          DateAndTime
        </DataType>
        <DataSize>
          8
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr license|mtxr lic level
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.4.3.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr lic level
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          current key level
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.4.3
        </OriginalOID>
        <OriginalLabel>
          mtxrLicLevel
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr license|mtxr lic version
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.4.4.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr lic version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          software version
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.4.4
        </OriginalOID>
        <OriginalLabel>
          mtxrLicVersion
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr license|mtxr lic upgradable to
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.4.5.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr lic upgradable to
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          upgradable to
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.4.5
        </OriginalOID>
        <OriginalLabel>
          mtxrLicUpgradableTo
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user serverid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user serverid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserServerID
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user domain
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user domain
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserDomain
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active usermac
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.6
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active usermac
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserMAC
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user connect time
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user connect time
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserConnectTime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user valid till time
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user valid till time
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserValidTillTime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user idle start time
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user idle start time
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserIdleStartTime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user idle timeout
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.10
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user idle timeout
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserIdleTimeout
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user ping timeout
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.11
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user ping timeout
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserPingTimeout
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user bytes in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.12
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr hotspot active user in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserBytesIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user bytes out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.13
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr hotspot active user out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserBytesOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user packets in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.14
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user packets in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.14
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserPacketsIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user packets out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.15
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user packets out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.15
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserPacketsOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user limit bytes in
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.16
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr hotspot active user limit in
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.16
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserLimitBytesIn
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user limit bytes out
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.17
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr hotspot active user limit out
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.17
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserLimitBytesOut
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user advert status
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.18
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user advert status
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.18
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserAdvertStatus
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user radius
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.19
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user radius
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.19
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserRadius
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr hotspot active users: #[1.3.6.1.4.1.14988.1.1.5.1.1.1]|mtxr hotspot active user blocked by advert
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.5.1.1.20
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr hotspot active user blocked by advert
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.5.1.1.20
        </OriginalOID>
        <OriginalLabel>
          mtxrHotspotActiveUserBlockedByAdvert
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.5.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrdhcp|mtxrdhcplease count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.6.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrdhcplease count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.6.1
        </OriginalOID>
        <OriginalLabel>
          mtxrDHCPLeaseCount
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr system reboot
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr system reboot
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          set non zero to reboot
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.1
        </OriginalOID>
        <OriginalLabel>
          mtxrSystemReboot
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxrusbpower reset
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.2.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrusbpower reset
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          switches off usb power for specified amout of seconds
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.2
        </OriginalOID>
        <OriginalLabel>
          mtxrUSBPowerReset
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr serial number
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.3.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr serial number
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          RouterBOARD serial number
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.3
        </OriginalOID>
        <OriginalLabel>
          mtxrSerialNumber
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr firmware version
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.4.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr firmware version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Current firmware version
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.4
        </OriginalOID>
        <OriginalLabel>
          mtxrFirmwareVersion
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr note
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.5.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr note
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          note
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.5
        </OriginalOID>
        <OriginalLabel>
          mtxrNote
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr build time
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.6.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr build time
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          build time
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.6
        </OriginalOID>
        <OriginalLabel>
          mtxrBuildTime
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr firmware upgrade version
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.7.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr firmware upgrade version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          Upgrade firmware version
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.7
        </OriginalOID>
        <OriginalLabel>
          mtxrFirmwareUpgradeVersion
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr display name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.8.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr display name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          display name
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.8
        </OriginalOID>
        <OriginalLabel>
          mtxrDisplayName
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr system|mtxr board name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.7.9.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr board name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          board name
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.7.9
        </OriginalOID>
        <OriginalLabel>
          mtxrBoardName
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr script: #[1.3.6.1.4.1.14988.1.1.8.1.1.1]|mtxr script index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.8.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr script index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.8.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrScriptIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.8.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr script: #[1.3.6.1.4.1.14988.1.1.8.1.1.1]|mtxr script name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.8.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr script name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.8.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrScriptName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.8.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr script: #[1.3.6.1.4.1.14988.1.1.8.1.1.1]|mtxr script run cmd
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.8.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr script run cmd
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          set non zero to run
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.8.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrScriptRunCmd
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.8.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr script run: #[1.3.6.1.4.1.14988.1.1.18.1.1.1]|mtxr script run index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.18.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr script run index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.18.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrScriptRunIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.18.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr script run: #[1.3.6.1.4.1.14988.1.1.18.1.1.1]|mtxr script run output
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.18.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr script run output
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          this oid on get request will run script and return it&apos;s output
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.18.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrScriptRunOutput
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.18.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn stat index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn stat index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrDnStatIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn stat tx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn stat tx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrDnStatTxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn stat rx rate
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn stat rx rate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          bits per second
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrDnStatRxRate
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn stat tx strength
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn stat tx strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrDnStatTxStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn stat rx strength
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn stat rx strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrDnStatRxStrength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr dn stat: #[1.3.6.1.4.1.14988.1.1.10.1.1.1]|mtxr dn connected
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.10.1.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr dn connected
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          0 - not connected, connected otherwise
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.10.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrDnConnected
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.10.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor mac address
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor mac address
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborMacAddress
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          1x:
        </DisplayHint>
        <DataType>
          MacAddress
        </DataType>
        <DataSize>
          6
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor version
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborVersion
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor platform
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.5
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor platform
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborPlatform
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor identity
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.6
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor identity
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborIdentity
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor softwareid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.7
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor softwareid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborSoftwareID
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr neighbor: #[1.3.6.1.4.1.14988.1.1.11.1.1.1]|mtxr neighbor interfaceid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.11.1.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr neighbor interfaceid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.11.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrNeighborInterfaceID
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.11.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr date
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr date
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          UNIX time
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.1
        </OriginalOID>
        <OriginalLabel>
          mtxrDate
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr longtitude
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.2.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr longtitude
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          longtitude
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.2
        </OriginalOID>
        <OriginalLabel>
          mtxrLongtitude
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr latitude
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.3.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr latitude
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          latitude
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.3
        </OriginalOID>
        <OriginalLabel>
          mtxrLatitude
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr altitude
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.4.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr altitude
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          altitude
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.4
        </OriginalOID>
        <OriginalLabel>
          mtxrAltitude
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr speed
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.5.0
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr speed
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          speed
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.5
        </OriginalOID>
        <OriginalLabel>
          mtxrSpeed
        </OriginalLabel>
        <TableOID/>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr sattelites
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.6.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr sattelites
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          visible sattelite count
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.6
        </OriginalOID>
        <OriginalLabel>
          mtxrSattelites
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr gps|mtxr valid
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.12.7.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr valid
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          is the data valid
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.12.7
        </OriginalOID>
        <OriginalLabel>
          mtxrValid
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wireless modem|mtxr wireless modem signal strength
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.13.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wireless modem signal strength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          signal strength in dBm (if first ppp-client modem supports)
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.13.1
        </OriginalOID>
        <OriginalLabel>
          mtxrWirelessModemSignalStrength
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr wireless modem|mtxr wireless modem signal ec  io
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.13.2.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr wireless modem signal ec  io 
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          signal EC/IO in dB (if first ppp-client modem supports)
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.13.2
        </OriginalOID>
        <OriginalLabel>
          mtxrWirelessModemSignalECIO
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.2
          
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats driver rx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.11
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr interface stats driver rx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsDriverRxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats driver rx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.12
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats driver rx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsDriverRxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats driver tx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.13
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr interface stats driver tx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsDriverTxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats driver tx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.14
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats driver tx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.14
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsDriverTxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx64
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.15
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx64
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.15
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx64
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx65to127
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.16
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx65to127
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.16
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx65To127
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx128to255
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.17
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx128to255
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.17
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx128To255
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx256to511
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.18
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx256to511
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.18
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx256To511
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx512to1023
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.19
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx512to1023
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.19
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx512To1023
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx1024to1518
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.20
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx1024to1518
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.20
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx1024To1518
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx rx1519to max
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.21
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx rx1519to max
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.21
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxRx1519ToMax
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.31
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr interface stats rx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.31
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.32
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.32
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx too short
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.33
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx too short
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.33
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxTooShort
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx64
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.34
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx64
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.34
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx64
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx65to127
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.35
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx65to127
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.35
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx65To127
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx128to255
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.36
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx128to255
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.36
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx128To255
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx256to511
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.37
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx256to511
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.37
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx256To511
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx512to1023
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.38
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx512to1023
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.38
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx512To1023
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx1024to1518
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.39
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx1024to1518
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.39
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx1024To1518
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx1519to max
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.40
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx1519to max
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.40
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRx1519ToMax
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx too long
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.41
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx too long
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.41
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxTooLong
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx broadcast
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.42
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx broadcast
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.42
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxBroadcast
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx pause
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.43
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx pause
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.43
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxPause
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx multicast
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.44
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx multicast
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.44
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxMulticast
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rxfcserror
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.45
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rxfcserror
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.45
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxFCSError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx align error
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.46
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx align error
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.46
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxAlignError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx fragment
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.47
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx fragment
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.47
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxFragment
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx overflow
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.48
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx overflow
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.48
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxOverflow
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx control
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.49
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx control
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.49
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxControl
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx unknown op
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.50
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx unknown op
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.50
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxUnknownOp
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx length error
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.51
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          length
        </units>
        <indicator>
          mtxr interface stats rx error
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.51
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxLengthError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx code error
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.52
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx code error
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.52
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxCodeError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx carrier error
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.53
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx carrier error
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.53
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxCarrierError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx jabber
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.54
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx jabber
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.54
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxJabber
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats rx drop
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.55
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats rx drop
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.55
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsRxDrop
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.61
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr interface stats tx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.61
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.62
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.62
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx too short
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.63
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx too short
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.63
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxTooShort
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx64
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.64
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx64
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.64
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx64
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx65to127
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.65
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx65to127
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.65
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx65To127
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx128to255
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.66
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx128to255
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.66
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx128To255
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx256to511
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.67
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx256to511
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.67
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx256To511
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx512to1023
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.68
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx512to1023
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.68
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx512To1023
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx1024to1518
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.69
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx1024to1518
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.69
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx1024To1518
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx1519to max
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.70
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx1519to max
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.70
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTx1519ToMax
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx too long
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.71
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx too long
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.71
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxTooLong
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx broadcast
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.72
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx broadcast
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.72
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxBroadcast
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx pause
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.73
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx pause
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.73
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxPause
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx multicast
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.74
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx multicast
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.74
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxMulticast
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx underrun
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.75
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx underrun
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.75
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxUnderrun
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.76
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.76
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx excessive collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.77
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx excessive collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.77
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxExcessiveCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx multiple collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.78
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx multiple collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.78
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxMultipleCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx single collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.79
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx single collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.79
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxSingleCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx excessive deferred
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.80
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx excessive deferred
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.80
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxExcessiveDeferred
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx deferred
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.81
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx deferred
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.81
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxDeferred
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx late collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.82
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx late collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.82
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxLateCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx total collision
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.83
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx total collision
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.83
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxTotalCollision
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx pause honored
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.84
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx pause honored
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.84
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxPauseHonored
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx drop
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.85
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx drop
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.85
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxDrop
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx jabber
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.86
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx jabber
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.86
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxJabber
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats txfcserror
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.87
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats txfcserror
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.87
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxFCSError
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx control
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.88
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx control
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.88
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxControl
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats tx fragment
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.89
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats tx fragment
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.89
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsTxFragment
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr interface stats: #[1.3.6.1.4.1.14988.1.1.14.1.1.1]|mtxr interface stats link downs
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.14.1.1.90
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr interface stats link downs
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.14.1.1.90
        </OriginalOID>
        <OriginalLabel>
          mtxrInterfaceStatsLinkDowns
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.14.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoeinterface index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoeinterface index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrPOEInterfaceIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoename
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoename
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrPOEName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoestatus
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrpoe.mtxrpoestatus
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoestatus
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrPOEStatus
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoevoltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoevoltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          V
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrPOEVoltage
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Voltage
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoecurrent
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoecurrent
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          mA
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrPOECurrent
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrpoe: #[1.3.6.1.4.1.14988.1.1.15.1.1.1]|mtxrpoepower
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.15.1.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrpoepower
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          W
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.15.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrPOEPower
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.15.1.1
        </TableOID>
        <DisplayHint>
          d-1
        </DisplayHint>
        <DataType>
          Power
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem interface index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem interface index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemInterfaceIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem signalrssi
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.2
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem signalrssi
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemSignalRSSI
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem signalrsrq
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem signalrsrq
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dB
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemSignalRSRQ
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem signalrsrp
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem signalrsrp
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dBm
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemSignalRSRP
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem cell id
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem cell id
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          current cell ID
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemCellId
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          HexInt
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem access technology
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrltemodem.mtxrltemodemaccesstechnology
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem access technology
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          as reported by +CREG
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemAccessTechnology
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem signalsinr
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem signalsinr
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dB
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemSignalSINR
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem enb id
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem enb id
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemEnbId
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem sector id
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem sector id
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemSectorId
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodem lac
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.10
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodem lac
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemLac
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodemimei
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.11
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodemimei
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemIMEI
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodemimsi
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.12
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodemimsi
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemIMSI
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodemuicc
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.13
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodemuicc
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemUICC
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxrltemodem: #[1.3.6.1.4.1.14988.1.1.16.1.1.1]|mtxrltemodemrat
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.16.1.1.14
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxrltemodemrat
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.16.1.1.14
        </OriginalOID>
        <OriginalLabel>
          mtxrLTEModemRAT
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.16.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition size
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition size
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          MB
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionSize
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition version
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.4
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition version
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionVersion
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition active
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrpartition.mtxrpartitionactive
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition active
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionActive
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr partition: #[1.3.6.1.4.1.14988.1.1.17.1.1.1]|mtxr partition running
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrpartition.mtxrpartitionrunning
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.17.1.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr partition running
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.17.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrPartitionRunning
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.17.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical index
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr optical index
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical name
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr optical name
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalName
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical rx loss
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxroptical.mtxropticalrxloss
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.3
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr optical rx loss
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalRxLoss
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical tx fault
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxroptical.mtxropticaltxfault
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr optical tx fault
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalTxFault
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical wavelength
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          nm
        </units>
        <indicator>
          mtxr optical wavelength
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalWavelength
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          d-2
        </DisplayHint>
        <DataType>
          GDiv100
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical temperature
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          C
        </units>
        <indicator>
          mtxr optical temperature
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalTemperature
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical supply voltage
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          V
        </units>
        <indicator>
          mtxr optical supply voltage
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalSupplyVoltage
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          d-3
        </DisplayHint>
        <DataType>
          GDiv1000
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical tx bias current
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          mA
        </units>
        <indicator>
          mtxr optical tx bias current
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalTxBiasCurrent
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical tx power
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          dBm
        </units>
        <indicator>
          mtxr optical tx power
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalTxPower
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          d-3
        </DisplayHint>
        <DataType>
          IDiv1000
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr optical: #[1.3.6.1.4.1.14988.1.1.19.1.1.1]|mtxr optical rx power
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.19.1.1.10
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          dBm
        </units>
        <indicator>
          mtxr optical rx power
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.19.1.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrOpticalRxPower
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.19.1.1
        </TableOID>
        <DisplayHint>
          d-3
        </DisplayHint>
        <DataType>
          IDiv1000
        </DataType>
        <DataSize>
          -2147483648
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxripsec|mtxr ike sa count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.1.0
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkDirect
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ike sa count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          IKE SA count
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.1
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSACount
        </OriginalLabel>
        <TableOID/>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaindex
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.1
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaindex
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.1
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAIndex
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint>
          x
        </DisplayHint>
        <DataType>
          ObjectIndex
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesainitiator cookie
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.2
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesainitiator cookie
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          initiator SPI
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.2
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAInitiatorCookie
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint>
          16a
        </DisplayHint>
        <DataType>
          IsakmpCookie
        </DataType>
        <DataSize>
          16
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaresponder cookie
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.3
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaresponder cookie
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          responder SPI
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.3
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAResponderCookie
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint>
          16a
        </DisplayHint>
        <DataType>
          IsakmpCookie
        </DataType>
        <DataSize>
          16
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaresponder
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesaresponder
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.4
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaresponder
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          IKE side
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.4
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAResponder
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesanatt
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesanatt
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.5
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesanatt
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          NAT is detected
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.5
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSANatt
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          BoolValue
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaversion
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.6
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaversion
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          protocol version
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.6
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAVersion
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesastate
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesastate
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.7
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesastate
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.7
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAState
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_INTEGER
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesauptime
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.8
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesauptime
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.8
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAUptime
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          TimeTicks
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaseen
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.9
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaseen
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          time elapsed since last valid IKE packet
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.9
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSASeen
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          TimeTicks
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesaidentity
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.10
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesaidentity
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          peer identity
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.10
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAIdentity
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint>
          255a
        </DisplayHint>
        <DataType>
          ASN_OCTET_STR
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ike sa ph2count
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.11
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ike sa ph2count
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          total ph2 SA pairs
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.11
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAPh2Count
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_GAUGE
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesalocal address type
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesalocaladdresstype
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.12
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesalocal address type
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.12
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSALocalAddressType
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddressType
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesalocal address
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.13
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesalocal address
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.13
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSALocalAddress
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddress
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesapeer address type
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesapeeraddresstype
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.15
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesapeer address type
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.15
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAPeerAddressType
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddressType
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesapeer address
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.16
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesapeer address
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.16
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSAPeerAddress
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddress
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesadynamic address type
        </name>
        <lookupname>
          oid.mikrotik-mib.mtxrikesa.mtxrikesadynamicaddresstype
        </lookupname>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.18
        </oid>
        <type>
          vmAbsolute
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesadynamic address type
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description/>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.18
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSADynamicAddressType
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddressType
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ikesadynamic address
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.19
        </oid>
        <type>
          vmString
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ikesadynamic address
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          no
        </is64bit>
        <isunsigned>
          no
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          dynamic address allocated by mode config
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.19
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSADynamicAddress
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          InetAddress
        </DataType>
        <DataSize>
          255
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ike sa tx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.20
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr ike sa tx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          ph2 SA tx bytes
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.20
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSATxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ike sa rx bytes
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.21
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutBytes
        </unittype>
        <units>
          bytes
        </units>
        <indicator>
          mtxr ike sa rx
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          ph2 SA rx bytes
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.21
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSARxBytes
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ike sa tx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.22
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ike sa tx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          ph2 SA tx packets
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.22
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSATxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
      <entry>
        <name>
          MIKROTIK-MIB|mtxr ikesa: #[1.3.6.1.4.1.14988.1.1.20.2.1.1]|mtxr ike sa rx packets
        </name>
        <lookupname/>
        <oid>
          1.3.6.1.4.1.14988.1.1.20.2.1.23
        </oid>
        <type>
          vmDiff
        </type>
        <kind>
          mkTable
        </kind>
        <unittype>
          sutCustom
        </unittype>
        <units>
          #
        </units>
        <indicator>
          mtxr ike sa rx packets
        </indicator>
        <scale>
          1
        </scale>
        <multiply>
          no
        </multiply>
        <max>
          0
        </max>
        <usegetnext>
          no
        </usegetnext>
        <is64bit>
          yes
        </is64bit>
        <isunsigned>
          yes
        </isunsigned>
        <isfloat>
          no
        </isfloat>
        <description>
          ph2 SA rx packets
        </description>
        <OriginalOID>
          1.3.6.1.4.1.14988.1.1.20.2.1.23
        </OriginalOID>
        <OriginalLabel>
          mtxrIkeSARxPackets
        </OriginalLabel>
        <TableOID>
          1.3.6.1.4.1.14988.1.1.20.2.1
        </TableOID>
        <DisplayHint/>
        <DataType>
          ASN_COUNTER64
        </DataType>
        <DataSize>
          0
        </DataSize>
        <UnitSource/>
        <UnitNormalized/>
        <GroupMajor/>
        <GroupMinor/>
        <GroupSub/>
        <FormatType/>
        <FormatValue/>
      </entry>
    </list>
    <lookups>
      <oid.mikrotik-mib.mtxrgauge.mtxrgaugeunit>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          celsius
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          rpm
        </cell>
        <cell row="2" col="0">
          3
        </cell>
        <cell row="2" col="1">
          dV
        </cell>
        <cell row="3" col="0">
          4
        </cell>
        <cell row="3" col="1">
          dA
        </cell>
        <cell row="4" col="0">
          5
        </cell>
        <cell row="4" col="1">
          dW
        </cell>
        <cell row="5" col="0">
          6
        </cell>
        <cell row="5" col="1">
          status
        </cell>
      </oid.mikrotik-mib.mtxrgauge.mtxrgaugeunit>
      <oid.mikrotik-mib.mtxrhealth.mtxrhlbackuppowersupplystate>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrhealth.mtxrhlbackuppowersupplystate>
      <oid.mikrotik-mib.mtxrhealth.mtxrhlpowersupplystate>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrhealth.mtxrhlpowersupplystate>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesadynamicaddresstype>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          ipv4
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          ipv6
        </cell>
        <cell row="2" col="0">
          16
        </cell>
        <cell row="2" col="1">
          dns
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesadynamicaddresstype>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesalocaladdresstype>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          ipv4
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          ipv6
        </cell>
        <cell row="2" col="0">
          16
        </cell>
        <cell row="2" col="1">
          dns
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesalocaladdresstype>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesanatt>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesanatt>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesapeeraddresstype>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          ipv4
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          ipv6
        </cell>
        <cell row="2" col="0">
          16
        </cell>
        <cell row="2" col="1">
          dns
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesapeeraddresstype>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesaresponder>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesaresponder>
      <oid.mikrotik-mib.mtxrikesa.mtxrikesastate>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          exchange
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          established
        </cell>
        <cell row="2" col="0">
          3
        </cell>
        <cell row="2" col="1">
          expired
        </cell>
        <cell row="3" col="0">
          4
        </cell>
        <cell row="3" col="1">
          eap
        </cell>
      </oid.mikrotik-mib.mtxrikesa.mtxrikesastate>
      <oid.mikrotik-mib.mtxrltemodem.mtxrltemodemaccesstechnology>
        <cell row="0" col="0">
          -1
        </cell>
        <cell row="0" col="1">
          unknown
        </cell>
        <cell row="1" col="0">
          0
        </cell>
        <cell row="1" col="1">
          gsmcompact
        </cell>
        <cell row="2" col="0">
          1
        </cell>
        <cell row="2" col="1">
          gsm
        </cell>
        <cell row="3" col="0">
          2
        </cell>
        <cell row="3" col="1">
          utran
        </cell>
        <cell row="4" col="0">
          3
        </cell>
        <cell row="4" col="1">
          egprs
        </cell>
        <cell row="5" col="0">
          4
        </cell>
        <cell row="5" col="1">
          hsdpa
        </cell>
        <cell row="6" col="0">
          5
        </cell>
        <cell row="6" col="1">
          hsupa
        </cell>
        <cell row="7" col="0">
          6
        </cell>
        <cell row="7" col="1">
          hsdpahsupa
        </cell>
        <cell row="8" col="0">
          7
        </cell>
        <cell row="8" col="1">
          eutran
        </cell>
        <cell row="9" col="0">
          11
        </cell>
        <cell row="9" col="1">
          nr-sa
        </cell>
        <cell row="10" col="0">
          13
        </cell>
        <cell row="10" col="1">
          nr-nsa
        </cell>
      </oid.mikrotik-mib.mtxrltemodem.mtxrltemodemaccesstechnology>
      <oid.mikrotik-mib.mtxroptical.mtxropticalrxloss>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxroptical.mtxropticalrxloss>
      <oid.mikrotik-mib.mtxroptical.mtxropticaltxfault>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxroptical.mtxropticaltxfault>
      <oid.mikrotik-mib.mtxrpartition.mtxrpartitionactive>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrpartition.mtxrpartitionactive>
      <oid.mikrotik-mib.mtxrpartition.mtxrpartitionrunning>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrpartition.mtxrpartitionrunning>
      <oid.mikrotik-mib.mtxrpoe.mtxrpoestatus>
        <cell row="0" col="0">
          1
        </cell>
        <cell row="0" col="1">
          disabled
        </cell>
        <cell row="1" col="0">
          2
        </cell>
        <cell row="1" col="1">
          waitingForLoad
        </cell>
        <cell row="2" col="0">
          3
        </cell>
        <cell row="2" col="1">
          poweredOn
        </cell>
        <cell row="3" col="0">
          4
        </cell>
        <cell row="3" col="1">
          overload
        </cell>
      </oid.mikrotik-mib.mtxrpoe.mtxrpoestatus>
      <oid.mikrotik-mib.mtxrwl60g.mtxrwl60gconnected>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrwl60g.mtxrwl60gconnected>
      <oid.mikrotik-mib.mtxrwl60g.mtxrwl60gmode>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          apBridge
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          stationBridge
        </cell>
        <cell row="2" col="0">
          2
        </cell>
        <cell row="2" col="1">
          sniff
        </cell>
        <cell row="3" col="0">
          3
        </cell>
        <cell row="3" col="1">
          bridge
        </cell>
      </oid.mikrotik-mib.mtxrwl60g.mtxrwl60gmode>
      <oid.mikrotik-mib.mtxrwl60gsta.mtxrwl60gstaconnected>
        <cell row="0" col="0">
          0
        </cell>
        <cell row="0" col="1">
          false
        </cell>
        <cell row="1" col="0">
          1
        </cell>
        <cell row="1" col="1">
          true
        </cell>
      </oid.mikrotik-mib.mtxrwl60gsta.mtxrwl60gstaconnected>
    </lookups>
  </oidlist>


File: /README.md
# MIBS SNMP MIKROTIK

## HEALTH

```JS
core voltage=1.3.6.1.4.1.14988.1.1.3.1.0
3.3V voltage=1.3.6.1.4.1.14988.1.1.3.2.0
5V voltage=1.3.6.1.4.1.14988.1.1.3.3.0
12V voltage=1.3.6.1.4.1.14988.1.1.3.4.0
temperature at sensor chip=1.3.6.1.4.1.14988.1.1.3.5.0
temperaturenear cpu=1.3.6.1.4.1.14988.1.1.3.6.0
board temperature=1.3.6.1.4.1.14988.1.1.3.7.0
voltage=1.3.6.1.4.1.14988.1.1.3.8.0
active fan=1.3.6.1.4.1.14988.1.1.3.9.0
temperature=1.3.6.1.4.1.14988.1.1.3.10.0
processor temperature=1.3.6.1.4.1.14988.1.1.3.11.0
power=1.3.6.1.4.1.14988.1.1.3.12.0
current=1.3.6.1.4.1.14988.1.1.3.13.0
processor frequency=1.3.6.1.4.1.14988.1.1.3.14.0
power supply state=1.3.6.1.4.1.14988.1.1.3.15.0
backup power supply state=1.3.6.1.4.1.14988.1.1.3.16.0
fan speed1=1.3.6.1.4.1.14988.1.1.3.17.0
fan speed2=1.3.6.1.4.1.14988.1.1.3.18.0
```

## INTERFACE

```JS
mtxr interface stats index=1.3.6.1.4.1.14988.1.1.14.1.1.1
mtxr interface stats type=1.3.6.1.2.1.2.2.1.3
mtxr interface stats name=1.3.6.1.4.1.14988.1.1.14.1.1.2
mtxr interface stats alias=1.3.6.1.2.1.31.1.1.1.18
mtxr interface stats rx bytes=1.3.6.1.4.1.14988.1.1.14.1.1.31
mtxr interface stats tx bytes=1.3.6.1.4.1.14988.1.1.14.1.1.61
mtxr interface stats link downs=1.3.6.1.4.1.14988.1.1.14.1.1.90


```

## OPTICAL

```JS
mtxr optical index=1.3.6.1.4.1.14988.1.1.19.1.1.1
mtxr optical name=1.3.6.1.4.1.14988.1.1.19.1.1.2
mtxr optical rx loss=1.3.6.1.4.1.14988.1.1.19.1.1.3
mtxr optical tx fault=1.3.6.1.4.1.14988.1.1.19.1.1.4
mtxr optical wavelength=1.3.6.1.4.1.14988.1.1.19.1.1.5
mtxr optical temperature=1.3.6.1.4.1.14988.1.1.19.1.1.6
mtxr optical supply voltage=1.3.6.1.4.1.14988.1.1.19.1.1.7
mtxr optical tx bias current=1.3.6.1.4.1.14988.1.1.19.1.1.8
mtxr optical tx power=1.3.6.1.4.1.14988.1.1.19.1.1.9
mtxr optical rx power=1.3.6.1.4.1.14988.1.1.19.1.1.10
```

## SCRIPT

```JS
mtxr script index=1.3.6.1.4.1.14988.1.1.8.1.1.1
mtxr script name=1.3.6.1.4.1.14988.1.1.8.1.1.2
mtxr script run cmd=1.3.6.1.4.1.14988.1.1.8.1.1.3
mtxr script run index=1.3.6.1.4.1.14988.1.1.18.1.1.1
mtxr script run output=1.3.6.1.4.1.14988.1.1.18.1.1.2
```

## GAUGE

```JS
mtxr gauge index=1.3.6.1.4.1.14988.1.1.3.100.1.1
mtxr gauge name=1.3.6.1.4.1.14988.1.1.3.100.1.2
mtxr gauge value=1.3.6.1.4.1.14988.1.1.3.100.1.3
mtxr gauge unit=1.3.6.1.4.1.14988.1.1.3.100.1.4
```

## NEIGHBOR

```JS
mtxr neighbor index=1.3.6.1.4.1.14988.1.1.11.1.1.1
mtxr neighbor ip address=1.3.6.1.4.1.14988.1.1.11.1.1.8
mtxr neighbor mac address=1.3.6.1.4.1.14988.1.1.11.1.1.3
mtxr neighbor version=1.3.6.1.4.1.14988.1.1.11.1.1.4
mtxr neighbor platform=1.3.6.1.4.1.14988.1.1.11.1.1.5
mtxr neighbor identity=1.3.6.1.4.1.14988.1.1.11.1.1.6
mtxr neighbor softwareid=1.3.6.1.4.1.14988.1.1.11.1.1.7
mtxr neighbor interfaceid=1.3.6.1.4.1.14988.1.1.11.1.1.8
```


