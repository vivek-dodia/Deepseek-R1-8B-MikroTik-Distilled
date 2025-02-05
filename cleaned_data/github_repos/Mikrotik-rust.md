# Repository Information
Name: Mikrotik-rust

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-rust/
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
    │   │       ├── pack-48cfa80fc9cb98da2d3dc996004cf6004ef82d02.idx
    │   │       └── pack-48cfa80fc9cb98da2d3dc996004cf6004ef82d02.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .travis.yml
    ├── Cargo.lock
    ├── Cargo.toml
    ├── example.rs
    ├── README.md
    └── src/
        └── routeros.rs


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
	url = https://github.com/woowe/Mikrotik-rust.git
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
0000000000000000000000000000000000000000 69aea2f3495b4f5130723a56a4d2a99f16839425 vivek-dodia <vivek.dodia@icloud.com> 1738606055 -0500	clone: from https://github.com/woowe/Mikrotik-rust.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 69aea2f3495b4f5130723a56a4d2a99f16839425 vivek-dodia <vivek.dodia@icloud.com> 1738606055 -0500	clone: from https://github.com/woowe/Mikrotik-rust.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 69aea2f3495b4f5130723a56a4d2a99f16839425 vivek-dodia <vivek.dodia@icloud.com> 1738606055 -0500	clone: from https://github.com/woowe/Mikrotik-rust.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
69aea2f3495b4f5130723a56a4d2a99f16839425 refs/remotes/origin/master


File: /.git\refs\heads\master
69aea2f3495b4f5130723a56a4d2a99f16839425


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/target
/Cargo.lock


File: /.travis.yml
language: rust


File: /Cargo.lock
[root]
name = "routeros_rust"
version = "0.0.2"
dependencies = [
 "rust-crypto 0.2.31 (registry+https://github.com/rust-lang/crates.io-index)",
]

[[package]]
name = "gcc"
version = "0.3.5"
source = "registry+https://github.com/rust-lang/crates.io-index"

[[package]]
name = "libc"
version = "0.1.6"
source = "registry+https://github.com/rust-lang/crates.io-index"

[[package]]
name = "rand"
version = "0.3.8"
source = "registry+https://github.com/rust-lang/crates.io-index"
dependencies = [
 "libc 0.1.6 (registry+https://github.com/rust-lang/crates.io-index)",
]

[[package]]
name = "rust-crypto"
version = "0.2.31"
source = "registry+https://github.com/rust-lang/crates.io-index"
dependencies = [
 "gcc 0.3.5 (registry+https://github.com/rust-lang/crates.io-index)",
 "libc 0.1.6 (registry+https://github.com/rust-lang/crates.io-index)",
 "rand 0.3.8 (registry+https://github.com/rust-lang/crates.io-index)",
 "rustc-serialize 0.3.14 (registry+https://github.com/rust-lang/crates.io-index)",
 "time 0.1.25 (registry+https://github.com/rust-lang/crates.io-index)",
]

[[package]]
name = "rustc-serialize"
version = "0.3.14"
source = "registry+https://github.com/rust-lang/crates.io-index"

[[package]]
name = "time"
version = "0.1.25"
source = "registry+https://github.com/rust-lang/crates.io-index"
dependencies = [
 "gcc 0.3.5 (registry+https://github.com/rust-lang/crates.io-index)",
 "libc 0.1.6 (registry+https://github.com/rust-lang/crates.io-index)",
]



File: /Cargo.toml
[package]

name = "routeros_rust"
version = "0.0.2"
authors = ["Jason Cardinal <jasonfowl1234@yahoo.com>"]
repository = "https://github.com/Wooowe/mikrotik-rust"
description = "Mikrotik API for Rust"
readme = "README.md"
license = "GPL-3.0"

keywords = ["Mikrotik", "Router Os", "Router Os API"]

[lib]
name = "router_os"
path = "src/routeros.rs"

[[bin]]
name = "example"
path = "example.rs"

[dependencies]
rust-crypto = "0.2.31"


File: /example.rs

extern crate router_os;

use router_os::ApiRos;


use std::net::TcpStream;
use std::io::BufRead;
use std::io;

fn get_line() -> String {
    let stdin_u = io::stdin();
    let mut stdin = stdin_u.lock();
    let mut line = String::new();
    stdin.read_line(&mut line).unwrap();
	line.pop();
    return line;
}

fn main() {
	let mut stream = TcpStream::connect("192.168.1.1:8728").unwrap();

	let mut apiros = ApiRos::new(&mut stream);
	apiros.login("username".to_string(), "password".to_string());

	let mut input_sentence: Vec<String> = Vec::new();
	let mut has_written = false;
	let mut was_command = false;

	println!("Type '#quit#' to exit program");

	'main_loop: loop {
		if has_written {
			'reply_loop: loop {
				let replies = apiros.read_sentence();
				if replies.len() == 0 {
					continue;
				}
				if replies[0] == "!done" {
					has_written = false;
					break 'reply_loop;
				}
			}
		}else {
			let input = get_line();

			if &input[..] == "#quit#" {
				break 'main_loop;
			}

			if &input[..] == "" && was_command {
				apiros.write_sentence(input_sentence.clone());
				input_sentence.clear();
				was_command = false;
				has_written = true;
			}else {
				input_sentence.push(input);
				was_command = true;
				has_written = false;
			}
		}
	}

	println!("Goodbye!");
}


File: /README.md
Router Os
================
Mikrotik API for Rust

This API gives you the ability to connect to your mikrotik router over a tcp connection.

[![Build Status](https://travis-ci.org/Wooowe/Mikrotik-rust.svg?branch=master)](https://travis-ci.org/Wooowe/Mikrotik-rust) [![Latest Version](https://img.shields.io/badge/crates.io-0.0.21-orange.svg)](https://crates.io/crates/routeros_rust)

### Installation

Add router_os via your `Cargo.toml`:
```toml
[dependencies]
routeros_rust = "*"
```

#### or

```toml
[dependencies.routeros_rust]
git = "https://github.com/Wooowe/mikrotik-rust"
```

### Usage
```rs
extern crate router_os;

use router_os::ApiRos;
use std::net::TcpStream;

fn main() {
    let mut stream = TcpStream::connect("192.168.1.1:8728").unwrap();

    let mut apiros = ApiRos::new(&mut stream);
    apiros.login("admin".to_string(), "".to_string());

    apiros.write_sentence(vec!["/ip/address/print".to_string()]);

    loop {
        let reply = apiros.read_sentence();

        if reply.len() == 0 {
            continue;
        }

        if reply[0] == "!done" {
            break;
        }
    }
}
```


File: /src\routeros.rs
#![crate_name = "router_os"]
#![crate_type = "lib"]

extern crate crypto;

use crypto::md5::Md5;
use crypto::digest::Digest;

use std::collections::BTreeMap;
use std::io::prelude::*;
use std::net::TcpStream;

fn hex_binascii<'a>(hexstr: String) -> Result<Vec<u8>, &'a str> {
	if hexstr.len() % 2 != 0 {
		Err("Odd number of characters")
	}else {
		let mut result: Vec<u8> = Vec::new();
		let mut i = 0;
		let c_hexstr: Vec<char> = hexstr.chars().collect();
		while i < c_hexstr.len()-1 {
		    let top = c_hexstr[i].to_digit(16).unwrap() as u8;
		    let bottom = c_hexstr[i+1].to_digit(16).unwrap() as u8;
		    let r = (top << 4) + bottom;

			result.push(r);

		    i += 2;
		}
		Ok(result)
	}
}


pub struct ApiRos<'a> {
	stream: &'a mut TcpStream,
}

impl<'a> ApiRos<'a> {

	pub fn new(s: &'a mut TcpStream) -> ApiRos<'a> {
		ApiRos {
			stream: s
		}
	}

	pub fn try_read(&mut self) -> bool {
		if self.stream.read(&mut [0]).unwrap() > 0 {
			true
		}else {
			false
		}
	}

    fn write_str(&mut self, str_buff: &[u8]) {
        match self.stream.write(str_buff) {
            Ok(_) => {}
			Err(e) => { panic!("connection closed by remote end, {}", e); }
		}
	}

    fn read_str(&mut self, length: usize) -> String {
        let mut buff: Vec<u8> = Vec::new();
        for _ in 0 .. length {
			let mut tmp_buff: [u8; 1] = [0];
			match self.stream.read(&mut tmp_buff) {
				Ok(_) => {}
				Err(e) => { panic!("connection closed by remote end, {}", e); }
			}
			buff.push(tmp_buff[0]);
		}
		String::from_utf8(buff).unwrap()
	}

	fn write_len(&mut self, len: u32) {
        if len < 0x80 {
            self.write_str(&[len as u8]);
		} else if len < 0x4000 {
            let l = len | 0x8000;
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else if len < 0x200000 {
            let l = len | 0xC00000;
            self.write_str( &[((l >> 16) & 0xFF) as u8] );
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else if len < 0x10000000 {
            let l = len | 0xE0000000;
            self.write_str( &[((l >> 16) & 0xFF) as u8] );
            self.write_str( &[((l >> 24) & 0xFF) as u8] );
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else {
            self.write_str( &[(0xF0) as u8] );
            self.write_str( &[((len >> 24) & 0xFF) as u8] );
            self.write_str( &[((len >> 16) & 0xFF) as u8] );
            self.write_str( &[((len >> 8) & 0xFF) as u8] );
            self.write_str( &[(len & 0xFF) as u8] );
		}
	}

    fn read_len(&mut self) -> u32 {
        let mut c: u32 = self.read_str(1).as_bytes()[0] as u32;
        if c & 0x80 == 0x00 {

		} else if c & 0xC0 == 0x80 {
            c &= !0xC0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xE0 == 0xC0 {
            c &= !0xE0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xF0 == 0xE0 {
            c &= !0xF0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xF8 == 0xF0 {
            c = self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
		}
		c
	}

	fn read_word(&mut self) -> String {
		let len = self.read_len();
		let ret = self.read_str(len as usize);
		ret
	}

	fn write_word(&mut self, w: String) {
		self.write_len(w.len() as u32);
		self.write_str(&w.as_bytes());
	}

	pub fn write_sentence(&mut self, words: Vec<String>) -> u32{
		let mut ret: u32 = 0;
		for w in words {
			self.write_word(w);
			ret += 1;
		}
		self.write_word("".to_string());
		ret
	}

	pub fn read_sentence(&mut self) -> Vec<String>  {
		let mut r: Vec<String> = Vec::new();
		loop {
			let w = self.read_word();
			if &w[..] == "" {
				return r;
			}
			r.push(w);
		}
	}


	fn talk(&mut self, words: Vec<String>) -> Vec<(String, BTreeMap<String, String>)>{
		if self.write_sentence(words) == 0 {
			return vec![];
		}

		let mut r: Vec<(String, BTreeMap<String, String>)> = Vec::new();

		loop {
			let i: Vec<String> = self.read_sentence();
			if i.len() == 0 {
				continue;
			}

			let reply: String = i[0].clone();
			let mut attrs: BTreeMap<String, String> = BTreeMap::new();

			for w in &i[1..] {
				match w[1..].find("=") {
					Some(n) => { attrs.insert( 	w[..n+1].to_string() ,
												w[(n+2)..].to_string() ); }

					None    => { attrs.insert(w.clone(), "".to_string()); }
				};
			}
			r.push((reply.clone(), attrs));
			if reply == "!done" {
				return r;
			}
		}

	}

	pub fn login(&mut self, username: String, pwd: String) {
		let mut chal: Vec<u8> = Vec::new();
		for (_ /*reply*/, attrs) in self.talk(vec![r"/login".to_string()]) {
			chal = hex_binascii(attrs["=ret"].clone()).unwrap();
		}

		let mut md = Md5::new();
		md.input(&[0]);
		md.input(pwd.as_bytes());
		md.input(&chal[..]);

		self.talk(vec![r"/login".to_string(), format!("=name={}", username),
						format!("=response=00{}",md.result_str())]);
	}
}


