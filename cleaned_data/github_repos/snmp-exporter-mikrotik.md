# Repository Information
Name: snmp-exporter-mikrotik

# Directory Structure
Directory structure:
└── github_repos/snmp-exporter-mikrotik/
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
    │   │       ├── pack-8b2d6e6c3a0222e3411c09d47d9dfce608d1cbf9.idx
    │   │       └── pack-8b2d6e6c3a0222e3411c09d47d9dfce608d1cbf9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── README.md
    └── snmp.yml


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
	url = https://github.com/Kerwood/snmp-exporter-mikrotik.git
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
0000000000000000000000000000000000000000 1989f7806752b811404603a00813adf997be61ac vivek-dodia <vivek.dodia@icloud.com> 1738606037 -0500	clone: from https://github.com/Kerwood/snmp-exporter-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 1989f7806752b811404603a00813adf997be61ac vivek-dodia <vivek.dodia@icloud.com> 1738606037 -0500	clone: from https://github.com/Kerwood/snmp-exporter-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 1989f7806752b811404603a00813adf997be61ac vivek-dodia <vivek.dodia@icloud.com> 1738606037 -0500	clone: from https://github.com/Kerwood/snmp-exporter-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
1989f7806752b811404603a00813adf997be61ac refs/remotes/origin/master


File: /.git\refs\heads\master
1989f7806752b811404603a00813adf997be61ac


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /README.md
# snmp-exporter-mikrotik
A snmp-exporter configuration for Mikrotik devices


File: /snmp.yml
mikrotik:
  walk:
  - 1.3.6.1.2.1.17.1.1
  - 1.3.6.1.2.1.17.2.1
  - 1.3.6.1.2.1.17.2.2
  - 1.3.6.1.2.1.17.4.3.1.1
  - 1.3.6.1.2.1.17.4.3.1.2
  - 1.3.6.1.2.1.17.4.3.1.3
  - 1.3.6.1.2.1.2.2.1.1
  - 1.3.6.1.2.1.2.2.1.10
  - 1.3.6.1.2.1.2.2.1.11
  - 1.3.6.1.2.1.2.2.1.12
  - 1.3.6.1.2.1.2.2.1.13
  - 1.3.6.1.2.1.2.2.1.14
  - 1.3.6.1.2.1.2.2.1.15
  - 1.3.6.1.2.1.2.2.1.16
  - 1.3.6.1.2.1.2.2.1.17
  - 1.3.6.1.2.1.2.2.1.18
  - 1.3.6.1.2.1.2.2.1.19
  - 1.3.6.1.2.1.2.2.1.2
  - 1.3.6.1.2.1.2.2.1.20
  - 1.3.6.1.2.1.2.2.1.21
  - 1.3.6.1.2.1.2.2.1.3
  - 1.3.6.1.2.1.2.2.1.4
  - 1.3.6.1.2.1.2.2.1.5
  - 1.3.6.1.2.1.2.2.1.6
  - 1.3.6.1.2.1.2.2.1.7
  - 1.3.6.1.2.1.2.2.1.8
  - 1.3.6.1.2.1.2.2.1.9
  - 1.3.6.1.2.1.25.1.1
  - 1.3.6.1.2.1.25.2.2
  - 1.3.6.1.2.1.25.2.3.1.1
  - 1.3.6.1.2.1.25.2.3.1.3
  - 1.3.6.1.2.1.25.2.3.1.4
  - 1.3.6.1.2.1.25.2.3.1.5
  - 1.3.6.1.2.1.25.2.3.1.6
  - 1.3.6.1.2.1.25.2.3.1.7
  - 1.3.6.1.2.1.25.3.2.1.1
  - 1.3.6.1.2.1.25.3.2.1.3
  - 1.3.6.1.2.1.25.3.2.1.5
  - 1.3.6.1.2.1.25.3.2.1.6
  - 1.3.6.1.2.1.25.3.3.1.2
  - 1.3.6.1.2.1.31.1.1.1.1
  - 1.3.6.1.2.1.31.1.1.1.10
  - 1.3.6.1.2.1.31.1.1.1.11
  - 1.3.6.1.2.1.31.1.1.1.12
  - 1.3.6.1.2.1.31.1.1.1.13
  - 1.3.6.1.2.1.31.1.1.1.15
  - 1.3.6.1.2.1.31.1.1.1.2
  - 1.3.6.1.2.1.31.1.1.1.3
  - 1.3.6.1.2.1.31.1.1.1.4
  - 1.3.6.1.2.1.31.1.1.1.5
  - 1.3.6.1.2.1.31.1.1.1.6
  - 1.3.6.1.2.1.31.1.1.1.7
  - 1.3.6.1.2.1.31.1.1.1.8
  - 1.3.6.1.2.1.31.1.1.1.9
  - 1.3.6.1.2.1.4.1
  - 1.3.6.1.2.1.4.2
  - 1.3.6.1.2.1.4.20.1.1
  - 1.3.6.1.2.1.4.20.1.2
  - 1.3.6.1.2.1.4.20.1.3
  - 1.3.6.1.2.1.4.20.1.4
  - 1.3.6.1.2.1.4.20.1.5
  - 1.3.6.1.2.1.4.22.1.1
  - 1.3.6.1.2.1.4.22.1.2
  - 1.3.6.1.2.1.4.22.1.3
  - 1.3.6.1.2.1.4.22.1.4
  - 1.3.6.1.2.1.4.24.3
  - 1.3.6.1.2.1.4.24.4.1.1
  - 1.3.6.1.2.1.4.24.4.1.10
  - 1.3.6.1.2.1.4.24.4.1.11
  - 1.3.6.1.2.1.4.24.4.1.12
  - 1.3.6.1.2.1.4.24.4.1.13
  - 1.3.6.1.2.1.4.24.4.1.14
  - 1.3.6.1.2.1.4.24.4.1.15
  - 1.3.6.1.2.1.4.24.4.1.16
  - 1.3.6.1.2.1.4.24.4.1.2
  - 1.3.6.1.2.1.4.24.4.1.3
  - 1.3.6.1.2.1.4.24.4.1.4
  - 1.3.6.1.2.1.4.24.4.1.5
  - 1.3.6.1.2.1.4.24.4.1.6
  - 1.3.6.1.2.1.4.24.4.1.7
  - 1.3.6.1.2.1.4.24.4.1.8
  - 1.3.6.1.2.1.47.1.1.1.1.1
  - 1.3.6.1.2.1.47.1.1.1.1.10
  - 1.3.6.1.2.1.47.1.1.1.1.11
  - 1.3.6.1.2.1.47.1.1.1.1.12
  - 1.3.6.1.2.1.47.1.1.1.1.13
  - 1.3.6.1.2.1.47.1.1.1.1.14
  - 1.3.6.1.2.1.47.1.1.1.1.15
  - 1.3.6.1.2.1.47.1.1.1.1.16
  - 1.3.6.1.2.1.47.1.1.1.1.2
  - 1.3.6.1.2.1.47.1.1.1.1.4
  - 1.3.6.1.2.1.47.1.1.1.1.5
  - 1.3.6.1.2.1.47.1.1.1.1.6
  - 1.3.6.1.2.1.47.1.1.1.1.7
  - 1.3.6.1.2.1.47.1.1.1.1.8
  - 1.3.6.1.2.1.47.1.1.1.1.9
  - 1.3.6.1.4.1.14988.1.1.1.4
  - 1.3.6.1.4.1.14988.1.1.1.6
  - 1.3.6.1.4.1.14988.1.1.11.1.1.2
  - 1.3.6.1.4.1.14988.1.1.11.1.1.3
  - 1.3.6.1.4.1.14988.1.1.11.1.1.4
  - 1.3.6.1.4.1.14988.1.1.11.1.1.5
  - 1.3.6.1.4.1.14988.1.1.11.1.1.6
  - 1.3.6.1.4.1.14988.1.1.11.1.1.7
  - 1.3.6.1.4.1.14988.1.1.11.1.1.8
  - 1.3.6.1.4.1.14988.1.1.13.1
  - 1.3.6.1.4.1.14988.1.1.13.2
  - 1.3.6.1.4.1.14988.1.1.14.1.1.1
  - 1.3.6.1.4.1.14988.1.1.14.1.1.11
  - 1.3.6.1.4.1.14988.1.1.14.1.1.12
  - 1.3.6.1.4.1.14988.1.1.14.1.1.13
  - 1.3.6.1.4.1.14988.1.1.14.1.1.14
  - 1.3.6.1.4.1.14988.1.1.14.1.1.15
  - 1.3.6.1.4.1.14988.1.1.14.1.1.16
  - 1.3.6.1.4.1.14988.1.1.14.1.1.17
  - 1.3.6.1.4.1.14988.1.1.14.1.1.18
  - 1.3.6.1.4.1.14988.1.1.14.1.1.19
  - 1.3.6.1.4.1.14988.1.1.14.1.1.2
  - 1.3.6.1.4.1.14988.1.1.14.1.1.20
  - 1.3.6.1.4.1.14988.1.1.14.1.1.21
  - 1.3.6.1.4.1.14988.1.1.14.1.1.31
  - 1.3.6.1.4.1.14988.1.1.14.1.1.32
  - 1.3.6.1.4.1.14988.1.1.14.1.1.33
  - 1.3.6.1.4.1.14988.1.1.14.1.1.34
  - 1.3.6.1.4.1.14988.1.1.14.1.1.35
  - 1.3.6.1.4.1.14988.1.1.14.1.1.36
  - 1.3.6.1.4.1.14988.1.1.14.1.1.37
  - 1.3.6.1.4.1.14988.1.1.14.1.1.38
  - 1.3.6.1.4.1.14988.1.1.14.1.1.39
  - 1.3.6.1.4.1.14988.1.1.14.1.1.40
  - 1.3.6.1.4.1.14988.1.1.14.1.1.41
  - 1.3.6.1.4.1.14988.1.1.14.1.1.42
  - 1.3.6.1.4.1.14988.1.1.14.1.1.43
  - 1.3.6.1.4.1.14988.1.1.14.1.1.44
  - 1.3.6.1.4.1.14988.1.1.14.1.1.45
  - 1.3.6.1.4.1.14988.1.1.14.1.1.46
  - 1.3.6.1.4.1.14988.1.1.14.1.1.47
  - 1.3.6.1.4.1.14988.1.1.14.1.1.48
  - 1.3.6.1.4.1.14988.1.1.14.1.1.49
  - 1.3.6.1.4.1.14988.1.1.14.1.1.50
  - 1.3.6.1.4.1.14988.1.1.14.1.1.51
  - 1.3.6.1.4.1.14988.1.1.14.1.1.52
  - 1.3.6.1.4.1.14988.1.1.14.1.1.53
  - 1.3.6.1.4.1.14988.1.1.14.1.1.54
  - 1.3.6.1.4.1.14988.1.1.14.1.1.55
  - 1.3.6.1.4.1.14988.1.1.14.1.1.61
  - 1.3.6.1.4.1.14988.1.1.14.1.1.62
  - 1.3.6.1.4.1.14988.1.1.14.1.1.63
  - 1.3.6.1.4.1.14988.1.1.14.1.1.64
  - 1.3.6.1.4.1.14988.1.1.14.1.1.65
  - 1.3.6.1.4.1.14988.1.1.14.1.1.66
  - 1.3.6.1.4.1.14988.1.1.14.1.1.67
  - 1.3.6.1.4.1.14988.1.1.14.1.1.68
  - 1.3.6.1.4.1.14988.1.1.14.1.1.69
  - 1.3.6.1.4.1.14988.1.1.14.1.1.70
  - 1.3.6.1.4.1.14988.1.1.14.1.1.71
  - 1.3.6.1.4.1.14988.1.1.14.1.1.72
  - 1.3.6.1.4.1.14988.1.1.14.1.1.73
  - 1.3.6.1.4.1.14988.1.1.14.1.1.74
  - 1.3.6.1.4.1.14988.1.1.14.1.1.75
  - 1.3.6.1.4.1.14988.1.1.14.1.1.76
  - 1.3.6.1.4.1.14988.1.1.14.1.1.77
  - 1.3.6.1.4.1.14988.1.1.14.1.1.78
  - 1.3.6.1.4.1.14988.1.1.14.1.1.79
  - 1.3.6.1.4.1.14988.1.1.14.1.1.80
  - 1.3.6.1.4.1.14988.1.1.14.1.1.81
  - 1.3.6.1.4.1.14988.1.1.14.1.1.82
  - 1.3.6.1.4.1.14988.1.1.14.1.1.83
  - 1.3.6.1.4.1.14988.1.1.14.1.1.84
  - 1.3.6.1.4.1.14988.1.1.14.1.1.85
  - 1.3.6.1.4.1.14988.1.1.14.1.1.86
  - 1.3.6.1.4.1.14988.1.1.14.1.1.87
  - 1.3.6.1.4.1.14988.1.1.14.1.1.88
  - 1.3.6.1.4.1.14988.1.1.14.1.1.89
  - 1.3.6.1.4.1.14988.1.1.15.1.1.1
  - 1.3.6.1.4.1.14988.1.1.15.1.1.2
  - 1.3.6.1.4.1.14988.1.1.15.1.1.3
  - 1.3.6.1.4.1.14988.1.1.15.1.1.4
  - 1.3.6.1.4.1.14988.1.1.15.1.1.5
  - 1.3.6.1.4.1.14988.1.1.15.1.1.6
  - 1.3.6.1.4.1.14988.1.1.17.1.1.2
  - 1.3.6.1.4.1.14988.1.1.17.1.1.3
  - 1.3.6.1.4.1.14988.1.1.17.1.1.4
  - 1.3.6.1.4.1.14988.1.1.17.1.1.5
  - 1.3.6.1.4.1.14988.1.1.17.1.1.6
  - 1.3.6.1.4.1.14988.1.1.3.10
  - 1.3.6.1.4.1.14988.1.1.3.14
  - 1.3.6.1.4.1.14988.1.1.3.8
  - 1.3.6.1.4.1.14988.1.1.3.9
  - 1.3.6.1.4.1.14988.1.1.4.1
  - 1.3.6.1.4.1.14988.1.1.4.2
  - 1.3.6.1.4.1.14988.1.1.4.3
  - 1.3.6.1.4.1.14988.1.1.4.4
  - 1.3.6.1.4.1.14988.1.1.4.5
  - 1.3.6.1.4.1.14988.1.1.6.1
  - 1.3.6.1.4.1.14988.1.1.7.1
  - 1.3.6.1.4.1.14988.1.1.7.2
  - 1.3.6.1.4.1.14988.1.1.7.3
  - 1.3.6.1.4.1.14988.1.1.7.4
  - 1.3.6.1.4.1.14988.1.1.7.5
  - 1.3.6.1.4.1.14988.1.1.7.6
  - 1.3.6.1.4.1.14988.1.1.7.7
  metrics:
  - name: dot1dBaseBridgeAddress
    oid: 1.3.6.1.2.1.17.1.1
    type: PhysAddress48
    help: The MAC address used by this bridge when it must be referred to in a unique
      fashion - 1.3.6.1.2.1.17.1.1
  - name: dot1dStpProtocolSpecification
    oid: 1.3.6.1.2.1.17.2.1
    type: gauge
    help: An indication of what version of the Spanning Tree Protocol is being run
      - 1.3.6.1.2.1.17.2.1
  - name: dot1dStpPriority
    oid: 1.3.6.1.2.1.17.2.2
    type: gauge
    help: The value of the write-able portion of the Bridge ID (i.e., the first two
      octets of the (8 octet long) Bridge ID) - 1.3.6.1.2.1.17.2.2
  - name: dot1dTpFdbAddress
    oid: 1.3.6.1.2.1.17.4.3.1.1
    type: PhysAddress48
    help: A unicast MAC address for which the bridge has forwarding and/or filtering
      information. - 1.3.6.1.2.1.17.4.3.1.1
    indexes:
    - labelname: dot1dTpFdbAddress
      type: PhysAddress48
      fixed_size: 6
  - name: dot1dTpFdbPort
    oid: 1.3.6.1.2.1.17.4.3.1.2
    type: gauge
    help: Either the value '0', or the port number of the port on which a frame having
      a source address equal to the value of the corresponding instance of dot1dTpFdbAddress
      has been seen - 1.3.6.1.2.1.17.4.3.1.2
    indexes:
    - labelname: dot1dTpFdbAddress
      type: PhysAddress48
      fixed_size: 6
  - name: dot1dTpFdbStatus
    oid: 1.3.6.1.2.1.17.4.3.1.3
    type: gauge
    help: The status of this entry - 1.3.6.1.2.1.17.4.3.1.3
    indexes:
    - labelname: dot1dTpFdbAddress
      type: PhysAddress48
      fixed_size: 6
  - name: ifIndex
    oid: 1.3.6.1.2.1.2.2.1.1
    type: gauge
    help: A unique value, greater than zero, for each interface - 1.3.6.1.2.1.2.2.1.1
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInOctets
    oid: 1.3.6.1.2.1.2.2.1.10
    type: counter
    help: The total number of octets received on the interface, including framing
      characters - 1.3.6.1.2.1.2.2.1.10
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInUcastPkts
    oid: 1.3.6.1.2.1.2.2.1.11
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were not addressed to a multicast or broadcast address at this sub-layer
      - 1.3.6.1.2.1.2.2.1.11
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInNUcastPkts
    oid: 1.3.6.1.2.1.2.2.1.12
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were addressed to a multicast or broadcast address at this sub-layer -
      1.3.6.1.2.1.2.2.1.12
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInDiscards
    oid: 1.3.6.1.2.1.2.2.1.13
    type: counter
    help: The number of inbound packets which were chosen to be discarded even though
      no errors had been detected to prevent their being deliverable to a higher-layer
      protocol - 1.3.6.1.2.1.2.2.1.13
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInErrors
    oid: 1.3.6.1.2.1.2.2.1.14
    type: counter
    help: For packet-oriented interfaces, the number of inbound packets that contained
      errors preventing them from being deliverable to a higher-layer protocol - 1.3.6.1.2.1.2.2.1.14
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInUnknownProtos
    oid: 1.3.6.1.2.1.2.2.1.15
    type: counter
    help: For packet-oriented interfaces, the number of packets received via the interface
      which were discarded because of an unknown or unsupported protocol - 1.3.6.1.2.1.2.2.1.15
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutOctets
    oid: 1.3.6.1.2.1.2.2.1.16
    type: counter
    help: The total number of octets transmitted out of the interface, including framing
      characters - 1.3.6.1.2.1.2.2.1.16
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutUcastPkts
    oid: 1.3.6.1.2.1.2.2.1.17
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were not addressed to a multicast or broadcast address at this sub-layer,
      including those that were discarded or not sent - 1.3.6.1.2.1.2.2.1.17
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutNUcastPkts
    oid: 1.3.6.1.2.1.2.2.1.18
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were addressed to a multicast or broadcast address at this sub-layer,
      including those that were discarded or not sent - 1.3.6.1.2.1.2.2.1.18
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutDiscards
    oid: 1.3.6.1.2.1.2.2.1.19
    type: counter
    help: The number of outbound packets which were chosen to be discarded even though
      no errors had been detected to prevent their being transmitted - 1.3.6.1.2.1.2.2.1.19
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifDescr
    oid: 1.3.6.1.2.1.2.2.1.2
    type: DisplayString
    help: A textual string containing information about the interface - 1.3.6.1.2.1.2.2.1.2
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutErrors
    oid: 1.3.6.1.2.1.2.2.1.20
    type: counter
    help: For packet-oriented interfaces, the number of outbound packets that could
      not be transmitted because of errors - 1.3.6.1.2.1.2.2.1.20
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutQLen
    oid: 1.3.6.1.2.1.2.2.1.21
    type: gauge
    help: The length of the output packet queue (in packets). - 1.3.6.1.2.1.2.2.1.21
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifType
    oid: 1.3.6.1.2.1.2.2.1.3
    type: gauge
    help: The type of interface - 1.3.6.1.2.1.2.2.1.3
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifMtu
    oid: 1.3.6.1.2.1.2.2.1.4
    type: gauge
    help: The size of the largest packet which can be sent/received on the interface,
      specified in octets - 1.3.6.1.2.1.2.2.1.4
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifSpeed
    oid: 1.3.6.1.2.1.2.2.1.5
    type: gauge
    help: An estimate of the interface's current bandwidth in bits per second - 1.3.6.1.2.1.2.2.1.5
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifPhysAddress
    oid: 1.3.6.1.2.1.2.2.1.6
    type: PhysAddress48
    help: The interface's address at its protocol sub-layer - 1.3.6.1.2.1.2.2.1.6
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifAdminStatus
    oid: 1.3.6.1.2.1.2.2.1.7
    type: gauge
    help: The desired state of the interface - 1.3.6.1.2.1.2.2.1.7
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOperStatus
    oid: 1.3.6.1.2.1.2.2.1.8
    type: gauge
    help: The current operational state of the interface - 1.3.6.1.2.1.2.2.1.8
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifLastChange
    oid: 1.3.6.1.2.1.2.2.1.9
    type: gauge
    help: The value of sysUpTime at the time the interface entered its current operational
      state - 1.3.6.1.2.1.2.2.1.9
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: hrSystemUptime
    oid: 1.3.6.1.2.1.25.1.1
    type: gauge
    help: The amount of time since this host was last initialized - 1.3.6.1.2.1.25.1.1
  - name: hrMemorySize
    oid: 1.3.6.1.2.1.25.2.2
    type: gauge
    help: The amount of physical read-write main memory, typically RAM, contained
      by the host. - 1.3.6.1.2.1.25.2.2
  - name: hrStorageIndex
    oid: 1.3.6.1.2.1.25.2.3.1.1
    type: gauge
    help: A unique value for each logical storage area contained by the host. - 1.3.6.1.2.1.25.2.3.1.1
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrStorageDescr
    oid: 1.3.6.1.2.1.25.2.3.1.3
    type: DisplayString
    help: A description of the type and instance of the storage described by this
      entry. - 1.3.6.1.2.1.25.2.3.1.3
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrStorageAllocationUnits
    oid: 1.3.6.1.2.1.25.2.3.1.4
    type: gauge
    help: The size, in bytes, of the data objects allocated from this pool - 1.3.6.1.2.1.25.2.3.1.4
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrStorageSize
    oid: 1.3.6.1.2.1.25.2.3.1.5
    type: gauge
    help: The size of the storage represented by this entry, in units of hrStorageAllocationUnits
      - 1.3.6.1.2.1.25.2.3.1.5
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrStorageUsed
    oid: 1.3.6.1.2.1.25.2.3.1.6
    type: gauge
    help: The amount of the storage represented by this entry that is allocated, in
      units of hrStorageAllocationUnits. - 1.3.6.1.2.1.25.2.3.1.6
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrStorageAllocationFailures
    oid: 1.3.6.1.2.1.25.2.3.1.7
    type: counter
    help: The number of requests for storage represented by this entry that could
      not be honored due to not enough storage - 1.3.6.1.2.1.25.2.3.1.7
    indexes:
    - labelname: hrStorageIndex
      type: gauge
  - name: hrDeviceIndex
    oid: 1.3.6.1.2.1.25.3.2.1.1
    type: gauge
    help: A unique value for each device contained by the host - 1.3.6.1.2.1.25.3.2.1.1
    indexes:
    - labelname: hrDeviceIndex
      type: gauge
  - name: hrDeviceDescr
    oid: 1.3.6.1.2.1.25.3.2.1.3
    type: DisplayString
    help: A textual description of this device, including the device's manufacturer
      and revision, and optionally, its serial number. - 1.3.6.1.2.1.25.3.2.1.3
    indexes:
    - labelname: hrDeviceIndex
      type: gauge
  - name: hrDeviceStatus
    oid: 1.3.6.1.2.1.25.3.2.1.5
    type: gauge
    help: The current operational state of the device described by this row of the
      table - 1.3.6.1.2.1.25.3.2.1.5
    indexes:
    - labelname: hrDeviceIndex
      type: gauge
  - name: hrDeviceErrors
    oid: 1.3.6.1.2.1.25.3.2.1.6
    type: counter
    help: The number of errors detected on this device - 1.3.6.1.2.1.25.3.2.1.6
    indexes:
    - labelname: hrDeviceIndex
      type: gauge
  - name: hrProcessorLoad
    oid: 1.3.6.1.2.1.25.3.3.1.2
    type: gauge
    help: The average, over the last minute, of the percentage of time that this processor
      was not idle - 1.3.6.1.2.1.25.3.3.1.2
    indexes:
    - labelname: hrDeviceIndex
      type: gauge
  - name: ifName
    oid: 1.3.6.1.2.1.31.1.1.1.1
    type: DisplayString
    help: The textual name of the interface - 1.3.6.1.2.1.31.1.1.1.1
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCOutOctets
    oid: 1.3.6.1.2.1.31.1.1.1.10
    type: counter
    help: The total number of octets transmitted out of the interface, including framing
      characters - 1.3.6.1.2.1.31.1.1.1.10
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCOutUcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.11
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were not addressed to a multicast or broadcast address at this sub-layer,
      including those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.11
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCOutMulticastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.12
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were addressed to a multicast address at this sub-layer, including
      those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.12
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCOutBroadcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.13
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were addressed to a broadcast address at this sub-layer, including
      those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.13
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHighSpeed
    oid: 1.3.6.1.2.1.31.1.1.1.15
    type: gauge
    help: An estimate of the interface's current bandwidth in units of 1,000,000 bits
      per second - 1.3.6.1.2.1.31.1.1.1.15
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInMulticastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.2
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were addressed to a multicast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.2
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifInBroadcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.3
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were addressed to a broadcast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.3
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutMulticastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.4
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were addressed to a multicast address at this sub-layer, including
      those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.4
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifOutBroadcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.5
    type: counter
    help: The total number of packets that higher-level protocols requested be transmitted,
      and which were addressed to a broadcast address at this sub-layer, including
      those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.5
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCInOctets
    oid: 1.3.6.1.2.1.31.1.1.1.6
    type: counter
    help: The total number of octets received on the interface, including framing
      characters - 1.3.6.1.2.1.31.1.1.1.6
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCInUcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.7
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were not addressed to a multicast or broadcast address at this sub-layer
      - 1.3.6.1.2.1.31.1.1.1.7
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCInMulticastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.8
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were addressed to a multicast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.8
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ifHCInBroadcastPkts
    oid: 1.3.6.1.2.1.31.1.1.1.9
    type: counter
    help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
      which were addressed to a broadcast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.9
    indexes:
    - labelname: ifIndex
      type: gauge
  - name: ipForwarding
    oid: 1.3.6.1.2.1.4.1
    type: gauge
    help: The indication of whether this entity is acting as an IPv4 router in respect
      to the forwarding of datagrams received by, but not addressed to, this entity
      - 1.3.6.1.2.1.4.1
  - name: ipDefaultTTL
    oid: 1.3.6.1.2.1.4.2
    type: gauge
    help: The default value inserted into the Time-To-Live field of the IPv4 header
      of datagrams originated at this entity, whenever a TTL value is not supplied
      by the transport layer protocol - 1.3.6.1.2.1.4.2
  - name: ipAdEntAddr
    oid: 1.3.6.1.2.1.4.20.1.1
    type: IpAddr
    help: The IPv4 address to which this entry's addressing information pertains.
      - 1.3.6.1.2.1.4.20.1.1
    indexes:
    - labelname: ipAdEntAddr
      type: IpAddr
  - name: ipAdEntIfIndex
    oid: 1.3.6.1.2.1.4.20.1.2
    type: gauge
    help: The index value which uniquely identifies the interface to which this entry
      is applicable - 1.3.6.1.2.1.4.20.1.2
    indexes:
    - labelname: ipAdEntAddr
      type: IpAddr
  - name: ipAdEntNetMask
    oid: 1.3.6.1.2.1.4.20.1.3
    type: IpAddr
    help: The subnet mask associated with the IPv4 address of this entry - 1.3.6.1.2.1.4.20.1.3
    indexes:
    - labelname: ipAdEntAddr
      type: IpAddr
  - name: ipAdEntBcastAddr
    oid: 1.3.6.1.2.1.4.20.1.4
    type: gauge
    help: The value of the least-significant bit in the IPv4 broadcast address used
      for sending datagrams on the (logical) interface associated with the IPv4 address
      of this entry - 1.3.6.1.2.1.4.20.1.4
    indexes:
    - labelname: ipAdEntAddr
      type: IpAddr
  - name: ipAdEntReasmMaxSize
    oid: 1.3.6.1.2.1.4.20.1.5
    type: gauge
    help: The size of the largest IPv4 datagram which this entity can re-assemble
      from incoming IPv4 fragmented datagrams received on this interface. - 1.3.6.1.2.1.4.20.1.5
    indexes:
    - labelname: ipAdEntAddr
      type: IpAddr
  - name: ipNetToMediaIfIndex
    oid: 1.3.6.1.2.1.4.22.1.1
    type: gauge
    help: The interface on which this entry's equivalence is effective - 1.3.6.1.2.1.4.22.1.1
    indexes:
    - labelname: ipNetToMediaIfIndex
      type: gauge
    - labelname: ipNetToMediaNetAddress
      type: IpAddr
  - name: ipNetToMediaPhysAddress
    oid: 1.3.6.1.2.1.4.22.1.2
    type: PhysAddress48
    help: The media-dependent `physical' address - 1.3.6.1.2.1.4.22.1.2
    indexes:
    - labelname: ipNetToMediaIfIndex
      type: gauge
    - labelname: ipNetToMediaNetAddress
      type: IpAddr
  - name: ipNetToMediaNetAddress
    oid: 1.3.6.1.2.1.4.22.1.3
    type: IpAddr
    help: The IpAddress corresponding to the media-dependent `physical' address -
      1.3.6.1.2.1.4.22.1.3
    indexes:
    - labelname: ipNetToMediaIfIndex
      type: gauge
    - labelname: ipNetToMediaNetAddress
      type: IpAddr
  - name: ipNetToMediaType
    oid: 1.3.6.1.2.1.4.22.1.4
    type: gauge
    help: The type of mapping - 1.3.6.1.2.1.4.22.1.4
    indexes:
    - labelname: ipNetToMediaIfIndex
      type: gauge
    - labelname: ipNetToMediaNetAddress
      type: IpAddr
  - name: ipCidrRouteNumber
    oid: 1.3.6.1.2.1.4.24.3
    type: gauge
    help: The number of current ipCidrRouteTable entries that are not invalid - 1.3.6.1.2.1.4.24.3
  - name: ipCidrRouteDest
    oid: 1.3.6.1.2.1.4.24.4.1.1
    type: IpAddr
    help: The destination IP address of this route - 1.3.6.1.2.1.4.24.4.1.1
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteNextHopAS
    oid: 1.3.6.1.2.1.4.24.4.1.10
    type: gauge
    help: The Autonomous System Number of the Next Hop - 1.3.6.1.2.1.4.24.4.1.10
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMetric1
    oid: 1.3.6.1.2.1.4.24.4.1.11
    type: gauge
    help: The primary routing metric for this route - 1.3.6.1.2.1.4.24.4.1.11
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMetric2
    oid: 1.3.6.1.2.1.4.24.4.1.12
    type: gauge
    help: An alternate routing metric for this route - 1.3.6.1.2.1.4.24.4.1.12
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMetric3
    oid: 1.3.6.1.2.1.4.24.4.1.13
    type: gauge
    help: An alternate routing metric for this route - 1.3.6.1.2.1.4.24.4.1.13
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMetric4
    oid: 1.3.6.1.2.1.4.24.4.1.14
    type: gauge
    help: An alternate routing metric for this route - 1.3.6.1.2.1.4.24.4.1.14
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMetric5
    oid: 1.3.6.1.2.1.4.24.4.1.15
    type: gauge
    help: An alternate routing metric for this route - 1.3.6.1.2.1.4.24.4.1.15
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteStatus
    oid: 1.3.6.1.2.1.4.24.4.1.16
    type: gauge
    help: The row status variable, used according to row installation and removal
      conventions. - 1.3.6.1.2.1.4.24.4.1.16
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteMask
    oid: 1.3.6.1.2.1.4.24.4.1.2
    type: IpAddr
    help: Indicate the mask to be logical-ANDed with the destination address before
      being compared to the value in the ipCidrRouteDest field - 1.3.6.1.2.1.4.24.4.1.2
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteTos
    oid: 1.3.6.1.2.1.4.24.4.1.3
    type: gauge
    help: The policy specifier is the IP TOS Field - 1.3.6.1.2.1.4.24.4.1.3
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteNextHop
    oid: 1.3.6.1.2.1.4.24.4.1.4
    type: IpAddr
    help: On remote routes, the address of the next system en route; Otherwise, 0.0.0.0.
      - 1.3.6.1.2.1.4.24.4.1.4
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteIfIndex
    oid: 1.3.6.1.2.1.4.24.4.1.5
    type: gauge
    help: The ifIndex value that identifies the local interface through which the
      next hop of this route should be reached. - 1.3.6.1.2.1.4.24.4.1.5
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteType
    oid: 1.3.6.1.2.1.4.24.4.1.6
    type: gauge
    help: The type of route - 1.3.6.1.2.1.4.24.4.1.6
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteProto
    oid: 1.3.6.1.2.1.4.24.4.1.7
    type: gauge
    help: The routing mechanism via which this route was learned - 1.3.6.1.2.1.4.24.4.1.7
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: ipCidrRouteAge
    oid: 1.3.6.1.2.1.4.24.4.1.8
    type: gauge
    help: The number of seconds since this route was last updated or otherwise determined
      to be correct - 1.3.6.1.2.1.4.24.4.1.8
    indexes:
    - labelname: ipCidrRouteDest
      type: IpAddr
    - labelname: ipCidrRouteMask
      type: IpAddr
    - labelname: ipCidrRouteTos
      type: gauge
    - labelname: ipCidrRouteNextHop
      type: IpAddr
  - name: entPhysicalIndex
    oid: 1.3.6.1.2.1.47.1.1.1.1.1
    type: gauge
    help: The index for this entry. - 1.3.6.1.2.1.47.1.1.1.1.1
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalSoftwareRev
    oid: 1.3.6.1.2.1.47.1.1.1.1.10
    type: DisplayString
    help: The vendor-specific software revision string for the physical entity - 1.3.6.1.2.1.47.1.1.1.1.10
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalSerialNum
    oid: 1.3.6.1.2.1.47.1.1.1.1.11
    type: DisplayString
    help: The vendor-specific serial number string for the physical entity - 1.3.6.1.2.1.47.1.1.1.1.11
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalMfgName
    oid: 1.3.6.1.2.1.47.1.1.1.1.12
    type: DisplayString
    help: The name of the manufacturer of this physical component - 1.3.6.1.2.1.47.1.1.1.1.12
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalModelName
    oid: 1.3.6.1.2.1.47.1.1.1.1.13
    type: DisplayString
    help: The vendor-specific model name identifier string associated with this physical
      component - 1.3.6.1.2.1.47.1.1.1.1.13
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalAlias
    oid: 1.3.6.1.2.1.47.1.1.1.1.14
    type: DisplayString
    help: This object is an 'alias' name for the physical entity, as specified by
      a network manager, and provides a non-volatile 'handle' for the physical entity
      - 1.3.6.1.2.1.47.1.1.1.1.14
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalAssetID
    oid: 1.3.6.1.2.1.47.1.1.1.1.15
    type: DisplayString
    help: This object is a user-assigned asset tracking identifier (as specified by
      a network manager) for the physical entity, and provides non-volatile storage
      of this information - 1.3.6.1.2.1.47.1.1.1.1.15
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalIsFRU
    oid: 1.3.6.1.2.1.47.1.1.1.1.16
    type: gauge
    help: This object indicates whether or not this physical entity is considered
      a 'field replaceable unit' by the vendor - 1.3.6.1.2.1.47.1.1.1.1.16
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalDescr
    oid: 1.3.6.1.2.1.47.1.1.1.1.2
    type: DisplayString
    help: A textual description of physical entity - 1.3.6.1.2.1.47.1.1.1.1.2
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalContainedIn
    oid: 1.3.6.1.2.1.47.1.1.1.1.4
    type: gauge
    help: The value of entPhysicalIndex for the physical entity which 'contains' this
      physical entity - 1.3.6.1.2.1.47.1.1.1.1.4
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalClass
    oid: 1.3.6.1.2.1.47.1.1.1.1.5
    type: gauge
    help: An indication of the general hardware type of the physical entity - 1.3.6.1.2.1.47.1.1.1.1.5
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalParentRelPos
    oid: 1.3.6.1.2.1.47.1.1.1.1.6
    type: gauge
    help: An indication of the relative position of this 'child' component among all
      its 'sibling' components - 1.3.6.1.2.1.47.1.1.1.1.6
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalName
    oid: 1.3.6.1.2.1.47.1.1.1.1.7
    type: DisplayString
    help: The textual name of the physical entity - 1.3.6.1.2.1.47.1.1.1.1.7
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalHardwareRev
    oid: 1.3.6.1.2.1.47.1.1.1.1.8
    type: DisplayString
    help: The vendor-specific hardware revision string for the physical entity - 1.3.6.1.2.1.47.1.1.1.1.8
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: entPhysicalFirmwareRev
    oid: 1.3.6.1.2.1.47.1.1.1.1.9
    type: DisplayString
    help: The vendor-specific firmware revision string for the physical entity - 1.3.6.1.2.1.47.1.1.1.1.9
    indexes:
    - labelname: entPhysicalIndex
      type: gauge
  - name: mtxrWlRtabEntryCount
    oid: 1.3.6.1.4.1.14988.1.1.1.4
    type: gauge
    help: Wireless registration table entry count - 1.3.6.1.4.1.14988.1.1.1.4
  - name: mtxrWlCMRtabEntryCount
    oid: 1.3.6.1.4.1.14988.1.1.1.6
    type: gauge
    help: Wireless CAPSMAN registration table entry count - 1.3.6.1.4.1.14988.1.1.1.6
  - name: mtxrNeighborIpAddress
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.2
    type: IpAddr
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.2'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborMacAddress
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.3
    type: PhysAddress48
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.3'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborVersion
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.4
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.4'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborPlatform
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.5
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.5'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborIdentity
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.6
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.6'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborSoftwareID
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.7
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.7'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrNeighborInterfaceID
    oid: 1.3.6.1.4.1.14988.1.1.11.1.1.8
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.8'
    indexes:
    - labelname: mtxrNeighborIndex
      type: gauge
  - name: mtxrWirelessModemSignalStrength
    oid: 1.3.6.1.4.1.14988.1.1.13.1
    type: gauge
    help: signal strength in dBm (if first ppp-client modem supports) - 1.3.6.1.4.1.14988.1.1.13.1
  - name: mtxrWirelessModemSignalECIO
    oid: 1.3.6.1.4.1.14988.1.1.13.2
    type: gauge
    help: signal EC/IO in dB (if first ppp-client modem supports) - 1.3.6.1.4.1.14988.1.1.13.2
  - name: mtxrInterfaceStatsIndex
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.1
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.1'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsDriverRxBytes
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.11
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.11'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsDriverRxPackets
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.12
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.12'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsDriverTxBytes
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.13
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.13'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsDriverTxPackets
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.14
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.14'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx64
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.15
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.15'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx65To127
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.16
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.16'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx128To255
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.17
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.17'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx256To511
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.18
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.18'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx512To1023
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.19
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.19'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsName
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.2
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.2'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx1024To1518
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.20
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.20'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxRx1519ToMax
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.21
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.21'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxBytes
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.31
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.31'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxPackets
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.32
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.32'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxTooShort
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.33
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.33'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx64
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.34
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.34'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx65To127
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.35
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.35'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx128To255
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.36
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.36'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx256To511
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.37
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.37'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx512To1023
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.38
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.38'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx1024To1518
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.39
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.39'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRx1519ToMax
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.40
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.40'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxTooLong
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.41
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.41'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxBroadcast
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.42
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.42'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxPause
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.43
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.43'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxMulticast
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.44
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.44'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxFCSError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.45
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.45'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxAlignError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.46
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.46'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxFragment
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.47
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.47'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxOverflow
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.48
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.48'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxControl
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.49
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.49'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxUnknownOp
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.50
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.50'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxLengthError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.51
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.51'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxCodeError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.52
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.52'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxCarrierError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.53
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.53'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxJabber
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.54
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.54'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsRxDrop
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.55
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.55'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxBytes
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.61
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.61'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxPackets
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.62
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.62'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxTooShort
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.63
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.63'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx64
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.64
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.64'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx65To127
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.65
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.65'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx128To255
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.66
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.66'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx256To511
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.67
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.67'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx512To1023
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.68
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.68'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx1024To1518
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.69
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.69'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTx1519ToMax
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.70
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.70'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxTooLong
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.71
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.71'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxBroadcast
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.72
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.72'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxPause
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.73
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.73'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxMulticast
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.74
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.74'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxUnderrun
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.75
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.75'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.76
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.76'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxExcessiveCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.77
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.77'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxMultipleCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.78
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.78'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxSingleCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.79
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.79'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxExcessiveDeferred
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.80
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.80'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxDeferred
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.81
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.81'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxLateCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.82
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.82'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxTotalCollision
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.83
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.83'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxPauseHonored
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.84
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.84'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxDrop
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.85
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.85'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxJabber
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.86
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.86'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxFCSError
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.87
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.87'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxControl
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.88
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.88'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrInterfaceStatsTxFragment
    oid: 1.3.6.1.4.1.14988.1.1.14.1.1.89
    type: counter
    help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.89'
    indexes:
    - labelname: mtxrInterfaceStatsIndex
      type: gauge
  - name: mtxrPOEInterfaceIndex
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.1
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.1'
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPOEName
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.2
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.2'
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPOEStatus
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.3
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.3'
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPOEVoltage
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.4
    type: gauge
    help: V - 1.3.6.1.4.1.14988.1.1.15.1.1.4
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPOECurrent
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.5
    type: gauge
    help: mA - 1.3.6.1.4.1.14988.1.1.15.1.1.5
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPOEPower
    oid: 1.3.6.1.4.1.14988.1.1.15.1.1.6
    type: gauge
    help: W - 1.3.6.1.4.1.14988.1.1.15.1.1.6
    indexes:
    - labelname: mtxrPOEInterfaceIndex
      type: gauge
  - name: mtxrPartitionName
    oid: 1.3.6.1.4.1.14988.1.1.17.1.1.2
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.2'
    indexes:
    - labelname: mtxrPartitionIndex
      type: gauge
  - name: mtxrPartitionSize
    oid: 1.3.6.1.4.1.14988.1.1.17.1.1.3
    type: gauge
    help: MB - 1.3.6.1.4.1.14988.1.1.17.1.1.3
    indexes:
    - labelname: mtxrPartitionIndex
      type: gauge
  - name: mtxrPartitionActive
    oid: 1.3.6.1.4.1.14988.1.1.17.1.1.5
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.5'
    indexes:
    - labelname: mtxrPartitionIndex
      type: gauge
  - name: mtxrPartitionRunning
    oid: 1.3.6.1.4.1.14988.1.1.17.1.1.6
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.6'
    indexes:
    - labelname: mtxrPartitionIndex
      type: gauge
  - name: mtxrHlTemperature
    oid: 1.3.6.1.4.1.14988.1.1.3.10
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.3.10'
  - name: mtxrHlProcessorFrequency
    oid: 1.3.6.1.4.1.14988.1.1.3.14
    type: gauge
    help: Mhz - 1.3.6.1.4.1.14988.1.1.3.14
  - name: mtxrHlVoltage
    oid: 1.3.6.1.4.1.14988.1.1.3.8
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.3.8'
  - name: mtxrHlActiveFan
    oid: 1.3.6.1.4.1.14988.1.1.3.9
    type: DisplayString
    help: ' - 1.3.6.1.4.1.14988.1.1.3.9'
  - name: mtxrLicSoftwareId
    oid: 1.3.6.1.4.1.14988.1.1.4.1
    type: DisplayString
    help: software id - 1.3.6.1.4.1.14988.1.1.4.1
  - name: mtxrLicLevel
    oid: 1.3.6.1.4.1.14988.1.1.4.3
    type: gauge
    help: current key level - 1.3.6.1.4.1.14988.1.1.4.3
  - name: mtxrLicVersion
    oid: 1.3.6.1.4.1.14988.1.1.4.4
    type: DisplayString
    help: software version - 1.3.6.1.4.1.14988.1.1.4.4
  - name: mtxrLicUpgradableTo
    oid: 1.3.6.1.4.1.14988.1.1.4.5
    type: gauge
    help: upgradable to - 1.3.6.1.4.1.14988.1.1.4.5
  - name: mtxrDHCPLeaseCount
    oid: 1.3.6.1.4.1.14988.1.1.6.1
    type: gauge
    help: ' - 1.3.6.1.4.1.14988.1.1.6.1'
  - name: mtxrSystemReboot
    oid: 1.3.6.1.4.1.14988.1.1.7.1
    type: gauge
    help: set non zero to reboot - 1.3.6.1.4.1.14988.1.1.7.1
  - name: mtxrUSBPowerReset
    oid: 1.3.6.1.4.1.14988.1.1.7.2
    type: gauge
    help: switches off usb power for specified amout of seconds - 1.3.6.1.4.1.14988.1.1.7.2
  - name: mtxrSerialNumber
    oid: 1.3.6.1.4.1.14988.1.1.7.3
    type: DisplayString
    help: RouterBOARD serial number - 1.3.6.1.4.1.14988.1.1.7.3
  - name: mtxrFirmwareVersion
    oid: 1.3.6.1.4.1.14988.1.1.7.4
    type: DisplayString
    help: Current firmware version - 1.3.6.1.4.1.14988.1.1.7.4
  - name: mtxrNote
    oid: 1.3.6.1.4.1.14988.1.1.7.5
    type: DisplayString
    help: note - 1.3.6.1.4.1.14988.1.1.7.5
  - name: mtxrBuildTime
    oid: 1.3.6.1.4.1.14988.1.1.7.6
    type: DisplayString
    help: build time - 1.3.6.1.4.1.14988.1.1.7.6
  - name: mtxrFirmwareUpgradeVersion
    oid: 1.3.6.1.4.1.14988.1.1.7.7
    type: DisplayString
    help: Upgrade firmware version - 1.3.6.1.4.1.14988.1.1.7.7


