# Repository Information
Name: Mikrotik-RouterOS-API-VFP-9.0

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-RouterOS-API-VFP-9.0/
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
    │   │       ├── pack-b9a48a55e0a60c884d0b6b40f806e29c6ad6f8ae.idx
    │   │       └── pack-b9a48a55e0a60c884d0b6b40f806e29c6ad6f8ae.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── base2base.prg
    ├── hex2ascii.prg
    ├── LICENSE.md
    ├── md5.VCT
    ├── md5.vcx
    ├── MikrotikAPI.PJT
    ├── MikrotikAPI.pjx
    ├── mikrotik_sync.VCT
    ├── mikrotik_sync.vcx
    ├── README.md
    ├── test.prg
    └── winsocket.prg


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
	url = https://github.com/bobr-kun/Mikrotik-RouterOS-API-VFP-9.0.git
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
0000000000000000000000000000000000000000 b59c8e77dfc7caee24309373ee9bdac1a253681a vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/bobr-kun/Mikrotik-RouterOS-API-VFP-9.0.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b59c8e77dfc7caee24309373ee9bdac1a253681a vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/bobr-kun/Mikrotik-RouterOS-API-VFP-9.0.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b59c8e77dfc7caee24309373ee9bdac1a253681a vivek-dodia <vivek.dodia@icloud.com> 1738606086 -0500	clone: from https://github.com/bobr-kun/Mikrotik-RouterOS-API-VFP-9.0.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b59c8e77dfc7caee24309373ee9bdac1a253681a refs/remotes/origin/master


File: /.git\refs\heads\master
b59c8e77dfc7caee24309373ee9bdac1a253681a


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /base2base.prg
FUNCTION Base2Base  
 *  Base2Base( <cInString>, <nInBase>, <nOutBase> ) --> cNewBaseValue  
 *	Converts number in string representation from one notation 
 *  to another in notations range from 2 to 201

  lPARAMETERS cInString, nInBase, nOutBase  
  T_CHAR		= "C"  
  T_NUM			= "N"  
  T_LOGIC		= "L"  
  T_DATE		= "D"  
  T_TIME		= "T"  
  T_MONEY		= "Y"  
  T_NULL		= "X"  
  T_OBJ			= "O"  
  T_UNKNOWN		= "U"  
  T_GENERAL		= "G"  

 *  Note, that to convert from HEX notation you need to use ONLY upper case letters ABCDEF
  
  LDS_B2B_DIG 	= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
  
  LOCAL cNewBaseValue, ln_i, ln_len, DecPos, IntValue, FracValue  
  LOCAL FracProduct, FracCounter, IntProdStr, FracOutStr, IntOutString  
  LOCAL IntStr, FracString, FracLimit, Remainder, Quotient, NegSign 
  LOCAL digits_num, tRemainder
   
  cNewBaseValue = ""  
  FracValue = 0.00000000000000000000  
  IntValue = 0  
  
 *  Parameters check    
  IF VARTYPE(cInString) == T_NUM
  	tRemainder = cInString
  	digits_num = 0
  	
  	DO WHILE tRemainder > 0
  		tRemainder = INT(tRemainder / 10)
  		digits_num = digits_num + 1 
  	ENDDO 	
  	
  	cInString = TRANSFORM(STR(cInString, digits_num), '@T')
  ENDIF 
   
  IF VARTYPE(cInString) == T_CHAR AND ALLTRIM(cInString) == ''
  	RETURN ''  		  		
  ENDIF 
  	
  IF VARTYPE(cInString) != T_CHAR
  	cInString = TRANSFORM(cInString)
  	cInString = ALLTRIM(cInString)
  ENDIF 
  
  IF cInString == '0' 
  	RETURN '0'
  ENDIF   
  
  IF EMPTY(cInString) OR LEN(cInString ) > 20  
  	cNewBaseValue = .F.  
  ELSE  
  	STORE ALLTRIM(cInString) TO cInString  
  	IF EMPTY(nInBase)  
  		STORE 10 TO nInBase  
  	ENDIF  
  	IF EMPTY(nOutBase)  
  		STORE 10 TO nOutBase	  
  	endif  
  	IF varTYPE(nInBase) != T_NUM .OR. varTYPE(nOutBase) != T_NUM  
  		cNewBaseValue=.F.  
  	ELSE  
		*  Out of notation range check  		
  		IF nInBase > 62 .OR. nOutBase > 62 .OR. nInBase < 2 .OR. nOutBase < 2  
  			cNewBaseValue = .F.  
  		ELSE  
			*  Check for the correspondence of each digit of the original number to the notation
  			ln_i = 1  
  			STORE LEN(cInString) TO ln_len  
  			DO WHILE ln_i < ln_len .AND. varTYPE(cNewBaseValue) != T_LOGIC  
  				ln_i = ln_i + 1  
  				IF .NOT. UPPER(SUBSTR(cInString , ln_i , 1)) $ UPPER((SUBSTR(LDS_B2B_DIG, 1, nInBase) + "."))
  					cNewBaseValue = .F.  
  				ENDIF  
  			ENDDO  
  		ENDIF  
  	ENDIF  
  ENDIF  
  
  IF VARTYPE(cNewBaseValue) != T_LOGIC    
	*  Check if the converted number is negative
  	NegSign = IIF(Left(cInString, 1) == "-", "-", "")  
  	IF .NOT. EMPTY(NegSign)  
  		cInString = SUBSTR(ALLTRIM(SUBSTR(cInString, 2)), 2)  
  	ENDIF  

	*  Decimal point defifnition
  	DecPos = AT(".", cInString)  
  	IntStr = IIF(DecPos>1, SUBSTR(cInString, 1, DecPos - 1 ), IIF(DecPos = 1, "0", cInString))  
  	FracString = IIF(DecPos>0, SUBSTR(cInString, DecPos + 1 ), "0")  

	*  Conversion of the int part of the string to digital in decimal notation
  	STORE LEN(IntStr) TO ln_len  
  	FOR ln_i = ln_len TO 1 STEP  - 1  
  		IntValue = IntValue + (AT(SUBSTR(IntStr, ln_i, 1), LDS_B2B_DIG) - 1) * (nInBase ** (ln_len - ln_i))  
  	NEXT  

	*  Conversion of the fractional part of the string to digital in decimal notation  	
      STORE LEN(FracString) TO ln_len  
  	FOR ln_i = 1 TO ln_len  
  		FracValue = FracValue + (AT(SUBSTR(FracString, ln_i, 1), LDS_B2B_DIG) - 1) * (nInBase ** ( - ln_i))  
    NEXT  

	*  Calculation of the int part of the input string
  	Quotient = IntValue  
  	IntOutString = ""  
  	DO WHILE Quotient != 0  
  		Remainder = Quotient % nOutBase  
  		Quotient = INT(Quotient / nOutBase)  
  		IntOutString = SUBSTR(LDS_B2B_DIG, Remainder + 1, 1) + IntOutString  
  	ENDDO  
  	
  	IF EMPTY(IntOutstring)  
  		STORE "0" TO IntOutString  
  	endif  
  	
	*  Calculation of the fractional part of the input string
  	FracLimit = 20 - DecPos  
  	FracProduct = FracValue  
  	FracCounter = 1  
  	FracOutStr = ""  
  	DO WHILE FracCounter < FracLimit .AND. FracProduct < 0.00000000000001  
  		FracCounter = FracCounter + 1  
        	IntProdStr = FracProduct * nOutBase  
  		FracOutStr = FracOutStr + SUBSTR(LDS_B2B_DIG, INT(IntProdStr) + 1, 1)  
  		FracProduct = IntProdStr - INT(IntProdStr)  
  	ENDDO  
  ENDIF  
  
  *  Formation of the returning string
  IF varTYPE (cNewBaseValue) != T_LOGIC	
  	cNewBaseValue = IIF(DecPos > 0, NegSign + IntOutString + "." + FracOutStr, IntOutString)  
  ENDIF  
RETURN cNewBaseValue

File: /hex2ascii.prg
FUNCTION hex2ascii
PARAMETERS in_val
LOCAL uncrypt_str, extracted_chars, i
PRIVATE uncrypt_str, extracted_chars, i

	STORE '' TO uncrypt_str, extracted_chars
	
	IF EMPTY(in_val)
		RETURN uncrypt_str
	ENDIF 
	
	IF VARTYPE(in_val) != 'C' 
		in_val = TRANSFORM(in_val)	
	ENDIF 

	FOR i = 1 TO LEN(in_val) STEP 2
		extracted_chars = SUBSTR(in_val, i, 2)

		IF extracted_chars != '' 
			uncrypt_str = uncrypt_str + CHR(VAL(base2base(extracted_chars, 16, 10)))
		ENDIF 

	ENDFOR 

RETURN uncrypt_str 

File: /LICENSE.md

                  GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

(This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.)

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
Licenses are intended to guarantee your freedom to share and change
free software--to make sure the software is free for all its users.

  This license, the Lesser General Public License, applies to some
specially designated software packages--typically libraries--of the
Free Software Foundation and other authors who decide to use it.  You
can use it too, but we suggest you first think carefully about whether
this license or the ordinary General Public License is the better
strategy to use in any particular case, based on the explanations below.

  When we speak of free software, we are referring to freedom of use,
not price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and charge
for this service if you wish); that you receive source code or can get
it if you want it; that you can change the software and use pieces of
it in new free programs; and that you are informed that you can do
these things.

  To protect your rights, we need to make restrictions that forbid
distributors to deny you these rights or to ask you to surrender these
rights.  These restrictions translate to certain responsibilities for
you if you distribute copies of the library or if you modify it.

  For example, if you distribute copies of the library, whether gratis
or for a fee, you must give the recipients all the rights that we gave
you.  You must make sure that they, too, receive or can get the source
code.  If you link other code with the library, you must provide
complete object files to the recipients, so that they can relink them
with the library after making changes to the library and recompiling
it.  And you must show them these terms so they know their rights.

  We protect your rights with a two-step method: (1) we copyright the
library, and (2) we offer you this license, which gives you legal
permission to copy, distribute and/or modify the library.

  To protect each distributor, we want to make it very clear that
there is no warranty for the free library.  Also, if the library is
modified by someone else and passed on, the recipients should know
that what they have is not the original version, so that the original
author's reputation will not be affected by problems that might be
introduced by others.

  Finally, software patents pose a constant threat to the existence of
any free program.  We wish to make sure that a company cannot
effectively restrict the users of a free program by obtaining a
restrictive license from a patent holder.  Therefore, we insist that
any patent license obtained for a version of the library must be
consistent with the full freedom of use specified in this license.

  Most GNU software, including some libraries, is covered by the
ordinary GNU General Public License.  This license, the GNU Lesser
General Public License, applies to certain designated libraries, and
is quite different from the ordinary General Public License.  We use
this license for certain libraries in order to permit linking those
libraries into non-free programs.

  When a program is linked with a library, whether statically or using
a shared library, the combination of the two is legally speaking a
combined work, a derivative of the original library.  The ordinary
General Public License therefore permits such linking only if the
entire combination fits its criteria of freedom.  The Lesser General
Public License permits more lax criteria for linking other code with
the library.

  We call this license the "Lesser" General Public License because it
does Less to protect the user's freedom than the ordinary General
Public License.  It also provides other free software developers Less
of an advantage over competing non-free programs.  These disadvantages
are the reason we use the ordinary General Public License for many
libraries.  However, the Lesser license provides advantages in certain
special circumstances.

  For example, on rare occasions, there may be a special need to
encourage the widest possible use of a certain library, so that it becomes
a de-facto standard.  To achieve this, non-free programs must be
allowed to use the library.  A more frequent case is that a free
library does the same job as widely used non-free libraries.  In this
case, there is little to gain by limiting the free library to free
software only, so we use the Lesser General Public License.

  In other cases, permission to use a particular library in non-free
programs enables a greater number of people to use a large body of
free software.  For example, permission to use the GNU C Library in
non-free programs enables many more people to use the whole GNU
operating system, as well as its variant, the GNU/Linux operating
system.

  Although the Lesser General Public License is Less protective of the
users' freedom, it does ensure that the user of a program that is
linked with the Library has the freedom and the wherewithal to run
that program using a modified version of the Library.

  The precise terms and conditions for copying, distribution and
modification follow.  Pay close attention to the difference between a
"work based on the library" and a "work that uses the library".  The
former contains code derived from the library, whereas the latter must
be combined with the library in order to run.

                  GNU LESSER GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License Agreement applies to any software library or other
program which contains a notice placed by the copyright holder or
other authorized party saying it may be distributed under the terms of
this Lesser General Public License (also called "this License").
Each licensee is addressed as "you".

  A "library" means a collection of software functions and/or data
prepared so as to be conveniently linked with application programs
(which use some of those functions and data) to form executables.

  The "Library", below, refers to any such software library or work
which has been distributed under these terms.  A "work based on the
Library" means either the Library or any derivative work under
copyright law: that is to say, a work containing the Library or a
portion of it, either verbatim or with modifications and/or translated
straightforwardly into another language.  (Hereinafter, translation is
included without limitation in the term "modification".)

  "Source code" for a work means the preferred form of the work for
making modifications to it.  For a library, complete source code means
all the source code for all modules it contains, plus any associated
interface definition files, plus the scripts used to control compilation
and installation of the library.

  Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running a program using the Library is not restricted, and output from
such a program is covered only if its contents constitute a work based
on the Library (independent of the use of the Library in a tool for
writing it).  Whether that is true depends on what the Library does
and what the program that uses the Library does.

  1. You may copy and distribute verbatim copies of the Library's
complete source code as you receive it, in any medium, provided that
you conspicuously and appropriately publish on each copy an
appropriate copyright notice and disclaimer of warranty; keep intact
all the notices that refer to this License and to the absence of any
warranty; and distribute a copy of this License along with the
Library.

  You may charge a fee for the physical act of transferring a copy,
and you may at your option offer warranty protection in exchange for a
fee.

  2. You may modify your copy or copies of the Library or any portion
of it, thus forming a work based on the Library, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) The modified work must itself be a software library.

    b) You must cause the files modified to carry prominent notices
    stating that you changed the files and the date of any change.

    c) You must cause the whole of the work to be licensed at no
    charge to all third parties under the terms of this License.

    d) If a facility in the modified Library refers to a function or a
    table of data to be supplied by an application program that uses
    the facility, other than as an argument passed when the facility
    is invoked, then you must make a good faith effort to ensure that,
    in the event an application does not supply such function or
    table, the facility still operates, and performs whatever part of
    its purpose remains meaningful.

    (For example, a function in a library to compute square roots has
    a purpose that is entirely well-defined independent of the
    application.  Therefore, Subsection 2d requires that any
    application-supplied function or table used by this function must
    be optional: if the application does not supply it, the square
    root function must still compute square roots.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Library,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Library, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote
it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Library.

In addition, mere aggregation of another work not based on the Library
with the Library (or with a work based on the Library) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.  To do
this, you must alter all the notices that refer to this License, so
that they refer to the ordinary GNU General Public License, version 2,
instead of to this License.  (If a newer version than version 2 of the
ordinary GNU General Public License has appeared, then you can specify
that version instead if you wish.)  Do not make any other change in
these notices.

  Once this change is made in a given copy, it is irreversible for
that copy, so the ordinary GNU General Public License applies to all
subsequent copies and derivative works made from that copy.

  This option is useful when you wish to copy part of the code of
the Library into a program that is not a library.

  4. You may copy and distribute the Library (or a portion or
derivative of it, under Section 2) in object code or executable form
under the terms of Sections 1 and 2 above provided that you accompany
it with the complete corresponding machine-readable source code, which
must be distributed under the terms of Sections 1 and 2 above on a
medium customarily used for software interchange.

  If distribution of object code is made by offering access to copy
from a designated place, then offering equivalent access to copy the
source code from the same place satisfies the requirement to
distribute the source code, even though third parties are not
compelled to copy the source along with the object code.

  5. A program that contains no derivative of any portion of the
Library, but is designed to work with the Library by being compiled or
linked with it, is called a "work that uses the Library".  Such a
work, in isolation, is not a derivative work of the Library, and
therefore falls outside the scope of this License.

  However, linking a "work that uses the Library" with the Library
creates an executable that is a derivative of the Library (because it
contains portions of the Library), rather than a "work that uses the
library".  The executable is therefore covered by this License.
Section 6 states terms for distribution of such executables.

  When a "work that uses the Library" uses material from a header file
that is part of the Library, the object code for the work may be a
derivative work of the Library even though the source code is not.
Whether this is true is especially significant if the work can be
linked without the Library, or if the work is itself a library.  The
threshold for this to be true is not precisely defined by law.

  If such an object file uses only numerical parameters, data
structure layouts and accessors, and small macros and small inline
functions (ten lines or less in length), then the use of the object
file is unrestricted, regardless of whether it is legally a derivative
work.  (Executables containing this object code plus portions of the
Library will still fall under Section 6.)

  Otherwise, if the work is a derivative of the Library, you may
distribute the object code for the work under the terms of Section 6.
Any executables containing that work also fall under Section 6,
whether or not they are linked directly with the Library itself.

  6. As an exception to the Sections above, you may also combine or
link a "work that uses the Library" with the Library to produce a
work containing portions of the Library, and distribute that work
under terms of your choice, provided that the terms permit
modification of the work for the customer's own use and reverse
engineering for debugging such modifications.

  You must give prominent notice with each copy of the work that the
Library is used in it and that the Library and its use are covered by
this License.  You must supply a copy of this License.  If the work
during execution displays copyright notices, you must include the
copyright notice for the Library among them, as well as a reference
directing the user to the copy of this License.  Also, you must do one
of these things:

    a) Accompany the work with the complete corresponding
    machine-readable source code for the Library including whatever
    changes were used in the work (which must be distributed under
    Sections 1 and 2 above); and, if the work is an executable linked
    with the Library, with the complete machine-readable "work that
    uses the Library", as object code and/or source code, so that the
    user can modify the Library and then relink to produce a modified
    executable containing the modified Library.  (It is understood
    that the user who changes the contents of definitions files in the
    Library will not necessarily be able to recompile the application
    to use the modified definitions.)

    b) Use a suitable shared library mechanism for linking with the
    Library.  A suitable mechanism is one that (1) uses at run time a
    copy of the library already present on the user's computer system,
    rather than copying library functions into the executable, and (2)
    will operate properly with a modified version of the library, if
    the user installs one, as long as the modified version is
    interface-compatible with the version that the work was made with.

    c) Accompany the work with a written offer, valid for at
    least three years, to give the same user the materials
    specified in Subsection 6a, above, for a charge no more
    than the cost of performing this distribution.

    d) If distribution of the work is made by offering access to copy
    from a designated place, offer equivalent access to copy the above
    specified materials from the same place.

    e) Verify that the user has already received a copy of these
    materials or that you have already sent this user a copy.

  For an executable, the required form of the "work that uses the
Library" must include any data and utility programs needed for
reproducing the executable from it.  However, as a special exception,
the materials to be distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies
the executable.

  It may happen that this requirement contradicts the license
restrictions of other proprietary libraries that do not normally
accompany the operating system.  Such a contradiction means you cannot
use both them and the Library together in an executable that you
distribute.

  7. You may place library facilities that are a work based on the
Library side-by-side in a single library together with other library
facilities not covered by this License, and distribute such a combined
library, provided that the separate distribution of the work based on
the Library and of the other library facilities is otherwise
permitted, and provided that you do these two things:

    a) Accompany the combined library with a copy of the same work
    based on the Library, uncombined with any other library
    facilities.  This must be distributed under the terms of the
    Sections above.

    b) Give prominent notice with the combined library of the fact
    that part of it is a work based on the Library, and explaining
    where to find the accompanying uncombined form of the same work.

  8. You may not copy, modify, sublicense, link with, or distribute
the Library except as expressly provided under this License.  Any
attempt otherwise to copy, modify, sublicense, link with, or
distribute the Library is void, and will automatically terminate your
rights under this License.  However, parties who have received copies,
or rights, from you under this License will not have their licenses
terminated so long as such parties remain in full compliance.

  9. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Library or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Library (or any work based on the
Library), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Library or works based on it.

  10. Each time you redistribute the Library (or any work based on the
Library), the recipient automatically receives a license from the
original licensor to copy, distribute, link with or modify the Library
subject to these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties with
this License.

  11. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Library at all.  For example, if a patent
license would not permit royalty-free redistribution of the Library by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Library.

If any portion of this section is held invalid or unenforceable under any
particular circumstance, the balance of the section is intended to apply,
and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  12. If the distribution and/or use of the Library is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Library under this License may add
an explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded.  In such case, this License incorporates the limitation as if
written in the body of this License.

  13. The Free Software Foundation may publish revised and/or new
versions of the Lesser General Public License from time to time.
Such new versions will be similar in spirit to the present version,
but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation.

  14. If you wish to incorporate parts of the Library into other free
programs whose distribution conditions are incompatible with these,
write to the author to ask for permission.  For software which is
copyrighted by the Free Software Foundation, write to the Free
Software Foundation; we sometimes make exceptions for this.  Our
decision will be guided by the two goals of preserving the free status
of all derivatives of our free software and of promoting the sharing
and reuse of software generally.

                            NO WARRANTY

  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
LIBRARY IS WITH YOU.  SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

                     END OF TERMS AND CONDITIONS

           How to Apply These Terms to Your New Libraries

  If you develop a new library, and you want it to be of the greatest
possible use to the public, we recommend making it free software that
everyone can redistribute and change.  You can do so by permitting
redistribution under these terms (or, alternatively, under the terms of the
ordinary General Public License).

  To apply these terms, attach the following notices to the library.  It is
safest to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least the
"copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA

Also add information on how to contact you by electronic and paper mail.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the library, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the
  library `Frob' (a library for tweaking knobs) written by James Random
  Hacker.

  {signature of Ty Coon}, 1 April 1990
  Ty Coon, President of Vice

That's all there is to it!


File: /README.md
Mikrotik RouterOS API realization based on Ben Menking's https://github.com/BenMenking/routeros-api
Written in Visual FoxPro 9.0 SP2 

File: /test.prg
PROCEDURE test
	SET PROCEDURE TO 'winsocket', 'hex2ascii', 'base2base'
	SET CLASSLIB TO 'mikrotik_sync', 'md5'
	
	MTikAPI   = CREATEOBJECT('mikrotikapi')
	
	MTikAPI.MTikIP   = '192.168.88.1'
	MTikAPI.MTikPort = 8728
SET STEP ON 
	IF !MTikAPI.connectMTik()
		****	write some log info
		RETURN .F.
	ENDIF 
	
	MTikAPI.MTikLogin = 'admin'
	MTikAPI.MTikPassword = 'admin'
	
	IF !MTikAPI.logInMTik()
		****	write some log info
		RETURN .F.
	ENDIF 
	
	CREATE CURSOR tcurss (param_name C(100), param_val C(100))	
	
	****	simple example

	MTikAPI.composeCommand('/interface/print')
	MTikAPI.parseResponse()

	FOR i = 1 TO ALEN(MTikAPI.MTikResponseParsedArray, 1)
		INSERT INTO tcurss (param_name, param_val) ;
					VALUES (MTikAPI.MTikResponseParsedArray[i, 1], MTikAPI.MTikResponseParsedArray[i, 2])
	ENDFOR 
	
	SELECT tcurss	
	BROWSE NORMAL 
	APPEND BLANK
	APPEND BLANK
	APPEND BLANK
	APPEND BLANK

*!*		MTikAPI.composeCommand('/queue/simple/print')
*!*		MTikAPI.parseResponse()

*!*		FOR i = 1 TO ALEN(MTikAPI.MTikResponseParsedArray, 1)
*!*			INSERT INTO tcurss (param_name, param_val) ;
*!*						VALUES (MTikAPI.MTikResponseParsedArray[i, 1], MTikAPI.MTikResponseParsedArray[i, 2])
*!*		ENDFOR 
*!*		
*!*		SELECT tcurss	
*!*		BROWSE NORMAL 
*!*		APPEND BLANK
*!*		APPEND BLANK
*!*		APPEND BLANK
*!*		APPEND BLANK
*!*		
*!*		
	****	now trying to make some queries to get particular records	
	DIMENSION props [2,2]
	props[1,1] = '.proplist'
	props[1,2] = '.id'
	props[2,1] = '?address'			&& you can put any attribute here, like 'server' or 'comment' - any,
									&& existing in '/ip dhcp-server lease' (like name of a colunm in Winbox)									
	props[2,2] = '10.100.0.120' 		&& put any existing IP here (or whatever you're looking for)

	MTikResult = .F.				
	MTikResult = MTikAPI.composeCommand('/ip/dhcp-server/lease/print', @props)

	IF MTikResult	&& if anything found
		MTikAPI.parseResponse()

		FOR i = 1 TO ALEN(MTikAPI.MTikResponseParsedArray, 1)
			INSERT INTO tcurss (param_name, param_val) ;
						VALUES (MTikAPI.MTikResponseParsedArray[i, 1], MTikAPI.MTikResponseParsedArray[i, 2])
		ENDFOR 
		
		SELECT tcurss	
		BROWSE NORMAL 
		APPEND BLANK
		APPEND BLANK

		****	now, let's try to modify the record we've found 
		DIMENSION props [2,2]
		props[1,1] = '.id'
		props[1,2] = MTikAPI.MTikResponseParsedArray[1,2]	&& the Mikrotik ID of the record we've found
		props[2,1] = 'comment'
		props[2,2] = 'lalalalala' 
		
*		MTikResult = MTikAPI.composeCommand('/ip/dhcp-server/lease/set', @props)
	ENDIF 

	DIMENSION props [4,2]
	props[1,1] = '.proplist'
	props[1,2] = '.id'
	props[2,1] = '?target'			&& you can put any attribute here, like 'name' or 'comment' - any,
									&& existing in '/queue simple' (like name of a colunm in Winbox)
	props[2,2] = '"10.24.4.1/32"' 	&& put any existing IP here (or whatever you're looking for)
	props[3,1] = '?disabled'
	props[3,2] = 'no'
	props[4,1] = '?#'
	props[4,2] = '&'
SET STEP ON 	
	MTikResult = .F.				
	MTikResult = MTikAPI.composeCommand('/queue/simple/print', @props)
	
	IF MTikResult	&& if anything found
		MTikAPI.parseResponse()
		
		FOR i = 1 TO ALEN(MTikAPI.MTikResponseParsedArray, 1)
			INSERT INTO tcurss (param_name, param_val) ;
						VALUES (MTikAPI.MTikResponseParsedArray[i, 1], MTikAPI.MTikResponseParsedArray[i, 2])
		ENDFOR 
		
		SELECT tcurss
		BROWSE NORMAL
		APPEND BLANK
		APPEND BLANK

		****	now, let's try to modify the record we've found 
		DIMENSION props [2,2]
		props[1,1] = '.id'
		props[1,2] = MTikAPI.MTikResponseParsedArray[1,2]	&& the Mikrotik ID of the record we've found
		props[2,1] = 'comment'
		props[2,2] = 'lalalalala'
		
		MTikResult = MTikAPI.composeCommand('/queue/simple/set', @props)
	ENDIF 	
ENDPROC 

File: /winsocket.prg
*************************************************************************************************
**************************************************
*-- Class:        CWinSocket
*-- ParentClass:  custom
*-- BaseClass:    custom
*
DEFINE CLASS CWinSocket As Custom

#DEFINE AF_INET       2
#DEFINE SOCK_STREAM   1
#DEFINE IPPROTO_TCP   6
#DEFINE SOCKET_ERROR -1
#DEFINE FD_READ       1

#DEFINE CRLF          chr(13)+chr(10)
  
 host     = ""
 IP       = ""
 Port     = 80
 hSocket  = 0
 cIn      = ""
 WaitForRead = 0
 Time_out	=	1000
 cString = ""

FUNCTION Init()
  THIS.decl
  IF WSAStartup(0x202, Repli(Chr(0),512)) <> 0
    * unable to initialize Winsock on this computer
	RETURN .F.
  ELSE
	=rand(-1)
	RETURN .T.
  ENDIF
ENDFUNC

PROCEDURE Destroy
  = WSACleanup()
ENDPROC
  
PROCEDURE HostAssign( vNewVal )
  THIS.IP = iif(empty(vNewVal),"",THIS.GetIP(vNewVal))
  THIS.Host = iif(empty(THIS.IP),"",vNewVal)
ENDPROC

PROTECTED FUNCTION GetIP( pcHost )
  #DEFINE HOSTENT_SIZE 16
  LOCAL nStruct, nSize, cBuffer, nAddr, cIP
  nStruct = gethostbyname(pcHost)
  IF nStruct = 0
	RETURN ""
  ENDIF
  cBuffer = Repli(Chr(0), HOSTENT_SIZE)
  cIP = Repli(Chr(0), 4)
  = CopyMemory(@cBuffer, nStruct, HOSTENT_SIZE)
  = CopyMemory(@cIP, THIS.buf2dword(SUBS(cBuffer,13,4)),4)
  = CopyMemory(@cIP, THIS.buf2dword(cIP),4)
  RETURN inet_ntoa(THIS.buf2dword(cIP))
ENDFUNC

FUNCTION Connect
  LOCAL cBuffer, cPort, cHost, lResult
  THIS.hSocket = socket(AF_INET, SOCK_STREAM,0) 		&&	IPPROTO_TCP)
  IF THIS.hSocket = SOCKET_ERROR
	RETURN .F.
  ENDIF
    
*  cPort = THIS.num2word(htons(THIS.Port)) - as this will not work in win10 and win 8/8.1 probably
*	so using this hack	BitAnd(htons(8728), 0xffff)
*	found here: 
*	https://stackoverflow.com/questions/47475862/wsock32-dll-htons-function

  cPort = THIS.num2word(BitAnd(htons(this.Port), 0xffff))
  nHost = inet_addr(THIS.IP)
  cHost = THIS.num2dword(nHost)
  cBuffer = THIS.num2word(AF_INET) + cPort + cHost + Repli(Chr(0),8)
  lResult = (ws_connect(THIS.hSocket, @cBuffer, Len(cBuffer))=0)
  RETURN lResult
ENDFUNC

FUNCTION Disconnect
  if THIS.hSocket<>SOCKET_ERROR
	= closesocket(THIS.hSocket)
  endif
  THIS.hSocket = SOCKET_ERROR
ENDFUNC

* GET *************************************************************
* pcUrl - string like "HTTP://www.test.com/test.php"
* cHeaders - strings lika '<Name>: <value>'+chr(13)+chr(10)
*
* If cHeaders assgined - assigned headers are send

FUNCTION Get(pcUrl,cHeaders)
  LOCAL lResult
  IF THIS.Connect()
	THIS.snd('GET '+pcURL+' http/1.0'+crlf)
	if	!empty(cHeaders)
		THIS.snd(cHeaders)
	endif
	THIS.snd(crlf,.t.) && End of headers
	lResult = .T.
  ELSE
	lResult = .F.
  ENDIF
  THIS.Disconnect()
ENDFUNC

* POST **************************************************************
* pcUrl - string like "HTTP://www.test.com/test.php"
* cHeaders - strings lika '<Name>: <value>'+chr(13)+chr(10)
* cStr - string like ['<VarName.>=<Var value.>'+'&']+[<VarName. for pcData>]+chr(13)+chr(10)
* pcData - character string with data to pass to the server
* 
* If cHeaders assgined - headers are send before the data.
* If cStr is not assigned - pcData is send and an empty string 
* 	and it supposed pcData contains cStr and datablock already 

FUNCTION Post(pcUrl, cHeaders, cStr, pcData)
  LOCAL lResult, lcB, lcStr, lnCount, lnCnt, lcName, lcValue, lT1, lT2
  this.cIn=""
  IF THIS.Connect()
	lcB="pst"+alltrim(str(1000000*rand(),6))
	THIS.snd('POST '+pcURL+' http/1.0'+crlf)
	if	!empty(cHeaders)
		THIS.snd(cHeaders)
	endif
	if	!empty(cStr)
		THIS.snd('Content-Type: multipart/form-data; boundary='+lcB+crlf)
		lcStr=""
		lnCount=occurs("&",cStr)
		if	lnCount#0
			for	lnCnt=1	to	lnCount	step	1
				lT1=AT("=",cStr,1)-1
				lT2=AT("&",cStr,1)-1
				lcName=substr(cStr,1,lT1)
				lcValue=substr(cStr,lT1+2,lT2-lT1-1)
				lcStr=lcStr+"--"+lcB+crlf+'Content-Disposition: form-data; name="'+lcName+'"'+crlf+crlf+lcValue+crlf
				cStr=substr(cStr,lT2+2,len(cStr)-lT2+1)
			endfor
		endif
		lT1=AT("=",cStr,1)-1
		if	lT1>0
			lcStr=lcStr+"--"+lcB+crlf+'Content-Disposition: form-data; name="'+substr(cStr,1,lT1)+'"'+crlf+crlf
			lcStr=lcStr+alltrim(substr(cStr,lT1+2,len(cStr)-lT1+1))+crlf+'--'+lcB+'--'+crlf
		else
			lcStr=lcStr+"--"+lcB+crlf+'Content-Disposition: form-data; name="'+cStr+'"'+crlf+crlf
			lcStr=lcStr+pcData+crlf+'--'+lcB+'--'+crlf
		endif
		THIS.snd('Content-Length: '+alltrim(str(len(lcStr)))+crlf)
		THIS.snd(crlf) && End of headers
		THIS.snd(lcStr,.t.) && get a response, too.
	else
		if	!empty(pcData)
			THIS.snd(crlf)			&& End of headers
			THIS.snd(pcData,.t.)	&& get a response, too.
		else
			THIS.snd(crlf,.t.)		&& get a response, too.
		endif
	endif
	lResult = .T.
  ELSE
	lResult = .F.
  ENDIF
  THIS.Disconnect()
  This.cString=lcStr
ENDFUNC

  FUNCTION sendSocket(cData, lResponse)
    LOCAL cBuffer, nResult, cResponse
    cBuffer = cData && + CrLf
    nResult = send(THIS.hSocket, @cBuffer, Len(cBuffer), 0)
    IF nResult = SOCKET_ERROR
        RETURN .F.
    ENDIF
    IF Not lResponse
        RETURN .T.
    ENDIF

    LOCAL hEventRead, nWait, cRead
    DO WHILE .T.
        * creating event, linking it to the socket and wait
        hEventRead = WSACreateEvent()
        = WSAEventSelect(THIS.hSocket, hEventRead, FD_READ)

        * 1000 milliseconds can be not enough
        THIS.WaitForRead = WSAWaitForMultipleEvents(1, @hEventRead, 0, THIS.Time_out, 0)
        = WSACloseEvent(hEventRead)

        IF THIS.WaitForRead <> 0 && error or timeout
            EXIT
        ENDIF
        
        * reading data from connected socket
        THIS.cIn = THIS.cIn+THIS.Rd()
    ENDDO
  RETURN .T.
  ENDFUNC

  FUNCTION readSocket
  #DEFINE READ_SIZE 65536
    LOCAL cRecv, nRecv, nFlags
    cRecv = Repli(Chr(0), READ_SIZE)
    nFlags = 0
    nRecv = recv(THIS.hSocket, @cRecv, READ_SIZE, nFlags)
    RETURN Iif(nRecv<=0, "", LEFT(cRecv, nRecv))
  ENDFUNC

  PROCEDURE decl
    DECLARE INTEGER gethostbyname IN ws2_32 STRING host
    DECLARE STRING inet_ntoa IN ws2_32 INTEGER in_addr
    DECLARE INTEGER socket IN ws2_32 INTEGER af, INTEGER tp, INTEGER pt
    DECLARE INTEGER closesocket IN ws2_32 INTEGER s
    DECLARE INTEGER WSACreateEvent IN ws2_32
    DECLARE INTEGER WSACloseEvent IN ws2_32 INTEGER hEvent
    DECLARE GetSystemTime IN kernel32 STRING @lpSystemTime
    DECLARE INTEGER inet_addr IN ws2_32 STRING cp
    DECLARE INTEGER htons IN ws2_32 INTEGER hostshort
    DECLARE INTEGER WSAStartup IN ws2_32 INTEGER wVerRq, STRING lpWSAData
    DECLARE INTEGER WSACleanup IN ws2_32

    DECLARE INTEGER connect IN ws2_32 AS ws_connect ;
        INTEGER s, STRING @sname, INTEGER namelen

    DECLARE INTEGER send IN ws2_32;
        INTEGER s, STRING @buf, INTEGER buflen, INTEGER flags

    DECLARE INTEGER recv IN ws2_32;
        INTEGER s, STRING @buf, INTEGER buflen, INTEGER flags

    DECLARE INTEGER WSAEventSelect IN ws2_32;
        INTEGER s, INTEGER hEventObject, INTEGER lNetworkEvents

    DECLARE INTEGER WSAWaitForMultipleEvents IN ws2_32;
        INTEGER cEvents, INTEGER @lphEvents, INTEGER fWaitAll,;
        INTEGER dwTimeout, INTEGER fAlertable

    DECLARE RtlMoveMemory IN kernel32 As CopyMemory;
        STRING @Dest, INTEGER Src, INTEGER nLength
  ENDPROC

  FUNCTION buf2dword(lcBuffer)
    RETURN Asc(SUBSTR(lcBuffer, 1,1)) + ;
        BitLShift(Asc(SUBSTR(lcBuffer, 2,1)), 8) +;
        BitLShift(Asc(SUBSTR(lcBuffer, 3,1)), 16) +;
        BitLShift(Asc(SUBSTR(lcBuffer, 4,1)), 24)
  ENDFUNC
  
  FUNCTION num2dword(lnValue)
  #DEFINE m0 256
  #DEFINE m1 65536
  #DEFINE m2 16777216
      IF lnValue < 0
          lnValue = 0x100000000 + lnValue
      ENDIF
      LOCAL b0, b1, b2, b3
      b3 = Int(lnValue/m2)
      b2 = Int((lnValue - b3*m2)/m1)
      b1 = Int((lnValue - b3*m2 - b2*m1)/m0)
      b0 = Mod(lnValue, m0)
  RETURN Chr(b0)+Chr(b1)+Chr(b2)+Chr(b3)
  ENDFUNC
  
  FUNCTION num2word(lnValue)
    RETURN Chr(MOD(m.lnValue,256)) + CHR(INT(m.lnValue/256))
  ENDFUNC

ENDDEFINE
*
*-- EndDefine: CWinSocket
**************************************************


