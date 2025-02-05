# Repository Information
Name: mikrotik-facebook

# Directory Structure
Directory structure:
└── github_repos/mikrotik-facebook/
    ├── .env.example
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
    │   │       ├── pack-913002a274d6248088b550f76fca38e3b9f6ac2d.idx
    │   │       └── pack-913002a274d6248088b550f76fca38e3b9f6ac2d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── composer.json
    ├── connect.php
    ├── favicomatic/
    │   └── code.txt
    ├── fb-callback.php
    ├── font-awesome/
    │   ├── .npmignore
    │   ├── css/
    │   │   └── font-awesome.css
    │   ├── fonts/
    │   │   ├── fontawesome-webfont.eot
    │   │   ├── fontawesome-webfont.ttf
    │   │   ├── fontawesome-webfont.woff
    │   │   ├── fontawesome-webfont.woff2
    │   │   └── FontAwesome.otf
    │   ├── less/
    │   │   ├── animated.less
    │   │   ├── bordered-pulled.less
    │   │   ├── core.less
    │   │   ├── fixed-width.less
    │   │   ├── font-awesome.less
    │   │   ├── icons.less
    │   │   ├── larger.less
    │   │   ├── list.less
    │   │   ├── mixins.less
    │   │   ├── path.less
    │   │   ├── rotated-flipped.less
    │   │   ├── stacked.less
    │   │   └── variables.less
    │   ├── package.json
    │   ├── README.md
    │   └── scss/
    │       ├── font-awesome.scss
    │       ├── _animated.scss
    │       ├── _bordered-pulled.scss
    │       ├── _core.scss
    │       ├── _fixed-width.scss
    │       ├── _icons.scss
    │       ├── _larger.scss
    │       ├── _list.scss
    │       ├── _mixins.scss
    │       ├── _path.scss
    │       ├── _rotated-flipped.scss
    │       ├── _stacked.scss
    │       └── _variables.scss
    ├── index.php
    ├── md5.js
    ├── parameters.php.example
    ├── policy.php
    ├── README.md
    ├── style.css
    ├── thankyou.htm
    └── welcome.php


# Content
File: /.env.example
#DB parameters

HOST_IP = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""

APP_ID = ""
APP_SECRET = ""
DEFAULT_GRAPH_VERSION = ""

File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/jairuque/mikrotik-facebook.git
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
0000000000000000000000000000000000000000 ec368ae54de86d2627fde17b3e939fe38caca532 vivek-dodia <vivek.dodia@icloud.com> 1738606469 -0500	clone: from https://github.com/jairuque/mikrotik-facebook.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 ec368ae54de86d2627fde17b3e939fe38caca532 vivek-dodia <vivek.dodia@icloud.com> 1738606469 -0500	clone: from https://github.com/jairuque/mikrotik-facebook.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ec368ae54de86d2627fde17b3e939fe38caca532 vivek-dodia <vivek.dodia@icloud.com> 1738606469 -0500	clone: from https://github.com/jairuque/mikrotik-facebook.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ec368ae54de86d2627fde17b3e939fe38caca532 refs/remotes/origin/master


File: /.git\refs\heads\master
ec368ae54de86d2627fde17b3e939fe38caca532


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto


File: /.gitignore
parameters.php
composer.lock
composer.phar
vendor/
*.html

File: /composer.json
{
    "require": {
        "fortawesome/font-awesome": "^5.3",
        "facebook/graph-sdk": "*",
        "vlucas/phpdotenv": "^5"
    }
}

File: /connect.php
<?php
session_start();

include 'parameters.php';

$mac = $_SESSION["mac"];
$ip = $_SESSION["ip"];
$linkorig = "https://portal.astiisb.com/thankyou.htm";
$linkloginonly = $_SESSION["linkloginonly"];
$method = $_SESSION["method"];

$last_updated = date("Y-m-d H:i:s");

$username="admin";
/*
Collecting the data entered by users of type "new" or "repeat_old" in form. It will be posted to the DB.
For "repeat_recent" type users no change will be made in the DB, they'll be authorized directly
*/

require __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . "/../");
$dotenv->load();

$host_ip = $_SERVER['HOST_IP'];
$db_user = $_SERVER['DB_USER'];
$db_pass = $_SERVER['DB_PASS'];
$db_name = $_SERVER['DB_NAME'];

$con=mysqli_connect($host_ip,$db_user,$db_pass,$db_name);

if (mysqli_connect_errno()) {
        echo "Failed to connect to SQL: " . mysqli_connect_error();
}

if($_SESSION["user_type"]=="new" && $_SESSION["method"]=="Form"){

  $fname=$_POST['fname'];
  $lname=$_POST['lname'];
  $email=$_POST['email'];

  mysqli_query($con, "
  CREATE TABLE IF NOT EXISTS `$table_name` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `firstname` varchar(45) NOT NULL,
    `lastname` varchar(45) NOT NULL,
    `email` varchar(45) NOT NULL,
    `mac` varchar(45) NOT NULL,
    `method` varchar(45) NOT NULL,
    `last_updated` varchar(45) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
  )");

  mysqli_query($con,"INSERT INTO `$table_name` (firstname, lastname, email, mac, method, last_updated) VALUES ('$fname', '$lname', '$email', '$mac', '$method', '$last_updated')");

}
elseif($_SESSION["user_type"]=="new" && $_SESSION["method"]=="Facebook"){

  $fname=$_SESSION['fname'];
  $lname=$_SESSION['lname'];
  $email=$_SESSION['email'];

  mysqli_query($con, "
  CREATE TABLE IF NOT EXISTS `$table_name` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `firstname` varchar(45) NOT NULL,
    `lastname` varchar(45) NOT NULL,
    `email` varchar(45) NOT NULL,
    `mac` varchar(45) NOT NULL,
    `method` varchar(45) NOT NULL,
    `last_updated` varchar(45) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
  )");

  mysqli_query($con,"INSERT INTO `$table_name` (firstname, lastname, email, mac, method, last_updated) VALUES ('$fname', '$lname', '$email', '$mac', '$method', '$last_updated')");

}
else {
  $fname=$_SESSION['fname'];
  $lname=$_SESSION['lname'];
  $email=$_SESSION['email'];

  mysqli_query($con,"INSERT INTO `$table_name` (firstname, lastname, email, mac, method, last_updated) VALUES ('$fname', '$lname', '$email', '$mac', '$method', '$last_updated')");
}

mysqli_close($con);

?>
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Astiisb WiFi</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <link rel="stylesheet" href="bulma.min.css" />
  <script defer src="fontawesome-free-5.3.1-web\js\all.js"></script>
  <link rel="icon" type="image/png" href="favicomatic\favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-16x16.png" sizes="16x16" />
  <link rel="stylesheet" href="style.css">  
</head>
<body>
	<div class="bg">

    <section id="logo" class="section">
      <figure>
        <img src="logo.png">
      </figure>
    </section>

		<div id="handle" class="content is-size-6">Please wait, you are being </div>
		<div id="devices" class="content is-size-6">authorized on WiFi</div>

    <div id="powered_handle" class="content is-size-6">Powered by Astiisb</div>
    <div id="copyright" class="content is-size-6">(C) Copyright 2020</div>

  </div>

  <script type="text/javascript" src="./md5.js"></script>
        <script type="text/javascript">
                        function doLogin() {
                                        <?php if(strlen($chapid) < 1) echo "return true;\n"; ?>
                                        document.sendin.username.value = document.login.username.value;
                                        document.sendin.password.value = hexMD5('\011\373\054\364\002\233\266\263\270\373\173\323\234\313\365\337\356');
                                        document.sendin.submit();
                                        return false;
                        }
        </script>
        <script type="text/javascript">
                function formAutoSubmit () {
                        var frm = document.getElementById("login");
                        document.getElementById("login").submit();
                        frm.submit();
        }
        window.onload = formAutoSubmit;
        </script>

        <form id="login" method="post" action="<?php echo $linkloginonly; ?>" onSubmit="return doLogin()">
        <input name="dst" type="hidden" value="<?php echo $linkorig; ?>" />
        <input name="popup" type="hidden" value="false" />
        <input name="username" type="hidden" value="<?php echo $username; ?>"/>
        <input name="password" type="hidden"/>
        </form>

</body>
</html>

File: /favicomatic\code.txt
<link rel="icon" type="image/png" href="favicon-32x32.png" sizes="32x32" />
<link rel="icon" type="image/png" href="favicon-16x16.png" sizes="16x16" />


File: /fb-callback.php
<?php
// Pass session data over. Only needed if not already passed by another script like WordPress.
session_start();

// Include the required dependencies.
require __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . "/../");
$dotenv->load();

$fb = new Facebook\Facebook([
    'app_id'                => $_SERVER['APP_ID'],
    'app_secret'            => $_SERVER['APP_SECRET'],
    'default_graph_version' => $_SERVER['DEFAULT_GRAPH_VERSION'],
  ]);

$helper = $fb->getRedirectLoginHelper();

$_SESSION['FBRLH_state']=$_GET['state'];

try {
  $accessToken = $helper->getAccessToken();
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  // When Graph returns an error
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  // When validation fails or other local issues
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}

if (! isset($accessToken)) {
  if ($helper->getError()) {
    header('HTTP/1.0 401 Unauthorized');
    echo "Error: " . $helper->getError() . "\n";
    echo "Error Code: " . $helper->getErrorCode() . "\n";
    echo "Error Reason: " . $helper->getErrorReason() . "\n";
    echo "Error Description: " . $helper->getErrorDescription() . "\n";
  } else {
    header('HTTP/1.0 400 Bad Request');
    echo 'Bad request';
  }
  exit;
}

if (isset($accessToken)) {
  // Logged in!
  $_SESSION['facebook_access_token'] = (string) $accessToken;
  echo "Logged in!". ".<br>";

  // Now you can redirect to another page and use the
  // access token from $_SESSION['facebook_access_token']
}

try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get('/me?fields=email,name', $_SESSION['facebook_access_token']);
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}

$user = $response->getGraphUser();

$_SESSION["email"]=$user['email'];
$_SESSION["method"]="Facebook";

$name=$user['name'];
$parts = explode(" ", $name);

$_SESSION["lname"] = array_pop($parts);
$_SESSION["fname"] = implode(" ", $parts);

header("Location: connect.php");

File: /font-awesome\.npmignore
File: /font-awesome\css\font-awesome.css
/*!
 *  Font Awesome 4.3.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../fonts/fontawesome-webfont.eot?v=4.3.0');
  src: url('../fonts/fontawesome-webfont.eot?#iefix&v=4.3.0') format('embedded-opentype'), url('../fonts/fontawesome-webfont.woff2?v=4.3.0') format('woff2'), url('../fonts/fontawesome-webfont.woff?v=4.3.0') format('woff'), url('../fonts/fontawesome-webfont.ttf?v=4.3.0') format('truetype'), url('../fonts/fontawesome-webfont.svg?v=4.3.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform: translate(0, 0);
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eeeeee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #ffffff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-genderless:before,
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}


File: /font-awesome\less\animated.less
// Animated Icons
// --------------------------

.@{fa-css-prefix}-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear;
}

.@{fa-css-prefix}-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8);
}

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
            transform: rotate(359deg);
  }
}

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
            transform: rotate(359deg);
  }
}


File: /font-awesome\less\bordered-pulled.less
// Bordered & Pulled
// -------------------------

.@{fa-css-prefix}-border {
  padding: .2em .25em .15em;
  border: solid .08em @fa-border-color;
  border-radius: .1em;
}

.pull-right { float: right; }
.pull-left { float: left; }

.@{fa-css-prefix} {
  &.pull-left { margin-right: .3em; }
  &.pull-right { margin-left: .3em; }
}


File: /font-awesome\less\core.less
// Base Class Definition
// -------------------------

.@{fa-css-prefix} {
  display: inline-block;
  font: normal normal normal @fa-font-size-base/1 FontAwesome; // shortening font declaration
  font-size: inherit; // can't have font-size inherit on line above, so need to override
  text-rendering: auto; // optimizelegibility throws things off #1094
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform: translate(0, 0); // ensures no half-pixel rendering in firefox

}


File: /font-awesome\less\fixed-width.less
// Fixed Width Icons
// -------------------------
.@{fa-css-prefix}-fw {
  width: (18em / 14);
  text-align: center;
}


File: /font-awesome\less\font-awesome.less
/*!
 *  Font Awesome 4.3.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */

@import "variables.less";
@import "mixins.less";
@import "path.less";
@import "core.less";
@import "larger.less";
@import "fixed-width.less";
@import "list.less";
@import "bordered-pulled.less";
@import "animated.less";
@import "rotated-flipped.less";
@import "stacked.less";
@import "icons.less";


File: /font-awesome\less\icons.less
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */

.@{fa-css-prefix}-glass:before { content: @fa-var-glass; }
.@{fa-css-prefix}-music:before { content: @fa-var-music; }
.@{fa-css-prefix}-search:before { content: @fa-var-search; }
.@{fa-css-prefix}-envelope-o:before { content: @fa-var-envelope-o; }
.@{fa-css-prefix}-heart:before { content: @fa-var-heart; }
.@{fa-css-prefix}-star:before { content: @fa-var-star; }
.@{fa-css-prefix}-star-o:before { content: @fa-var-star-o; }
.@{fa-css-prefix}-user:before { content: @fa-var-user; }
.@{fa-css-prefix}-film:before { content: @fa-var-film; }
.@{fa-css-prefix}-th-large:before { content: @fa-var-th-large; }
.@{fa-css-prefix}-th:before { content: @fa-var-th; }
.@{fa-css-prefix}-th-list:before { content: @fa-var-th-list; }
.@{fa-css-prefix}-check:before { content: @fa-var-check; }
.@{fa-css-prefix}-remove:before,
.@{fa-css-prefix}-close:before,
.@{fa-css-prefix}-times:before { content: @fa-var-times; }
.@{fa-css-prefix}-search-plus:before { content: @fa-var-search-plus; }
.@{fa-css-prefix}-search-minus:before { content: @fa-var-search-minus; }
.@{fa-css-prefix}-power-off:before { content: @fa-var-power-off; }
.@{fa-css-prefix}-signal:before { content: @fa-var-signal; }
.@{fa-css-prefix}-gear:before,
.@{fa-css-prefix}-cog:before { content: @fa-var-cog; }
.@{fa-css-prefix}-trash-o:before { content: @fa-var-trash-o; }
.@{fa-css-prefix}-home:before { content: @fa-var-home; }
.@{fa-css-prefix}-file-o:before { content: @fa-var-file-o; }
.@{fa-css-prefix}-clock-o:before { content: @fa-var-clock-o; }
.@{fa-css-prefix}-road:before { content: @fa-var-road; }
.@{fa-css-prefix}-download:before { content: @fa-var-download; }
.@{fa-css-prefix}-arrow-circle-o-down:before { content: @fa-var-arrow-circle-o-down; }
.@{fa-css-prefix}-arrow-circle-o-up:before { content: @fa-var-arrow-circle-o-up; }
.@{fa-css-prefix}-inbox:before { content: @fa-var-inbox; }
.@{fa-css-prefix}-play-circle-o:before { content: @fa-var-play-circle-o; }
.@{fa-css-prefix}-rotate-right:before,
.@{fa-css-prefix}-repeat:before { content: @fa-var-repeat; }
.@{fa-css-prefix}-refresh:before { content: @fa-var-refresh; }
.@{fa-css-prefix}-list-alt:before { content: @fa-var-list-alt; }
.@{fa-css-prefix}-lock:before { content: @fa-var-lock; }
.@{fa-css-prefix}-flag:before { content: @fa-var-flag; }
.@{fa-css-prefix}-headphones:before { content: @fa-var-headphones; }
.@{fa-css-prefix}-volume-off:before { content: @fa-var-volume-off; }
.@{fa-css-prefix}-volume-down:before { content: @fa-var-volume-down; }
.@{fa-css-prefix}-volume-up:before { content: @fa-var-volume-up; }
.@{fa-css-prefix}-qrcode:before { content: @fa-var-qrcode; }
.@{fa-css-prefix}-barcode:before { content: @fa-var-barcode; }
.@{fa-css-prefix}-tag:before { content: @fa-var-tag; }
.@{fa-css-prefix}-tags:before { content: @fa-var-tags; }
.@{fa-css-prefix}-book:before { content: @fa-var-book; }
.@{fa-css-prefix}-bookmark:before { content: @fa-var-bookmark; }
.@{fa-css-prefix}-print:before { content: @fa-var-print; }
.@{fa-css-prefix}-camera:before { content: @fa-var-camera; }
.@{fa-css-prefix}-font:before { content: @fa-var-font; }
.@{fa-css-prefix}-bold:before { content: @fa-var-bold; }
.@{fa-css-prefix}-italic:before { content: @fa-var-italic; }
.@{fa-css-prefix}-text-height:before { content: @fa-var-text-height; }
.@{fa-css-prefix}-text-width:before { content: @fa-var-text-width; }
.@{fa-css-prefix}-align-left:before { content: @fa-var-align-left; }
.@{fa-css-prefix}-align-center:before { content: @fa-var-align-center; }
.@{fa-css-prefix}-align-right:before { content: @fa-var-align-right; }
.@{fa-css-prefix}-align-justify:before { content: @fa-var-align-justify; }
.@{fa-css-prefix}-list:before { content: @fa-var-list; }
.@{fa-css-prefix}-dedent:before,
.@{fa-css-prefix}-outdent:before { content: @fa-var-outdent; }
.@{fa-css-prefix}-indent:before { content: @fa-var-indent; }
.@{fa-css-prefix}-video-camera:before { content: @fa-var-video-camera; }
.@{fa-css-prefix}-photo:before,
.@{fa-css-prefix}-image:before,
.@{fa-css-prefix}-picture-o:before { content: @fa-var-picture-o; }
.@{fa-css-prefix}-pencil:before { content: @fa-var-pencil; }
.@{fa-css-prefix}-map-marker:before { content: @fa-var-map-marker; }
.@{fa-css-prefix}-adjust:before { content: @fa-var-adjust; }
.@{fa-css-prefix}-tint:before { content: @fa-var-tint; }
.@{fa-css-prefix}-edit:before,
.@{fa-css-prefix}-pencil-square-o:before { content: @fa-var-pencil-square-o; }
.@{fa-css-prefix}-share-square-o:before { content: @fa-var-share-square-o; }
.@{fa-css-prefix}-check-square-o:before { content: @fa-var-check-square-o; }
.@{fa-css-prefix}-arrows:before { content: @fa-var-arrows; }
.@{fa-css-prefix}-step-backward:before { content: @fa-var-step-backward; }
.@{fa-css-prefix}-fast-backward:before { content: @fa-var-fast-backward; }
.@{fa-css-prefix}-backward:before { content: @fa-var-backward; }
.@{fa-css-prefix}-play:before { content: @fa-var-play; }
.@{fa-css-prefix}-pause:before { content: @fa-var-pause; }
.@{fa-css-prefix}-stop:before { content: @fa-var-stop; }
.@{fa-css-prefix}-forward:before { content: @fa-var-forward; }
.@{fa-css-prefix}-fast-forward:before { content: @fa-var-fast-forward; }
.@{fa-css-prefix}-step-forward:before { content: @fa-var-step-forward; }
.@{fa-css-prefix}-eject:before { content: @fa-var-eject; }
.@{fa-css-prefix}-chevron-left:before { content: @fa-var-chevron-left; }
.@{fa-css-prefix}-chevron-right:before { content: @fa-var-chevron-right; }
.@{fa-css-prefix}-plus-circle:before { content: @fa-var-plus-circle; }
.@{fa-css-prefix}-minus-circle:before { content: @fa-var-minus-circle; }
.@{fa-css-prefix}-times-circle:before { content: @fa-var-times-circle; }
.@{fa-css-prefix}-check-circle:before { content: @fa-var-check-circle; }
.@{fa-css-prefix}-question-circle:before { content: @fa-var-question-circle; }
.@{fa-css-prefix}-info-circle:before { content: @fa-var-info-circle; }
.@{fa-css-prefix}-crosshairs:before { content: @fa-var-crosshairs; }
.@{fa-css-prefix}-times-circle-o:before { content: @fa-var-times-circle-o; }
.@{fa-css-prefix}-check-circle-o:before { content: @fa-var-check-circle-o; }
.@{fa-css-prefix}-ban:before { content: @fa-var-ban; }
.@{fa-css-prefix}-arrow-left:before { content: @fa-var-arrow-left; }
.@{fa-css-prefix}-arrow-right:before { content: @fa-var-arrow-right; }
.@{fa-css-prefix}-arrow-up:before { content: @fa-var-arrow-up; }
.@{fa-css-prefix}-arrow-down:before { content: @fa-var-arrow-down; }
.@{fa-css-prefix}-mail-forward:before,
.@{fa-css-prefix}-share:before { content: @fa-var-share; }
.@{fa-css-prefix}-expand:before { content: @fa-var-expand; }
.@{fa-css-prefix}-compress:before { content: @fa-var-compress; }
.@{fa-css-prefix}-plus:before { content: @fa-var-plus; }
.@{fa-css-prefix}-minus:before { content: @fa-var-minus; }
.@{fa-css-prefix}-asterisk:before { content: @fa-var-asterisk; }
.@{fa-css-prefix}-exclamation-circle:before { content: @fa-var-exclamation-circle; }
.@{fa-css-prefix}-gift:before { content: @fa-var-gift; }
.@{fa-css-prefix}-leaf:before { content: @fa-var-leaf; }
.@{fa-css-prefix}-fire:before { content: @fa-var-fire; }
.@{fa-css-prefix}-eye:before { content: @fa-var-eye; }
.@{fa-css-prefix}-eye-slash:before { content: @fa-var-eye-slash; }
.@{fa-css-prefix}-warning:before,
.@{fa-css-prefix}-exclamation-triangle:before { content: @fa-var-exclamation-triangle; }
.@{fa-css-prefix}-plane:before { content: @fa-var-plane; }
.@{fa-css-prefix}-calendar:before { content: @fa-var-calendar; }
.@{fa-css-prefix}-random:before { content: @fa-var-random; }
.@{fa-css-prefix}-comment:before { content: @fa-var-comment; }
.@{fa-css-prefix}-magnet:before { content: @fa-var-magnet; }
.@{fa-css-prefix}-chevron-up:before { content: @fa-var-chevron-up; }
.@{fa-css-prefix}-chevron-down:before { content: @fa-var-chevron-down; }
.@{fa-css-prefix}-retweet:before { content: @fa-var-retweet; }
.@{fa-css-prefix}-shopping-cart:before { content: @fa-var-shopping-cart; }
.@{fa-css-prefix}-folder:before { content: @fa-var-folder; }
.@{fa-css-prefix}-folder-open:before { content: @fa-var-folder-open; }
.@{fa-css-prefix}-arrows-v:before { content: @fa-var-arrows-v; }
.@{fa-css-prefix}-arrows-h:before { content: @fa-var-arrows-h; }
.@{fa-css-prefix}-bar-chart-o:before,
.@{fa-css-prefix}-bar-chart:before { content: @fa-var-bar-chart; }
.@{fa-css-prefix}-twitter-square:before { content: @fa-var-twitter-square; }
.@{fa-css-prefix}-facebook-square:before { content: @fa-var-facebook-square; }
.@{fa-css-prefix}-camera-retro:before { content: @fa-var-camera-retro; }
.@{fa-css-prefix}-key:before { content: @fa-var-key; }
.@{fa-css-prefix}-gears:before,
.@{fa-css-prefix}-cogs:before { content: @fa-var-cogs; }
.@{fa-css-prefix}-comments:before { content: @fa-var-comments; }
.@{fa-css-prefix}-thumbs-o-up:before { content: @fa-var-thumbs-o-up; }
.@{fa-css-prefix}-thumbs-o-down:before { content: @fa-var-thumbs-o-down; }
.@{fa-css-prefix}-star-half:before { content: @fa-var-star-half; }
.@{fa-css-prefix}-heart-o:before { content: @fa-var-heart-o; }
.@{fa-css-prefix}-sign-out:before { content: @fa-var-sign-out; }
.@{fa-css-prefix}-linkedin-square:before { content: @fa-var-linkedin-square; }
.@{fa-css-prefix}-thumb-tack:before { content: @fa-var-thumb-tack; }
.@{fa-css-prefix}-external-link:before { content: @fa-var-external-link; }
.@{fa-css-prefix}-sign-in:before { content: @fa-var-sign-in; }
.@{fa-css-prefix}-trophy:before { content: @fa-var-trophy; }
.@{fa-css-prefix}-github-square:before { content: @fa-var-github-square; }
.@{fa-css-prefix}-upload:before { content: @fa-var-upload; }
.@{fa-css-prefix}-lemon-o:before { content: @fa-var-lemon-o; }
.@{fa-css-prefix}-phone:before { content: @fa-var-phone; }
.@{fa-css-prefix}-square-o:before { content: @fa-var-square-o; }
.@{fa-css-prefix}-bookmark-o:before { content: @fa-var-bookmark-o; }
.@{fa-css-prefix}-phone-square:before { content: @fa-var-phone-square; }
.@{fa-css-prefix}-twitter:before { content: @fa-var-twitter; }
.@{fa-css-prefix}-facebook-f:before,
.@{fa-css-prefix}-facebook:before { content: @fa-var-facebook; }
.@{fa-css-prefix}-github:before { content: @fa-var-github; }
.@{fa-css-prefix}-unlock:before { content: @fa-var-unlock; }
.@{fa-css-prefix}-credit-card:before { content: @fa-var-credit-card; }
.@{fa-css-prefix}-rss:before { content: @fa-var-rss; }
.@{fa-css-prefix}-hdd-o:before { content: @fa-var-hdd-o; }
.@{fa-css-prefix}-bullhorn:before { content: @fa-var-bullhorn; }
.@{fa-css-prefix}-bell:before { content: @fa-var-bell; }
.@{fa-css-prefix}-certificate:before { content: @fa-var-certificate; }
.@{fa-css-prefix}-hand-o-right:before { content: @fa-var-hand-o-right; }
.@{fa-css-prefix}-hand-o-left:before { content: @fa-var-hand-o-left; }
.@{fa-css-prefix}-hand-o-up:before { content: @fa-var-hand-o-up; }
.@{fa-css-prefix}-hand-o-down:before { content: @fa-var-hand-o-down; }
.@{fa-css-prefix}-arrow-circle-left:before { content: @fa-var-arrow-circle-left; }
.@{fa-css-prefix}-arrow-circle-right:before { content: @fa-var-arrow-circle-right; }
.@{fa-css-prefix}-arrow-circle-up:before { content: @fa-var-arrow-circle-up; }
.@{fa-css-prefix}-arrow-circle-down:before { content: @fa-var-arrow-circle-down; }
.@{fa-css-prefix}-globe:before { content: @fa-var-globe; }
.@{fa-css-prefix}-wrench:before { content: @fa-var-wrench; }
.@{fa-css-prefix}-tasks:before { content: @fa-var-tasks; }
.@{fa-css-prefix}-filter:before { content: @fa-var-filter; }
.@{fa-css-prefix}-briefcase:before { content: @fa-var-briefcase; }
.@{fa-css-prefix}-arrows-alt:before { content: @fa-var-arrows-alt; }
.@{fa-css-prefix}-group:before,
.@{fa-css-prefix}-users:before { content: @fa-var-users; }
.@{fa-css-prefix}-chain:before,
.@{fa-css-prefix}-link:before { content: @fa-var-link; }
.@{fa-css-prefix}-cloud:before { content: @fa-var-cloud; }
.@{fa-css-prefix}-flask:before { content: @fa-var-flask; }
.@{fa-css-prefix}-cut:before,
.@{fa-css-prefix}-scissors:before { content: @fa-var-scissors; }
.@{fa-css-prefix}-copy:before,
.@{fa-css-prefix}-files-o:before { content: @fa-var-files-o; }
.@{fa-css-prefix}-paperclip:before { content: @fa-var-paperclip; }
.@{fa-css-prefix}-save:before,
.@{fa-css-prefix}-floppy-o:before { content: @fa-var-floppy-o; }
.@{fa-css-prefix}-square:before { content: @fa-var-square; }
.@{fa-css-prefix}-navicon:before,
.@{fa-css-prefix}-reorder:before,
.@{fa-css-prefix}-bars:before { content: @fa-var-bars; }
.@{fa-css-prefix}-list-ul:before { content: @fa-var-list-ul; }
.@{fa-css-prefix}-list-ol:before { content: @fa-var-list-ol; }
.@{fa-css-prefix}-strikethrough:before { content: @fa-var-strikethrough; }
.@{fa-css-prefix}-underline:before { content: @fa-var-underline; }
.@{fa-css-prefix}-table:before { content: @fa-var-table; }
.@{fa-css-prefix}-magic:before { content: @fa-var-magic; }
.@{fa-css-prefix}-truck:before { content: @fa-var-truck; }
.@{fa-css-prefix}-pinterest:before { content: @fa-var-pinterest; }
.@{fa-css-prefix}-pinterest-square:before { content: @fa-var-pinterest-square; }
.@{fa-css-prefix}-google-plus-square:before { content: @fa-var-google-plus-square; }
.@{fa-css-prefix}-google-plus:before { content: @fa-var-google-plus; }
.@{fa-css-prefix}-money:before { content: @fa-var-money; }
.@{fa-css-prefix}-caret-down:before { content: @fa-var-caret-down; }
.@{fa-css-prefix}-caret-up:before { content: @fa-var-caret-up; }
.@{fa-css-prefix}-caret-left:before { content: @fa-var-caret-left; }
.@{fa-css-prefix}-caret-right:before { content: @fa-var-caret-right; }
.@{fa-css-prefix}-columns:before { content: @fa-var-columns; }
.@{fa-css-prefix}-unsorted:before,
.@{fa-css-prefix}-sort:before { content: @fa-var-sort; }
.@{fa-css-prefix}-sort-down:before,
.@{fa-css-prefix}-sort-desc:before { content: @fa-var-sort-desc; }
.@{fa-css-prefix}-sort-up:before,
.@{fa-css-prefix}-sort-asc:before { content: @fa-var-sort-asc; }
.@{fa-css-prefix}-envelope:before { content: @fa-var-envelope; }
.@{fa-css-prefix}-linkedin:before { content: @fa-var-linkedin; }
.@{fa-css-prefix}-rotate-left:before,
.@{fa-css-prefix}-undo:before { content: @fa-var-undo; }
.@{fa-css-prefix}-legal:before,
.@{fa-css-prefix}-gavel:before { content: @fa-var-gavel; }
.@{fa-css-prefix}-dashboard:before,
.@{fa-css-prefix}-tachometer:before { content: @fa-var-tachometer; }
.@{fa-css-prefix}-comment-o:before { content: @fa-var-comment-o; }
.@{fa-css-prefix}-comments-o:before { content: @fa-var-comments-o; }
.@{fa-css-prefix}-flash:before,
.@{fa-css-prefix}-bolt:before { content: @fa-var-bolt; }
.@{fa-css-prefix}-sitemap:before { content: @fa-var-sitemap; }
.@{fa-css-prefix}-umbrella:before { content: @fa-var-umbrella; }
.@{fa-css-prefix}-paste:before,
.@{fa-css-prefix}-clipboard:before { content: @fa-var-clipboard; }
.@{fa-css-prefix}-lightbulb-o:before { content: @fa-var-lightbulb-o; }
.@{fa-css-prefix}-exchange:before { content: @fa-var-exchange; }
.@{fa-css-prefix}-cloud-download:before { content: @fa-var-cloud-download; }
.@{fa-css-prefix}-cloud-upload:before { content: @fa-var-cloud-upload; }
.@{fa-css-prefix}-user-md:before { content: @fa-var-user-md; }
.@{fa-css-prefix}-stethoscope:before { content: @fa-var-stethoscope; }
.@{fa-css-prefix}-suitcase:before { content: @fa-var-suitcase; }
.@{fa-css-prefix}-bell-o:before { content: @fa-var-bell-o; }
.@{fa-css-prefix}-coffee:before { content: @fa-var-coffee; }
.@{fa-css-prefix}-cutlery:before { content: @fa-var-cutlery; }
.@{fa-css-prefix}-file-text-o:before { content: @fa-var-file-text-o; }
.@{fa-css-prefix}-building-o:before { content: @fa-var-building-o; }
.@{fa-css-prefix}-hospital-o:before { content: @fa-var-hospital-o; }
.@{fa-css-prefix}-ambulance:before { content: @fa-var-ambulance; }
.@{fa-css-prefix}-medkit:before { content: @fa-var-medkit; }
.@{fa-css-prefix}-fighter-jet:before { content: @fa-var-fighter-jet; }
.@{fa-css-prefix}-beer:before { content: @fa-var-beer; }
.@{fa-css-prefix}-h-square:before { content: @fa-var-h-square; }
.@{fa-css-prefix}-plus-square:before { content: @fa-var-plus-square; }
.@{fa-css-prefix}-angle-double-left:before { content: @fa-var-angle-double-left; }
.@{fa-css-prefix}-angle-double-right:before { content: @fa-var-angle-double-right; }
.@{fa-css-prefix}-angle-double-up:before { content: @fa-var-angle-double-up; }
.@{fa-css-prefix}-angle-double-down:before { content: @fa-var-angle-double-down; }
.@{fa-css-prefix}-angle-left:before { content: @fa-var-angle-left; }
.@{fa-css-prefix}-angle-right:before { content: @fa-var-angle-right; }
.@{fa-css-prefix}-angle-up:before { content: @fa-var-angle-up; }
.@{fa-css-prefix}-angle-down:before { content: @fa-var-angle-down; }
.@{fa-css-prefix}-desktop:before { content: @fa-var-desktop; }
.@{fa-css-prefix}-laptop:before { content: @fa-var-laptop; }
.@{fa-css-prefix}-tablet:before { content: @fa-var-tablet; }
.@{fa-css-prefix}-mobile-phone:before,
.@{fa-css-prefix}-mobile:before { content: @fa-var-mobile; }
.@{fa-css-prefix}-circle-o:before { content: @fa-var-circle-o; }
.@{fa-css-prefix}-quote-left:before { content: @fa-var-quote-left; }
.@{fa-css-prefix}-quote-right:before { content: @fa-var-quote-right; }
.@{fa-css-prefix}-spinner:before { content: @fa-var-spinner; }
.@{fa-css-prefix}-circle:before { content: @fa-var-circle; }
.@{fa-css-prefix}-mail-reply:before,
.@{fa-css-prefix}-reply:before { content: @fa-var-reply; }
.@{fa-css-prefix}-github-alt:before { content: @fa-var-github-alt; }
.@{fa-css-prefix}-folder-o:before { content: @fa-var-folder-o; }
.@{fa-css-prefix}-folder-open-o:before { content: @fa-var-folder-open-o; }
.@{fa-css-prefix}-smile-o:before { content: @fa-var-smile-o; }
.@{fa-css-prefix}-frown-o:before { content: @fa-var-frown-o; }
.@{fa-css-prefix}-meh-o:before { content: @fa-var-meh-o; }
.@{fa-css-prefix}-gamepad:before { content: @fa-var-gamepad; }
.@{fa-css-prefix}-keyboard-o:before { content: @fa-var-keyboard-o; }
.@{fa-css-prefix}-flag-o:before { content: @fa-var-flag-o; }
.@{fa-css-prefix}-flag-checkered:before { content: @fa-var-flag-checkered; }
.@{fa-css-prefix}-terminal:before { content: @fa-var-terminal; }
.@{fa-css-prefix}-code:before { content: @fa-var-code; }
.@{fa-css-prefix}-mail-reply-all:before,
.@{fa-css-prefix}-reply-all:before { content: @fa-var-reply-all; }
.@{fa-css-prefix}-star-half-empty:before,
.@{fa-css-prefix}-star-half-full:before,
.@{fa-css-prefix}-star-half-o:before { content: @fa-var-star-half-o; }
.@{fa-css-prefix}-location-arrow:before { content: @fa-var-location-arrow; }
.@{fa-css-prefix}-crop:before { content: @fa-var-crop; }
.@{fa-css-prefix}-code-fork:before { content: @fa-var-code-fork; }
.@{fa-css-prefix}-unlink:before,
.@{fa-css-prefix}-chain-broken:before { content: @fa-var-chain-broken; }
.@{fa-css-prefix}-question:before { content: @fa-var-question; }
.@{fa-css-prefix}-info:before { content: @fa-var-info; }
.@{fa-css-prefix}-exclamation:before { content: @fa-var-exclamation; }
.@{fa-css-prefix}-superscript:before { content: @fa-var-superscript; }
.@{fa-css-prefix}-subscript:before { content: @fa-var-subscript; }
.@{fa-css-prefix}-eraser:before { content: @fa-var-eraser; }
.@{fa-css-prefix}-puzzle-piece:before { content: @fa-var-puzzle-piece; }
.@{fa-css-prefix}-microphone:before { content: @fa-var-microphone; }
.@{fa-css-prefix}-microphone-slash:before { content: @fa-var-microphone-slash; }
.@{fa-css-prefix}-shield:before { content: @fa-var-shield; }
.@{fa-css-prefix}-calendar-o:before { content: @fa-var-calendar-o; }
.@{fa-css-prefix}-fire-extinguisher:before { content: @fa-var-fire-extinguisher; }
.@{fa-css-prefix}-rocket:before { content: @fa-var-rocket; }
.@{fa-css-prefix}-maxcdn:before { content: @fa-var-maxcdn; }
.@{fa-css-prefix}-chevron-circle-left:before { content: @fa-var-chevron-circle-left; }
.@{fa-css-prefix}-chevron-circle-right:before { content: @fa-var-chevron-circle-right; }
.@{fa-css-prefix}-chevron-circle-up:before { content: @fa-var-chevron-circle-up; }
.@{fa-css-prefix}-chevron-circle-down:before { content: @fa-var-chevron-circle-down; }
.@{fa-css-prefix}-html5:before { content: @fa-var-html5; }
.@{fa-css-prefix}-css3:before { content: @fa-var-css3; }
.@{fa-css-prefix}-anchor:before { content: @fa-var-anchor; }
.@{fa-css-prefix}-unlock-alt:before { content: @fa-var-unlock-alt; }
.@{fa-css-prefix}-bullseye:before { content: @fa-var-bullseye; }
.@{fa-css-prefix}-ellipsis-h:before { content: @fa-var-ellipsis-h; }
.@{fa-css-prefix}-ellipsis-v:before { content: @fa-var-ellipsis-v; }
.@{fa-css-prefix}-rss-square:before { content: @fa-var-rss-square; }
.@{fa-css-prefix}-play-circle:before { content: @fa-var-play-circle; }
.@{fa-css-prefix}-ticket:before { content: @fa-var-ticket; }
.@{fa-css-prefix}-minus-square:before { content: @fa-var-minus-square; }
.@{fa-css-prefix}-minus-square-o:before { content: @fa-var-minus-square-o; }
.@{fa-css-prefix}-level-up:before { content: @fa-var-level-up; }
.@{fa-css-prefix}-level-down:before { content: @fa-var-level-down; }
.@{fa-css-prefix}-check-square:before { content: @fa-var-check-square; }
.@{fa-css-prefix}-pencil-square:before { content: @fa-var-pencil-square; }
.@{fa-css-prefix}-external-link-square:before { content: @fa-var-external-link-square; }
.@{fa-css-prefix}-share-square:before { content: @fa-var-share-square; }
.@{fa-css-prefix}-compass:before { content: @fa-var-compass; }
.@{fa-css-prefix}-toggle-down:before,
.@{fa-css-prefix}-caret-square-o-down:before { content: @fa-var-caret-square-o-down; }
.@{fa-css-prefix}-toggle-up:before,
.@{fa-css-prefix}-caret-square-o-up:before { content: @fa-var-caret-square-o-up; }
.@{fa-css-prefix}-toggle-right:before,
.@{fa-css-prefix}-caret-square-o-right:before { content: @fa-var-caret-square-o-right; }
.@{fa-css-prefix}-euro:before,
.@{fa-css-prefix}-eur:before { content: @fa-var-eur; }
.@{fa-css-prefix}-gbp:before { content: @fa-var-gbp; }
.@{fa-css-prefix}-dollar:before,
.@{fa-css-prefix}-usd:before { content: @fa-var-usd; }
.@{fa-css-prefix}-rupee:before,
.@{fa-css-prefix}-inr:before { content: @fa-var-inr; }
.@{fa-css-prefix}-cny:before,
.@{fa-css-prefix}-rmb:before,
.@{fa-css-prefix}-yen:before,
.@{fa-css-prefix}-jpy:before { content: @fa-var-jpy; }
.@{fa-css-prefix}-ruble:before,
.@{fa-css-prefix}-rouble:before,
.@{fa-css-prefix}-rub:before { content: @fa-var-rub; }
.@{fa-css-prefix}-won:before,
.@{fa-css-prefix}-krw:before { content: @fa-var-krw; }
.@{fa-css-prefix}-bitcoin:before,
.@{fa-css-prefix}-btc:before { content: @fa-var-btc; }
.@{fa-css-prefix}-file:before { content: @fa-var-file; }
.@{fa-css-prefix}-file-text:before { content: @fa-var-file-text; }
.@{fa-css-prefix}-sort-alpha-asc:before { content: @fa-var-sort-alpha-asc; }
.@{fa-css-prefix}-sort-alpha-desc:before { content: @fa-var-sort-alpha-desc; }
.@{fa-css-prefix}-sort-amount-asc:before { content: @fa-var-sort-amount-asc; }
.@{fa-css-prefix}-sort-amount-desc:before { content: @fa-var-sort-amount-desc; }
.@{fa-css-prefix}-sort-numeric-asc:before { content: @fa-var-sort-numeric-asc; }
.@{fa-css-prefix}-sort-numeric-desc:before { content: @fa-var-sort-numeric-desc; }
.@{fa-css-prefix}-thumbs-up:before { content: @fa-var-thumbs-up; }
.@{fa-css-prefix}-thumbs-down:before { content: @fa-var-thumbs-down; }
.@{fa-css-prefix}-youtube-square:before { content: @fa-var-youtube-square; }
.@{fa-css-prefix}-youtube:before { content: @fa-var-youtube; }
.@{fa-css-prefix}-xing:before { content: @fa-var-xing; }
.@{fa-css-prefix}-xing-square:before { content: @fa-var-xing-square; }
.@{fa-css-prefix}-youtube-play:before { content: @fa-var-youtube-play; }
.@{fa-css-prefix}-dropbox:before { content: @fa-var-dropbox; }
.@{fa-css-prefix}-stack-overflow:before { content: @fa-var-stack-overflow; }
.@{fa-css-prefix}-instagram:before { content: @fa-var-instagram; }
.@{fa-css-prefix}-flickr:before { content: @fa-var-flickr; }
.@{fa-css-prefix}-adn:before { content: @fa-var-adn; }
.@{fa-css-prefix}-bitbucket:before { content: @fa-var-bitbucket; }
.@{fa-css-prefix}-bitbucket-square:before { content: @fa-var-bitbucket-square; }
.@{fa-css-prefix}-tumblr:before { content: @fa-var-tumblr; }
.@{fa-css-prefix}-tumblr-square:before { content: @fa-var-tumblr-square; }
.@{fa-css-prefix}-long-arrow-down:before { content: @fa-var-long-arrow-down; }
.@{fa-css-prefix}-long-arrow-up:before { content: @fa-var-long-arrow-up; }
.@{fa-css-prefix}-long-arrow-left:before { content: @fa-var-long-arrow-left; }
.@{fa-css-prefix}-long-arrow-right:before { content: @fa-var-long-arrow-right; }
.@{fa-css-prefix}-apple:before { content: @fa-var-apple; }
.@{fa-css-prefix}-windows:before { content: @fa-var-windows; }
.@{fa-css-prefix}-android:before { content: @fa-var-android; }
.@{fa-css-prefix}-linux:before { content: @fa-var-linux; }
.@{fa-css-prefix}-dribbble:before { content: @fa-var-dribbble; }
.@{fa-css-prefix}-skype:before { content: @fa-var-skype; }
.@{fa-css-prefix}-foursquare:before { content: @fa-var-foursquare; }
.@{fa-css-prefix}-trello:before { content: @fa-var-trello; }
.@{fa-css-prefix}-female:before { content: @fa-var-female; }
.@{fa-css-prefix}-male:before { content: @fa-var-male; }
.@{fa-css-prefix}-gittip:before,
.@{fa-css-prefix}-gratipay:before { content: @fa-var-gratipay; }
.@{fa-css-prefix}-sun-o:before { content: @fa-var-sun-o; }
.@{fa-css-prefix}-moon-o:before { content: @fa-var-moon-o; }
.@{fa-css-prefix}-archive:before { content: @fa-var-archive; }
.@{fa-css-prefix}-bug:before { content: @fa-var-bug; }
.@{fa-css-prefix}-vk:before { content: @fa-var-vk; }
.@{fa-css-prefix}-weibo:before { content: @fa-var-weibo; }
.@{fa-css-prefix}-renren:before { content: @fa-var-renren; }
.@{fa-css-prefix}-pagelines:before { content: @fa-var-pagelines; }
.@{fa-css-prefix}-stack-exchange:before { content: @fa-var-stack-exchange; }
.@{fa-css-prefix}-arrow-circle-o-right:before { content: @fa-var-arrow-circle-o-right; }
.@{fa-css-prefix}-arrow-circle-o-left:before { content: @fa-var-arrow-circle-o-left; }
.@{fa-css-prefix}-toggle-left:before,
.@{fa-css-prefix}-caret-square-o-left:before { content: @fa-var-caret-square-o-left; }
.@{fa-css-prefix}-dot-circle-o:before { content: @fa-var-dot-circle-o; }
.@{fa-css-prefix}-wheelchair:before { content: @fa-var-wheelchair; }
.@{fa-css-prefix}-vimeo-square:before { content: @fa-var-vimeo-square; }
.@{fa-css-prefix}-turkish-lira:before,
.@{fa-css-prefix}-try:before { content: @fa-var-try; }
.@{fa-css-prefix}-plus-square-o:before { content: @fa-var-plus-square-o; }
.@{fa-css-prefix}-space-shuttle:before { content: @fa-var-space-shuttle; }
.@{fa-css-prefix}-slack:before { content: @fa-var-slack; }
.@{fa-css-prefix}-envelope-square:before { content: @fa-var-envelope-square; }
.@{fa-css-prefix}-wordpress:before { content: @fa-var-wordpress; }
.@{fa-css-prefix}-openid:before { content: @fa-var-openid; }
.@{fa-css-prefix}-institution:before,
.@{fa-css-prefix}-bank:before,
.@{fa-css-prefix}-university:before { content: @fa-var-university; }
.@{fa-css-prefix}-mortar-board:before,
.@{fa-css-prefix}-graduation-cap:before { content: @fa-var-graduation-cap; }
.@{fa-css-prefix}-yahoo:before { content: @fa-var-yahoo; }
.@{fa-css-prefix}-google:before { content: @fa-var-google; }
.@{fa-css-prefix}-reddit:before { content: @fa-var-reddit; }
.@{fa-css-prefix}-reddit-square:before { content: @fa-var-reddit-square; }
.@{fa-css-prefix}-stumbleupon-circle:before { content: @fa-var-stumbleupon-circle; }
.@{fa-css-prefix}-stumbleupon:before { content: @fa-var-stumbleupon; }
.@{fa-css-prefix}-delicious:before { content: @fa-var-delicious; }
.@{fa-css-prefix}-digg:before { content: @fa-var-digg; }
.@{fa-css-prefix}-pied-piper:before { content: @fa-var-pied-piper; }
.@{fa-css-prefix}-pied-piper-alt:before { content: @fa-var-pied-piper-alt; }
.@{fa-css-prefix}-drupal:before { content: @fa-var-drupal; }
.@{fa-css-prefix}-joomla:before { content: @fa-var-joomla; }
.@{fa-css-prefix}-language:before { content: @fa-var-language; }
.@{fa-css-prefix}-fax:before { content: @fa-var-fax; }
.@{fa-css-prefix}-building:before { content: @fa-var-building; }
.@{fa-css-prefix}-child:before { content: @fa-var-child; }
.@{fa-css-prefix}-paw:before { content: @fa-var-paw; }
.@{fa-css-prefix}-spoon:before { content: @fa-var-spoon; }
.@{fa-css-prefix}-cube:before { content: @fa-var-cube; }
.@{fa-css-prefix}-cubes:before { content: @fa-var-cubes; }
.@{fa-css-prefix}-behance:before { content: @fa-var-behance; }
.@{fa-css-prefix}-behance-square:before { content: @fa-var-behance-square; }
.@{fa-css-prefix}-steam:before { content: @fa-var-steam; }
.@{fa-css-prefix}-steam-square:before { content: @fa-var-steam-square; }
.@{fa-css-prefix}-recycle:before { content: @fa-var-recycle; }
.@{fa-css-prefix}-automobile:before,
.@{fa-css-prefix}-car:before { content: @fa-var-car; }
.@{fa-css-prefix}-cab:before,
.@{fa-css-prefix}-taxi:before { content: @fa-var-taxi; }
.@{fa-css-prefix}-tree:before { content: @fa-var-tree; }
.@{fa-css-prefix}-spotify:before { content: @fa-var-spotify; }
.@{fa-css-prefix}-deviantart:before { content: @fa-var-deviantart; }
.@{fa-css-prefix}-soundcloud:before { content: @fa-var-soundcloud; }
.@{fa-css-prefix}-database:before { content: @fa-var-database; }
.@{fa-css-prefix}-file-pdf-o:before { content: @fa-var-file-pdf-o; }
.@{fa-css-prefix}-file-word-o:before { content: @fa-var-file-word-o; }
.@{fa-css-prefix}-file-excel-o:before { content: @fa-var-file-excel-o; }
.@{fa-css-prefix}-file-powerpoint-o:before { content: @fa-var-file-powerpoint-o; }
.@{fa-css-prefix}-file-photo-o:before,
.@{fa-css-prefix}-file-picture-o:before,
.@{fa-css-prefix}-file-image-o:before { content: @fa-var-file-image-o; }
.@{fa-css-prefix}-file-zip-o:before,
.@{fa-css-prefix}-file-archive-o:before { content: @fa-var-file-archive-o; }
.@{fa-css-prefix}-file-sound-o:before,
.@{fa-css-prefix}-file-audio-o:before { content: @fa-var-file-audio-o; }
.@{fa-css-prefix}-file-movie-o:before,
.@{fa-css-prefix}-file-video-o:before { content: @fa-var-file-video-o; }
.@{fa-css-prefix}-file-code-o:before { content: @fa-var-file-code-o; }
.@{fa-css-prefix}-vine:before { content: @fa-var-vine; }
.@{fa-css-prefix}-codepen:before { content: @fa-var-codepen; }
.@{fa-css-prefix}-jsfiddle:before { content: @fa-var-jsfiddle; }
.@{fa-css-prefix}-life-bouy:before,
.@{fa-css-prefix}-life-buoy:before,
.@{fa-css-prefix}-life-saver:before,
.@{fa-css-prefix}-support:before,
.@{fa-css-prefix}-life-ring:before { content: @fa-var-life-ring; }
.@{fa-css-prefix}-circle-o-notch:before { content: @fa-var-circle-o-notch; }
.@{fa-css-prefix}-ra:before,
.@{fa-css-prefix}-rebel:before { content: @fa-var-rebel; }
.@{fa-css-prefix}-ge:before,
.@{fa-css-prefix}-empire:before { content: @fa-var-empire; }
.@{fa-css-prefix}-git-square:before { content: @fa-var-git-square; }
.@{fa-css-prefix}-git:before { content: @fa-var-git; }
.@{fa-css-prefix}-hacker-news:before { content: @fa-var-hacker-news; }
.@{fa-css-prefix}-tencent-weibo:before { content: @fa-var-tencent-weibo; }
.@{fa-css-prefix}-qq:before { content: @fa-var-qq; }
.@{fa-css-prefix}-wechat:before,
.@{fa-css-prefix}-weixin:before { content: @fa-var-weixin; }
.@{fa-css-prefix}-send:before,
.@{fa-css-prefix}-paper-plane:before { content: @fa-var-paper-plane; }
.@{fa-css-prefix}-send-o:before,
.@{fa-css-prefix}-paper-plane-o:before { content: @fa-var-paper-plane-o; }
.@{fa-css-prefix}-history:before { content: @fa-var-history; }
.@{fa-css-prefix}-genderless:before,
.@{fa-css-prefix}-circle-thin:before { content: @fa-var-circle-thin; }
.@{fa-css-prefix}-header:before { content: @fa-var-header; }
.@{fa-css-prefix}-paragraph:before { content: @fa-var-paragraph; }
.@{fa-css-prefix}-sliders:before { content: @fa-var-sliders; }
.@{fa-css-prefix}-share-alt:before { content: @fa-var-share-alt; }
.@{fa-css-prefix}-share-alt-square:before { content: @fa-var-share-alt-square; }
.@{fa-css-prefix}-bomb:before { content: @fa-var-bomb; }
.@{fa-css-prefix}-soccer-ball-o:before,
.@{fa-css-prefix}-futbol-o:before { content: @fa-var-futbol-o; }
.@{fa-css-prefix}-tty:before { content: @fa-var-tty; }
.@{fa-css-prefix}-binoculars:before { content: @fa-var-binoculars; }
.@{fa-css-prefix}-plug:before { content: @fa-var-plug; }
.@{fa-css-prefix}-slideshare:before { content: @fa-var-slideshare; }
.@{fa-css-prefix}-twitch:before { content: @fa-var-twitch; }
.@{fa-css-prefix}-yelp:before { content: @fa-var-yelp; }
.@{fa-css-prefix}-newspaper-o:before { content: @fa-var-newspaper-o; }
.@{fa-css-prefix}-wifi:before { content: @fa-var-wifi; }
.@{fa-css-prefix}-calculator:before { content: @fa-var-calculator; }
.@{fa-css-prefix}-paypal:before { content: @fa-var-paypal; }
.@{fa-css-prefix}-google-wallet:before { content: @fa-var-google-wallet; }
.@{fa-css-prefix}-cc-visa:before { content: @fa-var-cc-visa; }
.@{fa-css-prefix}-cc-mastercard:before { content: @fa-var-cc-mastercard; }
.@{fa-css-prefix}-cc-discover:before { content: @fa-var-cc-discover; }
.@{fa-css-prefix}-cc-amex:before { content: @fa-var-cc-amex; }
.@{fa-css-prefix}-cc-paypal:before { content: @fa-var-cc-paypal; }
.@{fa-css-prefix}-cc-stripe:before { content: @fa-var-cc-stripe; }
.@{fa-css-prefix}-bell-slash:before { content: @fa-var-bell-slash; }
.@{fa-css-prefix}-bell-slash-o:before { content: @fa-var-bell-slash-o; }
.@{fa-css-prefix}-trash:before { content: @fa-var-trash; }
.@{fa-css-prefix}-copyright:before { content: @fa-var-copyright; }
.@{fa-css-prefix}-at:before { content: @fa-var-at; }
.@{fa-css-prefix}-eyedropper:before { content: @fa-var-eyedropper; }
.@{fa-css-prefix}-paint-brush:before { content: @fa-var-paint-brush; }
.@{fa-css-prefix}-birthday-cake:before { content: @fa-var-birthday-cake; }
.@{fa-css-prefix}-area-chart:before { content: @fa-var-area-chart; }
.@{fa-css-prefix}-pie-chart:before { content: @fa-var-pie-chart; }
.@{fa-css-prefix}-line-chart:before { content: @fa-var-line-chart; }
.@{fa-css-prefix}-lastfm:before { content: @fa-var-lastfm; }
.@{fa-css-prefix}-lastfm-square:before { content: @fa-var-lastfm-square; }
.@{fa-css-prefix}-toggle-off:before { content: @fa-var-toggle-off; }
.@{fa-css-prefix}-toggle-on:before { content: @fa-var-toggle-on; }
.@{fa-css-prefix}-bicycle:before { content: @fa-var-bicycle; }
.@{fa-css-prefix}-bus:before { content: @fa-var-bus; }
.@{fa-css-prefix}-ioxhost:before { content: @fa-var-ioxhost; }
.@{fa-css-prefix}-angellist:before { content: @fa-var-angellist; }
.@{fa-css-prefix}-cc:before { content: @fa-var-cc; }
.@{fa-css-prefix}-shekel:before,
.@{fa-css-prefix}-sheqel:before,
.@{fa-css-prefix}-ils:before { content: @fa-var-ils; }
.@{fa-css-prefix}-meanpath:before { content: @fa-var-meanpath; }
.@{fa-css-prefix}-buysellads:before { content: @fa-var-buysellads; }
.@{fa-css-prefix}-connectdevelop:before { content: @fa-var-connectdevelop; }
.@{fa-css-prefix}-dashcube:before { content: @fa-var-dashcube; }
.@{fa-css-prefix}-forumbee:before { content: @fa-var-forumbee; }
.@{fa-css-prefix}-leanpub:before { content: @fa-var-leanpub; }
.@{fa-css-prefix}-sellsy:before { content: @fa-var-sellsy; }
.@{fa-css-prefix}-shirtsinbulk:before { content: @fa-var-shirtsinbulk; }
.@{fa-css-prefix}-simplybuilt:before { content: @fa-var-simplybuilt; }
.@{fa-css-prefix}-skyatlas:before { content: @fa-var-skyatlas; }
.@{fa-css-prefix}-cart-plus:before { content: @fa-var-cart-plus; }
.@{fa-css-prefix}-cart-arrow-down:before { content: @fa-var-cart-arrow-down; }
.@{fa-css-prefix}-diamond:before { content: @fa-var-diamond; }
.@{fa-css-prefix}-ship:before { content: @fa-var-ship; }
.@{fa-css-prefix}-user-secret:before { content: @fa-var-user-secret; }
.@{fa-css-prefix}-motorcycle:before { content: @fa-var-motorcycle; }
.@{fa-css-prefix}-street-view:before { content: @fa-var-street-view; }
.@{fa-css-prefix}-heartbeat:before { content: @fa-var-heartbeat; }
.@{fa-css-prefix}-venus:before { content: @fa-var-venus; }
.@{fa-css-prefix}-mars:before { content: @fa-var-mars; }
.@{fa-css-prefix}-mercury:before { content: @fa-var-mercury; }
.@{fa-css-prefix}-transgender:before { content: @fa-var-transgender; }
.@{fa-css-prefix}-transgender-alt:before { content: @fa-var-transgender-alt; }
.@{fa-css-prefix}-venus-double:before { content: @fa-var-venus-double; }
.@{fa-css-prefix}-mars-double:before { content: @fa-var-mars-double; }
.@{fa-css-prefix}-venus-mars:before { content: @fa-var-venus-mars; }
.@{fa-css-prefix}-mars-stroke:before { content: @fa-var-mars-stroke; }
.@{fa-css-prefix}-mars-stroke-v:before { content: @fa-var-mars-stroke-v; }
.@{fa-css-prefix}-mars-stroke-h:before { content: @fa-var-mars-stroke-h; }
.@{fa-css-prefix}-neuter:before { content: @fa-var-neuter; }
.@{fa-css-prefix}-facebook-official:before { content: @fa-var-facebook-official; }
.@{fa-css-prefix}-pinterest-p:before { content: @fa-var-pinterest-p; }
.@{fa-css-prefix}-whatsapp:before { content: @fa-var-whatsapp; }
.@{fa-css-prefix}-server:before { content: @fa-var-server; }
.@{fa-css-prefix}-user-plus:before { content: @fa-var-user-plus; }
.@{fa-css-prefix}-user-times:before { content: @fa-var-user-times; }
.@{fa-css-prefix}-hotel:before,
.@{fa-css-prefix}-bed:before { content: @fa-var-bed; }
.@{fa-css-prefix}-viacoin:before { content: @fa-var-viacoin; }
.@{fa-css-prefix}-train:before { content: @fa-var-train; }
.@{fa-css-prefix}-subway:before { content: @fa-var-subway; }
.@{fa-css-prefix}-medium:before { content: @fa-var-medium; }


File: /font-awesome\less\larger.less
// Icon Sizes
// -------------------------

/* makes the font 33% larger relative to the icon container */
.@{fa-css-prefix}-lg {
  font-size: (4em / 3);
  line-height: (3em / 4);
  vertical-align: -15%;
}
.@{fa-css-prefix}-2x { font-size: 2em; }
.@{fa-css-prefix}-3x { font-size: 3em; }
.@{fa-css-prefix}-4x { font-size: 4em; }
.@{fa-css-prefix}-5x { font-size: 5em; }


File: /font-awesome\less\list.less
// List Icons
// -------------------------

.@{fa-css-prefix}-ul {
  padding-left: 0;
  margin-left: @fa-li-width;
  list-style-type: none;
  > li { position: relative; }
}
.@{fa-css-prefix}-li {
  position: absolute;
  left: -@fa-li-width;
  width: @fa-li-width;
  top: (2em / 14);
  text-align: center;
  &.@{fa-css-prefix}-lg {
    left: (-@fa-li-width + (4em / 14));
  }
}


File: /font-awesome\less\mixins.less
// Mixins
// --------------------------

.fa-icon() {
  display: inline-block;
  font: normal normal normal @fa-font-size-base/1 FontAwesome; // shortening font declaration
  font-size: inherit; // can't have font-size inherit on line above, so need to override
  text-rendering: auto; // optimizelegibility throws things off #1094
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform: translate(0, 0); // ensures no half-pixel rendering in firefox

}

.fa-icon-rotate(@degrees, @rotation) {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=@rotation);
  -webkit-transform: rotate(@degrees);
      -ms-transform: rotate(@degrees);
          transform: rotate(@degrees);
}

.fa-icon-flip(@horiz, @vert, @rotation) {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=@rotation, mirror=1);
  -webkit-transform: scale(@horiz, @vert);
      -ms-transform: scale(@horiz, @vert);
          transform: scale(@horiz, @vert);
}


File: /font-awesome\less\path.less
/* FONT PATH
 * -------------------------- */

@font-face {
  font-family: 'FontAwesome';
  src: url('@{fa-font-path}/fontawesome-webfont.eot?v=@{fa-version}');
  src: url('@{fa-font-path}/fontawesome-webfont.eot?#iefix&v=@{fa-version}') format('embedded-opentype'),
    url('@{fa-font-path}/fontawesome-webfont.woff2?v=@{fa-version}') format('woff2'),
    url('@{fa-font-path}/fontawesome-webfont.woff?v=@{fa-version}') format('woff'),
    url('@{fa-font-path}/fontawesome-webfont.ttf?v=@{fa-version}') format('truetype'),
    url('@{fa-font-path}/fontawesome-webfont.svg?v=@{fa-version}#fontawesomeregular') format('svg');
//  src: url('@{fa-font-path}/FontAwesome.otf') format('opentype'); // used when developing fonts
  font-weight: normal;
  font-style: normal;
}


File: /font-awesome\less\rotated-flipped.less
// Rotated & Flipped Icons
// -------------------------

.@{fa-css-prefix}-rotate-90  { .fa-icon-rotate(90deg, 1);  }
.@{fa-css-prefix}-rotate-180 { .fa-icon-rotate(180deg, 2); }
.@{fa-css-prefix}-rotate-270 { .fa-icon-rotate(270deg, 3); }

.@{fa-css-prefix}-flip-horizontal { .fa-icon-flip(-1, 1, 0); }
.@{fa-css-prefix}-flip-vertical   { .fa-icon-flip(1, -1, 2); }

// Hook for IE8-9
// -------------------------

:root .@{fa-css-prefix}-rotate-90,
:root .@{fa-css-prefix}-rotate-180,
:root .@{fa-css-prefix}-rotate-270,
:root .@{fa-css-prefix}-flip-horizontal,
:root .@{fa-css-prefix}-flip-vertical {
  filter: none;
}


File: /font-awesome\less\stacked.less
// Stacked Icons
// -------------------------

.@{fa-css-prefix}-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.@{fa-css-prefix}-stack-1x, .@{fa-css-prefix}-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.@{fa-css-prefix}-stack-1x { line-height: inherit; }
.@{fa-css-prefix}-stack-2x { font-size: 2em; }
.@{fa-css-prefix}-inverse { color: @fa-inverse; }


File: /font-awesome\less\variables.less
// Variables
// --------------------------

@fa-font-path:        "../fonts";
@fa-font-size-base:   14px;
//@fa-font-path:        "//netdna.bootstrapcdn.com/font-awesome/4.3.0/fonts"; // for referencing Bootstrap CDN font files directly
@fa-css-prefix:       fa;
@fa-version:          "4.3.0";
@fa-border-color:     #eee;
@fa-inverse:          #fff;
@fa-li-width:         (30em / 14);

@fa-var-adjust: "\f042";
@fa-var-adn: "\f170";
@fa-var-align-center: "\f037";
@fa-var-align-justify: "\f039";
@fa-var-align-left: "\f036";
@fa-var-align-right: "\f038";
@fa-var-ambulance: "\f0f9";
@fa-var-anchor: "\f13d";
@fa-var-android: "\f17b";
@fa-var-angellist: "\f209";
@fa-var-angle-double-down: "\f103";
@fa-var-angle-double-left: "\f100";
@fa-var-angle-double-right: "\f101";
@fa-var-angle-double-up: "\f102";
@fa-var-angle-down: "\f107";
@fa-var-angle-left: "\f104";
@fa-var-angle-right: "\f105";
@fa-var-angle-up: "\f106";
@fa-var-apple: "\f179";
@fa-var-archive: "\f187";
@fa-var-area-chart: "\f1fe";
@fa-var-arrow-circle-down: "\f0ab";
@fa-var-arrow-circle-left: "\f0a8";
@fa-var-arrow-circle-o-down: "\f01a";
@fa-var-arrow-circle-o-left: "\f190";
@fa-var-arrow-circle-o-right: "\f18e";
@fa-var-arrow-circle-o-up: "\f01b";
@fa-var-arrow-circle-right: "\f0a9";
@fa-var-arrow-circle-up: "\f0aa";
@fa-var-arrow-down: "\f063";
@fa-var-arrow-left: "\f060";
@fa-var-arrow-right: "\f061";
@fa-var-arrow-up: "\f062";
@fa-var-arrows: "\f047";
@fa-var-arrows-alt: "\f0b2";
@fa-var-arrows-h: "\f07e";
@fa-var-arrows-v: "\f07d";
@fa-var-asterisk: "\f069";
@fa-var-at: "\f1fa";
@fa-var-automobile: "\f1b9";
@fa-var-backward: "\f04a";
@fa-var-ban: "\f05e";
@fa-var-bank: "\f19c";
@fa-var-bar-chart: "\f080";
@fa-var-bar-chart-o: "\f080";
@fa-var-barcode: "\f02a";
@fa-var-bars: "\f0c9";
@fa-var-bed: "\f236";
@fa-var-beer: "\f0fc";
@fa-var-behance: "\f1b4";
@fa-var-behance-square: "\f1b5";
@fa-var-bell: "\f0f3";
@fa-var-bell-o: "\f0a2";
@fa-var-bell-slash: "\f1f6";
@fa-var-bell-slash-o: "\f1f7";
@fa-var-bicycle: "\f206";
@fa-var-binoculars: "\f1e5";
@fa-var-birthday-cake: "\f1fd";
@fa-var-bitbucket: "\f171";
@fa-var-bitbucket-square: "\f172";
@fa-var-bitcoin: "\f15a";
@fa-var-bold: "\f032";
@fa-var-bolt: "\f0e7";
@fa-var-bomb: "\f1e2";
@fa-var-book: "\f02d";
@fa-var-bookmark: "\f02e";
@fa-var-bookmark-o: "\f097";
@fa-var-briefcase: "\f0b1";
@fa-var-btc: "\f15a";
@fa-var-bug: "\f188";
@fa-var-building: "\f1ad";
@fa-var-building-o: "\f0f7";
@fa-var-bullhorn: "\f0a1";
@fa-var-bullseye: "\f140";
@fa-var-bus: "\f207";
@fa-var-buysellads: "\f20d";
@fa-var-cab: "\f1ba";
@fa-var-calculator: "\f1ec";
@fa-var-calendar: "\f073";
@fa-var-calendar-o: "\f133";
@fa-var-camera: "\f030";
@fa-var-camera-retro: "\f083";
@fa-var-car: "\f1b9";
@fa-var-caret-down: "\f0d7";
@fa-var-caret-left: "\f0d9";
@fa-var-caret-right: "\f0da";
@fa-var-caret-square-o-down: "\f150";
@fa-var-caret-square-o-left: "\f191";
@fa-var-caret-square-o-right: "\f152";
@fa-var-caret-square-o-up: "\f151";
@fa-var-caret-up: "\f0d8";
@fa-var-cart-arrow-down: "\f218";
@fa-var-cart-plus: "\f217";
@fa-var-cc: "\f20a";
@fa-var-cc-amex: "\f1f3";
@fa-var-cc-discover: "\f1f2";
@fa-var-cc-mastercard: "\f1f1";
@fa-var-cc-paypal: "\f1f4";
@fa-var-cc-stripe: "\f1f5";
@fa-var-cc-visa: "\f1f0";
@fa-var-certificate: "\f0a3";
@fa-var-chain: "\f0c1";
@fa-var-chain-broken: "\f127";
@fa-var-check: "\f00c";
@fa-var-check-circle: "\f058";
@fa-var-check-circle-o: "\f05d";
@fa-var-check-square: "\f14a";
@fa-var-check-square-o: "\f046";
@fa-var-chevron-circle-down: "\f13a";
@fa-var-chevron-circle-left: "\f137";
@fa-var-chevron-circle-right: "\f138";
@fa-var-chevron-circle-up: "\f139";
@fa-var-chevron-down: "\f078";
@fa-var-chevron-left: "\f053";
@fa-var-chevron-right: "\f054";
@fa-var-chevron-up: "\f077";
@fa-var-child: "\f1ae";
@fa-var-circle: "\f111";
@fa-var-circle-o: "\f10c";
@fa-var-circle-o-notch: "\f1ce";
@fa-var-circle-thin: "\f1db";
@fa-var-clipboard: "\f0ea";
@fa-var-clock-o: "\f017";
@fa-var-close: "\f00d";
@fa-var-cloud: "\f0c2";
@fa-var-cloud-download: "\f0ed";
@fa-var-cloud-upload: "\f0ee";
@fa-var-cny: "\f157";
@fa-var-code: "\f121";
@fa-var-code-fork: "\f126";
@fa-var-codepen: "\f1cb";
@fa-var-coffee: "\f0f4";
@fa-var-cog: "\f013";
@fa-var-cogs: "\f085";
@fa-var-columns: "\f0db";
@fa-var-comment: "\f075";
@fa-var-comment-o: "\f0e5";
@fa-var-comments: "\f086";
@fa-var-comments-o: "\f0e6";
@fa-var-compass: "\f14e";
@fa-var-compress: "\f066";
@fa-var-connectdevelop: "\f20e";
@fa-var-copy: "\f0c5";
@fa-var-copyright: "\f1f9";
@fa-var-credit-card: "\f09d";
@fa-var-crop: "\f125";
@fa-var-crosshairs: "\f05b";
@fa-var-css3: "\f13c";
@fa-var-cube: "\f1b2";
@fa-var-cubes: "\f1b3";
@fa-var-cut: "\f0c4";
@fa-var-cutlery: "\f0f5";
@fa-var-dashboard: "\f0e4";
@fa-var-dashcube: "\f210";
@fa-var-database: "\f1c0";
@fa-var-dedent: "\f03b";
@fa-var-delicious: "\f1a5";
@fa-var-desktop: "\f108";
@fa-var-deviantart: "\f1bd";
@fa-var-diamond: "\f219";
@fa-var-digg: "\f1a6";
@fa-var-dollar: "\f155";
@fa-var-dot-circle-o: "\f192";
@fa-var-download: "\f019";
@fa-var-dribbble: "\f17d";
@fa-var-dropbox: "\f16b";
@fa-var-drupal: "\f1a9";
@fa-var-edit: "\f044";
@fa-var-eject: "\f052";
@fa-var-ellipsis-h: "\f141";
@fa-var-ellipsis-v: "\f142";
@fa-var-empire: "\f1d1";
@fa-var-envelope: "\f0e0";
@fa-var-envelope-o: "\f003";
@fa-var-envelope-square: "\f199";
@fa-var-eraser: "\f12d";
@fa-var-eur: "\f153";
@fa-var-euro: "\f153";
@fa-var-exchange: "\f0ec";
@fa-var-exclamation: "\f12a";
@fa-var-exclamation-circle: "\f06a";
@fa-var-exclamation-triangle: "\f071";
@fa-var-expand: "\f065";
@fa-var-external-link: "\f08e";
@fa-var-external-link-square: "\f14c";
@fa-var-eye: "\f06e";
@fa-var-eye-slash: "\f070";
@fa-var-eyedropper: "\f1fb";
@fa-var-facebook: "\f09a";
@fa-var-facebook-f: "\f09a";
@fa-var-facebook-official: "\f230";
@fa-var-facebook-square: "\f082";
@fa-var-fast-backward: "\f049";
@fa-var-fast-forward: "\f050";
@fa-var-fax: "\f1ac";
@fa-var-female: "\f182";
@fa-var-fighter-jet: "\f0fb";
@fa-var-file: "\f15b";
@fa-var-file-archive-o: "\f1c6";
@fa-var-file-audio-o: "\f1c7";
@fa-var-file-code-o: "\f1c9";
@fa-var-file-excel-o: "\f1c3";
@fa-var-file-image-o: "\f1c5";
@fa-var-file-movie-o: "\f1c8";
@fa-var-file-o: "\f016";
@fa-var-file-pdf-o: "\f1c1";
@fa-var-file-photo-o: "\f1c5";
@fa-var-file-picture-o: "\f1c5";
@fa-var-file-powerpoint-o: "\f1c4";
@fa-var-file-sound-o: "\f1c7";
@fa-var-file-text: "\f15c";
@fa-var-file-text-o: "\f0f6";
@fa-var-file-video-o: "\f1c8";
@fa-var-file-word-o: "\f1c2";
@fa-var-file-zip-o: "\f1c6";
@fa-var-files-o: "\f0c5";
@fa-var-film: "\f008";
@fa-var-filter: "\f0b0";
@fa-var-fire: "\f06d";
@fa-var-fire-extinguisher: "\f134";
@fa-var-flag: "\f024";
@fa-var-flag-checkered: "\f11e";
@fa-var-flag-o: "\f11d";
@fa-var-flash: "\f0e7";
@fa-var-flask: "\f0c3";
@fa-var-flickr: "\f16e";
@fa-var-floppy-o: "\f0c7";
@fa-var-folder: "\f07b";
@fa-var-folder-o: "\f114";
@fa-var-folder-open: "\f07c";
@fa-var-folder-open-o: "\f115";
@fa-var-font: "\f031";
@fa-var-forumbee: "\f211";
@fa-var-forward: "\f04e";
@fa-var-foursquare: "\f180";
@fa-var-frown-o: "\f119";
@fa-var-futbol-o: "\f1e3";
@fa-var-gamepad: "\f11b";
@fa-var-gavel: "\f0e3";
@fa-var-gbp: "\f154";
@fa-var-ge: "\f1d1";
@fa-var-gear: "\f013";
@fa-var-gears: "\f085";
@fa-var-genderless: "\f1db";
@fa-var-gift: "\f06b";
@fa-var-git: "\f1d3";
@fa-var-git-square: "\f1d2";
@fa-var-github: "\f09b";
@fa-var-github-alt: "\f113";
@fa-var-github-square: "\f092";
@fa-var-gittip: "\f184";
@fa-var-glass: "\f000";
@fa-var-globe: "\f0ac";
@fa-var-google: "\f1a0";
@fa-var-google-plus: "\f0d5";
@fa-var-google-plus-square: "\f0d4";
@fa-var-google-wallet: "\f1ee";
@fa-var-graduation-cap: "\f19d";
@fa-var-gratipay: "\f184";
@fa-var-group: "\f0c0";
@fa-var-h-square: "\f0fd";
@fa-var-hacker-news: "\f1d4";
@fa-var-hand-o-down: "\f0a7";
@fa-var-hand-o-left: "\f0a5";
@fa-var-hand-o-right: "\f0a4";
@fa-var-hand-o-up: "\f0a6";
@fa-var-hdd-o: "\f0a0";
@fa-var-header: "\f1dc";
@fa-var-headphones: "\f025";
@fa-var-heart: "\f004";
@fa-var-heart-o: "\f08a";
@fa-var-heartbeat: "\f21e";
@fa-var-history: "\f1da";
@fa-var-home: "\f015";
@fa-var-hospital-o: "\f0f8";
@fa-var-hotel: "\f236";
@fa-var-html5: "\f13b";
@fa-var-ils: "\f20b";
@fa-var-image: "\f03e";
@fa-var-inbox: "\f01c";
@fa-var-indent: "\f03c";
@fa-var-info: "\f129";
@fa-var-info-circle: "\f05a";
@fa-var-inr: "\f156";
@fa-var-instagram: "\f16d";
@fa-var-institution: "\f19c";
@fa-var-ioxhost: "\f208";
@fa-var-italic: "\f033";
@fa-var-joomla: "\f1aa";
@fa-var-jpy: "\f157";
@fa-var-jsfiddle: "\f1cc";
@fa-var-key: "\f084";
@fa-var-keyboard-o: "\f11c";
@fa-var-krw: "\f159";
@fa-var-language: "\f1ab";
@fa-var-laptop: "\f109";
@fa-var-lastfm: "\f202";
@fa-var-lastfm-square: "\f203";
@fa-var-leaf: "\f06c";
@fa-var-leanpub: "\f212";
@fa-var-legal: "\f0e3";
@fa-var-lemon-o: "\f094";
@fa-var-level-down: "\f149";
@fa-var-level-up: "\f148";
@fa-var-life-bouy: "\f1cd";
@fa-var-life-buoy: "\f1cd";
@fa-var-life-ring: "\f1cd";
@fa-var-life-saver: "\f1cd";
@fa-var-lightbulb-o: "\f0eb";
@fa-var-line-chart: "\f201";
@fa-var-link: "\f0c1";
@fa-var-linkedin: "\f0e1";
@fa-var-linkedin-square: "\f08c";
@fa-var-linux: "\f17c";
@fa-var-list: "\f03a";
@fa-var-list-alt: "\f022";
@fa-var-list-ol: "\f0cb";
@fa-var-list-ul: "\f0ca";
@fa-var-location-arrow: "\f124";
@fa-var-lock: "\f023";
@fa-var-long-arrow-down: "\f175";
@fa-var-long-arrow-left: "\f177";
@fa-var-long-arrow-right: "\f178";
@fa-var-long-arrow-up: "\f176";
@fa-var-magic: "\f0d0";
@fa-var-magnet: "\f076";
@fa-var-mail-forward: "\f064";
@fa-var-mail-reply: "\f112";
@fa-var-mail-reply-all: "\f122";
@fa-var-male: "\f183";
@fa-var-map-marker: "\f041";
@fa-var-mars: "\f222";
@fa-var-mars-double: "\f227";
@fa-var-mars-stroke: "\f229";
@fa-var-mars-stroke-h: "\f22b";
@fa-var-mars-stroke-v: "\f22a";
@fa-var-maxcdn: "\f136";
@fa-var-meanpath: "\f20c";
@fa-var-medium: "\f23a";
@fa-var-medkit: "\f0fa";
@fa-var-meh-o: "\f11a";
@fa-var-mercury: "\f223";
@fa-var-microphone: "\f130";
@fa-var-microphone-slash: "\f131";
@fa-var-minus: "\f068";
@fa-var-minus-circle: "\f056";
@fa-var-minus-square: "\f146";
@fa-var-minus-square-o: "\f147";
@fa-var-mobile: "\f10b";
@fa-var-mobile-phone: "\f10b";
@fa-var-money: "\f0d6";
@fa-var-moon-o: "\f186";
@fa-var-mortar-board: "\f19d";
@fa-var-motorcycle: "\f21c";
@fa-var-music: "\f001";
@fa-var-navicon: "\f0c9";
@fa-var-neuter: "\f22c";
@fa-var-newspaper-o: "\f1ea";
@fa-var-openid: "\f19b";
@fa-var-outdent: "\f03b";
@fa-var-pagelines: "\f18c";
@fa-var-paint-brush: "\f1fc";
@fa-var-paper-plane: "\f1d8";
@fa-var-paper-plane-o: "\f1d9";
@fa-var-paperclip: "\f0c6";
@fa-var-paragraph: "\f1dd";
@fa-var-paste: "\f0ea";
@fa-var-pause: "\f04c";
@fa-var-paw: "\f1b0";
@fa-var-paypal: "\f1ed";
@fa-var-pencil: "\f040";
@fa-var-pencil-square: "\f14b";
@fa-var-pencil-square-o: "\f044";
@fa-var-phone: "\f095";
@fa-var-phone-square: "\f098";
@fa-var-photo: "\f03e";
@fa-var-picture-o: "\f03e";
@fa-var-pie-chart: "\f200";
@fa-var-pied-piper: "\f1a7";
@fa-var-pied-piper-alt: "\f1a8";
@fa-var-pinterest: "\f0d2";
@fa-var-pinterest-p: "\f231";
@fa-var-pinterest-square: "\f0d3";
@fa-var-plane: "\f072";
@fa-var-play: "\f04b";
@fa-var-play-circle: "\f144";
@fa-var-play-circle-o: "\f01d";
@fa-var-plug: "\f1e6";
@fa-var-plus: "\f067";
@fa-var-plus-circle: "\f055";
@fa-var-plus-square: "\f0fe";
@fa-var-plus-square-o: "\f196";
@fa-var-power-off: "\f011";
@fa-var-print: "\f02f";
@fa-var-puzzle-piece: "\f12e";
@fa-var-qq: "\f1d6";
@fa-var-qrcode: "\f029";
@fa-var-question: "\f128";
@fa-var-question-circle: "\f059";
@fa-var-quote-left: "\f10d";
@fa-var-quote-right: "\f10e";
@fa-var-ra: "\f1d0";
@fa-var-random: "\f074";
@fa-var-rebel: "\f1d0";
@fa-var-recycle: "\f1b8";
@fa-var-reddit: "\f1a1";
@fa-var-reddit-square: "\f1a2";
@fa-var-refresh: "\f021";
@fa-var-remove: "\f00d";
@fa-var-renren: "\f18b";
@fa-var-reorder: "\f0c9";
@fa-var-repeat: "\f01e";
@fa-var-reply: "\f112";
@fa-var-reply-all: "\f122";
@fa-var-retweet: "\f079";
@fa-var-rmb: "\f157";
@fa-var-road: "\f018";
@fa-var-rocket: "\f135";
@fa-var-rotate-left: "\f0e2";
@fa-var-rotate-right: "\f01e";
@fa-var-rouble: "\f158";
@fa-var-rss: "\f09e";
@fa-var-rss-square: "\f143";
@fa-var-rub: "\f158";
@fa-var-ruble: "\f158";
@fa-var-rupee: "\f156";
@fa-var-save: "\f0c7";
@fa-var-scissors: "\f0c4";
@fa-var-search: "\f002";
@fa-var-search-minus: "\f010";
@fa-var-search-plus: "\f00e";
@fa-var-sellsy: "\f213";
@fa-var-send: "\f1d8";
@fa-var-send-o: "\f1d9";
@fa-var-server: "\f233";
@fa-var-share: "\f064";
@fa-var-share-alt: "\f1e0";
@fa-var-share-alt-square: "\f1e1";
@fa-var-share-square: "\f14d";
@fa-var-share-square-o: "\f045";
@fa-var-shekel: "\f20b";
@fa-var-sheqel: "\f20b";
@fa-var-shield: "\f132";
@fa-var-ship: "\f21a";
@fa-var-shirtsinbulk: "\f214";
@fa-var-shopping-cart: "\f07a";
@fa-var-sign-in: "\f090";
@fa-var-sign-out: "\f08b";
@fa-var-signal: "\f012";
@fa-var-simplybuilt: "\f215";
@fa-var-sitemap: "\f0e8";
@fa-var-skyatlas: "\f216";
@fa-var-skype: "\f17e";
@fa-var-slack: "\f198";
@fa-var-sliders: "\f1de";
@fa-var-slideshare: "\f1e7";
@fa-var-smile-o: "\f118";
@fa-var-soccer-ball-o: "\f1e3";
@fa-var-sort: "\f0dc";
@fa-var-sort-alpha-asc: "\f15d";
@fa-var-sort-alpha-desc: "\f15e";
@fa-var-sort-amount-asc: "\f160";
@fa-var-sort-amount-desc: "\f161";
@fa-var-sort-asc: "\f0de";
@fa-var-sort-desc: "\f0dd";
@fa-var-sort-down: "\f0dd";
@fa-var-sort-numeric-asc: "\f162";
@fa-var-sort-numeric-desc: "\f163";
@fa-var-sort-up: "\f0de";
@fa-var-soundcloud: "\f1be";
@fa-var-space-shuttle: "\f197";
@fa-var-spinner: "\f110";
@fa-var-spoon: "\f1b1";
@fa-var-spotify: "\f1bc";
@fa-var-square: "\f0c8";
@fa-var-square-o: "\f096";
@fa-var-stack-exchange: "\f18d";
@fa-var-stack-overflow: "\f16c";
@fa-var-star: "\f005";
@fa-var-star-half: "\f089";
@fa-var-star-half-empty: "\f123";
@fa-var-star-half-full: "\f123";
@fa-var-star-half-o: "\f123";
@fa-var-star-o: "\f006";
@fa-var-steam: "\f1b6";
@fa-var-steam-square: "\f1b7";
@fa-var-step-backward: "\f048";
@fa-var-step-forward: "\f051";
@fa-var-stethoscope: "\f0f1";
@fa-var-stop: "\f04d";
@fa-var-street-view: "\f21d";
@fa-var-strikethrough: "\f0cc";
@fa-var-stumbleupon: "\f1a4";
@fa-var-stumbleupon-circle: "\f1a3";
@fa-var-subscript: "\f12c";
@fa-var-subway: "\f239";
@fa-var-suitcase: "\f0f2";
@fa-var-sun-o: "\f185";
@fa-var-superscript: "\f12b";
@fa-var-support: "\f1cd";
@fa-var-table: "\f0ce";
@fa-var-tablet: "\f10a";
@fa-var-tachometer: "\f0e4";
@fa-var-tag: "\f02b";
@fa-var-tags: "\f02c";
@fa-var-tasks: "\f0ae";
@fa-var-taxi: "\f1ba";
@fa-var-tencent-weibo: "\f1d5";
@fa-var-terminal: "\f120";
@fa-var-text-height: "\f034";
@fa-var-text-width: "\f035";
@fa-var-th: "\f00a";
@fa-var-th-large: "\f009";
@fa-var-th-list: "\f00b";
@fa-var-thumb-tack: "\f08d";
@fa-var-thumbs-down: "\f165";
@fa-var-thumbs-o-down: "\f088";
@fa-var-thumbs-o-up: "\f087";
@fa-var-thumbs-up: "\f164";
@fa-var-ticket: "\f145";
@fa-var-times: "\f00d";
@fa-var-times-circle: "\f057";
@fa-var-times-circle-o: "\f05c";
@fa-var-tint: "\f043";
@fa-var-toggle-down: "\f150";
@fa-var-toggle-left: "\f191";
@fa-var-toggle-off: "\f204";
@fa-var-toggle-on: "\f205";
@fa-var-toggle-right: "\f152";
@fa-var-toggle-up: "\f151";
@fa-var-train: "\f238";
@fa-var-transgender: "\f224";
@fa-var-transgender-alt: "\f225";
@fa-var-trash: "\f1f8";
@fa-var-trash-o: "\f014";
@fa-var-tree: "\f1bb";
@fa-var-trello: "\f181";
@fa-var-trophy: "\f091";
@fa-var-truck: "\f0d1";
@fa-var-try: "\f195";
@fa-var-tty: "\f1e4";
@fa-var-tumblr: "\f173";
@fa-var-tumblr-square: "\f174";
@fa-var-turkish-lira: "\f195";
@fa-var-twitch: "\f1e8";
@fa-var-twitter: "\f099";
@fa-var-twitter-square: "\f081";
@fa-var-umbrella: "\f0e9";
@fa-var-underline: "\f0cd";
@fa-var-undo: "\f0e2";
@fa-var-university: "\f19c";
@fa-var-unlink: "\f127";
@fa-var-unlock: "\f09c";
@fa-var-unlock-alt: "\f13e";
@fa-var-unsorted: "\f0dc";
@fa-var-upload: "\f093";
@fa-var-usd: "\f155";
@fa-var-user: "\f007";
@fa-var-user-md: "\f0f0";
@fa-var-user-plus: "\f234";
@fa-var-user-secret: "\f21b";
@fa-var-user-times: "\f235";
@fa-var-users: "\f0c0";
@fa-var-venus: "\f221";
@fa-var-venus-double: "\f226";
@fa-var-venus-mars: "\f228";
@fa-var-viacoin: "\f237";
@fa-var-video-camera: "\f03d";
@fa-var-vimeo-square: "\f194";
@fa-var-vine: "\f1ca";
@fa-var-vk: "\f189";
@fa-var-volume-down: "\f027";
@fa-var-volume-off: "\f026";
@fa-var-volume-up: "\f028";
@fa-var-warning: "\f071";
@fa-var-wechat: "\f1d7";
@fa-var-weibo: "\f18a";
@fa-var-weixin: "\f1d7";
@fa-var-whatsapp: "\f232";
@fa-var-wheelchair: "\f193";
@fa-var-wifi: "\f1eb";
@fa-var-windows: "\f17a";
@fa-var-won: "\f159";
@fa-var-wordpress: "\f19a";
@fa-var-wrench: "\f0ad";
@fa-var-xing: "\f168";
@fa-var-xing-square: "\f169";
@fa-var-yahoo: "\f19e";
@fa-var-yelp: "\f1e9";
@fa-var-yen: "\f157";
@fa-var-youtube: "\f167";
@fa-var-youtube-play: "\f16a";
@fa-var-youtube-square: "\f166";



File: /font-awesome\package.json
{
  "name": "font-awesome",
  "description": "The iconic font and CSS framework",
  "version": "4.3.0",
  "keywords": [
    "font",
    "awesome",
    "fontawesome",
    "icon",
    "font",
    "bootstrap"
  ],
  "homepage": "http://fontawesome.io/",
  "bugs": {
    "url": "http://github.com/FortAwesome/Font-Awesome/issues"
  },
  "author": {
    "name": "Dave Gandy",
    "email": "dave@fontawesome.io",
    "url": "http://twitter.com/davegandy"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/FortAwesome/Font-Awesome.git"
  },
  "contributors": [
    {
      "name": "Rob Madole",
      "url": "http://twitter.com/robmadole"
    },
    {
      "name": "Geremia Taglialatela",
      "url": "http://twitter.com/gtagliala"
    },
    {
      "name": "Travis Chase",
      "url": "http://twitter.com/supercodepoet"
    }
  ],
  "licenses": [
    {
      "type": "OFL-1.1",
      "url": "http://scripts.sil.org/OFL"
    },
    {
      "type": "MIT",
      "url": "http://opensource.org/licenses/mit-license.html"
    }
  ],
  "dependencies": {},
  "engines": {
    "node": ">=0.10.3"
  },
  "readme": "#[Font Awesome v4.3.0](http://fontawesome.io)\n###The iconic font and CSS framework\n\nFont Awesome is a full suite of 519 pictographic icons for easy scalable vector graphics on websites,\ncreated and maintained by [Dave Gandy](http://twitter.com/davegandy).\nStay up to date with the latest release and announcements on Twitter:\n[@fontawesome](http://twitter.com/fontawesome).\n\nGet started at http://fontawesome.io!\n\n##License\n- The Font Awesome font is licensed under the SIL OFL 1.1:\n  - http://scripts.sil.org/OFL\n- Font Awesome CSS, LESS, and Sass files are licensed under the MIT License:\n  - http://opensource.org/licenses/mit-license.html\n- The Font Awesome documentation is licensed under the CC BY 3.0 License:\n  - http://creativecommons.org/licenses/by/3.0/\n- Attribution is no longer required as of Font Awesome 3.0, but much appreciated:\n  - `Font Awesome by Dave Gandy - http://fontawesome.io`\n- Full details: http://fontawesome.io/license\n\n##Changelog\n- v3.0.0 - all icons redesigned from scratch, optimized for Bootstrap's 14px default\n- v3.0.1 - much improved rendering in webkit, various bug fixes\n- v3.0.2 - much improved rendering and alignment in IE7\n- v3.1.0 - Added 54 icons, icon stacking styles, flipping and rotating icons, removed Sass support\n- [v3.1.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=4&page=1&state=closed)\n- [v3.2.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=3&page=1&state=closed)\n- [v3.2.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=5&page=1&state=closed)\n- [v4.0.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=2&page=1&state=closed)\n- [v4.0.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=7&page=1&state=closed)\n- [v4.0.2 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=8&page=1&state=closed)\n- [v4.0.3 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=9&page=1&state=closed)\n- [v4.1.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=6&page=1&state=closed)\n- [v4.2.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=12&page=1&state=closed)\n- [v4.3.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?q=milestone%3A4.3.0+is%3Aclosed)\n\n## Contributing\n\nPlease read through our [contributing guidelines](https://github.com/FortAwesome/Font-Awesome/blob/master/CONTRIBUTING.md).\nIncluded are directions for opening issues, coding standards, and notes on development.\n\n##Versioning\n\nFont Awesome will be maintained under the Semantic Versioning guidelines as much as possible. Releases will be numbered\nwith the following format:\n\n`<major>.<minor>.<patch>`\n\nAnd constructed with the following guidelines:\n\n* Breaking backward compatibility bumps the major (and resets the minor and patch)\n* New additions, including new icons, without breaking backward compatibility bumps the minor (and resets the patch)\n* Bug fixes and misc changes bumps the patch\n\nFor more information on SemVer, please visit http://semver.org.\n\n##Author\n- Email: dave@fontawesome.io\n- Twitter: http://twitter.com/davegandy\n- GitHub: https://github.com/davegandy\n\n##Component\nTo include as a [component](http://github.com/component/component), just run\n\n    $ component install FortAwesome/Font-Awesome\n\nOr add\n\n    \"FortAwesome/Font-Awesome\": \"*\"\n\nto the `dependencies` in your `component.json`.\n\n## Hacking on Font Awesome\n\nFrom the root of the repository, install the tools used to develop.\n\n    $ bundle install\n    $ npm install\n\nBuild the project and documentation:\n\n    $ bundle exec jekyll build\n\nOr serve it on a local server on http://localhost:7998/Font-Awesome/:\n\n    $ bundle exec jekyll -w serve\n",
  "readmeFilename": "README.md",
  "_id": "font-awesome@4.3.0",
  "dist": {
    "shasum": "a2c0daa3d66c0d592af1c2723e940b926110e0a6"
  },
  "_from": "font-awesome@4.3.0",
  "_resolved": "https://registry.npmjs.org/font-awesome/-/font-awesome-4.3.0.tgz"
}


File: /font-awesome\README.md
#[Font Awesome v4.3.0](http://fontawesome.io)
###The iconic font and CSS framework

Font Awesome is a full suite of 519 pictographic icons for easy scalable vector graphics on websites,
created and maintained by [Dave Gandy](http://twitter.com/davegandy).
Stay up to date with the latest release and announcements on Twitter:
[@fontawesome](http://twitter.com/fontawesome).

Get started at http://fontawesome.io!

##License
- The Font Awesome font is licensed under the SIL OFL 1.1:
  - http://scripts.sil.org/OFL
- Font Awesome CSS, LESS, and Sass files are licensed under the MIT License:
  - http://opensource.org/licenses/mit-license.html
- The Font Awesome documentation is licensed under the CC BY 3.0 License:
  - http://creativecommons.org/licenses/by/3.0/
- Attribution is no longer required as of Font Awesome 3.0, but much appreciated:
  - `Font Awesome by Dave Gandy - http://fontawesome.io`
- Full details: http://fontawesome.io/license

##Changelog
- v3.0.0 - all icons redesigned from scratch, optimized for Bootstrap's 14px default
- v3.0.1 - much improved rendering in webkit, various bug fixes
- v3.0.2 - much improved rendering and alignment in IE7
- v3.1.0 - Added 54 icons, icon stacking styles, flipping and rotating icons, removed Sass support
- [v3.1.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=4&page=1&state=closed)
- [v3.2.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=3&page=1&state=closed)
- [v3.2.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=5&page=1&state=closed)
- [v4.0.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=2&page=1&state=closed)
- [v4.0.1 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=7&page=1&state=closed)
- [v4.0.2 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=8&page=1&state=closed)
- [v4.0.3 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=9&page=1&state=closed)
- [v4.1.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=6&page=1&state=closed)
- [v4.2.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?milestone=12&page=1&state=closed)
- [v4.3.0 GitHub milestones](https://github.com/FortAwesome/Font-Awesome/issues?q=milestone%3A4.3.0+is%3Aclosed)

## Contributing

Please read through our [contributing guidelines](https://github.com/FortAwesome/Font-Awesome/blob/master/CONTRIBUTING.md).
Included are directions for opening issues, coding standards, and notes on development.

##Versioning

Font Awesome will be maintained under the Semantic Versioning guidelines as much as possible. Releases will be numbered
with the following format:

`<major>.<minor>.<patch>`

And constructed with the following guidelines:

* Breaking backward compatibility bumps the major (and resets the minor and patch)
* New additions, including new icons, without breaking backward compatibility bumps the minor (and resets the patch)
* Bug fixes and misc changes bumps the patch

For more information on SemVer, please visit http://semver.org.

##Author
- Email: dave@fontawesome.io
- Twitter: http://twitter.com/davegandy
- GitHub: https://github.com/davegandy

##Component
To include as a [component](http://github.com/component/component), just run

    $ component install FortAwesome/Font-Awesome

Or add

    "FortAwesome/Font-Awesome": "*"

to the `dependencies` in your `component.json`.

## Hacking on Font Awesome

From the root of the repository, install the tools used to develop.

    $ bundle install
    $ npm install

Build the project and documentation:

    $ bundle exec jekyll build

Or serve it on a local server on http://localhost:7998/Font-Awesome/:

    $ bundle exec jekyll -w serve


File: /font-awesome\scss\font-awesome.scss
/*!
 *  Font Awesome 4.3.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */

@import "variables";
@import "mixins";
@import "path";
@import "core";
@import "larger";
@import "fixed-width";
@import "list";
@import "bordered-pulled";
@import "animated";
@import "rotated-flipped";
@import "stacked";
@import "icons";


File: /font-awesome\scss\_animated.scss
// Spinning Icons
// --------------------------

.#{$fa-css-prefix}-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear;
}

.#{$fa-css-prefix}-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8);
}

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
            transform: rotate(359deg);
  }
}

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
            transform: rotate(359deg);
  }
}


File: /font-awesome\scss\_bordered-pulled.scss
// Bordered & Pulled
// -------------------------

.#{$fa-css-prefix}-border {
  padding: .2em .25em .15em;
  border: solid .08em $fa-border-color;
  border-radius: .1em;
}

.pull-right { float: right; }
.pull-left { float: left; }

.#{$fa-css-prefix} {
  &.pull-left { margin-right: .3em; }
  &.pull-right { margin-left: .3em; }
}


File: /font-awesome\scss\_core.scss
// Base Class Definition
// -------------------------

.#{$fa-css-prefix} {
  display: inline-block;
  font: normal normal normal #{$fa-font-size-base}/1 FontAwesome; // shortening font declaration
  font-size: inherit; // can't have font-size inherit on line above, so need to override
  text-rendering: auto; // optimizelegibility throws things off #1094
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform: translate(0, 0); // ensures no half-pixel rendering in firefox

}


File: /font-awesome\scss\_fixed-width.scss
// Fixed Width Icons
// -------------------------
.#{$fa-css-prefix}-fw {
  width: (18em / 14);
  text-align: center;
}


File: /font-awesome\scss\_icons.scss
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */

.#{$fa-css-prefix}-glass:before { content: $fa-var-glass; }
.#{$fa-css-prefix}-music:before { content: $fa-var-music; }
.#{$fa-css-prefix}-search:before { content: $fa-var-search; }
.#{$fa-css-prefix}-envelope-o:before { content: $fa-var-envelope-o; }
.#{$fa-css-prefix}-heart:before { content: $fa-var-heart; }
.#{$fa-css-prefix}-star:before { content: $fa-var-star; }
.#{$fa-css-prefix}-star-o:before { content: $fa-var-star-o; }
.#{$fa-css-prefix}-user:before { content: $fa-var-user; }
.#{$fa-css-prefix}-film:before { content: $fa-var-film; }
.#{$fa-css-prefix}-th-large:before { content: $fa-var-th-large; }
.#{$fa-css-prefix}-th:before { content: $fa-var-th; }
.#{$fa-css-prefix}-th-list:before { content: $fa-var-th-list; }
.#{$fa-css-prefix}-check:before { content: $fa-var-check; }
.#{$fa-css-prefix}-remove:before,
.#{$fa-css-prefix}-close:before,
.#{$fa-css-prefix}-times:before { content: $fa-var-times; }
.#{$fa-css-prefix}-search-plus:before { content: $fa-var-search-plus; }
.#{$fa-css-prefix}-search-minus:before { content: $fa-var-search-minus; }
.#{$fa-css-prefix}-power-off:before { content: $fa-var-power-off; }
.#{$fa-css-prefix}-signal:before { content: $fa-var-signal; }
.#{$fa-css-prefix}-gear:before,
.#{$fa-css-prefix}-cog:before { content: $fa-var-cog; }
.#{$fa-css-prefix}-trash-o:before { content: $fa-var-trash-o; }
.#{$fa-css-prefix}-home:before { content: $fa-var-home; }
.#{$fa-css-prefix}-file-o:before { content: $fa-var-file-o; }
.#{$fa-css-prefix}-clock-o:before { content: $fa-var-clock-o; }
.#{$fa-css-prefix}-road:before { content: $fa-var-road; }
.#{$fa-css-prefix}-download:before { content: $fa-var-download; }
.#{$fa-css-prefix}-arrow-circle-o-down:before { content: $fa-var-arrow-circle-o-down; }
.#{$fa-css-prefix}-arrow-circle-o-up:before { content: $fa-var-arrow-circle-o-up; }
.#{$fa-css-prefix}-inbox:before { content: $fa-var-inbox; }
.#{$fa-css-prefix}-play-circle-o:before { content: $fa-var-play-circle-o; }
.#{$fa-css-prefix}-rotate-right:before,
.#{$fa-css-prefix}-repeat:before { content: $fa-var-repeat; }
.#{$fa-css-prefix}-refresh:before { content: $fa-var-refresh; }
.#{$fa-css-prefix}-list-alt:before { content: $fa-var-list-alt; }
.#{$fa-css-prefix}-lock:before { content: $fa-var-lock; }
.#{$fa-css-prefix}-flag:before { content: $fa-var-flag; }
.#{$fa-css-prefix}-headphones:before { content: $fa-var-headphones; }
.#{$fa-css-prefix}-volume-off:before { content: $fa-var-volume-off; }
.#{$fa-css-prefix}-volume-down:before { content: $fa-var-volume-down; }
.#{$fa-css-prefix}-volume-up:before { content: $fa-var-volume-up; }
.#{$fa-css-prefix}-qrcode:before { content: $fa-var-qrcode; }
.#{$fa-css-prefix}-barcode:before { content: $fa-var-barcode; }
.#{$fa-css-prefix}-tag:before { content: $fa-var-tag; }
.#{$fa-css-prefix}-tags:before { content: $fa-var-tags; }
.#{$fa-css-prefix}-book:before { content: $fa-var-book; }
.#{$fa-css-prefix}-bookmark:before { content: $fa-var-bookmark; }
.#{$fa-css-prefix}-print:before { content: $fa-var-print; }
.#{$fa-css-prefix}-camera:before { content: $fa-var-camera; }
.#{$fa-css-prefix}-font:before { content: $fa-var-font; }
.#{$fa-css-prefix}-bold:before { content: $fa-var-bold; }
.#{$fa-css-prefix}-italic:before { content: $fa-var-italic; }
.#{$fa-css-prefix}-text-height:before { content: $fa-var-text-height; }
.#{$fa-css-prefix}-text-width:before { content: $fa-var-text-width; }
.#{$fa-css-prefix}-align-left:before { content: $fa-var-align-left; }
.#{$fa-css-prefix}-align-center:before { content: $fa-var-align-center; }
.#{$fa-css-prefix}-align-right:before { content: $fa-var-align-right; }
.#{$fa-css-prefix}-align-justify:before { content: $fa-var-align-justify; }
.#{$fa-css-prefix}-list:before { content: $fa-var-list; }
.#{$fa-css-prefix}-dedent:before,
.#{$fa-css-prefix}-outdent:before { content: $fa-var-outdent; }
.#{$fa-css-prefix}-indent:before { content: $fa-var-indent; }
.#{$fa-css-prefix}-video-camera:before { content: $fa-var-video-camera; }
.#{$fa-css-prefix}-photo:before,
.#{$fa-css-prefix}-image:before,
.#{$fa-css-prefix}-picture-o:before { content: $fa-var-picture-o; }
.#{$fa-css-prefix}-pencil:before { content: $fa-var-pencil; }
.#{$fa-css-prefix}-map-marker:before { content: $fa-var-map-marker; }
.#{$fa-css-prefix}-adjust:before { content: $fa-var-adjust; }
.#{$fa-css-prefix}-tint:before { content: $fa-var-tint; }
.#{$fa-css-prefix}-edit:before,
.#{$fa-css-prefix}-pencil-square-o:before { content: $fa-var-pencil-square-o; }
.#{$fa-css-prefix}-share-square-o:before { content: $fa-var-share-square-o; }
.#{$fa-css-prefix}-check-square-o:before { content: $fa-var-check-square-o; }
.#{$fa-css-prefix}-arrows:before { content: $fa-var-arrows; }
.#{$fa-css-prefix}-step-backward:before { content: $fa-var-step-backward; }
.#{$fa-css-prefix}-fast-backward:before { content: $fa-var-fast-backward; }
.#{$fa-css-prefix}-backward:before { content: $fa-var-backward; }
.#{$fa-css-prefix}-play:before { content: $fa-var-play; }
.#{$fa-css-prefix}-pause:before { content: $fa-var-pause; }
.#{$fa-css-prefix}-stop:before { content: $fa-var-stop; }
.#{$fa-css-prefix}-forward:before { content: $fa-var-forward; }
.#{$fa-css-prefix}-fast-forward:before { content: $fa-var-fast-forward; }
.#{$fa-css-prefix}-step-forward:before { content: $fa-var-step-forward; }
.#{$fa-css-prefix}-eject:before { content: $fa-var-eject; }
.#{$fa-css-prefix}-chevron-left:before { content: $fa-var-chevron-left; }
.#{$fa-css-prefix}-chevron-right:before { content: $fa-var-chevron-right; }
.#{$fa-css-prefix}-plus-circle:before { content: $fa-var-plus-circle; }
.#{$fa-css-prefix}-minus-circle:before { content: $fa-var-minus-circle; }
.#{$fa-css-prefix}-times-circle:before { content: $fa-var-times-circle; }
.#{$fa-css-prefix}-check-circle:before { content: $fa-var-check-circle; }
.#{$fa-css-prefix}-question-circle:before { content: $fa-var-question-circle; }
.#{$fa-css-prefix}-info-circle:before { content: $fa-var-info-circle; }
.#{$fa-css-prefix}-crosshairs:before { content: $fa-var-crosshairs; }
.#{$fa-css-prefix}-times-circle-o:before { content: $fa-var-times-circle-o; }
.#{$fa-css-prefix}-check-circle-o:before { content: $fa-var-check-circle-o; }
.#{$fa-css-prefix}-ban:before { content: $fa-var-ban; }
.#{$fa-css-prefix}-arrow-left:before { content: $fa-var-arrow-left; }
.#{$fa-css-prefix}-arrow-right:before { content: $fa-var-arrow-right; }
.#{$fa-css-prefix}-arrow-up:before { content: $fa-var-arrow-up; }
.#{$fa-css-prefix}-arrow-down:before { content: $fa-var-arrow-down; }
.#{$fa-css-prefix}-mail-forward:before,
.#{$fa-css-prefix}-share:before { content: $fa-var-share; }
.#{$fa-css-prefix}-expand:before { content: $fa-var-expand; }
.#{$fa-css-prefix}-compress:before { content: $fa-var-compress; }
.#{$fa-css-prefix}-plus:before { content: $fa-var-plus; }
.#{$fa-css-prefix}-minus:before { content: $fa-var-minus; }
.#{$fa-css-prefix}-asterisk:before { content: $fa-var-asterisk; }
.#{$fa-css-prefix}-exclamation-circle:before { content: $fa-var-exclamation-circle; }
.#{$fa-css-prefix}-gift:before { content: $fa-var-gift; }
.#{$fa-css-prefix}-leaf:before { content: $fa-var-leaf; }
.#{$fa-css-prefix}-fire:before { content: $fa-var-fire; }
.#{$fa-css-prefix}-eye:before { content: $fa-var-eye; }
.#{$fa-css-prefix}-eye-slash:before { content: $fa-var-eye-slash; }
.#{$fa-css-prefix}-warning:before,
.#{$fa-css-prefix}-exclamation-triangle:before { content: $fa-var-exclamation-triangle; }
.#{$fa-css-prefix}-plane:before { content: $fa-var-plane; }
.#{$fa-css-prefix}-calendar:before { content: $fa-var-calendar; }
.#{$fa-css-prefix}-random:before { content: $fa-var-random; }
.#{$fa-css-prefix}-comment:before { content: $fa-var-comment; }
.#{$fa-css-prefix}-magnet:before { content: $fa-var-magnet; }
.#{$fa-css-prefix}-chevron-up:before { content: $fa-var-chevron-up; }
.#{$fa-css-prefix}-chevron-down:before { content: $fa-var-chevron-down; }
.#{$fa-css-prefix}-retweet:before { content: $fa-var-retweet; }
.#{$fa-css-prefix}-shopping-cart:before { content: $fa-var-shopping-cart; }
.#{$fa-css-prefix}-folder:before { content: $fa-var-folder; }
.#{$fa-css-prefix}-folder-open:before { content: $fa-var-folder-open; }
.#{$fa-css-prefix}-arrows-v:before { content: $fa-var-arrows-v; }
.#{$fa-css-prefix}-arrows-h:before { content: $fa-var-arrows-h; }
.#{$fa-css-prefix}-bar-chart-o:before,
.#{$fa-css-prefix}-bar-chart:before { content: $fa-var-bar-chart; }
.#{$fa-css-prefix}-twitter-square:before { content: $fa-var-twitter-square; }
.#{$fa-css-prefix}-facebook-square:before { content: $fa-var-facebook-square; }
.#{$fa-css-prefix}-camera-retro:before { content: $fa-var-camera-retro; }
.#{$fa-css-prefix}-key:before { content: $fa-var-key; }
.#{$fa-css-prefix}-gears:before,
.#{$fa-css-prefix}-cogs:before { content: $fa-var-cogs; }
.#{$fa-css-prefix}-comments:before { content: $fa-var-comments; }
.#{$fa-css-prefix}-thumbs-o-up:before { content: $fa-var-thumbs-o-up; }
.#{$fa-css-prefix}-thumbs-o-down:before { content: $fa-var-thumbs-o-down; }
.#{$fa-css-prefix}-star-half:before { content: $fa-var-star-half; }
.#{$fa-css-prefix}-heart-o:before { content: $fa-var-heart-o; }
.#{$fa-css-prefix}-sign-out:before { content: $fa-var-sign-out; }
.#{$fa-css-prefix}-linkedin-square:before { content: $fa-var-linkedin-square; }
.#{$fa-css-prefix}-thumb-tack:before { content: $fa-var-thumb-tack; }
.#{$fa-css-prefix}-external-link:before { content: $fa-var-external-link; }
.#{$fa-css-prefix}-sign-in:before { content: $fa-var-sign-in; }
.#{$fa-css-prefix}-trophy:before { content: $fa-var-trophy; }
.#{$fa-css-prefix}-github-square:before { content: $fa-var-github-square; }
.#{$fa-css-prefix}-upload:before { content: $fa-var-upload; }
.#{$fa-css-prefix}-lemon-o:before { content: $fa-var-lemon-o; }
.#{$fa-css-prefix}-phone:before { content: $fa-var-phone; }
.#{$fa-css-prefix}-square-o:before { content: $fa-var-square-o; }
.#{$fa-css-prefix}-bookmark-o:before { content: $fa-var-bookmark-o; }
.#{$fa-css-prefix}-phone-square:before { content: $fa-var-phone-square; }
.#{$fa-css-prefix}-twitter:before { content: $fa-var-twitter; }
.#{$fa-css-prefix}-facebook-f:before,
.#{$fa-css-prefix}-facebook:before { content: $fa-var-facebook; }
.#{$fa-css-prefix}-github:before { content: $fa-var-github; }
.#{$fa-css-prefix}-unlock:before { content: $fa-var-unlock; }
.#{$fa-css-prefix}-credit-card:before { content: $fa-var-credit-card; }
.#{$fa-css-prefix}-rss:before { content: $fa-var-rss; }
.#{$fa-css-prefix}-hdd-o:before { content: $fa-var-hdd-o; }
.#{$fa-css-prefix}-bullhorn:before { content: $fa-var-bullhorn; }
.#{$fa-css-prefix}-bell:before { content: $fa-var-bell; }
.#{$fa-css-prefix}-certificate:before { content: $fa-var-certificate; }
.#{$fa-css-prefix}-hand-o-right:before { content: $fa-var-hand-o-right; }
.#{$fa-css-prefix}-hand-o-left:before { content: $fa-var-hand-o-left; }
.#{$fa-css-prefix}-hand-o-up:before { content: $fa-var-hand-o-up; }
.#{$fa-css-prefix}-hand-o-down:before { content: $fa-var-hand-o-down; }
.#{$fa-css-prefix}-arrow-circle-left:before { content: $fa-var-arrow-circle-left; }
.#{$fa-css-prefix}-arrow-circle-right:before { content: $fa-var-arrow-circle-right; }
.#{$fa-css-prefix}-arrow-circle-up:before { content: $fa-var-arrow-circle-up; }
.#{$fa-css-prefix}-arrow-circle-down:before { content: $fa-var-arrow-circle-down; }
.#{$fa-css-prefix}-globe:before { content: $fa-var-globe; }
.#{$fa-css-prefix}-wrench:before { content: $fa-var-wrench; }
.#{$fa-css-prefix}-tasks:before { content: $fa-var-tasks; }
.#{$fa-css-prefix}-filter:before { content: $fa-var-filter; }
.#{$fa-css-prefix}-briefcase:before { content: $fa-var-briefcase; }
.#{$fa-css-prefix}-arrows-alt:before { content: $fa-var-arrows-alt; }
.#{$fa-css-prefix}-group:before,
.#{$fa-css-prefix}-users:before { content: $fa-var-users; }
.#{$fa-css-prefix}-chain:before,
.#{$fa-css-prefix}-link:before { content: $fa-var-link; }
.#{$fa-css-prefix}-cloud:before { content: $fa-var-cloud; }
.#{$fa-css-prefix}-flask:before { content: $fa-var-flask; }
.#{$fa-css-prefix}-cut:before,
.#{$fa-css-prefix}-scissors:before { content: $fa-var-scissors; }
.#{$fa-css-prefix}-copy:before,
.#{$fa-css-prefix}-files-o:before { content: $fa-var-files-o; }
.#{$fa-css-prefix}-paperclip:before { content: $fa-var-paperclip; }
.#{$fa-css-prefix}-save:before,
.#{$fa-css-prefix}-floppy-o:before { content: $fa-var-floppy-o; }
.#{$fa-css-prefix}-square:before { content: $fa-var-square; }
.#{$fa-css-prefix}-navicon:before,
.#{$fa-css-prefix}-reorder:before,
.#{$fa-css-prefix}-bars:before { content: $fa-var-bars; }
.#{$fa-css-prefix}-list-ul:before { content: $fa-var-list-ul; }
.#{$fa-css-prefix}-list-ol:before { content: $fa-var-list-ol; }
.#{$fa-css-prefix}-strikethrough:before { content: $fa-var-strikethrough; }
.#{$fa-css-prefix}-underline:before { content: $fa-var-underline; }
.#{$fa-css-prefix}-table:before { content: $fa-var-table; }
.#{$fa-css-prefix}-magic:before { content: $fa-var-magic; }
.#{$fa-css-prefix}-truck:before { content: $fa-var-truck; }
.#{$fa-css-prefix}-pinterest:before { content: $fa-var-pinterest; }
.#{$fa-css-prefix}-pinterest-square:before { content: $fa-var-pinterest-square; }
.#{$fa-css-prefix}-google-plus-square:before { content: $fa-var-google-plus-square; }
.#{$fa-css-prefix}-google-plus:before { content: $fa-var-google-plus; }
.#{$fa-css-prefix}-money:before { content: $fa-var-money; }
.#{$fa-css-prefix}-caret-down:before { content: $fa-var-caret-down; }
.#{$fa-css-prefix}-caret-up:before { content: $fa-var-caret-up; }
.#{$fa-css-prefix}-caret-left:before { content: $fa-var-caret-left; }
.#{$fa-css-prefix}-caret-right:before { content: $fa-var-caret-right; }
.#{$fa-css-prefix}-columns:before { content: $fa-var-columns; }
.#{$fa-css-prefix}-unsorted:before,
.#{$fa-css-prefix}-sort:before { content: $fa-var-sort; }
.#{$fa-css-prefix}-sort-down:before,
.#{$fa-css-prefix}-sort-desc:before { content: $fa-var-sort-desc; }
.#{$fa-css-prefix}-sort-up:before,
.#{$fa-css-prefix}-sort-asc:before { content: $fa-var-sort-asc; }
.#{$fa-css-prefix}-envelope:before { content: $fa-var-envelope; }
.#{$fa-css-prefix}-linkedin:before { content: $fa-var-linkedin; }
.#{$fa-css-prefix}-rotate-left:before,
.#{$fa-css-prefix}-undo:before { content: $fa-var-undo; }
.#{$fa-css-prefix}-legal:before,
.#{$fa-css-prefix}-gavel:before { content: $fa-var-gavel; }
.#{$fa-css-prefix}-dashboard:before,
.#{$fa-css-prefix}-tachometer:before { content: $fa-var-tachometer; }
.#{$fa-css-prefix}-comment-o:before { content: $fa-var-comment-o; }
.#{$fa-css-prefix}-comments-o:before { content: $fa-var-comments-o; }
.#{$fa-css-prefix}-flash:before,
.#{$fa-css-prefix}-bolt:before { content: $fa-var-bolt; }
.#{$fa-css-prefix}-sitemap:before { content: $fa-var-sitemap; }
.#{$fa-css-prefix}-umbrella:before { content: $fa-var-umbrella; }
.#{$fa-css-prefix}-paste:before,
.#{$fa-css-prefix}-clipboard:before { content: $fa-var-clipboard; }
.#{$fa-css-prefix}-lightbulb-o:before { content: $fa-var-lightbulb-o; }
.#{$fa-css-prefix}-exchange:before { content: $fa-var-exchange; }
.#{$fa-css-prefix}-cloud-download:before { content: $fa-var-cloud-download; }
.#{$fa-css-prefix}-cloud-upload:before { content: $fa-var-cloud-upload; }
.#{$fa-css-prefix}-user-md:before { content: $fa-var-user-md; }
.#{$fa-css-prefix}-stethoscope:before { content: $fa-var-stethoscope; }
.#{$fa-css-prefix}-suitcase:before { content: $fa-var-suitcase; }
.#{$fa-css-prefix}-bell-o:before { content: $fa-var-bell-o; }
.#{$fa-css-prefix}-coffee:before { content: $fa-var-coffee; }
.#{$fa-css-prefix}-cutlery:before { content: $fa-var-cutlery; }
.#{$fa-css-prefix}-file-text-o:before { content: $fa-var-file-text-o; }
.#{$fa-css-prefix}-building-o:before { content: $fa-var-building-o; }
.#{$fa-css-prefix}-hospital-o:before { content: $fa-var-hospital-o; }
.#{$fa-css-prefix}-ambulance:before { content: $fa-var-ambulance; }
.#{$fa-css-prefix}-medkit:before { content: $fa-var-medkit; }
.#{$fa-css-prefix}-fighter-jet:before { content: $fa-var-fighter-jet; }
.#{$fa-css-prefix}-beer:before { content: $fa-var-beer; }
.#{$fa-css-prefix}-h-square:before { content: $fa-var-h-square; }
.#{$fa-css-prefix}-plus-square:before { content: $fa-var-plus-square; }
.#{$fa-css-prefix}-angle-double-left:before { content: $fa-var-angle-double-left; }
.#{$fa-css-prefix}-angle-double-right:before { content: $fa-var-angle-double-right; }
.#{$fa-css-prefix}-angle-double-up:before { content: $fa-var-angle-double-up; }
.#{$fa-css-prefix}-angle-double-down:before { content: $fa-var-angle-double-down; }
.#{$fa-css-prefix}-angle-left:before { content: $fa-var-angle-left; }
.#{$fa-css-prefix}-angle-right:before { content: $fa-var-angle-right; }
.#{$fa-css-prefix}-angle-up:before { content: $fa-var-angle-up; }
.#{$fa-css-prefix}-angle-down:before { content: $fa-var-angle-down; }
.#{$fa-css-prefix}-desktop:before { content: $fa-var-desktop; }
.#{$fa-css-prefix}-laptop:before { content: $fa-var-laptop; }
.#{$fa-css-prefix}-tablet:before { content: $fa-var-tablet; }
.#{$fa-css-prefix}-mobile-phone:before,
.#{$fa-css-prefix}-mobile:before { content: $fa-var-mobile; }
.#{$fa-css-prefix}-circle-o:before { content: $fa-var-circle-o; }
.#{$fa-css-prefix}-quote-left:before { content: $fa-var-quote-left; }
.#{$fa-css-prefix}-quote-right:before { content: $fa-var-quote-right; }
.#{$fa-css-prefix}-spinner:before { content: $fa-var-spinner; }
.#{$fa-css-prefix}-circle:before { content: $fa-var-circle; }
.#{$fa-css-prefix}-mail-reply:before,
.#{$fa-css-prefix}-reply:before { content: $fa-var-reply; }
.#{$fa-css-prefix}-github-alt:before { content: $fa-var-github-alt; }
.#{$fa-css-prefix}-folder-o:before { content: $fa-var-folder-o; }
.#{$fa-css-prefix}-folder-open-o:before { content: $fa-var-folder-open-o; }
.#{$fa-css-prefix}-smile-o:before { content: $fa-var-smile-o; }
.#{$fa-css-prefix}-frown-o:before { content: $fa-var-frown-o; }
.#{$fa-css-prefix}-meh-o:before { content: $fa-var-meh-o; }
.#{$fa-css-prefix}-gamepad:before { content: $fa-var-gamepad; }
.#{$fa-css-prefix}-keyboard-o:before { content: $fa-var-keyboard-o; }
.#{$fa-css-prefix}-flag-o:before { content: $fa-var-flag-o; }
.#{$fa-css-prefix}-flag-checkered:before { content: $fa-var-flag-checkered; }
.#{$fa-css-prefix}-terminal:before { content: $fa-var-terminal; }
.#{$fa-css-prefix}-code:before { content: $fa-var-code; }
.#{$fa-css-prefix}-mail-reply-all:before,
.#{$fa-css-prefix}-reply-all:before { content: $fa-var-reply-all; }
.#{$fa-css-prefix}-star-half-empty:before,
.#{$fa-css-prefix}-star-half-full:before,
.#{$fa-css-prefix}-star-half-o:before { content: $fa-var-star-half-o; }
.#{$fa-css-prefix}-location-arrow:before { content: $fa-var-location-arrow; }
.#{$fa-css-prefix}-crop:before { content: $fa-var-crop; }
.#{$fa-css-prefix}-code-fork:before { content: $fa-var-code-fork; }
.#{$fa-css-prefix}-unlink:before,
.#{$fa-css-prefix}-chain-broken:before { content: $fa-var-chain-broken; }
.#{$fa-css-prefix}-question:before { content: $fa-var-question; }
.#{$fa-css-prefix}-info:before { content: $fa-var-info; }
.#{$fa-css-prefix}-exclamation:before { content: $fa-var-exclamation; }
.#{$fa-css-prefix}-superscript:before { content: $fa-var-superscript; }
.#{$fa-css-prefix}-subscript:before { content: $fa-var-subscript; }
.#{$fa-css-prefix}-eraser:before { content: $fa-var-eraser; }
.#{$fa-css-prefix}-puzzle-piece:before { content: $fa-var-puzzle-piece; }
.#{$fa-css-prefix}-microphone:before { content: $fa-var-microphone; }
.#{$fa-css-prefix}-microphone-slash:before { content: $fa-var-microphone-slash; }
.#{$fa-css-prefix}-shield:before { content: $fa-var-shield; }
.#{$fa-css-prefix}-calendar-o:before { content: $fa-var-calendar-o; }
.#{$fa-css-prefix}-fire-extinguisher:before { content: $fa-var-fire-extinguisher; }
.#{$fa-css-prefix}-rocket:before { content: $fa-var-rocket; }
.#{$fa-css-prefix}-maxcdn:before { content: $fa-var-maxcdn; }
.#{$fa-css-prefix}-chevron-circle-left:before { content: $fa-var-chevron-circle-left; }
.#{$fa-css-prefix}-chevron-circle-right:before { content: $fa-var-chevron-circle-right; }
.#{$fa-css-prefix}-chevron-circle-up:before { content: $fa-var-chevron-circle-up; }
.#{$fa-css-prefix}-chevron-circle-down:before { content: $fa-var-chevron-circle-down; }
.#{$fa-css-prefix}-html5:before { content: $fa-var-html5; }
.#{$fa-css-prefix}-css3:before { content: $fa-var-css3; }
.#{$fa-css-prefix}-anchor:before { content: $fa-var-anchor; }
.#{$fa-css-prefix}-unlock-alt:before { content: $fa-var-unlock-alt; }
.#{$fa-css-prefix}-bullseye:before { content: $fa-var-bullseye; }
.#{$fa-css-prefix}-ellipsis-h:before { content: $fa-var-ellipsis-h; }
.#{$fa-css-prefix}-ellipsis-v:before { content: $fa-var-ellipsis-v; }
.#{$fa-css-prefix}-rss-square:before { content: $fa-var-rss-square; }
.#{$fa-css-prefix}-play-circle:before { content: $fa-var-play-circle; }
.#{$fa-css-prefix}-ticket:before { content: $fa-var-ticket; }
.#{$fa-css-prefix}-minus-square:before { content: $fa-var-minus-square; }
.#{$fa-css-prefix}-minus-square-o:before { content: $fa-var-minus-square-o; }
.#{$fa-css-prefix}-level-up:before { content: $fa-var-level-up; }
.#{$fa-css-prefix}-level-down:before { content: $fa-var-level-down; }
.#{$fa-css-prefix}-check-square:before { content: $fa-var-check-square; }
.#{$fa-css-prefix}-pencil-square:before { content: $fa-var-pencil-square; }
.#{$fa-css-prefix}-external-link-square:before { content: $fa-var-external-link-square; }
.#{$fa-css-prefix}-share-square:before { content: $fa-var-share-square; }
.#{$fa-css-prefix}-compass:before { content: $fa-var-compass; }
.#{$fa-css-prefix}-toggle-down:before,
.#{$fa-css-prefix}-caret-square-o-down:before { content: $fa-var-caret-square-o-down; }
.#{$fa-css-prefix}-toggle-up:before,
.#{$fa-css-prefix}-caret-square-o-up:before { content: $fa-var-caret-square-o-up; }
.#{$fa-css-prefix}-toggle-right:before,
.#{$fa-css-prefix}-caret-square-o-right:before { content: $fa-var-caret-square-o-right; }
.#{$fa-css-prefix}-euro:before,
.#{$fa-css-prefix}-eur:before { content: $fa-var-eur; }
.#{$fa-css-prefix}-gbp:before { content: $fa-var-gbp; }
.#{$fa-css-prefix}-dollar:before,
.#{$fa-css-prefix}-usd:before { content: $fa-var-usd; }
.#{$fa-css-prefix}-rupee:before,
.#{$fa-css-prefix}-inr:before { content: $fa-var-inr; }
.#{$fa-css-prefix}-cny:before,
.#{$fa-css-prefix}-rmb:before,
.#{$fa-css-prefix}-yen:before,
.#{$fa-css-prefix}-jpy:before { content: $fa-var-jpy; }
.#{$fa-css-prefix}-ruble:before,
.#{$fa-css-prefix}-rouble:before,
.#{$fa-css-prefix}-rub:before { content: $fa-var-rub; }
.#{$fa-css-prefix}-won:before,
.#{$fa-css-prefix}-krw:before { content: $fa-var-krw; }
.#{$fa-css-prefix}-bitcoin:before,
.#{$fa-css-prefix}-btc:before { content: $fa-var-btc; }
.#{$fa-css-prefix}-file:before { content: $fa-var-file; }
.#{$fa-css-prefix}-file-text:before { content: $fa-var-file-text; }
.#{$fa-css-prefix}-sort-alpha-asc:before { content: $fa-var-sort-alpha-asc; }
.#{$fa-css-prefix}-sort-alpha-desc:before { content: $fa-var-sort-alpha-desc; }
.#{$fa-css-prefix}-sort-amount-asc:before { content: $fa-var-sort-amount-asc; }
.#{$fa-css-prefix}-sort-amount-desc:before { content: $fa-var-sort-amount-desc; }
.#{$fa-css-prefix}-sort-numeric-asc:before { content: $fa-var-sort-numeric-asc; }
.#{$fa-css-prefix}-sort-numeric-desc:before { content: $fa-var-sort-numeric-desc; }
.#{$fa-css-prefix}-thumbs-up:before { content: $fa-var-thumbs-up; }
.#{$fa-css-prefix}-thumbs-down:before { content: $fa-var-thumbs-down; }
.#{$fa-css-prefix}-youtube-square:before { content: $fa-var-youtube-square; }
.#{$fa-css-prefix}-youtube:before { content: $fa-var-youtube; }
.#{$fa-css-prefix}-xing:before { content: $fa-var-xing; }
.#{$fa-css-prefix}-xing-square:before { content: $fa-var-xing-square; }
.#{$fa-css-prefix}-youtube-play:before { content: $fa-var-youtube-play; }
.#{$fa-css-prefix}-dropbox:before { content: $fa-var-dropbox; }
.#{$fa-css-prefix}-stack-overflow:before { content: $fa-var-stack-overflow; }
.#{$fa-css-prefix}-instagram:before { content: $fa-var-instagram; }
.#{$fa-css-prefix}-flickr:before { content: $fa-var-flickr; }
.#{$fa-css-prefix}-adn:before { content: $fa-var-adn; }
.#{$fa-css-prefix}-bitbucket:before { content: $fa-var-bitbucket; }
.#{$fa-css-prefix}-bitbucket-square:before { content: $fa-var-bitbucket-square; }
.#{$fa-css-prefix}-tumblr:before { content: $fa-var-tumblr; }
.#{$fa-css-prefix}-tumblr-square:before { content: $fa-var-tumblr-square; }
.#{$fa-css-prefix}-long-arrow-down:before { content: $fa-var-long-arrow-down; }
.#{$fa-css-prefix}-long-arrow-up:before { content: $fa-var-long-arrow-up; }
.#{$fa-css-prefix}-long-arrow-left:before { content: $fa-var-long-arrow-left; }
.#{$fa-css-prefix}-long-arrow-right:before { content: $fa-var-long-arrow-right; }
.#{$fa-css-prefix}-apple:before { content: $fa-var-apple; }
.#{$fa-css-prefix}-windows:before { content: $fa-var-windows; }
.#{$fa-css-prefix}-android:before { content: $fa-var-android; }
.#{$fa-css-prefix}-linux:before { content: $fa-var-linux; }
.#{$fa-css-prefix}-dribbble:before { content: $fa-var-dribbble; }
.#{$fa-css-prefix}-skype:before { content: $fa-var-skype; }
.#{$fa-css-prefix}-foursquare:before { content: $fa-var-foursquare; }
.#{$fa-css-prefix}-trello:before { content: $fa-var-trello; }
.#{$fa-css-prefix}-female:before { content: $fa-var-female; }
.#{$fa-css-prefix}-male:before { content: $fa-var-male; }
.#{$fa-css-prefix}-gittip:before,
.#{$fa-css-prefix}-gratipay:before { content: $fa-var-gratipay; }
.#{$fa-css-prefix}-sun-o:before { content: $fa-var-sun-o; }
.#{$fa-css-prefix}-moon-o:before { content: $fa-var-moon-o; }
.#{$fa-css-prefix}-archive:before { content: $fa-var-archive; }
.#{$fa-css-prefix}-bug:before { content: $fa-var-bug; }
.#{$fa-css-prefix}-vk:before { content: $fa-var-vk; }
.#{$fa-css-prefix}-weibo:before { content: $fa-var-weibo; }
.#{$fa-css-prefix}-renren:before { content: $fa-var-renren; }
.#{$fa-css-prefix}-pagelines:before { content: $fa-var-pagelines; }
.#{$fa-css-prefix}-stack-exchange:before { content: $fa-var-stack-exchange; }
.#{$fa-css-prefix}-arrow-circle-o-right:before { content: $fa-var-arrow-circle-o-right; }
.#{$fa-css-prefix}-arrow-circle-o-left:before { content: $fa-var-arrow-circle-o-left; }
.#{$fa-css-prefix}-toggle-left:before,
.#{$fa-css-prefix}-caret-square-o-left:before { content: $fa-var-caret-square-o-left; }
.#{$fa-css-prefix}-dot-circle-o:before { content: $fa-var-dot-circle-o; }
.#{$fa-css-prefix}-wheelchair:before { content: $fa-var-wheelchair; }
.#{$fa-css-prefix}-vimeo-square:before { content: $fa-var-vimeo-square; }
.#{$fa-css-prefix}-turkish-lira:before,
.#{$fa-css-prefix}-try:before { content: $fa-var-try; }
.#{$fa-css-prefix}-plus-square-o:before { content: $fa-var-plus-square-o; }
.#{$fa-css-prefix}-space-shuttle:before { content: $fa-var-space-shuttle; }
.#{$fa-css-prefix}-slack:before { content: $fa-var-slack; }
.#{$fa-css-prefix}-envelope-square:before { content: $fa-var-envelope-square; }
.#{$fa-css-prefix}-wordpress:before { content: $fa-var-wordpress; }
.#{$fa-css-prefix}-openid:before { content: $fa-var-openid; }
.#{$fa-css-prefix}-institution:before,
.#{$fa-css-prefix}-bank:before,
.#{$fa-css-prefix}-university:before { content: $fa-var-university; }
.#{$fa-css-prefix}-mortar-board:before,
.#{$fa-css-prefix}-graduation-cap:before { content: $fa-var-graduation-cap; }
.#{$fa-css-prefix}-yahoo:before { content: $fa-var-yahoo; }
.#{$fa-css-prefix}-google:before { content: $fa-var-google; }
.#{$fa-css-prefix}-reddit:before { content: $fa-var-reddit; }
.#{$fa-css-prefix}-reddit-square:before { content: $fa-var-reddit-square; }
.#{$fa-css-prefix}-stumbleupon-circle:before { content: $fa-var-stumbleupon-circle; }
.#{$fa-css-prefix}-stumbleupon:before { content: $fa-var-stumbleupon; }
.#{$fa-css-prefix}-delicious:before { content: $fa-var-delicious; }
.#{$fa-css-prefix}-digg:before { content: $fa-var-digg; }
.#{$fa-css-prefix}-pied-piper:before { content: $fa-var-pied-piper; }
.#{$fa-css-prefix}-pied-piper-alt:before { content: $fa-var-pied-piper-alt; }
.#{$fa-css-prefix}-drupal:before { content: $fa-var-drupal; }
.#{$fa-css-prefix}-joomla:before { content: $fa-var-joomla; }
.#{$fa-css-prefix}-language:before { content: $fa-var-language; }
.#{$fa-css-prefix}-fax:before { content: $fa-var-fax; }
.#{$fa-css-prefix}-building:before { content: $fa-var-building; }
.#{$fa-css-prefix}-child:before { content: $fa-var-child; }
.#{$fa-css-prefix}-paw:before { content: $fa-var-paw; }
.#{$fa-css-prefix}-spoon:before { content: $fa-var-spoon; }
.#{$fa-css-prefix}-cube:before { content: $fa-var-cube; }
.#{$fa-css-prefix}-cubes:before { content: $fa-var-cubes; }
.#{$fa-css-prefix}-behance:before { content: $fa-var-behance; }
.#{$fa-css-prefix}-behance-square:before { content: $fa-var-behance-square; }
.#{$fa-css-prefix}-steam:before { content: $fa-var-steam; }
.#{$fa-css-prefix}-steam-square:before { content: $fa-var-steam-square; }
.#{$fa-css-prefix}-recycle:before { content: $fa-var-recycle; }
.#{$fa-css-prefix}-automobile:before,
.#{$fa-css-prefix}-car:before { content: $fa-var-car; }
.#{$fa-css-prefix}-cab:before,
.#{$fa-css-prefix}-taxi:before { content: $fa-var-taxi; }
.#{$fa-css-prefix}-tree:before { content: $fa-var-tree; }
.#{$fa-css-prefix}-spotify:before { content: $fa-var-spotify; }
.#{$fa-css-prefix}-deviantart:before { content: $fa-var-deviantart; }
.#{$fa-css-prefix}-soundcloud:before { content: $fa-var-soundcloud; }
.#{$fa-css-prefix}-database:before { content: $fa-var-database; }
.#{$fa-css-prefix}-file-pdf-o:before { content: $fa-var-file-pdf-o; }
.#{$fa-css-prefix}-file-word-o:before { content: $fa-var-file-word-o; }
.#{$fa-css-prefix}-file-excel-o:before { content: $fa-var-file-excel-o; }
.#{$fa-css-prefix}-file-powerpoint-o:before { content: $fa-var-file-powerpoint-o; }
.#{$fa-css-prefix}-file-photo-o:before,
.#{$fa-css-prefix}-file-picture-o:before,
.#{$fa-css-prefix}-file-image-o:before { content: $fa-var-file-image-o; }
.#{$fa-css-prefix}-file-zip-o:before,
.#{$fa-css-prefix}-file-archive-o:before { content: $fa-var-file-archive-o; }
.#{$fa-css-prefix}-file-sound-o:before,
.#{$fa-css-prefix}-file-audio-o:before { content: $fa-var-file-audio-o; }
.#{$fa-css-prefix}-file-movie-o:before,
.#{$fa-css-prefix}-file-video-o:before { content: $fa-var-file-video-o; }
.#{$fa-css-prefix}-file-code-o:before { content: $fa-var-file-code-o; }
.#{$fa-css-prefix}-vine:before { content: $fa-var-vine; }
.#{$fa-css-prefix}-codepen:before { content: $fa-var-codepen; }
.#{$fa-css-prefix}-jsfiddle:before { content: $fa-var-jsfiddle; }
.#{$fa-css-prefix}-life-bouy:before,
.#{$fa-css-prefix}-life-buoy:before,
.#{$fa-css-prefix}-life-saver:before,
.#{$fa-css-prefix}-support:before,
.#{$fa-css-prefix}-life-ring:before { content: $fa-var-life-ring; }
.#{$fa-css-prefix}-circle-o-notch:before { content: $fa-var-circle-o-notch; }
.#{$fa-css-prefix}-ra:before,
.#{$fa-css-prefix}-rebel:before { content: $fa-var-rebel; }
.#{$fa-css-prefix}-ge:before,
.#{$fa-css-prefix}-empire:before { content: $fa-var-empire; }
.#{$fa-css-prefix}-git-square:before { content: $fa-var-git-square; }
.#{$fa-css-prefix}-git:before { content: $fa-var-git; }
.#{$fa-css-prefix}-hacker-news:before { content: $fa-var-hacker-news; }
.#{$fa-css-prefix}-tencent-weibo:before { content: $fa-var-tencent-weibo; }
.#{$fa-css-prefix}-qq:before { content: $fa-var-qq; }
.#{$fa-css-prefix}-wechat:before,
.#{$fa-css-prefix}-weixin:before { content: $fa-var-weixin; }
.#{$fa-css-prefix}-send:before,
.#{$fa-css-prefix}-paper-plane:before { content: $fa-var-paper-plane; }
.#{$fa-css-prefix}-send-o:before,
.#{$fa-css-prefix}-paper-plane-o:before { content: $fa-var-paper-plane-o; }
.#{$fa-css-prefix}-history:before { content: $fa-var-history; }
.#{$fa-css-prefix}-genderless:before,
.#{$fa-css-prefix}-circle-thin:before { content: $fa-var-circle-thin; }
.#{$fa-css-prefix}-header:before { content: $fa-var-header; }
.#{$fa-css-prefix}-paragraph:before { content: $fa-var-paragraph; }
.#{$fa-css-prefix}-sliders:before { content: $fa-var-sliders; }
.#{$fa-css-prefix}-share-alt:before { content: $fa-var-share-alt; }
.#{$fa-css-prefix}-share-alt-square:before { content: $fa-var-share-alt-square; }
.#{$fa-css-prefix}-bomb:before { content: $fa-var-bomb; }
.#{$fa-css-prefix}-soccer-ball-o:before,
.#{$fa-css-prefix}-futbol-o:before { content: $fa-var-futbol-o; }
.#{$fa-css-prefix}-tty:before { content: $fa-var-tty; }
.#{$fa-css-prefix}-binoculars:before { content: $fa-var-binoculars; }
.#{$fa-css-prefix}-plug:before { content: $fa-var-plug; }
.#{$fa-css-prefix}-slideshare:before { content: $fa-var-slideshare; }
.#{$fa-css-prefix}-twitch:before { content: $fa-var-twitch; }
.#{$fa-css-prefix}-yelp:before { content: $fa-var-yelp; }
.#{$fa-css-prefix}-newspaper-o:before { content: $fa-var-newspaper-o; }
.#{$fa-css-prefix}-wifi:before { content: $fa-var-wifi; }
.#{$fa-css-prefix}-calculator:before { content: $fa-var-calculator; }
.#{$fa-css-prefix}-paypal:before { content: $fa-var-paypal; }
.#{$fa-css-prefix}-google-wallet:before { content: $fa-var-google-wallet; }
.#{$fa-css-prefix}-cc-visa:before { content: $fa-var-cc-visa; }
.#{$fa-css-prefix}-cc-mastercard:before { content: $fa-var-cc-mastercard; }
.#{$fa-css-prefix}-cc-discover:before { content: $fa-var-cc-discover; }
.#{$fa-css-prefix}-cc-amex:before { content: $fa-var-cc-amex; }
.#{$fa-css-prefix}-cc-paypal:before { content: $fa-var-cc-paypal; }
.#{$fa-css-prefix}-cc-stripe:before { content: $fa-var-cc-stripe; }
.#{$fa-css-prefix}-bell-slash:before { content: $fa-var-bell-slash; }
.#{$fa-css-prefix}-bell-slash-o:before { content: $fa-var-bell-slash-o; }
.#{$fa-css-prefix}-trash:before { content: $fa-var-trash; }
.#{$fa-css-prefix}-copyright:before { content: $fa-var-copyright; }
.#{$fa-css-prefix}-at:before { content: $fa-var-at; }
.#{$fa-css-prefix}-eyedropper:before { content: $fa-var-eyedropper; }
.#{$fa-css-prefix}-paint-brush:before { content: $fa-var-paint-brush; }
.#{$fa-css-prefix}-birthday-cake:before { content: $fa-var-birthday-cake; }
.#{$fa-css-prefix}-area-chart:before { content: $fa-var-area-chart; }
.#{$fa-css-prefix}-pie-chart:before { content: $fa-var-pie-chart; }
.#{$fa-css-prefix}-line-chart:before { content: $fa-var-line-chart; }
.#{$fa-css-prefix}-lastfm:before { content: $fa-var-lastfm; }
.#{$fa-css-prefix}-lastfm-square:before { content: $fa-var-lastfm-square; }
.#{$fa-css-prefix}-toggle-off:before { content: $fa-var-toggle-off; }
.#{$fa-css-prefix}-toggle-on:before { content: $fa-var-toggle-on; }
.#{$fa-css-prefix}-bicycle:before { content: $fa-var-bicycle; }
.#{$fa-css-prefix}-bus:before { content: $fa-var-bus; }
.#{$fa-css-prefix}-ioxhost:before { content: $fa-var-ioxhost; }
.#{$fa-css-prefix}-angellist:before { content: $fa-var-angellist; }
.#{$fa-css-prefix}-cc:before { content: $fa-var-cc; }
.#{$fa-css-prefix}-shekel:before,
.#{$fa-css-prefix}-sheqel:before,
.#{$fa-css-prefix}-ils:before { content: $fa-var-ils; }
.#{$fa-css-prefix}-meanpath:before { content: $fa-var-meanpath; }
.#{$fa-css-prefix}-buysellads:before { content: $fa-var-buysellads; }
.#{$fa-css-prefix}-connectdevelop:before { content: $fa-var-connectdevelop; }
.#{$fa-css-prefix}-dashcube:before { content: $fa-var-dashcube; }
.#{$fa-css-prefix}-forumbee:before { content: $fa-var-forumbee; }
.#{$fa-css-prefix}-leanpub:before { content: $fa-var-leanpub; }
.#{$fa-css-prefix}-sellsy:before { content: $fa-var-sellsy; }
.#{$fa-css-prefix}-shirtsinbulk:before { content: $fa-var-shirtsinbulk; }
.#{$fa-css-prefix}-simplybuilt:before { content: $fa-var-simplybuilt; }
.#{$fa-css-prefix}-skyatlas:before { content: $fa-var-skyatlas; }
.#{$fa-css-prefix}-cart-plus:before { content: $fa-var-cart-plus; }
.#{$fa-css-prefix}-cart-arrow-down:before { content: $fa-var-cart-arrow-down; }
.#{$fa-css-prefix}-diamond:before { content: $fa-var-diamond; }
.#{$fa-css-prefix}-ship:before { content: $fa-var-ship; }
.#{$fa-css-prefix}-user-secret:before { content: $fa-var-user-secret; }
.#{$fa-css-prefix}-motorcycle:before { content: $fa-var-motorcycle; }
.#{$fa-css-prefix}-street-view:before { content: $fa-var-street-view; }
.#{$fa-css-prefix}-heartbeat:before { content: $fa-var-heartbeat; }
.#{$fa-css-prefix}-venus:before { content: $fa-var-venus; }
.#{$fa-css-prefix}-mars:before { content: $fa-var-mars; }
.#{$fa-css-prefix}-mercury:before { content: $fa-var-mercury; }
.#{$fa-css-prefix}-transgender:before { content: $fa-var-transgender; }
.#{$fa-css-prefix}-transgender-alt:before { content: $fa-var-transgender-alt; }
.#{$fa-css-prefix}-venus-double:before { content: $fa-var-venus-double; }
.#{$fa-css-prefix}-mars-double:before { content: $fa-var-mars-double; }
.#{$fa-css-prefix}-venus-mars:before { content: $fa-var-venus-mars; }
.#{$fa-css-prefix}-mars-stroke:before { content: $fa-var-mars-stroke; }
.#{$fa-css-prefix}-mars-stroke-v:before { content: $fa-var-mars-stroke-v; }
.#{$fa-css-prefix}-mars-stroke-h:before { content: $fa-var-mars-stroke-h; }
.#{$fa-css-prefix}-neuter:before { content: $fa-var-neuter; }
.#{$fa-css-prefix}-facebook-official:before { content: $fa-var-facebook-official; }
.#{$fa-css-prefix}-pinterest-p:before { content: $fa-var-pinterest-p; }
.#{$fa-css-prefix}-whatsapp:before { content: $fa-var-whatsapp; }
.#{$fa-css-prefix}-server:before { content: $fa-var-server; }
.#{$fa-css-prefix}-user-plus:before { content: $fa-var-user-plus; }
.#{$fa-css-prefix}-user-times:before { content: $fa-var-user-times; }
.#{$fa-css-prefix}-hotel:before,
.#{$fa-css-prefix}-bed:before { content: $fa-var-bed; }
.#{$fa-css-prefix}-viacoin:before { content: $fa-var-viacoin; }
.#{$fa-css-prefix}-train:before { content: $fa-var-train; }
.#{$fa-css-prefix}-subway:before { content: $fa-var-subway; }
.#{$fa-css-prefix}-medium:before { content: $fa-var-medium; }


File: /font-awesome\scss\_larger.scss
// Icon Sizes
// -------------------------

/* makes the font 33% larger relative to the icon container */
.#{$fa-css-prefix}-lg {
  font-size: (4em / 3);
  line-height: (3em / 4);
  vertical-align: -15%;
}
.#{$fa-css-prefix}-2x { font-size: 2em; }
.#{$fa-css-prefix}-3x { font-size: 3em; }
.#{$fa-css-prefix}-4x { font-size: 4em; }
.#{$fa-css-prefix}-5x { font-size: 5em; }


File: /font-awesome\scss\_list.scss
// List Icons
// -------------------------

.#{$fa-css-prefix}-ul {
  padding-left: 0;
  margin-left: $fa-li-width;
  list-style-type: none;
  > li { position: relative; }
}
.#{$fa-css-prefix}-li {
  position: absolute;
  left: -$fa-li-width;
  width: $fa-li-width;
  top: (2em / 14);
  text-align: center;
  &.#{$fa-css-prefix}-lg {
    left: -$fa-li-width + (4em / 14);
  }
}


File: /font-awesome\scss\_mixins.scss
// Mixins
// --------------------------

@mixin fa-icon() {
  display: inline-block;
  font: normal normal normal #{$fa-font-size-base}/1 FontAwesome; // shortening font declaration
  font-size: inherit; // can't have font-size inherit on line above, so need to override
  text-rendering: auto; // optimizelegibility throws things off #1094
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  transform: translate(0, 0); // ensures no half-pixel rendering in firefox

}

@mixin fa-icon-rotate($degrees, $rotation) {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=#{$rotation});
  -webkit-transform: rotate($degrees);
      -ms-transform: rotate($degrees);
          transform: rotate($degrees);
}

@mixin fa-icon-flip($horiz, $vert, $rotation) {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=#{$rotation});
  -webkit-transform: scale($horiz, $vert);
      -ms-transform: scale($horiz, $vert);
          transform: scale($horiz, $vert);
}


File: /font-awesome\scss\_path.scss
/* FONT PATH
 * -------------------------- */

@font-face {
  font-family: 'FontAwesome';
  src: url('#{$fa-font-path}/fontawesome-webfont.eot?v=#{$fa-version}');
  src: url('#{$fa-font-path}/fontawesome-webfont.eot?#iefix&v=#{$fa-version}') format('embedded-opentype'),
    url('#{$fa-font-path}/fontawesome-webfont.woff2?v=#{$fa-version}') format('woff2'),
    url('#{$fa-font-path}/fontawesome-webfont.woff?v=#{$fa-version}') format('woff'),
    url('#{$fa-font-path}/fontawesome-webfont.ttf?v=#{$fa-version}') format('truetype'),
    url('#{$fa-font-path}/fontawesome-webfont.svg?v=#{$fa-version}#fontawesomeregular') format('svg');
//  src: url('#{$fa-font-path}/FontAwesome.otf') format('opentype'); // used when developing fonts
  font-weight: normal;
  font-style: normal;
}


File: /font-awesome\scss\_rotated-flipped.scss
// Rotated & Flipped Icons
// -------------------------

.#{$fa-css-prefix}-rotate-90  { @include fa-icon-rotate(90deg, 1);  }
.#{$fa-css-prefix}-rotate-180 { @include fa-icon-rotate(180deg, 2); }
.#{$fa-css-prefix}-rotate-270 { @include fa-icon-rotate(270deg, 3); }

.#{$fa-css-prefix}-flip-horizontal { @include fa-icon-flip(-1, 1, 0); }
.#{$fa-css-prefix}-flip-vertical   { @include fa-icon-flip(1, -1, 2); }

// Hook for IE8-9
// -------------------------

:root .#{$fa-css-prefix}-rotate-90,
:root .#{$fa-css-prefix}-rotate-180,
:root .#{$fa-css-prefix}-rotate-270,
:root .#{$fa-css-prefix}-flip-horizontal,
:root .#{$fa-css-prefix}-flip-vertical {
  filter: none;
}


File: /font-awesome\scss\_stacked.scss
// Stacked Icons
// -------------------------

.#{$fa-css-prefix}-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.#{$fa-css-prefix}-stack-1x, .#{$fa-css-prefix}-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.#{$fa-css-prefix}-stack-1x { line-height: inherit; }
.#{$fa-css-prefix}-stack-2x { font-size: 2em; }
.#{$fa-css-prefix}-inverse { color: $fa-inverse; }


File: /font-awesome\scss\_variables.scss
// Variables
// --------------------------

$fa-font-path:        "../fonts" !default;
$fa-font-size-base:   14px !default;
//$fa-font-path:        "//netdna.bootstrapcdn.com/font-awesome/4.3.0/fonts" !default; // for referencing Bootstrap CDN font files directly
$fa-css-prefix:       fa !default;
$fa-version:          "4.3.0" !default;
$fa-border-color:     #eee !default;
$fa-inverse:          #fff !default;
$fa-li-width:         (30em / 14) !default;

$fa-var-adjust: "\f042";
$fa-var-adn: "\f170";
$fa-var-align-center: "\f037";
$fa-var-align-justify: "\f039";
$fa-var-align-left: "\f036";
$fa-var-align-right: "\f038";
$fa-var-ambulance: "\f0f9";
$fa-var-anchor: "\f13d";
$fa-var-android: "\f17b";
$fa-var-angellist: "\f209";
$fa-var-angle-double-down: "\f103";
$fa-var-angle-double-left: "\f100";
$fa-var-angle-double-right: "\f101";
$fa-var-angle-double-up: "\f102";
$fa-var-angle-down: "\f107";
$fa-var-angle-left: "\f104";
$fa-var-angle-right: "\f105";
$fa-var-angle-up: "\f106";
$fa-var-apple: "\f179";
$fa-var-archive: "\f187";
$fa-var-area-chart: "\f1fe";
$fa-var-arrow-circle-down: "\f0ab";
$fa-var-arrow-circle-left: "\f0a8";
$fa-var-arrow-circle-o-down: "\f01a";
$fa-var-arrow-circle-o-left: "\f190";
$fa-var-arrow-circle-o-right: "\f18e";
$fa-var-arrow-circle-o-up: "\f01b";
$fa-var-arrow-circle-right: "\f0a9";
$fa-var-arrow-circle-up: "\f0aa";
$fa-var-arrow-down: "\f063";
$fa-var-arrow-left: "\f060";
$fa-var-arrow-right: "\f061";
$fa-var-arrow-up: "\f062";
$fa-var-arrows: "\f047";
$fa-var-arrows-alt: "\f0b2";
$fa-var-arrows-h: "\f07e";
$fa-var-arrows-v: "\f07d";
$fa-var-asterisk: "\f069";
$fa-var-at: "\f1fa";
$fa-var-automobile: "\f1b9";
$fa-var-backward: "\f04a";
$fa-var-ban: "\f05e";
$fa-var-bank: "\f19c";
$fa-var-bar-chart: "\f080";
$fa-var-bar-chart-o: "\f080";
$fa-var-barcode: "\f02a";
$fa-var-bars: "\f0c9";
$fa-var-bed: "\f236";
$fa-var-beer: "\f0fc";
$fa-var-behance: "\f1b4";
$fa-var-behance-square: "\f1b5";
$fa-var-bell: "\f0f3";
$fa-var-bell-o: "\f0a2";
$fa-var-bell-slash: "\f1f6";
$fa-var-bell-slash-o: "\f1f7";
$fa-var-bicycle: "\f206";
$fa-var-binoculars: "\f1e5";
$fa-var-birthday-cake: "\f1fd";
$fa-var-bitbucket: "\f171";
$fa-var-bitbucket-square: "\f172";
$fa-var-bitcoin: "\f15a";
$fa-var-bold: "\f032";
$fa-var-bolt: "\f0e7";
$fa-var-bomb: "\f1e2";
$fa-var-book: "\f02d";
$fa-var-bookmark: "\f02e";
$fa-var-bookmark-o: "\f097";
$fa-var-briefcase: "\f0b1";
$fa-var-btc: "\f15a";
$fa-var-bug: "\f188";
$fa-var-building: "\f1ad";
$fa-var-building-o: "\f0f7";
$fa-var-bullhorn: "\f0a1";
$fa-var-bullseye: "\f140";
$fa-var-bus: "\f207";
$fa-var-buysellads: "\f20d";
$fa-var-cab: "\f1ba";
$fa-var-calculator: "\f1ec";
$fa-var-calendar: "\f073";
$fa-var-calendar-o: "\f133";
$fa-var-camera: "\f030";
$fa-var-camera-retro: "\f083";
$fa-var-car: "\f1b9";
$fa-var-caret-down: "\f0d7";
$fa-var-caret-left: "\f0d9";
$fa-var-caret-right: "\f0da";
$fa-var-caret-square-o-down: "\f150";
$fa-var-caret-square-o-left: "\f191";
$fa-var-caret-square-o-right: "\f152";
$fa-var-caret-square-o-up: "\f151";
$fa-var-caret-up: "\f0d8";
$fa-var-cart-arrow-down: "\f218";
$fa-var-cart-plus: "\f217";
$fa-var-cc: "\f20a";
$fa-var-cc-amex: "\f1f3";
$fa-var-cc-discover: "\f1f2";
$fa-var-cc-mastercard: "\f1f1";
$fa-var-cc-paypal: "\f1f4";
$fa-var-cc-stripe: "\f1f5";
$fa-var-cc-visa: "\f1f0";
$fa-var-certificate: "\f0a3";
$fa-var-chain: "\f0c1";
$fa-var-chain-broken: "\f127";
$fa-var-check: "\f00c";
$fa-var-check-circle: "\f058";
$fa-var-check-circle-o: "\f05d";
$fa-var-check-square: "\f14a";
$fa-var-check-square-o: "\f046";
$fa-var-chevron-circle-down: "\f13a";
$fa-var-chevron-circle-left: "\f137";
$fa-var-chevron-circle-right: "\f138";
$fa-var-chevron-circle-up: "\f139";
$fa-var-chevron-down: "\f078";
$fa-var-chevron-left: "\f053";
$fa-var-chevron-right: "\f054";
$fa-var-chevron-up: "\f077";
$fa-var-child: "\f1ae";
$fa-var-circle: "\f111";
$fa-var-circle-o: "\f10c";
$fa-var-circle-o-notch: "\f1ce";
$fa-var-circle-thin: "\f1db";
$fa-var-clipboard: "\f0ea";
$fa-var-clock-o: "\f017";
$fa-var-close: "\f00d";
$fa-var-cloud: "\f0c2";
$fa-var-cloud-download: "\f0ed";
$fa-var-cloud-upload: "\f0ee";
$fa-var-cny: "\f157";
$fa-var-code: "\f121";
$fa-var-code-fork: "\f126";
$fa-var-codepen: "\f1cb";
$fa-var-coffee: "\f0f4";
$fa-var-cog: "\f013";
$fa-var-cogs: "\f085";
$fa-var-columns: "\f0db";
$fa-var-comment: "\f075";
$fa-var-comment-o: "\f0e5";
$fa-var-comments: "\f086";
$fa-var-comments-o: "\f0e6";
$fa-var-compass: "\f14e";
$fa-var-compress: "\f066";
$fa-var-connectdevelop: "\f20e";
$fa-var-copy: "\f0c5";
$fa-var-copyright: "\f1f9";
$fa-var-credit-card: "\f09d";
$fa-var-crop: "\f125";
$fa-var-crosshairs: "\f05b";
$fa-var-css3: "\f13c";
$fa-var-cube: "\f1b2";
$fa-var-cubes: "\f1b3";
$fa-var-cut: "\f0c4";
$fa-var-cutlery: "\f0f5";
$fa-var-dashboard: "\f0e4";
$fa-var-dashcube: "\f210";
$fa-var-database: "\f1c0";
$fa-var-dedent: "\f03b";
$fa-var-delicious: "\f1a5";
$fa-var-desktop: "\f108";
$fa-var-deviantart: "\f1bd";
$fa-var-diamond: "\f219";
$fa-var-digg: "\f1a6";
$fa-var-dollar: "\f155";
$fa-var-dot-circle-o: "\f192";
$fa-var-download: "\f019";
$fa-var-dribbble: "\f17d";
$fa-var-dropbox: "\f16b";
$fa-var-drupal: "\f1a9";
$fa-var-edit: "\f044";
$fa-var-eject: "\f052";
$fa-var-ellipsis-h: "\f141";
$fa-var-ellipsis-v: "\f142";
$fa-var-empire: "\f1d1";
$fa-var-envelope: "\f0e0";
$fa-var-envelope-o: "\f003";
$fa-var-envelope-square: "\f199";
$fa-var-eraser: "\f12d";
$fa-var-eur: "\f153";
$fa-var-euro: "\f153";
$fa-var-exchange: "\f0ec";
$fa-var-exclamation: "\f12a";
$fa-var-exclamation-circle: "\f06a";
$fa-var-exclamation-triangle: "\f071";
$fa-var-expand: "\f065";
$fa-var-external-link: "\f08e";
$fa-var-external-link-square: "\f14c";
$fa-var-eye: "\f06e";
$fa-var-eye-slash: "\f070";
$fa-var-eyedropper: "\f1fb";
$fa-var-facebook: "\f09a";
$fa-var-facebook-f: "\f09a";
$fa-var-facebook-official: "\f230";
$fa-var-facebook-square: "\f082";
$fa-var-fast-backward: "\f049";
$fa-var-fast-forward: "\f050";
$fa-var-fax: "\f1ac";
$fa-var-female: "\f182";
$fa-var-fighter-jet: "\f0fb";
$fa-var-file: "\f15b";
$fa-var-file-archive-o: "\f1c6";
$fa-var-file-audio-o: "\f1c7";
$fa-var-file-code-o: "\f1c9";
$fa-var-file-excel-o: "\f1c3";
$fa-var-file-image-o: "\f1c5";
$fa-var-file-movie-o: "\f1c8";
$fa-var-file-o: "\f016";
$fa-var-file-pdf-o: "\f1c1";
$fa-var-file-photo-o: "\f1c5";
$fa-var-file-picture-o: "\f1c5";
$fa-var-file-powerpoint-o: "\f1c4";
$fa-var-file-sound-o: "\f1c7";
$fa-var-file-text: "\f15c";
$fa-var-file-text-o: "\f0f6";
$fa-var-file-video-o: "\f1c8";
$fa-var-file-word-o: "\f1c2";
$fa-var-file-zip-o: "\f1c6";
$fa-var-files-o: "\f0c5";
$fa-var-film: "\f008";
$fa-var-filter: "\f0b0";
$fa-var-fire: "\f06d";
$fa-var-fire-extinguisher: "\f134";
$fa-var-flag: "\f024";
$fa-var-flag-checkered: "\f11e";
$fa-var-flag-o: "\f11d";
$fa-var-flash: "\f0e7";
$fa-var-flask: "\f0c3";
$fa-var-flickr: "\f16e";
$fa-var-floppy-o: "\f0c7";
$fa-var-folder: "\f07b";
$fa-var-folder-o: "\f114";
$fa-var-folder-open: "\f07c";
$fa-var-folder-open-o: "\f115";
$fa-var-font: "\f031";
$fa-var-forumbee: "\f211";
$fa-var-forward: "\f04e";
$fa-var-foursquare: "\f180";
$fa-var-frown-o: "\f119";
$fa-var-futbol-o: "\f1e3";
$fa-var-gamepad: "\f11b";
$fa-var-gavel: "\f0e3";
$fa-var-gbp: "\f154";
$fa-var-ge: "\f1d1";
$fa-var-gear: "\f013";
$fa-var-gears: "\f085";
$fa-var-genderless: "\f1db";
$fa-var-gift: "\f06b";
$fa-var-git: "\f1d3";
$fa-var-git-square: "\f1d2";
$fa-var-github: "\f09b";
$fa-var-github-alt: "\f113";
$fa-var-github-square: "\f092";
$fa-var-gittip: "\f184";
$fa-var-glass: "\f000";
$fa-var-globe: "\f0ac";
$fa-var-google: "\f1a0";
$fa-var-google-plus: "\f0d5";
$fa-var-google-plus-square: "\f0d4";
$fa-var-google-wallet: "\f1ee";
$fa-var-graduation-cap: "\f19d";
$fa-var-gratipay: "\f184";
$fa-var-group: "\f0c0";
$fa-var-h-square: "\f0fd";
$fa-var-hacker-news: "\f1d4";
$fa-var-hand-o-down: "\f0a7";
$fa-var-hand-o-left: "\f0a5";
$fa-var-hand-o-right: "\f0a4";
$fa-var-hand-o-up: "\f0a6";
$fa-var-hdd-o: "\f0a0";
$fa-var-header: "\f1dc";
$fa-var-headphones: "\f025";
$fa-var-heart: "\f004";
$fa-var-heart-o: "\f08a";
$fa-var-heartbeat: "\f21e";
$fa-var-history: "\f1da";
$fa-var-home: "\f015";
$fa-var-hospital-o: "\f0f8";
$fa-var-hotel: "\f236";
$fa-var-html5: "\f13b";
$fa-var-ils: "\f20b";
$fa-var-image: "\f03e";
$fa-var-inbox: "\f01c";
$fa-var-indent: "\f03c";
$fa-var-info: "\f129";
$fa-var-info-circle: "\f05a";
$fa-var-inr: "\f156";
$fa-var-instagram: "\f16d";
$fa-var-institution: "\f19c";
$fa-var-ioxhost: "\f208";
$fa-var-italic: "\f033";
$fa-var-joomla: "\f1aa";
$fa-var-jpy: "\f157";
$fa-var-jsfiddle: "\f1cc";
$fa-var-key: "\f084";
$fa-var-keyboard-o: "\f11c";
$fa-var-krw: "\f159";
$fa-var-language: "\f1ab";
$fa-var-laptop: "\f109";
$fa-var-lastfm: "\f202";
$fa-var-lastfm-square: "\f203";
$fa-var-leaf: "\f06c";
$fa-var-leanpub: "\f212";
$fa-var-legal: "\f0e3";
$fa-var-lemon-o: "\f094";
$fa-var-level-down: "\f149";
$fa-var-level-up: "\f148";
$fa-var-life-bouy: "\f1cd";
$fa-var-life-buoy: "\f1cd";
$fa-var-life-ring: "\f1cd";
$fa-var-life-saver: "\f1cd";
$fa-var-lightbulb-o: "\f0eb";
$fa-var-line-chart: "\f201";
$fa-var-link: "\f0c1";
$fa-var-linkedin: "\f0e1";
$fa-var-linkedin-square: "\f08c";
$fa-var-linux: "\f17c";
$fa-var-list: "\f03a";
$fa-var-list-alt: "\f022";
$fa-var-list-ol: "\f0cb";
$fa-var-list-ul: "\f0ca";
$fa-var-location-arrow: "\f124";
$fa-var-lock: "\f023";
$fa-var-long-arrow-down: "\f175";
$fa-var-long-arrow-left: "\f177";
$fa-var-long-arrow-right: "\f178";
$fa-var-long-arrow-up: "\f176";
$fa-var-magic: "\f0d0";
$fa-var-magnet: "\f076";
$fa-var-mail-forward: "\f064";
$fa-var-mail-reply: "\f112";
$fa-var-mail-reply-all: "\f122";
$fa-var-male: "\f183";
$fa-var-map-marker: "\f041";
$fa-var-mars: "\f222";
$fa-var-mars-double: "\f227";
$fa-var-mars-stroke: "\f229";
$fa-var-mars-stroke-h: "\f22b";
$fa-var-mars-stroke-v: "\f22a";
$fa-var-maxcdn: "\f136";
$fa-var-meanpath: "\f20c";
$fa-var-medium: "\f23a";
$fa-var-medkit: "\f0fa";
$fa-var-meh-o: "\f11a";
$fa-var-mercury: "\f223";
$fa-var-microphone: "\f130";
$fa-var-microphone-slash: "\f131";
$fa-var-minus: "\f068";
$fa-var-minus-circle: "\f056";
$fa-var-minus-square: "\f146";
$fa-var-minus-square-o: "\f147";
$fa-var-mobile: "\f10b";
$fa-var-mobile-phone: "\f10b";
$fa-var-money: "\f0d6";
$fa-var-moon-o: "\f186";
$fa-var-mortar-board: "\f19d";
$fa-var-motorcycle: "\f21c";
$fa-var-music: "\f001";
$fa-var-navicon: "\f0c9";
$fa-var-neuter: "\f22c";
$fa-var-newspaper-o: "\f1ea";
$fa-var-openid: "\f19b";
$fa-var-outdent: "\f03b";
$fa-var-pagelines: "\f18c";
$fa-var-paint-brush: "\f1fc";
$fa-var-paper-plane: "\f1d8";
$fa-var-paper-plane-o: "\f1d9";
$fa-var-paperclip: "\f0c6";
$fa-var-paragraph: "\f1dd";
$fa-var-paste: "\f0ea";
$fa-var-pause: "\f04c";
$fa-var-paw: "\f1b0";
$fa-var-paypal: "\f1ed";
$fa-var-pencil: "\f040";
$fa-var-pencil-square: "\f14b";
$fa-var-pencil-square-o: "\f044";
$fa-var-phone: "\f095";
$fa-var-phone-square: "\f098";
$fa-var-photo: "\f03e";
$fa-var-picture-o: "\f03e";
$fa-var-pie-chart: "\f200";
$fa-var-pied-piper: "\f1a7";
$fa-var-pied-piper-alt: "\f1a8";
$fa-var-pinterest: "\f0d2";
$fa-var-pinterest-p: "\f231";
$fa-var-pinterest-square: "\f0d3";
$fa-var-plane: "\f072";
$fa-var-play: "\f04b";
$fa-var-play-circle: "\f144";
$fa-var-play-circle-o: "\f01d";
$fa-var-plug: "\f1e6";
$fa-var-plus: "\f067";
$fa-var-plus-circle: "\f055";
$fa-var-plus-square: "\f0fe";
$fa-var-plus-square-o: "\f196";
$fa-var-power-off: "\f011";
$fa-var-print: "\f02f";
$fa-var-puzzle-piece: "\f12e";
$fa-var-qq: "\f1d6";
$fa-var-qrcode: "\f029";
$fa-var-question: "\f128";
$fa-var-question-circle: "\f059";
$fa-var-quote-left: "\f10d";
$fa-var-quote-right: "\f10e";
$fa-var-ra: "\f1d0";
$fa-var-random: "\f074";
$fa-var-rebel: "\f1d0";
$fa-var-recycle: "\f1b8";
$fa-var-reddit: "\f1a1";
$fa-var-reddit-square: "\f1a2";
$fa-var-refresh: "\f021";
$fa-var-remove: "\f00d";
$fa-var-renren: "\f18b";
$fa-var-reorder: "\f0c9";
$fa-var-repeat: "\f01e";
$fa-var-reply: "\f112";
$fa-var-reply-all: "\f122";
$fa-var-retweet: "\f079";
$fa-var-rmb: "\f157";
$fa-var-road: "\f018";
$fa-var-rocket: "\f135";
$fa-var-rotate-left: "\f0e2";
$fa-var-rotate-right: "\f01e";
$fa-var-rouble: "\f158";
$fa-var-rss: "\f09e";
$fa-var-rss-square: "\f143";
$fa-var-rub: "\f158";
$fa-var-ruble: "\f158";
$fa-var-rupee: "\f156";
$fa-var-save: "\f0c7";
$fa-var-scissors: "\f0c4";
$fa-var-search: "\f002";
$fa-var-search-minus: "\f010";
$fa-var-search-plus: "\f00e";
$fa-var-sellsy: "\f213";
$fa-var-send: "\f1d8";
$fa-var-send-o: "\f1d9";
$fa-var-server: "\f233";
$fa-var-share: "\f064";
$fa-var-share-alt: "\f1e0";
$fa-var-share-alt-square: "\f1e1";
$fa-var-share-square: "\f14d";
$fa-var-share-square-o: "\f045";
$fa-var-shekel: "\f20b";
$fa-var-sheqel: "\f20b";
$fa-var-shield: "\f132";
$fa-var-ship: "\f21a";
$fa-var-shirtsinbulk: "\f214";
$fa-var-shopping-cart: "\f07a";
$fa-var-sign-in: "\f090";
$fa-var-sign-out: "\f08b";
$fa-var-signal: "\f012";
$fa-var-simplybuilt: "\f215";
$fa-var-sitemap: "\f0e8";
$fa-var-skyatlas: "\f216";
$fa-var-skype: "\f17e";
$fa-var-slack: "\f198";
$fa-var-sliders: "\f1de";
$fa-var-slideshare: "\f1e7";
$fa-var-smile-o: "\f118";
$fa-var-soccer-ball-o: "\f1e3";
$fa-var-sort: "\f0dc";
$fa-var-sort-alpha-asc: "\f15d";
$fa-var-sort-alpha-desc: "\f15e";
$fa-var-sort-amount-asc: "\f160";
$fa-var-sort-amount-desc: "\f161";
$fa-var-sort-asc: "\f0de";
$fa-var-sort-desc: "\f0dd";
$fa-var-sort-down: "\f0dd";
$fa-var-sort-numeric-asc: "\f162";
$fa-var-sort-numeric-desc: "\f163";
$fa-var-sort-up: "\f0de";
$fa-var-soundcloud: "\f1be";
$fa-var-space-shuttle: "\f197";
$fa-var-spinner: "\f110";
$fa-var-spoon: "\f1b1";
$fa-var-spotify: "\f1bc";
$fa-var-square: "\f0c8";
$fa-var-square-o: "\f096";
$fa-var-stack-exchange: "\f18d";
$fa-var-stack-overflow: "\f16c";
$fa-var-star: "\f005";
$fa-var-star-half: "\f089";
$fa-var-star-half-empty: "\f123";
$fa-var-star-half-full: "\f123";
$fa-var-star-half-o: "\f123";
$fa-var-star-o: "\f006";
$fa-var-steam: "\f1b6";
$fa-var-steam-square: "\f1b7";
$fa-var-step-backward: "\f048";
$fa-var-step-forward: "\f051";
$fa-var-stethoscope: "\f0f1";
$fa-var-stop: "\f04d";
$fa-var-street-view: "\f21d";
$fa-var-strikethrough: "\f0cc";
$fa-var-stumbleupon: "\f1a4";
$fa-var-stumbleupon-circle: "\f1a3";
$fa-var-subscript: "\f12c";
$fa-var-subway: "\f239";
$fa-var-suitcase: "\f0f2";
$fa-var-sun-o: "\f185";
$fa-var-superscript: "\f12b";
$fa-var-support: "\f1cd";
$fa-var-table: "\f0ce";
$fa-var-tablet: "\f10a";
$fa-var-tachometer: "\f0e4";
$fa-var-tag: "\f02b";
$fa-var-tags: "\f02c";
$fa-var-tasks: "\f0ae";
$fa-var-taxi: "\f1ba";
$fa-var-tencent-weibo: "\f1d5";
$fa-var-terminal: "\f120";
$fa-var-text-height: "\f034";
$fa-var-text-width: "\f035";
$fa-var-th: "\f00a";
$fa-var-th-large: "\f009";
$fa-var-th-list: "\f00b";
$fa-var-thumb-tack: "\f08d";
$fa-var-thumbs-down: "\f165";
$fa-var-thumbs-o-down: "\f088";
$fa-var-thumbs-o-up: "\f087";
$fa-var-thumbs-up: "\f164";
$fa-var-ticket: "\f145";
$fa-var-times: "\f00d";
$fa-var-times-circle: "\f057";
$fa-var-times-circle-o: "\f05c";
$fa-var-tint: "\f043";
$fa-var-toggle-down: "\f150";
$fa-var-toggle-left: "\f191";
$fa-var-toggle-off: "\f204";
$fa-var-toggle-on: "\f205";
$fa-var-toggle-right: "\f152";
$fa-var-toggle-up: "\f151";
$fa-var-train: "\f238";
$fa-var-transgender: "\f224";
$fa-var-transgender-alt: "\f225";
$fa-var-trash: "\f1f8";
$fa-var-trash-o: "\f014";
$fa-var-tree: "\f1bb";
$fa-var-trello: "\f181";
$fa-var-trophy: "\f091";
$fa-var-truck: "\f0d1";
$fa-var-try: "\f195";
$fa-var-tty: "\f1e4";
$fa-var-tumblr: "\f173";
$fa-var-tumblr-square: "\f174";
$fa-var-turkish-lira: "\f195";
$fa-var-twitch: "\f1e8";
$fa-var-twitter: "\f099";
$fa-var-twitter-square: "\f081";
$fa-var-umbrella: "\f0e9";
$fa-var-underline: "\f0cd";
$fa-var-undo: "\f0e2";
$fa-var-university: "\f19c";
$fa-var-unlink: "\f127";
$fa-var-unlock: "\f09c";
$fa-var-unlock-alt: "\f13e";
$fa-var-unsorted: "\f0dc";
$fa-var-upload: "\f093";
$fa-var-usd: "\f155";
$fa-var-user: "\f007";
$fa-var-user-md: "\f0f0";
$fa-var-user-plus: "\f234";
$fa-var-user-secret: "\f21b";
$fa-var-user-times: "\f235";
$fa-var-users: "\f0c0";
$fa-var-venus: "\f221";
$fa-var-venus-double: "\f226";
$fa-var-venus-mars: "\f228";
$fa-var-viacoin: "\f237";
$fa-var-video-camera: "\f03d";
$fa-var-vimeo-square: "\f194";
$fa-var-vine: "\f1ca";
$fa-var-vk: "\f189";
$fa-var-volume-down: "\f027";
$fa-var-volume-off: "\f026";
$fa-var-volume-up: "\f028";
$fa-var-warning: "\f071";
$fa-var-wechat: "\f1d7";
$fa-var-weibo: "\f18a";
$fa-var-weixin: "\f1d7";
$fa-var-whatsapp: "\f232";
$fa-var-wheelchair: "\f193";
$fa-var-wifi: "\f1eb";
$fa-var-windows: "\f17a";
$fa-var-won: "\f159";
$fa-var-wordpress: "\f19a";
$fa-var-wrench: "\f0ad";
$fa-var-xing: "\f168";
$fa-var-xing-square: "\f169";
$fa-var-yahoo: "\f19e";
$fa-var-yelp: "\f1e9";
$fa-var-yen: "\f157";
$fa-var-youtube: "\f167";
$fa-var-youtube-play: "\f16a";
$fa-var-youtube-square: "\f166";



File: /index.php
<?php
session_start();

include 'parameters.php';
require __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . "/../");
$dotenv->load();

$fb = new Facebook\Facebook([
  'app_id'                => $_SERVER['APP_ID'],
  'app_secret'            => $_SERVER['APP_SECRET'],
  'default_graph_version' => $_SERVER['DEFAULT_GRAPH_VERSION'],
]);

$helper      = $fb->getRedirectLoginHelper();
$scope       = array("email");
$loginUrl    = $helper->getLoginUrl($callBackUrl,$scope);

$_SESSION["mac"]=$_POST['mac'];
$_SESSION["ip"]=$_POST['ip'];
$_SESSION["linkorig"]=$_POST['link-orig'];
$_SESSION["linkloginonly"]=$_POST['link-login-only'];

$_SESSION["user_type"] = "new";
$_SESSION["method"] = "Form";

/*
Checking DB to see if user exists or not.
*/

$host_ip = $_SERVER['HOST_IP'];
$db_user = $_SERVER['DB_USER'];
$db_pass = $_SERVER['DB_PASS'];
$db_name = $_SERVER['DB_NAME'];

$con = mysqli_connect($host_ip, $db_user, $db_pass, $db_name);

if (mysqli_connect_errno()) {
  echo "Failed to connect to SQL: " . mysqli_connect_error();
}

$result = mysqli_query($con, "SELECT * FROM `$table_name` WHERE mac='$_SESSION[mac]'");

if ($result->num_rows >= 1) {
  $row = mysqli_fetch_array($result);

  $_SESSION["fname"] = $row[1];
  $_SESSION["lname"] = $row[2];
  $_SESSION["email"] = $row[3];
  $_SESSION["method"] = $row[5];

  mysqli_close($con);

  $_SESSION["user_type"] = "repeat";
  header("Location: welcome.php");
} else {
  mysqli_close($con);
}

?>

<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Astiisb WiFi</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <link rel="stylesheet" href="bulma.min.css" />
  <link rel="stylesheet" href="font-awesome\css\font-awesome.min.css" />
  <script defer src="vendor\fortawesome\font-awesome\js\all.js"></script>
  <link rel="icon" type="image/png" href="favicomatic\favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-16x16.png" sizes="16x16" />
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="bg">

    <figure id="logo">
      <img src="logo.png">
    </figure>

    <div id="login" class="content is-size-4 has-text-weight-bold">Login for Free Wi-Fi</div>

    <form id="login_success" class="form_login" method="post" action="connect.php">
      <br>
      
      <div class="field">
        <div class="control has-icons-left">
          <input class="input" type="text" id="form_font" name="fname" placeholder="First Name" required>
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
        </div>
      </div>
      
      <div class="field">
        <div class="control has-icons-left">
          <input class="input" type="text" id="form_font" name="lname" placeholder="Last Name" required>
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
        </div>
      </div>
      
      <div class="field">
        <div class="control has-icons-left">
          <input class="input" type="email" id="form_font" name="email" placeholder="Email" required>
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
        </div>
      </div>
      
      <div id="access_wifi" class="control">
        <button id="button_font" class="button is-danger">Continue</button>
      </div>
                        
    </form>

    <div id="logintext" class="content is-size-6">Or login using:</div>
    
    <div id="social">
      <a href="<?php echo htmlspecialchars($loginUrl);?>" class="facebookBtn smGlobalBtn"></a>
    </div>
    <br>

    <div id="powered" class="content is-size-6">Powered by Astiisb</div>
    <div id="copyright" class="content is-size-6">(C) Copyright 2020</div>

  </div>

</body>
</html>

File: /md5.js
/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 1.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Code also contributed by Greg Holt
 * See http://pajhome.org.uk/site/legal.html for details.
 */

/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt))
}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t)
{
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t)
{
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t)
{
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t)
{
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t)
{
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}

/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x)
{
  var a =  1732584193
  var b = -271733879
  var c = -1732584194
  var d =  271733878

  for(i = 0; i < x.length; i += 16)
  {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d

    a = ff(a, b, c, d, x[i+ 0], 7 , -680876936)
    d = ff(d, a, b, c, x[i+ 1], 12, -389564586)
    c = ff(c, d, a, b, x[i+ 2], 17,  606105819)
    b = ff(b, c, d, a, x[i+ 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i+ 4], 7 , -176418897)
    d = ff(d, a, b, c, x[i+ 5], 12,  1200080426)
    c = ff(c, d, a, b, x[i+ 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i+ 7], 22, -45705983)
    a = ff(a, b, c, d, x[i+ 8], 7 ,  1770035416)
    d = ff(d, a, b, c, x[i+ 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i+10], 17, -42063)
    b = ff(b, c, d, a, x[i+11], 22, -1990404162)
    a = ff(a, b, c, d, x[i+12], 7 ,  1804603682)
    d = ff(d, a, b, c, x[i+13], 12, -40341101)
    c = ff(c, d, a, b, x[i+14], 17, -1502002290)
    b = ff(b, c, d, a, x[i+15], 22,  1236535329)

    a = gg(a, b, c, d, x[i+ 1], 5 , -165796510)
    d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632)
    c = gg(c, d, a, b, x[i+11], 14,  643717713)
    b = gg(b, c, d, a, x[i+ 0], 20, -373897302)
    a = gg(a, b, c, d, x[i+ 5], 5 , -701558691)
    d = gg(d, a, b, c, x[i+10], 9 ,  38016083)
    c = gg(c, d, a, b, x[i+15], 14, -660478335)
    b = gg(b, c, d, a, x[i+ 4], 20, -405537848)
    a = gg(a, b, c, d, x[i+ 9], 5 ,  568446438)
    d = gg(d, a, b, c, x[i+14], 9 , -1019803690)
    c = gg(c, d, a, b, x[i+ 3], 14, -187363961)
    b = gg(b, c, d, a, x[i+ 8], 20,  1163531501)
    a = gg(a, b, c, d, x[i+13], 5 , -1444681467)
    d = gg(d, a, b, c, x[i+ 2], 9 , -51403784)
    c = gg(c, d, a, b, x[i+ 7], 14,  1735328473)
    b = gg(b, c, d, a, x[i+12], 20, -1926607734)

    a = hh(a, b, c, d, x[i+ 5], 4 , -378558)
    d = hh(d, a, b, c, x[i+ 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i+11], 16,  1839030562)
    b = hh(b, c, d, a, x[i+14], 23, -35309556)
    a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060)
    d = hh(d, a, b, c, x[i+ 4], 11,  1272893353)
    c = hh(c, d, a, b, x[i+ 7], 16, -155497632)
    b = hh(b, c, d, a, x[i+10], 23, -1094730640)
    a = hh(a, b, c, d, x[i+13], 4 ,  681279174)
    d = hh(d, a, b, c, x[i+ 0], 11, -358537222)
    c = hh(c, d, a, b, x[i+ 3], 16, -722521979)
    b = hh(b, c, d, a, x[i+ 6], 23,  76029189)
    a = hh(a, b, c, d, x[i+ 9], 4 , -640364487)
    d = hh(d, a, b, c, x[i+12], 11, -421815835)
    c = hh(c, d, a, b, x[i+15], 16,  530742520)
    b = hh(b, c, d, a, x[i+ 2], 23, -995338651)

    a = ii(a, b, c, d, x[i+ 0], 6 , -198630844)
    d = ii(d, a, b, c, x[i+ 7], 10,  1126891415)
    c = ii(c, d, a, b, x[i+14], 15, -1416354905)
    b = ii(b, c, d, a, x[i+ 5], 21, -57434055)
    a = ii(a, b, c, d, x[i+12], 6 ,  1700485571)
    d = ii(d, a, b, c, x[i+ 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i+10], 15, -1051523)
    b = ii(b, c, d, a, x[i+ 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i+ 8], 6 ,  1873313359)
    d = ii(d, a, b, c, x[i+15], 10, -30611744)
    c = ii(c, d, a, b, x[i+ 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i+13], 21,  1309151649)
    a = ii(a, b, c, d, x[i+ 4], 6 , -145523070)
    d = ii(d, a, b, c, x[i+11], 10, -1120210379)
    c = ii(c, d, a, b, x[i+ 2], 15,  718787259)
    b = ii(b, c, d, a, x[i+ 9], 21, -343485551)

    a = safe_add(a, olda)
    b = safe_add(b, oldb)
    c = safe_add(c, oldc)
    d = safe_add(d, oldd)
  }
  return [a, b, c, d]
}

/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = "0123456789abcdef"
  var str = ""
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8)) & 0xF)
  }
  return str
}

/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for(var i = 0; i < binarray.length * 32; i += 6)
  {
    str += tab.charAt(((binarray[i>>5] << (i%32)) & 0x3F) |
                      ((binarray[i>>5+1] >> (32-i%32)) & 0x3F))
  }
  return str
}

/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str)
{
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>2] |= (str.charCodeAt(i) & 0xFF) << ((i%4) * 8)
  blks[i>>2] |= 0x80 << ((i%4) * 8)
  blks[nblk*16-2] = str.length * 8
  return blks
}

/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str)
{
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>1] |= str.charCodeAt(i) << ((i%2) * 16)
  blks[i>>1] |= 0x80 << ((i%2) * 16)
  blks[nblk*16-2] = str.length * 16
  return blks
}

/*
 * External interface
 */
function hexMD5 (str) { return binl2hex(coreMD5( str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5 (str) { return binl2b64(coreMD5( str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5( str2binl(str))) }


File: /parameters.php.example
<?php

#MySQL DB table name for this site

$table_name = "";

#Facebook Callback URL

$callBackUrl = "";

?>

File: /policy.php
<h2>Welcome</h2>
	<p>These terms and conditions outline the rules and regulations for the use of this Website.</p> 
	<p>By accessing this website we assume you accept these terms and conditions in full. Do not continue to use this website 
	if you do not accept all of the terms and conditions stated on this page.</p>
	<p>The following terminology applies to these Terms and Conditions, Privacy Statement and Disclaimer Notice
	and any or all Agreements: “Client”, “You” and “Your” refers to you, the person accessing this website
	and accepting the Company’s terms and conditions. “The Company”, “Ourselves”, “We”, “Our” and “Us”, refers
	to our Company. “Party”, “Parties”, or “Us”, refers to both the Client and ourselves, or either the Client
	or ourselves. All terms refer to the offer, acceptance and consideration of payment necessary to undertake
	the process of our assistance to the Client in the most appropriate manner, whether by formal meetings
	of a fixed duration, or any other means, for the express purpose of meeting the Client’s needs in respect
	of provision of the Company’s stated services/products, in accordance with and subject to, prevailing law
	of . Any use of the above terminology or other words in the singular, plural,
	capitalisation and/or he/she or they, are taken as interchangeable and therefore as referring to same.</p><h2>Cookies</h2>
	<p>We employ the use of cookies. By using this website you consent to the use of cookies 
	in accordance with this website's privacy policy.</p><p>Most of the modern day interactive web sites
	use cookies to enable us to retrieve user details for each visit. Cookies are used in some areas of our site
	to enable the functionality of this area and ease of use for those people visiting. Some of our 
	affiliate / advertising partners may also use cookies.</p><h2>License</h2>
	<p>Unless otherwise stated, this website and/or it’s licensors own the intellectual property rights for
	all material on this website. All intellectual property rights are reserved.</p>

	<p>Redistribute content from this website (unless content is specifically made for redistribution).</p>
<h2>Reservation of Rights</h2>
	<p>We reserve the right at any time and in its sole discretion to request that you remove all links or any particular
	link to our Web site. You agree to immediately remove all links to our Web site upon such request. We also
	reserve the right to amend these terms and conditions and its linking policy at any time. By continuing
	to link to our Web site, you agree to be bound to and abide by these linking terms and conditions.</p>
<h2>Removal of links from our website</h2>
	<p>If you find any link on our Web site or any linked web site objectionable for any reason, you may contact
	us about this. We will consider requests to remove links but will have no obligation to do so or to respond
	directly to you.</p>
	<p>Whilst we endeavour to ensure that the information on this website is correct, we do not warrant its completeness
	or accuracy; nor do we commit to ensuring that the website remains available or that the material on the
	website is kept up to date.</p>
<h2>Content Liability</h2>
	<p>We shall have no responsibility or liability for any content appearing on your Web site. You agree to indemnify
	and defend us against all claims arising out of or based upon your Website. No link(s) may appear on any
	page on your Web site or within any context containing content or materials that may be interpreted as
	libelous, obscene or criminal, or which infringes, otherwise violates, or advocates the infringement or
	other violation of, any third party rights.</p>
<h2>Disclaimer</h2>
	<p>To the maximum extent permitted by applicable law, we exclude all representations, warranties and conditions relating to our website and the use of this website (including, without limitation, any warranties implied by law in respect of satisfactory quality, fitness for purpose and/or the use of reasonable care and skill). Nothing in this disclaimer will:</p>
	<ol>
	<li>limit or exclude our or your liability for death or personal injury resulting from negligence;</li>
	<li>limit or exclude our or your liability for fraud or fraudulent misrepresentation;</li>
	<li>limit any of our or your liabilities in any way that is not permitted under applicable law; or</li>
	<li>exclude any of our or your liabilities that may not be excluded under applicable law.</li>
	</ol>
	<p>The limitations and exclusions of liability set out in this Section and elsewhere in this disclaimer: (a)
	are subject to the preceding paragraph; and (b) govern all liabilities arising under the disclaimer or
	in relation to the subject matter of this disclaimer, including liabilities arising in contract, in tort
	(including negligence) and for breach of statutory duty.</p>
	<p>To the extent that the website and the information and services on the website are provided free of charge,
	we will not be liable for any loss or damage of any nature.</p>


File: /README.md
# External Captive Portal for Mikrotik with Facebook Login

The captive portal web server can be setup using the instructions given [here](https://gist.github.com/nasirhafeez/4e1c2c5536d313db96e2b4ce4b3b269e). The following actions are required to use the code given in this repo:
 
Copy the `.env.example` file to the upper level folder and change its name to `.env`. Set the values of the given project-wide environment variables in it.

Rename the `parameters.php.example` file to `parameters.php` and set the values of variables according to the current site.

*Install Composer*

Then run `php composer.phar install` to install the packages given in `composer.json`.


File: /style.css
/*
    *{ border: 1px solid red; }
*/

body {
    color: black;
    font-family: "Ariel", sans-serif;
}

.bg {
    position:relative;
    padding:0;
    margin:0;
    top:0;
    left:0;
    width: 100%;
    height: 100%;
    background-color: white;
    background-size: cover;
}

#logo {
    padding-top: 3px;
    width: 30%;
    height: 20%;
    margin-left: auto;
    margin-right: auto;
}

.form_login {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
}

#login {
    text-align: center;
    margin-bottom: 5px;
}

#devices {
    text-align: center;
    margin: 0;
}

#handle {
    text-align: center;
    margin: 0;
    margin-top: 10px;
}

#thanks {
    text-align: center;
    margin: 0;
    margin-top: 15px;
}

#customers {
    text-align: center;
    margin: 0;
}

#social {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
}

#logintext {
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
}

.smGlobalBtn{ /* global button class */
    display: inline-block;
    position: relative;
    cursor: pointer;
    width: 50px;
    height: 50px;
    box-shadow: 0 2px 2px #999;
    padding: 0px;
    text-decoration: none;
    text-align: center;
    color: #fff;
    font-size: 25px;
    font-weight: normal;
    line-height: 2em;
    border-radius: 25px;
    -moz-border-radius:25px;
    -webkit-border-radius:25px;
  }
  
/* facebook button class*/
.facebookBtn{
background: #4060A5;
}

.facebookBtn:before{ /* use :before to add the relevant icons */
font-family: "FontAwesome";
content: "\f09a"; /* add facebook icon */
}

.facebookBtn:hover{
color: #4060A5;
background: #fff;
}

#powered {
    text-align: center;
    margin: 0;
}

#powered_handle {
    text-align: center;
    margin: 0;
    margin-top: 220px;
}

#powered_thanks {
    text-align: center;
    margin: 0;
    margin-top: 220px;
}

#powered_welcome {
    text-align: center;
    margin: 0;
    margin-top: 210px;
}

#copyright {
    text-align: center;
    margin: 0;
}

a {
    color: black;
    text-decoration: underline;           
}

a:hover {
    color: black;
}

/* Media Query for Desktops */

@media only screen and (min-width: 768px) {
    html {
        overflow: hidden;
    }
    .bg {
        position: absolute;
        background-size: 100% 100%;
    }
    #logo {
        max-width: 10%;
    }
    #login {
        margin-top: 20px;
    }
    #powered {
        margin-top: 0px;
    }
    #powered_handle {
        margin-top: 275px;
    }
    #powered_thanks {
        margin-top: 275px;
    }
    #powered_welcome {
        margin-top: 270px;
    }
    #logintext {
        margin-top: 15px;
        margin-bottom: 15px;
    }
}

/* Media Query for iPads */

@media only screen 
and (min-device-width : 768px) 
and (max-device-width : 1024px)  {
    #powered {
        margin-top: 100px;
    }
    #powered_handle {
        margin-top: 420px;
    }
    #powered_thanks {
        margin-top: 420px;
    }
    #powered_welcome {
        margin-top: 410px;
    }
    #logo {
        max-width: 20%;
    }
    #logintext {
        margin-top: 15px;
        margin-bottom: 15px;
    }
}


File: /thankyou.htm
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Astiisb WiFi</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <link rel="stylesheet" href="bulma.min.css" />
  <script defer src="vendor\fortawesome\font-awesome\js\all.js"></script>
  <meta http-equiv="refresh" content="5;url=https://www.google.com" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-16x16.png" sizes="16x16" />
  <link rel="stylesheet" href="style.css">
</head>
<body>
	<div class="bg">

    <section id="logo" class="section">
      <figure>
        <img src="logo.png">
      </figure>
    </section>

		<div id="thanks" class="content is-size-6">Thanks, you are now </div>
		<div id="devices" class="content is-size-6">authorized on WiFi</div>

    <div id="powered_thanks" class="content is-size-6">Powered by Astiisb</div>
    <div id="copyright" class="content is-size-6">(C) Copyright 2020</div>

	</div>
</body>
</html>

File: /welcome.php
<?php error_reporting(E_ALL ^ E_NOTICE); 
session_start();

/*
Printing a welcome message for the user
*/

?>
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Astiisb WiFi</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <link rel="stylesheet" href="bulma.min.css" />
  <script defer src="vendor\fortawesome\font-awesome\js\all.js"></script>
  <meta http-equiv="refresh" content="5;url=connect.php" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-32x32.png" sizes="32x32" />
  <link rel="icon" type="image/png" href="favicomatic\favicon-16x16.png" sizes="16x16" />
  <link rel="stylesheet" href="style.css">
</head>
<body>
	<div class="bg">

    <section id="logo" class="section">
      <figure>
        <img src="logo.png">
      </figure>
    </section>

		<div id="devices" class="content is-size-6">Welcome, <?php echo htmlspecialchars($_SESSION["fname"]);?>!</div>
		<div id="devices" class="content is-size-6">You'll be automatically authorized</div>
		<div id="devices" class="content is-size-6">on the network in a few moments</div>
    
    <div id="powered_welcome" class="content is-size-6">Powered by Astiisb</div>
    <div id="copyright" class="content is-size-6">(C) Copyright 2020</div>

	</div>
</body>
</html>


