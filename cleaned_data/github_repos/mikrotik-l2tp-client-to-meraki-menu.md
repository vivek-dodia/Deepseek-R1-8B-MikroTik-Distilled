# Repository Information
Name: mikrotik-l2tp-client-to-meraki-menu

# Directory Structure
Directory structure:
└── github_repos/mikrotik-l2tp-client-to-meraki-menu/
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
    │   │       ├── pack-3eadc2b44e66804cb4ba1c3e98c06e43a0a4c2bf.idx
    │   │       └── pack-3eadc2b44e66804cb4ba1c3e98c06e43a0a4c2bf.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── ISSUE_TEMPLATE/
    │       └── bug_report.md
    ├── CODE_OF_CONDUCT.md
    ├── LICENSE.md
    ├── Meraki VPN Interactive Menu.rsc
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
	url = https://github.com/lightbulb703/mikrotik-l2tp-client-to-meraki-menu.git
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
0000000000000000000000000000000000000000 62e421d622dfe1c0991b116a8d71f99bdc5936b2 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/lightbulb703/mikrotik-l2tp-client-to-meraki-menu.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 62e421d622dfe1c0991b116a8d71f99bdc5936b2 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/lightbulb703/mikrotik-l2tp-client-to-meraki-menu.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 62e421d622dfe1c0991b116a8d71f99bdc5936b2 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/lightbulb703/mikrotik-l2tp-client-to-meraki-menu.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
62e421d622dfe1c0991b116a8d71f99bdc5936b2 refs/remotes/origin/master


File: /.git\refs\heads\master
62e421d622dfe1c0991b116a8d71f99bdc5936b2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\ISSUE_TEMPLATE\bug_report.md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. iOS]
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]

**Smartphone (please complete the following information):**
 - Device: [e.g. iPhone6]
 - OS: [e.g. iOS8.1]
 - Browser [e.g. stock browser, safari]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.


File: /CODE_OF_CONDUCT.md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at dennis@lbsys.xyz. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq


File: /LICENSE.md
MIT License

Copyright (c) 2020 Dennis Cole III

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


File: /Meraki VPN Interactive Menu.rsc
# Meraki VPN Interactive Menu
# Enable a L2TP client configured to connect to a Meraki from a Mikrotik Router
# Version 0.1.2
# Author: Dennis Cole III
# License: MIT
#
# Prerequisites:
# (Common Settings - these should always be enabled, firewall rule preference
# may need to be adjusted)
####
## Meraki profile
# /ppp profile add name=meraki use-encryption=required use-ipv6=no \
#  use-mpls=no
##
## Set ipsec profile and proposal, 3des and aes128, group2 and group5
# /ip ipsec profile set [ find default=yes ] dh-group=modp1536,modp1024 \
#  lifetime=8h
# /ip ipsec proposal set [ find default=yes ] \
#  enc-algorithms=aes-128-cbc,3des lifetime=8h pfs-group=none
##
## Mark routing for traffic from only allowed sources
# /ip firewall mangle add action=mark-routing chain=prerouting \
#  comment="Leave this enabled always" new-routing-mark=merakivpns \
#  passthrough=yes src-address-list="Source VPN Addresses"
##
## Address List
## Sample of two shown below. Use as many or as few as needed.
# /ip firewall address-list add address=LOCALADDRESS1 \
#  list="Source VPN Addresses"
# /ip firewall address-list add address=LOCALADDRESS2 \
#  list="Source VPN Addresses"
####
# Per Client Settings (firewall rule preference may need to be adjusted):
# /interface l2tp-client add allow=pap comment=CLIENTNAME connect-to=\
#  DESTINATION ipsec-secret=SECRET name=l2tp-out1 password=PASSWORD profile=\
#  meraki use-ipsec=yes user="DOMAIN\\user||user@domain.com||user"
# /interface l2tp-client disable name=l2tp-out1
##
## Address List
## Sample of two shown below. Use as many or as few as needed.
# /ip firewall address-list add address=DSTADDRESS1 list=CLIENTNAME
# /ip firewall address-list add address=DSTADDRESS2 list=CLIENTNAME
##
## Firewall rule to NAT traffic for valid sources addresses to
## destination routes
# /ip firewall nat add action=masquerade chain=srcnat comment=CLIENTNAME \
# disabled=yes dst-address-list=CLIENTNAME out-interface=l2tp-out1 \
# src-address-list="Source VPN Addresses"
##
## Routes
## Sample of two shown below. Use as many or as few as needed.
# /ip route add comment=CLIENTNAME disabled=yes distance=1 dst-address=\
# DSTADDRESS1 gateway=l2tp-out1 routing-mark=merakivpns
# /ip route add comment=CLIENTNAME disabled=yes distance=1 dst-address=\
# DSTADDRESS2 gateway=l2tp-out1 routing-mark=merakivpns
####

# Function to get input
:global read do={:return}

# Funtion to enable or disable L2TP Client
:global changeClient do={
  # Getting our NAT rules and routes
  :local natRule [/ip firewall nat find where comment=$clientName]
  :local routes [/ip route find where comment=$clientName]

  # Boolean variables
  :local l2tpInterfaceChangeStatus true
  :local natRuleChangeStatus true
  :local oneRouteChangeStatus
  :local partialRouteChanges
  :local allRoutesChangeStatus true

  # Message and other variables
  :local done "..OK!"
  :local halfDone "..some failed!"
  :local failed "..FAILED!"
  :local lowerPrefix
  :local upperPrefix
  # Delay between command execution
  :local delayTime 500ms

  if ($change="enable") do={
    :set lowerPrefix "en"
    :set upperPrefix "En"
  } else={
    :set lowerPrefix "dis"
    :set upperPrefix "Dis"
  }

  # L2TP Client Enable/Disable
  if ($change="enable") do={
    do {
      /interface l2tp-client enable [find comment=$clientName]
    } on-error={
      :set $l2tpInterfaceChangeStatus false
    }
  } else={
    do {
      /interface l2tp-client disable [find comment=$clientName]
    } on-error={
      :set $l2tpInterfaceChangeStatus false
    }
  }
  delay $delayTime
  if ($l2tpInterfaceChangeStatus) do={
    :put ($upperPrefix . "abling L2TP Client for $clientName." . $done)
  } else={
    :put ($upperPrefix . "abling L2TP Client for $clientName." . $failed)
  }

  # NAT Rule Change
  if ($change="enable") do={
    do {
      /ip firewall nat enable [find comment=$clientName]
    } on-error={
      :set $natRuleChangeStatus false
    }
  } else={
    do {
      /ip firewall nat disable [find comment=$clientName]
    } on-error={
      :set $natRuleChangeStatus false
    }
  }
  delay $delayTime
  if ($natRuleChangeStatus) do={
    :put ($upperPrefix . "abling NAT rule for $clientName." . $done)
  } else={
    :put ($upperPrefix . "abling NAT rule for $clientName." . $failed)
  }

  # Route Changes
  delay $delayTime
  :put ($upperPrefix . "abling routes for $clientName:")
  delay $delayTime
  foreach route in $routes do={
    :set $oneRouteChangeStatus true
    :local dstAddress [/ip route get value-name=dst-address \
      [find where .id=$route]]
    if ($change="enable") do={
      do {
        /ip route enable [find .id=$route]
      } on-error={
        :set $oneRouteChangeStatus false
      }
    } else={
      do {
        /ip route disable [find .id=$route]
      } on-error={
        :set $oneRouteChangeStatus false
      }
    }
    delay $delayTime
    :set $allRoutesChangeStatus ($oneRouteChangeStatus && \
      $allRoutesChangeStatus)
    if ($oneRouteChangeStatus) do={
      :set $partialRouteChanges true
      :put "  - $dstAddress.$done"
    } else={
      :put "  - $dstAddress.$done"
    }
  }
  if ($allRoutesChangeStatus) do={:put ("Route changes" . $done)} else={
    if ($partialRouteChanges) do={:put ("Route changes" . $halfDone)} else={
      :put ("Routes changes" . $failed)
    }
  }

  # Verification
  if ($l2tpInterfaceChangeStatus && $natRuleChangeStatus && \
    $allRoutesChangeStatus) do={
    :put ("All rules for $clientName have been $lowerPrefix" . "abled" . $done)
    if ($change="enable") do={
      :put ("Checking status of the VPN connection...")
      :local numberOfChecks 0
      :local vpnIsUp
      while ($numberOfChecks < 5) do={
        :delay 5s
        :set vpnIsUp [/interface l2tp-client get [find comment=$clientName] running]
        if ($vpnIsUp) do={
          :put ("VPN connection is UP!")
          :set $numberOfChecks 5
        } else={
          :set $numberOfChecks ($numberOfChecks+1)
          if ($numberOfChecks < 5) do={
           :put ("VPN connection is not yet up. Try $numberOfChecks of 5 tries...")
          } else={
           :put ("VPN connection is not yet up. You may need to check your settings.")
          }
        }
      }
    }
  } else={
    if ($l2tpInterfaceChangeStatus || $natRuleChangeStatus || \
      $allRoutesChangeStatus) do={
      :put ("Some rules were not $lowerPrefix" . "abled.")
    } else={
        :put "All rule changes failed."
    }
  }
}

# Main routine

# Boolean variables
:local skipEnable false

# Message variables
:local goodbye "Goodbye!"

# Check for Active L2TP Clients
:local merakiL2tpActive [/interface l2tp-client find where profile="meraki" \
  disabled=no]

# If there are Active L2TP Clients, we want to disable first.
foreach merakiClient in=$merakiL2tpActive do={
  # Getting Info on the Active Client
  :local clientName [/interface l2tp-client get \
    [find where .id=$merakiClient] value-name=comment]

  # Ask to disable Active Client
  :local vpnIsUp [/interface l2tp-client get [find comment=$clientName] running]
   if ($vpnIsUp) do={
      :put "$clientName is currently enabled and the VPN connection is UP! Would you like to disable (Y/n)?"
   } else={
      :put "$clientName is currently enabled, however the VPN connection is down. Would you like to disable (Y/n)?"
   }
  :local userinput [$read]
  if ( $userinput = "n" || $userinput = "N") do={
    # We don't want to disable so we will end the script
    :set $skipEnable true
    :put $goodbye
  } else={
    # We will disable all rules
    $changeClient clientName=$clientName change="disable"

    # Do we want to enable another client?
    :put "Do you want to enable another VPN (y/N)?"
    :local userinput [$read]
    if (!( $userinput = "y" || $userinput = "Y")) do={
     :set $skipEnable true
     :put $goodbye
    }
  }
}

# Now asking what VPN do we want to enable, that is, if we are not skipping
if (!$skipEnable) do={
  :local merakiL2tpInactive [/interface l2tp-client find where \
    profile="meraki" disabled=yes]
  :local merakiClientsbyName [ :toarray "" ]

  # Get all Meraki L2TP Clients
  foreach merakiClient in=$merakiL2tpInactive do={
    :local clientName [/interface l2tp-client get \
      [find where .id=$merakiClient] value-name=comment]
    :set merakiClientsbyName ( $merakiClientsbyName, $clientName )
  }
  # List Clients
  :local i 1
  :local numOfClients [ :len $merakiClientsbyName ]
  :put "List of Meraki L2TP Clients"
  foreach clientName in $merakiClientsbyName do={
    if (i < 10) do={
      :put "   $i.  $clientName"
    } else={
      :put "  $i.  $clientName"
    }
    :set i ($i+1)
  }
  :put "   X.  Exit"

  # Decide which client to enable
  :put "What client would you like to enable? (1-$numOfClients or eXit)"
  :local userinput [$read]
  if ([:typeof $userinput] = "num") do={
    # Choice needs to be 1 less
    :local choice ($userinput-1)
    if ($choice >= 0 && $choice < [:len $merakiClientsbyName]) do={
      $changeClient clientName=($merakiClientsbyName->$choice) change="enable"
    } else={
      :put $goodbye
    }
  } else={
    :put $goodbye
  }
}


File: /README.md
# Mikrotik script - Meraki VPN Interactive Menu

Scenario:
You configure your Mikrotik router to be a L2TP Client to a Meraki. You may
  have a few L2TP clients setup this way. This interactive script (only
  via **ssh** or **telnet**) will search for clients and enable or disable the
  one you select.

The script identifies clients by the comment on the L2TP interface, NAT rule
  and Routes. Therefore, the comment must be exactly the same on all three types.

The L2TP interfaces need to use a profile named **meraki** for the detection
  to work (setup below).

The script will check for an active VPN first, which must be disabled prior
  to enabling a new VPN.

## Prerequisite setup
Common Settings (this should always be enabled, firewall rule preference may
  need to be adjusted):

    # Meraki profile
    /ppp profile add name=meraki use-encryption=required use-ipv6=no \
     use-mpls=no

    # Set ipsec profile and proposal, 3des and aes128, group2 and group5
    /ip ipsec profile set [ find default=yes ] dh-group=modp1536,modp1024 \
     lifetime=8h
    /ip ipsec proposal set [ find default=yes ] \
     enc-algorithms=aes-128-cbc,3des lifetime=8h pfs-group=none

    # Mark routing for traffic from only allowed sources
    /ip firewall mangle add action=mark-routing chain=prerouting \
     comment="Leave this enabled always" new-routing-mark=merakivpns \
     passthrough=yes src-address-list="Source VPN Addresses"

    # Address List
    # Sample of two shown below. Use as many or as few as needed.
    /ip firewall address-list add address=LOCALADDRESS1 \
     list="Source VPN Addresses"
    /ip firewall address-list add address=LOCALADDRESS2 \
     list="Source VPN Addresses"


Per Client Settings (firewall rule preference may need to be adjusted):

    # L2TP Client Setup, take note of the interface name
    /interface l2tp-client add allow=pap comment=CLIENTNAME \
     connect-to=DESTINATION ipsec-secret=SECRET name=l2tp-out1 \
     password=PASSWORD profile=meraki use-ipsec=yes \
     user="DOMAIN\\user||user@domain.com||user"
    /interface l2tp-client disable name=l2tp-out1

    # Address List
    # Sample of two shown below. Use as many or as few as needed.
    /ip firewall address-list add address=DSTADDRESS1 list=CLIENTNAME
    /ip firewall address-list add address=DSTADDRESS2 list=CLIENTNAME

    # Firewall rule to NAT traffic for valid sources addresses to
    # destination routes
    /ip firewall nat add action=masquerade chain=srcnat comment=CLIENTNAME \
     disabled=yes dst-address-list=CLIENTNAME out-interface=l2tp-out1 \
     src-address-list="Source VPN Addresses"

    # Routes
    # Sample of two shown below. Use as many or as few as needed.
    /ip route add comment=CLIENTNAME disabled=yes distance=1 \
     dst-address=DSTADDRESS1 gateway=l2tp-out1 routing-mark=merakivpns
    /ip route add comment=CLIENTNAME disabled=yes distance=1 \
     dst-address=DSTADDRESS2 gateway=l2tp-out1 routing-mark=merakivpns

## Sample Runs
Enable (detected no active VPNs):

    List of Meraki L2TP Clients
      1.  Client A
      2.  Client B
      3.  Client C
      4.  Client D
      5.  Client E
      X.  Exit
    What client would you like to enable? (1-5 or eXit)
    value: 4
    Enabling L2TP Client for Client D...OK!
    Enabling NAT rule for Client D...OK!
    Enabling routes for Client D:
      - 10.0.0.0/11....OK!
      - 192.168.0.0/19....OK!
    Route changes..OK!
    Checking status of the VPN connection...
    All rules for Client D have been enabled!

Disable (active VPN detected, will ask if you want to enable a new VPN):

    Client D Backup is currently enabledand the VPN connection is UP! Would you like to disable (Y/n)?
    value: y
    Disabling L2TP Client for Client D...OK!
    Disabling NAT rule for Client D...OK!
    Disabling routes for Client D:
      - 10.0.0.0/11....OK!
      - 192.168.0.0/19....OK!
    Route changes..OK!
    All rules for Client D have been disabled!
    Do you want to enable another VPN (y/N)?
    value: n
    Goodbye!


