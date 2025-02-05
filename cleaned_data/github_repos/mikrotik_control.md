# Repository Information
Name: mikrotik_control

# Directory Structure
Directory structure:
└── github_repos/mikrotik_control/
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
    │   │       ├── pack-7cd5342ab576861ae02365346faafbdfacf3b0da.idx
    │   │       └── pack-7cd5342ab576861ae02365346faafbdfacf3b0da.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── c
    ├── control.py
    ├── libs/
    │   ├── capsman/
    │   │   ├── accesslistmenu.py
    │   │   ├── acl.py
    │   │   ├── capsman.py
    │   │   └── capsmanmenu.py
    │   ├── cls.py
    │   ├── configuration.py
    │   ├── cprint.py
    │   ├── device.py
    │   ├── devicecreatedialog.py
    │   ├── devicehandler.py
    │   ├── devicemenu.py
    │   ├── devicesmenu.py
    │   ├── group.py
    │   ├── grouphandler.py
    │   ├── interface.py
    │   ├── ip/
    │   │   └── dhcp-server.py
    │   ├── mainmenu.py
    │   ├── program.py
    │   ├── script.py
    │   ├── scripthandler.py
    │   ├── scriptmenu.py
    │   ├── scriptsmenu.py
    │   └── __init__.py
    ├── LICENSE
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
	url = https://github.com/spidermila/mikrotik_control.git
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
0000000000000000000000000000000000000000 196b1dd19cd46156cbf779f5af7f9232ab1e6aaf vivek-dodia <vivek.dodia@icloud.com> 1738606089 -0500	clone: from https://github.com/spidermila/mikrotik_control.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 196b1dd19cd46156cbf779f5af7f9232ab1e6aaf vivek-dodia <vivek.dodia@icloud.com> 1738606089 -0500	clone: from https://github.com/spidermila/mikrotik_control.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 196b1dd19cd46156cbf779f5af7f9232ab1e6aaf vivek-dodia <vivek.dodia@icloud.com> 1738606089 -0500	clone: from https://github.com/spidermila/mikrotik_control.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
196b1dd19cd46156cbf779f5af7f9232ab1e6aaf refs/remotes/origin/main


File: /.git\refs\heads\main
196b1dd19cd46156cbf779f5af7f9232ab1e6aaf


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
# Byte-compiled / optimized / DLL files
File: /.pre-commit-config.yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-docstring-first
    -   id: check-yaml
    -   id: debug-statements
    -   id: double-quote-string-fixer
-   repo: https://github.com/PyCQA/flake8
    rev: 7.1.1
    hooks:
    -   id: flake8
-   repo: https://github.com/asottile/reorder-python-imports
    rev: v3.14.0
    hooks:
    -   id: reorder-python-imports
        args: [--py3-plus]
-   repo: https://github.com/asottile/add-trailing-comma
    rev: v3.1.0
    hooks:
    -   id: add-trailing-comma
        args: [--py36-plus]
-   repo: https://github.com/asottile/pyupgrade
    rev: v3.19.1
    hooks:
    -   id: pyupgrade
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.14.1
    hooks:
    -   id: mypy
        additional_dependencies: [types-PyYAML, types-paramiko]


File: /c
. venv/bin/activate
python control.py


File: /control.py
from libs.program import Program


def main() -> int:
    program = Program()
    program.run()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


File: /libs\capsman\accesslistmenu.py
# import getpass
# from typing import List
# from typing import Optional
from libs.configuration import Configuration
from libs.device import Device
# from libs.cprint import cprint


class AccesslistMenu:
    def __init__(
        self,
        config: Configuration,
        selected_device: Device,
    ) -> None:
        self.config = config
        self.selected_device = selected_device
        self.commands = {
            'back': ['q'],
            'help': ['h', 'help'],
            'print': ['p'],
        }

    def run(self) -> bool:
        print(f'>{self.selected_device.name}<')
        command_line = input('dev/capsman/acl: ')
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['back']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command in self.commands['print']:
            self.selected_device.get_capsman_acl()
            for item in self.selected_device.capsman.acl.items:
                print(
                    f'{item.number} |' +
                    f'{item.macaddress} |' +
                    f'{item.comment} |' +
                    f'{item.interface} |' +
                    f'{item.action}',
                )
        else:
            print('Unknown command')
            print('')
        return True


File: /libs\capsman\acl.py
from typing import List


class ACL:
    def __init__(self) -> None:
        self.items: List[ACLItem] = []

    def additem(
            self,
            number: int,
            comment: str,
            macaddress: str,
            interface: str,
            action: str,
    ):
        self.items.append(
            ACLItem(
                number,
                comment,
                macaddress,
                interface,
                action,
            ),
        )


class ACLItem:
    def __init__(
        self,
        number: int = -1,
        comment: str = '',
        macaddress: str = '',
        interface: str = '',
        action: str = '',
    ) -> None:
        self.number = number
        self.comment = comment
        self.macaddress = macaddress
        self.interface = interface
        self.action = action


File: /libs\capsman\capsman.py
from libs.capsman.acl import ACL


class Capsman:
    def __init__(self) -> None:
        self.acl = ACL()
        self.status_known: bool = False
        self.enabled: bool = False


File: /libs\capsman\capsmanmenu.py
# import getpass
# from typing import List
# from typing import Optional
from libs.capsman.accesslistmenu import AccesslistMenu
from libs.configuration import Configuration
from libs.device import Device
# from libs.cprint import cprint


class CapsmanMenu:
    def __init__(
        self,
        config: Configuration,
        selected_device: Device,
    ) -> None:
        self.config = config
        self.selected_device = selected_device
        self.commands = {
            'back': ['q'],
            'help': ['h', 'help'],
            'access list menu': ['a'],
        }

        self.accesslist_menu = AccesslistMenu(
            self.config,
            self.selected_device,
        )

    def run(self) -> bool:
        print(f'>{self.selected_device.name}<')
        if not self.selected_device.capsman.status_known:
            self.selected_device.get_capsman_manager_status()
        if self.selected_device.capsman.enabled:
            print('CAPsMAN Enabled')
        else:
            print('CAPsMAN Disabled')
        command_line = input('dev/capsman: ')
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['back']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command[0] in self.commands['access list menu']:
            while self.accesslist_menu.run():
                ...
        else:
            print('Unknown command')
            print('')
        return True


File: /libs\cls.py
from os import system
from sys import platform


def cls() -> None:
    if platform.find('linux') != -1:
        cls_command = 'clear'
    elif platform.find('win') != -1:
        cls_command = 'cls'
    elif platform.find('darwin') != -1:
        cls_command = 'clear'
    else:
        print('Unknown OS. cls will not work!')
        cls_command = False  # type: ignore
    if cls_command:
        system(cls_command)


File: /libs\configuration.py
import secrets

try:
    import yaml
except (NameError, ModuleNotFoundError):
    import sys
    print('PyYAML is needed for this program.')
    raise ImportError(
        'PyYAML is needed for this program.\n'
        f'Install it: {sys.executable} -m pip install PyYAML',
    )

from base64 import urlsafe_b64encode as b64e
from base64 import urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path
from typing import List


class Configuration:
    def __init__(self, password: str, filename: str = 'cfg.yaml') -> None:
        self.password = password
        self.filename = filename
        self.targets: List[dict] = []

    def save_cfg_to_file(self) -> None:
        data = {}
        data['targets'] = self.targets
        with open(self.filename, 'w', encoding='utf8') as outfile:
            yaml.dump(
                data,
                outfile,
                default_flow_style=False,
                allow_unicode=True,
            )

    def _derive_key(
            self,
            password: bytes,
            salt: bytes,
            iterations: int = 100_000,
    ) -> bytes:
        """Derive a secret key from a given password and salt"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend(),
        )
        return b64e(kdf.derive(password))

    def password_encrypt(
            self,
            data_to_encrypt: bytes,
            password: str,
            iterations: int = 100_000,
    ) -> str:
        salt = secrets.token_bytes(16)
        key = self._derive_key(password.encode(), salt, iterations)
        return b64e(
            b'%b%b%b' % (
                salt,
                iterations.to_bytes(4, 'big'),
                b64d(Fernet(key).encrypt(data_to_encrypt)),
            ),
        ).decode('utf-8')

    def password_decrypt(self, token: bytes) -> str:
        try:
            decoded = b64d(token)
            salt, iter, token = (
                decoded[:16],
                decoded[16:20],
                b64e(decoded[20:]),
            )
            iterations = int.from_bytes(iter, 'big')
            key = self. _derive_key(
                self.password.encode(),
                salt,
                iterations,
            )
            return Fernet(key).decrypt(token).decode('utf-8')
        except InvalidToken:
            return 'Invalid password'

    def is_password_correct(self) -> bool:
        if len(self.targets) == 0:
            return True
        for target in self.targets:
            token = target['password']
            try:
                decoded = b64d(token)
                salt, iter, token = (
                    decoded[:16],
                    decoded[16:20],
                    b64e(decoded[20:]),
                )
                iterations = int.from_bytes(iter, 'big')
                key = self._derive_key(
                    self.password.encode(),
                    salt,
                    iterations,
                )
                Fernet(key).decrypt(token).decode('utf-8')
            except InvalidToken:
                return False
        return True

    def load_config(self) -> None:
        if Path(self.filename).is_file():
            with open(self.filename) as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                else:
                    self.targets = data['targets']
        else:
            print(f"File {self.filename} doesn't exist.")
            return

    def check_or_create_config_file(self) -> None:
        if Path(self.filename).is_file():
            file_has_data = False
            with open(self.filename) as stream:
                try:
                    data = yaml.safe_load(stream)
                    file_has_data = True
                except yaml.YAMLError as exc:
                    file_has_data = False
                    print(exc)
            if file_has_data:
                if isinstance(data, dict):
                    if 'targets' not in data.keys():
                        pass
                    else:
                        if isinstance(data['targets'], list):
                            all_are_dct = True
                            for target in data['targets']:
                                if not isinstance(target, dict):
                                    all_are_dct = False
                            if not all_are_dct:
                                print(
                                    'cfg file error: '
                                    'some of the targets are/is not a dict',
                                )
                                return
                        else:
                            print((
                                'cfg file error: '
                                'targets are not a list',
                            ))
                            return
                    # more keys will follow here
                    # more ifs'
                else:
                    print(
                        f'Wrong format of {self.filename}. '
                        'Expected dict as the main object.',
                    )
                    raise
            else:
                ...
                # create structure
        else:
            ...
            # create file and basic structure


File: /libs\cprint.py
from typing import Any
from typing import Dict
from typing import List


def cprint(rows) -> None:  # type: ignore
    column_widths: Dict[int, Any] = {}
    for row in rows:
        for number, column in enumerate(row):
            current_column_width = len(str(column))
            if number not in column_widths.keys():
                column_widths[number] = current_column_width
            else:
                if column_widths[number] <= current_column_width:
                    column_widths[number] = current_column_width

    output: List[str] = []
    for row in rows:
        new_row = ''
        for number, column in enumerate(row):
            new_row += f'{column:<{column_widths[number]}}'
        output.append(new_row)

    for item in output:
        print(item)


File: /libs\device.py
import subprocess
from typing import Optional

import paramiko

from libs.capsman.capsman import Capsman
from libs.configuration import Configuration
from libs.cprint import cprint
from libs.group import Group
from libs.interface import Interface

# paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)


class Device:
    def __init__(
            self,
            name: str,
            address: str,
            port: int,
            user: str,
            encrypted_password: str,
            group: Group,
            config: Configuration,
    ) -> None:
        self.name = name
        self.address = address
        self.port = port
        self.user = user
        self.encrypted_password = encrypted_password
        self.group = group
        self.config = config

        self.interfaces: list[Interface] = []
        self.os_version: str = ''
        self.time_of_last_update: Optional[int] = None

        self.capsman = Capsman()

    def test_connection(self) -> list[bool]:
        result = [False, False]
        if self._ping_test():
            result[0] = True
            if self._ssh_test():
                result[1] = True
        return result

    def _ssh_test(self) -> bool:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(
                hostname=self.address,
                port=self.port,
                username=self.user,
                password=self.config.password_decrypt(
                    bytes(self.encrypted_password, 'utf-8'),
                ),
                look_for_keys=False,
            )
        except (
            paramiko.AuthenticationException,
            paramiko.SSHException,
        ) as err:
            print(f'ssh err on {self.name}: {err}')
            return False
        else:
            # remote_cmd = 'interface print terse'
            # stdin, stdout, stderr = ssh.exec_command(remote_cmd)
            # for line in stdout.readlines():
            #     print(line.strip('\n'))
            # print((
            #   "Options available to deal with the "
            #   f"connectios are many like\n{dir(ssh)}"
            # ))
            ssh.close()
            return True

    def _ping_test(self) -> bool:
        result = subprocess.run(
            [
                'ping',
                '-c1',
                self.address,
            ],
            shell=False,
            stdin=None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode != 0:
            print('-'*20)
            print(f'Error when pinging {self.name}')
            print('stdout:')
            print(f"{result.stdout.decode('utf-8')}")
            print('stderr:')
            print(f"{result.stderr.decode('utf-8')}")
            print('-'*20)
            return False
        return True

    def _ssh_call(self, remote_cmd: str) -> list:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(
                hostname=self.address,
                port=self.port,
                username=self.user,
                password=self.config.password_decrypt(
                    bytes(self.encrypted_password, 'utf-8'),
                ),
                look_for_keys=False,
            )
        except paramiko.AuthenticationException as err:
            print(f'ssh err on {self.name}: {err}')
            return []
        else:
            stdin, stdout, stderr = ssh.exec_command(remote_cmd)
            output = []
            for line in stdout.readlines():
                output.append(line.strip('\n'))
            ssh.close()
            return output

    def get_interfaces_from_device(self) -> None:
        print(f'Updating interfaces from {self.name}...')
        output = self._ssh_call('interface print terse')
        self.interfaces = []
        for line in output:
            if 'name' not in line:
                break
            number = int(line.split()[0])
            name = line.split('name=')[1].split()[0]
            comment = ''
            if 'comment=' in line:
                raw_comment = line.split('comment=')[1].split()[:-1]
                output = []
                for item in raw_comment:
                    if '=' in item:
                        break
                    output.append(item)
                comment = ' '.join(output)
            status = line.split()[1]
            if 'X' in status:
                disabled = True
            else:
                disabled = False
            if 'R' in status:
                running = True
            else:
                running = False
            if 'S' in status:
                slave = True
            else:
                slave = False
            if 'D' in status:
                dynamic = True
            else:
                dynamic = False
            interface = Interface(
                    number,
                    name,
                    disabled,
                    running,
                    slave,
                    dynamic,
                    comment,
            )
            interface._set_time_since_last_update_now()
            self.interfaces.append(interface)

    def get_os_version(self) -> None:
        output = self._ssh_call('system package print')
        for line in output:
            if 'routeros' in line:
                self.os_version = line.split()[2]
                print(f'{self.name} os version refreshed')

    def get_name(self) -> str:
        output = self._ssh_call('system identity print')
        return output[0].split()[1]

    def get_capsman_manager_status(self) -> None:
        # print(f'Updating capsman status from {self.name}...')
        output = self._ssh_call('caps-man manager print')
        for line in output:
            if 'enabled:' in line:
                if 'yes' in line:
                    self.capsman.enabled = True
                else:
                    self.capsman.enabled = False
                self.capsman.status_known = True
                return

    def get_capsman_acl(self) -> None:
        output = self._ssh_call('caps-man access-list print terse')
        self.capsman.acl.items = []
        for line in output:
            if len(line.split()) > 1:
                number = line.split()[0]
                if 'comment=' in line:
                    comment = line.split(
                        'mac-address',
                    )[0].split('comment=')[1].strip()
                else:
                    comment = ''
                if 'mac-address' in line:
                    macaddress = line.split('mac-address=')[-1].split()[0]
                else:
                    macaddress = ''
                if 'interface' in line:
                    interface = line.split('interface=')[-1].split()[0]
                else:
                    interface = ''
                if 'action' in line:
                    action = line.split('action=')[-1].split()[0]
                else:
                    action = ''
                self.capsman.acl.additem(
                    number,
                    comment,
                    macaddress,
                    interface,
                    action,
                )

    def print_cached_interfaces(self) -> None:
        if len(self.interfaces) == 0:
            self.get_interfaces_from_device()
        if self.interfaces[0].enought_time_passed():
            self.get_interfaces_from_device()
        if len(self.interfaces) == 0:
            print('No interfaces found')
            return
        rows = []
        for interface in self.interfaces:
            status = ''
            if interface.dynamic:
                status += 'D'
            if interface.running:
                status += 'R'
            if interface.slave:
                status += 'S'
            if interface.disabled:
                status += 'X'
            row = [
                f'{interface.number}',
                f':{interface.name}',
                f':{status}',
                f':{interface.comment}',
            ]
            rows.append(row)
        cprint(rows)


File: /libs\devicecreatedialog.py
import getpass
from typing import List

from libs.cls import cls
from libs.configuration import Configuration
from libs.device import Device
from libs.group import Group


class DeviceCreateDialog:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
    ) -> None:
        self.config = config
        self.devices = devices
        self.groups = groups

    def _pick_group_dialog(self) -> Group:
        while True:
            group_chosen = False
            if len(self.groups) == 0:
                print('There are no existing groups.')
            else:
                print('Existing groups:')
                for group in self.groups:
                    print(f'{group.name}')
                print('-' * 15)
            print('Enter group')
            new_group_name = input('> ')
            found = False
            for group in self.groups:
                if new_group_name == group.name:
                    print(f'Using existing group {group.name}')
                    found = True
                    group_chosen = True
                    chosen_group = group
                    break
            if group_chosen:
                break
            if not found:
                print(f"Group {new_group_name} doesn't exist yet")
                print('Create a new group? (yY/nN/q)')
                while True:
                    answer = input('>')
                    if answer.lower() == 'y':
                        self.groups.append(
                            Group(
                                new_group_name,
                                self.config,
                            ),
                        )
                        chosen_group = self.groups[-1]
                        print(f'New group {new_group_name} created.')
                        group_chosen = True
                        break
                    elif answer.lower() == 'n':
                        break
                    elif answer.lower() == 'q':
                        exit(0)
                    else:
                        pass
                if group_chosen:
                    break
        return chosen_group

    def run(self):
        if len(self.config.targets) > 0:
            if not self.config.is_password_correct():
                print(
                    "Wrong password. Can't decrypt passwords for the devices.",
                )
                return
        cls()
        if len(self.devices) > 0:
            print('Already existing defices:')
            for device in self.devices:
                print(f'{device.name}')
            print('-' * 15)
        print('Ener IP address')
        print('Leave blank to go back.')
        address = input('> ')
        if len(address) == 0:
            return
        while True:
            print('Ener port (default: 22)')
            prt = input('> ')
            if prt == '':
                port = 22
                break
            try:
                port = int(prt)
            except ValueError:
                print('Port must be an integer!')
            else:
                if port > 65_535:
                    print('Port must have a value lower than 65,535!')
                else:
                    break
        print('Ener user (default: control)')
        user = input('>')
        if len(user) == 0:
            user = 'control'
        print('Ener password')
        device_password = getpass.getpass('> ')
        encrypted_password = self.config.password_encrypt(
            bytes(device_password, 'utf-8'),
            self.config.password,
        )

        _device = Device(
            '_dummy_',
            address,
            port,
            user,
            encrypted_password,
            '__dummy__',
            self.config,
        )
        print('getting name from the device...')
        name = _device.get_name()
        print(f'device name: {name}')
        print('enter device name or leave blank to keep the above.')
        answer = input('>')
        if len(answer) != 0:
            name = answer

        chosen_group = self._pick_group_dialog()

        record = {
            'name': name,
            'address': address,
            'port': port,
            'user': user,
            'password': encrypted_password,
            'group': chosen_group.name,
        }
        self.devices.append(
            Device(
                name,
                address,
                port,
                user,
                encrypted_password,
                chosen_group,
                self.config,
            ),
        )
        self.config.targets.append(record)
        self.config.save_cfg_to_file()
        print(f'New device {name} created and saved.')


File: /libs\devicehandler.py
from typing import List

from libs.configuration import Configuration
from libs.device import Device


class DeviceHandler:
    def __init__(
        self,
        config: Configuration,
    ) -> None:
        self.config = config
        self.devices: List[Device] = []

    def instantiate_devices(self):
        if len(self.config.targets) == 0:
            return
        for target in self.config.targets:
            self.devices.append(
                Device(
                    target['name'],
                    target['address'],
                    target['port'],
                    target['user'],
                    target['password'],
                    target['group'],
                    self.config,
                ),
            )


File: /libs\devicemenu.py
import getpass
from typing import List
from typing import Optional

from libs.capsman.capsmanmenu import CapsmanMenu
from libs.configuration import Configuration
from libs.cprint import cprint
from libs.device import Device
from libs.devicecreatedialog import DeviceCreateDialog
from libs.group import Group
from libs.script import Script


class DeviceMenu:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
        scripts: List[Script],
    ) -> None:
        self.config = config
        self.devices = devices
        self.groups = groups
        self.scripts = scripts
        self.selected_device: Optional[Device] = None
        self.commands = {
            'back': ['q'],
            'help': ['h', 'help'],
            'list all devices': ['l'],
            'testall devices': ['ta'],
            'create device': ['c'],
            'edit device': ['e'],
            'select device': ['s'],
            'list interfaces': ['li'],
            'capsman menu': ['cm'],
        }

    def run(self) -> bool:
        if not self.selected_device:
            if len(self.devices) == 0:
                return False
            print('Select a device to manage:')
            print('Leave empty to go back to main menu.')
            devices_with_idx = []
            indexes = []
            for idx, device in enumerate(self.devices):
                devices_with_idx.append((idx, f': {device.name}'))
                indexes.append(idx)
            cprint(devices_with_idx)
            while True:
                answer = input('> ')
                if len(answer) == 0:
                    return False
                try:
                    intanswer = int(answer)
                except ValueError:
                    print('Pick a number.')
                else:
                    if intanswer in indexes:
                        self.selected_device = self.devices[intanswer]
                        break
                    else:
                        print('Pick a number from the list of devices.')

        self.capsman_menu = CapsmanMenu(
            self.config,
            self.selected_device,
        )

        print(f'>{self.selected_device.name}<')
        command_line = input('dev: ')
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['back']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command in self.commands['list all devices']:
            if len(self.config.targets) > 0:
                for device in self.devices:
                    print(f'nme: {device.name}')
                    print(f'IPa: {device.address}')
                    print(f'prt: {device.port}')
                    print(f'usr: {device.user}')
                    print(f'grp: {device.group}')
                    print('-'*20)
        elif command in self.commands['list interfaces']:
            self.selected_device.print_cached_interfaces()
        elif command in self.commands['create device']:
            device_create_dialog = DeviceCreateDialog(
                self.config,
                self.devices,
                self.groups,
            )
            device_create_dialog.run()
        elif command in self.commands['edit device']:
            self.edit_dialog(self.selected_device)
        elif command in self.commands['select device']:
            self.selected_device = None
        elif command in self.commands['testall devices']:
            print('Testing...')
            output = []
            for device in self.devices:
                if device.test_connection():
                    output.append((device.name, ': ok'))
                else:
                    output.append((device.name, ': KO!'))
            print('result:')
            print('-'*15)
            cprint(output)
        elif command in self.commands['capsman menu']:
            while self.capsman_menu.run():
                ...
        else:
            print('Unknown command')
            print('')
        return True

    def edit_dialog(self, device: Device) -> None:
        print(f'Name: {device.name}')
        print('Leave blank to keep')
        new_name = input('> ')
        if new_name != '':
            device.name = new_name

        print(f'IP: {device.address}')
        print('Leave blank to keep')
        new_address = input('> ')
        if new_address != '':
            device.address = new_address

        while True:
            print(f'Port: {device.port}')
            print('Leave blank to keep')
            new_port = input('> ')
            if new_port != '':
                try:
                    device.port = int(new_port)
                except ValueError:
                    print('Port must be an int number')
                else:
                    break
            else:
                break

        print(f'User: {device.user}')
        print('Leave blank to keep')
        new_user = input('> ')
        if new_user != '':
            device.user = new_user

        print('Password:')
        print('Leave blank to keep')
        new_password = getpass.getpass('> ')
        if new_password != '':
            device.encrypted_password = self.config.password_encrypt(
                bytes(new_password, 'utf-8'),
                self.config.password,
            )
        self.generate_targets_from_devices()
        self.config.save_cfg_to_file()

    def generate_targets_from_devices(self) -> None:
        self.config.targets = []
        for device in self.devices:
            record = {
                'name': device.name,
                'address': device.address,
                'port': device.port,
                'user': device.user,
                'password': device.encrypted_password,
                'group': device.group,
            }
            self.config.targets.append(record)


File: /libs\devicesmenu.py
import getpass
from typing import List
from typing import Optional

from libs.configuration import Configuration
from libs.cprint import cprint
from libs.device import Device
from libs.devicecreatedialog import DeviceCreateDialog
from libs.group import Group
from libs.script import Script


class DevicesMenu:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
        scripts: List[Script],
    ) -> None:
        self.config = config
        self.devices = devices
        self.groups = groups
        self.scripts = scripts
        self.command_history: list[str] = []
        self.selected_device: Optional[Device] = None
        self.commands = {
            'back': ['q'],
            'help': ['h', 'help'],
            'list details of all devices': ['l'],
            'test connection to all devices': ['tc'],
            'create device': ['c'],
            'refresh devices': ['r'],
            'sort devices': ['s'],
        }

    def run(self) -> bool:
        if len(self.devices) == 0:
            print('There are no devices defined.')
            print('Add a new device?')
            #  TODO: add new device dialog
            return False

        devices_with_idx = []
        indexes = []
        for idx, device in enumerate(self.devices):
            devices_with_idx.append((
                idx,
                f': {device.group}',
                f': {device.name}',
                f': {device.os_version}',
            ))
            indexes.append(idx)

        if len(self.command_history) == 0:
            cprint(devices_with_idx)

        command_line = input('devices > ')
        self.command_history.append(command_line)

        if len(command_line) == 0:
            cprint(devices_with_idx)
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True

        if command.isnumeric():
            intcommand = int(command)
            if intcommand in indexes:
                #  TODO: run device menu here
                print('run device menu here')
            else:
                print(
                    'Pick a number from the list of devices or use a command.',
                )
        if command in self.commands['back']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command in self.commands['list details of all devices']:
            if len(self.config.targets) > 0:
                for device in self.devices:
                    print(f'nme: {device.name}')
                    print(f'IPa: {device.address}')
                    print(f'prt: {device.port}')
                    print(f'usr: {device.user}')
                    print(f'grp: {device.group}')
                    print('-'*20)
        elif command in self.commands['create device']:
            device_create_dialog = DeviceCreateDialog(
                self.config,
                self.devices,
                self.groups,
            )
            device_create_dialog.run()
        elif command in self.commands['refresh devices']:
            for device in self.devices:
                device.get_os_version()
        elif command in self.commands['sort devices']:
            self.devices = sorted(
                self.devices,
                key=lambda x: x.name, reverse=True,
            )
            self.generate_targets_from_devices()
            self.config.save_cfg_to_file()
        elif command in self.commands['test connection to all devices']:
            print('Testing...')
            output = []
            for device in self.devices:
                ping_result, ssh_result = device.test_connection()
                if ping_result:
                    if ssh_result:
                        output.append((
                            device.name,
                            ': ping ok',
                            ': ssh ok',
                        ))
                    else:
                        output.append((
                            device.name,
                            ': ping ok',
                            ': ssh KO!',
                        ))
                else:
                    if ssh_result:
                        output.append((
                            device.name,
                            ': ping KO!',
                            ': ssh: ok',
                        ))
                    else:
                        output.append((
                            device.name,
                            ': ping KO!',
                            ': ssh: KO!',
                        ))
            print('result:')
            print('-'*15)
            cprint(output)
        else:
            print('Unknown command')
            print('')
        return True

    def edit_dialog(self, device: Device) -> None:
        print(f'Name: {device.name}')
        print('Leave blank to keep')
        new_name = input('> ')
        if new_name != '':
            device.name = new_name

        print(f'IP: {device.address}')
        print('Leave blank to keep')
        new_address = input('> ')
        if new_address != '':
            device.address = new_address

        while True:
            print(f'Port: {device.port}')
            print('Leave blank to keep')
            new_port = input('> ')
            if new_port != '':
                try:
                    device.port = int(new_port)
                except ValueError:
                    print('Port must be an int number')
                else:
                    break
            else:
                break

        print(f'User: {device.user}')
        print('Leave blank to keep')
        new_user = input('> ')
        if new_user != '':
            device.user = new_user

        print('Password:')
        print('Leave blank to keep')
        new_password = getpass.getpass('> ')
        if new_password != '':
            device.encrypted_password = self.config.password_encrypt(
                bytes(new_password, 'utf-8'),
                self.config.password,
            )
        self.generate_targets_from_devices()
        self.config.save_cfg_to_file()

    def generate_targets_from_devices(self) -> None:
        self.config.targets = []
        for device in self.devices:
            record = {
                'name': device.name,
                'address': device.address,
                'port': device.port,
                'user': device.user,
                'password': device.encrypted_password,
                'group': device.group,
            }
            self.config.targets.append(record)


File: /libs\group.py
from libs.configuration import Configuration


class Group:
    def __init__(self, name: str, config: Configuration) -> None:
        self.name = name
        self.config = config


File: /libs\grouphandler.py
from typing import List
from typing import Optional

from libs.configuration import Configuration
from libs.group import Group


class GroupHandler:
    def __init__(
        self,
        config: Configuration,
    ) -> None:
        self.config = config
        self.groups: List[Group] = []

    def instantiate_groups(self):
        if len(self.config.targets) == 0:
            return
        for target in self.config.targets:
            if not self.group_by_name_exists(
                target['group'],
            ):
                self.groups.append(
                    Group(
                        target['group'],
                        self.config,
                    ),
                )

    def get_group_by_name(self, lookup_name: str) -> Optional[Group]:
        assert self.group_by_name_exists(lookup_name)
        for group in self.groups:
            if group.name == lookup_name:
                return group
        return None

    def group_by_name_exists(self, lookup_name: str) -> bool:
        for group in self.groups:
            if group.name == lookup_name:
                return True
        return False


File: /libs\interface.py
from time import monotonic


class Interface:
    def __init__(
        self,
        number: int,
        name: str,
        disabled: bool,
        running: bool,
        slave: bool,
        dynamic: bool,
        comment: str,
    ) -> None:
        self.number = number
        self.name = name
        self.disabled = disabled
        self.running = running
        self.slave = slave
        self.dynamic = dynamic
        self.comment = comment
        self.time_since_last_update: int | None = None

    def _set_time_since_last_update_now(self):
        current_time = int(monotonic())
        self.time_of_last_update = current_time

    def enought_time_passed(self, timeout: int = 20) -> bool:
        current_time = int(monotonic())
        if not self.time_of_last_update:
            self.time_of_last_update = current_time
            return True
        if current_time - self.time_of_last_update > timeout:
            self._set_time_since_last_update_now()
            return True
        return False


File: /libs\ip\dhcp-server.py
from typing import List

from lib.interface import Interface


class DHCPServer:
    def __init__(self) -> None:
        self.items = List[DHCPServerItem]
        self.leases = Leases()


class DHCPServerItem:
    def __init__(
        self,
        number: int,
        name: str,
        interface: Interface,
        address_pool: str,  # implement class later
        lease_time: str,  # implement class later
    ) -> None:
        self.number = number
        self.name = name
        self.interface = interface
        self.address_pool = address_pool
        self.lease_time = lease_time


class Leases:
    def __init__(self) -> None:
        self.items = List[LeasesItem]


class LeasesItem:
    def __init__(self):
        pass


File: /libs\mainmenu.py
from typing import List

from libs.configuration import Configuration
from libs.device import Device
from libs.devicesmenu import DevicesMenu
from libs.group import Group
from libs.script import Script
from libs.scriptsmenu import ScriptsMenu


class MainMenu:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
        scripts: List[Script],
    ) -> None:

        self.config = config
        self.devices = devices
        self.groups = groups
        self.scripts = scripts
        self.password_verified = False
        self.command_history: list[str] = []

        self.devices_menu = DevicesMenu(
            self.config,
            self.devices,
            self.groups,
            self.scripts,
        )

        self.scripts_menu = ScriptsMenu(
            self.config,
            self.devices,
            self.groups,
            self.scripts,
        )

        self.commands = {
            'quit': ['q', 'quit', 'exit'],
            'help': ['h', 'help'],
            'devices menu': ['d'],
            'scripts menu': ['s'],
        }

    def _print_help(self) -> None:
        for c in self.commands:
            print(f'{c}: {self.commands[c]}')

    def run(self) -> bool:
        if not self.password_verified:
            if not self.config.is_password_correct():
                print(
                    'Wrong password. '
                    "Can't decrypt passwords for the devices.\n"
                    "If you've lost your password, "
                    'create a new configuration file '
                    'and start over.',
                )
                return False
            else:
                self.password_verified = True

        if len(self.command_history) == 0:
            self._print_help()
        command_line = input(': ')
        self.command_history.append(command_line)
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['quit']:
            return False
        elif command in self.commands['help']:
            self._print_help()
        elif command[0] in self.commands['devices menu']:
            while self.devices_menu.run():
                ...
        elif command[0] in self.commands['scripts menu']:
            while self.scripts_menu.run():
                ...
        else:
            print('Unknown command')
            print('')
        return True


File: /libs\program.py
import getpass
from typing import List

from libs.cls import cls
from libs.configuration import Configuration
from libs.device import Device
from libs.devicehandler import DeviceHandler
from libs.group import Group
from libs.grouphandler import GroupHandler
from libs.mainmenu import MainMenu
from libs.script import Script
from libs.scripthandler import ScriptHandler


class Program:
    def __init__(self) -> None:
        self.config = Configuration(getpass.getpass())
        self.config.check_or_create_config_file()
        self.config.load_config()

        self.device_handler = DeviceHandler(self.config)
        self.device_handler.instantiate_devices()

        self.group_handler = GroupHandler(self.config)
        self.group_handler.instantiate_groups()

        self.script_handler = ScriptHandler()
        self.script_handler.load_scripts()
        self.script_handler.instantiate_scripts()

        self.devices: List[Device] = self.device_handler.devices
        self.groups: List[Group] = self.group_handler.groups
        self.scripts: List[Script] = self.script_handler.scripts

    def run(self) -> int:
        main_menu = MainMenu(
            self.config,
            self.devices,
            self.groups,
            self.scripts,
        )

        cls()
        while main_menu.run():
            ...
        return 0


File: /libs\script.py
from typing import List
from typing import Optional

from libs.device import Device
from libs.group import Group


class Script:
    def __init__(
        self,
        name: str,
        devices: Optional[List[Device]],
        groups: Optional[List[Group]],
        scripts: Optional[List],
        actions: List[str],
    ) -> None:
        self.name = name
        self.devices = devices
        self.groups = groups
        self.scripts = scripts
        self.actions = actions


File: /libs\scripthandler.py
# import io
from pathlib import Path
from typing import List

from libs.script import Script

try:
    import yaml
except (NameError, ModuleNotFoundError):
    import sys
    print('PyYAML is needed for this program.')
    raise ImportError((
        'PyYAML is needed for this program.\n'
        f'Install it: {sys.executable} -m pip install PyYAML',
    ))


class ScriptHandler:
    def __init__(self, filename: str = 'scripts.yaml') -> None:
        self.filename = filename
        self.scripts_from_file: list = []
        self.scripts: List[Script] = []

    def load_scripts(self) -> None:
        if Path(self.filename).is_file():
            with open(self.filename) as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            print(f"File {self.filename} doesn't exist.")
            raise
        self.scripts_from_file = data['scripts']

    def instantiate_scripts(self) -> None:
        for entry in self.scripts_from_file:
            self.scripts.append(
                Script(
                    entry['name'],
                    entry['devices'],
                    entry['groups'],
                    entry['scripts'],
                    entry['actions'],
                ),
            )


File: /libs\scriptmenu.py
from typing import List

from libs.configuration import Configuration
from libs.device import Device
from libs.group import Group
from libs.script import Script


class ScriptMenu:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
        scripts: List[Script],
    ) -> None:
        self.config = config
        self.devices = devices
        self.groups = groups
        self.scripts = scripts

        self.commands = {
            'quit': ['q', 'quit', 'exit'],
            'help': ['h', 'help'],
            'list scripts': ['l'],
            'create script': ['c'],
            'run script': ['r'],
            'edit script': ['e'],
        }

    def run(self) -> bool:
        command_line = input('scr: ')
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['quit']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command in self.commands['list scripts']:
            if len(self.scripts) > 0:
                for script in self.scripts:
                    print(f'name   : {script.name}')
                    print(f'devices: {script.devices}')
                    print(f'groups : {script.groups}')
                    print(f'scripts: {script.scripts}')
                    print(f'actions: {script.actions}')
                    print('-'*20)
            else:
                print('No scripts defined.')
        elif command in self.commands['create script']:
            ...
        elif command in self.commands['run script']:
            ...
        elif command in self.commands['edit script']:
            ...
        else:
            print('Unknown command')
            print('')
        return True


File: /libs\scriptsmenu.py
from typing import List

from libs.configuration import Configuration
from libs.device import Device
from libs.group import Group
from libs.script import Script


class ScriptsMenu:
    def __init__(
        self,
        config: Configuration,
        devices: List[Device],
        groups: List[Group],
        scripts: List[Script],
    ) -> None:
        self.config = config
        self.devices = devices
        self.groups = groups
        self.scripts = scripts

        self.commands = {
            'quit': ['q', 'quit', 'exit'],
            'help': ['h', 'help'],
            'list scripts': ['l'],
            'create script': ['c'],
            'run script': ['r'],
            'edit script': ['e'],
        }

    def run(self) -> bool:
        command_line = input('scr: ')
        if len(command_line) == 0:
            return True
        try:
            command = command_line.lower().split()[0]
        except IndexError:
            return True
        if command in self.commands['quit']:
            return False
        elif command in self.commands['help']:
            for c in self.commands:
                print(f'{c}: {self.commands[c]}')
        elif command in self.commands['list scripts']:
            if len(self.scripts) > 0:
                for script in self.scripts:
                    print(f'name   : {script.name}')
                    print(f'devices: {script.devices}')
                    print(f'groups : {script.groups}')
                    print(f'scripts: {script.scripts}')
                    print(f'actions: {script.actions}')
                    print('-'*20)
            else:
                print('No scripts defined.')
        elif command in self.commands['create script']:
            ...
        elif command in self.commands['run script']:
            ...
        elif command in self.commands['edit script']:
            ...
        else:
            print('Unknown command')
            print('')
        return True


File: /LICENSE
MIT License

Copyright (c) 2021 spidermila

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


File: /README.md
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/spidermila/mikrotik_control/main.svg)](https://results.pre-commit.ci/latest/github/spidermila/mikrotik_control/main)

# mikrotik_control
use Python to control my Mikrotik devices using an interactive console


