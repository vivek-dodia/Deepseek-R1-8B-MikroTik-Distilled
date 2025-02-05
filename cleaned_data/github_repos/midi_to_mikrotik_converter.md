# Repository Information
Name: midi_to_mikrotik_converter

# Directory Structure
Directory structure:
└── github_repos/midi_to_mikrotik_converter/
    ├── .clang-format
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
    │   │       ├── pack-d59b533799459d64fa14fe4051ab237689d3d7ea.idx
    │   │       └── pack-d59b533799459d64fa14fe4051ab237689d3d7ea.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── workflows/
    │       └── cmake.yml
    ├── .gitignore
    ├── .gitmodules
    ├── CMakeLists.txt
    ├── conanfile.txt
    ├── conan_provider.cmake
    ├── docs/
    ├── libmidi/
    ├── LICENSE
    ├── README.md
    ├── src/
    │   ├── Config.hpp
    │   ├── midi-to-mikrotik-converter.cpp
    │   ├── MikrotikNote.hpp
    │   ├── MikrotikTrack.hpp
    │   ├── Sequence.hpp
    │   ├── TrackAnalyzer.hpp
    │   └── Utils.hpp
    └── test-files/
        └── midi/
            ├── Imperial March.mid
            ├── Jingle bells.mid
            ├── Jingle bells_original.mid
            ├── Jingle bells_patched.mid
            ├── later_bitches.mid
            ├── later_bitches_test.mid
            ├── long_notes.mid
            ├── overlayed_notes.mid
            ├── overlayed_notes_variant_3.mid
            ├── predelay_fl_test.mid
            ├── skibidi.mid
            ├── two_notes_simultaneously.mid
            └── where_is_my_mind_multilayered.mid


# Content
File: /.clang-format
BasedOnStyle: Microsoft
UseTab: false
IndentWidth: 4
# BreakBeforeBraces: Allman
BreakBeforeBraces: Custom
AllowShortIfStatementsOnASingleLine: false
IndentCaseLabels: false
IndentAccessModifiers: false
AccessModifierOffset: -4
ColumnLimit: 164
IndentExternBlock: NoIndent
BraceWrapping:
  AfterExternBlock: false # <-- And this

# BraceWrapping:
#   AfterExternBlock: true
#   AfterFunction: true
# AlignAfterOpenBracket: DontAlign
# SortIncludes: false


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/altucor/midi_to_mikrotik_converter.git
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
0000000000000000000000000000000000000000 e475f258fb591ede7cbdf807cebbcf83fc1c856e vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/altucor/midi_to_mikrotik_converter.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 e475f258fb591ede7cbdf807cebbcf83fc1c856e vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/altucor/midi_to_mikrotik_converter.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e475f258fb591ede7cbdf807cebbcf83fc1c856e vivek-dodia <vivek.dodia@icloud.com> 1738605951 -0500	clone: from https://github.com/altucor/midi_to_mikrotik_converter.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e475f258fb591ede7cbdf807cebbcf83fc1c856e refs/remotes/origin/master
e5ebfa511949b96048a3313069327eba472c9e25 refs/remotes/origin/move-to-midi-lib
1d5c7ce45941d526a45f776c3d9a5ae451ee578a refs/tags/1.0
a29b8aad9a838713a111f822c7eb7a313a2033fb refs/tags/2
998d8a609e376fb818f6181cc71ee5b011b0b899 refs/tags/3


File: /.git\refs\heads\master
e475f258fb591ede7cbdf807cebbcf83fc1c856e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\workflows\cmake.yml
name: CMake

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

env:
  # Customize the CMake build type here (Release, Debug, RelWithDebInfo, etc.)
  BUILD_TYPE: Release

jobs:
  build-and-release:
    # The CMake configure and build commands are platform agnostic and should work equally well on Windows or Mac.
    # You can convert this to a matrix build if you need cross-platform coverage.
    # See: https://docs.github.com/en/free-pro-team@latest/actions/learn-github-actions/managing-complex-workflows#using-a-build-matrix
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-2019, macos-latest]

    steps:
      - uses: actions/checkout@v4
        with:
          submodules: recursive

      - name: Install boost Linux
        if: runner.os == 'Linux'
        run: |
          sudo apt-get update 
          sudo apt-get install -y libboost-all-dev
          echo "BOOST_ROOT=$(dpkg -L libboost-all-dev | grep '/usr/include/boost')" >> $GITHUB_ENV

      - name: Install Conan Linux
        if: runner.os == 'Linux'
        run: pip install conan --break-system-packages

      - name: Conan version Linux
        if: runner.os == 'Linux'
        run: echo "${{ steps.conan.outputs.version }}"

      - name: Install Conan macOS
        if: runner.os == 'macOS'
        run: brew install conan

      - name: Conan version macOS
        if: runner.os == 'macOS'
        run: echo "${{ steps.conan.outputs.version }}"

      - name: Install boost Windows
        if: runner.os == 'Windows'
        run: choco install -y boost-msvc-14.2 --version 1.86.0

      # Configure CMake in a 'build' subdirectory. `CMAKE_BUILD_TYPE` is only required if you are using a single-configuration generator such as make.
      # See https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html?highlight=cmake_build_type
      - name: Configure CMake Windows
        if: runner.os == 'Windows'
        run: cmake -B ${{github.workspace}}/build -S . -DCMAKE_BUILD_TYPE=${{env.BUILD_TYPE}} -DCMAKE_GENERATOR_TOOLSET=v142
        env:
          BOOST_ROOT: "C:\\local\\boost_1_86_0\\"

      - name: Configure CMake Linux
        if: runner.os == 'Linux'
        run: cmake -B ${{github.workspace}}/build -S . -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=${{github.workspace}}/conan_provider.cmake -DCMAKE_BUILD_TYPE=${{env.BUILD_TYPE}}

      - name: Configure CMake macOS
        if: runner.os == 'macOS'
        run: cmake -B ${{github.workspace}}/build -S . -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=${{github.workspace}}/conan_provider.cmake -DCMAKE_BUILD_TYPE=${{env.BUILD_TYPE}}

      - name: Build
        run: cmake --build ${{github.workspace}}/build --config ${{env.BUILD_TYPE}}

      - name: Test
        working-directory: ${{github.workspace}}/build
        # Execute tests defined by the CMake configuration.
        # See https://cmake.org/cmake/help/latest/manual/ctest.1.html for more detail
        run: ctest -C ${{env.BUILD_TYPE}}

      - name: Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
          tag_name: 3.0
          files: |
            README.md
            LICENSE
            ${{github.workspace}}\build\Release\midi-to-mikrotik-converter-win.exe
            ${{github.workspace}}/build/midi-to-mikrotik-converter-osx
            ${{github.workspace}}/build/midi-to-mikrotik-converter-linux


File: /.gitignore
.vs
.vscode
File: /.gitmodules
[submodule "libmidi"]
	path = libmidi
	url = git@github.com:altucor/libmidi.git
	branch = master


File: /CMakeLists.txt
cmake_minimum_required(VERSION 3.24)

project(midi-to-mikrotik-converter C CXX)

set(CMAKE_CXX_STANDARD 20)

IF(MSVC)
  set(PROJECT_NAME "${PROJECT_NAME}-win")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc /MT")
ELSEIF(APPLE)
  set(PROJECT_NAME "${PROJECT_NAME}-osx")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
ELSEIF(UNIX)
  set(PROJECT_NAME "${PROJECT_NAME}-linux")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
ENDIF()

set(REQUIRED_BOOST_VERSION 1.86.0)

set(BOOST_MIN_VERSION 1.86.0)

IF(CMAKE_BUILD_TYPE MATCHES Debug)
  message("Debug build.")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
ELSEIF(CMAKE_BUILD_TYPE MATCHES Release)
  message("Release build.")
ELSE()
  message(" ! ! ! Unknown build type.")
ENDIF()

message("CMAKEFLAGS DUMP: ${CMAKE_CXX_FLAGS}")

add_subdirectory(libmidi)

set(Boost_DEBUG 1)
set(Boost_USE_STATIC_LIBS ON)
set(Boost_USE_MULTITHREADED ON)
set(Boost_NO_SYSTEM_PATHS TRUE)

IF(MSVC)
  set(Boost_USE_STATIC_RUNTIME ON)
ENDIF()

IF(MSVC)
  find_package(Boost ${BOOST_MIN_VERSION} COMPONENTS program_options log_setup log REQUIRED)
ELSE()
  find_package(Boost CONFIG ${BOOST_MIN_VERSION} COMPONENTS program_options log_setup log REQUIRED)
ENDIF()

include_directories("./libmidi/src")
include_directories(${Boost_INCLUDE_DIRS})
include_directories("./include")

file(GLOB_RECURSE ${PROJECT_NAME}_SOURCES "src/**.cpp" "src/**.hpp")

add_executable(${PROJECT_NAME} ${${PROJECT_NAME}_SOURCES})

IF(MSVC)
  set_property(TARGET ${PROJECT_NAME} PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:>:>")
ENDIF()

IF(MSVC)
  target_link_libraries(${PROJECT_NAME} PRIVATE ${Boost_LIBRARIES} midi)
ELSE()
  target_link_libraries(${PROJECT_NAME} PRIVATE boost_log_setup boost_log ${Boost_LIBRARIES} midi)
ENDIF()


File: /conanfile.txt
[requires]
boost/1.86.0

[layout]
cmake_layout

[generators]
CMakeDeps

File: /conan_provider.cmake
# The MIT License (MIT)
#
# Copyright (c) 2024 JFrog
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

set(CONAN_MINIMUM_VERSION 2.0.5)

# Create a new policy scope and set the minimum required cmake version so the
# features behind a policy setting like if(... IN_LIST ...) behaves as expected
# even if the parent project does not specify a minimum cmake version or a minimum
# version less than this module requires (e.g. 3.0) before the first project() call.
# (see: https://cmake.org/cmake/help/latest/variable/CMAKE_PROJECT_TOP_LEVEL_INCLUDES.html)
#
# The policy-affecting calls like cmake_policy(SET...) or `cmake_minimum_required` only
# affects the current policy scope, i.e. between the PUSH and POP in this case.
#
# https://cmake.org/cmake/help/book/mastering-cmake/chapter/Policies.html#the-policy-stack
cmake_policy(PUSH)
cmake_minimum_required(VERSION 3.24)


function(detect_os os os_api_level os_sdk os_subsystem os_version)
    # it could be cross compilation
    message(STATUS "CMake-Conan: cmake_system_name=${CMAKE_SYSTEM_NAME}")
    if(CMAKE_SYSTEM_NAME AND NOT CMAKE_SYSTEM_NAME STREQUAL "Generic")
        if(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
            set(${os} Macos PARENT_SCOPE)
        elseif(CMAKE_SYSTEM_NAME STREQUAL "QNX")
            set(${os} Neutrino PARENT_SCOPE)
        elseif(CMAKE_SYSTEM_NAME STREQUAL "CYGWIN")
            set(${os} Windows PARENT_SCOPE)
            set(${os_subsystem} cygwin PARENT_SCOPE)
        elseif(CMAKE_SYSTEM_NAME MATCHES "^MSYS")
            set(${os} Windows PARENT_SCOPE)
            set(${os_subsystem} msys2 PARENT_SCOPE)
        else()
            set(${os} ${CMAKE_SYSTEM_NAME} PARENT_SCOPE)
        endif()
        if(CMAKE_SYSTEM_NAME STREQUAL "Android")
            if(DEFINED ANDROID_PLATFORM)
                string(REGEX MATCH "[0-9]+" _os_api_level ${ANDROID_PLATFORM})
            elseif(DEFINED CMAKE_SYSTEM_VERSION)
                set(_os_api_level ${CMAKE_SYSTEM_VERSION})
            endif()
            message(STATUS "CMake-Conan: android api level=${_os_api_level}")
            set(${os_api_level} ${_os_api_level} PARENT_SCOPE)
        endif()
        if(CMAKE_SYSTEM_NAME MATCHES "Darwin|iOS|tvOS|watchOS")
            # CMAKE_OSX_SYSROOT contains the full path to the SDK for MakeFile/Ninja
            # generators, but just has the original input string for Xcode.
            if(NOT IS_DIRECTORY ${CMAKE_OSX_SYSROOT})
                set(_os_sdk ${CMAKE_OSX_SYSROOT})
            else()
                if(CMAKE_OSX_SYSROOT MATCHES Simulator)
                    set(apple_platform_suffix simulator)
                else()
                    set(apple_platform_suffix os)
                endif()
                if(CMAKE_OSX_SYSROOT MATCHES AppleTV)
                    set(_os_sdk "appletv${apple_platform_suffix}")
                elseif(CMAKE_OSX_SYSROOT MATCHES iPhone)
                    set(_os_sdk "iphone${apple_platform_suffix}")
                elseif(CMAKE_OSX_SYSROOT MATCHES Watch)
                    set(_os_sdk "watch${apple_platform_suffix}")
                endif()
            endif()
            if(DEFINED os_sdk)
                message(STATUS "CMake-Conan: cmake_osx_sysroot=${CMAKE_OSX_SYSROOT}")
                set(${os_sdk} ${_os_sdk} PARENT_SCOPE)
            endif()
            if(DEFINED CMAKE_OSX_DEPLOYMENT_TARGET)
                message(STATUS "CMake-Conan: cmake_osx_deployment_target=${CMAKE_OSX_DEPLOYMENT_TARGET}")
                set(${os_version} ${CMAKE_OSX_DEPLOYMENT_TARGET} PARENT_SCOPE)
            endif()
        endif()
    endif()
endfunction()


function(detect_arch arch)
    # CMAKE_OSX_ARCHITECTURES can contain multiple architectures, but Conan only supports one.
    # Therefore this code only finds one. If the recipes support multiple architectures, the
    # build will work. Otherwise, there will be a linker error for the missing architecture(s).
    if(DEFINED CMAKE_OSX_ARCHITECTURES)
        string(REPLACE " " ";" apple_arch_list "${CMAKE_OSX_ARCHITECTURES}")
        list(LENGTH apple_arch_list apple_arch_count)
        if(apple_arch_count GREATER 1)
            message(WARNING "CMake-Conan: Multiple architectures detected, this will only work if Conan recipe(s) produce fat binaries.")
        endif()
    endif()
    if(CMAKE_SYSTEM_NAME MATCHES "Darwin|iOS|tvOS|watchOS" AND NOT CMAKE_OSX_ARCHITECTURES STREQUAL "")
        set(host_arch ${CMAKE_OSX_ARCHITECTURES})
    elseif(MSVC)
        set(host_arch ${CMAKE_CXX_COMPILER_ARCHITECTURE_ID})
    else()
        set(host_arch ${CMAKE_SYSTEM_PROCESSOR})
    endif()
    if(host_arch MATCHES "aarch64|arm64|ARM64")
        set(_arch armv8)
    elseif(host_arch MATCHES "armv7|armv7-a|armv7l|ARMV7")
        set(_arch armv7)
    elseif(host_arch MATCHES armv7s)
        set(_arch armv7s)
    elseif(host_arch MATCHES "i686|i386|X86")
        set(_arch x86)
    elseif(host_arch MATCHES "AMD64|amd64|x86_64|x64")
        set(_arch x86_64)
    endif()
    message(STATUS "CMake-Conan: cmake_system_processor=${_arch}")
    set(${arch} ${_arch} PARENT_SCOPE)
endfunction()


function(detect_cxx_standard cxx_standard)
    set(${cxx_standard} ${CMAKE_CXX_STANDARD} PARENT_SCOPE)
    if(CMAKE_CXX_EXTENSIONS)
        set(${cxx_standard} "gnu${CMAKE_CXX_STANDARD}" PARENT_SCOPE)
    endif()
endfunction()


macro(detect_gnu_libstdcxx)
    # _conan_is_gnu_libstdcxx true if GNU libstdc++
    check_cxx_source_compiles("
    #include <cstddef>
    #if !defined(__GLIBCXX__) && !defined(__GLIBCPP__)
    static_assert(false);
    #endif
    int main(){}" _conan_is_gnu_libstdcxx)

    # _conan_gnu_libstdcxx_is_cxx11_abi true if C++11 ABI
    check_cxx_source_compiles("
    #include <string>
    static_assert(sizeof(std::string) != sizeof(void*), \"using libstdc++\");
    int main () {}" _conan_gnu_libstdcxx_is_cxx11_abi)

    set(_conan_gnu_libstdcxx_suffix "")
    if(_conan_gnu_libstdcxx_is_cxx11_abi)
        set(_conan_gnu_libstdcxx_suffix "11")
    endif()
    unset (_conan_gnu_libstdcxx_is_cxx11_abi)
endmacro()


macro(detect_libcxx)
    # _conan_is_libcxx true if LLVM libc++
    check_cxx_source_compiles("
    #include <cstddef>
    #if !defined(_LIBCPP_VERSION)
       static_assert(false);
    #endif
    int main(){}" _conan_is_libcxx)
endmacro()


function(detect_lib_cxx lib_cxx)
    if(CMAKE_SYSTEM_NAME STREQUAL "Android")
        message(STATUS "CMake-Conan: android_stl=${CMAKE_ANDROID_STL_TYPE}")
        set(${lib_cxx} ${CMAKE_ANDROID_STL_TYPE} PARENT_SCOPE)
        return()
    endif()

    include(CheckCXXSourceCompiles)

    if(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
        detect_gnu_libstdcxx()
        set(${lib_cxx} "libstdc++${_conan_gnu_libstdcxx_suffix}" PARENT_SCOPE)
    elseif(CMAKE_CXX_COMPILER_ID MATCHES "AppleClang")
        set(${lib_cxx} "libc++" PARENT_SCOPE)
    elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang" AND NOT CMAKE_SYSTEM_NAME MATCHES "Windows")
        # Check for libc++
        detect_libcxx()
        if(_conan_is_libcxx)
            set(${lib_cxx} "libc++" PARENT_SCOPE)
            return()
        endif()

        # Check for libstdc++
        detect_gnu_libstdcxx()
        if(_conan_is_gnu_libstdcxx)
            set(${lib_cxx} "libstdc++${_conan_gnu_libstdcxx_suffix}" PARENT_SCOPE)
            return()
        endif()

        # TODO: it would be an error if we reach this point
    elseif(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
        # Do nothing - compiler.runtime and compiler.runtime_type
        # should be handled separately: https://github.com/conan-io/cmake-conan/pull/516
        return()
    else()
        # TODO: unable to determine, ask user to provide a full profile file instead
    endif()
endfunction()


function(detect_compiler compiler compiler_version compiler_runtime compiler_runtime_type)
    if(DEFINED CMAKE_CXX_COMPILER_ID)
        set(_compiler ${CMAKE_CXX_COMPILER_ID})
        set(_compiler_version ${CMAKE_CXX_COMPILER_VERSION})
    else()
        if(NOT DEFINED CMAKE_C_COMPILER_ID)
            message(FATAL_ERROR "C or C++ compiler not defined")
        endif()
        set(_compiler ${CMAKE_C_COMPILER_ID})
        set(_compiler_version ${CMAKE_C_COMPILER_VERSION})
    endif()

    message(STATUS "CMake-Conan: CMake compiler=${_compiler}")
    message(STATUS "CMake-Conan: CMake compiler version=${_compiler_version}")

    if(_compiler MATCHES MSVC)
        set(_compiler "msvc")
        string(SUBSTRING ${MSVC_VERSION} 0 3 _compiler_version)
        # Configure compiler.runtime and compiler.runtime_type settings for MSVC
        if(CMAKE_MSVC_RUNTIME_LIBRARY)
            set(_msvc_runtime_library ${CMAKE_MSVC_RUNTIME_LIBRARY})
        else()
            set(_msvc_runtime_library MultiThreaded$<$<CONFIG:Debug>:Debug>DLL) # default value documented by CMake
        endif()

        set(_KNOWN_MSVC_RUNTIME_VALUES "")
        list(APPEND _KNOWN_MSVC_RUNTIME_VALUES MultiThreaded MultiThreadedDLL)
        list(APPEND _KNOWN_MSVC_RUNTIME_VALUES MultiThreadedDebug MultiThreadedDebugDLL)
        list(APPEND _KNOWN_MSVC_RUNTIME_VALUES MultiThreaded$<$<CONFIG:Debug>:Debug> MultiThreaded$<$<CONFIG:Debug>:Debug>DLL)

        # only accept the 6 possible values, otherwise we don't don't know to map this
        if(NOT _msvc_runtime_library IN_LIST _KNOWN_MSVC_RUNTIME_VALUES)
            message(FATAL_ERROR "CMake-Conan: unable to map MSVC runtime: ${_msvc_runtime_library} to Conan settings")
        endif()

        # Runtime is "dynamic" in all cases if it ends in DLL
        if(_msvc_runtime_library MATCHES ".*DLL$")
            set(_compiler_runtime "dynamic")
        else()
            set(_compiler_runtime "static")
        endif()
        message(STATUS "CMake-Conan: CMake compiler.runtime=${_compiler_runtime}")

        # Only define compiler.runtime_type when explicitly requested
        # If a generator expression is used, let Conan handle it conditional on build_type
        if(NOT _msvc_runtime_library MATCHES "<CONFIG:Debug>:Debug>")
            if(_msvc_runtime_library MATCHES "Debug")
                set(_compiler_runtime_type "Debug")
            else()
                set(_compiler_runtime_type "Release")
            endif()
            message(STATUS "CMake-Conan: CMake compiler.runtime_type=${_compiler_runtime_type}")
        endif()

        unset(_KNOWN_MSVC_RUNTIME_VALUES)

    elseif(_compiler MATCHES AppleClang)
        set(_compiler "apple-clang")
        string(REPLACE "." ";" VERSION_LIST ${CMAKE_CXX_COMPILER_VERSION})
        list(GET VERSION_LIST 0 _compiler_version)
    elseif(_compiler MATCHES Clang)
        set(_compiler "clang")
        string(REPLACE "." ";" VERSION_LIST ${CMAKE_CXX_COMPILER_VERSION})
        list(GET VERSION_LIST 0 _compiler_version)
    elseif(_compiler MATCHES GNU)
        set(_compiler "gcc")
        string(REPLACE "." ";" VERSION_LIST ${CMAKE_CXX_COMPILER_VERSION})
        list(GET VERSION_LIST 0 _compiler_version)
    endif()

    message(STATUS "CMake-Conan: [settings] compiler=${_compiler}")
    message(STATUS "CMake-Conan: [settings] compiler.version=${_compiler_version}")
    if (_compiler_runtime)
        message(STATUS "CMake-Conan: [settings] compiler.runtime=${_compiler_runtime}")
    endif()
    if (_compiler_runtime_type)
        message(STATUS "CMake-Conan: [settings] compiler.runtime_type=${_compiler_runtime_type}")
    endif()

    set(${compiler} ${_compiler} PARENT_SCOPE)
    set(${compiler_version} ${_compiler_version} PARENT_SCOPE)
    set(${compiler_runtime} ${_compiler_runtime} PARENT_SCOPE)
    set(${compiler_runtime_type} ${_compiler_runtime_type} PARENT_SCOPE)
endfunction()


function(detect_build_type build_type)
    get_property(multiconfig_generator GLOBAL PROPERTY GENERATOR_IS_MULTI_CONFIG)
    if(NOT multiconfig_generator)
        # Only set when we know we are in a single-configuration generator
        # Note: we may want to fail early if `CMAKE_BUILD_TYPE` is not defined
        set(${build_type} ${CMAKE_BUILD_TYPE} PARENT_SCOPE)
    endif()
endfunction()


macro(set_conan_compiler_if_appleclang lang command output_variable)
    if(CMAKE_${lang}_COMPILER_ID STREQUAL "AppleClang")
        execute_process(COMMAND xcrun --find ${command}
            OUTPUT_VARIABLE _xcrun_out OUTPUT_STRIP_TRAILING_WHITESPACE)
        cmake_path(GET _xcrun_out PARENT_PATH _xcrun_toolchain_path)
        cmake_path(GET CMAKE_${lang}_COMPILER PARENT_PATH _compiler_parent_path)
        if ("${_xcrun_toolchain_path}" STREQUAL "${_compiler_parent_path}")
            set(${output_variable} "")
        endif()
        unset(_xcrun_out)
        unset(_xcrun_toolchain_path)
        unset(_compiler_parent_path)
    endif()
endmacro()


macro(append_compiler_executables_configuration)
    set(_conan_c_compiler "")
    set(_conan_cpp_compiler "")
    set(_conan_rc_compiler "")
    set(_conan_compilers_list "")
    if(CMAKE_C_COMPILER)
        set(_conan_c_compiler "\"c\":\"${CMAKE_C_COMPILER}\"")
        set_conan_compiler_if_appleclang(C cc _conan_c_compiler)
        list(APPEND _conan_compilers_list ${_conan_c_compiler})
    else()
        message(WARNING "CMake-Conan: The C compiler is not defined. "
                        "Please define CMAKE_C_COMPILER or enable the C language.")
    endif()
    if(CMAKE_CXX_COMPILER)
        set(_conan_cpp_compiler "\"cpp\":\"${CMAKE_CXX_COMPILER}\"")
        set_conan_compiler_if_appleclang(CXX c++ _conan_cpp_compiler)
        list(APPEND _conan_compilers_list ${_conan_cpp_compiler})
    else()
        message(WARNING "CMake-Conan: The C++ compiler is not defined. "
                        "Please define CMAKE_CXX_COMPILER or enable the C++ language.")
    endif()
    if(CMAKE_RC_COMPILER)
        set(_conan_rc_compiler "\"rc\":\"${CMAKE_RC_COMPILER}\"")
        list(APPEND _conan_compilers_list ${_conan_rc_compiler})
        # Not necessary to warn if RC not defined
    endif()
    if(NOT "x${_conan_compilers_list}" STREQUAL "x")
        string(REPLACE ";" "," _conan_compilers_list "${_conan_compilers_list}")
        string(APPEND profile "tools.build:compiler_executables={${_conan_compilers_list}}\n")
    endif()
    unset(_conan_c_compiler)
    unset(_conan_cpp_compiler)
    unset(_conan_rc_compiler)
    unset(_conan_compilers_list)
endmacro()


function(detect_host_profile output_file)
    detect_os(os os_api_level os_sdk os_subsystem os_version)
    detect_arch(arch)
    detect_compiler(compiler compiler_version compiler_runtime compiler_runtime_type)
    detect_cxx_standard(compiler_cppstd)
    detect_lib_cxx(compiler_libcxx)
    detect_build_type(build_type)

    set(profile "")
    string(APPEND profile "[settings]\n")
    if(arch)
        string(APPEND profile arch=${arch} "\n")
    endif()
    if(os)
        string(APPEND profile os=${os} "\n")
    endif()
    if(os_api_level)
        string(APPEND profile os.api_level=${os_api_level} "\n")
    endif()
    if(os_version)
        string(APPEND profile os.version=${os_version} "\n")
    endif()
    if(os_sdk)
        string(APPEND profile os.sdk=${os_sdk} "\n")
    endif()
    if(os_subsystem)
        string(APPEND profile os.subsystem=${os_subsystem} "\n")
    endif()
    if(compiler)
        string(APPEND profile compiler=${compiler} "\n")
    endif()
    if(compiler_version)
        string(APPEND profile compiler.version=${compiler_version} "\n")
    endif()
    if(compiler_runtime)
        string(APPEND profile compiler.runtime=${compiler_runtime} "\n")
    endif()
    if(compiler_runtime_type)
        string(APPEND profile compiler.runtime_type=${compiler_runtime_type} "\n")
    endif()
    if(compiler_cppstd)
        string(APPEND profile compiler.cppstd=${compiler_cppstd} "\n")
    endif()
    if(compiler_libcxx)
        string(APPEND profile compiler.libcxx=${compiler_libcxx} "\n")
    endif()
    if(build_type)
        string(APPEND profile "build_type=${build_type}\n")
    endif()

    if(NOT DEFINED output_file)
        set(file_name "${CMAKE_BINARY_DIR}/profile")
    else()
        set(file_name ${output_file})
    endif()

    string(APPEND profile "[conf]\n")
    string(APPEND profile "tools.cmake.cmaketoolchain:generator=${CMAKE_GENERATOR}\n")

    # propagate compilers via profile
    append_compiler_executables_configuration()

    if(os STREQUAL "Android")
        string(APPEND profile "tools.android:ndk_path=${CMAKE_ANDROID_NDK}\n")
    endif()

    message(STATUS "CMake-Conan: Creating profile ${file_name}")
    file(WRITE ${file_name} ${profile})
    message(STATUS "CMake-Conan: Profile: \n${profile}")
endfunction()


function(conan_profile_detect_default)
    message(STATUS "CMake-Conan: Checking if a default profile exists")
    execute_process(COMMAND ${CONAN_COMMAND} profile path default
                    RESULT_VARIABLE return_code
                    OUTPUT_VARIABLE conan_stdout
                    ERROR_VARIABLE conan_stderr
                    ECHO_ERROR_VARIABLE    # show the text output regardless
                    ECHO_OUTPUT_VARIABLE
                    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
    if(NOT ${return_code} EQUAL "0")
        message(STATUS "CMake-Conan: The default profile doesn't exist, detecting it.")
        execute_process(COMMAND ${CONAN_COMMAND} profile detect
            RESULT_VARIABLE return_code
            OUTPUT_VARIABLE conan_stdout
            ERROR_VARIABLE conan_stderr
            ECHO_ERROR_VARIABLE    # show the text output regardless
            ECHO_OUTPUT_VARIABLE
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
    endif()
endfunction()


function(conan_install)
    cmake_parse_arguments(ARGS conan_args ${ARGN})
    set(conan_output_folder ${CMAKE_BINARY_DIR}/conan)
    # Invoke "conan install" with the provided arguments
    set(conan_args ${conan_args} -of=${conan_output_folder})
    message(STATUS "CMake-Conan: conan install ${CMAKE_SOURCE_DIR} ${conan_args} ${ARGN}")


    # In case there was not a valid cmake executable in the PATH, we inject the
    # same we used to invoke the provider to the PATH
    if(DEFINED PATH_TO_CMAKE_BIN)
        set(old_path $ENV{PATH})
        set(ENV{PATH} "$ENV{PATH}:${PATH_TO_CMAKE_BIN}")
    endif()

    execute_process(COMMAND ${CONAN_COMMAND} install ${CMAKE_SOURCE_DIR} ${conan_args} ${ARGN} --format=json
                    RESULT_VARIABLE return_code
                    OUTPUT_VARIABLE conan_stdout
                    ERROR_VARIABLE conan_stderr
                    ECHO_ERROR_VARIABLE    # show the text output regardless
                    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})

    if(DEFINED PATH_TO_CMAKE_BIN)
        set(ENV{PATH} "${old_path}")
    endif()

    if(NOT "${return_code}" STREQUAL "0")
        message(FATAL_ERROR "Conan install failed='${return_code}'")
    endif()

    # the files are generated in a folder that depends on the layout used, if
    # one is specified, but we don't know a priori where this is.
    # TODO: this can be made more robust if Conan can provide this in the json output
    string(JSON conan_generators_folder GET "${conan_stdout}" graph nodes 0 generators_folder)
    cmake_path(CONVERT ${conan_generators_folder} TO_CMAKE_PATH_LIST conan_generators_folder)

    message(STATUS "CMake-Conan: CONAN_GENERATORS_FOLDER=${conan_generators_folder}")
    set_property(GLOBAL PROPERTY CONAN_GENERATORS_FOLDER "${conan_generators_folder}")
    # reconfigure on conanfile changes
    string(JSON conanfile GET "${conan_stdout}" graph nodes 0 label)
    message(STATUS "CMake-Conan: CONANFILE=${CMAKE_SOURCE_DIR}/${conanfile}")
    set_property(DIRECTORY ${CMAKE_SOURCE_DIR} APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/${conanfile}")
    # success
    set_property(GLOBAL PROPERTY CONAN_INSTALL_SUCCESS TRUE)

endfunction()


function(conan_get_version conan_command conan_current_version)
    execute_process(
        COMMAND ${conan_command} --version
        OUTPUT_VARIABLE conan_output
        RESULT_VARIABLE conan_result
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    if(conan_result)
        message(FATAL_ERROR "CMake-Conan: Error when trying to run Conan")
    endif()

    string(REGEX MATCH "[0-9]+\\.[0-9]+\\.[0-9]+" conan_version ${conan_output})
    set(${conan_current_version} ${conan_version} PARENT_SCOPE)
endfunction()


function(conan_version_check)
    set(options )
    set(one_value_args MINIMUM CURRENT)
    set(multi_value_args )
    cmake_parse_arguments(conan_version_check
        "${options}" "${one_value_args}" "${multi_value_args}" ${ARGN})

    if(NOT conan_version_check_MINIMUM)
        message(FATAL_ERROR "CMake-Conan: Required parameter MINIMUM not set!")
    endif()
        if(NOT conan_version_check_CURRENT)
        message(FATAL_ERROR "CMake-Conan: Required parameter CURRENT not set!")
    endif()

    if(conan_version_check_CURRENT VERSION_LESS conan_version_check_MINIMUM)
        message(FATAL_ERROR "CMake-Conan: Conan version must be ${conan_version_check_MINIMUM} or later")
    endif()
endfunction()


macro(construct_profile_argument argument_variable profile_list)
    set(${argument_variable} "")
    if("${profile_list}" STREQUAL "CONAN_HOST_PROFILE")
        set(_arg_flag "--profile:host=")
    elseif("${profile_list}" STREQUAL "CONAN_BUILD_PROFILE")
        set(_arg_flag "--profile:build=")
    endif()

    set(_profile_list "${${profile_list}}")
    list(TRANSFORM _profile_list REPLACE "auto-cmake" "${CMAKE_BINARY_DIR}/conan_host_profile")
    list(TRANSFORM _profile_list PREPEND ${_arg_flag})
    set(${argument_variable} ${_profile_list})

    unset(_arg_flag)
    unset(_profile_list)
endmacro()


macro(conan_provide_dependency method package_name)
    set_property(GLOBAL PROPERTY CONAN_PROVIDE_DEPENDENCY_INVOKED TRUE)
    get_property(_conan_install_success GLOBAL PROPERTY CONAN_INSTALL_SUCCESS)
    if(NOT _conan_install_success)
        find_program(CONAN_COMMAND "conan" REQUIRED)
        conan_get_version(${CONAN_COMMAND} CONAN_CURRENT_VERSION)
        conan_version_check(MINIMUM ${CONAN_MINIMUM_VERSION} CURRENT ${CONAN_CURRENT_VERSION})
        message(STATUS "CMake-Conan: first find_package() found. Installing dependencies with Conan")
        if("default" IN_LIST CONAN_HOST_PROFILE OR "default" IN_LIST CONAN_BUILD_PROFILE)
            conan_profile_detect_default()
        endif()
        if("auto-cmake" IN_LIST CONAN_HOST_PROFILE)
            detect_host_profile(${CMAKE_BINARY_DIR}/conan_host_profile)
        endif()
        construct_profile_argument(_host_profile_flags CONAN_HOST_PROFILE)
        construct_profile_argument(_build_profile_flags CONAN_BUILD_PROFILE)
        if(EXISTS "${CMAKE_SOURCE_DIR}/conanfile.py")
            file(READ "${CMAKE_SOURCE_DIR}/conanfile.py" outfile)
            if(NOT "${outfile}" MATCHES ".*CMakeDeps.*")
                message(WARNING "Cmake-conan: CMakeDeps generator was not defined in the conanfile")
            endif()
            set(generator "")
        elseif (EXISTS "${CMAKE_SOURCE_DIR}/conanfile.txt")
            file(READ "${CMAKE_SOURCE_DIR}/conanfile.txt" outfile)
            if(NOT "${outfile}" MATCHES ".*CMakeDeps.*")
                message(WARNING "Cmake-conan: CMakeDeps generator was not defined in the conanfile. "
                        "Please define the generator as it will be mandatory in the future")
            endif()
            set(generator "-g;CMakeDeps")
        endif()
        get_property(_multiconfig_generator GLOBAL PROPERTY GENERATOR_IS_MULTI_CONFIG)
        if(NOT _multiconfig_generator)
            message(STATUS "CMake-Conan: Installing single configuration ${CMAKE_BUILD_TYPE}")
            conan_install(${_host_profile_flags} ${_build_profile_flags} ${CONAN_INSTALL_ARGS} ${generator})
        else()
            message(STATUS "CMake-Conan: Installing both Debug and Release")
            conan_install(${_host_profile_flags} ${_build_profile_flags} -s build_type=Release ${CONAN_INSTALL_ARGS} ${generator})
            conan_install(${_host_profile_flags} ${_build_profile_flags} -s build_type=Debug ${CONAN_INSTALL_ARGS} ${generator})
        endif()
        unset(_host_profile_flags)
        unset(_build_profile_flags)
        unset(_multiconfig_generator)
        unset(_conan_install_success)
    else()
        message(STATUS "CMake-Conan: find_package(${ARGV1}) found, 'conan install' already ran")
        unset(_conan_install_success)
    endif()

    get_property(_conan_generators_folder GLOBAL PROPERTY CONAN_GENERATORS_FOLDER)

    # Ensure that we consider Conan-provided packages ahead of any other,
    # irrespective of other settings that modify the search order or search paths
    # This follows the guidelines from the find_package documentation
    #  (https://cmake.org/cmake/help/latest/command/find_package.html):
    #       find_package (<PackageName> PATHS paths... NO_DEFAULT_PATH)
    #       find_package (<PackageName>)

    # Filter out `REQUIRED` from the argument list, as the first call may fail
    set(_find_args_${package_name} "${ARGN}")
    list(REMOVE_ITEM _find_args_${package_name} "REQUIRED")
    if(NOT "MODULE" IN_LIST _find_args_${package_name})
        find_package(${package_name} ${_find_args_${package_name}} BYPASS_PROVIDER PATHS "${_conan_generators_folder}" NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
        unset(_find_args_${package_name})
    endif()

    # Invoke find_package a second time - if the first call succeeded,
    # this will simply reuse the result. If not, fall back to CMake default search
    # behaviour, also allowing modules to be searched.
    if(NOT ${package_name}_FOUND)
        list(FIND CMAKE_MODULE_PATH "${_conan_generators_folder}" _index)
        if(_index EQUAL -1)
            list(PREPEND CMAKE_MODULE_PATH "${_conan_generators_folder}")
        endif()
        unset(_index)
        find_package(${package_name} ${ARGN} BYPASS_PROVIDER)
        list(REMOVE_ITEM CMAKE_MODULE_PATH "${_conan_generators_folder}")
    endif()
endmacro()


cmake_language(
    SET_DEPENDENCY_PROVIDER conan_provide_dependency
    SUPPORTED_METHODS FIND_PACKAGE
)


macro(conan_provide_dependency_check)
    set(_conan_provide_dependency_invoked FALSE)
    get_property(_conan_provide_dependency_invoked GLOBAL PROPERTY CONAN_PROVIDE_DEPENDENCY_INVOKED)
    if(NOT _conan_provide_dependency_invoked)
        message(WARNING "Conan is correctly configured as dependency provider, "
                        "but Conan has not been invoked. Please add at least one "
                        "call to `find_package()`.")
        if(DEFINED CONAN_COMMAND)
            # supress warning in case `CONAN_COMMAND` was specified but unused.
            set(_conan_command ${CONAN_COMMAND})
            unset(_conan_command)
        endif()
    endif()
    unset(_conan_provide_dependency_invoked)
endmacro()


# Add a deferred call at the end of processing the top-level directory
# to check if the dependency provider was invoked at all.
cmake_language(DEFER DIRECTORY "${CMAKE_SOURCE_DIR}" CALL conan_provide_dependency_check)

# Configurable variables for Conan profiles
set(CONAN_HOST_PROFILE "default;auto-cmake" CACHE STRING "Conan host profile")
set(CONAN_BUILD_PROFILE "default" CACHE STRING "Conan build profile")
set(CONAN_INSTALL_ARGS "--build=missing" CACHE STRING "Command line arguments for conan install")

find_program(_cmake_program NAMES cmake NO_PACKAGE_ROOT_PATH NO_CMAKE_PATH NO_CMAKE_ENVIRONMENT_PATH NO_CMAKE_SYSTEM_PATH NO_CMAKE_FIND_ROOT_PATH)
if(NOT _cmake_program)
    get_filename_component(PATH_TO_CMAKE_BIN "${CMAKE_COMMAND}" DIRECTORY)
    set(PATH_TO_CMAKE_BIN "${PATH_TO_CMAKE_BIN}" CACHE INTERNAL "Path where the CMake executable is")
endif()

cmake_policy(POP)


File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {one line to give the program's name and a brief idea of what it does.}
    Copyright (C) {year}  {name of author}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.


File: /README.md
# midi_to_mikrotik_converter
[![CodeFactor](https://www.codefactor.io/repository/github/altucor/midi_to_mikrotik_converter/badge/master)](https://www.codefactor.io/repository/github/altucor/midi_to_mikrotik_converter/overview/master)\
Forum links:\
https://forum.mikrotik.com/viewtopic.php?f=9&t=135207  
Video how to manually parse music to midi file and how to use that program, check time codes in video description:\
https://www.youtube.com/watch?v=g6GZVlYP7X0

# Features
1) Parse SMF and extract ppqn, bpm and other info
2) Support octave/note/fine shift globally for input file
3) Support multitrack files, can find tempo data in one track and apply to other tracks
4) Can add comments to output file with note name and timestamp
5) Correctly detects pre-delays and VLV values
6) Verbose logging
7) Creating sub-tracks for intersected notes. Only one note can be played at one moment of time on one device. Cause MikroTik beeper is single voice.

# Using program

| Short Key | Full Key | Description | Example |
| ------ | ------ | ------ |  ------ |
| -h | --help | Print this help message | -h |
| -f | --file | Select input standard midi file (SMF) | -f <input_file.mid> |
| -o | --octave-shift | Sets the octave shift relative to the original (-10 to +10) | -o -2 //Shifts all notes 2 octaves down |
| -n | --note-shift | Sets the note shift relative to the original | -n 3 //Shifts all notes 3 notes up |
| -t | --fine-tuning | Sets frequency offset for all notes in case when you think your beeper produces beeps at wrong frequencies | -t -10.3 //Shifts all notes for 10.3Hz down |
| -b | --bpm | Sets the new bpm to output file | -b 130 //Sets a new bpm to 130, ignores the original bpm in the file |
| -c | --comments | Adds comments in the form of notes | -c |
| -l | --log-level | Set logging level (trace, debug, info, warning, error, fatal) | -l debug |

# Building program
1) Install CMake
2) Install conan
3) cd midi_to_mikrotik_converter
4) mkdir build
5) Run only once with provider to pull BOOST library: `cmake -B build -S . -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=./conan_provider.cmake -DCMAKE_BUILD_TYPE=Debug`
6) cd build
7) cmake --build ./ --config Release

Conan CMake provider manual: https://github.com/conan-io/cmake-conan/tree/develop2

If you have some problems with getting Boost library than check available prebuilt packages and configure project to match one of available here: https://conan.io/center/boost?version=1.75.0&os=Windows&tab=configuration\


File: /src\Config.hpp
#pragma once

#include "util.h"

#include "boost/log/trivial.hpp"

#include <fstream>
#include <string>

class PitchShift
{
public:
    int8_t octave = 0;
    int8_t note = 0;
    float fine = 0.0f;
    uint8_t process(const uint8_t pitch) const
    {
        return pitch + (octave * MIDI_NOTES_IN_OCTAVE) + note;
    }
    float freq(const uint8_t pitch) const
    {
        return pitch_to_freq(pitch + (octave * MIDI_NOTES_IN_OCTAVE) + note) + fine;
    }
    void toStream(std::ofstream &out) const
    {
        out << "octave: " << (octave >= 0 ? "+" : "-") << std::to_string(octave);
        out << " note: " << (note >= 0 ? "+" : "-") << std::to_string(note);
        out << " fine: " << (fine >= 0.0f ? "+" : "-") << std::to_string(fine);
    }
};

class Config
{
public:
    bool comments = false;
    boost::log::trivial::severity_level logLevel = boost::log::trivial::severity_level::info;
    uint16_t ppqn = 0;
    int32_t bpm = 0;
    PitchShift pitchShift = {0};
    std::string inFileName = "";
};


File: /src\midi-to-mikrotik-converter.cpp

/*
 +   1) detect note on/off
 +   2) detect delay in ms beetwen notes
 +   3) detect tempo
 +   4) detect ppqn
 +   5) add octave/note/fine shift
 +   6) add multitrack decoding
 +   7) add BPM change
 +   8) add flag -c for writing note comments in file
 +   9) detect full VLV delays
 +  10) detect first/pre delay
 +  11) add logging levels
 -  12) add boost filesystem processing for files
*/

#include "file.h"

#include "Config.hpp"
#include "MikrotikTrack.hpp"
#include "TrackAnalyzer.hpp"

#include "boost/log/trivial.hpp"
#include "boost/log/utility/setup.hpp"
#include <boost/program_options.hpp>

#include <cstdio>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>

namespace po = boost::program_options;

static void init_log()
{
    static const std::string COMMON_FMT("[%TimeStamp%][%Severity%]: %Message%");

    boost::log::register_simple_formatter_factory<boost::log::trivial::severity_level, char>("Severity");

    // Output message to console
    boost::log::add_console_log(std::cout, boost::log::keywords::format = COMMON_FMT, boost::log::keywords::auto_flush = true);

    // Output message to file, rotates when file
    // reached 1mb or at midnight every day. Each log file
    // is capped at 1mb and total is 20mb
    boost::log::add_file_log(boost::log::keywords::file_name = "mtmc_%3N.log", boost::log::keywords::rotation_size = 100 * 1024 * 1024,
                             boost::log::keywords::max_size = 100 * 1024 * 1024,
                             boost::log::keywords::time_based_rotation = boost::log::sinks::file::rotation_at_time_point(0, 0, 0),
                             boost::log::keywords::format = COMMON_FMT, boost::log::keywords::auto_flush = true);

    boost::log::add_common_attributes();

    // Only output message with INFO or higher severity in Release
#ifndef _DEBUG
    boost::log::core::get()->set_filter(boost::log::trivial::severity >= boost::log::trivial::info);
#endif
}

static int32_t parseArguments(int argc, char *argv[], Config &config)
{
    po::options_description desc("Application arguments");
    desc.add_options()                                                                                                                  //
        ("help,h", "Print this help message")                                                                                           //
        ("file,f", po::value<std::string>(&config.inFileName), "Select input standart midi file (SMF)")                                 //
        ("octave-shift,o", po::value<int8_t>(&config.pitchShift.octave), "Sets the octave shift relative to the original (-10 to +10)") //
        ("note-shift,n", po::value<int8_t>(&config.pitchShift.note), "Sets the note shift relative to the original")                    //
        ("fine-tuning,t", po::value<float>(&config.pitchShift.fine),
         "Sets frequency offset for all notes in case when you think your beeper produces beeps at wrong frequencies") //
        ("bpm,b", po::value<int>(&config.bpm), "Sets the new bpm to output file")                                      //
        ("log-level,l", po::value<boost::log::trivial::severity_level>(&config.logLevel)->default_value(boost::log::trivial::severity_level::info),
         "Sets the log level: trace, debug, info, warning, error, fatal") //
        ("comments,c", "Adds comments in the form of notes");

    if (argc == 1)
    {
        std::cout << desc << std::endl;
        return 0;
    }

    po::variables_map vm;
    try
    {
        po::parsed_options parsed = po::command_line_parser(argc, argv).options(desc).allow_unregistered().run();
        po::store(parsed, vm);
        po::notify(vm);

        if (vm.count("help"))
        {
            std::cout << desc << std::endl;
            return 0;
        }
        if (vm.count("comments"))
        {
            config.comments = true;
        }
    }
    catch (std::exception &ex)
    {
        std::cout << ex.what() << std::endl;
        std::cout << desc << std::endl;
    }

    boost::log::core::get()->set_filter(boost::log::trivial::severity >= config.logLevel);

    if (config.inFileName == "")
    {
        BOOST_LOG_TRIVIAL(error) << "[mtmc] no input (SMF) file specified";
        std::cout << desc << std::endl;
        return -1;
    }

    return 0;
}

int main(int argc, char *argv[])
{
    init_log();

    Config config = {0};
    int32_t ret = parseArguments(argc, argv, config);
    if (ret < 0)
    {
        return ret;
    }

    std::ifstream midiStream{config.inFileName, midiStream.binary | midiStream.in};
    if (!midiStream.is_open())
    {
        BOOST_LOG_TRIVIAL(error) << "[mtmc] cannot open file: " << config.inFileName;
        return -1;
    }
    std::vector<unsigned char> midiFileBuffer(std::istreambuf_iterator<char>(midiStream), {});

    midi_file_t *midiFile = midi_file_new();

    int read = midi_file_unmarshal(midiFile, midiFileBuffer.data(), midiFileBuffer.size());
    if (read > 0)
    {
        BOOST_LOG_TRIVIAL(info) << "[mtmc] midi file parsed total bytes: " << std::to_string(read) << std::endl;
    }
    else
    {
        BOOST_LOG_TRIVIAL(error) << "[mtmc] error parsing midi file stream: " << std::to_string(read) << std::endl;
        midi_file_free(midiFile);
        return -1;
    }

    config.ppqn = midi_file_get_mthd(midiFile).ppqn;
    BOOST_LOG_TRIVIAL(info) << "[mtmc] mthd ppqn: " << std::to_string(config.ppqn);
    const uint16_t trackCount = midi_file_get_tracks_count(midiFile);
    BOOST_LOG_TRIVIAL(info) << "[mtmc] track count: " << std::to_string(trackCount);

    // If new BPM not set by user input find in one of tracks
    if (config.bpm == 0)
    {
        BOOST_LOG_TRIVIAL(info) << "[mtmc] searching bpm event...";
        for (uint32_t i = 0; i < trackCount; i++)
        {
            mtrk_t *track = midi_file_get_track(midiFile, i);

            // midi_cmd_t cmd = {.status = MIDI_STATUS_SYSTEM, .subCmd = MIDI_STATUS_SYSTEM_RESET_OR_META};
            midi_cmd_t cmd = {MIDI_STATUS_SYSTEM_RESET_OR_META, MIDI_STATUS_SYSTEM};
            uint8_t message_meta = MIDI_META_EVENT_TEMPO;
            uint32_t bpmIndex = mtrk_find_event_index(track, 0, cmd, message_meta);
            if (bpmIndex != -1)
            {
                midi_event_smf_t *bpmEvent = mtrk_get_event(track, bpmIndex);
                config.bpm = bpmEvent->event.meta.tempo.val;
            }
        }
    }

    BOOST_LOG_TRIVIAL(info) << "[mtmc] bpm set to: " << std::to_string(config.bpm);

    std::vector<MikrotikTrack> mikrotikTracks;

    for (uint16_t i = 0; i < trackCount; i++)
    {
        TrackAnalyzer trackAnalyzer(config, i);
        mtrk_t *track = midi_file_get_track(midiFile, i);
        BOOST_LOG_TRIVIAL(info) << "[mtmc] analyzing track: " << std::to_string(i);
        auto tracks = trackAnalyzer.analyze(track);
        mikrotikTracks.insert(mikrotikTracks.end(), tracks.begin(), tracks.end());
        BOOST_LOG_TRIVIAL(info) << "[mtmc] analyzing track: " << std::to_string(i) << " done";
    }

    midi_file_free(midiFile);

    std::for_each(mikrotikTracks.begin(), mikrotikTracks.end(), [&](MikrotikTrack &track) { track.exportScript(config); });

    return 0;
}


File: /src\MikrotikNote.hpp
#pragma once

#include "util.h"

#include "Config.hpp"
#include "Utils.hpp"

#include <boost/log/trivial.hpp>

#include <fstream>
#include <sstream>

bool isInRange(const uint32_t val, const uint32_t min, const uint32_t max)
{
    return min < val && val < max;
}

class MikrotikNote
{
public:
    MikrotikNote()
    {
    }
    MikrotikNote(const uint8_t pitch, const uint32_t start, const uint32_t end) : m_pitch(pitch), m_timeStart(start), m_timeEnd(end)
    {
    }
    const std::string prefix() const
    {
        return "[Note % " + std::to_string(m_pitch) + "] ";
    }
    void log() const
    {
        BOOST_LOG_TRIVIAL(debug) << prefix() << " start: " << (uint32_t)m_timeStart << " end: " << (uint32_t)m_timeEnd;
    }
    uint8_t pitch() const
    {
        return m_pitch;
    }
    uint32_t start() const
    {
        return m_timeStart;
    }
    uint32_t end() const
    {
        return m_timeEnd;
    }
    uint32_t duration() const
    {
        return m_timeEnd - m_timeStart;
    }
    uint32_t getPredelayFromPrevious(const MikrotikNote &other) const
    {
        return m_timeStart - other.m_timeEnd;
    }
    bool intersectsWith(const MikrotikNote &other) const
    {
        /*
         * 1) 10-20 and 30-40
         * 2) 10-20 and 15-25
         * 3) 10-20 and 05-15
         * 4) 10-20 and 20-30
         *
         */

        if (m_timeStart == other.m_timeStart || m_timeEnd == other.m_timeEnd)
        {
            return true;
        }

        if (m_timeStart < other.m_timeStart && isInRange(m_timeEnd, other.m_timeStart, m_timeEnd))
        {
            return true;
        }
        else if (other.m_timeStart < m_timeStart && isInRange(other.m_timeEnd, m_timeStart, m_timeEnd))
        {
            return true;
        }

        return false;
    }
    std::string beepLine(const PitchShift &pitch, const float pps) const
    {
        /*
         * :beep frequency=440 length=1000ms; # C4 + 35Hz @ HH:MM:SS:MS
         * :delay 1000ms;
         */

        std::stringstream ss;
        ss << ":beep frequency=" << std::to_string(pitch.freq(m_pitch));
        ss << " length=" << duration_to_ms(duration(), pps) << "ms;";

        return ss.str();
    }

private:
    uint8_t m_pitch = 0;
    uint32_t m_timeStart = 0;
    uint32_t m_timeEnd = 0;
};


File: /src\MikrotikTrack.hpp
#pragma once

#include "Config.hpp"
#include "MikrotikNote.hpp"
#include "Utils.hpp"

#include "boost/log/trivial.hpp"

#include <fstream>
#include <iomanip>
#include <sstream>
#include <vector>

class TrackMetaTextInfo
{
public:
    std::string text;
    std::string copyright;
    std::string track;
    std::string instrument;
    std::string lyric;
    std::string marker;
    std::string cue;
};

static std::string getTrackTimeLength(const double time)
{
    std::stringstream out;
    out << Utils::getTimeAsText(time);
    out << " HH:MM:SS:MS";
    return out.str();
}

class MikrotikTrack
{
public:
    MikrotikTrack()
    {
    }

    MikrotikTrack(const std::size_t trackIndex, const std::size_t midiChannel, const std::size_t sequenceIndex)
        : m_trackIndex(trackIndex), m_midiChannel(midiChannel), m_sequenceIndex(sequenceIndex)
    {
        std::stringstream ss;
        ss << std::to_string(m_trackIndex);
        ss << "-" << std::to_string(m_midiChannel);
        ss << "-" << std::to_string(m_sequenceIndex);
        m_nameSuffix = ss.str();
    }

    const std::string prefix() const
    {
        return "[MikrotikTrack # " + m_nameSuffix + "] ";
    }

    bool tryAppend(const MikrotikNote &note)
    {
        if (!m_notes.size() || !note.intersectsWith(m_notes.back()))
        {
            m_notes.push_back(note);
            return true;
        }

        return false;
    }

    void setTrackInfo(TrackMetaTextInfo &info)
    {
        m_metaTextInfo = info;
    }

    float duration(const float pps) const
    {
        return duration_to_ms(m_notes.back().end(), pps);
    }

    void noteComment(const MikrotikNote &note, PitchShift pitchShift, const float timeElapsed, std::ofstream &out)
    {
        out << " # " << std::string(pitch_to_name(pitchShift.process(note.pitch())));
        if (pitchShift.fine != 0.0f)
        {
            out << std::string(" ");
            out << ((pitchShift.fine < 0.0f) ? "-" : "+");
            out << pitchShift.fine;
            out << std::string(" Hz");
        }
        out << " @ " << Utils::getTimeAsText(timeElapsed);
    }

    void getScriptHeader(const Config &config, const float pps, std::ofstream &out)
    {
        out << "#----------------File Description-----------------#\n";
        out << "# This file generated by Midi To Mikrotik Converter\n";
        out << "# Visit app repo: https://github.com/altucor/midi_to_mikrotik_converter\n";
        out << "# Pitch shift config: ";
        config.pitchShift.toStream(out);
        out << "\n";
        out << "# Original midi file name/path: " << config.inFileName << "\n";
        out << "# Track BPM: " << std::to_string(config.bpm) << "\n";
        out << "# MIDI Channel: " << std::to_string(m_midiChannel) << "\n";
        out << "# Number of notes: " << m_notes.size() << "\n";
        out << "# Track length: " << getTrackTimeLength(duration(pps)) << "\n";
        out << "# Track name: " << m_metaTextInfo.track << "\n";
        out << "# Instrument name: " << m_metaTextInfo.instrument << "\n";
        out << "# Track text: " << m_metaTextInfo.text << "\n";
        out << "# Track copyright: " << m_metaTextInfo.copyright << "\n";
        out << "# Vocals: " << m_metaTextInfo.lyric << "\n";
        out << "# Text marker: " << m_metaTextInfo.marker << "\n";
        out << "# Cue Point: " << m_metaTextInfo.cue << "\n";
        out << "#-------------------------------------------------#\n\n";
    }

    int exportScript(Config &config)
    {
        if (m_notes.size() == 0)
        {
            return 0;
        }

        std::string outFileName = config.inFileName + "-" + m_nameSuffix + ".txt";
        std::ofstream outputFile;

        outputFile.open(outFileName);
        if (!outputFile.is_open())
        {
            BOOST_LOG_TRIVIAL(fatal) << prefix() << "export failed cannot create output file: " << outFileName;
            return -1;
        }

        BOOST_LOG_TRIVIAL(info) << prefix() << "export started for track: " << outFileName;

        const float pps = pulses_per_second(config.ppqn, config.bpm);
        BOOST_LOG_TRIVIAL(debug) << prefix() << "pps: " << pps;
        getScriptHeader(config, pps, outputFile);

        std::size_t timeElapsed = 0;
        std::for_each(m_notes.begin(), m_notes.end(), [&](const MikrotikNote &note) {
            if (note.start() - timeElapsed)
            {
                // write predelay line if start timing is non zero
                outputFile << Utils::getDelayLine(duration_to_ms(note.start() - timeElapsed, pps));
            }
            outputFile << note.beepLine(config.pitchShift, pps);
            timeElapsed = note.start(); // update global comment timer
            if (config.comments)
            {
                noteComment(note, config.pitchShift, duration_to_ms(timeElapsed, pps), outputFile);
            }
            outputFile << "\n";
            outputFile << Utils::getDelayLine(duration_to_ms(note.duration(), pps));
            outputFile << "\n";
            timeElapsed = note.end();
        });

        BOOST_LOG_TRIVIAL(info) << prefix() << "export finished";
        return 0;
    }

private:
    std::string m_nameSuffix = "";
    std::size_t m_trackIndex = 0;
    std::size_t m_sequenceIndex = 0;
    std::size_t m_midiChannel = 0;
    TrackMetaTextInfo m_metaTextInfo;
    std::vector<MikrotikNote> m_notes;
};


File: /src\Sequence.hpp
#pragma once

#include "events/note.h"

#include "MikrotikNote.hpp"

#include <boost/log/trivial.hpp>

#include <algorithm>
#include <array>
#include <sstream>
#include <vector>

const uint8_t kPitchMax = 128;

enum class SequenceEvent
{
    NONE = 0,
    NOTE_ON,
    NOTE_OFF,
    NOTE_OFF_ON,
};

class TimeMarker
{
public:
    TimeMarker(const uint32_t time, const bool on, const uint8_t pitch) : m_timeMarker(time)
    {
        setNote(on, pitch);
    }
    void setNote(const bool on, const uint8_t pitch)
    {
        if (m_pitch.at(pitch) == SequenceEvent::NOTE_OFF && on)
        {
            m_pitch.at(pitch) = SequenceEvent::NOTE_OFF_ON;
            return;
        }
        m_pitch.at(pitch) = on ? SequenceEvent::NOTE_ON : SequenceEvent::NOTE_OFF;
    }
    const std::string prefix() const
    {
        return "[TimeMarker @ " + std::to_string(m_timeMarker) + "] ";
    }
    uint32_t time() const
    {
        return m_timeMarker;
    }
    SequenceEvent pitch(const uint8_t pitch) const
    {
        return m_pitch.at(pitch);
    }
    void dumpEvents() const
    {
        std::stringstream ss;
        for (uint8_t i = 0; i < kPitchMax; i++)
        {
            if (m_pitch.at(i) == SequenceEvent::NOTE_ON || m_pitch.at(i) == SequenceEvent::NOTE_OFF)
            {
                ss << "pitch: " << std::to_string(i) << " ";
                ss << std::to_string(static_cast<uint8_t>(m_pitch.at(i))) << " ";
            }
        }
        BOOST_LOG_TRIVIAL(info) << prefix() << "enabled events: " << ss.str();
    }
    bool hasNoteOffAtPitch(const uint32_t pitch) const
    {
        return m_pitch.at(pitch) == SequenceEvent::NOTE_OFF || m_pitch.at(pitch) == SequenceEvent::NOTE_OFF_ON;
    }
    bool timeEquals(const uint32_t otherTime) const
    {
        return otherTime == m_timeMarker;
    }

private:
    std::array<SequenceEvent, kPitchMax> m_pitch = {SequenceEvent::NONE};
    uint32_t m_timeMarker = 0;
};

class Sequence
{
public:
    Sequence()
    {
    }
    Sequence(const std::size_t trackIndex, const uint8_t channel) : m_trackIndex(trackIndex), m_channel(channel)
    {
    }
    const std::string prefix() const
    {
        return "[Sequence ch# " + std::to_string(m_channel) + "] ";
    }
    void setTrackInfo(TrackMetaTextInfo &info)
    {
        m_metaTextInfo = info;
    }
    void appenMidiNoteEvent(const bool on, const uint8_t pitch, const uint32_t time)
    {
        BOOST_LOG_TRIVIAL(debug) << prefix() << "event add: " << (on ? " ON" : "OFF") << " pitch: " << std::to_string(pitch) << " time: " << std::to_string(time);
        if (auto it = std::find_if(begin(m_timeMarkers), end(m_timeMarkers), [&](TimeMarker &marker) { return marker.timeEquals(time); });
            it != std::end(m_timeMarkers))
        {
            it->setNote(on, pitch);
        }
        else
        {
            m_timeMarkers.push_back(TimeMarker(time, on, pitch));
        }
    }
    MikrotikNote getNote(const uint32_t startTime, const uint8_t pitch) const
    {
        MikrotikNote note;

        auto it = std::find_if(begin(m_timeMarkers), end(m_timeMarkers),
                               [&](const TimeMarker &marker) { return marker.time() > startTime && marker.hasNoteOffAtPitch(pitch); });

        if (it == std::end(m_timeMarkers))
        {
            return note;
        }

        note = MikrotikNote(pitch, startTime, it->time());
        return note;
    }
    std::vector<MikrotikTrack> analyze()
    {
        std::size_t trackSequenceIndex = 0;
        std::vector<MikrotikTrack> mikrotikTracks;
        mikrotikTracks.push_back(MikrotikTrack(m_trackIndex, m_channel, trackSequenceIndex++));
        mikrotikTracks.back().setTrackInfo(m_metaTextInfo);
        if (m_timeMarkers.size() == 0)
        {
            return mikrotikTracks;
        }
        BOOST_LOG_TRIVIAL(info) << prefix() << "analysis started, total time markers: " << std::to_string(m_timeMarkers.size());
        std::for_each(m_timeMarkers.begin(), m_timeMarkers.end(), [&](TimeMarker &marker) {
            for (uint8_t i = 0; i < kPitchMax; i++)
            {
                if (marker.pitch(i) == SequenceEvent::NOTE_OFF || marker.pitch(i) == SequenceEvent::NONE)
                {
                    continue;
                }
                auto note = getNote(marker.time(), i);
                note.log();

                if (std::ranges::none_of(mikrotikTracks, [&](MikrotikTrack &track) { return track.tryAppend(note); }))
                {
                    BOOST_LOG_TRIVIAL(info) << prefix() << "No free Track, creating new and adding to it";
                    mikrotikTracks.push_back(MikrotikTrack(m_trackIndex, m_channel, trackSequenceIndex++));
                    mikrotikTracks.back().setTrackInfo(m_metaTextInfo);
                    mikrotikTracks.back().tryAppend(note);
                }
            }
        });
        if (mikrotikTracks.size() > 0 && m_timeMarkers.size() > 0)
        {
            BOOST_LOG_TRIVIAL(info) << prefix() << "total tracks used: " << std::to_string(mikrotikTracks.size());
        }

        return mikrotikTracks;
    }

private:
    std::size_t m_trackIndex = 0;
    uint8_t m_channel = 0;
    TrackMetaTextInfo m_metaTextInfo;
    std::vector<TimeMarker> m_timeMarkers;
};


File: /src\TrackAnalyzer.hpp
#pragma once

#include "mtrk.h"

#include "Config.hpp"
#include "Sequence.hpp"

#include "boost/log/trivial.hpp"

#include <array>
#include <vector>

class TrackAnalyzer
{
public:
    TrackAnalyzer(Config &config, const std::size_t trackIndex) : m_config(config), m_trackIndex(trackIndex)
    {
        for (uint8_t i = 0; i < MIDI_CHANNELS_MAX_COUNT; i++)
        {
            m_sequences[i] = Sequence(m_trackIndex, i);
        }
    }
    std::vector<MikrotikTrack> analyze(mtrk_t *track)
    {
        if (track == nullptr)
        {
            return std::vector<MikrotikTrack>();
        }
        uint32_t eventsCount = mtrk_get_events_count(track);
        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] available midi events: " << std::to_string(eventsCount);
        for (uint32_t i = 0; i < eventsCount; i++)
        {
            midi_event_smf_t *event = mtrk_get_event(track, i);
            m_trackDuration += event->predelay.val;
            if (event->message.status == MIDI_STATUS_NOTE_OFF || event->message.status == MIDI_STATUS_NOTE_ON)
            {
                midi_note_t note = event->event.note;
                m_sequences.at(note.channel).appenMidiNoteEvent(note.on, note.pitch, m_trackDuration);
            }
            else if (event->message.status == MIDI_STATUS_SYSTEM)
            {
                // store additional events
                if (is_meta_text_event(event->message_meta))
                {
                    BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] found TEXT event: " << Utils::toHex(event->message_meta, 1);
                    switch (event->message_meta)
                    {
                    case MIDI_META_EVENT_TEXT:
                        m_metaTextInfo.text = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] text: " << m_metaTextInfo.text;
                        break;
                    case MIDI_META_EVENT_COPYRIGHT:
                        m_metaTextInfo.copyright = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] copyright: " << m_metaTextInfo.copyright;
                        break;
                    case MIDI_META_EVENT_TRACK_NAME:
                        m_metaTextInfo.track = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] track: " << m_metaTextInfo.track;
                        break;
                    case MIDI_META_EVENT_INSTRUMENT_NAME:
                        m_metaTextInfo.instrument = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] instrument: " << m_metaTextInfo.instrument;
                        break;
                    case MIDI_META_EVENT_LYRIC_TEXT:
                        m_metaTextInfo.lyric = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] lyric: " << m_metaTextInfo.lyric;
                        break;
                    case MIDI_META_EVENT_TEXT_MARKER:
                        m_metaTextInfo.marker = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] marker: " << m_metaTextInfo.marker;
                        break;
                    case MIDI_META_EVENT_CUE_POINT:
                        m_metaTextInfo.cue = std::string(event->event.meta.text.val);
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] cue: " << m_metaTextInfo.cue;
                        break;
                    }
                }
                else
                {
                    BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] found system event: " << Utils::toHex(event->message_meta, 1);
                    switch (event->message_meta)
                    {
                    case MIDI_META_EVENT_TRACK_END:
                        BOOST_LOG_TRIVIAL(info) << "[TrackAnalyzer] system event END OF TRACK";
                        break;
                    }
                }
            }
        }

        std::vector<MikrotikTrack> outTracks;
        std::for_each(m_sequences.begin(), m_sequences.end(), [&](Sequence &seq) {
            seq.setTrackInfo(m_metaTextInfo);
            auto tracks = seq.analyze();
            outTracks.insert(outTracks.end(), tracks.begin(), tracks.end());
        });

        return outTracks;
    }

private:
    Config m_config;
    std::size_t m_trackIndex = 0;
    uint64_t m_trackDuration = 0;
    std::array<Sequence, MIDI_CHANNELS_MAX_COUNT> m_sequences;
    TrackMetaTextInfo m_metaTextInfo;
};


File: /src\Utils.hpp
#pragma once

#include <iomanip>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

namespace Utils
{
static std::string toHexBuffer(std::vector<uint8_t> &buf)
{
    if (buf.size() == 0)
        return std::string();
    std::stringstream ss;
    for (std::size_t i = 0; i < buf.size(); i++)
    {
        ss << std::hex << std::uppercase << std::setfill('0') << std::setw(2) << ((int)buf[i]) << " " << std::dec;
    }
    return ss.str();
}

static std::string toHex(uint64_t val, size_t width)
{
    std::stringstream ss;
    ss << "0x" << std::hex << std::uppercase << std::setfill('0') << std::setw(width) << ((int64_t)val) << std::dec;
    return ss.str();
}

static std::string getTimeAsText(const double time)
{
    std::stringstream out;
    out << std::setfill('0') << std::setw(2) << ((static_cast<int>(time) / (1000 * 60 * 60)) % 24) << ":";
    out << std::setfill('0') << std::setw(2) << ((static_cast<int>(time) / (1000 * 60)) % 60) << ":";
    out << std::setfill('0') << std::setw(2) << ((static_cast<int>(time) / 1000) % 60) << ":";
    out << std::setfill('0') << std::setw(3) << ((static_cast<int>(time) % 1000));
    return out.str();
}

static std::string getDelayLine(const float duration)
{
    /*
     * :delay 1000ms;
     */

    return ":delay " + std::to_string((int)duration) + "ms;\n";
}

}; // namespace Utils


