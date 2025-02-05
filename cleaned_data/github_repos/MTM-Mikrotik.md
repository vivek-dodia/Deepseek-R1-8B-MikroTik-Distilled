# Repository Information
Name: MTM-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/MTM-Mikrotik/
    ├── .buildpath
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
    │   │       ├── pack-9ee531daf6cff0e62cb5ab79976b069590522f55.idx
    │   │       └── pack-9ee531daf6cff0e62cb5ab79976b069590522f55.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .project
    ├── .settings/
    │   ├── org.eclipse.php.core.prefs
    │   └── org.eclipse.wst.common.project.facet.core.xml
    ├── composer.json
    ├── Docs/
    │   ├── Examples/
    │   │   └── ISC-DHCP/
    │   │       └── dhcpd.conf
    │   └── README.md
    ├── Enable.php
    ├── Factories/
    │   ├── Base.php
    │   └── Tools.php
    ├── Factories.php
    ├── README.md
    └── Tools/
        └── NetInstall/
            ├── API.php
            ├── Discovery.php
            └── Flash.php


# Content
File: /.buildpath
<?xml version="1.0" encoding="UTF-8"?>
<buildpath>
	<buildpathentry kind="src" path=""/>
	<buildpathentry kind="con" path="org.eclipse.php.core.LANGUAGE"/>
</buildpath>


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/hjf288/MTM-Mikrotik.git
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
0000000000000000000000000000000000000000 abc616e48d697cbde5e31e8d38fd8800d567268b vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/hjf288/MTM-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 abc616e48d697cbde5e31e8d38fd8800d567268b vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/hjf288/MTM-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 abc616e48d697cbde5e31e8d38fd8800d567268b vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/hjf288/MTM-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
abc616e48d697cbde5e31e8d38fd8800d567268b refs/remotes/origin/master


File: /.git\refs\heads\master
abc616e48d697cbde5e31e8d38fd8800d567268b


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.project
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>MTM-Mikrotik</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.eclipse.wst.validation.validationbuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
		<buildCommand>
			<name>org.eclipse.dltk.core.scriptbuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>org.eclipse.php.core.PHPNature</nature>
	</natures>
</projectDescription>


File: /.settings\org.eclipse.php.core.prefs
eclipse.preferences.version=1
include_path=0;/MTM-Mikrotik


File: /.settings\org.eclipse.wst.common.project.facet.core.xml
<?xml version="1.0" encoding="UTF-8"?>
<faceted-project>
  <fixed facet="php.component"/>
  <fixed facet="php.core.component"/>
  <installed facet="php.core.component" version="1"/>
  <installed facet="php.component" version="7.2"/>
</faceted-project>


File: /composer.json
{
	"name" : "merlinthemagic/mtm-mikrotik",
	"type" : "library",
	"description" : "Mikrotik tools for PHP 7",
	"version" : "0.0.1",
	"keywords" : [
		"mikrotik",
		"net-install",
		"routeros"
	],
	"homepage" : "https://github.com/merlinthemagic/MTM-Mikrotik",
	"license" : "LGPL-3.0",
	"authors" : [{
			"name" : "Martin Peter Madsen",
			"email" : "dev@martinpetermadsen.com",
			"role" : "Developer"
		}
	],
	"require" : {
		"php" : ">=7.3.0"
	},
	"autoload" : {
		"files" : [
			"./Enable.php"
		]
	},
	"minimum-stability" : "dev"
}

File: /Docs\Examples\ISC-DHCP\dhcpd.conf
ddns-update-style interim;
default-lease-time 300;
max-lease-time 600;
authoritative;
allow booting;
allow bootp;
##tftp server is located on the edge provisioning device
next-server 10.192.3.2;
interfaces="ens34";

class "mmipsBoot" {
        match if substring(option vendor-class-identifier, 0, 9) = "MMipsBoot";
}
class "armBoot" {
        match if substring(option vendor-class-identifier, 0, 9) = "ARM__boot";
}

subnet 10.192.3.0 netmask 255.255.255.0 {

        option domain-name-servers 10.192.1.2, 10.192.1.3;
        option routers 10.192.3.1;
        option broadcast-address 10.192.3.255;
        pool {
                allow dynamic bootp clients;
                allow members of "mmipsBoot";
                allow members of "armBoot";
                range dynamic-bootp 10.192.3.51 10.192.3.150;

                if substring(option vendor-class-identifier, 0, 9) = "MMipsBoot" {
                        filename "mmips_boot_6.42.5";
                } elsif substring(option vendor-class-identifier, 0, 9) = "ARM__boot" {
                        filename "arm_boot_6.42.5";
                }
        }
        pool {
                range 10.192.3.151 10.192.3.250;
        }
}


File: /Docs\README.md
### NetInstall:

#### install:

```
composer require mtm-mikrotik;
```

I assume your device has been served vmlinux from a tftp server and is ready for net install.
one way to do this is using <a href="./Examples/ISC-DHCP/dhcpd.conf">ISC DHCP</a> with a bootp config to serve up the vmlinux image.
if you just want to test, use the regular net install for this and once the device shows as "ready" you can proceed

#### ready the tool object:

```
require_once "/path/to/mtm-mikrotik/Enable.php";
$toolObj	= \MTM\Mikrotik\Factories::getTools()->getNetInstall();
```

#### set environment:

Set the ip and mac from the SERVER interface you wish to use
these are the values from the server the PHP script is running on
remember the server must have L2 access to the routerboard, L2 VPN access if fine

```
$ip		= "10.155.9.46";
$mac	= "00:0c:29:17:c6:fb";
$toolObj->setTxConfig($ip, $mac);
```

#### Identify the routerboard you want to NetInstall:

if you dont know the mac, or want to validate the device is ready for netInstall use this, otherwise skip this step:

```
$devObjs	= $toolObj->getDeviceList()
print_r($devObjs);
```

#### Flash a device

```
//MANDATORY: MAC address of Ether1 on the routerboard
$macAddr		= "B969B4234D37";

//MANDATORY: path to the NPK file downloaded from MT
$fwPath		= "/path/to/npk/file/routeros-arm-6.44.6.npk";

//OPTIONAL: path to the script that should be set as the default config
$scriptPath	= "/path/to/my/script/resetToDefaults.rsc";
	
//execute the net install
$toolObj->flashByMac($macAddr, $fwPath, $scriptPath);
```

done, unit will reboot and trigger the default config script if needed



File: /Enable.php
<?php
// 2019 Martin Peter Madsen
if (defined("MTM_MIKROTIK_BASE_PATH") === false) {
	define("MTM_MIKROTIK_BASE_PATH", __DIR__ . DIRECTORY_SEPARATOR);
	spl_autoload_register(function($className)
	{
		if (class_exists($className) === false) {
			$cPath		= array_values(array_filter(explode("\\", $className)));
			if (array_shift($cPath) == "MTM" && array_shift($cPath) == "Mikrotik") {
				$filePath	= MTM_MIKROTIK_BASE_PATH . implode(DIRECTORY_SEPARATOR, $cPath) . ".php";
				if (is_readable($filePath) === true) {
					require_once $filePath;
				}
			}
		}
	});
	function loadMtmMikrotik()
	{
		
	}
	loadMtmMikrotik();
}

File: /Factories\Base.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik\Factories;

class Base
{
	protected $_s=array();
}

File: /Factories\Tools.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik\Factories;

class Tools extends Base
{
	public function getNetInstall()
	{
		if (array_key_exists(__FUNCTION__, $this->_s) === false) {
			$this->_s[__FUNCTION__]	= new \MTM\Mikrotik\Tools\NetInstall\API();
		}
		return $this->_s[__FUNCTION__];
	}
}

File: /Factories.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik;

class Factories
{
	private static $_s=array();
	
	//USE: $aFact		= \MTM\Mikrotik\Factories::$METHOD_NAME();
	
	public static function getTools()
	{
		if (array_key_exists(__FUNCTION__, self::$_s) === false) {
			self::$_s[__FUNCTION__]	= new \MTM\Mikrotik\Factories\Tools();
		}
		return self::$_s[__FUNCTION__];
	}
}

File: /README.md
# MTM-Mikrotik

File: /Tools\NetInstall\API.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik\Tools\NetInstall;

class API extends Flash
{
	protected $_s=array();
	protected $_rxSockObj=null;
	protected $_txSockObj=null;
	protected $_rxMaxBytes=1024;
	protected $_txIpAddr=null;
	protected $_txMacAddr=null;
	
	public function __destruct()
	{
		if (is_resource($this->_rxSockObj) === true) {
			socket_close($this->_rxSockObj);
		}
		if (is_resource($this->_txSockObj) === true) {
			socket_close($this->_txSockObj);
		}
	}
	public function setTxConfig($ipAddr, $macAddr)
	{
		//only set this if you have multiple interfaces
		//you might only be able to set this if the default route originates from the same interface as the ip
		$this->_txIpAddr	= $ipAddr;
		$this->_txMacAddr	= preg_replace("/[^a-fA-F0-9]+/", "", strtoupper(trim($macAddr)));
		return $this;
	}
	protected function getRxSocket()
	{
		if ($this->_rxSockObj === null) {
			$sockObj = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
			socket_set_option($sockObj, SOL_SOCKET, SO_REUSEADDR, 1);
			socket_bind($sockObj, "0.0.0.0", 5000);
			socket_set_nonblock($sockObj);
			$this->_rxSockObj	= $sockObj;
		}
		return $this->_rxSockObj;
	}
	protected function socketRead($timeoutMs=10000)
	{
		$tTime	    = \MTM\Utilities\Factories::getTime()->getMicroEpoch() + ($timeoutMs / 1000);
		$sockObj	= $this->getRxSocket();
		while (true) {

			$data		= socket_read($sockObj, $this->_rxMaxBytes);
			$dLen		= strlen(trim($data));
			if ($dLen > 0) {
				
				$hexData				= bin2hex($data);
				
				$rObj					= new \stdClass();
				$heads					= new \stdClass();
				$payload				= new \stdClass();
				$rObj->headers			= $heads;
				$rObj->payload			= $payload;
				$rObj->raw				= $data;
				
				$payload->bytes			= $this->hexCountToDecimal(substr($hexData, 28, 4));
				$payload->hex			= substr($hexData, 40);
				$payload->bin			= hex2bin($payload->hex);

				$heads->srcPos			= $this->hexCountToDecimal(substr($hexData, 32, 4));
				$heads->dstPos			= $this->hexCountToDecimal(substr($hexData, 36, 4));
				$heads->srcMac			= strtoupper(substr($hexData, 0, 12));
				$heads->dstMac			= strtoupper(substr($hexData, 12, 12));
				
				return $rObj;
				
			} elseif (\MTM\Utilities\Factories::getTime()->getMicroEpoch() > $tTime) {
				throw new \Exception("Read Timeout", 13465);
			} else {
				usleep(10000);
			}
		}
	}
	protected function getTxSocket()
	{
		if ($this->_txSockObj === null) {
			$sockObj = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
			socket_set_option($sockObj, SOL_SOCKET, SO_REUSEADDR, 1);
			socket_set_option($sockObj, SOL_SOCKET, SO_BROADCAST, 1);
			
			//we need to bind on the interface that holds the default gateway
			if ($this->_txIpAddr === null) {
				throw new \Exception("You must set the server ip and mac");
				//$this->_txIpAddr	= getHostByName(getHostName()); //automate in the future?
			}
			socket_bind($sockObj, $this->_txIpAddr, 5000);
			socket_set_nonblock($sockObj);
			$this->_txSockObj	= $sockObj;
		}
		return $this->_txSockObj;
	}
	protected function socketWrite($data)
	{
		socket_sendto($this->getTxSocket(), $data, strlen($data), 0, "255.255.255.255", 5000);
		return $this;
	}
	protected function decCountToHex($dec)
	{
		$oHex	= dechex($dec);
		$oHex	= str_repeat("0", 4 - strlen($oHex)) . $oHex;
		$hPs	= str_split($oHex, 2);
		$oHex	= $hPs[1] . $hPs[0];
		return $oHex;
	}
	protected function hexCountToDecimal($hex)
	{
		$dPs	= str_split($hex, 2);
		return hexdec($dPs[1] . $dPs[0]);
	}
	protected function arrayToHex($array)
	{
		$hexStr	= "";
		foreach ($array as $item) {
			
			//if you send numbers as strings they will be handled as such
			if (is_int($item) === true) {
				$hex	= dechex($item);
			} else {
				$hex	= dechex(ord($item));
			}
			$hexStr	.= str_repeat("0", 2 - strlen($hex)) . $hex;
		}
		
		return $hexStr;
	}
}

File: /Tools\NetInstall\Discovery.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik\Tools\NetInstall;

class Discovery
{	
	public function getDeviceList($timeoutMs=10000)
	{
		$timeout	= $timeoutMs;
		$tObjs		= array();
		$rObjs		= array();
		$sTime  	= \MTM\Utilities\Factories::getTime()->getMicroEpoch();
		while (true) {
			
			try {
				
				$dataObj	= $this->socketRead($timeout);
				$rows		= explode("\n", $dataObj->payload->bin);
				if (count($rows) == 7) {
					
					$macAddr	= $dataObj->headers->srcMac;
					if (array_key_exists($macAddr, $tObjs) === false) {
						$tObjs[$macAddr]		= "Handled"; //tracking set
						$devObj					= new \stdClass();
						$licObj					= new \stdClass();
						$rbObj					= new \stdClass();
						
						$devObj->mac			= $macAddr;
						$devObj->license		= $licObj;
						$devObj->routerboard	= $rbObj;
						
						$licObj->id				= null;
						$licObj->key			= null;
						if (trim($rows[1]) != "") {
							$licObj->id			= trim($rows[1]);
						}
						if (trim($rows[2]) != "") {
							$licObj->key			= base64_decode(trim($rows[2]));
						}

						$rbObj->model		    = trim($rows[3]);
						$rbObj->architecture	= trim($rows[4]);
						$rbObj->minOs			= trim($rows[5]);//minimum version required for install
						
						//make sure we do not already discovered this device on another of its interfaces
						$exist		= false;
						$nMacVal	= hexdec(substr($macAddr, -8)); //on 32bit systems we cannot represent a 48 bit value
						foreach ($rObjs as $rId => $eObj) {
							if ($licObj->id == $eObj->license->id) {
								if ($nMacVal < hexdec(substr($eObj->mac, -8))) {
									//this interface has a lower index, lets use it instead
									//mikrotik allows flashing on ether1
									$rObjs[$rId]	= $devObj;
								}
								$exist	= true;
								break;
							}
						}
						if ($exist === false) {
							$rObjs[]      = $devObj;
						}

					} else {
						//already encountered that device once before, we are done
						break;
					}
					
				} else {
					//we got another type of message
				}

				//set a new timeout value, read returns any frame it receives
				$cTime  	= \MTM\Utilities\Factories::getTime()->getMicroEpoch();
				$timeout	= $timeoutMs - intval(($cTime - $sTime) * 1000);
				if ($timeout < 1) {
					//we have run out of time
					break;
				}
				
			} catch (\Exception $e) {
				switch ($e->getCode()) {
					case 13465:
						//timeout reading
						break;
					default:
						throw $e;
				}
			}
		}
		
		return $rObjs;
	}
	public function getDeviceByMacAddress($macAddr, $timeoutMs=10000)
	{
		$macAddr	= preg_replace("/[^a-fA-F0-9]+/", "", strtoupper(trim($macAddr)));
		$devObjs	= $this->getDeviceList($timeoutMs);
		foreach ($devObjs as $devObj) {
			if ($devObj->mac == $macAddr) {
				return $devObj;
			}
		}
		return null;
	}
}

File: /Tools\NetInstall\Flash.php
<?php
// 2019 Martin Peter Madsen
namespace MTM\Mikrotik\Tools\NetInstall;

class Flash extends Discovery
{	
	protected $_txMaxBytes=1024;
	protected $_txDelay=7500; //delay between packets in micro sec, this can be optimized. Major reason for slow execution
	
	public function flashByMac($macAddr, $fwPath, $scriptPath=null)
	{
		//discover the device using the mac to make sure we see it on the broadcast domain
		$devObj		= $this->getDeviceByMacAddress($macAddr);
		if ($devObj === null) {
			throw new \Exception("Device not discovered with mac address: " . $macAddr);
		}
		return $this->flashByDevice($devObj, $fwPath, $scriptPath);
	}
	public function flashByDevice($devObj, $fwPath, $scriptPath=null)
	{
		$scriptFile	= null;
		//TODO: add check if the fw file matches the CPU arch, the npk holds the data starting around byte 12
		//also check the minimum version requirements
		$fwFile		= \MTM\FS\Factories::getFiles()->getFileFromPath($fwPath);
		if ($fwFile->getExists() === false) {
			throw new \Exception("Firmware file does not exist on path: " . $fwPath);
		} elseif ($scriptPath !== null) {
			$scriptFile	= \MTM\FS\Factories::getFiles()->getFileFromPath($scriptPath);
			if ($scriptFile->getExists() === false) {
				throw new \Exception("Script file does not exist on path: " . $scriptPath);
			}
		}
		$this->runflash($devObj, $fwFile, $scriptFile);
		return $this;
	}
	protected function runflash($devObj, $fwFile, $scriptFile)
	{
		$flashObj				= new \stdClass();
		$flashObj->dstMac		= $devObj->mac;
		$flashObj->srcMac		= $this->_txMacAddr;
		$flashObj->dstPos		= 0;
		$flashObj->srcPos		= 0;
		$flashObj->timeout		= 10000;
		$flashObj->retries		= 0;
		$flashObj->maxRetries	= 3;
		$flashObj->lastData		= null;

		$this->flashOffer($flashObj);
		$this->flashFormat($flashObj);
		$this->flashSpacer($flashObj);
		$this->flashFileHeader($flashObj, $fwFile);
		$this->flashFile($flashObj, $fwFile);
		
		if (is_object($scriptFile) === true) {
			$this->flashSpacer($flashObj);
			$this->flashFileHeader($flashObj, $scriptFile, "autorun.scr");
			$this->flashFile($flashObj, $scriptFile);
		}
		$this->flashSpacer($flashObj);
		$this->flashComplete($flashObj);

		$this->flashReboot($flashObj);
		return $this;
	}
	protected function flashOffer($flashObj)
	{
		try {
			
			$flashObj->dstPos	= 0;
			$flashObj->srcPos	= 1;
			
			$cmd				= array("O", "F", "F", "R", 10, 10);
			$data				= $this->arrayToHex($cmd);
			$this->flashWrite($flashObj, $data);
			
			$flashObj->dstPos	= 1;
			$respObj			= $this->flashWait($flashObj);

			$cmd				= array("Y", "A", "C", "K", 10);
			$okResp				= $this->arrayToHex($cmd);
			if ($okResp == $respObj->payload->hex) {
				$flashObj->retries	= 0;
				return;
			} else {
				throw new \Exception("Invalid Offer ACK");
			}
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				$flashObj->retries++;
				return $this->flashOffer($flashObj);
			} else {
				throw $e;
			}
		}
	}
	protected function flashFormat($flashObj)
	{
		try {
			
			if ($flashObj->retries > 0) {
				$flashObj->srcPos--;
				$flashObj->dstPos--;
			}
			$flashObj->srcPos++;
			//tell the routerboard to wipe its flash (i think that is what this position does)
			$data				= "";
			$this->flashWrite($flashObj, $data);
			$flashObj->dstPos++;

			//wait for return, this takes longer since the disk has to format
			//have observed this takes at least 8 sec on RB750Gr3
			$respObj			= $this->flashWait($flashObj, ($flashObj->timeout + 10000));
			
			$cmd				= array("S", "T", "R", "T");
			$okResp				= $this->arrayToHex($cmd);
			if ($okResp == $respObj->payload->hex) {
				$flashObj->retries	= 0;
				return;
			} else {
				throw new \Exception("Invalid Format Start return");
			}
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				$flashObj->retries++;
				return $this->flashFormat($flashObj);
			} else {
				throw $e;
			}
		}
	}
	protected function flashSpacer($flashObj)
	{
		try {
			
			if ($flashObj->retries > 0) {
				$flashObj->srcPos--;
				$flashObj->dstPos--;
			}
			$flashObj->srcPos++;
			
			$data				= "";
			$this->flashWrite($flashObj, $data);
			$flashObj->dstPos++;
			$respObj			= $this->flashWait($flashObj);
			
			$cmd				= array("R", "E", "T", "R");
			$okResp				= $this->arrayToHex($cmd);
			if ($okResp == $respObj->payload->hex) {
				$flashObj->retries	= 0;
				return;
			} else {
				throw new \Exception("Invalid Spacer Return");
			}
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				$flashObj->retries++;
				return $this->flashSpacer($flashObj);
			} else {
				throw $e;
			}
		}
	}
	protected function flashFileHeader($flashObj, $fileObj, $fileName=null)
	{
		//send the file header and size
		if ($fileName === null) {
			$fileName	= $fileObj->getName();
		}
		
		try {
			
			if ($flashObj->retries > 0) {
				$flashObj->srcPos--;
				$flashObj->dstPos--;
			}
			$flashObj->srcPos++;
			
			$cmd				= array("F", "I", "L", "E", 10);
			$cmd				= array_merge($cmd, str_split($fileName, 1));
			$cmd[]				= 10;
			$cmd				= array_merge($cmd, str_split($fileObj->getByteCount(), 1));
			$cmd[]				= 10;
			$data				= $this->arrayToHex($cmd);
			$this->flashWrite($flashObj, $data);
			$flashObj->dstPos++;
			$respObj			= $this->flashWait($flashObj);
			
			$cmd				= array("R", "E", "T", "R");
			$okResp				= $this->arrayToHex($cmd);
			if ($okResp == $respObj->payload->hex) {
				$flashObj->retries	= 0;
				return;
			} else {
				throw new \Exception("Invalid File Header Return");
			}
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				$flashObj->retries++;
				return $this->flashFileHeader($flashObj);
			} else {
				throw $e;
			}
		}
	}
	protected function flashFile($flashObj, $fileObj, $cPos=1)
	{
		//no retries on this function, if we dont make it there is no recovering
		//it takes too long to retrieve the response and re-try from the failed position
		//i have tried many different ways. So if doing flashing with high latency wrap
		//the UDP connection in a TCP based VPN to ensure delivery
		
		//if we require ZTS and spawn a seperate tread for reading it might be possible
		//or just use a language with native support for threads :)
		$maxPos		= $fileObj->getByteCount();
		while (true) {

			$flashObj->srcPos++;

			$cmd			= $fileObj->getBytes($this->_txMaxBytes, $cPos);
			$data		    = bin2hex($cmd);
			$this->flashWrite($flashObj, $data);
			
			$flashObj->dstPos++;
			$cPos			= $cPos + $this->_txMaxBytes;
			if ($cPos >= $maxPos) {
			
				try {

					$respObj			= $this->flashWait($flashObj);
					$cmd				= array("R", "E", "T", "R");
					$okResp				= $this->arrayToHex($cmd);
					if ($okResp == $respObj->payload->hex) {
						$flashObj->retries	= 0;
						return;
					} else {
						throw new \Exception("Invalid File Return");
					}

				} catch (\Exception $e) {
					throw $e;
				}
			
			} else {
				//wait for a bit before sending the next frame
				//this can be optimized, this is the main source of delay
				//the issue may be out of order errors
				usleep($this->_txDelay);
			}
		}
	}
	protected function flashComplete($flashObj)
	{
		try {
			
			if ($flashObj->retries > 0) {
				$flashObj->srcPos--;
				$flashObj->dstPos--;
			}
			$flashObj->srcPos++;
			
			$cmd				= array("F", "I", "L", "E", 10);
			$data				= $this->arrayToHex($cmd);
			$this->flashWrite($flashObj, $data);
			$flashObj->dstPos++;
			$respObj			= $this->flashWait($flashObj);
			
			$cmd				= array("W", "T", "R", "M");
			$okResp				= $this->arrayToHex($cmd);
			if ($okResp == $respObj->payload->hex) {
				$flashObj->retries	= 0;
				return;
			} else {
				throw new \Exception("Invalid Termination Return");
			}
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				$flashObj->retries++;
				return $this->flashComplete($flashObj);
			} else {
				throw $e;
			}
		}
	}
	protected function flashReboot($flashObj)
	{	
		try {
	
			if ($flashObj->retries > 0) {
				$flashObj->srcPos--;
				$flashObj->dstPos--;
			}
			$flashObj->srcPos++;
			
			$cmd				= array("T", "E", "R", "M", 10);
			$cmd				= array_merge($cmd, str_split("Installation successful", 1));
			$cmd[]				= 10;
			$data				= $this->arrayToHex($cmd);
			$this->flashWrite($flashObj, $data);
			$flashObj->dstPos++;
			
			//the real net install seems to get a return, but a packet capture does not seem to show it
			//on UDP:5000, maybe its using another protocol to establish if the unit is really down?
			return;
			
		} catch (\Exception $e) {
			if ($flashObj->retries < $flashObj->maxRetries) {
				return $this->flashReboot($flashObj);
			} else {
				throw $e;
			}
		}
	}
	
	private function flashWrite($flashObj, $hexData)
	{
		//craft transmission
		$data		= strtolower($flashObj->srcMac) . strtolower($flashObj->dstMac);
		
		//these 4 octets seem to be a delimitor
		$data		.= "0000";
		
		//set the payload size
		$data		.= $this->decCountToHex(strlen(hex2bin($hexData)));
		
		//set the tx position
		$data		.= $this->decCountToHex($flashObj->srcPos) . $this->decCountToHex($flashObj->dstPos);
		
		//now add the real payload
		$data		.= $hexData;
		
		//send
		$this->socketWrite(hex2bin($data));
		return $this;
	}
	private function flashWait($flashObj, $timeoutMs=null)
	{
		if ($timeoutMs === null) {
			$timeoutMs	= $flashObj->timeout;
		}
		
		$timeout	= $timeoutMs;
		$sTime	    = \MTM\Utilities\Factories::getTime()->getMicroEpoch();
		while (true) {
			
			try {
			
				$dataObj		= $this->socketRead($timeout);
				if (
					$dataObj->headers->srcMac == $flashObj->dstMac
					&& (
						$dataObj->headers->dstMac == $flashObj->srcMac
						|| $dataObj->headers->dstMac == "000000000000"
					)
				) {
					
					$flashObj->lastData	= $dataObj;
					if (
						$dataObj->headers->dstPos == $flashObj->srcPos
						&& $dataObj->headers->srcPos == $flashObj->dstPos
					) {
						return $dataObj;
					}
				}
			
			} catch (\Exception $e) {
				switch ($e->getCode()) {
					case 13465:
						//timeout reading
						throw new \Exception("Flash Wait Timed out");
					default:
						throw $e;
				}
			}
			
			$cTime	    = \MTM\Utilities\Factories::getTime()->getMicroEpoch();
			$timeout	= $timeoutMs - intval(($cTime - $sTime) * 1000);
			if ($timeout < 1) {
				throw new \Exception("Flash Wait Timeout");
			}
		}
	}
}

