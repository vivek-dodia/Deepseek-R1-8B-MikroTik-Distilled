# Repository Information
Name: mikrotik_parental_control

# Directory Structure
Directory structure:
└── github_repos/mikrotik_parental_control/
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
    │   │       ├── pack-34295f1e770ecffb01323a4c0036057f19206f4e.idx
    │   │       └── pack-34295f1e770ecffb01323a4c0036057f19206f4e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── but1.py
    ├── dhcp_hosts.py
    ├── filter.py
    ├── logs.py
    ├── MAIN.py
    ├── mainwin.py
    ├── message.py
    ├── mikr_api.py
    ├── README.md
    ├── same.py
    ├── scheduler.py
    ├── sched_but.py
    └── scirpt.py


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
	url = https://github.com/evgeniy-p/mikrotik_parental_control.git
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
0000000000000000000000000000000000000000 20aa30efbdfbeb88a29d4ab15282cb6a51a60459 vivek-dodia <vivek.dodia@icloud.com> 1738606352 -0500	clone: from https://github.com/evgeniy-p/mikrotik_parental_control.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 20aa30efbdfbeb88a29d4ab15282cb6a51a60459 vivek-dodia <vivek.dodia@icloud.com> 1738606352 -0500	clone: from https://github.com/evgeniy-p/mikrotik_parental_control.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 20aa30efbdfbeb88a29d4ab15282cb6a51a60459 vivek-dodia <vivek.dodia@icloud.com> 1738606352 -0500	clone: from https://github.com/evgeniy-p/mikrotik_parental_control.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
20aa30efbdfbeb88a29d4ab15282cb6a51a60459 refs/remotes/origin/master


File: /.git\refs\heads\master
20aa30efbdfbeb88a29d4ab15282cb6a51a60459


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /but1.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 181)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 99, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "None"))
        self.pushButton.setText(_translate("Form", "make static"))
        self.pushButton_2.setText(_translate("Form", "inet is on"))
        self.pushButton_3.setText(_translate("Form", "remove static"))
        self.pushButton_4.setText(_translate("Form", "Расписание"))



File: /dhcp_hosts.py
import io
import logging
from contextlib import redirect_stdout


class DhcpHosts:

    hosts = dict()

    def __init__(self, router):
        self.__class__.hosts = dict()
        self.router = router
        self.get_hosts()

    def talk(self, question):
        logging.debug(' Отправляю запрос {}....'.format(question))
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(["{}".format(question)])
            answer = buf.getvalue()
        if ">>> =message=no such command" in answer.split('\n') \
                or ">>> =message=no such command prefix" in answer.split('\n'):
            logging.debug(' Получен ответ {}!'.format(answer))
            logging.debug(' Введенный запрос не корректен!')
        else:
            return answer

    def get_hosts(self):
        try:
            hosts_list = self.talk('/ip/dhcp-server/lease/print').split('>>> !re')
            hosts_list.remove('<<< /ip/dhcp-server/lease/print\n<<< \n')
            for host in range(0, len(hosts_list)):
                self.__class__.hosts[host] = {}
                for element in hosts_list[host].split('\n'):
                    if element == '>>> ' or element == '':
                        continue
                    elif element == '>>> !done':
                        break
                    self.__class__.hosts[host].update({element.split('=')[1]: element.split('=')[2]})
            self.__class__.hosts = {nhost['host-name']: nhost for nhost in self.__class__.hosts.values()}
            logging.info(' Хосты: {}'.format(self.__class__.hosts.keys()))
            logging.debug(':')
            logging.debug(self.__class__.hosts)
        except ValueError:
            logging.debug('Совсем нет Lease....')
            self.__class__.hosts = {'None': {'host-name': 'None'}}

    def make_static(self, *args):
        for arhost in args:
            if arhost in [kwhost['host-name'] for kwhost in self.__class__.hosts.values()]:
                logging.debug(' Задаем статику для {}, ID - {}'.format(arhost, self.__class__.hosts[arhost]['.id']))
                with io.StringIO() as buf, redirect_stdout(buf):
                    self.router.talk(['/ip/dhcp-server/lease/make-static', '=.id='+self.__class__.hosts[arhost]['.id']])
                    answer = buf.getvalue()
                    logging.debug(answer)

    def remove_static(self, *args):
        for arhost in args:
            if arhost in [kwhost['host-name'] for kwhost in self.__class__.hosts.values()]:
                logging.debug(' Удаляем lease для {}, ID - {}'.format(arhost, self.__class__.hosts[arhost]['.id']))
                with io.StringIO() as buf, redirect_stdout(buf):
                    self.router.talk(['/ip/dhcp-server/lease/remove', '=.id='+self.__class__.hosts[arhost]['.id']])
                    answer = buf.getvalue()
                    logging.debug(answer)



File: /filter.py
import io
import dhcp_hosts
import logging
from contextlib import redirect_stdout
from re import match


class Filter:
    def __init__(self, router):
        self.router = router
        self.ids = dict()
        self.answer = None
        self.hosts_dict = dhcp_hosts.DhcpHosts.hosts

    def forwardblock(self, host, method):
        self.hosts_dict = dhcp_hosts.DhcpHosts.hosts
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(['/ip/firewall/filter/add', '=chain=forward', '=action=reject',
                              '=reject-with=icmp-admin-prohibited',
                              '=comment=' + method + '_' + self.hosts_dict[host]['address'], '=place-before=0',
                              '=src-address=' + self.hosts_dict[host]['address']])
            answer = buf.getvalue()
            logging.debug(answer)

    def isblocked(self, host, method):
        self.hosts_dict = dhcp_hosts.DhcpHosts.hosts
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(['/ip/firewall/filter/print', '?comment=' + method + '_'
                              + self.hosts_dict[host]['address']])
            self.answer = buf.getvalue()
            logging.debug(self.answer)
        if ">>> !re" in self.answer.split('\n'):
            for line in self.answer.split('\n'):
                if match('^.*\.id.*', line):
                    self.ids[host] = match('^.*\.id=(.*)', line).group(1)
            return True
        else:
            return False

    def disable_rule(self, host, method):
        self.hosts_dict = dhcp_hosts.DhcpHosts.hosts
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(['/ip/firewall/filter/print', '?comment=' + method + '_'
                              + self.hosts_dict[host]['address']])
            self.answer = buf.getvalue()
            logging.debug(self.answer)
        if ">>> !re" in self.answer.split('\n'):
            for line in self.answer.split('\n'):
                if match('^.*\.id.*', line):
                    with io.StringIO() as buf, redirect_stdout(buf):
                        self.router.talk(['/ip/firewall/filter/set', '=.id=' + match('^.*\.id=(.*)', line).group(1),
                                          '=disabled=yes'])
                        disabled = buf.getvalue()
                        logging.debug(disabled)

    def delete_rule(self, host, method):
        self.hosts_dict = dhcp_hosts.DhcpHosts.hosts
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(['/ip/firewall/filter/print', '?comment=' + method + '_'
                              + self.hosts_dict[host]['address']])
            self.answer = buf.getvalue()
            logging.debug(self.answer)
        if ">>> !re" in self.answer.split('\n'):
            for line in self.answer.split('\n'):
                if match('^.*\.id.*', line):
                    with io.StringIO() as buf, redirect_stdout(buf):
                        self.router.talk(['/ip/firewall/filter/remove', '=.id=' + match('^.*\.id=(.*)', line).group(1),])
                        deleted = buf.getvalue()
                        logging.debug(deleted)








File: /logs.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textBrowser = QtWidgets.QPlainTextEdit(Form)
        self.textBrowser.setGeometry(QtCore.QRect(15, 21, 371, 261))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "logs"))



File: /MAIN.py
import sys
import mainwin
import but1
import logs
import message
import mikr_api
import conf
import sys
import io
import dhcp_hosts
import filter
import scirpt
import scheduler
import sched_but
import logging
from contextlib import redirect_stdout
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        # Окно кнопки 3 (logger)
        self.uibut3 = logs.Ui_Form()
        self.windowbut3 = QMainWindow()
        self.windowbut3.move(700, 600)
        self.uibut3.setupUi(self.windowbut3)
        # logger conf
        self.logger = logging.getLogger(__name__)
        self.gui = logging.StreamHandler(Writer(self.uibut3))
        self.logfile = logging.FileHandler('mikrotik.log')
        self.logger.addHandler(self.gui)
        self.logger.addHandler(self.logfile)
        # Соединение с mikrotik
        self.s = None
        self.router = None
        self.start_connect()
        self.login()
        self.logger.debug(' Запускаем главное окно, передаем список хостов')
        # обращаемся к классу, по которому можно получить список хостов, а также задать статику и т.п
        self.router_hosts = dhcp_hosts.DhcpHosts(self.router)
        self.hosts_dict = self.router_hosts.hosts
        # обращаемся к классу, по которому можно создать\удалить правило в firewall
        self.router_filter = filter.Filter(self.router)
        # Обращаемся к классу, по работе с скриптами
        self.wwscript = scirpt.Scripts(self.router)
        # Обращаемся к классу по работе с расписанием
        self.scheduler = scheduler.Scheduler(self.router)
        # Главное окно
        self.Mui = mainwin.Ui_MainWindow()
        self.Mwindow = QMainWindow()
        self.Mwindow.move(300, 300)
        self.Mui.setupUi(self.Mwindow)
        self.Mui.pushButton.clicked.connect(self.button1)
        self.Mui.pushButton_3.clicked.connect(self.button3)
        self.Mui.pushButton_4.clicked.connect(self.refresh)
        # Окно кнопки 1
        self.uibut1 = but1.Ui_Form()
        self.windowbut1 = QMainWindow()
        self.uibut1.setupUi(self.windowbut1)
        self.uibut1.pushButton.clicked.connect(self.pushbuttonbut1_1)
        self.uibut1.pushButton_2.clicked.connect(self.pushbuttonbut1_2)
        self.uibut1.pushButton_3.clicked.connect(self.pushbuttonbut1_3)
        self.uibut1.pushButton_4.clicked.connect(self.pushbuttonbut1_4)
        # Окно кнопки 2(1-4) (расписание)
        self.uibut2 = but1.Ui_Form()
        self.windowbut2 = QMainWindow()
        self.uibut2.setupUi(self.windowbut2)
        self.uibut2.pushButton.clicked.connect(self.pushbuttonbut2_1)
        self.uibut2.pushButton_2.clicked.connect(self.pushbuttonbut2_2)
        self.uibut2.pushButton_3.clicked.connect(self.pushbuttonbut2_3)
        self.uibut2.pushButton_4.clicked.connect(self.pushbuttonbut2_4)
        self.uibut2.pushButton_2.setDisabled(True)
        self.uibut2.pushButton_3.setDisabled(True)
        self.uibut2.pushButton_4.setDisabled(True)
        # Окно сообщения об ошибке
        self.uimessage = message.Ui_Form()
        self.windowmessage = QMainWindow()
        self.windowmessage.move(500, 500)
        self.uimessage.setupUi(self.windowmessage)
        # Окно кнопки sched_but
        self.uished_but = sched_but.Ui_Form()
        self.windowshed_but = QMainWindow()
        self.windowshed_but.move(1000, 300)
        self.uished_but.setupUi(self.windowshed_but)
        self.uished_but.dateTimeEdit_2.setDisabled(True)
        self.uished_but.dateTimeEdit_4.setDisabled(True)
        self.uished_but.label_2.setDisabled(True)
        self.uished_but.label_5.setDisabled(True)
        self.uished_but.label_6.setDisabled(True)
        self.uished_but.radioButton_4.checkStateSet()
        self.uished_but.radioButton_4.setDisabled(True)
        self.uished_but.radioButton_5.setDisabled(True)
        self.uished_but.radioButton_6.setDisabled(True)
        self.uished_but.radioButton.setChecked(True)
        self.uished_but.radioButton_6.setChecked(True)
        self.time_disabeled_2 = True
        self.uished_but.pushButton_2.clicked.connect(self.set_en_2)
        self.date_en = False
        self.interval_en = False
        self.date_dis = False
        self.date_en2 = False
        self.date_dis2 = False
        self.interval_en2 = False

    def set_en_2(self):
        if self.time_disabeled_2:
            self.uished_but.label_2.setDisabled(False)
            self.uished_but.label_5.setDisabled(False)
            self.uished_but.label_6.setDisabled(False)
            self.uished_but.radioButton_4.setDisabled(False)
            self.uished_but.radioButton_5.setDisabled(False)
            self.uished_but.radioButton_6.setDisabled(False)
            self.uished_but.pushButton_2.setText('-')
            self.uished_but.dateTimeEdit_2.setDisabled(False)
            self.uished_but.dateTimeEdit_4.setDisabled(False)
            self.time_disabeled_2 = False
        else:
            self.uished_but.label_2.setDisabled(True)
            self.uished_but.label_5.setDisabled(True)
            self.uished_but.label_6.setDisabled(True)
            self.uished_but.radioButton_4.setDisabled(True)
            self.uished_but.radioButton_5.setDisabled(True)
            self.uished_but.radioButton_6.setDisabled(True)
            self.uished_but.pushButton_2.setText('+')
            self.uished_but.dateTimeEdit_2.setDisabled(True)
            self.uished_but.dateTimeEdit_4.setDisabled(True)
            self.time_disabeled_2= True

    def start_connect(self):
        self.s = mikr_api.main(conf.r1_ipaddr)
        if not self.s:
            self.uimessage.label.setText('Нет соединения!!!!')
            self.uimessage.pushButton.clicked.connect(self.windowmessage.close)
            self.windowmessage.show()
            self.logger.critical(' Соединение с mikrotik не установилась!')
            sys.exit(self.app.exec_())
        self.router = mikr_api.ApiRos(self.s)
        self.logger.debug(' Соединение по сети прошло успешно')

    def login(self):
        self.logger.debug(' Попытка логина (авторизация)....')
        with io.StringIO() as buf, redirect_stdout(buf):
            try:
                self.router.login(conf.r1_login, conf.r1_passwd1)
            except AttributeError:
                self.uimessage.label.setText('    Не авторизован!')
                self.uimessage.pushButton.clicked.connect(self.windowmessage.close)
                self.windowmessage.show()
                sys.exit(self.app.exec_())
                sys.exit()
            output = buf.getvalue()
            if ">>> =message=cannot log in" in output.split('\n'):
                self.logger.critical(' Логин или пароль не верен!')
                self.uimessage.label.setText('    Не авторизован!')
                self.uimessage.pushButton.clicked.connect(self.windowmessage.close)
                self.windowmessage.show()
                sys.exit(self.app.exec_())
                sys.exit()
            self.logger.debug(' Логин прошел успешно')

    def set_combo_box(self):
        self.Mui.comboBox.clear()
        self.Mui.comboBox.addItem('None')
        for host in self.hosts_dict:
            self.Mui.comboBox.addItem(self.hosts_dict[host]['host-name'])

    def run(self):
        self.set_combo_box()
        self.logger.debug('заполняем выпадающий список')
        self.Mwindow.show()
        sys.exit(self.app.exec_())

    def button1(self):
        self.Mui.comboBox.close()
        self.Mui.label.setText('Выбран хост:')
        self.Mui.label_2.setText(self.Mui.comboBox.currentText())
        if self.Mui.comboBox.currentText() == 'None':
            if self.windowbut1:
                self.windowbut1.hide()
            self.logger.debug(' host- none- warning')
            self.uimessage.label.setText('   ВЫБЕРИТЕ ХОСТ!!!\nЕсли хостов нет -\nпопробуйте\n'
                                         'переподключить\nустройство к сети!')
            self.uimessage.pushButton.clicked.connect(self.windowmessage.hide)
            self.windowmessage.show()
            return
        self.windowbut1.move(700, 300)
        self.windowbut2.close()
        if self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'block'):
            self.dynamic()
            self.uibut1.pushButton_2.setText("unblock inet")
            self.uibut1.pushButton_3.setDisabled(True)
            self.uibut1.pushButton_4.setDisabled(True)
        elif self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'sched'):
            self.uibut1.pushButton.setDisabled(True)
            self.uibut1.pushButton_2.setDisabled(True)
            self.uibut1.pushButton_3.setDisabled(True)
            self.uibut1.pushButton_4.setDisabled(False)
        else:
            self.uibut1.pushButton_2.setText("block inet")
            self.uibut1.pushButton_3.setDisabled(False)
            self.uibut1.pushButton_4.setDisabled(False)
            self.dynamic()
        if self.windowmessage:
            self.windowmessage.hide()
        self.logger.debug('modify "' + self.Mui.comboBox.currentText() + '" host')
        self.windowbut1.setWindowTitle(self.Mui.comboBox.currentText())
        self.uibut1.hostname = self.Mui.comboBox.currentText()
        self.windowbut1.show()

    def dynamic(self):
        try:
            if self.hosts_dict[self.Mui.comboBox.currentText()]['dynamic'] == 'false':
                self.uibut1.pushButton.setText('already static')
                self.uibut1.pushButton.setDisabled(True)
                self.uibut1.pushButton_3.setDisabled(False)
                self.uibut1.pushButton_2.setDisabled(False)
                self.uibut1.pushButton_4.setDisabled(False)
            else:
                self.uibut1.pushButton_4.setDisabled(True)
                self.uibut1.pushButton.setText('make static')
                self.uibut1.pushButton_2.setDisabled(True)
                self.uibut1.pushButton.setDisabled(False)
                self.uibut1.pushButton_3.setDisabled(True)
        except KeyError:
            self.no_shuch_host()

    def button3(self):
        self.logger.debug('"Логи"')
        if self.windowmessage:
            self.windowmessage.hide()
        if self.windowbut1:
            self.windowbut1.hide()
        self.windowbut3.show()

    def pushbuttonbut1_1(self):
        self.logger.debug('make static "' + self.Mui.comboBox.currentText() + '" host')
        self.router_hosts.make_static(self.Mui.comboBox.currentText())
        self.start_connect()
        self.login()
        self.router_hosts = dhcp_hosts.DhcpHosts(self.router)
        self.hosts_dict = self.router_hosts.hosts
        self.dynamic()

    def pushbuttonbut1_2(self):
        self.windowbut1.close()
        self.windowshed_but.close()
        self.router_filter = filter.Filter(self.router)
        if self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'sched'):
            self.uibut1.pushButton_2.setDisabled(True)
            self.uibut1.pushButton_3.setDisabled(True)
        else:
            self.buttonbut1_2()

    def buttonbut1_2(self):
        if self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'block'):
            self.logger.debug('turn on internet "' + self.Mui.comboBox.currentText() + '" enable host in firewall')
            self.router_filter.delete_rule(self.Mui.comboBox.currentText(), 'block')
            self.uibut1.pushButton_2.setText("block inet")
            self.uibut1.pushButton_3.setDisabled(False)
            self.uibut1.pushButton_4.setDisabled(False)
        else:
            self.logger.debug('turn off internet "' + self.Mui.comboBox.currentText() + '" disable host in firewall')
            self.router_filter.forwardblock(self.Mui.comboBox.currentText(), 'block')
            self.uibut1.pushButton_2.setText("unblock inet")
            self.uibut1.pushButton_3.setDisabled(True)
            self.uibut1.pushButton_4.setDisabled(True)

    def pushbuttonbut1_3(self):
        self.windowbut1.hide()
        self.logger.debug('remove static lease host "' + self.Mui.comboBox.currentText() + '"')
        self.router_hosts.remove_static(self.Mui.comboBox.currentText())
        self.refresh()
        self.uimessage.label.setText('Удалено!\nНужно будет\nпереподключить\nустройства к сети'
                                     '\nдля дальнейшей\nработы!')
        self.uimessage.pushButton.clicked.connect(self.windowmessage.hide)
        self.windowmessage.show()

    def pushbuttonbut1_4(self):
        self.windowbut2.move(800, 300)
        self.windowbut2.setWindowTitle('Расписание')
        self.uibut2.pushButton.setText('Настроить')
        if self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'sched'):
            self.logger.debug('Правила в firewall уже созданы')
            self.uibut2.pushButton_2.setDisabled(False)
            self.uibut2.pushButton_3.setDisabled(True)
            self.uibut2.pushButton_4.setDisabled(False)
        self.uibut2.pushButton_2.setText("Включить")
        self.uibut2.pushButton_3.setText("Выключить")
        self.uibut2.pushButton_4.setText('Удалить')
        self.windowbut1.close()
        self.windowbut2.show()

    def pushbuttonbut2_1(self):
        self.uished_but.pushButton.clicked.connect(self.set_time)
        self.date_en, self.date_dis, self.interval_en = self.show_current_sched_rules('Enable_1', 'Disable_1')
        self.date_en2, self.date_dis2, self.interval_en2 = self.show_current_sched_rules('Enable_2', 'Disable_2')
        if self.date_en:
            self.get_time(self.date_en, self.date_dis, self.uished_but.dateTimeEdit, self.uished_but.dateTimeEdit_3)
        if self.date_en2:
            self.get_time(self.date_en2, self.date_dis2, self.uished_but.dateTimeEdit_2, self.uished_but.dateTimeEdit_4)
        self.set_rbut(self.uished_but.radioButton, self.uished_but.radioButton_2, self.uished_but.radioButton_3,
                      self.interval_en)
        self.set_rbut(self.uished_but.radioButton_6, self.uished_but.radioButton_5, self.uished_but.radioButton_4,
                      self.interval_en2)
        self.windowshed_but.show()

    def show_current_sched_rules(self, first, second):
        date_en, interval = self.scheduler.show_shed(self.Mui.comboBox.currentText(), first)
        date_dis, interval = self.scheduler.show_shed(self.Mui.comboBox.currentText(), second)
        return date_en, date_dis, interval

    def get_time(self, de, dd, qdt1, qdt2):
        date_enable = QtCore.QDateTime(QtCore.QDate(de[2], de[1], de[0]), QtCore.QTime(de[3], de[4], de[5]))
        date_disable = QtCore.QDateTime(QtCore.QDate(dd[2], dd[1], dd[0]), QtCore.QTime(dd[3], dd[4], dd[5]))
        qdt1.setDateTime(date_enable)
        qdt2.setDateTime(date_disable)

    def set_rbut(self, but1, but2, but3, interval):
        if interval == '1d':
            but1.setChecked(True)
        elif interval == '1w':
            but2.setChecked(True)
        else:
            but3.setChecked(True)

    def set_time(self):
        self.Mui.pushButton.setText('wait...')
        self.Mui.pushButton.setDisabled(True)
        self.windowbut2.close()
        self.windowshed_but.close()
        QtCore.QTimer.singleShot(4000, self.unhide)
        if not self.router_filter.isblocked(self.Mui.comboBox.currentText(), 'sched'):
            self.router_filter.forwardblock(self.Mui.comboBox.currentText(), 'sched')
            self.router_filter.disable_rule(self.Mui.comboBox.currentText(), 'sched')
        self.uibut2.pushButton.setDisabled(True)
        self.uibut2.pushButton_2.setDisabled(False)
        self.uibut2.pushButton_3.setDisabled(True)
        self.uibut2.pushButton_4.setDisabled(False)
        if self.date_en:
            self.delete_old_rules('Enable_1', 'Disable_1')
        if self.date_en2:
            self.delete_old_rules('Enable_2', 'Disable_2')
        self.init_script('Enable_1', 'Disable_1')
        self.date_en = self.uished_but.dateTimeEdit.dateTime().toString(format('MM*dd/yyyy*hh:mm:ss'))
        self.date_dis = self.uished_but.dateTimeEdit_3.dateTime().toString(format('MM*dd/yyyy*hh:mm:ss'))
        self.interval_en = self.check_button(self.uished_but.radioButton, self.uished_but.radioButton_2)
        self.scheduler.make_sched(self.Mui.comboBox.currentText(), self.date_en, self.interval_en, 'Enable_1')
        self.scheduler.make_sched(self.Mui.comboBox.currentText(), self.date_dis, self.interval_en, 'Disable_1')
        if not self.time_disabeled_2:
            self.init_script('Enable_2', 'Disable_2')
            self.date_en2 = self.uished_but.dateTimeEdit_2.dateTime().toString(format('MM*dd/yyyy*hh:mm:ss'))
            self.date_dis2 = self.uished_but.dateTimeEdit_4.dateTime().toString(format('MM*dd/yyyy*hh:mm:ss'))
            self.interval_en2 = self.check_button(self.uished_but.radioButton_6, self.uished_but.radioButton_5)
            self.scheduler.make_sched(self.Mui.comboBox.currentText(), self.date_en2, self.interval_en2, 'Enable_2')
            self.scheduler.make_sched(self.Mui.comboBox.currentText(), self.date_dis2, self.interval_en2, 'Disable_2')

    def unhide(self):
        self.Mui.pushButton.setText('Изменить')
        self.Mui.pushButton.setDisabled(False)
        self.uibut2.pushButton.setText('Настроить')
        self.uibut2.pushButton.setDisabled(False)

    def init_script(self, first, second):
        if not self.wwscript.script_is_here(self.Mui.comboBox.currentText(), first):
            self.wwscript.make_script(self.Mui.comboBox.currentText(),
                                      self.hosts_dict[self.Mui.comboBox.currentText()]['address'], first, 'no')
            self.wwscript.make_script(self.Mui.comboBox.currentText(),
                                      self.hosts_dict[self.Mui.comboBox.currentText()]['address'], second, 'yes')

    def delete_old_rules(self, first, second):
        self.scheduler.remove_shed(self.Mui.comboBox.currentText(), first)
        self.scheduler.remove_shed(self.Mui.comboBox.currentText(), second)
        self.wwscript.remove_script(self.Mui.comboBox.currentText(), first)
        self.wwscript.remove_script(self.Mui.comboBox.currentText(), second)

    def check_button(self, rbut1, rbut2):
        if rbut1.isChecked():
            interval = '1d 00:00:00'
        elif rbut2.isChecked():
            interval = '7d 00:00:00'
        else:
            interval = '365d 00:00:00'
        return interval

    def pushbuttonbut2_2(self):
        self.change_stat('no')
        self.uibut2.pushButton_2.setDisabled(True)
        self.uibut2.pushButton_3.setDisabled(False)

    def change_stat(self, disable='yes'):
        self.scheduler.modify_shed(self.Mui.comboBox.currentText(), 'Enable_1', disable)
        self.scheduler.modify_shed(self.Mui.comboBox.currentText(), 'Disable_1', disable)
        self.scheduler.modify_shed(self.Mui.comboBox.currentText(), 'Enable_2', disable)
        self.scheduler.modify_shed(self.Mui.comboBox.currentText(), 'Disable_2', disable)

    def pushbuttonbut2_3(self):
        self.change_stat()
        self.uibut2.pushButton_2.setDisabled(False)
        self.uibut2.pushButton_3.setDisabled(True)

    def pushbuttonbut2_4(self):
        self.windowshed_but.close()
        self.uibut2.pushButton.setText('wait...')
        self.uibut2.pushButton.setDisabled(True)
        self.Mui.pushButton.setText('wait...')
        self.Mui.pushButton.setDisabled(True)
        QtCore.QTimer.singleShot(4000, self.unhide)
        self.delete_old_rules('Enable_1', 'Disable_1')
        self.delete_old_rules('Enable_2', 'Disable_2')
        self.router_filter.delete_rule(self.Mui.comboBox.currentText(), 'sched')
        self.uibut2.pushButton_2.setDisabled(True)
        self.uibut2.pushButton_3.setDisabled(True)
        self.uibut2.pushButton_4.setDisabled(True)

    def refresh(self):
        self.logger.debug(' refresh button pressed')
        self.logger.debug(' Restart')
        self.Mui.comboBox.clear()
        self.Mui.label_2.setText('')
        self.Mui.label.setText('Выберите хост:')
        self.Mui.comboBox.show()
        self.start_connect()
        self.login()
        self.router_hosts = dhcp_hosts.DhcpHosts(self.router)
        self.hosts_dict = self.router_hosts.hosts
        self.set_combo_box()
        self.windowbut1.close()
        self.windowbut2.close()
        self.windowbut3.close()
        self.windowshed_but.close()

    def no_shuch_host(self):
        self.uimessage.label.setText('Нажмите "Обновить"')
        self.uimessage.pushButton.clicked.connect(self.windowmessage.close)
        self.windowmessage.show()


class Writer:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.textBrowser.appendPlainText(text)


if __name__ == '__main__':
    logging.basicConfig(filename='mikrotik.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.debug(' Start')
    widget = MainWindow()
    widget.run()


File: /mainwin.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untilted.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 155)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 70, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 85, 27))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 27))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 80, 27))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 70, 180, 27))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mikrotik host control"))
        self.pushButton.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_3.setText(_translate("MainWindow", "Логи"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить список хостов"))
        self.label.setText(_translate("MainWindow", "Выберите хост:"))




File: /message.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'host.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 150)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 100))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 105, 40, 35))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Сообщение:"))
        self.label.setText(_translate("Form", "message"))
        self.pushButton.setText(_translate("Form", "OK"))



File: /mikr_api.py
#!/usr/bin/python3

import sys, time, binascii, socket, select
import hashlib
import io

from contextlib import redirect_stdout
from re import match
import logging

class ApiRos:
    "Routeros api"

    def __init__(self, sk):
        self.sk = sk
        self.currenttag = 0

    def login(self, username, pwd):
        for repl, attrs in self.talk(["/login"]):
            chal = binascii.unhexlify((attrs['=ret']).encode('UTF-8'))
        md = hashlib.md5()
        md.update(b'\x00')
        md.update(pwd.encode('UTF-8'))
        md.update(chal)
        self.talk(["/login", "=name=" + username,
                   "=response=00" + binascii.hexlify(md.digest()).decode('UTF-8')])


    def talk(self, words):
        if self.writeSentence(words) == 0:
            return
        r = []
        while True:
            i = self.readSentence()
            if len(i) == 0:
                continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if j == -1:
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j + 1:]
            r.append((reply, attrs))
            if reply == '!done':
                return r

    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret

    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '':
                return r
            r.append(w)

    def readall(self):
        r = []
        while True:
            i = self.readSentence()
            if len(i) == 0:
                continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if j == -1:
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j + 1:]
            r.append((reply, attrs))
            if reply == '!done':
                return r

    def writeWord(self, w):
        print(("<<< " + w))
        self.writeLen(len(w))
        self.writeStr(w)

    def readWord(self):
        ret = self.readStr(self.readLen())
        print((">>> " + ret))
        return ret

    def writeLen(self, l):
        if l < 0x80:
            self.writeStr(chr(l))
        elif l < 0x4000:
            l |= 0x8000
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        else:
            self.writeStr(chr(0xF0))
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))

    def readLen(self):
        c = ord(self.readStr(1))
        if (c & 0x80) == 0x00:
            pass
        elif (c & 0xC0) == 0x80:
            c &= ~0xC0
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xE0) == 0xC0:
            c &= ~0xE0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xF0) == 0xE0:
            c &= ~0xF0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xF8) == 0xF0:
            c = ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        return c

    def writeStr(self, str):
        n = 0
        while n < len(str):
            r = self.sk.send(bytes(str[n:], 'UTF-8'))
            if r == 0:
                raise RuntimeError("connection closed by remote end")
            n += r

    def readStr(self, length):
        ret = ''
        while len(ret) < length:
            s = self.sk.recv(length - len(ret))
            if s == '':
                raise RuntimeError("connection closed by remote end")
            ret += s.decode('UTF-8', 'replace')
        return ret

    def talk_buff(self, question):
        logging.debug('Отправляю запрос {}'.format(question))
        with io.StringIO() as buf, redirect_stdout(buf):
            self.writeSentence(question)
            self.readall()
            answer = buf.getvalue()
        logging.debug('Получен ответ {}'.format(answer))
        if '>>> =message=failure: item with such name already exists' in answer.split('\n') or \
                '>>> =message=failure: item with this name already exists' in answer.split('\n'):
            logging.warning('Указанный item уже существует!!!')
            return True
        else:
            return False

def main(ipaddr):
    s = None
    for res in socket.getaddrinfo(ipaddr, "8728", socket.AF_INET, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            print('could not open socket - {}'.format(msg))
            continue
        break
    if __name__ == '__main__' and s is None:
        sys.exit(1)

    return s

def interactive():
    s = main(sys.argv[1])
    apiros = ApiRos(s)
    apiros.login(sys.argv[2], sys.argv[3])

    inputsentence = []

    while True:
        r = select.select([s, sys.stdin], [], [], None)
        if s in r[0]:
            # something to read in socket, read sentence
            x = apiros.readSentence()

        if sys.stdin in r[0]:
            # read line from input and strip off newline
            l = sys.stdin.readline()
            l = l[:-1]

            # if empty line, send sentence and start with new
            # otherwise append to input sentence
            if l == '':
                apiros.writeSentence(inputsentence)
                inputsentence = []
            else:
                inputsentence.append(l)


if __name__ == '__main__':
    interactive()


File: /README.md
# study

Программа работает с Lease dhcp сервера, задает статику\удаляет lease

Обойти статику на dhcp-сервере можно статикой на устройстве, поэтому нужно выполнить:
https://wiki.mikrotik.com/wiki/How_to_block_non_DHCP_clients_without_the_firewall


File: /same.py
import logging
import io
from contextlib import redirect_stdout
from re import match


class Same:

    def __init__(self, router):
        self.router = router

    def make(self, *args):
        with io.StringIO() as buf, redirect_stdout(buf):
            if not self.router.talk(args):
                logging.debug('Already exist')
            self.answer = buf.getvalue()
            logging.debug(self.answer)
            if ">>> !re" in self.answer.split('\n'):
                for line in self.answer.split('\n'):
                    if match('^.*\.id.*', line):
                        return match('^.*\.id=(.*)', line).group(1)
            else:
                return False

    def getanswer(self, *args):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.router.talk(args)
            return buf.getvalue()


File: /scheduler.py
import same
import logging
from re import match

monts = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
         '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

monts_rev = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
             'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}


def make_day(input_date):
    day = monts[input_date.split('*')[0]] + '/' + input_date.split('*')[1]
    return day


class Scheduler(same.Same):
    def __init__(self, router):
        super().__init__(router)

    def make_sched(self, host, date, interv, method):
        self.make('/system/scheduler/add', '=name={}_'.format(method) + host,
                  '=start-date=' + make_day(date), '=start-time=' + date.split('*')[2],
                  '=interval=' + interv, '=on-event={}_'.format(method) + host, '=disabled=yes')

    def remove_shed(self, host, method):
        shed_id = self.make('/system/scheduler/print', '?name={}_'.format(method) + host)
        if shed_id:
            self.make('/system/scheduler/remove', '=.id=' + shed_id)

    def show_shed(self, host, method):
        answer = self.getanswer('/system/scheduler/print', '?name={}_'.format(method) + host)
        logging.debug(answer)
        if ">>> !re" in answer.split('\n'):
            for line in answer.split('\n'):
                if match('^.*start-date=.*', line):
                    shed_startd = match('^.*start-date=(.*)', line).group(1)
                if match('^.*start-time=.*', line):
                    shed_startt = match('^.*start-time=(.*)', line).group(1)
                if match('^.*interval=.*', line):
                    shed_interv = match('^.*interval=(.*)', line).group(1)
            return [int(shed_startd.split('/')[1]), int(monts_rev[shed_startd.split('/')[0]]),
                    int(shed_startd.split('/')[2]), int(shed_startt.split(':')[0]),
                    int(shed_startt.split(':')[1]), int(shed_startt.split(':')[0])], shed_interv
        else:
            return False, False

    def modify_shed(self, host, method, disable='yes'):
        shed_id = self.make('/system/scheduler/print', '?name={}_'.format(method) + host)
        if shed_id:
            self.make('/system/scheduler/set', '=.id=' + shed_id, '=disabled='+disable)


File: /sched_but.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 381)
        Form.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 350, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 180, 31, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 30, 91, 21))
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 30, 194, 27))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 151, 21))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(150, 90, 117, 22))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 120, 117, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 150, 117, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(90, 60, 194, 27))
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 91, 21))
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_4.setGeometry(QtCore.QRect(90, 230, 194, 27))
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(90, 200, 194, 27))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 200, 91, 21))
        self.label_2.setObjectName("label_2")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setGeometry(QtCore.QRect(150, 320, 117, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(150, 290, 117, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Form)
        self.radioButton_6.setGeometry(QtCore.QRect(150, 260, 117, 22))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 260, 151, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 230, 91, 21))
        self.label_6.setObjectName("label_6")
        self.dateTimeEdit.setDisplayFormat('dd.MM.yyyy hh:mm')
        self.dateTimeEdit_2.setDisplayFormat('dd.MM.yyyy hh:mm')
        self.dateTimeEdit_3.setDisplayFormat('dd.MM.yyyy hh:mm')
        self.dateTimeEdit_4.setDisplayFormat('dd.MM.yyyy hh:mm')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Расписание"))
        self.pushButton.setText(_translate("Form", "Установить"))
        self.pushButton_2.setText(_translate("Form", "+"))
        self.label_7.setText(_translate("Form", "Format: day.month.year hour:min"))
        self.label.setText(_translate("Form", "Включить :"))
        self.label_4.setText(_translate("Form", "Повторять каждый :"))
        self.radioButton.setText(_translate("Form", "день"))
        self.radioButton_2.setText(_translate("Form", "месяц"))
        self.radioButton_3.setText(_translate("Form", "год"))
        self.label_3.setText(_translate("Form", "Отключить:"))
        self.label_2.setText(_translate("Form", "Включить :"))
        self.radioButton_4.setText(_translate("Form", "год"))
        self.radioButton_5.setText(_translate("Form", "месяц"))
        self.radioButton_6.setText(_translate("Form", "день"))
        self.label_5.setText(_translate("Form", "Повторять каждый :"))
        self.label_6.setText(_translate("Form", "Отключить:"))






File: /scirpt.py
import same


class Scripts(same.Same):

    def __init__(self, router):
        super().__init__(router)

    def make_script(self, host, addr, method, disabled='yes'):
        self.remove_script(host, method)
        self.make('/system/script/add', '=name={}_'.format(method) + host,
                  '=source=: ip firewall filter {{ set [find comment=sched_{}] '
                  'disabled={}}}'.format(addr, disabled))

    def remove_script(self, host, method):
        script_id = self.make('/system/script/print', '?name={}_'.format(method) + host)
        if script_id:
            self.make('/system/script/remove', '=.id='+script_id)

    def script_is_here(self, host, method):
        return self.make('/system/script/print', '?name={}_'.format(method) + host)


