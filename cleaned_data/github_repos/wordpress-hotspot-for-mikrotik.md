# Repository Information
Name: wordpress-hotspot-for-mikrotik

# Directory Structure
Directory structure:
└── github_repos/wordpress-hotspot-for-mikrotik/
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
    │   │       ├── pack-8ef6d1f3f75c75604baccc21e386dc8a7e07a26d.idx
    │   │       └── pack-8ef6d1f3f75c75604baccc21e386dc8a7e07a26d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── admin/
    │   ├── class-hotspot-for-mikrotik-admin.php
    │   ├── css/
    │   │   └── hotspot-for-mikrotik-admin.css
    │   ├── index.php
    │   ├── js/
    │   │   └── hotspot-for-mikrotik-admin.js
    │   └── partials/
    │       └── hotspot-for-mikrotik-admin-display.php
    ├── assets/
    │   └── img/
    ├── composer.json
    ├── hotspot-for-mikrotik.php
    ├── includes/
    │   ├── class-hotspot-for-mikrotik-activator.php
    │   ├── class-hotspot-for-mikrotik-deactivator.php
    │   ├── class-hotspot-for-mikrotik-i18n.php
    │   ├── class-hotspot-for-mikrotik-loader.php
    │   ├── class-hotspot-for-mikrotik.php
    │   ├── class-wp-route.php
    │   └── index.php
    ├── index.php
    ├── languages/
    │   └── hotspot-for-mikrotik.pot
    ├── LICENSE.txt
    ├── public/
    │   ├── class-hotspot-for-mikrotik-public.php
    │   ├── css/
    │   │   ├── hotspot-for-mikrotik-public.css
    │   │   └── mikrotik.css
    │   ├── index.php
    │   ├── js/
    │   │   ├── hotspot-for-mikrotik-public.js
    │   │   └── mikrotik-md5.js
    │   └── partials/
    │       └── hotspot-for-mikrotik-public-display.php
    ├── README.txt
    ├── templates/
    │   ├── login.php
    │   └── router/
    │       └── login.html
    └── uninstall.php


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
	url = https://github.com/mbezuidenhout/wordpress-hotspot-for-mikrotik.git
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
0000000000000000000000000000000000000000 dc0f62f0f5f5758303762535d46774510abffd67 vivek-dodia <vivek.dodia@icloud.com> 1738606094 -0500	clone: from https://github.com/mbezuidenhout/wordpress-hotspot-for-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 dc0f62f0f5f5758303762535d46774510abffd67 vivek-dodia <vivek.dodia@icloud.com> 1738606094 -0500	clone: from https://github.com/mbezuidenhout/wordpress-hotspot-for-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 dc0f62f0f5f5758303762535d46774510abffd67 vivek-dodia <vivek.dodia@icloud.com> 1738606094 -0500	clone: from https://github.com/mbezuidenhout/wordpress-hotspot-for-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
dc0f62f0f5f5758303762535d46774510abffd67 refs/remotes/origin/master


File: /.git\refs\heads\master
dc0f62f0f5f5758303762535d46774510abffd67


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/vendor/
/composer.lock


File: /admin\class-hotspot-for-mikrotik-admin.php
<?php
/**
 * The admin-specific functionality of the plugin.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/admin
 */

/**
 * The admin-specific functionality of the plugin.
 *
 * Defines the plugin name, version, and two examples hooks for how to
 * enqueue the admin-specific stylesheet and JavaScript.
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/admin
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_Admin {

	/**
	 * The ID of this plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 * @var      string    $plugin_name    The ID of this plugin.
	 */
	private $plugin_name;

	/**
	 * The version of this plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 * @var      string    $version    The current version of this plugin.
	 */
	private $version;

	/**
	 * Initialize the class and set its properties.
	 *
	 * @since    1.0.0
	 * @param      string $plugin_name       The name of this plugin.
	 * @param      string $version    The version of this plugin.
	 */
	public function __construct( $plugin_name, $version ) {

		$this->plugin_name = $plugin_name;
		$this->version     = $version;

	}

	/**
	 * Register the stylesheets for the admin area.
	 *
	 * @since    1.0.0
	 */
	public function enqueue_styles() {

		/**
		 * This function is provided for demonstration purposes only.
		 *
		 * An instance of this class should be passed to the run() function
		 * defined in Hotspot_For_Mikrotik_Loader as all of the hooks are defined
		 * in that particular class.
		 *
		 * The Hotspot_For_Mikrotik_Loader will then create the relationship
		 * between the defined hooks and the functions defined in this
		 * class.
		 */

		wp_enqueue_style( $this->plugin_name, plugin_dir_url( __FILE__ ) . 'css/hotspot-for-mikrotik-admin.css', array(), $this->version, 'all' );

	}

	/**
	 * Register the JavaScript for the admin area.
	 *
	 * @since    1.0.0
	 */
	public function enqueue_scripts() {

		/**
		 * This function is provided for demonstration purposes only.
		 *
		 * An instance of this class should be passed to the run() function
		 * defined in Hotspot_For_Mikrotik_Loader as all of the hooks are defined
		 * in that particular class.
		 *
		 * The Hotspot_For_Mikrotik_Loader will then create the relationship
		 * between the defined hooks and the functions defined in this
		 * class.
		 */

		wp_enqueue_script( $this->plugin_name, plugin_dir_url( __FILE__ ) . 'js/hotspot-for-mikrotik-admin.js', array( 'jquery' ), $this->version, false );

	}

	public function plugin_section_text( $section ) {
		$test = 1;
	}

	public function mikrotik_hotspot_field( $args ) {
		global $wp_settings_fields;
		$options = get_option( $args['label_for'] );
		switch ( $args['type'] ) {
			case 'text':
				echo "<input name=\"" . $args['label_for'] . "\" type=\"" . $args['type'] . "\" id=\"" . $args['label_for'] . "\" value=\"\" class=\"regular-text\">";
				break;
		}

	}

	/**
	 * Register plugin settings
	 *
	 * @since    1.0.0
	 */
	public function register_settings() {
		add_settings_section( 'router_settings', 'Router Settings', array( $this, 'plugin_section_text' ), 'mikrotik_hotspot_plugin' );

		add_settings_field(
			'hotspot_admin_username',
			'Hotspot Admin Username',
			array( $this, 'mikrotik_hotspot_field' ),
			'mikrotik_hotspot_plugin',
			'router_settings',
			array(
				'label_for' => 'username',
				'type'      => 'text',
			),
		);
		add_settings_field(
			'hotspot_admin_password',
			'Hotspot Admin Password',
			array( $this, 'mikrotik_hotspot_field' ),
			'mikrotik_hotspot_plugin',
			'router_settings',
			array(
				'label_for' => 'password',
			),
		);
		register_setting( 'mikrotik_hotspot_plugin_options', 'mikrotik_hotspot_username' );
	}

	/**
	 * Add plugin settings page.
	 *
	 * @since    1.0.0
	 */
	public function add_settings_page() {
		add_options_page( __('Mikrotik Hotspot Settings'), __('Mikrotik Hotspot'), 'manage_options', 'mikrotik-hotspot-settings', array( $this, 'render_settings_page' ) );
	}

	public function render_settings_page( $args ) {
		global $wp_settings_sections;
		?>
        <div class="wrap">
		<h1><?php echo esc_html(get_admin_page_title()) ?></h1>
		<form action="options.php" method="post">
			<?php
			settings_fields( 'mikrotik_hotspot_plugin_options' );
			do_settings_sections( 'mikrotik_hotspot_plugin' );
            submit_button();
            ?>
		</form>
        </div>
		<?php
	}

	/**
	 * Add a direct link from the plugin page to the settings page for this plugin.
	 *
	 * @param array $links An array of links to display in the WordPress plugin list.
	 *
	 * @return array
	 */
	public function plugin_links( $links ) {
		$settings_url = add_query_arg(
			array(
				'page'    => 'mikrotik-hotspot-settings',
			),
			admin_url( 'admin.php' )
		);

		$plugin_links = array(
			'<a href="' . esc_url( $settings_url ) . '">' . __( 'Settings' ) . '</a>',
		);

		return array_merge( $plugin_links, $links );
	}
}


File: /admin\css\hotspot-for-mikrotik-admin.css
/**
 * All of the CSS for your admin-specific functionality should be
 * included in this file.
 */

File: /admin\index.php
<?php // Silence is golden

File: /admin\js\hotspot-for-mikrotik-admin.js
(function( $ ) {
	'use strict';

	/**
	 * All of the code for your admin-facing JavaScript source
	 * should reside in this file.
	 *
	 * Note: It has been assumed you will write jQuery code here, so the
	 * $ function reference has been prepared for usage within the scope
	 * of this function.
	 *
	 * This enables you to define handlers, for when the DOM is ready:
	 *
	 * $(function() {
	 *
	 * });
	 *
	 * When the window is loaded:
	 *
	 * $( window ).load(function() {
	 *
	 * });
	 *
	 * ...and/or other possibilities.
	 *
	 * Ideally, it is not considered best practise to attach more than a
	 * single DOM-ready or window-load handler for a particular page.
	 * Although scripts in the WordPress core, Plugins and Themes may be
	 * practising this, we should strive to set a better example in our own work.
	 */

})( jQuery );


File: /admin\partials\hotspot-for-mikrotik-admin-display.php
<?php

/**
 * Provide a admin area view for the plugin
 *
 * This file is used to markup the admin-facing aspects of the plugin.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/admin/partials
 */
?>

<!-- This file should primarily consist of HTML with a little bit of PHP. -->


File: /composer.json
{
    "require": {
        "pear2/net_routeros": "1.0.0b6",
        "pear2/net_transmitter": "1.0.0b1"
    }
}


File: /hotspot-for-mikrotik.php
<?php
/**
 * The plugin bootstrap file
 *
 * This file is read by WordPress to generate the plugin information in the plugin
 * admin area. This file also includes all of the dependencies used by the plugin,
 * registers the activation and deactivation functions, and defines a function
 * that starts the plugin.
 *
 * @package    Hotspot_For_Mikrotik
 * @author     Marius Bezuidenhout
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @wordpress-plugin
 * Plugin Name:       Hotspot for Mikrotik routers
 * Plugin URI:        https://github.com/mbezuidenhout/wordpress-hotspot-for-mirkotik
 * Description:       Replace the login.html page on your Mikrotik router and create your own hotspot login page.
 * Version:           1.0.0
 * Requires at least: 4.9
 * Tested up to:      5.7.0
 * Author:            Marius Bezuidenhout
 * Author URI:        https://profiles.wordpress.org/mbezuidenhout/
 * License:           GPL-2.0+
 * License URI:       http://www.gnu.org/licenses/gpl-2.0.txt
 * Text Domain:       hotspot-for-mikrotik
 * Domain Path:       /languages
 */

// If this file is called directly, abort.
if ( ! defined( 'WPINC' ) ) {
	die;
}

/**
 * Currently plugin version.
 * Start at version 1.0.0 and use SemVer - https://semver.org
 * Rename this for your plugin and update it as you release new versions.
 */
define( 'HOTSPOT_FOR_MIKROTIK_VERSION', '1.0.0' );

/**
 * The plugin file used in WordPress
 */
define( 'HOTSPOT_FOR_MIKROTIK_PLUGIN_FILE', __FILE__ );

/**
 * The code that runs during plugin activation.
 * This action is documented in includes/class-hotspot-for-mikrotik-activator.php
 */
function activate_hotspot_for_mikrotik() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-hotspot-for-mikrotik-activator.php';
	Hotspot_For_Mikrotik_Activator::activate();
}

/**
 * The code that runs during plugin deactivation.
 * This action is documented in includes/class-hotspot-for-mikrotik-deactivator.php
 */
function deactivate_hotspot_for_mikrotik() {
	require_once plugin_dir_path( __FILE__ ) . 'includes/class-hotspot-for-mikrotik-deactivator.php';
	Hotspot_For_Mikrotik_Deactivator::deactivate();
}

register_activation_hook( __FILE__, 'activate_hotspot_for_mikrotik' );
register_deactivation_hook( __FILE__, 'deactivate_hotspot_for_mikrotik' );

/**
 * The core plugin class that is used to define internationalization,
 * admin-specific hooks, and public-facing site hooks.
 */
require plugin_dir_path( __FILE__ ) . 'includes/class-hotspot-for-mikrotik.php';

/**
 * Begins execution of the plugin.
 *
 * Since everything within the plugin is registered via hooks,
 * then kicking off the plugin from this point in the file does
 * not affect the page life cycle.
 *
 * @since    1.0.0
 */
function run_hotspot_for_mikrotik() {

	$plugin = new Hotspot_For_Mikrotik();
	$plugin->run();

}
run_hotspot_for_mikrotik();


File: /includes\class-hotspot-for-mikrotik-activator.php
<?php

/**
 * Fired during plugin activation
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 */

/**
 * Fired during plugin activation.
 *
 * This class defines all code necessary to run during the plugin's activation.
 *
 * @since      1.0.0
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_Activator {

	/**
	 * Short Description. (use period)
	 *
	 * Long Description.
	 *
	 * @since    1.0.0
	 */
	public static function activate() {

	}

}


File: /includes\class-hotspot-for-mikrotik-deactivator.php
<?php

/**
 * Fired during plugin deactivation
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 */

/**
 * Fired during plugin deactivation.
 *
 * This class defines all code necessary to run during the plugin's deactivation.
 *
 * @since      1.0.0
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_Deactivator {

	/**
	 * Short Description. (use period)
	 *
	 * Long Description.
	 *
	 * @since    1.0.0
	 */
	public static function deactivate() {

	}

}


File: /includes\class-hotspot-for-mikrotik-i18n.php
<?php

/**
 * Define the internationalization functionality
 *
 * Loads and defines the internationalization files for this plugin
 * so that it is ready for translation.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 */

/**
 * Define the internationalization functionality.
 *
 * Loads and defines the internationalization files for this plugin
 * so that it is ready for translation.
 *
 * @since      1.0.0
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_i18n {


	/**
	 * Load the plugin text domain for translation.
	 *
	 * @since    1.0.0
	 */
	public function load_plugin_textdomain() {

		load_plugin_textdomain(
			'hotspot-for-mikrotik',
			false,
			dirname( dirname( plugin_basename( __FILE__ ) ) ) . '/languages/'
		);

	}



}


File: /includes\class-hotspot-for-mikrotik-loader.php
<?php

/**
 * Register all actions and filters for the plugin
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 */

/**
 * Register all actions and filters for the plugin.
 *
 * Maintain a list of all hooks that are registered throughout
 * the plugin, and register them with the WordPress API. Call the
 * run function to execute the list of actions and filters.
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_Loader {

	/**
	 * The array of actions registered with WordPress.
	 *
	 * @since    1.0.0
	 * @access   protected
	 * @var      array    $actions    The actions registered with WordPress to fire when the plugin loads.
	 */
	protected $actions;

	/**
	 * The array of filters registered with WordPress.
	 *
	 * @since    1.0.0
	 * @access   protected
	 * @var      array    $filters    The filters registered with WordPress to fire when the plugin loads.
	 */
	protected $filters;

	/**
	 * Initialize the collections used to maintain the actions and filters.
	 *
	 * @since    1.0.0
	 */
	public function __construct() {

		$this->actions = array();
		$this->filters = array();

	}

	/**
	 * Add a new action to the collection to be registered with WordPress.
	 *
	 * @since    1.0.0
	 * @param    string               $hook             The name of the WordPress action that is being registered.
	 * @param    object               $component        A reference to the instance of the object on which the action is defined.
	 * @param    string               $callback         The name of the function definition on the $component.
	 * @param    int                  $priority         Optional. The priority at which the function should be fired. Default is 10.
	 * @param    int                  $accepted_args    Optional. The number of arguments that should be passed to the $callback. Default is 1.
	 */
	public function add_action( $hook, $component, $callback, $priority = 10, $accepted_args = 1 ) {
		$this->actions = $this->add( $this->actions, $hook, $component, $callback, $priority, $accepted_args );
	}

	/**
	 * Add a new filter to the collection to be registered with WordPress.
	 *
	 * @since    1.0.0
	 * @param    string               $hook             The name of the WordPress filter that is being registered.
	 * @param    object               $component        A reference to the instance of the object on which the filter is defined.
	 * @param    string               $callback         The name of the function definition on the $component.
	 * @param    int                  $priority         Optional. The priority at which the function should be fired. Default is 10.
	 * @param    int                  $accepted_args    Optional. The number of arguments that should be passed to the $callback. Default is 1
	 */
	public function add_filter( $hook, $component, $callback, $priority = 10, $accepted_args = 1 ) {
		$this->filters = $this->add( $this->filters, $hook, $component, $callback, $priority, $accepted_args );
	}

	/**
	 * A utility function that is used to register the actions and hooks into a single
	 * collection.
	 *
	 * @since    1.0.0
	 * @access   private
	 * @param    array                $hooks            The collection of hooks that is being registered (that is, actions or filters).
	 * @param    string               $hook             The name of the WordPress filter that is being registered.
	 * @param    object               $component        A reference to the instance of the object on which the filter is defined.
	 * @param    string               $callback         The name of the function definition on the $component.
	 * @param    int                  $priority         The priority at which the function should be fired.
	 * @param    int                  $accepted_args    The number of arguments that should be passed to the $callback.
	 * @return   array                                  The collection of actions and filters registered with WordPress.
	 */
	private function add( $hooks, $hook, $component, $callback, $priority, $accepted_args ) {

		$hooks[] = array(
			'hook'          => $hook,
			'component'     => $component,
			'callback'      => $callback,
			'priority'      => $priority,
			'accepted_args' => $accepted_args
		);

		return $hooks;

	}

	/**
	 * Register the filters and actions with WordPress.
	 *
	 * @since    1.0.0
	 */
	public function run() {

		foreach ( $this->filters as $hook ) {
			add_filter( $hook['hook'], array( $hook['component'], $hook['callback'] ), $hook['priority'], $hook['accepted_args'] );
		}

		foreach ( $this->actions as $hook ) {
			add_action( $hook['hook'], array( $hook['component'], $hook['callback'] ), $hook['priority'], $hook['accepted_args'] );
		}

	}

}


File: /includes\class-hotspot-for-mikrotik.php
<?php
/**
 * The file that defines the core plugin class
 *
 * A class definition that includes attributes and functions used across both the
 * public-facing side of the site and the admin area.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 */

/**
 * The core plugin class.
 *
 * This is used to define internationalization, admin-specific hooks, and
 * public-facing site hooks.
 *
 * Also maintains the unique identifier of this plugin as well as the current
 * version of the plugin.
 *
 * @since      1.0.0
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/includes
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik {

	/**
	 * The loader that's responsible for maintaining and registering all hooks that power
	 * the plugin.
	 *
	 * @since    1.0.0
	 * @access   protected
	 * @var      Hotspot_For_Mikrotik_Loader    $loader    Maintains and registers all hooks for the plugin.
	 */
	protected $loader;

	/**
	 * The unique identifier of this plugin.
	 *
	 * @since    1.0.0
	 * @access   protected
	 * @var      string    $plugin_name    The string used to uniquely identify this plugin.
	 */
	protected $plugin_name;

	/**
	 * The current version of the plugin.
	 *
	 * @since    1.0.0
	 * @access   protected
	 * @var      string    $version    The current version of the plugin.
	 */
	protected $version;

	/**
	 * Define the core functionality of the plugin.
	 *
	 * Set the plugin name and the plugin version that can be used throughout the plugin.
	 * Load the dependencies, define the locale, and set the hooks for the admin area and
	 * the public-facing side of the site.
	 *
	 * @since    1.0.0
	 */
	public function __construct() {
		if ( defined( 'HOTSPOT_FOR_MIKROTIK_VERSION' ) ) {
			$this->version = HOTSPOT_FOR_MIKROTIK_VERSION;
		} else {
			$this->version = '1.0.0';
		}
		$this->plugin_name = 'hotspot-for-mikrotik';

		$this->load_dependencies();
		$this->set_locale();
		$this->define_admin_hooks();
		$this->define_public_hooks();

	}

	/**
	 * Load the required dependencies for this plugin.
	 *
	 * Include the following files that make up the plugin:
	 *
	 * - Hotspot_For_Mikrotik_Loader. Orchestrates the hooks of the plugin.
	 * - Hotspot_For_Mikrotik_i18n. Defines internationalization functionality.
	 * - Hotspot_For_Mikrotik_Admin. Defines all hooks for the admin area.
	 * - Hotspot_For_Mikrotik_Public. Defines all hooks for the public side of the site.
	 *
	 * Create an instance of the loader which will be used to register the hooks
	 * with WordPress.
	 *
	 * @since    1.0.0
	 * @access   private
	 */
	private function load_dependencies() {

		/**
		 * The class responsible for orchestrating the actions and filters of the
		 * core plugin.
		 */
		require_once plugin_dir_path( dirname( __FILE__ ) ) . 'includes/class-hotspot-for-mikrotik-loader.php';

		/**
		 * The class responsible for defining internationalization functionality
		 * of the plugin.
		 */
		require_once plugin_dir_path( dirname( __FILE__ ) ) . 'includes/class-hotspot-for-mikrotik-i18n.php';

		/**
		 * The class responsible for defining all actions that occur in the admin area.
		 */
		require_once plugin_dir_path( dirname( __FILE__ ) ) . 'admin/class-hotspot-for-mikrotik-admin.php';

		/**
		 * The class responsible for defining all actions that occur in the public-facing
		 * side of the site.
		 */
		require_once plugin_dir_path( dirname( __FILE__ ) ) . 'public/class-hotspot-for-mikrotik-public.php';

		/**
		 * Composer libraries
		 */
		require_once plugin_dir_path( dirname( __FILE__ ) ) . 'vendor' . DIRECTORY_SEPARATOR . 'autoload.php';

		$this->loader = new Hotspot_For_Mikrotik_Loader();

	}

	/**
	 * Define the locale for this plugin for internationalization.
	 *
	 * Uses the Hotspot_For_Mikrotik_i18n class in order to set the domain and to register the hook
	 * with WordPress.
	 *
	 * @since    1.0.0
	 * @access   private
	 */
	private function set_locale() {

		$plugin_i18n = new Hotspot_For_Mikrotik_i18n();

		$this->loader->add_action( 'plugins_loaded', $plugin_i18n, 'load_plugin_textdomain' );

	}

	/**
	 * Register all of the hooks related to the admin area functionality
	 * of the plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 */
	private function define_admin_hooks() {

		$plugin_admin = new Hotspot_For_Mikrotik_Admin( $this->get_plugin_name(), $this->get_version() );

		$this->loader->add_action( 'admin_enqueue_scripts', $plugin_admin, 'enqueue_styles' );
		$this->loader->add_action( 'admin_enqueue_scripts', $plugin_admin, 'enqueue_scripts' );

		$this->loader->add_action( 'admin_menu', $plugin_admin, 'add_settings_page', 50 );
		$this->loader->add_action( 'admin_init', $plugin_admin, 'register_settings' );
		$this->loader->add_filter( 'plugin_action_links_' . plugin_basename( HOTSPOT_FOR_MIKROTIK_PLUGIN_FILE ), $plugin_admin, 'plugin_links' );
	}

	/**
	 * Register all of the hooks related to the public-facing functionality
	 * of the plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 */
	private function define_public_hooks() {

		$plugin_public = new Hotspot_For_Mikrotik_Public( $this->get_plugin_name(), $this->get_version() );

		$this->loader->add_action( 'wp_enqueue_scripts', $plugin_public, 'enqueue_styles' );
		$this->loader->add_action( 'wp_enqueue_scripts', $plugin_public, 'enqueue_scripts' );

        /** @see Hotspot_For_Mikrotik_Public::add_routes */
        $this->loader->add_action( 'init', $plugin_public, 'add_routes' );
	}

	/**
	 * Run the loader to execute all of the hooks with WordPress.
	 *
	 * @since    1.0.0
	 */
	public function run() {
		$this->loader->run();
	}

	/**
	 * The name of the plugin used to uniquely identify it within the context of
	 * WordPress and to define internationalization functionality.
	 *
	 * @since     1.0.0
	 * @return    string    The name of the plugin.
	 */
	public function get_plugin_name() {
		return $this->plugin_name;
	}

	/**
	 * The reference to the class that orchestrates the hooks with the plugin.
	 *
	 * @since     1.0.0
	 * @return    Hotspot_For_Mikrotik_Loader    Orchestrates the hooks of the plugin.
	 */
	public function get_loader() {
		return $this->loader;
	}

	/**
	 * Retrieve the version number of the plugin.
	 *
	 * @since     1.0.0
	 * @return    string    The version number of the plugin.
	 */
	public function get_version() {
		return $this->version;
	}

}


File: /includes\class-wp-route.php
<?php
/**
 * WP_Route
 *
 * A simple class for binding
 * complex routes to functions
 * methods or WP_AJAX actions.
 *
 * @author     Anthony Budd
 */
final class WP_Route {

	private $hooked = false;

	/** @var array $reserved_names */
	protected $reserved_names;

	private $routes = array(
		'ANY'    => array(),
		'GET'    => array(),
		'POST'   => array(),
		'HEAD'   => array(),
		'PUT'    => array(),
		'DELETE' => array(),
	);

	private function __construct() {
		if ( ! function_exists( 'get_subdirectory_reserved_names' ) ) {
			require_once ABSPATH . 'wp-includes' . DIRECTORY_SEPARATOR . 'ms-functions.php';
		}
		$this->reserved_names = get_subdirectory_reserved_names();
	}

	public static function instance() {
		static $instance = null;
		if ( null === $instance ) {
			$instance = new WP_Route();
			$instance->hook();
		}
		return $instance;
	}

	// -----------------------------------------------------
	// CREATE ROUTE METHODS
	// -----------------------------------------------------
	public static function any( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'ANY', $route, $callable );
	}

	public static function get( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'GET', $route, $callable );
	}

	public static function post( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'POST', $route, $callable );
	}

	public static function head( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'HEAD', $route, $callable );
	}

	public static function put( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'PUT', $route, $callable );
	}

	public static function delete( $route, $callable ) {
		$r = self::instance();
		$r->add_route( 'DELETE', $route, $callable );
	}

	public static function match( $methods, $route, $callable ) {
		if ( ! is_array( $methods ) ) {
			throw new Exception( "\$methods must be an array" );
		}
		$r = self::instance();
		foreach ( $methods as $method ) {
			if ( ! in_array( strtoupper( $method ), array_keys( self::$routes ), true ) ) {
				throw new Exception( "Unknown method {$method}" );
			}

			$r->add_route( strtoupper( $method ), $route, $callable );
		}
	}

	public static function redirect( $route, $redirect, $code = 301 ) {
		$r = self::instance();
		$r->add_route(
			'ANY',
			$route,
			$redirect,
			array(
				'code'     => $code,
				'redirect' => $redirect,
			)
		);
	}

	// -----------------------------------------------------
	// INTERNAL UTILITY METHODS
	// -----------------------------------------------------
	private function add_route( $method, $route, $callable, $options = array() ) {
		$base_path = explode( '?', $this->tokenize( $route )[0] )[0];
		if ( in_array( $base_path, $this->reserved_names, true ) ) {
			throw new Exception( 'Route contains reserved name' );
		}
		$this->routes[ $method ][] = (object) array_merge(
			array(
				'route'    => ltrim( $route, '/' ),
				'callable' => $callable,
			),
			$options
		);

	}

	private function hook() {
		if ( ! $this->hooked ) {
			add_action( 'wp_loaded', array( 'WP_Route', 'on_init' ), 1, 0 );
			$this->hooked = true;
		}
	}

	public static function on_init() {
		$r = self::instance();
		$r->handle();
	}

	private function get_route_params( $route ) {
		$tokenized_route      = $this->tokenize( $route );
		$tokenized_request_uri = $this->tokenize( $this->requestURI() );
		preg_match_all( '/\{\s*.+?\s*\}/', $route, $matches );
		$return = array();
		foreach ( $matches[0] as $match ) {
			$search = array_search( $match, $tokenized_route );
			if ( $search !== false ) {
				$return[] = $tokenized_request_uri[ $search ];
			}
		}

		return $return;
	}

	// -----------------------------------------------------
	// GENERAL UTILITY METHODS
	// -----------------------------------------------------
	public static function routes() {
		$r = self::instance();
		return $r->routes;
	}

	public function tokenize($url) {
		return array_filter( explode( '/', ltrim($url, '/') ) );
	}

	public function requestURI() {
		return ltrim( $_SERVER['REQUEST_URI'], '/' );
	}

	// -----------------------------------------------------
	// handle()
	// -----------------------------------------------------
	public function handle() {
		$method                = strtoupper( $_SERVER['REQUEST_METHOD'] );
		$routes                = is_array($this->routes[ $method ]) ? array_merge( $this->routes[ $method ], $this->routes['ANY'] ) : null;
		$request_uri           = $this->requestURI();
		$tokenized_request_uri = $this->tokenize( $request_uri );
		$request_uri_path      = explode( '?', $this->tokenize( $request_uri )[0] )[0];

		if ( is_array( $routes ) ) {
			foreach ( $routes as $key => $route ) {
				// First, filter routes that do not have equal tokenized lengths
				if ( count( $this->tokenize( $route->route ) ) !== count( $tokenized_request_uri ) ) {
					unset( $routes[ $key ] );
					continue;
				}
				if ( $this->tokenize( $route->route )[0] !== $request_uri_path ) {
					unset( $routes[ $key ] );
					continue;
				}

				// Add more filtering here as routing gets more complex.
			}
			$routes = array_values( $routes );
			if ( isset( $routes[0] ) ) {
				$route = $routes[0];
				if ( is_string( $route->callable )
				 && class_exists( $route->callable )
				 && is_subclass_of( $route->callable, 'WP_AJAX' ) ) {
					$callable   = $route->callable;
					$controller = new $callable();
					call_user_func_array( array( $controller, 'boot' ), $this->get_route_params( $route->route ) );
					exit;
				} elseif ( isset( $routes[0]->redirect ) ) {
					$redirect = $routes[0]->redirect;
					header( "Location: {$redirect}", true, $routes[0]->code );
					wp_die();
				} else {
					call_user_func_array( $route->callable, $this->get_route_params( $route->route ) );
					exit;
				}
			}
		}
	}
}


File: /includes\index.php
<?php // Silence is golden

File: /index.php
<?php // Silence is golden

File: /LICENSE.txt
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.

File: /public\class-hotspot-for-mikrotik-public.php
<?php

/**
 * The public-facing functionality of the plugin.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/public
 */

/**
 * The public-facing functionality of the plugin.
 *
 * Defines the plugin name, version, and two examples hooks for how to
 * enqueue the public-facing stylesheet and JavaScript.
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/public
 * @author     Marius Bezuidenhout <marius dot bezuidenhout at gmail dot com>
 */
class Hotspot_For_Mikrotik_Public {

	/**
	 * The ID of this plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 * @var      string    $plugin_name    The ID of this plugin.
	 */
	private $plugin_name;

	/**
	 * The version of this plugin.
	 *
	 * @since    1.0.0
	 * @access   private
	 * @var      string    $version    The current version of this plugin.
	 */
	private $version;

	/**
	 * Initialize the class and set its properties.
	 *
	 * @since    1.0.0
	 * @param      string    $plugin_name       The name of the plugin.
	 * @param      string    $version    The version of this plugin.
	 */
	public function __construct( $plugin_name, $version ) {

		$this->plugin_name = $plugin_name;
		$this->version = $version;

	}

	/**
	 * Register the stylesheets for the public-facing side of the site.
	 *
	 * @since    1.0.0
	 */
	public function enqueue_styles() {

		/**
		 * This function is provided for demonstration purposes only.
		 *
		 * An instance of this class should be passed to the run() function
		 * defined in Hotspot_For_Mikrotik_Loader as all of the hooks are defined
		 * in that particular class.
		 *
		 * The Hotspot_For_Mikrotik_Loader will then create the relationship
		 * between the defined hooks and the functions defined in this
		 * class.
		 */

		wp_enqueue_style( $this->plugin_name, plugin_dir_url( __FILE__ ) . 'css/hotspot-for-mikrotik-public.css', array(), $this->version, 'all' );

	}

	/**
	 * Register the JavaScript for the public-facing side of the site.
	 *
	 * @since    1.0.0
	 */
	public function enqueue_scripts() {

		/**
		 * This function is provided for demonstration purposes only.
		 *
		 * An instance of this class should be passed to the run() function
		 * defined in Hotspot_For_Mikrotik_Loader as all of the hooks are defined
		 * in that particular class.
		 *
		 * The Hotspot_For_Mikrotik_Loader will then create the relationship
		 * between the defined hooks and the functions defined in this
		 * class.
		 */

		wp_enqueue_script( $this->plugin_name, plugin_dir_url( __FILE__ ) . 'js/hotspot-for-mikrotik-public.js', array( 'jquery' ), $this->version, false );

	}

    /**
     * Add routes used for event displays.
     */
    public function add_routes()
    {
        if ( ! class_exists( 'WP_Route' ) ) {
            require_once plugin_dir_path( __DIR__ ) . 'includes' . DIRECTORY_SEPARATOR . 'class-wp-route.php';
        }

        WP_Route::any( 'mikrotik/login', array( $this, 'get_login_page' ) );
    }

    /**
     * Usage: ://<server>/mikrotik/login
     *
     * @throws Exception
     */
    public function get_login_page()
    {
        $defaults = array(
            'username'   => '',
            'error'      => '',
            'trial'      => 'no'
        );
        wp_register_style( 'mikrotik',  plugin_dir_url( __FILE__ ) . 'css/mikrotik.css', array(), $this->version, 'all' );
        wp_register_script( 'mikrotik-md5', plugin_dir_url( __FILE__ ) . 'js/mikrotik-md5.js', array(), $this->version, false );
	    $args = wp_parse_args( sanitize_post( $_REQUEST  ), $defaults );  // phpcs:ignore WordPress.Security.NonceVerification
        include plugin_dir_path( __DIR__ ) . 'templates' . DIRECTORY_SEPARATOR . 'login.php';
    }
}


File: /public\css\hotspot-for-mikrotik-public.css
/**
 * All of the CSS for your public-facing functionality should be
 * included in this file.
 */

File: /public\css\mikrotik.css
a,body,div,form,html,img,input,label,p,span {
	margin:0;padding:0;border:0;font-family:sans-serif,Arial
}
body,html {
	min-height:100%;overflow-x:hidden
}
html {
	background: url(/wp-content/plugins/hotspot-for-mikrotik/assets/img/bg.jpg) no-repeat center center fixed;
	-webkit-background-size: cover;
	-moz-background-size: cover;
	-o-background-size: cover;
	background-size: cover;
}
a {
	color:#486173
}
input,label {
	vertical-align:middle;white-space:normal;background:0 0;line-height:1
}
label {
	position:relative;display:block
}
p::first-letter {
	text-transform:uppercase
}
.main {
	min-height:calc(100vh - 90px);width:100%;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column
}
.ie-fixMinHeight {
	display:-webkit-box;display:-ms-flexbox;display:flex
}
.ico {
	height:16px;position:absolute;top:0;left:0;margin-top:13px;margin-left:14px
}
.logo {
	max-width:200px;display:block;margin:0 auto 30px auto
}
.logo * {
	fill:#fff
}
.lite .logo * {
	fill:#444
}
h1 {
	text-align:center;color:#fff;font-size:24px!important
}
* {
	-webkit-box-sizing:border-box;box-sizing:border-box;font-size:16px
}
.wrap {
	margin:auto;padding:40px;-webkit-transition:width .3s ease-in-out;transition:width .3s ease-in-out
}
@media only screen and (min-width:1px) and (max-width:575px) {
	.wrap {
		width:100%
	}
}
form {
	width:100%;margin-bottom:20px
}
@-webkit-keyframes fadeIn {
	from {
		opacity:0
	}
	to {
		opacity:1
	}
}
@keyframes fadeIn {
	from {
		opacity:0
	}
	to {
		opacity:1
	}
}
.fadeIn {
	-webkit-animation-name:fadeIn;animation-name:fadeIn
}
.animated {
	-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-fill-mode:both;animation-fill-mode:both
}
.info {
	color:#fff;text-align:center;margin-bottom:30px
}
input {
	outline:0;-webkit-appearance:none;-moz-appearance:none;appearance:none
}
input:focus {
	outline:0
}
input[type=password],input[type=text] {
	width:100%;border:1px solid background-color: rgba(255,255,255,.8);height:44px;padding:3px 20px 3px 40px;margin-bottom:20px;border-radius:6px;background-color:rgba(255,255,255,.8);-webkit-transition:-webkit-box-shadow .3s ease-in-out;transition:-webkit-box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out,-webkit-box-shadow .3s ease-in-out
}
input[type=password]:focus,input[type=text]:focus {
	-webkit-box-shadow:0 0 5px 0 rgba(255,255,255,1);box-shadow:0 0 5px 0 rgba(255,255,255,1)
}
.bt {
	opacity:.4
}
input[type=submit] {
	background:#3e4d59;color:#fff;border:0;cursor:pointer;text-align:center;width:100%;height:44px;border-radius:6px;-webkit-transition:background .3s ease-in-out;transition:background .3s ease-in-out
}
input[type=submit]:focus,input[type=submit]:hover {
	background:#33404a
}
table {
	border-collapse:collapse;width:100%;margin-bottom:20px
}
table td{
	color:#fff;border-bottom:1px solid #e6e6e6;padding:10px 4px 10px 0
}
table td:first-child {
	font-weight:700
}
.lite {
	background:#fff
}
.lite input[type=password],.lite input[type=text] {
	border:1px solid #c3c3c3
}
.lite .info,.lite h1,.lite table td {
	color:#444
}
.lite input[type=password]:focus,.lite input[type=text]:focus {
	-webkit-box-shadow:0 0 5px 0 rgba(62,77,89,.2);box-shadow:0 0 5px 0 rgba(62,77,89,.2)
}
.dark {
	background:#343434
}
.dark input[type=submit] {
	background:#dc3a41
}
.dark input[type=submit]:focus,.dark input[type=submit]:hover {
	background:#b92f35
}
.dark input[type=password],.dark input[type=text] {
	background-color:#fff
}
.dark a {
	color:#dc3a41
}
.dark table td {
	border-bottom:1px solid #505050
}
.info.alert {
	color:#da3d41
}

@media (min-width:576px) {
	.wrap {
		width:410px
	}
	* {
		font-size:14px!important
	}
}

File: /public\index.php
<?php // Silence is golden

File: /public\js\hotspot-for-mikrotik-public.js
(function( $ ) {
	'use strict';

	/**
	 * All of the code for your public-facing JavaScript source
	 * should reside in this file.
	 *
	 * Note: It has been assumed you will write jQuery code here, so the
	 * $ function reference has been prepared for usage within the scope
	 * of this function.
	 *
	 * This enables you to define handlers, for when the DOM is ready:
	 *
	 * $(function() {
	 *
	 * });
	 *
	 * When the window is loaded:
	 *
	 * $( window ).load(function() {
	 *
	 * });
	 *
	 * ...and/or other possibilities.
	 *
	 * Ideally, it is not considered best practise to attach more than a
	 * single DOM-ready or window-load handler for a particular page.
	 * Although scripts in the WordPress core, Plugins and Themes may be
	 * practising this, we should strive to set a better example in our own work.
	 */

})( jQuery );


File: /public\js\mikrotik-md5.js
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


File: /public\partials\hotspot-for-mikrotik-public-display.php
<?php

/**
 * Provide a public-facing view for the plugin
 *
 * This file is used to markup the public-facing aspects of the plugin.
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 * @subpackage Hotspot_For_Mikrotik/public/partials
 */
?>

<!-- This file should primarily consist of HTML with a little bit of PHP. -->


File: /README.txt
=== Plugin Name ===
Contributors: (this should be a list of wordpress.org userid's)
Donate link: https://profiles.wordpress.org/mbezuidenhout/
Tags: comments, spam
Requires at least: 3.0.1
Tested up to: 3.4
Stable tag: 4.3
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

Here is a short description of the plugin.  This should be no more than 150 characters.  No markup here.

== Description ==

This is the long description.  No limit, and you can use Markdown (as well as in the following sections).

For backwards compatibility, if this section is missing, the full length of the short description will be used, and
Markdown parsed.

A few notes about the sections above:

*   "Contributors" is a comma separated list of wp.org/wp-plugins.org usernames
*   "Tags" is a comma separated list of tags that apply to the plugin
*   "Requires at least" is the lowest version that the plugin will work on
*   "Tested up to" is the highest version that you've *successfully used to test the plugin*. Note that it might work on
higher versions... this is just the highest one you've verified.
*   Stable tag should indicate the Subversion "tag" of the latest stable version, or "trunk," if you use `/trunk/` for
stable.

    Note that the `readme.txt` of the stable tag is the one that is considered the defining one for the plugin, so
if the `/trunk/readme.txt` file says that the stable tag is `4.3`, then it is `/tags/4.3/readme.txt` that'll be used
for displaying information about the plugin.  In this situation, the only thing considered from the trunk `readme.txt`
is the stable tag pointer.  Thus, if you develop in trunk, you can update the trunk `readme.txt` to reflect changes in
your in-development version, without having that information incorrectly disclosed about the current stable version
that lacks those changes -- as long as the trunk's `readme.txt` points to the correct stable tag.

    If no stable tag is provided, it is assumed that trunk is stable, but you should specify "trunk" if that's where
you put the stable version, in order to eliminate any doubt.

== Installation ==

This section describes how to install the plugin and get it working.

e.g.

1. Upload `hotspot-for-mikrotik.php` to the `/wp-content/plugins/` directory
1. Activate the plugin through the 'Plugins' menu in WordPress
1. Place `<?php do_action('plugin_name_hook'); ?>` in your templates

== Frequently Asked Questions ==

= A question that someone might have =

An answer to that question.

= What about foo bar? =

Answer to foo bar dilemma.

== Screenshots ==

1. This screen shot description corresponds to screenshot-1.(png|jpg|jpeg|gif). Note that the screenshot is taken from
the /assets directory or the directory that contains the stable readme.txt (tags or trunk). Screenshots in the /assets
directory take precedence. For example, `/assets/screenshot-1.png` would win over `/tags/4.3/screenshot-1.png`
(or jpg, jpeg, gif).
2. This is the second screen shot

== Changelog ==

= 1.0 =
* A change since the previous version.
* Another change.

= 0.5 =
* List versions from most recent at top to oldest at bottom.

== Upgrade Notice ==

= 1.0 =
Upgrade notices describe the reason a user should upgrade.  No more than 300 characters.

= 0.5 =
This version fixes a security related bug.  Upgrade immediately.

== Arbitrary section ==

You may provide arbitrary sections, in the same format as the ones above.  This may be of use for extremely complicated
plugins where more information needs to be conveyed that doesn't fit into the categories of "description" or
"installation."  Arbitrary sections will be shown below the built-in sections outlined above.

== A brief Markdown Example ==

Ordered list:

1. Some feature
1. Another feature
1. Something else about the plugin

Unordered list:

* something
* something else
* third thing

Here's a link to [WordPress](http://wordpress.org/ "Your favorite software") and one to [Markdown's Syntax Documentation][markdown syntax].
Titles are optional, naturally.

[markdown syntax]: http://daringfireball.net/projects/markdown/syntax
            "Markdown is what the parser uses to process much of the readme file"

Markdown uses email style notation for blockquotes and I've been told:
> Asterisks for *emphasis*. Double it up  for **strong**.

`<?php code(); // goes in backticks ?>`

File: /templates\login.php
<?php
//echo phpinfo();
wp_enqueue_script( 'mikrotik-md5' );
wp_enqueue_style( 'mikrotik' );
?>
<!doctype html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<meta http-equiv="pragma" content="no-cache" />
	<meta http-equiv="expires" content="-1" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Internet hotspot - Log in</title>
	<?php
	$styles = wp_print_styles();
	$scripts = wp_print_scripts();
	?>
</head>

<body>

<!-- two other colors

<body class="lite">
<body class="dark">

-->

<?php
if($args['chap-id']):
?>
<form name="sendin" action="<?php echo $args['link-login-only'] ?>" method="post" style="display:none">
	<input type="hidden" name="username" />
	<input type="hidden" name="password" />
	<input type="hidden" name="dst" value="<?php echo urldecode($args['link-orig-esc']) ?>" />
	<input type="hidden" name="popup" value="true" />
</form>

<script>
	function doLogin() {
		document.sendin.username.value = document.login.username.value;
		document.sendin.password.value = hexMD5('<?php echo $args['chap-id'] ?>' + document.login.password.value + '<?php echo $args['chap-challenge'] ?>');
		document.sendin.submit();
		return false;
	}

</script>
<?php
endif;
?>
<div class="ie-fixMinHeight">
	<div class="main">
		<div class="wrap animated fadeIn">
			<form name="login" action="<?php echo $args['link-login-only'] ?>" method="post" <?php if($args['chap-id']) { echo 'onSubmit="return doLogin()"'; } ?>>
				<input type="hidden" name="dst" value="<?php echo urldecode($args['link-orig-esc']) ?>" />
				<input type="hidden" name="popup" value="true" />
				<svg class="logo" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 174 42">
					<path fill="#fff" d="M7.32 13.66L0 41.74 3.12 41.74 9.49 15.94 9.58 15.94 15.01 41.74 18.22 41.74 36.86 16.34 36.95 16.34 30.02 41.74 33.18 41.74 40.4 13.66 35.73 13.66 17.23 38.87 11.99 13.66 7.32 13.66zM43.43 21.45L38.19 41.74 41.16 41.74 46.4 21.45 43.43 21.45zM50.68 21.45L45.5 41.74 48.47 41.74 50.36 34.39 55.55 30.77 62.02 41.74 65.27 41.74 57.91 29.28 69.43 21.45 65.46 21.45 51.21 31.36 51.12 31.28 53.66 21.45 50.68 21.45z" />
					<path d="M71.18 21.45L65.94 41.74h3l2.74-10.62c1-3.81 3.82-7.39 9.16-7.47.56 0 1.13 0 1.7 0l.66-2.48c-.52 0-1.09 0-1.61 0-4.34 0-6.94 2-8.82 5h-.1l1.23-4.68zM103.8 28.8c0-5-4-7.94-9.63-7.94-8.69 0-13.59 6.37-13.59 13 0 5.07 3.44 8.45 9.72 8.45 9 0 13.5-6.68 13.5-13.53m-3 .52c0 4.72-3.44 10.93-9.95 10.93-5 0-7.32-2.68-7.32-6.61 0-4.76 3.59-10.7 10.1-10.7 4.77 0 7.17 2.6 7.17 6.38M132.33 21.43L134.26 13.66 105.19 13.66 103.27 21.45 112.59 21.45 112.59 21.45 122.99 21.45 122.99 21.45 132.33 21.43zM111.67 25.17L107.55 41.74 117.93 41.74 122.06 25.17 122.06 25.16 111.67 25.16 111.67 25.17zM134 25.17l-4.11 16.57h9.35l4.1-16.57zm10.28-3.73l1.94-7.78h-9.34l-2 7.79zM150.09 13.66L143.11 41.74 152.45 41.74 153.91 35.92 156.04 34.34 159.34 41.74 169.49 41.74 163.26 29.55 174.26 21.33 163.07 21.33 156.18 27.3 156.09 27.3 159.44 13.66 150.09 13.66zM47.45 0c1.14 7.93 5.39 12.74 14.07 13.14A10.69 10.69 0 0 1 47.45 0" fill="#fff" fill-rule="evenodd" />
					<path d="M42.91,1.4c.1,0,.11,0,.12.11A16.55,16.55,0,0,0,48.26,13a16.6,16.6,0,0,0,12,4.66c-10,4-20.55-5.6-17.33-16.28" fill="#fff" fill-rule="evenodd" /></svg>


				<p class="info <?php if($args['error']) { echo 'alert'; } ?>">
                    <?php
                    if($args['error'] == "") {
                        echo 'Please log in to use the internet hotspot service ';
                        if($args['trial'] == 'yes') {
	                        $trail_url = $args['link-login-only'] . '?dst=' . $args['link-orig-esc'] . '&amp;username=T-' . $args['mac-esc'];
                            echo '<br />Free trial available, <a href="' . $trail_url . '">click here</a>.';
                        }
					}

					if ( $args['error'] ) {
					    echo $args['error'];
					}
					?>
				</p>
				<label>
					<img class="ico" src="<?php echo plugin_dir_url( __DIR__ ) . 'assets/img/user.svg' ?>" alt="#" />
					<input name="username" type="text" value="<?php echo $args['username']; ?>" placeholder="Username" />
				</label>

				<label>
					<img class="ico" src="<?php echo plugin_dir_url( __DIR__ ) . 'assets/img/password.svg' ?>" alt="#" />
					<input name="password" type="password" placeholder="Password" />
				</label>

				<input type="submit" value="Connect" />

			</form>
		</div>
	</div>
</div>
</body>

</html>

File: /templates\router\login.html
<html lang="en">
<head><title>…</title></head>
<body>
$(if chap-id)
<noscript>
<b>JavaScript required. Please enable JavaScript to continue.</b>
</noscript>
$(endif)
If you are not redirected within a few seconds please click on continue below<br>
<form name="redirect" action="https://blackhorse.co.za/mikrotik/login" method="get">
    <input type="hidden" name="mac" value="$(mac)">
    <input type="hidden" name="trial" value="$(trial)">
    <input type="hidden" name="hostname" value="$(hostname)">
    <input type="hidden" name="server-address" value="$(server-address)">
    <input type="hidden" name="plain-passwd" value="$(plain-passwd)">
    <input type="hidden" name="ssl-login" value="$(ssl-login)">
    <input type="hidden" name="username" value="$(username)">
    <input type="hidden" name="url" value="$(link-login)">
    <input type="hidden" name="link-orig" value="$(link-orig)">
    <input type="hidden" name="error" value="$(error)">
    <input type="hidden" name="chap-id" value="$(chap-id)">
    <input type="hidden" name="chap-challenge" value="$(chap-challenge)">
    <input type="hidden" name="link-login-only" value="$(link-login-only)">
    <input type="hidden" name="link-orig-esc" value="$(link-orig-esc)">
    <input type="hidden" name="mac-esc" value="$(mac-esc)">
    <input type="hidden" name="ip" value="$(ip)">
    <input type="submit" value="continue">
</form>
<script>
<!--
  document.redirect.submit();
//-->
</script>
</body>
</html>


File: /uninstall.php
<?php

/**
 * Fired when the plugin is uninstalled.
 *
 * When populating this file, consider the following flow
 * of control:
 *
 * - This method should be static
 * - Check if the $_REQUEST content actually is the plugin name
 * - Run an admin referrer check to make sure it goes through authentication
 * - Verify the output of $_GET makes sense
 * - Repeat with other user roles. Best directly by using the links/query string parameters.
 * - Repeat things for multisite. Once for a single site in the network, once sitewide.
 *
 * This file may be updated more in future version of the Boilerplate; however, this is the
 * general skeleton and outline for how the file should work.
 *
 * For more information, see the following discussion:
 * https://github.com/tommcfarlin/WordPress-Plugin-Boilerplate/pull/123#issuecomment-28541913
 *
 * @link       https://profiles.wordpress.org/mbezuidenhout/
 * @since      1.0.0
 *
 * @package    Hotspot_For_Mikrotik
 */

// If uninstall not called from WordPress, then exit.
if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
	exit;
}


