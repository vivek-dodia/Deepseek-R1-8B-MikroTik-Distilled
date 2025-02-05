# Repository Information
Name: Mikrotik-Theme

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-Theme/
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
    │   │       ├── pack-ceda0cd6d15db6c66dd20eb03ebcbea0555ff122.idx
    │   │       └── pack-ceda0cd6d15db6c66dd20eb03ebcbea0555ff122.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── alogin.html
    ├── error.html
    ├── errors.txt
    ├── fonts/
    │   ├── maagkramp.woff
    │   └── VarelaRound-Regular.otf
    ├── images/
    │   └── Thumbs.db
    ├── LICENSE
    ├── login.html
    ├── logout.html
    ├── md5.js
    ├── radvert.html
    ├── readme.md
    ├── redirect.html
    ├── rlogin.html
    ├── screenshots/
    ├── status.html
    └── style.css


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
	url = https://github.com/shirshak55/Mikrotik-Theme.git
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
0000000000000000000000000000000000000000 cabb8ed4ca4b9c484f98963a98ecd4acb9442dce vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/shirshak55/Mikrotik-Theme.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 cabb8ed4ca4b9c484f98963a98ecd4acb9442dce vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/shirshak55/Mikrotik-Theme.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 cabb8ed4ca4b9c484f98963a98ecd4acb9442dce vivek-dodia <vivek.dodia@icloud.com> 1738606035 -0500	clone: from https://github.com/shirshak55/Mikrotik-Theme.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
cabb8ed4ca4b9c484f98963a98ecd4acb9442dce refs/remotes/origin/master


File: /.git\refs\heads\master
cabb8ed4ca4b9c484f98963a98ecd4acb9442dce


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /alogin.html
<html>
<head>
<title>Kathmandu University Free Wifi</title>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
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

	You are logged in Marpha Cyber Redirection
<br>
	If nothing is happening, click <a href="$(link-redirect)">here</a>
	<br>
Thanks for staying with US.

Redirector Created by Shirshak

<table width="100%" height="100%">
<tr>
    <td align="center" valign="middle">
    You are logged in at Kathmandu University Free Wifi
    <br><br>
    If nothing happens, click <a href="$(link-redirect)">here</a> to go to your site</td>
</tr>
</table>

</body>
</html>


File: /error.html
<html>
<head>
<title>Kathmandu University Free Wifi</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
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
</head>
<body>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
There is some ERROR : $(error)<br>
<br>
Please Login again from this link : <a href="$(link-login)">$(link-login)</a>

<br>
If you think there is problem contact ISMS at Kathmandu University
</td>
</tr>
</table>
</body>
</html>

File: /errors.txt
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

internal-error = Internal error ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = Configuration error ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Uou are not logged in (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = Cannot assign IP because of full ip pool

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = Hotspot service is sutting down

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = You are not allowed to use more than one session

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = session limit reached ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = Invalid username ($(username)): this MAC address is not yours

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

chap-missing = Please enable Javascript because we use it for security reason or try again

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = Invalid Username or Password

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = User $(username) is not allowed to log in from this MAC address

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = User $(username) has reached uptime limit
traffic-limit = User $(username) has reached traffic limit

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server is not responding

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = Already authorizing, retry later

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /LICENSE
MIT License

Copyright (c) 2017 Shirshak Bajgain

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


File: /login.html
<!doctype html>
<html lang="en-US" prefix="og: http://ogp.me/ns#">

<head>
    <title>Kathmandu University Free Wifi</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="style.css" type="text/css" />
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


    <body>
        <div class="layout">
            <header>
                <div id="top" class="top">
                    <div class="headerwrap">
                        <div class="logo">
                            <a href="/">
                                <span style="color:green;">K</span>U
                                <span>
                                    <span style="color:yellow"> Wifi</span>
                                </span>
                            </a>
                        </div>
                    </div>
                    <div style="clear:both;"></div>

                </div>
                <div style="clear:both;"></div>
                <div class="separator">
                    <span class="s1"></span>
                    <span class="s2"></span>
                    <span class="s3"></span>
                    <span class="s4"></span>
                </div>
                <div style="clear:both;"></div>

            </header>


            <div class="pagewrap">



                <div class="grid group">

                    <div class=" grid-2">
                        <div class="module">

                            <h2>Login To Acess Internet</h2>
                            <hr>

                            <p>$(if error)$(error)$(endif)</p>

                            <form name="login" class="respond userloginform" action="$(link-login-only)" method="post"
        $(if chap-id) onSubmit="return doLogin()" $(endif)>

                                <input type="hidden" name="dst" value="$(link-orig)" />
                                <input type="hidden" name="popup" value="true" />

                                <div class="formdiv">
                                    <label for="username">Username</label>
                                    <input name="username" type="text" value="$(username)" />
                                </div>

                                <div class="formdiv">
                                    <label for="password">Password</label>
                                    <input name="password" type="password"/>
                                </div>

                                <div class="buttons">
                                    <input type="submit" class="button" value="Login"  />
                                </div>

                            </form>
                            <hr/>

                        </div>
                    </div>

                    <div class="grid-3">
                        <div class="module">

                          <h2>Our Details</h2>
                            <ul>
                           <li>ISMS</li>
                                <hr/>
                        </div>
                    </div>

                </div>

            </div>

        </div>

    </body>
<script type="text/javascript">
<!--
  document.login.username.focus();
//-->
</script>
</body>
</html>


File: /logout.html
<!doctype html>
<html lang="en-US" prefix="og: http://ogp.me/ns#">

<head>


    <title>Status | Kathmandu University Free Wifi</title>

    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />


    $(if refresh-timeout)
    <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
    $(endif)


    <link rel="stylesheet" href="style.css" type="text/css" />

</head>

<body>



    <body>
        <div class="layout">
            <header>
                <div id="top" class="top">
                    <div class="headerwrap">
                        <div class="logo">
                            <a href="/">
                                <span style="color:green;">K</span>U
                                <span>
                                    <span style="color:yellow"> Wifi</span>
                                </span>
                            </a>
                        </div>
                    </div>
                    <div style="clear:both;"></div>

                </div>
                <div style="clear:both;"></div>
                <div class="separator">
                    <span class="s1"></span>
                    <span class="s2"></span>
                    <span class="s3"></span>
                    <span class="s4"></span>
                </div>
                <div style="clear:both;"></div>

            </header>



            <div class="pagewrap">



                <div class="grid group">

                    <div class=" grid-1-1">
                        <div class="module">

                            <h2>Logged Out. Statistics :</h2>
                            <hr>

                            <p>$(if error)$(error)$(endif)</p>

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
<b>You have just logged out</b> <br><br>
<table class="tabula" border="1">
<tr><td align="right">User name</td><td>$(username)</td></tr>
<tr><td align="right">IP address</td><td>$(ip)</td></tr>
<tr><td align="right">Session time</td><td>$(uptime)</td></tr>
$(if session-time-left)
<tr><td align="right">time left</td><td>$(session-time-left)</td></tr>
$(endif)
<tr><td align="right">bytes up/down:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
<input type="submit" class="button" value="log in">
</form>
</table>




                        </div>
                    </div>



                </div>

            </div>

        </div>


    </body>


    <script type="text/javascript">
    <!--
    document.login.username.focus();
    //-->
    </script>
</body>

</html>


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


File: /radvert.html
<html>
<head>
<title>Kathmandu University Advertisement</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
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
	Advertisement.
	<br><br>
	If nothing happens, open
	<a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
	manually.
	</td>
</tr>
</table>
</body>
</html>


File: /readme.md
# Beautiful Theme For Mikrotik Hotspot
* Theme made by Shirshak for mikrotik router. If you like it use it. If you find any problem you can post issue on issue tab . I used it on various mikrotik routers. Please test it before deploying.

## Installation
* Open winbox and login to your mikrotik router.
* Remote the screenshot folder as it is useless for mikrotik
* Open the filesystem and upload this theme. 
* Check your hotspot page.

## Customization
You may want to customize the text etc. You can just change theme text and it is simple HTML.

## Contribution
PR are welcome and I am happy to merge any PR.

## Contributors
Here are list of kind people who have significantly contributed this project.

1. Jonas Westerholm

## Licence
MIT

## Contributing
* I don't want to lie but I will only update this project when somebody find a problem. And I am not financially strong to support these project as I don't have time. However I can give you paid support. For that lets discuss `bloggervista@gmail.com`
* This doesn't mean I don't care about it. I will keep updating if I find any problem.

## Security
If you discover any security related issue, please email `bloggervista@gmail.com` .

## Donation
Considering the hours spend on developing this theme and you might have used it on production I accept the donation. Doner's name will be written on this repo as a mark of apperciation. I do accept cards payment, paypal but I am not writing it here. If you like to donate kindly ping me at `bloggervista@gmail.com` . 
If you are bitcoin user you can send me donations at blockchain `1NJb7cqYqP3nbR5WDjdaVvaduXfg8KEsHG` or `ether` at `0xA583445Acf22604219037D31f2D163B877DAad08`


File: /redirect.html
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>


File: /rlogin.html
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
</head>
<body>
</body>
</html>


File: /status.html
<!doctype html>
<html lang="en-US" prefix="og: http://ogp.me/ns#">

<head>


    <title>Status | Kathmandu Univerisity Free Wifi</title>

$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)

    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />


    $(if refresh-timeout)
    <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
    $(endif)



    <link rel="stylesheet" href="style.css" type="text/css" />





<script language="JavaScript">

function readablizeBytes(bytes) {
var s = ['bytes', 'kb', 'MB', 'GB', 'TB', 'PB'];
var e = Math.floor(Math.log(bytes)/Math.log(1024));
return (bytes/Math.pow(1024, Math.floor(e))).toFixed(2)+" "+s[e];
}

</script>

</head>

<body>



    <body>
        <div class="layout">
                        <header>
                <div id="top" class="top">
                    <div class="headerwrap">
                        <div class="logo">
                            <a href="/">
                                <span style="color:green;">K</span>U
                                <span>
                                    <span style="color:yellow"> Wifi</span>
                                </span>
                            </a>
                        </div>
                    </div>
                    <div style="clear:both;"></div>

                </div>
                <div style="clear:both;"></div>
                <div class="separator">
                    <span class="s1"></span>
                    <span class="s2"></span>
                    <span class="s3"></span>
                    <span class="s4"></span>
                </div>
                <div style="clear:both;"></div>

            </header>



            <div class="pagewrap">



                <div class="grid group">

                    <div class=" grid-1-1">
                        <div class="module">

                            <h2>Status:</h2>
                            <hr>
                            $(if link-orig)
                            <p>Your requested URL is <a href=" $(link-orig) ">this</a>. </p>
                            $(endif)

                            <p>$(if error)$(error)$(endif)</p>

<table border="1" class="tabula">
$(if login-by == 'trial')
    <br><div style="text-align: center;">Welcome trial user!</div><br>
$(elif login-by != 'mac')
    <br><div style="text-align: center;"><h1>Welcome $(username)!</h1></div><br>
$(endif)
    <tr><td align="center">This Session bytes up/down</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
$(if uptime)
    <tr><td align="center">This Session connected time </td><td>$(uptime)</td></tr>
$(endif)

$(if session-time-left)
    <tr><td align="center">Your Time left:</td><td>$(session-time-left)</td></tr>
$(endif)

$(if remain-bytes-out)
<tr><td align="center">Megabytes Remaining:</td><td><script language="JavaScript">document.write(readablizeBytes($(remain-bytes-out)));</script></td></tr>
$(endif)

$(if blocked == 'yes')
    <tr><td align="center">status:</td><td><div style="color: #FF8080">
<a href="$(link-advert)" target="hotspot_advert">advertisement</a> required</div></td></tr>
$(elif refresh-timeout)
    <tr><td align="center">status refresh:</td><td>$(refresh-timeout)</td></tr>
$(endif)
</table>

<a href="logout"><input type="submit" class="button" value="log off"></a>
<br><br>
<a href="logout?erase-cookie=true"><input type="submit" class="button" value="log off full"></a>
                            <hr/>

<h2>Your Information</h2>
<table>
    $(if login-by)
    <tr><td align="center">Logged in By:</td><td>$(login-by)</td></tr>
    $(endif)

    $(if mac)
    <tr><td align="center">Mac Address : </td><td>$(mac)</td></tr>
    $(endif)

    $(if ip)
    <tr><td align="center">Ip Address : </td><td>$(ip)</td></tr>
    $(endif)
</table>

                        </div>
                    </div>



                </div>

            </div>

        </div>


    </body>


</body>

</html>


File: /style.css
/*
This THeme is Designed by Shirshak. No modification should be made and no content should be copied. If you are fool than who can stop you anyway .. So if you are mad and crazy than do whatever you like . But if you are wise you will surely understand copy right yeah?
*/
@font-face {
    font-family:maagkramp;
    font-style:normal;
    font-weight:400;
    src:local('maagkramp'), local('maagkramp'), url(fonts/maagkramp.woff) format('woff')
}
@font-face {
    font-family:'Varela Round';
    font-style:normal;
    font-weight:400;
    src:local('Varela Round'), local('Varela Round'), url('fonts/VarelaRound-Regular.otf') format('opentype')
}
body {

    font-family:'Varela Round';
    font-size:16px;
    color:#333;
    line-height:1.4
}
a {
    color:#0a2a91
}
a:focus, a:hover {
    color:#2445ae
}
a:active {
    color:#000
}
.heading, h1, h2, h3, h4, h5, h6 {
    margin:0 0 10px;
    padding:0;
    font-family:'Whitney Cond A', 'Whitney Cond B', ronnia-condensed, 'Varela Round';
    font-weight:700;
    font-style:normal;
    line-height:1.1
}
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    color:#111
}
.h1, h1 {
    font-size:32px;
    margin:0
}
.h2, h2 {
    font-size:24px;
    margin:0
}
b, strong {
    font-weight:700
}
.explanation, blockquote {
    padding:10px 10px 10px 15px;
    margin:0 0 20px;
    background:#eee;
    border-left:6px solid #859ce6
}
.explanation p:last-child, blockquote p:last-child {
    margin:0
}
.explanation {
    padding:20px!important;
    border-left-color:orange
}
.expire-message p {
    font-size:11px!important;
    color:red!important;
    margin:0 0 5px!important
}
hr {
    border:0;
    height:1px;
    background:-moz-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, .5), rgba(0, 0, 0, 0));
    background:-o-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, .5), rgba(0, 0, 0, 0));
    background:-webkit-linear-gradient(left, rgba(0, 0, 0, 0), rgba(0, 0, 0, .5), rgba(0, 0, 0, 0));
    background:linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, .5), rgba(0, 0, 0, 0));
    margin:35px 0 33px
}
@media screen {
    *, :after, :before {
        -webkit-box-sizing:border-box;
        -moz-box-sizing:border-box;
        box-sizing:border-box
    }
    a {
        text-decoration:none
    }
    article, aside, details, figcaption, figure, footer, header, hgroup, nav, section, summary {
        display:block
    }
    html {
        font-size:100%;
        -webkit-text-size-adjust:100%;
        -ms-text-size-adjust:100%;
        margin:0;
        padding:0
    }
    button, html, input, select, textarea {
        font-family:'Varela Round',sans-serif;
    }
    images {
        border:0;
        -ms-interpolation-mode:bicubic;
        max-width:100%;
        height:auto!important
    }
    svg:not(:root) {
        overflow:hidden
    }
    form {
        margin:0
    }
    fieldset {
        border:0;
        margin:0;
        padding:0
    }
    legend {
        border:0;
        padding:0;
        white-space:normal;
        *margin-left:-7px
    }
    button, input, select, textarea {
        font-size:120%;
        margin:0;
        vertical-align:baseline;
        *vertical-align:middle
    }
    button, input {
        line-height:normal
    }
    button, html input[type=button], input[type=reset], input[type=submit] {
        -webkit-appearance:button;
        cursor:pointer
    }
    button[disabled], input[disabled] {
        cursor:default
    }
    input[type=checkbox], input[type=radio] {
        padding:0
    }
    input[type=search] {
        -webkit-appearance:textfield
    }
    input[type=search]::-webkit-search-cancel-button, input[type=search]::-webkit-search-decoration {
        -webkit-appearance:none
    }
    button::-moz-focus-inner, input::-moz-focus-inner {
        border:0;
        padding:0
    }
    textarea {
        overflow:auto;
        vertical-align:top
    }
    table {
        border-collapse:collapse;
        border-spacing:0;
        width:100%;
        margin:0 0 20px
    }
    table th {
        text-align:left
    }
    table td, table th {
        border:3px solid #ccc;
        padding:5px
    }
    .group:after {
        content:"";
        display:table;
        clear:both
    }
    p:empty {
        display:none
    }
    .post-info table td, .post-info table th {
        border:0
    }
    #rcp_submit, .button, .button1, .button2 {
        border:0;
        outline:0;
        background:#53c74e;
        box-shadow:1px 0 1px #20912e, 0 1px 1px #38b150, 2px 1px 1px #209132, 1px 2px 1px #47b138, 3px 2px 1px #209125, 2px 3px 1px #50b138, 4px 3px 1px #259120, 3px 4px 1px #38b142, 5px 4px 1px #379120, 4px 5px 1px #38b138, 6px 5px 1px #209129;
        color:#fff;
        white-space:nowrap;
        font-family:'Varela Round';
        padding:9px 16px;
        position:relative;
        top:-5px;
        border-radius:3px
    }
    #rcp_submit:focus, #rcp_submit:hover, .button1:hover, .button2:active, .button2:hover, .button:focus, .button:hover {
        color:#fff;
        background:#50b43d
    }
    #rcp_submit:active, .button1:active, .button2:active, .button:active {
        box-shadow:1px 0 1px #209120, 0 1px 1px #42b138, 2px 1px 1px #329120, 1px 2px 1px #5ab138, 3px 2px 1px #329120;
        top:-2px;
        left:3px
    }
    input[type=email], input[type=password], input[type=search], input[type=text], input[type=url], select, textarea {
        font-family:'Varela Round',"Whitney SSm A", "Whitney SSm B", ff-meta-web-pro, sans-serif;
        padding:6px 0 6px 6px;
        outline:0 none;
        word-break:normal;
        border:6px solid #eee;
        border-radius:0;
        background:none repeat scroll 0 0 #F9FFFF
    }
    textarea {
        width:100%
    }
    input[type=radio] {
        float:left;
        position:relative;
        top:3px;
        width:10%
    }
    .grid {
        padding:20px 0 20px 20px
    }
    .grid-1-1 {
        width:100%
    }
    .grid-2 {
        width:60%
    }
    .grid-3 {
        width:35%
    }
    [class*=grid-] {
        float:left;
        padding-right:20px;
        position:relative
    }
    .gridswitch[class*=grid-] {
        float:right;
        padding-right:0;
        padding-left:20px
    }
    body {
        background:#eee url(images/bg.png);
        margin:0
    }
    .separator span {
        display:block;
        height:15px;
        width:25%;
        float:left
    }
    .s1 {
        background:#f3a01e
    }
    .s2 {
        background:#d05d2a;
        left:25%
    }
    .s3 {
        background:#9dc425;
        left:50%
    }
    .s4 {
        background:#4b8db5;
        left:75%
    }
    .top {
        background:#ccc;
        background-color:rgba(90, 88, 88, .24)
    }
    .headerwrap {
        width:70%;
        margin:0 auto
    }
    .logo {
        width:560px;
        margin:0 auto
    }
    .formdiv input, .formdiv select {
        margin-bottom:10px;
        width:60%
    }
    .formdiv label {
        width:30%;
        display:inline-block;
        float:left;
        font-weight:700
    }
    .logo a {
        display:block;
        font-family:maagkramp, sans-serif;
        text-decoration:none;
        font-weight:700;
        color:#bb3f3f;
        font-size:350%
    }
    .pagewrap {
        background:#eaeaea;
        width:80%;
        margin:0 auto;
        position:relative;
        padding-top:20px
    }
    .pagewrap:after, .pagewrap:before {
        content:"";
        position:absolute;
        top:6px;
        left:6px;
        width:100%;
        height:100%;
        background:#989898;
        z-index:-1
    }
    .pagewrap:before {
        top:12px;
        left:12px;
        background:#6c6666
    }
    .module {
        overflow:hidden;
        background:#fff;
        padding:45px 40px 30px;
        clear:both;
        border:1px solid #ccc;
        margin:0 0 20px;
        position:relative
    }
    .module:before {
        content:"";
        position:absolute;
        font-size:11px;
        text-transform:uppercase;
        top:0;
        left:0;
        width:100%;
        padding:1px 10px 0;
        color:#fff
    }
    .module-ad images {
        display:block;
        max-width:100%;
        height:auto!important;
        margin:-1px auto 0
    }
    .module ul {
        list-style-type:square;
        margin:0;
        padding:0 0 0 20px
    }
    .module li {
        border-bottom:0 solid #e6e6e6;
        line-height:1.3em;
        text-decoration:none;
        margin:0;
        padding:4px 0 0
    }
    ::-webkit-scrollbar-thumb:horizontal {
        height:10px;
        background-color:#00a5f0
    }
    ::-webkit-scrollbar-thumb:vertical {
        width:10px;
        background-color:#00a5f0;
        -webkit-box-shadow:1px 1px 4px rgba(0, 0, 0, .16);
        -moz-box-shadow:1px 1px 4px rgba(0, 0, 0, .16);
        box-shadow:1px 1px 4px rgba(0, 0, 0, .16)
    }
    ::-webkit-scrollbar {
        width:15px;
        height:15px;
        background:#ebebeb;
        -webkit-box-shadow:inset 1px 1px 4px rgba(0, 0, 0, .13);
        -moz-box-shadow:inset 1px 1px 4px rgba(0, 0, 0, .13);
        box-shadow:inset 1px 1px 4px rgba(0, 0, 0, .13)
    }
    ::selection {
        background:#00a5f0;
        color:#fff;
        text-shadow:1px 1px rgba(0, 0, 0, .2)
    }
    .subscribe-box {
        background:#e4ff8e
    }
    footer {
        margin-top:25px
    }
    .footerwrap {
        background:rgba(0, 0, 0, .49);
        color:#fff
    }
    .copyright {
        text-align:center
    }
}
@media screen and (max-width:53.75em) {
    .logo {
        float:none;
        margin:0 auto
    }
}
@media screen and (max-width:43.75em) {
    body {
        font-size:13px
    }
    .h1, h1 {
        font-size:32px
    }
    .h2, h2 {
        font-size:24px
    }
    .headerwrap {
        float:none;
        margin:0 auto
    }
    .logo {
        width:400px;
        margin:0 auto;
        float:none
    }
    .headerwrap, .pagewrap {
        width:100%;
        padding-top:10px
    }
    .grid {
        padding:10px 0 10px 10px
    }
    [class*=grid-] {
        float:none;
        width:100%;
        padding-right:10px
    }
    .pagewrap:after, .pagewrap:before {
        display:none
    }
}
@media screen and (max-width:34.375em) {
    .ad-middle, .header-ad {
        display:none;
        float:none
    }
    body.show-nav .search {
        top:205px;
        left:0
    }
    .logo {
        margin:0 auto;
        float:none;
        width:auto
    }
    .logo a {
        font-size:350%
    }
    .button, .button1, .button2 {
        display:block
    }
}
@media screen and (max-width:25em) {
    .logo a {
        font-size:300%
    }
    .formdiv input{
    	width:95%;
    }
    .module{
        padding:5px;
    }
    hr{
        margin:10px 0;
    }
    [class*="grid-"] {
        padding-right:0;
    }
    .pagewrap>.grid.group{
        padding:0;
    }
}
@media screen and (max-width:20em) {
    .logo a {
        font-size:200%
    }
    body.show-nav .search {
        top:290px
    }
}


