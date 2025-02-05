# Repository Information
Name: mikrotik-gfw-list

# Directory Structure
Directory structure:
└── github_repos/mikrotik-gfw-list/
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
    │   │       ├── pack-9cbfe3f813d759d7f8491e7f78965bdf0ea2324a.idx
    │   │       └── pack-9cbfe3f813d759d7f8491e7f78965bdf0ea2324a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── aggregate-cidr-addresses.pl
    ├── amazon-hk
    ├── apple
    ├── generate_gfw-range.sh
    ├── generate_gfwl2.sh
    ├── generate_ipcn-ct-range.sh
    ├── generate_ipcn-unicom-range.sh
    ├── generate_ipcn-unicom.sh
    ├── gfw
    ├── gfw.txt
    ├── ipblock_bootstrap.sh
    ├── ipnet_to_iprange.py
    ├── microsoft
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
	url = https://github.com/atmouse-/mikrotik-gfw-list.git
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
0000000000000000000000000000000000000000 f54b8fcba794661b77a1206a95d4cdba3e919fdc vivek-dodia <vivek.dodia@icloud.com> 1738606027 -0500	clone: from https://github.com/atmouse-/mikrotik-gfw-list.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 f54b8fcba794661b77a1206a95d4cdba3e919fdc vivek-dodia <vivek.dodia@icloud.com> 1738606027 -0500	clone: from https://github.com/atmouse-/mikrotik-gfw-list.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 f54b8fcba794661b77a1206a95d4cdba3e919fdc vivek-dodia <vivek.dodia@icloud.com> 1738606027 -0500	clone: from https://github.com/atmouse-/mikrotik-gfw-list.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
f54b8fcba794661b77a1206a95d4cdba3e919fdc refs/remotes/origin/master


File: /.git\refs\heads\master
f54b8fcba794661b77a1206a95d4cdba3e919fdc


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /aggregate-cidr-addresses.pl
#!/usr/bin/perl
#
# aggregate-cidr-addresses - combine a list of CIDR address blocks
# Copyright (C) 2001,2007 Mark Suter <suter@zwitterion.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see L<http://www.gnu.org/licenses/>.
#
# [MJS 22 Oct 2001] Aggregate CIDR addresses
# [MJS  9 Oct 2007] Overlap idea from Anthony Ledesma at theplanet dot com.
# [MJS 16 Feb 2012] Prompted to clarify license by Alexander Talos-Zens - at at univie dot ac dot at
# [MJS 21 Feb 2012] IPv6 fixes by Alexander Talos-Zens
# [MJS 21 Feb 2012] Split ranges into prefixes (fixes a 10+ year old bug)

use strict;
use warnings;
use English qw( -no_match_vars );
use Net::IP;

## Read in all the IP addresses
my @addrs = map { Net::IP->new($_) or die "$PROGRAM_NAME: Not an IP: \"$_\"."; }
    map { / \A \s* (.+?) \s* \Z /msix and $1; } <>;

## Split any ranges into prefixes
@addrs = map {
    defined $_->prefixlen ? $_ : map { Net::IP->new($_) }
        $_->find_prefixes
} @addrs;

## Sort the IP addresses
@addrs = sort { $a->version <=> $b->version or $a->bincomp( 'lt', $b ) ? -1 : $a->bincomp( 'gt', $b ) ? 1 : 0 } @addrs;

## Handle overlaps
my $count   = 0;
my $current = $addrs[0];
foreach my $next ( @addrs[ 1 .. $#addrs ] ) {
    my $r = $current->overlaps($next);
    if ( $current->version != $next->version or $r == $IP_NO_OVERLAP ) {
        $current = $next;
        $count++;
    }
    elsif ( $r == $IP_A_IN_B_OVERLAP ) {
        $current = $next;
        splice @addrs, $count, 1;
    }
    elsif ( $r == $IP_B_IN_A_OVERLAP or $r == $IP_IDENTICAL ) {
        splice @addrs, $count + 1, 1;
    }
    else {
        die "$PROGRAM_NAME: internal error - overlaps() returned an unexpected value!\n";
    }
}

## Keep aggregating until we don't change anything
my $change = 1;
while ($change) {
    $change = 0;
    my @new_addrs = ();
    $current = $addrs[0];
    foreach my $next ( @addrs[ 1 .. $#addrs ] ) {
        if ( my $total = $current->aggregate($next) ) {
            $current = $total;
            $change  = 1;
        }
        else {
            push @new_addrs, $current;
            $current = $next;
        }
    }
    push @new_addrs, $current;
    @addrs = @new_addrs;
}

## Print out the IP addresses
foreach (@addrs) {
    print $_->prefix(), "\n";
}

# $Id: aggregate-cidr-addresses,v 1.9 2012/02/21 10:14:22 suter Exp suter $


File: /amazon-hk
## amazon-hk
/ip route add comment=amazon-hk dst-address=52.84.42.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.84.44.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.84.48.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.85.148.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.85.152.0/21 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.211.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.223.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.234.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.238.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.249.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=52.222.254.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.182.0.0/21 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.182.170.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.192.64.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.192.72.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.230.64.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.230.72.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.239.129.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.239.130.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.239.216.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.239.218.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.240.24.0/22 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.240.57.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.240.58.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.240.60.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=54.240.62.0/23 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=204.246.187.0/24 gateway=117.28.231.30
/ip route add comment=amazon-hk dst-address=216.137.54.0/23 gateway=117.28.231.30

File: /apple
## apple
/ip route add comment=apple dst-address=17.0.0.0/8 gateway=117.28.231.30

File: /generate_gfw-range.sh
#!/usr/bin/sh

cat gfw | grep -oE '((1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\/[0-9][0-9]?' | ./aggregate-cidr-addresses.pl | python ./ipnet_to_iprange.py


File: /generate_gfwl2.sh
#!/usr/bin/sh

cat_all () {
    find ./ipblock-ipcn/ipcdn ./ipblock-ipcn/ipcloud -name "*.txt" | while read line
    do
        cat $line
    done
}

cat_all | ./aggregate-cidr-addresses.pl | while read line
do
    echo "/ip firewall address-list add list=gfwl2 address=$line"
done


File: /generate_ipcn-ct-range.sh
#!/usr/bin/sh


cat_all () {
    find ./ipblock-ipcn/ipcn/CHINANET -name "*.txt" | while read line
    do
        cat $line
    done
}

cat_all | ./aggregate-cidr-addresses.pl | python ./ipnet_to_iprange.py


File: /generate_ipcn-unicom-range.sh
#!/usr/bin/sh


cat_all () {
    find ./ipblock-ipcn/ipcn/UNICOM -name "*.txt" | while read line
    do
        cat $line
    done
}

cat_all | ./aggregate-cidr-addresses.pl | python ./ipnet_to_iprange.py


File: /generate_ipcn-unicom.sh
#!/usr/bin/sh

cat_all () {
    find ./ipblock-ipcn/ipcn/UNICOM -name "*.txt" | while read line
    do
        cat $line
    done
}

cat_all | ./aggregate-cidr-addresses.pl | while read line
do
    echo "/ip firewall address-list add list=ipcn-unicom address=$line"
done


File: /gfw
# Google LLC _netblocks
/ip firewall address-list add list=gfw address=35.190.247.0/24
/ip firewall address-list add list=gfw address=35.191.0.0/16
/ip firewall address-list add list=gfw address=64.233.160.0/19
/ip firewall address-list add list=gfw address=66.102.0.0/20
/ip firewall address-list add list=gfw address=66.249.80.0/20
/ip firewall address-list add list=gfw address=72.14.192.0/18
/ip firewall address-list add list=gfw address=74.125.0.0/16
/ip firewall address-list add list=gfw address=108.177.8.0/21
/ip firewall address-list add list=gfw address=108.177.96.0/19
/ip firewall address-list add list=gfw address=130.211.0.0/22
/ip firewall address-list add list=gfw address=142.250.0.0/15
/ip firewall address-list add list=gfw address=172.217.0.0/19
/ip firewall address-list add list=gfw address=172.217.128.0/19
/ip firewall address-list add list=gfw address=172.217.160.0/20
/ip firewall address-list add list=gfw address=172.217.192.0/19
/ip firewall address-list add list=gfw address=172.217.32.0/20
/ip firewall address-list add list=gfw address=172.253.56.0/21
/ip firewall address-list add list=gfw address=172.253.112.0/20
/ip firewall address-list add list=gfw address=173.194.0.0/16
/ip firewall address-list add list=gfw address=209.85.128.0/17
/ip firewall address-list add list=gfw address=216.239.32.0/19
/ip firewall address-list add list=gfw address=216.58.192.0/19
# Google Cloud global scope service
/ip firewall address-list add list=gfw address=34.95.64.0/18
/ip firewall address-list add list=gfw address=34.96.64.0/18
/ip firewall address-list add list=gfw address=34.98.64.0/18
/ip firewall address-list add list=gfw address=34.102.128.0/17
/ip firewall address-list add list=gfw address=34.104.27.0/24
/ip firewall address-list add list=gfw address=34.107.128.0/17
/ip firewall address-list add list=gfw address=34.116.0.0/21
/ip firewall address-list add list=gfw address=34.117.0.0/16
/ip firewall address-list add list=gfw address=34.120.0.0/16
/ip firewall address-list add list=gfw address=34.149.0.0/16
/ip firewall address-list add list=gfw address=35.186.192.0/18
/ip firewall address-list add list=gfw address=35.190.0.0/18
/ip firewall address-list add list=gfw address=35.190.64.0/19
/ip firewall address-list add list=gfw address=35.190.112.0/20
/ip firewall address-list add list=gfw address=35.201.64.0/18
/ip firewall address-list add list=gfw address=35.227.192.0/18
/ip firewall address-list add list=gfw address=35.241.0.0/18
/ip firewall address-list add list=gfw address=35.244.128.0/17
/ip firewall address-list add list=gfw address=107.178.240.0/20
/ip firewall address-list add list=gfw address=130.211.4.0/22
/ip firewall address-list add list=gfw address=130.211.8.0/21
/ip firewall address-list add list=gfw address=130.211.16.0/20
/ip firewall address-list add list=gfw address=130.211.32.0/20
# Anycast of Google LLC AS396982, bitly
/ip firewall address-list add list=gfw address=67.199.248.0/24
# facebook AS32934, AS54115
/ip firewall address-list add list=gfw address=31.13.24.0/21
/ip firewall address-list add list=gfw address=31.13.64.0/18
/ip firewall address-list add list=gfw address=45.64.40.0/22
/ip firewall address-list add list=gfw address=66.220.144.0/20
/ip firewall address-list add list=gfw address=69.63.176.0/20
/ip firewall address-list add list=gfw address=69.171.224.0/19
/ip firewall address-list add list=gfw address=74.119.76.0/22
/ip firewall address-list add list=gfw address=102.132.96.0/20
/ip firewall address-list add list=gfw address=103.4.96.0/22
/ip firewall address-list add list=gfw address=129.134.0.0/16
/ip firewall address-list add list=gfw address=147.75.208.0/20
/ip firewall address-list add list=gfw address=157.240.0.0/16
/ip firewall address-list add list=gfw address=173.252.64.0/18
/ip firewall address-list add list=gfw address=179.60.192.0/22
/ip firewall address-list add list=gfw address=185.60.216.0/22
/ip firewall address-list add list=gfw address=185.89.216.0/22
/ip firewall address-list add list=gfw address=199.201.64.0/22
/ip firewall address-list add list=gfw address=204.15.20.0/22
# twitter AS13414
/ip firewall address-list add list=gfw address=64.63.0.0/18
/ip firewall address-list add list=gfw address=69.12.56.0/21
/ip firewall address-list add list=gfw address=69.195.160.0/19
/ip firewall address-list add list=gfw address=103.55.162.0/24
/ip firewall address-list add list=gfw address=103.252.112.0/22
/ip firewall address-list add list=gfw address=104.244.40.0/21
/ip firewall address-list add list=gfw address=185.45.4.0/22
/ip firewall address-list add list=gfw address=192.44.68.0/23
/ip firewall address-list add list=gfw address=192.48.236.0/23
/ip firewall address-list add list=gfw address=192.133.76.0/22
/ip firewall address-list add list=gfw address=199.16.156.0/22
/ip firewall address-list add list=gfw address=199.59.148.0/22
/ip firewall address-list add list=gfw address=199.69.58.0/23
/ip firewall address-list add list=gfw address=199.96.56.0/21
/ip firewall address-list add list=gfw address=202.160.128.0/22
/ip firewall address-list add list=gfw address=209.237.192.0/19
# Anycast of Edgecast, twitter
/ip firewall address-list add list=gfw address=117.18.232.0/24
/ip firewall address-list add list=gfw address=117.18.237.0/24
/ip firewall address-list add list=gfw address=117.18.238.0/24
/ip firewall address-list add list=gfw address=117.18.239.0/24
/ip firewall address-list add list=gfw address=152.199.24.0/24
/ip firewall address-list add list=gfw address=152.199.43.0/24
/ip firewall address-list add list=gfw address=192.229.173.0/24
/ip firewall address-list add list=gfw address=192.229.163.0/24
/ip firewall address-list add list=gfw address=192.229.237.0/24
/ip firewall address-list add list=gfw address=72.21.91.0/24
# dropbox AS19679
/ip firewall address-list add list=gfw address=45.58.64.0/20
/ip firewall address-list add list=gfw address=108.160.160.0/20
/ip firewall address-list add list=gfw address=162.125.0.0/16
/ip firewall address-list add list=gfw address=185.45.8.0/22
/ip firewall address-list add list=gfw address=199.47.216.0/22
# line.me AS38631
/ip firewall address-list add list=gfw address=43.223.0.0/16
/ip firewall address-list add list=gfw address=103.2.28.0/24
/ip firewall address-list add list=gfw address=103.2.30.0/23
/ip firewall address-list add list=gfw address=119.235.224.0/20
/ip firewall address-list add list=gfw address=147.92.128.0/17
/ip firewall address-list add list=gfw address=203.104.128.0/20
/ip firewall address-list add list=gfw address=203.104.144.0/21
/ip firewall address-list add list=gfw address=203.104.152.0/22
/ip firewall address-list add list=gfw address=203.104.156.0/23
/ip firewall address-list add list=gfw address=203.104.158.0/24
# telegram AS62014, AS62041, AS59930, AS44907
/ip firewall address-list add list=gfw address=91.108.4.0/22
/ip firewall address-list add list=gfw address=91.108.8.0/21
/ip firewall address-list add list=gfw address=91.108.16.0/21
/ip firewall address-list add list=gfw address=91.108.36.0/22
/ip firewall address-list add list=gfw address=91.108.56.0/22
/ip firewall address-list add list=gfw address=95.161.64.0/20
/ip firewall address-list add list=gfw address=149.154.160.0/20
# AS14907 wikipedia
/ip firewall address-list add list=gfw address=91.198.174.0/24
/ip firewall address-list add list=gfw address=103.102.166.0/24
/ip firewall address-list add list=gfw address=185.15.56.0/22
/ip firewall address-list add list=gfw address=198.35.26.0/23
/ip firewall address-list add list=gfw address=208.80.152.0/22
# AS7941 INTERN-95 INTERNET-ARCHIVE
/ip firewall address-list add list=gfw address=207.241.224.0/20
/ip firewall address-list add list=gfw address=208.70.24.0/21
# 4shared.com AS40824 WZ Communications Inc.
/ip firewall address-list add list=gfw address=74.117.176.0/21
/ip firewall address-list add list=gfw address=199.80.52.0/22
/ip firewall address-list add list=gfw address=199.101.132.0/22
/ip firewall address-list add list=gfw address=204.155.144.0/20
/ip firewall address-list add list=gfw address=208.88.224.0/22
/ip firewall address-list add list=gfw address=208.94.232.0/22
# Anycast of Fastly, reddit, twitch, pinterest, imgur, vimeo
/ip firewall address-list add list=gfw address=151.101.0.0/16
/ip firewall address-list add list=gfw address=185.199.108.0/22
/ip firewall address-list add list=gfw address=199.232.192.0/22
/ip firewall address-list add list=gfw address=199.232.196.0/22
# bgp.he.net AS6939
/ip firewall address-list add list=gfw address=72.52.64.0/18
# Anycast of AWS GlobalAccelerator
/ip firewall address-list add list=gfw address=3.2.8.0/21
/ip firewall address-list add list=gfw address=3.3.0.0/23
/ip firewall address-list add list=gfw address=3.3.6.0/23
/ip firewall address-list add list=gfw address=3.3.8.0/21
/ip firewall address-list add list=gfw address=3.33.128.0/17
/ip firewall address-list add list=gfw address=13.248.96.0/21
/ip firewall address-list add list=gfw address=13.248.104.0/22
/ip firewall address-list add list=gfw address=13.248.108.0/23
/ip firewall address-list add list=gfw address=13.248.111.0/24
/ip firewall address-list add list=gfw address=13.248.112.0/20
/ip firewall address-list add list=gfw address=13.248.128.0/17
/ip firewall address-list add list=gfw address=15.197.0.0/23
/ip firewall address-list add list=gfw address=15.197.2.0/24
/ip firewall address-list add list=gfw address=15.197.4.0/22
/ip firewall address-list add list=gfw address=15.197.128.0/17
/ip firewall address-list add list=gfw address=35.71.128.0/17
/ip firewall address-list add list=gfw address=52.223.0.0/17
/ip firewall address-list add list=gfw address=54.230.192.0/21
/ip firewall address-list add list=gfw address=75.2.0.0/17
/ip firewall address-list add list=gfw address=76.223.0.0/17
/ip firewall address-list add list=gfw address=99.77.188.0/23
/ip firewall address-list add list=gfw address=99.77.190.0/24
/ip firewall address-list add list=gfw address=99.82.156.0/22
/ip firewall address-list add list=gfw address=99.82.160.0/20
/ip firewall address-list add list=gfw address=99.83.96.0/24
/ip firewall address-list add list=gfw address=99.83.98.0/23
/ip firewall address-list add list=gfw address=99.83.100.0/23
/ip firewall address-list add list=gfw address=99.83.128.0/17
# Anycast of Akamai AS33905
/ip firewall address-list add list=gfw address=2.18.48.0/21
/ip firewall address-list add list=gfw address=23.1.35.0/24
/ip firewall address-list add list=gfw address=23.1.99.0/24
/ip firewall address-list add list=gfw address=23.1.106.0/24
/ip firewall address-list add list=gfw address=23.7.244.0/24
/ip firewall address-list add list=gfw address=23.36.184.0/22
/ip firewall address-list add list=gfw address=23.40.100.0/24
/ip firewall address-list add list=gfw address=23.56.111.0/24
/ip firewall address-list add list=gfw address=23.76.146.0/24
/ip firewall address-list add list=gfw address=23.202.36.0/23
/ip firewall address-list add list=gfw address=23.213.202.0/23
/ip firewall address-list add list=gfw address=96.16.62.0/24
/ip firewall address-list add list=gfw address=104.75.170.0/23
/ip firewall address-list add list=gfw address=104.94.220.0/22
/ip firewall address-list add list=gfw address=104.96.176.0/22
/ip firewall address-list add list=gfw address=104.96.180.0/23
/ip firewall address-list add list=gfw address=104.107.211.0/24
/ip firewall address-list add list=gfw address=104.107.220.0/22
/ip firewall address-list add list=gfw address=104.109.10.0/23
/ip firewall address-list add list=gfw address=104.109.12.0/24
/ip firewall address-list add list=gfw address=104.119.192.0/19
/ip firewall address-list add list=gfw address=115.69.232.0/22
/ip firewall address-list add list=gfw address=184.25.103.0/24
/ip firewall address-list add list=gfw address=184.25.179.0/24
/ip firewall address-list add list=gfw address=184.31.3.0/24
/ip firewall address-list add list=gfw address=184.31.10.0/24
# Anycast of msedge AS8068
/ip firewall address-list add list=gfw address=13.107.3.0/24
/ip firewall address-list add list=gfw address=13.107.4.0/22
/ip firewall address-list add list=gfw address=13.107.9.0/24
/ip firewall address-list add list=gfw address=13.107.12.0/23
/ip firewall address-list add list=gfw address=13.107.15.0/24
/ip firewall address-list add list=gfw address=13.107.16.0/24
/ip firewall address-list add list=gfw address=13.107.18.0/23
/ip firewall address-list add list=gfw address=13.107.21.0/24
/ip firewall address-list add list=gfw address=13.107.22.0/24
/ip firewall address-list add list=gfw address=13.107.24.0/24
/ip firewall address-list add list=gfw address=13.107.39.0/24
/ip firewall address-list add list=gfw address=13.107.40.0/24
/ip firewall address-list add list=gfw address=13.107.42.0/23
/ip firewall address-list add list=gfw address=13.107.46.0/23
/ip firewall address-list add list=gfw address=13.107.48.0/22
/ip firewall address-list add list=gfw address=13.107.52.0/23
/ip firewall address-list add list=gfw address=13.107.54.0/24
/ip firewall address-list add list=gfw address=13.107.56.0/24
/ip firewall address-list add list=gfw address=13.107.128.0/23
/ip firewall address-list add list=gfw address=13.107.136.0/22
/ip firewall address-list add list=gfw address=13.107.140.0/24
/ip firewall address-list add list=gfw address=13.107.160.0/24
/ip firewall address-list add list=gfw address=13.107.208.0/24
/ip firewall address-list add list=gfw address=13.107.213.0/24
/ip firewall address-list add list=gfw address=13.107.224.0/24
/ip firewall address-list add list=gfw address=13.107.226.0/24
/ip firewall address-list add list=gfw address=13.107.246.0/24
/ip firewall address-list add list=gfw address=13.107.253.0/24
/ip firewall address-list add list=gfw address=13.107.254.0/24
/ip firewall address-list add list=gfw address=52.113.194.0/23
/ip firewall address-list add list=gfw address=52.113.196.0/23
/ip firewall address-list add list=gfw address=131.253.3.0/24
/ip firewall address-list add list=gfw address=131.253.21.0/24
/ip firewall address-list add list=gfw address=131.253.33.0/24
/ip firewall address-list add list=gfw address=150.171.32.0/24
/ip firewall address-list add list=gfw address=150.171.40.0/22
/ip firewall address-list add list=gfw address=150.171.44.0/24
/ip firewall address-list add list=gfw address=204.79.197.0/24
# Anycast of Cloudflare AS13335
/ip firewall address-list add list=gfw address=104.16.0.0/13
/ip firewall address-list add list=gfw address=104.24.0.0/14
/ip firewall address-list add list=gfw address=108.162.192.0/18
/ip firewall address-list add list=gfw address=172.64.0.0/15
/ip firewall address-list add list=gfw address=172.66.0.0/22
/ip firewall address-list add list=gfw address=172.66.40.0/21
/ip firewall address-list add list=gfw address=172.67.0.0/16


File: /gfw.txt
35.190.247.0/24
35.191.0.0/16
64.233.160.0/19
66.102.0.0/20
66.249.80.0/20
72.14.192.0/18
74.125.0.0/16
108.177.8.0/21
108.177.96.0/19
130.211.0.0/22
142.250.0.0/15
172.217.0.0/19
172.217.128.0/19
172.217.160.0/20
172.217.192.0/19
172.217.32.0/20
172.253.56.0/21
172.253.112.0/20
173.194.0.0/16
209.85.128.0/17
216.239.32.0/19
216.58.192.0/19
34.95.64.0/18
34.96.64.0/18
34.98.64.0/18
34.102.128.0/17
34.104.27.0/24
34.107.128.0/17
34.116.0.0/21
34.117.0.0/16
34.120.0.0/16
34.149.0.0/16
35.186.192.0/18
35.190.0.0/18
35.190.64.0/19
35.190.112.0/20
35.201.64.0/18
35.227.192.0/18
35.241.0.0/18
35.244.128.0/17
107.178.240.0/20
130.211.4.0/22
130.211.8.0/21
130.211.16.0/20
130.211.32.0/20
31.13.24.0/21
31.13.64.0/18
45.64.40.0/22
66.220.144.0/20
69.63.176.0/20
69.171.224.0/19
74.119.76.0/22
102.132.96.0/20
103.4.96.0/22
129.134.0.0/16
147.75.208.0/20
157.240.0.0/16
173.252.64.0/18
179.60.192.0/22
185.60.216.0/22
185.89.216.0/22
199.201.64.0/22
204.15.20.0/22
64.63.0.0/18
69.12.56.0/21
69.195.160.0/19
103.55.162.0/24
103.252.112.0/22
104.244.40.0/21
185.45.4.0/22
192.44.68.0/23
192.48.236.0/23
192.133.76.0/22
199.16.156.0/22
199.59.148.0/22
199.69.58.0/23
199.96.56.0/21
202.160.128.0/22
209.237.192.0/19
117.18.232.0/24
117.18.237.0/24
117.18.238.0/24
117.18.239.0/24
152.199.24.0/24
152.199.43.0/24
192.229.173.0/24
192.229.163.0/24
192.229.237.0/24
72.21.91.0/24
45.58.64.0/20
108.160.160.0/20
162.125.0.0/16
185.45.8.0/22
199.47.216.0/22
103.2.28.0/24
103.2.30.0/23
119.235.224.0/20
147.92.128.0/17
203.104.128.0/20
203.104.144.0/21
203.104.152.0/22
203.104.156.0/23
203.104.158.0/24
91.108.4.0/22
91.108.8.0/21
91.108.16.0/21
91.108.36.0/22
91.108.56.0/22
95.161.64.0/20
149.154.160.0/20
91.198.174.0/24
103.102.166.0/24
185.15.56.0/22
198.35.26.0/23
208.80.152.0/22
207.241.224.0/20
208.70.24.0/21
74.117.176.0/21
199.80.52.0/22
199.101.132.0/22
204.155.144.0/20
208.88.224.0/22
208.94.232.0/22
151.101.0.0/16
185.199.108.0/22
199.232.192.0/22
199.232.196.0/22
72.52.64.0/18
3.2.8.0/21
3.3.0.0/23
3.3.6.0/23
3.3.8.0/21
3.33.128.0/17
13.248.96.0/21
13.248.104.0/22
13.248.108.0/23
13.248.111.0/24
13.248.112.0/20
13.248.128.0/17
15.197.0.0/23
15.197.2.0/24
15.197.4.0/22
15.197.128.0/17
35.71.128.0/17
52.223.0.0/17
54.230.192.0/21
75.2.0.0/17
76.223.0.0/17
99.77.188.0/23
99.77.190.0/24
99.82.156.0/22
99.82.160.0/20
99.83.96.0/24
99.83.98.0/23
99.83.100.0/23
99.83.128.0/17
2.18.48.0/21
23.1.35.0/24
23.1.99.0/24
23.1.106.0/24
23.7.244.0/24
23.36.184.0/22
23.40.100.0/24
23.56.111.0/24
23.76.146.0/24
23.202.36.0/23
23.213.202.0/23
96.16.62.0/24
104.75.170.0/23
104.94.220.0/22
104.96.176.0/22
104.96.180.0/23
104.107.211.0/24
104.107.220.0/22
104.109.10.0/23
104.109.12.0/24
104.119.192.0/19
115.69.232.0/22
184.25.103.0/24
184.25.179.0/24
184.31.3.0/24
184.31.10.0/24
67.199.248.0/24
43.223.0.0/16
13.107.3.0/24
13.107.4.0/22
13.107.9.0/24
13.107.12.0/23
13.107.15.0/24
13.107.16.0/24
13.107.18.0/23
13.107.21.0/24
13.107.22.0/24
13.107.24.0/24
13.107.39.0/24
13.107.40.0/24
13.107.42.0/23
13.107.46.0/23
13.107.48.0/22
13.107.52.0/23
13.107.54.0/24
13.107.56.0/24
13.107.128.0/23
13.107.136.0/22
13.107.140.0/24
13.107.160.0/24
13.107.208.0/24
13.107.213.0/24
13.107.224.0/24
13.107.226.0/24
13.107.246.0/24
13.107.253.0/24
13.107.254.0/24
52.113.194.0/23
52.113.196.0/23
131.253.3.0/24
131.253.21.0/24
131.253.33.0/24
150.171.32.0/24
150.171.40.0/22
150.171.44.0/24
204.79.197.0/24
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
172.64.0.0/15
172.66.0.0/22
172.66.40.0/21
172.67.0.0/16


File: /ipblock_bootstrap.sh
#!/usr/bin/sh

rm -rf ipblock-ipcn
git clone --quiet --depth=1 --single-branch --branch archive https://github.com/atmouse-/ipblock-ipcn.git
if [ $? -ne 0 ]
then
    exit 1
fi


File: /ipnet_to_iprange.py
#!/usr/bin/python

import netaddr
import fileinput

if __name__ == "__main__":
    for line in fileinput.input():
        ipnet = netaddr.IPNetwork(line.strip())
        print("{}-{}".format(ipnet[0], ipnet[-1]))
        

File: /microsoft
## microsoft
/ip route add comment=microsoft dst-address=65.53.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.54.0.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.54.1.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.54.2.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.28.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.28.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.188.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=70.42.230.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=104.44.112.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.107.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.107.0.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.107.217.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.54.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.57.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.58.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.58.192.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.58.248.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.59.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.60.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.0.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.8.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.9.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.10.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.16.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.24.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.40.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.48.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.64.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.148.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.152.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.236.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.248.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=198.105.232.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=198.180.95.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.2.137.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.242.48.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.182.144.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.255.244.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.192.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.196.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.200.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.201.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=194.69.96.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=194.69.100.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=194.69.126.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=13.64.0.0/11 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=13.104.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=13.107.20.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=23.96.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=23.100.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=23.102.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=23.103.64.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=23.103.128.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=40.64.0.0/10 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.10.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.12.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.18.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.51.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.53.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.103.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.104.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.107.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.116.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.120.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.124.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.132.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.136.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.138.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.140.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.144.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.96.0.0/12 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.112.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.120.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.125.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.126.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.130.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.132.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.136.0.0/13 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.145.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.146.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.148.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.152.0.0/13 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.160.0.0/11 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=52.224.0.0/11 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=64.4.0.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.52.0.0/14 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.44.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.117.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=66.119.144.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=70.37.0.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=70.37.128.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=94.245.64.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=104.40.0.0/13 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=104.146.0.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=104.146.128.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=104.208.0.0/13 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=111.221.16.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=111.221.64.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.1.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.5.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.6.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.8.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.12.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.18.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.24.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.32.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.33.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.61.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.62.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.128.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=132.245.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=134.170.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=137.116.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=137.135.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=137.135.128.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=138.91.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=138.196.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=146.147.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=150.171.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.55.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.56.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.60.23.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.60.31.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=167.220.240.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=168.61.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=168.62.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=191.232.0.0/13 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=192.48.225.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=192.84.159.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=192.84.160.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=192.197.157.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=193.149.64.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=193.221.113.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=198.49.8.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=198.200.130.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=198.206.164.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.30.16.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.60.28.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.74.210.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.103.90.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.103.122.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=199.242.48.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=202.89.224.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.79.135.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.79.179.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.79.195.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.79.252.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.95.96.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.152.140.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=206.138.168.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=206.191.224.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.0.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.33.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.34.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.36.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.40.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.48.0/20 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.64.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.98.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.46.128.0/17 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.68.128.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=207.82.250.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.68.136.0/21 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.76.45.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.76.46.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.84.0.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.84.1.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.84.2.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=208.84.3.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=209.1.112.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=209.185.128.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=209.185.240.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=209.240.192.0/19 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=213.199.128.0/18 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=216.32.180.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=216.32.240.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=216.33.240.0/22 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.16.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=131.253.22.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=157.58.2.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=194.69.104.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=191.234.96.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=191.234.98.0/23 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=192.92.214.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=64.41.193.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.112.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.55.171.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=65.221.5.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=204.176.46.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=209.1.15.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=216.32.180.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=216.34.51.0/24 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.4.0.0/15 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.4.0.0/16 gateway=117.28.231.30
/ip route add comment=microsoft dst-address=51.5.0.0/16 gateway=117.28.231.30

File: /README.md
WARNING: This project is no longer actively maintained.
---

You can add comment to that route and remove by comment
```
/ip route remove [find comment="tw2-route"]
```

or remove by dst-address
```
/ip route remove [find dst-address="207.xx.xxx.xx/32"]
```

Update firewall address-list
```
/ip firewall address-list remove [/ip firewall address-list find list="gfwl2"]
scp gfwl2 admin@10.0.0.6:
/import gfwl2
```

```
/ip firewall address-list remove [/ip firewall address-list find address="152.195.50.0/23"]
```

