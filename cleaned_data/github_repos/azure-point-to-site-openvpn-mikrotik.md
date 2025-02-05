# Repository Information
Name: azure-point-to-site-openvpn-mikrotik

# Directory Structure
Directory structure:
└── github_repos/azure-point-to-site-openvpn-mikrotik/
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
    │   │       ├── pack-b6b2f877caaa9e782604dce586c4c4fc92c4bee6.idx
    │   │       └── pack-b6b2f877caaa9e782604dce586c4c4fc92c4bee6.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── ca.crt
    ├── client.crt
    ├── client.key
    ├── client.ovpn
    ├── Deployment-Microsoft.VirtualNetwork-20201206160544/
    │   └── deployment.json
    ├── keyinstrcutions.txt
    ├── README.md
    └── secret


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
	url = https://github.com/MischaOputa/azure-point-to-site-openvpn-mikrotik.git
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
0000000000000000000000000000000000000000 a1eaa61537255783b22a41a8ff5d9f3b8999def0 vivek-dodia <vivek.dodia@icloud.com> 1738606372 -0500	clone: from https://github.com/MischaOputa/azure-point-to-site-openvpn-mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 a1eaa61537255783b22a41a8ff5d9f3b8999def0 vivek-dodia <vivek.dodia@icloud.com> 1738606372 -0500	clone: from https://github.com/MischaOputa/azure-point-to-site-openvpn-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a1eaa61537255783b22a41a8ff5d9f3b8999def0 vivek-dodia <vivek.dodia@icloud.com> 1738606372 -0500	clone: from https://github.com/MischaOputa/azure-point-to-site-openvpn-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
a1eaa61537255783b22a41a8ff5d9f3b8999def0 refs/remotes/origin/main


File: /.git\refs\heads\main
a1eaa61537255783b22a41a8ff5d9f3b8999def0


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /ca.crt
-----BEGIN CERTIFICATE-----
MIIDNjCCAh6gAwIBAgIIeK7XlEFxot8wDQYJKoZIhvcNAQELBQAwDTELMAkGA1UE
AwwCY2EwHhcNMjAxMjA2MjExNzE2WhcNMjExMjA2MjExNzE2WjANMQswCQYDVQQD
DAJjYTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM1B9e6x8COXCKVC
jDiW0530TejiDbJyRyr3EkYkvdVtMJFmp0q7o0mycVMktaKMAju8Q9CyYAHAMEcD
SC2FA2x/yAOLIk6OMnT6cNZ5sxPt/OKzFg96mI/I/vj5AmmqZS+F5i76aBUswDTd
8ZPxdNHViVUsLBkXxVH0t0UsmkKlhh9n7Nu/pzI+fZHNVQmnLGDjr7HzlTNSei2h
aiLuYY7SwcAUDoh9QVY4SeBHqElQbawIVuoHig6PWbnvLigIG+wWiUgT0uQKzQOJ
NQy4gb9BwAC/Jqcjxpru7Q9B821Vjhf3unRSVDOoRBfFpglIKFHGaEcENdaIGDHg
vecqvD8CAwEAAaOBmTCBljAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIB
BjAdBgNVHQ4EFgQUiorXg/foGw3INUQGub+xBW8Zm70wLgYDVR0fBCcwJTAjoCGg
H4YdaHR0cDovLzE5Mi4xNjguMC4xMC9jcmwvNC5jcmwwJAYJYIZIAYb4QgENBBcW
FUdlbmVyYXRlZCBieSBSb3V0ZXJPUzANBgkqhkiG9w0BAQsFAAOCAQEAq/aeUVxt
WBib8btFLCfQJKKxapir9lw3+9NYzfynD6FUPZU3QGm6rM6xGBut+2Bq4lRDFzvS
6I9Qw9BdY3ltmdFEaI4atx/IlUHumxhy63CMjGPDsugTl7mNjyqus6sD0IFG6ITN
hpmCNp5QY8ZtCTdi88IIchunDhPtqAKFHd85cpHfmVFMcpWOD7H0p75AIJFgY3R4
E6yedZ7lm1KptPcBM62/rljbmWbdZhJvgxwcE0k3vQVPjJFEpiUpkFBwsxzsuXP6
BvcBjuBP8brXlxQz++wkQR/9FUd0HxJ7VZ2cIFLT2F4jCa5H8jSL1Xuof2mTOPxx
Fet635qXhpbLpg==
-----END CERTIFICATE-----


File: /client.crt
-----BEGIN CERTIFICATE-----
MIIDHTCCAgWgAwIBAgIIBfw5CUqomXwwDQYJKoZIhvcNAQELBQAwDTELMAkGA1UE
AwwCY2EwHhcNMjAxMjA2MjEyMzM0WhcNMjExMjA2MjEyMzM0WjARMQ8wDQYDVQQD
DAZjbGllbnQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/d8tAkVk+
WXN5yqH/Auh8KJtJlhp46Up2wYp77oubK1htccSUKNz56c9HLNOqxth7TZ6rbvq/
H/bX/0tMMSK4/t0PojND7Ag4fYQeB42WVgauwgKZasghl4rfsCXc6qUEnh2AixkK
5/fnMPZNWQUYQx82KerYJ0WaVOIbUGhAiYX08eMlmbGvTZnbG+us8FkDaF5vn/UG
+OHctZM6oancdKCTYgiUUxymdWuaR5i8hftuCgDOcul9ht8GOizdNcPsIhcF9lfQ
OiLaO3qtWnUILomXxryWdEk2GEbJhKSm1bxV/kitDEwsn0McPxiZKtoErwgkcPlM
PRGabtYiFotdAgMBAAGjfTB7MBMGA1UdJQQMMAoGCCsGAQUFBwMCMB0GA1UdDgQW
BBQJcMOj72MvY8QL2knggCCL1Nx53zAfBgNVHSMEGDAWgBSKiteD9+gbDcg1RAa5
v7EFbxmbvTAkBglghkgBhvhCAQ0EFxYVR2VuZXJhdGVkIGJ5IFJvdXRlck9TMA0G
CSqGSIb3DQEBCwUAA4IBAQA7tpCWz6+JIUaru5fCnvVFA2G32hdXLohn89dbxzcB
YxD70S9y4TMLAt9dAzso4hlHyuYtkRfexroT9rC2oRRJjrifbxO3UGpa7lIvwTXK
WK/yMGGro21hhqEzBnMucIFkH7Yn1ICVPFCsTHOubCoKZnQ2R/fUJoPDHF6QP7z6
GcJw6cbxSA/RTaTTt/nutauoWi94CknfQsvzOlcuenxm9vcake8msLOL7hGPQK5G
iAcRO/t8utbooXzpeCNFyh4NcWMCWd44/oE/V5HMTMAHDlsI/Lc8ZUqJSBL/ioUi
HR7jtoZwvda3q2PiOXHqt/iQb2XycxhJaFIWjQpjGu21
-----END CERTIFICATE-----


File: /client.key
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFHzBJBgkqhkiG9w0BBQ0wPDAbBgkqhkiG9w0BBQwwDgQIFXueRvdD11wCAggA
MB0GCWCGSAFlAwQBKgQQUS9/xXR/y7vnf0VMxMFm6QSCBNDRFbWmdU+yFcTx06/A
0N3YLyp4J6FwOLxJEHtM2g4Nq1o3ZkHz5ErzLUOgEPd23LMrJYLUmoSOVNPU1Pfi
3FSMub9/EVgLJ5Ye5kGZQh8F2t+c6/IZOy+0cM5as/M3mAAkobeR3MGSH/aD39/t
5r+0x2a/097J+RKQ/7Vf0aADXl/kjt/S0xrP93RiN9+P4Y22WV8H1J6ZMSaWxU0C
z3w2c7je/LmbvgI2Trf9OzXdklx/gvXGhdmqihuiW8/EwVVSBkLtLAiwbL3UKMvp
XPyGv8AKnXt1eG3Eu3eb3suIJtlAl60xqOe1WoepF46TZMwhbQxUJyJqrCTUBef5
mXbgjmOPllrs/gtEyHlfTIw4OopW/lK4cmx1SEUKgUSIpjzDMzF8tyA4Iss0ZCIv
fEzHcfI3JPYXClpxjSCXyKMQjgQWxbwXuVkJcHJW3c0EmGsivkaIKPfRwUAd/jSR
26fw4ggLR7UjAEBtX77wu69OABBpMqbpXqrrqEJfZaB45PS/2Kg6APcJwwQJ/DNe
kBkwqbeth6wf+jQHZ5L2HLyct3hBIibc7povNm1qZnC4+JuxymhRuNx4QgMj3vEf
y4rWEIJOgYHMlLqCyOArxHEzFdJ0IzAPlvhh23u1EXNnR05O3WdCY4V40kG7Ci3b
U/dbTunNDxghiURZ8UCcyYnS7wMnonpdEaE4wOEouB/Rfz8vf5cnbSXsn6psmkCE
GXaJoD4DkNFIg5QrcIzQ888ioesP1nvt6jsStrHNyp6ImljXnVPOZvR2W344xRWg
rmVdbP7nYHDsHVz31+Lo0ThtOW6guXvibuGhDJEVDPyZakX6Ux1YUwcz7KNQNxoa
utxKIsD70pjERlkyqrAKd1/syqDZgi/tsrxKxyNBgws+SnSpqXhv8yvRdmZQz7Sn
2tawIRBybHt6BUZagLP1m/mIRS8q09Eu3ZUTCt79T057N4M4mKxVpq/de/3NZv0P
GAcfoiIPZDM1qRWs6AMg6kQruG8RwqJmOpEFPSVzZ13A/2jXbLiqmfYB1sJr0NJc
xcC6MCpHh4FURxmqNeMuiuS8iMzSu2v/KqgiBrj7ihjivITMF7HZBVHsz+Uv5EfX
pfSF/zSJLJ9uw9HbTzaJNlLynnuJ+Ey1U1dAHxG5f49rMWbkiBXXQfyLerpgy5qV
nSneKEdDUATCDSKFeUT4wniNtsHrIkEwHRqlRAuzhBm76FVYLHoLGORnE9O28mEs
Nj5IJewBZGIGsOpN/WFgt5eNcBl8aMRvbyqIQvSGcrr550vSA6yJwFL1nkthLZVW
RsKSSbXgcDwaqxFa73hZODRllL1KtBCUEymaWEW5+dCROuYMm5tjipP5X1j9VoP3
MTXducrA5Y/6BsFLxwNpyP8BF0OCybCxtt8rZ7xfYCQGp3dmlp08QTua1pyJGpTd
qIFozyJVoMXPRJuyS3kYKGv4uI03h8ygE0VCseJy7zfqpFqTCAmvw7IIu9NKFVmj
4be0oKhW1/WgpRRtpapPoiEVG4GNH6LbwG0hzfnhmYn1N8tEk6/20iuvTFNy5VR3
+zr3d7YWc0cBY6gQMinAH90HxYCfaxFEMu6fd4WzQyC9iknfWs+SuyH6XIocvo5f
YibfAvlnoett2N42HvZNDuGkiw==
-----END ENCRYPTED PRIVATE KEY-----


File: /client.ovpn
client
proto udp
remote 192.168.0/xx
dev tun
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
verify-x509-name "OpenVPN Server cert" name
auth SHA256
auth-nocache
cipher AES-128-CBC
tls-client
tls-version-min 1.2
tls-cipher TLS-DHE-RSA-WITH-AES-128-GCM-SHA256
setenv opt block-outside-dns
verb 3

<ca>
-----BEGIN CERTIFICATE-----

-----END CERTIFICATE-----
</ca>
<cert>

-----BEGIN CERTIFICATE-----

-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN PRIVATE KEY-----

-----END PRIVATE KEY-----
</key>
key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----

-----END OpenVPN Static key V1-----
</tls-auth>


File: /Deployment-Microsoft.VirtualNetwork-20201206160544\deployment.json
{
  "id": "xxxxxxxxx/VNResource/providers/xxx/deployments/Microsoft.VirtualNetwork-xxxxx",
  "name": "Microsoft.VirtualNetwork-20201206160544",
  "type": "Microsoft.Resources/deployments",
  "tags": {
    "primaryResourceId": "xxx/Vxxxxxxe/providers/Microsoft.Network/virtualNetworks/VN1",
    "marketplaceItemId": "Microsoft.VirtualNetwork-ARM"
  },
  "properties": {
    "templateHash": "30xxxxxxxx0133",
    "parameters": {
      "location": {
        "type": "String",
        "value": "westeurope"
      },
      "virtualNetworkName": {
        "type": "String",
        "value": "VN1"
      },
      "resourceGroup": {
        "type": "String",
        "value": "VNResource"
      },
      "addressSpaces": {
        "type": "Array",
        "value": [
          "10.0.0.0/16"
        ]
      },
      "ipv6Enabled": {
        "type": "Bool",
        "value": false
      },
      "subnetCount": {
        "type": "Int",
        "value": 1
      },
      "subnet0_name": {
        "type": "String",
        "value": "default"
      },
      "subnet0_addressRange": {
        "type": "String",
        "value": "10.0.0.0/24"
      },
      "ddosProtectionPlanEnabled": {
        "type": "Bool",
        "value": false
      },
      "firewallEnabled": {
        "type": "Bool",
        "value": false
      },
      "bastionEnabled": {
        "type": "Bool",
        "value": false
      }
    },
    "mode": "Incremental",
    "debugSetting": {
      "detailLevel": "None"
    },
    "provisioningState": "Succeeded",
    "timestamp": "2020-12-06T15:07:36.256857Z",
    "duration": "PT4.9503974S",
    "correlationId": "axxx45a5xxxxxx-a12e-9f21a33d7dca",
    "providers": [
      {
        "namespace": "Microsoft.Network",
        "resourceTypes": [
          {
            "resourceType": "VirtualNetworks",
            "locations": [
              "westeurope"
            ]
          }
        ]
      }
    ],
    "dependencies": [],
    "outputResources": [
      {
        "id": "/subscriptions/xxxxxxxxxxxxxxxxx/rexxxxxx/xxxxxxxxxxxxe/providers/Microsoft.Network/VirtualNetworks/VN1"
      }
    ],
    "validationLevel": "Template"
  }
}

File: /keyinstrcutions.txt
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
Create your own static key here (easy-peasy) https://openvpn.net/community-resources/static-key-mini-howto/
-----END OpenVPN Static key V1-----


File: /README.md
# azure-point-to-site-openvpn-mikrotik
create openvpn server on mikrotik create free azure account on azure create two linux ubuntu VMs in different virtual networks and create routing between them connect one of the VMs to vpn  
Assuming you have a routeros/Mikrotik connection setup already:
Download winbox  https://mikrotik.com/download select winbox for your os, download and run and login with your credentials e.g
IP: 20.xx.xx5.xxx
username: admin
password: xxxxxxxxxx
10.0.0.0/16 (default address range)
10.1.0.0/1610.0.0.0/16 (default subnet)
In this network, MikroTik Router (RouterOS v6.46) is connected to internet through ether1 interface with your(Mikrotik router) IP address. In your network, this IP address should be replaced with public IP address. MikroTik Router’s ether2 interface is connected to local network having IP network 10.10.11.0/24. We will configure OpenVPN server in this router and OpenVPN client in a Windows Operating System. After OpenVPN Server and Client configuration, the router will create a virtual interface (OpenVPN Tunnel) across public network where VPN Gateway IP address will be 192.168.2.1 and Client machine will get an IP Address within 192.168.2.0/24 IP Block. We will also declare route in OpenVPN Client so that connected VPN user can access resources of OpenVPN server’s network.
Enable and configure OpenVPN Server in MikroTik Router. It is assumed that your WAN and LAN networks are working without any issue.

Complete MikroTik OpenVPN Server configuration can be divided into the following three steps.

Step 1: Creating TLS Certificate for OpenVPN Server and Client
Step 2: Enabling and Configuring OpenVPN Server
Step 3: Creating OpenVPN Users
Please refer to https://wiki.mikrotik.com/wiki/Main_Page for details 
We will create required OpenVPN certificate from our RouterOS. OpenVPN Server and Client require three types of certificates:

CA (Certification Authority) Certificate
Server Certificate and
Client Certificate
Creating CA certificate

The following steps will show how to create CA certificate in MikroTik RouterOS.

From Winbox, go to System > Certificates menu item and click on Certificates tab and then click on PLUS SIGN (+). New Certificate window will appear.
Put your CA certificate name (for example: CA) in Name input field. Also put a certificate common name (for example: CA) in Common Name input field.

Click on Key Usage tab and uncheck all checkboxes except crl sign and key cert. sign checkboxes.
Click on Apply button and then click on Sign button. Sign window will appear now.
Your created CA certificate template will appear in Certificate dropdown menu. Select your newly created certificate template if it is not selected.
Put MikroTik Router’s WAN IP address (example: 117.58.247.198) in CA CRL Host input field.
Click on Sign button. Your Signed certificate will be created within few seconds.
Click on OK button to close New Certificate window.
If newly created CA certificate does not show T flag or Trusted property shows no, double click on your CA certificate and click on Trusted checkbox located at the bottom of General tab and then click on Apply and OK button.

Creating Server Certificate

Next--> Server certificate .

Click on PLUS SIGN (+) again. New Certificate window will appear.
Put your server certificate name (for example: Server) in Name input field. Also put a certificate common name (for example: Server) in Common Name input field.
If you have put any optional field in CA certificate, put them here also.
Click on Key Usage tab and uncheck all checkboxes except digital signature, key encipherment and tls server checkboxes.
Click on Apply button and then click on Sign button. Sign window will appear now.
Your newly created Server certificate template will appear in certificate dropdown menu. Select newly created certificate template if it is not selected.
Also select CA certificate from CA dropdown menu.
Click on Sign button. Your Signed certificate will be created within few seconds.
Click on OK button to close New Certificate window.
Double click on your server certificate and click on Trusted checkbox located at the bottom of General tab and then click on Apply and OK button.

Creating Client Certificate

The following steps will show how to create client certificate in MikroTik RouterOS.

Click on PLUS SIGN (+) again. New Certificate window will appear.
Put your client certificate name (for example: Client) in Name input field. Also put a certificate common name (for example: Client) in Common Name input field.
If you put any optional field in CA certificate, put them here also.
Click on Key Usage tab and uncheck all checkboxes except tls client checkbox.
Click on Apply button and then click on Sign button. Sign window will appear now.
Your newly created Client certificate template will appear in certificate dropdown menu. Select your newly created certificate template if it is not selected.
Also select CA certificate from CA dropdown menu.
Click on Sign button. Your Signed certificate will be created within few seconds.
Click on OK button to close New Certificate window.

NOW...Export all certs by going to files select and copy the certs,createa folder locally and cpy/paste them in there.
NEXT STEP--> OpenVPN Server Configuration in MikroTik Router
Click on PPP menu item from Winbox and then click on Interface tab.
Click on OVPN Server button. OVPN Server window will appear.
Click on Enabled checkbox to enable OpenVPN Server.
Put your desired TCP Port (example: 443) on which you want to run OpenVPN Server in Port input field.
Make sure ip option is selected in Mode dropdown menu.
From Certificate dropdown menu, choose server certificate that we created before. Also click on Require Client Certificate checkbox.
From Auth. Panel, uncheck all checkboxes except sha1.
From Cipher panel, uncheck all checkboxes except aes 256.
Now click on Apply and OK button.(OpenVPN Server is now running in MikroTik Router)
 Creating OpenVPN Users
MikroTik OpenVPN uses username and password to validate legal connection. So, we have to create username and password to allow any user. The complete user configuration for OpenVPN Server can be divided into three parts.

IP Pool Configuration
User Profile Configuration and
User Configuration
IP Pool Configuration

Usually multiple users can connect to OpenVPN Server. So, it is always better to create an IP Pool from where connected user will get IP address. The following steps will show how to create IP Pool in MikroTik Router.

From Winbox, go to IP > Pool menu item. IP Pool Window will appear.
Click on PLUS SIGN (+). New IP Pool window will appear.
Put a meaningful name (vpn_pool) in Name input field.
Put desired IP Ranges (192.168.2.2-192.168.2.250 Use yours these are just dummies for the example) in Addresses input filed. Make sure not to use VPN Gateway IP (192.168.2.1) and the last IP (192.168.2.154) because last IP will be used as DHCP Server IP.
Click Apply and OK button.

User Profile Configuration

After creating IP Pool, we will now configure profile so that all users can have similar characteristics. The following steps will show how to configure user profile for OpenVPN User.

From Winbox, go to PPP menu item and click on Profile tab and then click on PLUS SIGN (+). New PPP Profile window will appear.
Put a meaningful name (vpn_profile) in Name input field.
Put VPN Gateway address (192.168.2.1) in Local Address input field.
Choose the created IP Pool (vpn_pool) from Remote Address dropdown menu.
Click Apply and OK button.

OpenVPN Users Configuration

After creating user profile, we will now create users who will be connected to OpenVPN Server. The following steps will show how to create OpenVPN users in MikroTik RouterOS.

From PPP window, click on Secrets tab and then click on PLUS SIGN (+). New PPP Secret window will appear.
Put username (For example: mischa123) in Name input field and put password in Password input field.
Choose ovpn from Service dropdown menu.
Choose the created profile from Profile dropdown menu.
Click on Apply and OK button.(Openvpn server user created)
NOW..timefor the fun part install opevpn OpenVPN Users Configuration
Go to https://openvpn.net/community-downloads/ pick the one suited for your os
Note: when installing select the following TAP Virtual Adapter, EasyRSA Mgmt scripts,GUI
After install open netwrok connections and enable TAP Windows adapter-V9 
Now take the certs you copied earlier and copy them to the config file(windows C:Programfiles/openvpn/config)
Rename the certs as follows
ca:     CA.crt
cert:   Client.crt
key:   Client.key 
Open the sample-config will be found where a sample OpenVPN Client configuration file named client.ovpn is provided. Copy this sample configuration file into config folder and then open the client configuration file with a text editor such as WordPad, NotePad ++ and add the required parameters to the file and save


File: /secret
ovpn
test

