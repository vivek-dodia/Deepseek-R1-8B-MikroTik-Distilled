# Repository Information
Name: ApiMikrotik

# Directory Structure
Directory structure:
└── github_repos/ApiMikrotik/
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
    │   │       ├── pack-22278f2914a47d6dfa43999bfba9eff1c0249481.idx
    │   │       └── pack-22278f2914a47d6dfa43999bfba9eff1c0249481.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── backend/
    │   ├── .gitattributes
    │   ├── .gitignore
    │   ├── app.js
    │   ├── app2.js
    │   ├── config/
    │   │   ├── database/
    │   │   │   └── mysql.example.js
    │   │   └── password.example.js
    │   ├── package-lock.json
    │   ├── package.json
    │   └── test.js
    └── frontend/
        ├── .gitignore
        ├── components/
        │   ├── date.js
        │   ├── layout.js
        │   └── layout.module.css
        ├── lib/
        │   └── posts.js
        ├── package-lock.json
        ├── package.json
        ├── pages/
        │   ├── index.js
        │   ├── posts/
        │   │   └── [id].js
        │   └── _app.js
        ├── posts/
        │   ├── pre-rendering.md
        │   └── ssg-ssr.md
        ├── public/
        │   └── images/
        ├── README.md
        └── styles/
            ├── global.css
            └── utils.module.css


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
	url = https://github.com/Maiconfsantos/ApiMikrotik.git
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
0000000000000000000000000000000000000000 149d7924c430b61ff53e69a0aeefb0a856ab2877 vivek-dodia <vivek.dodia@icloud.com> 1738606395 -0500	clone: from https://github.com/Maiconfsantos/ApiMikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 149d7924c430b61ff53e69a0aeefb0a856ab2877 vivek-dodia <vivek.dodia@icloud.com> 1738606395 -0500	clone: from https://github.com/Maiconfsantos/ApiMikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 149d7924c430b61ff53e69a0aeefb0a856ab2877 vivek-dodia <vivek.dodia@icloud.com> 1738606395 -0500	clone: from https://github.com/Maiconfsantos/ApiMikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
149d7924c430b61ff53e69a0aeefb0a856ab2877 refs/remotes/origin/master


File: /.git\refs\heads\master
149d7924c430b61ff53e69a0aeefb0a856ab2877


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore

backend/config/database/mysql.js


File: /backend\.gitattributes
# Auto detect text files and perform LF normalization
* text=auto


File: /backend\.gitignore
# Logs
logs
File: /backend\app.js
const express = require('express')
const app = express()
const port = 3000

const api = require('mikronode');
let passwords = require('./config/password')
let dbConn = require('./config/database/mysql')

let info = [];

let info2 = [];

app.get('/', async  (req, res) => {
   info2 = [];
   data = getDevices();

   await data.then( async (data) => {
      var device;

      let promise = new Promise ( async function (resolve, reject){
         Promise.all(data.map(async function (element)  {
            device=new api(element.IPv4 , '1420');
            info = [];
            await connect(device);
            info2 = [...info2,{
               localname: element.name,
               localIP: element.IPv4,
               IPaddress: info
            }];    
         })).then(() =>{

            resolve(info2); 
         })    
      })

      promise.then( (data) =>{
         res.json(data);
      })
   })
   
   
})

async function getDevices(){
   return new Promise(async function(resolve, reject){
      await dbConn.query("select * from devices where IPv4='10.255.2.254'", function (err, rows) {
         resolve(rows);
      });

   })
   
}

async function connect(device){

   await device.connect()
   .then(([login])=>{
     return login(passwords.mikrotikEquipamentUser,passwords.mikrotikEquipament);
   })
   .then(function(conn) {
     
      var chan=conn.openChannel("addresses"); // open a named channel
      chan.write('/ip/address/print');

   
      return new Promise((resolve, reject)=>{
         if(!chan) reject('sem conexao');
         chan.on('done',async function(data) {
            chan.close();
            conn.close();
            info = data.data
            resolve(data.data)            
         }); 
      }) 
   }, (reject) =>{
     // console.log('error:', reject)
   })
}


app.listen(port, () => {
  //console.log(`Example app listening at http://localhost:${port}`)
})

File: /backend\app2.js
const express = require('express')
const app = express()
const port = 3000

const api = require('mikronode');
let passwords = require('./config/password')
let dbConn = require('./config/database/mysql')

let info = [];

let info2 = [];

app.get('/', async  (req, res) => {
   info2 = [];
   data = getDevices();

   await data.then( async (data) => {
      var device;

      let promise = new Promise ( async function (resolve, reject){
         Promise.all(data.map(async function (element)  {
            info=[];
            device=new api(element.IPv4 , '1420');
            await connect(device);
            info2 = [...info2,{
               localname: element.name,
               localIP: element.IPv4,
               IPaddress: info
            }];    
         })).then(() =>{

            resolve(info2); 
         })    
      })

      promise.then( (data) =>{
         res.json(data);
      })
   })
   
   
})

async function getDevices(){
   return new Promise(async function(resolve, reject){
      await dbConn.query("select * from devices where IPv4='10.255.2.254'", function (err, rows) {
         resolve(rows);
      });

   })
   
}

async function connect(device){

   await device.connect()
   .then(([login])=>{
     return login(passwords.mikrotikEquipamentUser,passwords.mikrotikEquipament);
   })
   .then(function(conn) {
     
      var chan=conn.openChannel();
      chan.write('/interface/print');

   
      return new Promise((resolve, reject)=>{
         if(!chan) reject('sem conexao');
         chan.on('done',async function(data) {
            chan.close();
            conn.close();
            data.data.map((port)=>{
                if (port[3].value == 'ether'){
                    info=[...info, port]
                }
            })
            resolve(data.data)            
         }); 
      }) 
   }, (reject) =>{
     // console.log('error:', reject)
   })
}


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

File: /backend\config\database\mysql.example.js
var mysql = require('mysql');

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'user',
    password: 'pass',
    database: 'database'
})

connection.connect();

module.exports = connection;

File: /backend\config\password.example.js
var passwords = {
    mikrotikEquipament: 'yourPassword',
    mikrotikEquipamentUser: 'yourUsername',
}


module.exports = passwords;

File: /backend\package-lock.json
{
  "name": "apimikrotik",
  "version": "1.0.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "accepts": {
      "version": "1.3.7",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.7.tgz",
      "integrity": "sha512-Il80Qs2WjYlJIBNzNkK6KYqlVMTbZLXgHx2oT0pU/fjRHyEp+PEfEPY0R3WCwAGVOtauxh1hOxNgIf5bv7dQpA==",
      "requires": {
        "mime-types": "~2.1.24",
        "negotiator": "0.6.2"
      }
    },
    "array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha1-ml9pkFGx5wczKPKgCJaLZOopVdI="
    },
    "bignumber.js": {
      "version": "9.0.0",
      "resolved": "https://registry.npmjs.org/bignumber.js/-/bignumber.js-9.0.0.tgz",
      "integrity": "sha512-t/OYhhJ2SD+YGBQcjY8GzzDHEk9f3nerxjtfa6tlMXfe7frs/WozhvCNoGvpM0P3bNf3Gq5ZRMlGr5f3r4/N8A=="
    },
    "body-parser": {
      "version": "1.19.0",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.19.0.tgz",
      "integrity": "sha512-dhEPs72UPbDnAQJ9ZKMNTP6ptJaionhP5cBb541nXPlW60Jepo9RV/a4fX4XWW9CuFNK22krhrj1+rgzifNCsw==",
      "requires": {
        "bytes": "3.1.0",
        "content-type": "~1.0.4",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "http-errors": "1.7.2",
        "iconv-lite": "0.4.24",
        "on-finished": "~2.3.0",
        "qs": "6.7.0",
        "raw-body": "2.4.0",
        "type-is": "~1.6.17"
      }
    },
    "bytes": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.0.tgz",
      "integrity": "sha512-zauLjrfCG+xvoyaqLoV8bLVXXNGC4JqlxFCutSDWA6fJrTo2ZuvLYTqZ7aHBLZSMOopbzwv8f+wZcVzfVTI2Dg=="
    },
    "content-disposition": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.3.tgz",
      "integrity": "sha512-ExO0774ikEObIAEV9kDo50o+79VCUdEB6n6lzKgGwupcVeRlhrj3qGAfwq8G6uBJjkqLrhT0qEYFcWng8z1z0g==",
      "requires": {
        "safe-buffer": "5.1.2"
      }
    },
    "content-type": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.4.tgz",
      "integrity": "sha512-hIP3EEPs8tB9AT1L+NUqtwOAps4mk2Zob89MWXMHjHWg9milF/j4osnnQLXBCBFBk/tvIG/tUc9mOUJiPBhPXA=="
    },
    "cookie": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.4.0.tgz",
      "integrity": "sha512-+Hp8fLp57wnUSt0tY0tHEXh4voZRDnoIrZPqlo3DPiI4y9lwg/jqx+1Om94/W6ZaPDOUbnjOt/99w66zk+l1Xg=="
    },
    "cookie-signature": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
      "integrity": "sha1-4wOogrNCzD7oylE6eZmXNNqzriw="
    },
    "core-decorators": {
      "version": "0.20.0",
      "resolved": "https://registry.npmjs.org/core-decorators/-/core-decorators-0.20.0.tgz",
      "integrity": "sha1-YFiWYkBTr4wo775zXCWjAaYcZcU="
    },
    "core-util-is": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
      "integrity": "sha1-tf1UIgqivFq1eqtxQMlAdUUDwac="
    },
    "debug": {
      "version": "2.6.9",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
      "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
      "requires": {
        "ms": "2.0.0"
      }
    },
    "depd": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
      "integrity": "sha1-m81S4UwJd2PnSbJ0xDRu0uVgtak="
    },
    "destroy": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz",
      "integrity": "sha1-l4hXRCxEdJ5CBmE+N5RiBYJqvYA="
    },
    "ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha1-WQxhFWsK4vTwJVcyoViyZrxWsh0="
    },
    "encodeurl": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
      "integrity": "sha1-rT/0yG7C0CkyL1oCw6mmBslbP1k="
    },
    "escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha1-Aljq5NPQwJdN4cFpGI7wBR0dGYg="
    },
    "etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha1-Qa4u62XvpiJorr/qg6x9eSmbCIc="
    },
    "express": {
      "version": "4.17.1",
      "resolved": "https://registry.npmjs.org/express/-/express-4.17.1.tgz",
      "integrity": "sha512-mHJ9O79RqluphRrcw2X/GTh3k9tVv8YcoyY4Kkh4WDMUYKRZUq0h1o0w2rrrxBqM7VoeUVqgb27xlEMXTnYt4g==",
      "requires": {
        "accepts": "~1.3.7",
        "array-flatten": "1.1.1",
        "body-parser": "1.19.0",
        "content-disposition": "0.5.3",
        "content-type": "~1.0.4",
        "cookie": "0.4.0",
        "cookie-signature": "1.0.6",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "~1.1.2",
        "fresh": "0.5.2",
        "merge-descriptors": "1.0.1",
        "methods": "~1.1.2",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.3",
        "path-to-regexp": "0.1.7",
        "proxy-addr": "~2.0.5",
        "qs": "6.7.0",
        "range-parser": "~1.2.1",
        "safe-buffer": "5.1.2",
        "send": "0.17.1",
        "serve-static": "1.14.1",
        "setprototypeof": "1.1.1",
        "statuses": "~1.5.0",
        "type-is": "~1.6.18",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      }
    },
    "finalhandler": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.1.2.tgz",
      "integrity": "sha512-aAWcW57uxVNrQZqFXjITpW3sIUQmHGG3qSb9mUah9MgMC4NeWhNOlNjXEYq3HjRAvL6arUviZGGJsBg6z0zsWA==",
      "requires": {
        "debug": "2.6.9",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.3",
        "statuses": "~1.5.0",
        "unpipe": "~1.0.0"
      }
    },
    "forwarded": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.1.2.tgz",
      "integrity": "sha1-mMI9qxF1ZXuMBXPozszZGw/xjIQ="
    },
    "fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha1-PYyt2Q2XZWn6g1qx+OSyOhBWBac="
    },
    "http-errors": {
      "version": "1.7.2",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.7.2.tgz",
      "integrity": "sha512-uUQBt3H/cSIVfch6i1EuPNy/YsRSOUBXTVfZ+yR7Zjez3qjBz6i9+i4zjNaoqcoFVI4lQJ5plg63TvGfRSDCRg==",
      "requires": {
        "depd": "~1.1.2",
        "inherits": "2.0.3",
        "setprototypeof": "1.1.1",
        "statuses": ">= 1.5.0 < 2",
        "toidentifier": "1.0.0"
      }
    },
    "iconv-lite": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz",
      "integrity": "sha512-v3MXnZAcvnywkTUEZomIActle7RXXeedOR31wwl7VlyoXO4Qi9arvSenNQWne1TcRwhCL1HwLI21bEqdpj8/rA==",
      "requires": {
        "safer-buffer": ">= 2.1.2 < 3"
      }
    },
    "inherits": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
      "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4="
    },
    "ipaddr.js": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.9.1.tgz",
      "integrity": "sha512-0KI/607xoxSToH7GjN1FfSbLoU0+btTicjsQSWQlh/hZykN8KpmMf7uYwPW3R+akZ6R/w18ZlXSHBYXiYUPO3g=="
    },
    "isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha1-u5NdSFgsuhaMBoNJV6VKPgcSTxE="
    },
    "media-typer": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha1-hxDXrwqmJvj/+hzgAWhUUmMlV0g="
    },
    "merge-descriptors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz",
      "integrity": "sha1-sAqqVW3YtEVoFQ7J0blT8/kMu2E="
    },
    "methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha1-VSmk1nZUE07cxSZmVoNbD4Ua/O4="
    },
    "mikronode": {
      "version": "2.3.11",
      "resolved": "https://registry.npmjs.org/mikronode/-/mikronode-2.3.11.tgz",
      "integrity": "sha512-FRtWHZFPhyPEA+7qwGJK7clU8gjz+TdPy8JizuEGTroqiJ9J0vSoOLPu5kUocv2nTyMsljc44O9OzOT7eWI25Q=="
    },
    "mime": {
      "version": "1.6.0",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.6.0.tgz",
      "integrity": "sha512-x0Vn8spI+wuJ1O6S7gnbaQg8Pxh4NNHb7KSINmEWKiPE4RKOplvijn+NkmYmmRgP68mc70j2EbeTFRsrswaQeg=="
    },
    "mime-db": {
      "version": "1.44.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.44.0.tgz",
      "integrity": "sha512-/NOTfLrsPBVeH7YtFPgsVWveuL+4SjjYxaQ1xtM1KMFj7HdxlBlxeyNLzhyJVx7r4rZGJAZ/6lkKCitSc/Nmpg=="
    },
    "mime-types": {
      "version": "2.1.27",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.27.tgz",
      "integrity": "sha512-JIhqnCasI9yD+SsmkquHBxTSEuZdQX5BuQnS2Vc7puQQQ+8yiP5AY5uWhpdv4YL4VM5c6iliiYWPgJ/nJQLp7w==",
      "requires": {
        "mime-db": "1.44.0"
      }
    },
    "ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
    },
    "mysql": {
      "version": "2.18.1",
      "resolved": "https://registry.npmjs.org/mysql/-/mysql-2.18.1.tgz",
      "integrity": "sha512-Bca+gk2YWmqp2Uf6k5NFEurwY/0td0cpebAucFpY/3jhrwrVGuxU2uQFCHjU19SJfje0yQvi+rVWdq78hR5lig==",
      "requires": {
        "bignumber.js": "9.0.0",
        "readable-stream": "2.3.7",
        "safe-buffer": "5.1.2",
        "sqlstring": "2.3.1"
      }
    },
    "negotiator": {
      "version": "0.6.2",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.2.tgz",
      "integrity": "sha512-hZXc7K2e+PgeI1eDBe/10Ard4ekbfrrqG8Ep+8Jmf4JID2bNg7NvCPOZN+kfF574pFQI7mum2AUqDidoKqcTOw=="
    },
    "on-finished": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz",
      "integrity": "sha1-IPEzZIGwg811M3mSoWlxqi2QaUc=",
      "requires": {
        "ee-first": "1.1.1"
      }
    },
    "parseurl": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz",
      "integrity": "sha512-CiyeOxFT/JZyN5m0z9PfXw4SCBJ6Sygz1Dpl0wqjlhDEGGBP1GnsUVEL0p63hoG1fcj3fHynXi9NYO4nWOL+qQ=="
    },
    "path-to-regexp": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz",
      "integrity": "sha1-32BBeABfUi8V60SQ5yR6G/qmf4w="
    },
    "process-nextick-args": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
      "integrity": "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag=="
    },
    "proxy-addr": {
      "version": "2.0.6",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.6.tgz",
      "integrity": "sha512-dh/frvCBVmSsDYzw6n926jv974gddhkFPfiN8hPOi30Wax25QZyZEGveluCgliBnqmuM+UJmBErbAUFIoDbjOw==",
      "requires": {
        "forwarded": "~0.1.2",
        "ipaddr.js": "1.9.1"
      }
    },
    "qs": {
      "version": "6.7.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.7.0.tgz",
      "integrity": "sha512-VCdBRNFTX1fyE7Nb6FYoURo/SPe62QCaAyzJvUjwRaIsc+NePBEniHlvxFmmX56+HZphIGtV0XeCirBtpDrTyQ=="
    },
    "range-parser": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.1.tgz",
      "integrity": "sha512-Hrgsx+orqoygnmhFbKaHE6c296J+HTAQXoxEF6gNupROmmGJRoyzfG3ccAveqCBrwr/2yxQ5BVd/GTl5agOwSg=="
    },
    "raw-body": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.4.0.tgz",
      "integrity": "sha512-4Oz8DUIwdvoa5qMJelxipzi/iJIi40O5cGV1wNYp5hvZP8ZN0T+jiNkL0QepXs+EsQ9XJ8ipEDoiH70ySUJP3Q==",
      "requires": {
        "bytes": "3.1.0",
        "http-errors": "1.7.2",
        "iconv-lite": "0.4.24",
        "unpipe": "1.0.0"
      }
    },
    "readable-stream": {
      "version": "2.3.7",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz",
      "integrity": "sha512-Ebho8K4jIbHAxnuxi7o42OrZgF/ZTNcsZj6nRKyUmkhLFq8CHItp/fy6hQZuZmP/n3yZ9VBUbp4zz/mX8hmYPw==",
      "requires": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      }
    },
    "rxjs": {
      "version": "5.3.3",
      "resolved": "https://registry.npmjs.org/rxjs/-/rxjs-5.3.3.tgz",
      "integrity": "sha1-3S+VEF9xPZXyW4lMvl9opfMskmw=",
      "requires": {
        "symbol-observable": "^1.0.1"
      }
    },
    "safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="
    },
    "safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg=="
    },
    "send": {
      "version": "0.17.1",
      "resolved": "https://registry.npmjs.org/send/-/send-0.17.1.tgz",
      "integrity": "sha512-BsVKsiGcQMFwT8UxypobUKyv7irCNRHk1T0G680vk88yf6LBByGcZJOTJCrTP2xVN6yI+XjPJcNuE3V4fT9sAg==",
      "requires": {
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "destroy": "~1.0.4",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "0.5.2",
        "http-errors": "~1.7.2",
        "mime": "1.6.0",
        "ms": "2.1.1",
        "on-finished": "~2.3.0",
        "range-parser": "~1.2.1",
        "statuses": "~1.5.0"
      },
      "dependencies": {
        "ms": {
          "version": "2.1.1",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.1.tgz",
          "integrity": "sha512-tgp+dl5cGk28utYktBsrFqA7HKgrhgPsg6Z/EfhWI4gl1Hwq8B/GmY/0oXZ6nF8hDVesS/FpnYaD/kOWhYQvyg=="
        }
      }
    },
    "serve-static": {
      "version": "1.14.1",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.14.1.tgz",
      "integrity": "sha512-JMrvUwE54emCYWlTI+hGrGv5I8dEwmco/00EvkzIIsR7MqrHonbD9pO2MOfFnpFntl7ecpZs+3mW+XbQZu9QCg==",
      "requires": {
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.3",
        "send": "0.17.1"
      }
    },
    "setprototypeof": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.1.tgz",
      "integrity": "sha512-JvdAWfbXeIGaZ9cILp38HntZSFSo3mWg6xGcJJsd+d4aRMOqauag1C63dJfDw7OaMYwEbHMOxEZ1lqVRYP2OAw=="
    },
    "sqlstring": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/sqlstring/-/sqlstring-2.3.1.tgz",
      "integrity": "sha1-R1OT/56RR5rqYtyvDKPRSYOn+0A="
    },
    "statuses": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz",
      "integrity": "sha1-Fhx9rBd2Wf2YEfQ3cfqZOBR4Yow="
    },
    "string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "requires": {
        "safe-buffer": "~5.1.0"
      }
    },
    "symbol-observable": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz",
      "integrity": "sha512-e900nM8RRtGhlV36KGEU9k65K3mPb1WV70OdjfxlG2EAuM1noi/E/BaW/uMhL7bPEssK8QV57vN3esixjUvcXQ=="
    },
    "toidentifier": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.0.tgz",
      "integrity": "sha512-yaOH/Pk/VEhBWWTlhI+qXxDFXlejDGcQipMlyxda9nthulaxLZUNcUqFxokp0vcYnvteJln5FNQDRrxj3YcbVw=="
    },
    "type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "requires": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      }
    },
    "unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha1-sr9O6FFKrmFltIF4KdIbLvSZBOw="
    },
    "util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha1-RQ1Nyfpw3nMnYvvS1KKJgUGaDM8="
    },
    "utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha1-n5VxD1CiZ5R7LMwSR0HBAoQn5xM="
    },
    "vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha1-IpnwLG3tMNSllhsLn3RSShj2NPw="
    }
  }
}


File: /backend\package.json
{
  "name": "apimikrotik",
  "version": "1.0.0",
  "description": "INB API Mikrotik",
  "main": "index.js",
  "scripts": {
    "test": "teste"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Maiconfsantos/ApiMikrotik.git"
  },
  "keywords": [
    "mikrotik"
  ],
  "author": "Maicon Flor dos Santos",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/Maiconfsantos/ApiMikrotik/issues"
  },
  "homepage": "https://github.com/Maiconfsantos/ApiMikrotik#readme",
  "dependencies": {
    "core-decorators": "^0.20.0",
    "express": "^4.17.1",
    "mikronode": "^2.3.11",
    "mysql": "^2.18.1",
    "rxjs": "^5.3.3"
  }
}


File: /backend\test.js
// Example function that returns a Promise that will resolve after 2 seconds
var getGenres = function() {
  return new Promise(function(resolve) {
    setTimeout(function(){
      resolve(['comedy', 'drama', 'action'])
    }, 2000);
  });
}

main()

// We start an 'async' function to use the 'await' keyword
async function main(){
  var result = await getGenres()
  console.log('Woo done!', result)


}

File: /frontend\.gitignore
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
File: /frontend\components\date.js
import { parseISO, format } from 'date-fns'

export default function Date({ dateString }) {
  const date = parseISO(dateString)
  return <time dateTime={dateString}>{format(date, 'LLLL d, yyyy')}</time>
}

File: /frontend\components\layout.js
import Head from 'next/head'
import styles from './layout.module.css'
import utilStyles from '../styles/utils.module.css'
import Link from 'next/link'

export const siteTitle = 'Next.js Sample Website'

export default function Layout({ children, home }) {
  return (
    <div className={styles.container}>
      <Head>
        <link rel="icon" href="/favicon.ico" />
        <meta
          name="description"
          content="Learn how to build a personal website using Next.js"
        />
        <meta
          property="og:image"
          content={`https://og-image.now.sh/${encodeURI(
            siteTitle
          )}.png?theme=light&md=0&fontSize=75px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fnextjs-black-logo.svg`}
        />
        <meta name="og:title" content={siteTitle} />
        <meta name="twitter:card" content="summary_large_image" />
      </Head>
      
      <main>{children}</main>
      
    </div>
  )
}

File: /frontend\components\layout.module.css
.container {
    max-width: 36rem;
    padding: 0 1rem;
    margin: 3rem auto 6rem;
  }
  
  .header {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .headerImage {
    width: 6rem;
    height: 6rem;
  }
  
  .headerHomeImage {
    width: 8rem;
    height: 8rem;
  }
  
  .backToHome {
    margin: 3rem 0 0;
  }

File: /frontend\lib\posts.js
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import remark from 'remark'
import html from 'remark-html'

const postsDirectory = path.join(process.cwd(), 'posts')

export function getSortedPostsData() {
  // Get file names under /posts
  const fileNames = fs.readdirSync(postsDirectory)
  const allPostsData = fileNames.map(fileName => {
    // Remove ".md" from file name to get id
    const id = fileName.replace(/\.md$/, '')

    // Read markdown file as string
    const fullPath = path.join(postsDirectory, fileName)
    const fileContents = fs.readFileSync(fullPath, 'utf8')

    // Use gray-matter to parse the post metadata section
    const matterResult = matter(fileContents)

    // Combine the data with the id
    return {
      id,
      ...matterResult.data
    }
  })
  // Sort posts by date
  return allPostsData.sort((a, b) => {
    if (a.date < b.date) {
      return 1
    } else {
      return -1
    }
  })
}

export function getAllPostIds() {
  const fileNames = fs.readdirSync(postsDirectory)

  return fileNames.map(fileName => {
    return {
      params: {
        id: fileName.replace(/\.md$/, '')
      }
    }
  })
}

export async function getPostData(id) {
  const fullPath = path.join(postsDirectory, `${id}.md`)
  const fileContents = fs.readFileSync(fullPath, 'utf8')

  // Use gray-matter to parse the post metadata section
  const matterResult = matter(fileContents)

  // Use remark to convert markdown into HTML string
  const processedContent = await remark()
    .use(html)
    .process(matterResult.content)
  const contentHtml = processedContent.toString()

  // Combine the data with the id and contentHtml
  return {
    id,
    contentHtml,
    ...matterResult.data
  }
}

File: /frontend\package-lock.json
{
  "name": "learn-starter",
  "version": "0.1.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "@ampproject/toolbox-core": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/@ampproject/toolbox-core/-/toolbox-core-2.6.0.tgz",
      "integrity": "sha512-sDMnHj8WaX3tqJS5VsIHkeW98nq5WQ0C9RoFc1PPS3rmYIlS0vhAfHbrjJw6wtuxBTQFxccje+Ew+2OJ2D15kA==",
      "requires": {
        "cross-fetch": "3.0.5",
        "lru-cache": "6.0.0"
      }
    },
    "@ampproject/toolbox-optimizer": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/@ampproject/toolbox-optimizer/-/toolbox-optimizer-2.2.0.tgz",
      "integrity": "sha512-lEujArv6jyl/mEab0uBZ25oMkf+kf8cpTuHPcy8k3+jtomNyVtd94lbSWbQtomsEnYQ0MA9MvLvCJXsJz1fQcg==",
      "requires": {
        "@ampproject/toolbox-core": "^2.2.0",
        "@ampproject/toolbox-runtime-version": "^2.2.0",
        "@ampproject/toolbox-script-csp": "^2.2.0",
        "@ampproject/toolbox-validator-rules": "^2.2.0",
        "cssnano": "4.1.10",
        "domhandler": "3.0.0",
        "domutils": "2.0.0",
        "htmlparser2": "4.1.0",
        "normalize-html-whitespace": "1.0.0",
        "postcss-safe-parser": "4.0.2",
        "terser": "4.6.8"
      }
    },
    "@ampproject/toolbox-runtime-version": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/@ampproject/toolbox-runtime-version/-/toolbox-runtime-version-2.6.0.tgz",
      "integrity": "sha512-wT+Ehsoq2PRXqpgjebygHD01BpSlaAE4HfDEVxgPVT8oAsLzE4ywZgzI2VQZfaCdb8qLyO5+WXrLSoJXxDBo2Q==",
      "requires": {
        "@ampproject/toolbox-core": "^2.6.0"
      }
    },
    "@ampproject/toolbox-script-csp": {
      "version": "2.5.4",
      "resolved": "https://registry.npmjs.org/@ampproject/toolbox-script-csp/-/toolbox-script-csp-2.5.4.tgz",
      "integrity": "sha512-+knTYetI5nWllRZ9wFcj7mYxelkiiFVRAAW/hl0ad8EnKHMH82tRlk40CapEnUHhp6Er5sCYkumQ8dngs3Q4zQ=="
    },
    "@ampproject/toolbox-validator-rules": {
      "version": "2.5.4",
      "resolved": "https://registry.npmjs.org/@ampproject/toolbox-validator-rules/-/toolbox-validator-rules-2.5.4.tgz",
      "integrity": "sha512-bS7uF+h0s5aiklc/iRaujiSsiladOsZBLrJ6QImJDXvubCAQtvE7om7ShlGSXixkMAO0OVMDWyuwLlEy8V1Ing==",
      "requires": {
        "cross-fetch": "3.0.5"
      }
    },
    "@babel/code-frame": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.10.4.tgz",
      "integrity": "sha512-vG6SvB6oYEhvgisZNFRmRCUkLz11c7rp+tbNTynGqc6mS1d5ATd/sGyV6W0KZZnXRKMTzZDRgQT3Ou9jhpAfUg==",
      "requires": {
        "@babel/highlight": "^7.10.4"
      }
    },
    "@babel/core": {
      "version": "7.7.2",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.7.2.tgz",
      "integrity": "sha512-eeD7VEZKfhK1KUXGiyPFettgF3m513f8FoBSWiQ1xTvl1RAopLs42Wp9+Ze911I6H0N9lNqJMDgoZT7gHsipeQ==",
      "requires": {
        "@babel/code-frame": "^7.5.5",
        "@babel/generator": "^7.7.2",
        "@babel/helpers": "^7.7.0",
        "@babel/parser": "^7.7.2",
        "@babel/template": "^7.7.0",
        "@babel/traverse": "^7.7.2",
        "@babel/types": "^7.7.2",
        "convert-source-map": "^1.7.0",
        "debug": "^4.1.0",
        "json5": "^2.1.0",
        "lodash": "^4.17.13",
        "resolve": "^1.3.2",
        "semver": "^5.4.1",
        "source-map": "^0.5.0"
      },
      "dependencies": {
        "source-map": {
          "version": "0.5.7",
          "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz",
          "integrity": "sha1-igOdLRAh0i0eoUyA2OpGi6LvP8w="
        }
      }
    },
    "@babel/generator": {
      "version": "7.11.4",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.11.4.tgz",
      "integrity": "sha512-Rn26vueFx0eOoz7iifCN2UHT6rGtnkSGWSoDRIy8jZN3B91PzeSULbswfLoOWuTuAcNwpG/mxy+uCTDnZ9Mp1g==",
      "requires": {
        "@babel/types": "^7.11.0",
        "jsesc": "^2.5.1",
        "source-map": "^0.5.0"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        },
        "source-map": {
          "version": "0.5.7",
          "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz",
          "integrity": "sha1-igOdLRAh0i0eoUyA2OpGi6LvP8w="
        }
      }
    },
    "@babel/helper-annotate-as-pure": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.10.4.tgz",
      "integrity": "sha512-XQlqKQP4vXFB7BN8fEEerrmYvHp3fK/rBkRFz9jaJbzK0B1DSfej9Kc7ZzE8Z/OnId1jpJdNAZ3BFQjWG68rcA==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-builder-binary-assignment-operator-visitor": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-builder-binary-assignment-operator-visitor/-/helper-builder-binary-assignment-operator-visitor-7.10.4.tgz",
      "integrity": "sha512-L0zGlFrGWZK4PbT8AszSfLTM5sDU1+Az/En9VrdT8/LmEiJt4zXt+Jve9DCAnQcbqDhCI+29y/L93mrDzddCcg==",
      "requires": {
        "@babel/helper-explode-assignable-expression": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-builder-react-jsx": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-builder-react-jsx/-/helper-builder-react-jsx-7.10.4.tgz",
      "integrity": "sha512-5nPcIZ7+KKDxT1427oBivl9V9YTal7qk0diccnh7RrcgrT/pGFOjgGw1dgryyx1GvHEpXVfoDF6Ak3rTiWh8Rg==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-builder-react-jsx-experimental": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-builder-react-jsx-experimental/-/helper-builder-react-jsx-experimental-7.10.5.tgz",
      "integrity": "sha512-Buewnx6M4ttG+NLkKyt7baQn7ScC/Td+e99G914fRU8fGIUivDDgVIQeDHFa5e4CRSJQt58WpNHhsAZgtzVhsg==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/helper-module-imports": "^7.10.4",
        "@babel/types": "^7.10.5"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-create-class-features-plugin": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.10.5.tgz",
      "integrity": "sha512-0nkdeijB7VlZoLT3r/mY3bUkw3T8WG/hNw+FATs/6+pG2039IJWjTYL0VTISqsNHMUTEnwbVnc89WIJX9Qed0A==",
      "requires": {
        "@babel/helper-function-name": "^7.10.4",
        "@babel/helper-member-expression-to-functions": "^7.10.5",
        "@babel/helper-optimise-call-expression": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-replace-supers": "^7.10.4",
        "@babel/helper-split-export-declaration": "^7.10.4"
      }
    },
    "@babel/helper-create-regexp-features-plugin": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.10.4.tgz",
      "integrity": "sha512-2/hu58IEPKeoLF45DBwx3XFqsbCXmkdAay4spVr2x0jYgRxrSNp+ePwvSsy9g6YSaNDcKIQVPXk1Ov8S2edk2g==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/helper-regex": "^7.10.4",
        "regexpu-core": "^4.7.0"
      }
    },
    "@babel/helper-define-map": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-define-map/-/helper-define-map-7.10.5.tgz",
      "integrity": "sha512-fMw4kgFB720aQFXSVaXr79pjjcW5puTCM16+rECJ/plGS+zByelE8l9nCpV1GibxTnFVmUuYG9U8wYfQHdzOEQ==",
      "requires": {
        "@babel/helper-function-name": "^7.10.4",
        "@babel/types": "^7.10.5",
        "lodash": "^4.17.19"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-explode-assignable-expression": {
      "version": "7.11.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-explode-assignable-expression/-/helper-explode-assignable-expression-7.11.4.tgz",
      "integrity": "sha512-ux9hm3zR4WV1Y3xXxXkdG/0gxF9nvI0YVmKVhvK9AfMoaQkemL3sJpXw+Xbz65azo8qJiEz2XVDUpK3KYhH3ZQ==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-function-name": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-7.10.4.tgz",
      "integrity": "sha512-YdaSyz1n8gY44EmN7x44zBn9zQ1Ry2Y+3GTA+3vH6Mizke1Vw0aWDM66FOYEPw8//qKkmqOckrGgTYa+6sceqQ==",
      "requires": {
        "@babel/helper-get-function-arity": "^7.10.4",
        "@babel/template": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-get-function-arity": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-get-function-arity/-/helper-get-function-arity-7.10.4.tgz",
      "integrity": "sha512-EkN3YDB+SRDgiIUnNgcmiD361ti+AVbL3f3Henf6dqqUyr5dMsorno0lJWJuLhDhkI5sYEpgj6y9kB8AOU1I2A==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-hoist-variables": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.10.4.tgz",
      "integrity": "sha512-wljroF5PgCk2juF69kanHVs6vrLwIPNp6DLD+Lrl3hoQ3PpPPikaDRNFA+0t81NOoMt2DL6WW/mdU8k4k6ZzuA==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-member-expression-to-functions": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.11.0.tgz",
      "integrity": "sha512-JbFlKHFntRV5qKw3YC0CvQnDZ4XMwgzzBbld7Ly4Mj4cbFy3KywcR8NtNctRToMWJOVvLINJv525Gd6wwVEx/Q==",
      "requires": {
        "@babel/types": "^7.11.0"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-module-imports": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.10.4.tgz",
      "integrity": "sha512-nEQJHqYavI217oD9+s5MUBzk6x1IlvoS9WTPfgG43CbMEeStE0v+r+TucWdx8KFGowPGvyOkDT9+7DHedIDnVw==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-module-transforms": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.11.0.tgz",
      "integrity": "sha512-02EVu8COMuTRO1TAzdMtpBPbe6aQ1w/8fePD2YgQmxZU4gpNWaL9gK3Jp7dxlkUlUCJOTaSeA+Hrm1BRQwqIhg==",
      "requires": {
        "@babel/helper-module-imports": "^7.10.4",
        "@babel/helper-replace-supers": "^7.10.4",
        "@babel/helper-simple-access": "^7.10.4",
        "@babel/helper-split-export-declaration": "^7.11.0",
        "@babel/template": "^7.10.4",
        "@babel/types": "^7.11.0",
        "lodash": "^4.17.19"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-optimise-call-expression": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.10.4.tgz",
      "integrity": "sha512-n3UGKY4VXwXThEiKrgRAoVPBMqeoPgHVqiHZOanAJCG9nQUL2pLRQirUzl0ioKclHGpGqRgIOkgcIJaIWLpygg==",
      "requires": {
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-plugin-utils": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.10.4.tgz",
      "integrity": "sha512-O4KCvQA6lLiMU9l2eawBPMf1xPP8xPfB3iEQw150hOVTqj/rfXz0ThTb4HEzqQfs2Bmo5Ay8BzxfzVtBrr9dVg=="
    },
    "@babel/helper-regex": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-regex/-/helper-regex-7.10.5.tgz",
      "integrity": "sha512-68kdUAzDrljqBrio7DYAEgCoJHxppJOERHOgOrDN7WjOzP0ZQ1LsSDRXcemzVZaLvjaJsJEESb6qt+znNuENDg==",
      "requires": {
        "lodash": "^4.17.19"
      }
    },
    "@babel/helper-remap-async-to-generator": {
      "version": "7.11.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.11.4.tgz",
      "integrity": "sha512-tR5vJ/vBa9wFy3m5LLv2faapJLnDFxNWff2SAYkSE4rLUdbp7CdObYFgI7wK4T/Mj4UzpjPwzR8Pzmr5m7MHGA==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/helper-wrap-function": "^7.10.4",
        "@babel/template": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-replace-supers": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.10.4.tgz",
      "integrity": "sha512-sPxZfFXocEymYTdVK1UNmFPBN+Hv5mJkLPsYWwGBxZAxaWfFu+xqp7b6qWD0yjNuNL2VKc6L5M18tOXUP7NU0A==",
      "requires": {
        "@babel/helper-member-expression-to-functions": "^7.10.4",
        "@babel/helper-optimise-call-expression": "^7.10.4",
        "@babel/traverse": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-simple-access": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.10.4.tgz",
      "integrity": "sha512-0fMy72ej/VEvF8ULmX6yb5MtHG4uH4Dbd6I/aHDb/JVg0bbivwt9Wg+h3uMvX+QSFtwr5MeItvazbrc4jtRAXw==",
      "requires": {
        "@babel/template": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-skip-transparent-expression-wrappers": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.11.0.tgz",
      "integrity": "sha512-0XIdiQln4Elglgjbwo9wuJpL/K7AGCY26kmEt0+pRP0TAj4jjyNq1MjoRvikrTVqKcx4Gysxt4cXvVFXP/JO2Q==",
      "requires": {
        "@babel/types": "^7.11.0"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-split-export-declaration": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.11.0.tgz",
      "integrity": "sha512-74Vejvp6mHkGE+m+k5vHY93FX2cAtrw1zXrZXRlG4l410Nm9PxfEiVTn1PjDPV5SnmieiueY4AFg2xqhNFuuZg==",
      "requires": {
        "@babel/types": "^7.11.0"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helper-validator-identifier": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.10.4.tgz",
      "integrity": "sha512-3U9y+43hz7ZM+rzG24Qe2mufW5KhvFg/NhnNph+i9mgCtdTCtMJuI1TMkrIUiK7Ix4PYlRF9I5dhqaLYA/ADXw=="
    },
    "@babel/helper-wrap-function": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helper-wrap-function/-/helper-wrap-function-7.10.4.tgz",
      "integrity": "sha512-6py45WvEF0MhiLrdxtRjKjufwLL1/ob2qDJgg5JgNdojBAZSAKnAjkyOCNug6n+OBl4VW76XjvgSFTdaMcW0Ug==",
      "requires": {
        "@babel/helper-function-name": "^7.10.4",
        "@babel/template": "^7.10.4",
        "@babel/traverse": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/helpers": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.10.4.tgz",
      "integrity": "sha512-L2gX/XeUONeEbI78dXSrJzGdz4GQ+ZTA/aazfUsFaWjSe95kiCuOZ5HsXvkiw3iwF+mFHSRUfJU8t6YavocdXA==",
      "requires": {
        "@babel/template": "^7.10.4",
        "@babel/traverse": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/highlight": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/highlight/-/highlight-7.10.4.tgz",
      "integrity": "sha512-i6rgnR/YgPEQzZZnbTHHuZdlE8qyoBNalD6F+q4vAFlcMEcqmkoG+mPqJYJCo63qPf74+Y1UZsl3l6f7/RIkmA==",
      "requires": {
        "@babel/helper-validator-identifier": "^7.10.4",
        "chalk": "^2.0.0",
        "js-tokens": "^4.0.0"
      }
    },
    "@babel/parser": {
      "version": "7.11.4",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.11.4.tgz",
      "integrity": "sha512-MggwidiH+E9j5Sh8pbrX5sJvMcsqS5o+7iB42M9/k0CD63MjYbdP4nhSh7uB5wnv2/RVzTZFTxzF/kIa5mrCqA=="
    },
    "@babel/plugin-proposal-async-generator-functions": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-async-generator-functions/-/plugin-proposal-async-generator-functions-7.10.5.tgz",
      "integrity": "sha512-cNMCVezQbrRGvXJwm9fu/1sJj9bHdGAgKodZdLqOQIpfoH3raqmRPBM17+lh7CzhiKRRBrGtZL9WcjxSoGYUSg==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-remap-async-to-generator": "^7.10.4",
        "@babel/plugin-syntax-async-generators": "^7.8.0"
      }
    },
    "@babel/plugin-proposal-class-properties": {
      "version": "7.7.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-class-properties/-/plugin-proposal-class-properties-7.7.0.tgz",
      "integrity": "sha512-tufDcFA1Vj+eWvwHN+jvMN6QsV5o+vUlytNKrbMiCeDL0F2j92RURzUsUMWE5EJkLyWxjdUslCsMQa9FWth16A==",
      "requires": {
        "@babel/helper-create-class-features-plugin": "^7.7.0",
        "@babel/helper-plugin-utils": "^7.0.0"
      }
    },
    "@babel/plugin-proposal-dynamic-import": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-dynamic-import/-/plugin-proposal-dynamic-import-7.10.4.tgz",
      "integrity": "sha512-up6oID1LeidOOASNXgv/CFbgBqTuKJ0cJjz6An5tWD+NVBNlp3VNSBxv2ZdU7SYl3NxJC7agAQDApZusV6uFwQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-dynamic-import": "^7.8.0"
      },
      "dependencies": {
        "@babel/plugin-syntax-dynamic-import": {
          "version": "7.8.3",
          "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.8.3.tgz",
          "integrity": "sha512-5gdGbFon+PszYzqs83S3E5mpi7/y/8M9eC90MRTZfduQOYW76ig6SOSPNe41IG5LoP3FGBn2N0RjVDSQiS94kQ==",
          "requires": {
            "@babel/helper-plugin-utils": "^7.8.0"
          }
        }
      }
    },
    "@babel/plugin-proposal-json-strings": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-json-strings/-/plugin-proposal-json-strings-7.10.4.tgz",
      "integrity": "sha512-fCL7QF0Jo83uy1K0P2YXrfX11tj3lkpN7l4dMv9Y9VkowkhkQDwFHFd8IiwyK5MZjE8UpbgokkgtcReH88Abaw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-json-strings": "^7.8.0"
      }
    },
    "@babel/plugin-proposal-nullish-coalescing-operator": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-nullish-coalescing-operator/-/plugin-proposal-nullish-coalescing-operator-7.7.4.tgz",
      "integrity": "sha512-TbYHmr1Gl1UC7Vo2HVuj/Naci5BEGNZ0AJhzqD2Vpr6QPFWpUmBRLrIDjedzx7/CShq0bRDS2gI4FIs77VHLVQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-syntax-nullish-coalescing-operator": "^7.7.4"
      }
    },
    "@babel/plugin-proposal-numeric-separator": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-numeric-separator/-/plugin-proposal-numeric-separator-7.8.3.tgz",
      "integrity": "sha512-jWioO1s6R/R+wEHizfaScNsAx+xKgwTLNXSh7tTC4Usj3ItsPEhYkEpU4h+lpnBwq7NBVOJXfO6cRFYcX69JUQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.3",
        "@babel/plugin-syntax-numeric-separator": "^7.8.3"
      }
    },
    "@babel/plugin-proposal-object-rest-spread": {
      "version": "7.6.2",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-object-rest-spread/-/plugin-proposal-object-rest-spread-7.6.2.tgz",
      "integrity": "sha512-LDBXlmADCsMZV1Y9OQwMc0MyGZ8Ta/zlD9N67BfQT8uYwkRswiu2hU6nJKrjrt/58aH/vqfQlR/9yId/7A2gWw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-syntax-object-rest-spread": "^7.2.0"
      }
    },
    "@babel/plugin-proposal-optional-catch-binding": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-optional-catch-binding/-/plugin-proposal-optional-catch-binding-7.10.4.tgz",
      "integrity": "sha512-LflT6nPh+GK2MnFiKDyLiqSqVHkQnVf7hdoAvyTnnKj9xB3docGRsdPuxp6qqqW19ifK3xgc9U5/FwrSaCNX5g==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-optional-catch-binding": "^7.8.0"
      }
    },
    "@babel/plugin-proposal-optional-chaining": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-optional-chaining/-/plugin-proposal-optional-chaining-7.7.4.tgz",
      "integrity": "sha512-JmgaS+ygAWDR/STPe3/7y0lNlHgS+19qZ9aC06nYLwQ/XB7c0q5Xs+ksFU3EDnp9EiEsO0dnRAOKeyLHTZuW3A==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-syntax-optional-chaining": "^7.7.4"
      }
    },
    "@babel/plugin-proposal-unicode-property-regex": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-proposal-unicode-property-regex/-/plugin-proposal-unicode-property-regex-7.10.4.tgz",
      "integrity": "sha512-H+3fOgPnEXFL9zGYtKQe4IDOPKYlZdF1kqFDQRRb8PK4B8af1vAGK04tF5iQAAsui+mHNBQSAtd2/ndEDe9wuA==",
      "requires": {
        "@babel/helper-create-regexp-features-plugin": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-syntax-async-generators": {
      "version": "7.8.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz",
      "integrity": "sha512-tycmZxkGfZaxhMRbXlPXuVFpdWlXpir2W4AMhSJgRKzk/eDlIXOhb2LHWoLpDF7TEHylV5zNhykX6KAgHJmTNw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-bigint": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-bigint/-/plugin-syntax-bigint-7.8.3.tgz",
      "integrity": "sha512-wnTnFlG+YxQm3vDxpGE57Pj0srRU4sHE/mDkt1qv2YJJSeUAec2ma4WLUnUPeKjyrfntVwe/N6dCXpU+zL3Npg==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-dynamic-import": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.2.0.tgz",
      "integrity": "sha512-mVxuJ0YroI/h/tbFTPGZR8cv6ai+STMKNBq0f8hFxsxWjl94qqhsb+wXbpNMDPU3cfR1TIsVFzU3nXyZMqyK4w==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0"
      }
    },
    "@babel/plugin-syntax-json-strings": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-json-strings/-/plugin-syntax-json-strings-7.8.3.tgz",
      "integrity": "sha512-lY6kdGpWHvjoe2vk4WrAapEuBR69EMxZl+RoGRhrFGNYVK8mOPAW8VfbT/ZgrFbXlDNiiaxQnAtgVCZ6jv30EA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-jsx": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.10.4.tgz",
      "integrity": "sha512-KCg9mio9jwiARCB7WAcQ7Y1q+qicILjoK8LP/VkPkEKaf5dkaZZK1EcTe91a3JJlZ3qy6L5s9X52boEYi8DM9g==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-syntax-nullish-coalescing-operator": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-nullish-coalescing-operator/-/plugin-syntax-nullish-coalescing-operator-7.8.3.tgz",
      "integrity": "sha512-aSff4zPII1u2QD7y+F8oDsz19ew4IGEJg9SVW+bqwpwtfFleiQDMdzA/R+UlWDzfnHFCxxleFT0PMIrR36XLNQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-numeric-separator": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-numeric-separator/-/plugin-syntax-numeric-separator-7.10.4.tgz",
      "integrity": "sha512-9H6YdfkcK/uOnY/K7/aA2xpzaAgkQn37yzWUMRK7OaPOqOpGS1+n0H5hxT9AUw9EsSjPW8SVyMJwYRtWs3X3ug==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-syntax-object-rest-spread": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-object-rest-spread/-/plugin-syntax-object-rest-spread-7.8.3.tgz",
      "integrity": "sha512-XoqMijGZb9y3y2XskN+P1wUGiVwWZ5JmoDRwx5+3GmEplNyVM2s2Dg8ILFQm8rWM48orGy5YpI5Bl8U1y7ydlA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-optional-catch-binding": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-optional-catch-binding/-/plugin-syntax-optional-catch-binding-7.8.3.tgz",
      "integrity": "sha512-6VPD0Pc1lpTqw0aKoeRTMiB+kWhAoT24PA+ksWSBrFtl5SIRVpZlwN3NNPQjehA2E/91FV3RjLWoVTglWcSV3Q==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-optional-chaining": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-optional-chaining/-/plugin-syntax-optional-chaining-7.8.3.tgz",
      "integrity": "sha512-KoK9ErH1MBlCPxV0VANkXW2/dw4vlbGDrFgz8bmUsBGYkFRcbRwMh6cIJubdPrkxRwuGdtCk0v/wPTKbQgBjkg==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.8.0"
      }
    },
    "@babel/plugin-syntax-top-level-await": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-top-level-await/-/plugin-syntax-top-level-await-7.10.4.tgz",
      "integrity": "sha512-ni1brg4lXEmWyafKr0ccFWkJG0CeMt4WV1oyeBW6EFObF4oOHclbkj5cARxAPQyAQ2UTuplJyK4nfkXIMMFvsQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-syntax-typescript": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-typescript/-/plugin-syntax-typescript-7.10.4.tgz",
      "integrity": "sha512-oSAEz1YkBCAKr5Yiq8/BNtvSAPwkp/IyUnwZogd8p+F0RuYQQrLeRUzIQhueQTTBy/F+a40uS7OFKxnkRvmvFQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-arrow-functions": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-arrow-functions/-/plugin-transform-arrow-functions-7.10.4.tgz",
      "integrity": "sha512-9J/oD1jV0ZCBcgnoFWFq1vJd4msoKb/TCpGNFyyLt0zABdcvgK3aYikZ8HjzB14c26bc7E3Q1yugpwGy2aTPNA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-async-to-generator": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-async-to-generator/-/plugin-transform-async-to-generator-7.10.4.tgz",
      "integrity": "sha512-F6nREOan7J5UXTLsDsZG3DXmZSVofr2tGNwfdrVwkDWHfQckbQXnXSPfD7iO+c/2HGqycwyLST3DnZ16n+cBJQ==",
      "requires": {
        "@babel/helper-module-imports": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-remap-async-to-generator": "^7.10.4"
      }
    },
    "@babel/plugin-transform-block-scoped-functions": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-block-scoped-functions/-/plugin-transform-block-scoped-functions-7.10.4.tgz",
      "integrity": "sha512-WzXDarQXYYfjaV1szJvN3AD7rZgZzC1JtjJZ8dMHUyiK8mxPRahynp14zzNjU3VkPqPsO38CzxiWO1c9ARZ8JA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-block-scoping": {
      "version": "7.11.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-block-scoping/-/plugin-transform-block-scoping-7.11.1.tgz",
      "integrity": "sha512-00dYeDE0EVEHuuM+26+0w/SCL0BH2Qy7LwHuI4Hi4MH5gkC8/AqMN5uWFJIsoXZrAphiMm1iXzBw6L2T+eA0ew==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-classes": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-classes/-/plugin-transform-classes-7.10.4.tgz",
      "integrity": "sha512-2oZ9qLjt161dn1ZE0Ms66xBncQH4In8Sqw1YWgBUZuGVJJS5c0OFZXL6dP2MRHrkU/eKhWg8CzFJhRQl50rQxA==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/helper-define-map": "^7.10.4",
        "@babel/helper-function-name": "^7.10.4",
        "@babel/helper-optimise-call-expression": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-replace-supers": "^7.10.4",
        "@babel/helper-split-export-declaration": "^7.10.4",
        "globals": "^11.1.0"
      }
    },
    "@babel/plugin-transform-computed-properties": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-computed-properties/-/plugin-transform-computed-properties-7.10.4.tgz",
      "integrity": "sha512-JFwVDXcP/hM/TbyzGq3l/XWGut7p46Z3QvqFMXTfk6/09m7xZHJUN9xHfsv7vqqD4YnfI5ueYdSJtXqqBLyjBw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-destructuring": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-destructuring/-/plugin-transform-destructuring-7.10.4.tgz",
      "integrity": "sha512-+WmfvyfsyF603iPa6825mq6Qrb7uLjTOsa3XOFzlYcYDHSS4QmpOWOL0NNBY5qMbvrcf3tq0Cw+v4lxswOBpgA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-dotall-regex": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.10.4.tgz",
      "integrity": "sha512-ZEAVvUTCMlMFAbASYSVQoxIbHm2OkG2MseW6bV2JjIygOjdVv8tuxrCTzj1+Rynh7ODb8GivUy7dzEXzEhuPaA==",
      "requires": {
        "@babel/helper-create-regexp-features-plugin": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-duplicate-keys": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-duplicate-keys/-/plugin-transform-duplicate-keys-7.10.4.tgz",
      "integrity": "sha512-GL0/fJnmgMclHiBTTWXNlYjYsA7rDrtsazHG6mglaGSTh0KsrW04qml+Bbz9FL0LcJIRwBWL5ZqlNHKTkU3xAA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-exponentiation-operator": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-exponentiation-operator/-/plugin-transform-exponentiation-operator-7.10.4.tgz",
      "integrity": "sha512-S5HgLVgkBcRdyQAHbKj+7KyuWx8C6t5oETmUuwz1pt3WTWJhsUV0WIIXuVvfXMxl/QQyHKlSCNNtaIamG8fysw==",
      "requires": {
        "@babel/helper-builder-binary-assignment-operator-visitor": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-for-of": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-for-of/-/plugin-transform-for-of-7.10.4.tgz",
      "integrity": "sha512-ItdQfAzu9AlEqmusA/65TqJ79eRcgGmpPPFvBnGILXZH975G0LNjP1yjHvGgfuCxqrPPueXOPe+FsvxmxKiHHQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-function-name": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-function-name/-/plugin-transform-function-name-7.10.4.tgz",
      "integrity": "sha512-OcDCq2y5+E0dVD5MagT5X+yTRbcvFjDI2ZVAottGH6tzqjx/LKpgkUepu3hp/u4tZBzxxpNGwLsAvGBvQ2mJzg==",
      "requires": {
        "@babel/helper-function-name": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-literals": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-literals/-/plugin-transform-literals-7.10.4.tgz",
      "integrity": "sha512-Xd/dFSTEVuUWnyZiMu76/InZxLTYilOSr1UlHV+p115Z/Le2Fi1KXkJUYz0b42DfndostYlPub3m8ZTQlMaiqQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-member-expression-literals": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-member-expression-literals/-/plugin-transform-member-expression-literals-7.10.4.tgz",
      "integrity": "sha512-0bFOvPyAoTBhtcJLr9VcwZqKmSjFml1iVxvPL0ReomGU53CX53HsM4h2SzckNdkQcHox1bpAqzxBI1Y09LlBSw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-modules-amd": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.10.5.tgz",
      "integrity": "sha512-elm5uruNio7CTLFItVC/rIzKLfQ17+fX7EVz5W0TMgIHFo1zY0Ozzx+lgwhL4plzl8OzVn6Qasx5DeEFyoNiRw==",
      "requires": {
        "@babel/helper-module-transforms": "^7.10.5",
        "@babel/helper-plugin-utils": "^7.10.4",
        "babel-plugin-dynamic-import-node": "^2.3.3"
      }
    },
    "@babel/plugin-transform-modules-commonjs": {
      "version": "7.7.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.7.0.tgz",
      "integrity": "sha512-KEMyWNNWnjOom8vR/1+d+Ocz/mILZG/eyHHO06OuBQ2aNhxT62fr4y6fGOplRx+CxCSp3IFwesL8WdINfY/3kg==",
      "requires": {
        "@babel/helper-module-transforms": "^7.7.0",
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/helper-simple-access": "^7.7.0",
        "babel-plugin-dynamic-import-node": "^2.3.0"
      }
    },
    "@babel/plugin-transform-modules-systemjs": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.10.5.tgz",
      "integrity": "sha512-f4RLO/OL14/FP1AEbcsWMzpbUz6tssRaeQg11RH1BP/XnPpRoVwgeYViMFacnkaw4k4wjRSjn3ip1Uw9TaXuMw==",
      "requires": {
        "@babel/helper-hoist-variables": "^7.10.4",
        "@babel/helper-module-transforms": "^7.10.5",
        "@babel/helper-plugin-utils": "^7.10.4",
        "babel-plugin-dynamic-import-node": "^2.3.3"
      }
    },
    "@babel/plugin-transform-modules-umd": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-modules-umd/-/plugin-transform-modules-umd-7.10.4.tgz",
      "integrity": "sha512-mohW5q3uAEt8T45YT7Qc5ws6mWgJAaL/8BfWD9Dodo1A3RKWli8wTS+WiQ/knF+tXlPirW/1/MqzzGfCExKECA==",
      "requires": {
        "@babel/helper-module-transforms": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-named-capturing-groups-regex": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-named-capturing-groups-regex/-/plugin-transform-named-capturing-groups-regex-7.10.4.tgz",
      "integrity": "sha512-V6LuOnD31kTkxQPhKiVYzYC/Jgdq53irJC/xBSmqcNcqFGV+PER4l6rU5SH2Vl7bH9mLDHcc0+l9HUOe4RNGKA==",
      "requires": {
        "@babel/helper-create-regexp-features-plugin": "^7.10.4"
      }
    },
    "@babel/plugin-transform-new-target": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-new-target/-/plugin-transform-new-target-7.10.4.tgz",
      "integrity": "sha512-YXwWUDAH/J6dlfwqlWsztI2Puz1NtUAubXhOPLQ5gjR/qmQ5U96DY4FQO8At33JN4XPBhrjB8I4eMmLROjjLjw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-object-super": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-object-super/-/plugin-transform-object-super-7.10.4.tgz",
      "integrity": "sha512-5iTw0JkdRdJvr7sY0vHqTpnruUpTea32JHmq/atIWqsnNussbRzjEDyWep8UNztt1B5IusBYg8Irb0bLbiEBCQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-replace-supers": "^7.10.4"
      }
    },
    "@babel/plugin-transform-parameters": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-parameters/-/plugin-transform-parameters-7.10.5.tgz",
      "integrity": "sha512-xPHwUj5RdFV8l1wuYiu5S9fqWGM2DrYc24TMvUiRrPVm+SM3XeqU9BcokQX/kEUe+p2RBwy+yoiR1w/Blq6ubw==",
      "requires": {
        "@babel/helper-get-function-arity": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-property-literals": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-property-literals/-/plugin-transform-property-literals-7.10.4.tgz",
      "integrity": "sha512-ofsAcKiUxQ8TY4sScgsGeR2vJIsfrzqvFb9GvJ5UdXDzl+MyYCaBj/FGzXuv7qE0aJcjWMILny1epqelnFlz8g==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-react-display-name": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-display-name/-/plugin-transform-react-display-name-7.10.4.tgz",
      "integrity": "sha512-Zd4X54Mu9SBfPGnEcaGcOrVAYOtjT2on8QZkLKEq1S/tHexG39d9XXGZv19VfRrDjPJzFmPfTAqOQS1pfFOujw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-react-jsx": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx/-/plugin-transform-react-jsx-7.10.4.tgz",
      "integrity": "sha512-L+MfRhWjX0eI7Js093MM6MacKU4M6dnCRa/QPDwYMxjljzSCzzlzKzj9Pk4P3OtrPcxr2N3znR419nr3Xw+65A==",
      "requires": {
        "@babel/helper-builder-react-jsx": "^7.10.4",
        "@babel/helper-builder-react-jsx-experimental": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-jsx": "^7.10.4"
      }
    },
    "@babel/plugin-transform-react-jsx-self": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.10.4.tgz",
      "integrity": "sha512-yOvxY2pDiVJi0axdTWHSMi5T0DILN+H+SaeJeACHKjQLezEzhLx9nEF9xgpBLPtkZsks9cnb5P9iBEi21En3gg==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-jsx": "^7.10.4"
      }
    },
    "@babel/plugin-transform-react-jsx-source": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.10.5.tgz",
      "integrity": "sha512-wTeqHVkN1lfPLubRiZH3o73f4rfon42HpgxUSs86Nc+8QIcm/B9s8NNVXu/gwGcOyd7yDib9ikxoDLxJP0UiDA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-jsx": "^7.10.4"
      }
    },
    "@babel/plugin-transform-regenerator": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-regenerator/-/plugin-transform-regenerator-7.10.4.tgz",
      "integrity": "sha512-3thAHwtor39A7C04XucbMg17RcZ3Qppfxr22wYzZNcVIkPHfpM9J0SO8zuCV6SZa265kxBJSrfKTvDCYqBFXGw==",
      "requires": {
        "regenerator-transform": "^0.14.2"
      }
    },
    "@babel/plugin-transform-reserved-words": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-reserved-words/-/plugin-transform-reserved-words-7.10.4.tgz",
      "integrity": "sha512-hGsw1O6Rew1fkFbDImZIEqA8GoidwTAilwCyWqLBM9f+e/u/sQMQu7uX6dyokfOayRuuVfKOW4O7HvaBWM+JlQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-runtime": {
      "version": "7.6.2",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-runtime/-/plugin-transform-runtime-7.6.2.tgz",
      "integrity": "sha512-cqULw/QB4yl73cS5Y0TZlQSjDvNkzDbu0FurTZyHlJpWE5T3PCMdnyV+xXoH1opr1ldyHODe3QAX3OMAii5NxA==",
      "requires": {
        "@babel/helper-module-imports": "^7.0.0",
        "@babel/helper-plugin-utils": "^7.0.0",
        "resolve": "^1.8.1",
        "semver": "^5.5.1"
      }
    },
    "@babel/plugin-transform-shorthand-properties": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-shorthand-properties/-/plugin-transform-shorthand-properties-7.10.4.tgz",
      "integrity": "sha512-AC2K/t7o07KeTIxMoHneyX90v3zkm5cjHJEokrPEAGEy3UCp8sLKfnfOIGdZ194fyN4wfX/zZUWT9trJZ0qc+Q==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-spread": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-spread/-/plugin-transform-spread-7.11.0.tgz",
      "integrity": "sha512-UwQYGOqIdQJe4aWNyS7noqAnN2VbaczPLiEtln+zPowRNlD+79w3oi2TWfYe0eZgd+gjZCbsydN7lzWysDt+gw==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-skip-transparent-expression-wrappers": "^7.11.0"
      }
    },
    "@babel/plugin-transform-sticky-regex": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-sticky-regex/-/plugin-transform-sticky-regex-7.10.4.tgz",
      "integrity": "sha512-Ddy3QZfIbEV0VYcVtFDCjeE4xwVTJWTmUtorAJkn6u/92Z/nWJNV+mILyqHKrUxXYKA2EoCilgoPePymKL4DvQ==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/helper-regex": "^7.10.4"
      }
    },
    "@babel/plugin-transform-template-literals": {
      "version": "7.10.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-template-literals/-/plugin-transform-template-literals-7.10.5.tgz",
      "integrity": "sha512-V/lnPGIb+KT12OQikDvgSuesRX14ck5FfJXt6+tXhdkJ+Vsd0lDCVtF6jcB4rNClYFzaB2jusZ+lNISDk2mMMw==",
      "requires": {
        "@babel/helper-annotate-as-pure": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-typeof-symbol": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-typeof-symbol/-/plugin-transform-typeof-symbol-7.10.4.tgz",
      "integrity": "sha512-QqNgYwuuW0y0H+kUE/GWSR45t/ccRhe14Fs/4ZRouNNQsyd4o3PG4OtHiIrepbM2WKUBDAXKCAK/Lk4VhzTaGA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/plugin-transform-typescript": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-typescript/-/plugin-transform-typescript-7.11.0.tgz",
      "integrity": "sha512-edJsNzTtvb3MaXQwj8403B7mZoGu9ElDJQZOKjGUnvilquxBA3IQoEIOvkX/1O8xfAsnHS/oQhe2w/IXrr+w0w==",
      "requires": {
        "@babel/helper-create-class-features-plugin": "^7.10.5",
        "@babel/helper-plugin-utils": "^7.10.4",
        "@babel/plugin-syntax-typescript": "^7.10.4"
      }
    },
    "@babel/plugin-transform-unicode-regex": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-unicode-regex/-/plugin-transform-unicode-regex-7.10.4.tgz",
      "integrity": "sha512-wNfsc4s8N2qnIwpO/WP2ZiSyjfpTamT2C9V9FDH/Ljub9zw6P3SjkXcFmc0RQUt96k2fmIvtla2MMjgTwIAC+A==",
      "requires": {
        "@babel/helper-create-regexp-features-plugin": "^7.10.4",
        "@babel/helper-plugin-utils": "^7.10.4"
      }
    },
    "@babel/preset-env": {
      "version": "7.7.1",
      "resolved": "https://registry.npmjs.org/@babel/preset-env/-/preset-env-7.7.1.tgz",
      "integrity": "sha512-/93SWhi3PxcVTDpSqC+Dp4YxUu3qZ4m7I76k0w73wYfn7bGVuRIO4QUz95aJksbS+AD1/mT1Ie7rbkT0wSplaA==",
      "requires": {
        "@babel/helper-module-imports": "^7.7.0",
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-proposal-async-generator-functions": "^7.7.0",
        "@babel/plugin-proposal-dynamic-import": "^7.7.0",
        "@babel/plugin-proposal-json-strings": "^7.2.0",
        "@babel/plugin-proposal-object-rest-spread": "^7.6.2",
        "@babel/plugin-proposal-optional-catch-binding": "^7.2.0",
        "@babel/plugin-proposal-unicode-property-regex": "^7.7.0",
        "@babel/plugin-syntax-async-generators": "^7.2.0",
        "@babel/plugin-syntax-dynamic-import": "^7.2.0",
        "@babel/plugin-syntax-json-strings": "^7.2.0",
        "@babel/plugin-syntax-object-rest-spread": "^7.2.0",
        "@babel/plugin-syntax-optional-catch-binding": "^7.2.0",
        "@babel/plugin-syntax-top-level-await": "^7.7.0",
        "@babel/plugin-transform-arrow-functions": "^7.2.0",
        "@babel/plugin-transform-async-to-generator": "^7.7.0",
        "@babel/plugin-transform-block-scoped-functions": "^7.2.0",
        "@babel/plugin-transform-block-scoping": "^7.6.3",
        "@babel/plugin-transform-classes": "^7.7.0",
        "@babel/plugin-transform-computed-properties": "^7.2.0",
        "@babel/plugin-transform-destructuring": "^7.6.0",
        "@babel/plugin-transform-dotall-regex": "^7.7.0",
        "@babel/plugin-transform-duplicate-keys": "^7.5.0",
        "@babel/plugin-transform-exponentiation-operator": "^7.2.0",
        "@babel/plugin-transform-for-of": "^7.4.4",
        "@babel/plugin-transform-function-name": "^7.7.0",
        "@babel/plugin-transform-literals": "^7.2.0",
        "@babel/plugin-transform-member-expression-literals": "^7.2.0",
        "@babel/plugin-transform-modules-amd": "^7.5.0",
        "@babel/plugin-transform-modules-commonjs": "^7.7.0",
        "@babel/plugin-transform-modules-systemjs": "^7.7.0",
        "@babel/plugin-transform-modules-umd": "^7.7.0",
        "@babel/plugin-transform-named-capturing-groups-regex": "^7.7.0",
        "@babel/plugin-transform-new-target": "^7.4.4",
        "@babel/plugin-transform-object-super": "^7.5.5",
        "@babel/plugin-transform-parameters": "^7.4.4",
        "@babel/plugin-transform-property-literals": "^7.2.0",
        "@babel/plugin-transform-regenerator": "^7.7.0",
        "@babel/plugin-transform-reserved-words": "^7.2.0",
        "@babel/plugin-transform-shorthand-properties": "^7.2.0",
        "@babel/plugin-transform-spread": "^7.6.2",
        "@babel/plugin-transform-sticky-regex": "^7.2.0",
        "@babel/plugin-transform-template-literals": "^7.4.4",
        "@babel/plugin-transform-typeof-symbol": "^7.2.0",
        "@babel/plugin-transform-unicode-regex": "^7.7.0",
        "@babel/types": "^7.7.1",
        "browserslist": "^4.6.0",
        "core-js-compat": "^3.1.1",
        "invariant": "^2.2.2",
        "js-levenshtein": "^1.1.3",
        "semver": "^5.5.0"
      }
    },
    "@babel/preset-modules": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/@babel/preset-modules/-/preset-modules-0.1.1.tgz",
      "integrity": "sha512-x/kt2aAZlgcFnP3P851fkkb2s4FmTiyGic58pkWMaRK9Am3u9KkH1ttHGjwlsKu7/TVJsLEBXZnjUxqsid3tww==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-proposal-unicode-property-regex": "^7.4.4",
        "@babel/plugin-transform-dotall-regex": "^7.4.4",
        "@babel/types": "^7.4.4",
        "esutils": "^2.0.2"
      }
    },
    "@babel/preset-react": {
      "version": "7.7.0",
      "resolved": "https://registry.npmjs.org/@babel/preset-react/-/preset-react-7.7.0.tgz",
      "integrity": "sha512-IXXgSUYBPHUGhUkH+89TR6faMcBtuMW0h5OHbMuVbL3/5wK2g6a2M2BBpkLa+Kw0sAHiZ9dNVgqJMDP/O4GRBA==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-transform-react-display-name": "^7.0.0",
        "@babel/plugin-transform-react-jsx": "^7.7.0",
        "@babel/plugin-transform-react-jsx-self": "^7.0.0",
        "@babel/plugin-transform-react-jsx-source": "^7.0.0"
      }
    },
    "@babel/preset-typescript": {
      "version": "7.7.2",
      "resolved": "https://registry.npmjs.org/@babel/preset-typescript/-/preset-typescript-7.7.2.tgz",
      "integrity": "sha512-1B4HthAelaLGfNRyrWqJtBEjXX1ulThCrLQ5B2VOtEAznWFIFXFJahgXImqppy66lx/Oh+cOSCQdJzZqh2Jh5g==",
      "requires": {
        "@babel/helper-plugin-utils": "^7.0.0",
        "@babel/plugin-transform-typescript": "^7.7.2"
      }
    },
    "@babel/runtime": {
      "version": "7.7.2",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.7.2.tgz",
      "integrity": "sha512-JONRbXbTXc9WQE2mAZd1p0Z3DZ/6vaQIkgYMSTP3KjRCyd7rCZCcfhCyX+YjwcKxcZ82UrxbRD358bpExNgrjw==",
      "requires": {
        "regenerator-runtime": "^0.13.2"
      }
    },
    "@babel/template": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.10.4.tgz",
      "integrity": "sha512-ZCjD27cGJFUB6nmCB1Enki3r+L5kJveX9pq1SvAUKoICy6CZ9yD8xO086YXdYhvNjBdnekm4ZnaP5yC8Cs/1tA==",
      "requires": {
        "@babel/code-frame": "^7.10.4",
        "@babel/parser": "^7.10.4",
        "@babel/types": "^7.10.4"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/traverse": {
      "version": "7.11.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.11.0.tgz",
      "integrity": "sha512-ZB2V+LskoWKNpMq6E5UUCrjtDUh5IOTAyIl0dTjIEoXum/iKWkoIEKIRDnUucO6f+2FzNkE0oD4RLKoPIufDtg==",
      "requires": {
        "@babel/code-frame": "^7.10.4",
        "@babel/generator": "^7.11.0",
        "@babel/helper-function-name": "^7.10.4",
        "@babel/helper-split-export-declaration": "^7.11.0",
        "@babel/parser": "^7.11.0",
        "@babel/types": "^7.11.0",
        "debug": "^4.1.0",
        "globals": "^11.1.0",
        "lodash": "^4.17.19"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.11.0",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz",
          "integrity": "sha512-O53yME4ZZI0jO1EVGtF1ePGl0LHirG4P1ibcD80XyzZcKhcMFeCXmh4Xb1ifGBIV233Qg12x4rBfQgA+tmOukA==",
          "requires": {
            "@babel/helper-validator-identifier": "^7.10.4",
            "lodash": "^4.17.19",
            "to-fast-properties": "^2.0.0"
          }
        }
      }
    },
    "@babel/types": {
      "version": "7.7.4",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.7.4.tgz",
      "integrity": "sha512-cz5Ji23KCi4T+YIE/BolWosrJuSmoZeN1EFnRtBwF+KKLi8GG/Z2c2hOJJeCXPk4mwk4QFvTmwIodJowXgttRA==",
      "requires": {
        "esutils": "^2.0.2",
        "lodash": "^4.17.13",
        "to-fast-properties": "^2.0.0"
      }
    },
    "@types/json-schema": {
      "version": "7.0.5",
      "resolved": "https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.5.tgz",
      "integrity": "sha512-7+2BITlgjgDhH0vvwZU/HZJVyk+2XUlvxXe8dFMedNX/aMkaOq++rMAFXc0tM7ij15QaWlbdQASBR9dihi+bDQ=="
    },
    "@types/mdast": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/@types/mdast/-/mdast-3.0.3.tgz",
      "integrity": "sha512-SXPBMnFVQg1s00dlMCc/jCdvPqdE4mXaMMCeRlxLDmTAEoegHT53xKtkDnzDTOcmMHUfcjyf36/YYZ6SxRdnsw==",
      "requires": {
        "@types/unist": "*"
      }
    },
    "@types/q": {
      "version": "1.5.4",
      "resolved": "https://registry.npmjs.org/@types/q/-/q-1.5.4.tgz",
      "integrity": "sha512-1HcDas8SEj4z1Wc696tH56G8OlRaH/sqZOynNNB+HF0WOeXPaxTtbYzJY2oEfiUxjSKjhCKr+MvR7dCHcEelug=="
    },
    "@types/unist": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/@types/unist/-/unist-2.0.3.tgz",
      "integrity": "sha512-FvUupuM3rlRsRtCN+fDudtmytGO6iHJuuRKS1Ss0pG5z8oX0diNEw94UEL7hgDbpN94rgaK5R7sWm6RrSkZuAQ=="
    },
    "@webassemblyjs/ast": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/ast/-/ast-1.9.0.tgz",
      "integrity": "sha512-C6wW5L+b7ogSDVqymbkkvuW9kruN//YisMED04xzeBBqjHa2FYnmvOlS6Xj68xWQRgWvI9cIglsjFowH/RJyEA==",
      "requires": {
        "@webassemblyjs/helper-module-context": "1.9.0",
        "@webassemblyjs/helper-wasm-bytecode": "1.9.0",
        "@webassemblyjs/wast-parser": "1.9.0"
      }
    },
    "@webassemblyjs/floating-point-hex-parser": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/floating-point-hex-parser/-/floating-point-hex-parser-1.9.0.tgz",
      "integrity": "sha512-TG5qcFsS8QB4g4MhrxK5TqfdNe7Ey/7YL/xN+36rRjl/BlGE/NcBvJcqsRgCP6Z92mRE+7N50pRIi8SmKUbcQA=="
    },
    "@webassemblyjs/helper-api-error": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-api-error/-/helper-api-error-1.9.0.tgz",
      "integrity": "sha512-NcMLjoFMXpsASZFxJ5h2HZRcEhDkvnNFOAKneP5RbKRzaWJN36NC4jqQHKwStIhGXu5mUWlUUk7ygdtrO8lbmw=="
    },
    "@webassemblyjs/helper-buffer": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-buffer/-/helper-buffer-1.9.0.tgz",
      "integrity": "sha512-qZol43oqhq6yBPx7YM3m9Bv7WMV9Eevj6kMi6InKOuZxhw+q9hOkvq5e/PpKSiLfyetpaBnogSbNCfBwyB00CA=="
    },
    "@webassemblyjs/helper-code-frame": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-code-frame/-/helper-code-frame-1.9.0.tgz",
      "integrity": "sha512-ERCYdJBkD9Vu4vtjUYe8LZruWuNIToYq/ME22igL+2vj2dQ2OOujIZr3MEFvfEaqKoVqpsFKAGsRdBSBjrIvZA==",
      "requires": {
        "@webassemblyjs/wast-printer": "1.9.0"
      }
    },
    "@webassemblyjs/helper-fsm": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-fsm/-/helper-fsm-1.9.0.tgz",
      "integrity": "sha512-OPRowhGbshCb5PxJ8LocpdX9Kl0uB4XsAjl6jH/dWKlk/mzsANvhwbiULsaiqT5GZGT9qinTICdj6PLuM5gslw=="
    },
    "@webassemblyjs/helper-module-context": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-module-context/-/helper-module-context-1.9.0.tgz",
      "integrity": "sha512-MJCW8iGC08tMk2enck1aPW+BE5Cw8/7ph/VGZxwyvGbJwjktKkDK7vy7gAmMDx88D7mhDTCNKAW5tED+gZ0W8g==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0"
      }
    },
    "@webassemblyjs/helper-wasm-bytecode": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-wasm-bytecode/-/helper-wasm-bytecode-1.9.0.tgz",
      "integrity": "sha512-R7FStIzyNcd7xKxCZH5lE0Bqy+hGTwS3LJjuv1ZVxd9O7eHCedSdrId/hMOd20I+v8wDXEn+bjfKDLzTepoaUw=="
    },
    "@webassemblyjs/helper-wasm-section": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/helper-wasm-section/-/helper-wasm-section-1.9.0.tgz",
      "integrity": "sha512-XnMB8l3ek4tvrKUUku+IVaXNHz2YsJyOOmz+MMkZvh8h1uSJpSen6vYnw3IoQ7WwEuAhL8Efjms1ZWjqh2agvw==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-buffer": "1.9.0",
        "@webassemblyjs/helper-wasm-bytecode": "1.9.0",
        "@webassemblyjs/wasm-gen": "1.9.0"
      }
    },
    "@webassemblyjs/ieee754": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/ieee754/-/ieee754-1.9.0.tgz",
      "integrity": "sha512-dcX8JuYU/gvymzIHc9DgxTzUUTLexWwt8uCTWP3otys596io0L5aW02Gb1RjYpx2+0Jus1h4ZFqjla7umFniTg==",
      "requires": {
        "@xtuc/ieee754": "^1.2.0"
      }
    },
    "@webassemblyjs/leb128": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/leb128/-/leb128-1.9.0.tgz",
      "integrity": "sha512-ENVzM5VwV1ojs9jam6vPys97B/S65YQtv/aanqnU7D8aSoHFX8GyhGg0CMfyKNIHBuAVjy3tlzd5QMMINa7wpw==",
      "requires": {
        "@xtuc/long": "4.2.2"
      }
    },
    "@webassemblyjs/utf8": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/utf8/-/utf8-1.9.0.tgz",
      "integrity": "sha512-GZbQlWtopBTP0u7cHrEx+73yZKrQoBMpwkGEIqlacljhXCkVM1kMQge/Mf+csMJAjEdSwhOyLAS0AoR3AG5P8w=="
    },
    "@webassemblyjs/wasm-edit": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wasm-edit/-/wasm-edit-1.9.0.tgz",
      "integrity": "sha512-FgHzBm80uwz5M8WKnMTn6j/sVbqilPdQXTWraSjBwFXSYGirpkSWE2R9Qvz9tNiTKQvoKILpCuTjBKzOIm0nxw==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-buffer": "1.9.0",
        "@webassemblyjs/helper-wasm-bytecode": "1.9.0",
        "@webassemblyjs/helper-wasm-section": "1.9.0",
        "@webassemblyjs/wasm-gen": "1.9.0",
        "@webassemblyjs/wasm-opt": "1.9.0",
        "@webassemblyjs/wasm-parser": "1.9.0",
        "@webassemblyjs/wast-printer": "1.9.0"
      }
    },
    "@webassemblyjs/wasm-gen": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wasm-gen/-/wasm-gen-1.9.0.tgz",
      "integrity": "sha512-cPE3o44YzOOHvlsb4+E9qSqjc9Qf9Na1OO/BHFy4OI91XDE14MjFN4lTMezzaIWdPqHnsTodGGNP+iRSYfGkjA==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-wasm-bytecode": "1.9.0",
        "@webassemblyjs/ieee754": "1.9.0",
        "@webassemblyjs/leb128": "1.9.0",
        "@webassemblyjs/utf8": "1.9.0"
      }
    },
    "@webassemblyjs/wasm-opt": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wasm-opt/-/wasm-opt-1.9.0.tgz",
      "integrity": "sha512-Qkjgm6Anhm+OMbIL0iokO7meajkzQD71ioelnfPEj6r4eOFuqm4YC3VBPqXjFyyNwowzbMD+hizmprP/Fwkl2A==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-buffer": "1.9.0",
        "@webassemblyjs/wasm-gen": "1.9.0",
        "@webassemblyjs/wasm-parser": "1.9.0"
      }
    },
    "@webassemblyjs/wasm-parser": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wasm-parser/-/wasm-parser-1.9.0.tgz",
      "integrity": "sha512-9+wkMowR2AmdSWQzsPEjFU7njh8HTO5MqO8vjwEHuM+AMHioNqSBONRdr0NQQ3dVQrzp0s8lTcYqzUdb7YgELA==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-api-error": "1.9.0",
        "@webassemblyjs/helper-wasm-bytecode": "1.9.0",
        "@webassemblyjs/ieee754": "1.9.0",
        "@webassemblyjs/leb128": "1.9.0",
        "@webassemblyjs/utf8": "1.9.0"
      }
    },
    "@webassemblyjs/wast-parser": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wast-parser/-/wast-parser-1.9.0.tgz",
      "integrity": "sha512-qsqSAP3QQ3LyZjNC/0jBJ/ToSxfYJ8kYyuiGvtn/8MK89VrNEfwj7BPQzJVHi0jGTRK2dGdJ5PRqhtjzoww+bw==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/floating-point-hex-parser": "1.9.0",
        "@webassemblyjs/helper-api-error": "1.9.0",
        "@webassemblyjs/helper-code-frame": "1.9.0",
        "@webassemblyjs/helper-fsm": "1.9.0",
        "@xtuc/long": "4.2.2"
      }
    },
    "@webassemblyjs/wast-printer": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@webassemblyjs/wast-printer/-/wast-printer-1.9.0.tgz",
      "integrity": "sha512-2J0nE95rHXHyQ24cWjMKJ1tqB/ds8z/cyeOZxJhcb+rW+SQASVjuznUSmdz5GpVJTzU8JkhYut0D3siFDD6wsA==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/wast-parser": "1.9.0",
        "@xtuc/long": "4.2.2"
      }
    },
    "@xtuc/ieee754": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/@xtuc/ieee754/-/ieee754-1.2.0.tgz",
      "integrity": "sha512-DX8nKgqcGwsc0eJSqYt5lwP4DH5FlHnmuWWBRy7X0NcaGR0ZtuyeESgMwTYVEtxmsNGY+qit4QYT/MIYTOTPeA=="
    },
    "@xtuc/long": {
      "version": "4.2.2",
      "resolved": "https://registry.npmjs.org/@xtuc/long/-/long-4.2.2.tgz",
      "integrity": "sha512-NuHqBY1PB/D8xU6s/thBgOAiAP7HOYDQ32+BFZILJ8ivkUkAHQnWfn6WhL79Owj1qmUnoN/YPhktdIoucipkAQ=="
    },
    "acorn": {
      "version": "6.4.1",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-6.4.1.tgz",
      "integrity": "sha512-ZVA9k326Nwrj3Cj9jlh3wGFutC2ZornPNARZwsNYqQYgN0EsV2d53w5RN/co65Ohn4sUAUtb1rSUAOD6XN9idA=="
    },
    "adjust-sourcemap-loader": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/adjust-sourcemap-loader/-/adjust-sourcemap-loader-2.0.0.tgz",
      "integrity": "sha512-4hFsTsn58+YjrU9qKzML2JSSDqKvN8mUGQ0nNIrfPi8hmIONT4L3uUaT6MKdMsZ9AjsU6D2xDkZxCkbQPxChrA==",
      "requires": {
        "assert": "1.4.1",
        "camelcase": "5.0.0",
        "loader-utils": "1.2.3",
        "object-path": "0.11.4",
        "regex-parser": "2.2.10"
      },
      "dependencies": {
        "camelcase": {
          "version": "5.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-5.0.0.tgz",
          "integrity": "sha512-faqwZqnWxbxn+F1d399ygeamQNy3lPp/H9H6rNrqYh4FSVCtcY+3cub1MxA8o9mDd55mM8Aghuu/kuyYA6VTsA=="
        },
        "emojis-list": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz",
          "integrity": "sha1-TapNnbAPmBmIDHn6RXrlsJof04k="
        },
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.2.3",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz",
          "integrity": "sha512-fkpz8ejdnEMG3s37wGL07iSBDg99O9D5yflE9RGNH3hRdx9SOwYfnGYdZOUIZitN8E+E2vkq3MUMYMvPYl5ZZA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^2.0.0",
            "json5": "^1.0.1"
          }
        }
      }
    },
    "ajv": {
      "version": "6.12.4",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.12.4.tgz",
      "integrity": "sha512-eienB2c9qVQs2KWexhkrdMLVDoIQCz5KSeLxwg9Lzk4DOfBtIK9PQwwufcsn1jjGuf9WZmqPMbGxOzfcuphJCQ==",
      "requires": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      }
    },
    "ajv-errors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/ajv-errors/-/ajv-errors-1.0.1.tgz",
      "integrity": "sha512-DCRfO/4nQ+89p/RK43i8Ezd41EqdGIU4ld7nGF8OQ14oc/we5rEntLCUa7+jrn3nn83BosfwZA0wb4pon2o8iQ=="
    },
    "ajv-keywords": {
      "version": "3.5.2",
      "resolved": "https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz",
      "integrity": "sha512-5p6WTN0DdTGVQk6VjcEju19IgaHudalcfabD7yhDGeA6bcQnmL+CpveLJq/3hvfwd1aof6L386Ougkx6RfyMIQ=="
    },
    "alphanum-sort": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz",
      "integrity": "sha1-l6ERlkmyEa0zaR2fn0hqjsn74KM="
    },
    "ansi-regex": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
      "integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8="
    },
    "ansi-styles": {
      "version": "3.2.1",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz",
      "integrity": "sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==",
      "requires": {
        "color-convert": "^1.9.0"
      }
    },
    "anymatch": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.1.tgz",
      "integrity": "sha512-mM8522psRCqzV+6LhomX5wgp25YVibjh8Wj23I5RPkPppSVSjyKD2A2mBJmWGa+KN7f2D6LNh9jkBCeyLktzjg==",
      "requires": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      }
    },
    "aproba": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz",
      "integrity": "sha512-Y9J6ZjXtoYh8RnXVCMOU/ttDmk1aBjunq9vO0ta5x85WDQiQfUF9sIPBITdbiiIVcBo03Hi3jMxigBtsddlXRw=="
    },
    "argparse": {
      "version": "1.0.10",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz",
      "integrity": "sha512-o5Roy6tNG4SL/FOkCAN6RzjiakZS25RLYFrcMttJqbdd8BWrnA+fGz57iN5Pb06pvBGvl5gQ0B48dJlslXvoTg==",
      "requires": {
        "sprintf-js": "~1.0.2"
      }
    },
    "arity-n": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/arity-n/-/arity-n-1.0.4.tgz",
      "integrity": "sha1-2edrEXM+CFacCEeuezmyhgswt0U="
    },
    "arr-diff": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-4.0.0.tgz",
      "integrity": "sha1-1kYQdP6/7HHn4VI1dhoyml3HxSA="
    },
    "arr-flatten": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz",
      "integrity": "sha512-L3hKV5R/p5o81R7O02IGnwpDmkp6E982XhtbuwSe3O4qOtMMMtodicASA1Cny2U+aCXcNpml+m4dPsvsJ3jatg=="
    },
    "arr-union": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/arr-union/-/arr-union-3.1.0.tgz",
      "integrity": "sha1-45sJrqne+Gao8gbiiK9jkZuuOcQ="
    },
    "array-unique": {
      "version": "0.3.2",
      "resolved": "https://registry.npmjs.org/array-unique/-/array-unique-0.3.2.tgz",
      "integrity": "sha1-qJS3XUvE9s1nnvMkSp/Y9Gri1Cg="
    },
    "asn1.js": {
      "version": "5.4.1",
      "resolved": "https://registry.npmjs.org/asn1.js/-/asn1.js-5.4.1.tgz",
      "integrity": "sha512-+I//4cYPccV8LdmBLiX8CYvf9Sp3vQsrqu2QNXRcrbiWvcx/UdlFiqUJJzxRQxgsZmvhXhn4cSKeSmoFjVdupA==",
      "requires": {
        "bn.js": "^4.0.0",
        "inherits": "^2.0.1",
        "minimalistic-assert": "^1.0.0",
        "safer-buffer": "^2.1.0"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "assert": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/assert/-/assert-1.4.1.tgz",
      "integrity": "sha1-mZEtWRg2tab1s0XA8H7vwI/GXZE=",
      "requires": {
        "util": "0.10.3"
      }
    },
    "assign-symbols": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/assign-symbols/-/assign-symbols-1.0.0.tgz",
      "integrity": "sha1-WWZ/QfrdTyDMvCu5a41Pf3jsA2c="
    },
    "async-each": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/async-each/-/async-each-1.0.3.tgz",
      "integrity": "sha512-z/WhQ5FPySLdvREByI2vZiTWwCnF0moMJ1hK9YQwDTHKh6I7/uSckMetoRGb5UBZPC1z0jlw+n/XCgjeH7y1AQ==",
      "optional": true
    },
    "atob": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/atob/-/atob-2.1.2.tgz",
      "integrity": "sha512-Wm6ukoaOGJi/73p/cl2GvLjTI5JM1k/O14isD73YML8StrH/7/lRFgmg8nICZgD3bZZvjwCGxtMOD3wWNAu8cg=="
    },
    "babel-code-frame": {
      "version": "6.26.0",
      "resolved": "https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz",
      "integrity": "sha1-Y/1D99weO7fONZR9uP42mj9Yx0s=",
      "requires": {
        "chalk": "^1.1.3",
        "esutils": "^2.0.2",
        "js-tokens": "^3.0.2"
      },
      "dependencies": {
        "ansi-styles": {
          "version": "2.2.1",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz",
          "integrity": "sha1-tDLdM1i2NM914eRmQ2gkBTPB3b4="
        },
        "chalk": {
          "version": "1.1.3",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz",
          "integrity": "sha1-qBFcVeSnAv5NFQq9OHKCKn4J/Jg=",
          "requires": {
            "ansi-styles": "^2.2.1",
            "escape-string-regexp": "^1.0.2",
            "has-ansi": "^2.0.0",
            "strip-ansi": "^3.0.0",
            "supports-color": "^2.0.0"
          }
        },
        "js-tokens": {
          "version": "3.0.2",
          "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz",
          "integrity": "sha1-mGbfOVECEw449/mWvOtlRDIJwls="
        },
        "supports-color": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz",
          "integrity": "sha1-U10EXOa2Nj+kARcIRimZXp3zJMc="
        }
      }
    },
    "babel-plugin-dynamic-import-node": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.3.tgz",
      "integrity": "sha512-jZVI+s9Zg3IqA/kdi0i6UDCybUI3aSBLnglhYbSSjKlV7yF1F/5LWv8MakQmvYpnbJDS6fcBL2KzHSxNCMtWSQ==",
      "requires": {
        "object.assign": "^4.1.0"
      }
    },
    "babel-plugin-syntax-jsx": {
      "version": "6.18.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-jsx/-/babel-plugin-syntax-jsx-6.18.0.tgz",
      "integrity": "sha1-CvMqmm4Tyno/1QaeYtew9Y0NiUY="
    },
    "babel-plugin-transform-define": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-define/-/babel-plugin-transform-define-2.0.0.tgz",
      "integrity": "sha512-0dv5RNRUlUKxGYIIErl01lpvi8b7W2R04Qcl1mCj70ahwZcgiklfXnFlh4FGnRh6aayCfSZKdhiMryVzcq5Dmg==",
      "requires": {
        "lodash": "^4.17.11",
        "traverse": "0.6.6"
      }
    },
    "babel-plugin-transform-react-remove-prop-types": {
      "version": "0.4.24",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-react-remove-prop-types/-/babel-plugin-transform-react-remove-prop-types-0.4.24.tgz",
      "integrity": "sha512-eqj0hVcJUR57/Ug2zE1Yswsw4LhuqqHhD+8v120T1cl3kjg76QwtyBrdIk4WVwK+lAhBJVYCd/v+4nc4y+8JsA=="
    },
    "bail": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/bail/-/bail-1.0.5.tgz",
      "integrity": "sha512-xFbRxM1tahm08yHBP16MMjVUAvDaBMD38zsM9EMAUN61omwLmKlOpB/Zku5QkjZ8TZ4vn53pj+t518cH0S03RQ=="
    },
    "balanced-match": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz",
      "integrity": "sha1-ibTRmasr7kneFk6gK4nORi1xt2c="
    },
    "base": {
      "version": "0.11.2",
      "resolved": "https://registry.npmjs.org/base/-/base-0.11.2.tgz",
      "integrity": "sha512-5T6P4xPgpp0YDFvSWwEZ4NoE3aM4QBQXDzmVbraCkFj8zHM+mba8SyqB5DbZWyR7mYHo6Y7BdQo3MoA4m0TeQg==",
      "requires": {
        "cache-base": "^1.0.1",
        "class-utils": "^0.3.5",
        "component-emitter": "^1.2.1",
        "define-property": "^1.0.0",
        "isobject": "^3.0.1",
        "mixin-deep": "^1.2.0",
        "pascalcase": "^0.1.1"
      },
      "dependencies": {
        "define-property": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz",
          "integrity": "sha1-dp66rz9KY6rTr56NMEybvnm/sOY=",
          "requires": {
            "is-descriptor": "^1.0.0"
          }
        },
        "is-accessor-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz",
          "integrity": "sha512-m5hnHTkcVsPfqx3AKlyttIPb7J+XykHvJP2B9bZDjlhLIoEq4XoK64Vg7boZlVWYK6LUY94dYPEE7Lh0ZkZKcQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-data-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz",
          "integrity": "sha512-jbRXy1FmtAoCjQkVmIVYwuuqDFUbaOeDjmed1tOGPrsMhtJA4rD9tkgA0F1qJ3gRFRXcHYVkdeaP50Q5rE/jLQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-descriptor": {
          "version": "1.0.2",
          "resolved": "https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz",
          "integrity": "sha512-2eis5WqQGV7peooDyLmNEPUrps9+SXX5c9pL3xEB+4e9HnGuDa7mB7kHxHw4CbqS9k1T2hOH3miL8n8WtiYVtg==",
          "requires": {
            "is-accessor-descriptor": "^1.0.0",
            "is-data-descriptor": "^1.0.0",
            "kind-of": "^6.0.2"
          }
        }
      }
    },
    "base64-js": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.3.1.tgz",
      "integrity": "sha512-mLQ4i2QO1ytvGWFWmcngKO//JXAQueZvwEKtjgQFM4jIK0kU+ytMfplL8j+n5mspOfjHwoAg+9yhb7BwAHm36g=="
    },
    "big.js": {
      "version": "5.2.2",
      "resolved": "https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz",
      "integrity": "sha512-vyL2OymJxmarO8gxMr0mhChsO9QGwhynfuu4+MHTAW6czfq9humCB7rKpUjDd9YUiDPU4mzpyupFSvOClAwbmQ=="
    },
    "binary-extensions": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.1.0.tgz",
      "integrity": "sha512-1Yj8h9Q+QDF5FzhMs/c9+6UntbD5MkRfRwac8DoEm9ZfUBZ7tZ55YcGVAzEe4bXsdQHEk+s9S5wsOKVdZrw0tQ=="
    },
    "bluebird": {
      "version": "3.7.2",
      "resolved": "https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz",
      "integrity": "sha512-XpNj6GDQzdfW+r2Wnn7xiSAd7TM3jzkxGXBGTtWKuSXv1xUV+azxAm8jdWZN06QTQk+2N2XB9jRDkvbmQmcRtg=="
    },
    "bn.js": {
      "version": "5.1.3",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-5.1.3.tgz",
      "integrity": "sha512-GkTiFpjFtUzU9CbMeJ5iazkCzGL3jrhzerzZIuqLABjbwRaFt33I9tUdSNryIptM+RxDet6OKm2WnLXzW51KsQ=="
    },
    "boolbase": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz",
      "integrity": "sha1-aN/1++YMUes3cl6p4+0xDcwed24="
    },
    "brace-expansion": {
      "version": "1.1.11",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz",
      "integrity": "sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==",
      "requires": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "braces": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.2.tgz",
      "integrity": "sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==",
      "requires": {
        "fill-range": "^7.0.1"
      }
    },
    "brorand": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/brorand/-/brorand-1.1.0.tgz",
      "integrity": "sha1-EsJe/kCkXjwyPrhnWgoM5XsiNx8="
    },
    "browserify-aes": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/browserify-aes/-/browserify-aes-1.2.0.tgz",
      "integrity": "sha512-+7CHXqGuspUn/Sl5aO7Ea0xWGAtETPXNSAjHo48JfLdPWcMng33Xe4znFvQweqc/uzk5zSOI3H52CYnjCfb5hA==",
      "requires": {
        "buffer-xor": "^1.0.3",
        "cipher-base": "^1.0.0",
        "create-hash": "^1.1.0",
        "evp_bytestokey": "^1.0.3",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "browserify-cipher": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/browserify-cipher/-/browserify-cipher-1.0.1.tgz",
      "integrity": "sha512-sPhkz0ARKbf4rRQt2hTpAHqn47X3llLkUGn+xEJzLjwY8LRs2p0v7ljvI5EyoRO/mexrNunNECisZs+gw2zz1w==",
      "requires": {
        "browserify-aes": "^1.0.4",
        "browserify-des": "^1.0.0",
        "evp_bytestokey": "^1.0.0"
      }
    },
    "browserify-des": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/browserify-des/-/browserify-des-1.0.2.tgz",
      "integrity": "sha512-BioO1xf3hFwz4kc6iBhI3ieDFompMhrMlnDFC4/0/vd5MokpuAc3R+LYbwTA9A5Yc9pq9UYPqffKpW2ObuwX5A==",
      "requires": {
        "cipher-base": "^1.0.1",
        "des.js": "^1.0.0",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.1.2"
      }
    },
    "browserify-rsa": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/browserify-rsa/-/browserify-rsa-4.0.1.tgz",
      "integrity": "sha1-IeCr+vbyApzy+vsTNWenAdQTVSQ=",
      "requires": {
        "bn.js": "^4.1.0",
        "randombytes": "^2.0.1"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "browserify-sign": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/browserify-sign/-/browserify-sign-4.2.1.tgz",
      "integrity": "sha512-/vrA5fguVAKKAVTNJjgSm1tRQDHUU6DbwO9IROu/0WAzC8PKhucDSh18J0RMvVeHAn5puMd+QHC2erPRNf8lmg==",
      "requires": {
        "bn.js": "^5.1.1",
        "browserify-rsa": "^4.0.1",
        "create-hash": "^1.2.0",
        "create-hmac": "^1.1.7",
        "elliptic": "^6.5.3",
        "inherits": "^2.0.4",
        "parse-asn1": "^5.1.5",
        "readable-stream": "^3.6.0",
        "safe-buffer": "^5.2.0"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        },
        "readable-stream": {
          "version": "3.6.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.0.tgz",
          "integrity": "sha512-BViHy7LKeTz4oNnkcLJ+lVSL6vpiFeX6/d3oSH8zCW7UxP2onchk+vTGB143xuFjHS3deTgkKoXXymXqymiIdA==",
          "requires": {
            "inherits": "^2.0.3",
            "string_decoder": "^1.1.1",
            "util-deprecate": "^1.0.1"
          }
        },
        "safe-buffer": {
          "version": "5.2.1",
          "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
          "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ=="
        }
      }
    },
    "browserify-zlib": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.2.0.tgz",
      "integrity": "sha512-Z942RysHXmJrhqk88FmKBVq/v5tqmSkDz7p54G/MGyjMnCFFnC79XWNbg+Vta8W6Wb2qtSZTSxIGkJrRpCFEiA==",
      "requires": {
        "pako": "~1.0.5"
      }
    },
    "browserslist": {
      "version": "4.8.3",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.8.3.tgz",
      "integrity": "sha512-iU43cMMknxG1ClEZ2MDKeonKE1CCrFVkQK2AqO2YWFmvIrx4JWrvQ4w4hQez6EpVI8rHTtqh/ruHHDHSOKxvUg==",
      "requires": {
        "caniuse-lite": "^1.0.30001017",
        "electron-to-chromium": "^1.3.322",
        "node-releases": "^1.1.44"
      }
    },
    "buffer": {
      "version": "4.9.2",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-4.9.2.tgz",
      "integrity": "sha512-xq+q3SRMOxGivLhBNaUdC64hDTQwejJ+H0T/NB1XMtTVEwNTrfFF3gAxiyW0Bu/xWEGhjVKgUcMhCrUy2+uCWg==",
      "requires": {
        "base64-js": "^1.0.2",
        "ieee754": "^1.1.4",
        "isarray": "^1.0.0"
      }
    },
    "buffer-from": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz",
      "integrity": "sha512-MQcXEUbCKtEo7bhqEs6560Hyd4XaovZlO/k9V3hjVUF/zwW7KBVdSK4gIt/bzwS9MbR5qob+F5jusZsb0YQK2A=="
    },
    "buffer-xor": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/buffer-xor/-/buffer-xor-1.0.3.tgz",
      "integrity": "sha1-JuYe0UIvtw3ULm42cp7VHYVf6Nk="
    },
    "builtin-status-codes": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/builtin-status-codes/-/builtin-status-codes-3.0.0.tgz",
      "integrity": "sha1-hZgoeOIbmOHGZCXgPQF0eI9Wnug="
    },
    "cacache": {
      "version": "12.0.4",
      "resolved": "https://registry.npmjs.org/cacache/-/cacache-12.0.4.tgz",
      "integrity": "sha512-a0tMB40oefvuInr4Cwb3GerbL9xTj1D5yg0T5xrjGCGyfvbxseIXX7BAO/u/hIXdafzOI5JC3wDwHyf24buOAQ==",
      "requires": {
        "bluebird": "^3.5.5",
        "chownr": "^1.1.1",
        "figgy-pudding": "^3.5.1",
        "glob": "^7.1.4",
        "graceful-fs": "^4.1.15",
        "infer-owner": "^1.0.3",
        "lru-cache": "^5.1.1",
        "mississippi": "^3.0.0",
        "mkdirp": "^0.5.1",
        "move-concurrently": "^1.0.1",
        "promise-inflight": "^1.0.1",
        "rimraf": "^2.6.3",
        "ssri": "^6.0.1",
        "unique-filename": "^1.1.1",
        "y18n": "^4.0.0"
      },
      "dependencies": {
        "lru-cache": {
          "version": "5.1.1",
          "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
          "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
          "requires": {
            "yallist": "^3.0.2"
          }
        },
        "yallist": {
          "version": "3.1.1",
          "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
          "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g=="
        }
      }
    },
    "cache-base": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/cache-base/-/cache-base-1.0.1.tgz",
      "integrity": "sha512-AKcdTnFSWATd5/GCPRxr2ChwIJ85CeyrEyjRHlKxQ56d4XJMGym0uAiKn0xbLOGOl3+yRpOTi484dVCEc5AUzQ==",
      "requires": {
        "collection-visit": "^1.0.0",
        "component-emitter": "^1.2.1",
        "get-value": "^2.0.6",
        "has-value": "^1.0.0",
        "isobject": "^3.0.1",
        "set-value": "^2.0.0",
        "to-object-path": "^0.3.0",
        "union-value": "^1.0.0",
        "unset-value": "^1.0.0"
      }
    },
    "caller-callsite": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/caller-callsite/-/caller-callsite-2.0.0.tgz",
      "integrity": "sha1-hH4PzgoiN1CpoCfFSzNzGtMVQTQ=",
      "requires": {
        "callsites": "^2.0.0"
      }
    },
    "caller-path": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/caller-path/-/caller-path-2.0.0.tgz",
      "integrity": "sha1-Ro+DBE42mrIBD6xfBs7uFbsssfQ=",
      "requires": {
        "caller-callsite": "^2.0.0"
      }
    },
    "callsites": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/callsites/-/callsites-2.0.0.tgz",
      "integrity": "sha1-BuuE8A7qQT2oav/vrL/7Ngk7PFA="
    },
    "camelcase": {
      "version": "5.3.1",
      "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz",
      "integrity": "sha512-L28STB170nwWS63UjtlEOE3dldQApaJXZkOI1uMFfzf3rRuPegHaHesyee+YxQ+W6SvRDQV6UrdOdRiR153wJg=="
    },
    "caniuse-api": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/caniuse-api/-/caniuse-api-3.0.0.tgz",
      "integrity": "sha512-bsTwuIg/BZZK/vreVTYYbSWoe2F+71P7K5QGEX+pT250DZbfU1MQ5prOKpPR+LL6uWKK3KMwMCAS74QB3Um1uw==",
      "requires": {
        "browserslist": "^4.0.0",
        "caniuse-lite": "^1.0.0",
        "lodash.memoize": "^4.1.2",
        "lodash.uniq": "^4.5.0"
      }
    },
    "caniuse-lite": {
      "version": "1.0.30001117",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001117.tgz",
      "integrity": "sha512-4tY0Fatzdx59kYjQs+bNxUwZB03ZEBgVmJ1UkFPz/Q8OLiUUbjct2EdpnXj0fvFTPej2EkbPIG0w8BWsjAyk1Q=="
    },
    "ccount": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/ccount/-/ccount-1.0.5.tgz",
      "integrity": "sha512-MOli1W+nfbPLlKEhInaxhRdp7KVLFxLN5ykwzHgLsLI3H3gs5jjFAK4Eoj3OzzcxCtumDaI8onoVDeQyWaNTkw=="
    },
    "chalk": {
      "version": "2.4.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz",
      "integrity": "sha512-Mti+f9lpJNcwF4tWV8/OrTTtF1gZi+f8FqlyAdouralcFWFQWF2+NgCHShjkCb+IFBLq9buZwE1xckQU4peSuQ==",
      "requires": {
        "ansi-styles": "^3.2.1",
        "escape-string-regexp": "^1.0.5",
        "supports-color": "^5.3.0"
      },
      "dependencies": {
        "supports-color": {
          "version": "5.5.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz",
          "integrity": "sha512-QjVjwdXIt408MIiAqCX4oUKsgU2EqAGzs2Ppkm4aQYbjm+ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow==",
          "requires": {
            "has-flag": "^3.0.0"
          }
        }
      }
    },
    "character-entities": {
      "version": "1.2.4",
      "resolved": "https://registry.npmjs.org/character-entities/-/character-entities-1.2.4.tgz",
      "integrity": "sha512-iBMyeEHxfVnIakwOuDXpVkc54HijNgCyQB2w0VfGQThle6NXn50zU6V/u+LDhxHcDUPojn6Kpga3PTAD8W1bQw=="
    },
    "character-entities-html4": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/character-entities-html4/-/character-entities-html4-1.1.4.tgz",
      "integrity": "sha512-HRcDxZuZqMx3/a+qrzxdBKBPUpxWEq9xw2OPZ3a/174ihfrQKVsFhqtthBInFy1zZ9GgZyFXOatNujm8M+El3g=="
    },
    "character-entities-legacy": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/character-entities-legacy/-/character-entities-legacy-1.1.4.tgz",
      "integrity": "sha512-3Xnr+7ZFS1uxeiUDvV02wQ+QDbc55o97tIV5zHScSPJpcLm/r0DFPcoY3tYRp+VZukxuMeKgXYmsXQHO05zQeA=="
    },
    "character-reference-invalid": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/character-reference-invalid/-/character-reference-invalid-1.1.4.tgz",
      "integrity": "sha512-mKKUkUbhPpQlCOfIuZkvSEgktjPFIsZKRRbC6KWVEMvlzblj3i3asQv5ODsrwt0N3pHAEvjP8KTQPHkp0+6jOg=="
    },
    "chokidar": {
      "version": "3.4.2",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.4.2.tgz",
      "integrity": "sha512-IZHaDeBeI+sZJRX7lGcXsdzgvZqKv6sECqsbErJA4mHWfpRrD8B97kSFN4cQz6nGBGiuFia1MKR4d6c1o8Cv7A==",
      "requires": {
        "anymatch": "~3.1.1",
        "braces": "~3.0.2",
        "fsevents": "~2.1.2",
        "glob-parent": "~5.1.0",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.4.0"
      }
    },
    "chownr": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz",
      "integrity": "sha512-jJ0bqzaylmJtVnNgzTeSOs8DPavpbYgEr/b0YL8/2GO3xJEhInFmhKMUnEJQjZumK7KXGFhUy89PrsJWlakBVg=="
    },
    "chrome-trace-event": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/chrome-trace-event/-/chrome-trace-event-1.0.2.tgz",
      "integrity": "sha512-9e/zx1jw7B4CO+c/RXoCsfg/x1AfUBioy4owYH0bJprEYAx5hRFLRhWBqHAG57D0ZM4H7vxbP7bPe0VwhQRYDQ==",
      "requires": {
        "tslib": "^1.9.0"
      }
    },
    "cipher-base": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/cipher-base/-/cipher-base-1.0.4.tgz",
      "integrity": "sha512-Kkht5ye6ZGmwv40uUDZztayT2ThLQGfnj/T71N/XzeZeo3nf8foyW7zGTsPYkEya3m5f3cAypH+qe7YOrM1U2Q==",
      "requires": {
        "inherits": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "class-utils": {
      "version": "0.3.6",
      "resolved": "https://registry.npmjs.org/class-utils/-/class-utils-0.3.6.tgz",
      "integrity": "sha512-qOhPa/Fj7s6TY8H8esGu5QNpMMQxz79h+urzrNYN6mn+9BnxlDGf5QZ+XeCDsxSjPqsSR56XOZOJmpeurnLMeg==",
      "requires": {
        "arr-union": "^3.1.0",
        "define-property": "^0.2.5",
        "isobject": "^3.0.0",
        "static-extend": "^0.1.1"
      },
      "dependencies": {
        "define-property": {
          "version": "0.2.5",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz",
          "integrity": "sha1-w1se+RjsPJkPmlvFe+BKrOxcgRY=",
          "requires": {
            "is-descriptor": "^0.1.0"
          }
        }
      }
    },
    "clone-deep": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/clone-deep/-/clone-deep-4.0.1.tgz",
      "integrity": "sha512-neHB9xuzh/wk0dIHweyAXv2aPGZIVk3pLMe+/RNzINf17fe0OG96QroktYAUm7SM1PBnzTabaLboqqxDyMU+SQ==",
      "requires": {
        "is-plain-object": "^2.0.4",
        "kind-of": "^6.0.2",
        "shallow-clone": "^3.0.0"
      }
    },
    "coa": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/coa/-/coa-2.0.2.tgz",
      "integrity": "sha512-q5/jG+YQnSy4nRTV4F7lPepBJZ8qBNJJDBuJdoejDyLXgmL7IEo+Le2JDZudFTFt7mrCqIRaSjws4ygRCTCAXA==",
      "requires": {
        "@types/q": "^1.5.1",
        "chalk": "^2.4.1",
        "q": "^1.1.2"
      }
    },
    "collapse-white-space": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/collapse-white-space/-/collapse-white-space-1.0.6.tgz",
      "integrity": "sha512-jEovNnrhMuqyCcjfEJA56v0Xq8SkIoPKDyaHahwo3POf4qcSXqMYuwNcOTzp74vTsR9Tn08z4MxWqAhcekogkQ=="
    },
    "collection-visit": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/collection-visit/-/collection-visit-1.0.0.tgz",
      "integrity": "sha1-S8A3PBZLwykbTTaMgpzxqApZ3KA=",
      "requires": {
        "map-visit": "^1.0.0",
        "object-visit": "^1.0.0"
      }
    },
    "color": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/color/-/color-3.1.2.tgz",
      "integrity": "sha512-vXTJhHebByxZn3lDvDJYw4lR5+uB3vuoHsuYA5AKuxRVn5wzzIfQKGLBmgdVRHKTJYeK5rvJcHnrd0Li49CFpg==",
      "requires": {
        "color-convert": "^1.9.1",
        "color-string": "^1.5.2"
      }
    },
    "color-convert": {
      "version": "1.9.3",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz",
      "integrity": "sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==",
      "requires": {
        "color-name": "1.1.3"
      }
    },
    "color-name": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz",
      "integrity": "sha1-p9BVi9icQveV3UIyj3QIMcpTvCU="
    },
    "color-string": {
      "version": "1.5.3",
      "resolved": "https://registry.npmjs.org/color-string/-/color-string-1.5.3.tgz",
      "integrity": "sha512-dC2C5qeWoYkxki5UAXapdjqO672AM4vZuPGRQfO8b5HKuKGBbKWpITyDYN7TOFKvRW7kOgAn3746clDBMDJyQw==",
      "requires": {
        "color-name": "^1.0.0",
        "simple-swizzle": "^0.2.2"
      }
    },
    "comma-separated-tokens": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/comma-separated-tokens/-/comma-separated-tokens-1.0.8.tgz",
      "integrity": "sha512-GHuDRO12Sypu2cV70d1dkA2EUmXHgntrzbpvOB+Qy+49ypNfGgFQIC2fhhXbnyrJRynDCAARsT7Ou0M6hirpfw=="
    },
    "commander": {
      "version": "2.20.3",
      "resolved": "https://registry.npmjs.org/commander/-/commander-2.20.3.tgz",
      "integrity": "sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ=="
    },
    "commondir": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz",
      "integrity": "sha1-3dgA2gxmEnOTzKWVDqloo6rxJTs="
    },
    "component-emitter": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/component-emitter/-/component-emitter-1.3.0.tgz",
      "integrity": "sha512-Rd3se6QB+sO1TwqZjscQrurpEPIfO0/yYnSin6Q/rD3mOutHvUrCAhJub3r90uNb+SESBuE0QYoB90YdfatsRg=="
    },
    "compose-function": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/compose-function/-/compose-function-3.0.3.tgz",
      "integrity": "sha1-ntZ18TzFRQHTCVCkhv9qe6OrGF8=",
      "requires": {
        "arity-n": "^1.0.4"
      }
    },
    "concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha1-2Klr13/Wjfd5OnMDajug1UBdR3s="
    },
    "concat-stream": {
      "version": "1.6.2",
      "resolved": "https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz",
      "integrity": "sha512-27HBghJxjiZtIk3Ycvn/4kbJk/1uZuJFfuPEns6LaEvpvG1f0hTea8lilrouyo9mVc2GWdcEZ8OLoGmSADlrCw==",
      "requires": {
        "buffer-from": "^1.0.0",
        "inherits": "^2.0.3",
        "readable-stream": "^2.2.2",
        "typedarray": "^0.0.6"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "console-browserify": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/console-browserify/-/console-browserify-1.2.0.tgz",
      "integrity": "sha512-ZMkYO/LkF17QvCPqM0gxw8yUzigAOZOSWSHg91FH6orS7vcEj5dVZTidN2fQ14yBSdg97RqhSNwLUXInd52OTA=="
    },
    "constants-browserify": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/constants-browserify/-/constants-browserify-1.0.0.tgz",
      "integrity": "sha1-wguW2MYXdIqvHBYCF2DNJ/y4y3U="
    },
    "convert-source-map": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.7.0.tgz",
      "integrity": "sha512-4FJkXzKXEDB1snCFZlLP4gpC3JILicCpGbzG9f9G7tGqGCzETQ2hWPrcinA9oU4wtf2biUaEH5065UnMeR33oA==",
      "requires": {
        "safe-buffer": "~5.1.1"
      }
    },
    "copy-concurrently": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/copy-concurrently/-/copy-concurrently-1.0.5.tgz",
      "integrity": "sha512-f2domd9fsVDFtaFcbaRZuYXwtdmnzqbADSwhSWYxYB/Q8zsdUUFMXVRwXGDMWmbEzAn1kdRrtI1T/KTFOL4X2A==",
      "requires": {
        "aproba": "^1.1.1",
        "fs-write-stream-atomic": "^1.0.8",
        "iferr": "^0.1.5",
        "mkdirp": "^0.5.1",
        "rimraf": "^2.5.4",
        "run-queue": "^1.0.0"
      }
    },
    "copy-descriptor": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/copy-descriptor/-/copy-descriptor-0.1.1.tgz",
      "integrity": "sha1-Z29us8OZl8LuGsOpJP1hJHSPV40="
    },
    "core-js-compat": {
      "version": "3.6.5",
      "resolved": "https://registry.npmjs.org/core-js-compat/-/core-js-compat-3.6.5.tgz",
      "integrity": "sha512-7ItTKOhOZbznhXAQ2g/slGg1PJV5zDO/WdkTwi7UEOJmkvsE32PWvx6mKtDjiMpjnR2CNf6BAD6sSxIlv7ptng==",
      "requires": {
        "browserslist": "^4.8.5",
        "semver": "7.0.0"
      },
      "dependencies": {
        "browserslist": {
          "version": "4.14.0",
          "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.14.0.tgz",
          "integrity": "sha512-pUsXKAF2lVwhmtpeA3LJrZ76jXuusrNyhduuQs7CDFf9foT4Y38aQOserd2lMe5DSSrjf3fx34oHwryuvxAUgQ==",
          "requires": {
            "caniuse-lite": "^1.0.30001111",
            "electron-to-chromium": "^1.3.523",
            "escalade": "^3.0.2",
            "node-releases": "^1.1.60"
          }
        },
        "semver": {
          "version": "7.0.0",
          "resolved": "https://registry.npmjs.org/semver/-/semver-7.0.0.tgz",
          "integrity": "sha512-+GB6zVA9LWh6zovYQLALHwv5rb2PHGlJi3lfiqIHxR0uuwCgefcOJc59v9fv1w8GbStwxuuqqAjI9NMAOOgq1A=="
        }
      }
    },
    "core-util-is": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz",
      "integrity": "sha1-tf1UIgqivFq1eqtxQMlAdUUDwac="
    },
    "cosmiconfig": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-5.2.1.tgz",
      "integrity": "sha512-H65gsXo1SKjf8zmrJ67eJk8aIRKV5ff2D4uKZIBZShbhGSpEmsQOPW/SKMKYhSTrqR7ufy6RP69rPogdaPh/kA==",
      "requires": {
        "import-fresh": "^2.0.0",
        "is-directory": "^0.3.1",
        "js-yaml": "^3.13.1",
        "parse-json": "^4.0.0"
      }
    },
    "create-ecdh": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/create-ecdh/-/create-ecdh-4.0.4.tgz",
      "integrity": "sha512-mf+TCx8wWc9VpuxfP2ht0iSISLZnt0JgWlrOKZiNqyUZWnjIaCIVNQArMHnCZKfEYRg6IM7A+NeJoN8gf/Ws0A==",
      "requires": {
        "bn.js": "^4.1.0",
        "elliptic": "^6.5.3"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "create-hash": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/create-hash/-/create-hash-1.2.0.tgz",
      "integrity": "sha512-z00bCGNHDG8mHAkP7CtT1qVu+bFQUPjYq/4Iv3C3kWjTFV10zIjfSoeqXo9Asws8gwSHDGj/hl2u4OGIjapeCg==",
      "requires": {
        "cipher-base": "^1.0.1",
        "inherits": "^2.0.1",
        "md5.js": "^1.3.4",
        "ripemd160": "^2.0.1",
        "sha.js": "^2.4.0"
      }
    },
    "create-hmac": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/create-hmac/-/create-hmac-1.1.7.tgz",
      "integrity": "sha512-MJG9liiZ+ogc4TzUwuvbER1JRdgvUFSB5+VR/g5h82fGaIRWMWddtKBHi7/sVhfjQZ6SehlyhvQYrcYkaUIpLg==",
      "requires": {
        "cipher-base": "^1.0.3",
        "create-hash": "^1.1.0",
        "inherits": "^2.0.1",
        "ripemd160": "^2.0.0",
        "safe-buffer": "^5.0.1",
        "sha.js": "^2.4.8"
      }
    },
    "cross-fetch": {
      "version": "3.0.5",
      "resolved": "https://registry.npmjs.org/cross-fetch/-/cross-fetch-3.0.5.tgz",
      "integrity": "sha512-FFLcLtraisj5eteosnX1gf01qYDCOc4fDy0+euOt8Kn9YBY2NtXL/pCoYPavw24NIQkQqm5ZOLsGD5Zzj0gyew==",
      "requires": {
        "node-fetch": "2.6.0"
      }
    },
    "crypto-browserify": {
      "version": "3.12.0",
      "resolved": "https://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.12.0.tgz",
      "integrity": "sha512-fz4spIh+znjO2VjL+IdhEpRJ3YN6sMzITSBijk6FK2UvTqruSQW+/cCZTSNsMiZNvUeq0CqurF+dAbyiGOY6Wg==",
      "requires": {
        "browserify-cipher": "^1.0.0",
        "browserify-sign": "^4.0.0",
        "create-ecdh": "^4.0.0",
        "create-hash": "^1.1.0",
        "create-hmac": "^1.1.0",
        "diffie-hellman": "^5.0.0",
        "inherits": "^2.0.1",
        "pbkdf2": "^3.0.3",
        "public-encrypt": "^4.0.0",
        "randombytes": "^2.0.0",
        "randomfill": "^1.0.3"
      }
    },
    "css": {
      "version": "2.2.4",
      "resolved": "https://registry.npmjs.org/css/-/css-2.2.4.tgz",
      "integrity": "sha512-oUnjmWpy0niI3x/mPL8dVEI1l7MnG3+HHyRPHf+YFSbK+svOhXpmSOcDURUh2aOCgl2grzrOPt1nHLuCVFULLw==",
      "requires": {
        "inherits": "^2.0.3",
        "source-map": "^0.6.1",
        "source-map-resolve": "^0.5.2",
        "urix": "^0.1.0"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "css-color-names": {
      "version": "0.0.4",
      "resolved": "https://registry.npmjs.org/css-color-names/-/css-color-names-0.0.4.tgz",
      "integrity": "sha1-gIrcLnnPhHOAabZGyyDsJ762KeA="
    },
    "css-declaration-sorter": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/css-declaration-sorter/-/css-declaration-sorter-4.0.1.tgz",
      "integrity": "sha512-BcxQSKTSEEQUftYpBVnsH4SF05NTuBokb19/sBt6asXGKZ/6VP7PLG1CBCkFDYOnhXhPh0jMhO6xZ71oYHXHBA==",
      "requires": {
        "postcss": "^7.0.1",
        "timsort": "^0.3.0"
      }
    },
    "css-loader": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/css-loader/-/css-loader-3.3.0.tgz",
      "integrity": "sha512-x9Y1vvHe5RR+4tzwFdWExPueK00uqFTCw7mZy+9aE/X1SKWOArm5luaOrtJ4d05IpOwJ6S86b/tVcIdhw1Bu4A==",
      "requires": {
        "camelcase": "^5.3.1",
        "cssesc": "^3.0.0",
        "icss-utils": "^4.1.1",
        "loader-utils": "^1.2.3",
        "normalize-path": "^3.0.0",
        "postcss": "^7.0.23",
        "postcss-modules-extract-imports": "^2.0.0",
        "postcss-modules-local-by-default": "^3.0.2",
        "postcss-modules-scope": "^2.1.1",
        "postcss-modules-values": "^3.0.0",
        "postcss-value-parser": "^4.0.2",
        "schema-utils": "^2.6.0"
      },
      "dependencies": {
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.4.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.0.tgz",
          "integrity": "sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^3.0.0",
            "json5": "^1.0.1"
          }
        }
      }
    },
    "css-select": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/css-select/-/css-select-2.1.0.tgz",
      "integrity": "sha512-Dqk7LQKpwLoH3VovzZnkzegqNSuAziQyNZUcrdDM401iY+R5NkGBXGmtO05/yaXQziALuPogeG0b7UAgjnTJTQ==",
      "requires": {
        "boolbase": "^1.0.0",
        "css-what": "^3.2.1",
        "domutils": "^1.7.0",
        "nth-check": "^1.0.2"
      },
      "dependencies": {
        "domutils": {
          "version": "1.7.0",
          "resolved": "https://registry.npmjs.org/domutils/-/domutils-1.7.0.tgz",
          "integrity": "sha512-Lgd2XcJ/NjEw+7tFvfKxOzCYKZsdct5lczQ2ZaQY8Djz7pfAD3Gbp8ySJWtreII/vDlMVmxwa6pHmdxIYgttDg==",
          "requires": {
            "dom-serializer": "0",
            "domelementtype": "1"
          }
        }
      }
    },
    "css-select-base-adapter": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/css-select-base-adapter/-/css-select-base-adapter-0.1.1.tgz",
      "integrity": "sha512-jQVeeRG70QI08vSTwf1jHxp74JoZsr2XSgETae8/xC8ovSnL2WF87GTLO86Sbwdt2lK4Umg4HnnwMO4YF3Ce7w=="
    },
    "css-tree": {
      "version": "1.0.0-alpha.37",
      "resolved": "https://registry.npmjs.org/css-tree/-/css-tree-1.0.0-alpha.37.tgz",
      "integrity": "sha512-DMxWJg0rnz7UgxKT0Q1HU/L9BeJI0M6ksor0OgqOnF+aRCDWg/N2641HmVyU9KVIu0OVVWOb2IpC9A+BJRnejg==",
      "requires": {
        "mdn-data": "2.0.4",
        "source-map": "^0.6.1"
      }
    },
    "css-what": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/css-what/-/css-what-3.3.0.tgz",
      "integrity": "sha512-pv9JPyatiPaQ6pf4OvD/dbfm0o5LviWmwxNWzblYf/1u9QZd0ihV+PMwy5jdQWQ3349kZmKEx9WXuSka2dM4cg=="
    },
    "cssesc": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
      "integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg=="
    },
    "cssnano": {
      "version": "4.1.10",
      "resolved": "https://registry.npmjs.org/cssnano/-/cssnano-4.1.10.tgz",
      "integrity": "sha512-5wny+F6H4/8RgNlaqab4ktc3e0/blKutmq8yNlBFXA//nSFFAqAngjNVRzUvCgYROULmZZUoosL/KSoZo5aUaQ==",
      "requires": {
        "cosmiconfig": "^5.0.0",
        "cssnano-preset-default": "^4.0.7",
        "is-resolvable": "^1.0.0",
        "postcss": "^7.0.0"
      }
    },
    "cssnano-preset-default": {
      "version": "4.0.7",
      "resolved": "https://registry.npmjs.org/cssnano-preset-default/-/cssnano-preset-default-4.0.7.tgz",
      "integrity": "sha512-x0YHHx2h6p0fCl1zY9L9roD7rnlltugGu7zXSKQx6k2rYw0Hi3IqxcoAGF7u9Q5w1nt7vK0ulxV8Lo+EvllGsA==",
      "requires": {
        "css-declaration-sorter": "^4.0.1",
        "cssnano-util-raw-cache": "^4.0.1",
        "postcss": "^7.0.0",
        "postcss-calc": "^7.0.1",
        "postcss-colormin": "^4.0.3",
        "postcss-convert-values": "^4.0.1",
        "postcss-discard-comments": "^4.0.2",
        "postcss-discard-duplicates": "^4.0.2",
        "postcss-discard-empty": "^4.0.1",
        "postcss-discard-overridden": "^4.0.1",
        "postcss-merge-longhand": "^4.0.11",
        "postcss-merge-rules": "^4.0.3",
        "postcss-minify-font-values": "^4.0.2",
        "postcss-minify-gradients": "^4.0.2",
        "postcss-minify-params": "^4.0.2",
        "postcss-minify-selectors": "^4.0.2",
        "postcss-normalize-charset": "^4.0.1",
        "postcss-normalize-display-values": "^4.0.2",
        "postcss-normalize-positions": "^4.0.2",
        "postcss-normalize-repeat-style": "^4.0.2",
        "postcss-normalize-string": "^4.0.2",
        "postcss-normalize-timing-functions": "^4.0.2",
        "postcss-normalize-unicode": "^4.0.1",
        "postcss-normalize-url": "^4.0.1",
        "postcss-normalize-whitespace": "^4.0.2",
        "postcss-ordered-values": "^4.1.2",
        "postcss-reduce-initial": "^4.0.3",
        "postcss-reduce-transforms": "^4.0.2",
        "postcss-svgo": "^4.0.2",
        "postcss-unique-selectors": "^4.0.1"
      }
    },
    "cssnano-util-get-arguments": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/cssnano-util-get-arguments/-/cssnano-util-get-arguments-4.0.0.tgz",
      "integrity": "sha1-7ToIKZ8h11dBsg87gfGU7UnMFQ8="
    },
    "cssnano-util-get-match": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/cssnano-util-get-match/-/cssnano-util-get-match-4.0.0.tgz",
      "integrity": "sha1-wOTKB/U4a7F+xeUiULT1lhNlFW0="
    },
    "cssnano-util-raw-cache": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/cssnano-util-raw-cache/-/cssnano-util-raw-cache-4.0.1.tgz",
      "integrity": "sha512-qLuYtWK2b2Dy55I8ZX3ky1Z16WYsx544Q0UWViebptpwn/xDBmog2TLg4f+DBMg1rJ6JDWtn96WHbOKDWt1WQA==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "cssnano-util-same-parent": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/cssnano-util-same-parent/-/cssnano-util-same-parent-4.0.1.tgz",
      "integrity": "sha512-WcKx5OY+KoSIAxBW6UBBRay1U6vkYheCdjyVNDm85zt5K9mHoGOfsOsqIszfAqrQQFIIKgjh2+FDgIj/zsl21Q=="
    },
    "csso": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/csso/-/csso-4.0.3.tgz",
      "integrity": "sha512-NL3spysxUkcrOgnpsT4Xdl2aiEiBG6bXswAABQVHcMrfjjBisFOKwLDOmf4wf32aPdcJws1zds2B0Rg+jqMyHQ==",
      "requires": {
        "css-tree": "1.0.0-alpha.39"
      },
      "dependencies": {
        "css-tree": {
          "version": "1.0.0-alpha.39",
          "resolved": "https://registry.npmjs.org/css-tree/-/css-tree-1.0.0-alpha.39.tgz",
          "integrity": "sha512-7UvkEYgBAHRG9Nt980lYxjsTrCyHFN53ky3wVsDkiMdVqylqRt+Zc+jm5qw7/qyOvN2dHSYtX0e4MbCCExSvnA==",
          "requires": {
            "mdn-data": "2.0.6",
            "source-map": "^0.6.1"
          }
        },
        "mdn-data": {
          "version": "2.0.6",
          "resolved": "https://registry.npmjs.org/mdn-data/-/mdn-data-2.0.6.tgz",
          "integrity": "sha512-rQvjv71olwNHgiTbfPZFkJtjNMciWgswYeciZhtvWLO8bmX3TnhyA62I6sTWOyZssWHJJjY6/KiWwqQsWWsqOA=="
        }
      }
    },
    "cyclist": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/cyclist/-/cyclist-1.0.1.tgz",
      "integrity": "sha1-WW6WmP0MgOEgOMK4LW6xs1tiJNk="
    },
    "d": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/d/-/d-1.0.1.tgz",
      "integrity": "sha512-m62ShEObQ39CfralilEQRjH6oAMtNCV1xJyEx5LpRYUVN+EviphDgUc/F3hnYbADmkiNs67Y+3ylmlG7Lnu+FA==",
      "requires": {
        "es5-ext": "^0.10.50",
        "type": "^1.0.1"
      }
    },
    "date-fns": {
      "version": "2.15.0",
      "resolved": "https://registry.npmjs.org/date-fns/-/date-fns-2.15.0.tgz",
      "integrity": "sha512-ZCPzAMJZn3rNUvvQIMlXhDr4A+Ar07eLeGsGREoWU19a3Pqf5oYa+ccd+B3F6XVtQY6HANMFdOQ8A+ipFnvJdQ=="
    },
    "debug": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.1.1.tgz",
      "integrity": "sha512-pYAIzeRo8J6KPEaJ0VWOh5Pzkbw/RetuzehGM7QRRX5he4fPHx2rdKMB256ehJCkX+XRQm16eZLqLNS8RSZXZw==",
      "requires": {
        "ms": "^2.1.1"
      }
    },
    "decode-uri-component": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/decode-uri-component/-/decode-uri-component-0.2.0.tgz",
      "integrity": "sha1-6zkTMzRYd1y4TNGh+uBiEGu4dUU="
    },
    "define-properties": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/define-properties/-/define-properties-1.1.3.tgz",
      "integrity": "sha512-3MqfYKj2lLzdMSf8ZIZE/V+Zuy+BgD6f164e8K2w7dgnpKArBDerGYpM46IYYcjnkdPNMjPk9A6VFB8+3SKlXQ==",
      "requires": {
        "object-keys": "^1.0.12"
      }
    },
    "define-property": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/define-property/-/define-property-2.0.2.tgz",
      "integrity": "sha512-jwK2UV4cnPpbcG7+VRARKTZPUWowwXA8bzH5NP6ud0oeAxyYPuGZUAC7hMugpCdz4BeSZl2Dl9k66CHJ/46ZYQ==",
      "requires": {
        "is-descriptor": "^1.0.2",
        "isobject": "^3.0.1"
      },
      "dependencies": {
        "is-accessor-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz",
          "integrity": "sha512-m5hnHTkcVsPfqx3AKlyttIPb7J+XykHvJP2B9bZDjlhLIoEq4XoK64Vg7boZlVWYK6LUY94dYPEE7Lh0ZkZKcQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-data-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz",
          "integrity": "sha512-jbRXy1FmtAoCjQkVmIVYwuuqDFUbaOeDjmed1tOGPrsMhtJA4rD9tkgA0F1qJ3gRFRXcHYVkdeaP50Q5rE/jLQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-descriptor": {
          "version": "1.0.2",
          "resolved": "https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz",
          "integrity": "sha512-2eis5WqQGV7peooDyLmNEPUrps9+SXX5c9pL3xEB+4e9HnGuDa7mB7kHxHw4CbqS9k1T2hOH3miL8n8WtiYVtg==",
          "requires": {
            "is-accessor-descriptor": "^1.0.0",
            "is-data-descriptor": "^1.0.0",
            "kind-of": "^6.0.2"
          }
        }
      }
    },
    "des.js": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/des.js/-/des.js-1.0.1.tgz",
      "integrity": "sha512-Q0I4pfFrv2VPd34/vfLrFOoRmlYj3OV50i7fskps1jZWK1kApMWWT9G6RRUeYedLcBDIhnSDaUvJMb3AhUlaEA==",
      "requires": {
        "inherits": "^2.0.1",
        "minimalistic-assert": "^1.0.0"
      }
    },
    "detab": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/detab/-/detab-2.0.3.tgz",
      "integrity": "sha512-Up8P0clUVwq0FnFjDclzZsy9PadzRn5FFxrr47tQQvMHqyiFYVbpH8oXDzWtF0Q7pYy3l+RPmtBl+BsFF6wH0A==",
      "requires": {
        "repeat-string": "^1.5.4"
      }
    },
    "diffie-hellman": {
      "version": "5.0.3",
      "resolved": "https://registry.npmjs.org/diffie-hellman/-/diffie-hellman-5.0.3.tgz",
      "integrity": "sha512-kqag/Nl+f3GwyK25fhUMYj81BUOrZ9IuJsjIcDE5icNM9FJHAVm3VcUDxdLPoQtTuUylWm6ZIknYJwwaPxsUzg==",
      "requires": {
        "bn.js": "^4.1.0",
        "miller-rabin": "^4.0.0",
        "randombytes": "^2.0.0"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "dom-serializer": {
      "version": "0.2.2",
      "resolved": "https://registry.npmjs.org/dom-serializer/-/dom-serializer-0.2.2.tgz",
      "integrity": "sha512-2/xPb3ORsQ42nHYiSunXkDjPLBaEj/xTwUO4B7XCZQTRk7EBtTOPaygh10YAAh2OI1Qrp6NWfpAhzswj0ydt9g==",
      "requires": {
        "domelementtype": "^2.0.1",
        "entities": "^2.0.0"
      },
      "dependencies": {
        "domelementtype": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-2.0.1.tgz",
          "integrity": "sha512-5HOHUDsYZWV8FGWN0Njbr/Rn7f/eWSQi1v7+HsUVwXgn8nWWlL64zKDkS0n8ZmQ3mlWOMuXOnR+7Nx/5tMO5AQ=="
        }
      }
    },
    "domain-browser": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/domain-browser/-/domain-browser-1.2.0.tgz",
      "integrity": "sha512-jnjyiM6eRyZl2H+W8Q/zLMA481hzi0eszAaBUzIVnmYVDBbnLxVNnfu1HgEBvCbL+71FrxMl3E6lpKH7Ge3OXA=="
    },
    "domelementtype": {
      "version": "1.3.1",
      "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-1.3.1.tgz",
      "integrity": "sha512-BSKB+TSpMpFI/HOxCNr1O8aMOTZ8hT3pM3GQ0w/mWRmkhEDSFJkkyzz4XQsBV44BChwGkrDfMyjVD0eA2aFV3w=="
    },
    "domhandler": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/domhandler/-/domhandler-3.0.0.tgz",
      "integrity": "sha512-eKLdI5v9m67kbXQbJSNn1zjh0SDzvzWVWtX+qEI3eMjZw8daH9k8rlj1FZY9memPwjiskQFbe7vHVVJIAqoEhw==",
      "requires": {
        "domelementtype": "^2.0.1"
      },
      "dependencies": {
        "domelementtype": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-2.0.1.tgz",
          "integrity": "sha512-5HOHUDsYZWV8FGWN0Njbr/Rn7f/eWSQi1v7+HsUVwXgn8nWWlL64zKDkS0n8ZmQ3mlWOMuXOnR+7Nx/5tMO5AQ=="
        }
      }
    },
    "domutils": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/domutils/-/domutils-2.0.0.tgz",
      "integrity": "sha512-n5SelJ1axbO636c2yUtOGia/IcJtVtlhQbFiVDBZHKV5ReJO1ViX7sFEemtuyoAnBxk5meNSYgA8V4s0271efg==",
      "requires": {
        "dom-serializer": "^0.2.1",
        "domelementtype": "^2.0.1",
        "domhandler": "^3.0.0"
      },
      "dependencies": {
        "domelementtype": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-2.0.1.tgz",
          "integrity": "sha512-5HOHUDsYZWV8FGWN0Njbr/Rn7f/eWSQi1v7+HsUVwXgn8nWWlL64zKDkS0n8ZmQ3mlWOMuXOnR+7Nx/5tMO5AQ=="
        }
      }
    },
    "dot-prop": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/dot-prop/-/dot-prop-5.2.0.tgz",
      "integrity": "sha512-uEUyaDKoSQ1M4Oq8l45hSE26SnTxL6snNnqvK/VWx5wJhmff5z0FUVJDKDanor/6w3kzE3i7XZOk+7wC0EXr1A==",
      "requires": {
        "is-obj": "^2.0.0"
      }
    },
    "duplexify": {
      "version": "3.7.1",
      "resolved": "https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz",
      "integrity": "sha512-07z8uv2wMyS51kKhD1KsdXJg5WQ6t93RneqRxUHnskXVtlYYkLqM0gqStQZ3pj073g687jPCHrqNfCzawLYh5g==",
      "requires": {
        "end-of-stream": "^1.0.0",
        "inherits": "^2.0.1",
        "readable-stream": "^2.0.0",
        "stream-shift": "^1.0.0"
      }
    },
    "electron-to-chromium": {
      "version": "1.3.540",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.540.tgz",
      "integrity": "sha512-IoGiZb8SMqTtkDYJtP8EtCdvv3VMtd1QoTlypO2RUBxRq/Wk0rU5IzhzhMckPaC9XxDqUvWsL0XKOBhTiYVN3w=="
    },
    "elliptic": {
      "version": "6.5.3",
      "resolved": "https://registry.npmjs.org/elliptic/-/elliptic-6.5.3.tgz",
      "integrity": "sha512-IMqzv5wNQf+E6aHeIqATs0tOLeOTwj1QKbRcS3jBbYkl5oLAserA8yJTT7/VyHUYG91PRmPyeQDObKLPpeS4dw==",
      "requires": {
        "bn.js": "^4.4.0",
        "brorand": "^1.0.1",
        "hash.js": "^1.0.0",
        "hmac-drbg": "^1.0.0",
        "inherits": "^2.0.1",
        "minimalistic-assert": "^1.0.0",
        "minimalistic-crypto-utils": "^1.0.0"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "emojis-list": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/emojis-list/-/emojis-list-3.0.0.tgz",
      "integrity": "sha512-/kyM18EfinwXZbno9FyUGeFh87KC8HRQBQGildHZbEuRyWFOmv1U10o9BBp8XVZDVNNuQKyIGIu5ZYAAXJ0V2Q=="
    },
    "end-of-stream": {
      "version": "1.4.4",
      "resolved": "https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz",
      "integrity": "sha512-+uw1inIHVPQoaVuHzRyXd21icM+cnt4CzD5rW+NC1wjOUSTOs+Te7FOv7AhN7vS9x/oIyhLP5PR1H+phQAHu5Q==",
      "requires": {
        "once": "^1.4.0"
      }
    },
    "enhanced-resolve": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-4.3.0.tgz",
      "integrity": "sha512-3e87LvavsdxyoCfGusJnrZ5G8SLPOFeHSNpZI/ATL9a5leXo2k0w6MKnbqhdBad9qTobSfB20Ld7UmgoNbAZkQ==",
      "requires": {
        "graceful-fs": "^4.1.2",
        "memory-fs": "^0.5.0",
        "tapable": "^1.0.0"
      },
      "dependencies": {
        "memory-fs": {
          "version": "0.5.0",
          "resolved": "https://registry.npmjs.org/memory-fs/-/memory-fs-0.5.0.tgz",
          "integrity": "sha512-jA0rdU5KoQMC0e6ppoNRtpp6vjFq6+NY7r8hywnC7V+1Xj/MtHwGIbB1QaK/dunyjWteJzmkpd7ooeWg10T7GA==",
          "requires": {
            "errno": "^0.1.3",
            "readable-stream": "^2.0.1"
          }
        }
      }
    },
    "entities": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/entities/-/entities-2.0.3.tgz",
      "integrity": "sha512-MyoZ0jgnLvB2X3Lg5HqpFmn1kybDiIfEQmKzTb5apr51Rb+T3KdmMiqa70T+bhGnyv7bQ6WMj2QMHpGMmlrUYQ=="
    },
    "errno": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/errno/-/errno-0.1.7.tgz",
      "integrity": "sha512-MfrRBDWzIWifgq6tJj60gkAwtLNb6sQPlcFrSOflcP1aFmmruKQ2wRnze/8V6kgyz7H3FF8Npzv78mZ7XLLflg==",
      "requires": {
        "prr": "~1.0.1"
      }
    },
    "error-ex": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz",
      "integrity": "sha512-7dFHNmqeFSEt2ZBsCriorKnn3Z2pj+fd9kmI6QoWw4//DL+icEBfc0U7qJCisqrTsKTjw4fNFy2pW9OqStD84g==",
      "requires": {
        "is-arrayish": "^0.2.1"
      }
    },
    "es-abstract": {
      "version": "1.17.6",
      "resolved": "https://registry.npmjs.org/es-abstract/-/es-abstract-1.17.6.tgz",
      "integrity": "sha512-Fr89bON3WFyUi5EvAeI48QTWX0AyekGgLA8H+c+7fbfCkJwRWRMLd8CQedNEyJuoYYhmtEqY92pgte1FAhBlhw==",
      "requires": {
        "es-to-primitive": "^1.2.1",
        "function-bind": "^1.1.1",
        "has": "^1.0.3",
        "has-symbols": "^1.0.1",
        "is-callable": "^1.2.0",
        "is-regex": "^1.1.0",
        "object-inspect": "^1.7.0",
        "object-keys": "^1.1.1",
        "object.assign": "^4.1.0",
        "string.prototype.trimend": "^1.0.1",
        "string.prototype.trimstart": "^1.0.1"
      }
    },
    "es-to-primitive": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.2.1.tgz",
      "integrity": "sha512-QCOllgZJtaUo9miYBcLChTUaHNjJF3PYs1VidD7AwiEj1kYxKeQTctLAezAOH5ZKRH0g2IgPn6KwB4IT8iRpvA==",
      "requires": {
        "is-callable": "^1.1.4",
        "is-date-object": "^1.0.1",
        "is-symbol": "^1.0.2"
      }
    },
    "es5-ext": {
      "version": "0.10.53",
      "resolved": "https://registry.npmjs.org/es5-ext/-/es5-ext-0.10.53.tgz",
      "integrity": "sha512-Xs2Stw6NiNHWypzRTY1MtaG/uJlwCk8kH81920ma8mvN8Xq1gsfhZvpkImLQArw8AHnv8MT2I45J3c0R8slE+Q==",
      "requires": {
        "es6-iterator": "~2.0.3",
        "es6-symbol": "~3.1.3",
        "next-tick": "~1.0.0"
      }
    },
    "es6-iterator": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.3.tgz",
      "integrity": "sha1-p96IkUGgWpSwhUQDstCg+/qY87c=",
      "requires": {
        "d": "1",
        "es5-ext": "^0.10.35",
        "es6-symbol": "^3.1.1"
      }
    },
    "es6-symbol": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.3.tgz",
      "integrity": "sha512-NJ6Yn3FuDinBaBRWl/q5X/s4koRHBrgKAu+yGI6JCBeiu3qrcbJhwT2GeR/EXVfylRk8dpQVJoLEFhK+Mu31NA==",
      "requires": {
        "d": "^1.0.1",
        "ext": "^1.1.2"
      }
    },
    "escalade": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.0.2.tgz",
      "integrity": "sha512-gPYAU37hYCUhW5euPeR+Y74F7BL+IBsV93j5cvGriSaD1aG6MGsqsV1yamRdrWrb2j3aiZvb0X+UBOWpx3JWtQ=="
    },
    "escape-string-regexp": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz",
      "integrity": "sha1-G2HAViGQqN/2rjuyzwIAyhMLhtQ="
    },
    "eslint-scope": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/eslint-scope/-/eslint-scope-4.0.3.tgz",
      "integrity": "sha512-p7VutNr1O/QrxysMo3E45FjYDTeXBy0iTltPFNSqKAIfjDSXC+4dj+qfyuD8bfAXrW/y6lW3O76VaYNPKfpKrg==",
      "requires": {
        "esrecurse": "^4.1.0",
        "estraverse": "^4.1.1"
      }
    },
    "esprima": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz",
      "integrity": "sha512-eGuFFw7Upda+g4p+QHvnW0RyTX/SVeJBDM/gCtMARO0cLuT2HcEKnTPvhjV6aGeqrCB/sbNop0Kszm0jsaWU4A=="
    },
    "esrecurse": {
      "version": "4.2.1",
      "resolved": "https://registry.npmjs.org/esrecurse/-/esrecurse-4.2.1.tgz",
      "integrity": "sha512-64RBB++fIOAXPw3P9cy89qfMlvZEXZkqqJkjqqXIvzP5ezRZjW+lPWjw35UX/3EhUPFYbg5ER4JYgDw4007/DQ==",
      "requires": {
        "estraverse": "^4.1.0"
      }
    },
    "estraverse": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz",
      "integrity": "sha512-39nnKffWz8xN1BU/2c79n9nB9HDzo0niYUqx6xyqUnyoAnQyyWpOTdZEeiCch8BBu515t4wp9ZmgVfVhn9EBpw=="
    },
    "esutils": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz",
      "integrity": "sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g=="
    },
    "events": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/events/-/events-3.2.0.tgz",
      "integrity": "sha512-/46HWwbfCX2xTawVfkKLGxMifJYQBWMwY1mjywRtb4c9x8l5NP3KoJtnIOiL1hfdRkIuYhETxQlo62IF8tcnlg=="
    },
    "evp_bytestokey": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/evp_bytestokey/-/evp_bytestokey-1.0.3.tgz",
      "integrity": "sha512-/f2Go4TognH/KvCISP7OUsHn85hT9nUkxxA9BEWxFn+Oj9o8ZNLm/40hdlgSLyuOimsrTKLUMEorQexp/aPQeA==",
      "requires": {
        "md5.js": "^1.3.4",
        "safe-buffer": "^5.1.1"
      }
    },
    "expand-brackets": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/expand-brackets/-/expand-brackets-2.1.4.tgz",
      "integrity": "sha1-t3c14xXOMPa27/D4OwQVGiJEliI=",
      "requires": {
        "debug": "^2.3.3",
        "define-property": "^0.2.5",
        "extend-shallow": "^2.0.1",
        "posix-character-classes": "^0.1.0",
        "regex-not": "^1.0.0",
        "snapdragon": "^0.8.1",
        "to-regex": "^3.0.1"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "define-property": {
          "version": "0.2.5",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz",
          "integrity": "sha1-w1se+RjsPJkPmlvFe+BKrOxcgRY=",
          "requires": {
            "is-descriptor": "^0.1.0"
          }
        },
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "requires": {
            "is-extendable": "^0.1.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        }
      }
    },
    "ext": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/ext/-/ext-1.4.0.tgz",
      "integrity": "sha512-Key5NIsUxdqKg3vIsdw9dSuXpPCQ297y6wBjL30edxwPgt2E44WcWBZey/ZvUc6sERLTxKdyCu4gZFmUbk1Q7A==",
      "requires": {
        "type": "^2.0.0"
      },
      "dependencies": {
        "type": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/type/-/type-2.1.0.tgz",
          "integrity": "sha512-G9absDWvhAWCV2gmF1zKud3OyC61nZDwWvBL2DApaVFogI07CprggiQAOOjvp2NRjYWFzPyu7vwtDrQFq8jeSA=="
        }
      }
    },
    "extend": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.2.tgz",
      "integrity": "sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g=="
    },
    "extend-shallow": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-3.0.2.tgz",
      "integrity": "sha1-Jqcarwc7OfshJxcnRhMcJwQCjbg=",
      "requires": {
        "assign-symbols": "^1.0.0",
        "is-extendable": "^1.0.1"
      },
      "dependencies": {
        "is-extendable": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-1.0.1.tgz",
          "integrity": "sha512-arnXMxT1hhoKo9k1LZdmlNyJdDDfy2v0fXjFlmok4+i8ul/6WlbVge9bhM74OpNPQPMGUToDtz+KXa1PneJxOA==",
          "requires": {
            "is-plain-object": "^2.0.4"
          }
        }
      }
    },
    "extglob": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/extglob/-/extglob-2.0.4.tgz",
      "integrity": "sha512-Nmb6QXkELsuBr24CJSkilo6UHHgbekK5UiZgfE6UHD3Eb27YC6oD+bhcT+tJ6cl8dmsgdQxnWlcry8ksBIBLpw==",
      "requires": {
        "array-unique": "^0.3.2",
        "define-property": "^1.0.0",
        "expand-brackets": "^2.1.4",
        "extend-shallow": "^2.0.1",
        "fragment-cache": "^0.2.1",
        "regex-not": "^1.0.0",
        "snapdragon": "^0.8.1",
        "to-regex": "^3.0.1"
      },
      "dependencies": {
        "define-property": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz",
          "integrity": "sha1-dp66rz9KY6rTr56NMEybvnm/sOY=",
          "requires": {
            "is-descriptor": "^1.0.0"
          }
        },
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "requires": {
            "is-extendable": "^0.1.0"
          }
        },
        "is-accessor-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz",
          "integrity": "sha512-m5hnHTkcVsPfqx3AKlyttIPb7J+XykHvJP2B9bZDjlhLIoEq4XoK64Vg7boZlVWYK6LUY94dYPEE7Lh0ZkZKcQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-data-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz",
          "integrity": "sha512-jbRXy1FmtAoCjQkVmIVYwuuqDFUbaOeDjmed1tOGPrsMhtJA4rD9tkgA0F1qJ3gRFRXcHYVkdeaP50Q5rE/jLQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-descriptor": {
          "version": "1.0.2",
          "resolved": "https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz",
          "integrity": "sha512-2eis5WqQGV7peooDyLmNEPUrps9+SXX5c9pL3xEB+4e9HnGuDa7mB7kHxHw4CbqS9k1T2hOH3miL8n8WtiYVtg==",
          "requires": {
            "is-accessor-descriptor": "^1.0.0",
            "is-data-descriptor": "^1.0.0",
            "kind-of": "^6.0.2"
          }
        }
      }
    },
    "fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q=="
    },
    "fast-json-stable-stringify": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
      "integrity": "sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw=="
    },
    "figgy-pudding": {
      "version": "3.5.2",
      "resolved": "https://registry.npmjs.org/figgy-pudding/-/figgy-pudding-3.5.2.tgz",
      "integrity": "sha512-0btnI/H8f2pavGMN8w40mlSKOfTK2SVJmBfBeVIj3kNw0swwgzyRq0d5TJVOwodFmtvpPeWPN/MCcfuWF0Ezbw=="
    },
    "fill-range": {
      "version": "7.0.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.0.1.tgz",
      "integrity": "sha512-qOo9F+dMUmC2Lcb4BbVvnKJxTPjCm+RRpe4gDuGrzkL7mEVl/djYSu2OdQ2Pa302N4oqkSg9ir6jaLWJ2USVpQ==",
      "requires": {
        "to-regex-range": "^5.0.1"
      }
    },
    "find-cache-dir": {
      "version": "3.3.1",
      "resolved": "https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-3.3.1.tgz",
      "integrity": "sha512-t2GDMt3oGC/v+BMwzmllWDuJF/xcDtE5j/fCGbqDD7OLuJkj0cfh1YSA5VKPvwMeLFLNDBkwOKZ2X85jGLVftQ==",
      "requires": {
        "commondir": "^1.0.1",
        "make-dir": "^3.0.2",
        "pkg-dir": "^4.1.0"
      }
    },
    "find-up": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz",
      "integrity": "sha512-PpOwAdQ/YlXQ2vj8a3h8IipDuYRi3wceVQQGYWxNINccq40Anw7BlsEXCMbt1Zt+OLA6Fq9suIpIWD0OsnISlw==",
      "requires": {
        "locate-path": "^5.0.0",
        "path-exists": "^4.0.0"
      }
    },
    "flush-write-stream": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/flush-write-stream/-/flush-write-stream-1.1.1.tgz",
      "integrity": "sha512-3Z4XhFZ3992uIq0XOqb9AreonueSYphE6oYbpt5+3u06JWklbsPkNv3ZKkP9Bz/r+1MWCaMoSQ28P85+1Yc77w==",
      "requires": {
        "inherits": "^2.0.3",
        "readable-stream": "^2.3.6"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "for-in": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz",
      "integrity": "sha1-gQaNKVqBQuwKxybG4iAMMPttXoA="
    },
    "fork-ts-checker-webpack-plugin": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/fork-ts-checker-webpack-plugin/-/fork-ts-checker-webpack-plugin-3.1.1.tgz",
      "integrity": "sha512-DuVkPNrM12jR41KM2e+N+styka0EgLkTnXmNcXdgOM37vtGeY+oCBK/Jx0hzSeEU6memFCtWb4htrHPMDfwwUQ==",
      "requires": {
        "babel-code-frame": "^6.22.0",
        "chalk": "^2.4.1",
        "chokidar": "^3.3.0",
        "micromatch": "^3.1.10",
        "minimatch": "^3.0.4",
        "semver": "^5.6.0",
        "tapable": "^1.0.0",
        "worker-rpc": "^0.1.0"
      }
    },
    "fragment-cache": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/fragment-cache/-/fragment-cache-0.2.1.tgz",
      "integrity": "sha1-QpD60n8T6Jvn8zeZxrxaCr//DRk=",
      "requires": {
        "map-cache": "^0.2.2"
      }
    },
    "from2": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/from2/-/from2-2.3.0.tgz",
      "integrity": "sha1-i/tVAr3kpNNs/e6gB/zKIdfjgq8=",
      "requires": {
        "inherits": "^2.0.1",
        "readable-stream": "^2.0.0"
      }
    },
    "fs-write-stream-atomic": {
      "version": "1.0.10",
      "resolved": "https://registry.npmjs.org/fs-write-stream-atomic/-/fs-write-stream-atomic-1.0.10.tgz",
      "integrity": "sha1-tH31NJPvkR33VzHnCp3tAYnbQMk=",
      "requires": {
        "graceful-fs": "^4.1.2",
        "iferr": "^0.1.5",
        "imurmurhash": "^0.1.4",
        "readable-stream": "1 || 2"
      }
    },
    "fs.realpath": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz",
      "integrity": "sha1-FQStJSMVjKpA20onh8sBQRmU6k8="
    },
    "fsevents": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.1.3.tgz",
      "integrity": "sha512-Auw9a4AxqWpa9GUfj370BMPzzyncfBABW8Mab7BGWBYDj4Isgq+cDKtx0i6u9jcX9pQDnswsaaOTgTmA5pEjuQ==",
      "optional": true
    },
    "function-bind": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz",
      "integrity": "sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A=="
    },
    "get-value": {
      "version": "2.0.6",
      "resolved": "https://registry.npmjs.org/get-value/-/get-value-2.0.6.tgz",
      "integrity": "sha1-3BXKHGcjh8p2vTesCjlbogQqLCg="
    },
    "glob": {
      "version": "7.1.6",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.6.tgz",
      "integrity": "sha512-LwaxwyZ72Lk7vZINtNNrywX0ZuLyStrdDtabefZKAY5ZGJhVtgdznluResxNmPitE0SAO+O26sWTHeKSI2wMBA==",
      "requires": {
        "fs.realpath": "^1.0.0",
        "inflight": "^1.0.4",
        "inherits": "2",
        "minimatch": "^3.0.4",
        "once": "^1.3.0",
        "path-is-absolute": "^1.0.0"
      }
    },
    "glob-parent": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.1.tgz",
      "integrity": "sha512-FnI+VGOpnlGHWZxthPGR+QhR78fuiK0sNLkHQv+bL9fQi57lNNdquIbna/WrfROrolq8GK5Ek6BiMwqL/voRYQ==",
      "requires": {
        "is-glob": "^4.0.1"
      }
    },
    "glob-to-regexp": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/glob-to-regexp/-/glob-to-regexp-0.4.1.tgz",
      "integrity": "sha512-lkX1HJXwyMcprw/5YUZc2s7DrpAiHB21/V+E1rHUrVNokkvB6bqMzT0VfV6/86ZNabt1k14YOIaT7nDvOX3Iiw=="
    },
    "globals": {
      "version": "11.12.0",
      "resolved": "https://registry.npmjs.org/globals/-/globals-11.12.0.tgz",
      "integrity": "sha512-WOBp/EEGUiIsJSp7wcv/y6MO+lV9UoncWqxuFfm8eBwzWNgyfBd6Gz+IeKQ9jCmyhoH99g15M3T+QaVHFjizVA=="
    },
    "graceful-fs": {
      "version": "4.2.4",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.4.tgz",
      "integrity": "sha512-WjKPNJF79dtJAVniUlGGWHYGz2jWxT6VhN/4m1NdkbZ2nOsEF+cI1Edgql5zCRhs/VsQYRvrXctxktVXZUkixw=="
    },
    "gray-matter": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/gray-matter/-/gray-matter-4.0.2.tgz",
      "integrity": "sha512-7hB/+LxrOjq/dd8APlK0r24uL/67w7SkYnfwhNFwg/VDIGWGmduTDYf3WNstLW2fbbmRwrDGCVSJ2isuf2+4Hw==",
      "requires": {
        "js-yaml": "^3.11.0",
        "kind-of": "^6.0.2",
        "section-matter": "^1.0.0",
        "strip-bom-string": "^1.0.0"
      }
    },
    "has": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/has/-/has-1.0.3.tgz",
      "integrity": "sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==",
      "requires": {
        "function-bind": "^1.1.1"
      }
    },
    "has-ansi": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz",
      "integrity": "sha1-NPUEnOHs3ysGSa8+8k5F7TVBbZE=",
      "requires": {
        "ansi-regex": "^2.0.0"
      }
    },
    "has-flag": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz",
      "integrity": "sha1-tdRU3CGZriJWmfNGfloH87lVuv0="
    },
    "has-symbols": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.1.tgz",
      "integrity": "sha512-PLcsoqu++dmEIZB+6totNFKq/7Do+Z0u4oT0zKOJNl3lYK6vGwwu2hjHs+68OEZbTjiUE9bgOABXbP/GvrS0Kg=="
    },
    "has-value": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/has-value/-/has-value-1.0.0.tgz",
      "integrity": "sha1-GLKB2lhbHFxR3vJMkw7SmgvmsXc=",
      "requires": {
        "get-value": "^2.0.6",
        "has-values": "^1.0.0",
        "isobject": "^3.0.0"
      }
    },
    "has-values": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/has-values/-/has-values-1.0.0.tgz",
      "integrity": "sha1-lbC2P+whRmGab+V/51Yo1aOe/k8=",
      "requires": {
        "is-number": "^3.0.0",
        "kind-of": "^4.0.0"
      },
      "dependencies": {
        "is-number": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz",
          "integrity": "sha1-JP1iAaR4LPUFYcgQJ2r8fRLXEZU=",
          "requires": {
            "kind-of": "^3.0.2"
          },
          "dependencies": {
            "kind-of": {
              "version": "3.2.2",
              "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
              "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
              "requires": {
                "is-buffer": "^1.1.5"
              }
            }
          }
        },
        "kind-of": {
          "version": "4.0.0",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz",
          "integrity": "sha1-IIE989cSkosgc3hpGkUGb65y3Vc=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "hash-base": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/hash-base/-/hash-base-3.1.0.tgz",
      "integrity": "sha512-1nmYp/rhMDiE7AYkDw+lLwlAzz0AntGIe51F3RfFfEqyQ3feY2eI/NcwC6umIQVOASPMsWJLJScWKSSvzL9IVA==",
      "requires": {
        "inherits": "^2.0.4",
        "readable-stream": "^3.6.0",
        "safe-buffer": "^5.2.0"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        },
        "readable-stream": {
          "version": "3.6.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.0.tgz",
          "integrity": "sha512-BViHy7LKeTz4oNnkcLJ+lVSL6vpiFeX6/d3oSH8zCW7UxP2onchk+vTGB143xuFjHS3deTgkKoXXymXqymiIdA==",
          "requires": {
            "inherits": "^2.0.3",
            "string_decoder": "^1.1.1",
            "util-deprecate": "^1.0.1"
          }
        },
        "safe-buffer": {
          "version": "5.2.1",
          "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
          "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ=="
        }
      }
    },
    "hash.js": {
      "version": "1.1.7",
      "resolved": "https://registry.npmjs.org/hash.js/-/hash.js-1.1.7.tgz",
      "integrity": "sha512-taOaskGt4z4SOANNseOviYDvjEJinIkRgmp7LbKP2YTTmVxWBl87s/uzK9r+44BclBSp2X7K1hqeNfz9JbBeXA==",
      "requires": {
        "inherits": "^2.0.3",
        "minimalistic-assert": "^1.0.1"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "hast-util-is-element": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/hast-util-is-element/-/hast-util-is-element-1.1.0.tgz",
      "integrity": "sha512-oUmNua0bFbdrD/ELDSSEadRVtWZOf3iF6Lbv81naqsIV99RnSCieTbWuWCY8BAeEfKJTKl0gRdokv+dELutHGQ=="
    },
    "hast-util-sanitize": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/hast-util-sanitize/-/hast-util-sanitize-3.0.0.tgz",
      "integrity": "sha512-gxsM24ARtuulsrWEj8QtVM6FNeAEHklF/t7TEIWvX1wuQcoAQtJtEUcT8t0os4uxCUqh1epX/gTi8fp8gNKvCA==",
      "requires": {
        "xtend": "^4.0.0"
      }
    },
    "hast-util-to-html": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/hast-util-to-html/-/hast-util-to-html-7.1.1.tgz",
      "integrity": "sha512-Ujqj0hGuo3dIQKilkbauAv5teOqPvhaSLEgs1lgApFT0812e114KiffV8XfE4ttR8dRPqxNOIJOMu6SKOVOGlg==",
      "requires": {
        "ccount": "^1.0.0",
        "comma-separated-tokens": "^1.0.0",
        "hast-util-is-element": "^1.0.0",
        "hast-util-whitespace": "^1.0.0",
        "html-void-elements": "^1.0.0",
        "property-information": "^5.0.0",
        "space-separated-tokens": "^1.0.0",
        "stringify-entities": "^3.0.1",
        "unist-util-is": "^4.0.0",
        "xtend": "^4.0.0"
      }
    },
    "hast-util-whitespace": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/hast-util-whitespace/-/hast-util-whitespace-1.0.4.tgz",
      "integrity": "sha512-I5GTdSfhYfAPNztx2xJRQpG8cuDSNt599/7YUn7Gx/WxNMsG+a835k97TDkFgk123cwjfwINaZknkKkphx/f2A=="
    },
    "hex-color-regex": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/hex-color-regex/-/hex-color-regex-1.1.0.tgz",
      "integrity": "sha512-l9sfDFsuqtOqKDsQdqrMRk0U85RZc0RtOR9yPI7mRVOa4FsR/BVnZ0shmQRM96Ji99kYZP/7hn1cedc1+ApsTQ=="
    },
    "hmac-drbg": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/hmac-drbg/-/hmac-drbg-1.0.1.tgz",
      "integrity": "sha1-0nRXAQJabHdabFRXk+1QL8DGSaE=",
      "requires": {
        "hash.js": "^1.0.3",
        "minimalistic-assert": "^1.0.0",
        "minimalistic-crypto-utils": "^1.0.1"
      }
    },
    "hsl-regex": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/hsl-regex/-/hsl-regex-1.0.0.tgz",
      "integrity": "sha1-1JMwx4ntgZ4nakwNJy3/owsY/m4="
    },
    "hsla-regex": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/hsla-regex/-/hsla-regex-1.0.0.tgz",
      "integrity": "sha1-wc56MWjIxmFAM6S194d/OyJfnDg="
    },
    "html-comment-regex": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/html-comment-regex/-/html-comment-regex-1.1.2.tgz",
      "integrity": "sha512-P+M65QY2JQ5Y0G9KKdlDpo0zK+/OHptU5AaBwUfAIDJZk1MYf32Frm84EcOytfJE0t5JvkAnKlmjsXDnWzCJmQ=="
    },
    "html-void-elements": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/html-void-elements/-/html-void-elements-1.0.5.tgz",
      "integrity": "sha512-uE/TxKuyNIcx44cIWnjr/rfIATDH7ZaOMmstu0CwhFG1Dunhlp4OC6/NMbhiwoq5BpW0ubi303qnEk/PZj614w=="
    },
    "htmlparser2": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/htmlparser2/-/htmlparser2-4.1.0.tgz",
      "integrity": "sha512-4zDq1a1zhE4gQso/c5LP1OtrhYTncXNSpvJYtWJBtXAETPlMfi3IFNjGuQbYLuVY4ZR0QMqRVvo4Pdy9KLyP8Q==",
      "requires": {
        "domelementtype": "^2.0.1",
        "domhandler": "^3.0.0",
        "domutils": "^2.0.0",
        "entities": "^2.0.0"
      },
      "dependencies": {
        "domelementtype": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-2.0.1.tgz",
          "integrity": "sha512-5HOHUDsYZWV8FGWN0Njbr/Rn7f/eWSQi1v7+HsUVwXgn8nWWlL64zKDkS0n8ZmQ3mlWOMuXOnR+7Nx/5tMO5AQ=="
        }
      }
    },
    "https-browserify": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/https-browserify/-/https-browserify-1.0.0.tgz",
      "integrity": "sha1-7AbBDgo0wPL68Zn3/X/Hj//QPHM="
    },
    "icss-utils": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/icss-utils/-/icss-utils-4.1.1.tgz",
      "integrity": "sha512-4aFq7wvWyMHKgxsH8QQtGpvbASCf+eM3wPRLI6R+MgAnTCZ6STYsRvttLvRWK0Nfif5piF394St3HeJDaljGPA==",
      "requires": {
        "postcss": "^7.0.14"
      }
    },
    "ieee754": {
      "version": "1.1.13",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.1.13.tgz",
      "integrity": "sha512-4vf7I2LYV/HaWerSo3XmlMkp5eZ83i+/CDluXi/IGTs/O1sejBNhTtnxzmRZfvOUqj7lZjqHkeTvpgSFDlWZTg=="
    },
    "iferr": {
      "version": "0.1.5",
      "resolved": "https://registry.npmjs.org/iferr/-/iferr-0.1.5.tgz",
      "integrity": "sha1-xg7taebY/bazEEofy8ocGS3FtQE="
    },
    "import-fresh": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/import-fresh/-/import-fresh-2.0.0.tgz",
      "integrity": "sha1-2BNVwVYS04bGH53dOSLUMEgipUY=",
      "requires": {
        "caller-path": "^2.0.0",
        "resolve-from": "^3.0.0"
      }
    },
    "imurmurhash": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz",
      "integrity": "sha1-khi5srkoojixPcT7a21XbyMUU+o="
    },
    "indexes-of": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/indexes-of/-/indexes-of-1.0.1.tgz",
      "integrity": "sha1-8w9xbI4r00bHtn0985FVZqfAVgc="
    },
    "infer-owner": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/infer-owner/-/infer-owner-1.0.4.tgz",
      "integrity": "sha512-IClj+Xz94+d7irH5qRyfJonOdfTzuDaifE6ZPWfx0N0+/ATZCbuTPq2prFl526urkQd90WyUKIh1DfBQ2hMz9A=="
    },
    "inflight": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz",
      "integrity": "sha1-Sb1jMdfQLQwJvJEKEHW6gWW1bfk=",
      "requires": {
        "once": "^1.3.0",
        "wrappy": "1"
      }
    },
    "inherits": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.1.tgz",
      "integrity": "sha1-sX0I0ya0Qj5Wjv9xn5GwscvfafE="
    },
    "invariant": {
      "version": "2.2.4",
      "resolved": "https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz",
      "integrity": "sha512-phJfQVBuaJM5raOpJjSfkiD6BpbCE4Ns//LaXl6wGYtUBY83nWS6Rf9tXm2e8VaK60JEjYldbPif/A2B1C2gNA==",
      "requires": {
        "loose-envify": "^1.0.0"
      }
    },
    "is-absolute-url": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-absolute-url/-/is-absolute-url-2.1.0.tgz",
      "integrity": "sha1-UFMN+4T8yap9vnhS6Do3uTufKqY="
    },
    "is-accessor-descriptor": {
      "version": "0.1.6",
      "resolved": "https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-0.1.6.tgz",
      "integrity": "sha1-qeEss66Nh2cn7u84Q/igiXtcmNY=",
      "requires": {
        "kind-of": "^3.0.2"
      },
      "dependencies": {
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "is-alphabetical": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-alphabetical/-/is-alphabetical-1.0.4.tgz",
      "integrity": "sha512-DwzsA04LQ10FHTZuL0/grVDk4rFoVH1pjAToYwBrHSxcrBIGQuXrQMtD5U1b0U2XVgKZCTLLP8u2Qxqhy3l2Vg=="
    },
    "is-alphanumeric": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/is-alphanumeric/-/is-alphanumeric-1.0.0.tgz",
      "integrity": "sha1-Spzvcdr0wAHB2B1j0UDPU/1oifQ="
    },
    "is-alphanumerical": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-alphanumerical/-/is-alphanumerical-1.0.4.tgz",
      "integrity": "sha512-UzoZUr+XfVz3t3v4KyGEniVL9BDRoQtY7tOyrRybkVNjDFWyo1yhXNGrrBTQxp3ib9BLAWs7k2YKBQsFRkZG9A==",
      "requires": {
        "is-alphabetical": "^1.0.0",
        "is-decimal": "^1.0.0"
      }
    },
    "is-arrayish": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz",
      "integrity": "sha1-d8mYQFJ6qOyxqLppe4BkWnqSap0="
    },
    "is-binary-path": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
      "integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
      "requires": {
        "binary-extensions": "^2.0.0"
      }
    },
    "is-buffer": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz",
      "integrity": "sha512-NcdALwpXkTm5Zvvbk7owOUSvVvBKDgKP5/ewfXEznmQFfs4ZRmanOeKBTjRVjka3QFoN6XJ+9F3USqfHqTaU5w=="
    },
    "is-callable": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/is-callable/-/is-callable-1.2.0.tgz",
      "integrity": "sha512-pyVD9AaGLxtg6srb2Ng6ynWJqkHU9bEM087AKck0w8QwDarTfNcpIYoU8x8Hv2Icm8u6kFJM18Dag8lyqGkviw=="
    },
    "is-color-stop": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-color-stop/-/is-color-stop-1.1.0.tgz",
      "integrity": "sha1-z/9HGu5N1cnhWFmPvhKWe1za00U=",
      "requires": {
        "css-color-names": "^0.0.4",
        "hex-color-regex": "^1.1.0",
        "hsl-regex": "^1.0.0",
        "hsla-regex": "^1.0.0",
        "rgb-regex": "^1.0.1",
        "rgba-regex": "^1.0.0"
      }
    },
    "is-data-descriptor": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-0.1.4.tgz",
      "integrity": "sha1-C17mSDiOLIYCgueT8YVv7D8wG1Y=",
      "requires": {
        "kind-of": "^3.0.2"
      },
      "dependencies": {
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "is-date-object": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.2.tgz",
      "integrity": "sha512-USlDT524woQ08aoZFzh3/Z6ch9Y/EWXEHQ/AaRN0SkKq4t2Jw2R2339tSXmwuVoY7LLlBCbOIlx2myP/L5zk0g=="
    },
    "is-decimal": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-decimal/-/is-decimal-1.0.4.tgz",
      "integrity": "sha512-RGdriMmQQvZ2aqaQq3awNA6dCGtKpiDFcOzrTWrDAT2MiWrKQVPmxLGHl7Y2nNu6led0kEyoX0enY0qXYsv9zw=="
    },
    "is-descriptor": {
      "version": "0.1.6",
      "resolved": "https://registry.npmjs.org/is-descriptor/-/is-descriptor-0.1.6.tgz",
      "integrity": "sha512-avDYr0SB3DwO9zsMov0gKCESFYqCnE4hq/4z3TdUlukEy5t9C0YRq7HLrsN52NAcqXKaepeCD0n+B0arnVG3Hg==",
      "requires": {
        "is-accessor-descriptor": "^0.1.6",
        "is-data-descriptor": "^0.1.4",
        "kind-of": "^5.0.0"
      },
      "dependencies": {
        "kind-of": {
          "version": "5.1.0",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-5.1.0.tgz",
          "integrity": "sha512-NGEErnH6F2vUuXDh+OlbcKW7/wOcfdRHaZ7VWtqCztfHri/++YKmP51OdWeGPuqCOba6kk2OTe5d02VmTB80Pw=="
        }
      }
    },
    "is-directory": {
      "version": "0.3.1",
      "resolved": "https://registry.npmjs.org/is-directory/-/is-directory-0.3.1.tgz",
      "integrity": "sha1-YTObbyR1/Hcv2cnYP1yFddwVSuE="
    },
    "is-extendable": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz",
      "integrity": "sha1-YrEQ4omkcUGOPsNqYX1HLjAd/Ik="
    },
    "is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha1-qIwCU1eR8C7TfHahueqXc8gz+MI="
    },
    "is-glob": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.1.tgz",
      "integrity": "sha512-5G0tKtBTFImOqDnLB2hG6Bp2qcKEFduo4tZu9MT/H6NQv/ghhy30o55ufafxJ/LdH79LLs2Kfrn85TLKyA7BUg==",
      "requires": {
        "is-extglob": "^2.1.1"
      }
    },
    "is-hexadecimal": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-hexadecimal/-/is-hexadecimal-1.0.4.tgz",
      "integrity": "sha512-gyPJuv83bHMpocVYoqof5VDiZveEoGoFL8m3BXNb2VW8Xs+rz9kqO8LOQ5DH6EsuvilT1ApazU0pyl+ytbPtlw=="
    },
    "is-number": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
      "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng=="
    },
    "is-obj": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/is-obj/-/is-obj-2.0.0.tgz",
      "integrity": "sha512-drqDG3cbczxxEJRoOXcOjtdp1J/lyp1mNn0xaznRs8+muBhgQcrnbspox5X5fOw0HnMnbfDzvnEMEtqDEJEo8w=="
    },
    "is-plain-obj": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz",
      "integrity": "sha1-caUMhCnfync8kqOQpKA7OfzVHT4="
    },
    "is-plain-object": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz",
      "integrity": "sha512-h5PpgXkWitc38BBMYawTYMWJHFZJVnBquFE57xFpjB8pJFiF6gZ+bU+WyI/yqXiFR5mdLsgYNaPe8uao6Uv9Og==",
      "requires": {
        "isobject": "^3.0.1"
      }
    },
    "is-regex": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/is-regex/-/is-regex-1.1.1.tgz",
      "integrity": "sha512-1+QkEcxiLlB7VEyFtyBg94e08OAsvq7FUBgApTq/w2ymCLyKJgDPsybBENVtA7XCQEgEXxKPonG+mvYRxh/LIg==",
      "requires": {
        "has-symbols": "^1.0.1"
      }
    },
    "is-resolvable": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-resolvable/-/is-resolvable-1.1.0.tgz",
      "integrity": "sha512-qgDYXFSR5WvEfuS5dMj6oTMEbrrSaM0CrFk2Yiq/gXnBvD9pMa2jGXxyhGLfvhZpuMZe18CJpFxAt3CRs42NMg=="
    },
    "is-svg": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/is-svg/-/is-svg-3.0.0.tgz",
      "integrity": "sha512-gi4iHK53LR2ujhLVVj+37Ykh9GLqYHX6JOVXbLAucaG/Cqw9xwdFOjDM2qeifLs1sF1npXXFvDu0r5HNgCMrzQ==",
      "requires": {
        "html-comment-regex": "^1.1.0"
      }
    },
    "is-symbol": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/is-symbol/-/is-symbol-1.0.3.tgz",
      "integrity": "sha512-OwijhaRSgqvhm/0ZdAcXNZt9lYdKFpcRDT5ULUuYXPoT794UNOdU+gpT6Rzo7b4V2HUl/op6GqY894AZwv9faQ==",
      "requires": {
        "has-symbols": "^1.0.1"
      }
    },
    "is-whitespace-character": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-whitespace-character/-/is-whitespace-character-1.0.4.tgz",
      "integrity": "sha512-SDweEzfIZM0SJV0EUga669UTKlmL0Pq8Lno0QDQsPnvECB3IM2aP0gdx5TrU0A01MAPfViaZiI2V1QMZLaKK5w=="
    },
    "is-windows": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz",
      "integrity": "sha512-eXK1UInq2bPmjyX6e3VHIzMLobc4J94i4AWn+Hpq3OU5KkrRC96OAcR3PRJ/pGu6m8TRnBHP9dkXQVsT/COVIA=="
    },
    "is-word-character": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/is-word-character/-/is-word-character-1.0.4.tgz",
      "integrity": "sha512-5SMO8RVennx3nZrqtKwCGyyetPE9VDba5ugvKLaD4KopPG5kR4mQ7tNt/r7feL5yt5h3lpuBbIUmCOG2eSzXHA=="
    },
    "is-wsl": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/is-wsl/-/is-wsl-1.1.0.tgz",
      "integrity": "sha1-HxbkqiKwTRM2tmGIpmrzxgDDpm0="
    },
    "isarray": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz",
      "integrity": "sha1-u5NdSFgsuhaMBoNJV6VKPgcSTxE="
    },
    "isobject": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz",
      "integrity": "sha1-TkMekrEalzFjaqH5yNHMvP2reN8="
    },
    "jest-worker": {
      "version": "24.9.0",
      "resolved": "https://registry.npmjs.org/jest-worker/-/jest-worker-24.9.0.tgz",
      "integrity": "sha512-51PE4haMSXcHohnSMdM42anbvZANYTqMrr52tVKPqqsPJMzoP6FYYDVqahX/HrAoKEKz3uUPzSvKs9A3qR4iVw==",
      "requires": {
        "merge-stream": "^2.0.0",
        "supports-color": "^6.1.0"
      }
    },
    "js-levenshtein": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/js-levenshtein/-/js-levenshtein-1.1.6.tgz",
      "integrity": "sha512-X2BB11YZtrRqY4EnQcLX5Rh373zbK4alC1FW7D7MBhL2gtcC17cTnr6DmfHZeS0s2rTHjUTMMHfG7gO8SSdw+g=="
    },
    "js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ=="
    },
    "js-yaml": {
      "version": "3.14.0",
      "resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-3.14.0.tgz",
      "integrity": "sha512-/4IbIeHcD9VMHFqDR/gQ7EdZdLimOvW2DdcxFjdyyZ9NsbS+ccrXqVWDtab/lRl5AlUqmpBx8EhPaWR+OtY17A==",
      "requires": {
        "argparse": "^1.0.7",
        "esprima": "^4.0.0"
      }
    },
    "jsesc": {
      "version": "2.5.2",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz",
      "integrity": "sha512-OYu7XEzjkCQ3C5Ps3QIZsQfNpqoJyZZA99wd9aWd05NCtC5pWOkShK2mkL6HXQR6/Cy2lbNdPlZBpuQHXE63gA=="
    },
    "json-parse-better-errors": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz",
      "integrity": "sha512-mrqyZKfX5EhL7hvqcV6WG1yYjnjeuYDzDhhcAAUrq8Po85NBQBJP+ZDUT75qZQ98IkUoBqdkExkukOU7Ts2wrw=="
    },
    "json-schema-traverse": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz",
      "integrity": "sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg=="
    },
    "json5": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.1.3.tgz",
      "integrity": "sha512-KXPvOm8K9IJKFM0bmdn8QXh7udDh1g/giieX0NLCaMnb4hEiVFqnop2ImTXCc5e0/oHz3LTqmHGtExn5hfMkOA==",
      "requires": {
        "minimist": "^1.2.5"
      }
    },
    "kind-of": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-6.0.3.tgz",
      "integrity": "sha512-dcS1ul+9tmeD95T+x28/ehLgd9mENa3LsvDTtzm3vyBEO7RPptvAD+t44WVXaUjTBRcrpFeFlC8WCruUR456hw=="
    },
    "loader-runner": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/loader-runner/-/loader-runner-2.4.0.tgz",
      "integrity": "sha512-Jsmr89RcXGIwivFY21FcRrisYZfvLMTWx5kOLc+JTxtpBOG6xML0vzbc6SEQG2FO9/4Fc3wW4LVcB5DmGflaRw=="
    },
    "loader-utils": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-2.0.0.tgz",
      "integrity": "sha512-rP4F0h2RaWSvPEkD7BLDFQnvSf+nK+wr3ESUjNTyAGobqrijmW92zc+SO6d4p4B1wh7+B/Jg1mkQe5NYUEHtHQ==",
      "requires": {
        "big.js": "^5.2.2",
        "emojis-list": "^3.0.0",
        "json5": "^2.1.2"
      }
    },
    "locate-path": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz",
      "integrity": "sha512-t7hw9pI+WvuwNJXwk5zVHpyhIqzg2qTlklJOf0mVxGSbe3Fp2VieZcduNYjaLDoy6p9uGpQEGWG87WpMKlNq8g==",
      "requires": {
        "p-locate": "^4.1.0"
      }
    },
    "lodash": {
      "version": "4.17.20",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.20.tgz",
      "integrity": "sha512-PlhdFcillOINfeV7Ni6oF1TAEayyZBoZ8bcshTHqOYJYlrqzRK5hagpagky5o4HfCzzd1TRkXPMFq6cKk9rGmA=="
    },
    "lodash.memoize": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/lodash.memoize/-/lodash.memoize-4.1.2.tgz",
      "integrity": "sha1-vMbEmkKihA7Zl/Mj6tpezRguC/4="
    },
    "lodash.uniq": {
      "version": "4.5.0",
      "resolved": "https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz",
      "integrity": "sha1-0CJTc662Uq3BvILklFM5qEJ1R3M="
    },
    "longest-streak": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/longest-streak/-/longest-streak-2.0.4.tgz",
      "integrity": "sha512-vM6rUVCVUJJt33bnmHiZEvr7wPT78ztX7rojL+LW51bHtLh6HTjx84LA5W4+oa6aKEJA7jJu5LR6vQRBpA5DVg=="
    },
    "loose-envify": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
      "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
      "requires": {
        "js-tokens": "^3.0.0 || ^4.0.0"
      }
    },
    "lru-cache": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz",
      "integrity": "sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==",
      "requires": {
        "yallist": "^4.0.0"
      }
    },
    "make-dir": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/make-dir/-/make-dir-3.1.0.tgz",
      "integrity": "sha512-g3FeP20LNwhALb/6Cz6Dd4F2ngze0jz7tbzrD2wAV+o9FeNHe4rL+yK2md0J/fiSf1sa1ADhXqi5+oVwOM/eGw==",
      "requires": {
        "semver": "^6.0.0"
      },
      "dependencies": {
        "semver": {
          "version": "6.3.0",
          "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.0.tgz",
          "integrity": "sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw=="
        }
      }
    },
    "map-cache": {
      "version": "0.2.2",
      "resolved": "https://registry.npmjs.org/map-cache/-/map-cache-0.2.2.tgz",
      "integrity": "sha1-wyq9C9ZSXZsFFkW7TyasXcmKDb8="
    },
    "map-visit": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/map-visit/-/map-visit-1.0.0.tgz",
      "integrity": "sha1-7Nyo8TFE5mDxtb1B8S80edmN+48=",
      "requires": {
        "object-visit": "^1.0.0"
      }
    },
    "markdown-escapes": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/markdown-escapes/-/markdown-escapes-1.0.4.tgz",
      "integrity": "sha512-8z4efJYk43E0upd0NbVXwgSTQs6cT3T06etieCMEg7dRbzCbxUCK/GHlX8mhHRDcp+OLlHkPKsvqQTCvsRl2cg=="
    },
    "markdown-table": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/markdown-table/-/markdown-table-2.0.0.tgz",
      "integrity": "sha512-Ezda85ToJUBhM6WGaG6veasyym+Tbs3cMAw/ZhOPqXiYsr0jgocBV3j3nx+4lk47plLlIqjwuTm/ywVI+zjJ/A==",
      "requires": {
        "repeat-string": "^1.0.0"
      }
    },
    "md5.js": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/md5.js/-/md5.js-1.3.5.tgz",
      "integrity": "sha512-xitP+WxNPcTTOgnTJcrhM0xvdPepipPSf3I8EIpGKeFLjt3PlJLIDG3u8EX53ZIubkb+5U2+3rELYpEhHhzdkg==",
      "requires": {
        "hash-base": "^3.0.0",
        "inherits": "^2.0.1",
        "safe-buffer": "^5.1.2"
      }
    },
    "mdast-util-compact": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/mdast-util-compact/-/mdast-util-compact-2.0.1.tgz",
      "integrity": "sha512-7GlnT24gEwDrdAwEHrU4Vv5lLWrEer4KOkAiKT9nYstsTad7Oc1TwqT2zIMKRdZF7cTuaf+GA1E4Kv7jJh8mPA==",
      "requires": {
        "unist-util-visit": "^2.0.0"
      }
    },
    "mdast-util-definitions": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/mdast-util-definitions/-/mdast-util-definitions-3.0.1.tgz",
      "integrity": "sha512-BAv2iUm/e6IK/b2/t+Fx69EL/AGcq/IG2S+HxHjDJGfLJtd6i9SZUS76aC9cig+IEucsqxKTR0ot3m933R3iuA==",
      "requires": {
        "unist-util-visit": "^2.0.0"
      }
    },
    "mdast-util-to-hast": {
      "version": "9.1.0",
      "resolved": "https://registry.npmjs.org/mdast-util-to-hast/-/mdast-util-to-hast-9.1.0.tgz",
      "integrity": "sha512-Akl2Vi9y9cSdr19/Dfu58PVwifPXuFt1IrHe7l+Crme1KvgUT+5z+cHLVcQVGCiNTZZcdqjnuv9vPkGsqWytWA==",
      "requires": {
        "@types/mdast": "^3.0.0",
        "@types/unist": "^2.0.3",
        "collapse-white-space": "^1.0.0",
        "detab": "^2.0.0",
        "mdast-util-definitions": "^3.0.0",
        "mdurl": "^1.0.0",
        "trim-lines": "^1.0.0",
        "unist-builder": "^2.0.0",
        "unist-util-generated": "^1.0.0",
        "unist-util-position": "^3.0.0",
        "unist-util-visit": "^2.0.0"
      }
    },
    "mdn-data": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/mdn-data/-/mdn-data-2.0.4.tgz",
      "integrity": "sha512-iV3XNKw06j5Q7mi6h+9vbx23Tv7JkjEVgKHW4pimwyDGWm0OIQntJJ+u1C6mg6mK1EaTv42XQ7w76yuzH7M2cA=="
    },
    "mdurl": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/mdurl/-/mdurl-1.0.1.tgz",
      "integrity": "sha1-/oWy7HWlkDfyrf7BAP1sYBdhFS4="
    },
    "memory-fs": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/memory-fs/-/memory-fs-0.4.1.tgz",
      "integrity": "sha1-OpoguEYlI+RHz7x+i7gO1me/xVI=",
      "requires": {
        "errno": "^0.1.3",
        "readable-stream": "^2.0.1"
      }
    },
    "merge-stream": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz",
      "integrity": "sha512-abv/qOcuPfk3URPfDzmZU1LKmuw8kT+0nIHvKrKgFrwifol/doWcdA4ZqsWQ8ENrFKkd67Mfpo/LovbIUsbt3w=="
    },
    "microevent.ts": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/microevent.ts/-/microevent.ts-0.1.1.tgz",
      "integrity": "sha512-jo1OfR4TaEwd5HOrt5+tAZ9mqT4jmpNAusXtyfNzqVm9uiSYFZlKM1wYL4oU7azZW/PxQW53wM0S6OR1JHNa2g=="
    },
    "micromatch": {
      "version": "3.1.10",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-3.1.10.tgz",
      "integrity": "sha512-MWikgl9n9M3w+bpsY3He8L+w9eF9338xRl8IAO5viDizwSzziFEyUzo2xrrloB64ADbTf8uA8vRqqttDTOmccg==",
      "requires": {
        "arr-diff": "^4.0.0",
        "array-unique": "^0.3.2",
        "braces": "^2.3.1",
        "define-property": "^2.0.2",
        "extend-shallow": "^3.0.2",
        "extglob": "^2.0.4",
        "fragment-cache": "^0.2.1",
        "kind-of": "^6.0.2",
        "nanomatch": "^1.2.9",
        "object.pick": "^1.3.0",
        "regex-not": "^1.0.0",
        "snapdragon": "^0.8.1",
        "to-regex": "^3.0.2"
      },
      "dependencies": {
        "braces": {
          "version": "2.3.2",
          "resolved": "https://registry.npmjs.org/braces/-/braces-2.3.2.tgz",
          "integrity": "sha512-aNdbnj9P8PjdXU4ybaWLK2IF3jc/EoDYbC7AazW6to3TRsfXxscC9UXOB5iDiEQrkyIbWp2SLQda4+QAa7nc3w==",
          "requires": {
            "arr-flatten": "^1.1.0",
            "array-unique": "^0.3.2",
            "extend-shallow": "^2.0.1",
            "fill-range": "^4.0.0",
            "isobject": "^3.0.1",
            "repeat-element": "^1.1.2",
            "snapdragon": "^0.8.1",
            "snapdragon-node": "^2.0.1",
            "split-string": "^3.0.2",
            "to-regex": "^3.0.1"
          },
          "dependencies": {
            "extend-shallow": {
              "version": "2.0.1",
              "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
              "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
              "requires": {
                "is-extendable": "^0.1.0"
              }
            }
          }
        },
        "fill-range": {
          "version": "4.0.0",
          "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-4.0.0.tgz",
          "integrity": "sha1-1USBHUKPmOsGpj3EAtJAPDKMOPc=",
          "requires": {
            "extend-shallow": "^2.0.1",
            "is-number": "^3.0.0",
            "repeat-string": "^1.6.1",
            "to-regex-range": "^2.1.0"
          },
          "dependencies": {
            "extend-shallow": {
              "version": "2.0.1",
              "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
              "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
              "requires": {
                "is-extendable": "^0.1.0"
              }
            }
          }
        },
        "is-number": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz",
          "integrity": "sha1-JP1iAaR4LPUFYcgQJ2r8fRLXEZU=",
          "requires": {
            "kind-of": "^3.0.2"
          },
          "dependencies": {
            "kind-of": {
              "version": "3.2.2",
              "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
              "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
              "requires": {
                "is-buffer": "^1.1.5"
              }
            }
          }
        },
        "to-regex-range": {
          "version": "2.1.1",
          "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-2.1.1.tgz",
          "integrity": "sha1-fIDBe53+vlmeJzZ+DU3VWQFB2zg=",
          "requires": {
            "is-number": "^3.0.0",
            "repeat-string": "^1.6.1"
          }
        }
      }
    },
    "miller-rabin": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/miller-rabin/-/miller-rabin-4.0.1.tgz",
      "integrity": "sha512-115fLhvZVqWwHPbClyntxEVfVDfl9DLLTuJvq3g2O/Oxi8AiNouAHvDSzHS0viUJc+V5vm3eq91Xwqn9dp4jRA==",
      "requires": {
        "bn.js": "^4.0.0",
        "brorand": "^1.0.1"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "mini-css-extract-plugin": {
      "version": "0.8.0",
      "resolved": "https://registry.npmjs.org/mini-css-extract-plugin/-/mini-css-extract-plugin-0.8.0.tgz",
      "integrity": "sha512-MNpRGbNA52q6U92i0qbVpQNsgk7LExy41MdAlG84FeytfDOtRIf/mCHdEgG8rpTKOaNKiqUnZdlptF469hxqOw==",
      "requires": {
        "loader-utils": "^1.1.0",
        "normalize-url": "1.9.1",
        "schema-utils": "^1.0.0",
        "webpack-sources": "^1.1.0"
      },
      "dependencies": {
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.4.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.0.tgz",
          "integrity": "sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^3.0.0",
            "json5": "^1.0.1"
          }
        },
        "normalize-url": {
          "version": "1.9.1",
          "resolved": "https://registry.npmjs.org/normalize-url/-/normalize-url-1.9.1.tgz",
          "integrity": "sha1-LMDWazHqIwNkWENuNiDYWVTGbDw=",
          "requires": {
            "object-assign": "^4.0.1",
            "prepend-http": "^1.0.0",
            "query-string": "^4.1.0",
            "sort-keys": "^1.0.0"
          }
        },
        "schema-utils": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-1.0.0.tgz",
          "integrity": "sha512-i27Mic4KovM/lnGsy8whRCHhc7VicJajAjTrYg11K9zfZXnYIt4k5F+kZkwjnrhKzLic/HLU4j11mjsz2G/75g==",
          "requires": {
            "ajv": "^6.1.0",
            "ajv-errors": "^1.0.0",
            "ajv-keywords": "^3.1.0"
          }
        }
      }
    },
    "minimalistic-assert": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/minimalistic-assert/-/minimalistic-assert-1.0.1.tgz",
      "integrity": "sha512-UtJcAD4yEaGtjPezWuO9wC4nwUnVH/8/Im3yEHQP4b67cXlD/Qr9hdITCU1xDbSEXg2XKNaP8jsReV7vQd00/A=="
    },
    "minimalistic-crypto-utils": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/minimalistic-crypto-utils/-/minimalistic-crypto-utils-1.0.1.tgz",
      "integrity": "sha1-9sAMHAsIIkblxNmd+4x8CDsrWCo="
    },
    "minimatch": {
      "version": "3.0.4",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz",
      "integrity": "sha512-yJHVQEhyqPLUTgt9B83PXu6W3rx4MvvHvSUvToogpwoGDOUQ+yDrR0HRot+yOCdCO7u4hX3pWft6kWBBcqh0UA==",
      "requires": {
        "brace-expansion": "^1.1.7"
      }
    },
    "minimist": {
      "version": "1.2.5",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz",
      "integrity": "sha512-FM9nNUYrRBAELZQT3xeZQ7fmMOBg6nWNmJKTcgsJeaLstP/UODVpGsr5OhXhhXg6f+qtJ8uiZ+PUxkDWcgIXLw=="
    },
    "mississippi": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/mississippi/-/mississippi-3.0.0.tgz",
      "integrity": "sha512-x471SsVjUtBRtcvd4BzKE9kFC+/2TeWgKCgw0bZcw1b9l2X3QX5vCWgF+KaZaYm87Ss//rHnWryupDrgLvmSkA==",
      "requires": {
        "concat-stream": "^1.5.0",
        "duplexify": "^3.4.2",
        "end-of-stream": "^1.1.0",
        "flush-write-stream": "^1.0.0",
        "from2": "^2.1.0",
        "parallel-transform": "^1.1.0",
        "pump": "^3.0.0",
        "pumpify": "^1.3.3",
        "stream-each": "^1.1.0",
        "through2": "^2.0.0"
      }
    },
    "mixin-deep": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/mixin-deep/-/mixin-deep-1.3.2.tgz",
      "integrity": "sha512-WRoDn//mXBiJ1H40rqa3vH0toePwSsGb45iInWlTySa+Uu4k3tYUSxa2v1KqAiLtvlrSzaExqS1gtk96A9zvEA==",
      "requires": {
        "for-in": "^1.0.2",
        "is-extendable": "^1.0.1"
      },
      "dependencies": {
        "is-extendable": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-1.0.1.tgz",
          "integrity": "sha512-arnXMxT1hhoKo9k1LZdmlNyJdDDfy2v0fXjFlmok4+i8ul/6WlbVge9bhM74OpNPQPMGUToDtz+KXa1PneJxOA==",
          "requires": {
            "is-plain-object": "^2.0.4"
          }
        }
      }
    },
    "mkdirp": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.3.tgz",
      "integrity": "sha512-P+2gwrFqx8lhew375MQHHeTlY8AuOJSrGf0R5ddkEndUkmwpgUob/vQuBD1V22/Cw1/lJr4x+EjllSezBThzBg==",
      "requires": {
        "minimist": "^1.2.5"
      }
    },
    "move-concurrently": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/move-concurrently/-/move-concurrently-1.0.1.tgz",
      "integrity": "sha1-viwAX9oy4LKa8fBdfEszIUxwH5I=",
      "requires": {
        "aproba": "^1.1.1",
        "copy-concurrently": "^1.0.0",
        "fs-write-stream-atomic": "^1.0.8",
        "mkdirp": "^0.5.1",
        "rimraf": "^2.5.4",
        "run-queue": "^1.0.3"
      }
    },
    "ms": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz",
      "integrity": "sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w=="
    },
    "nanomatch": {
      "version": "1.2.13",
      "resolved": "https://registry.npmjs.org/nanomatch/-/nanomatch-1.2.13.tgz",
      "integrity": "sha512-fpoe2T0RbHwBTBUOftAfBPaDEi06ufaUai0mE6Yn1kacc3SnTErfb/h+X94VXzI64rKFHYImXSvdwGGCmwOqCA==",
      "requires": {
        "arr-diff": "^4.0.0",
        "array-unique": "^0.3.2",
        "define-property": "^2.0.2",
        "extend-shallow": "^3.0.2",
        "fragment-cache": "^0.2.1",
        "is-windows": "^1.0.2",
        "kind-of": "^6.0.2",
        "object.pick": "^1.3.0",
        "regex-not": "^1.0.0",
        "snapdragon": "^0.8.1",
        "to-regex": "^3.0.1"
      }
    },
    "native-url": {
      "version": "0.3.1",
      "resolved": "https://registry.npmjs.org/native-url/-/native-url-0.3.1.tgz",
      "integrity": "sha512-VL0XRW8nNBdSpxqZCbLJKrLHmIMn82FZ8pJzriJgyBmErjdEtrUX6eZAJbtHjlkMooEWUV+EtJ0D5tOP3+1Piw==",
      "requires": {
        "querystring": "^0.2.0"
      }
    },
    "neo-async": {
      "version": "2.6.2",
      "resolved": "https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz",
      "integrity": "sha512-Yd3UES5mWCSqR+qNT93S3UoYUkqAZ9lLg8a7g9rimsWmYGK8cVToA4/sF3RrshdyV3sAGMXVUmpMYOw+dLpOuw=="
    },
    "next": {
      "version": "9.3.5",
      "resolved": "https://registry.npmjs.org/next/-/next-9.3.5.tgz",
      "integrity": "sha512-vJKGUK2nMsveYZTZH5Oz9L+cDYcCsuWLUXfWJejvhdQ3jLgVhZVa+7TQ45Kt0PA1ea7jqlDUN22DtzmPFi981w==",
      "requires": {
        "@ampproject/toolbox-optimizer": "2.2.0",
        "@babel/core": "7.7.2",
        "@babel/plugin-proposal-class-properties": "7.7.0",
        "@babel/plugin-proposal-nullish-coalescing-operator": "7.7.4",
        "@babel/plugin-proposal-numeric-separator": "7.8.3",
        "@babel/plugin-proposal-object-rest-spread": "7.6.2",
        "@babel/plugin-proposal-optional-chaining": "7.7.4",
        "@babel/plugin-syntax-bigint": "7.8.3",
        "@babel/plugin-syntax-dynamic-import": "7.2.0",
        "@babel/plugin-transform-modules-commonjs": "7.7.0",
        "@babel/plugin-transform-runtime": "7.6.2",
        "@babel/preset-env": "7.7.1",
        "@babel/preset-modules": "0.1.1",
        "@babel/preset-react": "7.7.0",
        "@babel/preset-typescript": "7.7.2",
        "@babel/runtime": "7.7.2",
        "@babel/types": "7.7.4",
        "babel-plugin-syntax-jsx": "6.18.0",
        "babel-plugin-transform-define": "2.0.0",
        "babel-plugin-transform-react-remove-prop-types": "0.4.24",
        "browserslist": "4.8.3",
        "css-loader": "3.3.0",
        "find-cache-dir": "3.3.1",
        "fork-ts-checker-webpack-plugin": "3.1.1",
        "jest-worker": "24.9.0",
        "loader-utils": "2.0.0",
        "mini-css-extract-plugin": "0.8.0",
        "mkdirp": "0.5.3",
        "native-url": "0.3.1",
        "pnp-webpack-plugin": "1.5.0",
        "postcss": "7.0.27",
        "prop-types": "15.7.2",
        "prop-types-exact": "1.2.0",
        "react-is": "16.8.6",
        "resolve-url-loader": "3.1.1",
        "sass-loader": "8.0.2",
        "style-loader": "1.0.0",
        "styled-jsx": "3.2.5",
        "use-subscription": "1.1.1",
        "watchpack": "2.0.0-beta.13",
        "webpack": "4.42.1",
        "webpack-sources": "1.4.3"
      }
    },
    "next-tick": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/next-tick/-/next-tick-1.0.0.tgz",
      "integrity": "sha1-yobR/ogoFpsBICCOPchCS524NCw="
    },
    "node-fetch": {
      "version": "2.6.0",
      "resolved": "https://registry.npmjs.org/node-fetch/-/node-fetch-2.6.0.tgz",
      "integrity": "sha512-8dG4H5ujfvFiqDmVu9fQ5bOHUC15JMjMY/Zumv26oOvvVJjM67KF8koCWIabKQ1GJIa9r2mMZscBq/TbdOcmNA=="
    },
    "node-libs-browser": {
      "version": "2.2.1",
      "resolved": "https://registry.npmjs.org/node-libs-browser/-/node-libs-browser-2.2.1.tgz",
      "integrity": "sha512-h/zcD8H9kaDZ9ALUWwlBUDo6TKF8a7qBSCSEGfjTVIYeqsioSKaAX+BN7NgiMGp6iSIXZ3PxgCu8KS3b71YK5Q==",
      "requires": {
        "assert": "^1.1.1",
        "browserify-zlib": "^0.2.0",
        "buffer": "^4.3.0",
        "console-browserify": "^1.1.0",
        "constants-browserify": "^1.0.0",
        "crypto-browserify": "^3.11.0",
        "domain-browser": "^1.1.1",
        "events": "^3.0.0",
        "https-browserify": "^1.0.0",
        "os-browserify": "^0.3.0",
        "path-browserify": "0.0.1",
        "process": "^0.11.10",
        "punycode": "^1.2.4",
        "querystring-es3": "^0.2.0",
        "readable-stream": "^2.3.3",
        "stream-browserify": "^2.0.1",
        "stream-http": "^2.7.2",
        "string_decoder": "^1.0.0",
        "timers-browserify": "^2.0.4",
        "tty-browserify": "0.0.0",
        "url": "^0.11.0",
        "util": "^0.11.0",
        "vm-browserify": "^1.0.1"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.3",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
          "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4="
        },
        "punycode": {
          "version": "1.4.1",
          "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz",
          "integrity": "sha1-wNWmOycYgArY4esPpSachN1BhF4="
        },
        "util": {
          "version": "0.11.1",
          "resolved": "https://registry.npmjs.org/util/-/util-0.11.1.tgz",
          "integrity": "sha512-HShAsny+zS2TZfaXxD9tYj4HQGlBezXZMZuM/S5PKLLoZkShZiGk9o5CzukI1LVHZvjdvZ2Sj1aW/Ndn2NB/HQ==",
          "requires": {
            "inherits": "2.0.3"
          }
        }
      }
    },
    "node-releases": {
      "version": "1.1.60",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-1.1.60.tgz",
      "integrity": "sha512-gsO4vjEdQaTusZAEebUWp2a5d7dF5DYoIpDG7WySnk7BuZDW+GPpHXoXXuYawRBr/9t5q54tirPz79kFIWg4dA=="
    },
    "normalize-html-whitespace": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/normalize-html-whitespace/-/normalize-html-whitespace-1.0.0.tgz",
      "integrity": "sha512-9ui7CGtOOlehQu0t/OhhlmDyc71mKVlv+4vF+me4iZLPrNtRL2xoquEdfZxasC/bdQi/Hr3iTrpyRKIG+ocabA=="
    },
    "normalize-path": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
      "integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA=="
    },
    "normalize-url": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/normalize-url/-/normalize-url-3.3.0.tgz",
      "integrity": "sha512-U+JJi7duF1o+u2pynbp2zXDW2/PADgC30f0GsHZtRh+HOcXHnw137TrNlyxxRvWW5fjKd3bcLHPxofWuCjaeZg=="
    },
    "nth-check": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/nth-check/-/nth-check-1.0.2.tgz",
      "integrity": "sha512-WeBOdju8SnzPN5vTUJYxYUxLeXpCaVP5i5e0LF8fg7WORF2Wd7wFX/pk0tYZk7s8T+J7VLy0Da6J1+wCT0AtHg==",
      "requires": {
        "boolbase": "~1.0.0"
      }
    },
    "object-assign": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
      "integrity": "sha1-IQmtx5ZYh8/AXLvUQsrIv7s2CGM="
    },
    "object-copy": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/object-copy/-/object-copy-0.1.0.tgz",
      "integrity": "sha1-fn2Fi3gb18mRpBupde04EnVOmYw=",
      "requires": {
        "copy-descriptor": "^0.1.0",
        "define-property": "^0.2.5",
        "kind-of": "^3.0.3"
      },
      "dependencies": {
        "define-property": {
          "version": "0.2.5",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz",
          "integrity": "sha1-w1se+RjsPJkPmlvFe+BKrOxcgRY=",
          "requires": {
            "is-descriptor": "^0.1.0"
          }
        },
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "object-inspect": {
      "version": "1.8.0",
      "resolved": "https://registry.npmjs.org/object-inspect/-/object-inspect-1.8.0.tgz",
      "integrity": "sha512-jLdtEOB112fORuypAyl/50VRVIBIdVQOSUUGQHzJ4xBSbit81zRarz7GThkEFZy1RceYrWYcPcBFPQwHyAc1gA=="
    },
    "object-keys": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz",
      "integrity": "sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA=="
    },
    "object-path": {
      "version": "0.11.4",
      "resolved": "https://registry.npmjs.org/object-path/-/object-path-0.11.4.tgz",
      "integrity": "sha1-NwrnUvvzfePqcKhhwju6iRVpGUk="
    },
    "object-visit": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/object-visit/-/object-visit-1.0.1.tgz",
      "integrity": "sha1-95xEk68MU3e1n+OdOV5BBC3QRbs=",
      "requires": {
        "isobject": "^3.0.0"
      }
    },
    "object.assign": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/object.assign/-/object.assign-4.1.0.tgz",
      "integrity": "sha512-exHJeq6kBKj58mqGyTQ9DFvrZC/eR6OwxzoM9YRoGBqrXYonaFyGiFMuc9VZrXf7DarreEwMpurG3dd+CNyW5w==",
      "requires": {
        "define-properties": "^1.1.2",
        "function-bind": "^1.1.1",
        "has-symbols": "^1.0.0",
        "object-keys": "^1.0.11"
      }
    },
    "object.getownpropertydescriptors": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/object.getownpropertydescriptors/-/object.getownpropertydescriptors-2.1.0.tgz",
      "integrity": "sha512-Z53Oah9A3TdLoblT7VKJaTDdXdT+lQO+cNpKVnya5JDe9uLvzu1YyY1yFDFrcxrlRgWrEFH0jJtD/IbuwjcEVg==",
      "requires": {
        "define-properties": "^1.1.3",
        "es-abstract": "^1.17.0-next.1"
      }
    },
    "object.pick": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/object.pick/-/object.pick-1.3.0.tgz",
      "integrity": "sha1-h6EKxMFpS9Lhy/U1kaZhQftd10c=",
      "requires": {
        "isobject": "^3.0.1"
      }
    },
    "object.values": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/object.values/-/object.values-1.1.1.tgz",
      "integrity": "sha512-WTa54g2K8iu0kmS/us18jEmdv1a4Wi//BZ/DTVYEcH0XhLM5NYdpDHja3gt57VrZLcNAO2WGA+KpWsDBaHt6eA==",
      "requires": {
        "define-properties": "^1.1.3",
        "es-abstract": "^1.17.0-next.1",
        "function-bind": "^1.1.1",
        "has": "^1.0.3"
      }
    },
    "once": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz",
      "integrity": "sha1-WDsap3WWHUsROsF9nFC6753Xa9E=",
      "requires": {
        "wrappy": "1"
      }
    },
    "os-browserify": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/os-browserify/-/os-browserify-0.3.0.tgz",
      "integrity": "sha1-hUNzx/XCMVkU/Jv8a9gjj92h7Cc="
    },
    "p-limit": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz",
      "integrity": "sha512-//88mFWSJx8lxCzwdAABTJL2MyWB12+eIY7MDL2SqLmAkeKU9qxRvWuSyTjm3FUmpBEMuFfckAIqEaVGUDxb6w==",
      "requires": {
        "p-try": "^2.0.0"
      }
    },
    "p-locate": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz",
      "integrity": "sha512-R79ZZ/0wAxKGu3oYMlz8jy/kbhsNrS7SKZ7PxEHBgJ5+F2mtFW2fK2cOtBh1cHYkQsbzFV7I+EoRKe6Yt0oK7A==",
      "requires": {
        "p-limit": "^2.2.0"
      }
    },
    "p-try": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz",
      "integrity": "sha512-R4nPAVTAU0B9D35/Gk3uJf/7XYbQcyohSKdvAxIRSNghFl4e71hVoGnBNQz9cWaXxO2I10KTC+3jMdvvoKw6dQ=="
    },
    "pako": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/pako/-/pako-1.0.11.tgz",
      "integrity": "sha512-4hLB8Py4zZce5s4yd9XzopqwVv/yGNhV1Bl8NTmCq1763HeK2+EwVTv+leGeL13Dnh2wfbqowVPXCIO0z4taYw=="
    },
    "parallel-transform": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/parallel-transform/-/parallel-transform-1.2.0.tgz",
      "integrity": "sha512-P2vSmIu38uIlvdcU7fDkyrxj33gTUy/ABO5ZUbGowxNCopBq/OoD42bP4UmMrJoPyk4Uqf0mu3mtWBhHCZD8yg==",
      "requires": {
        "cyclist": "^1.0.1",
        "inherits": "^2.0.3",
        "readable-stream": "^2.1.5"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "parse-asn1": {
      "version": "5.1.6",
      "resolved": "https://registry.npmjs.org/parse-asn1/-/parse-asn1-5.1.6.tgz",
      "integrity": "sha512-RnZRo1EPU6JBnra2vGHj0yhp6ebyjBZpmUCLHWiFhxlzvBCCpAuZ7elsBp1PVAbQN0/04VD/19rfzlBSwLstMw==",
      "requires": {
        "asn1.js": "^5.2.0",
        "browserify-aes": "^1.0.0",
        "evp_bytestokey": "^1.0.0",
        "pbkdf2": "^3.0.3",
        "safe-buffer": "^5.1.1"
      }
    },
    "parse-entities": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/parse-entities/-/parse-entities-2.0.0.tgz",
      "integrity": "sha512-kkywGpCcRYhqQIchaWqZ875wzpS/bMKhz5HnN3p7wveJTkTtyAB/AlnS0f8DFSqYW1T82t6yEAkEcB+A1I3MbQ==",
      "requires": {
        "character-entities": "^1.0.0",
        "character-entities-legacy": "^1.0.0",
        "character-reference-invalid": "^1.0.0",
        "is-alphanumerical": "^1.0.0",
        "is-decimal": "^1.0.0",
        "is-hexadecimal": "^1.0.0"
      }
    },
    "parse-json": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz",
      "integrity": "sha1-vjX1Qlvh9/bHRxhPmKeIy5lHfuA=",
      "requires": {
        "error-ex": "^1.3.1",
        "json-parse-better-errors": "^1.0.1"
      }
    },
    "pascalcase": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/pascalcase/-/pascalcase-0.1.1.tgz",
      "integrity": "sha1-s2PlXoAGym/iF4TS2yK9FdeRfxQ="
    },
    "path-browserify": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/path-browserify/-/path-browserify-0.0.1.tgz",
      "integrity": "sha512-BapA40NHICOS+USX9SN4tyhq+A2RrN/Ws5F0Z5aMHDp98Fl86lX8Oti8B7uN93L4Ifv4fHOEA+pQw87gmMO/lQ=="
    },
    "path-dirname": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/path-dirname/-/path-dirname-1.0.2.tgz",
      "integrity": "sha1-zDPSTVJeCZpTiMAzbG4yuRYGCeA=",
      "optional": true
    },
    "path-exists": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz",
      "integrity": "sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w=="
    },
    "path-is-absolute": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz",
      "integrity": "sha1-F0uSaHNVNP+8es5r9TpanhtcX18="
    },
    "path-parse": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz",
      "integrity": "sha512-GSmOT2EbHrINBf9SR7CDELwlJ8AENk3Qn7OikK4nFYAu3Ote2+JYNVvkpAEQm3/TLNEJFD/xZJjzyxg3KBWOzw=="
    },
    "pbkdf2": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/pbkdf2/-/pbkdf2-3.1.1.tgz",
      "integrity": "sha512-4Ejy1OPxi9f2tt1rRV7Go7zmfDQ+ZectEQz3VGUQhgq62HtIRPDyG/JtnwIxs6x3uNMwo2V7q1fMvKjb+Tnpqg==",
      "requires": {
        "create-hash": "^1.1.2",
        "create-hmac": "^1.1.4",
        "ripemd160": "^2.0.1",
        "safe-buffer": "^5.0.1",
        "sha.js": "^2.4.8"
      }
    },
    "picomatch": {
      "version": "2.2.2",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.2.2.tgz",
      "integrity": "sha512-q0M/9eZHzmr0AulXyPwNfZjtwZ/RBZlbN3K3CErVrk50T2ASYI7Bye0EvekFY3IP1Nt2DHu0re+V2ZHIpMkuWg=="
    },
    "pify": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/pify/-/pify-4.0.1.tgz",
      "integrity": "sha512-uB80kBFb/tfd68bVleG9T5GGsGPjJrLAUpR5PZIrhBnIaRTQRjqdJSsIKkOP6OAIFbj7GOrcudc5pNjZ+geV2g=="
    },
    "pkg-dir": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/pkg-dir/-/pkg-dir-4.2.0.tgz",
      "integrity": "sha512-HRDzbaKjC+AOWVXxAU/x54COGeIv9eb+6CkDSQoNTt4XyWoIJvuPsXizxu/Fr23EiekbtZwmh1IcIG/l/a10GQ==",
      "requires": {
        "find-up": "^4.0.0"
      }
    },
    "pnp-webpack-plugin": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/pnp-webpack-plugin/-/pnp-webpack-plugin-1.5.0.tgz",
      "integrity": "sha512-jd9olUr9D7do+RN8Wspzhpxhgp1n6Vd0NtQ4SFkmIACZoEL1nkyAdW9Ygrinjec0vgDcWjscFQQ1gDW8rsfKTg==",
      "requires": {
        "ts-pnp": "^1.1.2"
      }
    },
    "posix-character-classes": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/posix-character-classes/-/posix-character-classes-0.1.1.tgz",
      "integrity": "sha1-AerA/jta9xoqbAL+q7jB/vfgDqs="
    },
    "postcss": {
      "version": "7.0.27",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-7.0.27.tgz",
      "integrity": "sha512-WuQETPMcW9Uf1/22HWUWP9lgsIC+KEHg2kozMflKjbeUtw9ujvFX6QmIfozaErDkmLWS9WEnEdEe6Uo9/BNTdQ==",
      "requires": {
        "chalk": "^2.4.2",
        "source-map": "^0.6.1",
        "supports-color": "^6.1.0"
      }
    },
    "postcss-calc": {
      "version": "7.0.3",
      "resolved": "https://registry.npmjs.org/postcss-calc/-/postcss-calc-7.0.3.tgz",
      "integrity": "sha512-IB/EAEmZhIMEIhG7Ov4x+l47UaXOS1n2f4FBUk/aKllQhtSCxWhTzn0nJgkqN7fo/jcWySvWTSB6Syk9L+31bA==",
      "requires": {
        "postcss": "^7.0.27",
        "postcss-selector-parser": "^6.0.2",
        "postcss-value-parser": "^4.0.2"
      }
    },
    "postcss-colormin": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/postcss-colormin/-/postcss-colormin-4.0.3.tgz",
      "integrity": "sha512-WyQFAdDZpExQh32j0U0feWisZ0dmOtPl44qYmJKkq9xFWY3p+4qnRzCHeNrkeRhwPHz9bQ3mo0/yVkaply0MNw==",
      "requires": {
        "browserslist": "^4.0.0",
        "color": "^3.0.0",
        "has": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-convert-values": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-4.0.1.tgz",
      "integrity": "sha512-Kisdo1y77KUC0Jmn0OXU/COOJbzM8cImvw1ZFsBgBgMgb1iL23Zs/LXRe3r+EZqM3vGYKdQ2YJVQ5VkJI+zEJQ==",
      "requires": {
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-discard-comments": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-4.0.2.tgz",
      "integrity": "sha512-RJutN259iuRf3IW7GZyLM5Sw4GLTOH8FmsXBnv8Ab/Tc2k4SR4qbV4DNbyyY4+Sjo362SyDmW2DQ7lBSChrpkg==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "postcss-discard-duplicates": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-4.0.2.tgz",
      "integrity": "sha512-ZNQfR1gPNAiXZhgENFfEglF93pciw0WxMkJeVmw8eF+JZBbMD7jp6C67GqJAXVZP2BWbOztKfbsdmMp/k8c6oQ==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "postcss-discard-empty": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-4.0.1.tgz",
      "integrity": "sha512-B9miTzbznhDjTfjvipfHoqbWKwd0Mj+/fL5s1QOz06wufguil+Xheo4XpOnc4NqKYBCNqqEzgPv2aPBIJLox0w==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "postcss-discard-overridden": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-4.0.1.tgz",
      "integrity": "sha512-IYY2bEDD7g1XM1IDEsUT4//iEYCxAmP5oDSFMVU/JVvT7gh+l4fmjciLqGgwjdWpQIdb0Che2VX00QObS5+cTg==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "postcss-merge-longhand": {
      "version": "4.0.11",
      "resolved": "https://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-4.0.11.tgz",
      "integrity": "sha512-alx/zmoeXvJjp7L4mxEMjh8lxVlDFX1gqWHzaaQewwMZiVhLo42TEClKaeHbRf6J7j82ZOdTJ808RtN0ZOZwvw==",
      "requires": {
        "css-color-names": "0.0.4",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0",
        "stylehacks": "^4.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-merge-rules": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-4.0.3.tgz",
      "integrity": "sha512-U7e3r1SbvYzO0Jr3UT/zKBVgYYyhAz0aitvGIYOYK5CPmkNih+WDSsS5tvPrJ8YMQYlEMvsZIiqmn7HdFUaeEQ==",
      "requires": {
        "browserslist": "^4.0.0",
        "caniuse-api": "^3.0.0",
        "cssnano-util-same-parent": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-selector-parser": "^3.0.0",
        "vendors": "^1.0.0"
      },
      "dependencies": {
        "postcss-selector-parser": {
          "version": "3.1.2",
          "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-3.1.2.tgz",
          "integrity": "sha512-h7fJ/5uWuRVyOtkO45pnt1Ih40CEleeyCHzipqAZO2e5H20g25Y48uYnFUiShvY4rZWNJ/Bib/KVPmanaCtOhA==",
          "requires": {
            "dot-prop": "^5.2.0",
            "indexes-of": "^1.0.1",
            "uniq": "^1.0.1"
          }
        }
      }
    },
    "postcss-minify-font-values": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-4.0.2.tgz",
      "integrity": "sha512-j85oO6OnRU9zPf04+PZv1LYIYOprWm6IA6zkXkrJXyRveDEuQggG6tvoy8ir8ZwjLxLuGfNkCZEQG7zan+Hbtg==",
      "requires": {
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-minify-gradients": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-4.0.2.tgz",
      "integrity": "sha512-qKPfwlONdcf/AndP1U8SJ/uzIJtowHlMaSioKzebAXSG4iJthlWC9iSWznQcX4f66gIWX44RSA841HTHj3wK+Q==",
      "requires": {
        "cssnano-util-get-arguments": "^4.0.0",
        "is-color-stop": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-minify-params": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-4.0.2.tgz",
      "integrity": "sha512-G7eWyzEx0xL4/wiBBJxJOz48zAKV2WG3iZOqVhPet/9geefm/Px5uo1fzlHu+DOjT+m0Mmiz3jkQzVHe6wxAWg==",
      "requires": {
        "alphanum-sort": "^1.0.0",
        "browserslist": "^4.0.0",
        "cssnano-util-get-arguments": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0",
        "uniqs": "^2.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-minify-selectors": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-4.0.2.tgz",
      "integrity": "sha512-D5S1iViljXBj9kflQo4YutWnJmwm8VvIsU1GeXJGiG9j8CIg9zs4voPMdQDUmIxetUOh60VilsNzCiAFTOqu3g==",
      "requires": {
        "alphanum-sort": "^1.0.0",
        "has": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-selector-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-selector-parser": {
          "version": "3.1.2",
          "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-3.1.2.tgz",
          "integrity": "sha512-h7fJ/5uWuRVyOtkO45pnt1Ih40CEleeyCHzipqAZO2e5H20g25Y48uYnFUiShvY4rZWNJ/Bib/KVPmanaCtOhA==",
          "requires": {
            "dot-prop": "^5.2.0",
            "indexes-of": "^1.0.1",
            "uniq": "^1.0.1"
          }
        }
      }
    },
    "postcss-modules-extract-imports": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-extract-imports/-/postcss-modules-extract-imports-2.0.0.tgz",
      "integrity": "sha512-LaYLDNS4SG8Q5WAWqIJgdHPJrDDr/Lv775rMBFUbgjTz6j34lUznACHcdRWroPvXANP2Vj7yNK57vp9eFqzLWQ==",
      "requires": {
        "postcss": "^7.0.5"
      }
    },
    "postcss-modules-local-by-default": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/postcss-modules-local-by-default/-/postcss-modules-local-by-default-3.0.3.tgz",
      "integrity": "sha512-e3xDq+LotiGesympRlKNgaJ0PCzoUIdpH0dj47iWAui/kyTgh3CiAr1qP54uodmJhl6p9rN6BoNcdEDVJx9RDw==",
      "requires": {
        "icss-utils": "^4.1.1",
        "postcss": "^7.0.32",
        "postcss-selector-parser": "^6.0.2",
        "postcss-value-parser": "^4.1.0"
      },
      "dependencies": {
        "postcss": {
          "version": "7.0.32",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-7.0.32.tgz",
          "integrity": "sha512-03eXong5NLnNCD05xscnGKGDZ98CyzoqPSMjOe6SuoQY7Z2hIj0Ld1g/O/UQRuOle2aRtiIRDg9tDcTGAkLfKw==",
          "requires": {
            "chalk": "^2.4.2",
            "source-map": "^0.6.1",
            "supports-color": "^6.1.0"
          }
        }
      }
    },
    "postcss-modules-scope": {
      "version": "2.2.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-scope/-/postcss-modules-scope-2.2.0.tgz",
      "integrity": "sha512-YyEgsTMRpNd+HmyC7H/mh3y+MeFWevy7V1evVhJWewmMbjDHIbZbOXICC2y+m1xI1UVfIT1HMW/O04Hxyu9oXQ==",
      "requires": {
        "postcss": "^7.0.6",
        "postcss-selector-parser": "^6.0.0"
      }
    },
    "postcss-modules-values": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-values/-/postcss-modules-values-3.0.0.tgz",
      "integrity": "sha512-1//E5jCBrZ9DmRX+zCtmQtRSV6PV42Ix7Bzj9GbwJceduuf7IqP8MgeTXuRDHOWj2m0VzZD5+roFWDuU8RQjcg==",
      "requires": {
        "icss-utils": "^4.0.0",
        "postcss": "^7.0.6"
      }
    },
    "postcss-normalize-charset": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-4.0.1.tgz",
      "integrity": "sha512-gMXCrrlWh6G27U0hF3vNvR3w8I1s2wOBILvA87iNXaPvSNo5uZAMYsZG7XjCUf1eVxuPfyL4TJ7++SGZLc9A3g==",
      "requires": {
        "postcss": "^7.0.0"
      }
    },
    "postcss-normalize-display-values": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-display-values/-/postcss-normalize-display-values-4.0.2.tgz",
      "integrity": "sha512-3F2jcsaMW7+VtRMAqf/3m4cPFhPD3EFRgNs18u+k3lTJJlVe7d0YPO+bnwqo2xg8YiRpDXJI2u8A0wqJxMsQuQ==",
      "requires": {
        "cssnano-util-get-match": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-positions": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-positions/-/postcss-normalize-positions-4.0.2.tgz",
      "integrity": "sha512-Dlf3/9AxpxE+NF1fJxYDeggi5WwV35MXGFnnoccP/9qDtFrTArZ0D0R+iKcg5WsUd8nUYMIl8yXDCtcrT8JrdA==",
      "requires": {
        "cssnano-util-get-arguments": "^4.0.0",
        "has": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-repeat-style": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-repeat-style/-/postcss-normalize-repeat-style-4.0.2.tgz",
      "integrity": "sha512-qvigdYYMpSuoFs3Is/f5nHdRLJN/ITA7huIoCyqqENJe9PvPmLhNLMu7QTjPdtnVf6OcYYO5SHonx4+fbJE1+Q==",
      "requires": {
        "cssnano-util-get-arguments": "^4.0.0",
        "cssnano-util-get-match": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-string": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-string/-/postcss-normalize-string-4.0.2.tgz",
      "integrity": "sha512-RrERod97Dnwqq49WNz8qo66ps0swYZDSb6rM57kN2J+aoyEAJfZ6bMx0sx/F9TIEX0xthPGCmeyiam/jXif0eA==",
      "requires": {
        "has": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-timing-functions": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-timing-functions/-/postcss-normalize-timing-functions-4.0.2.tgz",
      "integrity": "sha512-acwJY95edP762e++00Ehq9L4sZCEcOPyaHwoaFOhIwWCDfik6YvqsYNxckee65JHLKzuNSSmAdxwD2Cud1Z54A==",
      "requires": {
        "cssnano-util-get-match": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-unicode": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-normalize-unicode/-/postcss-normalize-unicode-4.0.1.tgz",
      "integrity": "sha512-od18Uq2wCYn+vZ/qCOeutvHjB5jm57ToxRaMeNuf0nWVHaP9Hua56QyMF6fs/4FSUnVIw0CBPsU0K4LnBPwYwg==",
      "requires": {
        "browserslist": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-url": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-4.0.1.tgz",
      "integrity": "sha512-p5oVaF4+IHwu7VpMan/SSpmpYxcJMtkGppYf0VbdH5B6hN8YNmVyJLuY9FmLQTzY3fag5ESUUHDqM+heid0UVA==",
      "requires": {
        "is-absolute-url": "^2.0.0",
        "normalize-url": "^3.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-normalize-whitespace": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-normalize-whitespace/-/postcss-normalize-whitespace-4.0.2.tgz",
      "integrity": "sha512-tO8QIgrsI3p95r8fyqKV+ufKlSHh9hMJqACqbv2XknufqEDhDvbguXGBBqxw9nsQoXWf0qOqppziKJKHMD4GtA==",
      "requires": {
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-ordered-values": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-4.1.2.tgz",
      "integrity": "sha512-2fCObh5UanxvSxeXrtLtlwVThBvHn6MQcu4ksNT2tsaV2Fg76R2CV98W7wNSlX+5/pFwEyaDwKLLoEV7uRybAw==",
      "requires": {
        "cssnano-util-get-arguments": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-reduce-initial": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-4.0.3.tgz",
      "integrity": "sha512-gKWmR5aUulSjbzOfD9AlJiHCGH6AEVLaM0AV+aSioxUDd16qXP1PCh8d1/BGVvpdWn8k/HiK7n6TjeoXN1F7DA==",
      "requires": {
        "browserslist": "^4.0.0",
        "caniuse-api": "^3.0.0",
        "has": "^1.0.0",
        "postcss": "^7.0.0"
      }
    },
    "postcss-reduce-transforms": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-4.0.2.tgz",
      "integrity": "sha512-EEVig1Q2QJ4ELpJXMZR8Vt5DQx8/mo+dGWSR7vWXqcob2gQLyQGsionYcGKATXvQzMPn6DSN1vTN7yFximdIAg==",
      "requires": {
        "cssnano-util-get-match": "^4.0.0",
        "has": "^1.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-safe-parser": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-safe-parser/-/postcss-safe-parser-4.0.2.tgz",
      "integrity": "sha512-Uw6ekxSWNLCPesSv/cmqf2bY/77z11O7jZGPax3ycZMFU/oi2DMH9i89AdHc1tRwFg/arFoEwX0IS3LCUxJh1g==",
      "requires": {
        "postcss": "^7.0.26"
      }
    },
    "postcss-selector-parser": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.2.tgz",
      "integrity": "sha512-36P2QR59jDTOAiIkqEprfJDsoNrvwFei3eCqKd1Y0tUsBimsq39BLp7RD+JWny3WgB1zGhJX8XVePwm9k4wdBg==",
      "requires": {
        "cssesc": "^3.0.0",
        "indexes-of": "^1.0.1",
        "uniq": "^1.0.1"
      }
    },
    "postcss-svgo": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/postcss-svgo/-/postcss-svgo-4.0.2.tgz",
      "integrity": "sha512-C6wyjo3VwFm0QgBy+Fu7gCYOkCmgmClghO+pjcxvrcBKtiKt0uCF+hvbMO1fyv5BMImRK90SMb+dwUnfbGd+jw==",
      "requires": {
        "is-svg": "^3.0.0",
        "postcss": "^7.0.0",
        "postcss-value-parser": "^3.0.0",
        "svgo": "^1.0.0"
      },
      "dependencies": {
        "postcss-value-parser": {
          "version": "3.3.1",
          "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz",
          "integrity": "sha512-pISE66AbVkp4fDQ7VHBwRNXzAAKJjw4Vw7nWI/+Q3vuly7SNfgYXvm6i5IgFylHGK5sP/xHAbB7N49OS4gWNyQ=="
        }
      }
    },
    "postcss-unique-selectors": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-4.0.1.tgz",
      "integrity": "sha512-+JanVaryLo9QwZjKrmJgkI4Fn8SBgRO6WXQBJi7KiAVPlmxikB5Jzc4EvXMT2H0/m0RjrVVm9rGNhZddm/8Spg==",
      "requires": {
        "alphanum-sort": "^1.0.0",
        "postcss": "^7.0.0",
        "uniqs": "^2.0.0"
      }
    },
    "postcss-value-parser": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.1.0.tgz",
      "integrity": "sha512-97DXOFbQJhk71ne5/Mt6cOu6yxsSfM0QGQyl0L25Gca4yGWEGJaig7l7gbCX623VqTBNGLRLaVUCnNkcedlRSQ=="
    },
    "prepend-http": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz",
      "integrity": "sha1-1PRWKwzjaW5BrFLQ4ALlemNdxtw="
    },
    "process": {
      "version": "0.11.10",
      "resolved": "https://registry.npmjs.org/process/-/process-0.11.10.tgz",
      "integrity": "sha1-czIwDoQBYb2j5podHZGn1LwW8YI="
    },
    "process-nextick-args": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz",
      "integrity": "sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag=="
    },
    "promise-inflight": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz",
      "integrity": "sha1-mEcocL8igTL8vdhoEputEsPAKeM="
    },
    "prop-types": {
      "version": "15.7.2",
      "resolved": "https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz",
      "integrity": "sha512-8QQikdH7//R2vurIJSutZ1smHYTcLpRWEOlHnzcWHmBYrOGUysKwSsrC89BCiFj3CbrfJ/nXFdJepOVrY1GCHQ==",
      "requires": {
        "loose-envify": "^1.4.0",
        "object-assign": "^4.1.1",
        "react-is": "^16.8.1"
      }
    },
    "prop-types-exact": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/prop-types-exact/-/prop-types-exact-1.2.0.tgz",
      "integrity": "sha512-K+Tk3Kd9V0odiXFP9fwDHUYRyvK3Nun3GVyPapSIs5OBkITAm15W0CPFD/YKTkMUAbc0b9CUwRQp2ybiBIq+eA==",
      "requires": {
        "has": "^1.0.3",
        "object.assign": "^4.1.0",
        "reflect.ownkeys": "^0.2.0"
      }
    },
    "property-information": {
      "version": "5.5.0",
      "resolved": "https://registry.npmjs.org/property-information/-/property-information-5.5.0.tgz",
      "integrity": "sha512-RgEbCx2HLa1chNgvChcx+rrCWD0ctBmGSE0M7lVm1yyv4UbvbrWoXp/BkVLZefzjrRBGW8/Js6uh/BnlHXFyjA==",
      "requires": {
        "xtend": "^4.0.0"
      }
    },
    "prr": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/prr/-/prr-1.0.1.tgz",
      "integrity": "sha1-0/wRS6BplaRexok/SEzrHXj19HY="
    },
    "public-encrypt": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/public-encrypt/-/public-encrypt-4.0.3.tgz",
      "integrity": "sha512-zVpa8oKZSz5bTMTFClc1fQOnyyEzpl5ozpi1B5YcvBrdohMjH2rfsBtyXcuNuwjsDIXmBYlF2N5FlJYhR29t8Q==",
      "requires": {
        "bn.js": "^4.1.0",
        "browserify-rsa": "^4.0.0",
        "create-hash": "^1.1.0",
        "parse-asn1": "^5.0.0",
        "randombytes": "^2.0.1",
        "safe-buffer": "^5.1.2"
      },
      "dependencies": {
        "bn.js": {
          "version": "4.11.9",
          "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.9.tgz",
          "integrity": "sha512-E6QoYqCKZfgatHTdHzs1RRKP7ip4vvm+EyRUeE2RF0NblwVvb0p6jSVeNTOFxPn26QXN2o6SMfNxKp6kU8zQaw=="
        }
      }
    },
    "pump": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/pump/-/pump-3.0.0.tgz",
      "integrity": "sha512-LwZy+p3SFs1Pytd/jYct4wpv49HiYCqd9Rlc5ZVdk0V+8Yzv6jR5Blk3TRmPL1ft69TxP0IMZGJ+WPFU2BFhww==",
      "requires": {
        "end-of-stream": "^1.1.0",
        "once": "^1.3.1"
      }
    },
    "pumpify": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/pumpify/-/pumpify-1.5.1.tgz",
      "integrity": "sha512-oClZI37HvuUJJxSKKrC17bZ9Cu0ZYhEAGPsPUy9KlMUmv9dKX2o77RUmq7f3XjIxbwyGwYzbzQ1L2Ks8sIradQ==",
      "requires": {
        "duplexify": "^3.6.0",
        "inherits": "^2.0.3",
        "pump": "^2.0.0"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        },
        "pump": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/pump/-/pump-2.0.1.tgz",
          "integrity": "sha512-ruPMNRkN3MHP1cWJc9OWr+T/xDP0jhXYCLfJcBuX54hhfIBnaQmAUMfDcG4DM5UMWByBbJY69QSphm3jtDKIkA==",
          "requires": {
            "end-of-stream": "^1.1.0",
            "once": "^1.3.1"
          }
        }
      }
    },
    "punycode": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz",
      "integrity": "sha512-XRsRjdf+j5ml+y/6GKHPZbrF/8p2Yga0JPtdqTIY2Xe5ohJPD9saDJJLPvp9+NSBprVvevdXZybnj2cv8OEd0A=="
    },
    "q": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/q/-/q-1.5.1.tgz",
      "integrity": "sha1-fjL3W0E4EpHQRhHxvxQQmsAGUdc="
    },
    "query-string": {
      "version": "4.3.4",
      "resolved": "https://registry.npmjs.org/query-string/-/query-string-4.3.4.tgz",
      "integrity": "sha1-u7aTucqRXCMlFbIosaArYJBD2+s=",
      "requires": {
        "object-assign": "^4.1.0",
        "strict-uri-encode": "^1.0.0"
      }
    },
    "querystring": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/querystring/-/querystring-0.2.0.tgz",
      "integrity": "sha1-sgmEkgO7Jd+CDadW50cAWHhSFiA="
    },
    "querystring-es3": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz",
      "integrity": "sha1-nsYfeQSYdXB9aUFFlv2Qek1xHnM="
    },
    "randombytes": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/randombytes/-/randombytes-2.1.0.tgz",
      "integrity": "sha512-vYl3iOX+4CKUWuxGi9Ukhie6fsqXqS9FE2Zaic4tNFD2N2QQaXOMFbuKK4QmDHC0JO6B1Zp41J0LpT0oR68amQ==",
      "requires": {
        "safe-buffer": "^5.1.0"
      }
    },
    "randomfill": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/randomfill/-/randomfill-1.0.4.tgz",
      "integrity": "sha512-87lcbR8+MhcWcUiQ+9e+Rwx8MyR2P7qnt15ynUlbm3TU/fjbgz4GsvfSUDTemtCCtVCqb4ZcEFlyPNTh9bBTLw==",
      "requires": {
        "randombytes": "^2.0.5",
        "safe-buffer": "^5.1.0"
      }
    },
    "react": {
      "version": "16.13.1",
      "resolved": "https://registry.npmjs.org/react/-/react-16.13.1.tgz",
      "integrity": "sha512-YMZQQq32xHLX0bz5Mnibv1/LHb3Sqzngu7xstSM+vrkE5Kzr9xE0yMByK5kMoTK30YVJE61WfbxIFFvfeDKT1w==",
      "requires": {
        "loose-envify": "^1.1.0",
        "object-assign": "^4.1.1",
        "prop-types": "^15.6.2"
      }
    },
    "react-dom": {
      "version": "16.13.1",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-16.13.1.tgz",
      "integrity": "sha512-81PIMmVLnCNLO/fFOQxdQkvEq/+Hfpv24XNJfpyZhTRfO0QcmQIF/PgCa1zCOj2w1hrn12MFLyaJ/G0+Mxtfag==",
      "requires": {
        "loose-envify": "^1.1.0",
        "object-assign": "^4.1.1",
        "prop-types": "^15.6.2",
        "scheduler": "^0.19.1"
      }
    },
    "react-is": {
      "version": "16.8.6",
      "resolved": "https://registry.npmjs.org/react-is/-/react-is-16.8.6.tgz",
      "integrity": "sha512-aUk3bHfZ2bRSVFFbbeVS4i+lNPZr3/WM5jT2J5omUVV1zzcs1nAaf3l51ctA5FFvCRbhrH0bdAsRRQddFJZPtA=="
    },
    "readable-stream": {
      "version": "2.3.7",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.7.tgz",
      "integrity": "sha512-Ebho8K4jIbHAxnuxi7o42OrZgF/ZTNcsZj6nRKyUmkhLFq8CHItp/fy6hQZuZmP/n3yZ9VBUbp4zz/mX8hmYPw==",
      "requires": {
        "core-util-is": "~1.0.0",
        "inherits": "~2.0.3",
        "isarray": "~1.0.0",
        "process-nextick-args": "~2.0.0",
        "safe-buffer": "~5.1.1",
        "string_decoder": "~1.1.1",
        "util-deprecate": "~1.0.1"
      },
      "dependencies": {
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ=="
        }
      }
    },
    "readdirp": {
      "version": "3.4.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.4.0.tgz",
      "integrity": "sha512-0xe001vZBnJEK+uKcj8qOhyAKPzIT+gStxWr3LCB0DwcXR5NZJ3IaC+yGnHCYzB/S7ov3m3EEbZI2zeNvX+hGQ==",
      "requires": {
        "picomatch": "^2.2.1"
      }
    },
    "reflect.ownkeys": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/reflect.ownkeys/-/reflect.ownkeys-0.2.0.tgz",
      "integrity": "sha1-dJrO7H8/34tj+SegSAnpDFwLNGA="
    },
    "regenerate": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/regenerate/-/regenerate-1.4.1.tgz",
      "integrity": "sha512-j2+C8+NtXQgEKWk49MMP5P/u2GhnahTtVkRIHr5R5lVRlbKvmQ+oS+A5aLKWp2ma5VkT8sh6v+v4hbH0YHR66A=="
    },
    "regenerate-unicode-properties": {
      "version": "8.2.0",
      "resolved": "https://registry.npmjs.org/regenerate-unicode-properties/-/regenerate-unicode-properties-8.2.0.tgz",
      "integrity": "sha512-F9DjY1vKLo/tPePDycuH3dn9H1OTPIkVD9Kz4LODu+F2C75mgjAJ7x/gwy6ZcSNRAAkhNlJSOHRe8k3p+K9WhA==",
      "requires": {
        "regenerate": "^1.4.0"
      }
    },
    "regenerator-runtime": {
      "version": "0.13.7",
      "resolved": "https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.7.tgz",
      "integrity": "sha512-a54FxoJDIr27pgf7IgeQGxmqUNYrcV338lf/6gH456HZ/PhX+5BcwHXG9ajESmwe6WRO0tAzRUrRmNONWgkrew=="
    },
    "regenerator-transform": {
      "version": "0.14.5",
      "resolved": "https://registry.npmjs.org/regenerator-transform/-/regenerator-transform-0.14.5.tgz",
      "integrity": "sha512-eOf6vka5IO151Jfsw2NO9WpGX58W6wWmefK3I1zEGr0lOD0u8rwPaNqQL1aRxUaxLeKO3ArNh3VYg1KbaD+FFw==",
      "requires": {
        "@babel/runtime": "^7.8.4"
      },
      "dependencies": {
        "@babel/runtime": {
          "version": "7.11.2",
          "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.11.2.tgz",
          "integrity": "sha512-TeWkU52so0mPtDcaCTxNBI/IHiz0pZgr8VEFqXFtZWpYD08ZB6FaSwVAS8MKRQAP3bYKiVjwysOJgMFY28o6Tw==",
          "requires": {
            "regenerator-runtime": "^0.13.4"
          }
        }
      }
    },
    "regex-not": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/regex-not/-/regex-not-1.0.2.tgz",
      "integrity": "sha512-J6SDjUgDxQj5NusnOtdFxDwN/+HWykR8GELwctJ7mdqhcyy1xEc4SRFHUXvxTp661YaVKAjfRLZ9cCqS6tn32A==",
      "requires": {
        "extend-shallow": "^3.0.2",
        "safe-regex": "^1.1.0"
      }
    },
    "regex-parser": {
      "version": "2.2.10",
      "resolved": "https://registry.npmjs.org/regex-parser/-/regex-parser-2.2.10.tgz",
      "integrity": "sha512-8t6074A68gHfU8Neftl0Le6KTDwfGAj7IyjPIMSfikI2wJUTHDMaIq42bUsfVnj8mhx0R+45rdUXHGpN164avA=="
    },
    "regexpu-core": {
      "version": "4.7.0",
      "resolved": "https://registry.npmjs.org/regexpu-core/-/regexpu-core-4.7.0.tgz",
      "integrity": "sha512-TQ4KXRnIn6tz6tjnrXEkD/sshygKH/j5KzK86X8MkeHyZ8qst/LZ89j3X4/8HEIfHANTFIP/AbXakeRhWIl5YQ==",
      "requires": {
        "regenerate": "^1.4.0",
        "regenerate-unicode-properties": "^8.2.0",
        "regjsgen": "^0.5.1",
        "regjsparser": "^0.6.4",
        "unicode-match-property-ecmascript": "^1.0.4",
        "unicode-match-property-value-ecmascript": "^1.2.0"
      }
    },
    "regjsgen": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/regjsgen/-/regjsgen-0.5.2.tgz",
      "integrity": "sha512-OFFT3MfrH90xIW8OOSyUrk6QHD5E9JOTeGodiJeBS3J6IwlgzJMNE/1bZklWz5oTg+9dCMyEetclvCVXOPoN3A=="
    },
    "regjsparser": {
      "version": "0.6.4",
      "resolved": "https://registry.npmjs.org/regjsparser/-/regjsparser-0.6.4.tgz",
      "integrity": "sha512-64O87/dPDgfk8/RQqC4gkZoGyyWFIEUTTh80CU6CWuK5vkCGyekIx+oKcEIYtP/RAxSQltCZHCNu/mdd7fqlJw==",
      "requires": {
        "jsesc": "~0.5.0"
      },
      "dependencies": {
        "jsesc": {
          "version": "0.5.0",
          "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz",
          "integrity": "sha1-597mbjXW/Bb3EP6R1c9p9w8IkR0="
        }
      }
    },
    "remark": {
      "version": "12.0.1",
      "resolved": "https://registry.npmjs.org/remark/-/remark-12.0.1.tgz",
      "integrity": "sha512-gS7HDonkdIaHmmP/+shCPejCEEW+liMp/t/QwmF0Xt47Rpuhl32lLtDV1uKWvGoq+kxr5jSgg5oAIpGuyULjUw==",
      "requires": {
        "remark-parse": "^8.0.0",
        "remark-stringify": "^8.0.0",
        "unified": "^9.0.0"
      }
    },
    "remark-html": {
      "version": "12.0.0",
      "resolved": "https://registry.npmjs.org/remark-html/-/remark-html-12.0.0.tgz",
      "integrity": "sha512-M104NMHs48+uswChJkCDXCdabzxAinpHikpt6kS3gmGMyIvPZ5kn53tB9shFsL2O4HUJ9DIEsah1SX1Ve5FXHA==",
      "requires": {
        "hast-util-sanitize": "^3.0.0",
        "hast-util-to-html": "^7.0.0",
        "mdast-util-to-hast": "^9.0.0",
        "xtend": "^4.0.1"
      }
    },
    "remark-parse": {
      "version": "8.0.3",
      "resolved": "https://registry.npmjs.org/remark-parse/-/remark-parse-8.0.3.tgz",
      "integrity": "sha512-E1K9+QLGgggHxCQtLt++uXltxEprmWzNfg+MxpfHsZlrddKzZ/hZyWHDbK3/Ap8HJQqYJRXP+jHczdL6q6i85Q==",
      "requires": {
        "ccount": "^1.0.0",
        "collapse-white-space": "^1.0.2",
        "is-alphabetical": "^1.0.0",
        "is-decimal": "^1.0.0",
        "is-whitespace-character": "^1.0.0",
        "is-word-character": "^1.0.0",
        "markdown-escapes": "^1.0.0",
        "parse-entities": "^2.0.0",
        "repeat-string": "^1.5.4",
        "state-toggle": "^1.0.0",
        "trim": "0.0.1",
        "trim-trailing-lines": "^1.0.0",
        "unherit": "^1.0.4",
        "unist-util-remove-position": "^2.0.0",
        "vfile-location": "^3.0.0",
        "xtend": "^4.0.1"
      }
    },
    "remark-stringify": {
      "version": "8.1.1",
      "resolved": "https://registry.npmjs.org/remark-stringify/-/remark-stringify-8.1.1.tgz",
      "integrity": "sha512-q4EyPZT3PcA3Eq7vPpT6bIdokXzFGp9i85igjmhRyXWmPs0Y6/d2FYwUNotKAWyLch7g0ASZJn/KHHcHZQ163A==",
      "requires": {
        "ccount": "^1.0.0",
        "is-alphanumeric": "^1.0.0",
        "is-decimal": "^1.0.0",
        "is-whitespace-character": "^1.0.0",
        "longest-streak": "^2.0.1",
        "markdown-escapes": "^1.0.0",
        "markdown-table": "^2.0.0",
        "mdast-util-compact": "^2.0.0",
        "parse-entities": "^2.0.0",
        "repeat-string": "^1.5.4",
        "state-toggle": "^1.0.0",
        "stringify-entities": "^3.0.0",
        "unherit": "^1.0.4",
        "xtend": "^4.0.1"
      }
    },
    "remove-trailing-separator": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz",
      "integrity": "sha1-wkvOKig62tW8P1jg1IJJuSN52O8=",
      "optional": true
    },
    "repeat-element": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.3.tgz",
      "integrity": "sha512-ahGq0ZnV5m5XtZLMb+vP76kcAM5nkLqk0lpqAuojSKGgQtn4eRi4ZZGm2olo2zKFH+sMsWaqOCW1dqAnOru72g=="
    },
    "repeat-string": {
      "version": "1.6.1",
      "resolved": "https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz",
      "integrity": "sha1-jcrkcOHIirwtYA//Sndihtp15jc="
    },
    "replace-ext": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/replace-ext/-/replace-ext-1.0.0.tgz",
      "integrity": "sha1-3mMSg3P8v3w8z6TeWkgMRaZ5WOs="
    },
    "resolve": {
      "version": "1.17.0",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.17.0.tgz",
      "integrity": "sha512-ic+7JYiV8Vi2yzQGFWOkiZD5Z9z7O2Zhm9XMaTxdJExKasieFCr+yXZ/WmXsckHiKl12ar0y6XiXDx3m4RHn1w==",
      "requires": {
        "path-parse": "^1.0.6"
      }
    },
    "resolve-from": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/resolve-from/-/resolve-from-3.0.0.tgz",
      "integrity": "sha1-six699nWiBvItuZTM17rywoYh0g="
    },
    "resolve-url": {
      "version": "0.2.1",
      "resolved": "https://registry.npmjs.org/resolve-url/-/resolve-url-0.2.1.tgz",
      "integrity": "sha1-LGN/53yJOv0qZj/iGqkIAGjiBSo="
    },
    "resolve-url-loader": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/resolve-url-loader/-/resolve-url-loader-3.1.1.tgz",
      "integrity": "sha512-K1N5xUjj7v0l2j/3Sgs5b8CjrrgtC70SmdCuZiJ8tSyb5J+uk3FoeZ4b7yTnH6j7ngI+Bc5bldHJIa8hYdu2gQ==",
      "requires": {
        "adjust-sourcemap-loader": "2.0.0",
        "camelcase": "5.3.1",
        "compose-function": "3.0.3",
        "convert-source-map": "1.7.0",
        "es6-iterator": "2.0.3",
        "loader-utils": "1.2.3",
        "postcss": "7.0.21",
        "rework": "1.0.1",
        "rework-visit": "1.0.0",
        "source-map": "0.6.1"
      },
      "dependencies": {
        "emojis-list": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz",
          "integrity": "sha1-TapNnbAPmBmIDHn6RXrlsJof04k="
        },
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.2.3",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz",
          "integrity": "sha512-fkpz8ejdnEMG3s37wGL07iSBDg99O9D5yflE9RGNH3hRdx9SOwYfnGYdZOUIZitN8E+E2vkq3MUMYMvPYl5ZZA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^2.0.0",
            "json5": "^1.0.1"
          }
        },
        "postcss": {
          "version": "7.0.21",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-7.0.21.tgz",
          "integrity": "sha512-uIFtJElxJo29QC753JzhidoAhvp/e/Exezkdhfmt8AymWT6/5B7W1WmponYWkHk2eg6sONyTch0A3nkMPun3SQ==",
          "requires": {
            "chalk": "^2.4.2",
            "source-map": "^0.6.1",
            "supports-color": "^6.1.0"
          }
        }
      }
    },
    "ret": {
      "version": "0.1.15",
      "resolved": "https://registry.npmjs.org/ret/-/ret-0.1.15.tgz",
      "integrity": "sha512-TTlYpa+OL+vMMNG24xSlQGEJ3B/RzEfUlLct7b5G/ytav+wPrplCpVMFuwzXbkecJrb6IYo1iFb0S9v37754mg=="
    },
    "rework": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/rework/-/rework-1.0.1.tgz",
      "integrity": "sha1-MIBqhBNCtUUQqkEQhQzUhTQUSqc=",
      "requires": {
        "convert-source-map": "^0.3.3",
        "css": "^2.0.0"
      },
      "dependencies": {
        "convert-source-map": {
          "version": "0.3.5",
          "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-0.3.5.tgz",
          "integrity": "sha1-8dgClQr33SYxof6+BZZVDIarMZA="
        }
      }
    },
    "rework-visit": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/rework-visit/-/rework-visit-1.0.0.tgz",
      "integrity": "sha1-mUWygD8hni96ygCtuLyfZA+ELJo="
    },
    "rgb-regex": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/rgb-regex/-/rgb-regex-1.0.1.tgz",
      "integrity": "sha1-wODWiC3w4jviVKR16O3UGRX+rrE="
    },
    "rgba-regex": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/rgba-regex/-/rgba-regex-1.0.0.tgz",
      "integrity": "sha1-QzdOLiyglosO8VI0YLfXMP8i7rM="
    },
    "rimraf": {
      "version": "2.7.1",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz",
      "integrity": "sha512-uWjbaKIK3T1OSVptzX7Nl6PvQ3qAGtKEtVRjRuazjfL3Bx5eI409VZSqgND+4UNnmzLVdPj9FqFJNPqBZFve4w==",
      "requires": {
        "glob": "^7.1.3"
      }
    },
    "ripemd160": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/ripemd160/-/ripemd160-2.0.2.tgz",
      "integrity": "sha512-ii4iagi25WusVoiC4B4lq7pbXfAp3D9v5CwfkY33vffw2+pkDjY1D8GaN7spsxvCSx8dkPqOZCEZyfxcmJG2IA==",
      "requires": {
        "hash-base": "^3.0.0",
        "inherits": "^2.0.1"
      }
    },
    "run-queue": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/run-queue/-/run-queue-1.0.3.tgz",
      "integrity": "sha1-6Eg5bwV9Ij8kOGkkYY4laUFh7Ec=",
      "requires": {
        "aproba": "^1.1.1"
      }
    },
    "safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="
    },
    "safe-regex": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/safe-regex/-/safe-regex-1.1.0.tgz",
      "integrity": "sha1-QKNmnzsHfR6UPURinhV91IAjvy4=",
      "requires": {
        "ret": "~0.1.10"
      }
    },
    "safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg=="
    },
    "sass-loader": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/sass-loader/-/sass-loader-8.0.2.tgz",
      "integrity": "sha512-7o4dbSK8/Ol2KflEmSco4jTjQoV988bM82P9CZdmo9hR3RLnvNc0ufMNdMrB0caq38JQ/FgF4/7RcbcfKzxoFQ==",
      "requires": {
        "clone-deep": "^4.0.1",
        "loader-utils": "^1.2.3",
        "neo-async": "^2.6.1",
        "schema-utils": "^2.6.1",
        "semver": "^6.3.0"
      },
      "dependencies": {
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.4.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.0.tgz",
          "integrity": "sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^3.0.0",
            "json5": "^1.0.1"
          }
        },
        "semver": {
          "version": "6.3.0",
          "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.0.tgz",
          "integrity": "sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw=="
        }
      }
    },
    "sax": {
      "version": "1.2.4",
      "resolved": "https://registry.npmjs.org/sax/-/sax-1.2.4.tgz",
      "integrity": "sha512-NqVDv9TpANUjFm0N8uM5GxL36UgKi9/atZw+x7YFnQ8ckwFGKrl4xX4yWtrey3UJm5nP1kUbnYgLopqWNSRhWw=="
    },
    "scheduler": {
      "version": "0.19.1",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.19.1.tgz",
      "integrity": "sha512-n/zwRWRYSUj0/3g/otKDRPMh6qv2SYMWNq85IEa8iZyAv8od9zDYpGSnpBEjNgcMNq6Scbu5KfIPxNF72R/2EA==",
      "requires": {
        "loose-envify": "^1.1.0",
        "object-assign": "^4.1.1"
      }
    },
    "schema-utils": {
      "version": "2.7.0",
      "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-2.7.0.tgz",
      "integrity": "sha512-0ilKFI6QQF5nxDZLFn2dMjvc4hjg/Wkg7rHd3jK6/A4a1Hl9VFdQWvgB1UMGoU94pad1P/8N7fMcEnLnSiju8A==",
      "requires": {
        "@types/json-schema": "^7.0.4",
        "ajv": "^6.12.2",
        "ajv-keywords": "^3.4.1"
      }
    },
    "section-matter": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/section-matter/-/section-matter-1.0.0.tgz",
      "integrity": "sha512-vfD3pmTzGpufjScBh50YHKzEu2lxBWhVEHsNGoEXmCmn2hKGfeNLYMzCJpe8cD7gqX7TJluOVpBkAequ6dgMmA==",
      "requires": {
        "extend-shallow": "^2.0.1",
        "kind-of": "^6.0.0"
      },
      "dependencies": {
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "requires": {
            "is-extendable": "^0.1.0"
          }
        }
      }
    },
    "semver": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-5.7.1.tgz",
      "integrity": "sha512-sauaDf/PZdVgrLTNYHRtpXa1iRiKcaebiKQ1BJdpQlWH2lCvexQdX55snPFyK7QzpudqbCI0qXFfOasHdyNDGQ=="
    },
    "serialize-javascript": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/serialize-javascript/-/serialize-javascript-4.0.0.tgz",
      "integrity": "sha512-GaNA54380uFefWghODBWEGisLZFj00nS5ACs6yHa9nLqlLpVLO8ChDGeKRjZnV4Nh4n0Qi7nhYZD/9fCPzEqkw==",
      "requires": {
        "randombytes": "^2.1.0"
      }
    },
    "set-value": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/set-value/-/set-value-2.0.1.tgz",
      "integrity": "sha512-JxHc1weCN68wRY0fhCoXpyK55m/XPHafOmK4UWD7m2CI14GMcFypt4w/0+NV5f/ZMby2F6S2wwA7fgynh9gWSw==",
      "requires": {
        "extend-shallow": "^2.0.1",
        "is-extendable": "^0.1.1",
        "is-plain-object": "^2.0.3",
        "split-string": "^3.0.1"
      },
      "dependencies": {
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "requires": {
            "is-extendable": "^0.1.0"
          }
        }
      }
    },
    "setimmediate": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz",
      "integrity": "sha1-KQy7Iy4waULX1+qbg3Mqt4VvgoU="
    },
    "sha.js": {
      "version": "2.4.11",
      "resolved": "https://registry.npmjs.org/sha.js/-/sha.js-2.4.11.tgz",
      "integrity": "sha512-QMEp5B7cftE7APOjk5Y6xgrbWu+WkLVQwk8JNjZ8nKRciZaByEW6MubieAiToS7+dwvrjGhH8jRXz3MVd0AYqQ==",
      "requires": {
        "inherits": "^2.0.1",
        "safe-buffer": "^5.0.1"
      }
    },
    "shallow-clone": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/shallow-clone/-/shallow-clone-3.0.1.tgz",
      "integrity": "sha512-/6KqX+GVUdqPuPPd2LxDDxzX6CAbjJehAAOKlNpqqUpAqPM6HeL8f+o3a+JsyGjn2lv0WY8UsTgUJjU9Ok55NA==",
      "requires": {
        "kind-of": "^6.0.2"
      }
    },
    "simple-swizzle": {
      "version": "0.2.2",
      "resolved": "https://registry.npmjs.org/simple-swizzle/-/simple-swizzle-0.2.2.tgz",
      "integrity": "sha1-pNprY1/8zMoz9w0Xy5JZLeleVXo=",
      "requires": {
        "is-arrayish": "^0.3.1"
      },
      "dependencies": {
        "is-arrayish": {
          "version": "0.3.2",
          "resolved": "https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.3.2.tgz",
          "integrity": "sha512-eVRqCvVlZbuw3GrM63ovNSNAeA1K16kaR/LRY/92w0zxQ5/1YzwblUX652i4Xs9RwAGjW9d9y6X88t8OaAJfWQ=="
        }
      }
    },
    "snapdragon": {
      "version": "0.8.2",
      "resolved": "https://registry.npmjs.org/snapdragon/-/snapdragon-0.8.2.tgz",
      "integrity": "sha512-FtyOnWN/wCHTVXOMwvSv26d+ko5vWlIDD6zoUJ7LW8vh+ZBC8QdljveRP+crNrtBwioEUWy/4dMtbBjA4ioNlg==",
      "requires": {
        "base": "^0.11.1",
        "debug": "^2.2.0",
        "define-property": "^0.2.5",
        "extend-shallow": "^2.0.1",
        "map-cache": "^0.2.2",
        "source-map": "^0.5.6",
        "source-map-resolve": "^0.5.0",
        "use": "^3.1.0"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        },
        "define-property": {
          "version": "0.2.5",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz",
          "integrity": "sha1-w1se+RjsPJkPmlvFe+BKrOxcgRY=",
          "requires": {
            "is-descriptor": "^0.1.0"
          }
        },
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "requires": {
            "is-extendable": "^0.1.0"
          }
        },
        "ms": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
        },
        "source-map": {
          "version": "0.5.7",
          "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz",
          "integrity": "sha1-igOdLRAh0i0eoUyA2OpGi6LvP8w="
        }
      }
    },
    "snapdragon-node": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/snapdragon-node/-/snapdragon-node-2.1.1.tgz",
      "integrity": "sha512-O27l4xaMYt/RSQ5TR3vpWCAB5Kb/czIcqUFOM/C4fYcLnbZUc1PkjTAMjof2pBWaSTwOUd6qUHcFGVGj7aIwnw==",
      "requires": {
        "define-property": "^1.0.0",
        "isobject": "^3.0.0",
        "snapdragon-util": "^3.0.1"
      },
      "dependencies": {
        "define-property": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz",
          "integrity": "sha1-dp66rz9KY6rTr56NMEybvnm/sOY=",
          "requires": {
            "is-descriptor": "^1.0.0"
          }
        },
        "is-accessor-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz",
          "integrity": "sha512-m5hnHTkcVsPfqx3AKlyttIPb7J+XykHvJP2B9bZDjlhLIoEq4XoK64Vg7boZlVWYK6LUY94dYPEE7Lh0ZkZKcQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-data-descriptor": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz",
          "integrity": "sha512-jbRXy1FmtAoCjQkVmIVYwuuqDFUbaOeDjmed1tOGPrsMhtJA4rD9tkgA0F1qJ3gRFRXcHYVkdeaP50Q5rE/jLQ==",
          "requires": {
            "kind-of": "^6.0.0"
          }
        },
        "is-descriptor": {
          "version": "1.0.2",
          "resolved": "https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz",
          "integrity": "sha512-2eis5WqQGV7peooDyLmNEPUrps9+SXX5c9pL3xEB+4e9HnGuDa7mB7kHxHw4CbqS9k1T2hOH3miL8n8WtiYVtg==",
          "requires": {
            "is-accessor-descriptor": "^1.0.0",
            "is-data-descriptor": "^1.0.0",
            "kind-of": "^6.0.2"
          }
        }
      }
    },
    "snapdragon-util": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/snapdragon-util/-/snapdragon-util-3.0.1.tgz",
      "integrity": "sha512-mbKkMdQKsjX4BAL4bRYTj21edOf8cN7XHdYUJEe+Zn99hVEYcMvKPct1IqNe7+AZPirn8BCDOQBHQZknqmKlZQ==",
      "requires": {
        "kind-of": "^3.2.0"
      },
      "dependencies": {
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "sort-keys": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/sort-keys/-/sort-keys-1.1.2.tgz",
      "integrity": "sha1-RBttTTRnmPG05J6JIK37oOVD+a0=",
      "requires": {
        "is-plain-obj": "^1.0.0"
      }
    },
    "source-list-map": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.1.tgz",
      "integrity": "sha512-qnQ7gVMxGNxsiL4lEuJwe/To8UnK7fAnmbGEEH8RpLouuKbeEm0lhbQVFIrNSuB+G7tVrAlVsZgETT5nljf+Iw=="
    },
    "source-map": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz",
      "integrity": "sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g=="
    },
    "source-map-resolve": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/source-map-resolve/-/source-map-resolve-0.5.3.tgz",
      "integrity": "sha512-Htz+RnsXWk5+P2slx5Jh3Q66vhQj1Cllm0zvnaY98+NFx+Dv2CF/f5O/t8x+KaNdrdIAsruNzoh/KpialbqAnw==",
      "requires": {
        "atob": "^2.1.2",
        "decode-uri-component": "^0.2.0",
        "resolve-url": "^0.2.1",
        "source-map-url": "^0.4.0",
        "urix": "^0.1.0"
      }
    },
    "source-map-support": {
      "version": "0.5.19",
      "resolved": "https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.19.tgz",
      "integrity": "sha512-Wonm7zOCIJzBGQdB+thsPar0kYuCIzYvxZwlBa87yi/Mdjv7Tip2cyVbLj5o0cFPN4EVkuTwb3GDDyUx2DGnGw==",
      "requires": {
        "buffer-from": "^1.0.0",
        "source-map": "^0.6.0"
      }
    },
    "source-map-url": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/source-map-url/-/source-map-url-0.4.0.tgz",
      "integrity": "sha1-PpNdfd1zYxuXZZlW1VEo6HtQhKM="
    },
    "space-separated-tokens": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/space-separated-tokens/-/space-separated-tokens-1.1.5.tgz",
      "integrity": "sha512-q/JSVd1Lptzhf5bkYm4ob4iWPjx0KiRe3sRFBNrVqbJkFaBm5vbbowy1mymoPNLRa52+oadOhJ+K49wsSeSjTA=="
    },
    "split-string": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/split-string/-/split-string-3.1.0.tgz",
      "integrity": "sha512-NzNVhJDYpwceVVii8/Hu6DKfD2G+NrQHlS/V/qgv763EYudVwEcMQNxd2lh+0VrUByXN/oJkl5grOhYWvQUYiw==",
      "requires": {
        "extend-shallow": "^3.0.0"
      }
    },
    "sprintf-js": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz",
      "integrity": "sha1-BOaSb2YolTVPPdAVIDYzuFcpfiw="
    },
    "ssri": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/ssri/-/ssri-6.0.1.tgz",
      "integrity": "sha512-3Wge10hNcT1Kur4PDFwEieXSCMCJs/7WvSACcrMYrNp+b8kDL1/0wJch5Ni2WrtwEa2IO8OsVfeKIciKCDx/QA==",
      "requires": {
        "figgy-pudding": "^3.5.1"
      }
    },
    "stable": {
      "version": "0.1.8",
      "resolved": "https://registry.npmjs.org/stable/-/stable-0.1.8.tgz",
      "integrity": "sha512-ji9qxRnOVfcuLDySj9qzhGSEFVobyt1kIOSkj1qZzYLzq7Tos/oUUWvotUPQLlrsidqsK6tBH89Bc9kL5zHA6w=="
    },
    "state-toggle": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/state-toggle/-/state-toggle-1.0.3.tgz",
      "integrity": "sha512-d/5Z4/2iiCnHw6Xzghyhb+GcmF89bxwgXG60wjIiZaxnymbyOmI8Hk4VqHXiVVp6u2ysaskFfXg3ekCj4WNftQ=="
    },
    "static-extend": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/static-extend/-/static-extend-0.1.2.tgz",
      "integrity": "sha1-YICcOcv/VTNyJv1eC1IPNB8ftcY=",
      "requires": {
        "define-property": "^0.2.5",
        "object-copy": "^0.1.0"
      },
      "dependencies": {
        "define-property": {
          "version": "0.2.5",
          "resolved": "https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz",
          "integrity": "sha1-w1se+RjsPJkPmlvFe+BKrOxcgRY=",
          "requires": {
            "is-descriptor": "^0.1.0"
          }
        }
      }
    },
    "stream-browserify": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/stream-browserify/-/stream-browserify-2.0.2.tgz",
      "integrity": "sha512-nX6hmklHs/gr2FuxYDltq8fJA1GDlxKQCz8O/IM4atRqBH8OORmBNgfvW5gG10GT/qQ9u0CzIvr2X5Pkt6ntqg==",
      "requires": {
        "inherits": "~2.0.1",
        "readable-stream": "^2.0.2"
      }
    },
    "stream-each": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/stream-each/-/stream-each-1.2.3.tgz",
      "integrity": "sha512-vlMC2f8I2u/bZGqkdfLQW/13Zihpej/7PmSiMQsbYddxuTsJp8vRe2x2FvVExZg7FaOds43ROAuFJwPR4MTZLw==",
      "requires": {
        "end-of-stream": "^1.1.0",
        "stream-shift": "^1.0.0"
      }
    },
    "stream-http": {
      "version": "2.8.3",
      "resolved": "https://registry.npmjs.org/stream-http/-/stream-http-2.8.3.tgz",
      "integrity": "sha512-+TSkfINHDo4J+ZobQLWiMouQYB+UVYFttRA94FpEzzJ7ZdqcL4uUUQ7WkdkI4DSozGmgBUE/a47L+38PenXhUw==",
      "requires": {
        "builtin-status-codes": "^3.0.0",
        "inherits": "^2.0.1",
        "readable-stream": "^2.3.6",
        "to-arraybuffer": "^1.0.0",
        "xtend": "^4.0.0"
      }
    },
    "stream-shift": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.1.tgz",
      "integrity": "sha512-AiisoFqQ0vbGcZgQPY1cdP2I76glaVA/RauYR4G4thNFgkTqr90yXTo4LYX60Jl+sIlPNHHdGSwo01AvbKUSVQ=="
    },
    "strict-uri-encode": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/strict-uri-encode/-/strict-uri-encode-1.1.0.tgz",
      "integrity": "sha1-J5siXfHVgrH1TmWt3UNS4Y+qBxM="
    },
    "string-hash": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/string-hash/-/string-hash-1.1.3.tgz",
      "integrity": "sha1-6Kr8CsGFW0Zmkp7X3RJ1311sgRs="
    },
    "string.prototype.trimend": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.1.tgz",
      "integrity": "sha512-LRPxFUaTtpqYsTeNKaFOw3R4bxIzWOnbQ837QfBylo8jIxtcbK/A/sMV7Q+OAV/vWo+7s25pOE10KYSjaSO06g==",
      "requires": {
        "define-properties": "^1.1.3",
        "es-abstract": "^1.17.5"
      }
    },
    "string.prototype.trimstart": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.1.tgz",
      "integrity": "sha512-XxZn+QpvrBI1FOcg6dIpxUPgWCPuNXvMD72aaRaUQv1eD4e/Qy8i/hFTe0BUmD60p/QA6bh1avmuPTfNjqVWRw==",
      "requires": {
        "define-properties": "^1.1.3",
        "es-abstract": "^1.17.5"
      }
    },
    "string_decoder": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz",
      "integrity": "sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==",
      "requires": {
        "safe-buffer": "~5.1.0"
      }
    },
    "stringify-entities": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/stringify-entities/-/stringify-entities-3.0.1.tgz",
      "integrity": "sha512-Lsk3ISA2++eJYqBMPKcr/8eby1I6L0gP0NlxF8Zja6c05yr/yCYyb2c9PwXjd08Ib3If1vn1rbs1H5ZtVuOfvQ==",
      "requires": {
        "character-entities-html4": "^1.0.0",
        "character-entities-legacy": "^1.0.0",
        "is-alphanumerical": "^1.0.0",
        "is-decimal": "^1.0.2",
        "is-hexadecimal": "^1.0.0"
      }
    },
    "strip-ansi": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz",
      "integrity": "sha1-ajhfuIU9lS1f8F0Oiq+UJ43GPc8=",
      "requires": {
        "ansi-regex": "^2.0.0"
      }
    },
    "strip-bom-string": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/strip-bom-string/-/strip-bom-string-1.0.0.tgz",
      "integrity": "sha1-5SEekiQ2n7uB1jOi8ABE3IztrZI="
    },
    "style-loader": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/style-loader/-/style-loader-1.0.0.tgz",
      "integrity": "sha512-B0dOCFwv7/eY31a5PCieNwMgMhVGFe9w+rh7s/Bx8kfFkrth9zfTZquoYvdw8URgiqxObQKcpW51Ugz1HjfdZw==",
      "requires": {
        "loader-utils": "^1.2.3",
        "schema-utils": "^2.0.1"
      },
      "dependencies": {
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.4.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.0.tgz",
          "integrity": "sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^3.0.0",
            "json5": "^1.0.1"
          }
        }
      }
    },
    "styled-jsx": {
      "version": "3.2.5",
      "resolved": "https://registry.npmjs.org/styled-jsx/-/styled-jsx-3.2.5.tgz",
      "integrity": "sha512-prEahkYwQHomUljJzXzrFnBmQrSMtWOBbXn8QeEkpfFkqMZQGshxzzp4H8ebBIsbVlHF/3+GSXMnmK/fp7qVYQ==",
      "requires": {
        "@babel/types": "7.8.3",
        "babel-plugin-syntax-jsx": "6.18.0",
        "convert-source-map": "1.7.0",
        "loader-utils": "1.2.3",
        "source-map": "0.7.3",
        "string-hash": "1.1.3",
        "stylis": "3.5.4",
        "stylis-rule-sheet": "0.0.10"
      },
      "dependencies": {
        "@babel/types": {
          "version": "7.8.3",
          "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.8.3.tgz",
          "integrity": "sha512-jBD+G8+LWpMBBWvVcdr4QysjUE4mU/syrhN17o1u3gx0/WzJB1kwiVZAXRtWbsIPOwW8pF/YJV5+nmetPzepXg==",
          "requires": {
            "esutils": "^2.0.2",
            "lodash": "^4.17.13",
            "to-fast-properties": "^2.0.0"
          }
        },
        "emojis-list": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz",
          "integrity": "sha1-TapNnbAPmBmIDHn6RXrlsJof04k="
        },
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.2.3",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz",
          "integrity": "sha512-fkpz8ejdnEMG3s37wGL07iSBDg99O9D5yflE9RGNH3hRdx9SOwYfnGYdZOUIZitN8E+E2vkq3MUMYMvPYl5ZZA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^2.0.0",
            "json5": "^1.0.1"
          }
        },
        "source-map": {
          "version": "0.7.3",
          "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.7.3.tgz",
          "integrity": "sha512-CkCj6giN3S+n9qrYiBTX5gystlENnRW5jZeNLHpe6aue+SrHcG5VYwujhW9s4dY31mEGsxBDrHR6oI69fTXsaQ=="
        }
      }
    },
    "stylehacks": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/stylehacks/-/stylehacks-4.0.3.tgz",
      "integrity": "sha512-7GlLk9JwlElY4Y6a/rmbH2MhVlTyVmiJd1PfTCqFaIBEGMYNsrO/v3SeGTdhBThLg4Z+NbOk/qFMwCa+J+3p/g==",
      "requires": {
        "browserslist": "^4.0.0",
        "postcss": "^7.0.0",
        "postcss-selector-parser": "^3.0.0"
      },
      "dependencies": {
        "postcss-selector-parser": {
          "version": "3.1.2",
          "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-3.1.2.tgz",
          "integrity": "sha512-h7fJ/5uWuRVyOtkO45pnt1Ih40CEleeyCHzipqAZO2e5H20g25Y48uYnFUiShvY4rZWNJ/Bib/KVPmanaCtOhA==",
          "requires": {
            "dot-prop": "^5.2.0",
            "indexes-of": "^1.0.1",
            "uniq": "^1.0.1"
          }
        }
      }
    },
    "stylis": {
      "version": "3.5.4",
      "resolved": "https://registry.npmjs.org/stylis/-/stylis-3.5.4.tgz",
      "integrity": "sha512-8/3pSmthWM7lsPBKv7NXkzn2Uc9W7NotcwGNpJaa3k7WMM1XDCA4MgT5k/8BIexd5ydZdboXtU90XH9Ec4Bv/Q=="
    },
    "stylis-rule-sheet": {
      "version": "0.0.10",
      "resolved": "https://registry.npmjs.org/stylis-rule-sheet/-/stylis-rule-sheet-0.0.10.tgz",
      "integrity": "sha512-nTbZoaqoBnmK+ptANthb10ZRZOGC+EmTLLUxeYIuHNkEKcmKgXX1XWKkUBT2Ac4es3NybooPe0SmvKdhKJZAuw=="
    },
    "supports-color": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-6.1.0.tgz",
      "integrity": "sha512-qe1jfm1Mg7Nq/NSh6XE24gPXROEVsWHxC1LIx//XNlD9iw7YZQGjZNjYN7xGaEG6iKdA8EtNFW6R0gjnVXp+wQ==",
      "requires": {
        "has-flag": "^3.0.0"
      }
    },
    "svgo": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/svgo/-/svgo-1.3.2.tgz",
      "integrity": "sha512-yhy/sQYxR5BkC98CY7o31VGsg014AKLEPxdfhora76l36hD9Rdy5NZA/Ocn6yayNPgSamYdtX2rFJdcv07AYVw==",
      "requires": {
        "chalk": "^2.4.1",
        "coa": "^2.0.2",
        "css-select": "^2.0.0",
        "css-select-base-adapter": "^0.1.1",
        "css-tree": "1.0.0-alpha.37",
        "csso": "^4.0.2",
        "js-yaml": "^3.13.1",
        "mkdirp": "~0.5.1",
        "object.values": "^1.1.0",
        "sax": "~1.2.4",
        "stable": "^0.1.8",
        "unquote": "~1.1.1",
        "util.promisify": "~1.0.0"
      }
    },
    "tapable": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/tapable/-/tapable-1.1.3.tgz",
      "integrity": "sha512-4WK/bYZmj8xLr+HUCODHGF1ZFzsYffasLUgEiMBY4fgtltdO6B4WJtlSbPaDTLpYTcGVwM2qLnFTICEcNxs3kA=="
    },
    "terser": {
      "version": "4.6.8",
      "resolved": "https://registry.npmjs.org/terser/-/terser-4.6.8.tgz",
      "integrity": "sha512-drV7ga6ZlIpBtitvb87Uk7P7gAJkCt3j/TqZr9wwF4Dlt0MBn52ANIAyuvP1F605WdPY4w6vT63u6KTWqaXFRQ==",
      "requires": {
        "commander": "^2.20.0",
        "source-map": "~0.6.1",
        "source-map-support": "~0.5.12"
      }
    },
    "terser-webpack-plugin": {
      "version": "1.4.5",
      "resolved": "https://registry.npmjs.org/terser-webpack-plugin/-/terser-webpack-plugin-1.4.5.tgz",
      "integrity": "sha512-04Rfe496lN8EYruwi6oPQkG0vo8C+HT49X687FZnpPF0qMAIHONI6HEXYPKDOE8e5HjXTyKfqRd/agHtH0kOtw==",
      "requires": {
        "cacache": "^12.0.2",
        "find-cache-dir": "^2.1.0",
        "is-wsl": "^1.1.0",
        "schema-utils": "^1.0.0",
        "serialize-javascript": "^4.0.0",
        "source-map": "^0.6.1",
        "terser": "^4.1.2",
        "webpack-sources": "^1.4.0",
        "worker-farm": "^1.7.0"
      },
      "dependencies": {
        "find-cache-dir": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-2.1.0.tgz",
          "integrity": "sha512-Tq6PixE0w/VMFfCgbONnkiQIVol/JJL7nRMi20fqzA4NRs9AfeqMGeRdPi3wIhYkxjeBaWh2rxwapn5Tu3IqOQ==",
          "requires": {
            "commondir": "^1.0.1",
            "make-dir": "^2.0.0",
            "pkg-dir": "^3.0.0"
          }
        },
        "find-up": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz",
          "integrity": "sha512-1yD6RmLI1XBfxugvORwlck6f75tYL+iR0jqwsOrOxMZyGYqUuDhJ0l4AXdO1iX/FTs9cBAMEk1gWSEx1kSbylg==",
          "requires": {
            "locate-path": "^3.0.0"
          }
        },
        "locate-path": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz",
          "integrity": "sha512-7AO748wWnIhNqAuaty2ZWHkQHRSNfPVIsPIfwEOWO22AmaoVrWavlOcMR5nzTLNYvp36X220/maaRsrec1G65A==",
          "requires": {
            "p-locate": "^3.0.0",
            "path-exists": "^3.0.0"
          }
        },
        "make-dir": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/make-dir/-/make-dir-2.1.0.tgz",
          "integrity": "sha512-LS9X+dc8KLxXCb8dni79fLIIUA5VyZoyjSMCwTluaXA0o27cCK0bhXkpgw+sTXVpPy/lSO57ilRixqk0vDmtRA==",
          "requires": {
            "pify": "^4.0.1",
            "semver": "^5.6.0"
          }
        },
        "p-locate": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz",
          "integrity": "sha512-x+12w/To+4GFfgJhBEpiDcLozRJGegY+Ei7/z0tSLkMmxGZNybVMSfWj9aJn8Z5Fc7dBUNJOOVgPv2H7IwulSQ==",
          "requires": {
            "p-limit": "^2.0.0"
          }
        },
        "path-exists": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz",
          "integrity": "sha1-zg6+ql94yxiSXqfYENe1mwEP1RU="
        },
        "pkg-dir": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/pkg-dir/-/pkg-dir-3.0.0.tgz",
          "integrity": "sha512-/E57AYkoeQ25qkxMj5PBOVgF8Kiu/h7cYS30Z5+R7WaiCCBfLq58ZI/dSeaEKb9WVJV5n/03QwrN3IeWIFllvw==",
          "requires": {
            "find-up": "^3.0.0"
          }
        },
        "schema-utils": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-1.0.0.tgz",
          "integrity": "sha512-i27Mic4KovM/lnGsy8whRCHhc7VicJajAjTrYg11K9zfZXnYIt4k5F+kZkwjnrhKzLic/HLU4j11mjsz2G/75g==",
          "requires": {
            "ajv": "^6.1.0",
            "ajv-errors": "^1.0.0",
            "ajv-keywords": "^3.1.0"
          }
        }
      }
    },
    "through2": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/through2/-/through2-2.0.5.tgz",
      "integrity": "sha512-/mrRod8xqpA+IHSLyGCQ2s8SPHiCDEeQJSep1jqLYeEUClOFG2Qsh+4FU6G9VeqpZnGW/Su8LQGc4YKni5rYSQ==",
      "requires": {
        "readable-stream": "~2.3.6",
        "xtend": "~4.0.1"
      }
    },
    "timers-browserify": {
      "version": "2.0.11",
      "resolved": "https://registry.npmjs.org/timers-browserify/-/timers-browserify-2.0.11.tgz",
      "integrity": "sha512-60aV6sgJ5YEbzUdn9c8kYGIqOubPoUdqQCul3SBAsRCZ40s6Y5cMcrW4dt3/k/EsbLVJNl9n6Vz3fTc+k2GeKQ==",
      "requires": {
        "setimmediate": "^1.0.4"
      }
    },
    "timsort": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/timsort/-/timsort-0.3.0.tgz",
      "integrity": "sha1-QFQRqOfmM5/mTbmiNN4R3DHgK9Q="
    },
    "to-arraybuffer": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/to-arraybuffer/-/to-arraybuffer-1.0.1.tgz",
      "integrity": "sha1-fSKbH8xjfkZsoIEYCDanqr/4P0M="
    },
    "to-fast-properties": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz",
      "integrity": "sha1-3F5pjL0HkmW8c+A3doGk5Og/YW4="
    },
    "to-object-path": {
      "version": "0.3.0",
      "resolved": "https://registry.npmjs.org/to-object-path/-/to-object-path-0.3.0.tgz",
      "integrity": "sha1-KXWIt7Dn4KwI4E5nL4XB9JmeF68=",
      "requires": {
        "kind-of": "^3.0.2"
      },
      "dependencies": {
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "requires": {
            "is-buffer": "^1.1.5"
          }
        }
      }
    },
    "to-regex": {
      "version": "3.0.2",
      "resolved": "https://registry.npmjs.org/to-regex/-/to-regex-3.0.2.tgz",
      "integrity": "sha512-FWtleNAtZ/Ki2qtqej2CXTOayOH9bHDQF+Q48VpWyDXjbYxA4Yz8iDB31zXOBUlOHHKidDbqGVrTUvQMPmBGBw==",
      "requires": {
        "define-property": "^2.0.2",
        "extend-shallow": "^3.0.2",
        "regex-not": "^1.0.2",
        "safe-regex": "^1.1.0"
      }
    },
    "to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "requires": {
        "is-number": "^7.0.0"
      }
    },
    "traverse": {
      "version": "0.6.6",
      "resolved": "https://registry.npmjs.org/traverse/-/traverse-0.6.6.tgz",
      "integrity": "sha1-y99WD9e5r2MlAv7UD5GMFX6pcTc="
    },
    "trim": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/trim/-/trim-0.0.1.tgz",
      "integrity": "sha1-WFhUf2spB1fulczMZm+1AITEYN0="
    },
    "trim-lines": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/trim-lines/-/trim-lines-1.1.3.tgz",
      "integrity": "sha512-E0ZosSWYK2mkSu+KEtQ9/KqarVjA9HztOSX+9FDdNacRAq29RRV6ZQNgob3iuW8Htar9vAfEa6yyt5qBAHZDBA=="
    },
    "trim-trailing-lines": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/trim-trailing-lines/-/trim-trailing-lines-1.1.3.tgz",
      "integrity": "sha512-4ku0mmjXifQcTVfYDfR5lpgV7zVqPg6zV9rdZmwOPqq0+Zq19xDqEgagqVbc4pOOShbncuAOIs59R3+3gcF3ZA=="
    },
    "trough": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/trough/-/trough-1.0.5.tgz",
      "integrity": "sha512-rvuRbTarPXmMb79SmzEp8aqXNKcK+y0XaB298IXueQ8I2PsrATcPBCSPyK/dDNa2iWOhKlfNnOjdAOTBU/nkFA=="
    },
    "ts-pnp": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/ts-pnp/-/ts-pnp-1.2.0.tgz",
      "integrity": "sha512-csd+vJOb/gkzvcCHgTGSChYpy5f1/XKNsmvBGO4JXS+z1v2HobugDz4s1IeFXM3wZB44uczs+eazB5Q/ccdhQw=="
    },
    "tslib": {
      "version": "1.13.0",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-1.13.0.tgz",
      "integrity": "sha512-i/6DQjL8Xf3be4K/E6Wgpekn5Qasl1usyw++dAA35Ue5orEn65VIxOA+YvNNl9HV3qv70T7CNwjODHZrLwvd1Q=="
    },
    "tty-browserify": {
      "version": "0.0.0",
      "resolved": "https://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.0.tgz",
      "integrity": "sha1-oVe6QC2iTpv5V/mqadUk7tQpAaY="
    },
    "type": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/type/-/type-1.2.0.tgz",
      "integrity": "sha512-+5nt5AAniqsCnu2cEQQdpzCAh33kVx8n0VoFidKpB1dVVLAN/F+bgVOqOJqOnEnrhp222clB5p3vUlD+1QAnfg=="
    },
    "typedarray": {
      "version": "0.0.6",
      "resolved": "https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz",
      "integrity": "sha1-hnrHTjhkGHsdPUfZlqeOxciDB3c="
    },
    "unherit": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/unherit/-/unherit-1.1.3.tgz",
      "integrity": "sha512-Ft16BJcnapDKp0+J/rqFC3Rrk6Y/Ng4nzsC028k2jdDII/rdZ7Wd3pPT/6+vIIxRagwRc9K0IUX0Ra4fKvw+WQ==",
      "requires": {
        "inherits": "^2.0.0",
        "xtend": "^4.0.0"
      }
    },
    "unicode-canonical-property-names-ecmascript": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-1.0.4.tgz",
      "integrity": "sha512-jDrNnXWHd4oHiTZnx/ZG7gtUTVp+gCcTTKr8L0HjlwphROEW3+Him+IpvC+xcJEFegapiMZyZe02CyuOnRmbnQ=="
    },
    "unicode-match-property-ecmascript": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-1.0.4.tgz",
      "integrity": "sha512-L4Qoh15vTfntsn4P1zqnHulG0LdXgjSO035fEpdtp6YxXhMT51Q6vgM5lYdG/5X3MjS+k/Y9Xw4SFCY9IkR0rg==",
      "requires": {
        "unicode-canonical-property-names-ecmascript": "^1.0.4",
        "unicode-property-aliases-ecmascript": "^1.0.4"
      }
    },
    "unicode-match-property-value-ecmascript": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-1.2.0.tgz",
      "integrity": "sha512-wjuQHGQVofmSJv1uVISKLE5zO2rNGzM/KCYZch/QQvez7C1hUhBIuZ701fYXExuufJFMPhv2SyL8CyoIfMLbIQ=="
    },
    "unicode-property-aliases-ecmascript": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-1.1.0.tgz",
      "integrity": "sha512-PqSoPh/pWetQ2phoj5RLiaqIk4kCNwoV3CI+LfGmWLKI3rE3kl1h59XpX2BjgDrmbxD9ARtQobPGU1SguCYuQg=="
    },
    "unified": {
      "version": "9.2.0",
      "resolved": "https://registry.npmjs.org/unified/-/unified-9.2.0.tgz",
      "integrity": "sha512-vx2Z0vY+a3YoTj8+pttM3tiJHCwY5UFbYdiWrwBEbHmK8pvsPj2rtAX2BFfgXen8T39CJWblWRDT4L5WGXtDdg==",
      "requires": {
        "bail": "^1.0.0",
        "extend": "^3.0.0",
        "is-buffer": "^2.0.0",
        "is-plain-obj": "^2.0.0",
        "trough": "^1.0.0",
        "vfile": "^4.0.0"
      },
      "dependencies": {
        "is-buffer": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-2.0.4.tgz",
          "integrity": "sha512-Kq1rokWXOPXWuaMAqZiJW4XxsmD9zGx9q4aePabbn3qCRGedtH7Cm+zV8WETitMfu1wdh+Rvd6w5egwSngUX2A=="
        },
        "is-plain-obj": {
          "version": "2.1.0",
          "resolved": "https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-2.1.0.tgz",
          "integrity": "sha512-YWnfyRwxL/+SsrWYfOpUtz5b3YD+nyfkHvjbcanzk8zgyO4ASD67uVMRt8k5bM4lLMDnXfriRhOpemw+NfT1eA=="
        }
      }
    },
    "union-value": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/union-value/-/union-value-1.0.1.tgz",
      "integrity": "sha512-tJfXmxMeWYnczCVs7XAEvIV7ieppALdyepWMkHkwciRpZraG/xwT+s2JN8+pr1+8jCRf80FFzvr+MpQeeoF4Xg==",
      "requires": {
        "arr-union": "^3.1.0",
        "get-value": "^2.0.6",
        "is-extendable": "^0.1.1",
        "set-value": "^2.0.1"
      }
    },
    "uniq": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/uniq/-/uniq-1.0.1.tgz",
      "integrity": "sha1-sxxa6CVIRKOoKBVBzisEuGWnNP8="
    },
    "uniqs": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/uniqs/-/uniqs-2.0.0.tgz",
      "integrity": "sha1-/+3ks2slKQaW5uFl1KWe25mOawI="
    },
    "unique-filename": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz",
      "integrity": "sha512-Vmp0jIp2ln35UTXuryvjzkjGdRyf9b2lTXuSYUiPmzRcl3FDtYqAwOnTJkAngD9SWhnoJzDbTKwaOrZ+STtxNQ==",
      "requires": {
        "unique-slug": "^2.0.0"
      }
    },
    "unique-slug": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.2.tgz",
      "integrity": "sha512-zoWr9ObaxALD3DOPfjPSqxt4fnZiWblxHIgeWqW8x7UqDzEtHEQLzji2cuJYQFCU6KmoJikOYAZlrTHHebjx2w==",
      "requires": {
        "imurmurhash": "^0.1.4"
      }
    },
    "unist-builder": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/unist-builder/-/unist-builder-2.0.3.tgz",
      "integrity": "sha512-f98yt5pnlMWlzP539tPc4grGMsFaQQlP/vM396b00jngsiINumNmsY8rkXjfoi1c6QaM8nQ3vaGDuoKWbe/1Uw=="
    },
    "unist-util-generated": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/unist-util-generated/-/unist-util-generated-1.1.5.tgz",
      "integrity": "sha512-1TC+NxQa4N9pNdayCYA1EGUOCAO0Le3fVp7Jzns6lnua/mYgwHo0tz5WUAfrdpNch1RZLHc61VZ1SDgrtNXLSw=="
    },
    "unist-util-is": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/unist-util-is/-/unist-util-is-4.0.2.tgz",
      "integrity": "sha512-Ofx8uf6haexJwI1gxWMGg6I/dLnF2yE+KibhD3/diOqY2TinLcqHXCV6OI5gFVn3xQqDH+u0M625pfKwIwgBKQ=="
    },
    "unist-util-position": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/unist-util-position/-/unist-util-position-3.1.0.tgz",
      "integrity": "sha512-w+PkwCbYSFw8vpgWD0v7zRCl1FpY3fjDSQ3/N/wNd9Ffa4gPi8+4keqt99N3XW6F99t/mUzp2xAhNmfKWp95QA=="
    },
    "unist-util-remove-position": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/unist-util-remove-position/-/unist-util-remove-position-2.0.1.tgz",
      "integrity": "sha512-fDZsLYIe2uT+oGFnuZmy73K6ZxOPG/Qcm+w7jbEjaFcJgbQ6cqjs/eSPzXhsmGpAsWPkqZM9pYjww5QTn3LHMA==",
      "requires": {
        "unist-util-visit": "^2.0.0"
      }
    },
    "unist-util-stringify-position": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/unist-util-stringify-position/-/unist-util-stringify-position-2.0.3.tgz",
      "integrity": "sha512-3faScn5I+hy9VleOq/qNbAd6pAx7iH5jYBMS9I1HgQVijz/4mv5Bvw5iw1sC/90CODiKo81G/ps8AJrISn687g==",
      "requires": {
        "@types/unist": "^2.0.2"
      }
    },
    "unist-util-visit": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/unist-util-visit/-/unist-util-visit-2.0.3.tgz",
      "integrity": "sha512-iJ4/RczbJMkD0712mGktuGpm/U4By4FfDonL7N/9tATGIF4imikjOuagyMY53tnZq3NP6BcmlrHhEKAfGWjh7Q==",
      "requires": {
        "@types/unist": "^2.0.0",
        "unist-util-is": "^4.0.0",
        "unist-util-visit-parents": "^3.0.0"
      }
    },
    "unist-util-visit-parents": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/unist-util-visit-parents/-/unist-util-visit-parents-3.1.0.tgz",
      "integrity": "sha512-0g4wbluTF93npyPrp/ymd3tCDTMnP0yo2akFD2FIBAYXq/Sga3lwaU1D8OYKbtpioaI6CkDcQ6fsMnmtzt7htw==",
      "requires": {
        "@types/unist": "^2.0.0",
        "unist-util-is": "^4.0.0"
      }
    },
    "unquote": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/unquote/-/unquote-1.1.1.tgz",
      "integrity": "sha1-j97XMk7G6IoP+LkF58CYzcCG1UQ="
    },
    "unset-value": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unset-value/-/unset-value-1.0.0.tgz",
      "integrity": "sha1-g3aHP30jNRef+x5vw6jtDfyKtVk=",
      "requires": {
        "has-value": "^0.3.1",
        "isobject": "^3.0.0"
      },
      "dependencies": {
        "has-value": {
          "version": "0.3.1",
          "resolved": "https://registry.npmjs.org/has-value/-/has-value-0.3.1.tgz",
          "integrity": "sha1-ex9YutpiyoJ+wKIHgCVlSEWZXh8=",
          "requires": {
            "get-value": "^2.0.3",
            "has-values": "^0.1.4",
            "isobject": "^2.0.0"
          },
          "dependencies": {
            "isobject": {
              "version": "2.1.0",
              "resolved": "https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz",
              "integrity": "sha1-8GVWEJaj8dou9GJy+BXIQNh+DIk=",
              "requires": {
                "isarray": "1.0.0"
              }
            }
          }
        },
        "has-values": {
          "version": "0.1.4",
          "resolved": "https://registry.npmjs.org/has-values/-/has-values-0.1.4.tgz",
          "integrity": "sha1-bWHeldkd/Km5oCCJrThL/49it3E="
        }
      }
    },
    "upath": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/upath/-/upath-1.2.0.tgz",
      "integrity": "sha512-aZwGpamFO61g3OlfT7OQCHqhGnW43ieH9WZeP7QxN/G/jS4jfqUkZxoryvJgVPEcrl5NL/ggHsSmLMHuH64Lhg==",
      "optional": true
    },
    "uri-js": {
      "version": "4.2.2",
      "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.2.2.tgz",
      "integrity": "sha512-KY9Frmirql91X2Qgjry0Wd4Y+YTdrdZheS8TFwvkbLWf/G5KNJDCh6pKL5OZctEW4+0Baa5idK2ZQuELRwPznQ==",
      "requires": {
        "punycode": "^2.1.0"
      }
    },
    "urix": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/urix/-/urix-0.1.0.tgz",
      "integrity": "sha1-2pN/emLiH+wf0Y1Js1wpNQZ6bHI="
    },
    "url": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/url/-/url-0.11.0.tgz",
      "integrity": "sha1-ODjpfPxgUh63PFJajlW/3Z4uKPE=",
      "requires": {
        "punycode": "1.3.2",
        "querystring": "0.2.0"
      },
      "dependencies": {
        "punycode": {
          "version": "1.3.2",
          "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.3.2.tgz",
          "integrity": "sha1-llOgNvt8HuQjQvIyXM7v6jkmxI0="
        }
      }
    },
    "use": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/use/-/use-3.1.1.tgz",
      "integrity": "sha512-cwESVXlO3url9YWlFW/TA9cshCEhtu7IKJ/p5soJ/gGpj7vbvFrAY/eIioQ6Dw23KjZhYgiIo8HOs1nQ2vr/oQ=="
    },
    "use-subscription": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/use-subscription/-/use-subscription-1.1.1.tgz",
      "integrity": "sha512-gk4fPTYvNhs6Ia7u8/+K7bM7sZ7O7AMfWtS+zPO8luH+zWuiGgGcrW0hL4MRWZSzXo+4ofNorf87wZwBKz2YdQ=="
    },
    "util": {
      "version": "0.10.3",
      "resolved": "https://registry.npmjs.org/util/-/util-0.10.3.tgz",
      "integrity": "sha1-evsa/lCAUkZInj23/g7TeTNqwPk=",
      "requires": {
        "inherits": "2.0.1"
      }
    },
    "util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha1-RQ1Nyfpw3nMnYvvS1KKJgUGaDM8="
    },
    "util.promisify": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/util.promisify/-/util.promisify-1.0.1.tgz",
      "integrity": "sha512-g9JpC/3He3bm38zsLupWryXHoEcS22YHthuPQSJdMy6KNrzIRzWqcsHzD/WUnqe45whVou4VIsPew37DoXWNrA==",
      "requires": {
        "define-properties": "^1.1.3",
        "es-abstract": "^1.17.2",
        "has-symbols": "^1.0.1",
        "object.getownpropertydescriptors": "^2.1.0"
      }
    },
    "vendors": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/vendors/-/vendors-1.0.4.tgz",
      "integrity": "sha512-/juG65kTL4Cy2su4P8HjtkTxk6VmJDiOPBufWniqQ6wknac6jNiXS9vU+hO3wgusiyqWlzTbVHi0dyJqRONg3w=="
    },
    "vfile": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/vfile/-/vfile-4.2.0.tgz",
      "integrity": "sha512-a/alcwCvtuc8OX92rqqo7PflxiCgXRFjdyoGVuYV+qbgCb0GgZJRvIgCD4+U/Kl1yhaRsaTwksF88xbPyGsgpw==",
      "requires": {
        "@types/unist": "^2.0.0",
        "is-buffer": "^2.0.0",
        "replace-ext": "1.0.0",
        "unist-util-stringify-position": "^2.0.0",
        "vfile-message": "^2.0.0"
      },
      "dependencies": {
        "is-buffer": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-2.0.4.tgz",
          "integrity": "sha512-Kq1rokWXOPXWuaMAqZiJW4XxsmD9zGx9q4aePabbn3qCRGedtH7Cm+zV8WETitMfu1wdh+Rvd6w5egwSngUX2A=="
        }
      }
    },
    "vfile-location": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/vfile-location/-/vfile-location-3.1.0.tgz",
      "integrity": "sha512-FCZ4AN9xMcjFIG1oGmZKo61PjwJHRVA+0/tPUP2ul4uIwjGGndIxavEMRpWn5p4xwm/ZsdXp9YNygf1ZyE4x8g=="
    },
    "vfile-message": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/vfile-message/-/vfile-message-2.0.4.tgz",
      "integrity": "sha512-DjssxRGkMvifUOJre00juHoP9DPWuzjxKuMDrhNbk2TdaYYBNMStsNhEOt3idrtI12VQYM/1+iM0KOzXi4pxwQ==",
      "requires": {
        "@types/unist": "^2.0.0",
        "unist-util-stringify-position": "^2.0.0"
      }
    },
    "vm-browserify": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vm-browserify/-/vm-browserify-1.1.2.tgz",
      "integrity": "sha512-2ham8XPWTONajOR0ohOKOHXkm3+gaBmGut3SRuu75xLd/RRaY6vqgh8NBYYk7+RW3u5AtzPQZG8F10LHkl0lAQ=="
    },
    "watchpack": {
      "version": "2.0.0-beta.13",
      "resolved": "https://registry.npmjs.org/watchpack/-/watchpack-2.0.0-beta.13.tgz",
      "integrity": "sha512-ZEFq2mx/k5qgQwgi6NOm+2ImICb8ngAkA/rZ6oyXZ7SgPn3pncf+nfhYTCrs3lmHwOxnPtGLTOuFLfpSMh1VMA==",
      "requires": {
        "glob-to-regexp": "^0.4.1",
        "graceful-fs": "^4.1.2"
      }
    },
    "watchpack-chokidar2": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/watchpack-chokidar2/-/watchpack-chokidar2-2.0.0.tgz",
      "integrity": "sha512-9TyfOyN/zLUbA288wZ8IsMZ+6cbzvsNyEzSBp6e/zkifi6xxbl8SmQ/CxQq32k8NNqrdVEVUVSEf56L4rQ/ZxA==",
      "optional": true,
      "requires": {
        "chokidar": "^2.1.8"
      },
      "dependencies": {
        "anymatch": {
          "version": "2.0.0",
          "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-2.0.0.tgz",
          "integrity": "sha512-5teOsQWABXHHBFP9y3skS5P3d/WfWXpv3FUpy+LorMrNYaT9pI4oLMQX7jzQ2KklNpGpWHzdCXTDT2Y3XGlZBw==",
          "optional": true,
          "requires": {
            "micromatch": "^3.1.4",
            "normalize-path": "^2.1.1"
          },
          "dependencies": {
            "normalize-path": {
              "version": "2.1.1",
              "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz",
              "integrity": "sha1-GrKLVW4Zg2Oowab35vogE3/mrtk=",
              "optional": true,
              "requires": {
                "remove-trailing-separator": "^1.0.1"
              }
            }
          }
        },
        "binary-extensions": {
          "version": "1.13.1",
          "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-1.13.1.tgz",
          "integrity": "sha512-Un7MIEDdUC5gNpcGDV97op1Ywk748MpHcFTHoYs6qnj1Z3j7I53VG3nwZhKzoBZmbdRNnb6WRdFlwl7tSDuZGw==",
          "optional": true
        },
        "braces": {
          "version": "2.3.2",
          "resolved": "https://registry.npmjs.org/braces/-/braces-2.3.2.tgz",
          "integrity": "sha512-aNdbnj9P8PjdXU4ybaWLK2IF3jc/EoDYbC7AazW6to3TRsfXxscC9UXOB5iDiEQrkyIbWp2SLQda4+QAa7nc3w==",
          "optional": true,
          "requires": {
            "arr-flatten": "^1.1.0",
            "array-unique": "^0.3.2",
            "extend-shallow": "^2.0.1",
            "fill-range": "^4.0.0",
            "isobject": "^3.0.1",
            "repeat-element": "^1.1.2",
            "snapdragon": "^0.8.1",
            "snapdragon-node": "^2.0.1",
            "split-string": "^3.0.2",
            "to-regex": "^3.0.1"
          }
        },
        "chokidar": {
          "version": "2.1.8",
          "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-2.1.8.tgz",
          "integrity": "sha512-ZmZUazfOzf0Nve7duiCKD23PFSCs4JPoYyccjUFF3aQkQadqBhfzhjkwBH2mNOG9cTBwhamM37EIsIkZw3nRgg==",
          "optional": true,
          "requires": {
            "anymatch": "^2.0.0",
            "async-each": "^1.0.1",
            "braces": "^2.3.2",
            "fsevents": "^1.2.7",
            "glob-parent": "^3.1.0",
            "inherits": "^2.0.3",
            "is-binary-path": "^1.0.0",
            "is-glob": "^4.0.0",
            "normalize-path": "^3.0.0",
            "path-is-absolute": "^1.0.0",
            "readdirp": "^2.2.1",
            "upath": "^1.1.1"
          }
        },
        "extend-shallow": {
          "version": "2.0.1",
          "resolved": "https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz",
          "integrity": "sha1-Ua99YUrZqfYQ6huvu5idaxxWiQ8=",
          "optional": true,
          "requires": {
            "is-extendable": "^0.1.0"
          }
        },
        "fill-range": {
          "version": "4.0.0",
          "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-4.0.0.tgz",
          "integrity": "sha1-1USBHUKPmOsGpj3EAtJAPDKMOPc=",
          "optional": true,
          "requires": {
            "extend-shallow": "^2.0.1",
            "is-number": "^3.0.0",
            "repeat-string": "^1.6.1",
            "to-regex-range": "^2.1.0"
          }
        },
        "fsevents": {
          "version": "1.2.13",
          "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-1.2.13.tgz",
          "integrity": "sha512-oWb1Z6mkHIskLzEJ/XWX0srkpkTQ7vaopMQkyaEIoq0fmtFVxOthb8cCxeT+p3ynTdkk/RZwbgG4brR5BeWECw==",
          "optional": true
        },
        "glob-parent": {
          "version": "3.1.0",
          "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-3.1.0.tgz",
          "integrity": "sha1-nmr2KZ2NO9K9QEMIMr0RPfkGxa4=",
          "optional": true,
          "requires": {
            "is-glob": "^3.1.0",
            "path-dirname": "^1.0.0"
          },
          "dependencies": {
            "is-glob": {
              "version": "3.1.0",
              "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-3.1.0.tgz",
              "integrity": "sha1-e6WuJCF4BKxwcHuWkiVnSGzD6Eo=",
              "optional": true,
              "requires": {
                "is-extglob": "^2.1.0"
              }
            }
          }
        },
        "inherits": {
          "version": "2.0.4",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz",
          "integrity": "sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==",
          "optional": true
        },
        "is-binary-path": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz",
          "integrity": "sha1-dfFmQrSA8YenEcgUFh/TpKdlWJg=",
          "optional": true,
          "requires": {
            "binary-extensions": "^1.0.0"
          }
        },
        "is-number": {
          "version": "3.0.0",
          "resolved": "https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz",
          "integrity": "sha1-JP1iAaR4LPUFYcgQJ2r8fRLXEZU=",
          "optional": true,
          "requires": {
            "kind-of": "^3.0.2"
          }
        },
        "kind-of": {
          "version": "3.2.2",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz",
          "integrity": "sha1-MeohpzS6ubuw8yRm2JOupR5KPGQ=",
          "optional": true,
          "requires": {
            "is-buffer": "^1.1.5"
          }
        },
        "readdirp": {
          "version": "2.2.1",
          "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-2.2.1.tgz",
          "integrity": "sha512-1JU/8q+VgFZyxwrJ+SVIOsh+KywWGpds3NTqikiKpDMZWScmAYyKIgqkO+ARvNWJfXeXR1zxz7aHF4u4CyH6vQ==",
          "optional": true,
          "requires": {
            "graceful-fs": "^4.1.11",
            "micromatch": "^3.1.10",
            "readable-stream": "^2.0.2"
          }
        },
        "to-regex-range": {
          "version": "2.1.1",
          "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-2.1.1.tgz",
          "integrity": "sha1-fIDBe53+vlmeJzZ+DU3VWQFB2zg=",
          "optional": true,
          "requires": {
            "is-number": "^3.0.0",
            "repeat-string": "^1.6.1"
          }
        }
      }
    },
    "webpack": {
      "version": "4.42.1",
      "resolved": "https://registry.npmjs.org/webpack/-/webpack-4.42.1.tgz",
      "integrity": "sha512-SGfYMigqEfdGchGhFFJ9KyRpQKnipvEvjc1TwrXEPCM6H5Wywu10ka8o3KGrMzSMxMQKt8aCHUFh5DaQ9UmyRg==",
      "requires": {
        "@webassemblyjs/ast": "1.9.0",
        "@webassemblyjs/helper-module-context": "1.9.0",
        "@webassemblyjs/wasm-edit": "1.9.0",
        "@webassemblyjs/wasm-parser": "1.9.0",
        "acorn": "^6.2.1",
        "ajv": "^6.10.2",
        "ajv-keywords": "^3.4.1",
        "chrome-trace-event": "^1.0.2",
        "enhanced-resolve": "^4.1.0",
        "eslint-scope": "^4.0.3",
        "json-parse-better-errors": "^1.0.2",
        "loader-runner": "^2.4.0",
        "loader-utils": "^1.2.3",
        "memory-fs": "^0.4.1",
        "micromatch": "^3.1.10",
        "mkdirp": "^0.5.3",
        "neo-async": "^2.6.1",
        "node-libs-browser": "^2.2.1",
        "schema-utils": "^1.0.0",
        "tapable": "^1.1.3",
        "terser-webpack-plugin": "^1.4.3",
        "watchpack": "^1.6.0",
        "webpack-sources": "^1.4.1"
      },
      "dependencies": {
        "json5": {
          "version": "1.0.1",
          "resolved": "https://registry.npmjs.org/json5/-/json5-1.0.1.tgz",
          "integrity": "sha512-aKS4WQjPenRxiQsC93MNfjx+nbF4PAdYzmd/1JIj8HYzqfbu86beTuNgXDzPknWk0n0uARlyewZo4s++ES36Ow==",
          "requires": {
            "minimist": "^1.2.0"
          }
        },
        "loader-utils": {
          "version": "1.4.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.4.0.tgz",
          "integrity": "sha512-qH0WSMBtn/oHuwjy/NucEgbx5dbxxnxup9s4PVXJUDHZBQY+s0NWA9rJf53RBnQZxfch7euUui7hpoAPvALZdA==",
          "requires": {
            "big.js": "^5.2.2",
            "emojis-list": "^3.0.0",
            "json5": "^1.0.1"
          }
        },
        "schema-utils": {
          "version": "1.0.0",
          "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-1.0.0.tgz",
          "integrity": "sha512-i27Mic4KovM/lnGsy8whRCHhc7VicJajAjTrYg11K9zfZXnYIt4k5F+kZkwjnrhKzLic/HLU4j11mjsz2G/75g==",
          "requires": {
            "ajv": "^6.1.0",
            "ajv-errors": "^1.0.0",
            "ajv-keywords": "^3.1.0"
          }
        },
        "watchpack": {
          "version": "1.7.4",
          "resolved": "https://registry.npmjs.org/watchpack/-/watchpack-1.7.4.tgz",
          "integrity": "sha512-aWAgTW4MoSJzZPAicljkO1hsi1oKj/RRq/OJQh2PKI2UKL04c2Bs+MBOB+BBABHTXJpf9mCwHN7ANCvYsvY2sg==",
          "requires": {
            "chokidar": "^3.4.1",
            "graceful-fs": "^4.1.2",
            "neo-async": "^2.5.0",
            "watchpack-chokidar2": "^2.0.0"
          }
        }
      }
    },
    "webpack-sources": {
      "version": "1.4.3",
      "resolved": "https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.4.3.tgz",
      "integrity": "sha512-lgTS3Xhv1lCOKo7SA5TjKXMjpSM4sBjNV5+q2bqesbSPs5FjGmU6jjtBSkX9b4qW87vDIsCIlUPOEhbZrMdjeQ==",
      "requires": {
        "source-list-map": "^2.0.0",
        "source-map": "~0.6.1"
      }
    },
    "worker-farm": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/worker-farm/-/worker-farm-1.7.0.tgz",
      "integrity": "sha512-rvw3QTZc8lAxyVrqcSGVm5yP/IJ2UcB3U0graE3LCFoZ0Yn2x4EoVSqJKdB/T5M+FLcRPjz4TDacRf3OCfNUzw==",
      "requires": {
        "errno": "~0.1.7"
      }
    },
    "worker-rpc": {
      "version": "0.1.1",
      "resolved": "https://registry.npmjs.org/worker-rpc/-/worker-rpc-0.1.1.tgz",
      "integrity": "sha512-P1WjMrUB3qgJNI9jfmpZ/htmBEjFh//6l/5y8SD9hg1Ef5zTTVVoRjTrTEzPrNBQvmhMxkoTsjOXN10GWU7aCg==",
      "requires": {
        "microevent.ts": "~0.1.1"
      }
    },
    "wrappy": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz",
      "integrity": "sha1-tSQ9jz7BqjXxNkYFvA0QNuMKtp8="
    },
    "xtend": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz",
      "integrity": "sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ=="
    },
    "y18n": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/y18n/-/y18n-4.0.0.tgz",
      "integrity": "sha512-r9S/ZyXu/Xu9q1tYlpsLIsa3EeLXXk0VwlxqTcFRfg9EhMW+17kbt9G0NrgCmhGb5vT2hyhJZLfDGx+7+5Uj/w=="
    },
    "yallist": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz",
      "integrity": "sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A=="
    }
  }
}


File: /frontend\package.json
{
  "name": "learn-starter",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev -p 80",
    "build": "next build",
    "start": "next start -p 80"
  },
  "dependencies": {
    "date-fns": "^2.15.0",
    "gray-matter": "^4.0.2",
    "next": "9.3.5",
    "node-fetch": "^2.6.0",
    "react": "16.13.1",
    "react-dom": "16.13.1",
    "remark": "^12.0.1",
    "remark-html": "^12.0.0"
  }
}


File: /frontend\pages\index.js

import Layout, { siteTitle } from '../components/layout'

const fetch = require('node-fetch');


export default function Home({ devices }) {
  return (
    <Layout >
      {devices.map((device) => (
          <table>  
            {console.log('1')}
            <tbody>
              <tr>
                <th>
                    {device.localname} / {device.localIP}  
                </th>
              </tr>

              <tr>
                <td>
                  Interface
                </td>
                <td>
                  Address
                </td>
                <td>
                  Network
                </td>
              </tr>  
              {device.IPaddress.map(port =>(
                <tr>
                  <td>
                    {console.log(port), port[3].value /*interface name*/} 
                  </td>
                  <td>
                    {port[1].value /*address name*/}
                  </td>
                  <td>
                    {port[2].value /*network name*/}
                  </td>

                </tr>
              ))}
            </tbody>
          </table>
      ))}
    </Layout >
      
  )
}

export async function getStaticProps() {
  const res = await fetch('http://localhost:3000')
  const devices = await res.json()

  return {
    props: {
      devices
    }
  }
}

File: /frontend\pages\posts\[id].js
import Layout from '../../components/layout'
import Head from 'next/head'
import Date from '../../components/date'
import utilStyles from '../../styles/utils.module.css'

import { getAllPostIds, getPostData } from '../../lib/posts'

export default function Post({ postData }) {
    return (
        <Layout>
            <Head>
                <title>{postData.title}</title>
            </Head>
            <article>
                <h1 className={utilStyles.headingXl}>{postData.title}</h1>
                <div className={utilStyles.lightText}>
                    <Date dateString={postData.date} />
                </div>
                <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
            </article>
        </Layout>
    )
}

export async function getStaticPaths() {
    const paths = getAllPostIds()
    return {
        paths,
        fallback: false
    }
}

export async function getStaticProps({ params }) {
    const postData = await getPostData(params.id)
    return {
        props: {
        postData
        }
    }
}

File: /frontend\pages\_app.js
import '../styles/global.css'

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}

File: /frontend\posts\pre-rendering.md
---
title: 'Two Forms of Pre-rendering'
date: '2020-01-01'
---

Next.js has two forms of pre-rendering: **Static Generation** and **Server-side Rendering**. The difference is in **when** it generates the HTML for a page.

- **Static Generation** is the pre-rendering method that generates the HTML at **build time**. The pre-rendered HTML is then _reused_ on each request.
- **Server-side Rendering** is the pre-rendering method that generates the HTML on **each request**.

Importantly, Next.js lets you **choose** which pre-rendering form to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

File: /frontend\posts\ssg-ssr.md
---
title: 'When to Use Static Generation v.s. Server-side Rendering'
date: '2020-01-02'
---

We recommend using **Static Generation** (with and without data) whenever possible because your page can be built once and served by CDN, which makes it much faster than having a server render the page on every request.

You can use Static Generation for many types of pages, including:

- Marketing pages
- Blog posts
- E-commerce product listings
- Help and documentation

You should ask yourself: "Can I pre-render this page **ahead** of a user's request?" If the answer is yes, then you should choose Static Generation.

On the other hand, Static Generation is **not** a good idea if you cannot pre-render a page ahead of a user's request. Maybe your page shows frequently updated data, and the page content changes on every request.

In that case, you can use **Server-Side Rendering**. It will be slower, but the pre-rendered page will always be up-to-date. Or you can skip pre-rendering and use client-side JavaScript to populate data.

File: /frontend\README.md
This is a starter template for [Learn Next.js](https://nextjs.org/learn).

File: /frontend\styles\global.css
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu,
    Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
  line-height: 1.6;
  font-size: 18px;
}

* {
  box-sizing: border-box;
}

a {
  color: #0070f3;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

img {
  max-width: 100%;
  display: block;
}

File: /frontend\styles\utils.module.css
.heading2Xl {
    font-size: 2.5rem;
    line-height: 1.2;
    font-weight: 800;
    letter-spacing: -0.05rem;
    margin: 1rem 0;
  }
  
  .headingXl {
    font-size: 2rem;
    line-height: 1.3;
    font-weight: 800;
    letter-spacing: -0.05rem;
    margin: 1rem 0;
  }
  
  .headingLg {
    font-size: 1.5rem;
    line-height: 1.4;
    margin: 1rem 0;
  }
  
  .headingMd {
    font-size: 1.2rem;
    line-height: 1.5;
  }
  
  .borderCircle {
    border-radius: 9999px;
  }
  
  .colorInherit {
    color: inherit;
  }
  
  .padding1px {
    padding-top: 1px;
  }
  
  .list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .listItem {
    margin: 0 0 1.25rem;
  }
  
  .lightText {
    color: #999;
  }

