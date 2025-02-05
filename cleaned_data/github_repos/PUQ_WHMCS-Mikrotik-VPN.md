# Repository Information
Name: PUQ_WHMCS-Mikrotik-VPN

# Directory Structure
Directory structure:
└── github_repos/PUQ_WHMCS-Mikrotik-VPN/
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
    │   │       ├── pack-03efadbc604b904fed127ba60c4e6d7cf8d4dbff.idx
    │   │       └── pack-03efadbc604b904fed127ba60c4e6d7cf8d4dbff.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── puqMikrotikVPN/
    │   ├── clientarea.tpl
    │   ├── lang/
    │   │   ├── english.php
    │   │   └── polish.php
    │   └── puqMikrotikVPN.php
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
	url = https://github.com/PUQ-sp-z-o-o/PUQ_WHMCS-Mikrotik-VPN.git
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
0000000000000000000000000000000000000000 bfdb8a57f02292136a7f347c5a9fa3282bcf49e1 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/PUQ-sp-z-o-o/PUQ_WHMCS-Mikrotik-VPN.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 bfdb8a57f02292136a7f347c5a9fa3282bcf49e1 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/PUQ-sp-z-o-o/PUQ_WHMCS-Mikrotik-VPN.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 bfdb8a57f02292136a7f347c5a9fa3282bcf49e1 vivek-dodia <vivek.dodia@icloud.com> 1738606024 -0500	clone: from https://github.com/PUQ-sp-z-o-o/PUQ_WHMCS-Mikrotik-VPN.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
bfdb8a57f02292136a7f347c5a9fa3282bcf49e1 refs/remotes/origin/main


File: /.git\refs\heads\main
bfdb8a57f02292136a7f347c5a9fa3282bcf49e1


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /puqMikrotikVPN\clientarea.tpl

<table style="width:100%" >
<tr>
<th>
<table style="width:90%" class="table table-striped">
<tr>
<td colspan="2">
{if $curl['name']}
<div class="alert alert-success text-center">ONLINE</div></td>
{else}
<div class="alert alert-danger text-center">OFFLINE</div></td>
{/if}
</tr>
<tr>
<td><b>Service:</b></td>
<td>
{if $curl['service']}{$curl['service']}{else}<img src="/assets/img/statusfailed.gif" alt="Online" width="16" height="16">{/if}
</td>
</tr>
<tr>
<td><b>Name:</b></td>
<td>
{if $curl['name']}{$curl['name']}{else}<img src="/assets/img/statusfailed.gif" alt="Online" width="16" height="16">{/if}
</td>
</tr>
<tr>
<td><b>Caller-id:</b></td>
<td>
{if $curl['caller-id']}{$curl['caller-id']}{else}<img src="/assets/img/statusfailed.gif" alt="Online" width="16" height="16">{/if}
</td>
</tr>
<tr>
<td><b>Address:</b></td>
<td>
{if $curl['address']}{$curl['address']}{else}<img src="/assets/img/statusfailed.gif" alt="Online" width="16" height="16">{/if}
</td>
</tr>
<tr>
<td><b>Uptime:</b></td>
<td>
{if $curl['uptime']}{$curl['uptime']}{else}<img src="/assets/img/statusfailed.gif" alt="Online" width="16" height="16">{/if}
</td>
</tr>
</table>
</th>
<th>
<b>{$lang['server_address']}:</b> <h2>{$params['serverhostname']}</h2>
<hr>
<h5>{$lang['info_1']}</h5>
<table style="width:90%" class="table">
    <tr>
        <td>{$lang['username']}:</td>
        <td>{$params['username']}</td>
    </tr>
        <td>{$lang['password']}:</td>
        <td>{$params['password']}</td>
    </td>
</tr>
</table>
</th>
</tr>
</table>

File: /puqMikrotikVPN\lang\english.php
<?php
$_LANG_PUQ['server_address'] = "Server address";
$_LANG_PUQ['username'] = "Username";
$_LANG_PUQ['password'] = "Password";
$_LANG_PUQ['info_1'] = "You can log in using your Username/Password";




File: /puqMikrotikVPN\lang\polish.php
<?php
$_LANG_PUQ ['server_address'] = "Adres serwera";
$_LANG_PUQ ['username'] = "Nazwa użytkownika";
$_LANG_PUQ ['password'] = "Hasło";
$_LANG_PUQ ['info_1'] = "Możesz zalogować się przy użyciu swojej nazwy użytkownika i hasła";



File: /puqMikrotikVPN\puqMikrotikVPN.php
<?php
/*
 +-----------------------------------------------------------------------------------------+
 | This file is part of the WHMCS module. "PUQ_WHMCS-Mikrotik-VPN"                         |
 | The module allows you to manage the /ppp/secret/ users as a product in the system WHMCS.|
 | This program is free software: you can redistribute it and/or modify it                 |
 +-----------------------------------------------------------------------------------------+
 | Author: Ruslan Poloviy ruslan.polovyi@puq.pl                                            |
 | Warszawa 04.2021 PUQ sp. z o.o. www.puq.pl                                              |
 | version: 1.1.1                                                                          |
 +-----------------------------------------------------------------------------------------+
*/

use WHMCS\Database\Capsule;

function puqMikrotikVPN_MetaData(){
  return array(
      'DisplayName' => 'PUQ Mikrotik VPN',
      'DefaultSSLPort' => '443',
      'language' => 'english',
  );
}

function puqMikrotikVPN_ConfigOptions() {
  $configarray = array(
      'Comment PREFIX' => array( 'Type' => 'text', 'Default' => 'WHMCS'),
      'Profile' => array( 'Type' => 'text', 'Default' => 'default' ,'Size' => '20','Description' => 'PPP Secret Profile',),
      'Max Limit Upload' => array( 'Type' => 'text', 'Default' => '10' ,'Size' => '10','Description' => 'M',),
      'Max Limit Download' => array( 'Type' => 'text', 'Default' => '10' ,'Size' => '10','Description' => 'M',),

      'Service' => array( 'Type' => 'dropdown',
          'Options' => array(
              'any' => 'any',
              'async' => 'async',
              'l2tp' => 'l2tp',
              'ovpn' => 'ovpn',
              'pppoe' => 'pppoe',
              'ppptp' => 'ppptp',
              'sstp' => 'sstp',
          ), 'Default' => 'any' ,'Size' => '20','Description' => 'PPP Secret Servive',),

  );
  return $configarray;
}

function puqMikrotikVPN_apiCurl($params,$data,$url,$method){

  $curl_url = 'https://' . $params['serverhostname'] . ':'. $params['serverport'] . '/rest' . $url;
  $postdata = json_encode($data);
  $curl = curl_init();
  curl_setopt($curl, CURLOPT_URL, $curl_url);
  curl_setopt($curl, CURLOPT_HTTPHEADER, array('content-type: application/json'));
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($curl, CURLOPT_CUSTOMREQUEST, $method);
  curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
  curl_setopt($curl, CURLOPT_USERPWD, $params['serverusername'].':'.$params['serverpassword']);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $postdata);
  curl_setopt($curl,CURLOPT_TIMEOUT,5);
  $answer = curl_exec($curl);
  $array = json_decode($answer,TRUE);
  curl_close($curl);
  return $array;
}

function puqMikrotikVPN_GetIP($params) {
  $serverid = $params['serverid'];
  $ips_sql = json_decode(json_encode( Capsule::table('tblservers')
      ->select('tblservers.assignedips')
      ->where('id',$serverid)
      ->get(), true));

  $ips = explode("\r\n",$ips_sql[0]->assignedips);


  $hosting_ips_sql = json_decode(json_encode( Capsule::table('tblhosting')
      ->select('tblhosting.dedicatedip')
      ->where(array(
          array('server',$serverid),
          array('domainstatus','!=','Terminated')
          )
      )
      ->get(), true));

  $hosting_ips = array();
  foreach ($hosting_ips_sql as $ip) {
    array_push($hosting_ips, $ip->dedicatedip);
  }

  foreach ($ips as $ip) {
    if (!in_array($ip,$hosting_ips)){
      return $ip;
    }
  }
  return '0.0.0.0';
  //logModuleCall('puqMikrotikVPN', 'GetIP', $ips, $hosting_ips);
}

function puqMikrotikVPN_CreateAccount($params) {
  $ip = puqMikrotikVPN_GetIP($params);
  $serviceid = $params['serviceid'];
  $username = $params['username'];
  $password = $params['password'];
  $mikrotik_profile = $params['configoption2'];
  $mikrotik_service = $params['configoption5'];
  $mikrotik_comment = $params['configoption1'] . '|Product ID:'. $params['serviceid'] . '|' . $params['clientsdetails']['email'];
  $mikrotik_max_limit = $params['configoption3'] . 'M/' . $params['configoption4'].'M';

  Capsule::table('tblhosting')->where('id', $serviceid)->update(["dedicatedip"=>$ip]);

  $data = array(
    'name'=> $username,
    'password' => $password,
    'remote-address'=>$ip,
    'profile'=> $mikrotik_profile,
    'service'=> $mikrotik_service,
    'comment'=> $mikrotik_comment
    );

    #add ppp user
    $create_user = puqMikrotikVPN_apiCurl($params,$data,'/ppp/secret', 'PUT');
    if(!$create_user){
      return 'API problem';
    }
    if($create_user['error']){
      return 'Error: ' . $create_user['error'] . '| Message' . $create_user['message'];
    }

    #add queue
    puqMikrotikVPN_apiCurl($params,$data,'/queue/simple/'.$username, 'DELETE');
    $data = array(
        'name'=> $username,
        'target'=>$ip,
        'max-limit'=> $mikrotik_max_limit,
        'comment'=> $mikrotik_comment
    );

    $add_queue = puqMikrotikVPN_apiCurl($params,$data,'/queue/simple', 'PUT');
    if(!$add_queue){
      return 'API problem';
    }
    if($add_queue['error']){
      return 'Error: ' . $add_queue['error'] . '| Message' . $add_queue['message'];
    }

    return 'success';
}

function puqMikrotikVPN_resetConnection($params) {

  $data = array();
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/active/'.$params['username'], 'DELETE');
  if($curl['error']){
    return 'Error: ' . $curl['error'] . '| Message' . $curl['message'] . '|' . $curl['detail'];
  }
  return 'success';

}


function puqMikrotikVPN_AdminCustomButtonArray() {
  $buttonarray = array(
      'Reset connection' => 'resetConnection',
  );
  return $buttonarray;
}

function puqMikrotikVPN_SuspendAccount($params) {

  $data = array(
      'disabled'=> 'yes',
  );
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/secret/'.$params['username'], 'PATCH');
  if(!$curl){
    return 'API problem';
  }
  if($curl['error']){
    return 'Error: ' . $curl['error'] . '| Message' . $curl['message'] . '|' . $curl['detail'];
  }

  puqMikrotikVPN_resetConnection($params);
  return 'success';
}

function puqMikrotikVPN_UnsuspendAccount($params) {

  $data = array(
      'disabled'=> 'no',
  );
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/secret/'.$params['username'], 'PATCH');
  if(!$curl){
    return 'API problem';
  }
  if($curl['error']){
    return 'Error: ' . $curl['error'] . '| Message' . $curl['message'] . '|' . $curl['detail'];
  }
  return 'success';
}


function puqMikrotikVPN_TerminateAccount($params) {

  $data = array();
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/secret/'.$params['username'], 'DELETE');
  if($curl['error']){
    return 'Error: ' . $curl['error'] . '| Message' . $curl['message'] . '|' . $curl['detail'];
  }

  puqMikrotikVPN_apiCurl($params,$data,'/queue/simple/'.$params['username'], 'DELETE');
  puqMikrotikVPN_resetConnection($params);

  return 'success';

}

function puqMikrotikVPN_ChangePassword($params) {

  $username = $params['username'];
  $password = $params['password'];

  $data = array(
      'password' => $password,
  );
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/secret/'.$username, 'PATCH');
  if(!$curl){
    return 'API problem';
  }
  if($curl['error']){
    return 'Error: ' . $curl['error'] . '| Message' . $curl['message'] . '|' . $curl['detail'];
  }
  puqMikrotikVPN_resetConnection($params);
  return 'success';

}

function puqMikrotikVPN_ChangePackage($params) {
  puqMikrotikVPN_TerminateAccount($params);
  puqMikrotikVPN_CreateAccount($params);
}

function puqMikrotikVPN_loadLangPUQ($params) {

  $lang = $params['model']['client']['language'];

  $langFile = dirname(__FILE__) . "/lang/" . $lang . ".php";
  if (!file_exists($langFile))
    $langFile = dirname(__FILE__) . "/lang/" . ucfirst($lang) . ".php";
  if (!file_exists($langFile))
    $langFile = dirname(__FILE__) . "/lang/english.php";

  require dirname(__FILE__) . '/lang/english.php';
  require $langFile;

  return $_LANG_PUQ;
}


function puqMikrotikVPN_ClientArea($params) {
  $lang = puqMikrotikVPN_loadLangPUQ($params);

  $data = array();
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/active/'.$params['username'], 'GET');
  if($curl){
    return array(
        'templatefile' => 'clientarea',
        'vars' => array(
            'lang' => $lang,
            'params'=> $params,
            'curl' => $curl
        ),
    );
  }
  return 'API problem';
}


function puqMikrotikVPN_AdminServicesTabFields($params) {
  $data = array();
  $curl = puqMikrotikVPN_apiCurl($params,$data,'/ppp/active/'.$params['username'], 'GET');

  if($curl['error']){
    $fieldsarray = array(
        'API Connection Status' => '<div class="successbox">API Connection OK</div>',
        'Connection information' => 'NOT ONLINE',
    );
  }
  if(!$curl){
    $fieldsarray = array('API Connection Status' => '<div class="errorbox">API connection problem.</div>');
  }

  if($curl['.id']){
    $fieldsarray = array(
        'API Connection Status' => '<div class="successbox">API Connection OK</div>',
        'Connection information' =>
            '<table style="width:30%">

    <tr>
    <td><b>Comment:</b></td>
    <td>' . $curl['comment'] . '</td>
    </tr>

    <tr>
    <td><b>Service:</b></td>
    <td>' . $curl['service'] . '</td>
    </tr>

    <tr>
    <td><b>Name:</b></td>
    <td>' . $curl['name'] . '</td>
    </tr>
    
    <tr>
    <td><b>Caller-id:</b></td>
    <td>' . $curl['caller-id'] . '</td>
    </tr>
        
    <tr>
    <td><b>Address:</b></td>
    <td>' . $curl['address'] . '</td>
    </tr>

    <tr>
    <td><b>Uptime:</b></td>
    <td>' . $curl['uptime'] . '</td>
    </tr>
    </table>'
    );
  }
  return $fieldsarray;
}
?>


File: /README.md
# PUQ_WHMCS-Mikrotik-VPN

Module for the WHMCS system.
For manage Mikrotik secrets users as a product VPN.

Functions:

- Auto create and deploy produkt VPN
- Only Mikrotik API using
- Multilanguage

Admin area:

- Create users
- Suspend users
- Terminate users
- Unsuspend users
- Change the VPN users password
- Change Package
- VPN connection status
- Reset Connection

Client area:

- Change the VPN password
- VPN connection status

---------------------------------------------------------------
Testing:

WHMCS: 8.1.3

Mikrotik: CHR 7.3.1

--------------------------------------------------------------
### WHMCS part setup guide
1. ```git clone https://github.com/PUQ-sp-z-o-o/PUQ_WHMCS-Mikrotik-VPN.git```
2. Copy "puqMikrotikVPN" to "WHMCS_WEB_DIR/modules/servers/"

2. Create new server Mikrotik in WHMCS (System Settings->Products/Services->Servers)  
- Hostname: Mikrotik DNS (vpn.xxxxx.xxx)
- Module: PUQ Mikrotik VPN
- Assigned IP Addresses: pool of IP address for VPN users (One per line)	
- Username: Mikrotik admin user
- Password: Mikrotik admin user password
- Port 443 (not 8729)


3. Create a new Products/Services
- Module Settings/Module Name: PUQ Mikrotik VPN

### Mikrotik part setup guide
Enabling HTTPS
Create your own root CA on your router
```
/certificate
add name=LocalCA common-name=LocalCA key-usage=key-cert-sign,crl-sign
```
Sign the newly created CA certificate
```
/certificate
sign LocalCA
```
Create a new certificate for Webfig (non-root certificate)
```
/certificate
add name=Webfig common-name=XXX.XXX.XXX.XXX
```
Sign the newly created certificate for Webfig
```
/certificate
sign Webfig ca=LocalCA 
```
Enable www-ssl and specify to use the newly created certificate for Webfig
```
/ip service
set www-ssl certificate=Webfig disabled=no
```
Enable api-ssl and specify to use the newly created certificate for Webfig
```
 /ip service 
 set api-ssl certificate=Webfig disabled=no 
```


