# Repository Information
Name: FurMikrotik-bot

# Directory Structure
Directory structure:
└── github_repos/FurMikrotik-bot/
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
    │   │       ├── pack-9ddf0c9408cdbeda4b18081a786f99aee37e93fb.idx
    │   │       └── pack-9ddf0c9408cdbeda4b18081a786f99aee37e93fb.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── CHANGELOG-EN.md
    ├── CHANGELOG-ID.md
    ├── LICENSE
    ├── README.md
    ├── script text/
    │   ├── func_fetch
    │   ├── func_lowercase
    │   ├── func_uppercase
    │   ├── tg_cmd_capitalize
    │   ├── tg_cmd_corona
    │   ├── tg_cmd_currency
    │   ├── tg_cmd_define
    │   ├── tg_cmd_definisi
    │   ├── tg_cmd_help
    │   ├── tg_cmd_install
    │   ├── tg_cmd_ipcalc
    │   ├── tg_cmd_jokes
    │   ├── tg_cmd_lookup
    │   ├── tg_cmd_lowercase
    │   ├── tg_cmd_ping
    │   ├── tg_cmd_quran
    │   ├── tg_cmd_quran2
    │   ├── tg_cmd_randomcase
    │   ├── tg_cmd_randomize
    │   ├── tg_cmd_shalat
    │   ├── tg_cmd_shorten
    │   ├── tg_cmd_update
    │   ├── tg_cmd_uppercase
    │   ├── tg_config
    │   ├── tg_getkey
    │   ├── tg_getUpdates
    │   ├── tg_sendAudio
    │   └── tg_sendMessage
    ├── setup.rsc
    └── util/
        ├── availableCommand
        ├── listSurahQuran
        └── randomizeScript


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
	url = https://github.com/furaihan/FurMikrotik-bot.git
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
0000000000000000000000000000000000000000 3972385aedc1f65eca09d835680902db4d3ed329 vivek-dodia <vivek.dodia@icloud.com> 1738606047 -0500	clone: from https://github.com/furaihan/FurMikrotik-bot.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 3972385aedc1f65eca09d835680902db4d3ed329 vivek-dodia <vivek.dodia@icloud.com> 1738606047 -0500	clone: from https://github.com/furaihan/FurMikrotik-bot.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3972385aedc1f65eca09d835680902db4d3ed329 vivek-dodia <vivek.dodia@icloud.com> 1738606047 -0500	clone: from https://github.com/furaihan/FurMikrotik-bot.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3972385aedc1f65eca09d835680902db4d3ed329 refs/remotes/origin/master
f82a3e2c46982a93a8e1b920ed5522ce65802be3 refs/remotes/origin/per-script-version
2541f9cce423b0a9ca87208ab0e4f29e0f98faaa refs/tags/1.0.0


File: /.git\refs\heads\master
3972385aedc1f65eca09d835680902db4d3ed329


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /CHANGELOG-EN.md
## 1.0.0
* Initial Release

File: /CHANGELOG-ID.md
## 1.0.0
* Versi Pertama

File: /LICENSE
MIT License

Copyright (c) 2020 Zhafar Al Fathi

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
# FurMikrotik Bot
Pada dasarnya kegunaan script ini adalah untuk menjadikan router mikrotik kita sebagai server dari telegram bot
karena saya tidak bisa membeli server untuk menjalankan bot telegram maka saya membuat ini sebagai alternatif,
script ini memiliki banyak fungsi yang bisa digunakan untuk membantu kita sehari-hari, contohnya perintah `/corona`
bisa digunakan untuk mengetahui data pasien corona di dunia, dan masih banyak perintah bermanfaat lainnya

---

## Instalasi
Untuk menginstal script ini anda butuh token telegram bot serta ChatID akun telegram anda, untuk cara membuat telegram bot bisa dicari di internet.
Setelah mendapatkan token bot telegram dan ChatID nya, lalu ikuti step dibawah ini

1. Download file setup.rsc
2. Import file setup.rsc kedalam mikrotik dengan cara drag and drop melalui winbox atau menggunakan aplikasi tambahan seperti FileZilla atau WinSCP
3. Buka terminal MikroTik anda dan copy paste perintah ini: `/import file-name=setup.rsc`
4. Arahkan winbox ke System >> Script >> tg_config, lalu konfigurasikan sesuai dengan yang anda miliki dengan mengikuti penjelasan [disini](#penjelasan-konfigurasi-tg_config)

### Penjelasan Konfigurasi tg_config
* `"botAPI"="xxxxxxxxxxxxxx:xxxxxxxxxx";` ganti dengan bot token anda
* `"defaultChatID"="xxxxxxxxxx";` ganti dengan ChatID milik anda
* `"trusted"="xxxxxxx, xxxxxxxx, xxxxxxxx";` ini adalah daftar akun telegram yang menjadi admin bot, diisi dengan ChatID per user
* `"storage"="";` ini adalah konfigurasi tempat menyimpan file file telegram. Saran saya biarkan default
* `"timeout"=5;` yang ini juga biarkan default
* `"refresh_active"=15;` yang ini juga biarkan default
* `"refresh_standby"=300;` yang ini juga biarkan default
* `"available_for_public"=true;` apabila anda ingin bot anda bisa diakses seluruh pengguna telegram maka biarkan `true`, jika tidak silahkan ganti `false`

## Daftar perintah
| Perintah | Fungsi | Contoh |
| -------- | ------ | ------ |
| ``/help`` |  Menampilkan daftar perintah yang tersedia | ``/help`` |
| ``/install`` |  Menginstall perintah | `/install jokes` |
| ``/update`` |  Mengupdate perintah | `/update jokes` |

## Catatan
* Untuk menampilkan daftar perintah lengkap gunakan fitur /help pada telegram bot anda
* Untuk menampilkan penjelasan perintah silahkan menggunakan `/perintah help`. contoh apabila anda ingin menampilkan penjelasan untuk perintah `jokes` maka ketikkan `/jokes help`

## Changelog / Catatan Perubahan
* [INDONESIA](CHANGELOG-ID.md)
* [ENGLISH](CHANGELOG-EN.md)

## Special Thanks
Special thanks to 
* [BlackVS](https://github.com/BlackVS/Mikrotik-scripts/tree/master/scripts/Telegram%20bot%20for%20Mikrotik) for creating Mikrotik and telegram script
* All member who help me in [Forum Mikrotik](https://forum.mikrotik.com/index.php)


File: /script text\func_fetch
#########################################################
# Wrapper for /tools fetch
#  Input:
#    mode
#    upload=yes/no
#    user
#    password
#    address
#    host
#    httpdata
#    httpmethod
#    check-certificate
#    src-path
#    dst-path
#    ascii=yes/no
#    url
#    resfile

:local res "fetchresult.txt"
:if ([:len $resfile]>0) do={:set res $resfile}
#:put $res

:local cmd "/tool fetch"
:if ([:len $mode]>0) do={:set cmd "$cmd mode=$mode"}
:if ([:len $upload]>0) do={:set cmd "$cmd upload=$upload"}
:if ([:len $user]>0) do={:set cmd "$cmd user=\"$user\""}
:if ([:len $password]>0) do={:set cmd "$cmd password=\"$password\""}
:if ([:len $address]>0) do={:set cmd "$cmd address=\"$address\""}
:if ([:len $host]>0) do={:set cmd "$cmd host=\"$host\""}
:if ([:len $"http-data"]>0) do={:set cmd "$cmd http-data=\"$"http-data"\""}
:if ([:len $"http-method"]>0) do={:set cmd "$cmd http-method=\"$"http-method"\""}
:if ([:len $"check-certificate"]>0) do={:set cmd "$cmd check-certificate=\"$"check-certificate"\""}
:if ([:len $"src-path"]>0) do={:set cmd "$cmd src-path=\"$"src-path"\""}
:if ([:len $"dst-path"]>0) do={:set cmd "$cmd dst-path=\"$"dst-path"\""}
:if ([:len $ascii]>0) do={:set cmd "$cmd ascii=\"$ascii\""}
:if ([:len $url]>0) do={:set cmd "$cmd url=\"$url\""}

:put ">> $cmd"

:global FETCHRESULT
:set FETCHRESULT "none"

:local script "\
 :global FETCHRESULT;\
 :do {\
   $cmd;\
   :set FETCHRESULT \"success\";\
 } on-error={\
  :set FETCHRESULT \"failed\";\
 }\
"
:execute script=$script file=$res
:local cnt 0
#:put "$cnt -> $FETCHRESULT"
:while ($cnt<100 and $FETCHRESULT="none") do={ 
 :delay 1s
 :set $cnt ($cnt+1)
 #:put "$cnt -> $FETCHRESULT"
}
:local content [/file get [find name=$res] content]
#:put $content
if ($content~"finished") do={:return "success"}
:return $FETCHRESULT

File: /script text\func_lowercase
:local alphabet {"A"="a";"B"="b";"C"="c";"D"="d";"E"="e";"F"="f";"G"="g";"H"="h";"I"="i";"J"="j";"K"="k";"L"="l";"M"="m";"N"="n";"O"="o";"P"="p";"Q"="q";"R"="r";"S"="s";"T"="t";"U"="u";"V"="v";"X"="x";"Z"="z";"Y"="y";"W"="w"};
:local result
:local character
:for strings from=0 to=([:len $1] - 1) do={
	:local single [:pick $1 $strings]
	:set character ($alphabet->$single)
	:if ([:typeof $character] = "str") do={set single $character}
	:set result ($result.$single)
}
:return $result


File: /script text\func_uppercase
:local alphabet {"a"="A";"b"="B";"c"="C";"d"="D";"e"="E";"f"="F";"g"="G";"h"="H";"i"="I";"j"="J";"k"="K";"l"="L";"m"="M";"n"="N";"o"="O";"p"="P";"q"="Q";"r"="R";"s"="S";"t"="T";"u"="U";"v"="V";"x"="X";"z"="Z";"y"="Y";"w"="W"};
:local result
:local character
:for strings from=0 to=([:len $1] - 1) do={
    :local single [:pick $1 $strings]
    :set character ($alphabet->$single)
    :if ([:typeof $character] = "str") do={set single $character}
    :set result ($result.$single)
}
:return $result

File: /script text\tg_cmd_capitalize
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local toupper [:parse [/system script get func_uppercase source]]

:local paramsLower [$tolower $params]

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
    :local helptext ("%3D%3D%3D%3D%3D%3D%3D%20CAPITALIZE%20%3D%3D%3D%3D%3D%3D%3D%0A%0A")
	:local helptext ($helptext."Hi $from, With this tool you can automatize capitalize and convert the given text title case%0A%0A")
	:local helptext ($helptext."*USAGE:*%0A")
	:local helptext ($helptext."/capitalize _<text>_%0A%0A")
	:local helptext ($helptext."*EXAMPLE*%0A")
	:local helptext ($helptext."/capitalize _hello world_%0A%0A")
	:local helptext ($helptext."*The output should be:*%0A")
	:local helptext ($helptext."Hello World%0A%0A")
	:local helptext ($helptext."*NOTE:*%0A")
	:local helptext ($helptext."> you can use many words as you want, but please dont spam this command too frequently%0A")
	:local helptext ($helptext."> if possible, please dont use any punctuation mark. That will cause script not work properly%0A")
	$send chat=$chatid text=("$helptext") mode="Markdown"
}

:if (($paramsLower = "help") or ([:len $params] = 0)) do={$sendHelp from=$from chatid=$chatid; :return -1}

:local result
:if (([:len $params] > 0) and ([:typeof [:tostr $params]] = "str")) do={
	:local pos 0
	:for i from=0 to=([:len $paramsLower] - 1) do={
		:set pos ($pos + 1)
		:local char [:pick $paramsLower $i];
		:local determine [:pick $paramsLower ($i -1)];
		:if (($pos = 1) or ($determine = " ")) do={
			:set char [$toupper $char];
		}
		:set result ($result.$char);
	}
	:if ([:len $result] < 2) do={$sendHelp from=$from chatid=$chatid; :return -1}
	$send chat=$chatid text=$result;
}

File: /script text\tg_cmd_corona
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}

:local urlEncode do={
  :local Input [ :tostr $1 ];
  :local Return "";

  :if ([ :len $Input ] > 0) do={
    :local Chars " !\"#\$%&'()*+,:;<=>\?@[\\]^`{|}~-";
    :local Subs { "%20"; "%21"; "%22"; "%23"; "%24"; "%25"; "%26"; "%27"; "%28"; "%29";
                  "%2A"; "%2B"; "%2C"; "%3A"; "%3B"; "%3C"; "%3D"; "%3E"; "%3F"; "%40";
                  "%5B"; "%5C"; "%5D"; "%5E"; "%60"; "%7B"; "%7C"; "%7D"; "%7E"; "%20" };

    :for I from=0 to=([ :len $Input ] - 1) do={
      :local Char [ :pick $Input $I ];
      :local Replace [ :find $Chars $Char ];

      :if ([ :len $Replace ] > 0) do={
        :set Char ($Subs->$Replace);
      }
      :set Return ($Return . $Char);
    }
  }
	:return $Return;
}

:local paramsLower [$tolower $params]
:put $paramsLower

:local alternativeMention {"united states of america"="usa"; "saudi"="saudi arabia"; "uk"="united kingdom"; "wales"="united kingdom"; "england"="united kingdom"; "scotland"="united kingdom"; "america"="usa"}
:if ([:typeof ($alternativeMention -> $paramsLower)] = "str") do={:set paramsLower ($alternativeMention -> $paramsLower)}
:put $paramsLower

:local paramsEncode [$urlEncode $paramsLower]
:put $paramsEncode

:local ConvertUpperCase do={
	:local alphabet {"a"="A";"b"="B";"c"="C";"d"="D";"e"="E";"f"="F";"g"="G";"h"="H";"i"="I";"j"="J";"k"="K";"l"="L";"m"="M";"n"="N";"o"="O";"p"="P";"q"="Q";"r"="R";"s"="S";"t"="T";"u"="U";"v"="V";"x"="X";"z"="Z";"y"="Y";"w"="W"};
	:local result;
	:local character;
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings];
		:set character ($alphabet->$single);
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single);
	}
	:return $result
}

:if ($paramsLower = "help") do={
:local helptext ("Covid 19 spread, infection and recovery information%0A%0A")
:set helptext ($helptext."*Usage*:%0A")
:set helptext ($helptext."/corona _<country>_%0A%0A")
:set helptext ($helptext."*Example*:%0A")
:set helptext ($helptext."/corona _bosnia-and-herzegovina_%0A")
:set helptext ($helptext."/corona _indonesia_%0A%0A")
:put $helptext
$send chat=$chatid text=$helptext mode="Markdown"
}

:if ( ([:len $params] > 0) and ($paramsLower != "help") ) do={
	:do {
		:local dataCovid ([/tool fetch mode=https url="https://covid19.mathdro.id/api/countries/$paramsEncode/" output=user as-value]->"data");
		:local confirmedCases [$gkey block="confirmed" key="value" text=$dataCovid];
		:local recovered [$gkey block="recovered" key="value" text=$dataCovid];
		:local deaths [$gkey block="deaths" key="value" text=$dataCovid];
		:local activeCases ([:tonum $confirmedCases] - [:tonum $recovered] - [:tonum $deaths]);
		:local sendThisText ("*COVID 19 PANDEMIC IN $[$ConvertUpperCase $params]*%0A%0A");
		:set sendThisText ($sendThisText."*Confirmed Case*: $[:tonum $confirmedCases]%0A");
		:set sendThisText ($sendThisText."*Recovered*: $[:tonum $recovered]%0A");
		:set sendThisText ($sendThisText."*Deaths*: $[:tonum $deaths]%0A");
		:set sendThisText ($sendThisText."*Active Cases*: $[:tonum $activeCases]%0A");
		:if ([:len $confirmedCases] > 0) do={
			$send chat=$chatid text=$sendThisText mode="Markdown"
		} else={
			$send chat=$chatid text=("Sorry pal, we cannot find any data in $params") mode="Markdown"
		}
	} on-error={
		$send chat=$chatid text="Unknown error occurred, please try again later" mode="Markdown"
	}
} else={
	:if ($paramsLower != "help") do={
		:local dataCovid ([/tool fetch mode=https url="https://api.covid19api.com/world/total" output=user as-value]->"data");
		:put $dataCovid
		:local confirmedCases [$gkey key="TotalConfirmed" text=$dataCovid];
		:local deaths [$gkey key="TotalDeaths" text=$dataCovid];
		:local recovered [:pick $dataCovid ([:find $dataCovid "TotalRecovered"]+ [:len "TotalRecovered"] + 2) ([:len $dataCovid] - 2)];
		:put $recovered
		:local activeCases ([:tonum $confirmedCases] - [:tonum $recovered] - [:tonum $deaths]);
		:local sendThisText ("*COVID 19 PANDEMIC IN WORLDWIDE*%0A%0A");
		:set sendThisText ($sendThisText."*Confirmed Case*: $[:tonum $confirmedCases]%0A");
		:set sendThisText ($sendThisText."*Recovered*: $[:tonum $recovered]%0A");
		:set sendThisText ($sendThisText."*Deaths*: $[:tonum $deaths]%0A");
		:set sendThisText ($sendThisText."*Active Cases*: $[:tonum $activeCases]%0A");
		$send chat=$chatid text=$sendThisText mode="Markdown"
	}
}


File: /script text\tg_cmd_currency
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local toupper [:parse [/system script get func_uppercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}


:local paramsLower [$tolower $params];
:local param1Lower [$tolower $param1];
:local param2Lower [$tolower $param2];
:local param3Lower [$tolower $param3];
:local param2Upper [$toupper $param2];
:local param1Upper [$toupper $param1];

:local encode do={
    :local subs {","="%0A"; "\""=" "; ":"=" --> "}
	:local result
	:local character
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings]
		:set character ($subs->$single)
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single)
	}
	:return $result
}
:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
    :local txt ("Hey $from%2C%0A")
    :set txt ($txt."Use this command to calculate live currency from [Frankfurter App](https://www.frankfurter.app/)%0A%0A")
    :set txt ($txt."*USAGE:*%0A")
    :set txt ($txt."/currency <from> <to> <amount>%0A%0A")
    :set txt ($txt."*EXAMPLE:*%0A")
    :set txt ($txt."/currency _usd sgd 20_ (this will convert 20 USD to SGD)%0A%0A")
    :set txt ($txt."*NOTE: *%0A")
    :set txt ($txt."> To see the list of supported currencies just type /currency list%0A")
    :set txt ($txt."> If you dont specify amount, its default value will be 1%0A")
    $send chat=$chatid text=$txt mode="Markdown"
}

:local url ("https://api.frankfurter.app/latest\?from=$param1Upper&to=$param2Upper")
:local listCurrency [:toarray ("aud", "bgn", "brl", "cad", "chf", "cny", "czk", "dkk", "eur", "gbp", "hkd", "hrk", "huf",\
                             "idr", "ils", "inr", "isk", "jpy", "krw", "mxn", "myr", "nok", "nzd", "php", "pln", "ron", "rub",\
                             "sek", "sgd", "thb", "try", "usd", "zar")]

:if ($paramsLower = "list") do={
    :local fetchCurrencies ([/tool fetch url="https://api.frankfurter.app/currencies" output=user as-value]->"data")
    :local supportedCurrencies [:pick $fetchCurrencies 1 ([:len $fetchCurrencies] - 1)]
    :local text ("List of supported currencies:%0A%0A$[$encode $supportedCurrencies]")
    $send chat=$chatid text=$text
    :return true
}

:if ($paramsLower = "help") do={$sendHelp from=$from chatid=$chatid; :return true}

:if ([:len $params] > 0) do={
    :local valid (([:typeof [:find $listCurrency $param1Lower]] != "nil") and ([:typeof [:find $listCurrency $param2Lower]] != "nil"))
    :if ($valid) do={
        :local amountValid (([:len $param3] > 0) and ([:typeof [:tonum $param3]] = "num") and ([:tonum $param3] > 0))
        :if ($amountValid) do={ :set url ($url."&amount=$param3Lower")}
        :put $url
        :local fetchData ([/tool fetch url=$url output=user as-value]->"data")
        :local afterConversion [:pick $fetchData ([:find $fetchData $param2Upper] + 5) ([:len $fetchData] - 2)]
        :local sendThisText ("*Conversion Result:%0A*")
        :if ($amountValid) do={:set $sendThisText ($sendThisText."$param3 ")} else={:set $sendThisText ($sendThisText."1 ")}
        :set sendThisText ($sendThisText."$param1Upper equal to $afterConversion $param2Upper")
        $send chat=$chatid text=$sendThisText mode="Markdown"
    } else={
        :if ([:typeof [:find $listCurrency $paramsLower]] != "nil") do={$sendHelp from=$from; :return true}
        :local currencyInvalid ("Hey $from, currently $param1 ")
        :if ([:len $param2] > 0) do={:set currencyInvalid ($currencyInvalid."and $param2 ");}
        :set currencyInvalid ($currencyInvalid."is not yet supported")
        $send chat=$chatid text=$currencyInvalid
    }
} else={
    $sendHelp from=$from chatid=$chatid;
}


File: /script text\tg_cmd_define
:local send [:parse [/system script get tg_sendMessage source]]
:local sendaudio [:parse [/system script get tg_sendAudio source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}

:put $params
:put $param1
:put $param2
:put $param3
:put $chatid
:put $from

:local ConvertUpperCase do={
	:local alphabet {"a"="A";"b"="B";"c"="C";"d"="D";"e"="E";"f"="F";"g"="G";"h"="H";"i"="I";"j"="J";"k"="K";"l"="L";"m"="M";"n"="N";"o"="O";"p"="P";"q"="Q";"r"="R";"s"="S";"t"="T";"u"="U";"v"="V";"x"="X";"z"="Z";"y"="Y";"w"="W"};
	:local result;
	:local character;
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings];
		:set character ($alphabet->$single);
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single);
	}
	:return $result
}


:local paramsLower [$tolower $params]

:if ($paramsLower = "help") do={
	$send chat=$chatid text="%3D%3D%3D%3D%3D%3D%3D%3D%3D%20DEFINE%20%3D%3D%3D%3D%3D%3D%3D%3D%3D%0AUsed%20to%20define%20a%20given%20word.%20Definition%20taken%20from%20Google%20Dictionary%20(https%3A%2F%2Fgithub.com%2FmeetDeveloper%2FgoogleDictionaryAPI)%0A%0AUse%3A%0A%2Fdefine%20word%0AExample%3A%0A%2Fdefine%20supercalifragilisticexpialidocious%0A%0ANote%3A%0A%3E%20This%20feature%20still%20has%20many%20bugs%2C%20due%20to%20limitations%20in%20scripting%20in%20RouterOS%0A%3E%20You%20cannot%20(yet)%20define%20a%20phrase%20containing%20two%20or%20more%20words"

}
:if ([:len $params] > 0) do={
	:if ( ([:typeof [:tostr $params]] = "str") and ([:len $param1] = 1) and ($paramsLower != "help") ) do={
		:do {
			:local khak ([/tool fetch http-header-field="content-type: application/json" url="https://api.dictionaryapi.dev/api/v2/entries/en/$params" output=user as-value ]->"data");
			:put khak;
			:local pron [$gkey key="audio" text=$khak];
			:local def [$gkey block=definitions key=definition text=$khak];
			:local cth [$gkey block=definitions key=example text=$khak];
			:local typ [$gkey block=meanings key=partOfSpeech text=$khak];
			:local mptri ([pick $pron ([find $pron "\""]+1) [find $pron ".mp3"]].".mp3");
			:local defitext;
			:set defitext ("*$[$ConvertUpperCase $params]*%0A%0A");
			:if ([:len $def] > 0) do={:set defitext ($defitext."$def%0A%0A"); }
			:if ([:len $typ] > 0) do={ :set defitext ($defitext."Parts of Speech: _$typ_ %0A"); }
			:if ([:len $cth] > 0) do={ :set defitext ($defitext."Example: $cth%0A"); }
			:if ([:len $typ] > 0) do={
				$send chat=$chatid text=("$defitext") mode="Markdown"
			} else={
				$send chat=$chatid text="Sorry%20pal%2C%20we%20couldn't%20find%20definitions%20for%20the%20word%20you%20were%20looking%20for"
			}
			:if ([:len $params] > 9) do={
				:put $mptri
				$sendaudio chat=$chatid audio=("$mptri")
			}
		} on-error={
			:local ertext ("*unknown error occurred*%0A");
			:local ertext ($ertext."Please try again later%0A%0A");
			:local ertext ($ertext."_Please be advised that this tool is still have some bugs due to Mikrotik RouterOS limitation itself, you can try this again but if you keep getting an error you can try to use another word_");
			$send chat=$chatid text=("$ertext") mode="Markdown"
		}
	} else={
		:if ($paramsLower != "help") do={
			$send chat=$chatid text=("$params%20cannot%20be%20defined%2C%20please%20type%20%2Fdefine%20help%20for%20more%20information") mode="Markdown"
		}
	}
} else={
	$send chat=$chatid text=("Actually, you need somethind to be defined, type */define help* for more information") mode="Markdown"
}


File: /script text\tg_cmd_definisi
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}


:local ConvertUpperCase do={
	:local alphabet {"a"="A";"b"="B";"c"="C";"d"="D";"e"="E";"f"="F";"g"="G";"h"="H";"i"="I";"j"="J";"k"="K";"l"="L";"m"="M";"n"="N";"o"="O";"p"="P";"q"="Q";"r"="R";"s"="S";"t"="T";"u"="U";"v"="V";"x"="X";"z"="Z";"y"="Y";"w"="W"};
	:local result
	:local character
	:for strings from=0 to=([:len $1] - 1) do={
		:local single [:pick $1 $strings]
		:set character ($alphabet->$single)
		:if ([:typeof $character] = "str") do={set single $character}
		:set result ($result.$single)
	}
	:return $result
}

:if ($params = "help") do={
	:local bantuan
	:set bantuan ("*Perintah Definisi*%0A")
	:set bantuan ($bantuan."Digunakan untuk mendefinisikan sebuah kata yang diberikan. Definisi diambil dari web [Kateglo](http://kateglo.com/) yang bersumber dari KBBI%0A%0A")
	:set bantuan ($bantuan."*Penggunaan: *%0A")
	:set bantuan ($bantuan."_/definisi <kata>_%0A")
	:set bantuan ($bantuan."Contoh: ``` /definisi hujan ```%0A%0A")
	:set bantuan ($bantuan."*Catatan: *%0A")
	:set bantuan ($bantuan.">	Fitur ini masih memiliki banyak bug, karena keterbatasan dalam penulisan skrip di RouterOS%0A")
	:set bantuan ($bantuan.">	Silahkan ketikkan kata yang didefinisikan dalam satu kata%0A%0A")
	:set bantuan ($bantuan."*Known Bugs:*%0A")
	:set bantuan ($bantuan.">	Apabila definisi dari kata yang diberikan terdapat tanda baca koma (,)maka yang akan dikirim di telegram adalah seluruh kalimat sebelum tanda koma tersebut%0A")
	:set bantuan ($bantuan.">	Tidak bisa mendefinisikan dua kata atau lebih seperti: _tanggung jawab, bumi hanguskan, bercerai berai, dll_%0A")
	$send chat=$chatid text=("$bantuan") mode="Markdown"
}

:if ( ([:typeof [:tostr $params]] = "str") and ([:len $param1] = 1) and ($params != "help") ) do={
	:do {
		:local a ([/tool fetch mode=http http-method=get url="http://kateglo.com/api.php\?format=json&phrase=$params" as-value output=user ]->"data");
		:local def [$gkey block="definition" key="def_text" text=$a];
		:local sample [$gkey block="definition" key="sample" text=$a];
		:local kat [$gkey block="kateglo" key="lex_class_name" text=$a];
		:local pepatah [$gkey block="proverbs" key="proverb" text=$a];
		:local pptmean [$gkey block="proverbs" key="meaning" text=$a];
		:put $def; put $kat; put $pepatah;
		:local paramsuppercase [$ConvertUpperCase $params]
		:local deftext;
		:set deftext ("* $paramsuppercase *%0A");
		:set deftext ($deftext."Jenis: $kat%0A");
		:set deftext ($deftext."Definisi: $def%0A");
		:if ( ($sample != "null") and ([:len $sample] > 0) ) do={ :set deftext ($deftext."Sampel: $sample%0A"); }
		:if ([:len $pepatah] > 0) do={ :set deftext ($deftext."Pepatah: _$pepatah_ ($pptmean)%0A")}
		:if ([:len $kat] > 0) do={
			$send chat=$chatid text=("$deftext") mode="Markdown"
		} else={
			$send chat=$chatid text=("Definisi $params tidak ditemukan") mode="Markdown"
		}
	} on-error={
		:local ertext ("*unknown error occurred*%0A");
		:local ertext ($ertext."Please try again later%0A%0A");
		:local ertext ($ertext."_Please be advised that this tool is still have some bugs due to Mikrotik RouterOS limitation itself, you can try this again but if you keep getting an error you can try to use another word_");
		$send chat=$chatid text=("$ertext") mode="Markdown"
	}
} else={
	:if ($params != "help") do={
		$send chat=$chatid text=("$params tidak bisa di-definisikan, silahkan ketik ``` /definisi help ``` untuk informasi lebih lanjut") mode="Markdown"
	}
}


File: /script text\tg_cmd_help
:local send [:parse [/system script get tg_sendMessage source]]


:local helpBody;
:set helpBody ("Hi, $from%0ALorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt \
                ut labore et dolore magna aliqua. Ut enim ad minim veniam%0A%0AAvailable Commands:%0A")

:foreach script in=[/system script find where name~"tg_cmd_"] do={
    :local name [/system script get $script name]
    :local command [:pick $name 7 [:len $name]]
    :set helpBody ($helpBody."/$command%0A")
}
:set helpBody ($helpBody."%0ANote:%0A> For detailed command help type: <command> help%0A\
                > *install* and *update* command is only available for bot admin")
$send chat=$chatid text=$helpBody mode="Markdown";


File: /script text\tg_cmd_install
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local fconfig [:parse [/system script get tg_config source]]
:local config [$fconfig]

:local trusted [:toarray ($config->"trusted")]
:local allowed ([:type [:find $trusted $chatid]] != "nil")
:if (!$allowed) do={
 :put "Unknown sender, keep silence"
 :return -1
}

:local paramsLower [$tolower $params];
:local fetchCommand ([/tool fetch url="https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/util/availableCommand" output=user as-value]->"data")
:local availableCommand [:toarray $fetchCommand]

:local sendHelp do={
	:local send [:parse [/system script get tg_sendMessage source]]
    :local txt ("Hi, $from%0AUse this command to install a script%0A\
                *Usage:*%0A/install <command>%0A*Example:*%0A/install _jokes_%0A\
                *Note:*%0Ato see the available script just type /install list");
    $send chat=$chatid text=$txt mode="Markdown";
}

:if ($paramsLower = "list") do={
	:local listScript ("List of available script%0A%0A")
	:local number 0
	:for i from=0 to=([:len $availableCommand] - 1) do={
		:local command [:pick $availableCommand $i]
		:set number ($number + 1)
		:set listScript ($listScript."$number. $command%0A")
	}
	:set listScript ($listScript."%0Ato install a command just type /install <command>. For example%0A/install jokes")
	$send chat=$chatid text=$listScript mode="Markdown"; :return -1
}

:if ($paramsLower = "help") do={
	$sendHelp from=$from chatid=$chatid; :return -1
}

:local valid ([:typeof [:find $availableCommand $paramsLower]] != "nil")
:if ($valid) do={
	:local scriptName ("tg_cmd_$paramsLower")
	:if ([:len [/system script find where name=$scriptName]] > 0) do={
		$send chat=$chatid text=("$scriptName script has been installed, if you want to update the script, use /update instead");
		:return -1
	}
	:local scriptUrlInstall ("https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/script%20text/$scriptName")
	:do {
		:local scriptSource ([/tool fetch url=$scriptUrlInstall output=user as-value]->"data")
		/system script add name=$scriptName policy=read source=$scriptSource
		$send chat=$chatid text=("Script $scriptName installed successfully"); :return -1
	} on-error={
		$send chat=$chatid text=("Failed to install script"); :return -1
	}	
} else={
	:if ([:typeof [:find $params " "]] != "num" ) do={
		$send chat=$chatid text=("Unfortunately, $params script is not available yet, please type /install list to show you all of available scripts")
	} else={
		$sendHelp from=$from chatid=$chatid; :return -1
	}
	
}

File: /script text\tg_cmd_ipcalc
:local send [:parse [/system script get tg_sendMessage source]];
:local tolower [:parse [/system script get func_lowercase source]];

:local ipPrefix [:tostr $params];
:local paramsLower [$tolower $params];

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]];
    :local txt ("Hi $from, use this command to calculate an ip address (Max , Min, Network, and Broadcast Address)%0A%0A\
                *Usage:*%0A/ipcalc <ip-prefix>%0A%0A*Example:*%0A/ipcalc 192.168.1.54/26")
    $send chat=$chatid text=$txt mode="Markdown"
}

#source: https://s.id/t5AP7
:if (($paramsLower = "help") or ([:len $params] = 0)) do={$sendHelp from=$from chatid=$chatid; :return -1}
:local ipAddress [:toip [:pick $ipPrefix 0 [:find $ipPrefix "/"]]]
:if ([:typeof $ipAddress] != "ip") do={ $send chat=$chatid text=("Invalid Ip Address"); :return -1}
:local subnetBits [:tonum [:pick $ipPrefix ([:find $ipPrefix "/"] + 1) [:len $ipPrefix]]];
:local subnetMask ((255.255.255.255 << (32 - $subnetBits)) & 255.255.255.255);
:if ([:len $params] > 0) do={
    :local result ("*$params*%0A%0A")
    :set result ($result."Address: $ipAddress%0A")
    :set result ($result."Subnet Mask: $subnetMask%0A")
    :set result ($result."Network Address: ".($ipAddress & $subnetMask)."/$subnetBits%0A")
    :set result ($result."Max Address: ".(($ipAddress | ~$subnetMask) ^ 0.0.0.1)."%0A")
    :set result ($result."Min Address: ".(($ipAddress & $subnetMask) | 0.0.0.1)."%0A")
    :set result ($result."Broadcast Address: ".($ipAddress | ~$subnetMask)."%0A")
    $send chat=$chatid text=$result mode="Markdown"
}

File: /script text\tg_cmd_jokes
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]

:local paramsLower [$tolower $params];

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]];
    :local txt ("Hi, $from%0Athis command will give you a random dad jokes that available on [https://icanhazdadjoke.com/](icanhazdadjoke)%0A");
    :set txt ($txt."to use this command, simply send /jokes to this bot and the bot will reply with a random jokes");
    $send chat=$chatid text=$txt mode="Markdown"
}


:if ([:len $params] = 0) do={
    :local jokes    ([/tool fetch http-header-field="Accept: text/plain, User-Agent: (https://github.com/user/repo)"\
                    url="https://icanhazdadjoke.com/" output=user as-value]->"data")
    $send chat=$chatid text=$jokes mode="Markdown";
} else={
    $sendhelp from=$from chatid=$chatid;
}

File: /script text\tg_cmd_lookup
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}


:local urlEncode do={
  :local Input [ :tostr $1 ];
  :local Return "";

  :if ([ :len $Input ] > 0) do={
    :local Chars " !\"#\$&'()*+,:;<=>\?@[\\]^`{|}~";
    :local Subs { "%20"; "%21"; "%22"; "%23"; "%24"; "%26"; "%27"; "%28"; "%29";
                  "%2A"; "%2B"; "%2C"; "%3A"; "%3B"; "%3C"; "%3D"; "%3E"; "%3F"; "%40";
                  "%5B"; "%5C"; "%5D"; "%5E"; "%60"; "%7B"; "%7C"; "%7D"; "%7E" };

    :for I from=0 to=([ :len $Input ] - 1) do={
      :local Char [ :pick $Input $I ];
      :local Replace [ :find $Chars $Char ];

      :if ([ :len $Replace ] > 0) do={
        :set Char ($Subs->$Replace);
      }
      :set Return ($Return . $Char);
    }
  }
	:return $Return;
}
:local paramsLower [$tolower $params];

:local sendHelp do={
	:local send [:parse [/system script get tg_sendMessage source]]
	:local helpText ("Find a geolocation of an IP address including region, city, and country%0A%0A")
	:set helpText ($helpText."*Usage*:%0A")
	:set helpText ($helpText."/lookup _<domain>_%0A")
	:set helpText ($helpText."/lookup _<ip-address>_%0A%0A")
	:set helpText ($helpText."*Example*:%0A")
	:set helpText ($helpText."/lookup _google.com.sg_%0A")
	:set helpText ($helpText."/lookup _1.1.1.1_%0A%0A")
	:put $helpText
	$send chat=$chatid text=$helpText mode="Markdown"
}

:if ([:len $params] > 0) do={
	:if ($paramsLower = "help") do={$sendHelp;}
	:if ((([:typeof [:toip $params]] = "ip") or ([:typeof [:resolve $paramsLower]] = "ip")) and ([:len $param1] = 1) ) do={
		:local urlLookup ("http://ip-api.com/json/$paramsLower")
		:put $urlLookup
		:local lookupData ([/tool fetch mode=http url=$urlLookup output=user as-value]->"data")
		:put $lookupData
		:local status [$gkey key=status text=$lookupData]
		:put $status
		:if ($status = "success") do={
			:local sendThisText (" <b>Lookup $paramsLower</b> %0A%0A");
			:local queryIP [:pick $lookupData ([:find $lookupData "\"query\""] + [:len "\"query\""]+ 2 ) ([:len $lookupData ] - 2)];
			:set sendThisText ($sendThisText."<b>Query</b>: $queryIP%0A");
			:local asNumber [$gkey key=as text=$lookupData];
			:set sendThisText ($sendThisText."<b>AS Number</b>: $asNumber%0A");
			:local isp [$gkey key=isp text=$lookupData];
			:if ([:len $isp] > 0) do={:set sendThisText ($sendThisText."<b>Internet Provider</b>: $isp%0A")} else={:set sendThisText ($sendThisText."<b>Internet Provider</b>: Unknown%0A")}
			:local country [$gkey key=country text=$lookupData];
			:local regionName [$gkey key=regionName text=$lookupData];
			:local city [$gkey key=city text=$lookupData];
			:if ([:len $country] > 0) do={:set sendThisText ($sendThisText."<b>Country</b>: $country%0A")} else={:set sendThisText ($sendThisText."<b>Country</b>: Unknown%0A")}
			:if ([:len $regionName] > 0) do={:set sendThisText ($sendThisText."<b>Region</b>: $regionName%0A")} else={:set sendThisText ($sendThisText."<b>Region</b>: Unknown%0A")}
			:if ([:len $city] > 0) do={:set sendThisText ($sendThisText."<b>City</b>: $city%0A")} else={:set sendThisText ($sendThisText."<b>City</b>: Unknown%0A")}
			:local org [$gkey key=org text=$lookupData]
			:if ([:len $org] > 0) do={:set sendThisText ($sendThisText."<b>ORG</b>: $org%0A")} else={:set sendThisText ($sendThisText."<b>ORG</b>: Unknown%0A")}
			:local timeZone [$gkey key=timezone text=$lookupData]; :set sendThisText ($sendThisText."<b>Time-Zone</b>: $timeZone%0A");
			:put $sendThisText
			$send chat=$chatid text=[$urlEncode $sendThisText] mode="html"
		} else={
			:local failMessage [$gkey key=message text=$lookupData]
			$send chat=$chatid text=("Something wrong. Message: $failMessage")
		}
	} else={
		:if ($paramsLower != "help") do={
			$send chat=$chatid text=("Unknown parameter, please type */lookup help* for more information") mode="Markdown"
		}
	}
} else={
	$sendHelp
}


File: /script text\tg_cmd_lowercase
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]


if ($params = "help") do={
	:local helptext ("======== LOWERCASE COMMAND ========%0A%0A")
	:local helptext ($helptext."This command will convert given text to lowercase%0A%0A")
	:local helptext ($helptext."*USAGE:*%0A")
	:local helptext ($helptext."/lowercase _<text>_%0A%0A")
	:local helptext ($helptext."*EXAMPLE*%0A")
	:local helptext ($helptext."/lowercase _aNtIdIsEsTaBlIsHmEnTaRiAnIsM_%0A%0A")
	:local helptext ($helptext."*The output should be:*%0A")
	:local helptext ($helptext."antidisestablishmentarianism%0A%0A")
	:local helptext ($helptext."*NOTE:*%0A")
	:local helptext ($helptext."> you can use many words as you want, but please dont spam this command too frequently%0A")
	:local helptext ($helptext."> if possible, please dont use any punctuation mark. That will cause script doesnt work properly%0A")
	$send chat=$chatid text=("$helptext") mode="Markdown"
}

if (($params != "help") and ([:typeof $params] = "str")) do={
	:local outputbody ("*Here is your lowercase text:*%0A%0A")
	:local lctext [$tolower ("$params")]
	set outputbody ($outputbody."==============================%0A")
	set outputbody ($outputbody." ``` $lctext ``` %0A")
	set outputbody ($outputbody."==============================%0A")
	$send chat=$chatid text=("$outputbody") mode="Markdown"
}


File: /script text\tg_cmd_ping
:local send [:parse [/system script get tg_sendMessage source]]

#ip address of api.telegram.org
:local address 149.154.167.220

:if ([:typeof [:toip $params]] = "ip" ) do={:set address $params}
:local time
#flood-ping
/tool flood-ping $address count=10 do={
    :set time $"avg-rtt";
}
$send chat=$chatid text=("Pong \F0\9F\8F\93%0A$time\ ms")

File: /script text\tg_cmd_quran
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]

#check language quran file availability
:local fileName ("quran-lang-data.txt");
:if ([:len [/file find where name=$fileName]] < 1) do={
    /system identity print file=$fileName
    :delay 1500ms;
    /file set $fileName contents="en"
}
#list number of verses by surah
:local ayat {"1"="7"; "2"="286"; "3"="200"; "4"="176"; "5"="120"; "6"="165"; "7"="206"; "8"="75"; "9"="129"; "10"="109"; "11"="123"; "12"="111"; "13"="43"; "14"="52";\
            "15"="99"; "16"="128"; "17"="111"; "18"="110"; "19"="98"; "20"="135"; "21"="112"; "22"="78"; "23"="118"; "24"="64"; "25"="77"; "26"="227"; "27"="93"; "28"="88";\
            "29"="69"; "30"="60"; "31"="34"; "32"="30"; "33"="73"; "34"="54"; "35"="45"; "36"="83"; "37"="182"; "38"="88"; "39"="75"; "40"="85"; "41"="54"; "42"="53";\
            "43"="89"; "44"="59"; "45"="37"; "46"="35"; "47"="38"; "48"="29"; "49"="18"; "50"="45"; "51"="60"; "52"="49"; "53"="62"; "54"="55"; "55"="78"; "56"="96";\
            "57"="29"; "58"="22"; "59"="24"; "60"="13"; "61"="14"; "62"="11"; "63"="11"; "64"="18"; "65"="12"; "66"="12"; "67"="30"; "68"="52"; "69"="52"; "70"="44";\
            "71"="28"; "72"="28"; "73"="20"; "74"="56"; "75"="40"; "76"="31"; "77"="50"; "78"="40"; "79"="46"; "80"="42"; "81"="29"; "82"="19"; "83"="36"; "84"="25";\
            "85"="22"; "86"="17"; "87"="19"; "88"="26"; "89"="30"; "90"="20"; "91"="15"; "92"="21"; "93"="11"; "94"="8"; "95"="8"; "96"="19"; "97"="5"; "98"="8"; "99"="8";\
            "100"="11"; "101"="11"; "102"="8"; "103"="3"; "104"="9"; "105"="5"; "106"="4"; "107"="7"; "108"="3"; "109"="6"; "110"="3"; "111"="5"; "112"="4"; "113"="5"; "114"="6"}
:local listLang [:toarray ("al","ar","az","en","fr","de","id")]
:local paramsLower [$tolower $params];
:local param1Lower [$tolower $param1];
:local param2Lower [$tolower $param2];

#show user how to operate /quran command
:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
    :local txt ("get random Quran verses%0A%0A")
    :set txt ($txt."Valid Parameter:%0A")
    :set txt ($txt."> /quran - get random Quran verses%0A")
    :set txt ($txt."> /quran language <language-id> - change the languange%0A")
    :set txt ($txt."> /quran language list - show the list of supported languages%0A")
    :set txt ($txt."> /quran language current - show the current language%0A")
    $send chat=$chatid text=$txt mode="Markdown"
}

:if ($paramsLower = "help") do={
    $sendHelp chatid=$chatid
    :return true
}
:local dataFileName ("quran-json.txt");
:local randSurah;
:local randAyah;
#get random number from 1 to 114 (amount of surah in al-qur'an)
:if (([:len $params] < 1) and ($paramsLower != "help") and ($param1Lower != "language")) do={
    :do {:set randSurah ([/tool fetch url="https://www.random.org/integers/\?num=1&min=1&max=114&col=1&base=10&format=plain&rnd=new" output=user as-value]->"data")} on-error={
        $send chat=$chatid text=("Something went wrong, Failed to fetch random <1>") mode="Markdown"; :return -1
    }
    :set randSurah [:pick $randSurah 0 ([:len $randSurah] - 1)]
    :local toAyat ($ayat->$randSurah)
    #get a random number based on the amount of verses from the surah obtained
    :do {:set randAyah ([/tool fetch url="https://www.random.org/integers/\?num=1&min=1&max=$toAyat&col=1&base=10&format=plain&rnd=new" output=user as-value]->"data")} on-error={
        $send chat=$chatid text=("Something went wrong, Failed to fetch random <2>") mode="Markdown"; :return -2
    }
    :set randAyah [:pick $randAyah 0 ([:len $randAyah] - 1)]
    :local language [/file get $fileName contents]
    :local uri ("https://api.banghasan.com/quran/format/json/surat/$randSurah/ayat/$randAyah/bahasa/$language")
    :do {/tool fetch dst-path=$dataFileName url=$uri} on-error={$send chat=$chatid text=("Something went wrong, Failed to fetch quran data") mode="Markdown"; :return -3}
    :delay 700ms;
    :local jsonData [/file get $dataFileName contents]
    :local textAyah [:pick $jsonData ([:find $jsonData "teks"] + [:len "teks"] + 4) ([:len $jsonData] - 51)]
    :local surahName; :if ($language = "id") do={:set $surahName [$gkey block=surat key=nama text=$jsonData]} else={:set $surahName [$gkey block=surat key=name text=$jsonData]}
    :local surahOrigin [$gkey block=surat key=type text=$jsonData]
    :local sendThisText ("$[:pick $surahName 2 ([:len $surahName] - 1)]($randSurah): $randAyah%0ARevealed in: $surahOrigin%0A$textAyah")
    :do {$send chat=$chatid text=$sendThisText} on-error={$send chat=$chatid text=("Something went wrong, Failed to fetch telegram API");}
    /file remove $dataFileName
    :return true
} else={
    :if (($paramsLower != "help" )and ($param1Lower != "language")) do={
        $sendHelp chatid=$chatid
    }
}

:if ($param1Lower = "language") do={
    :local listLangValue {"al"="albenian"; "ar"="arabic"; "az"="azerbaijani"; "en"="english"; "fr"="french"; "de"="germany"; "id"="indonesia"}
    :if ([typeof [:find $listLang "$param2Lower"]] != "nil") do={
        /file set $fileName contents=$param2Lower
        $send chat=$chatid text=("Language changed to $[($listLangValue -> $param2Lower)]")
        :return true
    }
    :if ($param2Lower = "list") do={
        :local listText ("List of available language%0A%0A")
        :for i from=0 to=([:len $listLang] - 1) do={
            :set $listText ($listText."$[:pick $listLang $i] : $[($listLangValue->[:pick $listLang $i])]%0A")
        }
        $send chat=$chatid text=$listText
        :return true
    }
    :if ($param2Lower = "current") do={
        :local currentLanguage [/file get $fileName contents]
        $send chat=$chatid text=("current language is $[($listLangValue->$currentLanguage)]")
    }
    :local invalid ([typeof [:find $listLang "$param2Lower"]] = "nil" and $param2Lower != "list" and $param2Lower != "current")
    :if ($invalid) do={$sendHelp chatid=$chatid;}
}


File: /script text\tg_cmd_quran2
#compact version of quran command
#only support bahasa indonesia
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local paramsLower [$tolower $params]

:if ($paramsLower = "help") do={
    :local txt ("Hi, $from%0APerintah ini berguna untuk mendapatkan ayat alquran secara acak%0A");
    :set txt ($txt."untuk menggunakannya, silahkan tulis \"/quran\" maka bot akan menjawab dengan ayat alquran yang terpilih secara random");
    $send chat=$chatid text=$txt; :return true
}

:if ([:len $params] != 0) do={
    $send chat=$chatid text=("Penggunaan perintah $params tidak tersedia, silahkan tulis \"/quran help\" untuk info lebih lanjut"); :return true
}

:local pickTextIndo do={
    :return [:pick $text ([:find $text "\"teks\""] + [:len "\"teks\""] + 3) ([:len $text] - 12)]
}

:local pickTerxtArab do={
    :return [:pick $text ([:find $text "\"teks\""] + [:len "\"teks\""] + 3) ([:len $text] - 1)]
}

:local fetch ([/tool fetch output=user url="https://api.banghasan.com/quran/format/json/acak" as-value ]->"data")
:local acak [:pick $fetch 73 ([:find $fetch "nomor"] - 42)];
:local arabBlock [:pick $acak [:find $acak "\"ar\""] [:len $acak]]  
:local indoBlock [:pick $acak [:find $acak "\"id\""] ([:find $acak "},"] + 1)]
:local teksIndoBefore [$pickTextIndo text=$indoBlock]
:local teksIndo
:for i from=0 to=([:len $teksIndoBefore] - 1) do={
    :local char [:pick $teksIndoBefore $i]
    :if ($char = "\\") do={
        :set $char ""
    }
    :set teksIndo ($teksIndo.$char)
}
:local teksArab [$pickTerxtArab text=$arabBlock]
:local surat [$gkey key=("\"nama\"") block=surat text=$fetch];
:local ayat [$gkey key=("\"ayat\"") text=$indoBlock];
:local sendtelegram ("*QS. $surat: $ayat*%0A%0A$teksArab%0A%0A*Terjemahan:*%0A$teksIndo");
$send chat=$chatid text=$sendtelegram mode="Markdown"

File: /script text\tg_cmd_randomcase
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local toupper [:parse [/system script get func_uppercase source]]
:local randomizeScriptUrl ("https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/util/randomizeScript")


:local paramsLower [$tolower $params]

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
    :local helptext ("%3D%3D%3D%3D%3D%3D%3D%20RANDOMCASE%20%3D%3D%3D%3D%3D%3D%3D%0A%0A")
	:local helptext ($helptext."Hi $from, With this tool you can randomize the case of characters in text. \
                    This tool arbitrarily selects the lower or upper case version of each character%0A%0A")
	:local helptext ($helptext."*USAGE:*%0A")
	:local helptext ($helptext."/randomcase _<text>_%0A%0A")
	:local helptext ($helptext."*EXAMPLE*%0A")
	:local helptext ($helptext."/randomcase _antidisestablishmentarianism_%0A%0A")
	:local helptext ($helptext."*The output should be:*%0A")
	:local helptext ($helptext."AntiDisEsTabLISHmeNtArIanIsM%0A%0A")
	:local helptext ($helptext."*NOTE:*%0A")
	:local helptext ($helptext."> you can use many words as you want, but please dont spam this command too frequently%0A")
	:local helptext ($helptext."> if possible, please dont use any punctuation mark. That will cause script not work properly%0A")
	$send chat=$chatid text=("$helptext") mode="Markdown"
}

:if (($paramsLower = "help") or ([:len $params] = 0)) do={$sendHelp from=$from chatid=$chatid; :return -1}

:local randomize [:parse ([/tool fetch mode=https url=$randomizeScriptUrl output=user as-value]->"data")];

:local result
:if (([:len $params] > 0) and ([:typeof [:tostr $params]] = "str")) do={
    :local randomNum [$randomize type="integer"];
    :local num 0
    :local numIndex 2
    :for i from=0 to=([:len $paramsLower] - 1) do={
        :set num ($num + 1)
        :if ($num > 20) do={
            :set num $numIndex;
            :set numIndex ($numIndex + 1)
            :if ($numIndex > 15) do={:set numIndex 2}
        }
        :local char [:pick $paramsLower $i]
        :local selectNum [:pick $randomNum $num]
        :if (($selectNum % 2) = 1) do={
            :set char [$toupper $char]
        }
        :set result ($result.$char)
    }
    :put $result
    $send chat=$chatid text=$result
}

File: /script text\tg_cmd_randomize
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}

:local paramsLower [$tolower $params];
:local param1Lower [$tolower $param1];
:local param2Lower [$tolower $param2];
:local param3Lower [$tolower $param3]
:global RandomizeStyle;
:local randomizeScriptUrl ("https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/util/randomizeScript")

:if ($paramsLower = "method") do={
	:local invalidmode
	:set invalidmode ("*Operation is invalid*%0A");
	:set invalidmode ($invalidmode."%0A_Valid options are:_%0A");
	:set invalidmode ($invalidmode."/randomize method _local_%0A");
	:set invalidmode ($invalidmode."/randomize method _internet_%0A");
	$send chat=$chatid text=("$invalidmode") mode="Markdown"
	:return true
}

:if ($param1Lower = "method") do={
	:if (($param2Lower = "local") or ($param2Lower = "internet")) do={
		:if ($param2Lower = "local") do={ set RandomizeStyle ("local"); $send chat=$chatid text=("randomization method has been successfully changed to $RandomizeStyle") mode="Markdown" }
		:if ($param2Lower = "internet") do={ set RandomizeStyle ("internet"); $send chat=$chatid text=("randomization method has been successfully changed to $RandomizeStyle") mode="Markdown"}
	} else={
		:local invalidmode
		:set invalidmode ("*Option $param2 is invalid*%0A");
		:set invalidmode ($invalidmode."%0A_Valid options are:_%0A");
		:set invalidmode ($invalidmode."/randomize method _local_%0A");
		:set invalidmode ($invalidmode."/randomize method _internet_%0A");
		$send chat=$chatid text=("$invalidmode") mode="Markdown"
		:return true
	}
}

:if ($paramsLower = "help") do={
	:local randomizehelp;
	:set randomizehelp ("======== RANDOMIZE COMMAND ========%0A%0A");
	:set randomizehelp ($randomizehelp."*Valid Options Are:*%0A");
	:set randomizehelp ($randomizehelp.">	/randomize method _'local' <or> 'internet'_ - choose a randomization method between local or internet methods%0A");
	:set randomizehelp ($randomizehelp."/randomize string <length> - generate random string (length maximum = 20)%0A");
	:set randomizehelp ($randomizehelp."/randomize number <length> - generate random number (length maximum = 20)%0A");
	$send chat=$chatid text=("$randomizehelp") mode="Markdown"
	:return true
}
:if ($param1Lower = "string") do={
	:if ([typeof [tonum $param2]] = "num") do={
		:if (($param2 < 21) and ($param2 > 0)) do={
			:if ($RandomizeStyle = "local") do={
				:local randomize [:parse ([/tool fetch mode=https url=$randomizeScriptUrl output=user as-value]->"data")];
				:local rand [$randomize type="string"];
				:local randomresult [:pick $rand 0 $param2 ];
				:local rslstext ("*Here is your random string*%0A%0A");
				:set rslstext ($rslstext." ``` $randomresult ``` ");
				$send chat=$chatid text=("$rslstext") mode="Markdown"
				:return true
			}
			:if ($RandomizeStyle = "internet") do={
				:local randomorg [:tostr ([/tool fetch url="https://www.random.org/strings/\?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new" as-value output=user ]->"data")];
				:local pickrandomorg [:pick $randomorg 0 $param2];
				:local rsistext ("*Here is your random string*%0A%0A");
				:set rsistext ($rsistext." ``` $pickrandomorg ``` ");
				$send chat=$chatid text=("$rsistext") mode="Markdown"
				:return true
			}
			:if (($RandomizeStyle != "local") and ($RandomizeStyle != "internet")) do={
				$send chat=$chatid text=("randomize method has not been set, please type _/randomize method_ to continue") mode="Markdown"
				:return true
			}
		} else={
			$send chat=$chatid text=("Please choose range beetwen *1 - 20*") mode="Markdown"
		}
	} else={
		$send chat=$chatid text=("*Invalid Parameter*%0A%0APlease type /randomize help for more information") mode="Markdown"
	}
}

:if ($param1 = "number") do={
	:if ([:typeof [:tonum $param2]] = "num") do={
		:if (($param2 < 21) and ($param2 > 0)) do={
			:if ($RandomizeStyle = "local") do={
				:local randomize [:parse ([/tool fetch mode=https url=$randomizeScriptUrl output=user as-value]->"data")];
				:local rand [$randomize type="integer"];
				:local randomresult [:pick $rand 0 $param2 ];
				:local rslntext ("*Here is your random number*%0A%0A");
				:set rslntext ($rslntext." ``` $randomresult ``` ");
				$send chat=$chatid text=("$rslntext") mode="Markdown"
				:return true
			}
			:if ($RandomizeStyle = "internet") do={
				:local randomorg [:tostr ([/tool fetch url="https://www.random.org/strings/\?num=1&len=20&digits=on&unique=on&format=plain&rnd=new" as-value output=user ]->"data")];
				:local pickrandomorg [:pick $randomorg 0 $param2];
				:local rsintext ("*Here is your random number*%0A%0A");
				:set rsintext ($rsintext." ``` $pickrandomorg ``` ");
				$send chat=$chatid text=("$rsintext") mode="Markdown"
				:return true
			}
			:if (($RandomizeStyle != "local") and ($RandomizeStyle != "internet")) do={
				$send chat=$chatid text=("randomize method has not been set, please type _/randomize method_ to continue") mode="Markdown"
				:return true
			}

		} else={
			$send chat=$chatid text=("Please choose range beetwen *1 - 20*") mode="Markdown"
		}
	} else={
		$send chat=$chatid text=("*Invalid Parameter*%0A%0APlease type /randomize help for more information") mode="Markdown"
	}
}


File: /script text\tg_cmd_shalat
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]

:local paramsLower [$tolower $params];
:local param1Lower [$tolower $param1];
:local param2Lower [$tolower $param2];

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
}

:if ([:typeof $params] = "str") do={
    :local searchCityUrl ("https://api.banghasan.com/sholat/format/json/kota/nama/$paramsLower")
    :local searchJson ([/tool fetch url=$searchCityUrl output=user as-value]->"data")
    :local cityCode [$gkey block=kota key=id text=$searchJson]
    :local cityName [$gkey block=kota key=nama text=$searchJson]
    # $send chat=$chatid text=("$cityName%0A$cityCode")
    # unfinished
}


File: /script text\tg_cmd_shorten
:local send [:parse [/system script get tg_sendMessage source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local param1 [:pick $params 0 [:find $params " "]]
:local param2 [:pick $params ([:find $params " "]+1) [:len $params]]
:local param3 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] ([:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]+1) [:len [:pick $params ([:find $params " "]+1) [:len $params]]]]
:if ([:len [:find $param2 " "]]>0) do={
	:set param2 [:pick [:pick $params ([:find $params " "]+1) [:len $params]] 0 [:find [:pick $params ([:find $params " "]+1) [:len $params]] " "]]
} else={
	:set param3 ""
}
:local privateParams $params
:put $params
:put $param1
:put $param2
:put $param3
:put $chatid
:put $from


:local paramsLower [$tolower $params];
:put $paramsLower

:local sendHelp do={
	:local send [:parse [/system script get tg_sendMessage source]]
	:local helpText
	:set helpText ($helpText."Short your long url with [rel.ink](https://rel.ink/) shortener services, powered by Cloudflare%0A%0A")
	:set helpText ($helpText." *Usage*: %0A")
	:set helpText ($helpText."/shorten _<long-url>_%0A%0A")
	:set helpText ($helpText." *Example*: %0A")
	:set helpText ($helpText."/shorten _https://mikrotik.com/download_")
	$send chat=$chatid text=$helpText mode="Markdown"
}

:if ($paramsLower = "help") do={
	$sendHelp chatid=$chatid;
}

:if ([:pick $privateParams ([:len $privateParams]-1 )] = "/") do={
	:set privateParams [:pick $privateParams 0 ([:len $privateParams] - 2)];
	:put $privateParams;
}
:put [:len $params]
:if (([:len $params] > 0) and ($paramsLower != "help")) do={
	:do {
		:local httpData ("{\"url\":\"$privateParams\"}")
		:put $httpData
		:local shortData ([/tool fetch http-method=post http-header-field="content-type: application/json" http-data=("$httpData") url="https://rel.ink/api/links/" output=user as-value]->"data")
		:put $shortData
		:local hashID [$gkey key=hashid text=$shortData]
		:local shortUrl ("https://rel.ink/$hashID")
		:put $shortUrl
		:local sendThisText
		:set sendThisText ($sendThisText."Your link is successfully shortened%0A")
		:set sendThisText ($sendThisText."[$shortUrl]($shortUrl)%0A")
		$send chat=$chatid text=$sendThisText mode="Markdown"
	} on-error={
		$send chat=$chatid text=("Something went wrong. Try again later or check your url")
		$sendHelp chatid=$chatid;
	}
} else={
	$sendHelp chatid=$chatid;
}


File: /script text\tg_cmd_update
:local send [:parse [/system script get tg_sendMessage source]]
:local tolower [:parse [/system script get func_lowercase source]]
:local fconfig [:parse [/system script get tg_config source]]
:local config [$fconfig]

:local trusted [:toarray ($config->"trusted")]
:local allowed ([:type [:find $trusted $chatid]] != "nil")
:if (!$allowed) do={
 :put "Unknown sender, keep silence"
 :return -1
}

:local paramsLower [$tolower $params];
:local fetchCommand ([/tool fetch url="https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/util/availableCommand" output=user as-value]->"data")
:local availableCommand [:toarray $fetchCommand]

:local sendHelp do={
    :local send [:parse [/system script get tg_sendMessage source]]
    :local txt ("Hi, $from%0AUse this command to update your installed script%0A\
                *Usage:*%0A/update <command>%0A*Example:*%0A/update _jokes_%0A\
                *Note:*%0Ato see the available script just type /update list");
    $send chat=$chatid text=$txt mode="Markdown";
}

:if ($paramsLower = "list") do={
	:local listScript ("List of available script%0A%0A")
	:local number 0
	:for i from=0 to=([:len $availableCommand] - 1) do={
		:local command [:pick $availableCommand $i]
		:set number ($number + 1)
		:set listScript ($listScript."$number. $command%0A")
	}
	:set listScript ($listScript."%0Ato update a command just type /update <command>. For example%0A/update jokes")
	$send chat=$chatid text=$listScript mode="Markdown"; :return -1
}
:if ($paramsLower = "help") do={
	$sendHelp from=$from chatid=$chatid; :return -1
}

:if ([:len $params] > 0) do={
    :local valid ([:typeof [:find $availableCommand $paramsLower]] != "nil")
    :if ($valid) do={
        :local scriptName ("tg_cmd_$paramsLower")
        :if ([:len [/system script find where name=$scriptName]] > 0) do={
            /system script remove $scriptName;
            :local scriptUrlInstall ("https://raw.githubusercontent.com/furaihan/FurMikrotik-bot/master/script%20text/$scriptName")
            :do {
                :local scriptSource ([/tool fetch url=$scriptUrlInstall output=user as-value]->"data")
                /system script add name=$scriptName policy=read source=$scriptSource
                $send chat=$chatid text=("Script $scriptName updated successfully")
            } on-error={
                $send chat=$chatid text=("Failed to update script, please try again later")
            }	
        } else={
            $send chat=$chatid text=("$scriptName is not installed, please use /install $paramsLower to install")
        }
    } else={
        :if ([:typeof [:find $params " "]] != "num" ) do={
            $send chat=$chatid text=("Unfortunately, $params script is not available yet, please type /update list to show you all of available scripts")
            :return -1
	    } else={
		    $sendHelp from=$from chatid=$chatid; :return -1
	    }
    }
} else={
    $sendHelp from=$from chatid=$chatid; :return -1
}

File: /script text\tg_cmd_uppercase
:local send [:parse [/system script get tg_sendMessage source]]
:local toupper [:parse [/system script get func_uppercase source]]

if ($params = "help") do={
	:local helptext ("======== UPPERCASE COMMAND ========%0A%0A");
	:local helptext ($helptext."This command will convert given text to uppercase%0A%0A");
	:local helptext ($helptext."*USAGE:*%0A");
	:local helptext ($helptext."/uppercase _<text>_%0A%0A");
	:local helptext ($helptext."*EXAMPLE*%0A");
	:local helptext ($helptext."/uppercase _aNtIdIsEsTaBlIsHmEnTaRiAnIsM_%0A%0A");
	:local helptext ($helptext."*The output should be:*%0A");
	:local helptext ($helptext."ANTIDISESTABLISHMENTARIANISM%0A%0A");
	:local helptext ($helptext."*NOTE:*%0A");
	:local helptext ($helptext."> you can use many words as you want, but please dont spam this command too frequently%0A");
	:local helptext ($helptext."> if possible, please dont use any punctuation mark. That will cause script doesnt work properly%0A");
	$send chat=$chatid text=("$helptext") mode="Markdown"
}

if (($params != "help") and ([:typeof $params] = "str")) do={
	:local outputbody ("*Here is your uppercase text:*%0A%0A");
	:local lctext [$toupper ("$params")];
	set outputbody ($outputbody."==============================%0A");
	set outputbody ($outputbody." ``` $lctext ``` %0A");
	set outputbody ($outputbody."==============================%0A");
	$send chat=$chatid text=("$outputbody") mode="Markdown"
}


File: /script text\tg_config
######################################
# Telegram bot API, VVS/BlackVS 2017
#                                Config file
######################################
:log info "telegram configuration file has been loaded";

# to use config insert next lines:
#:local fconfig [:parse [/system script get tg_config source]]
#:local config [$fconfig]
#:put $config

######################################
# Common parameters
######################################

:local config {
"Command"="telegram";
	"botAPI"="xxxxxxxxxxxxxx:xxxxxxxxxx";
	"defaultChatID"="xxxxxxxxxx";
	"trusted"="xxxxxxx, xxxxxxxx, xxxxxxxx";
	"storage"="";
	"timeout"=5;
	"refresh_active"=15;
	"refresh_standby"=300;
	"available_for_public"=true;
}
return $config


File: /script text\tg_getkey
:local cur 0
:local lkey [:len $key]
:local res ""
:local p

:if ([:len $block]>0) do={
 :set p [:find $text $block $cur]
 :if ([:type $p]="nil") do={
  :return $res
 }
 :set cur ($p+[:len $block]+2)
}

:set p [:find $text $key $cur]
:if ([:type $p]!="nil") do={
 :set cur ($p+lkey+2)
 :set p [:find $text "," $cur]
 :if ([:type $p]!="nil") do={
   if ([:pick $text $cur]="\"") do={
    :set res [:pick $text ($cur+1) ($p-1)]
   } else={
    :set res [:pick $text $cur $p]
   }
 } 
}
:return $res

File: /script text\tg_getUpdates
:global TGLASTMSGID
:global TGLASTUPDID

:local fconfig [:parse [/system script get tg_config source]]
:local http [:parse [/system script get func_fetch source]]
:local gkey [:parse [/system script get tg_getkey source]]
:local send [:parse [/system script get tg_sendMessage source]]

:local cfg [$fconfig]
:local trusted [:toarray ($cfg->"trusted")]
:local botID ($cfg->"botAPI")
:local storage ($cfg->"storage")
:local timeout ($cfg->"timeout")
:local availableForPublic [:tobool ($cfg->"available_for_public")]

:put "cfg=$cfg"
:put "trusted=$trusted"
:put "botID=$botID"
:put "storage=$storage"
:put "timeout=$timeout"

:local file ($storage."tg_get_updates.txt")
:local logfile ($storage."tg_fetch_log.txt")
#get 1 message per time
:local url ("https://api.telegram.org/bot".$botID."/getUpdates?timeout=$timeout&limit=1")
:if ([:len $TGLASTUPDID]>0) do={
  :set url "$url&offset=$($TGLASTUPDID+1)"
}

:put "Reading updates..."
:local res [$http dst-path=$file url=$url resfile=$logfile]
:if ($res!="success") do={
  :put "Error getting updates"
  return "Failed get updates"
}
:put "Finished to read updates."

:local content [/file get [/file find name=$file] contents]

:local msgid [$gkey key="message_id" text=$content]
:if ($msgid="") do={ 
 :put "No new updates"
 :return 0 
}
:set TGLASTMSGID $msgid

:local updid [$gkey key="update_id" text=$content]
:set TGLASTUPDID $updid

:local fromid [$gkey block="from" key="id" text=$content]
:local username [$gkey block="from" key="username" text=$content]
:local firstname [$gkey block="from" key="first_name" text=$content]
:local lastname [$gkey block="from" key="last_name" text=$content]
:local chatid [$gkey block="chat" key="id" text=$content]
:local chattext [$gkey block="chat" key="text" text=$content]

:put "message id=$msgid"
:put "update id=$updid"
:put "from id=$fromid"
:put "first name=$firstname"
:put "last name=$lastname"
:put "username=$username"
:local name "$firstname $lastname"
:if ([:len $name]<2) do {
 :set name $username
}

:put "in chat=$chatid"
:put "command=$chattext"

:if (!$availableForPublic) do={
  :local allowed ( [:type [:find $trusted $fromid]]!="nil" or [:type [:find $trusted $chatid]]!="nil")
  :if (!$allowed) do={
  :put "Unknown sender, keep silence"
  :return -1
  }  
}


:local cmd ""
:local params ""
:local ltext [:len $chattext]

:local pos [:find $chattext " "]
:if ([:type $pos]="nil") do={
 :set cmd [:pick $chattext 1 $ltext]
} else={
 :set cmd [:pick $chattext 1 $pos]
 :set params [:pick $chattext ($pos+1) $ltext]
}

:local pos [:find $cmd "@"]
:if ([:type $pos]!="nil") do={
 :set cmd [:pick $cmd 0 $pos]
}

:put "cmd=<$cmd>"
:put "params=<$params>"

:local alternativeCommand {"hi"="help"; "start"="help"; "hello"="help"; "support"="help"; "assistance"="help"}
:if ([:typeof ($alternativeCommand -> $cmd)] = "str") do={:set cmd ($alternativeCommand -> $cmd); :put "cmd=<$cmd>"}

:global TGLASTCMD $cmd

:put "Try to invoke external script tg_cmd_$cmd"
:local script [:parse [/system script get "tg_cmd_$cmd" source]]
$script params=$params chatid=$chatid from=$name

File: /script text\tg_sendAudio
:local configuration [:parse [/system script get tg_config source]]
:local conf [$configuration]
:local chatID ($conf->"defaultChatID")
:local botID ($conf->"botAPI")
:local storage ($conf->"storage")

:if ([:len $chat]>0) do={:set chatID $chat}
:local url "https://api.telegram.org/bot$botID/sendAudio?chat_id=$chatID&audio=$audio"

:local file ($tgStorage."tg_get_updates.txt")
:local logfile ($tgStorage."tg_fetch_log.txt")
:put $url

/tool fetch url=$url keep-result=no


File: /script text\tg_sendMessage
:local fconfig [:parse [/system script get tg_config source]]

:local cfg [$fconfig]
:local chatID ($cfg->"defaultChatID")
:local botID ($cfg->"botAPI")
:local storage ($cfg->"storage")

:if ([:len $chat]>0) do={:set chatID $chat}

:local url "https://api.telegram.org/bot$botID/sendmessage?chat_id=$chatID&text=$text"
:if ([:len $mode]>0) do={:set url ($url."&parse_mode=$mode")}

:local file ($tgStorage."tg_get_updates.txt")
:local logfile ($tgStorage."tg_fetch_log.txt")

/tool fetch url=$url keep-result=no

File: /setup.rsc
/system script
add name=tg_cmd_help policy=read \
    source=":local send [:parse [/system script get tg_sendMessage source]]\r\
    \n\r\
    \n\r\
    \n:local helpBody;\r\
    \n:set helpBody (\"Hi, \$from%0ALorem ipsum dolor sit amet, consectetur ad\
    ipisicing elit, sed do eiusmod tempor incididunt \\\r\
    \n                ut labore et dolore magna aliqua. Ut enim ad minim venia\
    m%0A%0AAvailable Commands:%0A\")\r\
    \n\r\
    \n:foreach script in=[/system script find where name~\"tg_cmd_\"] do={\r\
    \n    :local name [/system script get \$script name]\r\
    \n    :local command [:pick \$name 7 [:len \$name]]\r\
    \n    :set helpBody (\$helpBody.\"/\$command%0A\")\r\
    \n}\r\
    \n:set helpBody (\$helpBody.\"%0ANote:%0A> For detailed command help type:\
    \_<command> help%0A\\\r\
    \n                > *install* and *update* command is only available for b\
    ot admin\")\r\
    \n\$send chat=\$chatid text=\$helpBody mode=\"Markdown\";\r\
    \n"
add name=tg_cmd_ping policy=read \
    source=":local send [:parse [/system script get tg_sendMessage source]]\r\
    \n\r\
    \n#ip address of api.telegram.org\r\
    \n:local address 149.154.167.220\r\
    \n\r\
    \n:if ([:typeof [:toip \$params]] = \"ip\" ) do={:set address \$params}\r\
    \n:local time\r\
    \n#flood-ping\r\
    \n/tool flood-ping \$address count=10 do={\r\
    \n    :set time \$\"avg-rtt\";\r\
    \n}\r\
    \n\$send chat=\$chatid text=(\"Pong \\F0\\9F\\8F\\93%0A\$time\\ ms\")"
add name=tg_cmd_update policy=read \
    source=":local send [:parse [/system script get tg_sendMessage source]]\r\
    \n:local tolower [:parse [/system script get func_lowercase source]]\r\
    \n:local fconfig [:parse [/system script get tg_config source]]\r\
    \n:local config [\$fconfig]\r\
    \n\r\
    \n:local trusted [:toarray (\$config->\"trusted\")]\r\
    \n:local allowed ([:type [:find \$trusted \$chatid]] != \"nil\")\r\
    \n:if (!\$allowed) do={\r\
    \n :put \"Unknown sender, keep silence\"\r\
    \n :return -1\r\
    \n}\r\
    \n\r\
    \n:local paramsLower [\$tolower \$params];\r\
    \n:local fetchCommand ([/tool fetch url=\"https://raw.githubusercontent.co\
    m/furaihan/FurMikrotik-bot/master/util/availableCommand\" output=user as-v\
    alue]->\"data\")\r\
    \n:local availableCommand [:toarray \$fetchCommand]\r\
    \n\r\
    \n:local sendHelp do={\r\
    \n    :local send [:parse [/system script get tg_sendMessage source]]\r\
    \n    :local txt (\"Hi, \$from%0AUse this command to update your installed\
    \_script%0A\\\r\
    \n                *Usage:*%0A/update <command>%0A*Example:*%0A/update _jok\
    es_%0A\\\r\
    \n                *Note:*%0Ato see the available script just type /update \
    list\");\r\
    \n    \$send chat=\$chatid text=\$txt mode=\"Markdown\";\r\
    \n}\r\
    \n\r\
    \n:if (\$paramsLower = \"list\") do={\r\
    \n\t:local listScript (\"List of available script%0A%0A\")\r\
    \n\t:local number 0\r\
    \n\t:for i from=0 to=([:len \$availableCommand] - 1) do={\r\
    \n\t\t:local command [:pick \$availableCommand \$i]\r\
    \n\t\t:set number (\$number + 1)\r\
    \n\t\t:set listScript (\$listScript.\"\$number. \$command%0A\")\r\
    \n\t}\r\
    \n\t:set listScript (\$listScript.\"%0Ato update a command just type /upda\
    te <command>. For example%0A/update jokes\")\r\
    \n\t\$send chat=\$chatid text=\$listScript mode=\"Markdown\"; :return -1\r\
    \n}\r\
    \n:if (\$paramsLower = \"help\") do={\r\
    \n\t\$sendHelp from=\$from chatid=\$chatid; :return -1\r\
    \n}\r\
    \n\r\
    \n:if ([:len \$params] > 0) do={\r\
    \n    :local valid ([:typeof [:find \$availableCommand \$paramsLower]] != \
    \"nil\")\r\
    \n    :if (\$valid) do={\r\
    \n        :local scriptName (\"tg_cmd_\$paramsLower\")\r\
    \n        :if ([:len [/system script find where name=\$scriptName]] > 0) d\
    o={\r\
    \n            /system script remove \$scriptName;\r\
    \n            :local scriptUrlInstall (\"https://raw.githubusercontent.com\
    /furaihan/FurMikrotik-bot/master/script%20text/\$scriptName\")\r\
    \n            :do {\r\
    \n                :local scriptSource ([/tool fetch url=\$scriptUrlInstall\
    \_output=user as-value]->\"data\")\r\
    \n                /system script add name=\$scriptName policy=read source=\
    \$scriptSource\r\
    \n                \$send chat=\$chatid text=(\"Script \$scriptName updated\
    \_successfully\")\r\
    \n            } on-error={\r\
    \n                \$send chat=\$chatid text=(\"Failed to update script, pl\
    ease try again later\")\r\
    \n            }\t\r\
    \n        } else={\r\
    \n            \$send chat=\$chatid text=(\"\$scriptName is not installed, \
    please use /install \$paramsLower to install\")\r\
    \n        }\r\
    \n    } else={\r\
    \n        :if ([:typeof [:find \$params \" \"]] != \"num\" ) do={\r\
    \n            \$send chat=\$chatid text=(\"Unfortunately, \$params script \
    is not available yet, please type /update list to show you all of availabl\
    e scripts\")\r\
    \n            :return -1\r\
    \n\t    } else={\r\
    \n\t\t    \$sendHelp from=\$from chatid=\$chatid; :return -1\r\
    \n\t    }\r\
    \n    }\r\
    \n} else={\r\
    \n    \$sendHelp from=\$from chatid=\$chatid; :return -1\r\
    \n}"
add name=tg_cmd_install policy=read \
    source=":local send [:parse [/system script get tg_sendMessage source]]\r\
    \n:local tolower [:parse [/system script get func_lowercase source]]\r\
    \n:local fconfig [:parse [/system script get tg_config source]]\r\
    \n:local config [\$fconfig]\r\
    \n\r\
    \n:local trusted [:toarray (\$config->\"trusted\")]\r\
    \n:local allowed ([:type [:find \$trusted \$chatid]] != \"nil\")\r\
    \n:if (!\$allowed) do={\r\
    \n :put \"Unknown sender, keep silence\"\r\
    \n :return -1\r\
    \n}\r\
    \n\r\
    \n:local paramsLower [\$tolower \$params];\r\
    \n:local fetchCommand ([/tool fetch url=\"https://raw.githubusercontent.co\
    m/furaihan/FurMikrotik-bot/master/util/availableCommand\" output=user as-v\
    alue]->\"data\")\r\
    \n:local availableCommand [:toarray \$fetchCommand]\r\
    \n\r\
    \n:local sendHelp do={\r\
    \n\t:local send [:parse [/system script get tg_sendMessage source]]\r\
    \n    :local txt (\"Hi, \$from%0AUse this command to install a script%0A\\\
    \r\
    \n                *Usage:*%0A/install <command>%0A*Example:*%0A/install _j\
    okes_%0A\\\r\
    \n                *Note:*%0Ato see the available script just type /install\
    \_list\");\r\
    \n    \$send chat=\$chatid text=\$txt mode=\"Markdown\";\r\
    \n}\r\
    \n\r\
    \n:if (\$paramsLower = \"list\") do={\r\
    \n\t:local listScript (\"List of available script%0A%0A\")\r\
    \n\t:local number 0\r\
    \n\t:for i from=0 to=([:len \$availableCommand] - 1) do={\r\
    \n\t\t:local command [:pick \$availableCommand \$i]\r\
    \n\t\t:set number (\$number + 1)\r\
    \n\t\t:set listScript (\$listScript.\"\$number. \$command%0A\")\r\
    \n\t}\r\
    \n\t:set listScript (\$listScript.\"%0Ato install a command just type /ins\
    tall <command>. For example%0A/install jokes\")\r\
    \n\t\$send chat=\$chatid text=\$listScript mode=\"Markdown\"; :return -1\r\
    \n}\r\
    \n\r\
    \n:if (\$paramsLower = \"help\") do={\r\
    \n\t\$sendHelp from=\$from chatid=\$chatid; :return -1\r\
    \n}\r\
    \n\r\
    \n:local valid ([:typeof [:find \$availableCommand \$paramsLower]] != \"ni\
    l\")\r\
    \n:if (\$valid) do={\r\
    \n\t:local scriptName (\"tg_cmd_\$paramsLower\")\r\
    \n\t:if ([:len [/system script find where name=\$scriptName]] > 0) do={\r\
    \n\t\t\$send chat=\$chatid text=(\"\$scriptName script has been installed,\
    \_if you want to update the script, use /update instead\");\r\
    \n\t\t:return -1\r\
    \n\t}\r\
    \n\t:local scriptUrlInstall (\"https://raw.githubusercontent.com/furaihan/\
    FurMikrotik-bot/master/script%20text/\$scriptName\")\r\
    \n\t:do {\r\
    \n\t\t:local scriptSource ([/tool fetch url=\$scriptUrlInstall output=user\
    \_as-value]->\"data\")\r\
    \n\t\t/system script add name=\$scriptName policy=read source=\$scriptSour\
    ce\r\
    \n\t\t\$send chat=\$chatid text=(\"Script \$scriptName installed successfu\
    lly\"); :return -1\r\
    \n\t} on-error={\r\
    \n\t\t\$send chat=\$chatid text=(\"Failed to install script\"); :return -1\
    \r\
    \n\t}\t\r\
    \n} else={\r\
    \n\t:if ([:typeof [:find \$params \" \"]] != \"num\" ) do={\r\
    \n\t\t\$send chat=\$chatid text=(\"Unfortunately, \$params script is not a\
    vailable yet, please type /install list to show you all of available scrip\
    ts\")\r\
    \n\t} else={\r\
    \n\t\t\$sendHelp from=\$from chatid=\$chatid; :return -1\r\
    \n\t}\r\
    \n\t\r\
    \n}"
add name=tg_cmd_ipcalc policy=read \
    source=":local send [:parse [/system script get tg_sendMessage source]];\r\
    \n:local tolower [:parse [/system script get func_lowercase source]];\r\
    \n\r\
    \n:local ipPrefix [:tostr \$params];\r\
    \n:local paramsLower [\$tolower \$params];\r\
    \n\r\
    \n:local sendHelp do={\r\
    \n    :local send [:parse [/system script get tg_sendMessage source]];\r\
    \n    :local txt (\"Hi \$from, use this command to calculate an ip address\
    \_(Max , Min, Network, and Broadcast Address)%0A%0A\\\r\
    \n                *Usage:*%0A/ipcalc <ip-prefix>%0A%0A*Example:*%0A/ipcalc\
    \_192.168.1.54/26\")\r\
    \n    \$send chat=\$chatid text=\$txt mode=\"Markdown\"\r\
    \n}\r\
    \n\r\
    \n#source: https://s.id/t5AP7\r\
    \n:if ((\$paramsLower = \"help\") or ([:len \$params] = 0)) do={\$sendHelp\
    \_from=\$from chatid=\$chatid; :return -1}\r\
    \n:local ipAddress [:toip [:pick \$ipPrefix 0 [:find \$ipPrefix \"/\"]]]\r\
    \n:if ([:typeof \$ipAddress] != \"ip\") do={ \$send chat=\$chatid text=(\"\
    Invalid Ip Address\"); :return -1}\r\
    \n:local subnetBits [:tonum [:pick \$ipPrefix ([:find \$ipPrefix \"/\"] + \
    1) [:len \$ipPrefix]]];\r\
    \n:local subnetMask ((255.255.255.255 << (32 - \$subnetBits)) & 255.255.25\
    5.255);\r\
    \n:if ([:len \$params] > 0) do={\r\
    \n    :local result (\"*\$params*%0A%0A\")\r\
    \n    :set result (\$result.\"Address: \$ipAddress%0A\")\r\
    \n    :set result (\$result.\"Subnet Mask: \$subnetMask%0A\")\r\
    \n    :set result (\$result.\"Network Address: \".(\$ipAddress & \$subnetM\
    ask).\"/\$subnetBits%0A\")\r\
    \n    :set result (\$result.\"Max Address: \".((\$ipAddress | ~\$subnetMas\
    k) ^ 0.0.0.1).\"%0A\")\r\
    \n    :set result (\$result.\"Min Address: \".((\$ipAddress & \$subnetMask\
    ) | 0.0.0.1).\"%0A\")\r\
    \n    :set result (\$result.\"Broadcast Address: \".(\$ipAddress | ~\$subn\
    etMask).\"%0A\")\r\
    \n    \$send chat=\$chatid text=\$result mode=\"Markdown\"\r\
    \n}"
add name=func_fetch policy=read \
    source="#########################################################\r\
    \n# Wrapper for /tools fetch\r\
    \n#  Input:\r\
    \n#    mode\r\
    \n#    upload=yes/no\r\
    \n#    user\r\
    \n#    password\r\
    \n#    address\r\
    \n#    host\r\
    \n#    httpdata\r\
    \n#    httpmethod\r\
    \n#    check-certificate\r\
    \n#    src-path\r\
    \n#    dst-path\r\
    \n#    ascii=yes/no\r\
    \n#    url\r\
    \n#    resfile\r\
    \n\r\
    \n:local res \"fetchresult.txt\"\r\
    \n:if ([:len \$resfile]>0) do={:set res \$resfile}\r\
    \n#:put \$res\r\
    \n\r\
    \n:local cmd \"/tool fetch\"\r\
    \n:if ([:len \$mode]>0) do={:set cmd \"\$cmd mode=\$mode\"}\r\
    \n:if ([:len \$upload]>0) do={:set cmd \"\$cmd upload=\$upload\"}\r\
    \n:if ([:len \$user]>0) do={:set cmd \"\$cmd user=\\\"\$user\\\"\"}\r\
    \n:if ([:len \$password]>0) do={:set cmd \"\$cmd password=\\\"\$password\\\
    \"\"}\r\
    \n:if ([:len \$address]>0) do={:set cmd \"\$cmd address=\\\"\$address\\\"\
    \"}\r\
    \n:if ([:len \$host]>0) do={:set cmd \"\$cmd host=\\\"\$host\\\"\"}\r\
    \n:if ([:len \$\"http-data\"]>0) do={:set cmd \"\$cmd http-data=\\\"\$\"ht\
    tp-data\"\\\"\"}\r\
    \n:if ([:len \$\"http-method\"]>0) do={:set cmd \"\$cmd http-method=\\\"\$\
    \"http-method\"\\\"\"}\r\
    \n:if ([:len \$\"check-certificate\"]>0) do={:set cmd \"\$cmd check-certif\
    icate=\\\"\$\"check-certificate\"\\\"\"}\r\
    \n:if ([:len \$\"src-path\"]>0) do={:set cmd \"\$cmd src-path=\\\"\$\"src-\
    path\"\\\"\"}\r\
    \n:if ([:len \$\"dst-path\"]>0) do={:set cmd \"\$cmd dst-path=\\\"\$\"dst-\
    path\"\\\"\"}\r\
    \n:if ([:len \$ascii]>0) do={:set cmd \"\$cmd ascii=\\\"\$ascii\\\"\"}\r\
    \n:if ([:len \$url]>0) do={:set cmd \"\$cmd url=\\\"\$url\\\"\"}\r\
    \n\r\
    \n:put \">> \$cmd\"\r\
    \n\r\
    \n:global FETCHRESULT\r\
    \n:set FETCHRESULT \"none\"\r\
    \n\r\
    \n:local script \"\\\r\
    \n :global FETCHRESULT;\\\r\
    \n :do {\\\r\
    \n   \$cmd;\\\r\
    \n   :set FETCHRESULT \\\"success\\\";\\\r\
    \n } on-error={\\\r\
    \n  :set FETCHRESULT \\\"failed\\\";\\\r\
    \n }\\\r\
    \n\"\r\
    \n:execute script=\$script file=\$res\r\
    \n:local cnt 0\r\
    \n#:put \"\$cnt -> \$FETCHRESULT\"\r\
    \n:while (\$cnt<100 and \$FETCHRESULT=\"none\") do={ \r\
    \n :delay 1s\r\
    \n :set \$cnt (\$cnt+1)\r\
    \n #:put \"\$cnt -> \$FETCHRESULT\"\r\
    \n}\r\
    \n:local content [/file get [find name=\$res] content]\r\
    \n#:put \$content\r\
    \nif (\$content~\"finished\") do={:return \"success\"}\r\
    \n:return \$FETCHRESULT"
add name=func_lowercase policy=read \
    source=":local alphabet {\"A\"=\"a\";\"B\"=\"b\";\"C\"=\"c\";\"D\"=\"d\";\
    \"E\"=\"e\";\"F\"=\"f\";\"G\"=\"g\";\"H\"=\"h\";\"I\"=\"i\";\"J\"=\"j\";\"\
    K\"=\"k\";\"L\"=\"l\";\"M\"=\"m\";\"N\"=\"n\";\"O\"=\"o\";\"P\"=\"p\";\"Q\
    \"=\"q\";\"R\"=\"r\";\"S\"=\"s\";\"T\"=\"t\";\"U\"=\"u\";\"V\"=\"v\";\"X\"\
    =\"x\";\"Z\"=\"z\";\"Y\"=\"y\";\"W\"=\"w\"};\r\
    \n:local result\r\
    \n:local character\r\
    \n:for strings from=0 to=([:len \$1] - 1) do={\r\
    \n\t:local single [:pick \$1 \$strings]\r\
    \n\t:set character (\$alphabet->\$single)\r\
    \n\t:if ([:typeof \$character] = \"str\") do={set single \$character}\r\
    \n\t:set result (\$result.\$single)\r\
    \n}\r\
    \n:return \$result\r\
    \n"
add name=func_uppercase policy=read \
    source=":local alphabet {\"a\"=\"A\";\"b\"=\"B\";\"c\"=\"C\";\"d\"=\"D\";\
    \"e\"=\"E\";\"f\"=\"F\";\"g\"=\"G\";\"h\"=\"H\";\"i\"=\"I\";\"j\"=\"J\";\"\
    k\"=\"K\";\"l\"=\"L\";\"m\"=\"M\";\"n\"=\"N\";\"o\"=\"O\";\"p\"=\"P\";\"q\
    \"=\"Q\";\"r\"=\"R\";\"s\"=\"S\";\"t\"=\"T\";\"u\"=\"U\";\"v\"=\"V\";\"x\"\
    =\"X\";\"z\"=\"Z\";\"y\"=\"Y\";\"w\"=\"W\"};\r\
    \n:local result\r\
    \n:local character\r\
    \n:for strings from=0 to=([:len \$1] - 1) do={\r\
    \n    :local single [:pick \$1 \$strings]\r\
    \n    :set character (\$alphabet->\$single)\r\
    \n    :if ([:typeof \$character] = \"str\") do={set single \$character}\r\
    \n    :set result (\$result.\$single)\r\
    \n}\r\
    \n:return \$result"
add name=tg_config policy=read \
    source="######################################\r\
    \n# Telegram bot API, VVS/BlackVS 2017\r\
    \n#                                Config file\r\
    \n######################################\r\
    \n:log info \"telegram configuration file has been loaded\";\r\
    \n\r\
    \n# to use config insert next lines:\r\
    \n#:local fconfig [:parse [/system script get tg_config source]]\r\
    \n#:local config [\$fconfig]\r\
    \n#:put \$config\r\
    \n\r\
    \n######################################\r\
    \n# Common parameters\r\
    \n######################################\r\
    \n\r\
    \n:local config {\r\
    \n\"Command\"=\"telegram\";\r\
    \n\t\"botAPI\"=\"xxxxxxxxxxxxxx:xxxxxxxxxx\";\r\
    \n\t\"defaultChatID\"=\"xxxxxxxxxx\";\r\
    \n\t\"trusted\"=\"xxxxxxx, xxxxxxxx, xxxxxxxx\";\r\
    \n\t\"storage\"=\"\";\r\
    \n\t\"timeout\"=5;\r\
    \n\t\"refresh_active\"=15;\r\
    \n\t\"refresh_standby\"=300;\r\
    \n\t\"available_for_public\"=true;\r\
    \n}\r\
    \nreturn \$config\r\
    \n"
add name=tg_getUpdates policy=\
    reboot,read,write,policy,test,sniff,sensitive,romon source=":global TGLAST\
    MSGID\r\
    \n:global TGLASTUPDID\r\
    \n\r\
    \n:local fconfig [:parse [/system script get tg_config source]]\r\
    \n:local http [:parse [/system script get func_fetch source]]\r\
    \n:local gkey [:parse [/system script get tg_getkey source]]\r\
    \n:local send [:parse [/system script get tg_sendMessage source]]\r\
    \n\r\
    \n:local cfg [\$fconfig]\r\
    \n:local trusted [:toarray (\$cfg->\"trusted\")]\r\
    \n:local botID (\$cfg->\"botAPI\")\r\
    \n:local storage (\$cfg->\"storage\")\r\
    \n:local timeout (\$cfg->\"timeout\")\r\
    \n:local availableForPublic [:tobool (\$cfg->\"available_for_public\")]\r\
    \n\r\
    \n:put \"cfg=\$cfg\"\r\
    \n:put \"trusted=\$trusted\"\r\
    \n:put \"botID=\$botID\"\r\
    \n:put \"storage=\$storage\"\r\
    \n:put \"timeout=\$timeout\"\r\
    \n\r\
    \n:local file (\$storage.\"tg_get_updates.txt\")\r\
    \n:local logfile (\$storage.\"tg_fetch_log.txt\")\r\
    \n#get 1 message per time\r\
    \n:local url (\"https://api.telegram.org/bot\".\$botID.\"/getUpdates\?time\
    out=\$timeout&limit=1\")\r\
    \n:if ([:len \$TGLASTUPDID]>0) do={\r\
    \n  :set url \"\$url&offset=\$(\$TGLASTUPDID+1)\"\r\
    \n}\r\
    \n\r\
    \n:put \"Reading updates...\"\r\
    \n:local res [\$http dst-path=\$file url=\$url resfile=\$logfile]\r\
    \n:if (\$res!=\"success\") do={\r\
    \n  :put \"Error getting updates\"\r\
    \n  return \"Failed get updates\"\r\
    \n}\r\
    \n:put \"Finished to read updates.\"\r\
    \n\r\
    \n:local content [/file get [/file find name=\$file] contents]\r\
    \n\r\
    \n:local msgid [\$gkey key=\"message_id\" text=\$content]\r\
    \n:if (\$msgid=\"\") do={ \r\
    \n :put \"No new updates\"\r\
    \n :return 0 \r\
    \n}\r\
    \n:set TGLASTMSGID \$msgid\r\
    \n\r\
    \n:local updid [\$gkey key=\"update_id\" text=\$content]\r\
    \n:set TGLASTUPDID \$updid\r\
    \n\r\
    \n:local fromid [\$gkey block=\"from\" key=\"id\" text=\$content]\r\
    \n:local username [\$gkey block=\"from\" key=\"username\" text=\$content]\
    \r\
    \n:local firstname [\$gkey block=\"from\" key=\"first_name\" text=\$conten\
    t]\r\
    \n:local lastname [\$gkey block=\"from\" key=\"last_name\" text=\$content]\
    \r\
    \n:local chatid [\$gkey block=\"chat\" key=\"id\" text=\$content]\r\
    \n:local chattext [\$gkey block=\"chat\" key=\"text\" text=\$content]\r\
    \n\r\
    \n:put \"message id=\$msgid\"\r\
    \n:put \"update id=\$updid\"\r\
    \n:put \"from id=\$fromid\"\r\
    \n:put \"first name=\$firstname\"\r\
    \n:put \"last name=\$lastname\"\r\
    \n:put \"username=\$username\"\r\
    \n:local name \"\$firstname \$lastname\"\r\
    \n:if ([:len \$name]<2) do {\r\
    \n :set name \$username\r\
    \n}\r\
    \n\r\
    \n:put \"in chat=\$chatid\"\r\
    \n:put \"command=\$chattext\"\r\
    \n\r\
    \n:if (!\$availableForPublic) do={\r\
    \n  :local allowed ( [:type [:find \$trusted \$fromid]]!=\"nil\" or [:type\
    \_[:find \$trusted \$chatid]]!=\"nil\")\r\
    \n  :if (!\$allowed) do={\r\
    \n  :put \"Unknown sender, keep silence\"\r\
    \n  :return -1\r\
    \n  }  \r\
    \n}\r\
    \n\r\
    \n\r\
    \n:local cmd \"\"\r\
    \n:local params \"\"\r\
    \n:local ltext [:len \$chattext]\r\
    \n\r\
    \n:local pos [:find \$chattext \" \"]\r\
    \n:if ([:type \$pos]=\"nil\") do={\r\
    \n :set cmd [:pick \$chattext 1 \$ltext]\r\
    \n} else={\r\
    \n :set cmd [:pick \$chattext 1 \$pos]\r\
    \n :set params [:pick \$chattext (\$pos+1) \$ltext]\r\
    \n}\r\
    \n\r\
    \n:local pos [:find \$cmd \"@\"]\r\
    \n:if ([:type \$pos]!=\"nil\") do={\r\
    \n :set cmd [:pick \$cmd 0 \$pos]\r\
    \n}\r\
    \n\r\
    \n:put \"cmd=<\$cmd>\"\r\
    \n:put \"params=<\$params>\"\r\
    \n\r\
    \n:local alternativeCommand {\"hi\"=\"help\"; \"start\"=\"help\"; \"hello\
    \"=\"help\"; \"support\"=\"help\"; \"assistance\"=\"help\"}\r\
    \n:if ([:typeof (\$alternativeCommand -> \$cmd)] = \"str\") do={:set cmd (\
    \$alternativeCommand -> \$cmd); :put \"cmd=<\$cmd>\"}\r\
    \n\r\
    \n:global TGLASTCMD \$cmd\r\
    \n\r\
    \n:put \"Try to invoke external script tg_cmd_\$cmd\"\r\
    \n:local script [:parse [/system script get \"tg_cmd_\$cmd\" source]]\r\
    \n\$script params=\$params chatid=\$chatid from=\$name"
add name=tg_sendMessage policy=read \
    source=":local fconfig [:parse [/system script get tg_config source]]\r\
    \n\r\
    \n:local cfg [\$fconfig]\r\
    \n:local chatID (\$cfg->\"defaultChatID\")\r\
    \n:local botID (\$cfg->\"botAPI\")\r\
    \n:local storage (\$cfg->\"storage\")\r\
    \n\r\
    \n:if ([:len \$chat]>0) do={:set chatID \$chat}\r\
    \n\r\
    \n:local url \"https://api.telegram.org/bot\$botID/sendmessage\?chat_id=\$\
    chatID&text=\$text\"\r\
    \n:if ([:len \$mode]>0) do={:set url (\$url.\"&parse_mode=\$mode\")}\r\
    \n\r\
    \n:local file (\$tgStorage.\"tg_get_updates.txt\")\r\
    \n:local logfile (\$tgStorage.\"tg_fetch_log.txt\")\r\
    \n\r\
    \n/tool fetch url=\$url keep-result=no"
add name=tg_getkey policy=read \
    source=":local cur 0\r\
    \n:local lkey [:len \$key]\r\
    \n:local res \"\"\r\
    \n:local p\r\
    \n\r\
    \n:if ([:len \$block]>0) do={\r\
    \n :set p [:find \$text \$block \$cur]\r\
    \n :if ([:type \$p]=\"nil\") do={\r\
    \n  :return \$res\r\
    \n }\r\
    \n :set cur (\$p+[:len \$block]+2)\r\
    \n}\r\
    \n\r\
    \n:set p [:find \$text \$key \$cur]\r\
    \n:if ([:type \$p]!=\"nil\") do={\r\
    \n :set cur (\$p+lkey+2)\r\
    \n :set p [:find \$text \",\" \$cur]\r\
    \n :if ([:type \$p]!=\"nil\") do={\r\
    \n   if ([:pick \$text \$cur]=\"\\\"\") do={\r\
    \n    :set res [:pick \$text (\$cur+1) (\$p-1)]\r\
    \n   } else={\r\
    \n    :set res [:pick \$text \$cur \$p]\r\
    \n   }\r\
    \n } \r\
    \n}\r\
    \n:return \$res"
add name=tg_sendAudio policy=read \
    source=":local configuration [:parse [/system script get tg_config source]\
    ]\r\
    \n:local conf [\$configuration]\r\
    \n:local chatID (\$conf->\"defaultChatID\")\r\
    \n:local botID (\$conf->\"botAPI\")\r\
    \n:local storage (\$conf->\"storage\")\r\
    \n\r\
    \n:if ([:len \$chat]>0) do={:set chatID \$chat}\r\
    \n:local url \"https://api.telegram.org/bot\$botID/sendAudio\?chat_id=\$ch\
    atID&audio=\$audio\"\r\
    \n\r\
    \n:local file (\$tgStorage.\"tg_get_updates.txt\")\r\
    \n:local logfile (\$tgStorage.\"tg_fetch_log.txt\")\r\
    \n:put \$url\r\
    \n\r\
    \n/tool fetch url=\$url keep-result=no\r\
    \n"
/system scheduler
add interval=10s name=Telegram-bot on-event="/system script run tg_getUpdates" \
    policy=reboot,read,write,policy,test,sniff,sensitive,romon \
    start-time=startup

File: /util\availableCommand
"define", "definisi", "lowercase", "lookup", "quran", "quran2", "randomize", "shorten", "uppercase", "jokes", "corona", "ipcalc", "randomcase", "capitalize", "ping"

File: /util\listSurahQuran
:local surah {
    1="Al-Fatihah","Al-Fatiha","Pembukaan","The Opening, The Opening of the Divine Writ, The Essence of the Divine Writ, The Surah of Praise, The Foundation of the Qur'an, andThe Seven Oft-Repeated","7","1";
    2="Al-Baqarah","Al-Baqarah","Sapi Betina","The Calf, The Cow","286","2";
    3="Ali ‘Imran","Al Imran","Keluarga ‘Imran","The Family of Imraan, The House of Imran","200","2";
    4="An-Nisa’","An-Nisa","Wanita","The Women","176","2";
    5="Al-Ma’idah","Al-Ma'idah","Jamuan (hidangan makanan)","The Food, The Repast, The Table","120","2";
    6="Al-An’am","Al-An'am","Hewan Ternak","The Cattle","165","1";
    7="Al-A’raf","Al-A'raf","Tempat yang tertinggi","The Heights, The Faculty of Discernment","206","1";
    8="Al-Anfal","Al-Anfal","Harta rampasan perang","The Spoils of War","75","2";
    9="At-Taubah","At-Tawbah","Pengampunan","The Repentance","129","2";
    10="Yunus","Yunus","Nabi Yunus","Jonah","109","1";
    11="Hud","Hud","Nabi Hud","Hud","123","1";
    12="Yusuf","Yusuf","Nabi Yusuf","Joseph","111","1";
    13="Ar-Ra’d","Ar-Ra'd","Guruh (petir)","The Thunder","43","1";
    14="Ibrahim","Ibrahim","Nabi Ibrahim","Abraham","52","1";
    15="Al-Hijr","Al-Hijr","Gunung Al Hijr","The Rocky Tract, The Stoneland, The Rock City, Al-Hijr","99","1";
    16="An-Nahl","An-Nahl","Lebah","The Honey Bees, The Bee","128","1";
    17="Al-Isra’","Al-Isra","Perjalanan Malam","The Night Journey","111","1";
    18="Al-Kahf","Al-Kahf","Penghuni-penghuni Gua","The Cave","110","1";
    19="Maryam","Maryam","Maryam (Maria)","Mary","98","1";
    20="Ta Ha","Ta-Ha","Ta Ha","Ṭāʾ Hāʾ (a name of Muhammad)","135","1";
    21="Al-Anbiya","Al-Anbiya","Nabi-Nabi","The Prophets","112","1";
    22="Al-Hajj","Al-Hajj","Haji","The Pilgrimage, The Hajj","78","Madinah & Makkah";
    23="Al-Mu’minun","Al-Mu'minun","Orang-orang mukmin","The Believers","118","1";
    24="An-Nur","An-Nur","Cahaya","The Light","64","2";
    25="Al-Furqan","Al-Furqan","Pembeda","The Criterion, The Standard, The Standard of True and False","77","1";
    26="Asy-Syu’ara’","Ash-Shu'ara","Penyair","The Poets","227","1";
    27="An-Naml","An-Naml","Semut","The Ant, The Ants","93","1";
    28="Al-Qasas","Al-Qasas","Kisah","The Narrations, The Stories, The Story","88","1";
    29="Al-‘Ankabut","Al-Ankabut","Laba-laba","The Spider","69","1";
    30="Ar-Rum","Ar-Rum","Bangsa Romawi","Rome, Byzantium","60","1";
    31="Luqman","Luqmaan","Keluarga Luqman","Luqman","34","1";
    32="As-Sajdah","As-Sajda","Sajdah","The Prostration, Worship, Adoration","30","1";
    33="Al-Ahzab","Al-Ahzaab","Golongan-Golongan yang bersekutu","The Clans, The Confederates, The Combined Forces","73","2";
    34="Saba’","Saba (surah)","Kaum Saba’","Sheba","54","1";
    35="Fatir","Faatir","Pencipta","The Originator","45","1";
    36="Ya Sin","Yaseen","Yaasiin","Yāʾ Sīn (a name of Muhammad)","83","1";
    37="As-Saffat","As-Saaffaat","Barisan-barisan","Those Who Set The Ranks, Drawn Up In Ranks, Those Ranged in Ranks","182","1";
    38="Sad","Saad","Shaad","Ṣād","88","1";
    39="Az-Zumar","Az-Zumar","Rombongan-rombongan","The Crowds, The Troops, Throngs","75","1";
    40="Ghafir","Ghafir","Yang mengampuni","The Forgiver (God), Forgiving","85","1";
    41="Fussilat","Fussilat","Yang dijelaskan","Expounded, Explained In Detail, Clearly Spelled Out","54","1";
    42="Asy-Syura","Ash_Shooraa","Musyawarah","The Consultation","53","1";
    43="Az-Zukhruf","Az-Zukhruf","Perhiasan","The Gold Adornments, The Ornaments of Gold, Luxury, Gold","89","1";
    44="Ad-Dukhan","Ad-Dukhaan","Kabut","The Smoke","59","1";
    45="Al-Jasiyah","Al-Jaathiyah","Yang bertekuk lutut","The Kneeling Down, Crouching","37","1";
    46="Al-Ahqaf","Al-Ahqaaf","Bukit-bukit pasir","Winding Sand-tracts, The Dunes, The Sand-Dunes","35","1";
    47="Muhammad","Muhammad","Nabi Muhammad","Muhammad","38","2";
    48="Al-Fath","Al-Fath","Kemenangan","The Victory, Conquest","29","2";
    49="Al-Hujurat","Al-Hujuraat","Kamar-kamar","The Private Apartments, The Inner Apartments","18","2";
    50="Qaf","Qaaf","Qaaf","Q̈āf","45","1";
    51="Az-Zariyat","Adh-Dhaariyaat","Angin yang menerbangkan","The Wind That Scatter, The Winnowing Winds, The Dust-Scattering Winds","60","1";
    52="At-Tur","At-Toor","Bukit","The Mount, Mount Sinai","49","1";
    53="An-Najm","An-Najm","Bintang","The Star, The Unfolding","62","1";
    54="Al-Qamar","Al-Qamar","Bulan","The Moon","55","1";
    55="Ar-Rahman","Ar-Rahman","Yang Maha Pemurah","The Most Merciful, The Most Gracious","78","Madinah & Mekkah";
    56="Al-Waqi’ah","Al-Waqi'a","Hari Kiamat","The Inevitable, The Event, That Which Must Come to Pass","96","1";
    57="Al-Hadid","Al-Hadeed","Besi","The Iron","29","2";
    58="Al-Mujadilah","Al-Mujadila","Wanita yang mengajukan gugatan","The Pleading, The Pleading Woman","22","2";
    59="Al-Hasyr","Al-Hashr","Pengusiran","The Mustering, The Gathering, Exile, Banishment","24","2";
    60="Al-Mumtahanah","Al-Mumtahanah","Wanita yang diuji","The Examined One, She That Is To Be Examined","13","2";
    61="As-Saff","As-Saff","Satu barisan","The Ranks, Battle Array","14","2";
    62="Al-Jumu’ah","Al-Jumu'ah","Hari Jum’at","Congregation, Friday","11","2";
    63="Al-Munafiqun","Al-Munafiqoon","Orang-orang yang munafik","The Hypocrites","11","2";
    64="At-Tagabun","At-Taghabun","Hari dinampakkan kesalahan-kesalahan","The Cheating, The Mutual Disillusion, The Mutual Loss and Gain, Loss and Gain","18","2";
    65="At-Talaq","At-Talaq","Talak","Divorce","12","2";
    66="At-Tahrim","At-Tahreem","Mengharamkan","The Prohibition","12","2";
    67="Al-Mulk","Al-Mulk","Kerajaan","The Dominion, Sovereignty, Control","30","1";
    68="Al-Qalam","Al-Qalam","Pena","The Pen","52","1";
    69="Al-Haqqah","Al-Haaqqa","Hari kiamat","The Sure Reality, The Laying-Bare of the Truth","52","1";
    70="Al-Ma’arij","Al-Ma'aarij","Tempat naik","The Ways of Ascent, The Ascending Stairways","44","1";
    71="Nuh","Nooh","Nabi Nuh","Noah","28","1";
    72="Al-Jinn","Al-Jinn","Jin","The Jinn, The Spirits, The Unseen Beings","28","1";
    73="Al-Muzzammil","Al-Muzzammil","Orang yang berselimut","The Enfolded One, The Enshrouded One, Bundled Up, The Enwrapped One","20","1";
    74="Al-Muddassir","Al-Muddaththir","Orang yang berkemul","The One Wrapped Up, The Cloaked One, The Man Wearing A Cloak, The Enfolded One","56","1";
    75="Al-Qiyamah","Al-Qiyamah","Kiamat","Resurrection, The Day of Resurrection, Rising Of The Dead","40","1";
    76="Al-Insan","Al-Insaan","Manusia","The Human, Man","31","2";
    77="Al-Mursalat","Al-Mursalaat","Malaikat-Malaikat Yang Diutus","Those Sent Forth, The Emissaries, Winds Sent Forth","50","1";
    78="An-Naba’","An-Naba'","Berita besar","The Great News, The Announcement, The Tiding","40","1";
    79="An-Nazi’at","An-Naazi'aat","Malaikat-Malaikat Yang Mencabut","Those Who Tear Out, Those Who Drag Forth, Soul-snatchers, Those That Rise","46","1";
    80="‘Abasa","Abasa","Ia Bermuka masam","He Frowned","42","1";
    81="At-Takwir","At-Takweer","Menggulung","The Folding Up, The Overthrowing, Shrouding in Darkness","29","1";
    82="Al-Infitar","Al-Infitar","Terbelah","The Cleaving Asunder, Bursting Apart","19","1";
    83="Al-Tatfif","Al-Mutaffifeen","Orang-orang yang curang","The Dealers in Fraud, Defrauding, The Cheats, Those Who Give Short Measure","36","1";
    84="Al-Insyiqaq","Al-Inshiqaaq","Terbelah","The Rending Asunder, The Sundering, Splitting Open, The Splitting Asunder","25","1";
    85="Al-Buruj","Al-Burooj","Gugusan bintang","The Mansions Of The Stars, The Constellations, The Great Constellations","22","1";
    86="At-Tariq","At-Taariq","Yang datang di malam hari","The Night-Visitant, The Morning Star, The Nightcomer, That Which Comes in the Night","17","1";
    87="Al-A’la","Al-A'laa","Yang paling tinggi","The Most High, The All-Highest, Glory To Your Lord In The Highest","19","1";
    88="Al-Gasyiyah","Al-Ghaashiyah","Hari Pembalasan","The Overwhelming Event, The Overshadowing Event, The Pall","26","1";
    89="Al-Fajr","Al-Fajr","Fajar","The Break of Day, The Daybreak, The Dawn","30","1";
    90="Al-Balad","Al-Balad","Negeri","The City, The Land","20","1";
    91="Asy-Syams","Ash-Shams","Matahari","The Sun","15","1";
    92="Al-Lail","Al-Layl","Malam","The Night","21","1";
    93="Ad-Duha","Ad-Dhuha","Waktu matahari sepenggalahan naik (Dhuha)","The Glorious Morning Light, The Forenoon, Morning Hours, Morning Bright, The Bright Morning Hours","11","1";
    94="Al-Insyirah","Ash-Sharh (Al-Inshirah)","Melapangkan","The Expansion of Breast, Solace, Consolation, Relief, Patient, The Opening-Up of the Heart","8","1";
    95="At-Tin","At-Teen","Buah Tin","The Fig Tree, The Fig","8","1";
    96="Al-‘Alaq","Al-'Alaq","Segumpal Darah","The Clinging Clot, Clot of Blood, The Germ-Cell","19","1";
    97="Al-Qadr","Al-Qadr","Kemuliaan","The Night of Honor, The Night of Decree, Power, Fate, Destiny","5","1";
    98="Al-Bayyinah","Al-Bayyinahh","Pembuktian","The Clear Evidence, The Evidence of the Truth","8","2";
    99="Az-Zalzalah","Az-Zalzalah","Kegoncangan","The Earthquake","8","2";
    100="Al-‘Adiyat","Al-'Aadiyaat","Berlari kencang","The Courser, The Chargers, The War Horse","11","1";
    101="Al-Qari’ah","Al-Qaari'ah","Hari Kiamat","The Striking Hour, The Great Calamity, The Stunning Blow, The Sudden Calamity","11","1";
    102="At-Takasur","At-Takaathur","Bermegah-megahan","The Piling Up, Rivalry in World Increase, Competition, Greed for More and More","8","1";
    103="Al-‘Asr","Al-'Asr","Masa/Waktu","The Time, The Declining Day, The Epoch, The Flight of Time","3","1";
    104="Al-Humazah","Al-Humazah","Pengumpat","The Scandalmonger, The Traducer, The Gossipmonger, The Slanderer","9","1";
    105="Al-Fil","Al-Feel","Gajah","The Elephant","5","1";
    106="Quraisy","Quraysh","Suku Quraisy","The Quraysh","4","1";
    107="Al-Ma’un","Al-Maa'oon","Barang-barang yang berguna","The Neighbourly Assistance, Small Kindnesses, Almsgiving, Assistance","7","1";
    108="Al-Kausar","Al-Kawthar","Nikmat yang berlimpah","Abundance, Plenty, Good in Abundance","3","1";
    109="Al-Kafirun","Al-Kaafiroon","Orang-orang kafir","The Disbelievers, The Kuffar, Those Who Deny the Truth","6","1";
    110="An-Nasr","An-Nasr","Pertolongan","The Help, Divine Support, Victory, Succour","3","2";
    111="Al-Lahab","Al-Masad","Gejolak Api / Sabut","The Plaited Rope, The Palm Fibre, The Twisted Strands","5","1";
    112="Al-Ikhlas","Al-Ikhlaas","Ikhlas","Purity of Faith, The Fidelity, The Declaration of [God's] Perfection","4","1";
    113="Al-Falaq","Al-Falaq","Waktu Subuh","The Daybreak, Dawn, The Rising Dawn","5","1";
    114="An-Nas","Al-Naas","Umat Manusia","Mankind, Men","6","1";
}
:return $surah

File: /util\randomizeScript
:local hour [:pick [/system clock get time] 0 2];
:local hourx;
:local minute [:pick [/system clock get time] 3 5];
:local minutex;
:local second [:pick [/system clock get time] 6 8];
:local secondx;
:local hundred ("1$second");
:local hundred2 ("1$minute");
:local hundred3 ("1$hour");
:local utsec;
:local uthour;
:local utmin;
:local uptime [/system resource get uptime];
:if ([:len $uptime] = 10) do={:set utsec [:pick $uptime 8 10]; :set utmin [:pick $uptime 5 7]; :set uthour [:pick $uptime 2 4]};
:if ([:len $uptime] = 11) do={:set utsec [:pick $uptime 9 11]; :set utmin [:pick $uptime 6 8]; :set uthour [:pick $uptime 3 5]};
:if ([:len $uptime] = 12) do={:set utsec [:pick $uptime 10 12]; :set utmin [:pick $uptime 7 9]; :set uthour [:pick $uptime 4 6]};
:if ([:len $uptime] = 8) do={:set utsec [:pick $uptime 6 8]; :set utmin [:pick $uptime 3 5]; :set uthour [:pick $uptime 0 2]};
:if (([:len $uptime] != 12) and ([:len $uptime] != 10) and ([:len $uptime] != 11) and ([:len $uptime] != 8)) do={
    /log error message="Script error please contact the creator";
}
:local utsecx ([:pick $utsec 1].[:pick $utsec 0]);
:if (([:pick $hour 1] = [:pick $hour 0]) or ([:pick $minute 1] = [:pick $minute 0]) or ([:pick $second 1] = [:pick $second 0])) do={
    :set hourx (([:pick $hour 1].[:pick $hour 0]) + 1);
    :set minutex (([:pick $minute 1].[:pick $minute 0]) + 1);
    :set secondx (([:pick $second 1].[:pick $second 0]) + 8);
} else={
    :set hourx ([:pick $hour 1].[:pick $hour 0]);
    :set minutex ([:pick $minute 1].[:pick $minute 0]);
    :set secondx ([:pick $second 1].[:pick $second 0]);
}
:if ($hundred2 = $hundred) do={:set hundred2 ($hundred2 + $hour + 1)};
:if (($hundred3 = $hundred) or ($hundred3 = $hundred2)) do={ :set hundred3 ($hundred3 + $second)};
:if ($minute + $utsec - $hour < 5) do={
    :set utsec ($utsec + 25);
    :set minute ($minute + 60);
}
:local string
:if ($type = "string") do={
    :set string ("FbPTYV9mjUNF4JWq4y1tD6sjdak0t2m8EbvSOIJ5zSXx2zBzTdVbreMTTtYNu2n0y383CHqASakcmw3NnhAeU6szwSsSqasDaMytTnw0CEzglNhbMyfGUkHfQexNk5C0m4iICxIQm\
                XotuYvGvbJO5XhzGHt3Xb2al4chtzNvTBnniz9RfrdqzTQHixeLh1uvHJ1xP885MLm025D6vzBNmPLWl0GX64zXbABIWudpcfhzrcl2mg11FYXHYAdi5XggVblwizY9Rt4a2Utvmi1\
                mmhbtTX2gVntOh3jotnUOD5nB69d4bnnUGoth");
}
:if ($type = "integer") do={
    :set string ("857942409324079924597220765691387859683055723045203124933189298538729356872140414647102436510066373639151713513171131252244546015539855265455\
                5810892943759503660388434505376119325439189112229996798299967611622498655616397194432203904171831777728491020225711996450683469478597214223062\
                27212493834056443900559616751");
}

:local RandomString;
:set RandomString 	([:pick $string ($utsecx + $utmin)].[:pick $string ($utsecx + 50)].[:pick $string ($utsecx + $hour + 29)].[:pick $string ($utsecx)].\
                    [:pick $string ($utsec + 21)].[:pick $string ($second + utmin)].[:pick $string ($second + uthour + 100)].[:pick $string ($utsec + 29)].\
                    [:pick $string ($utsec + $hourx)].[:pick $string ($second + uthour + 1)].[:pick $string ($second + uthour)].[:pick $string ($secondx + $uthour)].\
                    [:pick $string ($minute + $utsec - $hour)].[:pick $string ($minute + $uthour + $secondx)].[:pick $string [:tonum ($hundred + $uthour)]].\
                    [:pick $string [:tonum ($hundred2 + $utsec)]].[:pick $string [:tonum $hundred3]].[:pick $string ($utmin + $hourx + $second)].\
                    [:pick $string ($hourx + $hour + $second)].[:pick $string ($secondx + $utsec)]);
:return $RandomString;

