# Repository Information
Name: Laravel-Mikrotik-API

# Directory Structure
Directory structure:
└── github_repos/Laravel-Mikrotik-API/
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
    │   │       ├── pack-99c828a5fbec14a0c8146149b390c4c5fc422d7c.idx
    │   │       └── pack-99c828a5fbec14a0c8146149b390c4c5fc422d7c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── composer.json
    ├── README.MD
    └── src/
        ├── Cache/
        │   ├── SHM/
        │   │   ├── Adapter/
        │   │   │   ├── APC.php
        │   │   │   ├── APCu.php
        │   │   │   ├── Placebo.php
        │   │   │   └── Wincache.php
        │   │   ├── Exception.php
        │   │   └── InvalidArgumentException.php
        │   └── SHM.php
        ├── Client.php
        ├── Communicator.php
        ├── Console/
        │   ├── Color/
        │   │   ├── Backgrounds.php
        │   │   ├── Exception.php
        │   │   ├── Flags.php
        │   │   ├── Fonts.php
        │   │   ├── Styles.php
        │   │   └── UnexpectedValueException.php
        │   ├── Color.php
        │   ├── CommandLine/
        │   │   ├── Action/
        │   │   │   ├── Action_List.php
        │   │   │   ├── Callback.php
        │   │   │   ├── Counter.php
        │   │   │   ├── Help.php
        │   │   │   ├── Password.php
        │   │   │   ├── StoreArray.php
        │   │   │   ├── StoreFalse.php
        │   │   │   ├── StoreFloat.php
        │   │   │   ├── StoreInt.php
        │   │   │   ├── StoreString.php
        │   │   │   ├── StoreTrue.php
        │   │   │   └── Version.php
        │   │   ├── Action.php
        │   │   ├── Argument.php
        │   │   ├── Command.php
        │   │   ├── CustomMessageProvider.php
        │   │   ├── Element.php
        │   │   ├── Exception.php
        │   │   ├── MessageProvider/
        │   │   │   └── DefaultProvider.php
        │   │   ├── MessageProvider.php
        │   │   ├── Option.php
        │   │   ├── Outputter.php
        │   │   ├── Outputter_Default.php
        │   │   ├── Renderer.php
        │   │   ├── Renderer_Default.php
        │   │   ├── Result.php
        │   │   └── XmlParser.php
        │   └── CommandLine.php
        ├── DataFlowException.php
        ├── Exception.php
        ├── InvalidArgumentException.php
        ├── LengthException.php
        ├── Message.php
        ├── MikrotikServiceProvider.php
        ├── Net/
        │   └── Transmitter/
        │       ├── Exception.php
        │       ├── FilterCollection.php
        │       ├── LockException.php
        │       ├── NetworkStream.php
        │       ├── SocketException.php
        │       ├── Stream.php
        │       ├── StreamException.php
        │       ├── TcpClient.php
        │       └── TcpServerConnection.php
        ├── NotSupportedException.php
        ├── ParserException.php
        ├── Query.php
        ├── Registry.php
        ├── Request.php
        ├── Response.php
        ├── ResponseCollection.php
        ├── RouterErrorException.php
        ├── Script.php
        ├── SocketException.php
        ├── StreamException.php
        ├── UnexpectedValueException.php
        └── Util.php


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
	url = https://github.com/bnjunge/Laravel-Mikrotik-API.git
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
0000000000000000000000000000000000000000 25606ffae313d988fd60716e3306907c8d36112c vivek-dodia <vivek.dodia@icloud.com> 1738606353 -0500	clone: from https://github.com/bnjunge/Laravel-Mikrotik-API.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 25606ffae313d988fd60716e3306907c8d36112c vivek-dodia <vivek.dodia@icloud.com> 1738606353 -0500	clone: from https://github.com/bnjunge/Laravel-Mikrotik-API.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 25606ffae313d988fd60716e3306907c8d36112c vivek-dodia <vivek.dodia@icloud.com> 1738606353 -0500	clone: from https://github.com/bnjunge/Laravel-Mikrotik-API.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
25606ffae313d988fd60716e3306907c8d36112c refs/remotes/origin/master


File: /.git\refs\heads\master
25606ffae313d988fd60716e3306907c8d36112c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /composer.json
{
    "name": "mikrotikapisurvtech/survteckmikrotik",
    "type": "package",
    "version": "1.0",
    "description": "Convert BNjunge Mikrotik API into Composer psr-4 compatible",
    "license": "MIT",
    "authors": [
        {
            "name": "bnjunge",
            "email": "survtechke@gmail.com"
        }
    ],
    "require": {},
    "autoload": {
        "psr-4": {
            "BNjunge\\": "src/",
            "BNjunge\\Net\\Transmitter\\": "src/Net/Transmitter",
            "BNjunge\\Cache\\": "src/Cache",
            "BNjunge\\Cache\\SHM\\": "src/Cache/SHM",
            "BNjunge\\Cache\\SHM\\Adapter\\": "src/Cache/SHM/Adapter",
            "BNjunge\\Console\\": "src/Console",
            "BNjunge\\Console\\CommandLine\\": "src/Console/CommandLine",
            "BNjunge\\Console\\CommandLine\\Action\\": "src/Console/CommandLine/Action",
            "BNjunge\\Console\\CommandLine\\MessageProvider\\": "src/Console/CommandLine/MessageProvider",
            "BNjunge\\Console\\Color\\": "src/Console/Color"
        }
    },
    "extra": {
        "laravel": {
            "providers": [
                "BNjunge\\MikrotikServiceProvider"
            ]
        }
    }
}


File: /README.MD
### Mikrotik API Laravel Package
This is a Laravel Package for Mikrotik API Developed out of intrest

File: /src\Cache\SHM\Adapter\APC.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 *
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link APC::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the APC extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class APC extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases even on errors in the
     * critical sections, since APC doesn't have an actual locking function.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as key) obtained
     * during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId = __CLASS__ . ' ' . $persistentId;
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
        register_shutdown_function(
            get_called_class() . '::releaseLocks',
            $this->persistentId,
            true
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('apc')
            && version_compare(phpversion('apc'), '3.1.1', '>=')
            && ini_get('apc.enabled')
            && ('cli' !== PHP_SAPI || ini_get('apc.enable_cli'));
    }

    /**
     * Releases all locks in a storage.
     *
     * This function is not meant to be used directly. It is implicitly called
     * by the the destructor and as a shutdown function when the request ends.
     * One of these calls ends up releasing any unreleased locks obtained
     * during the request. A lock is also implicitly released as soon as there
     * are no objects left in the current request using the same persistent ID.
     *
     * @param string $internalPersistentId The internal persistent ID, the locks
     *     of which are being released.
     * @param bool   $isAtShutdown         Whether the function was executed at
     *     shutdown.
     *
     * @return void
     *
     * @internal
     */
    public static function releaseLocks($internalPersistentId, $isAtShutdown)
    {
        $hasInstances = 0 !== static::$requestInstances[$internalPersistentId];
        if ($isAtShutdown === $hasInstances) {
            foreach (static::$locksBackup[$internalPersistentId] as $key) {
                apc_delete($internalPersistentId . 'l ' . $key);
            }
        }
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        static::$requestInstances[$this->persistentId]--;
        static::releaseLocks($this->persistentId, false);
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $hasTimeout = $timeout !== null;
        $start = microtime(true);
        while (!apc_add($lock, 1)) {
            if ($hasTimeout && (microtime(true) - $start) > $timeout) {
                return false;
            }
        }
        static::$locksBackup[$this->persistentId] = $key;
        return true;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $success = apc_delete($lock);
        if ($success) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
            return true;
        }
        return false;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return apc_exists($this->persistentId . 'd ' . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return apc_add($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return apc_store($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $fullKey = $this->persistentId . 'd ' . $key;
        if (apc_exists($fullKey)) {
            $value = apc_fetch($fullKey, $success);
            if (!$success) {
                throw new SHM\InvalidArgumentException(
                    'Unable to fetch key. ' .
                    'Key has either just now expired or (if no TTL was set) ' .
                    'is possibly in a race condition with another request.',
                    100
                );
            }
            return $value;
        }
        throw new SHM\InvalidArgumentException('No such key in cache', 101);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return apc_delete($this->persistentId . 'd ' . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = apc_inc(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                102
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = apc_dec(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                103
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return apc_cas($this->persistentId . 'd ' . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            apc_delete($key);
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $result = array();
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            $localKey = strstr($key, $this->persistentId . 'd ');
            if (null === $filter || preg_match($filter, $localKey)) {
                if ($keysOnly) {
                    $result[] = $localKey;
                } else {
                    $result[$localKey] = apc_fetch($key);
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Cache\SHM\Adapter\APCu.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 *
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link APC::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the APC extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class APCu extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases even on errors in the
     * critical sections, since APC doesn't have an actual locking function.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as key) obtained
     * during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId = __CLASS__ . ' ' . $persistentId;
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
        register_shutdown_function(
            get_called_class() . '::releaseLocks',
            $this->persistentId,
            true
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('apcu')
            && version_compare(phpversion('apcu'), '5.0.0', '>=')
            && ini_get('apc.enabled')
            && ('cli' !== PHP_SAPI || ini_get('apc.enable_cli'));
    }

    /**
     * Releases all locks in a storage.
     *
     * This function is not meant to be used directly. It is implicitly called
     * by the the destructor and as a shutdown function when the request ends.
     * One of these calls ends up releasing any unreleased locks obtained
     * during the request. A lock is also implicitly released as soon as there
     * are no objects left in the current request using the same persistent ID.
     *
     * @param string $internalPersistentId The internal persistent ID, the locks
     *     of which are being released.
     * @param bool   $isAtShutdown         Whether the function was executed at
     *     shutdown.
     *
     * @return void
     *
     * @internal
     */
    public static function releaseLocks($internalPersistentId, $isAtShutdown)
    {
        $hasInstances = 0 !== static::$requestInstances[$internalPersistentId];
        if ($isAtShutdown === $hasInstances) {
            foreach (static::$locksBackup[$internalPersistentId] as $key) {
                apcu_delete($internalPersistentId . 'l ' . $key);
            }
        }
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        static::$requestInstances[$this->persistentId]--;
        static::releaseLocks($this->persistentId, false);
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $hasTimeout = $timeout !== null;
        $start = microtime(true);
        while (!apcu_add($lock, 1)) {
            if ($hasTimeout && (microtime(true) - $start) > $timeout) {
                return false;
            }
        }
        static::$locksBackup[$this->persistentId] = $key;
        return true;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $success = apcu_delete($lock);
        if ($success) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
            return true;
        }
        return false;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return apcu_exists($this->persistentId . 'd ' . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return apcu_add($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return apcu_store($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $fullKey = $this->persistentId . 'd ' . $key;
        if (apcu_exists($fullKey)) {
            $value = apcu_fetch($fullKey, $success);
            if (!$success) {
                throw new SHM\InvalidArgumentException(
                    'Unable to fetch key. ' .
                    'Key has either just now expired or (if no TTL was set) ' .
                    'is possibly in a race condition with another request.',
                    100
                );
            }
            return $value;
        }
        throw new SHM\InvalidArgumentException('No such key in cache', 101);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return apcu_delete($this->persistentId . 'd ' . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = apcu_inc(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                102
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = apcu_dec(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                103
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return apcu_cas($this->persistentId . 'd ' . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            apcu_delete($key);
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $result = array();
        foreach (new APCUIterator(
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            $localKey = strstr($key, $this->persistentId . 'd ');
            if (null === $filter || preg_match($filter, $localKey)) {
                if ($keysOnly) {
                    $result[] = $localKey;
                } else {
                    $result[$localKey] = apcu_fetch($key);
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Cache\SHM\Adapter\Placebo.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 *
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Placebo::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * This adapter is not truly persistent. It is intended to emulate persistence
 * in non persistent environments, so that upper level applications can use a
 * single code path for persistent and non persistent code.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Placebo extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as
     *     key) obtained during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * The data storage.
     *
     * Each persistent ID is a key, and the value is an array.
     * Each such array has data keys as its keys, and an array as a value.
     * Each such array has as its elements the value, the timeout and the time
     * the data was set.
     *
     * @var array
     */
    protected static $data = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        if (isset(static::$requestInstances[$persistentId])) {
            ++static::$requestInstances[$persistentId];
        } else {
            static::$requestInstances[$persistentId] = 1;
            static::$locksBackup[$persistentId] = array();
            static::$data[$persistentId] = array();
        }
        $this->persistentId = $persistentId;
    }

    /**
     * Releases any unreleased locks.
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            static::$locksBackup[$this->persistentId] = array();
        }
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return 'cli' === PHP_SAPI;
    }

    /**
     * Pretends to obtain a lock.
     *
     * @param string $key     Ignored.
     * @param double $timeout Ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $key = (string) $key;
        if (in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        static::$locksBackup[$this->persistentId][] = $key;
        return true;
    }

    /**
     * Pretends to release a lock.
     *
     * @param string $key Ignored
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $key = (string) $key;
        if (!in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        unset(
            static::$locksBackup[$this->persistentId][array_search(
                $key,
                static::$locksBackup[$this->persistentId],
                true
            )]
        );
        return true;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return array_key_exists($key, static::$data[$this->persistentId]);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        if ($this->exists($key)) {
            return false;
        }
        return $this->set($key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        static::$data[$this->persistentId][$key] = $value;
        return true;
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        if ($this->exists($key)) {
            return static::$data[$this->persistentId][$key];
        }
        throw new SHM\InvalidArgumentException(
            'Unable to fetch key. No such key.',
            200
        );
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        if ($this->exists($key)) {
            unset(static::$data[$this->persistentId][$key]);
            return true;
        }
        return false;
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value + (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                201
            );
        }
        return $this->get($key);
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value - (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                202
            );
        }
        return $this->get($key);
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return $this->exists($key) && ($this->get($key) === $old)
            && is_int($new) && $this->set($key, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        static::$data[$this->persistentId] = array();
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        if (null === $filter) {
            return new ArrayObject(
                $keysOnly
                ? array_keys(static::$data[$this->persistentId])
                : static::$data[$this->persistentId]
            );
        }

        $result = array();
        foreach (static::$data[$this->persistentId] as $key => $value) {
            if (preg_match($filter, $key)) {
                $result[$key] = $value;
            }
        }
        return new ArrayObject($keysOnly ? array_keys($result) : $result);
    }
}


File: /src\Cache\SHM\Adapter\Wincache.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 *
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Wincache::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the WinCache extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Wincache extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names obtained during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId
            = static::encodeLockName(__CLASS__ . ' ' . $persistentId) . ' ';
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
    }

    /**
     * Encodes a lock name
     *
     * Encodes a lock name, so that it can be properly obtained. The scheme used
     * is a subset of URL encoding, with only the "%" and "\" characters being
     * escaped. The encoding itself is necessary, since lock names can't contain
     * the "\" character.
     *
     * @param string $name The lock name to encode.
     *
     * @return string The encoded name.
     *
     * @link http://msdn.microsoft.com/en-us/library/ms682411(VS.85).aspx
     */
    protected static function encodeLockName($name)
    {
        return str_replace(array('%', '\\'), array('%25', '%5C'), $name);
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('wincache')
            && version_compare(phpversion('wincache'), '1.1.0', '>=')
            && ini_get('wincache.ucenabled')
            && ('cli' !== PHP_SAPI || ini_get('wincache.enablecli'));
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            foreach (static::$locksBackup[$this->persistentId] as $key) {
                wincache_unlock(
                    $this->persistentId . static::encodeLockName($key)
                );
            }
        }
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout Ignored with WinCache. Script will always block if
     *     the lock can't be immediately obtained.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $result = wincache_lock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            static::$locksBackup[$this->persistentId] = $key;
        }
        return $result;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $result = wincache_unlock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
        }
        return $result;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return wincache_ucache_exists($this->persistentId . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Sets a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return wincache_ucache_add($this->persistentId . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return wincache_ucache_set($this->persistentId . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $value = wincache_ucache_get($this->persistentId . $key, $success);
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to fetch key. No such key, or key has expired.',
                300
            );
        }
        return $value;
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return wincache_ucache_delete($this->persistentId . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = wincache_ucache_inc(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                301
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = wincache_ucache_dec(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                302
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return wincache_ucache_cas($this->persistentId . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        $info = wincache_ucache_info();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                wincache_ucache_delete($entry['key_name']);
            }
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $info = wincache_ucache_info();
        $result = array();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                $localKey = strstr($entry['key_name'], $this->persistentId);
                if (null === $filter || preg_match($filter, $localKey)) {
                    if ($keysOnly) {
                        $result[] = $localKey;
                    } else {
                        $result[$localKey] = apc_fetch($localKey);
                    }
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Cache\SHM\Exception.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 * 
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Generic exception class of this package.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
interface Exception
{
}


File: /src\Cache\SHM\InvalidArgumentException.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 * 
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Exception thrown when there's something wrong with an argument.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class InvalidArgumentException extends \InvalidArgumentException
    implements Exception
{
}


File: /src\Cache\SHM.php
<?php

/**
 * Wrapper for shared memory and locking functionality across different extensions.

 *
 * Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.2.0
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

/**
 * The namespace declaration.
 */
namespace PEAR2\Cache;

/**
 * Used as a catch-all for adapter initialization.
 */
use Exception as E;

/**
 * Implements this class.
 */
use IteratorAggregate;

/**
 * Used on failures by this class.
 */
use PEAR2\Cache\SHM\InvalidArgumentException;

/**
 * Main class for this package.
 *
 * Automatically chooses an adapter based on the available extensions.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
abstract class SHM implements IteratorAggregate
{
    /**
     * An array of adapter names that meet their requirements.
     *
     * @var array
     */
    private static $_adapters = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage. Adapter is automatically
     * chosen based on the available extensions.
     *
     * @param string $persistentId The ID for the storage.
     *
     * @return static|SHM A new instance of an SHM adapter (child of this
     * class).
     */
    final public static function factory($persistentId)
    {
        foreach (self::$_adapters as $adapter) {
            try {
                return new $adapter($persistentId);
            } catch (E $e) {
                //In case of a runtime error, try to fallback to other adapters.
            }
        }
        throw new InvalidArgumentException(
            'No appropriate adapter available',
            1
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return true;
    }

    /**
     * Registers an adapter.
     *
     * Registers an SHM adapter, allowing you to call it with {@link factory()}.
     *
     * @param string $adapter FQCN of adapter. A valid adapter is one that
     *     extends this class. The class will be autoloaded if not already
     *     present.
     * @param bool   $prepend Whether to prepend this adapter into the list of
     *     possible adapters, instead of appending to it.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    final public static function registerAdapter($adapter, $prepend = false)
    {
        if (class_exists($adapter, true)
            && is_subclass_of($adapter, '\\' . __CLASS__)
            && $adapter::isMeetingRequirements()
        ) {
            if ($prepend) {
                self::$_adapters = array_merge(
                    array($adapter),
                    self::$_adapters
                );
            } else {
                self::$_adapters[] = $adapter;
            }
            return true;
        }
        return false;
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __invoke($key, $value, $ttl = 0)
    {
        return $this->add($key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to get
     * the value of will be fetched from the adapter, treating the property name
     * as the key of the value to get.
     *
     * @param string $key Name of key to get.
     *
     * @return mixed The current value of the specified key.
     */
    public function __get($key)
    {
        return $this->get($key);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to set
     * the value of will be set by the adapter, treating the property name as
     * the key of the value to set. The value is set without a TTL.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __set($key, $value)
    {
        return $this->set($key, $value);
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * This is a magic method, thanks to which any property you call isset() on
     * will be checked by the adapter, treating the property name as the key
     * of the value to check.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function __isset($key)
    {
        return $this->exists($key);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to unset
     * the value of will be unset by the adapter, treating the property name as
     * the key of the value to delete.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __unset($key)
    {
        return $this->delete($key);
    }

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    abstract public function __construct($persistentId);

    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function lock($key, $timeout = null);

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function unlock($key);

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    abstract public function exists($key);

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function add($key, $value, $ttl = 0);

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function set($key, $value, $ttl = 0);

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    abstract public function get($key);

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function delete($key);

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    abstract public function inc($key, $step = 1);

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    abstract public function dec($key, $step = 1);

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function cas($key, $old, $new);

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    abstract public function clear();

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return \Traversable An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    abstract public function getIterator($filter = null, $keysOnly = false);
}

SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Placebo');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Wincache');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\APCu');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\APC');


File: /src\Client.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Refers to transmitter direction constants.
 */
use BNjunge\Net\Transmitter\Stream as S;

/**
 * Refers to the cryptography constants.
 */
use BNjunge\Net\Transmitter\NetworkStream as N;

/**
 * Catches arbitrary exceptions at some points.
 */
use Exception as E;

/**
 * A RouterOS client.
 *
 * Provides functionality for easily communicating with a RouterOS host.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Client
{
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that have a callback.
     */
    const FILTER_CALLBACK = 1;
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that use the buffer.
     */
    const FILTER_BUFFER = 2;
    /**
     * Used in {@link static::isRequestActive()} to indicate no limit in search.
     */
    const FILTER_ALL = 3;

    /**
     * The communicator for this client.
     *
     * @var Communicator
     */
    protected $com;

    /**
     * The number of currently pending requests.
     *
     * @var int
     */
    protected $pendingRequestsCount = 0;

    /**
     * An array of responses that have not yet been extracted
     * or passed to a callback.
     *
     * Key is the tag of the request, and the value is an array of
     * associated responses.
     *
     * @var array<string,Response[]>
     */
    protected $responseBuffer = array();

    /**
     * An array of callbacks to be executed as responses come.
     *
     * Key is the tag of the request, and the value is the callback for it.
     *
     * @var array<string,callback>
     */
    protected $callbacks = array();

    /**
     * A registry for the operations.
     *
     * Particularly helpful at persistent connections.
     *
     * @var Registry
     */
    protected $registry = null;

    /**
     * Whether to stream future responses.
     *
     * @var bool
     */
    private $_streamingResponses = false;

    /**
     * Creates a new instance of a RouterOS API client.
     *
     * Creates a new instance of a RouterOS API client with the specified
     * settings.
     *
     * @param string        $host     Hostname (IP or domain) of RouterOS.
     * @param string        $username The RouterOS username.
     * @param string        $password The RouterOS password.
     * @param int|null      $port     The port on which the RouterOS host
     *     provides the API service. You can also specify NULL, in which case
     *     the port will automatically be chosen between 8728 and 8729,
     *     depending on the value of $crypto.
     * @param bool          $persist  Whether or not the connection should be a
     *     persistent one.
     * @param double|null   $timeout  The timeout for the connection.
     * @param string        $crypto   The encryption for this connection.
     *     Must be one of the BNjunge\Net\Transmitter\NetworkStream::CRYPTO_*
     *     constants. Off by default. RouterOS currently supports only TLS, but
     *     the setting is provided in this fashion for forward compatibility's
     *     sake. And for the sake of simplicity, if you specify an encryption,
     *     don't specify a context and your default context uses the value
     *     "DEFAULT" for ciphers, "ADH" will be automatically added to the list
     *     of ciphers.
     * @param resource|null $context  A context for the socket.
     *
     * @see sendSync()
     * @see sendAsync()
     */
    public function __construct(
        $host,
        $username,
        $password = '',
        $port = 8728,
        $persist = false,
        $timeout = null,
        $crypto = N::CRYPTO_OFF,
        $context = null
    ) {
        $this->com = new Communicator(
            $host,
            $port,
            $persist,
            $timeout,
            $username . '/' . $password,
            $crypto,
            $context
        );
        $timeout = null == $timeout
            ? ini_get('default_socket_timeout')
            : (int) $timeout;
        //Login the user if necessary
        if ((!$persist
            || !($old = $this->com->getTransmitter()->lock(S::DIRECTION_ALL)))
            && $this->com->getTransmitter()->isFresh()
        ) {
            if (!static::login($this->com, $username, $password, $timeout)) {
                $this->com->close();
                throw new DataFlowException(
                    'Invalid username or password supplied.',
                    DataFlowException::CODE_INVALID_CREDENTIALS
                );
            }
        }

        if (isset($old)) {
            $this->com->getTransmitter()->lock($old, true);
        }

        if ($persist) {
            $this->registry = new Registry("{$host}:{$port}/{$username}");
        }
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param mixed $arg Value can be either a {@link Request} to send, which
     *     would be sent asynchronously if it has a tag, and synchronously if
     *     not, a number to loop with or NULL to complete all pending requests.
     *     Any other value is converted to string and treated as the tag of a
     *     request to complete.
     *
     * @return mixed Whatever the long form function would have returned.
     */
    public function __invoke($arg = null)
    {
        if (is_int($arg) || is_double($arg)) {
            return $this->loop($arg);
        } elseif ($arg instanceof Request) {
            return '' == $arg->getTag() ? $this->sendSync($arg)
                : $this->sendAsync($arg);
        } elseif (null === $arg) {
            return $this->completeRequest();
        }
        return $this->completeRequest((string) $arg);
    }

    /**
     * Login to a RouterOS connection.
     *
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinitely.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        if (null !== ($remoteCharset = $com->getCharset($com::CHARSET_REMOTE))
            && null !== ($localCharset = $com->getCharset($com::CHARSET_LOCAL))
        ) {
            $password = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $password
            );
        }
        $old = null;
        try {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()->lock(S::DIRECTION_ALL);
                $result = self::_login($com, $username, $password, $timeout);
                $com->getTransmitter()->lock($old, true);
                return $result;
            }
            return self::_login($com, $username, $password, $timeout);
        } catch (E $e) {
            if ($com->getTransmitter()->isPersistent() && null !== $old) {
                $com->getTransmitter()->lock($old, true);
            }
            throw ($e instanceof NotSupportedException
            || $e instanceof UnexpectedValueException
            || !$com->getTransmitter()->isDataAwaiting()) ? new SocketException(
                'This is not a compatible RouterOS service',
                SocketException::CODE_SERVICE_INCOMPATIBLE,
                $e
            ) : $e;
        }
    }

    /**
     * Login to a RouterOS connection.
     *
     * This is the actual login procedure, applied regardless of persistence and
     * charset settings.
     *
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password. Potentially parsed
     *     already by iconv.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinitely.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    private static function _login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        $request = new Request('/login');
        $request->send($com);
        $response = new Response($com, false, $timeout);
        $request->setArgument('name', $username);
        $request->setArgument(
            'response',
            '00' . md5(
                chr(0) . $password
                . pack('H*', $response->getProperty('ret'))
            )
        );
        $request->verify($com)->send($com);

        $response = new Response($com, false, $timeout);
        if ($response->getType() === Response::TYPE_FINAL) {
            return null === $response->getProperty('ret');
        } else {
            while ($response->getType() !== Response::TYPE_FINAL
                && $response->getType() !== Response::TYPE_FATAL
            ) {
                $response = new Response($com, false, $timeout);
            }
            return false;
        }
    }

    /**
     * Sets the charset(s) for this connection.
     *
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future requests and responses. When sending,
     * {@link Communicator::CHARSET_LOCAL} is converted to
     * {@link Communicator::CHARSET_REMOTE}, and when receiving,
     * {@link Communicator::CHARSET_REMOTE} is converted to
     * {@link Communicator::CHARSET_LOCAL}. Setting NULL to either charset will
     * disable charset convertion, and data will be both sent and received "as
     * is".
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, you can supply either a string to
     *     use for all charsets, or an array with the charset types as keys, and
     *     the charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the old values will be returned as
     *     an array with the types as keys, and charsets as values.
     *
     * @see Communicator::setDefaultCharset()
     */
    public function setCharset(
        $charset,
        $charsetType = Communicator::CHARSET_ALL
    ) {
        return $this->com->setCharset($charset, $charsetType);
    }

    /**
     * Gets the charset(s) for this connection.
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the current values will be
     *     returned as an array with the types as keys, and charsets as values.
     *
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return $this->com->getCharset($charsetType);
    }

    /**
     * Sends a request and waits for responses.
     *
     * @param Request       $request  The request to send.
     * @param callback|null $callback Optional. A function that is to be
     *     executed when new responses for this request are available.
     *     The callback takes two parameters. The {@link Response} object as
     *     the first, and the {@link Client} object as the second one. If the
     *     callback returns TRUE, the request is canceled. Note that the
     *     callback may be executed at least two times after that. Once with a
     *     {@link Response::TYPE_ERROR} response that notifies about the
     *     canceling, plus the {@link Response::TYPE_FINAL} response.
     *
     * @return $this The client object.
     *
     * @see completeRequest()
     * @see loop()
     * @see cancelRequest()
     */
    public function sendAsync(Request $request, $callback = null)
    {
        //Error checking
        $tag = $request->getTag();
        if ('' == $tag) {
            throw new DataFlowException(
                'Asynchonous commands must have a tag.',
                DataFlowException::CODE_TAG_REQUIRED
            );
        }
        if ($this->isRequestActive($tag)) {
            throw new DataFlowException(
                'There must not be multiple active requests sharing a tag.',
                DataFlowException::CODE_TAG_UNIQUE
            );
        }
        if (null !== $callback && !is_callable($callback, true)) {
            throw new UnexpectedValueException(
                'Invalid callback provided.',
                UnexpectedValueException::CODE_CALLBACK_INVALID
            );
        }

        $this->send($request);

        if (null === $callback) {
            //Register the request at the buffer
            $this->responseBuffer[$tag] = array();
        } else {
            //Prepare the callback
            $this->callbacks[$tag] = $callback;
        }
        return $this;
    }

    /**
     * Checks if a request is active.
     *
     * Checks if a request is active. A request is considered active if it's a
     * pending request and/or has responses that are not yet extracted.
     *
     * @param string $tag    The tag of the request to look for.
     * @param int    $filter One of the FILTER_* constants. Limits the search
     *     to the specified places.
     *
     * @return bool TRUE if the request is active, FALSE otherwise.
     *
     * @see getPendingRequestsCount()
     * @see completeRequest()
     */
    public function isRequestActive($tag, $filter = self::FILTER_ALL)
    {
        $result = 0;
        if ($filter & self::FILTER_CALLBACK) {
            $result |= (int) array_key_exists($tag, $this->callbacks);
        }
        if ($filter & self::FILTER_BUFFER) {
            $result |= (int) array_key_exists($tag, $this->responseBuffer);
        }
        return 0 !== $result;
    }

    /**
     * Sends a request and gets the full response.
     *
     * @param Request $request The request to send.
     *
     * @return ResponseCollection The received responses as a collection.
     *
     * @see sendAsync()
     * @see close()
     */
    public function sendSync(Request $request)
    {
        $tag = $request->getTag();
        if ('' == $tag) {
            $this->send($request);
        } else {
            $this->sendAsync($request);
        }
        return $this->completeRequest($tag);
    }

    /**
     * Completes a specified request.
     *
     * Starts an event loop for the RouterOS callbacks and finishes when a
     * specified request is completed.
     *
     * @param string|null $tag The tag of the request to complete.
     *     Setting NULL completes all requests.
     *
     * @return ResponseCollection A collection of {@link Response} objects that
     *     haven't been passed to a callback function or previously extracted
     *     with {@link static::extractNewResponses()}. Returns an empty
     *     collection when $tag is set to NULL (responses can still be
     *     extracted).
     */
    public function completeRequest($tag = null)
    {
        $hasNoTag = '' == $tag;
        $result = $hasNoTag ? array()
            : $this->extractNewResponses($tag)->toArray();
        while ((!$hasNoTag && $this->isRequestActive($tag))
        || ($hasNoTag && 0 !== $this->getPendingRequestsCount())
        ) {
            $newReply = $this->dispatchNextResponse(null);
            if ($newReply->getTag() === $tag) {
                if ($hasNoTag) {
                    $result[] = $newReply;
                }
                if ($newReply->getType() === Response::TYPE_FINAL) {
                    if (!$hasNoTag) {
                        $result = array_merge(
                            $result,
                            $this->isRequestActive($tag)
                            ? $this->extractNewResponses($tag)->toArray()
                            : array()
                        );
                    }
                    break;
                }
            }
        }
        return new ResponseCollection($result);
    }

    /**
     * Extracts responses for a request.
     *
     * Gets all new responses for a request that haven't been passed to a
     * callback and clears the buffer from them.
     *
     * @param string|null $tag The tag of the request to extract
     *     new responses for.
     *     Specifying NULL with extract new responses for all requests.
     *
     * @return ResponseCollection A collection of {@link Response} objects for
     *     the specified request.
     *
     * @see loop()
     */
    public function extractNewResponses($tag = null)
    {
        if (null === $tag) {
            $result = array();
            foreach (array_keys($this->responseBuffer) as $tag) {
                $result = array_merge(
                    $result,
                    $this->extractNewResponses($tag)->toArray()
                );
            }
            return new ResponseCollection($result);
        } elseif ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
            return new ResponseCollection(array());
        } elseif ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
            $result = $this->responseBuffer[$tag];
            if (!empty($result)) {
                if (end($result)->getType() === Response::TYPE_FINAL) {
                    unset($this->responseBuffer[$tag]);
                } else {
                    $this->responseBuffer[$tag] = array();
                }
            }
            return new ResponseCollection($result);
        } else {
            throw new DataFlowException(
                'No such request, or the request has already finished.',
                DataFlowException::CODE_UNKNOWN_REQUEST
            );
        }
    }

    /**
     * Starts an event loop for the RouterOS callbacks.
     *
     * Starts an event loop for the RouterOS callbacks and finishes when there
     * are no more pending requests or when a specified timeout has passed
     * (whichever comes first).
     *
     * @param int|null $sTimeout  Timeout for the loop.
     *     If NULL, there is no time limit.
     * @param int      $usTimeout Microseconds to add to the time limit.
     *
     * @return bool TRUE when there are any more pending requests, FALSE
     *     otherwise.
     *
     * @see extractNewResponses()
     * @see getPendingRequestsCount()
     */
    public function loop($sTimeout = null, $usTimeout = 0)
    {
        try {
            if (null === $sTimeout) {
                while ($this->getPendingRequestsCount() !== 0) {
                    $this->dispatchNextResponse(null);
                }
            } else {
                list($usStart, $sStart) = explode(' ', microtime());
                while ($this->getPendingRequestsCount() !== 0
                    && ($sTimeout >= 0 || $usTimeout >= 0)
                ) {
                    $this->dispatchNextResponse($sTimeout, $usTimeout);
                    list($usEnd, $sEnd) = explode(' ', microtime());

                    $sTimeout -= $sEnd - $sStart;
                    $usTimeout -= $usEnd - $usStart;
                    if ($usTimeout <= 0) {
                        if ($sTimeout > 0) {
                            $usTimeout = 1000000 + $usTimeout;
                            $sTimeout--;
                        }
                    }

                    $sStart = $sEnd;
                    $usStart = $usEnd;
                }
            }
        } catch (SocketException $e) {
            if ($e->getCode() !== SocketException::CODE_NO_DATA) {
                // @codeCoverageIgnoreStart
                // It's impossible to reliably cause any other SocketException.
                // This line is only here in case the unthinkable happens:
                // The connection terminates just after it was supposedly
                // about to send back some data.
                throw $e;
                // @codeCoverageIgnoreEnd
            }
        }
        return $this->getPendingRequestsCount() !== 0;
    }

    /**
     * Gets the number of pending requests.
     *
     * @return int The number of pending requests.
     *
     * @see isRequestActive()
     */
    public function getPendingRequestsCount()
    {
        return $this->pendingRequestsCount;
    }

    /**
     * Cancels a request.
     *
     * Cancels an active request. Using this function in favor of a plain call
     * to the "/cancel" command is highly recommended, as it also updates the
     * counter of pending requests properly. Note that canceling a request also
     * removes any responses for it that were not previously extracted with
     * {@link static::extractNewResponses()}.
     *
     * @param string|null $tag Tag of the request to cancel.
     *     Setting NULL will cancel all requests.
     *
     * @return $this The client object.
     *
     * @see sendAsync()
     * @see close()
     */
    public function cancelRequest($tag = null)
    {
        $cancelRequest = new Request('/cancel');
        $hasTag = !('' == $tag);
        $hasReg = null !== $this->registry;
        if ($hasReg && !$hasTag) {
            $tags = array_merge(
                array_keys($this->responseBuffer),
                array_keys($this->callbacks)
            );
            $this->registry->setTaglessMode(true);
            foreach ($tags as $t) {
                $cancelRequest->setArgument(
                    'tag',
                    $this->registry->getOwnershipTag() . $t
                );
                $this->sendSync($cancelRequest);
            }
            $this->registry->setTaglessMode(false);
        } else {
            if ($hasTag) {
                if ($this->isRequestActive($tag)) {
                    if ($hasReg) {
                        $this->registry->setTaglessMode(true);
                        $cancelRequest->setArgument(
                            'tag',
                            $this->registry->getOwnershipTag() . $tag
                        );
                    } else {
                        $cancelRequest->setArgument('tag', $tag);
                    }
                } else {
                    throw new DataFlowException(
                        'No such request. Canceling aborted.',
                        DataFlowException::CODE_CANCEL_FAIL
                    );
                }
            }
            $this->sendSync($cancelRequest);
            if ($hasReg) {
                $this->registry->setTaglessMode(false);
            }
        }

        if ($hasTag) {
            if ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
                $this->responseBuffer[$tag] = $this->completeRequest($tag);
            } else {
                $this->completeRequest($tag);
            }
        } else {
            $this->loop();
        }
        return $this;
    }

    /**
     * Sets response streaming setting.
     *
     * Sets whether future responses are streamed. If responses are streamed,
     * the argument values are returned as streams instead of strings. This is
     * particularly useful if you expect a response that may contain one or more
     * very large words.
     *
     * @param bool $streamingResponses Whether to stream future responses.
     *
     * @return bool The previous value of the setting.
     *
     * @see isStreamingResponses()
     */
    public function setStreamingResponses($streamingResponses)
    {
        $oldValue = $this->_streamingResponses;
        $this->_streamingResponses = (bool) $streamingResponses;
        return $oldValue;
    }

    /**
     * Gets response streaming setting.
     *
     * Gets whether future responses are streamed.
     *
     * @return bool The value of the setting.
     *
     * @see setStreamingResponses()
     */
    public function isStreamingResponses()
    {
        return $this->_streamingResponses;
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     *
     * Closes the opened connection, even if it is a persistent one. Note that
     * {@link static::extractNewResponses()} can still be used to extract
     * responses collected prior to the closing.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        $result = true;
        /*
         * The check below is done because for some unknown reason
         * (either a PHP or a RouterOS bug) calling "/quit" on an encrypted
         * connection makes one end hang.
         *
         * Since encrypted connections only appeared in RouterOS 6.1, and
         * the "/quit" call is needed for all <6.0 versions, problems due
         * to its absence should be limited to some earlier 6.* versions
         * on some RouterBOARD devices.
         */
        if ($this->com->getTransmitter()->getCrypto() === N::CRYPTO_OFF) {
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(true);
            }
            try {
                $response = $this->sendSync(new Request('/quit'));
                $result = $response[0]->getType() === Response::TYPE_FATAL;
            } catch (SocketException $e) {
                $result
                    = $e->getCode() === SocketException::CODE_REQUEST_SEND_FAIL;
            } catch (E $e) {
                //Ignore unknown errors.
            }
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(false);
            }
        }
        $result = $result && $this->com->close();
        $this->callbacks = array();
        $this->pendingRequestsCount = 0;
        return $result;
    }

    /**
     * Closes the connection, unless it's a persistent one.
     */
    public function __destruct()
    {
        if ($this->com->getTransmitter()->isPersistent()) {
            if (0 !== $this->pendingRequestsCount) {
                $this->cancelRequest();
            }
        } else {
            $this->close();
        }
    }

    /**
     * Sends a request to RouterOS.
     *
     * @param Request $request The request to send.
     *
     * @return $this The client object.
     *
     * @see sendSync()
     * @see sendAsync()
     */
    protected function send(Request $request)
    {
        $request->verify($this->com)->send($this->com, $this->registry);
        $this->pendingRequestsCount++;
        return $this;
    }

    /**
     * Dispatches the next response in queue.
     *
     * Dispatches the next response in queue, i.e. it executes the associated
     * callback if there is one, or places the response in the response buffer.
     *
     * @param int|null $sTimeout  If a response is not immediately available,
     *     wait this many seconds.
     *     If NULL, wait indefinitely.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     *
     * @throws SocketException When there's no response within the time limit.
     * @return Response The dispatched response.
     */
    protected function dispatchNextResponse($sTimeout = 0, $usTimeout = 0)
    {
        $response = new Response(
            $this->com,
            $this->_streamingResponses,
            $sTimeout,
            $usTimeout,
            $this->registry
        );
        if ($response->getType() === Response::TYPE_FATAL) {
            $this->pendingRequestsCount = 0;
            $this->com->close();
            return $response;
        }

        $tag = $response->getTag();
        $isLastForRequest = $response->getType() === Response::TYPE_FINAL;
        if ($isLastForRequest) {
            $this->pendingRequestsCount--;
        }

        if ('' != $tag) {
            if ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
                if ($this->callbacks[$tag]($response, $this)) {
                    try {
                        $this->cancelRequest($tag);
                    } catch (DataFlowException $e) {
                        if ($e->getCode() !== DataFlowException::CODE_UNKNOWN_REQUEST
                        ) {
                            throw $e;
                        }
                    }
                } elseif ($isLastForRequest) {
                    unset($this->callbacks[$tag]);
                }
            } else {
                $this->responseBuffer[$tag][] = $response;
            }
        }
        return $response;
    }
}


File: /src\Communicator.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Using transmitters.
 */
use BNjunge\Net\Transmitter as T;

/**
 * A RouterOS communicator.
 *
 * Implementation of the RouterOS API protocol. Unlike the other classes in this
 * package, this class doesn't provide any conveniences beyond the low level
 * implementation details (automatic word length encoding/decoding, charset
 * translation and data integrity), and because of that, its direct usage is
 * strongly discouraged.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 * @see      Client
 */
class Communicator
{
    /**
     * Used when getting/setting all (default) charsets.
     */
    const CHARSET_ALL = -1;

    /**
     * Used when getting/setting the (default) remote charset.
     *
     * The remote charset is the charset in which RouterOS stores its data.
     * If you want to keep compatibility with your Winbox, this charset should
     * match the default charset from your Windows' regional settings.
     */
    const CHARSET_REMOTE = 0;

    /**
     * Used when getting/setting the (default) local charset.
     *
     * The local charset is the charset in which the data from RouterOS will be
     * returned as. This charset should match the charset of the place the data
     * will eventually be written to.
     */
    const CHARSET_LOCAL = 1;

    /**
     * An array with the default charset.
     *
     * Charset types as keys, and the default charsets as values.
     *
     * @var array<string,string|null>
     */
    protected static $defaultCharsets = array(
        self::CHARSET_REMOTE => null,
        self::CHARSET_LOCAL  => null
    );

    /**
     * An array with the current charset.
     *
     * Charset types as keys, and the current charsets as values.
     *
     * @var array<string,string|null>
     */
    protected $charsets = array();

    /**
     * The transmitter for the connection.
     *
     * @var T\TcpClient
     */
    protected $trans;

    /**
     * Creates a new connection with the specified options.
     *
     * @param string        $host    Hostname (IP or domain) of RouterOS.
     * @param int|null      $port    The port on which the RouterOS host
     *     provides the API service. You can also specify NULL, in which case
     *     the port will automatically be chosen between 8728 and 8729,
     *     depending on the value of $crypto.
     * @param bool          $persist Whether or not the connection should be a
     *     persistent one.
     * @param double|null   $timeout The timeout for the connection.
     * @param string        $key     A string that uniquely identifies the
     *     connection.
     * @param string        $crypto  The encryption for this connection.
     *     Must be one of the BNjunge\Net\Transmitter\NetworkStream::CRYPTO_*
     *     constants. Off by default. RouterOS currently supports only TLS, but
     *     the setting is provided in this fashion for forward compatibility's
     *     sake. And for the sake of simplicity, if you specify an encryption,
     *     don't specify a context and your default context uses the value
     *     "DEFAULT" for ciphers, "ADH" will be automatically added to the list
     *     of ciphers.
     * @param resource|null $context A context for the socket.
     *
     * @see sendWord()
     */
    public function __construct(
        $host,
        $port = 8728,
        $persist = false,
        $timeout = null,
        $key = '',
        $crypto = T\NetworkStream::CRYPTO_OFF,
        $context = null
    ) {
        $isUnencrypted = T\NetworkStream::CRYPTO_OFF === $crypto;
        if (($context === null) && !$isUnencrypted) {
            $context = stream_context_get_default();
            $opts = stream_context_get_options($context);
            if (!isset($opts['ssl']['ciphers'])
                || 'DEFAULT' === $opts['ssl']['ciphers']
            ) {
                stream_context_set_option(
                    $context,
                    array(
                        'ssl' => array(
                            'ciphers' => 'ADH',
                            'verify_peer' => false,
                            'verify_peer_name' => false
                        )
                    )
                );
            }
        }
        // @codeCoverageIgnoreStart
        // The $port is customizable in testing.
        if (null === $port) {
            $port = $isUnencrypted ? 8728 : 8729;
        }
        // @codeCoverageIgnoreEnd

        try {
            $this->trans = new T\TcpClient(
                $host,
                $port,
                $persist,
                $timeout,
                $key,
                $crypto,
                $context
            );
        } catch (T\Exception $e) {
            throw new SocketException(
                'Error connecting to RouterOS',
                SocketException::CODE_CONNECTION_FAIL,
                $e
            );
        }
        $this->setCharset(
            self::getDefaultCharset(self::CHARSET_ALL),
            self::CHARSET_ALL
        );
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param string|null $string A string of the word to send, or NULL to get
     *     the next word as a string.
     *
     * @return int|string If a string is provided, returns the number of bytes
     *     sent, otherwise returns the next word as a string.
     */
    public function __invoke($string = null)
    {
        return null === $string ? $this->getNextWord()
            : $this->sendWord($string);
    }

    /**
     * Checks whether a variable is a seekable stream resource.
     *
     * @param mixed $var The value to check.
     *
     * @return bool TRUE if $var is a seekable stream, FALSE otherwise.
     */
    public static function isSeekableStream($var)
    {
        if (T\Stream::isStream($var)) {
            $meta = stream_get_meta_data($var);
            return $meta['seekable'];
        }
        return false;
    }

    /**
     * Uses iconv to convert a stream from one charset to another.
     *
     * @param string   $inCharset  The charset of the stream.
     * @param string   $outCharset The desired resulting charset.
     * @param resource $stream     The stream to convert. The stream is assumed
     *     to be seekable, and is read from its current position to its end,
     *     after which, it is seeked back to its starting position.
     *
     * @return resource A new stream that uses the $out_charset. The stream is a
     *     subset from the original stream, from its current position to its
     *     end, seeked at its start.
     */
    public static function iconvStream($inCharset, $outCharset, $stream)
    {
        $bytes = 0;
        $result = fopen('php://temp', 'r+b');
        $iconvFilter = stream_filter_append(
            $result,
            'convert.iconv.' . $inCharset . '.' . $outCharset,
            STREAM_FILTER_WRITE
        );

        flock($stream, LOCK_SH);
        $reader = new T\Stream($stream, false);
        $writer = new T\Stream($result, false);
        $chunkSize = $reader->getChunk(T\Stream::DIRECTION_RECEIVE);
        while ($reader->isAvailable() && $reader->isDataAwaiting()) {
            $bytes += $writer->send(fread($stream, $chunkSize));
        }
        fseek($stream, -$bytes, SEEK_CUR);
        flock($stream, LOCK_UN);

        stream_filter_remove($iconvFilter);
        rewind($result);
        return $result;
    }

    /**
     * Sets the default charset(s) for new connections.
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setCharset()
     */
    public static function setDefaultCharset(
        $charset,
        $charsetType = self::CHARSET_ALL
    ) {
        if (array_key_exists($charsetType, self::$defaultCharsets)) {
             $oldCharset = self::$defaultCharsets[$charsetType];
             self::$defaultCharsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = self::$defaultCharsets;
            self::$defaultCharsets = is_array($charset) ? $charset : array_fill(
                0,
                count(self::$defaultCharsets),
                $charset
            );
            return $oldCharsets;
        }
    }

    /**
     * Gets the default charset(s).
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setDefaultCharset()
     */
    public static function getDefaultCharset($charsetType)
    {
        return array_key_exists($charsetType, self::$defaultCharsets)
            ? self::$defaultCharsets[$charsetType] : self::$defaultCharsets;
    }

    /**
     * Gets the length of a seekable stream.
     *
     * Gets the length of a seekable stream.
     *
     * @param resource $stream The stream to check. The stream is assumed to be
     *     seekable.
     *
     * @return double The number of bytes in the stream between its current
     *     position and its end.
     */
    public static function seekableStreamLength($stream)
    {
        $streamPosition = (double) sprintf('%u', ftell($stream));
        fseek($stream, 0, SEEK_END);
        $streamLength = ((double) sprintf('%u', ftell($stream)))
            - $streamPosition;
        fseek($stream, $streamPosition, SEEK_SET);
        return $streamLength;
    }

    /**
     * Sets the charset(s) for this connection.
     *
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future words. When sending, {@link self::CHARSET_LOCAL} is
     * converted to {@link self::CHARSET_REMOTE}, and when receiving,
     * {@link self::CHARSET_REMOTE} is converted to {@link self::CHARSET_LOCAL}.
     * Setting  NULL to either charset will disable charset conversion, and data
     * will be both sent and received "as is".
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setDefaultCharset()
     */
    public function setCharset($charset, $charsetType = self::CHARSET_ALL)
    {
        if (array_key_exists($charsetType, $this->charsets)) {
             $oldCharset = $this->charsets[$charsetType];
             $this->charsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = $this->charsets;
            $this->charsets = is_array($charset) ? $charset : array_fill(
                0,
                count($this->charsets),
                $charset
            );
            return $oldCharsets;
        }
    }

    /**
     * Gets the charset(s) for this connection.
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see getDefaultCharset()
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return array_key_exists($charsetType, $this->charsets)
            ? $this->charsets[$charsetType] : $this->charsets;
    }

    /**
     * Gets the transmitter for this connection.
     *
     * @return T\TcpClient The transmitter for this connection.
     */
    public function getTransmitter()
    {
        return $this->trans;
    }

    /**
     * Sends a word.
     *
     * Sends a word and automatically encodes its length when doing so.
     *
     * @param string $word The word to send.
     *
     * @return int The number of bytes sent.
     *
     * @see sendWordFromStream()
     * @see getNextWord()
     */
    public function sendWord($word)
    {
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }
        $length = strlen($word);
        static::verifyLengthSupport($length);
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->trans->send(self::encodeLength($length) . $word);
            $this->trans->lock($old, true);
            return $bytes;
        }
        return $this->trans->send(self::encodeLength($length) . $word);
    }

    /**
     * Sends a word based on a stream.
     *
     * Sends a word based on a stream and automatically encodes its length when
     * doing so. The stream is read from its current position to its end, and
     * then returned to its current position. Because of those operations, the
     * supplied stream must be seekable.
     *
     * @param string   $prefix A string to prepend before the stream contents.
     * @param resource $stream The seekable stream to send.
     *
     * @return int The number of bytes sent.
     *
     * @see sendWord()
     */
    public function sendWordFromStream($prefix, $stream)
    {
        if (!self::isSeekableStream($stream)) {
            throw new InvalidArgumentException(
                'The stream must be seekable.',
                InvalidArgumentException::CODE_SEEKABLE_REQUIRED
            );
        }
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $prefix = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $prefix
            );
            $stream = self::iconvStream(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $stream
            );
        }

        flock($stream, LOCK_SH);
        $totalLength = strlen($prefix) + self::seekableStreamLength($stream);
        static::verifyLengthSupport($totalLength);

        $bytes = $this->trans->send(self::encodeLength($totalLength) . $prefix);
        $bytes += $this->trans->send($stream);

        flock($stream, LOCK_UN);
        return $bytes;
    }

    /**
     * Verifies that the length is supported.
     *
     * Verifies if the specified length is supported by the API. Throws a
     * {@link LengthException} if that's not the case. Currently, RouterOS
     * supports words up to 0xFFFFFFFF in length, so that's the only check
     * performed.
     *
     * @param int $length The length to verify.
     *
     * @return void
     */
    public static function verifyLengthSupport($length)
    {
        if ($length > 0xFFFFFFFF) {
            throw new LengthException(
                'Words with length above 0xFFFFFFFF are not supported.',
                LengthException::CODE_UNSUPPORTED,
                null,
                $length
            );
        }
    }

    /**
     * Encodes the length as required by the RouterOS API.
     *
     * @param int $length The length to encode.
     *
     * @return string The encoded length.
     */
    public static function encodeLength($length)
    {
        if ($length < 0) {
            throw new LengthException(
                'Length must not be negative.',
                LengthException::CODE_INVALID,
                null,
                $length
            );
        } elseif ($length < 0x80) {
            return chr($length);
        } elseif ($length < 0x4000) {
            return pack('n', $length |= 0x8000);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            return pack('n', $length >> 8) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            return pack('N', $length |= 0xE0000000);
        } elseif ($length <= 0xFFFFFFFF) {
            return chr(0xF0) . pack('N', $length);
        } elseif ($length <= 0x7FFFFFFFF) {
            $length = 'f' . base_convert($length, 10, 16);
            return chr(hexdec(substr($length, 0, 2))) .
                pack('N', hexdec(substr($length, 2)));
        }
        throw new LengthException(
            'Length must not be above 0x7FFFFFFFF.',
            LengthException::CODE_BEYOND_SHEME,
            null,
            $length
        );
    }

    /**
     * Get the next word in queue as a string.
     *
     * Get the next word in queue as a string, after automatically decoding its
     * length.
     *
     * @return string The word.
     *
     * @see close()
     */
    public function getNextWord()
    {
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
            $this->trans->lock($old, true);
        } else {
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
        }

        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $remoteCharset,
                $localCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }

        return $word;
    }

    /**
     * Get the next word in queue as a stream.
     *
     * Get the next word in queue as a stream, after automatically decoding its
     * length.
     *
     * @return resource The word, as a stream.
     *
     * @see close()
     */
    public function getNextWordAsStream()
    {
        $filters = new T\FilterCollection();
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $filters->append(
                'convert.iconv.' .
                $remoteCharset . '.' . $localCharset . '//IGNORE//TRANSLIT'
            );
        }

        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
            $this->trans->lock($old, true);
        } else {
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
        }

        return $stream;
    }

    /**
     * Decodes the length of the incoming message.
     *
     * Decodes the length of the incoming message, as specified by the RouterOS
     * API.
     *
     * @param T\Stream $trans The transmitter from which to decode the length of
     * the incoming message.
     *
     * @return int|double The decoded length.
     *     Is of type "double" only for values above "2 << 31".
     */
    public static function decodeLength(T\Stream $trans)
    {
        if ($trans->isPersistent() && $trans instanceof T\TcpClient) {
            $old = $trans->lock($trans::DIRECTION_RECEIVE);
            $length = self::_decodeLength($trans);
            $trans->lock($old, true);
            return $length;
        }
        return self::_decodeLength($trans);
    }

    /**
     * Decodes the length of the incoming message.
     *
     * Decodes the length of the incoming message, as specified by the RouterOS
     * API.
     *
     * Difference with the non private function is that this one doesn't perform
     * locking if the connection is a persistent one.
     *
     * @param T\Stream $trans The transmitter from which to decode the length of
     *     the incoming message.
     *
     * @return int|double The decoded length.
     *     Is of type "double" only for values above "2 << 31".
     */
    private static function _decodeLength(T\Stream $trans)
    {
        $byte = ord($trans->receive(1, 'initial length byte'));
        if ($byte & 0x80) {
            if (($byte & 0xC0) === 0x80) {
                return (($byte & 077) << 8 ) + ord($trans->receive(1));
            } elseif (($byte & 0xE0) === 0xC0) {
                $rem = unpack('n~', $trans->receive(2));
                return (($byte & 037) << 16 ) + $rem['~'];
            } elseif (($byte & 0xF0) === 0xE0) {
                $rem = unpack('n~/C~~', $trans->receive(3));
                return (($byte & 017) << 24 ) + ($rem['~'] << 8) + $rem['~~'];
            } elseif (($byte & 0xF8) === 0xF0) {
                $rem = unpack('N~', $trans->receive(4));
                return (($byte & 007) * 0x100000000/* '<< 32' or '2^32' */)
                    + (double) sprintf('%u', $rem['~']);
            }
            throw new NotSupportedException(
                'Unknown control byte encountered.',
                NotSupportedException::CODE_CONTROL_BYTE,
                null,
                $byte
            );
        } else {
            return $byte;
        }
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        return $this->trans->close();
    }
}


File: /src\Console\Color\Backgrounds.php
<?php

/**
 * Backgrounds class for BNjunge_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category  Console
 * @package   BNjunge_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0
 * @link      http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

/**
 * This class has the possibles values to a Background Color.
 *
 * @category  Console
 * @package   BNjunge_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://BNjunge.php.net/BNjunge_Console_Color
 */
abstract class Backgrounds
{
    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to specify that
     * the background color already in effect should be kept.
     */
    const KEEP    = null;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to black/grey (implmementation defined).
     */
    const BLACK   = 40;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to black/grey (implementation defined).
     */
    const GREY    = 40;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to maroon/red (implementation defined).
     */
    const MAROON  = 41;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to maroon/red (implementation defined).
     */
    const RED     = 41;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to green/lime (implementation defined).
     */
    const GREEN   = 42;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to green/lime (implementation defined).
     */
    const LIME    = 42;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to brown/yellow (implementation defined).
     */
    const BROWN   = 43;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to brown/yellow (implementation defined).
     */
    const YELLOW  = 43;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to navy/blue (implementation defined).
     */
    const NAVY    = 44;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to navy/blue (implementation defined).
     */
    const BLUE    = 44;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to purple/magenta (implementation defined).
     */
    const PURPLE  = 45;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to purple/magenta (implementation defined).
     */
    const MAGENTA = 45;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to teal/cyan (implementation defined).
     */
    const TEAL    = 46;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to teal/cyan (implementation defined).
     */
    const CYAN    = 46;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to silver/white (implementation defined).
     */
    const SILVER  = 47;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to silver/white (implementation defined).
     */
    const WHITE   = 47;

    /**
     * Used at {@link \BNjunge\Console\Color::setBackground()} to set the
     * background color to whatever the default one is.
     */
    const RESET   = 49;
}


File: /src\Console\Color\Exception.php
<?php

/**
 * Exception class for BNjunge_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

/**
 * Exception class for BNjunge_Console_Color.
 *
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
interface Exception
{
}


File: /src\Console\Color\Flags.php
<?php

/**
 * Flags class for BNjunge_Console_Color
 * Mappping the names of Font Style to your values.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

use ReflectionClass;

/**
 * This class has the possibles flags to a color setting.
 * 
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
abstract class Flags
{
    /**
     * Used at {@link \BNjunge\Console\Color::setFlags()} to specify that no
     * flags should be applied.
     */
    const NONE    = 0;

    /**
     * Used at {@link \BNjunge\Console\Color::setFlags()} as part of a bitmask.
     * If specified, resets all color and style information before applying
     * everything else.
     */
    const RESET   = 1;

    /**
     * Used at {@link \BNjunge\Console\Color::setFlags()} as part of a bitmask.
     * If specified, inverses the font and background colors, before letting
     * the remaining settings further modify things.
     * If specified together with {@link self::RESET}, takes effect AFTER the
     * reset.
     */
    const INVERSE = 2;

    /**
     * @var int[] Array with the flag as a key, and the corresponding code as a
     *     value.
     */
    protected static $flagCodes = array(
        self::RESET   => 0,
        self::INVERSE => 7
    );

    /**
     * Gets the codes for a flag set.
     * 
     * @param int $flags The flags to get the codes for.
     * 
     * @return int[] The codes for the flags specified, in ascending order,
     *     based on the flag constants' values.
     */
    final public static function getCodes($flags)
    {
        if (self::NONE === $flags) {
            return array();
        }

        $result = array();
        $flagsClass = new ReflectionClass(get_called_class());
        $validFlags = array_values(
            array_unique($flagsClass->getConstants(), SORT_NUMERIC)
        );
        foreach ($validFlags as $flag) {
            if ($flags & $flag) {
                $result[] = static::$flagCodes[$flag];
            }
        }
        return $result;
    }
}


File: /src\Console\Color\Fonts.php
<?php

/**
 * Font class for BNjunge_Console_Color
 * 
 * PHP version 5.3
 *
 * @category  Console
 * @package   BNjunge_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0
 * @link      http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

/**
 * This class has the possibles values to a Font Color.
 *
 * @category  Console
 * @package   BNjunge_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://BNjunge.php.net/BNjunge_Console_Color
 */
abstract class Fonts
{
    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to specify that
     * the font color already in effect should be kept.
     */
    const KEEP    = null;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to black/grey (implementation defined).
     */
    const BLACK   = 30;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to black/grey (implementation defined).
     */
    const GREY    = 30;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to maroon/red (implementation defined).
     */
    const MAROON  = 31;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to maroon/red (implementation defined).
     */
    const RED     = 31;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to green/lime (implementation defined).
     */
    const LIME    = 32;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to green/lime (implementation defined).
     */
    const GREEN   = 32;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to brown/yellow (implementation defined).
     */
    const BROWN   = 33;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to brown/yellow (implementation defined).
     */
    const YELLOW  = 33;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to navy/blue (implementation defined).
     */
    const NAVY    = 34;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to navy/blue (implementation defined).
     */
    const BLUE    = 34;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to purple/magenta (implementation defined).
     */
    const PURPLE  = 35;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to purple/magenta (implementation defined).
     */
    const MAGENTA = 35;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to teal/cyan (implementation defined).
     */
    const TEAL    = 36;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to teal/cyan (implementation defined).
     */
    const CYAN    = 36;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to silver/white (implementation defined).
     */
    const SILVER  = 37;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to silver/white (implementation defined).
     */
    const WHITE   = 37;

    /**
     * Used at {@link \BNjunge\Console\Color::setFont()} to set the
     * font color to whatever the default one is.
     */
    const RESET   = 39;
}


File: /src\Console\Color\Styles.php
<?php

/**
 * Styles class for BNjunge_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

use ReflectionClass;

/**
 * This class has the possibles values to a Font Style.
 * 
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
abstract class Styles
{
    /**
     * Used in {@link \BNjunge\Console\Color::setStyles()} to match all styles.
     */
    const ALL       = null;

    /**
     * Used in {@link \BNjunge\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the bold style.
     * When this style is enabled, the font is bolder.
     * With ANSICON, the font color becomes more intense (but not bolder).
     */
    const BOLD      = 1;

    /**
     * Used in {@link \BNjunge\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the underline style.
     * When this style is enabled, the font is underlined.
     * With ANSICON, the background color becomes more intense
     * (and the font is not underlined), same as {@link self::BLINK}.
     */
    const UNDERLINE = 2;

    /**
     * Used in {@link \BNjunge\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the blink style.
     * When this style is enabled, the font color switches between its regular
     * color and the background color at regular (implementation defined)
     * intervals, creating the illusion of a blinking text.
     * With ANSICON, the background color becomes more intense
     * (and the font is not blinking), same as with {@link self::UNDERLINE}.
     */
    const BLINK     = 4;

    /**
     * Used in {@link \BNjunge\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the concealed style.
     * When this style is enabled, the font color becomes the background color,
     * rendering the text invisible. This style is particularly useful for
     * implementations where simply setting the same color and background color
     * would not necesarily provide a fully invisibile text (e.g. ANSICON).
     */
    const CONCEALED = 8;

    /**
     * @var (int[])[] An array describing the codes for the styles.
     *     Each array key is the style's constant, and each value is an array
     *     where the first member is the disable code, and the second is the
     *     enable code.
     */
    protected static $styleCodes = array(
        self::BOLD      => array(22, 1),
        self::UNDERLINE => array(24, 4),
        self::BLINK     => array(25, 5),
        self::CONCEALED => array(28, 8)
    );

    /**
     * Get style constants.
     * 
     * @param int|null $styles Bitmask of styles to match.
     *     You can also use {@link self::ALL} (only) to get all styles.
     * 
     * @return int[] Matching style constants.
     */
    final public static function match($styles)
    {
        $flagsClass = new ReflectionClass(get_called_class());
        $validStyles = array_values(
            array_unique($flagsClass->getConstants(), SORT_NUMERIC)
        );
        unset($validStyles[array_search(self::ALL, $validStyles, true)]);

        if (self::ALL === $styles) {
            return $validStyles;
        }
        $styles = (int)$styles;

        $result = array();
        foreach ($validStyles as $flag) {
            if ($styles & $flag) {
                $result[] = $flag;
            }
        }
        return $result;
    }

    /**
     * Gets the code for a style.
     * 
     * @param int  $style The style to get the code for.
     * @param bool $state The state to get code for.
     *     TRUE for the enabled state codes,
     *     FALSE for the disabled state codes.
     * 
     * @return int The code for the flag specified.
     */
    final public static function getCode($style, $state)
    {
        return static::$styleCodes[$style][(int)(bool)$state];
    }
}


File: /src\Console\Color\UnexpectedValueException.php
<?php

/**
 * Exception class for BNjunge_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  BNjunge_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
namespace BNjunge\Console\Color;

use UnexpectedValueException as U;

/**
 * Exception class for BNjunge_Console_Color.
 *
 * @category  Console
 * @package   BNjunge_Console_Color
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://BNjunge.php.net/BNjunge_Console_Color
 */
class UnexpectedValueException extends U implements Exception
{
    /**
     * Used when an unexpected font value is supplied.
     */
    const CODE_FONT       = 1;

    /**
     * Used when an unexpected background value is supplied.
     */
    const CODE_BACKGROUND = 2;
}


File: /src\Console\Color.php
<?php

/**
 * Main class for Console_Color
 *
 * PHP version 5.3
 *
 * @category Console
 * @package  Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @author   Ivo Nascimento <ivo@o8o.com.br>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear.php.net/package/Console_Color
 */
namespace BNjunge\Console;

use BNjunge\Console\Color\Backgrounds;
use BNjunge\Console\Color\Flags;
use BNjunge\Console\Color\Fonts;
use BNjunge\Console\Color\Styles;
use BNjunge\Console\Color\UnexpectedValueException;
use ReflectionClass;

/**
 * Main class for Console_Color.
 *
 * @category Console
 * @package  Console_Color
 * @author   Ivo Nascimento <ivo@o8o.com.br>
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Console_Color
 */
class Color
{
    /**
     * @var array List of valid font colors.
     *     Filled by {@link fillValidators()}.
     */
    protected static $validFonts = array();

    /**
     * @var array List of valid background colors.
     *     Filled by {@link fillValidators()}.
     */
    protected static $validBackgorunds = array();

    /**
     * @var string Name of a class that is used to resolve flags to codes.
     */
    protected static $flagsResolver = '';

    /**
     * @var string Name of a class that is used to resolve styles to codes.
     */
    protected static $stylesResolver = '';

    /**
     * @var int Flags to set.
     */
    protected $flags = 0;

    /**
     * @var int|null The code for the currently specified font color.
     */
    protected $font = null;

    /**
     * @var int|null The code for the currently specified background color.
     */
    protected $backgorund = null;

    /**
     * @var bool[] Array with the status of each style.
     */
    protected $styles = array();

    /**
     * @var string|null The string to write to console to get the specified
     *     styling. NULL when the string needs to be regenerated.
     */
    protected $sequence = null;

    /**
     * Fills the list of valid fonts and backgrounds.
     * 
     * Classes extending this one that wish to add additional valid colors,
     * flags or styles should call this method in their own constructor BEFORE
     * calling the parent constructor.
     * 
     * @param string $fonts       Name of class, the constants of which are
     *     valid font colors.
     * @param string $backgrounds Name of class, the constants of which are
     *     valid background colors.
     * @param string $flags       Name of class that resolves flags to codes.
     *     Must inheirt from {@link Flags}. Constants of this
     *     class are considered the valid flags, and the coresponding codes must
     *     be overriden at the static $flagCodes property.
     * @param string $styles      Name of class that resolves styles to codes.
     *     Must inherit from {@link Styles}. Constants of this class are
     *     considered the valid styles, and the corresponding off/on codes must
     *     be overriden at the static $styleCodes property.
     * 
     * @return void
     */
    protected static function fillVlidators(
        $fonts,
        $backgrounds,
        $flags,
        $styles
    ) {
        if (empty(static::$validFonts)) {
            $fonts = new ReflectionClass($fonts);
            static::$validFonts = array_values(
                array_unique($fonts->getConstants(), SORT_REGULAR)
            );
        }

        if (empty(static::$validBackgorunds)) {
            $bgs = new ReflectionClass($backgrounds);
            static::$validBackgorunds = array_values(
                array_unique($bgs->getConstants(), SORT_REGULAR)
            );
        }

        if ('' === static::$flagsResolver) {
            $base = __CLASS__ . '\Flags';
            if ($base === $flags || is_subclass_of($flags, $base)) {
                static::$flagsResolver = $flags;
            }
        }

        if ('' === static::$stylesResolver) {
            $base = __CLASS__ . '\Styles';
            if ($base === $styles || is_subclass_of($styles, $base)) {
                static::$stylesResolver = $styles;
            }
        }
    }

    /**
     * Creates a new color.
     * 
     * Note that leaving all arguments with their default values (and not
     * applying styles) would result in a sequence that resets all settings to
     * the console's defaults.
     * 
     * @param int|null $font       Initial font color.
     * @param int|null $background Initial backgorund color.
     * @param int      $flags      Initial flags.
     * 
     * @see setFlags()
     * @see setStyles()
     * @see __toString()
     */
    public function __construct(
        $font = Fonts::KEEP,
        $background = Backgrounds::KEEP,
        $flags = Flags::NONE
    ) {
        static::fillVlidators(
            __CLASS__ . '\Fonts',
            __CLASS__ . '\Backgrounds',
            __CLASS__ . '\Flags',
            __CLASS__ . '\Styles'
        );
        $this->setFont($font);
        $this->setBackground($background);
        $this->setFlags($flags);
    }

    /**
     * Gets the font color.
     * 
     * @return int|null $color The font color.
     */
    public function getFont()
    {
        return $this->font;
    }

    /**
     * Sets the font color.
     * 
     * @param int|null $color The font color.
     * 
     * @return $this
     */
    public function setFont($color)
    {
        if (!in_array($color, static::$validFonts, true)) {
            throw new UnexpectedValueException(
                'Invalid font supplied.',
                UnexpectedValueException::CODE_FONT
            );
        }
        $this->font = $color;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets the background color.
     * 
     * @return int|null $color The background color.
     */
    public function getBackground()
    {
        return $this->backgorund;
    }

    /**
     * Sets the background color.
     * 
     * @param int|null $color The background color.
     * 
     * @return $this
     */
    public function setBackground($color)
    {
        if (!in_array($color, static::$validBackgorunds, true)) {
            throw new UnexpectedValueException(
                'Invalid background supplied.',
                UnexpectedValueException::CODE_BACKGROUND
            );
        }
        $this->backgorund = $color;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets the flags.
     * 
     * @return int The currently set flags.
     */
    public function getFlags()
    {
        return $this->flags;
    }

    /**
     * Sets the flags.
     * 
     * Sets the flags to apply in the sequence. Note that flags are applied
     * before all other settings, in ascending order of the constant values.
     * 
     * @param int $flags The new flags to set. Unknown flags will be ignored
     *     when forming the sequence, but will be visible with
     *     {@link getFlags()} non the less.
     * 
     * @return $this
     */
    public function setFlags($flags)
    {
        $this->flags = (int)$flags;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets styles.
     * 
     * @param int|null $style A single style to get the status of,
     *     or {@link Styles::ALL} to get all styles in an array.
     * 
     * @return bool|null|bool[] A single style status, or
     *     an array of status if $style is {@link Styles::ALL}.
     */
    public function getStyles($style = Styles::ALL)
    {
        if (Styles::ALL === $style) {
            return $this->styles;
        }
        return isset($this->styles[$style]) ? $this->styles[$style] : null;
    }

    /**
     * Sets styles.
     * 
     * Sets styles matched to a specified state.
     * 
     * @param int|null  $styles Bitmask of styles to set. You can also use the
     *     constant {@link Styles::ALL} (only) to set all known styles.
     *     Unknown styles will be ignored.
     * @param bool|null $state  The state to set the matched styles in.
     *     TRUE to enable them,
     *     FLASE to disable them,
     *     NULL to remove the setting for them (in effect using whatever the
     *     console had before the sequence was applied).
     * 
     * @return $this
     */
    public function setStyles($styles, $state)
    {
        $matchingStyles = call_user_func(
            array(static::$stylesResolver, 'match'),
            $styles
        );
        if (null === $state) {
            foreach ($matchingStyles as $style) {
                unset($this->styles[$style]);
            }
        } else {
            $state = (bool)$state;
            foreach ($matchingStyles as $style) {
                $this->styles[$style] = $state;
            }
            ksort($this->styles);
        }

        $this->sequence = null;
        return $this;
    }

    /**
     * Get the console escaping sequence.
     * 
     * This is a magic PHP method that will be called when you use the object in
     * a string context or otherwise explicitly cast it to a string.
     * 
     * It generates the escape sequence and returns it.
     * For the sake of performance, the escape sequence is cached, and is only
     * regenerated when a setter has been previously called.
     * 
     * @return string The string to write to console to get the specified
     *     styling.
     */
    public function __toString()
    {
        if (null === $this->sequence) {
            $seq = "\033[";

            $flags = implode(
                ';',
                call_user_func(
                    array(static::$flagsResolver, 'getCodes'),
                    $this->flags
                )
            );
            if ('' !== $flags) {
                $seq .= $flags . ';';
            }

            if (Fonts::KEEP !== $this->font) {
                $seq .= "{$this->font};";
            }
            if (Backgrounds::KEEP !== $this->backgorund) {
                $seq .= "{$this->backgorund};";
            }

            foreach ($this->styles as $style => $state) {
                $seq .= call_user_func(
                    array(static::$stylesResolver, 'getCode'),
                    $style,
                    $state
                ) . ';';
            }

            $this->sequence = rtrim($seq, ';') . 'm';
        }

        return $this->sequence;
    }
}


File: /src\Console\CommandLine\Action\Action_List.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   CVS: $Id: List.php,v 1.2 2009/02/27 08:03:17 izi Exp $
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;
use BNjunge\Console\CommandLine;

/**
 * Class that represent the List action, a special action that simply output an
 * array as a list.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Action_List extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * Possible parameters are:
     * - message: an alternative message to display instead of the default
     *   message,
     * - delimiter: an alternative delimiter instead of the comma,
     * - post: a string to append after the message (default is the new line
     *   char).
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $list = isset($params['list']) ? $params['list'] : array();
        $msg  = isset($params['message'])
            ? $params['message']
            : $this->parser->message_provider->get('LIST_DISPLAYED_MESSAGE');
        $del  = isset($params['delimiter']) ? $params['delimiter'] : ', ';
        $post = isset($params['post']) ? $params['post'] : "\n";
        $this->parser->outputter->stdout($msg . implode($del, $list) . $post);
        exit(0);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\Callback.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */
namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;


/**
 * Class that represent the Callback action.
 *
 * The result option array entry value is set to the return value of the
 * callback defined in the option.
 *
 * There are two steps to defining a callback option:
 *   - define the option itself using the callback action
 *   - write the callback; this is a function (or method) that takes five
 *     arguments, as described below.
 *
 * All callbacks are called as follows:
 * <code>
 * callable_func(
 *     $value,           // the value of the option
 *     $option_instance, // the option instance
 *     $result_instance, // the result instance
 *     $parser_instance, // the parser instance
 *     $params           // an array of params as specified in the option
 * );
 * </code>
 * and *must* return the option value.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Callback extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The value of the option
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(
            call_user_func(
                $this->option->callback,
                $value,
                $this->option,
                $this->result,
                $this->parser,
                $params
            )
        );
    }
    // }}}
}


File: /src\Console\CommandLine\Action\Counter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the Version action.
 *
 * The execute methode add 1 to the value of the result option array entry.
 * The value is incremented each time the option is found, for example
 * with an option defined like that:
 *
 * <code>
 * $parser->addOption(
 *     'verbose',
 *     array(
 *         'short_name' => '-v',
 *         'action'     => 'Counter'
 *     )
 * );
 * </code>
 * If the user type:
 * <code>
 * $ script.php -v -v -v
 * </code>
 * or:
 * <code>
 * $ script.php -vvv
 * </code>
 * the verbose variable will be set to to 3.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Counter extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if ($result === null) {
            $result = 0;
        }
        $this->setResult(++$result);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\Help.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the Help action, a special action that displays the
 * help message, telling the user how to use the program.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Help extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayUsage();
    }
    // }}}
}


File: /src\Console\CommandLine\Action\Password.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the Password action, a special action that allow the
 * user to specify the password on the commandline or to be prompted for
 * entering it.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Password extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(empty($value) ? $this->_promptPassword() : $value);
    }
    // }}}
    // _promptPassword() {{{

    /**
     * Prompts the password to the user without echoing it.
     *
     * @return string
     *
     * @todo not echo-ing the password does not work on windows is there a way
     *       to make this work ?
     */
    private function _promptPassword()
    {
        if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
            fwrite(
                STDOUT,
                $this->parser->message_provider->get('PASSWORD_PROMPT_ECHO')
            );
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
        } else {
            fwrite(STDOUT, $this->parser->message_provider->get('PASSWORD_PROMPT'));
            // disable echoing
            system('stty -echo');
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
            system('stty echo');
        }
        return trim($passwd);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\StoreArray.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreArray action.
 *
 * The execute method appends the value of the option entered by the user to
 * the result option array entry.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreArray extends CommandLine\Action
{
    // Protected properties {{{

    /**
     * Force a clean result when first called, overriding any defaults assigned.
     *
     * @var object $firstPass First time this action has been called.
     */
    protected $firstPass = true;

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if (null === $result || $this->firstPass) {
            $result          = array();
            $this->firstPass = false;
        }
        $result[] = $value;
        $this->setResult($result);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\StoreFalse.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreFalse action.
 *
 * The execute method store the boolean 'false' in the corrsponding result
 * option array entry (the value is true if the option is not present in the
 * command line entered by the user).
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFalse extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(false);
    }

    // }}}
}


File: /src\Console\CommandLine\Action\StoreFloat.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreFloat action.
 *
 * The execute method store the value of the option entered by the user as a
 * float in the result option array entry, if the value passed is not a float
 * an Exception is raised.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFloat extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws BNjunge\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'float',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((float)$value);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\StoreInt.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreInt action.
 *
 * The execute method store the value of the option entered by the user as an
 * integer in the result option array entry, if the value passed is not an
 * integer an Exception is raised.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreInt extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws BNjunge\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'int',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((int)$value);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\StoreString.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreString action.
 *
 * The execute method store the value of the option entered by the user as a
 * string in the result option array entry.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreString extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult((string)$value);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\StoreTrue.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the StoreTrue action.
 *
 * The execute method store the boolean 'true' in the corrsponding result
 * option array entry (the value is false if the option is not present in the
 * command line entered by the user).
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreTrue extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(true);
    }
    // }}}
}


File: /src\Console\CommandLine\Action\Version.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\Action;

use BNjunge\Console\CommandLine;

/**
 * Class that represent the Version action, a special action that displays the
 * version string of the program.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Version extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayVersion();
    }
    // }}}
}


File: /src\Console\CommandLine\Action.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */
namespace BNjunge\Console\CommandLine;

/**
 * Class that represent an option action.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Action
{
    // Properties {{{

    /**
     * A reference to the result instance.
     *
     * @var BNjunge\Console\CommandLine_Result $result The result instance
     */
    protected $result;

    /**
     * A reference to the option instance.
     *
     * @var BNjunge\Console\CommandLine_Option $option The action option
     */
    protected $option;

    /**
     * A reference to the parser instance.
     *
     * @var BNjunge\Console\CommandLine $parser The parser
     */
    protected $parser;

    // }}}
    // __construct() {{{

    /**
     * Constructor
     *
     * @param BNjunge\Console\CommandLine_Result $result The result instance
     * @param BNjunge\Console\CommandLine_Option $option The action option
     * @param BNjunge\Console\CommandLine        $parser The current parser
     *
     * @return void
     */
    public function __construct($result, $option, $parser)
    {
        $this->result = $result;
        $this->option = $option;
        $this->parser = $parser;
    }

    // }}}
    // getResult() {{{

    /**
     * Convenience method to retrieve the value of result->options[name].
     *
     * @return mixed The result value or null
     */
    public function getResult()
    {
        if (isset($this->result->options[$this->option->name])) {
            return $this->result->options[$this->option->name];
        }
        return null;
    }

    // }}}
    // format() {{{

    /**
     * Allow a value to be pre-formatted prior to being used in a choices test.
     * Setting $value to the new format will keep the formatting.
     *
     * @param mixed &$value The value to format
     *
     * @return mixed The formatted value
     */
    public function format(&$value)
    {
        return $value;
    }

    // }}}
    // setResult() {{{

    /**
     * Convenience method to assign the result->options[name] value.
     *
     * @param mixed $result The result value
     *
     * @return void
     */
    public function setResult($result)
    {
        $this->result->options[$this->option->name] = $result;
    }

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * All children actions must implement this method.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    abstract public function execute($value = false, $params = array());
    // }}}
}


File: /src\Console\CommandLine\Argument.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Class that represent a command line argument.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Argument extends Element
{
    // Public properties {{{

    /**
     * Setting this to true will tell the parser that the argument expects more
     * than one argument and that argument values should be stored in an array.
     *
     * @var boolean $multiple Whether the argument expects multiple values
     */
    public $multiple = false;

    /**
     * Setting this to true will tell the parser that the argument is optional
     * and can be ommited.
     * Note that it is not a good practice to make arguments optional, it is
     * the role of the options to be optional, by essence.
     *
     * @var boolean $optional Whether the argument is optional or not.
     */
    public $optional = false;

    // }}}
    // validate() {{{

    /**
     * Validates the argument instance.
     *
     * @return void
     * @throws BNjunge\Console\CommandLine\Exception
     *
     * @todo use exceptions
     */
    public function validate()
    {
        // check if the argument name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            \BNjunge\Console\CommandLine::triggerError(
                'argument_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!$this->optional && $this->default !== null) {
            \BNjunge\Console\CommandLine::triggerError(
                'argument_no_default',
                E_USER_ERROR
            );
        }
        parent::validate();
    }

    // }}}
}


File: /src\Console\CommandLine\Command.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Class that represent a command with option and arguments.
 *
 * This class exist just to clarify the interface but at the moment it is
 * strictly identical to BNjunge\Console\CommandLine class, it could change in the
 * future though.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Command extends \BNjunge\Console\CommandLine
{
    // Public properties {{{

    /**
     * An array of aliases for the subcommand.
     *
     * @var array $aliases Aliases for the subcommand.
     */
    public $aliases = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($params = array())
    {
        if (isset($params['aliases'])) {
            $this->aliases = $params['aliases'];
        }
        parent::__construct($params);
    }

    // }}}
}


File: /src\Console\CommandLine\CustomMessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   CVS: $Id: CustomMessageProvider.php 282427 2009-06-19 10:22:48Z izi $
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 1.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Common interfacefor message providers that allow overriding with custom
 * messages
 *
 * Message providers may optionally implement this interface.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Interface available since release 1.1.0
 */
interface CustomMessageProvider
{
    // getWithCustomMesssages() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     *
     * For a list of identifiers please see the provided default message
     * provider.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     *
     * @see BNjunge\Console\CommandLine_MessageProvider
     * @see BNjunge\Console\CommandLine_MessageProvider\DefaultProvider
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    );

    // }}}
}


File: /src\Console\CommandLine\Element.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Class that represent a command line element (an option, or an argument).
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Element
{
    // Public properties {{{

    /**
     * The element name.
     *
     * @var string $name Element name
     */
    public $name;

    /**
     * The name of variable displayed in the usage message, if no set it
     * defaults to the "name" property.
     *
     * @var string $help_name Element "help" variable name
     */
    public $help_name;

    /**
     * The element description.
     *
     * @var string $description Element description
     */
    public $description;
     /**
     * The default value of the element if not provided on the command line.
     *
     * @var mixed $default Default value of the option.
     */
    public $default;

    /**
     * Custom errors messages for this element
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see BNjunge\Console\CommandLine_MessageProvider\DefaultProvider
     */
    public $messages = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the element
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        $this->name = $name;
        foreach ($params as $attr => $value) {
            if (property_exists($this, $attr)) {
                $this->$attr = $value;
            }
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the element.
     *
     * @return string The string representation of the element
     *
     * @todo use __toString() instead
     */
    public function toString()
    {
        return $this->help_name;
    }
    // }}}
    // validate() {{{

    /**
     * Validates the element instance and set it's default values.
     *
     * @return void
     * @throws BNjunge\Console\CommandLine\Exception
     */
    public function validate()
    {
        // if no help_name passed, default to name
        if ($this->help_name == null) {
            $this->help_name = $this->name;
        }
    }

    // }}}
}


File: /src\Console\CommandLine\Exception.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

use Exception as E;

/**
 * Class for exceptions raised by the BNjunge\Console\CommandLine package.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Exception extends E
{
    // Codes constants {{{

    /**#@+
     * Exception code constants.
     */
    const OPTION_VALUE_REQUIRED   = 1;
    const OPTION_VALUE_UNEXPECTED = 2;
    const OPTION_VALUE_TYPE_ERROR = 3;
    const OPTION_UNKNOWN          = 4;
    const ARGUMENT_REQUIRED       = 5;
    const INVALID_SUBCOMMAND      = 6;
    /**#@-*/

    // }}}
    // factory() {{{

    /**
     * Convenience method that builds the exception with the array of params by
     * calling the message provider class.
     *
     * @param string                    $code     The string identifier of the
     *                                            exception.
     * @param array                     $params   Array of template vars/values
     * @param BNjunge\Console\CommandLine $parser   An instance of the parser
     * @param array                     $messages An optional array of messages
     *                                            passed to the message provider.
     *
     * @return BNjunge\Console\CommandLine\Exception The exception instance
     */
    public static function factory(
        $code, $params, $parser, array $messages = array()
    ) {
        $provider = $parser->message_provider;
        if ($provider instanceof CustomMessageProvider) {
            $msg = $provider->getWithCustomMessages(
                $code,
                $params,
                $messages
            );
        } else {
            $msg = $provider->get($code, $params);
        }
        $const = '\BNjunge\Console\CommandLine\Exception::' . $code;
        $code  = defined($const) ? constant($const) : 0;
        return new static($msg, $code);
    }

    // }}}
}


File: /src\Console\CommandLine\MessageProvider\DefaultProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine\MessageProvider;

use BNjunge\Console\CommandLine\MessageProvider;
use BNjunge\Console\CommandLine\CustomMessageProvider;

/**
 * Lightweight class that manages messages used by BNjunge\Console\CommandLine package,
 * allowing the developper to customize these messages, for example to
 * internationalize a command line frontend.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class DefaultProvider
    implements MessageProvider,
    CustomMessageProvider
{
    // Properties {{{

    /**
     * Associative array of messages
     *
     * @var array $messages
     */
    protected $messages = array(
        'OPTION_VALUE_REQUIRED'   => 'Option "{$name}" requires a value.',
        'OPTION_VALUE_UNEXPECTED' => 'Option "{$name}" does not expect a value (got "{$value}").',
        'OPTION_VALUE_NOT_VALID'  => 'Option "{$name}" must be one of the following: "{$choices}" (got "{$value}").',
        'OPTION_VALUE_TYPE_ERROR' => 'Option "{$name}" requires a value of type {$type} (got "{$value}").',
        'OPTION_AMBIGUOUS'        => 'Ambiguous option "{$name}", can be one of the following: {$matches}.',
        'OPTION_UNKNOWN'          => 'Unknown option "{$name}".',
        'ARGUMENT_REQUIRED'       => 'You must provide at least {$argnum} argument{$plural}.',
        'PROG_HELP_LINE'          => 'Type "{$progname} --help" to get help.',
        'PROG_VERSION_LINE'       => '{$progname} version {$version}.',
        'COMMAND_HELP_LINE'       => 'Type "{$progname} <command> --help" to get help on specific command.',
        'USAGE_WORD'              => 'Usage',
        'OPTION_WORD'             => 'Options',
        'ARGUMENT_WORD'           => 'Arguments',
        'COMMAND_WORD'            => 'Commands',
        'PASSWORD_PROMPT'         => 'Password: ',
        'PASSWORD_PROMPT_ECHO'    => 'Password (warning: will echo): ',
        'INVALID_CUSTOM_INSTANCE' => 'Instance does not implement the required interface',
        'LIST_OPTION_MESSAGE'     => 'lists valid choices for option {$name}',
        'LIST_DISPLAYED_MESSAGE'  => 'Valid choices are: ',
        'INVALID_SUBCOMMAND'      => 'Command "{$command}" is not valid.',
        'SUBCOMMAND_REQUIRED'     => 'Please enter one of the following command: {$commands}.',
    );

    // }}}
    // get() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     */
    public function get($code, $vars = array())
    {
        if (!isset($this->messages[$code])) {
            return 'UNKNOWN';
        }
        return $this->replaceTemplateVars($this->messages[$code], $vars);
    }

    // }}}
    // getWithCustomMessages() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    ) {
        // get message
        if (isset($messages[$code])) {
            $message = $messages[$code];
        } elseif (isset($this->messages[$code])) {
            $message = $this->messages[$code];
        } else {
            $message = 'UNKNOWN';
        }
        return $this->replaceTemplateVars($message, $vars);
    }

    // }}}
    // replaceTemplateVars() {{{

    /**
     * Replaces template vars in a message
     *
     * @param string $message The message
     * @param array  $vars    An array of template variables
     *
     * @return string
     */
    protected function replaceTemplateVars($message, $vars = array())
    {
        $tmpkeys = array_keys($vars);
        $keys    = array();
        foreach ($tmpkeys as $key) {
            $keys[] = '{$' . $key . '}';
        }
        return str_replace($keys, array_values($vars), $message);
    }

    // }}}
}


File: /src\Console\CommandLine\MessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Message providers common interface, all message providers must implement
 * this interface.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface MessageProvider
{
    // get() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     * For a list of identifiers please see the provided default message
     * provider.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     *
     * @see BNjunge\Console\CommandLine\MessageProvider\DefaultProvider
     */
    public function get($code, $vars=array());

    // }}}
}


File: /src\Console\CommandLine\Option.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

use BNjunge\Console;

/**
 * Class that represent a commandline option.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Option extends Element
{
    // Public properties {{{

    /**
     * The option short name (ex: -v).
     *
     * @var string $short_name Short name of the option
     */
    public $short_name;

    /**
     * The option long name (ex: --verbose).
     *
     * @var string $long_name Long name of the option
     */
    public $long_name;

    /**
     * The option action, defaults to "StoreString".
     *
     * @var string $action Option action
     */
    public $action = 'StoreString';

    /**
     * An array of possible values for the option. If this array is not empty
     * and the value passed is not in the array an exception is raised.
     * This only make sense for actions that accept values of course.
     *
     * @var array $choices Valid choices for the option
     */
    public $choices = array();

    /**
     * The callback function (or method) to call for an action of type
     * Callback, this can be any callable supported by the php function
     * call_user_func.
     *
     * Example:
     *
     * <code>
     * $parser->addOption('myoption', array(
     *     'short_name' => '-m',
     *     'long_name'  => '--myoption',
     *     'action'     => 'Callback',
     *     'callback'   => 'myCallbackFunction'
     * ));
     * </code>
     *
     * @var callable $callback The option callback
     */
    public $callback;

    /**
     * An associative array of additional params to pass to the class
     * corresponding to the action, this array will also be passed to the
     * callback defined for an action of type Callback, Example:
     *
     * <code>
     * // for a custom action
     * $parser->addOption('myoption', array(
     *     'short_name'    => '-m',
     *     'long_name'     => '--myoption',
     *     'action'        => 'MyCustomAction',
     *     'action_params' => array('foo'=>true, 'bar'=>false)
     * ));
     *
     * // if the user type:
     * // $ <yourprogram> -m spam
     * // in your MyCustomAction class the execute() method will be called
     * // with the value 'spam' as first parameter and
     * // array('foo'=>true, 'bar'=>false) as second parameter
     * </code>
     *
     * @var array $action_params Additional parameters to pass to the action
     */
    public $action_params = array();

    /**
     * For options that expect an argument, this property tells the parser if
     * the option argument is optional and can be ommited.
     *
     * @var bool $argumentOptional Whether the option arg is optional or not
     */
    public $argument_optional = false;

    /**
     * For options that uses the "choice" property only.
     * Adds a --list-<choice> option to the parser that displays the list of
     * choices for the option.
     *
     * @var bool $add_list_option Whether to add a list option or not
     */
    public $add_list_option = false;

    // }}}
    // Private properties {{{

    /**
     * When an action is called remember it to allow for multiple calls.
     *
     * @var object $action_instance Placeholder for action
     */
    private $_action_instance = null;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the option
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        parent::__construct($name, $params);
        if ($this->action == 'Password') {
            // special case for Password action, password can be passed to the
            // commandline or prompted by the parser
            $this->argument_optional = true;
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the option.
     *
     * @param string $delim Delimiter to use between short and long option
     *
     * @return string The string representation of the option
     * 
     * @todo use __toString() instead
     */
    public function toString($delim = ", ")
    {
        $ret     = '';
        $padding = '';
        if ($this->short_name != null) {
            $ret .= $this->short_name;
            if ($this->expectsArgument()) {
                $ret .= ' ' . $this->help_name;
            }
            $padding = $delim;
        }
        if ($this->long_name != null) {
            $ret .= $padding . $this->long_name;
            if ($this->expectsArgument()) {
                $ret .= '=' . $this->help_name;
            }
        }
        return $ret;
    }

    // }}}
    // expectsArgument() {{{

    /**
     * Returns true if the option requires one or more argument and false
     * otherwise.
     *
     * @return bool Whether the option expects an argument or not
     */
    public function expectsArgument()
    {
        if ($this->action == 'StoreTrue'
            || $this->action == 'StoreFalse'
            || $this->action == 'Help'
            || $this->action == 'Version'
            || $this->action == 'Counter'
            || $this->action == 'List'
        ) {
            return false;
        }
        return true;
    }

    // }}}
    // dispatchAction() {{{

    /**
     * Formats the value $value according to the action of the option and
     * updates the passed BNjunge\Console\CommandLine_Result object.
     *
     * @param mixed                            $value  The value to format
     * @param BNjunge\Console\CommandLine_Result $result The result instance
     * @param BNjunge\Console\CommandLine        $parser The parser instance
     *
     * @return void
     * @throws BNjunge\Console\CommandLine\Exception
     */
    public function dispatchAction($value, $result, $parser)
    {
        $actionInfo = Console\CommandLine::$actions[$this->action];
        $clsname    = $actionInfo[0];
        if ($this->_action_instance === null) {
            $this->_action_instance  = new $clsname($result, $this, $parser);
        }

        // check value is in option choices
        if (!empty($this->choices)
            && !in_array(
                $this->_action_instance->format($value),
                $this->choices
            )
        ) {
            throw Console\CommandLine\Exception::factory(
                'OPTION_VALUE_NOT_VALID',
                array(
                    'name'    => $this->name,
                    'choices' => implode('", "', $this->choices),
                    'value'   => $value,
                ),
                $parser,
                $this->messages
            );
        }
        $this->_action_instance->execute($value, $this->action_params);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the option instance.
     *
     * @return void
     * @throws BNjunge\Console\CommandLine\Exception
     * 
     * @todo use exceptions instead
     */
    public function validate()
    {
        // check if the option name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            Console\CommandLine::triggerError(
                'option_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // call the parent validate method
        parent::validate();
        // a short_name or a long_name must be provided
        if ($this->short_name == null && $this->long_name == null) {
            Console\CommandLine::triggerError(
                'option_long_and_short_name_missing',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // check if the option short_name is valid
        if ($this->short_name != null
            && !(preg_match('/^\-[a-zA-Z]{1}$/', $this->short_name))
        ) {
            Console\CommandLine::triggerError(
                'option_bad_short_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$short_name}' => $this->short_name
                )
            );
        }
        // check if the option long_name is valid
        if ($this->long_name != null
            && !preg_match('/^\-\-[a-zA-Z]+[a-zA-Z0-9_\-]*$/', $this->long_name)
        ) {
            Console\CommandLine::triggerError(
                'option_bad_long_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$long_name}' => $this->long_name
                )
            );
        }
        // check if we have a valid action
        if (!is_string($this->action)) {
            Console\CommandLine::triggerError(
                'option_bad_action',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!isset(Console\CommandLine::$actions[$this->action])) {
            Console\CommandLine::triggerError(
                'option_unregistered_action',
                E_USER_ERROR,
                array(
                    '{$action}' => $this->action,
                    '{$name}' => $this->name
                )
            );
        }
        // if the action is a callback, check that we have a valid callback
        if ($this->action == 'Callback' && !is_callable($this->callback)) {
            Console\CommandLine::triggerError(
                'option_invalid_callback',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
    }

    // }}}
    // setDefaults() {{{

    /**
     * Set the default value according to the configured action.
     *
     * Note that for backward compatibility issues this method is only called
     * when the 'force_options_defaults' is set to true, it will become the
     * default behaviour in the next major release of BNjunge\Console\CommandLine.
     *
     * @return void
     */
    public function setDefaults()
    {
        if ($this->default !== null) {
            // already set
            return;
        }
        switch ($this->action) {
        case 'Counter':
        case 'StoreInt':
            $this->default = 0;
            break;
        case 'StoreFloat':
            $this->default = 0.0;
            break;
        case 'StoreArray':
            $this->default = array();
            break;
        case 'StoreTrue':
            $this->default = false;
            break;
        case 'StoreFalse':
            $this->default = true;
            break;
        default:
            return;
        }
    }

    // }}}
}


File: /src\Console\CommandLine\Outputter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Outputters common interface, all outputters must implement this interface.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Outputter
{
    // stdout() {{{

    /**
     * Processes the output for a message that should be displayed on STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg);

    // }}}
    // stderr() {{{

    /**
     * Processes the output for a message that should be displayed on STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg);

    // }}}
}


File: /src\Console\CommandLine\Outputter_Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * BNjunge\Console\CommandLine default Outputter.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Outputter_Default implements Outputter
{
    // stdout() {{{

    /**
     * Writes the message $msg to STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg)
    {
        if (defined('STDOUT')) {
            fwrite(STDOUT, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
    // stderr() {{{

    /**
     * Writes the message $msg to STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg)
    {
        if (defined('STDERR')) {
            fwrite(STDERR, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
}


File: /src\Console\CommandLine\Renderer.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * Renderers common interface, all renderers must implement this interface.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Renderer
{
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage();

    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error);

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version();

    // }}}
}


File: /src\Console\CommandLine\Renderer_Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 */

namespace BNjunge\Console\CommandLine;

/**
 * BNjunge\Console\CommandLine default renderer.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Renderer_Default implements Renderer
{
    // Properties {{{

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $line_width = 75;

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $options_on_different_lines = false;

    /**
     * An instance of BNjunge\Console\CommandLine.
     *
     * @var BNjunge\Console\CommandLine $parser The parser
     */
    public $parser = false;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param object $parser A BNjunge\Console\CommandLine instance
     *
     * @return void
     */
    public function __construct($parser = false)
    {
        $this->parser = $parser;
    }

    // }}}
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage()
    {
        $ret = '';
        if (!empty($this->parser->description)) {
            $ret .= $this->description() . "\n\n";
        }
        $ret .= $this->usageLine() . "\n";
        if (count($this->parser->commands) > 0) {
            $ret .= $this->commandUsageLine() . "\n";
        }
        if (count($this->parser->options) > 0) {
            $ret .= "\n" . $this->optionList() . "\n";
        }
        if (count($this->parser->args) > 0) {
            $ret .= "\n" . $this->argumentList() . "\n";
        }
        if (count($this->parser->commands) > 0) {
            $ret .= "\n" . $this->commandList() . "\n";
        }
        $ret .= "\n";
        return $ret;
    }
    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error)
    {
        $ret = 'Error: ' . $error . "\n";
        if ($this->parser->add_help_option) {
            $name = $this->name();
            $ret .= $this->wrap(
                $this->parser->message_provider->get(
                    'PROG_HELP_LINE',
                    array('progname' => $name)
                )
            ) . "\n";
            if (count($this->parser->commands) > 0) {
                $ret .= $this->wrap(
                    $this->parser->message_provider->get(
                        'COMMAND_HELP_LINE',
                        array('progname' => $name)
                    )
                ) . "\n";
            }
        }
        return $ret;
    }

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version()
    {
        return $this->parser->message_provider->get(
            'PROG_VERSION_LINE',
            array(
                'progname' => $this->name(),
                'version'  => $this->parser->version
            )
        ) . "\n";
    }

    // }}}
    // name() {{{

    /**
     * Returns the full name of the program or the sub command
     *
     * @return string The name of the program
     */
    protected function name()
    {
        $name   = $this->parser->name;
        $parent = $this->parser->parent;
        while ($parent) {
            if (count($parent->options) > 0) {
                $name = '['
                    . strtolower(
                        $this->parser->message_provider->get(
                            'OPTION_WORD',
                            array('plural' => 's')
                        )
                    ) . '] ' . $name;
            }
            $name = $parent->name . ' ' . $name;
            $parent = $parent->parent;
        }
        return $this->wrap($name);
    }

    // }}}
    // description() {{{

    /**
     * Returns the command line description message.
     *
     * @return string The description message
     */
    protected function description()
    {
        return $this->wrap($this->parser->description);
    }

    // }}}
    // usageLine() {{{

    /**
     * Returns the command line usage message
     *
     * @return string the usage message
     */
    protected function usageLine()
    {
        $usage = $this->parser->message_provider->get('USAGE_WORD') . ":\n";
        $ret   = $usage . '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        if (count($this->parser->args) > 0) {
            foreach ($this->parser->args as $name=>$arg) {
                $arg_str = $arg->help_name;
                if ($arg->multiple) {
                    $arg_str .= '1 ' . $arg->help_name . '2 ...';
                }
                if ($arg->optional) {
                    $arg_str = '[' . $arg_str . ']';
                }
                $ret .= ' ' . $arg_str;
            }
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // commandUsageLine() {{{

    /**
     * Returns the command line usage message for subcommands.
     *
     * @return string The usage line
     */
    protected function commandUsageLine()
    {
        if (count($this->parser->commands) == 0) {
            return '';
        }
        $ret = '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        $ret       .= " <command>";
        $hasArgs    = false;
        $hasOptions = false;
        foreach ($this->parser->commands as $command) {
            if (!$hasArgs && count($command->args) > 0) {
                $hasArgs = true;
            }
            if (!$hasOptions && ($command->add_help_option
                || $command->add_version_option
                || count($command->options) > 0)
            ) {
                $hasOptions = true;
            }
        }
        if ($hasOptions) {
            $ret .= ' [options]';
        }
        if ($hasArgs) {
            $ret .= ' [args]';
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // argumentList() {{{

    /**
     * Render the arguments list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted argument list
     */
    protected function argumentList()
    {
        $col  = 0;
        $args = array();
        foreach ($this->parser->args as $arg) {
            $argstr = '  ' . $arg->toString();
            $args[] = array($argstr, $arg->description);
            $ln     = strlen($argstr);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('ARGUMENT_WORD') . ":";
        foreach ($args as $arg) {
            $text = str_pad($arg[0], $col) . '  ' . $arg[1];
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // optionList() {{{

    /**
     * Render the options list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted option list
     */
    protected function optionList()
    {
        $col     = 0;
        $options = array();
        foreach ($this->parser->options as $option) {
            $delim    = $this->options_on_different_lines ? "\n" : ', ';
            $optstr   = $option->toString($delim);
            $lines    = explode("\n", $optstr);
            $lines[0] = '  ' . $lines[0];
            if (count($lines) > 1) {
                $lines[1] = '  ' . $lines[1];
                $ln       = strlen($lines[1]);
            } else {
                $ln = strlen($lines[0]);
            }
            $options[] = array($lines, $option->description);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('OPTION_WORD') . ":";
        foreach ($options as $option) {
            if (count($option[0]) > 1) {
                $text = str_pad($option[0][1], $col) . '  ' . $option[1];
                $pre  = $option[0][0] . "\n";
            } else {
                $text = str_pad($option[0][0], $col) . '  ' . $option[1];
                $pre  = '';
            }
            $ret .= "\n" . $pre . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // commandList() {{{

    /**
     * Render the command list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted subcommand list
     */
    protected function commandList()
    {

        $commands = array();
        $col      = 0;
        foreach ($this->parser->commands as $cmdname=>$command) {
            $cmdname    = '  ' . $cmdname;
            $commands[] = array($cmdname, $command->description, $command->aliases);
            $ln         = strlen($cmdname);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('COMMAND_WORD') . ":";
        foreach ($commands as $command) {
            $text = str_pad($command[0], $col) . '  ' . $command[1];
            if ($aliasesCount = count($command[2])) {
                $pad = '';
                $text .= ' (';
                $text .= $aliasesCount > 1 ? 'aliases: ' : 'alias: ';
                foreach ($command[2] as $alias) {
                    $text .= $pad . $alias;
                    $pad   = ', ';
                }
                $text .= ')';
            }
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // wrap() {{{

    /**
     * Wraps the text passed to the method.
     *
     * @param string $text The text to wrap
     * @param int    $lw   The column width (defaults to line_width property)
     *
     * @return string The wrapped text
     */
    protected function wrap($text, $lw=null)
    {
        if ($this->line_width > 0) {
            if ($lw === null) {
                $lw = $this->line_width;
            }
            return wordwrap($text, $lw, "\n", false);
        }
        return $text;
    }

    // }}}
    // columnWrap() {{{

    /**
     * Wraps the text passed to the method at the specified width.
     *
     * @param string $text The text to wrap
     * @param int    $cw   The wrap width
     *
     * @return string The wrapped text
     */
    protected function columnWrap($text, $cw)
    {
        $tokens = explode("\n", $this->wrap($text));
        $ret    = $tokens[0];
        $text   = trim(substr($text, strlen($ret)));
        if (empty($text)) {
            return $ret;
        }

        $chunks = $this->wrap($text, $this->line_width - $cw);
        $tokens = explode("\n", $chunks);
        foreach ($tokens as $token) {
            if (!empty($token)) {
                $ret .= "\n" . str_repeat(' ', $cw) . $token;
            } else {
                $ret .= "\n";
            }
        }
        return $ret;
    }

    // }}}
}


File: /src\Console\CommandLine\Result.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

/**
 * A lightweight class to store the result of the command line parsing.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Result
{
    // Public properties {{{

    /**
     * The result options associative array.
     * Key is the name of the option and value its value.
     *
     * @var array $options Result options array
     */
    public $options = array();

    /**
     * The result arguments array.
     *
     * @var array $args Result arguments array
     */
    public $args = array();

    /**
     * Name of the command invoked by the user, false if no command invoked.
     *
     * @var string $command_name Result command name
     */
    public $command_name = false;

    /**
     * A result instance for the subcommand.
     *
     * @var static $command Result instance for the subcommand
     */
    public $command = false;

    // }}}
}


File: /src\Console\CommandLine\XmlParser.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.3
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace BNjunge\Console\CommandLine;

use BNjunge\Console\CommandLine;
use DOMDocument;
use DOMNode;
use Phar;

/**
 * Parser for command line xml definitions.
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class XmlParser
{
    // parse() {{{

    /**
     * Parses the given xml definition file and returns a
     * BNjunge\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlfile The xml file to parse
     *
     * @return BNjunge\Console\CommandLine A parser instance
     */
    public static function parse($xmlfile)
    {
        if (!is_readable($xmlfile)) {
            CommandLine::triggerError(
                'invalid_xml_file',
                E_USER_ERROR,
                array('{$file}' => $xmlfile)
            );
        }
        $doc = new DOMDocument();
        $doc->load($xmlfile);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // parseString() {{{

    /**
     * Parses the given xml definition string and returns a
     * BNjunge\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlstr The xml string to parse
     *
     * @return BNjunge\Console\CommandLine A parser instance
     */
    public static function parseString($xmlstr)
    {
        $doc = new DOMDocument();
        $doc->loadXml($xmlstr);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the xml definition using Relax NG.
     *
     * @param DOMDocument $doc The document to validate
     *
     * @return boolean Whether the xml data is valid or not.
     * @throws BNjunge\Console\CommandLine\Exception
     *
     * @todo use exceptions only
     */
    public static function validate(DOMDocument $doc)
    {
        $paths = array();
        if (!class_exists('Phar', false) || !Phar::running()) {
            // Pyrus
            $paths[]
                = 'D:\Vasko\WEB\PHP\_shared\BNjunge\data/BNjunge.php.net/BNjunge_Console_CommandLine/xmlschema.rng';
            // PEAR
            $pearDataDirEnv = getenv('PHP_PEAR_DATA_DIR');
            if ($pearDataDirEnv) {
                $paths[] = $pearDataDirEnv .
                    '/BNjunge_Console_CommandLine/xmlschema.rng';
            }
            $paths[] = 'D:\Vasko\WEB\PHP\_shared\BNjunge\data/BNjunge_Console_CommandLine/xmlschema.rng';
        }
        $pkgData  = __DIR__ . '/../../../../data/';
        // PHAR dep
        $paths[] = $pkgData .
            'BNjunge.php.net/BNjunge_Console_CommandLine/xmlschema.rng';
        $paths[] = $pkgData . 'BNjunge_Console_CommandLine/xmlschema.rng';
        $paths[] = $pkgData . 'BNjunge/console_commandline/xmlschema.rng';
        // Git/Composer
        $paths[] = $pkgData . 'xmlschema.rng';
        $paths[] = 'xmlschema.rng';

        foreach ($paths as $path) {
            if (is_readable($path)) {
                return $doc->relaxNGValidate($path);
            }
        }
        CommandLine::triggerError(
            'invalid_xml_file',
            E_USER_ERROR,
            array('{$file}' => $path)
        );
    }

    // }}}
    // _parseCommandNode() {{{

    /**
     * Parses the root command node or a command node and returns the
     * constructed BNjunge\Console\CommandLine or BNjunge\Console\CommandLine_Command
     * instance.
     *
     * @param DOMNode $node       The node to parse
     * @param bool    $isRootNode Whether it is a root node or not
     *
     * @return CommandLine|CommandLine\Command An instance of CommandLine for
     *     root node, CommandLine\Command otherwise.
     */
    private static function _parseCommandNode(DOMNode $node, $isRootNode = false)
    {
        if ($isRootNode) {
            $obj = new CommandLine();
        } else {
            $obj = new CommandLine\Command();
        }
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'name':
            case 'description':
            case 'version':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'add_help_option':
            case 'add_version_option':
            case 'force_posix':
                $obj->$cNodeName = self::_bool(trim($cNode->nodeValue));
                break;
            case 'option':
                $obj->addOption(self::_parseOptionNode($cNode));
                break;
            case 'argument':
                $obj->addArgument(self::_parseArgumentNode($cNode));
                break;
            case 'command':
                $obj->addCommand(self::_parseCommandNode($cNode));
                break;
            case 'aliases':
                if (!$isRootNode) {
                    foreach ($cNode->childNodes as $subChildNode) {
                        if ($subChildNode->nodeName == 'alias') {
                            $obj->aliases[] = trim($subChildNode->nodeValue);
                        }
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _parseOptionNode() {{{

    /**
     * Parses an option node and returns the constructed
     * BNjunge\Console\CommandLine_Option instance.
     *
     * @param DOMNode $node The node to parse
     *
     * @return BNjunge\Console\CommandLine\Option The built option
     */
    private static function _parseOptionNode(DOMNode $node)
    {
        $obj = new CommandLine\Option($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'choices':
                foreach ($cNode->childNodes as $subChildNode) {
                    if ($subChildNode->nodeName == 'choice') {
                        $obj->choices[] = trim($subChildNode->nodeValue);
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                if (property_exists($obj, $cNodeName)) {
                    $obj->$cNodeName = trim($cNode->nodeValue);
                }
                break;
            }
        }
        if ($obj->action == 'Password') {
            $obj->argument_optional = true;
        }
        return $obj;
    }

    // }}}
    // _parseArgumentNode() {{{

    /**
     * Parses an argument node and returns the constructed
     * BNjunge\Console\CommandLine_Argument instance.
     *
     * @param DOMNode $node The node to parse
     *
     * @return BNjunge\Console\CommandLine\Argument The built argument
     */
    private static function _parseArgumentNode(DOMNode $node)
    {
        $obj = new CommandLine\Argument($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'description':
            case 'help_name':
            case 'default':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'multiple':
                $obj->multiple = self::_bool(trim($cNode->nodeValue));
                break;
            case 'optional':
                $obj->optional = self::_bool(trim($cNode->nodeValue));
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _bool() {{{

    /**
     * Returns a boolean according to true/false possible strings.
     *
     * @param string $str The string to process
     *
     * @return boolean
     */
    private static function _bool($str)
    {
        return in_array((string)$str, array('true', '1', 'on', 'yes'));
    }

    // }}}
    // _messages() {{{

    /**
     * Returns an array of custom messages for the element
     *
     * @param DOMNode $node The messages node to process
     *
     * @return array an array of messages
     *
     * @see BNjunge\Console\CommandLine::$messages
     * @see BNjunge\Console\CommandLine_Element::$messages
     */
    private static function _messages(DOMNode $node)
    {
        $messages = array();

        foreach ($node->childNodes as $cNode) {
            if ($cNode->nodeType == XML_ELEMENT_NODE) {
                $name  = $cNode->getAttribute('name');
                $value = trim($cNode->nodeValue);

                $messages[$name] = $value;
            }
        }

        return $messages;
    }

    // }}}
}


File: /src\Console\CommandLine.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the BNjunge\Console\CommandLine package.
 *
 * A full featured package for managing command-line options and arguments
 * hightly inspired from python optparse module, it allows the developper to
 * easily build complex command line interfaces.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
namespace BNjunge\Console;

/**
 * Main class for parsing command line options and arguments.
 *
 * There are three ways to create parsers with this class:
 * <code>
 * // direct usage
 * $parser = new BNjunge\Console\CommandLine();
 *
 * // with an xml definition file
 * $parser = BNjunge\Console\CommandLine::fromXmlFile('path/to/file.xml');
 *
 * // with an xml definition string
 * $validXmlString = '..your xml string...';
 * $parser = BNjunge\Console\CommandLine::fromXmlString($validXmlString);
 * </code>
 *
 * @category  Console
 * @package   BNjunge\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://BNjunge.php.net/BNjunge_Console_CommandLine
 * @since     File available since release 0.1.0
 * @example   docs/examples/ex1.php
 * @example   docs/examples/ex2.php
 */
class CommandLine
{
    // Public properties {{{

    /**
     * Error messages.
     *
     * @var array $errors Error messages
     *
     * @todo move this to BNjunge\Console\CommandLine\MessageProvider
     */
    public static $errors = array(
        'option_bad_name'                    => 'option name must be a valid php variable name (got: {$name})',
        'argument_bad_name'                  => 'argument name must be a valid php variable name (got: {$name})',
        'argument_no_default'                => 'only optional arguments can have a default value',
        'option_long_and_short_name_missing' => 'you must provide at least an option short name or long name for option "{$name}"',
        'option_bad_short_name'              => 'option "{$name}" short name must be a dash followed by a letter (got: "{$short_name}")',
        'option_bad_long_name'               => 'option "{$name}" long name must be 2 dashes followed by a word (got: "{$long_name}")',
        'option_unregistered_action'         => 'unregistered action "{$action}" for option "{$name}".',
        'option_bad_action'                  => 'invalid action for option "{$name}".',
        'option_invalid_callback'            => 'you must provide a valid callback for option "{$name}"',
        'action_class_does_not_exists'       => 'action "{$name}" class "{$class}" not found, make sure that your class is available before calling BNjunge\Console\CommandLine::registerAction()',
        'invalid_xml_file'                   => 'XML definition file "{$file}" does not exists or is not readable',
        'invalid_rng_file'                   => 'RNG file "{$file}" does not exists or is not readable'
    );

    /**
     * The name of the program, if not given it defaults to argv[0].
     *
     * @var string $name Name of your program
     */
    public $name;

    /**
     * A description text that will be displayed in the help message.
     *
     * @var string $description Description of your program
     */
    public $description = '';

    /**
     * A string that represents the version of the program, if this property is
     * not empty and property add_version_option is not set to false, the
     * command line parser will add a --version option, that will display the
     * property content.
     *
     * @var    string $version
     * @access public
     */
    public $version = '';

    /**
     * Boolean that determine if the command line parser should add the help
     * (-h, --help) option automatically.
     *
     * @var bool $add_help_option Whether to add a help option or not
     */
    public $add_help_option = true;

    /**
     * Boolean that determine if the command line parser should add the version
     * (-v, --version) option automatically.
     * Note that the version option is also generated only if the version
     * property is not empty, it's up to you to provide a version string of
     * course.
     *
     * @var bool $add_version_option Whether to add a version option or not
     */
    public $add_version_option = true;

    /**
     * Boolean that determine if providing a subcommand is mandatory.
     *
     * @var bool $subcommand_required Whether a subcommand is required or not
     */
    public $subcommand_required = false;

    /**
     * The command line parser renderer instance.
     *
     * @var BNjunge\Console\CommandLine\Renderer a renderer
     */
    public $renderer = false;

    /**
     * The command line parser outputter instance.
     *
     * @var BNjunge\Console\CommandLine\Outputter An outputter
     */
    public $outputter = false;

    /**
     * The command line message provider instance.
     *
     * @var BNjunge\Console\CommandLine\MessageProvider A message provider
     */
    public $message_provider = false;

    /**
     * Boolean that tells the parser to be POSIX compliant, POSIX demands the
     * following behavior: the first non-option stops option processing.
     *
     * @var bool $force_posix Whether to force posix compliance or not
     */
    public $force_posix = false;

    /**
     * Boolean that tells the parser to set relevant options default values,
     * according to the option action.
     *
     * @see BNjunge\Console\CommandLine\Option::setDefaults()
     * @var bool $force_options_defaults Whether to force option default values
     */
    public $force_options_defaults = false;

    /**
     * An array of BNjunge\Console\CommandLine\Option objects.
     *
     * @var array $options The options array
     */
    public $options = array();

    /**
     * An array of BNjunge\Console\CommandLine\Argument objects.
     *
     * @var array $args The arguments array
     */
    public $args = array();

    /**
     * An array of BNjunge\Console\CommandLine\Command objects (sub commands).
     *
     * @var array $commands The commands array
     */
    public $commands = array();

    /**
     * Parent, only relevant in Command objects but left here for interface
     * convenience.
     *
     * @var BNjunge\Console\CommandLine The parent instance
     * 
     * @todo move CommandLine::parent to CommandLine\Command
     */
    public $parent = false;

    /**
     * Array of valid actions for an option, this array will also store user
     * registered actions.
     *
     * The array format is:
     * <pre>
     * array(
     *     <ActionName:string> => array(<ActionClass:string>, <builtin:bool>)
     * )
     * </pre>
     *
     * @var array $actions List of valid actions
     */
    public static $actions = array(
        'StoreTrue'   => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreTrue', true
        ),
        'StoreFalse'  => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreFalse', true
        ),
        'StoreString' => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreString', true
        ),
        'StoreInt'    => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreInt', true
        ),
        'StoreFloat'  => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreFloat', true
        ),
        'StoreArray'  => array(
            'BNjunge\\Console\\CommandLine\\Action\\StoreArray', true
        ),
        'Callback'    => array(
            'BNjunge\\Console\\CommandLine\\Action\\Callback', true
        ),
        'Counter'     => array(
            'BNjunge\\Console\\CommandLine\\Action\\Counter', true
        ),
        'Help'        => array(
            'BNjunge\\Console\\CommandLine\\Action\\Help', true
        ),
        'Version'     => array(
            'BNjunge\\Console\\CommandLine\\Action\\Version', true
        ),
        'Password'    => array(
            'BNjunge\\Console\\CommandLine\\Action\\Password', true
        ),
        'List'        => array(
            'BNjunge\\Console\\CommandLine\\Action_List', true
        ),
    );

    /**
     * Custom errors messages for this command
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see BNjunge\Console\CommandLine\MessageProvider\DefaultProvider
     */
    public $messages = array();

    // }}}
    // {{{ Private properties

    /**
     * Array of options that must be dispatched at the end.
     *
     * @var array $_dispatchLater Options to be dispatched
     */
    private $_dispatchLater = array();

    private $_lastopt = false;
    private $_stopflag = false;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     * Example:
     *
     * <code>
     * $parser = new BNjunge\Console\CommandLine(array(
     *     'name'               => 'yourprogram', // defaults to argv[0]
     *     'description'        => 'Description of your program',
     *     'version'            => '0.0.1', // your program version
     *     'add_help_option'    => true, // or false to disable --help option
     *     'add_version_option' => true, // or false to disable --version option
     *     'force_posix'        => false // or true to force posix compliance
     * ));
     * </code>
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct(array $params = array())
    {
        if (isset($params['name'])) {
            $this->name = $params['name'];
        } else if (isset($argv) && count($argv) > 0) {
            $this->name = $argv[0];
        } else if (isset($_SERVER['argv']) && count($_SERVER['argv']) > 0) {
            $this->name = $_SERVER['argv'][0];
        } else if (isset($_SERVER['SCRIPT_NAME'])) {
            $this->name = basename($_SERVER['SCRIPT_NAME']);
        }
        if (isset($params['description'])) {
            $this->description = $params['description'];
        }
        if (isset($params['version'])) {
            $this->version = $params['version'];
        }
        if (isset($params['add_version_option'])) {
            $this->add_version_option = $params['add_version_option'];
        }
        if (isset($params['add_help_option'])) {
            $this->add_help_option = $params['add_help_option'];
        }
        if (isset($params['subcommand_required'])) {
            $this->subcommand_required = $params['subcommand_required'];
        }
        if (isset($params['force_posix'])) {
            $this->force_posix = $params['force_posix'];
        } else if (getenv('POSIXLY_CORRECT')) {
            $this->force_posix = true;
        }
        if (isset($params['messages']) && is_array($params['messages'])) {
            $this->messages = $params['messages'];
        }
        // set default instances
        $this->renderer         = new CommandLine\Renderer_Default($this);
        $this->outputter        = new CommandLine\Outputter_Default();
        $this->message_provider = new CommandLine\MessageProvider\DefaultProvider();
    }

    // }}}
    // accept() {{{

    /**
     * Method to allow BNjunge\Console\CommandLine to accept either:
     *  + a custom renderer,
     *  + a custom outputter,
     *  + or a custom message provider
     *
     * @param mixed $instance The custom instance
     *
     * @return void
     * @throws BNjunge\Console\CommandLine\Exception if wrong argument passed
     */
    public function accept($instance)
    {
        if ($instance instanceof CommandLine\Renderer) {
            if (property_exists($instance, 'parser') && !$instance->parser) {
                $instance->parser = $this;
            }
            $this->renderer = $instance;
        } else if ($instance instanceof CommandLine\Outputter) {
            $this->outputter = $instance;
        } else if ($instance instanceof CommandLine\MessageProvider) {
            $this->message_provider = $instance;
        } else {
            throw CommandLine\Exception::factory(
                'INVALID_CUSTOM_INSTANCE',
                array(),
                $this,
                $this->messages
            );
        }
    }

    // }}}
    // fromXmlFile() {{{

    /**
     * Returns a command line parser instance built from an xml file.
     *
     * Example:
     * <code>
     * $parser = BNjunge\Console\CommandLine::fromXmlFile('path/to/file.xml');
     * $result = $parser->parse();
     * </code>
     *
     * @param string $file Path to the xml file
     *
     * @return BNjunge\Console\CommandLine The parser instance
     */
    public static function fromXmlFile($file)
    {
        return CommandLine\XmlParser::parse($file);
    }

    // }}}
    // fromXmlString() {{{

    /**
     * Returns a command line parser instance built from an xml string.
     *
     * Example:
     * <code>
     * $xmldata = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>
     * <command>
     *   <description>Compress files</description>
     *   <option name="quiet">
     *     <short_name>-q</short_name>
     *     <long_name>--quiet</long_name>
     *     <description>be quiet when run</description>
     *     <action>StoreTrue/action>
     *   </option>
     *   <argument name="files">
     *     <description>a list of files</description>
     *     <multiple>true</multiple>
     *   </argument>
     * </command>';
     * $parser = BNjunge\Console\CommandLine::fromXmlString($xmldata);
     * $result = $parser->parse();
     * </code>
     *
     * @param string $string The xml data
     *
     * @return BNjunge\Console\CommandLine The parser instance
     */
    public static function fromXmlString($string)
    {
        return CommandLine\XmlParser::parseString($string);
    }

    // }}}
    // addArgument() {{{

    /**
     * Adds an argument to the command line parser and returns it.
     *
     * Adds an argument with the name $name and set its attributes with the
     * array $params, then return the BNjunge\Console\CommandLine\Argument instance
     * created.
     * The method accepts another form: you can directly pass a
     * BNjunge\Console\CommandLine\Argument object as the sole argument, this allows
     * you to contruct the argument separately, in order to reuse it in
     * different command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new BNjunge\Console\CommandLine();
     * // add an array argument
     * $parser->addArgument('input_files', array('multiple'=>true));
     * // add a simple argument
     * $parser->addArgument('output_file');
     * $result = $parser->parse();
     * print_r($result->args['input_files']);
     * print_r($result->args['output_file']);
     * // will print:
     * // array('file1', 'file2')
     * // 'file3'
     * // if the command line was:
     * // myscript.php file1 file2 file3
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php <input_files...> <output_file>
     * </code>
     *
     * @param mixed $name   A string containing the argument name or an
     *                      instance of BNjunge\Console\CommandLine\Argument
     * @param array $params An array containing the argument attributes
     *
     * @return BNjunge\Console\CommandLine\Argument the added argument
     * 
     * @see BNjunge\Console\CommandLine\Argument
     */
    public function addArgument($name, $params = array())
    {
        if ($name instanceof CommandLine\Argument) {
            $argument = $name;
        } else {
            $argument = new CommandLine\Argument($name, $params);
        }
        $argument->validate();
        $this->args[$argument->name] = $argument;
        return $argument;
    }

    // }}}
    // addCommand() {{{

    /**
     * Adds a sub-command to the command line parser.
     *
     * Adds a command with the given $name to the parser and returns the
     * BNjunge\Console\CommandLine\Command instance, you can then populate the command
     * with options, configure it, etc... like you would do for the main parser
     * because the class BNjunge\Console\CommandLine\Command inherits from
     * BNjunge\Console\CommandLine.
     *
     * An example:
     * <code>
     * $parser = new BNjunge\Console\CommandLine();
     * $install_cmd = $parser->addCommand('install');
     * $install_cmd->addOption(
     *     'verbose',
     *     array(
     *         'short_name'  => '-v',
     *         'long_name'   => '--verbose',
     *         'description' => 'be noisy when installing stuff',
     *         'action'      => 'StoreTrue'
     *      )
     * );
     * $parser->parse();
     * </code>
     * Then in a terminal:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php install [options]
     *
     * Options:
     *   -h, --help     display this help message and exit
     *   -v, --verbose  be noisy when installing stuff
     *
     * $ myscript.php install --verbose
     * Installing whatever...
     * $
     * </code>
     *
     * @param mixed $name   A string containing the command name or an
     *                      instance of BNjunge\Console\CommandLine\Command
     * @param array $params An array containing the command attributes
     *
     * @return BNjunge\Console\CommandLine\Command The added subcommand
     * @see    BNjunge\Console\CommandLine\Command
     */
    public function addCommand($name, $params = array())
    {
        if ($name instanceof CommandLine\Command) {
            $command = $name;
        } else {
            $params['name'] = $name;
            $command        = new CommandLine\Command($params);
            // some properties must cascade to the child command if not
            // passed explicitely. This is done only in this case, because if
            // we have a Command object we have no way to determine if theses
            // properties have already been set
            $cascade = array(
                'add_help_option',
                'add_version_option',
                'outputter',
                'message_provider',
                'force_posix',
                'force_options_defaults'
            );
            foreach ($cascade as $property) {
                if (!isset($params[$property])) {
                    $command->$property = $this->$property;
                }
            }
            if (!isset($params['renderer'])) {
                $renderer          = clone $this->renderer;
                $renderer->parser  = $command;
                $command->renderer = $renderer;
            }
        }
        $command->parent = $this;
        $this->commands[$command->name] = $command;
        return $command;
    }

    // }}}
    // addOption() {{{

    /**
     * Adds an option to the command line parser and returns it.
     *
     * Adds an option with the name $name and set its attributes with the
     * array $params, then return the BNjunge\Console\CommandLine\Option instance
     * created.
     * The method accepts another form: you can directly pass a
     * BNjunge\Console\CommandLine\Option object as the sole argument, this allows
     * you to contruct the option separately, in order to reuse it in different
     * command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new BNjunge\Console\CommandLine();
     * $parser->addOption('path', array(
     *     'short_name'  => '-p',  // a short name
     *     'long_name'   => '--path', // a long name
     *     'description' => 'path to the dir', // a description msg
     *     'action'      => 'StoreString',
     *     'default'     => '/tmp' // a default value
     * ));
     * $parser->parse();
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php --help
     * Usage: myscript.php [options]
     *
     * Options:
     *   -h, --help  display this help message and exit
     *   -p, --path  path to the dir
     *
     * </code>
     *
     * Various methods to specify an option, these 3 commands are equivalent:
     * <code>
     * $ myscript.php --path=some/path
     * $ myscript.php -p some/path
     * $ myscript.php -psome/path
     * </code>
     *
     * @param mixed $name   A string containing the option name or an
     *                      instance of BNjunge\Console\CommandLine\Option
     * @param array $params An array containing the option attributes
     *
     * @return BNjunge\Console\CommandLine\Option The added option
     * @see    BNjunge\Console\CommandLine\Option
     */
    public function addOption($name, $params = array())
    {
        if ($name instanceof CommandLine\Option) {
            $opt = $name;
        } else {
            $opt = new CommandLine\Option($name, $params);
        }
        $opt->validate();
        if ($this->force_options_defaults) {
            $opt->setDefaults();
        }
        $this->options[$opt->name] = $opt;
        if (!empty($opt->choices) && $opt->add_list_option) {
            $this->addOption(
                'list_' . $opt->name,
                array(
                    'long_name'     => '--list-' . $opt->name,
                    'description'   => $this->message_provider->get(
                        'LIST_OPTION_MESSAGE',
                        array('name' => $opt->name)
                    ),
                    'action'        => 'List',
                    'action_params' => array('list' => $opt->choices),
                )
            );
        }
        return $opt;
    }

    // }}}
    // displayError() {{{

    /**
     * Displays an error to the user via stderr and exit with $exitCode if its
     * value is not equals to false.
     *
     * @param string $error    The error message
     * @param int    $exitCode The exit code number (default: 1). If set to
     *                         false, the exit() function will not be called
     *
     * @return void
     */
    public function displayError($error, $exitCode = 1)
    {
        $this->outputter->stderr($this->renderer->error($error));
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayUsage() {{{

    /**
     * Displays the usage help message to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayUsage($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->usage());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayVersion() {{{

    /**
     * Displays the program version to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayVersion($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->version());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // findOption() {{{

    /**
     * Finds the option that matches the given short_name (ex: -v), long_name
     * (ex: --verbose) or name (ex: verbose).
     *
     * @param string $str The option identifier
     *
     * @return mixed A BNjunge\Console\CommandLine\Option instance or false
     */
    public function findOption($str)
    {
        $str = trim($str);
        if ($str === '') {
            return false;
        }
        $matches = array();
        foreach ($this->options as $opt) {
            if ($opt->short_name == $str
                || $opt->long_name == $str
                || $opt->name == $str
            ) {
                // exact match
                return $opt;
            }
            if (substr($opt->long_name, 0, strlen($str)) === $str) {
                // abbreviated long option
                $matches[] = $opt;
            }
        }
        if ($count = count($matches)) {
            if ($count > 1) {
                $matches_str = '';
                $padding     = '';
                foreach ($matches as $opt) {
                    $matches_str .= $padding . $opt->long_name;
                    $padding      = ', ';
                }
                throw CommandLine\Exception::factory(
                    'OPTION_AMBIGUOUS',
                    array('name' => $str, 'matches' => $matches_str),
                    $this,
                    $this->messages
                );
            }
            return $matches[0];
        }
        return false;
    }
    // }}}
    // registerAction() {{{

    /**
     * Registers a custom action for the parser, an example:
     *
     * <code>
     *
     * // in this example we create a "range" action:
     * // the user will be able to enter something like:
     * // $ <program> -r 1,5
     * // and in the result we will have:
     * // $result->options['range']: array(1, 5)
     *
     * class ActionRange extends BNjunge\Console\CommandLine\Action
     * {
     *     public function execute($value=false, $params=array())
     *     {
     *         $range = explode(',', str_replace(' ', '', $value));
     *         if (count($range) != 2) {
     *             throw new Exception(sprintf(
     *                 'Option "%s" must be 2 integers separated by a comma',
     *                 $this->option->name
     *             ));
     *         }
     *         $this->setResult($range);
     *     }
     * }
     * // then we can register our action
     * BNjunge\Console\CommandLine::registerAction('Range', 'ActionRange');
     * // and now our action is available !
     * $parser = new BNjunge\Console\CommandLine();
     * $parser->addOption('range', array(
     *     'short_name'  => '-r',
     *     'long_name'   => '--range',
     *     'action'      => 'Range', // note our custom action
     *     'description' => 'A range of two integers separated by a comma'
     * ));
     * // etc...
     *
     * </code>
     *
     * @param string $name  The name of the custom action
     * @param string $class The class name of the custom action
     *
     * @return void
     */
    public static function registerAction($name, $class)
    {
        if (!isset(self::$actions[$name])) {
            if (!class_exists($class)) {
                self::triggerError(
                    'action_class_does_not_exists',
                    E_USER_ERROR,
                    array('{$name}' => $name, '{$class}' => $class)
                );
            }
            self::$actions[$name] = array($class, false);
        }
    }

    // }}}
    // triggerError() {{{

    /**
     * A wrapper for programming errors triggering.
     *
     * @param string $msgId  Identifier of the message
     * @param int    $level  The php error level
     * @param array  $params An array of search=>replaces entries
     *
     * @return void
     * 
     * @todo remove Console::triggerError() and use exceptions only
     */
    public static function triggerError($msgId, $level, $params=array())
    {
        if (isset(self::$errors[$msgId])) {
            $msg = str_replace(
                array_keys($params),
                array_values($params),
                self::$errors[$msgId]
            );
            trigger_error($msg, $level);
        } else {
            trigger_error('unknown error', $level);
        }
    }

    // }}}
    // parse() {{{

    /**
     * Parses the command line arguments and returns a
     * BNjunge\Console\CommandLine\Result instance.
     *
     * @param integer $userArgc Number of arguments (optional)
     * @param array   $userArgv Array containing arguments (optional)
     *
     * @return BNjunge\Console\CommandLine\Result The result instance
     * @throws Exception on user errors
     */
    public function parse($userArgc=null, $userArgv=null)
    {
        $this->addBuiltinOptions();
        if ($userArgc !== null && $userArgv !== null) {
            $argc = $userArgc;
            $argv = $userArgv;
        } else {
            list($argc, $argv) = $this->getArgcArgv();
        }
        // build an empty result
        $result = new CommandLine\Result();
        if (!($this instanceof CommandLine\Command)) {
            // remove script name if we're not in a subcommand
            array_shift($argv);
            $argc--;
        }
        // will contain arguments
        $args = array();
        foreach ($this->options as $name=>$option) {
            $result->options[$name] = $option->default;
        }
        // parse command line tokens
        while ($argc--) {
            $token = array_shift($argv);
            try {
                if ($cmd = $this->_getSubCommand($token)) {
                    $result->command_name = $cmd->name;
                    $result->command      = $cmd->parse($argc, $argv);
                    break;
                } else {
                    $this->parseToken($token, $result, $args, $argc);
                }
            } catch (\Exception $exc) {
                throw $exc;
            }
        }
        // Parse a null token to allow any undespatched actions to be despatched.
        $this->parseToken(null, $result, $args, 0);
        // Check if an invalid subcommand was specified. If there are
        // subcommands and no arguments, but an argument was provided, it is
        // an invalid subcommand.
        if (count($this->commands) > 0
            && count($this->args) === 0
            && count($args) > 0
        ) {
            throw CommandLine\Exception::factory(
                'INVALID_SUBCOMMAND',
                array('command' => $args[0]),
                $this,
                $this->messages
            );
        }
        // if subcommand_required is set to true we must check that we have a
        // subcommand.
        if (count($this->commands)
            && $this->subcommand_required
            && !$result->command_name
        ) {
            throw CommandLine\Exception::factory(
                'SUBCOMMAND_REQUIRED',
                array('commands' => implode(array_keys($this->commands), array(', '))),
                $this,
                $this->messages
            );
        }
        // minimum argument number check
        $argnum = 0;
        foreach ($this->args as $name=>$arg) {
            if (!$arg->optional) {
                $argnum++;
            }
        }
        if (count($args) < $argnum) {
            throw CommandLine\Exception::factory(
                'ARGUMENT_REQUIRED',
                array('argnum' => $argnum, 'plural' => $argnum>1 ? 's': ''),
                $this,
                $this->messages
            );
        }
        // handle arguments
        $c = count($this->args);
        foreach ($this->args as $name=>$arg) {
            $c--;
            if ($arg->multiple) {
                $result->args[$name] = $c ? array_splice($args, 0, -$c) : $args;
            } else {
                $result->args[$name] = array_shift($args);
            }
            if (!$result->args[$name] && $arg->optional && $arg->default) {
                $result->args[$name] = $arg->default;
            }
        }
        // dispatch deferred options
        foreach ($this->_dispatchLater as $optArray) {
            $optArray[0]->dispatchAction($optArray[1], $optArray[2], $this);
        }
        return $result;
    }

    // }}}
    // parseToken() {{{

    /**
     * Parses the command line token and modifies *by reference* the $options
     * and $args arrays.
     *
     * @param string $token  The command line token to parse
     * @param object $result The BNjunge\Console\CommandLine\Result instance
     * @param array  &$args  The argv array
     * @param int    $argc   Number of lasting args
     *
     * @return void
     * @access protected
     * @throws Exception on user errors
     */
    protected function parseToken($token, $result, &$args, $argc)
    {
        $last  = $argc === 0;
        if (!$this->_stopflag && $this->_lastopt) {
            if (substr($token, 0, 1) == '-') {
                if ($this->_lastopt->argument_optional) {
                    $this->_dispatchAction($this->_lastopt, '', $result);
                    if ($this->_lastopt->action != 'StoreArray') {
                        $this->_lastopt = false;
                    }
                } else if (isset($result->options[$this->_lastopt->name])) {
                    // case of an option that expect a list of args
                    $this->_lastopt = false;
                } else {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $this->_lastopt->name),
                        $this,
                        $this->messages
                    );
                }
            } else {
                // when a StoreArray option is positioned last, the behavior
                // is to consider that if there's already an element in the
                // array, and the commandline expects one or more args, we
                // leave last tokens to arguments
                if ($this->_lastopt->action == 'StoreArray'
                    && !empty($result->options[$this->_lastopt->name])
                    && count($this->args) > ($argc + count($args))
                ) {
                    if (!is_null($token)) {
                        $args[] = $token;
                    }
                    return;
                }
                if (!is_null($token) || $this->_lastopt->action == 'Password') {
                    $this->_dispatchAction($this->_lastopt, $token, $result);
                }
                if ($this->_lastopt->action != 'StoreArray') {
                    $this->_lastopt = false;
                }
                return;
            }
        }
        if (!$this->_stopflag && substr($token, 0, 2) == '--') {
            // a long option
            $optkv = explode('=', $token, 2);
            if (trim($optkv[0]) == '--') {
                // the special argument "--" forces in all cases the end of
                // option scanning.
                $this->_stopflag = true;
                return;
            }
            $opt = $this->findOption($optkv[0]);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optkv[0]),
                    $this,
                    $this->messages
                );
            }
            $value = isset($optkv[1]) ? $optkv[1] : false;
            if (!$opt->expectsArgument() && $value !== false) {
                throw CommandLine\Exception::factory(
                    'OPTION_VALUE_UNEXPECTED',
                    array('name' => $opt->name, 'value' => $value),
                    $this,
                    $this->messages
                );
            }
            if ($opt->expectsArgument() && $value === false) {
                // maybe the long option argument is separated by a space, if
                // this is the case it will be the next arg
                if ($last && !$opt->argument_optional) {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $opt->name),
                        $this,
                        $this->messages
                    );
                }
                // we will have a value next time
                $this->_lastopt = $opt;
                return;
            }
            if ($opt->action == 'StoreArray') {
                $this->_lastopt = $opt;
            }
            $this->_dispatchAction($opt, $value, $result);
        } else if (!$this->_stopflag && substr($token, 0, 1) == '-') {
            // a short option
            $optname = substr($token, 0, 2);
            if ($optname == '-') {
                // special case of "-": try to read stdin
                $args[] = file_get_contents('php://stdin');
                return;
            }
            $opt = $this->findOption($optname);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optname),
                    $this,
                    $this->messages
                );
            }
            // parse other options or set the value
            // in short: handle -f<value> and -f <value>
            $next = substr($token, 2, 1);
            // check if we must wait for a value
            if (!$next) {
                if ($opt->expectsArgument()) {
                    if ($last && !$opt->argument_optional) {
                        throw CommandLine\Exception::factory(
                            'OPTION_VALUE_REQUIRED',
                            array('name' => $opt->name),
                            $this,
                            $this->messages
                        );
                    }
                    // we will have a value next time
                    $this->_lastopt = $opt;
                    return;
                }
                $value = false;
            } else {
                if (!$opt->expectsArgument()) {
                    if ($nextopt = $this->findOption('-' . $next)) {
                        $this->_dispatchAction($opt, false, $result);
                        $this->parseToken(
                            '-' . substr($token, 2),
                            $result,
                            $args,
                            $last
                        );
                        return;
                    } else {
                        throw CommandLine\Exception::factory(
                            'OPTION_UNKNOWN',
                            array('name' => $next),
                            $this,
                            $this->messages
                        );
                    }
                }
                if ($opt->action == 'StoreArray') {
                    $this->_lastopt = $opt;
                }
                $value = substr($token, 2);
            }
            $this->_dispatchAction($opt, $value, $result);
        } else {
            // We have an argument.
            // if we are in POSIX compliant mode, we must set the stop flag to
            // true in order to stop option parsing.
            if (!$this->_stopflag && $this->force_posix) {
                $this->_stopflag = true;
            }
            if (!is_null($token)) {
                $args[] = $token;
            }
        }
    }

    // }}}
    // addBuiltinOptions() {{{

    /**
     * Adds the builtin "Help" and "Version" options if needed.
     *
     * @return void
     */
    public function addBuiltinOptions()
    {
        if ($this->add_help_option) {
            $helpOptionParams = array(
                'long_name'   => '--help',
                'description' => 'show this help message and exit',
                'action'      => 'Help'
            );
            if (!($option = $this->findOption('-h')) || $option->action == 'Help') {
                // short name is available, take it
                $helpOptionParams['short_name'] = '-h';
            }
            $this->addOption('help', $helpOptionParams);
        }
        if ($this->add_version_option && !empty($this->version)) {
            $versionOptionParams = array(
                'long_name'   => '--version',
                'description' => 'show the program version and exit',
                'action'      => 'Version'
            );
            if (!$this->findOption('-v')) {
                // short name is available, take it
                $versionOptionParams['short_name'] = '-v';
            }
            $this->addOption('version', $versionOptionParams);
        }
    }

    // }}}
    // getArgcArgv() {{{

    /**
     * Tries to return an array containing argc and argv, or trigger an error
     * if it fails to get them.
     *
     * @return array The argc/argv array
     * @throws BNjunge\Console\CommandLine\Exception
     */
    protected function getArgcArgv()
    {
        if (php_sapi_name() != 'cli') {
            // we have a web request
            $argv = array($this->name);
            if (isset($_REQUEST)) {
                foreach ($_REQUEST as $key => $value) {
                    if (!is_array($value)) {
                        $value = array($value);
                    }
                    $opt = $this->findOption($key);
                    if ($opt instanceof CommandLine\Option) {
                        // match a configured option
                        $argv[] = $opt->short_name ?
                            $opt->short_name : $opt->long_name;
                        foreach ($value as $v) {
                            if ($opt->expectsArgument()) {
                                $argv[] = isset($_REQUEST[$key])
                                    ? urldecode($v)
                                    : $v;
                            } else if ($v == '0' || $v == 'false') {
                                array_pop($argv);
                            }
                        }
                    } else if (isset($this->args[$key])) {
                        // match a configured argument
                        foreach ($value as $v) {
                            $argv[] = isset($_REQUEST[$key]) ? urldecode($v) : $v;
                        }
                    }
                }
            }
            return array(count($argv), $argv);
        }
        if (isset($argc) && isset($argv)) {
            // case of register_argv_argc = 1
            return array($argc, $argv);
        }
        if (isset($_SERVER['argc']) && isset($_SERVER['argv'])) {
            return array($_SERVER['argc'], $_SERVER['argv']);
        }
        return array(0, array());
    }

    // }}}
    // _dispatchAction() {{{

    /**
     * Dispatches the given option or store the option to dispatch it later.
     *
     * @param BNjunge\Console\CommandLine\Option $option The option instance
     * @param string                           $token  Command line token to parse
     * @param BNjunge\Console\CommandLine\Result $result The result instance
     *
     * @return void
     */
    private function _dispatchAction($option, $token, $result)
    {
        if ($option->action == 'Password') {
            $this->_dispatchLater[] = array($option, $token, $result);
        } else {
            $option->dispatchAction($token, $result, $this);
        }
    }
    // }}}
    // _getSubCommand() {{{

    /**
     * Tries to return the subcommand that matches the given token or returns
     * false if no subcommand was found.
     *
     * @param string $token Current command line token
     *
     * @return mixed An instance of BNjunge\Console\CommandLine\Command or false
     */
    private function _getSubCommand($token)
    {
        foreach ($this->commands as $cmd) {
            if ($cmd->name == $token || in_array($token, $cmd->aliases)) {
                return $cmd;
            }
        }
        return false;
    }

    // }}}
}


File: /src\DataFlowException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when the request/response cycle goes an unexpected way.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class DataFlowException extends RuntimeException implements Exception
{
    const CODE_INVALID_CREDENTIALS = 10000;
    const CODE_TAG_REQUIRED = 10500;
    const CODE_TAG_UNIQUE = 10501;
    const CODE_UNKNOWN_REQUEST = 10900;
    const CODE_CANCEL_FAIL = 11200;
}


File: /src\Exception.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Generic exception class of this package.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
interface Exception
{
}


File: /src\InvalidArgumentException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

use InvalidArgumentException as I;

/**
 * Exception thrown when there's something wrong with message arguments.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class InvalidArgumentException extends I implements Exception
{
    const CODE_SEEKABLE_REQUIRED = 1100;
    const CODE_NAME_INVALID = 20100;
    const CODE_ABSOLUTE_REQUIRED = 40200;
    const CODE_CMD_UNRESOLVABLE = 40201;
    const CODE_CMD_INVALID = 40202;
    const CODE_NAME_UNPARSABLE = 41000;
    const CODE_VALUE_UNPARSABLE = 41001;
}


File: /src\LengthException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base of this class.
 */
use LengthException as L;

/**
 * Used in $previous
 */
use Exception as E;

/**
 * Exception thrown when there is a problem with a word's length.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class LengthException extends L implements Exception
{

    const CODE_UNSUPPORTED = 1200;
    const CODE_INVALID = 1300;
    const CODE_BEYOND_SHEME = 1301;

    /**
     * The problematic length.
     *
     * @var int|double|null
     */
    private $_length;

    /**
     * Creates a new LengthException.
     *
     * @param string          $message  The Exception message to throw.
     * @param int             $code     The Exception code.
     * @param E|null          $previous The previous exception used for the
     *     exception chaining.
     * @param int|double|null $length   The length.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $length = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_length = $length;
    }

    /**
     * Gets the length.
     *
     * @return int|double|null The length.
     */
    public function getLength()
    {
        return $this->_length;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nLength:{$this->_length}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Message.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Implements this interface.
 */
use Countable;

/**
 * Implements this interface.
 */
use IteratorAggregate;

/**
 * Required for IteratorAggregate::getIterator() to work properly with foreach.
 */
use ArrayObject;

/**
 * Represents a RouterOS message.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
abstract class Message implements IteratorAggregate, Countable
{

    /**
     * An array with message attributes.
     *
     * Each array key is the the name of an attribute,
     * and the corresponding array value is the value for that attribute.
     *
     * @var array<string,string|resource>
     */
    protected $attributes = array();

    /**
     * An optional tag to associate the message with.
     *
     * @var string
     */
    private $_tag = null;

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param string|null $name The name of an attribute to get the value of,
     *     or NULL to get the tag.
     *
     * @return string|resource The value of the specified attribute,
     *     or the tag if NULL is provided.
     */
    public function __invoke($name = null)
    {
        if (null === $name) {
            return $this->getTag();
        }
        return $this->getAttribute($name);
    }

    /**
     * Sanitizes a name of an attribute (message or query one).
     *
     * @param mixed $name The name to sanitize.
     *
     * @return string The sanitized name.
     */
    public static function sanitizeAttributeName($name)
    {
        $name = (string) $name;
        if ((empty($name) && $name !== '0')
            || preg_match('/[=\s]/s', $name)
        ) {
            throw new InvalidArgumentException(
                'Invalid name of argument supplied.',
                InvalidArgumentException::CODE_NAME_INVALID
            );
        }
        return $name;
    }

    /**
     * Sanitizes a value of an attribute (message or query one).
     *
     * @param mixed $value The value to sanitize.
     *
     * @return string|resource The sanitized value.
     */
    public static function sanitizeAttributeValue($value)
    {
        if (Communicator::isSeekableStream($value)) {
            return $value;
        } else {
            return (string) $value;
        }
    }

    /**
     * Gets the tag that the message is associated with.
     *
     * @return string The current tag or NULL if there isn't a tag.
     *
     * @see setTag()
     */
    public function getTag()
    {
        return $this->_tag;
    }

    /**
     * Sets the tag to associate the request with.
     *
     * Sets the tag to associate the message with. Setting NULL erases the
     * currently set tag.
     *
     * @param string $tag The tag to set.
     *
     * @return $this The message object.
     *
     * @see getTag()
     */
    protected function setTag($tag)
    {
        $this->_tag = (null === $tag) ? null : (string) $tag;
        return $this;
    }

    /**
     * Gets the value of an attribute.
     *
     * @param string $name The name of the attribute.
     *
     * @return string|resource|null The value of the specified attribute.
     *     Returns NULL if such an attribute is not set.
     *
     * @see setAttribute()
     */
    protected function getAttribute($name)
    {
        $name = self::sanitizeAttributeName($name);
        if (array_key_exists($name, $this->attributes)) {
            return $this->attributes[$name];
        }
        return null;
    }

    /**
     * Gets all arguments in an array.
     *
     * @return ArrayObject An ArrayObject with the keys being argument names,
     *     and the array values being argument values.
     *
     * @see getArgument()
     * @see setArgument()
     */
    public function getIterator()
    {
        return new ArrayObject($this->attributes);
    }

    /**
     * Counts the number of attributes.
     *
     * @return int The number of attributes.
     */
    public function count()
    {
        return count($this->attributes);
    }

    /**
     * Sets an attribute for the message.
     *
     * @param string               $name  Name of the attribute.
     * @param string|resource|null $value Value of the attribute as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return $this The message object.
     *
     * @see getArgument()
     */
    protected function setAttribute($name, $value = '')
    {
        if (null === $value) {
            unset($this->attributes[self::sanitizeAttributeName($name)]);
        } else {
            $this->attributes[self::sanitizeAttributeName($name)]
                = self::sanitizeAttributeValue($value);
        }
        return $this;
    }

    /**
     * Removes all attributes from the message.
     *
     * @return $this The message object.
     */
    protected function removeAllAttributes()
    {
        $this->attributes = array();
        return $this;
    }
}


File: /src\MikrotikServiceProvider.php
<?php

namespace BNjunge;

use Illuminate\Support\ServiceProvider;

class MikrotikServiceProvider extends ServiceProvider{

    public function boot(){
        // echo 'It Works';
    }

    public function register(){
        
    }
}

File: /src\Net\Transmitter\Exception.php
<?php

/**
 * Wrapper for network stream functionality.

 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * Generic exception class of this package.
 * 
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
interface Exception
{
}


File: /src\Net\Transmitter\FilterCollection.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * A filter collection.
 *
 * Represents a collection of stream filters.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 * @see      Client
 */
class FilterCollection implements \SeekableIterator, \Countable
{
    /**
     * The filter collection itself.
     *
     * @var array
     */
    protected $filters = array();

    /**
     * A pointer, as required by SeekableIterator.
     *
     * @var int
     */
    protected $position = 0;

    /**
     * Appends a filter to the collection
     *
     * @param string $name   The name of the filter.
     * @param array  $params An array of parameters for the filter.
     *
     * @return $this The collection itself.
     */
    public function append($name, array $params = array())
    {
        $this->filters[] = array((string) $name, $params);
        return $this;
    }

    /**
     * Inserts the filter before a position.
     *
     * Inserts the specified filter before a filter at a specified position. The
     * new filter takes the specified position, while previous filters are moved
     * forward by one.
     *
     * @param int    $position The position before which the filter will be
     *     inserted.
     * @param string $name     The name of the filter.
     * @param array  $params   An array of parameters for the filter.
     *
     * @return $this The collection itself.
     */
    public function insertBefore($position, $name, array $params = array())
    {
        $position = (int) $position;
        if ($position <= 0) {
            $this->filters = array_merge(
                array(0 => array((string) $name, $params)),
                $this->filters
            );
            return $this;
        }
        if ($position > count($this->filters)) {
            return $this->append($name, $params);
        }
        $this->filters = array_merge(
            array_slice($this->filters, 0, $position),
            array(0 => array((string) $name, $params)),
            array_slice($this->filters, $position)
        );
        return $this;
    }

    /**
     * Removes a filter at a specified position.
     *
     * @param int $position The position from which to remove a filter.
     *
     * @return $this The collection itself.
     */
    public function removeAt($position)
    {
        unset($this->filters[$position]);
        $this->filters = array_values($this->filters);
        return $this;
    }

    /**
     * Clears the collection
     *
     * @return $this The collection itself.
     */
    public function clear()
    {
        $this->filters = array();
        return $this;
    }

    /**
     * Gets the number of filters in the collection.
     *
     * @return int The number of filters in the collection.
     */
    public function count()
    {
        return count($this->filters);
    }

    /**
     * Resets the pointer to 0.
     *
     * @return bool TRUE if the collection is not empty, FALSE otherwise.
     */
    public function rewind()
    {
        return $this->seek(0);
    }

    /**
     * Moves the pointer to a specified position.
     *
     * @param int $position The position to move to.
     *
     * @return bool TRUE if the specified position is valid, FALSE otherwise.
     */
    public function seek($position)
    {
        $this->position = $position;
        return $this->valid();
    }

    /**
     * Gets the current position.
     *
     * @return int The current position.
     */
    public function getCurrentPosition()
    {
        return $this->position;
    }

    /**
     * Moves the pointer forward by 1.
     *
     * @return bool TRUE if the new position is valid, FALSE otherwise.
     */
    public function next()
    {
        ++$this->position;
        return $this->valid();
    }

    /**
     * Gets the filter name at the current pointer position.
     *
     * @return string|false The name of the filter at the current position.
     */
    public function key()
    {
        return $this->valid() ? $this->filters[$this->position][0] : false;
    }

    /**
     * Gets the filter parameters at the current pointer position.
     *
     * @return array|false An array of parameters for the filter at the current
     *     position, or FALSE if the position is not valid.
     */
    public function current()
    {
        return $this->valid() ? $this->filters[$this->position][1] : false;
    }

    /**
     * Moves the pointer backwards by 1.
     *
     * @return bool TRUE if the new position is valid, FALSE otherwise.
     */
    public function prev()
    {
        --$this->position;
        return $this->valid();
    }

    /**
     * Moves the pointer to the last valid position.
     *
     * @return bool TRUE if the collection is not empty, FALSE otherwise.
     */
    public function end()
    {
        $this->position = count($this->filters) - 1;
        return $this->valid();
    }

    /**
     * Checks if the pointer is still pointing to an existing offset.
     *
     * @return bool TRUE if the pointer is valid, FALSE otherwise.
     */
    public function valid()
    {
        return array_key_exists($this->position, $this->filters);
    }
}


File: /src\Net\Transmitter\LockException.php
<?php

/**
 * Wrapper for network stream functionality.

 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * Exception thrown when something goes wrong when dealing with locks.
 * 
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class LockException extends \RuntimeException implements Exception
{
}


File: /src\Net\Transmitter\NetworkStream.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * A network transmitter.
 *
 * This is a convenience wrapper for network streams. Used to ensure data
 * integrity.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
abstract class NetworkStream extends Stream
{
    /**
     * Used in {@link setCrypto()} to disable encryption.
     */
    const CRYPTO_OFF = '';

    /**
     * Used in {@link setCrypto()} to set encryption to either SSLv2 or SSLv3,
     * depending on what the other end supports.
     */
    const CRYPTO_SSL = 'SSLv23';

    /**
     * Used in {@link setCrypto()} to set encryption to SSLv2.
     */
    const CRYPTO_SSL2 = 'SSLv2';

    /**
     * Used in {@link setCrypto()} to set encryption to SSLv3.
     */
    const CRYPTO_SSL3 = 'SSLv3';

    /**
     * Used in {@link setCrypto()} to set encryption to TLS (exact version
     * negotiated between 1.0 and 1.2).
     */
    const CRYPTO_TLS = 'TLS';

    /**
     * The type of stream. Can be either "_CLIENT" or "_SERVER".
     *
     * Used to complement the encryption type. Must be set by child classes
     * for {@link setCrypto()} to work properly.
     *
     * @var string
     */
    protected $streamType = '';

    /**
     * The current cryptography setting.
     *
     * @var string
     */
    protected $crypto = '';

    /**
     * Wraps around the specified stream.
     *
     * @param resource $stream The stream to wrap around.
     */
    public function __construct($stream)
    {
        parent::__construct($stream, true);
    }

    /**
     * Gets the current cryptography setting.
     *
     * @return string One of this class' CRYPTO_* constants.
     */
    public function getCrypto()
    {
        return $this->crypto;
    }

    /**
     * Sets the current connection's cryptography setting.
     *
     * @param string $type The encryption type to set. Must be one of this
     *     class' CRYPTO_* constants.
     *
     * @return boolean TRUE on success, FALSE on failure.
     */
    public function setCrypto($type)
    {
        if (self::CRYPTO_OFF === $type) {
            $result = stream_socket_enable_crypto($this->stream, false);
        } else {
            $result = stream_socket_enable_crypto(
                $this->stream,
                true,
                constant("STREAM_CRYPTO_METHOD_{$type}{$this->streamType}")
            );
        }

        if ($result) {
            $this->crypto = $type;
        }
        return $result;
    }

    /**
     * Checks whether the stream is available for operations.
     *
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        if ($this->isStream($this->stream)) {
            if ($this->isBlocking && feof($this->stream)) {
                return false;
            }
            $meta = stream_get_meta_data($this->stream);
            return !$meta['eof'];
        }
        return false;
    }

    /**
     * Sets the size of a stream's buffer.
     *
     * @param int $size      The desired size of the buffer, in bytes.
     * @param int $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        $result = parent::setBuffer($size, $direction);
        if (self::DIRECTION_SEND === $direction
            && function_exists('stream_set_chunk_size') && !$result
        ) {
            return false !== @stream_set_chunk_size($this->stream, $size);
        }
        return $result;
    }

    /**
     * Shutdown a full-duplex connection
     *
     * Shutdowns (partially or not) a full-duplex connection.
     *
     * @param int $direction The direction for which to disable further
     *     communications.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function shutdown($direction = self::DIRECTION_ALL)
    {
        $directionMap = array(
            self::DIRECTION_ALL => STREAM_SHUT_RDWR,
            self::DIRECTION_SEND => STREAM_SHUT_WR,
            self::DIRECTION_RECEIVE => STREAM_SHUT_RD
        );
        return array_key_exists($direction, $directionMap)
            && stream_socket_shutdown($this->stream, $directionMap[$direction]);
    }
}


File: /src\Net\Transmitter\SocketException.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * Used to enable any exception in chaining.
 */
use Exception as E;

/**
 * Exception thrown when something goes wrong with the connection.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class SocketException extends StreamException
{

    /**
     * The system level error code.
     *
     * @var int
     */
    protected $errorNo;

    /**
     * The system level error message.
     *
     * @var string
     */
    protected $errorStr;

    /**
     * Creates a new socket exception.
     *
     * @param string                   $message  The Exception message to throw.
     * @param int                      $code     The Exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occurred before the operation started.
     * @param int                      $errorNo  The system level error number.
     * @param string                   $errorStr The system level
     *     error message.
     */
    public function __construct(
        $message = '',
        $code = 0,
        E $previous = null,
        $fragment = null,
        $errorNo = null,
        $errorStr = null
    ) {
        parent::__construct($message, $code, $previous, $fragment);
        $this->errorNo = $errorNo;
        $this->errorStr = $errorStr;
    }

    /**
     * Gets the system level error code on the socket.
     *
     * @return int The system level error number.
     */
    public function getSocketErrorNumber()
    {
        return $this->errorNo;
    }

    // @codeCoverageIgnoreStart
    // Unreliable in testing.

    /**
     * Gets the system level error message on the socket.
     *
     * @return string The system level error message.
     */
    public function getSocketErrorMessage()
    {
        return $this->errorStr;
    }

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if (null !== $this->getSocketErrorNumber()) {
            $result .= "\nSocket error number:" . $this->getSocketErrorNumber();
        }
        if (null !== $this->getSocketErrorMessage()) {
            $result .= "\nSocket error message:"
                . $this->getSocketErrorMessage();
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}


File: /src\Net\Transmitter\Stream.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

use Exception as E;

/**
 * A stream transmitter.
 *
 * This is a convenience wrapper for stream functionality. Used to ensure data
 * integrity. Designed for TCP sockets, but it has intentionally been made to
 * accept any stream.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class Stream
{
    /**
     * Used to stop settings in either direction being applied.
     */
    const DIRECTION_NONE = 0;
    /**
     * Used to apply settings only to receiving.
     */
    const DIRECTION_RECEIVE = 1;
    /**
     * Used to apply settings only to sending.
     */
    const DIRECTION_SEND = 2;
    /**
     * Used to apply settings to both sending and receiving.
     */
    const DIRECTION_ALL = 3;

    /**
     * The stream to wrap around.
     *
     * @var resource
     */
    protected $stream;

    /**
     * Whether to automatically close the stream on object destruction if
     * it's not a persistent one.
     *
     * Setting this to FALSE may be useful if you're only using this class
     * "part time", while setting it to TRUE might be useful if you're doing
     * some "one offs".
     *
     * @var bool
     */
    protected $autoClose = false;

    /**
     * A flag that tells whether or not the stream is persistent.
     *
     * @var bool
     */
    protected $persist;

    /**
     * Whether the wrapped stream is in blocking mode or not.
     *
     * @var bool
     */
    protected $isBlocking = true;

    /**
     * An associative array with the chunk size of each direction.
     *
     * Key is the direction, value is the size in bytes as integer.
     *
     * @var array<int,int>
     */
    protected $chunkSize = array(
        self::DIRECTION_SEND => 0xFFFFF, self::DIRECTION_RECEIVE => 0xFFFFF
    );

    /**
     * Wraps around the specified stream.
     *
     * @param resource $stream    The stream to wrap around.
     * @param bool     $autoClose Whether to automatically close the stream on
     *     object destruction if it's not a persistent one. Setting this to
     *     FALSE may be useful if you're only using this class "part time",
     *     while setting it to TRUE might be useful if you're doing some
     *     "on offs".
     *
     * @see static::isFresh()
     */
    public function __construct($stream, $autoClose = false)
    {
        if (!self::isStream($stream)) {
            throw $this->createException('Invalid stream supplied.', 1);
        }
        $this->stream = $stream;
        $this->autoClose = (bool) $autoClose;
        $this->persist = (bool) preg_match(
            '#\s?persistent\s?#sm',
            get_resource_type($stream)
        );
        $meta = stream_get_meta_data($stream);
        $this->isBlocking = isset($meta['blocked']) ? $meta['blocked'] : true;
    }

    /**
     * PHP error handler for connection errors.
     *
     * @param string $level   Level of PHP error raised. Ignored.
     * @param string $message Message raised by PHP.
     *
     * @return void
     *
     * @throws SocketException That's how the error is handled.
     *
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    protected function handleError($level, $message)
    {
        throw $this->createException($message, 0);
    }

    /**
     * Checks if a given variable is a stream resource.
     *
     * @param mixed $var The variable to check.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isStream($var)
    {
        return is_resource($var)
            && (bool) preg_match('#\s?stream$#sm', get_resource_type($var));
    }

    /**
     * Checks whether the wrapped stream is fresh.
     *
     * Checks whether the wrapped stream is fresh. A stream is considered fresh
     * if there hasn't been any activity on it. Particularly useful for
     * detecting reused persistent connections.
     *
     * @return bool TRUE if the socket is fresh, FALSE otherwise.
     */
    public function isFresh()
    {
        return ftell($this->stream) === 0;
    }

    /**
     * Checks whether the wrapped stream is a persistent one.
     *
     * @return bool TRUE if the stream is a persistent one, FALSE otherwise.
     */
    public function isPersistent()
    {
        return $this->persist;
    }

    /**
     * Checks whether the wrapped stream is a blocking one.
     *
     * @return bool TRUE if the stream is a blocking one, FALSE otherwise.
     */
    public function isBlocking()
    {
        return $this->isBlocking;
    }

    /**
     * Sets blocking mode.
     *
     * @param bool $block Sets whether the stream is in blocking mode.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setIsBlocking($block)
    {
        $block = (bool)$block;
        if (stream_set_blocking($this->stream, (int)$block)) {
            $this->isBlocking = $block;
            return true;
        }
        return false;
    }

    /**
     * Sets the timeout for the stream.
     *
     * @param int $seconds      Timeout in seconds.
     * @param int $microseconds Timeout in microseconds to be added to the
     *     seconds.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setTimeout($seconds, $microseconds = 0)
    {
        return stream_set_timeout($this->stream, $seconds, $microseconds);
    }

    /**
     * Sets the size of a stream's buffer.
     *
     * @param int $size      The desired size of the buffer, in bytes.
     * @param int $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        switch($direction) {
        case self::DIRECTION_SEND:
            return stream_set_write_buffer($this->stream, $size) === 0;
        case self::DIRECTION_RECEIVE:
            return stream_set_read_buffer($this->stream, $size) === 0;
        case self::DIRECTION_ALL:
            return $this->setBuffer($size, self::DIRECTION_RECEIVE)
                && $this->setBuffer($size, self::DIRECTION_SEND);
        }
        return false;
    }

    /**
     * Sets the size of the chunk.
     *
     * To ensure data integrity, as well as to allow for lower memory
     * consumption, data is sent/received in chunks. This function
     * allows you to set the size of each chunk. The default is 0xFFFFF.
     *
     * @param int $size      The desired size of the chunk, in bytes.
     * @param int $direction The chunk of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setChunk($size, $direction = self::DIRECTION_ALL)
    {
        $size = (int) $size;
        if ($size <= 0) {
            return false;
        }
        switch($direction) {
        case self::DIRECTION_SEND:
        case self::DIRECTION_RECEIVE:
            $this->chunkSize[$direction] = $size;
            return true;
        case self::DIRECTION_ALL:
            $this->chunkSize[self::DIRECTION_SEND]
                = $this->chunkSize[self::DIRECTION_RECEIVE] = $size;
            return true;
        }
        return false;
    }

    /**
     * Gets the size of the chunk.
     *
     * @param int $direction The chunk of which direction to get. Valid
     *     values are the DIRECTION_* constants.
     *
     * @return int|array<int,int>|false The chunk size in bytes,
     *     or an array of chunk sizes with the directions as keys.
     *     FALSE on invalid direction.
     */
    public function getChunk($direction = self::DIRECTION_ALL)
    {
        switch($direction) {
        case self::DIRECTION_SEND:
        case self::DIRECTION_RECEIVE:
            return $this->chunkSize[$direction];
        case self::DIRECTION_ALL:
            return $this->chunkSize;
        }
        return false;
    }

    /**
     * Sends a string or stream over the wrapped stream.
     *
     * Sends a string or stream over the wrapped stream. If a seekable stream is
     * provided, it will be seeked back to the same position it was passed as,
     * regardless of the $offset parameter.
     *
     * @param string|resource $contents The string or stream to send.
     * @param int             $offset   The offset from which to start sending.
     *     If a stream is provided, and this is set to NULL, sending will start
     *     from the current stream position.
     * @param int             $length   The maximum length to send. If omitted,
     *     the string/stream will be sent to its end.
     *
     * @return int The number of bytes sent.
     */
    public function send($contents, $offset = null, $length = null)
    {
        $bytes = 0;
        $chunkSize = $this->chunkSize[self::DIRECTION_SEND];
        $lengthIsNotNull = null !== $length;
        $offsetIsNotNull = null !== $offset;
        if (self::isStream($contents)) {
            if ($offsetIsNotNull) {
                $oldPos = ftell($contents);
                fseek($contents, $offset, SEEK_SET);
            }
            while (!feof($contents)) {
                if ($lengthIsNotNull
                    && 0 === $chunkSize = min($chunkSize, $length - $bytes)
                ) {
                    break;
                }
                $contentsToSend = fread($contents, $chunkSize);
                if ('' != $contentsToSend) {
                    $bytesNow = @fwrite(
                        $this->stream,
                        $contentsToSend
                    );
                    if (0 != $bytesNow) {
                        $bytes += $bytesNow;
                    } elseif ($this->isBlocking || false === $bytesNow) {
                        throw $this->createException(
                            'Failed while sending stream.',
                            2,
                            null,
                            $bytes
                        );
                    }
                }
                $this->isAcceptingData(null);
            }
            if ($offsetIsNotNull) {
                fseek($contents, $oldPos, SEEK_SET);
            } else {
                fseek($contents, -$bytes, SEEK_CUR);
            }
        } else {
            $contents = (string) $contents;
            if ($offsetIsNotNull) {
                $contents = substr($contents, $offset);
            }
            if ($lengthIsNotNull) {
                $contents = substr($contents, 0, $length);
            }
            $bytesToSend = (double) sprintf('%u', strlen($contents));
            while ($bytes < $bytesToSend) {
                $bytesNow = @fwrite(
                    $this->stream,
                    substr($contents, $bytes, $chunkSize)
                );
                if (0 != $bytesNow) {
                    $bytes += $bytesNow;
                } elseif ($this->isBlocking || false === $bytesNow) {
                    throw $this->createException(
                        'Failed while sending string.',
                        3,
                        null,
                        $bytes
                    );
                }
                $this->isAcceptingData(null);
            }
        }
        return $bytes;
    }

    /**
     * Reads from the wrapped stream to receive.
     *
     * Reads from the wrapped stream to receive content as a string.
     *
     * @param int    $length The number of bytes to receive.
     * @param string $what   Descriptive string about what is being received
     *     (used in exception messages).
     *
     * @return string The received content.
     */
    public function receive($length, $what = 'data')
    {
        $result = '';
        $chunkSize = $this->chunkSize[self::DIRECTION_RECEIVE];
        while ($length > 0) {
            while ($this->isAvailable()) {
                $fragment = fread($this->stream, min($length, $chunkSize));
                if ('' != $fragment) {
                    $length -= strlen($fragment);
                    $result .= $fragment;
                    continue 2;
                } elseif (!$this->isBlocking && !(false === $fragment)) {
                    usleep(3000);
                    continue 2;
                }
            }
            throw $this->createException(
                "Failed while receiving {$what}",
                4,
                null,
                $result
            );
        }
        return $result;
    }

    /**
     * Reads from the wrapped stream to receive.
     *
     * Reads from the wrapped stream to receive content as a stream.
     *
     * @param int              $length  The number of bytes to receive.
     * @param FilterCollection $filters A collection of filters to apply to the
     *     stream while receiving. Note that the filters will not be present on
     *     the stream after receiving is done.
     * @param string           $what    Descriptive string about what is being
     *     received (used in exception messages).
     *
     * @return resource The received content.
     */
    public function receiveStream(
        $length,
        FilterCollection $filters = null,
        $what = 'stream data'
    ) {
        $result = fopen('php://temp', 'r+b');
        $appliedFilters = array();
        if (null !== $filters) {
            foreach ($filters as $filterName => $params) {
                $appliedFilters[] = stream_filter_append(
                    $result,
                    $filterName,
                    STREAM_FILTER_WRITE,
                    $params
                );
            }
        }

        $chunkSize = $this->chunkSize[self::DIRECTION_RECEIVE];
        while ($length > 0) {
            while ($this->isAvailable()) {
                $fragment = fread($this->stream, min($length, $chunkSize));
                if ('' != $fragment) {
                    $length -= strlen($fragment);
                    fwrite($result, $fragment);
                    continue 2;
                } elseif (!$this->isBlocking && !(false === $fragment)) {
                    usleep(3000);
                    continue 2;
                }
            }

            foreach ($appliedFilters as $filter) {
                stream_filter_remove($filter);
            }
            rewind($result);
            throw $this->createException(
                "Failed while receiving {$what}",
                5,
                null,
                $result
            );
        }

        foreach ($appliedFilters as $filter) {
            stream_filter_remove($filter);
        }
        rewind($result);
        return $result;
    }

    /**
     * Checks whether the stream is available for operations.
     *
     * For network streams, this means whether the other end has closed the
     * connection.
     *
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        return self::isStream($this->stream) && !feof($this->stream);
    }

    /**
     * Checks whether there is data to be read from the wrapped stream.
     *
     * @param int|null $sTimeout  If there isn't data awaiting currently,
     *     wait for it this many seconds for data to arrive. If NULL is
     *     specified, wait indefinitely for that.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     *
     * @return bool TRUE if there is data to be read, FALSE otherwise.
     *
     * @SuppressWarnings(PHPMD.ShortVariable)
     */
    public function isDataAwaiting($sTimeout = 0, $usTimeout = 0)
    {
        if (self::isStream($this->stream)) {
            if (null === $sTimeout && !$this->isBlocking) {
                $meta = stream_get_meta_data($this->stream);
                return !$meta['eof'];
            }

            $w = $e = null;
            $r = array($this->stream);
            return 1 === @/* due to PHP bug #54563 */stream_select(
                $r,
                $w,
                $e,
                $sTimeout,
                $usTimeout
            );
        }
        return false;
    }

    /**
     * Checks whether the wrapped stream can be written to without a block.
     *
     * @param int|null $sTimeout  If the stream isn't currently accepting data,
     *     wait for it this many seconds to start accepting data. If NULL is
     *     specified, wait indefinitely for that.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     *
     * @return bool TRUE if the wrapped stream would not block on a write,
     *     FALSE otherwise.
     *
     * @SuppressWarnings(PHPMD.ShortVariable)
     */
    public function isAcceptingData($sTimeout = 0, $usTimeout = 0)
    {
        if (self::isStream($this->stream)) {
            if (!$this->isBlocking) {
                $meta = stream_get_meta_data($this->stream);
                return !$meta['eof'];
            } elseif (feof($this->stream)) {
                return false;
            }

            $r = $e = null;
            $w = array($this->stream);
            return 1 === @/* due to PHP bug #54563 */stream_select(
                $r,
                $w,
                $e,
                $sTimeout,
                $usTimeout
            );
        }
        return false;
    }

    /**
     * Closes the opened stream, unless it's a persistent one.
     */
    public function __destruct()
    {
        if ((!$this->persist) && $this->autoClose) {
            $this->close();
        }
    }

    /**
     * Closes the opened stream, even if it is a persistent one.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        return self::isStream($this->stream) && fclose($this->stream);
    }

    /**
     * Creates a new exception.
     *
     * Creates a new exception. Used by the rest of the functions in this class.
     * Override in derived classes for custom exception handling.
     *
     * @param string                   $message  The exception message.
     * @param int                      $code     The exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *
     * @return StreamException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new StreamException($message, $code, $previous, $fragment);
    }
}


File: /src\Net\Transmitter\StreamException.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * Base for this exception.
 */
use RuntimeException;

/**
 * Used to enable any exception in chaining.
 */
use Exception as E;

/**
 * Exception thrown when something goes wrong with the connection.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class StreamException extends RuntimeException implements Exception
{
    /**
     * The fragment up until the point of failure.
     *
     * On failure with sending, this is the number of bytes sent successfully
     * before the failure.
     * On failure when receiving, this is a string/stream holding the contents
     * received successfully before the failure.
     * NULL if the failure occurred before the operation started.
     *
     * @var int|string|resource|null
     */
    protected $fragment = null;

    /**
     * Creates a new stream exception.
     *
     * @param string                   $message  The Exception message to throw.
     * @param int                      $code     The Exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occurred before the operation started.
     */
    public function __construct(
        $message,
        $code,
        E $previous = null,
        $fragment = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->fragment = $fragment;
    }

    /**
     * Gets the stream fragment.
     *
     * @return int|string|resource|null The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occurred before the operation started.
     */
    public function getFragment()
    {
        return $this->fragment;
    }

    // @codeCoverageIgnoreStart
    // Unreliable in testing.

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if (null !== $this->fragment) {
            $result .= "\nFragment: ";
            if (is_scalar($this->fragment)) {
                $result .= (string)$this->fragment;
            } else {
                $result .= stream_get_contents($this->fragment);
            }
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}


File: /src\Net\Transmitter\TcpClient.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

/**
 * Used for managing persistent connections.
 */
use BNjunge\Cache\SHM;

/**
 * Used for matching arbitrary exceptions in
 * {@link TcpClient::createException()} and releasing locks properly.
 */
use Exception as E;

/**
 * A socket transmitter.
 *
 * This is a convenience wrapper for socket functionality. Used to ensure data
 * integrity.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class TcpClient extends NetworkStream
{

    /**
     * The error code of the last error on the socket.
     *
     * @var int
     */
    protected $errorNo = 0;

    /**
     * The error message of the last error on the socket.
     *
     * @var string
     */
    protected $errorStr = null;

    /**
     * Persistent connection handler.
     *
     * Remains NULL for non-persistent connections.
     *
     * @var SHM
     */
    protected $shmHandler = null;

    /**
     * An array with all connections from this PHP request (as keys)
     * and their lock state (as a value).
     *
     * @var array
     */
    protected static $lockState = array();

    /**
     * Mappings from a protocol name to an URI scheme.
     *
     * @var array<string,string>
     */
    protected static $cryptoScheme = array(
        parent::CRYPTO_OFF => 'tcp',
        parent::CRYPTO_SSL2 => 'sslv2',
        parent::CRYPTO_SSL3 => 'sslv3',
        parent::CRYPTO_SSL => 'ssl',
        parent::CRYPTO_TLS => 'tls'
    );

    /**
     * The URI of this connection.
     *
     * @var string
     */
    protected $uri;

    /**
     * Creates a new connection with the specified options.
     *
     * @param string   $host    Hostname (IP or domain) of the server.
     * @param int      $port    The port on the server.
     * @param bool     $persist Whether or not the connection should be a
     *     persistent one.
     * @param float    $timeout The timeout for the connection.
     * @param string   $key     A string that uniquely identifies the
     *     connection. Ignored for non-persistent connections.
     * @param string   $crypto  Encryption setting. Must be one of the
     *     NetworkStream::CRYPTO_* constants. By default, encryption is
     *     disabled. If the setting has an associated scheme for it, it will be
     *     used, and if not, the setting will be adjusted right after the
     *     connection is established.
     * @param resource $context A context for the socket.
     */
    public function __construct(
        $host,
        $port,
        $persist = false,
        $timeout = null,
        $key = '',
        $crypto = parent::CRYPTO_OFF,
        $context = null
    ) {
        $this->streamType = '_CLIENT';

        if (strpos($host, ':') !== false) {
            $host = "[{$host}]";
        }

        $timeout
            = null == $timeout ? ini_get('default_socket_timeout') : $timeout;

        if (null === $context) {
            $context = stream_context_get_default();
        } elseif ((!is_resource($context))
            || ('stream-context' !== get_resource_type($context))
        ) {
            throw $this->createException('Invalid context supplied.', 6);
        }
        $hasCryptoScheme = array_key_exists($crypto, static::$cryptoScheme);
        $scheme = $hasCryptoScheme ? static::$cryptoScheme[$crypto] : 'tcp';
        $flags = STREAM_CLIENT_CONNECT;
        if ($persist) {
            $flags |= STREAM_CLIENT_PERSISTENT;
            $key = rawurlencode($key);
            $this->uri = "{$scheme}://{$host}:{$port}/{$key}";
        } else {
            $this->uri = "{$scheme}://{$host}:{$port}";
        }
        set_error_handler(array($this, 'handleError'));
        try {
            parent::__construct(
                stream_socket_client(
                    $this->uri,
                    $this->errorNo,
                    $this->errorStr,
                    $timeout,
                    $flags,
                    $context
                )
            );
            restore_error_handler();
        } catch (E $e) {
            restore_error_handler();
            if (0 === $this->errorNo) {
                throw $this->createException(
                    'Failed to initialize socket.',
                    7,
                    $e
                );
            }
            throw $this->createException(
                'Failed to connect with socket.',
                8,
                $e
            );
        }

        if ($hasCryptoScheme) {
            $this->crypto = $crypto;
        } elseif (parent::CRYPTO_OFF !== $crypto) {
            $this->setCrypto($crypto);
        }
        if (parent::CRYPTO_OFF !== $crypto) {
            $this->setIsBlocking(false);
        }

        if ($persist) {
            $this->shmHandler = SHM::factory(
                __CLASS__ . ' ' . $this->uri . ' '
            );
            self::$lockState[$this->uri] = self::DIRECTION_NONE;
        }
    }

    /**
     * Creates a new exception.
     *
     * Creates a new exception. Used by the rest of the functions in this class.
     *
     * @param string                   $message  The exception message.
     * @param int                      $code     The exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *
     * @return SocketException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new SocketException(
            $message,
            $code,
            $previous,
            $fragment,
            $this->errorNo,
            $this->errorStr
        );
    }

    /**
     * Locks transmission.
     *
     * Locks transmission in one or more directions. Useful when dealing with
     * persistent connections. Note that every send/receive call implicitly
     * calls this function and then restores it to the previous state. You only
     * need to call this function if you need to do an uninterrupted sequence of
     * such calls.
     *
     * @param int  $direction The direction(s) to have locked. Acceptable values
     *     are the DIRECTION_* constants. If a lock for a direction can't be
     *     obtained immediately, the function will block until one is acquired.
     *     Note that if you specify {@link static::DIRECTION_ALL},
     *     the sending lock will be obtained before the receiving one,
     *     and if obtaining the receiving lock afterwards fails,
     *     the sending lock will be released too.
     * @param bool $replace   Whether to replace all locks with the specified
     *     ones. Setting this to FALSE will make the function only obtain the
     *     locks which are not already obtained.
     *
     * @return int|false The previous state or FALSE if the connection is not
     *     persistent or arguments are invalid.
     */
    public function lock($direction = self::DIRECTION_ALL, $replace = false)
    {
        if ($this->persist && is_int($direction)) {
            $old = self::$lockState[$this->uri];

            if ($direction & self::DIRECTION_SEND) {
                if (($old & self::DIRECTION_SEND)
                    || $this->shmHandler->lock(self::DIRECTION_SEND)
                ) {
                    self::$lockState[$this->uri] |= self::DIRECTION_SEND;
                } else {
                    throw new LockException('Unable to obtain sending lock.');
                }
            } elseif ($replace) {
                if (!($old & self::DIRECTION_SEND)
                    || $this->shmHandler->unlock(self::DIRECTION_SEND)
                ) {
                    self::$lockState[$this->uri] &= ~self::DIRECTION_SEND;
                } else {
                    throw new LockException('Unable to release sending lock.');
                }
            }

            try {
                if ($direction & self::DIRECTION_RECEIVE) {
                    if (($old & self::DIRECTION_RECEIVE)
                        || $this->shmHandler->lock(self::DIRECTION_RECEIVE)
                    ) {
                        self::$lockState[$this->uri] |= self::DIRECTION_RECEIVE;
                    } else {
                        throw new LockException(
                            'Unable to obtain receiving lock.'
                        );
                    }
                } elseif ($replace) {
                    if (!($old & self::DIRECTION_RECEIVE)
                        || $this->shmHandler->unlock(self::DIRECTION_RECEIVE)
                    ) {
                        self::$lockState[$this->uri]
                            &= ~self::DIRECTION_RECEIVE;
                    } else {
                        throw new LockException(
                            'Unable to release receiving lock.'
                        );
                    }
                }
            } catch (LockException $e) {
                if ($direction & self::DIRECTION_SEND
                    && !($old & self::DIRECTION_SEND)
                ) {
                    $this->shmHandler->unlock(self::DIRECTION_SEND);
                }
                throw $e;
            }
            return $old;
        }
        return false;
    }


    /**
     * Sends a string or stream to the server.
     *
     * Sends a string or stream to the server. If a seekable stream is
     * provided, it will be seeked back to the same position it was passed as,
     * regardless of the $offset parameter.
     *
     * @param string|resource $contents The string or stream to send.
     * @param int             $offset   The offset from which to start sending.
     *     If a stream is provided, and this is set to NULL, sending will start
     *     from the current stream position.
     * @param int             $length   The maximum length to send. If omitted,
     *     the string/stream will be sent to its end.
     *
     * @return int The number of bytes sent.
     * @throws E
     */
    public function send($contents, $offset = null, $length = null)
    {
        if (false === ($previousState = $this->lock(self::DIRECTION_SEND))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain sending lock',
                10
            );
        }
        try {
            $result = parent::send($contents, $offset, $length);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }

    /**
     * Receives data from the server.
     *
     * Receives data from the server as a string.
     *
     * @param int    $length The number of bytes to receive.
     * @param string $what   Descriptive string about what is being received
     *     (used in exception messages).
     *
     * @return string The received content.
     */
    public function receive($length, $what = 'data')
    {
        if (false === ($previousState = $this->lock(self::DIRECTION_RECEIVE))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain receiving lock',
                9
            );
        }
        try {
            $result = parent::receive($length, $what);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }

    /**
     * Receives data from the server.
     *
     * Receives data from the server as a stream.
     *
     * @param int              $length  The number of bytes to receive.
     * @param FilterCollection $filters A collection of filters to apply to the
     *     stream while receiving. Note that the filters will not be present on
     *     the stream after receiving is done.
     * @param string           $what    Descriptive string about what is being
     *     received (used in exception messages).
     *
     * @return resource The received content.
     */
    public function receiveStream(
        $length,
        FilterCollection $filters = null,
        $what = 'stream data'
    ) {
        if (false === ($previousState = $this->lock(self::DIRECTION_RECEIVE))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain receiving lock',
                9
            );
        }
        try {
            $result = parent::receiveStream($length, $filters, $what);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }
}


File: /src\Net\Transmitter\TcpServerConnection.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge\Net\Transmitter;

use Exception as E;

/**
 * A transmitter for connections to a socket server.
 *
 * This is a convenience wrapper for functionality of socket server connections.
 * Used to ensure data integrity. Server handling is not part of the class in
 * order to allow its usage as part of various server implementations (e.g. fork
 * and/or sequential).
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class TcpServerConnection extends NetworkStream
{

    /**
     * The IP address of the connected client.
     *
     * @var string
     */
    protected $peerIP;

    /**
     * The port of the connected client.
     *
     * @var int
     */
    protected $peerPort;

    /**
     * Creates a new connection with the specified options.
     *
     * @param resource   $server  A socket server, created with
     *     {@link stream_socket_server()}.
     * @param float|null $timeout The timeout for the connection. Leaving this
     *     to NULL uses the default socket timeout.
     */
    public function __construct($server, $timeout = null)
    {
        $this->streamType = '_SERVER';

        if (!self::isStream($server)) {
            throw $this->createException('Invalid server supplied.', 9);
        }
        $timeout
            = null == $timeout ? ini_get('default_socket_timeout') : $timeout;

        set_error_handler(array($this, 'handleError'));
        try {
            parent::__construct(
                stream_socket_accept($server, $timeout, $peerName)
            );
            restore_error_handler();
            $portString = strrchr($peerName, ':');
            $this->peerPort = (int) substr($portString, 1);
            $ipString = substr(
                $peerName,
                0,
                strlen($peerName) - strlen($portString)
            );
            if (strpos($ipString, '[') === 0
                && strpos(strrev($ipString), ']') === 0
            ) {
                $ipString = substr($ipString, 1, strlen($ipString) - 2);
            }
            $this->peerIP = $ipString;
        } catch (E $e) {
            restore_error_handler();
            throw $this->createException(
                'Failed to initialize connection.',
                10,
                $e
            );
        }
    }

    /**
     * Gets the IP address of the connected client.
     *
     * @return string The IP address of the connected client.
     */
    public function getPeerIP()
    {
        return $this->peerIP;
    }

    /**
     * Gets the port of the connected client.
     *
     * @return int The port of the connected client.
     */
    public function getPeerPort()
    {
        return $this->peerPort;
    }

    /**
     * Creates a new exception.
     *
     * Creates a new exception. Used by the rest of the functions in this class.
     *
     * @param string      $message  The exception message.
     * @param int         $code     The exception code.
     * @param E|null      $previous Previous exception thrown, or NULL if there
     *     is none.
     * @param string|null $fragment The fragment up until the point of failure.
     *     NULL if the failure occurred before the operation started.
     *
     * @return SocketException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new SocketException(
            $message,
            $code,
            $previous,
            $fragment
        );
    }
}


File: /src\NotSupportedException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base of this class.
 */
use Exception as E;

/**
 * Exception thrown when encountering something not supported by RouterOS or
 * this package.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class NotSupportedException extends E implements Exception
{

    const CODE_CONTROL_BYTE = 1601;

    const CODE_MENU_MISMATCH = 60000;

    const CODE_ARG_PROHIBITED = 60001;

    /**
     * The unsupported value.
     *
     * @var mixed
     */
    private $_value;

    /**
     * Creates a new NotSupportedException.
     *
     * @param string $message  The Exception message to throw.
     * @param int    $code     The Exception code.
     * @param E|null $previous The previous exception used for the exception
     *     chaining.
     * @param mixed  $value    The unsupported value.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unsupported value.
     *
     * @return mixed The unsupported value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\ParserException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base of this class.
 */
use DomainException;

/**
 * Exception thrown when a value can't be parsed properly.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class ParserException extends DomainException implements Exception
{
    const CODE_DATETIME = 1;
    const CODE_DATEINTERVAL = 2;
    const CODE_ARRAY = 3;
}


File: /src\Query.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Refers to transmitter direction constants.
 */
use BNjunge\Net\Transmitter as T;

/**
 * Represents a query for RouterOS requests.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Query
{

    /**
     * Checks if the property exists.
     */
    const OP_EX = '';

    /**
     * Checks if the property does not exist.
     */
    const OP_NEX = '-';

    /**
     * Checks if the property equals a certain value.
     */
    const OP_EQ = '=';

    /**
     * Checks if the property is less than a certain value.
     */
    const OP_LT = '<';

    /**
     * Checks if the property is greater than a certain value.
     */
    const OP_GT = '>';

    /**
     * An array of the words forming the query.
     *
     * Each value is an array with the first member being the predicate
     * (operator and name), and the second member being the value
     * for the predicate.
     *
     * @var array<string,string|null>[]
     */
    protected $words = array();

    /**
     * This class is not to be instantiated normally, but by static methods
     * instead. Use {@link static::where()} to create an instance of it.
     */
    protected function __construct()
    {

    }

    /**
     * Sanitizes the operator of a condition.
     *
     * @param string $operator The operator to sanitize.
     *
     * @return string The sanitized operator.
     */
    protected static function sanitizeOperator($operator)
    {
        $operator = (string) $operator;
        switch ($operator) {
        case Query::OP_EX:
        case Query::OP_NEX:
        case Query::OP_EQ:
        case Query::OP_LT:
        case Query::OP_GT:
            return $operator;
        default:
            throw new UnexpectedValueException(
                'Unknown operator specified',
                UnexpectedValueException::CODE_ACTION_UNKNOWN,
                null,
                $operator
            );
        }
    }

    /**
     * Creates a new query with an initial condition.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return static A new query object.
     */
    public static function where(
        $name,
        $value = null,
        $operator = self::OP_EX
    ) {
        $query = new static;
        return $query->addWhere($name, $value, $operator);
    }

    /**
     * Negates the query.
     *
     * @return $this The query object.
     */
    public function not()
    {
        $this->words[] = array('#!', null);
        return $this;
    }

    /**
     * Adds a condition as an alternative to the query.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    public function orWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#|', null);
        return $this;
    }

    /**
     * Adds a condition in addition to the query.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    public function andWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#&', null);
        return $this;
    }

    /**
     * Sends the query over a communicator.
     *
     * @param Communicator $com The communicator to send the query over.
     *
     * @return int The number of bytes sent.
     */
    public function send(Communicator $com)
    {
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends the query over a communicator.
     *
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     *
     * @param Communicator $com The communicator to send the query over.
     *
     * @return int The number of bytes sent.
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_QUERY_SEND_FAIL
            );
        }
        $bytes = 0;
        foreach ($this->words as $queryWord) {
            list($predicate, $value) = $queryWord;
            $prefix = '?' . $predicate;
            if (null === $value) {
                $bytes += $com->sendWord($prefix);
            } else {
                $prefix .= '=';
                if (is_string($value)) {
                    $bytes += $com->sendWord($prefix . $value);
                } else {
                    $bytes += $com->sendWordFromStream($prefix, $value);
                }
            }
        }
        return $bytes;
    }

    /**
     * Verifies the query.
     *
     * Verifies the query against a communicator, i.e. whether the query
     * could successfully be sent (assuming the connection is still opened).
     *
     * @param Communicator $com The Communicator to check against.
     *
     * @return $this The query object itself.
     *
     * @throws LengthException If the resulting length of an API word is not
     *     supported.
     */
    public function verify(Communicator $com)
    {
        foreach ($this->words as $queryWord) {
            list($predicate, $value) = $queryWord;
            if (null === $value) {
                $com::verifyLengthSupport(strlen('?' . $predicate));
            } elseif (is_string($value)) {
                $com::verifyLengthSupport(
                    strlen('?' . $predicate . '=' . $value)
                );
            } else {
                $com::verifyLengthSupport(
                    strlen('?' . $predicate . '=') +
                    $com::seekableStreamLength($value)
                );
            }
        }
        return $this;
    }

    /**
     * Adds a condition.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the ACTION_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    protected function addWhere($name, $value, $operator)
    {
        $this->words[] = array(
            static::sanitizeOperator($operator)
            . Message::sanitizeAttributeName($name),
            (null === $value ? null : Message::sanitizeAttributeValue($value))
        );
        return $this;
    }
}


File: /src\Registry.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Uses shared memory to keep responses in.
 */
use BNjunge\Cache\SHM;

/**
 * A RouterOS registry.
 *
 * Provides functionality for managing the request/response flow. Particularly
 * useful in persistent connections.
 *
 * Note that this class is not meant to be called directly.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Registry
{
    /**
     * The storage.
     *
     * @var SHM
     */
    protected $shm;

    /**
     * ID of request. Populated at first instance in request.
     *
     * @var int
     */
    protected static $requestId = -1;

    /**
     * ID to be given to next instance, after incrementing it.
     *
     * @var int
     */
    protected static $instanceIdSeed = -1;

    /**
     * ID of instance within the request.
     *
     * @var int
     */
    protected $instanceId;

    /**
     * Creates a registry.
     *
     * @param string $uri An URI to bind the registry to.
     */
    public function __construct($uri)
    {
        $this->shm = SHM::factory(__CLASS__ . ' ' . $uri);
        if (-1 === self::$requestId) {
            self::$requestId = $this->shm->add('requestId', 0)
                ? 0 : $this->shm->inc('requestId');
        }
        $this->instanceId = ++self::$instanceIdSeed;
        $this->shm->add('responseBuffer_' . $this->getOwnershipTag(), array());
    }

    /**
     * Parses a tag.
     *
     * Parses a tag to reveal the ownership part of it, and the original tag.
     *
     * @param string $tag The tag (as received) to parse.
     *
     * @return array<int,string|null> An array with
     *     the first member being the ownership tag, and
     *     the second one being the original tag.
     */
    public static function parseTag($tag)
    {
        if (null === $tag) {
            return array(null, null);
        }
        $result = explode('__', $tag, 2);
        $result[0] .= '__';
        if ('' === $result[1]) {
            $result[1] = null;
        }
        return $result;
    }

    /**
     * Checks if this instance is the tagless mode owner.
     *
     * @return bool TRUE if this instance is the tagless mode owner, FALSE
     *     otherwise.
     */
    public function isTaglessModeOwner()
    {
        $this->shm->lock('taglessModeOwner');
        $result = $this->shm->exists('taglessModeOwner')
            && $this->getOwnershipTag() === $this->shm->get('taglessModeOwner');
        $this->shm->unlock('taglessModeOwner');
        return $result;
    }

    /**
     * Sets the "tagless mode" setting.
     *
     * While in tagless mode, this instance will claim ownership of any
     * responses without a tag. While not in this mode, any requests without a
     * tag will be given to all instances.
     *
     * Regardless of mode, if the type of the response is
     * {@link Response::TYPE_FATAL}, it will be given to all instances.
     *
     * @param bool $taglessMode TRUE to claim tagless ownership, FALSE to
     *     release such ownership, if taken.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setTaglessMode($taglessMode)
    {
        return $taglessMode
            ?   ($this->shm->lock('taglessMode')
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->add('taglessModeOwner', $this->getOwnershipTag())
                && $this->shm->unlock('taglessModeOwner'))
            :   ($this->isTaglessModeOwner()
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->delete('taglessModeOwner')
                && $this->shm->unlock('taglessModeOwner')
                && $this->shm->unlock('taglessMode'));
    }

    /**
     * Get the ownership tag for this instance.
     *
     * @return string The ownership tag for this registry instance.
     */
    public function getOwnershipTag()
    {
        return self::$requestId . '_' . $this->instanceId . '__';
    }

    /**
     * Add a response to the registry.
     *
     * @param Response $response     The response to add. The caller of this
     *     function is responsible for ensuring that the ownership tag and the
     *     original tag are separated, so that only the original one remains in
     *     the response.
     * @param string   $ownershipTag The ownership tag that the response had.
     *
     * @return bool TRUE if the request was added to its buffer, FALSE if
     *     this instance owns the response, and therefore doesn't need to add
     *     the response to its buffer.
     */
    public function add(Response $response, $ownershipTag)
    {
        if ($this->getOwnershipTag() === $ownershipTag
            || ($this->isTaglessModeOwner()
            && $response->getType() !== Response::TYPE_FATAL)
        ) {
            return false;
        }

        if (null === $ownershipTag) {
            $this->shm->lock('taglessModeOwner');
            if ($this->shm->exists('taglessModeOwner')
                && $response->getType() !== Response::TYPE_FATAL
            ) {
                $ownershipTag = $this->shm->get('taglessModeOwner');
                $this->shm->unlock('taglessModeOwner');
            } else {
                $this->shm->unlock('taglessModeOwner');
                foreach ($this->shm->getIterator(
                    '/^(responseBuffer\_)/',
                    true
                ) as $targetBufferName) {
                    $this->_add($response, $targetBufferName);
                }
                return true;
            }
        }

        $this->_add($response, 'responseBuffer_' . $ownershipTag);
        return true;
    }

    /**
     * Adds a response to a buffer.
     *
     * @param Response $response         The response to add.
     * @param string   $targetBufferName The name of the buffer to add the
     *     response to.
     *
     * @return void
     */
    private function _add(Response $response, $targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $targetBuffer = $this->shm->get($targetBufferName);
            $targetBuffer[] = $response;
            $this->shm->set($targetBufferName, $targetBuffer);
            $this->shm->unlock($targetBufferName);
        }
    }

    /**
     * Gets the next response from this instance's buffer.
     *
     * @return Response|null The next response, or NULL if there isn't one.
     */
    public function getNextResponse()
    {
        $response = null;
        $targetBufferName = 'responseBuffer_' . $this->getOwnershipTag();
        if ($this->shm->exists($targetBufferName)
            && $this->shm->lock($targetBufferName)
        ) {
            $targetBuffer = $this->shm->get($targetBufferName);
            if (!empty($targetBuffer)) {
                $response = array_shift($targetBuffer);
                $this->shm->set($targetBufferName, $targetBuffer);
            }
            $this->shm->unlock($targetBufferName);
        }
        return $response;
    }

    /**
     * Closes the registry.
     *
     * Closes the registry, meaning that all buffers are cleared.
     *
     * @return void
     */
    public function close()
    {
        self::$requestId = -1;
        self::$instanceIdSeed = -1;
        $this->shm->clear();
    }

    /**
     * Removes a buffer.
     *
     * @param string $targetBufferName The buffer to remove.
     *
     * @return void
     */
    private function _close($targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $this->shm->delete($targetBufferName);
            $this->shm->unlock($targetBufferName);
        }
    }

    /**
     * Removes this instance's buffer.
     */
    public function __destruct()
    {
        $this->_close('responseBuffer_' . $this->getOwnershipTag());
    }
}


File: /src\Request.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Refers to transmitter direction constants.
 */
use BNjunge\Net\Transmitter as T;

/**
 * Represents a RouterOS request.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Request extends Message
{

    /**
     * The command to be executed.
     *
     * @var string
     */
    private $_command;

    /**
     * A query for the command.
     *
     * @var Query
     */
    private $_query;

    /**
     * Creates a request to send to RouterOS.
     *
     * @param string      $command The command to send.
     *     Can also contain arguments expressed in a shell-like syntax.
     * @param Query|null  $query   A query to associate with the request.
     * @param string|null $tag     The tag for the request.
     *
     * @see setCommand()
     * @see setArgument()
     * @see setTag()
     * @see setQuery()
     */
    public function __construct($command, Query $query = null, $tag = null)
    {
        if (false !== strpos($command, '=')
            && false !== ($spaceBeforeEquals = strrpos(
                strstr($command, '=', true),
                ' '
            ))
        ) {
            $this->parseArgumentString(substr($command, $spaceBeforeEquals));
            $command = rtrim(substr($command, 0, $spaceBeforeEquals));
        }
        $this->setCommand($command);
        $this->setQuery($query);
        $this->setTag($tag);
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param Query|Communicator|string|null $arg A {@link Query} to associate
     *     the request with, a {@link Communicator} to send the request over,
     *     an argument to get the value of, or NULL to get the tag. If a
     *     second argument is provided, this becomes the name of the argument to
     *     set the value of, and the second argument is the value to set.
     *
     * @return string|resource|int|$this Whatever the long form
     *     function returns.
     */
    public function __invoke($arg = null)
    {
        if (func_num_args() > 1) {
            return $this->setArgument(func_get_arg(0), func_get_arg(1));
        }
        if ($arg instanceof Query) {
            return $this->setQuery($arg);
        }
        if ($arg instanceof Communicator) {
            return $this->send($arg);
        }
        return parent::__invoke($arg);
    }

    /**
     * Sets the command to send to RouterOS.
     *
     * Sets the command to send to RouterOS. The command can use the API or CLI
     * syntax of RouterOS, but either way, it must be absolute (begin  with a
     * "/") and without arguments.
     *
     * @param string $command The command to send.
     *
     * @return $this The request object.
     *
     * @see getCommand()
     * @see setArgument()
     */
    public function setCommand($command)
    {
        $command = (string) $command;
        if (strpos($command, '/') !== 0) {
            throw new InvalidArgumentException(
                'Commands must be absolute.',
                InvalidArgumentException::CODE_ABSOLUTE_REQUIRED
            );
        }
        if (substr_count($command, '/') === 1) {
            //Command line syntax convertion
            $cmdParts = preg_split('#[\s/]+#sm', $command);
            $cmdRes = array($cmdParts[0]);
            for ($i = 1, $n = count($cmdParts); $i < $n; $i++) {
                if ('..' === $cmdParts[$i]) {
                    $delIndex = count($cmdRes) - 1;
                    if ($delIndex < 1) {
                        throw new InvalidArgumentException(
                            'Unable to resolve command',
                            InvalidArgumentException::CODE_CMD_UNRESOLVABLE
                        );
                    }
                    unset($cmdRes[$delIndex]);
                    $cmdRes = array_values($cmdRes);
                } else {
                    $cmdRes[] = $cmdParts[$i];
                }
            }
            $command = implode('/', $cmdRes);
        }
        if (!preg_match('#^/\S+$#sm', $command)) {
            throw new InvalidArgumentException(
                'Invalid command supplied.',
                InvalidArgumentException::CODE_CMD_INVALID
            );
        }
        $this->_command = $command;
        return $this;
    }

    /**
     * Gets the command that will be send to RouterOS.
     *
     * Gets the command that will be send to RouterOS in its API syntax.
     *
     * @return string The command to send.
     *
     * @see setCommand()
     */
    public function getCommand()
    {
        return $this->_command;
    }

    /**
     * Sets the query to send with the command.
     *
     * @param Query|null $query The query to be set.
     *     Setting NULL will remove the  currently associated query.
     *
     * @return $this The request object.
     *
     * @see getQuery()
     */
    public function setQuery(Query $query = null)
    {
        $this->_query = $query;
        return $this;
    }

    /**
     * Gets the currently associated query
     *
     * @return Query|null The currently associated query.
     *
     * @see setQuery()
     */
    public function getQuery()
    {
        return $this->_query;
    }

    /**
     * Sets the tag to associate the request with.
     *
     * Sets the tag to associate the request with. Setting NULL erases the
     * currently set tag.
     *
     * @param string|null $tag The tag to set.
     *
     * @return $this The request object.
     *
     * @see getTag()
     */
    public function setTag($tag)
    {
        return parent::setTag($tag);
    }

    /**
     * Sets an argument for the request.
     *
     * @param string               $name  Name of the argument.
     * @param string|resource|null $value Value of the argument as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return $this The request object.
     *
     * @see getArgument()
     */
    public function setArgument($name, $value = '')
    {
        return parent::setAttribute($name, $value);
    }

    /**
     * Gets the value of an argument.
     *
     * @param string $name The name of the argument.
     *
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     *
     * @see setAttribute()
     */
    public function getArgument($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Removes all arguments from the request.
     *
     * @return $this The request object.
     */
    public function removeAllArguments()
    {
        return parent::removeAllAttributes();
    }

    /**
     * Sends a request over a communicator.
     *
     * @param Communicator  $com The communicator to send the request over.
     * @param Registry|null $reg An optional registry to sync the request with.
     *
     * @return int The number of bytes sent.
     *
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    public function send(Communicator $com, Registry $reg = null)
    {
        if (null !== $reg
            && (null != $this->getTag() || !$reg->isTaglessModeOwner())
        ) {
            $originalTag = $this->getTag();
            $this->setTag($reg->getOwnershipTag() . $originalTag);
            $bytes = $this->send($com);
            $this->setTag($originalTag);
            return $bytes;
        }
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends a request over a communicator.
     *
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     *
     * @param Communicator $com The communicator to send the request over.
     *
     * @return int The number of bytes sent.
     *
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_REQUEST_SEND_FAIL
            );
        }
        $bytes = 0;
        $bytes += $com->sendWord($this->getCommand());
        if (null !== ($tag = $this->getTag())) {
            $bytes += $com->sendWord('.tag=' . $tag);
        }
        foreach ($this->attributes as $name => $value) {
            $prefix = '=' . $name . '=';
            if (is_string($value)) {
                $bytes += $com->sendWord($prefix . $value);
            } else {
                $bytes += $com->sendWordFromStream($prefix, $value);
            }
        }
        $query = $this->getQuery();
        if ($query instanceof Query) {
            $bytes += $query->send($com);
        }
        $bytes += $com->sendWord('');
        return $bytes;
    }

    /**
     * Verifies the request.
     *
     * Verifies the request against a communicator, i.e. whether the request
     * could successfully be sent (assuming the connection is still opened).
     *
     * @param Communicator $com The Communicator to check against.
     *
     * @return $this The request object itself.
     *
     * @throws LengthException If the resulting length of an API word is not
     *     supported.
     */
    public function verify(Communicator $com)
    {
        $com::verifyLengthSupport(strlen($this->getCommand()));
        $com::verifyLengthSupport(strlen('.tag=' . (string)$this->getTag()));
        foreach ($this->attributes as $name => $value) {
            if (is_string($value)) {
                $com::verifyLengthSupport(strlen('=' . $name . '=' . $value));
            } else {
                $com::verifyLengthSupport(
                    strlen('=' . $name . '=') +
                    $com::seekableStreamLength($value)
                );
            }
        }
        $query = $this->getQuery();
        if ($query instanceof Query) {
            $query->verify($com);
        }
        return $this;
    }

    /**
     * Parses the arguments of a command.
     *
     * @param string $string The argument string to parse.
     *
     * @return void
     */
    protected function parseArgumentString($string)
    {
        /*
         * Grammar:
         *
         * <arguments> := (<<\s+>>, <argument>)*,
         * <argument> := <name>, <value>?
         * <name> := <<[^\=\s]+>>
         * <value> := "=", (<quoted string> | <unquoted string>)
         * <quotedString> := <<">>, <<([^"]|\\"|\\\\)*>>, <<">>
         * <unquotedString> := <<\S+>>
         */

        $token = '';
        $name = null;
        while ($string = substr($string, strlen($token))) {
            if (null === $name) {
                if (preg_match('/^\s+([^\s=]+)/sS', $string, $matches)) {
                    $token = $matches[0];
                    $name = $matches[1];
                } else {
                    throw new InvalidArgumentException(
                        "Parsing of argument name failed near '{$string}'",
                        InvalidArgumentException::CODE_NAME_UNPARSABLE
                    );
                }
            } elseif (preg_match('/^\s/s', $string, $matches)) {
                //Empty argument
                $token = '';
                $this->setArgument($name);
                $name = null;
            } elseif (preg_match(
                '/^="(([^\\\"]|\\\"|\\\\)*)"/sS',
                $string,
                $matches
            )) {
                $token = $matches[0];
                $this->setArgument(
                    $name,
                    str_replace(
                        array('\\"', '\\\\'),
                        array('"', '\\'),
                        $matches[1]
                    )
                );
                $name = null;
            } elseif (preg_match('/^=(\S+)/sS', $string, $matches)) {
                $token = $matches[0];
                $this->setArgument($name, $matches[1]);
                $name = null;
            } else {
                throw new InvalidArgumentException(
                    "Parsing of argument value failed near '{$string}'",
                    InvalidArgumentException::CODE_VALUE_UNPARSABLE
                );
            }
        }

        if (null !== $name && ('' !== ($name = trim($name)))) {
            $this->setArgument($name, '');
        }

    }
}


File: /src\Response.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Refers to transmitter direction constants.
 */
use BNjunge\Net\Transmitter as T;

/**
 * Locks are released upon any exception from anywhere.
 */
use Exception as E;

/**
 * Represents a RouterOS response.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Response extends Message
{

    /**
     * The last response for a request.
     */
    const TYPE_FINAL = '!done';

    /**
     * A response with data.
     */
    const TYPE_DATA = '!re';

    /**
     * A response signifying error.
     */
    const TYPE_ERROR = '!trap';

    /**
     * A response signifying a fatal error, due to which the connection would be
     * terminated.
     */
    const TYPE_FATAL = '!fatal';

    /**
     * An array of unrecognized words in network order.
     *
     * @var string[]
     */
    protected $unrecognizedWords = array();

    /**
     * The response type.
     *
     * @var string
     */
    private $_type;

    /**
     * Extracts a new response from a communicator.
     *
     * @param Communicator  $com       The communicator from which to extract
     *     the new response.
     * @param bool          $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int           $sTimeout  If a response is not immediately
     *     available, wait this many seconds. If NULL, wait indefinitely.
     * @param int|null      $usTimeout Microseconds to add to the waiting time.
     * @param Registry|null $reg       An optional registry to sync the
     *     response with.
     *
     * @see getType()
     * @see getArgument()
     */
    public function __construct(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null,
        Registry $reg = null
    ) {
        if (null === $reg) {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()
                    ->lock(T\Stream::DIRECTION_RECEIVE);
                try {
                    $this->_receive($com, $asStream, $sTimeout, $usTimeout);
                } catch (E $e) {
                    $com->getTransmitter()->lock($old, true);
                    throw $e;
                }
                $com->getTransmitter()->lock($old, true);
            } else {
                $this->_receive($com, $asStream, $sTimeout, $usTimeout);
            }
        } else {
            while (null === ($response = $reg->getNextResponse())) {
                $newResponse = new self($com, true, $sTimeout, $usTimeout);
                $tagInfo = $reg::parseTag($newResponse->getTag());
                $newResponse->setTag($tagInfo[1]);
                if (!$reg->add($newResponse, $tagInfo[0])) {
                    $response = $newResponse;
                    break;
                }
            }

            $this->_type = $response->_type;
            $this->attributes = $response->attributes;
            $this->unrecognizedWords = $response->unrecognizedWords;
            $this->setTag($response->getTag());

            if (!$asStream) {
                foreach ($this->attributes as $name => $value) {
                    $this->setAttribute(
                        $name,
                        stream_get_contents($value)
                    );
                }
                foreach ($response->unrecognizedWords as $i => $value) {
                    $this->unrecognizedWords[$i] = stream_get_contents($value);
                }
            }
        }
    }

    /**
     * Extracts a new response from a communicator.
     *
     * This is the function that performs the actual receiving, while the
     * constructor is also involved in locks and registry sync.
     *
     * @param Communicator $com       The communicator from which to extract
     *     the new response.
     * @param bool         $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int          $sTimeout  If a response is not immediately
     *     available, wait this many seconds. If NULL, wait indefinitely.
     *     Note that if an empty sentence is received, the timeout will be
     *     reset for another sentence receiving.
     * @param int|null     $usTimeout Microseconds to add to the waiting time.
     *
     * @return void
     */
    private function _receive(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null
    ) {
        do {
            if (!$com->getTransmitter()->isDataAwaiting(
                $sTimeout,
                $usTimeout
            )) {
                throw new SocketException(
                    'No data within the time limit',
                    SocketException::CODE_NO_DATA
                );
            }
            $type = $com->getNextWord();
        } while ('' === $type);
        $this->setType($type);
        if ($asStream) {
            for ($word = $com->getNextWordAsStream(), fseek($word, 0, SEEK_END);
                ftell($word) !== 0;
                $word = $com->getNextWordAsStream(), fseek(
                    $word,
                    0,
                    SEEK_END
                )) {
                rewind($word);
                $ind = fread($word, 1);
                if ('=' === $ind || '.' === $ind) {
                    $prefix = stream_get_line($word, null, '=');
                }
                if ('=' === $ind) {
                    $value = fopen('php://temp', 'r+b');
                    $bytesCopied = ftell($word);
                    while (!feof($word)) {
                        $bytesCopied += stream_copy_to_stream(
                            $word,
                            $value,
                            0xFFFFF,
                            $bytesCopied
                        );
                    }
                    rewind($value);
                    $this->setAttribute($prefix, $value);
                    continue;
                }
                if ('.' === $ind && 'tag' === $prefix) {
                    $this->setTag(stream_get_contents($word, -1, -1));
                    continue;
                }
                rewind($word);
                $this->unrecognizedWords[] = $word;
            }
        } else {
            for ($word = $com->getNextWord(); '' !== $word;
                $word = $com->getNextWord()) {
                if (preg_match('/^=([^=]+)=(.*)$/sS', $word, $matches)) {
                    $this->setAttribute($matches[1], $matches[2]);
                } elseif (preg_match('/^\.tag=(.*)$/sS', $word, $matches)) {
                    $this->setTag($matches[1]);
                } else {
                    $this->unrecognizedWords[] = $word;
                }
            }
        }
    }

    /**
     * Sets the response type.
     *
     * Sets the response type. Valid values are the TYPE_* constants.
     *
     * @param string $type The new response type.
     *
     * @return $this The response object.
     *
     * @see getType()
     */
    protected function setType($type)
    {
        switch ($type) {
        case self::TYPE_FINAL:
        case self::TYPE_DATA:
        case self::TYPE_ERROR:
        case self::TYPE_FATAL:
            $this->_type = $type;
            return $this;
        default:
            throw new UnexpectedValueException(
                'Unrecognized response type.',
                UnexpectedValueException::CODE_RESPONSE_TYPE_UNKNOWN,
                null,
                $type
            );
        }
    }

    /**
     * Gets the response type.
     *
     * @return string The response type.
     *
     * @see setType()
     */
    public function getType()
    {
        return $this->_type;
    }

    /**
     * Gets the value of an argument.
     *
     * @param string $name The name of the argument.
     *
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     *
     * @deprecated         1.0.0b5 Use {@link static::getProperty()} instead.
     *     This method will be removed upon final release, and is currently
     *     left standing merely because it can't be easily search&replaced in
     *     existing code, due to the fact the name "getArgument()" is shared
     *     with {@link Request::getArgument()}, which is still valid.
     * @codeCoverageIgnore
     */
    public function getArgument($name)
    {
        trigger_error(
            'Response::getArgument() is deprecated in favor of ' .
            'Response::getProperty() (but note that Request::getArgument() ' .
            'is still valid)',
            E_USER_DEPRECATED
        );
        return $this->getAttribute($name);
    }

    /**
     * Gets the value of a property.
     *
     * @param string $name The name of the property.
     *
     * @return string|resource|null The value of the specified property.
     *     Returns NULL if such a property is not set.
     */
    public function getProperty($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Gets a list of unrecognized words.
     *
     * @return string[] The list of unrecognized words.
     */
    public function getUnrecognizedWords()
    {
        return $this->unrecognizedWords;
    }
}


File: /src\ResponseCollection.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Implemented by this class.
 */
use ArrayAccess;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Implemented by this class.
 */
use SeekableIterator;

/**
 * Represents a collection of RouterOS responses.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 *
 * @method string getType()
 *     Calls {@link Response::getType()}
 *     on the response pointed by the pointer.
 * @method string[] getUnrecognizedWords()
 *     Calls {@link Response::getUnrecognizedWords()}
 *     on the response pointed by the pointer.
 * @method string|resource|null getProperty(string $name)
 *     Calls {@link Response::getProperty()}
 *     on the response pointed by the pointer.
 * @method string getTag()
 *     Calls {@link Response::getTag()}
 *     on the response pointed by the pointer.
 */
class ResponseCollection implements ArrayAccess, SeekableIterator, Countable
{

    /**
     * An array with all {@link Response} objects.
     *
     * An array with all Response objects.
     *
     * @var Response[]
     */
    protected $responses = array();

    /**
     * An array with each Response object's type.
     *
     * An array with each {@link Response} object's type.
     *
     * @var string[]
     */
    protected $responseTypes = array();

    /**
     * An array with each Response object's tag.
     *
     * An array with each {@link Response} object's tag.
     *
     * @var string[]
     */
    protected $responseTags = array();

    /**
     * An array with positions of responses, based on an property name.
     *
     * The name of each property is the array key, and the array value
     * is another array where the key is the value for that property, and
     * the value is the position of the response. For performance reasons,
     * each key is built only when {@link static::setIndex()} is called with
     * that property, and remains available for the lifetime of this collection.
     *
     * @var array<string,array<string,int>>
     */
    protected $responsesIndex = array();

    /**
     * An array with all distinct properties.
     *
     * An array with all distinct properties across all {@link Response}
     * objects. Created at the first call of {@link static::getPropertyMap()}.
     *
     * @var array<string,int[]>
     */
    protected $propertyMap = null;

    /**
     * A pointer, as required by SeekableIterator.
     *
     * @var int
     */
    protected $position = 0;

    /**
     * Name of property to use as index
     *
     * NULL when disabled.
     *
     * @var string|null
     */
    protected $index = null;

    /**
     * Compare criteria.
     *
     * Used by {@link static::compare()} to determine the order between
     * two responses. See {@link static::orderBy()} for a detailed description
     * of this array's format.
     *
     * @var string[]|array<string,null|int|array<int|callable>>
     */
    protected $compareBy = array();

    /**
     * Creates a new collection.
     *
     * @param Response[] $responses An array of responses, in network order.
     */
    public function __construct(array $responses)
    {
        $pos = 0;
        foreach ($responses as $response) {
            if ($response instanceof Response) {
                $this->responseTypes[$pos] = $response->getType();
                $this->responseTags[$pos] = $response->getTag();
                $this->responses[$pos++] = $response;
            }
        }
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param int|string|null $offset The offset of the response to seek to.
     *     If the offset is negative, seek to that relative to the end.
     *     If the collection is indexed, you can also supply a value to seek to.
     *     Setting NULL will get the current response's iterator.
     *
     * @return Response|ArrayObject The {@link Response} at the specified
     *     offset, the current response's iterator (which is an ArrayObject)
     *     when NULL is given, or FALSE if the offset is invalid
     *     or the collection is empty.
     */
    public function __invoke($offset = null)
    {
        return null === $offset
            ? $this->current()->getIterator()
            : $this->seek($offset);
    }

    /**
     * Sets a property to be usable as a key in the collection.
     *
     * @param string|null $name The name of the property to use. Future calls
     *     that accept a position will then also be able to search values of
     *     that property for a matching value.
     *     Specifying NULL will disable such lookups (as is by default).
     *     Note that in case this value occurs multiple times within the
     *     collection, only the last matching response will be accessible by
     *     that value.
     *
     * @return $this The object itself.
     */
    public function setIndex($name)
    {
        if (null !== $name) {
            $name = (string)$name;
            if (!isset($this->responsesIndex[$name])) {
                $this->responsesIndex[$name] = array();
                foreach ($this->responses as $pos => $response) {
                    $val = $response->getProperty($name);
                    if (null !== $val) {
                        $this->responsesIndex[$name][$val] = $pos;
                    }
                }
            }
        }
        $this->index = $name;
        return $this;
    }

    /**
     * Gets the name of the property used as an index.
     *
     * @return string|null Name of property used as index. NULL when disabled.
     */
    public function getIndex()
    {
        return $this->index;
    }

    /**
     * Gets the whole collection as an array.
     *
     * @param bool $useIndex Whether to use the index values as keys for the
     *     resulting array.
     *
     * @return Response[] An array with all responses, in network order.
     */
    public function toArray($useIndex = false)
    {
        if ($useIndex) {
            $positions = $this->responsesIndex[$this->index];
            asort($positions, SORT_NUMERIC);
            $positions = array_flip($positions);
            return array_combine(
                $positions,
                array_intersect_key($this->responses, $positions)
            );
        }
        return $this->responses;
    }

    /**
     * Counts the responses in the collection.
     *
     * @return int The number of responses in the collection.
     */
    public function count()
    {
        return count($this->responses);
    }

    /**
     * Checks if an offset exists.
     *
     * @param int|string $offset The offset to check. If the
     *     collection is indexed, you can also supply a value to check.
     *     Note that negative numeric offsets are NOT accepted.
     *
     * @return bool TRUE if the offset exists, FALSE otherwise.
     */
    public function offsetExists($offset)
    {
        return is_int($offset)
            ? array_key_exists($offset, $this->responses)
            : array_key_exists($offset, $this->responsesIndex[$this->index]);
    }

    /**
     * Gets a {@link Response} from a specified offset.
     *
     * @param int|string $offset The offset of the desired response. If the
     *     collection is indexed, you can also supply the value to search for.
     *
     * @return Response The response at the specified offset.
     */
    public function offsetGet($offset)
    {
        return is_int($offset)
            ? $this->responses[$offset >= 0
            ? $offset
            : count($this->responses) + $offset]
            : $this->responses[$this->responsesIndex[$this->index][$offset]];
    }

    /**
     * N/A
     *
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     *
     * @param int|string $offset N/A
     * @param Response   $value  N/A
     *
     * @return void
     *
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetSet($offset, $value)
    {

    }

    /**
     * N/A
     *
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     *
     * @param int|string $offset N/A
     *
     * @return void
     *
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetUnset($offset)
    {

    }

    /**
     * Resets the pointer to 0, and returns the first response.
     *
     * @return Response|false The first response in the collection,
     *     or FALSE if the collection is empty.
     */
    public function rewind()
    {
        return $this->seek(0);
    }

    /**
     * Moves the position pointer to a specified position.
     *
     * @param int|string $position The position to move to. If the collection is
     *     indexed, you can also supply a value to move the pointer to.
     *     A non-existent index will move the pointer to "-1".
     *
     * @return Response|false The {@link Response} at the specified position,
     *     or FALSE if the specified position is not valid.
     */
    public function seek($position)
    {
        $this->position = is_int($position)
            ? ($position >= 0
            ? $position
            : count($this->responses) + $position)
            : ($this->offsetExists($position)
            ? $this->responsesIndex[$this->index][$position]
            : -1);
        return $this->current();
    }

    /**
     * Moves the pointer forward by 1, and gets the next response.
     *
     * @return Response|false The next {@link Response} object,
     *     or FALSE if the position is not valid.
     */
    public function next()
    {
        ++$this->position;
        return $this->current();
    }

    /**
     * Gets the response at the current pointer position.
     *
     * @return Response|false The response at the current pointer position,
     *     or FALSE if the position is not valid.
     */
    public function current()
    {
        return $this->valid() ? $this->responses[$this->position] : false;
    }

    /**
     * Moves the pointer backwards by 1, and gets the previous response.
     *
     * @return Response|false The next {@link Response} object,
     *     or FALSE if the position is not valid.
     */
    public function prev()
    {
        --$this->position;
        return $this->current();
    }

    /**
     * Moves the pointer to the last valid position, and returns the last
     * response.
     *
     * @return Response|false The last response in the collection,
     *     or FALSE if the collection is empty.
     */
    public function end()
    {
        $this->position = count($this->responses) - 1;
        return $this->current();
    }

    /**
     * Gets the key at the current pointer position.
     *
     * @return int|false The key at the current pointer position,
     *     i.e. the pointer position itself, or FALSE if the position
     *     is not valid.
     */
    public function key()
    {
        return $this->valid() ? $this->position : false;
    }

    /**
     * Checks if the pointer is still pointing to an existing offset.
     *
     * @return bool TRUE if the pointer is valid, FALSE otherwise.
     */
    public function valid()
    {
        return $this->offsetExists($this->position);
    }

    /**
     * Gets all distinct property names.
     *
     * Gets all distinct property names across all responses.
     *
     * @return array<string,int[]> An array with
     *     all distinct property names as keys, and
     *     the indexes at which they occur as values.
     */
    public function getPropertyMap()
    {
        if (null === $this->propertyMap) {
            $properties = array();
            foreach ($this->responses as $index => $response) {
                $names = array_keys($response->getIterator()->getArrayCopy());
                foreach ($names as $name) {
                    if (!isset($properties[$name])) {
                        $properties[$name] = array();
                    }
                    $properties[$name][] = $index;
                }
            }
            $this->propertyMap = $properties;
        }
        return $this->propertyMap;
    }

    /**
     * Gets all responses of a specified type.
     *
     * @param string $type The response type to filter by. Valid values are the
     *     Response::TYPE_* constants.
     *
     * @return static A new collection with responses of the
     *     specified type.
     */
    public function getAllOfType($type)
    {
        $result = array();
        foreach (array_keys($this->responseTypes, $type, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Gets all responses with a specified tag.
     *
     * @param string $tag The tag to filter by.
     *
     * @return static A new collection with responses having the
     *     specified tag.
     */
    public function getAllTagged($tag)
    {
        $result = array();
        foreach (array_keys($this->responseTags, $tag, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Order resones by criteria.
     *
     * @param string[]|array<string,null|int|array<int|callable>> $criteria The
     *     criteria to order responses by. It takes the
     *     form of an array where each key is the name of the property to use
     *     as (N+1)th sorting key. The value of each member can be either NULL
     *     (for that property, sort normally in ascending order), a single sort
     *     order constant (SORT_ASC or SORT_DESC) to sort normally in the
     *     specified order, an array where the first member is an order
     *     constant, and the second one is sorting flags (same as built in PHP
     *     array functions) or a callback.
     *     If a callback is provided, it must accept two arguments
     *     (the two values to be compared), and return -1, 0 or 1 if the first
     *     value is respectively less than, equal to or greater than the second
     *     one.
     *     Each key of $criteria can also be numeric, in which case the
     *     value is the name of the property, and sorting is done normally in
     *     ascending order.
     *
     * @return static A new collection with the responses sorted in the
     *     specified order.
     */
    public function orderBy(array $criteria)
    {
        $this->compareBy = $criteria;
        $sortedResponses = $this->responses;
        usort($sortedResponses, array($this, 'compare'));
        return new static($sortedResponses);
    }

    /**
     * Calls a method of the response pointed by the pointer.
     *
     * Calls a method of the response pointed by the pointer. This is a magic
     * PHP method, thanks to which any function you call on the collection that
     * is not defined will be redirected to the response.
     *
     * @param string $method The name of the method to call.
     * @param array  $args   The arguments to pass to the method.
     *
     * @return mixed Whatever the called function returns.
     */
    public function __call($method, array $args)
    {
        return call_user_func_array(
            array($this->current(), $method),
            $args
        );
    }

    /**
     * Compares two responses.
     *
     * Compares two responses, based on criteria defined in
     * {@link static::$compareBy}.
     *
     * @param Response $itemA The response to compare.
     * @param Response $itemB The response to compare $a against.
     *
     * @return int Returns 0 if the two responses are equal according to every
     *     criteria specified, -1 if $a should be placed before $b, and 1 if $b
     *     should be placed before $a.
     */
    protected function compare(Response $itemA, Response $itemB)
    {
        foreach ($this->compareBy as $name => $spec) {
            if (!is_string($name)) {
                $name = $spec;
                $spec = null;
            }

            $members = array(
                0 => $itemA->getProperty($name),
                1 => $itemB->getProperty($name)
            );

            if (is_callable($spec)) {
                uasort($members, $spec);
            } elseif ($members[0] === $members[1]) {
                continue;
            } else {
                $flags = SORT_REGULAR;
                $order = SORT_ASC;
                if (is_array($spec)) {
                    list($order, $flags) = $spec;
                } elseif (null !== $spec) {
                    $order = $spec;
                }

                if (SORT_ASC === $order) {
                    asort($members, $flags);
                } else {
                    arsort($members, $flags);
                }
            }
            return (key($members) === 0) ? -1 : 1;
        }

        return 0;
    }
}


File: /src\RouterErrorException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Refered to in the constructor.
 */
use Exception as E;

/**
 * Exception thrown by higher level classes (Util, etc.) when the router
 * returns an error.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class RouterErrorException extends RuntimeException implements Exception
{
    const CODE_ITEM_ERROR           = 0x100000;
    const CODE_SCRIPT_ERROR         = 0x200000;
    const CODE_READ_ERROR           = 0x010000;
    const CODE_WRITE_ERROR          = 0x020000;
    const CODE_EXEC_ERROR           = 0x040000;

    const CODE_CACHE_ERROR          = 0x100001;
    const CODE_GET_ERROR            = 0x110001;
    const CODE_GETALL_ERROR         = 0x110002;
    const CODE_ADD_ERROR            = 0x120001;
    const CODE_SET_ERROR            = 0x120002;
    const CODE_REMOVE_ERROR         = 0x120004;
    const CODE_ENABLE_ERROR         = 0x120012;
    const CODE_DISABLE_ERROR        = 0x120022;
    const CODE_COMMENT_ERROR        = 0x120042;
    const CODE_UNSET_ERROR          = 0x120082;
    const CODE_MOVE_ERROR           = 0x120107;
    const CODE_SCRIPT_ADD_ERROR     = 0x220001;
    const CODE_SCRIPT_REMOVE_ERROR  = 0x220004;
    const CODE_SCRIPT_RUN_ERROR     = 0x240001;
    const CODE_SCRIPT_FILE_ERROR    = 0x240003;

    /**
     * The complete response returned by the router.
     *
     * NULL when the router was not contacted at all.
     *
     * @var ResponseCollection|null
     */
    private $_responses = null;

    /**
     * Creates a new RouterErrorException.
     *
     * @param string                  $message   The Exception message to throw.
     * @param int                     $code      The Exception code.
     * @param E|null                  $previous  The previous exception used for
     *     the exception chaining.
     * @param ResponseCollection|null $responses The complete set responses
     *     returned by the router.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        ResponseCollection $responses = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_responses = $responses;
    }

    /**
     * Gets the complete set responses returned by the router.
     *
     * @return ResponseCollection|null The complete set responses
     *     returned by the router.
     */
    public function getResponses()
    {
        return $this->_responses;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if ($this->_responses instanceof ResponseCollection) {
            $result .= "\nResponse collection:\n" .
                print_r($this->_responses->toArray(), true);
        }
        return $result;
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Script.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateTime;

/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateInterval;

/**
 * Used at {@link Script::escapeValue()} to get the proper time.
 */
use DateTimeZone;

/**
 * Used to reliably write to streams at {@link Script::prepare()}.
 */
use BNjunge\Net\Transmitter\Stream;

/**
 * Used to catch DateTime and DateInterval exceptions at
 * {@link Script::parseValue()}.
 */
use Exception as E;

/**
 * Scripting class.
 *
 * Provides functionality related to parsing and composing RouterOS scripts and
 * values.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Script
{
    /**
     * Parses a value from a RouterOS scripting context.
     *
     * Turns a value from RouterOS into an equivalent PHP value, based on
     * determining the type in the same way RouterOS would determine it for a
     * literal.
     *
     * This method is intended to be the very opposite of
     * {@link static::escapeValue()}. That is, results from that method, if
     * given to this method, should produce equivalent results.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object (either the main value, or values within an array)
     *     will use. Defaults to UTC.
     *
     * @return mixed Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - "array" - an array, with the keys and values processed recursively.
     *     - "time" - a {@link DateInterval} object.
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight.
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time.
     *     - "str" (a quoted string) - a string, with the contents escaped.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValue($value, DateTimeZone $timezone = null)
    {
        $value = static::parseValueToSimple($value);
        if (!is_string($value)) {
            return $value;
        }

        try {
            return static::parseValueToArray($value, $timezone);
        } catch (ParserException $e) {
            try {
                return static::parseValueToDateInterval($value);
            } catch (ParserException $e) {
                try {
                    return static::parseValueToDateTime($value, $timezone);
                } catch (ParserException $e) {
                    return static::parseValueToString($value);
                }
            }
        }
    }

    /**
     * Parses a RouterOS value into a PHP string.
     *
     * @param string $value The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string If a quoted string is provided, it would be parsed.
     *     Otherwise, the value is casted to a string, and returned unmodified.
     */
    public static function parseValueToString($value)
    {
        $value = (string)$value;
        if ('"' === $value[0] && '"' === $value[strlen($value) - 1]) {
            return str_replace(
                array('\"', '\\\\', "\\\n", "\\\r\n", "\\\r"),
                array('"', '\\'),
                substr($value, 1, -1)
            );
        }
        return $value;
    }

    /**
     * Parses a RouterOS value into a PHP simple type.
     *
     * Parses a RouterOS value into a PHP simple type. "Simple" types being
     * scalar types, plus NULL.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string|bool|int|double|null Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValueToSimple($value)
    {
        $value = (string)$value;

        if (in_array($value, array('', '[]'), true)) {
            return null;
        } elseif (in_array($value, array('true', 'false', 'yes', 'no'), true)) {
            return $value === 'true' || $value === 'yes';
        } elseif ($value === (string)($num = (int)$value)
            || $value === (string)($num = (double)$value)
        ) {
            return $num;
        }
        return $value;
    }

    /**
     * Parses a RouterOS value into a PHP DateTime object
     *
     * Parses a RouterOS value into a PHP DateTime object.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which the resulting
     *     DateTime object will use. Defaults to UTC.
     *
     * @return DateTime Depending on RouterOS type detected:
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight UTC time (regardless
     *         of timezone provided).
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time,
     *         with the specified timezone.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateTime(
        $value,
        DateTimeZone $timezone = null
    ) {
        $previous = null;
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '#^
                (?<mon>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
                /
                (?<day>\d\d?)
                /
                (?<year>\d{4})
                (?:
                    \s+(?<time>\d{2}\:\d{2}:\d{2})
                )?
            $#uix',
            $value,
            $date
        )) {
            if (!isset($date['time'])) {
                $date['time'] = '00:00:00';
                $timezone = new DateTimeZone('UTC');
            } elseif (null === $timezone) {
                $timezone = new DateTimeZone('UTC');
            }
            try {
                return new DateTime(
                    $date['year'] .
                    '-' . ucfirst($date['mon']) .
                    "-{$date['day']} {$date['time']}",
                    $timezone
                );
            } catch (E $e) {
                $previous = $e;
            }
        }
        throw new ParserException(
            'The supplied value can not be converted to a DateTime',
            ParserException::CODE_DATETIME,
            $previous
        );
    }

    /**
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return DateInterval The value as a DateInterval object.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateInterval($value)
    {
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '/^
                (?:(\d+)w)?
                (?:(\d+)d)?
                (?:(\d+)(?:\:|h))?
                (?|
                    (\d+)\:
                    (\d*(?:\.\d{1,9})?)
                |
                    (?:(\d+)m)?
                    (?:(\d+|\d*\.\d{1,9})s)?
                    (?:((?5))ms)?
                    (?:((?5))us)?
                    (?:((?5))ns)?
                )
            $/x',
            $value,
            $time
        )) {
            $days = isset($time[2]) ? (int)$time[2] : 0;
            if (isset($time[1])) {
                $days += 7 * (int)$time[1];
            }
            if (empty($time[3])) {
                $time[3] = 0;
            }
            if (empty($time[4])) {
                $time[4] = 0;
            }
            if (empty($time[5])) {
                $time[5] = 0;
            }

            $subsecondTime = 0.0;
            //@codeCoverageIgnoreStart
            // No PHP version currently supports sub-second DateIntervals,
            // meaning this section is untestable, since no version constraints
            // can be specified for test inputs.
            // All inputs currently use integer seconds only, making this
            // section unreachable during tests.
            // Nevertheless, this section exists right now, in order to provide
            // such support as soon as PHP has it.
            if (!empty($time[6])) {
                $subsecondTime += ((double)$time[6]) / 1000;
            }
            if (!empty($time[7])) {
                $subsecondTime += ((double)$time[7]) / 1000000;
            }
            if (!empty($time[8])) {
                $subsecondTime += ((double)$time[8]) / 1000000000;
            }
            //@codeCoverageIgnoreEnd

            $secondsSpec = $time[5] + $subsecondTime;
            try {
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
                //@codeCoverageIgnoreStart
                // See previous ignored section's note.
                //
                // This section is added for backwards compatibility with current
                // PHP versions, when in the future sub-second support is added.
                // In that event, the test inputs for older versions will be
                // expected to get a rounded up result of the sub-second data.
            } catch (E $e) {
                $secondsSpec = (int)round($secondsSpec);
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
            }
            //@codeCoverageIgnoreEnd
        }
        throw new ParserException(
            'The supplied value can not be converted to DateInterval',
            ParserException::CODE_DATEINTERVAL
        );
    }

    /**
     * Parses a RouterOS value into a PHP array.
     *
     * Parses a RouterOS value into a PHP array.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object within the array will use. Defaults to UTC.
     *
     * @return array An array, with the keys and values processed recursively,
     *         the keys with {@link static::parseValueToSimple()},
     *         and the values with {@link static::parseValue()}.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToArray(
        $value,
        DateTimeZone $timezone = null
    ) {
        $value = (string)$value;
        if ('{' === $value[0] && '}' === $value[strlen($value) - 1]) {
            $value = substr($value, 1, -1);
            if ('' === $value) {
                return array();
            }
            $parsedValue = preg_split(
                '/
                    (\"(?:\\\\\\\\|\\\\"|[^"])*\")
                    |
                    (\{[^{}]*(?2)?\})
                    |
                    ([^;=]+)
                /sx',
                $value,
                null,
                PREG_SPLIT_DELIM_CAPTURE
            );
            $result = array();
            $newVal = null;
            $newKey = null;
            for ($i = 0, $l = count($parsedValue); $i < $l; ++$i) {
                switch ($parsedValue[$i]) {
                case '':
                    break;
                case ';':
                    if (null === $newKey) {
                        $result[] = $newVal;
                    } else {
                        $result[$newKey] = $newVal;
                    }
                    $newKey = $newVal = null;
                    break;
                case '=':
                    $newKey = static::parseValueToSimple($parsedValue[$i - 1]);
                    $newVal = static::parseValue($parsedValue[++$i], $timezone);
                    break;
                default:
                    $newVal = static::parseValue($parsedValue[$i], $timezone);
                }
            }
            if (null === $newKey) {
                $result[] = $newVal;
            } else {
                $result[$newKey] = $newVal;
            }
            return $result;
        }
        throw new ParserException(
            'The supplied value can not be converted to an array',
            ParserException::CODE_ARRAY
        );
    }

    /**
     * Prepares a script.
     *
     * Prepares a script for eventual execution by prepending parameters as
     * variables to it.
     *
     * This is particularly useful when you're creating scripts that you don't
     * want to execute right now (as with {@link Util::exec()}, but instead
     * you want to store it for later execution, perhaps by supplying it to
     * "/system scheduler".
     *
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return resource A new PHP temporary stream with the script as contents,
     *     with the pointer back at the start.
     *
     * @see static::append()
     */
    public static function prepare(
        $source,
        array $params = array()
    ) {
        $resultStream = fopen('php://temp', 'r+b');
        static::append($resultStream, $source, $params);
        rewind($resultStream);
        return $resultStream;
    }

    /**
     * Appends a script.
     *
     * Appends a script to an existing stream.
     *
     * @param resource                $stream An existing stream to write the
     *     resulting script to.
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return int The number of bytes written to $stream is returned,
     *     and the pointer remains where it was after the write
     *     (i.e. it is not seeked back, even if seeking is supported).
     */
    public static function append(
        $stream,
        $source,
        array $params = array()
    ) {
        $writer = new Stream($stream, false);
        $bytes = 0;

        foreach ($params as $pname => $pvalue) {
            if (is_int($pname)) {
                $pvalue = static::escapeString((string)$pvalue);
                $bytes += $writer->send(":local \"{$pvalue}\";\n");
                continue;
            }
            $pname = static::escapeString($pname);
            $bytes += $writer->send(":local \"{$pname}\" ");
            if (Stream::isStream($pvalue)) {
                $reader = new Stream($pvalue, false);
                $chunkSize = $reader->getChunk(Stream::DIRECTION_RECEIVE);
                $bytes += $writer->send('"');
                while ($reader->isAvailable() && $reader->isDataAwaiting()) {
                    $bytes += $writer->send(
                        static::escapeString(fread($pvalue, $chunkSize), true)
                    );
                }
                $bytes += $writer->send("\";\n");
            } else {
                $bytes += $writer->send(static::escapeValue($pvalue) . ";\n");
            }
        }

        $bytes += $writer->send($source);
        return $bytes;
    }

    /**
     * Escapes a value for a RouterOS scripting context.
     *
     * Turns any native PHP value into an equivalent whole value that can be
     * inserted as part of a RouterOS script.
     *
     * DateInterval objects will be casted to RouterOS' "time" type.
     *
     * DateTime objects will be casted to a string following the "M/d/Y H:i:s"
     * format. If the time is exactly midnight (including microseconds), and
     * the timezone is UTC, the string will include only the "M/d/Y" date.
     *
     * Unrecognized types (i.e. resources and other objects) are casted to
     * strings, and those strings are then escaped.
     *
     * @param mixed $value The value to be escaped.
     *
     * @return string A string representation that can be directly inserted in a
     *     script as a whole value.
     */
    public static function escapeValue($value)
    {
        switch(gettype($value)) {
        case 'NULL':
            $value = '[]';
            break;
        case 'integer':
            $value = (string)$value;
            break;
        case 'boolean':
            $value = $value ? 'true' : 'false';
            break;
        case 'array':
            if (0 === count($value)) {
                $value = '({})';
                break;
            }
            $result = '';
            foreach ($value as $key => $val) {
                $result .= ';';
                if (!is_int($key)) {
                    $result .= static::escapeValue($key) . '=';
                }
                $result .= static::escapeValue($val);
            }
            $value = '{' . substr($result, 1) . '}';
            break;
        case 'object':
            if ($value instanceof DateTime) {
                $usec = $value->format('u');
                $usec = '000000' === $usec ? '' : '.' . $usec;
                $value = '00:00:00.000000 UTC' === $value->format('H:i:s.u e')
                    ? $value->format('M/d/Y')
                    : $value->format('M/d/Y H:i:s') . $usec;
            }
            if ($value instanceof DateInterval) {
                if (false === $value->days || $value->days < 0) {
                    $value = $value->format('%r%dd%H:%I:%S');
                } else {
                    $value = $value->format('%r%ad%H:%I:%S');
                }
                break;
            }
            //break; intentionally omitted
        default:
            $value = '"' . static::escapeString((string)$value) . '"';
            break;
        }
        return $value;
    }

    /**
     * Escapes a string for a RouterOS scripting context.
     *
     * Escapes a string for a RouterOS scripting context. The value can then be
     * surrounded with quotes at a RouterOS script (or concatenated onto a
     * larger string first), and you can be sure there won't be any code
     * injections coming from it.
     *
     * By default, for the sake of brevity of the output, ASCII alphanumeric
     * characters and underscores are left untouched. And for the sake of
     * character conversion, bytes above 0x7F are also left untouched.
     *
     * @param string $value Value to be escaped.
     * @param bool   $full  Whether to escape all bytes in the string, including
     *     ASCII alphanumeric characters, underscores and bytes above 0x7F.
     *
     * @return string The escaped value.
     *
     * @internal Why leave ONLY those ASCII characters and not also others?
     *     Because those can't in any way be mistaken for language constructs,
     *     unlike many other "safe inside strings, but not outside" ASCII
     *     characters, like ",", ".", "+", "-", "~", etc.
     */
    public static function escapeString($value, $full = false)
    {
        if ($full) {
            return self::_escapeCharacters(array($value));
        }
        return preg_replace_callback(
            '/[^\\_A-Za-z0-9\\x80-\\xFF]+/S',
            array(__CLASS__, '_escapeCharacters'),
            $value
        );
    }

    /**
     * Escapes a character for a RouterOS scripting context.
     *
     * Escapes a character for a RouterOS scripting context.
     * Intended to only be called by {@link self::escapeString()} for the
     * matching strings.
     *
     * @param array $chars The matches array, expected to contain exactly one
     *     member, in which is the whole string to be escaped.
     *
     * @return string The escaped characters.
     */
    private static function _escapeCharacters(array $chars)
    {
        $result = '';
        for ($i = 0, $l = strlen($chars[0]); $i < $l; ++$i) {
            $result .= '\\' . str_pad(
                strtoupper(dechex(ord($chars[0][$i]))),
                2,
                '0',
                STR_PAD_LEFT
            );
        }
        return $result;
    }
}


File: /src\SocketException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace Bnjunge;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when something goes wrong with the connection.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class SocketException extends RuntimeException
{
    const CODE_SERVICE_INCOMPATIBLE = 10200;
    const CODE_CONNECTION_FAIL = 100;
    const CODE_QUERY_SEND_FAIL = 30600;
    const CODE_REQUEST_SEND_FAIL = 40900;
    const CODE_NO_DATA = 50000;
}


File: /src\StreamException.php
<?php

/**
 * Wrapper for network stream functionality.

 *
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b2
 * @link      http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Base for this exception.
 */
use RuntimeException;

/**
 * Used to enable any exception in chaining.
 */
use Exception as E;

/**
 * Exception thrown when something goes wrong with the connection.
 *
 * @category Net
 * @package  BNjunge_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_Transmitter
 */
class StreamException extends RuntimeException implements Exception
{
    /**
     * The fragment up until the point of failure.
     *
     * On failure with sending, this is the number of bytes sent successfully
     * before the failure.
     * On failure when receiving, this is a string/stream holding the contents
     * received successfully before the failure.
     * NULL if the failure occurred before the operation started.
     *
     * @var int|string|resource|null
     */
    protected $fragment = null;

    /**
     * Creates a new stream exception.
     *
     * @param string                   $message  The Exception message to throw.
     * @param int                      $code     The Exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occurred before the operation started.
     */
    public function __construct(
        $message,
        $code,
        E $previous = null,
        $fragment = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->fragment = $fragment;
    }

    /**
     * Gets the stream fragment.
     *
     * @return int|string|resource|null The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occurred before the operation started.
     */
    public function getFragment()
    {
        return $this->fragment;
    }

    // @codeCoverageIgnoreStart
    // Unreliable in testing.

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if (null !== $this->fragment) {
            $result .= "\nFragment: ";
            if (is_scalar($this->fragment)) {
                $result .= (string)$this->fragment;
            } else {
                $result .= stream_get_contents($this->fragment);
            }
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}


File: /src\UnexpectedValueException.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * The base for this exception.
 */
use UnexpectedValueException as U;

/**
 * Used in $previous.
 */
use Exception as E;

/**
 * Exception thrown when encountering an invalid value in a function argument.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class UnexpectedValueException extends U implements Exception
{
    const CODE_CALLBACK_INVALID = 10502;
    const CODE_ACTION_UNKNOWN = 30100;
    const CODE_RESPONSE_TYPE_UNKNOWN = 50100;

    /**
     * The unexpected value.
     *
     * @var mixed
     */
    private $_value;

    /**
     * Creates a new UnexpectedValueException.
     *
     * @param string $message  The Exception message to throw.
     * @param int    $code     The Exception code.
     * @param E|null $previous The previous exception used for the exception
     *     chaining.
     * @param mixed  $value    The unexpected value.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unexpected value.
     *
     * @return mixed The unexpected value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Util.php
<?php

/**
 * RouterOS API client implementation.

 *
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 *
 * PHP version 5
 *
 * @category  Net
 * @package   BNjunge_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b6
 * @link      http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace BNjunge;

/**
 * Returned from {@link Util::getCurrentTime()}.
 */
use DateTime;

/**
 * Used at {@link Util::getCurrentTime()} to get the proper time.
 */
use DateTimeZone;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Used to detect streams in various methods of this class.
 */
use BNjunge\Net\Transmitter\Stream;

/**
 * Used to catch a DateTime exception at {@link Util::getCurrentTime()}.
 */
use Exception as E;

/**
 * Utility class.
 *
 * Abstracts away frequently used functionality (particularly CRUD operations)
 * in convenient to use methods by wrapping around a connection.
 *
 * @category Net
 * @package  BNjunge_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://BNjunge.php.net/BNjunge_Net_RouterOS
 */
class Util implements Countable
{
    /**
     * The connection to wrap around.
     *
     * @var Client
     */
    protected $client;

    /**
     * The current menu.
     *
     * Note that the root menu (only) uses an empty string.
     * This is done to enable commands executed at it without special casing it
     * at all commands.
     * Instead, only {@link static::setMenu()} is special cased.
     *
     * @var string
     */
    protected $menu = '';

    /**
     * An array with the numbers of items in the current menu.
     *
     * Numbers as keys, and the corresponding IDs as values.
     * NULL when the cache needs regenerating.
     *
     * @var array<int,string>|null
     */
    protected $idCache = null;

    /**
     * Creates a new Util instance.
     *
     * Wraps around a connection to provide convenience methods.
     *
     * @param Client $client The connection to wrap around.
     */
    public function __construct(Client $client)
    {
        $this->client = $client;
    }

    /**
     * Gets the current menu.
     *
     * @return string The absolute path to current menu, using API syntax.
     */
    public function getMenu()
    {
        return '' === $this->menu ? '/' : $this->menu;
    }

    /**
     * Sets the current menu.
     *
     * Sets the current menu.
     *
     * @param string $newMenu The menu to change to. Can be specified with API
     *     or CLI syntax and can be either absolute or relative. If relative,
     *     it's relative to the current menu, which by default is the root.
     *
     * @return $this The object itself. If an empty string is given for
     *     a new menu, no change is performed,
     *     but the ID cache is cleared anyway.
     *
     * @see static::clearIdCache()
     */
    public function setMenu($newMenu)
    {
        $newMenu = (string)$newMenu;
        if ('' !== $newMenu) {
            $menuRequest = new Request('/menu');
            if ('/' === $newMenu) {
                $this->menu = '';
            } elseif ('/' === $newMenu[0]) {
                $this->menu = $menuRequest->setCommand($newMenu)->getCommand();
            } else {
                $newMenu = (string)substr(
                    $menuRequest->setCommand(
                        '/' .
                        str_replace('/', ' ', (string)substr($this->menu, 1)) .
                        ' ' .
                        str_replace('/', ' ', $newMenu)
                        . ' ?'
                    )->getCommand(),
                    1,
                    -2/*strlen('/?')*/
                );
                if ('' !== $newMenu) {
                    $this->menu = '/' . $newMenu;
                } else {
                    $this->menu = '';
                }
            }
        }
        $this->clearIdCache();
        return $this;
    }

    /**
     * Creates a Request object.
     *
     * Creates a {@link Request} object, with a command that's at the
     * current menu. The request can then be sent using {@link Client}.
     *
     * @param string      $command The command of the request, not including
     *     the menu. The request will have that command at the current menu.
     * @param array       $args    Arguments of the request.
     *     Each array key is the name of the argument, and each array value is
     *     the value of the argument to be passed.
     *     Arguments without a value (i.e. empty arguments) can also be
     *     specified using a numeric key, and the name of the argument as the
     *     array value.
     * @param Query|null  $query   The {@link Query} of the request.
     * @param string|null $tag     The tag of the request.
     *
     * @return Request The {@link Request} object.
     *
     * @throws NotSupportedException On an attempt to call a command in a
     *     different menu using API syntax.
     * @throws InvalidArgumentException On an attempt to call a command in a
     *     different menu using CLI syntax.
     */
    public function newRequest(
        $command,
        array $args = array(),
        Query $query = null,
        $tag = null
    ) {
        if (false !== strpos($command, '/')) {
            throw new NotSupportedException(
                'Command tried to go to a different menu',
                NotSupportedException::CODE_MENU_MISMATCH,
                null,
                $command
            );
        }
        $request = new Request('/menu', $query, $tag);
        $request->setCommand("{$this->menu}/{$command}");
        foreach ($args as $name => $value) {
            if (is_int($name)) {
                $request->setArgument($value);
            } else {
                $request->setArgument($name, $value);
            }
        }
        return $request;
    }

    /**
     * Executes a RouterOS script.
     *
     * Executes a RouterOS script, written as a string or a stream.
     * Note that in cases of errors, the line numbers will be off, because the
     * script is executed at the current menu as context, with the specified
     * variables pre declared. This is achieved by prepending 1+count($params)
     * lines before your actual script.
     *
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *     Note that the script's (generated) name is always added as the
     *     variable "_", which will be inadvertently lost if you overwrite it
     *     from here.
     * @param string|null             $policy Allows you to specify a policy the
     *     script must follow. Has the same format as in terminal.
     *     If left NULL, the script has no restrictions beyond those imposed by
     *     the username.
     * @param string|null             $name   The script is executed after being
     *     saved in "/system script" and is removed after execution.
     *     If this argument is left NULL, a random string,
     *     prefixed with the computer's name, is generated and used
     *     as the script's name.
     *     To eliminate any possibility of name clashes,
     *     you can specify your own name instead.
     *
     * @return ResponseCollection The responses of all requests involved, i.e.
     *     the add, the run and the remove.
     *
     * @throws RouterErrorException When there is an error in any step of the
     *     way. The reponses include all successful commands prior to the error
     *     as well. If the error occurs during the run, there will also be a
     *     remove attempt, and the results will include its results as well.
     */
    public function exec(
        $source,
        array $params = array(),
        $policy = null,
        $name = null
    ) {
        if (null === $name) {
            $name = uniqid(gethostname(), true);
        }

        $request = new Request('/system/script/add');
        $request->setArgument('name', $name);
        $request->setArgument('policy', $policy);

        $params += array('_' => $name);

        $finalSource = fopen('php://temp', 'r+b');
        fwrite(
            $finalSource,
            '/' . str_replace('/', ' ', substr($this->menu, 1)). "\n"
        );
        Script::append($finalSource, $source, $params);
        fwrite($finalSource, "\n");
        rewind($finalSource);

        $request->setArgument('source', $finalSource);
        $addResult = $this->client->sendSync($request);

        if (count($addResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when trying to add script',
                RouterErrorException::CODE_SCRIPT_ADD_ERROR,
                null,
                $addResult
            );
        }

        $request = new Request('/system/script/run');
        $request->setArgument('number', $name);
        $runResult = $this->client->sendSync($request);
        $request = new Request('/system/script/remove');
        $request->setArgument('numbers', $name);
        $removeResult = $this->client->sendSync($request);

        $results = new ResponseCollection(
            array_merge(
                $addResult->toArray(),
                $runResult->toArray(),
                $removeResult->toArray()
            )
        );

        if (count($runResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when running script',
                RouterErrorException::CODE_SCRIPT_RUN_ERROR,
                null,
                $results
            );
        }
        if (count($removeResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when removing script',
                RouterErrorException::CODE_SCRIPT_REMOVE_ERROR,
                null,
                $results
            );
        }

        return $results;
    }

    /**
     * Clears the ID cache.
     *
     * Normally, the ID cache improves performance when targeting items by a
     * number. If you're using both Util's methods and other means (e.g.
     * {@link Client} or {@link Util::exec()}) to add/move/remove items, the
     * cache may end up being out of date. By calling this method right before
     * targeting an item with a number, you can ensure number accuracy.
     *
     * Note that Util's {@link static::move()} and {@link static::remove()}
     * methods automatically clear the cache before returning, while
     * {@link static::add()} adds the new item's ID to the cache as the next
     * number. A change in the menu also clears the cache.
     *
     * Note also that the cache is being rebuilt unconditionally every time you
     * use {@link static::find()} with a callback.
     *
     * @return $this The Util object itself.
     */
    public function clearIdCache()
    {
        $this->idCache = null;
        return $this;
    }

    /**
     * Gets the current time on the router.
     *
     * Gets the current time on the router, regardless of the current menu.
     *
     * If the timezone is one known to both RouterOS and PHP, it will be used
     * as the timezone identifier. Otherwise (e.g. "manual"), the current GMT
     * offset will be used as a timezone, without any DST awareness.
     *
     * @return DateTime The current time of the router, as a DateTime object.
     */
    public function getCurrentTime()
    {
        $clock = $this->client->sendSync(
            new Request(
                '/system/clock/print
                .proplist=date,time,time-zone-name,gmt-offset'
            )
        )->current();
        $clockParts = array();
        foreach (array(
            'date',
            'time',
            'time-zone-name',
            'gmt-offset'
        ) as $clockPart) {
            $clockParts[$clockPart] = $clock->getProperty($clockPart);
            if (Stream::isStream($clockParts[$clockPart])) {
                $clockParts[$clockPart] = stream_get_contents(
                    $clockParts[$clockPart]
                );
            }
        }
        $datetime = ucfirst(strtolower($clockParts['date'])) . ' ' .
            $clockParts['time'];
        try {
            $result = DateTime::createFromFormat(
                'M/j/Y H:i:s',
                $datetime,
                new DateTimeZone($clockParts['time-zone-name'])
            );
        } catch (E $e) {
            $result = DateTime::createFromFormat(
                'M/j/Y H:i:s P',
                $datetime . ' ' . $clockParts['gmt-offset'],
                new DateTimeZone('UTC')
            );
        }
        return $result;
    }

    /**
     * Finds the IDs of items at the current menu.
     *
     * Finds the IDs of items based on specified criteria, and returns them as
     * a comma separated string, ready for insertion at a "numbers" argument.
     *
     * Accepts zero or more criteria as arguments. If zero arguments are
     * specified, returns all items' IDs. The value of each criteria can be a
     * number (just as in Winbox), a literal ID to be included, a {@link Query}
     * object, or a callback. If a callback is specified, it is called for each
     * item, with the item as an argument. If it returns a true value, the
     * item's ID is included in the result. Every other value is casted to a
     * string. A string is treated as a comma separated values of IDs, numbers
     * or callback names. Non-existent callback names are instead placed in the
     * result, which may be useful in menus that accept identifiers other than
     * IDs, but note that it can cause errors on other menus.
     *
     * @return string A comma separated list of all items matching the
     *     specified criteria.
     */
    public function find()
    {
        if (func_num_args() === 0) {
            if (null === $this->idCache) {
                $ret = $this->client->sendSync(
                    new Request($this->menu . '/find')
                )->getProperty('ret');
                if (null === $ret) {
                    $this->idCache = array();
                    return '';
                } elseif (!is_string($ret)) {
                    $ret = stream_get_contents($ret);
                }

                $idCache = str_replace(
                    ';',
                    ',',
                    strtolower($ret)
                );
                $this->idCache = explode(',', $idCache);
                return $idCache;
            }
            return implode(',', $this->idCache);
        }
        $idList = '';
        foreach (func_get_args() as $criteria) {
            if ($criteria instanceof Query) {
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print .proplist=.id', $criteria)
                )->getAllOfType(Response::TYPE_DATA) as $response) {
                    $newId = $response->getProperty('.id');
                    $idList .= strtolower(
                        is_string($newId)
                        ? $newId
                        : stream_get_contents($newId) . ','
                    );
                }
            } elseif (is_callable($criteria)) {
                $idCache = array();
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print')
                )->getAllOfType(Response::TYPE_DATA) as $response) {
                    $newId = $response->getProperty('.id');
                    $newId = strtolower(
                        is_string($newId)
                        ? $newId
                        : stream_get_contents($newId)
                    );
                    if ($criteria($response)) {
                        $idList .= $newId . ',';
                    }
                    $idCache[] = $newId;
                }
                $this->idCache = $idCache;
            } else {
                $this->find();
                if (is_int($criteria)) {
                    if (isset($this->idCache[$criteria])) {
                        $idList = $this->idCache[$criteria] . ',';
                    }
                } else {
                    $criteria = (string)$criteria;
                    if ($criteria === (string)(int)$criteria) {
                        if (isset($this->idCache[(int)$criteria])) {
                            $idList .= $this->idCache[(int)$criteria] . ',';
                        }
                    } elseif (false === strpos($criteria, ',')) {
                        $idList .= $criteria . ',';
                    } else {
                        $criteriaArr = explode(',', $criteria);
                        for ($i = count($criteriaArr) - 1; $i >= 0; --$i) {
                            if ('' === $criteriaArr[$i]) {
                                unset($criteriaArr[$i]);
                            } elseif ('*' === $criteriaArr[$i][0]) {
                                $idList .= $criteriaArr[$i] . ',';
                                unset($criteriaArr[$i]);
                            }
                        }
                        if (!empty($criteriaArr)) {
                            $idList .= call_user_func_array(
                                array($this, 'find'),
                                $criteriaArr
                            ) . ',';
                        }
                    }
                }
            }
        }
        return rtrim($idList, ',');
    }

    /**
     * Gets a value of a specified item at the current menu.
     *
     * @param int|string|null|Query $number    A number identifying the target
     *     item. Can also be an ID or (in some menus) name. For menus where
     *     there are no items (e.g. "/system identity"), you can specify NULL.
     *     You can also specify a {@link Query}, in which case the first match
     *     will be considered the target item.
     * @param string|resource|null  $valueName The name of the value to get.
     *     If omitted, or set to NULL, gets all properties of the target item.
     *
     * @return string|resource|null|array The value of the specified
     *     property as a string or as new PHP temp stream if the underlying
     *     {@link Client::isStreamingResponses()} is set to TRUE.
     *     If the property is not set, NULL will be returned.
     *     If $valueName is NULL, returns all properties as an array, where
     *     the result is parsed with {@link Script::parseValueToArray()}.
     *
     * @throws RouterErrorException When the router returns an error response
     *     (e.g. no such item, invalid property, etc.).
     */
    public function get($number, $valueName = null)
    {
        if ($number instanceof Query) {
            $number = explode(',', $this->find($number));
            $number = $number[0];
        } elseif (is_int($number) || ((string)$number === (string)(int)$number)) {
            $this->find();
            if (isset($this->idCache[(int)$number])) {
                $number = $this->idCache[(int)$number];
            } else {
                throw new RouterErrorException(
                    'Unable to resolve number from ID cache (no such item maybe)',
                    RouterErrorException::CODE_CACHE_ERROR
                );
            }
        }

        $request = new Request($this->menu . '/get');
        $request->setArgument('number', $number);
        $request->setArgument('value-name', $valueName);
        $responses = $this->client->sendSync($request);
        if (Response::TYPE_ERROR === $responses->getType()) {
            throw new RouterErrorException(
                'Error getting property',
                RouterErrorException::CODE_GET_ERROR,
                null,
                $responses
            );
        }

        $result = $responses->getProperty('ret');
        if (Stream::isStream($result)) {
            $result = stream_get_contents($result);
        }
        if (null === $valueName) {
            // @codeCoverageIgnoreStart
            //Some earlier RouterOS versions use "," instead of ";" as separator
            //Newer versions can't possibly enter this condition
            if (false === strpos($result, ';')
                && preg_match('/^([^=,]+\=[^=,]*)(?:\,(?1))+$/', $result)
            ) {
                $result = str_replace(',', ';', $result);
            }
            // @codeCoverageIgnoreEnd
            return Script::parseValueToArray('{' . $result . '}');
        }
        return $result;
    }

    /**
     * Enables all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, enables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function enable()
    {
        $responses = $this->doBulk('enable', func_get_args());
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when enabling items',
                RouterErrorException::CODE_ENABLE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Disables all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, disables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function disable()
    {
        $responses = $this->doBulk('disable', func_get_args());
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when disabling items',
                RouterErrorException::CODE_DISABLE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Removes all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, removes all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function remove()
    {
        $responses = $this->doBulk('remove', func_get_args());
        $this->clearIdCache();
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when removing items',
                RouterErrorException::CODE_REMOVE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Comments items.
     *
     * Sets new comments on all items at the current menu
     * which match certain criteria, using the "comment" command.
     *
     * Note that not all menus have a "comment" command. Most notably, those are
     * menus without items in them (e.g. "/system identity"), and menus with
     * fixed items (e.g. "/ip service").
     *
     * @param mixed           $numbers Targeted items. Can be any criteria
     *     accepted by {@link static::find()}.
     * @param string|resource $comment The new comment to set on the item as a
     *     string or a seekable stream.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function comment($numbers, $comment)
    {
        $commentRequest = new Request($this->menu . '/comment');
        $commentRequest->setArgument('comment', $comment);
        $commentRequest->setArgument('numbers', $this->find($numbers));
        $responses = $this->client->sendSync($commentRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when commenting items',
                RouterErrorException::CODE_COMMENT_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Sets new values.
     *
     * Sets new values on certain properties on all items at the current menu
     * which match certain criteria.
     *
     * @param mixed                                           $numbers   Items
     *     to be modified.
     *     Can be any criteria accepted by {@link static::find()} or NULL
     *     in case the menu is one without items (e.g. "/system identity").
     * @param array<string,string|resource>|array<int,string> $newValues An
     *     array with the names of each property to set as an array key, and the
     *     new value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function set($numbers, array $newValues)
    {
        $setRequest = new Request($this->menu . '/set');
        foreach ($newValues as $name => $value) {
            if (is_int($name)) {
                $setRequest->setArgument($value, 'true');
            } else {
                $setRequest->setArgument($name, $value);
            }
        }
        if (null !== $numbers) {
            $setRequest->setArgument('numbers', $this->find($numbers));
        }
        $responses = $this->client->sendSync($setRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when setting items',
                RouterErrorException::CODE_SET_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Alias of {@link static::set()}
     *
     * @param mixed                $numbers   Items to be modified.
     *     Can be any criteria accepted by {@link static::find()} or NULL
     *     in case the menu is one without items (e.g. "/system identity").
     * @param string               $valueName Name of property to be modified.
     * @param string|resource|null $newValue  The new value to set.
     *     If set to NULL, the property is unset.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function edit($numbers, $valueName, $newValue)
    {
        return null === $newValue
            ? $this->unsetValue($numbers, $valueName)
            : $this->set($numbers, array($valueName => $newValue));
    }

    /**
     * Unsets a value of a specified item at the current menu.
     *
     * Equivalent of scripting's "unset" command. The "Value" part in the method
     * name is added because "unset" is a language construct, and thus a
     * reserved word.
     *
     * @param mixed  $numbers   Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param string $valueName The name of the value you want to unset.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function unsetValue($numbers, $valueName)
    {
        $unsetRequest = new Request($this->menu . '/unset');
        $responses = $this->client->sendSync(
            $unsetRequest->setArgument('numbers', $this->find($numbers))
                ->setArgument('value-name', $valueName)
        );
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when unsetting value of items',
                RouterErrorException::CODE_UNSET_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Adds a new item at the current menu.
     *
     * @param array<string,string|resource>|array<int,string> $values Accepts
     *     one or more items to add to the current menu.
     *     The data about each item is specified as an array with the names of
     *     each property as an array key, and the value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     * @param array<string,string|resource>|array<int,string> $...    Additional
     *     items.
     *
     * @return string A comma separated list of the new items' IDs.
     *
     * @throws RouterErrorException When one or more items were not succesfully
     *     added. Note that the response collection will include all replies of
     *     all add commands, including the successful ones, in order.
     */
    public function add(array $values)
    {
        $addRequest = new Request($this->menu . '/add');
        $hasErrors = false;
        $results = array();
        foreach (func_get_args() as $values) {
            if (!is_array($values)) {
                continue;
            }
            foreach ($values as $name => $value) {
                if (is_int($name)) {
                    $addRequest->setArgument($value, 'true');
                } else {
                    $addRequest->setArgument($name, $value);
                }
            }
            $result = $this->client->sendSync($addRequest);
            if (count($result->getAllOfType(Response::TYPE_ERROR)) > 0) {
                $hasErrors = true;
            }
            $results = array_merge($results, $result->toArray());
            $addRequest->removeAllArguments();
        }

        $this->clearIdCache();
        if ($hasErrors) {
            throw new RouterErrorException(
                'Router returned error when adding items',
                RouterErrorException::CODE_ADD_ERROR,
                null,
                new ResponseCollection($results)
            );
        }
        $results = new ResponseCollection($results);
        $idList = '';
        foreach ($results->getAllOfType(Response::TYPE_FINAL) as $final) {
            $idList .= ',' . strtolower($final->getProperty('ret'));
        }
        return substr($idList, 1);
    }

    /**
     * Moves items at the current menu before a certain other item.
     *
     * Moves items before a certain other item. Note that the "move"
     * command is not available on all menus. As a rule of thumb, if the order
     * of items in a menu is irrelevant to their interpretation, there won't
     * be a move command on that menu. If in doubt, check from a terminal.
     *
     * @param mixed $numbers     Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param mixed $destination Item before which the targeted items will be
     *     moved to. Can be any criteria accepted by {@link static::find()}.
     *     If multiple items match the criteria, the targeted items will move
     *     above the first match.
     *     If NULL is given (or this argument is omitted), the targeted items
     *     will be moved to the bottom of the menu.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function move($numbers, $destination = null)
    {
        $moveRequest = new Request($this->menu . '/move');
        $moveRequest->setArgument('numbers', $this->find($numbers));
        if (null !== $destination) {
            $destination = $this->find($destination);
            if (false !== strpos($destination, ',')) {
                $destination = strstr($destination, ',', true);
            }
            $moveRequest->setArgument('destination', $destination);
        }
        $this->clearIdCache();
        $responses = $this->client->sendSync($moveRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when moving items',
                RouterErrorException::CODE_MOVE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Counts items at the current menu.
     *
     * Counts items at the current menu. This executes a dedicated command
     * ("print" with a "count-only" argument) on RouterOS, which is why only
     * queries are allowed as a criteria, in contrast with
     * {@link static::find()}, where numbers and callbacks are allowed also.
     *
     * @param Query|null           $query A query to filter items by.
     *     Without it, all items are included in the count.
     * @param string|resource|null $from  A comma separated list of item IDs.
     *     Any items in the set that still exist at the time of couting
     *     are included in the final tally. Note that the $query filters this
     *     set further (i.e. the item must be in the list AND match the $query).
     *     Leaving the value to NULL means all matching items at the current
     *     menu are included in the count.
     *
     * @return int The number of items, or -1 on failure (e.g. if the
     *     current menu does not have a "print" command or items to be counted).
     */
    public function count(Query $query = null, $from = null)
    {
        $countRequest = new Request(
            $this->menu . '/print count-only=""',
            $query
        );
        $countRequest->setArgument('from', $from);
        $result = $this->client->sendSync($countRequest)->end()
            ->getProperty('ret');

        if (null === $result) {
            return -1;
        }
        if (Stream::isStream($result)) {
            $result = stream_get_contents($result);
        }
        return (int)$result;
    }

    /**
     * Gets all items in the current menu.
     *
     * Gets all items in the current menu, using a print request.
     *
     * @param array<string,string|resource>|array<int,string> $args  Additional
     *     arguments to pass to the request.
     *     Each array key is the name of the argument, and each array value is
     *     the value of the argument to be passed.
     *     Arguments without a value (i.e. empty arguments) can also be
     *     specified using a numeric key, and the name of the argument as the
     *     array value.
     *     The "follow" and "follow-only" arguments are prohibited,
     *     as they would cause a synchronous request to run forever, without
     *     allowing the results to be observed.
     *     If you need to use those arguments, use {@link static::newRequest()},
     *     and pass the resulting {@link Request} to {@link Client::sendAsync()}.
     *     The "count-only" argument is also prohibited, as results from it
     *     would not be consumable. Use {@link static::count()} for that.
     * @param Query|null                                      $query A query to
     *     filter items by.
     *     NULL to get all items.
     *
     * @return ResponseCollection A response collection with all
     *     {@link Response::TYPE_DATA} responses. The collection will be empty
     *     when there are no matching items.
     *
     * @throws NotSupportedException If $args contains prohibited arguments
     *     ("follow", "follow-only" or "count-only").
     *
     * @throws RouterErrorException When there's an error upon attempting to
     *     call the "print" command on the specified menu (e.g. if there's no
     *     "print" command at the menu to begin with).
     */
    public function getAll(array $args = array(), Query $query = null)
    {
        $printRequest = new Request($this->menu . '/print', $query);
        foreach ($args as $name => $value) {
            if (is_int($name)) {
                $printRequest->setArgument($value);
            } else {
                $printRequest->setArgument($name, $value);
            }
        }

        foreach (array('follow', 'follow-only', 'count-only') as $arg) {
            if ($printRequest->getArgument($arg) !== null) {
                throw new NotSupportedException(
                    "The argument '{$arg}' was specified, but is prohibited",
                    NotSupportedException::CODE_ARG_PROHIBITED,
                    null,
                    $arg
                );
            }
        }
        $responses = $this->client->sendSync($printRequest);

        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when reading items',
                RouterErrorException::CODE_GETALL_ERROR,
                null,
                $responses
            );
        }
        return $responses->getAllOfType(Response::TYPE_DATA);
    }

    /**
     * Puts a file on RouterOS's file system.
     *
     * Puts a file on RouterOS's file system, regardless of the current menu.
     * Note that this is a **VERY VERY VERY** time consuming method - it takes a
     * minimum of a little over 4 seconds, most of which are in sleep. It waits
     * 2 seconds after a file is first created (required to actually start
     * writing to the file), and another 2 seconds after its contents is written
     * (performed in order to verify success afterwards).
     * Similarly for removal (when $data is NULL) - there are two seconds in
     * sleep, used to verify the file was really deleted.
     *
     * If you want an efficient way of transferring files, use (T)FTP.
     * If you want an efficient way of removing files, use
     * {@link static::setMenu()} to move to the "/file" menu, and call
     * {@link static::remove()} without performing verification afterwards.
     *
     * @param string               $filename  The filename to write data in.
     * @param string|resource|null $data      The data the file is going to have
     *     as a string or a seekable stream.
     *     Setting the value to NULL removes a file of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param bool                 $overwrite Whether to overwrite the file if
     *     it exists.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function filePutContents($filename, $data, $overwrite = false)
    {
        $printRequest = new Request(
            '/file/print .proplist=""',
            Query::where('name', $filename)
        );
        $fileExists = count($this->client->sendSync($printRequest)) > 1;

        if (null === $data) {
            if (!$fileExists) {
                return false;
            }
            $removeRequest = new Request('/file/remove');
            $this->client->sendSync(
                $removeRequest->setArgument('numbers', $filename)
            );
            //Required for RouterOS to REALLY remove the file.
            sleep(2);
            return !(count($this->client->sendSync($printRequest)) > 1);
        }

        if (!$overwrite && $fileExists) {
            return false;
        }
        $result = $this->client->sendSync(
            $printRequest->setArgument('file', $filename)
        );
        if (count($result->getAllOfType(Response::TYPE_ERROR)) > 0) {
            return false;
        }
        //Required for RouterOS to write the initial file.
        sleep(2);
        $setRequest = new Request('/file/set contents=""');
        $setRequest->setArgument('numbers', $filename);
        $this->client->sendSync($setRequest);
        $this->client->sendSync($setRequest->setArgument('contents', $data));
        //Required for RouterOS to write the file's new contents.
        sleep(2);

        $fileSize = $this->client->sendSync(
            $printRequest->setArgument('file', null)
                ->setArgument('.proplist', 'size')
        )->getProperty('size');
        if (Stream::isStream($fileSize)) {
            $fileSize = stream_get_contents($fileSize);
        }
        if (Communicator::isSeekableStream($data)) {
            return Communicator::seekableStreamLength($data) == $fileSize;
        } else {
            return sprintf('%u', strlen((string)$data)) === $fileSize;
        }
    }

    /**
     * Gets the contents of a specified file.
     *
     * @param string      $filename      The name of the file to get
     *     the contents of.
     * @param string|null $tmpScriptName In order to get the file's contents, a
     *     script is created at "/system script", the source of which is then
     *     overwritten with the file's contents, then retrieved from there,
     *     after which the script is removed.
     *     If this argument is left NULL, a random string,
     *     prefixed with the computer's name, is generated and used
     *     as the script's name.
     *     To eliminate any possibility of name clashes,
     *     you can specify your own name instead.
     *
     * @return string|resource The contents of the file as a string or as
     *     new PHP temp stream if the underlying
     *     {@link Client::isStreamingResponses()} is set to TRUE.
     *
     * @throws RouterErrorException When there's an error with the temporary
     *     script used to get the file, or if the file doesn't exist.
     */
    public function fileGetContents($filename, $tmpScriptName = null)
    {
        try {
            $responses = $this->exec(
                ':error ("&" . [/file get $filename contents]);',
                array('filename' => $filename),
                null,
                $tmpScriptName
            );
            throw new RouterErrorException(
                'Unable to read file through script (no error returned)',
                RouterErrorException::CODE_SCRIPT_FILE_ERROR,
                null,
                $responses
            );
        } catch (RouterErrorException $e) {
            if ($e->getCode() !== RouterErrorException::CODE_SCRIPT_RUN_ERROR) {
                throw $e;
            }
            $message = $e->getResponses()->getAllOfType(Response::TYPE_ERROR)
                ->getProperty('message');
            if (Stream::isStream($message)) {
                $successToken = fread($message, 1/*strlen('&')*/);
                if ('&' === $successToken) {
                    $messageCopy = fopen('php://temp', 'r+b');
                    stream_copy_to_stream($message, $messageCopy);
                    rewind($messageCopy);
                    fclose($message);
                    return $messageCopy;
                }
                rewind($message);
            } elseif (strpos($message, '&') === 0) {
                return substr($message, 1/*strlen('&')*/);
            }
            throw $e;
        }
    }

    /**
     * Performs an action on a bulk of items at the current menu.
     *
     * @param string $command What command to perform.
     * @param array  $args    Zero or more arguments can be specified,
     *     each being a criteria.
     *     If zero arguments are specified, matches all items.
     *     See {@link static::find()} for a description of what criteria are
     *     accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    protected function doBulk($command, array $args = array())
    {
        $bulkRequest = new Request("{$this->menu}/{$command}");
        $bulkRequest->setArgument(
            'numbers',
            call_user_func_array(array($this, 'find'), $args)
        );
        return $this->client->sendSync($bulkRequest);
    }
}


