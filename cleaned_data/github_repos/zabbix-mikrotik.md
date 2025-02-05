# Repository Information
Name: zabbix-mikrotik

# Directory Structure
Directory structure:
└── github_repos/zabbix-mikrotik/
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
    │   │       ├── pack-548de6109418d50d8a0af190595b199798b576a5.idx
    │   │       └── pack-548de6109418d50d8a0af190595b199798b576a5.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── Advanced_Template_Module_Interfaces_SNMPv2.xml
    ├── Advanced_Template_Net_Mikrotik_SNMPv2.xml
    ├── graph_for_module_icmp_ping.xml
    ├── README.md
    └── regexp/


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
	url = https://github.com/XaTTa6bl4/zabbix-mikrotik.git
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
0000000000000000000000000000000000000000 2b787f7b4222c4bb7ee0f3d480450032e8123662 vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/XaTTa6bl4/zabbix-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 2b787f7b4222c4bb7ee0f3d480450032e8123662 vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/XaTTa6bl4/zabbix-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 2b787f7b4222c4bb7ee0f3d480450032e8123662 vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/XaTTa6bl4/zabbix-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
2b787f7b4222c4bb7ee0f3d480450032e8123662 refs/remotes/origin/master


File: /.git\refs\heads\master
2b787f7b4222c4bb7ee0f3d480450032e8123662


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
File: /Advanced_Template_Module_Interfaces_SNMPv2.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
   <version>3.4</version>
   <date>2015-12-30T14:41:30Z</date>
   <groups>
      <group>
         <name>Templates/Modules</name>
      </group>
   </groups>
   <templates>
      <template>
         <template>Advanced Template Module Interfaces SNMPv2</template>
         <name>Advanced Template Module Interfaces SNMPv2</name>
         <description>Link: https://github.com/XaTTa6bl4/zabbix-mikrotik

Based on Zabbix 3.4.5 official Template Interfaces version: 0.15
(https://share.zabbix.com/official-templates)
MIBs used:
IF-MIB</description>
         <groups>
            <group>
               <name>Templates/Modules</name>
            </group>
         </groups>
         <applications>
            <application>
               <name>Network Interfaces</name>
            </application>
         </applications>
         <items/>
         <discovery_rules>
            <discovery_rule>
               <name>Network Interfaces Discovery</name>
               <type>4</type>
               <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
               <snmp_oid>discovery[{#IFOPERSTATUS},1.3.6.1.2.1.2.2.1.8,{#IFADMINSTATUS},1.3.6.1.2.1.2.2.1.7,{#IFALIAS},1.3.6.1.2.1.31.1.1.1.18,{#IFNAME},1.3.6.1.2.1.31.1.1.1.1,{#IFDESCR},1.3.6.1.2.1.2.2.1.2,{#IFTYPE},1.3.6.1.2.1.2.2.1.3]</snmp_oid>
               <key>net.if.discovery</key>
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
                  <evaltype>1</evaltype>
                  <formula/>
                  <conditions>
                     <condition>
                        <macro>{#IFADMINSTATUS}</macro>
                        <value>(1|3)</value>
                        <!--  ignore interfaces with admin status of down(2) -->
                        <operator>8</operator>
                        <formulaid>B</formulaid>
                        <!-- (1-up, 2-down, 3-testing, 4-unknown, 5-dormant, 6-notPresent, 7-lowerLayerDown)-->
                     </condition>
                     <condition>
                        <macro>{#IFOPERSTATUS}</macro>
                        <value>(1|2|3|4|5|7)</value>
                        <!--  ignore notPresent(6) -->
                        <operator>8</operator>
                        <formulaid>C</formulaid>
                     </condition>
                     <condition>
                        <macro>{#IFNAME}</macro>
                        <value>@Network interfaces for discovery</value>
                        <!-- should filter out loopbacks and nulls -->
                        <operator>8</operator>
                        <formulaid>B</formulaid>
                     </condition>
                  </conditions>
               </filter>
               <lifetime>30d</lifetime>
               <description>Discovering interfaces from IF-MIB. Interfaces are not discovered:
- with down(2) Administrative status
- with notPresent(6) Operational status
- loopbacks</description>
               <item_prototypes>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Operational status</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.8.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.status[ifOperStatus.{#SNMPINDEX}]</key>
                     <delay>1m</delay>
                     <history>2w</history>
                     <trends>0d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
The current operational state of the interface.
- The testing(3) state indicates that no operational packet scan be passed
- If ifAdminStatus is down(2) then ifOperStatus should be down(2)
- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic
- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)
- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state
- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap>
                        <name>IF-MIB::ifOperStatus</name>
                     </valuemap>
                     <logtimefmt/>
                     <preprocessing/>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Bits received</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.31.1.1.1.6.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.in[ifHCInOctets.{#SNMPINDEX}]</key>
                     <delay>3m</delay>
                     <history>30d</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
                     <allowed_hosts/>
                     <units>bps</units>
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
                     <description>MIB: IF-MIB
The total number of octets received on the interface,including framing characters.  This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                        <step>
                           <type>1</type>
                           <params>8</params>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Bits sent</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.31.1.1.1.10.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.out[ifHCOutOctets.{#SNMPINDEX}]</key>
                     <delay>3m</delay>
                     <history>30d</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
                     <allowed_hosts/>
                     <units>bps</units>
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
                     <description>MIB: IF-MIB
The total number of octets transmitted out of the interface, including framing characters.  This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                        <step>
                           <type>1</type>
                           <params>8</params>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.14.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.in.errors[ifInErrors.{#SNMPINDEX}]</key>
                     <delay>5m</delay>
                     <history>1w</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.20.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.out.errors[ifOutErrors.{#SNMPINDEX}]</key>
                     <delay>5m</delay>
                     <history>1w</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.19.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.out.discards[ifOutDiscards.{#SNMPINDEX}]</key>
                     <delay>5m</delay>
                     <history>1w</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
The number of outbound packets which were chosen to be discarded
even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.
One possible reason for discarding such a packet could be to free up buffer space.
Discontinuities in the value of this counter can occur at re-initialization of the management system,
and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.13.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.in.discards[ifInDiscards.{#SNMPINDEX}]</key>
                     <delay>5m</delay>
                     <history>1w</history>
                     <trends>365d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
The number of inbound packets which were chosen to be discarded
even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.
One possible reason for discarding such a packet could be to free up buffer space.
Discontinuities in the value of this counter can occur at re-initialization of the management system,
and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>10</type>
                           <params/>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Interface type</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.2.2.1.3.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.type[ifType.{#SNMPINDEX}]</key>
                     <delay>1h</delay>
                     <history>1w</history>
                     <trends>0d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
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
                     <description>MIB: IF-MIB
The type of interface.
Additional values for ifType are assigned by the Internet Assigned NumbersAuthority (IANA),
through updating the syntax of the IANAifType textual convention.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap>
                        <name>IF-MIB::ifType</name>
                     </valuemap>
                     <logtimefmt/>
                     <preprocessing/>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                     <name>Interface {#IFNAME}({#IFALIAS}): Speed</name>
                     <type>4</type>
                     <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                     <snmp_oid>1.3.6.1.2.1.31.1.1.1.15.{#SNMPINDEX}</snmp_oid>
                     <key>net.if.speed[ifHighSpeed.{#SNMPINDEX}]</key>
                     <delay>5m</delay>
                     <history>1w</history>
                     <trends>0d</trends>
                     <status>0</status>
                     <value_type>3</value_type>
                     <allowed_hosts/>
                     <units>bps</units>
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
                     <description>MIB: IF-MIB
An estimate of the interface's current bandwidth in units of 1,000,000 bits per second.  If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.  For a sub-layer which has no concept of bandwidth, this object should be zero.</description>
                     <inventory_link>0</inventory_link>
                     <applications>
                        <application>
                           <name>Network Interfaces</name>
                        </application>
                     </applications>
                     <valuemap/>
                     <logtimefmt/>
                     <preprocessing>
                        <step>
                           <type>1</type>
                           <params>1000000</params>
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                      <name>Interface {#IFNAME}({#IFALIAS}): MAC address</name>
                      <type>4</type>
                      <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                      <snmp_oid>.1.3.6.1.2.1.2.2.1.6.{#SNMPINDEX}</snmp_oid>
                      <key>net.if.mac[ifMacAddr.{#SNMPINDEX}]</key>
                      <delay>3600</delay>
                      <history>1w</history>
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
                      <description>MIB: IF-MIB
The interface's address at the protocol layer immediately `below' the network layer in the protocol stack. For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length.</description>
                      <inventory_link>0</inventory_link>
                      <applications>
                          <application>
                              <name>Network Interfaces</name>
                          </application>
                      </applications>
                      <valuemap/>
                      <logtimefmt/>
                      <preprocessing/>
                      <jmx_endpoint/>
                      <application_prototypes/>
                      <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                      <name>Interface {#IFNAME}({#IFALIAS}): Inbound unicast packets</name>
                      <type>4</type>
                      <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                      <snmp_oid>.1.3.6.1.2.1.31.1.1.1.7.{#SNMPINDEX}</snmp_oid>
                      <key>net.if.in.ucast[ifInUcast.{#SNMPINDEX}]</key>
                      <delay>300</delay>
                      <history>1w</history>
                      <trends>365d</trends>
                      <status>0</status>
                      <value_type>3</value_type>
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
                      <description>MIB: IF-MIB
The number of packets, delivered by this sub-layer to a higher (sub-)layer, which were not addressed to a multicast or broadcast address at this sub-layer. This object is a 64-bit version of ifInUcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                      <inventory_link>0</inventory_link>
                      <applications>
                          <application>
                              <name>Network Interfaces</name>
                          </application>
                      </applications>
                      <valuemap/>
                      <logtimefmt/>
                      <preprocessing>
                          <step>
                              <type>10</type>
                              <params/>
                          </step>
                      </preprocessing>
                      <jmx_endpoint/>
                      <application_prototypes/>
                      <master_item_prototype/>
                  </item_prototype>
                  <item_prototype>
                      <name>Interface {#IFNAME}({#IFALIAS}): Outbound unicast packets</name>
                      <type>4</type>
                      <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                      <snmp_oid>.1.3.6.1.2.1.31.1.1.1.11.{#SNMPINDEX}</snmp_oid>
                      <key>net.if.out.ucast[ifOutUcast.{#SNMPINDEX}]</key>
                      <delay>300</delay>
                      <history>1w</history>
                      <trends>365d</trends>
                      <status>0</status>
                      <value_type>3</value_type>
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
                      <description>MIB: IF-MIB
The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent. This object is a 64-bit version of ifOutUcastPkts. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.</description>
                      <inventory_link>0</inventory_link>
                      <applications>
                          <application>
                              <name>Network Interfaces</name>
                          </application>
                      </applications>
                      <valuemap/>
                      <logtimefmt/>
                      <preprocessing>
                          <step>
                              <type>10</type>
                              <params/>
                          </step>
                      </preprocessing>
                      <jmx_endpoint/>
                      <application_prototypes/>
                      <master_item_prototype/>
                  </item_prototype>
               </item_prototypes>
               <trigger_prototypes>
                  <trigger_prototype>
                     <expression>{$IFCONTROL:"{#IFNAME}"}=1 and ({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}&lt;&gt;2</recovery_expression>
                     <name>Interface {#IFNAME}({#IFALIAS}): Link down</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>3</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.
Interface is down</description>
                     <type>0</type>
                     <manual_close>0</manual_close>
                     <dependencies/>
                     <tags/>
                  </trigger_prototype>
                  <trigger_prototype>
                     <expression>({Advanced Template Module Interfaces SNMPv2:net.if.in[ifHCInOctets.{#SNMPINDEX}].avg(15m)}&gt;({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()} or
{Advanced Template Module Interfaces SNMPv2:net.if.out[ifHCOutOctets.{#SNMPINDEX}].avg(15m)}&gt;({$IF_UTIL_MAX:"{#IFNAME}"}/100)*{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}) and
{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}&gt;0 and {Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=6</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.in[ifHCInOctets.{#SNMPINDEX}].avg(15m)}&lt;(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()} and
{Advanced Template Module Interfaces SNMPv2:net.if.out[ifHCOutOctets.{#SNMPINDEX}].avg(15m)}&lt;(({$IF_UTIL_MAX:"{#IFNAME}"}-3)/100)*{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}</recovery_expression>
                     <name>Interface {#IFNAME}({#IFALIAS}): High bandwidth usage &gt;{$IF_UTIL_MAX:"{#IFNAME}"}%</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>2</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.</description>
                     <type>0</type>
                     <manual_close>1</manual_close>
                     <dependencies>
                        <dependency>
                           <name>Interface {#IFNAME}({#IFALIAS}): Link down</name>
                           <expression>{$IFCONTROL:"{#IFNAME}"}=1 and ({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)</expression>
                           <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}&lt;&gt;2</recovery_expression>
                        </dependency>
                     </dependencies>
                     <tags/>
                  </trigger_prototype>
                  <trigger_prototype>
                     <expression>{Advanced Template Module Interfaces SNMPv2:net.if.in.errors[ifInErrors.{#SNMPINDEX}].avg(5m)}&gt;{$IF_ERRORS_WARN:"{#IFNAME}"}
or {Advanced Template Module Interfaces SNMPv2:net.if.out.errors[ifOutErrors.{#SNMPINDEX}].avg(5m)}&gt;{$IF_ERRORS_WARN:"{#IFNAME}"}</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.in.errors[ifInErrors.{#SNMPINDEX}].avg(5m)}&lt;{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8
and {Advanced Template Module Interfaces SNMPv2:net.if.out.errors[ifOutErrors.{#SNMPINDEX}].avg(5m)}&lt;{$IF_ERRORS_WARN:"{#IFNAME}"}*0.8</recovery_expression>
                     <name>Interface {#IFNAME}({#IFALIAS}): High error rate</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>2</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.
Recovers when below 80% of {$IF_ERRORS_WARN:"{#IFNAME}"} threshold</description>
                     <type>0</type>
                     <manual_close>1</manual_close>
                     <dependencies>
                        <dependency>
                           <name>Interface {#IFNAME}({#IFALIAS}): Link down</name>
                           <expression>{$IFCONTROL:"{#IFNAME}"}=1 and ({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)</expression>
                           <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}&lt;&gt;2</recovery_expression>
                        </dependency>
                     </dependencies>
                     <tags/>
                  </trigger_prototype>
                  <trigger_prototype>
                     <expression>{Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].change()}&lt;0 and {Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].last()}&gt;0
and (
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=6 or
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=7 or
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=11 or
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=62 or
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=69 or
{Advanced Template Module Interfaces SNMPv2:net.if.type[ifType.{#SNMPINDEX}].last()}=117
)
and
({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}&lt;&gt;2)
</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>({Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].change()}&gt;0 and {Advanced Template Module Interfaces SNMPv2:net.if.speed[ifHighSpeed.{#SNMPINDEX}].prev()}&gt;0) or
({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2)</recovery_expression>
                     <name>Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>1</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.
This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Ack to close.</description>
                     <type>0</type>
                     <manual_close>1</manual_close>
                     <dependencies>
                        <dependency>
                           <name>Interface {#IFNAME}({#IFALIAS}): Link down</name>
                           <expression>{$IFCONTROL:"{#IFNAME}"}=1 and ({Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}=2 and {Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].diff()}=1)</expression>
                           <recovery_expression>{Advanced Template Module Interfaces SNMPv2:net.if.status[ifOperStatus.{#SNMPINDEX}].last()}&lt;&gt;2</recovery_expression>
                        </dependency>
                     </dependencies>
                     <tags/>
                  </trigger_prototype>
               </trigger_prototypes>
               <graph_prototypes>
                   <graph_prototype>
                       <name>Interface {#IFNAME}({#IFALIAS}): Network traffic</name>
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
                       <ymin_type_1>0</ymin_type_1>
                       <ymax_type_1>0</ymax_type_1>
                       <ymin_item_1>0</ymin_item_1>
                       <ymax_item_1>0</ymax_item_1>
                       <graph_items>
                           <graph_item>
                               <sortorder>0</sortorder>
                               <drawtype>5</drawtype>
                               <color>00AA00</color>
                               <yaxisside>0</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.in[ifHCInOctets.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>1</sortorder>
                               <drawtype>5</drawtype>
                               <color>3333FF</color>
                               <yaxisside>0</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.out[ifHCOutOctets.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>2</sortorder>
                               <drawtype>2</drawtype>
                               <color>EEEE00</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.in.ucast[ifInUcast.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>3</sortorder>
                               <drawtype>2</drawtype>
                               <color>EE00EE</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.out.ucast[ifOutUcast.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>4</sortorder>
                               <drawtype>0</drawtype>
                               <color>F63100</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.out.errors[ifOutErrors.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>5</sortorder>
                               <drawtype>0</drawtype>
                               <color>A54F10</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.in.errors[ifInErrors.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>6</sortorder>
                               <drawtype>0</drawtype>
                               <color>FC6EA3</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.out.discards[ifOutDiscards.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                           <graph_item>
                               <sortorder>7</sortorder>
                               <drawtype>0</drawtype>
                               <color>6C59DC</color>
                               <yaxisside>1</yaxisside>
                               <calc_fnc>2</calc_fnc>
                               <type>0</type>
                               <item>
                                   <host>Advanced Template Module Interfaces SNMPv2</host>
                                   <key>net.if.in.discards[ifInDiscards.{#SNMPINDEX}]</key>
                               </item>
                           </graph_item>
                       </graph_items>
                   </graph_prototype>
               </graph_prototypes>
               <host_prototypes/>
               <jmx_endpoint/>
            </discovery_rule>
         </discovery_rules>
         <httptests/>
         <macros>
            <macro>
               <macro>{$IFCONTROL}</macro>
               <value>1</value>
            </macro>
            <macro>
               <macro>{$IF_UTIL_MAX}</macro>
               <value>90</value>
            </macro>
            <macro>
               <macro>{$IF_ERRORS_WARN}</macro>
               <value>2</value>
            </macro>
         </macros>
         <templates/>
         <screens/>
      </template>
   </templates>
   <graphs/>
   <triggers/>
   <value_maps>
      <value_map>
         <name>IF-MIB::ifOperStatus</name>
         <mappings>
            <mapping>
               <value>1</value>
               <newvalue>up</newvalue>
            </mapping>
            <mapping>
               <value>2</value>
               <newvalue>down</newvalue>
            </mapping>
            <mapping>
               <value>3</value>
               <newvalue>testing</newvalue>
            </mapping>
            <mapping>
               <value>4</value>
               <newvalue>unknown</newvalue>
            </mapping>
            <mapping>
               <value>5</value>
               <newvalue>dormant</newvalue>
            </mapping>
            <mapping>
               <value>6</value>
               <newvalue>notPresent</newvalue>
            </mapping>
            <mapping>
               <value>7</value>
               <newvalue>lowerLayerDown</newvalue>
            </mapping>
         </mappings>
      </value_map>
      <value_map>
         <name>IF-MIB::ifType</name>
         <!-- https://www.iana.org/assignments/ianaiftype-mib/ianaiftype-mib LAST-UPDATED "201703300000Z"  March 30, 2017 -->
         <mappings>
            <mapping>
               <value>1</value>
               <newvalue>other</newvalue>
            </mapping>
            <mapping>
               <value>2</value>
               <newvalue>regular1822</newvalue>
            </mapping>
            <mapping>
               <value>3</value>
               <newvalue>hdh1822</newvalue>
            </mapping>
            <mapping>
               <value>4</value>
               <newvalue>ddnX25</newvalue>
            </mapping>
            <mapping>
               <value>5</value>
               <newvalue>rfc877x25</newvalue>
            </mapping>
            <mapping>
               <value>6</value>
               <newvalue>ethernetCsmacd</newvalue>
            </mapping>
            <mapping>
               <value>7</value>
               <newvalue>iso88023Csmacd</newvalue>
            </mapping>
            <mapping>
               <value>8</value>
               <newvalue>iso88024TokenBus</newvalue>
            </mapping>
            <mapping>
               <value>9</value>
               <newvalue>iso88025TokenRing</newvalue>
            </mapping>
            <mapping>
               <value>10</value>
               <newvalue>iso88026Man</newvalue>
            </mapping>
            <mapping>
               <value>11</value>
               <newvalue>starLan</newvalue>
            </mapping>
            <mapping>
               <value>12</value>
               <newvalue>proteon10Mbit</newvalue>
            </mapping>
            <mapping>
               <value>13</value>
               <newvalue>proteon80Mbit</newvalue>
            </mapping>
            <mapping>
               <value>14</value>
               <newvalue>hyperchannel</newvalue>
            </mapping>
            <mapping>
               <value>15</value>
               <newvalue>fddi</newvalue>
            </mapping>
            <mapping>
               <value>16</value>
               <newvalue>lapb</newvalue>
            </mapping>
            <mapping>
               <value>17</value>
               <newvalue>sdlc</newvalue>
            </mapping>
            <mapping>
               <value>18</value>
               <newvalue>ds1</newvalue>
            </mapping>
            <mapping>
               <value>19</value>
               <newvalue>e1</newvalue>
            </mapping>
            <mapping>
               <value>20</value>
               <newvalue>basicISDN</newvalue>
            </mapping>
            <mapping>
               <value>21</value>
               <newvalue>primaryISDN</newvalue>
            </mapping>
            <mapping>
               <value>22</value>
               <newvalue>propPointToPointSerial</newvalue>
            </mapping>
            <mapping>
               <value>23</value>
               <newvalue>ppp</newvalue>
            </mapping>
            <mapping>
               <value>24</value>
               <newvalue>softwareLoopback</newvalue>
            </mapping>
            <mapping>
               <value>25</value>
               <newvalue>eon</newvalue>
            </mapping>
            <mapping>
               <value>26</value>
               <newvalue>ethernet3Mbit</newvalue>
            </mapping>
            <mapping>
               <value>27</value>
               <newvalue>nsip</newvalue>
            </mapping>
            <mapping>
               <value>28</value>
               <newvalue>slip</newvalue>
            </mapping>
            <mapping>
               <value>29</value>
               <newvalue>ultra</newvalue>
            </mapping>
            <mapping>
               <value>30</value>
               <newvalue>ds3</newvalue>
            </mapping>
            <mapping>
               <value>31</value>
               <newvalue>sip</newvalue>
            </mapping>
            <mapping>
               <value>32</value>
               <newvalue>frameRelay</newvalue>
            </mapping>
            <mapping>
               <value>33</value>
               <newvalue>rs232</newvalue>
            </mapping>
            <mapping>
               <value>34</value>
               <newvalue>para</newvalue>
            </mapping>
            <mapping>
               <value>35</value>
               <newvalue>arcnet</newvalue>
            </mapping>
            <mapping>
               <value>36</value>
               <newvalue>arcnetPlus</newvalue>
            </mapping>
            <mapping>
               <value>37</value>
               <newvalue>atm</newvalue>
            </mapping>
            <mapping>
               <value>38</value>
               <newvalue>miox25</newvalue>
            </mapping>
            <mapping>
               <value>39</value>
               <newvalue>sonet</newvalue>
            </mapping>
            <mapping>
               <value>40</value>
               <newvalue>x25ple</newvalue>
            </mapping>
            <mapping>
               <value>41</value>
               <newvalue>iso88022llc</newvalue>
            </mapping>
            <mapping>
               <value>42</value>
               <newvalue>localTalk</newvalue>
            </mapping>
            <mapping>
               <value>43</value>
               <newvalue>smdsDxi</newvalue>
            </mapping>
            <mapping>
               <value>44</value>
               <newvalue>frameRelayService</newvalue>
            </mapping>
            <mapping>
               <value>45</value>
               <newvalue>v35</newvalue>
            </mapping>
            <mapping>
               <value>46</value>
               <newvalue>hssi</newvalue>
            </mapping>
            <mapping>
               <value>47</value>
               <newvalue>hippi</newvalue>
            </mapping>
            <mapping>
               <value>48</value>
               <newvalue>modem</newvalue>
            </mapping>
            <mapping>
               <value>49</value>
               <newvalue>aal5</newvalue>
            </mapping>
            <mapping>
               <value>50</value>
               <newvalue>sonetPath</newvalue>
            </mapping>
            <mapping>
               <value>51</value>
               <newvalue>sonetVT</newvalue>
            </mapping>
            <mapping>
               <value>52</value>
               <newvalue>smdsIcip</newvalue>
            </mapping>
            <mapping>
               <value>53</value>
               <newvalue>propVirtual</newvalue>
            </mapping>
            <mapping>
               <value>54</value>
               <newvalue>propMultiplexor</newvalue>
            </mapping>
            <mapping>
               <value>55</value>
               <newvalue>ieee80212</newvalue>
            </mapping>
            <mapping>
               <value>56</value>
               <newvalue>fibreChannel</newvalue>
            </mapping>
            <mapping>
               <value>57</value>
               <newvalue>hippiInterface</newvalue>
            </mapping>
            <mapping>
               <value>58</value>
               <newvalue>frameRelayInterconnect</newvalue>
            </mapping>
            <mapping>
               <value>59</value>
               <newvalue>aflane8023</newvalue>
            </mapping>
            <mapping>
               <value>60</value>
               <newvalue>aflane8025</newvalue>
            </mapping>
            <mapping>
               <value>61</value>
               <newvalue>cctEmul</newvalue>
            </mapping>
            <mapping>
               <value>62</value>
               <newvalue>fastEther</newvalue>
            </mapping>
            <mapping>
               <value>63</value>
               <newvalue>isdn</newvalue>
            </mapping>
            <mapping>
               <value>64</value>
               <newvalue>v11</newvalue>
            </mapping>
            <mapping>
               <value>65</value>
               <newvalue>v36</newvalue>
            </mapping>
            <mapping>
               <value>66</value>
               <newvalue>g703at64k</newvalue>
            </mapping>
            <mapping>
               <value>67</value>
               <newvalue>g703at2mb</newvalue>
            </mapping>
            <mapping>
               <value>68</value>
               <newvalue>qllc</newvalue>
            </mapping>
            <mapping>
               <value>69</value>
               <newvalue>fastEtherFX</newvalue>
            </mapping>
            <mapping>
               <value>70</value>
               <newvalue>channel</newvalue>
            </mapping>
            <mapping>
               <value>71</value>
               <newvalue>ieee80211</newvalue>
            </mapping>
            <mapping>
               <value>72</value>
               <newvalue>ibm370parChan</newvalue>
            </mapping>
            <mapping>
               <value>73</value>
               <newvalue>escon</newvalue>
            </mapping>
            <mapping>
               <value>74</value>
               <newvalue>dlsw</newvalue>
            </mapping>
            <mapping>
               <value>75</value>
               <newvalue>isdns</newvalue>
            </mapping>
            <mapping>
               <value>76</value>
               <newvalue>isdnu</newvalue>
            </mapping>
            <mapping>
               <value>77</value>
               <newvalue>lapd</newvalue>
            </mapping>
            <mapping>
               <value>78</value>
               <newvalue>ipSwitch</newvalue>
            </mapping>
            <mapping>
               <value>79</value>
               <newvalue>rsrb</newvalue>
            </mapping>
            <mapping>
               <value>80</value>
               <newvalue>atmLogical</newvalue>
            </mapping>
            <mapping>
               <value>81</value>
               <newvalue>ds0</newvalue>
            </mapping>
            <mapping>
               <value>82</value>
               <newvalue>ds0Bundle</newvalue>
            </mapping>
            <mapping>
               <value>83</value>
               <newvalue>bsc</newvalue>
            </mapping>
            <mapping>
               <value>84</value>
               <newvalue>async</newvalue>
            </mapping>
            <mapping>
               <value>85</value>
               <newvalue>cnr</newvalue>
            </mapping>
            <mapping>
               <value>86</value>
               <newvalue>iso88025Dtr</newvalue>
            </mapping>
            <mapping>
               <value>87</value>
               <newvalue>eplrs</newvalue>
            </mapping>
            <mapping>
               <value>88</value>
               <newvalue>arap</newvalue>
            </mapping>
            <mapping>
               <value>89</value>
               <newvalue>propCnls</newvalue>
            </mapping>
            <mapping>
               <value>90</value>
               <newvalue>hostPad</newvalue>
            </mapping>
            <mapping>
               <value>91</value>
               <newvalue>termPad</newvalue>
            </mapping>
            <mapping>
               <value>92</value>
               <newvalue>frameRelayMPI</newvalue>
            </mapping>
            <mapping>
               <value>93</value>
               <newvalue>x213</newvalue>
            </mapping>
            <mapping>
               <value>94</value>
               <newvalue>adsl</newvalue>
            </mapping>
            <mapping>
               <value>95</value>
               <newvalue>radsl</newvalue>
            </mapping>
            <mapping>
               <value>96</value>
               <newvalue>sdsl</newvalue>
            </mapping>
            <mapping>
               <value>97</value>
               <newvalue>vdsl</newvalue>
            </mapping>
            <mapping>
               <value>98</value>
               <newvalue>iso88025CRFPInt</newvalue>
            </mapping>
            <mapping>
               <value>99</value>
               <newvalue>myrinet</newvalue>
            </mapping>
            <mapping>
               <value>100</value>
               <newvalue>voiceEM</newvalue>
            </mapping>
            <mapping>
               <value>101</value>
               <newvalue>voiceFXO</newvalue>
            </mapping>
            <mapping>
               <value>102</value>
               <newvalue>voiceFXS</newvalue>
            </mapping>
            <mapping>
               <value>103</value>
               <newvalue>voiceEncap</newvalue>
            </mapping>
            <mapping>
               <value>104</value>
               <newvalue>voiceOverIp</newvalue>
            </mapping>
            <mapping>
               <value>105</value>
               <newvalue>atmDxi</newvalue>
            </mapping>
            <mapping>
               <value>106</value>
               <newvalue>atmFuni</newvalue>
            </mapping>
            <mapping>
               <value>107</value>
               <newvalue>atmIma</newvalue>
            </mapping>
            <mapping>
               <value>108</value>
               <newvalue>pppMultilinkBundle</newvalue>
            </mapping>
            <mapping>
               <value>109</value>
               <newvalue>ipOverCdlc</newvalue>
            </mapping>
            <mapping>
               <value>110</value>
               <newvalue>ipOverClaw</newvalue>
            </mapping>
            <mapping>
               <value>111</value>
               <newvalue>stackToStack</newvalue>
            </mapping>
            <mapping>
               <value>112</value>
               <newvalue>virtualIpAddress</newvalue>
            </mapping>
            <mapping>
               <value>113</value>
               <newvalue>mpc</newvalue>
            </mapping>
            <mapping>
               <value>114</value>
               <newvalue>ipOverAtm</newvalue>
            </mapping>
            <mapping>
               <value>115</value>
               <newvalue>iso88025Fiber</newvalue>
            </mapping>
            <mapping>
               <value>116</value>
               <newvalue>tdlc</newvalue>
            </mapping>
            <mapping>
               <value>117</value>
               <newvalue>gigabitEthernet</newvalue>
            </mapping>
            <mapping>
               <value>118</value>
               <newvalue>hdlc</newvalue>
            </mapping>
            <mapping>
               <value>119</value>
               <newvalue>lapf</newvalue>
            </mapping>
            <mapping>
               <value>120</value>
               <newvalue>v37</newvalue>
            </mapping>
            <mapping>
               <value>121</value>
               <newvalue>x25mlp</newvalue>
            </mapping>
            <mapping>
               <value>122</value>
               <newvalue>x25huntGroup</newvalue>
            </mapping>
            <mapping>
               <value>123</value>
               <newvalue>trasnpHdlc</newvalue>
            </mapping>
            <mapping>
               <value>124</value>
               <newvalue>interleave</newvalue>
            </mapping>
            <mapping>
               <value>125</value>
               <newvalue>fast</newvalue>
            </mapping>
            <mapping>
               <value>126</value>
               <newvalue>ip</newvalue>
            </mapping>
            <mapping>
               <value>127</value>
               <newvalue>docsCableMaclayer</newvalue>
            </mapping>
            <mapping>
               <value>128</value>
               <newvalue>docsCableDownstream</newvalue>
            </mapping>
            <mapping>
               <value>129</value>
               <newvalue>docsCableUpstream</newvalue>
            </mapping>
            <mapping>
               <value>130</value>
               <newvalue>a12MppSwitch</newvalue>
            </mapping>
            <mapping>
               <value>131</value>
               <newvalue>tunnel</newvalue>
            </mapping>
            <mapping>
               <value>132</value>
               <newvalue>coffee</newvalue>
            </mapping>
            <mapping>
               <value>133</value>
               <newvalue>ces</newvalue>
            </mapping>
            <mapping>
               <value>134</value>
               <newvalue>atmSubInterface</newvalue>
            </mapping>
            <mapping>
               <value>135</value>
               <newvalue>l2vlan</newvalue>
            </mapping>
            <mapping>
               <value>136</value>
               <newvalue>l3ipvlan</newvalue>
            </mapping>
            <mapping>
               <value>137</value>
               <newvalue>l3ipxvlan</newvalue>
            </mapping>
            <mapping>
               <value>138</value>
               <newvalue>digitalPowerline</newvalue>
            </mapping>
            <mapping>
               <value>139</value>
               <newvalue>mediaMailOverIp</newvalue>
            </mapping>
            <mapping>
               <value>140</value>
               <newvalue>dtm</newvalue>
            </mapping>
            <mapping>
               <value>141</value>
               <newvalue>dcn</newvalue>
            </mapping>
            <mapping>
               <value>142</value>
               <newvalue>ipForward</newvalue>
            </mapping>
            <mapping>
               <value>143</value>
               <newvalue>msdsl</newvalue>
            </mapping>
            <mapping>
               <value>144</value>
               <newvalue>ieee1394</newvalue>
            </mapping>
            <mapping>
               <value>145</value>
               <newvalue>if-gsn</newvalue>
            </mapping>
            <mapping>
               <value>146</value>
               <newvalue>dvbRccMacLayer</newvalue>
            </mapping>
            <mapping>
               <value>147</value>
               <newvalue>dvbRccDownstream</newvalue>
            </mapping>
            <mapping>
               <value>148</value>
               <newvalue>dvbRccUpstream</newvalue>
            </mapping>
            <mapping>
               <value>149</value>
               <newvalue>atmVirtual</newvalue>
            </mapping>
            <mapping>
               <value>150</value>
               <newvalue>mplsTunnel</newvalue>
            </mapping>
            <mapping>
               <value>151</value>
               <newvalue>srp</newvalue>
            </mapping>
            <mapping>
               <value>152</value>
               <newvalue>voiceOverAtm</newvalue>
            </mapping>
            <mapping>
               <value>153</value>
               <newvalue>voiceOverFrameRelay</newvalue>
            </mapping>
            <mapping>
               <value>154</value>
               <newvalue>idsl</newvalue>
            </mapping>
            <mapping>
               <value>155</value>
               <newvalue>compositeLink</newvalue>
            </mapping>
            <mapping>
               <value>156</value>
               <newvalue>ss7SigLink</newvalue>
            </mapping>
            <mapping>
               <value>157</value>
               <newvalue>propWirelessP2P</newvalue>
            </mapping>
            <mapping>
               <value>158</value>
               <newvalue>frForward</newvalue>
            </mapping>
            <mapping>
               <value>159</value>
               <newvalue>rfc1483</newvalue>
            </mapping>
            <mapping>
               <value>160</value>
               <newvalue>usb</newvalue>
            </mapping>
            <mapping>
               <value>161</value>
               <newvalue>ieee8023adLag</newvalue>
            </mapping>
            <mapping>
               <value>162</value>
               <newvalue>bgppolicyaccounting</newvalue>
            </mapping>
            <mapping>
               <value>163</value>
               <newvalue>frf16MfrBundle</newvalue>
            </mapping>
            <mapping>
               <value>164</value>
               <newvalue>h323Gatekeeper</newvalue>
            </mapping>
            <mapping>
               <value>165</value>
               <newvalue>h323Proxy</newvalue>
            </mapping>
            <mapping>
               <value>166</value>
               <newvalue>mpls</newvalue>
            </mapping>
            <mapping>
               <value>167</value>
               <newvalue>mfSigLink</newvalue>
            </mapping>
            <mapping>
               <value>168</value>
               <newvalue>hdsl2</newvalue>
            </mapping>
            <mapping>
               <value>169</value>
               <newvalue>shdsl</newvalue>
            </mapping>
            <mapping>
               <value>170</value>
               <newvalue>ds1FDL</newvalue>
            </mapping>
            <mapping>
               <value>171</value>
               <newvalue>pos</newvalue>
            </mapping>
            <mapping>
               <value>172</value>
               <newvalue>dvbAsiIn</newvalue>
            </mapping>
            <mapping>
               <value>173</value>
               <newvalue>dvbAsiOut</newvalue>
            </mapping>
            <mapping>
               <value>174</value>
               <newvalue>plc</newvalue>
            </mapping>
            <mapping>
               <value>175</value>
               <newvalue>nfas</newvalue>
            </mapping>
            <mapping>
               <value>176</value>
               <newvalue>tr008</newvalue>
            </mapping>
            <mapping>
               <value>177</value>
               <newvalue>gr303RDT</newvalue>
            </mapping>
            <mapping>
               <value>178</value>
               <newvalue>gr303IDT</newvalue>
            </mapping>
            <mapping>
               <value>179</value>
               <newvalue>isup</newvalue>
            </mapping>
            <mapping>
               <value>180</value>
               <newvalue>propDocsWirelessMaclayer</newvalue>
            </mapping>
            <mapping>
               <value>181</value>
               <newvalue>propDocsWirelessDownstream</newvalue>
            </mapping>
            <mapping>
               <value>182</value>
               <newvalue>propDocsWirelessUpstream</newvalue>
            </mapping>
            <mapping>
               <value>183</value>
               <newvalue>hiperlan2</newvalue>
            </mapping>
            <mapping>
               <value>184</value>
               <newvalue>propBWAp2Mp</newvalue>
            </mapping>
            <mapping>
               <value>185</value>
               <newvalue>sonetOverheadChannel</newvalue>
            </mapping>
            <mapping>
               <value>186</value>
               <newvalue>digitalWrapperOverheadChannel</newvalue>
            </mapping>
            <mapping>
               <value>187</value>
               <newvalue>aal2</newvalue>
            </mapping>
            <mapping>
               <value>188</value>
               <newvalue>radioMAC</newvalue>
            </mapping>
            <mapping>
               <value>189</value>
               <newvalue>atmRadio</newvalue>
            </mapping>
            <mapping>
               <value>190</value>
               <newvalue>imt</newvalue>
            </mapping>
            <mapping>
               <value>191</value>
               <newvalue>mvl</newvalue>
            </mapping>
            <mapping>
               <value>192</value>
               <newvalue>reachDSL</newvalue>
            </mapping>
            <mapping>
               <value>193</value>
               <newvalue>frDlciEndPt</newvalue>
            </mapping>
            <mapping>
               <value>194</value>
               <newvalue>atmVciEndPt</newvalue>
            </mapping>
            <mapping>
               <value>195</value>
               <newvalue>opticalChannel</newvalue>
            </mapping>
            <mapping>
               <value>196</value>
               <newvalue>opticalTransport</newvalue>
            </mapping>
            <mapping>
               <value>197</value>
               <newvalue>propAtm</newvalue>
            </mapping>
            <mapping>
               <value>198</value>
               <newvalue>voiceOverCable</newvalue>
            </mapping>
            <mapping>
               <value>199</value>
               <newvalue>infiniband</newvalue>
            </mapping>
            <mapping>
               <value>200</value>
               <newvalue>teLink</newvalue>
            </mapping>
            <mapping>
               <value>201</value>
               <newvalue>q2931</newvalue>
            </mapping>
            <mapping>
               <value>202</value>
               <newvalue>virtualTg</newvalue>
            </mapping>
            <mapping>
               <value>203</value>
               <newvalue>sipTg</newvalue>
            </mapping>
            <mapping>
               <value>204</value>
               <newvalue>sipSig</newvalue>
            </mapping>
            <mapping>
               <value>205</value>
               <newvalue>docsCableUpstreamChannel</newvalue>
            </mapping>
            <mapping>
               <value>206</value>
               <newvalue>econet</newvalue>
            </mapping>
            <mapping>
               <value>207</value>
               <newvalue>pon155</newvalue>
            </mapping>
            <mapping>
               <value>208</value>
               <newvalue>pon622</newvalue>
            </mapping>
            <mapping>
               <value>209</value>
               <newvalue>bridge</newvalue>
            </mapping>
            <mapping>
               <value>210</value>
               <newvalue>linegroup</newvalue>
            </mapping>
            <mapping>
               <value>211</value>
               <newvalue>voiceEMFGD</newvalue>
            </mapping>
            <mapping>
               <value>212</value>
               <newvalue>voiceFGDEANA</newvalue>
            </mapping>
            <mapping>
               <value>213</value>
               <newvalue>voiceDID</newvalue>
            </mapping>
            <mapping>
               <value>214</value>
               <newvalue>mpegTransport</newvalue>
            </mapping>
            <mapping>
               <value>215</value>
               <newvalue>sixToFour</newvalue>
            </mapping>
            <mapping>
               <value>216</value>
               <newvalue>gtp</newvalue>
            </mapping>
            <mapping>
               <value>217</value>
               <newvalue>pdnEtherLoop1</newvalue>
            </mapping>
            <mapping>
               <value>218</value>
               <newvalue>pdnEtherLoop2</newvalue>
            </mapping>
            <mapping>
               <value>219</value>
               <newvalue>opticalChannelGroup</newvalue>
            </mapping>
            <mapping>
               <value>220</value>
               <newvalue>homepna</newvalue>
            </mapping>
            <mapping>
               <value>221</value>
               <newvalue>gfp</newvalue>
            </mapping>
            <mapping>
               <value>222</value>
               <newvalue>ciscoISLvlan</newvalue>
            </mapping>
            <mapping>
               <value>223</value>
               <newvalue>actelisMetaLOOP</newvalue>
            </mapping>
            <mapping>
               <value>224</value>
               <newvalue>fcipLink</newvalue>
            </mapping>
            <mapping>
               <value>225</value>
               <newvalue>rpr</newvalue>
            </mapping>
            <mapping>
               <value>226</value>
               <newvalue>qam</newvalue>
            </mapping>
            <mapping>
               <value>227</value>
               <newvalue>lmp</newvalue>
            </mapping>
            <mapping>
               <value>228</value>
               <newvalue>cblVectaStar</newvalue>
            </mapping>
            <mapping>
               <value>229</value>
               <newvalue>docsCableMCmtsDownstream</newvalue>
            </mapping>
            <mapping>
               <value>230</value>
               <newvalue>adsl2</newvalue>
            </mapping>
            <mapping>
               <value>231</value>
               <newvalue>macSecControlledIF</newvalue>
            </mapping>
            <mapping>
               <value>232</value>
               <newvalue>macSecUncontrolledIF</newvalue>
            </mapping>
            <mapping>
               <value>233</value>
               <newvalue>aviciOpticalEther</newvalue>
            </mapping>
            <mapping>
               <value>234</value>
               <newvalue>atmbond</newvalue>
            </mapping>
            <mapping>
               <value>235</value>
               <newvalue>voiceFGDOS</newvalue>
            </mapping>
            <mapping>
               <value>236</value>
               <newvalue>mocaVersion1</newvalue>
            </mapping>
            <!-- as documented in information provided privately to IANA -->
            <mapping>
               <value>237</value>
               <newvalue>ieee80216WMAN</newvalue>
            </mapping>
            <mapping>
               <value>238</value>
               <newvalue>adsl2plus</newvalue>
            </mapping>
            <mapping>
               <value>239</value>
               <newvalue>dvbRcsMacLayer</newvalue>
            </mapping>
            <mapping>
               <value>240</value>
               <newvalue>dvbTdm</newvalue>
            </mapping>
            <mapping>
               <value>241</value>
               <newvalue>dvbRcsTdma</newvalue>
            </mapping>
            <mapping>
               <value>242</value>
               <newvalue>x86Laps</newvalue>
            </mapping>
            <mapping>
               <value>243</value>
               <newvalue>wwanPP</newvalue>
            </mapping>
            <mapping>
               <value>244</value>
               <newvalue>wwanPP2</newvalue>
            </mapping>
            <mapping>
               <value>245</value>
               <newvalue>voiceEBS</newvalue>
            </mapping>
            <mapping>
               <value>246</value>
               <newvalue>ifPwType</newvalue>
            </mapping>
            <mapping>
               <value>247</value>
               <newvalue>ilan</newvalue>
            </mapping>
            <mapping>
               <value>248</value>
               <newvalue>pip</newvalue>
            </mapping>
            <mapping>
               <value>249</value>
               <newvalue>aluELP</newvalue>
            </mapping>
            <mapping>
               <value>250</value>
               <newvalue>gpon</newvalue>
            </mapping>
            <mapping>
               <value>251</value>
               <newvalue>vdsl2</newvalue>
            </mapping>
            <mapping>
               <value>252</value>
               <newvalue>capwapDot11Profile</newvalue>
            </mapping>
            <mapping>
               <value>253</value>
               <newvalue>capwapDot11Bss</newvalue>
            </mapping>
            <mapping>
               <value>254</value>
               <newvalue>capwapWtpVirtualRadio</newvalue>
            </mapping>
            <mapping>
               <value>255</value>
               <newvalue>bits</newvalue>
            </mapping>
            <mapping>
               <value>256</value>
               <newvalue>docsCableUpstreamRfPort</newvalue>
            </mapping>
            <mapping>
               <value>257</value>
               <newvalue>cableDownstreamRfPort</newvalue>
            </mapping>
            <mapping>
               <value>258</value>
               <newvalue>vmwareVirtualNic</newvalue>
            </mapping>
            <mapping>
               <value>259</value>
               <newvalue>ieee802154</newvalue>
            </mapping>
            <mapping>
               <value>260</value>
               <newvalue>otnOdu</newvalue>
            </mapping>
            <mapping>
               <value>261</value>
               <newvalue>otnOtu</newvalue>
            </mapping>
            <mapping>
               <value>262</value>
               <newvalue>ifVfiType</newvalue>
            </mapping>
            <mapping>
               <value>263</value>
               <newvalue>g9981</newvalue>
            </mapping>
            <mapping>
               <value>264</value>
               <newvalue>g9982</newvalue>
            </mapping>
            <mapping>
               <value>265</value>
               <newvalue>g9983</newvalue>
            </mapping>
            <mapping>
               <value>266</value>
               <newvalue>aluEpon</newvalue>
            </mapping>
            <mapping>
               <value>267</value>
               <newvalue>aluEponOnu</newvalue>
            </mapping>
            <mapping>
               <value>268</value>
               <newvalue>aluEponPhysicalUni</newvalue>
            </mapping>
            <mapping>
               <value>269</value>
               <newvalue>aluEponLogicalLink</newvalue>
            </mapping>
            <mapping>
               <value>270</value>
               <newvalue>aluGponOnu</newvalue>
            </mapping>
            <mapping>
               <value>271</value>
               <newvalue>aluGponPhysicalUni</newvalue>
            </mapping>
            <mapping>
               <value>272</value>
               <newvalue>vmwareNicTeam</newvalue>
            </mapping>
            <mapping>
               <value>277</value>
               <newvalue>docsOfdmDownstream</newvalue>
            </mapping>
            <mapping>
               <value>278</value>
               <newvalue>docsOfdmaUpstream</newvalue>
            </mapping>
            <mapping>
               <value>279</value>
               <newvalue>gfast</newvalue>
            </mapping>
            <mapping>
               <value>280</value>
               <newvalue>sdci</newvalue>
            </mapping>
            <mapping>
               <value>281</value>
               <newvalue>xboxWireless</newvalue>
            </mapping>
            <mapping>
               <value>282</value>
               <newvalue>fastdsl</newvalue>
            </mapping>
            <mapping>
               <value>283</value>
               <newvalue>docsCableScte55d1FwdOob</newvalue>
            </mapping>
            <mapping>
               <value>284</value>
               <newvalue>docsCableScte55d1RetOob</newvalue>
            </mapping>
            <mapping>
               <value>285</value>
               <newvalue>docsCableScte55d2DsOob</newvalue>
            </mapping>
            <mapping>
               <value>286</value>
               <newvalue>docsCableScte55d2UsOob</newvalue>
            </mapping>
            <mapping>
               <value>287</value>
               <newvalue>docsCableNdf</newvalue>
            </mapping>
            <mapping>
               <value>288</value>
               <newvalue>docsCableNdr</newvalue>
            </mapping>
            <mapping>
               <value>289</value>
               <newvalue>ptm</newvalue>
            </mapping>
            <mapping>
               <value>290</value>
               <newvalue>ghn</newvalue>
            </mapping>
         </mappings>
      </value_map>
   </value_maps>
</zabbix_export>


File: /Advanced_Template_Net_Mikrotik_SNMPv2.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
   <version>3.4</version>
   <date>2015-12-30T14:41:30Z</date>
   <groups>
      <group>
         <name>Templates/Network Devices</name>
      </group>
   </groups>
   <templates>
      <template>
         <template>Advanced Template Net Mikrotik SNMPv2</template>
         <name>Advanced Template Net Mikrotik SNMPv2</name>
         <description>Link: https://github.com/XaTTa6bl4/zabbix-mikrotik

Based on Zabbix 3.4.5 official Template Net Mikrotik version: 0.15
(https://share.zabbix.com/official-templates)
MIBs used:
HOST-RESOURCES-MIB
MIKROTIK-MIB
Known Issues:
description : Doesn't have ifHighSpeed filled. fixed in more recent versions
version : RotuerOS 6.28 or lower
device : description : Doesn't have any temperature sensors
version : RotuerOS 6.38.5
device : Mikrotik 941-2nD, Mikrotik 951G-2HnD</description>
         <groups>
            <group>
               <name>Templates/Network Devices</name>
            </group>
         </groups>
         <applications>
            <application>
               <name>CPU</name>
            </application>
            <application>
               <name>Memory</name>
            </application>
            <application>
               <name>Temperature</name>
            </application>
            <application>
               <name>Storage</name>
            </application>
            <application>
               <name>Inventory</name>
            </application>
            <application>
                <name>Queues</name>
            </application>
         </applications>
         <items>
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
               <description>MIB: HOST-RESOURCES-MIB
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
                  </step>
               </preprocessing>
               <jmx_endpoint/>
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
               <description>MIB: HOST-RESOURCES-MIB
The size of the storage represented by this entry, in
units of hrStorageAllocationUnits. This object is
writable to allow remote configuration of the size of
the storage area in those cases where such an
operation makes sense and is possible on the
underlying system. For example, the amount of main
memory allocated to a buffer pool might be modified or
the amount of disk space allocated to virtual memory
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
                  </step>
               </preprocessing>
               <jmx_endpoint/>
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
               <master_item/>
            </item>
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
               <description>MIB: MIKROTIK-MIB
(mtxrHlTemperature) Device temperature in Celsius (degrees C). Might be missing in entry models (RB750, RB450G..)
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
                  </step>
               </preprocessing>
               <jmx_endpoint/>
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
               <trends>0d</trends>
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
               <description>MIB: MIKROTIK-MIB
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
               <trends>0d</trends>
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
               <trends>0d</trends>
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
               <description>MIB: MIKROTIK-MIB
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
               <trends>0d</trends>
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
               <description>MIB: MIKROTIK-MIB
Current firmware version</description>
               <inventory_link>16</inventory_link>
               <applications>
                  <application>
                     <name>Inventory</name>
                  </application>
               </applications>
               <valuemap/>
               <logtimefmt/>
               <preprocessing/>
               <jmx_endpoint/>
               <master_item/>
            </item>
	        <item>
	            <name>Main MAC</name>
	            <type>4</type>
	            <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
	            <snmp_oid>.1.3.6.1.2.1.2.2.1.6.1</snmp_oid>
	            <key>system.mac</key>
	            <delay>3600</delay>
	            <history>14d</history>
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
	            <description>MIB: MIKROTIK-MIB
Main MAC-address</description>
	            <inventory_link>12</inventory_link>
	            <applications>
	                <application>
	                    <name>Inventory</name>
	                </application>
	            </applications>
	            <valuemap/>
	            <logtimefmt/>
	            <preprocessing/>
	            <jmx_endpoint/>
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
                     <description>MIB: HOST-RESOURCES-MIB
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
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
               </item_prototypes>
               <trigger_prototypes>
                  <trigger_prototype>
                     <expression>{Advanced Template Net Mikrotik SNMPv2:system.cpu.util[hrProcessorLoad.{#SNMPINDEX}].avg(5m)}&gt;{$CPU_UTIL_MAX}</expression>
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
                     <yaxismin>0</yaxismin>
                     <yaxismax>100</yaxismax>
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
                              <host>Advanced Template Net Mikrotik SNMPv2</host>
                              <key>system.cpu.util[hrProcessorLoad.{#SNMPINDEX}]</key>
                           </item>
                        </graph_item>
                     </graph_items>
                  </graph_prototype>
               </graph_prototypes>
               <host_prototypes/>
               <jmx_endpoint/>
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
               <description>MIKROTIK-MIB::mtxrHlProcessorTemperature
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
                     <description>MIB: MIKROTIK-MIB
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
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
               </item_prototypes>
               <trigger_prototypes>
                  <trigger_prototype>
                     <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_WARN:"CPU"}</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_WARN:"CPU"}-3</recovery_expression>
                     <name>CPU: Temperature is above warning threshold: &gt;{$TEMP_WARN:"CPU"}</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>2</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
                     <type>0</type>
                     <manual_close>0</manual_close>
                     <dependencies>
                        <dependency>
                           <name>CPU: Temperature is above critical threshold: &gt;{$TEMP_CRIT:"CPU"}</name>
                           <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_CRIT:"CPU"}</expression>
                           <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_CRIT:"CPU"}-3</recovery_expression>
                        </dependency>
                     </dependencies>
                     <tags/>
                  </trigger_prototype>
                  <trigger_prototype>
                     <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&gt;{$TEMP_CRIT:"CPU"}</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].max(5m)}&lt;{$TEMP_CRIT:"CPU"}-3</recovery_expression>
                     <name>CPU: Temperature is above critical threshold: &gt;{$TEMP_CRIT:"CPU"}</name>
                     <correlation_mode>0</correlation_mode>
                     <correlation_tag/>
                     <url/>
                     <status>0</status>
                     <priority>4</priority>
                     <description>Last value: {ITEM.LASTVALUE1}.
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
                     <type>0</type>
                     <manual_close>0</manual_close>
                     <dependencies/>
                     <tags/>
                  </trigger_prototype>
                  <trigger_prototype>
                     <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].avg(5m)}&lt;{$TEMP_CRIT_LOW:"CPU"}</expression>
                     <recovery_mode>1</recovery_mode>
                     <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlProcessorTemperature.{#SNMPINDEX}].min(5m)}&gt;{$TEMP_CRIT_LOW:"CPU"}+3</recovery_expression>
                     <name>CPU: Temperature is too low: &lt;{$TEMP_CRIT_LOW:"CPU"}</name>
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
                        <formulaid>B</formulaid>
                     </condition>
                     <condition>
                        <macro>{#STORAGE_TYPE}</macro>
                        <value>.+hrStorageFixedDisk</value>
                        <operator>8</operator>
                        <formulaid>A</formulaid>
                     </condition>
                  </conditions>
               </filter>
               <lifetime>30d</lifetime>
               <description>HOST-RESOURCES-MIB::hrStorage discovery with storage filter</description>
               <item_prototypes>
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
                     <description>MIB: HOST-RESOURCES-MIB
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
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
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
                     <description>MIB: HOST-RESOURCES-MIB
The size of the storage represented by this entry, in
units of hrStorageAllocationUnits. This object is
writable to allow remote configuration of the size of
the storage area in those cases where such an
operation makes sense and is possible on the
underlying system. For example, the amount of main
memory allocated to a buffer pool might be modified or
the amount of disk space allocated to virtual memory
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
                        </step>
                     </preprocessing>
                     <jmx_endpoint/>
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
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
                     <application_prototypes/>
                     <master_item_prototype/>
                  </item_prototype>
               </item_prototypes>
               <trigger_prototypes>
                  <trigger_prototype>
                     <expression>{Advanced Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_CRIT}</expression>
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
                     <expression>{Advanced Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_WARN}</expression>
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
                           <expression>{Advanced Template Net Mikrotik SNMPv2:vfs.fs.pused[hrStorageSize.{#SNMPINDEX}].avg(5m)}&gt;{$STORAGE_UTIL_CRIT}</expression>
                           <recovery_expression/>
                        </dependency>
                     </dependencies>
                     <tags/>
                  </trigger_prototype>
               </trigger_prototypes>
               <graph_prototypes/>
               <host_prototypes/>
               <jmx_endpoint/>
            </discovery_rule>
            <discovery_rule>
                <name>Queues Simple Discovery</name>
                <type>4</type>
                <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                <snmp_oid>discovery[{#IFNAME},.1.3.6.1.4.1.14988.1.1.2.1.1.2]</snmp_oid>
                <key>queues.simple.discovery</key>
                <delay>3600</delay>
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
                    <evaltype>1</evaltype>
                    <formula/>
                    <conditions/>
                </filter>
                <lifetime>30d</lifetime>
                <description>Discovering Mikrotik Queues Simple.</description>
                <item_prototypes>
                    <item_prototype>
                        <name>Queue Simple {#IFNAME}: Bits received</name>
                        <type>4</type>
                        <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                        <snmp_oid>.1.3.6.1.4.1.14988.1.1.2.1.1.8.{#SNMPINDEX}</snmp_oid>
                        <key>queue.simple.in[QueueSimpleInOctets.{#SNMPINDEX}]</key>
                        <delay>180</delay>
                        <history>30d</history>
                        <trends>365d</trends>
                        <status>0</status>
                        <value_type>3</value_type>
                        <allowed_hosts/>
                        <units>bps</units>
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
                        <inventory_link>0</inventory_link>
                        <applications>
                            <application>
                                <name>Queues</name>
                            </application>
                        </applications>
                        <valuemap/>
                        <logtimefmt/>
                        <preprocessing>
                            <step>
                                <type>10</type>
                                <params/>
                            </step>
                            <step>
                                <type>1</type>
                                <params>8</params>
                            </step>
                        </preprocessing>
                        <jmx_endpoint/>
                        <application_prototypes/>
                        <master_item_prototype/>
                    </item_prototype>
                    <item_prototype>
                        <name>Queue Simple {#IFNAME}: Bits sent</name>
                        <type>4</type>
                        <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                        <snmp_oid>.1.3.6.1.4.1.14988.1.1.2.1.1.9.{#SNMPINDEX}</snmp_oid>
                        <key>queue.simple.out[QueueSimpleOutOctets.{#SNMPINDEX}]</key>
                        <delay>180</delay>
                        <history>30d</history>
                        <trends>365d</trends>
                        <status>0</status>
                        <value_type>3</value_type>
                        <allowed_hosts/>
                        <units>bps</units>
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
                        <inventory_link>0</inventory_link>
                        <applications>
                            <application>
                                <name>Queues</name>
                            </application>
                        </applications>
                        <valuemap/>
                        <logtimefmt/>
                        <preprocessing>
                            <step>
                                <type>10</type>
                                <params/>
                            </step>
                            <step>
                                <type>1</type>
                                <params>8</params>
                            </step>
                        </preprocessing>
                        <jmx_endpoint/>
                        <application_prototypes/>
                        <master_item_prototype/>
                    </item_prototype>
                </item_prototypes>
                <trigger_prototypes/>
                <graph_prototypes>
                    <graph_prototype>
                        <name>Queue {#IFNAME}: traffic</name>
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
                        <ymin_type_1>0</ymin_type_1>
                        <ymax_type_1>0</ymax_type_1>
                        <ymin_item_1>0</ymin_item_1>
                        <ymax_item_1>0</ymax_item_1>
                        <graph_items>
                            <graph_item>
                                <sortorder>0</sortorder>
                                <drawtype>5</drawtype>
                                <color>00AA00</color>
                                <yaxisside>0</yaxisside>
                                <calc_fnc>2</calc_fnc>
                                <type>0</type>
                                <item>
                                    <host>Advanced Template Net Mikrotik SNMPv2</host>
                                    <key>queue.simple.in[QueueSimpleInOctets.{#SNMPINDEX}]</key>
                                </item>
                            </graph_item>
                            <graph_item>
                                <sortorder>1</sortorder>
                                <drawtype>5</drawtype>
                                <color>3333FF</color>
                                <yaxisside>0</yaxisside>
                                <calc_fnc>2</calc_fnc>
                                <type>0</type>
                                <item>
                                    <host>Advanced Template Net Mikrotik SNMPv2</host>
                                    <key>queue.simple.out[QueueSimpleOutOctets.{#SNMPINDEX}]</key>
                                </item>
                            </graph_item>
                        </graph_items>
                    </graph_prototype>
                </graph_prototypes>
                <host_prototypes/>
                <jmx_endpoint/>
            </discovery_rule>

            <discovery_rule>
                <name>IP Addresses Discovery</name>
                <type>4</type>
                <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                <snmp_oid>discovery[{#IPADDR},.1.3.6.1.2.1.4.20.1.1, {#IFACEID},.1.3.6.1.2.1.4.20.1.2]</snmp_oid>
                <key>ip.addr.discovery</key>
                <delay>3600</delay>
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
                    <conditions>
                        <condition>
                            <macro>{#IPADDR}</macro>
                            <value>@IP addresses for discovery</value>
                            <operator>8</operator>
                            <formulaid>A</formulaid>
                        </condition>
                    </conditions>
                </filter>
                <lifetime>30d</lifetime>
                <description>Discovering IP from all interfaces.</description>
                <item_prototypes>
                    <item_prototype>
                        <name>ICMP loss {#IPADDR}</name>
                        <type>3</type>
                        <snmp_community/>
                        <snmp_oid/>
                        <key>icmppingloss[{#IPADDR}]</key>
                        <delay>60</delay>
                        <history>1w</history>
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
                        <description/>
                        <inventory_link>0</inventory_link>
                        <applications>
                            <application>
                                <name>Status</name>
                            </application>
                        </applications>
                        <valuemap/>
                        <logtimefmt/>
                        <preprocessing/>
                        <jmx_endpoint/>
                        <application_prototypes/>
                        <master_item_prototype/>
                    </item_prototype>
                    <item_prototype>
                        <name>ICMP response time {#IPADDR}</name>
                        <type>3</type>
                        <snmp_community/>
                        <snmp_oid/>
                        <key>icmppingsec[{#IPADDR}]</key>
                        <delay>60</delay>
                        <history>1w</history>
                        <trends>365d</trends>
                        <status>0</status>
                        <value_type>0</value_type>
                        <allowed_hosts/>
                        <units>s</units>
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
                        <inventory_link>0</inventory_link>
                        <applications>
                            <application>
                                <name>Status</name>
                            </application>
                        </applications>
                        <valuemap/>
                        <logtimefmt/>
                        <preprocessing/>
                        <jmx_endpoint/>
                        <application_prototypes/>
                        <master_item_prototype/>
                    </item_prototype>
                    <item_prototype>
                        <name>ICMP ping {#IPADDR}</name>
                        <type>3</type>
                        <snmp_community/>
                        <snmp_oid/>
                        <key>icmpping[{#IPADDR}]</key>
                        <delay>60</delay>
                        <history>1w</history>
                        <trends>365d</trends>
                        <status>0</status>
                        <value_type>3</value_type>
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
                        <inventory_link>0</inventory_link>
                        <applications>
                            <application>
                                <name>Status</name>
                            </application>
                        </applications>
                        <valuemap>
                            <name>Service state</name>
                        </valuemap>
                        <logtimefmt/>
                        <preprocessing/>
                        <jmx_endpoint/>
                        <application_prototypes/>
                        <master_item_prototype/>
                    </item_prototype>
                </item_prototypes>
                <trigger_prototypes>
                    <trigger_prototype>
                        <expression>{Advanced Template Net Mikrotik SNMPv2:icmppingloss[{#IPADDR}].min(5m)}&gt;{$ICMP_LOSS_WARN} and {Advanced Template Net Mikrotik SNMPv2:icmppingloss[{#IPADDR}].min(5m)}&lt;100</expression>
                        <recovery_mode>0</recovery_mode>
                        <recovery_expression/>
                        <name>High ICMP ping loss</name>
                        <correlation_mode>0</correlation_mode>
                        <correlation_tag/>
                        <url/>
                        <status>0</status>
                        <priority>2</priority>
                        <description/>
                        <type>0</type>
                        <manual_close>0</manual_close>
                        <dependencies>
                            <dependency>
                                <name>Unavailable by ICMP ping</name>
                                <expression>{Advanced Template Net Mikrotik SNMPv2:icmpping[{#IPADDR}].max(3)}=0</expression>
                                <recovery_expression/>
                            </dependency>
                        </dependencies>
                        <tags/>
                    </trigger_prototype>
                    <trigger_prototype>
                        <expression>{Advanced Template Net Mikrotik SNMPv2:icmppingsec[{#IPADDR}].avg(5m)}&gt;{$ICMP_RESPONSE_TIME_WARN}</expression>
                        <recovery_mode>0</recovery_mode>
                        <recovery_expression/>
                        <name>High ICMP ping response time</name>
                        <correlation_mode>0</correlation_mode>
                        <correlation_tag/>
                        <url/>
                        <status>0</status>
                        <priority>2</priority>
                        <description/>
                        <type>0</type>
                        <manual_close>0</manual_close>
                        <dependencies>
                            <dependency>
                                <name>High ICMP ping loss</name>
                                <expression>{Advanced Template Net Mikrotik SNMPv2:icmppingloss[{#IPADDR}].min(5m)}&gt;{$ICMP_LOSS_WARN} and {Advanced Template Net Mikrotik SNMPv2:icmppingloss[{#IPADDR}].min(5m)}&lt;100</expression>
                                <recovery_expression/>
                            </dependency>
                            <dependency>
                                <name>Unavailable by ICMP ping</name>
                                <expression>{Advanced Template Net Mikrotik SNMPv2:icmpping[{#IPADDR}].max(3)}=0</expression>
                                <recovery_expression/>
                            </dependency>
                        </dependencies>
                        <tags/>
                    </trigger_prototype>
                    <trigger_prototype>
                        <expression>{Advanced Template Net Mikrotik SNMPv2:icmpping[{#IPADDR}].max(3)}=0</expression>
                        <recovery_mode>0</recovery_mode>
                        <recovery_expression/>
                        <name>Unavailable by ICMP ping</name>
                        <correlation_mode>0</correlation_mode>
                        <correlation_tag/>
                        <url/>
                        <status>0</status>
                        <priority>4</priority>
                        <description>Last value: {ITEM.LASTVALUE1}.
Last three attempts returned timeout.  Please check device connectivity.</description>
                        <type>0</type>
                        <manual_close>0</manual_close>
                        <dependencies/>
                        <tags/>
                    </trigger_prototype>
                </trigger_prototypes>
                <graph_prototypes>
                    <graph_prototype>
                        <name>ICMP ping statistics {#IPADDR}</name>
                        <width>900</width>
                        <height>200</height>
                        <yaxismin>0.0000</yaxismin>
                        <yaxismax>100.0000</yaxismax>
                        <show_work_period>1</show_work_period>
                        <show_triggers>0</show_triggers>
                        <type>0</type>
                        <show_legend>1</show_legend>
                        <show_3d>0</show_3d>
                        <percent_left>0.0000</percent_left>
                        <percent_right>0.0000</percent_right>
                        <ymin_type_1>0</ymin_type_1>
                        <ymax_type_1>0</ymax_type_1>
                        <ymin_item_1>0</ymin_item_1>
                        <ymax_item_1>0</ymax_item_1>
                        <graph_items>
                            <graph_item>
                                <sortorder>0</sortorder>
                                <drawtype>5</drawtype>
                                <color>00CC00</color>
                                <yaxisside>0</yaxisside>
                                <calc_fnc>2</calc_fnc>
                                <type>0</type>
                                <item>
                                    <host>Advanced Template Net Mikrotik SNMPv2</host>
                                    <key>icmppingsec[{#IPADDR}]</key>
                                </item>
                            </graph_item>
                            <graph_item>
                                <sortorder>1</sortorder>
                                <drawtype>0</drawtype>
                                <color>EE0000</color>
                                <yaxisside>1</yaxisside>
                                <calc_fnc>2</calc_fnc>
                                <type>0</type>
                                <item>
                                    <host>Advanced Template Net Mikrotik SNMPv2</host>
                                    <key>icmppingloss[{#IPADDR}]</key>
                                </item>
                            </graph_item>
                        </graph_items>
                    </graph_prototype>
                </graph_prototypes>
                <host_prototypes/>
                <jmx_endpoint/>
            </discovery_rule>
         </discovery_rules>
         <httptests/>
         <macros>
            <macro>
               <macro>{$TEMP_CRIT:"CPU"}</macro>
               <value>75</value>
            </macro>
            <macro>
               <macro>{$TEMP_WARN:"CPU"}</macro>
               <value>70</value>
            </macro>
            <macro>
               <macro>{$CPU_UTIL_MAX}</macro>
               <value>90</value>
            </macro>
            <macro>
               <macro>{$MEMORY_UTIL_MAX}</macro>
               <value>90</value>
            </macro>
            <macro>
               <macro>{$TEMP_CRIT}</macro>
               <value>60</value>
            </macro>
            <macro>
               <macro>{$TEMP_WARN}</macro>
               <value>50</value>
            </macro>
            <macro>
               <macro>{$TEMP_CRIT_LOW}</macro>
               <value>5</value>
            </macro>
            <macro>
               <macro>{$STORAGE_UTIL_CRIT}</macro>
               <value>90</value>
            </macro>
            <macro>
               <macro>{$STORAGE_UTIL_WARN}</macro>
               <value>80</value>
            </macro>
         </macros>
         <templates>
            <template>
               <name>Advanced Template Module Interfaces SNMPv2</name>
            </template>
            <template>	
               <name>Template Module Generic SNMPv2</name>	
            </template>
         </templates>
         <screens/>
      </template>
   </templates>
   <graphs>
      <graph>
         <name>Memory utilization</name>
         <width>900</width>
         <height>200</height>
         <yaxismin>0</yaxismin>
         <yaxismax>100</yaxismax>
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
                  <host>Advanced Template Net Mikrotik SNMPv2</host>
                  <key>vm.memory.pused[memoryUsedPercentage.Memory]</key>
               </item>
            </graph_item>
         </graph_items>
      </graph>
   </graphs>
   <triggers>
      <trigger>
         <expression>{Advanced Template Net Mikrotik SNMPv2:vm.memory.pused[memoryUsedPercentage.Memory].avg(5m)}&gt;{$MEMORY_UTIL_MAX}</expression>
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
      <trigger>
         <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_WARN:"Device"}</expression>
         <recovery_mode>1</recovery_mode>
         <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_WARN:"Device"}-3</recovery_expression>
         <name>Device: Temperature is above warning threshold: &gt;{$TEMP_WARN:"Device"}</name>
         <correlation_mode>0</correlation_mode>
         <correlation_tag/>
         <url/>
         <status>0</status>
         <priority>2</priority>
         <description>Last value: {ITEM.LASTVALUE1}.
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
         <type>0</type>
         <manual_close>0</manual_close>
         <dependencies>
            <dependency>
               <name>Device: Temperature is above critical threshold: &gt;{$TEMP_CRIT:"Device"}</name>
               <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_CRIT:"Device"}</expression>
               <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_CRIT:"Device"}-3</recovery_expression>
            </dependency>
         </dependencies>
         <tags/>
      </trigger>
      <trigger>
         <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&gt;{$TEMP_CRIT:"Device"}</expression>
         <recovery_mode>1</recovery_mode>
         <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].max(5m)}&lt;{$TEMP_CRIT:"Device"}-3</recovery_expression>
         <name>Device: Temperature is above critical threshold: &gt;{$TEMP_CRIT:"Device"}</name>
         <correlation_mode>0</correlation_mode>
         <correlation_tag/>
         <url/>
         <status>0</status>
         <priority>4</priority>
         <description>Last value: {ITEM.LASTVALUE1}.
This trigger uses temperature sensor values as well as temperature sensor status if available</description>
         <type>0</type>
         <manual_close>0</manual_close>
         <dependencies/>
         <tags/>
      </trigger>
      <trigger>
         <expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].avg(5m)}&lt;{$TEMP_CRIT_LOW:"Device"}</expression>
         <recovery_mode>1</recovery_mode>
         <recovery_expression>{Advanced Template Net Mikrotik SNMPv2:sensor.temp.value[mtxrHlTemperature].min(5m)}&gt;{$TEMP_CRIT_LOW:"Device"}+3</recovery_expression>
         <name>Device: Temperature is too low: &lt;{$TEMP_CRIT_LOW:"Device"}</name>
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
         <expression>{Advanced Template Net Mikrotik SNMPv2:system.hw.serialnumber.diff()}=1 and {Advanced Template Net Mikrotik SNMPv2:system.hw.serialnumber.strlen()}&gt;0</expression>
         <recovery_mode>2</recovery_mode>
         <recovery_expression/>
         <name>Device has been replaced (new serial number received)</name>
         <correlation_mode>0</correlation_mode>
         <correlation_tag/>
         <url/>
         <status>0</status>
         <priority>1</priority>
         <description>Last value: {ITEM.LASTVALUE1}.
Device serial number has changed. Ack to close</description>
         <type>0</type>
         <manual_close>1</manual_close>
         <dependencies/>
         <tags/>
      </trigger>
      <trigger>
         <expression>{Advanced Template Net Mikrotik SNMPv2:system.hw.firmware.diff()}=1 and {Advanced Template Net Mikrotik SNMPv2:system.hw.firmware.strlen()}&gt;0</expression>
         <recovery_mode>2</recovery_mode>
         <recovery_expression/>
         <name>Firmware has changed</name>
         <correlation_mode>0</correlation_mode>
         <correlation_tag/>
         <url/>
         <status>0</status>
         <priority>1</priority>
         <description>Last value: {ITEM.LASTVALUE1}.
Firmware version has changed. Ack to close</description>
         <type>0</type>
         <manual_close>1</manual_close>
         <dependencies/>
         <tags/>
      </trigger>
   </triggers>
   <value_maps/>
</zabbix_export>


File: /graph_for_module_icmp_ping.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
   <version>3.4</version>
   <date>2015-12-30T14:41:30Z</date>
   <graphs>
       <graph>
           <name>ICMP ping statistics</name>
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
           <percent_right>100.0000</percent_right>
           <ymin_type_1>0</ymin_type_1>
           <ymax_type_1>0</ymax_type_1>
           <ymin_item_1>0</ymin_item_1>
           <ymax_item_1>0</ymax_item_1>
           <graph_items>
               <graph_item>
                   <sortorder>0</sortorder>
                   <drawtype>5</drawtype>
                   <color>00AA00</color>
                   <yaxisside>0</yaxisside>
                   <calc_fnc>2</calc_fnc>
                   <type>0</type>
                   <item>
                       <host>Template Module ICMP Ping</host>
                       <key>icmppingsec</key>
                   </item>
               </graph_item>
               <graph_item>
                   <sortorder>1</sortorder>
                   <drawtype>2</drawtype>
                   <color>FF3333</color>
                   <yaxisside>0</yaxisside>
                   <calc_fnc>2</calc_fnc>
                   <type>0</type>
                   <item>
                       <host>Template Module ICMP Ping</host>
                       <key>icmppingloss</key>
                   </item>
               </graph_item>
           </graph_items>
       </graph>
   </graphs>
</zabbix_export>


File: /README.md
# Advanced Template Net Mikrotik SNMPv2

Template based on original Template Net Mikrotik SNMPv2 from stock Zabbix 3.4

## Improvements
* Added main device MAC to inventory
* Added item "Interface MAC address" for each interface (useful for mac-telnet/mac-winbox in MikroTik)
* Added unicast pps items and added them to traffic graphs
* Changed trigger "High bandwidth usage" to operate only on ethernet type interfaces (because speed of other type interfaces determines incorrect in MikroTik)
* Added Queues Simple discovery with graphs
* Added IP discovery with ICMP triggers and graphs, for multiwan configurations (discovering all IPs, except regexp)

## Installation

Tested on Zabbix 3.4+

* At first you need to import `Advanced_Template_Module_Interfaces_SNMPv2.xml`. This module is linked with the main template.
* Then import  the main module `Advanced_Template_Net_Mikrotik_SNMPv2.xml`

For correct IP discovery working, you need to add Regular Expressions (see screenshot), for discovering only public IPs:
```
IP addresses for discovery	
1	»	^(172\.(1+[6-9]|2+[0-9]|3+[0-2])\.)+[0-9]{1,3}+\.+[0-9]{1,3}$	[Result is FALSE]
2	»	^(10\.[0-9]{1,3}\.)+[0-9]{1,3}+\.+[0-9]{1,3}$			[Result is FALSE]
3	»	^(192\.168\.)+[0-9]{1,3}+\.+[0-9]{1,3}$				[Result is FALSE]
```
![RegExp IP addresses for discovery](/regexp/regexp-ip_addresses_for_discovery.png?raw=true "RegExp IP addresses for discovery")


