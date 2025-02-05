# Repository Information
Name: firewall-mikrotik

# Directory Structure
Directory structure:
└── github_repos/firewall-mikrotik/
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
    │   │       ├── pack-6c769fd5077846e483d9b588662dc7f77a45446a.idx
    │   │       └── pack-6c769fd5077846e483d9b588662dc7f77a45446a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── firewall.txt
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
	url = https://github.com/nmaggots/firewall-mikrotik.git
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
0000000000000000000000000000000000000000 cb7d5d2718575574183bd98df1d8a0905f26e210 vivek-dodia <vivek.dodia@icloud.com> 1738606056 -0500	clone: from https://github.com/nmaggots/firewall-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 cb7d5d2718575574183bd98df1d8a0905f26e210 vivek-dodia <vivek.dodia@icloud.com> 1738606056 -0500	clone: from https://github.com/nmaggots/firewall-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 cb7d5d2718575574183bd98df1d8a0905f26e210 vivek-dodia <vivek.dodia@icloud.com> 1738606056 -0500	clone: from https://github.com/nmaggots/firewall-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
cb7d5d2718575574183bd98df1d8a0905f26e210 refs/remotes/origin/master


File: /.git\refs\heads\master
cb7d5d2718575574183bd98df1d8a0905f26e210


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /firewall.txt
add chain= virus protocol= tcp dst-port= 135-139 action= drop comment= "Blokir Blaster Worm"
add chain= virus protocol= udp dst-port= 135-139 action= drop comment= "Blokir Messenger Worm"  
add chain= virus protocol= tcp dst-port= 445 action= drop comment= "Blokir Blaster Worm TCP"
add chain= virus protocol= udp dst-port= 445 action= drop comment= "Blokir Blaster Worm UDP"
add chain= virus protocol= tcp dst-port= 593 action= drop comment= "Blokir Port Virus 1"
add chain= virus protocol= tcp dst-port= 1024-1030 action= drop comment= "Blokir Port Virus 2"
add chain= virus protocol= tcp dst-port= 1080 action= drop comment= "Drop MyDoom"
add chain= virus protocol= tcp dst-port= 1214 action= drop comment= "Blokir Port Virus 3"
add chain= virus protocol= tcp dst-port= 1363 action= drop comment= "Blokir ndm requester"
add chain= virus protocol= tcp dst-port= 1364 action= drop comment= "Blokir ndm server"
add chain= virus protocol= tcp dst-port= 1368 action= drop comment= "Blokir screen cast"
add chain= virus protocol= tcp dst-port= 1373 action= drop comment= "Blokir hromgrafx"
add chain= virus protocol= tcp dst-port= 1377 action= drop comment= "Blokir cichlid"
add chain= virus protocol= tcp dst-port= 1433-1434 action= drop comment= "Blokir Worm"
add chain= virus protocol= tcp dst-port= 2745 action= drop comment= "Blokir Bagle Virus"
add chain= virus protocol= tcp dst-port= 2283 action= drop comment= "Blokir  Dumaru.Y"
add chain= virus protocol= tcp dst-port= 2535 action= drop comment= "Blokir  Beagle"
add chain= virus protocol= tcp dst-port= 2745 action= drop comment= "Blokir  Beagle.C-K"
add chain= virus protocol= tcp dst-port= 3127-3128 action= drop comment= "Blokir  MyDoom"
add chain= virus protocol= tcp dst-port= 3410 action= drop comment= "Blokir  Backdoor OptixPro"
add chain= virus protocol= tcp dst-port= 4444 action= drop comment= "Blokir Worm TCP"
add chain= virus protocol= udp dst-port= 4444 action= drop comment= "Blokir Worm UDP"
add chain= virus protocol= tcp dst-port= 5554 action= drop comment= "Blokir  Sasser"
add chain= virus protocol= tcp dst-port= 8866 action= drop comment= "Blokir  Beagle.B"
add chain= virus protocol= tcp dst-port= 9898 action= drop comment= "Blokir  Dabber.A-B"
add chain= virus protocol= tcp dst-port= 10000 action= drop comment= "Blokir  Dumaru.Y"
add chain= virus protocol= tcp dst-port= 10080 action= drop comment= "Blokir  MyDoom.B"
add chain= virus protocol= tcp dst-port= 12345 action= drop comment= "Blokir  NetBus"
add chain= virus protocol= tcp dst-port= 17300 action= drop comment= "Blokir  Kuang2"
add chain= virus protocol= tcp dst-port= 27374 action= drop comment= "Blokir  SubSeven"
add chain= virus protocol= tcp dst-port= 65506 action= drop comment= "Blokir  PhatBot, Agobot, Gaobot"
add chain= virus protocol= tcp dst-port= 27665 action= drop comment= "Blokir Trinoo 27665"
add chain= virus protocol= tcp dst-port= 31335 action= drop comment= "Blokir Trinoo 31335"
add chain= virus protocol= tcp dst-port= 31846 action= drop comment= "Blokir Trinoo 31846"
add chain= virus protocol= tcp dst-port= 34555 action= drop comment= "Blokir Trinoo 34555"
add chain= virus protocol= tcp dst-port= 35555 action= drop comment= "Blokir Trinoo 35555" 
add chain=forward src-address=0.0.0.0/8 action=drop comment="Block Bogus IP \ Address" disabled=no 
add chain=forward dst-address=0.0.0.0/8 action=drop comment="" disabled=no 
add chain=forward src-address=127.0.0.0/8 action=drop comment="" disabled=no 
add chain=forward dst-address=127.0.0.0/8 action=drop comment="" disabled=no 
add chain=forward src-address=224.0.0.0/3 action=drop comment="" disabled=no 
add chain=forward dst-address=224.0.0.0/3 action=drop comment="" disabled=no 
add chain=input protocol=tcp dst-port=22 src-address-list=ssh_blacklist action=drop comment="Drop SSH brute forcers" disabled=no 
add chain=input protocol=tcp dst-port=22 connection-state=new src-address-list=ssh_stage3 action=add-src-to-address-list address-list=ssh_blacklist address-list-timeout=1w3d comment="" disabled=no 
add chain=input protocol=tcp dst-port=22 connection-state=new src-address-list=ssh_stage2 action=add-src-to-address-list address-list=ssh_stage3 address-list-timeout=1m comment="" disabled=no 
add chain=input protocol=tcp dst-port=22 connection-state=new src-address-list=ssh_stage1 action=add-src-to-address-list address-list=ssh_stage2 address-list-timeout=1m comment="" disabled=no 
add chain=input protocol=tcp dst-port=22 connection-state=new action=add-src-to-address-list address-list=ssh_stage1 address-list-timeout=1m comment="" disabled=no 
add chain=input protocol=tcp psd=21,3s,3,1 action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="Port \ Scanners to list " disabled=no 
add chain=input protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input protocol=tcp tcp-flags=fin,syn action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input protocol=tcp tcp-flags=syn,rst action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="" disabled=no 
add chain=input src-address-list="port scanners" action=drop comment="" disabled=no 
add chain=input protocol=tcp dst-port=21 src-address-list=ftp_blacklist action=drop comment="Filter FTP to Box" disabled=no 
add chain=output protocol=tcp content="530 Login incorrect" dst-limit=1/1m,9,dst-address/1m action=accept comment="" disabled=no 
add chain=output protocol=tcp content="530 Login incorrect" action=add-dst-to-address-list address-list=ftp_blacklist address-list-timeout=3h comment="" disabled=no 
add chain=forward protocol=tcp action=jump jump-target=tcp comment="Separate \ Protocol into Chains" disabled=no 
add chain=forward protocol=udp action=jump jump-target=udp comment="" disabled=no 
add chain=forward protocol=icmp action=jump jump-target=icmp comment="" disabled=no 
add chain=udp protocol=udp dst-port=69 action=drop comment="Blocking UDP \ Packet" disabled=no 
add chain=udp protocol=udp dst-port=111 action=drop comment="" disabled=no 
add chain=udp protocol=udp dst-port=135 action=drop comment="" disabled=no 
add chain=udp protocol=udp dst-port=137-139 action=drop comment="" disabled=no 
add chain=udp protocol=udp dst-port=2049 action=drop comment="" disabled=no 
add chain=udp protocol=udp dst-port=3133 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=69 action=drop comment="Bloking TCP \ Packet" disabled=no 
add chain=tcp protocol=tcp dst-port=111 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=119 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=135 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=137-139 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=445 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=2049 action=drop comment="" disabled=no
add chain=tcp protocol=tcp dst-port=12345-12346 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=20034 action=drop comment="" disabled=no 
add chain=tcp protocol=tcp dst-port=3133 action=drop comment="" disabled=no
add chain=tcp protocol=tcp dst-port=67-68 action=drop comment="" disabled=no 
add chain=icmp protocol=icmp icmp-options=0:0-255 limit=5,5 action=accept comment="Limited Ping Flood" disabled=no 
add chain=icmp protocol=icmp icmp-options=3:3 limit=5,5 action=accept comment="" disabled=no 
add chain=icmp protocol=icmp icmp-options=3:4 limit=5,5 action=accept comment="" disabled=no 
add chain=icmp protocol=icmp icmp-options=8:0-255 limit=5,5 action=accept comment="" disabled=no 
add chain=icmp protocol=icmp icmp-options=11:0-255 limit=5,5 action=accept comment="" disabled=no 
add chain=icmp protocol=icmp action=drop comment="" disabled=no 
add chain=input dst-address-type=broadcast action=accept comment="Allow \ Broadcast Traffic" disabled=no 
add chain=input connection-state=established action=accept comment="Connection \ State" disabled=no 
add chain=input connection-state=related action=accept comment="" disabled=no 
add chain=input connection-state=invalid action=drop comment="" disabled=no 
add chain=virus protocol=udp action=drop dst-port=1 comment="Sockets des Troie"
add chain=virus protocol=tcp action=drop dst-port=2 comment="Death"
add chain=virus protocol=tcp action=drop dst-port=20 comment="Senna Spy FTP server" 
add chain=virus protocol=tcp action=drop dst-port=21 comment="Back Construction, Blade Runner, Cattivik FTP Server, CC Invader, Dark FTP, Doly Trojan, Fore, Invisible FTP, Juggernaut 42, Larva, MotIv FTP, Net Administrator, Ramen, Senna Spy FTP server, The Flu, Traitor 21, WebEx, WinCrash"
add chain=virus protocol=tcp action=drop dst-port=22 comment="Shaft"
add chain=virus protocol=tcp action=drop dst-port=23 comment="Fire HacKer, Tiny Telnet Server TTS, Truva Atl"
add chain=virus protocol=tcp action=drop dst-port=25 comment="Ajan, Antigen, Barok, Email Password Sender EPS, EPS II, Gip, Gris, Happy99, Hpteam mail, Hybris, I love you, Kuang2, Magic Horse, MBT Mail Bombing Trojan, Moscow Email trojan, Naebi, NewApt worm, ProMail trojan, Shtirlitz, Stealth, Tapiras, Terminator, WinPC, WinSpy"
add chain=virus protocol=tcp action=drop dst-port=30 comment="Agent 40421"
add chain=virus protocol=tcp action=drop dst-port=31 comment="Agent 31, Hackers Paradise, Masters Paradise"
add chain=virus protocol=tcp action=drop dst-port=41 comment="Deep Throat, Foreplay"
add chain=virus protocol=tcp action=drop dst-port=48 comment="DRAT"
add chain=virus protocol=tcp action=drop dst-port=50 comment="DRAT"
add chain=virus protocol=tcp action=drop dst-port=58 comment="DMSetup"
add chain=virus protocol=tcp action=drop dst-port=59 comment="DMSetup"
add chain=virus protocol=tcp action=drop dst-port=79 comment="CDK, Firehotcker"
add chain=virus protocol=tcp action=drop dst-port=80 comment="711 trojan, Seven Eleven, AckCmd, Back End, Back Orifice 2000 Plug-Ins, Cafeini, CGI Backdoor, Executor, God Message, God Message Creator, Hooker, IISworm, MTX, NCX, Reverse WWW Tunnel Backdoor, RingZero, Seeker, WAN Remote, Web Server CT, WebDownloader"
add chain=virus protocol=tcp action=drop dst-port=81 comment="RemoConChubo"
add chain=virus protocol=tcp action=drop dst-port=99 comment="Hidden Port, NCX"
add chain=virus protocol=tcp action=drop dst-port=110 comment="ProMail trojan"
add chain=virus protocol=tcp action=drop dst-port=113 comment="Invisible Identd Deamon, Kazimas"
add chain=virus protocol=tcp action=drop dst-port=119 comment="Happy99"
add chain=virus protocol=tcp action=drop dst-port=121 comment="Attack Bot, God Message, JammerKillah"
add chain=virus protocol=tcp action=drop dst-port=123 comment="Net Controller"
add chain=virus protocol=tcp action=drop dst-port=133 comment="Farnaz"
add chain=virus protocol=tcp action=drop dst-port=135-139 comment="Blaster worm"
add chain=virus protocol=udp action=drop dst-port=135-139 comment="messenger worm"
add chain=virus protocol=tcp action=drop dst-port=142 comment="NetTaxi"
add chain=virus protocol=tcp action=drop dst-port=146 comment="Infector"
add chain=virus protocol=udp action=drop dst-port=146 comment="Infector"
add chain=virus protocol=tcp action=drop dst-port=170 comment="A-trojan"
add chain=virus protocol=tcp action=drop dst-port=334 comment="Backage"
add chain=virus protocol=tcp action=drop dst-port=411 comment="Backage"
add chain=virus protocol=tcp action=drop dst-port=420 comment="Breach, Incognito"
add chain=virus protocol=tcp action=drop dst-port=421 comment="TCP Wrappers trojan"
add chain=virus protocol=tcp action=drop dst-port=445 comment="Blaster worm
add chain=virus protocol=udp action=drop dst-port=445 comment="Blaster worm
add chain=virus protocol=tcp action=drop dst-port=455 comment="Fatal Connections"
add chain=virus protocol=tcp action=drop dst-port=456 comment="Hackers Paradise"
add chain=virus protocol=tcp action=drop dst-port=513 comment="Grlogin"
add chain=virus protocol=tcp action=drop dst-port=514 comment="RPC Backdoor"
add chain=virus protocol=tcp action=drop dst-port=531 comment="Net666, Rasmin"
add chain=virus protocol=tcp action=drop dst-port=555 comment="711 trojan, Seven Eleven, Ini-Killer, Net Administrator, Phase Zero, Phase-0, Stealth Spy"
add chain=virus protocol=tcp action=drop dst-port=605 comment="Secret Service"
add chain=virus protocol=tcp action=drop dst-port=666 comment="Attack FTP, Back Construction, BLA trojan, Cain & Abel, NokNok, Satans Back Door SBD, ServU, Shadow Phyre, th3r1pp3rz Therippers"
add chain=virus protocol=tcp action=drop dst-port=667 comment="SniperNet"
add chain=virus protocol=tcp action=drop dst-port=669 comment="DP trojan"
add chain=virus protocol=tcp action=drop dst-port=692 comment="GayOL"
add chain=virus protocol=tcp action=drop dst-port=777 comment="AimSpy, Undetected"
add chain=virus protocol=tcp action=drop dst-port=808 comment="WinHole"
add chain=virus protocol=tcp action=drop dst-port=911 comment="Dark Shadow"
add chain=virus protocol=tcp action=drop dst-port=999 comment="Deep Throat, Foreplay, WinSatan"
add chain=virus protocol=tcp action=drop dst-port=1000 comment="Der Spaeher, Direct Connection"
add chain=virus protocol=tcp action=drop dst-port=1001 comment="Der Spaeher, Le Guardien, Silencer, WebEx"
add chain=virus protocol=tcp action=drop dst-port=1010-1016 comment="Doly Trojan"
add chain=virus protocol=tcp action=drop dst-port=1020 comment="Vampire"
add chain=virus protocol=tcp action=drop dst-port=1024 comment="Jade, Latinus, NetSpy"
add chain=virus protocol=tcp action=drop dst-port=1025 comment="Remote Storm"
add chain=virus protocol=udp action=drop dst-port=1025 comment="Remote Storm"
add chain=virus protocol=tcp action=drop dst-port=1035 comment="Multidropper"
add chain=virus protocol=tcp action=drop dst-port=1042 comment="BLA trojan"
add chain=virus protocol=tcp action=drop dst-port=1045 comment="Rasmin"
add chain=virus protocol=tcp action=drop dst-port=1049 comment="sbin initd"
add chain=virus protocol=tcp action=drop dst-port=1050 comment="MiniCommand"
add chain=virus protocol=tcp action=drop dst-port=1053 comment="The Thief"
add chain=virus protocol=tcp action=drop dst-port=1054 comment="AckCmd"
add chain=virus protocol=tcp action=drop dst-port=1080-1083 comment="WinHole"
add chain=virus protocol=tcp action=drop dst-port=1090 comment="Xtreme"
add chain=virus protocol=tcp action=drop dst-port=1095-1098 comment="Remote Administration Tool RAT"
add chain=virus protocol=tcp action=drop dst-port=1099 comment="Blood Fest Evolution, Remote Administration Tool RAT"
add chain=virus protocol=tcp action=drop dst-port=1150-1151 comment="Orion"
add chain=virus protocol=tcp action=drop dst-port=1170 comment="Psyber Stream Server PSS, Streaming Audio Server, Voice"
add chain=virus protocol=udp action=drop dst-port=1200-1201 comment="NoBackO"
add chain=virus protocol=tcp action=drop dst-port=1207 comment="SoftWAR"
add chain=virus protocol=tcp action=drop dst-port=1208 comment="Infector"
add chain=virus protocol=tcp action=drop dst-port=1212 comment="Kaos"
add chain=virus protocol=tcp action=drop dst-port=1234 comment="SubSeven Java client, Ultors Trojan"
add chain=virus protocol=tcp action=drop dst-port=1243 comment="BackDoor-G, SubSeven, SubSeven Apocalypse, Tiles"
add chain=virus protocol=tcp action=drop dst-port=1245 comment="VooDoo Doll"
add chain=virus protocol=tcp action=drop dst-port=1255 comment="Scarab"
add chain=virus protocol=tcp action=drop dst-port=1256 comment="Project nEXT"
add chain=virus protocol=tcp action=drop dst-port=1269 comment="Matrix"
add chain=virus protocol=tcp action=drop dst-port=1272 comment="The Matrix"
add chain=virus protocol=tcp action=drop dst-port=1313 comment="NETrojan"
add chain=virus protocol=tcp action=drop dst-port=1338 comment="Millenium Worm"
add chain=virus protocol=tcp action=drop dst-port=1349 comment="Bo dll"
add chain=virus protocol=tcp action=drop dst-port=1394 comment="GoFriller, Backdoor G-1"
add chain=virus protocol=tcp action=drop dst-port=1441 comment="Remote Storm"
add chain=virus protocol=tcp action=drop dst-port=1492 comment="FTP99CMP"
add chain=virus protocol=tcp action=drop dst-port=1524 comment="Trinoo"
add chain=virus protocol=tcp action=drop dst-port=1568 comment="Remote Hack"
add chain=virus protocol=tcp action=drop dst-port=1600 comment="Direct Connection, Shivka-Burka"
add chain=virus protocol=tcp action=drop dst-port=1703 comment="Exploiter"
add chain=virus protocol=tcp action=drop dst-port=1777 comment="Scarab"
add chain=virus protocol=tcp action=drop dst-port=1807 comment="SpySender"
add chain=virus protocol=tcp action=drop dst-port=1966 comment="Fake FTP"
add chain=virus protocol=tcp action=drop dst-port=1967 comment="WM FTP Server"
add chain=virus protocol=tcp action=drop dst-port=1969 comment="OpC BO"
add chain=virus protocol=tcp action=drop dst-port=1981 comment="Bowl, Shockrave"
add chain=virus protocol=tcp action=drop dst-port=1999 comment="Back Door, SubSeven, TransScout"
add chain=virus protocol=tcp action=drop dst-port=2000 comment="Der Spaeher, Insane Network, Last 2000, Remote Explorer 2000, Senna Spy Trojan Generator"
add chain=virus protocol=tcp action=drop dst-port=2001 comment="Der Spaeher, Trojan Cow"
add chain=virus protocol=tcp action=drop dst-port=2023 comment="Ripper Pro"
add chain=virus protocol=tcp action=drop dst-port=2080 comment="WinHole"
add chain=virus protocol=tcp action=drop dst-port=2115 comment="Bugs"
add chain=virus protocol=udp action=drop dst-port=2130 comment="Mini Backlash"
add chain=virus protocol=tcp action=drop dst-port=2140 comment="The Invasor"
add chain=virus protocol=udp action=drop dst-port=2140 comment="Deep Throat, Foreplay"
add chain=virus protocol=tcp action=drop dst-port=2155 comment="Illusion Mailer"
add chain=virus protocol=tcp action=drop dst-port=2255 comment="Nirvana"
add chain=virus protocol=tcp action=drop dst-port=2283 comment="Hvl RAT"
add chain=virus protocol=tcp action=drop dst-port=2300 comment="Xplorer"
add chain=virus protocol=tcp action=drop dst-port=2311 comment="Studio 54"
add chain=virus protocol=tcp action=drop dst-port=2330-2339 comment="Contact"
add chain=virus protocol=udp action=drop dst-port=2339 comment="Voice Spy"
add chain=virus protocol=tcp action=drop dst-port=2345 comment="Doly Trojan"
add chain=virus protocol=tcp action=drop dst-port=2565 comment="Striker trojan"
add chain=virus protocol=tcp action=drop dst-port=2583 comment="WinCrash"
add chain=virus protocol=tcp action=drop dst-port=2600 comment="Digital RootBeer"
add chain=virus protocol=tcp action=drop dst-port=2716 comment="The Prayer"
add chain=virus protocol=tcp action=drop dst-port=2773-2774 comment="SubSeven, SubSeven 2.1 Gold"
add chain=virus protocol=tcp action=drop dst-port=2801 comment="Phineas Phucker"
add chain=virus protocol=udp action=drop dst-port=2989 comment="Remote Administration Tool RAT"
add chain=virus protocol=tcp action=drop dst-port=3000 comment="Remote Shut"
add chain=virus protocol=tcp action=drop dst-port=3024 comment="WinCrash"
add chain=virus protocol=tcp action=drop dst-port=3031 comment="Microspy"
add chain=virus protocol=tcp action=drop dst-port=3128 comment="Reverse WWW Tunnel Backdoor, RingZero"
add chain=virus protocol=tcp action=drop dst-port=3129 comment="Masters Paradise"
add chain=virus protocol=tcp action=drop dst-port=3150 comment="The Invasor"
add chain=virus protocol=udp action=drop dst-port=3150 comment="Deep Throat, Foreplay, Mini Backlash"
add chain=virus protocol=tcp action=drop dst-port=3456 comment="Terror trojan"
add chain=virus protocol=tcp action=drop dst-port=3459 comment="Eclipse 2000, Sanctuary"
add chain=virus protocol=tcp action=drop dst-port=3700 comment="Portal of Doom"
add chain=virus protocol=tcp action=drop dst-port=3777 comment="PsychWard"
add chain=virus protocol=tcp action=drop dst-port=3791-3801 comment="Total Solar Eclypse"
add chain=virus protocol=tcp action=drop dst-port=4000 comment="SkyDance"
add chain=virus protocol=tcp action=drop dst-port=4092 comment="WinCrash"
add chain=virus protocol=tcp action=drop dst-port=4242 comment="Virtual Hacking Machine VHM"
add chain=virus protocol=tcp action=drop dst-port=4321 comment="BoBo"
add chain=virus protocol=tcp action=drop dst-port=4444 comment="Prosiak, Swift Remote"
add chain=virus protocol=tcp action=drop dst-port=4567 comment="File Nail"
add chain=virus protocol=tcp action=drop dst-port=4590 comment="ICQ Trojan"
add chain=virus protocol=tcp action=drop dst-port=4950 comment="ICQ Trogen Lm"
add chain=virus protocol=tcp action=drop dst-port=5000 comment="Back Door Setup, Blazer5, Bubbel, ICKiller, Ra1d, Sockets des Troie"
add chain=virus protocol=tcp action=drop dst-port=5001 comment="Back Door Setup, Sockets des Troie"
add chain=virus protocol=tcp action=drop dst-port=5002 comment="cd00r, Shaft"
add chain=virus protocol=tcp action=drop dst-port=5010 comment="Solo"
add chain=virus protocol=tcp action=drop dst-port=5011 comment="One of the Last Trojans OOTLT, One of the Last Trojans OOTLT, modified"
add chain=virus protocol=tcp action=drop dst-port=5025 comment="WM Remote KeyLogger"
add chain=virus protocol=tcp action=drop dst-port=5031-5032 comment="Net Metropolitan"
add chain=virus protocol=tcp action=drop dst-port=5321 comment="Firehotcker"
add chain=virus protocol=tcp action=drop dst-port=5333 comment="Backage, NetDemon"
add chain=virus protocol=tcp action=drop dst-port=5343 comment="wCrat WC Remote Administration Tool"
add chain=virus protocol=tcp action=drop dst-port=5400-5402 comment="Back Construction, Blade Runner"
add chain=virus protocol=tcp action=drop dst-port=5512 comment="Illusion Mailer"
add chain=virus protocol=tcp action=drop dst-port=5534 comment="The Flu"
add chain=virus protocol=tcp action=drop dst-port=5550 comment="Xtcp"
add chain=virus protocol=tcp action=drop dst-port=5555 comment="ServeMe"
add chain=virus protocol=tcp action=drop dst-port=5556-5557 comment="BO Facil"
add chain=virus protocol=tcp action=drop dst-port=5569 comment="Robo-Hack"
add chain=virus protocol=tcp action=drop dst-port=5637-5638 comment="PC Crasher"
add chain=virus protocol=tcp action=drop dst-port=5742 comment="WinCrash"
add chain=virus protocol=tcp action=drop dst-port=5760 comment="Portmap Remote Root Linux Exploit"
add chain=virus protocol=tcp action=drop dst-port=5880-5889 comment="Y3K RAT"
add chain=virus protocol=tcp action=drop dst-port=6000 comment="The Thing"
add chain=virus protocol=tcp action=drop dst-port=6006 comment="Bad Blood"
add chain=virus protocol=tcp action=drop dst-port=6272 comment="Secret Service"


File: /README.md
# firewall-mikrotik
using this script for block virus on port


