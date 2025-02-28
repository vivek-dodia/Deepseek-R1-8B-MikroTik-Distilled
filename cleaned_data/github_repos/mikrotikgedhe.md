# Repository Information
Name: mikrotikgedhe

# Directory Structure
Directory structure:
└── github_repos/mikrotikgedhe/
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
    │   │       ├── pack-6cd2880ad53f838da41ec601fed59b09842f9d9c.idx
    │   │       └── pack-6cd2880ad53f838da41ec601fed59b09842f9d9c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── flash/
    │   └── hotspot/
    │       ├── alogin.html
    │       ├── error.html
    │       ├── errors.txt
    │       ├── img/
    │       ├── jqm/
    │       │   ├── images/
    │       │   ├── jquery.mobile-1.2.0.css
    │       │   └── jquery.mobile-1.3.1.css
    │       ├── login.html
    │       ├── logout.html
    │       ├── lv/
    │       │   ├── alogin.html
    │       │   ├── errors.txt
    │       │   ├── login.html
    │       │   ├── logout.html
    │       │   ├── radvert.html
    │       │   └── status.html
    │       ├── md5.js
    │       ├── radvert.html
    │       ├── redirect.html
    │       ├── rlogin.html
    │       ├── status.html
    │       └── xml/
    │           ├── alogin.html
    │           ├── error.html
    │           ├── flogout.html
    │           ├── login.html
    │           ├── logout.html
    │           ├── rlogin.html
    │           └── WISPAccessGatewayParam.xsd
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
	url = https://github.com/prianthon/mikrotikgedhe.git
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
0000000000000000000000000000000000000000 ae61f88d936fbafb03d4537234e25b5f6ab4a693 vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/prianthon/mikrotikgedhe.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 ae61f88d936fbafb03d4537234e25b5f6ab4a693 vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/prianthon/mikrotikgedhe.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ae61f88d936fbafb03d4537234e25b5f6ab4a693 vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/prianthon/mikrotikgedhe.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ae61f88d936fbafb03d4537234e25b5f6ab4a693 refs/remotes/origin/master


File: /.git\refs\heads\master
ae61f88d936fbafb03d4537234e25b5f6ab4a693


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /flash\hotspot\alogin.html
<html>
<head>
<title>INTERNET > LEMPARAN</title>
<meta http-equiv="refresh" content="2; url=http://wlaharwetan.desa.id/">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = 'http://wlaharwetan.desa.id/';
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Anda sudah masuk
	<br><br>
	Jika tidak terjadi sesuatu, segera klik <a href="$(link-redirect)">ini</a></td>
</tr>
</table>
</body>
</html>


File: /flash\hotspot\error.html
<html>
<head>
<title>INTERNET > ERROR</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
</head>
<body>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
Hotspot ERROR: $(error)<br>
<br>
Halaman masuk: <a href="$(link-login)">$(link-login)</a>
</td>
</tr>
</table>
</body>
</html>


File: /flash\hotspot\errors.txt
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in

# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)

internal-error = internal error ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = configuration error ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = you are not logged in (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = cannot assign ip address - no more free addresses from pool

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot service is shutting down

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = no more sessions are allowed for user $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = session limit reached ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = invalid username ($(username)): this MAC address is not yours

# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.

chap-missing = web browser did not send challenge response (try again, enable JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = invalid username or password

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = user $(username) is not allowed to log in from this MAC address

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = user $(username) has reached uptime limit
traffic-limit = user $(username) has reached traffic limit

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server is not responding

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = already authorizing, retry later

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /flash\hotspot\jqm\jquery.mobile-1.2.0.css
/*
* jQuery Mobile Framework Git Build: SHA1: b49cc06499abf8f987cf90f35349cfac0918c939 <> Date: Tue Oct 2 11:22:34 2012 -0700
* http://jquerymobile.com
*
* Copyright 2012 jQuery Foundation and other contributors
* Released under the MIT license.
* http://jquery.org/license
*
*/


/* Swatches */
/* A
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-a {
	border: 1px solid 		#005994 /*{a-bar-border}*/;
	background: 			#0093EA /*{a-bar-background-color}*/;
	color: 					#fff /*{a-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-bar-background-start}*/), to( #007dcd /*{a-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/);
}
.ui-bar-a,
.ui-bar-a input,
.ui-bar-a select,
.ui-bar-a textarea,
.ui-bar-a button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-a .ui-link-inherit {
	color: #fff /*{a-bar-color}*/;
}
.ui-bar-a a.ui-link {
	color: #7cc4e7 /*{a-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-a a.ui-link:visited {
    color: #2489ce /*{a-bar-link-visited}*/;
}
.ui-bar-a a.ui-link:hover {
	color: #2489ce /*{a-bar-link-hover}*/;
}
.ui-bar-a a.ui-link:active {
	color: #2489ce /*{a-bar-link-active}*/;
}
.ui-body-a,
.ui-overlay-a {
	border: 1px solid 		#444 /*{a-body-border}*/;
	background: 			#222 /*{a-body-background-color}*/;
	color: 					#fff /*{a-body-color}*/;
	font-weight: normal;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #444 /*{a-body-background-start}*/), to( #222 /*{a-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/);	
}
.ui-overlay-a {
	background-image: none;
	border-width: 0;
}
.ui-body-a,
.ui-body-a input,
.ui-body-a select,
.ui-body-a textarea,
.ui-body-a button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-a .ui-link-inherit {
	color: 	#fff /*{a-body-color}*/;
}
.ui-body-a .ui-link {
	color: #2489ce /*{a-body-link-color}*/;
	font-weight: bold;
}
.ui-body-a .ui-link:visited {
    color: #2489ce /*{a-body-link-visited}*/;
}
.ui-body-a .ui-link:hover {
	color: #2489ce /*{a-body-link-hover}*/;
}
.ui-body-a .ui-link:active {
	color: #2489ce /*{a-body-link-active}*/;
}
.ui-btn-up-a {
	border: 1px solid 		#cfcfcf /*{a-bup-border}*/;
	background: 			#333 /*{a-bup-background-color}*/;
	font-weight: bold;
	color: 					#111 /*{a-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff /*{a-bup-background-start}*/), to( #fff /*{a-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff /*{a-bup-background-start}*/, #fff /*{a-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff /*{a-bup-background-start}*/, #fff /*{a-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff /*{a-bup-background-start}*/, #fff /*{a-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff /*{a-bup-background-start}*/, #fff /*{a-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff /*{a-bup-background-start}*/, #fff /*{a-bup-background-end}*/);
}
.ui-btn-up-a:visited,
.ui-btn-up-a a.ui-link-inherit {
	color: 					#111 /*{a-bup-color}*/;
}
.ui-btn-hover-a {
	border: 1px solid 		#007dcd /*{a-bhover-border}*/;
	background: 			#444 /*{a-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-bhover-background-start}*/), to( #0093EA /*{a-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/);
}
.ui-btn-hover-a:visited,
.ui-btn-hover-a:hover,
.ui-btn-hover-a a.ui-link-inherit {
	color: 					#fff /*{a-bhover-color}*/;
}
.ui-btn-down-a {
	border: 1px solid 		#000 /*{a-bdown-border}*/;
	background: 			#222 /*{a-bdown-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{a-bdown-background-start}*/), to( #007dcd /*{a-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/);
}
.ui-btn-down-a:visited,
.ui-btn-down-a:hover,
.ui-btn-down-a a.ui-link-inherit {
	color: 					#fff /*{a-bdown-color}*/;
}
.ui-btn-up-a,
.ui-btn-hover-a,
.ui-btn-down-a {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* B
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-b {
	border: 1px solid 		#005994 /*{b-bar-border}*/;
	background: 			#0093EA /*{b-bar-background-color}*/;
	color: 					#fff /*{b-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{b-bar-background-start}*/), to( #007dcd /*{b-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/);
}
.ui-bar-b,
.ui-bar-b input,
.ui-bar-b select,
.ui-bar-b textarea,
.ui-bar-b button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-b .ui-link-inherit {
	color: 	#fff /*{b-bar-color}*/;
}
.ui-bar-b a.ui-link {
	color: #ddf0f8 /*{b-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-b a.ui-link:visited {
    color: #ddf0f8 /*{b-bar-link-visited}*/;
}
.ui-bar-b a.ui-link:hover {
	color: #ddf0f8 /*{b-bar-link-hover}*/;
}
.ui-bar-b a.ui-link:active {
	color: #ddf0f8 /*{b-bar-link-active}*/;
}
.ui-body-b,
.ui-overlay-b {
	border: 1px solid 		#999 /*{b-body-border}*/;
	background: 			#f3f3f3 /*{b-body-background-color}*/;
	color: 					#222 /*{b-body-color}*/;
	font-weight: normal;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ddd /*{b-body-background-start}*/), to( #ccc /*{b-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/);
}
.ui-overlay-b {
	background-image: none;
	border-width: 0;
}
.ui-body-b,
.ui-body-b input,
.ui-body-b select,
.ui-body-b textarea,
.ui-body-b button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-b .ui-link-inherit {
	color: 	#333 /*{b-body-color}*/;
}
.ui-body-b .ui-link {
	color: #2489ce /*{b-body-link-color}*/;
	font-weight: bold;
}
.ui-body-b .ui-link:visited {
    color: #2489ce /*{b-body-link-visited}*/;
}
.ui-body-b .ui-link:hover {
	color: #2489ce /*{b-body-link-hover}*/;
}
.ui-body-b .ui-link:active {
	color: #2489ce /*{b-body-link-active}*/;
}
.ui-btn-up-b {
	border: 1px solid 		#044062 /*{b-bup-border}*/;
	background: 			#396b9e /*{b-bup-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #5f9cc5 /*{b-bup-background-start}*/), to( #396b9e /*{b-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/);
}
.ui-btn-up-b:visited,
.ui-btn-up-b a.ui-link-inherit {
	color: 					#fff /*{b-bup-color}*/;
}
.ui-btn-hover-b {
	border: 1px solid 		#00415e /*{b-bhover-border}*/;
	background: 			#4b88b6 /*{b-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #6facd5 /*{b-bhover-background-start}*/), to( #4272a4 /*{b-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/);
}
.ui-btn-hover-b:visited,
.ui-btn-hover-b:hover,
.ui-btn-hover-b a.ui-link-inherit {
	color: 					#fff /*{b-bhover-color}*/;
}
.ui-btn-down-b {
	border: 1px solid 		#225377 /*{b-bdown-border}*/;
	background: 			#4e89c5 /*{b-bdown-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #295b8e /*{b-bdown-background-start}*/), to( #3e79b5 /*{b-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/);
}
.ui-btn-down-b:visited,
.ui-btn-down-b:hover,
.ui-btn-down-b a.ui-link-inherit {
	color: 					#fff /*{b-bdown-color}*/;
}
.ui-btn-up-b,
.ui-btn-hover-b,
.ui-btn-down-b {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* C
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-c {
	border: 1px solid 		#b3b3b3 /*{c-bar-border}*/;
	background: 			#eee /*{c-bar-background-color}*/;
	color: 					#3e3e3e /*{c-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #f0f0f0 /*{c-bar-background-start}*/), to( #ddd /*{c-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/);
}
.ui-bar-c .ui-link-inherit {
	color: 	#3e3e3e /*{c-bar-color}*/;
}
.ui-bar-c a.ui-link {
	color: #7cc4e7 /*{c-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-c a.ui-link:visited {
    color: #2489ce /*{c-bar-link-visited}*/;
}
.ui-bar-c a.ui-link:hover {
	color: #2489ce /*{c-bar-link-hover}*/;
}
.ui-bar-c a.ui-link:active {
	color: #2489ce /*{c-bar-link-active}*/;
}
.ui-bar-c,
.ui-bar-c input,
.ui-bar-c select,
.ui-bar-c textarea,
.ui-bar-c button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-c,
.ui-overlay-c {
	border: 1px solid 		#aaa /*{c-body-border}*/;
	color: 					#333 /*{c-body-color}*/;
	background: 			#eee /*{c-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #eee /*{c-body-background-start}*/), to( #eee /*{c-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/);
}
.ui-overlay-c {
	background-image: none;
	border-width: 0;
}
.ui-body-c,
.ui-body-c input,
.ui-body-c select,
.ui-body-c textarea,
.ui-body-c button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-c .ui-link-inherit {
	color: 	#333 /*{c-body-color}*/;
}
.ui-body-c .ui-link {
	color: #007dcd /*{c-body-link-color}*/;
	font-weight: bold;
}
.ui-body-c .ui-link:visited {
    color: #007dcd /*{c-body-link-visited}*/;
}
.ui-body-c .ui-link:hover {
	color: #0093EA /*{c-body-link-hover}*/;
}
.ui-body-c .ui-link:active {
	color: #007dcd /*{c-body-link-active}*/;
}
.ui-btn-up-c {
	border: 1px solid 		#ccc /*{c-bup-border}*/;
	background: 			#eee /*{c-bup-background-color}*/;
	font-weight: bold;
	color: 					#222 /*{c-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff /*{c-bup-background-start}*/), to( #fff /*{c-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/);
}
.ui-btn-up-c:visited,
.ui-btn-up-c a.ui-link-inherit {
	color: 					#2f3e46 /*{c-bup-color}*/;
}
.ui-btn-hover-c {
	border: 1px solid 		#bbb /*{c-bhover-border}*/;
	background: 			#dfdfdf /*{c-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{c-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{c-bhover-background-start}*/), to( #0093EA /*{c-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/);
}
.ui-btn-hover-c:visited,
.ui-btn-hover-c:hover,
.ui-btn-hover-c a.ui-link-inherit {
	color: 					#fff /*{c-bhover-color}*/;
}
.ui-btn-down-c {
	border: 1px solid 		#bbb /*{c-bdown-border}*/;
	background: 			#d6d6d6 /*{c-bdown-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{c-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{c-bdown-background-start}*/), to( #007dcd /*{c-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/);
}
.ui-btn-down-c:visited,
.ui-btn-down-c:hover,
.ui-btn-down-c a.ui-link-inherit {
	color: 					#fff /*{c-bdown-color}*/;
}
.ui-btn-up-c,
.ui-btn-hover-c,
.ui-btn-down-c {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* D
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-d {
	border: 1px solid 		#bbb /*{d-bar-border}*/;
	background: 			#bbb /*{d-bar-background-color}*/;
	color: 					#333 /*{d-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ddd /*{d-bar-background-start}*/), to( #bbb /*{d-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/);
}
.ui-bar-d,
.ui-bar-d input,
.ui-bar-d select,
.ui-bar-d textarea,
.ui-bar-d button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-d .ui-link-inherit {
	color: 	#333 /*{d-bar-color}*/;
}
.ui-bar-d a.ui-link {
	color: #2489ce /*{d-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-d a.ui-link:visited {
    color: #2489ce /*{d-bar-link-visited}*/;
}
.ui-bar-d a.ui-link:hover {
	color: #2489ce /*{d-bar-link-hover}*/;
}
.ui-bar-d a.ui-link:active {
	color: #2489ce /*{d-bar-link-active}*/;
}
.ui-body-d,
.ui-overlay-d {
	border: 1px solid 		#bbb /*{d-body-border}*/;
	color: 					#333 /*{d-body-color}*/;
	background: 			#fff /*{d-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff /*{d-body-background-start}*/), to( #fff /*{d-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/);
}
.ui-overlay-d {
	background-image: none;
	border-width: 0;
}
.ui-body-d,
.ui-body-d input,
.ui-body-d select,
.ui-body-d textarea,
.ui-body-d button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-d .ui-link-inherit {
	color: 	#333 /*{d-body-color}*/;
}
.ui-body-d .ui-link {
	color: #2489ce /*{d-body-link-color}*/;
	font-weight: bold;
}
.ui-body-d .ui-link:visited {
    color: #2489ce /*{d-body-link-visited}*/;
}
.ui-body-d .ui-link:hover {
	color: #2489ce /*{d-body-link-hover}*/;
}
.ui-body-d .ui-link:active {
	color: #2489ce /*{d-body-link-active}*/;
}
.ui-btn-up-d {
	border: 1px solid 		#bbb /*{d-bup-border}*/;
	background: 			#fff /*{d-bup-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fafafa /*{d-bup-background-start}*/), to( #f6f6f6 /*{d-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/);
}
.ui-btn-up-d:visited,
.ui-btn-up-d a.ui-link-inherit {
	color: 					#333 /*{d-bup-color}*/;
}
.ui-btn-hover-d {
	border: 1px solid 		#aaa /*{d-bhover-border}*/;
	background: 			#eee /*{d-bhover-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bhover-color}*/;
	cursor: pointer;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #eee /*{d-bhover-background-start}*/), to( #fff /*{d-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/);
}
.ui-btn-hover-d:visited,
.ui-btn-hover-d:hover,
.ui-btn-hover-d a.ui-link-inherit {
	color: 					#333 /*{d-bhover-color}*/;
}
.ui-btn-down-d {
	border: 1px solid 		#aaa /*{d-bdown-border}*/;
	background: 			#eee /*{d-bdown-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #e5e5e5 /*{d-bdown-background-start}*/), to( #f2f2f2 /*{d-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/);
}
.ui-btn-down-d:visited,
.ui-btn-down-d:hover,
.ui-btn-down-d a.ui-link-inherit {
	color: 					#333 /*{d-bdown-color}*/;
}
.ui-btn-up-d,
.ui-btn-hover-d,
.ui-btn-down-d {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* E
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-e {
	border: 1px solid 		#f7c942 /*{e-bar-border}*/;
	background: 			#fadb4e /*{e-bar-background-color}*/;
	color: 					#333 /*{e-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fceda7 /*{e-bar-background-start}*/), to( #fbef7e /*{e-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/);
}
.ui-bar-e,
.ui-bar-e input,
.ui-bar-e select,
.ui-bar-e textarea,
.ui-bar-e button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-e .ui-link-inherit {
	color: 	#333 /*{e-bar-color}*/;
}
.ui-bar-e a.ui-link {
	color: #2489ce /*{e-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-e a.ui-link:visited {
    color: #2489ce /*{e-bar-link-visited}*/;
}
.ui-bar-e a.ui-link:hover {
	color: #2489ce /*{e-bar-link-hover}*/;
}
.ui-bar-e a.ui-link:active {
	color: #2489ce /*{e-bar-link-active}*/;
}
.ui-body-e,
.ui-overlay-e {
	border: 1px solid 		#f7c942 /*{e-body-border}*/;
	color: 					#222 /*{e-body-color}*/;
	background: 			#fff9df /*{e-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fffadf /*{e-body-background-start}*/), to( #fff3a5 /*{e-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/);
}
.ui-overlay-e {
	background-image: none;
	border-width: 0;
}
.ui-body-e,
.ui-body-e input,
.ui-body-e select,
.ui-body-e textarea,
.ui-body-e button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-e .ui-link-inherit {
	color: 	#222 /*{e-body-color}*/;
}
.ui-body-e .ui-link {
	color: #2489ce /*{e-body-link-color}*/;
	font-weight: bold;
}
.ui-body-e .ui-link:visited {
    color: #2489ce /*{e-body-link-visited}*/;
}
.ui-body-e .ui-link:hover {
	color: #2489ce /*{e-body-link-hover}*/;
}
.ui-body-e .ui-link:active {
	color: #2489ce /*{e-body-link-active}*/;
}
.ui-btn-up-e {
	border: 1px solid 		#f4c63f /*{e-bup-border}*/;
	background: 			#fadb4e /*{e-bup-background-color}*/;
	font-weight: bold;
	color: 					#222 /*{e-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ffefaa /*{e-bup-background-start}*/), to( #ffe155 /*{e-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/);
}
.ui-btn-up-e:visited,
.ui-btn-up-e a.ui-link-inherit {
	color: 					#222 /*{e-bup-color}*/;
}
.ui-btn-hover-e {
	border: 1px solid 		#f2c43d /*{e-bhover-border}*/;
	background: 			#fbe26f /*{e-bhover-background-color}*/;
	font-weight: bold;
	color: 					#111 /*{e-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff5ba /*{e-bhover-background-start}*/), to( #fbdd52 /*{e-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/);
}
.ui-btn-hover-e:visited,
.ui-btn-hover-e:hover,
.ui-btn-hover-e a.ui-link-inherit {
	color: 					#333 /*{e-bhover-color}*/;
}
.ui-btn-down-e {
	border: 1px solid 		#f2c43d /*{e-bdown-border}*/;
	background: 			#fceda7 /*{e-bdown-background-color}*/;
	font-weight: bold;
	color: 					#111 /*{e-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #f8d94c /*{e-bdown-background-start}*/), to( #fadb4e /*{e-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/);
}
.ui-btn-down-e:visited,
.ui-btn-down-e:hover,
.ui-btn-down-e a.ui-link-inherit {
	color: 					#333 /*{e-bdown-color}*/;
}
.ui-btn-up-e,
.ui-btn-hover-e,
.ui-btn-down-e {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* Structure */
/* links within "buttons" 
-----------------------------------------------------------------------------------------------------------*/
a.ui-link-inherit {
	text-decoration: none !important;
}
/* Active class used as the "on" state across all themes
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-active {
	border: 1px solid 		#0093EA /*{global-active-border}*/;
	background: 			#007dcd /*{global-active-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{global-active-color}*/;
	cursor: pointer;
	text-decoration: none;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{global-active-background-start}*/), to( #007dcd /*{global-active-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/);
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-btn-active:visited,
.ui-btn-active:hover,
.ui-btn-active a.ui-link-inherit {
	color: 					#fff /*{global-active-color}*/;
}
/* button inner top highlight
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-inner {
	border-top: 1px solid 	#fff;
	border-color: 			rgba(255,255,255,.3);
}
/* corner rounding classes
-----------------------------------------------------------------------------------------------------------*/
.ui-corner-tl {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-left-radius: 			0.2em /*{global-radii-blocks}*/;
}
.ui-corner-tr {
	-moz-border-radius-topright: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-right-radius: 			0.2em /*{global-radii-blocks}*/;
}
.ui-corner-bl {
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-blocks}*/;
}
.ui-corner-br {
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-blocks}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-blocks}*/;
}
.ui-corner-top {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-left-radius: 			0.2em /*{global-radii-blocks}*/;
	-moz-border-radius-topright: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-right-radius: 			0.2em /*{global-radii-blocks}*/;
}
.ui-corner-bottom {
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-blocks}*/;
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-blocks}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-blocks}*/;
	}
.ui-corner-right {
	-moz-border-radius-topright: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-right-radius: 			0.2em /*{global-radii-blocks}*/;
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-blocks}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-blocks}*/;
}
.ui-corner-left {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-top-left-radius: 			0.2em /*{global-radii-blocks}*/;
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-blocks}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-blocks}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-blocks}*/;
}
.ui-corner-all {
	-moz-border-radius: 				0.2em /*{global-radii-blocks}*/;
	-webkit-border-radius: 				0.2em /*{global-radii-blocks}*/;
	border-radius: 						0.2em /*{global-radii-blocks}*/;
}
.ui-corner-none {
	-moz-border-radius: 				   0;
	-webkit-border-radius: 				   0;
	border-radius: 						   0;
}
/* Form field separator
-----------------------------------------------------------------------------------------------------------*/
.ui-br {
	border-bottom: rgb(130,130,130);
	border-bottom: rgba(130,130,130,.3);
	border-bottom-width: 1px;
	border-bottom-style: solid;
}
/* Interaction cues
-----------------------------------------------------------------------------------------------------------*/
.ui-disabled {
	filter: Alpha(Opacity=30);
	opacity: .3;
	zoom: 1;
}
.ui-disabled,
.ui-disabled a {
	cursor: default !important;
	pointer-events: none;
}
/* Icons
-----------------------------------------------------------------------------------------------------------*/
.ui-icon,
.ui-icon-searchfield:after {
	background-image: url(images/icons-18-black.png) /*{global-icon-set}*/;
}
/* Alt icon color
-----------------------------------------------------------------------------------------------------------*/
.ui-icon-alt {
	background: 						#fff;
	background: 						rgba(255,255,255,.3);
	background-image: url(images/icons-18-black.png);
	background-repeat: no-repeat;
}
/* HD/"retina" sprite
-----------------------------------------------------------------------------------------------------------*/
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
       only screen and (min--moz-device-pixel-ratio: 1.5),
       only screen and (min-resolution: 240dpi) {
	
	.ui-icon-plus, .ui-icon-minus, .ui-icon-delete, .ui-icon-arrow-r,
	.ui-icon-arrow-l, .ui-icon-arrow-u, .ui-icon-arrow-d, .ui-icon-check,
	.ui-icon-gear, .ui-icon-refresh, .ui-icon-forward, .ui-icon-back,
	.ui-icon-grid, .ui-icon-star, .ui-icon-alert, .ui-icon-info, .ui-icon-home, .ui-icon-search, .ui-icon-searchfield:after, 
	.ui-icon-checkbox-off, .ui-icon-checkbox-on, .ui-icon-radio-off, .ui-icon-radio-on {
		background-image: url(images/icons-36-black.png);
		-moz-background-size: 776px 18px;
		-o-background-size: 776px 18px;
		-webkit-background-size: 776px 18px;
		background-size: 776px 18px;
	}
	.ui-icon-alt {
		background-image: url(images/icons-36-black.png);
	}
}
/* plus minus */
.ui-icon-plus {
	background-position: 	-0 50%;
}
.ui-icon-minus {
	background-position: 	-36px 50%;
}
/* delete/close */
.ui-icon-delete {
	background-position: 	-72px 50%;
}
/* arrows */
.ui-icon-arrow-r {
	background-position: 	-108px 50%;
}
.ui-icon-arrow-l {
	background-position: 	-144px 50%;
}
.ui-icon-arrow-u {
	background-position: 	-180px 50%;
}
.ui-icon-arrow-d {
	background-position: 	-216px 50%;
}
/* misc */
.ui-icon-check {
	background-position: 	-252px 50%;
}
.ui-icon-gear {
	background-position: 	-288px 50%;
}
.ui-icon-refresh {
	background-position: 	-324px 50%;
}
.ui-icon-forward {
	background-position: 	-360px 50%;
}
.ui-icon-back {
	background-position: 	-396px 50%;
}
.ui-icon-grid {
	background-position: 	-432px 50%;
}
.ui-icon-star {
	background-position: 	-468px 50%;
}
.ui-icon-alert {
	background-position: 	-504px 50%;
}
.ui-icon-info {
	background-position: 	-540px 50%;
}
.ui-icon-home {
	background-position: 	-576px 50%;
}
.ui-icon-search,
.ui-icon-searchfield:after {
	background-position: 	-612px 50%;
}
.ui-icon-checkbox-off {
	background-position: 	-684px 50%;
}
.ui-icon-checkbox-on {
	background-position: 	-648px 50%;
}
.ui-icon-radio-off {
	background-position: 	-756px 50%;
}
.ui-icon-radio-on {
	background-position: 	-720px 50%;
}
/* checks,radios */
.ui-checkbox .ui-icon,
.ui-selectmenu-list .ui-icon {
	-moz-border-radius: 3px;
	-webkit-border-radius: 3px;
	border-radius: 3px;
}
.ui-icon-checkbox-off,
.ui-icon-radio-off {
	background-color: transparent;	
}
.ui-checkbox-on .ui-icon,
.ui-radio-on .ui-icon {
	background-color: #007dcd /*{global-active-background-color}*/; /* NOTE: this hex should match the active state color. It's repeated here for cascade */
}
.ui-radio-on .ui-icon {
  border-radius: 10px;
  -moz-border-radius: 10px;
  -webkit-border-radius: 10px;
}
/* loading icon */
.ui-icon-loading {
	background: url(images/ajax-loader.gif);
	background-size: 46px 46px;
}
/* Button corner classes
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-corner-tl {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-left-radius: 			0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-tr {
	-moz-border-radius-topright: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-right-radius: 			0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-bl {
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-br {
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-buttons}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-top {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-left-radius: 			0.2em /*{global-radii-buttons}*/;
	-moz-border-radius-topright: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-right-radius: 			0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-bottom {
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-buttons}*/;
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-buttons}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-right {
	 -moz-border-radius-topright: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-right-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-right-radius: 			0.2em /*{global-radii-buttons}*/;
	-moz-border-radius-bottomright: 	0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-right-radius: 0.2em /*{global-radii-buttons}*/;
	border-bottom-right-radius: 		0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-left {
	-moz-border-radius-topleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-top-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-top-left-radius: 			0.2em /*{global-radii-buttons}*/;
	-moz-border-radius-bottomleft: 		0.2em /*{global-radii-buttons}*/;
	-webkit-border-bottom-left-radius: 	0.2em /*{global-radii-buttons}*/;
	border-bottom-left-radius: 			0.2em /*{global-radii-buttons}*/;
}
.ui-btn-corner-all {
	-moz-border-radius: 				0.2em /*{global-radii-buttons}*/;
	-webkit-border-radius: 				0.2em /*{global-radii-buttons}*/;
	border-radius: 						0.2em /*{global-radii-buttons}*/;
}
/* radius clip workaround for cleaning up corner trapping */
.ui-corner-tl,
.ui-corner-tr,
.ui-corner-bl,
.ui-corner-br,
.ui-corner-top,
.ui-corner-bottom,
.ui-corner-right,
.ui-corner-left,
.ui-corner-all,
.ui-btn-corner-tl,
.ui-btn-corner-tr,
.ui-btn-corner-bl,
.ui-btn-corner-br,
.ui-btn-corner-top,
.ui-btn-corner-bottom,
.ui-btn-corner-right,
.ui-btn-corner-left,
.ui-btn-corner-all {
  -webkit-background-clip: padding-box;
     -moz-background-clip: padding;
          background-clip: padding-box;
}
/* Overlay / modal
-----------------------------------------------------------------------------------------------------------*/
.ui-overlay {
	background: #666;
	filter: Alpha(Opacity=50);
	opacity: .5;
	position: absolute;
	width: 100%;
	height: 100%;
}
.ui-overlay-shadow {
	-moz-box-shadow: 0px 0px 12px 			rgba(0,0,0,.6);
	-webkit-box-shadow: 0px 0px 12px 		rgba(0,0,0,.6);
	box-shadow: 0px 0px 12px 				rgba(0,0,0,.6);
}
.ui-shadow {
	-moz-box-shadow: 0px 1px 1px /*{global-box-shadow-size}*/ 			rgba(0,0,0,0.2) /*{global-box-shadow-color}*/;
	-webkit-box-shadow: 0px 1px 1px /*{global-box-shadow-size}*/ 		rgba(0,0,0,0.2) /*{global-box-shadow-color}*/;
	box-shadow: 0px 1px 1px /*{global-box-shadow-size}*/ 				rgba(0,0,0,0.2) /*{global-box-shadow-color}*/;
}
.ui-bar-a .ui-shadow,
.ui-bar-b .ui-shadow ,
.ui-bar-c .ui-shadow  {
	-moz-box-shadow: 0px 1px 0 				rgba(255,255,255,.3);
	-webkit-box-shadow: 0px 1px 0 			rgba(255,255,255,.3);
	box-shadow: 0px 1px 0 					rgba(255,255,255,.3);
}
.ui-shadow-inset {
	-moz-box-shadow: inset 0px 1px 4px 		rgba(0,0,0,.2);
	-webkit-box-shadow: inset 0px 1px 4px 	rgba(0,0,0,.2);
	box-shadow: inset 0px 1px 4px 			rgba(0,0,0,.2);
}
/* Focus state - set here for specificity (note: these classes are added by JavaScript)
-----------------------------------------------------------------------------------------------------------*/
.ui-btn:focus, .ui-link-inherit:focus {
	outline: 0;
}
.ui-btn.ui-focus {
	z-index: 1;
}
.ui-focus,
.ui-btn:focus {
	-moz-box-shadow: inset 0px 0px 1px 		#007dcd /*{global-active-background-color}*/, 0px 0px 3px 		#007dcd /*{global-active-background-color}*/;
	-webkit-box-shadow: inset 0px 0px 1px 	#007dcd /*{global-active-background-color}*/, 0px 0px 3px 		#007dcd /*{global-active-background-color}*/;
	box-shadow: inset 0px 0px 1px 			#007dcd /*{global-active-background-color}*/, 0px 0px 3px 		#007dcd /*{global-active-background-color}*/;
}
.ui-input-text.ui-focus,
.ui-input-search.ui-focus {
	-moz-box-shadow: 0px 0px 1px 			#007dcd /*{global-active-background-color}*/;
	-webkit-box-shadow: 0px 0px 1px 		#007dcd /*{global-active-background-color}*/;
	box-shadow: 0px 0px 1px 					#007dcd /*{global-active-background-color}*/;	
}
/* unset box shadow in browsers that don't do it right
-----------------------------------------------------------------------------------------------------------*/
.ui-mobile-nosupport-boxshadow * {
	-moz-box-shadow: none !important;
	-webkit-box-shadow: none !important;
	box-shadow: none !important;
}
/* ...and bring back focus */
.ui-mobile-nosupport-boxshadow .ui-focus,
.ui-mobile-nosupport-boxshadow .ui-btn:focus,
.ui-mobile-nosupport-boxshadow .ui-link-inherit:focus {
	outline-width: 1px;
	outline-style: auto;
}
/* some unsets - more probably needed */
.ui-mobile, .ui-mobile body { height: 99.9%; }
.ui-mobile fieldset, .ui-page { padding: 0; margin: 0; }
.ui-mobile a img, .ui-mobile fieldset { border-width: 0; }
/* responsive page widths */
.ui-mobile-viewport { margin: 0; overflow-x: visible; -webkit-text-size-adjust: 100%; -ms-text-size-adjust:none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); }
/* Issue #2066 */
body.ui-mobile-viewport,
div.ui-mobile-viewport { overflow-x: hidden; }
/* "page" containers - full-screen views, one should always be in view post-pageload */
.ui-mobile [data-role=page], .ui-mobile [data-role=dialog], .ui-page { top: 0; left: 0; width: 100%; min-height: 100%; position: absolute; display: none; border: 0; }
.ui-mobile .ui-page-active { display: block; overflow: visible; }
/* on ios4, setting focus on the page element causes flashing during transitions when there is an outline, so we turn off outlines */
.ui-page { outline: none; }
/*orientations from js are available */
@media screen and (orientation: portrait){
.ui-mobile, .ui-mobile .ui-page { min-height: 420px; }
}
@media screen and (orientation: landscape){
.ui-mobile, .ui-mobile .ui-page { min-height: 300px; }
}
/* loading screen */
.ui-loading .ui-loader { display: block; }
.ui-loader { display: none; z-index: 9999999; position: fixed; top: 50%; left: 50%; border:0; }
.ui-loader-default { background: none; filter: Alpha(Opacity=18); opacity: .18; width: 46px; height: 46px; margin-left: -23px; margin-top: -23px; }
.ui-loader-verbose { width: 200px; filter: Alpha(Opacity=88); opacity: .88; box-shadow: 0 1px 1px -1px #fff; height: auto; margin-left: -110px; margin-top: -43px; padding: 10px; }
.ui-loader-default h1 { font-size: 0; width: 0; height: 0; overflow: hidden; }
.ui-loader-verbose h1 { font-size: 16px; margin: 0; text-align: center; }
.ui-loader .ui-icon { background-color: #000; display: block; margin: 0; width: 44px; height: 44px; padding: 1px; -webkit-border-radius: 36px; -moz-border-radius: 36px; border-radius: 36px; }
.ui-loader-verbose .ui-icon { margin: 0 auto 10px; filter: Alpha(Opacity=75); opacity: .75; }
.ui-loader-textonly { padding: 15px; margin-left: -115px; }
.ui-loader-textonly .ui-icon { display: none; }
.ui-loader-fakefix { position: absolute; }
/*fouc*/
.ui-mobile-rendering > * { visibility: hidden; }
/*headers, content panels*/
.ui-bar, .ui-body { position: relative; padding: .4em 15px; overflow: hidden; display: block; clear:both; }
.ui-bar { font-size: 16px; margin: 0; }
.ui-bar h1, .ui-bar h2, .ui-bar h3, .ui-bar h4, .ui-bar h5, .ui-bar h6 { margin: 0; padding: 0; font-size: 16px; display: inline-block; }
.ui-header, .ui-footer { position: relative; border-left-width: 0; border-right-width: 0; border-top-width: 0; zoom: 1; }
.ui-header .ui-btn-left,
.ui-header .ui-btn-right,
.ui-footer .ui-btn-left,
.ui-footer .ui-btn-right { position: absolute; top: 4px; }
.ui-header .ui-btn-left,
.ui-footer .ui-btn-left { left: 5px; }
.ui-header .ui-btn-right,
.ui-footer .ui-btn-right { right: 5px; }
.ui-footer .ui-btn-icon-notext,
.ui-header .ui-btn-icon-notext { top: 6px; }
.ui-header .ui-title, .ui-footer .ui-title { min-height: 1.1em; text-align: center; font-size: 16px; display: block; margin: .6em 30% .8em; padding: 0; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; outline: 0 !important; }
.ui-footer .ui-title { margin: .6em 15px .8em; }
/*content area*/
.ui-content { border-width: 0; overflow: visible; overflow-x: hidden; padding: 10px; }
/* icons sizing */
.ui-icon { width: 18px; height: 18px; }
/* non-js content hiding */
.ui-nojs { position: absolute; left: -9999px; }
/* accessible content hiding */
.ui-hide-label label.ui-input-text, .ui-hide-label label.ui-select, .ui-hide-label label.ui-slider, .ui-hide-label label.ui-submit, .ui-hide-label .ui-controlgroup-label,
.ui-hidden-accessible { position: absolute !important; left: -9999px; clip: rect(1px 1px 1px 1px); clip: rect(1px,1px,1px,1px); }
/* Transitions originally inspired by those from jQtouch, nice work, folks */
.ui-mobile-viewport-transitioning,
.ui-mobile-viewport-transitioning .ui-page {
	width: 100%;
	height: 100%;
	overflow: hidden;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	box-sizing: border-box;
}
.ui-page-pre-in {
	opacity: 0;
}
.in {
	-webkit-animation-timing-function: ease-out;
	-webkit-animation-duration: 350ms;
	-moz-animation-timing-function: ease-out;
	-moz-animation-duration: 350ms;
}
.out {
	-webkit-animation-timing-function: ease-in;
	-webkit-animation-duration: 225ms;
	-moz-animation-timing-function: ease-in;
	-moz-animation-duration: 225ms;
}
@-webkit-keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
@-moz-keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
@-webkit-keyframes fadeout {
    from { opacity: 1; }
    to { opacity: 0; }
}
@-moz-keyframes fadeout {
    from { opacity: 1; }
    to { opacity: 0; }
}
.fade.out {
	opacity: 0;
	-webkit-animation-duration: 125ms;
	-webkit-animation-name: fadeout;
	-moz-animation-duration: 125ms;
	-moz-animation-name: fadeout;
}
.fade.in {
	opacity: 1;
	-webkit-animation-duration: 225ms;
	-webkit-animation-name: fadein;
	-moz-animation-duration: 225ms;
	-moz-animation-name: fadein;
}
.pop {
	-webkit-transform-origin: 50% 50%;
	-moz-transform-origin: 50% 50%;
}
.pop.in {
	-webkit-transform: scale(1);
	-moz-transform: scale(1);
    opacity: 1;
	-webkit-animation-name: popin;
	-moz-animation-name: popin;
	-webkit-animation-duration: 350ms;
	-moz-animation-duration: 350ms;
}
.pop.out {
	-webkit-animation-name: fadeout;
	-moz-animation-name: fadeout;
	opacity: 0;
	-webkit-animation-duration: 100ms;
	-moz-animation-duration: 100ms;
}
.pop.in.reverse {
	-webkit-animation-name: fadein;
	-moz-animation-name: fadein;
}
.pop.out.reverse {
	-webkit-transform: scale(.8);
	-moz-transform: scale(.8);
	-webkit-animation-name: popout;
	-moz-animation-name: popout;
}
@-webkit-keyframes popin {
    from {
        -webkit-transform: scale(.8);
        opacity: 0;
    }
    to {
        -webkit-transform: scale(1);
        opacity: 1;
    }
}
@-moz-keyframes popin {
    from {
        -moz-transform: scale(.8);
        opacity: 0;
    }
    to {
        -moz-transform: scale(1);
        opacity: 1;
    }
}
@-webkit-keyframes popout {
    from {
        -webkit-transform: scale(1);
        opacity: 1;
    }
    to {
        -webkit-transform: scale(.8);
        opacity: 0;
    }
}
@-moz-keyframes popout {
    from {
        -moz-transform: scale(1);
        opacity: 1;
    }
    to {
        -moz-transform: scale(.8);
        opacity: 0;
    }
}
/* keyframes for slidein from sides */
@-webkit-keyframes slideinfromright {
    from { -webkit-transform: translateX(100%); }
    to { -webkit-transform: translateX(0); }
}
@-moz-keyframes slideinfromright {
    from { -moz-transform: translateX(100%); }
    to { -moz-transform: translateX(0); }
}
@-webkit-keyframes slideinfromleft {
    from { -webkit-transform: translateX(-100%); }
    to { -webkit-transform: translateX(0); }
}
@-moz-keyframes slideinfromleft {
    from { -moz-transform: translateX(-100%); }
    to { -moz-transform: translateX(0); }
}
/* keyframes for slideout to sides */
@-webkit-keyframes slideouttoleft {
    from { -webkit-transform: translateX(0); }
    to { -webkit-transform: translateX(-100%); }
}
@-moz-keyframes slideouttoleft {
    from { -moz-transform: translateX(0); }
    to { -moz-transform: translateX(-100%); }
}
@-webkit-keyframes slideouttoright {
    from { -webkit-transform: translateX(0); }
    to { -webkit-transform: translateX(100%); }
}
@-moz-keyframes slideouttoright {
    from { -moz-transform: translateX(0); }
    to { -moz-transform: translateX(100%); }
}
.slide.out, .slide.in {
	-webkit-animation-timing-function: ease-out;
	-webkit-animation-duration: 350ms;
	-moz-animation-timing-function: ease-out;
	-moz-animation-duration: 350ms;
}
.slide.out {
	-webkit-transform: translateX(-100%);
	-webkit-animation-name: slideouttoleft;
	-moz-transform: translateX(-100%);
	-moz-animation-name: slideouttoleft;
}
.slide.in {
	-webkit-transform: translateX(0);
	-webkit-animation-name: slideinfromright;
	-moz-transform: translateX(0);
	-moz-animation-name: slideinfromright;
}
.slide.out.reverse {
	-webkit-transform: translateX(100%);
	-webkit-animation-name: slideouttoright;
	-moz-transform: translateX(100%);
	-moz-animation-name: slideouttoright;
}
.slide.in.reverse {
	-webkit-transform: translateX(0);
	-webkit-animation-name: slideinfromleft;
	-moz-transform: translateX(0);
	-moz-animation-name: slideinfromleft;
}
.slidefade.out {
	-webkit-transform: translateX(-100%);
	-webkit-animation-name: slideouttoleft;
	-moz-transform: translateX(-100%);
	-moz-animation-name: slideouttoleft;
	-webkit-animation-duration: 225ms;
	-moz-animation-duration: 225ms;
}
.slidefade.in {
	-webkit-transform: translateX(0);
	-webkit-animation-name: fadein;
	-moz-transform: translateX(0);
	-moz-animation-name: fadein;
	-webkit-animation-duration: 200ms;
	-moz-animation-duration: 200ms;
}
.slidefade.out.reverse {
	-webkit-transform: translateX(100%);
	-webkit-animation-name: slideouttoright;
	-moz-transform: translateX(100%);
	-moz-animation-name: slideouttoright;
	-webkit-animation-duration: 200ms;
	-moz-animation-duration: 200ms;
}
.slidefade.in.reverse {
	-webkit-transform: translateX(0);
	-webkit-animation-name: fadein;
	-moz-transform: translateX(0);
	-moz-animation-name: fadein;
	-webkit-animation-duration: 200ms;
	-moz-animation-duration: 200ms;
}
/* slide down */
.slidedown.out {
	-webkit-animation-name: fadeout;
	-moz-animation-name: fadeout;
	-webkit-animation-duration: 100ms;
	-moz-animation-duration: 100ms;
}
.slidedown.in {
	-webkit-transform: translateY(0);
	-webkit-animation-name: slideinfromtop;
	-moz-transform: translateY(0);
	-moz-animation-name: slideinfromtop;
	-webkit-animation-duration: 250ms;
	-moz-animation-duration: 250ms;
}
.slidedown.in.reverse {
	-webkit-animation-name: fadein;
	-moz-animation-name: fadein;
	-webkit-animation-duration: 150ms;
	-moz-animation-duration: 150ms;
}
.slidedown.out.reverse {
	-webkit-transform: translateY(-100%);
	-moz-transform: translateY(-100%);
	-webkit-animation-name: slideouttotop;
	-moz-animation-name: slideouttotop;
	-webkit-animation-duration: 200ms;
	-moz-animation-duration: 200ms;
}
@-webkit-keyframes slideinfromtop {
    from { -webkit-transform: translateY(-100%); }
    to { -webkit-transform: translateY(0); }
}
@-moz-keyframes slideinfromtop {
    from { -moz-transform: translateY(-100%); }
    to { -moz-transform: translateY(0); }
}
@-webkit-keyframes slideouttotop {
    from { -webkit-transform: translateY(0); }
    to { -webkit-transform: translateY(-100%); }
}
@-moz-keyframes slideouttotop {
    from { -moz-transform: translateY(0); }
    to { -moz-transform: translateY(-100%); }
}
/* slide up */
.slideup.out {
	-webkit-animation-name: fadeout;
	-moz-animation-name: fadeout;
	-webkit-animation-duration: 100ms;
	-moz-animation-duration: 100ms;
}
.slideup.in {
	-webkit-transform: translateY(0);
	-webkit-animation-name: slideinfrombottom;
	-moz-transform: translateY(0);
	-moz-animation-name: slideinfrombottom;
	-webkit-animation-duration: 250ms;
	-moz-animation-duration: 250ms;
}
.slideup.in.reverse {
	-webkit-animation-name: fadein;
	-moz-animation-name: fadein;
	-webkit-animation-duration: 150ms;
	-moz-animation-duration: 150ms;
}
.slideup.out.reverse {
	-webkit-transform: translateY(100%);
	-moz-transform: translateY(100%);
	-webkit-animation-name: slideouttobottom;
	-moz-animation-name: slideouttobottom;
	-webkit-animation-duration: 200ms;
	-moz-animation-duration: 200ms;
}
@-webkit-keyframes slideinfrombottom {
    from { -webkit-transform: translateY(100%); }
    to { -webkit-transform: translateY(0); }
}
@-moz-keyframes slideinfrombottom {
    from { -moz-transform: translateY(100%); }
    to { -moz-transform: translateY(0); }
}
@-webkit-keyframes slideouttobottom {
    from { -webkit-transform: translateY(0); }
    to { -webkit-transform: translateY(100%); }
}
@-moz-keyframes slideouttobottom {
    from { -moz-transform: translateY(0); }
    to { -moz-transform: translateY(100%); }
}
/* The properties in this rule are only necessary for the 'flip' transition.
 * We need specify the perspective to create a projection matrix. This will add
 * some depth as the element flips. The depth number represents the distance of
 * the viewer from the z-plane. According to the CSS3 spec, 1000 is a moderate
 * value.
 */
.viewport-flip {
	-webkit-perspective: 1000;
	-moz-perspective: 1000;
	position: absolute;
}
.flip {
	-webkit-backface-visibility:hidden;
	-webkit-transform:translateX(0); /* Needed to work around an iOS 3.1 bug that causes listview thumbs to disappear when -webkit-visibility:hidden is used. */
	-moz-backface-visibility:hidden;
	-moz-transform:translateX(0);
}
.flip.out {
	-webkit-transform: rotateY(-90deg) scale(.9);
	-webkit-animation-name: flipouttoleft;
	-webkit-animation-duration: 175ms;
	-moz-transform: rotateY(-90deg) scale(.9);
	-moz-animation-name: flipouttoleft;
	-moz-animation-duration: 175ms;
}
.flip.in {
	-webkit-animation-name: flipintoright;
	-webkit-animation-duration: 225ms;
	-moz-animation-name: flipintoright;
	-moz-animation-duration: 225ms;
}
.flip.out.reverse {
	-webkit-transform: rotateY(90deg) scale(.9);
	-webkit-animation-name: flipouttoright;
	-moz-transform: rotateY(90deg) scale(.9);
	-moz-animation-name: flipouttoright;
}
.flip.in.reverse {
	-webkit-animation-name: flipintoleft;
	-moz-animation-name: flipintoleft;
}
@-webkit-keyframes flipouttoleft {
    from { -webkit-transform: rotateY(0); }
    to { -webkit-transform: rotateY(-90deg) scale(.9); }
}
@-moz-keyframes flipouttoleft {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(-90deg) scale(.9); }
}
@-webkit-keyframes flipouttoright {
    from { -webkit-transform: rotateY(0) ; }
    to { -webkit-transform: rotateY(90deg) scale(.9); }
}
@-moz-keyframes flipouttoright {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(90deg) scale(.9); }
}
@-webkit-keyframes flipintoleft {
    from { -webkit-transform: rotateY(-90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoleft {
    from { -moz-transform: rotateY(-90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@-webkit-keyframes flipintoright {
    from { -webkit-transform: rotateY(90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoright {
    from { -moz-transform: rotateY(90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
/* The properties in this rule are only necessary for the 'flip' transition.
 * We need specify the perspective to create a projection matrix. This will add
 * some depth as the element flips. The depth number represents the distance of
 * the viewer from the z-plane. According to the CSS3 spec, 1000 is a moderate
 * value.
 */
.viewport-turn {
	-webkit-perspective: 1000;
	-moz-perspective: 1000;
	position: absolute;
}
.turn {
	-webkit-backface-visibility:hidden;
	-webkit-transform:translateX(0); /* Needed to work around an iOS 3.1 bug that causes listview thumbs to disappear when -webkit-visibility:hidden is used. */
	-webkit-transform-origin: 0;
	
	-moz-backface-visibility:hidden;
	-moz-transform:translateX(0); /* Needed to work around an iOS 3.1 bug that causes listview thumbs to disappear when -webkit-visibility:hidden is used. */
	-moz-transform-origin: 0;
}
.turn.out {
	-webkit-transform: rotateY(-90deg) scale(.9);
	-webkit-animation-name: flipouttoleft;
	-moz-transform: rotateY(-90deg) scale(.9);
	-moz-animation-name: flipouttoleft;
	-webkit-animation-duration: 125ms;
	-moz-animation-duration: 125ms;
}
.turn.in {
	-webkit-animation-name: flipintoright;
	-moz-animation-name: flipintoright;
	-webkit-animation-duration: 250ms;
	-moz-animation-duration: 250ms;
	
}
.turn.out.reverse {
	-webkit-transform: rotateY(90deg) scale(.9);
	-webkit-animation-name: flipouttoright;
	-moz-transform: rotateY(90deg) scale(.9);
	-moz-animation-name: flipouttoright;
}
.turn.in.reverse {
	-webkit-animation-name: flipintoleft;
	-moz-animation-name: flipintoleft;
}
@-webkit-keyframes flipouttoleft {
    from { -webkit-transform: rotateY(0); }
    to { -webkit-transform: rotateY(-90deg) scale(.9); }
}
@-moz-keyframes flipouttoleft {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(-90deg) scale(.9); }
}
@-webkit-keyframes flipouttoright {
    from { -webkit-transform: rotateY(0) ; }
    to { -webkit-transform: rotateY(90deg) scale(.9); }
}
@-moz-keyframes flipouttoright {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(90deg) scale(.9); }
}
@-webkit-keyframes flipintoleft {
    from { -webkit-transform: rotateY(-90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoleft {
    from { -moz-transform: rotateY(-90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@-webkit-keyframes flipintoright {
    from { -webkit-transform: rotateY(90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoright {
    from { -moz-transform: rotateY(90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
/* flow transition */
.flow {
	-webkit-transform-origin: 50% 30%;
	-moz-transform-origin: 50% 30%;	
	-webkit-box-shadow: 0 0 20px rgba(0,0,0,.4);
	-moz-box-shadow: 0 0 20px rgba(0,0,0,.4);
}
.ui-dialog.flow {
	-webkit-transform-origin: none;
	-moz-transform-origin: none;	
	-webkit-box-shadow: none;
	-moz-box-shadow: none;
}
.flow.out {
	-webkit-transform: translateX(-100%) scale(.7);
	-webkit-animation-name: flowouttoleft;
	-webkit-animation-timing-function: ease;
	-webkit-animation-duration: 350ms;
	-moz-transform: translateX(-100%) scale(.7);
	-moz-animation-name: flowouttoleft;
	-moz-animation-timing-function: ease;
	-moz-animation-duration: 350ms;
}
.flow.in {
	-webkit-transform: translateX(0) scale(1);
	-webkit-animation-name: flowinfromright;
	-webkit-animation-timing-function: ease;
	-webkit-animation-duration: 350ms;
	-moz-transform: translateX(0) scale(1);
	-moz-animation-name: flowinfromright;
	-moz-animation-timing-function: ease;
	-moz-animation-duration: 350ms;
}
.flow.out.reverse {
	-webkit-transform: translateX(100%);
	-webkit-animation-name: flowouttoright;
	-moz-transform: translateX(100%);
	-moz-animation-name: flowouttoright;
}
.flow.in.reverse {
	-webkit-animation-name: flowinfromleft;
	-moz-animation-name: flowinfromleft;
}
@-webkit-keyframes flowouttoleft {
    0% { -webkit-transform: translateX(0) scale(1); }
	60%, 70% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(-100%) scale(.7); }
}
@-moz-keyframes flowouttoleft {
    0% { -moz-transform: translateX(0) scale(1); }
	60%, 70% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform:  translateX(-100%) scale(.7); }
}
@-webkit-keyframes flowouttoright {
    0% { -webkit-transform: translateX(0) scale(1); }
	60%, 70% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform:  translateX(100%) scale(.7); }
}
@-moz-keyframes flowouttoright {
    0% { -moz-transform: translateX(0) scale(1); }
	60%, 70% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform:  translateX(100%) scale(.7); }
}
@-webkit-keyframes flowinfromleft {
    0% { -webkit-transform: translateX(-100%) scale(.7); }
	30%, 40% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(0) scale(1); }
}
@-moz-keyframes flowinfromleft {
    0% { -moz-transform: translateX(-100%) scale(.7); }
	30%, 40% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform: translateX(0) scale(1); }
}
@-webkit-keyframes flowinfromright {
    0% { -webkit-transform: translateX(100%) scale(.7); }
	30%, 40% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(0) scale(1); }
}
@-moz-keyframes flowinfromright {
    0% { -moz-transform: translateX(100%) scale(.7); }
	30%, 40% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform: translateX(0) scale(1); }
}
/* content configurations. */
.ui-grid-a, .ui-grid-b, .ui-grid-c, .ui-grid-d { overflow: hidden; }
.ui-block-a, .ui-block-b, .ui-block-c, .ui-block-d, .ui-block-e { margin: 0; padding: 0; border: 0; float: left; min-height: 1px; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
/* grid solo: 100 - single item fallback */
.ui-grid-solo .ui-block-a { display: block; float: none; }
/* Lower percentages for older browsers (i.e. IE7) to prevent wrapping. -.5px to fix BB5 wrap issue. */
/* grid a: 50/50 */
.ui-grid-a .ui-block-a, .ui-grid-a .ui-block-b { width: 49.95%; }
.ui-grid-a > :nth-child(n) { width: 50%; margin-right: -.5px; }
.ui-grid-a .ui-block-a { clear: left; }
/* grid b: 33/33/33 */
.ui-grid-b .ui-block-a, .ui-grid-b .ui-block-b, .ui-grid-b .ui-block-c { width: 33.25%; }
.ui-grid-b > :nth-child(n) { width: 33.333%; margin-right: -.5px; }
.ui-grid-b .ui-block-a { clear: left; }
/* grid c: 25/25/25/25 */
.ui-grid-c .ui-block-a, .ui-grid-c .ui-block-b, .ui-grid-c .ui-block-c, .ui-grid-c .ui-block-d { width: 24.925%; }
.ui-grid-c > :nth-child(n) { width: 25%; margin-right: -.5px; }
.ui-grid-c .ui-block-a { clear: left; }
/* grid d: 20/20/20/20/20 */
.ui-grid-d .ui-block-a, .ui-grid-d .ui-block-b, .ui-grid-d .ui-block-c, .ui-grid-d .ui-block-d, .ui-grid-d .ui-block-e { width: 19.925%; }
.ui-grid-d > :nth-child(n) { width: 20%; }
.ui-grid-d .ui-block-a { clear: left; }
/* fixed page header & footer configuration */
.ui-header-fixed,
.ui-footer-fixed {
	left: 0;
	right: 0;
	width: 100%;
	position: fixed;
	z-index: 1000;
}
.ui-header-fixed {
	top: 0;
}
.ui-footer-fixed {
	bottom: 0;
}
.ui-header-fullscreen,
.ui-footer-fullscreen {
	filter: Alpha(Opacity=90);
	opacity: .9;
}
.ui-page-header-fixed {
	padding-top: 2.6875em;
}
.ui-page-footer-fixed {
	padding-bottom: 2.6875em;
}
.ui-page-header-fullscreen .ui-content,
.ui-page-footer-fullscreen .ui-content {
	padding: 0;
}
.ui-fixed-hidden {
	position: absolute;
}
.ui-page-header-fullscreen .ui-fixed-hidden,
.ui-page-footer-fullscreen .ui-fixed-hidden {
	left: -9999px;
}
.ui-header-fixed .ui-btn,
.ui-footer-fixed .ui-btn { 
	z-index: 10;
}
.ui-navbar { max-width: 100%; }
.ui-navbar.ui-mini { margin: 0; }
.ui-navbar ul:before, .ui-navbar ul:after { content: " "; display: table; }
.ui-navbar ul:after { clear: both; }
.ui-navbar ul { list-style:none; margin: 0; padding: 0; position: relative; display: block; border: 0; max-width: 100%; overflow: visible; zoom: 1; }
.ui-navbar li .ui-btn { display: block; text-align: center; margin: -1px -1px -1px 0; border-right-width: 0; }
.ui-navbar li .ui-btn-icon-right .ui-icon { right: 6px; }
/* add border if not in header/footer (full width) */
.ui-navbar li:last-child .ui-btn,
.ui-navbar .ui-grid-duo .ui-block-b .ui-btn { margin-right: 0; border-right-width: 1px; }
.ui-header .ui-navbar li:last-child .ui-btn,
.ui-footer .ui-navbar li:last-child .ui-btn,
.ui-header .ui-navbar .ui-grid-duo .ui-block-b .ui-btn,
.ui-footer .ui-navbar .ui-grid-duo .ui-block-b .ui-btn { margin-right: -1px; border-right-width: 0; }
.ui-navbar .ui-grid-duo li.ui-block-a:last-child .ui-btn { margin-right: -1px; border-right-width: 1px; }
.ui-header .ui-navbar li .ui-btn,
.ui-footer .ui-navbar li .ui-btn { border-top-width: 0; border-bottom-width: 0; }
/* fixing gaps caused by subpixel problem */
.ui-header .ui-navbar .ui-grid-b li.ui-block-c .ui-btn,
.ui-footer .ui-navbar .ui-grid-b li.ui-block-c .ui-btn { margin-right: -5px; }
.ui-header .ui-navbar .ui-grid-c li.ui-block-d .ui-btn,
.ui-footer .ui-navbar .ui-grid-c li.ui-block-d .ui-btn,
.ui-header .ui-navbar .ui-grid-d li.ui-block-e .ui-btn,
.ui-footer .ui-navbar .ui-grid-d li.ui-block-e .ui-btn { margin-right: -4px; }
.ui-header .ui-navbar .ui-grid-b li.ui-block-c .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-b li.ui-block-c .ui-btn-icon-right .ui-icon,
.ui-header .ui-navbar .ui-grid-c li.ui-block-d .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-c li.ui-block-d .ui-btn-icon-right .ui-icon,
.ui-header .ui-navbar .ui-grid-d li.ui-block-e .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-d li.ui-block-e .ui-btn-icon-right .ui-icon { right: 8px; }
.ui-navbar li .ui-btn .ui-btn-inner { padding-top: .7em; padding-bottom: .6em }
.ui-navbar li .ui-btn-icon-top .ui-btn-inner { padding-top: 25px; }
.ui-navbar li .ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 30px; }
.ui-btn { display: block; text-align: center; cursor:pointer; position: relative; margin: .5em 0; padding: 0; }
.ui-mini { margin-top: .25em; margin-bottom: .25em; }
.ui-btn-left, .ui-btn-right, .ui-input-clear, .ui-btn-inline,
.ui-grid-a .ui-btn, .ui-grid-b .ui-btn, .ui-grid-c .ui-btn, .ui-grid-d .ui-btn, .ui-grid-e .ui-btn, .ui-grid-solo .ui-btn { margin-right: 5px; margin-left: 5px; }
.ui-btn-inner { font-size: 16px; padding: .6em 20px; min-width: .75em; display: block; position: relative; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; zoom: 1; }
.ui-btn input, .ui-btn button { z-index: 2; }
.ui-btn-left, .ui-btn-right, .ui-btn-inline { display: inline-block; vertical-align: middle; }
.ui-mobile .ui-btn-left, .ui-mobile .ui-btn-right { margin: 0; } /* .ui-mobile to increase specificity level */
.ui-btn-block { display: block; }
.ui-header > .ui-btn,
.ui-footer > .ui-btn { display: inline-block; margin: 0; }
.ui-header .ui-btn-block,
.ui-footer .ui-btn-block { display: block; }
.ui-header .ui-btn-inner,
.ui-footer .ui-btn-inner,
.ui-mini .ui-btn-inner { font-size: 12.5px; padding: .55em 11px .5em; }
.ui-fullsize .ui-btn-inner,
.ui-fullsize .ui-btn-inner { font-size: 16px; padding: .6em 20px; }
.ui-btn-icon-notext { width: 24px; height: 24px; }
.ui-btn-icon-notext .ui-btn-inner { padding: 0; height: 100%; }
.ui-btn-icon-notext .ui-btn-inner .ui-icon { margin: 2px 1px 2px 3px; float: left; }
.ui-btn-text { position: relative; z-index: 1; width: 100%; -moz-user-select: none; -webkit-user-select: none; -ms-user-select: none; }
.ui-btn-icon-notext .ui-btn-text { position: absolute; left: -9999px; }
.ui-btn-icon-left .ui-btn-inner { padding-left: 40px; }
.ui-btn-icon-right .ui-btn-inner { padding-right: 40px; }
.ui-btn-icon-top .ui-btn-inner { padding-top: 40px; }
.ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 40px; }
.ui-header .ui-btn-icon-left .ui-btn-inner,
.ui-footer .ui-btn-icon-left .ui-btn-inner,
.ui-mini.ui-btn-icon-left .ui-btn-inner,
.ui-mini .ui-btn-icon-left .ui-btn-inner { padding-left: 30px; }
.ui-header .ui-btn-icon-right .ui-btn-inner,
.ui-footer .ui-btn-icon-right .ui-btn-inner,
.ui-mini.ui-btn-icon-right .ui-btn-inner,
.ui-mini .ui-btn-icon-right .ui-btn-inner { padding-right: 30px; }
.ui-header .ui-btn-icon-top .ui-btn-inner,
.ui-footer .ui-btn-icon-top .ui-btn-inner { padding: 30px 3px .5em 3px; }
.ui-mini.ui-btn-icon-top .ui-btn-inner,
.ui-mini .ui-btn-icon-top .ui-btn-inner { padding-top: 30px; }
.ui-header .ui-btn-icon-bottom .ui-btn-inner,
.ui-footer .ui-btn-icon-bottom .ui-btn-inner { padding: .55em 3px 30px 3px; }
.ui-mini.ui-btn-icon-bottom .ui-btn-inner,
.ui-mini .ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 30px; }
/*btn icon positioning*/
.ui-btn-icon-notext .ui-icon { display: block; z-index: 0;}
.ui-btn-icon-left > .ui-btn-inner > .ui-icon, .ui-btn-icon-right > .ui-btn-inner > .ui-icon { position: absolute; top: 50%; margin-top: -9px; }
.ui-btn-icon-top .ui-btn-inner .ui-icon, .ui-btn-icon-bottom .ui-btn-inner .ui-icon { position: absolute; left: 50%; margin-left: -9px; }
.ui-btn-icon-left .ui-icon { left: 10px; }
.ui-btn-icon-right .ui-icon { right: 10px; }
.ui-btn-icon-top .ui-icon { top: 10px; }
.ui-btn-icon-bottom .ui-icon { top: auto; bottom: 10px; }
.ui-header .ui-btn-icon-left .ui-icon,
.ui-footer .ui-btn-icon-left .ui-icon,
.ui-mini.ui-btn-icon-left .ui-icon,
.ui-mini .ui-btn-icon-left .ui-icon { left: 5px; }
.ui-header .ui-btn-icon-right .ui-icon,
.ui-footer .ui-btn-icon-right .ui-icon,
.ui-mini.ui-btn-icon-right .ui-icon,
.ui-mini .ui-btn-icon-right .ui-icon { right: 5px; }
.ui-header .ui-btn-icon-top .ui-icon,
.ui-footer .ui-btn-icon-top .ui-icon,
.ui-mini.ui-btn-icon-top .ui-icon,
.ui-mini .ui-btn-icon-top .ui-icon { top: 5px; }
.ui-header .ui-btn-icon-bottom .ui-icon,
.ui-footer .ui-btn-icon-bottom .ui-icon,
.ui-mini.ui-btn-icon-bottom .ui-icon,
.ui-mini .ui-btn-icon-bottom .ui-icon { bottom: 5px; }
/*hiding native button,inputs */
.ui-btn-hidden { position: absolute; top: 0; left: 0; width: 100%; height: 100%; -webkit-appearance: none; cursor: pointer; background: #fff; background: rgba(255,255,255,0); filter: Alpha(Opacity=0); opacity: .1; font-size: 1px; border: none; text-indent: -9999px; }
/* Fixes IE/WP filter alpha opacity bugs */
.ui-disabled .ui-btn-hidden { display: none; }
.ui-disabled { z-index: 1; }
.ui-field-contain .ui-btn.ui-submit { margin: 0; }
label.ui-submit { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .3em; display: block; }
@media all and (min-width: 450px){
	.ui-field-contain label.ui-submit { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-btn.ui-submit { width: 78%; display: inline-block; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
	.ui-hide-label .ui-btn.ui-submit { width: auto; display: block; }
}
.ui-collapsible-inset { margin: .5em 0; }
.ui-collapsible-heading { font-size: 16px; display: block; margin: 0 -15px; padding: 0; position: relative; }
.ui-collapsible-inset .ui-collapsible-heading { margin: 0; }
.ui-collapsible-heading .ui-btn { text-align: left; margin: 0; border-left-width: 0; border-right-width: 0; }
.ui-collapsible-inset .ui-collapsible-heading .ui-btn { border-right-width: 1px; border-left-width: 1px; }
.ui-collapsible-collapsed + .ui-collapsible:not(.ui-collapsible-inset) .ui-collapsible-heading .ui-btn { border-top-width: 0; }
.ui-collapsible-set .ui-collapsible:not(.ui-collapsible-inset) .ui-collapsible-heading .ui-btn { border-top-width: 1px; }
.ui-collapsible-heading .ui-btn-inner,
.ui-collapsible-heading .ui-btn-icon-left .ui-btn-inner { padding-left: 40px; }
.ui-collapsible-heading .ui-btn-icon-right .ui-btn-inner { padding-left: 12px; padding-right: 40px; }
.ui-collapsible-heading .ui-btn-icon-top .ui-btn-inner,
.ui-collapsible-heading .ui-btn-icon-bottom .ui-btn-inner { padding-right: 40px; text-align: center; }
.ui-collapsible-heading .ui-btn span.ui-btn { position: absolute; left: 6px; top: 50%; margin: -12px 0 0 0; width: 20px; height: 20px; padding: 1px 0px 1px 2px; text-indent: -9999px; }
.ui-collapsible-heading .ui-btn span.ui-btn .ui-btn-inner { padding: 10px 0; }
.ui-collapsible-heading .ui-btn span.ui-btn .ui-icon { left: 0; margin-top: -10px; }
.ui-collapsible-heading-status { position: absolute; top: -9999px; left:0px; }
.ui-collapsible-content {
	display: block;
	margin: 0 -15px;	
	padding: 10px 15px;
	border-left-width: 0;
	border-right-width: 0;
	border-top: none;      /* Overrides ui-body-* */
	background-image: none; /* Overrides ui-body-* */
}
.ui-collapsible-inset .ui-collapsible-content { margin: 0; border-right-width: 1px; border-left-width: 1px; }
.ui-collapsible-content-collapsed { display: none; }
.ui-collapsible-set { margin: .5em 0; }
.ui-collapsible-set .ui-collapsible { margin: -1px 0 0; }
.ui-collapsible-set .ui-collapsible:first-child { margin-top: 0; }
.ui-controlgroup, fieldset.ui-controlgroup { padding: 0; margin: .5em 0; zoom: 1; }
.ui-controlgroup.ui-mini, fieldset.ui-controlgroup.ui-mini { margin: .25em 0; }
.ui-field-contain .ui-controlgroup, .ui-field-contain fieldset.ui-controlgroup { margin: 0; }
.ui-bar .ui-controlgroup { margin: 0 5px; }
.ui-controlgroup-label { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .4em; }
.ui-controlgroup li { list-style: none; }
.ui-controlgroup-vertical .ui-btn,
.ui-controlgroup-vertical .ui-checkbox, .ui-controlgroup-vertical .ui-radio { margin: 0; border-bottom-width: 0; }
.ui-controlgroup-vertical .ui-controlgroup-last { border-bottom-width: 1px; }
.ui-controlgroup-controls label.ui-select { position: absolute; left: -9999px; }
.ui-controlgroup .ui-btn-icon-notext { width: auto; height: auto; top: auto; }
.ui-controlgroup .ui-btn-icon-notext .ui-btn-inner { height: 20px; padding: .6em 20px .6em 20px }
.ui-controlgroup-horizontal .ui-btn-icon-notext .ui-btn-inner { width: 18px; }
.ui-controlgroup.ui-mini .ui-btn-icon-notext .ui-btn-inner,
.ui-header .ui-controlgroup .ui-btn-icon-notext .ui-btn-inner,
.ui-footer .ui-controlgroup .ui-btn-icon-notext .ui-btn-inner { height: 16px; padding: .55em 11px .5em 11px; }
.ui-controlgroup .ui-btn-icon-notext .ui-btn-inner .ui-icon { position: absolute; top: 50%; right: 50%; margin: -9px -9px 0 0; }
.ui-controlgroup-horizontal .ui-controlgroup-controls:before,
.ui-controlgroup-horizontal .ui-controlgroup-controls:after { content: ""; display: table; }
.ui-controlgroup-horizontal .ui-controlgroup-controls:after { clear: both; }
.ui-controlgroup-horizontal .ui-controlgroup-controls { display: inline-block; vertical-align: middle; zoom: 1; }
.ui-controlgroup-horizontal .ui-btn-inner { text-align: center; }
.ui-controlgroup-horizontal.ui-mini .ui-btn-inner { height: 16px; line-height: 16px; }
.ui-controlgroup-horizontal .ui-btn, .ui-controlgroup-horizontal .ui-select,
.ui-controlgroup-horizontal .ui-checkbox, .ui-controlgroup-horizontal .ui-radio { float: left; clear: none; margin: 0 -1px 0 0; }
.ui-controlgroup-horizontal .ui-select .ui-btn,
.ui-controlgroup-horizontal .ui-checkbox .ui-btn, .ui-controlgroup-horizontal .ui-radio .ui-btn { float: none; margin: 0; }
.ui-controlgroup-horizontal .ui-controlgroup-last, .ui-controlgroup-horizontal .ui-select:last-child,
.ui-controlgroup-horizontal .ui-checkbox:last-child, .ui-controlgroup-horizontal .ui-radio:last-child { margin-right: 0; }
.ui-controlgroup .ui-checkbox label, .ui-controlgroup .ui-radio label { font-size: 16px; }
@media all and (min-width: 450px){
	.ui-field-contain .ui-controlgroup-label { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-controlgroup-controls { width: 78%; display: inline-block; }
	.ui-field-contain .ui-controlgroup .ui-select { width: 100%; display: block; } 
	.ui-field-contain .ui-controlgroup-horizontal .ui-select { width: auto; }
	.ui-hide-label .ui-controlgroup-controls { width: 100%; }
}	
.ui-dialog {
	 background: none !important; /* this is to ensure that dialog theming does not apply (by default at least) on the page div */
}
.ui-dialog-contain {
	width: 92.5%;
	max-width: 500px;
	margin: 10% auto 15px auto;
	padding: 0;
	position: relative;
	top: -15px;
}
.ui-dialog-contain > .ui-header, 
.ui-dialog-contain > .ui-content, 
.ui-dialog-contain > .ui-footer { 
	display: block;
	position: relative; 
	width: auto;
	margin: 0;
}
.ui-dialog-contain > .ui-header {
	border: none;
	overflow: hidden;
	z-index: 10; 
	padding: 0;
}
.ui-dialog-contain > .ui-content { 
	padding: 15px; 
}
.ui-dialog-contain > .ui-footer {
	z-index: 10; 
	padding: 0 15px; 
}
.ui-popup-open .ui-header-fixed,
.ui-popup-open .ui-footer-fixed {
	position: absolute !important; 	/* See line #553 of popup.js */
}
.ui-popup-screen {
	background-image: url(data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==); /* Necessary to set some form of background to ensure element is clickable in IE6/7. While legacy IE won't understand the data-URI'd image, it ensures no additional requests occur in all other browsers with little overhead. */
	top: 0px;
	left: 0px;
	right: 0px;
	bottom: 1px;
	position: absolute;
	filter: Alpha(Opacity=0);
	opacity: 0;
	z-index: 1099;
}
.ui-popup-screen.in {
	opacity: 0.5;
	filter: Alpha(Opacity=50);
}
.ui-popup-screen.out {
	opacity: 0;
	filter: Alpha(Opacity=0);
}
.ui-popup-container {
	z-index: 1100;
	display: inline-block;
	position: absolute;
	padding: 0;
	outline: 0;
}
.ui-popup {
	position: relative;
}
.ui-popup.ui-content,
.ui-popup .ui-content {
	overflow: visible;
}
.ui-popup > p,
.ui-popup > h1,
.ui-popup > h2,
.ui-popup > h3,
.ui-popup > h4,
.ui-popup > h5,
.ui-popup > h6 {
	margin: .5em 7px;
}
.ui-popup > span {
	display: block;
	margin: .5em 7px;
}
.ui-popup .ui-title {
	font-size: 16px;
	font-weight: bold;
	margin-top: .5em;
	margin-bottom: .5em;
}
.ui-popup-container .ui-content > p,
.ui-popup-container .ui-content > h1,
.ui-popup-container .ui-content > h2,
.ui-popup-container .ui-content > h3,
.ui-popup-container .ui-content > h4,
.ui-popup-container .ui-content > h5,
.ui-popup-container .ui-content > h6 {
	margin: .5em 0;
}
.ui-popup-container .ui-content > span {
	margin: 0;
}
.ui-popup-container .ui-content > p:first-child,
.ui-popup-container .ui-content > h1:first-child,
.ui-popup-container .ui-content > h2:first-child,
.ui-popup-container .ui-content > h3:first-child,
.ui-popup-container .ui-content > h4:first-child,
.ui-popup-container .ui-content > h5:first-child,
.ui-popup-container .ui-content > h6:first-child {
	margin-top: 0;
}
.ui-popup-container .ui-content > p:last-child,
.ui-popup-container .ui-content > h1:last-child,
.ui-popup-container .ui-content > h2:last-child,
.ui-popup-container .ui-content > h3:last-child,
.ui-popup-container .ui-content > h4:last-child,
.ui-popup-container .ui-content > h5:last-child,
.ui-popup-container .ui-content > h6:last-child {
	margin-bottom: 0;
}
.ui-popup > img {
	width: auto;
	height: auto;
	max-width: 100%;
	max-height: 100%;
	vertical-align: middle;
}
.ui-popup iframe {
	vertical-align: middle;
}
@media all and (min-width: 450px){
	.ui-popup .ui-field-contain label.ui-submit,
	.ui-popup .ui-field-contain .ui-controlgroup-label,
	.ui-popup .ui-field-contain label.ui-select,
	.ui-popup .ui-field-contain label.ui-input-text {
		font-size: 16px; line-height: 1.4; display: block; font-weight: normal; margin: 0 0 .3em;
	}
	.ui-popup .ui-field-contain .ui-btn.ui-submit,
	.ui-popup .ui-field-contain .ui-controlgroup-controls,
	.ui-popup .ui-field-contain .ui-select,
	.ui-popup .ui-field-contain input.ui-input-text,
	.ui-popup .ui-field-contain textarea.ui-input-text,
	.ui-popup .ui-field-contain .ui-input-search {
		width: 100%; display: block;
	}
}
.ui-popup > .ui-btn-left,
.ui-popup > .ui-btn-right {
	position: absolute; 
	top: -9px;
	margin: 0;
	z-index: 1101;
}
.ui-popup > .ui-btn-left { left: -9px; }
.ui-popup > .ui-btn-right { right: -9px; }
.ui-popup.ui-corner-all > .ui-header,
.ui-popup.ui-corner-all ~ .ui-content,
.ui-popup.ui-corner-all > .ui-content:first-child {
	-webkit-border-top-left-radius:  inherit;
	border-top-left-radius:          inherit;
	-webkit-border-top-right-radius: inherit;
	border-top-right-radius:         inherit;
}
.ui-popup.ui-corner-all > .ui-content,
.ui-popup.ui-corner-all > .ui-footer,
.ui-popup.ui-corner-all > .ui-header:nth-child(n):last-child {
	-webkit-border-bottom-left-radius:  inherit;
	border-bottom-left-radius:          inherit;
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius:         inherit;
}
.ui-popup.ui-corner-all > .ui-content:nth-child(2),
.ui-popup.ui-corner-all > .ui-header:nth-child(2) {
	-webkit-border-top-left-radius:  0;
	border-top-left-radius:          0;
	-webkit-border-top-right-radius: 0;
	border-top-right-radius:         0;
}
.ui-popup.ui-corner-all > .ui-content:nth-last-child(1n+2),
.ui-popup.ui-corner-all > .ui-footer:nth-last-child(1n+2) {
	-webkit-border-bottom-left-radius:  0;
	border-bottom-left-radius:          0;
	-webkit-border-bottom-right-radius: 0;
	border-bottom-right-radius:         0;
}
.ui-popup.ui-corner-all > .ui-header:only-child,
.ui-popup.ui-corner-all > .ui-footer:only-child {
	-webkit-border-radius: inherit;
	border-radius:         inherit;
}
.ui-checkbox, .ui-radio { position: relative; clear: both; margin: 0; z-index: 1; }
.ui-checkbox .ui-btn, .ui-radio .ui-btn { margin-top: .5em; margin-bottom: .5em; text-align: left; z-index: 2; }
.ui-checkbox .ui-btn.ui-mini, .ui-radio .ui-btn.ui-mini { margin: .25em 0; }
.ui-controlgroup .ui-checkbox .ui-btn, .ui-controlgroup .ui-radio .ui-btn { margin: 0; }
.ui-checkbox .ui-btn-inner, .ui-radio .ui-btn-inner { white-space: normal; }
.ui-checkbox .ui-btn-icon-left .ui-btn-inner,.ui-radio .ui-btn-icon-left .ui-btn-inner { padding-left: 45px; }
.ui-checkbox .ui-mini.ui-btn-icon-left .ui-btn-inner,.ui-radio .ui-mini.ui-btn-icon-left .ui-btn-inner { padding-left: 36px; }
.ui-checkbox .ui-btn-icon-right .ui-btn-inner, .ui-radio .ui-btn-icon-right .ui-btn-inner { padding-right: 45px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-btn-inner, .ui-radio .ui-mini.ui-btn-icon-right .ui-btn-inner { padding-right: 36px; }
.ui-checkbox .ui-btn-icon-top .ui-btn-inner,.ui-radio .ui-btn-icon-top .ui-btn-inner { padding-right: 0; padding-left: 0; text-align: center; }
.ui-checkbox .ui-btn-icon-bottom .ui-btn-inner, .ui-radio .ui-btn-icon-bottom .ui-btn-inner { padding-right: 0; padding-left: 0; text-align: center; }
.ui-checkbox .ui-icon, .ui-radio .ui-icon { top: 1.1em; }
.ui-checkbox .ui-btn-icon-left .ui-icon, .ui-radio .ui-btn-icon-left .ui-icon { left: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-left .ui-icon, .ui-radio .ui-mini.ui-btn-icon-left .ui-icon { left: 9px; }
.ui-checkbox .ui-btn-icon-right .ui-icon, .ui-radio .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-icon, .ui-radio .ui-mini.ui-btn-icon-right .ui-icon { right: 9px; }
.ui-checkbox .ui-btn-icon-top .ui-icon, .ui-radio .ui-btn-icon-top .ui-icon { top: 10px; }
.ui-checkbox .ui-btn-icon-bottom .ui-icon, .ui-radio .ui-btn-icon-bottom .ui-icon { top: auto; bottom: 10px; }
.ui-checkbox .ui-btn-icon-right .ui-icon, .ui-radio .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-icon, .ui-radio .ui-mini.ui-btn-icon-right .ui-icon { right: 9px; }
/* input, label positioning */
.ui-checkbox input,.ui-radio input { position:absolute; left:20px; top:50%; width: 10px; height: 10px; margin:-5px 0 0 0; outline: 0 !important; z-index: 1; }
.ui-field-contain, fieldset.ui-field-contain { padding: .8em 0; margin: 0; border-width: 0 0 1px 0; overflow: visible; }
.ui-field-contain:last-child { border-bottom-width: 0; }
.ui-field-contain { max-width: 100%; } /* This prevents horizontal scrollbar in IE7 */
@media all and (min-width: 450px){
	.ui-field-contain, .ui-mobile fieldset.ui-field-contain { border-width: 0; padding: 0; margin: 1em 0; }
}
.ui-select { display: block; position: relative; }
.ui-select select { position: absolute; left: -9999px; top: -9999px; }
.ui-select .ui-btn { overflow: hidden; opacity: 1; }
.ui-field-contain .ui-select .ui-btn { margin: 0; }
/* Fixes #2588: When Windows Phone 7.5 (Mango) tries to calculate a numeric opacity for a select (including "inherit") without explicitly specifying an opacity on the parent to give it context, a bug appears where clicking elsewhere on the page after opening the select will open the select again. */
.ui-select .ui-btn select { cursor: pointer; -webkit-appearance: none; left: 0; top:0; width: 100%; min-height: 1.5em; min-height: 100%; height: 3em; max-height: 100%; filter: Alpha(Opacity=0); opacity: 0; z-index: 2; }
.ui-select .ui-disabled { opacity: .3; }
/* Display none because of issues with IE/WP's filter alpha opacity */
.ui-select .ui-disabled select { display: none; }
@-moz-document url-prefix() { .ui-select .ui-btn select { opacity: 0.0001; }}
.ui-select .ui-btn.ui-select-nativeonly { border-radius: 0; border: 0; }
.ui-select .ui-btn.ui-select-nativeonly select { opacity: 1; text-indent: 0; display: block; }
.ui-select .ui-disabled.ui-select-nativeonly .ui-btn-inner { opacity: 0; }
.ui-select .ui-btn-icon-right .ui-btn-inner, .ui-select .ui-li-has-count .ui-btn-inner { padding-right: 45px; }
.ui-select .ui-mini.ui-btn-icon-right .ui-btn-inner { padding-right: 32px; }
.ui-select .ui-btn-icon-right.ui-li-has-count .ui-btn-inner { padding-right: 80px; }
.ui-select .ui-mini.ui-btn-icon-right.ui-li-has-count .ui-btn-inner { padding-right: 67px; }
.ui-select .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-select .ui-mini.ui-btn-icon-right .ui-icon { right: 7px; }
.ui-select .ui-btn-icon-right.ui-li-has-count .ui-li-count { right: 45px; }
.ui-select .ui-mini.ui-btn-icon-right.ui-li-has-count .ui-li-count { right: 32px; }
/* labels */
label.ui-select { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .3em; display: block; }
/*listbox*/
.ui-select .ui-btn-text, .ui-selectmenu .ui-btn-text { display: block; min-height: 1em; overflow: hidden !important;
/* This !important is required for iPad Safari specifically. See https://github.com/jquery/jquery-mobile/issues/2647 */ }
.ui-select .ui-btn-text { text-overflow: ellipsis; }
.ui-selectmenu { padding: 6px; min-width: 160px; }
.ui-selectmenu .ui-listview { margin: 0; }
.ui-selectmenu .ui-btn.ui-li-divider { cursor: default; }
.ui-selectmenu-hidden { top: -99999px; left: -9999px; }
.ui-screen-hidden, .ui-selectmenu-list .ui-li .ui-icon { display: none; }
.ui-selectmenu-list .ui-li .ui-icon { display: block; }
.ui-li.ui-selectmenu-placeholder { display: none; }
.ui-selectmenu .ui-header { margin: 0; padding: 0; }
.ui-selectmenu .ui-header .ui-title { margin: 0.6em 46px 0.8em; }
@media all and (min-width: 450px){
	.ui-field-contain label.ui-select { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-select { width: 78%; display: inline-block; }
	.ui-hide-label .ui-select { width: 100%; } 
}
/* when no placeholder is defined in a multiple select, the header height doesn't even extend past the close button.  this shim's content in there */
.ui-selectmenu .ui-header h1:after { content: '.'; visibility: hidden; }
label.ui-input-text { font-size: 16px; line-height: 1.4; display: block; font-weight: normal; margin: 0 0 .3em; }
input.ui-input-text, textarea.ui-input-text { background-image: none; padding: .4em; margin: .5em 0; line-height: 1.4; font-size: 16px; display: block; width: 100%; outline: 0; }
input.ui-input-text.ui-mini, textarea.ui-input-text.ui-mini { margin: .25em 0; }
.ui-field-contain input.ui-input-text, .ui-field-contain textarea.ui-input-text { margin: 0; }
input.ui-input-text, textarea.ui-input-text, .ui-input-search { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
input.ui-input-text { -webkit-appearance: none; }
textarea.ui-input-text { height: 50px; -webkit-transition: height 200ms linear; -moz-transition: height 200ms linear; -o-transition: height 200ms linear; transition: height 200ms linear; }
.ui-input-search { padding: 0 30px; margin: .5em 0; background-image: none; position: relative; }
.ui-input-search.ui-mini { margin: .25em 0; }
.ui-field-contain .ui-input-search { margin: 0; }
.ui-icon-searchfield:after { position: absolute; left: 7px; top: 50%; margin-top: -9px; content: ""; width: 18px; height: 18px; opacity: .5; }
.ui-input-search input.ui-input-text { border: none; width: 98%; padding: .4em 0; margin: 0; display: block; background: transparent none; outline: 0 !important; }
.ui-input-search .ui-input-clear { position: absolute; right: 0; top: 50%; margin-top: -13px; }
.ui-mini .ui-input-clear { right: -3px; }
.ui-input-search .ui-input-clear-hidden { display: none; }
input.ui-mini, .ui-mini input, textarea.ui-mini { font-size: 14px; }
textarea.ui-mini { height: 45px; }
@media all and (min-width: 450px){
	.ui-field-contain label.ui-input-text  { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0 }
	.ui-field-contain input.ui-input-text, 
	.ui-field-contain textarea.ui-input-text, 
	.ui-field-contain .ui-input-search { width: 78%; display: inline-block; } 
	.ui-hide-label input.ui-input-text, 
	.ui-hide-label textarea.ui-input-text, 
	.ui-hide-label .ui-input-search { width: 100%; }
	.ui-input-search input.ui-input-text { width: 98%; /*echos rule from above*/ }
}
.ui-listview { margin: 0; }
ol.ui-listview, ol.ui-listview .ui-li-divider { counter-reset: listnumbering; }
.ui-content .ui-listview { margin: -15px; }
.ui-collapsible-content > .ui-listview { margin: -10px -15px; }
.ui-content .ui-listview-inset { margin: 1em 0; }
.ui-collapsible-content .ui-listview-inset { margin: .5em 0; }
.ui-listview, .ui-li { list-style:none; padding:0; }
.ui-li, .ui-li.ui-field-contain { display: block; margin:0; position: relative; overflow: visible; text-align: left; border-width: 0; border-top-width: 1px; }
.ui-li.ui-btn { margin: 0; }
.ui-li .ui-btn-text a.ui-link-inherit { text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
.ui-li-static { background-image: none; }
.ui-li-divider { padding: 1em 15px; font-size: 14px; font-weight: bold; }
ol.ui-listview .ui-link-inherit:before, ol.ui-listview .ui-li-static:before, .ui-li-dec { font-size: .8em; display: inline-block; padding-right: .3em; font-weight: normal; counter-increment: listnumbering; content: counter(listnumbering) ". "; }
ol.ui-listview .ui-li-jsnumbering:before { content: "" !important; } /* to avoid chance of duplication */
.ui-listview-inset .ui-li { border-right-width: 1px; border-left-width: 1px; }
.ui-li-last, .ui-li.ui-field-contain.ui-li-last { border-bottom-width: 1px; }
.ui-collapsible [class*="ui-body"] > .ui-listview:not(.ui-listview-inset) .ui-li-last { border-bottom-width: 0; }
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset) .ui-li:first-child { border-top-width: 0; }
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset),
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset) .ui-li-last { -webkit-border-bottom-left-radius: inherit; -webkit-border-bottom-right-radius: inherit; border-bottom-left-radius: inherit; border-bottom-right-radius: inherit; }
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset) .ui-li-last .ui-li-link-alt { -webkit-border-bottom-right-radius: inherit; border-bottom-right-radius: inherit; }
.ui-li>.ui-btn-inner { display: block; position: relative; padding: 0; }
.ui-li .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li { padding: .7em 15px; display: block; }
.ui-li-has-thumb .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-thumb  { min-height: 60px; padding-left: 100px; }
.ui-li-has-icon .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-icon { min-height: 20px; padding-left: 40px; }
.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-count, .ui-li-divider.ui-li-has-count { padding-right: 45px; }
.ui-li-has-arrow .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-arrow { padding-right: 40px; }
.ui-li-has-arrow.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-arrow.ui-li-has-count { padding-right: 75px; }
.ui-li-heading { font-size: 16px; font-weight: bold; display: block; margin: .6em 0; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
.ui-li-desc { font-size: 12px; font-weight: normal; display: block; margin: -.5em 0 .6em; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
.ui-li-thumb, .ui-listview .ui-li-icon { position: absolute; left: 1px; top: 0; max-height: 80px; max-width: 80px; }
.ui-listview .ui-li-icon { max-height: 16px; max-width: 16px; left: 10px; top: .9em; }
.ui-li-thumb, .ui-listview .ui-li-icon, .ui-li-content { float: left; margin-right: 10px; }
.ui-li-aside { float: right; width: 50%; text-align: right; margin: .3em 0; }
@media all and (min-width: 480px){
	 .ui-li-aside { width: 45%; }
}	 
.ui-li-divider { cursor: default; }
.ui-li-has-alt .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-alt { padding-right: 53px; }
.ui-li-has-alt.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-alt.ui-li-has-count { padding-right: 88px; }
.ui-li-has-count .ui-li-count { position: absolute; font-size: 11px; font-weight: bold; padding: .2em .5em; top: 50%; margin-top: -.9em; right: 10px; }
.ui-li-has-count.ui-li-divider .ui-li-count, .ui-li-has-count .ui-link-inherit .ui-li-count { margin-top: -.95em; }
.ui-li-has-arrow.ui-li-has-count .ui-li-count { right: 40px; }
.ui-li-has-alt.ui-li-has-count .ui-li-count { right: 53px; }
.ui-li-link-alt { position: absolute; width: 40px; height: 100%; border-width: 0; border-left-width: 1px; top: 0; right: 0; margin: 0; padding: 0; z-index: 2; }
.ui-li-link-alt .ui-btn { overflow: hidden; position: absolute; right: 8px; top: 50%; margin: -13px 0 0 0; border-bottom-width: 1px; z-index: -1;}
.ui-li-link-alt .ui-btn-inner { padding: 0; height: 100%; position: absolute; width: 100%; top: 0; left: 0;}
.ui-li-link-alt .ui-btn .ui-icon { right: 50%; margin-right: -9px; }
.ui-li-link-alt .ui-btn-icon-notext .ui-btn-inner .ui-icon { position: absolute; top: 50%; margin-top: -9px; }
.ui-listview * .ui-btn-inner > .ui-btn > .ui-btn-inner { border-top: 0px; }
.ui-listview-filter { border-width: 0; overflow: hidden; margin: -15px -15px 15px -15px; }
.ui-collapsible-content .ui-listview-filter { margin: -10px -15px 10px -15px; border-bottom: inherit; }
.ui-listview-filter-inset { margin: -15px -5px; background: transparent; }
.ui-collapsible-content .ui-listview-filter-inset { margin: -5px; border-bottom-width: 0; }
.ui-listview-filter .ui-input-search { margin: 5px; width: auto; display: block; }
.ui-li.ui-screen-hidden{ display:none; }
/* Odd iPad positioning issue. */
@media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
    .ui-li .ui-btn-text { overflow:  visible; }
}
label.ui-slider { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .3em; display: block; }
input.ui-slider-input,
.ui-field-contain input.ui-slider-input { display: inline-block; width: 50px; background-image: none; padding: .4em; margin: .5em 0; line-height: 1.4; font-size: 16px; outline: 0; }
input.ui-slider-input.ui-mini,
.ui-field-contain input.ui-slider-input.ui-mini { width: 45px; margin: .25em 0; font-size: 14px; }
.ui-field-contain input.ui-slider-input { margin: 0; }
input.ui-slider-input, .ui-field-contain input.ui-slider-input { -webkit-box-sizing: content-box; -moz-box-sizing: content-box; -ms-box-sizing: content-box; box-sizing: content-box; }
/* Fixes input fields being to small on Safari/Mac because of the up and down arrows. */
.ui-slider-input::-webkit-outer-spin-button { margin: 0; }
select.ui-slider-switch { display: none; }
div.ui-slider { position: relative; display: inline-block; overflow: visible; height: 15px; padding: 0; margin: 0 2% 0 20px; top: 4px; width: 65%; }
div.ui-slider-mini { height: 12px; margin-left: 10px; top: 2px; }
div.ui-slider-bg { border: none; height: 100%; padding-right: 8px; }
.ui-controlgroup a.ui-slider-handle, a.ui-btn.ui-slider-handle { position: absolute; z-index: 1; top: 50%; width: 28px; height: 28px; margin: -15px 0 0 -15px; outline: 0; }
a.ui-btn.ui-slider-handle .ui-btn-inner { padding: 0; height: 100%; }
div.ui-slider-mini a.ui-slider-handle { height: 14px; width: 14px; margin: -8px 0 0 -7px; }
div.ui-slider-mini a.ui-slider-handle .ui-btn-inner { height: 30px; width: 30px; padding: 0; margin: -9px 0 0 -9px; border-top: none; }
@media all and (min-width: 450px){
	.ui-field-contain label.ui-slider { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain div.ui-slider { width: 43%; }
	.ui-field-contain div.ui-slider-switch { width: 5.5em; }
}	
div.ui-slider-switch { height: 32px; margin-left: 0; width: 5.8em; }
a.ui-slider-handle-snapping { -webkit-transition: left 70ms linear; -moz-transition: left 70ms linear; }
div.ui-slider-switch .ui-slider-handle { margin: 1px 0 0 -15px; }
.ui-slider-inneroffset { margin: 0 16px; position: relative; z-index: 1; }
div.ui-slider-switch.ui-slider-mini { width: 5em; height: 29px; }
div.ui-slider-switch.ui-slider-mini .ui-slider-inneroffset { margin: 0 15px 0 14px; }
div.ui-slider-switch.ui-slider-mini .ui-slider-handle { width: 25px; height: 25px; margin: 1px 0 0 -13px; }
div.ui-slider-switch.ui-slider-mini a.ui-slider-handle .ui-btn-inner { height: 30px; width: 30px; padding: 0; margin: 0; }
span.ui-slider-label { position: absolute; text-align: center; width: 100%; overflow: hidden; font-size: 16px; top: 0; line-height: 2; min-height: 100%; border-width: 0; white-space: nowrap; }
.ui-slider-mini span.ui-slider-label { font-size: 14px; }
span.ui-slider-label-a { z-index: 1; left: 0; text-indent: -1.5em; }
span.ui-slider-label-b { z-index: 0; right: 0; text-indent: 1.5em;}
.ui-slider-inline { width: 120px; display: inline-block; }

/** Custom additions **/
.ui-btn-active .ui-icon {
	background-image: url(images/icons-18-white.png) /*{global-icon-set}*/;
}
.ui-btn-hover-a .ui-icon {
	background-image: url(images/icons-18-white.png) /*{global-icon-set}*/;
}
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
       only screen and (min--moz-device-pixel-ratio: 1.5),
       only screen and (min-resolution: 240dpi) {
  .ui-btn-active .ui-icon {
    background-image: url(images/icons-36-white.png) /*{global-icon-set}*/;
  }
  .ui-btn-hover-a .ui-icon {
    background-image: url(images/icons-36-white.png) /*{global-icon-set}*/;
  }
}

/* 
  I wanted the ability to change buttons in the header.
  This theme flips the start and end points for the gradients
*/
.ui-header > .ui-btn-up-a, .ui-footer > .ui-btn-up-a {
	border: 1px solid 		#005994 /*{a-header-bhover-border}*/;
	background: 			#444 /*{a-header-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-header-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-header-bhover-background-start}*/), to( #0093EA /*{a-header-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-header-bhover-background-start}*/, #0093EA /*{a-header-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-header-bhover-background-start}*/, #0093EA /*{a-header-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-header-bhover-background-start}*/, #0093EA /*{a-header-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-header-bhover-background-start}*/, #0093EA /*{a-header-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-header-bhover-background-start}*/, #0093EA /*{a-header-bhover-background-end}*/);
  box-shadow: 0px 1px 1px rgba(0,0,0,.15) /*{a-header-dropshadow-color}*/;
  -moz-box-shadow: 0px 1px 1px rgba(0,0,0,.15) /*{a-header-dropshadow-color}*/;
  -webkit-box-shadow: 0px 1px 1px rgba(0,0,0,.15) /*{a-header-dropshadow-color}*/;
}
.ui-header.ui-bar-a {
  box-shadow: 0px 1px 2px rgba(0,0,0,0.15) /*{a-bar-dropshadow-color}*/, inset 0 1px 0 rgba(255,255,255,0.1) /*{a-bar-dropshadow-inset-color}*/;
  -moz-box-shadow: 0px 1px 2px rgba(0,0,0,0.15) /*{a-bar-dropshadow-color}*/, inset 0 1px 0 rgba(255,255,255,0.1) /*{a-bar-dropshadow-inset-color}*/;
  -webkit-box-shadow: 0px 1px 2px rgba(0,0,0,0.15) /*{a-bar-dropshadow-color}*/, inset 0 1px 0 rgba(255,255,255,0.1) /*{a-bar-dropshadow-inset-color}*/;
}
.ui-footer.ui-bar-a {
  box-shadow: 0px -2px 2px rgba(0, 0, 0, .2);
  -moz-box-shadow: 0px -2px 2px rgba(0, 0, 0, .2);
  -webkit-box-shadow: 0px -2px 2px rgba(0, 0, 0, .2);
}
/* Sliders need their own look */
span.ui-slider-label-b.ui-btn-down-c {
	border: 1px solid 		#bbb /*{c-bdown-slider-border}*/;
	background: 			#d6d6d6 /*{c-bdown-background-slider-color}*/;
	font-weight: bold;
	color: 					#222 /*{c-bdown-slider-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #d0d0d0 /*{c-bdown-background-slider-start}*/), to( #dfdfdf /*{c-bdown-background-slider-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #d0d0d0 /*{c-bdown-background-slider-start}*/, #dfdfdf /*{c-bdown-background-slider-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #d0d0d0 /*{c-bdown-background-slider-start}*/, #dfdfdf /*{c-bdown-background-slider-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #d0d0d0 /*{c-bdown-background-slider-start}*/, #dfdfdf /*{c-bdown-background-slider-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #d0d0d0 /*{c-bdown-background-slider-start}*/, #dfdfdf /*{c-bdown-background-slider-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #d0d0d0 /*{c-bdown-background-slider-start}*/, #dfdfdf /*{c-bdown-background-slider-end}*/);
}
a.ui-btn.ui-slider-handle.ui-btn-hover-c {
  background-image: none;
  background-color: #fff; /*{c-bhover-slider-background}*/
}
.ui-li-divider.ui-corner-top {
  -moz-border-radius-topleft: 0.6em;
  -webkit-border-top-left-radius: 0.6em;
  border-top-left-radius: 0.6em;
  -moz-border-radius-topright: 0.6em;
  -webkit-border-top-right-radius: 0.6em;
  border-top-right-radius: 0.6em;
}


File: /flash\hotspot\jqm\jquery.mobile-1.3.1.css
/*
* jQuery Mobile 1.3.1
* Git HEAD hash: 74b4bec049fd93e4fe40205e6157de16eb64eb46 <> Date: Wed Apr 10 2013 21:57:23 UTC
* http://jquerymobile.com
*
* Copyright 2010, 2013 jQuery Foundation, Inc. and other contributors
* Released under the MIT license.
* http://jquery.org/license
*
*/


/* Swatches */
/* A
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-a {
	border: 1px solid 		#005994 /*{a-bar-border}*/;
	background: 			#0093EA /*{a-bar-background-color}*/;
	color: 					#fff /*{a-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-bar-background-start}*/), to( #007dcd /*{a-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-bar-background-start}*/, #007dcd /*{a-bar-background-end}*/);
}
.ui-bar-a,
.ui-bar-a input,
.ui-bar-a select,
.ui-bar-a textarea,
.ui-bar-a button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-a .ui-link-inherit {
	color: #fff /*{a-bar-color}*/;
}
.ui-bar-a a.ui-link {
	color: #7cc4e7 /*{a-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-a a.ui-link:visited {
    color: #2489ce /*{a-bar-link-visited}*/;
}
.ui-bar-a a.ui-link:hover {
	color: #2489ce /*{a-bar-link-hover}*/;
}
.ui-bar-a a.ui-link:active {
	color: #2489ce /*{a-bar-link-active}*/;
}
.ui-body-a,
.ui-overlay-a {
	border: 1px solid 		#444 /*{a-body-border}*/;
	background: 			#222 /*{a-body-background-color}*/;
	color: 					#fff /*{a-body-color}*/;
	font-weight: normal;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #444 /*{a-body-background-start}*/), to( #222 /*{a-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #444 /*{a-body-background-start}*/, #222 /*{a-body-background-end}*/);	
}
.ui-overlay-a {
	background-image: none;
	border-width: 0;
}
.ui-body-a,
.ui-body-a input,
.ui-body-a select,
.ui-body-a textarea,
.ui-body-a button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-a .ui-link-inherit {
	color: 	#fff /*{a-body-color}*/;
}
.ui-body-a .ui-link {
	color: #2489ce /*{a-body-link-color}*/;
	font-weight: bold;
}
.ui-body-a .ui-link:visited {
    color: #2489ce /*{a-body-link-visited}*/;
}
.ui-body-a .ui-link:hover {
	color: #2489ce /*{a-body-link-hover}*/;
}
.ui-body-a .ui-link:active {
	color: #2489ce /*{a-body-link-active}*/;
}
.ui-btn-up-a {
	border: 1px solid 		#007dcd /*{a-bup-border}*/;
	background: 			#333 /*{a-bup-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-bup-background-start}*/), to( #0093EA /*{a-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-bup-background-start}*/, #0093EA /*{a-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-bup-background-start}*/, #0093EA /*{a-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-bup-background-start}*/, #0093EA /*{a-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-bup-background-start}*/, #0093EA /*{a-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-bup-background-start}*/, #0093EA /*{a-bup-background-end}*/);
}
.ui-btn-up-a:visited,
.ui-btn-up-a a.ui-link-inherit {
	color: 					#fff /*{a-bup-color}*/;
}
.ui-btn-hover-a {
	border: 1px solid 		#007dcd /*{a-bhover-border}*/;
	background: 			#444 /*{a-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{a-bhover-background-start}*/), to( #0093EA /*{a-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{a-bhover-background-start}*/, #0093EA /*{a-bhover-background-end}*/);
}
.ui-btn-hover-a:visited,
.ui-btn-hover-a:hover,
.ui-btn-hover-a a.ui-link-inherit {
	color: 					#fff /*{a-bhover-color}*/;
}
.ui-btn-down-a {
	border: 1px solid 		#000 /*{a-bdown-border}*/;
	background: 			#222 /*{a-bdown-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{a-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{a-bdown-background-start}*/), to( #007dcd /*{a-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{a-bdown-background-start}*/, #007dcd /*{a-bdown-background-end}*/);
}
.ui-btn-down-a:visited,
.ui-btn-down-a:hover,
.ui-btn-down-a a.ui-link-inherit {
	color: 					#fff /*{a-bdown-color}*/;
}
.ui-btn-up-a,
.ui-btn-hover-a,
.ui-btn-down-a {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* B
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-b {
	border: 1px solid 		#005994 /*{b-bar-border}*/;
	background: 			#0093EA /*{b-bar-background-color}*/;
	color: 					#fff /*{b-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{b-bar-background-start}*/), to( #007dcd /*{b-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{b-bar-background-start}*/, #007dcd /*{b-bar-background-end}*/);
}
.ui-bar-b,
.ui-bar-b input,
.ui-bar-b select,
.ui-bar-b textarea,
.ui-bar-b button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-b .ui-link-inherit {
	color: 	#fff /*{b-bar-color}*/;
}
.ui-bar-b a.ui-link {
	color: #ddf0f8 /*{b-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-b a.ui-link:visited {
    color: #ddf0f8 /*{b-bar-link-visited}*/;
}
.ui-bar-b a.ui-link:hover {
	color: #ddf0f8 /*{b-bar-link-hover}*/;
}
.ui-bar-b a.ui-link:active {
	color: #ddf0f8 /*{b-bar-link-active}*/;
}
.ui-body-b,
.ui-overlay-b {
	border: 1px solid 		#999 /*{b-body-border}*/;
	background: 			#f3f3f3 /*{b-body-background-color}*/;
	color: 					#222 /*{b-body-color}*/;
	font-weight: normal;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ddd /*{b-body-background-start}*/), to( #ccc /*{b-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ddd /*{b-body-background-start}*/, #ccc /*{b-body-background-end}*/);
}
.ui-overlay-b {
	background-image: none;
	border-width: 0;
}
.ui-body-b,
.ui-body-b input,
.ui-body-b select,
.ui-body-b textarea,
.ui-body-b button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-b .ui-link-inherit {
	color: 	#333 /*{b-body-color}*/;
}
.ui-body-b .ui-link {
	color: #2489ce /*{b-body-link-color}*/;
	font-weight: bold;
}
.ui-body-b .ui-link:visited {
    color: #2489ce /*{b-body-link-visited}*/;
}
.ui-body-b .ui-link:hover {
	color: #2489ce /*{b-body-link-hover}*/;
}
.ui-body-b .ui-link:active {
	color: #2489ce /*{b-body-link-active}*/;
}
.ui-btn-up-b {
	border: 1px solid 		#044062 /*{b-bup-border}*/;
	background: 			#396b9e /*{b-bup-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #5f9cc5 /*{b-bup-background-start}*/), to( #396b9e /*{b-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #5f9cc5 /*{b-bup-background-start}*/, #396b9e /*{b-bup-background-end}*/);
}
.ui-btn-up-b:visited,
.ui-btn-up-b a.ui-link-inherit {
	color: 					#fff /*{b-bup-color}*/;
}
.ui-btn-hover-b {
	border: 1px solid 		#00415e /*{b-bhover-border}*/;
	background: 			#4b88b6 /*{b-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #6facd5 /*{b-bhover-background-start}*/), to( #4272a4 /*{b-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #6facd5 /*{b-bhover-background-start}*/, #4272a4 /*{b-bhover-background-end}*/);
}
.ui-btn-hover-b:visited,
.ui-btn-hover-b:hover,
.ui-btn-hover-b a.ui-link-inherit {
	color: 					#fff /*{b-bhover-color}*/;
}
.ui-btn-down-b {
	border: 1px solid 		#225377 /*{b-bdown-border}*/;
	background: 			#4e89c5 /*{b-bdown-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{b-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #295b8e /*{b-bdown-background-start}*/), to( #3e79b5 /*{b-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #295b8e /*{b-bdown-background-start}*/, #3e79b5 /*{b-bdown-background-end}*/);
}
.ui-btn-down-b:visited,
.ui-btn-down-b:hover,
.ui-btn-down-b a.ui-link-inherit {
	color: 					#fff /*{b-bdown-color}*/;
}
.ui-btn-up-b,
.ui-btn-hover-b,
.ui-btn-down-b {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* C
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-c {
	border: 1px solid 		#b3b3b3 /*{c-bar-border}*/;
	background: 			#eee /*{c-bar-background-color}*/;
	color: 					#3e3e3e /*{c-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #f0f0f0 /*{c-bar-background-start}*/), to( #ddd /*{c-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #f0f0f0 /*{c-bar-background-start}*/, #ddd /*{c-bar-background-end}*/);
}
.ui-bar-c .ui-link-inherit {
	color: 	#3e3e3e /*{c-bar-color}*/;
}
.ui-bar-c a.ui-link {
	color: #7cc4e7 /*{c-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-c a.ui-link:visited {
    color: #2489ce /*{c-bar-link-visited}*/;
}
.ui-bar-c a.ui-link:hover {
	color: #2489ce /*{c-bar-link-hover}*/;
}
.ui-bar-c a.ui-link:active {
	color: #2489ce /*{c-bar-link-active}*/;
}
.ui-bar-c,
.ui-bar-c input,
.ui-bar-c select,
.ui-bar-c textarea,
.ui-bar-c button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-c,
.ui-overlay-c {
	border: 1px solid 		#aaa /*{c-body-border}*/;
	color: 					#333 /*{c-body-color}*/;
	background: 			#eee /*{c-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #eee /*{c-body-background-start}*/), to( #eee /*{c-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #eee /*{c-body-background-start}*/, #eee /*{c-body-background-end}*/);
}
.ui-overlay-c {
	background-image: none;
	border-width: 0;
}
.ui-body-c,
.ui-body-c input,
.ui-body-c select,
.ui-body-c textarea,
.ui-body-c button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-c .ui-link-inherit {
	color: 	#333 /*{c-body-color}*/;
}
.ui-body-c .ui-link {
	color: #007dcd /*{c-body-link-color}*/;
	font-weight: bold;
}
.ui-body-c .ui-link:visited {
    color: #007dcd /*{c-body-link-visited}*/;
}
.ui-body-c .ui-link:hover {
	color: #0093EA /*{c-body-link-hover}*/;
}
.ui-body-c .ui-link:active {
	color: #007dcd /*{c-body-link-active}*/;
}
.ui-btn-up-c {
	border: 1px solid 		#ccc /*{c-bup-border}*/;
	background: 			#eee /*{c-bup-background-color}*/;
	font-weight: bold;
	color: 					#222 /*{c-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff /*{c-bup-background-start}*/), to( #fff /*{c-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff /*{c-bup-background-start}*/, #fff /*{c-bup-background-end}*/);
}
.ui-btn-up-c:visited,
.ui-btn-up-c a.ui-link-inherit {
	color: 					#2f3e46 /*{c-bup-color}*/;
}
.ui-btn-hover-c {
	border: 1px solid 		#bbb /*{c-bhover-border}*/;
	background: 			#dfdfdf /*{c-bhover-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{c-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #0093EA /*{c-bhover-background-start}*/), to( #0093EA /*{c-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #0093EA /*{c-bhover-background-start}*/, #0093EA /*{c-bhover-background-end}*/);
}
.ui-btn-hover-c:visited,
.ui-btn-hover-c:hover,
.ui-btn-hover-c a.ui-link-inherit {
	color: 					#fff /*{c-bhover-color}*/;
}
.ui-btn-down-c {
	border: 1px solid 		#bbb /*{c-bdown-border}*/;
	background: 			#d6d6d6 /*{c-bdown-background-color}*/;
	font-weight: bold;
	color: 					#222 /*{c-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{c-bdown-background-start}*/), to( #007dcd /*{c-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{c-bdown-background-start}*/, #007dcd /*{c-bdown-background-end}*/);
}
.ui-btn-down-c:visited,
.ui-btn-down-c:hover,
.ui-btn-down-c a.ui-link-inherit {
	color: 					#2f3e46 /*{c-bdown-color}*/;
}
.ui-btn-up-c,
.ui-btn-hover-c,
.ui-btn-down-c {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* D
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-d {
	border: 1px solid 		#bbb /*{d-bar-border}*/;
	background: 			#bbb /*{d-bar-background-color}*/;
	color: 					#333 /*{d-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ddd /*{d-bar-background-start}*/), to( #bbb /*{d-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ddd /*{d-bar-background-start}*/, #bbb /*{d-bar-background-end}*/);
}
.ui-bar-d,
.ui-bar-d input,
.ui-bar-d select,
.ui-bar-d textarea,
.ui-bar-d button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-d .ui-link-inherit {
	color: 	#333 /*{d-bar-color}*/;
}
.ui-bar-d a.ui-link {
	color: #2489ce /*{d-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-d a.ui-link:visited {
    color: #2489ce /*{d-bar-link-visited}*/;
}
.ui-bar-d a.ui-link:hover {
	color: #2489ce /*{d-bar-link-hover}*/;
}
.ui-bar-d a.ui-link:active {
	color: #2489ce /*{d-bar-link-active}*/;
}
.ui-body-d,
.ui-overlay-d {
	border: 1px solid 		#bbb /*{d-body-border}*/;
	color: 					#333 /*{d-body-color}*/;
	background: 			#fff /*{d-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff /*{d-body-background-start}*/), to( #fff /*{d-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff /*{d-body-background-start}*/, #fff /*{d-body-background-end}*/);
}
.ui-overlay-d {
	background-image: none;
	border-width: 0;
}
.ui-body-d,
.ui-body-d input,
.ui-body-d select,
.ui-body-d textarea,
.ui-body-d button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-d .ui-link-inherit {
	color: 	#333 /*{d-body-color}*/;
}
.ui-body-d .ui-link {
	color: #2489ce /*{d-body-link-color}*/;
	font-weight: bold;
}
.ui-body-d .ui-link:visited {
    color: #2489ce /*{d-body-link-visited}*/;
}
.ui-body-d .ui-link:hover {
	color: #2489ce /*{d-body-link-hover}*/;
}
.ui-body-d .ui-link:active {
	color: #2489ce /*{d-body-link-active}*/;
}
.ui-btn-up-d {
	border: 1px solid 		#bbb /*{d-bup-border}*/;
	background: 			#fff /*{d-bup-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fafafa /*{d-bup-background-start}*/), to( #f6f6f6 /*{d-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fafafa /*{d-bup-background-start}*/, #f6f6f6 /*{d-bup-background-end}*/);
}
.ui-btn-up-d:visited,
.ui-btn-up-d a.ui-link-inherit {
	color: 					#333 /*{d-bup-color}*/;
}
.ui-btn-hover-d {
	border: 1px solid 		#aaa /*{d-bhover-border}*/;
	background: 			#eee /*{d-bhover-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bhover-color}*/;
	cursor: pointer;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #eee /*{d-bhover-background-start}*/), to( #fff /*{d-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #eee /*{d-bhover-background-start}*/, #fff /*{d-bhover-background-end}*/);
}
.ui-btn-hover-d:visited,
.ui-btn-hover-d:hover,
.ui-btn-hover-d a.ui-link-inherit {
	color: 					#333 /*{d-bhover-color}*/;
}
.ui-btn-down-d {
	border: 1px solid 		#aaa /*{d-bdown-border}*/;
	background: 			#eee /*{d-bdown-background-color}*/;
	font-weight: bold;
	color: 					#333 /*{d-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #e5e5e5 /*{d-bdown-background-start}*/), to( #f2f2f2 /*{d-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #e5e5e5 /*{d-bdown-background-start}*/, #f2f2f2 /*{d-bdown-background-end}*/);
}
.ui-btn-down-d:visited,
.ui-btn-down-d:hover,
.ui-btn-down-d a.ui-link-inherit {
	color: 					#333 /*{d-bdown-color}*/;
}
.ui-btn-up-d,
.ui-btn-hover-d,
.ui-btn-down-d {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* E
-----------------------------------------------------------------------------------------------------------*/
.ui-bar-e {
	border: 1px solid 		#f7c942 /*{e-bar-border}*/;
	background: 			#fadb4e /*{e-bar-background-color}*/;
	color: 					#333 /*{e-bar-color}*/;
	font-weight: bold;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fceda7 /*{e-bar-background-start}*/), to( #fbef7e /*{e-bar-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fceda7 /*{e-bar-background-start}*/, #fbef7e /*{e-bar-background-end}*/);
}
.ui-bar-e,
.ui-bar-e input,
.ui-bar-e select,
.ui-bar-e textarea,
.ui-bar-e button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-bar-e .ui-link-inherit {
	color: 	#333 /*{e-bar-color}*/;
}
.ui-bar-e a.ui-link {
	color: #2489ce /*{e-bar-link-color}*/;
	font-weight: bold;
}
.ui-bar-e a.ui-link:visited {
    color: #2489ce /*{e-bar-link-visited}*/;
}
.ui-bar-e a.ui-link:hover {
	color: #2489ce /*{e-bar-link-hover}*/;
}
.ui-bar-e a.ui-link:active {
	color: #2489ce /*{e-bar-link-active}*/;
}
.ui-body-e,
.ui-overlay-e {
	border: 1px solid 		#f7c942 /*{e-body-border}*/;
	color: 					#222 /*{e-body-color}*/;
	background: 			#fff9df /*{e-body-background-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fffadf /*{e-body-background-start}*/), to( #fff3a5 /*{e-body-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fffadf /*{e-body-background-start}*/, #fff3a5 /*{e-body-background-end}*/);
}
.ui-overlay-e {
	background-image: none;
	border-width: 0;
}
.ui-body-e,
.ui-body-e input,
.ui-body-e select,
.ui-body-e textarea,
.ui-body-e button {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-body-e .ui-link-inherit {
	color: 	#222 /*{e-body-color}*/;
}
.ui-body-e .ui-link {
	color: #2489ce /*{e-body-link-color}*/;
	font-weight: bold;
}
.ui-body-e .ui-link:visited {
    color: #2489ce /*{e-body-link-visited}*/;
}
.ui-body-e .ui-link:hover {
	color: #2489ce /*{e-body-link-hover}*/;
}
.ui-body-e .ui-link:active {
	color: #2489ce /*{e-body-link-active}*/;
}
.ui-btn-up-e {
	border: 1px solid 		#f4c63f /*{e-bup-border}*/;
	background: 			#fadb4e /*{e-bup-background-color}*/;
	font-weight: bold;
	color: 					#222 /*{e-bup-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #ffefaa /*{e-bup-background-start}*/), to( #ffe155 /*{e-bup-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #ffefaa /*{e-bup-background-start}*/, #ffe155 /*{e-bup-background-end}*/);
}
.ui-btn-up-e:visited,
.ui-btn-up-e a.ui-link-inherit {
	color: 					#222 /*{e-bup-color}*/;
}
.ui-btn-hover-e {
	border: 1px solid 		#f2c43d /*{e-bhover-border}*/;
	background: 			#fbe26f /*{e-bhover-background-color}*/;
	font-weight: bold;
	color: 					#111 /*{e-bhover-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #fff5ba /*{e-bhover-background-start}*/), to( #fbdd52 /*{e-bhover-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #fff5ba /*{e-bhover-background-start}*/, #fbdd52 /*{e-bhover-background-end}*/);
}
.ui-btn-hover-e:visited,
.ui-btn-hover-e:hover,
.ui-btn-hover-e a.ui-link-inherit {
	color: 					#333 /*{e-bhover-color}*/;
}
.ui-btn-down-e {
	border: 1px solid 		#f2c43d /*{e-bdown-border}*/;
	background: 			#fceda7 /*{e-bdown-background-color}*/;
	font-weight: bold;
	color: 					#111 /*{e-bdown-color}*/;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #f8d94c /*{e-bdown-background-start}*/), to( #fadb4e /*{e-bdown-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #f8d94c /*{e-bdown-background-start}*/, #fadb4e /*{e-bdown-background-end}*/);
}
.ui-btn-down-e:visited,
.ui-btn-down-e:hover,
.ui-btn-down-e a.ui-link-inherit {
	color: 					#333 /*{e-bdown-color}*/;
}
.ui-btn-up-e,
.ui-btn-hover-e,
.ui-btn-down-e {
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
	text-decoration: none;
}
/* Structure */
/* links within "buttons" 
-----------------------------------------------------------------------------------------------------------*/
a.ui-link-inherit {
	text-decoration: none !important;
}
/* Active class used as the "on" state across all themes
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-active {
	border: 1px solid 		#0093EA /*{global-active-border}*/;
	background: 			#007dcd /*{global-active-background-color}*/;
	font-weight: bold;
	color: 					#fff /*{global-active-color}*/;
	cursor: pointer;
	text-decoration: none;
	background-image: -webkit-gradient(linear, left top, left bottom, from( #007dcd /*{global-active-background-start}*/), to( #007dcd /*{global-active-background-end}*/)); /* Saf4+, Chrome */
	background-image: -webkit-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* Chrome 10+, Saf5.1+ */
	background-image:    -moz-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* FF3.6 */
	background-image:     -ms-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* IE10 */
	background-image:      -o-linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/); /* Opera 11.10+ */
	background-image:         linear-gradient( #007dcd /*{global-active-background-start}*/, #007dcd /*{global-active-background-end}*/);
	font-family: Helvetica, Arial, sans-serif /*{global-font-family}*/;
}
.ui-btn-active:visited,
.ui-btn-active:hover,
.ui-btn-active a.ui-link-inherit {
	color: 					#fff /*{global-active-color}*/;
}
/* button inner top highlight
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-inner {
	border-top: 1px solid 	#fff;
	border-color: 			rgba(255,255,255,.3);
}
/* corner rounding classes
-----------------------------------------------------------------------------------------------------------*/
.ui-corner-all {
	-webkit-border-radius: 				0.2em /*{global-radii-blocks}*/;
	border-radius: 						0.2em /*{global-radii-blocks}*/;
}
/* Form field separator
-----------------------------------------------------------------------------------------------------------*/
.ui-br {
	border-color: rgb(130,130,130);
	border-color: rgba(130,130,130,.3);
	border-style: solid;
}
/* Interaction cues
-----------------------------------------------------------------------------------------------------------*/
.ui-disabled {
	filter: Alpha(Opacity=30);
	opacity: .3;
	zoom: 1;
}
.ui-disabled,
.ui-disabled a {
	cursor: default !important;
	pointer-events: none;
}
/* Icons
-----------------------------------------------------------------------------------------------------------*/
.ui-icon,
.ui-icon-searchfield:after {
	background-color: 						#666 /*{global-icon-color}*/;
	background-color: 						rgba(0,0,0,.4) /*{global-icon-disc}*/;
	background-image: url(images/icons-18-white.png) /*{global-icon-set}*/;
	background-repeat: no-repeat;
	-webkit-border-radius: 				9px;
	border-radius: 						9px;
}
/* Alt icon color
-----------------------------------------------------------------------------------------------------------*/
.ui-icon-alt .ui-icon,
.ui-icon-alt .ui-icon-searchfield:after {
	background-color: 						#fff;
	background-color: 						rgba(255,255,255,.3);
	background-image: url(images/icons-18-black.png);
	background-repeat: no-repeat;
}
/* No disc
-----------------------------------------------------------------------------------------------------------*/
.ui-icon-nodisc .ui-icon,
.ui-icon-nodisc .ui-icon-searchfield:after,
.ui-icon-nodisc .ui-icon-alt .ui-icon,
.ui-icon-nodisc .ui-icon-alt .ui-icon-searchfield:after {
	background-color: transparent;
}
/* Icon sprite
-----------------------------------------------------------------------------------------------------------*/
/* plus minus */
.ui-icon-plus {
	background-position: 	-1px -1px;
}
.ui-icon-minus {
	background-position: 	-37px -1px;
}
/* delete/close */
.ui-icon-delete {
	background-position: 	-73px -1px;
}
/* arrows */
.ui-icon-arrow-r {
	background-position: 	-108px -1px;
}
.ui-icon-arrow-l {
	background-position: 	-144px -1px;
}
.ui-icon-arrow-u {
	background-position: 	-180px -1px;
}
.ui-icon-arrow-d {
	background-position: 	-216px -1px;
}
/* misc */
.ui-icon-check {
	background-position: 	-252px -1px;
}
.ui-icon-gear {
	background-position: 	-288px -1px;
}
.ui-icon-refresh {
	background-position: 	-323px -1px;
}
.ui-icon-forward {
	background-position: 	-360px -1px;
}
.ui-icon-back {
	background-position: 	-396px -1px;
}
.ui-icon-grid {
	background-position: 	-432px -1px;
}
.ui-icon-star {
	background-position: 	-467px -1px;
}
.ui-icon-alert {
	background-position: 	-503px -1px;
}
.ui-icon-info {
	background-position: 	-539px -1px;
}
.ui-icon-home {
	background-position: 	-575px -1px;
}
/* search */
.ui-icon-search,
.ui-icon-searchfield:after {
	background-position: 	-611px -1px;
}
/* checkbox radio */
.ui-icon-checkbox-on {
	background-position: 	-647px -1px;
}
.ui-icon-checkbox-off {
	background-position: 	-683px -1px;
}
.ui-icon-radio-on {
	background-position: 	-718px -1px;
}
.ui-icon-radio-off {
	background-position: 	-754px -1px;
}
/* menu edit */
.ui-icon-bars {
	background-position: 	-788px -1px;
}
.ui-icon-edit {
	background-position: 	-824px -1px;
}
/* HD/"retina" sprite
-----------------------------------------------------------------------------------------------------------*/
@media only screen and (-webkit-min-device-pixel-ratio: 1.3),
       only screen and (min--moz-device-pixel-ratio: 1.3),
       only screen and (min-resolution: 200dpi) {
	
	.ui-icon-plus, .ui-icon-minus, .ui-icon-delete, .ui-icon-arrow-r,
	.ui-icon-arrow-l, .ui-icon-arrow-u, .ui-icon-arrow-d, .ui-icon-check,
	.ui-icon-gear, .ui-icon-refresh, .ui-icon-forward, .ui-icon-back,
	.ui-icon-grid, .ui-icon-star, .ui-icon-alert, .ui-icon-info, .ui-icon-home, .ui-icon-bars, .ui-icon-edit,
	.ui-icon-search, .ui-icon-searchfield:after, 
	.ui-icon-checkbox-off, .ui-icon-checkbox-on, .ui-icon-radio-off, .ui-icon-radio-on {
		background-image: url(images/icons-36-white.png);
		-moz-background-size: 864px 18px;
		-o-background-size: 864px 18px;
		-webkit-background-size: 864px 18px;
		background-size: 864px 18px;
	}
	.ui-icon-alt .ui-icon {
		background-image: url(images/icons-36-black.png);
	}
	.ui-icon-plus {
		background-position: 	0 50%;
	}
	.ui-icon-minus {
		background-position: 	-36px 50%;
	}
	.ui-icon-delete {
		background-position: 	-72px 50%;
	}
	.ui-icon-arrow-r {
		background-position: 	-108px 50%;
	}
	.ui-icon-arrow-l {
		background-position: 	-144px 50%;
	}
	.ui-icon-arrow-u {
		background-position: 	-179px 50%;
	}
	.ui-icon-arrow-d {
		background-position: 	-215px 50%;
	}
	.ui-icon-check {
		background-position: 	-252px 50%;
	}
	.ui-icon-gear {
		background-position: 	-287px 50%;
	}
	.ui-icon-refresh {
		background-position: 	-323px 50%;
	}
	.ui-icon-forward {
		background-position: 	-360px 50%;
	}
	.ui-icon-back {
		background-position: 	-395px 50%;
	}
	.ui-icon-grid {
		background-position: 	-431px 50%;
	}
	.ui-icon-star {
		background-position: 	-467px 50%;
	}
	.ui-icon-alert {
		background-position: 	-503px 50%;
	}
	.ui-icon-info {
		background-position: 	-538px 50%;
	}
	.ui-icon-home {
		background-position: 	-575px 50%;
	}
	.ui-icon-search,
	.ui-icon-searchfield:after {
		background-position: 	-611px 50%;
	}
	.ui-icon-checkbox-on {
		background-position: 	-647px 50%;
	}
	.ui-icon-checkbox-off {
		background-position: 	-683px 50%;
	}
	.ui-icon-radio-on {
		background-position: 	-718px 50%;
	}
	.ui-icon-radio-off {
		background-position: 	-754px 50%;
	}
	.ui-icon-bars {
		background-position: 	-788px 50%;
	
	}.ui-icon-edit {
		background-position: 	-824px 50%;
	}
}
/* checks,radios */
.ui-checkbox .ui-icon,
.ui-selectmenu-list .ui-icon {
	-webkit-border-radius: 3px;
	border-radius: 3px;
}
.ui-icon-checkbox-off,
.ui-icon-radio-off {
	background-color: transparent;	
}
.ui-checkbox-on .ui-icon,
.ui-radio-on .ui-icon {
	background-color: #007dcd /*{global-active-background-color}*/; /* NOTE: this hex should match the active state color. It's repeated here for cascade */
}
/* loading icon */
.ui-icon-loading {
	background: url(images/ajax-loader.gif);
	background-size: 46px 46px;
}
/* Button corner class
-----------------------------------------------------------------------------------------------------------*/
.ui-btn-corner-all {
	-webkit-border-radius: 				0.2em /*{global-radii-buttons}*/;
	border-radius: 						0.2em /*{global-radii-buttons}*/;
}
/* radius clip workaround for cleaning up corner trapping */
.ui-corner-all,
.ui-btn-corner-all {
	-webkit-background-clip: padding;
	background-clip: padding-box;
}
/* Overlay / modal
-----------------------------------------------------------------------------------------------------------*/
.ui-overlay {
	background: #666;
	filter: Alpha(Opacity=50);
	opacity: .5;
	position: absolute;
	width: 100%;
	height: 100%;
}
.ui-overlay-shadow {
	-moz-box-shadow: 0 0 12px 			rgba(0,0,0,.6);
	-webkit-box-shadow: 0 0 12px 		rgba(0,0,0,.6);
	box-shadow: 0 0 12px 				rgba(0,0,0,.6);
}
.ui-shadow {
	-moz-box-shadow: 0 1px 1px /*{global-box-shadow-size}*/ 			rgba(0,0,0,0.2) /*{global-box-shadow-color}*/;
	-webkit-box-shadow: 0 1px 1px /*{global-box-shadow-size}*/ 		rgba(0,0,0,0.2) /*{global-box-shadow-color}*/;
	box-shadow: 0 1px 1px /*{global-box-shadow-size}*/ 				rgba(0,0,0,0.2) /*{global-box-shadow-color}*/
}
.ui-bar-a .ui-shadow,
.ui-bar-b .ui-shadow ,
.ui-bar-c .ui-shadow  {
	-moz-box-shadow: 0 1px 0 				rgba(255,255,255,.3);
	-webkit-box-shadow: 0 1px 0 			rgba(255,255,255,.3);
	box-shadow: 0 1px 0 					rgba(255,255,255,.3);
}
.ui-shadow-inset {
	-moz-box-shadow: inset 0 1px 4px 		rgba(0,0,0,.2);
	-webkit-box-shadow: inset 0 1px 4px 	rgba(0,0,0,.2);
	box-shadow: inset 0 1px 4px 			rgba(0,0,0,.2);
}
.ui-icon-shadow {
	-moz-box-shadow: 0 1px 0 				rgba(255,255,255,.4) /*{global-icon-shadow}*/;
	-webkit-box-shadow: 0 1px 0 			rgba(255,255,255,.4) /*{global-icon-shadow}*/;
	box-shadow: 0 1px 0 					rgba(255,255,255,.4) /*{global-icon-shadow}*/;
}
/* Focus state - set here for specificity (note: these classes are added by JavaScript)
-----------------------------------------------------------------------------------------------------------*/
.ui-btn:focus, .ui-link-inherit:focus {
	outline: 0;
}
.ui-btn.ui-focus {
	z-index: 1;
}
.ui-focus,
.ui-btn:focus {
	-moz-box-shadow: inset 0 0 3px 		#007dcd /*{global-active-background-color}*/, 0 0 9px 		#007dcd /*{global-active-background-color}*/;
	-webkit-box-shadow: inset 0 0 3px 	#007dcd /*{global-active-background-color}*/, 0 0 9px 		#007dcd /*{global-active-background-color}*/;
	box-shadow: inset 0 0 3px 			#007dcd /*{global-active-background-color}*/, 0 0 9px 		#007dcd /*{global-active-background-color}*/;
}
.ui-input-text.ui-focus,
.ui-input-search.ui-focus {
	-moz-box-shadow: 0 0 12px 			#007dcd /*{global-active-background-color}*/;
	-webkit-box-shadow: 0 0 12px 		#007dcd /*{global-active-background-color}*/;
	box-shadow: 0 0 12px 					#007dcd /*{global-active-background-color}*/;	
}
/* unset box shadow in browsers that don't do it right
-----------------------------------------------------------------------------------------------------------*/
.ui-mobile-nosupport-boxshadow * {
	-moz-box-shadow: none !important;
	-webkit-box-shadow: none !important;
	box-shadow: none !important;
}
/* ...and bring back focus */
.ui-mobile-nosupport-boxshadow .ui-focus,
.ui-mobile-nosupport-boxshadow .ui-btn:focus,
.ui-mobile-nosupport-boxshadow .ui-link-inherit:focus {
	outline-width: 1px;
	outline-style: auto;
}
/* some unsets - more probably needed */
.ui-mobile, .ui-mobile body { height: 99.9%; }
.ui-mobile fieldset, .ui-page { padding: 0; margin: 0; }
.ui-mobile a img, .ui-mobile fieldset { border-width: 0; }
/* responsive page widths */
.ui-mobile-viewport { margin: 0; overflow-x: visible; -webkit-text-size-adjust: 100%; -ms-text-size-adjust:none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); }
/* Issue #2066 */
body.ui-mobile-viewport,
div.ui-mobile-viewport { overflow-x: hidden; }
/* "page" containers - full-screen views, one should always be in view post-pageload */
.ui-mobile [data-role=page], .ui-mobile [data-role=dialog], .ui-page { top: 0; left: 0; width: 100%; min-height: 100%; position: absolute; display: none; border: 0; }
.ui-mobile .ui-page-active { display: block; overflow: visible; }
/* on ios4, setting focus on the page element causes flashing during transitions when there is an outline, so we turn off outlines */
.ui-page { outline: none; }
/*orientations from js are available */
@media screen and (orientation: portrait){
.ui-mobile .ui-page { min-height: 420px; }
}
@media screen and (orientation: landscape){
.ui-mobile .ui-page { min-height: 300px; }
}
/* loading screen */
.ui-loading .ui-loader { display: block; }
.ui-loader { display: none; z-index: 9999999; position: fixed; top: 50%; left: 50%; border:0; }
.ui-loader-default { background: none; filter: Alpha(Opacity=18); opacity: .18; width: 46px; height: 46px; margin-left: -23px; margin-top: -23px; }
.ui-loader-verbose { width: 200px; filter: Alpha(Opacity=88); opacity: .88; box-shadow: 0 1px 1px -1px #fff; height: auto; margin-left: -110px; margin-top: -43px; padding: 10px; }
.ui-loader-default h1 { font-size: 0; width: 0; height: 0; overflow: hidden; }
.ui-loader-verbose h1 { font-size: 16px; margin: 0; text-align: center; }
.ui-loader .ui-icon { background-color: #000; display: block; margin: 0; width: 44px; height: 44px; padding: 1px; -webkit-border-radius: 36px; border-radius: 36px; }
.ui-loader-verbose .ui-icon { margin: 0 auto 10px; filter: Alpha(Opacity=75); opacity: .75; }
.ui-loader-textonly { padding: 15px; margin-left: -115px; }
.ui-loader-textonly .ui-icon { display: none; }
.ui-loader-fakefix { position: absolute; }
/*fouc*/
.ui-mobile-rendering > * { visibility: hidden; }
/*headers, content panels*/
.ui-bar, .ui-body { position: relative; padding: .4em 15px; overflow: hidden; display: block; clear:both; }
.ui-bar { font-size: 16px; margin: 0; }
.ui-bar h1, .ui-bar h2, .ui-bar h3, .ui-bar h4, .ui-bar h5, .ui-bar h6 { margin: 0; padding: 0; font-size: 16px; display: inline-block; }
.ui-header, .ui-footer { position: relative; zoom: 1; }
.ui-mobile .ui-header, .ui-mobile .ui-footer { border-left-width: 0; border-right-width: 0; }
.ui-header .ui-btn-left,
.ui-header .ui-btn-right,
.ui-footer .ui-btn-left,
.ui-footer .ui-btn-right,
.ui-header-fixed.ui-fixed-hidden .ui-btn-left,
.ui-header-fixed.ui-fixed-hidden .ui-btn-right { position: absolute; top: 3px; }
.ui-header-fixed .ui-btn-left,
.ui-header-fixed .ui-btn-right { top: 4px;}
.ui-header .ui-btn-left,
.ui-footer .ui-btn-left { left: 5px; }
.ui-header .ui-btn-right,
.ui-footer .ui-btn-right { right: 5px; }
.ui-footer > .ui-btn-icon-notext,
.ui-header > .ui-btn-icon-notext,
.ui-header-fixed.ui-fixed-hidden > .ui-btn-icon-notext { top: 6px; }
.ui-header-fixed > .ui-btn-icon-notext { top: 7px;}
.ui-header .ui-title, .ui-footer .ui-title { min-height: 1.1em; text-align: center; font-size: 16px; display: block; margin: .6em 30% .8em; padding: 0; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; outline: 0 !important; }
.ui-footer .ui-title { margin: .6em 15px .8em; }
/* content area*/
.ui-content { border-width: 0; overflow: visible; overflow-x: hidden; padding: 15px; }
/* corner styling for dialogs and popups */
.ui-corner-all > .ui-header:first-child,
.ui-corner-all > .ui-content:first-child,
.ui-corner-all > .ui-footer:first-child {
	-webkit-border-top-left-radius: inherit;
	border-top-left-radius: inherit;
	-webkit-border-top-right-radius: inherit;
	border-top-right-radius: inherit;
}
.ui-corner-all > .ui-header:last-child,
.ui-corner-all > .ui-content:last-child,
.ui-corner-all > .ui-footer:last-child {
	-webkit-border-bottom-left-radius: inherit;
	border-bottom-left-radius: inherit;
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius: inherit;
}
/* icons sizing */
.ui-icon { width: 18px; height: 18px; }
/* non-js content hiding */
.ui-nojs { position: absolute; left: -9999px; }
/* accessible content hiding */
.ui-hide-label label.ui-input-text, .ui-hide-label label.ui-select, .ui-hide-label label.ui-slider, .ui-hide-label label.ui-submit, .ui-hide-label .ui-controlgroup-label,
.ui-hidden-accessible { position: absolute !important; left: -9999px; clip: rect(1px 1px 1px 1px); clip: rect(1px,1px,1px,1px); }
/* Transitions originally inspired by those from jQtouch, nice work, folks */
.ui-mobile-viewport-transitioning,
.ui-mobile-viewport-transitioning .ui-page {
	width: 100%;
	height: 100%;
	overflow: hidden;
	-webkit-box-sizing: border-box;
	-moz-box-sizing: border-box;
	box-sizing: border-box;
}
.ui-page-pre-in {
	opacity: 0;
}
.in {
	-webkit-animation-timing-function: ease-out;
	-webkit-animation-duration: 350ms;
	-moz-animation-timing-function: ease-out;
	-moz-animation-duration: 350ms;
	animation-timing-function: ease-out;
	animation-duration: 350ms;
}
.out {
	-webkit-animation-timing-function: ease-in;
	-webkit-animation-duration: 225ms;
	-moz-animation-timing-function: ease-in;
	-moz-animation-duration: 225ms;
	animation-timing-function: ease-in;
	animation-duration: 225ms;
}
@-webkit-keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
@-moz-keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes fadein {
    from { opacity: 0; }
    to { opacity: 1; }
}
@-webkit-keyframes fadeout {
    from { opacity: 1; }
    to { opacity: 0; }
}
@-moz-keyframes fadeout {
    from { opacity: 1; }
    to { opacity: 0; }
}
@keyframes fadeout {
    from { opacity: 1; }
    to { opacity: 0; }
}
.fade.out {
	opacity: 0;
	-webkit-animation-duration: 125ms;
	-webkit-animation-name: fadeout;
	-moz-animation-duration: 125ms;
	-moz-animation-name: fadeout;
	animation-duration: 125ms;
	animation-name: fadeout;
}
.fade.in {
	opacity: 1;
	-webkit-animation-duration: 225ms;
	-webkit-animation-name: fadein;
	-moz-animation-duration: 225ms;
	-moz-animation-name: fadein;
	animation-duration: 225ms;
	animation-name: fadein;
}
.pop {
	-webkit-transform-origin: 50% 50%;
	-moz-transform-origin: 50% 50%;
	transform-origin: 50% 50%;
}
.pop.in {
	-webkit-transform: scale(1);
	-webkit-animation-name: popin;
	-webkit-animation-duration: 350ms;
	-moz-transform: scale(1);
	-moz-animation-name: popin;
	-moz-animation-duration: 350ms;
	transform: scale(1);
	animation-name: popin;
	animation-duration: 350ms;
    opacity: 1;
}
.pop.out {
	-webkit-animation-name: fadeout;
	-webkit-animation-duration: 100ms;
	-moz-animation-name: fadeout;
	-moz-animation-duration: 100ms;
	animation-name: fadeout;
	animation-duration: 100ms;
	opacity: 0;
}
.pop.in.reverse {
	-webkit-animation-name: fadein;
	-moz-animation-name: fadein;
	animation-name: fadein;
}
.pop.out.reverse {
	-webkit-transform: scale(.8);
	-webkit-animation-name: popout;
	-moz-transform: scale(.8);
	-moz-animation-name: popout;
	transform: scale(.8);
	animation-name: popout;
}
@-webkit-keyframes popin {
    from {
        -webkit-transform: scale(.8);
        opacity: 0;
    }
    to {
        -webkit-transform: scale(1);
        opacity: 1;
    }
}
@-moz-keyframes popin {
    from {
        -moz-transform: scale(.8);
        opacity: 0;
    }
    to {
        -moz-transform: scale(1);
        opacity: 1;
    }
}
@keyframes popin {
    from {
        transform: scale(.8);
        opacity: 0;
    }
    to {
        transform: scale(1);
        opacity: 1;
    }
}
@-webkit-keyframes popout {
    from {
        -webkit-transform: scale(1);
        opacity: 1;
    }
    to {
        -webkit-transform: scale(.8);
        opacity: 0;
    }
}
@-moz-keyframes popout {
    from {
        -moz-transform: scale(1);
        opacity: 1;
    }
    to {
        -moz-transform: scale(.8);
        opacity: 0;
    }
}
@keyframes popout {
    from {
        transform: scale(1);
        opacity: 1;
    }
    to {
        transform: scale(.8);
        opacity: 0;
    }
}
/* keyframes for slidein from sides */
@-webkit-keyframes slideinfromright {
    from { -webkit-transform: translate3d(100%,0,0); }
    to { -webkit-transform: translate3d(0,0,0); }
}
@-moz-keyframes slideinfromright {
    from { -moz-transform: translateX(100%); }
    to { -moz-transform: translateX(0); }
}
@keyframes slideinfromright {
    from { transform: translateX(100%); }
    to { transform: translateX(0); }
}
@-webkit-keyframes slideinfromleft {
    from { -webkit-transform: translate3d(-100%,0,0); }
    to { -webkit-transform: translate3d(0,0,0); }
}
@-moz-keyframes slideinfromleft {
    from { -moz-transform: translateX(-100%); }
    to { -moz-transform: translateX(0); }
}
@keyframes slideinfromleft {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}
/* keyframes for slideout to sides */
@-webkit-keyframes slideouttoleft {
    from { -webkit-transform: translate3d(0,0,0); }
    to { -webkit-transform: translate3d(-100%,0,0); }
}
@-moz-keyframes slideouttoleft {
    from { -moz-transform: translateX(0); }
    to { -moz-transform: translateX(-100%); }
}
@keyframes slideouttoleft {
    from { transform: translateX(0); }
    to { transform: translateX(-100%); }
}
@-webkit-keyframes slideouttoright {
    from { -webkit-transform: translate3d(0,0,0); }
    to { -webkit-transform: translate3d(100%,0,0); }
}
@-moz-keyframes slideouttoright {
    from { -moz-transform: translateX(0); }
    to { -moz-transform: translateX(100%); }
}
@keyframes slideouttoright {
    from { transform: translateX(0); }
    to { transform: translateX(100%); }
}
.slide.out, .slide.in {
	-webkit-animation-timing-function: ease-out;
	-webkit-animation-duration: 350ms;
	-moz-animation-timing-function: ease-out;
	-moz-animation-duration: 350ms;
	animation-timing-function: ease-out;
	animation-duration: 350ms;
}
.slide.out {
	-webkit-transform: translate3d(-100%,0,0);
	-webkit-animation-name: slideouttoleft;
	-moz-transform: translateX(-100%);
	-moz-animation-name: slideouttoleft;
	transform: translateX(-100%);
	animation-name: slideouttoleft;
}
.slide.in {
	-webkit-transform: translate3d(0,0,0);
	-webkit-animation-name: slideinfromright;
	-moz-transform: translateX(0);
	-moz-animation-name: slideinfromright;
	transform: translateX(0);
	animation-name: slideinfromright;
}
.slide.out.reverse {
	-webkit-transform: translate3d(100%,0,0);
	-webkit-animation-name: slideouttoright;
	-moz-transform: translateX(100%);
	-moz-animation-name: slideouttoright;
	transform: translateX(100%);
	animation-name: slideouttoright;
}
.slide.in.reverse {
	-webkit-transform: translate3d(0,0,0);
	-webkit-animation-name: slideinfromleft;
	-moz-transform: translateX(0);
	-moz-animation-name: slideinfromleft;
	transform: translateX(0);
	animation-name: slideinfromleft;
}
.slidefade.out {
	-webkit-transform: translateX(-100%);
	-webkit-animation-name: slideouttoleft;
	-webkit-animation-duration: 225ms;
	-moz-transform: translateX(-100%);
	-moz-animation-name: slideouttoleft;
	-moz-animation-duration: 225ms;
	transform: translateX(-100%);
	animation-name: slideouttoleft;
	animation-duration: 225ms;
}
.slidefade.in {
	-webkit-transform: translateX(0);
	-webkit-animation-name: fadein;
	-webkit-animation-duration: 200ms;
	-moz-transform: translateX(0);
	-moz-animation-name: fadein;
	-moz-animation-duration: 200ms;
	transform: translateX(0);
	animation-name: fadein;
	animation-duration: 200ms;
}
.slidefade.out.reverse {
	-webkit-transform: translateX(100%);
	-webkit-animation-name: slideouttoright;
	-webkit-animation-duration: 200ms;
	-moz-transform: translateX(100%);
	-moz-animation-name: slideouttoright;
	-moz-animation-duration: 200ms;
	transform: translateX(100%);
	animation-name: slideouttoright;
	animation-duration: 200ms;
}
.slidefade.in.reverse {
	-webkit-transform: translateX(0);
	-webkit-animation-name: fadein;
	-webkit-animation-duration: 200ms;
	-moz-transform: translateX(0);
	-moz-animation-name: fadein;
	-moz-animation-duration: 200ms;
	transform: translateX(0);
	animation-name: fadein;
	animation-duration: 200ms;
}
/* slide down */
.slidedown.out {
	-webkit-animation-name: fadeout;
	-webkit-animation-duration: 100ms;
	-moz-animation-name: fadeout;
	-moz-animation-duration: 100ms;
	animation-name: fadeout;
	animation-duration: 100ms;
}
.slidedown.in {
	-webkit-transform: translateY(0);
	-webkit-animation-name: slideinfromtop;
	-webkit-animation-duration: 250ms;
	-moz-transform: translateY(0);
	-moz-animation-name: slideinfromtop;
	-moz-animation-duration: 250ms;
	transform: translateY(0);
	animation-name: slideinfromtop;
	animation-duration: 250ms;
}
.slidedown.in.reverse {
	-webkit-animation-name: fadein;
	-webkit-animation-duration: 150ms;
	-moz-animation-name: fadein;
	-moz-animation-duration: 150ms;
	animation-name: fadein;
	animation-duration: 150ms;
}
.slidedown.out.reverse {
	-webkit-transform: translateY(-100%);
	-webkit-animation-name: slideouttotop;
	-webkit-animation-duration: 200ms;
	-moz-transform: translateY(-100%);
	-moz-animation-name: slideouttotop;
	-moz-animation-duration: 200ms;
	transform: translateY(-100%);
	animation-name: slideouttotop;
	animation-duration: 200ms;
}
@-webkit-keyframes slideinfromtop {
    from { -webkit-transform: translateY(-100%); }
    to { -webkit-transform: translateY(0); }
}
@-moz-keyframes slideinfromtop {
    from { -moz-transform: translateY(-100%); }
    to { -moz-transform: translateY(0); }
}
@keyframes slideinfromtop {
    from { transform: translateY(-100%); }
    to { transform: translateY(0); }
}
@-webkit-keyframes slideouttotop {
    from { -webkit-transform: translateY(0); }
    to { -webkit-transform: translateY(-100%); }
}
@-moz-keyframes slideouttotop {
    from { -moz-transform: translateY(0); }
    to { -moz-transform: translateY(-100%); }
}
@keyframes slideouttotop {
    from { transform: translateY(0); }
    to { transform: translateY(-100%); }
}
/* slide up */
.slideup.out {
	-webkit-animation-name: fadeout;
	-webkit-animation-duration: 100ms;
	-moz-animation-name: fadeout;
	-moz-animation-duration: 100ms;
	animation-name: fadeout;
	animation-duration: 100ms;
}
.slideup.in {
	-webkit-transform: translateY(0);
	-webkit-animation-name: slideinfrombottom;
	-webkit-animation-duration: 250ms;
	-moz-transform: translateY(0);
	-moz-animation-name: slideinfrombottom;
	-moz-animation-duration: 250ms;
	transform: translateY(0);
	animation-name: slideinfrombottom;
	animation-duration: 250ms;
}
.slideup.in.reverse {
	-webkit-animation-name: fadein;
	-webkit-animation-duration: 150ms;
	-moz-animation-name: fadein;
	-moz-animation-duration: 150ms;
	animation-name: fadein;
	animation-duration: 150ms;
}
.slideup.out.reverse {
	-webkit-transform: translateY(100%);
	-webkit-animation-name: slideouttobottom;
	-webkit-animation-duration: 200ms;
	-moz-transform: translateY(100%);
	-moz-animation-name: slideouttobottom;
	-moz-animation-duration: 200ms;
	transform: translateY(100%);
	animation-name: slideouttobottom;
	animation-duration: 200ms;
}
@-webkit-keyframes slideinfrombottom {
    from { -webkit-transform: translateY(100%); }
    to { -webkit-transform: translateY(0); }
}
@-moz-keyframes slideinfrombottom {
    from { -moz-transform: translateY(100%); }
    to { -moz-transform: translateY(0); }
}
@keyframes slideinfrombottom {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
}
@-webkit-keyframes slideouttobottom {
    from { -webkit-transform: translateY(0); }
    to { -webkit-transform: translateY(100%); }
}
@-moz-keyframes slideouttobottom {
    from { -moz-transform: translateY(0); }
    to { -moz-transform: translateY(100%); }
}
@keyframes slideouttobottom {
    from { transform: translateY(0); }
    to { transform: translateY(100%); }
}
/* The properties in this rule are only necessary for the 'flip' transition.
 * We need specify the perspective to create a projection matrix. This will add
 * some depth as the element flips. The depth number represents the distance of
 * the viewer from the z-plane. According to the CSS3 spec, 1000 is a moderate
 * value.
 */
.viewport-flip {
	-webkit-perspective: 1000;
	-moz-perspective: 1000;
	perspective: 1000;
	position: absolute;
}
.flip {
	-webkit-backface-visibility: hidden;
	-webkit-transform: translateX(0); /* Needed to work around an iOS 3.1 bug that causes listview thumbs to disappear when -webkit-visibility:hidden is used. */
	-moz-backface-visibility: hidden;
	-moz-transform: translateX(0);
	backface-visibility: hidden;
	transform: translateX(0);
}
.flip.out {
	-webkit-transform: rotateY(-90deg) scale(.9);
	-webkit-animation-name: flipouttoleft;
	-webkit-animation-duration: 175ms;
	-moz-transform: rotateY(-90deg) scale(.9);
	-moz-animation-name: flipouttoleft;
	-moz-animation-duration: 175ms;
	transform: rotateY(-90deg) scale(.9);
	animation-name: flipouttoleft;
	animation-duration: 175ms;
}
.flip.in {
	-webkit-animation-name: flipintoright;
	-webkit-animation-duration: 225ms;
	-moz-animation-name: flipintoright;
	-moz-animation-duration: 225ms;
	animation-name: flipintoright;
	animation-duration: 225ms;
}
.flip.out.reverse {
	-webkit-transform: rotateY(90deg) scale(.9);
	-webkit-animation-name: flipouttoright;
	-moz-transform: rotateY(90deg) scale(.9);
	-moz-animation-name: flipouttoright;
	transform: rotateY(90deg) scale(.9);
	animation-name: flipouttoright;
}
.flip.in.reverse {
	-webkit-animation-name: flipintoleft;
	-moz-animation-name: flipintoleft;
	animation-name: flipintoleft;
}
@-webkit-keyframes flipouttoleft {
    from { -webkit-transform: rotateY(0); }
    to { -webkit-transform: rotateY(-90deg) scale(.9); }
}
@-moz-keyframes flipouttoleft {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(-90deg) scale(.9); }
}
@keyframes flipouttoleft {
    from { transform: rotateY(0); }
    to { transform: rotateY(-90deg) scale(.9); }
}
@-webkit-keyframes flipouttoright {
    from { -webkit-transform: rotateY(0) ; }
    to { -webkit-transform: rotateY(90deg) scale(.9); }
}
@-moz-keyframes flipouttoright {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(90deg) scale(.9); }
}
@keyframes flipouttoright {
    from { transform: rotateY(0); }
    to { transform: rotateY(90deg) scale(.9); }
}
@-webkit-keyframes flipintoleft {
    from { -webkit-transform: rotateY(-90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoleft {
    from { -moz-transform: rotateY(-90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@keyframes flipintoleft {
    from { transform: rotateY(-90deg) scale(.9); }
    to { transform: rotateY(0); }
}
@-webkit-keyframes flipintoright {
    from { -webkit-transform: rotateY(90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoright {
    from { -moz-transform: rotateY(90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@keyframes flipintoright {
    from { transform: rotateY(90deg) scale(.9); }
    to { transform: rotateY(0); }
}
/* The properties in this rule are only necessary for the 'flip' transition.
 * We need specify the perspective to create a projection matrix. This will add
 * some depth as the element flips. The depth number represents the distance of
 * the viewer from the z-plane. According to the CSS3 spec, 1000 is a moderate
 * value.
 */
.viewport-turn {
	-webkit-perspective: 200px;
	-moz-perspective: 200px;
	-ms-perspective: 200px;
	perspective: 200px;
	position: absolute;
}
.turn {
	-webkit-backface-visibility: hidden;
	-webkit-transform: translateX(0); /* Needed to work around an iOS 3.1 bug that causes listview thumbs to disappear when -webkit-visibility:hidden is used. */
	-webkit-transform-origin: 0;
	
	-moz-backface-visibility: hidden;
	-moz-transform: translateX(0);
	-moz-transform-origin: 0;
	
	backface-visibility :hidden;
	transform: translateX(0);
	transform-origin: 0;
}
.turn.out {
	-webkit-transform: rotateY(-90deg) scale(.9);
	-webkit-animation-name: flipouttoleft;
	-webkit-animation-duration: 125ms;
	-moz-transform: rotateY(-90deg) scale(.9);
	-moz-animation-name: flipouttoleft;
	-moz-animation-duration: 125ms;
	transform: rotateY(-90deg) scale(.9);
	animation-name: flipouttoleft;
	animation-duration: 125ms;
}
.turn.in {
	-webkit-animation-name: flipintoright;
	-webkit-animation-duration: 250ms;
	-moz-animation-name: flipintoright;
	-moz-animation-duration: 250ms;
	animation-name: flipintoright;
	animation-duration: 250ms;
	
}
.turn.out.reverse {
	-webkit-transform: rotateY(90deg) scale(.9);
	-webkit-animation-name: flipouttoright;
	-moz-transform: rotateY(90deg) scale(.9);
	-moz-animation-name: flipouttoright;
	transform: rotateY(90deg) scale(.9);
	animation-name: flipouttoright;
}
.turn.in.reverse {
	-webkit-animation-name: flipintoleft;
	-moz-animation-name: flipintoleft;
	animation-name: flipintoleft;
}
@-webkit-keyframes flipouttoleft {
    from { -webkit-transform: rotateY(0); }
    to { -webkit-transform: rotateY(-90deg) scale(.9); }
}
@-moz-keyframes flipouttoleft {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(-90deg) scale(.9); }
}
@keyframes flipouttoleft {
    from { transform: rotateY(0); }
    to { transform: rotateY(-90deg) scale(.9); }
}
@-webkit-keyframes flipouttoright {
    from { -webkit-transform: rotateY(0) ; }
    to { -webkit-transform: rotateY(90deg) scale(.9); }
}
@-moz-keyframes flipouttoright {
    from { -moz-transform: rotateY(0); }
    to { -moz-transform: rotateY(90deg) scale(.9); }
}
@keyframes flipouttoright {
    from { transform: rotateY(0); }
    to { transform: rotateY(90deg) scale(.9); }
}
@-webkit-keyframes flipintoleft {
    from { -webkit-transform: rotateY(-90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoleft {
    from { -moz-transform: rotateY(-90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@keyframes flipintoleft {
    from { transform: rotateY(-90deg) scale(.9); }
    to { transform: rotateY(0); }
}
@-webkit-keyframes flipintoright {
    from { -webkit-transform: rotateY(90deg) scale(.9); }
    to { -webkit-transform: rotateY(0); }
}
@-moz-keyframes flipintoright {
    from { -moz-transform: rotateY(90deg) scale(.9); }
    to { -moz-transform: rotateY(0); }
}
@keyframes flipintoright {
    from { transform: rotateY(90deg) scale(.9); }
    to { transform: rotateY(0); }
}
/* flow transition */
.flow {
	-webkit-transform-origin: 50% 30%;
	-webkit-box-shadow: 0 0 20px rgba(0,0,0,.4);
	-moz-transform-origin: 50% 30%;	
	-moz-box-shadow: 0 0 20px rgba(0,0,0,.4);
	transform-origin: 50% 30%;	
	box-shadow: 0 0 20px rgba(0,0,0,.4);
}
.ui-dialog.flow {
	-webkit-transform-origin: none;
	-webkit-box-shadow: none;
	-moz-transform-origin: none;	
	-moz-box-shadow: none;
	transform-origin: none;	
	box-shadow: none;
}
.flow.out {
	-webkit-transform: translateX(-100%) scale(.7);
	-webkit-animation-name: flowouttoleft;
	-webkit-animation-timing-function: ease;
	-webkit-animation-duration: 350ms;
	-moz-transform: translateX(-100%) scale(.7);
	-moz-animation-name: flowouttoleft;
	-moz-animation-timing-function: ease;
	-moz-animation-duration: 350ms;
	transform: translateX(-100%) scale(.7);
	animation-name: flowouttoleft;
	animation-timing-function: ease;
	animation-duration: 350ms;
}
.flow.in {
	-webkit-transform: translateX(0) scale(1);
	-webkit-animation-name: flowinfromright;
	-webkit-animation-timing-function: ease;
	-webkit-animation-duration: 350ms;
	-moz-transform: translateX(0) scale(1);
	-moz-animation-name: flowinfromright;
	-moz-animation-timing-function: ease;
	-moz-animation-duration: 350ms;
	transform: translateX(0) scale(1);
	animation-name: flowinfromright;
	animation-timing-function: ease;
	animation-duration: 350ms;
}
.flow.out.reverse {
	-webkit-transform: translateX(100%);
	-webkit-animation-name: flowouttoright;
	-moz-transform: translateX(100%);
	-moz-animation-name: flowouttoright;
	transform: translateX(100%);
	animation-name: flowouttoright;
}
.flow.in.reverse {
	-webkit-animation-name: flowinfromleft;
	-moz-animation-name: flowinfromleft;
	animation-name: flowinfromleft;
}
@-webkit-keyframes flowouttoleft {
    0% { -webkit-transform: translateX(0) scale(1); }
	60%, 70% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(-100%) scale(.7); }
}
@-moz-keyframes flowouttoleft {
    0% { -moz-transform: translateX(0) scale(1); }
	60%, 70% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform:  translateX(-100%) scale(.7); }
}
@keyframes flowouttoleft {
    0% { transform: translateX(0) scale(1); }
	60%, 70% { transform: translateX(0) scale(.7); }
    100% { transform:  translateX(-100%) scale(.7); }
}
@-webkit-keyframes flowouttoright {
    0% { -webkit-transform: translateX(0) scale(1); }
	60%, 70% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform:  translateX(100%) scale(.7); }
}
@-moz-keyframes flowouttoright {
    0% { -moz-transform: translateX(0) scale(1); }
	60%, 70% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform:  translateX(100%) scale(.7); }
}
@keyframes flowouttoright {
    0% { transform: translateX(0) scale(1); }
	60%, 70% { transform: translateX(0) scale(.7); }
    100% { transform:  translateX(100%) scale(.7); }
}
@-webkit-keyframes flowinfromleft {
    0% { -webkit-transform: translateX(-100%) scale(.7); }
	30%, 40% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(0) scale(1); }
}
@-moz-keyframes flowinfromleft {
    0% { -moz-transform: translateX(-100%) scale(.7); }
	30%, 40% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform: translateX(0) scale(1); }
}
@keyframes flowinfromleft {
    0% { transform: translateX(-100%) scale(.7); }
	30%, 40% { transform: translateX(0) scale(.7); }
    100% { transform: translateX(0) scale(1); }
}
@-webkit-keyframes flowinfromright {
    0% { -webkit-transform: translateX(100%) scale(.7); }
	30%, 40% { -webkit-transform: translateX(0) scale(.7); }
    100% { -webkit-transform: translateX(0) scale(1); }
}
@-moz-keyframes flowinfromright {
    0% { -moz-transform: translateX(100%) scale(.7); }
	30%, 40% { -moz-transform: translateX(0) scale(.7); }
    100% { -moz-transform: translateX(0) scale(1); }
}
@keyframes flowinfromright {
    0% { transform: translateX(100%) scale(.7); }
	30%, 40% { transform: translateX(0) scale(.7); }
    100% { transform: translateX(0) scale(1); }
}
/* content configurations. */
.ui-grid-a, .ui-grid-b, .ui-grid-c, .ui-grid-d { overflow: hidden; }
.ui-block-a, .ui-block-b, .ui-block-c, .ui-block-d, .ui-block-e { margin: 0; padding: 0; border: 0; float: left; min-height: 1px; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
/* grid solo: 100 - single item fallback */
.ui-grid-solo .ui-block-a { display: block; float: none; }
/* Lower percentages for older browsers (i.e. IE7) to prevent wrapping. -.5px to fix BB5 wrap issue. */
/* grid a: 50/50 */
.ui-grid-a .ui-block-a, .ui-grid-a .ui-block-b { width: 49.95%; }
.ui-grid-a > :nth-child(n) { width: 50%; margin-right: -.5px; }
.ui-grid-a .ui-block-a { clear: left; }
/* grid b: 33/33/33 */
.ui-grid-b .ui-block-a, .ui-grid-b .ui-block-b, .ui-grid-b .ui-block-c { width: 33.25%; }
.ui-grid-b > :nth-child(n) { width: 33.333%; margin-right: -.5px; }
.ui-grid-b .ui-block-a { clear: left; }
/* grid c: 25/25/25/25 */
.ui-grid-c .ui-block-a, .ui-grid-c .ui-block-b, .ui-grid-c .ui-block-c, .ui-grid-c .ui-block-d { width: 24.925%; }
.ui-grid-c > :nth-child(n) { width: 25%; margin-right: -.5px; }
.ui-grid-c .ui-block-a { clear: left; }
/* grid d: 20/20/20/20/20 */
.ui-grid-d .ui-block-a, .ui-grid-d .ui-block-b, .ui-grid-d .ui-block-c, .ui-grid-d .ui-block-d, .ui-grid-d .ui-block-e { width: 19.925%; }
.ui-grid-d > :nth-child(n) { width: 20%; }
.ui-grid-d .ui-block-a { clear: left; }
/* preset breakpoint to switch to stacked grid styles below 35em (560px) */
@media all and (max-width: 35em) {
	.ui-responsive .ui-block-a, 
	.ui-responsive .ui-block-b, 
	.ui-responsive .ui-block-c,
	.ui-responsive .ui-block-d,
	.ui-responsive .ui-block-e { 
		width: 100%; 
		float:none; 
	}
}
/* fixed page header & footer configuration */
.ui-header-fixed,
.ui-footer-fixed {
	left: 0;
	right: 0;
	width: 100%;
	position: fixed;
	z-index: 1000;
}
.ui-header-fixed {
	top: -1px;
	padding-top: 1px;
}
.ui-header-fixed.ui-fixed-hidden {
	top: 0;
	padding-top: 0;
}
.ui-footer-fixed {
	bottom: -1px;
	padding-bottom: 1px;
}
.ui-footer-fixed.ui-fixed-hidden {
	bottom: 0;
	padding-bottom: 0;
}
.ui-header-fullscreen,
.ui-footer-fullscreen {
	filter: Alpha(Opacity=90);
	opacity: .9;
}
.ui-page-header-fixed {
	padding-top: 2.6875em;
}
.ui-page-footer-fixed {
	padding-bottom: 2.6875em;
}
.ui-page-header-fullscreen > .ui-content,
.ui-page-footer-fullscreen > .ui-content {
	padding: 0;
}
.ui-fixed-hidden {
	position: absolute;
}
.ui-page-header-fullscreen .ui-fixed-hidden,
.ui-page-footer-fullscreen .ui-fixed-hidden {
	left: -9999px;
}
.ui-header-fixed .ui-btn,
.ui-footer-fixed .ui-btn { 
	z-index: 10;
}
/* workarounds for other widgets */
.ui-android-2x-fixed .ui-li-has-thumb {
	-webkit-transform: translate3d(0,0,0);
}
.ui-navbar { max-width: 100%; }
.ui-navbar.ui-mini { margin: 0; }
.ui-navbar ul:before, .ui-navbar ul:after { content: " "; display: table; }
.ui-navbar ul:after { clear: both; }
.ui-navbar ul { list-style:none; margin: 0; padding: 0; position: relative; display: block; border: 0; max-width: 100%; overflow: visible; zoom: 1; }
.ui-navbar li .ui-btn { display: block; text-align: center; margin: 0 -1px 0 0; border-right-width: 0; }
.ui-navbar li .ui-btn-icon-right .ui-icon { right: 6px; }
/* add border if not in header/footer (full width) */
.ui-navbar li:last-child .ui-btn,
.ui-navbar .ui-grid-duo .ui-block-b .ui-btn { margin-right: 0; border-right-width: 1px; }
.ui-header .ui-navbar li:last-child .ui-btn,
.ui-footer .ui-navbar li:last-child .ui-btn,
.ui-header .ui-navbar .ui-grid-duo .ui-block-b .ui-btn,
.ui-footer .ui-navbar .ui-grid-duo .ui-block-b .ui-btn { margin-right: -1px; border-right-width: 0; }
.ui-navbar .ui-grid-duo li.ui-block-a:last-child .ui-btn { margin-right: -1px; border-right-width: 1px; }
.ui-header .ui-navbar li .ui-btn,
.ui-footer .ui-navbar li .ui-btn { border-top-width: 0; border-bottom-width: 0; }
/* fixing gaps caused by subpixel problem */
.ui-header .ui-navbar .ui-grid-b li.ui-block-c .ui-btn,
.ui-footer .ui-navbar .ui-grid-b li.ui-block-c .ui-btn { margin-right: -5px; }
.ui-header .ui-navbar .ui-grid-c li.ui-block-d .ui-btn,
.ui-footer .ui-navbar .ui-grid-c li.ui-block-d .ui-btn,
.ui-header .ui-navbar .ui-grid-d li.ui-block-e .ui-btn,
.ui-footer .ui-navbar .ui-grid-d li.ui-block-e .ui-btn { margin-right: -4px; }
.ui-header .ui-navbar .ui-grid-b li.ui-block-c .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-b li.ui-block-c .ui-btn-icon-right .ui-icon,
.ui-header .ui-navbar .ui-grid-c li.ui-block-d .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-c li.ui-block-d .ui-btn-icon-right .ui-icon,
.ui-header .ui-navbar .ui-grid-d li.ui-block-e .ui-btn-icon-right .ui-icon,
.ui-footer .ui-navbar .ui-grid-d li.ui-block-e .ui-btn-icon-right .ui-icon { right: 8px; }
.ui-navbar li .ui-btn .ui-btn-inner { padding-top: .7em; padding-bottom: .8em }
.ui-navbar li .ui-btn-icon-top .ui-btn-inner { padding-top: 30px; }
.ui-navbar li .ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 30px; }
.ui-btn { display: block; text-align: center; cursor:pointer; position: relative; margin: .5em 0; padding: 0; }
.ui-mini { margin-top: .25em; margin-bottom: .25em; }
.ui-btn-left, .ui-btn-right, .ui-input-clear, .ui-btn-inline,
.ui-grid-a .ui-btn, .ui-grid-b .ui-btn, .ui-grid-c .ui-btn, .ui-grid-d .ui-btn, .ui-grid-e .ui-btn, .ui-grid-solo .ui-btn { margin-right: 5px; margin-left: 5px; }
.ui-btn-inner { font-size: 16px; padding: .6em 20px; min-width: .75em; display: block; position: relative; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; zoom: 1; }
.ui-btn input, .ui-btn button { z-index: 2; }
.ui-btn-left, .ui-btn-right, .ui-btn-inline { display: inline-block; vertical-align: middle; }
.ui-mobile .ui-btn-left, .ui-mobile .ui-btn-right, .ui-btn-left > .ui-btn, .ui-btn-right > .ui-btn { margin: 0; } /* .ui-mobile to increase specificity level */
.ui-btn-block { display: block; }
.ui-header > .ui-btn,
.ui-footer > .ui-btn { display: inline-block; margin: 0; }
.ui-header .ui-btn-block,
.ui-footer .ui-btn-block { display: block; }
.ui-header .ui-btn-inner,
.ui-footer .ui-btn-inner,
.ui-mini .ui-btn-inner { font-size: 12.5px; padding: .55em 11px .5em; }
.ui-fullsize .ui-btn-inner,
.ui-fullsize .ui-btn-inner { font-size: 16px; padding: .6em 20px; }
.ui-btn-icon-notext { width: 24px; height: 24px; }
.ui-btn-icon-notext .ui-btn-inner { padding: 0; height: 100%; }
.ui-btn-icon-notext .ui-btn-inner .ui-icon { margin: 2px 1px 2px 3px; float: left; }
.ui-btn-text { position: relative; z-index: 1; width: 100%; -moz-user-select: none; -webkit-user-select: none; -ms-user-select: none; }
div.ui-btn-text { width: auto; }
.ui-btn-icon-notext .ui-btn-text { position: absolute; left: -9999px; }
.ui-btn-icon-left .ui-btn-inner { padding-left: 40px; }
.ui-btn-icon-right .ui-btn-inner { padding-right: 40px; }
.ui-btn-icon-top .ui-btn-inner { padding-top: 40px; }
.ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 40px; }
.ui-header .ui-btn-icon-left .ui-btn-inner,
.ui-footer .ui-btn-icon-left .ui-btn-inner,
.ui-mini.ui-btn-icon-left .ui-btn-inner,
.ui-mini .ui-btn-icon-left .ui-btn-inner { padding-left: 30px; }
.ui-header .ui-btn-icon-right .ui-btn-inner,
.ui-footer .ui-btn-icon-right .ui-btn-inner,
.ui-mini.ui-btn-icon-right .ui-btn-inner,
.ui-mini .ui-btn-icon-right .ui-btn-inner { padding-right: 30px; }
.ui-header .ui-btn-icon-top .ui-btn-inner,
.ui-footer .ui-btn-icon-top .ui-btn-inner { padding: 30px 3px .5em 3px; }
.ui-mini.ui-btn-icon-top .ui-btn-inner,
.ui-mini .ui-btn-icon-top .ui-btn-inner { padding-top: 30px; }
.ui-header .ui-btn-icon-bottom .ui-btn-inner,
.ui-footer .ui-btn-icon-bottom .ui-btn-inner { padding: .55em 3px 30px 3px; }
.ui-mini.ui-btn-icon-bottom .ui-btn-inner,
.ui-mini .ui-btn-icon-bottom .ui-btn-inner { padding-bottom: 30px; }
/* Corner styling inheritance */
.ui-btn-inner {
	-webkit-border-radius: inherit;	
	border-radius: inherit;
}
/*btn icon positioning*/
.ui-btn-icon-notext .ui-icon { display: block; z-index: 0;}
.ui-btn-icon-left > .ui-btn-inner > .ui-icon, .ui-btn-icon-right > .ui-btn-inner > .ui-icon { position: absolute; top: 50%; margin-top: -9px; }
.ui-btn-icon-top .ui-btn-inner .ui-icon, .ui-btn-icon-bottom .ui-btn-inner .ui-icon { position: absolute; left: 50%; margin-left: -9px; }
.ui-btn-icon-left .ui-icon { left: 10px; }
.ui-btn-icon-right .ui-icon { right: 10px; }
.ui-btn-icon-top .ui-icon { top: 10px; }
.ui-btn-icon-bottom .ui-icon { top: auto; bottom: 10px; }
.ui-header .ui-btn-icon-left .ui-icon,
.ui-footer .ui-btn-icon-left .ui-icon,
.ui-mini.ui-btn-icon-left .ui-icon,
.ui-mini .ui-btn-icon-left .ui-icon { left: 5px; }
.ui-header .ui-btn-icon-right .ui-icon,
.ui-footer .ui-btn-icon-right .ui-icon,
.ui-mini.ui-btn-icon-right .ui-icon,
.ui-mini .ui-btn-icon-right .ui-icon { right: 5px; }
.ui-header .ui-btn-icon-top .ui-icon,
.ui-footer .ui-btn-icon-top .ui-icon,
.ui-mini.ui-btn-icon-top .ui-icon,
.ui-mini .ui-btn-icon-top .ui-icon { top: 5px; }
.ui-header .ui-btn-icon-bottom .ui-icon,
.ui-footer .ui-btn-icon-bottom .ui-icon,
.ui-mini.ui-btn-icon-bottom .ui-icon,
.ui-mini .ui-btn-icon-bottom .ui-icon { bottom: 5px; }
/*hiding native button,inputs */
.ui-btn-hidden { position: absolute; top: 0; left: 0; width: 100%; height: 100%; -webkit-appearance: none; cursor: pointer; background: #fff; background: rgba(255,255,255,0); filter: Alpha(Opacity=0); opacity: .1; font-size: 1px; border: none; text-indent: -9999px; }
/* Fixes IE/WP filter alpha opacity bugs */
.ui-disabled .ui-btn-hidden { display: none; }
.ui-disabled { z-index: 1; }
.ui-field-contain .ui-btn.ui-submit { margin: 0; }
label.ui-submit { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .3em; display: block; }
@media all and (min-width: 28em){
	.ui-field-contain label.ui-submit { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-btn.ui-submit { width: 78%; display: inline-block; -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
	.ui-hide-label .ui-btn.ui-submit { width: auto; display: block; }
}
.ui-collapsible-inset { margin: .5em 0; }
.ui-collapsible-heading { font-size: 16px; display: block; margin: 0 -15px; padding: 0; position: relative; }
.ui-collapsible-inset .ui-collapsible-heading { margin: 0; }
.ui-collapsible-heading .ui-btn { text-align: left; margin: 0; border-left-width: 0; border-right-width: 0; }
.ui-collapsible-inset .ui-collapsible-heading .ui-btn { border-right-width: 1px; border-left-width: 1px; }
.ui-collapsible-collapsed + .ui-collapsible:not(.ui-collapsible-inset) .ui-collapsible-heading .ui-btn { border-top-width: 0; }
.ui-collapsible-set .ui-collapsible:not(.ui-collapsible-inset) .ui-collapsible-heading .ui-btn { border-top-width: 1px; }
.ui-collapsible-heading .ui-btn-inner { padding-left: 12px; padding-right: 12px; }
.ui-collapsible-heading .ui-btn-icon-left .ui-btn-inner { padding-left: 40px; }
.ui-collapsible-heading .ui-btn-icon-right .ui-btn-inner { padding-right: 40px; }
.ui-collapsible-heading .ui-btn-icon-top .ui-btn-inner,
.ui-collapsible-heading .ui-btn-icon-bottom .ui-btn-inner { text-align: center; }
.ui-collapsible-heading .ui-btn-icon-left.ui-mini .ui-btn-inner { padding-left: 30px; }
.ui-collapsible-heading .ui-btn-icon-right.ui-mini .ui-btn-inner { padding-right: 30px; }
.ui-collapsible-heading .ui-btn span.ui-btn { position: absolute; left: 6px; top: 50%; margin: -12px 0 0 0; width: 20px; height: 20px; padding: 1px 0 1px 2px; text-indent: -9999px; }
.ui-collapsible-heading .ui-btn span.ui-btn .ui-btn-inner { padding: 10px 0; }
.ui-collapsible-heading .ui-btn span.ui-btn .ui-icon { left: 0; margin-top: -10px; }
.ui-collapsible-heading-status { position: absolute; top: -9999px; left: 0; }
.ui-collapsible-content {
	display: block;
	margin: 0 -15px;	
	padding: 10px 15px;
	border-left-width: 0;
	border-right-width: 0;
	border-top: none;      /* Overrides ui-body-* */
	background-image: none; /* Overrides ui-body-* */
}
.ui-collapsible-inset .ui-collapsible-content { margin: 0; border-right-width: 1px; border-left-width: 1px; }
.ui-collapsible-content-collapsed { display: none; }
.ui-collapsible-set > .ui-collapsible.ui-corner-all {
	-webkit-border-radius: 0;
	border-radius: 0;
}
.ui-collapsible-heading,
.ui-collapsible-heading > .ui-btn {
	-webkit-border-radius: inherit;	
	border-radius: inherit;	
}
.ui-collapsible-set .ui-collapsible.ui-first-child {
	-webkit-border-top-right-radius: inherit;	
	border-top-right-radius: inherit;
	-webkit-border-top-left-radius: inherit;	
	border-top-left-radius: inherit;		
}
.ui-collapsible-content,
.ui-collapsible-set .ui-collapsible.ui-last-child {
	-webkit-border-bottom-right-radius: inherit;	
	border-bottom-right-radius: inherit;
	-webkit-border-bottom-left-radius: inherit;	
	border-bottom-left-radius: inherit;		
}
.ui-collapsible-themed-content:not(.ui-collapsible-collapsed) > .ui-collapsible-heading {
	-webkit-border-bottom-right-radius: 0;	
	border-bottom-right-radius: 0;
	-webkit-border-bottom-left-radius: 0;	
	border-bottom-left-radius: 0;		
}
.ui-collapsible-set { margin: .5em 0; }
.ui-collapsible-set .ui-collapsible { margin: -1px 0 0; }
.ui-collapsible-set .ui-collapsible.ui-first-child { margin-top: 0; }
.ui-controlgroup, fieldset.ui-controlgroup { padding: 0; margin: .5em 0; zoom: 1; }
.ui-controlgroup.ui-mini, fieldset.ui-controlgroup.ui-mini { margin: .25em 0; }
.ui-field-contain .ui-controlgroup, .ui-field-contain fieldset.ui-controlgroup { margin: 0; }
.ui-bar .ui-controlgroup { margin: 0 5px; }
.ui-controlgroup-label { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .4em; }
.ui-controlgroup-controls label.ui-select,
.ui-controlgroup-controls label.ui-submit { position: absolute; left: -9999px; }
.ui-controlgroup li { list-style: none; }
.ui-controlgroup .ui-btn { margin: 0; }
.ui-controlgroup .ui-btn-icon-notext { width: auto; height: auto; top: auto; }
.ui-controlgroup .ui-btn-icon-notext .ui-btn-inner { height: 20px; padding: .6em 20px .6em 20px }
.ui-controlgroup-horizontal .ui-btn-icon-notext .ui-btn-inner { width: 18px; }
.ui-controlgroup.ui-mini .ui-btn-icon-notext .ui-btn-inner,
.ui-header .ui-controlgroup .ui-btn-icon-notext .ui-btn-inner,
.ui-footer .ui-controlgroup .ui-btn-icon-notext .ui-btn-inner { height: 16px; padding: .55em 11px .5em 11px; }
.ui-controlgroup .ui-btn-icon-notext .ui-btn-inner .ui-icon { position: absolute; top: 50%; right: 50%; margin: -9px -9px 0 0; }
.ui-controlgroup-horizontal .ui-btn-inner { text-align: center; }
.ui-controlgroup-horizontal.ui-mini .ui-btn-inner { height: 16px; line-height: 16px; }
.ui-controlgroup .ui-checkbox label, .ui-controlgroup .ui-radio label { font-size: 16px; }
.ui-controlgroup-horizontal .ui-controlgroup-controls:before,
.ui-controlgroup-horizontal .ui-controlgroup-controls:after { content: ""; display: table; }
.ui-controlgroup-horizontal .ui-controlgroup-controls:after { clear: both; }
.ui-controlgroup-horizontal .ui-controlgroup-controls { display: inline-block; vertical-align: middle; zoom: 1; }
.ui-controlgroup-horizontal .ui-controlgroup-controls > .ui-btn, .ui-controlgroup-horizontal .ui-controlgroup-controls li > .ui-btn,
.ui-controlgroup-horizontal .ui-checkbox, .ui-controlgroup-horizontal .ui-radio,
.ui-controlgroup-horizontal .ui-select { float: left; clear: none; margin: 0; }
/* On IE7 the floating selects will be displayed as block if .ui-btn-text has width 100% */
.ui-controlgroup-horizontal .ui-select .ui-btn-text { width: auto; }
.ui-controlgroup-vertical .ui-btn {	border-bottom-width: 0; }
.ui-controlgroup-vertical .ui-btn.ui-last-child { border-bottom-width: 1px; }
.ui-controlgroup-horizontal .ui-btn { border-right-width: 0; }
.ui-controlgroup-horizontal .ui-btn.ui-last-child {	border-right-width: 1px; }
.ui-controlgroup .ui-btn-corner-all {
	-webkit-border-radius: 0;
	border-radius: 0;
}
.ui-controlgroup .ui-controlgroup-controls,
.ui-controlgroup .ui-radio,
.ui-controlgroup .ui-checkbox,
.ui-controlgroup .ui-select,
.ui-controlgroup li {
	-webkit-border-radius: inherit;
	border-radius: inherit;
}
.ui-controlgroup-vertical .ui-btn.ui-first-child {
	-webkit-border-top-left-radius: inherit;
	border-top-left-radius: inherit;
	-webkit-border-top-right-radius: inherit;
	border-top-right-radius: inherit;
}
.ui-controlgroup-vertical .ui-btn.ui-last-child {
	-webkit-border-bottom-left-radius: inherit;
	border-bottom-left-radius: inherit;
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius: inherit;
}
.ui-controlgroup-horizontal .ui-btn.ui-first-child {
	-webkit-border-top-left-radius: inherit;
	border-top-left-radius: inherit;
	-webkit-border-bottom-left-radius: inherit;
	border-bottom-left-radius: inherit;
}
.ui-controlgroup-horizontal .ui-btn.ui-last-child {
	-webkit-border-top-right-radius: inherit;
	border-top-right-radius: inherit;
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius: inherit;
}
.ui-controlgroup .ui-shadow:not(.ui-focus) {
	-moz-box-shadow: none;
	-webkit-box-shadow: none;
	box-shadow: none;
}
@media all and (min-width: 28em){
	.ui-field-contain .ui-controlgroup-label { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-controlgroup-controls { width: 78%; display: inline-block; }
	.ui-field-contain .ui-controlgroup .ui-select { width: 100%; display: block; } 
	.ui-field-contain .ui-controlgroup-horizontal .ui-select { width: auto; }
	.ui-hide-label .ui-controlgroup-controls { width: 100%; }
}	
.ui-dialog {
	 background: none !important; /* this is to ensure that dialog theming does not apply (by default at least) on the page div */
}
.ui-dialog-contain {
	width: 92.5%;
	max-width: 500px;
	margin: 10% auto 15px auto;
	padding: 0;
	position: relative;
	top: -15px;
}
.ui-dialog-contain > .ui-header, 
.ui-dialog-contain > .ui-content, 
.ui-dialog-contain > .ui-footer { 
	display: block;
	position: relative; 
	width: auto;
	margin: 0;
}
.ui-dialog-contain > .ui-header {
	border: none;
	overflow: hidden;
	z-index: 10; 
	padding: 0;
}
.ui-dialog-contain > .ui-content { 
	padding: 15px; 
}
.ui-dialog-contain > .ui-footer {
	z-index: 10; 
	padding: 0 15px; 
}
.ui-popup-open .ui-header-fixed,
.ui-popup-open .ui-footer-fixed {
	position: absolute !important; 	/* See line #553 of popup.js */
}
.ui-popup-screen {
	background-image: url(data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==); /* Necessary to set some form of background to ensure element is clickable in IE6/7. While legacy IE won't understand the data-URI'd image, it ensures no additional requests occur in all other browsers with little overhead. */
	top: 0;
	left: 0;
	right: 0;
	bottom: 1px;
	position: absolute;
	filter: Alpha(Opacity=0);
	opacity: 0;
	z-index: 1099;
}
.ui-popup-screen.in {
	opacity: 0.5;
	filter: Alpha(Opacity=50);
}
.ui-popup-screen.out {
	opacity: 0;
	filter: Alpha(Opacity=0);
}
.ui-popup-container {
	z-index: 1100;
	display: inline-block;
	position: absolute;
	padding: 0;
	outline: 0;
}
.ui-popup {
	position: relative;
}
.ui-popup.ui-content,
.ui-popup .ui-content {
	overflow: visible;
}
.ui-popup > p,
.ui-popup > h1,
.ui-popup > h2,
.ui-popup > h3,
.ui-popup > h4,
.ui-popup > h5,
.ui-popup > h6 {
	margin: .5em 7px;
}
.ui-popup > span {
	display: block;
	margin: .5em 7px;
}
.ui-popup .ui-title {
	font-size: 16px;
	font-weight: bold;
	margin-top: .5em;
	margin-bottom: .5em;
}
.ui-popup-container .ui-content > p,
.ui-popup-container .ui-content > h1,
.ui-popup-container .ui-content > h2,
.ui-popup-container .ui-content > h3,
.ui-popup-container .ui-content > h4,
.ui-popup-container .ui-content > h5,
.ui-popup-container .ui-content > h6 {
	margin: .5em 0;
}
.ui-popup-container .ui-content > span {
	margin: 0;
}
.ui-popup-container .ui-content > p:first-child,
.ui-popup-container .ui-content > h1:first-child,
.ui-popup-container .ui-content > h2:first-child,
.ui-popup-container .ui-content > h3:first-child,
.ui-popup-container .ui-content > h4:first-child,
.ui-popup-container .ui-content > h5:first-child,
.ui-popup-container .ui-content > h6:first-child {
	margin-top: 0;
}
.ui-popup-container .ui-content > p:last-child,
.ui-popup-container .ui-content > h1:last-child,
.ui-popup-container .ui-content > h2:last-child,
.ui-popup-container .ui-content > h3:last-child,
.ui-popup-container .ui-content > h4:last-child,
.ui-popup-container .ui-content > h5:last-child,
.ui-popup-container .ui-content > h6:last-child {
	margin-bottom: 0;
}
.ui-popup > img {
	width: auto;
	height: auto;
	max-width: 100%;
	max-height: 100%;
	vertical-align: middle;
}
.ui-popup:not(.ui-content) > img:only-child,
.ui-popup:not(.ui-content) > .ui-btn-left:first-child + img:last-child,
.ui-popup:not(.ui-content) > .ui-btn-right:first-child + img:last-child {
	-webkit-border-radius: inherit;
	border-radius: inherit;
}
.ui-popup iframe {
	vertical-align: middle;
}
@media all and (min-width: 28em){
	.ui-popup .ui-field-contain label.ui-submit,
	.ui-popup .ui-field-contain .ui-controlgroup-label,
	.ui-popup .ui-field-contain label.ui-select,
	.ui-popup .ui-field-contain label.ui-input-text {
		font-size: 16px; line-height: 1.4; display: block; font-weight: normal; margin: 0 0 .3em;
	}
	.ui-popup .ui-field-contain .ui-btn.ui-submit,
	.ui-popup .ui-field-contain .ui-controlgroup-controls,
	.ui-popup .ui-field-contain .ui-select,
	.ui-popup .ui-field-contain input.ui-input-text,
	.ui-popup .ui-field-contain textarea.ui-input-text,
	.ui-popup .ui-field-contain .ui-input-search {
		width: 100%; display: block;
	}
}
.ui-popup > .ui-btn-left,
.ui-popup > .ui-btn-right {
	position: absolute; 
	top: -9px;
	margin: 0;
	z-index: 1101;
}
.ui-popup > .ui-btn-left { left: -9px; }
.ui-popup > .ui-btn-right { right: -9px; }
.ui-popup-hidden { top: -99999px; left: -9999px; }
.ui-checkbox, .ui-radio { position: relative; clear: both; margin: 0; z-index: 1; }
.ui-checkbox .ui-btn, .ui-radio .ui-btn { text-align: left; z-index: 2; }
.ui-controlgroup .ui-checkbox .ui-btn, .ui-controlgroup .ui-radio .ui-btn { margin: 0; }
.ui-checkbox .ui-btn-inner, .ui-radio .ui-btn-inner { white-space: normal; }
.ui-checkbox .ui-btn-icon-left .ui-btn-inner,.ui-radio .ui-btn-icon-left .ui-btn-inner { padding-left: 45px; }
.ui-checkbox .ui-mini.ui-btn-icon-left .ui-btn-inner,.ui-radio .ui-mini.ui-btn-icon-left .ui-btn-inner { padding-left: 36px; }
.ui-checkbox .ui-btn-icon-right .ui-btn-inner, .ui-radio .ui-btn-icon-right .ui-btn-inner { padding-right: 45px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-btn-inner, .ui-radio .ui-mini.ui-btn-icon-right .ui-btn-inner { padding-right: 36px; }
.ui-checkbox .ui-btn-icon-top .ui-btn-inner, .ui-radio .ui-btn-icon-top .ui-btn-inner { padding-right: 0; padding-left: 0; text-align: center; }
.ui-checkbox .ui-btn-icon-bottom .ui-btn-inner, .ui-radio .ui-btn-icon-bottom .ui-btn-inner { padding-right: 0; padding-left: 0; text-align: center; }
.ui-checkbox .ui-icon, .ui-radio .ui-icon { top: 1.1em; }
.ui-checkbox .ui-btn-icon-left .ui-icon, .ui-radio .ui-btn-icon-left .ui-icon { left: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-left .ui-icon, .ui-radio .ui-mini.ui-btn-icon-left .ui-icon { left: 9px; }
.ui-checkbox .ui-btn-icon-right .ui-icon, .ui-radio .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-icon, .ui-radio .ui-mini.ui-btn-icon-right .ui-icon { right: 9px; }
.ui-checkbox .ui-btn-icon-top .ui-icon, .ui-radio .ui-btn-icon-top .ui-icon { top: 10px; }
.ui-checkbox .ui-btn-icon-bottom .ui-icon, .ui-radio .ui-btn-icon-bottom .ui-icon { top: auto; bottom: 10px; }
.ui-checkbox .ui-btn-icon-right .ui-icon, .ui-radio .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-checkbox .ui-mini.ui-btn-icon-right .ui-icon, .ui-radio .ui-mini.ui-btn-icon-right .ui-icon { right: 9px; }
.ui-controlgroup-horizontal .ui-checkbox .ui-icon,
.ui-controlgroup-horizontal .ui-radio .ui-icon { display: none; }
.ui-controlgroup-horizontal .ui-checkbox .ui-btn-inner,
.ui-controlgroup-horizontal .ui-radio .ui-btn-inner { padding: .6em 20px; }
.ui-controlgroup-horizontal .ui-checkbox .ui-mini .ui-btn-inner,
.ui-controlgroup-horizontal .ui-radio .ui-mini .ui-btn-inner { padding: .55em 11px .5em; }
/* input, label positioning */
.ui-checkbox input,.ui-radio input { position:absolute; left:20px; top:50%; width: 10px; height: 10px; margin:-5px 0 0 0; outline: 0 !important; z-index: 1; }
.ui-field-contain, fieldset.ui-field-contain { padding: .8em 0; margin: 0; border-width: 0 0 1px 0; overflow: visible; }
.ui-field-contain:last-child { border-bottom-width: 0; }
.ui-field-contain { max-width: 100%; } /* This prevents horizontal scrollbar in IE7 */
@media all and (min-width: 28em){
	.ui-field-contain, .ui-mobile fieldset.ui-field-contain { border-width: 0; padding: 0; margin: 1em 0; }
}
.ui-select { display: block; position: relative; }
.ui-select select { position: absolute; left: -9999px; top: -9999px; }
.ui-select .ui-btn { opacity: 1; }
.ui-field-contain .ui-select .ui-btn { margin: 0; }
/* Fixes #2588: When Windows Phone 7.5 (Mango) tries to calculate a numeric opacity for a select (including "inherit") without explicitly specifying an opacity on the parent to give it context, a bug appears where clicking elsewhere on the page after opening the select will open the select again. */
.ui-select .ui-btn select { cursor: pointer; -webkit-appearance: none; left: 0; top:0; width: 100%; min-height: 1.5em; min-height: 100%; height: 3em; max-height: 100%; filter: Alpha(Opacity=0); opacity: 0; z-index: 2; }
.ui-select .ui-disabled { opacity: .3; }
/* Display none because of issues with IE/WP's filter alpha opacity */
.ui-select .ui-disabled select { display: none; }
@-moz-document url-prefix() { .ui-select .ui-btn select { opacity: 0.0001; }}
.ui-select .ui-btn.ui-select-nativeonly { border-radius: 0; border: 0; }
.ui-select .ui-btn.ui-select-nativeonly select { opacity: 1; text-indent: 0; display: block; }
.ui-select .ui-disabled.ui-select-nativeonly .ui-btn-inner { opacity: 0; }
.ui-select .ui-btn-icon-right .ui-btn-inner, .ui-select .ui-li-has-count .ui-btn-inner { padding-right: 45px; }
.ui-select .ui-mini.ui-btn-icon-right .ui-btn-inner { padding-right: 32px; }
.ui-select .ui-btn-icon-right.ui-li-has-count .ui-btn-inner { padding-right: 80px; }
.ui-select .ui-mini.ui-btn-icon-right.ui-li-has-count .ui-btn-inner { padding-right: 67px; }
.ui-select .ui-btn-icon-right .ui-icon { right: 15px; }
.ui-select .ui-mini.ui-btn-icon-right .ui-icon { right: 7px; }
.ui-select .ui-btn-icon-right.ui-li-has-count .ui-li-count { right: 45px; }
.ui-select .ui-mini.ui-btn-icon-right.ui-li-has-count .ui-li-count { right: 32px; }
/* labels */
label.ui-select { font-size: 16px; line-height: 1.4; font-weight: normal; margin: 0 0 .3em; display: block; }
/*listbox*/
.ui-select .ui-btn-text, .ui-selectmenu .ui-btn-text { display: block; min-height: 1em; overflow: hidden !important;
/* This !important is required for iPad Safari specifically. See https://github.com/jquery/jquery-mobile/issues/2647 */ }
.ui-select .ui-btn-text { text-overflow: ellipsis; }
.ui-selectmenu { padding: 6px; min-width: 160px; }
.ui-selectmenu .ui-listview { margin: 0; }
.ui-selectmenu .ui-btn.ui-li-divider { cursor: default; }
.ui-screen-hidden, .ui-selectmenu-list .ui-li .ui-icon { display: none; }
.ui-selectmenu-list .ui-li .ui-icon { display: block; }
.ui-li.ui-selectmenu-placeholder { display: none; }
.ui-selectmenu .ui-header { margin: 0; padding: 0; }
.ui-selectmenu.ui-popup .ui-header { -webkit-border-top-left-radius: 0; border-top-left-radius: 0; -webkit-border-top-right-radius: 0; border-top-right-radius: 0; }
.ui-selectmenu .ui-header .ui-title { margin: 0.6em 46px 0.8em; }
@media all and (min-width: 28em){
	.ui-field-contain label.ui-select { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0; }
	.ui-field-contain .ui-select { width: 78%; display: inline-block; }
	.ui-hide-label .ui-select { width: 100%; } 
}
/* when no placeholder is defined in a multiple select, the header height doesn't even extend past the close button.  this shim's content in there */
.ui-selectmenu .ui-header h1:after { content: '.'; visibility: hidden; }
label.ui-input-text { font-size: 16px; line-height: 1.4; display: block; font-weight: normal; margin: 0 0 .3em; }
input.ui-input-text, textarea.ui-input-text { background-image: none; padding: .4em; margin: .5em 0; min-height: 1.4em; line-height: 1.4em; font-size: 16px; display: block; width: 100%; outline: 0; }
input.ui-mini, .ui-mini input, textarea.ui-mini { font-size: 14px; }
div.ui-input-text input.ui-input-text, div.ui-input-text textarea.ui-input-text,
.ui-input-search input.ui-input-text { border: none; width: 100%; padding: .4em 0; margin: 0; display: block; background: transparent none; outline: 0 !important; }
.ui-input-search, div.ui-input-text { margin: .5em 0; background-image: none; position: relative; }
.ui-input-search { padding: 0 30px; }
div.ui-input-text { padding: 0 .4em; }
div.ui-input-has-clear { padding: 0 30px 0 .4em; }
input.ui-input-text.ui-mini, textarea.ui-input-text.ui-mini,
.ui-input-search.ui-mini, div.ui-input-text.ui-mini { margin: .25em 0; }
.ui-field-contain input.ui-input-text, .ui-field-contain textarea.ui-input-text,
.ui-field-contain .ui-input-search, .ui-field-contain div.ui-input-text { margin: 0; }
textarea.ui-input-text { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
input.ui-input-text { -webkit-appearance: none; }
textarea.ui-input-text { height: 50px; -webkit-transition: height 200ms linear; -moz-transition: height 200ms linear; -o-transition: height 200ms linear; transition: height 200ms linear; }
textarea.ui-mini { height: 45px; }
.ui-icon-searchfield:after { position: absolute; left: 7px; top: 50%; margin-top: -9px; content: ""; width: 18px; height: 18px; opacity: .5; }
.ui-input-search .ui-input-clear, .ui-input-text .ui-input-clear { position: absolute; right: 0; top: 50%; margin-top: -13px; }
.ui-mini .ui-input-clear { right: -3px; }
.ui-input-search .ui-input-clear-hidden, .ui-input-text .ui-input-clear-hidden { display: none; }
/* Resolves issue #5166: Added to support issue introduced in Firefox 15. We can likely remove this in the future. */
input::-moz-placeholder, textarea::-moz-placeholder { color: #aaa; }
/* Resolves issue #5131: Width of textinput depends on its type, for Android 4.1 */
input[type=number]::-webkit-outer-spin-button { margin: 0; }
@media all and (min-width: 28em){
	.ui-field-contain label.ui-input-text { vertical-align: top; display: inline-block; width: 20%; margin: 0 2% 0 0 }
	.ui-field-contain input.ui-input-text,
	.ui-field-contain textarea.ui-input-text,
	.ui-field-contain .ui-input-search,
	.ui-field-contain div.ui-input-text { width: 78%; display: inline-block; }
	.ui-field-contain .ui-input-search,
	.ui-field-contain div.ui-input-text { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; -ms-box-sizing: border-box; box-sizing: border-box; }
	.ui-hide-label input.ui-input-text,
	.ui-hide-label textarea.ui-input-text,
	.ui-hide-label .ui-input-search,
	.ui-hide-label div.ui-input-text,
	.ui-input-search input.ui-input-text,
	div.ui-input-text input.ui-input-text { width: 100%; }
}
.ui-rangeslider {
	zoom: 1;
	margin: 0;
}
.ui-rangeslider:before,
.ui-rangeslider:after {
	content: "";
	display: table;
}
.ui-rangeslider:after {
	clear: both;
}
/* Margin-top/bottom: .5em * 16px/14px to make it equal to ui-rangeslider-sliders margin (input font-size is 14px) */
.ui-rangeslider input.ui-input-text.ui-slider-input {
	margin: .57143em 0;
}
.ui-rangeslider.ui-mini input.ui-slider-input {
	margin: .28571em 0;
}
.ui-rangeslider input.ui-slider-input.ui-rangeslider-last {
	float: right;
}
.ui-rangeslider .ui-rangeslider-sliders {
	position: relative;
	overflow: visible;
	height: 30px;
	margin: .5em 68px;
}
.ui-rangeslider.ui-mini .ui-rangeslider-sliders {
	margin: .25em 68px;
}
.ui-field-contain .ui-rangeslider input.ui-slider-input,
.ui-field-contain .ui-rangeslider.ui-mini input.ui-slider-input,
.ui-field-contain .ui-rangeslider .ui-rangeslider-sliders,
.ui-field-contain .ui-rangeslider.ui-mini .ui-rangeslider-sliders {
	margin-top: 0;
	margin-bottom: 0;
}
.ui-rangeslider .ui-rangeslider-sliders .ui-slider-track {
	position: absolute;
	top: 6px;
	right: 0;
	left: 0;
	margin: 0;
}
.ui-rangeslider.ui-mini .ui-rangeslider-sliders .ui-slider-track {
	top: 8px;
}
.ui-rangeslider .ui-slider-track:first-child .ui-slider-bg {
	display: none;
}
.ui-rangeslider .ui-rangeslider-sliders .ui-slider-track:first-child {
	background-color: transparent;
	background: none;
	border-width: 0;
	height: 0;
}
/* this makes ie6 and ie7 set height to 0 to fix z-index problem */
html >/**/body .ui-rangeslider .ui-rangeslider-sliders .ui-slider-track:first-child {
	height: 15px;
	border-width: 1px;
}
html >/**/body .ui-rangeslider.ui-mini .ui-rangeslider-sliders .ui-slider-track:first-child {
	height: 12px;
}
@media all and (min-width: 28em){
	.ui-field-contain .ui-rangeslider label.ui-slider {
		float: left;
	}
	.ui-field-contain .ui-rangeslider input.ui-slider-input {
		position: relative;
		z-index: 1;
	}
	.ui-field-contain .ui-rangeslider input.ui-slider-input.ui-rangeslider-first,
	.ui-field-contain .ui-rangeslider.ui-mini input.ui-slider-input.ui-rangeslider-first {
		margin-right: 17px;
	}
	.ui-field-contain .ui-rangeslider .ui-rangeslider-sliders,
	.ui-field-contain .ui-rangeslider.ui-mini .ui-rangeslider-sliders {
		float: left;
		width: 78%;
		margin: 0 -68px;
	}
	.ui-field-contain .ui-rangeslider .ui-slider-track,
	.ui-field-contain .ui-rangeslider.ui-mini .ui-slider-track {
		right: 68px;
		left: 68px;
	}
	.ui-field-contain.ui-hide-label .ui-rangeslider input.ui-slider-input.ui-rangeslider-first {
		margin: 0;
	}
	.ui-field-contain.ui-hide-label .ui-rangeslider .ui-rangeslider-sliders,
	.ui-field-contain.ui-hide-label .ui-rangeslider.ui-mini .ui-rangeslider-sliders {
		width: auto;
		float: none;
		margin: 0 68px;
	}
	.ui-field-contain.ui-hide-label .ui-rangeslider .ui-slider-track,
	.ui-field-contain.ui-hide-label .ui-rangeslider.ui-mini .ui-slider-track {
		right: 0;
		left: 0;
	}
}
.ui-listview { margin: 0; }
ol.ui-listview, ol.ui-listview .ui-li-divider { counter-reset: listnumbering; }
.ui-content .ui-listview, .ui-panel-inner > .ui-listview { margin: -15px; }
.ui-collapsible-content > .ui-listview { margin: -10px -15px; }
.ui-content .ui-listview-inset, .ui-panel-inner .ui-listview-inset { margin: 1em 0; }
.ui-collapsible-content .ui-listview-inset { margin: .5em 0; }
.ui-listview, .ui-li { list-style: none; padding: 0; }
.ui-li, .ui-li.ui-field-contain { display: block; margin: 0; position: relative; overflow: visible; text-align: left; border-width: 0; border-top-width: 1px; }
.ui-li.ui-btn, .ui-li.ui-field-contain, .ui-li-divider, .ui-li-static { margin: 0; }
.ui-listview-inset .ui-li { border-right-width: 1px; border-left-width: 1px; }
.ui-li.ui-last-child, .ui-li.ui-field-contain.ui-last-child { border-bottom-width: 1px; }
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset) > .ui-li.ui-first-child { border-top-width: 0; }
.ui-collapsible-themed-content .ui-listview:not(.ui-listview-inset) > .ui-li.ui-last-child { border-bottom-width: 0; }
.ui-li .ui-btn-text a.ui-link-inherit { text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
.ui-li-static { background-image: none; }
.ui-li-divider { padding: .5em 15px; font-size: 14px; font-weight: bold; }
ol.ui-listview .ui-link-inherit:before, ol.ui-listview .ui-li-static:before, .ui-li-dec { font-size: .8em; display: inline-block; padding-right: .3em; font-weight: normal; counter-increment: listnumbering; content: counter(listnumbering) ". "; }
ol.ui-listview .ui-li-jsnumbering:before { content: "" !important; } /* to avoid chance of duplication */
.ui-listview .ui-li > .ui-btn-text {
	-webkit-border-radius: inherit;	
	border-radius: inherit;
}
.ui-listview > .ui-li.ui-first-child,
.ui-listview .ui-btn.ui-first-child > .ui-li > .ui-btn-text > .ui-link-inherit {
	-webkit-border-top-right-radius: inherit;	
	border-top-right-radius: inherit;
	-webkit-border-top-left-radius: inherit;
	border-top-left-radius: inherit;
}
.ui-listview > .ui-li.ui-last-child,
.ui-listview .ui-btn.ui-last-child > .ui-li > .ui-btn-text > .ui-link-inherit,
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset),
.ui-collapsible-content > .ui-listview:not(.ui-listview-inset) .ui-li.ui-last-child {
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius: inherit;
	-webkit-border-bottom-left-radius: inherit;
	border-bottom-left-radius: inherit;
}
.ui-listview > .ui-li.ui-first-child .ui-li-link-alt {
	-webkit-border-top-right-radius: inherit;	
	border-top-right-radius: inherit;	
}
.ui-listview > .ui-li.ui-last-child .ui-li-link-alt {
	-webkit-border-bottom-right-radius: inherit;
	border-bottom-right-radius: inherit;	
}
.ui-listview > .ui-li.ui-first-child .ui-li-thumb:not(.ui-li-icon) {
	-webkit-border-top-left-radius: inherit;
	border-top-left-radius: inherit;	
}
.ui-listview > .ui-li.ui-last-child .ui-li-thumb:not(.ui-li-icon) {
	-webkit-border-bottom-left-radius: inherit;
	border-bottom-left-radius: inherit;	
}
.ui-li>.ui-btn-inner { display: block; position: relative; padding: 0; }
.ui-li .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li { padding: .7em 15px; display: block; }
.ui-li-has-thumb .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-thumb  { min-height: 59px; padding-left: 100px; }
.ui-li-has-icon .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-icon { min-height: 20px; padding-left: 40px; }
.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-count, .ui-li-divider.ui-li-has-count { padding-right: 45px; }
.ui-li-has-arrow .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-arrow { padding-right: 40px; }
.ui-li-has-arrow.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-arrow.ui-li-has-count { padding-right: 75px; }
.ui-li-heading { font-size: 16px; font-weight: bold; display: block; margin: .6em 0; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
.ui-li-desc { font-size: 12px; font-weight: normal; display: block; margin: -.5em 0 .6em; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }
ol.ui-listview > .ui-li .ui-li-heading { display: inline-block; width: 100%; margin-left: -1.3em; text-indent: 1.3em; vertical-align: middle; }
ol.ui-listview > .ui-li .ui-li-desc:not(.ui-li-aside) { text-indent: 1.55em; }
.ui-li-thumb, .ui-listview .ui-li-icon { position: absolute; left: 1px; top: 0; max-height: 80px; max-width: 80px; }
.ui-listview .ui-li-icon { max-height: 16px; max-width: 16px; left: 10px; top: .9em; }
.ui-li-thumb, .ui-listview .ui-li-icon, .ui-li-content { float: left; margin-right: 10px; }
.ui-li-aside { float: right; width: 50%; text-align: right; margin: .3em 0; }
@media all and (min-width: 480px){
	 .ui-li-aside { width: 45%; }
}	 
.ui-li-divider { cursor: default; }
.ui-li-has-alt .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-alt { padding-right: 53px; }
.ui-li-has-alt.ui-li-has-count .ui-btn-inner a.ui-link-inherit, .ui-li-static.ui-li-has-alt.ui-li-has-count { padding-right: 88px; }
.ui-li-has-count .ui-li-count { position: absolute; font-size: 11px; font-weight: bold; padding: .2em .5em; top: 50%; margin-top: -.9em; right: 10px; }
.ui-li-has-count.ui-li-divider .ui-li-count, .ui-li-has-count .ui-link-inherit .ui-li-count { margin-top: -.95em; }
.ui-li-has-arrow.ui-li-has-count .ui-li-count { right: 40px; }
.ui-li-has-alt.ui-li-has-count .ui-li-count { right: 53px; }
.ui-li-link-alt { position: absolute; width: 40px; height: 100%; border-width: 0; border-left-width: 1px; top: 0; right: 0; margin: 0; padding: 0; z-index: 2; }
.ui-li-link-alt .ui-btn { overflow: hidden; position: absolute; right: 8px; top: 50%; margin: -13px 0 0 0; border-bottom-width: 1px; z-index: -1;}
.ui-li-link-alt .ui-btn-inner { padding: 0; height: 100%; position: absolute; width: 100%; top: 0; left: 0;}
.ui-li-link-alt .ui-btn .ui-icon { right: 50%; margin-right: -9px; }
.ui-li-link-alt .ui-btn-icon-notext .ui-btn-inner .ui-icon { position: absolute; top: 50%; margin-top: -9px; }
.ui-listview * .ui-btn-inner > .ui-btn > .ui-btn-inner { border-top: 0; }
.ui-listview-filter { border-width: 0; overflow: hidden; margin: -15px -15px 15px -15px; }
.ui-collapsible-content .ui-listview-filter { margin: -10px -15px 10px -15px; border-bottom: inherit; }
.ui-listview-filter-inset { margin: -15px -5px; background: transparent; }
.ui-collapsible-content .ui-listview-filter-inset { margin: -5px; border-bottom-width: 0; }
.ui-listview-filter .ui-input-search { margin: 5px; width: auto; display: block; }
.ui-li.ui-screen-hidden{ display:none; }
/* Odd iPad positioning issue. */
@media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
    .ui-li .ui-btn-text { overflow:  visible; }
}
label.ui-slider {
	font-size: 16px;
	line-height: 1.4;
	font-weight: normal;
	margin: 0;
	display: block;
}
.ui-field-contain label.ui-slider {
	margin-bottom: .4em;
}
div.ui-slider {
	height: 30px;
	margin: .5em 0;
	zoom: 1;
}
div.ui-slider.ui-mini {
	margin: .25em 0;
}
.ui-field-contain div.ui-slider,
.ui-field-contain div.ui-slider.ui-mini {
	margin: 0;
}
div.ui-slider:before, div.ui-slider:after {
	content: "";
	display: table;
}
div.ui-slider:after {
	clear: both;
}
/* High level of specificity to override Textinput CSS. */
input.ui-input-text.ui-slider-input {
	display: block;
	float: left;
	margin: 0;
	padding: 4px;
	width: 40px;
	height: 22px;
	line-height: 22px;
	font-size: 14px;
	border-width: 0;
	background-image: none;
	font-weight: bold;
	text-align: center;
	vertical-align: text-bottom;
	outline: 0;
	-webkit-box-sizing: content-box;
	-moz-box-sizing: content-box;
	-ms-box-sizing: content-box;
	box-sizing: content-box;
}
.ui-slider-input::-webkit-outer-spin-button,
.ui-slider-input::-webkit-inner-spin-button {
	-webkit-appearance: none;
	margin: 0;
}
.ui-slider-track,
.ui-slider-switch {
	position: relative;
	overflow: visible;
	height: 15px;
	margin: 0 15px 0 68px;
	top: 6px;
}
.ui-slider-track.ui-mini {
	height: 12px;
	top: 8px;
}
.ui-slider-bg {
	border: none;
	height: 100%;
}
/* High level of specificity to override button margins in grids */
.ui-slider-track .ui-btn.ui-slider-handle,
.ui-slider-switch .ui-btn.ui-slider-handle {
	position: absolute;
	z-index: 1;
	top: 50%;
	width: 28px;
	height: 28px;
	margin: -15px 0 0 -15px;
	outline: 0;
}
.ui-slider-track.ui-mini .ui-slider-handle {
	height: 14px;
	width: 14px;
	margin: -8px 0 0 -7px;
}
.ui-slider-handle .ui-btn-inner {
	padding: 0;
	height: 100%;
}
.ui-slider-track.ui-mini .ui-slider-handle .ui-btn-inner {
	height: 30px;
	width: 30px;
	padding: 0;
	margin: -9px 0 0 -9px;
	border-top: none;
}
select.ui-slider-switch {
	display: none;
}
div.ui-slider-switch {
	display: inline-block;
	height: 32px;
	width: 5.8em;
	margin: .5em 0;
	top: 0;
}
/* reset the clearfix */
div.ui-slider-switch:before, div.ui-slider-switch:after {
	display: none;
	clear: none;
}
div.ui-slider-switch.ui-mini {
	width: 5em;
	height: 29px;
	margin: .25em 0;
	top: 0;
}
.ui-field-contain .ui-slider-switch,
.ui-field-contain .ui-slider-switch.ui-mini {
	margin: 0;
}
.ui-slider-inneroffset {
	margin: 0 16px;
	position: relative;
	z-index: 1;
}
.ui-slider-switch.ui-mini .ui-slider-inneroffset {
	margin: 0 15px 0 14px;
}
.ui-slider-switch .ui-btn.ui-slider-handle {
	margin: 1px 0 0 -15px;
}
.ui-slider-switch.ui-mini .ui-slider-handle {
	width: 25px;
	height: 25px;
	margin: 1px 0 0 -13px;
	padding: 0;
}
.ui-slider-handle-snapping {
	-webkit-transition: left 70ms linear;
	-moz-transition: left 70ms linear;
}
.ui-slider-switch.ui-mini .ui-slider-handle .ui-btn-inner {
	height: 30px;
	width: 30px;
	padding: 0;
	margin: 0;
	border-top: none;
}
.ui-slider-switch .ui-slider-label {
	position: absolute;
	text-align: center;
	width: 100%;
	overflow: hidden;
	font-size: 16px;
	top: 0;
	line-height: 2;
	min-height: 100%;
	border-width: 0;
	white-space: nowrap;
	cursor: pointer;
}
.ui-slider-switch.ui-mini .ui-slider-label {
	font-size: 14px;
}
.ui-slider-switch .ui-slider-label-a {
	z-index: 1;
	left: 0;
	text-indent: -1.5em;
}
.ui-slider-switch .ui-slider-label-b {
	z-index: 0;
	right: 0;
	text-indent: 1.5em;
}
@media all and (min-width: 28em){
	.ui-field-contain label.ui-slider {
		vertical-align: top;
		display: inline-block;
		width: 20%;
		margin: 0 2% 0 0;
	}
	.ui-field-contain div.ui-slider {
		display: inline-block;
		width: 78%;
	}
	.ui-field-contain.ui-hide-label div.ui-slider {
		display: block;
		width: auto;
	}
	.ui-field-contain div.ui-slider-switch,
	.ui-field-contain.ui-hide-label div.ui-slider-switch {
		display: inline-block;
		width: 5.8em;
	}
	.ui-field-contain div.ui-slider-switch.ui-mini {
		width: 5em;
	}
}	
.ui-table {
   border: 0;
   border-collapse: collapse;
   padding: 0;
   width: 100%;
}
.ui-table th,
.ui-table td {
  line-height: 1.5em;
  text-align: left;
  padding: .4em .5em;
  vertical-align:top;
}
.ui-table th .ui-btn,
.ui-table td .ui-btn {
	line-height: normal;
}
.ui-table th {
  font-weight: bold;
}
.ui-table caption {
  text-align:left;
  margin-bottom:1.4em;
  opacity: .5;
}
/* Add strokes between each row */
.table-stroke thead th {
  border-bottom: 1px solid #d6d6d6; /* non-RGBA fallback */
  border-bottom: 1px solid rgba(0, 0, 0, .1);
}
.table-stroke tbody th,
.table-stroke tbody td {
  border-bottom: 1px solid #e6e6e6; /* non-RGBA fallback  */
  border-bottom: 1px solid rgba(0, 0, 0, .05);
}
/* Add alternating row stripes */
.table-stripe tbody tr:nth-child(odd) td,
.table-stripe tbody tr:nth-child(odd) th {
  background-color: #eeeeee; /* non-RGBA fallback  */
  background-color: rgba(0,0,0,0.04);
}
/* Add stroke to the header and last item */
.table-stripe thead th,
.table-stripe tbody tr:last-child {
  border-bottom: 1px solid #d6d6d6; /* non-RGBA fallback  */
  border-bottom: 1px solid rgba(0, 0, 0, .1);
}
/*
 Styles for the table columntoggle mode
*/
.ui-table-columntoggle-btn {
	float: right;
	margin-bottom:.8em;
}
/* Remove top/bottom margins around the fieldcontain on check list */
.ui-table-columntoggle-popup fieldset {
	margin:0;
}
/* Hide all prioritized columns by default */
@media only all {
	th.ui-table-priority-6,
	td.ui-table-priority-6,
	th.ui-table-priority-5,
	td.ui-table-priority-5,
	th.ui-table-priority-4,
	td.ui-table-priority-4,
	th.ui-table-priority-3,
	td.ui-table-priority-3,
	th.ui-table-priority-2,
	td.ui-table-priority-2,
	th.ui-table-priority-1,
	td.ui-table-priority-1 {
		display: none;
	}
}
/* Preset breakpoints if ".ui-responsive" class added to table */
/* Show priority 1 at 320px (20em x 16px) */
@media screen and (min-width: 20em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-1,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-1 {
		display: table-cell;
	}
}
/* Show priority 2 at 480px (30em x 16px) */
@media screen and (min-width: 30em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-2,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-2 {
		display: table-cell;
	}
}
/* Show priority 3 at 640px (40em x 16px) */
@media screen and (min-width: 40em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-3,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-3 {
		display: table-cell;
	}
}
/* Show priority 4 at 800px (50em x 16px) */
@media screen and (min-width: 50em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-4,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-4 {
		display: table-cell;
	}
}
/* Show priority 5 at 960px (60em x 16px) */
@media screen and (min-width: 60em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-5,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-5 {
		display: table-cell;
	}
}
/* Show priority 6 at 1,120px (70em x 16px) */
@media screen and (min-width: 70em) {
	.ui-table-columntoggle.ui-responsive th.ui-table-priority-6,
	.ui-table-columntoggle.ui-responsive td.ui-table-priority-6 {
		display: table-cell;
	}
}
/* Unchecked manually: Always hide */
.ui-table-columntoggle th.ui-table-cell-hidden,
.ui-table-columntoggle td.ui-table-cell-hidden,
.ui-table-columntoggle.ui-responsive th.ui-table-cell-hidden,
.ui-table-columntoggle.ui-responsive td.ui-table-cell-hidden {
	display: none;
}
/* Checked manually: Always show */
.ui-table-columntoggle th.ui-table-cell-visible,
.ui-table-columntoggle td.ui-table-cell-visible,
.ui-table-columntoggle.ui-responsive th.ui-table-cell-visible,
.ui-table-columntoggle.ui-responsive td.ui-table-cell-visible {
	display: table-cell;
}
/*
 Styles for the table columntoggle mode
*/
.ui-table-reflow td .ui-table-cell-label,
.ui-table-reflow th .ui-table-cell-label { 
	display: none;
}
/* Mobile first styles: Begin with the stacked presentation at narrow widths */ 
@media only all {
	/* Hide the table headers */ 
	.ui-table-reflow thead td, 
	.ui-table-reflow thead th {
		display: none;
	}
	/* Show the table cells as a block level element */ 
	.ui-table-reflow td,
	.ui-table-reflow th { 
		text-align: left;
		display: block;
	}
	/* Add a fair amount of top margin to visually separate each row when stacked */  
	.ui-table-reflow tbody th {
		margin-top: 3em;
	}
	/* Make the label elements a percentage width */ 
	.ui-table-reflow td .ui-table-cell-label,
	.ui-table-reflow th .ui-table-cell-label { 
		display: block;
		padding: .4em; 
		min-width: 30%; 
		display: inline-block;
		margin: -.4em 1em -.4em -.4em;
	}
	/* For grouped headers, have a different style to visually separate the levels by classing the first label in each col group */ 
	.ui-table-reflow th .ui-table-cell-label-top,
	.ui-table-reflow td .ui-table-cell-label-top {
		display: block;
		padding: .4em 0;
		margin: .4em 0;
		text-transform: uppercase;
		font-size: .9em;
		font-weight: normal;
	}
}
/* Breakpoint to show as a standard table at 560px (35em x 16px) or wider */ 
@media ( min-width: 35em ) {
	/* Fixes table rendering when switching between breakpoints in Safari <= 5. See https://github.com/jquery/jquery-mobile/issues/5380 */
	.ui-table-reflow.ui-responsive {
		display: table-row-group;
	}
	/* Show the table header rows */ 
	.ui-table-reflow.ui-responsive td,
	.ui-table-reflow.ui-responsive th,
	.ui-table-reflow.ui-responsive tbody th,
	.ui-table-reflow.ui-responsive tbody td,
	.ui-table-reflow.ui-responsive thead td,
	.ui-table-reflow.ui-responsive thead th {
		display: table-cell;
		margin: 0;
	}
	/* Hide the labels in each cell */ 
	.ui-table-reflow.ui-responsive td .ui-table-cell-label,
	.ui-table-reflow.ui-responsive th .ui-table-cell-label { 
		display: none;
	}
}
/* Hack to make IE9 and WP7.5 treat cells like block level elements, scoped to ui-responsive class */ 
/* Applied in a max-width media query up to the table layout breakpoint so we don't need to negate this*/ 
@media ( max-width: 35em ) {
	.ui-table-reflow.ui-responsive td,
	.ui-table-reflow.ui-responsive th {
		width: 100%;
		-webkit-box-sizing: border-box;
		-moz-box-sizing: border-box;
		box-sizing: border-box;
		float: left;
		clear: left;
	}
}
/* panel */
.ui-panel {
	width: 17em;
	min-height: 100%;
	max-height: none;
	border-width: 0;
	position: absolute;
	top: 0;
	display: block;
}
.ui-panel-closed {
	width: 0;
	max-height: 100%;
	overflow: hidden;
	visibility: hidden;
}
.ui-panel-fixed {
	position: fixed;
	bottom: -1px; /* fixes gap on Chrome for Android */
	padding-bottom: 1px;
}
.ui-panel-display-overlay {
	z-index: 1001; /* fixed toolbars have z-index 1000 */
}
.ui-panel-display-reveal {
	z-index: 0;
}
.ui-panel-display-push {
	z-index: 999;
}
.ui-panel-inner {
	padding: 15px;
}
/* content-wrap */
.ui-panel-content-wrap {
	position: relative;
	left: 0;
	min-height: inherit;
	border: none;
	z-index: 999;
}
.ui-panel-content-wrap-display-overlay,
.ui-panel-animate.ui-panel-content-wrap > .ui-header, /* ios4 fix */
.ui-panel-content-wrap-closed {
	position: static;
}
/* dismiss */
.ui-panel-dismiss {
	position: absolute;
	top: 0;
	left:0;
	height: 100%;
	width: 100%;
	z-index: 1002;
	display: none;
}
.ui-panel-dismiss-open {
	display: block;
}
/* animate class is added to panel, wrapper and fixed toolbars */
.ui-panel-animate {
	-webkit-transition: -webkit-transform 350ms ease;
	-moz-transition: -moz-transform 350ms ease;
	transition: transform 350ms ease;
}
/* hardware acceleration for smoother transitions on WebKit browsers */
.ui-panel-animate.ui-panel:not(.ui-panel-display-reveal),
.ui-panel-animate.ui-panel:not(.ui-panel-display-reveal) > div,
.ui-panel-animate.ui-panel-closed.ui-panel-display-reveal > div,
.ui-panel-animate.ui-panel-content-wrap,
.ui-panel-animate.ui-panel-content-fixed-toolbar {
	-webkit-backface-visibility: hidden;
	-webkit-transform: translate3d(0,0,0);
}
/* positioning: panel */
/* panel left  */
.ui-panel-position-left {
	left: -17em;
}
/* animated: panel left (for overlay and push) */
.ui-panel-animate.ui-panel-position-left.ui-panel-display-overlay,
.ui-panel-animate.ui-panel-position-left.ui-panel-display-push {
	left: 0;
	-webkit-transform: translate3d(-17em,0,0);
	-moz-transform: translate3d(-17em,0,0);
	transform: translate3d(-17em,0,0);
}
/* panel left open */
.ui-panel-position-left.ui-panel-display-reveal, /* negate "panel left" for reveal */
.ui-panel-position-left.ui-panel-open {
	left: 0;
}
/* animated: panel left open (for overlay and push) */
.ui-panel-animate.ui-panel-position-left.ui-panel-open.ui-panel-display-overlay,
.ui-panel-animate.ui-panel-position-left.ui-panel-open.ui-panel-display-push {
	-webkit-transform: translate3d(0,0,0);
	transform: translate3d(0,0,0);
	-moz-transform: none;
}
/* panel right */
.ui-panel-position-right {
	right: -17em;
}
/* animated: panel right (for overlay and push) */
.ui-panel-animate.ui-panel-position-right.ui-panel-display-overlay,
.ui-panel-animate.ui-panel-position-right.ui-panel-display-push {
	right: 0;
	-webkit-transform: translate3d(17em,0,0);
	-moz-transform: translate3d(17em,0,0);
	transform: translate3d(17em,0,0);
}
/* panel right open */
.ui-panel-position-right.ui-panel-display-reveal,  /* negate "panel right" for reveal */
.ui-panel-position-right.ui-panel-open {
	right: 0;
}
/* animated: panel right open (for overlay and push) */
.ui-panel-animate.ui-panel-position-right.ui-panel-open.ui-panel-display-overlay,
.ui-panel-animate.ui-panel-position-right.ui-panel-open.ui-panel-display-push {
	-webkit-transform: translate3d(0,0,0);
	transform: translate3d(0,0,0);
	-moz-transform: none;
}
/* positioning: content wrap, fixed toolbars and dismiss */
/* panel left open */
.ui-panel-content-fixed-toolbar-position-left.ui-panel-content-fixed-toolbar-open,
.ui-panel-content-wrap-position-left.ui-panel-content-wrap-open,
.ui-panel-dismiss-position-left.ui-panel-dismiss-open {
	left: 17em;
	right: -17em;
}
/* animated: panel left open (for reveal and push) */
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-left.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-reveal,
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-left.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-push,
.ui-panel-animate.ui-panel-content-wrap-position-left.ui-panel-content-wrap-open.ui-panel-content-wrap-display-reveal,
.ui-panel-animate.ui-panel-content-wrap-position-left.ui-panel-content-wrap-open.ui-panel-content-wrap-display-push {
	left: 0;
	right: 0;
	-webkit-transform: translate3d(17em,0,0);
	-moz-transform: translate3d(17em,0,0);
	transform: translate3d(17em,0,0);
}
/* panel right open */
.ui-panel-content-fixed-toolbar-position-right.ui-panel-content-fixed-toolbar-open,
.ui-panel-content-wrap-position-right.ui-panel-content-wrap-open,
.ui-panel-dismiss-position-right.ui-panel-dismiss-open {
	left: -17em;
	right: 17em;
}
/* animated: panel right open (for reveal and push) */
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-right.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-reveal, 
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-right.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-push,
.ui-panel-animate.ui-panel-content-wrap-position-right.ui-panel-content-wrap-open.ui-panel-content-wrap-display-reveal, 
.ui-panel-animate.ui-panel-content-wrap-position-right.ui-panel-content-wrap-open.ui-panel-content-wrap-display-push {
	left: 0;
	right: 0;
	-webkit-transform: translate3d(-17em,0,0);
	-moz-transform: translate3d(-17em,0,0);
	transform: translate3d(-17em,0,0);
}
/* negate "panel left/right open" for overlay */
.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-overlay,
.ui-panel-content-wrap-open.ui-panel-content-wrap-display-overlay {
	left: 0;
}
/* always disable overflow-x to prevent zoom issue on Android */
.ui-page-active.ui-page-panel {
	overflow-x: hidden;
}
/* shadows and borders */
.ui-panel-display-reveal {
	-webkit-box-shadow: inset -5px 0 5px rgba(0,0,0,.15);
	-moz-box-shadow: inset -5px 0 5px rgba(0,0,0,.15);
	box-shadow: inset -5px 0 5px rgba(0,0,0,.15);
}
.ui-panel-position-right.ui-panel-display-reveal {
	-webkit-box-shadow: inset 5px 0 5px rgba(0,0,0,.15);
	-moz-box-shadow: inset 5px 0 5px rgba(0,0,0,.15);
	box-shadow: inset 5px 0 5px rgba(0,0,0,.15);
}
.ui-panel-display-overlay {
	-webkit-box-shadow: 5px 0 5px rgba(0,0,0,.15);
	-moz-box-shadow: 5px 0 5px rgba(0,0,0,.15);
	box-shadow: 5px 0 5px rgba(0,0,0,.15);
}
.ui-panel-position-right.ui-panel-display-overlay {
	-webkit-box-shadow: -5px 0 5px rgba(0,0,0,.15);
	-moz-box-shadow: -5px 0 5px rgba(0,0,0,.15);
	box-shadow: -5px 0 5px rgba(0,0,0,.15);
}
.ui-panel-display-push.ui-panel-open.ui-panel-position-left {
	border-right-width: 1px;
	margin-right: -1px;
}
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-left.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-push {
	margin-left: 1px;
}
.ui-panel-display-push.ui-panel-open.ui-panel-position-right {
	border-left-width: 1px;
	margin-left: -1px;
}
.ui-panel-animate.ui-panel-content-fixed-toolbar-position-right.ui-panel-content-fixed-toolbar-open.ui-panel-content-fixed-toolbar-display-push {
	margin-right: 1px;
}
/* wrap on wide viewports once open */
@media (min-width:55em){
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-push.ui-panel-content-fixed-toolbar-position-left,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-reveal.ui-panel-content-fixed-toolbar-position-left,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-wrap-display-push.ui-panel-content-wrap-position-left,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-wrap-display-reveal.ui-panel-content-wrap-position-left {
		margin-right: 17em;
	}
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-push.ui-panel-content-fixed-toolbar-position-right,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-reveal.ui-panel-content-fixed-toolbar-position-right,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-wrap-display-push.ui-panel-content-wrap-position-right,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-wrap-display-reveal.ui-panel-content-wrap-position-right {
		margin-left: 17em;
	}
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-push,
	.ui-responsive-panel.ui-page-panel-open .ui-panel-content-fixed-toolbar-display-reveal {
		width: auto;	
	}
	.ui-responsive-panel .ui-panel-dismiss-display-push {
		display: none;
	}	
}


File: /flash\hotspot\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>INTERNET > MASUK</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta http-equiv="pragma" content="no-cache" />
  <meta http-equiv="expires" content="-1" />
  <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
  <script src="jqm/jquery-1.9.1.min.js"></script>
  <script src="jqm/jquery.mobile-1.3.1.min.js"></script>
</head>
<body>
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
<div data-role="page">

  <div data-role="header" data-position="fixed">
    <h1><a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">INTERNET > MASUK</a></h1>
  </div><!-- /header -->

  <div class="ui-body">
    <h1>Selamat Datang</h1>
    <p>di Internet Desa Wlahar Wetan. Internet ini merupakan media resmi Pemerintah Desa (PemDes) Wlahar Wetan dan semoga dapat bermanfaat bagi semua pihak.</p>
    <div align="center">$(if error)<br /><div style="color: #FF8080; font-size: 15px">$(error)</div>$(endif)</div>
    <div data-role="collapsible" data-collapsed="true" data-theme="a">
      <h3>Internet Cepat</h3>
      <p><p><strong>Masuk</strong> dengan akun terdaftar memiliki akses internet tak terbatas kecepatan dan waktu penggunaan, hanya dengan memasukkan nama pengguna dan kata sandi, untuk info lebih lanjut dapat menghubungi admin desa wlahar wetan melalui alamat e-mail <strong>info@wlaharwetan.desa.id</strong></p>
      <form name="login" action="$(link-login-only)" method="post"
          $(if chap-id) onSubmit="return doLogin()" $(endif)>
        <input type="hidden" name="dst" value="$(link-orig)" />
        <input type="hidden" name="popup" value="true" />
        <label for="name-c">Nama Pengguna:</label>
        <input name="username" type="text" value="$(username)" placeholder="Nama Pengguna">
        <label for="name-c">Kata Sandi:</label>
        <input type="password" name="password" placeholder="Kata Sandi"><br>
        <input type="submit" value="MASUK">
      </form>
      </p>
    </div><!-- /collapsible -->
    <div data-role="collapsible" data-theme="a" data-content-theme="a">
      <h3>Internet Gratis</h3>
      <p><p><strong>Masuk</strong> dengan akun bebas memiliki akses internet cepat 256kbps dan terbatas waktu 9 jam/hari, tidak perlu repot memasukkan nama pengguna dan kata sandi, selamat berselancar.</p>
      $(if trial == 'yes')
      <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)"><input class="btn btn-warning" type="submit" value="GRATIS"></a>
      $(endif)
      </p>
    </div>
  </div>

  <div data-role="footer" data-position="fixed">
    <div data-role="navbar">
      <ul>
        <li><a href="#" class="ui-btn-active ui-state-persist">Ditenagai oleh MikroTik RouterOS</a></li>
      </ul>
    </div>
  </div>

</div><!-- /page -->
<script type="text/javascript">
<!--
  document.login.username.focus();
  jnjkeverugiwghiuhvuh6i45a

  ghgfhg gfjhjhg
//-->
</script>
</body>
</html>


File: /flash\hotspot\logout.html
<html>
<head>
<title>INTERNET > KELUAR</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{

border-width: 1px;
border-collapse: collapse;
border-color: #c1c1c1;
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

th {
    border-bottom: 1px solid #d6d6d6;
}

tr:nth-child(even) {
    background: #e9e9e9;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
</head>

<body>
<script language="JavaScript">
<!--
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
//-->
</script>

<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<b>anda sudah keluar</b> <br><br>
<table data-role="table" data-mode="columntoggle" class="ui-responsive ui-shadow" border="1">
<tr><td align="right">Nama pengguna</td><td>$(username)</td></tr>
<tr><td align="right">IP address</td><td>$(ip)</td></tr>
<tr><td align="right">MAC address</td><td>$(mac)</td></tr>
<tr><td align="right">Sesi waktu</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">Sisa waktu</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">bytes up/down:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="MASUK">
</form>
</td>
</table>
</body>
</html>


File: /flash\hotspot\lv\alogin.html
<html>
<head>
<title>mikrotik hotspot > novirzt</title>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = '$(link-redirect)';
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Js esat piesldzies
	<br><br>
	Ja nekas nenotiek, klikiniet <a href="$(link-redirect)">eit</a></td>
</tr>
</table>
</body>
</html>


File: /flash\hotspot\lv\errors.txt
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in

# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)

internal-error = sistēmas kļūda ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = konfigurācijas kļūda ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Jūs neesat pieslēdzies (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = nevaru piešķirt IP adresi - nav vairāk brīvu adrešu krātuvē

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot serviss tiek apstādināts, mēģiniet pēc brīža vēlreiz

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = lietotājam $(username) vairāk sessijas nav atļautas

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = ir sasniegts maksimālais sessiju skaits ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = nepareizs lietotāja vārds ($(username)): šī MAC adrese nav tava

# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.

chap-missing = problēmas ar kodu (mēģiniet vēlreiz, atļaujiet JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = nepareizs lietotāja vārds vai parole

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = lietotājam $(username) nav atļauts pieslēgties no šīs MAC adreses

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = lietotāja $(username) atļautasi pieslēguma laiks ir beidzies
traffic-limit = lietotāja $(username) atļautais datu pārraides apjoms ir sasniegts

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = autorizācijas serveris neatbild (mēģiniet vēlreiz)

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = notiek autorizācija (mēģiniet vēlāk)

# radius-reply
# Radius server returned some custom error message

radius-reply = autorizācijas kļūda ($(error-orig))


File: /flash\hotspot\lv\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>mikrotik hotspot > ieeja </title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />
<style type="text/css">
body {color: #737373; font-size: 10px; font-family: verdana;}

textarea,input,select {
background-color: #FDFBFB;
border: 1px solid #BBBBBB;
padding: 2px;
margin: 1px;
font-size: 14px;
color: #808080;
}

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 14px; color: #7A7A7A; }
</style>

</head>

<body>
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

<div align="center">
<a href="$(link-login-only)?target=%2F&amp;dst=$(link-orig-esc)">English</a>
</div>

<table width="100%" style="margin-top: 10%;">
	<tr>
	<td align="center" valign="middle">
		<div class="notice" style="color: #c1c1c1; font-size: 9px">Lūdzu pieslēdzieties, lai lietotu mikrotik hotspot servisu.<br />$(if trial == 'yes')Lai izmēģinātu bez maksas, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">spiediet šeit.</a>.$(endif)</div><br />
		<table width="240" height="240" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
			<tr>
				<td align="center" valign="bottom" height="175" colspan="2">
					<form name="login" action="$(link-login-only)" method="post"
					    $(if chap-id) onSubmit="return doLogin()" $(endif)>
						<input type="hidden" name="dst" value="$(link-orig)" />
						<input type="hidden" name="popup" value="true" />
						
							<table width="100" style="background-color: #ffffff">
								<tr><td align="right">login</td>
										<td><input style="width: 80px" name="username" type="text" value="$(username)"/></td>
								</tr>
								<tr><td align="right">parole</td>
										<td><input style="width: 80px" name="password" type="password"/></td>
								</tr>
								<tr><td>&nbsp;</td>
										<td><input type="submit" value="OK" /></td>
								</tr>
							</table>
					</form>
				</td>
			</tr>
			<tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
		</table>
	
	<br /><div style="color: #c1c1c1; font-size: 9px">nodrošina mikrotik routeros &copy; 2005 mikrotik</div>
	$(if error)<br /><div style="color: #FF8080; font-size: 9px">$(error)</div>$(endif)
	</td>
	</tr>
</table>

<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
</body>
</html>


File: /flash\hotspot\lv\logout.html
<html>
<head>
<title>mikrotik hotspot > atsldzies</title>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{
 
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
</head>

<body>
<script language="JavaScript">
<!--
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
//-->
</script>

<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<b>sessija ir aizvrta</b> <br><br>
<table class="tabula" border="1">  
<tr><td align="right">lietotja vrds</td><td>$(username)</td></tr>
<tr><td align="right">IP adrese</td><td>$(ip)</td></tr>
<tr><td align="right">MAC adrese</td><td>$(mac)</td></tr>
<tr><td align="right">sesijas ilgums</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">atlikuais laiks</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" value="pieslgties no jauna">
</form>
</td>
</table>
</body>
</html>


File: /flash\hotspot\lv\radvert.html
<html>
<head>
<title>mikrotik hotspot > advertisement</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = '$(link-orig)';
    }
    function openAd() {
	location.href = '$(link-redirect)';
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Reklma.
	<br><br>
	Ja nekas nenotiek, atveriet
	<a href="$(link-redirect)" target="hotspot_advert">reklmu</a>
	parocgi.
	</td>
</tr>
</table>
</body>
</html>


File: /flash\hotspot\lv\status.html
<html>
<head>
<title>mikrotik hotspot > statuss</title>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta http-equiv="Content-Type" content="text/html; charset=windows-1257">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

.tabula{
 
border-width: 1px; 
border-collapse: collapse; 
border-color: #c1c1c1; 
background-color: transparent;
font-family: verdana;
font-size: 11px;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; padding: 4px;}

-->
</style>
<script language="JavaScript">
<!--
$(if advert-pending == 'yes')
    var popup = '';
    function focusAdvert() {
	if (window.focus) popup.focus();
    }
    function openAdvert() {
	popup = open('$(link-advert)', 'hotspot_advert', '');
	setTimeout("focusAdvert()", 1000);
    }
$(endif)
    function openLogout() {
	if (window.name != 'hotspot_status') return true;
        open('$(link-logout)', 'hotspot_logout', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=280,height=250');
	window.close();
	return false;
    }
//-->
</script>
</head>
<body bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0"
$(if advert-pending == 'yes')
	onLoad="openAdvert()"
$(endif)
>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
<table border="1" class="tabula">
$(if login-by == 'trial')
	<br><div style="text-align: center;">Sveiks!</div><br>
$(elif login-by != 'mac')
	<br><div style="text-align: center;">Sveiks $(username)!</div><br>
$(endif)
	<tr><td align="right">IP adrese:</td><td>$(ip)</td></tr>
	<tr><td align="right">baiti prom/urp:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
$(if session-time-left)
	<tr><td align="right">ilgums / atlicis:</td><td>$(uptime) / $(session-time-left)</td></tr>
$(else)
	<tr><td align="right">ilgums:</td><td>$(uptime)</td></tr>
$(endif)
$(if blocked == 'yes')
	<tr><td align="right">statuss:</td><td><div style="color: #FF8080">
nepiecieama <a href="$(link-advert)" target="hotspot_advert">reklma</a></div></td>
$(elif refresh-timeout)
	<tr><td align="right">intervls:</td><td>$(refresh-timeout)</td>
$(endif)

</table>
$(if login-by-mac != 'yes')
<br>
<input type="submit" value="atslgties">
$(endif)
</form>
</td>
</table>
</body>
</html>


File: /flash\hotspot\md5.js
/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 1.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Code also contributed by Greg Holt
 * See http://pajhome.org.uk/site/legal.html for details.
 */

/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt))
}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t)
{
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t)
{
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t)
{
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t)
{
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t)
{
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}

/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x)
{
  var a =  1732584193
  var b = -271733879
  var c = -1732584194
  var d =  271733878

  for(i = 0; i < x.length; i += 16)
  {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d

    a = ff(a, b, c, d, x[i+ 0], 7 , -680876936)
    d = ff(d, a, b, c, x[i+ 1], 12, -389564586)
    c = ff(c, d, a, b, x[i+ 2], 17,  606105819)
    b = ff(b, c, d, a, x[i+ 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i+ 4], 7 , -176418897)
    d = ff(d, a, b, c, x[i+ 5], 12,  1200080426)
    c = ff(c, d, a, b, x[i+ 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i+ 7], 22, -45705983)
    a = ff(a, b, c, d, x[i+ 8], 7 ,  1770035416)
    d = ff(d, a, b, c, x[i+ 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i+10], 17, -42063)
    b = ff(b, c, d, a, x[i+11], 22, -1990404162)
    a = ff(a, b, c, d, x[i+12], 7 ,  1804603682)
    d = ff(d, a, b, c, x[i+13], 12, -40341101)
    c = ff(c, d, a, b, x[i+14], 17, -1502002290)
    b = ff(b, c, d, a, x[i+15], 22,  1236535329)

    a = gg(a, b, c, d, x[i+ 1], 5 , -165796510)
    d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632)
    c = gg(c, d, a, b, x[i+11], 14,  643717713)
    b = gg(b, c, d, a, x[i+ 0], 20, -373897302)
    a = gg(a, b, c, d, x[i+ 5], 5 , -701558691)
    d = gg(d, a, b, c, x[i+10], 9 ,  38016083)
    c = gg(c, d, a, b, x[i+15], 14, -660478335)
    b = gg(b, c, d, a, x[i+ 4], 20, -405537848)
    a = gg(a, b, c, d, x[i+ 9], 5 ,  568446438)
    d = gg(d, a, b, c, x[i+14], 9 , -1019803690)
    c = gg(c, d, a, b, x[i+ 3], 14, -187363961)
    b = gg(b, c, d, a, x[i+ 8], 20,  1163531501)
    a = gg(a, b, c, d, x[i+13], 5 , -1444681467)
    d = gg(d, a, b, c, x[i+ 2], 9 , -51403784)
    c = gg(c, d, a, b, x[i+ 7], 14,  1735328473)
    b = gg(b, c, d, a, x[i+12], 20, -1926607734)

    a = hh(a, b, c, d, x[i+ 5], 4 , -378558)
    d = hh(d, a, b, c, x[i+ 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i+11], 16,  1839030562)
    b = hh(b, c, d, a, x[i+14], 23, -35309556)
    a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060)
    d = hh(d, a, b, c, x[i+ 4], 11,  1272893353)
    c = hh(c, d, a, b, x[i+ 7], 16, -155497632)
    b = hh(b, c, d, a, x[i+10], 23, -1094730640)
    a = hh(a, b, c, d, x[i+13], 4 ,  681279174)
    d = hh(d, a, b, c, x[i+ 0], 11, -358537222)
    c = hh(c, d, a, b, x[i+ 3], 16, -722521979)
    b = hh(b, c, d, a, x[i+ 6], 23,  76029189)
    a = hh(a, b, c, d, x[i+ 9], 4 , -640364487)
    d = hh(d, a, b, c, x[i+12], 11, -421815835)
    c = hh(c, d, a, b, x[i+15], 16,  530742520)
    b = hh(b, c, d, a, x[i+ 2], 23, -995338651)

    a = ii(a, b, c, d, x[i+ 0], 6 , -198630844)
    d = ii(d, a, b, c, x[i+ 7], 10,  1126891415)
    c = ii(c, d, a, b, x[i+14], 15, -1416354905)
    b = ii(b, c, d, a, x[i+ 5], 21, -57434055)
    a = ii(a, b, c, d, x[i+12], 6 ,  1700485571)
    d = ii(d, a, b, c, x[i+ 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i+10], 15, -1051523)
    b = ii(b, c, d, a, x[i+ 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i+ 8], 6 ,  1873313359)
    d = ii(d, a, b, c, x[i+15], 10, -30611744)
    c = ii(c, d, a, b, x[i+ 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i+13], 21,  1309151649)
    a = ii(a, b, c, d, x[i+ 4], 6 , -145523070)
    d = ii(d, a, b, c, x[i+11], 10, -1120210379)
    c = ii(c, d, a, b, x[i+ 2], 15,  718787259)
    b = ii(b, c, d, a, x[i+ 9], 21, -343485551)

    a = safe_add(a, olda)
    b = safe_add(b, oldb)
    c = safe_add(c, oldc)
    d = safe_add(d, oldd)
  }
  return [a, b, c, d]
}

/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = "0123456789abcdef"
  var str = ""
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8)) & 0xF)
  }
  return str
}

/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for(var i = 0; i < binarray.length * 32; i += 6)
  {
    str += tab.charAt(((binarray[i>>5] << (i%32)) & 0x3F) |
                      ((binarray[i>>5+1] >> (32-i%32)) & 0x3F))
  }
  return str
}

/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str)
{
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>2] |= (str.charCodeAt(i) & 0xFF) << ((i%4) * 8)
  blks[i>>2] |= 0x80 << ((i%4) * 8)
  blks[nblk*16-2] = str.length * 8
  return blks
}

/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str)
{
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>1] |= str.charCodeAt(i) << ((i%2) * 16)
  blks[i>>1] |= 0x80 << ((i%2) * 16)
  blks[nblk*16-2] = str.length * 16
  return blks
}

/*
 * External interface
 */
function hexMD5 (str) { return binl2hex(coreMD5( str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5 (str) { return binl2b64(coreMD5( str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5( str2binl(str))) }


File: /flash\hotspot\radvert.html
<html>
<head>
<title>INTERNET > IKLAN</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = '$(link-orig)';
    }
    function openAd() {
	location.href = '$(link-redirect)';
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Iklan.
	<br><br>
	Jika tidak ada yang terjadi, membuka
	<a href="$(link-redirect)" target="hotspot_advert">iklan</a>
	secara manual.
	</td>
</tr>
</table>
</body>
</html>


File: /flash\hotspot\redirect.html
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
</head>
<body>
</body>
</html>


File: /flash\hotspot\rlogin.html
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)?target=xml</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
-->
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
<script src="jqm/jquery-1.9.1.min.js"></script>
<script src="jqm/jquery.mobile-1.3.1.min.js"></script>
</head>
<body>
</body>
</html>


File: /flash\hotspot\status.html
<!DOCTYPE html>
<html>
<head>
  <title>INTERNET > STATUS</title>
  $(if refresh-timeout)
  <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
  $(endif)
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <meta http-equiv="pragma" content="no-cache">
  <meta http-equiv="expires" content="-1">
  <meta name="viewport" content="initial-scale=1.0">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <link rel="stylesheet" href="jqm/jquery.mobile-1.3.1.css" />
  <script src="jqm/jquery-1.9.1.min.js"></script>
  <script src="jqm/jquery.mobile-1.3.1.min.js"></script>
    <style type="text/css">
    <!--
    textarea,input,select {
    background-color: #FDFBFB;
    border: 1px #BBBBBB solid;
    padding: 2px;
    margin: 1px;
    font-size: 14px;
    color: #808080;
    }

    .tabula{

    border-width: 1px;
    border-collapse: collapse;
    border-color: #c1c1c1;
    background-color: transparent;
    font-family: verdana;
    font-size: 11px;
    }

    body{ color: #737373; font-size: 12px; font-family: verdana; }

    a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
    a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
    img {border: none;}
    td { font-size: 12px; padding: 4px;}

    -->
    </style>
    <script language="JavaScript">
        <!--
        $(if advert-pending == 'yes')
            var popup = '';
            function focusAdvert() {
          if (window.focus) popup.focus();
            }
            function openAdvert() {
          popup = open('$(link-advert)', 'hotspot_advert', '');
          setTimeout("focusAdvert()", 1000);
            }
        $(endif)
            function openLogout() {
          if (window.name != 'hotspot_status') return true;
            open('$(link-logout)', 'hotspot_logout', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=280,height=250');
          window.close();
          return false;
            }
        //-->
    </script>
</head>
<body  bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0"
$(if advert-pending == 'yes')
  onLoad="openAdvert()"
$(endif)
>

<div data-role="page">

  <div data-role="header" data-position="fixed">
    <h1>INTERNET > STATUS</h1>
  </div><!-- /header -->
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
$(if login-by == 'trial')
	<br><div style="text-align: center;">Selamat Datang Pengguna Internet Gratis<br> Desa Wlahar Wetan</div>
$(elif login-by != 'mac')
	<br><div style="text-align: center;">Selamat Datang $(username)!<br> di Internet Desa Wlahar Wetan</div>
$(endif)
  <div data-role="content">
    <ul data-role="listview" data-inset="true">
      <li data-role="list-divider">STATUS DATA</li>
      <li>IP address: $(ip)</li>
      <li>bytes up/down: $(bytes-in-nice) / $(bytes-out-nice)</li>
      $(if session-time-left)
      <li>connected / left: $(uptime) / $(session-time-left)</li>
      $(else)
      <li>connected: $(uptime)</li>
      $(endif)
      $(if blocked == 'yes')
      <li>status: <a href="$(link-advert)" target="hotspot_advert">advertisement</a> required</li>
      $(elif refresh-timeout)
      <li>status refresh: $(refresh-timeout)</li>
      $(endif)
    </ul>
    $(if login-by-mac != 'yes')
    <!-- user manager link. if user manager resides on other router, replace $(hostname) by its address
    <button onclick="document.location='http://$(hostname)/user?subs='; return false;">status</button>
    <!-- end of user manager link -->
    <input type="submit" value="KELUAR">

  </div><!-- /content -->
    $(endif)
</form>
  <div data-role="footer" data-position="fixed">
    <div data-role="navbar">
      <ul>
        <li><a href="#" class="ui-btn-active ui-state-persist">Ditenagai oleh MikroTik RouterOS</a></li>
      </ul>
    </div>
  </div>

</div><!-- /page -->

</body>
</html>


File: /flash\hotspot\xml\alogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>50</ResponseCode>
	<LogoffURL>$(link-logout)</LogoffURL>
	<RedirectionURL>$(link-redirect)</RedirectionURL>
$(if radius18[0])	<ReplyMessage>$(radius18[0])</ReplyMessage>	$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\error.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>255</ResponseCode>
	<ReplyMessage>$(error)</ReplyMessage>
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\flogout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\login.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>
$(if error-type == 'radius-timeout')
		102
$(else)
		100
$(endif)
	</ResponseCode>
$(if error)		<ReplyMessage>$(error)</ReplyMessage>		$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\logout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
<WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\rlogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
--> </HTML>


File: /flash\hotspot\xml\WISPAccessGatewayParam.xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="WISPAccessGatewayParam">
		<xs:complexType>
			<xs:choice>
				<xs:element name="Redirect" type="RedirectType"/>
				<xs:element name="Proxy" type="ProxyType"/>
				<xs:element name="AuthenticationReply" type="AuthenticationReplyType"/>
				<xs:element name="AuthenticationPollReply" type="AuthenticationPollReplyType"/>
				<xs:element name="LogoffReply" type="LogoffReplyType"/>
				<xs:element name="AbortLoginReply" type="AbortLoginReplyType"/>
			</xs:choice>
		</xs:complexType>
	</xs:element>
	<xs:simpleType name="AbortLoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="NextURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="AccessProcedureType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="AccessLocationType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LocationNameType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="MessageTypeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ResponseCodeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ReplyMessageType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginResultsURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="LogoffURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="DelayType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:complexType name="RedirectType">
		<xs:all>
			<xs:element name="AccessProcedure" type="AccessProcedureType"/>
			<xs:element name="AccessLocation" type="AccessLocationType"/>
			<xs:element name="LocationName" type="LocationNameType"/>
			<xs:element name="LoginURL" type="LoginURLType"/>
			<xs:element name="AbortLoginURL" type="AbortLoginURLType"/>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="ProxyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="NextURL" type="NextURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LoginResultsURL" type="LoginResultsURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationPollReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="LogoffReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AbortLoginReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:sequence>
	</xs:complexType>
</xs:schema>


File: /README.md
# MikroTik Gedhe Foundation
Hanya desain login mikrotik hotspot untuk desa


