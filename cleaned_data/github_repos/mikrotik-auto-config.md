# Repository Information
Name: mikrotik-auto-config

# Directory Structure
Directory structure:
└── github_repos/mikrotik-auto-config/
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
    │   │       ├── pack-ac12d572355c8b228fe47feb2e82321467de103a.idx
    │   │       └── pack-ac12d572355c8b228fe47feb2e82321467de103a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── LICENSE
    ├── mikrotik-auto-config-ssh.py
    ├── README.md
    ├── requirements.txt
    └── squid.md


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
	url = https://github.com/InfosecBlake/mikrotik-auto-config.git
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
0000000000000000000000000000000000000000 0b7b6ae07d13eb782a4d6f060794d57f93c5992e vivek-dodia <vivek.dodia@icloud.com> 1738606060 -0500	clone: from https://github.com/InfosecBlake/mikrotik-auto-config.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 0b7b6ae07d13eb782a4d6f060794d57f93c5992e vivek-dodia <vivek.dodia@icloud.com> 1738606060 -0500	clone: from https://github.com/InfosecBlake/mikrotik-auto-config.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0b7b6ae07d13eb782a4d6f060794d57f93c5992e vivek-dodia <vivek.dodia@icloud.com> 1738606060 -0500	clone: from https://github.com/InfosecBlake/mikrotik-auto-config.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0b7b6ae07d13eb782a4d6f060794d57f93c5992e refs/remotes/origin/main
2cb78a7c929c1bd38a8ec48da87fa3a05988d124 refs/tags/0.2.1
93be3c585bf8db9b4cffff8ccdaa217ffc1df212 refs/tags/0.3.0


File: /.git\refs\heads\main
0b7b6ae07d13eb782a4d6f060794d57f93c5992e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
# ignore all logs
File: /LICENSE
MIT License

Copyright (c) 2021 InfosecBlake

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


File: /mikrotik-auto-config-ssh.py
import paramiko

from tkinter import *
from tkinter import filedialog


def run_command(cmd_str, hostname, port, username, password, nbytes=4096):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')

    session.exec_command(cmd_str)

    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print('exit status: ', session.recv_exit_status())

    session.close()
    client.close()


def sftp_upload_config(config_file, hostname, port, username, password):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(client)
    sftp.put(config_file, "flash/config.rsc")
    sftp.close()
    print('SFTP Config File Upload Complete.')


def sftp_upload_firmware(fw_file, hostname, port, username, password):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(client)
    sftp.put(fw_file, "firmware.npk")
    sftp.close()
    print('SFTP Firmware Upload Complete.')


def gen_cmd_str_ip(ip, interface):
    return f"ip address add address={ip} interface={interface}"


def gen_cmd_str_gw(gateway):
    return f"ip route add dst-address=0.0.0.0/0 gateway={gateway}"


def gen_cmd_str_id(identity):
    return f"system identity set name={identity}"


def gen_cmd_str_wpa(wpa):
    return f"interface wireless security-profiles add name=WPA mode=dynamic-keys authentication-types=wpa2-psk wpa2-pre-shared-key={wpa}"


def gen_cmd_str_ssid1(ssid1):
    return f"interface wireless set ssid={ssid1} wlan1"


def gen_cmd_str_ssid2(ssid2):
    return f"interface wireless set ssid={ssid2} wlan2"


def init_tk(root):
    def select_config():
        filename = filedialog.askopenfilename()
        config_entries.insert('0.0', filename)
        debug_box.insert(END, ('\nConfig File Selected: ' + filename))
    def upload_config():
        config_name = config_entries.get('0.0', 'end')
        formatted_config_name = config_name.strip()
        sftp_upload_config((formatted_config_name), entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Config Uploading...')
        debug_box.insert(END, 'Config Uploaded\n')
    def select_firmware():
        firmware = filedialog.askopenfilename()
        firmware_entries.insert('0.0', firmware)
        debug_box.insert(END, ('\nFirmware File Selected: ' + firmware))
    def upload_firmware():
        fw_name = firmware_entries.get('0.0', 'end')
        formatted_fw_name = fw_name.strip()
        sftp_upload_firmware((formatted_fw_name), entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Firmware Uploaded') 
        debug_box.insert(END, '\nFirmware uploaded')
    def reboot_device():
        reboot_command = []
        reboot_cmd = 'system reboot'
        reboot_command.append(reboot_cmd)
        reboot_cmd = 'y'
        reboot_command.append(reboot_cmd)
        format_reboot = "\n".join(reboot_command)
        run_command(format_reboot, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Device is rebooting')
        debug_box.insert(END, 'Device has rebooted\n')
    def reset_config():
        reset_command = []
        reset_cmd = 'system reset-configuration run-after-reset=flash/config.rsc no-defaults=yes'
        reset_command.append(reset_cmd)
        reset_cmd = 'y'
        reset_command.append(reset_cmd)
        format_reset = "\n".join(reset_command)
        run_command(format_reset, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Resetting device configuration and installing baseline config...')
        debug_box.insert(END, 'Resetting device configuration and installing baseline config...\n')
    def clear_entries():
        for key, entry, in entries.items():
            entry.delete(0, 'end')
        config_entries.delete('0.0', 'end')
        firmware_entries.delete('0.0', 'end')
        debug_box.delete('0.0', 'end')
    def send_commands():
        all_commands = []

        if entries['ip'].get() != '':
            cmd_str = gen_cmd_str_ip(entries['ip'].get(), interface_select.get())
            all_commands.append(cmd_str)
            debug_box.insert(END, '\nWAN IP address changed to: ', entries['ip'].get())
        else:
            debug_box.insert(END, 'Did not change WAN IP address\n')
            print('Did not change WAN IP address')

        if entries['gateway'].get() != '':
            cmd_str = gen_cmd_str_gw(entries['gateway'].get())
            all_commands.append(cmd_str)
            debug_box.insert(END, '\nGateway IP address changed to: ', entries['gateway'].get())
        else:
            debug_box.insert(END, 'Did not change gateway IP address\n')
            print('Did not change IP address')

        if entries['identity'].get() != '':
            if ' ' in entries['identity'].get():
                debug_box.insert(END, 'Please remove space in Identity\n')
                print('Please remove space in Identity')
            else:
                cmd_str = (gen_cmd_str_id(entries['identity'].get()))
                all_commands.append(cmd_str) 
                debug_box.insert(END, '\nIdentity changed to: ' + entries['identity'].get())     
        else:
            print('Did not change identity')

        if entries['wpa'].get() != '' or len(entries['wpa'].get()) >=8:
            cmd_str = gen_cmd_str_wpa(entries['wpa'].get())
            all_commands.append(cmd_str)
            debug_box.insert(END, '\nWPA passphrase changed to: ', entries['wpa'].get())
        else:
            debug_box.insert(END, 'Did not change WPA passphrase\n')
            print('Did not change WPA passphrase')

        if entries['ssid1'].get() != '':
            cmd_str = gen_cmd_str_ssid1(entries['ssid1'].get())
            all_commands.append(cmd_str)
            debug_box.insert(END, '\n2.4Ghz SSID changed to: ', entries['ssid1'].get())
        else:
            debug_box.insert(END, 'Did not change 2.4 Ghz SSID\n')
            print('Did not change 2.4 Ghz SSID')

        if entries['ssid2'].get() != '':
            cmd_str = gen_cmd_str_ssid2(entries['ssid2'].get())
            all_commands.append(cmd_str)
            debug_box.insert(END, '\n5Ghz SSID changed to: ', entries['ssid2'].get())
        else:
            debug_box.insert(END, 'Did not change 5Ghz Ghz SSID\n')
            print('Did not change 5Ghz SSID')
        
        formatted_commands = "\n".join(all_commands)
        run_command(formatted_commands, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
    
    root.geometry("825x550")
    root.title("Lets get configuring!")
    root.eval('tk::PlaceWindow . center')
    root.configure(background='snow2')
    entries = {}
    mgmt_ip_label = Label(root, text='Management IP Address:*', font=('calibre', 10, 'bold'), bg='snow2', fg='forest green')
    entries['mgmt_ip'] = Entry(root, justify='center', font=('calibre', 10))
    mgmt_ip_label.grid(row=0, column=0, sticky = W, pady=2, padx=5)
    entries['mgmt_ip'].grid(row=0, column=1, pady=2)
    port_label = Label(root, text='Management Port:*', font=('calibre', 10, 'bold'), bg='snow2', fg='forest green')
    entries['port'] = Entry(root, justify='center', font=('calibre', 10))
    port_label.grid(row=0, column=2, sticky=W, pady=2, padx=5)
    entries['port'].grid(row=0, column=3, pady=2)
    user_label = Label(root, text='Username:*', font=('calibre', 10, 'bold'), bg='snow2', fg='forest green')
    entries['user'] = Entry(root, justify='center', font=('calibre', 10))
    user_label.grid(row=1, column=0, sticky=W, pady=2, padx=5)
    entries['user'].grid(row=1, column=1, pady=2)
    pass_label = Label(root, text='Password:*', font=('calibre', 10, 'bold'), bg='snow2', fg='forest green')
    entries['pass'] = Entry(root, justify='center', show='*', font=('calibre', 10))
    pass_label.grid(row = 1, column=2, sticky=W, pady=2, padx=5)
    entries['pass'].grid(row=1, column=3, pady=2)
    ip_label = Label(root, text='WAN IP Address (CIDR):', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['ip'] = Entry(root, justify='center', font=('calibre', 10))
    ip_label.grid(row=3, column=0, sticky=W, pady=2, padx=5)
    entries['ip'].grid(row= 3, column=1, pady=2)
    interface_list = ['ether1', 'ether2', 'ether3', 'ether4', 'ether5', 'ether6', 'ether7', 'ether8', 'ether9', 'ether10', 'wlan1', 'wlan2', 'sfp1', 'sfp+plus1']
    interface_select = StringVar(root)
    interface_select.set(interface_list[0])
    interface_label = Label(root, text = 'WAN Interface:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    interface_drop = OptionMenu(root, interface_select, *interface_list)
    interface_label.grid(row=4, column=0, sticky=W, pady=2, padx=5)
    interface_drop.grid(row=4, column=1, pady=2)
    gateway_label = Label(root, text='Default Gateway:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['gateway']=Entry(root, justify='center', font=('calibre', 10))
    gateway_label.grid(row=5, column=0, sticky=W, pady=2, padx=5)
    entries['gateway'].grid(row=5, column=1, pady=2)
    identity_label = Label(root, text='Identity:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['identity'] = Entry(root, justify='center', font=('calibre', 10))
    identity_label.grid(row=6, column=0, sticky=W, pady=2, padx=5)
    entries['identity'].grid(row=6, column=1, pady=2)
    wpa_label = Label(root, text='WiFi Password:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['wpa'] = Entry(root, justify='center', show='*', font=('calibre', 10))
    wpa_label.grid(row =7, column=0, sticky=W, pady=2, padx=5)
    entries['wpa'].grid(row=7, column=1, pady=2)
    ssid1_label = Label(root, text='2.4Ghz SSID:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['ssid1'] = Entry(root, justify='center', font=('calibre', 10))
    ssid1_label.grid(row=8, column=0, sticky=W, pady=2, padx=5)
    entries['ssid1'].grid(row=8, column=1, pady=2)
    ssid2_label = Label(root, text='5Ghz SSID:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    entries['ssid2'] = Entry(root, justify='center', font=('calibre', 10))
    ssid2_label.grid(row=9, column=0, sticky=W, pady=2, padx=5)
    entries['ssid2'].grid(row=9, column=1, pady=2)
    submit_button = Button(root, text='Submit', command=send_commands)
    submit_button.grid(row=12, column=2, sticky=W, pady=10, padx=5)
    clear_button = Button(root, text='Clear', command=clear_entries)
    clear_button.grid(row=12, column=1, sticky=E, pady=10, padx=5)
    config_entries = Text(root, height=1, width=20, font=('calibre', 10))
    config_entries.grid(row=4, column=3, sticky=N, columnspan=2, pady=2, padx=5)
    config_label = Label(root, text='Upload Configuration File:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    config_label.grid(row=4, column=2, sticky=N, pady=2, padx=5)
    config_button = Button(root, text='Select', command=select_config)
    config_button.grid(row=5, column=2, sticky=W, pady=2, padx=5)
    upload_button = Button(root, text='Upload', command=upload_config)
    upload_button.grid(row=5, column=2, sticky=E, pady=2, padx=5)
    firmware_entries = Text(root, height=1, width=20, font=('calibre', 10))
    firmware_entries.grid(row=6, column=3, sticky=N, columnspan=2, pady=2, padx=5)
    firmware_label = Label(root, text='Upload Firmware File:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    firmware_label.grid(row=6, column=2, sticky=W, pady=2, padx=5)
    firmware_select_button = Button(root, text='Select', command=select_firmware)
    firmware_select_button.grid(row=7, column=2, sticky=W, pady=2, padx=5)
    firmware_upload_button = Button(root, text='Upload', command=upload_firmware)
    firmware_upload_button.grid(row=7, column=2, sticky=E, pady=2, padx=5)
    reboot_button = Button(root, text='Reboot', command=reboot_device)
    reboot_button.grid(row=8, column=3, sticky=N, pady=2, padx=5)
    reset_button = Button(root, text='Run', command=reset_config)
    reset_button.grid(row=5, column=3, sticky=N, pady=2, padx=5)
    debug_lable = Label(root, text='Debug Console:', font=('calibre', 10, 'bold'), bg='snow2', fg='black')
    debug_lable.grid(row=10, column=0, sticky=W, pady=2, padx=5)
    debug_box = Text(root, height=10, width=75, font=('calibre', 10))
    debug_box.grid(row=11, column=0, sticky=N, columnspan=5, pady=2, padx=2)

def main():
    root = Tk()
    init_tk(root)
    root.mainloop()
    paramiko.util.log_to_file('paramiko.log', level='INFO')

if __name__ == '__main__':
    main()



File: /README.md
# Mikrotik Configuration Utility

Mikrotik Configuration Manager is a Python utility for better configuration and management. The utility uses SSH to configure the device and is intended as a replacement for quickset. This is an ongoing project that will help ISP/WISP/MSP installers and network administrators speed up their time till installtion. 


![MikrotikAutoConfigUtilityv0 3 0](https://user-images.githubusercontent.com/87310427/127784200-2088bdf7-1ae6-48dc-aa11-99a5f78560a4.png)


## Installation

Download the `mikrotik-auto-config-ssh.py` script and
use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install tkinter
pip install paramiko
```

## Usage

To use the utility, cd to the directory that contains your `mikrotik-auto-config-ssh.py` script and then run the script as shown below:
```bash
python mikrotik-auto-config-ssh.py
```
**Required Fields:**
- Management IP Address
- Management Port
- Username
- Password

**Step 1:** Configuration upload
- Once layer 3 access to device is verified, use the `Upload Configuration File` `select` button to choose your baseline config file. **See notes for requirements.**
- Click the upload button to transer the config file to the Routerboard
- Click the `Run` button to initiate defaulting the device and running the config file. This will take a couple minutes so be patient.

**Step 2:** Configuration of install related fields
- Proceed with entering the install related data fields. **All fields must be data filled for configuration to work.**
- **WAN IP must be entered in CIDR format i.e. 10.1.1.1/24**
- Choose your WAN interface from the drop down menu. 
- Enter Identity, WPA passphrase, and SSIDs to continue. **WPA passphrase must be at lease 8 characters long with at least one number or one capitol. This is a Mikrotik requirement.**
- Once all of the fields are filled, click the ```Submit``` button. This will initiate a SSH connection to the device and will send the remaining programing to the device. 

**Firmware Uploading:**
- Use the ```Select``` button under ```Upload Firmware File``` to chose the package file you would like to upload. 
- Once selected, use the ```Upload``` button to push the firmware file to the Routerboard. 
- Finally, click the ```Reboot``` button to send the reboot command to the Routerboard. Upon rebooting, the device will upgrade the firmware.

#### **Notes:**
This tool uses SSH and SFTP for connection to the device. You must have layer 3 access to the device to use this tool.

**You will need to add the following line to the top of any configuration files that you intend to use:**
```/delay delay-time=15s```

If you do not add the above line, the configuration utility of the program will fail and your device will be reset with no default configuration.

## Pipeline
#### Note: These items are subject to change at any time and are not guaranteed

- Ability to upload baseline configurations and scripts - **Complete**
- Ability to update and reboot devices - **Complete**
- Reformat of the GUI for easier navigation and usage
- Debugging and checks/balances - **Complete**
- Check connection - ICMP check to device
- Making tool executable
- Device detection, think similar to CDP neighbors
- Dynamic interface population

## Contributing
If you would like to become a contributer please open an issue. For changes, please open an issue first to discuss what you would like to change.

If a you would like to commit a change, please open a pull request for review. Please make sure to update tests as appropriate.

## License
MIT License


File: /requirements.txt
paramiko==2.7.2
tk-tools


File: /squid.md
```
       .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    \
   /        .-----.        \
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              | |
             _| |_
            /\( )/\
           /  ` '  \
          | |     | |
          '-'     '-'
          | |     | |
          | |     | |
          | |-----| |
       .`/  |     | |/`.
       |    |     |    |
       '._.'| .-. |'._.'
             \ | /
             | | |
             | | |
             | | |
            /| | |\
          .'_| | |_`.
ISB       `. | | | .'
       .    /  |  \    .
      /o`.-'  / \  `-.`o\
     /o  o\ .'   `. /o  o\
     `.___.'       `.___.'
```


