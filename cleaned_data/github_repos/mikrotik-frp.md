# Repository Information
Name: mikrotik-frp

# Directory Structure
Directory structure:
└── github_repos/mikrotik-frp/
    ├── .editorconfig
    ├── .eslintrc.json
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
    │   │       ├── pack-bf85816240cc00f9443b95c887217ee006a7a0a9.idx
    │   │       └── pack-bf85816240cc00f9443b95c887217ee006a7a0a9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .nycrc.json
    ├── .prettierrc.js
    ├── index.js
    ├── package-lock.json
    ├── package.json
    ├── src/
    │   └── protocol/
    │       ├── mappers.js
    │       └── parsers.js
    ├── test/
    │   └── protocol/
    │       ├── index.spec.js
    │       ├── mappers.spec.js
    │       └── parsers.spec.js
    └── wip/
        ├── api/
        │   ├── index.js
        │   └── query.js
        ├── client/
        │   └── index.js
        └── connection/
            └── index.js


# Content
File: /.editorconfig

# EditorConfig is awesome: http://EditorConfig.org

# .editorconfig for Elixir projects
# https://git.io/elixir-editorconfig

# top-most EditorConfig file
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.{md, markdown, eex}]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab

#[*.bat]
#end_of_line = crlf

File: /.eslintrc.json
{
  "env": {
    "commonjs": true,
    "es2021": true,
    "node": true,
    "mocha": true
  },
  "extends": [
    "airbnb-base",
    "prettier"
  ],
  "plugins": [
    "prettier"
  ],
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly"
  },
  "parserOptions": {
    "ecmaVersion": 2018
  },
  "rules": {
    "prettier/prettier": "error",
    "no-bitwise": 0,
    "indent": 0
  }
}


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/michaelkuk/mikrotik-frp.git
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
0000000000000000000000000000000000000000 e77deb0c90e6886fb07ded081f464addb5e4519e vivek-dodia <vivek.dodia@icloud.com> 1738606413 -0500	clone: from https://github.com/michaelkuk/mikrotik-frp.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 e77deb0c90e6886fb07ded081f464addb5e4519e vivek-dodia <vivek.dodia@icloud.com> 1738606413 -0500	clone: from https://github.com/michaelkuk/mikrotik-frp.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e77deb0c90e6886fb07ded081f464addb5e4519e vivek-dodia <vivek.dodia@icloud.com> 1738606413 -0500	clone: from https://github.com/michaelkuk/mikrotik-frp.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e77deb0c90e6886fb07ded081f464addb5e4519e refs/remotes/origin/master


File: /.git\refs\heads\master
e77deb0c90e6886fb07ded081f464addb5e4519e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
File: /.nycrc.json
{
  "all": true,
  "reporter": [
    "lcov",
    "text"
  ],
  "include": ["src/**/*.js"]
}


File: /.prettierrc.js
module.exports = {
  tabWidth: 2,
  semi: true,
  singleQuote: true,
  trailingComma: 'es5',
};


File: /index.js
const { createConnection } = require('net');
const split = require('binary-split');

const { commandToDeviceSentence } = require('./api/command/mappers');
const { toDeviceWord } = require('./api/command/mappers');

const command = {
  endpoint: '/login',
  attributes: {
    name: 'admin',
    password: 'M15lopm825lop!',
  },
  tag: 'login',
};

// const c1 = Buffer.concat([
//   toDeviceWord('/interface/lte/info'),
//   toDeviceWord('.tag=12'),
//   toDeviceWord('=number=0'),
//   // toDeviceWord('=once'),
//   toDeviceWord('=interval=1'),
//   toDeviceWord('=.proplist=rssi,rsrp,rsrq,sinr,session-uptime,registration-status'),
//   // toDeviceWord('=interval=2'),
//   Buffer.of(0),
// ]);

const c1 = Buffer.concat([
  // toDeviceWord('/tool/torch'),
  toDeviceWord('/interface/monitor-traffic'),
  toDeviceWord('.tag=22'),
  // toDeviceWord('=interfaces=lte1'),
  // toDeviceWord('=once'),
  toDeviceWord('=interval=5'),
  // toDeviceWord('=.proplist=rssi,rsrp,rsrq,sinr,session-uptime,registration-status'),
  // toDeviceWord('=interval=2'),
  Buffer.of(0),
]);

const b = commandToDeviceSentence(command);
let sent = false;

const conn = createConnection(
  {
    host: '192.168.42.10',
    port: 8728,
  },
  () => {
    conn.write(b);
  }
);

conn.pipe(split('\0')).on('data', (d) => {
  if (!sent) {
    sent = true;
    conn.write(c1);
  }
  if (sent) {
    console.log(JSON.stringify(d));
    console.log(d.toString());
  }
});
conn.on('error', (e) => console.error(e));

// console.log(b.toString());


File: /package-lock.json
{
  "name": "controller",
  "version": "1.0.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "binary-split": "^1.0.5",
        "core-decorators": "^0.20.0",
        "mikronode": "^2.3.11",
        "mikronode-ng": "^1.0.11",
        "mikrotik-node": "^1.0.0",
        "monet": "^0.9.2",
        "ramda": "^0.27.1",
        "ramda-adjunct": "^2.32.0",
        "rxjs": "^7.0.1",
        "short-uuid": "^4.2.0"
      },
      "devDependencies": {
        "chai": "^4.3.4",
        "chance": "^1.1.7",
        "codecov": "^3.8.2",
        "eslint": "^7.27.0",
        "eslint-config-airbnb-base": "^14.2.1",
        "eslint-config-prettier": "^8.3.0",
        "eslint-plugin-import": "^2.23.3",
        "eslint-plugin-prettier": "^3.4.0",
        "mocha": "^8.4.0",
        "mocha-lcov-reporter": "^1.3.0",
        "nyc": "^15.1.0",
        "prettier": "^2.3.0"
      }
    },
File: /package.json
{
  "name": "controller",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "mocha ./test/**/*.spec.js",
    "test:cover": "nyc mocha ./test/**/*.spec.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "binary-split": "^1.0.5",
    "core-decorators": "^0.20.0",
    "mikronode": "^2.3.11",
    "mikronode-ng": "^1.0.11",
    "mikrotik-node": "^1.0.0",
    "monet": "^0.9.2",
    "ramda": "^0.27.1",
    "ramda-adjunct": "^2.32.0",
    "rxjs": "^7.0.1",
    "short-uuid": "^4.2.0"
  },
  "devDependencies": {
    "chai": "^4.3.4",
    "chance": "^1.1.7",
    "codecov": "^3.8.2",
    "eslint": "^7.27.0",
    "eslint-config-airbnb-base": "^14.2.1",
    "eslint-config-prettier": "^8.3.0",
    "eslint-plugin-import": "^2.23.3",
    "eslint-plugin-prettier": "^3.4.0",
    "mocha": "^8.4.0",
    "mocha-lcov-reporter": "^1.3.0",
    "nyc": "^15.1.0",
    "prettier": "^2.3.0"
  }
}


File: /src\protocol\mappers.js
/* eslint-disable no-underscore-dangle */
const {
  cond,
  pipe,
  length,
  gt,
  T,
  converge,
  unapply,
  propOr,
  toPairs,
  prop,
  map,
  unary,
  when,
  ifElse,
} = require('ramda');
const { isNotEmpty } = require('ramda-adjunct');

const __encodeSingleByteLen = (len) => Buffer.of(len);

const __encodeTwoByteLen = (len) =>
  Buffer.concat([
    Buffer.of(((len | 0x8000) >> 8) & 0xff),
    Buffer.of((len | 0x8000) & 0xff),
  ]);

const __encodeThreeByteLen = (len) =>
  Buffer.concat([
    Buffer.of(((len | 0xc00000) >> 16) & 0xff),
    Buffer.of(((len | 0xc00000) >> 8) & 0xff),
    Buffer.of((len | 0xc00000) & 0xff),
  ]);

const __encodeFourByteLen = (len) =>
  Buffer.concat([
    Buffer.of(((len | 0xe0000000) >> 24) & 0xff),
    Buffer.of(((len | 0xe0000000) >> 16) & 0xff),
    Buffer.of(((len | 0xe0000000) >> 8) & 0xff),
    Buffer.of((len | 0xe0000000) & 0xff),
  ]);

const __encodeFiveByteLen = (len) =>
  Buffer.concat([
    Buffer.of(0xf0),
    Buffer.of((len >> 24) & 0xff),
    Buffer.of((len >> 16) & 0xff),
    Buffer.of((len >> 8) & 0xff),
    Buffer.of(len & 0xff),
  ]);

// const __encodeLengthImp = (len) => {
//   if (len < 0x80) {
//     return __encodeSingleByteLen(len);
//   }

//   if (len < 0x4000) {
//     return __encodeTwoByteLen(len);
//   }

//   if (len < 0x200000) {
//     return __encodeThreeByteLen(len);
//   }

//   if (len < 0x10000000) {
//     return __encodeFourByteLen(len);
//   }

//   return __encodeFiveByteLen(len);
// };

const __encodeLength = cond([
  [gt(0x80), __encodeSingleByteLen],
  [gt(0x4000), __encodeTwoByteLen],
  [gt(0x200000), __encodeThreeByteLen],
  [gt(0x10000000), __encodeFourByteLen],
  [T, __encodeFiveByteLen],
]);

const toDeviceWord = converge(unapply(unary(Buffer.concat)), [
  pipe(length, __encodeLength),
  // pipe(length, __encodeLengthImp),
  unary(Buffer.from),
]);

const serializeAttributePair = ([key, val]) => `=${key}=${val}`;
const setTag = (value) => `.tag=${value}`;
const toBuffer = (v) => Buffer.from(v);
const stopWord = () => Buffer.of(0);

// Command -> Buffer
const commandToDeviceSentence = pipe(
  converge(unapply(unary(Buffer.concat)), [
    // Encode endpoint word
    pipe(prop('endpoint'), toDeviceWord),
    // Encode channel tag if present
    pipe(
      propOr('', 'tag'),
      when(isNotEmpty, pipe(setTag, toDeviceWord)),
      toBuffer
    ),
    // Encode attributes
    pipe(
      propOr({}, 'attributes'),
      toPairs,
      map(pipe(serializeAttributePair, toDeviceWord)),
      ifElse(isNotEmpty, unary(Buffer.concat), () => Buffer.from(''))
    ),
    // TODO: Encode query attrybutes
    stopWord,
  ])
);

module.exports = {
  toDeviceWord,
  commandToDeviceSentence,
  __encodeLength,
};


File: /src\protocol\parsers.js
/* eslint-disable no-underscore-dangle */
const {
  cond,
  always,
  T,
  curryN,
  converge,
  unapply,
  sum,
  pipe,
  view,
  lensIndex,
  map,
  slice,
  toString,
  unary,
} = require('ramda');

const shiftLeft = curryN(2, (n, num) => num << n);
const binaryAnd = curryN(2, (n1, n2) => n2 & n1);

const __getLenFromSingleByte = pipe(view(lensIndex(0)), unary(Number));

const __getLenFromTwoBytes = converge(unapply(sum), [
  pipe(view(lensIndex(0)), binaryAnd(~0xc0), shiftLeft(8)),
  view(lensIndex(1)),
]);

const __getLenFromThreeBytes = converge(unapply(sum), [
  pipe(view(lensIndex(0)), binaryAnd(~0xe0), shiftLeft(16)),
  pipe(view(lensIndex(1)), shiftLeft(8)),
  view(lensIndex(2)),
]);

const __getLenFromFourBytes = converge(unapply(sum), [
  pipe(view(lensIndex(0)), binaryAnd(~0xf0), shiftLeft(24)),
  pipe(view(lensIndex(1)), shiftLeft(16)),
  pipe(view(lensIndex(2)), shiftLeft(8)),
  view(lensIndex(3)),
]);

const __getLenFromFiveBytes = converge(unapply(sum), [
  pipe(view(lensIndex(1)), shiftLeft(24)),
  pipe(view(lensIndex(2)), shiftLeft(16)),
  pipe(view(lensIndex(3)), shiftLeft(8)),
  view(lensIndex(4)),
]);

const __calculateLenBytes = cond([
  [(byte) => (byte & 0x80) === 0x00, always(1)],
  [(byte) => (byte & 0xc0) === 0x80, always(2)],
  [(byte) => (byte & 0xe0) === 0xc0, always(3)],
  [(byte) => (byte & 0xf0) === 0xe0, always(4)],
  [T, always(5)],
]);

function __toWordRanges(data, currentOffset = 0, acc = []) {
  if (currentOffset === data.length) {
    return acc;
  }

  const byteNo = __calculateLenBytes(data[currentOffset]);
  let len;
  let lenOffset;

  switch (byteNo) {
    case 1:
      lenOffset = currentOffset + 1;
      len = __getLenFromSingleByte(
        data.slice(currentOffset, currentOffset + lenOffset)
      );
      break;
    case 2:
      lenOffset = currentOffset + 2;
      len = __getLenFromTwoBytes(
        data.slice(currentOffset, currentOffset + lenOffset)
      );
      break;
    case 3:
      lenOffset = currentOffset + 3;
      len = __getLenFromThreeBytes(
        data.slice(currentOffset, currentOffset + lenOffset)
      );
      break;
    case 4:
      lenOffset = currentOffset + 4;
      len = __getLenFromTwoBytes(
        data.slice(currentOffset, currentOffset + lenOffset)
      );
      break;
    default:
      lenOffset = currentOffset + 5;
      len = __getLenFromTwoBytes(
        data.slice(currentOffset, currentOffset + lenOffset)
      );
  }

  const newOffset = lenOffset + len;

  return __toWordRanges(data, newOffset, [...acc, [lenOffset, newOffset]]);
}

const sliceWordRange = curryN(2, (data, range) =>
  slice(range[0], range[1], data)
);

const __wordRangesToWords = curryN(2, (data, wordRanges) =>
  map(pipe(sliceWordRange(data), toString))(wordRanges)
);

const parseApiSentence = (data) =>
  pipe(unary(__toWordRanges), __wordRangesToWords(data))(data);

module.exports = {
  __calculateLenBytes,
  __getLenFromSingleByte,
  __getLenFromTwoBytes,
  __getLenFromThreeBytes,
  __getLenFromFourBytes,
  __getLenFromFiveBytes,
  __toWordRanges,
  __wordRangesToWords,
  parseApiSentence,
};


File: /test\protocol\index.spec.js
const { expect } = require('chai');

const { __encodeLength, toDeviceWord } = require('../../src/protocol/mappers');
const {
  __calculateLenBytes,
  __getLenFromSingleByte,
  __getLenFromTwoBytes,
  __getLenFromThreeBytes,
  __getLenFromFourBytes,
  __getLenFromFiveBytes,
  parseApiSentence,
} = require('../../src/protocol/parsers');

describe('protocol', () => {
  describe('encode/decode single byte length', () => {
    it('should encode length <128 using single byte', () => {
      const encodedLen = __encodeLength(55);

      expect(encodedLen.length).equal(1);
      expect(encodedLen[0]).equal(55);
    });

    it('should be able to parse single byte length', () => {
      const encodedLen = __encodeLength(62);

      expect(__calculateLenBytes(encodedLen[0])).equal(1);
      expect(__getLenFromSingleByte(encodedLen)).equal(62);
    });
  });

  describe('encode/decode two byte length', () => {
    it('should encode length <16384 using two byte', () => {
      const encodedLen = __encodeLength(10000);

      expect(encodedLen.length).equal(2);
    });

    it('should be able to parse two byte length', () => {
      const encodedLen = __encodeLength(10000);

      expect(__calculateLenBytes(encodedLen[0])).equal(2);
      expect(__getLenFromTwoBytes(encodedLen)).equal(10000);
    });
  });

  describe('encode/decode three byte length', () => {
    it('should encode length <2097152 using three byte', () => {
      const encodedLen = __encodeLength(2097149);

      expect(encodedLen.length).equal(3);
    });

    it('should be able to parse three byte length', () => {
      const encodedLen = __encodeLength(2097149);

      expect(__calculateLenBytes(encodedLen[0])).equal(3);
      expect(__getLenFromThreeBytes(encodedLen)).equal(2097149);
    });
  });

  describe('encode/decode four byte length', () => {
    it('should encode length <268435456 using four byte', () => {
      const encodedLen = __encodeLength(268435455);

      expect(encodedLen.length).equal(4);
    });

    it('should be able to parse four byte length', () => {
      const encodedLen = __encodeLength(268435455);

      expect(__calculateLenBytes(encodedLen[0])).equal(4);
      expect(__getLenFromFourBytes(encodedLen)).equal(268435455);
    });
  });

  describe('encode/decode five byte length', () => {
    it('should encode length>=268435456 using five byte', () => {
      const encodedLen = __encodeLength(268435457);

      expect(encodedLen.length).equal(5);
    });

    it('should be able to parse five byte length', () => {
      const encodedLen = __encodeLength(268435457);

      expect(__calculateLenBytes(encodedLen[0])).equal(5);
      expect(__getLenFromFiveBytes(encodedLen)).equal(268435457);
    });
  });

  describe('parseApiSentence', () => {
    let originalWords;
    let encodedData;
    let result;

    before(() => {
      originalWords = [
        '/some/endpoint',
        '=some=attr',
        '=other=attr2',
        '.tag=xyzChannelId',
      ];

      encodedData = Buffer.concat(originalWords.map((w) => toDeviceWord(w)));

      result = parseApiSentence(encodedData);
    });

    it('should produce corrent number of words', () => {
      expect(result.length).equal(originalWords.length);
    });

    it('should produce words that are identical to input', () => {
      result.forEach((val, idx) => {
        expect(val).equal(originalWords[idx]);
      });
    });
  });
});


File: /test\protocol\mappers.spec.js
const { expect } = require('chai');
const Chance = require('chance');

const { toDeviceWord } = require('../../src/protocol/mappers');

describe('protocol/mappers', () => {
  describe('toDeviceWord', () => {
    it('should be a function', () => {
      expect(typeof toDeviceWord).equals('function');
    });

    it('should use single byte encoding for words shorter than 128 chars', () => {
      const word = '/some/endpoint';
      const encodedWord = toDeviceWord(word);
      const encodedFirstByte = encodedWord[0];
      const encodedRestString = encodedWord
        .slice(1, Number.MAX_SAFE_INTEGER)
        .toString();

      expect(encodedWord.length).equals(word.length + 1);
      expect(encodedFirstByte).equals(word.length);
      expect(encodedRestString).equals(word);
    });

    it('should use two byte encoding for words with length 128 <= l < 16384', () => {
      const generator = new Chance();
      const wordPayload = generator.paragraph({ length: 1000 });
      const word = `=comment=${wordPayload}`;
      const encodedWord = toDeviceWord(word);

      const encodedFirstByte = encodedWord[0];
      const encodedSecondByte = encodedWord[1];
      const encodedRestString = encodedWord
        .slice(2, Number.MAX_SAFE_INTEGER)
        .toString();

      expect(encodedFirstByte & 0xc0).equals(0x80);
      expect(((encodedFirstByte & ~0xc0) << 8) + encodedSecondByte).equals(
        word.length
      );
      expect(encodedRestString).equals(word);
    });

    it('should use three byte encoding for words with length 16384 <= l < 2097152', () => {
      const generator = new Chance();
      const wordPayload = generator.paragraph({ sentences: 22000 });
      const word = `=comment=${wordPayload}`;
      const encodedWord = toDeviceWord(word);

      const encodedFirstByte = encodedWord[0];
      const encodedSecondByte = encodedWord[1];
      const encodedThirdByte = encodedWord[2];
      const encodedRestString = encodedWord
        .slice(3, Number.MAX_SAFE_INTEGER)
        .toString();

      expect(encodedFirstByte & 0xe0).equals(0xc0);
      expect(
        ((encodedFirstByte & ~0xe0) << 16) +
          (encodedSecondByte << 8) +
          encodedThirdByte
      ).equals(word.length);
      expect(encodedRestString).equals(word);
    });
  });
});


File: /test\protocol\parsers.spec.js
const { expect } = require('chai');
const { toDeviceWord } = require('../../src/protocol/mappers');
const { parseApiSentence } = require('../../src/protocol/parsers');

describe('protocol', () => {
  describe('parsers', () => {
    let raw1byte;
    let raw2byte;
    let raw3byte;

    let encoded1byte;
    let encoded2byte;
    let encoded3byte;

    before(() => {
      raw1byte = `=attr=${'abcde'.repeat(10)}`;
      raw2byte = `=attribute=${'abcde'.repeat(Math.floor(16384 / 2 / 5))}`;
      raw3byte = `=attribute=${'abcde'.repeat(Math.floor(2097152 / 2 / 5))}`;

      encoded1byte = toDeviceWord(raw1byte);
      encoded2byte = toDeviceWord(raw2byte);
      encoded3byte = toDeviceWord(raw3byte);
    });

    it('should correctly parse sentence consisting of 1,2 and 3 byte words', () => {
      const result = parseApiSentence(
        Buffer.concat([encoded1byte, encoded2byte, encoded3byte])
      );

      expect(Array.isArray(result)).equal(true);
      expect(result[0]).equal(raw1byte);
      expect(result[1]).equal(raw2byte);
      expect(result[2]).equal(raw3byte);
    });
  });
});


File: /wip\api\index.js
const {
  identity,
  applySpec,
  always,
  curryN,
  over,
  lensProp,
  append,
} = require('ramda');

const query = require('./query');

const appendAttr = curryN(2, (sentence, attr) =>
  over(lensProp('attributes'), append(attr))(sentence)
);

const createCommand = applySpec({
  endpoint: identity,
  attributes: always([]),
  query: always([]),
  selectProps: always([]),
});

const addAtribute = curryN(3, (key, value, sentence) =>
  appendAttr(sentence, {
    key,
    value,
  })
);

module.exports = {
  query,
  createCommand,
  addAtribute,
};


File: /wip\api\query.js
const {
  applySpec,
  always,
  identity,
  over,
  lensProp,
  append,
  curryN,
  pipe,
} = require('ramda');

const appendQuery = curryN(2, (sentence, query) =>
  over(lensProp('query'), append(query))(sentence)
);

// (String, Sentence) -> (Sentence) -> Sentence
const hasProp = curryN(2, (name, sentence) =>
  pipe(
    applySpec({
      prefix: always('?'),
      key: identity,
      value: always(null),
    }),
    appendQuery(sentence)
  )(name)
);

// (String, String, Sentence) -> (Sentence, String) -> (Sentence) -> Sentence
const doesNotHaveProp = curryN(2, (name, sentence) =>
  pipe(
    applySpec({
      prefix: always('?-'),
      key: identity,
      value: always(null),
    }),
    appendQuery(sentence)
  )(name)
);

// (String, String, Sentence) -> (Sentence, String) -> (Sentence) -> Sentence
const propEq = curryN(3, (name, value, sentence) =>
  pipe(
    applySpec({
      prefix: always('?='),
      key: identity,
      value: always(value),
    }),
    appendQuery(sentence)
  )(name)
);

// (String, String, Sentence) -> (Sentence, String) -> (Sentence) -> Sentence
const propGt = curryN(3, (name, value, sentence) =>
  pipe(
    applySpec({
      prefix: always('?>'),
      key: identity,
      value: always(value),
    }),
    appendQuery(sentence)
  )(name)
);

// (String, String, Sentence) -> (Sentence, String) -> (Sentence) -> Sentence
const propLt = curryN(3, (name, value, sentence) =>
  pipe(
    applySpec({
      prefix: always('?<'),
      key: identity,
      value: always(value),
    }),
    appendQuery(sentence)
  )(name)
);

// (String, String, Sentence) -> (Sentence) -> Sentence
const propOperation = curryN(2, (op, sentence) =>
  pipe(
    applySpec({
      prefix: always('?#'),
      key: identity,
      value: always(null),
    }),
    appendQuery(sentence)
  )(op)
);

module.exports = {
  hasProp,
  doesNotHaveProp,
  propEq,
  propGt,
  propLt,
  propOperation,
};


File: /wip\client\index.js
const { Reader } = require('monet');
const { Observable } = require('rxjs');
const { generate: generateChannelId } = require('short-uuid');
const { assocPath } = require('ramda');
const { weave } = require('ramda-adjunct');
const split = require('binary-split');
const { map } = require('rxjs/operators');

const createApiMessage$ = (socket) =>
  Observable.create((observer) => {
    const handleData = (data) => observer.next(data);

    const splitStream = socket.pipe(split('\0'));

    splitStream.on('data', handleData);

    return () => splitStream.removeListener(handleData);
  }).pipe(map());

const createContext = (socket) => ({
  apiMessages$: createApiMessage$(socket),
  pendingCommands: [],
});

const cancelCommand = (tag) => Reader(({ context, socket }) => {});

const requestCancelCommand = (tag) =>
  Reader((config) =>
    process.setImmediate(() => {
      cancelCommand(tag).run(config);
    })
  );

const issueCommand = (command) =>
  Reader(
    ({ context, socket }) =>
      new Observable((observer) => {
        const commandWithTag = assocPath(['tag'], generateChannelId(), command);

        return () =>
          requestCancelCommand(commandWithTag.tag).run({ context, socket });
      })
  );

const createClient = (socket) => {};

module.exports = {
  createClient,
};


File: /wip\connection\index.js
const { connect } = require('net');
const { connect: connectTLS } = require('tls');
const { Observable, of } = require('rxjs');
const { mergeMap } = require('rxjs/operators');
const { always, unary, ifElse } = require('ramda');

const secureConnection = (socket) =>
  Observable.create((observer) => {
    const tlsSocket = connectTLS({ socket }, () => observer.next(tlsSocket));

    tlsSocket.once('error', (e) => observer.error(e));
    tlsSocket.once('end', () => observer.complete());

    return () => tlsSocket.destroy();
  });

const createConnection = ({ host, port, secure = false }) =>
  Observable.create((observer) => {
    const thePort = port || (secure ? 8729 : 8728);

    if (!host) {
      observer.error(new Error('host is required'));
      return null;
    }
    const socket = connect({ host, thePort }, () => {
      observer.next(socket);
    });

    socket.once('error', (e) => observer.error(e));
    socket.once('end', () => observer.complete());

    return () => socket.destroy();
  }).pipe(mergeMap(unary(ifElse(always(secure), secureConnection, unary(of)))));

module.exports = {
  createConnection,
};


