# Repository Information
Name: mikrotik-hotspot-external-login-page-none-PHP

# Directory Structure
Directory structure:
└── github_repos/mikrotik-hotspot-external-login-page-none-PHP/
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
    │   │       ├── pack-7ed35e298cc4159c9329626cfa85c8c6565cb7cc.idx
    │   │       └── pack-7ed35e298cc4159c9329626cfa85c8c6565cb7cc.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── default_slide_images/
    │   └── readme.md
    ├── hospot_login_page/
    │   └── login.html
    ├── images/
    │   └── default_slide_images/
    │       └── readme.md
    ├── index.html
    ├── line-awesome/
    │   ├── css/
    │   │   └── line-awesome.css
    │   └── fonts/
    │       ├── line-awesome.eot
    │       ├── line-awesome.ttf
    │       ├── line-awesome.woff
    │       └── line-awesome.woff2
    ├── md5.js
    ├── qs.js
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
	url = https://github.com/Tsehla/mikrotik-hotspot-external-login-page-none-PHP.git
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
0000000000000000000000000000000000000000 b5a0252945647508613bd857807ccc112e584047 vivek-dodia <vivek.dodia@icloud.com> 1738606046 -0500	clone: from https://github.com/Tsehla/mikrotik-hotspot-external-login-page-none-PHP.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b5a0252945647508613bd857807ccc112e584047 vivek-dodia <vivek.dodia@icloud.com> 1738606046 -0500	clone: from https://github.com/Tsehla/mikrotik-hotspot-external-login-page-none-PHP.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b5a0252945647508613bd857807ccc112e584047 vivek-dodia <vivek.dodia@icloud.com> 1738606046 -0500	clone: from https://github.com/Tsehla/mikrotik-hotspot-external-login-page-none-PHP.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b5a0252945647508613bd857807ccc112e584047 refs/remotes/origin/master


File: /.git\refs\heads\master
b5a0252945647508613bd857807ccc112e584047


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /default_slide_images\readme.md
Images should be more than : width 703; height : 1024


File: /hospot_login_page\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>internet hotspot > login</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="pragma" content="no-cache" />
<meta http-equiv="expires" content="-1" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
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
	
<script type="text/javascript">//checks for internet connection//en if available show external login//if not available show default mikrotik

	if(navigator.onLine){
		window.open('http://street-wify-transcat.herokuapp.com/hotspot?login=true&error=$(error)&link-login-only=$(link-login-only)&link-orig=$(link-orig)&chap-id=$(chap-id)&chap-challenge=$(chap-challenge)&link-orig-esc=$(link-orig-esc)&mac-esc=$(mac-esc)&username=$(username)&location=orangefarm', '_self');//open link where hotspot is at  
	}
	
</script>

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
<a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)">Latviski</a>
</div>

<table width="100%" style="margin-top: 10%;">
	<tr>
	<td align="center" valign="middle">
		<div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br />$(if trial == 'yes')Free trial available, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)</div><br />
		<table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
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
								<tr><td align="right">password</td>
										<td><input style="width: 80px" name="password" type="password"/></td>
								</tr>
								<tr><td>&nbsp;</td>
										<td><input type="submit" value="OK" /></td>
								</tr>
							</table>
					</form>
				</td>
			</tr>
			<tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="img/logobottom.png" alt="mikrotik" /></a></td></tr>
		</table>
	
	<br /><div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
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


File: /images\default_slide_images\readme.md
Images should be more than : width 703; height : 1024


File: /index.html
<html>
	<head>
			<title>Wifi Hotspot > login</title>

			<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0"/>
			<link rel="stylesheet" href="bootstrap.min.css">
			<link rel="stylesheet" href="line-awesome/css/line-awesome.css">


			<style type="text/css">
				body {color: #737373; font-size: 12px; font-family: verdana;min-height: 500px}

				img {border: none;}
				input{
						font-size: 1.5em;
						text-align: center;
					}
				*::-webkit-input-placeholder {
					color: blue;
				}
				*:-moz-placeholder {/* FF 4-18 */
					color: blue;
				}
				*::-moz-placeholder {/* FF 19+ */
					color: blue;
				}
				*:-ms-input-placeholder {/* IE 10+ */
					color: blue;
				}
			</style>

		</head>

	<body id='page_body'>
    
		<!-- login input forms -->
		<div style="width: 60vw;height: auto; position: absolute; display: none; background-color: antiquewhite; margin-top: 10%;margin-left:20vw;background-image: url(images/black-wood.jpg);background-position: center;background-repeat: no-repeat;background-size: cover" align="center" id="form_container">

			<!-- close button -->
			<button onclick="document.getElementById('bottom_bar').style.display='block',login_hide()" style="width: 40px; height: 40px; font-size: 1.5em; position: absolute;right: 1%; border: 0px" class="btn btn-info">&times;</button>

			<!-- login overlay background -->
			<div style="border: 3px double #cccccc; padding: 0px;background-image: url(images/black-wood.jpg); width: 100%;height: 100%">

				<!-- input content -->
				<!-- hotspot logo -->
				<p style='color: white;font-size: 15px;font-weight: 500;padding: 0px;border : 0px solid red;height: 70px' id='logo_container'></p>
				<br/>	

				<!-- top text -->
				<p style='color: white;font-size: 15px;font-weight: 500;margin: 0px;border : 0px solid red;height: auto' id='logo_container'>Enter</p>
				<br/>	

				<!-- voucher code input -->
				<input style="height: 10vh; width: 100%; margin-top:5%;border-radius: 20px" name="username" type="text" value="" placeholder="Voucher code" id='input_voucher_code'/>
				<br/>

				<!-- or -->
				<p style='color: white;font-size: 12px;font-weight: 500;margin-top: 30px'>OR</p>

				<!-- username input -->
				<input style="height: 10vh; width: 100%; margin-top:5%;border-radius: 20px" name="username" type="text" value="" placeholder="Username" id='input_user_name'/>

				<!-- user password input -->
				<input style="height: 10vh; width: 100%; margin-top:5%;border-radius: 20px" name="password" type="password" placeholder="Password" id='input_password'/>

				<!-- inputs login button -->	
				<button style="height: 15%; width: 100%; margin-top:4%;margin-bottom:4%" class="btn btn-primary" onclick='form_sender_decider()'>Log in</button>

			 </div>    

		</div>

		<br />

		<!--router error div -->
		<div style="color: #FF8080; font-size: 1.5em; width: 100%; height: 2em;text-align: center; background-color: dimgrey;border: 2px solid red;display:none" id='error_div'></div>



		<!-- Page content -->


		<!-- iframe --><!-- used to add promotions and click remotely by styling html page attached to mikrotik login as iframe --
		<iframe style="width:100vw; height: 80vh; overflow-x: auto; overflow-y: scroll; border: 0px" src="https://tsehla.github.io/strwify/index.html" seamless></iframe>
		-->

    	<!-- navi -->
        <div id='nav_container'> <!-- chnage href with you link -->
            <a href='#' onclick='balance()' class='btn btn-primary' role='button' style='margin-left: 20vw; border-bottom-right-radius:0px;border-top-right-radius:0px; '>Balance</a>
            <button class='btn btn-info' style='border-bottom-right-radius:0px;border-top-right-radius:0px;border-bottom-left-radius:0px;border-top-left-radius:0px' onclick='document.getElementById("help_container").style.display="block"'>HELP</button>
            <a href='#' onclick='logout()' class='btn btn-primary' role='button' style='border-bottom-left-radius:0px;border-top-left-radius:0px'>LogOut</a>
        </div>
        <style>  
            #nav_container{
                width: 100vw;
                height: 70px;
                display: flex;
            
            }
            #nav_container a{
                width: 20vw;
                height: 60px;
                text-align :center;
                line-height: 45px;
                font-size: 0.9em;
            }
            #nav_container button{
                width: 20vw;
                height: 60px;
                text-align :center;
                line-height: 45px;
                font-size: 18px;
            }
            
           {border: 1px solid blue}
        
        </style>

    	<!-- search -->
        <div id='navi_container'>
			<button onclick='buy()' class='btn btn-success' style="font-size: 30px">Buy</button>
            <input type='search' placeholder='Search Google or type URL' class='form-control' id='search'>
            <button onclick='search()' class='btn btn' style="background: rebeccapurple;">	&#8981;</button>
        </div>
        <style>
            #navi_container {
                width: 100vw;
                height: 70px;
				line-height: 45px;
				text-align: center;
                display: flex;
            }
            #navi_container input {
                width: 60vw;
                height: 80%;
                margin: 2% 2% 2% 4%;
                text-align: center;
            }
            #navi_container input::placeholder {
                 font-size: 15px;
            
            }
            #navi_container button {
                width: 20%;
                height: 98%;
                margin-top: 1%;
                color: snow;
                font-size: 60px;
                vertical-align: middle;
                line-height: 45px;
            }
            #navi_container button:active{
                background-color:black;
            }
            
        </style>
    	<!-- top arrow -->
        <div id='top_arrow_container' onclick='document.getElementById("free_sites_container").style.display="block"'>
            <div id='top_arrow_1' role="button" class='btn btn-default'>&#8679;</div>
        </div>
        <style>
            #top_arrow_container{
                width: 100vw;
                height: 80px;
                margin-top: 4%;
                margin-top: 4%;
                text-align: center;
                
            }
    
            #top_arrow_container div{
                width: 100%;
                margin: 0px;
                padding: 0px;
            }
            #top_arrow_container div:nth-child(1) {
                font-size: 4em;
                height: Calc(100%/1);
                color: blue;
                border: 0px;
                background-color: transparent;
                text-shadow : 2px 2px 1px snow;
                
            }            
           
        
        </style>
    	<!-- arrow center -->
        <div id='center_arrow_container'>
            <div id='left_arrow'>
                <div id='left_arrow_1' role="button" class='btn btn-default'>&#8678;</div>
            </div>
            <div id='right_arrow'>
                <div id='right_arrow_1' role="button" class='btn btn-default'>&#8680;</div>
            </div>
        </div>
            
            <style>
                #center_arrow_container {
                    width: 100vw;
                    height: 80px;
                    margin: 1vh 0px 0px 0px;
                    padding: 0px;
                    display: flex;
                    text-align: center;
                }
                /* left arrow */
                #left_arrow {
                    width: 50vw;
                    height: 100%;
                }
                #left_arrow div{
                    height: 100%;
                    vertical-align: middle;
                    line-height: 75px;
                }
                #left_arrow div:nth-child(1){
                    width:100%;
                    padding: 0px;
                    margin: 0px;
                    font-size: 60px;
                    color : orange;
                    border: 0px;
                    background-color: transparent;
                    text-shadow : 2px 2px 1px snow;
                } 
                /* right arrow */
                #right_arrow {
                    width: 50vw;
                    height: 100%;
                }
                #right_arrow div:active {
                background-color :grey;
                }
                #right_arrow div{
                    height: 100%;
                    vertical-align: middle;
                    line-height: 75px;
                    float: right;
                }
                #right_arrow div:nth-child(1){
                    width:100%;
                    padding: 0px;
                    margin: 0px;
                    font-size:60px;
                    color: orange;
                    border: 0px;
                    background-color: transparent;
                    text-shadow : 2px 2px 1px snow;
                }
            </style>

		            <!-- down arrow -->
             <div id='down_arrow_container' onclick='document.getElementById("notification_container").style.display="block"'>
                <div id='down_arrow_1' role="button" class='btn btn-default'>&#8681;</div>
				 <i class="la la-bullhorn" id='notification_alert_icon' aria-hidden="true" style="text-shadow:3px 3px 3px red, 3px 3px 3px blue;font-size: 5em;color: white "></i>
            </div>
            <style>
                #down_arrow_container{
                    width: 100vw;
                    height: 80px;
                    margin-top: 1%;
                    text-align: center;
                
                }
                #down_arrow_container div:active {
                background-color :grey;
                }
                #down_arrow_container div{
                    width: 100%;
                    margin: 0px;
                    padding: 0px;
                }
                #down_arrow_container div:nth-child(1) {
                    font-size: 60px;
                    height: Calc(100%/1);
                    color : green;
                    border: 0px;
                    background-color: transparent;
                    text-shadow : 2px 2px 1px snow;
					line-height: 75px;
                } 
				#notification_alert_icon{
					display: none;
				}
                
                
            </style>
    	<!-- wallpaper links -->
        
        <div id='walp_links_container' role='button' class='btn btn-primary'>
            <p id='walp_links' >no data yet</p>
        </div>		
		
        <style>
            #walp_links_container {
                margin-top: 7vh;
                margin-bottom: 100px;
                width: 100vw;
                height:100px;
                border: 0px;
                background: rgba(192,192,192,0.2);
                text-align: center;
                overflow: auto;
            }
            #walp_links_container p{
                width: 100%;
                height: auto;
                padding: 30px 1vw 1vh 1vw;
                background-color: transparent;
                color: snow;
                font-size: 20px;
                text-shadow : 1px 1px 12px black;
            }
        </style>
		
		<!-- notification  modal -->
       <div id='help_container'>
            <h1>How to use recharge Voucher</h1>
            <button onclick='document.getElementById("help_container").style.display="none"' class='btn btn-danger'>x</button>
            <div id='help'>
                <h2>Recharge</h2>
               
                    <ol>
                        <li>
                            Open browser 
                        </li>
                        <li>
                            goto <i style='color:green' id='how_to_router_link'></i>
                        </li>
                        <li>
                            Click <i style='color:green'>'CONNECT'</i>
                        </li>
                        <li>
                            Enter <i style='color:green'>VOUCHER</i>
                        </li>
						
						<li id='how_to_buy'></li>
						
                    </ol>
                
                <h2>Tips</h2>
                
                # Check balance
                    <ol>
                        <li>
                            goto <i style='color: green' id='how_to_check_balance'></i>
                        </li>
                    </ol>
                # Login
                    <ol>
                        <li>
                            goto <i style='color: green' id='how_to_log_in'></i>
                        </li>
                    </ol>
                # Logout
                    <ol>
                        <li>
                            goto <i style='color: green' id='how_to_log_out'></i>
                        </li>
                    </ol>
               				
				
                <h2>Voucher</h2>
                <div style="width: auto; height: 200px; background-image: url(static/images/voucher%20template.PNG); background-position: center; background-repeat: no-repeat;background-size: contain"></div>
            </div>
       <Marquee role='marquee' id='how_to_bottom_text'></Marquee>
       </div>
		<style>
             #help_container {
				font-size: 14px;
                position: fixed;
                display: none;
                top : 3vh;
                left :7vw;
                width : 85vw;
                min-height : 500px;
                max-height : 80vh;
                background-color : white;
                box-shadow: 3px 3px 13px blue, -3px -3px 13px blue;
                overflow-y: auto;
                overflow-x: hidden;
                border-radius: 9px;
              
           }
           #help_container h1 {
                width: 85%;
                height: 10%;
                margin-top: 0px;
                text-align: center;
                font-size: 1.5em;
                font-weight: 600;
                border-bottom:1px solid brown;
                padding : 0px;
                vertical-align: middle;
                line-height: 10vh;
              
           }
           #help_container button {
                position: absolute;
                width : 15%;
                height: 10%;
                top: 0px;
                right: 0px;
                padding: 0px;
                display : inline;
                float: right;
                font-size: 18px;
                vertical-align: middle;
                line-height: 5%;
                border-right: 0px;
           }
             #help {
                width: 85vw;
                height: auto;
                margin: 20px 0px 0px 0px;
                padding : 0px;
                border-bottom: 1px solid brown;
                
           }
           #help h2 {
                width :85vw;
                height: auto;
                margin: 0px;
                font-size: 1em;
                padding:0px;
                text-align: center;
                border: 1px solid grey;
                background-color:darkslategrey;
                color: snow;
           }
           #help a {
                width: 100vw;
                height: auto;
                margin : 1vh 0px 4vh 1vw;
                display:block;
                font-size: 1em;
                color : blue;
           }
           #help a:active {
                color: green;
           }
           #help a:visited{
                color: black;
           }
          
           #help_container marquee {
                width: 85vw;
                height: 10%;
                font-size: 22px;
                position: static;
          
           }
        </style>
		
		
		 <!-- free web modal -->
       <div id='free_sites_container'>
            <h1>FREE WEBSITES</h1>
            <button onclick='document.getElementById("free_sites_container").style.display="none"' class='btn btn-danger'>x</button>
            <div id='education'>
                <h2> EDUCATION</h2>
				<div id='education_free_links' style="width: auto;height: auto"></div>
            </div>
            <div id='work'>
                <h2>JOBS</h2>
                <div id='jobs_free_links' style="width: auto;height: auto"></div>
            </div>
       <Marquee role='marquee' id='free_sites_bottom_text'></Marquee>
       </div>
        <style>
           #free_sites_container {
                position: fixed;
                display: none;
                top : 3vh;
                left :7vw;
                width : 85vw;
                min-height : 500px;
                max-height : 80vh;
                background-color : white;
                box-shadow: 3px 3px 13px magenta, -3px -3px 13px magenta;
                overflow-y: auto;/*hidden scrolling*/
                overflow-x: hidden;
                border-radius: 9px;
              
           }
           #free_sites_container h1 {
                width: 85vw;
                height: 10%;
                margin-top: 0px;
                text-align: center;
                font-size: 15px;
                font-weight: 600;
                border-bottom:1px solid brown;
                padding : 0px;
                vertical-align: middle;
                line-height:50px;
              
           }
           #free_sites_container button {
                position: absolute;
                width : 10vw;
                height: 10%;
                top: 0px;
                right: 0px;
                padding: 0px;
                display : inline;
                float: right;
                font-size: 19px;
                vertical-align: middle;
                line-height: 1%;
           }
           #education {
                width: 85vw;
                height: auto;
                margin: 30px 0px 0px 0px;
                padding : 0px;
                border-bottom:1px solid brown;
           }
           #education h2 {
                width :100;
                height: 25px;
                margin-left: 10px;
                font-size: 14px;
                padding:0px;
                vertical-align: middle;
                line-height : 2.5vh;
           }
           #education a {
                width: 100vw;
                height: 30px;
                margin : 15px;
                display:block;
                font-size: 18px;
                color : blue;
           }
           #education a:active {
                color: green;
           }
           #education a:visited{
                color: black;
           }
           #work {
                width: 85vw;
                height: auto;
                margin: 20px 0px 20px 0px;
                padding : 0px;
                
           }
           #work h2 {
                width :100;
                height: 25px;
                margin-left: 10px;
                font-size: 14px;
                padding:0px;
                vertical-align: middle;
                line-height : 2.5vh;
           }
           #work a {
                width: 100vw;
                height: 30px;
                margin : 15px;
                display:block;
                font-size: 18px;
                color : blue;
           }
           #work a:active {
                color: green;
           }
           #work a:visited{
                color: black;
           }
           #free_sites_container marquee {
                width: 85vw;
                height: 10vh;
                font-size: 20px;
                position: static;
          
           }
        </style>
		
		<!-- notification  modal -->
       <div id='notification_container'>
            <h1>ANNOUNCEMENTS</h1>
            <button onclick='document.getElementById("notification_container").style.display="none"' class='btn btn-danger'>x</button>
            <div id='notification'></div>
		   
       <Marquee role='marquee' id='notification_bottom_text'></Marquee>
       </div>
        <style>
           #notification_container {
                position: fixed;
                display: none;
                top : 3vh;
                left :7vw;
                width : 85vw;
                min-height : 500px;
                max-height : 80vh;
                background-color : white;
                box-shadow: 3px 3px 13px green, -3px -3px 13px green;
                overflow-y: auto;
                overflow-x: hidden;
                border-radius: 9px;
              
           }
           #notification_container h1 {
                width: 85vw;
                height: 50px;
                margin-top: 0px;
                text-align: center;
                font-size: 15px;
                font-weight: 600;
                border-bottom:1px solid brown;
                padding : 0px;
                vertical-align: middle;
                line-height: 45px;
              
           }
           #notification_container button {
                position: absolute;
                width : 10vw;
                height: 50px;
                top: 0px;
                right: 0px;
                padding: 0px;
                display : inline;
                float: right;
                font-size: 19px;
                vertical-align: middle;
                line-height: 1vh;
           }
             #notification {
                width: 85vw;
                height: auto;
                margin: 20px 0px 0px 0px;
                padding : 0px;
                border-bottom: 1px solid brown;
                
           }
           #notification h2 {
                width :85vw;
                height: auto;
                margin: 0px;
                font-size: 10px;
                padding:0px;
                text-align: center;
                border: 1px solid grey;
                background-color: purple;
                color: snow;
           }
           #notification a {
                width: 80vw;
                height:auto;
                margin : 1vh 0px 4vh 1vw;
                display:block;
                font-size: 15px;
                color : blue;
	           }
           #notification a:active {
                color: green;
           }
           #notification a:visited{
                color: black;
           }
          
           #notification_container marquee {
                width: 85vw;
                height: 40px;
                font-size: 22px;
                position: static;
          
           }
           /*body*/
           body {
           background-image: url('slide_images/1.jpg');
           background-size: 100% 100%;
           background-repeat : no-repeat;
           background-position : center;
           }
        </style>
		
		
		
		
		
		
		
		







		<!-- Router connect button -->   
		<div id="bottom_bar" style="width:100%; min-height: 54px; max-height:64px ; background-color: #3498db; position: fixed; bottom: 5%" >
			<button onclick="document.getElementById('bottom_bar').style.display='none',login_display()" class="btn btn-success" style="width: 95px; height:45px; position: absolute; right:5%; margin-top: 4.5px">Connect</button>


		</div>


		<script type='text/JavaScript' src='jquery-3.3.1.min.js' ></script> 
		<script type="text/javascript" src="md5.js"></script>
		<!-- +++++++ get variable from router encoded on link  +++++++ -->
		<script type="text/javascript" src="qs.js"></script>
		<script type="text/javascript">

		//++++++++++++++++++login show
			function login_display(){//show login form
				document.getElementById("form_container").style.display="block";
			}
				function login_hide(){//hide login form
				document.getElementById("form_container").style.display="none";
			}


		//++++++++++++++++++++++++form processing

		//get varibles from router on link
		var router_variables_array = qs.get();
		//console.log(router_variables_array);

		// ++++++++++++++++++++++++++++++Error div 	
		if(router_variables_array.error){//if error from router

			document.getElementById('error_div').style.display='block';
			document.getElementById('error_div').innerHTML = router_variables_array.error.replace(/%20/g,' ');

		}

		//++++++++++++++++++++++++form sender
		function form_sender_decider() {

			var user_name_input_voucher_code = document.getElementById('input_voucher_code').value.toLowerCase();//converted to lower case//easy for Radiusdesk produced voucher since all are in lowercase anyway
			var user_name_input_user_name = document.getElementById('input_user_name').value;
			var user_name_input_user_password = document.getElementById('input_password').value;

			//___________________if chap used for login
			if(router_variables_array["chap-id"]){

				//http-chap//voucher only login
				if(user_name_input_voucher_code.length != 0 && user_name_input_user_name.length == 0 && user_name_input_user_password.length ==0 ){//something in voucher input

						var hashed_password = hexMD5(router_variables_array["chap-id"] + user_name_input_voucher_code + router_variables_array["chap-challenge"]);

						var form_to_url = router_variables_array["link-login-only"] + '?username=' + user_name_input_voucher_code + '&password=' + hashed_password + '&dst=' + router_variables_array["link-orig"] + '&popup=true';

						//alert(form_to_url);
						window.open(form_to_url, '_self');

						return;
					}

					//http-chap//name + password login
					if(user_name_input_voucher_code.length == 0 && user_name_input_user_name.length != 0 && user_name_input_user_password.length != 0){//nothing in voucher input
						var hashed_password = hexMD5(router_variables_array["chap-id"] + user_name_input_user_password + router_variables_array["chap-challenge"]);
						var form_to_url = router_variables_array["link-login-only"] + '?username=' + user_name_input_user_name + '&password=' + hashed_password + '&dst=' + router_variables_array["link-orig"] + '&popup=true';
						//alert(form_to_url);

						window.open(form_to_url, '_self');

						return;
					}

						alert('Please fill only Voucher code Or Username and Password.');

						document.getElementById('input_voucher_code').value='';
						document.getElementById('input_user_name').value='';
						document.getElementById('input_password').value='';

						return;
				}



				//__________________none chap login

					//voucher only login
					if(user_name_input_voucher_code.length != 0 && user_name_input_user_name.length == 0 && user_name_input_user_password.length ==0){//somethng in voucher input

							var form_to_url = router_variables_array["link-login-only"] + '?username=' + user_name_input_voucher_code + '&password=' + user_name_input_voucher_code + '&dst=' + router_variables_array["link-orig"] + '&popup=true';
							//alert(form_to_url)
							window.open(form_to_url, '_self');

						return;
					}

					//name + password login
					if(user_name_input_voucher_code.length == 0 && user_name_input_user_name.length != 0 && user_name_input_user_password.length != 0){//nothing in voucher input

							var form_to_url = router_variables_array["link-login-only"] + '?username=' + user_name_input_user_name + '&password=' + user_name_input_user_password + '&dst=' + router_variables_array["link-orig"] + '&popup=true';

							//alert(form_to_url)
							window.open(form_to_url, '_self');

						return;
					}

						alert('Please fill only Voucher code Or Username and Password.');

						document.getElementById('input_voucher_code').value='';
						document.getElementById('input_user_name').value='';
						document.getElementById('input_password').value='';

						return;

		}


		//+++++++++++++++++ db pulled data ++++++++++++++++++++++

		var hotspot_url;//GET it form db//url router hotspot server
		var hotspot_transaction_server_url;//GET form db server where voucher app runs from	
		var wall_link_description; //Get wallpaper links data from db


		function fill_data_from_db(data_from_db){//function applies data from DB

			//enviroment variables 
			hotspot_url ='http://streetwifiy.co.za';
			hotspot_transaction_server_url = 'http://streetwifiy.herokuapp.com/';
			var logo_image_url = 'images/logo.png';//logo image
			var how_to_bottom_text = 'Help yourself, To be helped;'//text shown on help menu as marquee
			var education_free_links =[
					{link:"https://scholar.google.co.za/", text:"Google scholar"},
					{link:"https://www.google.com",text:"Search on google"}
			] ;//free education links
			
			var jobs_free_links = [{link:"https://www.google.com",text:"Search on google"}];//free jobs links
			var free_sites_bottom_text = 'Pass it on, unconditionally help a stranger, a friend, a family member';//free sites bottom text;
			var notifications_from_db = ['Dare to be diffrents','Dare to write your destiny, Dare to write your destiny,Dare to write your destiny'];//notifications text
			var notification_bottom_text = 'If it was easy, no one would care. If it was impossible, no one would dare';//notification page bottom text
			
			wall_link_description =[//walp data	
				{image_link :"default_slide_images/1.jpg" , image_status_text : "Five Fingers", image_status_link: "default_slide_images/1.jpg"},	
				{image_link :"default_slide_images/2.jpg" , image_status_text : "We are One", image_status_link: "default_slide_images/2.jpg"},	
				{image_link :"default_slide_images/3.jpg" , image_status_text : "Legal for Creatives", image_status_link: "default_slide_images/3.jpg"},	
				{image_link :"default_slide_images/4.jpg" , image_status_text : "Five Fingers", image_status_link: "default_slide_images/4.jpg"},	
				{image_link :"default_slide_images/5.jpg" , image_status_text : "Marseillies", image_status_link: "default_slide_images/5.jpg"},	
				{image_link :"default_slide_images/6.jpg" , image_status_text : " Unarams", image_status_link: "default_slide_images/6.jpg"},	
				{image_link :"default_slide_images/7.jpg" , image_status_text : "Anrya", image_status_link: "default_slide_images/7.jpg"},	
				{image_link :"default_slide_images/8.jpg" , image_status_text : "Urban Village", image_status_link: "default_slide_images/8.jpg"},	
				{image_link :"default_slide_images/9.jpg" , image_status_text : "Nonkuphiri", image_status_link: "default_slide_images/9.jpg"},	
				{image_link :"default_slide_images/10.jpg" , image_status_text : "Know Your Voucher", image_status_link: "default_slide_images/10.jpg"}
			];

			
			//override provided data by using data from db; not necessary but fine
			
			if(data_from_db){
				
			}
			
			
			
			

			//logo image adding
			if(logo_image_url){
					document.getElementById('logo_container').style.backgroundImage='url('+logo_image_url+')';
					document.getElementById('logo_container').style.backgroundSize='auto 70px';
					document.getElementById('logo_container').style.backgroundRepeat='no-repeat';
					document.getElementById('logo_container').style.backgroundPosition='center';
			}
			
			//+++++++ apply enviroment data
			
			//how to link -- enter voucher
			document.getElementById('how_to_router_link').innerHTML = '<a href="' + hotspot_url + '">' + hotspot_url + '</a>';
							
			
			//	how to link -- status
			document.getElementById('how_to_check_balance').innerHTML = '<a href="' + hotspot_url + '/status">' + hotspot_url + '/status</a>';
			
			//	how to link -- login
			document.getElementById('how_to_log_in').innerHTML = '<a href="' + hotspot_url + '/login">' + hotspot_url + '/login</a>';
			
			//	how to link -- logout
			document.getElementById('how_to_log_out').innerHTML = '<a href="' + hotspot_url + '/logout">' + hotspot_url + '/logout</a>';
			//how to link -- buy
			document.getElementById('how_to_buy').innerHTML = '<a href="' + hotspot_transaction_server_url + '">Click <i style="color:green">BUY</i> Button to buy recharge voucher</a>';
			//how to link -- bottom text
			document.getElementById('how_to_bottom_text').innerHTML = how_to_bottom_text ;
			//free sites -- bottom text
			document.getElementById('free_sites_bottom_text').innerHTML = free_sites_bottom_text ;
			//free sites -- bottom text
			document.getElementById('notification_bottom_text').innerHTML = notification_bottom_text ;
			
			
			//++++++++++++++++++++ free links ++++++++++
			 //education_free_links  
			//education
			if(education_free_links){
			   	education_free_links.forEach(function(data){
					$('#education_free_links').append('<a href="'+data.link+'">'+data.text+'</a>');
				});
			   }
			
			//jobs
			//jobs_free_links
			if(jobs_free_links){
			   	jobs_free_links.forEach(function(data){
					$('#jobs_free_links').append('<a href="'+data.link+'">'+data.text+'</a>');
				});
			 }
			
			
			
			//++++++++++++++++++++ notifications   ++++++++++	 
			
			if(notifications_from_db){//if theres notifications
				
				//show announcement icon
				
				notifications_from_db.forEach(function(data, index){
					document.getElementById('notification_alert_icon').style.display='block';
					var notification_preview = data;//show preview of notification
					
					if(data.length > 10){//if notification is creater than 10 characters
						
						notification_preview = data.slice(0, 50)+'...';
					}
					
					
					$('#notification').append('<h2>ANNOUNCE' + (index + 1).toString()  + '</h2><br/><a href="#" onclick=\'this.innerHTML ="'+data+'"\'>' + notification_preview + '</a>');
				});
			}
					
			
			
			
                
			
		}
		fill_data_from_db();//start function	

			

			
			

		//++++++++++++++if page accessed from not router redirect

		if(!router_variables_array.login){//if login:true missing from url link//when not accesssed via hotspot running on router

		var go_to_home_page = confirm('Please enter this page by conneting to hotspot and Enter : '+hotspot_url+' in your browser to be able to enter voucher codes.\r\rDo you want to go to home page?');

			if(go_to_home_page){//open home page/transaction app
				if(hotspot_transaction_server_url){//if transact app link given
					window.open(hotspot_transaction_server_url, '_self');
				}
			}

		}
			
			
			
			
			
			
			
			
			
	    //+++++++++++++++++++++ wallpaper links +++++++++++++
         
        //wallpaper changer
        //wallpaper description
 			
        var current_image_content_tracker = 0;//image tracker
        
		//add wallpaper and link on page load	
        document.getElementById('walp_links').innerHTML = wall_link_description[0].image_status_text;
        document.getElementById('page_body').style.backgroundImage = 'url(' + wall_link_description[0].image_link + ')';
		
		//wallpaper size	
        document.getElementById('page_body').style.backgroundSize = '100vw 100vh';
        
        function walp_changer(){//slideshow
			
			//increment when function call
			current_image_content_tracker = current_image_content_tracker +1;
			
			//check if image tracker is still with provided image length rang
			if(current_image_content_tracker > wall_link_description.length -1){//if image tracker is over image array leng\\reset image traccker
			   	current_image_content_tracker = 0;
			   }
			
			document.getElementById('page_body').style.backgroundImage = 'url(' + wall_link_description[current_image_content_tracker].image_link + ')';

			document.getElementById('walp_links').innerHTML = wall_link_description[current_image_content_tracker].image_status_text;
			
       
        };
        
        
        var walp_interval =  setInterval(walp_changer, 6000);
        
        //++++++++++++++++++manual change
        
        document.getElementById('right_arrow_1').onclick = function (){//next image
			clearInterval(walp_interval);
			walp_changer();
        }
        
        document.getElementById('left_arrow_1').onclick = function (){//previous image
			clearInterval(walp_interval);
			
			current_image_content_tracker = current_image_content_tracker - 2;
			
			if(current_image_content_tracker < 0){
				
				current_image_content_tracker = wall_link_description.length -2 ;
			}
			
			walp_changer();

        } 
        
        
         document.getElementById('walp_links_container').onclick=function (){
			//alert(wall_link_description[current_image_content_tracker].image_status_link)
			 var image_text_link = wall_link_description[current_image_content_tracker].image_status_link;
			 
			 if(image_text_link){
			 	//alert(document.getElementById('walp_links').textContent);
			   window.open(wall_link_description[current_image_content_tracker].image_status_link);
			   
		 	}
		 }	
			
			
			
		//++++++++++++++++++++ hotspot stuff
		 
		function logout(){
			window.open(hotspot_url+'/login'); 
		 } 
			
		function balance(){
			window.open(hotspot_url+'/status');
		} 
		function buy(){
			window.open(hotspot_transaction_server_url);
		} 
		function search(){
			window.open('https://www.google.com/search?q='+document.getElementById('search').value);
		}
			
		
			
			



		</script>
	
	</body>
</html>


File: /line-awesome\css\line-awesome.css
/*!
 *  Line Awesome 1.1.0 by @icons_8 - https://icons8.com/line-awesome
 *  License - https://icons8.com/good-boy-license/ (Font: SIL OFL 1.1, CSS: MIT License)
 *
 * Made with love by Icons8 [ https://icons8.com/ ] using FontCustom [ https://github.com/FontCustom/fontcustom ]
 *
 * Contacts:
 *    [ https://icons8.com/contact ]
 *
 * Follow Icon8 on
 *    Twitter [ https://twitter.com/icons_8 ]
 *    Facebook [ https://www.facebook.com/Icons8 ]
 *    Google+ [ https://plus.google.com/+Icons8 ]
 *    GitHub [ https://github.com/icons8 ]
 */

@font-face {
  font-family: "LineAwesome";
  src: url("../fonts/line-awesome.eot?v=1.1.");
  src: url("../fonts/line-awesome.eot??v=1.1.#iefix") format("embedded-opentype"),
       url("../fonts/line-awesome.woff2?v=1.1.") format("woff2"),
       url("../fonts/line-awesome.woff?v=1.1.") format("woff"),
       url("../fonts/line-awesome.ttf?v=1.1.") format("truetype"),
       url("../fonts/line-awesome.svg?v=1.1.#fa") format("svg");
  font-weight: normal;
  font-style: normal;
}

@media screen and (-webkit-min-device-pixel-ratio:0) {
  @font-face {
    font-family: "LineAwesome";
    src: url("../fonts/line-awesome.svg?v=1.1.#fa") format("svg");
  }
}

/* Thanks to http://fontawesome.io @fontawesome and @davegandy */
.la {
    display: inline-block;
    font: normal normal normal 16px/1 "LineAwesome";
    font-size: inherit;
    text-decoration: inherit;
    text-rendering: optimizeLegibility;
    text-transform: none;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    font-smoothing: antialiased;
}
/* makes the font 33% larger relative to the icon container */
.la-lg {
    font-size: 1.33333333em;
    line-height: 0.75em;
    vertical-align: -15%;
}
.la-2x {
    font-size: 2em;
}
.la-3x {
    font-size: 3em;
}
.la-4x {
    font-size: 4em;
}
.la-5x {
    font-size: 5em;
}
.la-fw {
    width: 1.28571429em;
    text-align: center;
}
.la-ul {
    padding-left: 0;
    margin-left: 2.14285714em;
    list-style-type: none;
}
.la-ul > li {
    position: relative;
}
.la-li {
    position: absolute;
    left: -2.14285714em;
    width: 2.14285714em;
    top: 0.14285714em;
    text-align: center;
}
.la-li.la-lg {
    left: -1.85714286em;
}
.la-border {
    padding: .2em .25em .15em;
    border: solid 0.08em #eeeeee;
    border-radius: .1em;
}
.pull-right {
    float: right;
}
.pull-left {
    float: left;
}
.li.pull-left {
    margin-right: .3em;
}
.li.pull-right {
    margin-left: .3em;
}
.la-spin {
    -webkit-animation: fa-spin 2s infinite linear;
    animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(359deg);
        transform: rotate(359deg);
    }
}
@keyframes fa-spin {
    0% {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    100% {
        -webkit-transform: rotate(359deg);
        transform: rotate(359deg);
    }
}
.la-rotate-90 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
    -webkit-transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    transform: rotate(90deg);
}
.la-rotate-180 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
    -webkit-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    transform: rotate(180deg);
}
.la-rotate-270 {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
    -webkit-transform: rotate(270deg);
    -ms-transform: rotate(270deg);
    transform: rotate(270deg);
}
.la-flip-horizontal {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
    -webkit-transform: scale(-1, 1);
    -ms-transform: scale(-1, 1);
    transform: scale(-1, 1);
}
.la-flip-vertical {
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
    -webkit-transform: scale(1, -1);
    -ms-transform: scale(1, -1);
    transform: scale(1, -1);
}
:root .la-rotate-90,
:root .la-rotate-180,
:root .la-rotate-270,
:root .la-flip-horizontal,
:root .la-flip-vertical {
    filter: none;
}
.la-stack {
    position: relative;
    display: inline-block;
    width: 2em;
    height: 2em;
    line-height: 2em;
    vertical-align: middle;
}
.la-stack-1x,
.la-stack-2x {
    position: absolute;
    left: 0;
    width: 100%;
    text-align: center;
}
.la-stack-1x {
    line-height: inherit;
}
.la-stack-2x {
    font-size: 2em;
}
.la-inverse {
    color: #ffffff;
}
/* Thanks to http://fontawesome.io @fontawesome and @davegandy */

.la-500px:before { content: "\f100"; }
.la-adjust:before { content: "\f101"; }
.la-adn:before { content: "\f102"; }
.la-align-center:before { content: "\f103"; }
.la-align-justify:before { content: "\f104"; }
.la-align-left:before { content: "\f105"; }
.la-align-right:before { content: "\f106"; }
.la-amazon:before { content: "\f107"; }
.la-ambulance:before { content: "\f108"; }
.la-anchor:before { content: "\f109"; }
.la-android:before { content: "\f10a"; }
.la-angellist:before { content: "\f10b"; }
.la-angle-double-down:before { content: "\f10c"; }
.la-angle-double-left:before { content: "\f10d"; }
.la-angle-double-right:before { content: "\f10e"; }
.la-angle-double-up:before { content: "\f10f"; }
.la-angle-down:before { content: "\f110"; }
.la-angle-left:before { content: "\f111"; }
.la-angle-right:before { content: "\f112"; }
.la-angle-up:before { content: "\f113"; }
.la-apple:before { content: "\f114"; }
.la-archive:before { content: "\f115"; }
.la-area-chart:before { content: "\f116"; }
.la-arrow-circle-down:before { content: "\f117"; }
.la-arrow-circle-left:before { content: "\f118"; }
.la-arrow-circle-o-down:before { content: "\f119"; }
.la-arrow-circle-o-left:before { content: "\f11a"; }
.la-arrow-circle-o-right:before { content: "\f11b"; }
.la-arrow-circle-o-up:before { content: "\f11c"; }
.la-arrow-circle-right:before { content: "\f11d"; }
.la-arrow-circle-up:before { content: "\f11e"; }
.la-arrow-down:before { content: "\f11f"; }
.la-arrow-left:before { content: "\f120"; }
.la-arrow-right:before { content: "\f121"; }
.la-arrow-up:before { content: "\f122"; }
.la-arrows:before { content: "\f123"; }
.la-arrows-alt:before { content: "\f124"; }
.la-arrows-h:before { content: "\f125"; }
.la-arrows-v:before { content: "\f126"; }
.la-asterisk:before { content: "\f127"; }
.la-at:before { content: "\f128"; }
.la-automobile:before { content: "\f129"; }
.la-backward:before { content: "\f12a"; }
.la-balance-scale:before { content: "\f12b"; }
.la-ban:before { content: "\f12c"; }
.la-bank:before { content: "\f12d"; }
.la-bar-chart:before { content: "\f12e"; }
.la-bar-chart-o:before { content: "\f12f"; }
.la-barcode:before { content: "\f130"; }
.la-bars:before { content: "\f131"; }
.la-battery-0:before { content: "\f132"; }
.la-battery-1:before { content: "\f133"; }
.la-battery-2:before { content: "\f134"; }
.la-battery-3:before { content: "\f135"; }
.la-battery-4:before { content: "\f136"; }
.la-battery-empty:before { content: "\f137"; }
.la-battery-full:before { content: "\f138"; }
.la-battery-half:before { content: "\f139"; }
.la-battery-quarter:before { content: "\f13a"; }
.la-battery-three-quarters:before { content: "\f13b"; }
.la-bed:before { content: "\f13c"; }
.la-beer:before { content: "\f13d"; }
.la-behance:before { content: "\f13e"; }
.la-behance-square:before { content: "\f13f"; }
.la-bell:before { content: "\f140"; }
.la-bell-o:before { content: "\f141"; }
.la-bell-slash:before { content: "\f142"; }
.la-bell-slash-o:before { content: "\f143"; }
.la-bicycle:before { content: "\f144"; }
.la-binoculars:before { content: "\f145"; }
.la-birthday-cake:before { content: "\f146"; }
.la-bitbucket:before { content: "\f147"; }
.la-bitbucket-square:before { content: "\f148"; }
.la-bitcoin:before { content: "\f149"; }
.la-black-tie:before { content: "\f14a"; }
.la-bold:before { content: "\f14b"; }
.la-bolt:before { content: "\f14c"; }
.la-bomb:before { content: "\f14d"; }
.la-book:before { content: "\f14e"; }
.la-bookmark:before { content: "\f14f"; }
.la-bookmark-o:before { content: "\f150"; }
.la-briefcase:before { content: "\f151"; }
.la-btc:before { content: "\f152"; }
.la-bug:before { content: "\f153"; }
.la-building:before { content: "\f154"; }
.la-building-o:before { content: "\f155"; }
.la-bullhorn:before { content: "\f156"; }
.la-bullseye:before { content: "\f157"; }
.la-bus:before { content: "\f158"; }
.la-buysellads:before { content: "\f159"; }
.la-cab:before { content: "\f15a"; }
.la-calculator:before { content: "\f15b"; }
.la-calendar:before { content: "\f15c"; }
.la-calendar-check-o:before { content: "\f15d"; }
.la-calendar-minus-o:before { content: "\f15e"; }
.la-calendar-o:before { content: "\f15f"; }
.la-calendar-plus-o:before { content: "\f160"; }
.la-calendar-times-o:before { content: "\f161"; }
.la-camera:before { content: "\f162"; }
.la-camera-retro:before { content: "\f163"; }
.la-car:before { content: "\f164"; }
.la-caret-down:before { content: "\f165"; }
.la-caret-left:before { content: "\f166"; }
.la-caret-right:before { content: "\f167"; }
.la-caret-square-o-down:before, .la-toggle-down:before { content: "\f168"; }
.la-caret-square-o-left:before, .la-toggle-left:before { content: "\f169"; }
.la-caret-square-o-right:before, .la-toggle-right:before { content: "\f16a"; }
.la-caret-square-o-up:before, .la-toggle-up:before { content: "\f16b"; }
.la-caret-up:before { content: "\f16c"; }
.la-cart-arrow-down:before { content: "\f16d"; }
.la-cart-plus:before { content: "\f16e"; }
.la-cc:before { content: "\f16f"; }
.la-cc-amex:before { content: "\f170"; }
.la-cc-diners-club:before { content: "\f171"; }
.la-cc-discover:before { content: "\f172"; }
.la-cc-jcb:before { content: "\f173"; }
.la-cc-mastercard:before { content: "\f174"; }
.la-cc-paypal:before { content: "\f175"; }
.la-cc-stripe:before { content: "\f176"; }
.la-cc-visa:before { content: "\f177"; }
.la-certificate:before { content: "\f178"; }
.la-chain:before { content: "\f179"; }
.la-chain-broken:before { content: "\f17a"; }
.la-check:before { content: "\f17b"; }
.la-check-circle:before { content: "\f17c"; }
.la-check-circle-o:before { content: "\f17d"; }
.la-check-square:before { content: "\f17e"; }
.la-check-square-o:before { content: "\f17f"; }
.la-chevron-circle-down:before { content: "\f180"; }
.la-chevron-circle-left:before { content: "\f181"; }
.la-chevron-circle-right:before { content: "\f182"; }
.la-chevron-circle-up:before { content: "\f183"; }
.la-chevron-down:before { content: "\f184"; }
.la-chevron-left:before { content: "\f185"; }
.la-chevron-right:before { content: "\f186"; }
.la-chevron-up:before { content: "\f187"; }
.la-child:before { content: "\f188"; }
.la-chrome:before { content: "\f189"; }
.la-circle:before { content: "\f18a"; }
.la-circle-o:before { content: "\f18b"; }
.la-circle-o-notch:before { content: "\f18c"; }
.la-circle-thin:before { content: "\f18d"; }
.la-clipboard:before { content: "\f18e"; }
.la-clock-o:before { content: "\f18f"; }
.la-clone:before { content: "\f190"; }
.la-close:before { content: "\f191"; }
.la-cloud:before { content: "\f192"; }
.la-cloud-download:before { content: "\f193"; }
.la-cloud-upload:before { content: "\f194"; }
.la-cny:before { content: "\f195"; }
.la-code:before { content: "\f196"; }
.la-code-fork:before { content: "\f197"; }
.la-codepen:before { content: "\f198"; }
.la-coffee:before { content: "\f199"; }
.la-cog:before { content: "\f19a"; }
.la-cogs:before { content: "\f19b"; }
.la-columns:before { content: "\f19c"; }
.la-comment:before { content: "\f19d"; }
.la-comment-o:before { content: "\f19e"; }
.la-commenting:before { content: "\f19f"; }
.la-commenting-o:before { content: "\f1a0"; }
.la-comments:before { content: "\f1a1"; }
.la-comments-o:before { content: "\f1a2"; }
.la-compass:before { content: "\f1a3"; }
.la-compress:before { content: "\f1a4"; }
.la-connectdevelop:before { content: "\f1a5"; }
.la-contao:before { content: "\f1a6"; }
.la-copy:before { content: "\f1a7"; }
.la-copyright:before { content: "\f1a8"; }
.la-creative-commons:before { content: "\f1a9"; }
.la-credit-card:before { content: "\f1aa"; }
.la-crop:before { content: "\f1ab"; }
.la-crosshairs:before { content: "\f1ac"; }
.la-css3:before { content: "\f1ad"; }
.la-cube:before { content: "\f1ae"; }
.la-cubes:before { content: "\f1af"; }
.la-cut:before { content: "\f1b0"; }
.la-cutlery:before { content: "\f1b1"; }
.la-dashboard:before { content: "\f1b2"; }
.la-dashcube:before { content: "\f1b3"; }
.la-database:before { content: "\f1b4"; }
.la-dedent:before { content: "\f1b5"; }
.la-delicious:before { content: "\f1b6"; }
.la-desktop:before { content: "\f1b7"; }
.la-deviantart:before { content: "\f1b8"; }
.la-diamond:before { content: "\f1b9"; }
.la-digg:before { content: "\f1ba"; }
.la-dollar:before { content: "\f1bb"; }
.la-dot-circle-o:before { content: "\f1bc"; }
.la-download:before { content: "\f1bd"; }
.la-dribbble:before { content: "\f1be"; }
.la-dropbox:before { content: "\f1bf"; }
.la-drupal:before { content: "\f1c0"; }
.la-edit:before { content: "\f1c1"; }
.la-eject:before { content: "\f1c2"; }
.la-ellipsis-h:before { content: "\f1c3"; }
.la-ellipsis-v:before { content: "\f1c4"; }
.la-empire:before, .la-ge:before { content: "\f1c5"; }
.la-envelope:before { content: "\f1c6"; }
.la-envelope-o:before { content: "\f1c7"; }
.la-envelope-square:before { content: "\f1c8"; }
.la-eraser:before { content: "\f1c9"; }
.la-eur:before { content: "\f1ca"; }
.la-euro:before { content: "\f1cb"; }
.la-exchange:before { content: "\f1cc"; }
.la-exclamation:before { content: "\f1cd"; }
.la-exclamation-circle:before { content: "\f1ce"; }
.la-exclamation-triangle:before { content: "\f1cf"; }
.la-expand:before { content: "\f1d0"; }
.la-expeditedssl:before { content: "\f1d1"; }
.la-external-link:before { content: "\f1d2"; }
.la-external-link-square:before { content: "\f1d3"; }
.la-eye:before { content: "\f1d4"; }
.la-eye-slash:before { content: "\f1d5"; }
.la-eyedropper:before { content: "\f1d6"; }
.la-facebook:before, .la-facebook-f:before { content: "\f1d7"; }
.la-facebook-official:before { content: "\f1d8"; }
.la-facebook-square:before { content: "\f1d9"; }
.la-fast-backward:before { content: "\f1da"; }
.la-fast-forward:before { content: "\f1db"; }
.la-fax:before { content: "\f1dc"; }
.la-female:before { content: "\f1dd"; }
.la-fighter-jet:before { content: "\f1de"; }
.la-file:before { content: "\f1df"; }
.la-file-archive-o:before { content: "\f1e0"; }
.la-file-audio-o:before { content: "\f1e1"; }
.la-file-code-o:before { content: "\f1e2"; }
.la-file-excel-o:before { content: "\f1e3"; }
.la-file-image-o:before { content: "\f1e4"; }
.la-file-movie-o:before { content: "\f1e5"; }
.la-file-o:before { content: "\f1e6"; }
.la-file-pdf-o:before { content: "\f1e7"; }
.la-file-photo-o:before { content: "\f1e8"; }
.la-file-picture-o:before { content: "\f1e9"; }
.la-file-powerpoint-o:before { content: "\f1ea"; }
.la-file-sound-o:before { content: "\f1eb"; }
.la-file-text:before { content: "\f1ec"; }
.la-file-text-o:before { content: "\f1ed"; }
.la-file-video-o:before { content: "\f1ee"; }
.la-file-word-o:before { content: "\f1ef"; }
.la-file-zip-o:before { content: "\f1f0"; }
.la-files-o:before { content: "\f1f1"; }
.la-film:before { content: "\f1f2"; }
.la-filter:before { content: "\f1f3"; }
.la-fire:before { content: "\f1f4"; }
.la-fire-extinguisher:before { content: "\f1f5"; }
.la-firefox:before { content: "\f1f6"; }
.la-flag:before { content: "\f1f7"; }
.la-flag-checkered:before { content: "\f1f8"; }
.la-flag-o:before { content: "\f1f9"; }
.la-flash:before { content: "\f1fa"; }
.la-flask:before { content: "\f1fb"; }
.la-flickr:before { content: "\f1fc"; }
.la-floppy-o:before { content: "\f1fd"; }
.la-folder:before { content: "\f1fe"; }
.la-folder-o:before { content: "\f1ff"; }
.la-folder-open:before { content: "\f200"; }
.la-folder-open-o:before { content: "\f201"; }
.la-font:before { content: "\f202"; }
.la-fonticons:before { content: "\f203"; }
.la-forumbee:before { content: "\f204"; }
.la-forward:before { content: "\f205"; }
.la-foursquare:before { content: "\f206"; }
.la-frown-o:before { content: "\f207"; }
.la-futbol-o:before, .la-soccer-ball-o:before { content: "\f208"; }
.la-gamepad:before { content: "\f209"; }
.la-gavel:before { content: "\f20a"; }
.la-gbp:before { content: "\f20b"; }
.la-gear:before { content: "\f20c"; }
.la-gears:before { content: "\f20d"; }
.la-genderless:before { content: "\f20e"; }
.la-get-pocket:before { content: "\f20f"; }
.la-gg:before { content: "\f210"; }
.la-gg-circle:before { content: "\f211"; }
.la-gift:before { content: "\f212"; }
.la-git:before { content: "\f213"; }
.la-git-square:before { content: "\f214"; }
.la-github:before { content: "\f215"; }
.la-github-alt:before { content: "\f216"; }
.la-github-square:before { content: "\f217"; }
.la-glass:before { content: "\f218"; }
.la-globe:before { content: "\f219"; }
.la-google:before { content: "\f21a"; }
.la-google-plus:before { content: "\f21b"; }
.la-google-plus-square:before { content: "\f21c"; }
.la-google-wallet:before { content: "\f21d"; }
.la-graduation-cap:before { content: "\f21e"; }
.la-gratipay:before, .la-gittip:before { content: "\f21f"; }
.la-group:before { content: "\f220"; }
.la-h-square:before { content: "\f221"; }
.la-hacker-news:before { content: "\f222"; }
.la-hand-grab-o:before { content: "\f223"; }
.la-hand-lizard-o:before { content: "\f224"; }
.la-hand-o-down:before { content: "\f225"; }
.la-hand-o-left:before { content: "\f226"; }
.la-hand-o-right:before { content: "\f227"; }
.la-hand-o-up:before { content: "\f228"; }
.la-hand-paper-o:before { content: "\f229"; }
.la-hand-peace-o:before { content: "\f22a"; }
.la-hand-pointer-o:before { content: "\f22b"; }
.la-hand-rock-o:before { content: "\f22c"; }
.la-hand-scissors-o:before { content: "\f22d"; }
.la-hand-spock-o:before { content: "\f22e"; }
.la-hand-stop-o:before { content: "\f22f"; }
.la-hdd-o:before { content: "\f230"; }
.la-header:before { content: "\f231"; }
.la-headphones:before { content: "\f232"; }
.la-heart:before { content: "\f233"; }
.la-heart-o:before { content: "\f234"; }
.la-heartbeat:before { content: "\f235"; }
.la-history:before { content: "\f236"; }
.la-home:before { content: "\f237"; }
.la-hospital-o:before { content: "\f238"; }
.la-hotel:before { content: "\f239"; }
.la-hourglass:before { content: "\f23a"; }
.la-hourglass-1:before { content: "\f23b"; }
.la-hourglass-2:before { content: "\f23c"; }
.la-hourglass-3:before { content: "\f23d"; }
.la-hourglass-end:before { content: "\f23e"; }
.la-hourglass-half:before { content: "\f23f"; }
.la-hourglass-o:before { content: "\f240"; }
.la-hourglass-start:before { content: "\f241"; }
.la-houzz:before { content: "\f242"; }
.la-html5:before { content: "\f243"; }
.la-i-cursor:before { content: "\f244"; }
.la-ils:before { content: "\f245"; }
.la-image:before { content: "\f246"; }
.la-inbox:before { content: "\f247"; }
.la-indent:before { content: "\f248"; }
.la-industry:before { content: "\f249"; }
.la-info:before { content: "\f24a"; }
.la-info-circle:before { content: "\f24b"; }
.la-inr:before { content: "\f24c"; }
.la-instagram:before { content: "\f24d"; }
.la-institution:before { content: "\f24e"; }
.la-internet-explorer:before { content: "\f24f"; }
.la-ioxhost:before { content: "\f250"; }
.la-italic:before { content: "\f251"; }
.la-joomla:before { content: "\f252"; }
.la-jpy:before { content: "\f253"; }
.la-jsfiddle:before { content: "\f254"; }
.la-key:before { content: "\f255"; }
.la-keyboard-o:before { content: "\f256"; }
.la-krw:before { content: "\f257"; }
.la-language:before { content: "\f258"; }
.la-laptop:before { content: "\f259"; }
.la-lastfm:before { content: "\f25a"; }
.la-lastfm-square:before { content: "\f25b"; }
.la-leaf:before { content: "\f25c"; }
.la-leanpub:before { content: "\f25d"; }
.la-legal:before { content: "\f25e"; }
.la-lemon-o:before { content: "\f25f"; }
.la-level-down:before { content: "\f260"; }
.la-level-up:before { content: "\f261"; }
.la-life-bouy:before { content: "\f262"; }
.la-life-buoy:before { content: "\f263"; }
.la-life-ring:before, .la-support:before { content: "\f264"; }
.la-life-saver:before { content: "\f265"; }
.la-lightbulb-o:before { content: "\f266"; }
.la-line-chart:before { content: "\f267"; }
.la-link:before { content: "\f268"; }
.la-linkedin:before { content: "\f269"; }
.la-linkedin-square:before { content: "\f26a"; }
.la-linux:before { content: "\f26b"; }
.la-list:before { content: "\f26c"; }
.la-list-alt:before { content: "\f26d"; }
.la-list-ol:before { content: "\f26e"; }
.la-list-ul:before { content: "\f26f"; }
.la-location-arrow:before { content: "\f270"; }
.la-lock:before { content: "\f271"; }
.la-long-arrow-down:before { content: "\f272"; }
.la-long-arrow-left:before { content: "\f273"; }
.la-long-arrow-right:before { content: "\f274"; }
.la-long-arrow-up:before { content: "\f275"; }
.la-magic:before { content: "\f276"; }
.la-magnet:before { content: "\f277"; }
.la-mail-forward:before { content: "\f278"; }
.la-mail-reply:before { content: "\f279"; }
.la-mail-reply-all:before { content: "\f27a"; }
.la-male:before { content: "\f27b"; }
.la-map:before { content: "\f27c"; }
.la-map-marker:before { content: "\f27d"; }
.la-map-o:before { content: "\f27e"; }
.la-map-pin:before { content: "\f27f"; }
.la-map-signs:before { content: "\f280"; }
.la-mars:before { content: "\f281"; }
.la-mars-double:before { content: "\f282"; }
.la-mars-stroke:before { content: "\f283"; }
.la-mars-stroke-h:before { content: "\f284"; }
.la-mars-stroke-v:before { content: "\f285"; }
.la-maxcdn:before { content: "\f286"; }
.la-meanpath:before { content: "\f287"; }
.la-medium:before { content: "\f288"; }
.la-medkit:before { content: "\f289"; }
.la-meh-o:before { content: "\f28a"; }
.la-mercury:before { content: "\f28b"; }
.la-microphone:before { content: "\f28c"; }
.la-microphone-slash:before { content: "\f28d"; }
.la-minus:before { content: "\f28e"; }
.la-minus-circle:before { content: "\f28f"; }
.la-minus-square:before { content: "\f290"; }
.la-minus-square-o:before { content: "\f291"; }
.la-mobile:before { content: "\f292"; }
.la-mobile-phone:before { content: "\f293"; }
.la-money:before { content: "\f294"; }
.la-moon-o:before { content: "\f295"; }
.la-mortar-board:before { content: "\f296"; }
.la-motorcycle:before { content: "\f297"; }
.la-mouse-pointer:before { content: "\f298"; }
.la-music:before { content: "\f299"; }
.la-navicon:before { content: "\f29a"; }
.la-neuter:before { content: "\f29b"; }
.la-newspaper-o:before { content: "\f29c"; }
.la-object-group:before { content: "\f29d"; }
.la-object-ungroup:before { content: "\f29e"; }
.la-odnoklassniki:before { content: "\f29f"; }
.la-odnoklassniki-square:before { content: "\f2a0"; }
.la-opencart:before { content: "\f2a1"; }
.la-openid:before { content: "\f2a2"; }
.la-opera:before { content: "\f2a3"; }
.la-optin-monster:before { content: "\f2a4"; }
.la-outdent:before { content: "\f2a5"; }
.la-pagelines:before { content: "\f2a6"; }
.la-paint-brush:before { content: "\f2a7"; }
.la-paper-plane:before, .la-send:before { content: "\f2a8"; }
.la-paper-plane-o:before, .la-send-o:before { content: "\f2a9"; }
.la-paperclip:before { content: "\f2aa"; }
.la-paragraph:before { content: "\f2ab"; }
.la-paste:before { content: "\f2ac"; }
.la-pause:before { content: "\f2ad"; }
.la-paw:before { content: "\f2ae"; }
.la-paypal:before { content: "\f2af"; }
.la-pencil:before { content: "\f2b0"; }
.la-pencil-square:before { content: "\f2b1"; }
.la-pencil-square-o:before { content: "\f2b2"; }
.la-phone:before { content: "\f2b3"; }
.la-phone-square:before { content: "\f2b4"; }
.la-photo:before { content: "\f2b5"; }
.la-picture-o:before { content: "\f2b6"; }
.la-pie-chart:before { content: "\f2b7"; }
.la-pied-piper:before { content: "\f2b8"; }
.la-pied-piper-alt:before { content: "\f2b9"; }
.la-pinterest:before { content: "\f2ba"; }
.la-pinterest-p:before { content: "\f2bb"; }
.la-pinterest-square:before { content: "\f2bc"; }
.la-plane:before { content: "\f2bd"; }
.la-play:before { content: "\f2be"; }
.la-play-circle:before { content: "\f2bf"; }
.la-play-circle-o:before { content: "\f2c0"; }
.la-plug:before { content: "\f2c1"; }
.la-plus:before { content: "\f2c2"; }
.la-plus-circle:before { content: "\f2c3"; }
.la-plus-square:before { content: "\f2c4"; }
.la-plus-square-o:before { content: "\f2c5"; }
.la-power-off:before { content: "\f2c6"; }
.la-print:before { content: "\f2c7"; }
.la-puzzle-piece:before { content: "\f2c8"; }
.la-qq:before { content: "\f2c9"; }
.la-qrcode:before { content: "\f2ca"; }
.la-question:before { content: "\f2cb"; }
.la-question-circle:before { content: "\f2cc"; }
.la-quote-left:before { content: "\f2cd"; }
.la-quote-right:before { content: "\f2ce"; }
.la-ra:before { content: "\f2cf"; }
.la-random:before { content: "\f2d0"; }
.la-rebel:before { content: "\f2d1"; }
.la-recycle:before { content: "\f2d2"; }
.la-reddit:before { content: "\f2d3"; }
.la-reddit-square:before { content: "\f2d4"; }
.la-refresh:before { content: "\f2d5"; }
.la-registered:before { content: "\f2d6"; }
.la-renren:before { content: "\f2d7"; }
.la-reorder:before { content: "\f2d8"; }
.la-repeat:before { content: "\f2d9"; }
.la-reply:before { content: "\f2da"; }
.la-reply-all:before { content: "\f2db"; }
.la-retweet:before { content: "\f2dc"; }
.la-rmb:before { content: "\f2dd"; }
.la-road:before { content: "\f2de"; }
.la-rocket:before { content: "\f2df"; }
.la-rotate-left:before { content: "\f2e0"; }
.la-rotate-right:before { content: "\f2e1"; }
.la-rouble:before { content: "\f2e2"; }
.la-rss:before, .la-feed:before { content: "\f2e3"; }
.la-rss-square:before { content: "\f2e4"; }
.la-rub:before { content: "\f2e5"; }
.la-ruble:before { content: "\f2e6"; }
.la-rupee:before { content: "\f2e7"; }
.la-safari:before { content: "\f2e8"; }
.la-save:before { content: "\f2e9"; }
.la-scissors:before { content: "\f2ea"; }
.la-search:before { content: "\f2eb"; }
.la-search-minus:before { content: "\f2ec"; }
.la-search-plus:before { content: "\f2ed"; }
.la-sellsy:before { content: "\f2ee"; }
.la-server:before { content: "\f2ef"; }
.la-share:before { content: "\f2f0"; }
.la-share-alt:before { content: "\f2f1"; }
.la-share-alt-square:before { content: "\f2f2"; }
.la-share-square:before { content: "\f2f3"; }
.la-share-square-o:before { content: "\f2f4"; }
.la-shekel:before { content: "\f2f5"; }
.la-sheqel:before { content: "\f2f6"; }
.la-shield:before { content: "\f2f7"; }
.la-ship:before { content: "\f2f8"; }
.la-shirtsinbulk:before { content: "\f2f9"; }
.la-shopping-cart:before { content: "\f2fa"; }
.la-sign-in:before { content: "\f2fb"; }
.la-sign-out:before { content: "\f2fc"; }
.la-signal:before { content: "\f2fd"; }
.la-simplybuilt:before { content: "\f2fe"; }
.la-sitemap:before { content: "\f2ff"; }
.la-skyatlas:before { content: "\f300"; }
.la-skype:before { content: "\f301"; }
.la-slack:before { content: "\f302"; }
.la-sliders:before { content: "\f303"; }
.la-slideshare:before { content: "\f304"; }
.la-smile-o:before { content: "\f305"; }
.la-sort:before, .la-unsorted:before { content: "\f306"; }
.la-sort-alpha-asc:before { content: "\f307"; }
.la-sort-alpha-desc:before { content: "\f308"; }
.la-sort-amount-asc:before { content: "\f309"; }
.la-sort-amount-desc:before { content: "\f30a"; }
.la-sort-asc:before, .la-sort-up:before { content: "\f30b"; }
.la-sort-desc:before, .la-sort-down:before { content: "\f30c"; }
.la-sort-numeric-asc:before { content: "\f30d"; }
.la-sort-numeric-desc:before { content: "\f30e"; }
.la-soundcloud:before { content: "\f30f"; }
.la-space-shuttle:before { content: "\f310"; }
.la-spinner:before { content: "\f311"; }
.la-spoon:before { content: "\f312"; }
.la-spotify:before { content: "\f313"; }
.la-square:before { content: "\f314"; }
.la-square-o:before { content: "\f315"; }
.la-stack-exchange:before { content: "\f316"; }
.la-stack-overflow:before { content: "\f317"; }
.la-star:before { content: "\f318"; }
.la-star-half:before { content: "\f319"; }
.la-star-half-o:before, .la-star-half-full:before, .la-star-half-empty:before { content: "\f31a"; }
.la-star-o:before { content: "\f31b"; }
.la-steam:before { content: "\f31c"; }
.la-steam-square:before { content: "\f31d"; }
.la-step-backward:before { content: "\f31e"; }
.la-step-forward:before { content: "\f31f"; }
.la-stethoscope:before { content: "\f320"; }
.la-sticky-note:before { content: "\f321"; }
.la-sticky-note-o:before { content: "\f322"; }
.la-stop:before { content: "\f323"; }
.la-street-view:before { content: "\f324"; }
.la-strikethrough:before { content: "\f325"; }
.la-stumbleupon:before { content: "\f326"; }
.la-stumbleupon-circle:before { content: "\f327"; }
.la-subscript:before { content: "\f328"; }
.la-subway:before { content: "\f329"; }
.la-suitcase:before { content: "\f32a"; }
.la-sun-o:before { content: "\f32b"; }
.la-superscript:before { content: "\f32c"; }
.la-table:before { content: "\f32d"; }
.la-tablet:before { content: "\f32e"; }
.la-tachometer:before { content: "\f32f"; }
.la-tag:before { content: "\f330"; }
.la-tags:before { content: "\f331"; }
.la-tasks:before { content: "\f332"; }
.la-taxi:before { content: "\f333"; }
.la-television:before, .la-tv:before { content: "\f334"; }
.la-tencent-weibo:before { content: "\f335"; }
.la-terminal:before { content: "\f336"; }
.la-text-height:before { content: "\f337"; }
.la-text-width:before { content: "\f338"; }
.la-th:before { content: "\f339"; }
.la-th-large:before { content: "\f33a"; }
.la-th-list:before { content: "\f33b"; }
.la-thumb-tack:before { content: "\f33c"; }
.la-thumbs-down:before { content: "\f33d"; }
.la-thumbs-o-down:before { content: "\f33e"; }
.la-thumbs-o-up:before { content: "\f33f"; }
.la-thumbs-up:before { content: "\f340"; }
.la-ticket:before { content: "\f341"; }
.la-times:before, .la-remove:before { content: "\f342"; }
.la-times-circle:before { content: "\f343"; }
.la-times-circle-o:before { content: "\f344"; }
.la-tint:before { content: "\f345"; }
.la-toggle-off:before { content: "\f346"; }
.la-toggle-on:before { content: "\f347"; }
.la-trademark:before { content: "\f348"; }
.la-train:before { content: "\f349"; }
.la-transgender:before, .la-intersex:before { content: "\f34a"; }
.la-transgender-alt:before { content: "\f34b"; }
.la-trash:before { content: "\f34c"; }
.la-trash-o:before { content: "\f34d"; }
.la-tree:before { content: "\f34e"; }
.la-trello:before { content: "\f34f"; }
.la-tripadvisor:before { content: "\f350"; }
.la-trophy:before { content: "\f351"; }
.la-truck:before { content: "\f352"; }
.la-try:before { content: "\f353"; }
.la-tty:before { content: "\f354"; }
.la-tumblr:before { content: "\f355"; }
.la-tumblr-square:before { content: "\f356"; }
.la-turkish-lira:before { content: "\f357"; }
.la-twitch:before { content: "\f358"; }
.la-twitter:before { content: "\f359"; }
.la-twitter-square:before { content: "\f35a"; }
.la-umbrella:before { content: "\f35b"; }
.la-underline:before { content: "\f35c"; }
.la-undo:before { content: "\f35d"; }
.la-university:before { content: "\f35e"; }
.la-unlink:before { content: "\f35f"; }
.la-unlock:before { content: "\f360"; }
.la-unlock-alt:before { content: "\f361"; }
.la-upload:before { content: "\f362"; }
.la-usd:before { content: "\f363"; }
.la-user:before { content: "\f364"; }
.la-user-md:before { content: "\f365"; }
.la-user-plus:before { content: "\f366"; }
.la-user-secret:before { content: "\f367"; }
.la-user-times:before { content: "\f368"; }
.la-users:before { content: "\f369"; }
.la-venus:before { content: "\f36a"; }
.la-venus-double:before { content: "\f36b"; }
.la-venus-mars:before { content: "\f36c"; }
.la-viacoin:before { content: "\f36d"; }
.la-video-camera:before { content: "\f36e"; }
.la-vimeo:before { content: "\f36f"; }
.la-vimeo-square:before { content: "\f370"; }
.la-vine:before { content: "\f371"; }
.la-vk:before { content: "\f372"; }
.la-volume-down:before { content: "\f373"; }
.la-volume-off:before { content: "\f374"; }
.la-volume-up:before { content: "\f375"; }
.la-warning:before { content: "\f376"; }
.la-wechat:before { content: "\f377"; }
.la-weibo:before { content: "\f378"; }
.la-weixin:before { content: "\f379"; }
.la-whatsapp:before { content: "\f37a"; }
.la-wheelchair:before { content: "\f37b"; }
.la-wifi:before { content: "\f37c"; }
.la-wikipedia-w:before { content: "\f37d"; }
.la-windows:before { content: "\f37e"; }
.la-won:before { content: "\f37f"; }
.la-wordpress:before { content: "\f380"; }
.la-wrench:before { content: "\f381"; }
.la-xing:before { content: "\f382"; }
.la-xing-square:before { content: "\f383"; }
.la-y-combinator:before { content: "\f384"; }
.la-y-combinator-square:before { content: "\f385"; }
.la-yahoo:before { content: "\f386"; }
.la-yc:before { content: "\f387"; }
.la-yc-square:before { content: "\f388"; }
.la-yelp:before { content: "\f389"; }
.la-yen:before { content: "\f38a"; }
.la-youtube:before { content: "\f38b"; }
.la-youtube-play:before { content: "\f38c"; }
.la-youtube-square:before { content: "\f38d"; }

File: /md5.js
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


File: /qs.js
(function () {
  'use strict';

  // Array.isArray() polyfill
  if (!Array.isArray) {
    Array.isArray = function (arg) {
      return Object.prototype.toString.call(arg) === '[object Array]';
    };
  }

  // Main object that will be exported
  var qs = {

    // Function to parse query string and return an object
    get: function () {

      // Capture query string and initialize new object
      var query = window.location.search;
      var obj = {};

      // If no query string, return empty object
      if (query === '') return obj;

      // Remove the '?' at front of query string
      query = query.slice(1);

      // Split the query string into key/value pairs (ampersand-separated)
      query = query.split('&');

      // Loop through each key/value pair
      query.map(function (part) {
        var key;
        var value;

        // Split each key/value pair into their separate parts
        part = part.split('=');
        key = part[0];
        value = part[1];

        // If the key doesn't exist yet, set it
        if (!obj[key]) {
          obj[key] = value;
        } else {

          // If it does already exist...

          // If it's not an array, make it an array
          if (!Array.isArray(obj[key])) {
            obj[key] = [obj[key]];
          }

          // Push the new value to the key's array
          obj[key].push(value);
        }
      });

      // Return the query string object
      return obj;
    },
  };

  // Make sure we're in a browser
  if (window) {

    // Make sure we're not overwriting the qs key
    if (!window.qs) {
      window.qs = qs;
    } else {
      throw new Error('Error bootstrapping qs: window.qs already set.');
    }
  }
})();

File: /README.md
# mikrotik-hotspot-external-login-page-none-PHP
Mikrotik External hosted login page

#Instructions
this page is adoptation of full featured hotspot transaction server (it runs on nodjs):  github.com/Tsehla/strwify_voucher_transaction_auto_management

1)This page can run on any html server, but you will have to change details within the index.html to match yours

2) in your mikrotik router login.html #add this just before <body> tag
  
  <script type="text/javascript">//checks for internet connection//en if available show external login//if not available show default mikrotik

	if(navigator.onLine){
		window.open('http://EXTERNAL-HOTSPOT-LINK/index.html?login=true&error=$(error)&link-login-only=$(link-login-only)&link-orig=$(link-orig)&chap-id=$(chap-id)&chap-challenge=$(chap-challenge)&link-orig-esc=$(link-orig-esc)&mac-esc=$(mac-esc)&username=$(username)', '_self');//open link where hotspot is at  
	}
	
</script>

OR just upload this page to you mikrotik router :

https://github.com/Tsehla/mikrotik-hotspot-external-login-page-none-PHP/tree/master/hospot_login_page

change : http://EXTERNAL-HOTSPOT-LINK/index.html to url of were you have index.html at


#bug note

#currently this page does not work with Hotspot authentication method of [ Http-chap ] best use [ http-pap ]


