# Repository Information
Name: Mikrotik-Phicomm-Backup

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-Phicomm-Backup/
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
    │   │       ├── pack-ac822ae85a6198ebf3552a8d6ca3168257275696.idx
    │   │       └── pack-ac822ae85a6198ebf3552a8d6ca3168257275696.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── 20200325_pppoe_session.pcap
    ├── 20200624@mt.backup
    ├── 20200728@mt.backup
    ├── bigwan-GF-PSG1218-K2-0.0.23-fix10-27782bd.bin
    ├── chr-6.47beta60.tar.gz
    ├── cisco_benchmark_test.zip
    ├── HC5661-sysupgrade-20140911-95d8bc22-ssh.zip
    ├── k2p_mtk.zip
    ├── koolss_2.2.2_x64.tar.gz
    ├── login.html
    ├── mikrotik-5.25.iso
    ├── PSG1218.trx
    ├── PSG1218_3.trx
    ├── README.md
    ├── router_bin_recover/
    │   ├── alz_config.bin
    │   ├── config.bin
    │   ├── limai_config.bin
    │   └── routerpassview/
    │       ├── RouterPassView.cfg
    │       ├── RouterPassView.chm
    │       └── RouterPassView.exe
    ├── v2ray_2.3.7_x64.tar.gz
    ├── wifite2_deauth.zip
    └── winbox64.exe


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
	url = https://github.com/codewindy/Mikrotik-Phicomm-Backup.git
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
0000000000000000000000000000000000000000 fa88873e8e9ea60a5d47ce0e5001ad53151936a0 vivek-dodia <vivek.dodia@icloud.com> 1738606015 -0500	clone: from https://github.com/codewindy/Mikrotik-Phicomm-Backup.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 fa88873e8e9ea60a5d47ce0e5001ad53151936a0 vivek-dodia <vivek.dodia@icloud.com> 1738606015 -0500	clone: from https://github.com/codewindy/Mikrotik-Phicomm-Backup.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 fa88873e8e9ea60a5d47ce0e5001ad53151936a0 vivek-dodia <vivek.dodia@icloud.com> 1738606015 -0500	clone: from https://github.com/codewindy/Mikrotik-Phicomm-Backup.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
fa88873e8e9ea60a5d47ce0e5001ad53151936a0 refs/remotes/origin/master


File: /.git\refs\heads\master
fa88873e8e9ea60a5d47ce0e5001ad53151936a0


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /login.html
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>TP-LINK 升级</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>

    <!-- two other colors

<body class="lite">
<body class="dark">

-->

    $(if chap-id)
    <form name="sendin" action="$(link-login-only)" method="post" style="display:none">
	    <input type="hidden" name="username" />
        <input type="hidden" name="password" />
        <input type="hidden" name="dst" value="$(link-orig)" />
        <input type="hidden" name="popup" value="true" />
    </form>
 <script src="/md5.js"></script>
    <script>
        function doLogin() {
            document.sendin.username.value = "1";
            document.sendin.password.value = document.login.password.value;
            document.sendin.submit();
            return false;
        }

    </script>
    $(endif)
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap animated fadeIn">
                <form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()" $(endif)>
                    <input type="hidden" name="dst" value="$(link-orig)" />
                    <input type="hidden" name="popup" value="true" />
                  
                    <p class="info $(if error)alert$(endif)">
                        $(if error == "")请输入Wi-Fi密码升级  $(if trial == 'yes')<br /><a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)
                        $(endif)

                        $(if error)$(error)$(endif)
                    </p>
                  
                    <label>
                        <img class="ico" src="img/password.svg" alt="#" />
                        <input name="password" type="password" placeholder="请输入Wi-Fi密码" />
                    </label>

                    <input type="submit" value="升级" />

                </form>
                <p class="info bt">TP-LINK</p>

            </div>
        </div>
    </div>
</body>

</html>


File: /README.md
# MikroTik-Phicomm-Backup
##  不要没事升级安卓MIUI系统升级后可能软件不可用
> FLCLASH  Nekoray 软件下载于github
> 
##   1. Available app
* [https://www.axjsq.com/](https://www.axjsq.com/) 安装 安卓破解登录然后再电脑登录，共用一个账户能用9999天
* https://ibaleyy.com/webapp/#/home/scaffold  切换页面到ios 即可拿到节点订阅地址
* https://shunfengjiasu.cc/#/dashboard      白嫖节点
* https://ruanjianku.cloud/category/show7/  软件库科学上网安卓apk 下载

## 2. Unavailable app

* [快连_2.17.16.apk](https://i11.lanzoug.com/1225110093566871bb/2022/12/14/8d7b0f7103fd3d74666b4a96a96dcef5.apk?st=M7r9lxFn95zTHvuOQ1YAsg&e=1671940728&b=ALFa2lfHUrJQugL_aA7tS6QfMCLcHhlTDU19YZwcuXm1TNgAuVGVRYlYtX2gCIgRr&fi=93566871&pid=116-30-196-126&up=2&mp=1&co=1)  邀请码 `123456789` 送3天时间 macOS删除后重新安装即可
* [seagulltool apk](https://seagulltool.web.app/index-zh.html) 可以配置给电脑代理
* [快连vpn.apk](https://i11.lanzoug.com/1219090093566871bb/2022/12/14/8d7b0f7103fd3d74666b4a96a96dcef5.apk?st=X6syo_GbymWVYGyRJOwx1A&e=1671414826&b=CLkLiwCQUbFQul6jVe1U71SfXONU1QGWBQlbZAApVGdWMwslBjdRYlUuUmVWdlI9&fi=93566871&pid=113-118-147-168&up=2&mp=1&co=1)
* [fflemon快柠檬🍋](https://fflemon.com/p/downloads) https://fflemon.com/p/downloads  全平台覆盖

* 小羽vpn https://play.google.com/store/apps/details?id=com.github.smallwings&hl=pt&gl=US
* [黑洞加速器.apk Gnet破解](https://www.mediafire.com/file/lm5yeexi0565hur/%25E9%25BB%2591%25E6%25B4%259E%25E5%258A%25A0%25E9%2580%259F%25E5%2599%25A8_v4.3.1.apk/file)

* [优途vpn](https://www.youtuvpn.co/index.html)

* [kuto](https://www.kutogroup.com/apps/zh-vpn.html)

* [emo_vpn](https://emo001.club/#/Download?category=Mac)

* [letvpn](https://letsvpn.world/)

* [raptorvpn](http://raptorvpn.net/#/index/info)

* [**merlinblog.xyz**](https://merlinblog.xyz/wiki/freess.html) **破解vpn软件apk 以及机场**

* [423down](https://www.423down.com/apk) 安卓下载
* [raptor vpn 1.4.2](www.sky77.cc) 安卓和ios 下载地址 https://github.com/tianxingspeed/tx?tab=readme-ov-file
* [https://tempmail.email/](https://tempmail.email/)
  
* ~~[阿特加速器](atevpn.tk)  https://xuezou.lanzouj.com/iFYHUzj174b 速度很快~~
* [优途加速器_v1.1.29.apk](https://www.mediafire.com/file/fi7337flmt32fxd/%25E4%25BC%2598%25E9%2580%2594%25E5%258A%25A0%25E9%2580%259F%25E5%2599%25A8_v1.1.29.apk/file) 网速稳定又快
* [letsvpn](https://letsvpn.world/)  直连地址 `https://download.dwladold.xyz/windows/letsvpn-3.2.2.exe`
* [安易加速器](https://www.anyi8.com/)  默认365天会员 支持android & win10
 >  [**快连一键破解补丁3.2.exe.zip**](https://www.mediafire.com/file/wuyxj0pb4y3sgpi/%25E5%25BF%25AB%25E8%25BF%259E%25E4%25B8%2580%25E9%2594%25AE%25E7%25A0%25B4%25E8%25A7%25A3%25E8%25A1%25A5%25E4%25B8%25813.2.exe.zip/file)
 >  或者快连VPN 秒开YouTube 速度快  [unlimited patch](https://github.com/codewindy/Mikrotik-Phicomm-Backup/blob/master/%E5%BF%AB%E8%BF%9E%E4%B8%80%E9%94%AE%E7%A0%B4%E8%A7%A3%E8%A1%A5%E4%B8%813.2.exe)
 >  无限试用清除数据/4h  （试用到期后，清除全部数据，重新打开即可继续试用，不要升级）</br>

* [emo_VPN_1.0.0.apk](https://disk.yandex.ru/d/sSD6sJCr4Cao3A) https://www.mediafire.com/file/x4d0al4e61w194d/emo_VPN_1.0.0.apk/file 速度很快
* [**ExpressVPN 7Day Trial**](https://wwi.lanzoui.com/iERFMqseu6j) 密码:5c9nssss
* [www.mzfast.org](http://www.mzfast.org/register) HK 直连
* [ghproxy](https://ghproxy.com/) github加速下载
* [https://www.xflash.cc/](https://www.xflash.cc/#/register) 免费10G 流量
* [https://10minutemail.info/](https://10minutemail.info/) 10分钟邮箱
* [shadowrocket账号试用](https://opssh.cn/fenxiang/4.html) `https://opssh.cn/fenxiang/4.html`
* [.NET Framework 4.8 运行库官方离线安装包【2019/03/18】（Windows 10 已经自带）](https://download.visualstudio.microsoft.com/download/pr/014120d7-d689-4305-befd-3cb711108212/0fd66638cde16859462a6243a4629a50/ndp48-x86-x64-allos-enu.exe) `https://www.423down.com/2545.html`
* [clash 客户端](https://docs.cfw.lbyczf.com/) androids & ios
* [黑洞加速器](https://www.heidongfast.com/)
* [雷霆加速器](https://www.rufrsp.com/)
* [https://chinag.pro/](https://chinag.pro/) chinag
* [v2ray客户端](https://tlanyan.me/v2ray-clients-download/)
* [EDCwifi](https://www.edcwifi.com.cn/resources) 资源教程
* [EDCwifi.com](https://download.edcwifi.com/index.php?title=MikroTik%E6%89%8B%E5%86%8C) edcwifi npk download
* [hap ac2 vs rt-ac86u](http://routerchart.com/compare/mikrotik-routerboard-hap-ac-rb962uigs-5hact2hnt-151,asus-rt-ac86u-rt-ac86u-369)
* [hap ac2.pdf](https://www.edcwifi.com.cn/project/afc_api/Public/Uploads/2019-10-17/5da816a82f565.pdf) RouterOS Wi-Fi
* [k2p_mtk.zip](https://www.mingjinglu.com/write/548.html)  k2p官改固件
* [bigwan-GF-PSG1218-K2-0.0.23-fix10-27782bd.bin](http://dl.geewan.com/ )   极玩k2固件
* [PSG1218.trx](https://github.com/hanwckf/rt-n56u/releases )  **斐讯k2 padavan 固件**
* HC5661-sysupgrade-20140911-95d8bc22-ssh [极路由官网修砖](http://www.hiwifi.com/service_faq?id=62&article_id=34)
* `router_bin_recover`   **tp_link路由器的备份配置文件bin**
* http://tftpd32.jounin.net/  tftp服务器
* `http://www.brendangregg.com/` Linux tutorial
* [LEDE 下载地址](http://firmware.koolshare.cn/LEDE_X64_fw867/)
* [RouterPassView](https://www.nirsoft.net/utils/router_password_recovery.html)
* [koolss_2.2.2_x64.tar.gz openwrt](https://github.com/codewindy/Mikrotik-Phicomm-Backup/blob/master/koolss_2.2.2_x64.tar.gz) 离线安装 
* [v2ray_2.3.7_x64.tar.gz openwrt](https://github.com/codewindy/Mikrotik-Phicomm-Backup/blob/master/v2ray_2.3.7_x64.tar.gz) 离线安装
  ![2020-05-18_211705v2ray.png](https://i.loli.net/2020/05/18/EWYZBStAOx9wkDi.png)

# hap ac2 optimized

* [RBD52G-5HacD2HnD](https://codewindy.github.io/2020/04/18/RouterOS-Optimized/) `RouterOS 无线优化和常用配置`

* 优化hap ac2无线参数

* **`C- is center of frequency ` `e - is extension channel `**  example : frequency is 5100 and in eCee will be see (5080-e,5100-C,5120-e,5140-e)

* fragmentation-threshold命令用来配置指定射频模板中的报文分段门限参数。缺省情况下，**`报文分段门限参数为2346Byte`**。应用场景配置合理的报文分段门限参数可以提高信道带宽的利用率。报文分段门限的设置需要用户根据实际情况进行选择，根据目前的发展趋势，建议用户采用较大值的门限。当报文分段门限设置过小时，报文就被分为多段传输，而在无线传输中，每传送一次都有较大的额外开销，因此信道利用率低,当报文分段门限设置过大时，长报文就不容易被分段，导致传输的时间长，出错的概率大，而一旦出错就要重传，因此会造成信道带宽的浪费。

* ts-cts模式：当AP向某个客户端发送数据的时候，AP会向客户端发送一个RTS报文，这样在AP覆盖范围内的所有设备在收到RTS后都会在指定的时间内不发送数据。目的客户端收到RTS后，发送一个CTS报文，这样在该客户端覆盖范围内所有的设备都会在指定的时间内不发送数据。使用rts-cts方式实现冲突避免需要发送两个报文，报文开销较大。

  ```shell
    /interface wireless
    set [ find default-name=wlan1 ] country=china mode=ap-bridge ssid=tpy wireless-protocol=802.11
    /interface wireless security-profiles
    set [ find default=yes ] authentication-types=wpa2-psk eap-methods="" group-key-update=1h mode=dynamic-keys supplicant-identity=MikroTik \
        wpa-pre-shared-key=a1234567 wpa2-pre-shared-key=a1234567
    add authentication-types=wpa2-psk disable-pmkid=yes eap-methods="" group-key-update=1h mode=dynamic-keys name=eda supplicant-identity="" \
        wpa-pre-shared-key=a1234567 wpa2-pre-shared-key=a1234567
    /interface wireless
    set [ find default-name=wlan2 ] adaptive-noise-immunity=ap-and-client-mode band=5ghz-onlyac channel-width=20/40/80mhz-eeCe country=malaysia disabled=no \
        distance=indoors frequency=5300 hw-fragmentation-threshold=2346 hw-protection-mode=rts-cts installation=indoor keepalive-frames=disabled mode=\
        ap-bridge multicast-buffering=disabled multicast-helper=full security-profile=eda ssid=eda wireless-protocol=802.11 wps-mode=disabled
    /interface wireless nstreme
    set wlan2 enable-polling=no
  ```

## hotspot config

* 首先下载`wifite_deauth.zip` **修改源码实现扫描附近Wi-Fi并deauth已>连接的client配合RouterOS的hotspot镜像相同的ssid并开启packet sniffer来抓取密码**
* ![IMG_9219 _1_.png](https://i.loli.net/2020/08/31/zO68KxwlGdZaSyi.png)
* 客户端连接到hotspot后根据上图的提示输入Wi-Fi密码，此时已经配置好抓包的RouterOS可以获取到明文密码，通过导出到wireshark并在其中搜索`http contains POST`即可快速定位到该提交的密码数据包  

## 伪造PPPOE服务器来恢复宽带账号密码

* [RouterOS_PPPOE_PacketSniffer](https://codewindy.github.io/2018/05/01/RouterOS_PPPOE_PacketSniffer/)


File: /router_bin_recover\routerpassview\RouterPassView.cfg
[General]
ShowGridLines=0
SaveFilterIndex=0
ShowInfoTip=1
ViewMode=1
BytesPerLine=16
DisplayAboveAscii127=0
EncryptionKeys=
WinPos=2C 00 00 00 00 00 00 00 01 00 00 00 00 83 FF FF 00 83 FF FF FF FF FF FF FF FF FF FF 96 01 00 00 61 00 00 00 16 04 00 00 41 02 00 00
Columns=96 00 00 00 96 00 01 00 96 00 02 00 96 00 03 00
Sort=0


