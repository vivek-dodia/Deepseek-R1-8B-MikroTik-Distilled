# Repository Information
Name: MikrotikUpdateAvailable

# Directory Structure
Directory structure:
└── github_repos/MikrotikUpdateAvailable/
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
    │   │       ├── pack-5ecd6b45e5988e4b72176ce376d95583b224a608.idx
    │   │       └── pack-5ecd6b45e5988e4b72176ce376d95583b224a608.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── djFunctions.rsc
    ├── MikrotikUpdateAvailable-Rework.rsc
    ├── MikrotikUpdateAvailable.rsc
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
	url = https://github.com/DJManas/MikrotikUpdateAvailable.git
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
0000000000000000000000000000000000000000 78c6dca6258a41d184def297119850bde948cb87 vivek-dodia <vivek.dodia@icloud.com> 1738606332 -0500	clone: from https://github.com/DJManas/MikrotikUpdateAvailable.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 78c6dca6258a41d184def297119850bde948cb87 vivek-dodia <vivek.dodia@icloud.com> 1738606332 -0500	clone: from https://github.com/DJManas/MikrotikUpdateAvailable.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 78c6dca6258a41d184def297119850bde948cb87 vivek-dodia <vivek.dodia@icloud.com> 1738606332 -0500	clone: from https://github.com/DJManas/MikrotikUpdateAvailable.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
78c6dca6258a41d184def297119850bde948cb87 refs/remotes/origin/master
bb99efda173661dae06cf7fcaa4f28b2d846bf5b refs/tags/0.9


File: /.git\refs\heads\master
78c6dca6258a41d184def297119850bde948cb87


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
ClearLog.rsc
test.src
Workspace.code-workspace

File: /djFunctions.rsc
# Variable telling, that this script is loaded or not
:global djFunctions true

:global decToHex do={
  # Convert decimal character to hexadecimal
  #----------------------
  # Input:
  #   $number - Decimal Number
  # Return:
  #   Hexadecmial Number
  #----------------------
  # When number is lower than 10, return its value
  if ($number <= 10) do={
    :return $number
  }
  
  # Otherwise count
  :local tempNumber
  :local result
  :set tempNumber $number

  :while ($tempNumber > 0) do={
    # Store remainder
    :local remainder
    :set remainder ($tempNumber % 16)
    # Set new number
    :set tempNumber [:tonum ($tempNumber / 16)]

    # Convert remainder to number
    if ($remainder >= 10) do={
      if ($remainder = 10) do={
        :set result ("A" . $result)
      } else={
        if ($remainder = 11) do={
          :set result ("B" . $result)
        } else={
          if ($remainder = 12) do={
            :set result ("C" . $result)
          } else={
            if ($remainder = 13) do={
              :set result ("D" . $result)
            } else={
              if ($remainder = 14) do={
                :set result ("E" . $result)
              } else={
                :set result ("F" . $result)
              }
            }
          }
        }
      }
    } else={
      :set result ([:tostr $remainder] . $result)
    }
  }

  :return $result
}

:global fileExists do={
  # Check if file exists
  #----------------------
  # Input:
  #   $fileName - fileName of file to check
  # Return:
  #   Boolean whether exist or not
  #----------------------
  # Return if file exists
  :return [:tobool ([ /file find name=$fileName] != "")]
}

:global getDecChar do={
  # Convert hexadecimal character to char
  # Could have used array of values and substitute, but using \hex interpetation
  # which is supported by Mikrotik, although its a little fuzzy.
  #----------------------
  # Input:
  #   $charNumber - Hexadecimal number of character
  # Return:
  #   Character
  #----------------------
  # We will use decToHex function
  :global decToHex
  # Init result variable
  :local result
  # Get hexadecimal number
  :local evalStatement "\"\\$[$decToHex number=$charNumber]\""
  # Create e.g. string "\61", which represents letter a, but return it as a function
  :local function
  :set function [:parse ":tostr $evalStatement"]
  # Substitute function to letter
  :set result [$function]
  # Return letter
  :return $result
}

:global changeService do={
  # Changes service parameters
  #----------------------
  # Input:
  #   $s          - service name
  #   $sParameter - service parameter
  #   $sValue     - parameter value
  #   $sAddrOrig  - bool, if true put $value
  # Return:
  #   Bool, whether changed or not
  #----------------------
  :global stringReplace

  if ($sAddrOrig = nil) do={
    :set $sAddrOrig false
  }


  do {
    # According to the parameter do, only special handling at IP address
    if ($sParameter = "address") do={
      if ($sAddrOrig = false) do={
        # Whether to change value
        :local chValue false
        # Get addresses of the current ftp
        :local ftpAddress [:tostr [/ip service get [find where name=$s] address]]

        # If there is some address, add localhost if not already added
        if ([:len $ftpAddress] > 0) do={
          # Check if value is already in address list
          if (![:tobool [:find [:tostr $ftpAddress] $sValue -1]]) do={
            # Add address
            :set $ftpAddress ($ftpAddress . "," . $sValue)
            # Set if I can change
            :set $chValue true
          }
        } else={
          # We will add value only if service is disabled
          if ([/ip service get [find where name=$s] disabled] = true) do={ 
            # Set value
            :set $ftpAddress $sValue
            # Change flag
            :set $chValue true
          }
        }
              
        # Only when should change
        if ($chValue = true) do={
          # If needed, replace ; with , to save address
          :set $ftpAddress [$stringReplace str=$ftpAddress what=";" with=","]

          # Set new value
          /ip service set [find where name=$s] address=$ftpAddress
        }
      } else={
        :set $sValue [$stringReplace str=$sValue what=";" with=","]
        :put $sValue
        /ip service set [find where name=$s] address=$sValue
      }
    } else={
      :local runScript
      if ($sParameter = "disabled") do={
        :local dsbled
        if ($sValue = true) do={
          :set $dsbled "yes"
        } else={
          :set $dsbled "no"
        }

        [:parse ("/ip service set [find where name=\"$s\"] $sParameter=\"$dsbled\"")]
      } else={
        [:parse "/ip service set [find where name=\"$s\"] $sParameter=\"$sValue\""]
      }
    }
  } on-error {
    :return false
  }

  :return true
}

:global isNewFirmware do={
  # Is new version available?
  #----------------------
  # Input:
  #   N/A
  # Return:
  #   Boolean
  #----------------------
  :return [:tobool ([ /system routerboard get current-firmware ] != [ /system routerboard get upgrade-firmware ])]
}

:global isNewSoftware do={
  # Is new version available?
  #----------------------
  # Input:
  #   N/A
  # Return:
  #   Boolean
  #----------------------
  :return (:tobool ([ /system package update get installed-version ] != [ /system package update get latest-version ]))
}

:global logMessage do={
  # Log into log, maybe raise error
  #----------------------
  # Input:
  #   $message      - Message
  #   $messageType  - Message type info, warning, error, debug, default error
  #----------------------
  # TODO: Handle Debug and Warning messages properly
  if (($messageType = "") || ($messageType = nil)) do={
    :set $messageType "error"
  }

  if ($messageType = "error") do={
    [:parse "/log $messageType \"$message\""]
    :error $message
  } else={
    if ($messageType = "debug") do={
      [:parse ("/log $messageType \"$message\"")]
      :put $message
    } else={
      [:parse ("/log $messageType \"$message\"")]
    }
  }
}

:global prompt do={
  :global getDecChar
  :local result
  :local continueReading true

  # Display message for the user, if defined
  if ($message != nil && $message != "") do={
    :put $message
  }
  :put ""

  do {
    :local actualKey
    :local tmpString
    :set actualKey [ /terminal inkey ]

    # Enter key pressed, exit
    if ($actualKey = 13) do={
      # Check if default value is set
      if ([:len $defaultValues] > 0) do={
        :local canExit false
        :foreach value in=$defaultValues do={
          if ($result = $value) do={
            set canExit true
          }
        }
        :set continueReading (:tobool !$canExit)
      } else={
        :set continueReading false
      }
    } else={
      if ($actualKey = 8) do={
        :set tmpString ""

        for i from=0 to=([:len $result] - 2) do={
          :set tmpString ($tmpString . [:pick $result $i])
        }
        :set result $tmpString
      } else={
        :set result ($result . [$getDecChar charNumber=$actualKey])
      }
    }
    [ /terminal cuu ]
    [ /terminal el ]
    :put $result
  } while=($continueReading = true)

  # TODO: Handle bools properly
  :return $result
}

:global renameFile do={
  # Rename file
  #----------------------
  # Input:
  #   $fromFile - File name
  #   $toFile   - contents
  # Return:
  #   Boolean if moved
  #----------------------
  :global logMessage
  :global changeService
  # Need to create user with password for fetch command
  :local passwd ("\"" . [/system resource get cpu-load] . [/system identity get name] . [/system resource get free-memory] . "\"")

  # Clean, if user exists
  if ([:len [/user find name=("renameFile")]] > 0) do={
    /user remove "renameFile"
  }

  # Clean, if group exists
  if ([:len [/user group find name=("renameFile")]] > 0) do={
    /user group remove "renameFile"
  }
  
  # Create group
  /user group add name=renameFile policy=ftp,read,write comment="File Rename group"
  # Create user
  /user add name=renameFile group=renameFile address=127.0.0.1/32 comment="Rename file" password=[:tostr $passwd] disabled=no

  # Copy
  do {
    # To return back previous version of address
    :local previousAddress [:tostr [/ip service get [find where name="ftp"] address]]
    :local ftpDisabled [/ip service get [find where name="ftp"] disabled]

    # If FTP is disabled, enable it for localhost
    if ($ftpDisabled = true) do={
      :put "Disabled"
      if ([$changeService s="ftp" sParameter="address" sValue="127.0.0.1"] = true) do={
        [$changeService s="ftp" sParameter="disabled" sValue=false]
        :put "Enabling"
      }
    }

    # Rename using fetch command using generated user
    /tool fetch address=127.0.0.1 mode=ftp user=renameFile password=[:tostr $passwd] src-path=$fromFile dst-path=$toFile
    :local tmpString
    for i from=1 to=([:len $fromFile]-1) do={
      :set $tmpString ($tmpString . [:pick $fromFile $i])
    }

    # Remove source file
    /file remove $tmpString
    # Remove user
    /user remove "renameFile"
    # Remove group
    /user group remove "renameFile"

    # If ftp was disabled, disable it again
    if ($ftpDisabled = true) do={
      [$changeService s="ftp" sParameter="address" sValue=$previousAddress sAddrOrig=true]
      [$changeService s="ftp" sParameter="disabled" sValue=true]
    }
  } on-error {
    [$logMessage message="Error in renaming file"]
  }
}

:global shiftDate do={
  ################################################################### func_shiftDate - add days to date
  #  Input: date, days
  #    date - "jan/1/2017"
  #    days - number
  # correct only for years >1918
  ################################################################### uncomment for testing
  #:local date "jan/01/2100"
  #:local days 2560
  ########################################
  :local mdays  {31;28;31;30;31;30;31;31;30;31;30;31}
  :local months {"jan"=1;"feb"=2;"mar"=3;"apr"=4;"may"=5;"jun"=6;"jul"=7;"aug"=8;"sep"=9;"oct"=10;"nov"=11;"dec"=12}
  :local monthr  {"jan";"feb";"mar";"apr";"may";"jun";"jul";"aug";"sep";"oct";"nov";"dec"}

  :local dd [:tonum [:pick $date 4 6]]
  :local yy [:tonum [:pick $date 7 11]]
  :local month [:pick $date 0 3]

  :local mm (:$months->$month)
  :set dd ($dd+$days)

  :local dm [:pick $mdays ($mm-1)]
  :if ($mm=2 && (($yy&3=0 && ($yy/100*100 != $yy)) || $yy/400*400=$yy) ) do={ :set dm 29 }

  :while ($dd>$dm) do={
    :set dd ($dd-$dm)
    :set mm ($mm+1)
    :if ($mm>12) do={
      :set mm 1
      :set yy ($yy+1)
    }
    :set dm [:pick $mdays ($mm-1)]
    :if ($mm=2 &&  (($yy&3=0 && ($yy/100*100 != $yy)) || $yy/400*400=$yy) ) do={ :set dm 29 }
  };
  :local res "$[:pick $monthr ($mm-1)]/"
  :if ($dd<10) do={ :set res ($res."0") }
  :set $res "$res$dd/$yy"
  :return $res
}

:global stringReplace do={
  # Replace substring in string with
  #----------------------
  # Input:
  #   $str  - String to perform replacement
  #   $what = What to replace
  #   $with - String to replace using
  # Return:
  #   New string
  #----------------------
  # TODO: Handle empty input
  :local result
  :local length [:len $what]
  for i from=0 to=([:len $str]-$length) step=1 do={
    :local ch [:pick $str $i ($i+$length)]

    if ($ch = $what) do={
      
      if ([:len $result] = 0) do={
        :set $result $with
      } else={
        :set $result ($result . $with)
      }
    } else={
      if ([:len $result] = 0) do={
        :set $result [:pick $str $i]
      } else={
        :set $result ($result . [:pick $str $i])
      }
    }
  }
  :return $result
}

:global updateFile do={
  # Update file
  #----------------------
  # Input:
  #   $fileName - File name
  #   $contents - contents
  # Return:
  #   Boolean if created
  #----------------------
  # If file doesn't exists, create it
  :global fileExists
  :global logMessage

  if ([$fileExists fileName=$fileName] = false) do={
    :do {
      [:parse "/file print file=\"$fileName\"" ]
    } on-error={
      [$logMessage message=("Error in creating file: " . $fileName)]
    }
    # Wait second just to make sure file is created
    :delay 2
  }
  
  # File will have TXT extension, so I append it to $fileName
  :set $fileName ($fileName . ".txt")

  # Fill contents
  :do {
    #[:parse "/file set \"$fileName\" contents=\"$contents" ]
    /file set $fileName contents=$contents
  } on-error={
    [$logMessage message=("Error in updating file: " . $fileName)]
  }
}

File: /MikrotikUpdateAvailable-Rework.rsc
# Set variable, it will get filled when correct script is loaded
:global djFunctions
# Global variables should also be defined here to use them, still forgeting that
:global gUpdateLastNewVersion
:global gUpdateEmailNotification
:global gUpdateNotificationOnlyOnce
:global gUpdateDoBackup
:global gUpdateAutoInstall
:global gUpdateAutoTime

# When variable not set, execute correct script
if (!$djFunctions) do={
  # !!!! HardCoded, if you need, please change script name here. !!!!
  :execute script="djFunctions"

  # Double check if loaded
  if (!$djFunctions) do={
    :error "Script djFunctions is not present in the system!"
  }
}

# We need to include the functions from djFunctions function to work
:global prompt
:global logMessage
:global fileExists
:global updateFile
:global renameFile
:global isNewFirmware
:global isNewSoftware
:global shiftDate

:local setup do={
  # Setup procedure
  # 1.    Setup /tool e-mail
  # 2.    Check if configuration file exists on flash
  # 2.1   Setup notification receiver address
  # 2.2   Setup flag only once or every run to send notification
  # 2.3   Setup flag automatic update
  :global prompt
  :global logMessage
  :global fileExists
  :global updateFile
  :global renameFile
  :global gUpdateLastNewVersion
  :global gUpdateEmailNotification
  :global gUpdateNotificationOnlyOnce
  :global gUpdateDoBackup
  :global gUpdateAutoInstall
  :global gUpdateAutoTime

  # 1.    Setup /tool e-mail
  # Read SMTP
  if ([/tool e-mail get address] = "0.0.0.0") do={
    :local smtp [$prompt message="Please enter SMTP server:"]

    if ($smtp != "") do={
      [/tool e-mail set address=$smtp]
    }
    
    # Port, default is 25 but I need to ask if its ok
    if ([:len [/tool e-mail get port]] = 0 || [/tool e-mail get port] = 25) do={
      :local port [$prompt message="Please enter SMTP port:"]

      if ($port != "") do={
        [/tool e-mail set port=$port]
      }
    }

    # TLS
    :local tlsDefaultValues {"yes"; "no"; "tls-only"}
    :local tls [$prompt message="TLS, values yes, no, tls-only" defaultValues=$tlsDefaultValues]
    [/tool e-mail set start-tls=$tls]

    # Email from
    # TODO: Email address format check
    if ([/tool e-mail get from] = "" or [/tool e-mail get from] = "<>") do={
      :local emailFrom [$prompt message="Please enter FROM email address:"]

      if ($emailFrom != "") do={
        [/tool e-mail set from=$emailFrom]
      }
    }

    # Login name
    if ([/tool e-mail get user] = "") do={
      :local emailUser [$prompt message="Please enter email account login name:"]

      if ($emailUser != "") do={
        [/tool e-mail set user=$emailUser]
      }
    }

    # Login password
    # TODO: Add asterisks to prompt function
    if ([/tool e-mail get password] = "") do={
      :local emailPass [$prompt message="Please enter email password:"]

      if ($emailPass != "") do={
        [/tool e-mail set password=$emailPass]
      }
    }

    # Send test EMAIL
    /tool e-mail send to=[/tool e-mail get from] subject=("Email configuration: " . [/system identity get name]) body="Test OK!"
  }

  # 2.    Check if configuration file exists on flash
  if ([$fileExists fileName="flash/updateSettings.rsc"] = true) do={
    # Check if variables defined, if not, load script
    # I want to avoid rewrite of variables, when user changes them
    if ($gUpdateEmailNotification = nil or $gUpdateEmailNotification = "") do={
      # Load file, will add script to /system script under name updateSettings
      /import "flash/updateSettings.rsc"
      # Execute the script to load variables
      :execute script="updateSettings"
      # Delete script
      /system script remove "updateSettings"
    }
  } else={
    # Get email to send notifications
    :set gUpdateEmailNotification [$prompt message="Please enter update notification address to send notifications to:"]
    # Set default bool values
    #:set boolDefaultValues {"true"; "false"}
    # Ask for notification only once per vserion (until reboot)
    # TODO: Implement default booleans
    :set gUpdateNotificationOnlyOnce [$prompt message="Notify once per version (true, false):"]
    # Ask for auto install option
    # TODO: Implement default booleans
    :set gUpdateAutoInstall [$prompt message="Automatic installation (true, false):"]
    # Ask for sending backup when updating
    # TODO: Implement default booleans
    :set gUpdateDoBackup [$prompt message="Send backup before upgrading (true, false):"]
    # If autoupdate set time (its not working when assigning to global variable, so I made local
    # it works, but not gets saved into settings file, tried to do :set, but it sets it, but do not upgrade
    # it in variable in environment, strange behavior
    :local autoTime
    if ($gUpdateAutoInstall = true) do={
      # :set autoTime [$prompt message="Please set hour of upgrade HH:MM:SS, leave empty for no Hour"]
      :set gUpdateAutoTime [$prompt message="Please set hour of upgrade HH:MM:SS, leave empty for no Hour"]
    } else={
      :global gUpdateAutoTime ""
    }

    # Prepare configuration file contents
    :local contents ""
    # RSC will add value to /system script
    :set $contents ("/system script\n")
    :set $contents ($contents . "add name=\"updateSettings\" source=\"\n")
    # 2.1   Setup notification receiver address
    :set $contents ($contents . ":global gUpdateEmailNotification \\\"" . $gUpdateEmailNotification . "\\\"\n")
    # 2.2   Setup flag only once or every run to send notification
    :set $contents ($contents . ":global gUpdateNotificationOnlyOnce $gUpdateNotificationOnlyOnce\n")
    # 2.3   Setup flag automatic update
    :set $contents ($contents . ":global gUpdateAutoInstall $gUpdateAutoInstall\n")
    # 2.4   Ask if I should do backup before upgrade
    :set $contents ($contents . ":global gUpdateDoBackup $gUpdateDoBackup\n")
    # 2.5   Deferred time
    :set $contents ($contents . ":global gUpdateAutoTime \\\"" . [:tostr $autoTime] . "\\\"\n")
    :set $contents ($contents . "\"")

    # Write contents to file, only TXT one
    [$updateFile fileName="flash/updateSettings" contents=$contents]
    # Rename file using FTP obfuscation
    [$renameFile fromFile="/flash/updateSettings.txt" toFile="/flash/updateSettings.rsc"]
  }
}

:global notify do={
  # Process notification
  #----------------------
  # Input parms:
  #   $email    => email send notification to
  #   $body     => Message for body
  #   $fileName => File to be sent
  # Return parms:
  #   None
  #----------------------
  if ($fileName = nil or $fileName = "") do={
    [ /tool e-mail send to=$email subject=( [ /system identity get name ] . ": Updates available") body=$body]
  } else={
    [ /tool e-mail send to=$email subject=( [ /system identity get name ] . ": Updates available") body=$body file=$fileName]
  }
}

:local notifyAboutNewSoftware do={
  # Notify about software, for code reusability
  #----------------------
  # Input parms:
  #   $version        => new software version
  #   $withoutBackup  => without backup, used to send backup only once per new version, when notifying every run
  # Return parms:
  #   None
  #----------------------
  # If do backup is set, send it with notification
  # TODO: Think about sending it when upgrading
  # Set parameter
  #if ($withoutBackup = nil or $withoutBackup = "") do={
  #  :local withoutBackup false
  #}
  :global gUpdateDoBackup
  :global gUpdateEmailNotification
  :global notify

  if ($gUpdateDoBackup = true and $withoutBackup = false) do={
    # Do backup
    # prepare password, will be sent in another email
    :local pwd ([/system resource get cpu-load] . [/system identity get name] . [/system resource get free-memory])
    # Prepare file Name
    :local fileName ([ /system identity get name] . " - ". [ /system package update get installed-version ])
    # Create backup
    /system backup save encryption=aes-sha256 password=$pwd name=$fileName
    # Delay is necesary to finish backup and give email time to load the file
    :delay 2
    # Send email
    [$notify email=$gUpdateEmailNotification body=("Version: " . [:tostr $version] . " available! Please see changelogs!\nhttps://mikrotik.com/download/changelogs") fileName=$fileName]
    # Send password in different email, I should check in another mikrotik if the password works, if there is space
    [$notify email=$gUpdateEmailNotification body=("Version: " . [:tostr $version] . "\nPassword: " . $pwd)]
    # Delay before removing
    :delay 2
    # Remove
    /file remove "$fileName"
  } else= {
    # Just notify
    [$notify email=$gUpdateEmailNotification body=("Version: " . [:tostr $version] . " available! Please see changelogs!\nhttps://mikrotik.com/download/changelogs")]
  }
}

# *******************
# *******************
# *** Main script ***
# *******************
# *******************
# Firstly SETUP, if it is not SETUP, it will not work, this needs to be run in terminal, it will not open it
[$setup]

# Get new versions, please notice, that new firmware might get noticed after upgrade of the main packages
/system package update check-for-updates

# Check if software changed
if ([$isNewSoftware] = true) do={
  # Just get new version for further processing
  :local newSoftwareVersion [/system package update get latest-version]

  # Make record in log
  [$logMessage messageType="info" message=("New software available: " . [:tostr $newSoftwareVersion])]
  # Download change logs for sending in an email
  # TODO: Make default different branch than stable
  # TODO: Parse html
  #/tool fetch url="https://mikrotik.com/download/changelogs" dst-path="changelogs.htm"
  
  # Check if already notified to notify, when flag only once pressed
  if (($gUpdateNotificationOnlyOnce = true) || ($gUpdateNotificationOnlyOnce = "true")) do={
    # Check if last version not
    if (($gUpdateLastNewVersion = nil) || ($gUpdateLastNewVersion = "") || ($gUpdateLastNewVersion != $newSoftwareVersion)) do={
      # Set new version, to not process until next update
      :set $gUpdateLastNewVersion $newSoftwareVersion

      [$notifyAboutNewSoftware version=$newSoftwareVersion withoutBackup=false]
    }
  } else {
    # Notify every run
    # Send backup only once per version
    if (($gUpdateLastNewVersion = nil) || ($gUpdateLastNewVersion = "") || ($gUpdateLastNewVersion != $newSoftwareVersion)) do={
      # Set new version, to not process until next update
      :set $gUpdateLastNewVersion $newSoftwareVersion
      [$notifyAboutNewSoftware version=$newSoftwareVersion withoutBackup=false]
    } else={
      [$notifyAboutNewSoftware version=$newSoftwareVersion withoutBackup=true]
    }
  }
  
  if ($gUpdateAutoInstall = true) do={
    if ($gUpdateAutoTime = "") do={
      /system package update download
      /system reboot
    } else={
      :local actualTime [/system clock get time]
      :local actualDate [/system clock get date]
      :local actualHour [:pick $actualTime 0 2]
      :local actualMinute [:pick $actualTime 3 5]
      :local runHour [:pick $gUpdateAutoTime 0 2]
      :local runMinute [:pick $gUpdateAutoTime 3 5]

      # Decide if I should move date 1 day ahead
      :local runDate
      if ($runHour < $actualHour) do={
        :set $runDate [$shiftDate date=$actualDate days=1]
      } else={
        :set $actualMinute ($actualMinute + 2)
        if ($runHour = $actualHour && $runMinute <= $actualMinute) do={
          :set $runDate [$shiftDate date=$actualDate days=1]
        } else={
          :set $runDate $actualDate
        }
      }

      # Prepare update
      /system package update download

      # Prepare reboot script
      if ([:tobool [/system scheduler find where name="performUpdate"]] = true) do={
        # Script exists, change parameters
        /system scheduler set [find where name="performUpdate"] interval="00:00:00"
        /system scheduler set [find where name="performUpdate"] disabled="no"
        /system scheduler set [find where name="performUpdate"] start-date=$runDate
        /system scheduler set [find where name="performUpdate"] start-time=$gUpdateAutoTime
        /system scheduler set [find where name="performUpdate"] on-event="/reboot"
      } else {
        /system scheduler add name="performUpdate" interval="00:00:00" start-date=$runDate start-time=$gUpdateAutoTime on-event="/system reboot"
      }
    }
  }
}

if ([$isNewFirmware] = true) do={
  /system routerboard upgrade
  /system reboot
}


File: /MikrotikUpdateAvailable.rsc
# *** Script setup variables ***
# Email where the notifications will be sent
:local notificationAddress "<your email here>"

# When no updates found, this switches if the script will write it into log
:local logNoUpdates false

# Notify only once per new version of software/firmware
:local onlyOnce true

# When user downloaded software using /system packages download, proceed with reboot
# When this is on and the user has upgraded the reouter, /system routerboard upgrade and reboot
:local update true
# *** Script setup variables ***

# *** Functions ***
# Wrong parameter
:global wrongParm do={
  # Input parms:
  #   func => function
  #   parm => parameter value
  # Return parms:
  #   None
  [ /log error ($func . " function, unknown '" . $parm . "' parameter") ]
  :error ($func ." function, unknown '" . $parm ."' parameter")
}

# Check if file exists
:global fileExists do={
  # Input parms:
  #   about =>
  #     software -> packages
  #     firmware -> firmware
  # Return parms:
  #   true -> file exists
  #   false -> file doesn't exist
  # Check if parameter has correct value
  :global wrongParm;
  :local fileName ""
  if ($about = "software") do={
    :set fileName ($about . "-" . [ /system package update get latest-version ] . ".txt")
  } else={
    if ($about = "firmware") do={
      :set fileName ($about . "-" . [ /system routerboard get upgrade-firmware ] . ".txt")
    } else={
      [$wrongParm func="fileExists" parm="about"]
    }
  }

  # Return if file exists
  :return [:tobool ([ /file find name=$fileName] != "")]
}

# Create file which means that firmware has already been checked
# file is created in memory so after reboot it is deleted
:global createFile do={
  # Input parms:
  # about =>
  #   software -> packages
  #   firmware -> firmware
  # Check if parameter has correct value and create filename
  :global wrongParm
  :local fileName ""
  if ($about = "software") do={
    :set fileName ($about . "-" . [ /system package update get latest-version ])
  } else={
    if ($about = "firmware") do={
      :set fileName ($about . "-" . [ /system routerboard get upgrade-firmware ])
    } else={
      [$wrongParm func="createFile" parm="about"]
    }
  }

  # Create new file with contents of /file print screen
  [ /file print file=$fileName ]
  # Wait second just to make sure file is created
  :delay 1
  # Clear its contents
  :do {
    [ /file set $fileName contents="" ]
  } on-error={ :put "Error" }
}

# Check if email is configured /tool e-mail
:global isEmailConfigured do={
  # Input parms:
  #   None
  # Output:
  #   true -> is configured,
  #   false -> is not configured
  :return (![:tobool ([ /tool e-mail get address ] = "0.0.0.0" and [ /tool e-mail get from] = "<>")])
}

# Compare versions
:global isNewVersion do={
  # Input parms:
  # versionType =>
  #   software -> packages
  #   firmware -> firmware
  # Return parms:
  #   true -> yes new version is available
  #   false -> no new version is NOT available
  :global wrongParm;
  if ($versionType = "software") do={
    :return (:tobool ([ /system package update get installed-version ] != [ /system package update get latest-version ]))
  } else={
    if ($versionType = "firmware") do {
      :return [:tobool ([ /system routerboard get current-firmware ] != [ /system routerboard get upgrade-firmware ])]
    } else={
      [$wrongParm func="isNewVersion" parm="versionType"]
    }
  }
}

# Process notification
:global notify do={
  # Input parms:
  #   addr    => email send notification to
  #   about   => what is new: software or firmware
  #   once    => notify only once
  #   update  => when upgrade file is downloaded manually by user, reboot to upgrade
  # Return parms:
  #   None
  # Check if about has correct value
  :global wrongParm
  :global notifyAbout
  :global createFile
  :global fileExists
  if ($about = "software") do={
  } else={
    if ($about = "firmware") do={
    } else {
      [$wrongParm func="notify" parm="about"]
    }
  }

  # Process notification
  if ($once) do={
    # When not exist, notify
    if (![$fileExists about=$about]) do={
      [$notifyAbout addr=$addr about=$about]
      [$createFile about=$about]
    }
  } else={
    [$notifyAbout addr=$addr about=$about]
  }
}

# Sends notification email and adds line into log
:global notifyAbout do={
  # Input parms:
  #   addr  => email send notification to
  #   about => what is new: software or firmware
  #   once  => notify only once
  # Return parms:
  #   None
  [ /tool e-mail send to=$addr subject=( [ /system identity get name ] . ": New " . $about . " available") ]
  [ /log warning ("New " . $about . " available") ]
}

# Checks if router package upgrade file exists
:global upgradeFileExists do={
  # Input parms
  #   None
  # Return parms:
  #   true  => file exists
  #   false => file doesn't exist
  # Concatenate file
  # routeros-<architecture name>-<new version>.npk
  :local fileName ("routeros-" . [ /system resource get architecture-name ] . "-" . [ /system package update get latest-version ] . ".npk")

  # Return whether the file exists
  :return [:tobool ([ /file find name=$fileName] != "")]
}

# Upgrade
:global upgradeRouter do={
  # Input parms:
  #   about =>
  #     software  => packages
  #     firmware  => firmware
  # Return parms:
  #   None
  # Check if about has correct value
  :global upgradeFileExists;
  :global wrongParm;
  if ($about = "software") do={
    if ([$upgradeFileExists]) do={
      [ /system reboot ]
    }
  } else={
    if ($about = "firmware") do={
      # Upgrade
      [ /system routerboard upgrade ]

      # Reboot
      [ /system reboot ]
    } else {
      [$wrongParm func="notify" parm="about"]
    }
  }
}

# *** Main script ***
# Check if E-Mail is configured, when not, throw error
# Notice this only checks if some values are filled in, it doesn't check if the
# router really sends the email
if (![$isEmailConfigured]) do={
  # Log to log and then throw error to console and exit
  [ /log error "Please configure /tool e-mail tool for this script to work!!!" ]
  [ :error "Please configure /tool e-mail tool for this script to work!!!" ]
}

# Get new versions, please notice, that new firmware might get noticed after upgrade of the main packages
[ /system package update check-for-updates ]

# Software check
if ([$isNewVersion versionType="software"]) do={
  [$notify addr=$notificationAddress about="software" once=$onlyOnce update=$update]

  if ($update) do={
    [$upgradeRouter about="software"]
  }
} else={
  if ($logNoUpdates) do={
    [ /log info "No new software!" ]
  }

  # Firmware check - It is logical only to upgrade firmware, when no software is found,
  # new software could bring new firmware
  if ([$isNewVersion versionType="firmware"]) do={
    [$notify addr=$notificationAddress about="firmware" once=$onlyOnce update=$update]

    if ($update) do={
      [$upgradeRouter about="firmware"]
    }
  } else={
    if ($logNoUpdates) do={
      [ /log info "No new firmware!" ]
    }
  }
}


File: /README.md
# mikrotikUpdateAvailable - Rework #

This is the new version of the script, which is a little more advanced. But I am letting the original script to be available as well. If you are interested in the previous version, scroll down.

For this script to work you need only 2 things.

1. Create new script named exactly djFunctions in */system scripts*, sure you can rename it, but then you need to rename it in the other script. Then copy contents of file **djFunctions.rsc** into it.

2. Create new script in */system scripts*, name is on you and insert contents of file **MikrotikUpdateAvailable-rework.rsc** into it.

Then open please **New terminal** and insert: **/system script run &lt;name of the script from point 2&gt;**

You you will be prompted for:

- Setting up the values in */tool e-mail*, if not already set. When you set it up, test email will be sent to FROM email.
- Set up the values for correct script run:
  - **Please enter update notification address to send notifications to**: To this address you will be notified about new version,
  - **Notify once per version (true, false)**: If notification, about new version, should be sent once or every time the script is run,
  - **Automatic installation (true, false)**: If update should be installed on script run automatically,
  - **Send backup before upgrading (true, false)**: If actual backup should be sent in the notification,
  - **Please set hour of upgrade HH:MM:SS, leave empty for no Hour**: If auto update is enabled, you will be asked to enter time. So e.g. script will run in 2 a.m., but you can say here, that it should automatically install it at 8 a.m.
- It creates file *flash/updateSettings.rsc*, which is loaded on restart,
- It checks if new updates are available,
- According to settings:
  - Sends emails with actual backup (2 emails, one with backup, second one with generated password),
  - Upgrades software,
  - Restarts or waits for restart,
  - Upgrades firmware (it is ment to plan this on restart)

**Please notice**, that after initial setup it is ok, that this script is run using scheduler.

## More technical view ##

### Variables ###

These variables will be visible in */system script environment* and can be changed there:

- **gUpdateEmailNotification** - Email, where notifications will be sent,
- **gUpdateNotificationOnlyOnce** - (**true**/**false**) If true, notifications will be only once per version, else everytime the script is run and new version is available,
- **gUpdateAutoInstall** - (**true**/**false**) If true, the system will be automatically upgraded, if **gUpdateAutoTime** is set, it will be defered to that time, otherwise it needs to be upgraded manually,
- **gUpdateDoBackup** - (**true**/**false**) Whether to do backup and send it in notification email. If set to true 2 emails will be sent, once notification with backup file, second with password generated for this backup.
- **gUpdateAutoTime** - (HH:MM:SS) If auto update is set, this variable tels when to upgrade. It plans script for reboot for that time. If you run this script at 9 pm and have set this variable to 01:00:00 (should exactly be this pattern), new script will be created and planned for 1 a.m. with /system restart command, the download is done by this script.

**Please notice**:

- true and false should be written exactly in lowercase, also the HH:MM:SS should be held, because I don't do any check so the script will fail if entered incorrectly.
- Each update contains software and firmware, so I recommend 2 schedules of this script:
  - One instance on daily basis, it checks for new versions and informs user, etc.
  - Second instance should be planned on **startup**, will be launched when router reboots, checks if there is new firmware and does the upgrade straight away.

## TODO ##

- Add string functions
  - Email address format check,
  - Splitstring,
- Add asterisks when asking for password,
- Implement default values for setup prompt script,
- Implement bool values (not only true/false),
- Think about sending backup right before upgrade, not in notification,
- Think if it is necessary to send 2 emails, one with backup, second with password,
- Add support for different channels, when sending notification email with URL,
- I am lazy, so I will try to parse the mikrotik changed page to insert changenotes into email body.

---

## MikrotikUpdateAvailable - Old Version ##

---

This script simply checks for firmware/software update and notifies user on specified email address.

You have to configure */tool e-mail* to make this to work. When it is not set, the script raises error into the log and if run in console, it will put it into console.

You can set few variables at the begining of the script:

## :local notificationAddress "**\<your email here\>**" ##

Replace text in quotes with your valid email address.

## :local logNoUpdates false ##

- true - When no updates has been found, write it to */log*
- false - When no updates has been found, do not write it to */log*

## :local onlyOnce true ##

- true - Will notify you only once per new version, it uses */file* memory filename
- false - Will notify you everytime the script is run

## :local update true ##

This option automatically upgrades firmware, when new firmware is available. But when new software is available, it waits until you manually launch */system package update download*. This will tell the script that you want to upgrade router and it will upgrade it on next launch, whether set.

- true - Automatically update on next script runtime, when update available
- false - Do not automatically update on next runtime, when update available


