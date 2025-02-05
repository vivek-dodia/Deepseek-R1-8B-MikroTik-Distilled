# Repository Information
Name: mikrotik-2fa-vpn

# Directory Structure
Directory structure:
└── github_repos/mikrotik-2fa-vpn/
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
    │   │       ├── pack-783decdccfe1dc5830cd9173000ee1f0713f8d75.idx
    │   │       └── pack-783decdccfe1dc5830cd9173000ee1f0713f8d75.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── DhcpDynamicLeaseScript.lua
    ├── NotakeyFunctions.lua
    ├── NtkUsageExample.lua
    ├── PppProfileScript.lua
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
	url = https://github.com/notakey/mikrotik-2fa-vpn.git
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
0000000000000000000000000000000000000000 cfe50acceec7aacc16d0cd5a709bc83626ab6a44 vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/notakey/mikrotik-2fa-vpn.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 cfe50acceec7aacc16d0cd5a709bc83626ab6a44 vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/notakey/mikrotik-2fa-vpn.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 cfe50acceec7aacc16d0cd5a709bc83626ab6a44 vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/notakey/mikrotik-2fa-vpn.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
cfe50acceec7aacc16d0cd5a709bc83626ab6a44 refs/remotes/origin/master


File: /.git\refs\heads\master
cfe50acceec7aacc16d0cd5a709bc83626ab6a44


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /DhcpDynamicLeaseScript.lua
#
# This script runs when new DHCP clients register and request authorization for dynamic clients.
# If authorization is provided, a static lease is created and no more autorization is requested for
# further client connections.
# To install, copy script into DHCP server lease script field.
#
{
    :local dynLease [ /ip dhcp-server lease get [/ip dhcp-server lease find mac-address="$leaseActMAC"] dynamic ];
    :if ($dynLease) do={
        :if ($leaseBound = "1") do={
            :local hostName [/ip dhcp-server lease get [/ip dhcp-server lease find mac-address="$leaseActMAC"] host-name ];

            :if ($hostName."test" = "test") do={
                :set hostName "no hostname"
            }

            # Block traffic to router from this DHCP address
            # Remove old address, previously blocked, just in case
            /ip firewall filter remove [/ip firewall filter find where comment="auto-dhcp-rule-$leaseServerName-$leaseActIP"]
            /ip firewall filter add action=reject chain=input src-address="$leaseActIP" reject-with=icmp-admin-prohibited comment="auto-dhcp-rule-$leaseServerName-$leaseActIP"

            /system script run "JParseFunctions";
            :global JSONUnload;

            /system script run "NotakeyFunctions";
            :global NtkAuthRequest;
            :global NtkWaitFor;
            :global NtkUnload;

            # Change values below to match your Notakey installation
            # ntkHost - https hostname of Notakey Authentication Server (NtkAS)
            :local ntkHost "demo.notakey.com";
            # Change to your Notakey username
            :local ntkUser "mainadmin"
            # ntkAccessId - service ID of NtkAS, can be seen in settings
            :local ntkAccessId "12345645-b32b-4788-a00d-251cd7dc9a03";
            # Custom message in authentication request
            :local authDescMsg "Allow access to for $hostName with MAC $leaseActMAC and IP $leaseActIP\?";
            :local authTitleMsg "New DHCP client"

            :local ntkAuthUuid ([$NtkAuthRequest host=$ntkHost accessId=$ntkAccessId authUser=$ntkUser authTitle=$authTitleMsg authDesc=$authDescMsg authTtl=7200]);

            :if ([$NtkWaitFor uuid=$ntkAuthUuid host=$ntkHost accessId=$ntkAccessId]) do={
                # Remove blocking rule after successful 2FA autehntication
                /ip firewall filter remove [/ip firewall filter find where comment="auto-dhcp-rule-$leaseServerName-$leaseActIP"]
                /ip dhcp-server lease make-static [ /ip dhcp-server lease find where address="$leaseActIP" ]
            } else={
                :log info "DHCP client with MAC $leaseActMAC forbidden access by $ntkUser";
            }

            $NtkUnload
            $JSONUnload
        }
    }
}

File: /NotakeyFunctions.lua
#
# Creates a new authentication request to NAS for specified user
# Params:
#   host - hostname of NAS server
#   accessId - ID of NAS service, can be found in NAS dashboard
#   authUser - username that will receive approval request
#
:global NtkAuthRequest;
if (!any $NtkAuthRequest) do={ :global NtkAuthRequest do={
    :do {
        # API request response payload
        :local content;
        # Auth request UUID
        :local uuid;

        :global JSONLoads;
        :if ([:len $JSONLoads] = 0) do={
            :log error "NotakeyFunctions: JSONLoads empty, have you loaded JParseFunctions?";
            :put "ERROR JSONLoads empty, have you loaded JParseFunctions?";
            :error "ERROR JSONLoads empty, have you loaded JParseFunctions?";
        }

        :if (([:len $host] = 0) || ([:len $authUser] = 0) || ([:len $accessId] = 0)) do={
            :log error "NotakeyFunctions: One or more required params empty, please pass host,accessId,authUser params";
            :put "ERROR One or more required params empty, please pass host,accessId,authUser params";
            :error "ERROR One or more required params empty, please pass host,accessId,authUser params";
        }

        :local lauthTitle $authTitle;
        :local lauthDesc $authDesc;
        :local lauthTtl $authTtl;
        :local lauthFingerprint $authFingerprint;
        :local lauthUser;

        :if ([:len $lauthDesc] = 0) do={
            :set lauthDesc "Do you wish to proceed with authentication as user $authUser?";
        }

        :if ([:len $lauthTitle] = 0) do={
            :set lauthTitle "MikroTik Authentication";
        }

        :if ([:len $lauthFingerprint] = 0) do={
            :set lauthFingerprint $lauthDesc;
        }

        :if ([:len $lauthTtl] = 0) do={
            :set lauthTtl 300;
        }

        # Urlencode username
        :for i from=0 to=([:len $authUser] - 1) do={
            :local char [:pick $authUser $i];

            :if ($char = " ") do={
                :set $char "%20";
            }

            :if ($char = "/") do={
                :set $char "%2F";
            }

            :if ($char = "@") do={
                :set $char "%40";
            }

            :if ($char = ":") do={
                :set $char "%3A";
            }

            :set lauthUser ($lauthUser . $char);
        }

        :local result [/tool fetch mode=https url="https://$host/api/v2/application/$accessId/application_user/$lauthUser/auth_request" http-header-field="Content-type: application/json" http-method=post http-data="{\"action\": \"$lauthTitle\", \"description\": \"$lauthDesc\", \"ttl_seconds\": \"$lauthTtl\", \"fingerprint\": \"$lauthFingerprint\"}" as-value output=user];

        :if ($result->"status" != "finished") do={
            :log error "NotakeyFunctions: Notakey auth request creation request failed";
            :put "ERROR Notakey auth request creation request failed";
            :error "ERROR Notakey auth request creation request failed";
        }

        :set content ($result->"data");
        :set uuid ([$JSONLoads $content]->"uuid");
        # Clear payload contents
        :set content;

        :if ([:len $uuid] = 0) do={
            :log error "NotakeyFunctions: Notakey UUID missing";
            :put "ERROR Notakey UUID missing, have you loaded JParseFunctions?";
            :error "ERROR Notakey UUID missing, have you loaded JParseFunctions?";
        }

        :log info "NotakeyFunctions: Notakey Auth request $uuid created";
        :put "Notakey Auth request $uuid created";
        :return $uuid;
    } on-error={
        :log error "NotakeyFunctions: Notakey Auth request send error";
        :put "ERROR Notakey Auth request send error";
        :return false;
    }
}}

#
# Waits until specified auth request identified by uuid is approved or rejected or expires
# Params:
#   host - hostname of NAS server
#   uuid - ID of auth request, returned by NtkAuthRequest
#   accessId - ID of NAS service, can be found in NAS dashboard
#
:global NtkWaitFor;
if (!any $NtkWaitFor) do={ :global NtkWaitFor do={
    :do {
        :local hasResponse false;
        :local responseType "null";
        :local requestExpired false;
        :local content;

        :global JSONLoads;
        :if ([:len $JSONLoads] = 0) do={
            :log error "NotakeyFunctions: JSONLoads empty, have you loaded JParseFunctions?";
            :put "ERROR JSONLoads empty, have you loaded JParseFunctions?";
            :error "ERROR JSONLoads empty, have you loaded JParseFunctions?";
            :return false;
        }

        :if (([:len $host] = 0) || ([:len $uuid] = 0) || ([:len $accessId] = 0)) do={
            :log error "NotakeyFunctions: One or more required params empty, please pass host,accessId,uuid params";
            :put "ERROR One or more required params empty, please pass host,accessId,uuid params";
            :error "ERROR One or more required params empty, please pass host,accessId,uuid params";
            :return false;
        }

        :do {
            :local result [/tool fetch mode=https url="https://$host/api/v2/application/$accessId/auth_request/$uuid" http-header-field="Content-type: application/json" http-method=get as-value output=user];
            :set content ($result->"data");
            :set responseType ([$JSONLoads $content]->"response_type");
            :local requestExpired ([$JSONLoads $content]->"expired");
            # Clear payload contents
            :set content;

            :put ("Check $uuid status, response: $responseType, expired: $requestExpired")
            :if ([:len $responseType] > 0) do={
                :set hasResponse true;
            }

            :if ($requestExpired) do={
                :set hasResponse true;
            }

            :delay 2;
        } while=( $hasResponse = false )

        :if ($requestExpired) do={
            :log warn "NotakeyFunctions: Notakey Auth request expired with no response";
            :put "ERROR Notakey Auth request expired with no response";
            :error "Notakey Auth request expired with no response";
        }

        :if ($responseType = "ApproveRequest") do={
            :log info "NotakeyFunctions: Notakey Auth request $uuid approved";
            :put "Notakey Auth request $uuid approved";
            :return true;
        }

        :log info "NotakeyFunctions: Notakey Auth request $uuid denied";
        :put "Notakey Auth request $uuid denied";
        :return false;
    } on-error={
        :log error "NotakeyFunctions: Notakey Authentication procedure not successful";
        :put "ERROR Authentication procedure not successful";
        :return false;
    }
}}

#
# Unloads Notakey gobal functions
#
:global NtkUnload;
if (!any $NtkUnload) do={ :global NtkUnload do={
    :global NtkWaitFor;
    :set NtkWaitFor;
    :global NtkAuthRequest;
    :set NtkAuthRequest;
    :global NtkUnload;
    :set NtkUnload;
}}


File: /NtkUsageExample.lua
{
    :local localAddr $"local-address";
    :local remoteAddr $"remote-address";
    :local callerId $"caller-id";
    :local calledId $"called-id";

    /system script run "JParseFunctions";
    :global JSONUnload;

    /system script run "NotakeyFunctions";
    :global NtkAuthRequest;
    :global NtkWaitFor;
    :global NtkUnload;

    :log info "$user (srcIp=$callerId, dstIp=$calledId) connected: was given $remoteAddr IP (GW $localAddr)";

    # Change values below to match your Notakey installation
    # ntkHost - https hostname of Notakey Authentication Server (NtkAS)
    :local ntkHost "demo.notakey.com";

    # ntkAccessId - service ID of NtkAS, can be seen in settings
    :local ntkAccessId "12345645-b32b-4788-a00d-251cd7dc9a03";

    # Custom message in authentication request
    :local authDescMsg "Log in as $user from $callerId\?";

    :local ntkAuthUuid ([$NtkAuthRequest host=$ntkHost accessId=$ntkAccessId authUser=$user authTitle="VPN connection" authDesc=$authDescMsg authTtl=60]);

    :if ([$NtkWaitFor uuid=$ntkAuthUuid host=$ntkHost accessId=$ntkAccessId]) do={
        :log info "VPN 2FA authentication success for user $user from IP $callerId ($remoteAddr)";
        # Removes user IP from 2fa_pending access list (configure access list in PPP profile)
        /ip firewall address-list remove [/ip firewall address-list find where list=2fa_pending address=$remoteAddr]
    } else={
        :log info "VPN 2FA authentication failure for user $user from IP $callerId";
        # Disconnect active session with this IP and user
        /ppp active remove [/ppp active find name="$user" address="$remoteAddr"]
    }

    $NtkUnload
    $JSONUnload
}


File: /PppProfileScript.lua
# OnUp script
{
    :local localAddr $"local-address";
    :local remoteAddr $"remote-address";
    :local callerId $"caller-id";
    :local calledId $"called-id";

    :log info "$user (srcIp=$callerId, dstIp=$calledId) connected: was given $remoteAddr IP (GW $localAddr)";

    /system script run "JParseFunctions";
    :global JSONUnload;

    /system script run "NotakeyFunctions";
    :global NtkAuthRequest;
    :global NtkWaitFor;
    :global NtkUnload;

    # Change values below to match your Notakey installation

    # ntkHost - https hostname of Notakey Authentication Server (NtkAS)
    :local ntkHost "demo.notakey.com";

    # ntkAccessId - service ID of NtkAS, can be seen in settings
    :local ntkAccessId "12345645-b32b-4788-a00d-251cd7dc9a03";

    # Custom message in authentication request
    :local authDescMsg "Log in as $user from $callerId\?";

    :local ntkAuthUuid ([$NtkAuthRequest host=$ntkHost accessId=$ntkAccessId authUser=$user authTitle="VPN connection" authDesc=$authDescMsg authTtl=60]);

    :if ([$NtkWaitFor uuid=$ntkAuthUuid host=$ntkHost accessId=$ntkAccessId]) do={
        :put "All cool, we are letting you in";
        # Remove blocking rule after successful 2FA autehntication
        /ip firewall address-list remove [/ip firewall address-list find where list=vpn_pending address=$remoteAddr]
    } else={
        :log info "VPN 2FA authentication failure for user $user from IP $callerId";
        # Disconnect active session with this IP and user
        /ppp active remove [/ppp active find name="$user" address="$remoteAddr"]
    }

    $NtkUnload
    $JSONUnload
}

# OnDown script
{
    # Just logs the disconnect event, not in use right now

    :local localAddr $"local-address";
    :local remoteAddr $"remote-address";
    :local callerId $"caller-id";
    :local calledId $"called-id";

    :log info "$user (srcIp=$callerId, dstIp=$calledId) logged out: was given $remoteAddr IP (GW $localAddr)";
}

File: /README.md
# MikroTik client library for Notakey two factor authentication

Allows to integrate push notification based two factor authentication using Notakey Authenticator mobile app
for iOS or Android in various MikroTik workflows, mainly targeted for VPN strong authentication.

Note that you will need additional firewall or routing setup to use this solution to approve authentication
from the same device as the VPN is initiated on, e.g. start vpn and approve from the same device.

## Installation

* Install JParseFunctions library
  - Create JParseFunctions script on your MikroTik router (no privilledges required)
  - Copy contents from [JParseFunctions.lua](https://github.com/Winand/mikrotik-json-parser/raw/master/JParseFunctions) file into this script

* Install NotakeyFunctions library
  - Create NotakeyFunctions script on your MikroTik router (no privilledges required)
  - Copy contents from NotakeyFunctions.lua file in this repository into this script

* Enable two factor authentication inside PPP profile that your VPN service uses (usually default-encryption)
  - Copy Up and Down scripts from PppProfileScript.lua into profile
  - Adjust Notakey Autehntication Server parameters (ntkHost & ntkAccessId)
  - Adjust firewall rules according to your setup

## Generic usage example
```
{
    # Load dependencies first
    /system script run "JParseFunctions";
    :global JSONUnload;

    # Load Notakey function library
    /system script run "NotakeyFunctions";
    :global NtkAuthRequest;
    :global NtkWaitFor;
    :global NtkUnload;

    # Set Notakey Authentication Server params
    :local ntkHost "demoapi.notakey.com";
    :local ntkAccessId "12345645-b32b-4788-a00d-251cd7dc9a03";
    :local ntkUser "demo";

    # Send autehntication request to mobile device
    :local ntkAuthUuid ([$NtkAuthRequest host=$ntkHost accessId=$ntkAccessId authUser=$ntkUser]);

    # Wait for response from mobile
    :if ([$NtkWaitFor uuid=$ntkAuthUuid host=$ntkHost accessId=$ntkAccessId]) do={
        :put "All cool, we are letting you in";
    }else={
        :put "Auth expired or denied"
    }

    # Unload global function references
    $NtkUnload
    $JSONUnload
}
```

This script can be copied into MikroTik Terminal shell to test the functionality of scripts. Please remember to adjust Authentication Server params.

## Dependencies:

* JParseFunctions [https://github.com/Winand/mikrotik-json-parser]
* Hosted or on-premises Notakey Authentication Appliance installation
* iOS or Android device with onboarded service
* Username in onboarded service must match the one used for VPN authentication
* Fairly modern RouterOS >= v6.46.4

## Limitations

* Due to limitations of JParseFunctions library, you cannot use parentheses and possibly other special punctuation in authentication requests

## Links

* Documentation [https://documentation.notakey.com/]
* Contact [https://notakey.com/]
* Support [support@notakey.com]


