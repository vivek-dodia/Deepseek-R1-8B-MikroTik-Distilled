# Repository Information
Name: LoginHotspotMikrotik

# Directory Structure
Directory structure:
└── github_repos/LoginHotspotMikrotik/
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
    │   │       ├── pack-a0d2af4b589dde9368d4ffbc34c266bf5297b62a.idx
    │   │       └── pack-a0d2af4b589dde9368d4ffbc34c266bf5297b62a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── alogin.html
    ├── assets/
    │   ├── css/
    │   │   ├── custom.css
    │   │   ├── theme-3.css
    │   │   └── vendor.css
    │   ├── fonts/
    │   │   ├── glyphicons-halflings-regular-1.eot
    │   │   ├── glyphicons-halflings-regular-1.txt
    │   │   ├── glyphicons-halflings-regular-2.txt
    │   │   ├── glyphicons-halflings-regular.eot
    │   │   ├── glyphicons-halflings-regular.txt
    │   │   ├── slick-1.eot
    │   │   ├── slick-1.txt
    │   │   ├── slick.eot
    │   │   ├── slick.txt
    │   │   ├── themify-1.eot
    │   │   ├── themify-1.txt
    │   │   ├── themify.eot
    │   │   └── themify.txt
    │   ├── img/
    │   │   ├── contact/
    │   │   ├── number/
    │   │   └── service/
    │   └── js/
    │       ├── main.js
    │       ├── map.js
    │       └── vendor.js
    ├── error.html
    ├── errors.txt
    ├── img/
    ├── login.html
    ├── logout.html
    ├── lv/
    │   ├── alogin.html
    │   ├── errors.txt
    │   ├── login.html
    │   ├── logout.html
    │   ├── radvert.html
    │   └── status.html
    ├── md5.js
    ├── radvert.html
    ├── redirect.html
    ├── rlogin.html
    ├── status.html
    └── xml/
        ├── alogin.html
        ├── error.html
        ├── flogout.html
        ├── login.html
        ├── logout.html
        ├── rlogin.html
        └── WISPAccessGatewayParam.xsd


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
	url = https://github.com/AndreHerwanto/LoginHotspotMikrotik.git
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
0000000000000000000000000000000000000000 012bcde9720341ae54e2e5bfe96da97edba47c23 vivek-dodia <vivek.dodia@icloud.com> 1738606433 -0500	clone: from https://github.com/AndreHerwanto/LoginHotspotMikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 012bcde9720341ae54e2e5bfe96da97edba47c23 vivek-dodia <vivek.dodia@icloud.com> 1738606433 -0500	clone: from https://github.com/AndreHerwanto/LoginHotspotMikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 012bcde9720341ae54e2e5bfe96da97edba47c23 vivek-dodia <vivek.dodia@icloud.com> 1738606433 -0500	clone: from https://github.com/AndreHerwanto/LoginHotspotMikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
012bcde9720341ae54e2e5bfe96da97edba47c23 refs/remotes/origin/main


File: /.git\refs\heads\main
012bcde9720341ae54e2e5bfe96da97edba47c23


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /alogin.html
<html>
<head>
<title>mikrotik hotspot > redirect</title>
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
	location.href = unescape('$(link-redirect-esc)');
    }
//-->
</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	You are logged in
	<br><br>
	If nothing happens, click <a href="$(link-redirect)">here</a></td>
</tr>
</table>
</body>
</html>


File: /assets\css\custom.css
/**
 * place custom style in this file
 * add !important to the end if no effect
 * e.g. color: #fff !important;
 * --------------------------------------------------
 *
 */

#portfolio {
  position: relative;
  padding-top: 80px;
  padding-bottom: 80px;
}

.portfolio-row {
  margin-top: -30px;
}

.portfolio-card {
  display: block;
  transition: all 150ms ease-in-out;
  background-color: #fff;
  box-shadow: 0 1px 1px rgba(0,0,0,0.1);
  margin-top: 30px;
  border-radius: 2px;
}
.portfolio-card:hover,
.portfolio-card:focus {
  transform: translateY(-1px);
  box-shadow: 0 10px 20px 0 rgba(168,182,191,0.6);
}

.portfolio-card-media {
  height: 260px;
}

.portfolio-card-header {
  padding: 20px 15px;
}

.portfolio-card-avatar {
  float: left;
  display: inline-block;
  margin-right: 15px;
  width: 40px;
  height: 40px;
  background-color: #212121;
  color: #fff;
  border-radius: 50%;
  line-height: 40px;
  text-align: center;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.12);
}

.portfolio-card-title {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  font-size: 15px;
  font-weight: 500;
  line-height: 20px;
  color: #212121;
}

.portfolio-card-desc {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  font-size: 13px;
  line-height: 20px;
  color: #777;
}

/* demo */
.demo-panel,.demo-panel-toggle
{
	background-color: #fff;
	border: 1px solid #e5e5e5;
}
.demo-panel
{
	left: 0;
	ms-transform: translateX(-100%);
	o-transform: translateX(-100%);
	o-transition: all .2s ease-in-out;
	o-transition-property: -o-transform;
	padding-bottom: 28px;
	padding-top: 28px;
	position: fixed;
	top: 140px;
	transform: translateX(-100%);
	transition: all .2s ease-in-out;
	transition-property: transform;
	webkit-transform: translateX(-100%);
	webkit-transition: all .2s ease-in-out;
	webkit-transition-property: -webkit-transform;
	width: 240px;
	z-index: 10;
}
.demo-panel-in .demo-panel
{
	ms-transform: translateX(0);
	o-transform: translateX(0);
	transform: translateX(0);
	webkit-transform: translateX(0);
}
.demo-panel-toggle
{
	border-left-color: #fff;
	cursor: pointer;
	height: 48px;
	position: absolute;
	right: -47px;
	text-align: center;
	top: -1px;
	width: 48px;
}
.demo-panel-toggle i
{
	line-height: 48px;
}
.demo-panel h4
{
	margin-bottom: 8px;
}
[data-demo-panel-control=theme],[data-demo-panel-control=navbar-style],[data-demo-panel-control=navbar-style2]
{
	margin-left: -4px;
	margin-top: -4px;
}
[data-demo-panel-control=theme]:after,[data-demo-panel-control=theme]:before,[data-demo-panel-control=navbar-style]:after,[data-demo-panel-control=navbar-style]:before,[data-demo-panel-control=navbar-style2]:after,[data-demo-panel-control=navbar-style2]:before
{
	content: "";
	display: table;
}
[data-demo-panel-control=theme]:after,[data-demo-panel-control=navbar-style]:after,[data-demo-panel-control=navbar-style2]:after
{
	clear: both;
}
[data-demo-panel-control=theme] a,[data-demo-panel-control=navbar-style] a,[data-demo-panel-control=navbar-style2] a
{
	display: block;
	float: left;
	height: 20px;
	margin-left: 4px;
	margin-top: 4px;
	position: relative;
	width: 40px;
}
[data-demo-panel-control=theme] a.selected:after,[data-demo-panel-control=navbar-style] a.selected:after,[data-demo-panel-control=navbar-style2] a.selected:after
{
	border-left: 10px solid transparent;
	border-top: 10px solid rgba(25,25,25,.8);
	content: "";
	position: absolute;
	right: 0;
	top: 0;
}
[data-demo-panel-control=page-intro-size] a,[data-demo-panel-control=remove-el] a
{
	border: 2px solid transparent;
	border-radius: 2px;
	color: #757575;
	display: inline-block;
	font-weight: 700;
	line-height: 20px;
	margin-bottom: 4px;
	padding: 0 2px;
}
[data-demo-panel-control=page-intro-size] a.selected,[data-demo-panel-control=remove-el] a.selected
{
	background-color: #1a1a1a;
	border-color: #1a1a1a;
	color: #fff;
}

File: /assets\css\theme-3.css
/*!
 * Template Name: ELEANORE - Flexible App Landing Page
 * Author: bonefishcode.com
 *
 * Do not edit this file, recommend put custom style into `assets/css/custom.css`
 */
/**
 * ---------------------------------------------------------
 * Table of contents
 *
 * reboot
 * typography
 * plugin
 * common
 * page-loader
 * site-header
 * home
 * service
 * feature
 * skill
 * screenshot
 * watch-video
 * number
 * faq
 * pricing
 * download
 * subscribe
 * contact
 * site-footer
 * component
 * utility
 * ---------------------------------------------------------
 */
/**
 * reboot
 * ---------------------------------------------------------
 */
html {
  font-size: 1em;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
  -ms-overflow-style: scrollbar;
  -webkit-tap-highlight-color: transparent;
}

*,
*:before,
*:after {
  -webkit-box-sizing: inherit;
     -moz-box-sizing: inherit;
          box-sizing: inherit;
}

body {
  overflow-x: hidden;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
dl,
ol,
ul,
pre {
  margin-top: 0;
  margin-bottom: 0;
}

blockquote,
figure {
  margin: 0;
}

a {
  color: #b6e2a6;
  text-decoration: none;
}
a:hover, a:active {
  text-decoration: none;
}
a:focus {
  outline: dotted thin;
  outline: -webkit-focus-ring-color auto 5px;
  outline-offset: -2px;
}
a:hover, a:focus {
  color: #b6e2a6;
}
a:active {
  color: #b6e2a6;
}

fieldset {
  min-width: 0;
  margin: 0;
  border: 0;
  padding: 0;
}

/**
 * typography
 * ---------------------------------------------------------
 */
body {
  line-height: 1.714285714285714;
  background-color: #fff;
  color: #212121;
  font-size: 0.875rem;
  font-weight: 400;
  text-transform: inherit;
  letter-spacing: 0.01em;
}

h1, .text-h1,
h2, .text-h2,
h3, .text-h3,
h4, .text-h4,
h5, .text-h5,
h6, .text-h6 {
  color: inherit;
  font-weight: 500;
  text-transform: inherit;
  letter-spacing: 0.01em;
}

h1, .text-h1,
h2, .text-h2,
h3, .text-h3,
h4, .text-h4,
h5, .text-h5,
h6, .text-h6 {
  font-weight: 500;
  text-transform: inherit;
  letter-spacing: 0.01em;
}

p,
dl,
ol,
ul,
pre,
blockquote {
  margin-bottom: 1.5rem;
}
p:not(.navbar-nav):last-child,
dl:not(.navbar-nav):last-child,
ol:not(.navbar-nav):last-child,
ul:not(.navbar-nav):last-child,
pre:not(.navbar-nav):last-child,
blockquote:not(.navbar-nav):last-child {
  margin-bottom: 0;
}

.icon {
  letter-spacing: 0;
}

html:not(.ie9):not(.is-mobile) .wow {

}

html.sr [data-sr] {
  visibility: hidden;
}

.animate, .audio-toggle > a:before {
  visibility: hidden;
  -webkit-animation-duration: 1s;
       -o-animation-duration: 1s;
          animation-duration: 1s;
  -webkit-animation-fill-mode: both;
       -o-animation-fill-mode: both;
          animation-fill-mode: both;
}
.animate.infinite, .audio-toggle > a.infinite:before {
  -webkit-animation-iteration-count: infinite;
       -o-animation-iteration-count: infinite;
          animation-iteration-count: infinite;
}

@-webkit-keyframes jello {
  from, 11.1%, to {
    -webkit-transform: none;
            transform: none;
  }
  22.2% {
    -webkit-transform: skewX(-12.5deg) skewY(-12.5deg);
            transform: skewX(-12.5deg) skewY(-12.5deg);
  }
  33.3% {
    -webkit-transform: skewX(6.25deg) skewY(6.25deg);
            transform: skewX(6.25deg) skewY(6.25deg);
  }
  44.4% {
    -webkit-transform: skewX(-3.125deg) skewY(-3.125deg);
            transform: skewX(-3.125deg) skewY(-3.125deg);
  }
  55.5% {
    -webkit-transform: skewX(1.5625deg) skewY(1.5625deg);
            transform: skewX(1.5625deg) skewY(1.5625deg);
  }
  66.6% {
    -webkit-transform: skewX(-0.78125deg) skewY(-0.78125deg);
            transform: skewX(-0.78125deg) skewY(-0.78125deg);
  }
  77.7% {
    -webkit-transform: skewX(0.390625deg) skewY(0.390625deg);
            transform: skewX(0.390625deg) skewY(0.390625deg);
  }
  88.8% {
    -webkit-transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
            transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
  }
}

@-o-keyframes jello {
  from, 11.1%, to {
    -o-transform: none;
       transform: none;
  }
  22.2% {
    -o-transform: skewX(-12.5deg) skewY(-12.5deg);
       transform: skewX(-12.5deg) skewY(-12.5deg);
  }
  33.3% {
    -o-transform: skewX(6.25deg) skewY(6.25deg);
       transform: skewX(6.25deg) skewY(6.25deg);
  }
  44.4% {
    -o-transform: skewX(-3.125deg) skewY(-3.125deg);
       transform: skewX(-3.125deg) skewY(-3.125deg);
  }
  55.5% {
    -o-transform: skewX(1.5625deg) skewY(1.5625deg);
       transform: skewX(1.5625deg) skewY(1.5625deg);
  }
  66.6% {
    -o-transform: skewX(-0.78125deg) skewY(-0.78125deg);
       transform: skewX(-0.78125deg) skewY(-0.78125deg);
  }
  77.7% {
    -o-transform: skewX(0.390625deg) skewY(0.390625deg);
       transform: skewX(0.390625deg) skewY(0.390625deg);
  }
  88.8% {
    -o-transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
       transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
  }
}

@keyframes jello {
  from, 11.1%, to {
    -webkit-transform: none;
         -o-transform: none;
            transform: none;
  }
  22.2% {
    -webkit-transform: skewX(-12.5deg) skewY(-12.5deg);
         -o-transform: skewX(-12.5deg) skewY(-12.5deg);
            transform: skewX(-12.5deg) skewY(-12.5deg);
  }
  33.3% {
    -webkit-transform: skewX(6.25deg) skewY(6.25deg);
         -o-transform: skewX(6.25deg) skewY(6.25deg);
            transform: skewX(6.25deg) skewY(6.25deg);
  }
  44.4% {
    -webkit-transform: skewX(-3.125deg) skewY(-3.125deg);
         -o-transform: skewX(-3.125deg) skewY(-3.125deg);
            transform: skewX(-3.125deg) skewY(-3.125deg);
  }
  55.5% {
    -webkit-transform: skewX(1.5625deg) skewY(1.5625deg);
         -o-transform: skewX(1.5625deg) skewY(1.5625deg);
            transform: skewX(1.5625deg) skewY(1.5625deg);
  }
  66.6% {
    -webkit-transform: skewX(-0.78125deg) skewY(-0.78125deg);
         -o-transform: skewX(-0.78125deg) skewY(-0.78125deg);
            transform: skewX(-0.78125deg) skewY(-0.78125deg);
  }
  77.7% {
    -webkit-transform: skewX(0.390625deg) skewY(0.390625deg);
         -o-transform: skewX(0.390625deg) skewY(0.390625deg);
            transform: skewX(0.390625deg) skewY(0.390625deg);
  }
  88.8% {
    -webkit-transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
         -o-transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
            transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
  }
}
.jello {
  -webkit-animation-name: jello;
       -o-animation-name: jello;
          animation-name: jello;
  -webkit-transform-origin: center;
      -ms-transform-origin: center;
       -o-transform-origin: center;
          transform-origin: center;
}

@-webkit-keyframes fadeIn {

}

@-o-keyframes fadeIn {

}

@keyframes fadeIn {

}

.fadeIn {

}

@-webkit-keyframes fadeInUp {

}

@-o-keyframes fadeInUp {

}

@keyframes fadeInUp {

}

.fadeInUp {

}

@-webkit-keyframes fadeInRight {

}

@-o-keyframes fadeInRight {

}

@keyframes fadeInRight {

}

.fadeInRight {

}

@-webkit-keyframes fadeInDown {

}

@-o-keyframes fadeInDown {

}

@keyframes fadeInDown {

}

.fadeInDown {

}

@-webkit-keyframes fadeInLeft {

}

@-o-keyframes fadeInLeft {

}

@keyframes fadeInLeft {

}

.fadeInLeft {

}

.youtube-bg,
.youtube-bg-fallback,
.youtube-bg-placeholder,
.youtube-bg-player {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.youtube-bg-fallback {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.is-desktop .youtube-bg-fallback {
  display: none;
}

.youtube-bg-placeholder {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.youtube-bg-placeholder .is-mobile {
  display: none;
}

.slideshow,
.vegas-container {
  position: absolute !important;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.vegas-container {
  height: 100% !important;
}

.vegas-timer {
  z-index: 1;
}

.popup-doc {
  position: relative;
  padding: 2.25rem 1.5rem;
  max-width: 45rem;
  margin: 1.5rem auto;
  background-color: #fff;
}

html:not(.ie9):not(.is-mobile) .text-animate {
  visibility: hidden;
}

.title-row {
  margin-bottom: 6rem;
  text-align: center;
}

.section-title {
  line-height: 1.333333333333333;
  margin-top: 3rem;
  margin-bottom: 3rem;
  font-size: 2.25rem;
  font-weight: 300;
  color: black;
}

.section-title + .text-lead {
  line-height: 1.625;
  margin-top: -1.5rem;
  margin-bottom: 3rem;
  font-size: 1rem;
  font-weight: 300;
  color: black;
}

h2.section-title {
  line-height: 1.375;
  font-size: 2rem;

}

p.text-animate {
  color: black;

}

.btn-wrap > .btn {
  margin: 0.25rem;
}

.hint-text {
  line-height: 1.833333333333333;
  font-size: 0.75rem;
  color: inherit;
}
.hint-text .icon {
  margin-right: 0.5rem;
}

.cloud-from-right,
.cloud-from-left {
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
  position: absolute;
  bottom: 0;
  z-index: 10;
  background-image: url("../img/animate-cloud.png");
  background-repeat: repeat-x;
  height: 25rem;
  width: 73.125rem;
}

.cloud-from-right {
  left: 0;
  background-position: bottom left;
  -webkit-animation: cloud-from-right 15s linear infinite;
       -o-animation: cloud-from-right 15s linear infinite;
          animation: cloud-from-right 15s linear infinite;
}

.cloud-from-left {
  right: 0;
  background-position: bottom right;
  -webkit-animation: cloud-from-left 15s linear infinite;
       -o-animation: cloud-from-left 15s linear infinite;
          animation: cloud-from-left 15s linear infinite;
}

@-webkit-keyframes cloud-from-right {
  0% {
    -webkit-transform: translateX(0);
            transform: translateX(0);
  }
  100% {
    -webkit-transform: translateX(-585px);
            transform: translateX(-585px);
  }
}

@-o-keyframes cloud-from-right {
  0% {
    -o-transform: translateX(0);
       transform: translateX(0);
  }
  100% {
    -o-transform: translateX(-585px);
       transform: translateX(-585px);
  }
}

@keyframes cloud-from-right {
  0% {
    -webkit-transform: translateX(0);
         -o-transform: translateX(0);
            transform: translateX(0);
  }
  100% {
    -webkit-transform: translateX(-585px);
         -o-transform: translateX(-585px);
            transform: translateX(-585px);
  }
}
@-webkit-keyframes cloud-from-left {
  0% {
    -webkit-transform: translateX(0);
            transform: translateX(0);
  }
  100% {
    -webkit-transform: translateX(585px);
            transform: translateX(585px);
  }
}
@-o-keyframes cloud-from-left {
  0% {
    -o-transform: translateX(0);
       transform: translateX(0);
  }
  100% {
    -o-transform: translateX(585px);
       transform: translateX(585px);
  }
}
@keyframes cloud-from-left {
  0% {
    -webkit-transform: translateX(0);
         -o-transform: translateX(0);
            transform: translateX(0);
  }
  100% {
    -webkit-transform: translateX(585px);
         -o-transform: translateX(585px);
            transform: translateX(585px);
  }
}
.double-screen-right,
.double-screen-left {
  position: relative;
  max-width: 400px;
  overflow: hidden;
  z-index: 100;
  margin-right: auto;
  margin-left: auto;
}
.double-screen-right,
.double-screen-right .screen.top,
.double-screen-left,
.double-screen-left .screen.top {
  position: relative;
}

.double-screen-right .screen.top,
.double-screen-left .screen.top {
  z-index: 2;
}

.double-screen-right .screen.top {
  float: right;
}

.double-screen-left .screen.top {
  float: left;
}

.double-screen-right .screen.bottom,
.double-screen-left .screen.bottom {
  position: absolute;
  z-index: 1;
  top: 5%;
  height: 90%;
}

.double-screen-right .screen.bottom {
  left: 0;
}

.double-screen-left .screen.bottom {
  right: 0;
}

/**
 * page loader
 * ---------------------------------------------------------
 */
.page-loader {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: table;
  table-layout: fixed;
  width: 100%;
  height: 100%;
  background-color: #8a65c5;
  z-index: 9998;
}

.spinner {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

.spinner > div {
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
  width: 1.5rem;
  height: 1.5rem;
  background-color: #fff;
  -webkit-border-radius: 50%;
          border-radius: 50%;
  display: inline-block;
  -webkit-animation: page-loader 1.4s infinite ease-in-out both;
       -o-animation: page-loader 1.4s infinite ease-in-out both;
          animation: page-loader 1.4s infinite ease-in-out both;
  margin-right: 0.25rem;
  margin-left: 0.25rem;
}


@-webkit-keyframes page-loader {
  0%, 80%, 100% {
    -webkit-transform: scale(0);
            transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
}

@-o-keyframes page-loader {
  0%, 80%, 100% {
    -o-transform: scale(0);
       transform: scale(0);
  }
  40% {
    -o-transform: scale(1);
       transform: scale(1);
  }
}

@keyframes page-loader {
  0%, 80%, 100% {
    -webkit-transform: scale(0);
         -o-transform: scale(0);
            transform: scale(0);
  }
  40% {
    -webkit-transform: scale(1);
         -o-transform: scale(1);
            transform: scale(1);
  }
}
/**
 * site header
 * ---------------------------------------------------------
 */
.site-header-fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030;
}

/**
 * home
 * ---------------------------------------------------------
 */
#home {
  position: relative;
  overflow: hidden;
}

#home.align-outer {
  height: 50rem;
  height: 90vh;
  padding-top: 2.625rem; /** 9.625rem */
  padding-bottom: 5.625rem;
}
@media (min-width: 768px) {
  #home.align-outer {
    padding-top: 11.125rem;
  }
}

@media (min-width: 768px) {
  .home-row {
    background: rgba(255,255,255,0.8);
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
       -moz-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
}

@media (max-width: 767px) {
  .home-left-col {
    margin-bottom: 3rem;
    text-align: center;
  }
}

.home-form-col .panel {
  margin-bottom: 0;
  border: 0;
}
.home-form-col .panel-body {
  color: #212121;
}

#homeBgImg {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgOverlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgSlideshow {
  position: absolute !important;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  height: 100% !important;
}

.vegas-timer {
  z-index: 1;
}

#homeBgCloud {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow: hidden;
}
#homeBgCloud > .cloud {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
}
#homeBgCloud > .cloud:nth-child(1) {
  background-image: url(../img/home/home-cloud-1.png);
}
#homeBgCloud > .cloud:nth-child(2) {
  background-image: url(../img/home/home-cloud-2.png);
}
#homeBgCloud > .cloud:nth-child(3) {
  background-image: url(../img/home/home-cloud-3.png);
}

#homeBgStar {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
#homeBgStar > .star {
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
}
#homeBgStar > .star:after {
  position: absolute;
  content: "";
  top: 2000px;
}
#homeBgStar > .star:nth-child(1) {
  -webkit-animation: animationStar 50s linear infinite;
       -o-animation: animationStar 50s linear infinite;
          animation: animationStar 50s linear infinite;
  width: 1px;
  height: 1px;
  -webkit-box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
          box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
}
#homeBgStar > .star:nth-child(1):after {
  width: 1px;
  height: 1px;
  -webkit-box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
          box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
}
#homeBgStar > .star:nth-child(2) {
  -webkit-animation: animationStar 100s linear infinite;
       -o-animation: animationStar 100s linear infinite;
          animation: animationStar 100s linear infinite;
  width: 2px;
  height: 2px;
  -webkit-box-shadow: 332px 1704px #fff , 1089px 504px #fff , 1935px 1413px #fff , 256px 663px #fff , 1781px 1915px #fff , 1933px 1093px #fff , 302px 1962px #fff , 1787px 1267px #fff , 837px 1514px #fff , 1251px 812px #fff , 576px 1154px #fff , 292px 349px #fff , 1247px 1196px #fff , 1441px 1680px #fff , 316px 895px #fff , 257px 152px #fff , 1278px 1104px #fff , 455px 826px #fff , 1930px 1122px #fff , 1843px 1658px #fff , 99px 1944px #fff , 1973px 1253px #fff , 230px 633px #fff , 1527px 704px #fff , 972px 582px #fff , 1139px 435px #fff , 803px 831px #fff , 1235px 1280px #fff , 575px 1545px #fff , 1811px 1448px #fff , 83px 522px #fff , 668px 14px #fff , 605px 1256px #fff , 470px 1308px #fff , 1960px 796px #fff , 423px 940px #fff , 1766px 463px #fff , 1802px 1739px #fff , 231px 269px #fff , 1442px 1642px #fff , 950px 1327px #fff , 455px 1885px #fff , 897px 66px #fff , 1021px 422px #fff , 1262px 1423px #fff , 1194px 6px #fff , 341px 72px #fff , 1549px 854px #fff , 25px 1020px #fff , 358px 336px #fff , 1844px 338px #fff , 722px 244px #fff , 144px 1687px #fff , 1577px 1193px #fff , 920px 1877px #fff , 149px 1550px #fff , 1398px 1784px #fff , 1782px 607px #fff , 490px 1991px #fff , 439px 57px #fff , 851px 13px #fff , 73px 1797px #fff , 946px 954px #fff , 142px 171px #fff , 1319px 1868px #fff , 1008px 1458px #fff , 1483px 482px #fff , 716px 1100px #fff , 1585px 1347px #fff , 701px 1964px #fff , 1829px 1461px #fff , 608px 1320px #fff , 1134px 1259px #fff , 706px 979px #fff , 1417px 945px #fff , 1325px 180px #fff , 1266px 1682px #fff , 1339px 1516px #fff , 1608px 2px #fff , 1405px 100px #fff , 1275px 1591px #fff , 1505px 116px #fff , 1954px 1646px #fff , 1645px 1271px #fff , 633px 261px #fff , 1554px 1367px #fff , 1810px 1688px #fff , 1700px 470px #fff , 1759px 654px #fff , 266px 512px #fff , 942px 107px #fff , 379px 257px #fff , 622px 1721px #fff , 791px 958px #fff , 1259px 963px #fff , 1055px 45px #fff , 228px 160px #fff , 1197px 140px #fff , 1524px 796px #fff , 1773px 1490px #fff , 1538px 292px #fff , 1871px 1774px #fff , 1502px 1945px #fff , 1895px 120px #fff , 1001px 1468px #fff , 1055px 304px #fff , 678px 533px #fff , 1136px 1024px #fff , 642px 928px #fff , 1716px 430px #fff , 41px 622px #fff , 939px 1134px #fff , 4px 1388px #fff , 460px 496px #fff , 541px 1126px #fff , 1112px 1664px #fff , 1701px 1186px #fff , 1552px 738px #fff , 1951px 1561px #fff , 2000px 1709px #fff;
          box-shadow: 332px 1704px #fff , 1089px 504px #fff , 1935px 1413px #fff , 256px 663px #fff , 1781px 1915px #fff , 1933px 1093px #fff , 302px 1962px #fff , 1787px 1267px #fff , 837px 1514px #fff , 1251px 812px #fff , 576px 1154px #fff , 292px 349px #fff , 1247px 1196px #fff , 1441px 1680px #fff , 316px 895px #fff , 257px 152px #fff , 1278px 1104px #fff , 455px 826px #fff , 1930px 1122px #fff , 1843px 1658px #fff , 99px 1944px #fff , 1973px 1253px #fff , 230px 633px #fff , 1527px 704px #fff , 972px 582px #fff , 1139px 435px #fff , 803px 831px #fff , 1235px 1280px #fff , 575px 1545px #fff , 1811px 1448px #fff , 83px 522px #fff , 668px 14px #fff , 605px 1256px #fff , 470px 1308px #fff , 1960px 796px #fff , 423px 940px #fff , 1766px 463px #fff , 1802px 1739px #fff , 231px 269px #fff , 1442px 1642px #fff , 950px 1327px #fff , 455px 1885px #fff , 897px 66px #fff , 1021px 422px #fff , 1262px 1423px #fff , 1194px 6px #fff , 341px 72px #fff , 1549px 854px #fff , 25px 1020px #fff , 358px 336px #fff , 1844px 338px #fff , 722px 244px #fff , 144px 1687px #fff , 1577px 1193px #fff , 920px 1877px #fff , 149px 1550px #fff , 1398px 1784px #fff , 1782px 607px #fff , 490px 1991px #fff , 439px 57px #fff , 851px 13px #fff , 73px 1797px #fff , 946px 954px #fff , 142px 171px #fff , 1319px 1868px #fff , 1008px 1458px #fff , 1483px 482px #fff , 716px 1100px #fff , 1585px 1347px #fff , 701px 1964px #fff , 1829px 1461px #fff , 608px 1320px #fff , 1134px 1259px #fff , 706px 979px #fff , 1417px 945px #fff , 1325px 180px #fff , 1266px 1682px #fff , 1339px 1516px #fff , 1608px 2px #fff , 1405px 100px #fff , 1275px 1591px #fff , 1505px 116px #fff , 1954px 1646px #fff , 1645px 1271px #fff , 633px 261px #fff , 1554px 1367px #fff , 1810px 1688px #fff , 1700px 470px #fff , 1759px 654px #fff , 266px 512px #fff , 942px 107px #fff , 379px 257px #fff , 622px 1721px #fff , 791px 958px #fff , 1259px 963px #fff , 1055px 45px #fff , 228px 160px #fff , 1197px 140px #fff , 1524px 796px #fff , 1773px 1490px #fff , 1538px 292px #fff , 1871px 1774px #fff , 1502px 1945px #fff , 1895px 120px #fff , 1001px 1468px #fff , 1055px 304px #fff , 678px 533px #fff , 1136px 1024px #fff , 642px 928px #fff , 1716px 430px #fff , 41px 622px #fff , 939px 1134px #fff , 4px 1388px #fff , 460px 496px #fff , 541px 1126px #fff , 1112px 1664px #fff , 1701px 1186px #fff , 1552px 738px #fff , 1951px 1561px #fff , 2000px 1709px #fff;
}
#homeBgStar > .star:nth-child(2):after {
  width: 2px;
  height: 2px;
  -webkit-box-shadow: 332px 1704px #fff , 1089px 504px #fff , 1935px 1413px #fff , 256px 663px #fff , 1781px 1915px #fff , 1933px 1093px #fff , 302px 1962px #fff , 1787px 1267px #fff , 837px 1514px #fff , 1251px 812px #fff , 576px 1154px #fff , 292px 349px #fff , 1247px 1196px #fff , 1441px 1680px #fff , 316px 895px #fff , 257px 152px #fff , 1278px 1104px #fff , 455px 826px #fff , 1930px 1122px #fff , 1843px 1658px #fff , 99px 1944px #fff , 1973px 1253px #fff , 230px 633px #fff , 1527px 704px #fff , 972px 582px #fff , 1139px 435px #fff , 803px 831px #fff , 1235px 1280px #fff , 575px 1545px #fff , 1811px 1448px #fff , 83px 522px #fff , 668px 14px #fff , 605px 1256px #fff , 470px 1308px #fff , 1960px 796px #fff , 423px 940px #fff , 1766px 463px #fff , 1802px 1739px #fff , 231px 269px #fff , 1442px 1642px #fff , 950px 1327px #fff , 455px 1885px #fff , 897px 66px #fff , 1021px 422px #fff , 1262px 1423px #fff , 1194px 6px #fff , 341px 72px #fff , 1549px 854px #fff , 25px 1020px #fff , 358px 336px #fff , 1844px 338px #fff , 722px 244px #fff , 144px 1687px #fff , 1577px 1193px #fff , 920px 1877px #fff , 149px 1550px #fff , 1398px 1784px #fff , 1782px 607px #fff , 490px 1991px #fff , 439px 57px #fff , 851px 13px #fff , 73px 1797px #fff , 946px 954px #fff , 142px 171px #fff , 1319px 1868px #fff , 1008px 1458px #fff , 1483px 482px #fff , 716px 1100px #fff , 1585px 1347px #fff , 701px 1964px #fff , 1829px 1461px #fff , 608px 1320px #fff , 1134px 1259px #fff , 706px 979px #fff , 1417px 945px #fff , 1325px 180px #fff , 1266px 1682px #fff , 1339px 1516px #fff , 1608px 2px #fff , 1405px 100px #fff , 1275px 1591px #fff , 1505px 116px #fff , 1954px 1646px #fff , 1645px 1271px #fff , 633px 261px #fff , 1554px 1367px #fff , 1810px 1688px #fff , 1700px 470px #fff , 1759px 654px #fff , 266px 512px #fff , 942px 107px #fff , 379px 257px #fff , 622px 1721px #fff , 791px 958px #fff , 1259px 963px #fff , 1055px 45px #fff , 228px 160px #fff , 1197px 140px #fff , 1524px 796px #fff , 1773px 1490px #fff , 1538px 292px #fff , 1871px 1774px #fff , 1502px 1945px #fff , 1895px 120px #fff , 1001px 1468px #fff , 1055px 304px #fff , 678px 533px #fff , 1136px 1024px #fff , 642px 928px #fff , 1716px 430px #fff , 41px 622px #fff , 939px 1134px #fff , 4px 1388px #fff , 460px 496px #fff , 541px 1126px #fff , 1112px 1664px #fff , 1701px 1186px #fff , 1552px 738px #fff , 1951px 1561px #fff , 2000px 1709px #fff;
          box-shadow: 332px 1704px #fff , 1089px 504px #fff , 1935px 1413px #fff , 256px 663px #fff , 1781px 1915px #fff , 1933px 1093px #fff , 302px 1962px #fff , 1787px 1267px #fff , 837px 1514px #fff , 1251px 812px #fff , 576px 1154px #fff , 292px 349px #fff , 1247px 1196px #fff , 1441px 1680px #fff , 316px 895px #fff , 257px 152px #fff , 1278px 1104px #fff , 455px 826px #fff , 1930px 1122px #fff , 1843px 1658px #fff , 99px 1944px #fff , 1973px 1253px #fff , 230px 633px #fff , 1527px 704px #fff , 972px 582px #fff , 1139px 435px #fff , 803px 831px #fff , 1235px 1280px #fff , 575px 1545px #fff , 1811px 1448px #fff , 83px 522px #fff , 668px 14px #fff , 605px 1256px #fff , 470px 1308px #fff , 1960px 796px #fff , 423px 940px #fff , 1766px 463px #fff , 1802px 1739px #fff , 231px 269px #fff , 1442px 1642px #fff , 950px 1327px #fff , 455px 1885px #fff , 897px 66px #fff , 1021px 422px #fff , 1262px 1423px #fff , 1194px 6px #fff , 341px 72px #fff , 1549px 854px #fff , 25px 1020px #fff , 358px 336px #fff , 1844px 338px #fff , 722px 244px #fff , 144px 1687px #fff , 1577px 1193px #fff , 920px 1877px #fff , 149px 1550px #fff , 1398px 1784px #fff , 1782px 607px #fff , 490px 1991px #fff , 439px 57px #fff , 851px 13px #fff , 73px 1797px #fff , 946px 954px #fff , 142px 171px #fff , 1319px 1868px #fff , 1008px 1458px #fff , 1483px 482px #fff , 716px 1100px #fff , 1585px 1347px #fff , 701px 1964px #fff , 1829px 1461px #fff , 608px 1320px #fff , 1134px 1259px #fff , 706px 979px #fff , 1417px 945px #fff , 1325px 180px #fff , 1266px 1682px #fff , 1339px 1516px #fff , 1608px 2px #fff , 1405px 100px #fff , 1275px 1591px #fff , 1505px 116px #fff , 1954px 1646px #fff , 1645px 1271px #fff , 633px 261px #fff , 1554px 1367px #fff , 1810px 1688px #fff , 1700px 470px #fff , 1759px 654px #fff , 266px 512px #fff , 942px 107px #fff , 379px 257px #fff , 622px 1721px #fff , 791px 958px #fff , 1259px 963px #fff , 1055px 45px #fff , 228px 160px #fff , 1197px 140px #fff , 1524px 796px #fff , 1773px 1490px #fff , 1538px 292px #fff , 1871px 1774px #fff , 1502px 1945px #fff , 1895px 120px #fff , 1001px 1468px #fff , 1055px 304px #fff , 678px 533px #fff , 1136px 1024px #fff , 642px 928px #fff , 1716px 430px #fff , 41px 622px #fff , 939px 1134px #fff , 4px 1388px #fff , 460px 496px #fff , 541px 1126px #fff , 1112px 1664px #fff , 1701px 1186px #fff , 1552px 738px #fff , 1951px 1561px #fff , 2000px 1709px #fff;
}
#homeBgStar > .star:nth-child(3) {
  -webkit-animation: animationStar 150s linear infinite;
       -o-animation: animationStar 150s linear infinite;
          animation: animationStar 150s linear infinite;
  width: 3px;
  height: 3px;
  -webkit-box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
          box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
}
#homeBgStar > .star:nth-child(3):after {
  width: 3px;
  height: 3px;
  -webkit-box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
          box-shadow: 982px 1702px #fff , 532px 462px #fff , 1988px 1569px #fff , 1769px 519px #fff , 294px 1969px #fff , 1697px 1192px #fff , 1159px 439px #fff , 1056px 1653px #fff , 1387px 401px #fff , 917px 148px #fff , 1835px 1734px #fff , 1643px 316px #fff , 1720px 882px #fff , 846px 492px #fff , 1856px 1222px #fff , 365px 972px #fff , 838px 1862px #fff , 1513px 661px #fff , 1631px 1804px #fff , 1064px 906px #fff , 554px 1074px #fff , 1476px 1425px #fff , 1917px 157px #fff , 1008px 754px #fff , 848px 1571px #fff , 748px 1143px #fff , 715px 15px #fff , 1605px 1757px #fff , 1900px 1844px #fff , 1597px 1498px #fff , 234px 1917px #fff , 614px 1781px #fff , 25px 906px #fff , 1242px 1574px #fff , 1350px 1389px #fff , 1562px 149px #fff , 1717px 1690px #fff , 1018px 1876px #fff , 1126px 1970px #fff , 1945px 348px #fff , 1925px 593px #fff , 176px 1574px #fff , 928px 1456px #fff , 1212px 1795px #fff , 573px 1526px #fff , 1207px 1460px #fff , 1492px 86px #fff , 1847px 1011px #fff , 1213px 1359px #fff , 1462px 467px #fff , 1336px 1355px #fff , 1009px 1231px #fff , 535px 1729px #fff , 199px 1701px #fff , 171px 1318px #fff , 152px 1798px #fff , 1127px 859px #fff , 1761px 750px #fff , 507px 995px #fff , 1208px 1651px #fff , 1852px 1877px #fff , 820px 1506px #fff , 1740px 976px #fff , 198px 897px #fff , 1892px 913px #fff , 1485px 236px #fff , 179px 619px #fff , 1358px 1219px #fff , 733px 489px #fff , 1164px 1300px #fff , 584px 1000px #fff , 605px 1042px #fff , 439px 658px #fff , 105px 500px #fff , 1137px 1630px #fff , 1651px 1399px #fff , 931px 849px #fff , 1017px 322px #fff , 538px 523px #fff , 1342px 792px #fff , 489px 1672px #fff , 1183px 654px #fff , 1038px 1539px #fff , 410px 952px #fff , 1752px 1045px #fff , 1385px 1921px #fff , 985px 1122px #fff , 989px 1732px #fff , 783px 70px #fff , 1068px 521px #fff , 620px 581px #fff , 605px 1624px #fff , 1106px 331px #fff , 48px 947px #fff , 1921px 1091px #fff , 1366px 912px #fff , 1642px 19px #fff , 1317px 1712px #fff , 1068px 700px #fff , 657px 1558px #fff , 1573px 676px #fff , 1854px 765px #fff , 1617px 431px #fff , 298px 9px #fff , 1397px 559px #fff , 997px 1693px #fff , 789px 1092px #fff , 156px 335px #fff , 1914px 106px #fff , 718px 1622px #fff , 1003px 511px #fff , 1878px 1335px #fff , 1555px 1795px #fff , 981px 549px #fff , 866px 702px #fff , 1983px 1327px #fff , 671px 1207px #fff , 1515px 1202px #fff , 1324px 481px #fff , 1095px 846px #fff , 781px 133px #fff , 452px 1583px #fff , 2000px 790px #fff , 368px 1028px #fff , 1382px 1058px #fff , 1397px 987px #fff , 530px 708px #fff , 763px 470px #fff , 866px 1980px #fff , 1615px 795px #fff , 1750px 643px #fff , 1536px 1303px #fff , 1003px 1451px #fff , 1444px 227px #fff , 1703px 1172px #fff , 1190px 363px #fff , 1382px 1821px #fff , 250px 1052px #fff , 1799px 1444px #fff , 1778px 1083px #fff , 705px 1368px #fff , 1914px 1701px #fff , 1321px 1057px #fff , 342px 6px #fff , 1941px 1158px #fff , 628px 1625px #fff , 1544px 106px #fff , 610px 1452px #fff , 585px 1712px #fff , 876px 1942px #fff , 392px 1291px #fff , 1714px 1321px #fff , 1282px 898px #fff , 1994px 1808px #fff , 908px 1155px #fff , 635px 1225px #fff , 1171px 273px #fff , 147px 639px #fff , 1795px 204px #fff , 1466px 1427px #fff , 873px 1635px #fff , 206px 340px #fff , 1162px 981px #fff , 1991px 1113px #fff , 1455px 579px #fff , 1075px 1993px #fff , 628px 520px #fff , 1367px 824px #fff , 794px 1130px #fff , 498px 906px #fff , 1554px 252px #fff , 567px 800px #fff , 1447px 723px #fff , 1720px 1109px #fff , 1789px 741px #fff , 51px 821px #fff , 46px 361px #fff , 50px 1929px #fff , 1507px 699px #fff , 161px 1929px #fff;
}
@media (min-width: 992px) {
  #homeBgStar > .star:nth-child(1) {
    -webkit-box-shadow: 688px 477px #fff , 1887px 799px #fff , 927px 1297px #fff , 1258px 448px #fff , 985px 1368px #fff , 290px 822px #fff , 1903px 816px #fff , 1890px 379px #fff , 1410px 1164px #fff , 300px 1949px #fff , 951px 423px #fff , 1982px 1981px #fff , 254px 1594px #fff , 1545px 1916px #fff , 778px 812px #fff , 614px 1881px #fff , 1279px 27px #fff , 1975px 1118px #fff , 1px 765px #fff , 1299px 1796px #fff , 1716px 1919px #fff , 1271px 427px #fff , 1210px 824px #fff , 697px 508px #fff , 200px 377px #fff , 905px 1180px #fff , 496px 172px #fff , 1159px 1695px #fff , 478px 202px #fff , 588px 801px #fff , 167px 1091px #fff , 1314px 104px #fff , 1647px 1865px #fff , 1186px 775px #fff , 752px 58px #fff , 1630px 66px #fff , 1630px 443px #fff , 1533px 1704px #fff , 1229px 475px #fff , 1415px 1723px #fff , 1017px 1427px #fff , 825px 575px #fff , 45px 25px #fff , 697px 189px #fff , 1826px 374px #fff , 626px 1132px #fff , 1060px 1352px #fff , 1955px 183px #fff , 577px 810px #fff , 617px 425px #fff , 171px 27px #fff , 1106px 1657px #fff , 191px 1122px #fff , 1783px 1839px #fff , 27px 323px #fff , 1246px 1867px #fff , 100px 1319px #fff , 1840px 621px #fff , 136px 492px #fff , 1362px 677px #fff , 84px 1264px #fff , 1714px 750px #fff , 996px 825px #fff , 70px 1331px #fff , 1556px 219px #fff , 137px 1435px #fff , 656px 917px #fff , 1992px 1136px #fff , 1636px 1238px #fff , 228px 1291px #fff , 1266px 500px #fff , 761px 301px #fff , 268px 1516px #fff , 660px 700px #fff , 1623px 68px #fff , 981px 428px #fff , 578px 1775px #fff , 439px 402px #fff , 1750px 1546px #fff , 51px 1378px #fff , 1248px 929px #fff , 1574px 154px #fff , 1902px 224px #fff , 1189px 831px #fff , 878px 958px #fff , 688px 1523px #fff , 1803px 833px #fff , 767px 864px #fff , 1039px 748px #fff , 1186px 1265px #fff , 1502px 271px #fff , 843px 177px #fff , 54px 1245px #fff , 617px 411px #fff , 807px 1276px #fff , 668px 1729px #fff , 991px 932px #fff , 208px 956px #fff , 1955px 1983px #fff , 1px 1566px #fff , 476px 673px #fff , 1516px 725px #fff , 824px 598px #fff , 876px 90px #fff , 1664px 186px #fff , 1045px 514px #fff , 271px 968px #fff , 1242px 1106px #fff , 695px 1022px #fff , 1808px 681px #fff , 220px 799px #fff , 798px 1683px #fff , 1644px 780px #fff , 829px 1656px #fff , 1830px 187px #fff , 1757px 1803px #fff , 427px 1958px #fff , 1489px 1767px #fff , 668px 1881px #fff , 802px 890px #fff , 1957px 1164px #fff , 340px 1693px #fff , 1433px 637px #fff , 1403px 1113px #fff , 102px 669px #fff , 727px 1575px #fff , 254px 1839px #fff , 20px 848px #fff , 1103px 293px #fff , 76px 92px #fff , 412px 1166px #fff , 1292px 1829px #fff , 367px 1536px #fff , 871px 1081px #fff , 828px 1364px #fff , 1779px 133px #fff , 1657px 695px #fff , 837px 1727px #fff , 1831px 978px #fff , 495px 953px #fff , 1670px 38px #fff , 29px 1715px #fff , 316px 1141px #fff , 958px 1678px #fff , 919px 22px #fff , 459px 1165px #fff , 1976px 1698px #fff , 1877px 1294px #fff , 121px 326px #fff , 961px 1396px #fff , 1556px 1731px #fff , 519px 545px #fff , 1537px 1035px #fff , 1432px 281px #fff , 1788px 882px #fff , 1783px 735px #fff , 1763px 1062px #fff , 1096px 1996px #fff , 1999px 474px #fff , 1494px 759px #fff , 499px 392px #fff , 517px 1435px #fff , 291px 14px #fff , 975px 1509px #fff , 184px 1552px #fff , 1927px 1992px #fff , 731px 1155px #fff , 1126px 378px #fff , 774px 91px #fff , 1136px 1506px #fff , 1043px 421px #fff , 389px 1475px #fff , 1955px 1182px #fff , 815px 1302px #fff , 36px 450px #fff , 1078px 574px #fff , 1290px 1277px #fff , 1840px 19px #fff , 651px 882px #fff , 437px 126px #fff , 1815px 1518px #fff , 140px 1631px #fff , 563px 1601px #fff , 41px 1772px #fff , 314px 609px #fff , 1331px 1439px #fff , 1564px 922px #fff , 806px 1200px #fff , 529px 1620px #fff , 324px 657px #fff , 544px 505px #fff , 1134px 1691px #fff , 905px 297px #fff , 1693px 1171px #fff , 1272px 298px #fff , 687px 666px #fff , 1692px 753px #fff , 865px 61px #fff , 784px 86px #fff , 479px 90px #fff;
            box-shadow: 688px 477px #fff , 1887px 799px #fff , 927px 1297px #fff , 1258px 448px #fff , 985px 1368px #fff , 290px 822px #fff , 1903px 816px #fff , 1890px 379px #fff , 1410px 1164px #fff , 300px 1949px #fff , 951px 423px #fff , 1982px 1981px #fff , 254px 1594px #fff , 1545px 1916px #fff , 778px 812px #fff , 614px 1881px #fff , 1279px 27px #fff , 1975px 1118px #fff , 1px 765px #fff , 1299px 1796px #fff , 1716px 1919px #fff , 1271px 427px #fff , 1210px 824px #fff , 697px 508px #fff , 200px 377px #fff , 905px 1180px #fff , 496px 172px #fff , 1159px 1695px #fff , 478px 202px #fff , 588px 801px #fff , 167px 1091px #fff , 1314px 104px #fff , 1647px 1865px #fff , 1186px 775px #fff , 752px 58px #fff , 1630px 66px #fff , 1630px 443px #fff , 1533px 1704px #fff , 1229px 475px #fff , 1415px 1723px #fff , 1017px 1427px #fff , 825px 575px #fff , 45px 25px #fff , 697px 189px #fff , 1826px 374px #fff , 626px 1132px #fff , 1060px 1352px #fff , 1955px 183px #fff , 577px 810px #fff , 617px 425px #fff , 171px 27px #fff , 1106px 1657px #fff , 191px 1122px #fff , 1783px 1839px #fff , 27px 323px #fff , 1246px 1867px #fff , 100px 1319px #fff , 1840px 621px #fff , 136px 492px #fff , 1362px 677px #fff , 84px 1264px #fff , 1714px 750px #fff , 996px 825px #fff , 70px 1331px #fff , 1556px 219px #fff , 137px 1435px #fff , 656px 917px #fff , 1992px 1136px #fff , 1636px 1238px #fff , 228px 1291px #fff , 1266px 500px #fff , 761px 301px #fff , 268px 1516px #fff , 660px 700px #fff , 1623px 68px #fff , 981px 428px #fff , 578px 1775px #fff , 439px 402px #fff , 1750px 1546px #fff , 51px 1378px #fff , 1248px 929px #fff , 1574px 154px #fff , 1902px 224px #fff , 1189px 831px #fff , 878px 958px #fff , 688px 1523px #fff , 1803px 833px #fff , 767px 864px #fff , 1039px 748px #fff , 1186px 1265px #fff , 1502px 271px #fff , 843px 177px #fff , 54px 1245px #fff , 617px 411px #fff , 807px 1276px #fff , 668px 1729px #fff , 991px 932px #fff , 208px 956px #fff , 1955px 1983px #fff , 1px 1566px #fff , 476px 673px #fff , 1516px 725px #fff , 824px 598px #fff , 876px 90px #fff , 1664px 186px #fff , 1045px 514px #fff , 271px 968px #fff , 1242px 1106px #fff , 695px 1022px #fff , 1808px 681px #fff , 220px 799px #fff , 798px 1683px #fff , 1644px 780px #fff , 829px 1656px #fff , 1830px 187px #fff , 1757px 1803px #fff , 427px 1958px #fff , 1489px 1767px #fff , 668px 1881px #fff , 802px 890px #fff , 1957px 1164px #fff , 340px 1693px #fff , 1433px 637px #fff , 1403px 1113px #fff , 102px 669px #fff , 727px 1575px #fff , 254px 1839px #fff , 20px 848px #fff , 1103px 293px #fff , 76px 92px #fff , 412px 1166px #fff , 1292px 1829px #fff , 367px 1536px #fff , 871px 1081px #fff , 828px 1364px #fff , 1779px 133px #fff , 1657px 695px #fff , 837px 1727px #fff , 1831px 978px #fff , 495px 953px #fff , 1670px 38px #fff , 29px 1715px #fff , 316px 1141px #fff , 958px 1678px #fff , 919px 22px #fff , 459px 1165px #fff , 1976px 1698px #fff , 1877px 1294px #fff , 121px 326px #fff , 961px 1396px #fff , 1556px 1731px #fff , 519px 545px #fff , 1537px 1035px #fff , 1432px 281px #fff , 1788px 882px #fff , 1783px 735px #fff , 1763px 1062px #fff , 1096px 1996px #fff , 1999px 474px #fff , 1494px 759px #fff , 499px 392px #fff , 517px 1435px #fff , 291px 14px #fff , 975px 1509px #fff , 184px 1552px #fff , 1927px 1992px #fff , 731px 1155px #fff , 1126px 378px #fff , 774px 91px #fff , 1136px 1506px #fff , 1043px 421px #fff , 389px 1475px #fff , 1955px 1182px #fff , 815px 1302px #fff , 36px 450px #fff , 1078px 574px #fff , 1290px 1277px #fff , 1840px 19px #fff , 651px 882px #fff , 437px 126px #fff , 1815px 1518px #fff , 140px 1631px #fff , 563px 1601px #fff , 41px 1772px #fff , 314px 609px #fff , 1331px 1439px #fff , 1564px 922px #fff , 806px 1200px #fff , 529px 1620px #fff , 324px 657px #fff , 544px 505px #fff , 1134px 1691px #fff , 905px 297px #fff , 1693px 1171px #fff , 1272px 298px #fff , 687px 666px #fff , 1692px 753px #fff , 865px 61px #fff , 784px 86px #fff , 479px 90px #fff;
  }
  #homeBgStar > .star:nth-child(1):after {
    -webkit-box-shadow: 688px 477px #fff , 1887px 799px #fff , 927px 1297px #fff , 1258px 448px #fff , 985px 1368px #fff , 290px 822px #fff , 1903px 816px #fff , 1890px 379px #fff , 1410px 1164px #fff , 300px 1949px #fff , 951px 423px #fff , 1982px 1981px #fff , 254px 1594px #fff , 1545px 1916px #fff , 778px 812px #fff , 614px 1881px #fff , 1279px 27px #fff , 1975px 1118px #fff , 1px 765px #fff , 1299px 1796px #fff , 1716px 1919px #fff , 1271px 427px #fff , 1210px 824px #fff , 697px 508px #fff , 200px 377px #fff , 905px 1180px #fff , 496px 172px #fff , 1159px 1695px #fff , 478px 202px #fff , 588px 801px #fff , 167px 1091px #fff , 1314px 104px #fff , 1647px 1865px #fff , 1186px 775px #fff , 752px 58px #fff , 1630px 66px #fff , 1630px 443px #fff , 1533px 1704px #fff , 1229px 475px #fff , 1415px 1723px #fff , 1017px 1427px #fff , 825px 575px #fff , 45px 25px #fff , 697px 189px #fff , 1826px 374px #fff , 626px 1132px #fff , 1060px 1352px #fff , 1955px 183px #fff , 577px 810px #fff , 617px 425px #fff , 171px 27px #fff , 1106px 1657px #fff , 191px 1122px #fff , 1783px 1839px #fff , 27px 323px #fff , 1246px 1867px #fff , 100px 1319px #fff , 1840px 621px #fff , 136px 492px #fff , 1362px 677px #fff , 84px 1264px #fff , 1714px 750px #fff , 996px 825px #fff , 70px 1331px #fff , 1556px 219px #fff , 137px 1435px #fff , 656px 917px #fff , 1992px 1136px #fff , 1636px 1238px #fff , 228px 1291px #fff , 1266px 500px #fff , 761px 301px #fff , 268px 1516px #fff , 660px 700px #fff , 1623px 68px #fff , 981px 428px #fff , 578px 1775px #fff , 439px 402px #fff , 1750px 1546px #fff , 51px 1378px #fff , 1248px 929px #fff , 1574px 154px #fff , 1902px 224px #fff , 1189px 831px #fff , 878px 958px #fff , 688px 1523px #fff , 1803px 833px #fff , 767px 864px #fff , 1039px 748px #fff , 1186px 1265px #fff , 1502px 271px #fff , 843px 177px #fff , 54px 1245px #fff , 617px 411px #fff , 807px 1276px #fff , 668px 1729px #fff , 991px 932px #fff , 208px 956px #fff , 1955px 1983px #fff , 1px 1566px #fff , 476px 673px #fff , 1516px 725px #fff , 824px 598px #fff , 876px 90px #fff , 1664px 186px #fff , 1045px 514px #fff , 271px 968px #fff , 1242px 1106px #fff , 695px 1022px #fff , 1808px 681px #fff , 220px 799px #fff , 798px 1683px #fff , 1644px 780px #fff , 829px 1656px #fff , 1830px 187px #fff , 1757px 1803px #fff , 427px 1958px #fff , 1489px 1767px #fff , 668px 1881px #fff , 802px 890px #fff , 1957px 1164px #fff , 340px 1693px #fff , 1433px 637px #fff , 1403px 1113px #fff , 102px 669px #fff , 727px 1575px #fff , 254px 1839px #fff , 20px 848px #fff , 1103px 293px #fff , 76px 92px #fff , 412px 1166px #fff , 1292px 1829px #fff , 367px 1536px #fff , 871px 1081px #fff , 828px 1364px #fff , 1779px 133px #fff , 1657px 695px #fff , 837px 1727px #fff , 1831px 978px #fff , 495px 953px #fff , 1670px 38px #fff , 29px 1715px #fff , 316px 1141px #fff , 958px 1678px #fff , 919px 22px #fff , 459px 1165px #fff , 1976px 1698px #fff , 1877px 1294px #fff , 121px 326px #fff , 961px 1396px #fff , 1556px 1731px #fff , 519px 545px #fff , 1537px 1035px #fff , 1432px 281px #fff , 1788px 882px #fff , 1783px 735px #fff , 1763px 1062px #fff , 1096px 1996px #fff , 1999px 474px #fff , 1494px 759px #fff , 499px 392px #fff , 517px 1435px #fff , 291px 14px #fff , 975px 1509px #fff , 184px 1552px #fff , 1927px 1992px #fff , 731px 1155px #fff , 1126px 378px #fff , 774px 91px #fff , 1136px 1506px #fff , 1043px 421px #fff , 389px 1475px #fff , 1955px 1182px #fff , 815px 1302px #fff , 36px 450px #fff , 1078px 574px #fff , 1290px 1277px #fff , 1840px 19px #fff , 651px 882px #fff , 437px 126px #fff , 1815px 1518px #fff , 140px 1631px #fff , 563px 1601px #fff , 41px 1772px #fff , 314px 609px #fff , 1331px 1439px #fff , 1564px 922px #fff , 806px 1200px #fff , 529px 1620px #fff , 324px 657px #fff , 544px 505px #fff , 1134px 1691px #fff , 905px 297px #fff , 1693px 1171px #fff , 1272px 298px #fff , 687px 666px #fff , 1692px 753px #fff , 865px 61px #fff , 784px 86px #fff , 479px 90px #fff;
            box-shadow: 688px 477px #fff , 1887px 799px #fff , 927px 1297px #fff , 1258px 448px #fff , 985px 1368px #fff , 290px 822px #fff , 1903px 816px #fff , 1890px 379px #fff , 1410px 1164px #fff , 300px 1949px #fff , 951px 423px #fff , 1982px 1981px #fff , 254px 1594px #fff , 1545px 1916px #fff , 778px 812px #fff , 614px 1881px #fff , 1279px 27px #fff , 1975px 1118px #fff , 1px 765px #fff , 1299px 1796px #fff , 1716px 1919px #fff , 1271px 427px #fff , 1210px 824px #fff , 697px 508px #fff , 200px 377px #fff , 905px 1180px #fff , 496px 172px #fff , 1159px 1695px #fff , 478px 202px #fff , 588px 801px #fff , 167px 1091px #fff , 1314px 104px #fff , 1647px 1865px #fff , 1186px 775px #fff , 752px 58px #fff , 1630px 66px #fff , 1630px 443px #fff , 1533px 1704px #fff , 1229px 475px #fff , 1415px 1723px #fff , 1017px 1427px #fff , 825px 575px #fff , 45px 25px #fff , 697px 189px #fff , 1826px 374px #fff , 626px 1132px #fff , 1060px 1352px #fff , 1955px 183px #fff , 577px 810px #fff , 617px 425px #fff , 171px 27px #fff , 1106px 1657px #fff , 191px 1122px #fff , 1783px 1839px #fff , 27px 323px #fff , 1246px 1867px #fff , 100px 1319px #fff , 1840px 621px #fff , 136px 492px #fff , 1362px 677px #fff , 84px 1264px #fff , 1714px 750px #fff , 996px 825px #fff , 70px 1331px #fff , 1556px 219px #fff , 137px 1435px #fff , 656px 917px #fff , 1992px 1136px #fff , 1636px 1238px #fff , 228px 1291px #fff , 1266px 500px #fff , 761px 301px #fff , 268px 1516px #fff , 660px 700px #fff , 1623px 68px #fff , 981px 428px #fff , 578px 1775px #fff , 439px 402px #fff , 1750px 1546px #fff , 51px 1378px #fff , 1248px 929px #fff , 1574px 154px #fff , 1902px 224px #fff , 1189px 831px #fff , 878px 958px #fff , 688px 1523px #fff , 1803px 833px #fff , 767px 864px #fff , 1039px 748px #fff , 1186px 1265px #fff , 1502px 271px #fff , 843px 177px #fff , 54px 1245px #fff , 617px 411px #fff , 807px 1276px #fff , 668px 1729px #fff , 991px 932px #fff , 208px 956px #fff , 1955px 1983px #fff , 1px 1566px #fff , 476px 673px #fff , 1516px 725px #fff , 824px 598px #fff , 876px 90px #fff , 1664px 186px #fff , 1045px 514px #fff , 271px 968px #fff , 1242px 1106px #fff , 695px 1022px #fff , 1808px 681px #fff , 220px 799px #fff , 798px 1683px #fff , 1644px 780px #fff , 829px 1656px #fff , 1830px 187px #fff , 1757px 1803px #fff , 427px 1958px #fff , 1489px 1767px #fff , 668px 1881px #fff , 802px 890px #fff , 1957px 1164px #fff , 340px 1693px #fff , 1433px 637px #fff , 1403px 1113px #fff , 102px 669px #fff , 727px 1575px #fff , 254px 1839px #fff , 20px 848px #fff , 1103px 293px #fff , 76px 92px #fff , 412px 1166px #fff , 1292px 1829px #fff , 367px 1536px #fff , 871px 1081px #fff , 828px 1364px #fff , 1779px 133px #fff , 1657px 695px #fff , 837px 1727px #fff , 1831px 978px #fff , 495px 953px #fff , 1670px 38px #fff , 29px 1715px #fff , 316px 1141px #fff , 958px 1678px #fff , 919px 22px #fff , 459px 1165px #fff , 1976px 1698px #fff , 1877px 1294px #fff , 121px 326px #fff , 961px 1396px #fff , 1556px 1731px #fff , 519px 545px #fff , 1537px 1035px #fff , 1432px 281px #fff , 1788px 882px #fff , 1783px 735px #fff , 1763px 1062px #fff , 1096px 1996px #fff , 1999px 474px #fff , 1494px 759px #fff , 499px 392px #fff , 517px 1435px #fff , 291px 14px #fff , 975px 1509px #fff , 184px 1552px #fff , 1927px 1992px #fff , 731px 1155px #fff , 1126px 378px #fff , 774px 91px #fff , 1136px 1506px #fff , 1043px 421px #fff , 389px 1475px #fff , 1955px 1182px #fff , 815px 1302px #fff , 36px 450px #fff , 1078px 574px #fff , 1290px 1277px #fff , 1840px 19px #fff , 651px 882px #fff , 437px 126px #fff , 1815px 1518px #fff , 140px 1631px #fff , 563px 1601px #fff , 41px 1772px #fff , 314px 609px #fff , 1331px 1439px #fff , 1564px 922px #fff , 806px 1200px #fff , 529px 1620px #fff , 324px 657px #fff , 544px 505px #fff , 1134px 1691px #fff , 905px 297px #fff , 1693px 1171px #fff , 1272px 298px #fff , 687px 666px #fff , 1692px 753px #fff , 865px 61px #fff , 784px 86px #fff , 479px 90px #fff;
  }
  #homeBgStar > .star:nth-child(2) {
    -webkit-box-shadow: 1192px 1087px #fff , 1733px 804px #fff , 1954px 659px #fff , 302px 612px #fff , 400px 1646px #fff , 1757px 860px #fff , 983px 972px #fff , 1223px 1797px #fff , 690px 1166px #fff , 914px 1511px #fff , 1038px 1012px #fff , 978px 1680px #fff , 377px 721px #fff , 732px 1312px #fff , 868px 1016px #fff , 892px 877px #fff , 1493px 1946px #fff , 1214px 1619px #fff , 172px 1632px #fff , 1389px 1420px #fff , 1512px 1263px #fff , 1545px 1344px #fff , 348px 595px #fff , 930px 1862px #fff , 1354px 841px #fff , 1311px 361px #fff , 777px 865px #fff , 961px 1651px #fff , 129px 1371px #fff , 1768px 1767px #fff , 268px 1312px #fff , 642px 1974px #fff , 914px 862px #fff , 1693px 1684px #fff , 1046px 858px #fff , 791px 143px #fff , 242px 503px #fff , 1349px 34px #fff , 1445px 200px #fff , 647px 781px #fff , 1776px 368px #fff , 1111px 1481px #fff , 357px 1188px #fff , 726px 132px #fff , 1693px 1782px #fff , 474px 131px #fff , 281px 89px #fff , 1139px 374px #fff , 1556px 694px #fff , 388px 157px #fff , 1151px 15px #fff , 1066px 1506px #fff , 587px 769px #fff , 1523px 237px #fff , 915px 41px #fff , 1565px 850px #fff , 552px 759px #fff , 1145px 529px #fff , 1339px 377px #fff , 170px 446px #fff , 1474px 1033px #fff , 1656px 747px #fff , 147px 1676px #fff , 63px 217px #fff , 1464px 59px #fff , 1423px 1927px #fff , 1971px 326px #fff , 1064px 1073px #fff , 183px 244px #fff , 1582px 762px #fff , 343px 649px #fff , 12px 1499px #fff , 144px 285px #fff , 315px 1932px #fff , 291px 651px #fff , 1255px 610px #fff , 1010px 358px #fff , 1158px 1765px #fff , 1482px 153px #fff , 1807px 176px #fff , 771px 1771px #fff , 1898px 1477px #fff , 1560px 102px #fff , 125px 1402px #fff , 725px 702px #fff , 1536px 1658px #fff , 217px 1372px #fff , 1075px 591px #fff , 1160px 707px #fff , 661px 751px #fff , 1813px 1731px #fff , 1815px 879px #fff , 658px 239px #fff , 1053px 540px #fff , 1732px 37px #fff , 35px 779px #fff , 1608px 1905px #fff , 1930px 587px #fff , 586px 1767px #fff , 1341px 79px #fff , 1608px 1379px #fff , 936px 997px #fff , 453px 760px #fff , 1662px 1839px #fff , 55px 939px #fff , 312px 596px #fff , 800px 257px #fff , 711px 1138px #fff , 669px 1307px #fff , 1465px 1514px #fff , 1536px 1163px #fff , 1195px 1255px #fff , 1247px 715px #fff , 547px 224px #fff , 302px 970px #fff , 167px 1999px #fff , 1551px 1417px #fff , 1751px 258px #fff , 1823px 1826px #fff , 742px 1245px #fff , 1018px 242px #fff , 1438px 848px #fff , 1658px 454px #fff , 1748px 1401px #fff , 485px 1519px #fff , 751px 916px #fff , 1434px 1154px #fff , 136px 127px #fff , 1525px 1483px #fff , 885px 667px #fff , 693px 1075px #fff , 1453px 557px #fff , 883px 539px #fff , 494px 858px #fff , 1622px 1292px #fff , 1486px 12px #fff , 399px 595px #fff , 1993px 86px #fff , 1948px 1001px #fff , 698px 1700px #fff , 1054px 1082px #fff , 104px 1209px #fff , 266px 425px #fff , 1602px 1306px #fff , 1823px 881px #fff , 1106px 1524px #fff , 724px 808px #fff , 615px 358px #fff , 1121px 1958px #fff , 1050px 344px #fff;
            box-shadow: 1192px 1087px #fff , 1733px 804px #fff , 1954px 659px #fff , 302px 612px #fff , 400px 1646px #fff , 1757px 860px #fff , 983px 972px #fff , 1223px 1797px #fff , 690px 1166px #fff , 914px 1511px #fff , 1038px 1012px #fff , 978px 1680px #fff , 377px 721px #fff , 732px 1312px #fff , 868px 1016px #fff , 892px 877px #fff , 1493px 1946px #fff , 1214px 1619px #fff , 172px 1632px #fff , 1389px 1420px #fff , 1512px 1263px #fff , 1545px 1344px #fff , 348px 595px #fff , 930px 1862px #fff , 1354px 841px #fff , 1311px 361px #fff , 777px 865px #fff , 961px 1651px #fff , 129px 1371px #fff , 1768px 1767px #fff , 268px 1312px #fff , 642px 1974px #fff , 914px 862px #fff , 1693px 1684px #fff , 1046px 858px #fff , 791px 143px #fff , 242px 503px #fff , 1349px 34px #fff , 1445px 200px #fff , 647px 781px #fff , 1776px 368px #fff , 1111px 1481px #fff , 357px 1188px #fff , 726px 132px #fff , 1693px 1782px #fff , 474px 131px #fff , 281px 89px #fff , 1139px 374px #fff , 1556px 694px #fff , 388px 157px #fff , 1151px 15px #fff , 1066px 1506px #fff , 587px 769px #fff , 1523px 237px #fff , 915px 41px #fff , 1565px 850px #fff , 552px 759px #fff , 1145px 529px #fff , 1339px 377px #fff , 170px 446px #fff , 1474px 1033px #fff , 1656px 747px #fff , 147px 1676px #fff , 63px 217px #fff , 1464px 59px #fff , 1423px 1927px #fff , 1971px 326px #fff , 1064px 1073px #fff , 183px 244px #fff , 1582px 762px #fff , 343px 649px #fff , 12px 1499px #fff , 144px 285px #fff , 315px 1932px #fff , 291px 651px #fff , 1255px 610px #fff , 1010px 358px #fff , 1158px 1765px #fff , 1482px 153px #fff , 1807px 176px #fff , 771px 1771px #fff , 1898px 1477px #fff , 1560px 102px #fff , 125px 1402px #fff , 725px 702px #fff , 1536px 1658px #fff , 217px 1372px #fff , 1075px 591px #fff , 1160px 707px #fff , 661px 751px #fff , 1813px 1731px #fff , 1815px 879px #fff , 658px 239px #fff , 1053px 540px #fff , 1732px 37px #fff , 35px 779px #fff , 1608px 1905px #fff , 1930px 587px #fff , 586px 1767px #fff , 1341px 79px #fff , 1608px 1379px #fff , 936px 997px #fff , 453px 760px #fff , 1662px 1839px #fff , 55px 939px #fff , 312px 596px #fff , 800px 257px #fff , 711px 1138px #fff , 669px 1307px #fff , 1465px 1514px #fff , 1536px 1163px #fff , 1195px 1255px #fff , 1247px 715px #fff , 547px 224px #fff , 302px 970px #fff , 167px 1999px #fff , 1551px 1417px #fff , 1751px 258px #fff , 1823px 1826px #fff , 742px 1245px #fff , 1018px 242px #fff , 1438px 848px #fff , 1658px 454px #fff , 1748px 1401px #fff , 485px 1519px #fff , 751px 916px #fff , 1434px 1154px #fff , 136px 127px #fff , 1525px 1483px #fff , 885px 667px #fff , 693px 1075px #fff , 1453px 557px #fff , 883px 539px #fff , 494px 858px #fff , 1622px 1292px #fff , 1486px 12px #fff , 399px 595px #fff , 1993px 86px #fff , 1948px 1001px #fff , 698px 1700px #fff , 1054px 1082px #fff , 104px 1209px #fff , 266px 425px #fff , 1602px 1306px #fff , 1823px 881px #fff , 1106px 1524px #fff , 724px 808px #fff , 615px 358px #fff , 1121px 1958px #fff , 1050px 344px #fff;
  }
  #homeBgStar > .star:nth-child(2):after {
    -webkit-box-shadow: 1192px 1087px #fff , 1733px 804px #fff , 1954px 659px #fff , 302px 612px #fff , 400px 1646px #fff , 1757px 860px #fff , 983px 972px #fff , 1223px 1797px #fff , 690px 1166px #fff , 914px 1511px #fff , 1038px 1012px #fff , 978px 1680px #fff , 377px 721px #fff , 732px 1312px #fff , 868px 1016px #fff , 892px 877px #fff , 1493px 1946px #fff , 1214px 1619px #fff , 172px 1632px #fff , 1389px 1420px #fff , 1512px 1263px #fff , 1545px 1344px #fff , 348px 595px #fff , 930px 1862px #fff , 1354px 841px #fff , 1311px 361px #fff , 777px 865px #fff , 961px 1651px #fff , 129px 1371px #fff , 1768px 1767px #fff , 268px 1312px #fff , 642px 1974px #fff , 914px 862px #fff , 1693px 1684px #fff , 1046px 858px #fff , 791px 143px #fff , 242px 503px #fff , 1349px 34px #fff , 1445px 200px #fff , 647px 781px #fff , 1776px 368px #fff , 1111px 1481px #fff , 357px 1188px #fff , 726px 132px #fff , 1693px 1782px #fff , 474px 131px #fff , 281px 89px #fff , 1139px 374px #fff , 1556px 694px #fff , 388px 157px #fff , 1151px 15px #fff , 1066px 1506px #fff , 587px 769px #fff , 1523px 237px #fff , 915px 41px #fff , 1565px 850px #fff , 552px 759px #fff , 1145px 529px #fff , 1339px 377px #fff , 170px 446px #fff , 1474px 1033px #fff , 1656px 747px #fff , 147px 1676px #fff , 63px 217px #fff , 1464px 59px #fff , 1423px 1927px #fff , 1971px 326px #fff , 1064px 1073px #fff , 183px 244px #fff , 1582px 762px #fff , 343px 649px #fff , 12px 1499px #fff , 144px 285px #fff , 315px 1932px #fff , 291px 651px #fff , 1255px 610px #fff , 1010px 358px #fff , 1158px 1765px #fff , 1482px 153px #fff , 1807px 176px #fff , 771px 1771px #fff , 1898px 1477px #fff , 1560px 102px #fff , 125px 1402px #fff , 725px 702px #fff , 1536px 1658px #fff , 217px 1372px #fff , 1075px 591px #fff , 1160px 707px #fff , 661px 751px #fff , 1813px 1731px #fff , 1815px 879px #fff , 658px 239px #fff , 1053px 540px #fff , 1732px 37px #fff , 35px 779px #fff , 1608px 1905px #fff , 1930px 587px #fff , 586px 1767px #fff , 1341px 79px #fff , 1608px 1379px #fff , 936px 997px #fff , 453px 760px #fff , 1662px 1839px #fff , 55px 939px #fff , 312px 596px #fff , 800px 257px #fff , 711px 1138px #fff , 669px 1307px #fff , 1465px 1514px #fff , 1536px 1163px #fff , 1195px 1255px #fff , 1247px 715px #fff , 547px 224px #fff , 302px 970px #fff , 167px 1999px #fff , 1551px 1417px #fff , 1751px 258px #fff , 1823px 1826px #fff , 742px 1245px #fff , 1018px 242px #fff , 1438px 848px #fff , 1658px 454px #fff , 1748px 1401px #fff , 485px 1519px #fff , 751px 916px #fff , 1434px 1154px #fff , 136px 127px #fff , 1525px 1483px #fff , 885px 667px #fff , 693px 1075px #fff , 1453px 557px #fff , 883px 539px #fff , 494px 858px #fff , 1622px 1292px #fff , 1486px 12px #fff , 399px 595px #fff , 1993px 86px #fff , 1948px 1001px #fff , 698px 1700px #fff , 1054px 1082px #fff , 104px 1209px #fff , 266px 425px #fff , 1602px 1306px #fff , 1823px 881px #fff , 1106px 1524px #fff , 724px 808px #fff , 615px 358px #fff , 1121px 1958px #fff , 1050px 344px #fff;
            box-shadow: 1192px 1087px #fff , 1733px 804px #fff , 1954px 659px #fff , 302px 612px #fff , 400px 1646px #fff , 1757px 860px #fff , 983px 972px #fff , 1223px 1797px #fff , 690px 1166px #fff , 914px 1511px #fff , 1038px 1012px #fff , 978px 1680px #fff , 377px 721px #fff , 732px 1312px #fff , 868px 1016px #fff , 892px 877px #fff , 1493px 1946px #fff , 1214px 1619px #fff , 172px 1632px #fff , 1389px 1420px #fff , 1512px 1263px #fff , 1545px 1344px #fff , 348px 595px #fff , 930px 1862px #fff , 1354px 841px #fff , 1311px 361px #fff , 777px 865px #fff , 961px 1651px #fff , 129px 1371px #fff , 1768px 1767px #fff , 268px 1312px #fff , 642px 1974px #fff , 914px 862px #fff , 1693px 1684px #fff , 1046px 858px #fff , 791px 143px #fff , 242px 503px #fff , 1349px 34px #fff , 1445px 200px #fff , 647px 781px #fff , 1776px 368px #fff , 1111px 1481px #fff , 357px 1188px #fff , 726px 132px #fff , 1693px 1782px #fff , 474px 131px #fff , 281px 89px #fff , 1139px 374px #fff , 1556px 694px #fff , 388px 157px #fff , 1151px 15px #fff , 1066px 1506px #fff , 587px 769px #fff , 1523px 237px #fff , 915px 41px #fff , 1565px 850px #fff , 552px 759px #fff , 1145px 529px #fff , 1339px 377px #fff , 170px 446px #fff , 1474px 1033px #fff , 1656px 747px #fff , 147px 1676px #fff , 63px 217px #fff , 1464px 59px #fff , 1423px 1927px #fff , 1971px 326px #fff , 1064px 1073px #fff , 183px 244px #fff , 1582px 762px #fff , 343px 649px #fff , 12px 1499px #fff , 144px 285px #fff , 315px 1932px #fff , 291px 651px #fff , 1255px 610px #fff , 1010px 358px #fff , 1158px 1765px #fff , 1482px 153px #fff , 1807px 176px #fff , 771px 1771px #fff , 1898px 1477px #fff , 1560px 102px #fff , 125px 1402px #fff , 725px 702px #fff , 1536px 1658px #fff , 217px 1372px #fff , 1075px 591px #fff , 1160px 707px #fff , 661px 751px #fff , 1813px 1731px #fff , 1815px 879px #fff , 658px 239px #fff , 1053px 540px #fff , 1732px 37px #fff , 35px 779px #fff , 1608px 1905px #fff , 1930px 587px #fff , 586px 1767px #fff , 1341px 79px #fff , 1608px 1379px #fff , 936px 997px #fff , 453px 760px #fff , 1662px 1839px #fff , 55px 939px #fff , 312px 596px #fff , 800px 257px #fff , 711px 1138px #fff , 669px 1307px #fff , 1465px 1514px #fff , 1536px 1163px #fff , 1195px 1255px #fff , 1247px 715px #fff , 547px 224px #fff , 302px 970px #fff , 167px 1999px #fff , 1551px 1417px #fff , 1751px 258px #fff , 1823px 1826px #fff , 742px 1245px #fff , 1018px 242px #fff , 1438px 848px #fff , 1658px 454px #fff , 1748px 1401px #fff , 485px 1519px #fff , 751px 916px #fff , 1434px 1154px #fff , 136px 127px #fff , 1525px 1483px #fff , 885px 667px #fff , 693px 1075px #fff , 1453px 557px #fff , 883px 539px #fff , 494px 858px #fff , 1622px 1292px #fff , 1486px 12px #fff , 399px 595px #fff , 1993px 86px #fff , 1948px 1001px #fff , 698px 1700px #fff , 1054px 1082px #fff , 104px 1209px #fff , 266px 425px #fff , 1602px 1306px #fff , 1823px 881px #fff , 1106px 1524px #fff , 724px 808px #fff , 615px 358px #fff , 1121px 1958px #fff , 1050px 344px #fff;
  }
  #homeBgStar > .star:nth-child(3) {
    -webkit-box-shadow: 1362px 266px #fff , 1678px 1840px #fff , 45px 276px #fff , 1158px 1388px #fff , 1257px 1506px #fff , 93px 686px #fff , 809px 702px #fff , 1354px 1583px #fff , 1144px 1609px #fff , 66px 297px #fff , 787px 297px #fff , 1556px 1437px #fff , 50px 648px #fff , 787px 1676px #fff , 310px 263px #fff , 1511px 1073px #fff , 513px 1758px #fff , 618px 1456px #fff , 1988px 578px #fff , 1886px 991px #fff , 1101px 138px #fff , 1140px 1568px #fff , 1236px 1048px #fff , 757px 1539px #fff , 1205px 308px #fff , 84px 1817px #fff , 1408px 1616px #fff , 1092px 625px #fff , 1946px 361px #fff , 759px 155px #fff , 1543px 759px #fff , 628px 1800px #fff , 715px 371px #fff , 891px 1605px #fff , 966px 1535px #fff , 1281px 1298px #fff , 1444px 73px #fff , 168px 1144px #fff , 61px 970px #fff , 980px 162px #fff , 772px 1574px #fff , 538px 1970px #fff , 724px 734px #fff , 1974px 1291px #fff , 545px 580px #fff , 451px 642px #fff , 1178px 1840px #fff , 1717px 764px #fff , 1934px 1209px #fff , 1400px 1220px #fff , 1915px 1421px #fff , 1564px 1436px #fff , 1521px 14px #fff , 492px 1663px #fff , 597px 887px #fff , 792px 89px #fff , 1812px 1771px #fff , 828px 387px #fff , 830px 657px #fff , 290px 1673px #fff , 1324px 301px #fff , 1588px 694px #fff , 470px 1641px #fff , 1929px 1938px #fff , 1387px 1647px #fff , 304px 382px #fff , 1736px 101px #fff , 676px 19px #fff , 1145px 540px #fff , 1537px 1200px #fff , 1406px 1135px #fff , 633px 1040px #fff , 1679px 534px #fff , 1951px 412px #fff , 369px 624px #fff , 1448px 67px #fff , 1881px 1881px #fff , 749px 628px #fff , 1049px 163px #fff , 16px 1359px #fff , 1637px 36px #fff , 1636px 1996px #fff , 848px 1432px #fff , 1581px 619px #fff , 1431px 1344px #fff , 205px 289px #fff , 1504px 390px #fff , 1986px 1377px #fff , 42px 831px #fff , 385px 591px #fff , 58px 829px #fff , 165px 1218px #fff , 1787px 730px #fff , 1766px 1997px #fff , 1251px 1955px #fff , 644px 1380px #fff , 1476px 1606px #fff , 1843px 94px #fff , 1678px 549px #fff , 243px 1148px #fff;
            box-shadow: 1362px 266px #fff , 1678px 1840px #fff , 45px 276px #fff , 1158px 1388px #fff , 1257px 1506px #fff , 93px 686px #fff , 809px 702px #fff , 1354px 1583px #fff , 1144px 1609px #fff , 66px 297px #fff , 787px 297px #fff , 1556px 1437px #fff , 50px 648px #fff , 787px 1676px #fff , 310px 263px #fff , 1511px 1073px #fff , 513px 1758px #fff , 618px 1456px #fff , 1988px 578px #fff , 1886px 991px #fff , 1101px 138px #fff , 1140px 1568px #fff , 1236px 1048px #fff , 757px 1539px #fff , 1205px 308px #fff , 84px 1817px #fff , 1408px 1616px #fff , 1092px 625px #fff , 1946px 361px #fff , 759px 155px #fff , 1543px 759px #fff , 628px 1800px #fff , 715px 371px #fff , 891px 1605px #fff , 966px 1535px #fff , 1281px 1298px #fff , 1444px 73px #fff , 168px 1144px #fff , 61px 970px #fff , 980px 162px #fff , 772px 1574px #fff , 538px 1970px #fff , 724px 734px #fff , 1974px 1291px #fff , 545px 580px #fff , 451px 642px #fff , 1178px 1840px #fff , 1717px 764px #fff , 1934px 1209px #fff , 1400px 1220px #fff , 1915px 1421px #fff , 1564px 1436px #fff , 1521px 14px #fff , 492px 1663px #fff , 597px 887px #fff , 792px 89px #fff , 1812px 1771px #fff , 828px 387px #fff , 830px 657px #fff , 290px 1673px #fff , 1324px 301px #fff , 1588px 694px #fff , 470px 1641px #fff , 1929px 1938px #fff , 1387px 1647px #fff , 304px 382px #fff , 1736px 101px #fff , 676px 19px #fff , 1145px 540px #fff , 1537px 1200px #fff , 1406px 1135px #fff , 633px 1040px #fff , 1679px 534px #fff , 1951px 412px #fff , 369px 624px #fff , 1448px 67px #fff , 1881px 1881px #fff , 749px 628px #fff , 1049px 163px #fff , 16px 1359px #fff , 1637px 36px #fff , 1636px 1996px #fff , 848px 1432px #fff , 1581px 619px #fff , 1431px 1344px #fff , 205px 289px #fff , 1504px 390px #fff , 1986px 1377px #fff , 42px 831px #fff , 385px 591px #fff , 58px 829px #fff , 165px 1218px #fff , 1787px 730px #fff , 1766px 1997px #fff , 1251px 1955px #fff , 644px 1380px #fff , 1476px 1606px #fff , 1843px 94px #fff , 1678px 549px #fff , 243px 1148px #fff;
  }
  #homeBgStar > .star:nth-child(3):after {
    -webkit-box-shadow: 1362px 266px #fff , 1678px 1840px #fff , 45px 276px #fff , 1158px 1388px #fff , 1257px 1506px #fff , 93px 686px #fff , 809px 702px #fff , 1354px 1583px #fff , 1144px 1609px #fff , 66px 297px #fff , 787px 297px #fff , 1556px 1437px #fff , 50px 648px #fff , 787px 1676px #fff , 310px 263px #fff , 1511px 1073px #fff , 513px 1758px #fff , 618px 1456px #fff , 1988px 578px #fff , 1886px 991px #fff , 1101px 138px #fff , 1140px 1568px #fff , 1236px 1048px #fff , 757px 1539px #fff , 1205px 308px #fff , 84px 1817px #fff , 1408px 1616px #fff , 1092px 625px #fff , 1946px 361px #fff , 759px 155px #fff , 1543px 759px #fff , 628px 1800px #fff , 715px 371px #fff , 891px 1605px #fff , 966px 1535px #fff , 1281px 1298px #fff , 1444px 73px #fff , 168px 1144px #fff , 61px 970px #fff , 980px 162px #fff , 772px 1574px #fff , 538px 1970px #fff , 724px 734px #fff , 1974px 1291px #fff , 545px 580px #fff , 451px 642px #fff , 1178px 1840px #fff , 1717px 764px #fff , 1934px 1209px #fff , 1400px 1220px #fff , 1915px 1421px #fff , 1564px 1436px #fff , 1521px 14px #fff , 492px 1663px #fff , 597px 887px #fff , 792px 89px #fff , 1812px 1771px #fff , 828px 387px #fff , 830px 657px #fff , 290px 1673px #fff , 1324px 301px #fff , 1588px 694px #fff , 470px 1641px #fff , 1929px 1938px #fff , 1387px 1647px #fff , 304px 382px #fff , 1736px 101px #fff , 676px 19px #fff , 1145px 540px #fff , 1537px 1200px #fff , 1406px 1135px #fff , 633px 1040px #fff , 1679px 534px #fff , 1951px 412px #fff , 369px 624px #fff , 1448px 67px #fff , 1881px 1881px #fff , 749px 628px #fff , 1049px 163px #fff , 16px 1359px #fff , 1637px 36px #fff , 1636px 1996px #fff , 848px 1432px #fff , 1581px 619px #fff , 1431px 1344px #fff , 205px 289px #fff , 1504px 390px #fff , 1986px 1377px #fff , 42px 831px #fff , 385px 591px #fff , 58px 829px #fff , 165px 1218px #fff , 1787px 730px #fff , 1766px 1997px #fff , 1251px 1955px #fff , 644px 1380px #fff , 1476px 1606px #fff , 1843px 94px #fff , 1678px 549px #fff , 243px 1148px #fff;
            box-shadow: 1362px 266px #fff , 1678px 1840px #fff , 45px 276px #fff , 1158px 1388px #fff , 1257px 1506px #fff , 93px 686px #fff , 809px 702px #fff , 1354px 1583px #fff , 1144px 1609px #fff , 66px 297px #fff , 787px 297px #fff , 1556px 1437px #fff , 50px 648px #fff , 787px 1676px #fff , 310px 263px #fff , 1511px 1073px #fff , 513px 1758px #fff , 618px 1456px #fff , 1988px 578px #fff , 1886px 991px #fff , 1101px 138px #fff , 1140px 1568px #fff , 1236px 1048px #fff , 757px 1539px #fff , 1205px 308px #fff , 84px 1817px #fff , 1408px 1616px #fff , 1092px 625px #fff , 1946px 361px #fff , 759px 155px #fff , 1543px 759px #fff , 628px 1800px #fff , 715px 371px #fff , 891px 1605px #fff , 966px 1535px #fff , 1281px 1298px #fff , 1444px 73px #fff , 168px 1144px #fff , 61px 970px #fff , 980px 162px #fff , 772px 1574px #fff , 538px 1970px #fff , 724px 734px #fff , 1974px 1291px #fff , 545px 580px #fff , 451px 642px #fff , 1178px 1840px #fff , 1717px 764px #fff , 1934px 1209px #fff , 1400px 1220px #fff , 1915px 1421px #fff , 1564px 1436px #fff , 1521px 14px #fff , 492px 1663px #fff , 597px 887px #fff , 792px 89px #fff , 1812px 1771px #fff , 828px 387px #fff , 830px 657px #fff , 290px 1673px #fff , 1324px 301px #fff , 1588px 694px #fff , 470px 1641px #fff , 1929px 1938px #fff , 1387px 1647px #fff , 304px 382px #fff , 1736px 101px #fff , 676px 19px #fff , 1145px 540px #fff , 1537px 1200px #fff , 1406px 1135px #fff , 633px 1040px #fff , 1679px 534px #fff , 1951px 412px #fff , 369px 624px #fff , 1448px 67px #fff , 1881px 1881px #fff , 749px 628px #fff , 1049px 163px #fff , 16px 1359px #fff , 1637px 36px #fff , 1636px 1996px #fff , 848px 1432px #fff , 1581px 619px #fff , 1431px 1344px #fff , 205px 289px #fff , 1504px 390px #fff , 1986px 1377px #fff , 42px 831px #fff , 385px 591px #fff , 58px 829px #fff , 165px 1218px #fff , 1787px 730px #fff , 1766px 1997px #fff , 1251px 1955px #fff , 644px 1380px #fff , 1476px 1606px #fff , 1843px 94px #fff , 1678px 549px #fff , 243px 1148px #fff;
  }
}

@-webkit-keyframes animationStar {
  from {
    -webkit-transform: translateY(0px);
            transform: translateY(0px);
  }
  to {
    -webkit-transform: translateY(-2000px);
            transform: translateY(-2000px);
  }
}

@-o-keyframes animationStar {
  from {
    -o-transform: translateY(0px);
       transform: translateY(0px);
  }
  to {
    -o-transform: translateY(-2000px);
       transform: translateY(-2000px);
  }
}

@keyframes animationStar {
  from {
    -webkit-transform: translateY(0px);
         -o-transform: translateY(0px);
            transform: translateY(0px);
  }
  to {
    -webkit-transform: translateY(-2000px);
         -o-transform: translateY(-2000px);
            transform: translateY(-2000px);
  }
}
#homeBgParticle {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgSnow {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgAnimatedGradient {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgShootingStars {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  overflow: hidden;
  height: 100%;
  width: 100%;
}

#homeBgYoutube,
#homeBgYoutubeFallback,
#homeBgYoutubePlaceholder,
#homeBgYoutubePlayer {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

#homeBgMap {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

/**
 * service
 * ---------------------------------------------------------
 */
.service-section {
  padding-top: 3.75rem;
  padding-bottom: 3.75rem;
  background-color: #f7fbfe;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .service-section {
    padding-top: 5rem;
    padding-bottom: 5rem;
  }
}

.service-row {
  text-align: center;
}
.service-row > .iconbox {
  margin-bottom: 2.25rem;
}
.service-row > .iconbox:last-child {
  margin-bottom: 0;
}
@media (min-width: 768px) {
  .service-row > .iconbox {
    margin-bottom: 2.25rem;
  }
  .service-row > .iconbox:nth-child(3), .service-row > .iconbox:nth-child(4) {
    margin-bottom: 0;
  }
}
@media (min-width: 992px) {
  .service-row > .iconbox {
    margin-bottom: 0;
  }
}

/**
 * feature 1
 * ---------------------------------------------------------
 */
.feature1-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .feature1-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (min-width: 768px) {
  .feature-1-row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
       -moz-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
}

@media (max-width: 767px) {
  .feature-1-left-col {
    margin-bottom: 3rem;
  }
}

.feature-media-row {
  margin-top: -1.5rem;
}

.feature-media-col {
  margin-top: 1.5rem;
}

@media (max-width: 767px) {
  .feature-media .media-left {
    display: block;
  }
}
.feature-media .media-icon {
  width: 3rem;
  height: 3rem;
  font-size: 2.25rem;
}

@media (min-width: 768px) {
  .feature-media .media-left {
    padding-top: 0.25rem;
    padding-right: 1.25rem;
  }
}
/**
 * feature 2
 * ---------------------------------------------------------
 */
.feature2-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #f7fbfe;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .feature2-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (min-width: 768px) {
  .feature-2-right-col .btn-wrap > .btn:first-child {
    margin-left: 0;
  }
}
@media (min-width: 768px) {
  .feature-2-right-col {
    float: right;
  }
}
@media (max-width: 767px) {
  .feature-2-right-col {
    margin-bottom: 3rem;
  }
}

.feature-list {
  padding-left: 0;
  list-style: none;
}
.feature-list > li {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  font-size: 1rem;
  line-height: 1.625;
}
.feature-list > li > .icon {
  color: #58cc65;
  margin-right: 1em;
}

/**
 * skill
 * ---------------------------------------------------------
 */
.skill-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #f7fbfe;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .skill-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (min-width: 768px) {
  .skill-row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
       -moz-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
}

@media (max-width: 767px) {
  .skill-left-col {
    margin-bottom: 3rem;
    text-align: center;
  }
}
@media (min-width: 768px) {
  .skill-left-col .btn-wrap > .btn:first-child {
    margin-left: 0;
  }
}

@media (max-width: 767px) {
  .skill-right-col {
    max-width: 30rem;
    margin-right: auto;
    margin-left: auto;
  }
}
.skill-right-col .progress {
  margin-bottom: 2rem;
}
.skill-right-col .hint-text {
  color: #757575;
  margin-top: 3rem;
}

/**
 * screenshot
 * --------------------------------------------------
 */
.screenshot-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .screenshot-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

.screenshot-title-row {
  margin-bottom: 6rem;
}

.screenshot-title-col {
  text-align: center;
}

#screenshotCarousel.bfc-carousel {
  margin-right: -0.9375rem;
  margin-left: -0.9375rem;
}
#screenshotCarousel.bfc-carousel:before, #screenshotCarousel.bfc-carousel:after {
  content: "";
  display: table;
}
#screenshotCarousel.bfc-carousel:after {
  clear: both;
}
#screenshotCarousel.bfc-carousel.no-gutter {
  margin-right: 0;
  margin-left: 0;
}
#screenshotCarousel.bfc-carousel.no-gutter .bfc-carousel-item {
  padding-right: 0;
  padding-left: 0;
}
#screenshotCarousel .slick-slide {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
  -webkit-transition-property: -webkit-transform opacity;
       -o-transition-property: -o-transform opacity;
          transition-property: transform opacity;
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
}
#screenshotCarousel .slick-slide:not(.slick-center) {
  -webkit-transform: scale(0.9);
      -ms-transform: scale(0.9);
       -o-transform: scale(0.9);
          transform: scale(0.9);
  opacity: .85;
}
#screenshotCarousel .bfc-carousel-item-media-img {
  display: block;
  max-width: 100%;
  height: auto;
  margin-right: auto;
  margin-left: auto;
}
#screenshotCarousel .slick-prev {
  left: 0;
}
#screenshotCarousel .slick-next {
  right: 0;
}
#screenshotCarousel .slick-prev,
#screenshotCarousel .slick-next {
  display: block;
  width: 2.25rem;
  height: 2.25rem;
  z-index: 10;
}
#screenshotCarousel .slick-prev:before,
#screenshotCarousel .slick-next:before {
  font-size: 2.25rem;
  opacity: .75;
  color: #212121;
  font-family: "themify";
}
#screenshotCarousel .slick-prev:before {
  content: "\e64a";
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.12);
}
#screenshotCarousel .slick-next:before {
  content: "\e649";
  text-shadow: -1px 1px 2px rgba(0, 0, 0, 0.12);
}

/**
 * watch-video
 * ---------------------------------------------------------
 */
.watch-video-section {
  background-color: #8a65c5;
  color: #fff;
  position: relative;
  overflow: hidden;
  padding-top: 5rem;
  padding-bottom: 5rem;
}
@media (min-width: 992px) {
  .watch-video-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

.text-cover {
  position: absolute;
  top: 0;
  font-size: 10vw;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.08);
}
.text-cover.top {
  top: 0;
}
.text-cover.bottom {
  bottom: 0;
}
.text-cover.right {
  right: 1vh;
}
.text-cover.left {
  left: 1vh;
}
@media (max-width: 767px) {
  .text-cover {
    display: none;
  }
}

@media (min-width: 768px) {
  .watch-video-row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -webkit-flex-direction: row;
       -moz-box-orient: horizontal;
       -moz-box-direction: normal;
        -ms-flex-direction: row;
            flex-direction: row;
    -webkit-box-align: center;
    -webkit-align-items: center;
       -moz-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
}

@media (max-width: 767px) {
  .watch-video-left-col {
    margin-bottom: 3rem;
    text-align: center;
  }
}

.watch-video-icon {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
  -webkit-transition-property: -webkit-box-shadow;
       -o-transition-property: box-shadow;
          transition-property: box-shadow;
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -moz-inline-box;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
     -moz-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  width: 4.375rem;
  height: 4.375rem;
  margin-bottom: 1.5rem;
  -webkit-box-shadow: 0 2px 6px 2px rgba(0, 0, 0, 0.05);
          box-shadow: 0 2px 6px 2px rgba(0, 0, 0, 0.05);
  -webkit-border-radius: 50%;
          border-radius: 50%;
  background-color: #fff;
  color: #8a65c5;
  font-size: 2.25rem;
}
.no-flexbox .watch-video-icon {
  display: inline-block;
  line-height: 1.944444444444445;
  text-align: center;
}
.watch-video-icon:hover, .watch-video-icon:focus {
  -webkit-box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12), 0 2px 4px -1px rgba(0, 0, 0, 0.4);
          box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12), 0 2px 4px -1px rgba(0, 0, 0, 0.4);
}

.watch-video-right-col {
  margin-bottom: -5rem;
  text-align: center;
}
@media (min-width: 768px) {
  .watch-video-right-col {
    -webkit-align-self: flex-end;
        -ms-flex-item-align: end;
            align-self: flex-end;
  }
}
@media (min-width: 992px) {
  .watch-video-right-col {
    margin-bottom: -6.25rem;
  }
}
.watch-video-right-col > img {
  display: inline-block;
  max-width: 100%;
  height: auto;
}

/**
 * number
 * ---------------------------------------------------------
 */
.number-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  text-align: center;
  background-color: #8a65c5;
  color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .number-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (max-width: 767px) {
  .number-box-col {
    margin-bottom: 2.25rem;
  }
  .number-box-col:nth-child(3), .number-box-col:nth-child(4) {
    margin-bottom: 0;
  }
}

.number-box img {
  width: 5rem;
  margin-bottom: 0.5rem;
}
.number-box h5 {
  line-height: 1.318181818181818;
  margin-bottom: 0.5rem;
  font-size: 2.75rem;
  font-weight: 300;
}
.number-box p {
  line-height: 1.625;
  font-size: 1rem;
  font-weight: 300;
}

/**
 * faq
 * --------------------------------------------------
 */
.faq-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #b6e2a6;
  color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .faq-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (max-width: 991px) {
  .faq-box-col {
    margin-bottom: 2.25rem;
  }
}
.faq-box-col:last-child {
  margin-bottom: 0;
}
.faq-box-col .faq-box {
  margin-bottom: 2.25rem;
}
.faq-box-col .faq-box:last-child {
  margin-bottom: 0;
}
.faq-box-col .faq-box-question {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  margin-bottom: 0.25rem;
}
.faq-box-col .faq-box-question .q {
  display: inline-block;
  vertical-align: middle;
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -moz-inline-box;
  display: -ms-inline-flexbox;
  display: inline-flex;
  text-align: center;
  width: 1.5rem;
  height: 1.5rem;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
     -moz-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  background-color: rgb(61, 184, 219);
  color: #fff;
  margin-right: 1rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.faq-box-col .faq-box-answer {
  line-height: 1.625;
  font-size: 1rem;
  font-weight: 300;
}

/**
 * pricing
 * ---------------------------------------------------------
 */
.pricing-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .pricing-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

@media (max-width: 991px) {
  .pricing-section .pricing-table-col {
    margin-bottom: 2rem;
  }
  .pricing-section .pricing-table-col:last-child {
    margin-bottom: 0;
  }
}
.pricing-section .pricing-table {
  position: relative;
  max-width: 22.5rem;
  margin-right: auto;
  margin-left: auto;
  padding-right: 1.5rem;
  padding-left: 1.5rem;
  background-color: #fff;
  text-align: center;
}
.pricing-section .pricing-table-badge {
  position: absolute;
  top: 0;
  right: 0;
  display: block;
  border-top: 3.75rem solid #8a65c5;
  border-left: 3.75rem solid transparent;
  background-color: transparent;
  color: #fff;
}
.pricing-section .pricing-table-badge:before {
  position: absolute;
  top: -3.1875rem;
  right: 0.5625rem;
  content: "\e60a";
  line-height: 1;
  font-family: 'themify';
  font-size: 1rem;
}
.pricing-section .pricing-table-header {
  padding-top: 2rem;
  padding-bottom: 1.5rem;
}
.pricing-section .pricing-table-header-title {
  font-weight: 700;
  text-transform: uppercase;
}
.pricing-section .pricing-table-media {
  padding-top: 1rem;
  padding-bottom: 1.5rem;
}
.pricing-section .pricing-table-media > img {
  display: inline-block;
}
.pricing-section .pricing-table-price {
  line-height: 1.318181818181818;
  font-size: 2.75rem;
  font-weight: 300;
}
.pricing-section .pricing-table-detail {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}
.pricing-section .pricing-table-detail-item {
  padding-right: 1.5rem;
  padding-left: 1.5rem;
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}
.pricing-section .pricing-table-footer {
  padding-top: 1.5rem;
  padding-bottom: 2rem;
}

/**
 * Download
 * ---------------------------------------------------------
 */
.download-section {
  padding-top: 5rem;
  padding-bottom: 5rem;
  background-color: #8a65c5;
  color: #fff;
  position: relative;
  overflow: hidden;
}
@media (min-width: 992px) {
  .download-section {
    padding-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}
.download-section .section-title {
  margin-bottom: 0;
}

@media (min-width: 768px) {
  .download-row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
       -moz-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
}

@media (max-width: 767px) {
  .download-left-col {
    margin-bottom: 1.5rem;
    text-align: center;
  }
}

.download-right-col {
  text-align: center;
}
@media (min-width: 768px) {
  .download-right-col {
    text-align: right;
  }
}

/**
 * subscribe
 * ---------------------------------------------------------
 */
.popup-form {
  position: relative;
  max-width: 28.125rem;
  margin: 1.5rem auto;
}

.popup-subscribe-form {
  padding-right: 2.25rem;
  padding-left: 2.25rem;
  background-color: #fff;
  text-align: center;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  overflow: hidden;
}
.popup-subscribe-form .popup-subscribe-form-media {
  padding-top: 3.5rem;
  padding-bottom: 2.25rem;
}
.popup-subscribe-form .popup-subscribe-form-media > img {
  display: block;
  margin-right: auto;
  margin-left: auto;
}
.popup-subscribe-form .popup-subscribe-form-title {
  line-height: 1.375;
  font-size: 2rem;
  font-weight: 300;
}
.popup-subscribe-form .popup-subscribe-form-text-lead {
  line-height: 1.625;
  padding-top: 0.25rem;
  padding-bottom: 2rem;
  font-size: 1rem;
  font-weight: 300;
}
.popup-subscribe-form .form-notify {
  margin-top: 1em;
  padding-bottom: 2.25rem;
}

/**
 * contact
 * ---------------------------------------------------------
 */
.contact-section {
  background-color: #fff;
  position: relative;
  overflow: hidden;
}

.contact-title-row {
  padding-top: 5rem;
}
@media (min-width: 992px) {
  .contact-title-row {
    padding-top: 6.25rem;
  }
}

.contact-title-col {
  text-align: center;
}

.content-row{
  color: black;
}

.contact-content-row {
  margin-top: 1rem;
  padding-bottom: 5rem;
}
@media (min-width: 992px) {
  .contact-content-row {
    margin-top: 6.25rem;
    padding-bottom: 6.25rem;
  }
}

.contact-left-col .panel {
  margin-bottom: 0;
  border: 0;
}
.contact-left-col .panel-body {
  color: #212121;
}
@media (max-width: 767px) {
  .contact-left-col {
    margin-bottom: 3rem;
  }
}

.contact-info-col .text-lead {
  margin-bottom: 3rem;
}

.contact-info .media:not(:first-child) {
  margin-top: 1.5rem;
}
.contact-info .media-left {
  padding-right: 1.25rem;
}
.contact-info .media-object {
  width: 3rem;
  height: 3rem;
}

/**
 * map
 * ---------------------------------------------------------
 */
#map-canvas {
  height: 31.25rem;
  margin-top: 5rem;
}
@media (min-width: 992px) {
  #map-canvas {
    margin-top: 6.25rem;
  }
}

/**
 * site-footer
 * ---------------------------------------------------------
 */
.site-footer-top-section {
  padding-top: 5rem;
  background-color: #0a0a0a;
}
@media (min-width: 992px) {
  .site-footer-top-section {
    padding-top: 6.25rem;
    padding-bottom: 3.125rem;
  }
}
.site-footer-top-section .section-title {
  margin-bottom: 0;
  color: #fff;
}

.site-footer-top-col {
  text-align: center;
}

.site-footer-bottom-section {
  padding-top: 2rem;
  padding-bottom: 2rem;
  background-color: #0a0a0a;
  color: rgba(255, 255, 255, 0.5);
}

.site-footer-bottom-border {
  padding-top: 2rem;
  border-top: 0.0625rem solid rgba(255, 255, 255, 0.12);
}

@media (max-width: 991px) {
  .site-footer-bottom-left-col {
    margin-bottom: 1.5rem;
    text-align: center;
  }
}

.site-footer-brand {
  line-height: 1.555555555555556;
  margin-bottom: 0.5rem;
  color: white;
  font-size: 1.125rem;
  font-weight: 700;
}
.site-footer-brand > span {
  font-weight: 300;
}

.site-footer-bottom-info > ul {
  padding-left: 0;
  list-style: none;
  line-height: 1.846153846153846;
  font-size: 0.8125rem;
}
.site-footer-bottom-info > ul > li {
  display: inline-block;
}
.site-footer-bottom-info > ul > li:not(:last-child):after {
  display: inline-block;
  content: "|";
  margin-right: 1em;
  margin-left: 1em;
  color: rgba(255, 255, 255, 0.5);
}
.site-footer-bottom-info > ul > li > a {
  color: rgba(255, 255, 255, 0.5);
}
.site-footer-bottom-info > ul > li > a:hover {
  color: white;
}

@media (max-width: 991px) {
  .site-footer-bottom-right-col {
    text-align: center;
  }
}
@media (min-width: 992px) {
  .site-footer-bottom-right-col {
    text-align: right;
  }
}

.site-footer-bottom-social-list {
  padding-left: 0;
  list-style: none;
  margin-bottom: 0.75rem;
}
.site-footer-bottom-social-list > li {
  display: inline-block;
  padding-right: 0.5rem;
  padding-left: 0.5rem;
}
.site-footer-bottom-social-list > li > a {
  color: rgba(255, 255, 255, 0.5);
}
.site-footer-bottom-social-list > li > a:hover {
  color: white;
}

.site-footer-bottom-copyright {
  line-height: 1.846153846153846;
}

#footerSubscribeForm {
  margin-top: 8px;
}
#footerSubscribeForm .form-notify {
  color: #fff;
  margin: 16px 0 0;
}
@media (max-width: 767px) {
  #footerSubscribeForm {
    margin-top: 1.5rem;
  }
}

/**
 * base
 * ---------------------------------------------------------
 */
/**
 * btn
 * ---------------------------------------------------------
 */
.btn {
  display: -webkit-inline-box;
  display: -webkit-inline-flex;
  display: -moz-inline-box;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
     -moz-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  line-height: 1;
  border-width: 0.0625rem;
  font-weight: 500;
}
.is-desktop .btn {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
}

.btn:focus, .btn.focus, .btn:active:focus, .btn:active.focus, .btn.active:focus, .btn.active.focus {
  outline: dotted thin;
  outline: -webkit-focus-ring-color auto 5px;
  outline-offset: -2px;
}
.btn:hover, .btn:focus, .btn.focus {
  color: #212121;
}
.btn:active, .btn.active {
  -webkit-box-shadow: none;
          box-shadow: none;
}
.btn.disabled, .btn[disabled], fieldset[disabled] .btn {
  cursor: default;
}

.btn-theme-1 {
  color: white;
  background-color: #8a65c5;
  border-color: #8a65c5;
}
.btn-theme-1:focus, .btn-theme-1.focus {
  border-color: #7555a7;
  background-color: #7555a7;
  color: white;
}
.btn-theme-1:hover {
  border-color: #7555a7;
  background-color: #7555a7;
  color: white;
}
.btn-theme-1:active, .btn-theme-1.active, .open > .btn-theme-1.dropdown-toggle {
  border-color: #7555a7;
  background-color: #7555a7;
  color: white;
}
.btn-theme-1:active:hover, .btn-theme-1:active:focus, .btn-theme-1:active.focus, .btn-theme-1.active:hover, .btn-theme-1.active:focus, .btn-theme-1.active.focus, .open > .btn-theme-1.dropdown-toggle:hover, .open > .btn-theme-1.dropdown-toggle:focus, .open > .btn-theme-1.dropdown-toggle.focus {
  border-color: #7555a7;
  background-color: #7555a7;
  color: white;
}
.btn-theme-1:active, .btn-theme-1.active, .open > .btn-theme-1.dropdown-toggle {
  background-image: none;
}
.btn-theme-1.disabled:hover, .btn-theme-1.disabled:focus, .btn-theme-1.disabled.focus, .btn-theme-1[disabled]:hover, .btn-theme-1[disabled]:focus, .btn-theme-1[disabled].focus, fieldset[disabled] .btn-theme-1:hover, fieldset[disabled] .btn-theme-1:focus, fieldset[disabled] .btn-theme-1.focus {
  border-color: #8a65c5;
  background-color: #8a65c5;
}
.btn-theme-1 .badge {
  background-color: white;
  color: #8a65c5;
}

.btn-theme-2 {
  color: white;
  background-color: #3db8db;
  border-color: #3db8db;
}
.btn-theme-2:focus, .btn-theme-2.focus {
  border-color: #339cba;
  background-color: #339cba;
  color: white;
}
.btn-theme-2:hover {
  border-color: #339cba;
  background-color: #339cba;
  color: white;
}
.btn-theme-2:active, .btn-theme-2.active, .open > .btn-theme-2.dropdown-toggle {
  border-color: #339cba;
  background-color: #339cba;
  color: white;
}
.btn-theme-2:active:hover, .btn-theme-2:active:focus, .btn-theme-2:active.focus, .btn-theme-2.active:hover, .btn-theme-2.active:focus, .btn-theme-2.active.focus, .open > .btn-theme-2.dropdown-toggle:hover, .open > .btn-theme-2.dropdown-toggle:focus, .open > .btn-theme-2.dropdown-toggle.focus {
  border-color: #339cba;
  background-color: #339cba;
  color: white;
}
.btn-theme-2:active, .btn-theme-2.active, .open > .btn-theme-2.dropdown-toggle {
  background-image: none;
}
.btn-theme-2.disabled:hover, .btn-theme-2.disabled:focus, .btn-theme-2.disabled.focus, .btn-theme-2[disabled]:hover, .btn-theme-2[disabled]:focus, .btn-theme-2[disabled].focus, fieldset[disabled] .btn-theme-2:hover, fieldset[disabled] .btn-theme-2:focus, fieldset[disabled] .btn-theme-2.focus {
  border-color: #3db8db;
  background-color: #3db8db;
}
.btn-theme-2 .badge {
  background-color: white;
  color: #3db8db;
}

.btn-primary {
  color: white;
  background-color: #4285F4;
  border-color: #4285F4;
}
.btn-primary:focus, .btn-primary.focus {
  border-color: #3871cf;
  background-color: #3871cf;
  color: white;
}
.btn-primary:hover {
  border-color: #3871cf;
  background-color: #3871cf;
  color: white;
}
.btn-primary:active, .btn-primary.active, .open > .btn-primary.dropdown-toggle {
  border-color: #3871cf;
  background-color: #3871cf;
  color: white;
}
.btn-primary:active:hover, .btn-primary:active:focus, .btn-primary:active.focus, .btn-primary.active:hover, .btn-primary.active:focus, .btn-primary.active.focus, .open > .btn-primary.dropdown-toggle:hover, .open > .btn-primary.dropdown-toggle:focus, .open > .btn-primary.dropdown-toggle.focus {
  border-color: #3871cf;
  background-color: #3871cf;
  color: white;
}
.btn-primary:active, .btn-primary.active, .open > .btn-primary.dropdown-toggle {
  background-image: none;
}
.btn-primary.disabled:hover, .btn-primary.disabled:focus, .btn-primary.disabled.focus, .btn-primary[disabled]:hover, .btn-primary[disabled]:focus, .btn-primary[disabled].focus, fieldset[disabled] .btn-primary:hover, fieldset[disabled] .btn-primary:focus, fieldset[disabled] .btn-primary.focus {
  border-color: #4285F4;
  background-color: #4285F4;
}
.btn-primary .badge {
  background-color: white;
  color: #4285F4;
}

.btn-secondary {
  color: white;
  background-color: #58cc65;
  border-color: #58cc65;
}
.btn-secondary:focus, .btn-secondary.focus {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-secondary:hover {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-secondary:active, .btn-secondary.active, .open > .btn-secondary.dropdown-toggle {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-secondary:active:hover, .btn-secondary:active:focus, .btn-secondary:active.focus, .btn-secondary.active:hover, .btn-secondary.active:focus, .btn-secondary.active.focus, .open > .btn-secondary.dropdown-toggle:hover, .open > .btn-secondary.dropdown-toggle:focus, .open > .btn-secondary.dropdown-toggle.focus {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-secondary:active, .btn-secondary.active, .open > .btn-secondary.dropdown-toggle {
  background-image: none;
}
.btn-secondary.disabled:hover, .btn-secondary.disabled:focus, .btn-secondary.disabled.focus, .btn-secondary[disabled]:hover, .btn-secondary[disabled]:focus, .btn-secondary[disabled].focus, fieldset[disabled] .btn-secondary:hover, fieldset[disabled] .btn-secondary:focus, fieldset[disabled] .btn-secondary.focus {
  border-color: #58cc65;
  background-color: #58cc65;
}
.btn-secondary .badge {
  background-color: white;
  color: #58cc65;
}

.btn-accent {
  color: white;
  background-color: #817AF0;
  border-color: #817AF0;
}
.btn-accent:focus, .btn-accent.focus {
  border-color: #6d67cc;
  background-color: #6d67cc;
  color: white;
}
.btn-accent:hover {
  border-color: #6d67cc;
  background-color: #6d67cc;
  color: white;
}
.btn-accent:active, .btn-accent.active, .open > .btn-accent.dropdown-toggle {
  border-color: #6d67cc;
  background-color: #6d67cc;
  color: white;
}
.btn-accent:active:hover, .btn-accent:active:focus, .btn-accent:active.focus, .btn-accent.active:hover, .btn-accent.active:focus, .btn-accent.active.focus, .open > .btn-accent.dropdown-toggle:hover, .open > .btn-accent.dropdown-toggle:focus, .open > .btn-accent.dropdown-toggle.focus {
  border-color: #6d67cc;
  background-color: #6d67cc;
  color: white;
}
.btn-accent:active, .btn-accent.active, .open > .btn-accent.dropdown-toggle {
  background-image: none;
}
.btn-accent.disabled:hover, .btn-accent.disabled:focus, .btn-accent.disabled.focus, .btn-accent[disabled]:hover, .btn-accent[disabled]:focus, .btn-accent[disabled].focus, fieldset[disabled] .btn-accent:hover, fieldset[disabled] .btn-accent:focus, fieldset[disabled] .btn-accent.focus {
  border-color: #817AF0;
  background-color: #817AF0;
}
.btn-accent .badge {
  background-color: white;
  color: #817AF0;
}

.btn-info {
  color: white;
  background-color: #2196F3;
  border-color: #2196F3;
}
.btn-info:focus, .btn-info.focus {
  border-color: #1c7fce;
  background-color: #1c7fce;
  color: white;
}
.btn-info:hover {
  border-color: #1c7fce;
  background-color: #1c7fce;
  color: white;
}
.btn-info:active, .btn-info.active, .open > .btn-info.dropdown-toggle {
  border-color: #1c7fce;
  background-color: #1c7fce;
  color: white;
}
.btn-info:active:hover, .btn-info:active:focus, .btn-info:active.focus, .btn-info.active:hover, .btn-info.active:focus, .btn-info.active.focus, .open > .btn-info.dropdown-toggle:hover, .open > .btn-info.dropdown-toggle:focus, .open > .btn-info.dropdown-toggle.focus {
  border-color: #1c7fce;
  background-color: #1c7fce;
  color: white;
}
.btn-info:active, .btn-info.active, .open > .btn-info.dropdown-toggle {
  background-image: none;
}
.btn-info.disabled:hover, .btn-info.disabled:focus, .btn-info.disabled.focus, .btn-info[disabled]:hover, .btn-info[disabled]:focus, .btn-info[disabled].focus, fieldset[disabled] .btn-info:hover, fieldset[disabled] .btn-info:focus, fieldset[disabled] .btn-info.focus {
  border-color: #2196F3;
  background-color: #2196F3;
}
.btn-info .badge {
  background-color: white;
  color: #2196F3;
}

.btn-success {
  color: white;
  background-color: #58cc65;
  border-color: #58cc65;
}
.btn-success:focus, .btn-success.focus {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-success:hover {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-success:active, .btn-success.active, .open > .btn-success.dropdown-toggle {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-success:active:hover, .btn-success:active:focus, .btn-success:active.focus, .btn-success.active:hover, .btn-success.active:focus, .btn-success.active.focus, .open > .btn-success.dropdown-toggle:hover, .open > .btn-success.dropdown-toggle:focus, .open > .btn-success.dropdown-toggle.focus {
  border-color: #4aad55;
  background-color: #4aad55;
  color: white;
}
.btn-success:active, .btn-success.active, .open > .btn-success.dropdown-toggle {
  background-image: none;
}
.btn-success.disabled:hover, .btn-success.disabled:focus, .btn-success.disabled.focus, .btn-success[disabled]:hover, .btn-success[disabled]:focus, .btn-success[disabled].focus, fieldset[disabled] .btn-success:hover, fieldset[disabled] .btn-success:focus, fieldset[disabled] .btn-success.focus {
  border-color: #58cc65;
  background-color: #58cc65;
}
.btn-success .badge {
  background-color: white;
  color: #58cc65;
}

.btn-warning {
  color: white;
  background-color: #FBB03B;
  border-color: #FBB03B;
}
.btn-warning:focus, .btn-warning.focus {
  border-color: #d59532;
  background-color: #d59532;
  color: white;
}
.btn-warning:hover {
  border-color: #d59532;
  background-color: #d59532;
  color: white;
}
.btn-warning:active, .btn-warning.active, .open > .btn-warning.dropdown-toggle {
  border-color: #d59532;
  background-color: #d59532;
  color: white;
}
.btn-warning:active:hover, .btn-warning:active:focus, .btn-warning:active.focus, .btn-warning.active:hover, .btn-warning.active:focus, .btn-warning.active.focus, .open > .btn-warning.dropdown-toggle:hover, .open > .btn-warning.dropdown-toggle:focus, .open > .btn-warning.dropdown-toggle.focus {
  border-color: #d59532;
  background-color: #d59532;
  color: white;
}
.btn-warning:active, .btn-warning.active, .open > .btn-warning.dropdown-toggle {
  background-image: none;
}
.btn-warning.disabled:hover, .btn-warning.disabled:focus, .btn-warning.disabled.focus, .btn-warning[disabled]:hover, .btn-warning[disabled]:focus, .btn-warning[disabled].focus, fieldset[disabled] .btn-warning:hover, fieldset[disabled] .btn-warning:focus, fieldset[disabled] .btn-warning.focus {
  border-color: #FBB03B;
  background-color: #FBB03B;
}
.btn-warning .badge {
  background-color: white;
  color: #FBB03B;
}

.btn-danger {
  color: white;
  background-color: #F44336;
  border-color: #F44336;
}
.btn-danger:focus, .btn-danger.focus {
  border-color: #cf382d;
  background-color: #cf382d;
  color: white;
}
.btn-danger:hover {
  border-color: #cf382d;
  background-color: #cf382d;
  color: white;
}
.btn-danger:active, .btn-danger.active, .open > .btn-danger.dropdown-toggle {
  border-color: #cf382d;
  background-color: #cf382d;
  color: white;
}
.btn-danger:active:hover, .btn-danger:active:focus, .btn-danger:active.focus, .btn-danger.active:hover, .btn-danger.active:focus, .btn-danger.active.focus, .open > .btn-danger.dropdown-toggle:hover, .open > .btn-danger.dropdown-toggle:focus, .open > .btn-danger.dropdown-toggle.focus {
  border-color: #cf382d;
  background-color: #cf382d;
  color: white;
}
.btn-danger:active, .btn-danger.active, .open > .btn-danger.dropdown-toggle {
  background-image: none;
}
.btn-danger.disabled:hover, .btn-danger.disabled:focus, .btn-danger.disabled.focus, .btn-danger[disabled]:hover, .btn-danger[disabled]:focus, .btn-danger[disabled].focus, fieldset[disabled] .btn-danger:hover, fieldset[disabled] .btn-danger:focus, fieldset[disabled] .btn-danger.focus {
  border-color: #F44336;
  background-color: #F44336;
}
.btn-danger .badge {
  background-color: white;
  color: #F44336;
}

.btn {
  line-height: 1.5rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  padding: 0.4375rem 1rem;
  font-size: 0.875rem;
}

.btn-sm {
  line-height: 1.5rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  padding: 0.1875rem 1.5em;
  font-size: 0.8125rem;
}

.btn-lg {
  line-height: 1.5rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  padding: 0.9375rem 1.5em;
  font-size: 1rem;
}

.btn-block + .btn-block {
  margin-top: 0.25rem;
}

.btn-pill {
  -webkit-border-radius: 10rem;
          border-radius: 10rem;
}
.btn-pill {
  padding-right: 2.5em;
  padding-left: 2.5em;
}

.btn.pill {
  padding-right: 2.5em;
  padding-left: 2.5em;
}

.btn > .icon {
  margin-left: 0.5rem;
}

/**
 * form
 * ---------------------------------------------------------
 */
label {
  margin-bottom: 0.25rem;
}

input[type="radio"],
input[type="checkbox"] {
  margin-top: 0.25rem;
  margin-top: 1px \9;
}

input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: dotted thin;
  outline: -webkit-focus-ring-color auto 5px;
  outline-offset: -2px;
}

.form-control {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
  -webkit-transition-property: none;
       -o-transition-property: none;
          transition-property: none;
  height: 2.5rem;
  padding: 0.4375rem 0.75rem;
  font-size: 0.875rem;
  line-height: 1.714285714285714;
  background-color: #f8f9fb;
  color: #212121;
  border-width: 0.0625rem;
  border-color: rgba(0, 0, 0, 0.12);
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.form-control:focus {
  outline: 0;
  -webkit-box-shadow: none;
          box-shadow: none;
  border-color: rgba(0, 0, 0, 0.12);
  background-color: #f5f5f5;
}
.form-control::-webkit-input-placeholder {
  color: #ccc;
}
.form-control::-moz-placeholder {
  color: #ccc;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #ccc;
}
.form-control[disabled], .form-control[readonly], fieldset[disabled] .form-control {
  background-color: #f8f9fb;
  opacity: 0.65;
}
.form-control[disabled], fieldset[disabled] .form-control {
  cursor: default;
}

.form-group {
  margin-bottom: 1rem;
}

.input-lg, .input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 3.5rem;
  padding: 0.875rem 0.75rem;
  font-size: 1rem;
  line-height: 1.625rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}

select.input-lg, .input-group-lg > select.form-control,
.input-group-lg > select.input-group-addon,
.input-group-lg > .input-group-btn > select.btn {
  height: 3.5rem;
  line-height: 3.5rem;
}

textarea.input-lg, .input-group-lg > textarea.form-control,
.input-group-lg > textarea.input-group-addon,
.input-group-lg > .input-group-btn > textarea.btn,
select[multiple].input-lg,
.input-group-lg > select[multiple].form-control,
.input-group-lg > select[multiple].input-group-addon,
.input-group-lg > .input-group-btn > select[multiple].btn {
  height: auto;
}

.form-group-lg .form-control {
  height: 3.5rem;
  padding: 0.875rem 0.75rem;
  font-size: 1rem;
  line-height: 1.625rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.form-group-lg select.form-control {
  height: 3.5rem;
  line-height: 3.5rem;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 3.5rem;
  min-height: 2.625rem;
  padding: 1.875rem 0.75rem;
  font-size: 1rem;
  line-height: 1.625rem;
}

.has-feedback .form-control {
  padding-right: 2.5rem;
}

.form-control-feedback {
  width: 2.5rem;
  height: 2.5rem;
  line-height: 2.857142857142857;
}

.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline, .has-success.radio label, .has-success.checkbox label, .has-success.radio-inline label, .has-success.checkbox-inline label {
  color: #4aad55;
}
.has-success .form-control {
  border-color: #58cc65;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-success .form-control:focus {
  border-color: #58cc65;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-success .input-group-addon {
  color: #4aad55;
  border-color: #58cc65;
  background-color: #eef9ef;
}
.has-success .form-control-feedback {
  color: #4aad55;
}

.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline, .has-warning.radio label, .has-warning.checkbox label, .has-warning.radio-inline label, .has-warning.checkbox-inline label {
  color: #d59532;
}
.has-warning .form-control {
  border-color: #FBB03B;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-warning .form-control:focus {
  border-color: #FBB03B;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-warning .input-group-addon {
  color: #d59532;
  border-color: #FBB03B;
  background-color: #fef7eb;
}
.has-warning .form-control-feedback {
  color: #d59532;
}

.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline, .has-error.radio label, .has-error.checkbox label, .has-error.radio-inline label, .has-error.checkbox-inline label {
  color: #cf382d;
}
.has-error .form-control {
  border-color: #F44336;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-error .form-control:focus {
  border-color: #F44336;
  -webkit-box-shadow: none;
          box-shadow: none;
}
.has-error .input-group-addon {
  color: #cf382d;
  border-color: #F44336;
  background-color: #fdecea;
}
.has-error .form-control-feedback {
  color: #cf382d;
}

.has-feedback label ~ .form-control-feedback {
  top: 1.75rem;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}

.help-block {
  margin-top: 0.25rem;
  margin-bottom: 0.5rem;
  color: inherit;
  font-size: 0.8125rem;
  line-height: 1.538461538461539;
}

.form-lite .form-control {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
  -webkit-transition-property: background-size;
       -o-transition-property: background-size;
          transition-property: background-size;
  background-image: -webkit-gradient(linear, left top, left bottom, from(#8a65c5), to(#8a65c5)), -webkit-gradient(linear, left top, left bottom, from(rgba(0, 0, 0, 0.12)), to(rgba(0, 0, 0, 0.12)));
  background-image: -webkit-linear-gradient(#8a65c5, #8a65c5), -webkit-linear-gradient(rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.12));
  background-image: -o-linear-gradient(#8a65c5, #8a65c5), -o-linear-gradient(rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.12));
  background-image: linear-gradient(#8a65c5, #8a65c5), linear-gradient(rgba(0, 0, 0, 0.12), rgba(0, 0, 0, 0.12));
  background-color: transparent;
  background-repeat: no-repeat;
  background-position: center bottom, center -webkit-calc(100% - 0.0625rem);
  background-position: center bottom, center calc(100% - 0.0625rem);
  background-size: 0 0.125rem, 100% 0.0625rem;
  border-color: transparent;
  -webkit-border-radius: 0;
          border-radius: 0;
  padding-right: 0;
  padding-left: 0;
}
.form-lite .form-control:focus {
  background-size: 100% 0.125rem, 100% 0.0625rem;
  background-color: transparent;
}
.no-cssgradients .form-lite .form-control {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}
.no-cssgradients .form-lite .form-control:focus {
  border-bottom-color: #8a65c5;
}

.form-icon-success,
.form-icon-error {
  font-family: 'themify';
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  letter-spacing: 0;
  margin-right: 0.25rem;
  font-weight: 700;
}

.form-icon-success {
  color: #58cc65;
}
.form-icon-success:before {
  content: "\e64c";
}

.form-icon-error {
  color: #F44336;
}
.form-icon-error:before {
  content: "\e646";
}

.error label {
  color: #F44336;
}

/**
 * input-group
 * ---------------------------------------------------------
 */
.input-group-addon {
  padding: 0.4375rem 0.75rem;
  font-size: 0.875rem;
  font-weight: normal;
  line-height: 1;
  color: #212121;
  text-align: center;
  background-color: #f5f5f5;
  border-width: 0.0625rem;
  border-color: rgba(0, 0, 0, 0.12);
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.input-group-addon.input-sm,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .input-group-addon.btn {
  padding: 0.1875rem 0.75rem;
  font-size: 0.8125rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.input-group-addon.input-lg,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .input-group-addon.btn {
  padding: 0.875rem 0.75rem;
  font-size: 1rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}

.input-group-btn > .btn + .btn {
  margin-left: -0.0625rem;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -0.0625rem;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  margin-left: -0.0625rem;
}

/**
 * list
 * ---------------------------------------------------------
 */
.list-group {
  margin-bottom: 1.5rem;
}

.list-group-item {
  margin-bottom: -0.0625rem;
  border: 0.0625rem solid rgba(0, 0, 0, 0.12);
  padding: 0.6875rem 1.5rem;
  background-color: #fff;
}
.list-group-item:first-child {
  -webkit-border-top-right-radius: 0.125rem;
          border-top-right-radius: 0.125rem;
  -webkit-border-top-left-radius: 0.125rem;
          border-top-left-radius: 0.125rem;
}
.list-group-item:last-child {
  margin-bottom: 0;
  -webkit-border-bottom-right-radius: 0.125rem;
          border-bottom-right-radius: 0.125rem;
  -webkit-border-bottom-left-radius: 0.125rem;
          border-bottom-left-radius: 0.125rem;
}

.list-group.list-group-flat > .list-group-item {
  border-color: transparent;
}

/**
 * badge
 * ---------------------------------------------------------
 */
.list-group-item > .badge {
  margin-top: 0.1875rem;
}

/**
 * iconbox
 * ---------------------------------------------------------
 */
.iconbox {
  text-align: center;
}

.iconbox-media:first-child:not(:last-child) {
  margin-bottom: 1.25rem;
}

.iconbox-media-icon {
  font-size: 2.75rem;
}

.iconbox-media-img {
  display: block;
  max-width: 100%;
  height: auto;
  width: 3.75rem;
  height: 3.75rem;
  margin-right: auto;
  margin-left: auto;
}

.iconbox-header {
  margin-bottom: 0.75rem;
}

.iconbox-header-title {
  font-weight: 500;
}

.iconbox-content {
  /* hold */
}

/**
 * panel
 * ---------------------------------------------------------
 */
.panel {
  margin-bottom: 1.5rem;
  -webkit-box-shadow: none;
          box-shadow: none;
  border-width: 0.0625rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  background-color: #fff;
}

.panel-body {
  padding: 1rem 1.5rem;
}

.panel-heading {
  -webkit-border-top-right-radius: 0.125rem;
          border-top-right-radius: 0.125rem;
  -webkit-border-top-left-radius: 0.125rem;
          border-top-left-radius: 0.125rem;
  padding: 1rem 1.5rem;
  border-bottom-width: 0.0625rem;
}

.panel-title {
  line-height: 1.714285714285714;
  font-size: 0.875rem;
}

.panel-footer {
  -webkit-border-bottom-right-radius: 0.125rem;
          border-bottom-right-radius: 0.125rem;
  -webkit-border-bottom-left-radius: 0.125rem;
          border-bottom-left-radius: 0.125rem;
  padding: 1rem 1.5rem;
  background-color: #f5f5f5;
  border-top-width: 0.0625rem;
  border-top-color: rgba(0, 0, 0, 0.12);
}

.panel-default {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-default > .panel-heading {
  color: #212121;
  background-color: #f5f5f5;
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #212121;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-white {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-white > .panel-heading {
  color: #212121;
  background-color: #fff;
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-white > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-white > .panel-heading .badge {
  color: #fff;
  background-color: #212121;
}
.panel-white > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-dark {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-dark > .panel-heading {
  color: white;
  background-color: #1a1a1a;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-dark > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-dark > .panel-heading .badge {
  color: #1a1a1a;
  background-color: white;
}
.panel-dark > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-darker {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-darker > .panel-heading {
  color: white;
  background-color: #0a0a0a;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-darker > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-darker > .panel-heading .badge {
  color: #0a0a0a;
  background-color: white;
}
.panel-darker > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-theme-1 {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-theme-1 > .panel-heading {
  color: white;
  background-color: #8a65c5;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-theme-1 > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-theme-1 > .panel-heading .badge {
  color: #8a65c5;
  background-color: white;
}
.panel-theme-1 > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-theme-2 {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-theme-2 > .panel-heading {
  color: white;
  background-color: #3db8db;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-theme-2 > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-theme-2 > .panel-heading .badge {
  color: #3db8db;
  background-color: white;
}
.panel-theme-2 > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-primary {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-primary > .panel-heading {
  color: white;
  background-color: #4285F4;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-primary > .panel-heading .badge {
  color: #4285F4;
  background-color: white;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-secondary {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-secondary > .panel-heading {
  color: white;
  background-color: #58cc65;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-secondary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-secondary > .panel-heading .badge {
  color: #58cc65;
  background-color: white;
}
.panel-secondary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-accent {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-accent > .panel-heading {
  color: white;
  background-color: #817AF0;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-accent > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-accent > .panel-heading .badge {
  color: #817AF0;
  background-color: white;
}
.panel-accent > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-info {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-info > .panel-heading {
  color: white;
  background-color: #2196F3;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-info > .panel-heading .badge {
  color: #2196F3;
  background-color: white;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-success {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-success > .panel-heading {
  color: white;
  background-color: #58cc65;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-success > .panel-heading .badge {
  color: #58cc65;
  background-color: white;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-warning {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-warning > .panel-heading {
  color: white;
  background-color: #FBB03B;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-warning > .panel-heading .badge {
  color: #FBB03B;
  background-color: white;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

.panel-danger {
  border-color: rgba(0, 0, 0, 0.12);
}
.panel-danger > .panel-heading {
  color: white;
  background-color: #F44336;
  border-color: rgba(255, 255, 255, 0.12);
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: rgba(0, 0, 0, 0.12);
}
.panel-danger > .panel-heading .badge {
  color: #F44336;
  background-color: white;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: rgba(0, 0, 0, 0.12);
}

/**
 * progress
 * ---------------------------------------------------------
 */
.progress {
  margin-bottom: 1.5rem;
}
.progress:last-child {
  margin-bottom: 0;
}

.progress-sm {
  height: 0.75rem;
}

.progress-xs {
  height: 0.25rem;
}

.progress-text {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: justify;
  -webkit-justify-content: space-between;
     -moz-box-pack: justify;
      -ms-flex-pack: justify;
          justify-content: space-between;
  margin-bottom: 0.25rem;
  text-transform: uppercase;
}

.progress-percent {
  color: #757575;
}

.progress-bar-primary {
  background-color: #4285F4;
}

.progress-bar-accent {
  background-color: #817AF0;
}

.progress-bar-info {
  background-color: #2196F3;
}

.progress-bar-success {
  background-color: #58cc65;
}

.progress-bar-warning {
  background-color: #FBB03B;
}

.progress-bar-danger {
  background-color: #F44336;
}

/**
 * navbar
 * ---------------------------------------------------------
 */
.navbar-btn[data-mfp-src="#popupForm"] {
  margin-left: 15px;
  margin-right: 15px;
}

.navbar {
  position: relative;
  min-height: 5.5rem;
  margin-bottom: 1.5rem;
  border: 0.0625rem solid transparent;
}
.navbar:before, .navbar:after {
  content: "";
  display: table;
}
.navbar:after {
  clear: both;
}
@media (min-width: 992px) {
  .navbar {
    -webkit-border-radius: 0.125rem;
            border-radius: 0.125rem;
  }
}

.navbar-header {
  float: none;
}
.navbar-header:before, .navbar-header:after {
  content: "";
  display: table;
}
.navbar-header:after {
  clear: both;
}
@media (min-width: 992px) {
  .navbar-header {
    float: left;
  }
}

.navbar-collapse {
  overflow-x: visible;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
  border-top: 0.0625rem solid transparent;
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse:before, .navbar-collapse:after {
  content: "";
  display: table;
}
.navbar-collapse:after {
  clear: both;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 768px) {
  .navbar-collapse {
    width: inherit;
  }
  .navbar-collapse.collapse {
    display: none !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    display: inherit !important;
    overflow-y: auto !important;
  }
  .navbar-fixed-top .navbar-collapse, .navbar-static-top .navbar-collapse, .navbar-fixed-bottom .navbar-collapse {
    padding-right: 0.9375rem;
    padding-left: 0.9375rem;
  }
}
@media (min-width: 992px) {
  .navbar-collapse {
    width: auto;
    -webkit-box-shadow: none;
            box-shadow: none;
    border-top: 0;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse, .navbar-static-top .navbar-collapse, .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}

.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 21.25rem;
}
@media (max-device-width: 480px) and (orientation: landscape) {
  .panel-theme-2 {
    background-color: rgba(255,255,255,0.9);
    border-color: rgba(0, 0, 0, 0.12);
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 12.5rem;
  }
}

.container > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-header,
.container-fluid > .navbar-collapse {
  margin-right: -0.9375rem;
  margin-left: -0.9375rem;
}
@media (min-width: 992px) {
  .container > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-header,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}

.navbar-fixed-top {
  z-index: 1000;
  border: 0;
  -webkit-box-shadow: inset 0 -1px 0 0 rgba(0, 0, 0, 0.12);
          box-shadow: inset 0 -1px 0 0 rgba(0, 0, 0, 0.12);
}

.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 992px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    -webkit-border-radius: 0;
            border-radius: 0;
  }
}

.navbar-fixed-top {
  top: 0;
  border-width: 0 0 0.0625rem;
}

.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 0.0625rem 0 0;
}

.navbar-brand {
  float: left;
  height: 5.5rem;
  line-height: 1.5rem;
  padding: 2rem 0.9375rem;
  font-size: 1.125rem;
}
.navbar-brand:hover, .navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
  transform: scale(2);
}
@media (min-width: 992px) {
  .navbar > .container .navbar-brand, .navbar > .container-fluid .navbar-brand {
    margin-left: -0.9375rem;
  }
}

.navbar-brand-media-dark,
.navbar-brand-media-light {
  display: none;
}

.navbar-toggle {
  margin-top: 1.6875rem;
  margin-bottom: 1.6875rem;
  position: relative;
  float: right;
  margin-right: 0.9375rem;
  padding: 0.5625rem 0.625rem;
  background-color: transparent;
  background-image: none;
  border: 0.0625rem solid transparent;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 1rem;
  height: 0.125rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 0.25rem;
}
@media (min-width: 992px) {
  .navbar-toggle {
    display: none;
  }
}

.navbar-nav {
  margin: 0.5rem -0.9375rem;
}
.navbar-nav > li > a {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
  line-height: 1.5rem;
}
@media (max-width: 991px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    -webkit-box-shadow: none;
            box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 0.3125rem 0.9375rem 0.3125rem 1.5625rem;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 1.5rem;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover, .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 768px) {
  .navbar-nav {
    float: none !important;
  }
  .navbar-nav > li {
    float: none;
  }
}
@media (min-width: 992px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 2rem;
    padding-bottom: 2rem;
  }
}

.navbar-form {
  margin-left: -0.9375rem;
  margin-right: -0.9375rem;
  padding: 0.625rem 0.9375rem;
  border-top: 0.0625rem solid transparent;
  border-bottom: 0.0625rem solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}
@media (max-width: 991px) {
  .navbar-form .form-group {
    margin-bottom: 0.3125rem;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 992px) {
  .navbar-form {
    width: auto;
    -webkit-box-shadow: none;
            box-shadow: none;
    margin-left: 0;
    margin-right: 0;
    border: 0;
    padding-top: 0;
    padding-bottom: 0;
  }
}

.navbar-nav > li > .dropdown-menu {
  -webkit-border-top-right-radius: 0;
          border-top-right-radius: 0;
  -webkit-border-top-left-radius: 0;
          border-top-left-radius: 0;
  margin-top: 0;
}

.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  -webkit-border-top-right-radius: 0.125rem;
          border-top-right-radius: 0.125rem;
  -webkit-border-top-left-radius: 0.125rem;
          border-top-left-radius: 0.125rem;
  -webkit-border-bottom-right-radius: 0;
          border-bottom-right-radius: 0;
  -webkit-border-bottom-left-radius: 0;
          border-bottom-left-radius: 0;
  margin-bottom: 0;
}

.navbar-btn {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}
.navbar-btn.btn-lg {
  margin-top: 1rem;
  margin-bottom: 1rem;
}
.navbar-btn.btn-sm {
  margin-top: 1.75rem;
  margin-bottom: 1.75rem;
}
.navbar-btn.btn-xs {
  margin-top: 2.0625rem;
  margin-bottom: 2.0625rem;
}

.navbar-text {
  margin-top: 2rem;
  margin-bottom: 2rem;
}
@media (min-width: 992px) {
  .navbar-text {
    float: left;
    margin-left: 0.9375rem;
    margin-right: 0.9375rem;
  }
}

@media (min-width: 768px) {
  .navbar-right ~ .navbar-right {
    margin-right: inherit;
  }
}
@media (min-width: 992px) {
  .navbar-left {
    float: left !important;
  }

  .navbar-right {
    float: right !important;
    margin-right: -0.9375rem;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0;
  }
}
.navbar-default {
  background-color: #fff;
  border-color: rgba(0, 0, 0, 0.12);
}
@media (max-width: 991px) {
  .navbar-default .navbar-brand-media-light {
    display: none;
  }
}
.navbar-default .navbar-brand-media-light {
  display: none;
}
.navbar-default .navbar-brand {
  color: #212121;
}
.navbar-default .navbar-brand:hover, .navbar-default .navbar-brand:focus {
  color: #212121;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #757575;
}
.navbar-default .navbar-nav > li > a {
  color: #757575;
}
.navbar-default .navbar-nav > li > a:hover, .navbar-default .navbar-nav > li > a:focus {
  color: #212121;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a, .navbar-default .navbar-nav > .active > a:hover, .navbar-default .navbar-nav > .active > a:focus {
  color: black;
  background-color: #b6e2a6;
}
.navbar-default .navbar-nav > .disabled > a, .navbar-default .navbar-nav > .disabled > a:hover, .navbar-default .navbar-nav > .disabled > a:focus {
  color: #9e9e9e;
  background-color: #fff;
}
.navbar-default .navbar-toggle {
  border-color: rgba(0, 0, 0, 0.12);
}
.navbar-default .navbar-toggle:hover, .navbar-default .navbar-toggle:focus {
  background-color: #fff;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #1a1a1a;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: rgba(0, 0, 0, 0.12);
}
.navbar-default .navbar-nav > .open > a, .navbar-default .navbar-nav > .open > a:hover, .navbar-default .navbar-nav > .open > a:focus {
  background-color: #8a65c5;
  color: white;
}
@media (max-width: 991px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #757575;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover, .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #212121;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a, .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover, .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: white;
    background-color: #8a65c5;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a, .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover, .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #9e9e9e;
    background-color: #fff;
  }
}
.navbar-default .navbar-link {
  color: #757575;
}
.navbar-default .navbar-link:hover {
  color: #212121;
}
.navbar-default .btn-link,
.navbar-default .navbar-icon {
  color: #757575;
}
.navbar-default .btn-link:hover, .navbar-default .btn-link:focus,
.navbar-default .navbar-icon:hover,
.navbar-default .navbar-icon:focus {
  color: #212121;
}
.navbar-default .btn-link[disabled]:hover, .navbar-default .btn-link[disabled]:focus, fieldset[disabled] .navbar-default .btn-link:hover, fieldset[disabled] .navbar-default .btn-link:focus,
.navbar-default .navbar-icon[disabled]:hover,
.navbar-default .navbar-icon[disabled]:focus, fieldset[disabled]
.navbar-default .navbar-icon:hover, fieldset[disabled]
.navbar-default .navbar-icon:focus {
  color: #9e9e9e;
}
.navbar-default .navbar-toggle-icon {
  background-color: transparent;
  border-color: rgba(0, 0, 0, 0.12);
}
.navbar-default .navbar-toggle-icon:hover, .navbar-default .navbar-toggle-icon:focus {
  background-color: transparent;
}
.navbar-default .navbar-toggle-icon > .icon {
  color: #212121;
}

@media (max-width: 991px) {
  .navbar-inverse .navbar-brand-media-dark {
    display: none;
  }
}
.navbar-inverse .navbar-brand-media-dark {
  display: none;
}
.is-scrolled .navbar-inverse .navbar-brand-media-dark {
  display: none;
}
.is-scrolled .navbar-inverse .navbar-brand-media-light {
  display: block;
}
.navbar-inverse .navbar-toggle-icon {
  background-color: transparent;
  border-color: rgba(255, 255, 255, 0.12);
}
.navbar-inverse .navbar-toggle-icon:hover, .navbar-inverse .navbar-toggle-icon:focus {
  background-color: transparent;
}
.navbar-inverse .navbar-toggle-icon > .icon {
  color: white;
}

@media (min-width: 992px) {
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg {
    background-color: transparent;
    border-color: transparent;
    -webkit-box-shadow: none;
            box-shadow: none;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-brand-media-dark {
    display: none;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-brand-media-light {
    display: block;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-brand {
    color: white;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-brand:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-brand:focus {
    color: white;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-text {
    color: rgba(255, 255, 255, 0.7);
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > li > a {
    color: rgba(255, 255, 255, 0.7);
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > li > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > li > a:focus {
    color: white;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .active > a, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .active > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .active > a:focus {
    color: white;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .disabled > a, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .disabled > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .disabled > a:focus {
    color: rgba(255, 255, 255, 0.5);
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .open > a, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .open > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-nav > .open > a:focus {
    background-color: inherit;
    color: white;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-link {
    color: rgba(255, 255, 255, 0.7);
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-link:hover {
    color: white;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link,
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon {
    color: rgba(255, 255, 255, 0.7);
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link:focus,
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon:hover,
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon:focus {
    color: white;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link[disabled]:hover, html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link[disabled]:focus, fieldset[disabled] html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link:hover, fieldset[disabled] html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .btn-link:focus,
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon[disabled]:hover,
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon[disabled]:focus, fieldset[disabled]
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon:hover, fieldset[disabled]
  html:not(.is-scrolled) .navbar.site-navbar-from-light-fg .navbar-icon:focus {
    color: rgba(255, 255, 255, 0.5);
  }
}

@media (min-width: 992px) {
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg {
    background-color: grey;
    border-color: transparent;
    -webkit-box-shadow: none;
            box-shadow: none;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-brand-media-light {
    display: none;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-brand-media-dark {
    display: block;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-brand {
    color: #212121;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-brand:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-brand:focus {
    color: #212121;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-text {
    color: #757575;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > li > a {
    color: #757575;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > li > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > li > a:focus {
    color: #212121;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .active > a, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .active > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .active > a:focus {
    color: #212121;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .disabled > a, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .disabled > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .disabled > a:focus {
    color: #9e9e9e;
    background-color: inherit;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .open > a, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .open > a:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-nav > .open > a:focus {
    background-color: inherit;
    color: #212121;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-link {
    color: #757575;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .navbar-link:hover {
    color: #212121;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link {
    color: #757575;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link:focus {
    color: #212121;
  }
  html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link[disabled]:hover, html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link[disabled]:focus, fieldset[disabled] html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link:hover, fieldset[disabled] html:not(.is-scrolled) .navbar.site-navbar-from-dark-fg .btn-link:focus {
    color: #9e9e9e;
  }
  .is-scrolled .navbar.site-navbar-from-dark-fg.navbar-default .navbar-brand-media-dark {
    display: block;
  }
  .is-scrolled .navbar.site-navbar-from-dark-fg.navbar-default .navbar-brand-media-light {
    display: none;
  }
  .is-scrolled .navbar.site-navbar-from-dark-fg.navbar-inverse .navbar-brand-media-dark {
    display: none;
  }
  .is-scrolled .navbar.site-navbar-from-dark-fg.navbar-inverse .navbar-brand-media-light {
    display: block;
  }
}

.navbar-brand {
  padding-top: 1.625rem;
  padding-bottom: 1.625rem;
}
.navbar-brand > img {
  height: 2.25rem;
}

.navbar-nav > li > a {
  font-weight: 500;
}

@media (max-width: 991px) {
  .navbar-btn {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .navbar-btn + .navbar-nav, .navbar-nav + .navbar-btn {
    margin-top: 0;
  }
}

@media (min-width: 992px) {
  .navbar-btn-right {
    float: right;
  }
  .navbar-btn-right:not(:last-child) {
    margin-left: 1.875rem;
  }
  .navbar-right + .navbar-btn-right {
    margin-right: 1.875rem;
  }
}

.navbar-toggle-icon {
  margin-top: 1.625rem;
  margin-bottom: 1.625rem;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
     -moz-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
     -moz-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  width: 2.25rem;
  height: 2.25rem;
  border-width: 0.0625rem;
  -webkit-border-radius: 0.125rem;
          border-radius: 0.125rem;
  padding: 0;
}
.navbar-toggle-icon > .icon {
  font-size: 0.875rem;
}
@media (min-width: 992px) {
  .navbar-toggle-icon {
    display: none;
  }
}

@media (max-width: 991px) {
  .navbar {
    min-height: 4rem;
  }

  .navbar-brand {
    height: 4rem;
    padding-top: 1.125rem;
    padding-bottom: 1.125rem;
  }
  .navbar-brand > img {
    height: 1.75rem;
  }

  .navbar-toggle-icon {
    margin-top: 0.875rem;
    margin-bottom: 0.875rem;
  }
}
.navbar-icon {
  margin-top: 2.3125rem;
  margin-bottom: 2.3125rem;
  display: block;
  font-weight: 700;
  letter-spacing: 0;
  font-family: 'themify';
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
@media (max-width: 991px) {
  .navbar-icon {
    margin-top: 1.1875rem;
    margin-bottom: 1.1875rem;
    float: right;
    width: 2.25rem;
    text-align: center;
  }
}

.audio-toggle {
  overflow: hidden;
}

.audio-toggle > a:before {
  display: inline-block;
  -webkit-animation-iteration-count: infinite;
       -o-animation-iteration-count: infinite;
          animation-iteration-count: infinite;
  -webkit-animation-name: jello;
       -o-animation-name: jello;
          animation-name: jello;
  visibility: visible;
  font-family: 'themify';
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.audio-playing .audio-toggle > a:before {
  content: "\e689";
}
.audio-paused .audio-toggle > a:before {
  -webkit-animation: none;
       -o-animation: none;
          animation: none;
  content: "\e6ad";
}

@media (min-width: 992px) {
  .navbar-icon-right {
    float: right;
  }
  .navbar-icon-right:not(:last-child) {
    margin-left: 1.875rem;
  }
  .navbar-right + .navbar-icon-right {
    margin-right: 1.875rem;
  }
}

/**
 * font
 */
.font-body, body {
  font-family: Roboto, "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.font-heading, h1, .text-h1,
h2, .text-h2,
h3, .text-h3,
h4, .text-h4,
h5, .text-h5,
h6, .text-h6, .btn {
  font-family: Roboto, "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.font-sub {
  font-family: Georgia, "Times New Roman", Times, serif;
}

.font-mono, code,
kbd,
pre,
samp {
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
}

/**
 * text
 */
.text-d1,
.text-d2,
.text-d3,
.text-d4 {
  font-weight: 300;
  text-transform: inherit;
  letter-spacing: 0.01em;
}

.text-d1 {
  font-size: 2.75rem;
  line-height: 1.318181818181818;
}

.text-d2 {
  font-size: 2.5rem;
  line-height: 1.35;
}

.text-d3 {
  font-size: 2.25rem;
  line-height: 1.333333333333333;
}

.text-d4 {
  font-size: 2rem;
  line-height: 1.375;
}

h1, .text-h1 {
  font-size: 1.75rem;
  line-height: 1.428571428571429;
}

h2, .text-h2 {
  font-size: 1.5rem;
  line-height: 1.416666666666667;
}

h3, .text-h3 {
  font-size: 1.25rem;
  line-height: 1.5;
}

h4, .text-h4 {
  font-size: 1.125rem;
  line-height: 1.555555555555556;
}

h5, .text-h5 {
  font-size: 1rem;
  line-height: 1.625;
}

h6, .text-h6 {
  font-size: 0.875rem;
  line-height: 1.714285714285714;
}

.text-xl {
  font-size: 1.125rem;
  line-height: 1.555555555555556;
}

.text-lead,
.text-lg {
  font-size: 1rem;
  line-height: 1.625;
}

.text-md {
  font-size: 0.875rem;
  line-height: 1.714285714285714;
}

.text-sm {
  font-size: 0.8125rem;
  line-height: 1.846153846153846;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1.833333333333333;
}

.bg-no-repeat {
  background-repeat: no-repeat !important;
}

.bg-center {
  background-position: 50% !important;
}

.bg-cover {
  background-size: cover !important;
}

.bg-fixed {
  background-attachment: fixed !important;
}

/**
 * text color
 */
.color-white {
  color: #fff;
}

.color-black {
  color: #000;
}

.color-default {
  color: #212121;
}

.color-muted {
  color: #9e9e9e;
}

.color-theme-1 {
  color: #8a65c5;
}

.color-theme-2 {
  color: #3db8db;
}

.color-primary {
  color: #4285F4;
}

.color-accent {
  color: #817AF0;
}

.color-info {
  color: #2196F3;
}

.color-success {
  color: #58cc65;
}

.color-warning {
  color: #FBB03B;
}

.color-danger {
  color: #F44336;
}

/**
 * background color
 */
.bg-white {
  background-color: #fff !important;
  color: #212121 !important;
}

.bg-light {
  background-color: #f8f9fb !important;
  color: #212121 !important;
}

.bg-light-blue {
  background-color: #f7fbfe !important;
  color: #212121 !important;
}

.bg-dark {
  background-color: #1a1a1a !important;
  color: white !important;
}

.bg-black {
  background-color: #000 !important;
  color: white !important;
}

.bg-theme-1 {
  background-image: url('../img/tap-banner.jpg')  !important;
  background-position: center;
  background-size: cover;
  color: white !important;
}

.bg-theme-status {
  background-image: url('../img/tap-banner.jpg')  !important;
  background-position: center;
  background-size: cover;
  color: white !important;
}

.bg-theme-2 {
  background-color: #3db8db !important;
  color: white !important;
}

.bg-primary {
  background-color: #4285F4 !important;
  color: white !important;
}

.bg-accent {
  background-color: #817AF0 !important;
  color: white !important;
}

.bg-success {
  background-color: #58cc65 !important;
  color: white !important;
}

.bg-info {
  background-color: #2196F3 !important;
  color: white !important;
}

.bg-warning {
  background-color: #FBB03B !important;
  color: white !important;
}

.bg-danger {
  background-color: #F44336 !important;
  color: white !important;
}

.bg-gradient {
  background: -webkit-radial-gradient(bottom, ellipse, #1b2735 0%, #090a0f) !important;
  background: -o-radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f) !important;
  background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f) !important;
  color: white !important;
}

/**
 * align
 */
.align-top, .align-all-top > * {
  vertical-align: top;
}

.align-middle, .align-all-middle > * {
  vertical-align: middle;
}

.align-bottom, .align-all-bottom > * {
  vertical-align: bottom;
}

.align-baseline, .align-all-baseline > * {
  vertical-align: baseline;
}

.align-left, .align-all-left > * {
  text-align: left;
}

.align-center, .align-all-center > * {
  text-align: center;
}

.align-right, .align-all-right > * {
  text-align: right;
}

.align-outer {
  display: table;
  width: 100%;
}

.align-inner {
  display: table-cell;
}

/**
 * background image
 */
[data-bg-img],
[data-bg-img-mobile],
[data-bg-img-desktop] {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

/**
 * box-shadow
 */
.box-shadow-custom, .home-form-col .panel, #screenshotCarousel .bfc-carousel-item-media-img, .pricing-section .pricing-table, .popup-subscribe-form, .contact-left-col .panel {
  -webkit-transition: all 0.2s ease-in-out;
       -o-transition: all 0.2s ease-in-out;
          transition: all 0.2s ease-in-out;
  -webkit-box-shadow: 0 8px 48px 0 rgba(0, 0, 0, 0.08);
          box-shadow: 0 8px 48px 0 rgba(0, 0, 0, 0.08);
}
.box-shadow-custom:hover, .home-form-col .panel:hover, #screenshotCarousel .bfc-carousel-item-media-img:hover, .pricing-section .pricing-table:hover, .popup-subscribe-form:hover, .contact-left-col .panel:hover, .box-shadow-custom:focus, .home-form-col .panel:focus, #screenshotCarousel .bfc-carousel-item-media-img:focus, .pricing-section .pricing-table:focus, .popup-subscribe-form:focus, .contact-left-col .panel:focus {
  -webkit-box-shadow: 0 8px 48px 0 rgba(0, 0, 0, 0.16);
          box-shadow: 0 8px 48px 0 rgba(0, 0, 0, 0.16);
}

.flexible-widgets h1.widget-title {
  font-weight: 400;
  text-transform: capitalize;
  letter-spacing: -0.02em;
  font-size: 30px;
  line-height: 1.4;
}

.flexible-widgets h2.widget-title {
  font-weight: 500;
  text-transform: capitalize;
  letter-spacing: inherit;
  font-size: 24px;
  line-height: 1.41667;
}

File: /assets\css\vendor.css
﻿@charset "UTF-8";

/*!
 * animate.css -http://daneden.me/animate
 * Version - 3.5.1
 * Licensed under the MIT license - http://opensource.org/licenses/MIT
 *
 * Copyright (c) 2016 Daniel Eden
 */

/*
 * themify icon
 */

@font-face{font-family:'themify';src:url('../fonts/themify.eot');src:url('../fonts/themify-1.eot') format('embedded-opentype'), url('../fonts/themify.txt') format('woff'), url('../fonts/themify-1.txt') format('truetype'), url('../fonts/themify.svg') format('svg');font-weight:normal;font-style:normal}[class^="ti-"],[class*=" ti-"]{font-family:'themify';speak:none;font-style:normal;font-weight:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.ti-wand:before{content:"\e600"}.ti-volume:before{content:"\e601"}.ti-user:before{content:"\e602"}.ti-unlock:before{content:"\e603"}.ti-unlink:before{content:"\e604"}.ti-trash:before{content:"\e605"}.ti-thought:before{content:"\e606"}.ti-target:before{content:"\e607"}.ti-tag:before{content:"\e608"}.ti-tablet:before{content:"\e609"}.ti-star:before{content:"\e60a"}.ti-spray:before{content:"\e60b"}.ti-signal:before{content:"\e60c"}.ti-shopping-cart:before{content:"\e60d"}.ti-shopping-cart-full:before{content:"\e60e"}.ti-settings:before{content:"\e60f"}.ti-search:before{content:"\e610"}.ti-zoom-in:before{content:"\e611"}.ti-zoom-out:before{content:"\e612"}.ti-cut:before{content:"\e613"}.ti-ruler:before{content:"\e614"}.ti-ruler-pencil:before{content:"\e615"}.ti-ruler-alt:before{content:"\e616"}.ti-bookmark:before{content:"\e617"}.ti-bookmark-alt:before{content:"\e618"}.ti-reload:before{content:"\e619"}.ti-plus:before{content:"\e61a"}.ti-pin:before{content:"\e61b"}.ti-pencil:before{content:"\e61c"}.ti-pencil-alt:before{content:"\e61d"}.ti-paint-roller:before{content:"\e61e"}.ti-paint-bucket:before{content:"\e61f"}.ti-na:before{content:"\e620"}.ti-mobile:before{content:"\e621"}.ti-minus:before{content:"\e622"}.ti-medall:before{content:"\e623"}.ti-medall-alt:before{content:"\e624"}.ti-marker:before{content:"\e625"}.ti-marker-alt:before{content:"\e626"}.ti-arrow-up:before{content:"\e627"}.ti-arrow-right:before{content:"\e628"}.ti-arrow-left:before{content:"\e629"}.ti-arrow-down:before{content:"\e62a"}.ti-lock:before{content:"\e62b"}.ti-location-arrow:before{content:"\e62c"}.ti-link:before{content:"\e62d"}.ti-layout:before{content:"\e62e"}.ti-layers:before{content:"\e62f"}.ti-layers-alt:before{content:"\e630"}.ti-key:before{content:"\e631"}.ti-import:before{content:"\e632"}.ti-image:before{content:"\e633"}.ti-heart:before{content:"\e634"}.ti-heart-broken:before{content:"\e635"}.ti-hand-stop:before{content:"\e636"}.ti-hand-open:before{content:"\e637"}.ti-hand-drag:before{content:"\e638"}.ti-folder:before{content:"\e639"}.ti-flag:before{content:"\e63a"}.ti-flag-alt:before{content:"\e63b"}.ti-flag-alt-2:before{content:"\e63c"}.ti-eye:before{content:"\e63d"}.ti-export:before{content:"\e63e"}.ti-exchange-vertical:before{content:"\e63f"}.ti-desktop:before{content:"\e640"}.ti-cup:before{content:"\e641"}.ti-crown:before{content:"\e642"}.ti-comments:before{content:"\e643"}.ti-comment:before{content:"\e644"}.ti-comment-alt:before{content:"\e645"}.ti-close:before{content:"\e646"}.ti-clip:before{content:"\e647"}.ti-angle-up:before{content:"\e648"}.ti-angle-right:before{content:"\e649"}.ti-angle-left:before{content:"\e64a"}.ti-angle-down:before{content:"\e64b"}.ti-check:before{content:"\e64c"}.ti-check-box:before{content:"\e64d"}.ti-camera:before{content:"\e64e"}.ti-announcement:before{content:"\e64f"}.ti-brush:before{content:"\e650"}.ti-briefcase:before{content:"\e651"}.ti-bolt:before{content:"\e652"}.ti-bolt-alt:before{content:"\e653"}.ti-blackboard:before{content:"\e654"}.ti-bag:before{content:"\e655"}.ti-move:before{content:"\e656"}.ti-arrows-vertical:before{content:"\e657"}.ti-arrows-horizontal:before{content:"\e658"}.ti-fullscreen:before{content:"\e659"}.ti-arrow-top-right:before{content:"\e65a"}.ti-arrow-top-left:before{content:"\e65b"}.ti-arrow-circle-up:before{content:"\e65c"}.ti-arrow-circle-right:before{content:"\e65d"}.ti-arrow-circle-left:before{content:"\e65e"}.ti-arrow-circle-down:before{content:"\e65f"}.ti-angle-double-up:before{content:"\e660"}.ti-angle-double-right:before{content:"\e661"}.ti-angle-double-left:before{content:"\e662"}.ti-angle-double-down:before{content:"\e663"}.ti-zip:before{content:"\e664"}.ti-world:before{content:"\e665"}.ti-wheelchair:before{content:"\e666"}.ti-view-list:before{content:"\e667"}.ti-view-list-alt:before{content:"\e668"}.ti-view-grid:before{content:"\e669"}.ti-uppercase:before{content:"\e66a"}.ti-upload:before{content:"\e66b"}.ti-underline:before{content:"\e66c"}.ti-truck:before{content:"\e66d"}.ti-timer:before{content:"\e66e"}.ti-ticket:before{content:"\e66f"}.ti-thumb-up:before{content:"\e670"}.ti-thumb-down:before{content:"\e671"}.ti-text:before{content:"\e672"}.ti-stats-up:before{content:"\e673"}.ti-stats-down:before{content:"\e674"}.ti-split-v:before{content:"\e675"}.ti-split-h:before{content:"\e676"}.ti-smallcap:before{content:"\e677"}.ti-shine:before{content:"\e678"}.ti-shift-right:before{content:"\e679"}.ti-shift-left:before{content:"\e67a"}.ti-shield:before{content:"\e67b"}.ti-notepad:before{content:"\e67c"}.ti-server:before{content:"\e67d"}.ti-quote-right:before{content:"\e67e"}.ti-quote-left:before{content:"\e67f"}.ti-pulse:before{content:"\e680"}.ti-printer:before{content:"\e681"}.ti-power-off:before{content:"\e682"}.ti-plug:before{content:"\e683"}.ti-pie-chart:before{content:"\e684"}.ti-paragraph:before{content:"\e685"}.ti-panel:before{content:"\e686"}.ti-package:before{content:"\e687"}.ti-music:before{content:"\e688"}.ti-music-alt:before{content:"\e689"}.ti-mouse:before{content:"\e68a"}.ti-mouse-alt:before{content:"\e68b"}.ti-money:before{content:"\e68c"}.ti-microphone:before{content:"\e68d"}.ti-menu:before{content:"\e68e"}.ti-menu-alt:before{content:"\e68f"}.ti-map:before{content:"\e690"}.ti-map-alt:before{content:"\e691"}.ti-loop:before{content:"\e692"}.ti-location-pin:before{content:"\e693"}.ti-list:before{content:"\e694"}.ti-light-bulb:before{content:"\e695"}.ti-Italic:before{content:"\e696"}.ti-info:before{content:"\e697"}.ti-infinite:before{content:"\e698"}.ti-id-badge:before{content:"\e699"}.ti-hummer:before{content:"\e69a"}.ti-home:before{content:"\e69b"}.ti-help:before{content:"\e69c"}.ti-headphone:before{content:"\e69d"}.ti-harddrives:before{content:"\e69e"}.ti-harddrive:before{content:"\e69f"}.ti-gift:before{content:"\e6a0"}.ti-game:before{content:"\e6a1"}.ti-filter:before{content:"\e6a2"}.ti-files:before{content:"\e6a3"}.ti-file:before{content:"\e6a4"}.ti-eraser:before{content:"\e6a5"}.ti-envelope:before{content:"\e6a6"}.ti-download:before{content:"\e6a7"}.ti-direction:before{content:"\e6a8"}.ti-direction-alt:before{content:"\e6a9"}.ti-dashboard:before{content:"\e6aa"}.ti-control-stop:before{content:"\e6ab"}.ti-control-shuffle:before{content:"\e6ac"}.ti-control-play:before{content:"\e6ad"}.ti-control-pause:before{content:"\e6ae"}.ti-control-forward:before{content:"\e6af"}.ti-control-backward:before{content:"\e6b0"}.ti-cloud:before{content:"\e6b1"}.ti-cloud-up:before{content:"\e6b2"}.ti-cloud-down:before{content:"\e6b3"}.ti-clipboard:before{content:"\e6b4"}.ti-car:before{content:"\e6b5"}.ti-calendar:before{content:"\e6b6"}.ti-book:before{content:"\e6b7"}.ti-bell:before{content:"\e6b8"}.ti-basketball:before{content:"\e6b9"}.ti-bar-chart:before{content:"\e6ba"}.ti-bar-chart-alt:before{content:"\e6bb"}.ti-back-right:before{content:"\e6bc"}.ti-back-left:before{content:"\e6bd"}.ti-arrows-corner:before{content:"\e6be"}.ti-archive:before{content:"\e6bf"}.ti-anchor:before{content:"\e6c0"}.ti-align-right:before{content:"\e6c1"}.ti-align-left:before{content:"\e6c2"}.ti-align-justify:before{content:"\e6c3"}.ti-align-center:before{content:"\e6c4"}.ti-alert:before{content:"\e6c5"}.ti-alarm-clock:before{content:"\e6c6"}.ti-agenda:before{content:"\e6c7"}.ti-write:before{content:"\e6c8"}.ti-window:before{content:"\e6c9"}.ti-widgetized:before{content:"\e6ca"}.ti-widget:before{content:"\e6cb"}.ti-widget-alt:before{content:"\e6cc"}.ti-wallet:before{content:"\e6cd"}.ti-video-clapper:before{content:"\e6ce"}.ti-video-camera:before{content:"\e6cf"}.ti-vector:before{content:"\e6d0"}.ti-themify-logo:before{content:"\e6d1"}.ti-themify-favicon:before{content:"\e6d2"}.ti-themify-favicon-alt:before{content:"\e6d3"}.ti-support:before{content:"\e6d4"}.ti-stamp:before{content:"\e6d5"}.ti-split-v-alt:before{content:"\e6d6"}.ti-slice:before{content:"\e6d7"}.ti-shortcode:before{content:"\e6d8"}.ti-shift-right-alt:before{content:"\e6d9"}.ti-shift-left-alt:before{content:"\e6da"}.ti-ruler-alt-2:before{content:"\e6db"}.ti-receipt:before{content:"\e6dc"}.ti-pin2:before{content:"\e6dd"}.ti-pin-alt:before{content:"\e6de"}.ti-pencil-alt2:before{content:"\e6df"}.ti-palette:before{content:"\e6e0"}.ti-more:before{content:"\e6e1"}.ti-more-alt:before{content:"\e6e2"}.ti-microphone-alt:before{content:"\e6e3"}.ti-magnet:before{content:"\e6e4"}.ti-line-double:before{content:"\e6e5"}.ti-line-dotted:before{content:"\e6e6"}.ti-line-dashed:before{content:"\e6e7"}.ti-layout-width-full:before{content:"\e6e8"}.ti-layout-width-default:before{content:"\e6e9"}.ti-layout-width-default-alt:before{content:"\e6ea"}.ti-layout-tab:before{content:"\e6eb"}.ti-layout-tab-window:before{content:"\e6ec"}.ti-layout-tab-v:before{content:"\e6ed"}.ti-layout-tab-min:before{content:"\e6ee"}.ti-layout-slider:before{content:"\e6ef"}.ti-layout-slider-alt:before{content:"\e6f0"}.ti-layout-sidebar-right:before{content:"\e6f1"}.ti-layout-sidebar-none:before{content:"\e6f2"}.ti-layout-sidebar-left:before{content:"\e6f3"}.ti-layout-placeholder:before{content:"\e6f4"}.ti-layout-menu:before{content:"\e6f5"}.ti-layout-menu-v:before{content:"\e6f6"}.ti-layout-menu-separated:before{content:"\e6f7"}.ti-layout-menu-full:before{content:"\e6f8"}.ti-layout-media-right-alt:before{content:"\e6f9"}.ti-layout-media-right:before{content:"\e6fa"}.ti-layout-media-overlay:before{content:"\e6fb"}.ti-layout-media-overlay-alt:before{content:"\e6fc"}.ti-layout-media-overlay-alt-2:before{content:"\e6fd"}.ti-layout-media-left-alt:before{content:"\e6fe"}.ti-layout-media-left:before{content:"\e6ff"}.ti-layout-media-center-alt:before{content:"\e700"}.ti-layout-media-center:before{content:"\e701"}.ti-layout-list-thumb:before{content:"\e702"}.ti-layout-list-thumb-alt:before{content:"\e703"}.ti-layout-list-post:before{content:"\e704"}.ti-layout-list-large-image:before{content:"\e705"}.ti-layout-line-solid:before{content:"\e706"}.ti-layout-grid4:before{content:"\e707"}.ti-layout-grid3:before{content:"\e708"}.ti-layout-grid2:before{content:"\e709"}.ti-layout-grid2-thumb:before{content:"\e70a"}.ti-layout-cta-right:before{content:"\e70b"}.ti-layout-cta-left:before{content:"\e70c"}.ti-layout-cta-center:before{content:"\e70d"}.ti-layout-cta-btn-right:before{content:"\e70e"}.ti-layout-cta-btn-left:before{content:"\e70f"}.ti-layout-column4:before{content:"\e710"}.ti-layout-column3:before{content:"\e711"}.ti-layout-column2:before{content:"\e712"}.ti-layout-accordion-separated:before{content:"\e713"}.ti-layout-accordion-merged:before{content:"\e714"}.ti-layout-accordion-list:before{content:"\e715"}.ti-ink-pen:before{content:"\e716"}.ti-info-alt:before{content:"\e717"}.ti-help-alt:before{content:"\e718"}.ti-headphone-alt:before{content:"\e719"}.ti-hand-point-up:before{content:"\e71a"}.ti-hand-point-right:before{content:"\e71b"}.ti-hand-point-left:before{content:"\e71c"}.ti-hand-point-down:before{content:"\e71d"}.ti-gallery:before{content:"\e71e"}.ti-face-smile:before{content:"\e71f"}.ti-face-sad:before{content:"\e720"}.ti-credit-card:before{content:"\e721"}.ti-control-skip-forward:before{content:"\e722"}.ti-control-skip-backward:before{content:"\e723"}.ti-control-record:before{content:"\e724"}.ti-control-eject:before{content:"\e725"}.ti-comments-smiley:before{content:"\e726"}.ti-brush-alt:before{content:"\e727"}.ti-youtube:before{content:"\e728"}.ti-vimeo:before{content:"\e729"}.ti-twitter:before{content:"\e72a"}.ti-time:before{content:"\e72b"}.ti-tumblr:before{content:"\e72c"}.ti-skype:before{content:"\e72d"}.ti-share:before{content:"\e72e"}.ti-share-alt:before{content:"\e72f"}.ti-rocket:before{content:"\e730"}.ti-pinterest:before{content:"\e731"}.ti-new-window:before{content:"\e732"}.ti-microsoft:before{content:"\e733"}.ti-list-ol:before{content:"\e734"}.ti-linkedin:before{content:"\e735"}.ti-layout-sidebar-2:before{content:"\e736"}.ti-layout-grid4-alt:before{content:"\e737"}.ti-layout-grid3-alt:before{content:"\e738"}.ti-layout-grid2-alt:before{content:"\e739"}.ti-layout-column4-alt:before{content:"\e73a"}.ti-layout-column3-alt:before{content:"\e73b"}.ti-layout-column2-alt:before{content:"\e73c"}.ti-instagram:before{content:"\e73d"}.ti-google:before{content:"\e73e"}.ti-github:before{content:"\e73f"}.ti-flickr:before{content:"\e740"}.ti-instagram:before{content:"\e73d"}.ti-dropbox:before{content:"\e742"}.ti-dribbble:before{content:"\e743"}.ti-apple:before{content:"\e744"}.ti-android:before{content:"\e745"}.ti-save:before{content:"\e746"}.ti-save-alt:before{content:"\e747"}.ti-yahoo:before{content:"\e748"}.ti-wordpress:before{content:"\e749"}.ti-vimeo-alt:before{content:"\e74a"}.ti-twitter-alt:before{content:"\e74b"}.ti-tumblr-alt:before{content:"\e74c"}.ti-trello:before{content:"\e74d"}.ti-stack-overflow:before{content:"\e74e"}.ti-soundcloud:before{content:"\e74f"}.ti-sharethis:before{content:"\e750"}.ti-sharethis-alt:before{content:"\e751"}.ti-reddit:before{content:"\e752"}.ti-pinterest-alt:before{content:"\e753"}.ti-microsoft-alt:before{content:"\e754"}.ti-linux:before{content:"\e755"}.ti-jsfiddle:before{content:"\e756"}.ti-joomla:before{content:"\e757"}.ti-html5:before{content:"\e758"}.ti-flickr-alt:before{content:"\e759"}.ti-email:before{content:"\e75a"}.ti-drupal:before{content:"\e75b"}.ti-dropbox-alt:before{content:"\e75c"}.ti-css3:before{content:"\e75d"}.ti-rss:before{content:"\e75e"}.ti-rss-alt:before{content:"\e75f";}


/* ytplayer */
@charset"UTF-8";.mb_YTPBar,.mb_YTPBar span.mb_YTPUrl a{color:#fff}@font-face{font-family:ytpregular;src:url(font/ytp-regular.eot)}@font-face{font-family:ytpregular;src:url(data:application/x-font-woff;charset=utf-8;base64,d09GRgABAAAAAA5sABEAAAAAFCAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAABgAAAABwAAAAcZ9iuNUdERUYAAAGcAAAAHQAAACAAdAAET1MvMgAAAbwAAABJAAAAYHUMUrFjbWFwAAACCAAAAKkAAAGKn5XycWN2dCAAAAK0AAAANgAAADYNLQohZnBnbQAAAuwAAAGxAAACZVO0L6dnYXNwAAAEoAAAAAgAAAAIAAAAEGdseWYAAASoAAAGVQAAB4jz86dSaGVhZAAACwAAAAAzAAAANgbKONpoaGVhAAALNAAAACAAAAAkESQLXGhtdHgAAAtUAAAAVAAAARxOmwVwbG9jYQAAC6gAAAAjAAAAkFoEXRRtYXhwAAALzAAAACAAAAAgAWoB625hbWUAAAvsAAAA+wAAAeok3Eb+cG9zdAAADOgAAADAAAABN99tv1lwcmVwAAANqAAAALkAAAFY3I6ikndlYmYAAA5kAAAABgAAAAbHMlGnAAAAAQAAAADMPaLPAAAAAM3Nk7QAAAAAzc13sXjaY2BkYGDgA2IJBhBgYmAEQjcgZgHzGAAHTAB5AAAAeNpjYGbZwDiBgZWBhdWY5SwDA8MsCM10liGNKQ3IB0rBASMDEgj1DvdjcGDgfcDAlvYPqJJVldEZpoZVkuUZkFJgYAQAUUULewAAAHjaY2BgYGaAYBkGRgYQaAHyGMF8FoYMIC3GIAAUYQOyeBkUGKIYqhgWKHAp6CvEP2D4/x+sAyTuyJAIFGeAizP+//r/8f/D//f+n/HA8oHo/WcKblDzsQBGoOkwSUYmIMGErgDiRLyAhZWNnYOTi5uHl49fQFBIWERUTFxCUkpaRhYiLyevoKikrKKqpq6hqaWto6unb2BoZGxiambOQF1gQZYuAIQnH4IAAAAAAAAAAAABegEnAHEAswC9AOAA5QD+ARcBIwBdAHIBtgBcAGAAZgByAI8AogErAbIAUwBEBREAAHjaXVG7TltBEN0NDwOBxNggOdoUs5mQxnuhBQnE1Y1iZDuF5QhpN3KRi3EBH0CBRA3arxmgoaRImwYhF0h8Qj4hEjNriKI0Ozuzc86ZM0vKkap36WvPU+ckkMLdBs02/U5ItbMA96Tr642MtIMHWmxm9Mp1+/4LBpvRlDtqAOU9bykPGU07gVq0p/7R/AqG+/wf8zsYtDTT9NQ6CekhBOabcUuD7xnNussP+oLV4WIwMKSYpuIuP6ZS/rc052rLsLWR0byDMxH5yTRAU2ttBJr+1CHV83EUS5DLprE2mJiy/iQTwYXJdFVTtcz42sFdsrPoYIMqzYEH2MNWeQweDg8mFNK3JMosDRH2YqvECBGTHAo55dzJ/qRA+UgSxrxJSjvjhrUGxpHXwKA2T7P/PJtNbW8dwvhZHMF3vxlLOvjIhtoYEWI7YimACURCRlX5hhrPvSwG5FL7z0CUgOXxj3+dCLTu2EQ8l7V1DjFWCHp+29zyy4q7VrnOi0J3b6pqqNIpzftezr7HA54eC8NBY8Gbz/v+SoH6PCyuNGgOBEN6N3r/orXqiKu8Fz6yJ9O/sVoAAAAAAQAB//8AD3jaTZVrbBxXFcfvufNe72Nmdx77tmfHO2N76117784OTr154YAbR7RQuUQhttoSuXZKFQVKKYqgiFJAgkpIkVClIn8opSomjXY3VHHTFldEIYpay1hR+ID4Bha27FoIEQGpd8Idu4lY7c6eOfee//2f3+zeizAaQwif4iYRgwRUbgGqjLYFNvVxtcVzfxltM5iGqMUEaS5ItwU+vTPahiBPFFMpmoo5hnv8XnjFn+Um7/xmjF1GCLHoPf+fgsUVEYcSKIcGkYbaWYxKLZ3bgGa50qpACQ0NeyYoYILaDTqpurUK2FZBUYlJY8ukEc0egLpbo+kY8O/BQcx2dvwP2Fh6/Q+Gl19fyroubHmer7rpjHllPZ/NKB+tp2/4/TzxSx0zo/74uUY29vJZOEHIfng4lzz7cjyXzn/jJwqCwCOLdj2iPSP3F/hUAHF3v+Cviee5DIqhJDLRACLoPGpHECq1M7Sd5iDZ/W6zQW8mu9Ecql7SI6xYaiOpnxCydwPNWqWJ/tSSjY1mqtqU5ZYNpWal2pJiGy0XSi1bVuKX1Fyh1GuMoJYeUeJvy/GEVbTpfTOjHJRVzUim0tlcwekbKD1QrgR5M97OV8nIyMjQsKPUEKWGNEVFFBwqEs/yHMEVFMM1PIc4FhiWQVxHcxjD0zzXEkgbmHe5G1eA9T955453xd+B9tbpi6vj10+fvj6+evH0Fju7vPDU5szVY8euzmw+tXABv7kEov/v33WOv+v/C8LG9M2xD19/EquzCyuHVuY6R25Obz35+odw4NDKwuzWHAK86q9x21wKYYQkjFeZ3M5f/TUmw6Qo12P+38Wf0zEZpVABlVANfQu1owHXXMD1AdIyQhvNgeou2b1LAuhAkVwyExRps/ppAE230qrTX1MrEVXil5W4qlm9thMAMpR2MtVHAbXMnBJvZ8oVGjdZ5XK6u6cwNExqdNJ9dnm4D+8eIeYeM7hH0b3H9bcQuczdeH75ef+TxTveO/5tuDK2Mrs5d+HmzQtzm7MrbP6ZqxMrrz2+vf34aysTV5+5iN9YhMi51W93Tiz5/wFp+ujy/MntGXx+dfrjqflrO788Ob989MaMP716+Nr8FOpCjbvnw032BUrm82gKfQc10SJaAwwZGINHEUrksaEndI3XCppBavWaU7Nrda/u7QfPsnmBF1ReK4NjCxbkgVRJdW/MdmiyjHkhCgKvGkrNq+uGngPLUDXVioJTcGxONWguENOIYmkq1lQqaDu2q1AqKi6qRh6CN0uqhlkn1WIwt1Z3FTqH6lt2kWLkqZpQ2F1H4D3X1CzFUkCp1R8EVaeKGr3mgXpyd3OKZTcgioMi3qImqA2FaFSYrkHd7BYESnSMdqAx1HNgg/6pG0Bo95RAGehqoNAuaRHR90wGdXyJtkAJ1DxSDVQCfS8ocui+EohqagNjFroniyLAOYbBgvSQxuXxiUSCGQXReJBnjafhbf6xBs8P9ZclLLJdTJfdL3bLRsgd50Nf52P7JIWjInYqFuZhUGErucF0Qj/zNJtPGArDz7EYFi0chvSpw8C/mJRgRVLfgrEf7RvowhyjJ3JPfPlX/h8N/6fZryX7bh/pJsPj4QLX9Ra89NL3QQkljmOqnognU6HcxKkoI/JsaJ8cDcfCqZAMC2cfFeSoHu+WFEmWzIQqx8PVmCThSFqPKqLIsgxJx0QYZt1iocjgfrPbjIoiltkXxzxTlE5FVTL1zb7YmTOSzXGiEBU0ZgHzXexjd9HklDtTc2P7iR4/Wmqk/jGhfZXjZW1bYFVp3y01G+ocrh/K9VST3+05OUsaEnAYGKZRfWIpDQaXT2Ej2/vCl1S5nNe7jHq5eCAlM7rOpFx8PP1Zf/NzCUdkpXjUhHmdfdi/Xv31D6WccPAIDjNMmPnBzC+ErAipZzPf++LkQyGRhTDEpCNkbmLpz8892zmE3+8swq1YODIqf2Z7lO8RdJHn7RS8kpY6r0qhAg7xXIHnhViu+zBDbhcx16UOfGVgaGkoXe6LhwS+h7NgSa+vR7ESZvPyq6VUqN+SC0ZSTPm3oETGoxGIh/p60w3naIyJ/Gywf9CMnnAemR3524hT5DErxOwBhR55COMw3e+u0T0tOEsR0JMx+NBHftD/AJ+D/f7v/TW+9t+P+Bo9e/7vNYz+By6FsKkAAAB42mNgZGBgYGRwbI8IWhzPb/OVQZ6DAQTOni3fCKP/+/x7yrOBNRTI5WBgAokCAG3mDbAAeNpjYGRgYFX9t5eBgeftf5//WTwbGIAiKMAdAJycBph42mN6w+DCwcDAAMIsZ8D0HhBNLIap52D478fBwHQRyvbBpZ7nLYMtKeZjt5OJhxT1TKsYGFhDETTjcSAG0gyPoRgozigIpL0hNEiOBcgFAEBoNC142mNgYNCBwjoccALDBEY9RhsgPIMMmZcRhHtIhkcA9pQspAAAAQAAAEcBVAALAAAAAAACAAEAAgAWAAABAACTAAAAAHjalZCxTgJBFEXPApJoYYgF9VZUSIAFTdDCnmiIgsTKsASQuGiCu0YaCr4OfomKOzsTCHRmMzPn3blz38sCFyzJ4uXOgbKWZY+8KssZLqk7zkp9cJyjSOT4jD9WjvPSt46vKHoFx2txyfGGqnfPO18kyohSGjBjJPqRFmqPmWolWkZ9o0uHZ/EkfTNgTo0KVX017ujRps+TyDqvT7xW9U/UV1Vz9ZryrQn8o8QOL1JsdVA/5IwZpv7f/YsKTW50O1PqpzKNZyw1UnKov2c9dbkD7c1/zdhXFSrNdIz3HbuaJFH1KM9CZyDN3N3SoiFupfP66mbOYAd8k0EGAHjabc05TwJhHITxZ0BBBc/P4IkI7y4sh0dBsosHKiqHeLUiiTE0FH56Xdl/6TS/ZIoZUszzM+ad/3IOSilNmm122GWPfQ4ocEiRI0qUcXj4VKgSUKNOgybHnHDKGSER7Xjjgkuu6HDNDbd0ueOeB3r0GTDkkRFPPPPCK29a0KIyympJy1pRTnmtak3r2tCmtjLjz+/ph5edfU2cc2Fiy/3px4Xpmb5ZMatmYNbMutkwm2Yr0W8nBnOj+OcXVDk0PnjaRc67DoJAEAVQFuT9fqsJCSZ2+w12QkNjrCCx9w+sbSy19DsGK/9Ob3RZujk3k7nzZp8bsbvSkXXoR8Yew9gavN9QNHSUHTFch4oMfuoV0uqGNL4nv25emq3yHzzADwVcwOsFHMCtBWzAWQlYgJ0ImIA1rRmAeRbQAWM6vQD04A9GgXglRBo4Kh+19gJGYDgzBqOnZALGO8kUTLaSGZhWkjmYrSULMA8kS7CYi5ZgKTlQxr/W1F5aAAAAAAFRp8cxAAA=)format('woff'),url(font/ytp-regular.ttf)format('truetype');font-weight:400;font-style:normal}.mb_YTPlayer:focus{outline:0}.mbYTP_wrapper{display:block;transform:translateZ(0)translate3d(0,0,0);transform-style:preserve-3d;perspective:1000;-webkit-backface-visibility:hidden;backface-visibility:hidden;box-sizing:border-box}.mb_YTPlayer .loading{position:absolute;top:10px;right:10px;font-size:12px;color:#fff;background:rgba(0,0,0,.51);text-align:center;padding:2px 4px;border-radius:5px;font-family:"Droid Sans",sans-serif;-webkit-animation:fade .1s infinite alternate;animation:fade .1s infinite alternate}@-webkit-keyframes fade{0%{opacity:.5}100%{opacity:1}}@keyframes fade{0%{opacity:.5}100%{opacity:1}}.YTPFullscreen{display:block!important;position:fixed!important;width:100%!important;height:100%!important;top:0!important;left:0!important;margin:0!important;border:none!important;opacity:1!important;background-color:#000}.mbYTP_wrapper iframe{max-width:4000px!important}.inline_YTPlayer{margin-bottom:20px;vertical-align:top;position:relative;left:0;overflow:hidden;border-radius:4px;box-shadow:0 0 5px rgba(0,0,0,.7);background:rgba(0,0,0,.5)}.inline_YTPlayer img{border:none!important;margin:0!important;padding:0!important;transform:none!important}.mb_YTPBar,.mb_YTPBar .buttonBar{box-sizing:border-box;left:0;padding:5px;width:100%}.mb_YTPBar .ytpicon{font-size:20px;font-family:ytpregular}.mb_YTPBar .mb_YTPUrl.ytpicon{font-size:30px}.mb_YTPBar{transition:opacity .5s;display:block;height:10px;background:#333;position:fixed;bottom:0;text-align:left;z-index:1000;font:14px/16px sans-serif;opacity:.1}.mb_YTPBar.visible,.mb_YTPBar:hover{opacity:1}.mb_YTPBar .buttonBar{transition:all .5s;background:0 0;font:12px/14px Calibri;position:absolute;top:-30px;height:40px}.mb_YTPBar:hover .buttonBar{background:rgba(0,0,0,.4)}.mb_YTPBar span{display:inline-block;font:16px/20px Calibri,sans-serif;position:relative;width:30px;height:25px;vertical-align:middle}.mb_YTPBar span.mb_YTPTime{width:130px}.mb_YTPBar span.mb_OnlyYT,.mb_YTPBar span.mb_YTPUrl{position:absolute;width:auto;display:block;top:6px;right:10px;cursor:pointer}.mb_YTPBar span.mb_YTPUrl img{width:60px}.mb_YTPBar span.mb_OnlyYT{left:300px;right:auto}.mb_YTPBar span.mb_OnlyYT img{width:25px}.mb_YTPBar .mb_YTPMuteUnmute,.mb_YTPBar .mb_YTPPlaypause,.mb_YTPlayer .mb_YTPBar .mb_YTPPlaypause img{cursor:pointer}.mb_YTPBar .mb_YTPProgress{height:10px;width:100%;background:#222;bottom:0;left:0}.mb_YTPBar .mb_YTPLoaded{height:10px;width:0;background:#444;left:0}.mb_YTPBar .mb_YTPseekbar{height:10px;width:0;background:#bb110e;bottom:0;left:0;box-shadow:rgba(82,82,82,.47)1px 1px 3px}.mb_YTPBar .YTPOverlay{backface-visibility:hidden;-webkit-backface-visibility:hidden;-webkit-transform-style:"flat";box-sizing:border-box}.YTPOverlay.raster{background:url(images/raster.png)}.YTPOverlay.raster.retina{background:url(images/raster@2x.png)}.YTPOverlay.raster-dot{background:url(images/raster_dot.png)}.YTPOverlay.raster-dot.retina{background:url(images/raster_dot@2x.png)}.mb_YTPBar .simpleSlider{position:relative;width:100px;height:10px;border:1px solid #fff;overflow:hidden;box-sizing:border-box;margin-right:10px;cursor:pointer!important;border-radius:3px}.mb_YTPBar.compact .simpleSlider{width:40px}.mb_YTPBar .simpleSlider.muted{opacity:.3}.mb_YTPBar .level{position:absolute;left:0;bottom:0;background-color:#fff;box-sizing:border-box}.mb_YTPBar .level.horizontal{height:100%;width:0}.mb_YTPBar .level.vertical{height:auto;width:100%}


/* Slider */
.slick-slider{position:relative;display:block;box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-touch-callout:none;-khtml-user-select:none;-ms-touch-action:pan-y;touch-action:pan-y;-webkit-tap-highlight-color:transparent}.slick-list{position:relative;display:block;overflow:hidden;margin:0;padding:0}.slick-list:focus{outline:none}.slick-list.dragging{cursor:pointer;cursor:hand}.slick-slider .slick-track,.slick-slider .slick-list{-webkit-transform:translate3d(0, 0, 0);-moz-transform:translate3d(0, 0, 0);-ms-transform:translate3d(0, 0, 0);-o-transform:translate3d(0, 0, 0);transform:translate3d(0, 0, 0)}.slick-track{position:relative;top:0;left:0;display:block}.slick-track:before,.slick-track:after{display:table;content:''}.slick-track:after{clear:both}.slick-loading .slick-track{visibility:hidden}.slick-slide{display:none;float:left;height:100%;min-height:1px}[dir='rtl'] .slick-slide{float:right}.slick-slide img{display:block}.slick-slide.slick-loading img{display:none}.slick-slide.dragging img{pointer-events:none}.slick-initialized .slick-slide{display:block}.slick-loading .slick-slide{visibility:hidden}.slick-vertical .slick-slide{display:block;height:auto;border:1px solid transparent}.slick-arrow.slick-hidden{display:none}@charset 'UTF-8';.slick-loading .slick-list{background:#fff url('../img/ajax-loader.gif') center center no-repeat}@font-face{font-family:'slick';font-weight:normal;font-style:normal;src:url('../fonts/slick.eot');src:url('../fonts/slick-1.eot') format('embedded-opentype'), url('../fonts/slick.txt') format('woff'), url('../fonts/slick-1.txt') format('truetype'), url('../fonts/slick.svg') format('svg')}.slick-prev,.slick-next{font-size:0;line-height:0;position:absolute;top:50%;display:block;width:20px;height:20px;padding:0;-webkit-transform:translate(0, -50%);-ms-transform:translate(0, -50%);transform:translate(0, -50%);cursor:pointer;color:transparent;border:none;outline:none;background:transparent}.slick-prev:hover,.slick-prev:focus,.slick-next:hover,.slick-next:focus{color:transparent;outline:none;background:transparent}.slick-prev:hover:before,.slick-prev:focus:before,.slick-next:hover:before,.slick-next:focus:before{opacity:1}.slick-prev.slick-disabled:before,.slick-next.slick-disabled:before{opacity:.25}.slick-prev:before,.slick-next:before{font-family:'slick';font-size:20px;line-height:1;opacity:.75;color:white;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.slick-prev{left:-25px}[dir='rtl'] .slick-prev{right:-25px;left:auto}.slick-prev:before{content:'←'}[dir='rtl'] .slick-prev:before{content:'→'}.slick-next{right:-25px}[dir='rtl'] .slick-next{right:auto;left:-25px}.slick-next:before{content:'→'}[dir='rtl'] .slick-next:before{content:'←'}.slick-dotted.slick-slider{margin-bottom:30px}.slick-dots{position:absolute;bottom:-25px;display:block;width:100%;padding:0;margin:0;list-style:none;text-align:center}.slick-dots li{position:relative;display:inline-block;width:20px;height:20px;margin:0 5px;padding:0;cursor:pointer}.slick-dots li button{font-size:0;line-height:0;display:block;width:20px;height:20px;padding:5px;cursor:pointer;color:transparent;border:0;outline:none;background:transparent}.slick-dots li button:hover,.slick-dots li button:focus{outline:none}.slick-dots li button:hover:before,.slick-dots li button:focus:before{opacity:1}.slick-dots li button:before{font-family:'slick';font-size:6px;line-height:20px;position:absolute;top:0;left:0;width:20px;height:20px;content:'•';text-align:center;opacity:.25;color:black;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.slick-dots li.slick-active button:before{opacity:.75;color:black}

/*
 * vegas
 */

.vegas-overlay,.vegas-slide,.vegas-slide-inner,.vegas-timer,.vegas-wrapper{position:absolute;top:0;left:0;bottom:0;right:0;overflow:hidden;border:none;padding:0;margin:0}.vegas-overlay{opacity:.5;background:url(overlays/02.png) center center}.vegas-timer{top:auto;bottom:0;height:2px}.vegas-timer-progress{width:0;height:100%;background:#fff;-webkit-transition:width ease-out;transition:width ease-out}.vegas-timer-running .vegas-timer-progress{width:100%}.vegas-slide,.vegas-slide-inner{margin:0;padding:0;background:center center no-repeat;-webkit-transform:translateZ(0);transform:translateZ(0)}body .vegas-container{overflow:hidden!important;position:relative}.vegas-video{min-width:100%;min-height:100%;width:auto;height:auto}body.vegas-container{overflow:auto;position:static;z-index:-2}body.vegas-container>.vegas-overlay,body.vegas-container>.vegas-slide,body.vegas-container>.vegas-timer{position:fixed;z-index:-1}:root body.vegas-container>.vegas-overlay,:root body.vegas-container>.vegas-slide,_::full-page-media,_:future{bottom:-76px}.vegas-transition-fade,.vegas-transition-fade2{opacity:0}.vegas-transition-fade-in,.vegas-transition-fade2-in{opacity:1}.vegas-transition-fade2-out{opacity:0}.vegas-transition-blur,.vegas-transition-blur2{opacity:0;-webkit-filter:blur(32px);filter:blur(32px)}.vegas-transition-blur-in,.vegas-transition-blur2-in{opacity:1;-webkit-filter:blur(0);filter:blur(0)}.vegas-transition-blur2-out{opacity:0}.vegas-transition-flash,.vegas-transition-flash2{opacity:0;-webkit-filter:brightness(25);filter:brightness(25)}.vegas-transition-flash-in,.vegas-transition-flash2-in{opacity:1;-webkit-filter:brightness(1);filter:brightness(1)}.vegas-transition-flash2-out{opacity:0;-webkit-filter:brightness(25);filter:brightness(25)}.vegas-transition-negative,.vegas-transition-negative2{opacity:0;-webkit-filter:invert(100%);filter:invert(100%)}.vegas-transition-negative-in,.vegas-transition-negative2-in{opacity:1;-webkit-filter:invert(0);filter:invert(0)}.vegas-transition-negative2-out{opacity:0;-webkit-filter:invert(100%);filter:invert(100%)}.vegas-transition-burn,.vegas-transition-burn2{opacity:0;-webkit-filter:contrast(1000%) saturate(1000%);filter:contrast(1000%) saturate(1000%)}.vegas-transition-burn-in,.vegas-transition-burn2-in{opacity:1;-webkit-filter:contrast(100%) saturate(100%);filter:contrast(100%) saturate(100%)}.vegas-transition-burn2-out{opacity:0;-webkit-filter:contrast(1000%) saturate(1000%);filter:contrast(1000%) saturate(1000%)}.vegas-transition-slideLeft,.vegas-transition-slideLeft2{-webkit-transform:translateX(100%);transform:translateX(100%)}.vegas-transition-slideLeft-in,.vegas-transition-slideLeft2-in{-webkit-transform:translateX(0);transform:translateX(0)}.vegas-transition-slideLeft2-out,.vegas-transition-slideRight,.vegas-transition-slideRight2{-webkit-transform:translateX(-100%);transform:translateX(-100%)}.vegas-transition-slideRight-in,.vegas-transition-slideRight2-in{-webkit-transform:translateX(0);transform:translateX(0)}.vegas-transition-slideRight2-out{-webkit-transform:translateX(100%);transform:translateX(100%)}.vegas-transition-slideUp,.vegas-transition-slideUp2{-webkit-transform:translateY(100%);transform:translateY(100%)}.vegas-transition-slideUp-in,.vegas-transition-slideUp2-in{-webkit-transform:translateY(0);transform:translateY(0)}.vegas-transition-slideDown,.vegas-transition-slideDown2,.vegas-transition-slideUp2-out{-webkit-transform:translateY(-100%);transform:translateY(-100%)}.vegas-transition-slideDown-in,.vegas-transition-slideDown2-in{-webkit-transform:translateY(0);transform:translateY(0)}.vegas-transition-slideDown2-out{-webkit-transform:translateY(100%);transform:translateY(100%)}.vegas-transition-zoomIn,.vegas-transition-zoomIn2{-webkit-transform:scale(0);transform:scale(0);opacity:0}.vegas-transition-zoomIn-in,.vegas-transition-zoomIn2-in{-webkit-transform:scale(1);transform:scale(1);opacity:1}.vegas-transition-zoomIn2-out,.vegas-transition-zoomOut,.vegas-transition-zoomOut2{-webkit-transform:scale(2);transform:scale(2);opacity:0}.vegas-transition-zoomOut-in,.vegas-transition-zoomOut2-in{-webkit-transform:scale(1);transform:scale(1);opacity:1}.vegas-transition-zoomOut2-out{-webkit-transform:scale(0);transform:scale(0);opacity:0}.vegas-transition-swirlLeft,.vegas-transition-swirlLeft2{-webkit-transform:scale(2) rotate(35deg);transform:scale(2) rotate(35deg);opacity:0}.vegas-transition-swirlLeft-in,.vegas-transition-swirlLeft2-in{-webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0);opacity:1}.vegas-transition-swirlLeft2-out,.vegas-transition-swirlRight,.vegas-transition-swirlRight2{-webkit-transform:scale(2) rotate(-35deg);transform:scale(2) rotate(-35deg);opacity:0}.vegas-transition-swirlRight-in,.vegas-transition-swirlRight2-in{-webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0);opacity:1}.vegas-transition-swirlRight2-out{-webkit-transform:scale(2) rotate(35deg);transform:scale(2) rotate(35deg);opacity:0}.vegas-animation-kenburns{-webkit-animation:kenburns ease-out;animation:kenburns ease-out}@-webkit-keyframes kenburns{0%{-webkit-transform:scale(1.5);transform:scale(1.5)}100%{-webkit-transform:scale(1);transform:scale(1)}}@keyframes kenburns{0%{-webkit-transform:scale(1.5);transform:scale(1.5)}100%{-webkit-transform:scale(1);transform:scale(1)}}.vegas-animation-kenburnsUp{-webkit-animation:kenburnsUp ease-out;animation:kenburnsUp ease-out}@-webkit-keyframes kenburnsUp{0%{-webkit-transform:scale(1.5) translate(0,10%);transform:scale(1.5) translate(0,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsUp{0%{-webkit-transform:scale(1.5) translate(0,10%);transform:scale(1.5) translate(0,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsDown{-webkit-animation:kenburnsDown ease-out;animation:kenburnsDown ease-out}@-webkit-keyframes kenburnsDown{0%{-webkit-transform:scale(1.5) translate(0,-10%);transform:scale(1.5) translate(0,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsDown{0%{-webkit-transform:scale(1.5) translate(0,-10%);transform:scale(1.5) translate(0,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsLeft{-webkit-animation:kenburnsLeft ease-out;animation:kenburnsLeft ease-out}@-webkit-keyframes kenburnsLeft{0%{-webkit-transform:scale(1.5) translate(10%,0);transform:scale(1.5) translate(10%,0)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsLeft{0%{-webkit-transform:scale(1.5) translate(10%,0);transform:scale(1.5) translate(10%,0)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsRight{-webkit-animation:kenburnsRight ease-out;animation:kenburnsRight ease-out}@-webkit-keyframes kenburnsRight{0%{-webkit-transform:scale(1.5) translate(-10%,0);transform:scale(1.5) translate(-10%,0)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsRight{0%{-webkit-transform:scale(1.5) translate(-10%,0);transform:scale(1.5) translate(-10%,0)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsUpLeft{-webkit-animation:kenburnsUpLeft ease-out;animation:kenburnsUpLeft ease-out}@-webkit-keyframes kenburnsUpLeft{0%{-webkit-transform:scale(1.5) translate(10%,10%);transform:scale(1.5) translate(10%,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsUpLeft{0%{-webkit-transform:scale(1.5) translate(10%,10%);transform:scale(1.5) translate(10%,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsUpRight{-webkit-animation:kenburnsUpRight ease-out;animation:kenburnsUpRight ease-out}@-webkit-keyframes kenburnsUpRight{0%{-webkit-transform:scale(1.5) translate(-10%,10%);transform:scale(1.5) translate(-10%,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsUpRight{0%{-webkit-transform:scale(1.5) translate(-10%,10%);transform:scale(1.5) translate(-10%,10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsDownLeft{-webkit-animation:kenburnsDownLeft ease-out;animation:kenburnsDownLeft ease-out}@-webkit-keyframes kenburnsDownLeft{0%{-webkit-transform:scale(1.5) translate(10%,-10%);transform:scale(1.5) translate(10%,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsDownLeft{0%{-webkit-transform:scale(1.5) translate(10%,-10%);transform:scale(1.5) translate(10%,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}.vegas-animation-kenburnsDownRight{-webkit-animation:kenburnsDownRight ease-out;animation:kenburnsDownRight ease-out}@-webkit-keyframes kenburnsDownRight{0%{-webkit-transform:scale(1.5) translate(-10%,-10%);transform:scale(1.5) translate(-10%,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}@keyframes kenburnsDownRight{0%{-webkit-transform:scale(1.5) translate(-10%,-10%);transform:scale(1.5) translate(-10%,-10%)}100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)}}

/* Magnific Popup CSS */
.mfp-bg{top:0;left:0;width:100%;height:100%;z-index:1042;overflow:hidden;position:fixed;background:#0b0b0b;opacity:0.8}.mfp-wrap{top:0;left:0;width:100%;height:100%;z-index:1043;position:fixed;outline:none !important;-webkit-backface-visibility:hidden}.mfp-container{text-align:center;position:absolute;width:100%;height:100%;left:0;top:0;padding:0 8px;box-sizing:border-box}.mfp-container:before{content:'';display:inline-block;height:100%;vertical-align:middle}.mfp-align-top .mfp-container:before{display:none}.mfp-content{position:relative;display:inline-block;vertical-align:middle;margin:0 auto;text-align:left;z-index:1045}.mfp-inline-holder .mfp-content,.mfp-ajax-holder .mfp-content{width:100%;cursor:auto}.mfp-ajax-cur{cursor:progress}.mfp-zoom-out-cur,.mfp-zoom-out-cur .mfp-image-holder .mfp-close{cursor:-moz-zoom-out;cursor:-webkit-zoom-out;cursor:zoom-out}.mfp-zoom{cursor:pointer;cursor:-webkit-zoom-in;cursor:-moz-zoom-in;cursor:zoom-in}.mfp-auto-cursor .mfp-content{cursor:auto}.mfp-close,.mfp-arrow,.mfp-preloader,.mfp-counter{-webkit-user-select:none;-moz-user-select:none;user-select:none}.mfp-loading.mfp-figure{display:none}.mfp-hide{display:none !important}.mfp-preloader{color:#CCC;position:absolute;top:50%;width:auto;text-align:center;margin-top:-0.8em;left:8px;right:8px;z-index:1044}.mfp-preloader a{color:#CCC}.mfp-preloader a:hover{color:#FFF}.mfp-s-ready .mfp-preloader{display:none}.mfp-s-error .mfp-content{display:none}button.mfp-close,button.mfp-arrow{overflow:visible;cursor:pointer;background:transparent;border:0;-webkit-appearance:none;display:block;outline:none;padding:0;z-index:1046;box-shadow:none;touch-action:manipulation}button::-moz-focus-inner{padding:0;border:0}.mfp-close{width:44px;height:44px;line-height:44px;position:absolute;right:0;top:0;text-decoration:none;text-align:center;opacity:0.65;padding:0 0 18px 10px;color:#FFF;font-style:normal;font-size:28px;font-family:Arial, Baskerville, monospace}.mfp-close:hover,.mfp-close:focus{opacity:1}.mfp-close:active{top:1px}.mfp-close-btn-in .mfp-close{color:#333}.mfp-image-holder .mfp-close,.mfp-iframe-holder .mfp-close{color:#FFF;right:-6px;text-align:right;padding-right:6px;width:100%}.mfp-counter{position:absolute;top:0;right:0;color:#CCC;font-size:12px;line-height:18px;white-space:nowrap}.mfp-arrow{position:absolute;opacity:0.65;margin:0;top:50%;margin-top:-55px;padding:0;width:90px;height:110px;-webkit-tap-highlight-color:transparent}.mfp-arrow:active{margin-top:-54px}.mfp-arrow:hover,.mfp-arrow:focus{opacity:1}.mfp-arrow:before,.mfp-arrow:after{content:'';display:block;width:0;height:0;position:absolute;left:0;top:0;margin-top:35px;margin-left:35px;border:medium inset transparent}.mfp-arrow:after{border-top-width:13px;border-bottom-width:13px;top:8px}.mfp-arrow:before{border-top-width:21px;border-bottom-width:21px;opacity:0.7}.mfp-arrow-left{left:0}.mfp-arrow-left:after{border-right:17px solid #FFF;margin-left:31px}.mfp-arrow-left:before{margin-left:25px;border-right:27px solid #3F3F3F}.mfp-arrow-right{right:0}.mfp-arrow-right:after{border-left:17px solid #FFF;margin-left:39px}.mfp-arrow-right:before{border-left:27px solid #3F3F3F}.mfp-iframe-holder{padding-top:40px;padding-bottom:40px}.mfp-iframe-holder .mfp-content{line-height:0;width:100%;max-width:900px}.mfp-iframe-holder .mfp-close{top:-40px}.mfp-iframe-scaler{width:100%;height:0;overflow:hidden;padding-top:56.25%}.mfp-iframe-scaler iframe{position:absolute;display:block;top:0;left:0;width:100%;height:100%;box-shadow:0 0 8px rgba(0, 0, 0, 0.6);background:#000}img.mfp-img{width:auto;max-width:100%;height:auto;display:block;line-height:0;box-sizing:border-box;padding:40px 0 40px;margin:0 auto}.mfp-figure{line-height:0}.mfp-figure:after{content:'';position:absolute;left:0;top:40px;bottom:40px;display:block;right:0;width:auto;height:auto;z-index:-1;box-shadow:0 0 8px rgba(0, 0, 0, 0.6);background:#444}.mfp-figure small{color:#BDBDBD;display:block;font-size:12px;line-height:14px}.mfp-figure figure{margin:0}.mfp-bottom-bar{margin-top:-36px;position:absolute;top:100%;left:0;width:100%;cursor:auto}.mfp-title{text-align:left;line-height:18px;color:#F3F3F3;word-wrap:break-word;padding-right:36px}.mfp-image-holder .mfp-content{max-width:100%}.mfp-gallery .mfp-image-holder .mfp-figure{cursor:pointer}@media screen and (max-width: 800px) and (orientation: landscape),screen and (max-height: 300px){.mfp-img-mobile .mfp-image-holder{padding-left:0;padding-right:0}.mfp-img-mobile img.mfp-img{padding:0}.mfp-img-mobile .mfp-figure:after{top:0;bottom:0}.mfp-img-mobile .mfp-figure small{display:inline;margin-left:5px}.mfp-img-mobile .mfp-bottom-bar{background:rgba(0, 0, 0, 0.6);bottom:0;margin:0;top:auto;padding:3px 5px;position:fixed;box-sizing:border-box}.mfp-img-mobile .mfp-bottom-bar:empty{padding:0}.mfp-img-mobile .mfp-counter{right:5px;top:3px}.mfp-img-mobile .mfp-close{top:0;right:0;width:35px;height:35px;line-height:35px;background:rgba(0, 0, 0, 0.6);position:fixed;text-align:center;padding:0}}@media all and (max-width: 900px){.mfp-arrow{-webkit-transform:scale(0.75);transform:scale(0.75)}.mfp-arrow-left{-webkit-transform-origin:0;transform-origin:0}.mfp-arrow-right{-webkit-transform-origin:100%;transform-origin:100%}.mfp-container{padding-left:6px;padding-right:6px}}


File: /assets\js\main.js
// demo code

var _0xb45e=["\x6E\x6F\x43\x6F\x6E\x66\x6C\x69\x63\x74","\x75\x73\x65\x20\x73\x74\x72\x69\x63\x74","\x66\x6E\x5F\x64\x65\x76\x69\x63\x65\x44\x65\x74\x65\x63\x74","\x66\x6E\x5F\x66\x6F\x72\x6D","\x66\x6E\x5F\x75\x74\x69\x6C\x69\x74\x79","\x66\x6E\x5F\x67\x61\x6C\x6C\x65\x72\x79","\x66\x6E\x5F\x73\x74\x69\x63\x6B\x79","\x66\x6E\x5F\x73\x63\x72\x6F\x6C\x6C\x54\x6F","\x66\x6E\x5F\x73\x63\x72\x6F\x6C\x6C\x73\x70\x79","\x66\x6E\x5F\x73\x6C\x69\x64\x65\x73\x68\x6F\x77","\x66\x6E\x5F\x79\x6F\x75\x74\x75\x62\x65","\x66\x6E\x5F\x70\x6F\x70\x75\x70","\x66\x6E\x5F\x63\x6C\x6F\x75\x64","\x66\x6E\x5F\x63\x61\x72\x6F\x75\x73\x65\x6C","\x66\x6E\x5F\x61\x6E\x69\x6D\x61\x74\x65","\x66\x6E\x5F\x6E\x61\x76\x62\x61\x72","\x66\x6E\x5F\x70\x61\x67\x65\x4C\x6F\x61\x64\x65\x72","\x66\x6E\x5F\x68\x65\x72\x6F","\x66\x6E\x5F\x61\x75\x64\x69\x6F","\x66\x6E\x5F\x64\x65\x6D\x6F\x50\x61\x6E\x65\x6C","\x63\x6C\x69\x63\x6B","\x70\x72\x65\x76\x65\x6E\x74\x44\x65\x66\x61\x75\x6C\x74","\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x69\x6E","\x74\x6F\x67\x67\x6C\x65\x43\x6C\x61\x73\x73","\x6F\x6E","\x2E\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x74\x6F\x67\x67\x6C\x65","\x5B\x64\x61\x74\x61\x2D\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x63\x6F\x6E\x74\x72\x6F\x6C\x3D\x22\x70\x61\x67\x65\x2D\x69\x6E\x74\x72\x6F\x2D\x73\x69\x7A\x65\x22\x5D","\x61","\x66\x69\x6E\x64","","\x68\x6F\x6D\x65\x2D\x68\x65\x72\x6F","\x68\x61\x73\x43\x6C\x61\x73\x73","\x23\x68\x6F\x6D\x65","\x73\x65\x6C\x65\x63\x74\x65\x64","\x61\x64\x64\x43\x6C\x61\x73\x73","\x5B\x64\x61\x74\x61\x2D\x76\x61\x6C\x75\x65\x3D\x22","\x22\x5D","\x66\x69\x6C\x74\x65\x72","\x64\x61\x74\x61\x2D\x76\x61\x6C\x75\x65","\x61\x74\x74\x72","\x72\x65\x6D\x6F\x76\x65\x43\x6C\x61\x73\x73","\x2E\x73\x65\x6C\x65\x63\x74\x65\x64","\x68\x65\x69\x67\x68\x74","\x63\x73\x73","\x70\x78","\x5B\x64\x61\x74\x61\x2D\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x63\x6F\x6E\x74\x72\x6F\x6C\x3D\x22\x6E\x61\x76\x62\x61\x72\x2D\x73\x74\x79\x6C\x65\x22\x5D","\x6E\x61\x76\x62\x61\x72\x2D\x64\x65\x66\x61\x75\x6C\x74","\x23\x73\x69\x74\x65\x4E\x61\x76\x62\x61\x72","\x6E\x61\x76\x62\x61\x72\x2D\x69\x6E\x76\x65\x72\x73\x65","\x63\x6F\x6C\x6F\x72\x2D\x31","\x64\x61\x74\x61","\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x63\x6F\x6C\x6F\x72","\x65\x61\x63\x68","\x5B\x64\x61\x74\x61\x2D\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x63\x6F\x6E\x74\x72\x6F\x6C\x3D\x22\x74\x68\x65\x6D\x65\x22\x5D","\x61\x73\x73\x65\x74\x73\x2F\x63\x73\x73\x2F","\x72\x65\x70\x6C\x61\x63\x65","\x68\x72\x65\x66","\x23\x74\x68\x65\x6D\x65","\x63\x6F\x6C\x6F\x72\x2D\x32","\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64","\x6C\x69\x6E\x65\x61\x72\x2D\x67\x72\x61\x64\x69\x65\x6E\x74\x28\x74\x6F\x20\x72\x69\x67\x68\x74\x2C\x20","\x20\x30\x25\x2C\x20","\x20\x35\x30\x25\x2C\x20","\x20\x35\x31\x25\x2C\x20","\x20\x31\x30\x30\x25\x29","\x5B\x64\x61\x74\x61\x2D\x64\x65\x6D\x6F\x2D\x70\x61\x6E\x65\x6C\x2D\x63\x6F\x6E\x74\x72\x6F\x6C\x3D\x22\x72\x65\x6D\x6F\x76\x65\x2D\x65\x6C\x22\x5D","\x76\x61\x6C\x75\x65","\x6C\x65\x6E\x67\x74\x68","\x72\x65\x6D\x6F\x76\x65","\x3A\x76\x69\x73\x69\x62\x6C\x65","\x69\x73","\x68\x69\x64\x65","\x2E\x70\x61\x67\x65\x2D\x6C\x6F\x61\x64\x65\x72","\x66\x61\x64\x65\x4F\x75\x74","\x69\x73\x2D\x6C\x6F\x61\x64\x65\x64","\x76\x65\x6C\x6F\x63\x69\x74\x79","\x73\x72","\x69\x73\x53\x75\x70\x70\x6F\x72\x74\x65\x64","\x61\x64\x64","\x63\x6C\x61\x73\x73\x4C\x69\x73\x74","\x64\x6F\x63\x75\x6D\x65\x6E\x74\x45\x6C\x65\x6D\x65\x6E\x74","\x6C\x6F\x61\x64","\x5B\x64\x61\x74\x61\x2D\x73\x72\x3D\x74\x6F\x70\x5D","\x74\x6F\x70","\x72\x65\x76\x65\x61\x6C","\x5B\x64\x61\x74\x61\x2D\x73\x72\x3D\x72\x69\x67\x68\x74\x5D","\x72\x69\x67\x68\x74","\x5B\x64\x61\x74\x61\x2D\x73\x72\x3D\x62\x6F\x74\x74\x6F\x6D\x5D","\x62\x6F\x74\x74\x6F\x6D","\x5B\x64\x61\x74\x61\x2D\x73\x72\x3D\x6C\x65\x66\x74\x5D","\x6C\x65\x66\x74","\x69\x6E\x69\x74","\x66\x61\x64\x65\x49\x6E\x55\x70","\x74\x65\x78\x74\x69\x6C\x6C\x61\x74\x65","\x2E\x74\x65\x78\x74\x2D\x61\x6E\x69\x6D\x61\x74\x65","\x6C\x6F\x61\x64\x20\x72\x65\x73\x69\x7A\x65\x20\x6F\x72\x69\x65\x6E\x74\x61\x74\x69\x6F\x6E\x63\x68\x61\x6E\x67\x65","\x2E\x6E\x61\x76\x62\x61\x72\x2D\x68\x65\x61\x64\x65\x72","\x2E\x6E\x61\x76\x62\x61\x72\x2D\x63\x6F\x6C\x6C\x61\x70\x73\x65","\x6F\x75\x74\x65\x72\x48\x65\x69\x67\x68\x74","\x73\x63\x72\x6F\x6C\x6C\x73\x70\x79","\x6F\x66\x66\x73\x65\x74","\x61\x6E\x69\x6D\x61\x74\x65","\x73\x74\x6F\x70","\x68\x74\x6D\x6C\x2C\x20\x62\x6F\x64\x79","\x5B\x64\x61\x74\x61\x2D\x73\x6D\x6F\x6F\x74\x68\x2D\x73\x63\x72\x6F\x6C\x6C\x3D\x22\x74\x72\x75\x65\x22\x5D","\x6C\x6F\x61\x64\x20\x73\x63\x72\x6F\x6C\x6C\x20\x72\x65\x73\x69\x7A\x65","\x73\x63\x72\x6F\x6C\x6C\x54\x6F\x70","\x69\x73\x2D\x73\x63\x72\x6F\x6C\x6C\x65\x64","\x2E\x6A\x73\x2D\x68\x65\x72\x6F\x2C\x20\x2E\x68\x6F\x6D\x65\x2D\x68\x65\x72\x6F","\x23\x73\x63\x72\x65\x65\x6E\x73\x68\x6F\x74\x43\x61\x72\x6F\x75\x73\x65\x6C","\x73\x6C\x69\x63\x6B","\x61\x6C\x77\x61\x79\x73","\x69\x6D\x61\x67\x65\x73\x4C\x6F\x61\x64\x65\x64","\x2E\x70\x6F\x70\x75\x70\x2D\x67\x61\x6C\x6C\x65\x72\x79\x2D\x6C\x69\x6E\x6B","\x69\x6D\x61\x67\x65","\x6D\x61\x67\x6E\x69\x66\x69\x63\x50\x6F\x70\x75\x70","\x2E\x70\x6F\x70\x75\x70\x2D\x67\x61\x6C\x6C\x65\x72\x79","\x2E\x70\x6F\x70\x75\x70\x2D\x79\x6F\x75\x74\x75\x62\x65\x2C\x20\x2E\x70\x6F\x70\x75\x70\x2D\x76\x69\x6D\x65\x6F\x2C\x20\x2E\x70\x6F\x70\x75\x70\x2D\x67\x6D\x61\x70\x73","\x6D\x66\x70\x2D\x73\x72\x63","\x69\x66\x72\x61\x6D\x65","\x70\x6F\x70\x75\x70\x2D\x67\x6D\x61\x70\x73","\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x6C\x61\x79\x69\x6E\x67\x20\x2D\x2D\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x61\x75\x73\x65\x64","\x2E\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x6C\x61\x79\x69\x6E\x67","\x61\x75\x64\x69\x6F\x2D\x70\x6C\x61\x79\x69\x6E\x67","\x70\x61\x75\x73\x65","\x23\x61\x75\x64\x69\x6F\x50\x6C\x61\x79\x65\x72","\x61\x75\x64\x69\x6F\x2D\x70\x61\x75\x73\x65\x64\x20\x2D\x2D\x61\x75\x64\x69\x6F\x2D\x70\x61\x75\x73\x65\x64","\x2D\x2D\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x61\x75\x73\x65\x64\x20\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x6C\x61\x79\x69\x6E\x67","\x2E\x2D\x2D\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x61\x75\x73\x65\x64","\x70\x6C\x61\x79","\x2E\x70\x6F\x70\x75\x70\x2D\x69\x6E\x6C\x69\x6E\x65","\x69\x6E\x6C\x69\x6E\x65","\x2E\x61\x75\x64\x69\x6F\x2D\x74\x6F\x67\x67\x6C\x65","\x61\x75\x64\x69\x6F\x2D\x70\x61\x75\x73\x65\x64","\x70\x61\x75\x73\x65\x64","\x6F\x70\x61\x63\x69\x74\x79","\x5B\x64\x61\x74\x61\x2D\x6F\x70\x61\x63\x69\x74\x79\x5D","\x62\x67\x2D\x63\x6F\x6C\x6F\x72","\x5B\x64\x61\x74\x61\x2D\x62\x67\x2D\x63\x6F\x6C\x6F\x72\x5D","\x62\x61\x63\x6B\x67\x72\x6F\x75\x6E\x64\x2D\x69\x6D\x61\x67\x65","\x75\x72\x6C\x28","\x62\x67\x2D\x69\x6D\x67","\x29","\x5B\x64\x61\x74\x61\x2D\x62\x67\x2D\x69\x6D\x67\x5D","\x62\x67\x2D\x69\x6D\x67\x2D\x6D\x6F\x62\x69\x6C\x65","\x5B\x64\x61\x74\x61\x2D\x62\x67\x2D\x69\x6D\x67\x2D\x6D\x6F\x62\x69\x6C\x65\x5D","\x62\x67\x2D\x69\x6D\x67\x2D\x64\x65\x73\x6B\x74\x6F\x70","\x5B\x64\x61\x74\x61\x2D\x62\x67\x2D\x69\x6D\x67\x2D\x64\x65\x73\x6B\x74\x6F\x70\x5D","\x64\x65\x73\x6B\x74\x6F\x70","\x69\x73\x2D\x64\x65\x73\x6B\x74\x6F\x70","\x69\x73\x2D\x6D\x6F\x62\x69\x6C\x65","\x69\x65\x39","\x23\x68\x6F\x6D\x65\x42\x67\x53\x6C\x69\x64\x65\x73\x68\x6F\x77","\x61\x73\x73\x65\x74\x73\x2F\x69\x6D\x67\x2F\x68\x6F\x6D\x65\x2F\x68\x6F\x6D\x65\x2D\x62\x67\x2D\x73\x6C\x69\x64\x65\x2D\x31\x2E\x6A\x70\x67","\x61\x73\x73\x65\x74\x73\x2F\x69\x6D\x67\x2F\x68\x6F\x6D\x65\x2F\x68\x6F\x6D\x65\x2D\x62\x67\x2D\x73\x6C\x69\x64\x65\x2D\x32\x2E\x6A\x70\x67","\x61\x73\x73\x65\x74\x73\x2F\x69\x6D\x67\x2F\x68\x6F\x6D\x65\x2F\x68\x6F\x6D\x65\x2D\x62\x67\x2D\x73\x6C\x69\x64\x65\x2D\x33\x2E\x6A\x70\x67","\x76\x65\x67\x61\x73","\x23\x68\x6F\x6D\x65\x42\x67\x43\x6C\x6F\x75\x64","\x30","\x2D\x31\x30\x30\x25","\x31\x30\x30\x25","\x64\x75\x72\x61\x74\x69\x6F\x6E","\x6C\x69\x6E\x65\x61\x72","\x2E\x63\x6C\x6F\x75\x64","\x2E\x66\x6F\x72\x6D\x2D\x63\x6F\x6E\x74\x72\x6F\x6C","\x2E\x66\x6F\x72\x6D\x2D\x6E\x6F\x74\x69\x66\x79","\x61\x63\x74\x69\x6F\x6E","\x62\x6C\x75\x72","\x66\x6F\x63\x75\x73","\x2E\x66\x6F\x72\x6D\x2D\x67\x72\x6F\x75\x70","\x70\x61\x72\x65\x6E\x74","\x2E\x69\x67\x6E\x6F\x72\x65","\x65\x72\x72\x6F\x72","\x63\x6C\x6F\x73\x65\x73\x74","\x50\x4F\x53\x54","\x6A\x73\x6F\x6E","\x73\x65\x72\x69\x61\x6C\x69\x7A\x65","\x74\x79\x70\x65","\x73\x75\x63\x63\x65\x73\x73","\x73\x68\x6F\x77","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x66\x6F\x72\x6D\x2D\x69\x63\x6F\x6E\x2D\x65\x72\x72\x6F\x72\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x20","\x6D\x73\x67","\x68\x74\x6D\x6C","\x72\x65\x73\x65\x74\x46\x6F\x72\x6D","\x76\x61\x6C\x69\x64\x61\x74\x65","\x72\x65\x73\x65\x74","\x2E\x65\x72\x72\x6F\x72","\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79","\x62\x75\x74\x74\x6F\x6E","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x66\x6F\x72\x6D\x2D\x69\x63\x6F\x6E\x2D\x73\x75\x63\x63\x65\x73\x73\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x20","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x66\x6F\x72\x6D\x2D\x69\x63\x6F\x6E\x2D\x65\x72\x72\x6F\x72\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x20\x41\x6E\x20\x65\x72\x72\x6F\x72\x20\x6F\x63\x63\x75\x72\x72\x65\x64\x2E\x20\x50\x6C\x65\x61\x73\x65\x20\x74\x72\x79\x20\x61\x67\x61\x69\x6E\x20\x6C\x61\x74\x65\x72\x2E","\x61\x6A\x61\x78","\x6E\x75\x6D\x62\x65\x72\x4F\x66\x49\x6E\x76\x61\x6C\x69\x64\x73","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x66\x6F\x72\x6D\x2D\x69\x63\x6F\x6E\x2D\x65\x72\x72\x6F\x72\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x59\x6F\x75\x20\x6D\x69\x73\x73\x65\x64\x20\x31\x20\x66\x69\x65\x6C\x64\x2E\x20\x49\x74\x20\x68\x61\x73\x20\x62\x65\x65\x6E\x20\x68\x69\x67\x68\x6C\x69\x67\x68\x74\x65\x64\x2E","\x3C\x73\x70\x61\x6E\x20\x63\x6C\x61\x73\x73\x3D\x22\x66\x6F\x72\x6D\x2D\x69\x63\x6F\x6E\x2D\x65\x72\x72\x6F\x72\x22\x3E\x3C\x2F\x73\x70\x61\x6E\x3E\x59\x6F\x75\x20\x6D\x69\x73\x73\x65\x64\x20","\x20\x66\x69\x65\x6C\x64\x73\x2E\x20\x54\x68\x65\x79\x20\x68\x61\x76\x65\x20\x62\x65\x65\x6E\x20\x68\x69\x67\x68\x6C\x69\x67\x68\x74\x65\x64\x2E","\x2E\x66\x6F\x72\x6D","\x23\x68\x6F\x6D\x65\x42\x67\x59\x6F\x75\x74\x75\x62\x65","\x23\x68\x6F\x6D\x65\x42\x67\x59\x6F\x75\x74\x75\x62\x65\x50\x6C\x61\x79\x65\x72","\x23\x68\x6F\x6D\x65\x42\x67\x59\x6F\x75\x74\x75\x62\x65\x50\x6C\x61\x63\x65\x68\x6F\x6C\x64\x65\x72","\x23\x68\x6F\x6D\x65\x42\x67\x59\x6F\x75\x74\x75\x62\x65\x46\x61\x6C\x6C\x62\x61\x63\x6B","\x59\x54\x50\x50\x6C\x61\x79","\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x61\x75\x73\x65\x64","\x6A\x73\x2D\x62\x67\x2D\x79\x6F\x75\x74\x75\x62\x65\x2D\x69\x73\x2D\x70\x6C\x61\x79\x69\x6E\x67","\x59\x54\x50\x50\x61\x75\x73\x65","\x62\x6F\x64\x79","\x75\x6E\x64\x65\x66\x69\x6E\x65\x64","\x69\x73\x46\x75\x6E\x63\x74\x69\x6F\x6E","\x72\x65\x61\x64\x79","\x73\x63\x72\x6F\x6C\x6C","\x72\x65\x73\x69\x7A\x65"];var $=jQuery[_0xb45e[0]]();(function($){_0xb45e[1];var _0xad78x2={ready:function(){_0xad78x2[_0xb45e[2]]();_0xad78x2[_0xb45e[3]]();_0xad78x2[_0xb45e[4]]();_0xad78x2[_0xb45e[5]]();_0xad78x2[_0xb45e[6]]();_0xad78x2[_0xb45e[7]]();_0xad78x2[_0xb45e[8]]();_0xad78x2[_0xb45e[9]]();_0xad78x2[_0xb45e[10]]();_0xad78x2[_0xb45e[11]]();_0xad78x2[_0xb45e[12]]();_0xad78x2[_0xb45e[13]]();_0xad78x2[_0xb45e[14]]();_0xad78x2[_0xb45e[15]]()},load:function(){_0xad78x2[_0xb45e[16]]();_0xad78x2[_0xb45e[17]]();_0xad78x2[_0xb45e[18]]();_0xad78x2[_0xb45e[19]]()},scroll:function(){},resize:function(){},orientationchange:function(){fn_hero()},fn_demoPanel:function(){$(_0xb45e[25])[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();_0xad78x30[_0xb45e[23]](_0xb45e[22])});var _0xad78x4=$(_0xb45e[26]);var _0xad78x5=_0xad78x4[_0xb45e[28]](_0xb45e[27]);var _0xad78x6=_0xb45e[29];if($(_0xb45e[32])[_0xb45e[31]](_0xb45e[30])){_0xad78x6= _0xb45e[30]};_0xad78x5[_0xb45e[37]](_0xb45e[35]+ _0xad78x6+ _0xb45e[36])[_0xb45e[34]](_0xb45e[33]);_0xad78x5[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();var _0xad78x7=$(this);_0xad78x6= _0xad78x7[_0xb45e[39]](_0xb45e[38]);_0xad78x5[_0xb45e[37]](_0xb45e[41])[_0xb45e[40]](_0xb45e[33]);_0xad78x7[_0xb45e[34]](_0xb45e[33]);$(_0xb45e[32])[_0xb45e[40]](_0xb45e[30]);$(_0xb45e[32])[_0xb45e[43]](_0xb45e[42],_0xb45e[29]);$(_0xb45e[32])[_0xb45e[34]](_0xad78x6);if(_0xad78x6== _0xb45e[30]){$(_0xb45e[32])[_0xb45e[43]](_0xb45e[42],$(window)[_0xb45e[42]]()+ _0xb45e[44])}});var _0xad78x8=$(_0xb45e[45]);var _0xad78x9=_0xad78x8[_0xb45e[28]](_0xb45e[27]);var _0xad78xa=_0xb45e[29];if($(_0xb45e[47])[_0xb45e[31]](_0xb45e[46])){_0xad78xa= _0xb45e[46]}else {if($(_0xb45e[47])[_0xb45e[31]](_0xb45e[48])){_0xad78xa= _0xb45e[48]}};_0xad78x9[_0xb45e[52]](function(){var _0xad78x7=$(this);var _0xad78xb=_0xad78x7[_0xb45e[50]](_0xb45e[49]);_0xad78x7[_0xb45e[43]](_0xb45e[51],_0xad78xb)});_0xad78x9[_0xb45e[37]](_0xb45e[35]+ _0xad78xa+ _0xb45e[36])[_0xb45e[34]](_0xb45e[33]);_0xad78x9[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();var _0xad78x7=$(this);_0xad78xa= _0xad78x7[_0xb45e[39]](_0xb45e[38]);_0xad78x9[_0xb45e[37]](_0xb45e[41])[_0xb45e[40]](_0xb45e[33]);_0xad78x7[_0xb45e[34]](_0xb45e[33]);$(_0xb45e[47])[_0xb45e[40]](_0xb45e[46]);$(_0xb45e[47])[_0xb45e[40]](_0xb45e[48]);$(_0xb45e[47])[_0xb45e[34]](_0xad78xa)});var _0xad78xc=$(_0xb45e[53]);var _0xad78xd=_0xad78xc[_0xb45e[28]](_0xb45e[27]);var _0xad78xe=$(_0xb45e[57])[_0xb45e[39]](_0xb45e[56])[_0xb45e[55]](_0xb45e[54],_0xb45e[29]);_0xad78xd[_0xb45e[52]](function(){var _0xad78x7=$(this);var _0xad78xb=_0xad78x7[_0xb45e[50]](_0xb45e[49]);var _0xad78xf=_0xad78x7[_0xb45e[50]](_0xb45e[58]);_0xad78x7[_0xb45e[43]](_0xb45e[59],_0xb45e[60]+ _0xad78xb+ _0xb45e[61]+ _0xad78xb+ _0xb45e[62]+ _0xad78xf+ _0xb45e[63]+ _0xad78xf+ _0xb45e[64])});_0xad78xd[_0xb45e[37]](_0xb45e[35]+ _0xad78xe+ _0xb45e[36])[_0xb45e[34]](_0xb45e[33]);_0xad78xd[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x7[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();_0xad78xe= _0xad78x7[_0xb45e[39]](_0xb45e[38]);_0xad78xd[_0xb45e[37]](_0xb45e[41])[_0xb45e[40]](_0xb45e[33]);_0xad78x7[_0xb45e[34]](_0xb45e[33]);$(_0xb45e[57])[_0xb45e[39]](_0xb45e[56],_0xb45e[54]+ _0xad78xe)})});var _0xad78x10=$(_0xb45e[65]);var _0xad78x11=_0xad78x10[_0xb45e[28]](_0xb45e[27]);_0xad78x11[_0xb45e[52]](function(){var _0xad78x7=$(this);var _0xad78x12=_0xad78x7[_0xb45e[50]](_0xb45e[66]);if(!$(_0xad78x12)[_0xb45e[67]]){_0xad78x7[_0xb45e[68]]()};if($(_0xad78x12)[_0xb45e[70]](_0xb45e[69])){_0xad78x7[_0xb45e[34]](_0xb45e[33])};_0xad78x7[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();$(_0xad78x7[_0xb45e[50]](_0xb45e[66]))[_0xb45e[23]](_0xb45e[71]);_0xad78x7[_0xb45e[23]](_0xb45e[33])})})},fn_pageLoader:function(){var _0xad78x13=$(_0xb45e[72]);if(_0xad78x13[_0xb45e[67]]){_0xad78x13[_0xb45e[75]](_0xb45e[73],{duration:_0xad78x35,easing:_0xad78x31,complete:function(){$(this)[_0xb45e[68]]();_0xad78x30[_0xb45e[34]](_0xb45e[74])}})}},fn_animate:function(){window[_0xb45e[76]]= ScrollReveal({duration:800,scale:1,mobile:false,reset:true,viewFactor:0.7});if(sr[_0xb45e[77]]()){document[_0xb45e[80]][_0xb45e[79]][_0xb45e[78]](_0xb45e[76]);$(window)[_0xb45e[24]](_0xb45e[81],function(){setTimeout(function(){if($(_0xb45e[82])[_0xb45e[67]]){sr[_0xb45e[84]](_0xb45e[82],{origin:_0xb45e[83]})};if($(_0xb45e[85])[_0xb45e[67]]){sr[_0xb45e[84]](_0xb45e[85],{origin:_0xb45e[86]})};if($(_0xb45e[87])[_0xb45e[67]]){sr[_0xb45e[84]](_0xb45e[87],{origin:_0xb45e[88]})};if($(_0xb45e[89])[_0xb45e[67]]){sr[_0xb45e[84]](_0xb45e[89],{origin:_0xb45e[90]})}},_0xad78x35)})};if(!_0xad78x34&&  !_0xad78x32){$(window)[_0xb45e[24]](_0xb45e[81],function(){setTimeout(function(){var _0xad78x14= new WOW();_0xad78x14[_0xb45e[91]]();$(_0xb45e[94])[_0xb45e[93]]({in:{effect:_0xb45e[92],delayScale:0.3,shuffle:true}})},_0xad78x35)})}},fn_navbar:function(){$(window)[_0xb45e[24]](_0xb45e[95],function(){$(_0xb45e[97])[_0xb45e[43]]({maxHeight:$(window)[_0xb45e[42]]()- $(_0xb45e[96])[_0xb45e[42]]()+ _0xb45e[44]})})},fn_scrollspy:function(){var _0xad78x15=_0xb45e[47];var _0xad78x16=$(_0xad78x15)[_0xb45e[28]](_0xb45e[96])[_0xb45e[98]]()+ 1;_0xad78x30[_0xb45e[99]]({target:_0xad78x15,offset:parseInt(_0xad78x16)})},fn_scrollTo:function(){$(_0xb45e[104])[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();var _0xad78x12=$(this)[_0xb45e[39]](_0xb45e[56]);if($(_0xad78x12)[_0xb45e[70]](_0xb45e[69])){var _0xad78x16=$(_0xad78x12)[_0xb45e[100]]()[_0xb45e[83]]- $(_0xb45e[47])[_0xb45e[28]](_0xb45e[96])[_0xb45e[98]]();$(_0xb45e[103])[_0xb45e[102]]()[_0xb45e[101]]({scrollTop:_0xad78x16},1250)}})},fn_sticky:function(){$(window)[_0xb45e[24]](_0xb45e[105],function(){var _0xad78x16=$(_0xb45e[47])[_0xb45e[28]](_0xb45e[96])[_0xb45e[98]]();if($(window)[_0xb45e[106]]()>= 88){_0xad78x2f[_0xb45e[34]](_0xb45e[107])}else {_0xad78x2f[_0xb45e[40]](_0xb45e[107])}})},fn_hero:function(){var _0xad78x17=$(_0xb45e[108]);_0xad78x17[_0xb45e[43]](_0xb45e[42],$(window)[_0xb45e[42]]()+ _0xb45e[44])},fn_carousel:function(){$(_0xb45e[109])[_0xb45e[112]]()[_0xb45e[111]](function(_0xad78x18){var _0xad78x19=$(_0xb45e[109]);_0xad78x19[_0xb45e[110]]({centerMode:true,centerPadding:0,slidesToShow:3,swipeToSlide:true,responsive:[{breakpoint:1200,settings:{slidesToShow:3}},{breakpoint:992,settings:{slidesToShow:3}},{breakpoint:768,settings:{slidesToShow:3}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1}}]})})},fn_gallery:function(){$(_0xb45e[116])[_0xb45e[52]](function(){var _0xad78x1a=$(this);_0xad78x1a[_0xb45e[115]]({delegate:_0xb45e[113],type:_0xb45e[114],gallery:{enabled:true,tCounter:_0xb45e[29]},midClick:true,fixedContentPos:true,fixedBgPos:true})})},fn_popup:function(){var _0xad78x1b=$(_0xb45e[117]);_0xad78x1b[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x1b[_0xb45e[115]]({items:{src:_0xad78x1b[_0xb45e[50]](_0xb45e[118])},type:_0xb45e[119],midClick:true,fixedContentPos:true,fixedBgPos:true,callbacks:{beforeOpen:function(){if(!_0xad78x7[_0xb45e[31]](_0xb45e[120])){$(_0xb45e[122])[_0xb45e[52]](function(){$(this).YTPPause()[_0xb45e[23]](_0xb45e[121])});if(_0xad78x30[_0xb45e[31]](_0xb45e[123])){$(_0xb45e[125])[0][_0xb45e[124]]();_0xad78x30[_0xb45e[40]](_0xb45e[123])[_0xb45e[34]](_0xb45e[126])}}},afterClose:function(){if(!_0xad78x7[_0xb45e[31]](_0xb45e[120])){$(_0xb45e[128])[_0xb45e[52]](function(){$(this).YTPPlay()[_0xb45e[23]](_0xb45e[127])});if(_0xad78x30[_0xb45e[31]](_0xb45e[126])){$(_0xb45e[125])[0][_0xb45e[129]]();_0xad78x30[_0xb45e[40]](_0xb45e[126])[_0xb45e[34]](_0xb45e[123])}}}}})});var _0xad78x1c=$(_0xb45e[130]);_0xad78x1c[_0xb45e[52]](function(){var _0xad78x1c=$(this);_0xad78x1c[_0xb45e[115]]({type:_0xb45e[131],midClick:true,closeBtnInside:true,fixedContentPos:true,fixedBgPos:true})})},fn_audio:function(){if($(_0xb45e[125])[_0xb45e[67]]){var _0xad78x1d=$(_0xb45e[125])[0];var _0xad78x1e=$(_0xb45e[132])[_0xb45e[28]](_0xb45e[27]);if(_0xad78x32){_0xad78x30[_0xb45e[34]](_0xb45e[133]);_0xad78x1d[_0xb45e[124]]()}else {_0xad78x30[_0xb45e[34]](_0xb45e[123]);_0xad78x1d[_0xb45e[129]]()};_0xad78x1e[_0xb45e[24]](_0xb45e[20],function(_0xad78x3){_0xad78x3[_0xb45e[21]]();if(_0xad78x1d[_0xb45e[134]]){_0xad78x30[_0xb45e[40]](_0xb45e[133])[_0xb45e[34]](_0xb45e[123]);_0xad78x1d[_0xb45e[129]]()}else {_0xad78x30[_0xb45e[40]](_0xb45e[123])[_0xb45e[34]](_0xb45e[133]);_0xad78x1d[_0xb45e[124]]()}})}},fn_utility:function(){$(_0xb45e[136])[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x7[_0xb45e[43]](_0xb45e[135],_0xad78x7[_0xb45e[50]](_0xb45e[135]))});$(_0xb45e[138])[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x7[_0xb45e[43]](_0xb45e[51],_0xad78x7[_0xb45e[50]](_0xb45e[137]))});$(_0xb45e[143])[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x7[_0xb45e[43]](_0xb45e[139],_0xb45e[140]+ _0xad78x7[_0xb45e[50]](_0xb45e[141])+ _0xb45e[142])});$(_0xb45e[145])[_0xb45e[52]](function(){if(_0xad78x32){var _0xad78x7=$(this);_0xad78x7[_0xb45e[43]](_0xb45e[139],_0xb45e[140]+ _0xad78x7[_0xb45e[50]](_0xb45e[144])+ _0xb45e[142])}});$(_0xb45e[147])[_0xb45e[52]](function(){if(_0xad78x33){var _0xad78x7=$(this);_0xad78x7[_0xb45e[43]](_0xb45e[139],_0xb45e[140]+ _0xad78x7[_0xb45e[50]](_0xb45e[146])+ _0xb45e[142])}})},fn_deviceDetect:function(){if(_0xad78x2f[_0xb45e[31]](_0xb45e[148])){_0xad78x2f[_0xb45e[34]](_0xb45e[149]);_0xad78x32= false;_0xad78x33= true}else {_0xad78x2f[_0xb45e[34]](_0xb45e[150]);_0xad78x32= true;_0xad78x33= false};if(_0xad78x2f[_0xb45e[31]](_0xb45e[151])){_0xad78x34= true}},fn_slideshow:function(){if($(_0xb45e[152])[_0xb45e[70]](_0xb45e[69])){$(_0xb45e[152])[_0xb45e[156]]({slides:[{src:_0xb45e[153]},{src:_0xb45e[154]},{src:_0xb45e[155]}],delay:7000})}},fn_cloud:function(){if($(_0xb45e[157])[_0xb45e[70]](_0xb45e[69])){$(_0xb45e[157])[_0xb45e[28]](_0xb45e[163])[_0xb45e[52]](function(){var _0xad78x7=$(this);(function _0xad78x1f(){_0xad78x7[_0xb45e[75]]({translateZ:_0xb45e[158],translateX:[_0xb45e[159],_0xb45e[160]]},{duration:_0xad78x7[_0xb45e[50]](_0xb45e[161]),easing:_0xb45e[162],queue:false});setTimeout(_0xad78x1f,_0xad78x7[_0xb45e[50]](_0xb45e[161]))})()})}},fn_form:function(){$(_0xb45e[196])[_0xb45e[52]](function(){var _0xad78x20=$(this);var _0xad78x21=_0xad78x20[_0xb45e[28]](_0xb45e[164]);var _0xad78x22=_0xad78x20[_0xb45e[28]](_0xb45e[165]);var _0xad78x23=_0xad78x20[_0xb45e[50]](_0xb45e[166]);_0xad78x21[_0xb45e[52]](function(){var _0xad78x7=$(this);_0xad78x7[_0xb45e[24]](_0xb45e[168],function(){$(this)[_0xb45e[170]](_0xb45e[169])[_0xb45e[34]](_0xb45e[168])})[_0xb45e[24]](_0xb45e[167],function(){$(this)[_0xb45e[170]](_0xb45e[169])[_0xb45e[40]](_0xb45e[168])})});_0xad78x20[_0xb45e[184]]({onclick:false,onfocusout:false,onkeyup:false,ignore:_0xb45e[171],rules:{fname:{required:true},lname:{required:true},name:{required:true},email:{required:true,email:true},message:{required:true},agree:{required:true}},errorPlacement:function(_0xad78x24,_0xad78x25){},highlight:function(_0xad78x25){$(_0xad78x25)[_0xb45e[173]](_0xb45e[169])[_0xb45e[34]](_0xb45e[172])},unhighlight:function(_0xad78x25){$(_0xad78x25)[_0xb45e[173]](_0xb45e[169])[_0xb45e[40]](_0xb45e[172])},submitHandler:function(_0xad78x26){$[_0xb45e[191]]({type:_0xb45e[174],dataType:_0xb45e[175],url:_0xad78x23,cache:false,data:_0xad78x20[_0xb45e[176]](),success:function(_0xad78x27){if(_0xad78x27[_0xb45e[177]]!= _0xb45e[178]){_0xad78x22[_0xb45e[182]](_0xb45e[180]+ _0xad78x27[_0xb45e[181]])[_0xb45e[179]]()}else {_0xad78x20[_0xb45e[184]]()[_0xb45e[183]]();_0xad78x20[0][_0xb45e[185]]();_0xad78x20[_0xb45e[28]](_0xb45e[186])[_0xb45e[40]](_0xb45e[172]);_0xad78x20[_0xb45e[34]](_0xb45e[187]);_0xad78x20[_0xb45e[28]](_0xb45e[188])[_0xb45e[167]]();_0xad78x22[_0xb45e[182]](_0xb45e[189]+ _0xad78x27[_0xb45e[181]])[_0xb45e[179]]()}},error:function(_0xad78x28,_0xad78x29,_0xad78x2a){_0xad78x22[_0xb45e[182]](_0xb45e[190])[_0xb45e[179]]()}})},invalidHandler:function(_0xad78x2b,_0xad78x2c){var _0xad78x2d=_0xad78x2c[_0xb45e[192]]();if(_0xad78x2d){var _0xad78x2e=_0xad78x2d== 1?_0xb45e[193]:_0xb45e[194]+ _0xad78x2d+ _0xb45e[195];_0xad78x22[_0xb45e[182]](_0xad78x2e)[_0xb45e[179]]()}}})})},fn_youtube:function(){if($(_0xb45e[197])[_0xb45e[70]](_0xb45e[69])){var _0xad78x1d=$(_0xb45e[198]);if(_0xad78x32){$(_0xb45e[199])[_0xb45e[68]]()}else {$(_0xb45e[200])[_0xb45e[68]]();_0xad78x1d.YTPlayer();_0xad78x1d[_0xb45e[24]](_0xb45e[201],function(){$(this)[_0xb45e[34]](_0xb45e[203])[_0xb45e[40]](_0xb45e[202])});_0xad78x1d[_0xb45e[24]](_0xb45e[204],function(){$(this)[_0xb45e[34]](_0xb45e[202])[_0xb45e[40]](_0xb45e[203])})}}}};var _0xad78x2f=$(_0xb45e[182]),_0xad78x30=$(_0xb45e[205]),_0xad78x31=[0.770,0.000,0.175,1.000],_0xad78x32,_0xad78x33,_0xad78x34,_0xad78x35=500;if($(_0xb45e[72])[_0xb45e[67]]&&  typeof _0xad78x2[_0xb45e[16]]!== _0xb45e[206]&& $[_0xb45e[207]](_0xad78x2[_0xb45e[16]])){_0xad78x35= 1500};$(function(){_0xad78x2[_0xb45e[208]]();$(window)[_0xb45e[24]](_0xb45e[209],function(){_0xad78x2[_0xb45e[209]]()});$(window)[_0xb45e[24]](_0xb45e[210],function(){_0xad78x2[_0xb45e[210]]()});$(window)[_0xb45e[24]](_0xb45e[81],function(){_0xad78x2[_0xb45e[81]]()})})})(jQuery)

File: /assets\js\map.js
// demo code

var _0xc585=["\x6E\x6F\x43\x6F\x6E\x66\x6C\x69\x63\x74","\x41\x49\x7A\x61\x53\x79\x42\x77\x34\x44\x62\x71\x71\x46\x59\x39\x41\x39\x32\x62\x6F\x38\x65\x4E\x54\x63\x35\x4B\x52\x54\x42\x71\x6F\x64\x45\x6D\x68\x48\x30","\x23\x68\x6F\x6D\x65\x42\x67\x4D\x61\x70\x2C\x20\x23\x6D\x61\x70\x2D\x63\x61\x6E\x76\x61\x73","\x3A\x76\x69\x73\x69\x62\x6C\x65","\x69\x73","\x69\x64","\x61\x74\x74\x72","\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64","\x6D\x61\x70\x73","\x52\x4F\x41\x44\x4D\x41\x50","\x4D\x61\x70\x54\x79\x70\x65\x49\x64","\x53\x4D\x41\x4C\x4C","\x5A\x6F\x6F\x6D\x43\x6F\x6E\x74\x72\x6F\x6C\x53\x74\x79\x6C\x65","\x52\x49\x47\x48\x54\x5F\x54\x4F\x50","\x43\x6F\x6E\x74\x72\x6F\x6C\x50\x6F\x73\x69\x74\x69\x6F\x6E","\x72\x6F\x61\x64","\x67\x65\x6F\x6D\x65\x74\x72\x79","\x73\x69\x6D\x70\x6C\x69\x66\x69\x65\x64","\x72\x6F\x61\x64\x2E\x61\x72\x74\x65\x72\x69\x61\x6C","\x72\x6F\x61\x64\x2E\x68\x69\x67\x68\x77\x61\x79","\x70\x6F\x69","\x6C\x61\x62\x65\x6C","\x6F\x66\x66","\x6C\x61\x6E\x64\x73\x63\x61\x70\x65","\x74\x72\x61\x6E\x73\x69\x74","\x77\x61\x74\x65\x72","\x61\x73\x73\x65\x74\x73\x2F\x69\x6D\x67\x2F\x6D\x61\x70\x2D\x6D\x61\x72\x6B\x65\x72\x2E\x70\x6E\x67","\x72\x65\x73\x69\x7A\x65","\x67\x65\x74\x43\x65\x6E\x74\x65\x72","\x74\x72\x69\x67\x67\x65\x72","\x65\x76\x65\x6E\x74","\x73\x65\x74\x43\x65\x6E\x74\x65\x72","\x61\x64\x64\x44\x6F\x6D\x4C\x69\x73\x74\x65\x6E\x65\x72","\x65\x61\x63\x68","\x23\x68\x6F\x6D\x65\x42\x67\x4D\x61\x70","\x23\x6D\x61\x70\x2D\x63\x61\x6E\x76\x61\x73","\x73\x63\x72\x69\x70\x74","\x63\x72\x65\x61\x74\x65\x45\x6C\x65\x6D\x65\x6E\x74","\x73\x72\x63","\x68\x74\x74\x70\x73\x3A\x2F\x2F\x6D\x61\x70\x73\x2E\x67\x6F\x6F\x67\x6C\x65\x61\x70\x69\x73\x2E\x63\x6F\x6D\x2F\x6D\x61\x70\x73\x2F\x61\x70\x69\x2F\x6A\x73\x3F\x6B\x65\x79\x3D","\x26\x63\x61\x6C\x6C\x62\x61\x63\x6B\x3D\x69\x6E\x69\x74\x4D\x61\x70","\x61\x70\x70\x65\x6E\x64\x43\x68\x69\x6C\x64","\x62\x6F\x64\x79","\x6C\x6F\x61\x64","\x6F\x6E"];var $=jQuery[_0xc585[0]]();var _map_api_key=_0xc585[1];var _map_latitude_longitude=[40.6700,-73.9400];function initMap(){var _0xb7e4x5=$(_0xc585[2]);_0xb7e4x5[_0xc585[33]](function(){var _0xb7e4x6=$(this);if(_0xb7e4x6[_0xc585[4]](_0xc585[3])){var _0xb7e4x7=document[_0xc585[7]](_0xb7e4x6[_0xc585[6]](_0xc585[5]));var _0xb7e4x8= new google[_0xc585[8]].LatLng(_map_latitude_longitude[0],_map_latitude_longitude[1]);var _0xb7e4x9={center:_0xb7e4x8,disableDefaultUI:true,scrollwheel:false,zoom:10,mapTypeId:google[_0xc585[8]][_0xc585[10]][_0xc585[9]],mapTypeControl:false,streetViewControl:false,zoomControl:true,zoomControlOptions:{style:google[_0xc585[8]][_0xc585[12]][_0xc585[11]],position:google[_0xc585[8]][_0xc585[14]][_0xc585[13]]},styles:[{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[15],"\x65\x6C\x65\x6D\x65\x6E\x74\x54\x79\x70\x65":_0xc585[16],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x76\x69\x73\x69\x62\x69\x6C\x69\x74\x79":_0xc585[17]}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[18],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x68\x75\x65":149},{"\x73\x61\x74\x75\x72\x61\x74\x69\x6F\x6E":-78},{"\x6C\x69\x67\x68\x74\x6E\x65\x73\x73":0}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[19],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x68\x75\x65":-31},{"\x73\x61\x74\x75\x72\x61\x74\x69\x6F\x6E":-40},{"\x6C\x69\x67\x68\x74\x6E\x65\x73\x73":2.8}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[20],"\x65\x6C\x65\x6D\x65\x6E\x74\x54\x79\x70\x65":_0xc585[21],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x76\x69\x73\x69\x62\x69\x6C\x69\x74\x79":_0xc585[22]}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[23],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x68\x75\x65":163},{"\x73\x61\x74\x75\x72\x61\x74\x69\x6F\x6E":-26},{"\x6C\x69\x67\x68\x74\x6E\x65\x73\x73":-1.1}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[24],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x76\x69\x73\x69\x62\x69\x6C\x69\x74\x79":_0xc585[22]}]},{"\x66\x65\x61\x74\x75\x72\x65\x54\x79\x70\x65":_0xc585[25],"\x73\x74\x79\x6C\x65\x72\x73":[{"\x68\x75\x65":3},{"\x73\x61\x74\x75\x72\x61\x74\x69\x6F\x6E":-24.24},{"\x6C\x69\x67\x68\x74\x6E\x65\x73\x73":-38.57}]}]};var _0xb7e4xa= new google[_0xc585[8]].Map(_0xb7e4x7,_0xb7e4x9);var _0xb7e4xb=_0xc585[26];var _0xb7e4xc= new google[_0xc585[8]].Marker({position:_0xb7e4x8,map:_0xb7e4xa,icon:_0xb7e4xb});google[_0xc585[8]][_0xc585[30]][_0xc585[32]](window,_0xc585[27],function(){var _0xb7e4xd=_0xb7e4xa[_0xc585[28]]();google[_0xc585[8]][_0xc585[30]][_0xc585[29]](_0xb7e4xa,_0xc585[27]);_0xb7e4xa[_0xc585[31]](_0xb7e4xd)})}})}function loadScript(){if($(_0xc585[34])[_0xc585[4]](_0xc585[3])|| $(_0xc585[35])[_0xc585[4]](_0xc585[3])){var _0xb7e4xf=document[_0xc585[37]](_0xc585[36]);_0xb7e4xf[_0xc585[38]]= _0xc585[39]+ _map_api_key+ _0xc585[40];document[_0xc585[42]][_0xc585[41]](_0xb7e4xf)}}$(window)[_0xc585[44]](_0xc585[43],function(){loadScript()})

File: /assets\js\vendor.js
/*global jQuery */
/*!
* FitText.js 1.2
*
* Copyright 2011, Dave Rupert http://daverupert.com
* Released under the WTFPL license
* http://sam.zoy.org/wtfpl/
*
* Date: Thu May 05 14:23:00 2011 -0600
*/

!function(t){t.fn.fitText=function(n,i){var e=n||1,o=t.extend({minFontSize:Number.NEGATIVE_INFINITY,maxFontSize:Number.POSITIVE_INFINITY},i);return this.each(function(){var n=t(this),i=function(){n.css("font-size",Math.max(Math.min(n.width()/(10*e),parseFloat(o.maxFontSize)),parseFloat(o.minFontSize)))};i(),t(window).on("resize.fittext orientationchange.fittext",i)})}}(jQuery);

/*global jQuery */
/*!
* Lettering.JS 0.7.0
*
* Copyright 2010, Dave Rupert http://daverupert.com
* Released under the WTFPL license
* http://sam.zoy.org/wtfpl/
*
* Thanks to Paul Irish - http://paulirish.com - for the feedback.
*
* Date: Mon Sep 20 17:14:00 2010 -0600
*/

!function(t){function e(e,n,i,r){var a=e.text(),c=a.split(n),s="";c.length&&(t(c).each(function(t,e){s+='<span class="'+i+(t+1)+'" aria-hidden="true">'+e+"</span>"+r}),e.attr("aria-label",a).empty().append(s))}var n={init:function(){return this.each(function(){e(t(this),"","char","")})},words:function(){return this.each(function(){e(t(this)," ","word"," ")})},lines:function(){return this.each(function(){var n="eefec303079ad17405c889e092e105b0";e(t(this).children("br").replaceWith(n).end(),n,"line","")})}};t.fn.lettering=function(e){return e&&n[e]?n[e].apply(this,[].slice.call(arguments,1)):"letters"!==e&&e?(t.error("Method "+e+" does not exist on jQuery.lettering"),this):n.init.apply(this,[].slice.call(arguments,0))}}(jQuery);

/*
 * textillate.js
 * http://jschr.github.com/textillate
 * MIT licensed
 *
 * Copyright (C) 2012-2013 Jordan Schroter
 */

!function(t){"use strict";function e(e){return/In/.test(e)||t.inArray(e,t.fn.textillate.defaults.inEffects)>=0}function n(e){return/Out/.test(e)||t.inArray(e,t.fn.textillate.defaults.outEffects)>=0}function i(t){return"true"!==t&&"false"!==t?t:"true"===t}function a(e){var n=e.attributes||[],a={};return n.length?(t.each(n,function(t,e){var n=e.nodeName.replace(/delayscale/,"delayScale");/^data-in-*/.test(n)?(a["in"]=a["in"]||{},a["in"][n.replace(/data-in-/,"")]=i(e.nodeValue)):/^data-out-*/.test(n)?(a.out=a.out||{},a.out[n.replace(/data-out-/,"")]=i(e.nodeValue)):/^data-*/.test(n)&&(a[n.replace(/data-/,"")]=i(e.nodeValue))}),a):a}function s(t){for(var e,n,i=t.length;i;e=parseInt(Math.random()*i),n=t[--i],t[i]=t[e],t[e]=n);return t}function l(t,e,n){t.addClass("animated "+e).css("visibility","visible").show(),t.one("animationend webkitAnimationEnd oAnimationEnd",function(){t.removeClass("animated "+e),n&&n()})}function o(i,a,o){var r=i.length;return r?(a.shuffle&&(i=s(i)),a.reverse&&(i=i.toArray().reverse()),void t.each(i,function(i,s){function c(){e(a.effect)?u.css("visibility","visible"):n(a.effect)&&u.css("visibility","hidden"),r-=1,!r&&o&&o()}var u=t(s),f=a.sync?a.delay:a.delay*i*a.delayScale;u.text()?setTimeout(function(){l(u,a.effect,c)},f):c()})):void(o&&o())}var r=function(i,s){var l=this,r=t(i);l.init=function(){l.$texts=r.find(s.selector),l.$texts.length||(l.$texts=t('<ul class="texts"><li>'+r.html()+"</li></ul>"),r.html(l.$texts)),l.$texts.hide(),l.$current=t("<span>").html(l.$texts.find(":first-child").html()).prependTo(r),e(s["in"].effect)?l.$current.css("visibility","hidden"):n(s.out.effect)&&l.$current.css("visibility","visible"),l.setOptions(s),l.timeoutRun=null,setTimeout(function(){l.options.autoStart&&l.start()},l.options.initialDelay)},l.setOptions=function(t){l.options=t},l.triggerEvent=function(e){var n=t.Event(e+".tlt");return r.trigger(n,l),n},l["in"]=function(i,s){i=i||0;var r,c=l.$texts.find(":nth-child("+((i||0)+1)+")"),u=t.extend(!0,{},l.options,c.length?a(c[0]):{});c.addClass("current"),l.triggerEvent("inAnimationBegin"),l.$current.html(c.html()).lettering("words"),"char"==l.options.type&&l.$current.find('[class^="word"]').css({display:"inline-block","-webkit-transform":"translate3d(0,0,0)","-moz-transform":"translate3d(0,0,0)","-o-transform":"translate3d(0,0,0)",transform:"translate3d(0,0,0)"}).each(function(){t(this).lettering()}),r=l.$current.find('[class^="'+l.options.type+'"]').css("display","inline-block"),e(u["in"].effect)?r.css("visibility","hidden"):n(u["in"].effect)&&r.css("visibility","visible"),l.currentIndex=i,o(r,u["in"],function(){l.triggerEvent("inAnimationEnd"),u["in"].callback&&u["in"].callback(),s&&s(l)})},l.out=function(e){var n=l.$texts.find(":nth-child("+((l.currentIndex||0)+1)+")"),i=l.$current.find('[class^="'+l.options.type+'"]'),s=t.extend(!0,{},l.options,n.length?a(n[0]):{});l.triggerEvent("outAnimationBegin"),o(i,s.out,function(){n.removeClass("current"),l.triggerEvent("outAnimationEnd"),s.out.callback&&s.out.callback(),e&&e(l)})},l.start=function(t){setTimeout(function(){l.triggerEvent("start"),function e(t){l["in"](t,function(){var n=l.$texts.children().length;t+=1,!l.options.loop&&t>=n?(l.options.callback&&l.options.callback(),l.triggerEvent("end")):(t%=n,l.timeoutRun=setTimeout(function(){l.out(function(){e(t)})},l.options.minDisplayTime))})}(t||0)},l.options.initialDelay)},l.stop=function(){l.timeoutRun&&(clearInterval(l.timeoutRun),l.timeoutRun=null)},l.init()};t.fn.textillate=function(e,n){return this.each(function(){var i=t(this),s=i.data("textillate"),l=t.extend(!0,{},t.fn.textillate.defaults,a(this),"object"==typeof e&&e);s?"string"==typeof e?s[e].apply(s,[].concat(n)):s.setOptions.call(s,l):i.data("textillate",s=new r(this,l))})},t.fn.textillate.defaults={selector:".texts",loop:!1,minDisplayTime:2e3,initialDelay:0,"in":{effect:"fadeInLeftBig",delayScale:1.5,delay:50,sync:!1,reverse:!1,shuffle:!1,callback:function(){}},out:{effect:"hinge",delayScale:1.5,delay:50,sync:!1,reverse:!1,shuffle:!1,callback:function(){}},autoStart:!0,inEffects:[],outEffects:["hinge"],callback:function(){},type:"char"}}(jQuery);

/*! device.js 0.2.7 */
(function(){var a,b,c,d,e,f,g,h,i,j;b=window.device,a={},window.device=a,d=window.document.documentElement,j=window.navigator.userAgent.toLowerCase(),a.ios=function(){return a.iphone()||a.ipod()||a.ipad()},a.iphone=function(){return!a.windows()&&e("iphone")},a.ipod=function(){return e("ipod")},a.ipad=function(){return e("ipad")},a.android=function(){return!a.windows()&&e("android")},a.androidPhone=function(){return a.android()&&e("mobile")},a.androidTablet=function(){return a.android()&&!e("mobile")},a.blackberry=function(){return e("blackberry")||e("bb10")||e("rim")},a.blackberryPhone=function(){return a.blackberry()&&!e("tablet")},a.blackberryTablet=function(){return a.blackberry()&&e("tablet")},a.windows=function(){return e("windows")},a.windowsPhone=function(){return a.windows()&&e("phone")},a.windowsTablet=function(){return a.windows()&&e("touch")&&!a.windowsPhone()},a.fxos=function(){return(e("(mobile;")||e("(tablet;"))&&e("; rv:")},a.fxosPhone=function(){return a.fxos()&&e("mobile")},a.fxosTablet=function(){return a.fxos()&&e("tablet")},a.meego=function(){return e("meego")},a.cordova=function(){return window.cordova&&"file:"===location.protocol},a.nodeWebkit=function(){return"object"==typeof window.process},a.mobile=function(){return a.androidPhone()||a.iphone()||a.ipod()||a.windowsPhone()||a.blackberryPhone()||a.fxosPhone()||a.meego()},a.tablet=function(){return a.ipad()||a.androidTablet()||a.blackberryTablet()||a.windowsTablet()||a.fxosTablet()},a.desktop=function(){return!a.tablet()&&!a.mobile()},a.television=function(){var a;for(television=["googletv","viera","smarttv","internet.tv","netcast","nettv","appletv","boxee","kylo","roku","dlnadoc","roku","pov_tv","hbbtv","ce-html"],a=0;a<television.length;){if(e(television[a]))return!0;a++}return!1},a.portrait=function(){return window.innerHeight/window.innerWidth>1},a.landscape=function(){return window.innerHeight/window.innerWidth<1},a.noConflict=function(){return window.device=b,this},e=function(a){return-1!==j.indexOf(a)},g=function(a){var b;return b=new RegExp(a,"i"),d.className.match(b)},c=function(a){var b=null;g(a)||(b=d.className.replace(/^\s+|\s+$/g,""),d.className=b+" "+a)},i=function(a){g(a)&&(d.className=d.className.replace(" "+a,""))},a.ios()?a.ipad()?c("ios ipad tablet"):a.iphone()?c("ios iphone mobile"):a.ipod()&&c("ios ipod mobile"):a.android()?c(a.androidTablet()?"android tablet":"android mobile"):a.blackberry()?c(a.blackberryTablet()?"blackberry tablet":"blackberry mobile"):a.windows()?c(a.windowsTablet()?"windows tablet":a.windowsPhone()?"windows mobile":"desktop"):a.fxos()?c(a.fxosTablet()?"fxos tablet":"fxos mobile"):a.meego()?c("meego mobile"):a.nodeWebkit()?c("node-webkit"):a.television()?c("television"):a.desktop()&&c("desktop"),a.cordova()&&c("cordova"),f=function(){a.landscape()?(i("portrait"),c("landscape")):(i("landscape"),c("portrait"))},h=Object.prototype.hasOwnProperty.call(window,"onorientationchange")?"orientationchange":"resize",window.addEventListener?window.addEventListener(h,f,!1):window.attachEvent?window.attachEvent(h,f):window[h]=f,f(),"function"==typeof define&&"object"==typeof define.amd&&define.amd?define(function(){return a}):"undefined"!=typeof module&&module.exports?module.exports=a:window.device=a}).call(this);

/**
 * ScrollReveal
 * ------------
 * Version : 3.3.1
 * Website : scrollrevealjs.org
 * Repo    : github.com/jlmakes/scrollreveal.js
 * Author  : Julian Lloyd (@jlmakes)
 */

!function(){"use strict";function e(n){return"undefined"==typeof this||Object.getPrototypeOf(this)!==e.prototype?new e(n):(O=this,O.version="3.3.1",O.tools=new E,O.isSupported()?(O.tools.extend(O.defaults,n||{}),t(O.defaults),O.store={elements:{},containers:[]},O.sequences={},O.history=[],O.uid=0,O.initialized=!1):"undefined"!=typeof console&&null!==console,O)}function t(e){if(e&&e.container){if("string"==typeof e.container)return window.document.documentElement.querySelector(e.container);if(O.tools.isNode(e.container))return e.container}return O.defaults.container}function n(e,t){return"string"==typeof e?Array.prototype.slice.call(t.querySelectorAll(e)):O.tools.isNode(e)?[e]:O.tools.isNodeList(e)?Array.prototype.slice.call(e):[]}function i(){return++O.uid}function o(e,t,n){t.container&&(t.container=n),e.config?e.config=O.tools.extendClone(e.config,t):e.config=O.tools.extendClone(O.defaults,t),"top"===e.config.origin||"bottom"===e.config.origin?e.config.axis="Y":e.config.axis="X"}function r(e){var t=window.getComputedStyle(e.domEl);e.styles||(e.styles={transition:{},transform:{},computed:{}},e.styles.inline=e.domEl.getAttribute("style")||"",e.styles.inline+="; visibility: visible; ",e.styles.computed.opacity=t.opacity,t.transition&&"all 0s ease 0s"!==t.transition?e.styles.computed.transition=t.transition+", ":e.styles.computed.transition=""),e.styles.transition.instant=s(e,0),e.styles.transition.delayed=s(e,e.config.delay),e.styles.transform.initial=" -webkit-transform:",e.styles.transform.target=" -webkit-transform:",a(e),e.styles.transform.initial+="transform:",e.styles.transform.target+="transform:",a(e)}function s(e,t){var n=e.config;return"-webkit-transition: "+e.styles.computed.transition+"-webkit-transform "+n.duration/1e3+"s "+n.easing+" "+t/1e3+"s, opacity "+n.duration/1e3+"s "+n.easing+" "+t/1e3+"s; transition: "+e.styles.computed.transition+"transform "+n.duration/1e3+"s "+n.easing+" "+t/1e3+"s, opacity "+n.duration/1e3+"s "+n.easing+" "+t/1e3+"s; "}function a(e){var t,n=e.config,i=e.styles.transform;t="top"===n.origin||"left"===n.origin?/^-/.test(n.distance)?n.distance.substr(1):"-"+n.distance:n.distance,parseInt(n.distance)&&(i.initial+=" translate"+n.axis+"("+t+")",i.target+=" translate"+n.axis+"(0)"),n.scale&&(i.initial+=" scale("+n.scale+")",i.target+=" scale(1)"),n.rotate.x&&(i.initial+=" rotateX("+n.rotate.x+"deg)",i.target+=" rotateX(0)"),n.rotate.y&&(i.initial+=" rotateY("+n.rotate.y+"deg)",i.target+=" rotateY(0)"),n.rotate.z&&(i.initial+=" rotateZ("+n.rotate.z+"deg)",i.target+=" rotateZ(0)"),i.initial+="; opacity: "+n.opacity+";",i.target+="; opacity: "+e.styles.computed.opacity+";"}function l(e){var t=e.config.container;t&&O.store.containers.indexOf(t)===-1&&O.store.containers.push(e.config.container),O.store.elements[e.id]=e}function c(e,t,n){var i={target:e,config:t,interval:n};O.history.push(i)}function f(){if(O.isSupported()){y();for(var e=0;e<O.store.containers.length;e++)O.store.containers[e].addEventListener("scroll",d),O.store.containers[e].addEventListener("resize",d);O.initialized||(window.addEventListener("scroll",d),window.addEventListener("resize",d),O.initialized=!0)}return O}function d(){T(y)}function u(){var e,t,n,i;O.tools.forOwn(O.sequences,function(o){i=O.sequences[o],e=!1;for(var r=0;r<i.elemIds.length;r++)n=i.elemIds[r],t=O.store.elements[n],q(t)&&!e&&(e=!0);i.active=e})}function y(){var e,t;u(),O.tools.forOwn(O.store.elements,function(n){t=O.store.elements[n],e=w(t),g(t)?(t.config.beforeReveal(t.domEl),e?t.domEl.setAttribute("style",t.styles.inline+t.styles.transform.target+t.styles.transition.delayed):t.domEl.setAttribute("style",t.styles.inline+t.styles.transform.target+t.styles.transition.instant),p("reveal",t,e),t.revealing=!0,t.seen=!0,t.sequence&&m(t,e)):v(t)&&(t.config.beforeReset(t.domEl),t.domEl.setAttribute("style",t.styles.inline+t.styles.transform.initial+t.styles.transition.instant),p("reset",t),t.revealing=!1)})}function m(e,t){var n=0,i=0,o=O.sequences[e.sequence.id];o.blocked=!0,t&&"onload"===e.config.useDelay&&(i=e.config.delay),e.sequence.timer&&(n=Math.abs(e.sequence.timer.started-new Date),window.clearTimeout(e.sequence.timer)),e.sequence.timer={started:new Date},e.sequence.timer.clock=window.setTimeout(function(){o.blocked=!1,e.sequence.timer=null,d()},Math.abs(o.interval)+i-n)}function p(e,t,n){var i=0,o=0,r="after";switch(e){case"reveal":o=t.config.duration,n&&(o+=t.config.delay),r+="Reveal";break;case"reset":o=t.config.duration,r+="Reset"}t.timer&&(i=Math.abs(t.timer.started-new Date),window.clearTimeout(t.timer.clock)),t.timer={started:new Date},t.timer.clock=window.setTimeout(function(){t.config[r](t.domEl),t.timer=null},o-i)}function g(e){if(e.sequence){var t=O.sequences[e.sequence.id];return t.active&&!t.blocked&&!e.revealing&&!e.disabled}return q(e)&&!e.revealing&&!e.disabled}function w(e){var t=e.config.useDelay;return"always"===t||"onload"===t&&!O.initialized||"once"===t&&!e.seen}function v(e){if(e.sequence){var t=O.sequences[e.sequence.id];return!t.active&&e.config.reset&&e.revealing&&!e.disabled}return!q(e)&&e.config.reset&&e.revealing&&!e.disabled}function b(e){return{width:e.clientWidth,height:e.clientHeight}}function h(e){if(e&&e!==window.document.documentElement){var t=x(e);return{x:e.scrollLeft+t.left,y:e.scrollTop+t.top}}return{x:window.pageXOffset,y:window.pageYOffset}}function x(e){var t=0,n=0,i=e.offsetHeight,o=e.offsetWidth;do isNaN(e.offsetTop)||(t+=e.offsetTop),isNaN(e.offsetLeft)||(n+=e.offsetLeft),e=e.offsetParent;while(e);return{top:t,left:n,height:i,width:o}}function q(e){function t(){var t=c+a*s,n=f+l*s,i=d-a*s,y=u-l*s,m=r.y+e.config.viewOffset.top,p=r.x+e.config.viewOffset.left,g=r.y-e.config.viewOffset.bottom+o.height,w=r.x-e.config.viewOffset.right+o.width;return t<g&&i>m&&n>p&&y<w}function n(){return"fixed"===window.getComputedStyle(e.domEl).position}var i=x(e.domEl),o=b(e.config.container),r=h(e.config.container),s=e.config.viewFactor,a=i.height,l=i.width,c=i.top,f=i.left,d=c+a,u=f+l;return t()||n()}function E(){}var O,T;e.prototype.defaults={origin:"bottom",distance:"20px",duration:500,delay:0,rotate:{x:0,y:0,z:0},opacity:0,scale:.9,easing:"cubic-bezier(0.6, 0.2, 0.1, 1)",container:window.document.documentElement,mobile:!0,reset:!1,useDelay:"always",viewFactor:.2,viewOffset:{top:0,right:0,bottom:0,left:0},beforeReveal:function(e){},afterReveal:function(e){},beforeReset:function(e){},afterReset:function(e){}},e.prototype.isSupported=function(){var e=document.documentElement.style;return"WebkitTransition"in e&&"WebkitTransform"in e||"transition"in e&&"transform"in e},e.prototype.reveal=function(e,s,a,d){var u,y,m,p,g,w;if(void 0!==s&&"number"==typeof s?(a=s,s={}):void 0!==s&&null!==s||(s={}),u=t(s),y=n(e,u),!y.length)return O;a&&"number"==typeof a&&(w=i(),g=O.sequences[w]={id:w,interval:a,elemIds:[],active:!1});for(var v=0;v<y.length;v++)p=y[v].getAttribute("data-sr-id"),p?m=O.store.elements[p]:(m={id:i(),domEl:y[v],seen:!1,revealing:!1},m.domEl.setAttribute("data-sr-id",m.id)),g&&(m.sequence={id:g.id,index:g.elemIds.length},g.elemIds.push(m.id)),o(m,s,u),r(m),l(m),O.tools.isMobile()&&!m.config.mobile||!O.isSupported()?(m.domEl.setAttribute("style",m.styles.inline),m.disabled=!0):m.revealing||m.domEl.setAttribute("style",m.styles.inline+m.styles.transform.initial);return!d&&O.isSupported()&&(c(e,s,a),O.initTimeout&&window.clearTimeout(O.initTimeout),O.initTimeout=window.setTimeout(f,0)),O},e.prototype.sync=function(){if(O.history.length&&O.isSupported()){for(var e=0;e<O.history.length;e++){var t=O.history[e];O.reveal(t.target,t.config,t.interval,!0)}f()}return O},E.prototype.isObject=function(e){return null!==e&&"object"==typeof e&&e.constructor===Object},E.prototype.isNode=function(e){return"object"==typeof window.Node?e instanceof window.Node:e&&"object"==typeof e&&"number"==typeof e.nodeType&&"string"==typeof e.nodeName},E.prototype.isNodeList=function(e){var t=Object.prototype.toString.call(e),n=/^\[object (HTMLCollection|NodeList|Object)\]$/;return"object"==typeof window.NodeList?e instanceof window.NodeList:e&&"object"==typeof e&&n.test(t)&&"number"==typeof e.length&&(0===e.length||this.isNode(e[0]))},E.prototype.forOwn=function(e,t){if(!this.isObject(e))throw new TypeError('Expected "object", but received "'+typeof e+'".');for(var n in e)e.hasOwnProperty(n)&&t(n)},E.prototype.extend=function(e,t){return this.forOwn(t,function(n){this.isObject(t[n])?(e[n]&&this.isObject(e[n])||(e[n]={}),this.extend(e[n],t[n])):e[n]=t[n]}.bind(this)),e},E.prototype.extendClone=function(e,t){return this.extend(this.extend({},e),t)},E.prototype.isMobile=function(){return/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)},T=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||function(e){window.setTimeout(e,1e3/60)},"function"==typeof define&&"object"==typeof define.amd&&define.amd?define(function(){return e}):"undefined"!=typeof module&&module.exports?module.exports=e:window.ScrollReveal=e}();

/*!
 * imagesLoaded PACKAGED v4.1.1
 * JavaScript is all like "You images are done yet or what?"
 * MIT License
 */

!function(t,e){"function"==typeof define&&define.amd?define("ev-emitter/ev-emitter",e):"object"==typeof module&&module.exports?module.exports=e():t.EvEmitter=e()}("undefined"!=typeof window?window:this,function(){function t(){}var e=t.prototype;return e.on=function(t,e){if(t&&e){var i=this._events=this._events||{},n=i[t]=i[t]||[];return-1==n.indexOf(e)&&n.push(e),this}},e.once=function(t,e){if(t&&e){this.on(t,e);var i=this._onceEvents=this._onceEvents||{},n=i[t]=i[t]||{};return n[e]=!0,this}},e.off=function(t,e){var i=this._events&&this._events[t];if(i&&i.length){var n=i.indexOf(e);return-1!=n&&i.splice(n,1),this}},e.emitEvent=function(t,e){var i=this._events&&this._events[t];if(i&&i.length){var n=0,o=i[n];e=e||[];for(var r=this._onceEvents&&this._onceEvents[t];o;){var s=r&&r[o];s&&(this.off(t,o),delete r[o]),o.apply(this,e),n+=s?0:1,o=i[n]}return this}},t}),function(t,e){"use strict";"function"==typeof define&&define.amd?define(["ev-emitter/ev-emitter"],function(i){return e(t,i)}):"object"==typeof module&&module.exports?module.exports=e(t,require("ev-emitter")):t.imagesLoaded=e(t,t.EvEmitter)}(window,function(t,e){function i(t,e){for(var i in e)t[i]=e[i];return t}function n(t){var e=[];if(Array.isArray(t))e=t;else if("number"==typeof t.length)for(var i=0;i<t.length;i++)e.push(t[i]);else e.push(t);return e}function o(t,e,r){return this instanceof o?("string"==typeof t&&(t=document.querySelectorAll(t)),this.elements=n(t),this.options=i({},this.options),"function"==typeof e?r=e:i(this.options,e),r&&this.on("always",r),this.getImages(),h&&(this.jqDeferred=new h.Deferred),void setTimeout(function(){this.check()}.bind(this))):new o(t,e,r)}function r(t){this.img=t}function s(t,e){this.url=t,this.element=e,this.img=new Image}var h=t.jQuery,a=t.console;o.prototype=Object.create(e.prototype),o.prototype.options={},o.prototype.getImages=function(){this.images=[],this.elements.forEach(this.addElementImages,this)},o.prototype.addElementImages=function(t){"IMG"==t.nodeName&&this.addImage(t),this.options.background===!0&&this.addElementBackgroundImages(t);var e=t.nodeType;if(e&&d[e]){for(var i=t.querySelectorAll("img"),n=0;n<i.length;n++){var o=i[n];this.addImage(o)}if("string"==typeof this.options.background){var r=t.querySelectorAll(this.options.background);for(n=0;n<r.length;n++){var s=r[n];this.addElementBackgroundImages(s)}}}};var d={1:!0,9:!0,11:!0};return o.prototype.addElementBackgroundImages=function(t){var e=getComputedStyle(t);if(e)for(var i=/url\((['"])?(.*?)\1\)/gi,n=i.exec(e.backgroundImage);null!==n;){var o=n&&n[2];o&&this.addBackground(o,t),n=i.exec(e.backgroundImage)}},o.prototype.addImage=function(t){var e=new r(t);this.images.push(e)},o.prototype.addBackground=function(t,e){var i=new s(t,e);this.images.push(i)},o.prototype.check=function(){function t(t,i,n){setTimeout(function(){e.progress(t,i,n)})}var e=this;return this.progressedCount=0,this.hasAnyBroken=!1,this.images.length?void this.images.forEach(function(e){e.once("progress",t),e.check()}):void this.complete()},o.prototype.progress=function(t,e,i){this.progressedCount++,this.hasAnyBroken=this.hasAnyBroken||!t.isLoaded,this.emitEvent("progress",[this,t,e]),this.jqDeferred&&this.jqDeferred.notify&&this.jqDeferred.notify(this,t),this.progressedCount==this.images.length&&this.complete(),this.options.debug&&a&&a.log("progress: "+i,t,e)},o.prototype.complete=function(){var t=this.hasAnyBroken?"fail":"done";if(this.isComplete=!0,this.emitEvent(t,[this]),this.emitEvent("always",[this]),this.jqDeferred){var e=this.hasAnyBroken?"reject":"resolve";this.jqDeferred[e](this)}},r.prototype=Object.create(e.prototype),r.prototype.check=function(){var t=this.getIsImageComplete();return t?void this.confirm(0!==this.img.naturalWidth,"naturalWidth"):(this.proxyImage=new Image,this.proxyImage.addEventListener("load",this),this.proxyImage.addEventListener("error",this),this.img.addEventListener("load",this),this.img.addEventListener("error",this),void(this.proxyImage.src=this.img.src))},r.prototype.getIsImageComplete=function(){return this.img.complete&&void 0!==this.img.naturalWidth},r.prototype.confirm=function(t,e){this.isLoaded=t,this.emitEvent("progress",[this,this.img,e])},r.prototype.handleEvent=function(t){var e="on"+t.type;this[e]&&this[e](t)},r.prototype.onload=function(){this.confirm(!0,"onload"),this.unbindEvents()},r.prototype.onerror=function(){this.confirm(!1,"onerror"),this.unbindEvents()},r.prototype.unbindEvents=function(){this.proxyImage.removeEventListener("load",this),this.proxyImage.removeEventListener("error",this),this.img.removeEventListener("load",this),this.img.removeEventListener("error",this)},s.prototype=Object.create(r.prototype),s.prototype.check=function(){this.img.addEventListener("load",this),this.img.addEventListener("error",this),this.img.src=this.url;var t=this.getIsImageComplete();t&&(this.confirm(0!==this.img.naturalWidth,"naturalWidth"),this.unbindEvents())},s.prototype.unbindEvents=function(){this.img.removeEventListener("load",this),this.img.removeEventListener("error",this)},s.prototype.confirm=function(t,e){this.isLoaded=t,this.emitEvent("progress",[this,this.element,e])},o.makeJQueryPlugin=function(e){e=e||t.jQuery,e&&(h=e,h.fn.imagesLoaded=function(t,e){var i=new o(this,t,e);return i.jqDeferred.promise(h(this))})},o.makeJQueryPlugin(),o});

/* -----------------------------------------------
/* Author : Vincent Garreau  - vincentgarreau.com
/* MIT license: http://opensource.org/licenses/MIT
/* Demo / Generator : vincentgarreau.com/particles.js
/* GitHub : github.com/VincentGarreau/particles.js
/* How to use? : Check the GitHub README
/* v2.0.0
/* ----------------------------------------------- */
function hexToRgb(e){var a=/^#?([a-f\d])([a-f\d])([a-f\d])$/i;e=e.replace(a,function(e,a,t,i){return a+a+t+t+i+i});var t=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(e);return t?{r:parseInt(t[1],16),g:parseInt(t[2],16),b:parseInt(t[3],16)}:null}function clamp(e,a,t){return Math.min(Math.max(e,a),t)}function isInArray(e,a){return a.indexOf(e)>-1}var pJS=function(e,a){var t=document.querySelector("#"+e+" > .particles-js-canvas-el");this.pJS={canvas:{el:t,w:t.offsetWidth,h:t.offsetHeight},particles:{number:{value:400,density:{enable:!0,value_area:800}},color:{value:"#fff"},shape:{type:"circle",stroke:{width:0,color:"#ff0000"},polygon:{nb_sides:5},image:{src:"",width:100,height:100}},opacity:{value:1,random:!1,anim:{enable:!1,speed:2,opacity_min:0,sync:!1}},size:{value:20,random:!1,anim:{enable:!1,speed:20,size_min:0,sync:!1}},line_linked:{enable:!0,distance:100,color:"#fff",opacity:1,width:1},move:{enable:!0,speed:2,direction:"none",random:!1,straight:!1,out_mode:"out",bounce:!1,attract:{enable:!1,rotateX:3e3,rotateY:3e3}},array:[]},interactivity:{detect_on:"canvas",events:{onhover:{enable:!0,mode:"grab"},onclick:{enable:!0,mode:"push"},resize:!0},modes:{grab:{distance:100,line_linked:{opacity:1}},bubble:{distance:200,size:80,duration:.4},repulse:{distance:200,duration:.4},push:{particles_nb:4},remove:{particles_nb:2}},mouse:{}},retina_detect:!1,fn:{interact:{},modes:{},vendors:{}},tmp:{}};var i=this.pJS;a&&Object.deepExtend(i,a),i.tmp.obj={size_value:i.particles.size.value,size_anim_speed:i.particles.size.anim.speed,move_speed:i.particles.move.speed,line_linked_distance:i.particles.line_linked.distance,line_linked_width:i.particles.line_linked.width,mode_grab_distance:i.interactivity.modes.grab.distance,mode_bubble_distance:i.interactivity.modes.bubble.distance,mode_bubble_size:i.interactivity.modes.bubble.size,mode_repulse_distance:i.interactivity.modes.repulse.distance},i.fn.retinaInit=function(){i.retina_detect&&window.devicePixelRatio>1?(i.canvas.pxratio=window.devicePixelRatio,i.tmp.retina=!0):(i.canvas.pxratio=1,i.tmp.retina=!1),i.canvas.w=i.canvas.el.offsetWidth*i.canvas.pxratio,i.canvas.h=i.canvas.el.offsetHeight*i.canvas.pxratio,i.particles.size.value=i.tmp.obj.size_value*i.canvas.pxratio,i.particles.size.anim.speed=i.tmp.obj.size_anim_speed*i.canvas.pxratio,i.particles.move.speed=i.tmp.obj.move_speed*i.canvas.pxratio,i.particles.line_linked.distance=i.tmp.obj.line_linked_distance*i.canvas.pxratio,i.interactivity.modes.grab.distance=i.tmp.obj.mode_grab_distance*i.canvas.pxratio,i.interactivity.modes.bubble.distance=i.tmp.obj.mode_bubble_distance*i.canvas.pxratio,i.particles.line_linked.width=i.tmp.obj.line_linked_width*i.canvas.pxratio,i.interactivity.modes.bubble.size=i.tmp.obj.mode_bubble_size*i.canvas.pxratio,i.interactivity.modes.repulse.distance=i.tmp.obj.mode_repulse_distance*i.canvas.pxratio},i.fn.canvasInit=function(){i.canvas.ctx=i.canvas.el.getContext("2d")},i.fn.canvasSize=function(){i.canvas.el.width=i.canvas.w,i.canvas.el.height=i.canvas.h,i&&i.interactivity.events.resize&&window.addEventListener("resize",function(){i.canvas.w=i.canvas.el.offsetWidth,i.canvas.h=i.canvas.el.offsetHeight,i.tmp.retina&&(i.canvas.w*=i.canvas.pxratio,i.canvas.h*=i.canvas.pxratio),i.canvas.el.width=i.canvas.w,i.canvas.el.height=i.canvas.h,i.particles.move.enable||(i.fn.particlesEmpty(),i.fn.particlesCreate(),i.fn.particlesDraw(),i.fn.vendors.densityAutoParticles()),i.fn.vendors.densityAutoParticles()})},i.fn.canvasPaint=function(){i.canvas.ctx.fillRect(0,0,i.canvas.w,i.canvas.h)},i.fn.canvasClear=function(){i.canvas.ctx.clearRect(0,0,i.canvas.w,i.canvas.h)},i.fn.particle=function(e,a,t){if(this.radius=(i.particles.size.random?Math.random():1)*i.particles.size.value,i.particles.size.anim.enable&&(this.size_status=!1,this.vs=i.particles.size.anim.speed/100,i.particles.size.anim.sync||(this.vs=this.vs*Math.random())),this.x=t?t.x:Math.random()*i.canvas.w,this.y=t?t.y:Math.random()*i.canvas.h,this.x>i.canvas.w-2*this.radius?this.x=this.x-this.radius:this.x<2*this.radius&&(this.x=this.x+this.radius),this.y>i.canvas.h-2*this.radius?this.y=this.y-this.radius:this.y<2*this.radius&&(this.y=this.y+this.radius),i.particles.move.bounce&&i.fn.vendors.checkOverlap(this,t),this.color={},"object"==typeof e.value)if(e.value instanceof Array){var s=e.value[Math.floor(Math.random()*i.particles.color.value.length)];this.color.rgb=hexToRgb(s)}else void 0!=e.value.r&&void 0!=e.value.g&&void 0!=e.value.b&&(this.color.rgb={r:e.value.r,g:e.value.g,b:e.value.b}),void 0!=e.value.h&&void 0!=e.value.s&&void 0!=e.value.l&&(this.color.hsl={h:e.value.h,s:e.value.s,l:e.value.l});else"random"==e.value?this.color.rgb={r:Math.floor(256*Math.random())+0,g:Math.floor(256*Math.random())+0,b:Math.floor(256*Math.random())+0}:"string"==typeof e.value&&(this.color=e,this.color.rgb=hexToRgb(this.color.value));this.opacity=(i.particles.opacity.random?Math.random():1)*i.particles.opacity.value,i.particles.opacity.anim.enable&&(this.opacity_status=!1,this.vo=i.particles.opacity.anim.speed/100,i.particles.opacity.anim.sync||(this.vo=this.vo*Math.random()));var n={};switch(i.particles.move.direction){case"top":n={x:0,y:-1};break;case"top-right":n={x:.5,y:-.5};break;case"right":n={x:1,y:-0};break;case"bottom-right":n={x:.5,y:.5};break;case"bottom":n={x:0,y:1};break;case"bottom-left":n={x:-.5,y:1};break;case"left":n={x:-1,y:0};break;case"top-left":n={x:-.5,y:-.5};break;default:n={x:0,y:0}}i.particles.move.straight?(this.vx=n.x,this.vy=n.y,i.particles.move.random&&(this.vx=this.vx*Math.random(),this.vy=this.vy*Math.random())):(this.vx=n.x+Math.random()-.5,this.vy=n.y+Math.random()-.5),this.vx_i=this.vx,this.vy_i=this.vy;var r=i.particles.shape.type;if("object"==typeof r){if(r instanceof Array){var c=r[Math.floor(Math.random()*r.length)];this.shape=c}}else this.shape=r;if("image"==this.shape){var o=i.particles.shape;this.img={src:o.image.src,ratio:o.image.width/o.image.height},this.img.ratio||(this.img.ratio=1),"svg"==i.tmp.img_type&&void 0!=i.tmp.source_svg&&(i.fn.vendors.createSvgImg(this),i.tmp.pushing&&(this.img.loaded=!1))}},i.fn.particle.prototype.draw=function(){function e(){i.canvas.ctx.drawImage(r,a.x-t,a.y-t,2*t,2*t/a.img.ratio)}var a=this;if(void 0!=a.radius_bubble)var t=a.radius_bubble;else var t=a.radius;if(void 0!=a.opacity_bubble)var s=a.opacity_bubble;else var s=a.opacity;if(a.color.rgb)var n="rgba("+a.color.rgb.r+","+a.color.rgb.g+","+a.color.rgb.b+","+s+")";else var n="hsla("+a.color.hsl.h+","+a.color.hsl.s+"%,"+a.color.hsl.l+"%,"+s+")";switch(i.canvas.ctx.fillStyle=n,i.canvas.ctx.beginPath(),a.shape){case"circle":i.canvas.ctx.arc(a.x,a.y,t,0,2*Math.PI,!1);break;case"edge":i.canvas.ctx.rect(a.x-t,a.y-t,2*t,2*t);break;case"triangle":i.fn.vendors.drawShape(i.canvas.ctx,a.x-t,a.y+t/1.66,2*t,3,2);break;case"polygon":i.fn.vendors.drawShape(i.canvas.ctx,a.x-t/(i.particles.shape.polygon.nb_sides/3.5),a.y-t/.76,2.66*t/(i.particles.shape.polygon.nb_sides/3),i.particles.shape.polygon.nb_sides,1);break;case"star":i.fn.vendors.drawShape(i.canvas.ctx,a.x-2*t/(i.particles.shape.polygon.nb_sides/4),a.y-t/1.52,2*t*2.66/(i.particles.shape.polygon.nb_sides/3),i.particles.shape.polygon.nb_sides,2);break;case"image":if("svg"==i.tmp.img_type)var r=a.img.obj;else var r=i.tmp.img_obj;r&&e()}i.canvas.ctx.closePath(),i.particles.shape.stroke.width>0&&(i.canvas.ctx.strokeStyle=i.particles.shape.stroke.color,i.canvas.ctx.lineWidth=i.particles.shape.stroke.width,i.canvas.ctx.stroke()),i.canvas.ctx.fill()},i.fn.particlesCreate=function(){for(var e=0;e<i.particles.number.value;e++)i.particles.array.push(new i.fn.particle(i.particles.color,i.particles.opacity.value))},i.fn.particlesUpdate=function(){for(var e=0;e<i.particles.array.length;e++){var a=i.particles.array[e];if(i.particles.move.enable){var t=i.particles.move.speed/2;a.x+=a.vx*t,a.y+=a.vy*t}if(i.particles.opacity.anim.enable&&(1==a.opacity_status?(a.opacity>=i.particles.opacity.value&&(a.opacity_status=!1),a.opacity+=a.vo):(a.opacity<=i.particles.opacity.anim.opacity_min&&(a.opacity_status=!0),a.opacity-=a.vo),a.opacity<0&&(a.opacity=0)),i.particles.size.anim.enable&&(1==a.size_status?(a.radius>=i.particles.size.value&&(a.size_status=!1),a.radius+=a.vs):(a.radius<=i.particles.size.anim.size_min&&(a.size_status=!0),a.radius-=a.vs),a.radius<0&&(a.radius=0)),"bounce"==i.particles.move.out_mode)var s={x_left:a.radius,x_right:i.canvas.w,y_top:a.radius,y_bottom:i.canvas.h};else var s={x_left:-a.radius,x_right:i.canvas.w+a.radius,y_top:-a.radius,y_bottom:i.canvas.h+a.radius};switch(a.x-a.radius>i.canvas.w?(a.x=s.x_left,a.y=Math.random()*i.canvas.h):a.x+a.radius<0&&(a.x=s.x_right,a.y=Math.random()*i.canvas.h),a.y-a.radius>i.canvas.h?(a.y=s.y_top,a.x=Math.random()*i.canvas.w):a.y+a.radius<0&&(a.y=s.y_bottom,a.x=Math.random()*i.canvas.w),i.particles.move.out_mode){case"bounce":a.x+a.radius>i.canvas.w?a.vx=-a.vx:a.x-a.radius<0&&(a.vx=-a.vx),a.y+a.radius>i.canvas.h?a.vy=-a.vy:a.y-a.radius<0&&(a.vy=-a.vy)}if(isInArray("grab",i.interactivity.events.onhover.mode)&&i.fn.modes.grabParticle(a),(isInArray("bubble",i.interactivity.events.onhover.mode)||isInArray("bubble",i.interactivity.events.onclick.mode))&&i.fn.modes.bubbleParticle(a),(isInArray("repulse",i.interactivity.events.onhover.mode)||isInArray("repulse",i.interactivity.events.onclick.mode))&&i.fn.modes.repulseParticle(a),i.particles.line_linked.enable||i.particles.move.attract.enable)for(var n=e+1;n<i.particles.array.length;n++){var r=i.particles.array[n];i.particles.line_linked.enable&&i.fn.interact.linkParticles(a,r),i.particles.move.attract.enable&&i.fn.interact.attractParticles(a,r),i.particles.move.bounce&&i.fn.interact.bounceParticles(a,r)}}},i.fn.particlesDraw=function(){i.canvas.ctx.clearRect(0,0,i.canvas.w,i.canvas.h),i.fn.particlesUpdate();for(var e=0;e<i.particles.array.length;e++){var a=i.particles.array[e];a.draw()}},i.fn.particlesEmpty=function(){i.particles.array=[]},i.fn.particlesRefresh=function(){cancelRequestAnimFrame(i.fn.checkAnimFrame),cancelRequestAnimFrame(i.fn.drawAnimFrame),i.tmp.source_svg=void 0,i.tmp.img_obj=void 0,i.tmp.count_svg=0,i.fn.particlesEmpty(),i.fn.canvasClear(),i.fn.vendors.start()},i.fn.interact.linkParticles=function(e,a){var t=e.x-a.x,s=e.y-a.y,n=Math.sqrt(t*t+s*s);if(n<=i.particles.line_linked.distance){var r=i.particles.line_linked.opacity-n/(1/i.particles.line_linked.opacity)/i.particles.line_linked.distance;if(r>0){var c=i.particles.line_linked.color_rgb_line;i.canvas.ctx.strokeStyle="rgba("+c.r+","+c.g+","+c.b+","+r+")",i.canvas.ctx.lineWidth=i.particles.line_linked.width,i.canvas.ctx.beginPath(),i.canvas.ctx.moveTo(e.x,e.y),i.canvas.ctx.lineTo(a.x,a.y),i.canvas.ctx.stroke(),i.canvas.ctx.closePath()}}},i.fn.interact.attractParticles=function(e,a){var t=e.x-a.x,s=e.y-a.y,n=Math.sqrt(t*t+s*s);if(n<=i.particles.line_linked.distance){var r=t/(1e3*i.particles.move.attract.rotateX),c=s/(1e3*i.particles.move.attract.rotateY);e.vx-=r,e.vy-=c,a.vx+=r,a.vy+=c}},i.fn.interact.bounceParticles=function(e,a){var t=e.x-a.x,i=e.y-a.y,s=Math.sqrt(t*t+i*i),n=e.radius+a.radius;n>=s&&(e.vx=-e.vx,e.vy=-e.vy,a.vx=-a.vx,a.vy=-a.vy)},i.fn.modes.pushParticles=function(e,a){i.tmp.pushing=!0;for(var t=0;e>t;t++)i.particles.array.push(new i.fn.particle(i.particles.color,i.particles.opacity.value,{x:a?a.pos_x:Math.random()*i.canvas.w,y:a?a.pos_y:Math.random()*i.canvas.h})),t==e-1&&(i.particles.move.enable||i.fn.particlesDraw(),i.tmp.pushing=!1)},i.fn.modes.removeParticles=function(e){i.particles.array.splice(0,e),i.particles.move.enable||i.fn.particlesDraw()},i.fn.modes.bubbleParticle=function(e){function a(){e.opacity_bubble=e.opacity,e.radius_bubble=e.radius}function t(a,t,s,n,c){if(a!=t)if(i.tmp.bubble_duration_end){if(void 0!=s){var o=n-p*(n-a)/i.interactivity.modes.bubble.duration,l=a-o;d=a+l,"size"==c&&(e.radius_bubble=d),"opacity"==c&&(e.opacity_bubble=d)}}else if(r<=i.interactivity.modes.bubble.distance){if(void 0!=s)var v=s;else var v=n;if(v!=a){var d=n-p*(n-a)/i.interactivity.modes.bubble.duration;"size"==c&&(e.radius_bubble=d),"opacity"==c&&(e.opacity_bubble=d)}}else"size"==c&&(e.radius_bubble=void 0),"opacity"==c&&(e.opacity_bubble=void 0)}if(i.interactivity.events.onhover.enable&&isInArray("bubble",i.interactivity.events.onhover.mode)){var s=e.x-i.interactivity.mouse.pos_x,n=e.y-i.interactivity.mouse.pos_y,r=Math.sqrt(s*s+n*n),c=1-r/i.interactivity.modes.bubble.distance;if(r<=i.interactivity.modes.bubble.distance){if(c>=0&&"mousemove"==i.interactivity.status){if(i.interactivity.modes.bubble.size!=i.particles.size.value)if(i.interactivity.modes.bubble.size>i.particles.size.value){var o=e.radius+i.interactivity.modes.bubble.size*c;o>=0&&(e.radius_bubble=o)}else{var l=e.radius-i.interactivity.modes.bubble.size,o=e.radius-l*c;o>0?e.radius_bubble=o:e.radius_bubble=0}if(i.interactivity.modes.bubble.opacity!=i.particles.opacity.value)if(i.interactivity.modes.bubble.opacity>i.particles.opacity.value){var v=i.interactivity.modes.bubble.opacity*c;v>e.opacity&&v<=i.interactivity.modes.bubble.opacity&&(e.opacity_bubble=v)}else{var v=e.opacity-(i.particles.opacity.value-i.interactivity.modes.bubble.opacity)*c;v<e.opacity&&v>=i.interactivity.modes.bubble.opacity&&(e.opacity_bubble=v)}}}else a();"mouseleave"==i.interactivity.status&&a()}else if(i.interactivity.events.onclick.enable&&isInArray("bubble",i.interactivity.events.onclick.mode)){if(i.tmp.bubble_clicking){var s=e.x-i.interactivity.mouse.click_pos_x,n=e.y-i.interactivity.mouse.click_pos_y,r=Math.sqrt(s*s+n*n),p=((new Date).getTime()-i.interactivity.mouse.click_time)/1e3;p>i.interactivity.modes.bubble.duration&&(i.tmp.bubble_duration_end=!0),p>2*i.interactivity.modes.bubble.duration&&(i.tmp.bubble_clicking=!1,i.tmp.bubble_duration_end=!1)}i.tmp.bubble_clicking&&(t(i.interactivity.modes.bubble.size,i.particles.size.value,e.radius_bubble,e.radius,"size"),t(i.interactivity.modes.bubble.opacity,i.particles.opacity.value,e.opacity_bubble,e.opacity,"opacity"))}},i.fn.modes.repulseParticle=function(e){function a(){var a=Math.atan2(d,p);if(e.vx=u*Math.cos(a),e.vy=u*Math.sin(a),"bounce"==i.particles.move.out_mode){var t={x:e.x+e.vx,y:e.y+e.vy};t.x+e.radius>i.canvas.w?e.vx=-e.vx:t.x-e.radius<0&&(e.vx=-e.vx),t.y+e.radius>i.canvas.h?e.vy=-e.vy:t.y-e.radius<0&&(e.vy=-e.vy)}}if(i.interactivity.events.onhover.enable&&isInArray("repulse",i.interactivity.events.onhover.mode)&&"mousemove"==i.interactivity.status){var t=e.x-i.interactivity.mouse.pos_x,s=e.y-i.interactivity.mouse.pos_y,n=Math.sqrt(t*t+s*s),r={x:t/n,y:s/n},c=i.interactivity.modes.repulse.distance,o=100,l=clamp(1/c*(-1*Math.pow(n/c,2)+1)*c*o,0,50),v={x:e.x+r.x*l,y:e.y+r.y*l};"bounce"==i.particles.move.out_mode?(v.x-e.radius>0&&v.x+e.radius<i.canvas.w&&(e.x=v.x),v.y-e.radius>0&&v.y+e.radius<i.canvas.h&&(e.y=v.y)):(e.x=v.x,e.y=v.y)}else if(i.interactivity.events.onclick.enable&&isInArray("repulse",i.interactivity.events.onclick.mode))if(i.tmp.repulse_finish||(i.tmp.repulse_count++,i.tmp.repulse_count==i.particles.array.length&&(i.tmp.repulse_finish=!0)),i.tmp.repulse_clicking){var c=Math.pow(i.interactivity.modes.repulse.distance/6,3),p=i.interactivity.mouse.click_pos_x-e.x,d=i.interactivity.mouse.click_pos_y-e.y,m=p*p+d*d,u=-c/m*1;c>=m&&a()}else 0==i.tmp.repulse_clicking&&(e.vx=e.vx_i,e.vy=e.vy_i)},i.fn.modes.grabParticle=function(e){if(i.interactivity.events.onhover.enable&&"mousemove"==i.interactivity.status){var a=e.x-i.interactivity.mouse.pos_x,t=e.y-i.interactivity.mouse.pos_y,s=Math.sqrt(a*a+t*t);if(s<=i.interactivity.modes.grab.distance){var n=i.interactivity.modes.grab.line_linked.opacity-s/(1/i.interactivity.modes.grab.line_linked.opacity)/i.interactivity.modes.grab.distance;if(n>0){var r=i.particles.line_linked.color_rgb_line;i.canvas.ctx.strokeStyle="rgba("+r.r+","+r.g+","+r.b+","+n+")",i.canvas.ctx.lineWidth=i.particles.line_linked.width,i.canvas.ctx.beginPath(),i.canvas.ctx.moveTo(e.x,e.y),i.canvas.ctx.lineTo(i.interactivity.mouse.pos_x,i.interactivity.mouse.pos_y),i.canvas.ctx.stroke(),i.canvas.ctx.closePath()}}}},i.fn.vendors.eventsListeners=function(){"window"==i.interactivity.detect_on?i.interactivity.el=window:i.interactivity.el=i.canvas.el,(i.interactivity.events.onhover.enable||i.interactivity.events.onclick.enable)&&(i.interactivity.el.addEventListener("mousemove",function(e){if(i.interactivity.el==window)var a=e.clientX,t=e.clientY;else var a=e.offsetX||e.clientX,t=e.offsetY||e.clientY;i.interactivity.mouse.pos_x=a,i.interactivity.mouse.pos_y=t,i.tmp.retina&&(i.interactivity.mouse.pos_x*=i.canvas.pxratio,i.interactivity.mouse.pos_y*=i.canvas.pxratio),i.interactivity.status="mousemove"}),i.interactivity.el.addEventListener("mouseleave",function(e){i.interactivity.mouse.pos_x=null,i.interactivity.mouse.pos_y=null,i.interactivity.status="mouseleave"})),i.interactivity.events.onclick.enable&&i.interactivity.el.addEventListener("click",function(){if(i.interactivity.mouse.click_pos_x=i.interactivity.mouse.pos_x,i.interactivity.mouse.click_pos_y=i.interactivity.mouse.pos_y,i.interactivity.mouse.click_time=(new Date).getTime(),i.interactivity.events.onclick.enable)switch(i.interactivity.events.onclick.mode){case"push":i.particles.move.enable?i.fn.modes.pushParticles(i.interactivity.modes.push.particles_nb,i.interactivity.mouse):1==i.interactivity.modes.push.particles_nb?i.fn.modes.pushParticles(i.interactivity.modes.push.particles_nb,i.interactivity.mouse):i.interactivity.modes.push.particles_nb>1&&i.fn.modes.pushParticles(i.interactivity.modes.push.particles_nb);break;case"remove":i.fn.modes.removeParticles(i.interactivity.modes.remove.particles_nb);break;case"bubble":i.tmp.bubble_clicking=!0;break;case"repulse":i.tmp.repulse_clicking=!0,i.tmp.repulse_count=0,i.tmp.repulse_finish=!1,setTimeout(function(){i.tmp.repulse_clicking=!1},1e3*i.interactivity.modes.repulse.duration)}})},i.fn.vendors.densityAutoParticles=function(){if(i.particles.number.density.enable){var e=i.canvas.el.width*i.canvas.el.height/1e3;i.tmp.retina&&(e/=2*i.canvas.pxratio);var a=e*i.particles.number.value/i.particles.number.density.value_area,t=i.particles.array.length-a;0>t?i.fn.modes.pushParticles(Math.abs(t)):i.fn.modes.removeParticles(t)}},i.fn.vendors.checkOverlap=function(e,a){for(var t=0;t<i.particles.array.length;t++){var s=i.particles.array[t],n=e.x-s.x,r=e.y-s.y,c=Math.sqrt(n*n+r*r);c<=e.radius+s.radius&&(e.x=a?a.x:Math.random()*i.canvas.w,e.y=a?a.y:Math.random()*i.canvas.h,i.fn.vendors.checkOverlap(e))}},i.fn.vendors.createSvgImg=function(e){var a=i.tmp.source_svg,t=/#([0-9A-F]{3,6})/gi,s=a.replace(t,function(a,t,i,s){if(e.color.rgb)var n="rgba("+e.color.rgb.r+","+e.color.rgb.g+","+e.color.rgb.b+","+e.opacity+")";else var n="hsla("+e.color.hsl.h+","+e.color.hsl.s+"%,"+e.color.hsl.l+"%,"+e.opacity+")";return n}),n=new Blob([s],{type:"image/svg+xml;charset=utf-8"}),r=window.URL||window.webkitURL||window,c=r.createObjectURL(n),o=new Image;o.addEventListener("load",function(){e.img.obj=o,e.img.loaded=!0,r.revokeObjectURL(c),i.tmp.count_svg++}),o.src=c},i.fn.vendors.destroypJS=function(){cancelAnimationFrame(i.fn.drawAnimFrame),t.remove(),pJSDom=null},i.fn.vendors.drawShape=function(e,a,t,i,s,n){var r=s*n,c=s/n,o=180*(c-2)/c,l=Math.PI-Math.PI*o/180;e.save(),e.beginPath(),e.translate(a,t),e.moveTo(0,0);for(var v=0;r>v;v++)e.lineTo(i,0),e.translate(i,0),e.rotate(l);e.fill(),e.restore()},i.fn.vendors.exportImg=function(){window.open(i.canvas.el.toDataURL("image/png"),"_blank")},i.fn.vendors.loadImg=function(e){if(i.tmp.img_error=void 0,""!=i.particles.shape.image.src)if("svg"==e){var a=new XMLHttpRequest;a.open("GET",i.particles.shape.image.src),a.onreadystatechange=function(e){4==a.readyState&&(200==a.status?(i.tmp.source_svg=e.currentTarget.response,i.fn.vendors.checkBeforeDraw()):(console.log("Error pJS - Image not found"),i.tmp.img_error=!0))},a.send()}else{var t=new Image;t.addEventListener("load",function(){i.tmp.img_obj=t,i.fn.vendors.checkBeforeDraw()}),t.src=i.particles.shape.image.src}else console.log("Error pJS - No image.src"),i.tmp.img_error=!0},i.fn.vendors.draw=function(){"image"==i.particles.shape.type?"svg"==i.tmp.img_type?i.tmp.count_svg>=i.particles.number.value?(i.fn.particlesDraw(),i.particles.move.enable?i.fn.drawAnimFrame=requestAnimFrame(i.fn.vendors.draw):cancelRequestAnimFrame(i.fn.drawAnimFrame)):i.tmp.img_error||(i.fn.drawAnimFrame=requestAnimFrame(i.fn.vendors.draw)):void 0!=i.tmp.img_obj?(i.fn.particlesDraw(),i.particles.move.enable?i.fn.drawAnimFrame=requestAnimFrame(i.fn.vendors.draw):cancelRequestAnimFrame(i.fn.drawAnimFrame)):i.tmp.img_error||(i.fn.drawAnimFrame=requestAnimFrame(i.fn.vendors.draw)):(i.fn.particlesDraw(),i.particles.move.enable?i.fn.drawAnimFrame=requestAnimFrame(i.fn.vendors.draw):cancelRequestAnimFrame(i.fn.drawAnimFrame))},i.fn.vendors.checkBeforeDraw=function(){"image"==i.particles.shape.type?"svg"==i.tmp.img_type&&void 0==i.tmp.source_svg?i.tmp.checkAnimFrame=requestAnimFrame(check):(cancelRequestAnimFrame(i.tmp.checkAnimFrame),i.tmp.img_error||(i.fn.vendors.init(),i.fn.vendors.draw())):(i.fn.vendors.init(),i.fn.vendors.draw())},i.fn.vendors.init=function(){i.fn.retinaInit(),i.fn.canvasInit(),i.fn.canvasSize(),i.fn.canvasPaint(),i.fn.particlesCreate(),i.fn.vendors.densityAutoParticles(),i.particles.line_linked.color_rgb_line=hexToRgb(i.particles.line_linked.color)},i.fn.vendors.start=function(){isInArray("image",i.particles.shape.type)?(i.tmp.img_type=i.particles.shape.image.src.substr(i.particles.shape.image.src.length-3),i.fn.vendors.loadImg(i.tmp.img_type)):i.fn.vendors.checkBeforeDraw()},i.fn.vendors.eventsListeners(),i.fn.vendors.start()};Object.deepExtend=function(e,a){for(var t in a)a[t]&&a[t].constructor&&a[t].constructor===Object?(e[t]=e[t]||{},arguments.callee(e[t],a[t])):e[t]=a[t];return e},window.requestAnimFrame=function(){return window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||window.oRequestAnimationFrame||window.msRequestAnimationFrame||function(e){window.setTimeout(e,1e3/60)}}(),window.cancelRequestAnimFrame=function(){return window.cancelAnimationFrame||window.webkitCancelRequestAnimationFrame||window.mozCancelRequestAnimationFrame||window.oCancelRequestAnimationFrame||window.msCancelRequestAnimationFrame||clearTimeout}(),window.pJSDom=[],window.particlesJS=function(e,a){"string"!=typeof e&&(a=e,e="particles-js"),e||(e="particles-js");var t=document.getElementById(e),i="particles-js-canvas-el",s=t.getElementsByClassName(i);if(s.length)for(;s.length>0;)t.removeChild(s[0]);var n=document.createElement("canvas");n.className=i,n.style.width="100%",n.style.height="100%";var r=document.getElementById(e).appendChild(n);null!=r&&pJSDom.push(new pJS(e,a))},window.particlesJS.load=function(e,a,t){var i=new XMLHttpRequest;i.open("GET",a),i.onreadystatechange=function(a){if(4==i.readyState)if(200==i.status){var s=JSON.parse(a.currentTarget.response);window.particlesJS(e,s),t&&t()}else console.log("Error pJS - XMLHttpRequest status: "+i.status),console.log("Error pJS - File config not found")},i.send()};

/* particle */
$("#homeBgParticle").is(":visible")&&particlesJS("homeBgParticle",{particles:{number:{value:25,density:{enable:!0,value_area:500}},color:{value:"#ffffff"},opacity:{value:1,random:!1,anim:{enable:!1,speed:1,opacity_min:.1,sync:!1}},size:{value:4,random:!0,anim:{enable:!1,speed:40,size_min:.1,sync:!1}},line_linked:{enable:!0,distance:150,color:"#ffffff",opacity:1,width:1},move:{enable:!0,speed:3,direction:"top-right",random:!1,straight:!1,out_mode:"out",bounce:!1,attract:{enable:!1,rotateX:600,rotateY:1200}}},interactivity:{detect_on:"canvas",events:{onhover:{enable:!0,mode:"repulse"},onclick:{enable:!1,mode:"push"},resize:!0},modes:{grab:{distance:400,line_linked:{opacity:1}},bubble:{distance:400,size:40,duration:2,opacity:8,speed:3},repulse:{distance:200,duration:.4},push:{particles_nb:4},remove:{particles_nb:2}}},retina_detect:!0});

/* snow */
$("#homeBgSnow").is(":visible")&&particlesJS("homeBgSnow",{particles:{number:{value:100,density:{enable:!0,value_area:800}},color:{value:"#fff"},shape:{type:"circle",stroke:{width:0,color:"#000000"},polygon:{nb_sides:5}},opacity:{value:.5,random:!0,anim:{enable:!1,speed:1,opacity_min:.1,sync:!1}},size:{value:10,random:!0,anim:{enable:!1,speed:40,size_min:.1,sync:!1}},line_linked:{enable:!1,distance:500,color:"#ffffff",opacity:.4,width:2},move:{enable:!0,speed:3,direction:"bottom",random:!1,straight:!1,out_mode:"out",bounce:!1,attract:{enable:!1,rotateX:600,rotateY:1200}}},interactivity:{detect_on:"canvas",events:{onhover:{enable:!0,mode:"bubble"},onclick:{enable:!0,mode:"repulse"},resize:!0},modes:{grab:{distance:400,line_linked:{opacity:.5}},bubble:{distance:400,size:4,duration:.3,opacity:1,speed:3},repulse:{distance:200,duration:.4},push:{particles_nb:4},remove:{particles_nb:2}}},retina_detect:!0});


/*! jQuery Validation Plugin - v1.15.1 - 7/22/2016
 * http://jqueryvalidation.org/
 * Copyright (c) 2016 Jörn Zaefferer; Licensed MIT */
!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof module&&module.exports?module.exports=a(require("jquery")):a(jQuery)}(function(a){a.extend(a.fn,{validate:function(b){if(!this.length)return void(b&&b.debug&&window.console&&console.warn("Nothing selected, can't validate, returning nothing."));var c=a.data(this[0],"validator");return c?c:(this.attr("novalidate","novalidate"),c=new a.validator(b,this[0]),a.data(this[0],"validator",c),c.settings.onsubmit&&(this.on("click.validate",":submit",function(b){c.settings.submitHandler&&(c.submitButton=b.target),a(this).hasClass("cancel")&&(c.cancelSubmit=!0),void 0!==a(this).attr("formnovalidate")&&(c.cancelSubmit=!0)}),this.on("submit.validate",function(b){function d(){var d,e;return!c.settings.submitHandler||(c.submitButton&&(d=a("<input type='hidden'/>").attr("name",c.submitButton.name).val(a(c.submitButton).val()).appendTo(c.currentForm)),e=c.settings.submitHandler.call(c,c.currentForm,b),c.submitButton&&d.remove(),void 0!==e&&e)}return c.settings.debug&&b.preventDefault(),c.cancelSubmit?(c.cancelSubmit=!1,d()):c.form()?c.pendingRequest?(c.formSubmitted=!0,!1):d():(c.focusvalid(),!1)})),c)},valid:function(){var b,c,d;return a(this[0]).is("form")?b=this.validate().form():(d=[],b=!0,c=a(this[0].form).validate(),this.each(function(){b=c.element(this)&&b,b||(d=d.concat(c.errorList))}),c.errorList=d),b},rules:function(b,c){var d,e,f,g,h,i,j=this[0];if(null!=j&&null!=j.form){if(b)switch(d=a.data(j.form,"validator").settings,e=d.rules,f=a.validator.staticRules(j),b){case"add":a.extend(f,a.validator.normalizeRule(c)),delete f.messages,e[j.name]=f,c.messages&&(d.messages[j.name]=a.extend(d.messages[j.name],c.messages));break;case"remove":return c?(i={},a.each(c.split(/\s/),function(b,c){i[c]=f[c],delete f[c],"required"===c&&a(j).removeAttr("aria-required")}),i):(delete e[j.name],f)}return g=a.validator.normalizeRules(a.extend({},a.validator.classRules(j),a.validator.attributeRules(j),a.validator.dataRules(j),a.validator.staticRules(j)),j),g.required&&(h=g.required,delete g.required,g=a.extend({required:h},g),a(j).attr("aria-required","true")),g.remote&&(h=g.remote,delete g.remote,g=a.extend(g,{remote:h})),g}}}),a.extend(a.expr[":"],{blank:function(b){return!a.trim(""+a(b).val())},filled:function(b){var c=a(b).val();return null!==c&&!!a.trim(""+c)},unchecked:function(b){return!a(b).prop("checked")}}),a.validator=function(b,c){this.settings=a.extend(!0,{},a.validator.defaults,b),this.currentForm=c,this.init()},a.validator.format=function(b,c){return 1===arguments.length?function(){var c=a.makeArray(arguments);return c.unshift(b),a.validator.format.apply(this,c)}:void 0===c?b:(arguments.length>2&&c.constructor!==Array&&(c=a.makeArray(arguments).slice(1)),c.constructor!==Array&&(c=[c]),a.each(c,function(a,c){b=b.replace(new RegExp("\\{"+a+"\\}","g"),function(){return c})}),b)},a.extend(a.validator,{defaults:{messages:{},groups:{},rules:{},errorClass:"error",pendingClass:"pending",validClass:"valid",errorElement:"label",focusCleanup:!1,focusvalid:!0,errorContainer:a([]),errorLabelContainer:a([]),onsubmit:!0,ignore:":hidden",ignoreTitle:!1,onfocusin:function(a){this.lastActive=a,this.settings.focusCleanup&&(this.settings.unhighlight&&this.settings.unhighlight.call(this,a,this.settings.errorClass,this.settings.validClass),this.hideThese(this.errorsFor(a)))},onfocusout:function(a){this.checkable(a)||!(a.name in this.submitted)&&this.optional(a)||this.element(a)},onkeyup:function(b,c){var d=[16,17,18,20,35,36,37,38,39,40,45,144,225];9===c.which&&""===this.elementValue(b)||a.inArray(c.keyCode,d)!==-1||(b.name in this.submitted||b.name in this.valid)&&this.element(b)},onclick:function(a){a.name in this.submitted?this.element(a):a.parentNode.name in this.submitted&&this.element(a.parentNode)},highlight:function(b,c,d){"radio"===b.type?this.findByName(b.name).addClass(c).removeClass(d):a(b).addClass(c).removeClass(d)},unhighlight:function(b,c,d){"radio"===b.type?this.findByName(b.name).removeClass(c).addClass(d):a(b).removeClass(c).addClass(d)}},setDefaults:function(b){a.extend(a.validator.defaults,b)},messages:{required:"This field is required.",remote:"Please fix this field.",email:"Please enter a valid email address.",url:"Please enter a valid URL.",date:"Please enter a valid date.",dateISO:"Please enter a valid date (ISO).",number:"Please enter a valid number.",digits:"Please enter only digits.",equalTo:"Please enter the same value again.",maxlength:a.validator.format("Please enter no more than {0} characters."),minlength:a.validator.format("Please enter at least {0} characters."),rangelength:a.validator.format("Please enter a value between {0} and {1} characters long."),range:a.validator.format("Please enter a value between {0} and {1}."),max:a.validator.format("Please enter a value less than or equal to {0}."),min:a.validator.format("Please enter a value greater than or equal to {0}."),step:a.validator.format("Please enter a multiple of {0}.")},autoCreateRanges:!1,prototype:{init:function(){function b(b){!this.form&&this.hasAttribute("contenteditable")&&(this.form=a(this).closest("form")[0]);var c=a.data(this.form,"validator"),d="on"+b.type.replace(/^validate/,""),e=c.settings;e[d]&&!a(this).is(e.ignore)&&e[d].call(c,this,b)}this.labelContainer=a(this.settings.errorLabelContainer),this.errorContext=this.labelContainer.length&&this.labelContainer||a(this.currentForm),this.containers=a(this.settings.errorContainer).add(this.settings.errorLabelContainer),this.submitted={},this.valueCache={},this.pendingRequest=0,this.pending={},this.valid={},this.reset();var c,d=this.groups={};a.each(this.settings.groups,function(b,c){"string"==typeof c&&(c=c.split(/\s/)),a.each(c,function(a,c){d[c]=b})}),c=this.settings.rules,a.each(c,function(b,d){c[b]=a.validator.normalizeRule(d)}),a(this.currentForm).on("focusin.validate focusout.validate keyup.validate",":text, [type='password'], [type='file'], select, textarea, [type='number'], [type='search'], [type='tel'], [type='url'], [type='email'], [type='datetime'], [type='date'], [type='month'], [type='week'], [type='time'], [type='datetime-local'], [type='range'], [type='color'], [type='radio'], [type='checkbox'], [contenteditable]",b).on("click.validate","select, option, [type='radio'], [type='checkbox']",b),this.settings.validHandler&&a(this.currentForm).on("valid-form.validate",this.settings.validHandler),a(this.currentForm).find("[required], [data-rule-required], .required").attr("aria-required","true")},form:function(){return this.checkForm(),a.extend(this.submitted,this.errorMap),this.valid=a.extend({},this.errorMap),this.valid()||a(this.currentForm).triggerHandler("valid-form",[this]),this.showErrors(),this.valid()},checkForm:function(){this.prepareForm();for(var a=0,b=this.currentElements=this.elements();b[a];a++)this.check(b[a]);return this.valid()},element:function(b){var c,d,e=this.clean(b),f=this.validationTargetFor(e),g=this,h=!0;return void 0===f?delete this.valid[e.name]:(this.prepareElement(f),this.currentElements=a(f),d=this.groups[f.name],d&&a.each(this.groups,function(a,b){b===d&&a!==f.name&&(e=g.validationTargetFor(g.clean(g.findByName(a))),e&&e.name in g.valid&&(g.currentElements.push(e),h=g.check(e)&&h))}),c=this.check(f)!==!1,h=h&&c,c?this.valid[f.name]=!1:this.valid[f.name]=!0,this.numberOfvalids()||(this.toHide=this.toHide.add(this.containers)),this.showErrors(),a(b).attr("aria-valid",!c)),h},showErrors:function(b){if(b){var c=this;a.extend(this.errorMap,b),this.errorList=a.map(this.errorMap,function(a,b){return{message:a,element:c.findByName(b)[0]}}),this.successList=a.grep(this.successList,function(a){return!(a.name in b)})}this.settings.showErrors?this.settings.showErrors.call(this,this.errorMap,this.errorList):this.defaultShowErrors()},resetForm:function(){a.fn.resetForm&&a(this.currentForm).resetForm(),this.valid={},this.submitted={},this.prepareForm(),this.hideErrors();var b=this.elements().removeData("previousValue").removeAttr("aria-valid");this.resetElements(b)},resetElements:function(a){var b;if(this.settings.unhighlight)for(b=0;a[b];b++)this.settings.unhighlight.call(this,a[b],this.settings.errorClass,""),this.findByName(a[b].name).removeClass(this.settings.validClass);else a.removeClass(this.settings.errorClass).removeClass(this.settings.validClass)},numberOfvalids:function(){return this.objectLength(this.valid)},objectLength:function(a){var b,c=0;for(b in a)a[b]&&c++;return c},hideErrors:function(){this.hideThese(this.toHide)},hideThese:function(a){a.not(this.containers).text(""),this.addWrapper(a).hide()},valid:function(){return 0===this.size()},size:function(){return this.errorList.length},focusvalid:function(){if(this.settings.focusvalid)try{a(this.findLastActive()||this.errorList.length&&this.errorList[0].element||[]).filter(":visible").focus().trigger("focusin")}catch(a){}},findLastActive:function(){var b=this.lastActive;return b&&1===a.grep(this.errorList,function(a){return a.element.name===b.name}).length&&b},elements:function(){var b=this,c={};return a(this.currentForm).find("input, select, textarea, [contenteditable]").not(":submit, :reset, :image, :disabled").not(this.settings.ignore).filter(function(){var d=this.name||a(this).attr("name");return!d&&b.settings.debug&&window.console&&console.error("%o has no name assigned",this),this.hasAttribute("contenteditable")&&(this.form=a(this).closest("form")[0]),!(d in c||!b.objectLength(a(this).rules()))&&(c[d]=!0,!0)})},clean:function(b){return a(b)[0]},errors:function(){var b=this.settings.errorClass.split(" ").join(".");return a(this.settings.errorElement+"."+b,this.errorContext)},resetInternals:function(){this.successList=[],this.errorList=[],this.errorMap={},this.toShow=a([]),this.toHide=a([])},reset:function(){this.resetInternals(),this.currentElements=a([])},prepareForm:function(){this.reset(),this.toHide=this.errors().add(this.containers)},prepareElement:function(a){this.reset(),this.toHide=this.errorsFor(a)},elementValue:function(b){var c,d,e=a(b),f=b.type;return"radio"===f||"checkbox"===f?this.findByName(b.name).filter(":checked").val():"number"===f&&"undefined"!=typeof b.validity?b.validity.badInput?"NaN":e.val():(c=b.hasAttribute("contenteditable")?e.text():e.val(),"file"===f?"C:\\fakepath\\"===c.substr(0,12)?c.substr(12):(d=c.lastIndexOf("/"),d>=0?c.substr(d+1):(d=c.lastIndexOf("\\"),d>=0?c.substr(d+1):c)):"string"==typeof c?c.replace(/\r/g,""):c)},check:function(b){b=this.validationTargetFor(this.clean(b));var c,d,e,f=a(b).rules(),g=a.map(f,function(a,b){return b}).length,h=!1,i=this.elementValue(b);if("function"==typeof f.normalizer){if(i=f.normalizer.call(b,i),"string"!=typeof i)throw new TypeError("The normalizer should return a string value.");delete f.normalizer}for(d in f){e={method:d,parameters:f[d]};try{if(c=a.validator.methods[d].call(this,i,b,e.parameters),"dependency-mismatch"===c&&1===g){h=!0;continue}if(h=!1,"pending"===c)return void(this.toHide=this.toHide.not(this.errorsFor(b)));if(!c)return this.formatAndAdd(b,e),!1}catch(a){throw this.settings.debug&&window.console&&console.log("Exception occurred when checking element "+b.id+", check the '"+e.method+"' method.",a),a instanceof TypeError&&(a.message+=".  Exception occurred when checking element "+b.id+", check the '"+e.method+"' method."),a}}if(!h)return this.objectLength(f)&&this.successList.push(b),!0},customDataMessage:function(b,c){return a(b).data("msg"+c.charAt(0).toUpperCase()+c.substring(1).toLowerCase())||a(b).data("msg")},customMessage:function(a,b){var c=this.settings.messages[a];return c&&(c.constructor===String?c:c[b])},findDefined:function(){for(var a=0;a<arguments.length;a++)if(void 0!==arguments[a])return arguments[a]},defaultMessage:function(b,c){"string"==typeof c&&(c={method:c});var d=this.findDefined(this.customMessage(b.name,c.method),this.customDataMessage(b,c.method),!this.settings.ignoreTitle&&b.title||void 0,a.validator.messages[c.method],"<strong>Warning: No message defined for "+b.name+"</strong>"),e=/\$?\{(\d+)\}/g;return"function"==typeof d?d=d.call(this,c.parameters,b):e.test(d)&&(d=a.validator.format(d.replace(e,"{$1}"),c.parameters)),d},formatAndAdd:function(a,b){var c=this.defaultMessage(a,b);this.errorList.push({message:c,element:a,method:b.method}),this.errorMap[a.name]=c,this.submitted[a.name]=c},addWrapper:function(a){return this.settings.wrapper&&(a=a.add(a.parent(this.settings.wrapper))),a},defaultShowErrors:function(){var a,b,c;for(a=0;this.errorList[a];a++)c=this.errorList[a],this.settings.highlight&&this.settings.highlight.call(this,c.element,this.settings.errorClass,this.settings.validClass),this.showLabel(c.element,c.message);if(this.errorList.length&&(this.toShow=this.toShow.add(this.containers)),this.settings.success)for(a=0;this.successList[a];a++)this.showLabel(this.successList[a]);if(this.settings.unhighlight)for(a=0,b=this.validElements();b[a];a++)this.settings.unhighlight.call(this,b[a],this.settings.errorClass,this.settings.validClass);this.toHide=this.toHide.not(this.toShow),this.hideErrors(),this.addWrapper(this.toShow).show()},validElements:function(){return this.currentElements.not(this.validElements())},validElements:function(){return a(this.errorList).map(function(){return this.element})},showLabel:function(b,c){var d,e,f,g,h=this.errorsFor(b),i=this.idOrName(b),j=a(b).attr("aria-describedby");h.length?(h.removeClass(this.settings.validClass).addClass(this.settings.errorClass),h.html(c)):(h=a("<"+this.settings.errorElement+">").attr("id",i+"-error").addClass(this.settings.errorClass).html(c||""),d=h,this.settings.wrapper&&(d=h.hide().show().wrap("<"+this.settings.wrapper+"/>").parent()),this.labelContainer.length?this.labelContainer.append(d):this.settings.errorPlacement?this.settings.errorPlacement.call(this,d,a(b)):d.insertAfter(b),h.is("label")?h.attr("for",i):0===h.parents("label[for='"+this.escapeCssMeta(i)+"']").length&&(f=h.attr("id"),j?j.match(new RegExp("\\b"+this.escapeCssMeta(f)+"\\b"))||(j+=" "+f):j=f,a(b).attr("aria-describedby",j),e=this.groups[b.name],e&&(g=this,a.each(g.groups,function(b,c){c===e&&a("[name='"+g.escapeCssMeta(b)+"']",g.currentForm).attr("aria-describedby",h.attr("id"))})))),!c&&this.settings.success&&(h.text(""),"string"==typeof this.settings.success?h.addClass(this.settings.success):this.settings.success(h,b)),this.toShow=this.toShow.add(h)},errorsFor:function(b){var c=this.escapeCssMeta(this.idOrName(b)),d=a(b).attr("aria-describedby"),e="label[for='"+c+"'], label[for='"+c+"'] *";return d&&(e=e+", #"+this.escapeCssMeta(d).replace(/\s+/g,", #")),this.errors().filter(e)},escapeCssMeta:function(a){return a.replace(/([\\!"#$%&'()*+,./:;<=>?@\[\]^`{|}~])/g,"\\$1")},idOrName:function(a){return this.groups[a.name]||(this.checkable(a)?a.name:a.id||a.name)},validationTargetFor:function(b){return this.checkable(b)&&(b=this.findByName(b.name)),a(b).not(this.settings.ignore)[0]},checkable:function(a){return/radio|checkbox/i.test(a.type)},findByName:function(b){return a(this.currentForm).find("[name='"+this.escapeCssMeta(b)+"']")},getLength:function(b,c){switch(c.nodeName.toLowerCase()){case"select":return a("option:selected",c).length;case"input":if(this.checkable(c))return this.findByName(c.name).filter(":checked").length}return b.length},depend:function(a,b){return!this.dependTypes[typeof a]||this.dependTypes[typeof a](a,b)},dependTypes:{boolean:function(a){return a},string:function(b,c){return!!a(b,c.form).length},function:function(a,b){return a(b)}},optional:function(b){var c=this.elementValue(b);return!a.validator.methods.required.call(this,c,b)&&"dependency-mismatch"},startRequest:function(b){this.pending[b.name]||(this.pendingRequest++,a(b).addClass(this.settings.pendingClass),this.pending[b.name]=!0)},stopRequest:function(b,c){this.pendingRequest--,this.pendingRequest<0&&(this.pendingRequest=0),delete this.pending[b.name],a(b).removeClass(this.settings.pendingClass),c&&0===this.pendingRequest&&this.formSubmitted&&this.form()?(a(this.currentForm).submit(),this.formSubmitted=!1):!c&&0===this.pendingRequest&&this.formSubmitted&&(a(this.currentForm).triggerHandler("valid-form",[this]),this.formSubmitted=!1)},previousValue:function(b,c){return c="string"==typeof c&&c||"remote",a.data(b,"previousValue")||a.data(b,"previousValue",{old:null,valid:!0,message:this.defaultMessage(b,{method:c})})},destroy:function(){this.resetForm(),a(this.currentForm).off(".validate").removeData("validator").find(".validate-equalTo-blur").off(".validate-equalTo").removeClass("validate-equalTo-blur")}},classRuleSettings:{required:{required:!0},email:{email:!0},url:{url:!0},date:{date:!0},dateISO:{dateISO:!0},number:{number:!0},digits:{digits:!0},creditcard:{creditcard:!0}},addClassRules:function(b,c){b.constructor===String?this.classRuleSettings[b]=c:a.extend(this.classRuleSettings,b)},classRules:function(b){var c={},d=a(b).attr("class");return d&&a.each(d.split(" "),function(){this in a.validator.classRuleSettings&&a.extend(c,a.validator.classRuleSettings[this])}),c},normalizeAttributeRule:function(a,b,c,d){/min|max|step/.test(c)&&(null===b||/number|range|text/.test(b))&&(d=Number(d),isNaN(d)&&(d=void 0)),d||0===d?a[c]=d:b===c&&"range"!==b&&(a[c]=!0)},attributeRules:function(b){var c,d,e={},f=a(b),g=b.getAttribute("type");for(c in a.validator.methods)"required"===c?(d=b.getAttribute(c),""===d&&(d=!0),d=!!d):d=f.attr(c),this.normalizeAttributeRule(e,g,c,d);return e.maxlength&&/-1|2147483647|524288/.test(e.maxlength)&&delete e.maxlength,e},dataRules:function(b){var c,d,e={},f=a(b),g=b.getAttribute("type");for(c in a.validator.methods)d=f.data("rule"+c.charAt(0).toUpperCase()+c.substring(1).toLowerCase()),this.normalizeAttributeRule(e,g,c,d);return e},staticRules:function(b){var c={},d=a.data(b.form,"validator");return d.settings.rules&&(c=a.validator.normalizeRule(d.settings.rules[b.name])||{}),c},normalizeRules:function(b,c){return a.each(b,function(d,e){if(e===!1)return void delete b[d];if(e.param||e.depends){var f=!0;switch(typeof e.depends){case"string":f=!!a(e.depends,c.form).length;break;case"function":f=e.depends.call(c,c)}f?b[d]=void 0===e.param||e.param:(a.data(c.form,"validator").resetElements(a(c)),delete b[d])}}),a.each(b,function(d,e){b[d]=a.isFunction(e)&&"normalizer"!==d?e(c):e}),a.each(["minlength","maxlength"],function(){b[this]&&(b[this]=Number(b[this]))}),a.each(["rangelength","range"],function(){var c;b[this]&&(a.isArray(b[this])?b[this]=[Number(b[this][0]),Number(b[this][1])]:"string"==typeof b[this]&&(c=b[this].replace(/[\[\]]/g,"").split(/[\s,]+/),b[this]=[Number(c[0]),Number(c[1])]))}),a.validator.autoCreateRanges&&(null!=b.min&&null!=b.max&&(b.range=[b.min,b.max],delete b.min,delete b.max),null!=b.minlength&&null!=b.maxlength&&(b.rangelength=[b.minlength,b.maxlength],delete b.minlength,delete b.maxlength)),b},normalizeRule:function(b){if("string"==typeof b){var c={};a.each(b.split(/\s/),function(){c[this]=!0}),b=c}return b},addMethod:function(b,c,d){a.validator.methods[b]=c,a.validator.messages[b]=void 0!==d?d:a.validator.messages[b],c.length<3&&a.validator.addClassRules(b,a.validator.normalizeRule(b))},methods:{required:function(b,c,d){if(!this.depend(d,c))return"dependency-mismatch";if("select"===c.nodeName.toLowerCase()){var e=a(c).val();return e&&e.length>0}return this.checkable(c)?this.getLength(b,c)>0:b.length>0},email:function(a,b){return this.optional(b)||/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/.test(a)},url:function(a,b){return this.optional(b)||/^(?:(?:(?:https?|ftp):)?\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})).?)(?::\d{2,5})?(?:[/?#]\S*)?$/i.test(a)},date:function(a,b){return this.optional(b)||!/valid|NaN/.test(new Date(a).toString())},dateISO:function(a,b){return this.optional(b)||/^\d{4}[\/\-](0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])$/.test(a)},number:function(a,b){return this.optional(b)||/^(?:-?\d+|-?\d{1,3}(?:,\d{3})+)?(?:\.\d+)?$/.test(a)},digits:function(a,b){return this.optional(b)||/^\d+$/.test(a)},minlength:function(b,c,d){var e=a.isArray(b)?b.length:this.getLength(b,c);return this.optional(c)||e>=d},maxlength:function(b,c,d){var e=a.isArray(b)?b.length:this.getLength(b,c);return this.optional(c)||e<=d},rangelength:function(b,c,d){var e=a.isArray(b)?b.length:this.getLength(b,c);return this.optional(c)||e>=d[0]&&e<=d[1]},min:function(a,b,c){return this.optional(b)||a>=c},max:function(a,b,c){return this.optional(b)||a<=c},range:function(a,b,c){return this.optional(b)||a>=c[0]&&a<=c[1]},step:function(b,c,d){var e,f=a(c).attr("type"),g="Step attribute on input type "+f+" is not supported.",h=["text","number","range"],i=new RegExp("\\b"+f+"\\b"),j=f&&!i.test(h.join()),k=function(a){var b=(""+a).match(/(?:\.(\d+))?$/);return b&&b[1]?b[1].length:0},l=function(a){return Math.round(a*Math.pow(10,e))},m=!0;if(j)throw new Error(g);return e=k(d),(k(b)>e||l(b)%l(d)!==0)&&(m=!1),this.optional(c)||m},equalTo:function(b,c,d){var e=a(d);return this.settings.onfocusout&&e.not(".validate-equalTo-blur").length&&e.addClass("validate-equalTo-blur").on("blur.validate-equalTo",function(){a(c).valid()}),b===e.val()},remote:function(b,c,d,e){if(this.optional(c))return"dependency-mismatch";e="string"==typeof e&&e||"remote";var f,g,h,i=this.previousValue(c,e);return this.settings.messages[c.name]||(this.settings.messages[c.name]={}),i.originalMessage=i.originalMessage||this.settings.messages[c.name][e],this.settings.messages[c.name][e]=i.message,d="string"==typeof d&&{url:d}||d,h=a.param(a.extend({data:b},d.data)),i.old===h?i.valid:(i.old=h,f=this,this.startRequest(c),g={},g[c.name]=b,a.ajax(a.extend(!0,{mode:"abort",port:"validate"+c.name,dataType:"json",data:g,context:f.currentForm,success:function(a){var d,g,h,j=a===!0||"true"===a;f.settings.messages[c.name][e]=i.originalMessage,j?(h=f.formSubmitted,f.resetInternals(),f.toHide=f.errorsFor(c),f.formSubmitted=h,f.successList.push(c),f.valid[c.name]=!1,f.showErrors()):(d={},g=a||f.defaultMessage(c,{method:e,parameters:b}),d[c.name]=i.message=g,f.valid[c.name]=!0,f.showErrors(d)),i.valid=j,f.stopRequest(c,j)}},d)),"pending")}}});var b,c={};a.ajaxPrefilter?a.ajaxPrefilter(function(a,b,d){var e=a.port;"abort"===a.mode&&(c[e]&&c[e].abort(),c[e]=d)}):(b=a.ajax,a.ajax=function(d){var e=("mode"in d?d:a.ajaxSettings).mode,f=("port"in d?d:a.ajaxSettings).port;return"abort"===e?(c[f]&&c[f].abort(),c[f]=b.apply(this,arguments),c[f]):b.apply(this,arguments)})});

/*! jQuery Validation Plugin - v1.15.1 - 7/22/2016
 * http://jqueryvalidation.org/
 * Copyright (c) 2016 Jörn Zaefferer; Licensed MIT */
!function(a){"function"==typeof define&&define.amd?define(["jquery","./jquery.validate.min"],a):"object"==typeof module&&module.exports?module.exports=a(require("jquery")):a(jQuery)}(function(a){!function(){function b(a){return a.replace(/<.[^<>]*?>/g," ").replace(/&nbsp;|&#160;/gi," ").replace(/[.(),;:!?%#$'\"_+=\/\-“”’]*/g,"")}a.validator.addMethod("maxWords",function(a,c,d){return this.optional(c)||b(a).match(/\b\w+\b/g).length<=d},a.validator.format("Please enter {0} words or less.")),a.validator.addMethod("minWords",function(a,c,d){return this.optional(c)||b(a).match(/\b\w+\b/g).length>=d},a.validator.format("Please enter at least {0} words.")),a.validator.addMethod("rangeWords",function(a,c,d){var e=b(a),f=/\b\w+\b/g;return this.optional(c)||e.match(f).length>=d[0]&&e.match(f).length<=d[1]},a.validator.format("Please enter between {0} and {1} words."))}(),a.validator.addMethod("accept",function(b,c,d){var e,f,g,h="string"==typeof d?d.replace(/\s/g,""):"image/*",i=this.optional(c);if(i)return i;if("file"===a(c).attr("type")&&(h=h.replace(/[\-\[\]\/\{\}\(\)\+\?\.\\\^\$\|]/g,"\\$&").replace(/,/g,"|").replace(/\/\*/g,"/.*"),c.files&&c.files.length))for(g=new RegExp(".?("+h+")$","i"),e=0;e<c.files.length;e++)if(f=c.files[e],!f.type.match(g))return!1;return!0},a.validator.format("Please enter a value with a valid mimetype.")),a.validator.addMethod("alphanumeric",function(a,b){return this.optional(b)||/^\w+$/i.test(a)},"Letters, numbers, and underscores only please"),a.validator.addMethod("bankaccountNL",function(a,b){if(this.optional(b))return!0;if(!/^[0-9]{9}|([0-9]{2} ){3}[0-9]{3}$/.test(a))return!1;var c,d,e,f=a.replace(/ /g,""),g=0,h=f.length;for(c=0;c<h;c++)d=h-c,e=f.substring(c,c+1),g+=d*e;return g%11===0},"Please specify a valid bank account number"),a.validator.addMethod("bankorgiroaccountNL",function(b,c){return this.optional(c)||a.validator.methods.bankaccountNL.call(this,b,c)||a.validator.methods.giroaccountNL.call(this,b,c)},"Please specify a valid bank or giro account number"),a.validator.addMethod("bic",function(a,b){return this.optional(b)||/^([A-Z]{6}[A-Z2-9][A-NP-Z1-9])(X{3}|[A-WY-Z0-9][A-Z0-9]{2})?$/.test(a.toUpperCase())},"Please specify a valid BIC code"),a.validator.addMethod("cifES",function(a){"use strict";var b,c,d,e,f,g,h=[];if(a=a.toUpperCase(),!a.match("((^[A-Z]{1}[0-9]{7}[A-Z0-9]{1}$|^[T]{1}[A-Z0-9]{8}$)|^[0-9]{8}[A-Z]{1}$)"))return!1;for(d=0;d<9;d++)h[d]=parseInt(a.charAt(d),10);for(c=h[2]+h[4]+h[6],e=1;e<8;e+=2)f=(2*h[e]).toString(),g=f.charAt(1),c+=parseInt(f.charAt(0),10)+(""===g?0:parseInt(g,10));return!!/^[ABCDEFGHJNPQRSUVW]{1}/.test(a)&&(c+="",b=10-parseInt(c.charAt(c.length-1),10),a+=b,h[8].toString()===String.fromCharCode(64+b)||h[8].toString()===a.charAt(a.length-1))},"Please specify a valid CIF number."),a.validator.addMethod("cpfBR",function(a){if(a=a.replace(/([~!@#$%^&*()_+=`{}\[\]\-|\\:;'<>,.\/? ])+/g,""),11!==a.length)return!1;var b,c,d,e,f=0;if(b=parseInt(a.substring(9,10),10),c=parseInt(a.substring(10,11),10),d=function(a,b){var c=10*a%11;return 10!==c&&11!==c||(c=0),c===b},""===a||"00000000000"===a||"11111111111"===a||"22222222222"===a||"33333333333"===a||"44444444444"===a||"55555555555"===a||"66666666666"===a||"77777777777"===a||"88888888888"===a||"99999999999"===a)return!1;for(e=1;e<=9;e++)f+=parseInt(a.substring(e-1,e),10)*(11-e);if(d(f,b)){for(f=0,e=1;e<=10;e++)f+=parseInt(a.substring(e-1,e),10)*(12-e);return d(f,c)}return!1},"Please specify a valid CPF number"),a.validator.addMethod("creditcard",function(a,b){if(this.optional(b))return"dependency-mismatch";if(/[^0-9 \-]+/.test(a))return!1;var c,d,e=0,f=0,g=!1;if(a=a.replace(/\D/g,""),a.length<13||a.length>19)return!1;for(c=a.length-1;c>=0;c--)d=a.charAt(c),f=parseInt(d,10),g&&(f*=2)>9&&(f-=9),e+=f,g=!g;return e%10===0},"Please enter a valid credit card number."),a.validator.addMethod("creditcardtypes",function(a,b,c){if(/[^0-9\-]+/.test(a))return!1;a=a.replace(/\D/g,"");var d=0;return c.mastercard&&(d|=1),c.visa&&(d|=2),c.amex&&(d|=4),c.dinersclub&&(d|=8),c.enroute&&(d|=16),c.discover&&(d|=32),c.jcb&&(d|=64),c.unknown&&(d|=128),c.all&&(d=255),1&d&&/^(5[12345])/.test(a)?16===a.length:2&d&&/^(4)/.test(a)?16===a.length:4&d&&/^(3[47])/.test(a)?15===a.length:8&d&&/^(3(0[012345]|[68]))/.test(a)?14===a.length:16&d&&/^(2(014|149))/.test(a)?15===a.length:32&d&&/^(6011)/.test(a)?16===a.length:64&d&&/^(3)/.test(a)?16===a.length:64&d&&/^(2131|1800)/.test(a)?15===a.length:!!(128&d)},"Please enter a valid credit card number."),a.validator.addMethod("currency",function(a,b,c){var d,e="string"==typeof c,f=e?c:c[0],g=!!e||c[1];return f=f.replace(/,/g,""),f=g?f+"]":f+"]?",d="^["+f+"([1-9]{1}[0-9]{0,2}(\\,[0-9]{3})*(\\.[0-9]{0,2})?|[1-9]{1}[0-9]{0,}(\\.[0-9]{0,2})?|0(\\.[0-9]{0,2})?|(\\.[0-9]{1,2})?)$",d=new RegExp(d),this.optional(b)||d.test(a)},"Please specify a valid currency"),a.validator.addMethod("dateFA",function(a,b){return this.optional(b)||/^[1-4]\d{3}\/((0?[1-6]\/((3[0-1])|([1-2][0-9])|(0?[1-9])))|((1[0-2]|(0?[7-9]))\/(30|([1-2][0-9])|(0?[1-9]))))$/.test(a)},a.validator.messages.date),a.validator.addMethod("dateITA",function(a,b){var c,d,e,f,g,h=!1,i=/^\d{1,2}\/\d{1,2}\/\d{4}$/;return i.test(a)?(c=a.split("/"),d=parseInt(c[0],10),e=parseInt(c[1],10),f=parseInt(c[2],10),g=new Date(Date.UTC(f,e-1,d,12,0,0,0)),h=g.getUTCFullYear()===f&&g.getUTCMonth()===e-1&&g.getUTCDate()===d):h=!1,this.optional(b)||h},a.validator.messages.date),a.validator.addMethod("dateNL",function(a,b){return this.optional(b)||/^(0?[1-9]|[12]\d|3[01])[\.\/\-](0?[1-9]|1[012])[\.\/\-]([12]\d)?(\d\d)$/.test(a)},a.validator.messages.date),a.validator.addMethod("extension",function(a,b,c){return c="string"==typeof c?c.replace(/,/g,"|"):"png|jpe?g|gif",this.optional(b)||a.match(new RegExp("\\.("+c+")$","i"))},a.validator.format("Please enter a value with a valid extension.")),a.validator.addMethod("giroaccountNL",function(a,b){return this.optional(b)||/^[0-9]{1,7}$/.test(a)},"Please specify a valid giro account number"),a.validator.addMethod("iban",function(a,b){if(this.optional(b))return!0;var c,d,e,f,g,h,i,j,k,l=a.replace(/ /g,"").toUpperCase(),m="",n=!0,o="",p="",q=5;if(l.length<q)return!1;if(c=l.substring(0,2),h={AL:"\\d{8}[\\dA-Z]{16}",AD:"\\d{8}[\\dA-Z]{12}",AT:"\\d{16}",AZ:"[\\dA-Z]{4}\\d{20}",BE:"\\d{12}",BH:"[A-Z]{4}[\\dA-Z]{14}",BA:"\\d{16}",BR:"\\d{23}[A-Z][\\dA-Z]",BG:"[A-Z]{4}\\d{6}[\\dA-Z]{8}",CR:"\\d{17}",HR:"\\d{17}",CY:"\\d{8}[\\dA-Z]{16}",CZ:"\\d{20}",DK:"\\d{14}",DO:"[A-Z]{4}\\d{20}",EE:"\\d{16}",FO:"\\d{14}",FI:"\\d{14}",FR:"\\d{10}[\\dA-Z]{11}\\d{2}",GE:"[\\dA-Z]{2}\\d{16}",DE:"\\d{18}",GI:"[A-Z]{4}[\\dA-Z]{15}",GR:"\\d{7}[\\dA-Z]{16}",GL:"\\d{14}",GT:"[\\dA-Z]{4}[\\dA-Z]{20}",HU:"\\d{24}",IS:"\\d{22}",IE:"[\\dA-Z]{4}\\d{14}",IL:"\\d{19}",IT:"[A-Z]\\d{10}[\\dA-Z]{12}",KZ:"\\d{3}[\\dA-Z]{13}",KW:"[A-Z]{4}[\\dA-Z]{22}",LV:"[A-Z]{4}[\\dA-Z]{13}",LB:"\\d{4}[\\dA-Z]{20}",LI:"\\d{5}[\\dA-Z]{12}",LT:"\\d{16}",LU:"\\d{3}[\\dA-Z]{13}",MK:"\\d{3}[\\dA-Z]{10}\\d{2}",MT:"[A-Z]{4}\\d{5}[\\dA-Z]{18}",MR:"\\d{23}",MU:"[A-Z]{4}\\d{19}[A-Z]{3}",MC:"\\d{10}[\\dA-Z]{11}\\d{2}",MD:"[\\dA-Z]{2}\\d{18}",ME:"\\d{18}",NL:"[A-Z]{4}\\d{10}",NO:"\\d{11}",PK:"[\\dA-Z]{4}\\d{16}",PS:"[\\dA-Z]{4}\\d{21}",PL:"\\d{24}",PT:"\\d{21}",RO:"[A-Z]{4}[\\dA-Z]{16}",SM:"[A-Z]\\d{10}[\\dA-Z]{12}",SA:"\\d{2}[\\dA-Z]{18}",RS:"\\d{18}",SK:"\\d{20}",SI:"\\d{15}",ES:"\\d{20}",SE:"\\d{20}",CH:"\\d{5}[\\dA-Z]{12}",TN:"\\d{20}",TR:"\\d{5}[\\dA-Z]{17}",AE:"\\d{3}\\d{16}",GB:"[A-Z]{4}\\d{14}",VG:"[\\dA-Z]{4}\\d{16}"},g=h[c],"undefined"!=typeof g&&(i=new RegExp("^[A-Z]{2}\\d{2}"+g+"$",""),!i.test(l)))return!1;for(d=l.substring(4,l.length)+l.substring(0,4),j=0;j<d.length;j++)e=d.charAt(j),"0"!==e&&(n=!1),n||(m+="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(e));for(k=0;k<m.length;k++)f=m.charAt(k),p=""+o+f,o=p%97;return 1===o},"Please specify a valid IBAN"),a.validator.addMethod("integer",function(a,b){return this.optional(b)||/^-?\d+$/.test(a)},"A positive or negative non-decimal number please"),a.validator.addMethod("ipv4",function(a,b){return this.optional(b)||/^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$/i.test(a)},"Please enter a valid IP v4 address."),a.validator.addMethod("ipv6",function(a,b){return this.optional(b)||/^((([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}:[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){5}:([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){4}:([0-9A-Fa-f]{1,4}:){0,2}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){3}:([0-9A-Fa-f]{1,4}:){0,3}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){2}:([0-9A-Fa-f]{1,4}:){0,4}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(([0-9A-Fa-f]{1,4}:){0,5}:((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(::([0-9A-Fa-f]{1,4}:){0,5}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|([0-9A-Fa-f]{1,4}::([0-9A-Fa-f]{1,4}:){0,5}[0-9A-Fa-f]{1,4})|(::([0-9A-Fa-f]{1,4}:){0,6}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,7}:))$/i.test(a)},"Please enter a valid IP v6 address."),a.validator.addMethod("lettersonly",function(a,b){return this.optional(b)||/^[a-z]+$/i.test(a)},"Letters only please"),a.validator.addMethod("letterswithbasicpunc",function(a,b){return this.optional(b)||/^[a-z\-.,()'"\s]+$/i.test(a)},"Letters or punctuation only please"),a.validator.addMethod("mobileNL",function(a,b){return this.optional(b)||/^((\+|00(\s|\s?\-\s?)?)31(\s|\s?\-\s?)?(\(0\)[\-\s]?)?|0)6((\s|\s?\-\s?)?[0-9]){8}$/.test(a)},"Please specify a valid mobile number"),a.validator.addMethod("mobileUK",function(a,b){return a=a.replace(/\(|\)|\s+|-/g,""),this.optional(b)||a.length>9&&a.match(/^(?:(?:(?:00\s?|\+)44\s?|0)7(?:[1345789]\d{2}|624)\s?\d{3}\s?\d{3})$/)},"Please specify a valid mobile number"),a.validator.addMethod("nieES",function(a){"use strict";return a=a.toUpperCase(),!!a.match("((^[A-Z]{1}[0-9]{7}[A-Z0-9]{1}$|^[T]{1}[A-Z0-9]{8}$)|^[0-9]{8}[A-Z]{1}$)")&&(/^[T]{1}/.test(a)?a[8]===/^[T]{1}[A-Z0-9]{8}$/.test(a):!!/^[XYZ]{1}/.test(a)&&a[8]==="TRWAGMYFPDXBNJZSQVHLCKE".charAt(a.replace("X","0").replace("Y","1").replace("Z","2").substring(0,8)%23))},"Please specify a valid NIE number."),a.validator.addMethod("nifES",function(a){"use strict";return a=a.toUpperCase(),!!a.match("((^[A-Z]{1}[0-9]{7}[A-Z0-9]{1}$|^[T]{1}[A-Z0-9]{8}$)|^[0-9]{8}[A-Z]{1}$)")&&(/^[0-9]{8}[A-Z]{1}$/.test(a)?"TRWAGMYFPDXBNJZSQVHLCKE".charAt(a.substring(8,0)%23)===a.charAt(8):!!/^[KLM]{1}/.test(a)&&a[8]===String.fromCharCode(64))},"Please specify a valid NIF number."),a.validator.addMethod("notEqualTo",function(b,c,d){return this.optional(c)||!a.validator.methods.equalTo.call(this,b,c,d)},"Please enter a different value, values must not be the same."),a.validator.addMethod("nowhitespace",function(a,b){return this.optional(b)||/^\S+$/i.test(a)},"No white space please"),a.validator.addMethod("pattern",function(a,b,c){return!!this.optional(b)||("string"==typeof c&&(c=new RegExp("^(?:"+c+")$")),c.test(a))},"valid format."),a.validator.addMethod("phoneNL",function(a,b){return this.optional(b)||/^((\+|00(\s|\s?\-\s?)?)31(\s|\s?\-\s?)?(\(0\)[\-\s]?)?|0)[1-9]((\s|\s?\-\s?)?[0-9]){8}$/.test(a)},"Please specify a valid phone number."),a.validator.addMethod("phoneUK",function(a,b){return a=a.replace(/\(|\)|\s+|-/g,""),this.optional(b)||a.length>9&&a.match(/^(?:(?:(?:00\s?|\+)44\s?)|(?:\(?0))(?:\d{2}\)?\s?\d{4}\s?\d{4}|\d{3}\)?\s?\d{3}\s?\d{3,4}|\d{4}\)?\s?(?:\d{5}|\d{3}\s?\d{3})|\d{5}\)?\s?\d{4,5})$/)},"Please specify a valid phone number"),a.validator.addMethod("phoneUS",function(a,b){return a=a.replace(/\s+/g,""),this.optional(b)||a.length>9&&a.match(/^(\+?1-?)?(\([2-9]([02-9]\d|1[02-9])\)|[2-9]([02-9]\d|1[02-9]))-?[2-9]([02-9]\d|1[02-9])-?\d{4}$/)},"Please specify a valid phone number"),a.validator.addMethod("phonesUK",function(a,b){return a=a.replace(/\(|\)|\s+|-/g,""),this.optional(b)||a.length>9&&a.match(/^(?:(?:(?:00\s?|\+)44\s?|0)(?:1\d{8,9}|[23]\d{9}|7(?:[1345789]\d{8}|624\d{6})))$/)},"Please specify a valid uk phone number"),a.validator.addMethod("postalCodeCA",function(a,b){return this.optional(b)||/^[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ] *\d[ABCEGHJKLMNPRSTVWXYZ]\d$/i.test(a)},"Please specify a valid postal code"),a.validator.addMethod("postalcodeBR",function(a,b){return this.optional(b)||/^\d{2}.\d{3}-\d{3}?$|^\d{5}-?\d{3}?$/.test(a)},"Informe um CEP válido."),a.validator.addMethod("postalcodeIT",function(a,b){return this.optional(b)||/^\d{5}$/.test(a)},"Please specify a valid postal code"),a.validator.addMethod("postalcodeNL",function(a,b){return this.optional(b)||/^[1-9][0-9]{3}\s?[a-zA-Z]{2}$/.test(a)},"Please specify a valid postal code"),a.validator.addMethod("postcodeUK",function(a,b){return this.optional(b)||/^((([A-PR-UWYZ][0-9])|([A-PR-UWYZ][0-9][0-9])|([A-PR-UWYZ][A-HK-Y][0-9])|([A-PR-UWYZ][A-HK-Y][0-9][0-9])|([A-PR-UWYZ][0-9][A-HJKSTUW])|([A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))\s?([0-9][ABD-HJLNP-UW-Z]{2})|(GIR)\s?(0AA))$/i.test(a)},"Please specify a valid UK postcode"),a.validator.addMethod("require_from_group",function(b,c,d){var e=a(d[1],c.form),f=e.eq(0),g=f.data("valid_req_grp")?f.data("valid_req_grp"):a.extend({},this),h=e.filter(function(){return g.elementValue(this)}).length>=d[0];return f.data("valid_req_grp",g),a(c).data("being_validated")||(e.data("being_validated",!0),e.each(function(){g.element(this)}),e.data("being_validated",!1)),h},a.validator.format("Please fill at least {0} of these fields.")),a.validator.addMethod("skip_or_fill_minimum",function(b,c,d){var e=a(d[1],c.form),f=e.eq(0),g=f.data("valid_skip")?f.data("valid_skip"):a.extend({},this),h=e.filter(function(){return g.elementValue(this)}).length,i=0===h||h>=d[0];return f.data("valid_skip",g),a(c).data("being_validated")||(e.data("being_validated",!0),e.each(function(){g.element(this)}),e.data("being_validated",!1)),i},a.validator.format("Please either skip these fields or fill at least {0} of them.")),a.validator.addMethod("stateUS",function(a,b,c){var d,e="undefined"==typeof c,f=!e&&"undefined"!=typeof c.caseSensitive&&c.caseSensitive,g=!e&&"undefined"!=typeof c.includeTerritories&&c.includeTerritories,h=!e&&"undefined"!=typeof c.includeMilitary&&c.includeMilitary;return d=g||h?g&&h?"^(A[AEKLPRSZ]|C[AOT]|D[CE]|FL|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ADEINOPST]|N[CDEHJMVY]|O[HKR]|P[AR]|RI|S[CD]|T[NX]|UT|V[AIT]|W[AIVY])$":g?"^(A[KLRSZ]|C[AOT]|D[CE]|FL|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ADEINOPST]|N[CDEHJMVY]|O[HKR]|P[AR]|RI|S[CD]|T[NX]|UT|V[AIT]|W[AIVY])$":"^(A[AEKLPRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])$":"^(A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])$",d=f?new RegExp(d):new RegExp(d,"i"),this.optional(b)||d.test(a)},"Please specify a valid state"),a.validator.addMethod("strippedminlength",function(b,c,d){return a(b).text().length>=d},a.validator.format("Please enter at least {0} characters")),a.validator.addMethod("time",function(a,b){return this.optional(b)||/^([01]\d|2[0-3]|[0-9])(:[0-5]\d){1,2}$/.test(a)},"Please enter a valid time, between 00:00 and 23:59"),a.validator.addMethod("time12h",function(a,b){return this.optional(b)||/^((0?[1-9]|1[012])(:[0-5]\d){1,2}(\ ?[AP]M))$/i.test(a)},"Please enter a valid time in 12-hour am/pm format"),a.validator.addMethod("url2",function(a,b){return this.optional(b)||/^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)*(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i.test(a)},a.validator.messages.url),a.validator.addMethod("vinUS",function(a){if(17!==a.length)return!1;var b,c,d,e,f,g,h=["A","B","C","D","E","F","G","H","J","K","L","M","N","P","R","S","T","U","V","W","X","Y","Z"],i=[1,2,3,4,5,6,7,8,1,2,3,4,5,7,9,2,3,4,5,6,7,8,9],j=[8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2],k=0;for(b=0;b<17;b++){if(e=j[b],d=a.slice(b,b+1),8===b&&(g=d),isNaN(d)){for(c=0;c<h.length;c++)if(d.toUpperCase()===h[c]){d=i[c],d*=e,isNaN(g)&&8===c&&(g=h[c]);break}}else d*=e;k+=d}return f=k%11,10===f&&(f="X"),f===g},"The specified vehicle identification number (VIN) is valid."),a.validator.addMethod("zipcodeUS",function(a,b){return this.optional(b)||/^\d{5}(-\d{4})?$/.test(a)},"The specified US ZIP Code is valid"),a.validator.addMethod("ziprange",function(a,b){return this.optional(b)||/^90[2-5]\d\{2\}-\d{4}$/.test(a)},"Your ZIP-code must be in the range 902xx-xxxx to 905xx-xxxx")});

/*jquery.mb.YTPlayer 25-07-2016
 _ jquery.mb.components 
 _ email: matteo@open-lab.com 
 _ Copyright (c) 2001-2016. Matteo Bicocchi (Pupunzi); 
 _ blog: http://pupunzi.open-lab.com 
 _ Open Lab s.r.l., Florence - Italy 
 */
function onYouTubeIframeAPIReady(){ytp.YTAPIReady||(ytp.YTAPIReady=!0,jQuery(document).trigger("YTAPIReady"))}function uncamel(a){return a.replace(/([A-Z])/g,function(a){return"-"+a.toLowerCase()})}function setUnit(a,b){return"string"!=typeof a||a.match(/^[\-0-9\.]+jQuery/)?""+a+b:a}function setFilter(a,b,c){var d=uncamel(b),e=jQuery.browser.mozilla?"":jQuery.CSS.sfx;a[e+"filter"]=a[e+"filter"]||"",c=setUnit(c>jQuery.CSS.filters[b].max?jQuery.CSS.filters[b].max:c,jQuery.CSS.filters[b].unit),a[e+"filter"]+=d+"("+c+") ",delete a[b]}var ytp=ytp||{},getYTPVideoID=function(a){var b,c;return a.indexOf("youtu.be")>0?(b=a.substr(a.lastIndexOf("/")+1,a.length),c=b.indexOf("?list=")>0?b.substr(b.lastIndexOf("="),b.length):null,b=c?b.substr(0,b.lastIndexOf("?")):b):a.indexOf("http")>-1?(b=a.match(/[\\?&]v=([^&#]*)/)[1],c=a.indexOf("list=")>0?a.match(/[\\?&]list=([^&#]*)/)[1]:null):(b=a.length>15?null:a,c=b?null:a),{videoID:b,playlistID:c}};!function(jQuery,ytp){jQuery.mbYTPlayer={name:"jquery.mb.YTPlayer",version:"3.0.8",build:"5878",author:"Matteo Bicocchi",apiKey:"",defaults:{containment:"body",ratio:"auto",videoURL:null,playlistURL:null,startAt:0,stopAt:0,autoPlay:!0,vol:50,addRaster:!1,mask:!1,opacity:1,quality:"default",mute:!1,loop:!0,showControls:!0,showAnnotations:!1,showYTLogo:!0,stopMovieOnBlur:!0,realfullscreen:!0,mobileFallbackImage:null,gaTrack:!0,optimizeDisplay:!0,align:"center,center",onReady:function(a){}},controls:{play:"P",pause:"p",mute:"M",unmute:"A",onlyYT:"O",showSite:"R",ytLogo:"Y"},controlBar:null,loading:null,locationProtocol:"https:",filters:{grayscale:{value:0,unit:"%"},hue_rotate:{value:0,unit:"deg"},invert:{value:0,unit:"%"},opacity:{value:0,unit:"%"},saturate:{value:0,unit:"%"},sepia:{value:0,unit:"%"},brightness:{value:0,unit:"%"},contrast:{value:0,unit:"%"},blur:{value:0,unit:"px"}},buildPlayer:function(options){return this.each(function(){var YTPlayer=this,$YTPlayer=jQuery(YTPlayer);YTPlayer.loop=0,YTPlayer.opt={},YTPlayer.state={},YTPlayer.filters=jQuery.mbYTPlayer.filters,YTPlayer.filtersEnabled=!0,YTPlayer.id=YTPlayer.id||"YTP_"+(new Date).getTime(),$YTPlayer.addClass("mb_YTPlayer");var property=$YTPlayer.data("property")&&"string"==typeof $YTPlayer.data("property")?eval("("+$YTPlayer.data("property")+")"):$YTPlayer.data("property");"undefined"!=typeof property&&"undefined"!=typeof property.vol&&(property.vol=0===property.vol?property.vol=1:property.vol),jQuery.extend(YTPlayer.opt,jQuery.mbYTPlayer.defaults,options,property),YTPlayer.hasChanged||(YTPlayer.defaultOpt={},jQuery.extend(YTPlayer.defaultOpt,jQuery.mbYTPlayer.defaults,options)),"true"==YTPlayer.opt.loop&&(YTPlayer.opt.loop=9999),YTPlayer.isRetina=window.retina||window.devicePixelRatio>1;var isIframe=function(){var a=!1;try{self.location.href!=top.location.href&&(a=!0)}catch(b){a=!0}return a};YTPlayer.canGoFullScreen=!(jQuery.browser.msie||jQuery.browser.opera||isIframe()),YTPlayer.canGoFullScreen||(YTPlayer.opt.realfullscreen=!1),$YTPlayer.attr("id")||$YTPlayer.attr("id","video_"+(new Date).getTime());var playerID="mbYTP_"+YTPlayer.id;YTPlayer.isAlone=!1,YTPlayer.hasFocus=!0;var videoID=this.opt.videoURL?getYTPVideoID(this.opt.videoURL).videoID:$YTPlayer.attr("href")?getYTPVideoID($YTPlayer.attr("href")).videoID:!1,playlistID=this.opt.videoURL?getYTPVideoID(this.opt.videoURL).playlistID:$YTPlayer.attr("href")?getYTPVideoID($YTPlayer.attr("href")).playlistID:!1;YTPlayer.videoID=videoID,YTPlayer.playlistID=playlistID,YTPlayer.opt.showAnnotations=YTPlayer.opt.showAnnotations?"0":"3";var playerVars={modestbranding:1,autoplay:0,controls:0,showinfo:0,rel:0,enablejsapi:1,version:3,playerapiid:playerID,origin:"*",allowfullscreen:!0,wmode:"transparent",iv_load_policy:YTPlayer.opt.showAnnotations};if(document.createElement("video").canPlayType&&jQuery.extend(playerVars,{html5:1}),jQuery.browser.msie&&jQuery.browser.version<9&&(this.opt.opacity=1),YTPlayer.isSelf="self"==YTPlayer.opt.containment,YTPlayer.defaultOpt.containment=YTPlayer.opt.containment=jQuery("self"==YTPlayer.opt.containment?this:YTPlayer.opt.containment),YTPlayer.isBackground=YTPlayer.opt.containment.is("body"),!YTPlayer.isBackground||!ytp.backgroundIsInited){var isPlayer=YTPlayer.opt.containment.is(jQuery(this));YTPlayer.canPlayOnMobile=isPlayer&&0===jQuery(this).children().length,YTPlayer.isPlayer=!1,isPlayer?YTPlayer.isPlayer=!0:$YTPlayer.hide();var overlay=jQuery("<div/>").css({position:"absolute",top:0,left:0,width:"100%",height:"100%"}).addClass("YTPOverlay");YTPlayer.isPlayer&&overlay.on("click",function(){$YTPlayer.YTPTogglePlay()});var wrapper=jQuery("<div/>").addClass("mbYTP_wrapper").attr("id","wrapper_"+playerID);wrapper.css({position:"absolute",zIndex:0,minWidth:"100%",minHeight:"100%",left:0,top:0,overflow:"hidden",opacity:0});var playerBox=jQuery("<div/>").attr("id",playerID).addClass("playerBox");if(playerBox.css({position:"absolute",zIndex:0,width:"100%",height:"100%",top:0,left:0,overflow:"hidden"}),wrapper.append(playerBox),YTPlayer.opt.containment.children().not("script, style").each(function(){"static"==jQuery(this).css("position")&&jQuery(this).css("position","relative")}),YTPlayer.isBackground?(jQuery("body").css({boxSizing:"border-box"}),wrapper.css({position:"fixed",top:0,left:0,zIndex:0}),$YTPlayer.hide()):"static"==YTPlayer.opt.containment.css("position")&&YTPlayer.opt.containment.css({position:"relative"}),YTPlayer.opt.containment.prepend(wrapper),YTPlayer.wrapper=wrapper,playerBox.css({opacity:1}),jQuery.browser.mobile||(playerBox.after(overlay),YTPlayer.overlay=overlay),YTPlayer.isBackground||overlay.on("mouseenter",function(){YTPlayer.controlBar.length&&YTPlayer.controlBar.addClass("visible")}).on("mouseleave",function(){YTPlayer.controlBar.length&&YTPlayer.controlBar.removeClass("visible")}),ytp.YTAPIReady)setTimeout(function(){jQuery(document).trigger("YTAPIReady")},100);else{jQuery("#YTAPI").remove();var tag=jQuery("<script></script>").attr({src:jQuery.mbYTPlayer.locationProtocol+"//www.youtube.com/iframe_api?v="+jQuery.mbYTPlayer.version,id:"YTAPI"});jQuery("head").prepend(tag)}if(jQuery.browser.mobile&&!YTPlayer.canPlayOnMobile)return YTPlayer.opt.mobileFallbackImage&&YTPlayer.opt.containment.css({backgroundImage:"url("+YTPlayer.opt.mobileFallbackImage+")",backgroundPosition:"center center",backgroundSize:"cover",backgroundRepeat:"no-repeat"}),$YTPlayer.remove(),void jQuery(document).trigger("YTPUnavailable");jQuery(document).on("YTAPIReady",function(){YTPlayer.isBackground&&ytp.backgroundIsInited||YTPlayer.isInit||(YTPlayer.isBackground&&(ytp.backgroundIsInited=!0),YTPlayer.opt.autoPlay="undefined"==typeof YTPlayer.opt.autoPlay?YTPlayer.isBackground?!0:!1:YTPlayer.opt.autoPlay,YTPlayer.opt.vol=YTPlayer.opt.vol?YTPlayer.opt.vol:100,jQuery.mbYTPlayer.getDataFromAPI(YTPlayer),jQuery(YTPlayer).on("YTPChanged",function(){if(!YTPlayer.isInit){if(YTPlayer.isInit=!0,jQuery.browser.mobile&&YTPlayer.canPlayOnMobile){if(YTPlayer.opt.containment.outerWidth()>jQuery(window).width()){YTPlayer.opt.containment.css({maxWidth:"100%"});var h=.563*YTPlayer.opt.containment.outerWidth();YTPlayer.opt.containment.css({maxHeight:h})}return void new YT.Player(playerID,{videoId:YTPlayer.videoID.toString(),width:"100%",height:h,playerVars:playerVars,events:{onReady:function(a){YTPlayer.player=a.target,playerBox.css({opacity:1}),YTPlayer.wrapper.css({opacity:1})}}})}new YT.Player(playerID,{videoId:YTPlayer.videoID.toString(),playerVars:playerVars,events:{onReady:function(a){YTPlayer.player=a.target,YTPlayer.isReady||(YTPlayer.isReady=YTPlayer.isPlayer&&!YTPlayer.opt.autoPlay?!1:!0,YTPlayer.playerEl=YTPlayer.player.getIframe(),jQuery(YTPlayer.playerEl).unselectable(),$YTPlayer.optimizeDisplay(),YTPlayer.videoID=videoID,jQuery(window).off("resize.YTP_"+YTPlayer.id).on("resize.YTP_"+YTPlayer.id,function(){$YTPlayer.optimizeDisplay()}),jQuery.mbYTPlayer.checkForState(YTPlayer))},onStateChange:function(event){if("function"==typeof event.target.getPlayerState){var state=event.target.getPlayerState();if(YTPlayer.preventTrigger)return void(YTPlayer.preventTrigger=!1);YTPlayer.state=state;var eventType;switch(state){case-1:eventType="YTPUnstarted";break;case 0:eventType="YTPEnd";break;case 1:eventType="YTPPlay",YTPlayer.controlBar.length&&YTPlayer.controlBar.find(".mb_YTPPlaypause").html(jQuery.mbYTPlayer.controls.pause),"undefined"!=typeof _gaq&&eval(YTPlayer.opt.gaTrack)&&_gaq.push(["_trackEvent","YTPlayer","Play",YTPlayer.hasData?YTPlayer.videoData.title:YTPlayer.videoID.toString()]),"undefined"!=typeof ga&&eval(YTPlayer.opt.gaTrack)&&ga("send","event","YTPlayer","play",YTPlayer.hasData?YTPlayer.videoData.title:YTPlayer.videoID.toString());break;case 2:eventType="YTPPause",YTPlayer.controlBar.length&&YTPlayer.controlBar.find(".mb_YTPPlaypause").html(jQuery.mbYTPlayer.controls.play);break;case 3:YTPlayer.player.setPlaybackQuality(YTPlayer.opt.quality),eventType="YTPBuffering",YTPlayer.controlBar.length&&YTPlayer.controlBar.find(".mb_YTPPlaypause").html(jQuery.mbYTPlayer.controls.play);break;case 5:eventType="YTPCued"}var YTPEvent=jQuery.Event(eventType);YTPEvent.time=YTPlayer.currentTime,YTPlayer.canTrigger&&jQuery(YTPlayer).trigger(YTPEvent)}},onPlaybackQualityChange:function(a){var b=a.target.getPlaybackQuality(),c=jQuery.Event("YTPQualityChange");c.quality=b,jQuery(YTPlayer).trigger(c)},onError:function(a){150==a.data&&(console.log("Embedding this video is restricted by Youtube."),YTPlayer.isPlayList&&jQuery(YTPlayer).playNext()),2==a.data&&YTPlayer.isPlayList&&jQuery(YTPlayer).playNext(),"function"==typeof YTPlayer.opt.onError&&YTPlayer.opt.onError($YTPlayer,a)}}})}}))}),$YTPlayer.off("YTPTime.mask"),jQuery.mbYTPlayer.applyMask(YTPlayer)}})},getDataFromAPI:function(a){if(a.videoData=jQuery.mbStorage.get("YTPlayer_data_"+a.videoID),jQuery(a).off("YTPData.YTPlayer").on("YTPData.YTPlayer",function(){if(a.hasData&&a.isPlayer&&!a.opt.autoPlay){var b=a.videoData.thumb_max||a.videoData.thumb_high||a.videoData.thumb_medium;a.opt.containment.css({background:"rgba(0,0,0,0.5) url("+b+") center center",backgroundSize:"cover"}),a.opt.backgroundUrl=b}}),a.videoData)setTimeout(function(){a.opt.ratio="auto"==a.opt.ratio?"16/9":a.opt.ratio,a.dataReceived=!0,jQuery(a).trigger("YTPChanged");var b=jQuery.Event("YTPData");b.prop={};for(var c in a.videoData)b.prop[c]=a.videoData[c];jQuery(a).trigger(b)},500),a.hasData=!0;else if(jQuery.mbYTPlayer.apiKey)jQuery.getJSON(jQuery.mbYTPlayer.locationProtocol+"//www.googleapis.com/youtube/v3/videos?id="+a.videoID+"&key="+jQuery.mbYTPlayer.apiKey+"&part=snippet",function(b){function c(b){a.videoData={},a.videoData.id=a.videoID,a.videoData.channelTitle=b.channelTitle,a.videoData.title=b.title,a.videoData.description=b.description.length<400?b.description:b.description.substring(0,400)+" ...",a.videoData.aspectratio="auto"==a.opt.ratio?"16/9":a.opt.ratio,a.opt.ratio=a.videoData.aspectratio,a.videoData.thumb_max=b.thumbnails.maxres?b.thumbnails.maxres.url:null,a.videoData.thumb_high=b.thumbnails.high?b.thumbnails.high.url:null,a.videoData.thumb_medium=b.thumbnails.medium?b.thumbnails.medium.url:null,jQuery.mbStorage.set("YTPlayer_data_"+a.videoID,a.videoData)}a.dataReceived=!0,jQuery(a).trigger("YTPChanged"),c(b.items[0].snippet),a.hasData=!0;var d=jQuery.Event("YTPData");d.prop={};for(var e in a.videoData)d.prop[e]=a.videoData[e];jQuery(a).trigger(d)});else{if(setTimeout(function(){jQuery(a).trigger("YTPChanged")},50),a.isPlayer&&!a.opt.autoPlay){var b=jQuery.mbYTPlayer.locationProtocol+"//i.ytimg.com/vi/"+a.videoID+"/hqdefault.jpg";a.opt.containment.css({background:"rgba(0,0,0,0.5) url("+b+") center center",backgroundSize:"cover"}),a.opt.backgroundUrl=b}a.videoData=null,a.opt.ratio="auto"==a.opt.ratio?"16/9":a.opt.ratio}!a.isPlayer||a.opt.autoPlay||jQuery.browser.mobile||(a.loading=jQuery("<div/>").addClass("loading").html("Loading").hide(),jQuery(a).append(a.loading),a.loading.fadeIn())},removeStoredData:function(){jQuery.mbStorage.remove()},getVideoData:function(){var a=this.get(0);return a.videoData},getVideoID:function(){var a=this.get(0);return a.videoID||!1},setVideoQuality:function(a){var b=this.get(0);b.player.setPlaybackQuality(a)},playlist:function(a,b,c,d){var e=this,f=e.get(0);return f.isPlayList=!0,b&&(a=jQuery.shuffle(a)),f.videoID||(f.videos=a,f.videoCounter=0,f.videoLength=a.length,jQuery(f).data("property",a[0]),jQuery(f).mb_YTPlayer()),"function"==typeof c&&jQuery(f).one("YTPChanged",function(){c(f)}),jQuery(f).on("YTPEnd",function(){d="undefined"==typeof d?!0:d,jQuery(f).playNext(d)}),e},playNext:function(a){var b=this.get(0);return b.checkForStartAt&&(clearTimeout(b.checkForStartAt),clearInterval(b.getState)),b.videoCounter++,b.videoCounter>=b.videoLength&&a&&(b.videoCounter=0),b.videoCounter<b.videoLength?jQuery(b).changeMovie(b.videos[b.videoCounter]):b.videoCounter--,this},playPrev:function(){var a=this.get(0);return a.checkForStartAt&&(clearInterval(a.checkForStartAt),clearInterval(a.getState)),a.videoCounter--,a.videoCounter<0&&(a.videoCounter=a.videoLength-1),jQuery(a).changeMovie(a.videos[a.videoCounter]),this},playIndex:function(a){var b=this.get(0);return a-=1,b.checkForStartAt&&(clearInterval(b.checkForStartAt),clearInterval(b.getState)),b.videoCounter=a,b.videoCounter>=b.videoLength-1&&(b.videoCounter=b.videoLength-1),jQuery(b).changeMovie(b.videos[b.videoCounter]),this},changeMovie:function(a){var b=this,c=b.get(0);c.opt.startAt=0,c.opt.stopAt=0,c.opt.mask=!1,c.opt.mute=!0,c.hasData=!1,c.hasChanged=!0,c.player.loopTime=void 0,a&&jQuery.extend(c.opt,a),c.videoID=getYTPVideoID(c.opt.videoURL).videoID,"true"==c.opt.loop&&(c.opt.loop=9999),jQuery(c.playerEl).CSSAnimate({opacity:0},200,function(){var a=jQuery.Event("YTPChangeMovie");a.time=c.currentTime,a.videoId=c.videoID,jQuery(c).trigger(a),jQuery(c).YTPGetPlayer().cueVideoByUrl(encodeURI(jQuery.mbYTPlayer.locationProtocol+"//www.youtube.com/v/"+c.videoID),1,c.opt.quality),jQuery(c).optimizeDisplay(),jQuery.mbYTPlayer.checkForState(c),jQuery.mbYTPlayer.getDataFromAPI(c)}),jQuery.mbYTPlayer.applyMask(c)},getPlayer:function(){return jQuery(this).get(0).player},playerDestroy:function(){var a=this.get(0);ytp.YTAPIReady=!0,ytp.backgroundIsInited=!1,a.isInit=!1,a.videoID=null;var b=a.wrapper;return b.remove(),jQuery("#controlBar_"+a.id).remove(),clearInterval(a.checkForStartAt),clearInterval(a.getState),this},fullscreen:function(real){function hideMouse(){YTPlayer.overlay.css({cursor:"none"})}function RunPrefixMethod(a,b){for(var c,d,e=["webkit","moz","ms","o",""],f=0;f<e.length&&!a[c];){if(c=b,""==e[f]&&(c=c.substr(0,1).toLowerCase()+c.substr(1)),c=e[f]+c,d=typeof a[c],"undefined"!=d)return e=[e[f]],"function"==d?a[c]():a[c];f++}}function launchFullscreen(a){RunPrefixMethod(a,"RequestFullScreen")}function cancelFullscreen(){(RunPrefixMethod(document,"FullScreen")||RunPrefixMethod(document,"IsFullScreen"))&&RunPrefixMethod(document,"CancelFullScreen")}var YTPlayer=this.get(0);"undefined"==typeof real&&(real=YTPlayer.opt.realfullscreen),real=eval(real);var controls=jQuery("#controlBar_"+YTPlayer.id),fullScreenBtn=controls.find(".mb_OnlyYT"),videoWrapper=YTPlayer.isSelf?YTPlayer.opt.containment:YTPlayer.wrapper;if(real){var fullscreenchange=jQuery.browser.mozilla?"mozfullscreenchange":jQuery.browser.webkit?"webkitfullscreenchange":"fullscreenchange";jQuery(document).off(fullscreenchange).on(fullscreenchange,function(){var a=RunPrefixMethod(document,"IsFullScreen")||RunPrefixMethod(document,"FullScreen");a?(jQuery(YTPlayer).YTPSetVideoQuality("default"),jQuery(YTPlayer).trigger("YTPFullScreenStart")):(YTPlayer.isAlone=!1,fullScreenBtn.html(jQuery.mbYTPlayer.controls.onlyYT),jQuery(YTPlayer).YTPSetVideoQuality(YTPlayer.opt.quality),videoWrapper.removeClass("YTPFullscreen"),videoWrapper.CSSAnimate({opacity:YTPlayer.opt.opacity},500),videoWrapper.css({zIndex:0}),YTPlayer.isBackground?jQuery("body").after(controls):YTPlayer.wrapper.before(controls),jQuery(window).resize(),jQuery(YTPlayer).trigger("YTPFullScreenEnd"))})}return YTPlayer.isAlone?(jQuery(document).off("mousemove.YTPlayer"),clearTimeout(YTPlayer.hideCursor),YTPlayer.overlay.css({cursor:"auto"}),real?cancelFullscreen():(videoWrapper.CSSAnimate({opacity:YTPlayer.opt.opacity},500),videoWrapper.css({zIndex:0})),fullScreenBtn.html(jQuery.mbYTPlayer.controls.onlyYT),YTPlayer.isAlone=!1):(jQuery(document).on("mousemove.YTPlayer",function(a){YTPlayer.overlay.css({cursor:"auto"}),clearTimeout(YTPlayer.hideCursor),jQuery(a.target).parents().is(".mb_YTPBar")||(YTPlayer.hideCursor=setTimeout(hideMouse,3e3))}),hideMouse(),real?(videoWrapper.css({opacity:0}),videoWrapper.addClass("YTPFullscreen"),launchFullscreen(videoWrapper.get(0)),setTimeout(function(){videoWrapper.CSSAnimate({opacity:1},1e3),YTPlayer.wrapper.append(controls),jQuery(YTPlayer).optimizeDisplay(),YTPlayer.player.seekTo(YTPlayer.player.getCurrentTime()+.1,!0)},500)):videoWrapper.css({zIndex:1e4}).CSSAnimate({opacity:1},1e3),fullScreenBtn.html(jQuery.mbYTPlayer.controls.showSite),YTPlayer.isAlone=!0),this},toggleLoops:function(){var a=this.get(0),b=a.opt;return 1==b.loop?b.loop=0:(b.startAt?a.player.seekTo(b.startAt):a.player.playVideo(),b.loop=1),this},play:function(){var a=this.get(0);if(!a.isReady)return this;a.player.playVideo(),a.wrapper.CSSAnimate({opacity:a.isAlone?1:a.opt.opacity},2e3),jQuery(a.playerEl).CSSAnimate({opacity:1},1e3);var b=jQuery("#controlBar_"+a.id),c=b.find(".mb_YTPPlaypause");return c.html(jQuery.mbYTPlayer.controls.pause),a.state=1,jQuery(a).css("background-image","none"),this},togglePlay:function(a){var b=this.get(0);return 1==b.state?this.YTPPause():this.YTPPlay(),"function"==typeof a&&a(b.state),this},stop:function(){var a=this.get(0),b=jQuery("#controlBar_"+a.id),c=b.find(".mb_YTPPlaypause");return c.html(jQuery.mbYTPlayer.controls.play),a.player.stopVideo(),this},pause:function(){var a=this.get(0);return a.player.pauseVideo(),a.state=2,this},seekTo:function(a){var b=this.get(0);return b.player.seekTo(a,!0),this},setVolume:function(a){var b=this.get(0);return a||b.opt.vol||0!=b.player.getVolume()?!a&&b.player.getVolume()>0||a&&b.opt.vol==a?b.isMute?jQuery(b).YTPUnmute():jQuery(b).YTPMute():(b.opt.vol=a,b.player.setVolume(b.opt.vol),b.volumeBar&&b.volumeBar.length&&b.volumeBar.updateSliderVal(a)):jQuery(b).YTPUnmute(),this},toggleVolume:function(){var a=this.get(0);if(a)return a.player.isMuted()?(jQuery(a).YTPUnmute(),!0):(jQuery(a).YTPMute(),!1)},mute:function(){var a=this.get(0);if(!a.isMute){a.player.mute(),a.isMute=!0,a.player.setVolume(0),a.volumeBar&&a.volumeBar.length&&a.volumeBar.width()>10&&a.volumeBar.updateSliderVal(0);var b=jQuery("#controlBar_"+a.id),c=b.find(".mb_YTPMuteUnmute");c.html(jQuery.mbYTPlayer.controls.unmute),jQuery(a).addClass("isMuted"),a.volumeBar&&a.volumeBar.length&&a.volumeBar.addClass("muted");var d=jQuery.Event("YTPMuted");return d.time=a.currentTime,a.canTrigger&&jQuery(a).trigger(d),this}},unmute:function(){var a=this.get(0);if(a.isMute){a.player.unMute(),a.isMute=!1,a.player.setVolume(a.opt.vol),a.volumeBar&&a.volumeBar.length&&a.volumeBar.updateSliderVal(a.opt.vol>10?a.opt.vol:10);var b=jQuery("#controlBar_"+a.id),c=b.find(".mb_YTPMuteUnmute");c.html(jQuery.mbYTPlayer.controls.mute),jQuery(a).removeClass("isMuted"),a.volumeBar&&a.volumeBar.length&&a.volumeBar.removeClass("muted");var d=jQuery.Event("YTPUnmuted");return d.time=a.currentTime,a.canTrigger&&jQuery(a).trigger(d),this}},applyFilter:function(a,b){return this.each(function(){var c=this;c.filters[a].value=b,c.filtersEnabled&&jQuery(c).YTPEnableFilters()})},applyFilters:function(a){return this.each(function(){var b=this;if(!b.isReady)return void jQuery(b).on("YTPReady",function(){jQuery(b).YTPApplyFilters(a)});for(var c in a)jQuery(b).YTPApplyFilter(c,a[c]);jQuery(b).trigger("YTPFiltersApplied")})},toggleFilter:function(a,b){return this.each(function(){var c=this;c.filters[a].value?c.filters[a].value=0:c.filters[a].value=b,c.filtersEnabled&&jQuery(this).YTPEnableFilters()})},toggleFilters:function(a){return this.each(function(){var b=this;b.filtersEnabled?(jQuery(b).trigger("YTPDisableFilters"),jQuery(b).YTPDisableFilters()):(jQuery(b).YTPEnableFilters(),jQuery(b).trigger("YTPEnableFilters")),"function"==typeof a&&a(b.filtersEnabled)})},disableFilters:function(){return this.each(function(){var a=this,b=jQuery(a.playerEl);b.css("-webkit-filter",""),b.css("filter",""),a.filtersEnabled=!1})},enableFilters:function(){return this.each(function(){var a=this,b=jQuery(a.playerEl),c="";for(var d in a.filters)a.filters[d].value&&(c+=d.replace("_","-")+"("+a.filters[d].value+a.filters[d].unit+") ");b.css("-webkit-filter",c),b.css("filter",c),a.filtersEnabled=!0})},removeFilter:function(a,b){return this.each(function(){var c=this;if("function"==typeof a&&(b=a,a=null),a)jQuery(this).YTPApplyFilter(a,0),"function"==typeof b&&b(a);else for(var d in c.filters)jQuery(this).YTPApplyFilter(d,0),"function"==typeof b&&b(d)})},getFilters:function(){var a=this.get(0);return a.filters},addMask:function(a){var b=this.get(0),c=b.overlay;a||(a=b.actualMask);var d=jQuery("<img/>").attr("src",a).on("load",function(){c.CSSAnimate({opacity:0},500,function(){b.hasMask=!0,d.remove(),c.css({backgroundImage:"url("+a+")",backgroundRepeat:"no-repeat",backgroundPosition:"center center",backgroundSize:"cover"}),c.CSSAnimate({opacity:1},500)})});return this},removeMask:function(){var a=this.get(0),b=a.overlay;return b.CSSAnimate({opacity:0},500,function(){a.hasMask=!1,b.css({backgroundImage:"",backgroundRepeat:"",backgroundPosition:"",backgroundSize:""}),b.CSSAnimate({opacity:1},500)}),this},applyMask:function(a){var b=jQuery(a);if(b.off("YTPTime.mask"),a.opt.mask)if("string"==typeof a.opt.mask)b.YTPAddMask(a.opt.mask),a.actualMask=a.opt.mask;else if("object"==typeof a.opt.mask){for(var c in a.opt.mask)if(a.opt.mask[c]){jQuery("<img/>").attr("src",a.opt.mask[c])}a.opt.mask[0]&&b.YTPAddMask(a.opt.mask[0]),b.on("YTPTime.mask",function(c){for(var d in a.opt.mask)c.time==d&&(a.opt.mask[d]?(b.YTPAddMask(a.opt.mask[d]),a.actualMask=a.opt.mask[d]):b.YTPRemoveMask())})}},toggleMask:function(){var a=this.get(0),b=$(a);return a.hasMask?b.YTPRemoveMask():b.YTPAddMask(),this},manageProgress:function(){var a=this.get(0),b=jQuery("#controlBar_"+a.id),c=b.find(".mb_YTPProgress"),d=b.find(".mb_YTPLoaded"),e=b.find(".mb_YTPseekbar"),f=c.outerWidth(),g=Math.floor(a.player.getCurrentTime()),h=Math.floor(a.player.getDuration()),i=g*f/h,j=0,k=100*a.player.getVideoLoadedFraction();return d.css({left:j,width:k+"%"}),e.css({left:0,width:i}),{totalTime:h,currentTime:g}},buildControls:function(YTPlayer){var data=YTPlayer.opt;if(data.showYTLogo=data.showYTLogo||data.printUrl,!jQuery("#controlBar_"+YTPlayer.id).length){YTPlayer.controlBar=jQuery("<span/>").attr("id","controlBar_"+YTPlayer.id).addClass("mb_YTPBar").css({whiteSpace:"noWrap",position:YTPlayer.isBackground?"fixed":"absolute",zIndex:YTPlayer.isBackground?1e4:1e3}).hide();var buttonBar=jQuery("<div/>").addClass("buttonBar"),playpause=jQuery("<span>"+jQuery.mbYTPlayer.controls.play+"</span>").addClass("mb_YTPPlaypause ytpicon").click(function(){1==YTPlayer.player.getPlayerState()?jQuery(YTPlayer).YTPPause():jQuery(YTPlayer).YTPPlay()}),MuteUnmute=jQuery("<span>"+jQuery.mbYTPlayer.controls.mute+"</span>").addClass("mb_YTPMuteUnmute ytpicon").click(function(){0==YTPlayer.player.getVolume()?jQuery(YTPlayer).YTPUnmute():jQuery(YTPlayer).YTPMute()}),volumeBar=jQuery("<div/>").addClass("mb_YTPVolumeBar").css({display:"inline-block"});YTPlayer.volumeBar=volumeBar;var idx=jQuery("<span/>").addClass("mb_YTPTime"),vURL=data.videoURL?data.videoURL:"";vURL.indexOf("http")<0&&(vURL=jQuery.mbYTPlayer.locationProtocol+"//www.youtube.com/watch?v="+data.videoURL);var movieUrl=jQuery("<span/>").html(jQuery.mbYTPlayer.controls.ytLogo).addClass("mb_YTPUrl ytpicon").attr("title","view on YouTube").on("click",function(){window.open(vURL,"viewOnYT")}),onlyVideo=jQuery("<span/>").html(jQuery.mbYTPlayer.controls.onlyYT).addClass("mb_OnlyYT ytpicon").on("click",function(){jQuery(YTPlayer).YTPFullscreen(data.realfullscreen)}),progressBar=jQuery("<div/>").addClass("mb_YTPProgress").css("position","absolute").click(function(a){timeBar.css({width:a.clientX-timeBar.offset().left}),YTPlayer.timeW=a.clientX-timeBar.offset().left,YTPlayer.controlBar.find(".mb_YTPLoaded").css({width:0});var b=Math.floor(YTPlayer.player.getDuration());YTPlayer["goto"]=timeBar.outerWidth()*b/progressBar.outerWidth(),YTPlayer.player.seekTo(parseFloat(YTPlayer["goto"]),!0),YTPlayer.controlBar.find(".mb_YTPLoaded").css({width:0})}),loadedBar=jQuery("<div/>").addClass("mb_YTPLoaded").css("position","absolute"),timeBar=jQuery("<div/>").addClass("mb_YTPseekbar").css("position","absolute");progressBar.append(loadedBar).append(timeBar),buttonBar.append(playpause).append(MuteUnmute).append(volumeBar).append(idx),data.showYTLogo&&buttonBar.append(movieUrl),(YTPlayer.isBackground||eval(YTPlayer.opt.realfullscreen)&&!YTPlayer.isBackground)&&buttonBar.append(onlyVideo),YTPlayer.controlBar.append(buttonBar).append(progressBar),YTPlayer.isBackground?jQuery("body").after(YTPlayer.controlBar):(YTPlayer.controlBar.addClass("inlinePlayer"),YTPlayer.wrapper.before(YTPlayer.controlBar)),volumeBar.simpleSlider({initialval:YTPlayer.opt.vol,scale:100,orientation:"h",callback:function(a){0==a.value?jQuery(YTPlayer).YTPMute():jQuery(YTPlayer).YTPUnmute(),YTPlayer.player.setVolume(a.value),YTPlayer.isMute||(YTPlayer.opt.vol=a.value)}})}},checkForState:function(YTPlayer){var interval=YTPlayer.opt.showControls?100:400;return clearInterval(YTPlayer.getState),jQuery.contains(document,YTPlayer)?(jQuery.mbYTPlayer.checkForStart(YTPlayer),void(YTPlayer.getState=setInterval(function(){var prog=jQuery(YTPlayer).YTPManageProgress(),$YTPlayer=jQuery(YTPlayer),data=YTPlayer.opt,startAt=YTPlayer.opt.startAt?YTPlayer.opt.startAt:1,stopAt=YTPlayer.opt.stopAt>YTPlayer.opt.startAt?YTPlayer.opt.stopAt:0;if(stopAt=stopAt<YTPlayer.player.getDuration()?stopAt:0,YTPlayer.currentTime!=prog.currentTime){var YTPEvent=jQuery.Event("YTPTime");YTPEvent.time=YTPlayer.currentTime,jQuery(YTPlayer).trigger(YTPEvent)}if(YTPlayer.currentTime=prog.currentTime,YTPlayer.totalTime=YTPlayer.player.getDuration(),0==YTPlayer.player.getVolume()?$YTPlayer.addClass("isMuted"):$YTPlayer.removeClass("isMuted"),YTPlayer.opt.showControls&&(prog.totalTime?YTPlayer.controlBar.find(".mb_YTPTime").html(jQuery.mbYTPlayer.formatTime(prog.currentTime)+" / "+jQuery.mbYTPlayer.formatTime(prog.totalTime)):YTPlayer.controlBar.find(".mb_YTPTime").html("-- : -- / -- : --")),eval(YTPlayer.opt.stopMovieOnBlur)&&(document.hasFocus()?document.hasFocus()&&!YTPlayer.hasFocus&&-1!=YTPlayer.state&&0!=YTPlayer.state&&(YTPlayer.hasFocus=!0,$YTPlayer.YTPPlay()):1==YTPlayer.state&&(YTPlayer.hasFocus=!1,$YTPlayer.YTPPause())),YTPlayer.controlBar.length&&YTPlayer.controlBar.outerWidth()<=400&&!YTPlayer.isCompact?(YTPlayer.controlBar.addClass("compact"),YTPlayer.isCompact=!0,!YTPlayer.isMute&&YTPlayer.volumeBar&&YTPlayer.volumeBar.updateSliderVal(YTPlayer.opt.vol)):YTPlayer.controlBar.length&&YTPlayer.controlBar.outerWidth()>400&&YTPlayer.isCompact&&(YTPlayer.controlBar.removeClass("compact"),YTPlayer.isCompact=!1,!YTPlayer.isMute&&YTPlayer.volumeBar&&YTPlayer.volumeBar.updateSliderVal(YTPlayer.opt.vol)),1==YTPlayer.player.getPlayerState()&&(parseFloat(YTPlayer.player.getDuration()-1.5)<YTPlayer.player.getCurrentTime()||stopAt>0&&parseFloat(YTPlayer.player.getCurrentTime())>stopAt)){if(YTPlayer.isEnded)return;if(YTPlayer.isEnded=!0,setTimeout(function(){YTPlayer.isEnded=!1},1e3),YTPlayer.isPlayList){if(!data.loop||data.loop>0&&YTPlayer.player.loopTime===data.loop-1){YTPlayer.player.loopTime=void 0,clearInterval(YTPlayer.getState);var YTPEnd=jQuery.Event("YTPEnd");return YTPEnd.time=YTPlayer.currentTime,void jQuery(YTPlayer).trigger(YTPEnd)}}else if(!data.loop||data.loop>0&&YTPlayer.player.loopTime===data.loop-1)return YTPlayer.player.loopTime=void 0,YTPlayer.preventTrigger=!0,YTPlayer.state=2,jQuery(YTPlayer).YTPPause(),void YTPlayer.wrapper.CSSAnimate({opacity:0},500,function(){YTPlayer.controlBar.length&&YTPlayer.controlBar.find(".mb_YTPPlaypause").html(jQuery.mbYTPlayer.controls.play);var a=jQuery.Event("YTPEnd");a.time=YTPlayer.currentTime,jQuery(YTPlayer).trigger(a),YTPlayer.player.seekTo(startAt,!0),YTPlayer.isBackground||YTPlayer.opt.containment.css({background:"rgba(0,0,0,0.5) url("+YTPlayer.opt.backgroundUrl+") center center",backgroundSize:"cover"})});YTPlayer.player.loopTime=YTPlayer.player.loopTime?++YTPlayer.player.loopTime:1,startAt=startAt||1,YTPlayer.preventTrigger=!0,YTPlayer.state=2,jQuery(YTPlayer).YTPPause(),YTPlayer.player.seekTo(startAt,!0),$YTPlayer.YTPPlay()}},interval))):(jQuery(YTPlayer).YTPPlayerDestroy(),clearInterval(YTPlayer.getState),void clearInterval(YTPlayer.checkForStartAt))},getTime:function(){var a=this.get(0);return jQuery.mbYTPlayer.formatTime(a.currentTime)},getTotalTime:function(){var a=this.get(0);return jQuery.mbYTPlayer.formatTime(a.totalTime)},checkForStart:function(a){var b=jQuery(a);if(!jQuery.contains(document,a))return void jQuery(a).YTPPlayerDestroy();if(a.preventTrigger=!0,a.state=2,jQuery(a).YTPPause(),jQuery(a).muteYTPVolume(),jQuery("#controlBar_"+a.id).remove(),a.controlBar=!1,a.opt.showControls&&jQuery.mbYTPlayer.buildControls(a),a.opt.addRaster){var c="dot"==a.opt.addRaster?"raster-dot":"raster";a.overlay.addClass(a.isRetina?c+" retina":c)}else a.overlay.removeClass(function(a,b){var c=b.split(" "),d=[];return jQuery.each(c,function(a,b){/raster.*/.test(b)&&d.push(b)}),d.push("retina"),d.join(" ")});var d=a.opt.startAt?a.opt.startAt:1;a.player.playVideo(),a.player.seekTo(d,!0),a.checkForStartAt=setInterval(function(){jQuery(a).YTPMute();var c=a.player.getVideoLoadedFraction()>=d/a.player.getDuration();if(a.player.getDuration()>0&&a.player.getCurrentTime()>=d&&c){clearInterval(a.checkForStartAt),"function"==typeof a.opt.onReady&&a.opt.onReady(a),a.isReady=!0;var e=jQuery.Event("YTPReady");if(e.time=a.currentTime,jQuery(a).trigger(e),a.preventTrigger=!0,a.state=2,jQuery(a).YTPPause(),a.opt.mute||jQuery(a).YTPUnmute(),a.canTrigger=!0,a.opt.autoPlay){var f=jQuery.Event("YTPStart");f.time=a.currentTime,jQuery(a).trigger(f),b.css("background-image","none"),jQuery(a.playerEl).CSSAnimate({opacity:1},1e3),b.YTPPlay(),a.wrapper.CSSAnimate({opacity:a.isAlone?1:a.opt.opacity},1e3),jQuery.browser.safari&&(a.safariPlay=setInterval(function(){1!=a.state?b.YTPPlay():clearInterval(a.safariPlay)},10)),b.on("YTPReady",function(){b.YTPPlay()})}else a.player.pauseVideo(),a.isPlayer||(jQuery(a.playerEl).CSSAnimate({opacity:1},500),a.wrapper.CSSAnimate({opacity:a.isAlone?1:a.opt.opacity},500)),a.controlBar.length&&a.controlBar.find(".mb_YTPPlaypause").html(jQuery.mbYTPlayer.controls.play);a.isPlayer&&!a.opt.autoPlay&&a.loading&&a.loading.length&&(a.loading.html("Ready"),setTimeout(function(){a.loading.fadeOut()},100)),a.controlBar&&a.controlBar.length&&a.controlBar.slideDown(1e3)}else jQuery.browser.safari&&(a.player.playVideo(),d>=0&&a.player.seekTo(d,!0))},1)},setAlign:function(a){var b=this;b.optimizeDisplay(a)},getAlign:function(){var a=this.get(0);return a.opt.align},formatTime:function(a){var b=Math.floor(a/60),c=Math.floor(a-60*b);return(9>=b?"0"+b:b)+" : "+(9>=c?"0"+c:c)}},jQuery.fn.optimizeDisplay=function(a){var b=this.get(0),c=jQuery(b.playerEl),d={};b.opt.align=a||b.opt.align,b.opt.align="undefined "!=typeof b.opt.align?b.opt.align:"center,center";var e=b.opt.align.split(",");if(b.opt.optimizeDisplay){var f={},g=b.wrapper;f.width=g.outerWidth(),f.height=g.outerHeight(),d.width=f.width,d.height="16/9"==b.opt.ratio?Math.ceil(f.width*(9/16)):Math.ceil(.75*f.width),d.width=f.width,d.height="16/9"==b.opt.ratio?Math.ceil(f.width*(9/16)):Math.ceil(.75*f.width),d.marginTop=-((d.height-f.height)/2),d.marginLeft=0;var h=d.height<f.height;h&&(d.height=f.height,d.width="16/9"==b.opt.ratio?Math.floor(f.height*(16/9)):Math.floor(f.height*(4/3)),d.marginTop=0,d.marginLeft=-((d.width-f.width)/2));for(var i in e){var j=e[i].trim();
switch(j){case"top":d.marginTop=h?-((d.height-f.height)/2):0;break;case"bottom":d.marginTop=h?0:-(d.height-f.height);break;case"left":d.marginLeft=0;break;case"right":d.marginLeft=h?-(d.width-f.width):0}}}else d.width="100%",d.height="100%",d.marginTop=0,d.marginLeft=0;c.css({width:d.width,height:d.height,marginTop:d.marginTop,marginLeft:d.marginLeft})},jQuery.shuffle=function(a){for(var b=a.slice(),c=b.length,d=c;d--;){var e=parseInt(Math.random()*c),f=b[d];b[d]=b[e],b[e]=f}return b},jQuery.fn.unselectable=function(){return this.each(function(){jQuery(this).css({"-moz-user-select":"none","-webkit-user-select":"none","user-select":"none"}).attr("unselectable","on")})},jQuery.fn.YTPlayer=jQuery.mbYTPlayer.buildPlayer,jQuery.fn.YTPGetPlayer=jQuery.mbYTPlayer.getPlayer,jQuery.fn.YTPGetVideoID=jQuery.mbYTPlayer.getVideoID,jQuery.fn.YTPChangeMovie=jQuery.mbYTPlayer.changeMovie,jQuery.fn.YTPPlayerDestroy=jQuery.mbYTPlayer.playerDestroy,jQuery.fn.YTPPlay=jQuery.mbYTPlayer.play,jQuery.fn.YTPTogglePlay=jQuery.mbYTPlayer.togglePlay,jQuery.fn.YTPStop=jQuery.mbYTPlayer.stop,jQuery.fn.YTPPause=jQuery.mbYTPlayer.pause,jQuery.fn.YTPSeekTo=jQuery.mbYTPlayer.seekTo,jQuery.fn.YTPlaylist=jQuery.mbYTPlayer.playlist,jQuery.fn.YTPPlayNext=jQuery.mbYTPlayer.playNext,jQuery.fn.YTPPlayPrev=jQuery.mbYTPlayer.playPrev,jQuery.fn.YTPPlayIndex=jQuery.mbYTPlayer.playIndex,jQuery.fn.YTPMute=jQuery.mbYTPlayer.mute,jQuery.fn.YTPUnmute=jQuery.mbYTPlayer.unmute,jQuery.fn.YTPToggleVolume=jQuery.mbYTPlayer.toggleVolume,jQuery.fn.YTPSetVolume=jQuery.mbYTPlayer.setVolume,jQuery.fn.YTPGetVideoData=jQuery.mbYTPlayer.getVideoData,jQuery.fn.YTPFullscreen=jQuery.mbYTPlayer.fullscreen,jQuery.fn.YTPToggleLoops=jQuery.mbYTPlayer.toggleLoops,jQuery.fn.YTPSetVideoQuality=jQuery.mbYTPlayer.setVideoQuality,jQuery.fn.YTPManageProgress=jQuery.mbYTPlayer.manageProgress,jQuery.fn.YTPApplyFilter=jQuery.mbYTPlayer.applyFilter,jQuery.fn.YTPApplyFilters=jQuery.mbYTPlayer.applyFilters,jQuery.fn.YTPToggleFilter=jQuery.mbYTPlayer.toggleFilter,jQuery.fn.YTPToggleFilters=jQuery.mbYTPlayer.toggleFilters,jQuery.fn.YTPRemoveFilter=jQuery.mbYTPlayer.removeFilter,jQuery.fn.YTPDisableFilters=jQuery.mbYTPlayer.disableFilters,jQuery.fn.YTPEnableFilters=jQuery.mbYTPlayer.enableFilters,jQuery.fn.YTPGetFilters=jQuery.mbYTPlayer.getFilters,jQuery.fn.YTPGetTime=jQuery.mbYTPlayer.getTime,jQuery.fn.YTPGetTotalTime=jQuery.mbYTPlayer.getTotalTime,jQuery.fn.YTPAddMask=jQuery.mbYTPlayer.addMask,jQuery.fn.YTPRemoveMask=jQuery.mbYTPlayer.removeMask,jQuery.fn.YTPToggleMask=jQuery.mbYTPlayer.toggleMask,jQuery.fn.YTPSetAlign=jQuery.mbYTPlayer.setAlign,jQuery.fn.YTPGetAlign=jQuery.mbYTPlayer.getAlign,jQuery.fn.mb_YTPlayer=jQuery.mbYTPlayer.buildPlayer,jQuery.fn.playNext=jQuery.mbYTPlayer.playNext,jQuery.fn.playPrev=jQuery.mbYTPlayer.playPrev,jQuery.fn.changeMovie=jQuery.mbYTPlayer.changeMovie,jQuery.fn.getVideoID=jQuery.mbYTPlayer.getVideoID,jQuery.fn.getPlayer=jQuery.mbYTPlayer.getPlayer,jQuery.fn.playerDestroy=jQuery.mbYTPlayer.playerDestroy,jQuery.fn.fullscreen=jQuery.mbYTPlayer.fullscreen,jQuery.fn.buildYTPControls=jQuery.mbYTPlayer.buildControls,jQuery.fn.playYTP=jQuery.mbYTPlayer.play,jQuery.fn.toggleLoops=jQuery.mbYTPlayer.toggleLoops,jQuery.fn.stopYTP=jQuery.mbYTPlayer.stop,jQuery.fn.pauseYTP=jQuery.mbYTPlayer.pause,jQuery.fn.seekToYTP=jQuery.mbYTPlayer.seekTo,jQuery.fn.muteYTPVolume=jQuery.mbYTPlayer.mute,jQuery.fn.unmuteYTPVolume=jQuery.mbYTPlayer.unmute,jQuery.fn.setYTPVolume=jQuery.mbYTPlayer.setVolume,jQuery.fn.setVideoQuality=jQuery.mbYTPlayer.setVideoQuality,jQuery.fn.manageYTPProgress=jQuery.mbYTPlayer.manageProgress,jQuery.fn.YTPGetDataFromFeed=jQuery.mbYTPlayer.getVideoData}(jQuery,ytp),jQuery.support.CSStransition=function(){var a=document.body||document.documentElement,b=a.style;return void 0!==b.transition||void 0!==b.WebkitTransition||void 0!==b.MozTransition||void 0!==b.MsTransition||void 0!==b.OTransition}(),jQuery.CSS={name:"mb.CSSAnimate",author:"Matteo Bicocchi",version:"2.0.0",transitionEnd:"transitionEnd",sfx:"",filters:{blur:{min:0,max:100,unit:"px"},brightness:{min:0,max:400,unit:"%"},contrast:{min:0,max:400,unit:"%"},grayscale:{min:0,max:100,unit:"%"},hueRotate:{min:0,max:360,unit:"deg"},invert:{min:0,max:100,unit:"%"},saturate:{min:0,max:400,unit:"%"},sepia:{min:0,max:100,unit:"%"}},normalizeCss:function(a){var b=jQuery.extend(!0,{},a);jQuery.browser.webkit||jQuery.browser.opera?jQuery.CSS.sfx="-webkit-":jQuery.browser.mozilla?jQuery.CSS.sfx="-moz-":jQuery.browser.msie&&(jQuery.CSS.sfx="-ms-");for(var c in b){"transform"===c&&(b[jQuery.CSS.sfx+"transform"]=b[c],delete b[c]),"transform-origin"===c&&(b[jQuery.CSS.sfx+"transform-origin"]=a[c],delete b[c]),"filter"!==c||jQuery.browser.mozilla||(b[jQuery.CSS.sfx+"filter"]=a[c],delete b[c]),"blur"===c&&setFilter(b,"blur",a[c]),"brightness"===c&&setFilter(b,"brightness",a[c]),"contrast"===c&&setFilter(b,"contrast",a[c]),"grayscale"===c&&setFilter(b,"grayscale",a[c]),"hueRotate"===c&&setFilter(b,"hueRotate",a[c]),"invert"===c&&setFilter(b,"invert",a[c]),"saturate"===c&&setFilter(b,"saturate",a[c]),"sepia"===c&&setFilter(b,"sepia",a[c]);var d="";"x"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" translateX("+setUnit(a[c],"px")+")",delete b[c]),"y"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" translateY("+setUnit(a[c],"px")+")",delete b[c]),"z"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" translateZ("+setUnit(a[c],"px")+")",delete b[c]),"rotate"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" rotate("+setUnit(a[c],"deg")+")",delete b[c]),"rotateX"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" rotateX("+setUnit(a[c],"deg")+")",delete b[c]),"rotateY"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" rotateY("+setUnit(a[c],"deg")+")",delete b[c]),"rotateZ"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" rotateZ("+setUnit(a[c],"deg")+")",delete b[c]),"scale"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" scale("+setUnit(a[c],"")+")",delete b[c]),"scaleX"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" scaleX("+setUnit(a[c],"")+")",delete b[c]),"scaleY"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" scaleY("+setUnit(a[c],"")+")",delete b[c]),"scaleZ"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" scaleZ("+setUnit(a[c],"")+")",delete b[c]),"skew"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" skew("+setUnit(a[c],"deg")+")",delete b[c]),"skewX"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" skewX("+setUnit(a[c],"deg")+")",delete b[c]),"skewY"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" skewY("+setUnit(a[c],"deg")+")",delete b[c]),"perspective"===c&&(d=jQuery.CSS.sfx+"transform",b[d]=b[d]||"",b[d]+=" perspective("+setUnit(a[c],"px")+")",delete b[c])}return b},getProp:function(a){var b=[];for(var c in a)b.indexOf(c)<0&&b.push(uncamel(c));return b.join(",")},animate:function(a,b,c,d,e){return this.each(function(){function f(){g.called=!0,g.CSSAIsRunning=!1,h.off(jQuery.CSS.transitionEnd+"."+g.id),clearTimeout(g.timeout),h.css(jQuery.CSS.sfx+"transition",""),"function"==typeof e&&e.apply(g),"function"==typeof g.CSSqueue&&(g.CSSqueue(),g.CSSqueue=null)}var g=this,h=jQuery(this);g.id=g.id||"CSSA_"+(new Date).getTime();var i=i||{type:"noEvent"};if(g.CSSAIsRunning&&g.eventType==i.type&&!jQuery.browser.msie&&jQuery.browser.version<=9)return void(g.CSSqueue=function(){h.CSSAnimate(a,b,c,d,e)});if(g.CSSqueue=null,g.eventType=i.type,0!==h.length&&a){if(a=jQuery.normalizeCss(a),g.CSSAIsRunning=!0,"function"==typeof b&&(e=b,b=jQuery.fx.speeds._default),"function"==typeof c&&(d=c,c=0),"string"==typeof c&&(e=c,c=0),"function"==typeof d&&(e=d,d="cubic-bezier(0.65,0.03,0.36,0.72)"),"string"==typeof b)for(var j in jQuery.fx.speeds){if(b==j){b=jQuery.fx.speeds[j];break}b=jQuery.fx.speeds._default}if(b||(b=jQuery.fx.speeds._default),"string"==typeof e&&(d=e,e=null),!jQuery.support.CSStransition){for(var k in a){if("transform"===k&&delete a[k],"filter"===k&&delete a[k],"transform-origin"===k&&delete a[k],"auto"===a[k]&&delete a[k],"x"===k){var l=a[k],m="left";a[m]=l,delete a[k]}if("y"===k){var l=a[k],m="top";a[m]=l,delete a[k]}("-ms-transform"===k||"-ms-filter"===k)&&delete a[k]}return void h.delay(c).animate(a,b,e)}var n={"default":"ease","in":"ease-in",out:"ease-out","in-out":"ease-in-out",snap:"cubic-bezier(0,1,.5,1)",easeOutCubic:"cubic-bezier(.215,.61,.355,1)",easeInOutCubic:"cubic-bezier(.645,.045,.355,1)",easeInCirc:"cubic-bezier(.6,.04,.98,.335)",easeOutCirc:"cubic-bezier(.075,.82,.165,1)",easeInOutCirc:"cubic-bezier(.785,.135,.15,.86)",easeInExpo:"cubic-bezier(.95,.05,.795,.035)",easeOutExpo:"cubic-bezier(.19,1,.22,1)",easeInOutExpo:"cubic-bezier(1,0,0,1)",easeInQuad:"cubic-bezier(.55,.085,.68,.53)",easeOutQuad:"cubic-bezier(.25,.46,.45,.94)",easeInOutQuad:"cubic-bezier(.455,.03,.515,.955)",easeInQuart:"cubic-bezier(.895,.03,.685,.22)",easeOutQuart:"cubic-bezier(.165,.84,.44,1)",easeInOutQuart:"cubic-bezier(.77,0,.175,1)",easeInQuint:"cubic-bezier(.755,.05,.855,.06)",easeOutQuint:"cubic-bezier(.23,1,.32,1)",easeInOutQuint:"cubic-bezier(.86,0,.07,1)",easeInSine:"cubic-bezier(.47,0,.745,.715)",easeOutSine:"cubic-bezier(.39,.575,.565,1)",easeInOutSine:"cubic-bezier(.445,.05,.55,.95)",easeInBack:"cubic-bezier(.6,-.28,.735,.045)",easeOutBack:"cubic-bezier(.175, .885,.32,1.275)",easeInOutBack:"cubic-bezier(.68,-.55,.265,1.55)"};n[d]&&(d=n[d]),h.off(jQuery.CSS.transitionEnd+"."+g.id);var o=jQuery.CSS.getProp(a),p={};jQuery.extend(p,a),p[jQuery.CSS.sfx+"transition-property"]=o,p[jQuery.CSS.sfx+"transition-duration"]=b+"ms",p[jQuery.CSS.sfx+"transition-delay"]=c+"ms",p[jQuery.CSS.sfx+"transition-timing-function"]=d,setTimeout(function(){h.one(jQuery.CSS.transitionEnd+"."+g.id,f),h.css(p)},1),g.timeout=setTimeout(function(){return g.called||!e?(g.called=!1,void(g.CSSAIsRunning=!1)):(h.css(jQuery.CSS.sfx+"transition",""),e.apply(g),g.CSSAIsRunning=!1,void("function"==typeof g.CSSqueue&&(g.CSSqueue(),g.CSSqueue=null)))},b+c+10)}})}},jQuery.fn.CSSAnimate=jQuery.CSS.animate,jQuery.normalizeCss=jQuery.CSS.normalizeCss,jQuery.fn.css3=function(a){return this.each(function(){var b=jQuery(this),c=jQuery.normalizeCss(a);b.css(c)})};var nAgt=navigator.userAgent;if(!jQuery.browser){jQuery.browser={},jQuery.browser.mozilla=!1,jQuery.browser.webkit=!1,jQuery.browser.opera=!1,jQuery.browser.safari=!1,jQuery.browser.chrome=!1,jQuery.browser.androidStock=!1,jQuery.browser.msie=!1,jQuery.browser.ua=nAgt,jQuery.browser.name=navigator.appName,jQuery.browser.fullVersion=""+parseFloat(navigator.appVersion),jQuery.browser.majorVersion=parseInt(navigator.appVersion,10);var nameOffset,verOffset,ix;if(-1!=(verOffset=nAgt.indexOf("Opera")))jQuery.browser.opera=!0,jQuery.browser.name="Opera",jQuery.browser.fullVersion=nAgt.substring(verOffset+6),-1!=(verOffset=nAgt.indexOf("Version"))&&(jQuery.browser.fullVersion=nAgt.substring(verOffset+8));else if(-1!=(verOffset=nAgt.indexOf("OPR")))jQuery.browser.opera=!0,jQuery.browser.name="Opera",jQuery.browser.fullVersion=nAgt.substring(verOffset+4);else if(-1!=(verOffset=nAgt.indexOf("MSIE")))jQuery.browser.msie=!0,jQuery.browser.name="Microsoft Internet Explorer",jQuery.browser.fullVersion=nAgt.substring(verOffset+5);else if(-1!=nAgt.indexOf("Trident")||-1!=nAgt.indexOf("Edge")){jQuery.browser.msie=!0,jQuery.browser.name="Microsoft Internet Explorer";var start=nAgt.indexOf("rv:")+3,end=start+4;jQuery.browser.fullVersion=nAgt.substring(start,end)}else-1!=(verOffset=nAgt.indexOf("Chrome"))?(jQuery.browser.webkit=!0,jQuery.browser.chrome=!0,jQuery.browser.name="Chrome",jQuery.browser.fullVersion=nAgt.substring(verOffset+7)):nAgt.indexOf("mozilla/5.0")>-1&&nAgt.indexOf("android ")>-1&&nAgt.indexOf("applewebkit")>-1&&!(nAgt.indexOf("chrome")>-1)?(verOffset=nAgt.indexOf("Chrome"),jQuery.browser.webkit=!0,jQuery.browser.androidStock=!0,jQuery.browser.name="androidStock",jQuery.browser.fullVersion=nAgt.substring(verOffset+7)):-1!=(verOffset=nAgt.indexOf("Safari"))?(jQuery.browser.webkit=!0,jQuery.browser.safari=!0,jQuery.browser.name="Safari",jQuery.browser.fullVersion=nAgt.substring(verOffset+7),-1!=(verOffset=nAgt.indexOf("Version"))&&(jQuery.browser.fullVersion=nAgt.substring(verOffset+8))):-1!=(verOffset=nAgt.indexOf("AppleWebkit"))?(jQuery.browser.webkit=!0,jQuery.browser.safari=!0,jQuery.browser.name="Safari",jQuery.browser.fullVersion=nAgt.substring(verOffset+7),-1!=(verOffset=nAgt.indexOf("Version"))&&(jQuery.browser.fullVersion=nAgt.substring(verOffset+8))):-1!=(verOffset=nAgt.indexOf("Firefox"))?(jQuery.browser.mozilla=!0,jQuery.browser.name="Firefox",jQuery.browser.fullVersion=nAgt.substring(verOffset+8)):(nameOffset=nAgt.lastIndexOf(" ")+1)<(verOffset=nAgt.lastIndexOf("/"))&&(jQuery.browser.name=nAgt.substring(nameOffset,verOffset),jQuery.browser.fullVersion=nAgt.substring(verOffset+1),jQuery.browser.name.toLowerCase()==jQuery.browser.name.toUpperCase()&&(jQuery.browser.name=navigator.appName));-1!=(ix=jQuery.browser.fullVersion.indexOf(";"))&&(jQuery.browser.fullVersion=jQuery.browser.fullVersion.substring(0,ix)),-1!=(ix=jQuery.browser.fullVersion.indexOf(" "))&&(jQuery.browser.fullVersion=jQuery.browser.fullVersion.substring(0,ix)),jQuery.browser.majorVersion=parseInt(""+jQuery.browser.fullVersion,10),isNaN(jQuery.browser.majorVersion)&&(jQuery.browser.fullVersion=""+parseFloat(navigator.appVersion),jQuery.browser.majorVersion=parseInt(navigator.appVersion,10)),jQuery.browser.version=jQuery.browser.majorVersion}jQuery.browser.android=/Android/i.test(nAgt),jQuery.browser.blackberry=/BlackBerry|BB|PlayBook/i.test(nAgt),jQuery.browser.ios=/iPhone|iPad|iPod|webOS/i.test(nAgt),jQuery.browser.operaMobile=/Opera Mini/i.test(nAgt),jQuery.browser.windowsMobile=/IEMobile|Windows Phone/i.test(nAgt),jQuery.browser.kindle=/Kindle|Silk/i.test(nAgt),jQuery.browser.mobile=jQuery.browser.android||jQuery.browser.blackberry||jQuery.browser.ios||jQuery.browser.windowsMobile||jQuery.browser.operaMobile||jQuery.browser.kindle,jQuery.isMobile=jQuery.browser.mobile,jQuery.isTablet=jQuery.browser.mobile&&jQuery(window).width()>765,jQuery.isAndroidDefault=jQuery.browser.android&&!/chrome/i.test(nAgt),!function(a){var b=(/iphone|ipod|ipad|android|ie|blackberry|fennec/.test(navigator.userAgent.toLowerCase()),"ontouchstart"in window||window.navigator&&window.navigator.msPointerEnabled&&window.MSGesture||window.DocumentTouch&&document instanceof DocumentTouch||!1);a.simpleSlider={defaults:{initialval:0,scale:100,orientation:"h",readonly:!1,callback:!1},events:{start:b?"touchstart":"mousedown",end:b?"touchend":"mouseup",move:b?"touchmove":"mousemove"},init:function(c){return this.each(function(){var d=this,e=a(d);e.addClass("simpleSlider"),d.opt={},a.extend(d.opt,a.simpleSlider.defaults,c),a.extend(d.opt,e.data());var f="h"==d.opt.orientation?"horizontal":"vertical",g=a("<div/>").addClass("level").addClass(f);e.prepend(g),d.level=g,e.css({cursor:"default"}),"auto"==d.opt.scale&&(d.opt.scale=a(d).outerWidth()),e.updateSliderVal(),d.opt.readonly||(e.on(a.simpleSlider.events.start,function(a){b&&(a=a.changedTouches[0]),d.canSlide=!0,e.updateSliderVal(a),e.css({cursor:"col-resize"}),a.preventDefault(),a.stopPropagation()}),a(document).on(a.simpleSlider.events.move,function(c){b&&(c=c.changedTouches[0]),d.canSlide&&(a(document).css({cursor:"default"}),e.updateSliderVal(c),c.preventDefault(),c.stopPropagation())}).on(a.simpleSlider.events.end,function(){a(document).css({cursor:"auto"}),d.canSlide=!1,e.css({cursor:"auto"})}))})},updateSliderVal:function(b){function c(a,b){return Math.floor(100*a/b)}var d=this,e=d.get(0);if(e.opt){e.opt.initialval="number"==typeof e.opt.initialval?e.opt.initialval:e.opt.initialval(e);var f=a(e).outerWidth(),g=a(e).outerHeight();e.x="object"==typeof b?b.clientX+document.body.scrollLeft-d.offset().left:"number"==typeof b?b*f/e.opt.scale:e.opt.initialval*f/e.opt.scale,e.y="object"==typeof b?b.clientY+document.body.scrollTop-d.offset().top:"number"==typeof b?(e.opt.scale-e.opt.initialval-b)*g/e.opt.scale:e.opt.initialval*g/e.opt.scale,e.y=d.outerHeight()-e.y,e.scaleX=e.x*e.opt.scale/f,e.scaleY=e.y*e.opt.scale/g,e.outOfRangeX=e.scaleX>e.opt.scale?e.scaleX-e.opt.scale:e.scaleX<0?e.scaleX:0,e.outOfRangeY=e.scaleY>e.opt.scale?e.scaleY-e.opt.scale:e.scaleY<0?e.scaleY:0,e.outOfRange="h"==e.opt.orientation?e.outOfRangeX:e.outOfRangeY,"undefined"!=typeof b?e.value="h"==e.opt.orientation?e.x>=d.outerWidth()?e.opt.scale:e.x<=0?0:e.scaleX:e.y>=d.outerHeight()?e.opt.scale:e.y<=0?0:e.scaleY:e.value="h"==e.opt.orientation?e.scaleX:e.scaleY,"h"==e.opt.orientation?e.level.width(c(e.x,f)+"%"):e.level.height(c(e.y,g)),"function"==typeof e.opt.callback&&e.opt.callback(e)}}},a.fn.simpleSlider=a.simpleSlider.init,a.fn.updateSliderVal=a.simpleSlider.updateSliderVal}(jQuery),!function(a){a.mbCookie={set:function(a,b,c,d){b=JSON.stringify(b),c||(c=7),d=d?"; domain="+d:"";var e,f=new Date;f.setTime(f.getTime()+864e5*c),e="; expires="+f.toGMTString(),document.cookie=a+"="+b+e+"; path=/"+d},get:function(a){for(var b=a+"=",c=document.cookie.split(";"),d=0;d<c.length;d++){for(var e=c[d];" "==e.charAt(0);)e=e.substring(1,e.length);if(0==e.indexOf(b))return JSON.parse(e.substring(b.length,e.length))}return null},remove:function(b){a.mbCookie.set(b,"",-1)}},a.mbStorage={set:function(a,b){b=JSON.stringify(b),localStorage.setItem(a,b)},get:function(a){return localStorage[a]?JSON.parse(localStorage[a]):null},remove:function(a){a?localStorage.removeItem(a):localStorage.clear()}}}(jQuery);

//
// shooting stars
// https://github.com/jh3y/shooting-stars
//

if($('#homeBgShootingStars').is(':visible')){(function() {var t,i,e,o,r;i=function(t,i,e,o,r,n,a,s,h,l){var d;return d=this,d.x=s,d.y=h,d.size=t,d.color=a,d.border=n,d.outerRad=o,d.innerRad=r,d.rotation=i,d.points=e,d.opacity=0,d.scale=0,d.vx=2*Math.random()-1,d.vy=2*Math.random()-1,d.life=0,d.ss=l,d},i.prototype.update=function(){var t,i,e,o;return this.x+=this.vx,this.y+=this.vy,t=this.ss.canvas,i=this.ss.maxLife,e=this.ss.particlePool,o=this.ss.particles,this.opacity<1&&this.life<i/6&&(this.opacity+=100/(i/6)/100,this.scale+=100/(i/6)/100),this.life++,i-this.life<i/6&&(this.scale-=100/(i/6)/100),i-this.life<i/3?(this.vy*=1.075,this.vx*=1.075,this.opacity=(i-this.life)/100):this.life%2===0&&this.rotation++,this.life>=i&&(this.life=0,this.scale=0,this.x=Math.floor(Math.random()*t.width+1),this.y=Math.floor(Math.random()*t.height+1),this.vx=Math.random()-.5,this.vy=Math.random()-.5,self.vx=2*Math.random()-1,self.vy=2*Math.random()-1,e.push(o.shift())),this},i.prototype.render=function(t){var i,e,o,r,n,a;for(r=this,n=document.createElement("canvas"),n.width=r.size,n.height=r.size,a=n.getContext("2d"),a.save(),a.fillStyle=r.color,a.strokeStyle=r.border,a.globalAlpha=r.opacity,a.translate(r.size/2,r.size/2),a.rotate(r.rotation*Math.PI/180),a.translate(-(r.size/2),-(r.size/2)),a.scale(r.scale,r.scale),a.beginPath(),i=0;i<=2*r.points;)o=i*Math.PI/r.points,e=i%2===0?r.outerRad:r.innerRad,a.lineTo(r.size/2+e*Math.cos(o),r.size/2+e*Math.sin(o)),++i;return a.fill(),a.stroke(),a.restore(),t.drawImage(n,r.x,r.y)},e=function(t,i){var e;return e=void 0,e=void 0,function(){var o,r;return o=void 0,r=void 0,r=this,o=arguments,clearTimeout(e),e=setTimeout(function(){return t.apply(r,o)},i)}},o=function(t,i){var e;for(e in i)i.hasOwnProperty(e)&&void 0!==i[e]&&(t[e]=i[e]);return t},r=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||window.msRequestAnimationFrame||function(t){return setTimeout(t,1e3/60)},window.ShootingStars=t=function(t){var i,r,n,a;return a=this,r=t.id,n={particleLife:300,particleRenderProbability:.05,amount:5,resizePoll:250,star:{size:{upper:50,lower:25},rotateLimit:45,points:5,innerRadius:.5,borderColor:"#000",fillColor:"red"}},a.options=o(n,t),a.canvas=i=document.getElementById(r),i.width=window.innerWidth,i.height=window.innerHeight,i.ctx=i.getContext("2d"),a.maxLife=a.options.particleLife,a.particles=[],a.particlePool=[],a.particleProbability=a.options.particleRenderProbability,a.poolSize=a.options.amount,window.addEventListener("resize",e(function(){a.canvas.width=window.innerWidth,a.canvas.height=window.innerHeight,a.flushPool()},a.options.resizePoll)),a},t.prototype.flushPool=function(){var t,e,o,r,n,a,s,h,l,d;for(d=this,t=d.canvas,r=d.particlePool=[],n=d.particles=[],a=self.poolSize=d.options.amount,t.width<450&&(a=self.poolSize=a/2),o=0,s=[];a>o;)e=function(t,i){return Math.floor(Math.random()*(t-i+1)+i)},l=e(d.options.star.size.upper,d.options.star.size.lower),h=e(d.options.star.rotateLimit,0),r.push(new i(l,h,5,l/2,l/2*d.options.star.innerRadius,this.options.star.borderColor,this.options.star.fillColor,Math.floor(Math.random()*t.width+1),Math.floor(Math.random()*t.height+1),d)),s.push(o++);return s},t.prototype.render=function(){var t,i,e,o,n,a;for(a=this,t=a.canvas,i=t.ctx,o=a.particlePool,n=a.particles,i.save(),i.clearRect(0,0,t.width,t.height),Math.random()>a.particleProbability&&n.length<a.poolSize&&o.length>0&&n.push(o.shift()),e=0;e<n.length;)n[e].update(),n[e]&&n[e].render(i),e++;return i.restore(),r(function(){return a.render()})}}).call(this);

var config = {
  id: 'homeBgShootingStars',
  particleLife: 300,
  particleRenderProbability: 0.95,
  amount: 50,
  star: {
    size: {
      upper: 50,
      lower: 25
    },
    rotateLimit: 90,
    points: 5,
    innerRadius: 0.5,
    borderColor: '#290f5a',
    fillColor: '#ffcc00',
  }
};
myCanvas = new ShootingStars(config);
myCanvas.flushPool();
myCanvas.render();

}

/*
     _ _      _       _
 ___| (_) ___| | __  (_)___
/ __| | |/ __| |/ /  | / __|
\__ \ | | (__|   < _ | \__ \
|___/_|_|\___|_|\_(_)/ |___/
                   |__/

 Version: 1.6.0
  Author: Ken Wheeler
 Website: http://kenwheeler.github.io
    Docs: http://kenwheeler.github.io/slick
    Repo: http://github.com/kenwheeler/slick
  Issues: http://github.com/kenwheeler/slick/issues

 */
!function(a){"use strict";"function"==typeof define&&define.amd?define(["jquery"],a):"undefined"!=typeof exports?module.exports=a(require("jquery")):a(jQuery)}(function(a){"use strict";var b=window.Slick||{};b=function(){function c(c,d){var f,e=this;e.defaults={accessibility:!0,adaptiveHeight:!1,appendArrows:a(c),appendDots:a(c),arrows:!0,asNavFor:null,prevArrow:'<button type="button" data-role="none" class="slick-prev" aria-label="Previous" tabindex="0" role="button">Previous</button>',nextArrow:'<button type="button" data-role="none" class="slick-next" aria-label="Next" tabindex="0" role="button">Next</button>',autoplay:!1,autoplaySpeed:3e3,centerMode:!1,centerPadding:"50px",cssEase:"ease",customPaging:function(b,c){return a('<button type="button" data-role="none" role="button" tabindex="0" />').text(c+1)},dots:!1,dotsClass:"slick-dots",draggable:!0,easing:"linear",edgeFriction:.35,fade:!1,focusOnSelect:!1,infinite:!0,initialSlide:0,lazyLoad:"ondemand",mobileFirst:!1,pauseOnHover:!0,pauseOnFocus:!0,pauseOnDotsHover:!1,respondTo:"window",responsive:null,rows:1,rtl:!1,slide:"",slidesPerRow:1,slidesToShow:1,slidesToScroll:1,speed:500,swipe:!0,swipeToSlide:!1,touchMove:!0,touchThreshold:5,useCSS:!0,useTransform:!0,variableWidth:!1,vertical:!1,verticalSwiping:!1,waitForAnimate:!0,zIndex:1e3},e.initials={animating:!1,dragging:!1,autoPlayTimer:null,currentDirection:0,currentLeft:null,currentSlide:0,direction:1,$dots:null,listWidth:null,listHeight:null,loadIndex:0,$nextArrow:null,$prevArrow:null,slideCount:null,slideWidth:null,$slideTrack:null,$slides:null,sliding:!1,slideOffset:0,swipeLeft:null,$list:null,touchObject:{},transformsEnabled:!1,unslicked:!1},a.extend(e,e.initials),e.activeBreakpoint=null,e.animType=null,e.animProp=null,e.breakpoints=[],e.breakpointSettings=[],e.cssTransitions=!1,e.focussed=!1,e.interrupted=!1,e.hidden="hidden",e.paused=!0,e.positionProp=null,e.respondTo=null,e.rowCount=1,e.shouldClick=!0,e.$slider=a(c),e.$slidesCache=null,e.transformType=null,e.transitionType=null,e.visibilityChange="visibilitychange",e.windowWidth=0,e.windowTimer=null,f=a(c).data("slick")||{},e.options=a.extend({},e.defaults,d,f),e.currentSlide=e.options.initialSlide,e.originalSettings=e.options,"undefined"!=typeof document.mozHidden?(e.hidden="mozHidden",e.visibilityChange="mozvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(e.hidden="webkitHidden",e.visibilityChange="webkitvisibilitychange"),e.autoPlay=a.proxy(e.autoPlay,e),e.autoPlayClear=a.proxy(e.autoPlayClear,e),e.autoPlayIterator=a.proxy(e.autoPlayIterator,e),e.changeSlide=a.proxy(e.changeSlide,e),e.clickHandler=a.proxy(e.clickHandler,e),e.selectHandler=a.proxy(e.selectHandler,e),e.setPosition=a.proxy(e.setPosition,e),e.swipeHandler=a.proxy(e.swipeHandler,e),e.dragHandler=a.proxy(e.dragHandler,e),e.keyHandler=a.proxy(e.keyHandler,e),e.instanceUid=b++,e.htmlExpr=/^(?:\s*(<[\w\W]+>)[^>]*)$/,e.registerBreakpoints(),e.init(!0)}var b=0;return c}(),b.prototype.activateADA=function(){var a=this;a.$slideTrack.find(".slick-active").attr({"aria-hidden":"false"}).find("a, input, button, select").attr({tabindex:"0"})},b.prototype.addSlide=b.prototype.slickAdd=function(b,c,d){var e=this;if("boolean"==typeof c)d=c,c=null;else if(0>c||c>=e.slideCount)return!1;e.unload(),"number"==typeof c?0===c&&0===e.$slides.length?a(b).appendTo(e.$slideTrack):d?a(b).insertBefore(e.$slides.eq(c)):a(b).insertAfter(e.$slides.eq(c)):d===!0?a(b).prependTo(e.$slideTrack):a(b).appendTo(e.$slideTrack),e.$slides=e.$slideTrack.children(this.options.slide),e.$slideTrack.children(this.options.slide).detach(),e.$slideTrack.append(e.$slides),e.$slides.each(function(b,c){a(c).attr("data-slick-index",b)}),e.$slidesCache=e.$slides,e.reinit()},b.prototype.animateHeight=function(){var a=this;if(1===a.options.slidesToShow&&a.options.adaptiveHeight===!0&&a.options.vertical===!1){var b=a.$slides.eq(a.currentSlide).outerHeight(!0);a.$list.animate({height:b},a.options.speed)}},b.prototype.animateSlide=function(b,c){var d={},e=this;e.animateHeight(),e.options.rtl===!0&&e.options.vertical===!1&&(b=-b),e.transformsEnabled===!1?e.options.vertical===!1?e.$slideTrack.animate({left:b},e.options.speed,e.options.easing,c):e.$slideTrack.animate({top:b},e.options.speed,e.options.easing,c):e.cssTransitions===!1?(e.options.rtl===!0&&(e.currentLeft=-e.currentLeft),a({animStart:e.currentLeft}).animate({animStart:b},{duration:e.options.speed,easing:e.options.easing,step:function(a){a=Math.ceil(a),e.options.vertical===!1?(d[e.animType]="translate("+a+"px, 0px)",e.$slideTrack.css(d)):(d[e.animType]="translate(0px,"+a+"px)",e.$slideTrack.css(d))},complete:function(){c&&c.call()}})):(e.applyTransition(),b=Math.ceil(b),e.options.vertical===!1?d[e.animType]="translate3d("+b+"px, 0px, 0px)":d[e.animType]="translate3d(0px,"+b+"px, 0px)",e.$slideTrack.css(d),c&&setTimeout(function(){e.disableTransition(),c.call()},e.options.speed))},b.prototype.getNavTarget=function(){var b=this,c=b.options.asNavFor;return c&&null!==c&&(c=a(c).not(b.$slider)),c},b.prototype.asNavFor=function(b){var c=this,d=c.getNavTarget();null!==d&&"object"==typeof d&&d.each(function(){var c=a(this).slick("getSlick");c.unslicked||c.slideHandler(b,!0)})},b.prototype.applyTransition=function(a){var b=this,c={};b.options.fade===!1?c[b.transitionType]=b.transformType+" "+b.options.speed+"ms "+b.options.cssEase:c[b.transitionType]="opacity "+b.options.speed+"ms "+b.options.cssEase,b.options.fade===!1?b.$slideTrack.css(c):b.$slides.eq(a).css(c)},b.prototype.autoPlay=function(){var a=this;a.autoPlayClear(),a.slideCount>a.options.slidesToShow&&(a.autoPlayTimer=setInterval(a.autoPlayIterator,a.options.autoplaySpeed))},b.prototype.autoPlayClear=function(){var a=this;a.autoPlayTimer&&clearInterval(a.autoPlayTimer)},b.prototype.autoPlayIterator=function(){var a=this,b=a.currentSlide+a.options.slidesToScroll;a.paused||a.interrupted||a.focussed||(a.options.infinite===!1&&(1===a.direction&&a.currentSlide+1===a.slideCount-1?a.direction=0:0===a.direction&&(b=a.currentSlide-a.options.slidesToScroll,a.currentSlide-1===0&&(a.direction=1))),a.slideHandler(b))},b.prototype.buildArrows=function(){var b=this;b.options.arrows===!0&&(b.$prevArrow=a(b.options.prevArrow).addClass("slick-arrow"),b.$nextArrow=a(b.options.nextArrow).addClass("slick-arrow"),b.slideCount>b.options.slidesToShow?(b.$prevArrow.removeClass("slick-hidden").removeAttr("aria-hidden tabindex"),b.$nextArrow.removeClass("slick-hidden").removeAttr("aria-hidden tabindex"),b.htmlExpr.test(b.options.prevArrow)&&b.$prevArrow.prependTo(b.options.appendArrows),b.htmlExpr.test(b.options.nextArrow)&&b.$nextArrow.appendTo(b.options.appendArrows),b.options.infinite!==!0&&b.$prevArrow.addClass("slick-disabled").attr("aria-disabled","true")):b.$prevArrow.add(b.$nextArrow).addClass("slick-hidden").attr({"aria-disabled":"true",tabindex:"-1"}))},b.prototype.buildDots=function(){var c,d,b=this;if(b.options.dots===!0&&b.slideCount>b.options.slidesToShow){for(b.$slider.addClass("slick-dotted"),d=a("<ul />").addClass(b.options.dotsClass),c=0;c<=b.getDotCount();c+=1)d.append(a("<li />").append(b.options.customPaging.call(this,b,c)));b.$dots=d.appendTo(b.options.appendDots),b.$dots.find("li").first().addClass("slick-active").attr("aria-hidden","false")}},b.prototype.buildOut=function(){var b=this;b.$slides=b.$slider.children(b.options.slide+":not(.slick-cloned)").addClass("slick-slide"),b.slideCount=b.$slides.length,b.$slides.each(function(b,c){a(c).attr("data-slick-index",b).data("originalStyling",a(c).attr("style")||"")}),b.$slider.addClass("slick-slider"),b.$slideTrack=0===b.slideCount?a('<div class="slick-track"/>').appendTo(b.$slider):b.$slides.wrapAll('<div class="slick-track"/>').parent(),b.$list=b.$slideTrack.wrap('<div aria-live="polite" class="slick-list"/>').parent(),b.$slideTrack.css("opacity",0),(b.options.centerMode===!0||b.options.swipeToSlide===!0)&&(b.options.slidesToScroll=1),a("img[data-lazy]",b.$slider).not("[src]").addClass("slick-loading"),b.setupInfinite(),b.buildArrows(),b.buildDots(),b.updateDots(),b.setSlideClasses("number"==typeof b.currentSlide?b.currentSlide:0),b.options.draggable===!0&&b.$list.addClass("draggable")},b.prototype.buildRows=function(){var b,c,d,e,f,g,h,a=this;if(e=document.createDocumentFragment(),g=a.$slider.children(),a.options.rows>1){for(h=a.options.slidesPerRow*a.options.rows,f=Math.ceil(g.length/h),b=0;f>b;b++){var i=document.createElement("div");for(c=0;c<a.options.rows;c++){var j=document.createElement("div");for(d=0;d<a.options.slidesPerRow;d++){var k=b*h+(c*a.options.slidesPerRow+d);g.get(k)&&j.appendChild(g.get(k))}i.appendChild(j)}e.appendChild(i)}a.$slider.empty().append(e),a.$slider.children().children().children().css({width:100/a.options.slidesPerRow+"%",display:"inline-block"})}},b.prototype.checkResponsive=function(b,c){var e,f,g,d=this,h=!1,i=d.$slider.width(),j=window.innerWidth||a(window).width();if("window"===d.respondTo?g=j:"slider"===d.respondTo?g=i:"min"===d.respondTo&&(g=Math.min(j,i)),d.options.responsive&&d.options.responsive.length&&null!==d.options.responsive){f=null;for(e in d.breakpoints)d.breakpoints.hasOwnProperty(e)&&(d.originalSettings.mobileFirst===!1?g<d.breakpoints[e]&&(f=d.breakpoints[e]):g>d.breakpoints[e]&&(f=d.breakpoints[e]));null!==f?null!==d.activeBreakpoint?(f!==d.activeBreakpoint||c)&&(d.activeBreakpoint=f,"unslick"===d.breakpointSettings[f]?d.unslick(f):(d.options=a.extend({},d.originalSettings,d.breakpointSettings[f]),b===!0&&(d.currentSlide=d.options.initialSlide),d.refresh(b)),h=f):(d.activeBreakpoint=f,"unslick"===d.breakpointSettings[f]?d.unslick(f):(d.options=a.extend({},d.originalSettings,d.breakpointSettings[f]),b===!0&&(d.currentSlide=d.options.initialSlide),d.refresh(b)),h=f):null!==d.activeBreakpoint&&(d.activeBreakpoint=null,d.options=d.originalSettings,b===!0&&(d.currentSlide=d.options.initialSlide),d.refresh(b),h=f),b||h===!1||d.$slider.trigger("breakpoint",[d,h])}},b.prototype.changeSlide=function(b,c){var f,g,h,d=this,e=a(b.currentTarget);switch(e.is("a")&&b.preventDefault(),e.is("li")||(e=e.closest("li")),h=d.slideCount%d.options.slidesToScroll!==0,f=h?0:(d.slideCount-d.currentSlide)%d.options.slidesToScroll,b.data.message){case"previous":g=0===f?d.options.slidesToScroll:d.options.slidesToShow-f,d.slideCount>d.options.slidesToShow&&d.slideHandler(d.currentSlide-g,!1,c);break;case"next":g=0===f?d.options.slidesToScroll:f,d.slideCount>d.options.slidesToShow&&d.slideHandler(d.currentSlide+g,!1,c);break;case"index":var i=0===b.data.index?0:b.data.index||e.index()*d.options.slidesToScroll;d.slideHandler(d.checkNavigable(i),!1,c),e.children().trigger("focus");break;default:return}},b.prototype.checkNavigable=function(a){var c,d,b=this;if(c=b.getNavigableIndexes(),d=0,a>c[c.length-1])a=c[c.length-1];else for(var e in c){if(a<c[e]){a=d;break}d=c[e]}return a},b.prototype.cleanUpEvents=function(){var b=this;b.options.dots&&null!==b.$dots&&a("li",b.$dots).off("click.slick",b.changeSlide).off("mouseenter.slick",a.proxy(b.interrupt,b,!0)).off("mouseleave.slick",a.proxy(b.interrupt,b,!1)),b.$slider.off("focus.slick blur.slick"),b.options.arrows===!0&&b.slideCount>b.options.slidesToShow&&(b.$prevArrow&&b.$prevArrow.off("click.slick",b.changeSlide),b.$nextArrow&&b.$nextArrow.off("click.slick",b.changeSlide)),b.$list.off("touchstart.slick mousedown.slick",b.swipeHandler),b.$list.off("touchmove.slick mousemove.slick",b.swipeHandler),b.$list.off("touchend.slick mouseup.slick",b.swipeHandler),b.$list.off("touchcancel.slick mouseleave.slick",b.swipeHandler),b.$list.off("click.slick",b.clickHandler),a(document).off(b.visibilityChange,b.visibility),b.cleanUpSlideEvents(),b.options.accessibility===!0&&b.$list.off("keydown.slick",b.keyHandler),b.options.focusOnSelect===!0&&a(b.$slideTrack).children().off("click.slick",b.selectHandler),a(window).off("orientationchange.slick.slick-"+b.instanceUid,b.orientationChange),a(window).off("resize.slick.slick-"+b.instanceUid,b.resize),a("[draggable!=true]",b.$slideTrack).off("dragstart",b.preventDefault),a(window).off("load.slick.slick-"+b.instanceUid,b.setPosition),a(document).off("ready.slick.slick-"+b.instanceUid,b.setPosition)},b.prototype.cleanUpSlideEvents=function(){var b=this;b.$list.off("mouseenter.slick",a.proxy(b.interrupt,b,!0)),b.$list.off("mouseleave.slick",a.proxy(b.interrupt,b,!1))},b.prototype.cleanUpRows=function(){var b,a=this;a.options.rows>1&&(b=a.$slides.children().children(),b.removeAttr("style"),a.$slider.empty().append(b))},b.prototype.clickHandler=function(a){var b=this;b.shouldClick===!1&&(a.stopImmediatePropagation(),a.stopPropagation(),a.preventDefault())},b.prototype.destroy=function(b){var c=this;c.autoPlayClear(),c.touchObject={},c.cleanUpEvents(),a(".slick-cloned",c.$slider).detach(),c.$dots&&c.$dots.remove(),c.$prevArrow&&c.$prevArrow.length&&(c.$prevArrow.removeClass("slick-disabled slick-arrow slick-hidden").removeAttr("aria-hidden aria-disabled tabindex").css("display",""),c.htmlExpr.test(c.options.prevArrow)&&c.$prevArrow.remove()),c.$nextArrow&&c.$nextArrow.length&&(c.$nextArrow.removeClass("slick-disabled slick-arrow slick-hidden").removeAttr("aria-hidden aria-disabled tabindex").css("display",""),c.htmlExpr.test(c.options.nextArrow)&&c.$nextArrow.remove()),c.$slides&&(c.$slides.removeClass("slick-slide slick-active slick-center slick-visible slick-current").removeAttr("aria-hidden").removeAttr("data-slick-index").each(function(){a(this).attr("style",a(this).data("originalStyling"))}),c.$slideTrack.children(this.options.slide).detach(),c.$slideTrack.detach(),c.$list.detach(),c.$slider.append(c.$slides)),c.cleanUpRows(),c.$slider.removeClass("slick-slider"),c.$slider.removeClass("slick-initialized"),c.$slider.removeClass("slick-dotted"),c.unslicked=!0,b||c.$slider.trigger("destroy",[c])},b.prototype.disableTransition=function(a){var b=this,c={};c[b.transitionType]="",b.options.fade===!1?b.$slideTrack.css(c):b.$slides.eq(a).css(c)},b.prototype.fadeSlide=function(a,b){var c=this;c.cssTransitions===!1?(c.$slides.eq(a).css({zIndex:c.options.zIndex}),c.$slides.eq(a).animate({opacity:1},c.options.speed,c.options.easing,b)):(c.applyTransition(a),c.$slides.eq(a).css({opacity:1,zIndex:c.options.zIndex}),b&&setTimeout(function(){c.disableTransition(a),b.call()},c.options.speed))},b.prototype.fadeSlideOut=function(a){var b=this;b.cssTransitions===!1?b.$slides.eq(a).animate({opacity:0,zIndex:b.options.zIndex-2},b.options.speed,b.options.easing):(b.applyTransition(a),b.$slides.eq(a).css({opacity:0,zIndex:b.options.zIndex-2}))},b.prototype.filterSlides=b.prototype.slickFilter=function(a){var b=this;null!==a&&(b.$slidesCache=b.$slides,b.unload(),b.$slideTrack.children(this.options.slide).detach(),b.$slidesCache.filter(a).appendTo(b.$slideTrack),b.reinit())},b.prototype.focusHandler=function(){var b=this;b.$slider.off("focus.slick blur.slick").on("focus.slick blur.slick","*:not(.slick-arrow)",function(c){c.stopImmediatePropagation();var d=a(this);setTimeout(function(){b.options.pauseOnFocus&&(b.focussed=d.is(":focus"),b.autoPlay())},0)})},b.prototype.getCurrent=b.prototype.slickCurrentSlide=function(){var a=this;return a.currentSlide},b.prototype.getDotCount=function(){var a=this,b=0,c=0,d=0;if(a.options.infinite===!0)for(;b<a.slideCount;)++d,b=c+a.options.slidesToScroll,c+=a.options.slidesToScroll<=a.options.slidesToShow?a.options.slidesToScroll:a.options.slidesToShow;else if(a.options.centerMode===!0)d=a.slideCount;else if(a.options.asNavFor)for(;b<a.slideCount;)++d,b=c+a.options.slidesToScroll,c+=a.options.slidesToScroll<=a.options.slidesToShow?a.options.slidesToScroll:a.options.slidesToShow;else d=1+Math.ceil((a.slideCount-a.options.slidesToShow)/a.options.slidesToScroll);return d-1},b.prototype.getLeft=function(a){var c,d,f,b=this,e=0;return b.slideOffset=0,d=b.$slides.first().outerHeight(!0),b.options.infinite===!0?(b.slideCount>b.options.slidesToShow&&(b.slideOffset=b.slideWidth*b.options.slidesToShow*-1,e=d*b.options.slidesToShow*-1),b.slideCount%b.options.slidesToScroll!==0&&a+b.options.slidesToScroll>b.slideCount&&b.slideCount>b.options.slidesToShow&&(a>b.slideCount?(b.slideOffset=(b.options.slidesToShow-(a-b.slideCount))*b.slideWidth*-1,e=(b.options.slidesToShow-(a-b.slideCount))*d*-1):(b.slideOffset=b.slideCount%b.options.slidesToScroll*b.slideWidth*-1,e=b.slideCount%b.options.slidesToScroll*d*-1))):a+b.options.slidesToShow>b.slideCount&&(b.slideOffset=(a+b.options.slidesToShow-b.slideCount)*b.slideWidth,e=(a+b.options.slidesToShow-b.slideCount)*d),b.slideCount<=b.options.slidesToShow&&(b.slideOffset=0,e=0),b.options.centerMode===!0&&b.options.infinite===!0?b.slideOffset+=b.slideWidth*Math.floor(b.options.slidesToShow/2)-b.slideWidth:b.options.centerMode===!0&&(b.slideOffset=0,b.slideOffset+=b.slideWidth*Math.floor(b.options.slidesToShow/2)),c=b.options.vertical===!1?a*b.slideWidth*-1+b.slideOffset:a*d*-1+e,b.options.variableWidth===!0&&(f=b.slideCount<=b.options.slidesToShow||b.options.infinite===!1?b.$slideTrack.children(".slick-slide").eq(a):b.$slideTrack.children(".slick-slide").eq(a+b.options.slidesToShow),c=b.options.rtl===!0?f[0]?-1*(b.$slideTrack.width()-f[0].offsetLeft-f.width()):0:f[0]?-1*f[0].offsetLeft:0,b.options.centerMode===!0&&(f=b.slideCount<=b.options.slidesToShow||b.options.infinite===!1?b.$slideTrack.children(".slick-slide").eq(a):b.$slideTrack.children(".slick-slide").eq(a+b.options.slidesToShow+1),c=b.options.rtl===!0?f[0]?-1*(b.$slideTrack.width()-f[0].offsetLeft-f.width()):0:f[0]?-1*f[0].offsetLeft:0,c+=(b.$list.width()-f.outerWidth())/2)),c},b.prototype.getOption=b.prototype.slickGetOption=function(a){var b=this;return b.options[a]},b.prototype.getNavigableIndexes=function(){var e,a=this,b=0,c=0,d=[];for(a.options.infinite===!1?e=a.slideCount:(b=-1*a.options.slidesToScroll,c=-1*a.options.slidesToScroll,e=2*a.slideCount);e>b;)d.push(b),b=c+a.options.slidesToScroll,c+=a.options.slidesToScroll<=a.options.slidesToShow?a.options.slidesToScroll:a.options.slidesToShow;return d},b.prototype.getSlick=function(){return this},b.prototype.getSlideCount=function(){var c,d,e,b=this;return e=b.options.centerMode===!0?b.slideWidth*Math.floor(b.options.slidesToShow/2):0,b.options.swipeToSlide===!0?(b.$slideTrack.find(".slick-slide").each(function(c,f){return f.offsetLeft-e+a(f).outerWidth()/2>-1*b.swipeLeft?(d=f,!1):void 0}),c=Math.abs(a(d).attr("data-slick-index")-b.currentSlide)||1):b.options.slidesToScroll},b.prototype.goTo=b.prototype.slickGoTo=function(a,b){var c=this;c.changeSlide({data:{message:"index",index:parseInt(a)}},b)},b.prototype.init=function(b){var c=this;a(c.$slider).hasClass("slick-initialized")||(a(c.$slider).addClass("slick-initialized"),c.buildRows(),c.buildOut(),c.setProps(),c.startLoad(),c.loadSlider(),c.initializeEvents(),c.updateArrows(),c.updateDots(),c.checkResponsive(!0),c.focusHandler()),b&&c.$slider.trigger("init",[c]),c.options.accessibility===!0&&c.initADA(),c.options.autoplay&&(c.paused=!1,c.autoPlay())},b.prototype.initADA=function(){var b=this;b.$slides.add(b.$slideTrack.find(".slick-cloned")).attr({"aria-hidden":"true",tabindex:"-1"}).find("a, input, button, select").attr({tabindex:"-1"}),b.$slideTrack.attr("role","listbox"),b.$slides.not(b.$slideTrack.find(".slick-cloned")).each(function(c){a(this).attr({role:"option","aria-describedby":"slick-slide"+b.instanceUid+c})}),null!==b.$dots&&b.$dots.attr("role","tablist").find("li").each(function(c){a(this).attr({role:"presentation","aria-selected":"false","aria-controls":"navigation"+b.instanceUid+c,id:"slick-slide"+b.instanceUid+c})}).first().attr("aria-selected","true").end().find("button").attr("role","button").end().closest("div").attr("role","toolbar"),b.activateADA()},b.prototype.initArrowEvents=function(){var a=this;a.options.arrows===!0&&a.slideCount>a.options.slidesToShow&&(a.$prevArrow.off("click.slick").on("click.slick",{message:"previous"},a.changeSlide),a.$nextArrow.off("click.slick").on("click.slick",{message:"next"},a.changeSlide))},b.prototype.initDotEvents=function(){var b=this;b.options.dots===!0&&b.slideCount>b.options.slidesToShow&&a("li",b.$dots).on("click.slick",{message:"index"},b.changeSlide),b.options.dots===!0&&b.options.pauseOnDotsHover===!0&&a("li",b.$dots).on("mouseenter.slick",a.proxy(b.interrupt,b,!0)).on("mouseleave.slick",a.proxy(b.interrupt,b,!1))},b.prototype.initSlideEvents=function(){var b=this;b.options.pauseOnHover&&(b.$list.on("mouseenter.slick",a.proxy(b.interrupt,b,!0)),b.$list.on("mouseleave.slick",a.proxy(b.interrupt,b,!1)))},b.prototype.initializeEvents=function(){var b=this;b.initArrowEvents(),b.initDotEvents(),b.initSlideEvents(),b.$list.on("touchstart.slick mousedown.slick",{action:"start"},b.swipeHandler),b.$list.on("touchmove.slick mousemove.slick",{action:"move"},b.swipeHandler),b.$list.on("touchend.slick mouseup.slick",{action:"end"},b.swipeHandler),b.$list.on("touchcancel.slick mouseleave.slick",{action:"end"},b.swipeHandler),b.$list.on("click.slick",b.clickHandler),a(document).on(b.visibilityChange,a.proxy(b.visibility,b)),b.options.accessibility===!0&&b.$list.on("keydown.slick",b.keyHandler),b.options.focusOnSelect===!0&&a(b.$slideTrack).children().on("click.slick",b.selectHandler),a(window).on("orientationchange.slick.slick-"+b.instanceUid,a.proxy(b.orientationChange,b)),a(window).on("resize.slick.slick-"+b.instanceUid,a.proxy(b.resize,b)),a("[draggable!=true]",b.$slideTrack).on("dragstart",b.preventDefault),a(window).on("load.slick.slick-"+b.instanceUid,b.setPosition),a(document).on("ready.slick.slick-"+b.instanceUid,b.setPosition)},b.prototype.initUI=function(){var a=this;a.options.arrows===!0&&a.slideCount>a.options.slidesToShow&&(a.$prevArrow.show(),a.$nextArrow.show()),a.options.dots===!0&&a.slideCount>a.options.slidesToShow&&a.$dots.show()},b.prototype.keyHandler=function(a){var b=this;a.target.tagName.match("TEXTAREA|INPUT|SELECT")||(37===a.keyCode&&b.options.accessibility===!0?b.changeSlide({data:{message:b.options.rtl===!0?"next":"previous"}}):39===a.keyCode&&b.options.accessibility===!0&&b.changeSlide({data:{message:b.options.rtl===!0?"previous":"next"}}))},b.prototype.lazyLoad=function(){function g(c){a("img[data-lazy]",c).each(function(){var c=a(this),d=a(this).attr("data-lazy"),e=document.createElement("img");e.onload=function(){c.animate({opacity:0},100,function(){c.attr("src",d).animate({opacity:1},200,function(){c.removeAttr("data-lazy").removeClass("slick-loading")}),b.$slider.trigger("lazyLoaded",[b,c,d])})},e.onerror=function(){c.removeAttr("data-lazy").removeClass("slick-loading").addClass("slick-lazyload-error"),b.$slider.trigger("lazyLoadError",[b,c,d])},e.src=d})}var c,d,e,f,b=this;b.options.centerMode===!0?b.options.infinite===!0?(e=b.currentSlide+(b.options.slidesToShow/2+1),f=e+b.options.slidesToShow+2):(e=Math.max(0,b.currentSlide-(b.options.slidesToShow/2+1)),f=2+(b.options.slidesToShow/2+1)+b.currentSlide):(e=b.options.infinite?b.options.slidesToShow+b.currentSlide:b.currentSlide,f=Math.ceil(e+b.options.slidesToShow),b.options.fade===!0&&(e>0&&e--,f<=b.slideCount&&f++)),c=b.$slider.find(".slick-slide").slice(e,f),g(c),b.slideCount<=b.options.slidesToShow?(d=b.$slider.find(".slick-slide"),g(d)):b.currentSlide>=b.slideCount-b.options.slidesToShow?(d=b.$slider.find(".slick-cloned").slice(0,b.options.slidesToShow),g(d)):0===b.currentSlide&&(d=b.$slider.find(".slick-cloned").slice(-1*b.options.slidesToShow),g(d))},b.prototype.loadSlider=function(){var a=this;a.setPosition(),a.$slideTrack.css({opacity:1}),a.$slider.removeClass("slick-loading"),a.initUI(),"progressive"===a.options.lazyLoad&&a.progressiveLazyLoad()},b.prototype.next=b.prototype.slickNext=function(){var a=this;a.changeSlide({data:{message:"next"}})},b.prototype.orientationChange=function(){var a=this;a.checkResponsive(),a.setPosition()},b.prototype.pause=b.prototype.slickPause=function(){var a=this;a.autoPlayClear(),a.paused=!0},b.prototype.play=b.prototype.slickPlay=function(){var a=this;a.autoPlay(),a.options.autoplay=!0,a.paused=!1,a.focussed=!1,a.interrupted=!1},b.prototype.postSlide=function(a){var b=this;b.unslicked||(b.$slider.trigger("afterChange",[b,a]),b.animating=!1,b.setPosition(),b.swipeLeft=null,b.options.autoplay&&b.autoPlay(),b.options.accessibility===!0&&b.initADA())},b.prototype.prev=b.prototype.slickPrev=function(){var a=this;a.changeSlide({data:{message:"previous"}})},b.prototype.preventDefault=function(a){a.preventDefault()},b.prototype.progressiveLazyLoad=function(b){b=b||1;var e,f,g,c=this,d=a("img[data-lazy]",c.$slider);d.length?(e=d.first(),f=e.attr("data-lazy"),g=document.createElement("img"),g.onload=function(){e.attr("src",f).removeAttr("data-lazy").removeClass("slick-loading"),c.options.adaptiveHeight===!0&&c.setPosition(),c.$slider.trigger("lazyLoaded",[c,e,f]),c.progressiveLazyLoad()},g.onerror=function(){3>b?setTimeout(function(){c.progressiveLazyLoad(b+1)},500):(e.removeAttr("data-lazy").removeClass("slick-loading").addClass("slick-lazyload-error"),c.$slider.trigger("lazyLoadError",[c,e,f]),c.progressiveLazyLoad())},g.src=f):c.$slider.trigger("allImagesLoaded",[c])},b.prototype.refresh=function(b){var d,e,c=this;e=c.slideCount-c.options.slidesToShow,!c.options.infinite&&c.currentSlide>e&&(c.currentSlide=e),c.slideCount<=c.options.slidesToShow&&(c.currentSlide=0),d=c.currentSlide,c.destroy(!0),a.extend(c,c.initials,{currentSlide:d}),c.init(),b||c.changeSlide({data:{message:"index",index:d}},!1)},b.prototype.registerBreakpoints=function(){var c,d,e,b=this,f=b.options.responsive||null;if("array"===a.type(f)&&f.length){b.respondTo=b.options.respondTo||"window";for(c in f)if(e=b.breakpoints.length-1,d=f[c].breakpoint,f.hasOwnProperty(c)){for(;e>=0;)b.breakpoints[e]&&b.breakpoints[e]===d&&b.breakpoints.splice(e,1),e--;b.breakpoints.push(d),b.breakpointSettings[d]=f[c].settings}b.breakpoints.sort(function(a,c){return b.options.mobileFirst?a-c:c-a})}},b.prototype.reinit=function(){var b=this;b.$slides=b.$slideTrack.children(b.options.slide).addClass("slick-slide"),b.slideCount=b.$slides.length,b.currentSlide>=b.slideCount&&0!==b.currentSlide&&(b.currentSlide=b.currentSlide-b.options.slidesToScroll),b.slideCount<=b.options.slidesToShow&&(b.currentSlide=0),b.registerBreakpoints(),b.setProps(),b.setupInfinite(),b.buildArrows(),b.updateArrows(),b.initArrowEvents(),b.buildDots(),b.updateDots(),b.initDotEvents(),b.cleanUpSlideEvents(),b.initSlideEvents(),b.checkResponsive(!1,!0),b.options.focusOnSelect===!0&&a(b.$slideTrack).children().on("click.slick",b.selectHandler),b.setSlideClasses("number"==typeof b.currentSlide?b.currentSlide:0),b.setPosition(),b.focusHandler(),b.paused=!b.options.autoplay,b.autoPlay(),b.$slider.trigger("reInit",[b])},b.prototype.resize=function(){var b=this;a(window).width()!==b.windowWidth&&(clearTimeout(b.windowDelay),b.windowDelay=window.setTimeout(function(){b.windowWidth=a(window).width(),b.checkResponsive(),b.unslicked||b.setPosition()},50))},b.prototype.removeSlide=b.prototype.slickRemove=function(a,b,c){var d=this;return"boolean"==typeof a?(b=a,a=b===!0?0:d.slideCount-1):a=b===!0?--a:a,d.slideCount<1||0>a||a>d.slideCount-1?!1:(d.unload(),c===!0?d.$slideTrack.children().remove():d.$slideTrack.children(this.options.slide).eq(a).remove(),d.$slides=d.$slideTrack.children(this.options.slide),d.$slideTrack.children(this.options.slide).detach(),d.$slideTrack.append(d.$slides),d.$slidesCache=d.$slides,void d.reinit())},b.prototype.setCSS=function(a){var d,e,b=this,c={};b.options.rtl===!0&&(a=-a),d="left"==b.positionProp?Math.ceil(a)+"px":"0px",e="top"==b.positionProp?Math.ceil(a)+"px":"0px",c[b.positionProp]=a,b.transformsEnabled===!1?b.$slideTrack.css(c):(c={},b.cssTransitions===!1?(c[b.animType]="translate("+d+", "+e+")",b.$slideTrack.css(c)):(c[b.animType]="translate3d("+d+", "+e+", 0px)",b.$slideTrack.css(c)))},b.prototype.setDimensions=function(){var a=this;a.options.vertical===!1?a.options.centerMode===!0&&a.$list.css({padding:"0px "+a.options.centerPadding}):(a.$list.height(a.$slides.first().outerHeight(!0)*a.options.slidesToShow),a.options.centerMode===!0&&a.$list.css({padding:a.options.centerPadding+" 0px"})),a.listWidth=a.$list.width(),a.listHeight=a.$list.height(),a.options.vertical===!1&&a.options.variableWidth===!1?(a.slideWidth=Math.ceil(a.listWidth/a.options.slidesToShow),a.$slideTrack.width(Math.ceil(a.slideWidth*a.$slideTrack.children(".slick-slide").length))):a.options.variableWidth===!0?a.$slideTrack.width(5e3*a.slideCount):(a.slideWidth=Math.ceil(a.listWidth),a.$slideTrack.height(Math.ceil(a.$slides.first().outerHeight(!0)*a.$slideTrack.children(".slick-slide").length)));var b=a.$slides.first().outerWidth(!0)-a.$slides.first().width();a.options.variableWidth===!1&&a.$slideTrack.children(".slick-slide").width(a.slideWidth-b)},b.prototype.setFade=function(){var c,b=this;b.$slides.each(function(d,e){c=b.slideWidth*d*-1,b.options.rtl===!0?a(e).css({position:"relative",right:c,top:0,zIndex:b.options.zIndex-2,opacity:0}):a(e).css({position:"relative",left:c,top:0,zIndex:b.options.zIndex-2,opacity:0})}),b.$slides.eq(b.currentSlide).css({zIndex:b.options.zIndex-1,opacity:1})},b.prototype.setHeight=function(){var a=this;if(1===a.options.slidesToShow&&a.options.adaptiveHeight===!0&&a.options.vertical===!1){var b=a.$slides.eq(a.currentSlide).outerHeight(!0);a.$list.css("height",b)}},b.prototype.setOption=b.prototype.slickSetOption=function(){var c,d,e,f,h,b=this,g=!1;if("object"===a.type(arguments[0])?(e=arguments[0],g=arguments[1],h="multiple"):"string"===a.type(arguments[0])&&(e=arguments[0],f=arguments[1],g=arguments[2],"responsive"===arguments[0]&&"array"===a.type(arguments[1])?h="responsive":"undefined"!=typeof arguments[1]&&(h="single")),"single"===h)b.options[e]=f;else if("multiple"===h)a.each(e,function(a,c){b.options[a]=c});else if("responsive"===h)for(d in f)if("array"!==a.type(b.options.responsive))b.options.responsive=[f[d]];else{for(c=b.options.responsive.length-1;c>=0;)b.options.responsive[c].breakpoint===f[d].breakpoint&&b.options.responsive.splice(c,1),c--;b.options.responsive.push(f[d])}g&&(b.unload(),b.reinit())},b.prototype.setPosition=function(){var a=this;a.setDimensions(),a.setHeight(),a.options.fade===!1?a.setCSS(a.getLeft(a.currentSlide)):a.setFade(),a.$slider.trigger("setPosition",[a])},b.prototype.setProps=function(){var a=this,b=document.body.style;a.positionProp=a.options.vertical===!0?"top":"left","top"===a.positionProp?a.$slider.addClass("slick-vertical"):a.$slider.removeClass("slick-vertical"),(void 0!==b.WebkitTransition||void 0!==b.MozTransition||void 0!==b.msTransition)&&a.options.useCSS===!0&&(a.cssTransitions=!0),a.options.fade&&("number"==typeof a.options.zIndex?a.options.zIndex<3&&(a.options.zIndex=3):a.options.zIndex=a.defaults.zIndex),void 0!==b.OTransform&&(a.animType="OTransform",a.transformType="-o-transform",a.transitionType="OTransition",void 0===b.perspectiveProperty&&void 0===b.webkitPerspective&&(a.animType=!1)),void 0!==b.MozTransform&&(a.animType="MozTransform",a.transformType="-moz-transform",a.transitionType="MozTransition",void 0===b.perspectiveProperty&&void 0===b.MozPerspective&&(a.animType=!1)),void 0!==b.webkitTransform&&(a.animType="webkitTransform",a.transformType="-webkit-transform",a.transitionType="webkitTransition",void 0===b.perspectiveProperty&&void 0===b.webkitPerspective&&(a.animType=!1)),void 0!==b.msTransform&&(a.animType="msTransform",a.transformType="-ms-transform",a.transitionType="msTransition",void 0===b.msTransform&&(a.animType=!1)),void 0!==b.transform&&a.animType!==!1&&(a.animType="transform",a.transformType="transform",a.transitionType="transition"),a.transformsEnabled=a.options.useTransform&&null!==a.animType&&a.animType!==!1},b.prototype.setSlideClasses=function(a){var c,d,e,f,b=this;d=b.$slider.find(".slick-slide").removeClass("slick-active slick-center slick-current").attr("aria-hidden","true"),b.$slides.eq(a).addClass("slick-current"),b.options.centerMode===!0?(c=Math.floor(b.options.slidesToShow/2),b.options.infinite===!0&&(a>=c&&a<=b.slideCount-1-c?b.$slides.slice(a-c,a+c+1).addClass("slick-active").attr("aria-hidden","false"):(e=b.options.slidesToShow+a,
d.slice(e-c+1,e+c+2).addClass("slick-active").attr("aria-hidden","false")),0===a?d.eq(d.length-1-b.options.slidesToShow).addClass("slick-center"):a===b.slideCount-1&&d.eq(b.options.slidesToShow).addClass("slick-center")),b.$slides.eq(a).addClass("slick-center")):a>=0&&a<=b.slideCount-b.options.slidesToShow?b.$slides.slice(a,a+b.options.slidesToShow).addClass("slick-active").attr("aria-hidden","false"):d.length<=b.options.slidesToShow?d.addClass("slick-active").attr("aria-hidden","false"):(f=b.slideCount%b.options.slidesToShow,e=b.options.infinite===!0?b.options.slidesToShow+a:a,b.options.slidesToShow==b.options.slidesToScroll&&b.slideCount-a<b.options.slidesToShow?d.slice(e-(b.options.slidesToShow-f),e+f).addClass("slick-active").attr("aria-hidden","false"):d.slice(e,e+b.options.slidesToShow).addClass("slick-active").attr("aria-hidden","false")),"ondemand"===b.options.lazyLoad&&b.lazyLoad()},b.prototype.setupInfinite=function(){var c,d,e,b=this;if(b.options.fade===!0&&(b.options.centerMode=!1),b.options.infinite===!0&&b.options.fade===!1&&(d=null,b.slideCount>b.options.slidesToShow)){for(e=b.options.centerMode===!0?b.options.slidesToShow+1:b.options.slidesToShow,c=b.slideCount;c>b.slideCount-e;c-=1)d=c-1,a(b.$slides[d]).clone(!0).attr("id","").attr("data-slick-index",d-b.slideCount).prependTo(b.$slideTrack).addClass("slick-cloned");for(c=0;e>c;c+=1)d=c,a(b.$slides[d]).clone(!0).attr("id","").attr("data-slick-index",d+b.slideCount).appendTo(b.$slideTrack).addClass("slick-cloned");b.$slideTrack.find(".slick-cloned").find("[id]").each(function(){a(this).attr("id","")})}},b.prototype.interrupt=function(a){var b=this;a||b.autoPlay(),b.interrupted=a},b.prototype.selectHandler=function(b){var c=this,d=a(b.target).is(".slick-slide")?a(b.target):a(b.target).parents(".slick-slide"),e=parseInt(d.attr("data-slick-index"));return e||(e=0),c.slideCount<=c.options.slidesToShow?(c.setSlideClasses(e),void c.asNavFor(e)):void c.slideHandler(e)},b.prototype.slideHandler=function(a,b,c){var d,e,f,g,j,h=null,i=this;return b=b||!1,i.animating===!0&&i.options.waitForAnimate===!0||i.options.fade===!0&&i.currentSlide===a||i.slideCount<=i.options.slidesToShow?void 0:(b===!1&&i.asNavFor(a),d=a,h=i.getLeft(d),g=i.getLeft(i.currentSlide),i.currentLeft=null===i.swipeLeft?g:i.swipeLeft,i.options.infinite===!1&&i.options.centerMode===!1&&(0>a||a>i.getDotCount()*i.options.slidesToScroll)?void(i.options.fade===!1&&(d=i.currentSlide,c!==!0?i.animateSlide(g,function(){i.postSlide(d)}):i.postSlide(d))):i.options.infinite===!1&&i.options.centerMode===!0&&(0>a||a>i.slideCount-i.options.slidesToScroll)?void(i.options.fade===!1&&(d=i.currentSlide,c!==!0?i.animateSlide(g,function(){i.postSlide(d)}):i.postSlide(d))):(i.options.autoplay&&clearInterval(i.autoPlayTimer),e=0>d?i.slideCount%i.options.slidesToScroll!==0?i.slideCount-i.slideCount%i.options.slidesToScroll:i.slideCount+d:d>=i.slideCount?i.slideCount%i.options.slidesToScroll!==0?0:d-i.slideCount:d,i.animating=!0,i.$slider.trigger("beforeChange",[i,i.currentSlide,e]),f=i.currentSlide,i.currentSlide=e,i.setSlideClasses(i.currentSlide),i.options.asNavFor&&(j=i.getNavTarget(),j=j.slick("getSlick"),j.slideCount<=j.options.slidesToShow&&j.setSlideClasses(i.currentSlide)),i.updateDots(),i.updateArrows(),i.options.fade===!0?(c!==!0?(i.fadeSlideOut(f),i.fadeSlide(e,function(){i.postSlide(e)})):i.postSlide(e),void i.animateHeight()):void(c!==!0?i.animateSlide(h,function(){i.postSlide(e)}):i.postSlide(e))))},b.prototype.startLoad=function(){var a=this;a.options.arrows===!0&&a.slideCount>a.options.slidesToShow&&(a.$prevArrow.hide(),a.$nextArrow.hide()),a.options.dots===!0&&a.slideCount>a.options.slidesToShow&&a.$dots.hide(),a.$slider.addClass("slick-loading")},b.prototype.swipeDirection=function(){var a,b,c,d,e=this;return a=e.touchObject.startX-e.touchObject.curX,b=e.touchObject.startY-e.touchObject.curY,c=Math.atan2(b,a),d=Math.round(180*c/Math.PI),0>d&&(d=360-Math.abs(d)),45>=d&&d>=0?e.options.rtl===!1?"left":"right":360>=d&&d>=315?e.options.rtl===!1?"left":"right":d>=135&&225>=d?e.options.rtl===!1?"right":"left":e.options.verticalSwiping===!0?d>=35&&135>=d?"down":"up":"vertical"},b.prototype.swipeEnd=function(a){var c,d,b=this;if(b.dragging=!1,b.interrupted=!1,b.shouldClick=b.touchObject.swipeLength>10?!1:!0,void 0===b.touchObject.curX)return!1;if(b.touchObject.edgeHit===!0&&b.$slider.trigger("edge",[b,b.swipeDirection()]),b.touchObject.swipeLength>=b.touchObject.minSwipe){switch(d=b.swipeDirection()){case"left":case"down":c=b.options.swipeToSlide?b.checkNavigable(b.currentSlide+b.getSlideCount()):b.currentSlide+b.getSlideCount(),b.currentDirection=0;break;case"right":case"up":c=b.options.swipeToSlide?b.checkNavigable(b.currentSlide-b.getSlideCount()):b.currentSlide-b.getSlideCount(),b.currentDirection=1}"vertical"!=d&&(b.slideHandler(c),b.touchObject={},b.$slider.trigger("swipe",[b,d]))}else b.touchObject.startX!==b.touchObject.curX&&(b.slideHandler(b.currentSlide),b.touchObject={})},b.prototype.swipeHandler=function(a){var b=this;if(!(b.options.swipe===!1||"ontouchend"in document&&b.options.swipe===!1||b.options.draggable===!1&&-1!==a.type.indexOf("mouse")))switch(b.touchObject.fingerCount=a.originalEvent&&void 0!==a.originalEvent.touches?a.originalEvent.touches.length:1,b.touchObject.minSwipe=b.listWidth/b.options.touchThreshold,b.options.verticalSwiping===!0&&(b.touchObject.minSwipe=b.listHeight/b.options.touchThreshold),a.data.action){case"start":b.swipeStart(a);break;case"move":b.swipeMove(a);break;case"end":b.swipeEnd(a)}},b.prototype.swipeMove=function(a){var d,e,f,g,h,b=this;return h=void 0!==a.originalEvent?a.originalEvent.touches:null,!b.dragging||h&&1!==h.length?!1:(d=b.getLeft(b.currentSlide),b.touchObject.curX=void 0!==h?h[0].pageX:a.clientX,b.touchObject.curY=void 0!==h?h[0].pageY:a.clientY,b.touchObject.swipeLength=Math.round(Math.sqrt(Math.pow(b.touchObject.curX-b.touchObject.startX,2))),b.options.verticalSwiping===!0&&(b.touchObject.swipeLength=Math.round(Math.sqrt(Math.pow(b.touchObject.curY-b.touchObject.startY,2)))),e=b.swipeDirection(),"vertical"!==e?(void 0!==a.originalEvent&&b.touchObject.swipeLength>4&&a.preventDefault(),g=(b.options.rtl===!1?1:-1)*(b.touchObject.curX>b.touchObject.startX?1:-1),b.options.verticalSwiping===!0&&(g=b.touchObject.curY>b.touchObject.startY?1:-1),f=b.touchObject.swipeLength,b.touchObject.edgeHit=!1,b.options.infinite===!1&&(0===b.currentSlide&&"right"===e||b.currentSlide>=b.getDotCount()&&"left"===e)&&(f=b.touchObject.swipeLength*b.options.edgeFriction,b.touchObject.edgeHit=!0),b.options.vertical===!1?b.swipeLeft=d+f*g:b.swipeLeft=d+f*(b.$list.height()/b.listWidth)*g,b.options.verticalSwiping===!0&&(b.swipeLeft=d+f*g),b.options.fade===!0||b.options.touchMove===!1?!1:b.animating===!0?(b.swipeLeft=null,!1):void b.setCSS(b.swipeLeft)):void 0)},b.prototype.swipeStart=function(a){var c,b=this;return b.interrupted=!0,1!==b.touchObject.fingerCount||b.slideCount<=b.options.slidesToShow?(b.touchObject={},!1):(void 0!==a.originalEvent&&void 0!==a.originalEvent.touches&&(c=a.originalEvent.touches[0]),b.touchObject.startX=b.touchObject.curX=void 0!==c?c.pageX:a.clientX,b.touchObject.startY=b.touchObject.curY=void 0!==c?c.pageY:a.clientY,void(b.dragging=!0))},b.prototype.unfilterSlides=b.prototype.slickUnfilter=function(){var a=this;null!==a.$slidesCache&&(a.unload(),a.$slideTrack.children(this.options.slide).detach(),a.$slidesCache.appendTo(a.$slideTrack),a.reinit())},b.prototype.unload=function(){var b=this;a(".slick-cloned",b.$slider).remove(),b.$dots&&b.$dots.remove(),b.$prevArrow&&b.htmlExpr.test(b.options.prevArrow)&&b.$prevArrow.remove(),b.$nextArrow&&b.htmlExpr.test(b.options.nextArrow)&&b.$nextArrow.remove(),b.$slides.removeClass("slick-slide slick-active slick-visible slick-current").attr("aria-hidden","true").css("width","")},b.prototype.unslick=function(a){var b=this;b.$slider.trigger("unslick",[b,a]),b.destroy()},b.prototype.updateArrows=function(){var b,a=this;b=Math.floor(a.options.slidesToShow/2),a.options.arrows===!0&&a.slideCount>a.options.slidesToShow&&!a.options.infinite&&(a.$prevArrow.removeClass("slick-disabled").attr("aria-disabled","false"),a.$nextArrow.removeClass("slick-disabled").attr("aria-disabled","false"),0===a.currentSlide?(a.$prevArrow.addClass("slick-disabled").attr("aria-disabled","true"),a.$nextArrow.removeClass("slick-disabled").attr("aria-disabled","false")):a.currentSlide>=a.slideCount-a.options.slidesToShow&&a.options.centerMode===!1?(a.$nextArrow.addClass("slick-disabled").attr("aria-disabled","true"),a.$prevArrow.removeClass("slick-disabled").attr("aria-disabled","false")):a.currentSlide>=a.slideCount-1&&a.options.centerMode===!0&&(a.$nextArrow.addClass("slick-disabled").attr("aria-disabled","true"),a.$prevArrow.removeClass("slick-disabled").attr("aria-disabled","false")))},b.prototype.updateDots=function(){var a=this;null!==a.$dots&&(a.$dots.find("li").removeClass("slick-active").attr("aria-hidden","true"),a.$dots.find("li").eq(Math.floor(a.currentSlide/a.options.slidesToScroll)).addClass("slick-active").attr("aria-hidden","false"))},b.prototype.visibility=function(){var a=this;a.options.autoplay&&(document[a.hidden]?a.interrupted=!0:a.interrupted=!1)},a.fn.slick=function(){var f,g,a=this,c=arguments[0],d=Array.prototype.slice.call(arguments,1),e=a.length;for(f=0;e>f;f++)if("object"==typeof c||"undefined"==typeof c?a[f].slick=new b(a[f],c):g=a[f].slick[c].apply(a[f].slick,d),"undefined"!=typeof g)return g;return a}});


/*!-----------------------------------------------------------------------------
 * Vegas - Fullscreen Backgrounds and Slideshows.
 * v2.2.1 - built 2016-05-04
 * Licensed under the MIT License.
 * http://vegas.jaysalvat.com/
 * ----------------------------------------------------------------------------
 * Copyright (C) 2010-2016 Jay Salvat
 * http://jaysalvat.com/
 * --------------------------------------------------------------------------*/
!function(t){"use strict";var s={slide:0,delay:5e3,preload:!1,preloadImage:!1,preloadVideo:!1,timer:!0,overlay:!1,autoplay:!0,shuffle:!1,cover:!0,color:null,align:"center",valign:"center",transition:"fade",transitionDuration:1e3,transitionRegister:[],animation:null,animationDuration:"auto",animationRegister:[],init:function(){},play:function(){},pause:function(){},walk:function(){},slides:[]},i={},e=function(i,e){this.elmt=i,this.settings=t.extend({},s,t.vegas.defaults,e),this.slide=this.settings.slide,this.total=this.settings.slides.length,this.noshow=this.total<2,this.paused=!this.settings.autoplay||this.noshow,this.$elmt=t(i),this.$timer=null,this.$overlay=null,this.$slide=null,this.timeout=null,this.transitions=["fade","fade2","blur","blur2","flash","flash2","negative","negative2","burn","burn2","slideLeft","slideLeft2","slideRight","slideRight2","slideUp","slideUp2","slideDown","slideDown2","zoomIn","zoomIn2","zoomOut","zoomOut2","swirlLeft","swirlLeft2","swirlRight","swirlRight2"],this.animations=["kenburns","kenburnsLeft","kenburnsRight","kenburnsUp","kenburnsUpLeft","kenburnsUpRight","kenburnsDown","kenburnsDownLeft","kenburnsDownRight"],this.settings.transitionRegister instanceof Array==!1&&(this.settings.transitionRegister=[this.settings.transitionRegister]),this.settings.animationRegister instanceof Array==!1&&(this.settings.animationRegister=[this.settings.animationRegister]),this.transitions=this.transitions.concat(this.settings.transitionRegister),this.animations=this.animations.concat(this.settings.animationRegister),this.support={objectFit:"objectFit"in document.body.style,transition:"transition"in document.body.style||"WebkitTransition"in document.body.style,video:t.vegas.isVideoCompatible()},this.settings.shuffle===!0&&this.shuffle(),this._init()};e.prototype={_init:function(){var s,i,e,n="BODY"===this.elmt.tagName,o=this.settings.timer,a=this.settings.overlay,r=this;this._preload(),n||(this.$elmt.css("height",this.$elmt.css("height")),s=t('<div class="vegas-wrapper">').css("overflow",this.$elmt.css("overflow")).css("padding",this.$elmt.css("padding")),this.$elmt.css("padding")||s.css("padding-top",this.$elmt.css("padding-top")).css("padding-bottom",this.$elmt.css("padding-bottom")).css("padding-left",this.$elmt.css("padding-left")).css("padding-right",this.$elmt.css("padding-right")),this.$elmt.clone(!0).children().appendTo(s),this.elmt.innerHTML=""),o&&this.support.transition&&(e=t('<div class="vegas-timer"><div class="vegas-timer-progress">'),this.$timer=e,this.$elmt.prepend(e)),a&&(i=t('<div class="vegas-overlay">'),"string"==typeof a&&i.css("background-image","url("+a+")"),this.$overlay=i,this.$elmt.prepend(i)),this.$elmt.addClass("vegas-container"),n||this.$elmt.append(s),setTimeout(function(){r.trigger("init"),r._goto(r.slide),r.settings.autoplay&&r.trigger("play")},1)},_preload:function(){var t,s;for(s=0;s<this.settings.slides.length;s++)(this.settings.preload||this.settings.preloadImages)&&this.settings.slides[s].src&&(t=new Image,t.src=this.settings.slides[s].src),(this.settings.preload||this.settings.preloadVideos)&&this.support.video&&this.settings.slides[s].video&&(this.settings.slides[s].video instanceof Array?this._video(this.settings.slides[s].video):this._video(this.settings.slides[s].video.src))},_random:function(t){return t[Math.floor(Math.random()*t.length)]},_slideShow:function(){var t=this;this.total>1&&!this.paused&&!this.noshow&&(this.timeout=setTimeout(function(){t.next()},this._options("delay")))},_timer:function(t){var s=this;clearTimeout(this.timeout),this.$timer&&(this.$timer.removeClass("vegas-timer-running").find("div").css("transition-duration","0ms"),this.paused||this.noshow||t&&setTimeout(function(){s.$timer.addClass("vegas-timer-running").find("div").css("transition-duration",s._options("delay")-100+"ms")},100))},_video:function(t){var s,e,n=t.toString();return i[n]?i[n]:(t instanceof Array==!1&&(t=[t]),s=document.createElement("video"),s.preload=!0,t.forEach(function(t){e=document.createElement("source"),e.src=t,s.appendChild(e)}),i[n]=s,s)},_fadeOutSound:function(t,s){var i=this,e=s/10,n=t.volume-.09;n>0?(t.volume=n,setTimeout(function(){i._fadeOutSound(t,s)},e)):t.pause()},_fadeInSound:function(t,s){var i=this,e=s/10,n=t.volume+.09;1>n&&(t.volume=n,setTimeout(function(){i._fadeInSound(t,s)},e))},_options:function(t,s){return void 0===s&&(s=this.slide),void 0!==this.settings.slides[s][t]?this.settings.slides[s][t]:this.settings[t]},_goto:function(s){function i(){f._timer(!0),setTimeout(function(){y&&(f.support.transition?(h.css("transition","all "+_+"ms").addClass("vegas-transition-"+y+"-out"),h.each(function(){var t=h.find("video").get(0);t&&(t.volume=1,f._fadeOutSound(t,_))}),e.css("transition","all "+_+"ms").addClass("vegas-transition-"+y+"-in")):e.fadeIn(_));for(var t=0;t<h.length-4;t++)h.eq(t).remove();f.trigger("walk"),f._slideShow()},100)}"undefined"==typeof this.settings.slides[s]&&(s=0),this.slide=s;var e,n,o,a,r,h=this.$elmt.children(".vegas-slide"),d=this.settings.slides[s].src,l=this.settings.slides[s].video,g=this._options("delay"),u=this._options("align"),c=this._options("valign"),p=this._options("cover"),m=this._options("color")||this.$elmt.css("background-color"),f=this,v=h.length,y=this._options("transition"),_=this._options("transitionDuration"),w=this._options("animation"),b=this._options("animationDuration");"repeat"!==p&&(p===!0?p="cover":p===!1&&(p="contain")),("random"===y||y instanceof Array)&&(y=y instanceof Array?this._random(y):this._random(this.transitions)),("random"===w||w instanceof Array)&&(w=w instanceof Array?this._random(w):this._random(this.animations)),("auto"===_||_>g)&&(_=g),"auto"===b&&(b=g),e=t('<div class="vegas-slide"></div>'),this.support.transition&&y&&e.addClass("vegas-transition-"+y),this.support.video&&l?(a=l instanceof Array?this._video(l):this._video(l.src),a.loop=void 0!==l.loop?l.loop:!0,a.muted=void 0!==l.mute?l.mute:!0,a.muted===!1?(a.volume=0,this._fadeInSound(a,_)):a.pause(),o=t(a).addClass("vegas-video").css("background-color",m),this.support.objectFit?o.css("object-position",u+" "+c).css("object-fit",p).css("width","100%").css("height","100%"):"contain"===p&&o.css("width","100%").css("height","100%"),e.append(o)):(r=new Image,n=t('<div class="vegas-slide-inner"></div>').css("background-image","url("+d+")").css("background-color",m).css("background-position",u+" "+c),"repeat"===p?n.css("background-repeat","repeat"):n.css("background-size",p),this.support.transition&&w&&n.addClass("vegas-animation-"+w).css("animation-duration",b+"ms"),e.append(n)),this.support.transition||e.css("display","none"),v?h.eq(v-1).after(e):this.$elmt.prepend(e),f._timer(!1),a?(4===a.readyState&&(a.currentTime=0),a.play(),i()):(r.src=d,r.onload=i)},shuffle:function(){for(var t,s,i=this.total-1;i>0;i--)s=Math.floor(Math.random()*(i+1)),t=this.settings.slides[i],this.settings.slides[i]=this.settings.slides[s],this.settings.slides[s]=t},play:function(){this.paused&&(this.paused=!1,this.next(),this.trigger("play"))},pause:function(){this._timer(!1),this.paused=!0,this.trigger("pause")},toggle:function(){this.paused?this.play():this.pause()},playing:function(){return!this.paused&&!this.noshow},current:function(t){return t?{slide:this.slide,data:this.settings.slides[this.slide]}:this.slide},jump:function(t){0>t||t>this.total-1||t===this.slide||(this.slide=t,this._goto(this.slide))},next:function(){this.slide++,this.slide>=this.total&&(this.slide=0),this._goto(this.slide)},previous:function(){this.slide--,this.slide<0&&(this.slide=this.total-1),this._goto(this.slide)},trigger:function(t){var s=[];s="init"===t?[this.settings]:[this.slide,this.settings.slides[this.slide]],this.$elmt.trigger("vegas"+t,s),"function"==typeof this.settings[t]&&this.settings[t].apply(this.$elmt,s)},options:function(i,e){var n=this.settings.slides.slice();if("object"==typeof i)this.settings=t.extend({},s,t.vegas.defaults,i);else{if("string"!=typeof i)return this.settings;if(void 0===e)return this.settings[i];this.settings[i]=e}this.settings.slides!==n&&(this.total=this.settings.slides.length,this.noshow=this.total<2,this._preload())},destroy:function(){clearTimeout(this.timeout),this.$elmt.removeClass("vegas-container"),this.$elmt.find("> .vegas-slide").remove(),this.$elmt.find("> .vegas-wrapper").clone(!0).children().appendTo(this.$elmt),this.$elmt.find("> .vegas-wrapper").remove(),this.settings.timer&&this.$timer.remove(),this.settings.overlay&&this.$overlay.remove(),this.elmt._vegas=null}},t.fn.vegas=function(t){var s,i=arguments,n=!1;if(void 0===t||"object"==typeof t)return this.each(function(){this._vegas||(this._vegas=new e(this,t))});if("string"==typeof t){if(this.each(function(){var e=this._vegas;if(!e)throw new Error("No Vegas applied to this element.");"function"==typeof e[t]&&"_"!==t[0]?s=e[t].apply(e,[].slice.call(i,1)):n=!0}),n)throw new Error('No method "'+t+'" in Vegas.');return void 0!==s?s:this}},t.vegas={},t.vegas.defaults=s,t.vegas.isVideoCompatible=function(){return!/(Android|webOS|Phone|iPad|iPod|BlackBerry|Windows Phone)/i.test(navigator.userAgent)}}(window.jQuery||window.Zepto);


/*! Magnific Popup - v1.1.0 - 2016-02-20
* http://dimsemenov.com/plugins/magnific-popup/
* Copyright (c) 2016 Dmitry Semenov; */
!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):a("object"==typeof exports?require("jquery"):window.jQuery||window.Zepto)}(function(a){var b,c,d,e,f,g,h="Close",i="BeforeClose",j="AfterClose",k="BeforeAppend",l="MarkupParse",m="Open",n="Change",o="mfp",p="."+o,q="mfp-ready",r="mfp-removing",s="mfp-prevent-close",t=function(){},u=!!window.jQuery,v=a(window),w=function(a,c){b.ev.on(o+a+p,c)},x=function(b,c,d,e){var f=document.createElement("div");return f.className="mfp-"+b,d&&(f.innerHTML=d),e?c&&c.appendChild(f):(f=a(f),c&&f.appendTo(c)),f},y=function(c,d){b.ev.triggerHandler(o+c,d),b.st.callbacks&&(c=c.charAt(0).toLowerCase()+c.slice(1),b.st.callbacks[c]&&b.st.callbacks[c].apply(b,a.isArray(d)?d:[d]))},z=function(c){return c===g&&b.currTemplate.closeBtn||(b.currTemplate.closeBtn=a(b.st.closeMarkup.replace("%title%",b.st.tClose)),g=c),b.currTemplate.closeBtn},A=function(){a.magnificPopup.instance||(b=new t,b.init(),a.magnificPopup.instance=b)},B=function(){var a=document.createElement("p").style,b=["ms","O","Moz","Webkit"];if(void 0!==a.transition)return!0;for(;b.length;)if(b.pop()+"Transition"in a)return!0;return!1};t.prototype={constructor:t,init:function(){var c=navigator.appVersion;b.isLowIE=b.isIE8=document.all&&!document.addEventListener,b.isAndroid=/android/gi.test(c),b.isIOS=/iphone|ipad|ipod/gi.test(c),b.supportsTransition=B(),b.probablyMobile=b.isAndroid||b.isIOS||/(Opera Mini)|Kindle|webOS|BlackBerry|(Opera Mobi)|(Windows Phone)|IEMobile/i.test(navigator.userAgent),d=a(document),b.popupsCache={}},open:function(c){var e;if(c.isObj===!1){b.items=c.items.toArray(),b.index=0;var g,h=c.items;for(e=0;e<h.length;e++)if(g=h[e],g.parsed&&(g=g.el[0]),g===c.el[0]){b.index=e;break}}else b.items=a.isArray(c.items)?c.items:[c.items],b.index=c.index||0;if(b.isOpen)return void b.updateItemHTML();b.types=[],f="",c.mainEl&&c.mainEl.length?b.ev=c.mainEl.eq(0):b.ev=d,c.key?(b.popupsCache[c.key]||(b.popupsCache[c.key]={}),b.currTemplate=b.popupsCache[c.key]):b.currTemplate={},b.st=a.extend(!0,{},a.magnificPopup.defaults,c),b.fixedContentPos="auto"===b.st.fixedContentPos?!b.probablyMobile:b.st.fixedContentPos,b.st.modal&&(b.st.closeOnContentClick=!1,b.st.closeOnBgClick=!1,b.st.showCloseBtn=!1,b.st.enableEscapeKey=!1),b.bgOverlay||(b.bgOverlay=x("bg").on("click"+p,function(){b.close()}),b.wrap=x("wrap").attr("tabindex",-1).on("click"+p,function(a){b._checkIfClose(a.target)&&b.close()}),b.container=x("container",b.wrap)),b.contentContainer=x("content"),b.st.preloader&&(b.preloader=x("preloader",b.container,b.st.tLoading));var i=a.magnificPopup.modules;for(e=0;e<i.length;e++){var j=i[e];j=j.charAt(0).toUpperCase()+j.slice(1),b["init"+j].call(b)}y("BeforeOpen"),b.st.showCloseBtn&&(b.st.closeBtnInside?(w(l,function(a,b,c,d){c.close_replaceWith=z(d.type)}),f+=" mfp-close-btn-in"):b.wrap.append(z())),b.st.alignTop&&(f+=" mfp-align-top"),b.fixedContentPos?b.wrap.css({overflow:b.st.overflowY,overflowX:"hidden",overflowY:b.st.overflowY}):b.wrap.css({top:v.scrollTop(),position:"absolute"}),(b.st.fixedBgPos===!1||"auto"===b.st.fixedBgPos&&!b.fixedContentPos)&&b.bgOverlay.css({height:d.height(),position:"absolute"}),b.st.enableEscapeKey&&d.on("keyup"+p,function(a){27===a.keyCode&&b.close()}),v.on("resize"+p,function(){b.updateSize()}),b.st.closeOnContentClick||(f+=" mfp-auto-cursor"),f&&b.wrap.addClass(f);var k=b.wH=v.height(),n={};if(b.fixedContentPos&&b._hasScrollBar(k)){var o=b._getScrollbarSize();o&&(n.marginRight=o)}b.fixedContentPos&&(b.isIE7?a("body, html").css("overflow","hidden"):n.overflow="hidden");var r=b.st.mainClass;return b.isIE7&&(r+=" mfp-ie7"),r&&b._addClassToMFP(r),b.updateItemHTML(),y("BuildControls"),a("html").css(n),b.bgOverlay.add(b.wrap).prependTo(b.st.prependTo||a(document.body)),b._lastFocusedEl=document.activeElement,setTimeout(function(){b.content?(b._addClassToMFP(q),b._setFocus()):b.bgOverlay.addClass(q),d.on("focusin"+p,b._onFocusIn)},16),b.isOpen=!0,b.updateSize(k),y(m),c},close:function(){b.isOpen&&(y(i),b.isOpen=!1,b.st.removalDelay&&!b.isLowIE&&b.supportsTransition?(b._addClassToMFP(r),setTimeout(function(){b._close()},b.st.removalDelay)):b._close())},_close:function(){y(h);var c=r+" "+q+" ";if(b.bgOverlay.detach(),b.wrap.detach(),b.container.empty(),b.st.mainClass&&(c+=b.st.mainClass+" "),b._removeClassFromMFP(c),b.fixedContentPos){var e={marginRight:""};b.isIE7?a("body, html").css("overflow",""):e.overflow="",a("html").css(e)}d.off("keyup"+p+" focusin"+p),b.ev.off(p),b.wrap.attr("class","mfp-wrap").removeAttr("style"),b.bgOverlay.attr("class","mfp-bg"),b.container.attr("class","mfp-container"),!b.st.showCloseBtn||b.st.closeBtnInside&&b.currTemplate[b.currItem.type]!==!0||b.currTemplate.closeBtn&&b.currTemplate.closeBtn.detach(),b.st.autoFocusLast&&b._lastFocusedEl&&a(b._lastFocusedEl).focus(),b.currItem=null,b.content=null,b.currTemplate=null,b.prevHeight=0,y(j)},updateSize:function(a){if(b.isIOS){var c=document.documentElement.clientWidth/window.innerWidth,d=window.innerHeight*c;b.wrap.css("height",d),b.wH=d}else b.wH=a||v.height();b.fixedContentPos||b.wrap.css("height",b.wH),y("Resize")},updateItemHTML:function(){var c=b.items[b.index];b.contentContainer.detach(),b.content&&b.content.detach(),c.parsed||(c=b.parseEl(b.index));var d=c.type;if(y("BeforeChange",[b.currItem?b.currItem.type:"",d]),b.currItem=c,!b.currTemplate[d]){var f=b.st[d]?b.st[d].markup:!1;y("FirstMarkupParse",f),f?b.currTemplate[d]=a(f):b.currTemplate[d]=!0}e&&e!==c.type&&b.container.removeClass("mfp-"+e+"-holder");var g=b["get"+d.charAt(0).toUpperCase()+d.slice(1)](c,b.currTemplate[d]);b.appendContent(g,d),c.preloaded=!0,y(n,c),e=c.type,b.container.prepend(b.contentContainer),y("AfterChange")},appendContent:function(a,c){b.content=a,a?b.st.showCloseBtn&&b.st.closeBtnInside&&b.currTemplate[c]===!0?b.content.find(".mfp-close").length||b.content.append(z()):b.content=a:b.content="",y(k),b.container.addClass("mfp-"+c+"-holder"),b.contentContainer.append(b.content)},parseEl:function(c){var d,e=b.items[c];if(e.tagName?e={el:a(e)}:(d=e.type,e={data:e,src:e.src}),e.el){for(var f=b.types,g=0;g<f.length;g++)if(e.el.hasClass("mfp-"+f[g])){d=f[g];break}e.src=e.el.attr("data-mfp-src"),e.src||(e.src=e.el.attr("href"))}return e.type=d||b.st.type||"inline",e.index=c,e.parsed=!0,b.items[c]=e,y("ElementParse",e),b.items[c]},addGroup:function(a,c){var d=function(d){d.mfpEl=this,b._openClick(d,a,c)};c||(c={});var e="click.magnificPopup";c.mainEl=a,c.items?(c.isObj=!0,a.off(e).on(e,d)):(c.isObj=!1,c.delegate?a.off(e).on(e,c.delegate,d):(c.items=a,a.off(e).on(e,d)))},_openClick:function(c,d,e){var f=void 0!==e.midClick?e.midClick:a.magnificPopup.defaults.midClick;if(f||!(2===c.which||c.ctrlKey||c.metaKey||c.altKey||c.shiftKey)){var g=void 0!==e.disableOn?e.disableOn:a.magnificPopup.defaults.disableOn;if(g)if(a.isFunction(g)){if(!g.call(b))return!0}else if(v.width()<g)return!0;c.type&&(c.preventDefault(),b.isOpen&&c.stopPropagation()),e.el=a(c.mfpEl),e.delegate&&(e.items=d.find(e.delegate)),b.open(e)}},updateStatus:function(a,d){if(b.preloader){c!==a&&b.container.removeClass("mfp-s-"+c),d||"loading"!==a||(d=b.st.tLoading);var e={status:a,text:d};y("UpdateStatus",e),a=e.status,d=e.text,b.preloader.html(d),b.preloader.find("a").on("click",function(a){a.stopImmediatePropagation()}),b.container.addClass("mfp-s-"+a),c=a}},_checkIfClose:function(c){if(!a(c).hasClass(s)){var d=b.st.closeOnContentClick,e=b.st.closeOnBgClick;if(d&&e)return!0;if(!b.content||a(c).hasClass("mfp-close")||b.preloader&&c===b.preloader[0])return!0;if(c===b.content[0]||a.contains(b.content[0],c)){if(d)return!0}else if(e&&a.contains(document,c))return!0;return!1}},_addClassToMFP:function(a){b.bgOverlay.addClass(a),b.wrap.addClass(a)},_removeClassFromMFP:function(a){this.bgOverlay.removeClass(a),b.wrap.removeClass(a)},_hasScrollBar:function(a){return(b.isIE7?d.height():document.body.scrollHeight)>(a||v.height())},_setFocus:function(){(b.st.focus?b.content.find(b.st.focus).eq(0):b.wrap).focus()},_onFocusIn:function(c){return c.target===b.wrap[0]||a.contains(b.wrap[0],c.target)?void 0:(b._setFocus(),!1)},_parseMarkup:function(b,c,d){var e;d.data&&(c=a.extend(d.data,c)),y(l,[b,c,d]),a.each(c,function(c,d){if(void 0===d||d===!1)return!0;if(e=c.split("_"),e.length>1){var f=b.find(p+"-"+e[0]);if(f.length>0){var g=e[1];"replaceWith"===g?f[0]!==d[0]&&f.replaceWith(d):"img"===g?f.is("img")?f.attr("src",d):f.replaceWith(a("<img>").attr("src",d).attr("class",f.attr("class"))):f.attr(e[1],d)}}else b.find(p+"-"+c).html(d)})},_getScrollbarSize:function(){if(void 0===b.scrollbarSize){var a=document.createElement("div");a.style.cssText="width: 99px; height: 99px; overflow: scroll; position: absolute; top: -9999px;",document.body.appendChild(a),b.scrollbarSize=a.offsetWidth-a.clientWidth,document.body.removeChild(a)}return b.scrollbarSize}},a.magnificPopup={instance:null,proto:t.prototype,modules:[],open:function(b,c){return A(),b=b?a.extend(!0,{},b):{},b.isObj=!0,b.index=c||0,this.instance.open(b)},close:function(){return a.magnificPopup.instance&&a.magnificPopup.instance.close()},registerModule:function(b,c){c.options&&(a.magnificPopup.defaults[b]=c.options),a.extend(this.proto,c.proto),this.modules.push(b)},defaults:{disableOn:0,key:null,midClick:!1,mainClass:"",preloader:!0,focus:"",closeOnContentClick:!1,closeOnBgClick:!0,closeBtnInside:!0,showCloseBtn:!0,enableEscapeKey:!0,modal:!1,alignTop:!1,removalDelay:0,prependTo:null,fixedContentPos:"auto",fixedBgPos:"auto",overflowY:"auto",closeMarkup:'<button title="%title%" type="button" class="mfp-close">&#215;</button>',tClose:"Close (Esc)",tLoading:"Loading...",autoFocusLast:!0}},a.fn.magnificPopup=function(c){A();var d=a(this);if("string"==typeof c)if("open"===c){var e,f=u?d.data("magnificPopup"):d[0].magnificPopup,g=parseInt(arguments[1],10)||0;f.items?e=f.items[g]:(e=d,f.delegate&&(e=e.find(f.delegate)),e=e.eq(g)),b._openClick({mfpEl:e},d,f)}else b.isOpen&&b[c].apply(b,Array.prototype.slice.call(arguments,1));else c=a.extend(!0,{},c),u?d.data("magnificPopup",c):d[0].magnificPopup=c,b.addGroup(d,c);return d};var C,D,E,F="inline",G=function(){E&&(D.after(E.addClass(C)).detach(),E=null)};a.magnificPopup.registerModule(F,{options:{hiddenClass:"hide",markup:"",tNotFound:"Content not found"},proto:{initInline:function(){b.types.push(F),w(h+"."+F,function(){G()})},getInline:function(c,d){if(G(),c.src){var e=b.st.inline,f=a(c.src);if(f.length){var g=f[0].parentNode;g&&g.tagName&&(D||(C=e.hiddenClass,D=x(C),C="mfp-"+C),E=f.after(D).detach().removeClass(C)),b.updateStatus("ready")}else b.updateStatus("error",e.tNotFound),f=a("<div>");return c.inlineElement=f,f}return b.updateStatus("ready"),b._parseMarkup(d,{},c),d}}});var H,I="ajax",J=function(){H&&a(document.body).removeClass(H)},K=function(){J(),b.req&&b.req.abort()};a.magnificPopup.registerModule(I,{options:{settings:null,cursor:"mfp-ajax-cur",tError:'<a href="%url%">The content</a> could not be loaded.'},proto:{initAjax:function(){b.types.push(I),H=b.st.ajax.cursor,w(h+"."+I,K),w("BeforeChange."+I,K)},getAjax:function(c){H&&a(document.body).addClass(H),b.updateStatus("loading");var d=a.extend({url:c.src,success:function(d,e,f){var g={data:d,xhr:f};y("ParseAjax",g),b.appendContent(a(g.data),I),c.finished=!0,J(),b._setFocus(),setTimeout(function(){b.wrap.addClass(q)},16),b.updateStatus("ready"),y("AjaxContentAdded")},error:function(){J(),c.finished=c.loadError=!0,b.updateStatus("error",b.st.ajax.tError.replace("%url%",c.src))}},b.st.ajax.settings);return b.req=a.ajax(d),""}}});var L,M=function(c){if(c.data&&void 0!==c.data.title)return c.data.title;var d=b.st.image.titleSrc;if(d){if(a.isFunction(d))return d.call(b,c);if(c.el)return c.el.attr(d)||""}return""};a.magnificPopup.registerModule("image",{options:{markup:'<div class="mfp-figure"><div class="mfp-close"></div><figure><div class="mfp-img"></div><figcaption><div class="mfp-bottom-bar"><div class="mfp-title"></div><div class="mfp-counter"></div></div></figcaption></figure></div>',cursor:"mfp-zoom-out-cur",titleSrc:"title",verticalFit:!0,tError:'<a href="%url%">The image</a> could not be loaded.'},proto:{initImage:function(){var c=b.st.image,d=".image";b.types.push("image"),w(m+d,function(){"image"===b.currItem.type&&c.cursor&&a(document.body).addClass(c.cursor)}),w(h+d,function(){c.cursor&&a(document.body).removeClass(c.cursor),v.off("resize"+p)}),w("Resize"+d,b.resizeImage),b.isLowIE&&w("AfterChange",b.resizeImage)},resizeImage:function(){var a=b.currItem;if(a&&a.img&&b.st.image.verticalFit){var c=0;b.isLowIE&&(c=parseInt(a.img.css("padding-top"),10)+parseInt(a.img.css("padding-bottom"),10)),a.img.css("max-height",b.wH-c)}},_onImageHasSize:function(a){a.img&&(a.hasSize=!0,L&&clearInterval(L),a.isCheckingImgSize=!1,y("ImageHasSize",a),a.imgHidden&&(b.content&&b.content.removeClass("mfp-loading"),a.imgHidden=!1))},findImageSize:function(a){var c=0,d=a.img[0],e=function(f){L&&clearInterval(L),L=setInterval(function(){return d.naturalWidth>0?void b._onImageHasSize(a):(c>200&&clearInterval(L),c++,void(3===c?e(10):40===c?e(50):100===c&&e(500)))},f)};e(1)},getImage:function(c,d){var e=0,f=function(){c&&(c.img[0].complete?(c.img.off(".mfploader"),c===b.currItem&&(b._onImageHasSize(c),b.updateStatus("ready")),c.hasSize=!0,c.loaded=!0,y("ImageLoadComplete")):(e++,200>e?setTimeout(f,100):g()))},g=function(){c&&(c.img.off(".mfploader"),c===b.currItem&&(b._onImageHasSize(c),b.updateStatus("error",h.tError.replace("%url%",c.src))),c.hasSize=!0,c.loaded=!0,c.loadError=!0)},h=b.st.image,i=d.find(".mfp-img");if(i.length){var j=document.createElement("img");j.className="mfp-img",c.el&&c.el.find("img").length&&(j.alt=c.el.find("img").attr("alt")),c.img=a(j).on("load.mfploader",f).on("error.mfploader",g),j.src=c.src,i.is("img")&&(c.img=c.img.clone()),j=c.img[0],j.naturalWidth>0?c.hasSize=!0:j.width||(c.hasSize=!1)}return b._parseMarkup(d,{title:M(c),img_replaceWith:c.img},c),b.resizeImage(),c.hasSize?(L&&clearInterval(L),c.loadError?(d.addClass("mfp-loading"),b.updateStatus("error",h.tError.replace("%url%",c.src))):(d.removeClass("mfp-loading"),b.updateStatus("ready")),d):(b.updateStatus("loading"),c.loading=!0,c.hasSize||(c.imgHidden=!0,d.addClass("mfp-loading"),b.findImageSize(c)),d)}}});var N,O=function(){return void 0===N&&(N=void 0!==document.createElement("p").style.MozTransform),N};a.magnificPopup.registerModule("zoom",{options:{enabled:!1,easing:"ease-in-out",duration:300,opener:function(a){return a.is("img")?a:a.find("img")}},proto:{initZoom:function(){var a,c=b.st.zoom,d=".zoom";if(c.enabled&&b.supportsTransition){var e,f,g=c.duration,j=function(a){var b=a.clone().removeAttr("style").removeAttr("class").addClass("mfp-animated-image"),d="all "+c.duration/1e3+"s "+c.easing,e={position:"fixed",zIndex:9999,left:0,top:0,"-webkit-backface-visibility":"hidden"},f="transition";return e["-webkit-"+f]=e["-moz-"+f]=e["-o-"+f]=e[f]=d,b.css(e),b},k=function(){b.content.css("visibility","visible")};w("BuildControls"+d,function(){if(b._allowZoom()){if(clearTimeout(e),b.content.css("visibility","hidden"),a=b._getItemToZoom(),!a)return void k();f=j(a),f.css(b._getOffset()),b.wrap.append(f),e=setTimeout(function(){f.css(b._getOffset(!0)),e=setTimeout(function(){k(),setTimeout(function(){f.remove(),a=f=null,y("ZoomAnimationEnded")},16)},g)},16)}}),w(i+d,function(){if(b._allowZoom()){if(clearTimeout(e),b.st.removalDelay=g,!a){if(a=b._getItemToZoom(),!a)return;f=j(a)}f.css(b._getOffset(!0)),b.wrap.append(f),b.content.css("visibility","hidden"),setTimeout(function(){f.css(b._getOffset())},16)}}),w(h+d,function(){b._allowZoom()&&(k(),f&&f.remove(),a=null)})}},_allowZoom:function(){return"image"===b.currItem.type},_getItemToZoom:function(){return b.currItem.hasSize?b.currItem.img:!1},_getOffset:function(c){var d;d=c?b.currItem.img:b.st.zoom.opener(b.currItem.el||b.currItem);var e=d.offset(),f=parseInt(d.css("padding-top"),10),g=parseInt(d.css("padding-bottom"),10);e.top-=a(window).scrollTop()-f;var h={width:d.width(),height:(u?d.innerHeight():d[0].offsetHeight)-g-f};return O()?h["-moz-transform"]=h.transform="translate("+e.left+"px,"+e.top+"px)":(h.left=e.left,h.top=e.top),h}}});var P="iframe",Q="//about:blank",R=function(a){if(b.currTemplate[P]){var c=b.currTemplate[P].find("iframe");c.length&&(a||(c[0].src=Q),b.isIE8&&c.css("display",a?"block":"none"))}};a.magnificPopup.registerModule(P,{options:{markup:'<div class="mfp-iframe-scaler"><div class="mfp-close"></div><iframe class="mfp-iframe" src="//about:blank" frameborder="0" allowfullscreen></iframe></div>',srcAction:"iframe_src",patterns:{youtube:{index:"youtube.com",id:"v=",src:"//www.youtube.com/embed/%id%?autoplay=1"},vimeo:{index:"vimeo.com/",id:"/",src:"//player.vimeo.com/video/%id%?autoplay=1"},gmaps:{index:"//maps.google.",src:"%id%&output=embed"}}},proto:{initIframe:function(){b.types.push(P),w("BeforeChange",function(a,b,c){b!==c&&(b===P?R():c===P&&R(!0))}),w(h+"."+P,function(){R()})},getIframe:function(c,d){var e=c.src,f=b.st.iframe;a.each(f.patterns,function(){return e.indexOf(this.index)>-1?(this.id&&(e="string"==typeof this.id?e.substr(e.lastIndexOf(this.id)+this.id.length,e.length):this.id.call(this,e)),e=this.src.replace("%id%",e),!1):void 0});var g={};return f.srcAction&&(g[f.srcAction]=e),b._parseMarkup(d,g,c),b.updateStatus("ready"),d}}});var S=function(a){var c=b.items.length;return a>c-1?a-c:0>a?c+a:a},T=function(a,b,c){return a.replace(/%curr%/gi,b+1).replace(/%total%/gi,c)};a.magnificPopup.registerModule("gallery",{options:{enabled:!1,arrowMarkup:'<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>',preload:[0,2],navigateByImgClick:!0,arrows:!0,tPrev:"Previous (Left arrow key)",tNext:"Next (Right arrow key)",tCounter:"%curr% of %total%"},proto:{initGallery:function(){var c=b.st.gallery,e=".mfp-gallery";return b.direction=!0,c&&c.enabled?(f+=" mfp-gallery",w(m+e,function(){c.navigateByImgClick&&b.wrap.on("click"+e,".mfp-img",function(){return b.items.length>1?(b.next(),!1):void 0}),d.on("keydown"+e,function(a){37===a.keyCode?b.prev():39===a.keyCode&&b.next()})}),w("UpdateStatus"+e,function(a,c){c.text&&(c.text=T(c.text,b.currItem.index,b.items.length))}),w(l+e,function(a,d,e,f){var g=b.items.length;e.counter=g>1?T(c.tCounter,f.index,g):""}),w("BuildControls"+e,function(){if(b.items.length>1&&c.arrows&&!b.arrowLeft){var d=c.arrowMarkup,e=b.arrowLeft=a(d.replace(/%title%/gi,c.tPrev).replace(/%dir%/gi,"left")).addClass(s),f=b.arrowRight=a(d.replace(/%title%/gi,c.tNext).replace(/%dir%/gi,"right")).addClass(s);e.click(function(){b.prev()}),f.click(function(){b.next()}),b.container.append(e.add(f))}}),w(n+e,function(){b._preloadTimeout&&clearTimeout(b._preloadTimeout),b._preloadTimeout=setTimeout(function(){b.preloadNearbyImages(),b._preloadTimeout=null},16)}),void w(h+e,function(){d.off(e),b.wrap.off("click"+e),b.arrowRight=b.arrowLeft=null})):!1},next:function(){b.direction=!0,b.index=S(b.index+1),b.updateItemHTML()},prev:function(){b.direction=!1,b.index=S(b.index-1),b.updateItemHTML()},goTo:function(a){b.direction=a>=b.index,b.index=a,b.updateItemHTML()},preloadNearbyImages:function(){var a,c=b.st.gallery.preload,d=Math.min(c[0],b.items.length),e=Math.min(c[1],b.items.length);for(a=1;a<=(b.direction?e:d);a++)b._preloadItem(b.index+a);for(a=1;a<=(b.direction?d:e);a++)b._preloadItem(b.index-a)},_preloadItem:function(c){if(c=S(c),!b.items[c].preloaded){var d=b.items[c];d.parsed||(d=b.parseEl(c)),y("LazyLoad",d),"image"===d.type&&(d.img=a('<img class="mfp-img" />').on("load.mfploader",function(){d.hasSize=!0}).on("error.mfploader",function(){d.hasSize=!0,d.loadError=!0,y("LazyLoadError",d)}).attr("src",d.src)),d.preloaded=!0}}}});var U="retina";a.magnificPopup.registerModule(U,{options:{replaceSrc:function(a){return a.src.replace(/\.\w+$/,function(a){return"@2x"+a})},ratio:1},proto:{initRetina:function(){if(window.devicePixelRatio>1){var a=b.st.retina,c=a.ratio;c=isNaN(c)?c():c,c>1&&(w("ImageHasSize."+U,function(a,b){b.img.css({"max-width":b.img[0].naturalWidth/c,width:"100%"})}),w("ElementParse."+U,function(b,d){d.src=a.replaceSrc(d,c)}))}}}}),A()});

/*! WOW - v1.1.2 - 2015-04-07
* Copyright (c) 2015 Matthieu Aussaguel; Licensed MIT */(function(){var a,b,c,d,e,f=function(a,b){return function(){return a.apply(b,arguments)}},g=[].indexOf||function(a){for(var b=0,c=this.length;c>b;b++)if(b in this&&this[b]===a)return b;return-1};b=function(){function a(){}return a.prototype.extend=function(a,b){var c,d;for(c in b)d=b[c],null==a[c]&&(a[c]=d);return a},a.prototype.isMobile=function(a){return/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(a)},a.prototype.createEvent=function(a,b,c,d){var e;return null==b&&(b=!1),null==c&&(c=!1),null==d&&(d=null),null!=document.createEvent?(e=document.createEvent("CustomEvent"),e.initCustomEvent(a,b,c,d)):null!=document.createEventObject?(e=document.createEventObject(),e.eventType=a):e.eventName=a,e},a.prototype.emitEvent=function(a,b){return null!=a.dispatchEvent?a.dispatchEvent(b):b in(null!=a)?a[b]():"on"+b in(null!=a)?a["on"+b]():void 0},a.prototype.addEvent=function(a,b,c){return null!=a.addEventListener?a.addEventListener(b,c,!1):null!=a.attachEvent?a.attachEvent("on"+b,c):a[b]=c},a.prototype.removeEvent=function(a,b,c){return null!=a.removeEventListener?a.removeEventListener(b,c,!1):null!=a.detachEvent?a.detachEvent("on"+b,c):delete a[b]},a.prototype.innerHeight=function(){return"innerHeight"in window?window.innerHeight:document.documentElement.clientHeight},a}(),c=this.WeakMap||this.MozWeakMap||(c=function(){function a(){this.keys=[],this.values=[]}return a.prototype.get=function(a){var b,c,d,e,f;for(f=this.keys,b=d=0,e=f.length;e>d;b=++d)if(c=f[b],c===a)return this.values[b]},a.prototype.set=function(a,b){var c,d,e,f,g;for(g=this.keys,c=e=0,f=g.length;f>e;c=++e)if(d=g[c],d===a)return void(this.values[c]=b);return this.keys.push(a),this.values.push(b)},a}()),a=this.MutationObserver||this.WebkitMutationObserver||this.MozMutationObserver||(a=function(){function a(){"undefined"!=typeof console&&null!==console&&console.warn("MutationObserver is not supported by your browser."),"undefined"!=typeof console&&null!==console&&console.warn("WOW.js cannot detect dom mutations, please call .sync() after loading new content.")}return a.notSupported=!0,a.prototype.observe=function(){},a}()),d=this.getComputedStyle||function(a){return this.getPropertyValue=function(b){var c;return"float"===b&&(b="styleFloat"),e.test(b)&&b.replace(e,function(a,b){return b.toUpperCase()}),(null!=(c=a.currentStyle)?c[b]:void 0)||null},this},e=/(\-([a-z]){1})/g,this.WOW=function(){function e(a){null==a&&(a={}),this.scrollCallback=f(this.scrollCallback,this),this.scrollHandler=f(this.scrollHandler,this),this.resetAnimation=f(this.resetAnimation,this),this.start=f(this.start,this),this.scrolled=!0,this.config=this.util().extend(a,this.defaults),this.animationNameCache=new c,this.wowEvent=this.util().createEvent(this.config.boxClass)}return e.prototype.defaults={boxClass:"wow",animateClass:"animated",offset:0,mobile:!0,live:!0,callback:null},e.prototype.init=function(){var a;return this.element=window.document.documentElement,"interactive"===(a=document.readyState)||"complete"===a?this.start():this.util().addEvent(document,"DOMContentLoaded",this.start),this.finished=[]},e.prototype.start=function(){var b,c,d,e;if(this.stopped=!1,this.boxes=function(){var a,c,d,e;for(d=this.element.querySelectorAll("."+this.config.boxClass),e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.all=function(){var a,c,d,e;for(d=this.boxes,e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.boxes.length)if(this.disabled())this.resetStyle();else for(e=this.boxes,c=0,d=e.length;d>c;c++)b=e[c],this.applyStyle(b,!0);return this.disabled()||(this.util().addEvent(window,"scroll",this.scrollHandler),this.util().addEvent(window,"resize",this.scrollHandler),this.interval=setInterval(this.scrollCallback,50)),this.config.live?new a(function(a){return function(b){var c,d,e,f,g;for(g=[],c=0,d=b.length;d>c;c++)f=b[c],g.push(function(){var a,b,c,d;for(c=f.addedNodes||[],d=[],a=0,b=c.length;b>a;a++)e=c[a],d.push(this.doSync(e));return d}.call(a));return g}}(this)).observe(document.body,{childList:!0,subtree:!0}):void 0},e.prototype.stop=function(){return this.stopped=!0,this.util().removeEvent(window,"scroll",this.scrollHandler),this.util().removeEvent(window,"resize",this.scrollHandler),null!=this.interval?clearInterval(this.interval):void 0},e.prototype.sync=function(){return a.notSupported?this.doSync(this.element):void 0},e.prototype.doSync=function(a){var b,c,d,e,f;if(null==a&&(a=this.element),1===a.nodeType){for(a=a.parentNode||a,e=a.querySelectorAll("."+this.config.boxClass),f=[],c=0,d=e.length;d>c;c++)b=e[c],g.call(this.all,b)<0?(this.boxes.push(b),this.all.push(b),this.stopped||this.disabled()?this.resetStyle():this.applyStyle(b,!0),f.push(this.scrolled=!0)):f.push(void 0);return f}},e.prototype.show=function(a){return this.applyStyle(a),a.className=a.className+" "+this.config.animateClass,null!=this.config.callback&&this.config.callback(a),this.util().emitEvent(a,this.wowEvent),this.util().addEvent(a,"animationend",this.resetAnimation),this.util().addEvent(a,"oanimationend",this.resetAnimation),this.util().addEvent(a,"webkitAnimationEnd",this.resetAnimation),this.util().addEvent(a,"MSAnimationEnd",this.resetAnimation),a},e.prototype.applyStyle=function(a,b){var c,d,e;return d=a.getAttribute("data-wow-duration"),c=a.getAttribute("data-wow-delay"),e=a.getAttribute("data-wow-iteration"),this.animate(function(f){return function(){return f.customStyle(a,b,d,c,e)}}(this))},e.prototype.animate=function(){return"requestAnimationFrame"in window?function(a){return window.requestAnimationFrame(a)}:function(a){return a()}}(),e.prototype.resetStyle=function(){var a,b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],e.push(a.style.visibility="visible");return e},e.prototype.resetAnimation=function(a){var b;return a.type.toLowerCase().indexOf("animationend")>=0?(b=a.target||a.srcElement,b.className=b.className.replace(this.config.animateClass,"").trim()):void 0},e.prototype.customStyle=function(a,b,c,d,e){return b&&this.cacheAnimationName(a),a.style.visibility=b?"hidden":"visible",c&&this.vendorSet(a.style,{animationDuration:c}),d&&this.vendorSet(a.style,{animationDelay:d}),e&&this.vendorSet(a.style,{animationIterationCount:e}),this.vendorSet(a.style,{animationName:b?"none":this.cachedAnimationName(a)}),a},e.prototype.vendors=["moz","webkit"],e.prototype.vendorSet=function(a,b){var c,d,e,f;d=[];for(c in b)e=b[c],a[""+c]=e,d.push(function(){var b,d,g,h;for(g=this.vendors,h=[],b=0,d=g.length;d>b;b++)f=g[b],h.push(a[""+f+c.charAt(0).toUpperCase()+c.substr(1)]=e);return h}.call(this));return d},e.prototype.vendorCSS=function(a,b){var c,e,f,g,h,i;for(h=d(a),g=h.getPropertyCSSValue(b),f=this.vendors,c=0,e=f.length;e>c;c++)i=f[c],g=g||h.getPropertyCSSValue("-"+i+"-"+b);return g},e.prototype.animationName=function(a){var b;try{b=this.vendorCSS(a,"animation-name").cssText}catch(c){b=d(a).getPropertyValue("animation-name")}return"none"===b?"":b},e.prototype.cacheAnimationName=function(a){return this.animationNameCache.set(a,this.animationName(a))},e.prototype.cachedAnimationName=function(a){return this.animationNameCache.get(a)},e.prototype.scrollHandler=function(){return this.scrolled=!0},e.prototype.scrollCallback=function(){var a;return!this.scrolled||(this.scrolled=!1,this.boxes=function(){var b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],a&&(this.isVisible(a)?this.show(a):e.push(a));return e}.call(this),this.boxes.length||this.config.live)?void 0:this.stop()},e.prototype.offsetTop=function(a){for(var b;void 0===a.offsetTop;)a=a.parentNode;for(b=a.offsetTop;a=a.offsetParent;)b+=a.offsetTop;return b},e.prototype.isVisible=function(a){var b,c,d,e,f;return c=a.getAttribute("data-wow-offset")||this.config.offset,f=window.pageYOffset,e=f+Math.min(this.element.clientHeight,this.util().innerHeight())-c,d=this.offsetTop(a),b=d+a.clientHeight,e>=d&&b>=f},e.prototype.util=function(){return null!=this._util?this._util:this._util=new b},e.prototype.disabled=function(){return!this.config.mobile&&this.util().isMobile(navigator.userAgent)},e}()}).call(this);

/*! VelocityJS.org (1.2.3). (C) 2014 Julian Shapiro. MIT @license: en.wikipedia.org/wiki/MIT_License */
/*! VelocityJS.org jQuery Shim (1.0.1). (C) 2014 The jQuery Foundation. MIT @license: en.wikipedia.org/wiki/MIT_License. */
!function(a){function b(a){var b=a.length,d=c.type(a);return"function"===d||c.isWindow(a)?!1:1===a.nodeType&&b?!0:"array"===d||0===b||"number"==typeof b&&b>0&&b-1 in a}if(!a.jQuery){var c=function(a,b){return new c.fn.init(a,b)};c.isWindow=function(a){return null!=a&&a==a.window},c.type=function(a){return null==a?a+"":"object"==typeof a||"function"==typeof a?e[g.call(a)]||"object":typeof a},c.isArray=Array.isArray||function(a){return"array"===c.type(a)},c.isPlainObject=function(a){var b;if(!a||"object"!==c.type(a)||a.nodeType||c.isWindow(a))return!1;try{if(a.constructor&&!f.call(a,"constructor")&&!f.call(a.constructor.prototype,"isPrototypeOf"))return!1}catch(d){return!1}for(b in a);return void 0===b||f.call(a,b)},c.each=function(a,c,d){var e,f=0,g=a.length,h=b(a);if(d){if(h)for(;g>f&&(e=c.apply(a[f],d),e!==!1);f++);else for(f in a)if(e=c.apply(a[f],d),e===!1)break}else if(h)for(;g>f&&(e=c.call(a[f],f,a[f]),e!==!1);f++);else for(f in a)if(e=c.call(a[f],f,a[f]),e===!1)break;return a},c.data=function(a,b,e){if(void 0===e){var f=a[c.expando],g=f&&d[f];if(void 0===b)return g;if(g&&b in g)return g[b]}else if(void 0!==b){var f=a[c.expando]||(a[c.expando]=++c.uuid);return d[f]=d[f]||{},d[f][b]=e,e}},c.removeData=function(a,b){var e=a[c.expando],f=e&&d[e];f&&c.each(b,function(a,b){delete f[b]})},c.extend=function(){var a,b,d,e,f,g,h=arguments[0]||{},i=1,j=arguments.length,k=!1;for("boolean"==typeof h&&(k=h,h=arguments[i]||{},i++),"object"!=typeof h&&"function"!==c.type(h)&&(h={}),i===j&&(h=this,i--);j>i;i++)if(null!=(f=arguments[i]))for(e in f)a=h[e],d=f[e],h!==d&&(k&&d&&(c.isPlainObject(d)||(b=c.isArray(d)))?(b?(b=!1,g=a&&c.isArray(a)?a:[]):g=a&&c.isPlainObject(a)?a:{},h[e]=c.extend(k,g,d)):void 0!==d&&(h[e]=d));return h},c.queue=function(a,d,e){function f(a,c){var d=c||[];return null!=a&&(b(Object(a))?!function(a,b){for(var c=+b.length,d=0,e=a.length;c>d;)a[e++]=b[d++];if(c!==c)for(;void 0!==b[d];)a[e++]=b[d++];return a.length=e,a}(d,"string"==typeof a?[a]:a):[].push.call(d,a)),d}if(a){d=(d||"fx")+"queue";var g=c.data(a,d);return e?(!g||c.isArray(e)?g=c.data(a,d,f(e)):g.push(e),g):g||[]}},c.dequeue=function(a,b){c.each(a.nodeType?[a]:a,function(a,d){b=b||"fx";var e=c.queue(d,b),f=e.shift();"inprogress"===f&&(f=e.shift()),f&&("fx"===b&&e.unshift("inprogress"),f.call(d,function(){c.dequeue(d,b)}))})},c.fn=c.prototype={init:function(a){if(a.nodeType)return this[0]=a,this;throw new Error("Not a DOM node.")},offset:function(){var b=this[0].getBoundingClientRect?this[0].getBoundingClientRect():{top:0,left:0};return{top:b.top+(a.pageYOffset||document.scrollTop||0)-(document.clientTop||0),left:b.left+(a.pageXOffset||document.scrollLeft||0)-(document.clientLeft||0)}},position:function(){function a(){for(var a=this.offsetParent||document;a&&"html"===!a.nodeType.toLowerCase&&"static"===a.style.position;)a=a.offsetParent;return a||document}var b=this[0],a=a.apply(b),d=this.offset(),e=/^(?:body|html)$/i.test(a.nodeName)?{top:0,left:0}:c(a).offset();return d.top-=parseFloat(b.style.marginTop)||0,d.left-=parseFloat(b.style.marginLeft)||0,a.style&&(e.top+=parseFloat(a.style.borderTopWidth)||0,e.left+=parseFloat(a.style.borderLeftWidth)||0),{top:d.top-e.top,left:d.left-e.left}}};var d={};c.expando="velocity"+(new Date).getTime(),c.uuid=0;for(var e={},f=e.hasOwnProperty,g=e.toString,h="Boolean Number String Function Array Date RegExp Object Error".split(" "),i=0;i<h.length;i++)e["[object "+h[i]+"]"]=h[i].toLowerCase();c.fn.init.prototype=c.fn,a.Velocity={Utilities:c}}}(window),function(a){"object"==typeof module&&"object"==typeof module.exports?module.exports=a():"function"==typeof define&&define.amd?define(a):a()}(function(){return function(a,b,c,d){function e(a){for(var b=-1,c=a?a.length:0,d=[];++b<c;){var e=a[b];e&&d.push(e)}return d}function f(a){return p.isWrapped(a)?a=[].slice.call(a):p.isNode(a)&&(a=[a]),a}function g(a){var b=m.data(a,"velocity");return null===b?d:b}function h(a){return function(b){return Math.round(b*a)*(1/a)}}function i(a,c,d,e){function f(a,b){return 1-3*b+3*a}function g(a,b){return 3*b-6*a}function h(a){return 3*a}function i(a,b,c){return((f(b,c)*a+g(b,c))*a+h(b))*a}function j(a,b,c){return 3*f(b,c)*a*a+2*g(b,c)*a+h(b)}function k(b,c){for(var e=0;p>e;++e){var f=j(c,a,d);if(0===f)return c;var g=i(c,a,d)-b;c-=g/f}return c}function l(){for(var b=0;t>b;++b)x[b]=i(b*u,a,d)}function m(b,c,e){var f,g,h=0;do g=c+(e-c)/2,f=i(g,a,d)-b,f>0?e=g:c=g;while(Math.abs(f)>r&&++h<s);return g}function n(b){for(var c=0,e=1,f=t-1;e!=f&&x[e]<=b;++e)c+=u;--e;var g=(b-x[e])/(x[e+1]-x[e]),h=c+g*u,i=j(h,a,d);return i>=q?k(b,h):0==i?h:m(b,c,c+u)}function o(){y=!0,(a!=c||d!=e)&&l()}var p=4,q=.001,r=1e-7,s=10,t=11,u=1/(t-1),v="Float32Array"in b;if(4!==arguments.length)return!1;for(var w=0;4>w;++w)if("number"!=typeof arguments[w]||isNaN(arguments[w])||!isFinite(arguments[w]))return!1;a=Math.min(a,1),d=Math.min(d,1),a=Math.max(a,0),d=Math.max(d,0);var x=v?new Float32Array(t):new Array(t),y=!1,z=function(b){return y||o(),a===c&&d===e?b:0===b?0:1===b?1:i(n(b),c,e)};z.getControlPoints=function(){return[{x:a,y:c},{x:d,y:e}]};var A="generateBezier("+[a,c,d,e]+")";return z.toString=function(){return A},z}function j(a,b){var c=a;return p.isString(a)?t.Easings[a]||(c=!1):c=p.isArray(a)&&1===a.length?h.apply(null,a):p.isArray(a)&&2===a.length?u.apply(null,a.concat([b])):p.isArray(a)&&4===a.length?i.apply(null,a):!1,c===!1&&(c=t.Easings[t.defaults.easing]?t.defaults.easing:s),c}function k(a){if(a){var b=(new Date).getTime(),c=t.State.calls.length;c>1e4&&(t.State.calls=e(t.State.calls));for(var f=0;c>f;f++)if(t.State.calls[f]){var h=t.State.calls[f],i=h[0],j=h[2],n=h[3],o=!!n,q=null;n||(n=t.State.calls[f][3]=b-16);for(var r=Math.min((b-n)/j.duration,1),s=0,u=i.length;u>s;s++){var w=i[s],y=w.element;if(g(y)){var z=!1;if(j.display!==d&&null!==j.display&&"none"!==j.display){if("flex"===j.display){var A=["-webkit-box","-moz-box","-ms-flexbox","-webkit-flex"];m.each(A,function(a,b){v.setPropertyValue(y,"display",b)})}v.setPropertyValue(y,"display",j.display)}j.visibility!==d&&"hidden"!==j.visibility&&v.setPropertyValue(y,"visibility",j.visibility);for(var B in w)if("element"!==B){var C,D=w[B],E=p.isString(D.easing)?t.Easings[D.easing]:D.easing;if(1===r)C=D.endValue;else{var F=D.endValue-D.startValue;if(C=D.startValue+F*E(r,j,F),!o&&C===D.currentValue)continue}if(D.currentValue=C,"tween"===B)q=C;else{if(v.Hooks.registered[B]){var G=v.Hooks.getRoot(B),H=g(y).rootPropertyValueCache[G];H&&(D.rootPropertyValue=H)}var I=v.setPropertyValue(y,B,D.currentValue+(0===parseFloat(C)?"":D.unitType),D.rootPropertyValue,D.scrollData);v.Hooks.registered[B]&&(g(y).rootPropertyValueCache[G]=v.Normalizations.registered[G]?v.Normalizations.registered[G]("extract",null,I[1]):I[1]),"transform"===I[0]&&(z=!0)}}j.mobileHA&&g(y).transformCache.translate3d===d&&(g(y).transformCache.translate3d="(0px, 0px, 0px)",z=!0),z&&v.flushTransformCache(y)}}j.display!==d&&"none"!==j.display&&(t.State.calls[f][2].display=!1),j.visibility!==d&&"hidden"!==j.visibility&&(t.State.calls[f][2].visibility=!1),j.progress&&j.progress.call(h[1],h[1],r,Math.max(0,n+j.duration-b),n,q),1===r&&l(f)}}t.State.isTicking&&x(k)}function l(a,b){if(!t.State.calls[a])return!1;for(var c=t.State.calls[a][0],e=t.State.calls[a][1],f=t.State.calls[a][2],h=t.State.calls[a][4],i=!1,j=0,k=c.length;k>j;j++){var l=c[j].element;if(b||f.loop||("none"===f.display&&v.setPropertyValue(l,"display",f.display),"hidden"===f.visibility&&v.setPropertyValue(l,"visibility",f.visibility)),f.loop!==!0&&(m.queue(l)[1]===d||!/\.velocityQueueEntryFlag/i.test(m.queue(l)[1]))&&g(l)){g(l).isAnimating=!1,g(l).rootPropertyValueCache={};var n=!1;m.each(v.Lists.transforms3D,function(a,b){var c=/^scale/.test(b)?1:0,e=g(l).transformCache[b];g(l).transformCache[b]!==d&&new RegExp("^\\("+c+"[^.]").test(e)&&(n=!0,delete g(l).transformCache[b])}),f.mobileHA&&(n=!0,delete g(l).transformCache.translate3d),n&&v.flushTransformCache(l),v.Values.removeClass(l,"velocity-animating")}if(!b&&f.complete&&!f.loop&&j===k-1)try{f.complete.call(e,e)}catch(o){setTimeout(function(){throw o},1)}h&&f.loop!==!0&&h(e),g(l)&&f.loop===!0&&!b&&(m.each(g(l).tweensContainer,function(a,b){/^rotate/.test(a)&&360===parseFloat(b.endValue)&&(b.endValue=0,b.startValue=360),/^backgroundPosition/.test(a)&&100===parseFloat(b.endValue)&&"%"===b.unitType&&(b.endValue=0,b.startValue=100)}),t(l,"reverse",{loop:!0,delay:f.delay})),f.queue!==!1&&m.dequeue(l,f.queue)}t.State.calls[a]=!1;for(var p=0,q=t.State.calls.length;q>p;p++)if(t.State.calls[p]!==!1){i=!0;break}i===!1&&(t.State.isTicking=!1,delete t.State.calls,t.State.calls=[])}var m,n=function(){if(c.documentMode)return c.documentMode;for(var a=7;a>4;a--){var b=c.createElement("div");if(b.innerHTML="<!--[if IE "+a+"]><span></span><![endif]-->",b.getElementsByTagName("span").length)return b=null,a}return d}(),o=function(){var a=0;return b.webkitRequestAnimationFrame||b.mozRequestAnimationFrame||function(b){var c,d=(new Date).getTime();return c=Math.max(0,16-(d-a)),a=d+c,setTimeout(function(){b(d+c)},c)}}(),p={isString:function(a){return"string"==typeof a},isArray:Array.isArray||function(a){return"[object Array]"===Object.prototype.toString.call(a)},isFunction:function(a){return"[object Function]"===Object.prototype.toString.call(a)},isNode:function(a){return a&&a.nodeType},isNodeList:function(a){return"object"==typeof a&&/^\[object (HTMLCollection|NodeList|Object)\]$/.test(Object.prototype.toString.call(a))&&a.length!==d&&(0===a.length||"object"==typeof a[0]&&a[0].nodeType>0)},isWrapped:function(a){return a&&(a.jquery||b.Zepto&&b.Zepto.zepto.isZ(a))},isSVG:function(a){return b.SVGElement&&a instanceof b.SVGElement},isEmptyObject:function(a){for(var b in a)return!1;return!0}},q=!1;if(a.fn&&a.fn.jquery?(m=a,q=!0):m=b.Velocity.Utilities,8>=n&&!q)throw new Error("Velocity: IE8 and below require jQuery to be loaded before Velocity.");if(7>=n)return void(jQuery.fn.velocity=jQuery.fn.animate);var r=400,s="swing",t={State:{isMobile:/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent),isAndroid:/Android/i.test(navigator.userAgent),isGingerbread:/Android 2\.3\.[3-7]/i.test(navigator.userAgent),isChrome:b.chrome,isFirefox:/Firefox/i.test(navigator.userAgent),prefixElement:c.createElement("div"),prefixMatches:{},scrollAnchor:null,scrollPropertyLeft:null,scrollPropertyTop:null,isTicking:!1,calls:[]},CSS:{},Utilities:m,Redirects:{},Easings:{},Promise:b.Promise,defaults:{queue:"",duration:r,easing:s,begin:d,complete:d,progress:d,display:d,visibility:d,loop:!1,delay:!1,mobileHA:!0,_cacheValues:!0},init:function(a){m.data(a,"velocity",{isSVG:p.isSVG(a),isAnimating:!1,computedStyle:null,tweensContainer:null,rootPropertyValueCache:{},transformCache:{}})},hook:null,mock:!1,version:{major:1,minor:2,patch:2},debug:!1};b.pageYOffset!==d?(t.State.scrollAnchor=b,t.State.scrollPropertyLeft="pageXOffset",t.State.scrollPropertyTop="pageYOffset"):(t.State.scrollAnchor=c.documentElement||c.body.parentNode||c.body,t.State.scrollPropertyLeft="scrollLeft",t.State.scrollPropertyTop="scrollTop");var u=function(){function a(a){return-a.tension*a.x-a.friction*a.v}function b(b,c,d){var e={x:b.x+d.dx*c,v:b.v+d.dv*c,tension:b.tension,friction:b.friction};return{dx:e.v,dv:a(e)}}function c(c,d){var e={dx:c.v,dv:a(c)},f=b(c,.5*d,e),g=b(c,.5*d,f),h=b(c,d,g),i=1/6*(e.dx+2*(f.dx+g.dx)+h.dx),j=1/6*(e.dv+2*(f.dv+g.dv)+h.dv);return c.x=c.x+i*d,c.v=c.v+j*d,c}return function d(a,b,e){var f,g,h,i={x:-1,v:0,tension:null,friction:null},j=[0],k=0,l=1e-4,m=.016;for(a=parseFloat(a)||500,b=parseFloat(b)||20,e=e||null,i.tension=a,i.friction=b,f=null!==e,f?(k=d(a,b),g=k/e*m):g=m;;)if(h=c(h||i,g),j.push(1+h.x),k+=16,!(Math.abs(h.x)>l&&Math.abs(h.v)>l))break;return f?function(a){return j[a*(j.length-1)|0]}:k}}();t.Easings={linear:function(a){return a},swing:function(a){return.5-Math.cos(a*Math.PI)/2},spring:function(a){return 1-Math.cos(4.5*a*Math.PI)*Math.exp(6*-a)}},m.each([["ease",[.25,.1,.25,1]],["ease-in",[.42,0,1,1]],["ease-out",[0,0,.58,1]],["ease-in-out",[.42,0,.58,1]],["easeInSine",[.47,0,.745,.715]],["easeOutSine",[.39,.575,.565,1]],["easeInOutSine",[.445,.05,.55,.95]],["easeInQuad",[.55,.085,.68,.53]],["easeOutQuad",[.25,.46,.45,.94]],["easeInOutQuad",[.455,.03,.515,.955]],["easeInCubic",[.55,.055,.675,.19]],["easeOutCubic",[.215,.61,.355,1]],["easeInOutCubic",[.645,.045,.355,1]],["easeInQuart",[.895,.03,.685,.22]],["easeOutQuart",[.165,.84,.44,1]],["easeInOutQuart",[.77,0,.175,1]],["easeInQuint",[.755,.05,.855,.06]],["easeOutQuint",[.23,1,.32,1]],["easeInOutQuint",[.86,0,.07,1]],["easeInExpo",[.95,.05,.795,.035]],["easeOutExpo",[.19,1,.22,1]],["easeInOutExpo",[1,0,0,1]],["easeInCirc",[.6,.04,.98,.335]],["easeOutCirc",[.075,.82,.165,1]],["easeInOutCirc",[.785,.135,.15,.86]]],function(a,b){t.Easings[b[0]]=i.apply(null,b[1])});var v=t.CSS={RegEx:{isHex:/^#([A-f\d]{3}){1,2}$/i,valueUnwrap:/^[A-z]+\((.*)\)$/i,wrappedValueAlreadyExtracted:/[0-9.]+ [0-9.]+ [0-9.]+( [0-9.]+)?/,valueSplit:/([A-z]+\(.+\))|(([A-z0-9#-.]+?)(?=\s|$))/gi},Lists:{colors:["fill","stroke","stopColor","color","backgroundColor","borderColor","borderTopColor","borderRightColor","borderBottomColor","borderLeftColor","outlineColor"],transformsBase:["translateX","translateY","scale","scaleX","scaleY","skewX","skewY","rotateZ"],transforms3D:["transformPerspective","translateZ","scaleZ","rotateX","rotateY"]},Hooks:{templates:{textShadow:["Color X Y Blur","black 0px 0px 0px"],boxShadow:["Color X Y Blur Spread","black 0px 0px 0px 0px"],clip:["Top Right Bottom Left","0px 0px 0px 0px"],backgroundPosition:["X Y","0% 0%"],transformOrigin:["X Y Z","50% 50% 0px"],perspectiveOrigin:["X Y","50% 50%"]},registered:{},register:function(){for(var a=0;a<v.Lists.colors.length;a++){var b="color"===v.Lists.colors[a]?"0 0 0 1":"255 255 255 1";v.Hooks.templates[v.Lists.colors[a]]=["Red Green Blue Alpha",b]}var c,d,e;if(n)for(c in v.Hooks.templates){d=v.Hooks.templates[c],e=d[0].split(" ");var f=d[1].match(v.RegEx.valueSplit);"Color"===e[0]&&(e.push(e.shift()),f.push(f.shift()),v.Hooks.templates[c]=[e.join(" "),f.join(" ")])}for(c in v.Hooks.templates){d=v.Hooks.templates[c],e=d[0].split(" ");for(var a in e){var g=c+e[a],h=a;v.Hooks.registered[g]=[c,h]}}},getRoot:function(a){var b=v.Hooks.registered[a];return b?b[0]:a},cleanRootPropertyValue:function(a,b){return v.RegEx.valueUnwrap.test(b)&&(b=b.match(v.RegEx.valueUnwrap)[1]),v.Values.isCSSNullValue(b)&&(b=v.Hooks.templates[a][1]),b},extractValue:function(a,b){var c=v.Hooks.registered[a];if(c){var d=c[0],e=c[1];return b=v.Hooks.cleanRootPropertyValue(d,b),b.toString().match(v.RegEx.valueSplit)[e]}return b},injectValue:function(a,b,c){var d=v.Hooks.registered[a];if(d){var e,f,g=d[0],h=d[1];return c=v.Hooks.cleanRootPropertyValue(g,c),e=c.toString().match(v.RegEx.valueSplit),e[h]=b,f=e.join(" ")}return c}},Normalizations:{registered:{clip:function(a,b,c){switch(a){case"name":return"clip";case"extract":var d;return v.RegEx.wrappedValueAlreadyExtracted.test(c)?d=c:(d=c.toString().match(v.RegEx.valueUnwrap),d=d?d[1].replace(/,(\s+)?/g," "):c),d;case"inject":return"rect("+c+")"}},blur:function(a,b,c){switch(a){case"name":return t.State.isFirefox?"filter":"-webkit-filter";case"extract":var d=parseFloat(c);if(!d&&0!==d){var e=c.toString().match(/blur\(([0-9]+[A-z]+)\)/i);d=e?e[1]:0}return d;case"inject":return parseFloat(c)?"blur("+c+")":"none"}},opacity:function(a,b,c){if(8>=n)switch(a){case"name":return"filter";case"extract":var d=c.toString().match(/alpha\(opacity=(.*)\)/i);return c=d?d[1]/100:1;case"inject":return b.style.zoom=1,parseFloat(c)>=1?"":"alpha(opacity="+parseInt(100*parseFloat(c),10)+")"}else switch(a){case"name":return"opacity";case"extract":return c;case"inject":return c}}},register:function(){9>=n||t.State.isGingerbread||(v.Lists.transformsBase=v.Lists.transformsBase.concat(v.Lists.transforms3D));for(var a=0;a<v.Lists.transformsBase.length;a++)!function(){var b=v.Lists.transformsBase[a];v.Normalizations.registered[b]=function(a,c,e){switch(a){case"name":return"transform";case"extract":return g(c)===d||g(c).transformCache[b]===d?/^scale/i.test(b)?1:0:g(c).transformCache[b].replace(/[()]/g,"");case"inject":var f=!1;switch(b.substr(0,b.length-1)){case"translate":f=!/(%|px|em|rem|vw|vh|\d)$/i.test(e);break;case"scal":case"scale":t.State.isAndroid&&g(c).transformCache[b]===d&&1>e&&(e=1),f=!/(\d)$/i.test(e);break;case"skew":f=!/(deg|\d)$/i.test(e);break;case"rotate":f=!/(deg|\d)$/i.test(e)}return f||(g(c).transformCache[b]="("+e+")"),g(c).transformCache[b]}}}();for(var a=0;a<v.Lists.colors.length;a++)!function(){var b=v.Lists.colors[a];v.Normalizations.registered[b]=function(a,c,e){switch(a){case"name":return b;case"extract":var f;if(v.RegEx.wrappedValueAlreadyExtracted.test(e))f=e;else{var g,h={black:"rgb(0, 0, 0)",blue:"rgb(0, 0, 255)",gray:"rgb(128, 128, 128)",green:"rgb(0, 128, 0)",red:"rgb(255, 0, 0)",white:"rgb(255, 255, 255)"};/^[A-z]+$/i.test(e)?g=h[e]!==d?h[e]:h.black:v.RegEx.isHex.test(e)?g="rgb("+v.Values.hexToRgb(e).join(" ")+")":/^rgba?\(/i.test(e)||(g=h.black),f=(g||e).toString().match(v.RegEx.valueUnwrap)[1].replace(/,(\s+)?/g," ")}return 8>=n||3!==f.split(" ").length||(f+=" 1"),f;case"inject":return 8>=n?4===e.split(" ").length&&(e=e.split(/\s+/).slice(0,3).join(" ")):3===e.split(" ").length&&(e+=" 1"),(8>=n?"rgb":"rgba")+"("+e.replace(/\s+/g,",").replace(/\.(\d)+(?=,)/g,"")+")"}}}()}},Names:{camelCase:function(a){return a.replace(/-(\w)/g,function(a,b){return b.toUpperCase()})},SVGAttribute:function(a){var b="width|height|x|y|cx|cy|r|rx|ry|x1|x2|y1|y2";return(n||t.State.isAndroid&&!t.State.isChrome)&&(b+="|transform"),new RegExp("^("+b+")$","i").test(a)},prefixCheck:function(a){if(t.State.prefixMatches[a])return[t.State.prefixMatches[a],!0];for(var b=["","Webkit","Moz","ms","O"],c=0,d=b.length;d>c;c++){var e;if(e=0===c?a:b[c]+a.replace(/^\w/,function(a){return a.toUpperCase()}),p.isString(t.State.prefixElement.style[e]))return t.State.prefixMatches[a]=e,[e,!0]}return[a,!1]}},Values:{hexToRgb:function(a){var b,c=/^#?([a-f\d])([a-f\d])([a-f\d])$/i,d=/^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i;return a=a.replace(c,function(a,b,c,d){return b+b+c+c+d+d}),b=d.exec(a),b?[parseInt(b[1],16),parseInt(b[2],16),parseInt(b[3],16)]:[0,0,0]},isCSSNullValue:function(a){return 0==a||/^(none|auto|transparent|(rgba\(0, ?0, ?0, ?0\)))$/i.test(a)},getUnitType:function(a){return/^(rotate|skew)/i.test(a)?"deg":/(^(scale|scaleX|scaleY|scaleZ|alpha|flexGrow|flexHeight|zIndex|fontWeight)$)|((opacity|red|green|blue|alpha)$)/i.test(a)?"":"px"},getDisplayType:function(a){var b=a&&a.tagName.toString().toLowerCase();return/^(b|big|i|small|tt|abbr|acronym|cite|code|dfn|em|kbd|strong|samp|var|a|bdo|br|img|map|object|q|script|span|sub|sup|button|input|label|select|textarea)$/i.test(b)?"inline":/^(li)$/i.test(b)?"list-item":/^(tr)$/i.test(b)?"table-row":/^(table)$/i.test(b)?"table":/^(tbody)$/i.test(b)?"table-row-group":"block"},addClass:function(a,b){a.classList?a.classList.add(b):a.className+=(a.className.length?" ":"")+b},removeClass:function(a,b){a.classList?a.classList.remove(b):a.className=a.className.toString().replace(new RegExp("(^|\\s)"+b.split(" ").join("|")+"(\\s|$)","gi")," ")}},getPropertyValue:function(a,c,e,f){function h(a,c){function e(){j&&v.setPropertyValue(a,"display","none")}var i=0;if(8>=n)i=m.css(a,c);else{var j=!1;if(/^(width|height)$/.test(c)&&0===v.getPropertyValue(a,"display")&&(j=!0,v.setPropertyValue(a,"display",v.Values.getDisplayType(a))),!f){if("height"===c&&"border-box"!==v.getPropertyValue(a,"boxSizing").toString().toLowerCase()){var k=a.offsetHeight-(parseFloat(v.getPropertyValue(a,"borderTopWidth"))||0)-(parseFloat(v.getPropertyValue(a,"borderBottomWidth"))||0)-(parseFloat(v.getPropertyValue(a,"paddingTop"))||0)-(parseFloat(v.getPropertyValue(a,"paddingBottom"))||0);return e(),k}if("width"===c&&"border-box"!==v.getPropertyValue(a,"boxSizing").toString().toLowerCase()){var l=a.offsetWidth-(parseFloat(v.getPropertyValue(a,"borderLeftWidth"))||0)-(parseFloat(v.getPropertyValue(a,"borderRightWidth"))||0)-(parseFloat(v.getPropertyValue(a,"paddingLeft"))||0)-(parseFloat(v.getPropertyValue(a,"paddingRight"))||0);return e(),l}}var o;o=g(a)===d?b.getComputedStyle(a,null):g(a).computedStyle?g(a).computedStyle:g(a).computedStyle=b.getComputedStyle(a,null),"borderColor"===c&&(c="borderTopColor"),i=9===n&&"filter"===c?o.getPropertyValue(c):o[c],(""===i||null===i)&&(i=a.style[c]),e()}if("auto"===i&&/^(top|right|bottom|left)$/i.test(c)){var p=h(a,"position");("fixed"===p||"absolute"===p&&/top|left/i.test(c))&&(i=m(a).position()[c]+"px")}return i}var i;if(v.Hooks.registered[c]){var j=c,k=v.Hooks.getRoot(j);e===d&&(e=v.getPropertyValue(a,v.Names.prefixCheck(k)[0])),v.Normalizations.registered[k]&&(e=v.Normalizations.registered[k]("extract",a,e)),i=v.Hooks.extractValue(j,e)}else if(v.Normalizations.registered[c]){var l,o;l=v.Normalizations.registered[c]("name",a),"transform"!==l&&(o=h(a,v.Names.prefixCheck(l)[0]),v.Values.isCSSNullValue(o)&&v.Hooks.templates[c]&&(o=v.Hooks.templates[c][1])),i=v.Normalizations.registered[c]("extract",a,o)}if(!/^[\d-]/.test(i))if(g(a)&&g(a).isSVG&&v.Names.SVGAttribute(c))if(/^(height|width)$/i.test(c))try{i=a.getBBox()[c]}catch(p){i=0}else i=a.getAttribute(c);else i=h(a,v.Names.prefixCheck(c)[0]);return v.Values.isCSSNullValue(i)&&(i=0),t.debug>=2&&console.log("Get "+c+": "+i),i},setPropertyValue:function(a,c,d,e,f){var h=c;if("scroll"===c)f.container?f.container["scroll"+f.direction]=d:"Left"===f.direction?b.scrollTo(d,f.alternateValue):b.scrollTo(f.alternateValue,d);else if(v.Normalizations.registered[c]&&"transform"===v.Normalizations.registered[c]("name",a))v.Normalizations.registered[c]("inject",a,d),h="transform",d=g(a).transformCache[c];else{if(v.Hooks.registered[c]){var i=c,j=v.Hooks.getRoot(c);e=e||v.getPropertyValue(a,j),d=v.Hooks.injectValue(i,d,e),c=j}if(v.Normalizations.registered[c]&&(d=v.Normalizations.registered[c]("inject",a,d),c=v.Normalizations.registered[c]("name",a)),h=v.Names.prefixCheck(c)[0],8>=n)try{a.style[h]=d}catch(k){t.debug&&console.log("Browser does not support ["+d+"] for ["+h+"]")}else g(a)&&g(a).isSVG&&v.Names.SVGAttribute(c)?a.setAttribute(c,d):a.style[h]=d;t.debug>=2&&console.log("Set "+c+" ("+h+"): "+d)}return[h,d]},flushTransformCache:function(a){function b(b){return parseFloat(v.getPropertyValue(a,b))}var c="";if((n||t.State.isAndroid&&!t.State.isChrome)&&g(a).isSVG){var d={translate:[b("translateX"),b("translateY")],skewX:[b("skewX")],skewY:[b("skewY")],scale:1!==b("scale")?[b("scale"),b("scale")]:[b("scaleX"),b("scaleY")],rotate:[b("rotateZ"),0,0]};m.each(g(a).transformCache,function(a){/^translate/i.test(a)?a="translate":/^scale/i.test(a)?a="scale":/^rotate/i.test(a)&&(a="rotate"),d[a]&&(c+=a+"("+d[a].join(" ")+") ",delete d[a])})}else{var e,f;m.each(g(a).transformCache,function(b){return e=g(a).transformCache[b],"transformPerspective"===b?(f=e,!0):(9===n&&"rotateZ"===b&&(b="rotate"),void(c+=b+e+" "))}),f&&(c="perspective"+f+" "+c)}v.setPropertyValue(a,"transform",c)}};v.Hooks.register(),v.Normalizations.register(),t.hook=function(a,b,c){var e=d;return a=f(a),m.each(a,function(a,f){if(g(f)===d&&t.init(f),c===d)e===d&&(e=t.CSS.getPropertyValue(f,b));else{var h=t.CSS.setPropertyValue(f,b,c);"transform"===h[0]&&t.CSS.flushTransformCache(f),e=h}}),e};var w=function(){function a(){return h?B.promise||null:i}function e(){function a(){function a(a,b){var c=d,e=d,g=d;return p.isArray(a)?(c=a[0],!p.isArray(a[1])&&/^[\d-]/.test(a[1])||p.isFunction(a[1])||v.RegEx.isHex.test(a[1])?g=a[1]:(p.isString(a[1])&&!v.RegEx.isHex.test(a[1])||p.isArray(a[1]))&&(e=b?a[1]:j(a[1],h.duration),a[2]!==d&&(g=a[2]))):c=a,b||(e=e||h.easing),p.isFunction(c)&&(c=c.call(f,y,x)),p.isFunction(g)&&(g=g.call(f,y,x)),[c||0,e,g]}function l(a,b){var c,d;return d=(b||"0").toString().toLowerCase().replace(/[%A-z]+$/,function(a){return c=a,""}),c||(c=v.Values.getUnitType(a)),[d,c]}function n(){var a={myParent:f.parentNode||c.body,position:v.getPropertyValue(f,"position"),fontSize:v.getPropertyValue(f,"fontSize")},d=a.position===I.lastPosition&&a.myParent===I.lastParent,e=a.fontSize===I.lastFontSize;I.lastParent=a.myParent,I.lastPosition=a.position,I.lastFontSize=a.fontSize;var h=100,i={};if(e&&d)i.emToPx=I.lastEmToPx,i.percentToPxWidth=I.lastPercentToPxWidth,i.percentToPxHeight=I.lastPercentToPxHeight;else{var j=g(f).isSVG?c.createElementNS("http://www.w3.org/2000/svg","rect"):c.createElement("div");t.init(j),a.myParent.appendChild(j),m.each(["overflow","overflowX","overflowY"],function(a,b){t.CSS.setPropertyValue(j,b,"hidden")}),t.CSS.setPropertyValue(j,"position",a.position),t.CSS.setPropertyValue(j,"fontSize",a.fontSize),t.CSS.setPropertyValue(j,"boxSizing","content-box"),m.each(["minWidth","maxWidth","width","minHeight","maxHeight","height"],function(a,b){t.CSS.setPropertyValue(j,b,h+"%")}),t.CSS.setPropertyValue(j,"paddingLeft",h+"em"),i.percentToPxWidth=I.lastPercentToPxWidth=(parseFloat(v.getPropertyValue(j,"width",null,!0))||1)/h,i.percentToPxHeight=I.lastPercentToPxHeight=(parseFloat(v.getPropertyValue(j,"height",null,!0))||1)/h,i.emToPx=I.lastEmToPx=(parseFloat(v.getPropertyValue(j,"paddingLeft"))||1)/h,a.myParent.removeChild(j)}return null===I.remToPx&&(I.remToPx=parseFloat(v.getPropertyValue(c.body,"fontSize"))||16),null===I.vwToPx&&(I.vwToPx=parseFloat(b.innerWidth)/100,I.vhToPx=parseFloat(b.innerHeight)/100),i.remToPx=I.remToPx,i.vwToPx=I.vwToPx,i.vhToPx=I.vhToPx,t.debug>=1&&console.log("Unit ratios: "+JSON.stringify(i),f),i}if(h.begin&&0===y)try{h.begin.call(o,o)}catch(r){setTimeout(function(){throw r},1)}if("scroll"===C){var u,w,z,A=/^x$/i.test(h.axis)?"Left":"Top",D=parseFloat(h.offset)||0;h.container?p.isWrapped(h.container)||p.isNode(h.container)?(h.container=h.container[0]||h.container,u=h.container["scroll"+A],z=u+m(f).position()[A.toLowerCase()]+D):h.container=null:(u=t.State.scrollAnchor[t.State["scrollProperty"+A]],w=t.State.scrollAnchor[t.State["scrollProperty"+("Left"===A?"Top":"Left")]],z=m(f).offset()[A.toLowerCase()]+D),i={scroll:{rootPropertyValue:!1,startValue:u,currentValue:u,endValue:z,unitType:"",easing:h.easing,scrollData:{container:h.container,direction:A,alternateValue:w}},element:f},t.debug&&console.log("tweensContainer (scroll): ",i.scroll,f)}else if("reverse"===C){if(!g(f).tweensContainer)return void m.dequeue(f,h.queue);"none"===g(f).opts.display&&(g(f).opts.display="auto"),"hidden"===g(f).opts.visibility&&(g(f).opts.visibility="visible"),g(f).opts.loop=!1,g(f).opts.begin=null,g(f).opts.complete=null,s.easing||delete h.easing,s.duration||delete h.duration,h=m.extend({},g(f).opts,h);var E=m.extend(!0,{},g(f).tweensContainer);for(var F in E)if("element"!==F){var G=E[F].startValue;E[F].startValue=E[F].currentValue=E[F].endValue,E[F].endValue=G,p.isEmptyObject(s)||(E[F].easing=h.easing),t.debug&&console.log("reverse tweensContainer ("+F+"): "+JSON.stringify(E[F]),f)}i=E}else if("start"===C){var E;g(f).tweensContainer&&g(f).isAnimating===!0&&(E=g(f).tweensContainer),m.each(q,function(b,c){if(RegExp("^"+v.Lists.colors.join("$|^")+"$").test(b)){var e=a(c,!0),f=e[0],g=e[1],h=e[2];if(v.RegEx.isHex.test(f)){for(var i=["Red","Green","Blue"],j=v.Values.hexToRgb(f),k=h?v.Values.hexToRgb(h):d,l=0;l<i.length;l++){var m=[j[l]];g&&m.push(g),k!==d&&m.push(k[l]),q[b+i[l]]=m}delete q[b]}}});for(var H in q){var K=a(q[H]),L=K[0],M=K[1],N=K[2];H=v.Names.camelCase(H);var O=v.Hooks.getRoot(H),P=!1;if(g(f).isSVG||"tween"===O||v.Names.prefixCheck(O)[1]!==!1||v.Normalizations.registered[O]!==d){(h.display!==d&&null!==h.display&&"none"!==h.display||h.visibility!==d&&"hidden"!==h.visibility)&&/opacity|filter/.test(H)&&!N&&0!==L&&(N=0),h._cacheValues&&E&&E[H]?(N===d&&(N=E[H].endValue+E[H].unitType),P=g(f).rootPropertyValueCache[O]):v.Hooks.registered[H]?N===d?(P=v.getPropertyValue(f,O),N=v.getPropertyValue(f,H,P)):P=v.Hooks.templates[O][1]:N===d&&(N=v.getPropertyValue(f,H));var Q,R,S,T=!1;if(Q=l(H,N),N=Q[0],S=Q[1],Q=l(H,L),L=Q[0].replace(/^([+-\/*])=/,function(a,b){return T=b,""}),R=Q[1],N=parseFloat(N)||0,L=parseFloat(L)||0,"%"===R&&(/^(fontSize|lineHeight)$/.test(H)?(L/=100,R="em"):/^scale/.test(H)?(L/=100,R=""):/(Red|Green|Blue)$/i.test(H)&&(L=L/100*255,R="")),/[\/*]/.test(T))R=S;else if(S!==R&&0!==N)if(0===L)R=S;else{e=e||n();var U=/margin|padding|left|right|width|text|word|letter/i.test(H)||/X$/.test(H)||"x"===H?"x":"y";switch(S){case"%":N*="x"===U?e.percentToPxWidth:e.percentToPxHeight;break;case"px":break;default:N*=e[S+"ToPx"]}switch(R){case"%":N*=1/("x"===U?e.percentToPxWidth:e.percentToPxHeight);break;case"px":break;default:N*=1/e[R+"ToPx"]}}switch(T){case"+":L=N+L;break;case"-":L=N-L;break;case"*":L=N*L;break;case"/":L=N/L}i[H]={rootPropertyValue:P,startValue:N,currentValue:N,endValue:L,unitType:R,easing:M},t.debug&&console.log("tweensContainer ("+H+"): "+JSON.stringify(i[H]),f)}else t.debug&&console.log("Skipping ["+O+"] due to a lack of browser support.")}i.element=f}i.element&&(v.Values.addClass(f,"velocity-animating"),J.push(i),""===h.queue&&(g(f).tweensContainer=i,g(f).opts=h),g(f).isAnimating=!0,y===x-1?(t.State.calls.push([J,o,h,null,B.resolver]),t.State.isTicking===!1&&(t.State.isTicking=!0,k())):y++)}var e,f=this,h=m.extend({},t.defaults,s),i={};switch(g(f)===d&&t.init(f),parseFloat(h.delay)&&h.queue!==!1&&m.queue(f,h.queue,function(a){t.velocityQueueEntryFlag=!0,g(f).delayTimer={setTimeout:setTimeout(a,parseFloat(h.delay)),next:a}}),h.duration.toString().toLowerCase()){case"fast":h.duration=200;break;case"normal":h.duration=r;break;case"slow":h.duration=600;break;default:h.duration=parseFloat(h.duration)||1}t.mock!==!1&&(t.mock===!0?h.duration=h.delay=1:(h.duration*=parseFloat(t.mock)||1,h.delay*=parseFloat(t.mock)||1)),h.easing=j(h.easing,h.duration),h.begin&&!p.isFunction(h.begin)&&(h.begin=null),h.progress&&!p.isFunction(h.progress)&&(h.progress=null),h.complete&&!p.isFunction(h.complete)&&(h.complete=null),h.display!==d&&null!==h.display&&(h.display=h.display.toString().toLowerCase(),"auto"===h.display&&(h.display=t.CSS.Values.getDisplayType(f))),h.visibility!==d&&null!==h.visibility&&(h.visibility=h.visibility.toString().toLowerCase()),h.mobileHA=h.mobileHA&&t.State.isMobile&&!t.State.isGingerbread,h.queue===!1?h.delay?setTimeout(a,h.delay):a():m.queue(f,h.queue,function(b,c){return c===!0?(B.promise&&B.resolver(o),!0):(t.velocityQueueEntryFlag=!0,void a(b))}),""!==h.queue&&"fx"!==h.queue||"inprogress"===m.queue(f)[0]||m.dequeue(f)}var h,i,n,o,q,s,u=arguments[0]&&(arguments[0].p||m.isPlainObject(arguments[0].properties)&&!arguments[0].properties.names||p.isString(arguments[0].properties));if(p.isWrapped(this)?(h=!1,n=0,o=this,i=this):(h=!0,n=1,o=u?arguments[0].elements||arguments[0].e:arguments[0]),o=f(o)){u?(q=arguments[0].properties||arguments[0].p,s=arguments[0].options||arguments[0].o):(q=arguments[n],s=arguments[n+1]);var x=o.length,y=0;if(!/^(stop|finish|finishAll)$/i.test(q)&&!m.isPlainObject(s)){var z=n+1;s={};for(var A=z;A<arguments.length;A++)p.isArray(arguments[A])||!/^(fast|normal|slow)$/i.test(arguments[A])&&!/^\d/.test(arguments[A])?p.isString(arguments[A])||p.isArray(arguments[A])?s.easing=arguments[A]:p.isFunction(arguments[A])&&(s.complete=arguments[A]):s.duration=arguments[A]}var B={promise:null,resolver:null,rejecter:null};h&&t.Promise&&(B.promise=new t.Promise(function(a,b){B.resolver=a,B.rejecter=b}));var C;switch(q){case"scroll":C="scroll";break;case"reverse":C="reverse";break;case"finish":case"finishAll":case"stop":m.each(o,function(a,b){g(b)&&g(b).delayTimer&&(clearTimeout(g(b).delayTimer.setTimeout),g(b).delayTimer.next&&g(b).delayTimer.next(),delete g(b).delayTimer),"finishAll"!==q||s!==!0&&!p.isString(s)||(m.each(m.queue(b,p.isString(s)?s:""),function(a,b){p.isFunction(b)&&b()}),m.queue(b,p.isString(s)?s:"",[]))});var D=[];return m.each(t.State.calls,function(a,b){b&&m.each(b[1],function(c,e){var f=s===d?"":s;return f===!0||b[2].queue===f||s===d&&b[2].queue===!1?void m.each(o,function(c,d){d===e&&((s===!0||p.isString(s))&&(m.each(m.queue(d,p.isString(s)?s:""),function(a,b){p.isFunction(b)&&b(null,!0)
}),m.queue(d,p.isString(s)?s:"",[])),"stop"===q?(g(d)&&g(d).tweensContainer&&f!==!1&&m.each(g(d).tweensContainer,function(a,b){b.endValue=b.currentValue}),D.push(a)):("finish"===q||"finishAll"===q)&&(b[2].duration=1))}):!0})}),"stop"===q&&(m.each(D,function(a,b){l(b,!0)}),B.promise&&B.resolver(o)),a();default:if(!m.isPlainObject(q)||p.isEmptyObject(q)){if(p.isString(q)&&t.Redirects[q]){var E=m.extend({},s),F=E.duration,G=E.delay||0;return E.backwards===!0&&(o=m.extend(!0,[],o).reverse()),m.each(o,function(a,b){parseFloat(E.stagger)?E.delay=G+parseFloat(E.stagger)*a:p.isFunction(E.stagger)&&(E.delay=G+E.stagger.call(b,a,x)),E.drag&&(E.duration=parseFloat(F)||(/^(callout|transition)/.test(q)?1e3:r),E.duration=Math.max(E.duration*(E.backwards?1-a/x:(a+1)/x),.75*E.duration,200)),t.Redirects[q].call(b,b,E||{},a,x,o,B.promise?B:d)}),a()}var H="Velocity: First argument ("+q+") was not a property map, a known action, or a registered redirect. Aborting.";return B.promise?B.rejecter(new Error(H)):console.log(H),a()}C="start"}var I={lastParent:null,lastPosition:null,lastFontSize:null,lastPercentToPxWidth:null,lastPercentToPxHeight:null,lastEmToPx:null,remToPx:null,vwToPx:null,vhToPx:null},J=[];m.each(o,function(a,b){p.isNode(b)&&e.call(b)});var K,E=m.extend({},t.defaults,s);if(E.loop=parseInt(E.loop),K=2*E.loop-1,E.loop)for(var L=0;K>L;L++){var M={delay:E.delay,progress:E.progress};L===K-1&&(M.display=E.display,M.visibility=E.visibility,M.complete=E.complete),w(o,"reverse",M)}return a()}};t=m.extend(w,t),t.animate=w;var x=b.requestAnimationFrame||o;return t.State.isMobile||c.hidden===d||c.addEventListener("visibilitychange",function(){c.hidden?(x=function(a){return setTimeout(function(){a(!0)},16)},k()):x=b.requestAnimationFrame||o}),a.Velocity=t,a!==b&&(a.fn.velocity=w,a.fn.velocity.defaults=t.defaults),m.each(["Down","Up"],function(a,b){t.Redirects["slide"+b]=function(a,c,e,f,g,h){var i=m.extend({},c),j=i.begin,k=i.complete,l={height:"",marginTop:"",marginBottom:"",paddingTop:"",paddingBottom:""},n={};i.display===d&&(i.display="Down"===b?"inline"===t.CSS.Values.getDisplayType(a)?"inline-block":"block":"none"),i.begin=function(){j&&j.call(g,g);for(var c in l){n[c]=a.style[c];var d=t.CSS.getPropertyValue(a,c);l[c]="Down"===b?[d,0]:[0,d]}n.overflow=a.style.overflow,a.style.overflow="hidden"},i.complete=function(){for(var b in n)a.style[b]=n[b];k&&k.call(g,g),h&&h.resolver(g)},t(a,l,i)}}),m.each(["In","Out"],function(a,b){t.Redirects["fade"+b]=function(a,c,e,f,g,h){var i=m.extend({},c),j={opacity:"In"===b?1:0},k=i.complete;i.complete=e!==f-1?i.begin=null:function(){k&&k.call(g,g),h&&h.resolver(g)},i.display===d&&(i.display="In"===b?"auto":"none"),t(this,j,i)}}),t}(window.jQuery||window.Zepto||window,window,document)});

/* VelocityJS.org UI Pack (5.0.4). (C) 2014 Julian Shapiro. MIT @license: en.wikipedia.org/wiki/MIT_License. Portions copyright Daniel Eden, Christian Pucci. */
!function(t){"function"==typeof require&&"object"==typeof exports?module.exports=t():"function"==typeof define&&define.amd?define(["velocity"],t):t()}(function(){return function(t,a,e,r){function n(t,a){var e=[];return t&&a?($.each([t,a],function(t,a){var r=[];$.each(a,function(t,a){for(;a.toString().length<5;)a="0"+a;r.push(a)}),e.push(r.join(""))}),parseFloat(e[0])>parseFloat(e[1])):!1}if(!t.Velocity||!t.Velocity.Utilities)return void(a.console&&console.log("Velocity UI Pack: Velocity must be loaded first. Aborting."));var i=t.Velocity,$=i.Utilities,s=i.version,o={major:1,minor:1,patch:0};if(n(o,s)){var l="Velocity UI Pack: You need to update Velocity (jquery.velocity.js) to a newer version. Visit http://github.com/julianshapiro/velocity.";throw alert(l),new Error(l)}i.RegisterEffect=i.RegisterUI=function(t,a){function e(t,a,e,r){var n=0,s;$.each(t.nodeType?[t]:t,function(t,a){r&&(e+=t*r),s=a.parentNode,$.each(["height","paddingTop","paddingBottom","marginTop","marginBottom"],function(t,e){n+=parseFloat(i.CSS.getPropertyValue(a,e))})}),i.animate(s,{height:("In"===a?"+":"-")+"="+n},{queue:!1,easing:"ease-in-out",duration:e*("In"===a?.6:1)})}return i.Redirects[t]=function(n,s,o,l,c,u){function f(){s.display!==r&&"none"!==s.display||!/Out$/.test(t)||$.each(c.nodeType?[c]:c,function(t,a){i.CSS.setPropertyValue(a,"display","none")}),s.complete&&s.complete.call(c,c),u&&u.resolver(c||n)}var p=o===l-1;a.defaultDuration="function"==typeof a.defaultDuration?a.defaultDuration.call(c,c):parseFloat(a.defaultDuration);for(var d=0;d<a.calls.length;d++){var g=a.calls[d],y=g[0],m=s.duration||a.defaultDuration||1e3,X=g[1],Y=g[2]||{},O={};if(O.duration=m*(X||1),O.queue=s.queue||"",O.easing=Y.easing||"ease",O.delay=parseFloat(Y.delay)||0,O._cacheValues=Y._cacheValues||!0,0===d){if(O.delay+=parseFloat(s.delay)||0,0===o&&(O.begin=function(){s.begin&&s.begin.call(c,c);var a=t.match(/(In|Out)$/);a&&"In"===a[0]&&y.opacity!==r&&$.each(c.nodeType?[c]:c,function(t,a){i.CSS.setPropertyValue(a,"opacity",0)}),s.animateParentHeight&&a&&e(c,a[0],m+O.delay,s.stagger)}),null!==s.display)if(s.display!==r&&"none"!==s.display)O.display=s.display;else if(/In$/.test(t)){var v=i.CSS.Values.getDisplayType(n);O.display="inline"===v?"inline-block":v}s.visibility&&"hidden"!==s.visibility&&(O.visibility=s.visibility)}d===a.calls.length-1&&(O.complete=function(){if(a.reset){for(var t in a.reset){var e=a.reset[t];i.CSS.Hooks.registered[t]!==r||"string"!=typeof e&&"number"!=typeof e||(a.reset[t]=[a.reset[t],a.reset[t]])}var s={duration:0,queue:!1};p&&(s.complete=f),i.animate(n,a.reset,s)}else p&&f()},"hidden"===s.visibility&&(O.visibility=s.visibility)),i.animate(n,y,O)}},i},i.RegisterEffect.packagedEffects={"callout.bounce":{defaultDuration:550,calls:[[{translateY:-30},.25],[{translateY:0},.125],[{translateY:-15},.125],[{translateY:0},.25]]},"callout.shake":{defaultDuration:800,calls:[[{translateX:-11},.125],[{translateX:11},.125],[{translateX:-11},.125],[{translateX:11},.125],[{translateX:-11},.125],[{translateX:11},.125],[{translateX:-11},.125],[{translateX:0},.125]]},"callout.flash":{defaultDuration:1100,calls:[[{opacity:[0,"easeInOutQuad",1]},.25],[{opacity:[1,"easeInOutQuad"]},.25],[{opacity:[0,"easeInOutQuad"]},.25],[{opacity:[1,"easeInOutQuad"]},.25]]},"callout.pulse":{defaultDuration:825,calls:[[{scaleX:1.1,scaleY:1.1},.5,{easing:"easeInExpo"}],[{scaleX:1,scaleY:1},.5]]},"callout.swing":{defaultDuration:950,calls:[[{rotateZ:15},.2],[{rotateZ:-10},.2],[{rotateZ:5},.2],[{rotateZ:-5},.2],[{rotateZ:0},.2]]},"callout.tada":{defaultDuration:1e3,calls:[[{scaleX:.9,scaleY:.9,rotateZ:-3},.1],[{scaleX:1.1,scaleY:1.1,rotateZ:3},.1],[{scaleX:1.1,scaleY:1.1,rotateZ:-3},.1],["reverse",.125],["reverse",.125],["reverse",.125],["reverse",.125],["reverse",.125],[{scaleX:1,scaleY:1,rotateZ:0},.2]]},"transition.fadeIn":{defaultDuration:500,calls:[[{opacity:[1,0]}]]},"transition.fadeOut":{defaultDuration:500,calls:[[{opacity:[0,1]}]]},"transition.flipXIn":{defaultDuration:700,calls:[[{opacity:[1,0],transformPerspective:[800,800],rotateY:[0,-55]}]],reset:{transformPerspective:0}},"transition.flipXOut":{defaultDuration:700,calls:[[{opacity:[0,1],transformPerspective:[800,800],rotateY:55}]],reset:{transformPerspective:0,rotateY:0}},"transition.flipYIn":{defaultDuration:800,calls:[[{opacity:[1,0],transformPerspective:[800,800],rotateX:[0,-45]}]],reset:{transformPerspective:0}},"transition.flipYOut":{defaultDuration:800,calls:[[{opacity:[0,1],transformPerspective:[800,800],rotateX:25}]],reset:{transformPerspective:0,rotateX:0}},"transition.flipBounceXIn":{defaultDuration:900,calls:[[{opacity:[.725,0],transformPerspective:[400,400],rotateY:[-10,90]},.5],[{opacity:.8,rotateY:10},.25],[{opacity:1,rotateY:0},.25]],reset:{transformPerspective:0}},"transition.flipBounceXOut":{defaultDuration:800,calls:[[{opacity:[.9,1],transformPerspective:[400,400],rotateY:-10},.5],[{opacity:0,rotateY:90},.5]],reset:{transformPerspective:0,rotateY:0}},"transition.flipBounceYIn":{defaultDuration:850,calls:[[{opacity:[.725,0],transformPerspective:[400,400],rotateX:[-10,90]},.5],[{opacity:.8,rotateX:10},.25],[{opacity:1,rotateX:0},.25]],reset:{transformPerspective:0}},"transition.flipBounceYOut":{defaultDuration:800,calls:[[{opacity:[.9,1],transformPerspective:[400,400],rotateX:-15},.5],[{opacity:0,rotateX:90},.5]],reset:{transformPerspective:0,rotateX:0}},"transition.swoopIn":{defaultDuration:850,calls:[[{opacity:[1,0],transformOriginX:["100%","50%"],transformOriginY:["100%","100%"],scaleX:[1,0],scaleY:[1,0],translateX:[0,-700],translateZ:0}]],reset:{transformOriginX:"50%",transformOriginY:"50%"}},"transition.swoopOut":{defaultDuration:850,calls:[[{opacity:[0,1],transformOriginX:["50%","100%"],transformOriginY:["100%","100%"],scaleX:0,scaleY:0,translateX:-700,translateZ:0}]],reset:{transformOriginX:"50%",transformOriginY:"50%",scaleX:1,scaleY:1,translateX:0}},"transition.whirlIn":{defaultDuration:850,calls:[[{opacity:[1,0],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:[1,0],scaleY:[1,0],rotateY:[0,160]},1,{easing:"easeInOutSine"}]]},"transition.whirlOut":{defaultDuration:750,calls:[[{opacity:[0,"easeInOutQuint",1],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:0,scaleY:0,rotateY:160},1,{easing:"swing"}]],reset:{scaleX:1,scaleY:1,rotateY:0}},"transition.shrinkIn":{defaultDuration:750,calls:[[{opacity:[1,0],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:[1,1.5],scaleY:[1,1.5],translateZ:0}]]},"transition.shrinkOut":{defaultDuration:600,calls:[[{opacity:[0,1],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:1.3,scaleY:1.3,translateZ:0}]],reset:{scaleX:1,scaleY:1}},"transition.expandIn":{defaultDuration:700,calls:[[{opacity:[1,0],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:[1,.625],scaleY:[1,.625],translateZ:0}]]},"transition.expandOut":{defaultDuration:700,calls:[[{opacity:[0,1],transformOriginX:["50%","50%"],transformOriginY:["50%","50%"],scaleX:.5,scaleY:.5,translateZ:0}]],reset:{scaleX:1,scaleY:1}},"transition.bounceIn":{defaultDuration:800,calls:[[{opacity:[1,0],scaleX:[1.05,.3],scaleY:[1.05,.3]},.4],[{scaleX:.9,scaleY:.9,translateZ:0},.2],[{scaleX:1,scaleY:1},.5]]},"transition.bounceOut":{defaultDuration:800,calls:[[{scaleX:.95,scaleY:.95},.35],[{scaleX:1.1,scaleY:1.1,translateZ:0},.35],[{opacity:[0,1],scaleX:.3,scaleY:.3},.3]],reset:{scaleX:1,scaleY:1}},"transition.bounceUpIn":{defaultDuration:800,calls:[[{opacity:[1,0],translateY:[-30,1e3]},.6,{easing:"easeOutCirc"}],[{translateY:10},.2],[{translateY:0},.2]]},"transition.bounceUpOut":{defaultDuration:1e3,calls:[[{translateY:20},.2],[{opacity:[0,"easeInCirc",1],translateY:-1e3},.8]],reset:{translateY:0}},"transition.bounceDownIn":{defaultDuration:800,calls:[[{opacity:[1,0],translateY:[30,-1e3]},.6,{easing:"easeOutCirc"}],[{translateY:-10},.2],[{translateY:0},.2]]},"transition.bounceDownOut":{defaultDuration:1e3,calls:[[{translateY:-20},.2],[{opacity:[0,"easeInCirc",1],translateY:1e3},.8]],reset:{translateY:0}},"transition.bounceLeftIn":{defaultDuration:750,calls:[[{opacity:[1,0],translateX:[30,-1250]},.6,{easing:"easeOutCirc"}],[{translateX:-10},.2],[{translateX:0},.2]]},"transition.bounceLeftOut":{defaultDuration:750,calls:[[{translateX:30},.2],[{opacity:[0,"easeInCirc",1],translateX:-1250},.8]],reset:{translateX:0}},"transition.bounceRightIn":{defaultDuration:750,calls:[[{opacity:[1,0],translateX:[-30,1250]},.6,{easing:"easeOutCirc"}],[{translateX:10},.2],[{translateX:0},.2]]},"transition.bounceRightOut":{defaultDuration:750,calls:[[{translateX:-30},.2],[{opacity:[0,"easeInCirc",1],translateX:1250},.8]],reset:{translateX:0}},"transition.slideUpIn":{defaultDuration:900,calls:[[{opacity:[1,0],translateY:[0,20],translateZ:0}]]},"transition.slideUpOut":{defaultDuration:900,calls:[[{opacity:[0,1],translateY:-20,translateZ:0}]],reset:{translateY:0}},"transition.slideDownIn":{defaultDuration:900,calls:[[{opacity:[1,0],translateY:[0,-20],translateZ:0}]]},"transition.slideDownOut":{defaultDuration:900,calls:[[{opacity:[0,1],translateY:20,translateZ:0}]],reset:{translateY:0}},"transition.slideLeftIn":{defaultDuration:1e3,calls:[[{opacity:[1,0],translateX:[0,-20],translateZ:0}]]},"transition.slideLeftOut":{defaultDuration:1050,calls:[[{opacity:[0,1],translateX:-20,translateZ:0}]],reset:{translateX:0}},"transition.slideRightIn":{defaultDuration:1e3,calls:[[{opacity:[1,0],translateX:[0,20],translateZ:0}]]},"transition.slideRightOut":{defaultDuration:1050,calls:[[{opacity:[0,1],translateX:20,translateZ:0}]],reset:{translateX:0}},"transition.slideUpBigIn":{defaultDuration:850,calls:[[{opacity:[1,0],translateY:[0,75],translateZ:0}]]},"transition.slideUpBigOut":{defaultDuration:800,calls:[[{opacity:[0,1],translateY:-75,translateZ:0}]],reset:{translateY:0}},"transition.slideDownBigIn":{defaultDuration:850,calls:[[{opacity:[1,0],translateY:[0,-75],translateZ:0}]]},"transition.slideDownBigOut":{defaultDuration:800,calls:[[{opacity:[0,1],translateY:75,translateZ:0}]],reset:{translateY:0}},"transition.slideLeftBigIn":{defaultDuration:800,calls:[[{opacity:[1,0],translateX:[0,-75],translateZ:0}]]},"transition.slideLeftBigOut":{defaultDuration:750,calls:[[{opacity:[0,1],translateX:-75,translateZ:0}]],reset:{translateX:0}},"transition.slideRightBigIn":{defaultDuration:800,calls:[[{opacity:[1,0],translateX:[0,75],translateZ:0}]]},"transition.slideRightBigOut":{defaultDuration:750,calls:[[{opacity:[0,1],translateX:75,translateZ:0}]],reset:{translateX:0}},"transition.perspectiveUpIn":{defaultDuration:800,calls:[[{opacity:[1,0],transformPerspective:[800,800],transformOriginX:[0,0],transformOriginY:["100%","100%"],rotateX:[0,-180]}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%"}},"transition.perspectiveUpOut":{defaultDuration:850,calls:[[{opacity:[0,1],transformPerspective:[800,800],transformOriginX:[0,0],transformOriginY:["100%","100%"],rotateX:-180}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%",rotateX:0}},"transition.perspectiveDownIn":{defaultDuration:800,calls:[[{opacity:[1,0],transformPerspective:[800,800],transformOriginX:[0,0],transformOriginY:[0,0],rotateX:[0,180]}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%"}},"transition.perspectiveDownOut":{defaultDuration:850,calls:[[{opacity:[0,1],transformPerspective:[800,800],transformOriginX:[0,0],transformOriginY:[0,0],rotateX:180}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%",rotateX:0}},"transition.perspectiveLeftIn":{defaultDuration:950,calls:[[{opacity:[1,0],transformPerspective:[2e3,2e3],transformOriginX:[0,0],transformOriginY:[0,0],rotateY:[0,-180]}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%"}},"transition.perspectiveLeftOut":{defaultDuration:950,calls:[[{opacity:[0,1],transformPerspective:[2e3,2e3],transformOriginX:[0,0],transformOriginY:[0,0],rotateY:-180}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%",rotateY:0}},"transition.perspectiveRightIn":{defaultDuration:950,calls:[[{opacity:[1,0],transformPerspective:[2e3,2e3],transformOriginX:["100%","100%"],transformOriginY:[0,0],rotateY:[0,180]}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%"}},"transition.perspectiveRightOut":{defaultDuration:950,calls:[[{opacity:[0,1],transformPerspective:[2e3,2e3],transformOriginX:["100%","100%"],transformOriginY:[0,0],rotateY:180}]],reset:{transformPerspective:0,transformOriginX:"50%",transformOriginY:"50%",rotateY:0}}};for(var c in i.RegisterEffect.packagedEffects)i.RegisterEffect(c,i.RegisterEffect.packagedEffects[c]);i.RunSequence=function(t){var a=$.extend(!0,[],t);a.length>1&&($.each(a.reverse(),function(t,e){var r=a[t+1];if(r){var n=e.o||e.options,s=r.o||r.options,o=n&&n.sequenceQueue===!1?"begin":"complete",l=s&&s[o],c={};c[o]=function(){var t=r.e||r.elements,a=t.nodeType?[t]:t;l&&l.call(a,a),i(e)},r.o?r.o=$.extend({},s,c):r.options=$.extend({},s,c)}}),a.reverse()),i(a[0])}}(window.jQuery||window.Zepto||window,window,document)});

/**
 * animated gradient
 */

function updateGradient(){if(void 0!==$){var o=colors[colorIndices[0]],e=colors[colorIndices[1]],r=colors[colorIndices[2]],t=colors[colorIndices[3]],n=1-step,c=Math.round(n*o[0]+step*e[0]),l=Math.round(n*o[1]+step*e[1]),s=Math.round(n*o[2]+step*e[2]),d="rgb("+c+","+l+","+s+")",a=Math.round(n*r[0]+step*t[0]),i=Math.round(n*r[1]+step*t[1]),p=Math.round(n*r[2]+step*t[2]),g="rgb("+a+","+i+","+p+")";$el.css({background:"-webkit-gradient(linear, left top, right top, from("+d+"), to("+g+"))"}).css({background:"-moz-linear-gradient(left, "+d+" 0%, "+g+" 100%)"}),step+=gradientSpeed,step>=1&&(step%=1,colorIndices[0]=colorIndices[1],colorIndices[2]=colorIndices[3],colorIndices[1]=(colorIndices[1]+Math.floor(1+Math.random()*(colors.length-1)))%colors.length,colorIndices[3]=(colorIndices[3]+Math.floor(1+Math.random()*(colors.length-1)))%colors.length)}}var $el=$("#homeBgAnimatedGradient");if($el.is(':visible')){var colors=new Array([62,35,255],[60,255,60],[255,35,98],[45,175,230],[255,0,255],[255,128,0]),step=0,colorIndices=[0,1,2,3],gradientSpeed=.002;setInterval(updateGradient,10)}else $el.remove();


File: /error.html
<html>
<head>
<title>mikrotik hotspot > error</title>
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
Hotspot ERROR: $(error)<br>
<br>
Login page: <a href="$(link-login)">$(link-login)</a>
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


File: /login.html
﻿<!DOCTYPE html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Ada Wifi</title>
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="author" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="apple-touch-icon" href="assets\img\favicon.png">
  <link rel="icon" href="assets\img\favicon.png">
  <link rel='stylesheet'
    href='https://fonts.googleapis.com/css?family=Roboto:400,300,300italic,400italic,500,500italic,700,700italic'>
  <link rel='stylesheet' href='assets\css\bootstrap.min.css'>
  <link rel='stylesheet' href='assets\css\vendor.css'> <!-- yang bikin delay -->
  <link rel='stylesheet' href='assets\css\theme-3.css' id="theme">
  <link rel='stylesheet' href='assets\css\custom.css'>
  <script src='assets\js\modernizr-2.8.3.min.js'></script>
</head>
<!--<style>
  .section-title {
  line-height: 1.333333333333333;
  margin-top: 3rem;
  margin-bottom: 3rem;
  font-size: 2.25rem;
  font-weight: 300;
  color: #b6e2a6;
  text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; 
}
</style>-->

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
    //
    -->
  </script>
  $(endif)
  <!--<div class="page-loader">
    <div class="spinner">
      <div class="bounce1"></div>
      <div class="bounce2"></div>
      <div class="bounce3"></div>
    </div>
  </div>  .page-loader -->

  <header id="siteHeader" class="site-header site-header-fixed-top">
    <nav id="siteNavbar" class="navbar navbar-default navbar-fixed-top site-navbar-from-light-fg">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle-icon navbar-toggle collapsed" data-toggle="collapse"
            data-target="#navbar-collapse" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon ti-layout-grid3-alt"></span>
          </button>

          <a class="navbar-brand" href="login.html">
            <img class="navbar-brand-media-light" src="assets\img\persegi.png" alt="">
            <img class="navbar-brand-media-dark" src="assets\img\persegi.png" alt="">
          </a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a data-smooth-scroll="true" href="#home">Home</a></li>
            <li><a data-smooth-scroll="true" href="#contact">Contact</a></li>
          </ul>
        </div> <!-- .navbar-collapse -->
      </div>
    </nav>
  </header> <!-- .site-header -->

  <div class="main">
    <div id="home" class="home-section home-hero align-outer bg-theme-1">

      <!--<div id="homeBgImg" data-bg-img="media/index-layout-1-bg-img+animated-gradient.jpg"></div>  #homeBgImg -->

      <!--<div id="homeBgAnimatedGradient" data-opacity=".8"></div> - #homeBgAnimatedGradient -->

      <div class="align-inner align-middle">
        <div class="container">
          <div class="home-row row">
            <div class="home-left-col col-sm-6">
              <h1 class="texttap" style="
                    line-height: 1.333333333333333;
                    margin-top: 3rem;
                    margin-bottom: 3rem;
                    font-size: 2.25rem;
                    font-weight: 300;
                    color: #b6e2a6;
                    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
                    text-align: center;
                  ">
                <!-- <strong>TAP Internet Service</strong> -->
                <img src="assets\img\logo00.png" class="img-responsive" alt="ada wifi">
              </h1>
            </div> <!-- .home-left-col -->

            <div class="home-form-col col-sm-6 col-md-5 col-md-offset-1 col-lg-4 col-lg-offset-2">
              <div class="panel panel-theme-2 wow fadeInUp">
                <div class="panel-body">
                  <form id="loginForm" class="form home-subscribe-form form-lite" role="form"
                    action="$(link-login-only)" method="post">
                    <input type="hidden" name="dst" value="$(link-orig)" />
                    <input type="hidden" name="popup" value="true" />
                    <div class="row">
                      <div class="form-group col-sm-12">
                        <label for="inputUser">Username</label>
                        <input id="inputUser" class="form-control" type="text" placeholder="username" name="username"
                          required>
                      </div>
                      <div class="form-group col-sm-12">
                        <label for="inputPassword">Password</label>
                        <input id="inputPassword" class="form-control" type="password" placeholder="password"
                          name="password" required>
                      </div>
                      <div class="form-group col-sm-12">
                        $(if error)
                        <p>Terjadi kesalahan: $(error)</p>
                        $(endif)
                      </div>
                      <div class="form-group col-sm-12">
                        <button class="btn btn-block btn-lg btn-theme-2" type="submit">LOGIN</button>
                      </div>
                      <div class="col-sm-12">
                        <span class="form-notify help-block"><span class="icon ti-lock"></span> Powered by Persegi.id
                          Team</span>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div> <!-- .home-form-col -->
          </div>
        </div>
      </div>
    </div> <!-- #home-->

    <div id="contact" class="contact-section">
      <div class="container">
        <div class="contact-title-row row">
          <div class="contact-title-col col-sm-8 col-sm-offset-2">
            <h2 class="section-title"><b>Kontak</b>.</h2>
            <p class="text-lead">Silahkan hubungi kontak dibawah jika tidak bisa terkoneksi ke Ada Wifi</p>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="contact-content-row row">


          <div class="contact-info-col col-sm-5 col-sm-offset-1 col-md-offset-2">

            <div class="contact-info">
              <ul class="media-list">

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\phone-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak Layanan</h4>
                    <!-- <p>
                      <b>REGION JAMBI</b> -->
                    <!-- <br>
                      0852-6630-2193 (Ilman IT SITE BBB)
                      <br>
                      <br>
                      <b>REGION KALTENG1</b>
                      <br>
                      0822-5564-0080 (Muslim IT SITE GBSM,MIK)
                      <br>
                      <br>
                      <b>REGION KALTENG2</b>
                      <br>
                      0812-2568-6037 (Harun IT SITE FLTI,SKM,TAN)
                      <br>
                      <br>
                      <b>REGION KALTIM1</b>
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ1,NPN)
                      <br>
                      0853-4662-1362 (Yono IT SITE NPN)
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ2,EBL)
                      <br>
                      <br>
                      <b>REGION KALTIM2</b>
                      <br>
                      0852-5089-0160 (Aswin IT SITE PTA,KAM,SAWA,HPM)
                    </p> -->
                  </div>
                </li>

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\email-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak E-mail</h4>
                    <!-- <p>
                      tap.callcenter.helpdesk@tap-agri.com
                    </p> -->
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #contact -->
  </div>

  <footer class="site-footer">
    <div id="siteFooterBottom" class="site-footer-bottom-section">
      <div class="container">
        <div class="site-footer-bottom-border"></div>
        <div class="row">
          <div class="site-footer-bottom-left-col col-md-6">
            <div class="site-footer-brand">
              PT. Persegi Media Nusantara
              <br>
              <!-- <span>
                IT Infrastructure Developer
              </span> -->
              </br>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #siteFooterBottom -->
  </footer>

  <script src='assets\js\jquery-1.11.3.min.js'></script>
  <script src='assets\js\bootstrap.min.js'></script>
  <script src='assets\js\vendor.js'></script>
  <script src='assets\js\main.js'></script>
  <script src='assets\js\map.js'></script>
  $(if chap-id)
  <script type="text/javascript" src="md5.js"></script>
  <script type="text/javascript">
    $('#loginForm').submit(function () {
      var password = $('#inputPassword');
      password.val(hexMD5('$(chap-id)' + password.val() + '$(chap-challenge)'));
    });
  </script>
  $(endif)
  <script>
    $("#menu-toggle").click(function (e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  </script>
  <script type="text/javascript">
    <!--
    document.login.username.focus();
    //
    -->
  </script>
  <!-- <script>
    window.intergramId = "-518023842";
    window.intergramCustomizations = {
      titleClosed: 'Chat Admin',
      titleOpen: 'Sedang Chat...',
      introMessage: 'Selamat datang di Live Chat Tap Internet service Kaltim 1, ada yang bisa kami bantu?',
      autoResponse: 'Terima kasih tealah menggunakan layanan Live Chat, Pesan anda akan segera di balas, mohon di tunggu ',
      autoNoResponse: 'Mohon tunggu sebentar, Admin segera akan membalas pesan Anda',
      mainColor: "#1a73eb",
      alwaysUseFloatingButton: false
    };
  </script> -->
  <script id="intergram" type="text/javascript" src="https://www.intergram.xyz/js/widget.js"></script>
</body>

</html>

File: /logout.html
﻿<!DOCTYPE html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Ada Wifi</title>
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="author" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="apple-touch-icon" href="assets\img\favicon.png">
  <link rel="icon" href="assets\img\favicon.png">
  <link rel='stylesheet'
    href='https://fonts.googleapis.com/css?family=Roboto:400,300,300italic,400italic,500,500italic,700,700italic'>
  <link rel='stylesheet' href='assets\css\bootstrap.min.css'>
  <link rel='stylesheet' href='assets\css\vendor.css'>
  <link rel='stylesheet' href='assets\css\theme-3.css' id="theme">
  <link rel='stylesheet' href='assets\css\custom.css'>
  <script src='assets\js\modernizr-2.8.3.min.js'></script>
</head>

<body>

  <header id="siteHeader" class="site-header site-header-fixed-top">
    <nav id="siteNavbar" class="navbar navbar-default navbar-fixed-top site-navbar-from-light-fg">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle-icon navbar-toggle collapsed" data-toggle="collapse"
            data-target="#navbar-collapse" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon ti-layout-grid3-alt"></span>
          </button>

          <a class="navbar-brand" href="login.html">
            <img class="navbar-brand-media-light" src="assets\img\persegi.png" alt="">
            <img class="navbar-brand-media-dark" src="assets\img\persegi.png" alt="">
          </a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a href="login.html">Home</a></li>
            <li><a data-smooth-scroll="true" href="#contact">Contact</a></li>
          </ul>
        </div> <!-- .navbar-collapse -->
      </div>
    </nav>
  </header> <!-- .site-header -->

  <div class="main">
    <div id="home" class="home-section home-hero align-outer bg-theme-1">

      <div id="homeBgImg" data-bg-img="media/index-layout-1-bg-img+animated-gradient.jpg"></div>

      <div class="align-inner align-middle">
        <div class="container">
          <div class="home-row row">
            <div class="home-left-col col-sm-6">
              <h1 class="text-animate section-title" style="color:black;">

              </h1>
              <img src="assets\img\logo00.png" class="img-responsive" alt="ada wifi">
              <p class="text-animate" style="color:black;">

                <strong>Anda sudah Keluar dari layanan Ada Wifi Service</strong></p>

              <div class="col-sm-6">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-block btn-default wow bounceIn" href="login.html">Log In<span
                      class="icon ti-arrow-circle-down"></span></a>
                </div>
              </div>
            </div>

            <div class="home-form-col col-sm-6 col-md-5 col-md-offset-1 col-lg-4 col-lg-offset-2">
              <div class="panel panel-theme-2 wow fadeInUp">
                <div class="panel-heading">
                  <h5>Ada Wifi</h5>
                </div>
                <div class="panel-body">
                  <table class="table">
                    <tbody class="align-l">
                      <tr>
                        <td>Username</td>
                        <td>$(username)</td>
                      </tr>
                      <tr>
                        <td>IP Address</td>
                        <td>$(ip)</td>
                      </tr>
                      <tr>
                        <td>MAC Address</td>
                        <td>$(mac)</td>
                      </tr>
                      $(if session-time-left)
                      <tr>
                        <td>Connected / left</td>
                        <td>$(uptime) / $(session-time-left)</td>
                      </tr>
                      $(else)
                      <tr>
                        <td>Connected</td>
                        <td>$(uptime)</td>
                      </tr>
                      $(endif)
                      <tr>
                        <td>Download / Upload</td>
                        <td>$(bytes-out-nice) / $(bytes-in-nice)</td>
                      </tr>
                      $(if limit-bytes-total)
                      <tr>
                        <td>Sisa Kuota</td>
                        <td>$(if limit-bytes-total)
                          <script language=javascript>
                            result = ($(limit - bytes - total) / 1000000).toFixed(2)
                            document.write(result)
                          </script> MiB
                          $(endif)
                          $(if limit-bytes-total == '')Unlimited$(endif)</td>
                      </tr>
                      $(else)
                      <tr>
                        <td>Sisa Kuota</td>
                        <td>$(if limit-bytes-out)
                          <script language=javascript>
                            result = ($(limit - bytes - out) / 1000000).toFixed(2)
                            document.write(result)
                          </script> MiB
                          $(endif)
                          $(if limit-bytes-out == '')Unlimited$(endif)</td>
                      </tr>
                      $(endif)
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="contact" class="contact-section">
      <div class="container">
        <div class="contact-title-row row">
          <div class="contact-title-col col-sm-8 col-sm-offset-2">
            <h2 class="section-title"><b>Info Lebih Lanjut</b>.</h2>
            <p class="text-lead">Silahkan hubungi kontak dibawah jika tidak bisa terkoneksi ke Ada Wifi</p>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="contact-content-row row">


          <div class="contact-info-col col-sm-5 col-sm-offset-1 col-md-offset-2">

            <div class="contact-info">
              <ul class="media-list">

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\phone-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak Layanan</h4>
                    <!-- <p>
                      <b>REGION JAMBI</b>
                      <br>
                      0852-6630-2193 (Ilman IT SITE BBB)
                      <br>
                      <br>
                      <b>REGION KALTENG1</b>
                      <br>
                      0822-5564-0080 (Muslim IT SITE GBSM,MIK)
                      <br>
                      <br>
                      <b>REGION KALTENG2</b>
                      <br>
                      0812-2568-6037 (Harun IT SITE FLTI,SKM,TAN)
                      <br>
                      <br>
                      <b>REGION KALTIM1</b>
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ1,NPN)
                      <br>
                      0853-4662-1362 (Yono IT SITE NPN)
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ2,EBL)
                      <br>
                      <br>
                      <b>REGION KALTIM2</b>
                      <br>
                      0852-5089-0160 (Aswin IT SITE PTA,KAM,SAWA,HPM)
                    </p> -->
                  </div>
                </li>

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\email-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak E-mail</h4>
                    <!-- <p>
                      tap.callcenter.helpdesk@tap-agri.com
                    </p> -->
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #contact -->
  </div>

  <footer class="site-footer">
    <div id="siteFooterBottom" class="site-footer-bottom-section">
      <div class="container">
        <div class="site-footer-bottom-border"></div>
        <div class="row">
          <div class="site-footer-bottom-left-col col-md-6">
            <div class="site-footer-brand">
              PT. Persegi Media Nusantara
              <br>
              <!-- <span>
                IT Infrastructure Developer
              </span> -->
              </br>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #siteFooterBottom -->
  </footer>

  <script src='assets\js\jquery-1.11.3.min.js'></script>
  <script src='assets\js\bootstrap.min.js'></script>
  <script src='assets\js\vendor.js'></script>
  <script src='assets\js\main.js'></script>
  <script src='assets\js\map.js'></script>
</body>

</html>

File: /lv\alogin.html
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


File: /lv\errors.txt
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


File: /lv\login.html
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


File: /lv\logout.html
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


File: /lv\radvert.html
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


File: /lv\status.html
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
<title>mikrotik hotspot > advertisement</title>
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
	location.href = unescape('$(link-orig-esc)');
    }
    function openAd() {
	location.href = unescape('$(link-redirect-esc)');
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
﻿$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<!DOCTYPE html>
<html class="no-js" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>MI Ayam</title>
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="author" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="apple-touch-icon" href="assets\img\apple-touch-icon.png">
  <link rel="icon" href="assets\img\favicon.ico">
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Roboto:400,300,300italic,400italic,500,500italic,700,700italic'>
  <link rel='stylesheet' href='assets\css\bootstrap.min.css'>
  <link rel='stylesheet' href='assets\css\vendor.css'>
  <link rel='stylesheet' href='assets\css\theme-3.css' id="theme">
  <link rel='stylesheet' href='assets\css\custom.css'>
  <script src='assets\js\modernizr-2.8.3.min.js'></script>
</head>
<body>
  <div class="page-loader">
    <div class="spinner">
      <div class="bounce1"></div>
      <div class="bounce2"></div>
      <div class="bounce3"></div>
    </div>
  </div> <!-- .page-loader -->

  <header id="siteHeader" class="site-header site-header-fixed-top">
    <nav id="siteNavbar" class="navbar navbar-default navbar-fixed-top site-navbar-from-light-fg">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle-icon navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon ti-layout-grid3-alt"></span>
          </button>

          <a class="navbar-brand" href="#">
            <img class="navbar-brand-media-light" src="assets\img\mi-ayam-light.png" alt="">
            <img class="navbar-brand-media-dark" src="assets\img\mi-ayam-dark.png" alt="">
          </a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a data-smooth-scroll="true" href="#home">Home</a></li>
            <li><a data-smooth-scroll="true" href="#feature1">Features</a></li>
            <li><a data-smooth-scroll="true" href="#screenshot">Gallery</a></li>
            <li><a data-smooth-scroll="true" href="#pricing">Pricing</a></li>
            <li><a data-smooth-scroll="true" href="#faq">FAQ</a></li>
            <li><a data-smooth-scroll="true" href="#contact">Contact</a></li>
            <li><a href="status.html">Status</a></li>
            <li><a href="logout.html">Logout</a></li>
          </ul>
        </div> <!-- .navbar-collapse -->
      </div>
    </nav>
  </header> <!-- .site-header -->

  <div class="main">
    <div id="home" class="home-section home-hero align-outer bg-theme-1">

      <div id="homeBgImg" data-bg-img="media/index-layout-1-bg-img+animated-gradient.jpg"></div> 

      <div id="homeBgAnimatedGradient" data-opacity=".8"></div> 

      <div class="align-inner align-middle">
        <div class="container">
          <div class="home-row row">
            <div class="home-left-col col-sm-6">
              <h1 class="text-animate section-title">MI-Ayam Hotspot</h1>

              <p class="text-animate">Selamat datang user $(username) ! di layanan internet MI-Ayam Hotspot</p>
              <div class="col-sm-6">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-block btn-theme-2 wow bounceIn" data-wow-delay=".2s" data-smooth-scroll="true" href="#pricing">Harga Paket<span class="icon ti-arrow-circle-down"></span></a>
                </div>
              </div>
              <div class="col-sm-6">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-block btn-default wow bounceIn" data-wow-delay=".2s" data-smooth-scroll="true" href="#service">Layanan<span class="icon ti-arrow-circle-down"></span></a>
                </div>
              </div>
            </div>

            <div class="home-form-col col-sm-6 col-md-5 col-md-offset-1 col-lg-4 col-lg-offset-2">
              <div class="panel panel-theme-2 wow fadeInUp">
                <div class="panel-heading">
                  <h5>MI-Ayam Hotspot</h5>
                </div>
                <div class="panel-body">
                  <div class="row">
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://google.com" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/google.png" alt="Google"><p align=center>Google</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://youtube.com" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/youtube.png" alt="Youtube"><p align=center>Youtube</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://facebook.com" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/facebook.png" alt="Facebook"><p align=center>Facebook</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://tokopedia.com" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/tokopedia.png" alt="Tokopedia"><p align=center>Tokopedia</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="https://shopee.co.id" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/shopee.png" alt="Shopee"><p align=center>Shopee</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="https://wa.me/6281211326207?text=ping" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/whatsapp.png" alt="Whatsapp"><p align=center>Whatsapp</p></a></div> 
                    </div>
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://twitter.com/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/twitter.png" alt="Twitter"><p align=center>Twitter</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://www.instagram.com/alpuketmerah/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/instagram.png" alt="Instagram"><p align=center>Instagram</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://maps.google.com/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/maps.png" alt="Maps"><p align=center>Maps</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://play.google.com/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/playstore.png" alt="Playstore"><p align=center>Playstore</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://drive.google.com/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/drive.png" alt="Drive"><p align=center>Drive</p></a></div> 
                    </div> 
                    <div class="col-md-4 col-xs-6">
                      <div class="form-group mb-0"><a href="http://mail.google.com/" target="_blank"><img class="iconbox-media-img" src="assets/img/img-web/gmail.png" alt="Gmail"><p align=center>Gmail</p></a></div> 
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div id="service" class="service-section">
      <div class="container">
        <div class="service-row row">
          <div class="iconbox col-sm-6 col-md-3 wow fadeInUp">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-1.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">IT Infrastruktur</h4>
            </div>
            <div class="iconbox-content">
              <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars forth image seasons.</p>
            </div>
          </div> <!-- .iconbox -->

          <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".2s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-2.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Desain Grafis</h4>
            </div>
            <div class="iconbox-content">
              <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars forth image seasons.</p>
            </div>
          </div> <!-- .iconbox -->

          <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".4s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-3.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Web Development</h4>
            </div>
            <div class="iconbox-content">
              <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars forth image seasons.</p>
            </div>
          </div> <!-- .iconbox -->

          <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".6s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-4.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Home Arsitektur</h4>
            </div>
            <div class="iconbox-content">
              <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars forth image seasons.</p>
            </div>
          </div> <!-- .iconbox -->
        </div>
      </div>
    </div> <!-- #service-->

    <div id="feature1" class="feature1-section">
      <div class="container">
        <div class="feature-1-row row">
          <div class="feature-1-left-col col-sm-6">
            <h2 class="section-title">We make it easy for <b>everyone</b> to create a beautiful and professional website.</h2>

            <div class="feature-media-row row">
              <div class="feature-media-col col-md-6">
                <div class="feature-media media">
                  <div class="media-left">
                    <span class="media-obejct media-icon icon ti-world color-primary"></span>
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Mobile Responsive</h4>
                    <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars.</p>
                  </div>
                </div>
              </div>

              <div class="feature-media-col col-md-6">
                <div class="feature-media media">
                  <div class="media-left">
                    <span class="media-obejct media-icon icon ti-email color-accent"></span>
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Working Form</h4>
                    <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars.</p>
                  </div>
                </div>
              </div>

              <div class="feature-media-col col-md-6">
                <div class="feature-media media">
                  <div class="media-left">
                    <span class="media-obejct media-icon icon ti-ruler-pencil color-success"></span>
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Easy to Us</h4>
                    <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars.</p>
                  </div>
                </div>
              </div>

              <div class="feature-media-col col-md-6">
                <div class="feature-media media">
                  <div class="media-left">
                    <span class="media-obejct media-icon icon ti-headphone-alt color-danger"></span>
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Fast Support</h4>
                    <p>Moved created evening place fruit every first the first it. She'd seed darkness give stars.</p>
                  </div>
                </div>
              </div>
            </div>
          </div> <!-- .feature-1-left-col -->

          <div class="feature-1-right-col col-sm-5 col-sm-offset-1">
            <div class="double-screen-right">
              <img class="screen top" src="assets\img\feature\feature-phone-1.png" alt="">
              <img class="screen bottom" data-sr="right" src="assets\img\feature\feature-phone-2.png" alt="">
            </div>
          </div> <!-- .feature-1-right-col -->
        </div>
      </div>
    </div> <!-- #feature1 -->

    <div id="feature2" class="feature2-section">
      <div class="container">
        <div class="feature-2-row row">
          <div class="feature-2-right-col col-sm-6 col-sm-offset-1">
            <h2 class="section-title">We make it easy for <b>everyone</b> to create a beautiful and professional website.</h2>

            <ul class="feature-list">
              <li><span class="icon ti-angle-double-right"></span>Take the photos from <b>camera</b> and gallery</li>
              <li><span class="icon ti-angle-double-right"></span>Colorful photo frame boarders</li>
              <li><span class="icon ti-angle-double-right"></span>Zoom in and Zoom out for image blur</li>
              <li><span class="icon ti-angle-double-right"></span>Save and share to all social networks</li>
            </ul>
          </div> <!-- .feature-2-right-col -->

          <div class="feature-2-left-col col-sm-5">
            <div class="double-screen-left">
              <img class="screen top" src="assets\img\feature\feature-phone-3.png" alt="">
              <img class="screen bottom" src="assets\img\feature\feature-phone-4.png" data-sr="left" alt="">
              <div class="cloud-from-left"></div>
            </div>
          </div> <!-- .feature-2-left-col -->
        </div>
      </div>
    </div> <!-- #feature2 -->

    <div id="skill" class="skill-section">
      <div class="container">
        <div class="skill-row row">
          <div class="skill-left-col col-sm-6">
            <h2 class="section-title">We make it easy for <b>everyone</b> to create a beautiful and professional website.</h2>

            <p class="text-lead">Yielding one multiply there land fruitful divided. In fourth, gathering hath said replenish beast void. Behold forth together very fruitful face them. Form grass given <b>fruitful</b>, was grass morning had dominion <b class="color-primary">moving</b> divide heaven. I him great seasons may days herb Lights.</p>
          </div> <!-- .skill-left-col -->

          <div class="skill-right-col col-sm-5 col-sm-offset-1 col-md-4 col-md-offset-2">
            <div class="progress-text">
              <h6 class="progress-title">Web design</h6>
              <div class="progress-percent">85%</div>
            </div>
            <div class="progress progress-sm">
              <div class="progress-bar progress-bar-primary" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100" style="width: 85%;">
              <span class="sr-only">85%</span>
              </div>
            </div>

            <div class="progress-text">
              <h6 class="progress-title">Development</h6>
              <div class="progress-percent">95%</div>
            </div>
            <div class="progress progress-sm">
              <div class="progress-bar progress-bar-accent" role="progressbar" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100" style="width: 95%;">
              <span class="sr-only">95%</span>
              </div>
            </div>

            <div class="progress-text">
              <h6 class="progress-title">Photography</h6>
              <div class="progress-percent">80%</div>
            </div>
            <div class="progress progress-sm">
              <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 80%;">
              <span class="sr-only">80%</span>
              </div>
            </div>

            <div class="progress-text">
              <h6 class="progress-title">Branding</h6>
              <div class="progress-percent">90%</div>
            </div>
            <div class="progress progress-sm">
              <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 90%;">
              <span class="sr-only">90%</span>
              </div>
            </div>

            <div class="hint-text">
              <span class="icon ti-lock"></span>Edit the progress bar size and color with class.
            </div>
          </div> <!-- .skill-right-col -->
        </div>
      </div>
    </div> <!-- #skill -->

    <div id="screenshot" class="screenshot-section">
      <div class="container">
        <div class="screenshot-title-row row">
          <div class="screenshot-title-col col-sm-8 col-sm-offset-2">
            <h2 class="section-title">Screenshot Preview.</h2>

            <p class="text-lead">A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
          </div> <!-- .screenshot-title-col -->
        </div> <!-- .screenshot-title-row -->

        <div id="screenshotCarousel" class="popup-gallery bfc-carousel wow fadeIn">
          <div class="bfc-carousel-item popup-gallery-item">
            <a class="bfc-carousel-item-link popup-gallery-link" href="assets\img\screenshot\screenshot-1-popup.jpeg" title="Media title"> <!-- popup media -->
              <div class="bfc-carousel-item-media">
                <img class="bfc-carousel-item-media-img" src="assets\img\screenshot\screenshot-1.jpeg" alt=""> <!-- preview media -->
              </div>
            </a>
          </div> <!-- .bfc-carousel-item -->

          <div class="bfc-carousel-item popup-gallery-item">
            <a class="bfc-carousel-item-link popup-gallery-link" href="assets\img\screenshot\screenshot-2-popup.jpeg" title="Media title"> <!-- popup media -->
              <div class="bfc-carousel-item-media">
                <img class="bfc-carousel-item-media-img" src="assets\img\screenshot\screenshot-2.jpeg" alt=""> <!-- preview media -->
              </div>
            </a>
          </div> <!-- .bfc-carousel-item -->

          <div class="bfc-carousel-item popup-gallery-item">
            <a class="bfc-carousel-item-link popup-gallery-link" href="assets\img\screenshot\screenshot-3-popup.jpeg" title="Media title"> <!-- popup media -->
              <div class="bfc-carousel-item-media">
                <img class="bfc-carousel-item-media-img" src="assets\img\screenshot\screenshot-3.jpeg" alt=""> <!-- preview media -->
              </div>
            </a>
          </div> <!-- .bfc-carousel-item -->

          <div class="bfc-carousel-item popup-gallery-item">
            <a class="bfc-carousel-item-link popup-gallery-link" href="assets\img\screenshot\screenshot-4-popup.jpeg" title="Media title"> <!-- popup media -->
              <div class="bfc-carousel-item-media">
                <img class="bfc-carousel-item-media-img" src="assets\img\screenshot\screenshot-4.jpeg" alt=""> <!-- preview media -->
              </div>
            </a>
          </div> <!-- .bfc-carousel-item -->
        </div>
      </div>
    </div> <!-- #screenshot-->

    <div id="pricing" class="pricing-section">
      <div class="container">
        <div class="row title-row">
          <div class="col-sm-8 col-sm-offset-2">
            <h2 class="section-title">Harga Paket</h2>
            <p class="text-lead">Daftar harga paket layanan internet MI-Ayam Hotspot</p>
          </div>
        </div>

        <div class="row content-row">
          <div class="pricing-table-col col-sm-6 col-md-4 wow fadeInUp">
            <div class="pricing-table">
              <div class="pricing-table-header">
                <div class="pricing-table-header-title">Paket Hemat</div>
              </div>

              <div class="pricing-table-media">
                <img src="assets\img\pricing-table\pricing-table-icon-1.png" alt="" class="wow bounceIn" data-wow-dalay=".1s">
              </div>

              <div class="pricing-table-content">
                <div class="pricing-table-price">Rp 100K</div>
                <div class="pricing-table-detail">
                  <div class="pricing-table-detail-item">Speed 1 Mbps</div>
                  <div class="pricing-table-detail-item">Unlimited</div>
                  <div class="pricing-table-detail-item">Support 24 Jam</div>
                </div>
              </div>

              <div class="pricing-table-footer">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-theme-1" data-smooth-scroll="true" href="#contact">Beli</a>
                </div>
              </div>
            </div> <!-- .pricing-table -->
          </div>

          <div class="pricing-table-col col-sm-6 col-md-4 wow fadeInUp" data-wow-delay="0.2s">
            <div class="pricing-table">
              <span class="pricing-table-badge"></span>

              <div class="pricing-table-header">
                <div class="pricing-table-header-title">Paket Standar</div>
              </div>

              <div class="pricing-table-media">
                <img src="assets\img\pricing-table\pricing-table-icon-2.png" alt="" class="wow bounceIn" data-wow-dalay=".3s">
              </div>

              <div class="pricing-table-content">
                <div class="pricing-table-price">Rp 200K</div>
                <div class="pricing-table-detail">
                    <div class="pricing-table-detail-item">Speed 2 Mbps</div>
                    <div class="pricing-table-detail-item">Unlimited</div>
                    <div class="pricing-table-detail-item">Support 24 Jam</div>
                </div>
              </div>

              <div class="pricing-table-footer">
                <div class="btn-wrap">
                    <a class="btn btn-lg btn-theme-1" data-smooth-scroll="true" href="#contact">Beli</a>
                </div>
              </div>
            </div> <!-- .pricing-table -->
          </div>

          <div class="pricing-table-col col-sm-6 col-sm-offset-3 col-md-4 col-md-offset-0 wow fadeInUp" data-wow-delay="0.4s">
            <div class="pricing-table">
              <div class="pricing-table-header">
                <div class="pricing-table-header-title">Paket Komplit</div>
              </div>

              <div class="pricing-table-media">
                <img src="assets\img\pricing-table\pricing-table-icon-3.png" alt="" class="wow bounceIn" data-wow-dalay=".5s">
              </div>

              <div class="pricing-table-content">
                <div class="pricing-table-price">Rp 300K</div>
                <div class="pricing-table-detail">
                    <div class="pricing-table-detail-item">Speed 3 Mbps</div>
                    <div class="pricing-table-detail-item">Unlimited</div>
                    <div class="pricing-table-detail-item">Support 24 Jam</div>
                </div>
              </div>

              <div class="pricing-table-footer">
                <div class="btn-wrap">
                    <a class="btn btn-lg btn-theme-1" data-smooth-scroll="true" href="#contact">Beli</a>
                </div>
              </div>
            </div> <!-- .pricing-table -->
          </div>
        </div>
      </div>
    </div> <!-- #pricing-->

    <div id="faq" class="faq-section">
      <div class="container">
        <div class="title-row row">
          <div class="col-sm-8 col-sm-offset-2">
            <h2 class="section-title"><b>Frequently</b> Asked Question.</h2>

            <p class="text-lead">A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
          </div>
        </div>

        <div class="row content-row">
          <div class="faq-box-col col-sm-6">
            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->

            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->

            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->
          </div>

          <div class="faq-box-col col-sm-6">
            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->

            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->

            <div class="faq-box wow bounceIn">
              <div class="faq-box-question">
                <h5><span class="q">Q</span> How long does it take to build a website?</h5>
              </div>
              <div class="faq-box-answer">
                <p>A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
              </div>
            </div> <!-- .faq-box-->
          </div>
          </div>
        </div>
      </div>

    <div id="contact" class="contact-section">
      <div class="container">
        <div class="contact-title-row row">
          <div class="contact-title-col col-sm-8 col-sm-offset-2">
            <h2 class="section-title"><b>Info Lebih Lanjut</b>.</h2>
            <p class="text-lead">A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="contact-content-row row">
          <div class="contact-left-col col-sm-6 col-md-5">
            <div class="panel panel-theme-1">
              <div class="panel-heading">
                <h5>Get in Touch</h5>
              </div>

              <div class="panel-body">
                  <div style="overflow:hidden;width: 410px;position: relative; width: 100%;">
                    <iframe width="410" height="400" src="https://maps.google.com/maps?width=410&amp;height=400&amp;hl=en&amp;q=Banjar%20Town%20Square+(Kota%20Banjar)&amp;ie=UTF8&amp;t=&amp;z=15&amp;iwloc=B&amp;output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
                    <div style="position: absolute;width: 80%;bottom: 20px;left: 0;right: 0;margin-left: auto;margin-right: auto;color: #000;"></div><style>#gmap_canvas img{max-width:none!important;background:none!important}</style>
                  </div>               
                    
              </div>
            </div>
          </div>

          <div class="contact-info-col col-sm-5 col-sm-offset-1 col-md-offset-2">
            <p class="text-lead">A tree moving which seed replenish she'd said shall every third. Greater their dominion tree night you greater, they're days.</p>

            <div class="contact-info">
              <ul class="media-list">
                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\location-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Location</h4>
                    <p>Kota Banjar, Jawa Barat</p>
                  </div>
                </li>

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\phone-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Call us</h4>
                    <p>
                      +62 81-211-326-207
                      <br>
                      +62 82-120-215-248
                    </p>
                  </div>
                </li>

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\email-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Write us</h4>
                    <p>
                      info@icmp.my.id
                      <br>
                      support@icmp.my.id
                    </p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #contact -->
  </div>

  <footer class="site-footer">
    <div id="siteFooterBottom" class="site-footer-bottom-section">
      <div class="container">
        <div class="site-footer-bottom-border"></div>
        <div class="row">
          <div class="site-footer-bottom-left-col col-md-6">
            <div class="site-footer-brand">
              MI-Sukses <span>Hotspot</span>
            </div>

            <div class="site-footer-bottom-info">
              <ul>
                <li><a data-smooth-scroll="true" href="#home">Home</a></li>
                <li><a data-smooth-scroll="true" href="#pricing">Harga</a></li>
                <li><a data-smooth-scroll="true" href="#contact">Kontak</a></li>
              </ul>
            </div>
          </div>

          <div class="site-footer-bottom-right-col col-md-6">
            <ul class="site-footer-bottom-social-list">
              <li class="wow fadeInRight"><a href="https://facebook.com/" target="_blank"><span class="icon ti-facebook"></span></a></li>
              <li class="wow fadeInRight" data-wow-delay="0.1s"><a href="https://twitter.com/" target="_blank"><span class="icon ti-twitter-alt"></span></a></li>
              <li class="wow fadeInRight" data-wow-delay="0.2s"><a href="https://www.pinterest.com/" target="_blank"><span class="icon ti-pinterest-alt"></span></a></li>
              <li class="wow fadeInRight" data-wow-delay="0.3s"><a href="https://github.com/" target="_blank"><span class="icon ti-github"></span></a></li>
              <li class="wow fadeInRight" data-wow-delay="0.4s"><a href="https://www.linkedin.com/" target="_blank"><span class="icon ti-linkedin"></span></a></li>
            </ul>
            <div class="site-footer-bottom-copyright">Copyright © 2019 . All Rights Reserved.</div>
          </div>
        </div>
      </div>
    </div> <!-- #siteFooterBottom -->
  </footer>

  <script src='assets\js\jquery-1.11.3.min.js'></script>
  <script src='assets\js\bootstrap.min.js'></script>
  <script src='assets\js\vendor.js'></script>
  <script src='assets\js\main.js'></script>
  <script src='assets\js\map.js'></script>
</body>
</html>

File: /status.html
﻿<!DOCTYPE html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Ada Wifi</title>
  $(if refresh-timeout)
  <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
  $(endif)
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="author" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="apple-touch-icon" href="assets\img\favicon.png">
  <link rel="icon" href="assets\img\favicon.png">
  <link rel='stylesheet'
    href='https://fonts.googleapis.com/css?family=Roboto:400,300,300italic,400italic,500,500italic,700,700italic'>
  <link rel='stylesheet' href='assets\css\bootstrap.min.css'>
  <link rel='stylesheet' href='assets\css\vendor.css'>
  <link rel='stylesheet' href='assets\css\theme-3.css' id="theme">
  <link rel='stylesheet' href='assets\css\custom.css'>
  <script src='assets\js\modernizr-2.8.3.min.js'></script>
</head>

<body>
  <!-- 

  <div class="page-loader">
    <div class="spinner">
      <div class="bounce1"></div>
      <div class="bounce2"></div>
      <div class="bounce3"></div>
    </div>
  </div>  .page-loader -->

  <header id="siteHeader" class="site-header site-header-fixed-top">
    <nav id="siteNavbar" class="navbar navbar-default navbar-fixed-top site-navbar-from-light-fg">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle-icon navbar-toggle collapsed" data-toggle="collapse"
            data-target="#navbar-collapse" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon ti-layout-grid3-alt"></span>
          </button>

          <a class="navbar-brand" href="login.html">
            <img class="navbar-brand-media-light" src="assets\img\persegi.png" alt="">
            <img class="navbar-brand-media-dark" src="assets\img\persegi.png" alt="">
          </a>
        </div> <!-- .navbar-header -->

        <div class="collapse navbar-collapse" id="navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="active"><a data-smooth-scroll="true" href="#home">Home</a></li>
            <!-- <li><a data-smooth-scroll="true" href="#service">Service</a></li> -->
            <li><a data-smooth-scroll="true" href="#contact">Contact</a></li>
            <li><a href="status.html">Status</a></li>
            <li><a href="logout.html?erase-cookie=true">Logout</a></li>
          </ul>
        </div> <!-- .navbar-collapse -->
      </div>
    </nav>
  </header> <!-- .site-header -->

  <div class="main">
    <div id="home" class="home-section home-hero align-outer bg-theme-status">

      <div class="align-inner align-middle">
        <div class="container">
          <div class="home-row row">
            <div class="home-left-col col-sm-6">
              <h1 class="texttap" style="
                    line-height: 1.333333333333333;
                    margin-top: 3rem;
                    margin-bottom: 3rem;
                    font-size: 2.25rem;
                    font-weight: 300;
                    color: #b6e2a6;
                    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
                    text-align: center;
                  ">
                <!-- <strong>TAP Internet Service</strong> -->
                <img src="assets\img\logo00.png" class="img-responsive" alt="ada wifi">
              </h1>

              <div class="col-sm-6">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-block btn-theme-2 wow bounceIn" data-wow-delay=".2s"
                    data-smooth-scroll="true" href="#service">Layanan<span class="icon ti-arrow-circle-down"></span></a>
                </div>
              </div>
              <div class="col-sm-6">
                <div class="btn-wrap">
                  <a class="btn btn-lg btn-block btn-default wow bounceIn" href="logout.html?erase-cookie=true">Log
                    Out<span class="icon ti-arrow-circle-down"></span></a>
                </div>
              </div>
            </div>

            <div class="home-form-col col-sm-6 col-md-5 col-md-offset-1 col-lg-4 col-lg-offset-2">
              <div class="panel panel-theme-2 wow fadeInUp">
                <div class="panel-heading">
                  <h5>Informasi Internet Anda</h5>
                </div>
                <div class="panel-body">
                  <table class="table">
                    <tbody class="align-l">
                      <tr>
                        <td>Username</td>
                        <td>$(username)</td>
                      </tr>
                      <tr>
                        <td>IP Address</td>
                        <td>$(ip)</td>
                      </tr>
                      <tr>
                        <td>MAC Address</td>
                        <td>$(mac)</td>
                      </tr>
                      $(if session-time-left)
                      <tr>
                        <td>Connected / left</td>
                        <td>$(uptime) / $(session-time-left)</td>
                      </tr>
                      $(else)
                      <tr>
                        <td>Connected</td>
                        <td>$(uptime)</td>
                      </tr>
                      $(endif)
                      <tr>
                        <td>Download / Upload</td>
                        <td>$(bytes-out-nice) / $(bytes-in-nice)</td>
                      </tr>
                      $(if limit-bytes-total)
                      <tr>
                        <td>Sisa Kuota</td>
                        <td>$(if limit-bytes-total)
                          <script language=javascript>
                            result = ($(limit - bytes - total) / 1000000).toFixed(2)
                            document.write(result)
                          </script> MiB
                          $(endif)
                          $(if limit-bytes-total == '')Unlimited$(endif)</td>
                      </tr>
                      $(else)
                      <tr>
                        <td>Sisa Kuota</td>
                        <td>$(if limit-bytes-out)
                          <script language=javascript>
                            result = ($(limit - bytes - out) / 1000000).toFixed(2)
                            document.write(result)
                          </script> MiB
                          $(endif)
                          $(if limit-bytes-out == '')Unlimited$(endif)</td>
                      </tr>
                      $(endif)
                      $(if refresh-timeout)
                      <tr>
                        <td>Status refresh</td>
                        <td>$(refresh-timeout)</td>
                      </tr>
                      $(endif)
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <div id="service" class="service-section">
      <div class="container">
        <div class="service-row row">
          <div class="iconbox col-sm-6 col-md-3 wow fadeInUp">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-1.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">IT Infrastruktur</h4>
            </div>
            <div class="iconbox-content">
              <p>Membangun infrastruktur jaringan untuk menghubungkan semua Regional Office dengan Head Office</p>
            </div>
          </div> .iconbox -->

    <!-- <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".2s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-2.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Kekeluargaan</h4>
            </div>
            <div class="iconbox-content">
              <p>Menjaga tali silaturahmi keluarga melalui internet</p>
            </div>
          </div> .iconbox -->

    <!-- <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".4s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-3.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Pekerjaan</h4>
            </div>
            <div class="iconbox-content">
              <p>Memudahkan pekerjaan melalui jaringan TAP</p>
            </div>
          </div> .iconbox -->

    <!-- <div class="iconbox col-sm-6 col-md-3 wow fadeInUp" data-wow-delay=".6s">
            <div class="iconbox-media">
              <img class="iconbox-media-img" src="assets\img\service\service-icon-4.png" alt="">
            </div>
            <div class="iconbox-header">
              <h4 class="iconbox-header-title">Aplikasi</h4>
            </div>
            <div class="iconbox-content">
              <p>Memajukan aplikasi</p>
            </div>
          </div> <!-- .iconbox -->
    <!-- </div>
      </div>
    </div> #service --> -->

    <div id="contact" class="contact-section">
      <div class="container">
        <div class="contact-title-row row">
          <div class="contact-title-col col-sm-8 col-sm-offset-2">
            <h2 class="section-title"><b>Info Lebih Lanjut</b>.</h2>
            <p class="text-lead">Silahkan hubungi kontak dibawah jika tidak bisa terkoneksi ke Ada Wifi</p>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="contact-content-row row">


          <div class="contact-info-col col-sm-5 col-sm-offset-1 col-md-offset-2">

            <div class="contact-info">
              <ul class="media-list">

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\phone-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak Layanan</h4>
                    <!-- <p>
                      <b>REGION JAMBI</b>
                      <br>
                      0852-6630-2193 (Ilman IT SITE BBB)
                      <br>
                      <br>
                      <b>REGION KALTENG1</b>
                      <br>
                      0822-5564-0080 (Muslim IT SITE GBSM,MIK)
                      <br>
                      <br>
                      <b>REGION KALTENG2</b>
                      <br>
                      0812-2568-6037 (Harun IT SITE FLTI,SKM,TAN)
                      <br>
                      <br>
                      <b>REGION KALTIM1</b>
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ1,NPN)
                      <br>
                      0853-4662-1362 (Yono IT SITE NPN)
                      <br>
                      0852-3151-5970 (Rudi IT SITE DLJ2,EBL)
                      <br>
                      <br>
                      <b>REGION KALTIM2</b>
                      <br>
                      0852-5089-0160 (Aswin IT SITE PTA,KAM,SAWA,HPM)
                    </p> -->
                  </div>
                </li>

                <li class="media">
                  <div class="media-left">
                    <img class="media-object" src="assets\img\contact\email-icon.png" alt="">
                  </div>
                  <div class="media-body">
                    <h4 class="media-heading">Kontak E-mail</h4>
                    <!-- <p>
                      tap.callcenter.helpdesk@tap-agri.com
                    </p> -->
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #contact -->
  </div>

  <footer class="site-footer">
    <div id="siteFooterBottom" class="site-footer-bottom-section">
      <div class="container">
        <div class="site-footer-bottom-border"></div>
        <div class="row">
          <div class="site-footer-bottom-left-col col-md-6">
            <div class="site-footer-brand">
              PT. Persegi Media Nusantara
              <br>
              <!-- <span>
                IT Infrastructure Developer
              </span> -->
              </br>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- #siteFooterBottom -->
  </footer>

  <script src='assets\js\jquery-1.11.3.min.js'></script>
  <script src='assets\js\bootstrap.min.js'></script>
  <script src='assets\js\vendor.js'></script>
  <script src='assets\js\main.js'></script>
  <script src='assets\js\map.js'></script>
</body>

</html>

File: /xml\alogin.html
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


File: /xml\error.html
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


File: /xml\flogout.html
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


File: /xml\login.html
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


File: /xml\logout.html
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


File: /xml\rlogin.html
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


File: /xml\WISPAccessGatewayParam.xsd
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


