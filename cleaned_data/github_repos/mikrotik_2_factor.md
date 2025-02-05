# Repository Information
Name: mikrotik_2_factor

# Directory Structure
Directory structure:
└── github_repos/mikrotik_2_factor/
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
    │   │       ├── pack-eda32a2505aa464a260b25df6f85c225877dab16.idx
    │   │       └── pack-eda32a2505aa464a260b25df6f85c225877dab16.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── app/
    │   ├── .dockerignore
    │   ├── app/
    │   │   ├── asgi.py
    │   │   ├── celery.py
    │   │   ├── settings.py
    │   │   ├── tasks.py
    │   │   ├── urls.py
    │   │   ├── wsgi.py
    │   │   └── __init__.py
    │   ├── clients/
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations/
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── 0002_client_last_confirm_message_id.py
    │   │   │   ├── 0003_auto_20200807_1625.py
    │   │   │   ├── 0004_client_caller_id.py
    │   │   │   ├── 0005_client_name.py
    │   │   │   ├── 0006_alter_client_chat_id.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   ├── views.py
    │   │   └── __init__.py
    │   ├── Dockerfile
    │   ├── entrypoint.sh
    │   ├── helpers/
    │   │   ├── crud.py
    │   │   ├── request_templates.py
    │   │   ├── shell.py
    │   │   └── __init__.py
    │   ├── manage.py
    │   ├── requirements.txt
    │   ├── timecheck.py
    │   └── watcher.py
    ├── docker-compose.yml
    ├── nginx/
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── README.md
    ├── routeros_scripts/
    │   └── ppp_profile_behavior.rsc
    └── you_need.env


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
	url = https://github.com/m3xan1k/mikrotik_2_factor.git
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
0000000000000000000000000000000000000000 8ef0d3cb8b8a02d1b9a2fe443e0a8505387d3d40 vivek-dodia <vivek.dodia@icloud.com> 1738606329 -0500	clone: from https://github.com/m3xan1k/mikrotik_2_factor.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 8ef0d3cb8b8a02d1b9a2fe443e0a8505387d3d40 vivek-dodia <vivek.dodia@icloud.com> 1738606329 -0500	clone: from https://github.com/m3xan1k/mikrotik_2_factor.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 8ef0d3cb8b8a02d1b9a2fe443e0a8505387d3d40 vivek-dodia <vivek.dodia@icloud.com> 1738606329 -0500	clone: from https://github.com/m3xan1k/mikrotik_2_factor.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8ef0d3cb8b8a02d1b9a2fe443e0a8505387d3d40 refs/remotes/origin/master


File: /.git\refs\heads\master
8ef0d3cb8b8a02d1b9a2fe443e0a8505387d3d40


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore

# Created by https://www.toptal.com/developers/gitignore/api/django
# Edit at https://www.toptal.com/developers/gitignore?templates=django

### Django ###
File: /app\.dockerignore
celerybeat.pid


File: /app\app\asgi.py
"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()


File: /app\app\celery.py
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = Celery('app')
application.config_from_object('django.conf:settings', namespace='CELERY')
application.autodiscover_tasks()


File: /app\app\settings.py
"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from celery.schedules import crontab
import app.tasks


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'foobar')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', default=1))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clients',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CELERY_BROKER_URL = "redis://celery-redis:6379/0"
CELERY_RESULT_BACKEND = "redis://celery-redis:6379/0"


CELERY_BEAT_SCHEDULE = {
    'check_exceed_unconfirmed_connections': {
        'task': 'app.tasks.check_exceed_unconfirmed_connections',
        'schedule': crontab(minute='*/1'),
    }
}


File: /app\app\tasks.py
from celery import shared_task

from timecheck import TimeChecker


@shared_task
def check_exceed_unconfirmed_connections():
    TimeChecker.run()


File: /app\app\urls.py
"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
]


File: /app\app\wsgi.py
"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# import os

from django.core.wsgi import get_wsgi_application

# os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

application = get_wsgi_application()


File: /app\app\__init__.py
from .celery import application as celery_app

__all__ = ('celery_app', )


File: /app\clients\admin.py
from django.contrib import admin
from clients.models import Client

from helpers import shell


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    actions = ['remove_ban']

    list_display = ('name', 'chat_id', 'source_ip', 'destination_ip', 'caller_id', 'connected',
                    'confirmed', 'last_connection_time', 'unconfirmed_connections_count')

    def remove_ban(self, request, queryset):
        queryset.update(unconfirmed_connections_count=0)
        ips_to_unban = [client.caller_id for client in queryset]
        res = shell.unban_ip_address(ips_to_unban)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


File: /app\clients\apps.py
from django.apps import AppConfig


class ClientsConfig(AppConfig):
    name = 'clients'


File: /app\clients\migrations\0001_initial.py
# Generated by Django 3.0.7 on 2020-08-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('source_ip', models.TextField(blank=True)),
                ('destination_ip', models.TextField(blank=True)),
                ('connected', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('unconfirmed_connections_count', models.IntegerField(default=0)),
                ('last_connection_time', models.DateTimeField()),
            ],
        ),
    ]


File: /app\clients\migrations\0002_client_last_confirm_message_id.py
# Generated by Django 3.0.7 on 2020-08-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_confirm_message_id',
            field=models.IntegerField(null=True),
        ),
    ]


File: /app\clients\migrations\0003_auto_20200807_1625.py
# Generated by Django 3.0.7 on 2020-08-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_last_confirm_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='chat_id',
            field=models.IntegerField(db_index=True),
        ),
    ]


File: /app\clients\migrations\0004_client_caller_id.py
# Generated by Django 3.0.7 on 2020-08-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20200807_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='caller_id',
            field=models.TextField(blank=True),
        ),
    ]


File: /app\clients\migrations\0005_client_name.py
# Generated by Django 3.0.7 on 2021-04-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_client_caller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]


File: /app\clients\migrations\0006_alter_client_chat_id.py
# Generated by Django 4.0.4 on 2022-05-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='chat_id',
            field=models.BigIntegerField(db_index=True),
        ),
    ]


File: /app\clients\models.py
from django.db import models


class Client(models.Model):
    name = models.TextField(blank=True, null=False)
    chat_id = models.BigIntegerField(db_index=True)
    source_ip = models.TextField(blank=True, null=False)
    caller_id = models.TextField(blank=True, null=False)
    destination_ip = models.TextField(blank=True, null=False)
    connected = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    unconfirmed_connections_count = models.IntegerField(default=0)
    last_connection_time = models.DateTimeField()
    last_confirm_message_id = models.IntegerField(null=True)

    def __str__(self):
        return self.chat_id.__str__()


File: /app\clients\tests.py
import json
import os
from datetime import timedelta

from django.test import TestCase
from django.shortcuts import reverse
from django.http import JsonResponse
from django.utils import timezone

from clients.models import Client
from clients.views import (
    ConnectView, DisconnectView, ConfirmView, TimeCheckView
)


class TestViews(TestCase):

    CONNECT_URL = reverse(ConnectView.name)
    DISCONNECT_URL = reverse(DisconnectView.name)
    CONFIRM_URL = reverse(ConfirmView.name)
    TIMECHECK_URL = reverse(TimeCheckView.name)

    def setUp(self):
        os.environ.setdefault('SSH_HOST', '0.0.0.0')

    def test_bad_payload(self):
        payload = {
            'chat_id': '',
            'source_ip': '1.1.1.1',
            'caller_id': '2.2.2.2',
            'destination_ip': '255.255.255.0',
        }
        response: JsonResponse = self.client.post(
            self.CONNECT_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 400)
        msg = json.loads(response.content.decode('utf-8')).get('msg')
        self.assertEqual(msg, 'chat_id required in request body')

    def test_connect(self):
        payload = {
            'chat_id': '1',
            'source_ip': '1.1.1.1',
            'caller_id': '2.2.2.2',
            'destination_ip': '255.255.255.0',
        }
        response: JsonResponse = self.client.post(
            self.CONNECT_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 400)
        client = Client.objects.filter(chat_id=1).first()
        self.assertFalse(client.connected)
        self.assertFalse(client.confirmed)

    def test_exceeded_connections(self):
        max_conn = int(os.environ.get('MAX_UNCONFIRMED_CONNECTIONS'))
        client = Client.objects.create(
            chat_id=2,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=(max_conn + 1),
            last_connection_time=timezone.now(),
        )
        payload = {
            'chat_id': client.chat_id,
            'source_ip': client.source_ip,
            'destination_ip': client.destination_ip,
        }
        response: JsonResponse = self.client.post(
            self.CONNECT_URL, content_type='application/json', data=json.dumps(payload),
        )
        msg = json.loads(response.content.decode('utf-8')).get('msg')
        self.assertEqual(msg, 'client banned')

    def test_disconnect_not_found(self):
        payload = {'chat_id': '999'}
        response: JsonResponse = self.client.post(
            self.DISCONNECT_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 404)

    def test_disconnect_success(self):
        client = Client.objects.create(
            chat_id=3,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=0,
            last_connection_time=timezone.now(),
            connected=True,
        )
        payload = {'chat_id': client.chat_id}
        response: JsonResponse = self.client.post(
            self.DISCONNECT_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 200)
        msg = json.loads(response.content.decode('utf-8')).get('msg')
        self.assertEqual(msg, 'client disconnected')

    def test_confirm_not_found(self):
        payload = {'chat_id': '999'}
        response: JsonResponse = self.client.post(
            self.CONFIRM_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 404)

    def test_confirm_not_connected(self):
        client = Client.objects.create(
            chat_id=4,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=0,
            last_connection_time=timezone.now(),
            connected=False,
        )
        payload = {'chat_id': client.chat_id}
        response: JsonResponse = self.client.post(
            self.CONFIRM_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 422)

    def test_confirm_connected(self):
        client = Client.objects.create(
            chat_id=5,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=0,
            last_connection_time=timezone.now(),
            connected=True,
        )
        payload = {'chat_id': client.chat_id}
        response: JsonResponse = self.client.post(
            self.CONFIRM_URL, content_type='application/json', data=json.dumps(payload),
        )
        self.assertEqual(response.status_code, 200)
        msg = json.loads(response.content.decode('utf-8')).get('msg')
        self.assertEqual(msg, 'client confirmed')

    def test_disconnect_clients(self):
        timeout = int(os.environ.get('UNCONFIRMED_TIMEOUT'))
        time_border = timedelta(minutes=(timeout + 1))
        exceeded_client = Client.objects.create(
            chat_id=6,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=0,
            last_connection_time=timezone.now() - time_border,
            connected=True,
            confirmed=False,
        )
        normal_client = Client.objects.create(
            chat_id=7,
            source_ip='2.2.2.2',
            caller_id='2.2.2.2',
            destination_ip='255.255.255.0',
            unconfirmed_connections_count=0,
            last_connection_time=timezone.now(),
            connected=True,
            confirmed=False,
        )

        response: JsonResponse = self.client.get(self.TIMECHECK_URL)
        msg = json.loads(response.content.decode('utf-8')).get('msg')
        exceeded_client.refresh_from_db()
        normal_client.refresh_from_db()

        self.assertEqual(msg, '1 clients disconnected')
        self.assertFalse(exceeded_client.connected)
        self.assertTrue(normal_client.connected)


File: /app\clients\urls.py
from django.urls import path
from clients.views import ConnectView, ConfirmView, DisconnectView, TimeCheckView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('connect/', csrf_exempt(ConnectView.as_view()), name=ConnectView.name),
    path('disconnect/', csrf_exempt(DisconnectView.as_view()), name=DisconnectView.name),
    path('confirm/', csrf_exempt(ConfirmView.as_view()), name=ConfirmView.name),
    path('timecheck/', TimeCheckView.as_view(), name=TimeCheckView.name),
]


File: /app\clients\views.py
import json

from django.views import View
from django.http import HttpRequest, JsonResponse

from helpers import crud
from helpers.request_templates import (
    send_confirm_button, send_message, Message,
    delete_confirm_button,
)

from helpers import shell


class ConnectView(View):

    name = 'connect'

    def post(self, request: HttpRequest) -> JsonResponse:

        # serialize request body to python dict
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)

        if not payload['chat_id']:
            return JsonResponse({'msg': 'chat_id required in request body'}, status=400)
        chat_id = int(payload['chat_id'])

        # check if client has too much unconfirmed connections to ban or not
        if crud.has_exceeded_connections(payload):
            ban: bool = shell.ban_ip_address(payload['source_ip'], payload['caller_id'])

            # if client was not properly banned on router
            if not ban:
                return JsonResponse({'msg': 'client was not properly banned on router'})

            crud.save_disconnected_client(chat_id, banned=True)
            send_message.delay(chat_id, Message.banned())
            return JsonResponse({'msg': 'client banned'})

        # if ok save client and send confirmation button to tg
        crud.save_connected_client(payload)
        response = send_confirm_button(chat_id, payload)

        # wrong chat id may cause unsuccessfull response
        if not response.status_code == 200:
            crud.save_disconnected_client(chat_id)
            return JsonResponse({'msg': 'client disconnected. telegram request not ok'}, status=400)

        # if ok save btn message id finally
        crud.save_message_id(chat_id, response)
        return JsonResponse({'msg': 'client connected'})


class DisconnectView(View):

    name = 'disconnect'

    def post(self, request: HttpRequest) -> JsonResponse:

        # serialize request body to python dict
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)

        # try to find and save client
        client = crud.save_disconnected_client(int(payload['chat_id']))
        if not client:
            return JsonResponse({'msg': 'client not found'}, status=404)
        delete_confirm_button.delay(client.chat_id, client.last_confirm_message_id)
        send_message.delay(client.chat_id, Message.disconnected())
        return JsonResponse({'msg': 'client disconnected'})


class ConfirmView(View):

    name = 'confirm'

    def post(self, request: HttpRequest) -> JsonResponse:

        # serialize request body to python dict
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)

        chat_id = int(payload['chat_id'])

        # try to save client and check different cases of client state
        client, status = crud.save_confirmed_client(chat_id)

        # if client not found
        if status == 404:
            return JsonResponse({'msg': 'client not found'}, status=status)

        # clean button after all
        delete_confirm_button.delay(chat_id, client.last_confirm_message_id)

        # if client not connected
        if status == 422:
            return JsonResponse({'msg': 'client not connected'}, status=status)

        # successfully saved client authorizes on router
        router_response = shell.authorize_ip_address(client.source_ip)

        # for some reason router may not respond, so client will become unconfirmed and disconnected
        if not router_response:
            crud.save_disconnected_client(chat_id)
            send_message.delay(chat_id, Message.unavailable(client.source_ip))
            return JsonResponse({'msg': 'router not available'}, status=status)

        # send success message if all good
        send_message.delay(chat_id, Message.authorized(client.source_ip))

        return JsonResponse({'msg': 'client confirmed'})


class TimeCheckView(View):

    name = 'timecheck'

    def get(self, request: HttpRequest) -> JsonResponse:

        # check if there are exceeded(unconfirmed timeout) clients
        if exceeded_clients := crud.get_time_exceeded_clients():
            ips_to_disconnect = []
            for client in exceeded_clients:

                # client.connected = False
                # delete_confirm_button.delay(client.chat_id, client.last_confirm_message_id)
                ips_to_disconnect.append(client.caller_id)

            # disconnect them on router, change db state and delete button
            shell.disconnect_client.delay(ips_to_disconnect)
            # sql bulk update, much faster then change every instance in a loop
            # crud.bulk_update_clients(exceeded_clients, ['connected'])
            return JsonResponse({'msg': f'{len(exceeded_clients)} clients disconnected'})
        return JsonResponse({'msg': 'No disconnected clients'})


File: /app\Dockerfile
FROM python:3.8.2-slim

WORKDIR /usr/src/app
RUN mkdir static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk update && apk add postgresql-dev gcc make python3-dev musl-dev libffi-dev git
RUN apt-get update && apt-get install -y git netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

File: /app\entrypoint.sh
#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"


File: /app\helpers\crud.py
from datetime import timedelta
import os

import requests

from django.utils import timezone
from clients.models import Client
from django.db.models import QuerySet


MAX_UNCONFIRMED_CONNECTIONS = int(os.environ.get('MAX_UNCONFIRMED_CONNECTIONS'))
UNCONFIRMED_TIMEOUT = int(os.environ.get('UNCONFIRMED_TIMEOUT'))


def has_exceeded_connections(payload: dict) -> bool:
    chat_id = int(payload['chat_id'])
    if client := Client.objects.filter(chat_id=chat_id).first():
        if client.unconfirmed_connections_count > MAX_UNCONFIRMED_CONNECTIONS:
            return True
    return False


def save_connected_client(payload: dict) -> Client:
    chat_id = int(payload['chat_id'])
    client: Client or None = Client.objects.filter(chat_id=chat_id).first()
    if not client:
        client = Client()
    client.name = payload['name']
    client.chat_id = chat_id
    client.source_ip = payload['source_ip']
    client.caller_id = payload['caller_id']
    client.destination_ip = payload['destination_ip']
    client.connected = True
    client.last_connection_time = timezone.now()
    client.unconfirmed_connections_count += 1
    client.save()
    return client


def save_confirmed_client(chat_id: int) -> tuple:
    client: Client = Client.objects.filter(chat_id=chat_id).first()
    if not client:
        return (None, 404)
    if not client.connected:
        return (client, 422)
    client.confirmed = True
    client.unconfirmed_connections_count = 0
    client.save()
    return (client, 200)


def save_disconnected_client(chat_id: int, banned=False) -> Client or None:
    client: Client = Client.objects.filter(chat_id=chat_id).first()
    if not client:
        return None
    client.confirmed = False
    client.connected = False
    if banned:
        client.unconfirmed_connections_count = 0
    client.save()
    return client


def get_time_exceeded_clients() -> QuerySet:
    timeout = UNCONFIRMED_TIMEOUT
    time_border = timezone.now() - timedelta(minutes=timeout)
    exceeded_clients: QuerySet = (
        Client.objects
              .filter(last_connection_time__lt=time_border,
                      connected=True,
                      confirmed=False)
              .all()
    )
    return exceeded_clients


def save_message_id(chat_id: int, response: requests.Response) -> Client or None:
    answer = response.json()
    if answer['ok'] and answer.get('result'):
        message_id = answer['result']['message_id']

        client: Client = Client.objects.filter(chat_id=chat_id).first()
        client.last_confirm_message_id = message_id
        client.save()
        return client
    return None


def bulk_update_clients(clients: QuerySet, fields: list) -> None:
    Client.objects.bulk_update(clients, fields)


File: /app\helpers\request_templates.py
import json
import os

import requests

from celery import shared_task


BASE_URL = f'https://api.telegram.org/bot{os.environ.get("TOKEN")}'

if proxy_conn_string := os.environ.get('PROXY'):
    PROXIES = {
        'http': proxy_conn_string,
        'https': proxy_conn_string,
    }
else:
    PROXIES = None


class Message:
    @staticmethod
    def authorized(source_ip: str) -> str:
        return f'Your ip address {source_ip} authorized'

    @staticmethod
    def unavailable(source_ip: str) -> str:
        return f'Your ip address {source_ip} not authorized. \
            Either you are disconnected or router is unavailable. Try again later.'

    @staticmethod
    def unautorized() -> str:
        return 'You are not authorized.'

    @staticmethod
    def confirm_connection() -> str:
        return 'Are you trying connect to network?'

    @staticmethod
    def banned() -> str:
        return 'You are banned. Connections without confirmation exceeded.'

    @staticmethod
    def confirmation_time_exceeded() -> str:
        return 'Connection time without confirmation exceeded'

    @staticmethod
    def disconnected() -> str:
        return 'Your session has expired'


def get_updates(last_update_id: int) -> requests.Response or None:
    limit = 1
    offset = last_update_id + 1
    timeout = 100
    params = {'limit': limit, 'offset': offset, 'timeout': timeout}
    url = f'{BASE_URL}/getupdates'
    try:
        response = requests.get(url=url, params=params, proxies=PROXIES)
    except requests.ConnectionError:
        return None
    return response


@shared_task
def send_message(chat_id: int, message_text: str) -> requests.Response:
    params = {'text': message_text, 'chat_id': chat_id}
    url = f'{BASE_URL}/sendmessage'
    response = requests.get(url=url, params=params, proxies=PROXIES)
    return response.json()


def send_confirm_button(chat_id: int, payload: dict) -> requests.Response:
    message_text = Message.confirm_connection()
    button_text = 'Confirm'
    tg_data_keys = ('source_ip', 'destination_ip')
    truncated_payload = {key: value for key, value
                         in payload.items()
                         if key in tg_data_keys}
    reply_markup = {'inline_keyboard':
                    [[{'text': button_text, 'callback_data': str(truncated_payload)}]]}
    headers = {'content-type': 'application/json'}
    data = {'text': message_text, 'chat_id': chat_id, 'reply_markup': reply_markup}
    url = f'{BASE_URL}/sendmessage'
    response = requests.post(url=url, data=json.dumps(data), headers=headers, proxies=PROXIES)
    return response


def send_confirm_request(chat_id: int) -> requests.Response:
    headers = {'content-type': 'application/json'}
    data = {'chat_id': chat_id}
    url = 'http://nginx/clients/confirm/'
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    return response


@shared_task
def delete_confirm_button(chat_id: int, message_id: int) -> requests.Response:
    params = {'chat_id': chat_id, 'message_id': message_id}
    url = f'{BASE_URL}/deletemessage'
    response = requests.get(url=url, params=params, proxies=PROXIES)
    return response.json()


File: /app\helpers\shell.py
import os

from netmiko import ConnectHandler, NetmikoTimeoutException

from celery import shared_task


SSH_USERNAME = os.environ.get('SSH_USERNAME')
SSH_PASSWORD = os.environ.get('SSH_PASSWORD')
SSH_PORT = os.environ.get('SSH_PORT')
SSH_HOST = os.environ.get('SSH_HOST')

DENY_LIST = os.environ.get('DENY_LIST')
PERMIT_LIST = os.environ.get('PERMIT_LIST')
PERMANENT_BAN_LIST = os.environ.get('PERMANENT_BAN_LIST')
BAN_TIMEOUT = os.environ.get('BAN_TIMEOUT', '00:30:00')
VPN_SERVER = os.environ.get('VPN_SERVER')


def _configure_connection_settings() -> None:
    router = {
        'device_type': 'mikrotik_routeros',
        'host': SSH_HOST,
        'username': SSH_USERNAME,
        'password': SSH_PASSWORD,
        'port': SSH_PORT,
        'global_delay_factor': 2,
    }
    return router


def authorize_ip_address(source_ip: str) -> bool:
    router = _configure_connection_settings()
    try:
        ssh = ConnectHandler(**router)
    except NetmikoTimeoutException:
        return False

    ssh.send_command(f'ip firewall address-list remove [find address={source_ip} list={DENY_LIST}]')
    ssh.send_command(f'ip firewall address-list add list={PERMIT_LIST} address={source_ip} comment="vpn user"')
    ssh.disconnect()
    return True


def ban_ip_address(source_ip: str, caller_id: str) -> bool:
    router = _configure_connection_settings()
    try:
        ssh = ConnectHandler(**router)
    except NetmikoTimeoutException:
        return False

    ssh.send_command(f'ip firewall address-list remove [find address={source_ip} list={DENY_LIST}]')
    ssh.send_command(f'ip firewall address-list add list={PERMANENT_BAN_LIST} address={caller_id} timeout={BAN_TIMEOUT} comment="vpn user"')
    ssh.send_command(f'[/interface {VPN_SERVER}-server remove [find where client-address={caller_id}]]')
    ssh.disconnect()
    return True


def unban_ip_address(caller_id: str or list) -> bool:
    router = _configure_connection_settings()
    try:
        ssh = ConnectHandler(**router)
    except NetmikoTimeoutException:
        return False
    if isinstance(caller_id, list):
        for ip in caller_id:
            ssh.send_command(f'[/ip firewall address-list remove [find address={ip} list={PERMANENT_BAN_LIST}]]')
    else:
        ssh.send_command(f'[/ip firewall address-list remove [find address={caller_id} list={PERMANENT_BAN_LIST}]]')
    ssh.disconnect()
    return True


@shared_task
def disconnect_client(caller_id: str or list) -> bool:
    router = _configure_connection_settings()
    try:
        ssh = ConnectHandler(**router)
    except NetmikoTimeoutException:
        return False
    if isinstance(caller_id, list):
        for ip in caller_id:
            cmd = f'[/interface {VPN_SERVER}-server remove [find where client-address={ip}]]'
            ssh.send_command(cmd)
    else:
        cmd = f'[/interface {VPN_SERVER}-server remove [find where client-address={caller_id}]]'
        ssh.send_command(cmd)
    ssh.disconnect()
    return True


File: /app\manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


File: /app\requirements.txt
-i https://pypi.org/simple
amqp==2.6.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
asgiref==3.2.10; python_version >= '3.5'
bcrypt==3.1.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
billiard==3.6.3.0
celery==4.4.1
certifi==2020.6.20
cffi==1.14.1
chardet==3.0.4
cryptography==3.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
django==3.0.7
future==0.18.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'
gunicorn==20.0.4
idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
kombu==4.6.11; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
git+https://github.com/m3xan1k/netmiko#egg=netmiko
paramiko==2.7.1
psycopg2-binary==2.8.5
pycparser==2.20; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
pynacl==1.4.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
pyserial==3.4
pysocks==1.7.1
pytz==2020.1
redis==3.4.1
requests[socks]==2.24.0
scp==0.13.2
six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
sqlparse==0.3.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
textfsm==1.1.0
urllib3==1.25.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'
vine==1.3.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'


File: /app\timecheck.py
import requests


class TimeChecker:

    @staticmethod
    def run() -> None:
        url = 'http://nginx/clients/timecheck/'
        response = requests.get(url)
        return response


File: /app\watcher.py
from helpers.request_templates import (
    get_updates,
    send_confirm_request,
)


class Watcher:

    # parse telegram response to retrieve chat_id, update_id and callback data
    @staticmethod
    def parse_response(response: dict) -> dict:
        has_callback_data = False
        try:
            message = response['result'][0]['callback_query']['message']
            has_callback_data = True
        except KeyError:
            message = response['result'][0].get('message')
        if not message:
            return None
        chat_id = message['chat']['id']
        update_id = response['result'][0]['update_id']
        if has_callback_data:
            callback_data = message['reply_markup']['inline_keyboard'][0][0]['callback_data']
        else:
            callback_data = None
        return {
            'chat_id': chat_id,
            'update_id': update_id,
            'callback_data': callback_data,
        }

    @staticmethod
    def run() -> None:

        watcher = Watcher()
        last_update_id = 0

        # endless loop to watch chat updates
        while True:
            response = get_updates(last_update_id)
            if not response:
                continue

            # this may happen when token not provided
            if not response.status_code == 200:
                # TODO: logging or notification
                continue

            _json = response.json()

            if _json.get('ok') is True and _json['result']:
                parsed_response: dict = watcher.parse_response(_json)
                last_update_id = _json['result'][0]['update_id']
                if not parsed_response:
                    continue
                chat_id = int(parsed_response['chat_id'])

                # this may happen when user sends text message and not clicking button
                if not parsed_response['callback_data']:
                    # TODO: log?
                    continue

                # otherwise things must be ok and watcher triggers api to confirm client
                send_confirm_request(chat_id)


if __name__ == '__main__':
    Watcher.run()


File: /docker-compose.yml
version: '3'

services:
    web:
        build: ./app
        image: tik2fa-django:latest
        container_name: tik2fa_app
        command: gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers=2
        volumes:
            - ./app/:/usr/src/app/
            - static_volume:/usr/src/app/static
        expose:
            - 8000
        env_file: 
            - ./.env
        environment: 
            - DJANGO_ALLOWED_HOSTS=*
        restart: unless-stopped
        depends_on: 
            - db
            - celery-redis
    db:
        image: postgres:12.0-alpine
        container_name: tik2fa_db
        volumes:
            - postgres_data:/var/lib/postgresql/data/
        env_file: 
            - ./.env
        environment: 
            - POSTGRES_USER=${SQL_USER}
            - POSTGRES_PASSWORD=${SQL_PASSWORD}
            - POSTGRES_DB=${SQL_DATABASE}
    nginx:
        build: ./nginx
        container_name: tik2fa_nginx
        volumes: 
            - static_volume:/usr/src/app/static
        ports:
            - 80:80
        depends_on:
            - web
    celery-redis:
        image: redis:alpine
        container_name: tik2fa_redis
    celery:
        image: tik2fa-django:latest
        container_name: tik2fa_celery
        command: celery -A app worker -l info --concurrency=4
        volumes:
            - ./app/:/usr/src/app/
        env_file: 
            - ./.env
        environment: 
            - DJANGO_ALLOWED_HOSTS=*
        depends_on:
            - web
            - celery-redis
    celery-beat:
        image: tik2fa-django:latest
        container_name: tik2fa_celery_beat
        command: celery -A app beat -l info
        volumes:
            - ./app/:/usr/src/app/
        env_file: 
            - ./.env
        environment: 
            - DJANGO_ALLOWED_HOSTS=*
        depends_on:
            - web
            - celery-redis
    watcher:
        image: tik2fa-django:latest
        container_name: tik2fa_watcher
        command: python watcher.py
        env_file: 
            - ./.env
        restart: unless-stopped

volumes:
    postgres_data:
    static_volume:


File: /nginx\Dockerfile
FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d


File: /nginx\nginx.conf
upstream app {
    server web:8000;
}

server {

    listen 80;

    location / {
        proxy_pass http://app;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_redirect off;
        client_max_body_size 10M;
    }

    location /static/ {
        alias /usr/src/app/static/;
    }

}


File: /README.md
## Deploy instructions


1. Rename *you_need.env* to *.env* and fill config constants

2. Build and start containers(need docker and docker-compose to be installed)

```
docker-compose up -d
```

3. Apply migrations, create superuser to have access to django admin web interface, collect static(css/js)

```
docker exec -it tik2fa_app sh
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

4. Prepare router(need to automate this step):

- Make named access-lists
- Make and firewall rules for this lists
- Place up/down scripts for ppp profile
- Make specific user for this application
- Other security preparations
- Create and fill VPN accounts


---


### How it works


There are several processes/hosts that communicate and interact together:

- Client
- Router
- Django web API(hiddden behind NGINX + gunicorn) that does almost all logic
- Telegram updates watcher — just triggers API when client confirmes connection in chat
- Backgroud celery task — just triggers API to check for unconfirmed timeouts


---


### Few words about process roadmap


1. Client connects to VPN service

2. Connection triggers script that does:
- Moves source ip address of client to DENY_LIST(sandbox)
- Sends request to API */client/connect/* endpoint with payload that contains **source ip**, **destination ip** and **chat id**

3. Backend makes:
- verification that client has not exceed unconfirmed connections limit
    - sends "ban" command to router and client's ip moves to permanent ban list on router
- either creates new client or edits existed client instance
- sends confirmation button to client's chat

4. Watcher listens(or watches(lol)) telegram updates and here are few scenarios:
- client clicks button and wathcer sends confirm request to API(move next step)
- client waits too long, button will be removed and client will be disconnected from router by background celery task, that triggers API's */client/timecheck/* endpoint and backend does all the work

5. Backend checks if client is connected:
- If true — client is confirmed, backend triggers router to move client to PERMIT_LIST(allow)
- If disconnected — notifies about this fact in chat
- If router is unavailable — notifies about this too

6. When client disconnects from router, script does:
- remove client's ip from PERMIT_LIST
- send request to API to change client's status


---


### TODO

- [x] tests


---


File: /routeros_scripts\ppp_profile_behavior.rsc

# on up

{
    :local name ($"user");
	:local sourceIp ($"remote-address");
    :local destinationIp ($"local-address");
    :local denyList "sandboxed";
    :local callerId ($"caller-id");
    
    :log info $sourceIp;
    :log info $destinationIp;
    :log info $denyList;
    
    :local chatId [/ppp secret get [find name=$user] comment];
    :local endpointUrl "http://192.168.88.254/clients/connect/"
    
    :local payload "{\"name\": \"$name\", \"chat_id\": \"$chatId\", \"source_ip\": \"$sourceIp\", \"destination_ip\": \"$destinationIp\", \"caller_id\": \"$callerId\"}";
    
    [/ip firewall address-list add list=$denyList address=$sourceIp comment="vpn user"];
    
    [/tool fetch url=$endpointUrl http-header-field="content-type:application/json" http-method=post http-data=$payload];
    
}

# on down

{

	:local sourceIp ($"remote-address");
    :local destinationIp ($"local-address");
    :local denyList "sandboxed";
    :local permitList "allowed";
    :local chatId [/ppp secret get [find name=$user] comment];
    :local endpointUrl "http://192.168.88.254/clients/disconnect/"
    
    :local payload "{\"chat_id\": \"$chatId\", \"source_ip\": \"$sourceIp\", \"destination_ip\": \"$destinationIp\", \"caller_id\": \"$callerId\"}";
    
    [ip firewall address-list remove [find address=$sourceIp list=$permitList]];
    
    [ip firewall address-list remove [find address=$sourceIp list=$denyList]];

    [/tool fetch url=$endpointUrl http-header-field="content-type:application/json" http-method=post http-data=$payload];
    
}


File: /you_need.env
# django sensitive data
DEBUG=0
SECRET_KEY=your_django_app_secret_key

# db settings
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=db_name
SQL_USER=db_user
SQL_PASSWORD=db_password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

# tg token
TOKEN=tg_token

#VPN server type. ovpn for OpenVPN, l2tp for (guess!) L2TP-server
VPN_SERVER=ovpn

# proxy conn string (if you need it)
#PROXY=socks_proxy_url_string

# for netmiko
SSH_HOST=router_address
SSH_USERNAME=router_ssh_username
SSH_PASSWORD=router_ssh_password
SSH_PORT=22

# temporary block user until confirmed
DENY_LIST=2FA_sandboxed

# for confirmed users
PERMIT_LIST=2FA_allowed

# ban when connection number exceeds
PERMANENT_BAN_LIST=2FA_banned

# minutes
UNCONFIRMED_TIMEOUT=1

# ban limitations
MAX_UNCONFIRMED_CONNECTIONS=10

