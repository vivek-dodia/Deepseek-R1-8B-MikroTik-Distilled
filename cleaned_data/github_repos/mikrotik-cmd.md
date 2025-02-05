# Repository Information
Name: mikrotik-cmd

# Directory Structure
Directory structure:
└── github_repos/mikrotik-cmd/
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
    │   │       ├── pack-e563a1855e06c87fb22a23692b2f5eb475708b65.idx
    │   │       └── pack-e563a1855e06c87fb22a23692b2f5eb475708b65.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── mikrotik-cmd.py
    ├── mikrotik.py
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
	url = https://github.com/annttu/mikrotik-cmd.git
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
0000000000000000000000000000000000000000 5cd91ba239a1d4ea00ea099c99311d4806908376 vivek-dodia <vivek.dodia@icloud.com> 1738606090 -0500	clone: from https://github.com/annttu/mikrotik-cmd.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5cd91ba239a1d4ea00ea099c99311d4806908376 vivek-dodia <vivek.dodia@icloud.com> 1738606090 -0500	clone: from https://github.com/annttu/mikrotik-cmd.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5cd91ba239a1d4ea00ea099c99311d4806908376 vivek-dodia <vivek.dodia@icloud.com> 1738606090 -0500	clone: from https://github.com/annttu/mikrotik-cmd.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5cd91ba239a1d4ea00ea099c99311d4806908376 refs/remotes/origin/master


File: /.git\refs\heads\master
5cd91ba239a1d4ea00ea099c99311d4806908376


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
File: /mikrotik-cmd.py
#!/usr/bin/env python3
# encoding: utf-8

import cmd
import getpass
from mikrotik import Mikrotik, MikrotikAPIError

class colors:
    MAGENTA = '\033[35m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    RED = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class MikrotikCommandLoop(cmd.Cmd):

    m = None
    prompt = '> '

    def precmd(self, line):
        if self.m and line.startswith("/"):
            line = "run %s" % line
        return cmd.Cmd.precmd(self, line)

    def do_greet(self, line):
        print("Welcome to use Mikrotik remote command line tool")

    def do_EOF(self, line):
        print("")
        return True

    def do_login(self, line):
        """
        Connect to device
        Usage: address user password
        """
        args = line.split()
        if len(args) < 1:
            print("Usage: login address [user] [password]")
            return
        if len(args) < 2:
            user = input("Username: ")
            passwd = getpass.getpass("Password: ")
        elif len(args) < 3:
            user = args[1]
            passwd = getpass.getpass("Password: ")
        else:
            user = args[1]
            passwd = args[2]

        self.m =  Mikrotik(args[0])
        self.m.login(user, passwd)
        self.prompt = '%s> ' % args[0]

    def do_run(self, line):
        """
        Run command on remote Mikrotik.
        """
        if not self.m:
            print("login first!")
            return
        args = line.split()
        if len(args) < 1:
            print("Usage: run [args]")
            return
        command = args[0]
        arguments = {}
        queries = {}
        argument_dict = arguments
        expect_number = False
        for i in args[1:]:
            if i.lower() == 'where':
                argument_dict = queries
                continue
            if i.lower() in ['print', 'add']:
                command = "%s/%s" % (command, i.lower())
                continue
            if i.lower() in ['set', 'remove']:
                command = "%s/%s" % (command, i.lower())
                expect_number = True
                continue
            if i.isdigit() and expect_number:
                argument_dict['.id'] = '*%s' % i
                expect_number=False
                continue
            expect_number = False
            try:
                (a, b) = i.split("=",1)
                argument_dict[a] = b
            except ValueError:
                print("Invalid argument %s" % i)
                return

        response = self.m.run(command, attributes=arguments, queries=queries)
        for r in response:
            if r.status == "done":
                continue
            attributes = ' '.join(["%s%s%s=%s%s%s" % (colors.BLUE, k, colors.ENDC, colors.GREEN, v, colors.ENDC) for k, v in r.attributes.items()])
            if '.id' in r.attributes:
                _id = r.attributes['.id'].lstrip("*")
                print("!%s%s%s %s%s%s %s %s" % (colors.BOLD, colors.MAGENTA, r.status, colors.RED, _id, colors.ENDC, attributes, ' '.join(r.error)))
            else:
                print("!%s%s%s%s %s %s" % (colors.BOLD, colors.MAGENTA, r.status, colors.ENDC, attributes, ' '.join(r.error)))


    def do_logout(self, line):
        if self.m:
            self.m.disconnect()
            self.prompt = "> "
        else:
            self.prompt = "> "


if __name__ == '__main__':
    MikrotikCommandLoop().cmdloop()


File: /mikrotik.py
#!/usr/bin/env python3
# encoding: utf-8
from _socket import SHUT_WR

import logging
import socket
import struct
from hashlib import md5
import binascii


logger = logging.getLogger("MikrotikAPI")


class MikrotikAPIError(Exception):
    pass


class MikrotikAPIErrorCategory:

    MISSING = 0
    ARGUMENT_VALUE = 1
    INTERRUPTED = 2
    SCRIPT_FAILURE = 3
    GENERAL_FAILURE = 4
    API_FAILURE = 5
    TTY_FAILURE = 6
    RETURN_VALUE = 7


def pack_length(length):
    """
    Pack api request length.
    http://wiki.mikrotik.com/wiki/Manual:API#Protocol
    """
    if length < 0x80:
        return struct.pack("!B", length)
    elif length <= 0x3FFF:
        length = length | 0x8000
        return struct.pack("!BB", (length >> 8) & 0xFF, length & 0xFF)
    elif length <= 0x1FFFFF:
        length = length | 0xC00000
        return struct.pack("!BBB", length >> 16, (length & 0xFFFF) >> 8, length & 0xFF)
    elif length <= 0xFFFFFFF:
        length = length | 0xE0000000
        return struct.pack("!BBBB", length >> 24, (length & 0xFFFFFF) >> 16, (length & 0xFFFF) >> 8, length & 0xFF)
    else:
        raise MikrotikAPIError("Too long command!")


def unpack_length(length):
    """
    Unpack api request length.
    :param length: length string to unpack
    :return: length as integer
    """
    if len(length) == 1:
        return ord(length)
    elif len(length) == 2:
        c = ord(length[0]) & ~0xC0
        c <<= 8
        return c + ord(length[1])
    elif len(length) == 3:
        c = ord(length[0]) & ~0xE0
        c <<= 8
        c += ord(length[1])
        c <<= 8
        return c + ord(length[2])
    elif len(length) == 4 and (ord(length[0]) & 0xF0) == 0xE0:
        c = ord(length[0]) & ~0xF0
        c <<= 8
        c += ord(length[1])
        c <<= 8
        c += ord(length[2])
        c <<= 8
        return c + ord(length[3])
    elif len(length) == 4 and (ord(length[0]) & 0x8F) == 0xF0:
        c += ord(length[1])
        c <<= 8
        c += ord(length[2])
        c <<= 8
        c += ord(length[3])
        c <<= 8
        return c + ord(length[4])
    raise MikrotikAPIError("Invalid message length %s!" % length)

class MikrotikAPIResponseTypes:
    STATUS = 1
    ERROR = 2
    DATA = 3


class MikrotikApiResponse(object):
    def __init__(self, status, type, attributes=None, error=None):
        self.status = status
        self.type = type
        self.attributes = attributes
        self.error = error

    def __str__(self):
        return "!%s %s %s" % (self.status, ' '.join(["%s=%s" % (k, v) for k, v in self.attributes.items()]),
                              ' '.join(self.error))

class MikrotikAPIRequest(object):
    def __init__(self, command, attributes=None, api_attributes=None, queries=None):
        """
        Generate request for Mikrotik RouterOS API.
        """
        if not command.startswith('/'):
            raise MikrotikAPIError("Command should start with /")
        self.command = command
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = {}
        if api_attributes:
            self.api_attributes = api_attributes
        else:
            self.api_attributes = {}
        if queries:
            self.queries = queries
        else:
            self.queries = {}

    def get_request(self):
        request = []


        request.append(pack_length(len(self.command)))
        request.append(self.command.encode("utf-8"))

        for attribute, value in self.attributes.items():
            attrib = "=%s=%s" % (attribute, value)
            request.append(pack_length(len(attrib)))
            request.append(attrib.encode("utf-8"))

        for attribute, value in self.api_attributes.items():
            attrib = ".%s=%s" % (attribute, value)
            request.append(pack_length(len(attrib)))
            request.append(attrib.encode("utf-8"))

        # TODO: complete query parsing
        for key, value in self.queries.items():
            if value:
                query = "?%s=%s" % (key, value)
            else:
                query = "?%s" % (key,)
            request.append(pack_length(len(query)))
            request.append(query.encode("utf-8"))

        request.append(pack_length(0))
        return b''.join(request)


class Mikrotik(object):
    def __init__(self, address, port=8728):
        self._address = address
        self._port = port
        self.connect()

    def connect(self):
        self._socket = socket.socket()
        self._socket.connect((self._address, self._port))

    def _send(self, data):
        logger.debug("Sending %s" % data)
        self._socket.send(data)

    def _recv(self):
        responses = b''
        while True:
            responses += self._socket.recv(2048)
            logger.debug("Got %s from API" % (responses,))
            if responses[-1] != 0:
                # Next iteration needed
                continue
            break

        if len(responses) < 2:
            raise MikrotikAPIError("Invalid response from API: too short message")

        return_values = []

        for response in responses.split(b'\x00')[:-1]:
            start = 0
            response = response.decode("utf-8")
            f = response.find("!")
            length = unpack_length(response[:f])
            response = response[f:]
            status = response[1:length]
            if status not in ['done', 'trap', 'fatal', 're']:
                raise MikrotikAPIError("Invalid response from API: invalid status %s" % status)
            if status == 'done':
                _type = MikrotikAPIResponseTypes.STATUS
            elif status == 're':
                _type = MikrotikAPIResponseTypes.DATA
            elif status in ['trap', 'fatal']:
                _type = MikrotikAPIResponseTypes.ERROR
            else:
                raise MikrotikAPIError("Got unknown error from API: %s" % response[length+1:])
            start += length
            length_length = 0
            data = {}
            errors = []
            while start < len(response):
                if (ord(response[start]) & 0x80) == 0:
                    length = unpack_length(response[start])
                    length_length = 1
                elif (ord(response[start]) & 0xC0) == 0x80:
                    length = unpack_length(response[start:start+1])
                    length_length = 2
                elif (ord(response[start]) & 0xE0) == 0xC0:
                    length = unpack_length(response[start:start+2])
                    length_length = 3
                elif (ord(response[start]) & 0xF0) == 0xE0:
                    length = unpack_length(response[start:start+3])
                    length_length = 4
                elif (ord(response[start]) & 0xF8) == 0xF0:
                    length = unpack_length(response[start:start+4])
                    length_length = 5
                start += length_length
                message = response[start:start+length]
                if message.startswith('='):
                    if message.startswith("=message="):
                        errors.append(message[9:])
                    else:
                        (k, v) = message[1:].split("=",1)
                        data.update({k: v})
                start += length
            return_values.append(MikrotikApiResponse(status=status, type=_type, error=errors, attributes=data))
        return return_values

    def login(self, username, password):
        r = MikrotikAPIRequest(command="/login")
        self._send(r.get_request())
        response = self._recv()[0]
        if 'ret' in response.attributes.keys():
            value = binascii.unhexlify(response.attributes['ret'])
            md = md5()
            md.update('\x00'.encode("utf-8"))
            md.update(password.encode("utf-8"))
            md.update(value)
            r = MikrotikAPIRequest(command="/login", attributes={'name': username, 'response': "00" + md.hexdigest()})
            self._send(r.get_request())
            self._recv()
            return
        raise MikrotikAPIError("Cannot log in!")

    def run(self, *args, **kwargs):
        r = MikrotikAPIRequest(*args, **kwargs)
        self._send(r.get_request())
        return self._recv()

    def disconnect(self):
        self._socket.shutdown(SHUT_WR)
        self._socket.close()


File: /README.md
Mikrotik-API
===

Python interface and command line tool for Mikrotik API.

Usage
=====

Usage tries to be similar to cli. Commands are prefixed with same paths as in ssh. Options are given using key=value syntax.

print
-----

    /path print [where arg1=value1 [arg2=value2] ...]

Print prints current status of values in given path. Optional where limits query output to contain only values with those values set.
    
set
---

    /path set [id] arg1=value1 [arg2=value2] ...

Set sets new values for existing rows. Id is mandatory if value have ``.id`` attribute. 

add
---

    /path add arg1=value1 [arg2=value2] ...
    
Add adds new row to path.

remove
----

     /path remove id

Remove removes row from path with id ``id``

License
========

The MIT License (MIT)

Copyright (c) 2015 Antti Jaakkola

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


