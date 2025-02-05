# Repository Information
Name: MikroTik_CAPsMAN_Automation

# Directory Structure
Directory structure:
└── github_repos/MikroTik_CAPsMAN_Automation/
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
    │   │       ├── pack-cac5762920d0e7b03105317fa4b8bf8c8f891133.idx
    │   │       └── pack-cac5762920d0e7b03105317fa4b8bf8c8f891133.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── CAPsMAN_Auto_SSID_Pass_Change.rsc
    ├── CAPsMAN_CAP_Package_Auto_Download.rsc
    ├── CAPsMAN_CAP_Package_Auto_Install.rsc
    ├── CAPsMAN_Interfaces_Count.rsc
    ├── CAPsMAN_Interfaces_Import.rsc
    ├── CAPsMAN_Interfaces_Remove.rsc
    ├── CAPsMAN_Status.rsc
    └── README.md


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
	url = https://github.com/gbudny93/MikroTik_CAPsMAN_Automation.git
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
0000000000000000000000000000000000000000 a46baba267d3fb096d0b2d7582c7af948b78cbca vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/gbudny93/MikroTik_CAPsMAN_Automation.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 a46baba267d3fb096d0b2d7582c7af948b78cbca vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/gbudny93/MikroTik_CAPsMAN_Automation.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a46baba267d3fb096d0b2d7582c7af948b78cbca vivek-dodia <vivek.dodia@icloud.com> 1738606017 -0500	clone: from https://github.com/gbudny93/MikroTik_CAPsMAN_Automation.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
a46baba267d3fb096d0b2d7582c7af948b78cbca refs/remotes/origin/master


File: /.git\refs\heads\master
a46baba267d3fb096d0b2d7582c7af948b78cbca


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /CAPsMAN_Auto_SSID_Pass_Change.rsc
# RouterOS Fucntion 
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Generates string and updates CAPsMAN profile security config

:global AutoPassChange do={


    :local scriptSource;
    :local newSSIDPass;

    :local systemName [system identity get value name];

    /tool fetch mode=https http-method=get url=$url dst-path=($destinationPath."/".$destinationFileName);
    
    :log info "...:::Script String Generator fetched:::...";

    :set $scriptSource [/file get ($destinationPath."/".$destinationFileName) contents];

    /system script add name=$scriptName source=$scriptSource;

    :set $newSSIDPass $GenerateString; 

    /caps-man security set passphrase=$newSSIDPass where name=$securityProfile;

    /tool e-mail send server=$smtpServer port=$smtpPort from=($systemName.$domain)  \ 
    to=$recipient subject=($systemName." generated new pass for ".$securityProfile) \
    body=("New ."$securityProfile." generated password is: ".$newSSIDPass);

}

$AutoPassChange url="https://raw.githubusercontent.com/gbudny93/RouterOS_Useful_Scripts/master/RouterOS_String_Generator.rsc" \ 
destinationPath="scripts" destinationFileName="RouterOS_String_Generator.rsc" scriptName=scriptName securityProfile=securityProfileName \
smtpServer=smtpServer smtpPort=smtpPort domain=example.com recipient=recipient@example.com; 

File: /CAPsMAN_CAP_Package_Auto_Download.rsc
# RouterOS Fucntion 
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Checks if latest package is available. Downloads it to specified location and send email notification

:global PackageAutoDownload do={

    /system package update check-for-updates;

    :local packageCurrent [/system package update get installed-version];
    :local packageLatest [/system package update get latest-version];
    :local packageName [/system package get value-name=name number=0];
    :local systemName [/system identity get value-name=name]; 

    :if ($packageCurrent != $packageLatest) do={

        :log info ("...:::New cAP package available - ".$packageLatest." Downloading:::...");
        
        /system package update download;
        
        :log info ("...:::".$packageName." ".$packageLatest." downloaded. Moving to specified container:::...");
        :delay 2;
        
        /tool fetch address=$capsmanIP src-path=($packageName."-".$packageLatest.".npk") user=$userName password=$password dst-path=($packagePath."/".($packageName."-".$packageLatest.".npk")) mode=ftp port=21;
        
        :log info ("...:::Package moved to ".$capsmanIP."\n Ready to deploy:::..."); 

        /tool e-mail send server=$smtpServer port=$smtpPort from=($systemName.$domain) \ 
        to=$recipient subject=("cAP update available on ".$systemName) \ 
        body=($systemName." downloaded latest package ".$packageLatest.". \
        \nPackage ready to deploy.");

        /file remove ($packageName."-".$packageLatest.".npk");

    }\
    else={

        :log info ("...:::No cAP updates found. ".$packageCurrent." is the latest version...:::");

        /tool e-mail send server=$smtpServer port=$smtpPort from=($systemName.$domain) \ 
        to=$recipient subject=("No cAP update available on ".$systemName) \ 
        body=($systemName." cAPs have installed the latest package ".$packageLatest);

    }
}

$PackageAutoDownload userName=userName password=password packagePath=path \
smtpServer=ipAddress smtpPort=poty domain=@example.com \
recipient=recipient@example.com capsmanIP=capsmanIP;

File: /CAPsMAN_CAP_Package_Auto_Install.rsc
# RouterOS Fucntion 
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Upgrades all CAPs attached to CAPsMAN. Log actions in system log and in the file. Sends email notification upon completion 

:global CapAutoUpgrade do={

    :local capIdentity; 
    :local capVersion; 

    :local today [/system clock get date]; 
    :local time [/system clock get time]; 
    :local systemName [/system identity get value-name=name];
    :local capsNumber [/caps-man remote-cap print count-only];
    :local packagePath [/caps-man manager get package-path];

    :local fileName ($today."_".$systemName."_CAP_Upgrade.log");

    :if ([:len [/file find name=$fileName]] <= 0) do={
        
        :log warning"...:::Log file not found, creating file:::...";
        /file print file=$fileName;
    
    }

    :if ([:len [/file find name=$fileName]] > 0) do={
        
        :log info "...:::Log file found:::...";
        
    }

    :if ($packagePath != "") do={

        :log info "...:::Package path defined. Starting CAPs upgrade:::..."

        /file set $fileName contents=([get $fileName contents].("New upgrade task started ".$today." at ".$time);

        :for $i from=0 to=($capsNumber - 1) step=1 do={

            :set $capIdentity [/ caps-man remote-cap get value-name=identity number=$i];
            /caps-man remote-cap upgrade numbers=$i;
            :log info ("Upgrading ".$capIdentity."...");
            /file set $fileName contents=([get $fileName contents].($i.") Upgraded ".$capIdentity."\n"));
        
            :set $capIdentity; 

        }

        /tool e-mail send server=$smtpServer port=$smtpPort from=($systemName.$domain) \ 
        to=$recipient subject=("Remote CAPs upgrade run on ".$systemName) \ 
        body=($systemName." upgraded remote CAPs. \n Attached upgrade log file.") file=$fileName; 

    }\
    else={

        :log warning "...:::Upgrade path not specified. Firmware image is missing!:::..."

    }
}

$CapAutoUpgrade smtpServer=smtpIP port=smtpPort recipient=recipients@example.com domain=@example.com 

File: /CAPsMAN_Interfaces_Count.rsc
# RouterOS Script
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Makes a full copy to file all defined CAPsMAN interfaces.
# Script must be run on primary CAPsMAN in your environment.

:global capIntCount;

:local fileName "int_number.txt";
:local intFileName caps_int.rsc;

:local smtpServer #smtp server IP
:local smtpPort #smtp port
:local from #sender email  
:local to #recipients email
:local cc #cc email
:local subject "Interfaces Sync Notification"
:local body "CAPsMAN Ready for Interfaces Sync Process"

:log info "..::Interfaces count and export started::..";

:set capIntCount [/caps-man interface print count-only];

:if ([:len [/file find name=$fileName]] <= 0) do={
    :log info "File not found, creating file";
    file print file=$fileName;
}

:if ([:len [/file find name=$fileName]] > 0) do={
    :log info "File found";
    file set $fileName contents=$capIntCount;
}

:log info "..::Exporting Interfaces";

caps-man interface export file=$intFileName;

:log info "..::Interfaces count and export finished::..";

tool e-mail send server=$smtpServer port=$smtpPort from=$from to=$to cc=$cc subject=$subject body=$body;


File: /CAPsMAN_Interfaces_Import.rsc
# RouterOS Function 
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Imports CAPsMAN interfaces from file  

import file=caps_int.rsc
:log info "..::CAPsMAN Interfaces Imported::.."

File: /CAPsMAN_Interfaces_Remove.rsc
# RouterOS Script
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020 
# Removes all defined CAPsMAN interfaces. Downloads current list from primary CAPsMAN and import it. 
# Script must be run on any of backup CAPsMANs. 

:local primaryCAPsMAN #primary CAPsMAN IP
:local filePath caps_int.rsc
:local filePath2 int_number.txt
:local userName #Username
:local password #Password

:local capIntCount

:local smtpServer #smtp server IP
:local smtpPort #smtp port 
:local from #sender email 
:local to #recipeints email
:local cc #cc email
:local subject "Interfaces Sync Notification"
:local body "CAPsMAN Interfaces Sync Completed"

:log info "..::CAPsMAN Interfaces Update Script Started::..";
:log info "..::Downloading file from Primary CAPsMAN::..";

tool fetch address=$primaryCAPsMAN src-path=$filePath \
user=$userName mode=ftp password=$password dst-path=$filePath port=21;

tool fetch address=$primaryCAPsMAN src-path=$filePath2 \
user=$userName mode=ftp password=$password dst-path=$filePath2 port=21;

:set $capIntCount [/file get $filePath2 contents]; 

:set $capIntCount ($capIntCount -1);

:log info "..::Files downloaded::..";
:log info "..::waiting 5s:..";

:delay 5;

:log info "::..Removing CAPsMAN interfaces::..";

:for a from=0 to=$capIntCount step=1 do= \
{
    /caps-man interface remove $a;
}

:delay 5;

:log warning "..::CAPsMAN Interfaces removed::..";
:log info "..::Sending notification::..";

tool e-mail send server=$smtpServer port=$smtpPort from=$from to=$to cc=$cc subject=$subject body=$body;

:log info "..::Waiting for reboot::..";

:delay 10;

system reboot 

File: /CAPsMAN_Status.rsc
# RouterOS Function 
# Copyright (c) Grzegorz Budny 
# Version 1.0 
# Last update: 2/8/2020
# Generates e-mail CAPsMAN status 

:global CAPsMANStatus do={

    :local intCount         [/caps-man remote-cap print count-only];
    :local remoteCapCount   [/caps-man remote-cap print count-only];
    :local regTableCount    [/caps-man registration-table print count-only];
    :local inactiveIntCount [/caps-man interface print count-only where inactive];
    :local masterIntCount   [/caps-man interface print count-only where master];
    :local disabledIntCount [/caps-man interface print count-only where disabled];
    :local boundIntCount    [/caps-man interface print count-only where bound];
    :local channelCount     [/caps-man channel print count-only];
    :local aclCount         [/caps-man access-list print count-only];
    :local radiusCount      [/radius print count-only];
    #:local dnsServers       [/ip dns get value-name=servers];

    :local systemName       [/system identity get value-name=name];
    :local uptime           [/system resource get uptime];
    :local FreeMemory       [/system resource get free-memory];
    :local TotalMemory      [/system resource get total-memory];
    :local cpu              [/system resource get cpu];
    :local cpuCount         [/system resource get cpu-count];
    :local cpuFrequency     [/system resource get cpu-frequency];
    :local cpuLoad          [/system resource get cpu-load];
    :local freeHdd          [/system resource get free-hdd-space];
    :local totalHdd         [/system resource get total-hdd-space];
    :local architectureName [/system resource get architecture-name];  
    :local license          [/system license get level];
    :local boardName        [/system resource get board-name];
    :local version          [/system resource get version];


    /tool e-mail send server=$smtpServer port=$smtpPort from=($systemName.$domain) \ 
        to=$recipient subject=($systemName." status")       \
        body=($systemName." system status: \n\n"            \ 
             ."Uptime: ".$uptime."\n"                       \
             ."Free Memory: ".$FreeMemory." B \n"           \
             ."Total Memory: ".$TotalMemory." B \n"         \
             ."CPU ".$cpu."\n"                              \
             ."CPU Count: ".$cpuCount."\n"                  \
             ."CPU Frequency: ".$cpuFrequency."MHz\n"       \
             ."CPU Load: ".$cpuLoad." % \n"                 \
             ."Free HDD Space: ".$freeHdd." B \n"           \
             ."Total HDD Space:".$totalHdd." B \n"          \
             ."Architecture: ".$achritecture." \n"          \
             ."License Level: ".$license." \n"              \
             ."Board Name: ".$boardName." \n"               \
             ."Version: ".$version."\n\n\n"                 \
             ."CAP Interfaces: ".$intCount."\n"             \
             ."CAPs Registered: ".$remoteCapCount."\n"      \
             ."Hosts Registered: ".$regTableCount."\n"      \  
             ."Inactive Interfaces: ".$inactiveIntCount."\n"\
             ."Master Interfaces: ".$masterIntCount."\n"    \
             ."Disabled Interfaces: ".$disabledIntCount."\n"\
             ."Bouneded Interfaces: ".$boundIntCount."\n"   \
             ."Channels defined: ".$channelCount."\n"       \
             ."ACLs defined: ".$aclCount."\n"               \
             ."Radius Defined: ".$radiusCount);

}

$CAPsMANStatus smtpServer=smtpServer smtpPort=smtpPort domain=domain recipient=recipient@example.com;

File: /README.md
# MikroTik_CAPsMAN_Automation
> MikroTik CAPsMAN Automation contains RouterOS scripts and function that all together gives you a complex CAPsMAN Automation: simple sync mechanism, reporting, moniroring as well automation of administrative tasks. 
**This repository may use some scripts from :link: [RouterOS_Useful_Scripts](https://github.com/gbudny93/RouterOS_Useful_Scripts).**
**Here you can find script template that I use :link: [RouterOS_Script_Template](https://gist.github.com/gbudny93/8ad0899576407e5efe9323febb368796).**

![](https://img.shields.io/badge/scripting-routeros-important.svg)
![](https://img.shields.io/badge/mikrotik-routerBOARD-yellow)
![](https://img.shields.io/badge/network-automation-informational)
![](https://img.shields.io/badge/mikrotik-capsman-yellow)

## Change log
    
   - 10/17/2019 update code fixes
        - CAPsMAN_Status.rsc
        
   - 10/17/2019 update code fixes
        - CAPsMAN_Auto_SSID_Pass_Change.rsc
        - CAPsMAN_Package_Auto_Download.rsc

   - 8/4/2019 first release
    -   CAPsMAN General Automation 
        -   CAPsMAN_CAP_Package_Auto_Download.rsc
        -   CAPsMAN_CAP_Package_Auto_Install.rsc
    -   CAPsMAN Automated Sync 
        -   CAPsMAN_Interfaces_Count.rsc
        -   CAPsMAN_Interfaces_Import.rsc
        -   CAPsMAN_Interfaces_Remove.rsc
    -   CAPsMAN Reporting 
        -   CAPsMAN_Status.rsc

## Prerequisites

-  :white_check_mark: RouterOS v6.40 or higher

## How to use

### 1. CAPsMAN General Automation 

#### CAPsMAN_Auto_SSID_Pass_Change.rsc 
> Fetches [RouterOS_String_Generator.rsc](https://github.com/gbudny93/RouterOS_Useful_Scripts/blob/master/RouterOS_String_Generator.rsc) and adds it to scheduler. Generated string is added as new passphrase to pointed SSIDs based on scheduler. 

Example:
```
$AutoPassChange url="https://raw.githubusercontent.com/gbudny93/RouterOS_Useful_Scripts/master/RouterOS_String_Generator.rsc" \ 
destinationPath="scripts" destinationFileName="RouterOS_String_Generator.rsc" scriptName=scriptName securityProfile=securityProfileName \
smtpServer=smtpServer smtpPort=smtpPort domain=example.com recipient=recipient@example.com; 
```

#### CAPsMAN_Package_Auto_Download.rsc 
> Downloads latest RouterOS package if newer version available. Upgrades RouterOS and sends email notification. 

Example:
```
$PackageAutoDownload userName=userName password=password packagePath=path \
smtpServer=ipAddress smtpPort=poty domain=@example.com \
recipient=recipient@example.com capsmanIP=capsmanIP;
```

### 2. CAPsMAN Automated Sync (pseudo HA)
> Performs sync process of CAPsMAN features between primary CAPsMAN and backup controllers. Ensures pseudo HA keeping the same configuration on all systems modifying only primary. 

Supported features:
- [x] Sync CAP interfaces 
- [x] Email notifications
- [ ] Determine primary CAPsMAN based on condition 
- [ ] Sync channels 
- [ ] Sync provisioning 
- [ ] Sync ACL 
- [ ] Sync configurations 
- [ ] Sync custom parameters of RouterOS 
- [ ] Functions based 

Example: 
RouterOS_Interfaces_Count.rsc must be run on primary CAPsMAN
RouterOS_Interfaces_Remove.rsc must be run on backup CAPsMAN
RouterOS_Interfaces_Import.rsc must be run on backup CAPsMAN 

### 3. CAPsMAN Reporting 
> Set of scripts that performs some simple reporting on this what is going on with wireless environment from controller perspective. 

#### CAPSMAN_Status.rsc 
> Send general RouterOS and CAPsMAN status information via email. 

Example: 
```
$CAPsMANStatus smtpServer=smtpServer smtpPort=smtpPort domain=domain recipient=recipient@example.com;
```

## Authors

  - Grzegorz Budny

