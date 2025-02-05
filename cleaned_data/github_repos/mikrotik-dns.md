# Repository Information
Name: mikrotik-dns

# Directory Structure
Directory structure:
└── github_repos/mikrotik-dns/
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
    │   │       ├── pack-dc98dd6ee745217064bdb3d0d7a475a9c823c594.idx
    │   │       └── pack-dc98dd6ee745217064bdb3d0d7a475a9c823c594.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   ├── dependabot.yaml
    │   └── workflows/
    │       └── tests.yaml
    ├── .gitignore
    ├── go.mod
    ├── go.sum
    ├── LICENSE
    ├── main.go
    ├── Makefile
    ├── mikrotik.go
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
	url = https://github.com/middelink/mikrotik-dns.git
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
0000000000000000000000000000000000000000 3ae643f10ee4ff7ef4b6ca2e831c637e474c811f vivek-dodia <vivek.dodia@icloud.com> 1738606327 -0500	clone: from https://github.com/middelink/mikrotik-dns.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 3ae643f10ee4ff7ef4b6ca2e831c637e474c811f vivek-dodia <vivek.dodia@icloud.com> 1738606327 -0500	clone: from https://github.com/middelink/mikrotik-dns.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3ae643f10ee4ff7ef4b6ca2e831c637e474c811f vivek-dodia <vivek.dodia@icloud.com> 1738606327 -0500	clone: from https://github.com/middelink/mikrotik-dns.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3ae643f10ee4ff7ef4b6ca2e831c637e474c811f refs/remotes/origin/master
5de8b1ed192c772db54527da284e7297fdef034d refs/tags/v0.8


File: /.git\refs\heads\master
3ae643f10ee4ff7ef4b6ca2e831c637e474c811f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\dependabot.yaml
version: 2
updates:
  # Dependencies listed in go.mod
  - package-ecosystem: "gomod"
    directory: "/" # Location of package manifests
    schedule:
      interval: "weekly"

  # Dependencies listed in .github/workflows/*.yml
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"


File: /.github\workflows\tests.yaml
name: test

on:
  push:
    branches:
      - master
  pull_request:

permissions:
  contents: read
  # Optional: allow read access to pull request. Use with `only-new-issues` option.
  # pull-requests: read

env:
  latest_go: "1.21.x"
  GO111MODULE: on
  GOPROXY: https://proxy.golang.org

jobs:
  test:
    name: Go test
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go ${{ env.latest_go }}
        uses: actions/setup-go@v5
        with:
          go-version: ${{ env.latest_go }}

      - name: Build
        run: |
          go build .

      - name: Run tests
        run: |
          go test ./...

  lint:
    name: lint
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go ${{ env.latest_go }}
        uses: actions/setup-go@v5
        with:
          go-version: ${{ env.latest_go }}

      - name: golangci-lint
        uses: golangci/golangci-lint-action@v6
        with:
          # Require: The version of golangci-lint to use.
          # When `install-mode` is `binary` (default) the value can be v1.2 or v1.2.3 or `latest` to use the latest version.
          # When `install-mode` is `goinstall` the value can be v1.2.3, `latest`, or the hash of a commit.
          version: v1.54

          # Optional: working directory, useful for monorepos
          # working-directory: somedir

          # Optional: golangci-lint command line arguments.
          #
          # Note: By default, the `.golangci.yml` file should be at the root of the repository.
          # The location of the configuration file can be changed by using `--config=`
          # args: --timeout=30m --config=/my/path/.golangci.yml --issues-exit-code=0 

          # Optional: show only new issues if it's a pull request. The default value is `false`.
          # only-new-issues: true

          # Optional: if set to true, then all caching functionality will be completely disabled,
          #           takes precedence over all other caching options.
          # skip-cache: true

          # Optional: if set to true, then the action won't cache or restore ~/go/pkg.
          # skip-pkg-cache: true

          # Optional: if set to true, then the action won't cache or restore ~/.cache/go-build.
          # skip-build-cache: true

          # Optional: The mode to install golangci-lint. It can be 'binary' or 'goinstall'.
          # install-mode: "goinstall"

      - name: Check go.mod/go.sum
        run: |
          echo "check if go.mod and go.sum are up to date"
          go mod tidy
          git diff --exit-code go.mod go.sum


File: /.gitignore
*.exe
*.test
*.prof

mikrotik-dns
run.sh


File: /go.mod
module github.com/middelink/mikrotik-dns

go 1.21

require (
	github.com/go-routeros/routeros/v3 v3.0.0
	github.com/miekg/dns v1.1.63
)

require (
	golang.org/x/mod v0.18.0 // indirect
	golang.org/x/net v0.33.0 // indirect
	golang.org/x/sync v0.7.0 // indirect
	golang.org/x/sys v0.28.0 // indirect
	golang.org/x/tools v0.22.0 // indirect
)


File: /go.sum
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-routeros/routeros/v3 v3.0.0 h1:/V4Cgr+wmn3IyyYIXUX1KYK8pA1ADPiwLSlAi912j1M=
github.com/go-routeros/routeros/v3 v3.0.0/go.mod h1:j4mq65czXfKtHsdLkgVv8w7sNzyhLZy1TKi2zQDMpiQ=
github.com/miekg/dns v1.1.63 h1:8M5aAw6OMZfFXTT7K5V0Eu5YiiL8l7nUAkyN6C9YwaY=
github.com/miekg/dns v1.1.63/go.mod h1:6NGHfjhpmr5lt3XPLuyfDJi5AXbNIPM9PY6H6sF1Nfs=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
golang.org/x/mod v0.18.0 h1:5+9lSbEzPSdWkH32vYPBwEpX8KwDbM52Ud9xBUvNlb0=
golang.org/x/mod v0.18.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.33.0 h1:74SYHlV8BIgHIFC/LrYkOGIwL19eTYXQ5wc6TBuO36I=
golang.org/x/net v0.33.0/go.mod h1:HXLR5J+9DxmrqMwG9qjGCxZ+zKXxBru04zlTvWlWuN4=
golang.org/x/sync v0.7.0 h1:YsImfSBoP9QPYL0xyKJPq0gcaJdG3rInoqxTWbfQu9M=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.28.0 h1:Fksou7UEQUWlKvIdsqzJmUmCX3cZuD2+P3XyyzwMhlA=
golang.org/x/sys v0.28.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/tools v0.22.0 h1:gqSGLZqv+AI9lIQzniJ0nZDRG5GBPsSi+DRNHWNz6yA=
golang.org/x/tools v0.22.0/go.mod h1:aCwcsjqvq7Yqt6TNyX7QMU2enbQ/Gt0bo6krSeEri+c=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=


File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {description}
    Copyright (C) {year}  {fullname}

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  {signature of Ty Coon}, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.


File: /main.go
package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"net/url"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strings"

	"github.com/miekg/dns"
)

var (
	version = "dev"

	dnsFilter  = flag.String("dnsfilter", "", "comma separated list of dns prefixes to filter")
	address    = flag.String("address", "", "url like address of the MT to connect to `api://user:pass@host`. use apis for encrypted connections.")
	debug      = flag.Bool("debug", false, "run the program but do not make any changes on the Mikrotik")
	verbose    = flag.Bool("verbose", false, "be more verbose")
	useDNS     = flag.Bool("use_dns", false, "maintain static dns table from zone")
	useDHCP    = flag.Bool("use_dhcp", false, "maintain dhcp table based upon '; dhcp:<mac>' mac comments on the A records")
	hasVersion = flag.Bool("version", false, "output version information and exit")
)

func main() {
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), `Usage: %s [OPTION]... ZONE...

When --use_dns is given, this tool copies compatible RRs from the given zones
into the Mikrotiks static DNS table. This can for example be used in emergency
modes where the local nameserver is down, but the organisation still requires
an internal DNS in the mean time. Unknown entries from the static DNS table
will be removed!

When --use_dhcp is given, all A records from the given zones which have a
comment matching 'dhcp:<mac address>' will update the Mikrotiks DHCP table.
Unknown entries from the DHCP table will be removed!

`, os.Args[0])

		flag.PrintDefaults()
	}
	flag.Parse()

	if *hasVersion {
		fmt.Printf("mikrotik-dns version %s %s/%s\n", version, runtime.GOOS, runtime.GOARCH)
		return
	}

	if flag.NArg() < 1 {
		log.Fatalf("At least one zone file is required, none given")
	}

	dnsPrefixes := strings.Fields(strings.ReplaceAll(*dnsFilter, ",", " "))

	mtURL, err := url.Parse(*address)
	if err != nil {
		log.Fatalf("Unable to parse --address: %v", err)
	}
	if mtURL.Scheme != "api" && mtURL.Scheme != "apis" {
		log.Fatalf("Invalid scheme, expecting `api` or `apis`, not %v", mtURL.Scheme)
	}
	if mtURL.Opaque != "" || mtURL.Path != "" || mtURL.RawPath != "" || mtURL.RawQuery != "" || mtURL.Fragment != "" {
		log.Printf("Ignorning extra parts from url: %q", mtURL)
	}

	passwd, _ := mtURL.User.Password()
	mt, err := NewMikrotik("first", mtURL.Host, mtURL.User.Username(), passwd, mtURL.Scheme == "apis")
	if err != nil {
		log.Fatalf("Unable to connect to %s: %v", mtURL.Host, err)
	}

	var existingRRs map[string]dns.RR
	if existingRRs, err = mt.fetchDNSlist(); err != nil {
		mt.client.Close()
		log.Fatalf("Unable to fetch existing DNS entries: %v", err)
	}
	fmt.Printf("%d existing RRs found\n", len(existingRRs))

	mtRRs := map[uint16]struct{}{
		dns.TypeA:     {},
		dns.TypeAAAA:  {},
		dns.TypeCNAME: {},
		dns.TypeMX:    {},
		dns.TypeNS:    {},
		dns.TypeSRV:   {},
		dns.TypeTXT:   {},
	}

	var dhcpservers map[string][]*net.IPNet
	if *useDHCP {
		dhcpservers, err = mt.fetchDHCPNets()
		if err != nil {
			log.Fatalf("Unable to fetch existing DHCP servers: %v", err)
		}
	}

	zoneRRs := []dns.RR{}
	MACs := []DHCP{}
	for _, zonefile := range flag.Args() {
		origin := strings.TrimSuffix(filepath.Base(zonefile), ".db")

		stream, _ := os.Open(zonefile)
		scanner := dns.NewZoneParser(stream, origin, zonefile)

		for {
			rr, ok := scanner.Next()
			if !ok {
				if scanner.Err() != nil {
					fmt.Printf("error reading token: %v\n", scanner.Err())
				}
				break
			}

			if _, ok := mtRRs[rr.Header().Rrtype]; ok {
				found := false
				for _, p := range dnsPrefixes {
					if strings.HasPrefix(rr.Header().Name, p) {
						found = true
						break
					}
				}
				if !found {
					for _, zoneRR := range zoneRRs {
						if dns.IsDuplicate(rr, zoneRR) && rr.Header().Ttl == zoneRR.Header().Ttl {
							log.Fatalf("Duplicate entry found (%v)\n", rr.Header().Name)
						}
					}
					zoneRRs = append(zoneRRs, rr)
				}
			}

			if *useDHCP {
				cmtMap := mapComments(scanner.Comment())
				if rr.Header().Rrtype == dns.TypeA && cmtMap["dhcp"] != "" {
					hw, err := net.ParseMAC(cmtMap["dhcp"])
					if err != nil {
						fmt.Printf("parseMAC failed (%q): %v", cmtMap["dhcp"], err)
						continue
					}
					server := ""
				outside:
					for srv, nets := range dhcpservers {
						for _, net := range nets {
							if net.Contains(rr.(*dns.A).A) {
								server = srv
								break outside
							}
						}
					}
					if server != "" {
						suffix := ""
						if _, ok := cmtMap["static"]; ok {
							suffix = " (static)"
						}
						MACs = append(MACs, DHCP{Comment: rr.Header().Name + suffix, Server: server, IP: rr.(*dns.A).A, MAC: hw})
					} else if *verbose {
						fmt.Printf("[WARNING] Could not find a matching dhcp server for ip %v\n", rr.(*dns.A).A)
					}
				}
			}
		}
	}
	if *useDNS {
		sort.Slice(zoneRRs, func(i, j int) bool {
			if zoneRRs[i].Header().Rrtype < zoneRRs[j].Header().Rrtype {
				return true
			}
			if zoneRRs[i].Header().Rrtype == zoneRRs[j].Header().Rrtype && zoneRRs[i].Header().Name < zoneRRs[j].Header().Name {
				return true
			}
			return false
		})
		fmt.Printf("%v zone RR found\n", len(zoneRRs))

		// Prune the lists
		fmt.Println("Pruning lists for duplicates")
		for k, existingRR := range existingRRs {
			for i, r := range zoneRRs {
				if dns.IsDuplicate(existingRR, r) && r.Header().Ttl == existingRR.Header().Ttl {
					// Delete found element from both lists.
					zoneRRs = append(zoneRRs[:i], zoneRRs[i+1:]...)
					delete(existingRRs, k)
					break
				}
			}
		}

		fmt.Printf("%d existing RRs to be removed\n", len(existingRRs))
		for k, v := range existingRRs {
			fmt.Printf("%v: %v\n", k, v)
			if !*debug {
				if err := mt.DelDNS(k); err != nil {
					log.Printf("unable to remove DNS entry (%v, %v): %v", k, v, err)
				}
			}
		}
		fmt.Printf("%d missing RRs to be added\n", len(zoneRRs))
		for k, v := range zoneRRs {
			fmt.Printf("%v: %v\n", k, v)
			if !*debug {
				if err := mt.AddDNS(v, ""); err != nil {
					log.Printf("unable to add DNS entry (%v, %v): %v", k, v, err)
				}
			}
		}
	}

	if *useDHCP {
		existingDHCP, _ := mt.fetchDHCP()
		fmt.Printf("%d existing DHCP entries found\n", len(existingDHCP))
		fmt.Printf("%d zone DHCP entries found\n", len(MACs))

		fmt.Printf("Pruning duplicate DHCP entries\n")
		for k, dhcp := range existingDHCP {
			for i, d := range MACs {
				if dhcp.Comment == d.Comment && dhcp.Server == d.Server && dhcp.IP.String() == d.IP.String() && dhcp.MAC.String() == d.MAC.String() {
					// Delete found element from both lists.
					MACs = append(MACs[:i], MACs[i+1:]...)
					delete(existingDHCP, k)
					break
				}
			}
		}

		fmt.Printf("%d existing DHCP entries to be removed\n", len(existingDHCP))
		for k, v := range existingDHCP {
			fmt.Printf("  %v: %v\n", k, v)
			if !*debug {
				if err := mt.DelDHCP(k); err != nil {
					log.Printf("unable to remove DHCP entry (%v, %v): %v", k, v, err)
				}
			}
		}

		fmt.Printf("%d missing DHCP entries to be added\n", len(MACs))
		for k, v := range MACs {
			fmt.Printf("  %v: %v\n", k, v)
			if !*debug {
				if err := mt.AddDHCP(v); err != nil {
					log.Printf("unable to add DHCP entry (%v, %v): %v", k, v, err)
				}
			}
		}
	}
}

func mapComments(cmt string) map[string]string {
	m := make(map[string]string, 2)
	for _, c := range strings.Fields(strings.TrimPrefix(cmt, ";")) {
		if pos := strings.Index(c, ":"); pos < 0 {
			m[c] = ""
		} else {
			m[c[:pos]] = c[pos+1:]
		}
	}
	return m
}


File: /Makefile
.PHONY: clean build test

export GO111MODULE=on
export CGO_ENABLED=0

MAIN_DIRECTORY := .
BIN_OUTPUT := $(if $(filter $(shell go env GOOS), windows), mikrotik-dns.exe, mikrotik-dns)

TAG_NAME := $(shell git tag -l --contains HEAD)
SHA := $(shell git rev-parse HEAD)
VERSION := $(if $(TAG_NAME),$(TAG_NAME),$(SHA))

default: clean test build

clean:
	@echo BIN_OUTPUT: ${BIN_OUTPUT}
	rm -rf ${BIN_OUTPUT} cover.out

build: clean
	@echo Version: $(VERSION)
	go build -v -trimpath -ldflags '-X "main.version=${VERSION}"' -o ${BIN_OUTPUT} ${MAIN_DIRECTORY}

test: clean
	go test -v -cover ./...


File: /mikrotik.go
package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"

	ros "github.com/go-routeros/routeros/v3"
	"github.com/miekg/dns"
)

var (
	// 28w4d23h59m56s
	regTimeout = regexp.MustCompile(`(?:(\d+)w)?(?:(\d+)d)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?`)
)

// Mikrotik contains the internal state of a Mikrotik object, configuration
// details but also the API connection to the Mikrotik. It acts as a cache
// between the rest of the program and the Mikrotik.
type Mikrotik struct {
	conn   net.Conn
	client *ros.Client
	lock   sync.Mutex // prevent AddRR/DelRR racing

	Name    string
	Version float64 // E.g. 7.17

	Address string
	User    string
	Passwd  string
}

// DHCP contains a single dhcp entry.
type DHCP struct {
	Comment string // the comment for the dhcp entry.
	Server  string // one of the MTs dhcp servers.
	IP      net.IP
	MAC     net.HardwareAddr
}

func (d DHCP) String() string {
	return fmt.Sprintf("{%q %v %v %v}", d.Comment, d.Server, d.IP, d.MAC)
}

// Setup a deadline on the connection to the Mikrotik. It returns a cancel
// function, resetting the idle deadline on the connection.
func (mt *Mikrotik) startDeadline(duration time.Duration) func() {
	_ = mt.conn.SetDeadline(time.Now().Add(duration))
	return func() { _ = mt.conn.SetDeadline(time.Time{}) }
}

// NewMikrotik returns an initialized Mikrotik object.
func NewMikrotik(name, address, user, passwd string, useTLS bool) (*Mikrotik, error) {
	// Add port 8728/8729 if it was not included
	_, _, err := net.SplitHostPort(address)
	if err != nil {
		// For anything else than missing port, bail.
		if !strings.Contains(err.Error(), "missing port in address") {
			return nil, fmt.Errorf("%s: malformed address: %v", name, err)
		}
		if useTLS {
			address = net.JoinHostPort(address, "8729")
		} else {
			address = net.JoinHostPort(address, "8728")
		}
	}

	if *debug {
		log.Printf("NewMikrotik(name=%s, address=%s, user=%s, passwd=%s)\n", name, address, user, passwd)
	} else if *verbose {
		log.Printf("NewMikrotik(name=%s)\n", name)
	}

	mt := &Mikrotik{
		Name:    name,
		Address: address,
		User:    user,
		Passwd:  passwd,
	}
	// Open the connection, use our own code for this, as we need
	// access to it for setting deadlines.
	dialer := new(net.Dialer)
	dialer.Timeout = time.Minute
	if useTLS {
		mt.conn, err = tls.DialWithDialer(dialer, "tcp", mt.Address, nil)
	} else {
		mt.conn, err = dialer.Dial("tcp", mt.Address)
	}
	if err != nil {
		return nil, err
	}
	mt.client, err = ros.NewClient(mt.conn)
	if err != nil {
		mt.conn.Close()
		return nil, err
	}

	cancel := mt.startDeadline(5 * time.Second)
	err = mt.client.Login(mt.User, mt.Passwd)
	cancel()
	if err != nil {
		mt.client.Close()
		return nil, err
	}
	if mt.Version, err = mt.fetchVersion(); err != nil {
		mt.client.Close()
		return nil, err
	}

	if _, err := mt.fetchDNSlist(); err != nil {
		mt.client.Close()
		return nil, err
	}

	return mt, nil
}

func toDuration(ttl string) uint32 {
	res := regTimeout.FindStringSubmatch(ttl)
	var duration time.Duration
	if res[1] != "" {
		weeks, _ := strconv.Atoi(res[1])
		duration += time.Duration(weeks) * 7 * 24 * time.Hour
	}
	if res[2] != "" {
		days, _ := strconv.Atoi(res[2])
		duration += time.Duration(days) * 24 * time.Hour
	}
	if res[3] != "" {
		hours, _ := strconv.Atoi(res[3])
		duration += time.Duration(hours) * time.Hour
	}
	if res[4] != "" {
		minutes, _ := strconv.Atoi(res[4])
		duration += time.Duration(minutes) * time.Minute
	}
	if res[5] != "" {
		seconds, _ := strconv.Atoi(res[5])
		duration += time.Duration(seconds) * time.Second
	}
	return uint32(duration.Seconds())
}

func toSeconds(seconds uint32) string {
	dur := time.Duration(seconds) * time.Second
	str := ""
	if dur >= 24*time.Hour {
		days := int(dur / 24 / time.Hour)
		str = fmt.Sprintf("%dd ", days)
		dur -= time.Duration(days) * 24 * time.Hour
	}
	str += fmt.Sprintf("%02d:%02d:%02d", dur/time.Hour, dur/time.Minute%60, dur/time.Second%60)
	return str
}

func nameToRegexp(s string) string {
	if !strings.HasPrefix(s, "*.") {
		return s
	}

	// Detected wildcard RR. See https://en.wikipedia.org/wiki/Wildcard_DNS_record
	s = strings.TrimSuffix(s[1:], ".")
	return "^.*" + strings.ReplaceAll(s, ".", "\\.") + "$"
}

func regexpToName(s string) string {
	s = strings.TrimPrefix(s, "^")
	s = strings.ReplaceAll(s, ".*", "*")
	s = strings.TrimSuffix(s, "$")
	return strings.ReplaceAll(s, "\\.", ".")
}

func (mt *Mikrotik) fromFQDN(s string) string {
	if mt.Version >= 7.17 {
		return strings.TrimSuffix(s, ".")
	}
	return s
}

func (mt *Mikrotik) toFQDN(s string) string {
	if mt.Version >= 7.17 {
		return strings.TrimSuffix(s, ".") + "."
	}
	return s
}

func (mt *Mikrotik) fetchDNSlist() (map[string]dns.RR, error) {

	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.Run("/ip/dns/static/print", ".proplist=type")
	cancel()
	if err != nil {
		return nil, err
	}
	rrs := make(map[string]dns.RR, len(reply.Re))
	var rr dns.RR
	for _, re := range reply.Re {
		ttl := toDuration(re.Map["ttl"])
		name := mt.toFQDN(re.Map["name"])
		if v, ok := re.Map["regexp"]; ok {
			name = mt.toFQDN(regexpToName(v))
		}
		switch re.Map["type"] {
		case "": // mikrotik 6.47.3+ no longer return the type for "A" records. (Why? Is it the default?)
			fallthrough
		case "A":
			// dns entry: "!re @ [{`.id` `*1`} {`name` `router.polyware.nl`} {`type` `A`} {`address` `192.168.10.1`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.A{Hdr:dns.RR_Header{Name:"router.polyware.nl", Rrtype:0x1, Class:0x1, Ttl:0x15180, Rdlength:0x0}, A:net.IP(nil)}
			r := new(dns.A)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeA, Class: dns.ClassINET, Ttl: ttl}
			r.A = net.ParseIP(re.Map["address"])
			rr = r
		case "AAAA":
			// dns entry: "!re @ [{`.id` `*6`} {`name` `rp1.polyware.nl`} {`type` `AAAA`} {`address` `2a02:58:96:ab00:2dda:94ea:a768:a3e5`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.AAAA{Hdr:dns.RR_Header{Name:"rp1.polyware.nl", Rrtype:0x1c, Class:0x1, Ttl:0x15180, Rdlength:0x0}, AAAA:net.IP(nil)}
			r := new(dns.AAAA)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeAAAA, Class: dns.ClassINET, Ttl: ttl}
			r.AAAA = net.ParseIP(re.Map["address"])
			rr = r
		case "CNAME":
			r := new(dns.CNAME)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeCNAME, Class: dns.ClassINET, Ttl: ttl}
			r.Target = mt.toFQDN(re.Map["cname"])
			rr = r
		case "MX":
			// dns entry: "!re @ [{`.id` `*13`} {`name` `2`} {`type` `MX`} {`mx-preference` `50`} {`mx-exchange` `smtp.polyware.nl`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.MX{Hdr:dns.RR_Header{Name:"2", Rrtype:0xf, Class:0x1, Ttl:0x15180, Rdlength:0x0}, Preference:0x0, Mx:""}
			r := new(dns.MX)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeMX, Class: dns.ClassINET, Ttl: ttl}
			pref, _ := strconv.Atoi(re.Map["mx-preference"])
			r.Preference = uint16(pref)
			r.Mx = mt.toFQDN(re.Map["mx-exchange"])
			rr = r
		case "NS":
			// dns entry: "!re @ [{`.id` `*16`} {`name` `5`} {`type` `NS`} {`ns` `something`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.NS{Hdr:dns.RR_Header{Name:"5", Rrtype:0x2, Class:0x1, Ttl:0x15180, Rdlength:0x0}, Ns:""}
			r := new(dns.NS)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeNS, Class: dns.ClassINET, Ttl: ttl}
			r.Ns = mt.toFQDN(re.Map["ns"])
			rr = r
		case "SRV":
			// dns entry: "!re @ [{`.id` `*14`} {`name` `3`} {`type` `SRV`} {`srv-priority` `1`} {`srv-weight` `2`} {`srv-port` `1883`} {`srv-target` `rp1.polyware.nl`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.SRV{Hdr:dns.RR_Header{Name:"3", Rrtype:0x21, Class:0x1, Ttl:0x15180, Rdlength:0x0}, Priority:0x0, Weight:0x0, Port:0x0, Target:""}
			prio, _ := strconv.Atoi(re.Map["srv-priority"])
			weight, _ := strconv.Atoi(re.Map["srv-weight"])
			port, _ := strconv.Atoi(re.Map["srv-port"])
			r := new(dns.SRV)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeSRV, Class: dns.ClassINET, Ttl: ttl}
			r.Priority = uint16(prio)
			r.Weight = uint16(weight)
			r.Port = uint16(port)
			r.Target = mt.toFQDN(re.Map["srv-target"])
			rr = r
		case "TXT":
			//dns entry: "!re @ [{`.id` `*15`} {`name` `4`} {`type` `TXT`} {`text` `spf thingy`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
			// dns.TXT{Hdr:dns.RR_Header{Name:"4", Rrtype:0x10, Class:0x1, Ttl:0x15180, Rdlength:0x0}, Txt:[]string(nil)}
			r := new(dns.TXT)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeTXT, Class: dns.ClassINET, Ttl: ttl}
			r.Txt = []string{re.Map["text"]}
			rr = r
		case "(unknown)":
			r := new(dns.NULL)
			r.Hdr = dns.RR_Header{Name: name, Rrtype: dns.TypeNULL, Class: dns.ClassINET, Ttl: ttl}
			rr = r
		default:
			return nil, fmt.Errorf("unknown dns type: %v", re)
		}
		rrs[re.Map[".id"]] = rr
	}
	return rrs, nil
}

// fetchDHCP returns a map of all the static DHCP leases on the Mikrotik.
func (mt *Mikrotik) fetchDHCP() (map[string]DHCP, error) {

	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.Run("/ip/dhcp-server/lease/print")
	cancel()
	if err != nil {
		return nil, err
	}
	macs := make(map[string]DHCP, len(reply.Re))
	// dhcp: map[.id:*7B address:192.168.10.2 address-lists: blocked:false comment:pve dhcp-option: disabled:false dynamic:false last-seen:3d10h3m53s mac-address:60:45:CB:A8:76:7D radius:false server:dhcp1 status:waiting]
	for _, re := range reply.Re {
		if re.Map["dynamic"] == "false" {
			ip := net.ParseIP(re.Map["address"])
			mac, _ := net.ParseMAC(re.Map["mac-address"])
			macs[re.Map[".id"]] = DHCP{Comment: re.Map["comment"], Server: re.Map["server"], IP: ip, MAC: mac}
		}
	}
	return macs, nil
}

// fetchDHCPNets returns a map of active dhcp server and the ip range they listen to.
func (mt *Mikrotik) fetchDHCPNets() (map[string][]*net.IPNet, error) {

	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.Run("/ip/address/print")
	cancel()
	if err != nil {
		return nil, err
	}
	intfs := make(map[string][]*net.IPNet, len(reply.Re))
	for _, re := range reply.Re {
		// map[.id:*1 actual-interface:bridge-local address:192.168.10.1/24 disabled:false dynamic:false interface:bridge-local invalid:false network:192.168.10.0]
		if re.Map["disabled"] == "false" && re.Map["dynamic"] == "false" {
			_, ipnet, err := net.ParseCIDR(re.Map["address"])
			if err != nil {
				return nil, err
			}
			name := re.Map["actual-interface"]
			if intfs[name] == nil {
				intfs[name] = []*net.IPNet{ipnet}
			} else {
				intfs[name] = append(intfs[name], ipnet)
			}
		}
	}

	cancel = mt.startDeadline(5 * time.Second)
	reply, err = mt.client.Run("/ip/dhcp-server/print")
	cancel()
	if err != nil {
		return nil, err
	}
	dhcps := make(map[string][]*net.IPNet, len(reply.Re))
	for _, re := range reply.Re {
		// map[.id:*1 address-pool:default-dhcp authoritative:yes disabled:false dynamic:false interface:bridge-local invalid:false lease-script: lease-time:20m name:dhcp1 use-radius:no]
		if re.Map["disabled"] == "false" && re.Map["dynamic"] == "false" {
			name := re.Map["name"]
			intf := re.Map["interface"]
			if ips := intfs[intf]; ips != nil {
				dhcps[name] = ips
			} else {
				return nil, fmt.Errorf("dhcp server %q has an unknown, disabled or dynamic interface (%s)", name, intf)
			}
		}
	}

	return dhcps, nil
}

// AddDNS will add the given ip address to the Mikrotik, when duration is 0,
// the entry is seen as permanent and the white and blacklist are not checked
// for duplicates. Conflicts on those lists are checked when the configuration
// is read. It protects against double adding, as that will make the Mikrotik
// spit out an error which in the current implementation leads to a program
// restart. For all timeouts != 0, the index returned over the Mikrotik
// connection is stored, together with the IP itself, in the dynlist entry.
func (mt *Mikrotik) AddDNS(rr dns.RR, comment string) error {
	if *debug || *verbose {
		defer log.Printf("%s: AddDNS(%s) finished", mt.Name, rr)
	}
	// Protect against racing DelIP/AddIPs.
	mt.lock.Lock()
	defer mt.lock.Unlock()

	if *debug || *verbose {
		log.Printf("%s: AddDNS(%s) started", mt.Name, rr)
	}

	// Do the physical interaction with the MT.
	cmd := fmt.Sprintf("=name=%s", mt.fromFQDN(rr.Header().Name))
	if strings.HasPrefix(rr.Header().Name, "*.") {
		cmd = fmt.Sprintf("=regexp=%s", mt.fromFQDN(nameToRegexp(rr.Header().Name)))
	}
	args := []string{
		"/ip/dns/static/add",
		cmd,
		fmt.Sprintf("=ttl=%s", toSeconds(rr.Header().Ttl)),
	}
	switch rr.Header().Rrtype {
	case dns.TypeA:
		// dns entry: "!re @ [{`.id` `*1`} {`name` `router.polyware.nl`} {`type` `A`} {`address` `192.168.10.1`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=A")
		args = append(args, fmt.Sprintf("=address=%s", rr.(*dns.A).A))
	case dns.TypeAAAA:
		// dns entry: "!re @ [{`.id` `*6`} {`name` `rp1.polyware.nl`} {`type` `AAAA`} {`address` `2a02:58:96:ab00:2dda:94ea:a768:a3e5`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=AAAA")
		args = append(args, fmt.Sprintf("=address=%s", rr.(*dns.AAAA).AAAA))
	case dns.TypeCNAME:
		args = append(args, "=type=CNAME")
		args = append(args, fmt.Sprintf("=cname=%s", mt.fromFQDN(rr.(*dns.CNAME).Target)))
	case dns.TypeMX:
		// dns entry: "!re @ [{`.id` `*13`} {`name` `2`} {`type` `MX`} {`mx-preference` `50`} {`mx-exchange` `smtp.polyware.nl`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=MX")
		args = append(args, fmt.Sprintf("=mx-preference=%d", rr.(*dns.MX).Preference))
		args = append(args, fmt.Sprintf("=mx-exchange=%s", mt.fromFQDN(rr.(*dns.MX).Mx)))
	case dns.TypeNS:
		// dns entry: "!re @ [{`.id` `*16`} {`name` `5`} {`type` `NS`} {`ns` `something`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=NS")
		args = append(args, fmt.Sprintf("=ns=%s", mt.fromFQDN(rr.(*dns.NS).Ns)))
	case dns.TypeSRV:
		// dns entry: "!re @ [{`.id` `*14`} {`name` `3`} {`type` `SRV`} {`srv-priority` `1`} {`srv-weight` `2`} {`srv-port` `1883`} {`srv-target` `rp1.polyware.nl`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=SRV")
		args = append(args, fmt.Sprintf("=srv-priority=%d", rr.(*dns.SRV).Priority))
		args = append(args, fmt.Sprintf("=srv-weight=%d", rr.(*dns.SRV).Weight))
		args = append(args, fmt.Sprintf("=srv-port=%d", rr.(*dns.SRV).Port))
		args = append(args, fmt.Sprintf("=srv-target=%s", mt.fromFQDN(rr.(*dns.SRV).Target)))
	case dns.TypeTXT:
		//dns entry: "!re @ [{`.id` `*15`} {`name` `4`} {`type` `TXT`} {`text` `spf thingy`} {`ttl` `1d`} {`dynamic` `false`} {`disabled` `false`}]"
		args = append(args, "=type=TXT")
		args = append(args, fmt.Sprintf("=text=%s", strings.Join(rr.(*dns.TXT).Txt, "\n")))
	default:
		return fmt.Errorf("unknown dns type: %v", rr)
	}
	if comment != "" {
		args = append(args, fmt.Sprintf("=comment=%s", comment))
	}
	if *debug {
		return nil
	}
	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.RunArgs(args)
	cancel()
	if err != nil {
		if strings.Contains(err.Error(), "already have") {
			return nil
		}
		return fmt.Errorf("adddns=%v", err)
	}
	if _, ok := reply.Done.Map["ret"]; !ok {
		return fmt.Errorf("missing `ret`")
	}
	return nil
}

// DelDNS removes an DNS entry from the Mikrotik.
func (mt *Mikrotik) DelDNS(entry string) error {
	// Protect against racing DelIP/AddIPs.
	mt.lock.Lock()
	defer mt.lock.Unlock()
	if *debug {
		return nil
	}

	cancel := mt.startDeadline(5 * time.Second)
	selector := fmt.Sprintf("=.id=%s", entry)
	_, err := mt.client.Run("/ip/dns/static/remove", selector)
	cancel()

	return err
}

// AddDHCP adds a DHCP entry for the given argument.
func (mt *Mikrotik) AddDHCP(d DHCP) error {
	if *debug || *verbose {
		defer log.Printf("%s: AddDHCP(%s) finished", mt.Name, d)
	}
	// Protect against racing DelIP/AddIPs.
	mt.lock.Lock()
	defer mt.lock.Unlock()

	if *debug || *verbose {
		log.Printf("%s: AddDHCP(%s) started", mt.Name, d)
	}
	if *debug {
		return nil
	}

	// Do the physical interaction with the MT.
	args := []string{
		"/ip/dhcp-server/lease/add",
		fmt.Sprintf("=comment=%s", d.Comment),
		fmt.Sprintf("=address=%s", d.IP),
		fmt.Sprintf("=mac-address=%s", d.MAC),
		fmt.Sprintf("=server=%s", d.Server),
	}
	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.RunArgs(args)
	cancel()
	if err != nil {
		//if strings.Contains(err.Error(), "already have") {
		//	return nil
		//}
		return fmt.Errorf("adddhcp=%v", err)
	}
	if _, ok := reply.Done.Map["ret"]; !ok {
		return fmt.Errorf("missing `ret`")
	}
	return nil
}

// DelDHCP removes an DHCP entry from the Mikrotik.
func (mt *Mikrotik) DelDHCP(entry string) error {
	// Protect against racing DelIP/AddIPs.
	mt.lock.Lock()
	defer mt.lock.Unlock()
	if *debug {
		return nil
	}

	cancel := mt.startDeadline(5 * time.Second)
	selector := fmt.Sprintf("=.id=%s", entry)
	_, err := mt.client.Run("/ip/dhcp-server/lease/remove", selector)
	cancel()

	return err
}

// fetchVersion returns the active running firmware version.
func (mt *Mikrotik) fetchVersion() (float64, error) {
	cancel := mt.startDeadline(5 * time.Second)
	reply, err := mt.client.Run("/system/routerboard/print")
	cancel()
	if err != nil {
		return 0, fmt.Errorf("fetchVersion=%v", err)
	}
	for _, re := range reply.Re {
		if v, ok := re.Map["current-firmware"]; ok {
			version, _ := strconv.ParseFloat(v, 64)
			return float64(version), nil
		}
	}
	return 0, fmt.Errorf("missing `current-firmware`")
}

// Close closes the session with the mikrotik.
func (mt *Mikrotik) Close() {
	mt.client.Close()
}


File: /README.md
# mikrotik-dns

[![GoDoc](https://godoc.org/github.com/middelink/mikrotik-dns?status.svg)](https://godoc.org/github.com/middelink/mikrotik-dns)
[![License](https://img.shields.io/github/license/middelink/mikrotik-dns.svg)](https://github.com/middelink/mikrotik-dns/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/middelink/mikrotik-dns.svg?branch=master)](https://travis-ci.org/middelink/mikrotik-dns)
[![Coverage Status](https://coveralls.io/repos/github/middelink/mikrotik-dns/badge.svg?branch=master)](https://coveralls.io/github/middelink/mikrotik-dns?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/middelink/mikrotik-dns)](https://goreportcard.com/report/github.com/middelink/mikrotik-dns)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmiddelink%2Fmikrotik-dns.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmiddelink%2Fmikrotik-dns?ref=badge_shield)

## TL;DR

* mikrotik-dns reads the given nameserver zone file(s) in RFC1034 format and
  updates the internal mikrotik's DNS and/or DHCP server with the discovered
  information.
* It handles all the resources records Mikrotik's DNS supports. (A, AAAA,
  CNAME, MX, NS, SRV and TXT)
* When there is a dhcp:<mac address> is added to A RRs, the tool is capable
  of maintaining the static leases of one or more dhcp servers on the Mikrotik.

> :warning: When used this tool will *remove all DNS and DHCP leases* which are not in the source zone(s)!

## Why did I write this?

Due to a ingrained need to maintain the DNSSEC keys for my domains myself, I
run a so-called blind nameserver (pushing changes via notifications to a set
of publicly known nameservers). However, due to a recent upgrade on the server
the nameserver runs, our house was temporarily deprived of a working DNS.
Unacceptable. That made me think how to sync the given nameserver records to
the Mikrotik, which would allow me in time of need to use that as a emergency
DNS. However while it functioned properly as a forwarding DNS, there were no
entries for my local zone...

While implementing this tool, I figured it would also be nice to have a single
source of truth for the static DHCP leases as well, having the tool a) figure
out to which dhcp server instance the lease would go to and b) populate the DNS
name as a comment.

## Command Line Flags

```
Usage: ./mikrotik-dns [OPTION]... ZONE...

When --use_dns is given, this tool copies compatible RRs from the given zones
into the Mikrotiks static DNS table. This can for example be used in emergency
modes where the local nameserver is down, but the organisation still requires
an internal DNS in the mean time. Unknown entries from the static DNS table
will be removed!

When --use_dhcp is given, all A records from the given zones which have a
comment matching 'dhcp:<mac address>' will update the Mikrotiks DHCP table.
Unknown entries from the DHCP table will be removed!

  -address api://user:pass@host
    	url like address of the MT to connect to api://user:pass@host. use `apis` for encrypted connections.
  -dry_run
    	run the program but do not make any changes on the Mikrotik
  -dnsfilter string
    	comma separated list of dns prefixes to filter
  -use_dhcp
    	maintain dhcp table based upon '; dhcp:<mac>' mac comments on the A records
  -use_dns
    	maintain static dns table from zone
  -verbose
    	be more verbose
  -version
    	output version information and exit
```

## Example usage

Given a example zone file containing:
```dns
example.com	SOA ns.example.com postmaster.example.com 2020092602 28800 7200 2419200 1200
		IN NS		virthost.polyware.nl.
		IN TXT		"v=spf1 a:smtp.example.com ?all"
		IN SPF		"v=spf1 a:smtp.example.com ?all"
		CAA		0 issue "letsencrypt.org"

localhost	IN A		127.0.0.1

@		IN A		192.168.10.10 ; dhcp:01:23:45:67:89:ab
		IN AAAA		2a02:ff:ff:ffff:ffff:ff:ffff:ffff
		IN MX		50 smtp

$GENERATE 128-254 dhcp${-127,3} A 192.168.10.$
```

Running the tool with `mikrotik-dns --use_dns --use_dhcp --dnsfilter="dhcp" --address apis://<user>:<passwd>@<mikrotik> /var/named/<zone>`
will add example.com's NS, TXT, A and AAAA records to the mikrotik's static DNS cache while removing anything else.
Then, if it can find a configured dhcp server for this range, it will add the leases, removing anthing else.

## Installation

I presume you have a working experiance with go.

### Building the binary

* Make sure you have `make`, `git` and `go` installed.
* Clone the source `git clone https://github.com/middelink/mikrotik-dns`.
* Execute `make` to create the mikrotik-fwban binary.
* Copy the binary to /usr/local/bin.

### Mikrotik changes

* Create a group (`apis`) on your mikrotik (system > users; groups) and
  give it at least the `read`, `write` and `api` policies.
* Create a user on your mikrotik (system > users; users) and have it
  belong to the group you just created.


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmiddelink%2Fmikrotik-dns.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmiddelink%2Fmikrotik-dns?ref=badge_large)

