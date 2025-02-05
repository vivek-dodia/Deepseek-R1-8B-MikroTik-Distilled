# Repository Information
Name: nodejs-mikrotik-radius-server

# Directory Structure
Directory structure:
└── github_repos/nodejs-mikrotik-radius-server/
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
    │   │       ├── pack-d8a6e1b202b35de407fa08afc163507fcdd52b70.idx
    │   │       └── pack-d8a6e1b202b35de407fa08afc163507fcdd52b70.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── ecosystem.config.js.example
    ├── package.json
    ├── README.md
    ├── src/
    │   ├── admin-panel/
    │   │   └── wip
    │   ├── radius-server/
    │   │   ├── .env.example
    │   │   ├── dictionary.mikrotik
    │   │   ├── handler.js
    │   │   ├── repository/
    │   │   │   └── user.js
    │   │   ├── server.js
    │   │   └── server.x.js
    │   └── util.js
    └── yarn.lock


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
	url = https://github.com/lakuapik/nodejs-mikrotik-radius-server.git
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
0000000000000000000000000000000000000000 c0641df0fd1865de3a5443fdb28c8cfaec95c837 vivek-dodia <vivek.dodia@icloud.com> 1738606029 -0500	clone: from https://github.com/lakuapik/nodejs-mikrotik-radius-server.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c0641df0fd1865de3a5443fdb28c8cfaec95c837 vivek-dodia <vivek.dodia@icloud.com> 1738606029 -0500	clone: from https://github.com/lakuapik/nodejs-mikrotik-radius-server.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c0641df0fd1865de3a5443fdb28c8cfaec95c837 vivek-dodia <vivek.dodia@icloud.com> 1738606029 -0500	clone: from https://github.com/lakuapik/nodejs-mikrotik-radius-server.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c0641df0fd1865de3a5443fdb28c8cfaec95c837 refs/remotes/origin/master


File: /.git\refs\heads\master
c0641df0fd1865de3a5443fdb28c8cfaec95c837


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
node_modules

src/admin-panel/.env
src/radius-server/.env
ecosystem.config.js

File: /ecosystem.config.js.example
module.exports = {
  apps : [{
    name: 'radius-server',
    script: 'src/radius-server/server.js',
    args: '',
    instances: 1,
    autorestart: true,
    watch: true,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }],
};


File: /package.json
{
  "name": "nodejs-mikrotik-radius-server",
  "version": "0.0.1",
  "description": "A simple implementation of nodejs as radius server for mikrotik",
  "main": "index.js",
  "repository": "https://github.com/lakuapik/nodejs-mikrotik-radius-server",
  "author": "David Adi Nugroho",
  "license": "MIT",
  "dependencies": {
    "dotenv": "^8.2.0",
    "radius": "^1.1.4"
  }
}


File: /README.md
# NodeJS Mikrotik Radius Server

> This is a wip project.

A simple implementation of nodejs as radius server for mikrotik.

There are two app:
* `radius-server` for handling radius request
* `admin-panel` for managing radius users

File: /src\radius-server\.env.example
RADIUS_HOST=0.0.0.0
RADIUS_PORT=1812
RADIUS_SECRET=s3cr3t

File: /src\radius-server\dictionary.mikrotik
#####
# Copied from: https://wiki.mikrotik.com/index.php?title=Manual:RADIUS_Client/vendor_dictionary
# Date: 2020-08-13 01:53:20 GMT+7
#####

# MikroTik vendor specific dictionary
# Copyright (C) MikroTikls, SIA
#
# You may freely redistribute and use this software or any part of it in source
# and/or binary forms, with or without modification for any purposes without
# limitations, provided that you respect the following statement:
#
# This software is provided 'AS IS' without a warranty of any kind, expressed or
# implied, including, but not limited to, the implied warranty of
# merchantability and fitness for a particular purpose. In no event shall
# MikroTikls SIA be liable for direct or indirect, incidental, consequential or
# other damages that may result from the use of this software, including, but
# not limited to, loss of data, time and (or) profits.
#
# $Id: dictionary.mikrotik,v 1.8 2019/12/20 11:02:37 strods Exp $
#
# MikroTik Attributes

VENDOR          Mikrotik        14988

BEGIN-VENDOR    Mikrotik

ATTRIBUTE       Mikrotik-Recv-Limit             1   integer
ATTRIBUTE       Mikrotik-Xmit-Limit             2   integer
ATTRIBUTE       Mikrotik-Group                  3   string
ATTRIBUTE       Mikrotik-Wireless-Forward       4   integer
ATTRIBUTE       Mikrotik-Wireless-Skip-Dot1x    5   integer
ATTRIBUTE       Mikrotik-Wireless-Enc-Algo      6   integer
ATTRIBUTE       Mikrotik-Wireless-Enc-Key       7   string
ATTRIBUTE       Mikrotik-Rate-Limit             8   string
ATTRIBUTE       Mikrotik-Realm                  9   string
ATTRIBUTE       Mikrotik-Host-IP                10  ipaddr
ATTRIBUTE       Mikrotik-Mark-Id                11  string
ATTRIBUTE       Mikrotik-Advertise-URL          12  string
ATTRIBUTE       Mikrotik-Advertise-Interval     13  integer
ATTRIBUTE       Mikrotik-Recv-Limit-Gigawords   14  integer
ATTRIBUTE       Mikrotik-Xmit-Limit-Gigawords   15  integer
ATTRIBUTE       Mikrotik-Wireless-PSK           16  string
ATTRIBUTE       Mikrotik-Total-Limit            17  integer
ATTRIBUTE       Mikrotik-Total-Limit-Gigawords  18  integer
ATTRIBUTE       Mikrotik-Address-List           19  string
ATTRIBUTE       Mikrotik-Wireless-MPKey         20  string
ATTRIBUTE       Mikrotik-Wireless-Comment       21  string
ATTRIBUTE       Mikrotik-Delegated-IPv6-Pool    22  string
ATTRIBUTE       Mikrotik-DHCP-Option-Set        23  string
ATTRIBUTE       Mikrotik-DHCP-Option-Param-STR1 24  string
ATTRIBUTE       Mikortik-DHCP-Option-Param-STR2 25  string
ATTRIBUTE       Mikrotik-Wireless-VLANID        26  integer
ATTRIBUTE       Mikrotik-Wireless-VLANIDtype    27  integer
ATTRIBUTE       Mikrotik-Wireless-Minsignal     28  string
ATTRIBUTE       Mikrotik-Wireless-Maxsignal     29  string
ATTRIBUTE       Mikrotik-Switching-Filter       30  string

# MikroTik Values

VALUE           Mikrotik-Wireless-Enc-Algo            No-encryption                  0
VALUE           Mikrotik-Wireless-Enc-Algo            40-bit-WEP                     1
VALUE           Mikrotik-Wireless-Enc-Algo            104-bit-WEP                    2
VALUE           Mikrotik-Wireless-Enc-Algo            AES-CCM                        3
VALUE           Mikrotik-Wireless-Enc-Algo            TKIP                           4
VALUE           Mikrotik-Wireless-VLANIDtype          802.1q                         0
VALUE           Mikrotik-Wireless-VLANIDtype          802.1ad                        1

END-VENDOR      Mikrotik

File: /src\radius-server\handler.js
require("dotenv").config({ path: `${__dirname}/.env` });

const radius = require("radius");
const userRepo = require("./repository/user");

const encodeResponse = (data) => {
  console.log("Preparing response, data: ", data);
  return radius.encode(data);
}

exports.handleAccessRequest = (packet) => {
  let responseData = {
    secret: process.env.RADIUS_SECRET,
    identifier: packet.identifier,
    authenticator: packet.authenticator,
  };

  const user = userRepo.verify(
    packet.attributes["User-Name"],
    packet.attributes["User-Password"]
  );

  if (user === undefined) {
    responseData.code = "Access-Reject";
    return encodeResponse(responseData)
  }

  Object.assign(responseData, {
    code: "Access-Accept",
    attributes: [
      [
        "Vendor-Specific",
        "Mikrotik",
        [
          ["Mikrotik-Group", user.group],
          ["Mikrotik-Rate-Limit", user.rate_limit],
        ],
      ],
    ],
  });

  return encodeResponse(responseData);
};

exports.handleAccountingRequest = (packet) => {
  let responseData = {
    code: "Accounting-Response",
    secret: process.env.RADIUS_SECRET,
    identifier: packet.identifier,
    authenticator: packet.authenticator,
  };

  return encodeResponse(responseData);
};


File: /src\radius-server\repository\user.js
const util = require("../../util");

const users = [
  {
    id: 1,
    username: "user1",
    password: util.sha1("secret"),
    group: "uprof1",
    rate_limit: "50M/50M",
    session_time: 60, // in seconds
  },
  {
    id: 1,
    username: "user2",
    password: util.sha1("secret"),
    group: "uprof1",
    rate_limit: "20M/20M",
    session_time: 60 * 2, // in seconds
  },
];

exports.verify = (username, password) => {
  return users.find(
    (u) => username == u.username && util.sha1(password) == u.password
  );
};


File: /src\radius-server\server.js
require("dotenv").config({ path: `${__dirname}/.env` });

const host = process.env.RADIUS_HOST;
const port = process.env.RADIUS_PORT;

const dgram = require("dgram");
const radius = require("radius");
const handler = require("./handler");

radius.add_dictionary(`${__dirname}/dictionary.mikrotik`);

const server = dgram.createSocket("udp4");

server.on("listening", () =>
  console.log(`radius-server listening on ${host}:${port}`)
);

server.on("message", (message, rinfo) => {
  let packet = null;
  let response = null;

  try {
    packet = radius.decode({
      packet: message,
      secret: process.env.RADIUS_SECRET,
    });
  } catch (error) {
    console.log("Failed to decode radius packet, silently dropping:", error);
    return;
  }

  console.log(
    `Incoming packet, code: "${packet.code}", attributes: `,
    packet.attributes
  );

  switch (packet.code) {
    case "Access-Request":
      response = handler.handleAccessRequest(packet);
      break;
    case "Accounting-Request":
      response = handler.handleAccountingRequest(packet);
      break;
    default:
      console.log("Unknown packet type: ", packet.code);
      break;
  }

  if (response === null) {
    console.log("Failed to build response, silently dropping");
    return;
  }

  server.send(response, 0, response.length, rinfo.port, rinfo.address);
});

server.bind(port, host);


File: /src\radius-server\server.x.js
// Example radius server doing authentication

var radius = require('radius');
var dgram = require("dgram");

var secret = 'radius_secret';
var server = dgram.createSocket("udp4");

radius.add_dictionary(__dirname + '/dictionaries/dictionary.mikrotik');

server.on("message", function (msg, rinfo) {
  var code, username, password, packet;
  try {
    packet = radius.decode({packet: msg, secret: secret});
  } catch (e) {
    console.log("Failed to decode radius packet, silently dropping:", e);
    return;
  }

  if (packet.code != 'Access-Request') {
    console.log('unknown packet type: ', packet.code);
    return;
  }

  console.log(packet)

  username = packet.attributes['User-Name'];
  password = packet.attributes['User-Password'];

  console.log('Access-Request for ' + username + ':' + password);

  if (username == 'halo' && password == 'loha') {
    code = 'Access-Accept';
  } else {
    code = 'Access-Reject';
  }

  var attrs = [
    ['NAS-Port-Type', packet.attributes['NAS-Port-Type']],
    ['Calling-Station-Id', packet.attributes['Calling-Station-Id']],
    ['Called-Station-Id', packet.attributes['Called-Station-Id']],
    ['NAS-Port-Id', packet.attributes['NAS-Port-Id']],
    ['User-Name', packet.attributes['User-Name']],
    ['NAS-Port', packet.attributes['NAS-Port']],
    ['Acct-Session-Id', packet.attributes['Acct-Session-Id']],
    ['Framed-IP-Address', packet.attributes['Framed-IP-Address']],
    ['User-Password', packet.attributes['User-Password']],
    ['Service-Type', packet.attributes['Service-Type']],
    ['NAS-Identifier', packet.attributes['NAS-Identifier']],
    ['NAS-IP-Address', packet.attributes['NAS-IP-Address']],
    ['Vendor-Specific', 'Mikrotik', [
      ['Mikrotik-Host-IP', packet.attributes['Vendor-Specific']['Mikrotik-Host-IP']],
      ['Mikrotik-Rate-Limit', '50M/50M'],
    ]],
  ];

  var response = radius.encode({
    code: code,
    secret: secret,
    attributes: attrs,
    identifier: packet.identifier,
    authenticator: packet.authenticator,
  });

  console.log(response);

  var x = radius.decode({packet: response, secret: secret});

  console.log(x);

  // var response = radius.encode_response({
  //   packet: packet,
  //   code: code,
  //   secret: secret
  // });

  console.log('Sending ' + code + ' for user ' + username);
  server.send(response, 0, response.length, rinfo.port, rinfo.address, function(err, bytes) {
    if (err) {
      console.log('Error sending response to ', rinfo);
    }
  });
});

server.on("listening", function () {
  var address = server.address();
  console.log("radius server listening " +
      address.address + ":" + address.port);
});

server.bind(1812);

File: /src\util.js
exports.sha1 = (value) => {
    return require('crypto').createHash('sha1').update(value).digest('hex');
}

File: /yarn.lock
# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
# yarn lockfile v1


dotenv@^8.2.0:
  version "8.2.0"
  resolved "https://registry.yarnpkg.com/dotenv/-/dotenv-8.2.0.tgz#97e619259ada750eea3e4ea3e26bceea5424b16a"
  integrity sha512-8sJ78ElpbDJBHNeBzUbUVLsqKdccaa/BXF1uPTw3GrvQTBgrQrtObr2mUrE38vzYd8cEv+m/JBfDLioYcfXoaw==

radius@^1.1.4:
  version "1.1.4"
  resolved "https://registry.yarnpkg.com/radius/-/radius-1.1.4.tgz#3ce58d18a497d615618bc7d9286464ebecb50cb5"
  integrity sha512-UWuzdF6xf3NpsXFZZmUEkxtEalDXj8hdmMXgbGzn7vOk6zXNsiIY2I6SJ1euHt7PTQuMoz2qDEJB+AfJDJgQYw==


