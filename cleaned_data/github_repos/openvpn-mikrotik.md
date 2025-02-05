# Repository Information
Name: openvpn-mikrotik

# Directory Structure
Directory structure:
└── github_repos/openvpn-mikrotik/
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
    │   │       ├── pack-b7c3cbcc257fd4d513f0ea58279aef2796ce5b42.idx
    │   │       └── pack-b7c3cbcc257fd4d513f0ea58279aef2796ce5b42.pack
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
    ├── bin/
    │   ├── easyrsa_vars
    │   ├── ovpn_copy_server_files
    │   ├── ovpn_genconfig
    │   ├── ovpn_getclient
    │   ├── ovpn_getclient_all
    │   ├── ovpn_initpki
    │   ├── ovpn_otp_user
    │   ├── ovpn_run
    │   ├── ovpn_staticip
    │   ├── ovpn_status
    │   └── ovpn_xml_getclient
    ├── Dockerfile
    ├── docs/
    │   ├── advanced.md
    │   ├── backup.md
    │   ├── clients.md
    │   ├── debug.md
    │   ├── docker-openvpn.te
    │   ├── docker.md
    │   ├── faqs.md
    │   ├── ipv6.md
    │   ├── otp.md
    │   ├── paranoid.md
    │   ├── selinux.md
    │   ├── static-ips.md
    │   └── tcp.md
    ├── init/
    │   ├── docker-openvpn@.service
    │   └── upstart.init
    ├── LICENSE
    ├── otp/
    │   └── openvpn
    ├── README.md
    └── tests/
        ├── basic.sh
        ├── client/
        │   └── wait-for-connect.sh
        ├── otp.sh
        └── paranoid.sh


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
	url = https://github.com/AlexBeznos/openvpn-mikrotik.git
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
0000000000000000000000000000000000000000 b68efc205c52b4c2db6231a5fa029fa4330d8aa4 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/AlexBeznos/openvpn-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b68efc205c52b4c2db6231a5fa029fa4330d8aa4 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/AlexBeznos/openvpn-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b68efc205c52b4c2db6231a5fa029fa4330d8aa4 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/AlexBeznos/openvpn-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b68efc205c52b4c2db6231a5fa029fa4330d8aa4 refs/remotes/origin/master


File: /.git\refs\heads\master
b68efc205c52b4c2db6231a5fa029fa4330d8aa4


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
*~


File: /.travis.yml
# Disallowing packages: openvpn
# If you require these packages, please review the package approval process at: https://github.com/travis-ci/apt-package-whitelist#package-approval-process
#addons:
#    apt:
#        sources:
#            - ubuntu-toolchain-r-test
#        packages:
#            - openvpn

services:
    - docker

before_install:
    - docker --version
    - docker build -t beznosa/openvpn-mikrotik .
    - docker inspect beznosa/openvpn-mikrotik
    - docker run beznosa/openvpn-mikrotik openvpn --version || true # why does it returns 1?
    - docker run beznosa/openvpn-mikrotik openssl version

script:
    - pushd tests && for i in *.sh; do "./$i"; done && popd


File: /bin\easyrsa_vars
#!/bin/sh

#
# Import/export EasyRSA default settings
#

if [ "$DEBUG" == "1" ]; then
  set -x
fi

set -e

if [ $# -lt 1 ]; then
    echo "No command provided"
    echo
    echo "$0 export > /path/to/file"
    echo "$0 import < /path/to/file"
    exit 1
fi

cmd=$1
shift

case "$cmd" in
    export)
        if [ -f "$EASYRSA_VARS_FILE" ]; then
            cat "$EASYRSA_VARS_FILE"
        else
            cat "$EASYRSA/vars.example"
        fi
        ;;
    import)
        cat > "$EASYRSA_VARS_FILE"
        ;;
    *)
        echo "Unknown cmd \"$cmd\""
        exit 2
        ;;
esac


File: /bin\ovpn_copy_server_files
#!/bin/bash
## @licence MIT <http://opensource.org/licenses/MIT>
## @author Copyright (C) 2015 Robin Schneider <ypid@riseup.net>

set -e

if [ -z "$OPENVPN" ]; then
    export OPENVPN="$PWD"
fi
if ! source "$OPENVPN/ovpn_env.sh"; then
    echo "Could not source $OPENVPN/ovpn_env.sh."
    exit 1
fi

TARGET="$OPENVPN/server"
if [ -n "$1" ]; then
    TARGET="$1"
fi
mkdir -p "${TARGET}"

## Ensure that no other keys then the one for the server is present.
rm -rf "$TARGET/pki/private" "$TARGET/pki/issued"

FILES=(
    "openvpn.conf"
    "ovpn_env.sh"
    "pki/private/${OVPN_CN}.key"
    "pki/issued/${OVPN_CN}.crt"
    "pki/dh.pem"
    "pki/ta.key"
    "pki/ca.crt"
)

# rsync isn't available to keep size down
# cp --parents isn't in busybox version
# hack the directory structure with tar
tar cf - -C "${OPENVPN}" "${FILES[@]}" | tar xvf - -C "${TARGET}"

mkdir -p "$TARGET/ccd"

echo "Created the openvpn configuration for the server: $TARGET"


File: /bin\ovpn_genconfig
#!/bin/bash

#
# Generate OpenVPN configs
#

# Convert 1.2.3.4/24 -> 255.255.255.0
cidr2mask()
{
    local i
    local subnetmask=""
    local cidr=${1#*/}
    local full_octets=$(($cidr/8))
    local partial_octet=$(($cidr%8))

    for ((i=0;i<4;i+=1)); do
        if [ $i -lt $full_octets ]; then
            subnetmask+=255
        elif [ $i -eq $full_octets ]; then
            subnetmask+=$((256 - 2**(8-$partial_octet)))
        else
            subnetmask+=0
        fi
        [ $i -lt 3 ] && subnetmask+=.
    done
    echo $subnetmask
}

# Used often enough to justify a function
getroute() {
    echo ${1%/*} $(cidr2mask $1)
}

usage() {
    echo "usage: $0 [-d]"
    echo "                  -u SERVER_PUBLIC_URL"
    echo "                 [-s SERVER_SUBNET]"
    echo "                 [-r ROUTE ...]"
    echo "                 [-p PUSH ...]"
    echo "                 [-n DNS_SERVER ...]"
    echo
    echo "optional arguments:"
    echo " -d    Disable NAT routing and default route"
    echo " -c    Enable client-to-client option"
    echo " -D    Do not push dns servers"
    echo " -N    Configure NAT to access external server network"
    echo " -m    Set client MTU"
    echo " -t    Use TAP device (instead of TUN device)"
    echo " -T    Encrypt packets with the given cipher algorithm instead of the default one (tls-cipher)."
    echo " -C    A list of allowable TLS ciphers delimited by a colon (cipher)."
    echo " -a    Authenticate  packets with HMAC using the given message digest algorithm (auth)."
    echo " -z    Enable comp-lzo compression."
    echo " -2    Enable two factor authentication using Google Authenticator."
}

if [ "$DEBUG" == "1" ]; then
  set -x
fi

set -e

OVPN_ENV=$OPENVPN/ovpn_env.sh
OVPN_SERVER=192.168.0.0/16
OVPN_DEFROUTE=1
OVPN_NAT=0
OVPN_DNS=1
OVPN_ROUTES=()
TMP_ROUTES=()
OVPN_PUSH=()
TMP_PUSH=()
OVPN_DNS_SERVERS=("8.8.8.8" "8.8.4.4")
TMP_DNS_SERVERS=()
OVPN_TLS_CIPHER=''
OVPN_AUTH=''

# Import defaults if present
[ -r "$OVPN_ENV" ] && source "$OVPN_ENV"

# Parse arguments
while getopts ":a:C:T:r:s:du:cp:n:DNm:tz2" opt; do
    case $opt in
        a)
            OVPN_AUTH="$OPTARG"
            ;;
        T)
            OVPN_TLS_CIPHER="$OPTARG"
            ;;
        r)
            TMP_ROUTES+=("$OPTARG")
            ;;
        s)
            OVPN_SERVER=$OPTARG
            ;;
        d)
            OVPN_DEFROUTE=0
            ;;
        u)
            OVPN_SERVER_URL=$OPTARG
            ;;
        p)
            TMP_PUSH+=("$OPTARG")
            ;;
        n)
            TMP_DNS_SERVERS+=("$OPTARG")
            ;;
        D)
            OVPN_DNS=0
            ;;
        N)
            OVPN_NAT=1
            ;;
        m)
            OVPN_MTU=$OPTARG
            ;;
        2)
            OVPN_OTP_AUTH=1
            ;;
        \?)
            set +x
            echo "Invalid option: -$OPTARG" >&2
            usage
            exit 1
            ;;
        :)
            set +x
            echo "Option -$OPTARG requires an argument." >&2
            usage
            exit 1
            ;;
    esac
done

# if new routes were not defined with -r, use default
[ ${#TMP_ROUTES[@]} -gt 0 ] && OVPN_ROUTES=("${TMP_ROUTES[@]}")

# if new push directives were not defined with -p, use default
[ ${#TMP_PUSH[@]} -gt 0 ] && OVPN_PUSH=("${TMP_PUSH[@]}")

# if dns servers were not defined with -n, use google nameservers
[ ${#TMP_DNS_SERVERS[@]} -gt 0 ] && OVPN_DNS_SERVERS=("${TMP_DNS_SERVERS[@]}")

# Server name is in the form "udp://vpn.example.com:1194"
if [[ "$OVPN_SERVER_URL" =~ ^((udp|tcp)://)?([0-9a-zA-Z\.\-]+)(:([0-9]+))?$ ]]; then
    OVPN_CN=${BASH_REMATCH[3]};
    OVPN_PORT=${BASH_REMATCH[5]};
else
    set +x
    echo "Common name not specified, see '-u'"
    usage
    exit 1
fi

# Apply defaults
[ -z "$OVPN_PORT" ] && OVPN_PORT=1194
[ ${#OVPN_ROUTES[@]} -eq 0 ] && OVPN_ROUTES=("192.168.254.0/24")

export OVPN_SERVER OVPN_ROUTES OVPN_DEFROUTE
export OVPN_SERVER_URL OVPN_ENV OVPN_CN OVPN_PORT
export OVPN_PUSH OVPN_NAT OVPN_DNS OVPN_MTU
export OVPN_TLS_CIPHER OVPN_AUTH
export OVPN_OTP_AUTH

# Preserve config
if [ -f "$OVPN_ENV" ]; then
    bak_env=$OVPN_ENV.$(date +%s).bak
    echo "Backing up $OVPN_ENV -> $bak_env"
    mv "$OVPN_ENV" "$bak_env"
fi
export | grep OVPN_ > "$OVPN_ENV"

conf=$OPENVPN/openvpn.conf
if [ -f "$conf" ]; then
    bak=$conf.$(date +%s).bak
    echo "Backing up $conf -> $bak"
    mv "$conf" "$bak"
fi

cat > "$conf" <<EOF
server $(getroute $OVPN_SERVER)
push "route $(getroute $OVPN_SERVER)"
verb 3
key $EASYRSA_PKI/private/${OVPN_CN}.key
ca $EASYRSA_PKI/ca.crt
cert $EASYRSA_PKI/issued/${OVPN_CN}.crt
dh $EASYRSA_PKI/dh.pem
tls-auth $EASYRSA_PKI/ta.key
keepalive 10 120
tun-mtu 1500
mssfix 1450
persist-key
persist-tun

# Mikrotik supports only tcp
proto tcp

# Rely on Docker to do port mapping, internally always 1194
port 1194
dev tun
File: /bin\ovpn_getclient
#!/bin/bash

#
# Get an OpenVPN client configuration file
#

if [ "$DEBUG" == "1" ]; then
    set -x
fi

set -e

if [ -z "$OPENVPN" ]; then
    export OPENVPN="$PWD"
fi
if ! source "$OPENVPN/ovpn_env.sh"; then
    echo "Could not source $OPENVPN/ovpn_env.sh."
    exit 1
fi
if [ -z "$EASYRSA_PKI" ]; then
    export EASYRSA_PKI="$OPENVPN/pki"
fi

cn="$1"
parm="$2"

if [ ! -f "$EASYRSA_PKI/private/${cn}.key" ]; then
    echo "Unable to find \"${cn}\", please try again or generate the key first" >&2
    exit 1
fi

get_client_config() {
    mode="$1"
    echo "
client
nobind
dev $OVPN_DEVICE
remote-cert-tls server

remote $OVPN_CN $OVPN_PORT $OVPN_PROTO
"
    if [ "$mode" == "combined" ]; then
        echo "
<key>
$(cat $EASYRSA_PKI/private/${cn}.key)
</key>
<cert>
$(openssl x509 -in $EASYRSA_PKI/issued/${cn}.crt)
</cert>
<ca>
$(cat $EASYRSA_PKI/ca.crt)
</ca>
<tls-auth>
$(cat $EASYRSA_PKI/ta.key)
</tls-auth>
key-direction 1
"
    elif [ "$mode" == "separated" ]; then
        echo "
key ${cn}.key
ca ca.crt
cert ${cn}.crt
tls-auth ta.key 1
$OVPN_ADDITIONAL_CLIENT_CONFIG
"
    fi

    if [ "$OVPN_DEFROUTE" != "0" ];then
        echo "redirect-gateway def1"
    fi

    if [ -n "$OVPN_MTU" ]; then
        echo "tun-mtu $OVPN_MTU"
    fi

    if [ -n "$OVPN_TLS_CIPHER" ]; then
        echo "tls-cipher $OVPN_TLS_CIPHER"
    fi

    if [ -n "$OVPN_CIPHER" ]; then
        echo "cipher $OVPN_CIPHER"
    fi

    if [ -n "$OVPN_AUTH" ]; then
        echo "auth $OVPN_AUTH"
    fi

    if [ -n "$OVPN_OTP_AUTH" ]; then
        echo "auth-user-pass"
        echo "auth-nocache"
    fi

    if [ -n "$OVPN_COMP_LZO" ]; then
        echo "comp-lzo"
    fi
}

dir="$OPENVPN/clients/$cn"
case "$parm" in
    "separated")
        mkdir -p "$dir"
        get_client_config "$parm" > "$dir/${cn}.ovpn"
        cp "$EASYRSA_PKI/private/${cn}.key" "$dir/${cn}.key"
        cp "$EASYRSA_PKI/ca.crt" "$dir/ca.crt"
        cp "$EASYRSA_PKI/issued/${cn}.crt" "$dir/${cn}.crt"
        cp "$EASYRSA_PKI/ta.key" "$dir/ta.key"
        ;;
    "" | "combined")
        get_client_config "combined"
        ;;
    "combined-save")
        get_client_config "combined" > "$dir/${cn}-combined.ovpn"
        ;;
    *)
        echo "This script can produce the client configuration in to formats:" >&2
        echo "    1. combined (default): All needed configuration and cryptographic material is in one file (Use \"combined-save\" to write the configuration file in the same path as the separated parameter does)." >&2
        echo "    2. separated: Separated files." >&2
        echo "Please specific one of those options as second parameter." >&2
        ;;
esac


File: /bin\ovpn_getclient_all
#!/bin/bash
## @licence MIT <http://opensource.org/licenses/MIT>
## @author Copyright (C) 2015 Robin Schneider <ypid@riseup.net>

if [ -z "$OPENVPN" ]; then
    export OPENVPN="$PWD"
fi
if ! source "$OPENVPN/ovpn_env.sh"; then
    echo "Could not source $OPENVPN/ovpn_env.sh."
    exit 1
fi
if [ -z "$EASYRSA_PKI" ]; then
    export EASYRSA_PKI="$OPENVPN/pki"
fi

pushd "$EASYRSA_PKI"
for name in issued/*.crt; do
    name=${name%.crt}
    name=${name#issued/}
    if [ "$name" != "$OVPN_CN" ]; then
        ovpn_getclient "$name" separated
        ovpn_getclient "$name" combined-save
    fi
done
popd


File: /bin\ovpn_initpki
#!/bin/bash

#
# Initialize the EasyRSA PKI
#

if [ "$DEBUG" == "1" ]; then
  set -x
fi

set -e

source "$OPENVPN/ovpn_env.sh"

# Specify "nopass" as arg[2] to make the CA insecure (not recommended!)
nopass=$1

# Provides a sufficient warning before erasing pre-existing files
easyrsa init-pki

# CA always has a password for protection in event server is compromised. The
# password is only needed to sign client/server certificates.  No password is
# needed for normal OpenVPN operation.
easyrsa build-ca $nopass

easyrsa gen-dh
openvpn --genkey --secret $OPENVPN/pki/ta.key

# Was nice to autoset, but probably a bad idea in practice, users should
# have to explicitly specify the common name of their server
#if [ -z "$cn"]; then
#    #TODO: Handle IPv6 (when I get a VPS with IPv6)...
#    ip4=$(dig +short myip.opendns.com @resolver1.opendns.com)
#    ptr=$(dig +short -x $ip4 | sed -e 's:\.$::')
#
#    [ -n "$ptr" ] && cn=$ptr || cn=$ip4
#fi

# For a server key with a password, manually init; this is autopilot
easyrsa build-server-full "$OVPN_CN" nopass


File: /bin\ovpn_otp_user
#!/bin/bash

#
# Generate OpenVPN users via google authenticator
#

if ! source "$OPENVPN/ovpn_env.sh"; then
    echo "Could not source $OPENVPN/ovpn_env.sh."
    exit 1
fi

if [ "x$OVPN_OTP_AUTH" != "x1" ]; then
    echo "OTP authentication not enabled, please regenerate configuration using -2 flag"
    exit 1
fi

if [ -z $1 ]; then
    echo "Usage: ovpn_otp_user USERNAME"
    exit 1
fi

# Ensure the otp folder is present
[ -d /etc/openvpn/otp ] || mkdir -p /etc/openvpn/otp

# Binary is present in image, save an $user.google_authenticator file in /etc/openvpn/otp
if [ "$2" == "interactive" ]; then
    # Authenticator will ask for other parameters. User can choose rate limit, token reuse policy and time window policy
    # Always use time base OTP otherwise storage for counters must be configured somewhere in volume
    google-authenticator --time-based --force -l "${1}@${OVPN_CN}" -s /etc/openvpn/otp/${1}.google_authenticator
else
    google-authenticator --time-based --disallow-reuse --force --rate-limit=3 --rate-time=30 --window-size=3 \
        -l "${1}@${OVPN_CN}" -s /etc/openvpn/otp/${1}.google_authenticator
fi

File: /bin\ovpn_run
#!/bin/bash

#
# Run the OpenVPN server normally
#

if [ "$DEBUG" == "1" ]; then
  set -x
fi

set -e

# Build runtime arguments array based on environment
ARGS=("--config" "$OPENVPN/openvpn.conf")

source "$OPENVPN/ovpn_env.sh"

mkdir -p /etc/openvpn/ccd
mkdir -p /dev/net
if [ ! -c /dev/net/tun ]; then
    mknod /dev/net/tun c 10 200
fi

if [ -d "$OPENVPN/ccd" ]; then
    ARGS+=("--client-config-dir" "$OPENVPN/ccd")
fi

# When using --net=host, use this to specify nat device.
[ -z "$OVPN_NATDEVICE" ] && OVPN_NATDEVICE=eth0

# Setup NAT forwarding if requested
if [ "$OVPN_DEFROUTE" != "0" ] || [ "$OVPN_NAT" == "1" ] ; then
    iptables -t nat -C POSTROUTING -s $OVPN_SERVER -o $OVPN_NATDEVICE -j MASQUERADE || {
      iptables -t nat -A POSTROUTING -s $OVPN_SERVER -o $OVPN_NATDEVICE -j MASQUERADE
    }
    for i in "${OVPN_ROUTES[@]}"; do
        iptables -t nat -C POSTROUTING -s "$i" -o $OVPN_NATDEVICE -j MASQUERADE || {
          iptables -t nat -A POSTROUTING -s "$i" -o $OVPN_NATDEVICE -j MASQUERADE
        }
    done
fi

# Use a hacky hardlink as the CRL Needs to be readable by the user/group
# OpenVPN is running as.  Only pass arguments to OpenVPN if it's found.
if [ -r "$EASYRSA_PKI/crl.pem" ]; then
    if [ ! -r "$OPENVPN/crl.pem" ]; then
        ln "$EASYRSA_PKI/crl.pem" "$OPENVPN/crl.pem"
        chmod 644 "$OPENVPN/crl.pem"
    fi
    ARGS+=("--crl-verify" "$OPENVPN/crl.pem")
fi

ip -6 route show default 2>/dev/null
if [ $? = 0 ]; then
    echo "Enabling IPv6 Forwarding"
    # If this fails, ensure the docker container is run with --privileged
    # Could be side stepped with `ip netns` madness to drop privileged flag

    sysctl -w net.ipv6.conf.default.forwarding=1 || echo "Failed to enable IPv6 Forwarding default"
    sysctl -w net.ipv6.conf.all.forwarding=1 || echo "Failed to enable IPv6 Forwarding"
fi

if [ "$#" -gt 0 ]; then
    exec openvpn "$@"
else
    exec openvpn ${ARGS[@]}
fi


File: /bin\ovpn_staticip
#!/bin/bash

#
# Push static ip for client
#

client="$1"
ip="$2"

echo "ifconfig-push $ip 192.168.0.0" >> "$OPENVPN/ccd/$client"


File: /bin\ovpn_status
#!/bin/sh

#
# Get OpenVPN server status
#
if [ "$DEBUG" == "1" ]; then
  set -x
fi

set -e

File: /bin\ovpn_xml_getclient
#!/bin/bash

#
# Get an OpenVPN client configuration file
#

if [ "$DEBUG" == "1" ]; then
    set -x
fi

set -e

if [ -z "$OPENVPN" ]; then
    export OPENVPN="$PWD"
fi
if ! source "$OPENVPN/ovpn_env.sh"; then
    echo "Could not source $OPENVPN/ovpn_env.sh."
    exit 1
fi
if [ -z "$EASYRSA_PKI" ]; then
    export EASYRSA_PKI="$OPENVPN/pki"
fi

cn="$1"
parm="$2"

if [ ! -f "$EASYRSA_PKI/private/${cn}.key" ]; then
    echo "Unable to find \"${cn}\", please try again or generate the key first" >&2
    exit 1
fi

get_client_config() {
    mode="$1"
    echo "
<root>
<key>
$(cat $EASYRSA_PKI/private/${cn}.key)
</key>
<cert>
$(openssl x509 -in $EASYRSA_PKI/issued/${cn}.crt)
</cert>
<ca>
$(cat $EASYRSA_PKI/ca.crt)
</ca>
<root>
"
}

dir="$OPENVPN/clients/$cn"

get_client_config


File: /Dockerfile
# Original credit: https://github.com/jpetazzo/dockvpn

# Smallest base image
FROM alpine:3.2

MAINTAINER Alex Beznos <beznosa@yahoo.com>

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update openvpn iptables bash easy-rsa openvpn-auth-pam google-authenticator pamtester && \
    ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

# Needed by scripts
ENV OPENVPN /etc/openvpn
ENV EASYRSA /usr/share/easy-rsa
ENV EASYRSA_PKI $OPENVPN/pki
ENV EASYRSA_VARS_FILE $OPENVPN/vars

VOLUME ["/etc/openvpn"]

# Internally uses port 1194/udp, remap using `docker run -p 443:1194/tcp`
EXPOSE 443:1194/tcp

WORKDIR /etc/openvpn

CMD ["ovpn_run"]

COPY ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

# Add support for OTP authentication using a PAM module
COPY ./otp/openvpn /etc/pam.d/


File: /docs\advanced.md
# Advanced Configurations

The [`ovpn_genconfig`](/bin/ovpn_genconfig) script is intended for simple configurations that apply to the majority of the users.  If your use case isn't general, it likely won't be supported.  This document aims to explain how to work around that.

## Create host volume mounts rather than data volumes

* Refer to the Quick Start document, and substitute `--volumes-from $OVPN_DATA` with `-v /path/on/host/openvpn0:/etc/openvpn`
* Quick example that is likely to be out of date, but here's how to get started:

        mkdir openvpn0
        cd openvpn0
        docker run --rm -v $PWD:/etc/openvpn beznosa/openvpn-mikrotik ovpn_genconfig -u tcp://VPN.SERVERNAME.COM:443
        docker run --rm -v $PWD:/etc/openvpn -it beznosa/openvpn-mikrotik ovpn_initpki
        vim openvpn.conf
        docker run --rm -v $PWD:/etc/openvpn -it beznosa/openvpn-mikrotik easyrsa build-client-full CLIENTNAME nopass
        docker run --rm -v $PWD:/etc/openvpn beznosa/openvpn-mikrotik ovpn_getclient CLIENTNAME > CLIENTNAME.ovpn

* Start the server with:

        docker run -v $PWD:/etc/openvpn -d -p 443:1194/tcp --privileged beznosa/openvpn-mikrotik


File: /docs\backup.md
# Backing Up Configuration and Certificates

## Security

The resulting archive from this backup contains all credential to impersonate the server at a minimum.  If the client's private keys are generated using the EasyRSA utility then it also contains the client certificates that could be used to impersonate said clients.  Most importantly, if the certificate authority key is in this archive (as it is given the quick start directions), then a adversary could generate certificates at will.

I'd recommend encrypting the archive with something strong (e.g. gpg or openssl + AES).  For the paranoid keep backup offline.  For the [truly paranoid users](/docs/paranoid.md), never keep any keys (i.e. client and certificate authority) in the docker container to begin with :).


**TL;DR Protect the resulting archive file.  Ensure there is very limited access to it.**

## Backup to Archive

    docker run --volumes-from $OVPN_DATA --rm busybox tar -cvf - -C /etc openvpn | xz > openvpn-backup.tar.xz

## Restore to New Container

Assumes an existing container named `$OVPN_DATA` to extract the data over the top.

    xzcat openvpn-backup.tar.xz | docker run --name $OVPN_DATA -v /etc/openvpn -i busybox tar -xvf - -C /etc


File: /docs\clients.md
# Advanced Client Management

## Client Configuration Mode

The [`ovpn_getclient`](/bin/ovpn_getclient) can produce two different versions of the configuration.

1. combined (default): All needed configuration and cryptographic material is in one file (Use "combined-save" to write the configuration file in the same path as the separated parameter does).
2. separated: Separated files.

Note that some client software might be picky about which configuration format it accepts.

## Batch Mode

If you have more than a few clients, you will want to generate and update your client configuration in batch. For this task the script [`ovpn_getclient_all`](/bin/ovpn_getclient_all) was written, which writes out the configuration for each client to a separate directory called `clients/$cn`.

Execute the following to generate the configuration for all clients:

    docker run --rm -it --volumes-from $OVPN_DATA --volume /tmp/openvpn_clients:/etc/openvpn/clients beznosa/openvpn-mikrotik ovpn_getclient_all

After doing so, you will find the following files in each of the `$cn` directories:

    ca.crt
    $cn-combined.ovpn # Combined configuration file format. If your client recognices this file then only this file is needed.
    $cn.ovpn          # Separated configuration. This configuration file requires the other files ca.crt dh.pem $cn.crt $cn.key ta.key
    $cn.crt
    $cn.key
    ta.key

## Revoking Client Certificates

Revoke `client1`'s certificate and generate the certificate revocation list (CRL):

    docker run --rm -it --volumes-from $OVPN_DATA beznosa/openvpn-mikrotik easyrsa revoke client1
    docker run --rm -it --volumes-from $OVPN_DATA beznosa/openvpn-mikrotik easyrsa gen-crl

The OpenVPN server will read this change every time a client connects (no need to restart server) and deny clients access using revoked certificates.


File: /docs\debug.md
# Debugging

Random things I do to debug the containers.

## Login Shells

* Create a shell in the running docker container (aka namespace) with [nsenter](https://github.com/jpetazzo/nsenter)
* If you don't have nsenter/docker-enter, you can mount the data container and modify it with

        docker run --rm -it --volumes-from $OVPN_DATA beznosa/openvpn-mikrotik bash -l

## Stream OpenVPN Logs

1. Get the container's name or container ID:

        root@vpn:~/docker-openvpn# docker ps
        CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS                    NAMES
        ed335aaa9b82        beznosa/openvpn-mikrotik:latest   ovpn_run            5 minutes ago       Up 5 minutes        0.0.0.0:1194->1194/udp   sad_lovelace

2. Tail the logs:

        root@vpn:~/docker-openvpn# docker logs -f sad_lovelace
        + mkdir -p /dev/net
        + [ ! -c /dev/net/tun ]
        + mknod /dev/net/tun c 10 200
        + [ ! -d /etc/openvpn/ccd ]
        + iptables -t nat -A POSTROUTING -s 192.168.254.0/24 -o eth0 -j MASQUERADE
        + iptables -t nat -A POSTROUTING -s 192.168.255.0/24 -o eth0 -j MASQUERADE
        + conf=/etc/openvpn/openvpn.conf
        + [ ! -s /etc/openvpn/openvpn.conf ]
        + conf=/etc/openvpn/udp1194.conf
        + openvpn --config /etc/openvpn/udp1194.conf
        Tue Jul  1 06:56:48 2014 OpenVPN 2.3.2 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [EPOLL] [PKCS11] [eurephia] [MH] [IPv6] built on Mar 17 2014
        Tue Jul  1 06:56:49 2014 Diffie-Hellman initialized with 2048 bit key
        Tue Jul  1 06:56:49 2014 Control Channel Authentication: using '/etc/openvpn/pki/ta.key' as a OpenVPN static key file
        Tue Jul  1 06:56:49 2014 Outgoing Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
        Tue Jul  1 06:56:49 2014 Incoming Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
        Tue Jul  1 06:56:49 2014 Socket Buffers: R=[212992->131072] S=[212992->131072]



File: /docs\docker-openvpn.te
module docker-openvpn 1.0;

require {
	type svirt_lxc_net_t;
	class tun_socket create;
}

#============= svirt_lxc_net_t ==============
allow svirt_lxc_net_t self:tun_socket create;



File: /docs\docker.md
# Install Latest Docker Service

Docker included with some distributions lags far behind upstream.  This guide aims to provide a quick and reliable way to install or update it.

It is recommended to use platforms that support systemd as future versions of this docker image may require systemd to help with some tasks:

* Fedora
* Debian 8.1+

## Debian / Ubuntu

### Step 1 — Set Up Docker

Docker is moving fast and Debian / Ubuntu's long term support (LTS) policy doesn't keep up. To work around this we'll install a PPA that will get us the latest version of Docker. For Debian Jessie users, just install docker.io from jessie-backports.

Ensure dependencies are installed:

    sudo apt-get update && sudo apt-get install -y apt-transport-https curl

Add the upstream Docker repository package signing key. The apt-key command uses elevated privileges via sudo, so a password prompt for the user's password may appear:

    curl -L https://get.docker.com/gpg | sudo apt-key add -

Add the upstream Docker repository to the system list:

    echo deb https://get.docker.io/ubuntu docker main | sudo tee /etc/apt/sources.list.d/docker.list

Update the package list and install the Docker package:

    sudo apt-get update && sudo apt-get install -y lxc-docker

Add your user to the `docker` group to enable communication with the Docker daemon as a normal user, where `$USER` is your username. Exit and log in again for the new group to take effect:

    sudo usermod -aG docker $USER

After **re-logging in** verify the group membership using the id command. The expected response should include docker like the following example:

    uid=1001(test0) gid=1001(test0) groups=1001(test0),27(sudo),999(docker)

### Step 2 — Test Docker

Run a Debian jessie docker container:

    docker run --rm -it debian:jessie bash -l

Once inside the container you'll see the `root@<container id>:/#` prompt signifying that the current shell is in a Docker container. To confirm that it's different from the host, check the version of Debian running in the container:

    cat /etc/issue.net

Expected result:

    Debian GNU/Linux 8


File: /docs\faqs.md
# Frequently Asked Questions

## How do I edit `openvpn.conf`?

Use a Docker image with a text editor pre-installed (i.e. Ubuntu) and connect the volume container:

    docker run --volumes-from $OVPN_DATA --rm -it ubuntu vi /etc/openvpn/openvpn.conf


## Why not keep everything in one image?

The run-time image (`beznosa/openvpn-mikrotik`) is intended to be an ephemeral image. Nothing should be saved in it so that it can be re-downloaded and re-run when updates are pushed (i.e. newer version of OpenVPN or even Debian). The data container contains all this data and is attached at run time providing a safe home.

If it was all in one container, an upgrade would require a few steps to extract all the data, perform some upgrade import, and re-run. This technique is also prone to people losing their EasyRSA PKI when they forget where it was.  With everything in the data container upgrading is as simple as re-running `docker pull beznosa/openvpn-mikrotik` and then `docker run ... beznosa/openvpn-mikrotik`.

## How do I set up a split tunnel?

Split tunnels are configurations where only some of the traffic from a client goes to the VPN, with the remainder routed through the normal non-VPN interfaces. You'll want to disable a default route (-d) when you generate the configuration, but still use NAT (-N) to keep network address translation enabled. 

    ovpn_genconfig -N -d ...


File: /docs\ipv6.md
# IPv6 Support

This is a work in progress, more polish to follow.

## Tunnel IPv6 Address To OpenVPN Clients

This feature is advanced and recommended only for those who already have a functioning IPv4 tunnel and know how IPv6 works.

Systemd is used to setup a static route and Debian 8.1 or later is recommended as the host distribution.  Others probably work, but haven't been tested.


### Step 1 — Setup IPv6 on the Host Machine

The tutorial uses a free tunnel from [tunnelbroker.net](https://tunnelbroker.net/) to get a /64 and /48 prefix allocated to me.  The tunnel endpoint is less then 3 ms away from Digital Ocean's San Francisco datacenter.

Place the following in `/etc/network/interfaces`.  Replace `PUBLIC_IP` with your host's public IPv4 address and replace 2001:db8::2 and 2001:db8::1 with the corresponding tunnel endpoints:

    auto he-ipv6
    iface he-ipv6 inet6 v4tunnel
        address 2001:db8::2
        netmask 64
        endpoint 72.52.104.74
        local PUBLIC_IP
        ttl 255
        gateway 2001:db8::1

Bring the interface up:

    ifup he-ipv6

Test that IPv6 works on the host:

    ping6 google.com

If this doesn't work, figure it out.  It may be necessary to add an firewall rule to allow IP protocol 41 through the firewall.


### Step 2 — Update Docker's Init To Enable IPv6 Support

Add the `--ipv6` to the Docker daemon invocation.

On **Ubuntu** and old versions of Debian Append the `--ipv6` argument to the `DOCKER_OPTS` variable in:

    /etc/default/docker

On modern **systemd** distributions copy the service file and modify it and reload the service:

    sed -e 's:^\(ExecStart.*\):\1 --ipv6:' /lib/systemd/system/docker.service | tee /etc/systemd/system/docker.service
    systemctl restart docker.service


### Step 3 — Setup the systemd Unit File

Copy the systemd init file from the docker-openvpn /init directory of the repository and install into `/etc/systemd/system/docker-openvpn.service`

    curl -o /etc/systemd/system/docker-openvpn@.service 'https://raw.githubusercontent.com/kylemanna/docker-openvpn/dev/init/docker-openvpn%40.service'

Edit the file, replace `IP6_PREFIX` value with the value of your /64 prefix.

    vi /etc/systemd/system/docker-openvpn@.service

Finally, reload systemd so the changes take affect:

    systemctl daemon-reload

### Step 4 — Start OpenVPN

Ensure that OpenVPN has been initialized and configured as described in the top level `README.md`.

Start the systemd service file specifying the volume container suffix as the instance.  For example, `INSTANCE=test0` has a docker volume container named `ovpn-data-test0` and service will create `ovpn-test0` container:

    systemctl start docker-openvpn@test0

Verify logs if needed:

    systemctl status docker-openvpn@test0
    docker logs ovpn-test0

### Step 4 — Modify Client Config for IPv6 Default Route

Append the default route for the public Internet:

    echo "route-ipv6 2000::/3" >> clientname.ovpn

### Step 5 — Start up Client

If all went according to plan, then `ping6 2600::` and `ping6 google.com` should work.

Fire up a web browser and attempt to navigate to [https://ipv6.google.com](https://ipv6.google.com).


## Connect to the OpenVPN Server Over IPv6

Not implemented, yet.


File: /docs\otp.md
# Using two factor authentication for users

Instead of relying on complex passwords for client certificates (that usually get written somewhere) this image
provides support for two factor authentication with OTP devices.

The most common app that provides OTP generation is Google Authenticator ([iOS](https://itunes.apple.com/it/app/google-authenticator/id388497605?mt=8) and
[Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=it)) you can download it
and use this image to generate user configuration.

## Usage

In order to enable two factor authentication the following steps are required.

* Generate server configuration with `-2` option

        docker run --volumes-from $OVPN_DATA --rm fabn/openvpn ovpn_genconfig -u udp://vpn.example.com -2

* Generate your client certificate (possibly without a password since you're using OTP)

        docker run --volumes-from $OVPN_DATA --rm -it fabn/openvpn easyrsa build-client-full <user> nopass

* Generate authentication configuration for your client. -t is needed to show QR code, -i is optional for interactive usage

        docker run --volumes-from $OVPN_DATA --rm -t fabn/openvpn ovpn_otp_user <user>

The last step will generate OTP configuration for the provided user with the following options

```
google-authenticator --time-based --disallow-reuse --force --rate-limit=3 --rate-time=30 --window-size=3 \
    -l "${1}@${OVPN_CN}" -s /etc/openvpn/otp/${1}.google_authenticator
```

It will also show a shell QR code in terminal you can scan with the Google Authenticator application. It also provides
a link to a google chart url that will display a QR code for the authentication.

**Do not share QR code (or generated url) with anyone but final user, that is your second factor for authentication
  that is used to generate OTP codes**

Here's an example QR code generated for an hypotetical user@example.com user.

![Example QR Code](https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/user@example.com%3Fsecret%3DKEYZ66YEXMXDHPH5)

Generate client configuration for `<user>` and import it in OpenVPN client. On connection it will prompt for user and password.
 Enter your username and a 6 digit code generated by Authenticator app and you're logged in.

## TL;DR

Under the hood this configuration will setup an `openvpn` PAM service configuration (`/etc/pam.d/openvpn`)
that relies on the awesome [Google Authenticator PAM module](https://github.com/google/google-authenticator).
In this configuration the `auth` part of PAM flow is managed by OTP codes and the `account` part is not enforced
 because you're likely dealing with virtual users and you do not want to create a system account for every VPN user.

`ovpn_otp_user` script will store OTP credentials under `/etc/openvpn/otp/<user>.google_authentication`. In this
 way when you take a backup OTP users are included as well.

Finally it will enable the openvpn plugin `openvpn-plugin-auth-pam.so` in server configuration and append the
`auth-user-pass` directive in client configuration.

## Debug

If something is not working you can verify your PAM setup with these commands

```
# Start a shell in container
docker run --volumes-from $OVPN_DATA --rm -it fabn/openvpn bash
# Then in container install pamtester utility
apt-get update && apt-get install -y pamtester
# To check authentication use this command that will prompt for a valid code from Authenticator APP
pamtester -v openvpn <user> authenticate
```

If you configured everything correctly you should get authenticated by entering a OTP code from the app.


File: /docs\paranoid.md
# Advanced security

## Keep the CA root key save
As mentioned in the [backup section](/docs/backup.md), there are good reasons to not generate the CA and/or leave it on the server. This document describes how you can generate the CA and all your certificates on a secure machine and then copy only the needed files (which never includes the CA root key obviously ;) ) to the server(s) and clients.

Execute the following commands. Note that you might want to change the volume `$PWD` or use a data docker container for this.

    docker run --net=none --rm -t -i -v $PWD:/etc/openvpn beznosa/openvpn-mikrotik ovpn_genconfig -u udp://VPN.SERVERNAME.COM
    docker run --net=none --rm -t -i -v $PWD:/etc/openvpn beznosa/openvpn-mikrotik ovpn_initpki
    docker run --net=none --rm -t -i -v $PWD:/etc/openvpn beznosa/openvpn-mikrotik ovpn_copy_server_files

The [`ovpn_copy_server_files`](/bin/ovpn_copy_server_files) script puts all the needed configuration in a subdirectory which defaults to `$OPENVPN/server`. All you need to do now is to copy this directory to the server and you are good to go.

## Crypto Hardening

If you want to select the cyphers used by OpenVPN the following parameters of the `ovpn_genconfig` might interest you:

    -T    Encrypt packets with the given cipher algorithm instead of the default one (tls-cipher).
    -C    A list of allowable TLS ciphers delimited by a colon (cipher).
    -a    Authenticate  packets with HMAC using the given message digest algorithm (auth).


The following options have been tested successfully:

    docker run --volumes-from $OVPN_DATA --net=none --rm beznosa/openvpn-mikrotik ovpn_genconfig -C 'AES-256-CBC' -a 'SHA384'

Changing the `tls-cipher` option seems to be more complicated because some clients (namely NetworkManager in Debian Jessie) seem to have trouble with this. Running `openvpn` manually also did not solve the issue:

    TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
    TLS Error: TLS handshake failed

Have a look at the [Applied-Crypto-Hardening](https://github.com/BetterCrypto/Applied-Crypto-Hardening/tree/master/src/configuration/VPNs/OpenVPN) project for more examples.


File: /docs\selinux.md
# For hosts that use SELinux

Try this [policy file](docker-openvpn.te)

Run these commands to compile and load it:

```
checkmodule -M -m -o docker-openvpn.mod docker-openvpn.te
semodule_package -o docker-openvpn.pp -m docker-openvpn.mod
sudo semodule -i docker-openvpn.pp
```

Also, some configurations don't allow containers to load kernel modules, so on the host run this:

```
sudo modprobe tun
```

So the container doesn't have to load the `tun` module.


# Still having issues?

In January 2016, Fedora based systems got an update that fixed an issue for labeling namespaced net objects under /proc
to fix, make sure that you have run `sudo dnf update` and you need to reboot to load the new policies


File: /docs\static-ips.md
# Static IP Addresses

The docker image is setup for static client configuration on the 192.168.254.0/24 subnet.  To use it follow the Quick Start section below.  Note that the IP addresses octets need to be picked special, see [OpenVPN Documentation](https://openvpn.net/index.php/open-source/documentation/howto.html#policy) for more details.

## Quick Start

1. Create a client specific configuration:

        $ docker run --volumes-from $OVPN_DATA --rm -it beznosa/openvpn-mikrotik ovpn_staticip CLIENTNAME CLIENTIP
        ifconfig-push 192.168.254.1 192.168.254.2

2. Wait for client to reconnect if necessary

## Advanced Admin

Login to the data volume with a `bash` container, note only changes in /etc/openvpn will persist:

    docker run --volumes-from $OVPN_DATA -it --rm beznosa/openvpn-mikrotik bash -l

## Upgrading from Old OpenVPN Configurations

If you're running an old configuration and need to upgrade it to pull in the ccd directory run the following:

    docker run  --volumes-from $OVPN_DATA --rm beznosa/openvpn-mikrotik ovpn_genconfig


File: /docs\tcp.md
# TCP Protocol

## TCP vs. UDP - Pros & Cons
By default, OpenVPN is configured to use the UDP protocol.  Because UDP incurs minimal protocol overhead (for example, no acknowledgment is required upon successful packet receipt), it can sometimes result in slightly faster throughput.  However, in situations where VPN service is needed over an unreliable connection, the user experience can benefit from the extra diagnostic features of the TCP protocol.

As an example, users connecting from an airplane wifi network may experience high packet drop rates, where the error detection and sliding window control of TCP can more readily adjust to the inconsistent connection.

## Using TCP
Those requiring TCP connections should initialize the data container by specifying the TCP protocol and port number:

    docker run --volumes-from $OVPN_DATA --rm beznosa/openvpn-mikrotik ovpn_genconfig -u tcp://VPN.SERVERNAME.COM:443
    docker run --volumes-from $OVPN_DATA --rm -it beznosa/openvpn-mikrotik ovpn_initpki

Because the server container always exposes port 1194, regardless of the
specified protocol, adjust the mapping appropriately:

    docker run --volumes-from $OVPN_DATA -d -p 443:1194/tcp --cap-add=NET_ADMIN beznosa/openvpn-mikrotik



File: /init\docker-openvpn@.service
[Unit]
Description=OpenVPN Docker Container
Documentation=https://github.com/kylemanna/docker-openvpn
After=network.target docker.socket
Requires=docker.socket

[Service]
RestartSec=10
Restart=always

# Modify IP6_PREFIX to match network config
#Environment="IP6_PREFIX=2001:db8::/64"
#Environment="ARGS=--config openvpn.conf --server-ipv6 2001:db8::/64"
Environment="NAME=ovpn-%i"
Environment="DATA_VOL=ovpn-data-%i"
Environment="IMG=beznosa/openvpn-mikrotik:latest"
Environment="PORT=1194:1194/udp"

# To override environment variables, use local configuration directory:
# /etc/systemd/system/docker-openvpn@foo.d/local.conf
# http://www.freedesktop.org/software/systemd/man/systemd.unit.html

# Clean-up bad state if still hanging around
ExecStartPre=-/usr/bin/docker rm -f $NAME

# Attempt to pull new image for security updates
ExecStartPre=-/usr/bin/docker pull $IMG

# IPv6: Ensure forwarding is enabled on host's networking stack (hacky)
# Would be nice to use systemd-network on the host, but this doens't work
# http://lists.freedesktop.org/archives/systemd-devel/2015-June/032762.html
ExecStartPre=/bin/sh -c 'test -z "$IP6_PREFIX" && exit 0; sysctl net.ipv6.conf.all.forwarding=1'

# Main process
ExecStart=/usr/bin/docker run --rm --privileged --volumes-from ${DATA_VOL}:ro --name ${NAME} -p ${PORT} ${IMG} ovpn_run $ARGS

# IPv6: Add static route for IPv6 after it starts up
ExecStartPost=/bin/sh -c 'test -z "${IP6_PREFIX}" && exit 0; sleep 1; ip route replace ${IP6_PREFIX} via $(docker inspect -f "{{ .NetworkSettings.GlobalIPv6Address }}" $NAME ) dev docker0'

# IPv6: Clean-up
ExecStopPost=/bin/sh -c 'test -z "$IP6_PREFIX" && exit 0; ip route del $IP6_PREFIX dev docker0'

[Install]
WantedBy=multi-user.target


File: /init\upstart.init
# Copy to /etc/init/docker-openvpn.conf
description "Docker container for OpenVPN server"
start on filesystem and started docker
stop on runlevel [!2345]
respawn
script
  exec docker run --volumes-from ovpn-data --rm -p 1194:1194/udp --cap-add=NET_ADMIN beznosa/openvpn-mikrotik
end script


File: /LICENSE
The MIT License (MIT)

Copyright (c) 2014 Kyle Manna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

File: /otp\openvpn
# Uses google authenticator library as PAM module using a single folder for all users tokens
# User root is required to stick with an hardcoded user when trying to determine user id and allow unexisting system users
# See https://github.com/google/google-authenticator/tree/master/libpam#secretpathtosecretfile--usersome-user
auth required pam_google_authenticator.so secret=/etc/openvpn/otp/${USER}.google_authenticator user=root

# Accept any user since we're dealing with virtual users there's no need to have a system account (pam_unix.so)
account sufficient pam_permit.so


File: /README.md
# OpenVPN for Docker

OpenVPN server in a Docker container complete with an EasyRSA PKI CA and setted up for using with mikrotik routers.

## Quick Start

* Create the `$OVPN_DATA` volume container, i.e. `OVPN_DATA="ovpn-data"`

        docker run --name $OVPN_DATA -v /etc/openvpn busybox

* Initialize the `$OVPN_DATA` container that will hold the configuration files and certificates

        docker run --volumes-from $OVPN_DATA --rm beznosa/openvpn-mikrotik ovpn_genconfig -u tcp://VPN.SERVERNAME.COM:443

        docker run --volumes-from $OVPN_DATA --rm -it beznosa/openvpn-mikrotik ovpn_initpki

* Start OpenVPN server process

    - On Docker [version 1.2](http://blog.docker.com/2014/08/announcing-docker-1-2-0/) and newer

      `docker run --volumes-from $OVPN_DATA -d -p 443:1194/tcp --cap-add=NET_ADMIN beznosa/openvpn-mikrotik`

    - On Docker older than version 1.2

      `docker run --volumes-from $OVPN_DATA -d -p 443:1194/tcp --privileged beznosa/openvpn-mikrotik`

* Generate a client certificate without a passphrase

        docker run --volumes-from $OVPN_DATA --rm -it beznosa/openvpn-mikrotik easyrsa build-client-full CLIENTNAME nopass

* Retrieve the client configuration with embedded certificates

        docker run --volumes-from $OVPN_DATA --rm beznosa/openvpn-mikrotik ovpn_getclient CLIENTNAME > CLIENTNAME.ovpn

* Create an environment variable with the name DEBUG and value of 1 to enable debug output (using "docker -e").
  `docker run --volumes-from $OVPN_DATA -d -p 443:1194/tcp --privileged -e DEBUG=1 beznosa/openvpn-mikrotik`

## How Does It Work?

Initialize the volume container using the `beznosa/openvpn-mikrotik` image with the
included scripts to automatically generate:

- Diffie-Hellman parameters
- a private key
- a self-certificate matching the private key for the OpenVPN server
- an EasyRSA CA key and certificate
- a TLS auth key from HMAC security

The OpenVPN server is started with the default run cmd of `ovpn_run`

The configuration is located in `/etc/openvpn`, and the Dockerfile
declares that directory as a volume. It means that you can start another
container with the `--volumes-from` flag, and access the configuration.
The volume also holds the PKI keys and certs so that it could be backed up.

To generate a client certificate, `beznosa/openvpn-mikrotik` uses EasyRSA via the
`easyrsa` command in the container's path.  The `EASYRSA_*` environmental
variables place the PKI CA under `/etc/opevpn/pki`.

Conveniently, `beznosa/openvpn-mikrotik` comes with a script called `ovpn_getclient`,
which dumps an inline OpenVPN client configuration file.  This single file can
then be given to a client for access to the VPN.

To enable Two Factor Authentication for clients (a.k.a. OTP) see [this document](/docs/otp.md).

## OpenVPN Details

We use `tun` mode, because it works on the widest range of devices.
`tap` mode, for instance, does not work on Android, except if the device
is rooted.

The topology used is `net30`, because it works on the widest range of OS.
`p2p`, for instance, does not work on Windows.

The UDP server uses`192.168.255.0/24` for dynamic clients by default.

The client profile specifies `redirect-gateway def1`, meaning that after
establishing the VPN connection, all traffic will go through the VPN.
This might cause problems if you use local DNS recursors which are not
directly reachable, since you will try to reach them through the VPN
and they might not answer to you. If that happens, use public DNS
resolvers like those of Google (8.8.4.4 and 8.8.8.8) or OpenDNS
(208.67.222.222 and 208.67.220.220).


## Security Discussion

The Docker container runs its own EasyRSA PKI Certificate Authority.  This was
chosen as a good way to compromise on security and convenience.  The container
runs under the assumption that the OpenVPN container is running on a secure
host, that is to say that an adversary does not have access to the PKI files
under `/etc/openvpn/pki`.  This is a fairly reasonable compromise because if an
adversary had access to these files, the adversary could manipulate the
function of the OpenVPN server itself (sniff packets, create a new PKI CA, MITM
packets, etc).

* The certificate authority key is kept in the container by default for
  simplicity.  It's highly recommended to secure the CA key with some
  passphrase to protect against a filesystem compromise.  A more secure system
  would put the EasyRSA PKI CA on an offline system (can use the same Docker
  image and the script [`ovpn_copy_server_files`](/docs/paranoid.md) to accomplish this).
* It would be impossible for an adversary to sign bad or forged certificates
  without first cracking the key's passphase should the adversary have root
  access to the filesystem.
* The EasyRSA `build-client-full` command will generate and leave keys on the
  server, again possible to compromise and steal the keys.  The keys generated
  need to be signed by the CA which the user hopefully configured with a passphrase
  as described above.
* Assuming the rest of the Docker container's filesystem is secure, TLS + PKI
  security should prevent any malicious host from using the VPN.


## Benefits of Running Inside a Docker Container

### The Entire Daemon and Dependencies are in the Docker Image

This means that it will function correctly (after Docker itself is setup) on
all distributions Linux distributions such as: Ubuntu, Arch, Debian, Fedora,
etc.  Furthermore, an old stable server can run a bleeding edge OpenVPN server
without having to install/muck with library dependencies (i.e. run latest
OpenVPN with latest OpenSSL on Ubuntu 12.04 LTS).

### It Doesn't Stomp All Over the Server's Filesystem

Everything for the Docker container is contained in two images: the ephemeral
run time image (beznosa/openvpn-mikrotik) and the data image (using busybox as a
base).  To remove it, remove the two Docker images and corresponding containers
and it's all gone.  This also makes it easier to run multiple servers since
each lives in the bubble of the container (of course multiple IPs or separate
ports are needed to communicate with the world).

### Some (arguable) Security Benefits

At the simplest level compromising the container may prevent additional
compromise of the server.  There are many arguments surrounding this, but the
take away is that it certainly makes it more difficult to break out of the
container.  People are actively working on Linux containers to make this more
of a guarantee in the future.

## Differences from jpetazzo/dockvpn

* No longer uses serveconfig to distribute the configuration via https
* Proper PKI support integrated into image
* OpenVPN config files, PKI keys and certs are stored on a storage
  volume for re-use across containers
* Addition of tls-auth for HMAC security

## Tested On

* Docker hosts:
  * server a [Digital Ocean](https://www.digitalocean.com/?refcode=d19f7fe88c94) Droplet with 512 MB RAM running Ubuntu 14.04
* Clients
  * Android App OpenVPN Connect 1.1.14 (built 56)
     * OpenVPN core 3.0 android armv7a thumb2 32-bit
  * OS X Mavericks with Tunnelblick 3.4beta26 (build 3828) using openvpn-2.3.4
  * ArchLinux OpenVPN pkg 2.3.4-1
  *

## Having permissions issues with Selinux enabled?

See [this](docs/selinux.md)


File: /tests\basic.sh
#!/bin/bash
set -ex
OVPN_DATA=basic-data
CLIENT=travis-client
IMG=beznosa/openvpn-mikrotik

#
# Create a docker container with the config data
#
docker run --name $OVPN_DATA -v /etc/openvpn busybox

ip addr ls
SERV_IP=$(ip -4 -o addr show scope global  | awk '{print $4}' | sed -e 's:/.*::' | head -n1)
docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_genconfig -u udp://$SERV_IP

# nopass is insecure
docker run --volumes-from $OVPN_DATA --rm -it -e "EASYRSA_BATCH=1" -e "EASYRSA_REQ_CN=Travis-CI Test CA" $IMG ovpn_initpki nopass

docker run --volumes-from $OVPN_DATA --rm -it $IMG easyrsa build-client-full $CLIENT nopass

docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_getclient $CLIENT | tee client/config.ovpn

#
# Fire up the server
#
sudo iptables -N DOCKER
sudo iptables -I FORWARD -j DOCKER
# run in shell bg to get logs
docker run --name "ovpn-test" --volumes-from $OVPN_DATA --rm -p 1194:1194/udp --privileged $IMG &

#for i in $(seq 10); do
#    SERV_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}')
#    test -n "$SERV_IP" && break
#done
#sed -ie s:SERV_IP:$SERV_IP:g client/config.ovpn

#
# Fire up a client in a container since openvpn is disallowed by Travis-CI, don't NAT
# the host as it confuses itself:
# "Incoming packet rejected from [AF_INET]172.17.42.1:1194[2], expected peer address: [AF_INET]10.240.118.86:1194"
#
docker run --rm --net=host --privileged --volume $PWD/client:/client $IMG /client/wait-for-connect.sh

#
# Client either connected or timed out, kill server
#
kill %1

#
# Celebrate
#
cat <<EOF
 ___________
< it worked >
 -----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
EOF


File: /tests\client\wait-for-connect.sh
#!/bin/bash
set -ex
OPENVPN_CONFIG=${1:-/client/config.ovpn}

# Run in background, rely on bash for job management
openvpn --config "$OPENVPN_CONFIG" --management 127.0.0.1 9999 &

# Spin waiting for interface to exist signifying connection
timeout=10
for i in $(seq $timeout); do

    # Break when connected
    #echo state | busybox nc 127.0.0.1 9999 | grep -q "CONNECTED,SUCCESS" && break;

    # Bash magic for tcp sockets
    if exec 3<>/dev/tcp/127.0.0.1/9999; then
        # Consume all header input
        while read -t 0.1 <&3; do true; done
        echo "state" >&3
        read -t 1 <&3
        echo -n $REPLY | grep -q "CONNECTED,SUCCESS" && break || true
        exec 3>&-
    fi

    # Else sleep
    sleep 1
done

if [ $i -ge $timeout ]; then
    echo "Error starting OpenVPN, i=$i, exiting."
    exit 2;
fi

# The show is over.
kill %1


File: /tests\otp.sh
#!/bin/bash
set -ex
OVPN_DATA=basic-data-otp
CLIENT=travis-client
IMG=beznosa/openvpn-mikrotik
OTP_USER=otp
# Function to fail
abort() { cat <<< "$@" 1>&2; exit 1; }

#
# Create a docker container with the config data
#
docker run --name $OVPN_DATA -v /etc/openvpn busybox

ip addr ls
SERV_IP=$(ip -4 -o addr show scope global  | awk '{print $4}' | sed -e 's:/.*::' | head -n1)
# Configure server with two factor authentication
docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_genconfig -u udp://$SERV_IP -2

# nopass is insecure
docker run --volumes-from $OVPN_DATA --rm -it -e "EASYRSA_BATCH=1" -e "EASYRSA_REQ_CN=Travis-CI Test CA" $IMG ovpn_initpki nopass

docker run --volumes-from $OVPN_DATA --rm -it $IMG easyrsa build-client-full $CLIENT nopass

# Generate OTP credentials for user named test, should return QR code for test user
docker run --volumes-from $OVPN_DATA --rm -it $IMG ovpn_otp_user $OTP_USER | tee client/qrcode.txt
# Ensure a chart link is printed in client OTP configuration
grep 'https://www.google.com/chart' client/qrcode.txt || abort 'Link to chart not generated'
grep 'Your new secret key is:' client/qrcode.txt || abort 'Secret key is missing'
# Extract an emergency code from textual output, grepping for line and trimming spaces
OTP_TOKEN=$(grep -A1 'Your emergency scratch codes are' client/qrcode.txt | tail -1 | tr -d '[[:space:]]')
# Token should be present
if [ -z $OTP_TOKEN ]; then
  abort "QR Emergency Code not detected"
fi

# Store authentication credentials in config file and tell openvpn to use them
echo -e "$OTP_USER\n$OTP_TOKEN" > client/credentials.txt

# Override the auth-user-pass directive to use a credentials file
docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_getclient $CLIENT | sed 's/auth-user-pass/auth-user-pass \/client\/credentials.txt/' | tee client/config.ovpn

#
# Fire up the server
#
sudo iptables -N DOCKER || echo 'Firewall already configured'
sudo iptables -I FORWARD -j DOCKER || echo 'Forward already configured'
# run in shell bg to get logs
docker run --name "ovpn-test" --volumes-from $OVPN_DATA --rm -p 1194:1194/udp --privileged $IMG &

#for i in $(seq 10); do
#    SERV_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}')
#    test -n "$SERV_IP" && break
#done
#sed -ie s:SERV_IP:$SERV_IP:g client/config.ovpn

#
# Fire up a client in a container since openvpn is disallowed by Travis-CI, don't NAT
# the host as it confuses itself:
# "Incoming packet rejected from [AF_INET]172.17.42.1:1194[2], expected peer address: [AF_INET]10.240.118.86:1194"
#
docker run --rm --net=host --privileged --volume $PWD/client:/client $IMG /client/wait-for-connect.sh

#
# Client either connected or timed out, kill server
#
kill %1

#
# Celebrate
#
cat <<EOF
 ___________
< it worked >
 -----------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
EOF


File: /tests\paranoid.sh
#!/bin/bash

set -ex

IMG=${IMG:-beznosa/openvpn-mikrotik}

temp=$(mktemp -d)

pushd $temp

SERV_IP=$(ip -4 -o addr show scope global  | awk '{print $4}' | sed -e 's:/.*::' | head -n1)

docker run --net=none --rm -t -i -v $PWD:/etc/openvpn $IMG ovpn_genconfig -u udp://$SERV_IP

docker run --net=none --rm -t -i -v $PWD:/etc/openvpn -e "EASYRSA_BATCH=1" -e "EASYRSA_REQ_CN=Travis-CI Test CA" beznosa/openvpn-mikrotik ovpn_initpki nopass

docker run --net=none --rm -t -i -v $PWD:/etc/openvpn $IMG ovpn_copy_server_files

popd
# Can't delete the temp directory as docker creates some files as root.
# Just let it die with the test instance.
rm -rf $temp || true


