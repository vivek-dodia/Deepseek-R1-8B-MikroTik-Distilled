# Repository Information
Name: mikrotikapi

# Directory Structure
Directory structure:
└── github_repos/mikrotikapi/
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
    │   │       ├── pack-5eba6f8445fad1600b01c400484ec05e0f00927c.idx
    │   │       └── pack-5eba6f8445fad1600b01c400484ec05e0f00927c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── composer.json
    ├── composer.lock
    ├── config/
    │   └── mikrotik.php
    ├── phpunit.xml
    ├── readme.md
    ├── src/
    │   ├── Commands/
    │   │   ├── Command.php
    │   │   ├── Interfaces.php
    │   │   └── Ip.php
    │   ├── Contracts/
    │   │   ├── ClientContract.php
    │   │   ├── CommandContract.php
    │   │   └── MikrotikContract.php
    │   ├── Core/
    │   │   ├── Client.php
    │   │   ├── Collection.php
    │   │   ├── QueryBuilder.php
    │   │   └── Request.php
    │   ├── Entity/
    │   │   ├── Address.php
    │   │   ├── Bridge.php
    │   │   ├── Entity.php
    │   │   ├── Ethernet.php
    │   │   ├── GenericEntity.php
    │   │   └── InterfaceEntity.php
    │   ├── Exceptions/
    │   │   ├── CommandException.php
    │   │   ├── ConnectionException.php
    │   │   ├── InvalidCommandException.php
    │   │   └── WrongArgumentTypeException.php
    │   ├── Facades/
    │   │   └── MikrotikFacade.php
    │   ├── Mikrotik.php
    │   ├── MikrotikServiceProvider.php
    │   └── Support/
    │       ├── EntityUtils.php
    │       └── InterfaceEnums.php
    └── tests/
        ├── AuthTest.php
        ├── InterfacesCommandsTest.php
        ├── IpCommandsTest.php
        ├── StaticCommandTest.php
        └── Traits/
            └── CreateApplication.php


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
	url = https://github.com/jjcodes78/mikrotikapi.git
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
0000000000000000000000000000000000000000 aa71e3cfcf605d81061d174e2f2b7783ea17ea7c vivek-dodia <vivek.dodia@icloud.com> 1738606007 -0500	clone: from https://github.com/jjcodes78/mikrotikapi.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 aa71e3cfcf605d81061d174e2f2b7783ea17ea7c vivek-dodia <vivek.dodia@icloud.com> 1738606007 -0500	clone: from https://github.com/jjcodes78/mikrotikapi.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 aa71e3cfcf605d81061d174e2f2b7783ea17ea7c vivek-dodia <vivek.dodia@icloud.com> 1738606007 -0500	clone: from https://github.com/jjcodes78/mikrotikapi.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
aa71e3cfcf605d81061d174e2f2b7783ea17ea7c refs/remotes/origin/master
5413ff241b977dcbff686b2aef49182a087dae1b refs/tags/0.1


File: /.git\refs\heads\master
aa71e3cfcf605d81061d174e2f2b7783ea17ea7c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/node_modules
/public/storage
/public/hot
/storage/*.key
/bootstrap
/vendor
/.idea
Homestead.json
Homestead.yaml
.env


File: /composer.json
{
  "name": "jjsquady/mikrotikapi",
  "description": "An Mikrotik Api Wrapper",
   "minimum-stability": "dev",
   "prefer-stable": true,
  "license": "MIT",
  "authors": [
    {
      "name": "Jorge 'jjsquady' Junior",
      "email": "jjsquady@gmail.com"
    }
  ],
  "autoload": {
        "psr-4": {
            "jjsquady\\MikrotikApi\\": "src/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "jjsquady\\MikrotikApi\\Tests\\": "tests/"
        }
    },

    "require": {
        "php": "^7.4",
        "pear2/net_routeros": "1.0.0b6",
        "pear2/net_transmitter": "1.0.0b2"
    },
    "require-dev": {
        "laravel/framework": "^8.11",
        "orchestra/testbench": "^6.2",
        "phpunit/phpunit": "^9.4"
    },
    "extra": {
        "branch-alias": {
            "dev-master": "1.0-dev"
        },
        "laravel": {
            "providers": [
                "jjsquady\\MikrotikApi\\MikrotikServiceProvider"
            ],
            "aliases": {
                "Mikrotik": "jjsquady\\MikrotikApi\\Facades\\MikrotikFacade"
            }
        }
    },
    "config": {
        "sort-packages": true
    },
    "scripts": {
        "test": "vendor/bin/phpunit"
    }
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "20ccb06881e598823405ab42e11cbd31",
    "packages": [
        {
            "name": "pear2/net_routeros",
            "version": "1.0.0b5",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_RouterOS.git",
                "reference": "db24b8c4cd63d593dc8387987a954926d96cafb8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_RouterOS/zipball/db24b8c4cd63d593dc8387987a954926d96cafb8",
                "reference": "db24b8c4cd63d593dc8387987a954926d96cafb8",
                "shasum": ""
            },
            "require": {
                "pear2/net_transmitter": ">=1.0.0a5",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "pear2/cache_shm": "dev-develop",
                "pear2/console_color": "dev-develop",
                "pear2/console_commandline": "dev-master",
                "phpunit/phpunit": "@stable",
                "squizlabs/php_codesniffer": "@stable"
            },
            "suggest": {
                "ext-apc": "This or Wincache is required for persistent connections.",
                "ext-openssl": "Enables encrypted connections.",
                "ext-wincache": "This or APC is required for persistent connections. Reccomended instead of APC on Windows.",
                "pear2/cache_shm": "Enables persistent connections.",
                "pear2/console_color": "Enables colors in the console",
                "pear2/console_commandline": "Enables the console"
            },
            "bin": [
                "scripts/roscon.php"
            ],
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Net\\RouterOS\\": "src/",
                    "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
                    "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
                    "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Vasil Rangelov",
                    "email": "boen.robot@gmail.com",
                    "role": "lead"
                }
            ],
            "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
            "homepage": "http://pear2.github.com/Net_RouterOS/",
            "keywords": [
                "api",
                "mikrotik",
                "package",
                "pear2",
                "router",
                "routeros"
            ],
            "time": "2014-11-04T12:52:46+00:00"
        },
        {
            "name": "pear2/net_transmitter",
            "version": "1.0.0a5",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_Transmitter.git",
                "reference": "ac4d5fe6b7fd1a25f9a45c4454a8e85462837370"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_Transmitter/zipball/ac4d5fe6b7fd1a25f9a45c4454a8e85462837370",
                "reference": "ac4d5fe6b7fd1a25f9a45c4454a8e85462837370",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "pear2/cache_shm": "dev-develop",
                "phpunit/phpunit": "@stable"
            },
            "suggest": {
                "ext-apc": ">=3.0.13",
                "ext-openssl": "*",
                "ext-wincache": ">=1.1.0",
                "pear2/cache_shm": ">=0.1.3"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Net\\Transmitter\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Vasil Rangelov",
                    "email": "boen.robot@gmail.com",
                    "role": "lead"
                }
            ],
            "description": "A stream wrapper that ensures data integrity. Particularly useful for sockets.",
            "homepage": "http://pear2.github.com/Net_Transmitter/",
            "keywords": [
                "Socket",
                "integrity",
                "network",
                "networking",
                "package",
                "pear2",
                "sockets"
            ],
            "time": "2014-11-02T05:04:39+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "composer/xdebug-handler",
            "version": "1.3.3",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/xdebug-handler.git",
                "reference": "46867cbf8ca9fb8d60c506895449eb799db1184f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/xdebug-handler/zipball/46867cbf8ca9fb8d60c506895449eb799db1184f",
                "reference": "46867cbf8ca9fb8d60c506895449eb799db1184f",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.2 || ^7.0",
                "psr/log": "^1.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.5"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Composer\\XdebugHandler\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "John Stevenson",
                    "email": "john-stevenson@blueyonder.co.uk"
                }
            ],
            "description": "Restarts a process without xdebug.",
            "keywords": [
                "Xdebug",
                "performance"
            ],
            "time": "2019-05-27T17:52:04+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "1.3.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "45d9b132b262c1d03835cdeefd42938d881556fa"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/45d9b132b262c1d03835cdeefd42938d881556fa",
                "reference": "45d9b132b262c1d03835cdeefd42938d881556fa",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Inflector\\": "lib/Doctrine/Common/Inflector"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Common String Manipulations with regard to casing and singular/plural rules.",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "inflection",
                "pluralize",
                "singularize",
                "string"
            ],
            "time": "2018-06-15T19:03:38+00:00"
        },
        {
            "name": "doctrine/instantiator",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "fb21dea73761426178f8665f6b567c58fee488ff"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/fb21dea73761426178f8665f6b567c58fee488ff",
                "reference": "fb21dea73761426178f8665f6b567c58fee488ff",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpbench/phpbench": "^0.13",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpstan/phpstan-shim": "^0.11",
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Instantiator\\": "src/Doctrine/Instantiator/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "http://ocramius.github.com/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://www.doctrine-project.org/projects/instantiator.html",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "time": "2019-05-24T18:15:18+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "975c0e44ab85fb72acc5be2082464e74cade966b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/975c0e44ab85fb72acc5be2082464e74cade966b",
                "reference": "975c0e44ab85fb72acc5be2082464e74cade966b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2"
            },
            "require-dev": {
                "doctrine/coding-standard": "^6.0",
                "phpstan/phpstan": "^0.11.8",
                "phpunit/phpunit": "^8.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Lexer\\": "lib/Doctrine/Common/Lexer"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Lexer parser library that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "https://www.doctrine-project.org/projects/lexer.html",
            "keywords": [
                "annotations",
                "docblock",
                "lexer",
                "parser",
                "php"
            ],
            "time": "2019-06-11T06:26:51+00:00"
        },
        {
            "name": "dragonmantank/cron-expression",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/dragonmantank/cron-expression.git",
                "reference": "1aba9b92960c86e606aa9acf370817a23797179e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dragonmantank/cron-expression/zipball/1aba9b92960c86e606aa9acf370817a23797179e",
                "reference": "1aba9b92960c86e606aa9acf370817a23797179e",
                "shasum": ""
            },
            "require": {
                "php": "^7.2",
                "phpstan/phpstan": "^0.11"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.4|^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Cron\\": "src/Cron/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com",
                    "homepage": "https://github.com/mtdowling"
                },
                {
                    "name": "Chris Tankersley",
                    "email": "chris@ctankersley.com",
                    "homepage": "https://github.com/dragonmantank"
                }
            ],
            "description": "CRON for PHP: Calculate the next or previous run date and determine if a CRON expression is due",
            "keywords": [
                "cron",
                "schedule"
            ],
            "time": "2019-03-31T01:04:45+00:00"
        },
        {
            "name": "egulias/email-validator",
            "version": "2.1.9",
            "source": {
                "type": "git",
                "url": "https://github.com/egulias/EmailValidator.git",
                "reference": "128cc721d771ec2c46ce59698f4ca42b73f71b25"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/egulias/EmailValidator/zipball/128cc721d771ec2c46ce59698f4ca42b73f71b25",
                "reference": "128cc721d771ec2c46ce59698f4ca42b73f71b25",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "^1.0.1",
                "php": ">= 5.5"
            },
            "require-dev": {
                "dominicsayers/isemail": "dev-master",
                "phpunit/phpunit": "^4.8.35||^5.7||^6.0",
                "satooshi/php-coveralls": "^1.0.1"
            },
            "suggest": {
                "ext-intl": "PHP Internationalization Libraries are required to use the SpoofChecking validation"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Egulias\\EmailValidator\\": "EmailValidator"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Eduardo Gulias Davis"
                }
            ],
            "description": "A library for validating emails against several RFCs",
            "homepage": "https://github.com/egulias/EmailValidator",
            "keywords": [
                "email",
                "emailvalidation",
                "emailvalidator",
                "validation",
                "validator"
            ],
            "time": "2019-06-23T10:14:27+00:00"
        },
        {
            "name": "erusev/parsedown",
            "version": "1.8.0-beta-7",
            "source": {
                "type": "git",
                "url": "https://github.com/erusev/parsedown.git",
                "reference": "fe7a50eceb4a3c867cc9fa9c0aa906b1067d1955"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/erusev/parsedown/zipball/fe7a50eceb4a3c867cc9fa9c0aa906b1067d1955",
                "reference": "fe7a50eceb4a3c867cc9fa9c0aa906b1067d1955",
                "shasum": ""
            },
            "require": {
                "ext-mbstring": "*",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "Parsedown": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Emanuil Rusev",
                    "email": "hello@erusev.com",
                    "homepage": "http://erusev.com"
                }
            ],
            "description": "Parser for Markdown.",
            "homepage": "http://parsedown.org",
            "keywords": [
                "markdown",
                "parser"
            ],
            "time": "2019-03-17T18:47:21+00:00"
        },
        {
            "name": "fzaninotto/faker",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/fzaninotto/Faker.git",
                "reference": "fb218ada627f7c750c6e0e41cae486d2db48e911"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fzaninotto/Faker/zipball/fb218ada627f7c750c6e0e41cae486d2db48e911",
                "reference": "fb218ada627f7c750c6e0e41cae486d2db48e911",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "ext-intl": "*",
                "phpunit/phpunit": "^4.8.35 || ^5.7",
                "squizlabs/php_codesniffer": "^1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Faker\\": "src/Faker/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "François Zaninotto"
                }
            ],
            "description": "Faker is a PHP library that generates fake data for you.",
            "keywords": [
                "data",
                "faker",
                "fixtures"
            ],
            "time": "2019-04-16T09:48:34+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "c0436bf63689fc334f67ccaa5e17458af9700b42"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/c0436bf63689fc334f67ccaa5e17458af9700b42",
                "reference": "c0436bf63689fc334f67ccaa5e17458af9700b42",
                "shasum": ""
            },
            "require": {
                "php": "^5.3|^7.0"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "^1.4",
                "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0",
                "satooshi/php-coveralls": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "hamcrest"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "time": "2019-04-18T04:49:30+00:00"
        },
        {
            "name": "jean85/pretty-package-versions",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/Jean85/pretty-package-versions.git",
                "reference": "d6d851930b4433d9ac005c0aed87fc882d3eb994"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Jean85/pretty-package-versions/zipball/d6d851930b4433d9ac005c0aed87fc882d3eb994",
                "reference": "d6d851930b4433d9ac005c0aed87fc882d3eb994",
                "shasum": ""
            },
            "require": {
                "ocramius/package-versions": "^1.2.0",
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Jean85\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alessandro Lai",
                    "email": "alessandro.lai85@gmail.com"
                }
            ],
            "description": "A wrapper for ocramius/package-versions to get pretty versions strings",
            "keywords": [
                "composer",
                "package",
                "release",
                "versions"
            ],
            "time": "2019-01-14T10:28:42+00:00"
        },
        {
            "name": "laravel/framework",
            "version": "5.8.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/framework.git",
                "reference": "a9f880df1350cd755a41ec8eaafdffa3bc982aad"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/framework/zipball/a9f880df1350cd755a41ec8eaafdffa3bc982aad",
                "reference": "a9f880df1350cd755a41ec8eaafdffa3bc982aad",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.1",
                "dragonmantank/cron-expression": "^2.0",
                "egulias/email-validator": "^2.0",
                "erusev/parsedown": "^1.7",
                "ext-json": "*",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "league/flysystem": "^1.0.8",
                "monolog/monolog": "^1.12",
                "nesbot/carbon": "^1.26.3 || ^2.0",
                "opis/closure": "^3.1",
                "php": "^7.1.3",
                "psr/container": "^1.0",
                "psr/simple-cache": "^1.0",
                "ramsey/uuid": "^3.7",
                "swiftmailer/swiftmailer": "^6.0",
                "symfony/console": "^4.2",
                "symfony/debug": "^4.2",
                "symfony/finder": "^4.2",
                "symfony/http-foundation": "^4.2",
                "symfony/http-kernel": "^4.2",
                "symfony/process": "^4.2",
                "symfony/routing": "^4.2",
                "symfony/var-dumper": "^4.2",
                "tijsverkoyen/css-to-inline-styles": "^2.2.1",
                "vlucas/phpdotenv": "^3.3"
            },
            "conflict": {
                "tightenco/collect": "<5.5.33"
            },
            "replace": {
                "illuminate/auth": "self.version",
                "illuminate/broadcasting": "self.version",
                "illuminate/bus": "self.version",
                "illuminate/cache": "self.version",
                "illuminate/config": "self.version",
                "illuminate/console": "self.version",
                "illuminate/container": "self.version",
                "illuminate/contracts": "self.version",
                "illuminate/cookie": "self.version",
                "illuminate/database": "self.version",
                "illuminate/encryption": "self.version",
                "illuminate/events": "self.version",
                "illuminate/filesystem": "self.version",
                "illuminate/hashing": "self.version",
                "illuminate/http": "self.version",
                "illuminate/log": "self.version",
                "illuminate/mail": "self.version",
                "illuminate/notifications": "self.version",
                "illuminate/pagination": "self.version",
                "illuminate/pipeline": "self.version",
                "illuminate/queue": "self.version",
                "illuminate/redis": "self.version",
                "illuminate/routing": "self.version",
                "illuminate/session": "self.version",
                "illuminate/support": "self.version",
                "illuminate/translation": "self.version",
                "illuminate/validation": "self.version",
                "illuminate/view": "self.version"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^3.0",
                "doctrine/dbal": "^2.6",
                "filp/whoops": "^2.1.4",
                "guzzlehttp/guzzle": "^6.3",
                "league/flysystem-cached-adapter": "^1.0",
                "mockery/mockery": "^1.0",
                "moontoast/math": "^1.1",
                "orchestra/testbench-core": "3.8.*",
                "pda/pheanstalk": "^4.0",
                "phpunit/phpunit": "^7.5|^8.0",
                "predis/predis": "^1.1.1",
                "symfony/css-selector": "^4.2",
                "symfony/dom-crawler": "^4.2",
                "true/punycode": "^2.1"
            },
            "suggest": {
                "aws/aws-sdk-php": "Required to use the SQS queue driver and SES mail driver (^3.0).",
                "doctrine/dbal": "Required to rename columns and drop SQLite columns (^2.6).",
                "ext-pcntl": "Required to use all features of the queue worker.",
                "ext-posix": "Required to use all features of the queue worker.",
                "filp/whoops": "Required for friendly error pages in development (^2.1.4).",
                "fzaninotto/faker": "Required to use the eloquent factory builder (^1.4).",
                "guzzlehttp/guzzle": "Required to use the Mailgun and Mandrill mail drivers and the ping methods on schedules (^6.0).",
                "laravel/tinker": "Required to use the tinker console command (^1.0).",
                "league/flysystem-aws-s3-v3": "Required to use the Flysystem S3 driver (^1.0).",
                "league/flysystem-cached-adapter": "Required to use the Flysystem cache (^1.0).",
                "league/flysystem-rackspace": "Required to use the Flysystem Rackspace driver (^1.0).",
                "league/flysystem-sftp": "Required to use the Flysystem SFTP driver (^1.0).",
                "moontoast/math": "Required to use ordered UUIDs (^1.1).",
                "nexmo/client": "Required to use the Nexmo transport (^1.0).",
                "pda/pheanstalk": "Required to use the beanstalk queue driver (^4.0).",
                "predis/predis": "Required to use the redis cache and queue drivers (^1.0).",
                "pusher/pusher-php-server": "Required to use the Pusher broadcast driver (^3.0).",
                "symfony/css-selector": "Required to use some of the crawler integration testing tools (^4.2).",
                "symfony/dom-crawler": "Required to use most of the crawler integration testing tools (^4.2).",
                "symfony/psr-http-message-bridge": "Required to use PSR-7 bridging features (^1.1).",
                "wildbit/swiftmailer-postmark": "Required to use Postmark mail driver (^3.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.8-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/Illuminate/Foundation/helpers.php",
                    "src/Illuminate/Support/helpers.php"
                ],
                "psr-4": {
                    "Illuminate\\": "src/Illuminate/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Taylor Otwell",
                    "email": "taylor@laravel.com"
                }
            ],
            "description": "The Laravel Framework.",
            "homepage": "https://laravel.com",
            "keywords": [
                "framework",
                "laravel"
            ],
            "time": "2019-06-23T08:18:21+00:00"
        },
        {
            "name": "league/flysystem",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/flysystem.git",
                "reference": "741e9792d5f4efa1453513cb3adf6cf767090b82"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/flysystem/zipball/741e9792d5f4efa1453513cb3adf6cf767090b82",
                "reference": "741e9792d5f4efa1453513cb3adf6cf767090b82",
                "shasum": ""
            },
            "require": {
                "ext-fileinfo": "*",
                "php": ">=5.5.9"
            },
            "conflict": {
                "league/flysystem-sftp": "<1.0.6"
            },
            "require-dev": {
                "phpspec/phpspec": "^3.4",
                "phpunit/phpunit": "^5.7.10"
            },
            "suggest": {
                "ext-fileinfo": "Required for MimeType",
                "ext-ftp": "Allows you to use FTP server storage",
                "ext-openssl": "Allows you to use FTPS server storage",
                "league/flysystem-aws-s3-v2": "Allows you to use S3 storage with AWS SDK v2",
                "league/flysystem-aws-s3-v3": "Allows you to use S3 storage with AWS SDK v3",
                "league/flysystem-azure": "Allows you to use Windows Azure Blob storage",
                "league/flysystem-cached-adapter": "Flysystem adapter decorator for metadata caching",
                "league/flysystem-eventable-filesystem": "Allows you to use EventableFilesystem",
                "league/flysystem-rackspace": "Allows you to use Rackspace Cloud Files",
                "league/flysystem-sftp": "Allows you to use SFTP server storage via phpseclib",
                "league/flysystem-webdav": "Allows you to use WebDAV storage",
                "league/flysystem-ziparchive": "Allows you to use ZipArchive adapter",
                "spatie/flysystem-dropbox": "Allows you to use Dropbox storage",
                "srmklive/flysystem-dropbox-v2": "Allows you to use Dropbox storage for PHP 5 applications"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "League\\Flysystem\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Frank de Jonge",
                    "email": "info@frenky.net"
                }
            ],
            "description": "Filesystem abstraction: Many filesystems, one API.",
            "keywords": [
                "Cloud Files",
                "WebDAV",
                "abstraction",
                "aws",
                "cloud",
                "copy.com",
                "dropbox",
                "file systems",
                "files",
                "filesystem",
                "filesystems",
                "ftp",
                "rackspace",
                "remote",
                "s3",
                "sftp",
                "storage"
            ],
            "time": "2019-06-20T20:52:55+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "0eb0b48c3f07b3b89f5169ce005b7d05b18cf1d2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/0eb0b48c3f07b3b89f5169ce005b7d05b18cf1d2",
                "reference": "0eb0b48c3f07b3b89f5169ce005b7d05b18cf1d2",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "~2.0",
                "lib-pcre": ">=7.0",
                "php": ">=5.6.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~5.7.10|~6.5|~7.0|~8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Mockery": "library/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Pádraic Brady",
                    "email": "padraic.brady@gmail.com",
                    "homepage": "http://blog.astrumfutura.com"
                },
                {
                    "name": "Dave Marshall",
                    "email": "dave.marshall@atstsolutions.co.uk",
                    "homepage": "http://davedevelopment.co.uk"
                }
            ],
            "description": "Mockery is a simple yet flexible PHP mock object framework",
            "homepage": "https://github.com/mockery/mockery",
            "keywords": [
                "BDD",
                "TDD",
                "library",
                "mock",
                "mock objects",
                "mockery",
                "stub",
                "test",
                "test double",
                "testing"
            ],
            "time": "2019-02-13T09:37:52+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "1.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "4d5b7e6ba1127789c7ff59d6f762298eaa29787f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/4d5b7e6ba1127789c7ff59d6f762298eaa29787f",
                "reference": "4d5b7e6ba1127789c7ff59d6f762298eaa29787f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "psr/log": "~1.0"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "graylog2/gelf-php": "~1.0",
                "jakub-onderka/php-parallel-lint": "0.9",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpunit/phpunit": "~4.5",
                "phpunit/phpunit-mock-objects": "2.3.0",
                "ruflin/elastica": ">=0.90 <3.0",
                "sentry/sentry": "^0.13",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mongo": "Allow sending log messages to a MongoDB server",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server via PHP Driver",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server",
                "sentry/sentry": "Allow sending log messages to a Sentry server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Monolog\\": "src/Monolog"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "http://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "http://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "time": "2018-12-26T14:24:03+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "e6828efaba2c9b79f4499dae1d66ef8bfa7b2b72"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/e6828efaba2c9b79f4499dae1d66ef8bfa7b2b72",
                "reference": "e6828efaba2c9b79f4499dae1d66ef8bfa7b2b72",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "replace": {
                "myclabs/deep-copy": "self.version"
            },
            "require-dev": {
                "doctrine/collections": "^1.0",
                "doctrine/common": "^2.6",
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DeepCopy\\": "src/DeepCopy/"
                },
                "files": [
                    "src/DeepCopy/deep_copy.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Create deep copies (clones) of your objects",
            "keywords": [
                "clone",
                "copy",
                "duplicate",
                "object",
                "object graph"
            ],
            "time": "2019-04-07T13:18:21+00:00"
        },
        {
            "name": "nesbot/carbon",
            "version": "2.19.2",
            "source": {
                "type": "git",
                "url": "https://github.com/briannesbitt/Carbon.git",
                "reference": "adcad3f3af52d0ad4ad7b05f43aa58243b6ca67b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/briannesbitt/Carbon/zipball/adcad3f3af52d0ad4ad7b05f43aa58243b6ca67b",
                "reference": "adcad3f3af52d0ad4ad7b05f43aa58243b6ca67b",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.1.8 || ^8.0",
                "symfony/translation": "^3.4 || ^4.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.14 || ^3.0",
                "kylekatarnls/multi-tester": "^1.1",
                "phpmd/phpmd": "^2.6",
                "phpstan/phpstan": "^0.11",
                "phpunit/phpunit": "^7.5 || ^8.0",
                "squizlabs/php_codesniffer": "^3.4"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "Carbon\\Laravel\\ServiceProvider"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Carbon\\": "src/Carbon/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Brian Nesbitt",
                    "email": "brian@nesbot.com",
                    "homepage": "http://nesbot.com"
                }
            ],
            "description": "A simple API extension for DateTime.",
            "homepage": "http://carbon.nesbot.com",
            "keywords": [
                "date",
                "datetime",
                "time"
            ],
            "time": "2019-06-07T09:56:45+00:00"
        },
        {
            "name": "nette/bootstrap",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/bootstrap.git",
                "reference": "6c736302535c5dc0fb736441786f216b3be5a1f0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/bootstrap/zipball/6c736302535c5dc0fb736441786f216b3be5a1f0",
                "reference": "6c736302535c5dc0fb736441786f216b3be5a1f0",
                "shasum": ""
            },
            "require": {
                "nette/di": "^3.0",
                "nette/utils": "^3.0",
                "php": ">=7.1"
            },
            "require-dev": {
                "latte/latte": "^2.2",
                "nette/application": "^3.0",
                "nette/caching": "^3.0",
                "nette/database": "^3.0",
                "nette/forms": "^3.0",
                "nette/http": "^3.0",
                "nette/mail": "^3.0",
                "nette/robot-loader": "^3.0",
                "nette/safe-stream": "^2.2",
                "nette/security": "^3.0",
                "nette/tester": "^2.0",
                "tracy/tracy": "^2.6"
            },
            "suggest": {
                "nette/robot-loader": "to use Configurator::createRobotLoader()",
                "tracy/tracy": "to use Configurator::enableTracy()"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🅱 Nette Bootstrap: the simple way to configure and bootstrap your Nette application.",
            "homepage": "https://nette.org",
            "keywords": [
                "bootstrapping",
                "configurator",
                "nette"
            ],
            "time": "2019-03-26T16:26:04+00:00"
        },
        {
            "name": "nette/di",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/di.git",
                "reference": "4927bc085e7a883e365e0cc472c1a56d693ce610"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/di/zipball/4927bc085e7a883e365e0cc472c1a56d693ce610",
                "reference": "4927bc085e7a883e365e0cc472c1a56d693ce610",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "nette/neon": "^3.0",
                "nette/php-generator": "^3.2.2",
                "nette/robot-loader": "^3.2",
                "nette/schema": "^1.0",
                "nette/utils": "^3.0",
                "php": ">=7.1"
            },
            "conflict": {
                "nette/bootstrap": "<3.0"
            },
            "require-dev": {
                "nette/tester": "^2.2",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ],
                "files": [
                    "src/compatibility.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "💎 Nette Dependency Injection Container: Flexible, compiled and full-featured DIC with perfectly usable autowiring and support for all new PHP 7.1 features.",
            "homepage": "https://nette.org",
            "keywords": [
                "compiled",
                "di",
                "dic",
                "factory",
                "ioc",
                "nette",
                "static"
            ],
            "time": "2019-05-29T17:09:14+00:00"
        },
        {
            "name": "nette/finder",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/finder.git",
                "reference": "13240336bd80f9260cd35a3894b8c1aab9586ec2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/finder/zipball/13240336bd80f9260cd35a3894b8c1aab9586ec2",
                "reference": "13240336bd80f9260cd35a3894b8c1aab9586ec2",
                "shasum": ""
            },
            "require": {
                "nette/utils": "^2.4 || ~3.0.0",
                "php": ">=7.1"
            },
            "conflict": {
                "nette/nette": "<2.2"
            },
            "require-dev": {
                "nette/tester": "^2.0",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🔍 Nette Finder: find files and directories with an intuitive API.",
            "homepage": "https://nette.org",
            "keywords": [
                "filesystem",
                "glob",
                "iterator",
                "nette"
            ],
            "time": "2019-03-22T00:58:33+00:00"
        },
        {
            "name": "nette/neon",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/neon.git",
                "reference": "fecb5758ca7076cadb5ebd7b47e47f11d7298030"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/neon/zipball/fecb5758ca7076cadb5ebd7b47e47f11d7298030",
                "reference": "fecb5758ca7076cadb5ebd7b47e47f11d7298030",
                "shasum": ""
            },
            "require": {
                "ext-iconv": "*",
                "ext-json": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "nette/tester": "^2.0",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🍸 Nette NEON: encodes and decodes NEON file format.",
            "homepage": "http://ne-on.org",
            "keywords": [
                "export",
                "import",
                "neon",
                "nette",
                "yaml"
            ],
            "time": "2019-03-26T13:02:18+00:00"
        },
        {
            "name": "nette/php-generator",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/php-generator.git",
                "reference": "3328cb69855463c446a887b832000676a7a30d6d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/php-generator/zipball/3328cb69855463c446a887b832000676a7a30d6d",
                "reference": "3328cb69855463c446a887b832000676a7a30d6d",
                "shasum": ""
            },
            "require": {
                "nette/utils": "^2.4.2 || ~3.0.0",
                "php": ">=7.1"
            },
            "require-dev": {
                "nette/tester": "^2.0",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🐘 Nette PHP Generator: generates neat PHP code for you. Supports new PHP 7.3 features.",
            "homepage": "https://nette.org",
            "keywords": [
                "code",
                "nette",
                "php",
                "scaffolding"
            ],
            "time": "2019-04-02T18:41:07+00:00"
        },
        {
            "name": "nette/robot-loader",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/robot-loader.git",
                "reference": "a49e8e83e4eb762d1c0f6b7c13059cf97f493aaf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/robot-loader/zipball/a49e8e83e4eb762d1c0f6b7c13059cf97f493aaf",
                "reference": "a49e8e83e4eb762d1c0f6b7c13059cf97f493aaf",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "nette/finder": "^2.5 || ^3.0",
                "nette/utils": "^3.0",
                "php": ">=7.1"
            },
            "require-dev": {
                "nette/tester": "^2.0",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🍀 Nette RobotLoader: high performance and comfortable autoloader that will search and autoload classes within your application.",
            "homepage": "https://nette.org",
            "keywords": [
                "autoload",
                "class",
                "interface",
                "nette",
                "trait"
            ],
            "time": "2019-03-31T19:12:28+00:00"
        },
        {
            "name": "nette/schema",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/schema.git",
                "reference": "6241d8d4da39e825dd6cb5bfbe4242912f4d7e4d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/schema/zipball/6241d8d4da39e825dd6cb5bfbe4242912f4d7e4d",
                "reference": "6241d8d4da39e825dd6cb5bfbe4242912f4d7e4d",
                "shasum": ""
            },
            "require": {
                "nette/utils": "^3.0.1",
                "php": ">=7.1"
            },
            "require-dev": {
                "nette/tester": "^2.2",
                "tracy/tracy": "^2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "📐 Nette Schema: validating data structures against a given Schema.",
            "homepage": "https://nette.org",
            "keywords": [
                "config",
                "nette"
            ],
            "time": "2019-04-03T15:53:25+00:00"
        },
        {
            "name": "nette/utils",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/utils.git",
                "reference": "9f9fadd7158cfff8784fdd802a0c6dfced2a8fd5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/utils/zipball/9f9fadd7158cfff8784fdd802a0c6dfced2a8fd5",
                "reference": "9f9fadd7158cfff8784fdd802a0c6dfced2a8fd5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "require-dev": {
                "nette/tester": "~2.0",
                "tracy/tracy": "^2.3"
            },
            "suggest": {
                "ext-gd": "to use Image",
                "ext-iconv": "to use Strings::webalize() and toAscii()",
                "ext-intl": "to use Strings::webalize(), toAscii(), normalize() and compare()",
                "ext-json": "to use Nette\\Utils\\Json",
                "ext-mbstring": "to use Strings::lower() etc...",
                "ext-xml": "to use Strings::length() etc. when mbstring is not available"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0",
                "GPL-3.0"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🛠 Nette Utils: lightweight utilities for string & array manipulation, image handling, safe JSON encoding/decoding, validation, slug or strong password generating etc.",
            "homepage": "https://nette.org",
            "keywords": [
                "array",
                "core",
                "datetime",
                "images",
                "json",
                "nette",
                "paginator",
                "password",
                "slugify",
                "string",
                "unicode",
                "utf-8",
                "utility",
                "validation"
            ],
            "time": "2019-04-25T18:36:16+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "3cf61fdd267a9c39167eaa715b121a3d787f3c3f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/3cf61fdd267a9c39167eaa715b121a3d787f3c3f",
                "reference": "3cf61fdd267a9c39167eaa715b121a3d787f3c3f",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpParser\\": "lib/PhpParser"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Nikita Popov"
                }
            ],
            "description": "A PHP parser written in PHP",
            "keywords": [
                "parser",
                "php"
            ],
            "time": "2019-06-23T13:11:05+00:00"
        },
        {
            "name": "ocramius/package-versions",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Ocramius/PackageVersions.git",
                "reference": "a4d4b60d0e60da2487bd21a2c6ac089f85570dbb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Ocramius/PackageVersions/zipball/a4d4b60d0e60da2487bd21a2c6ac089f85570dbb",
                "reference": "a4d4b60d0e60da2487bd21a2c6ac089f85570dbb",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.0.0",
                "php": "^7.1.0"
            },
            "require-dev": {
                "composer/composer": "^1.6.3",
                "doctrine/coding-standard": "^5.0.1",
                "ext-zip": "*",
                "infection/infection": "^0.7.1",
                "phpunit/phpunit": "^7.0.0"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "PackageVersions\\Installer",
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PackageVersions\\": "src/PackageVersions"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "Composer plugin that provides efficient querying for installed package versions (no runtime IO)",
            "time": "2019-02-21T12:16:21+00:00"
        },
        {
            "name": "opis/closure",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/opis/closure.git",
                "reference": "f846725591203098246276b2e7b9e8b7814c4965"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/opis/closure/zipball/f846725591203098246276b2e7b9e8b7814c4965",
                "reference": "f846725591203098246276b2e7b9e8b7814c4965",
                "shasum": ""
            },
            "require": {
                "php": "^5.4 || ^7.0"
            },
            "require-dev": {
                "jeremeamia/superclosure": "^2.0",
                "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Opis\\Closure\\": "src/"
                },
                "files": [
                    "functions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marius Sarca",
                    "email": "marius.sarca@gmail.com"
                },
                {
                    "name": "Sorin Sarca",
                    "email": "sarca_sorin@hotmail.com"
                }
            ],
            "description": "A library that can be used to serialize closures (anonymous functions) and arbitrary objects.",
            "homepage": "https://opis.io/closure",
            "keywords": [
                "anonymous functions",
                "closure",
                "function",
                "serializable",
                "serialization",
                "serialize"
            ],
            "time": "2019-05-31T20:04:32+00:00"
        },
        {
            "name": "orchestra/testbench",
            "version": "3.8.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/orchestral/testbench.git",
                "reference": "df4de9cebb1cdde49513277fdca907fbd120e7a4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/orchestral/testbench/zipball/df4de9cebb1cdde49513277fdca907fbd120e7a4",
                "reference": "df4de9cebb1cdde49513277fdca907fbd120e7a4",
                "shasum": ""
            },
            "require": {
                "laravel/framework": "~5.8.19",
                "mockery/mockery": "^1.0",
                "orchestra/testbench-core": "~3.8.4",
                "php": ">=7.1",
                "phpunit/phpunit": "^7.5 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.8-dev"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mior Muhammad Zaki",
                    "email": "crynobone@gmail.com",
                    "homepage": "https://github.com/crynobone"
                }
            ],
            "description": "Laravel Testing Helper for Packages Development",
            "homepage": "http://orchestraplatform.com/docs/latest/components/testbench/",
            "keywords": [
                "BDD",
                "TDD",
                "laravel",
                "orchestra-platform",
                "orchestral",
                "testing"
            ],
            "time": "2019-06-12T19:47:32+00:00"
        },
        {
            "name": "orchestra/testbench-core",
            "version": "3.8.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/orchestral/testbench-core.git",
                "reference": "b81c24ef1036cb1f8ff0ca711535cea3f0281848"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/orchestral/testbench-core/zipball/b81c24ef1036cb1f8ff0ca711535cea3f0281848",
                "reference": "b81c24ef1036cb1f8ff0ca711535cea3f0281848",
                "shasum": ""
            },
            "require": {
                "fzaninotto/faker": "^1.4",
                "php": ">=7.1"
            },
            "require-dev": {
                "laravel/framework": "~5.8.3",
                "laravel/laravel": "dev-master",
                "mockery/mockery": "^1.0",
                "phpunit/phpunit": "^7.5 || ^8.0"
            },
            "suggest": {
                "laravel/framework": "Required for testing (~5.8.19).",
                "mockery/mockery": "Allow to use Mockery for testing (^1.0).",
                "orchestra/testbench-browser-kit": "Allow to use legacy Laravel BrowserKit for testing (^3.8).",
                "orchestra/testbench-dusk": "Allow to use Laravel Dusk for testing (^3.8).",
                "phpunit/phpunit": "Allow to use PHPUnit for testing (^7.5 || ^8.0)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.8-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Orchestra\\Testbench\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mior Muhammad Zaki",
                    "email": "crynobone@gmail.com",
                    "homepage": "https://github.com/crynobone"
                }
            ],
            "description": "Testing Helper for Laravel Development",
            "homepage": "http://orchestraplatform.com/docs/latest/components/testbench/",
            "keywords": [
                "BDD",
                "TDD",
                "laravel",
                "orchestra-platform",
                "orchestral",
                "testing"
            ],
            "time": "2019-06-10T08:29:56+00:00"
        },
        {
            "name": "paragonie/random_compat",
            "version": "v2.0.18",
            "source": {
                "type": "git",
                "url": "https://github.com/paragonie/random_compat.git",
                "reference": "0a58ef6e3146256cc3dc7cc393927bcc7d1b72db"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/paragonie/random_compat/zipball/0a58ef6e3146256cc3dc7cc393927bcc7d1b72db",
                "reference": "0a58ef6e3146256cc3dc7cc393927bcc7d1b72db",
                "shasum": ""
            },
            "require": {
                "php": ">=5.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*|5.*"
            },
            "suggest": {
                "ext-libsodium": "Provides a modern crypto API that can be used to generate random bytes."
            },
            "type": "library",
            "autoload": {
                "files": [
                    "lib/random.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paragon Initiative Enterprises",
                    "email": "security@paragonie.com",
                    "homepage": "https://paragonie.com"
                }
            ],
            "description": "PHP 5.x polyfill for random_bytes() and random_int() from PHP 7",
            "keywords": [
                "csprng",
                "polyfill",
                "pseudorandom",
                "random"
            ],
            "time": "2019-01-03T20:59:08+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "reference": "7761fcacf03b4d4f16e7ccb606d4879ca431fcf4",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "phar-io/version": "^2.0",
                "php": "^5.6 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Component for reading phar.io manifest information from a PHP Archive (PHAR)",
            "time": "2018-07-08T19:23:20+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "reference": "45a2ec53a73c70ce41d55cedef9063630abaf1b6",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Library for handling version information and constraints",
            "time": "2018-07-08T19:19:57+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "144c307535e82c8fdcaacbcfc1d6d8eeb896687c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/144c307535e82c8fdcaacbcfc1d6d8eeb896687c",
                "reference": "144c307535e82c8fdcaacbcfc1d6d8eeb896687c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jaap van Otterdijk",
                    "email": "opensource@ijaap.nl"
                }
            ],
            "description": "Common reflection classes used by phpdocumentor to reflect the code structure",
            "homepage": "http://www.phpdoc.org",
            "keywords": [
                "FQSEN",
                "phpDocumentor",
                "phpdoc",
                "reflection",
                "static analysis"
            ],
            "time": "2015-12-27T11:43:31+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "4.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "bdd9f737ebc2a01c06ea7ff4308ec6697db9b53c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/bdd9f737ebc2a01c06ea7ff4308ec6697db9b53c",
                "reference": "bdd9f737ebc2a01c06ea7ff4308ec6697db9b53c",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "phpdocumentor/reflection-common": "^1.0.0",
                "phpdocumentor/type-resolver": "^0.4.0",
                "webmozart/assert": "^1.0"
            },
            "require-dev": {
                "doctrine/instantiator": "~1.0.5",
                "mockery/mockery": "^1.0",
                "phpunit/phpunit": "^6.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "time": "2019-04-30T17:48:53+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "0.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/9c977708995954784726e25d0cd1dddf4e65b0f7",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7",
                "shasum": ""
            },
            "require": {
                "php": "^5.5 || ^7.0",
                "phpdocumentor/reflection-common": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^0.9.4",
                "phpunit/phpunit": "^5.2||^4.8.24"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                }
            ],
            "time": "2017-07-14T14:27:02+00:00"
        },
        {
            "name": "phpoption/phpoption",
            "version": "1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/php-option.git",
                "reference": "94e644f7d2051a5f0fcf77d81605f152eecff0ed"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/php-option/zipball/94e644f7d2051a5f0fcf77d81605f152eecff0ed",
                "reference": "94e644f7d2051a5f0fcf77d81605f152eecff0ed",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "4.7.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "PhpOption\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache2"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Option Type for PHP",
            "keywords": [
                "language",
                "option",
                "php",
                "type"
            ],
            "time": "2015-07-25T16:39:46+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "1927e75f4ed19131ec9bcc3b002e07fb1173ee76"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/1927e75f4ed19131ec9bcc3b002e07fb1173ee76",
                "reference": "1927e75f4ed19131ec9bcc3b002e07fb1173ee76",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^5.3|^7.0",
                "phpdocumentor/reflection-docblock": "^2.0|^3.0.2|^4.0",
                "sebastian/comparator": "^1.1|^2.0|^3.0",
                "sebastian/recursion-context": "^1.0|^2.0|^3.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^2.5|^3.2",
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.5 || ^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.8.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Prophecy\\": "src/Prophecy"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                },
                {
                    "name": "Marcello Duarte",
                    "email": "marcello.duarte@gmail.com"
                }
            ],
            "description": "Highly opinionated mocking framework for PHP 5.3+",
            "homepage": "https://github.com/phpspec/prophecy",
            "keywords": [
                "Double",
                "Dummy",
                "fake",
                "mock",
                "spy",
                "stub"
            ],
            "time": "2019-06-13T12:50:23+00:00"
        },
        {
            "name": "phpstan/phpdoc-parser",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpdoc-parser.git",
                "reference": "8c4ef2aefd9788238897b678a985e1d5c8df6db4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpdoc-parser/zipball/8c4ef2aefd9788238897b678a985e1d5c8df6db4",
                "reference": "8c4ef2aefd9788238897b678a985e1d5c8df6db4",
                "shasum": ""
            },
            "require": {
                "php": "~7.1"
            },
            "require-dev": {
                "consistence/coding-standard": "^3.5",
                "jakub-onderka/php-parallel-lint": "^0.9.2",
                "phing/phing": "^2.16.0",
                "phpstan/phpstan": "^0.10",
                "phpunit/phpunit": "^6.3",
                "slevomat/coding-standard": "^4.7.2",
                "squizlabs/php_codesniffer": "^3.3.2",
                "symfony/process": "^3.4 || ^4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\PhpDocParser\\": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPDoc parser with support for nullable, intersection and generic types",
            "time": "2019-06-07T19:13:52+00:00"
        },
        {
            "name": "phpstan/phpstan",
            "version": "0.11.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan.git",
                "reference": "25101c464ca0f8b9e3a552fd24dbc01a201787f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan/zipball/25101c464ca0f8b9e3a552fd24dbc01a201787f8",
                "reference": "25101c464ca0f8b9e3a552fd24dbc01a201787f8",
                "shasum": ""
            },
            "require": {
                "composer/xdebug-handler": "^1.3.0",
                "jean85/pretty-package-versions": "^1.0.3",
                "nette/bootstrap": "^2.4 || ^3.0",
                "nette/di": "^2.4.7 || ^3.0",
                "nette/robot-loader": "^3.0.1",
                "nette/schema": "^1.0",
                "nette/utils": "^2.4.5 || ^3.0",
                "nikic/php-parser": "^4.0.2",
                "php": "~7.1",
                "phpstan/phpdoc-parser": "^0.3.5",
                "symfony/console": "~3.2 || ~4.0",
                "symfony/finder": "~3.2 || ~4.0"
            },
            "conflict": {
                "symfony/console": "3.4.16 || 4.1.5"
            },
            "require-dev": {
                "brianium/paratest": "^2.0",
                "consistence/coding-standard": "^3.5",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.4.4",
                "ext-intl": "*",
                "ext-mysqli": "*",
                "ext-simplexml": "*",
                "ext-soap": "*",
                "ext-zip": "*",
                "jakub-onderka/php-parallel-lint": "^1.0",
                "localheinz/composer-normalize": "^1.1.0",
                "phing/phing": "^2.16.0",
                "phpstan/phpstan-deprecation-rules": "^0.11",
                "phpstan/phpstan-php-parser": "^0.11",
                "phpstan/phpstan-phpunit": "^0.11",
                "phpstan/phpstan-strict-rules": "^0.11",
                "phpunit/phpunit": "^7.0",
                "slevomat/coding-standard": "^4.7.2",
                "squizlabs/php_codesniffer": "^3.3.2"
            },
            "bin": [
                "bin/phpstan"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": [
                        "src/",
                        "build/PHPStan"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan - PHP Static Analysis Tool",
            "time": "2019-06-23T11:05:53+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "6.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "807e6013b00af69b6c5d9ceb4282d0393dbb9d8d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/807e6013b00af69b6c5d9ceb4282d0393dbb9d8d",
                "reference": "807e6013b00af69b6c5d9ceb4282d0393dbb9d8d",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-xmlwriter": "*",
                "php": "^7.1",
                "phpunit/php-file-iterator": "^2.0",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-token-stream": "^3.0",
                "sebastian/code-unit-reverse-lookup": "^1.0.1",
                "sebastian/environment": "^3.1 || ^4.0",
                "sebastian/version": "^2.0.1",
                "theseer/tokenizer": "^1.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "suggest": {
                "ext-xdebug": "^2.6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that provides collection, processing, and rendering functionality for PHP code coverage information.",
            "homepage": "https://github.com/sebastianbergmann/php-code-coverage",
            "keywords": [
                "coverage",
                "testing",
                "xunit"
            ],
            "time": "2018-10-31T16:06:48+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "80ca798a9fb7b60c6a2169d8c6cad9f00eb3a06a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/80ca798a9fb7b60c6a2169d8c6cad9f00eb3a06a",
                "reference": "80ca798a9fb7b60c6a2169d8c6cad9f00eb3a06a",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "time": "2019-05-24T06:36:01+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "time": "2015-06-21T13:50:34+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "29995fbf33aabda1b53b65ada13737d42ccaf53a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/29995fbf33aabda1b53b65ada13737d42ccaf53a",
                "reference": "29995fbf33aabda1b53b65ada13737d42ccaf53a",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "time": "2019-06-10T14:27:16+00:00"
        },
        {
            "name": "phpunit/php-token-stream",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "2d574d6767341959316726121431ecb9c4a61037"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/2d574d6767341959316726121431ecb9c4a61037",
                "reference": "2d574d6767341959316726121431ecb9c4a61037",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Wrapper around PHP's tokenizer extension.",
            "homepage": "https://github.com/sebastianbergmann/php-token-stream/",
            "keywords": [
                "tokenizer"
            ],
            "time": "2019-05-24T06:39:22+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "7.5.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "1477fe424dc8ba0b252b1262f91f40139e0f889b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/1477fe424dc8ba0b252b1262f91f40139e0f889b",
                "reference": "1477fe424dc8ba0b252b1262f91f40139e0f889b",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.1",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "myclabs/deep-copy": "^1.7",
                "phar-io/manifest": "^1.0.2",
                "phar-io/version": "^2.0",
                "php": "^7.1",
                "phpspec/prophecy": "^1.7",
                "phpunit/php-code-coverage": "^6.0.7",
                "phpunit/php-file-iterator": "^2.0.1",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-timer": "^2.1",
                "sebastian/comparator": "^3.0",
                "sebastian/diff": "^3.0",
                "sebastian/environment": "^4.0",
                "sebastian/exporter": "^3.1",
                "sebastian/global-state": "^2.0",
                "sebastian/object-enumerator": "^3.0.3",
                "sebastian/resource-operations": "^2.0",
                "sebastian/version": "^2.0.1"
            },
            "conflict": {
                "phpunit/phpunit-mock-objects": "*"
            },
            "require-dev": {
                "ext-pdo": "*"
            },
            "suggest": {
                "ext-soap": "*",
                "ext-xdebug": "*",
                "phpunit/php-invoker": "^2.0"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "7.5-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "The PHP Unit Testing framework.",
            "homepage": "https://phpunit.de/",
            "keywords": [
                "phpunit",
                "testing",
                "xunit"
            ],
            "time": "2019-06-20T14:04:28+00:00"
        },
        {
            "name": "psr/container",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "014d250daebff39eba15ba990eeb2a140798e77c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/014d250daebff39eba15ba990eeb2a140798e77c",
                "reference": "014d250daebff39eba15ba990eeb2a140798e77c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "time": "2018-12-29T15:36:03+00:00"
        },
        {
            "name": "psr/log",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "c4421fcac1edd5a324fda73e589a5cf96e52ffd0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/c4421fcac1edd5a324fda73e589a5cf96e52ffd0",
                "reference": "c4421fcac1edd5a324fda73e589a5cf96e52ffd0",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "Psr/Log/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "time": "2018-11-21T13:42:00+00:00"
        },
        {
            "name": "psr/simple-cache",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/simple-cache.git",
                "reference": "408d5eafb83c57f6365a3ca330ff23aa4a5fa39b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/simple-cache/zipball/408d5eafb83c57f6365a3ca330ff23aa4a5fa39b",
                "reference": "408d5eafb83c57f6365a3ca330ff23aa4a5fa39b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\SimpleCache\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interfaces for simple caching",
            "keywords": [
                "cache",
                "caching",
                "psr",
                "psr-16",
                "simple-cache"
            ],
            "time": "2017-10-23T01:57:42+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "446df35e870de74381348d433e62822dc2840a5c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/446df35e870de74381348d433e62822dc2840a5c",
                "reference": "446df35e870de74381348d433e62822dc2840a5c",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.2",
                "symfony/polyfill-ctype": "^1.8"
            },
            "require-dev": {
                "apigen/apigen": "^4.1",
                "codeception/aspect-mock": "^1.0 | ^2.0",
                "doctrine/annotations": "~1.2.0",
                "goaop/framework": "1.0.0-alpha.2 | ^1.0 | ^2.1",
                "ircmaxell/random-lib": "^1.1",
                "jakub-onderka/php-parallel-lint": "^0.9.0",
                "mockery/mockery": "^0.9.4",
                "moontoast/math": "^1.1",
                "php-mock/php-mock-phpunit": "^0.3|^1.1",
                "phpunit/phpunit": "^4.7|>=5.0 <5.4",
                "satooshi/php-coveralls": "^0.6.1",
                "squizlabs/php_codesniffer": "^2.3"
            },
            "suggest": {
                "ext-libsodium": "Provides the PECL libsodium extension for use with the SodiumRandomGenerator",
                "ext-uuid": "Provides the PECL UUID extension for use with the PeclUuidTimeGenerator and PeclUuidRandomGenerator",
                "ircmaxell/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "moontoast/math": "Provides support for converting UUID to 128-bit integer (in string form).",
                "ramsey/uuid-console": "A console application for generating UUIDs with ramsey/uuid",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marijn Huizendveld",
                    "email": "marijn.huizendveld@gmail.com"
                },
                {
                    "name": "Thibaud Fabre",
                    "email": "thibaud@aztech.io"
                },
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "Formerly rhumsaa/uuid. A PHP 5.4+ library for generating RFC 4122 version 1, 3, 4, and 5 universally unique identifiers (UUID).",
            "homepage": "https://github.com/ramsey/uuid",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "time": "2017-03-26T21:03:42+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "aa169192fe98c7270af0ec5c57e631094ad930df"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/aa169192fe98c7270af0ec5c57e631094ad930df",
                "reference": "aa169192fe98c7270af0ec5c57e631094ad930df",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.7 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "time": "2019-05-24T06:36:34+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "6ddb43a0106887320958344fc6e55aa033154b9d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/6ddb43a0106887320958344fc6e55aa033154b9d",
                "reference": "6ddb43a0106887320958344fc6e55aa033154b9d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1",
                "sebastian/diff": "^3.0",
                "sebastian/exporter": "^3.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "time": "2019-05-24T06:32:56+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "1d90f91424a056ebd763d7046ee5957d160c1c24"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/1d90f91424a056ebd763d7046ee5957d160c1c24",
                "reference": "1d90f91424a056ebd763d7046ee5957d160c1c24",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.5 || ^8.0",
                "symfony/process": "^2 || ^3.3 || ^4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Diff implementation",
            "homepage": "https://github.com/sebastianbergmann/diff",
            "keywords": [
                "diff",
                "udiff",
                "unidiff",
                "unified diff"
            ],
            "time": "2019-05-24T06:38:22+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "48c9235dc43ce325b15d950f53996da748f2d571"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/48c9235dc43ce325b15d950f53996da748f2d571",
                "reference": "48c9235dc43ce325b15d950f53996da748f2d571",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.5"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides functionality to handle HHVM/PHP environments",
            "homepage": "http://www.github.com/sebastianbergmann/environment",
            "keywords": [
                "Xdebug",
                "environment",
                "hhvm"
            ],
            "time": "2019-05-24T06:34:26+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "cf3a70cdc3af7b80ad571adae1ab718eb578be2b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/cf3a70cdc3af7b80ad571adae1ab718eb578be2b",
                "reference": "cf3a70cdc3af7b80ad571adae1ab718eb578be2b",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "time": "2019-05-24T06:35:43+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Snapshotting of global state",
            "homepage": "http://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "time": "2017-04-27T15:39:26+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "eb45b4b8fd5f845d36851767a6fe00ee15cb8952"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/eb45b4b8fd5f845d36851767a6fe00ee15cb8952",
                "reference": "eb45b4b8fd5f845d36851767a6fe00ee15cb8952",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/object-reflector": "^1.1.1",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Traverses array structures and object graphs to enumerate all referenced objects",
            "homepage": "https://github.com/sebastianbergmann/object-enumerator/",
            "time": "2019-05-24T06:37:20+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "a2539861984780016bb3d75420452d95f798e25d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/a2539861984780016bb3d75420452d95f798e25d",
                "reference": "a2539861984780016bb3d75420452d95f798e25d",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "time": "2019-05-24T06:35:22+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "b6a7e76741fee33ec10ccb55772e65d817a8f2fd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/b6a7e76741fee33ec10ccb55772e65d817a8f2fd",
                "reference": "b6a7e76741fee33ec10ccb55772e65d817a8f2fd",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "time": "2019-05-24T06:37:03+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "366bbb128ea2fd570ab9986e6d79a7167fd5c041"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/366bbb128ea2fd570ab9986e6d79a7167fd5c041",
                "reference": "366bbb128ea2fd570ab9986e6d79a7167fd5c041",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "time": "2019-05-24T06:40:48+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/99732be0ddb3361e16ad77b68ba41efc8e979019",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019",
                "shasum": ""
            },
            "require": {
                "php": "^7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "time": "2016-10-03T07:35:21+00:00"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "b22e508d2db967630445c553572d1e9eb997ecef"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/b22e508d2db967630445c553572d1e9eb997ecef",
                "reference": "b22e508d2db967630445c553572d1e9eb997ecef",
                "shasum": ""
            },
            "require": {
                "egulias/email-validator": "~2.0",
                "php": ">=7.0.0",
                "symfony/polyfill-iconv": "^1.0",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "~0.9.1",
                "symfony/phpunit-bridge": "^3.4.19|^4.1.8"
            },
            "suggest": {
                "ext-intl": "Needed to support internationalized email addresses",
                "true/punycode": "Needed to support internationalized email addresses, if ext-intl is not installed"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.2-dev"
                }
            },
            "autoload": {
                "files": [
                    "lib/swift_required.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Chris Corbyn"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Swiftmailer, free feature-rich PHP mailer",
            "homepage": "https://swiftmailer.symfony.com",
            "keywords": [
                "email",
                "mail",
                "mailer"
            ],
            "time": "2019-04-21T09:22:17+00:00"
        },
        {
            "name": "symfony/console",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "a2e6f67b286cf6735437b6e88f38cfee72405d36"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/a2e6f67b286cf6735437b6e88f38cfee72405d36",
                "reference": "a2e6f67b286cf6735437b6e88f38cfee72405d36",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/service-contracts": "^1.1"
            },
            "conflict": {
                "symfony/dependency-injection": "<3.4",
                "symfony/event-dispatcher": "<4.3|>=5",
                "symfony/process": "<3.3"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^3.4|^4.0|^5.0",
                "symfony/dependency-injection": "^3.4|^4.0|^5.0",
                "symfony/event-dispatcher": "^4.3",
                "symfony/lock": "^3.4|^4.0|^5.0",
                "symfony/process": "^3.4|^4.0|^5.0",
                "symfony/var-dumper": "^4.3|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Console Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-13T11:05:05+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "9ed158c52af88c6befa7dd00c8e6dfc273a52ab4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/9ed158c52af88c6befa7dd00c8e6dfc273a52ab4",
                "reference": "9ed158c52af88c6befa7dd00c8e6dfc273a52ab4",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\CssSelector\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony CssSelector Component",
            "homepage": "https://symfony.com",
            "time": "2019-05-09T07:23:25+00:00"
        },
        {
            "name": "symfony/debug",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/debug.git",
                "reference": "cbb87998772fcd65a037287a7a6a7f709c601666"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/debug/zipball/cbb87998772fcd65a037287a7a6a7f709c601666",
                "reference": "cbb87998772fcd65a037287a7a6a7f709c601666",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "psr/log": "~1.0"
            },
            "conflict": {
                "symfony/http-kernel": "<3.4"
            },
            "require-dev": {
                "symfony/http-kernel": "^3.4|^4.0|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Debug\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Debug Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-19T15:27:23+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "3f1bdf9140159fb5442b79072230a4d5f1306532"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/3f1bdf9140159fb5442b79072230a4d5f1306532",
                "reference": "3f1bdf9140159fb5442b79072230a4d5f1306532",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/event-dispatcher-contracts": "^1.1"
            },
            "conflict": {
                "symfony/dependency-injection": "<3.4"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "1.1"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^3.4|^4.0|^5.0",
                "symfony/dependency-injection": "^3.4|^4.0|^5.0",
                "symfony/expression-language": "^3.4|^4.0|^5.0",
                "symfony/http-foundation": "^3.4|^4.0|^5.0",
                "symfony/service-contracts": "^1.1",
                "symfony/stopwatch": "^3.4|^4.0|^5.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\EventDispatcher\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony EventDispatcher Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-13T11:05:05+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "c61766f4440ca687de1084a5c00b08e167a2575c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/c61766f4440ca687de1084a5c00b08e167a2575c",
                "reference": "c61766f4440ca687de1084a5c00b08e167a2575c",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "suggest": {
                "psr/event-dispatcher": "",
                "symfony/event-dispatcher-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "time": "2019-06-20T06:46:26+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "197be09fba72fbdb52e54ad1ead0372d11ee6533"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/197be09fba72fbdb52e54ad1ead0372d11ee6533",
                "reference": "197be09fba72fbdb52e54ad1ead0372d11ee6533",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Finder\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Finder Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-13T11:05:05+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "1bdcbf5a5d5294f45ab8cca491e3553d52796d35"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/1bdcbf5a5d5294f45ab8cca491e3553d52796d35",
                "reference": "1bdcbf5a5d5294f45ab8cca491e3553d52796d35",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/mime": "^4.3|^5.0",
                "symfony/polyfill-mbstring": "~1.1"
            },
            "require-dev": {
                "predis/predis": "~1.0",
                "symfony/expression-language": "^3.4|^4.0|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpFoundation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpFoundation Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-21T10:14:40+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "89275284a2c3c80922ede66f208a5429ee691f9b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/89275284a2c3c80922ede66f208a5429ee691f9b",
                "reference": "89275284a2c3c80922ede66f208a5429ee691f9b",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "psr/log": "~1.0",
                "symfony/debug": "^3.4|^4.0|^5.0",
                "symfony/event-dispatcher": "^4.3",
                "symfony/http-foundation": "^4.4|^5.0",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-php73": "^1.9"
            },
            "conflict": {
                "symfony/browser-kit": "<4.3",
                "symfony/config": "<3.4",
                "symfony/console": ">=5",
                "symfony/dependency-injection": "<4.3",
                "symfony/translation": "<4.2",
                "symfony/var-dumper": "<4.1.1",
                "twig/twig": "<1.34|<2.4,>=2"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/cache": "~1.0",
                "symfony/browser-kit": "^4.3|^5.0",
                "symfony/config": "^3.4|^4.0|^5.0",
                "symfony/console": "^3.4|^4.0",
                "symfony/css-selector": "^3.4|^4.0|^5.0",
                "symfony/dependency-injection": "^4.3|^5.0",
                "symfony/dom-crawler": "^3.4|^4.0|^5.0",
                "symfony/expression-language": "^3.4|^4.0|^5.0",
                "symfony/finder": "^3.4|^4.0|^5.0",
                "symfony/process": "^3.4|^4.0|^5.0",
                "symfony/routing": "^3.4|^4.0|^5.0",
                "symfony/stopwatch": "^3.4|^4.0|^5.0",
                "symfony/templating": "^3.4|^4.0|^5.0",
                "symfony/translation": "^4.2|^5.0",
                "symfony/translation-contracts": "^1.1",
                "symfony/var-dumper": "^4.1.1|^5.0",
                "twig/twig": "^1.34|^2.4"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": "",
                "symfony/var-dumper": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpKernel\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpKernel Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-17T17:38:10+00:00"
        },
        {
            "name": "symfony/mime",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/mime.git",
                "reference": "82c943c191b25ff79f2ec9ade40ed1eff7f5b35d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/mime/zipball/82c943c191b25ff79f2ec9ade40ed1eff7f5b35d",
                "reference": "82c943c191b25ff79f2ec9ade40ed1eff7f5b35d",
                "shasum": ""
            },
            "require": {
                "php": "^7.2.9",
                "symfony/polyfill-intl-idn": "^1.10",
                "symfony/polyfill-mbstring": "^1.0"
            },
            "require-dev": {
                "egulias/email-validator": "^2.0",
                "symfony/dependency-injection": "^4.4|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Mime\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A library to manipulate MIME messages",
            "homepage": "https://symfony.com",
            "keywords": [
                "mime",
                "mime-type"
            ],
            "time": "2019-06-22T22:57:33+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "82ebae02209c21113908c229e9883c419720738a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/82ebae02209c21113908c229e9883c419720738a",
                "reference": "82ebae02209c21113908c229e9883c419720738a",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Ctype\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                },
                {
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                }
            ],
            "description": "Symfony polyfill for ctype functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "ctype",
                "polyfill",
                "portable"
            ],
            "time": "2019-02-06T07:57:58+00:00"
        },
        {
            "name": "symfony/polyfill-iconv",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-iconv.git",
                "reference": "f037ea22acfaee983e271dd9c3b8bb4150bd8ad7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-iconv/zipball/f037ea22acfaee983e271dd9c3b8bb4150bd8ad7",
                "reference": "f037ea22acfaee983e271dd9c3b8bb4150bd8ad7",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-iconv": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Iconv\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Iconv extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "iconv",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2019-02-06T07:57:58+00:00"
        },
        {
            "name": "symfony/polyfill-intl-idn",
            "version": "v1.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-idn.git",
                "reference": "c766e95bec706cdd89903b1eda8afab7d7a6b7af"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-idn/zipball/c766e95bec706cdd89903b1eda8afab7d7a6b7af",
                "reference": "c766e95bec706cdd89903b1eda8afab7d7a6b7af",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/polyfill-mbstring": "^1.3",
                "symfony/polyfill-php72": "^1.9"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Idn\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                },
                {
                    "name": "Laurent Bassin",
                    "email": "laurent@bassin.info"
                }
            ],
            "description": "Symfony polyfill for intl's idn_to_ascii and idn_to_utf8 functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "idn",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2019-03-04T13:44:35+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "fe5e94c604826c35a32fa832f35bd036b6799609"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/fe5e94c604826c35a32fa832f35bd036b6799609",
                "reference": "fe5e94c604826c35a32fa832f35bd036b6799609",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2019-02-06T07:57:58+00:00"
        },
        {
            "name": "symfony/polyfill-php72",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php72.git",
                "reference": "ab50dcf166d5f577978419edd37aa2bb8eabce0c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php72/zipball/ab50dcf166d5f577978419edd37aa2bb8eabce0c",
                "reference": "ab50dcf166d5f577978419edd37aa2bb8eabce0c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php72\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.2+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2019-02-06T07:57:58+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "d1fb4abcc0c47be136208ad9d68bf59f1ee17abd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/d1fb4abcc0c47be136208ad9d68bf59f1ee17abd",
                "reference": "d1fb4abcc0c47be136208ad9d68bf59f1ee17abd",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.11-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2019-02-06T07:57:58+00:00"
        },
        {
            "name": "symfony/process",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/process.git",
                "reference": "1a42849a7fadb0130d2854f96db8d234da150403"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/process/zipball/1a42849a7fadb0130d2854f96db8d234da150403",
                "reference": "1a42849a7fadb0130d2854f96db8d234da150403",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Process\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Process Component",
            "homepage": "https://symfony.com",
            "time": "2019-05-30T16:10:19+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "23b861256bd6c5328cd586c6dd37666ce3e81e6e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/23b861256bd6c5328cd586c6dd37666ce3e81e6e",
                "reference": "23b861256bd6c5328cd586c6dd37666ce3e81e6e",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "conflict": {
                "symfony/config": "<4.2",
                "symfony/dependency-injection": "<3.4",
                "symfony/yaml": "<3.4"
            },
            "require-dev": {
                "doctrine/annotations": "~1.2",
                "psr/log": "~1.0",
                "symfony/config": "^4.2|^5.0",
                "symfony/dependency-injection": "^3.4|^4.0|^5.0",
                "symfony/expression-language": "^3.4|^4.0|^5.0",
                "symfony/http-foundation": "^3.4|^4.0|^5.0",
                "symfony/yaml": "^3.4|^4.0|^5.0"
            },
            "suggest": {
                "doctrine/annotations": "For using the annotation loader",
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Routing\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Routing Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "time": "2019-06-17T17:38:10+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "f391a00de78ec7ec8cf5cdcdae59ec7b883edb8d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/f391a00de78ec7ec8cf5cdcdae59ec7b883edb8d",
                "reference": "f391a00de78ec7ec8cf5cdcdae59ec7b883edb8d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "psr/container": "^1.0"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "time": "2019-06-13T11:15:36+00:00"
        },
        {
            "name": "symfony/translation",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "43dc8460dc5ba5543927309177075e43db51778d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/43dc8460dc5ba5543927309177075e43db51778d",
                "reference": "43dc8460dc5ba5543927309177075e43db51778d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/translation-contracts": "^1.1.2"
            },
            "conflict": {
                "symfony/config": "<3.4",
                "symfony/dependency-injection": "<3.4",
                "symfony/yaml": "<3.4"
            },
            "provide": {
                "symfony/translation-implementation": "1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^3.4|^4.0|^5.0",
                "symfony/console": "^3.4|^4.0|^5.0",
                "symfony/dependency-injection": "^3.4|^4.0|^5.0",
                "symfony/finder": "~2.8|~3.0|~4.0|^5.0",
                "symfony/http-kernel": "^3.4|^4.0|^5.0",
                "symfony/intl": "^3.4|^4.0|^5.0",
                "symfony/service-contracts": "^1.1.2",
                "symfony/var-dumper": "^3.4|^4.0|^5.0",
                "symfony/yaml": "^3.4|^4.0|^5.0"
            },
            "suggest": {
                "psr/log-implementation": "To use logging capability in translator",
                "symfony/config": "",
                "symfony/yaml": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Translation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Translation Component",
            "homepage": "https://symfony.com",
            "time": "2019-06-13T11:05:05+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "cb4b18ad7b92a26e83b65dde940fab78339e6f3c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/cb4b18ad7b92a26e83b65dde940fab78339e6f3c",
                "reference": "cb4b18ad7b92a26e83b65dde940fab78339e6f3c",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3"
            },
            "suggest": {
                "symfony/translation-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Translation\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to translation",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "time": "2019-06-13T11:15:36+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "4.4.x-dev",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "51e0fda695013eb8decc1576390527f6decc408d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/51e0fda695013eb8decc1576390527f6decc408d",
                "reference": "51e0fda695013eb8decc1576390527f6decc408d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1.3",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php72": "~1.5"
            },
            "conflict": {
                "phpunit/phpunit": "<4.8.35|<5.4.3,>=5.0",
                "symfony/console": "<3.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^3.4|^4.0|^5.0",
                "symfony/process": "^3.4|^4.0|^5.0",
                "twig/twig": "~1.34|~2.4"
            },
            "suggest": {
                "ext-iconv": "To convert non-UTF-8 strings to UTF-8 (or symfony/polyfill-iconv in case ext-iconv cannot be used).",
                "ext-intl": "To show region name in time zone dump",
                "symfony/console": "To use the ServerDumpCommand and/or the bin/var-dump-server script"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
                }
            },
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony mechanism for exploring and dumping PHP variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "time": "2019-06-17T17:38:10+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "11336f6f84e16a720dae9d8e6ed5019efa85a0f9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/11336f6f84e16a720dae9d8e6ed5019efa85a0f9",
                "reference": "11336f6f84e16a720dae9d8e6ed5019efa85a0f9",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                }
            ],
            "description": "A small library for converting tokenized PHP source code into XML and potentially other formats",
            "time": "2019-06-13T22:48:21+00:00"
        },
        {
            "name": "tijsverkoyen/css-to-inline-styles",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/tijsverkoyen/CssToInlineStyles.git",
                "reference": "0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/tijsverkoyen/CssToInlineStyles/zipball/0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757",
                "reference": "0ed4a2ea4e0902dac0489e6436ebcd5bbcae9757",
                "shasum": ""
            },
            "require": {
                "php": "^5.5 || ^7.0",
                "symfony/css-selector": "^2.7 || ^3.0 || ^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "TijsVerkoyen\\CssToInlineStyles\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Tijs Verkoyen",
                    "email": "css_to_inline_styles@verkoyen.eu",
                    "role": "Developer"
                }
            ],
            "description": "CssToInlineStyles is a class that enables you to convert HTML-pages/files into HTML-pages/files with inline styles. This is very useful when you're sending emails.",
            "homepage": "https://github.com/tijsverkoyen/CssToInlineStyles",
            "time": "2017-11-27T11:13:29+00:00"
        },
        {
            "name": "vlucas/phpdotenv",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/vlucas/phpdotenv.git",
                "reference": "5084b23845c24dbff8ac6c204290c341e4776c92"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vlucas/phpdotenv/zipball/5084b23845c24dbff8ac6c204290c341e4776c92",
                "reference": "5084b23845c24dbff8ac6c204290c341e4776c92",
                "shasum": ""
            },
            "require": {
                "php": "^5.4 || ^7.0",
                "phpoption/phpoption": "^1.5",
                "symfony/polyfill-ctype": "^1.9"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.0 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Dotenv\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Vance Lucas",
                    "email": "vance@vancelucas.com",
                    "homepage": "http://www.vancelucas.com"
                }
            ],
            "description": "Loads environment variables from `.env` to `getenv()`, `$_ENV` and `$_SERVER` automagically.",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "time": "2019-06-15T22:40:20+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozart/assert.git",
                "reference": "83e253c8e0be5b0257b881e1827274667c5c17a9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozart/assert/zipball/83e253c8e0be5b0257b881e1827274667c5c17a9",
                "reference": "83e253c8e0be5b0257b881e1827274667c5c17a9",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6",
                "sebastian/version": "^1.0.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Webmozart\\Assert\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Assertions to validate method input/output with nice error messages.",
            "keywords": [
                "assert",
                "check",
                "validate"
            ],
            "time": "2018-12-25T11:19:39+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "dev",
    "stability-flags": [],
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": [],
    "platform-dev": []
}


File: /config\mikrotik.php
<?php

return [
    'auth' => [
        'host' => env('MK_API_HOST', null),
        'user' => env('MK_API_USER', 'admin'),
        'password' => env('MK_API_PASSWORD', ''),
        'port' => env('MK_API_PORT', 8728)
    ],
    'entities' => [
        'interface' => \jjsquady\MikrotikApi\Entity\InterfaceEntity::class
    ]
];

File: /phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit backupGlobals="true"
         backupStaticAttributes="false"
         bootstrap="vendor/autoload.php"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false"
>
    <testsuites>
        <testsuite name="">
            <directory suffix=".php">./tests</directory>
        </testsuite>
    </testsuites>
</phpunit>

File: /readme.md
# Mikrotik Api for Laravel 8.x
WIP - Work In Progress

Instalation
----

Via composer:
```
composer require jjsquady/mikrotikapi
```

Or manually insert this block into your composer.json in require section:
```
"require": {
    "jjsquady/mikrotikapi": "dev-master", // <- this line
}
```

Configuration on Laravel (< 5.4):
----

Insert into `config/app.php` in `providers` array:

```
jjsquady\MikrotikApi\MikrotikServiceProvider::class
```

#### Use the Facade:

Insert into `config/app.php` in `facades` array:

```
'Mikrotik' => jjsquady\MikrotikApi\Facades\MikrotikFacade::class
```

**Note:** for Laravel 5.4+ this package comes with Package Discovery enabled.


#### Publish the configuration file:

```
php artisan vendor:publish --provider=jjsquady\MikrotikApi\MikrotikServiceProvider
```

Basic Usage:
----

Set up the host and credentials into .env file:

```$bash
   MK_API_HOST=<mk_ip>
   MK_API_USER=<username>
   MK_API_PASSWORD=<password>
   MK_API_PORT=<mk_port_defaults_8728>
```

```$php

// create a connection with Mikrotik Router

$conn = Mikrotik::connect()->getConnection();
 
if($conn->isConnected()) {
    // you have access to Commands
    // and can call from here...
}
```

Getting interfaces:
---
```$php
$conn = Mikrotik::connect()->getConnection();
 
if($conn->isConnected()) {
    // Get all interfaces
    $interfaces = Interfaces::bind($conn)->get();
    
    // get() returns a Collection and you can use all methods available
    
    // you can send it to view 
    return view("<some_view>", [
        'interfaces' => $interfaces
    ]);
}
```

This project its a work in progress... and its in early developing phase.
I really get thankful with ur contribution.

##### Created by jjsquady (Jorge Junior)
##### (cc) 2017-2019
##### License: MIT


File: /src\Commands\Command.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 21:31
 */

namespace jjsquady\MikrotikApi\Commands;

use jjsquady\MikrotikApi\Contracts\CommandContract as CommandInterface;
use jjsquady\MikrotikApi\Core\Client;
use jjsquady\MikrotikApi\Core\QueryBuilder;
use jjsquady\MikrotikApi\Core\Request;
use jjsquady\MikrotikApi\Entity\Entity;
use jjsquady\MikrotikApi\Entity\GenericEntity;
use jjsquady\MikrotikApi\Exceptions\CommandException;
use jjsquady\MikrotikApi\Exceptions\InvalidCommandException;
use jjsquady\MikrotikApi\Support\EntityUtils;

/**
 * Class Command
 * @package MiKontrol\Http\MikrotikApi\Commands
 */
abstract class Command implements CommandInterface
{
    use EntityUtils;

    /**
     * @var mixed
     */
    private $_response;


    /**
     * @var boolean
     */
    private $_async;

    /**
     * @var Client
     */
    protected $client;

    /**
     * @var Entity
     */
    protected $entityClass;

    protected $entity;

    /**
     * @var string
     */
    protected $rootPath;

    /**
     * @var \PEAR2\Net\RouterOS\Request
     */
    protected $request;

    /**
     * @var array
     */
    protected $commands = [];

    /**
     * @var array
     */
    protected $commandsAlias = [];

    /**
     * @var QueryBuilder
     */
    protected $query;


    /**
     * Command constructor.
     * @param Client $client
     * @throws CommandException
     */
    public function __construct(Client $client)
    {
        $this->client  = $client;

        $this->entityClass = $this->entityClass ?? GenericEntity::class;

        $this->entity = (new $this->entityClass);

        $this->rootPath = $this->entity->getPath();

        if(!$this->rootPath) {
            throw new CommandException('Command not found.');
        }

        $this->request = new Request($this->rootPath);
    }

    /**
     * @param $command
     * @param null $args
     * @return $this
     */
    private function executeCommand($command, $args = null)
    {
        $this->request = new Request($command);

        $this->processCommandArgs($args);

        $this->_response = $this->processCommand();

        return $this;

    }

    /**
     *
     * @return \jjsquady\MikrotikApi\Core\Collection
     */
    public function get()
    {
        $this->executeCommand($this->rootPath . '/print');
        return $this->convertArrayToEntities($this->_response);
    }

    public function remove($id)
    {
        $this->executeCommand($this->rootPath . '/remove', ['.id' => $id]);
    }

    public function find($attribute, $value = null)
    {
        // TODO: Implement find() method.
    }

    /**
     * @return mixed
     */
    public function getBaseCommand()
    {
        return $this->rootPath;
    }

    /**
     * @param array $args
     * @return string
     */
    protected function buildCommandPath(array $args)
    {
        if (!is_array($args)) {
            //TODO: throw exception
        }

        if (empty(array_last($args))) {
            return implode('', $args);
        }

        return implode("/", $args);
    }

    /**
     * @param $name
     * @param $arguments
     * @return QueryBuilder
     * @throws InvalidCommandException
     */
    public function __call($name, $arguments)
    {
        if (array_key_exists($name, $this->commands)) {
            $command = array_key_exists($name, $this->commandsAlias) ? $this->commandsAlias[$name] : $name;
            $fullCommand = $this->buildCommandPath([$this->base_command, $command]);
            return $this->buildNewQuery($this->commands[$name], $fullCommand);
        }

        throw new InvalidCommandException($name);
    }

    /**
     * @param $entityClass
     * @param $command
     * @return QueryBuilder
     */
    protected function buildNewQuery($entityClass, $command)
    {
        $this->query = new QueryBuilder($entityClass, $command, $this->client);
        return $this->query;
    }

    /**
     * @return \PEAR2\Net\RouterOS\ResponseCollection
     */
    private function processCommand()
    {
        return $this->client->sendSync($this->request);
    }

    /**
     * @param $args
     */
    private function processCommandArgs($args)
    {
        if (!is_array($args)) {
            return;
        }

        array_map(function ($arg) {
            $this->request->setArgument($arg);
        }, $args);
    }

    public static function bind(Client $client)
    {
        try {

            return new static($client);

        } catch (CommandException $e) {

            throw new CommandException($e);

        }
    }

}

File: /src\Commands\Interfaces.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 00:17
 */

namespace jjsquady\MikrotikApi\Commands;

use jjsquady\MikrotikApi\Core\Client;
use jjsquady\MikrotikApi\Exceptions\CommandException;

/**
 * Class InterfaceCommand
 * @package MiKontrol\Http\MikrotikApi\Commands
 */
class Interfaces extends Command
{
    /**
     * Interfaces constructor.
     * @param Client $client
     * @throws CommandException
     */
    public function __construct(Client $client)
    {
        $this->entityClass = config('mikrotik.entities.interface');

        parent::__construct($client);
    }

    /**
     * @param $id
     * @throws CommandException
     */
    public function remove($id)
    {
        throw new CommandException('Interfaces cannot be removed.');
    }
}

File: /src\Commands\Ip.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 22:03
 */

namespace jjsquady\MikrotikApi\Commands;

use jjsquady\MikrotikApi\Entity\Accounting;
use jjsquady\MikrotikApi\Entity\Address;
use jjsquady\MikrotikApi\Entity\Arp;

/**
 * Class IP
 * @package MiKontrol\Http\MikrotikApi\Commands
 */
class Ip extends Command
{

    /**
     * @var string
     */
    protected $base_command = '/ip';

    protected $commands = [
        'address' => Address::class,
        'arp' => Arp::class,
        'accounting' => Accounting::class
    ];

    public function address()
    {
        return $this->__call("address", null);
    }

    public function arp()
    {
        return $this->__call("arp", null);
    }

}

File: /src\Contracts\ClientContract.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 03:48
 */

namespace jjsquady\MikrotikApi\Contracts;


interface ClientContract
{
    function close();
    function isConnected();
    function api();
    function write($command, $params = true);
    function read($pretty = true);
}

File: /src\Contracts\CommandContract.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 21:26
 */

namespace jjsquady\MikrotikApi\Contracts;


use jjsquady\MikrotikApi\Core\Client;

interface CommandContract
{
    public function get();

    public function remove($id);

    public function find($attribute, $value = null);

    public function getBaseCommand();

    public static function bind(Client $client);
}

File: /src\Contracts\MikrotikContract.php
<?php
/**
 * Created by PhpStorm.
 * User: jjsquady
 * Date: 2019-06-24
 * Time: 03:06
 */

namespace jjsquady\MikrotikApi\Contracts;

interface MikrotikContract
{
    public function connect();

    public function getConnection();

    public function getCredentials();
}

File: /src\Core\Client.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 01:07
 */

namespace jjsquady\MikrotikApi\Core;

use jjsquady\MikrotikApi\Exceptions\ConnectionException;
use PEAR2\Net\RouterOS\Client as RouterClient;

class Client extends RouterClient
{
    /**
     * @var boolean
     */
    protected $connected;

    /**
     * Client constructor.
     * @param mixed ...$args
     * @throws ConnectionException
     */
    public function __construct(...$args)
    {
        try {
            parent::__construct(...$args);

            $this->connected = true;

        }catch (\Exception $exception) {

            $this->connected = false;

            throw new ConnectionException($exception->getMessage());
        }
    }

    /**
     * @return mixed
     */
    public function isConnected()
    {
        return $this->connected;
    }
}

File: /src\Core\Collection.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 02:14
 */

namespace jjsquady\MikrotikApi\Core;

use Illuminate\Support\Collection as IlluminateCollection;

class Collection extends IlluminateCollection
{
    public function add($value)
    {
        parent::push($value);
        return $this;
    }
}

File: /src\Core\QueryBuilder.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 01:40
 */

namespace jjsquady\MikrotikApi\Core;

use jjsquady\MikrotikApi\Support\EntityUtils;
use PEAR2\Net\RouterOS\Query as RouterQuery;
use PEAR2\Net\RouterOS\Util;

class QueryBuilder extends RouterQuery
{
    use EntityUtils;

    protected $entityClass;

    protected $client;

    protected $directory;

    public function __construct($entityClassName, $directory, Client $client)
    {
        $this->entityClass = $entityClassName;
        $this->client      = $client;
        $this->directory   = $directory;
    }

    public static function find($params)
    {

    }

    public static function where($property, $value = null, $operator = self::OP_EQ)
    {

    }

    public function all()
    {
        return $this->execute();
    }

    public function first()
    {
        return $this->all()->first();
    }

    public function get($args = array(), $query = null)
    {
        return $this->execute($args, $query);
    }

    private function execute($args = array(), $query = null)
    {
        $util = new Util($this->client);

        $util->setMenu($this->directory);

        $items = $util->getAll($args, $query);

        return $this->convertArrayToEntities($items, $this->entityClass);
    }


}

File: /src\Core\Request.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 01:10
 */

namespace jjsquady\MikrotikApi\Core;


use PEAR2\Net\RouterOS\Request as RouterRequest;

class Request extends RouterRequest
{

}

File: /src\Entity\Address.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 04:44
 */

namespace jjsquady\MikrotikApi\Entity;


class Address extends Entity
{
    /**
     * @var array
     */
    protected $fillable = [
        '.id',
        'address',
        'network',
        'interface',
        'actual-interface',
        'invalid',
        'dynamic',
        'disabled',
        'comment'
    ];
}

File: /src\Entity\Bridge.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 05:03
 */

namespace jjsquady\MikrotikApi\Entity;


class Bridge extends Entity
{
    /**
     * @var array
     */
    protected $fillable = [
        '.id',
        'name',
        'mtu',
        'l2mtu',
        'arp',
        'mac-address',
        'protocol-mode',
        'priority',
        'auto-mac',
        'admin-mac',
        'max-message-age',
        'forward-delay',
        'transmit-hold-count',
        'ageing-time',
        'running',
        'disabled',
        'comment'
    ];
}

File: /src\Entity\Entity.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 22:54
 */

namespace jjsquady\MikrotikApi\Entity;

use jjsquady\MikrotikApi\Core\QueryBuilder;
use ReflectionClass;

/**
 * Class Entity
 * @package MiKontrol\Http\MikrotikApi\Commands\Entity
 */
abstract class Entity
{

    protected $query;

    protected $directory;

    protected $fillable;

    public function __construct($query = null)
    {
        if ($query instanceof QueryBuilder) {
            $this->query = $query;
        }
    }

    public function getPath()
    {
        return $this->directory;
    }

    public function toArray()
    {
        return get_object_vars($this);
    }

    public function getDirectory()
    {
        return $this->directory;
    }

    /**
     * @return string
     */
    public function __toString()
    {
        return json_encode($this);
    }

    /**
     * @param $property
     * @return null
     */
    public function __get($property)
    {
        $propertyClean = $this->convertToDashes($property);

        if (isset($this->fillable)) {
            return $this->getFillableProperty($propertyClean);
        }

        return property_exists($this, $propertyClean) ? $this->{$propertyClean} : null;
    }

    public function setAttributes(array $attributes)
    {
        foreach ($attributes as $attribute => $value) {
            in_array($attribute, $this->fillable) ? $this->{$attribute} = $value : null;
        }

        return $this;
    }

    /**
     * If $fillable array its set, then looks into this array for properties
     * @param $property
     * @return null
     */
    private function getFillableProperty($property)
    {
        return in_array($property, $this->fillable) ?
            property_exists($this, $property) ?
                $this->{$property} :
                null :
            null;
    }

    /**
     * Convertes a camelCase property to hyphened-case (myProp -> my-prop)
     * @param $property
     * @return string
     */
    private function convertToDashes($property)
    {
        preg_match_all('!([A-Z][A-Z0-9]*(?=$|[A-Z][a-z0-9])|[A-Za-z][a-z0-9]+)!', $property, $matches);
        $ret = $matches[0];
        foreach ($ret as &$match) {
            $match = $match == strtoupper($match) ? strtolower($match) : lcfirst($match);
        }
        return implode('-', $ret);
    }
}

File: /src\Entity\Ethernet.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 01:18
 */

namespace jjsquady\MikrotikApi\Entity;


/**
 * Class Ethernet
 * @package MiKontrol\Http\MikrotikApi\Commands\Entity
 */
class Ethernet extends Entity
{
    /**
     * @var array
     */
    protected $fillable = [
        '.id',
        'name',
        'mtu',
        'mac-address',
        'arp',
        'disable-running-check',
        'auto-negotiation',
        'full-duplex',
        'cable-settings',
        'speed',
        'running',
        'slave',
        'disabled',
        'comment'
    ];
}

File: /src\Entity\GenericEntity.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 09:11
 */

namespace jjsquady\MikrotikApi\Entity;


class GenericEntity extends Entity
{
    protected $directory = '/';

    protected $fillable = [];
}

File: /src\Entity\InterfaceEntity.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 00:19
 */

namespace jjsquady\MikrotikApi\Entity;


class InterfaceEntity extends Entity
{
    protected $directory = '/interface';

    protected $fillable = [
        '.id',
        'name',
        'type',
        'mtu',
        'dynamic',
        'running',
        'disabled',
        'comment'
    ];
}

File: /src\Exceptions\CommandException.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 20/04/2017
 * Time: 19:39
 */

namespace jjsquady\MikrotikApi\Exceptions;


use Exception;

class CommandException extends Exception
{
    public function __construct($message)
    {
        parent::__construct($message);
    }
}

File: /src\Exceptions\ConnectionException.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 03:40
 */

namespace jjsquady\MikrotikApi\Exceptions;


use Exception;

class ConnectionException extends Exception
{
    public function __construct($host)
    {
        $message = "Cannot connect to Router on {$host}. Verify credentials and if host its working.";
        parent::__construct($message);
    }
}

File: /src\Exceptions\InvalidCommandException.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 00:37
 */

namespace jjsquady\MikrotikApi\Exceptions;

use Exception;

class InvalidCommandException extends Exception
{
    public function __construct($command)
    {
        $message = "Invalid command ({$command}). No such command or directory.";
        parent::__construct($message);
    }
}

File: /src\Exceptions\WrongArgumentTypeException.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 03:34
 */

namespace jjsquady\MikrotikApi\Exceptions;


use Exception;

class WrongArgumentTypeException extends Exception
{
    public function __construct($needed, $passed)
    {
        $message = "Expected {$needed}, but an {$passed} has found.";
        parent::__construct($message);
    }
}

File: /src\Facades\MikrotikFacade.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 21:12
 */

namespace jjsquady\MikrotikApi\Facades;


use Illuminate\Support\Facades\Facade;

class MikrotikFacade extends Facade
{
    protected static function getFacadeAccessor()
    {
        return 'mikontrollib';
    }
}

File: /src\Mikrotik.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 17/04/2017
 * Time: 21:15
 */

namespace jjsquady\MikrotikApi;

use jjsquady\MikrotikApi\Contracts\MikrotikContract;
use jjsquady\MikrotikApi\Core\Client;
use jjsquady\MikrotikApi\Exceptions\ConnectionException;

/**
 * Class Mikrotik
 * @package jjsquady\MikrotikApi
 */
class Mikrotik implements MikrotikContract
{
    /**
     * @var array
     */
    protected $credentials = [];

    /**
     * @var Client
     */
    protected $connection;

    /**
     * Mikrotik constructor.
     * @param $host
     * @param string $username
     * @param string $password
     * @param int $port
     */
    public function __construct($host, $username = 'admin', $password = '', $port = 8728)
    {
        $this->credentials = [
            'host' => $host,
            'username' => $username,
            'password' => $password,
            'port' => $port
        ];
    }

    /**
     * Connects to a MK host
     *
     * @return Mikrotik
     * @throws ConnectionException
     */
    public function connect()
    {
        $this->connection = new Client(...array_values($this->credentials));

        return $this;
    }

    /**
     * @return Client
     */
    public function getConnection()
    {
        return $this->connection;
    }

    /**
     * Get the credentials
     * @return array
     */
    public function getCredentials()
    {
        return $this->credentials;
    }

}

File: /src\MikrotikServiceProvider.php
<?php

namespace jjsquady\MikrotikApi;

use Illuminate\Support\ServiceProvider;

/**
 * Class MikrotikServiceProvider
 * @package jjsquady\MikrotikApi
 */
class MikrotikServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap the application services.
     *
     * @return void
     */
    public function boot()
    {
        $this->publishes([
            __DIR__ . '/../config/mikrotik.php' => config_path('mikrotik.php')
        ]);
    }

    /**
     * Register the application services.
     *
     * @return void
     */
    public function register()
    {
        $this->mergeConfigFrom(__DIR__ . '/../config/mikrotik.php', 'mikrotik');

        $this->app->singleton('mikontrollib', function($app) {
            return new Mikrotik(
                config('mikrotik.auth.host'),
                config('mikrotik.auth.user'),
                config('mikrotik.auth.password'),
                config('mikrotik.auth.port'),
            );
        });
    }

    public function provides()
    {
        return [
            'mikontrollib'
        ];
    }
}


File: /src\Support\EntityUtils.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 03:50
 */

namespace jjsquady\MikrotikApi\Support;

use jjsquady\MikrotikApi\Core\Collection;
use jjsquady\MikrotikApi\Entity\Entity;
use PEAR2\Net\RouterOS\Response;
use PEAR2\Net\RouterOS\ResponseCollection;

/**
 * Class EntityUtils
 * @package jjsquady\MikrotikApi\Support
 */
trait EntityUtils
{

    /**
     * @param $items
     * @return Collection
     */
    private function convertArrayToEntities($items)
    {
        if (!is_array($items)) {
            // TODO: throw exception
        }

        $collection = new Collection();

        foreach ($items as $item) {
            if ($item->getType() == Response::TYPE_DATA) {
                $collection->add(
                    $this->entity->setAttributes($this->getEntityProperties($item))
                );
            }
        }

        return $collection;
    }

    /**
     * @param $array
     * @return array
     */
    private function getEntityProperties($array)
    {
        $attributes = [];

        foreach ($array as $property => $value) {
            $attributes[$property] = $value;
        }

        return $attributes;
    }
}

File: /src\Support\InterfaceEnums.php
<?php

/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 01:51
 */
class InterfaceEnums
{
    static function ArpTypes()
    {
        return [
            'disabled',
            'enabled',
            'proxy-arp',
            'replay-only'
        ];
    }
}

File: /tests\AuthTest.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 18/04/2017
 * Time: 05:05
 */

namespace jjsquady\MikrotikApi\Tests;

use jjsquady\MikrotikApi\Core\Client;
use jjsquady\MikrotikApi\Exceptions\ConnectionException;
use jjsquady\MikrotikApi\Facades\MikrotikFacade as Mikrotik;
use jjsquady\MikrotikApi\Tests\Traits\CreateApplication;
use Orchestra\Testbench\TestCase;


class AuthTest extends TestCase
{
    use CreateApplication;

    private $client;

    private $mikrotik;

    protected function setUp(): void
    {
        parent::setUp();

        $this->mikrotik = Mikrotik::connect();

        $this->client = $this->mikrotik->getClient();
    }

    public function test_if_connection_returns_client_instance()
    {
        $this->assertInstanceOf(Client::class, $this->client);
    }

    public function test_if_throws_connection_exception()
    {
        $this->expectException(ConnectionException::class);

        (new \jjsquady\MikrotikApi\Mikrotik(config('mikrotik.auth.host'), 'wronguser'))->connect();

    }

    public function test_getting_credentials()
    {
        $this->assertIsArray($this->mikrotik->getCredentials());

        $this->assertTrue(in_array('admin', $this->mikrotik->getCredentials()));
    }

}


File: /tests\InterfacesCommandsTest.php
<?php
/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 01:17
 */

namespace jjsquady\MikrotikApi\Tests;

use jjsquady\MikrotikApi\Commands\Interfaces;
use jjsquady\MikrotikApi\Entity\InterfaceEntity;
use jjsquady\MikrotikApi\Facades\MikrotikFacade as Mikrotik;
use jjsquady\MikrotikApi\Tests\Traits\CreateApplication;
use Orchestra\Testbench\TestCase;

class InterfacesCommandsTest extends TestCase
{
    use CreateApplication;

    protected $client;

    protected function setUp(): void
    {
        parent::setUp();

        $this->client = Mikrotik::connect()->getClient();
    }

    public function test_execute_command_sync_response_array()
    {
        $response = Interfaces::bind($this->client)
            ->get()
            ->toArray();
        $this->assertEquals(true, is_array($response));
    }

    public function test_returns_an_interface_entity_object()
    {
        $response = Interfaces::bind($this->client)->get()->first();
        $this->assertInstanceOf(InterfaceEntity::class, $response);
    }
}


File: /tests\IpCommandsTest.php
<?php

/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 04:45
 */

use jjsquady\MikrotikApi\Commands\Ip;
use jjsquady\MikrotikApi\Core\Collection;
use jjsquady\MikrotikApi\Core\QueryBuilder;
use Orchestra\Testbench\TestCase;
use jjsquady\MikrotikApi\Facades\MikrotikFacade as Mikrotik;

class IpCommandsTest extends TestCase
{
    protected function getPackageProviders($app)
    {
        return [jjsquady\MikrotikApi\MikrotikServiceProvider::class];
    }

    protected function getPackageAliases($app)
    {
        return [
            'Mikrotik' => jjsquady\MikrotikApi\Facades\MikrotikFacade::class
        ];
    }

    public function getConn()
    {
        $client = Mikrotik::connect(['192.168.0.20', 'admin', '']);
        return $client;
    }

    public function test_if_command_works()
    {
        $this->assertInstanceOf(Ip::class, new Ip($this->getConn()));
    }

    public function test_if_command_address_exists()
    {
        $ipcomm = new Ip($this->getConn());
        $this->assertInstanceOf(QueryBuilder::class, $ipcomm->address());
    }

    public function test_arp_method()
    {
        $ipcomm = new Ip($this->getConn());
        $this->assertInstanceOf(QueryBuilder::class, $ipcomm->arp());
    }

    public function test_accounting_method()
    {
        $ipcomm = new Ip($this->getConn());
        $this->assertInstanceOf(Collection::class, $ipcomm->accounting()->all());
    }
}

File: /tests\StaticCommandTest.php
<?php

/**
 * Created by PhpStorm.
 * User: Jorge
 * Date: 19/04/2017
 * Time: 07:26
 */

namespace jjsquady\MikrotikApi\Tests;

use jjsquady\MikrotikApi\Core\Client;
use jjsquady\MikrotikApi\Facades\MikrotikFacade as Mikrotik;
use jjsquady\MikrotikApi\Tests\Traits\CreateApplication;
use Orchestra\Testbench\TestCase;

class StaticCommandTest extends TestCase
{
    use CreateApplication;
    
    /** @test **/
    public function it_a_client_mikrotik_instance()
    {
        $this->assertInstanceOf(Client::class, Mikrotik::connect()->getClient());
    }
}


File: /tests\Traits\CreateApplication.php
<?php
/**
 * Created by PhpStorm.
 * User: jjsquady
 * Date: 2019-06-24
 * Time: 01:20
 */

namespace jjsquady\MikrotikApi\Tests\Traits;

trait CreateApplication
{
    /**
     * Define environment setup.
     *
     * @param  \Illuminate\Foundation\Application  $app
     * @return void
     */
    protected function getEnvironmentSetUp($app)
    {
        $env = \Dotenv\Dotenv::create(__DIR__ . '/../../')->load();
        $app['config']->set('mikrotik.auth.host', $env['MK_API_HOST']);
        $app['config']->set('mikrotik.auth.user', $env['MK_API_USER']);
        $app['config']->set('mikrotik.auth.password', $env['MK_API_PASSWORD']);
        $app['config']->set('mikrotik.auth.port', $env['MK_API_PORT']);
    }

    protected function getPackageProviders($app)
    {
        return [\jjsquady\MikrotikApi\MikrotikServiceProvider::class];
    }

    protected function getPackageAliases($app)
    {
        return [
            'Mikrotik' => \jjsquady\MikrotikApi\Facades\MikrotikFacade::class
        ];
    }
}

