# Repository Information
Name: hass_mikrotik_sms

# Directory Structure
Directory structure:
└── github_repos/hass_mikrotik_sms/
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
    │   │       ├── pack-e1c22023f0fad10af1525680febef276fe83b605.idx
    │   │       └── pack-e1c22023f0fad10af1525680febef276fe83b605.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   ├── dependabot.yml
    │   └── workflows/
    │       ├── dependency-review.yml
    │       └── python-package.yml
    ├── .gitignore
    ├── .hintrc
    ├── .pre-commit-config.yaml
    │   ├── launch.json
    │   └── settings.json
    ├── conftest.py
    ├── custom_components/
    │   └── mikrotik_sms/
    │       ├── manifest.json
    │       ├── notify.py
    │       ├── services.yaml
    │       └── __init__.py
    ├── docs/
    │   └── index.md
    ├── hacs.json
    ├── info.md
    ├── LICENSE
    ├── mkdocs.yml
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    ├── requirements_docs.txt
    ├── requirements_test.txt
    └── tests/
        ├── test_notify.py
        └── __init__.py


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
	url = https://github.com/jeyrb/hass_mikrotik_sms.git
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
0000000000000000000000000000000000000000 9981f97666800a1e2c5c585bcd22a0b872cdc82d vivek-dodia <vivek.dodia@icloud.com> 1738606314 -0500	clone: from https://github.com/jeyrb/hass_mikrotik_sms.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 9981f97666800a1e2c5c585bcd22a0b872cdc82d vivek-dodia <vivek.dodia@icloud.com> 1738606314 -0500	clone: from https://github.com/jeyrb/hass_mikrotik_sms.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 9981f97666800a1e2c5c585bcd22a0b872cdc82d vivek-dodia <vivek.dodia@icloud.com> 1738606314 -0500	clone: from https://github.com/jeyrb/hass_mikrotik_sms.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
bd157a5616a511282108ae87e090d24a44cc4c96 refs/remotes/origin/gh-pages
9981f97666800a1e2c5c585bcd22a0b872cdc82d refs/remotes/origin/main
a99740fb425231cb9b84054e8b24bedf74835b43 refs/remotes/origin/master
9ad0ea5128e351a9dbe717e4046a916ffaa834ac refs/tags/0.1.0
44f9d00a4a891c3fd2c760f1ac6067e33f8ffe7d refs/tags/0.7.0
90b008f6a282d807c76091390c240c5e30728c9a refs/tags/0.8.0
845c08c851701575276292c4f2b8bf733d8c6cc0 refs/tags/0.9.0


File: /.git\refs\heads\main
9981f97666800a1e2c5c585bcd22a0b872cdc82d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.github\dependabot.yml
version: 2
updates:

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      # Check for updates to GitHub Actions every week
      interval: "weekly"

  - package-ecosystem: pip
    directory: "/"
    schedule:
      interval: weekly
      time: "13:00"
    groups:
      python-packages:
        patterns:
          - "*"


File: /.github\workflows\dependency-review.yml
# Dependency Review Action
#
# This Action will scan dependency manifest files that change as part of a Pull Request,
# surfacing known-vulnerable versions of the packages declared or updated in the PR.
# Once installed, if the workflow run is marked as required, PRs introducing known-vulnerable
# packages will be blocked from merging.
#
# Source repository: https://github.com/actions/dependency-review-action
# Public documentation: https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review#dependency-review-enforcement
name: 'Dependency review'
on:
  pull_request:
    branches: [ "main" ]

# If using a dependency submission action in this workflow this permission will need to be set to:
#
# permissions:
#   contents: write
#
# https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api
permissions:
  contents: read
  # Write permissions for pull-requests are required for using the `comment-summary-in-pr` option, comment out if you aren't using this option
  pull-requests: write

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - name: 'Checkout repository'
        uses: actions/checkout@v4
      - name: 'Dependency Review'
        uses: actions/dependency-review-action@v4
        # Commonly enabled options, see https://github.com/actions/dependency-review-action#configuration-options for all available options.
        with:
          comment-summary-in-pr: always
        #   fail-on-severity: moderate
        #   deny-licenses: GPL-1.0-or-later, LGPL-2.0-or-later
        #   retry-on-snapshot-warnings: true


File: /.github\workflows\python-package.yml
# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: MikrotikSMS

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.12"]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        if [ -f requirements_test.txt ]; then pip install -r requirements_test.txt; fi
    - name: Ruff
      uses: chartboost/ruff-action@v1
    - name: Test with pytest
      run: |
        pytest
    - name: HACS Action
      uses: "hacs/action@main"
      with:
        category: "integration"
        ignore: brands
    - name: Deploy docs
      uses: mhausenblas/mkdocs-deploy-gh-pages@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        REQUIREMENTS: requirements_docs.txt


File: /.gitignore
# Byte-compiled / optimized / DLL files
File: /.hintrc
{
    "connector": {
      "name": "local",
      "options": {
        "pattern": ["**", "!htmlcov/**"]
      }
    }
  }


File: /.pre-commit-config.yaml
default_language_version:
  python: python3.11

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.15.2
    hooks:
      - id: pyupgrade
        args: [--py311-plus]
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
     # Run the linter.
      - id: ruff
        args: [ --fix ]
      # Run the formatter.
      - id: ruff-format

  - repo: https://github.com/codespell-project/codespell
    rev: v2.2.6
    hooks:
      - id: codespell
        args:
          - --ignore-words-list=hass,alot,datas,dof,dur,farenheit,hist,iff,ines,ist,lightsensor,mut,nd,pres,referer,ser,serie,te,technik,ue,uint,visability,wan,wanna,withing
          - --skip="./.*,*.csv,*.json"
          - --quiet-level=2
        exclude_types: [csv, json]


  - repo: https://github.com/PyCQA/bandit
    rev: '1.7.8'
    hooks:
      - id: bandit
        args:
          - --quiet
        files: ^(custom_components)/.+\.py$
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: 'v4.6.0'
    hooks:
      - id: check-executables-have-shebangs
        stages: [manual]
      - id: check-json
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: 'v1.9.0'
    hooks:
      - id: mypy
        args:
          - --pretty
          - --explicit-package-bases
          - --show-error-codes
          - --show-error-context
        additional_dependencies:
          - homeassistant-stubs==2024.2.2
          - types-python-slugify==8.0.0.2
          - voluptuous-stubs==0.1.1
          - pytest
          - phonenumbers
          - async_timeout
          - RouterOS-api


File: /.vscode\launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug Tests",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "purpose": ["debug-test"],
            "console": "integratedTerminal",
            "env": {
                "PYTEST_ADDOPTS": "--no-cov"
            },
            "justMyCode": false
        }
    ]
}


File: /.vscode\settings.json
{
    "files.associations": {
        "*.yaml": "home-assistant"
    },
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "flake8.args": [
        "--max-line-length=128"
    ],
    "python.analysis.include": [
        "custom_components/mikrotik_sms/**",
        "tests/**",
        "conftest.py"
    ],
    "python.analysis.autoImportCompletions": true,
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.inlayHints.callArgumentNames": "all",
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.pytestParameters": true,
    "python.analysis.inlayHints.variableTypes": true
}


File: /conftest.py
from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations in all tests."""
    return


# This fixture is used to prevent HomeAssistant from attempting to create and dismiss persistent
# notifications. These calls would fail without this fixture since the persistent_notification
# integration is never loaded during a test.


@pytest.fixture(name="skip_notifications", autouse=True)
def skip_notifications_fixture():
    """Skip notification calls."""
    with (
        patch("homeassistant.components.persistent_notification.async_create"),
        patch("homeassistant.components.persistent_notification.async_dismiss"),
    ):
        yield


File: /custom_components\mikrotik_sms\manifest.json
{
    "domain":"mikrotik_sms",
    "name":"Mikrotik SMS",
    "version":"0.9.1",
    "requirements":[
        "RouterOS-api==0.17.0",
        "phonenumbers>=8.13.0"
    ],
    "iot_class":"local_push",
    "config_flow": false,
    "documentation": "https://github.com/jeyrb/hass_mikrotik_sms",
    "issue_tracker": "https://github.com/jeyrb/hass_mikrotik_sms/issues",
    "codeowners":["@jeyrb"]

    }


File: /custom_components\mikrotik_sms\notify.py
import logging

import async_timeout
import routeros_api  # type: ignore
import voluptuous as vol
from homeassistant.components.notify import ATTR_DATA, ATTR_TARGET, PLATFORM_SCHEMA, BaseNotificationService
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.reload import async_setup_reload_service
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    country_code_for_region,
    format_number,
    is_valid_number,
    number_type,
    parse,
)

from . import (
    CONF_BAN_PREMIUM,
    CONF_COUNTRY_CODES_ALLOWED,
    CONF_SMSC,
    CONF_TIMEOUT,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_USERNAME,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.NOTIFY]

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
    vol.Required(CONF_USERNAME, default=DEFAULT_USERNAME): str,
    vol.Required(CONF_PASSWORD): str,
    vol.Optional(CONF_PORT, default=DEFAULT_PORT): str,
    vol.Optional(CONF_SMSC): str,
    vol.Optional(CONF_TIMEOUT, default=20): int,
    vol.Optional(CONF_COUNTRY_CODES_ALLOWED, default=[]): vol.All(cv.ensure_list, [cv.positive_int]),
    vol.Optional(CONF_BAN_PREMIUM, default=True): bool,
})


class MikrotikSMSNotificationService(BaseNotificationService):
    """Implement MikroTik SMS notification service."""

    def __init__(
        self,
        hass: HomeAssistant,
        host: str | None = None,
        port: str | None = DEFAULT_PORT,
        username: str | None = None,
        password: str | None = None,
        timeout: int = 20,
        smsc: str | None = None,
        country_codes_allowed: list[int] | None = None,
        ban_premium: bool = True,
    ) -> None:
        """Initialize the service."""
        self.hass = hass
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.smsc = str(smsc) if smsc is not None else None
        self.timeout = timeout
        self.region = hass.config.country
        self.ban_premium = ban_premium
        self.country_codes_allowed = country_codes_allowed or []
        if self.region:
            self.country_codes_allowed.append(country_code_for_region(self.region))

    async def initialize(self) -> None:
        await self.validate_connection()

    def get_conn(self) -> routeros_api.RouterOsApiPool:
        if self.username is None or self.password is None:
            _LOGGER.error("MIKROSMS Username or Password not set")
            raise ValueError("MIKROSMS Username or Password not set")
        _LOGGER.info("MIKROSMS Connecting to %s as %s", self.host, self.username)
        return routeros_api.RouterOsApiPool(self.host, self.username, self.password, plaintext_login=True)

    async def validate_connection(self) -> None:
        conn = self.get_conn()
        async with async_timeout.timeout(self.timeout):
            r = conn.get_api().get_resource("/").call("tool/sms/print")
        _LOGGER.debug("Connected: %s", r)

    async def async_send_message(self, message: str = "", **kwargs) -> None:
        """Send a message via mikrotik router."""
        _LOGGER.debug("Message: %s, kwargs: %s", message, kwargs)
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA)
        if not targets:
            _LOGGER.info("At least 1 target phone number is required")
            return
        if len(message) > 160:
            _LOGGER.warning("Message > 160 (%s chars), truncating", len(message))
            message = message[:160]
        channel = sms_type = None
        if data:
            channel = data.get("channel")
            sms_type = data.get("type")
            if sms_type not in ("ussd", "class-0", "class-1", None):
                _LOGGER.warning("Unknown SMS type %s", sms_type)

        conn: routeros_api.RouterOsApiPool | None = None
        try:
            conn = self.get_conn()
            for target in targets:
                try:
                    payload = {
                        "port": self.port,
                        "phone-number": self.validated_number(target),
                        "message": message,
                    }
                    if channel is not None:
                        payload["channel"] = channel
                    if sms_type is not None:
                        payload["type"] = sms_type
                    if self.smsc is not None:
                        payload["smsc"] = self.smsc

                    async with async_timeout.timeout(self.timeout):
                        _LOGGER.debug("MIKROSMS %s:%s", self.host, self.port)
                        r = conn.get_api().get_resource("/").call("tool/sms/send", payload)
                        _LOGGER.debug("MIKROSMS Sent to %s with response %s, payload: %s", target, r, payload)
                except TimeoutError:
                    _LOGGER.error("Timeout accessing Mikrotik at %s:%s", self.host, self.port)
        finally:
            if conn is not None:
                conn.disconnect()

    def validated_number(self, number: str | int) -> str:
        try:
            phone_number = parse(str(number), self.region)
            if not is_valid_number(phone_number):
                raise InvalidNumber("Invalid phone number %s" % number)
            if phone_number.country_code not in self.country_codes_allowed and 0 not in self.country_codes_allowed:
                raise DisallowedNumber("Disallowed country code %s" % phone_number.country_code)
            if self.ban_premium and number_type(phone_number) == PhoneNumberType.PREMIUM_RATE:
                _LOGGER.warning("Disallowed premium rate number %s", number)
                raise DisallowedNumber("Disallowed premium rate number %s" % number)
            return format_number(phone_number, PhoneNumberFormat.E164)
        except NumberParseException as e:
            _LOGGER.error("Invalid phone number %s: %s", number, e)
            raise InvalidNumber(e) from e


class DisallowedNumber(BaseException):
    pass


class InvalidNumber(BaseException):
    pass


async def async_get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,  # noqa: ARG001
) -> MikrotikSMSNotificationService:
    hass.states.async_set(
        "%s.configured" % DOMAIN,
        True,
        {
            CONF_HOST: config.get(CONF_HOST),
            CONF_PORT: config.get(CONF_PORT),
            CONF_USERNAME: config.get(CONF_USERNAME),
            CONF_SMSC: config.get(CONF_SMSC),
            CONF_COUNTRY_CODES_ALLOWED: config.get(CONF_COUNTRY_CODES_ALLOWED),
            CONF_BAN_PREMIUM: config.get(CONF_BAN_PREMIUM),
        },
    )
    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)
    service = MikrotikSMSNotificationService(
        hass,
        config.get(CONF_HOST),
        config.get(CONF_PORT),
        config.get(CONF_USERNAME),
        config.get(CONF_PASSWORD),
        config.get(CONF_TIMEOUT, 10),
        config.get(CONF_SMSC),
        config.get(CONF_COUNTRY_CODES_ALLOWED),
        config.get(CONF_BAN_PREMIUM, True),
    )
    await service.initialize()
    return service


File: /custom_components\mikrotik_sms\services.yaml
reload:
  name: Reload
  description: Reload sms notify services.


File: /custom_components\mikrotik_sms\__init__.py
"""The Mikrotik SMS notification integration"""

import logging

DOMAIN = "mikrotik_sms"

PLATFORMS = ["notify"]

DEFAULT_HOST = "192.168.88.200"
DEFAULT_USERNAME = "hass"
DEFAULT_PORT = "lte1"
CONF_SMSC = "smscentre"
CONF_TIMEOUT = "timeout"
CONF_COUNTRY_CODES_ALLOWED = "country_codes_allowed"
CONF_BAN_PREMIUM = "ban_premium"

_LOGGER = logging.getLogger(__name__)


File: /docs\index.md
--8<-- "README.md"


File: /hacs.json
{
    "name": "Mikrotik SMS",
    "homeassistant": "2012.7.0",
    "render_readme": true
}


File: /info.md
SMS service using Mikrotik API to send via LTE modem.


File: /LICENSE
This software is unlicensed and reserved for the private use of the original developer.


File: /mkdocs.yml
site_name: Home Assistant Mikrotik SMS
site_url: https://jeyrb.github.io/hass_mikrotik_sms/
site_description: Notify via SMS text message for Mikrotik 4G modems
repo_name: jeyrb/hass_mikrotik_sms
repo_url: https://github.com/jeyrb/hass_mikrotik_sms

theme:
  name: material
  highlightjs: true
  features:
    - content.code.copy
    - content.code.select
    - content.code.annotate
plugins:
  - search
  - mkdocstrings:
      handlers:
        # See: https://mkdocstrings.github.io/python/usage/
        python:
          options:
            docstring_style: sphinx
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.superfences
  - smarty
  - toc:
      permalink: true
  - sane_lists
  - pymdownx.snippets:
      check_paths: true


File: /pyproject.toml
[project]
name = "mikrotik_sms"
readme = "README.md"

[tool.ruff]
line-length = 128
indent-width = 4
target-version = "py312"
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "htmlcov",
    ".mypy_cache",
    ".pytest_cache",
    ".github",
    "node_modules",
    "site-packages",
    "venv",
]

[tool.ruff.lint]
preview = false
select = ["E", "C","R", "F", "B", "W", "I", "C90", "N", "D", "UP", "YTT",
"RUF","PGH","PT","T20","DTZ","TD","PTH","ARG","INT","TCH","TID","SIM","PERF","ASYNC","ANN","S","A","COM","C4"]
ignore = [
    "W191","E111","E114","E117","D206","D300","Q000","Q001","COM812","COM819","ISC001","ISC002", # std formatter conflicts
    "D203","D213", # other formatter clashes
    "TD002","TD003","TD005","SIM102","SIM117","ANN002", "ANN003","SIM108",
    "D103","D100","D101","D102","D104","D107","D415","D400","D415","ANN101","ANN401",
    "S101","C901","FURB113","PGH003",
    "S602","S607"] # subprocess usage
unfixable = ["B"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = []
"**/{tests,docs}/*" = ["ANN201","ANN204","ANN001","ARG002","ARG001","ANN202","PT004","ARG001","SIM115"]
"conftest.py" = ["ANN201","ANN204","ANN001","ARG002","ARG001","ANN202","PT004","ARG001","SIM115"]

[tool.ruff.format]
preview = true

[tool.poetry.group.dev.dependencies]
homeassistant-stubs = "2024.2.2"

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = [
    "tests",
]
norecursedirs = [
    ".git",
    "templates",
]

addopts = [
    "--timeout=30",
    "--cov-report=xml:cov.xml",
    "--cov-report=html",
    "--cov-report=term-missing",
    "--cov=custom_components.mikrotik_sms",
    "--cov-fail-under=50"
]


File: /README.md
[![Rhizomatics Open Source](https://avatars.githubusercontent.com/u/162821163?s=96&v=4)](https://github.com/rhizomatics)

# Mikrotik SMS Notifier

Notify using SMS service via LTE modem on a Mikrotik router.

Sends to multiple notify targets, where each target is a phone number,
optionally using E.164 international style.

Filter out broken numbers, and control for premium rate and international numbers.

## Setup

Register this GitHub repo as a custom repo
in your [HACS]( https://hacs.xyz) configuration.

A username and password is required on the Mikrotik router.

Configure in the main Home Assistant config yaml, or an included notify.yaml

```yaml
- name: Mikrotik SMS
  platform: mikrotik_sms
  host: 192.168.88.200
  username: !secret mikrotik_user
  password: !secret mikrotik_password
  port: lte1
  ban_premium: true # default
  country_codes_allowed: 91, 43 # automatically adds country code for Home Assistant configured region
```

With the user and password added to the HomeAssistant `secrets.yaml` file

Optionally an `smscentre` can be configured, and also `timeout` in seconds tuned ( default 20 seconds).

To allow calling to any international code, use `0` as the wildcard in `country_codes_allowed`

## Options

In the notification data section, `type` and `channel` can optionally be specified.
See the Mikrotik documentation for understanding of those.

## Reference
https://wiki.mikrotik.com/wiki/Manual:Tools/Sms

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)


File: /requirements.txt
homeassistant>=2024.2.2
RouterOS-api>=0.17.0
async_timeout
phonenumbers>=8.13.0


File: /requirements_docs.txt
mkdocstrings
pymdown-extensions
mkdocs-material


File: /requirements_test.txt
pytest>=7.4.3
pytest-cov
pytest-homeassistant-custom-component>=0.13.88
pytest-asyncio
pytest-unordered
pylint
homeassistant-stubs==2024.2.2


File: /tests\test_notify.py
from unittest.mock import AsyncMock, Mock, patch

import pytest

from custom_components.mikrotik_sms.notify import DisallowedNumber, InvalidNumber, MikrotikSMSNotificationService


async def test_send_message() -> None:
    hass = Mock()
    hass.states = Mock()
    hass.config.country = "GB"
    hass.services.async_call = AsyncMock()
    with patch("custom_components.mikrotik_sms.notify.routeros_api.RouterOsApiPool") as mock_api:
        uut = MikrotikSMSNotificationService(
            hass,
            host="127.0.0.1",
            port="lte5",
            username="mikro_test",
            password="mikro_pass",  # noqa: S106
            timeout=10,
        )

        await uut.initialize()
        mock_api.assert_called_with("127.0.0.1", "mikro_test", "mikro_pass", plaintext_login=True)

        await uut.async_send_message(message="testing 123", target=["+441234999888"], data={"type": "ussd"})
        mock_call = mock_api().get_api().get_resource().call
        mock_call.assert_called_with(
            "tool/sms/send", {"port": 9000, "phone-number": "+441234999888", "message": "testing 123", "type": "ussd"}
        )


def test_phone_number_checks() -> None:
    hass = Mock()
    hass.config.country = "GB"
    uut = MikrotikSMSNotificationService(hass)
    assert uut.validated_number("07386404283") == "+447386404283"
    assert uut.validated_number("+447386404283") == "+447386404283"
    with pytest.raises(InvalidNumber):
        uut.validated_number("010 5932 8484 1234")
    with pytest.raises(DisallowedNumber):
        uut.validated_number("+917386404283")
    with pytest.raises(DisallowedNumber):
        uut.validated_number("090 5932 1234")

    uut = MikrotikSMSNotificationService(hass, country_codes_allowed=[91])
    assert uut.validated_number("+917386404283") == "+917386404283"


