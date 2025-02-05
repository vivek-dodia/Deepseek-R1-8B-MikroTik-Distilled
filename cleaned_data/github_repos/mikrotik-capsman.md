# Repository Information
Name: mikrotik-capsman

# Directory Structure
Directory structure:
└── github_repos/mikrotik-capsman/
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
    │   │       ├── pack-a9501913c8af29b67182fd03f21ef7fb8c679ab5.idx
    │   │       └── pack-a9501913c8af29b67182fd03f21ef7fb8c679ab5.pack
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
    │       ├── go.yml
    │       └── golangci-lint.yml
    ├── config.yml
    ├── doc/
    ├── go.mod
    ├── html/
    │   └── index.html
    ├── http.go
    ├── lib.go
    ├── main.go
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
	url = https://github.com/vponomarev/mikrotik-capsman.git
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
0000000000000000000000000000000000000000 1bf4e8f1147a7df3b097866a4a9ee495837d3ac7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/vponomarev/mikrotik-capsman.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 1bf4e8f1147a7df3b097866a4a9ee495837d3ac7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/vponomarev/mikrotik-capsman.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 1bf4e8f1147a7df3b097866a4a9ee495837d3ac7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/vponomarev/mikrotik-capsman.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
1bf4e8f1147a7df3b097866a4a9ee495837d3ac7 refs/remotes/origin/master
bcaadb7fae10051ae7b4b51dd76cfc78d13f120c refs/tags/1.2
1bf4e8f1147a7df3b097866a4a9ee495837d3ac7 refs/tags/1.3
df81b58eec687d17f8382d7e2cf3e2238466435d refs/tags/v1.0
86cf0c28c7a59347b1e12dcac6bbe76cd95d7c45 refs/tags/v1.1


File: /.git\refs\heads\master
1bf4e8f1147a7df3b097866a4a9ee495837d3ac7


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\workflows\go.yml
name: go-build

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:

  build:
    name: Build
    runs-on: ubuntu-latest
    steps:

    - name: Set up Go 1.x
      uses: actions/setup-go@v2
      with:
        go-version: ^1.13
      id: go

    - name: Check out code into the Go module directory
      uses: actions/checkout@v2

    - name: Get dependencies
      run: |
        go get -v -t -d ./...
        if [ -f Gopkg.toml ]; then
            curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
            dep ensure
        fi

    - name: Build
      run: |
        mkdir out_x86-64
        cp config.yml out_x86-64/
        cp -r html out_x86-64/
        go build -o out_x86-64/mikrotik-capsman -v .
        mkdir out_arm32
        cp config.yml out_arm32/
        cp -r html out_arm32/
        GOARCH=arm go build -o out_arm32/mikrotik-capsman -v .
        mkdir out_win
        cp config.yml out_win/
        cp -r html out_win/
        GOARCH=386 GOOS=windows go build -o out_win/mikrotik-capsman32.exe -v .
        GOARCH=amd64 GOOS=windows go build -o out_win/mikrotik-capsman64.exe -v .

    - name: Upload Linux binary x86-64
      uses: actions/upload-artifact@master
      with:
        name: mikrotik-capsman_linux_x86-64
        path: out_x86-64

    - name: Upload Linux binary arm32
      uses: actions/upload-artifact@master
      with:
        name: mikrotik-capsman_linux_arm32
        path: out_arm32

    - name: Upload Windows binary
      uses: actions/upload-artifact@master
      with:
        name: mikrotik-capsman_windows
        path: out_win


File: /.github\workflows\golangci-lint.yml
name: golangci-lint
on:
  push:
    tags:
      - v*
    branches:
      - master
  pull_request:
jobs:
  golangci:
    name: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: golangci-lint
        uses: golangci/golangci-lint-action@v1
        with:
          # Required: the version of golangci-lint is required and must be specified without patch version: we always use the latest patch version.
          version: v1.29

          # Optional: working directory, useful for monorepos
          # working-directory: somedir

          # Optional: golangci-lint command line arguments.
          # args: --issues-exit-code=0

          # Optional: show only new issues if it's a pull request. The default value is `false`.
          # only-new-issues: true


File: /config.yml
# Logging configuration
log:
  level: INFO

# Mikrotik CapsMan connection parameters
router:
  # mode: "wifi"
  mode: "capsman"
  address: "192.168.1.1:8728"
  username: "admin"
  password: ""
  interval: 3s

# Mikrotik DHCP server connection parameters
dhcp:
  address: "192.168.1.1:8728"
  username: "admin"
  password: ""
  interval: 1m


# Configuration file for MAC => DeviceName Name mapping
devices:
  - name: "Device 01"
    mac: "5C:C0:70:A1:00:00"
  - name: "Device 02"
    mac: "5C:C0:70:A2:00:00"
  - name: "Device 03"
    mac: "5C:C0:70:A3:00:00"
    on.connect:
      http.post: "http://127.0.0.1:8006/device/{mac}/{name}/state"
      http.post.content: "{ \"state\": \"connect\" }"
      http.header:
        "Authorization": "Bearer HereIsPassword"
        "Content-Type": "application/json"
    on.disconnect:
      http.post: "http://127.0.0.1:8006/device/{mac}/{name}/state"
      http.post.content: "{ \"state\": \"disconnect\" }"
      http.header:
        "Authorization": "Bearer HereIsPassword"
        "Content-Type": "application/json"
    on.roaming:
      http.post: "http://127.0.0.1:8006/device/{mac}/{name}/AP"
      http.post.content: "{ \"AP\": \"{roaming.to}\", \"AP_OLD\": \"{roaming.from}\" }"
      http.header:
        "Authorization": "Bearer HereIsPassword"
        "Content-Type": "application/json"
    on.level:
      http.post: "http://127.0.0.1:8006/device/{mac}/{name}/level"
      http.post.content: "{ \"level\": \"{level.to}\" }"
      http.header:
        "Authorization": "Bearer HereIsPassword"
        "Content-Type": "application/json"



File: /go.mod
module github.com/vponomarev/libsmpp

go 1.13

require (
	github.com/gorilla/websocket v1.4.2 // indirect
	github.com/sirupsen/logrus v1.6.0 // indirect
	gopkg.in/routeros.v2 v2.0.0-20190905230420-1bbf141cdd91 // indirect
	gopkg.in/yaml.v2 v2.3.0 // indirect
)


File: /html\index.html
<html>
<head>
    <title>CapsMAN Connection overview</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<table class="table table-sm table-bordered table-striped">
    <thead class="thead-light">
    <tr>
        <td>Interface</td>
        <td>SSID</td>
        <td>MAC</td>
        <td>IP</td>
        <td>Name</td>
        <td>Signal</td>
        <td>Hostname</td>
        <td>Comment</td>
        <td>&nbsp;</td>
    </tr>
    </thead>
    <tbody id="bodyData">

    </tbody>
</table>

<pre id="output"></pre>

<script type="application/javascript">
function doConnectWS() {
    let socket = new WebSocket("ws://{{.ServerHost}}/ws");
    let output = document.getElementById("output");
    output.innerHTML = "Status: Connecting...\n";

    socket.onopen = function () {
        output.innerHTML = "Status: Connected\n" + output.innerHTML;
    }
    socket.onmessage = function (e) {
        msg = JSON.parse(e.data)
        //console.log(msg)
        output.innerHTML = "Server: " + e.data + "\n" + output.innerHTML;

        // Truncate number of rows to 10 MAX
        let vr = output.innerHTML.split("\n");
        if (vr.length > 5) {
            vr.length = 5;
            output.innerHTML = vr.join("\n");
        }

        let idx;
        let lst = new Map();
        for (idx = 0; idx < msg.length; idx++) {
            let rec = msg[idx]
            rec["DONE"] = 0

            lst.set(rec["MAC"], rec)
        }
        console.log(lst);

        $("#bodyData tr").each(function () {
            let mac = $(this).find("td:eq(2)").text()
            if (lst.has(mac)) {
                let v = lst.get(mac)

                if ($(this).find("td:eq(5)").text() != v["Signal"]) {
                    $(this).find("td:eq(5)").text(v["Signal"]).css("background-color", "yellow")
                } else {
                    $(this).find("td:eq(5)").css("background-color", "white")
                }
                if ($(this).find("td:eq(0)").text() != v["Interface"]) {
                    $(this).find("td:eq(0)").text(v["Interface"]).css("background-color", "yellow")
                } else {
                    $(this).find("td:eq(0)").css("background-color", "white")
                }
                if ($(this).attr("setDelete") !== undefined) {
                    $(this).removeAttr("setDelete");
                    $(this).find("td:eq(0)").css("background-color", "white")
                }

                v["DONE"] = 1
            } else {
                // MAC DISAPPEARED, Mark to delete ROW
                if ($(this).attr("setDelete") !== undefined) {
                    if ($(this).attr("setDelete") > 0) {
                        $(this).attr("setDelete", $(this).attr("setDelete") - 1);
                    } else {
                        $(this).attr("doDelete", 1)
                    }
                } else {
                    $(this).attr("setDelete", 10)
                    $(this).find("td:eq(0)").css("background-color", "grey")
                }
            }
        });
        for (let e of lst.keys()) {
            let v = lst.get(e)
            if (v.DONE < 1) {
                console.log(v);
                $("#bodyData").append("<tr><td>" + v["Interface"] + "</td><td>" + v["SSID"] + "</td><td>" + v["MAC"] + "</td><td>" + v["IP"] + "</td><td>" + v["Name"] + "</td><td>" + v["Signal"] + "</td><td>" + v["Hostname"] + "</td><td>" + v["Comment"] + "</td></tr>");
            }
        }

        // Delete expired lines
        $("#bodyData [doDelete=1]").remove();
    };
    socket.onclose = function () {
        output.innerHTML += "Status: DISCONNECTED\n";

        // Reconnect in 5 sec
        setTimeout(doConnectWS, 5000);
    }
}

doConnectWS();
</script>


</body>

</html>

File: /http.go
package main

import (
	"fmt"
	"github.com/gorilla/websocket"
	log "github.com/sirupsen/logrus"
	"html/template"
	"io/ioutil"
	"net/http"
	"strings"
	"time"
)

func serveHTTP() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fn := "html/index.html"
		t, err := template.ParseFiles(fn)
		if err != nil {
			fmt.Fprint(w, "Error parsing template file:", fn, " with error:", err)
			return
		}
		if t.Execute(w, map[string]string{"ServerHost": r.Host}) != nil {
			fmt.Fprint(w, "Internal error: cannot execute template")
		}
	})

	http.HandleFunc("/ws", func(w http.ResponseWriter, r *http.Request) {
		conn, err := WS.Upgrade(w, r, nil)
		if err != nil {
			if _, ok := err.(websocket.HandshakeError); !ok {
				log.Println(err)
			}
			return
		}

		go WSwriter(conn)
		WSreader(conn)

	})

	log.WithFields(log.Fields{"listen": *listen}).Warn("Starting HTTP Listener")
	err := http.ListenAndServe(*listen, nil)
	log.WithFields(log.Fields{"listen": *listen}).Fatal("Received an error from HTTP Listener: ", err)
}

func WSwriter(ws *websocket.Conn) {
	pingTicker := time.NewTicker(pingPeriod)
	dataTicker := time.NewTicker(100 * time.Millisecond)

	var lastUpdate time.Time

	defer func() {
		pingTicker.Stop()
		dataTicker.Stop()
		ws.Close()
	}()

	for {
		select {
		case <-pingTicker.C:
			if ws.SetWriteDeadline(time.Now().Add(writeWait)) != nil {
				return
			}
			if err := ws.WriteMessage(websocket.PingMessage, []byte{}); err != nil {
				return
			}
		case <-dataTicker.C:
			// Check for LastUpdate
			broadcastData.RLock()
			if broadcastData.LastUpdate.After(lastUpdate) {
				data := broadcastData.Data
				lastUpdate = broadcastData.LastUpdate
				broadcastData.RUnlock()

				if ws.SetWriteDeadline(time.Now().Add(writeWait)) != nil {
					return
				}
				if err := ws.WriteMessage(websocket.TextMessage, []byte(data)); err != nil {
					return
				}
			} else {
				broadcastData.RUnlock()
			}
		}
	}
}

func WSreader(ws *websocket.Conn) {
	defer ws.Close()
	ws.SetReadLimit(512)

	if ws.SetReadDeadline(time.Now().Add(pongWait)) != nil {
		return
	}
	ws.SetPongHandler(func(string) error {
		return ws.SetReadDeadline(time.Now().Add(pongWait))
	})
	for {
		_, _, err := ws.ReadMessage()
		if err != nil {
			break
		}
	}
}

func makeRequest(event ConfigEvent, params map[string]string) {

	// Prepare request params
	method := "GET"
	data := ""
	url := event.HttpGet
	if len(event.HttpPost) > 0 {
		method = "POST"
		url = event.HttpPost
		data = event.HttpPostContent
	}

	for k, v := range params {
		url = strings.ReplaceAll(url, "{"+k+"}", v)
		data = strings.ReplaceAll(data, "{"+k+"}", v)
	}

	// Prepare request
	client := &http.Client{}
	req, err := http.NewRequest(method, url, strings.NewReader(data))
	if err != nil {
		log.WithFields(log.Fields{"action": "notify", "url": url}).Info("Error creating HTTP request: ", err)
		return
	}

	// Add headers
	for k, v := range event.HttpHeader {
		req.Header.Add(k, v)
	}
	resp, err := client.Do(req)
	if err != nil {
		log.WithFields(log.Fields{"action": "notify", "method": method, "url": url, "state": "fail"}).Info("Error making HTTP request: ", err)
		return
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.WithFields(log.Fields{"action": "notify", "method": method, "url": url, "state": "fail"}).Info("Error reading body of HTTP request: ", err)
		return
	}
	log.WithFields(log.Fields{"action": "notify", "method": method, "url": url, "state": "ok", "resp-body-len": len(body)}).Debug("HTTP Notification is sent")
}


File: /lib.go
package main

import (
	"encoding/json"
	"fmt"
	"github.com/gorilla/websocket"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2"
	"gopkg.in/yaml.v2"
	"io/ioutil"
	"strings"
	"sync"
	"time"
)

const (
	// Time allowed to read the next pong message from the client.
	pongWait = 60 * time.Second

	// Send pings to client with this period. Must be less than pongWait.
	pingPeriod = (pongWait * 9) / 10

	// Time allowed to write the file to the client.
	writeWait = 10 * time.Second
)

// Event types
const (
	EVENT_CONNECT = iota
	EVENT_ROAMING
	EVENT_DISCONNECT
	EVENT_LEVEL
)

type LeaseEntry struct {
	IP       string
	MAC      string
	Server   string
	Hostname string
	Comment  string
}

type ReportEntry struct {
	IP        string
	Name      string
	Interface string
	SSID      string
	MAC       string
	Signal    string
	Hostname  string
	Comment   string
}

type ReportEvent struct {
	EventType int
	Old       ReportEntry
	New       ReportEntry
}

var WS = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

type BroadcastData struct {
	Report     []ReportEntry
	ReportMap  map[string]ReportEntry
	Data       string
	LastUpdate time.Time
	sync.RWMutex

	ReportChan chan ReportEvent
}

type LeaseList struct {
	List []LeaseEntry
	sync.RWMutex
}

type ConfMikrotik struct {
	Address  string        `yaml:"address"`
	Username string        `yaml:"username"`
	Password string        `yaml:"password"`
	Interval time.Duration `yaml:"interval"`
	Mode     string        `yaml:"mode"`
}

type ConfDevice struct {
	Name         string      `yaml:"name"`
	MAC          string      `yaml:"mac"`
	OnConnect    ConfigEvent `yaml:"on.connect"`
	OnDisconnect ConfigEvent `yaml:"on.disconnect"`
	OnRoaming    ConfigEvent `yaml:"on.roaming"`
	OnLevel      ConfigEvent `yaml:"on.level"`
}

type ConfigEvent struct {
	HttpPost        string            `yaml:"http.post"`
	HttpGet         string            `yaml:"http.get"`
	HttpPostContent string            `yaml:"http.post.content"`
	HttpHeader      map[string]string `yaml:"http.header"`
}

type LogInfo struct {
	Level log.Level `yaml:"level"`
}

type Config struct {
	Log     LogInfo      `yaml:"log"`
	Router  ConfMikrotik `yaml:"router"`
	DHCP    ConfMikrotik `yaml:"dhcp"`
	Devices []ConfDevice `yaml:"devices"`
}

// Init BroadcastData entry
func (b *BroadcastData) Init() {
	b.ReportMap = map[string]ReportEntry{}
	b.ReportChan = make(chan ReportEvent)
}

var broadcastData BroadcastData
var leaseList LeaseList

var config Config
var configMTX sync.RWMutex

var devList map[string]ConfDevice
var devListMTX sync.RWMutex

func GetDHCPLeases(address, username, password string) (list []LeaseEntry, err error) {
	cl, err := routeros.Dial(address, username, password)
	if err != nil {
		return
	}
	defer cl.Close()

	reply, err := cl.Run("/ip/dhcp-server/lease/print")
	if err != nil {
		return
	}

	for _, re := range reply.Re {
		list = append(list, LeaseEntry{
			IP:       re.Map["address"],
			MAC:      re.Map["mac-address"],
			Server:   re.Map["server"],
			Hostname: re.Map["host-name"],
			Comment:  re.Map["comment"],
		})
	}
	return
}

func reloadDHCP() {
	ticker := time.NewTicker(config.DHCP.Interval)
	for { // nolint:gosimple
		select {
		case <-ticker.C:
			l, err := GetDHCPLeases(config.DHCP.Address, config.DHCP.Username, config.DHCP.Password)
			if err != nil {
				log.WithFields(log.Fields{"dhcp-addr": config.DHCP.Address}).Error("Error reloading DHCP Leases: ", err)
				return
			} else {
				leaseList.RLock()
				leaseList.List = l
				leaseList.RUnlock()
				log.WithFields(log.Fields{"count": len(l)}).Debug("Reloaded DHCP Leases")
			}

		}
	}
}

func FindLeaseByMAC(list []LeaseEntry, mac string) (e LeaseEntry, ok bool) {
	for _, e := range list {
		if e.MAC == mac {
			return e, true
		}
	}
	return
}

func RTLoop(c *routeros.Client, conf *Config) {
	for {
		cmd := "/caps-man/registration-table/print"
		if strings.ToLower(config.Router.Mode) == "wifi" {
			cmd = "/interface/wireless/registration-table/print"
		}

		reply, err := c.Run(cmd)
		if err != nil {
			log.WithFields(log.Fields{"address": config.Router.Address, "username": config.Router.Username}).Error("Error during request to CapsMan server: ", err)

			// Try to close connection
			c.Close()

			// Reconnect loop
			for {
				// Sleep for 5 sec
				time.Sleep(5 * time.Second)
				cNew, err := routeros.Dial(config.Router.Address, config.Router.Username, config.Router.Password)
				if err != nil {
					log.WithFields(log.Fields{"address": config.Router.Address, "username": config.Router.Username}).Error("Reconnect error to CapsMan server: ", err)
					continue
				}
				c = cNew
				log.WithFields(log.Fields{"address": config.Router.Address, "username": config.Router.Username}).Warn("Reconnected to CapsMan server")
				break
			}
			continue
		}

		var report []ReportEntry

		leaseList.RLock()
		for _, re := range reply.Re {
			var n, c, ip string
			if le, ok := FindLeaseByMAC(leaseList.List, re.Map["mac-address"]); ok {
				n = le.Hostname
				c = le.Comment
				ip = le.IP
			}
			devListMTX.RLock()
			rec := ReportEntry{
				IP:        ip,
				Name:      devList[re.Map["mac-address"]].Name,
				Interface: re.Map["interface"],
				SSID:      re.Map["ssid"],
				MAC:       re.Map["mac-address"],
				Signal:    re.Map["rx-signal"],
				Hostname:  n,
				Comment:   c,
			}

			if strings.ToLower(config.Router.Mode) == "wifi" {
				rec.Signal = re.Map["signal-strength"]
				if i := strings.Index(rec.Signal, "@"); i > 0 {
					rec.Signal = rec.Signal[0:i]
				}
			}
			devListMTX.RUnlock()
			report = append(report, rec)

			// fmt.Printf("%-20s\t%-20s\t%-20s\t%-10s\t%-30s\t%-30s\n", re.Map["interface"], re.Map["ssid"], re.Map["mac-address"], re.Map["rx-signal"], n, c)
		}
		log.WithFields(log.Fields{"count": len(report)}).Debug("Reloaded CapsMan entries")
		leaseList.RUnlock()

		if err = broadcastData.reportUpdate(report); err != nil {
			log.WithFields(log.Fields{}).Warn("Error during reportUpdate: ", err)

		}

		time.Sleep(*interval)
	}
}

func loadConfig(configFileName string) (config Config, err error) {
	devListMTX.RLock()
	defer devListMTX.RUnlock()

	config = Config{}
	devList = make(map[string]ConfDevice)

	source, err := ioutil.ReadFile(configFileName)
	if err != nil {
		err = fmt.Errorf("cannot read config file [%s]", configFileName)
		return
	}

	if err = yaml.Unmarshal(source, &config); err != nil {
		err = fmt.Errorf("error parsing config file [%s]: %v", configFileName, err)
		return
	}

	for _, v := range config.Devices {
		devList[strings.ToUpper(v.MAC)] = v
	}

	return
}

func usage() {

}

// Handle report update request
func (b *BroadcastData) reportUpdate(report []ReportEntry) error {
	output, err := json.Marshal(report)
	if err != nil {
		return err
	}

	// Lock mutex
	b.RLock()
	defer b.RUnlock()

	// Prepare new list of entries
	rm := map[string]ReportEntry{}
	for _, v := range report {
		rm[v.MAC] = v
	}

	// Scan for new entries
	for k := range rm {
		if _, ok := b.ReportMap[k]; !ok {
			// New entry
			b.ReportChan <- ReportEvent{
				EventType: EVENT_CONNECT,
				New:       rm[k],
			}
		} else {
			// Check for roaming
			if rm[k].Interface != b.ReportMap[k].Interface {
				b.ReportChan <- ReportEvent{
					EventType: EVENT_ROAMING,
					Old:       b.ReportMap[k],
					New:       rm[k],
				}
			}

			// Check for signal level change
			if rm[k].Signal != b.ReportMap[k].Signal {
				b.ReportChan <- ReportEvent{
					EventType: EVENT_LEVEL,
					Old:       b.ReportMap[k],
					New:       rm[k],
				}
			}
		}
	}

	// Scan for deleted entries
	for k := range b.ReportMap {
		if _, ok := rm[k]; !ok {
			b.ReportChan <- ReportEvent{
				EventType: EVENT_DISCONNECT,
				Old:       b.ReportMap[k],
			}
		}
	}

	b.ReportMap = rm
	b.Report = report
	b.Data = string(output)
	b.LastUpdate = time.Now()

	return nil
}

func (b *BroadcastData) EventHandler() {
	for { // nolint:gosimple
		select {
		case data := <-b.ReportChan:
			// fmt.Printf("New event received: %v\n", data)
			switch data.EventType {
			case EVENT_CONNECT:
				log.WithFields(log.Fields{"action": "register", "mac": data.New.MAC, "name": data.New.Name, "interface": data.New.Interface, "ssid": data.New.SSID, "hostname": data.New.Hostname, "comment": data.New.Comment, "level-to": data.New.Signal}).Info("New connection registered")

				// Get device info
				devListMTX.RLock()
				dev, ok := devList[data.New.MAC]
				devListMTX.RUnlock()
				if ok {
					if (len(dev.OnConnect.HttpPost) > 0) || (len(dev.OnConnect.HttpGet) > 0) {
						go makeRequest(dev.OnConnect, map[string]string{
							"name":         dev.Name,
							"mac":          data.New.MAC,
							"roaming.to":   "",
							"roaming.from": "",
							"level.to":     data.New.Signal,
							"level.from":   "",
						})
					}
				}

			case EVENT_DISCONNECT:
				log.WithFields(log.Fields{"action": "disconnect", "mac": data.Old.MAC, "name": data.Old.Name, "interface": data.Old.Interface, "hostname": data.Old.Hostname, "comment": data.Old.Comment}).Info("Client disconnect")

				// Get device info
				devListMTX.RLock()
				dev, ok := devList[data.New.MAC]
				devListMTX.RUnlock()
				if ok {
					if (len(dev.OnDisconnect.HttpPost) > 0) || (len(dev.OnDisconnect.HttpGet) > 0) {
						go makeRequest(dev.OnDisconnect, map[string]string{
							"name":         dev.Name,
							"mac":          data.Old.MAC,
							"roaming.to":   "",
							"roaming.from": "",
							"level.to":     "",
							"level.from":   data.Old.Signal,
						})
					}
				}

			case EVENT_ROAMING:
				log.WithFields(log.Fields{"action": "roaming", "mac": data.New.MAC, "name": data.New.Name, "interface-from": data.Old.Interface, "interface-to": data.New.Interface, "level-from": data.Old.Signal, "level-to": data.New.Signal}).Info("Client roaming")

				// Get device info
				devListMTX.RLock()
				dev, ok := devList[data.New.MAC]
				devListMTX.RUnlock()
				if ok {
					if (len(dev.OnRoaming.HttpPost) > 0) || (len(dev.OnRoaming.HttpGet) > 0) {
						go makeRequest(dev.OnRoaming, map[string]string{
							"name":         dev.Name,
							"mac":          data.New.MAC,
							"roaming.to":   data.New.Interface,
							"roaming.from": data.Old.Interface,
							"level.from":   data.Old.Signal,
							"level.to":     data.New.Signal,
						})
					}
				}

			case EVENT_LEVEL:
				log.WithFields(log.Fields{"action": "level", "mac": data.New.MAC, "name": data.New.Name, "interface": data.New.Interface, "level-from": data.Old.Signal, "level-to": data.New.Signal}).Debug("Signal level change")

				// Get device info
				devListMTX.RLock()
				dev, ok := devList[data.New.MAC]
				devListMTX.RUnlock()
				if ok {
					if (len(dev.OnLevel.HttpPost) > 0) || (len(dev.OnLevel.HttpGet) > 0) {
						go makeRequest(dev.OnLevel, map[string]string{
							"name":         dev.Name,
							"mac":          data.Old.MAC,
							"roaming.to":   "",
							"roaming.from": "",
							"level.from":   data.Old.Signal,
							"level.to":     data.New.Signal,
						})
					}
				}

			default:

			}
		}
	}
}


File: /main.go
package main

import (
	"flag"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2"
	"os"
	"time"
)

var (
	// HTTP Listen port
	listen = flag.String("listen", "0.0.0.0:8080", "HTTP Listen configuration")

	// Polling interval
	interval = flag.Duration("interval", 3*time.Second, "CapsMan Polling Interval")

	// Optional configuration file
	configFileName = flag.String("config", "config.yml", "Configuration file name")
)

func main() {
	// Check for `--help` param
	if len(os.Args) > 1 {
		if os.Args[1] == "--help" {
			usage()
			return
		}
	}

	// Init broadcast data
	broadcastData.Init()
	go broadcastData.EventHandler()

	flag.Parse()

	log.SetLevel(log.DebugLevel)
	log.Warning("Starting Mikrotik CapsMan monitor daemon")

	// Load config if specified
	cfg, err := loadConfig(*configFileName)
	if err != nil {
		log.WithFields(log.Fields{"config": *configFileName}).Fatal("Error loading config file")
		return
	}

	// Switch log level if required
	if cfg.Log.Level != log.DebugLevel {
		log.WithFields(log.Fields{"loglevel": cfg.Log.Level}).Warn("Switching Log Level")
		log.SetLevel(cfg.Log.Level)
	}

	// Validate reload interval duration
	if cfg.Router.Interval < (2 * time.Second) {
		log.WithFields(log.Fields{"config": *configFileName}).Fatal("capsman.interval is too short, minimum value is 2 sec")
	}

	if (len(cfg.DHCP.Address) > 0) && cfg.DHCP.Interval < (10*time.Second) {
		log.WithFields(log.Fields{"config": *configFileName}).Fatal("dhcp.interval is too short, minimum value is 10 sec")
	}

	log.WithFields(log.Fields{"config": *configFileName}).Warn("Loaded config file")
	configMTX.RLock()
	config = cfg
	configMTX.RUnlock()

	if len(cfg.DHCP.Address) > 0 {
		l, err := GetDHCPLeases(config.DHCP.Address, config.DHCP.Username, config.DHCP.Password)
		if err != nil {
			log.WithFields(log.Fields{"dhcp-addr": config.DHCP.Address, "dhcp-username": config.DHCP.Username}).Fatal("Cannot connect to DHCP Server")
		}

		leaseList.RLock()
		leaseList.List = l
		leaseList.RUnlock()
		log.WithFields(log.Fields{"dhcp-addr": config.DHCP.Address, "count": len(l)}).Info("Loaded DHCP Lease list")

	} else {
		log.WithFields(log.Fields{"dhcp-addr": config.DHCP.Address}).Warn("DHCP support is disabled in configuration")
	}

	conn, err := routeros.Dial(config.Router.Address, config.Router.Username, config.Router.Password)
	if err != nil {
		log.WithFields(log.Fields{"address": config.Router.Address, "username": config.Router.Username}).Fatal("Cannot connect to CapsMan node")
		return
	}
	log.WithFields(log.Fields{"address": config.Router.Address}).Info("Connected to CapsMan server")

	// Run HTTP Server
	go serveHTTP()

	// Start DHCP periodical reload
	if len(cfg.DHCP.Address) > 0 {
		go reloadDHCP()
	}

	// Run loop : scan Registration-Table
	RTLoop(conn, &config)
}


File: /README.md
# Mikrotik-CapsMan
* Web UI for Mikrotik CapsMan/WiFi interface
* HTTP Notification engine for CapsMan/WiFi client changes 

![UI Example](https://github.com/vponomarev/mikrotik-capsman/raw/master/doc/mikrotik-capsman-ui-sample-processed.PNG)

UI generates a dedicated and periodically updated WEB page with list of WiFi clients, that are connected to CapsMan. List is filled with extra information from Mikrotik DHCP Server.

UI contains:
- CapsMan interface name
- SSID
- Client MAC address
- Client IP address (from DHCP)
- Signal strength level
- Hostname (from DHCP)
- Comment (from DHCP)

Supported configuration params:
- `-config` - Name of configuration file (default: `config.yml`, example: `-config config-custom.yml`)

Supported parameters in configuration file:
- Router configuration
  - `mode` - operation mode (CapsMan / WiFi)
  - `address` - IP address and port of API interface (normally `8728`)
  - `username` - Login for API connection
  - `password` - Password for API connection
  - `interval` - Polling interval (examples: `5s`, `1m`, ...)
- DHCP Server configuration (only Mikrotik DHCP server is supported), optional
  - `address` - IP address and port of API interface (normally `8728`)
  - `username` - Login for API connection
  - `password` - Password for API connection
  - `interval` - Polling interval (examples: `5s`, `1m`, ...)
- Device list (personal configuration for each device)
  - `name` - Name, that will be displayed in interface
  - `mac` - MAC address of this device
  - `on.connect` - Action for connect event
  - `on.disconnect` - Action for disconnect event
  - `on.roaming` - Action for roaming between AP's (for CapsMan mode)
  - `on.level` - Action for signal level change

Each `on.*` event have the following configuration fields:
- `http.post` - URL for HTTP Post request with template support
- `http.get` - URL for HTTP Get request with templates (will be used if there is no `http.post` line)
- `http.post.content` - Content for HTTP Post request
- `http.header` - List of HTTP headers, that should be added into request (can be used for authentification/configuration of content-type and so on)

Supported template variables for `http.post`, `http.get` and `http.post.content` fields:
- `name` - Name of device (from configuration)
- `mac` - MAC address of device
- `roaming.to` - During roaming, name of New AP
- `roaming.from` - During roaming, name of OLD AP
- `level.to` - During level change, value of new signal level
- `level.from` - During level change, value of old signal level
  

WEB UI is published at: http://`listen`/

# Future plans
- Add configuration file with support of human-readable names for specific MAC addresses
- Add MQTT Support with publishing of WiFi client state for intergration with HomeAssistant or other smart house servers

Have any ideas?
Feel free to send change requests.

