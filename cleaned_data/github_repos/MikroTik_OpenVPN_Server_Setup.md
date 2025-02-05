# Repository Information
Name: MikroTik_OpenVPN_Server_Setup

# Directory Structure
Directory structure:
└── github_repos/MikroTik_OpenVPN_Server_Setup/
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
    │   │       ├── pack-686a35fcd6df77dc4e083d43aafd53ce946edeed.idx
    │   │       └── pack-686a35fcd6df77dc4e083d43aafd53ce946edeed.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── art/
    ├── create_config.sh
    ├── LICENSE
    ├── ovpn_clients.rsc
    ├── ovpn_server.rsc
    ├── README.md
    ├── sign_certs.sh
    └── template.ovpn


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
	url = https://github.com/ageapps/MikroTik_OpenVPN_Server_Setup.git
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
0000000000000000000000000000000000000000 b6fa795fe2387c954db53a4696b34b3b88483c95 vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/ageapps/MikroTik_OpenVPN_Server_Setup.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b6fa795fe2387c954db53a4696b34b3b88483c95 vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/ageapps/MikroTik_OpenVPN_Server_Setup.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b6fa795fe2387c954db53a4696b34b3b88483c95 vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/ageapps/MikroTik_OpenVPN_Server_Setup.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b6fa795fe2387c954db53a4696b34b3b88483c95 refs/remotes/origin/master


File: /.git\refs\heads\master
b6fa795fe2387c954db53a4696b34b3b88483c95


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
configs
certificates

File: /create_config.sh
#!/bin/bash

PUBLIC_ADDRESS="pihostadri.ddns.net" #YOUR PUBLIC IP OR ADDRESS
PUBLIC_PORT="1194" #YOUR PUBLIC PORT
PROTOCOL="tcp-client" #YOUR PROTOCOL udp/tcp-client

mkdir configs
for i in `seq 1 5`;
        do
                echo "Creating user $i dir..."
                mkdir configs/user$i
                echo "Copying user cert and key..."
                cp certificates/cert_export_user$i@CA.* configs/user$i
                cp certificates/cert_export_CA.crt configs/user$i

                echo "Creating user auth..."
                echo "user$i\nuser000$i" > configs/user$i/user.auth
                
                echo "Creating config file..."
                sed "s/{CLIENT}/user$i@CA/g; s/{PUBLIC_ADDRESS}/$PUBLIC_ADDRESS/g; s/{PUBLIC_PORT}/$PUBLIC_PORT/g; s/{PROTOCOL}/$PROTOCOL/g" template.ovpn > configs/user$i/user$i.ovpn
        done  


File: /LICENSE
MIT License

Copyright (c) 2018 Adrián García Espinosa

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


File: /ovpn_clients.rsc
:global CN "CA"
:global USERNAME "user1"
:global PASSWORD "user0001"

## add a user
/ppp secret add name=$USERNAME password=$PASSWORD profile=OVPN-PROFILE service=ovpn

## generate a client certificate
/certificate add name=client-template-to-issue copy-from="CLIENT-tpl" common-name="$USERNAME@$CN" 

/certificate sign client-template-to-issue ca="$CN" name="$USERNAME@$CN"
:delay 20
## client certificate, and private key
/certificate export-certificate "$USERNAME@$CN" export-passphrase="$PASSWORD"


:global USERNAME "user2"
:global PASSWORD "user0002"

## add a user
/ppp secret add name=$USERNAME password=$PASSWORD profile=OVPN-PROFILE service=ovpn

## generate a client certificate
/certificate add name=client-template-to-issue copy-from="CLIENT-tpl" common-name="$USERNAME@$CN" 

/certificate sign client-template-to-issue ca="$CN" name="$USERNAME@$CN"
:delay 20
## client certificate, and private key
/certificate export-certificate "$USERNAME@$CN" export-passphrase="$PASSWORD"

:global USERNAME "user3"
:global PASSWORD "user0003"

## add a user
/ppp secret add name=$USERNAME password=$PASSWORD profile=OVPN-PROFILE service=ovpn

## generate a client certificate
/certificate add name=client-template-to-issue copy-from="CLIENT-tpl" common-name="$USERNAME@$CN" 

/certificate sign client-template-to-issue ca="$CN" name="$USERNAME@$CN"
:delay 20
## client certificate, and private key
/certificate export-certificate "$USERNAME@$CN" export-passphrase="$PASSWORD"


:global USERNAME "user4"
:global PASSWORD "user0004"

## add a user
/ppp secret add name=$USERNAME password=$PASSWORD profile=OVPN-PROFILE service=ovpn

## generate a client certificate
/certificate add name=client-template-to-issue copy-from="CLIENT-tpl" common-name="$USERNAME@$CN" 

/certificate sign client-template-to-issue ca="$CN" name="$USERNAME@$CN"
:delay 20
## client certificate, and private key
/certificate export-certificate "$USERNAME@$CN" export-passphrase="$PASSWORD"


:global USERNAME "user5"
:global PASSWORD "user0005"

## add a user
/ppp secret add name=$USERNAME password=$PASSWORD profile=OVPN-PROFILE service=ovpn

## generate a client certificate
/certificate add name=client-template-to-issue copy-from="CLIENT-tpl" common-name="$USERNAME@$CN" 

/certificate sign client-template-to-issue ca="$CN" name="$USERNAME@$CN"
:delay 20
## export the CA, client certificate, and private key
/certificate export-certificate "$CN" export-passphrase="" 

/certificate export-certificate "$USERNAME@$CN" export-passphrase="$PASSWORD"

File: /ovpn_server.rsc
## PARAMETERS 
:global ORG "AGE"
:global COUNTRY "ES"
:global STATE "ES"
:global LOCALITY "Spain"
## Key sizes 1024, 2048, 4096
:global KEYSIZE 2048


## server and ca certificates
/certificate add name=CA-tpl country="$COUNTRY" state="$STATE" locality="$LOCALITY" organization="$ORG"  common-name="CA" key-size=$KEYSIZE key-usage=crl-sign,key-cert-sign
/certificate add name=SERVER-tpl country="$COUNTRY" state="$STATE" locality="$LOCALITY" organization="$ORG" common-name="SERVER" key-size=$KEYSIZE key-usage=digital-signature,key-encipherment,tls-server
/certificate add name=CLIENT-tpl country="$COUNTRY" state="$STATE" locality="$LOCALITY" organization="$ORG" common-name="CLIENT" key-size=$KEYSIZE key-usage=tls-client
/certificate sign CA-tpl ca-crl-host=127.0.0.1 name="CA"
/certificate sign SERVER-tpl ca="CA" name="SERVER"


## create IP pool
/ip pool add name=OVPN-POOL ranges=172.17.0.2-172.17.0.15 

## add VPN profile
/ppp profile add dns-server=172.17.0.1 local-address=172.17.0.1 name=OVPN-PROFILE remote-address=OVPN-POOL use-encryption=yes

## setup OpenVPN server
/interface ovpn-server server set auth=sha1 certificate="SERVER" cipher=aes128,aes192,aes256 default-profile=OVPN-PROFILE enabled=yes require-client-certificate=yes

## add a firewall rule
/ip firewall filter add chain=input dst-port=1194 protocol=tcp comment="Allow OpenVPN"





File: /README.md
# MikroTik_OpenVPN_Server_Setup

MikroTik (Router OS) OpenVPN Server Setup

## Server Setup in Mikrotik Router

Upload both files `ovpn_server.rsc` and `ovpn_clients.rsc`. To import any `.rsc` file open a terminal and write
````
import file=XXXXX
```` 
where XXXXX is the name of the file to import.

First import `ovpn_server.rsc` that will make the following actions:

+ Create the CA and Server certificates  
+ Create an IP pool that will be assigned to any client connected to the VPN
+ Setup a VPN profile linked to the ip pool created
+ Setup RouterOS's OpenVPN native server
+ Add a firewall route in order to accept traffic to the OpenVPN server

Then import `ovpn_clients.rsc` that will make the following actions for each user:

+ Create user secret  
+ Generate and sign user's certificate
+ Export user's client certificate and key


At the end it will also export the CA certificate neede for the client configuration file.

![clients](./art/clients.png)


## Client Setup in Mikrotik Router

Download all client certificates to your local machine and put them in the `/certificates` folder
then run:

**Each users's password is user000X where X is the user number**

Remove passwords from key files with the following script:
```
$sh ./sign_certs.sh
Signing cert from user 1
Enter pass phrase for certificates/cert_export_user1@CA.key:
writing RSA key
...
```
Go to `create_config.sh` and add the following variables `PUBLIC_ADDRESS` (your router's public ip address) and `PUBLIC_PORT` (OpenVPN's server exposed port).

Generate `.ovpn` config files with following script:

```
$sh create_config.sh
mkdir: configs: File exists
Creating user 1 dir...
Copying user cert and key...
Creating user auth...
Creating config file...
...
```

Now in `/configs` folder you will find one folder with each user and their config files needed to configure the client


## Resources
+ [OpenVPN Server and certificate management on MikroTik](https://gist.github.com/SmartFinn/8324a55a2020c56b267b)
+ [OpenVPN Mikrotik Wiki](https://wiki.mikrotik.com/wiki/OpenVPN)
+ [MikroTik OpenVPN server and Windows OpenVPN client (LAB demo)](https://www.youtube.com/watch?v=ucifDsLHj6c)



File: /sign_certs.sh
#!/bin/bash
for i in `seq 1 5`;
        do
                echo "Signing cert from user $i"
                openssl rsa -in certificates/cert_export_user$i\@CA.key -out certificates/cert_export_user$i\@CA.key
        done  

File: /template.ovpn
client
dev tun
proto {PROTOCOL}

remote {PUBLIC_ADDRESS} 
port {PUBLIC_PORT}
resolv-retry infinite


# Most clients don't need to bind to
# a specific local port number.
nobind

# Try to preserve some state across restarts.
persist-key
persist-tun

# SSL/TLS client
tls-client

# Chech server serificate in key-usage
remote-cert-tls server

ca cert_export_CA.crt
cert cert_export_{CLIENT}.crt
key  cert_export_{CLIENT}.key

# moderate verbosity
verb 4
mute 10

auth-user-pass user.auth
auth-nocache
# Select a cryptographic cipher.
# If the cipher option is used on the server
# then you must also specify it here.
cipher AES-256-CBC

# cipher algorithm
auth SHA1

# Pushing the redirect-gateway option to clients
# will cause all IP network traffic originating
# on client machines to pass through the OpenVPN
# server. 
redirect-gateway def1

# Silence  the output of replay warnings, which are a common false
# alarm on WiFi networks.  This option preserves the  security  of
# the replay protection code without the verbosity associated with
# warnings about duplicate packets.
mute-replay-warnings


