# Repository Information
Name: mikrotik-openvpn-client

# Directory Structure
Directory structure:
└── github_repos/mikrotik-openvpn-client/
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
    │   │       ├── pack-f826791ab3a653996bf409020af4a9b926cb614a.idx
    │   │       └── pack-f826791ab3a653996bf409020af4a9b926cb614a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── FUNDING.yml
    ├── .gitignore
    ├── install.sh
    ├── README.md
    ├── task/
    │   ├── cert.install.sh
    │   ├── file.list.sh
    │   ├── header.sh
    │   ├── ovpn.setup.sh
    │   ├── pkg.install.sh
    │   ├── pkg.list.sh
    │   ├── pkg.ntp.configure.sh
    │   ├── reboot.sh
    │   ├── ssh.dsa.sh
    │   ├── ssh.ftp.sh
    │   ├── ssh.init.sh
    │   ├── ssh.sh
    │   └── sys.update.sh
    ├── util.sh
    └── _config.yml


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
	url = https://github.com/missinglink/mikrotik-openvpn-client.git
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
0000000000000000000000000000000000000000 5a8d8868cd5770c7c98a70adc9722c649b0f6e8f vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/missinglink/mikrotik-openvpn-client.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5a8d8868cd5770c7c98a70adc9722c649b0f6e8f vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/missinglink/mikrotik-openvpn-client.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5a8d8868cd5770c7c98a70adc9722c649b0f6e8f vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/missinglink/mikrotik-openvpn-client.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5a8d8868cd5770c7c98a70adc9722c649b0f6e8f refs/remotes/origin/master


File: /.git\refs\heads\master
5a8d8868cd5770c7c98a70adc9722c649b0f6e8f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\FUNDING.yml
# These are supported funding model platforms

github: [missinglink]


File: /.gitignore
cert/
packages/


File: /install.sh
#!/bin/bash

ADDR="192.168.88.1"
SSH_USER="admin"

source util.sh
source task/header.sh

# ssh-keygen -f "/home/$USER/.ssh/known_hosts" -R 192.168.88.1 &>/dev/null
healthcheck

# print installed packages
source "task/pkg.list.sh"; hr
# task "Update system packages" "task/pkg.update.sh"
# task "Install extra packages" "task/pkg.install.sh"
# task "Configure NTP client/server" "task/pkg.ntp.configure.sh"

task "Install certificates" "task/cert.install.sh"
task "Configure openvpn client" "task/ovpn.setup.sh"


File: /README.md
# Mikrotik router as OpenVPN Client

There are a bunch of tutorials online about how to set up a Mikrotik routerboard as an OpenVPN *server*; this is not one of them, this repository contains information and code samples for configuring a Mikrotik router as a *client* to connect to your own OpenVPN server hosted elsewhere.

As of Jun '16 this is confirmed working on a Mikrotik 951Ui-2HnD routerboard, all traffic destined for the internet is routed via the VPN connection and I'm able to watch region-locked video streaming services while connected through this wifi network.

## Gotchas!

Sourced from: http://wiki.mikrotik.com/wiki/OpenVPN

- TCP is supported **UDP is not supported** (ie. the default setup is not supported)
- username/passwords **are not mandatory**
- certificates are supported
- LZO compression **is not supported**

## Setting up the server

This info applies to you if you are setting up the server for yourself, otherwise you best check with your server admin that they have configured the server for a Mikrotik client.

For the most part I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04) for installing OpenVPN server on Ubuntu 14.04.

> Be careful with this tutorial, if you are using any services other than OpenVPN and SSH; or if you use non-standard ports, make sure you add the corresponding firewall rules!

I only made a couple changes to my `server.conf`:

##### Change protocols from UDP to TCP

```
# TCP or UDP server?
proto tcp
;proto udp
```

add the corresponding firewall rule:

```bash
sudo ufw allow 1194/tcp
```

##### Disable compression (optional)

This step is optional, if you're streaming video you can disable compression by commenting it out:

```
# comp-lzo
```

## Setting up the client

This section covers the steps required to set up your Mikrotik routerboard as an OpenVPN client.

##### Copy files from server

You'll need some files from your OpenVPN server or VPN provider, only 3 files are required:

```
$ ls cert/
ca.crt  client.crt  client.key
```

> If you're using the scripts in this repo then you'll need to create a directory called `cert` and put those files inside. You'll also need to rename your client keys to match the file names above.

##### Establish a SSH session

All the commands are executed by SSH so you'll need SSH access to your routerboard before continuing, otherwise I guess you could read the commands and enter them in the GUI, up to you.

```bash
ssh admin@192.168.88.1
```

```bash

MMM      MMM       KKK                          TTTTTTTTTTT      KKK
MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

MikroTik RouterOS 6.35.2 (c) 1999-2016       http://www.mikrotik.com/

[?]             Gives the list of available commands
command [?]     Gives help on the command and list of arguments

[Tab]           Completes the command/word. If the input is ambiguous,
              a second [Tab] gives possible options

/               Move up to base level
..              Move up one level
/command        Use command at the base level

[admin@MikroTik] >
```

> Great you connected! the interface is a bit weird, all commands start with a ``/`` and you use `?` for help within each section. If you didn't manage to connect you're going to need to sort that out before continuing or give up and use a GUI.

Type `/quit` in to the console to exit.

##### Check your OS version

All the code in this repo is hard-coded for version `6.35.2` (which was current at time of writing). If yours is older than that go ahead and upgrade first.

```bash
ssh admin@192.168.88.1 system package update download
```

##### Upload your certificates

You'll need to upload those certificates that we downloaded earlier on to your Mikrotik.

> you'll need to do this for all 3 files, see ./task/cert.install.sh for more info.

```bash
scp ca.crt admin@192.168.88.1:/
scp client.crt admin@192.168.88.1:/
scp client.key admin@192.168.88.1:/
```

```bash
ssh admin@192.168.88.1 certificate import file-name=ca.crt passphrase=\"\"
ssh admin@192.168.88.1 certificate import file-name=client.crt passphrase=\"\"
ssh admin@192.168.88.1 certificate import file-name=client.key passphrase=\"\"
```

We can confirm that worked:

```bash
ssh admin@192.168.88.1 certificate print
```

```bash
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted
 #          NAME                        COMMON-NAME                     SUBJECT-ALT-NAME                                                  FINGERPRINT                    
 0        T ca.crt_0                    Fort-Funston CA                                                                                   12911f9e101be5b3e15cd44e52cc...
 1 K      T client.crt_0                missinglink1                    DNS:missinglink1                                                  8bd36e8431eef6c52151c8400ef0...
```

##### Rename your certificates

This is optional; if this if your first time, best do this so you can follow the rest of the steps:

```bash
ssh admin@192.168.88.1 certificate set ca.crt_0 name=CA
```

```bash
ssh admin@192.168.88.1 certificate set client.crt_0 name=client
```

We can confirm that worked:

```bash
ssh admin@192.168.88.1 certificate print
```

##### Create a PPP profile

This section contains all the details of *how* you will connect to the server, the following worked for me, you may need to change some settings for your specific server configuration:

```bash
ssh admin@192.168.88.1 ppp profile add name=OVPN-client change-tcp-mss=yes only-one=yes use-encryption=required use-mpls=no
```

We can confirm that worked:

```bash
ssh admin@192.168.88.1 ppp profile print
```

```bash
Flags: * - default
 0 * name="default" remote-ipv6-prefix-pool=none use-ipv6=yes use-mpls=default
     use-compression=default use-encryption=default only-one=default
     change-tcp-mss=yes use-upnp=default address-list="" on-up="" on-down=""

 1   name="OVPN-client" remote-ipv6-prefix-pool=none use-ipv6=yes use-mpls=no
     use-compression=default use-encryption=required only-one=yes
     change-tcp-mss=yes use-upnp=default address-list="" on-up="" on-down=""

 2 * name="default-encryption" remote-ipv6-prefix-pool=none use-ipv6=yes
     use-mpls=default use-compression=default use-encryption=yes
     only-one=default change-tcp-mss=yes use-upnp=default address-list=""
     on-up="" on-down=""
```

##### Create an OpenVPN interface

Here we actually create an interface for the VPN connection:

> IMPORTANT!! Change xxx.xxx.xxx.xxx to your own server address (ip address or domain name).

```bash
ssh admin@192.168.88.1 interface ovpn-client add connect-to=xxx.xxx.xxx.xxx add-default-route=no auth=sha1 certificate=client disabled=no user=vpnuser password=vpnpass name=myvpn profile=OVPN-client
```

User/password properties seem to be mandatory on the client even if the server doesn't have `auth-user-pass-verify` enabled.


##### Test the VPN connection

If everything went according to plan you should now be connected:

```bash
ssh admin@192.168.88.1 interface ovpn-client print
```

Note the `'R'` which shows the connection has been established (give it a few seconds):

```bash
Flags: X - disabled, R - running
 0  R name="myvpn" mac-address=FE:EE:75:8F:14:3D max-mtu=1500
      connect-to=xxx.xxx.xxx.xxx port=1194 mode=ip user="vpnuser" password="vpnpass"
      profile=OVPN-client certificate=client auth=sha1 cipher=blowfish128
      add-default-route=no
```

```bash
ssh admin@192.168.88.1 interface ovpn-client monitor 0
```

```bash
status: connected
uptime: 1h35m45s
encoding: BF-128-CBC/SHA1
   mtu: 1500

status: connected
uptime: 1h35m46s
encoding: BF-128-CBC/SHA1
   mtu: 1500
```

##### Configure the firewall

This is explained [in this post](http://wiki.mikrotik.com/wiki/Policy_Base_Routing), basically we define some routes in our local network that **won't** go through the VPN (things in the 10.0.0.0, 172.16.0.0 & 192.168.0.0 ranges) and we add them to a list called `local_traffic`:

```bash
ssh admin@192.168.88.1 ip firewall address-list add address=10.0.0.0/8 disabled=no list=local_traffic
```

```bash
ssh admin@192.168.88.1 ip firewall address-list add address=172.16.0.0/12 disabled=no list=local_traffic
```

```bash
ssh admin@192.168.88.1 ip firewall address-list add address=192.168.0.0/16 disabled=no list=local_traffic
```

Then we set up a `'mangle'` rule which marks packets coming from the local network and destined for the internet with a mark named `vpn_traffic`:

```bash
ssh admin@192.168.88.1 ip firewall mangle add disabled=no action=mark-routing chain=prerouting dst-address-list=\!local_traffic new-routing-mark=vpn_traffic passthrough=yes src-address=192.168.88.2-192.168.88.254
```

##### Configure routing

Next we tell the router that all traffic with the `vpn_traffic` mark should go through the VPN interface:

```bash
ssh admin@192.168.88.1 ip route add disabled=no dst-address=0.0.0.0/0 type=unicast gateway=myvpn routing-mark=vpn_traffic scope=30 target-scope=10
```

##### Configure masquerade

And finally we add a masquerade NAT rule:

```bash
ssh admin@192.168.88.1 ip firewall nat add chain=srcnat src-address=192.168.88.0/24 out-interface=myvpn action=masquerade
```

## Finished!

That's it! your external traffic should now be routed through the VPN.

If this readme helped you out please star the repo; github stars are like crack cocaine to software developers :)

## Credits / Resources

Big thanks to all these people who wrote about this in the past.

- https://lukas.dzunko.sk/index.php/MikrotTik:_OpenVPN
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04

## License

```
This work ‘as-is’ we provide.
No warranty express or implied.
  We’ve done our best,
  to debug and test.
Liability for damages denied.

Permission is granted hereby,
to copy, share, and modify.
  Use as is fit,
  free or for profit.
These rights, on this notice, rely.
```


File: /task\cert.install.sh
#!/bin/bash

# install certificates from ./cert

echo "[info] installing certificates from ./cert"

if [[ -d "cert" ]]; then
  cd cert
  # copy files to routerboard
  for f in *
  do
  	ssh_push $f "/"
    echo "importing $f"
    ssh_eval "certificate import file-name=$f passphrase=\"\""
  done
  cd ..
else
  echo "[error] directory ./cert does not exist"
fi

# rename certs?
ssh_eval "certificate set ca.crt_0 name=CA"
ssh_eval "certificate set client.crt_0 name=client"


File: /task\file.list.sh
#!/bin/bash

# list files on root filesystem
ssh_eval "file print"


File: /task\header.sh

echo -e "\e[33m"
echo "===================================="
echo "=======    Mikrotik Setup    ======="
echo "===================================="
echo -e "\e[0m"


File: /task\ovpn.setup.sh
#!/bin/bash

# configure oopenvpn client
# https://lukas.dzunko.sk/index.php/MikrotTik:_OpenVPN
# http://wiki.mikrotik.com/wiki/OpenVPN#Unsupported
# http://freedommafia.net/clanmain/knowledges-management-42/mikrotik/317-mikrotik-router-openvpn-setup-os-6-0-or-newer

echo -n "Enter the address of your server (IP or domain) [ENTER]: "
read SERVER_ADDR

# you can find these with /certificate print (after uploading them)
CLIENT_CERT="client"
CONN_NAME="myvpn"
PPP_PROFILE="OVPN-client"

# create PPP profile
# http://wiki.mikrotik.com/wiki/Manual:PPP_AAA
ssh_eval "ppp profile remove $PPP_PROFILE" &>/dev/null
ssh_eval "ppp profile add \
change-tcp-mss=yes \
name=$PPP_PROFILE \
only-one=yes \
use-compression=default \
use-encryption=required \
use-mpls=no";

# http://wiki.mikrotik.com/wiki/Manual:Interface/OVPN
ssh_eval "interface ovpn-client remove $CONN_NAME" &>/dev/null
ssh_eval "interface ovpn-client add \
disabled=no \
add-default-route=no \
auth=sha1 \
certificate=$CLIENT_CERT \
connect-to=$SERVER_ADDR \
port=1194 \
user=vpnuser \
password=vpnpass \
name=$CONN_NAME \
profile=$PPP_PROFILE";

# http://wiki.mikrotik.com/wiki/Policy_Base_Routing
# http://wiki.mikrotik.com/wiki/Manual:IP/Firewall/Filter
echo "[info] adding firewall rules"
ssh_eval 'ip firewall address-list add address=10.0.0.0/8 disabled=no list=local_traffic'
ssh_eval 'ip firewall address-list add address=172.16.0.0/12 disabled=no list=local_traffic'
ssh_eval 'ip firewall address-list add address=192.168.0.0/16 disabled=no list=local_traffic'
ssh_eval 'ip firewall mangle add disabled=no action=mark-routing chain=prerouting dst-address-list=!local_traffic new-routing-mark=vpn_traffic passthrough=yes src-address=192.168.88.2-192.168.88.254'
ssh_eval 'ip route add disabled=no dst-address=0.0.0.0/0 type=unicast gateway=ukvpn routing-mark=vpn_traffic scope=30 target-scope=10'
ssh_eval 'ip firewall nat add chain=srcnat src-address=192.168.88.0/24 out-interface=ukvpn action=masquerade'

# monitor connection
ssh_eval 'interface ovpn-client monitor 0'


File: /task\pkg.install.sh
#!/bin/bash

# update all packages
# http://wiki.mikrotik.com/wiki/Manual:System/Packages
# https://www.mikrotik.com/documentation/manual_2.5/Basic/Packages.html

VERSION="6.35.2"
URL="http://download2.mikrotik.com/routeros/$VERSION/all_packages-mipsbe-$VERSION.zip"

echo "[info] downloading packages"
rm -r packages &>/dev/null; mkdir packages; cd packages
rm packages.zip 2>/dev/null
wget -q $URL -O packages.zip
unzip packages.zip; rm packages.zip

# copy files to routerboard
for f in *.npk
do
	ssh_push $f "/"
done

cd ..

task "Reboot", "task/reboot.sh"


File: /task\pkg.list.sh
#!/bin/bash

# list packages
ssh_eval "system package print"


File: /task\pkg.ntp.configure.sh
#!/bin/bash

# configure network time server (most boards don't contain a clock battery)
# this is useful for systems requiring exact time for certificates to work
# http://wiki.mikrotik.com/wiki/Setup_local_NTP_servers

TIMEZONE="CET"

ssh_eval "system ntp server set broadcast=no enabled=yes manycast=yes multicast=no"
ssh_eval "system ntp client set enabled=yes primary-ntp=1.2.3.4 secondary-ntp=5.6.7.8"
ssh_eval "system clock set time-zone-name=$TIMEZONE"

echo "ntp server enabled"
echo "[warning] timezone set to $TIMEZONE, you may need to reconfigure this setting"
echo

ssh_eval "system clock print"


File: /task\reboot.sh
#!/bin/bash

# reboot the box
ssh_eval "system reboot"
exit 1


File: /task\ssh.dsa.sh

# create a new DSA keypair
ssh-keygen -t dsa
chmod 600 ~/.ssh/id_dsa.pub


File: /task\ssh.ftp.sh
#!/bin/bash

# upload file via FTP
# http://wiki.mikrotik.com/wiki/Use_SSH_to_execute_commands_(DSA_key_login)

echo "Connecting to Mikrotik via FTP"
echo "[note] the default admin password is blank"

ftp -n <<EOF
open $ADDR
user admin
put ~/.ssh/id_dsa.pub
quit
EOF

echo
echo "Your public key has been uploaded to the Mikrotik"
echo "you must now use the web interface to open a terminal, enter:"
echo


File: /task\ssh.init.sh

# clear known_hosts
ssh-keygen -f "/home/$USER/.ssh/known_hosts" -R "$ADDR" &> /dev/null


File: /task\ssh.sh

if [ ! -f ~/.ssh/id_dsa.pub ]; then
  echo "[warning] required id_dsa.pub file not found!"
  task "Create one" "task/ssh.dsa.sh"
fi

task "Upload public key via FTP" "task/ssh.ftp.sh"


File: /task\sys.update.sh
#!/bin/bash

# check for system updates
ssh_eval "system package update check-for-updates"


File: /util.sh

ssh_eval(){
  hr; echo -e "[EXEC] $1\n"
  ssh "$SSH_USER@$ADDR" $1
  echo
}

ssh_push(){
  echo "[info] copy $PWD/$1 to $2$1 on remote filesystem"
  if [[ -d $1 ]]; then
    scp -r "$1" "$SSH_USER@$ADDR:$2"
  else
    scp "$1" "$SSH_USER@$ADDR:$2"
  fi
  echo
}

task(){
  read -p "$1? [y/n] " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    source $2
  fi
  echo
}

hr(){
  printf '\e[90m%*s\n\n\e[0m' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
}

healthcheck(){
  # echo "testing via ping..."
  # ping -q -c3 "$ADDR" > /dev/null
  #
  # if [ $? -ne 0 ]
  # then
  # 	echo "ping failed at: $ADDR"
  #   exit 1
  # fi

  echo "testing ssh access..."
  ssh -q "$SSH_USER@$ADDR" "exit"

  if [ $? -ne 0 ]
  then
  	echo "ssh failed for user $SSH_USER at: $ADDR"

    if [ $? -eq 255 ]
    then
      ssh "$SSH_USER@$ADDR" "exit"
    fi
    exit 1
  fi

  echo "[info] found host at: $ADDR"
  echo
  hr
  ssh_eval "system resource print"
  hr
}


File: /_config.yml
theme: jekyll-theme-tactile

