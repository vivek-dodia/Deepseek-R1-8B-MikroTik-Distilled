# Repository Information
Name: ZabbixMikrotikSFPtemplate

# Directory Structure
Directory structure:
└── github_repos/ZabbixMikrotikSFPtemplate/
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
    │   │       ├── pack-0556c821ee4a91fd39847b04c9936f1ebb271100.idx
    │   │       └── pack-0556c821ee4a91fd39847b04c9936f1ebb271100.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── README.md
    └── zbx_templates.xml


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
	url = https://github.com/emaus/ZabbixMikrotikSFPtemplate.git
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
0000000000000000000000000000000000000000 aaad2630b7d4c10667bad10033e87511a21c8fb2 vivek-dodia <vivek.dodia@icloud.com> 1738606425 -0500	clone: from https://github.com/emaus/ZabbixMikrotikSFPtemplate.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 aaad2630b7d4c10667bad10033e87511a21c8fb2 vivek-dodia <vivek.dodia@icloud.com> 1738606425 -0500	clone: from https://github.com/emaus/ZabbixMikrotikSFPtemplate.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 aaad2630b7d4c10667bad10033e87511a21c8fb2 vivek-dodia <vivek.dodia@icloud.com> 1738606425 -0500	clone: from https://github.com/emaus/ZabbixMikrotikSFPtemplate.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
aaad2630b7d4c10667bad10033e87511a21c8fb2 refs/remotes/origin/master


File: /.git\refs\heads\master
aaad2630b7d4c10667bad10033e87511a21c8fb2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /README.md
# Zabbix Mikrotik SFP DDM template
A simple template for taking readings from an SFP module by protocol SNMP<br>
The template was tested on Zabbix 4.2.1 SFP modul Mikrotik S-31DLC20D on Mikrotik CCR1009-7G-1C-PC
<img src="https://raw.githubusercontent.com/emaus/ZabbixMikrotikSFPtemplate/master/chart2%20(1).png">


File: /zbx_templates.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>4.2</version>
    <date>2019-05-08T10:21:47Z</date>
    <groups>
        <group>
            <name>Templates/Network devices</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Net Mikrotik SNMPv2</template>
            <name>Template Net Mikrotik SNMPv2</name>
            <description>Template Net Mikrotik version: 0.15&#13;
MIBs used:&#13;
HOST-RESOURCES-MIB&#13;
MIKROTIK-MIB&#13;
Known Issues:&#13;
description : Doesn't have ifHighSpeed filled. fixed in more recent versions&#13;
version : RotuerOS 6.28 or lower&#13;
device : &#13;
description : Doesn't have any temperature sensors&#13;
version : RotuerOS 6.38.5&#13;
device : Mikrotik 941-2nD, Mikrotik 951G-2HnD</description>
            <groups>
                <group>
                    <name>Templates/Network devices</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>CPU</name>
                </application>
                <application>
                    <name>Inventory</name>
                </application>
                <application>
                    <name>Memory</name>
                </application>
                <application>
                    <name>Storage</name>
                </application>
                <application>
                    <name>Temperature</name>
                </application>
            </applications>
            <items>
                <item>
                    <name>Device: Temperature</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.4.1.14988.1.1.3.10.0</snmp_oid>
                    <key>sensor.temp.value[mtxrHlTemperature]</key>
                    <delay>3m</delay>
                    <history>30d</history>
                    <trends>365d</trends>
                    <status>0</status>
                    <value_type>0</value_type>
                    <allowed_hosts/>
                    <units>°C</units>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: MIKROTIK-MIB&#13;
(mtxrHlTemperature) Device temperature in Celsius (degrees C). Might be missing in entry models (RB750, RB450G..)&#13;
Reference: http://wiki.mikrotik.com/wiki/Manual:SNMP</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Temperature</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing>
                        <step>
                            <type>1</type>
                            <params>0.1</params>
                            <error_handler>0</error_handler>
                            <error_handler_params/>
                        </step>
                    </preprocessing>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Firmware version</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.4.1.14988.1.1.7.4.0</snmp_oid>
                    <key>system.hw.firmware</key>
                    <delay>1h</delay>
                    <history>2w</history>
                    <trends>0</trends>
                    <status>0</status>
                    <value_type>1</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: MIKROTIK-MIB&#13;
Current firmware version</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Inventory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Hardware model name</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.2.1.1.1.0</snmp_oid>
                    <key>system.hw.model</key>
                    <delay>1h</delay>
                    <history>2w</history>
                    <trends>0</trends>
                    <status>0</status>
                    <value_type>1</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>29</inventory_link>
                    <applications>
                        <application>
                            <name>Inventory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Hardware serial number</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.4.1.14988.1.1.7.3.0</snmp_oid>
                    <key>system.hw.serialnumber</key>
                    <delay>1h</delay>
                    <history>2w</history>
                    <trends>0</trends>
                    <status>0</status>
                    <value_type>1</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: MIKROTIK-MIB&#13;
RouterBOARD serial number</description>
                    <inventory_link>8</inventory_link>
                    <applications>
                        <application>
                            <name>Inventory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Operating system</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.4.1.14988.1.1.4.4.0</snmp_oid>
                    <key>system.sw.os</key>
                    <delay>1h</delay>
                    <history>2w</history>
                    <trends>0</trends>
                    <status>0</status>
                    <value_type>1</value_type>
                    <allowed_hosts/>
                    <units/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: MIKROTIK-MIB&#13;
Software version</description>
                    <inventory_link>5</inventory_link>
                    <applications>
                        <application>
                            <name>Inventory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Memory utilization</name>
                    <type>15</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>vm.memory.pused[memoryUsedPercentage.Memory]</key>
                    <delay>3m</delay>
                    <history>30d</history>
                    <trends>365d</trends>
                    <status>0</status>
                    <value_type>0</value_type>
                    <allowed_hosts/>
                    <units>%</units>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params>(last(vm.memory.used[hrStorageUsed.Memory])/last(vm.memory.total[hrStorageSize.Memory]))*100</params>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>Memory utilization in %</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Memory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Total memory</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.2.1.25.2.3.1.5.65536</snmp_oid>
                    <key>vm.memory.total[hrStorageSize.Memory]</key>
                    <delay>3m</delay>
                    <history>30d</history>
                    <trends>365d</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units>B</units>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: HOST-RESOURCES-MIB&#13;
The size of the storage represented by this entry, in&#13;
units of hrStorageAllocationUnits. This object is&#13;
writable to allow remote configuration of the size of&#13;
the storage area in those cases where such an&#13;
operation makes sense and is possible on the&#13;
underlying system. For example, the amount of main&#13;
memory allocated to a buffer pool might be modified or&#13;
the amount of disk space allocated to virtual memory&#13;
might be modified.</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Memory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing>
                        <step>
                            <type>1</type>
                            <params>1024</params>
                            <error_handler>0</error_handler>
                            <error_handler_params/>
                        </step>
                    </preprocessing>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
                <item>
                    <name>Used memory</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>1.3.6.1.2.1.25.2.3.1.6.65536</snmp_oid>
                    <key>vm.memory.used[hrStorageUsed.Memory]</key>
                    <delay>3m</delay>
                    <history>30d</history>
                    <trends>365d</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units>B</units>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>MIB: HOST-RESOURCES-MIB&#13;
The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Memory</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                    <preprocessing>
                        <step>
                            <type>1</type>
                            <params>1024</params>
                            <error_handler>0</error_handler>
                            <error_handler_params/>
                        </step>
                    </preprocessing>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <output_format>0</output_format>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <master_item/>
                </item>
            </items>
            <discovery_rules>
                <discovery_rule>
                    <name>CPU Discovery</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>discovery[{#SNMPVALUE},1.3.6.1.2.1.25.3.3.1.1]</snmp_oid>
                    <key>hrProcessorLoad.discovery</key>
                    <delay>1h</delay>
                    <status>0</status>
                    <allowed_hosts/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>30d</lifetime>
                    <description>HOST-RESOURCES-MIB::hrProcessorTable discovery</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>#{#SNMPINDEX}: CPU utilization</name>
                            <type>4</type>
                            <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                            <snmp_oid>1.3.6.1.2.1.25.3.3.1.2.{#SNMPINDEX}</snmp_oid>
                            <key>system.cpu.util[hrProcessorLoad.{#SNMPINDEX}]</key>
                            <delay>3m</delay>
                            <history>30d</history>
                            <trends>365d</trends>
                            <status>0</status>
                            <value_type>0</value_type>
                            <allowed_hosts/>
                            <units>%</units>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <params/>
                            <ipmi_sensor/>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>MIB: HOST-RESOURCES-MIB&#13;
The average, over the last minute, of the percentage of time that this processor was not idle.Implementations may approximate this one minute smoothing period if necessary.</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>CPU</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <preprocessing/>
                            <jmx_endpoint/>
                            <timeout>3s</timeout>
                            <url/>
                            <query_fields/>
                            <posts/>
                            <status_codes>200</status_codes>
                            <follow_redirects>1</follow_redirects>
                            <post_type>0</post_type>
                            <http_proxy/>
                            <headers/>
                            <retrieve_mode>0</retrieve_mode>
                            <request_method>0</request_method>
                            <output_format>0</output_format>
                            <allow_traps>0</allow_traps>
                            <ssl_cert_file/>
                            <ssl_key_file/>
                            <ssl_key_password/>
                            <verify_peer>0</verify_peer>
                            <verify_host>0</verify_host>
                            <application_prototypes/>
                            <master_item/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].avg(5m)}&gt;{$CPU_UTIL_MAX}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>#{#SNMPINDEX}: High CPU utilization</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>3</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                    </trigger_prototypes>
                    <graph_prototypes>
                        <graph_prototype>
                            <name>#{#SNMPINDEX}: CPU utilization</name>
                            <width>900</width>
                            <height>200</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>1</ymin_type_1>
                            <ymax_type_1>1</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>1A7C11</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Net Mikrotik SNMPv2</host>
                                        <key>system.cpu.util[hrProcessorLoad.{#SNMPINDEX}]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                    </graph_prototypes>
                    <host_prototypes/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <lld_macro_paths/>
                    <preprocessing/>
                    <master_item/>
                </discovery_rule>
                <discovery_rule>
                    <name>Temperature Discovery CPU</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>discovery[{#SNMPVALUE},1.3.6.1.4.1.14988.1.1.3.11]</snmp_oid>
                    <key>mtxrHlProcessorTemperature.discovery</key>
                    <delay>1h</delay>
                    <status>0</status>
                    <allowed_hosts/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>30d</lifetime>
                    <description>MIKROTIK-MIB::mtxrHlProcessorTemperature&#13;
Since temperature of CPU is not available on all Mikrotik hardware, this is done to avoid unsupported items.</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>CPU: Temperature</name>
                            <type>4</type>
                            <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                            <snmp_oid>1.3.6.1.4.1.14988.1.1.3.11.{#SNMPINDEX}</snmp_oid>
                            <key>sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}]</key>
                            <delay>3m</delay>
                            <history>30d</history>
                            <trends>365d</trends>
                            <status>0</status>
                            <value_type>0</value_type>
                            <allowed_hosts/>
                            <units>°C</units>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <params/>
                            <ipmi_sensor/>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>MIB: MIKROTIK-MIB&#13;
(mtxrHlProcessorTemperature) Processor temperature in Celsius (degrees C). Might be missing in entry models (RB750, RB450G..)</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Temperature</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <preprocessing>
                                <step>
                                    <type>1</type>
                                    <params>0.1</params>
                                    <error_handler>0</error_handler>
                                    <error_handler_params/>
                                </step>
                            </preprocessing>
                            <jmx_endpoint/>
                            <timeout>3s</timeout>
                            <url/>
                            <query_fields/>
                            <posts/>
                            <status_codes>200</status_codes>
                            <follow_redirects>1</follow_redirects>
                            <post_type>0</post_type>
                            <http_proxy/>
                            <headers/>
                            <retrieve_mode>0</retrieve_mode>
                            <request_method>0</request_method>
                            <output_format>0</output_format>
                            <allow_traps>0</allow_traps>
                            <ssl_cert_file/>
                            <ssl_key_file/>
                            <ssl_key_password/>
                            <verify_peer>0</verify_peer>
                            <verify_host>0</verify_host>
                            <application_prototypes/>
                            <master_item/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_CRIT:&quot;CPU&quot;}</expression>
                            <recovery_mode>1</recovery_mode>
                            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_CRIT:&quot;CPU&quot;}-3</recovery_expression>
                            <name>CPU: Temperature is above critical threshold: &gt;{$TEMP_CRIT:&quot;CPU&quot;}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>4</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.&#13;
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_WARN:&quot;CPU&quot;}</expression>
                            <recovery_mode>1</recovery_mode>
                            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_WARN:&quot;CPU&quot;}-3</recovery_expression>
                            <name>CPU: Temperature is above warning threshold: &gt;{$TEMP_WARN:&quot;CPU&quot;}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>2</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.&#13;
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies>
                                <dependency>
                                    <name>CPU: Temperature is above critical threshold: &gt;{$TEMP_CRIT:&quot;CPU&quot;}</name>
                                    <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_CRIT:&quot;CPU&quot;}</expression>
                                    <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_CRIT:&quot;CPU&quot;}-3</recovery_expression>
                                </dependency>
                            </dependencies>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&lt;{$TEMP_CRIT_LOW:&quot;CPU&quot;}</expression>
                            <recovery_mode>1</recovery_mode>
                            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].min(5m)}&gt;{$TEMP_CRIT_LOW:&quot;CPU&quot;}+3</recovery_expression>
                            <name>CPU: Temperature is too low: &lt;{$TEMP_CRIT_LOW:&quot;CPU&quot;}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>3</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                    </trigger_prototypes>
                    <graph_prototypes/>
                    <host_prototypes/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <lld_macro_paths/>
                    <preprocessing/>
                    <master_item/>
                </discovery_rule>
                <discovery_rule>
                    <name>Storage Discovery</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <snmp_oid>discovery[{#SNMPVALUE},1.3.6.1.2.1.25.2.3.1.3,{#ALLOC_UNITS},1.3.6.1.2.1.25.2.3.1.4,{#STORAGE_TYPE},1.3.6.1.2.1.25.2.3.1.2]</snmp_oid>
                    <key>storage.discovery</key>
                    <delay>1h</delay>
                    <status>0</status>
                    <allowed_hosts/>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>2</evaltype>
                        <formula/>
                        <conditions>
                            <condition>
                                <macro>{#STORAGE_TYPE}</macro>
                                <value>.+4$</value>
                                <operator>8</operator>
                                <formulaid>A</formulaid>
                            </condition>
                            <condition>
                                <macro>{#STORAGE_TYPE}</macro>
                                <value>.+hrStorageFixedDisk</value>
                                <operator>8</operator>
                                <formulaid>B</formulaid>
                            </condition>
                        </conditions>
                    </filter>
                    <lifetime>30d</lifetime>
                    <description>HOST-RESOURCES-MIB::hrStorage discovery with storage filter</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>Disk-{#SNMPINDEX}: Storage utilization</name>
                            <type>15</type>
                            <snmp_community/>
                            <snmp_oid/>
                            <key>vfs.fs.pused[hrStorageSize.{#SNMPINDEX}]</key>
                            <delay>5m</delay>
                            <history>30d</history>
                            <trends>365d</trends>
                            <status>0</status>
                            <value_type>0</value_type>
                            <allowed_hosts/>
                            <units>%</units>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <params>(last(vfs.fs.used[hrStorageSize.{#SNMPINDEX}])/last(vfs.fs.total[hrStorageSize.{#SNMPINDEX}]))*100</params>
                            <ipmi_sensor/>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Storage utilization in % for Disk-{#SNMPINDEX}</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Storage</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <preprocessing/>
                            <jmx_endpoint/>
                            <timeout>3s</timeout>
                            <url/>
                            <query_fields/>
                            <posts/>
                            <status_codes>200</status_codes>
                            <follow_redirects>1</follow_redirects>
                            <post_type>0</post_type>
                            <http_proxy/>
                            <headers/>
                            <retrieve_mode>0</retrieve_mode>
                            <request_method>0</request_method>
                            <output_format>0</output_format>
                            <allow_traps>0</allow_traps>
                            <ssl_cert_file/>
                            <ssl_key_file/>
                            <ssl_key_password/>
                            <verify_peer>0</verify_peer>
                            <verify_host>0</verify_host>
                            <application_prototypes/>
                            <master_item/>
                        </item_prototype>
                        <item_prototype>
                            <name>Disk-{#SNMPINDEX}: Total space</name>
                            <type>4</type>
                            <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                            <snmp_oid>1.3.6.1.2.1.25.2.3.1.5.{#SNMPINDEX}</snmp_oid>
                            <key>vfs.fs.total[hrStorageSize.{#SNMPINDEX}]</key>
                            <delay>5m</delay>
                            <history>30d</history>
                            <trends>365d</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts/>
                            <units>B</units>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <params/>
                            <ipmi_sensor/>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>MIB: HOST-RESOURCES-MIB&#13;
The size of the storage represented by this entry, in&#13;
units of hrStorageAllocationUnits. This object is&#13;
writable to allow remote configuration of the size of&#13;
the storage area in those cases where such an&#13;
operation makes sense and is possible on the&#13;
underlying system. For example, the amount of main&#13;
memory allocated to a buffer pool might be modified or&#13;
the amount of disk space allocated to virtual memory&#13;
might be modified.</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Storage</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <preprocessing>
                                <step>
                                    <type>1</type>
                                    <params>1024</params>
                                    <error_handler>0</error_handler>
                                    <error_handler_params/>
                                </step>
                            </preprocessing>
                            <jmx_endpoint/>
                            <timeout>3s</timeout>
                            <url/>
                            <query_fields/>
                            <posts/>
                            <status_codes>200</status_codes>
                            <follow_redirects>1</follow_redirects>
                            <post_type>0</post_type>
                            <http_proxy/>
                            <headers/>
                            <retrieve_mode>0</retrieve_mode>
                            <request_method>0</request_method>
                            <output_format>0</output_format>
                            <allow_traps>0</allow_traps>
                            <ssl_cert_file/>
                            <ssl_key_file/>
                            <ssl_key_password/>
                            <verify_peer>0</verify_peer>
                            <verify_host>0</verify_host>
                            <application_prototypes/>
                            <master_item/>
                        </item_prototype>
                        <item_prototype>
                            <name>Disk-{#SNMPINDEX}: Used space</name>
                            <type>4</type>
                            <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                            <snmp_oid>1.3.6.1.2.1.25.2.3.1.6.{#SNMPINDEX}</snmp_oid>
                            <key>vfs.fs.used[hrStorageSize.{#SNMPINDEX}]</key>
                            <delay>5m</delay>
                            <history>30d</history>
                            <trends>365d</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts/>
                            <units>B</units>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <params/>
                            <ipmi_sensor/>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>MIB: HOST-RESOURCES-MIB&#13;
The amount of the storage represented by this entry that is allocated, in units of hrStorageAllocationUnits.</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Storage</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <preprocessing>
                                <step>
                                    <type>1</type>
                                    <params>1024</params>
                                    <error_handler>0</error_handler>
                                    <error_handler_params/>
                                </step>
                            </preprocessing>
                            <jmx_endpoint/>
                            <timeout>3s</timeout>
                            <url/>
                            <query_fields/>
                            <posts/>
                            <status_codes>200</status_codes>
                            <follow_redirects>1</follow_redirects>
                            <post_type>0</post_type>
                            <http_proxy/>
                            <headers/>
                            <retrieve_mode>0</retrieve_mode>
                            <request_method>0</request_method>
                            <output_format>0</output_format>
                            <allow_traps>0</allow_traps>
                            <ssl_cert_file/>
                            <ssl_key_file/>
                            <ssl_key_password/>
                            <verify_peer>0</verify_peer>
                            <verify_host>0</verify_host>
                            <application_prototypes/>
                            <master_item/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_CRIT}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>Disk-{#SNMPINDEX}: Disk space is critically low</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>3</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_WARN}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>Disk-{#SNMPINDEX}: Disk space is low</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>2</priority>
                            <description>Last value: {ITEM.LASTVALUE1}.</description>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies>
                                <dependency>
                                    <name>Disk-{#SNMPINDEX}: Disk space is critically low</name>
                                    <expression>{Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_CRIT}</expression>
                                    <recovery_expression/>
                                </dependency>
                            </dependencies>
                            <tags/>
                        </trigger_prototype>
                    </trigger_prototypes>
                    <graph_prototypes/>
                    <host_prototypes/>
                    <jmx_endpoint/>
                    <timeout>3s</timeout>
                    <url/>
                    <query_fields/>
                    <posts/>
                    <status_codes>200</status_codes>
                    <follow_redirects>1</follow_redirects>
                    <post_type>0</post_type>
                    <http_proxy/>
                    <headers/>
                    <retrieve_mode>0</retrieve_mode>
                    <request_method>0</request_method>
                    <allow_traps>0</allow_traps>
                    <ssl_cert_file/>
                    <ssl_key_file/>
                    <ssl_key_password/>
                    <verify_peer>0</verify_peer>
                    <verify_host>0</verify_host>
                    <lld_macro_paths/>
                    <preprocessing/>
                    <master_item/>
                </discovery_rule>
            </discovery_rules>
            <httptests/>
            <macros>
                <macro>
                    <macro>{$CPU_UTIL_MAX}</macro>
                    <value>90</value>
                </macro>
                <macro>
                    <macro>{$MEMORY_UTIL_MAX}</macro>
                    <value>90</value>
                </macro>
                <macro>
                    <macro>{$STORAGE_UTIL_CRIT}</macro>
                    <value>90</value>
                </macro>
                <macro>
                    <macro>{$STORAGE_UTIL_WARN}</macro>
                    <value>80</value>
                </macro>
                <macro>
                    <macro>{$TEMP_CRIT}</macro>
                    <value>60</value>
                </macro>
                <macro>
                    <macro>{$TEMP_CRIT:&quot;CPU&quot;}</macro>
                    <value>75</value>
                </macro>
                <macro>
                    <macro>{$TEMP_CRIT_LOW}</macro>
                    <value>5</value>
                </macro>
                <macro>
                    <macro>{$TEMP_WARN}</macro>
                    <value>50</value>
                </macro>
                <macro>
                    <macro>{$TEMP_WARN:&quot;CPU&quot;}</macro>
                    <value>70</value>
                </macro>
            </macros>
            <templates>
                <template>
                    <name>Template Module Generic SNMPv2</name>
                </template>
                <template>
                    <name>Template Module Interfaces SNMPv2</name>
                </template>
            </templates>
            <screens/>
            <tags/>
        </template>
    </templates>
    <triggers>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_CRIT:&quot;Device&quot;}</expression>
            <recovery_mode>1</recovery_mode>
            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_CRIT:&quot;Device&quot;}-3</recovery_expression>
            <name>Device: Temperature is above critical threshold: &gt;{$TEMP_CRIT:&quot;Device&quot;}</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>4</priority>
            <description>Last value: {ITEM.LASTVALUE1}.&#13;
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
            <type>0</type>
            <manual_close>0</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_WARN:&quot;Device&quot;}</expression>
            <recovery_mode>1</recovery_mode>
            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_WARN:&quot;Device&quot;}-3</recovery_expression>
            <name>Device: Temperature is above warning threshold: &gt;{$TEMP_WARN:&quot;Device&quot;}</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>2</priority>
            <description>Last value: {ITEM.LASTVALUE1}.&#13;
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
            <type>0</type>
            <manual_close>0</manual_close>
            <dependencies>
                <dependency>
                    <name>Device: Temperature is above critical threshold: &gt;{$TEMP_CRIT:&quot;Device&quot;}</name>
                    <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_CRIT:&quot;Device&quot;}</expression>
                    <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_CRIT:&quot;Device&quot;}-3</recovery_expression>
                </dependency>
            </dependencies>
            <tags/>
        </trigger>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&lt;{$TEMP_CRIT_LOW:&quot;Device&quot;}</expression>
            <recovery_mode>1</recovery_mode>
            <recovery_expression>{Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].min(5m)}&gt;{$TEMP_CRIT_LOW:&quot;Device&quot;}+3</recovery_expression>
            <name>Device: Temperature is too low: &lt;{$TEMP_CRIT_LOW:&quot;Device&quot;}</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>3</priority>
            <description>Last value: {ITEM.LASTVALUE1}.</description>
            <type>0</type>
            <manual_close>0</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:system.hw.serialnumber.diff()}=1 and {Template Net Mikrotik SNMPv2:system.hw.serialnumber.strlen()}&gt;0</expression>
            <recovery_mode>2</recovery_mode>
            <recovery_expression/>
            <name>Device has been replaced (new serial number received)</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>1</priority>
            <description>Last value: {ITEM.LASTVALUE1}.&#13;
Device serial number has changed. Ack to close</description>
            <type>0</type>
            <manual_close>1</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:system.hw.firmware.diff()}=1 and {Template Net Mikrotik SNMPv2:system.hw.firmware.strlen()}&gt;0</expression>
            <recovery_mode>2</recovery_mode>
            <recovery_expression/>
            <name>Firmware has changed</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>1</priority>
            <description>Last value: {ITEM.LASTVALUE1}.&#13;
Firmware version has changed. Ack to close</description>
            <type>0</type>
            <manual_close>1</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
        <trigger>
            <expression>{Template Net Mikrotik SNMPv2:vm.memory.pused[memoryUsedPercentage.Memory].avg(5m)}&gt;{$MEMORY_UTIL_MAX}</expression>
            <recovery_mode>0</recovery_mode>
            <recovery_expression/>
            <name>High memory utilization</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>3</priority>
            <description>Last value: {ITEM.LASTVALUE1}.</description>
            <type>0</type>
            <manual_close>0</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
    </triggers>
    <graphs>
        <graph>
            <name>Memory utilization</name>
            <width>900</width>
            <height>200</height>
            <yaxismin>0.0000</yaxismin>
            <yaxismax>100.0000</yaxismax>
            <show_work_period>1</show_work_period>
            <show_triggers>1</show_triggers>
            <type>0</type>
            <show_legend>1</show_legend>
            <show_3d>0</show_3d>
            <percent_left>0.0000</percent_left>
            <percent_right>0.0000</percent_right>
            <ymin_type_1>1</ymin_type_1>
            <ymax_type_1>1</ymax_type_1>
            <ymin_item_1>0</ymin_item_1>
            <ymax_item_1>0</ymax_item_1>
            <graph_items>
                <graph_item>
                    <sortorder>0</sortorder>
                    <drawtype>5</drawtype>
                    <color>1A7C11</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template Net Mikrotik SNMPv2</host>
                        <key>vm.memory.pused[memoryUsedPercentage.Memory]</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>
    </graphs>
</zabbix_export>


