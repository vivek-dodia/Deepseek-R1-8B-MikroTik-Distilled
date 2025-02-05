# Repository Information
Name: MikrotikMCP

# Directory Structure
Directory structure:
└── github_repos/MikrotikMCP/
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
    │   │       ├── pack-d0f010e380509108a09e8179b821e3f67b5657a9.idx
    │   │       └── pack-d0f010e380509108a09e8179b821e3f67b5657a9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── FUNDING.yml
    ├── help.txt
    ├── LICENSE
    ├── MMCP.py
    ├── README.md
    ├── requirements.txt
    └── targets.txt


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
	url = https://github.com/DylanAKing/MikrotikMCP.git
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
0000000000000000000000000000000000000000 05902f33323fde50a41ac516826669d5d8b0a1fa vivek-dodia <vivek.dodia@icloud.com> 1738606040 -0500	clone: from https://github.com/DylanAKing/MikrotikMCP.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 05902f33323fde50a41ac516826669d5d8b0a1fa vivek-dodia <vivek.dodia@icloud.com> 1738606040 -0500	clone: from https://github.com/DylanAKing/MikrotikMCP.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 05902f33323fde50a41ac516826669d5d8b0a1fa vivek-dodia <vivek.dodia@icloud.com> 1738606040 -0500	clone: from https://github.com/DylanAKing/MikrotikMCP.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
05902f33323fde50a41ac516826669d5d8b0a1fa refs/remotes/origin/main
b61372a631dc1c332d4d4d7f214d847ec95b13e5 refs/remotes/origin/refactor
7e063d0e6869bcd06683580e2e69acdd8f5cbb10 refs/remotes/origin/refactor-oop
cb82399dc07b741ba715aa67e36c927e20a3ef4d refs/tags/0.2.1
44bb650e21ddcc6926dce1478baebe996d258505 refs/tags/v0.2.0-pre
1bc672c0b3e64d4dc67c1b5363bf6216d4453ecf refs/tags/v0.2.2
3011c5b3c7350788045f3e0f14a5fcaada652b96 refs/tags/v0.2.3
6d6e2d40976e09fba4e4ecb326901cbd4a9068f2 refs/tags/v0.2.4


File: /.git\refs\heads\main
05902f33323fde50a41ac516826669d5d8b0a1fa


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
File: /FUNDING.yml
# These are supported funding model platforms

github: [DylanAKing]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: DylanAKing
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']


File: /help.txt
This software was made to help manage Mikrotik Router os devices. It takes commands provided in the "commands" input field, and gets targets from the "targets" input field, or from a text file. the text file must be formatted with one target per line. After the program has the commands and targets, click submit to run the commands against the listed targets. the program will then ask the user to provide a username and password to authenticate with the targets.
###Disclaimer### This program was developed privately by an independent and is not affiliated with Mikrotik "Mikrotīkls". "Trademarks", "Banners", and "Logos" associated with Mikrotik that are used in this program are property of Mikrotik. Mikrotik will likely offer NO support for this software.
Version: 0.2.4
Build Date: 11/11/2021
Python Version: Python3.9


File: /LICENSE
BSD 3-Clause License

Copyright (c) 2021, Dylan A King
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


File: /MMCP.py
#!/usr/bin/env python3
# This script is intended to push commands to a mass amount of devices.
# Version: 0.2.4

import fnmatch
import re
import os
import tkinter as Tk
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import filedialog
from paramiko import *
import paramiko

# Variables
infile_check, loop, loop2 = 0, 0, 0
targetList = []
dir = os.path.dirname(__file__)
icon = os.path.join(dir, 'mikrotik-icon.png')
bannerPhoto = os.path.join(dir, 'mikrotik-banner.png')
helptext = os.path.join(dir, "help.txt")
blank, stdout_content, cmd, user, match, ssh, infile = '', '', '', '', '', '', ''
logstring = str(':log warning "User ran commands via MikrotikMCP"')


def debug():
    print(commands.get("1.0", "end"))


def connect(host, user, password, loop):
    global ssh
    port = int(sshport.get("1.0", "end"))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
    except AuthenticationException:
        output.configure(state='normal')
        output.insert("1.0", str(loop) + "." + str(loop2) + ": ERROR: Authentication failed.\n")
        output.configure(state='disabled')


def execute(*args):
    global stdout_content, cmd, ssh
    for a in args:
        ssh.exec_command(a)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout_content = stdout.readlines()


def chkPing():
    global cmd, match
    pattern = "ping*"
    match = fnmatch.fnmatch(cmd, pattern)
    if match:
        cmd = cmd[:-1] + " count=3"


def chkOutput():
    global loop2, stdout_content
    print(loop2)
    print(stdout_content)
    pattern2 = "*expected end of command*"
    pattern3 = "*bad command name*"
    chk2 = ['\r\n']

    if len(stdout_content) >= 3:
        index = len(stdout_content) - 2
        output.insert("end", str(loop) + "." + str(loop2) + ": " + stdout_content[index])
        return
    if len(stdout_content) == 0:
        output.insert("end", str(loop) + "." + str(loop2) + ": Success.\n")
    for x in stdout_content:
        match2 = fnmatch.fnmatch(str(stdout_content[loop2]), pattern2)
        match3 = fnmatch.fnmatch(str(stdout_content[loop2]), pattern3)
        print(match2)
        if match2:
            if match:
                output.insert("end", str(loop) + "." + str(loop2) + ": ERROR: Default ping is limited 3\n"
                                                                    "Please remove ping 'count' argument")
            else:
                output.insert("end", str(loop) + "." + str(loop2) + ": ERROR: Expected end of command\n")
        if match3:
            output.insert("end", str(loop) + "." + str(loop2) + ": ERROR: Command unavailable\n")
        if stdout_content[loop2] == chk2[0]:
            output.insert("1.0", str(loop) + "." + str(loop2) + ": Command was sent but status is unknown.\n")
        loop2 += 1
    if loop == len(targetList):
        output.configure(state="disabled")


def submit():
    global user, targetList, infile_check, loop, cmd, loop2
    loop = 0
    output.configure(state="normal")
    output.delete("1.0", "end")
    cmd = commands.get("1.0", "end")
    print(cmd)
    if user == "":
        user = tkinter.simpledialog.askstring("Username", "Please enter username:")
    password = tkinter.simpledialog.askstring("Password", "Please enter password for user: " + user, show='*')
    if infile_check == 0:
        targets = target.get("1.0", "end")
        print(targets)
        trgtlst = re.split(",|;| |\n", targets)
        targetList = trgtlst[:-1]
    for i in targetList:
        loop2 = 0
        loop += 1
        host = str(i)
        chkPing()
        connect(host, user, password, loop)
        execute(logstring, "quit")
        chkOutput()
        # if AuthenticationException:
        #     continue


def browseFiles():
    global infile
    infile = filedialog.askopenfilename(initialdir="~/",
                                        title="Select a File",
                                        filetypes=(("Text files",
                                                    "*.txt*"),
                                                   ("all files",
                                                    "*.*")))


def openfile():
    global infile_check, targetList
    trgtlst = []
    browseFiles()
    loop_check = 1
    with open(infile) as targetFile:
        targets = targetFile.readlines()
        infile_check += 1
        target.delete("1.0", "end")
        target.config(fg="black")
        for line in targets:
            loop_check += 1
            if loop_check < len(targets):
                trgt = line[:-1]
            else:
                trgt = line
            target.insert("end", str(trgt) + "\n")
            trgtlst.append(trgt)
        targetList = trgtlst


# def clearSampleText(field):
#     if field.cget("fg") == 'grey':
#         field.delete("1.0", "end")  # delete all the text in the field
#         field.insert('1.0', '')  # Insert blank for user input
#         field.config(fg='black')


def clearSampleCommand(event):
    if commands.cget('fg') == 'grey':
        commands.delete("1.0", "end")  # delete all the text in the field
        commands.insert('1.0', '')  # Insert blank for user input
        commands.config(fg='black')


def clearSampleTarget(event):
    if target.cget('fg') == 'grey':
        target.delete("1.0", "end")  # delete all the text in the field
        target.config(fg='black')
        target.insert("1.0", '')  # Insert blank for user input


def clearSampleSshPort(event):
    if sshport.cget('fg') == 'grey':
        sshport.delete("1.0", "end")  # delete all the text in the field
        sshport.config(fg='black')
        sshport.insert("1.0", '')  # Insert blank for user input


def enterSampleCommand(event):
    if commands.cget('fg') == 'black':
        if len(commands.get("1.0", "end")) == 1:
            commands.config(fg='grey')
            commands.insert('end', 'Enter commands here')


def enterSampleTarget(event):
    if target.cget('fg') == 'black':
        if len(target.get("1.0", "end")) == 1:
            target.config(fg='grey')
            target.insert('end', '172.0.0.1,172.0.0.2,...')


def enterSampleSshPort(event):
    if sshport.cget('fg') == 'black':
        if len(sshport.get("1.0", "end")) == 1:
            sshport.config(fg='grey')
            sshport.insert('end', '22')


def displayHelp():
    with open(helptext) as help.txt:
        helpDoc = help.txt.readlines()
        tkinter.messagebox.showinfo(title="Help", message=helpDoc)


def changeUser():
    global user
    user = tkinter.simpledialog.askstring("Username", "Please enter username:")


def configureTextbox(name, focusInCMD, focusOutCMD, sampleString):
    name.insert('1.0', sampleString)
    name.bind('<FocusIn>', focusInCMD)
    name.bind('<FocusOut>', focusOutCMD)
    name.config(fg='grey')


# initial setup of GUI window
root = Tk.Tk()
root.title("Mikrotik MCP")
root.wm_iconphoto(False, Tk.PhotoImage(file=icon))
for row in range(2, 5):
    root.rowconfigure(row, weight=1)
for column in range(0, 5):
    root.columnconfigure(column, weight=1)

# Insert graphic as application banner
bannerImage = Tk.PhotoImage(file=bannerPhoto)
banner = Tk.Label(root, image=bannerImage)
banner.grid(row=0, column=1, columnspan=3, padx=12, pady=10)

# Labels
H1 = Tk.Label(text="Mass Command Pusher", font=20)
H1.grid(row=1, column=1, columnspan=3)

H2 = Tk.Label(text="Commands:")
H2.grid(row=2, column=0, padx=10, pady=25)

H3 = Tk.Label(text="Targets:")
H3.grid(row=3, column=0)

H4 = Tk.Label(text="Output:")
H4.grid(row=4, column=0, pady=25)

H5 = Tk.Label(text="SSH Port:")
H5.grid(row=5, column=0, pady=10)

# Textboxes
# create input textbox for commands
commands = Tk.Text(root, bg="white", height=3, width=50)
configureTextbox(commands, clearSampleCommand, enterSampleCommand, "Enter commands here")
commands.grid(row=2, column=1, columnspan=3, sticky='news', pady=10)

# create input textbox for targets
target = Tk.Text(root, bg="white", height=3, width=50)
configureTextbox(target, clearSampleTarget, enterSampleTarget, "172.0.0.1,172.0.0.2,...")
target.grid(row=3, column=1, columnspan=3, pady=10, sticky='news')

# create output textbox
output = Tk.Text(root, bg='white', height=5, width=50)
output.configure(state='disabled')
output.grid(row=4, column=1, columnspan=3, pady=10, sticky='news')

# create input textbox for ssh port
sshport = Tk.Text(root, bg='white', height=1, width=10)
configureTextbox(sshport, clearSampleSshPort, enterSampleSshPort, "22")
sshport.grid(row=5, column=1, sticky='w')

## Buttons
# create load button
loadButton = Tk.Button(root, text="Load", activebackground="light grey", command=lambda: openfile())
loadButton.grid(row=3, column=4, padx=20)

# create submit button
submitButton = Tk.Button(root, text="Submit", activebackground="light grey", command=lambda: submit())
submitButton.grid(row=6, column=3, pady=20)

# create exit button
exitButton = Tk.Button(root, text="Quit", activebackground="light grey", command=lambda: exit())
exitButton.grid(row=6, column=4, padx=10, pady=20)

# create help button
helpButton = Tk.Button(root, text="Help", activebackground="light grey", command=lambda: displayHelp())
helpButton.grid(row=6, column=0, padx=10, pady=20)

# create change user button
userButton = Tk.Button(root, text="Change User", activebackground="light grey", command=lambda: changeUser())
userButton.grid(row=6, column=2, padx=10, pady=20)

root.mainloop()


File: /README.md
# MikrotikMCP
A gui application that uses python to send commands to a mass amount routerOS devices

## Installation

Install the required dependencies by running the following:

```bash
pip install -r requirements.txt
```

## Usage

This code is compatible only with python3. This is a executable script and can be executed by the following:

```bash
./path/to/MMCP.py
```

![Main-window](https://user-images.githubusercontent.com/49817441/140189107-85aa5b07-888a-4830-98fa-862a7c9badc6.png)

This application takes commands and targets and runs the command(s) against all the targets.
Targets can either be enter manually, seperated by commas (ex: 172.0.0.1,172.0.0.2,...,),
or targets can be loaded from a text file, with one target per line. 

![main+commands](https://user-images.githubusercontent.com/49817441/140189135-911a9b76-0c79-435d-a931-8627193d5aa7.png)

It then prompts the for a username and password to login to the targets with.

![username-prompt](https://user-images.githubusercontent.com/49817441/139592843-9c67bb5d-5399-476a-9e05-6b0e625ee0ed.png) ![password-prompt](https://user-images.githubusercontent.com/49817441/139592846-85da2095-d38f-4461-9586-26fcfc3a0abf.png)

Finally displays some general output 
from each system letting you know if the command(s) ran correcctly.

![output](https://user-images.githubusercontent.com/49817441/140189161-17d60d78-32ed-4bbd-b984-98bd38b2e1a1.png)

Additonally it adds a log entry to RouterOS devices informing the user this tool was ran

![routerOS-log](https://user-images.githubusercontent.com/49817441/139593029-20c6b73d-1d38-483b-a972-cb0774add6a0.png)




# Bugs may be encountered at this stage in development


File: /requirements.txt
paramiko==2.8.0


File: /targets.txt



