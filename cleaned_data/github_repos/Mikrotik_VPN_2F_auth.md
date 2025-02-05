# Repository Information
Name: Mikrotik_VPN_2F_auth

# Directory Structure
Directory structure:
└── github_repos/Mikrotik_VPN_2F_auth/
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
    │   │       ├── pack-20b6c7be554ae793559bc4080f493337c93560a8.idx
    │   │       └── pack-20b6c7be554ae793559bc4080f493337c93560a8.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── class/
    │   ├── index.php
    │   ├── lib/
    │   │   ├── http_response.class.php
    │   │   ├── MikroTik_2FAuth.class.php
    │   │   └── routeros_api.class.php
    │   ├── log/
    │   └── templates/
    │       └── success.php
    ├── function/
    │   └── index.php
    ├── LICENSE
    ├── mtvpn.rsc
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
	url = https://github.com/dagababaev/Mikrotik_VPN_2F_auth.git
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
0000000000000000000000000000000000000000 da1884bdaf7604f3acc7b26c2241330740ed37e5 vivek-dodia <vivek.dodia@icloud.com> 1738606025 -0500	clone: from https://github.com/dagababaev/Mikrotik_VPN_2F_auth.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 da1884bdaf7604f3acc7b26c2241330740ed37e5 vivek-dodia <vivek.dodia@icloud.com> 1738606025 -0500	clone: from https://github.com/dagababaev/Mikrotik_VPN_2F_auth.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 da1884bdaf7604f3acc7b26c2241330740ed37e5 vivek-dodia <vivek.dodia@icloud.com> 1738606025 -0500	clone: from https://github.com/dagababaev/Mikrotik_VPN_2F_auth.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
da1884bdaf7604f3acc7b26c2241330740ed37e5 refs/remotes/origin/master


File: /.git\refs\heads\master
da1884bdaf7604f3acc7b26c2241330740ed37e5


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /class\index.php
<?php
// ------------------------------------------------------------------------------
//  © Copyright (с) 2020
//  Author: Dmitri Agababaev, d.agababaev@duncat.net
//
//  Redistributions and use of source code, with or without modification, are
//  permitted that retain the above copyright notice
//
//  License: MIT
// ------------------------------------------------------------------------------

define('TELEGRAM_BOT_TOKEN', '1100052127:YER5vFiH0krj-BWN16optAycNH7hn8gne0s');
define('SYNOLOGY_WEBHOOK_URL', 'https://yourwebsite.com:5001/webapi/entry.cgi?api=SYNO.Chat.External&method=incoming&version=2&token=');
define('LOG_FILEPATH', 'log/MikroTik_2FAuth.log');

require_once('lib/http_response.class.php');
require_once('lib/routeros_api.class.php');
require_once('lib/MikroTik_2FAuth.class.php');

// Routers data array used as vpn-servers
$ruid_array = [
    '#ROUTERLOGIN#' => [
        'mdpass' => 'e5753db3df39fc52ec1490bbb5e83981',
        'ip' => '10.0.0.1',
        'login' => '#ROSAPI_LOGIN#',
        'password' => '#ROSAPI_PASS#',
        'smsgw' => ['SMS_gw1']
    ]
];
// Routers data array will be used to send auth sms
$SMS_gateways = [
    'SMS_gw1' => [
        'ip' => '10.0.0.1',
        'login' => '#ROSAPI_LOGIN#',
        'password' => '#ROSAPI_PASS#',
        'port' => '#USB_PORT#',
        'channel' => '#USB_CHANNEL#']
];

// All used parameters
$param = [
    'ruid' => @$_REQUEST['ruid'],
    'pass' => @$_REQUEST['pass'],
    'username' => @$_REQUEST['username'],
    'connection_type' => @$_REQUEST['connection_type'],
    'code' => @$_REQUEST['code'],
    'Telegram_botToken' => TELEGRAM_BOT_TOKEN,
    'Synology_WebhookURL' => SYNOLOGY_WEBHOOK_URL,
    'Telegram_chatid' => @$_REQUEST['telegram'],
    'Synology_chatToken' => @$_REQUEST['synology'],
    'phone' => @$_REQUEST['phone'],
    'savelog' => true, # true / false
    'log_filepath' => LOG_FILEPATH
];

$mtauth = new MikroTik_2FAuth($ruid_array, $param, $SMS_gateways);
print($mtauth->start());

?>


File: /class\lib\http_response.class.php
<?php
// ------------------------------------------------------------------------------
//  © Copyright (с) 2020
//  Author: Dmitri Agababaev, d.agababaev@duncat.net
//
//  Redistributions and use of source code, with or without modification, are
//  permitted that retain the above copyright notice
//
//  License: MIT
// ------------------------------------------------------------------------------

class http_response
{
    public static function set($code, $data = null) {
        $message = ['success' => $data['success']];
        switch ($code) {
            case 200: header('HTTP/1.1 200 OK'); break;
            case 201: header('HTTP/1.1 201 Created'); break;
            case 202: header('HTTP/1.1 202 Accepted'); break;
            case 204: header('HTTP/1.1 204 No Content'); break;

            case 400: header('HTTP/1.1 400 Bad Request');
                $message['error_code'] = 400;
                $message['error_message'] = 'Bad Request';
                break;
            case 401: header('HTTP/1.1 401 Unauthorized');
                $message['error_code'] = 401;
                $message['error_message'] = 'Unauthorized';
                break;
            case 403: header('HTTP/1.1 403 Forbidden');
                $message['error_code'] = 403;
                $message['error_message'] = 'Forbidden';
                break;
            case 404: header('HTTP/1.1 404 Not Found');
                $message['error_code'] = 404;
                $message['error_message'] = 'Not Found';
                break;
            case 406: header('HTTP/1.1 406 Not Acceptable');
                $message['error_code'] = 406;
                $message['error_message'] = 'Not Acceptable';
                break;
        }
        if(isset($data['description'])) $message['description'] = $data['description'];
        die(json_encode($message));
    }
}


File: /class\lib\MikroTik_2FAuth.class.php
<?php
// ------------------------------------------------------------------------------
//  © Copyright (с) 2020
//  Author: Dmitri Agababaev, d.agababaev@duncat.net
//
//  Redistributions and use of source code, with or without modification, are
//  permitted that retain the above copyright notice
//
//  License: MIT
// ------------------------------------------------------------------------------

class MikroTik_2FAuth
{
    protected $ROSAPI;
    protected $http_header;
    protected $host;

    protected $savelog = false;
    protected $log_array = [];
    protected $log_filepath;
    protected $ruid_array = [];
    protected $SMS_gateways;

    protected $username;
    protected $Telegram_botToken;
    protected $Telegram_chatid;
    protected $Synology_WebhookURL;
    protected $Synology_chatToken;
    protected $phone;
    protected $connection_type;

    protected $ruid;
    public $code;

    /*
     * $param = [
     *   'ruid' => @$_REQUEST['ruid'],
     *   'pass' => @$_REQUEST['pass'],
     *   'username' => @$_REQUEST['username'],
     *   'connection_type' => @$_REQUEST['connection_type'],
     *   'code' => @$_REQUEST['code'],
     *   'Telegram_botToken' => TELEGRAM_BOT_TOKEN,
     *   'Synology_WebhookURL' => SYNOLOGY_WEBHOOK_URL,
     *   'Telegram_chatid' => @$_REQUEST['telegram'],
     *   'Synology_chatToken' => @$_REQUEST['synology'],
     *   'phone' => @$_REQUEST['phone'],
     *   'savelog' => true, # true / false
     *   'log_filepath' => 'log/MikroTik_2FAuth.log'
     *   ];
     */
    public function __construct ($ruid_array, $param, $SMS_gateways = null)
    {
        $this->ROSAPI = new RouterosAPI();
        if (!$this->ROSAPI)
            http_response::set(200, ["success" => false, "description" => "RouterOS API Object required!"]);

        if (!$_REQUEST) http_response::set(404, ["success" => false, "description" => "Request is empty"]);
        $this->ruid_array = $ruid_array;

        // check ruid
        if (!isset($param['ruid']))
            http_response::set(400, ["success" => false, "description" => "Router id required"]);
        if (!array_key_exists($param['ruid'], $this->ruid_array))
            http_response::set(404, ["success" => false, "description" => "Router can't found"]);
        $this->ruid = $param['ruid'];

        $this->connection_type = $param['connection_type'];

        // check ruid password
        if ($this->connection_type == 'open') {
            if (!isset($param['pass']) || md5($param['pass']) != $this->ruid_array[$this->ruid]['mdpass'])
                http_response::set(403, ["success" => false]);
        }

        $this->code = @$param['code'];

        $this->username = $param['username'];
        $this->Telegram_botToken   = @$param['Telegram_botToken'];
        $this->Synology_WebhookURL = @$param['Synology_WebhookURL'];
        $this->Telegram_chatid     = @$param['Telegram_chatid'];
        $this->Synology_chatToken  = @$param['Synology_chatToken'];
        $this->phone               = @$param['phone'];

        $this->savelog = @$param['savelog'];
        $this->log_filepath = @$param['log_filepath'];

        $this->SMS_gateways = $SMS_gateways ? $SMS_gateways: false;

        $protocol = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] != 'off') ? 'https://' : 'http://';
        $this->host = $protocol.$_SERVER['HTTP_HOST'].$_SERVER['SCRIPT_NAME'];
    }

    public function start()
    {
        static $result;
        switch ($this->connection_type) {
            case 'open':
                $this->firewall();
                $result = $this->sendCode();
                break;
            case 'auth':
                if($this->doAuth()) $result = $this->renderTemplate('success.php');
                break;
            case 'close':
                break;
            default: http_response::set(404, ["success" => false, "description" => "Unknown connection type"]);
        }

        $this->writelog($this->connection_type);
        return $result;
    }

    public function doAuth()
    {
        $ruid = $this->ruid_array[$this->ruid];
        $ROSAPI = $this->ROSAPI;

        if ($ROSAPI->connect($ruid['ip'], $ruid['login'], $ruid['password'])) {
            // if connected successfully - sending command
            $ROSAPI->write('/ip/firewall/address-list/print', false);
            $ROSAPI->write('?comment='.$this->code, false);
            $ROSAPI->write('=.proplist=.id');
            // get response
            $response = $ROSAPI->read();
            // If no record in firewall address_list – reset
            if (!$response[0]) {
                $ROSAPI->disconnect();
                return false;
            };
            // delete firewall address-list
            $ROSAPI->write('/ip/firewall/address-list/remove', false);
            $ROSAPI->write('=.id=' . $response[0]['.id']);
            $ROSAPI->read();
        } else {
            http_response::set(200, ["success" => false, "description" => "Can't connect to router {$this->ruid}"]);
        }
        $ROSAPI->disconnect();
        return true;
    }

    public function sendCode()
    {
        $this->code = $this->genCode();
        $message = "To authorize user {$this->username} connection open {$this->host}?ruid={$this->ruid}&code={$this->code}&connection_type=auth";
        static $result;

        if ($this->Telegram_chatid) {
            $result = $this->Telegram($message);
        } elseif ($this->Synology_chatToken) {
            $result = $this->Synology($message);
        } elseif ($this->phone) {
            $result = $this->SMS($message);
        } else {
            http_response::set(404, ["success" => false, "description" => "Unknown auth method"]);
        }
        if ($result === true) {
            return $this->code;
        } else {
            http_response::set(404, ["success" => false, "description" => $result]);
        }
        return false;
    }

    public function POST($url, $message, $type = null)
    {
        switch ($type) {
            case 'json': $header[] = 'Content-Type: application/json'; break;
            default: $header[] = 'Content-Type: application/x-www-form-urlencoded';
        }

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $message);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $output = curl_exec ($ch);
        curl_close ($ch);

        return $output;
    }

    public function Telegram($message)
    {
        if(!$this->Telegram_botToken) http_response::set(404, ["success" => false, "description" => "Telegram_botToken required in param!"]);

        $url = 'https://api.telegram.org/bot'.$this->Telegram_botToken.'/sendMessage';
        $content = '{"chat_id":"'.$this->Telegram_chatid.'", "text": "'.$message.'"}';
        $result = json_decode($this->POST($url, $content, 'json'));
        if ($result->ok !== true) http_response::set(200, ["success" => false, "description" => $result]);
        return true;
    }

    public function Synology($message)
    {
        if(!$this->Synology_WebhookURL) http_response::set(404, ["success" => false, "description" => "Synology_WebhookURL required in param!"]);

        $url = $this->Synology_WebhookURL.urlencode($this->Synology_chatToken);
        $content = 'payload='.urlencode('{"text": "'.$message.'"}');
        $result = json_decode($this->POST($url, $content));
        if ($result->success !== true) http_response::set(200, ["success" => false, "description" => $result]);
        return true;
    }

    public function SMS($message) {

        $ruid = $this->ruid_array[$this->ruid];
        $modem = $ruid['smsgw'][array_rand($ruid['smsgw'], 1)];

        $gateway = $this->SMS_gateways[$modem];
        $ROSAPI = $this->ROSAPI;

        // if connected successfully - sending message
        if ($ROSAPI->connect($gateway['ip'], $gateway['login'], $gateway['password'])) {
            // SMS send command
            $ARRAY = $ROSAPI->comm("/tool/sms/send", array(
                "port"=>$gateway['port'],
                "channel"=>$gateway['channel'],
                "phone-number"=>$this->phone,
                "message"=>$message,));
            // Checking if send failed and error message return, will make usb power-reset to restart modem
            if(isset($ARRAY['!trap'])) {
                $ROSAPI->comm("/system/routerboard/usb/power-reset");
                $error = json_encode(["success" => "false", "message" => $ARRAY['!trap'][0]['message']]);
                $ROSAPI->disconnect();
                return $error;
        }
        $ROSAPI->disconnect();
        } else {
            $error = json_encode(["success" => "false", "message" => "Can't connect to {$modem}"]);
            return $error;
        }
        return true;
    }

    public function genCode() {
        $str = 'abcdefghijklmnopqrstuvwzyz';
        $str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $str2 = '0123456789';
        $str3 = '()/\_-+';

        $shuffled = str_shuffle($str);
        $shuffled1 = str_shuffle($str1);
        $shuffled2 = str_shuffle($str2);
        $shuffled3 = str_shuffle($str3);

        $total = $shuffled.$shuffled1.$shuffled2.$shuffled3;
        $shuffled_final = str_shuffle($total);
        $result= substr($shuffled_final, 0, 5);

        return $result;
    }

    public function firewall() {
        foreach ($this->ruid_array as $value) {
            $result = (in_array($_SERVER['REMOTE_ADDR'], $value) === true) ? true : false;
            if($result) return true; // if found record – break
        }
        $this->writelog('FIREWALL BLOCKED IP: '.$_SERVER['REMOTE_ADDR']);
        http_response::set(403, ["success" => false, "description" => "Firewall: not allow access for IP {$_SERVER['REMOTE_ADDR']}"]);
        return false;
    }

    private function writelog($msg) {
        if (!$this->savelog) return false;
        $fp = "\nTime = " . date("Y-m-d H:i:s")."\n";
        $fp .= $msg."\n";
        $fp .= print_r($_REQUEST, true);
        if(file_put_contents($this->log_filepath, $fp, FILE_APPEND | LOCK_EX))  {
            return true;
        } else {
            return false;
        }
    }

    private function renderTemplate($page, $item = null) {

        $content = $page;
        if (file_exists('templates/'.$page)) $content = file_get_contents('templates/'.$page);
        foreach ($item as $key => $value) {
            $content = str_replace('<?=$item[\''.$key.'\'];?>', $value, $content);
        }
        return $content;
    }
}


File: /class\lib\routeros_api.class.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 3;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    public function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $ip.':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login', false);
                $this->write('=name=' . $login, false);
                $this->write('=password=' . $password);
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0])) {
                    if ($RESPONSE[0] == '!done') {
                        if (!isset($RESPONSE[1])) {
                            // Login method post-v6.43
                            $this->connected = true;
                            break;
                        } else {
                            // Login method pre-v6.43
                            $MATCHES = array();
                            if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                                if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                                    $this->write('/login', false);
                                    $this->write('=name=' . $login, false);
                                    $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                                    $RESPONSE = $this->read(false);
                                    if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                        $this->connected = true;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


File: /class\templates\success.php
<!DOCTYPE html>
      <html lang="ru">
      <meta http-equiv="Content-Type" content="charset=utf-8" />
      <body style="font-family: Verdana, Arial, Helvetica, sans-serif; background-color: #282c34; color: #fff; height: 100vh; display: flex;">
        <div style="margin: auto; max-width: 50%;">
          <p style="font-size: 24pt; font-weight: bold; margin: 0 0 10px;">
    VPN-соединение установлено, можете продолжить работу<br />
          </p>
          <p style="font-size: 12pt; color: #aaa;">
    В случае недоступности сервисов обратитесь к вашему системному администратору<br />
          </p>
          <p style="font-size: 24pt; font-weight: bold; margin: 100px 0 10px;">
    VPN connection is established, you can continue to work
</p>
          <p style="font-size: 12pt; color: #aaa;">
            If any services unavalible you must contact with your system administrator<br />
          </p>
        </div>
      </body>
      </html>

File: /function\index.php
<?php

// ------------------------------------------------------------------------------
//  © Copyright (с) 2020
//  Author: Dmitri Agababaev, d.agababaev@duncat.net
//
//  Copyright by authors for used RouterOS PHP API class in the source code files
//
//  Redistributions and use of source code, with or without modification, are
//  permitted that retain the above copyright notice
//
//  License: MIT
// ------------------------------------------------------------------------------

define('TELEGRAM_BOT_TOKEN', '1100052127:YER5vFiH0krj-BWN16optAycNH7hn8gne0s');
define('SYNOLOGY_WEBHOOK_URL', 'https://yourwebsite.com:5001/webapi/entry.cgi?api=SYNO.Chat.External&method=incoming&version=2&token=');
define('LOG_FILEPATH', 'mt2Fvpn.log'); // Log file path
define('HOST', 'https://yourwebsite.com/'); // Full address that this script awalible


require_once('routeros_api.class.php');
// https://github.com/BenMenking/routeros-api

// -------------------------
// Base settings
// -------------------------
$firewall = true; // Firewall - allow access to send SMS only for router from array $ruid_data. Use? true | false
$uselog = true; // Use log? true | false

// Routers data array used as vpn-servers
$ruid_data = array(
    // password in md5, global ip-address, mikrotik login, password, SMS-gateway-key will be use to send sms
    '#ROUTERLOGIN#' => array('mdpass' => '#ROUTER_MD5_PASSWORD#',
                          'ip' => 'XXX.XXX.X.X',
                          'login' => '#ROSAPI_LOGIN#',
                          'password' => '#PASSWORD#',
                          'smsgw' => array(
                                           // If you want send SMS randomly from any SMS-gateways, add one here (low modem load)
                                           0 => 'SMS_gw1')
                          )
    );

// Routers data array will be used to send autherization sms
$SMS_gateway = array(
    // ip-address (global or local if used in one local network with server), login, password, USB-modem port, USB-modem channel
    'SMS_gw1' => array('ip' => 'XXX.XXX.X.X', 'login' => '#ROSAPI_LOGIN#', 'password' => '#PASSWORD#', 'port' => '#USB_PORT#', 'channel' => '#USB_CHANNEL#')
    );


// ----------------
// Input data check
// ----------------
if (!$_REQUEST) die(header('HTTP/1.0 406 Not Acceptable')); // if request free - reset
if (!$_REQUEST['ruid']) die(header('HTTP/1.0 406 Not Acceptable')); // if ruid not isset – reset
if (!array_key_exists($_REQUEST['ruid'], $ruid_data)) die(header('HTTP/1.0 406 Not Acceptable')); // if router does not exist – reset
if ($_REQUEST['auth']) autorize(); // if auth request allow without password
if (!ruid_auth()) die(header('HTTP/1.0 401 Unauthorized')); // check ruid password
if (@$_REQUEST['action'] == 'down') { // if vpn-connection closed
  writelog('CONNECTION CLOSED');
  die(header('HTTP/1.0 200 ОК'));
}
if (isset($_REQUEST['phone']) || isset($_REQUEST['synology']) || isset($_REQUEST['telegram'])) send_authcode(); // if phone number isset – sending SMS

// -----------------------------------
// Check for router (ruid) is in array
// -----------------------------------
function ruid_auth() {
  global $ruid_data;
  if (!$_REQUEST['pass']) return false; // if password not set - reset
  // check password md5-hash
  if (md5($_REQUEST['pass']) == $ruid_data[$_REQUEST['ruid']]['mdpass']) return true;
  return false;
}

// -------------------------------------------
// Send autherization sms via ros api function
// -------------------------------------------
function send_authcode() {
  global $firewall;
  // If firewall == true, allow access only to routers has record in array $ruid_data
  if ($firewall) firewall();

  // Generate auth-code and add to REQUEST array
  $_REQUEST['authcode'] = substr(str_shuffle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'), 0, 5);
  // Create message that will be sent to user
  $message = 'To authorize user '.$_REQUEST['username'].' connection open '.HOST.'?ruid='.$_REQUEST['ruid'].'&auth='.$_REQUEST['authcode'];

  if ($_REQUEST['telegram']) send_telegram($message); // via telegram
  if ($_REQUEST['syno_token']) send_synoChat($message); // via synology chat
  if ($_REQUEST['phone']) send_SMS($message); // via SMS to phone

  // логируем запросы | save log
  writelog('SEND AUTH CODE');
  die($_REQUEST['authcode']);
}

// -------------
// Over Telegram
// -------------

function send_telegram($message) {
  $url = 'https://api.telegram.org/bot'.TELEGRAM_BOT_TOKEN.'/sendMessage';
  // creating message
  $options = array('http' =>
      array(
          'method'  => 'POST',
          'header'  => 'Content-Type: application/json',
          'content' => '{"chat_id":"'.$_REQUEST['telegram'].'", "text": "'.$message.'"}'
      )
  );
  $content  = stream_context_create($options);
  $result = file_get_contents($url, false, $content);
}

// ------------------
// Over Synology chat
// ------------------
// info - https://www.synology.com/knowledgebase/DSM/tutorial/Collaboration/How_to_configure_webhooks_and_slash_commands_in_Chat_Integration
function send_synoChat($message) {
  $url = SYNOLOGY_WEBHOOK_URL.$_REQUEST['syno_token'];
  // creating message
  $options = array('http' =>
      array(
          'method'  => 'POST',
          'header'  => 'Content-Type: application/x-www-form-urlencoded',
          'content' => 'payload='.urlencode('{"text": "'.$message.'"}')
      )
  );
  $content  = stream_context_create($options);
  $result = file_get_contents($url, false, $content);
}


// -----------------
// SMS via usb-modem
// -----------------

function send_SMS($message) {
  global $ruid_data;
  global $SMS_gateway;
  // Get random SMS-gateway
  $sms_gw = $ruid_data[$_REQUEST['ruid']]['smsgw'][array_rand($ruid_data[$_REQUEST['ruid']]['smsgw'], 1)]; // gateway data

  if ($sms_gw == "PAY") UsePAYsmsc($message); // If use paid sms center gateway
  $API = new RouterosAPI(); // connect class
  // if connected successfully - sending message
  if ($API->connect($SMS_gateway[$sms_gw]['ip'], $SMS_gateway[$sms_gw]['login'], $SMS_gateway[$sms_gw]['password'])) {
      // SMS send command
      $ARRAY = $API->comm("/tool/sms/send", array(
      "port"=>$SMS_gateway[$sms_gw]['port'],
      "channel"=>$SMS_gateway[$sms_gw]['channel'],
      "phone-number"=>$_REQUEST['phone'],
      "message"=>$message,));
      // Checking if send failed and error message return, will make usb power-reset to restart modem
      if($ARRAY['!trap']) {
        $API->comm("/system/routerboard/usb/power-reset");
        // Save log | Add error to array and save all array to log
        $_REQUEST['ERROR'] = $ARRAY['!trap'][0]['message'];
        writelog('MODEM ERROR');
        die('Stop with error: '.$ARRAY['!trap'][0]['message'].' Making power reset of usb-port');}
  }

  $API->disconnect();
}

// --------------------------------------------------------------------
// Autherization using ros api function – delete list from address-list
// --------------------------------------------------------------------
function autorize() {
  global $ruid_data;
  // connect class
  $API = new RouterosAPI();
  if ($API->connect($ruid_data[$_REQUEST['ruid']]['ip'], $ruid_data[$_REQUEST['ruid']]['login'], $ruid_data[$_REQUEST['ruid']]['password'])) {
    // if connected successfully - sending command
    $API->write('/ip/firewall/address-list/print', false);
    $API->write('?comment='.$_REQUEST['auth'], false);
    $API->write('=.proplist=.id');
    // get response
    $ARRAYS = $API->read();
    // If no record in firewall address_list – reset
    if (!$ARRAYS[0]) die(header('HTTP/1.0 406 Not Acceptable'));
    // delete firewall address-list
    $API->write('/ip/firewall/address-list/remove', false);
    $API->write('=.id=' . $ARRAYS[0]['.id']);
    $READ = $API->read();
  }
  $API->disconnect();
  // save log
  writelog('AUTHERIZATION');

  // Show success page to user
  die('
      <!DOCTYPE html>
      <html lang="ru">
      <meta http-equiv="Content-Type" content="charset=utf-8" />
      <body style="font-family: Verdana, Arial, Helvetica, sans-serif; background-color: #282c34; color: #fff; height: 100vh; display: flex;">
        <div style="margin: auto; max-width: 50%;">
          <p style="font-size: 24pt; font-weight: bold; margin: 0 0 10px;">
            VPN-соединение установлено, можете продолжить работу<br />
          </p>
          <p style="font-size: 12pt; color: #aaa;">
            В случае недоступности сервисов обратитесь к вашему системному администратору<br />
          </p>
          <p style="font-size: 24pt; font-weight: bold; margin: 100px 0 10px;">
            VPN connection is established, you can continue to work
          </p>
          <p style="font-size: 12pt; color: #aaa;">
            If any services unavalible you must contact with your system administrator<br />
          </p>
        </div>
      </body>
      </html>
    ');
}

// -----------------------------------------------------------------------------------------------
// Send sms via paid sms center gateway (smsgw value in $ruid_data should be installed 0 => «pay»)
// -----------------------------------------------------------------------------------------------
function UsePAYsmsc($message) {
    // for example i use smsc.ru
    $smsc_login = '#SMSCLOGIN#';
    $smsc_pass = '#SMSCPASSWORD#';
    $smsc_sendername = '#SMSCSENDERNAME#'; // if need
    // SEND SMS
    $sms_send = file_get_contents('https://smsc.ru/sys/send.php?login='.$smsc_login.'&psw='.$smsc_pass.'&phones='.$_REQUEST['phone'].'&mes='.$message.'&sender='.$smsc_sendername.'&flash=0');
    if (strpos($sms_send, 'OK') !== false) {
      die($_REQUEST['authcode']);
    }
      die($_REQUEST['Send SMS error']);
};

// -------------------------------------------------------------------------
// Firewall - allow access to send SMS only for router from array $ruid_data
// -------------------------------------------------------------------------
function firewall() {
  global $uselog;
  global $log_path;
  global $ruid_data;

  $result = false;
  // serch ip in array $ruid_data
  foreach ($ruid_data as $value) {
    $result = (in_array($_SERVER['REMOTE_ADDR'], $value) === true) ? true : false;
    if($result) break; // if found record – break
  }
  // $uselog == true | save log
  if (!$result) {
    if ($uselog) {
      $fp = fopen(LOG_FILEPATH, 'a');
      fputs($fp, "\nTime = " . date("Y-m-d H:i:s")."\n");
      fputs($fp, 'FIREWALL BLOCKED ACCESS'."\n");
      fputs($fp, $_SERVER['REMOTE_ADDR']."\n");
      fclose($fp);
    }
    die(header('HTTP/1.0 403 Forbidden'));
  }
}

// -----------------
// Save log function
// -----------------
function writelog($type) {
  global $uselog;
  global $log_path;
  // $uselog == false – break
  if (!$uselog) return;
  // remove ruid password from array before saving log
  unset($_REQUEST['pass']);
  // save log
  $fp = fopen(LOG_FILEPATH, 'a');
  fputs($fp, "\nTime = " . date("Y-m-d H:i:s")."\n");
  fputs($fp, $type."\n");
  fputs($fp, print_r($_REQUEST, true));
  fclose($fp);
}

?>


File: /LICENSE
MIT License

Copyright (c) 2020 Dmitri Agababaev

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


File: /mtvpn.rsc
# Need to replace with your values in this code: yourwebsite.com, ROUTERLOGIN, ROUTER_PASSWORD
# Place #phone number / #synology_chat_token / #telegram_id in user ppp secret comment


/ip firewall address-list
add address=yourwebsite.com list=VPN_allow-list
add address=8.8.8.8 list=VPN_allow-list
add address=10.200.1.1 list=VPN_allow-list
add address=telegram.org list=Allow-list
add address=149.154.172.0/22 list=Allow-list comment=telegram
add address=149.154.168.0/22 list=Allow-list comment=telegram
add address=149.154.164.0/22 list=Allow-list comment=telegram
add address=149.154.160.0/22 list=Allow-list comment=telegram
add address=91.108.56.0/22 list=Allow-list comment=telegram
add address=91.108.16.0/22 list=Allow-list comment=telegram
add address=91.108.12.0/22 list=Allow-list comment=telegram
add address=91.108.8.0/22 list=Allow-list comment=telegram
add address=91.108.4.0/22 list=Allow-list comment=telegram

/ip firewall raw
add action=drop chain=prerouting dst-address-list=!VPN_allow-list src-address-list=VPN-unauth disabled=no

/ip pool
add name=2F-VPN_pool ranges=10.200.1.10-10.200.1.254

/ppp profile
add change-tcp-mss=no dns-server=10.10.0.1 idle-timeout=29m local-address=10.200.1.1 name=2F-VPN on-down=":global ruidlogin \"ROUTERLOGIN\";\r\
    \n:global ruidpass \"ROUTER_PASSWORD\";\r\
    \n:global host \"https://yourwebsite.com/\";\r\
    \n\r\
    \n:local userip \$\"remote-address\";\r\
    \n:local username \$user;\r\
    \n\r\
    \n/tool fetch http-method=post http-data=\"ruid=\$ruidlogin&pass=\$ruidpass&username=\$username&remote-ip=\$userip&action=down\" url=\"\$host\" mode=ht\
    tps as-value output=user;\r\
    \n/ip firewall address-list remove [find address=\$userip];\r\
    \n\r\
    \n:log warning \"User disconnected:\";\r\
    \n:log warning \$user;\r\
    \n:log warning \$userip;\r\
    \n" on-up=":global ruidlogin \"ROUTERLOGIN\";\r\
    \n:global ruidpass \"ROUTER_PASSWORD\";\r\
    \n:global host \"https://yourwebsite.com/\";\r\
    \n\r\
    \n:local userip \$\"remote-address\";\r\
    \n:local userAddress [/ppp secret get [find name=\$user] comment];\r\
    \n:local username \$user;\r\
    \n\r\
    \n:local authkey [/tool fetch http-method=post http-data=\"ruid=\$ruidlogin&pass=\$ruidpass&\$userAddress&username=\$username&remote-ip=\$userip\" url=\
    \"\$host\" mode=https as-value output=user];\r\
    \n\r\
    \n/ip firewall address-list remove [find address=\$userip];\r\
    \n/ip firewall address-list add address=\$userip list=VPN-blocked timeout=30m comment=(\$authkey->\"data\");\r\
    \n\r\
    \n:log warning \"User connect:\";\r\
    \n:log warning \$username;\r\
    \n:log warning \$userip;\r\
    \n:log warning (\$authkey->\"data\");" remote-address=2F-VPN_pool use-compression=no use-encryption=yes use-mpls=no use-upnp=no

/ppp secret
add comment="phone=<user_phone_number>" name=username1 password=testuser profile=2F-VPN disabled=yes
add comment="synology=<synology_token>" name=username2 password=testuser profile=2F-VPN disabled=yes
add comment="telegram=<telegram_username_id>" name=username3 password=testuser profile=2F-VPN disabled=yes


File: /README.md
# Mikrotik_VPN_2F_auth
2 factor authentification using SMS (over gsm modem or payed sms gateway) / Synology Chat / Telegram bot when users or any equipment create VPN connection to Mikrotik

Скрипт двухфакторной аутентификации пользователей VPN через SMS для MikroTik

- Простые скрипты ROS не создают никакой нагрузки и работают даже на hAP Lite
- Масштабируемость – возможность подключения большого количества VPN-шлюзов с целью снижения нагрузки или географического распределения
- Возможность использования Mikrotik CHR в качестве VPN-сервера
- «1хN» – 1 SMS-шлюз на неограниченное количество роутеров с возможностью расширения при росте нагрузки
- Возможность привязки отдельного роутера к «конкретному» модему
- Использование всего одного php скрипта на удаленном сервере
- Не важно какое устройство инициировало VPN-соединение, авторизация по ссылке из SMS
- Ведение log'а всех запросов на сервере (можно вкл/выкл)
- Увеличение отказоустойчивости и снижения нагрузки системы путем отправки SMS рандомно с нескольких модемов
- Возможность отправки SMS через платные шлюзы (на примере https://smsc.ru)
- Firewall – доступ на генерацию кодов и отправку SMS только у роутеров занесенных в список (можно вкл/выкл)
– Отправка кодов авторизации в Synology Chat и через Telegram Bot

------------

Two-factor authentication script for VPN users via SMS for MikroTik

- Simple ROS scripts do not create any load and even work on hAP Lite
- Scalability - the ability to connect a large number of VPN gateways to reduce load or geographical distribution
- Ability to use Mikrotik CHR as a VPN server
- “1xN” - 1 SMS gateway for an unlimited number of routers with the possibility of expansion with increasing load
- Ability to bind a separate router to a "specific" modem
- Using just one php script on a remote server
- It doesn’t matter which device initiated the VPN connection, authorization by the link from SMS
- Authorization log on the server (may be on/off)
- Increase fault tolerance and reduce system load by sending SMS randomly from multiple modems
- Send SMS via paid sms center getaway (for example https://smsc.ru)
- Firewall - allow access to generate codes and send SMS only for router from array (may be on/off)
– Send auth code via Synology Chat and Telegram Bot


