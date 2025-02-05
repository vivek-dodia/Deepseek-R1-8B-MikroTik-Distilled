# Repository Information
Name: lord_of_mikrotik

# Directory Structure
Directory structure:
└── github_repos/lord_of_mikrotik/
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
    │   │       ├── pack-268a29045d9618883b574adb89ebac3cd36f9a79.idx
    │   │       └── pack-268a29045d9618883b574adb89ebac3cd36f9a79.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── add_time.py
    ├── api_test3.py
    ├── bitbucket-pipelines.yml
    ├── bot.py
    ├── bot_web_hook.py
    ├── bot_web_hook_cherry.py
    ├── config_example.py
    ├── create_cert.py
    ├── create_database.py
    ├── create_mit_name.py
    ├── database.vdb
    ├── dbworker.py
    ├── duration.py
    ├── generation_name2.py
    ├── generation_pass.py
    ├── master/
    │   ├── add_time.py
    │   ├── api_test3.py
    │   ├── bot.py
    │   ├── bot_web_hook.py
    │   ├── bot_web_hook_cherry.py
    │   ├── config_example.py
    │   ├── create_cert.py
    │   ├── create_database.py
    │   ├── create_mit_name.py
    │   ├── duration.py
    │   ├── generation_name2.py
    │   ├── generation_pass.py
    │   ├── requirments.txt
    │   └── systemd_example.txt
    ├── README.md
    ├── requirments.txt
    └── systemd_example.txt


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
	url = https://github.com/namor-katz/lord_of_mikrotik.git
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
0000000000000000000000000000000000000000 d1bacd5fa4c0957371011be7d8eb303d82a4254c vivek-dodia <vivek.dodia@icloud.com> 1738606432 -0500	clone: from https://github.com/namor-katz/lord_of_mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d1bacd5fa4c0957371011be7d8eb303d82a4254c vivek-dodia <vivek.dodia@icloud.com> 1738606432 -0500	clone: from https://github.com/namor-katz/lord_of_mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d1bacd5fa4c0957371011be7d8eb303d82a4254c vivek-dodia <vivek.dodia@icloud.com> 1738606432 -0500	clone: from https://github.com/namor-katz/lord_of_mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d1bacd5fa4c0957371011be7d8eb303d82a4254c refs/remotes/origin/master


File: /.git\refs\heads\master
d1bacd5fa4c0957371011be7d8eb303d82a4254c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
*.sql
File: /add_time.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

def add_data2(duration):
    #print('я адд тайм',  duration)
    date_create = time()
    date_create = int(date_create)
    date_off = date_create + int(duration) * 3600
    return date_create,  date_off

#def add_extra_data2(dur):
'''
def who_poweroff():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM t WHERE date_off <= strftime('%s', 'now')")
    result = cursor.fetchall()
    return result
'''


File: /api_test3.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_api3.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#  
import ssl
from librouteros import connect
#from pprint import pprint
import os
#from datetime import datetime
from time import time

# check conf file
if os.access('config.py', os.F_OK) == True:
    import config
else:
    print('no config file! EXIT')
    print('please, create config.py, added to login, password and ip or dns  \
    your router')
    exit()

# connect to mikrotik
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ctx.set_ciphers('RSA')
api = connect(username = config.login, password = config.password, host = config.host, ssl_wrapper=ctx.wrap_socket, port=8729)
#if not connect connect no ssl!

# total count user vpn
def list_count_vpn_user():
    users = api(cmd='/ppp/secret/print')
    count_users = len(users)
    return count_users


# names all users vpn
def list_vpn_user_name():
    users = api(cmd='/ppp/secret/print')
    names = []
    for i in users:
        names.append(i['name'])
    return names



#count activity user vpn
def list_count_activity_vpn_user():
    users = api(cmd='/ppp/secret/print')
    i = 0
    for name in users:
        if name['disabled'] == False:
            i = i +1
    #return i
    count = i
    return count
    

#name activity user vpn
def list_vpn_active_user():
    users = api(cmd='/ppp/secret/print')
    names = []
    for i in users:
        if i['disabled'] == False:
            names.append(i['name'])
            #print(i['name'])
        else:
            pass
    return names

#close active conection from select user
def close_connection(name_input):
    '''this function close active connect'''
    connect = api(cmd='/ppp/active/print')
    if len(connect) != 0:
        
        params = {}
        for i in connect:
            if i['name'] == name_input:
                name_id = i['.id']
                params['.id'] = name_id
                api(cmd='/ppp/active/remove', **params)
                return True
            else:
                pass
    else:
        pass
        

#disable user vpn
def disable_vpn_user(name_input):
    ''' this function disable user, if exists'''
    users = api(cmd='/ppp/secret/print')
    params = {'disabled' : True}
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/set', **params)
            result = True
            return result
        else:
            pass
            
    #!!! close session if exists
    api(cmd='/ppp/secret/set', **params)
    #api.close
    

#enable user vpn
def enable_vpn_user(name_input):
    users = api(cmd='/ppp/secret/print')
    params = {'disabled' : False, '.id' : name_input}
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/set', **params)
            #print('user enable!')
            result = True
            return result
        else:
            pass

#user vpn status
def user_vpn_status(name_input):
    pass
    
#remove user vpn 
def remove_vpn_user(name_input):
    users = api(cmd='/ppp/secret/print')
    params = {}
    
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/remove', **params)
            #print('yes! remove!!')
            remove = True
            return remove
        else:
            #print('user not exist')
            pass
    

#create user vpn
def create_vpn_user(vpn_name,  duration):
    #users = api(cmd='/ppp/secret/print')
    params = {'profile' : 'default', 'service' : 'pptp'}
    import generation_pass
    vpn_pass = generation_pass.create_password()
    #print(vpn_name)
    if len(vpn_name) == 0:
        import generation_name2
        vpn_name = generation_name2.create_name()
    else:
        vpn_name = vpn_name
    
    params['name'] = vpn_name
    params['password'] = vpn_pass
    api(cmd='/ppp/secret/add', **params)
    #from create_database import add_user_in_database
    #add_user_in_database(vpn_name)
    #from add_time import add_data2
    #print('я дуратион из апи ',  duration)
    #from duration import date_off #!!
    #time_of = date_off(time_off)
    #a = add_data2(duration) #!!
    #date_create = a[0]
    #date_off = a[1]
    from create_database import add_user_in_database
    add_user_in_database(vpn_name, duration)
    '''
    from duration import date_off
    print(delta)
    date_off(delta)
    '''
    return params


#list profile print
def list_profile():
    profile = api(cmd='/ppp/profile/print')
    return profile
    #pprint(profile)

#list active connections
def list_active_connections():
    connections = api(cmd='/ppp/active/print')
    conn = []
    #print(type(conn))
    for i in connections:
        conn.append(i)
    #print(type(conn))
    #print(connections)
    return connections
 
#time left
def time_left(username):
     '''this function retunr left time'''
     from create_database import time_to_poweroff
     a = time_to_poweroff(username)
     if a == None:
         #time_left1 = 0
         return False
     else:
         date_off = a[0]
         date_real = time()
         time_left1 = date_off - int(date_real)
         #print('я из апи',  time_left1)
         return time_left1
         
     
#create new profile with fixed time


File: /bitbucket-pipelines.yml
# This is a sample build configuration for Python.
# Check our guides at https://confluence.atlassian.com/x/x4UWN for more examples.
# Only use spaces to indent your .yml configuration.
# -----
# You can specify a custom docker image from Docker Hub as your build environment.
image: python:3.5.1

pipelines:
  default:
    - step:
        caches:
          - pip
        script: # Modify the commands below to build your repository.
          - pip3 install -r requirements.txt

File: /bot.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
import config
from telebot import types
import logging
import api_test3
from create_database import whois
import re
import flask
from time  import sleep

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'увы, я тебя не знаю.'

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    #markup = types.InlineKeyboardMarkup()
    #btn_key_help = types.InlineKeyboardButton(text='start')
    #markup.add(btn_key_help)
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(commands=['count'])
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list'])
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        b = str(a)
        bot.send_message(message.chat.id, b)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text

#create new user vpn
@bot.message_handler(commands=['create'])
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    #print('я твое имя', au)
    if au[0] == True and au[1] <= 1:
        text = message.text[7:]
        text = text.strip()
        from generation_name2 import create_name
        zero_name = create_name()
        #print('я голый текст')
        if text == None:
            duration = 3600
        elif text.isdigit() == True:
            #print('это же число!')
            if text == 0:
                duration = 3600
            else:
                duration = int(text) * 3600
        elif len(text) == 0:
            duration = 3600
        else:
            #print('не поверишь, но ты тут')
            #add create_mit_name
            from create_mit_name import create_mit_name
            #print('а я текст который прилетит',  text)
            row_name = create_mit_name(text)
            #print('я есть полученный текст в мит',  row_name)
            #print(type(row_name))
            
            duration = row_name[1]
            duration = int(duration)
            #print('я дуратион,',   duration,  'мой тип',  type(duration))
            zero_name = row_name[0]
            #print('я зеро нейм',  zero_name)
            bot.send_message(message.chat.id, 'пробуем принять имя')
            #exit()
        
        #zero_name = ''
        a = api_test3.create_vpn_user(zero_name,  duration)
        b = a['name']
        b = str(b)
        #print('имя',  b)
        #print(type(b))
        c = a['password']
        c = str(c)
        #print(b)
        #print(c)
        d = 'логин ' + b + ' пароль ' + c
        bot.send_message(message.chat.id, d)
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass
    
    
    
    #print(text, 'это сырое число')
    

        
    #text = int(text)
    #print(text)


#delete user vpn
@bot.message_handler(commands=['delete'])
def delete_name(message):
    '''this function delete vpn user if exist'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        #print('в смысле нот тайп',  text)
        text = text.strip()
        a = api_test3.remove_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь удален')
        else:
            bot.send_message(message.chat.id, 'увы, такого пользователя нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()
        
        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
        
#enable user vpn
@bot.message_handler(commands=['enable'])
def enable_user(message):
    '''this function enable vpn user, if er exist'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        text = text.strip()

        a = api_test3.enable_vpn_user(text)
        if a == True:
            bot.send_message(message.chat.id, 'пользователь разрешен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого разрешать.')

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
    

@bot.message_handler(commands=['list_connect'])
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list_admins'])
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    b = str(a)
    bot.send_message(message.chat.id, b)
    #add humanize view

@bot.message_handler(commands=['my_time'])
def my_time(message):
    '''this function print left time'''
    from api_test3 import time_left
    text = get_name_u(message, 8) #тут влетает 'имя не указано, удалять нечего' из get_name_u
    #print('я текст из май тайм',  text)
    if text == None:
        bot.send_message(message.chat.id,  'не указано имя, показывать нечего')
        exit()
    else:
        text = text.strip()
    
    a = time_left(text)
    print(a)
    #a = a[0]
    if a > 0:
        time_o = a / 60
        time_o = int(time_o)
        time_o = str(time_o) + ' минут осталось'
    else:
        time_o = 'ваше время истекло'
    
    bot.send_message(message.chat.id, time_o)

bot.pulling(none_stop=True)


File: /bot_web_hook.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
import config
from telebot import types
import logging
import api_test3
from create_database import whois
import re
import flask
from time  import sleep

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

#set environment from web hooks
WEBHOOK_HOST = '138.201.174.71'
WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_key.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

bot = telebot.TeleBot(config.token)

app = flask.Flask(__name__)

#Empty webserver index, return nothing, just http 200
@app.route('/',  methods=['GET',  'HEAD'])
def index():
    return ''
    
# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'увы, я тебя не знаю.'

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    #markup = types.InlineKeyboardMarkup()
    #btn_key_help = types.InlineKeyboardButton(text='start')
    #markup.add(btn_key_help)
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(commands=['count'])
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list'])
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        b = str(a)
        bot.send_message(message.chat.id, b)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text

#create new user vpn
@bot.message_handler(commands=['create'])
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    #print('я твое имя', au)
    if au[0] == True and au[1] <= 1:
        text = message.text[7:]
        text = text.strip()
        from generation_name2 import create_name
        zero_name = create_name()
        #print('я голый текст')
        if text == None:
            duration = 3600
        elif text.isdigit() == True:
            #print('это же число!')
            if text == 0:
                duration = 3600
            else:
                duration = int(text) * 3600
        elif len(text) == 0:
            duration = 3600
        else:
            #print('не поверишь, но ты тут')
            #add create_mit_name
            from create_mit_name import create_mit_name
            #print('а я текст который прилетит',  text)
            row_name = create_mit_name(text)
            #print('я есть полученный текст в мит',  row_name)
            #print(type(row_name))
            
            duration = row_name[1]
            duration = int(duration)
            #print('я дуратион,',   duration,  'мой тип',  type(duration))
            zero_name = row_name[0]
            #print('я зеро нейм',  zero_name)
            bot.send_message(message.chat.id, 'пробуем принять имя')
            #exit()
        
        #zero_name = ''
        a = api_test3.create_vpn_user(zero_name,  duration)
        b = a['name']
        b = str(b)
        #print('имя',  b)
        #print(type(b))
        c = a['password']
        c = str(c)
        #print(b)
        #print(c)
        d = 'логин ' + b + ' пароль ' + c
        bot.send_message(message.chat.id, d)
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass
    
    
    
    #print(text, 'это сырое число')
    

        
    #text = int(text)
    #print(text)


#delete user vpn
@bot.message_handler(commands=['delete'])
def delete_name(message):
    '''this function delete vpn user if exist'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        #print('в смысле нот тайп',  text)
        text = text.strip()
        a = api_test3.remove_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь удален')
        else:
            bot.send_message(message.chat.id, 'увы, такого пользователя нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()
        
        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
        
#enable user vpn
@bot.message_handler(commands=['enable'])
def enable_user(message):
    '''this function enable vpn user, if er exist'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        text = text.strip()

        a = api_test3.enable_vpn_user(text)
        if a == True:
            bot.send_message(message.chat.id, 'пользователь разрешен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого разрешать.')

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
    

@bot.message_handler(commands=['list_connect'])
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list_admins'])
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    b = str(a)
    bot.send_message(message.chat.id, b)
    #add humanize view

@bot.message_handler(commands=['my_time'])
def my_time(message):
    '''this function print left time'''
    from api_test3 import time_left
    text = get_name_u(message, 8) #тут влетает 'имя не указано, удалять нечего' из get_name_u
    #print('я текст из май тайм',  text)
    if text == None:
        bot.send_message(message.chat.id,  'не указано имя, показывать нечего')
        exit()
    else:
        text = text.strip()
    
    a = time_left(text)
    print(a)
    #a = a[0]
    if a > 0:
        time_o = a / 60
        time_o = int(time_o)
        time_o = str(time_o) + ' минут осталось'
    else:
        time_o = 'ваше время истекло'
    
    bot.send_message(message.chat.id, time_o)

# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()
sleep(5)

# set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))
                

# start flask server
app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT, ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV), debug=True)


File: /bot_web_hook_cherry.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
from telebot import types
import logging
import api_test3
from create_database import whois
import re
from time  import sleep
import cherrypy
from os import getpid
import os
import dbworker

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


# check cert files if not - create
filename = 'webhook.crt'
if os.access(filename, os.F_OK) == True:
    pass
else:
    from create_cert import create_self_signed_cert
    create_self_signed_cert()

#create pid file
your_pid = getpid()
your_pid = str(your_pid)
pid_file = '/tmp/bot.pid'
with open (pid_file,  'w',  encoding='utf-8') as ff:
    ff.write(your_pid)

import config
WEBHOOK_PORT = config.WEBHOOK_PORT  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = config.WEBHOOK_LISTEN

WEBHOOK_SSL_CERT = config.WEBHOOK_SSL_CERT  # Путь к сертификату
WEBHOOK_SSL_PRIV = config.WEBHOOK_SSL_PRIV  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (config.WEBHOOK_HOST, config.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

bot = telebot.TeleBot(config.token)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'такого адмнинистратора нет. Попросите вас добавить.'

#create castom keyboard from admin level0
markup0 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
itembtn1 = types.KeyboardButton('администраторы')
itembtn2 = types.KeyboardButton('пользователи')
itembtn3 = types.KeyboardButton('информация')
markup0.add(itembtn1, itembtn2,  itembtn3)

#create custom keyboard from admin level1
markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#itembtn1 = types.KeyboardButton('администратор')
itembtn2 = types.KeyboardButton('пользователи')
itembtn3 = types.KeyboardButton('информация')
markup1.add(itembtn2,  itembtn3)

#create custom keyboard from admin level2
markup2 = types.ReplyKeyboardMarkup(row_width=2,  resize_keyboard = True)
itembtn1 = types.KeyboardButton('информация')
markup2.add(itembtn1)

#create subkeyboard admins
admins_keyboard = types.ReplyKeyboardMarkup(row_width=3,  resize_keyboard = True)
itembtn1 = types.KeyboardButton('добавить')
itembtn2 = types.KeyboardButton('удалить')
itembtn3 = types.KeyboardButton('список')
itembtn4 = types.KeyboardButton('главное_меню')
admins_keyboard.add(itembtn1,  itembtn2,  itembtn3, itembtn4)

#create subkeyboard users
users_keyboard = types.ReplyKeyboardMarkup(row_width = 3,  resize_keyboard = True)
itembtn1 = types.KeyboardButton('создать')
itembtn2 = types.KeyboardButton('удалить')
itembtn3 = types.KeyboardButton('запретить')
itembtn4 = types.KeyboardButton('разрешить')
itembtn5 = types.KeyboardButton('подключенные')
itembtn6 = types.KeyboardButton('всего')
itembtn7 = types.KeyboardButton('перечень')
itembtn8 = types.KeyboardButton('информация')
itembtn9 = types.KeyboardButton('продлить')
itembtn10 = types.KeyboardButton('главное_меню')
users_keyboard.add(itembtn1, itembtn2,  itembtn3,  itembtn4,  itembtn5,  itembtn6,  itembtn7,  itembtn8,  itembtn9, itembtn10)


@bot.message_handler(commands=['start'])
def start(message):
    '''This function displays various menus depending on the administrator's level'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] == 0:
        bot.send_message(message.chat.id,  'нажми любую кнопку',  reply_markup=markup0)
    elif au[0] == True and au[1] == 1:
        bot.send_message(message.chat.id,  'нажми любую кнопку',  reply_markup=markup1)
    elif au[0] == True and au[1] == 2:
        bot.send_message(message.chat.id,  'нажми любую кнопку',  reply_markup=markup2)
    else:
        bot.send_message(message.chat.id,  'нажми любую кнопку',  reply_markup=markup2)


@bot.message_handler(regexp='главное_меню')
def back(message):
    start(message)
    
@bot.message_handler(regexp='администраторы')
def administrators(message):
    bot.send_message(message.chat.id,  'вы в меню администраторы',  reply_markup=admins_keyboard)

@bot.message_handler(regexp='пользователи')   
def users(message):
    bot.send_message(message.chat.id,  'вы в меню пользователи',  reply_markup=users_keyboard)

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(regexp='всего')
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(regexp = 'перечень')
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        #print(type(a))
        #b = str(a)
        bot.send_message(message.chat.id, 'существуют следующие пользователи')
        temp_user_str = ''
        for i in a:
            temp_user_str = i + ',  ' + temp_user_str
        bot.send_message(message.chat.id, temp_user_str)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text


#create new user vpn
text_get_name = 'укажите имя нового пользователя, либо нажмите "отправить" чтобы имя создалось автоматически'
text_get_time = 'укажите время, цифрами, в часах.'
text_final = 'пробую создать пользователя...'

@bot.message_handler(regexp='создать')
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        #dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)
        state = dbworker.get_current_state(message.chat.id)
        if state == config.States.S_START.value:
            bot.send_message(message.chat.id,  text_get_name)
            dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)
        elif state == config.States.S_ENTER_NAME.value:
            bot.send_message(message.chat.id,  'введите имя')
        elif state == config.States.S_ENTER_TIME.value:
            bot.send_message(message.chat.id,  'введите время')
        elif state == config.States.S_ENTER_FINAL.value:
            final_create(message)
        else:
            bot.send_message(message.chat.id,  text_get_name)
            dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)
        
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "clear")
    dbworker.set_state(message.chat.id, config.States.S_START.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value) #1!
def get_name(message):
    '''get name if exist, set next step - get time'''
    name = message.text.strip()
    #sleep(1)
    #name = name.strip()
    dbworker.set_state(message.chat.id, config.States.S_ENTER_TIME.value) #set 2
    print('set2!')
    dbworker.save_name('name',  name)
    print('я есть имя: ',  name)
    #dbworker.save_name(message.chat.id,  name)
    bot.send_message(message.chat.id,  text_get_time)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_TIME.value)#2!
def get_time(message):
     '''get time from user to poweroff'''
     #bot.send_message(message.chat.id,  text_get_time)
     time_user = message.text.strip()
     #time_user = time_user.strip()
     #time_user = str(time_user)
     dbworker.save_time('time',  time_user)
     print('я есть время: ',  time_user)
     #dbworker.save_time(message.chat.id,  time_user)
     print('ща поставлю финал!')
     dbworker.set_state(message.chat.id, config.States.S_ENTER_FINAL.value)
     print('поставил финал')
     print(message.chat.id)
     bot.send_message(message.chat.id, 'отправьте любой символ для подтверждения создания.')
  
     

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_FINAL.value)#3
def final_create(message):
    bot.send_message(message.chat.id,  text_final)
    name = dbworker.get_name('name')
    print('получил наме из базы')
    time_to_off = dbworker.get_time()
    print('получил тайм из базы')
    if time_to_off == False:
        print("не, не получил")
    print('я имя!',  name)
    print('я время',  time_to_off)
    a = api_test3.create_vpn_user(name,  int(time_to_off))
    b = a['name']
    b = str(b)
    c = a['password']
    c = str(c)
    d = 'логин ' + b  + ' пароль ' + c
    bot.send_message(message.chat.id,  d)
    dbworker.set_state(message.chat.id, config.States.S_START.value)

#delete user vpn
@bot.message_handler(regexp = 'удалить')
def delete_name(message):
    '''просим имя'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        state = dbworker.get_current_state(message.chat.id)
        if state == config.States.S_START.value:
            bot.send_message(message.chat.id,  'введите имя удаляемого пользователя')
            dbworker.set_state(message.chat.id,  config.States.delete_del.value)
        elif state == config.States.delete_del.value:
            bot.send_message(message.chat.id,  'у вас есть неудаленный пользователь. продолжите \
            удаление или выполните команду /reset для отмены.')
        else:
            dbworker.set_state(message.chat.id,  config.States.S_START.value)
            bot.send_message(message.chat.id,  'что то пошло не так, я вернулся к исходному состоянию.\
            начните всё с начала.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
        
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.delete_del.value)
def delete_name2(message):
    """берем имя и удаляем"""
    name = message.text.strip()
    from create_database import user_exist
    a = user_exist(name)
    if a == False:
        bot.send_message(message.chat.id, 'увы, такого пользователя нет. проверьте имя на опечатки, и повторите ввод.')
    elif a == True:
        from api_test3 import remove_vpn_user
        dbworker.set_state(message.chat.id,  config.States.S_START.value)
        a = remove_vpn_user(name)

        from api_test3 import close_connection
        close_connection(name)
        from create_database import delete_user_from_database
        delete_user_from_database(name)
        bot.send_message(message.chat.id, 'пользователь удален')


#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()

        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#enable user vpn
@bot.message_handler(regexp = 'разрешить')
def enable_user(message):
    """берет имя, которое надо разрешить"""
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        state = dbworker.get_current_state(message.chat.id)
        if state == config.States.S_START.value:
            bot.send_message(message.chat.id,  'введите имя разрешаемого пользователя')
            dbworker.set_state(message.chat.id,  config.States.enable_get.value)
        elif state == config.States.enable_get.value:
            bot.send_message(message.chat.id,  'вы начали разрешать пользователя, но не завершили\
            завершите разрешение, или сбросьте все командой /reset')
        else:
            bot.send_message(message.chat.id,  'что то пошло не так, я сбросил все к началу.')
            dbworker.set_state(message.chat.id,  config.States.S_START.value)
    else:
        bot.send_message(message.chat.id, text_no_id)
            
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.enable_get.value)
def enable_user2(message):
    """разрешает это имя."""
    name = message.text.strip()
    print(name)
    from create_database import user_exist
    a = user_exist(name)
    print(a)
    if a == False:
        bot.send_message(message.chat.id, 'увы, такого пользователя нет. проверьте имя на опечатки, и повторите ввод.')
    elif a == True:
        from api_test3 import enable_vpn_user
        b = enable_vpn_user(name)
        if b == True:
            bot.send_message(message.chat.id,  'пользователь разрешен')
        else:
            bot.send_message(message.chat.id,  'на роутере нет такого пользователя. обратитесь к администратору')

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(regexp = 'добавить')
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass


@bot.message_handler(regexp = 'подключенные')
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(regexp='список')
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    bot.send_message(message.chat.id, 'есть следующие администраторы:')
    for i in a:
        t1 = i[0]
        t2 = i[1]
        t3 = 'админ ' + t1 + ' с уровнем доступа ' + str(t2)
        bot.send_message(message.chat.id, t3)


#add extra time
@bot.message_handler(regexp = 'продлить')
def add_extra_time(message):
    """запрашивает первый аргумент"""
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_START.value:
        bot.send_message(message.chat.id, 'введите имя пользователя, которому требуется \
        дать дополнительное время.')
        dbworker.set_state(message.chat.id, config.States.add_time_name.value)
    elif state == config.States.add_time_name.value:
        bot.send_message(message.chat.id,  'у вас есть пользователь с непродленным \
        временем. введите его имя, либо выполните /reset')
    elif state == config.States.add_time_time.value:
        bot.send_message(message.chat.id,  'у вас есть пользователь, имя которого введено, но время не продлено.\
        укажите время в часах, цифрами')
    else:
        pass
        
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.add_time_name.value)
def add_extra_time2(message):
    """берет имя, запрашивает время"""
    name = message.text.strip()
    from create_database import user_exist
    a = user_exist(name)
    dbworker.save_name('name_from_add_time', name)
    if a == False:
        bot.send_message(message.chat.id, 'увы, такого пользователя нет. проверьте имя на опечатки, и повторите ввод.')
    elif a == True:
        bot.send_message(message.chat.id,  'введите время, на которое нужно продлить сеанс пользователя.\
        указывайте время цифрами, в часах.')
        dbworker.set_state(message.chat.id,  config.States.add_time_time.value)        
    else:
        bot.send_message(message.chat.id,  'вы не должны были здесь оказаться. обратитесь к администратору.')
 
@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.add_time_time.value) 
def add_extra_time3(message):
    """'это берет время, на которое надо продлить, и продляет."""
    duration = message.text.strip()
    if duration.isdigit() == True:
        bot.send_message(message.chat.id,  'ок, добавляю время.') #!!проверять на -!!
        dbworker.set_state(message.chat.id,  config.States.S_START.value)
        #взять имя из бд
        from create_database import add_time2
        username = dbworker.get_name('name_from_add_time')
        a = add_time2(username,  duration)
        if a == True:
            bot.send_message(message.chat.id,  'время добавлено успешно')
        elif a == False:
            bot.send_message(message.chat.id,  'что то пошло не так, не добавлено')
        else:
            bot.send_message(message.chat.id,  'что то пошло не так. обратитесь к администратору.')
        #если тру - ок, продлено
    else:
        bot.send_message(message.chat.id,  'увы, это не число. Введите, пожалуйста, число.')
        
#return info (left_time) from user
@bot.message_handler(regexp = 'информация')
def my_time(message):
    '''this function print left time'''
    state = dbworker.get_current_state(message.chat.id)
    if state == config.States.S_START.value:
        bot.send_message(message.chat.id,  'введите имя пользователя, информацию о котором нужно получить.')
        dbworker.set_state(message.chat.id, config.States.USER_INFO_GET.value)
    elif state == config.States.USER_INFO_GET.value:
        bot.send_message(message.chat.id, 'введите имя.')
    else:
        bot.send_message(message.chat.id,  'введите имя пользователя, информацию о котором нужно получить.')
        dbworker.set_state(message.chat.id, config.States.USER_INFO_GET.value)
   

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.USER_INFO_GET.value)
def send_info(message):
    '''send info to chat'''
    from api_test3 import time_left
    a = time_left(message.text)
    #print(type(a))
    if a < 0:
        bot.send_message(message.chat.id,  'ваше время истекло.')
        dbworker.set_state(message.chat.id,  config.States.S_START.value)
    elif a > 0:
        c = a / 60
        c = int(c)
        c = str(c)
        b = 'осталось ' + c + ' минут(ы)' #??
        bot.send_message(message.chat.id, b)
        dbworker.set_state(message.chat.id,  config.States.S_START.value)
    elif a == False:
        bot.send_message(message.chat.id,  'увы, такого пользователя нет. Проверьте имя на опечатки, и введите еще раз.')
    else:
        bot.send_message(message.chat.id,  'вы не должны были здесь оказаться. \
        что то пошло не так. сообщите об этом администратору.')



# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()
sleep(3)

# set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

# start cherrypy server
cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})


File: /config_example.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config_example.py

login = 'admin_login'
password = 'admin_password'
host = 'ip or dns from your miktotik'
token = 'token your bot'
bot_admin_password = 'password from first authorization admin-user in bot'

#set environment from web hooks
WEBHOOK_HOST = '138.201.174.71' #set your ip or fqdn
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port open!)
WEBHOOK_LISTEN = '0.0.0.0'  # from any server (not all) == ip up

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # path to certificat
WEBHOOK_SSL_PRIV = 'webhook_key.pem'  # path to privat key


File: /create_cert.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  create_cert.py
#
#  Copyright 2018 Roman <rk@staffcop.ru>

from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join
from datetime import datetime, timedelta
import requests

internal_ip = requests.get('http://ipinfo.io').json()
internal_ip2 = internal_ip.get('ip')

CN = 'webhook'
CERT_FILE = "%s.crt" % CN
KEY_FILE = "%s.key" % CN
#now    = datetime.now()
#expire = now + timedelta(days=365)


def create_self_signed_cert(cert_dir="."):
    C_F = join(cert_dir, CERT_FILE)
    K_F = join(cert_dir, KEY_FILE)
    if not exists(C_F) or not exists(K_F):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)
        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "RU"
        cert.get_subject().ST = "Russland"
        cert.get_subject().L = "Nsk"
        cert.get_subject().O = "Home"
        cert.get_subject().OU = "Sofa"
        cert.get_subject().CN = internal_ip2
        cert.get_subject().emailAddress = 'namor925@gmail.com'
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(315360000)
        #cert.set_notBefore(now.strftime("%Y%m%d%H%M%SZ").encode())
        #cert.set_notAfter(expire.strftime("%Y%m%d%H%M%SZ").encode())
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')
        with open(C_F, "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            '''
            a = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
            b = a.encode('utf-8')
            print(a)
            print(type(a))
            '''
        with open(K_F, "wb") as ff:
            ff.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        print('generation success!')
    else:
        print('keys exists!')

create_self_signed_cert()


File: /create_database.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sqlite3


#db = SqliteDatabase('database.sql')
#db = ('database.sql')

#table description
db = 'database.sql'

def create_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE vpn_user (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT,
    date_create int NOT NULL,
    date_off int NOT NULL,
    username_telegram text
    )
    ''')
    
    cursor.execute('''CREATE TABLE bot (
    id INTEGER PRIMARY KEY,
    username_telegram TEXT NOT NULL UNIQUE,
    level int NOT NULL
    )
    ''')
    conn.close()

#db file - is exists?
file_path = 'database.sql'
if os.access(file_path, os.F_OK) == True:
    pass
else:
    create_db()


#first auth
def add_admin(password, username):
    from config import bot_admin_password
    if password == bot_admin_password:
        conn = sqlite3.connect('database.sql')
        cursor = conn.cursor()
        cursor.execute("SELECT username_telegram FROM bot WHERE username_telegram = ?", (username,))
        b = cursor.fetchall()
        if len(b) == 0:
            cursor.execute("INSERT INTO bot (username_telegram, level) VALUES (?, 0)", (username, ))
            conn.commit()
            return True
        else:
            pass
            return False
    else:
        return False


#who poweroff?
def who_poweroff():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM vpn_user WHERE date_off <= strftime('%s', 'now')")
    result = cursor.fetchall()
    conn.close()
    return result

#time to poweroff
def time_to_poweroff(username):
    ''' this function shows the time remaining before the trip.'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT date_off FROM vpn_user WHERE username = ?",  (username,  ))
    b = cursor.fetchone()
    print(b)
    print(type(b))
    return b
    
#whois?
def whois(username):
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram, level FROM bot WHERE username_telegram = ?", (username,))
    results = cursor.fetchone()
    #print(results)
    #print(type(results))
    #print(type(results))
    if results == None:
        pass
        auth = False
        level = 5
        return auth,  level
    else:
        if len(results) == 0:
            auth = False
            return auth
        elif results == None:
            auth = False
            return auth
        else:
            #print(results[1])
            auth = True
            level = results[1]
            return auth, level
    conn.close

#add admin bot user
def add_admin_mikrotik(username_telegram, level):
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram FROM bot WHERE username_telegram = ?", (username_telegram,))
    b = cursor.fetchall()
    if len(b) == 0:
        cursor.execute("INSERT INTO bot (username_telegram, level) VALUES (?, ?)", (username_telegram, level))
        #print(username_telegram)
        conn.commit()
        success = True
        #return success
    else:
        success = False
        pass
    conn.close

    return success

#list all admins
def list_all_admins():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram, level FROM Bot")
    results = cursor.fetchall()
    conn.close
    #print(results)
    return results

#added user name and create_data and pass in database
def add_user_in_database(name, duration=3600):
    #from duration import date_off
    from add_time import add_data2
    #off = date_off()
    data = add_data2(duration)
    date_create = data[0]
    date_off = data[1]
    
    conn = sqlite3.connect('database.sql', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vpn_user (username, date_create, date_off) VALUES (?, ?, ?)", (name, date_create, date_off))
    
    conn.commit()
    success = True
    conn.close
    return success

def user_exist(name):
    """this user name - exist?"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM vpn_user WHERE username = ?", (name, ))
    a = cursor.fetchone()
    conn.close()
    if a == None:
        return False
    else:
        return True

def add_time2(username,  duration):
    """this function added extra time from select user"""
    if user_exist(username) == True:
        from add_time import add_data2
        data = add_data2(duration)
        date_create = data[0]
        date_off = data[1]
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("UPDATE vpn_user SET date_create = ?, date_off = ? WHERE username = ?", (date_create, date_off, username) )
        conn.commit()
        return True
    else:
        return False
#whois(admin_id)

#delete vpn_user from database
def delete_user_from_database(name):
    """delete user from database"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vpn_user WHERE username = ?",  (name, ))
    cursor.fetchone()
    conn.commit()
    conn.close()
    #a = user_exist(name)


File: /create_mit_name.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def create_mit_name(text):
    a = text.strip() #this is make in function on bot
    b = re.sub(r'\s+',  ' ',  a)
    c = b.split(' ')
    duration = 3600
    vpn_name = ' '
    for i in c:
        if i.isdigit() == True:
            duration = i
        else:
            vpn_name = i
    return vpn_name,  duration


File: /dbworker.py
# -*- coding: utf-8 -*-

from vedis import Vedis
import config


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id]
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.S_START.value  # значение по умолчанию - начало диалога


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False

#save name
def save_name(name,  value):
    with Vedis(config.db_file) as db:
        try:
            name = db.set(name,  value)
            name.add(value)
            return True
        except:
            return False

#get name
def get_name(user_name):
    with Vedis(config.db_file) as db:
        try:
            return db.get(user_name)
        except KeyError:
            return False

#save time
def save_time(time,  value):
    with Vedis(config.db_file) as db:
        try:
            name = db.set(time,  value)
            name.add(value)
            return True
        except:
            return False

#get time
def get_time(time = 'time'):
    with Vedis(config.db_file) as db:
        try:
            return db.get(time)
        except:
            return False


File: /duration.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  duration.py
#  
#  Copyright 2018 Roman <namor925@gmail.com>

from datetime import datetime, timedelta

def date_off(duration=1):
    date_create = datetime.now()
    #date_create = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    if duration == None:
        #delta = 'время не задано. задайте время.'
        pass
    elif duration == 0:
        delta = timedelta(hours=1)
    else:
        delta = timedelta(hours=duration)
    #print(delta)
    date_off = date_create + delta
    #print(date_off)
    return date_create.strftime("%Y.%m.%d %H:%M:%S"), date_off.strftime("%Y.%m.%d %H:%M:%S")
    


File: /generation_name2.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name2.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#from generation name

from mimesis import Food
food = Food('en')

def create_name():
    a = food.drink()
    #print(a)
    return a



File: /generation_pass.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_pass.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#  


from random import choice
from string import ascii_letters

def create_password():
    passw = ''.join(choice(ascii_letters) for i in range(12))
    #print(passw)
    return passw

#create_password()


File: /master\add_time.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

def add_data2(username,  duration=3600):
    date_create = time()
    date_create = int(date_create)
    date_off = date_create + duration
    return date_create,  date_off

'''
def who_poweroff():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM t WHERE date_off <= strftime('%s', 'now')")
    result = cursor.fetchall()
    return result
'''


File: /master\api_test3.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_api3.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#  
import ssl
from librouteros import connect
#from pprint import pprint
import os
#from datetime import datetime
from time import time

# check conf file
if os.access('config.py', os.F_OK) == True:
    import config
else:
    print('no config file! EXIT')
    print('please, create config.py, added to login, password and ip or dns  \
    your router')
    exit()

# connect to mikrotik
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ctx.set_ciphers('RSA')
api = connect(username = config.login, password = config.password, host = config.host, ssl_wrapper=ctx.wrap_socket, port=8729)


# total count user vpn
def list_count_vpn_user():
    users = api(cmd='/ppp/secret/print')
    count_users = len(users)
    return count_users


# names all users vpn
def list_vpn_user_name():
    users = api(cmd='/ppp/secret/print')
    names = []
    for i in users:
        names.append(i['name'])
    return names



#count activity user vpn
def list_count_activity_vpn_user():
    users = api(cmd='/ppp/secret/print')
    i = 0
    for name in users:
        if name['disabled'] == False:
            i = i +1
    #return i
    count = i
    return count
    

#name activity user vpn
def list_vpn_active_user():
    users = api(cmd='/ppp/secret/print')
    names = []
    for i in users:
        if i['disabled'] == False:
            names.append(i['name'])
            #print(i['name'])
        else:
            pass
    return names

#close active conection from select user
def close_connection(name_input):
    '''this function close active connect'''
    connect = api(cmd='/ppp/active/print')
    if len(connect) != 0:
        
        params = {}
        for i in connect:
            if i['name'] == name_input:
                name_id = i['.id']
                params['.id'] = name_id
                api(cmd='/ppp/active/remove', **params)
                return True
            else:
                pass
    else:
        pass
        

#disable user vpn
def disable_vpn_user(name_input):
    ''' this function disable user, if exists'''
    users = api(cmd='/ppp/secret/print')
    params = {'disabled' : True}
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/set', **params)
            result = True
            return result
        else:
            pass
            
    #!!! close session if exists
    api(cmd='/ppp/secret/set', **params)
    #api.close
    

#enable user vpn
def enable_vpn_user(name_input):
    users = api(cmd='/ppp/secret/print')
    params = {'disabled' : False, '.id' : name_input}
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/set', **params)
            #print('user enable!')
            result = True
            return result
        else:
            pass

#user vpn status
def user_vpn_status(name_input):
    pass
    
#remove user vpn 
def remove_vpn_user(name_input):
    users = api(cmd='/ppp/secret/print')
    params = {}
    
    for i in users:
        if i['name'] == name_input:
            name_id = i['.id']
            params['.id'] = name_id
            api(cmd='/ppp/secret/remove', **params)
            #print('yes! remove!!')
            remove = True
            return remove
        else:
            #print('user not exist')
            pass
    

#create user vpn
def create_vpn_user(vpn_name = '',  duration=3600):
    #users = api(cmd='/ppp/secret/print')
    params = {'profile' : 'default', 'service' : 'pptp'}
    import generation_pass
    vpn_pass = generation_pass.create_password()
    print(vpn_name)
    if len(vpn_name) == 0:
        import generation_name2
        vpn_name = generation_name2.create_name()
    else:
        vpn_name = vpn_name
    
    params['name'] = vpn_name
    params['password'] = vpn_pass
    api(cmd='/ppp/secret/add', **params)
    #from create_database import add_user_in_database
    #add_user_in_database(vpn_name)
    from add_time import add_data2
    add_data2(vpn_name,  duration)
    #date_create = a[0]
    #date_off = a[1]
    from create_database import add_user_in_database
    add_user_in_database(vpn_name,  duration)
    '''
    from duration import date_off
    print(delta)
    date_off(delta)
    '''
    return params


#list profile print
def list_profile():
    profile = api(cmd='/ppp/profile/print')
    return profile
    #pprint(profile)

#list active connections
def list_active_connections():
    connections = api(cmd='/ppp/active/print')
    conn = []
    #print(type(conn))
    for i in connections:
        conn.append(i)
    #print(type(conn))
    #print(connections)
    return connections
 
#time left
def time_left(username):
     '''this function retunr left time'''
     from create_database import time_to_poweroff
     a = time_to_poweroff(username)
     if a == None:
         pass
         time_left1 = 0
         return time_left1
     else:
         date_off = a[0]
         date_real = time()
         time_left1 = date_off - int(date_real)
         print('я из апи',  time_left1)
         return time_left1
         
     
#create new profile with fixed time


File: /master\bot.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
import config
from telebot import types
import logging
import api_test3
from create_database import whois
import re
import flask
from time  import sleep

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'увы, я тебя не знаю.'

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    #markup = types.InlineKeyboardMarkup()
    #btn_key_help = types.InlineKeyboardButton(text='start')
    #markup.add(btn_key_help)
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(commands=['count'])
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list'])
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        b = str(a)
        bot.send_message(message.chat.id, b)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text

#create new user vpn
@bot.message_handler(commands=['create'])
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    #print('я твое имя', au)
    if au[0] == True and au[1] <= 1:
        text = message.text[7:]
        text = text.strip()
        from generation_name2 import create_name
        zero_name = create_name()
        #print('я голый текст')
        if text == None:
            duration = 3600
        elif text.isdigit() == True:
            #print('это же число!')
            if text == 0:
                duration = 3600
            else:
                duration = int(text) * 3600
        elif len(text) == 0:
            duration = 3600
        else:
            #print('не поверишь, но ты тут')
            #add create_mit_name
            from create_mit_name import create_mit_name
            #print('а я текст который прилетит',  text)
            row_name = create_mit_name(text)
            #print('я есть полученный текст в мит',  row_name)
            #print(type(row_name))
            
            duration = row_name[1]
            duration = int(duration)
            #print('я дуратион,',   duration,  'мой тип',  type(duration))
            zero_name = row_name[0]
            #print('я зеро нейм',  zero_name)
            bot.send_message(message.chat.id, 'пробуем принять имя')
            #exit()
        
        #zero_name = ''
        a = api_test3.create_vpn_user(zero_name,  duration)
        b = a['name']
        b = str(b)
        #print('имя',  b)
        #print(type(b))
        c = a['password']
        c = str(c)
        #print(b)
        #print(c)
        d = 'логин ' + b + ' пароль ' + c
        bot.send_message(message.chat.id, d)
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass
    
    
    
    #print(text, 'это сырое число')
    

        
    #text = int(text)
    #print(text)


#delete user vpn
@bot.message_handler(commands=['delete'])
def delete_name(message):
    '''this function delete vpn user if exist'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        #print('в смысле нот тайп',  text)
        text = text.strip()
        a = api_test3.remove_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь удален')
        else:
            bot.send_message(message.chat.id, 'увы, такого пользователя нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()
        
        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
        
#enable user vpn
@bot.message_handler(commands=['enable'])
def enable_user(message):
    '''this function enable vpn user, if er exist'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        text = text.strip()

        a = api_test3.enable_vpn_user(text)
        if a == True:
            bot.send_message(message.chat.id, 'пользователь разрешен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого разрешать.')

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
    

@bot.message_handler(commands=['list_connect'])
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list_admins'])
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    b = str(a)
    bot.send_message(message.chat.id, b)
    #add humanize view

@bot.message_handler(commands=['my_time'])
def my_time(message):
    '''this function print left time'''
    from api_test3 import time_left
    text = get_name_u(message, 8) #тут влетает 'имя не указано, удалять нечего' из get_name_u
    #print('я текст из май тайм',  text)
    if text == None:
        bot.send_message(message.chat.id,  'не указано имя, показывать нечего')
        exit()
    else:
        text = text.strip()
    
    a = time_left(text)
    print(a)
    #a = a[0]
    if a > 0:
        time_o = a / 60
        time_o = int(time_o)
        time_o = str(time_o) + ' минут осталось'
    else:
        time_o = 'ваше время истекло'
    
    bot.send_message(message.chat.id, time_o)

bot.pulling(none_stop=True)


File: /master\bot_web_hook.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
import config
from telebot import types
import logging
import api_test3
from create_database import whois
import re
import flask
from time  import sleep

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

#set environment from web hooks
WEBHOOK_HOST = '138.201.174.71'
WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_key.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

bot = telebot.TeleBot(config.token)

app = flask.Flask(__name__)

#Empty webserver index, return nothing, just http 200
@app.route('/',  methods=['GET',  'HEAD'])
def index():
    return ''
    
# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'увы, я тебя не знаю.'

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    #markup = types.InlineKeyboardMarkup()
    #btn_key_help = types.InlineKeyboardButton(text='start')
    #markup.add(btn_key_help)
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(commands=['count'])
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list'])
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        b = str(a)
        bot.send_message(message.chat.id, b)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text

#create new user vpn
@bot.message_handler(commands=['create'])
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    #print('я твое имя', au)
    if au[0] == True and au[1] <= 1:
        text = message.text[7:]
        text = text.strip()
        from generation_name2 import create_name
        zero_name = create_name()
        #print('я голый текст')
        if text == None:
            duration = 3600
        elif text.isdigit() == True:
            #print('это же число!')
            if text == 0:
                duration = 3600
            else:
                duration = int(text) * 3600
        elif len(text) == 0:
            duration = 3600
        else:
            #print('не поверишь, но ты тут')
            #add create_mit_name
            from create_mit_name import create_mit_name
            #print('а я текст который прилетит',  text)
            row_name = create_mit_name(text)
            #print('я есть полученный текст в мит',  row_name)
            #print(type(row_name))
            
            duration = row_name[1]
            duration = int(duration)
            #print('я дуратион,',   duration,  'мой тип',  type(duration))
            zero_name = row_name[0]
            #print('я зеро нейм',  zero_name)
            bot.send_message(message.chat.id, 'пробуем принять имя')
            #exit()
        
        #zero_name = ''
        a = api_test3.create_vpn_user(zero_name,  duration)
        b = a['name']
        b = str(b)
        #print('имя',  b)
        #print(type(b))
        c = a['password']
        c = str(c)
        #print(b)
        #print(c)
        d = 'логин ' + b + ' пароль ' + c
        bot.send_message(message.chat.id, d)
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass
    
    
    
    #print(text, 'это сырое число')
    

        
    #text = int(text)
    #print(text)


#delete user vpn
@bot.message_handler(commands=['delete'])
def delete_name(message):
    '''this function delete vpn user if exist'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        #print('в смысле нот тайп',  text)
        text = text.strip()
        a = api_test3.remove_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь удален')
        else:
            bot.send_message(message.chat.id, 'увы, такого пользователя нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()
        
        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
        
#enable user vpn
@bot.message_handler(commands=['enable'])
def enable_user(message):
    '''this function enable vpn user, if er exist'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        text = text.strip()

        a = api_test3.enable_vpn_user(text)
        if a == True:
            bot.send_message(message.chat.id, 'пользователь разрешен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого разрешать.')

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass
    

@bot.message_handler(commands=['list_connect'])
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list_admins'])
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    b = str(a)
    bot.send_message(message.chat.id, b)
    #add humanize view

@bot.message_handler(commands=['my_time'])
def my_time(message):
    '''this function print left time'''
    from api_test3 import time_left
    text = get_name_u(message, 8) #тут влетает 'имя не указано, удалять нечего' из get_name_u
    #print('я текст из май тайм',  text)
    if text == None:
        bot.send_message(message.chat.id,  'не указано имя, показывать нечего')
        exit()
    else:
        text = text.strip()
    
    a = time_left(text)
    print(a)
    #a = a[0]
    if a > 0:
        time_o = a / 60
        time_o = int(time_o)
        time_o = str(time_o) + ' минут осталось'
    else:
        time_o = 'ваше время истекло'
    
    bot.send_message(message.chat.id, time_o)

# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()
sleep(5)

# set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))
                

# start flask server
app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT, ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV), debug=True)


File: /master\bot_web_hook_cherry.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name.py
#
#  Copyright 2018 Roman <roman@roman-home>
#test bot from my mikrotik

import telebot
from telebot import types
import logging
import api_test3
from create_database import whois
import re
from time  import sleep
import cherrypy
from os import getpid
import os

#loggin in console
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


# check cert files if not - create
filename = 'webhook.crt'
if os.access(filename, os.F_OK) == True:
    pass
else:
    from create_cert import create_self_signed_cert
    create_self_signed_cert()

#create pid file
your_pid = getpid()
your_pid = str(your_pid)
pid_file = '/tmp/bot.pid'
with open (pid_file,  'w',  encoding='utf-8') as ff:
    ff.write(your_pid)

#set environment from web hooks
#WEBHOOK_HOST = '138.201.174.71'
import config
WEBHOOK_PORT = config.WEBHOOK_PORT  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = config.WEBHOOK_LISTEN

WEBHOOK_SSL_CERT = config.WEBHOOK_SSL_CERT  # Путь к сертификату
WEBHOOK_SSL_PRIV = config.WEBHOOK_SSL_PRIV  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (config.WEBHOOK_HOST, config.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

bot = telebot.TeleBot(config.token)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)

# event handling from keyboard
text_help = '/count - количество юзеров, всего; \n /count_a - активных юзеров; \n \
/list - показать имена всех; \n /list_a - показать имена активных; \n /create - создать нового юзера \n \
/delete - удалить юзера \n /disable - запретить юзера; \n /enable - разрешить юзера \n /add_admin - добавить нового администратора \n \
/list_connect - кто подключен сейчас? \n /list_admins - список админов \n /my_time - сколько осталось времени? \n '

text_no_id = 'увы, я тебя не знаю.'

@bot.message_handler(commands=['help'])
def help_for_bot(message):
    #markup = types.InlineKeyboardMarkup()
    #btn_key_help = types.InlineKeyboardButton(text='start')
    #markup.add(btn_key_help)
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        bot.send_message(message.chat.id, text_help)
    else:
        bot.send_message(message.chat.id, text_no_id)


@bot.message_handler(commands=['count'])
def count_all_user(message):
    a = whois(message.chat.username)
    if a[0] == True and a[1] <= 1:
        a = api_test3.list_count_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

        #bot.send_message(message.chat.id, text_help)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['count_a'])
def count_active_user(message):
    '''thi function print all count vpn user'''
    au = whois(message.chat.username)
    print(au)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_count_activity_vpn_user()
        b = str(a)
        bot.send_message(message.chat.id, b)

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list'])
def send_list_vpn_user_name(message):
    ''' this function list all user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_user_name()
        b = str(a)
        bot.send_message(message.chat.id, b)
    elif au[0] == False:
        bot.send_message(message.chat.id, text_no_id)
        pass
    else:
        pass

@bot.message_handler(commands=['list_a'])
def send_list_active_vpn_user(message):
    '''this command print list all active user vpn'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_vpn_active_user()
        b = str(a)
        bot.send_message(message.chat.id, b)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#internal get name, experimental
def get_name_u(message, shear):
    '''this function for get name from next command'''
    text = message.text[shear:]
    if len(text) == 0:
        bot.send_message(message.chat.id, 'имя не задано. некого удалять.')
    elif len(text) >= 50:
        bot.send_message(message.chat.id, 'очень много букаф. не могу понять. пожалуйста, короче.')
    else:
        return text

#create new user vpn
@bot.message_handler(commands=['create'])
def create_user(message):
    '''this function create new user vpn, set random name - cocteil
    and generation password. send it in chat'''
    au = whois(message.chat.username)
    #print('я твое имя', au)
    if au[0] == True and au[1] <= 1:
        text = message.text[7:]
        text = text.strip()
        from generation_name2 import create_name
        zero_name = create_name()
        #print('я голый текст')
        if text == None:
            duration = 3600
        elif text.isdigit() == True:
            #print('это же число!')
            if text == 0:
                duration = 3600
            else:
                duration = int(text) * 3600
        elif len(text) == 0:
            duration = 3600
        else:
            #print('не поверишь, но ты тут')
            #add create_mit_name
            from create_mit_name import create_mit_name
            #print('а я текст который прилетит',  text)
            row_name = create_mit_name(text)
            #print('я есть полученный текст в мит',  row_name)
            #print(type(row_name))

            duration = row_name[1]
            duration = int(duration)
            #print('я дуратион,',   duration,  'мой тип',  type(duration))
            zero_name = row_name[0]
            #print('я зеро нейм',  zero_name)
            bot.send_message(message.chat.id, 'пробуем принять имя')
            #exit()

        #zero_name = ''
        a = api_test3.create_vpn_user(zero_name,  duration)
        b = a['name']
        b = str(b)
        #print('имя',  b)
        #print(type(b))
        c = a['password']
        c = str(c)
        #print(b)
        #print(c)
        d = 'логин ' + b + ' пароль ' + c
        bot.send_message(message.chat.id, d)
    else:
        bot.send_message(message.chat.id, 'что то не то с правами. не буду создавать')
        pass



    #print(text, 'это сырое число')



    #text = int(text)
    #print(text)


#delete user vpn
@bot.message_handler(commands=['delete'])
def delete_name(message):
    '''this function delete vpn user if exist'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        #print('в смысле нот тайп',  text)
        text = text.strip()
        a = api_test3.remove_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь удален')
        else:
            bot.send_message(message.chat.id, 'увы, такого пользователя нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#def reset active connect from select user vpn

#disable user vpn
@bot.message_handler(commands=['disable'])
def disable_user(message):
    au  = whois(message.chat.username)
    '''this function disable vpn user, if exist'''
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 8)
        text = text.strip()

        a = api_test3.disable_vpn_user(text)
        if a == True:
            from api_test3 import close_connection
            close_connection(text)
            bot.send_message(message.chat.id, 'пользователь запрещен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого запрещать.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#enable user vpn
@bot.message_handler(commands=['enable'])
def enable_user(message):
    '''this function enable vpn user, if er exist'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        text = get_name_u(message, 7)
        text = text.strip()

        a = api_test3.enable_vpn_user(text)
        if a == True:
            bot.send_message(message.chat.id, 'пользователь разрешен.')
        else:
            bot.send_message(message.chat.id, 'нет такого пользователя. некого разрешать.')

    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

#first auth
#telegram_id = message.chat.id

@bot.message_handler(commands=['auth'])
def auth_admin(message):
    '''this function adds the first administrator'''
    password = message.text[5:]
    if len(password) == 0:
        bot.send_message(message.chat.id, 'не вижу пароля. не пущу.')
    else:
        from create_database import add_admin
        password = password.strip()
        a = add_admin(password, message.chat.username)
        if a == True:
            bot.send_message(message.chat.id,  'администратор добавлен')
        else:
            bot.send_message(message.chat.id,  'увы, я никого не добавил')
        #print(password,  message.chat.username)
        #print(type(message.chat.username))

@bot.message_handler(commands=['add_admin'])
def add_admin(message):
    '''this function add new admin from bot'''
    au = whois(message.chat.username)
    if au[0] == True and au[1] <= 0:
        raw_name = message.text[10:]
        raw_name2 = raw_name.strip()
        raw_name3 = re.sub(r'\s+', ' ', raw_name2)
        #raw_name4 = raw_name3.split(' ') #if mane str - many elements in corteg
        name_level = raw_name3.split(' ')
        #print(len(name_level))
        if len(name_level) == 2:
            name = name_level[0]
            level = name_level[1]
        else:
            bot.send_message(message.chat.id,  'нужно указать телеграм-нейм нового админа и его левел')
            exit()
        from create_database import add_admin_mikrotik
        result = add_admin_mikrotik(name, level)
        if result == True:
            text = 'новый администратор успешно создан'
            bot.send_message(message.chat.id, text)
        else:
            text = 'такой админ уже есть.'
            bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass


@bot.message_handler(commands=['list_connect'])
def list_connect(message):
    '''this function print list all active vpn connection. no arguments'''
    au  = whois(message.chat.username)
    if au[0] == True and au[1] <= 1:
        a = api_test3.list_active_connections()
        b = str(a)
        if len(a) != 0:
            bot.send_message(message.chat.id,  b)
        else:
            bot.send_message(message.chat.id, 'активных соединений нет.')
    else:
        bot.send_message(message.chat.id, text_no_id)
        pass

@bot.message_handler(commands=['list_admins'])
def list_admins(message):
    '''this function print list all admins bot'''
    from create_database import list_all_admins
    a = list_all_admins()
    b = str(a)
    bot.send_message(message.chat.id, b)
    #add humanize view

@bot.message_handler(commands=['my_time'])
def my_time(message):
    '''this function print left time'''
    from api_test3 import time_left
    text = get_name_u(message, 8) #тут влетает 'имя не указано, удалять нечего' из get_name_u
    #print('я текст из май тайм',  text)
    if text == None:
        bot.send_message(message.chat.id,  'не указано имя, показывать нечего')
        exit()
    else:
        text = text.strip()

    a = time_left(text)
    print(a)
    #a = a[0]
    if a > 0:
        time_o = a / 60
        time_o = int(time_o)
        time_o = str(time_o) + ' минут осталось'
    else:
        time_o = 'ваше время истекло'

    bot.send_message(message.chat.id, time_o)

# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()
sleep(3)

# set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

# start cherrypy server
cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})


File: /master\config_example.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config_example.py

login = 'admin_login'
password = 'admin_password'
host = 'ip or dns from your miktotik'
token = 'token your bot'
bot_admin_password = 'password from first authorization admin-user in bot'

#set environment from web hooks
WEBHOOK_HOST = '138.201.174.71' #set your ip or fqdn
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port open!)
WEBHOOK_LISTEN = '0.0.0.0'  # from any server (not all) == ip up

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # path to certificat
WEBHOOK_SSL_PRIV = 'webhook_key.pem'  # path to privat key


File: /master\create_cert.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  create_cert.py
#
#  Copyright 2018 Roman <rk@staffcop.ru>

from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join
from datetime import datetime, timedelta
import requests

internal_ip = requests.get('http://ipinfo.io').json()
internal_ip2 = internal_ip.get('ip')

CN = 'webhook'
CERT_FILE = "%s.crt" % CN
KEY_FILE = "%s.key" % CN
#now    = datetime.now()
#expire = now + timedelta(days=365)


def create_self_signed_cert(cert_dir="."):
    C_F = join(cert_dir, CERT_FILE)
    K_F = join(cert_dir, KEY_FILE)
    if not exists(C_F) or not exists(K_F):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)
        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "RU"
        cert.get_subject().ST = "Russland"
        cert.get_subject().L = "Nsk"
        cert.get_subject().O = "Home"
        cert.get_subject().OU = "Sofa"
        cert.get_subject().CN = internal_ip2
        cert.get_subject().emailAddress = 'namor925@gmail.com'
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(315360000)
        #cert.set_notBefore(now.strftime("%Y%m%d%H%M%SZ").encode())
        #cert.set_notAfter(expire.strftime("%Y%m%d%H%M%SZ").encode())
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')
        with open(C_F, "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            '''
            a = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
            b = a.encode('utf-8')
            print(a)
            print(type(a))
            '''
        with open(K_F, "wb") as ff:
            ff.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        print('generation success!')
    else:
        print('keys exists!')

create_self_signed_cert()


File: /master\create_database.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sqlite3


#db = SqliteDatabase('database.sql')
#db = ('database.sql')

#table description
db = 'database.sql'

def create_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE vpn_user (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT,
    date_create int NOT NULL,
    date_off int NOT NULL,
    username_telegram text
    )
    ''')
    
    cursor.execute('''CREATE TABLE bot (
    id INTEGER PRIMARY KEY,
    username_telegram TEXT NOT NULL UNIQUE,
    level int NOT NULL
    )
    ''')
    conn.close()

#db file - is exists?
file_path = 'database.sql'
if os.access(file_path, os.F_OK) == True:
    pass
else:
    create_db()


#first auth
def add_admin(password, username):
    from config import bot_admin_password
    if password == bot_admin_password:
        conn = sqlite3.connect('database.sql')
        cursor = conn.cursor()
        cursor.execute("SELECT username_telegram FROM bot WHERE username_telegram = ?", (username,))
        b = cursor.fetchall()
        if len(b) == 0:
            cursor.execute("INSERT INTO bot (username_telegram, level) VALUES (?, 0)", (username, ))
            conn.commit()
            return True
        else:
            pass
            return False
    else:
        return False


#who poweroff?
def who_poweroff():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM vpn_user WHERE date_off <= strftime('%s', 'now')")
    result = cursor.fetchall()
    conn.close()
    return result

#time to poweroff
def time_to_poweroff(username):
    ''' this function shows the time remaining before the trip.'''
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT date_off FROM vpn_user WHERE username = ?",  (username,  ))
    b = cursor.fetchone()
    print(b)
    print(type(b))
    return b
    
#whois?
def whois(username):
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram, level FROM bot WHERE username_telegram = ?", (username,))
    results = cursor.fetchone()
    #print(results)
    #print(type(results))
    #print(type(results))
    if results == None:
        pass
        auth = False
        level = 5
        return auth,  level
    else:
        if len(results) == 0:
            auth = False
            return auth
        elif results == None:
            auth = False
            return auth
        else:
            #print(results[1])
            auth = True
            level = results[1]
            return auth, level
    conn.close

#add admin bot user
def add_admin_mikrotik(username_telegram, level):
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram FROM bot WHERE username_telegram = ?", (username_telegram,))
    b = cursor.fetchall()
    if len(b) == 0:
        cursor.execute("INSERT INTO bot (username_telegram, level) VALUES (?, ?)", (username_telegram, level))
        #print(username_telegram)
        conn.commit()
        success = True
        #return success
    else:
        success = False
        pass
    conn.close

    return success



#list all admins
def list_all_admins():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT username_telegram, level FROM Bot")
    results = cursor.fetchall()
    conn.close
    #print(results)
    return results

#added user name and create_data and pass in database
def add_user_in_database(name, duration=3600):
    #from duration import date_off
    from add_time import add_data2
    #off = date_off()
    data = add_data2(name)
    date_create = data[0]
    date_off = data[1]
    
    conn = sqlite3.connect('database.sql', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vpn_user (username, date_create, date_off) VALUES (?, ?, ?)", (name, date_create, date_off))
    
    conn.commit()
    success = True
    conn.close
    return success

#whois(admin_id)


File: /master\create_mit_name.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def create_mit_name(text):
    a = text.strip() #this is make in function on bot
    b = re.sub(r'\s+',  ' ',  a)
    c = b.split(' ')
    duration = 3600
    vpn_name = ' '
    for i in c:
        if i.isdigit() == True:
            duration = i
        else:
            vpn_name = i
    return vpn_name,  duration


File: /master\duration.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  duration.py
#  
#  Copyright 2018 Roman <namor925@gmail.com>

from datetime import datetime, timedelta

def date_off(duration=1):
    date_create = datetime.now()
    #date_create = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    if duration == None:
        #delta = 'время не задано. задайте время.'
        pass
    elif duration == 0:
        delta = timedelta(hours=1)
    else:
        delta = timedelta(hours=duration)
    #print(delta)
    date_off = date_create + delta
    #print(date_off)
    return date_create.strftime("%Y.%m.%d %H:%M:%S"), date_off.strftime("%Y.%m.%d %H:%M:%S")
    


File: /master\generation_name2.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_name2.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#from generation name

from mimesis import Food
food = Food('en')

def create_name():
    a = food.drink()
    #print(a)
    return a



File: /master\generation_pass.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generation_pass.py
#  
#  Copyright 2018 Roman <roman@roman-home>
#  


from random import choice
from string import ascii_letters

def create_password():
    passw = ''.join(choice(ascii_letters) for i in range(12))
    #print(passw)
    return passw

#create_password()


File: /master\requirments.txt
pyTelegramBotAPI==3.6.0
librouteros==2.0.0
mimesis==2.0.0
CherryPy==14.0.1
pyOpenSSL==17.5.0
ipython==6.3.1
Fabric3==1.14


File: /master\systemd_example.txt
[Unit]
Description=Telegram bot service

[Service]
ExecStart=/usr/bin/python /home/roman/docs/microtik/bot.py
Restart=always
RestartSec=10
SyslogIdentifier=python-bot
RemainAfterExit=yes
User=roman
WorkingDirectory=/home/roman/docs/microtik/

[Install]
WantedBy=multi-user.target


File: /README.md
# Microtik



File: /requirments.txt
pyTelegramBotAPI==3.6.0
librouteros==2.0.0
mimesis==2.0.0
CherryPy==14.0.1
pyOpenSSL==17.5.0
ipython==6.3.1
Fabric3==1.14.post1
vedis==0.6.1


File: /systemd_example.txt
[Unit]
Description=Telegram bot service

[Service]
ExecStart=/usr/bin/python /home/roman/docs/microtik/bot.py
Restart=always
RestartSec=10
SyslogIdentifier=python-bot
RemainAfterExit=yes
User=roman
WorkingDirectory=/home/roman/docs/microtik/

[Install]
WantedBy=multi-user.target


