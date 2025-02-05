# Repository Information
Name: mikrotik-exporter

# Directory Structure
Directory structure:
└── github_repos/mikrotik-exporter/
    ├── .circleci/
    │   └── config.yml
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
    │   │       │   └── trunk
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-b3de2ad31d85732b240881df0b7385e44373a279.idx
    │   │       └── pack-b3de2ad31d85732b240881df0b7385e44373a279.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── trunk
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── collector/
    │   ├── bgp_collector.go
    │   ├── capsman_collector.go
    │   ├── collector.go
    │   ├── collector_context.go
    │   ├── conntrack_collector.go
    │   ├── dhcpv6_collector.go
    │   ├── dhcp_collector.go
    │   ├── dhcp_lease_collector.go
    │   ├── firmware_collector.go
    │   ├── health_collector.go
    │   ├── helper.go
    │   ├── helper_test.go
    │   ├── interface_collector.go
    │   ├── ipsec_collector.go
    │   ├── lte_collector.go
    │   ├── monitor_collector.go
    │   ├── netwatch_collector.go
    │   ├── optics_collector.go
    │   ├── poe_collector.go
    │   ├── pool_collector.go
    │   ├── resource_collector.go
    │   ├── resource_collector_test.go
    │   ├── routeros_collector.go
    │   ├── routes_collector.go
    │   ├── w60g_collector.go
    │   ├── wlanif_collector.go
    │   └── wlansta_collector.go
    ├── config/
    │   ├── config.go
    │   ├── config.test.yml
    │   └── config_test.go
    ├── Dockerfile
    ├── Dockerfile.arm64
    ├── Dockerfile.armhf
    ├── examples/
    │   ├── docker-compose/
    │   │   ├── .env
    │   │   └── docker-compose.yml
    │   └── kubernetes/
    │       └── single-device/
    │           ├── configmap.json
    │           ├── deployment.json
    │           └── secret.json
    ├── go.mod
    ├── go.sum
    ├── LICENSE
    ├── main.go
    ├── MAINTAINERS.md
    ├── Makefile
    ├── README.md
    ├── scripts/
    │   ├── build-armhf.sh
    │   ├── build.sh
    │   └── start.sh
    └── VERSION


# Content
File: /.circleci\config.yml
version: 2
jobs:
  build:
    docker:
      - image: circleci/golang:1.13.4-stretch
    branches:
      only:
        - master
        - /^nshttpd.*/
    steps:
      - checkout
      - setup_remote_docker:
          version: 18.06.0-ce
      - run: make dockerhub


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/nshttpd/mikrotik-exporter.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "trunk"]
	remote = origin
	merge = refs/heads/trunk


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/trunk


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
0000000000000000000000000000000000000000 e1b06c6ebe6e71a5661326b3a33afe2fd741283d vivek-dodia <vivek.dodia@icloud.com> 1738605780 -0500	clone: from https://github.com/nshttpd/mikrotik-exporter.git


File: /.git\logs\refs\heads\trunk
0000000000000000000000000000000000000000 e1b06c6ebe6e71a5661326b3a33afe2fd741283d vivek-dodia <vivek.dodia@icloud.com> 1738605780 -0500	clone: from https://github.com/nshttpd/mikrotik-exporter.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e1b06c6ebe6e71a5661326b3a33afe2fd741283d vivek-dodia <vivek.dodia@icloud.com> 1738605780 -0500	clone: from https://github.com/nshttpd/mikrotik-exporter.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8f0758db2993d670b317ac6088943699a8e8398e refs/remotes/origin/dependabot/go_modules/github.com/prometheus/client_golang-1.11.1
b0b51dd6c9f263ec01c0ca402ec969851dd5a465 refs/remotes/origin/dependabot/go_modules/golang.org/x/net-0.7.0
986448d7aa2b771c606ed724fd154a2971ea1521 refs/remotes/origin/dependabot/go_modules/golang.org/x/sys-0.1.0
66d72b4d9f569b0c1fdc744e7b2e1d5fc5eaa874 refs/remotes/origin/nshttpd/dead-device
1fa6658917d4070ef987894c2828a27c206e8d07 refs/remotes/origin/nshttpd/debug-health
9e7d70e5441cee78d611864f2f40427572c9f305 refs/remotes/origin/nshttpd/issue-68
b3ed4571d6f642746492c53214aff6e5226dd4b1 refs/remotes/origin/nshttpd/more-metrics
e1b06c6ebe6e71a5661326b3a33afe2fd741283d refs/remotes/origin/trunk
0f7d5bea2cc4c15ca2ce3643d9b8447402ee577f refs/tags/1.0.0
4264ed930f4b2e85a4a821bb40b07ee3737a06c1 refs/tags/1.0.1
bfba6be6086d9601e6918ac97defc298f783f7af refs/tags/1.0.10
9fc2841a61d92271635a9a1cff62b58f5619a279 refs/tags/1.0.11
0cf5d19883cebf5efe90fbed8bd1ce572f35bb4b refs/tags/1.0.11-DEVEL
60bb04d0e7cfefce9723773914f665b287cdd0f6 refs/tags/1.0.12-DEVEL
83cbed45d8142463717e9ffe03ac2f26c5ddef58 refs/tags/1.0.3
aee1517c10068d3704d124bbfeb9ddeec3c460d7 refs/tags/1.0.5
f0ebe4bd0a24a2b4d682c37492c4bac036938c12 refs/tags/1.0.6
dcaef1a51eeaec8b26e41b6e814b79898a30961b refs/tags/1.0.7
530f695305b47b0bea75e2caadc07c919724557d refs/tags/1.0.8
fc9c04efec6868fce4677f18d91baa1cce5e4b4d refs/tags/1.0.9


File: /.git\refs\heads\trunk
e1b06c6ebe6e71a5661326b3a33afe2fd741283d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/trunk


File: /.gitignore
# Binaries for programs and plugins
*.exe
*.dll
*.so
*.dylib

# Test binary, build with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Project-local glide cache, RE: https://github.com/Masterminds/glide/issues/736
.glide/

# IDE specific files
File: /collector\bgp_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type bgpCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newBGPCollector() routerOSCollector {
	c := &bgpCollector{}
	c.init()
	return c
}

func (c *bgpCollector) init() {
	c.props = []string{"name", "remote-as", "state", "prefix-count", "updates-sent", "updates-received", "withdrawn-sent", "withdrawn-received"}

	const prefix = "bgp"
	labelNames := []string{"name", "address", "session", "asn"}

	c.descriptions = make(map[string]*prometheus.Desc)
	c.descriptions["state"] = description(prefix, "up", "BGP session is established (up = 1)", labelNames)

	for _, p := range c.props[3:] {
		c.descriptions[p] = descriptionForPropertyName(prefix, p, labelNames)
	}
}

func (c *bgpCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *bgpCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *bgpCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/routing/bgp/peer/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching bgp metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *bgpCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	asn := re.Map["remote-as"]
	session := re.Map["name"]

	for _, p := range c.props[2:] {
		c.collectMetricForProperty(p, session, asn, re, ctx)
	}
}

func (c *bgpCollector) collectMetricForProperty(property, session, asn string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	v, err := c.parseValueForProperty(property, re.Map[property])
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"session":  session,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing bgp metric value")
		return
	}

	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, session, asn)
}

func (c *bgpCollector) parseValueForProperty(property, value string) (float64, error) {
	if property == "state" {
		if value == "established" {
			return 1, nil
		}

		return 0, nil
	}

	if value == "" {
		return 0, nil
	}

	return strconv.ParseFloat(value, 64)
}


File: /collector\capsman_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type capsmanCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newCapsmanCollector() routerOSCollector {
	c := &capsmanCollector{}
	c.init()
	return c
}

func (c *capsmanCollector) init() {
	//"rx-signal", "tx-signal",
	c.props = []string{"interface", "mac-address", "ssid", "uptime", "tx-signal", "rx-signal", "packets", "bytes"}
	labelNames := []string{"name", "address", "interface", "mac_address", "ssid"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props[3 : len(c.props)-2] {
		c.descriptions[p] = descriptionForPropertyName("capsman_station", p, labelNames)
	}
	for _, p := range c.props[len(c.props)-2:] {
		c.descriptions["tx_"+p] = descriptionForPropertyName("capsman_station", "tx_"+p, labelNames)
		c.descriptions["rx_"+p] = descriptionForPropertyName("capsman_station", "rx_"+p, labelNames)
	}
}

func (c *capsmanCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *capsmanCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *capsmanCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/caps-man/registration-table/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching wlan station metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *capsmanCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	iface := re.Map["interface"]
	mac := re.Map["mac-address"]
	ssid := re.Map["ssid"]

	for _, p := range c.props[3 : len(c.props)-2] {
		c.collectMetricForProperty(p, iface, mac, ssid, re, ctx)
	}
	for _, p := range c.props[len(c.props)-2:] {
		c.collectMetricForTXRXCounters(p, iface, mac, ssid, re, ctx)
	}
}

func (c *capsmanCollector) collectMetricForProperty(property, iface, mac, ssid string, re *proto.Sentence, ctx *collectorContext) {
	if re.Map[property] == "" {
		return
	}
	p := re.Map[property]
	i := strings.Index(p, "@")
	if i > -1 {
		p = p[:i]
	}
	var v float64
	var err error
	if property != "uptime" {
		v, err = strconv.ParseFloat(p, 64)
	} else {
		v, err = parseDuration(p)
	}
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing capsman station metric value")
		return
	}

	desc := c.descriptions[property]
	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, iface, mac, ssid)
}

func (c *capsmanCollector) collectMetricForTXRXCounters(property, iface, mac, ssid string, re *proto.Sentence, ctx *collectorContext) {
	tx, rx, err := splitStringToFloats(re.Map[property])
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing capsman station metric value")
		return
	}
	desc_tx := c.descriptions["tx_"+property]
	desc_rx := c.descriptions["rx_"+property]
	ctx.ch <- prometheus.MustNewConstMetric(desc_tx, prometheus.CounterValue, tx, ctx.device.Name, ctx.device.Address, iface, mac, ssid)
	ctx.ch <- prometheus.MustNewConstMetric(desc_rx, prometheus.CounterValue, rx, ctx.device.Name, ctx.device.Address, iface, mac, ssid)
}


File: /collector\collector.go
package collector

import (
	"crypto/md5"
	"crypto/tls"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"

	"mikrotik-exporter/config"

	"github.com/miekg/dns"
	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	routeros "gopkg.in/routeros.v2"
)

const (
	namespace  = "mikrotik"
	apiPort    = "8728"
	apiPortTLS = "8729"
	dnsPort    = 53

	// DefaultTimeout defines the default timeout when connecting to a router
	DefaultTimeout = 5 * time.Second
)

var (
	scrapeDurationDesc = prometheus.NewDesc(
		prometheus.BuildFQName(namespace, "scrape", "collector_duration_seconds"),
		"mikrotik_exporter: duration of a device collector scrape",
		[]string{"device"},
		nil,
	)
	scrapeSuccessDesc = prometheus.NewDesc(
		prometheus.BuildFQName(namespace, "scrape", "collector_success"),
		"mikrotik_exporter: whether a device collector succeeded",
		[]string{"device"},
		nil,
	)
)

type collector struct {
	devices     []config.Device
	collectors  []routerOSCollector
	timeout     time.Duration
	enableTLS   bool
	insecureTLS bool
}

// WithBGP enables BGP routing metrics
func WithBGP() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newBGPCollector())
	}
}

// WithRoutes enables routing table metrics
func WithRoutes() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newRoutesCollector())
	}
}

// WithDHCP enables DHCP serrver metrics
func WithDHCP() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newDHCPCollector())
	}
}

// WithDHCPL enables DHCP server leases
func WithDHCPL() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newDHCPLCollector())
	}
}

// WithDHCPv6 enables DHCPv6 serrver metrics
func WithDHCPv6() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newDHCPv6Collector())
	}
}

// WithFirmware grab installed firmware and version
func WithFirmware() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newFirmwareCollector())
	}
}

// WithHealth enables board Health metrics
func WithHealth() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newhealthCollector())
	}
}

// WithPOE enables PoE metrics
func WithPOE() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newPOECollector())
	}
}

// WithPools enables IP(v6) pool metrics
func WithPools() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newPoolCollector())
	}
}

// WithOptics enables optical diagnstocs
func WithOptics() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newOpticsCollector())
	}
}

// WithW60G enables w60g metrics
func WithW60G() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, neww60gInterfaceCollector())
	}
}

// WithWlanSTA enables wlan STA metrics
func WithWlanSTA() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newWlanSTACollector())
	}
}

// WithWlanIF enables wireless interface metrics
func WithCapsman() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newCapsmanCollector())
	}
}

// WithWlanIF enables wireless interface metrics
func WithWlanIF() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newWlanIFCollector())
	}
}

// WithMonitor enables ethernet monitor collector metrics
func Monitor() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newMonitorCollector())
	}
}

// WithTimeout sets timeout for connecting to router
func WithTimeout(d time.Duration) Option {
	return func(c *collector) {
		c.timeout = d
	}
}

// WithTLS enables TLS
func WithTLS(insecure bool) Option {
	return func(c *collector) {
		c.enableTLS = true
		c.insecureTLS = insecure
	}
}

// WithIpsec enables ipsec metrics
func WithIpsec() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newIpsecCollector())
	}
}

// WithConntrack enables firewall/NAT connection tracking metrics
func WithConntrack() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newConntrackCollector())
	}
}

// WithLte enables lte metrics
func WithLte() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newLteCollector())
	}
}

// WithNetwatch enables netwatch metrics
func WithNetwatch() Option {
	return func(c *collector) {
		c.collectors = append(c.collectors, newNetwatchCollector())
	}
}

// Option applies options to collector
type Option func(*collector)

// NewCollector creates a collector instance
func NewCollector(cfg *config.Config, opts ...Option) (prometheus.Collector, error) {
	log.WithFields(log.Fields{
		"numDevices": len(cfg.Devices),
	}).Info("setting up collector for devices")

	c := &collector{
		devices: cfg.Devices,
		timeout: DefaultTimeout,
		collectors: []routerOSCollector{
			newInterfaceCollector(),
			newResourceCollector(),
		},
	}

	for _, o := range opts {
		o(c)
	}

	return c, nil
}

// Describe implements the prometheus.Collector interface.
func (c *collector) Describe(ch chan<- *prometheus.Desc) {
	ch <- scrapeDurationDesc
	ch <- scrapeSuccessDesc

	for _, co := range c.collectors {
		co.describe(ch)
	}
}

// Collect implements the prometheus.Collector interface.
func (c *collector) Collect(ch chan<- prometheus.Metric) {
	wg := sync.WaitGroup{}

	var realDevices []config.Device

	for _, dev := range c.devices {
		if (config.SrvRecord{}) != dev.Srv {
			log.WithFields(log.Fields{
				"SRV": dev.Srv.Record,
			}).Info("SRV configuration detected")
			conf, _ := dns.ClientConfigFromFile("/etc/resolv.conf")
			dnsServer := net.JoinHostPort(conf.Servers[0], strconv.Itoa(dnsPort))
			if (config.DnsServer{}) != dev.Srv.Dns {
				dnsServer = net.JoinHostPort(dev.Srv.Dns.Address, strconv.Itoa(dev.Srv.Dns.Port))
				log.WithFields(log.Fields{
					"DnsServer": dnsServer,
				}).Info("Custom DNS config detected")
			}
			dnsMsg := new(dns.Msg)
			dnsCli := new(dns.Client)

			dnsMsg.RecursionDesired = true
			dnsMsg.SetQuestion(dns.Fqdn(dev.Srv.Record), dns.TypeSRV)
			r, _, err := dnsCli.Exchange(dnsMsg, dnsServer)

			if err != nil {
				os.Exit(1)
			}

			for _, k := range r.Answer {
				if s, ok := k.(*dns.SRV); ok {
					d := config.Device{}
					d.Name = strings.TrimRight(s.Target, ".")
					d.Address = strings.TrimRight(s.Target, ".")
					d.User = dev.User
					d.Password = dev.Password
					_ = c.getIdentity(&d)
					realDevices = append(realDevices, d)
				}
			}
		} else {
			realDevices = append(realDevices, dev)
		}
	}

	wg.Add(len(realDevices))

	for _, dev := range realDevices {
		go func(d config.Device) {
			c.collectForDevice(d, ch)
			wg.Done()
		}(dev)
	}

	wg.Wait()
}

func (c *collector) getIdentity(d *config.Device) error {
	cl, err := c.connect(d)
	if err != nil {
		log.WithFields(log.Fields{
			"device": d.Name,
			"error":  err,
		}).Error("error dialing device fetching identity")
		return err
	}
	defer cl.Close()
	reply, err := cl.Run("/system/identity/print")
	if err != nil {
		log.WithFields(log.Fields{
			"device": d.Name,
			"error":  err,
		}).Error("error fetching ethernet interfaces")
		return err
	}
	for _, id := range reply.Re {
		d.Name = id.Map["name"]
	}
	return nil
}

func (c *collector) collectForDevice(d config.Device, ch chan<- prometheus.Metric) {
	begin := time.Now()

	err := c.connectAndCollect(&d, ch)

	duration := time.Since(begin)
	var success float64
	if err != nil {
		log.Errorf("ERROR: %s collector failed after %fs: %s", d.Name, duration.Seconds(), err)
		success = 0
	} else {
		log.Debugf("OK: %s collector succeeded after %fs.", d.Name, duration.Seconds())
		success = 1
	}

	ch <- prometheus.MustNewConstMetric(scrapeDurationDesc, prometheus.GaugeValue, duration.Seconds(), d.Name)
	ch <- prometheus.MustNewConstMetric(scrapeSuccessDesc, prometheus.GaugeValue, success, d.Name)
}

func (c *collector) connectAndCollect(d *config.Device, ch chan<- prometheus.Metric) error {
	cl, err := c.connect(d)
	if err != nil {
		log.WithFields(log.Fields{
			"device": d.Name,
			"error":  err,
		}).Error("error dialing device")
		return err
	}
	defer cl.Close()

	for _, co := range c.collectors {
		ctx := &collectorContext{ch, d, cl}
		err = co.collect(ctx)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *collector) connect(d *config.Device) (*routeros.Client, error) {
	var conn net.Conn
	var err error

	log.WithField("device", d.Name).Debug("trying to Dial")
	if !c.enableTLS {
		if (d.Port) == "" {
			d.Port = apiPort
		}
		conn, err = net.DialTimeout("tcp", d.Address+":"+d.Port, c.timeout)
		if err != nil {
			return nil, err
		}
		//		return routeros.DialTimeout(d.Address+apiPort, d.User, d.Password, c.timeout)
	} else {
		tlsCfg := &tls.Config{
			InsecureSkipVerify: c.insecureTLS,
		}
		if (d.Port) == "" {
			d.Port = apiPortTLS
		}
		conn, err = tls.DialWithDialer(&net.Dialer{
			Timeout: c.timeout,
		},
			"tcp", d.Address+":"+d.Port, tlsCfg)
		if err != nil {
			return nil, err
		}
	}
	log.WithField("device", d.Name).Debug("done dialing")

	client, err := routeros.NewClient(conn)
	if err != nil {
		return nil, err
	}
	log.WithField("device", d.Name).Debug("got client")

	log.WithField("device", d.Name).Debug("trying to login")
	r, err := client.Run("/login", "=name="+d.User, "=password="+d.Password)
	if err != nil {
		return nil, err
	}
	ret, ok := r.Done.Map["ret"]
	if !ok {
		// Login method post-6.43 one stage, cleartext and no challenge
		if r.Done != nil {
			return client, nil
		}
		return nil, errors.New("RouterOS: /login: no ret (challenge) received")
	}

	// Login method pre-6.43 two stages, challenge
	b, err := hex.DecodeString(ret)
	if err != nil {
		return nil, fmt.Errorf("RouterOS: /login: invalid ret (challenge) hex string received: %s", err)
	}

	r, err = client.Run("/login", "=name="+d.User, "=response="+challengeResponse(b, d.Password))
	if err != nil {
		return nil, err
	}
	log.WithField("device", d.Name).Debug("done wth login")

	return client, nil

	//tlsCfg := &tls.Config{
	//	InsecureSkipVerify: c.insecureTLS,
	//}
	//	return routeros.DialTLSTimeout(d.Address+apiPortTLS, d.User, d.Password, tlsCfg, c.timeout)
}

func challengeResponse(cha []byte, password string) string {
	h := md5.New()
	h.Write([]byte{0})
	_, _ = io.WriteString(h, password)
	h.Write(cha)
	return fmt.Sprintf("00%x", h.Sum(nil))
}


File: /collector\collector_context.go
package collector

import (
	"mikrotik-exporter/config"

	"github.com/prometheus/client_golang/prometheus"
	routeros "gopkg.in/routeros.v2"
)

type collectorContext struct {
	ch     chan<- prometheus.Metric
	device *config.Device
	client *routeros.Client
}


File: /collector\conntrack_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type conntrackCollector struct {
	props            []string
	totalEntriesDesc *prometheus.Desc
	maxEntriesDesc   *prometheus.Desc
}

func newConntrackCollector() routerOSCollector {
	const prefix = "conntrack"

	labelNames := []string{"name", "address"}
	return &conntrackCollector{
		props:            []string{"total-entries", "max-entries"},
		totalEntriesDesc: description(prefix, "entries", "Number of tracked connections", labelNames),
		maxEntriesDesc:   description(prefix, "max_entries", "Conntrack table capacity", labelNames),
	}
}

func (c *conntrackCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.totalEntriesDesc
	ch <- c.maxEntriesDesc
}

func (c *conntrackCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/ip/firewall/connection/tracking/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching conntrack table metrics")
		return err
	}

	for _, re := range reply.Re {
		c.collectMetricForProperty("total-entries", c.totalEntriesDesc, re, ctx)
		c.collectMetricForProperty("max-entries", c.maxEntriesDesc, re, ctx)
	}

	return nil
}

func (c *conntrackCollector) collectMetricForProperty(property string, desc *prometheus.Desc, re *proto.Sentence, ctx *collectorContext) {
	if re.Map[property] == "" {
		return
	}
	v, err := strconv.ParseFloat(re.Map[property], 64)
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing conntrack metric value")
		return
	}

	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address)
}


File: /collector\dhcpv6_collector.go
package collector

import (
	"fmt"
	"strconv"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type dhcpv6Collector struct {
	bindingCountDesc *prometheus.Desc
}

func newDHCPv6Collector() routerOSCollector {
	c := &dhcpv6Collector{}
	c.init()
	return c
}

func (c *dhcpv6Collector) init() {
	const prefix = "dhcpv6"

	labelNames := []string{"name", "address", "server"}
	c.bindingCountDesc = description(prefix, "binding_count", "number of active bindings per DHCPv6 server", labelNames)
}

func (c *dhcpv6Collector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.bindingCountDesc
}

func (c *dhcpv6Collector) collect(ctx *collectorContext) error {
	names, err := c.fetchDHCPServerNames(ctx)
	if err != nil {
		return err
	}

	for _, n := range names {
		err := c.colllectForDHCPServer(ctx, n)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *dhcpv6Collector) fetchDHCPServerNames(ctx *collectorContext) ([]string, error) {
	reply, err := ctx.client.Run("/ipv6/dhcp-server/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching DHCPv6 server names")
		return nil, err
	}

	names := []string{}
	for _, re := range reply.Re {
		names = append(names, re.Map["name"])
	}

	return names, nil
}

func (c *dhcpv6Collector) colllectForDHCPServer(ctx *collectorContext, dhcpServer string) error {
	reply, err := ctx.client.Run("/ipv6/dhcp-server/binding/print", fmt.Sprintf("?server=%s", dhcpServer), "=count-only=")
	if err != nil {
		log.WithFields(log.Fields{
			"dhcpv6_server": dhcpServer,
			"device":        ctx.device.Name,
			"error":         err,
		}).Error("error fetching DHCPv6 binding counts")
		return err
	}

	v, err := strconv.ParseFloat(reply.Done.Map["ret"], 32)
	if err != nil {
		log.WithFields(log.Fields{
			"dhcpv6_server": dhcpServer,
			"device":        ctx.device.Name,
			"error":         err,
		}).Error("error parsing DHCPv6 binding counts")
		return err
	}

	ctx.ch <- prometheus.MustNewConstMetric(c.bindingCountDesc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, dhcpServer)
	return nil
}


File: /collector\dhcp_collector.go
package collector

import (
	"fmt"
	"strconv"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type dhcpCollector struct {
	leasesActiveCountDesc *prometheus.Desc
}

func (c *dhcpCollector) init() {
	const prefix = "dhcp"

	labelNames := []string{"name", "address", "server"}
	c.leasesActiveCountDesc = description(prefix, "leases_active_count", "number of active leases per DHCP server", labelNames)
}

func newDHCPCollector() routerOSCollector {
	c := &dhcpCollector{}
	c.init()
	return c
}

func (c *dhcpCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.leasesActiveCountDesc
}

func (c *dhcpCollector) collect(ctx *collectorContext) error {
	names, err := c.fetchDHCPServerNames(ctx)
	if err != nil {
		return err
	}

	for _, n := range names {
		err := c.colllectForDHCPServer(ctx, n)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *dhcpCollector) fetchDHCPServerNames(ctx *collectorContext) ([]string, error) {
	reply, err := ctx.client.Run("/ip/dhcp-server/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching DHCP server names")
		return nil, err
	}

	names := []string{}
	for _, re := range reply.Re {
		names = append(names, re.Map["name"])
	}

	return names, nil
}

func (c *dhcpCollector) colllectForDHCPServer(ctx *collectorContext, dhcpServer string) error {
	reply, err := ctx.client.Run("/ip/dhcp-server/lease/print", fmt.Sprintf("?server=%s", dhcpServer), "=active=", "=count-only=")
	if err != nil {
		log.WithFields(log.Fields{
			"dhcp_server": dhcpServer,
			"device":      ctx.device.Name,
			"error":       err,
		}).Error("error fetching DHCP lease counts")
		return err
	}
	if reply.Done.Map["ret"] == "" {
		return nil
	}
	v, err := strconv.ParseFloat(reply.Done.Map["ret"], 32)
	if err != nil {
		log.WithFields(log.Fields{
			"dhcp_server": dhcpServer,
			"device":      ctx.device.Name,
			"error":       err,
		}).Error("error parsing DHCP lease counts")
		return err
	}

	ctx.ch <- prometheus.MustNewConstMetric(c.leasesActiveCountDesc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, dhcpServer)
	return nil
}


File: /collector\dhcp_lease_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type dhcpLeaseCollector struct {
	props        []string
	descriptions *prometheus.Desc
}

func (c *dhcpLeaseCollector) init() {
	c.props = []string{"active-mac-address", "server", "status", "expires-after", "active-address", "host-name"}

	labelNames := []string{"name", "address", "activemacaddress", "server", "status", "expiresafter", "activeaddress", "hostname"}
	c.descriptions = description("dhcp", "leases_metrics", "number of metrics", labelNames)

}

func newDHCPLCollector() routerOSCollector {
	c := &dhcpLeaseCollector{}
	c.init()
	return c
}

func (c *dhcpLeaseCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.descriptions
}

func (c *dhcpLeaseCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectMetric(ctx, re)
	}

	return nil
}

func (c *dhcpLeaseCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/ip/dhcp-server/lease/print", "?status=bound", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching DHCP leases metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *dhcpLeaseCollector) collectMetric(ctx *collectorContext, re *proto.Sentence) {
	v := 1.0

	f, err := parseDuration(re.Map["expires-after"])
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": "expires-after",
			"value":    re.Map["expires-after"],
			"error":    err,
		}).Error("error parsing duration metric value")
		return
	}

	activemacaddress := re.Map["active-mac-address"]
	server := re.Map["server"]
	status := re.Map["status"]
	activeaddress := re.Map["active-address"]
	// QuoteToASCII because of broken DHCP clients
	hostname := strconv.QuoteToASCII(re.Map["host-name"])

	metric, err := prometheus.NewConstMetric(c.descriptions, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, activemacaddress, server, status, strconv.FormatFloat(f, 'f', 0, 64), activeaddress, hostname)
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error parsing dhcp lease")
		return
	}
	ctx.ch <- metric
}


File: /collector\firmware_collector.go
package collector

import (
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type firmwareCollector struct {
	props       []string
	description *prometheus.Desc
}

func newFirmwareCollector() routerOSCollector {
	c := &firmwareCollector{}
	c.init()
	return c
}

func (c *firmwareCollector) init() {
	labelNames := []string{"devicename", "name", "disabled", "version", "build_time"}
	c.description = description("system", "package", "system packages version", labelNames)
}

func (c *firmwareCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.description
}

func (c *firmwareCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/system/package/getall")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		})
		return err
	}

	pkgs := reply.Re

	for _, pkg := range pkgs {
		v := 1.0
		if strings.EqualFold(pkg.Map["disabled"], "true") {
			v = 0.0
		}
		ctx.ch <- prometheus.MustNewConstMetric(c.description, prometheus.GaugeValue, v, ctx.device.Name, pkg.Map["name"], pkg.Map["disabled"], pkg.Map["version"], pkg.Map["build-time"])
	}

	return nil
}


File: /collector\health_collector.go
package collector

import (
	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
	"strconv"
)

type healthCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newhealthCollector() routerOSCollector {
	c := &healthCollector{}
	c.init()
	return c
}

func (c *healthCollector) init() {
	c.props = []string{"voltage", "temperature", "cpu-temperature"}

	labelNames := []string{"name", "address"}
	helpText := []string{"Input voltage to the RouterOS board, in volts", "Temperature of RouterOS board, in degrees Celsius", "Temperature of RouterOS CPU, in degrees Celsius"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for i, p := range c.props {
		c.descriptions[p] = descriptionForPropertyNameHelpText("health", p, labelNames, helpText[i])
	}
}

func (c *healthCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *healthCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		if metric, ok := re.Map["name"]; ok {
			c.collectMetricForProperty(metric, re, ctx)
		} else {
			c.collectForStat(re, ctx)
		}
	}

	return nil
}

func (c *healthCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/system/health/print")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching system health metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *healthCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	for _, p := range c.props[:3] {
		c.collectMetricForProperty(p, re, ctx)
	}
}

func (c *healthCollector) collectMetricForProperty(property string, re *proto.Sentence, ctx *collectorContext) {
	var v float64
	var err error

	name := property
	value := re.Map[property]

	if value == "" {
		var ok bool
		if value, ok = re.Map["value"]; !ok {
			return
		}
	}
	v, err = strconv.ParseFloat(value, 64)

	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": name,
			"value":    value,
			"error":    err,
		}).Error("error parsing system health metric value")
		return
	}

	desc := c.descriptions[name]
	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address)
}


File: /collector\helper.go
package collector

import (
	"fmt"
	"math"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

var durationRegex *regexp.Regexp
var durationParts [6]time.Duration

func init() {
	durationRegex = regexp.MustCompile(`(?:(\d*)w)?(?:(\d*)d)?(?:(\d*)h)?(?:(\d*)m)?(?:(\d*)s)?(?:(\d*)ms)?`)
	durationParts = [6]time.Duration{time.Hour * 168, time.Hour * 24, time.Hour, time.Minute, time.Second, time.Millisecond}
}

func metricStringCleanup(in string) string {
	return strings.Replace(in, "-", "_", -1)
}

func descriptionForPropertyName(prefix, property string, labelNames []string) *prometheus.Desc {
	return descriptionForPropertyNameHelpText(prefix, property, labelNames, property)
}

func descriptionForPropertyNameHelpText(prefix, property string, labelNames []string, helpText string) *prometheus.Desc {
	return prometheus.NewDesc(
		prometheus.BuildFQName(namespace, prefix, metricStringCleanup(property)),
		helpText,
		labelNames,
		nil,
	)
}

func description(prefix, name, helpText string, labelNames []string) *prometheus.Desc {
	return prometheus.NewDesc(
		prometheus.BuildFQName(namespace, prefix, metricStringCleanup(name)),
		helpText,
		labelNames,
		nil,
	)
}

func splitStringToFloats(metric string) (float64, float64, error) {
	strs := strings.Split(metric, ",")
	if len(strs) == 0 {
		return 0, 0, nil
	}
	m1, err := strconv.ParseFloat(strs[0], 64)
	if err != nil {
		return math.NaN(), math.NaN(), err
	}
	m2, err := strconv.ParseFloat(strs[1], 64)
	if err != nil {
		return math.NaN(), math.NaN(), err
	}
	return m1, m2, nil
}

func parseDuration(duration string) (float64, error) {
	var u time.Duration

	reMatch := durationRegex.FindAllStringSubmatch(duration, -1)

	// should get one and only one match back on the regex
	if len(reMatch) != 1 {
		return 0, fmt.Errorf("invalid duration value sent to regex")
	} else {
		for i, match := range reMatch[0] {
			if match != "" && i != 0 {
				v, err := strconv.Atoi(match)
				if err != nil {
					log.WithFields(log.Fields{
						"duration": duration,
						"value":    match,
						"error":    err,
					}).Error("error parsing duration field value")
					return float64(0), err
				}
				u += time.Duration(v) * durationParts[i-1]
			}
		}
	}
	return u.Seconds(), nil
}


File: /collector\helper_test.go
package collector

import (
	"math"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSplitStringToFloats(t *testing.T) {
	var testCases = []struct {
		input    string
		expected struct {
			f1 float64
			f2 float64
		}
		isNaN    bool
		hasError bool
	}{
		{
			"1.2,2.1",
			struct {
				f1 float64
				f2 float64
			}{
				1.2,
				2.1,
			},
			false,
			false,
		},
		{
			input:    "1.2,",
			isNaN:    true,
			hasError: true,
		},
		{
			input:    ",2.1",
			isNaN:    true,
			hasError: true,
		},
		{
			"1.2,2.1,3.2",
			struct {
				f1 float64
				f2 float64
			}{
				1.2,
				2.1,
			},
			false,
			false,
		},
		{
			input:    "",
			isNaN:    true,
			hasError: true,
		},
	}

	for _, testCase := range testCases {
		f1, f2, err := splitStringToFloats(testCase.input)

		switch testCase.hasError {
		case true:
			assert.Error(t, err)
		case false:
			assert.NoError(t, err)
		}

		switch testCase.isNaN {
		case true:
			assert.True(t, math.IsNaN(f1))
			assert.True(t, math.IsNaN(f2))
		case false:
			assert.Equal(t, testCase.expected.f1, f1)
			assert.Equal(t, testCase.expected.f2, f2)
		}
	}
}

func TestParseDuration(t *testing.T) {
	var testCases = []struct {
		input    string
		output   float64
		hasError bool
	}{
		{
			"3d3h42m53s",
			272573,
			false,
		},
		{
			"15w3d3h42m53s",
			9344573,
			false,
		},
		{
			"42m53s",
			2573,
			false,
		},
		{
			"7w6d9h34m",
			4786440,
			false,
		},
		{
			"59",
			0,
			true,
		},
		{
			"s",
			0,
			false,
		},
		{
			"",
			0,
			false,
		},
	}

	for _, testCase := range testCases {
		f, err := parseDuration(testCase.input)

		switch testCase.hasError {
		case true:
			assert.Error(t, err)
		case false:
			assert.NoError(t, err)
		}

		assert.Equal(t, testCase.output, f)
	}
}


File: /collector\interface_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type interfaceCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newInterfaceCollector() routerOSCollector {
	c := &interfaceCollector{}
	c.init()
	return c
}

func (c *interfaceCollector) init() {
	c.props = []string{"name", "type", "disabled", "comment", "slave", "actual-mtu", "running", "rx-byte", "tx-byte", "rx-packet", "tx-packet", "rx-error", "tx-error", "rx-drop", "tx-drop", "link-downs"}
	labelNames := []string{"name", "address", "interface", "type", "disabled", "comment", "running", "slave"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props[5:] {
		c.descriptions[p] = descriptionForPropertyName("interface", p, labelNames)
	}
}

func (c *interfaceCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *interfaceCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *interfaceCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/interface/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *interfaceCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	for _, p := range c.props[5:] {
		c.collectMetricForProperty(p, re, ctx)
	}
}

func (c *interfaceCollector) collectMetricForProperty(property string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	if value := re.Map[property]; value != "" {
		var (
			v     float64
			vtype prometheus.ValueType
			err   error
		)
		vtype = prometheus.CounterValue

		switch property {
		case "running":
			vtype = prometheus.GaugeValue
			if value == "true" {
				v = 1
			} else {
				v = 0
			}
		case "actual-mtu":
			vtype = prometheus.GaugeValue
			fallthrough
		default:
			v, err = strconv.ParseFloat(value, 64)
			if err != nil {
				log.WithFields(log.Fields{
					"device":    ctx.device.Name,
					"interface": re.Map["name"],
					"property":  property,
					"value":     value,
					"error":     err,
				}).Error("error parsing interface metric value")
				return
			}
		}
		ctx.ch <- prometheus.MustNewConstMetric(desc, vtype, v, ctx.device.Name, ctx.device.Address,
			re.Map["name"], re.Map["type"], re.Map["disabled"], re.Map["comment"], re.Map["running"], re.Map["slave"])

	}
}


File: /collector\ipsec_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type ipsecCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newIpsecCollector() routerOSCollector {
	c := &ipsecCollector{}
	c.init()
	return c
}

func (c *ipsecCollector) init() {
	c.props = []string{"src-address", "dst-address", "ph2-state", "invalid", "active", "comment"}

	labelNames := []string{"devicename", "srcdst", "comment"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props[1:] {
		c.descriptions[p] = descriptionForPropertyName("ipsec", p, labelNames)
	}
}

func (c *ipsecCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *ipsecCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *ipsecCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/ip/ipsec/policy/print", "?disabled=false", "?dynamic=false", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *ipsecCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	srcdst := re.Map["src-address"] + "-" + re.Map["dst-address"]
	comment := re.Map["comment"]

	for _, p := range c.props[2:] {
		c.collectMetricForProperty(p, srcdst, comment, re, ctx)
	}
}

func (c *ipsecCollector) collectMetricForProperty(property, srcdst, comment string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	if value := re.Map[property]; value != "" {
		var v float64
		var err error
		v, err = strconv.ParseFloat(value, 64)

		switch property {
		case "ph2-state":
			if value == "established" {
				v, err = 1, nil
			} else {
				v, err = 0, nil
			}
		case "active", "invalid":
			if value == "true" {
				v, err = 1, nil
			} else {
				v, err = 0, nil
			}
		case "comment":
			return
		}

		if err != nil {
			log.WithFields(log.Fields{
				"device":   ctx.device.Name,
				"srcdst":   srcdst,
				"property": property,
				"value":    value,
				"error":    err,
			}).Error("error parsing ipsec metric value")
			return
		}
		ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.CounterValue, v, ctx.device.Name, srcdst, comment)
	}
}


File: /collector\lte_collector.go
package collector

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type lteCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newLteCollector() routerOSCollector {
	c := &lteCollector{}
	c.init()
	return c
}

func (c *lteCollector) init() {
	c.props = []string{"current-cellid", "primary-band" ,"ca-band", "rssi", "rsrp", "rsrq", "sinr"}
	labelNames := []string{"name", "address", "interface", "cellid", "primaryband", "caband"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props {
		c.descriptions[p] = descriptionForPropertyName("lte_interface", p, labelNames)
	}
}

func (c *lteCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *lteCollector) collect(ctx *collectorContext) error {
	names, err := c.fetchInterfaceNames(ctx)
	if err != nil {
		return err
	}

	for _, n := range names {
		err := c.collectForInterface(n, ctx)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *lteCollector) fetchInterfaceNames(ctx *collectorContext) ([]string, error) {
	reply, err := ctx.client.Run("/interface/lte/print", "?disabled=false", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching lte interface names")
		return nil, err
	}

	names := []string{}
	for _, re := range reply.Re {
		names = append(names, re.Map["name"])
	}

	return names, nil
}

func (c *lteCollector) collectForInterface(iface string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/lte/info", fmt.Sprintf("=number=%s", iface), "=once=", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"interface": iface,
			"device":    ctx.device.Name,
			"error":     err,
		}).Error("error fetching interface statistics")
		return err
	}

	for _, p := range c.props[3:] {
		// there's always going to be only one sentence in reply, as we
		// have to explicitly specify the interface
		c.collectMetricForProperty(p, iface, reply.Re[0], ctx)
	}

	return nil
}

func (c *lteCollector) collectMetricForProperty(property, iface string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	current_cellid := re.Map["current-cellid"]
	// get only band and its width, drop earfcn and phy-cellid info
	primaryband := re.Map["primary-band"]
	if primaryband != "" {
		primaryband = strings.Fields(primaryband)[0]
	}
	caband := re.Map["ca-band"]
	if caband != "" {
		caband = strings.Fields(caband)[0]
	}

	if re.Map[property] == "" {
		return
	}
	v, err := strconv.ParseFloat(re.Map[property], 64)
	if err != nil {
		log.WithFields(log.Fields{
			"property":  property,
			"interface": iface,
			"device":    ctx.device.Name,
			"error":     err,
		}).Error("error parsing interface metric value")
		return
	}

	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, iface, current_cellid, primaryband, caband)
}


File: /collector\monitor_collector.go
package collector

import (
	"strings"

	"gopkg.in/routeros.v2/proto"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type monitorCollector struct {
	props        []string // props from monitor, can add other ether props later if needed
	descriptions map[string]*prometheus.Desc
}

func newMonitorCollector() routerOSCollector {
	c := &monitorCollector{}
	c.init()
	return c
}

func (c *monitorCollector) init() {
	c.props = []string{"status", "rate", "full-duplex"}
	labelNames := []string{"name", "address", "interface"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props {
		c.descriptions[p] = descriptionForPropertyName("monitor", p, labelNames)
	}
}

func (c *monitorCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *monitorCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching ethernet interfaces")
		return err
	}

	eths := make([]string, len(reply.Re))
	for idx, eth := range reply.Re {
		eths[idx] = eth.Map["name"]
	}

	return c.collectForMonitor(eths, ctx)
}

func (c *monitorCollector) collectForMonitor(eths []string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/monitor",
		"=numbers="+strings.Join(eths, ","),
		"=once=",
		"=.proplist=name,"+strings.Join(c.props, ","))

	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching ethernet monitor info")
		return err
	}

	for _, e := range reply.Re {
		c.collectMetricsForEth(e.Map["name"], e, ctx)
	}

	return nil
}

func (c *monitorCollector) collectMetricsForEth(name string, se *proto.Sentence, ctx *collectorContext) {
	for _, prop := range c.props {
		v, ok := se.Map[prop]
		if !ok {
			continue
		}

		value := float64(c.valueForProp(prop, v))

		ctx.ch <- prometheus.MustNewConstMetric(c.descriptions[prop], prometheus.GaugeValue, value, ctx.device.Name, ctx.device.Address, name)

	}

}

func (c *monitorCollector) valueForProp(name, value string) int {
	switch {
	case name == "status":
		return func(v string) int {
			if v == "link-ok" {
				return 1
			}
			return 0
		}(value)
	case name == "rate":
		return func(v string) int {
			switch {
			case v == "10Mbps":
				return 10
			case v == "100Mbps":
				return 100
			case v == "1Gbps":
				return 1000
			case v == "10Gbps":
				return 10000
			}
			return 0
		}(value)
	case name == "full-duplex":
		return func(v string) int {
			if v == "true" {
				return 1
			}
			return 0
		}(value)
	default:
		return 0
	}
}


File: /collector\netwatch_collector.go
package collector

import (
	"fmt"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type netwatchCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newNetwatchCollector() routerOSCollector {
	c := &netwatchCollector{}
	c.init()
	return c
}

func (c *netwatchCollector) init() {
	c.props = []string{"host", "comment", "status"}
	labelNames := []string{"name", "address", "host", "comment"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props[1:] {
		c.descriptions[p] = descriptionForPropertyName("netwatch", p, labelNames)
	}
}

func (c *netwatchCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *netwatchCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *netwatchCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/tool/netwatch/print", "?disabled=false", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching netwatch metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *netwatchCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	host := re.Map["host"]
	comment := re.Map["comment"]

	for _, p := range c.props[2:] {
		c.collectMetricForProperty(p, host, comment, re, ctx)
	}
}

func (c *netwatchCollector) collectMetricForProperty(property, host, comment string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	if value := re.Map[property]; value != "" {
		var numericValue float64
		switch value {
		case "up":
			numericValue = 1
		case "unknown":
			numericValue = 0
		case "down":
			numericValue = -1
		default:
			log.WithFields(log.Fields{
				"device":   ctx.device.Name,
				"host":     host,
				"property": property,
				"value":    value,
				"error":    fmt.Errorf("unexpected netwatch status value"),
			}).Error("error parsing netwatch metric value")
		}
		ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.CounterValue, numericValue, ctx.device.Name, ctx.device.Address, host, comment)
	}
}


File: /collector\optics_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type opticsCollector struct {
	rxStatusDesc    *prometheus.Desc
	txStatusDesc    *prometheus.Desc
	rxPowerDesc     *prometheus.Desc
	txPowerDesc     *prometheus.Desc
	temperatureDesc *prometheus.Desc
	txBiasDesc      *prometheus.Desc
	voltageDesc     *prometheus.Desc
	props           []string
}

func newOpticsCollector() routerOSCollector {
	const prefix = "optics"

	labelNames := []string{"name", "address", "interface"}
	return &opticsCollector{
		rxStatusDesc:    description(prefix, "rx_status", "RX status (1 = no loss)", labelNames),
		txStatusDesc:    description(prefix, "tx_status", "TX status (1 = no faults)", labelNames),
		rxPowerDesc:     description(prefix, "rx_power_dbm", "RX power in dBM", labelNames),
		txPowerDesc:     description(prefix, "tx_power_dbm", "TX power in dBM", labelNames),
		temperatureDesc: description(prefix, "temperature_celsius", "temperature in degree celsius", labelNames),
		txBiasDesc:      description(prefix, "tx_bias_ma", "bias is milliamps", labelNames),
		voltageDesc:     description(prefix, "voltage_volt", "volage in volt", labelNames),
		props:           []string{"sfp-rx-loss", "sfp-tx-fault", "sfp-temperature", "sfp-supply-voltage", "sfp-tx-bias-current", "sfp-tx-power", "sfp-rx-power"},
	}
}

func (c *opticsCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.rxStatusDesc
	ch <- c.txStatusDesc
	ch <- c.rxPowerDesc
	ch <- c.txPowerDesc
	ch <- c.temperatureDesc
	ch <- c.txBiasDesc
	ch <- c.voltageDesc
}

func (c *opticsCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface metrics")
		return err
	}

	ifaces := make([]string, 0)
	for _, iface := range reply.Re {
		n := iface.Map["name"]
		if strings.HasPrefix(n, "sfp") {
			ifaces = append(ifaces, n)
		}
	}

	if len(ifaces) == 0 {
		return nil
	}

	return c.collectOpticalMetricsForInterfaces(ifaces, ctx)
}

func (c *opticsCollector) collectOpticalMetricsForInterfaces(ifaces []string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/monitor",
		"=numbers="+strings.Join(ifaces, ","),
		"=once=",
		"=.proplist=name,"+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface monitor metrics")
		return err
	}

	for _, se := range reply.Re {
		name, ok := se.Map["name"]
		if !ok {
			continue
		}

		c.collectMetricsForInterface(name, se, ctx)
	}

	return nil
}

func (c *opticsCollector) collectMetricsForInterface(name string, se *proto.Sentence, ctx *collectorContext) {
	for _, prop := range c.props {
		v, ok := se.Map[prop]
		if !ok {
			continue
		}

		value, err := c.valueForKey(prop, v)
		if err != nil {
			log.WithFields(log.Fields{
				"device":    ctx.device.Name,
				"interface": name,
				"property":  prop,
				"error":     err,
			}).Error("error parsing interface monitor metric")
			return
		}

		ctx.ch <- prometheus.MustNewConstMetric(c.descForKey(prop), prometheus.GaugeValue, value, ctx.device.Name, ctx.device.Address, name)
	}
}

func (c *opticsCollector) valueForKey(name, value string) (float64, error) {
	if name == "sfp-rx-loss" || name == "sfp-tx-fault" {
		status := float64(1)
		if value == "true" {
			status = float64(0)
		}

		return status, nil
	}

	return strconv.ParseFloat(value, 64)
}

func (c *opticsCollector) descForKey(name string) *prometheus.Desc {
	switch name {
	case "sfp-rx-loss":
		return c.rxStatusDesc
	case "sfp-tx-fault":
		return c.txStatusDesc
	case "sfp-temperature":
		return c.temperatureDesc
	case "sfp-supply-voltage":
		return c.voltageDesc
	case "sfp-tx-bias-current":
		return c.txBiasDesc
	case "sfp-tx-power":
		return c.txPowerDesc
	case "sfp-rx-power":
		return c.rxPowerDesc
	}

	return nil
}


File: /collector\poe_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type poeCollector struct {
	currentDesc *prometheus.Desc
	powerDesc   *prometheus.Desc
	voltageDesc *prometheus.Desc
	props       []string
}

func newPOECollector() routerOSCollector {
	const prefix = "poe"

	labelNames := []string{"name", "address", "interface"}
	return &poeCollector{
		currentDesc: description(prefix, "current", "current in mA", labelNames),
		powerDesc:   description(prefix, "wattage", "Power in W", labelNames),
		voltageDesc: description(prefix, "voltage", "Voltage in V", labelNames),
		props:       []string{"poe-out-current", "poe-out-voltage", "poe-out-power"},
	}
}

func (c *poeCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.currentDesc
	ch <- c.powerDesc
	ch <- c.voltageDesc
}

func (c *poeCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/poe/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface poe metrics")
		return err
	}

	ifaces := make([]string, 0)
	for _, iface := range reply.Re {
		n := iface.Map["name"]
		ifaces = append(ifaces, n)
	}

	if len(ifaces) == 0 {
		return nil
	}

	return c.collectPOEMetricsForInterfaces(ifaces, ctx)
}

func (c *poeCollector) collectPOEMetricsForInterfaces(ifaces []string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/ethernet/poe/monitor",
		"=numbers="+strings.Join(ifaces, ","),
		"=once=",
		"=.proplist=name,"+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching interface poe monitor metrics")
		return err
	}

	for _, se := range reply.Re {
		name, ok := se.Map["name"]
		if !ok {
			continue
		}

		c.collectMetricsForInterface(name, se, ctx)
	}

	return nil
}

func (c *poeCollector) collectMetricsForInterface(name string, se *proto.Sentence, ctx *collectorContext) {
	for _, prop := range c.props {
		v, ok := se.Map[prop]
		if !ok {
			continue
		}
		if v == "" {
			continue
		}
		value, err := strconv.ParseFloat(v, 64)
		if err != nil {
			log.WithFields(log.Fields{
				"device":    ctx.device.Name,
				"interface": name,
				"property":  prop,
				"error":     err,
			}).Error("error parsing interface poe monitor metric")
			return
		}

		ctx.ch <- prometheus.MustNewConstMetric(c.descForKey(prop), prometheus.GaugeValue, value, ctx.device.Name, ctx.device.Address, name)
	}
}

func (c *poeCollector) valueForKey(name, value string) (float64, error) {
	return strconv.ParseFloat(value, 64)
}

func (c *poeCollector) descForKey(name string) *prometheus.Desc {
	switch name {
	case "poe-out-current":
		return c.currentDesc
	case "poe-out-voltage":
		return c.voltageDesc
	case "poe-out-power":
		return c.powerDesc
	}

	return nil
}


File: /collector\pool_collector.go
package collector

import (
	"fmt"
	"strconv"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type poolCollector struct {
	usedCountDesc *prometheus.Desc
}

func (c *poolCollector) init() {
	const prefix = "ip_pool"

	labelNames := []string{"name", "address", "ip_version", "pool"}
	c.usedCountDesc = description(prefix, "pool_used_count", "number of used IP/prefixes in a pool", labelNames)
}

func newPoolCollector() routerOSCollector {
	c := &poolCollector{}
	c.init()
	return c
}

func (c *poolCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.usedCountDesc
}

func (c *poolCollector) collect(ctx *collectorContext) error {
	return c.collectForIPVersion("4", "ip", ctx)
}

func (c *poolCollector) collectForIPVersion(ipVersion, topic string, ctx *collectorContext) error {
	names, err := c.fetchPoolNames(ipVersion, topic, ctx)
	if err != nil {
		return err
	}

	for _, n := range names {
		err := c.collectForPool(ipVersion, topic, n, ctx)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *poolCollector) fetchPoolNames(ipVersion, topic string, ctx *collectorContext) ([]string, error) {
	reply, err := ctx.client.Run(fmt.Sprintf("/%s/pool/print", topic), "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching pool names")
		return nil, err
	}

	names := []string{}
	for _, re := range reply.Re {
		names = append(names, re.Map["name"])
	}

	return names, nil
}

func (c *poolCollector) collectForPool(ipVersion, topic, pool string, ctx *collectorContext) error {
	reply, err := ctx.client.Run(fmt.Sprintf("/%s/pool/used/print", topic), fmt.Sprintf("?pool=%s", pool), "=count-only=")
	if err != nil {
		log.WithFields(log.Fields{
			"pool":       pool,
			"ip_version": ipVersion,
			"device":     ctx.device.Name,
			"error":      err,
		}).Error("error fetching pool counts")
		return err
	}
	if reply.Done.Map["ret"] == "" {
		return nil
	}
	v, err := strconv.ParseFloat(reply.Done.Map["ret"], 32)
	if err != nil {
		log.WithFields(log.Fields{
			"pool":       pool,
			"ip_version": ipVersion,
			"device":     ctx.device.Name,
			"error":      err,
		}).Error("error parsing pool counts")
		return err
	}

	ctx.ch <- prometheus.MustNewConstMetric(c.usedCountDesc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, ipVersion, pool)
	return nil
}


File: /collector\resource_collector.go
package collector

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

var uptimeRegex *regexp.Regexp
var uptimeParts [5]time.Duration

func init() {
	uptimeRegex = regexp.MustCompile(`(?:(\d*)w)?(?:(\d*)d)?(?:(\d*)h)?(?:(\d*)m)?(?:(\d*)s)?`)
	uptimeParts = [5]time.Duration{time.Hour * 168, time.Hour * 24, time.Hour, time.Minute, time.Second}
}

type resourceCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newResourceCollector() routerOSCollector {
	c := &resourceCollector{}
	c.init()
	return c
}

func (c *resourceCollector) init() {
	c.props = []string{"free-memory", "total-memory", "cpu-load", "free-hdd-space", "total-hdd-space", "uptime", "board-name", "version"}

	labelNames := []string{"name", "address", "boardname", "version"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props {
		c.descriptions[p] = descriptionForPropertyName("system", p, labelNames)
	}
}

func (c *resourceCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *resourceCollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *resourceCollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/system/resource/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching system resource metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *resourceCollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	for _, p := range c.props[:6] {
		c.collectMetricForProperty(p, re, ctx)
	}
}

func (c *resourceCollector) collectMetricForProperty(property string, re *proto.Sentence, ctx *collectorContext) {
	var v float64
	var vtype prometheus.ValueType
	var err error
	//	const boardname = "BOARD"
	//	const version = "3.33.3"

	boardname := re.Map["board-name"]
	version := re.Map["version"]

	if property == "uptime" {
		v, err = parseUptime(re.Map[property])
		vtype = prometheus.CounterValue
	} else {
		if re.Map[property] == "" {
			return
		}
		v, err = strconv.ParseFloat(re.Map[property], 64)
		vtype = prometheus.GaugeValue
	}

	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing system resource metric value")
		return
	}

	desc := c.descriptions[property]
	ctx.ch <- prometheus.MustNewConstMetric(desc, vtype, v, ctx.device.Name, ctx.device.Address, boardname, version)
}

func parseUptime(uptime string) (float64, error) {
	var u time.Duration

	reMatch := uptimeRegex.FindAllStringSubmatch(uptime, -1)

	// should get one and only one match back on the regex
	if len(reMatch) != 1 {
		return 0, fmt.Errorf("invalid uptime value sent to regex")
	}

	for i, match := range reMatch[0] {
		if match != "" && i != 0 {
			v, err := strconv.Atoi(match)
			if err != nil {
				log.WithFields(log.Fields{
					"uptime": uptime,
					"value":  match,
					"error":  err,
				}).Error("error parsing uptime field value")
				return float64(0), err
			}
			u += time.Duration(v) * uptimeParts[i-1]
		}
	}
	return u.Seconds(), nil
}


File: /collector\resource_collector_test.go
package collector

import (
	"testing"
)

func TestParseUptime(t *testing.T) {

	uptimes := []struct {
		u string
		v float64
	}{
		{"3d3h42m53s", 272573},
		{"15w3d3h42m53s", 9344573},
		{"42m53s", 2573},
		{"7w6d9h34m", 4786440},
	}

	for _, uptime := range uptimes {
		seconds, err := parseUptime(uptime.u)
		if err != nil {
			t.Error(err)
		}
		if seconds != uptime.v {
			t.Errorf("seconds : %f != v : %f\n", seconds, uptime.v)
		}
	}
}


File: /collector\routeros_collector.go
package collector

import (
	"github.com/prometheus/client_golang/prometheus"
)

type routerOSCollector interface {
	describe(ch chan<- *prometheus.Desc)
	collect(ctx *collectorContext) error
}


File: /collector\routes_collector.go
package collector

import (
	"fmt"
	"strconv"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
)

type routesCollector struct {
	protocols         []string
	countDesc         *prometheus.Desc
	countProtocolDesc *prometheus.Desc
}

func newRoutesCollector() routerOSCollector {
	c := &routesCollector{}
	c.init()
	return c
}

func (c *routesCollector) init() {
	const prefix = "routes"
	labelNames := []string{"name", "address", "ip_version"}
	c.countDesc = description(prefix, "total_count", "number of routes in RIB", labelNames)
	c.countProtocolDesc = description(prefix, "protocol_count", "number of routes per protocol in RIB", append(labelNames, "protocol"))

	c.protocols = []string{"bgp", "static", "ospf", "dynamic", "connect", "rip"}
}

func (c *routesCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.countDesc
	ch <- c.countProtocolDesc
}

func (c *routesCollector) collect(ctx *collectorContext) error {
	err := c.colllectForIPVersion("4", "ip", ctx)
	if err != nil {
		return err
	}

	return c.colllectForIPVersion("6", "ip", ctx)
}

func (c *routesCollector) colllectForIPVersion(ipVersion, topic string, ctx *collectorContext) error {
	err := c.colllectCount(ipVersion, topic, ctx)
	if err != nil {
		return err
	}

	for _, p := range c.protocols {
		err := c.colllectCountProtcol(ipVersion, topic, p, ctx)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *routesCollector) colllectCount(ipVersion, topic string, ctx *collectorContext) error {
	reply, err := ctx.client.Run(fmt.Sprintf("/%s/route/print", topic), "?disabled=false", "=count-only=")
	if err != nil {
		log.WithFields(log.Fields{
			"ip_version": ipVersion,
			"device":     ctx.device.Name,
			"topic":      topic,
			"error":      err,
		}).Error("error fetching routes metrics")
		return err
	}
	if reply.Done.Map["ret"] == "" {
		return nil
	}
	v, err := strconv.ParseFloat(reply.Done.Map["ret"], 32)
	if err != nil {
		log.WithFields(log.Fields{
			"ip_version": ipVersion,
			"device":     ctx.device.Name,
			"error":      err,
		}).Error("error parsing routes metrics")
		return err
	}

	ctx.ch <- prometheus.MustNewConstMetric(c.countDesc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, ipVersion)
	return nil
}

func (c *routesCollector) colllectCountProtcol(ipVersion, topic, protocol string, ctx *collectorContext) error {
	reply, err := ctx.client.Run(fmt.Sprintf("/%s/route/print", topic), "?disabled=false", fmt.Sprintf("?%s", protocol), "=count-only=")
	if err != nil {
		log.WithFields(log.Fields{
			"ip_version": ipVersion,
			"protocol":   protocol,
			"device":     ctx.device.Name,
			"error":      err,
		}).Error("error fetching routes metrics")
		return err
	}
	if reply.Done.Map["ret"] == "" {
		return nil
	}
	v, err := strconv.ParseFloat(reply.Done.Map["ret"], 32)
	if err != nil {
		log.WithFields(log.Fields{
			"ip_version": ipVersion,
			"protocol":   protocol,
			"device":     ctx.device.Name,
			"error":      err,
		}).Error("error parsing routes metrics")
		return err
	}

	ctx.ch <- prometheus.MustNewConstMetric(c.countProtocolDesc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, ipVersion, protocol)
	return nil
}


File: /collector\w60g_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type w60gInterfaceCollector struct {
	frequencyDesc         *prometheus.Desc
	txMCSDesc             *prometheus.Desc
	txPHYRateDesc         *prometheus.Desc
	signalDesc            *prometheus.Desc
	rssiDesc              *prometheus.Desc
	txSectorDesc          *prometheus.Desc
	txDistanceDesc        *prometheus.Desc
	txPacketErrorRateDesc *prometheus.Desc
	props                 []string
}

func (c *w60gInterfaceCollector) describe(ch chan<- *prometheus.Desc) {
	ch <- c.frequencyDesc
	ch <- c.txMCSDesc
	ch <- c.txPHYRateDesc
	ch <- c.signalDesc
	ch <- c.rssiDesc
	ch <- c.txSectorDesc
	ch <- c.txDistanceDesc
	ch <- c.txPacketErrorRateDesc
}
func (c *w60gInterfaceCollector) collect(ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/w60g/print", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching w60g interface metrics")
		return err
	}

	ifaces := make([]string, 0)
	for _, iface := range reply.Re {
		n := iface.Map["name"]
		ifaces = append(ifaces, n)
	}

	if len(ifaces) == 0 {
		return nil
	}

	return c.collectw60gMetricsForInterfaces(ifaces, ctx)
}
func (c *w60gInterfaceCollector) collectw60gMetricsForInterfaces(ifaces []string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/w60g/monitor",
		"=numbers="+strings.Join(ifaces, ","),
		"=once=",
		"=.proplist=name,"+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching w60g interface monitor metrics")
		return err
	}
	for _, se := range reply.Re {
		name, ok := se.Map["name"]
		if !ok {
			continue
		}

		c.collectMetricsForw60gInterface(name, se, ctx)
	}

	return nil
}

func (c *w60gInterfaceCollector) collectMetricsForw60gInterface(name string, se *proto.Sentence, ctx *collectorContext) {
	for _, prop := range c.props {
		v, ok := se.Map[prop]
		if !ok {
			continue
		}
		if v == "" {
			continue
		}
		value, err := strconv.ParseFloat(v, 64)
		if err != nil {
			log.WithFields(log.Fields{
				"device":    ctx.device.Name,
				"interface": name,
				"property":  prop,
				"error":     err,
			}).Error("error parsing w60g interface monitor metric")
			return
		}

		ctx.ch <- prometheus.MustNewConstMetric(c.descForKey(prop), prometheus.GaugeValue, value, ctx.device.Name, ctx.device.Address, name)
	}
}

func neww60gInterfaceCollector() routerOSCollector {
	const prefix = "w60ginterface"

	labelNames := []string{"name", "address", "interface"}
	return &w60gInterfaceCollector{
		frequencyDesc:         description(prefix, "frequency", "frequency of tx in MHz", labelNames),
		txMCSDesc:             description(prefix, "txMCS", "TX MCS", labelNames),
		txPHYRateDesc:         description(prefix, "txPHYRate", "PHY Rate in bps", labelNames),
		signalDesc:            description(prefix, "signal", "Signal quality in %", labelNames),
		rssiDesc:              description(prefix, "rssi", "Signal RSSI in dB", labelNames),
		txSectorDesc:          description(prefix, "txSector", "TX Sector", labelNames),
		txDistanceDesc:        description(prefix, "txDistance", "Distance to remote", labelNames),
		txPacketErrorRateDesc: description(prefix, "txPacketErrorRate", "TX Packet Error Rate", labelNames),
		props:                 []string{"signal", "rssi", "tx-mcs", "frequency", "tx-phy-rate", "tx-sector", "distance", "tx-packet-error-rate"},
	}
}

func (c *w60gInterfaceCollector) valueForKey(name, value string) (float64, error) {
	return strconv.ParseFloat(value, 64)
}

func (c *w60gInterfaceCollector) descForKey(name string) *prometheus.Desc {
	switch name {
	case "signal":
		return c.signalDesc
	case "rssi":
		return c.rssiDesc
	case "tx-mcs":
		return c.txMCSDesc
	case "tx-phy-rate":
		return c.txPHYRateDesc
	case "frequency":
		return c.frequencyDesc
	case "tx-sector":
		return c.txSectorDesc
	case "distance":
		return c.txDistanceDesc
	case "tx-packet-error-rate":
		return c.txPacketErrorRateDesc
	}

	return nil
}


File: /collector\wlanif_collector.go
package collector

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type wlanIFCollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newWlanIFCollector() routerOSCollector {
	c := &wlanIFCollector{}
	c.init()
	return c
}

func (c *wlanIFCollector) init() {
	c.props = []string{"channel", "registered-clients", "noise-floor", "overall-tx-ccq"}
	labelNames := []string{"name", "address", "interface", "channel"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props {
		c.descriptions[p] = descriptionForPropertyName("wlan_interface", p, labelNames)
	}
}

func (c *wlanIFCollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *wlanIFCollector) collect(ctx *collectorContext) error {
	names, err := c.fetchInterfaceNames(ctx)
	if err != nil {
		return err
	}

	for _, n := range names {
		err := c.collectForInterface(n, ctx)
		if err != nil {
			return err
		}
	}

	return nil
}

func (c *wlanIFCollector) fetchInterfaceNames(ctx *collectorContext) ([]string, error) {
	reply, err := ctx.client.Run("/interface/wireless/print", "?disabled=false", "=.proplist=name")
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching wireless interface names")
		return nil, err
	}

	names := []string{}
	for _, re := range reply.Re {
		names = append(names, re.Map["name"])
	}

	return names, nil
}

func (c *wlanIFCollector) collectForInterface(iface string, ctx *collectorContext) error {
	reply, err := ctx.client.Run("/interface/wireless/monitor", fmt.Sprintf("=numbers=%s", iface), "=once=", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"interface": iface,
			"device":    ctx.device.Name,
			"error":     err,
		}).Error("error fetching interface statistics")
		return err
	}

	for _, p := range c.props[1:] {
		// there's always going to be only one sentence in reply, as we
		// have to explicitly specify the interface
		c.collectMetricForProperty(p, iface, reply.Re[0], ctx)
	}

	return nil
}

func (c *wlanIFCollector) collectMetricForProperty(property, iface string, re *proto.Sentence, ctx *collectorContext) {
	desc := c.descriptions[property]
	channel := re.Map["channel"]
	if re.Map[property] == "" {
		return
	}
	v, err := strconv.ParseFloat(re.Map[property], 64)
	if err != nil {
		log.WithFields(log.Fields{
			"property":  property,
			"interface": iface,
			"device":    ctx.device.Name,
			"error":     err,
		}).Error("error parsing interface metric value")
		return
	}

	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, iface, channel)
}


File: /collector\wlansta_collector.go
package collector

import (
	"strconv"
	"strings"

	"github.com/prometheus/client_golang/prometheus"
	log "github.com/sirupsen/logrus"
	"gopkg.in/routeros.v2/proto"
)

type wlanSTACollector struct {
	props        []string
	descriptions map[string]*prometheus.Desc
}

func newWlanSTACollector() routerOSCollector {
	c := &wlanSTACollector{}
	c.init()
	return c
}

func (c *wlanSTACollector) init() {
	c.props = []string{"interface", "mac-address", "signal-to-noise", "signal-strength", "packets", "bytes", "frames"}
	labelNames := []string{"name", "address", "interface", "mac_address"}
	c.descriptions = make(map[string]*prometheus.Desc)
	for _, p := range c.props[:len(c.props)-3] {
		c.descriptions[p] = descriptionForPropertyName("wlan_station", p, labelNames)
	}
	for _, p := range c.props[len(c.props)-3:] {
		c.descriptions["tx_"+p] = descriptionForPropertyName("wlan_station", "tx_"+p, labelNames)
		c.descriptions["rx_"+p] = descriptionForPropertyName("wlan_station", "rx_"+p, labelNames)
	}
}

func (c *wlanSTACollector) describe(ch chan<- *prometheus.Desc) {
	for _, d := range c.descriptions {
		ch <- d
	}
}

func (c *wlanSTACollector) collect(ctx *collectorContext) error {
	stats, err := c.fetch(ctx)
	if err != nil {
		return err
	}

	for _, re := range stats {
		c.collectForStat(re, ctx)
	}

	return nil
}

func (c *wlanSTACollector) fetch(ctx *collectorContext) ([]*proto.Sentence, error) {
	reply, err := ctx.client.Run("/interface/wireless/registration-table/print", "=.proplist="+strings.Join(c.props, ","))
	if err != nil {
		log.WithFields(log.Fields{
			"device": ctx.device.Name,
			"error":  err,
		}).Error("error fetching wlan station metrics")
		return nil, err
	}

	return reply.Re, nil
}

func (c *wlanSTACollector) collectForStat(re *proto.Sentence, ctx *collectorContext) {
	iface := re.Map["interface"]
	mac := re.Map["mac-address"]

	for _, p := range c.props[2 : len(c.props)-3] {
		c.collectMetricForProperty(p, iface, mac, re, ctx)
	}
	for _, p := range c.props[len(c.props)-3:] {
		c.collectMetricForTXRXCounters(p, iface, mac, re, ctx)
	}
}

func (c *wlanSTACollector) collectMetricForProperty(property, iface, mac string, re *proto.Sentence, ctx *collectorContext) {
	if re.Map[property] == "" {
		return
	}
	p := re.Map[property]
	i := strings.Index(p, "@")
	if i > -1 {
		p = p[:i]
	}
	v, err := strconv.ParseFloat(p, 64)
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing wlan station metric value")
		return
	}

	desc := c.descriptions[property]
	ctx.ch <- prometheus.MustNewConstMetric(desc, prometheus.GaugeValue, v, ctx.device.Name, ctx.device.Address, iface, mac)
}

func (c *wlanSTACollector) collectMetricForTXRXCounters(property, iface, mac string, re *proto.Sentence, ctx *collectorContext) {
	tx, rx, err := splitStringToFloats(re.Map[property])
	if err != nil {
		log.WithFields(log.Fields{
			"device":   ctx.device.Name,
			"property": property,
			"value":    re.Map[property],
			"error":    err,
		}).Error("error parsing wlan station metric value")
		return
	}
	desc_tx := c.descriptions["tx_"+property]
	desc_rx := c.descriptions["rx_"+property]
	ctx.ch <- prometheus.MustNewConstMetric(desc_tx, prometheus.CounterValue, tx, ctx.device.Name, ctx.device.Address, iface, mac)
	ctx.ch <- prometheus.MustNewConstMetric(desc_rx, prometheus.CounterValue, rx, ctx.device.Name, ctx.device.Address, iface, mac)
}


File: /config\config.go
package config

import (
	"io"
	"io/ioutil"

	yaml "gopkg.in/yaml.v2"
)

// Config represents the configuration for the exporter
type Config struct {
	Devices  []Device `yaml:"devices"`
	Features struct {
		BGP       bool `yaml:"bgp,omitempty"`
		Conntrack bool `yaml:"conntrack,omitempty"`
		DHCP      bool `yaml:"dhcp,omitempty"`
		DHCPL     bool `yaml:"dhcpl,omitempty"`
		DHCPv6    bool `yaml:"dhcpv6,omitempty"`
		Firmware  bool `yaml:"firmware,omitempty"`
		Health    bool `yaml:"health,omitempty"`
		Routes    bool `yaml:"routes,omitempty"`
		POE       bool `yaml:"poe,omitempty"`
		Pools     bool `yaml:"pools,omitempty"`
		Optics    bool `yaml:"optics,omitempty"`
		W60G      bool `yaml:"w60g,omitempty"`
		WlanSTA   bool `yaml:"wlansta,omitempty"`
		Capsman   bool `yaml:"capsman,omitempty"`
		WlanIF    bool `yaml:"wlanif,omitempty"`
		Monitor   bool `yaml:"monitor,omitempty"`
		Ipsec     bool `yaml:"ipsec,omitempty"`
		Lte       bool `yaml:"lte,omitempty"`
		Netwatch  bool `yaml:"netwatch,omitempty"`
	} `yaml:"features,omitempty"`
}

// Device represents a target device
type Device struct {
	Name     string    `yaml:"name"`
	Address  string    `yaml:"address,omitempty"`
	Srv      SrvRecord `yaml:"srv,omitempty"`
	User     string    `yaml:"user"`
	Password string    `yaml:"password"`
	Port     string    `yaml:"port"`
}

type SrvRecord struct {
	Record string    `yaml:"record"`
	Dns    DnsServer `yaml:"dns,omitempty"`
}
type DnsServer struct {
	Address string `yaml:"address"`
	Port    int    `yaml:"port"`
}

// Load reads YAML from reader and unmashals in Config
func Load(r io.Reader) (*Config, error) {
	b, err := ioutil.ReadAll(r)
	if err != nil {
		return nil, err
	}

	c := &Config{}
	err = yaml.Unmarshal(b, c)
	if err != nil {
		return nil, err
	}

	return c, nil
}


File: /config\config.test.yml
devices:
  - name: test1
    address: 192.168.1.1
    user: foo
    password: bar
  - name: test2
    address: 192.168.2.1
    user: test
    password: 123

features:
  bgp: true
  conntrack: true
  dhcp: true
  dhcpv6: true
  dhcpl: true
  routes: true
  pools: true
  optics: true
  wlansta: true
  wlanif: true
  ipsec: true
  lte: true
  netwatch: true


File: /config\config_test.go
package config

import (
	"bytes"
	"io/ioutil"
	"testing"
)

func TestShouldParse(t *testing.T) {
	b := loadTestFile(t)
	c, err := Load(bytes.NewReader(b))
	if err != nil {
		t.Fatalf("could not parse: %v", err)
	}

	if len(c.Devices) != 2 {
		t.Fatalf("expected 2 devices, got %v", len(c.Devices))
	}

	assertDevice("test1", "192.168.1.1", "foo", "bar", c.Devices[0], t)
	assertDevice("test2", "192.168.2.1", "test", "123", c.Devices[1], t)
	assertFeature("BGP", c.Features.BGP, t)
	assertFeature("Conntrack", c.Features.Conntrack, t)
	assertFeature("DHCP", c.Features.DHCP, t)
	assertFeature("DHCPv6", c.Features.DHCPv6, t)
	assertFeature("Pools", c.Features.Pools, t)
	assertFeature("Routes", c.Features.Routes, t)
	assertFeature("Optics", c.Features.Optics, t)
	assertFeature("WlanSTA", c.Features.WlanSTA, t)
	assertFeature("WlanIF", c.Features.WlanIF, t)
	assertFeature("Ipsec", c.Features.Ipsec, t)
	assertFeature("Lte", c.Features.Lte, t)
	assertFeature("Netwatch", c.Features.Netwatch, t)
}

func loadTestFile(t *testing.T) []byte {
	b, err := ioutil.ReadFile("config.test.yml")
	if err != nil {
		t.Fatalf("could not load config: %v", err)
	}

	return b
}

func assertDevice(name, address, user, password string, c Device, t *testing.T) {
	if c.Name != name {
		t.Fatalf("expected name %s, got %s", name, c.Name)
	}

	if c.Address != address {
		t.Fatalf("expected address %s, got %s", address, c.Address)
	}

	if c.User != user {
		t.Fatalf("expected user %s, got %s", user, c.User)
	}

	if c.Password != password {
		t.Fatalf("expected password %s, got %s", password, c.Password)
	}
}

func assertFeature(name string, v bool, t *testing.T) {
	if !v {
		t.Fatalf("exprected feature %s to be enabled", name)
	}
}


File: /Dockerfile
FROM debian:9.9-slim

EXPOSE 9436

COPY scripts/start.sh /app/
COPY dist/mikrotik-exporter_linux_amd64 /app/mikrotik-exporter

RUN chmod 755 /app/*

ENTRYPOINT ["/app/start.sh"]

File: /Dockerfile.arm64
FROM arm64v8/busybox:1.31.0

EXPOSE 9090

COPY scripts/start.sh /app/
COPY dist/mikrotik-exporter_linux_arm64 /app/mikrotik-exporter

ENTRYPOINT ["/app/start.sh"]


File: /Dockerfile.armhf
FROM arm32v7/busybox:1.27.2

EXPOSE 9090

COPY scripts/start.sh /app/
COPY dist/mikrotik-exporter_linux_arm /app/mikrotik-exporter

RUN chmod 755 /app/*

ENTRYPOINT ["/app/start.sh"]

File: /examples\docker-compose\.env
CONFIG_FILE=/config/config.yml


File: /examples\docker-compose\docker-compose.yml
version: "3"

services:
  prom_mikrotik_exporter:
    image: nshttpd/mikrotik-exporter:1.0.11 # replace version for latest version
    volumes:
      - './config:/config'
    env_file: .env
    ports:
      - 9436:9436
    restart: unless-stopped


File: /examples\kubernetes\single-device\configmap.json
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata": {
    "name": "mikrotik-exporter",
    "namespace": "prometheus"
  },
  "data": {
    "device": "router",
    "address": "192.168.11.1",
    "user": "prometheus"
  }
}

File: /examples\kubernetes\single-device\deployment.json
{
  "apiVersion": "apps/v1beta1",
  "kind": "Deployment",
  "metadata": {
    "name": "mikrotik-exporter",
    "namespace": "prometheus"
  },
  "spec": {
    "replicas": 1,
    "revisionHistoryLimit": 5,
    "strategy": {
      "type": "Recreate"
    },
    "template": {
      "metadata": {
        "labels": {
          "app": "mikrotik-exporter"
        },
        "annotations": {
          "prometheus.io/scrape": "true",
          "prometheus.io/port": "9090"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "mikrotik-exporter",
            "image": "nshttpd/mikrotik-exporter:044419a",
            "env": [
              {
                "name": "DEVICE",
                "valueFrom": {
                  "configMapKeyRef": {
                    "name": "mikrotik-exporter",
                    "key": "device"
                  }
                }
              },
              {
                "name": "ADDRESS",
                "valueFrom": {
                  "configMapKeyRef": {
                    "name": "mikrotik-exporter",
                    "key": "address"
                  }
                }
              },
              {
                "name": "USER",
                "valueFrom": {
                  "configMapKeyRef": {
                    "name": "mikrotik-exporter",
                    "key": "user"
                  }
                }
              },
              {
                "name": "PASSWORD",
                "valueFrom": {
                  "secretKeyRef": {
                    "name" : "mikrotik-exporter",
                    "key" : "pasword"
                  }
                }
              }
            ]
          }
        ]
      }
    }
  }


}


File: /examples\kubernetes\single-device\secret.json
{
  "apiVersion": "v1",
  "kind": "Secret",
  "metadata": {
    "name": "mikrotik-exporter",
    "namespace": "prometheus"
  },
  "data": {
    "password": "Y2hhbmdlbWUK"
  }
}

File: /go.mod
module mikrotik-exporter

go 1.13

require (
	github.com/miekg/dns v1.1.43
	github.com/prometheus/client_golang v1.4.1
	github.com/prometheus/common v0.9.1
	github.com/sirupsen/logrus v1.8.1
	github.com/stretchr/testify v1.4.0
	golang.org/x/net v0.0.0-20210805182204-aaa1db679c0d // indirect
	golang.org/x/sys v0.0.0-20210809222454-d867a43fc93e // indirect
	gopkg.in/routeros.v2 v2.0.0-20190905230420-1bbf141cdd91
	gopkg.in/yaml.v2 v2.4.0
)


File: /go.sum
github.com/alecthomas/template v0.0.0-20160405071501-a0175ee3bccc/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/units v0.0.0-20151022065526-2efee857e7cf/go.mod h1:ybxpYRFXyAe+OPACYpWeL0wqObRcbAqCMya13uyzqw0=
github.com/alecthomas/units v0.0.0-20190717042225-c3de453c63f4/go.mod h1:ybxpYRFXyAe+OPACYpWeL0wqObRcbAqCMya13uyzqw0=
github.com/beorn7/perks v0.0.0-20180321164747-3a771d992973/go.mod h1:Dwedo/Wpr24TaqPxmxbtue+5NUziq4I4S80YR8gNf3Q=
github.com/beorn7/perks v1.0.0/go.mod h1:KWe93zE9D1o94FZ5RNwFwVgaQK1VOXiVxmqh+CedLV8=
github.com/beorn7/perks v1.0.1 h1:VlbKKnNfV8bJzeqoa4cOKqO6bYr3WgKZxO8Z16+hsOM=
github.com/beorn7/perks v1.0.1/go.mod h1:G2ZrVWU2WbWT9wwq4/hrbKbnv/1ERSJQ0ibhJ6rlkpw=
github.com/cespare/xxhash/v2 v2.1.1 h1:6MnRN8NT7+YBpUIWxHtefFZOKTAPgGjpQSxqLNn0+qY=
github.com/cespare/xxhash/v2 v2.1.1/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-kit/kit v0.8.0/go.mod h1:xBxKIO96dXMWWy0MnWVtmwkA9/13aqxPnvrjFYMA2as=
github.com/go-kit/kit v0.9.0/go.mod h1:xBxKIO96dXMWWy0MnWVtmwkA9/13aqxPnvrjFYMA2as=
github.com/go-logfmt/logfmt v0.3.0/go.mod h1:Qt1PoO58o5twSAckw1HlFXLmHsOX5/0LbT9GBnD5lWE=
github.com/go-logfmt/logfmt v0.4.0/go.mod h1:3RMwSq7FuexP4Kalkev3ejPJsZTpXXBr9+V4qmtdjCk=
github.com/go-stack/stack v1.8.0/go.mod h1:v0f6uXyyMGvRgIKkXu+yp6POWl0qKG85gN/melR3HDY=
github.com/gogo/protobuf v1.1.1/go.mod h1:r8qH/GZQm5c6nD/R0oafs1akxWv10x8SbQlK7atdtwQ=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.1/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.2 h1:6nsPYzhq5kReh6QImI3k5qWzO4PEbvbIW2cwSfR/6xs=
github.com/golang/protobuf v1.3.2/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.4.0 h1:xsAVV57WRhGj6kEIi8ReJzQlHHqcBYCElAvkovg3B/4=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/json-iterator/go v1.1.6/go.mod h1:+SdeFBvtyEkXs7REEP0seUULqWtbJapLOCVDaaPEHmU=
github.com/json-iterator/go v1.1.9/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/julienschmidt/httprouter v1.2.0/go.mod h1:SYymIcj16QtmaHHD7aYtjjsJG7VTCxuUUipMqKk8s4w=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/logfmt v0.0.0-20140226030751-b84e30acd515/go.mod h1:+0opPa2QZZtGFBFZlji/RkVcI2GknAs/DXo4wKdlNEc=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/matttproud/golang_protobuf_extensions v1.0.1 h1:4hp9jkHxhMHkqkrB3Ix0jegS5sx/RkqARlsWZ6pIwiU=
github.com/matttproud/golang_protobuf_extensions v1.0.1/go.mod h1:D8He9yQNgCq6Z5Ld7szi9bcBfOoFv/3dc6xSMkL2PC0=
github.com/miekg/dns v1.1.43 h1:JKfpVSCB84vrAmHzyrsxB5NAr5kLoMXZArPSw7Qlgyg=
github.com/miekg/dns v1.1.43/go.mod h1:+evo5L0630/F6ca/Z9+GAqzhjGyn8/c+TBaOyfEl0V4=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/modern-go/reflect2 v1.0.1/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/mwitkow/go-conntrack v0.0.0-20161129095857-cc309e4a2223/go.mod h1:qRWi+5nqEBWmkhHvq77mSJWrCKwh8bxhgT7d/eI7P4U=
github.com/pkg/errors v0.8.0/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/prometheus/client_golang v0.9.1/go.mod h1:7SWBe2y4D6OKWSNQJUaRYU/AaXPKyh/dDVn+NZz0KFw=
github.com/prometheus/client_golang v1.0.0/go.mod h1:db9x61etRT2tGnBNRi70OPL5FsnadC4Ky3P0J6CfImo=
github.com/prometheus/client_golang v1.4.1 h1:FFSuS004yOQEtDdTq+TAOLP5xUq63KqAFYyOi8zA+Y8=
github.com/prometheus/client_golang v1.4.1/go.mod h1:e9GMxYsXl05ICDXkRhurwBS4Q3OK1iX/F2sw+iXX5zU=
github.com/prometheus/client_model v0.0.0-20180712105110-5c3871d89910/go.mod h1:MbSGuTsp3dbXC40dX6PRTWyKYBIrTGTE9sqQNg2J8bo=
github.com/prometheus/client_model v0.0.0-20190129233127-fd36f4220a90/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
github.com/prometheus/client_model v0.2.0 h1:uq5h0d+GuxiXLJLNABMgp2qUWDPiLvgCzz2dUR+/W/M=
github.com/prometheus/client_model v0.2.0/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
github.com/prometheus/common v0.4.1/go.mod h1:TNfzLD0ON7rHzMJeJkieUDPYmFC7Snx/y86RQel1bk4=
github.com/prometheus/common v0.9.1 h1:KOMtN28tlbam3/7ZKEYKHhKoJZYYj3gMH4uc62x7X7U=
github.com/prometheus/common v0.9.1/go.mod h1:yhUN8i9wzaXS3w1O07YhxHEBxD+W35wd8bs7vj7HSQ4=
github.com/prometheus/procfs v0.0.0-20181005140218-185b4288413d/go.mod h1:c3At6R/oaqEKCNdg8wHV1ftS6bRYblBhIjjI8uT2IGk=
github.com/prometheus/procfs v0.0.2/go.mod h1:TjEm7ze935MbeOT/UhFTIMYKhuLP4wbCsTZCD3I8kEA=
github.com/prometheus/procfs v0.0.8 h1:+fpWZdT24pJBiqJdAwYBjPSk+5YmQzYNPYzQsdzLkt8=
github.com/prometheus/procfs v0.0.8/go.mod h1:7Qr8sr6344vo1JqZ6HhLceV9o3AJ1Ff+GxbHq6oeK9A=
github.com/sirupsen/logrus v1.2.0/go.mod h1:LxeOpSwHxABJmUn/MG1IvRgCAasNZTLOkJPxbbu5VWo=
github.com/sirupsen/logrus v1.4.2/go.mod h1:tLMulIdttU9McNUspp0xgXVQah82FyeX6MwdIuYE2rE=
github.com/sirupsen/logrus v1.8.1 h1:dJKuHgqk1NNQlqoA6BTlM1Wf9DOH3NBjQyu0h9+AZZE=
github.com/sirupsen/logrus v1.8.1/go.mod h1:yWOB1SBYBC5VeMP7gHvWumXLIWorT60ONWic61uBYv0=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
golang.org/x/crypto v0.0.0-20180904163835-0709b304e793/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/net v0.0.0-20181114220301-adae6a3d119a/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190613194153-d28f0bde5980/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210805182204-aaa1db679c0d h1:20cMwl2fHAzkJMEA+8J4JgqBQcQGzbisXo31MIeenXI=
golang.org/x/net v0.0.0-20210805182204-aaa1db679c0d/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/sync v0.0.0-20181108010431-42b317875d0f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181221193216-37e7f081c4d4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20210220032951-036812b2e83c h1:5KslGYwFpkhGh+Q16bwMP3cOontH8FOep7tGV86Y7SQ=
golang.org/x/sync v0.0.0-20210220032951-036812b2e83c/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180905080454-ebe1bf3edb33/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20181116152217-5ac8a444bdc5/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190422165155-953cdadca894/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191026070338-33540a1f6037/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200122134326-e047566fdf82/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210303074136-134d130e1a04/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210809222454-d867a43fc93e h1:WUoyKPm6nCo1BnNUvPGnFG3T5DUVem42yDJZZ4CNxMA=
golang.org/x/sys v0.0.0-20210809222454-d867a43fc93e/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15 h1:YR8cESwS4TdDjEe65xsg0ogRM/Nc3DYOhEAlW+xobZo=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/routeros.v2 v2.0.0-20190905230420-1bbf141cdd91 h1:RqTijcxlh3kwSEx4M1YfVoIBgA6rFO632PIOIjXAbz4=
gopkg.in/routeros.v2 v2.0.0-20190905230420-1bbf141cdd91/go.mod h1:dXYL5YdVb9GEWLoWK8VHdwL/SuFrNyb/hj2/CXZVT7E=
gopkg.in/yaml.v2 v2.2.1/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.5 h1:ymVxjfMaHvXD8RqPRmzHHsB3VvucivSkIAvJFDI5O3c=
gopkg.in/yaml.v2 v2.2.5/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=


File: /LICENSE
BSD 3-Clause License

Copyright (c) 2021, sbrunton at gmail dot com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
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

File: /main.go
package main

import (
	"bytes"
	"flag"
	"io/ioutil"
	"os"

	"github.com/prometheus/common/version"

	"fmt"
	"net/http"

	"mikrotik-exporter/collector"
	"mikrotik-exporter/config"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	log "github.com/sirupsen/logrus"
)

// single device can be defined via CLI flags, multiple via config file.
var (
	address     = flag.String("address", "", "address of the device to monitor")
	configFile  = flag.String("config-file", "", "config file to load")
	device      = flag.String("device", "", "single device to monitor")
	insecure    = flag.Bool("insecure", false, "skips verification of server certificate when using TLS (not recommended)")
	logFormat   = flag.String("log-format", "json", "logformat text or json (default json)")
	logLevel    = flag.String("log-level", "info", "log level")
	metricsPath = flag.String("path", "/metrics", "path to answer requests on")
	password    = flag.String("password", "", "password for authentication for single device")
	deviceport  = flag.String("deviceport", "8728", "port for single device")
	port        = flag.String("port", ":9436", "port number to listen on")
	timeout     = flag.Duration("timeout", collector.DefaultTimeout, "timeout when connecting to devices")
	tls         = flag.Bool("tls", false, "use tls to connect to routers")
	user        = flag.String("user", "", "user for authentication with single device")
	ver         = flag.Bool("version", false, "find the version of binary")

	withBgp       = flag.Bool("with-bgp", false, "retrieves BGP routing infrormation")
	withConntrack = flag.Bool("with-conntrack", false, "retrieves connection tracking metrics")
	withRoutes    = flag.Bool("with-routes", false, "retrieves routing table information")
	withDHCP      = flag.Bool("with-dhcp", false, "retrieves DHCP server metrics")
	withDHCPL     = flag.Bool("with-dhcpl", false, "retrieves DHCP server lease metrics")
	withDHCPv6    = flag.Bool("with-dhcpv6", false, "retrieves DHCPv6 server metrics")
	withFirmware  = flag.Bool("with-firmware", false, "retrieves firmware versions")
	withHealth    = flag.Bool("with-health", false, "retrieves board Health metrics")
	withPOE       = flag.Bool("with-poe", false, "retrieves PoE metrics")
	withPools     = flag.Bool("with-pools", false, "retrieves IP(v6) pool metrics")
	withOptics    = flag.Bool("with-optics", false, "retrieves optical diagnostic metrics")
	withW60G      = flag.Bool("with-w60g", false, "retrieves w60g interface metrics")
	withWlanSTA   = flag.Bool("with-wlansta", false, "retrieves connected wlan station metrics")
	withWlanIF    = flag.Bool("with-wlanif", false, "retrieves wlan interface metrics")
	withCapsman   = flag.Bool("with-capsman", false, "retrieves capsman station metrics")
	withMonitor   = flag.Bool("with-monitor", false, "retrieves ethernet interface monitor info")
	withIpsec     = flag.Bool("with-ipsec", false, "retrieves ipsec metrics")
	withLte       = flag.Bool("with-lte", false, "retrieves lte metrics")
	withNetwatch  = flag.Bool("with-netwatch", false, "retrieves netwatch metrics")

	cfg *config.Config

	appVersion = "DEVELOPMENT"
	shortSha   = "0xDEADBEEF"
)

func init() {
	prometheus.MustRegister(version.NewCollector("mikrotik_exporter"))
}

func main() {
	flag.Parse()

	if *ver {
		fmt.Printf("\nVersion:   %s\nShort SHA: %s\n\n", appVersion, shortSha)
		os.Exit(0)
	}

	configureLog()

	c, err := loadConfig()
	if err != nil {
		log.Errorf("Could not load config: %v", err)
		os.Exit(3)
	}
	cfg = c

	startServer()
}

func configureLog() {
	ll, err := log.ParseLevel(*logLevel)
	if err != nil {
		panic(err)
	}

	log.SetLevel(ll)

	if *logFormat == "text" {
		log.SetFormatter(&log.TextFormatter{})
	} else {
		log.SetFormatter(&log.JSONFormatter{})
	}
}

func loadConfig() (*config.Config, error) {
	if *configFile != "" {
		return loadConfigFromFile()
	}

	return loadConfigFromFlags()
}

func loadConfigFromFile() (*config.Config, error) {
	b, err := ioutil.ReadFile(*configFile)
	if err != nil {
		return nil, err
	}

	return config.Load(bytes.NewReader(b))
}

func loadConfigFromFlags() (*config.Config, error) {
	// Attempt to read credentials from env if not already defined
	if *user == "" {
		*user = os.Getenv("MIKROTIK_USER")
	}
	if *password == "" {
		*password = os.Getenv("MIKROTIK_PASSWORD")
	}
	if *device == "" || *address == "" || *user == "" || *password == "" {
		return nil, fmt.Errorf("missing required param for single device configuration")
	}

	return &config.Config{
		Devices: []config.Device{
			config.Device{
				Name:     *device,
				Address:  *address,
				User:     *user,
				Password: *password,
				Port:     *deviceport,
			},
		},
	}, nil
}

func startServer() {
	h, err := createMetricsHandler()
	if err != nil {
		log.Fatal(err)
	}
	http.Handle(*metricsPath, h)

	http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
		_, _ = w.Write([]byte("ok"))
	})

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		_, _ = w.Write([]byte(`<html>
			<head><title>Mikrotik Exporter</title></head>
			<body>
			<h1>Mikrotik Exporter</h1>
			<p><a href="` + *metricsPath + `">Metrics</a></p>
			</body>
			</html>`))
	})

	log.Info("Listening on ", *port)
	log.Fatal(http.ListenAndServe(*port, nil))
}

func createMetricsHandler() (http.Handler, error) {
	opts := collectorOptions()
	nc, err := collector.NewCollector(cfg, opts...)
	if err != nil {
		return nil, err
	}

	promhttp.Handler()

	registry := prometheus.NewRegistry()
	err = registry.Register(prometheus.NewGoCollector())
	if err != nil {
		return nil, err
	}
	err = registry.Register(nc)
	if err != nil {
		return nil, err
	}

	return promhttp.HandlerFor(registry,
		promhttp.HandlerOpts{
			ErrorLog:      log.New(),
			ErrorHandling: promhttp.ContinueOnError,
		}), nil
}

func collectorOptions() []collector.Option {
	opts := []collector.Option{}

	if *withBgp || cfg.Features.BGP {
		opts = append(opts, collector.WithBGP())
	}

	if *withRoutes || cfg.Features.Routes {
		opts = append(opts, collector.WithRoutes())
	}

	if *withDHCP || cfg.Features.DHCP {
		opts = append(opts, collector.WithDHCP())
	}

	if *withDHCPL || cfg.Features.DHCPL {
		opts = append(opts, collector.WithDHCPL())
	}

	if *withDHCPv6 || cfg.Features.DHCPv6 {
		opts = append(opts, collector.WithDHCPv6())
	}

	if *withFirmware || cfg.Features.Firmware {
		opts = append(opts, collector.WithFirmware())
	}

	if *withHealth || cfg.Features.Health {
		opts = append(opts, collector.WithHealth())
	}

	if *withPOE || cfg.Features.POE {
		opts = append(opts, collector.WithPOE())
	}

	if *withPools || cfg.Features.Pools {
		opts = append(opts, collector.WithPools())
	}

	if *withOptics || cfg.Features.Optics {
		opts = append(opts, collector.WithOptics())
	}

	if *withW60G || cfg.Features.W60G {
		opts = append(opts, collector.WithW60G())
	}

	if *withWlanSTA || cfg.Features.WlanSTA {
		opts = append(opts, collector.WithWlanSTA())
	}

	if *withCapsman || cfg.Features.Capsman {
		opts = append(opts, collector.WithCapsman())
	}

	if *withWlanIF || cfg.Features.WlanIF {
		opts = append(opts, collector.WithWlanIF())
	}

	if *withMonitor || cfg.Features.Monitor {
		opts = append(opts, collector.Monitor())

	}

	if *withIpsec || cfg.Features.Ipsec {
		opts = append(opts, collector.WithIpsec())
	}

	if *withConntrack || cfg.Features.Conntrack {
		opts = append(opts, collector.WithConntrack())
	}

	if *withLte || cfg.Features.Lte {
		opts = append(opts, collector.WithLte())
	}

	if *withNetwatch || cfg.Features.Netwatch {
		opts = append(opts, collector.WithNetwatch())
	}

	if *timeout != collector.DefaultTimeout {
		opts = append(opts, collector.WithTimeout(*timeout))
	}

	if *tls {
		opts = append(opts, collector.WithTLS(*insecure))
	}

	return opts
}


File: /MAINTAINERS.md
* Steve Brunton <sbrunton@gmail.com> @nshttpd

File: /Makefile
# go run -ldflags "-X mikrotik-exporter/cmd.version=6.6.7-BETA -X mikrotik-exporter/cmd.shortSha=`git rev-parse HEAD`" main.go version

VERSION=`cat VERSION`
SHORTSHA=`git rev-parse --short HEAD`

LDFLAGS=-X main.appVersion=$(VERSION)
LDFLAGS+=-X main.shortSha=$(SHORTSHA)

build:
	go build -ldflags "$(LDFLAGS)" .

utils:
	go get github.com/mitchellh/gox
	go get github.com/tcnksm/ghr

deploy: utils
	CGO_ENABLED=0 gox -os="linux freebsd netbsd" -arch="amd64 arm arm64 386" -parallel=4 -ldflags "$(LDFLAGS)" -output "dist/mikrotik-exporter_{{.OS}}_{{.Arch}}"
	@ghr -t $(GITHUB_TOKEN) -u $(CIRCLE_PROJECT_USERNAME) -r $(CIRCLE_PROJECT_REPONAME) -replace $(VERSION) dist/

dockerhub: deploy
	@docker login -u $(DOCKER_USER) -p $(DOCKER_PASS)
	docker build -t $(CIRCLE_PROJECT_USERNAME)/$(CIRCLE_PROJECT_REPONAME):$(VERSION) .
	docker push $(CIRCLE_PROJECT_USERNAME)/$(CIRCLE_PROJECT_REPONAME):$(VERSION)
	docker build -f Dockerfile.arm64 -t $(CIRCLE_PROJECT_USERNAME)/$(CIRCLE_PROJECT_REPONAME)-linux-arm64:$(VERSION) .
	docker push $(CIRCLE_PROJECT_USERNAME)/$(CIRCLE_PROJECT_REPONAME)-linux-arm64:$(VERSION)


File: /README.md
[![Docker Pulls](https://img.shields.io/docker/pulls/nshttpd/mikrotik-exporter.svg)](https://hub.docker.com/r/nshttpd/mikrotik-exporter/)

## prometheus-mikrotik

tl;dr - prometheus exporter for mikrotik devices

This is still a work in progress .. consider `master` at the moment as a preview
release.

#### Description

A Prometheus Exporter for Mikrotik devices. Can be configured to collect metrics
from a single device or multiple devices. Single device monitoring can be configured
all on the command line. Multiple devices require a configuration file. A user will
be required that has read-only access to the device configuration via the API.

Currently the exporter collects metrics for interfaces and system resources. Others
can be added as long as published via the API.

#### Mikrotik Config

Create a user on the device that has API and read-only access.

`/user group add name=prometheus policy=api,read,winbox`

If `lte` is enabled it requires also the `test` policy.

`/user group add name=prometheus policy=api,read,winbox,test`

Create the user to access the API via.

`/user add name=prometheus group=prometheus password=changeme`

#### Single Device

`./mikrotik-exporter -address 10.10.0.1 -device my_router -password changeme -user prometheus`

where `address` is the address of your router. `device` is the label name for the device
in the metrics output to prometheus. The `user` and `password` are the ones you
created for the exporter to use to access the API.

User and password flags can be set with the `MIKROTIK_USER` and `MIKROTIK_PASSWORD` environment variables, respectively.

```
MIKROTIK_USER=prometheus
MIKROTIK_PASSWORD=changeme
./mikrotik-exporter -address 10.10.0.1 -device my_router
```

#### Config File

`./mikrotik-exporter -config-file config.yml`

where `config-file` is the path to a config file in YAML format.

###### example config
```yaml
devices:
  - name: my_router
    address: 10.10.0.1
    user: prometheus
    password: changeme
  - name: my_second_router
    address: 10.10.0.2
    port: 8999
    user: prometheus2
    password: password_to_second_router
  - name: routers_srv_dns
    srv:
      record: _mikrotik._udp.example.com
    user: prometheus
    password: password_to_all_dns_routers
  - name: routers_srv_custom_dns
    srv:
      record: _mikrotik2._udp.example.com
      dns:
        address: 1.1.1.1
        port: 53
    user: prometheus
    password: password_to_all_dns_routers

features:
  bgp: true
  dhcp: true
  dhcpv6: true
  dhcpl: true
  routes: true
  pools: true
  optics: true
```

If you add a devices with the `srv` parameter instead of `address` the exporter will perform a DNS query
to obtain the SRV record and discover the devices dynamically. Also, you can specify a DNS server to use
on the query.


###### example output

```
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether2",name="my_router"} 1.4189902583e+10
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether3",name="my_router"} 2.263768666e+09
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether4",name="my_router"} 1.6572299e+08
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether5",name="my_router"} 1.66711315e+08
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether6",name="my_router"} 1.0026481337e+10
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether7",name="my_router"} 3.18354425e+08
mikrotik_interface_tx_byte{address="10.10.0.1",interface="ether8",name="my_router"} 1.86405031e+08
```

 


File: /scripts\build-armhf.sh
#!/bin/bash
set -e
set -x

DIR=`pwd`
NAME=`basename ${DIR}`
SHA=`git rev-parse --short HEAD`
VERSION=${VERSION:-$SHA}

GOOS=linux GOARCH=arm go build .

docker build -t nshttpd/${NAME}:${VERSION}-armhf -f Dockerfile.armhf .
docker push nshttpd/${NAME}:${VERSION}-armhf

rm mikrotik-exporter

File: /scripts\build.sh
#!/bin/bash
set -e
set -x

DIR=`pwd`
NAME=`basename ${DIR}`
SHA=`git rev-parse --short HEAD`
VERSION=${VERSION:-$SHA}

GOOS=linux GOARCH=amd64 go build .

docker build -t nshttpd/${NAME}:${VERSION} .
docker push nshttpd/${NAME}:${VERSION}

rm mikrotik-exporter

File: /scripts\start.sh
#!/bin/sh

if [ ! -x /app/mikrotik-exporter ]; then
  chmod 755 /app/mikrotik-exporter
fi

if [ -z "$CONFIG_FILE" ]
then
    /app/mikrotik-exporter -device $DEVICE -address $ADDRESS -user $USER -password $PASSWORD
else
    /app/mikrotik-exporter -config-file $CONFIG_FILE
fi


File: /VERSION
1.0.12-DEVEL


