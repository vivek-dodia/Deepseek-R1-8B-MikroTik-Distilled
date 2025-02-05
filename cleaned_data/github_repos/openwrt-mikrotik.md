# Repository Information
Name: openwrt-mikrotik

# Directory Structure
Directory structure:
└── github_repos/openwrt-mikrotik/
    ├── .dockerignore
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
    │   │       ├── pack-bf9229bea40fb711b7508c87876dee8beec2c4b7.idx
    │   │       └── pack-bf9229bea40fb711b7508c87876dee8beec2c4b7.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── build.sh
    ├── configs/
    │   ├── ath79.txt
    │   ├── common.txt
    │   ├── hap-ac2.txt
    │   ├── ipq40xx.txt
    │   └── rtl838x.txt
    ├── docker/
    │   └── entrypoint.sh
    ├── docker-scripts/
    │   ├── config.sh
    │   ├── firmware.sh
    │   └── shell.sh
    ├── Dockerfile
    ├── files/
    │   └── root/
    │       └── .profile
    └── README.md


# Content
File: /.dockerignore
/downloads/
/build/


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/rusitschka/openwrt-mikrotik.git
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
0000000000000000000000000000000000000000 b0a748acdaf656031fd08ccbd97742ddb7f985b7 vivek-dodia <vivek.dodia@icloud.com> 1738606004 -0500	clone: from https://github.com/rusitschka/openwrt-mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 b0a748acdaf656031fd08ccbd97742ddb7f985b7 vivek-dodia <vivek.dodia@icloud.com> 1738606004 -0500	clone: from https://github.com/rusitschka/openwrt-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b0a748acdaf656031fd08ccbd97742ddb7f985b7 vivek-dodia <vivek.dodia@icloud.com> 1738606004 -0500	clone: from https://github.com/rusitschka/openwrt-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b0a748acdaf656031fd08ccbd97742ddb7f985b7 refs/remotes/origin/main


File: /.git\refs\heads\main
b0a748acdaf656031fd08ccbd97742ddb7f985b7


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
/downloads
/build
*.bak
File: /build.sh
#!/bin/bash -ex

DEFAULT_OPENWRT_VERSION="v23.05.5"
#DEFAULT_OPENWRT_VERSION="openwrt-22.03"
#DEFAULT_OPENWRT_VERSION="master"

TARGET="${TARGET:-ipq40xx}"
IMAGE_NAME="openwrt-mikrotik"
OPENWRT_VERSION="${OPENWRT_VERSION:-${DEFAULT_OPENWRT_VERSION}}"
OPENWRT_BUILD_DATE="$(date '+%Y-%m-%d-%H-%M-%S')"

function build_docker
{
    docker rmi $IMAGE_NAME.build -f || true
    docker build \
        --progress plain \
        -t $IMAGE_NAME.build .
    docker rmi $IMAGE_NAME -f || true
    docker tag $IMAGE_NAME.build $IMAGE_NAME
    docker rmi $IMAGE_NAME.build -f || true
}

function run_in_docker
{
    if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]
    then
        build_docker
    fi

    IFS=','
    for TARGET in $TARGET
    do
        echo "Building target $TARGET"
        CONFIG="configs/$TARGET.txt"
        if [ ! -e "$CONFIG" ]
        then
            echo "Invalid target $1: Config $CONFIG not found."
            exit 1
        fi
        TARGET_DIR="build/${OPENWRT_BUILD_DATE}_${OPENWRT_VERSION}"
        mkdir -p downloads
        mkdir -p $TARGET_DIR
        docker volume create $IMAGE_NAME-root-openwrt || true
        docker rm $IMAGE_NAME -f || true
        time docker run -it --rm \
            --name $IMAGE_NAME \
            -e OPENWRT_VERSION=$OPENWRT_VERSION \
            -e OPENWRT_BUILD_DATE=$OPENWRT_BUILD_DATE \
            -v $IMAGE_NAME-root-openwrt:/root/openwrt/ \
            -v $PWD/$TARGET_DIR://root/openwrt/bin/targets/ \
            -v $PWD/configs/common.txt:/root/openwrt/.config-common \
            -v $PWD/$CONFIG:/root/openwrt/.config-template \
            -v $PWD/files:/root/openwrt/files/ \
            -v $PWD/docker-scripts:/root/openwrt/docker-scripts \
            $IMAGE_NAME \
            ./docker-scripts/$1.sh || (mv $TARGET_DIR $TARGET_DIR.failed ; exit 1)
    done
    unset IFS
}

if [ "$1" = "--help" ]
then
    set +x
    echo
    echo "For help see https://github.com/rusitschka/openwrt-mikrotik/blob/main/README.md"
    exit 0
fi

if [ "$1" = "" ]
then
    run_in_docker "firmware"
    exit 0
fi

while [ "$1" != "" ]
do
    case "$1" in
        clean)
            docker rm $IMAGE_NAME || true
            docker rmi $IMAGE_NAME -f || true
            docker volume rm $IMAGE_NAME-root-openwrt -f || true
            ;;
        config)
            run_in_docker "config"
            ;;
        docker)
            build_docker
            ;;
        firmware)
            run_in_docker "firmware"
            ;;
        shell)
            run_in_docker "shell"
            ;;
        *)
            echo "Unsupported command: $1"
            exit 1
            ;;
    esac
    shift
done


File: /configs\ath79.txt
CONFIG_TARGET_ath79=y
CONFIG_TARGET_ath79_mikrotik=y
CONFIG_TARGET_ath79_mikrotik_DEVICE_mikrotik_routerboard-952ui-5ac2nd=y


File: /configs\common.txt
CONFIG_LIBCURL_COOKIES=y
CONFIG_LIBCURL_FILE=y
CONFIG_LIBCURL_FTP=y
CONFIG_LIBCURL_HTTP=y
CONFIG_LIBCURL_MBEDTLS=y
CONFIG_LIBCURL_NGHTTP2=y
CONFIG_LIBCURL_NO_SMB="!"
CONFIG_LIBCURL_PROXY=y
CONFIG_LIBCURL_UNIX_SOCKETS=y
CONFIG_LUCI_SRCDIET=y
CONFIG_PACKAGE_ca-certificates=y
CONFIG_PACKAGE_cgi-io=y
CONFIG_PACKAGE_curl=y
CONFIG_PACKAGE_iperf3=y
CONFIG_PACKAGE_libcurl=y
CONFIG_PACKAGE_libgcrypt=y
CONFIG_PACKAGE_libgpg-error=y
CONFIG_PACKAGE_libiperf3=y
CONFIG_PACKAGE_libiwinfo-lua=y
CONFIG_PACKAGE_liblua=y
CONFIG_PACKAGE_liblucihttp=y
CONFIG_PACKAGE_liblucihttp-lua=y
CONFIG_PACKAGE_liblucihttp-ucode=y
CONFIG_PACKAGE_libncurses=y
CONFIG_PACKAGE_libnghttp2=y
CONFIG_PACKAGE_libpcap=y
CONFIG_PACKAGE_libubus-lua=y
CONFIG_PACKAGE_libuci-lua=y
CONFIG_PACKAGE_lua=y
CONFIG_PACKAGE_lua-cjson=y
CONFIG_PACKAGE_luafilesystem=y
CONFIG_PACKAGE_luci=y
CONFIG_PACKAGE_luci-app-firewall=y
CONFIG_PACKAGE_luci-app-opkg=y
CONFIG_PACKAGE_luci-app-wifischedule=y
CONFIG_PACKAGE_luci-base=y
CONFIG_PACKAGE_luci-compat=y
CONFIG_PACKAGE_luci-lib-base=y
CONFIG_PACKAGE_luci-lib-ip=y
CONFIG_PACKAGE_luci-lib-json=y
CONFIG_PACKAGE_luci-lib-jsonc=y
CONFIG_PACKAGE_luci-lib-nixio=y
CONFIG_PACKAGE_luci-light=y
CONFIG_PACKAGE_luci-lua-runtime=y
CONFIG_PACKAGE_luci-mod-admin-full=y
CONFIG_PACKAGE_luci-mod-network=y
CONFIG_PACKAGE_luci-mod-status=y
CONFIG_PACKAGE_luci-mod-system=y
CONFIG_PACKAGE_luci-proto-ipv6=y
CONFIG_PACKAGE_luci-proto-ppp=y
CONFIG_PACKAGE_luci-theme-bootstrap=y
CONFIG_PACKAGE_nano=y
CONFIG_PACKAGE_rpcd=y
CONFIG_PACKAGE_rpcd-mod-file=y
CONFIG_PACKAGE_rpcd-mod-iwinfo=y
CONFIG_PACKAGE_rpcd-mod-luci=y
CONFIG_PACKAGE_rpcd-mod-rrdns=y
CONFIG_PACKAGE_rpcd-mod-ucode=y
CONFIG_PACKAGE_screen=y
CONFIG_PACKAGE_tcpdump-mini=y
CONFIG_PACKAGE_terminfo=y
CONFIG_PACKAGE_ucode-mod-html=y
CONFIG_PACKAGE_ucode-mod-lua=y
CONFIG_PACKAGE_ucode-mod-math=y
CONFIG_PACKAGE_uhttpd=y
CONFIG_PACKAGE_uhttpd-mod-ubus=y
CONFIG_PACKAGE_wifischedule=y


File: /configs\hap-ac2.txt
CONFIG_TARGET_ipq40xx=y
CONFIG_TARGET_ipq40xx_mikrotik=y
CONFIG_TARGET_MULTI_PROFILE=y
CONFIG_TARGET_DEVICE_ipq40xx_mikrotik_DEVICE_mikrotik_hap-ac2=y
CONFIG_TARGET_DEVICE_PACKAGES_ipq40xx_mikrotik_DEVICE_mikrotik_hap-ac2=""
CONFIG_TARGET_DEVICE_ipq40xx_mikrotik_DEVICE_mikrotik_sxtsq-5-ac=y
CONFIG_TARGET_DEVICE_PACKAGES_ipq40xx_mikrotik_DEVICE_mikrotik_sxtsq-5-ac=""
CONFIG_ALL_KMODS=y
CONFIG_ALL_NONSHARED=y
CONFIG_DEVEL=y
CONFIG_TARGET_PER_DEVICE_ROOTFS=y
CONFIG_AUTOREMOVE=y
CONFIG_BUILDBOT=y
CONFIG_COLLECT_KERNEL_DEBUG=y
CONFIG_IB=y
CONFIG_IMAGEOPT=y
CONFIG_JSON_OVERVIEW_IMAGE_INFO=y
CONFIG_KERNEL_BUILD_DOMAIN="buildhost"
CONFIG_KERNEL_BUILD_USER="builder"
# CONFIG_KERNEL_KALLSYMS is not set
CONFIG_PACKAGE_cgi-io=y
CONFIG_PACKAGE_libiwinfo-lua=y
CONFIG_PACKAGE_liblua=y
CONFIG_PACKAGE_liblucihttp=y
CONFIG_PACKAGE_liblucihttp-lua=y
CONFIG_PACKAGE_libubus-lua=y
CONFIG_PACKAGE_lua=y
CONFIG_PACKAGE_luci=y
CONFIG_PACKAGE_luci-app-firewall=y
CONFIG_PACKAGE_luci-app-opkg=y
CONFIG_PACKAGE_luci-base=y
CONFIG_PACKAGE_luci-lib-base=y
CONFIG_PACKAGE_luci-lib-ip=y
CONFIG_PACKAGE_luci-lib-jsonc=y
CONFIG_PACKAGE_luci-lib-nixio=y
CONFIG_PACKAGE_luci-mod-admin-full=y
CONFIG_PACKAGE_luci-mod-network=y
CONFIG_PACKAGE_luci-mod-status=y
CONFIG_PACKAGE_luci-mod-system=y
CONFIG_PACKAGE_luci-proto-ipv6=y
CONFIG_PACKAGE_luci-proto-ppp=y
CONFIG_PACKAGE_luci-ssl=y
CONFIG_PACKAGE_luci-theme-bootstrap=y
CONFIG_PACKAGE_px5g-wolfssl=y
CONFIG_PACKAGE_rpcd=y
CONFIG_PACKAGE_rpcd-mod-file=y
CONFIG_PACKAGE_rpcd-mod-iwinfo=y
CONFIG_PACKAGE_rpcd-mod-luci=y
CONFIG_PACKAGE_rpcd-mod-rrdns=y
CONFIG_PACKAGE_uhttpd=y
CONFIG_PACKAGE_uhttpd-mod-ubus=y
CONFIG_REPRODUCIBLE_DEBUG_INFO=y
CONFIG_SDK=y
CONFIG_TARGET_ALL_PROFILES=y
CONFIG_VERSIONOPT=y
CONFIG_VERSION_BUG_URL=""
CONFIG_VERSION_CODE=""
CONFIG_VERSION_DIST="OpenWrt"
CONFIG_VERSION_FILENAMES=y
CONFIG_VERSION_HOME_URL=""
CONFIG_VERSION_HWREV=""
CONFIG_VERSION_MANUFACTURER=""
CONFIG_VERSION_MANUFACTURER_URL=""
CONFIG_VERSION_NUMBER=""
CONFIG_VERSION_PRODUCT=""
# CONFIG_VERSION_REPO="https://downloads.openwrt.org/releases/21.02.0"
CONFIG_VERSION_SUPPORT_URL=""
CONFIG_PACKAGE_byobu=y
CONFIG_PACKAGE_htop=y
CONFIG_PACKAGE_iperf3=y
CONFIG_PACKAGE_libbz2=y
CONFIG_PACKAGE_libffi=y
CONFIG_PACKAGE_libnewt=y
CONFIG_PACKAGE_libpython3=y
CONFIG_PACKAGE_librt=y
CONFIG_PACKAGE_libslang2=y
CONFIG_PACKAGE_libuuid=y
CONFIG_PACKAGE_luci-app-wifischedule=y
CONFIG_PACKAGE_luci-compat=y
CONFIG_PACKAGE_luci-theme-openwrt-2020=y
CONFIG_PACKAGE_nano=y
CONFIG_PACKAGE_python3-base=y
CONFIG_PACKAGE_python3-light=y
CONFIG_PACKAGE_python3-newt=y
CONFIG_PACKAGE_tcpdump=y
CONFIG_PACKAGE_terminfo=y
CONFIG_PACKAGE_tmux=y
CONFIG_PACKAGE_wifischedule=y
CONFIG_PACKAGE_zlib=y


File: /configs\ipq40xx.txt
CONFIG_TARGET_ipq40xx=y
CONFIG_TARGET_ipq40xx_mikrotik=y
CONFIG_TARGET_MULTI_PROFILE=y
CONFIG_TARGET_DEVICE_ipq40xx_mikrotik_DEVICE_mikrotik_cap-ac=y
CONFIG_TARGET_DEVICE_ipq40xx_mikrotik_DEVICE_mikrotik_hap-ac2=y


File: /configs\rtl838x.txt
CONFIG_TARGET_realtek=y
CONFIG_TARGET_realtek_rtl838x=y
CONFIG_TARGET_realtek_rtl838x_DEVICE_netgear_gs308t-v1=y


File: /docker\entrypoint.sh
#!/bin/bash -ex

if [ -d .git ]
then
    git reset --hard
    git fetch --all
else
    git config --global init.defaultBranch main
    git config --global user.email "noreply@example.com"
    git config --global user.name "No Name"
    git init .
    git remote add -t \* -f origin https://github.com/openwrt/openwrt.git
fi

[ -e version ] && rm version
git checkout $OPENWRT_VERSION
git reset --hard
echo "$OPENWRT_BUILD_DATE" > version

./scripts/feeds update -a
./scripts/feeds install -a

cat .config-template .config-common > .config
make defconfig

# delete all downloaded files older than 7 days
[ -d dl ] && find dl/ -type f -mtime +7 -delete

exec "$@"


File: /docker-scripts\config.sh
#!/bin/bash -ex

make menuconfig
./scripts/diffconfig.sh


File: /docker-scripts\firmware.sh
#!/bin/bash -ex

# 10 parallel downloads no matter how many actual CPU cores
make -j10 download
if ! make -j$(nproc) world
then
    make V=sc world
fi


File: /docker-scripts\shell.sh
#!/bin/bash -ex

bash

File: /Dockerfile
FROM ubuntu:22.04

WORKDIR /root/openwrt
ENV FORCE_UNSAFE_CONFIGURE=1

RUN set -eux \
  ; apt-get update -yqq \
  ; DEBIAN_FRONTEND=noninteractive apt-get install -yqq --no-install-recommends \
    build-essential \
    ccache \
    ecj \
    fastjar \
    file \
    g++ \
    gawk \
    gettext \
    git \
    java-propose-classpath \
    libelf-dev \
    libncurses-dev \
    libpam-dev \
    libsnmp-dev \
    libssl-dev \
    make \
    python3 \
    python3-dev \
    python3-distutils \
    python3-setuptools \
    rsync \
    subversion \
    swig \
    time \
    unzip \
    wget \
    xsltproc \
    zlib1g-dev \
  ; find /var/cache/ldconfig /var/cache/apt /var/lib/apt/lists /var/log -type f -delete

    # bison \
    # clang \
    # flex \

ADD docker/entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]


File: /files\root\.profile
# screen only for interactive shells,
# see https://unix.stackexchange.com/a/45587
case $- in
  *i*)
    exec screen -xRR
    ;;
esac


File: /README.md
# openwrt-mikrotik

This script builds OpenWRT via Docker images/containers, i.e. Docker is your only build dependency.

Tested versions of OpenWRT:

* 23.05.0

## Configuring

The default target is ipq40xx for Mikrotik hAP ac2 and cAP ac.

You can add new targets by creating files in configs, similar to ipq40xx. A config will get merged
with common.txt which basically contains all the packages you'd like to have in the image.

To create new configs use

```bash
./build.sh docker config
```

which runs OpenWRTs menuconfig. Use the resulting
output to create new config files with the name of your choice.

## Building firmware images

To build OpenWRT execute:

```bash
./build.sh
```

The default target is `ipq40xx`. If you'd like to use a different target run the script like this:

```bash
TARGET=ath79 ./build.sh
```

This will use `configs/ath79.txt` as config.

You can also build multiple targets at the same time:

```bash
TARGET=ipq40xx,ath79,rtl838  ./build.sh
```


To build the master branch of OpenWRT use:

```bash
OPENWRT_VERSION=master ./build.sh
```

To build a tagged 23.05.0 OpenWRT version which supports hAP ac2 and cAP ac use for example:

```bash
OPENWRT_VERSION=v23.05.0 ./build.sh
```

To build a branch, use the branch name, e.g.:

```bash
OPENWRT_VERSION=openwrt-23.05 ./build.sh
```

After the script finishes the resulting target builds are
copied from the Docker container to the `build` folder in the local
file system. The resulting Docker images/containers will be up to
12G each in size and can be deleted after the build finished.

The whole process takes about 45 minutes on a modern CPU.

To clean the build files and force a fresh next build execute:

```bash
./build.sh clean
```

To get shell access to the build environment (useful for debugging):

```bash
./build.sh shell
```


