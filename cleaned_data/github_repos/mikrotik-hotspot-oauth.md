# Repository Information
Name: mikrotik-hotspot-oauth

# Directory Structure
Directory structure:
└── github_repos/mikrotik-hotspot-oauth/
    ├── .circleci/
    │   └── config.yml
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
    │   │       ├── pack-4e08273c2b7874f63ca1fe50c30f200360b27972.idx
    │   │       └── pack-4e08273c2b7874f63ca1fe50c30f200360b27972.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── docs/
    ├── LICENSE
    ├── mikrotik/
    │   ├── authorization.js
    │   ├── authorization.js.LICENSE.txt
    │   ├── index.js
    │   └── login.html
    ├── README.md
    └── source/
        ├── .npmignore
        ├── babel.config.js
        ├── dev/
        │   ├── indexDev.js
        │   └── login.html
        ├── jest.config.js
        ├── package.json
        ├── prod/
        │   └── login.html
        ├── README.md
        ├── src/
        │   ├── base/
        │   │   ├── keyCloakCerts.js
        │   │   ├── loginUtils.js
        │   │   └── restCalls.js
        │   └── index.js
        ├── unitTestConfig/
        │   └── jestSetup.js
        └── webpack.config.babel.js


# Content
File: /.circleci\config.yml
version: 2 # use CircleCI 2.0
jobs:
  build:
    working_directory: ~/mikrotik-hotspot-oauth # directory where steps will run

    docker: # run the steps with Docker
      - image: circleci/openjdk:11.0.2-node

    steps: # a collection of executable commands

      - checkout # check out source code to working directory

      - run:
          name: install hotspot ui
          command: cd source && npm i
      - run:
          name: build hotspot ui
          command: cd source && npm run lint
      - run:
          name: build hotspot ui
          command: cd source && npm run build


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/vzakharchenko/mikrotik-hotspot-oauth.git
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
0000000000000000000000000000000000000000 e29057709cad065c313eedc124a2528c2b529636 vivek-dodia <vivek.dodia@icloud.com> 1738605950 -0500	clone: from https://github.com/vzakharchenko/mikrotik-hotspot-oauth.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 e29057709cad065c313eedc124a2528c2b529636 vivek-dodia <vivek.dodia@icloud.com> 1738605950 -0500	clone: from https://github.com/vzakharchenko/mikrotik-hotspot-oauth.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e29057709cad065c313eedc124a2528c2b529636 vivek-dodia <vivek.dodia@icloud.com> 1738605950 -0500	clone: from https://github.com/vzakharchenko/mikrotik-hotspot-oauth.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e29057709cad065c313eedc124a2528c2b529636 refs/remotes/origin/master
2f9f104fa7eab5b0e46a013bf542b3a530906e8d refs/tags/1.0.1


File: /.git\refs\heads\master
e29057709cad065c313eedc124a2528c2b529636


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# Compiled class file
*.class

# Log file
File: /LICENSE
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


File: /mikrotik\authorization.js
/*! For license information please see authorization.js.LICENSE.txt */
File: /mikrotik\authorization.js.LICENSE.txt
/*!
 * The buffer module from node.js, for the browser.
 *
 * @author   Feross Aboukhadijeh <http://feross.org>
 * @license  MIT
 */

/*! ieee754. BSD-3-Clause License. Feross Aboukhadijeh <https://feross.org/opensource> */

/*! safe-buffer. MIT License. Feross Aboukhadijeh <https://feross.org/opensource> */

/**
 * [js-sha256]{@link https://github.com/emn178/js-sha256}
 *
 * @version 0.9.0
 * @author Chen, Yi-Cyuan [emn178@gmail.com]
 * @copyright Chen, Yi-Cyuan 2014-2017
 * @license MIT
 */


File: /mikrotik\index.js
/* eslint-disable no-unused-vars,no-var,vars-on-top */
// Common server variables
var hostname = '$(hostname)';
var identity = '$(identity)';
var serverAddress = '$(server-address)';
var sslLogin = '$(ssl-login)';
var serverName = '$(server-name)';

// Links
var linkLogin = '$(link-login)';
var loginOnly = '$(link-login-only)';
var linkLogout = '$(link-logout)';
var linkStatus = '$(link-status)';
var linkOrig = '$(link-orig)';

var chapId = '$(chap-id)';
var chapChallenge = '$(chap-challenge)';
var error = '';
var trial = '$(trial)';

// eslint-disable-next-line no-unused-vars
function doLogin(username, password) {
  document.sendin.action = loginOnly;
  document.sendin.username.value = username;
  document.sendin.dst.value = linkOrig;
  var psw = password;
  if (chapId) {
    psw = hexMD5(chapId + password + chapChallenge);
  }
  document.sendin.password.value = psw;
  document.sendin.submit();
  return false;
}


File: /mikrotik\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
    <title>internet hotspot > login</title>
    <style type="text/css">
        body {color: #737373; font-size: 10px; font-family: verdana;}

        textarea,input,select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
        a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
        img {border: none;}
        td { font-size: 14px; color: #7A7A7A; }
    </style>

</head>

<body>
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username" />
    <input type="hidden" name="password" />
    <input type="hidden" name="dst" value="$(link-orig)" />
    <input type="hidden" name="popup" value="true" />
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    /* eslint-disable no-unused-vars,no-var,vars-on-top */
    // Common server variables
    var hostname = "$(hostname)";
    var identity = "$(identity)";
    var serverAddress ="$(server-address)";
    var sslLogin = "$(ssl-login)";
    var serverName = "$(server-name)";

    // Links
    var linkLogin = "$(link-login)";
    var loginOnly = "$(link-login-only)";
    var linkLogout = "$(link-logout)";
    var linkStatus = "$(link-status)";
    var linkOrig = "$(link-orig)";

    var chapId = "$(chap-id)";
    var chapChallenge = "$(chap-challenge)";
    var error = "$(error)";
    var trial = "$(trial)";

    // eslint-disable-next-line no-unused-vars
    function doLogin(username, password) {
        document.sendin.action = loginOnly;
        document.sendin.username.value = username;
        document.sendin.dst.value = linkOrig;
        var psw = password;
        $(if chap-id)
            psw = hexMD5('$(chap-id)' + password + '$(chap-challenge)');
        $(endif)
        document.sendin.password.value = psw;
        document.sendin.submit();
        return false;
    }

    function onClickRefresh() {
        window.location.reload();
    }
</script>

<table id="root" width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br />$(if trial == 'yes')Free trial available, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)</div><br />
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form>
                            <table width="100" style="background-color: #ffffff">
                                <tr><td>&nbsp;</td>
                                    <td><input  type="submit" value="Refresh" onclick="onClickRefresh"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
            </table>

            <br /><div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            <div id="error"></div>
        </td>
    </tr>
</table>
<script type="text/javascript" src="authorization.js"></script></body>
</body>
</html>


File: /README.md
[![CircleCI](https://circleci.com/gh/vzakharchenko/mikrotik-hotspot-oauth.svg?style=svg)](https://circleci.com/gh/vzakharchenko/mikrotik-hotspot-oauth) 

# Keycloak Radius Hotspot
Setup social and other Oauth/Saml integration with [Keycloak Radius embedded server](https://github.com/vzakharchenko/keycloak-radius-plugin/releases)  
# How Keycloak Radius Hotspot works  
1. Authorization through Keycloak occurs by [OpenID Connect](https://www.keycloak.org/docs/latest/securing_apps/#openid-connect-2).  
2. User selects on the login page the identity provider through which he wants to log in  
3. The result of a successful authorization is a JWT that contains a temporary session key.  
4. With this key, the User is authorized through Radius Server.  
5. Radius Server checks if this key is in the user session. And whether it was used.  
6. Radius Server successfully authorizing the user  

# connection Schema`s

## - Cloud connection (Better to Use Radsec)
![KeycloakRadius (1)](/docs/KeycloakRadius.png)


## - Proxy connection
![KeycloakRadius](/docs/KeycloakRadius2.png)

# Setup, build and configure  HotSpot page for Social Login

1. Create Realm ![hotspotRealm](/docs/hotspotRealm.png)
2. create Radius Client ![RadiusClientHotSpot](/docs/RadiusClientHotSpot.png)  
3. create OpenId client ![hotspotClient](/docs/hotspotClient.png)  
4. Setting your Hotspot DNS in "Valid Redirect URIs" and "Web Origins" ![HotspotClientConfiguration](/docs/HotspotClientConfiguration.png)  
5. add "Radius Session Password" Mapper ![HotSpotMapper](/docs/HotSpotMapper.png) ![HotSpotMapper2](/docs/HotSpotMapper2_1.png)  
6. Download keycloak.json ![downloadKeycloakJson](/docs/downloadKeycloakJson.png)  

##  Setup Mikrotik
1. Upload all files from [hotspot/mikrotik](mikrotik) to flash/hotspot on device ([authorization.js](mikrotik/authorization.js) and [login.html](mikrotik/login.html))  
-  Using web UI  
-  Using scp  
- Using ftp  
- Using winbox  
2. Download keycloak.json ![downloadKeycloakJson](/docs/downloadKeycloakJson.png)  
3. upload keycloak.json into flash/hotspot on device  
4. update Walled Garden. Add your keycloak host ![addWalledGarden](/docs/addWalledGarden.png) ![KeycloakHostName](/docs/KeycloakHostName.png)  

## Facebook Login example
1.  [Install Keycloak with embedded Radius Server](https://github.com/vzakharchenko/keycloak-radius-plugin#release-setup)
2.  install [ngrok](https://ngrok.com/). Register ngrok  <pre><code>./ngrok authtoken \<YOUR TOKEN\></pre></code>
3. start ngrok <pre><code>./ngrok http 8090</pre></code>![Ngrok](/docs/Ngrok.png)
4. open keycloak goto realm and add Facebook Identity Provider ![SelectFacbook](/docs/SelectFacbook.png)
5. Copy Redirect URI ![Copy Redirect URI](/docs/Copy%20Redirect%20URI.png)
6. goto [https://developers.facebook.com/](https://developers.facebook.com/) and create a new application ![CreateApp1](/docs/CreateApp1.png)![CreateApp2](/docs/CreateApp2.png)![FacebookLogin3](/docs/FacebookLogin3.png)![Facebook4](/docs/Facebook4.png)
7. Insert Redirect URI from [Step 7](#L43) ![Facebook5](/docs/Facebook5.png)
8. Get App Id and Secret from application (Settings->basic) ![Facebook6](/docs/Facebook6.png)
9. back to Keycloak and set this App Id and Secret ![Facebook7](/docs/Facebook7.png)
10. add facebook hosts to Walled Garden ![FacebookWalledGarden](/docs/FacebookWalledGarden.png)  
```
/ip hotspot walled-garden  
add comment=facebook dst-host=facebook.*  
add comment=facebook dst-host=*.facebook.*  
add comment=facebook dst-host=*.fbcdn.*  
add comment=facebook dst-host=*akamai*  
add comment=facebook dst-host=*atdmt*
add comment=facebook dst-host=*fbsbx*
add comment=common dst-host=www.google-analytics.com
```

12. open hotspot page ![FacebookLoginHotspot](/docs/FacebookLoginHotspot.png) ![FacebookLogin2](/docs/FacebookLogin2.png)  



## build UI

### build UI Requirements:
node and npm must be installed  
macbook instalation [brew](https://brew.sh/) : *brew install node*  
[Install node on ubuntu ](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)  

### Building steps
1. cd [./source](source)  
2. npm i  
3. npm run build  
result in [./mikrotik](mikrotik)  


File: /source\.npmignore
# Created by .ignore support plugin (hsz.mobi)
### Java template
# Compiled class file
*.class

# Log file
File: /source\babel.config.js
module.exports = function (api) {
  api.cache(true);

  const presets = [
    '@babel/env',
  ];
  const plugins = [
    [
      '@babel/transform-runtime',
      {
        regenerator: true,
      },
    ],
    [
      '@babel/plugin-proposal-decorators',
      {
        legacy: true,
      },
    ],
  ];

  // if (process.env.NODE_ENV === 'test') {
  //   plugins.push('babel-plugin-dynamic-import-node');
  // } else {
  //   plugins.push('@babel/plugin-syntax-dynamic-import');
  // }

  return {
    presets,
    plugins,
  };
};


File: /source\dev\indexDev.js
/* eslint-disable no-unused-vars,no-var,vars-on-top */
// Common server variables
var hostname = '$(hostname)';
var identity = '$(identity)';
var serverAddress = '$(server-address)';
var sslLogin = '$(ssl-login)';
var serverName = '$(server-name)';

// Links
var linkLogin = '$(link-login)';
var loginOnly = '$(link-login-only)';
var linkLogout = '$(link-logout)';
var linkStatus = '$(link-status)';
var linkOrig = '$(link-orig)';

var chapId = '$(chap-id)';
var chapChallenge = '$(chap-challenge)';
var error = '';
var trial = '$(trial)';

// eslint-disable-next-line no-unused-vars
function doLogin(username, password) {
  document.sendin.action = loginOnly;
  document.sendin.username.value = username;
  document.sendin.dst.value = linkOrig;
  var psw = password;
  if (chapId) {
    psw = hexMD5(chapId + password + chapChallenge);
  }
  document.sendin.password.value = psw;
  document.sendin.submit();
  return false;
}


File: /source\dev\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
    <title>internet hotspot > login</title>
    <style type="text/css">
        body {color: #737373; font-size: 10px; font-family: verdana;}

        textarea,input,select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
        a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
        img {border: none;}
        td { font-size: 14px; color: #7A7A7A; }
    </style>

</head>

<body>
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username" />
    <input type="hidden" name="password" />
    <input type="hidden" name="dst" value="$(link-orig)" />
    <input type="hidden" name="popup" value="true" />
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript" src="/index.js"></script>

<table id="root" width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br /></div><br />
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form>
                            <table width="100" style="background-color: #ffffff">
                                <tr><td>&nbsp;</td>
                                    <td><input  type="submit" value="Refresh" onclick="onClickRefresh"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
            </table>

            <br /><div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            <div id="error"></div>
        </td>
    </tr>
</table>
<script type="text/javascript" src="bundle.js"></script></body>
</body>
</html>


File: /source\jest.config.js
module.exports = {
  setupFiles: ['./unitTestConfig/jestSetup.js'],
  transform: {
    '^.+\\.js$': 'babel-jest',
  },
File: /source\package.json
{
  "name": "hotspot-login-page",
  "version": "1.0.1",
  "description": "hotspot login page to work with keycloak",
  "main": "index.js",
  "scripts": {
    "start": "NODE_ENV=development webpack-dev-server --hot --mode=development",
    "build": "NODE_ENV=production webpack --bail --config webpack.config.babel.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "lint": "eslint --quiet --ext .js src",
    "lint:fix": "eslint --fix --quiet --ext .js src"
  },
  "author": "vzakharchenko",
  "license": "ISC",
  "keywords": [
    "hotspot-wifi",
    "hotspot",
    "mikrotik-hotspot",
    "mikrotik",
    "radius-server",
    "keycloak",
    "openid",
    "saml2",
    "facebook",
    "google",
    "Idp"],
  "devDependencies": {
    "@babel/core": "^7.7.7",
    "@babel/plugin-proposal-decorators": "^7.7.4",
    "@babel/plugin-transform-runtime": "^7.7.6",
    "@babel/preset-env": "^7.2.0",
    "@babel/preset-stage-3": "^7.0.0",
    "babel-eslint": "^10.0.1",
    "babel-loader": "^8.0.4",
    "babel-preset-es2015": "^6.24.1",
    "copy-webpack-plugin": "^5.1.1",
    "eslint": "^5.10.0",
    "eslint-config-airbnb": "^17.1.0",
    "eslint-plugin-import": "^2.14.0",
    "eslint-plugin-jsx-a11y": "^6.1.2",
    "eslint-plugin-react": "^7.17.0",
    "html-webpack-plugin": "^3.2.0",
    "progress-bar-webpack-plugin": "^1.11.0",
    "terser-webpack-plugin": "^2.3.2",
    "webpack": "^4.27.1",
    "webpack-cli": "^3.1.2",
    "webpack-dev-server": "^3.1.10"
  },
  "dependencies": {
    "axios": "*",
    "jsonwebtoken": "*",
    "keycloak-js": "*"
  },
  "eslintConfig": {
    "parser": "babel-eslint",
    "parserOptions": {
      "ecmaVersion": 7,
      "sourceType": "module",
      "ecmaFeatures": {
        "jsx": true
      }
    },
    "plugins": [],
    "extends": "airbnb",
    "rules": {
      "no-undef": 0,
      "import/extensions": 0,
      "import/prefer-default-export": 0,
      "import/no-extraneous-dependencies": 0,
      "react/jsx-indent": 0
    }
  }
}


File: /source\prod\login.html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="-1" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
    <title>internet hotspot > login</title>
    <style type="text/css">
        body {color: #737373; font-size: 10px; font-family: verdana;}

        textarea,input,select {
            background-color: #FDFBFB;
            border: 1px solid #BBBBBB;
            padding: 2px;
            margin: 1px;
            font-size: 14px;
            color: #808080;
        }

        a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 10px; }
        a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
        img {border: none;}
        td { font-size: 14px; color: #7A7A7A; }
    </style>

</head>

<body>
<form name="sendin" action="$(link-login-only)" method="post">
    <input type="hidden" name="username" />
    <input type="hidden" name="password" />
    <input type="hidden" name="dst" value="$(link-orig)" />
    <input type="hidden" name="popup" value="true" />
</form>

<script type="text/javascript" src="/md5.js"></script>
<script type="text/javascript">
    /* eslint-disable no-unused-vars,no-var,vars-on-top */
    // Common server variables
    var hostname = "$(hostname)";
    var identity = "$(identity)";
    var serverAddress ="$(server-address)";
    var sslLogin = "$(ssl-login)";
    var serverName = "$(server-name)";

    // Links
    var linkLogin = "$(link-login)";
    var loginOnly = "$(link-login-only)";
    var linkLogout = "$(link-logout)";
    var linkStatus = "$(link-status)";
    var linkOrig = "$(link-orig)";

    var chapId = "$(chap-id)";
    var chapChallenge = "$(chap-challenge)";
    var error = "$(error)";
    var trial = "$(trial)";

    // eslint-disable-next-line no-unused-vars
    function doLogin(username, password) {
        document.sendin.action = loginOnly;
        document.sendin.username.value = username;
        document.sendin.dst.value = linkOrig;
        var psw = password;
        $(if chap-id)
            psw = hexMD5('$(chap-id)' + password + '$(chap-challenge)');
        $(endif)
        document.sendin.password.value = psw;
        document.sendin.submit();
        return false;
    }

    function onClickRefresh() {
        window.location.reload();
    }
</script>

<table id="root" width="100%" style="margin-top: 10%;">
    <tr>
        <td align="center" valign="middle">
            <div class="notice" style="color: #c1c1c1; font-size: 9px">Please log on to use the internet hotspot service<br />$(if trial == 'yes')Free trial available, <a style="color: #FF8080"href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)</div><br />
            <table width="280" height="280" style="border: 1px solid #cccccc; padding: 0px;" cellpadding="0" cellspacing="0">
                <tr>
                    <td align="center" valign="bottom" height="175" colspan="2">
                        <form>
                            <table width="100" style="background-color: #ffffff">
                                <tr><td>&nbsp;</td>
                                    <td><input  type="submit" value="Refresh" onclick="onClickRefresh"/></td>
                                </tr>
                            </table>
                        </form>
                    </td>
                </tr>
                <tr><td align="center"><a href="http://www.mikrotik.com" target="_blank" style="border: none;"><img src="/img/logobottom.png" alt="mikrotik" /></a></td></tr>
            </table>

            <br /><div style="color: #c1c1c1; font-size: 9px">Powered by MikroTik RouterOS</div>
            <div id="error"></div>
        </td>
    </tr>
</table>
<script type="text/javascript" src="authorization.js"></script></body>
</body>
</html>


File: /source\README.md
[![CircleCI](https://circleci.com/gh/vzakharchenko/mikrotik-hotspot-oauth.svg?style=svg)](https://circleci.com/gh/vzakharchenko/mikrotik-hotspot-oauth)  
[![donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://secure.wayforpay.com/button/be27056b0a2b4)  

# Keycloak Radius Hotspot
Setup social and other Oauth/Saml integration with [Keycloak Radius embedded server](https://github.com/vzakharchenko/keycloak-radius-plugin/releases)  
# How Keycloak Radius Hotspot works  
1. Authorization through Keycloak occurs by [OpenID Connect](https://www.keycloak.org/docs/latest/securing_apps/#openid-connect-2).  
2. User selects on the login page the identity provider through which he wants to log in  
3. The result of a successful authorization is a JWT that contains a temporary session key.  
4. With this key, the User is authorized through Radius Server.  
5. Radius Server checks if this key is in the user session. And whether it was used.  
6. Radius Server successfully authorizing the user  

# connection Schema`s

## - Cloud connection (Better to Use Radsec)
![KeycloakRadius (1)](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/KeycloakRadius.png)


## - Proxy connection
![KeycloakRadius](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/KeycloakRadius2.png)

# Setup, build and configure  HotSpot page for Social Login

1. Create Realm ![hotspotRealm](/docs/hotspotRealm.png)
2. create Radius Client ![RadiusClientHotSpot](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/RadiusClientHotSpot.png)  
3. create OpenId client ![hotspotClient](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/hotspotClient.png)  
4. Setting your Hotspot DNS in "Valid Redirect URIs" and "Web Origins" ![HotspotClientConfiguration](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/HotspotClientConfiguration.png)  
5. add "Radius Session Password" Mapper ![HotSpotMapper](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/HotSpotMapper.png) ![HotSpotMapper2](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/HotSpotMapper2_1.png)  
6. Download keycloak.json ![downloadKeycloakJson](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/downloadKeycloakJson.png)  

##  Setup Mikrotik
1. Upload all files from [hotspot/mikrotik](mikrotik) to flash/hotspot on device ([authorization.js](mikrotik/authorization.js) and [login.html](mikrotik/login.html))  
-  Using web UI  
-  Using scp  
- Using ftp  
- Using winbox  
2. Download keycloak.json ![downloadKeycloakJson](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/downloadKeycloakJson.png)  
3. upload keycloak.json into flash/hotspot on device  
4. update Walled Garden. Add your keycloak host ![addWalledGarden](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/addWalledGarden.png) ![KeycloakHostName](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/KeycloakHostName.png)  

## Facebook Login example
1.  [Install Keycloak with embedded Radius Server](https://github.com/vzakharchenko/keycloak-radius-plugin#release-setup)
2.  install [ngrok](https://ngrok.com/). Register ngrok  <pre><code>./ngrok authtoken \<YOUR TOKEN\></pre></code>
3. start ngrok <pre><code>./ngrok http 8090</pre></code>![Ngrok](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Ngrok.png)
4. open keycloak goto realm and add Facebook Identity Provider ![SelectFacbook](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/SelectFacbook.png)
5. Copy Redirect URI ![Copy Redirect URI](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Copy%20Redirect%20URI.png)
6. goto [https://developers.facebook.com/](https://developers.facebook.com/) and create a new application ![CreateApp1](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/CreateApp1.png)![CreateApp2](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/CreateApp2.png)![FacebookLogin3](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/FacebookLogin3.png)![Facebook4](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Facebook4.png)
7. Insert Redirect URI from [Step 7](#L43) ![Facebook5](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Facebook5.png)
8. Get App Id and Secret from application (Settings->basic) ![Facebook6](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Facebook6.png)
9. back to Keycloak and set this App Id and Secret ![Facebook7](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/Facebook7.png)
10. add facebook hosts to Walled Garden ![FacebookWalledGarden](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/FacebookWalledGarden.png)  
```
/ip hotspot walled-garden  
add comment=facebook dst-host=facebook.*  
add comment=facebook dst-host=*.facebook.*  
add comment=facebook dst-host=*.fbcdn.*  
add comment=facebook dst-host=*akamai*  
add comment=facebook dst-host=*atdmt*
add comment=facebook dst-host=*fbsbx*
add comment=common dst-host=www.google-analytics.com
```

12. open hotspot page ![FacebookLoginHotspot](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/FacebookLoginHotspot.png) ![FacebookLogin2](https://github.com/vzakharchenko/mikrotik-hotspot-oauth/raw/master/docs/FacebookLogin2.png)  



## build UI

### build UI Requirements:
node and npm must be installed  
macbook instalation [brew](https://brew.sh/) : *brew install node*  
[Install node on ubuntu ](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)  

### Building steps
1. cd [./source](source)  
2. npm i  
3. npm run build  
result in [./mikrotik](mikrotik)  

# If you find these useful, please [Donate](https://secure.wayforpay.com/button/be27056b0a2b4)!  


File: /source\src\base\keyCloakCerts.js
import { fetchData } from './restCalls';

const BEGIN_KEY = '-----BEGIN RSA PUBLIC KEY-----\n';
const END_KEY = '\n-----END RSA PUBLIC KEY-----\n';

function parse(response) {
  return new Promise((resolve, reject) => {
    try {
      const parsedData = JSON.parse(response);
      resolve(parsedData);
    } catch (e) {
      reject(e);
    }
  });
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    fetchData(url, 'GET').then((res) => {
      parse(res.data)
        .then(result => resolve(result))
        .catch(error => reject(error));
    }).catch((e) => {
      reject(new Error(`Status: ${e.statusCode}`));
    });
  });
}

function getKey(response, kid) {
  return Object.hasOwnProperty.call(response, 'keys')
    ? response.keys.find(k => k.kid === kid)
    : undefined;
}

async function getKeyFromKeycloak(url, kid) {
  const response = await getJson(url);
  const key = getKey(response, kid);
  if (!key) {
    throw new Error(`Can't find key for kid "${kid}" in response.`);
  }
  return key;
}

function verify(key) {
  if (!(key.n && key.e)) {
    throw new Error('Can\'t find modulus or exponent in key.');
  }
  if (key.kty !== 'RSA') {
    throw new Error('Key type (kty) must be RSA.');
  }
  if (key.alg !== 'RS256') {
    throw new Error('Algorithm (alg) must be RS256.');
  }
}

// Based on tracker1's node-rsa-pem-from-mod-exp module.
// See https://github.com/tracker1/node-rsa-pem-from-mod-exp

function convertToHex(str) {
  const hex = Buffer.from(str, 'base64').toString('hex');
  return hex[0] < '0' || hex[0] > '7'
    ? `00${hex}`
    : hex;
}

function toHex(number) {
  const str = number.toString(16);
  return (str.length % 2)
    ? `0${str}`
    : str;
}

function toLongHex(number) {
  const str = toHex(number);
  const lengthByteLength = 128 + (str.length / 2);
  return toHex(lengthByteLength) + str;
}

function encodeLenght(n) {
  return n <= 127
    ? toHex(n)
    : toLongHex(n);
}

function getPublicKey(modulus, exponent) {
  const mod = convertToHex(modulus);
  const exp = convertToHex(exponent);
  const encModLen = encodeLenght(mod.length / 2);
  const encExpLen = encodeLenght(exp.length / 2);
  const part = [mod, exp, encModLen, encExpLen].map(n => n.length / 2).reduce((a, b) => a + b);
  const bufferSource = `30${encodeLenght(part + 2)}02${encModLen}${mod}02${encExpLen}${exp}`;
  const pubkey = Buffer.from(bufferSource, 'hex').toString('base64');
  return BEGIN_KEY + pubkey.match(/.{1,64}/g).join('\n') + END_KEY;
}
async function fetch(url, kid) {
  const key = await getKeyFromKeycloak(url, kid);

  verify(key);
  return getPublicKey(key.n, key.e);
}

// eslint-disable-next-line import/prefer-default-export
export async function KeycloakPublicKeyFetcher(url, realm, kid) {
  const certsUrl = realm ? `${url}/realms/${realm}/protocol/openid-connect/certs` : url;
  // eslint-disable-next-line no-return-await
  return await fetch(certsUrl, kid);
}


File: /source\src\base\loginUtils.js
import jwt from 'jsonwebtoken';
import { KeycloakPublicKeyFetcher } from './keyCloakCerts';
import { fetchData } from './restCalls';

function getRealmName(url) {
  const n = url.lastIndexOf('/');
  return url.substring(n + 1);
}

function getRealmNameFromToken(payloadjwt) {
  return getRealmName(payloadjwt.iss);
}

export async function verifyToken(token, keycloakJSON) {
  const decodedJwt = jwt.decode(token, { complete: true });
  if (!decodedJwt || !decodedJwt.header) {
    throw new Error('invalid token (header part)');
  } else {
    const { kid } = decodedJwt.header;
    const { alg } = decodedJwt.header;
    const realm = getRealmNameFromToken(decodedJwt.payload);
    if (alg.toLowerCase() !== 'none' && !alg.toLowerCase().startsWith('hs') && kid) {
      // fetch the PEM Public Key

      try {
        const publicKeyFunc = KeycloakPublicKeyFetcher(keycloakJSON['auth-server-url'],
          realm,
          kid);
        const key = await publicKeyFunc;
        return jwt.verify(token, key);
      } catch (e) {
        // Token is not valid
        throw new Error(`invalid token: ${e}`);
      }
    } else {
      throw new Error('invalid token');
    }
  }
}

export function getPassword(decodedToken) {
  return decodedToken[decodedToken.np || 'p'];
}

export function getUserName(decodedToken) {
  return decodedToken[decodedToken.n];
}

export function loadKeycloakJson() {
  return new Promise((resolve, reject) => {
    fetchData('/keycloak.json').then((r) => {
      resolve(JSON.parse(r.data));
    }).catch((e) => {
      if (e.response && e.response.status === 404) {
        // eslint-disable-next-line prefer-promise-reject-errors
        reject('Cannot found /keycloak.json');
      } else {
        reject(e.response ? e.response.data : e);
      }
    });
  });
}


File: /source\src\base\restCalls.js
import fetch from 'axios';

function errorHandler(response) {
  console.debug('error:', response.data);
}

export function fetchData(url, method = 'GET', headers) {
  return new Promise((resolve, reject) => {
    fetch({
      url,
      method,
      headers,
      transformResponse: req => req,
      withCredentials: true,
    }).then((response) => {
      resolve(response);
    }).catch((response) => {
      errorHandler(response);
      reject(response);
    });
  });
}

export function sendData(url, method = 'POST', data, headers) {
  return new Promise((resolve, reject) => {
    fetch({
      url,
      method,
      data,
      transformResponse: req => req,
      headers,
      withCredentials: true,
    }).then((response) => {
      resolve(response);
    }).catch((response) => {
      errorHandler(response);
      reject(response);
    });
  });
}


File: /source\src\index.js
import Keycloak from 'keycloak-js';
import {
  getPassword, getUserName, loadKeycloakJson, verifyToken,
} from './base/loginUtils';


function setError(message) {
  const errorElement = document.getElementById('error');
  errorElement.innerHTML = `<br /><div style="color: #FF8080; font-size: 9px">${message}</div>`;
}

function clear() {
  const rootElement = document.getElementById('root');
  rootElement.innerHTML = 'Please wait...';
}
if (!error) {
  loadKeycloakJson()
    .then((json) => {
      const keycloak = new Keycloak('/keycloak.json');
      keycloak.init({
        onLoad: 'login-required',
        promiseType: 'native',
      }).then((authenticated) => {
        if (authenticated) {
          verifyToken(keycloak.token, json).then((decodedToken) => {
            const password = getPassword(decodedToken);
            const userName = getUserName(decodedToken);
            if (!userName || !password) {
              setError(`Client ${json.resource} is not configured. Please check client mapper.`);
            } else {
              doLogin(userName, password);
              clear();
            }
          }).catch((ve) => {
            setError(`failed to verify token, please check configuration: ${ve}`);
          });
        } else {
          setError('failed to initialize SSO, please check configuration');
        }
      }).catch((e) => {
        setError(`failed to initialize SSO, please check configuration: ${e}`);
      });
    })
    .catch((e) => {
      setError(`failed to load keycloak.json, please check configuration: ${e}`);
    });
} else {
  setError(`${error}`);
}


File: /source\unitTestConfig\jestSetup.js
import '@babel/polyfill';

import { shallow, mount, render } from 'enzyme';

/**
 * enzyme settings for all tests
 */

global.shallow = shallow;
global.mount = mount;
global.render = render;


File: /source\webpack.config.babel.js
const webpack = require('webpack');
const HtmlWebPackPlugin = require('html-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ProgressBarPlugin = require('progress-bar-webpack-plugin');
const path = require('path');

const progressBarPlugin = new ProgressBarPlugin();

const env = process.env.NODE_ENV || 'development';


const copyConfigs = [];

if (env === 'production') {
  copyConfigs.push({
    from: './prod/login.html',
    to: 'login.html',
  });
} else {
  copyConfigs.push({
    from: './dev/keycloak.json',
    to: 'keycloak.json',
  });
  copyConfigs.push({
    from: './dev/indexDev.js',
    to: 'index.js',
  });
  copyConfigs.push({
    from: './md5.js',
    to: 'md5.js',
  });
}

const plugins = [
  new webpack.optimize.OccurrenceOrderPlugin(true),
  new CopyWebpackPlugin(copyConfigs),
  //    copyConfig,
  progressBarPlugin,
];

if (env !== 'production') {
  const htmlPlugin = new HtmlWebPackPlugin({
    template: './dev/login.html',
    filename: './login.html',
  });
  plugins.push(htmlPlugin);
}

const optimization = {};
if (env === 'production') {
  optimization.minimize = true;
  optimization.namedModules = false;
  optimization.namedChunks = false;
  optimization.mangleWasmImports = true;
  optimization.moduleIds = 'hashed';
  optimization.minimizer = [new TerserPlugin()];
}

module.exports = {
  output: {
    path: path.resolve(__dirname, '..', 'mikrotik'),
    filename: 'authorization.js',
  },
  mode: env,
  devServer: {
    contentBase: 'public',
    historyApiFallback: true,
    hot: false,
    inline: false,
    host: '0.0.0.0',
    disableHostCheck: true,
  },
  module: {
    rules: [
      {
        test: /\.js$/,