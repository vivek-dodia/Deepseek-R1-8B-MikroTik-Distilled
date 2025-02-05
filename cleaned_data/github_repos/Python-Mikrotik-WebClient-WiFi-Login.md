# Repository Information
Name: Python-Mikrotik-WebClient-WiFi-Login

# Directory Structure
Directory structure:
└── github_repos/Python-Mikrotik-WebClient-WiFi-Login/
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
    │   │       ├── pack-282415c2f6714b5167e4c314f3526a7142f747a3.idx
    │   │       └── pack-282415c2f6714b5167e4c314f3526a7142f747a3.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── CHANGELOG.md
    ├── example/
    │   ├── LICENSE
    │   ├── login_example.py
    │   ├── logout_example.py
    │   ├── README.md
    │   └── speedtest_example.py
    ├── LICENSE
    ├── python_mikrotik_login/
    │   ├── md5.py
    │   ├── mikrotik_login.py
    │   └── __init__.py
    ├── README.md
    ├── requirements/
    │   ├── default.txt
    │   └── requirements.txt
    └── setup.py


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
	url = https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login.git
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
0000000000000000000000000000000000000000 fdb1371a2745e6ebf0725bb1e0bd0791958aa19e vivek-dodia <vivek.dodia@icloud.com> 1738606077 -0500	clone: from https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 fdb1371a2745e6ebf0725bb1e0bd0791958aa19e vivek-dodia <vivek.dodia@icloud.com> 1738606077 -0500	clone: from https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 fdb1371a2745e6ebf0725bb1e0bd0791958aa19e vivek-dodia <vivek.dodia@icloud.com> 1738606077 -0500	clone: from https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
f82a1c7bf763efea3edb222d5972031288523a59 refs/remotes/origin/dependabot/pip/requirements/certifi-2022.12.7
703bcf42492fe65c236a6028bda77e4cd88af697 refs/remotes/origin/dependabot/pip/requirements/urllib3-1.26.5
fdb1371a2745e6ebf0725bb1e0bd0791958aa19e refs/remotes/origin/master
9ba7705140bb6aac664596b0bba9abd0287f5cdb refs/tags/1
82a7899166d40ffd6e6309f810380cee5cbadfb0 refs/tags/2
a586806e705559d305b3b7ef7765088c41dd472a refs/tags/2.1
23cad9dcd3b4c9db5cb4b4f58648efa6d7539896 refs/tags/v3.0.0
^659496d0b8bb601e6cc4a3ec5b15331f3ba7cab9
57701fb2cf954f31995f71327a7b8dccf61f3568 refs/tags/v3.0.7
b277a858e9237f628ed5033c5667ed21eafbd82c refs/tags/v3.0.8


File: /.git\refs\heads\master
fdb1371a2745e6ebf0725bb1e0bd0791958aa19e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
env
# Byte-compiled / optimized / DLL files
File: /CHANGELOG.md

# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
## [3.0.0] - 2020-12-19
 
Here we write upgrading notes for brands. It's a team effort to make them as
straightforward as possible.
 
### Added
-  Add logout feature
-  Add check login status
-  Add check internet status
-  Add speedtest
 
### Fixed
- Fix already logged in causing error in login function
 

File: /example\LICENSE
MIT License
Copyright (c) 2018 YOUR NAME
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

File: /example\login_example.py
from python_mikrotik_login import MikrotikLogin

# username="admin"
# password="admin"
# url="http://10.x.x.x/login" #your url
username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #working simulated Mikrotik login page url to test the code, change to your url

login = MikrotikLogin(username, password, url)
login.do_login()
print(login)


File: /example\logout_example.py
from python_mikrotik_login import MikrotikLogin

username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #working simulated Mikrotik login page url to test the code, change to your url

login = MikrotikLogin(username, password, url)
login.do_logout()
print(login)


File: /example\README.md
# Python Mikrotik WebClient WiFi Login
This is a python code to login to wifi Mikrotik Webclient for devices that has no access to GUI (such as headless Raspberry Pi, or Linux Terminal). Mikrotik Webclient is using unique keys or salts generated randomly at some time interval, this program is made to find that unique keys or salts and combine it with username and password to make final login request.

## Installing the package
        pip install python-mikrotik-login

## Using the program
### First import the module
        from python_mikrotik_login import mikrotikLogin
        
        mikrotikLogin("username","password","http://url") #you can leave the unique key index empty or set it manually

### Arguments
        mikrotikLogin(username_string, password_string, url_string, minkey1_integer_optional, maxkey1_integer_optional, minkey2_integer_optional, maxkey2_integer_optional)

## How this works
This code works by finding the unique key from the Mikrotik Web Client and then combine it with username and password then send back the `post` request to the Mikrotik Web Client.
### Finding the unique key
For the example this is the function where the login action is fired:

        function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315');
        document.sendin.submit();
        return false;
        }

In this case you should find the index of:

        \340
        and
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315

where:

        \340 is the first unique key or salt
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315 is the second unique key salt

File: /example\speedtest_example.py
from python_mikrotik_login import MikrotikLogin

username="ihsan"
password="fajar"
url="https://mikrorikloginexample.ihsanfr.repl.co/login" #working simulated Mikrotik login page url to test the code, change to your url

login = MikrotikLogin(username, password, url)
login.do_login()
login.check_internet()
print(login)
print(login.speed_test(share=True))


File: /LICENSE
MIT License
Copyright (c) 2018 YOUR NAME
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

File: /python_mikrotik_login\md5.py
__all__ = ['md5']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['ii', 'str2binl', 'binl2hex', 'b64MD5', 'safe_add', 'rol', 'b64MD5w', 'hh', 'gg', 'ff', 'binl2b64', 'hexMD5', 'strw2binl', 'cmn', 'coreMD5', 'hexMD5w', 'calcMD5'])
@Js
def PyJsHoisted_safe_add_(x, y, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
    var.registers(['msw', 'x', 'y', 'lsw'])
    var.put('lsw', ((var.get('x')&Js(65535))+(var.get('y')&Js(65535))))
    var.put('msw', (((var.get('x')>>Js(16.0))+(var.get('y')>>Js(16.0)))+(var.get('lsw')>>Js(16.0))))
    return ((var.get('msw')<<Js(16.0))|(var.get('lsw')&Js(65535)))
PyJsHoisted_safe_add_.func_name = 'safe_add'
var.put('safe_add', PyJsHoisted_safe_add_)
@Js
def PyJsHoisted_rol_(num, cnt, this, arguments, var=var):
    var = Scope({'num':num, 'cnt':cnt, 'this':this, 'arguments':arguments}, var)
    var.registers(['num', 'cnt'])
    return ((var.get('num')<<var.get('cnt'))|PyJsBshift(var.get('num'),(Js(32.0)-var.get('cnt'))))
PyJsHoisted_rol_.func_name = 'rol'
var.put('rol', PyJsHoisted_rol_)
@Js
def PyJsHoisted_cmn_(q, a, b, x, s, t, this, arguments, var=var):
    var = Scope({'q':q, 'a':a, 'b':b, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'b', 'q', 't', 'a', 's'])
    return var.get('safe_add')(var.get('rol')(var.get('safe_add')(var.get('safe_add')(var.get('a'), var.get('q')), var.get('safe_add')(var.get('x'), var.get('t'))), var.get('s')), var.get('b'))
PyJsHoisted_cmn_.func_name = 'cmn'
var.put('cmn', PyJsHoisted_cmn_)
@Js
def PyJsHoisted_ff_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')&var.get('c'))|((~var.get('b'))&var.get('d'))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_ff_.func_name = 'ff'
var.put('ff', PyJsHoisted_ff_)
@Js
def PyJsHoisted_gg_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')&var.get('d'))|(var.get('c')&(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_gg_.func_name = 'gg'
var.put('gg', PyJsHoisted_gg_)
@Js
def PyJsHoisted_hh_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')(((var.get('b')^var.get('c'))^var.get('d')), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_hh_.func_name = 'hh'
var.put('hh', PyJsHoisted_hh_)
@Js
def PyJsHoisted_ii_(a, b, c, d, x, s, t, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'x':x, 's':s, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 't', 'c', 'a', 's'])
    return var.get('cmn')((var.get('c')^(var.get('b')|(~var.get('d')))), var.get('a'), var.get('b'), var.get('x'), var.get('s'), var.get('t'))
PyJsHoisted_ii_.func_name = 'ii'
var.put('ii', PyJsHoisted_ii_)
@Js
def PyJsHoisted_coreMD5_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x', 'd', 'b', 'c', 'olda', 'a', 'oldb', 'oldc', 'oldd'])
    var.put('a', Js(1732584193.0))
    var.put('b', (-Js(271733879.0)))
    var.put('c', (-Js(1732584194.0)))
    var.put('d', Js(271733878.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('x').get('length')):
        try:
            var.put('olda', var.get('a'))
            var.put('oldb', var.get('b'))
            var.put('oldc', var.get('c'))
            var.put('oldd', var.get('d'))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(7.0), (-Js(680876936.0))))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(1.0))), Js(12.0), (-Js(389564586.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(17.0), Js(606105819.0)))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(3.0))), Js(22.0), (-Js(1044525330.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(7.0), (-Js(176418897.0))))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(5.0))), Js(12.0), Js(1200080426.0)))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(17.0), (-Js(1473231341.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(7.0))), Js(22.0), (-Js(45705983.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(7.0), Js(1770035416.0)))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(9.0))), Js(12.0), (-Js(1958414417.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(17.0), (-Js(42063.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(11.0))), Js(22.0), (-Js(1990404162.0))))
            var.put('a', var.get('ff')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(7.0), Js(1804603682.0)))
            var.put('d', var.get('ff')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(13.0))), Js(12.0), (-Js(40341101.0))))
            var.put('c', var.get('ff')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(17.0), (-Js(1502002290.0))))
            var.put('b', var.get('ff')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(15.0))), Js(22.0), Js(1236535329.0)))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(5.0), (-Js(165796510.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(6.0))), Js(9.0), (-Js(1069501632.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(14.0), Js(643717713.0)))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(0.0))), Js(20.0), (-Js(373897302.0))))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(5.0), (-Js(701558691.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(10.0))), Js(9.0), Js(38016083.0)))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(14.0), (-Js(660478335.0))))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(4.0))), Js(20.0), (-Js(405537848.0))))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(5.0), Js(568446438.0)))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(14.0))), Js(9.0), (-Js(1019803690.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(14.0), (-Js(187363961.0))))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(8.0))), Js(20.0), Js(1163531501.0)))
            var.put('a', var.get('gg')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(5.0), (-Js(1444681467.0))))
            var.put('d', var.get('gg')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(2.0))), Js(9.0), (-Js(51403784.0))))
            var.put('c', var.get('gg')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(14.0), Js(1735328473.0)))
            var.put('b', var.get('gg')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(12.0))), Js(20.0), (-Js(1926607734.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(5.0))), Js(4.0), (-Js(378558.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(8.0))), Js(11.0), (-Js(2022574463.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(11.0))), Js(16.0), Js(1839030562.0)))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(14.0))), Js(23.0), (-Js(35309556.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(1.0))), Js(4.0), (-Js(1530992060.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(4.0))), Js(11.0), Js(1272893353.0)))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(7.0))), Js(16.0), (-Js(155497632.0))))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(10.0))), Js(23.0), (-Js(1094730640.0))))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(13.0))), Js(4.0), Js(681279174.0)))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(0.0))), Js(11.0), (-Js(358537222.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(3.0))), Js(16.0), (-Js(722521979.0))))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(6.0))), Js(23.0), Js(76029189.0)))
            var.put('a', var.get('hh')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(9.0))), Js(4.0), (-Js(640364487.0))))
            var.put('d', var.get('hh')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(12.0))), Js(11.0), (-Js(421815835.0))))
            var.put('c', var.get('hh')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(15.0))), Js(16.0), Js(530742520.0)))
            var.put('b', var.get('hh')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(2.0))), Js(23.0), (-Js(995338651.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(0.0))), Js(6.0), (-Js(198630844.0))))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(7.0))), Js(10.0), Js(1126891415.0)))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(14.0))), Js(15.0), (-Js(1416354905.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(5.0))), Js(21.0), (-Js(57434055.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(12.0))), Js(6.0), Js(1700485571.0)))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(3.0))), Js(10.0), (-Js(1894986606.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(10.0))), Js(15.0), (-Js(1051523.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(1.0))), Js(21.0), (-Js(2054922799.0))))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(8.0))), Js(6.0), Js(1873313359.0)))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(15.0))), Js(10.0), (-Js(30611744.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(6.0))), Js(15.0), (-Js(1560198380.0))))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(13.0))), Js(21.0), Js(1309151649.0)))
            var.put('a', var.get('ii')(var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('x').get((var.get('i')+Js(4.0))), Js(6.0), (-Js(145523070.0))))
            var.put('d', var.get('ii')(var.get('d'), var.get('a'), var.get('b'), var.get('c'), var.get('x').get((var.get('i')+Js(11.0))), Js(10.0), (-Js(1120210379.0))))
            var.put('c', var.get('ii')(var.get('c'), var.get('d'), var.get('a'), var.get('b'), var.get('x').get((var.get('i')+Js(2.0))), Js(15.0), Js(718787259.0)))
            var.put('b', var.get('ii')(var.get('b'), var.get('c'), var.get('d'), var.get('a'), var.get('x').get((var.get('i')+Js(9.0))), Js(21.0), (-Js(343485551.0))))
            var.put('a', var.get('safe_add')(var.get('a'), var.get('olda')))
            var.put('b', var.get('safe_add')(var.get('b'), var.get('oldb')))
            var.put('c', var.get('safe_add')(var.get('c'), var.get('oldc')))
            var.put('d', var.get('safe_add')(var.get('d'), var.get('oldd')))
        finally:
                var.put('i', Js(16.0), '+')
    return Js([var.get('a'), var.get('b'), var.get('c'), var.get('d')])
PyJsHoisted_coreMD5_.func_name = 'coreMD5'
var.put('coreMD5', PyJsHoisted_coreMD5_)
@Js
def PyJsHoisted_binl2hex_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['hex_tab', 'str', 'i', 'binarray'])
    var.put('hex_tab', Js('0123456789abcdef'))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(4.0))):
        try:
            var.put('str', (var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>(((var.get('i')%Js(4.0))*Js(8.0))+Js(4.0)))&Js(15)))+var.get('hex_tab').callprop('charAt', ((var.get('binarray').get((var.get('i')>>Js(2.0)))>>((var.get('i')%Js(4.0))*Js(8.0)))&Js(15)))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('str')
PyJsHoisted_binl2hex_.func_name = 'binl2hex'
var.put('binl2hex', PyJsHoisted_binl2hex_)
@Js
def PyJsHoisted_binl2b64_(binarray, this, arguments, var=var):
    var = Scope({'binarray':binarray, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'tab', 'i', 'binarray'])
    var.put('tab', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('binarray').get('length')*Js(32.0))):
        try:
            var.put('str', var.get('tab').callprop('charAt', (((var.get('binarray').get((var.get('i')>>Js(5.0)))<<(var.get('i')%Js(32.0)))&Js(63))|((var.get('binarray').get((var.get('i')>>(Js(5.0)+Js(1.0))))>>(Js(32.0)-(var.get('i')%Js(32.0))))&Js(63)))), '+')
        finally:
                var.put('i', Js(6.0), '+')
    return var.get('str')
PyJsHoisted_binl2b64_.func_name = 'binl2b64'
var.put('binl2b64', PyJsHoisted_binl2b64_)
@Js
def PyJsHoisted_str2binl_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'nblk', 'blks', 'str'])
    var.put('nblk', (((var.get('str').get('length')+Js(8.0))>>Js(6.0))+Js(1.0)))
    var.put('blks', var.get('Array').create((var.get('nblk')*Js(16.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('nblk')*Js(16.0))):
        try:
            var.get('blks').put(var.get('i'), Js(0.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.get('blks').put((var.get('i')>>Js(2.0)), ((var.get('str').callprop('charCodeAt', var.get('i'))&Js(255))<<((var.get('i')%Js(4.0))*Js(8.0))), '|')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('blks').put((var.get('i')>>Js(2.0)), (Js(128)<<((var.get('i')%Js(4.0))*Js(8.0))), '|')
    var.get('blks').put(((var.get('nblk')*Js(16.0))-Js(2.0)), (var.get('str').get('length')*Js(8.0)))
    return var.get('blks')
PyJsHoisted_str2binl_.func_name = 'str2binl'
var.put('str2binl', PyJsHoisted_str2binl_)
@Js
def PyJsHoisted_strw2binl_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'nblk', 'blks', 'str'])
    var.put('nblk', (((var.get('str').get('length')+Js(4.0))>>Js(5.0))+Js(1.0)))
    var.put('blks', var.get('Array').create((var.get('nblk')*Js(16.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('nblk')*Js(16.0))):
        try:
            var.get('blks').put(var.get('i'), Js(0.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('str').get('length')):
        try:
            var.get('blks').put((var.get('i')>>Js(1.0)), (var.get('str').callprop('charCodeAt', var.get('i'))<<((var.get('i')%Js(2.0))*Js(16.0))), '|')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('blks').put((var.get('i')>>Js(1.0)), (Js(128)<<((var.get('i')%Js(2.0))*Js(16.0))), '|')
    var.get('blks').put(((var.get('nblk')*Js(16.0))-Js(2.0)), (var.get('str').get('length')*Js(16.0)))
    return var.get('blks')
PyJsHoisted_strw2binl_.func_name = 'strw2binl'
var.put('strw2binl', PyJsHoisted_strw2binl_)
@Js
def PyJsHoisted_hexMD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_hexMD5_.func_name = 'hexMD5'
var.put('hexMD5', PyJsHoisted_hexMD5_)
@Js
def PyJsHoisted_hexMD5w_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('strw2binl')(var.get('str'))))
PyJsHoisted_hexMD5w_.func_name = 'hexMD5w'
var.put('hexMD5w', PyJsHoisted_hexMD5w_)
@Js
def PyJsHoisted_b64MD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2b64')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_b64MD5_.func_name = 'b64MD5'
var.put('b64MD5', PyJsHoisted_b64MD5_)
@Js
def PyJsHoisted_b64MD5w_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2b64')(var.get('coreMD5')(var.get('strw2binl')(var.get('str'))))
PyJsHoisted_b64MD5w_.func_name = 'b64MD5w'
var.put('b64MD5w', PyJsHoisted_b64MD5w_)
@Js
def PyJsHoisted_calcMD5_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    return var.get('binl2hex')(var.get('coreMD5')(var.get('str2binl')(var.get('str'))))
PyJsHoisted_calcMD5_.func_name = 'calcMD5'
var.put('calcMD5', PyJsHoisted_calcMD5_)
pass


# Add lib to the module scope
md5 = var.to_python()

File: /python_mikrotik_login\mikrotik_login.py
import requests
from .md5 import md5
import urllib.request as urllib2
from urllib.parse import urlparse
import speedtest
import json

# program login wifi via webclient Mikrotik
# Contributors Ihsan Fajar Ramadhan, Marchel-Ace
# https://github.com/castrix, https://github.com/Marchel-Ace
# webclient login code


class MikrotikLogin:
    def __init__(self, username: str,
                 password: str, url: str,
                 minkey1: int = 0, maxkey1: int = 0,
                 minkey2: int = 0, maxkey2: int = 0) -> None:
        """
        you can set the salt index manually (if the pattern is different) or leave it empty
        minkey1=2625 # optional minimum index of the first unique encryption key
        maxkey1=2629 # optional maximum index of the first unique encryption key
        minkey2=2666 # optional minimum index of the second unique encryption key
        maxkey2=2730 # optional maximum index of the second unique encryption key

        """
        self.username = username
        self.password = password
        self.url = url
        self.minkey1 = minkey1
        self.maxkey1 = maxkey1
        self.minkey2 = minkey2
        self.maxkey2 = maxkey2
        self.is_connected = False
        self.is_logged_in = False

    def do_login(self):
        """
        you know what does it mean~
        """
        if self.check_login_status():
            print("Already logged in!")
            return True
        r = requests.get(self.url).text  # requesting the url text
        key1 = ""
        key2 = ""
        if self.minkey1 == 0 or self.maxkey1 == 0 or self.minkey2 == 0 or self.maxkey2 == 0:
            a = "document.sendin.password.value"
            try:
                b = r.index(a)
            except:
                print("Error, url format is not right. Please make sure you use the right url format: http://url/login")
                return False
            key1 = r[b+len(a)+11:b+len(a)+15]
            key2 = r[b+len(a)+52:b+len(a)+116]
        else:
            key1 = r[self.minkey1:self.maxkey1]
            key2 = r[self.minkey2:self.maxkey2]
        # translating octal characters to char
        key1 = bytes(key1, "utf-8").decode("unicode_escape")
        # translating octal characters to char
        key2 = bytes(key2, "utf-8").decode("unicode_escape")
        # encrypt the password
        encryptmd5 = md5.hexMD5(key1+self.password+key2)
        finallogin = self.url+"?username="+self.username + \
            "&password="+encryptmd5  # wrap all the variables
        response = requests.post(finallogin).text  # make the final requests
        print("Logging in ...")
        if self.check_login_status():
            print("Success! Logged in.")
            self.check_internet()
            return True
        else:
            print("Something is wrong!")
            print("Please make sure you use the right url format: http://url/login")
            return False

    def do_logout(self):
        """
        you know what does it mean~
        """
        url = urlparse(self.url)
        final_url = f'{url.scheme}://{url.netloc}/logout'
        req = requests.get(final_url)
        print("Logging out ...")
        if self.check_login_status():
            print("Something is wrong!")
            return True
        else:
            print("Success! Logged out.")
            self.check_internet()
            return False

    def check_login_status(self):
        """
        Check login status, will return True if authenticated and False if not
        """
        url = urlparse(self.url)
        final_url = f'{url.scheme}://{url.netloc}/status'
        req = requests.get(final_url)
        if 'status' in req.url:
            self.is_logged_in = True
            return True
        else:
            self.is_logged_in = False
            return False

    def check_internet(self):
        """
        Check internet connection, will return True
        if internet connection is detected and False if not
        """
        print("Checking internet connection ...")
        try:
            response = urllib2.urlopen('http://216.58.192.142', timeout=1)
            self.is_connected = True
            return True
        except Exception as e:
            print("error")
            print(e)
            self.is_connected = False
            return False

    def speed_test(self, share=False):
        """
        set share True if you want
        get image of your speedtest result
        """
        status = {}
        if self.check_internet():
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            s.upload()
            if share:
                status['share_url'] = s.results.share()
            results_dict = s.results.dict()
            status['download'] = results_dict['download']
            status['upload'] = results_dict['upload']
            del s
            return status
        else:
            status['status'] = "No internet connection"
            return status

    def __repr__(self) -> str:
        return json.dumps({
            'logged_in': self.is_logged_in,
            'internet_connection': self.is_connected
        })

File: /python_mikrotik_login\__init__.py
from .md5 import md5
from .mikrotik_login import MikrotikLogin

File: /README.md
# Python Mikrotik WebClient WiFi Login
This is a python code to login to wifi Mikrotik Webclient for devices that has no access to GUI (such as headless Raspberry Pi, or Linux Terminal). Mikrotik Webclient is using unique keys or salts generated randomly at some time interval, this program is made to find that unique keys or salts and combine it with username and password to make final login request.

## Installing the package
### using pip
        pip install python-mikrotik-login
### using git
        pip install git+https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login
## Using the program
### First import the module
        from python_mikrotik_login import MikrotikLogin

        login = MikrotikLogin("username","password","http://url") #you can leave the unique key index empty or set it manually
        login.do_login()
        print(login) # to see status
### Arguments
        MikrotikLogin(username_string, password_string, url_string, minkey1_integer_optional, maxkey1_integer_optional, minkey2_integer_optional, maxkey2_integer_optional)

if you are still confused, see the [Example](https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login/tree/master/example)

## How this works
This code works by finding the unique key from the Mikrotik Web Client and then combine it with username and password then send back the `post` request to the Mikrotik Web Client.
### Finding the unique key
For the example this is the function where the login action is fired:

        function doLogin() {
        document.sendin.username.value = document.login.username.value;
        document.sendin.password.value = hexMD5('\340' + document.login.password.value + '\043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315');
        document.sendin.submit();
        return false;
        }

In this case you should find the index of:

        \340
        and
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315

where:

        \340 is the first unique key or salt
        \043\242\062\374\062\365\062\266\201\323\145\251\200\303\025\315 is the second unique key salt

# Contributors

[Ihsan Fajar Ramadhan](https://github.com/castrix)

[MarchelAce](https://github.com/Marchel-Ace)

File: /requirements\default.txt
requests>=2.25.0
Js2Py>=0.70
speedtest-cli>=2.1.0


File: /requirements\requirements.txt
backports.zoneinfo==0.2.1
certifi==2020.12.5
chardet==4.0.0
idna==2.10
Js2Py==0.70
pyjsparser==2.7.1
requests==2.25.1
six==1.15.0
speedtest-cli==2.1.2
tzlocal==3.0b1
urllib3==1.26.3

File: /setup.py
import setuptools
import os
import re

NAME = 'python-mikrotik-login'
PACKAGE = 'python_mikrotik_login'

# -*- Distribution Meta -*-

def add_default(m):
    attr_name, attr_value = m.groups()
    return ((attr_name, attr_value.strip("\"'")),)


def add_doc(m):
    return (('doc', m.groups()[0]),)


re_meta = re.compile(r'__(\w+?)__\s*=\s*(.*)')
re_doc = re.compile(r'^"""(.+?)"""')
pats = {re_meta: add_default,
        re_doc: add_doc}
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, PACKAGE, '__init__.py')) as meta_fh:
    meta = {}
    for line in meta_fh:
        if line.strip() == '# -eof meta-':
            break
        for pattern, handler in pats.items():
            m = pattern.match(line.strip())
            if m:
                meta.update(handler(m))


# -*- Installation Requires -*-

def strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), 'requirements', *f)).readlines()
        ) if r]


def reqs(*f):
    return [req for subreq in _reqs(*f) for req in subreq]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version="3.0.5",
    author="castrix",
    author_email="castrix.ihsan@gmail.com",
    description="Python code to login to Mikrotik WebClient without GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=reqs('requirements.txt'),
    url="https://github.com/castrix/Python-Mikrotik-WebClient-WiFi-Login",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

