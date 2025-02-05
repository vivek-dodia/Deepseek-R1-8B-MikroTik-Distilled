# Repository Information
Name: mikrotik_EAP

# Directory Structure
Directory structure:
└── github_repos/mikrotik_EAP/
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
    │   │       ├── pack-6d7b225c4cfe378c522ae07144a1c9598d4ae2b8.idx
    │   │       └── pack-6d7b225c4cfe378c522ae07144a1c9598d4ae2b8.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
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
	url = https://github.com/multiduplikator/mikrotik_EAP.git
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
0000000000000000000000000000000000000000 7e1c5a5468a95ed9dd525d5ca81292e6e0bb268f vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/multiduplikator/mikrotik_EAP.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 7e1c5a5468a95ed9dd525d5ca81292e6e0bb268f vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/multiduplikator/mikrotik_EAP.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7e1c5a5468a95ed9dd525d5ca81292e6e0bb268f vivek-dodia <vivek.dodia@icloud.com> 1738605971 -0500	clone: from https://github.com/multiduplikator/mikrotik_EAP.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
7e1c5a5468a95ed9dd525d5ca81292e6e0bb268f refs/remotes/origin/main


File: /.git\refs\heads\main
7e1c5a5468a95ed9dd525d5ca81292e6e0bb268f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /README.md
# mikrotik EAP-TLS and EAP-PEAP (ROS6 classic or ROS7 with User Manager V5) 

We are going to do this in the following steps
- [Step 1: ROS6 and ROS7](#step-1-ros6-and-ros7)
  - [Enable CRL](#enable-crl)
- [Step 2a: ROS6](#step-2a-ros6)
  - [Create CA and certificates](#ros6---create-ca-and-certificates)
  - [Setup wireless AP](#ros6---setup-wireless-ap)
- [Step 2b: ROS7](#step-2b-ros7)
  - [Create CA and certificates](#ros7---create-ca-and-certificates)
  - [Setup User Manager](#ros7---setup-usermanager)
  - [Setup wireless AP](#ros7---setup-wireless-ap)
- [Step 3: ROS6 and ROS7](#step-3-ros6-and-ros7)
  - [Setup wireless client with EAP-TLS](#setup-wireless-client-with-eap-tls)
  - [Setup wireless client with EAP-PEAP](#setup-wireless-client-with-eap-peap)


We assume RouterOS is on 10.0.0.1 and APs are managed via CAPsMAN. And you are somewhat familiar with Mikrotik stuff.

## Step 1: ROS6 and ROS7

### Enable CRL

By default on recent RouterOS versions, CRL is disabled. In order to be able to revoke certificates later and effectively bar clients from connecting, CRL on RouterOS has to be enabled. In our use case, we dont need the CRL download feature.

As a side note, in case you want to use freeradius, you have to enable www service, so the freeradius server can download the CRL from RouterOS. Inspect a certificate to find the exact download URL to use. If you want RouterOS itself to download external CRLs, you have to enable the CRL Download feature.

```
/certificate settings
set crl-use=yes
```

Now, continue either with Step 2a or with Step 2b.

## Step 2a: ROS6

This setup gives us EAP-TLS only. EAP-PEAP has to be implemented with a sidecar radius server like freeradius (see Final Remarks). You might want to consider to split the wireless networks into one that does EAP-TLS and another one that does EAP passthrough to e.g. freeradius which does the EAP-PEAP.

### ROS6 - Create CA and certificates

This can also be done outside of RouterOS, but this way it is pretty convenient.

```
/certificate add name=RouterCA common-name=Router subject-alt-name=IP:10.0.0.1 key-size=4096 days-valid=3650 key-usage=crl-sign,key-cert-sign
/certificate sign RouterCA ca-crl-host=10.0.0.1 name=RouterCA
# for import as wireless network certificate or trusted root certification authority on client
/certificate export-certificate RouterCA type=pem

/certificate add name=EAP_AP common-name=EAP_AP subject-alt-name=IP:10.0.0.1 key-size=4096 days-valid=3650 key-usage=digital-signature,key-encipherment,tls-server
/certificate sign EAP_AP ca=RouterCA name=EAP_AP
/certificate set EAP_AP trusted=yes
# no export needed

/certificate add name=EAP_Client common-name=EAP_Client key-size=4096 days-valid=3650 key-usage=tls-client
/certificate sign EAP_Client ca=RouterCA name=EAP_Client
/certificate set EAP_Client trusted=yes
# for import as wireless network certificate or user certificate on client
/certificate export-certificate EAP_Client type=pkcs12 export-passphrase=<your_long_passphrase_goes_here>
```

The exported files should be:

```
cert_export_RouterCA.crt -> for deploying the client
cert_export_EAP_Client.p12 -> for deploying the client
```

### ROS6 - Setup wireless AP

We assume that we already have a working CAPsMAN setup and provisioned the AP with a security profile.

Create a new security profile.

```
/caps-man/security add name="security_eap-tls" authentication-types=wpa2-eap encryption=aes-ccm group-encryption=aes-ccm eap-methods=eap-tls tls-mode=verify-certificate-with-crl tls-certificate=EAP_AP
```

Now change the respective configuration for the AP to use the new profile and provision.

## Step 2b: ROS7

This setup gives us EAP-TLS and EAP-PEAP and it can be done on a given wireless network simultaneously. It is crucial to use secp384r1 and sha384 with the certificates. Otherwise, you will run into trouble with Android devices trying to use the anonymous identity, causing a user not found error in Usermanager (at least on ROS 7.1.1).

### ROS7 - Create CA and certificates

Again, this can also be done outside of RouterOS, but this way it is pretty convenient. For the client certificates, it seems that the validity period should not be more than 825 days.

```
# Generating a Certificate Authority
/certificate
add name=RouterCA common-name=Router subject-alt-name=IP:10.0.0.1 key-size=secp384r1 digest-algorithm=sha384 days-valid=1825 key-usage=key-cert-sign,crl-sign
sign RouterCA ca-crl-host=10.0.0.1 name=RouterCA

# Generating a server certificate for User Manager
add name=EAP_AP common-name=EAP_AP subject-alt-name=IP:10.0.0.1 key-size=secp384r1 digest-algorithm=sha384 days-valid=730 key-usage=tls-server
sign EAP_AP ca=RouterCA name=EAP_AP
set EAP_AP trusted=yes

# Generating a client certificate
add name=EAP_Client common-name=EAP_Client days-valid=730 key-size=secp384r1 digest-algorithm=sha384 key-usage=tls-client 
sign EAP_Client ca=RouterCA name=EAP_Client
set EAP_Client trusted=yes

# Exporting the public key of the CA as well as the generated client private key and certificate for distribution to client device
export-certificate RouterCA
export-certificate EAP_Client type=pkcs12 export-passphrase=<your_long_passphrase_goes_here>
```

The exported files should be:

```
cert_export_RouterCA.crt -> for deploying the client
cert_export_EAP_Client.p12 -> for deploying the client
```

### ROS7 - Setup Usermanager

The User Manger serves as the radius server that does the EAP stuff, using the EAP_AP certificate. We enable the router to do radius auth, adjust the user groups to provide one for EAP-TLS and another one for EAP-PEAP. Users with certificate go into the first group, having the same name as the common name of their certificate. Users that do EAP-PEAP go into the second group. Also, we allow for more than one device/connection to share a given user.

```
# Enabling User Manager and specifying, which certificate to use
/user-manager
set enabled=yes certificate=EAP_AP

# Adding access points
/user-manager router
add name=Router address=10.0.0.1 shared-secret=<your_long_shared_secret_goes_here>
# Limiting allowed authentication methods
/user-manager user group
set [find where name=default] outer-auths=eap-peap inner-auths=peap-mschap2
add name=certificate-authenticated outer-auths=eap-tls
# Adding users
/user-manager user
add name=EAP_Client group=certificate-authenticated shared-users=3
add name=SomeUser group=default password=<users_password_goes_here> shared-users=2
```

### ROS7 - Setup wireless AP

We assume that we already have a working CAPsMAN setup and provisioned the AP with a security profile. In ROS6 we did EAP direct against the certificate store. Now, in ROS7, we do it as passthrough to the User Manager. 

To make the passthrough work, we have to create an entry in the RADIUS configuration, that links to the User Manager

```
/radius add address=10.0.0.1 secret=<your_long_shared_secret_goes_here> service=wireless timeout=1s
```

Now, create a new security profile that does the actual passthrough.

```
/caps-man/security add name="security_eap-tls" authentication-types=wpa2-eap encryption=aes-ccm group-encryption=aes-ccm eap-methods=passthrough
```

Now change the respective configuration for the AP to use the new profile and provision.

## Step 3: ROS6 and ROS7

### Setup wireless client with EAP-TLS

For Windows (WIN), Android (AND) and iOS clients, you simply import the following two files

```
cert_export_RouterCA.crt
-> WIN: double click to install and specify to go into trusted root certification authorities (current user or local machine)
-> AND: install network certificate in advanced wireless settings
-> IOS: https://apple.stackexchange.com/questions/326208/how-do-i-configure-an-ipad-to-use-eap-tls

cert_export_EAP_Client.p12
-> WIN: double click to install (current user)
-> AND: as above with .crt
-> IOS: as above with .crt
```

From here, you can configure the respective device to use your imported CA and certificate. WIN and IOS usually autoselect when trying to connect. AND needs manual configuration.

### Setup wireless client with EAP-PEAP

In case you have ROS6, you have to implement EAP-PEAP via passthrough to a sidecar radius server, e.g. freeradius. This works with a dedicated wireless network that does the passthrough.

In case you have ROS7 and User Manager, you can do EAP-PEAP on the same wireless network, using the user/password combination as created in the default group above, i.e. username as "SomeUser" and password as "<users_password_goes_here>" - leaving the anonymous_identity blank.

This mode is particularly usefull for Chromebooks that are remote administered, and where you cannot install certificates permanently.

### Sidenote on WPA3 and Android 11+
We are on the advent of WPA3 and Android 11+ now starts to enforce section 5.1:
"The STA is configured with EAP credentials that explicitly specify a CA root certificate that matches the root certificate in the received Server Certificate message and, if the EAP credentials also include a domain name (FQDN or suffix-only), it matches the domain name (SubjectAltName DNSName if present, otherwise SubjectName CN) of the certificate [2] in the received Server Certificate message."

In somewhat simpler terms, this reads:
"The new Domain field in the wifi config dialog must be the CN or subjectAlternateName of the server certificate." 

Hence (esp. when setting up Androind 11+ wireless clients), make sure that you use the CN of the EAP_AP certificate as Domain field entry - in our scenario that would be "EAP_AP" - when setting up the client. Alternatively, you can add an additional "subject-alt-name=DNS:eap.ap.local" when creating the EAP_AP certificate and respectively use "eap.ap.local" as Domain field entry.

## Final remarks

Before deploying for real, make sure you check revokation works as expected, since you cannot delete certificates anymore (unless you remove all of them together with the CA).

It is relatively simple to exted the above to also provide EAP-TTLS support. ROS6 again via sidecar radius server, ROS7 via the Usermanager and its groups settings inner-auth/outer-auth.

Be aware, that you might struggle to use eapol_test with the ROS7 approach. At least I did not spent enough time to get it to work with the secp384r1 being a 384-bit prime field Weierstrass curve. 

Some links that might come in handy:

- ROS7
  - https://help.mikrotik.com/docs/display/ROS/Enterprise+wireless+security+with+User+Manager+v5

- ROS6
  - https://wiki.mikrotik.com/wiki/Manual:Wireless_EAP-TLS_using_RouterOS_with_FreeRADIUS
  - https://www.nkent.us/wiki/index.php/Wireless_networking_with_CAPsMAN_and_the_MikroTik_cAP_ac
  - https://serverfault.com/questions/986375/mikrotik-eap-tls-wifi-config-using-certificates


