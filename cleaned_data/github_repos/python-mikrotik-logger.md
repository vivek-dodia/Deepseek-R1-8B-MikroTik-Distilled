# Repository Information
Name: python-mikrotik-logger

# Directory Structure
Directory structure:
└── github_repos/python-mikrotik-logger/
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
    │   │       ├── pack-a17abef3afb52cd43dab1a0e74cc6ad1272bcca8.idx
    │   │       └── pack-a17abef3afb52cd43dab1a0e74cc6ad1272bcca8.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── docs/
    ├── hosts.yml
    ├── main.py
    ├── readme.md
    ├── requirements.txt
    └── src/
        ├── db_.py
        ├── mikrotik_.py
        ├── notif_.py
        └── __init__.py


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
	url = https://github.com/berrabe/python-mikrotik-logger.git
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
0000000000000000000000000000000000000000 366dd3e419e383f8e49ea6605093977cb60fb22d vivek-dodia <vivek.dodia@icloud.com> 1738606064 -0500	clone: from https://github.com/berrabe/python-mikrotik-logger.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 366dd3e419e383f8e49ea6605093977cb60fb22d vivek-dodia <vivek.dodia@icloud.com> 1738606064 -0500	clone: from https://github.com/berrabe/python-mikrotik-logger.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 366dd3e419e383f8e49ea6605093977cb60fb22d vivek-dodia <vivek.dodia@icloud.com> 1738606064 -0500	clone: from https://github.com/berrabe/python-mikrotik-logger.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
51486c2b7bc69797936ce1e2edc8cbea40f1e365 refs/remotes/origin/bugfix_log
5af0ebd7fda793f273de563ef104799e4ef1271c refs/remotes/origin/db-fiture
366dd3e419e383f8e49ea6605093977cb60fb22d refs/remotes/origin/master
4bd5db38c04981723ebcf3f592151a815b602c78 refs/remotes/origin/monitoring_grafana
deb03f230576cfce3e082470061498eba439f1e0 refs/tags/v1.0
^0e2d643597a40ccade4345cc2307cb68231bbfd1
b5124f335b16b5ee2470eab7703af13d032c3f02 refs/tags/v1.0.3
^903983837f44a6fea5e123b268fe7a6c9fb7acc9
e07f8eafcd762a9e00b36c5a23ea4fb123a3c532 refs/tags/v1.1.0
^8a56a522b240ec52c11a55e9fd37deef59388de7
8c80a0d3f7ec44827d5af2e4df8cfe5890a7d385 refs/tags/v1.1.1
^e07bf7f8086ee54785a33a2b5cd0bbaf89dcf8b9
68dc66cf6b78b3fd645221722f7c3acf80c6eb41 refs/tags/v2.0.0
^51486c2b7bc69797936ce1e2edc8cbea40f1e365
b00f9cb550b5ecab30dd1ec802a677cfdb743bde refs/tags/v2.0.1
^37b5dbfa15c91a9ceeda02733a314d7d3913407b
373f60358230d0436efe8e9af6e8d19b2b044dd3 refs/tags/v2.1.0
^490da3929fe67e3f1cb807f9413a3c0170ef0443


File: /.git\refs\heads\master
366dd3e419e383f8e49ea6605093977cb60fb22d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore

# Created by https://www.toptal.com/developers/gitignore/api/python
# Edit at https://www.toptal.com/developers/gitignore?templates=python

### Python ###
# Byte-compiled / optimized / DLL files
File: /hosts.yml
mtk_devices:
  patterns:
    - '- hotspot'
    - '- monitoring'
    - '+ error'
    - '+ logged'
    - '+ warning'
    - '+ link up'
    - '+ link down'
    - '+ rebooted'
    - '+ critical'
    - '+ failure'


  vars:
    telegram_token: 795xxxx:AAExxxxxxxxxxxxxxxxx
    telegran_chatid: '-10xxxxxxxxx'


  hosts:
    host_1:
      mtk_host: 10.0.0.1
      mtk_port: 1707
      mtk_username: monitor
      mtk_password: 123123

    host_2:
      mtk_host: 172.16.177.74
      mtk_port: 22
      mtk_username: monitor
      mtk_password: 123123


File: /main.py
"""
python mikrotik logger

read the docs :
- https://github.com/berrabe/python-mikrotik-logger.git

created by berrabe
"""

import time
import logging
import sys
import yaml
from src import mikrotik_, notif_

logger = logging.getLogger(__name__)

if __name__ == '__main__':
	try:

		logging.basicConfig(
			level = logging.INFO,
			filename='python-mikrotik-logger.log', filemode='a',
			format = '[ %(levelname)s ] [ %(name)-23s ] [ %(asctime)s ] => %(message)s',
			datefmt='%d-%b-%y %H:%M:%S'
			)


		with open('hosts.yml') as yaml_:
			confs = yaml.load_all(yaml_, Loader=yaml.FullLoader)

			for conf in confs:
				conf = conf.get('mtk_devices')

				hosts = conf['hosts']
				patterns = conf['patterns']
				var = conf['vars']


				for host in hosts.keys():
					start_time = time.time()
					logger.info("================== Logger Start @ %s ==================", ''.join(hosts[host]['mtk_host'][:]))

					MikrotikLogger = mikrotik_.MikrotikLogger(
						pattern = patterns,
						host = hosts[host]['mtk_host'],
						port = hosts[host]['mtk_port'],
						username = hosts[host]['mtk_username'],
						password = hosts[host]['mtk_password'])

					Notif = notif_.Notif(host = hosts[host]['mtk_host'])
					Notif.telegram_notif(
						token = var['telegram_token'],
						chatid = var['telegran_chatid'])

					logger.info("================== Done @ %.2f Second ==================\n\n", time.time() - start_time)

	except KeyboardInterrupt:
		sys.exit(17)


File: /readme.md
<p align="center">
  <img src="docs/logo.png">
</p>

<br/><br/>
### TLDR;
---
This python program is used to monitor, filter, and trigger log events on MikroTik RouterOS devices

the way this program works is quite simple, first this program will take logs on the MikroTik Device by making an ssh connection.

secondly, the program will filter out the word patterns that we have given / setting, for example like this `['- info', '+ ssh']`, with such a pattern, the program will get rid all logs that have the word `info` in it, either in topic and message column. and will keep logs with the word `ssh`, if the log containing the word ssh is 1 or more, the program will send a notification to the telegram bot as an alert

This program can be run anywhere, both Linux, Windows ,MacOS and agentless, meaning on the MikroTik side, no additional tools / scripts / programs are needed, **all you need is to allow ssh access to the MikroTik Device**


<br/><br/>
### MikroTik Configuration
---
I recommend some settings for mikrotik device(s) so that the python-mikrotik-logger program can work smoothly
- First, move all log storage modes from default (memory) to disk, this is highly recommended considering mikrotik will clear all logs if the router shuts down / reboot
```sh
# add action mode called PythonMikrotikLogger
> /system logging action add name="PythonMikrotikLogger" target=disk disk-file-name="PythonMikrotikLogger" disk-lines-per-file=2000 disk-file-count=1 disk-stop-on-full=no

# change all log topic to PythonMikrotikLogger action
> /system logging set [/system logging find where action!="PythonMikrotikLogger"] action=PythonMikrotikLogger
```

- Second, for security reasons, create a user with restricted permissions only to ssh and retrieve logs
```sh
# add group called monitoring
> /user group add name="monitoring" policy=ssh,ftp,read,!local,!telnet,!reboot,!write,!policy,!test,!winbox,!password,!web,!sniff,!sensitive,!api,!romon,!dude,!tikapp skin=default

# add user called monitoring with group monitoring
> /user add name="monitoring" group=monitoring password=<YOUR CUSTOM PASSWORD>
```


<br/><br/>
### USAGE
---
- first step, clone this repo, and do a few steps like the steps below to make sure this program can run perfectly
```sh
> git clone https://github.com/berrabe/python-mikrotik-logger.git
> cd python-mikrotik-logger
> pip install -r requirements.txt
```

- then, we will set some parameters that are used so that this program runs as we want, edit the **hosts.yml** file with your favorite code editor
```yaml
mtk_devices:
  patterns:
    - '- hotspot'
    - '- monitoring'
    - '+ error'
    - '+ logged'
    - '+ warning'
    - '+ link up'
    - '+ link down'
    - '+ rebooted'
    - '+ critical'
    - '+ failure'


  vars:
    telegram_token: < YOUR TELEGRAM TOKEN >
    telegran_chatid: '< YOUR TELEGRAM CHAT ID >'


  hosts:
    host_1:
      mtk_host: < MIKROTIK HOST IP / DOMAIN >
      mtk_port: < MIKROTIK SSH PORT >
      mtk_username: < MIKROTIK LOGIN USERNAME >
      mtk_password: < MIROTIK LOGIN PASSWORD >

```

- lastly, run this program with the command
```sh
> python3 main.py

# if you need some verbose output of what this program is doing
File: /requirements.txt
bcrypt==3.2.0
certifi==2020.6.20
cffi==1.14.3
chardet==3.0.4
cryptography==3.2
idna==2.10
paramiko==2.7.2
pycparser==2.20
PyNaCl==1.4.0
PyYAML==5.3.1
requests==2.24.0
six==1.15.0
urllib3==1.25.11


File: /src\db_.py
"""
This Module Is Used For Handling Database
Separately From Main Module
"""

import sqlite3
import logging
import sys

logger = logging.getLogger(__name__)

class DB():
	"""
	Main Class On This Module
	"""

	def __init__(self, db_table):
		"""
		Initialization Database
		"""

		self.conn = sqlite3.connect('logs.db')
		self.curr = self.conn.cursor()
		self.db_table = db_table

		self.curr.execute(f"""CREATE TABLE IF NOT EXISTS '{self.db_table}_logs' (
		ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		DATE TEXT NULL,
		TIME TEXT NOT NULL,
		CATEGORY TEXT NOT NULL,
		LOG TEXT NOT NULL
		)
		""")

		self.curr.execute(f"""CREATE TABLE IF NOT EXISTS '{self.db_table}_session' (
		ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		DATE TEXT NULL,
		TIME TEXT NOT NULL,
		CATEGORY TEXT NOT NULL,
		LOG TEXT NOT NULL
		)
		""")

		self.curr.execute(f"""CREATE TABLE IF NOT EXISTS '{self.db_table}_notif_tele' (
		ID INTEGER NOT NULL PRIMARY KEY,
		LOG TEXT NOT NULL,
		STATUS TEXT NOT NULL
		)
		""")


	def get_last_session(self):
		"""
		This method is useful for detect the last session from
		SQLite Database ... this method very important for
		method filtering
		"""

		try:
			self.curr.execute(f"SELECT * FROM '{self.db_table}_session' ORDER BY ID DESC LIMIT 1")
			data = self.curr.fetchone()

			if data is None:
				logger.info("Session Log Does Not Exist, Start Filtering New Log From Beginning")
			else:
				logger.info("Session Log Exist")
				return ' '.join(data[1:]).split()

			return 'none'

		except Exception:
			logger.exception("GATHER SESSION FAILED")
			sys.exit(1)


	def insert_filtered_log(self, filtered_log):
		"""
		This method is used to send filtered log to
		the SQLite 3 Database, but before that, it
		will filter if new log from filter is already
		in database or not
		"""

		try:
			if len(filtered_log) != 0:
				logger.info("Checking Database Record, Prevent Duplication")
				self.curr.execute(f"SELECT DATE,TIME,CATEGORY,LOG FROM '{self.db_table}_logs'")
				db_data = self.curr.fetchall()

				for item in filtered_log:
					item.insert(3, ' '.join(item[3:]))
					del item[4:]

					if tuple(item) not in db_data:
						logger.info("Sending To Database (%s)", item)
						self.curr.execute(f"INSERT INTO '{self.db_table}_logs' VALUES (NULL, :date, :time, :cat, :log)",
							{'date' : item[0], 'time' : item[1], 'cat' : item[2], 'log' : " ".join(item[3:])})
					else:
						logger.info("Record (%s) Already In Database", item)

				self.conn.commit()


			else:
				logger.info("Empty Log, Abort Sending Database")

		except Exception:
			logger.exception('INSERT FILTERED LOG ERROR')
			sys.exit(1)


	def insert_latest_session(self, sess_buff):
		"""
		This method is used to send latest gathered
		log from mikrotik device to session db table
		"""

		try:
			self.curr.execute(f"INSERT INTO '{self.db_table}_session' VALUES (NULL, :date, :time, :cat, :log)",
			{'date' : sess_buff[0], 'time' : sess_buff[1], 'cat' : sess_buff[2], 'log' : " ".join(sess_buff[3:])})

			self.conn.commit()
			logger.info("Insert Latest Record to DB For Session")

		except Exception:
			logger.exception('SENDING LATEST SESSION ERROR')
			sys.exit(1)


	def get_new_log_tele(self):
		"""
		This method is used to get new filtered log
		that have not been sended to telegram with
		sql join
		"""

		try:
			self.curr.execute(f"""
				SELECT '{self.db_table}_logs'.ID, '{self.db_table}_logs'.DATE, '{self.db_table}_logs'.TIME, '{self.db_table}_logs'.CATEGORY, '{self.db_table}_logs'.LOG
				FROM '{self.db_table}_logs' 
				LEFT JOIN '{self.db_table}_notif_tele' 
				ON '{self.db_table}_logs'.ID = '{self.db_table}_notif_tele'.ID
				WHERE '{self.db_table}_notif_tele'.STATUS IS NULL
				""")
			data = self.curr.fetchall()

			logger.info("Get New Filtered Log For Sending to Telegram SUCCESS, Total (%s) New Log(s)", len(data))
			return data

		except Exception:
			logger.exception('GET NEW LOG FOR NOTIFIED TELEGRAM ERROR')
			sys.exit(1)


	def insert_new_log_tele(self, id_, log, status):
		"""
		This method is used to insert status for
		telegram notif
		"""

		try:
			self.curr.execute(f"INSERT INTO '{self.db_table}_notif_tele' VALUES (:id, :log, :status)",
			{'id' : id_, 'log' : log, 'status' : status})

			self.conn.commit()
			logger.info("Update Telegram Status For ID (%s) to DB", id_)

		except Exception:
			logger.exception('INSERT NEW LOG FOR TELEGRAM ERROR')
			sys.exit(1)


File: /src\mikrotik_.py
"""
This module is used to parsing telegram log
based on given word pattern, and then
send filtered log to the telegram

created by berrabe
"""

import sys
import os
import logging
import datetime
import paramiko
import src.db_

logger = logging.getLogger(__name__)

class MikrotikLogger():
	"""
	Class Mikrotik Logger
	"""

	def __init__(self, pattern = None, host = "192.168.1.1", port = "22", username = "admin", password = ""):
		"""
		Constructor Class MikrotikLogger,
		when make object form MikrotikClass,
		must provide a list of patterns
		so that the log can be filtered
		"""
		if not os.path.exists('logs'):
			logger.info("Logs Folder Not Exist, Creating")
			os.makedirs('logs')

		if pattern is None:
			pattern = [
			'+ critical',
			'+ down',
			'+ error',
			'+ warning',
			'+ rebooted',
			'+ failure'
			]

		self.filtered_log = []
		self.patterns = pattern
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.date = datetime.datetime.now().strftime("%d-%b-%y")

		self.db_conn = src.db_.DB(self.host.replace('.','_'))
		self.__filtering()


	def __ssh(self):
		"""
		This method is useful for retrieving logs from MikroTik
		device using ssh protocol
		"""

		logger.info("SSH - (%s)", self.host)

		try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(self.host, self.port, self.username, self.password, look_for_keys=False)

			logger.info("SSH => Get Log File")
			sftp = ssh.open_sftp()
			sftp.get('PythonMikrotikLogger.0.txt',f"./logs/log__{self.date}__{self.host}")
			sftp.close()

			log_file = open(f"./logs/log__{self.date}__{self.host}",'r')
			logs = log_file.readlines()
			log_file.close()

			logger.info("SSH => Success")

			return logs

		except Exception:
			logger.exception("SSH TO MIKROTIK ERROR")
			sys.exit(1)


	def __filtering(self):
		"""
		This method is useful filtering log basend given pattern.
		All logs that are filtered will be stored in variables
		self.filtered_log
		"""

		try:
			start = 0
			logs = self.__ssh()
			session = self.db_conn.get_last_session()

			for log in logs:
				if session == log.split() and session != 'none':
					logger.info("Raw Log and Sesion Log Match, Start Filtering New Log From Last Session")
					start = 1
					continue

				if session == 'none' or start == 1:
					for pattern in self.patterns:
						if '-' in pattern.split():
							if ' '.join(pattern.split()[1:]) in log[:]:
								logger.info("Got - (%s) Pattern", ' '.join(pattern.split()[1:]))
								break
						elif '+' in pattern.split():
							if ' '.join(pattern.split()[1:]) in log[:]:
								self.filtered_log.append(log.split())
								logger.info("Got + (%s) Pattern", ' '.join(pattern.split()[1:]))
								break
						else:
							logger.warning("There is some unknown symbol on pattern - !! (%s)", pattern)
							continue
				else:
					continue

			if len(self.filtered_log) != 0:

				logger.info("Got (%s) New Record", len(self.filtered_log))

				self.db_conn.insert_filtered_log(self.filtered_log)

			else:
				logger.info("No New Log Detected")

			sess_buff = logs[-1].split()
			logger.info("Last Record On (%s)", ' '.join(sess_buff))
			self.db_conn.insert_latest_session(sess_buff)

		except Exception:
			logger.exception("FILTERING LOG ERROR")
			sys.exit(1)


	def show(self):
		"""
		This method is used to display all
		filtered logs to the terminal screen
		"""

		if len(self.filtered_log) != 0:
			# [ print(x[:]) for x in self.filtered_log ]
			for log in self.filtered_log:
				print(log[:])


File: /src\notif_.py
"""
This Module Is Used For Handling Notification
Regarding New Filtered Log
"""

import time
import logging
import sys
import requests
import src.db_

logger = logging.getLogger(__name__)

class Notif():
	"""
	Class For Store All Var and Method Used For Notified
	New Filtered Log
	"""

	def __init__(self, host):
		"""
		Initialization Notif Class
		"""

		self.host = host
		self.db_conn = src.db_.DB(self.host.replace('.','_'))


	def telegram_notif(self, token = '', chatid = ''):
		"""
		This method is used to send new filtered log to
		the telegram, via telegram bot
		"""

		try:
			logger.info("Starting Telegram Bot (%s) (%s)", token, chatid)

			new_log = self.db_conn.get_new_log_tele()

			if len(new_log) != 0:
				for log in new_log:

					text = f" [!] {self.host} - {log[0]} \n\n [+] {' '.join(log[1:3])} \n [+] {log[3]} \n\n [=] {' '.join(log[4:])}"

					data = {
						"chat_id" : f"{chatid}",
						"text" : f"<code>{text}</code>",
						"parse_mode" : "html"
					}

					time.sleep(2)

					req_ = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
						data = data,
						timeout = 10)

					if req_.status_code == 200:
						logger.info("Telegram Notif SUCCESS %s", log)
						self.db_conn.insert_new_log_tele(log[0], ' '.join(log[1:]), 'SUCCESS')
					else:
						logger.info("Telegram Notif FAILED %s", log)
						self.db_conn.insert_new_log_tele(log[0], ' '.join(log[1:]), 'FAILED')
			else:
				logger.info('No New Log For Sending To Telegram ... ABORTING')


		except Exception:
			logger.exception('TELEGRAM NOTIF ERROR')
			sys.exit(1)


File: /src\__init__.py
__all__ = ["mikrotik_", "db_", "notif_"]

