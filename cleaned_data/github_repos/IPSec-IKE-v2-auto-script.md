# Repository Information
Name: IPSec-IKE-v2-auto-script

# Directory Structure
Directory structure:
└── github_repos/IPSec-IKE-v2-auto-script/
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
    │   │       │   └── main
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-7890530a8dc4da5a1aebb3c485c1a4a7e2b760d9.idx
    │   │       └── pack-7890530a8dc4da5a1aebb3c485c1a4a7e2b760d9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── IKEv2-peer-autoscript.rsc
    ├── IKEv2-remove-peer-autoscript.rsc
    ├── IKEv2-server-autoscript.rsc
    ├── IKEv2-strongswan-peer-autoscript.rsc
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
	url = https://github.com/mikrotik-user/IPSec-IKE-v2-auto-script.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/main


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
0000000000000000000000000000000000000000 0006f8397f5ebfdaf94d5f9d04844578ed56b5b9 vivek-dodia <vivek.dodia@icloud.com> 1738605965 -0500	clone: from https://github.com/mikrotik-user/IPSec-IKE-v2-auto-script.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 0006f8397f5ebfdaf94d5f9d04844578ed56b5b9 vivek-dodia <vivek.dodia@icloud.com> 1738605965 -0500	clone: from https://github.com/mikrotik-user/IPSec-IKE-v2-auto-script.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0006f8397f5ebfdaf94d5f9d04844578ed56b5b9 vivek-dodia <vivek.dodia@icloud.com> 1738605965 -0500	clone: from https://github.com/mikrotik-user/IPSec-IKE-v2-auto-script.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0006f8397f5ebfdaf94d5f9d04844578ed56b5b9 refs/remotes/origin/main


File: /.git\refs\heads\main
0006f8397f5ebfdaf94d5f9d04844578ed56b5b9


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /IKEv2-peer-autoscript.rsc
/system script
add dont-require-permissions=no name=IKEv2-peer owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    local Hostname\r\
    \n:local PeerName\r\
    \n:local Password\r\
    \n:local PeerCertFile\r\
    \n:local variant\r\
    \n:local err false\r\
    \n\r\
    \n:local inputFunc do={:put \$1;:return}\r\
    \n\r\
    \n:put \"#################################################################\
    #############\"\r\
    \n:put \"Welcome to IPSec-auto-script. This script will setup IPSec IKEv2 \
    peer.\"\r\
    \n:put \"#################################################################\
    #############\\r\\n\"\r\
    \n:put \"What would you like to do\\\?\"\r\
    \n:put \"1. Create peer\"\r\
    \n:put \"2. Remove peer\"\r\
    \n\t   \r\
    \n:set variant [\$inputFunc \"Choose corresponding number.\"]\r\
    \n\r\
    \n:if (variant = 1) do={\r\
    \n     :put \"\"\r\
    \n     :set Hostname  [\$inputFunc \"Input domain name of IPSec IKEv2 serv\
    er you want to connect to. E.g.: 123456789012.sn.mynetname.net.\"]\r\
    \n\t :if (\$Hostname = \"\") do={\r\
    \n\t     :put \"Error: cannot get DNS name\"\r\
    \n         :set err \"true\"\r\
    \n\t    }\r\
    \n\t :set PeerCertFile  [\$inputFunc \"Input peer certificate filename you\
    \_uploaded from server. E.g.: PeerName@Hostname.p12\"]\r\
    \n\t :set PeerName [\$inputFunc \"Input PeerName. E.g.: newPeer\" ]\r\
    \n\t :set Password  [\$inputFunc \"Input passphrase to import certificate \
    from file\"]\r\
    \n\t :put \"Importing \$PeerCertFile\"\r\
    \n     :do {/certificate import file-name=\"\$PeerCertFile\" passphrase=\"\
    \$Password\"} on-error={\r\
    \n\t     :put \"Error importing \$PeerCertFile\"\r\
    \n\t\t :set err \"true\"}\r\
    \n\t :put \"Setting up new IPSec peer profile (phase 1)\"\r\
    \n\t :do {/ip ipsec profile add dh-group=modp2048,modp1536,modp1024 enc-al\
    gorithm=aes-256,aes-192,aes-128 hash-algorithm=sha256 name=\"profile-\$Hos\
    tname\" nat-traversal=yes proposal-check=obey} on-error={\r\
    \n\t     :put \"Error: cannot add peer profile profile-\$Hostname\"\r\
    \n\t\t :set err \"true\"}\r\
    \n     :put \"Adding new client IPSec peer (initiator)\"\r\
    \n     :do {/ip ipsec peer add address=\$Hostname exchange-mode=ike2 name=\
    \"peer-\$Hostname\" profile=\"profile-\$Hostname\"} on-error={\r\
    \n\t     :put \"Error: cannot add new client IPSec peer peer-\$Hostname (i\
    nitiator)\"\r\
    \n\t\t :set err \"true\"}\r\
    \n\t :put \"Setting up new IPSec proposal (phase 2)\"\r\
    \n\t :do {/ip ipsec proposal add auth-algorithms=sha512,sha256,sha1 enc-al\
    gorithms=aes-256-cbc,aes-256-ctr,aes-256-gcm,aes-192-ctr,aes-192-gcm,aes-1\
    28-cbc,aes-128-ctr,aes-128-gcm lifetime=8h name=\"proposal-\$Hostname\" pf\
    s-group=none} on-error={\r\
    \n\t     :put \"Error: cannot set up new IPSec proposal proposal-\$Hostnam\
    e (phase 2)\"\r\
    \n\t\t :set err \"true\"}\r\
    \n\t :put \"Adding new IPSec policy group\"\r\
    \n\t :do {/ip ipsec policy group add name=\"group-\$Hostname\"} on-error={\
    \r\
    \n\t     :put \"Error: cannot add new IPSec policy group group-\$Hostname\
    \"\r\
    \n\t\t :set err \"true\"} \r\
    \n\t :put \"Adding new IPSec policy template\"\r\
    \n\t :do {/ip ipsec policy add comment=\"policy template \$Hostname\" dst-\
    address=\"0.0.0.0/0\" group=\"group-\$Hostname\" proposal=\"proposal-\$Hos\
    tname\" src-address=10.0.88.0/24 template=yes} on-error={\r\
    \n\t     :put \"Error: cannot add new IPSec policy template\"\r\
    \n\t\t :set err \"true\"} \r\
    \n\t :put \"Assembling clients IPSec identity\"\r\
    \n\t :do {/ip ipsec identity\r\
    \n\t        add auth-method=digital-signature \\\r\
    \n\t\t\tcertificate=\"\$PeerCertFile_0\" generate-policy=port-strict mode-\
    config=request-only \\\r\
    \n\t\t\tmy-id=\"user-fqdn:\$PeerName@\$Hostname\" \\\r\
    \n\t\t\tpeer=\"peer-\$Hostname\" \\\r\
    \n\t\t\tpolicy-template-group=\"group-\$Hostname\" \\\r\
    \n\t\t\tremote-id=\"fqdn:\$Hostname\" } on-error={\r\
    \n\t            :put \"Error: cannot add new client\92s IPSec identity\"\r\
    \n\t\t        :set err \"true\"} \t \r\
    \n\t :if (\$err = \"true\") do={:error \"Cannot create peer\"}\r\
    \n}\r\
    \n:if (variant = 2) do={}\r\
    \n\r\
    \n:put \"Script finished\"\r\
    \n"


File: /IKEv2-remove-peer-autoscript.rsc
/system script
add dont-require-permissions=no name=IKEv2-remove-peer-autoscript owner=admin \
    policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    source=":local Hostname \"my.domain.com\"\r\
    \n:local PeerName \"UserName\"\r\
    \n\r\
    \n:log warn \" ============== Starting script ============== \"\r\
    \n\r\
    \n:log info \" ======== Revoke certificate PeerName@\$Hostname ======== \"\
    \r\
    \n:do {/certificate issued-revoke [ find name=\"\$PeerName@\$Hostname\"];}\
    \_on-error={:log error \"!!! cannot revoke certificate \$PeerName@\$Hostna\
    me\"}\r\
    \n:do {/file remove \"cert_export_\$PeerName@\$Hostname.p12\"} on-error={:\
    log error \"!!! cannot remove file cert_export_\$PeerName@\$Hostname.p12.\
    \" }\r\
    \n\r\
    \n:log info \" ======== Remove  IPSec identities dlya kazhdogo klienta ===\
    ===== \"\r\
    \n/ip ipsec identity\r\
    \nremove [find remote-id~\"\$PeerName\"]\r\
    \n\r\
    \n:log warn \" ============== Script finished ============== \"\r\
    \n"


File: /IKEv2-server-autoscript.rsc
/system script
add dont-require-permissions=no name=IKEv2 owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    local variant\r\
    \n:local Hostname\r\
    \n:local IPaddress \r\
    \n:local Country\r\
    \n:local State\r\
    \n:local CertFile\r\
    \n:local arrayRollback [ :toarray \"\" ]\r\
    \n:local err \"false\"\r\
    \n:local PeerName\r\
    \n:local Password\r\
    \n\r\
    \n:local inputFunc do={:put \$1;:return}\r\
    \n:local checkHostnameFunc do={\r\
    \n    :local hostname \$1\r\
    \n    :if ([:len \$hostname]=0) do={\r\
    \n         :if ([/ip cloud get value-name=ddns-enabled] = false) do {\r\
    \n             /ip cloud set ddns-enabled=yes\r\
    \n             :delay 10s\r\
    \n         } \r\
    \n    :set \$hostname [/ip cloud get value-name=dns-name]\r\
    \n\t:if ([:len \$hostname]=0) do={\r\
    \n         :return \"\"\r\
    \n\t    }\r\
    \n    }\r\
    \n\treturn \$hostname\r\
    \n}\r\
    \n:local checkIpAddressFunc do={\r\
    \n    :if ([:tostr \$1] = [:toip \$1]) do={:return \$1} else={:return \"\"\
    }\r\
    \n}\r\
    \n\r\
    \n:put (\"\\r\\n\\\r\
    \n     ###################################################################\
    ###########\\r\\n\\\r\
    \n     Welcome to IPSec-auto-script. This script will install and setup IP\
    Sec server.\\r\\n\\\r\
    \n     ###################################################################\
    ###########\\r\\n\\r\\n\")\r\
    \n:put (\"What would you like to do\\\?\\r\\n\\\r\
    \n       1. Install IKE v2 server\\r\\n\\\r\
    \n       2. Create peer\\r\\n\\\r\
    \n\t   3. Revoke peer\\r\\n\\\r\
    \n\t   4. Remove IKE v2 server\\r\\n\")\r\
    \n:set variant [\$inputFunc \"Choose corresponding number.\"]\r\
    \n:if (variant = 1) do={\r\
    \n    :put \"\"\r\
    \n    :set Hostname  [\$inputFunc \"Input domain name of this server. E.g.\
    : 123456789012.sn.mynetname.net. Leave it empty if you want this script to\
    \_find it out from /ip cloud settings\"]\r\
    \n\t:set \$Hostname [\$checkHostnameFunc \$Hostname]\r\
    \n\t:if (\$Hostname = \"\") do={\r\
    \n\t     :put \"Error: cannot get DNS name\"\r\
    \n         :set err \"true\"\r\
    \n\t    }\r\
    \n\tdo {\r\
    \n\t    :put \"\"\r\
    \n\t    :set IPaddress [\$inputFunc \"Input IP address of this server. E.g\
    .: 10.20.30.40. Leave it empty if you want this script to find it out by r\
    esolving Hostname\"]\r\
    \n\t\t:if ([:len \$IPaddress]=0) do={\r\
    \n             do {:set \$IPaddress [:resolve \$Hostname]} on-error={\r\
    \n\t             :put \"Error: cannot resolve DNS name\"\r\
    \n\t            }\r\
    \n            }\r\
    \n\t\t:set IPaddress [\$checkIpAddressFunc \$IPaddress]\r\
    \n\t\t} while=( [:len \$IPaddress]=0 )\r\
    \n\t:put \"\"\r\
    \n\t:set Country   [\$inputFunc \"Input Country of server location. E.g.: \
    DE\"]\r\
    \n\t:put \"\"\r\
    \n\t:set State     [\$inputFunc \"Input State of server location. E.g.: Fr\
    ankfurt\"]\r\
    \n    \r\
    \n\t:put \"\\r\\nChecking if script can use given parameters\\r\\n\"\r\
    \n\t:if ([/certificate find name=\"CA.\$Hostname\"] != \"\") do={\r\
    \n             :put \"Error: certificate CA.\$Hostname already exists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: certificate name CA.\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/certificate find name=\"\$Hostname\"] != \"\") do={\r\
    \n             :put \"Error: certificate \$Hostname already exists\"\r\
    \n\t\t     :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: certificate name \$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/certificate find name=\"~client-template@\$Hostname\"] != \"\
    \") do={\r\
    \n             :put \"Error: certificate template ~client-template@\$Hostn\
    ame already exists\"\r\
    \n\t\t     :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: certificate template name ~client-template@\$Hos\
    tname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/file find name=\"CA.\$Hostname.crt\"] != \"\") do={\r\
    \n             :put \"Error: file CA.\$Hostname.crt already exists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: file name CA.\$Hostname.crt\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/int bridge find name=\"bridge-vpn\"] != \"\") do={\r\
    \n             :put \"Error: bridge bridge-vpn already exists\"\r\
    \n\t\t     :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: bridge name bridge-vpn\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip address find address=\"10.0.88.1/24\"] != \"\") do={\r\
    \n             :put \"Error: ip address 10.0.88.1/24 already exists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ip address 10.0.88.1/24\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip pool find name=\"pool-\$Hostname\"] != \"\") do={\r\
    \n             :put \"Error: ip pool pool-\$Hostname already exists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ip pool name pool-\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec mode-config find name=\"modeconf-\$Hostname\"] != \"\
    \") do={\r\
    \n             :put \"Error: mode-config modeconf-\$Hostname already exist\
    s\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n              :put \"OK: mode-config name modeconf-\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec profile find name=\"profile-\$Hostname\"] != \"\") d\
    o={\r\
    \n             :put \"Error: ipsec profile profile-\$Hostname already exis\
    ts\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ipsec profile name profile-\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec peer find name=\"peer-\$IPaddress\"] !=\"\") do={\r\
    \n            :put \"Error: ipsec peer peer-\$IPaddress already exists\"\r\
    \n            :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ipsec peer name peer-\$IPaddress\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec proposal find name=\"proposal-\$Hostname\"] != \"\")\
    \_do={\r\
    \n             :put \"Error: ipsec proposal proposal-\$Hostname already ex\
    ists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ipsec proposal name proposal-\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec policy group find name=\"group-\$Hostname\"] != \"\"\
    ) do={\r\
    \n             :put \"Error: ipsec policy group group-\$Hostname already e\
    xists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ipsec policy group name group-\$Hostname\"\r\
    \n        }\r\
    \n\r\
    \n    :if ([/ip ipsec policy find dst-address=\"10.0.88.0/24\" ] != \"\") \
    do={\r\
    \n         :put \"Error: ipsec policy for dst-address=10.0.88.0/24 already\
    \_exists\"\r\
    \n         :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: ipsec policy for dst-address=10.0.88.0/24\"\r\
    \n        }\r\
    \n\t:if (\$err = \"true\") do={:error \"\\r\\nPrecheck failed\"} else={:pu\
    t \"\\r\\nPrecheck OK\"}\r\
    \n\t:put \"\\r\\n\"\r\
    \n\t:put \"Hostname is: \$Hostname\"\r\
    \n\t:put \"IP address is: \$IPaddress\"\r\
    \n\t:put \"Country is: \$Country\"\r\
    \n\t:put \"State is: \$State\"\r\
    \n\t:put \"\"\r\
    \n\t:if ([\$inputFunc \"Continue\? [y/n]\"]=\"n\") do={:error \"Script sto\
    pped by user request\"}\r\
    \n    :put \"\\r\\nGenerating CA SSL certificate\"\r\
    \n    :do {/certificate \r\
    \n         add name=\"CA.\$Hostname\" country=\$Country state=\$State loca\
    lity=City \\\r\
    \n         organization=\"\$Hostname\" common-name=\"CA.\$Hostname\"  subj\
    ect-alt-name=\"DNS:CA.\$Hostname\"  \\\r\
    \n         key-size=4096 days-valid=3650 trusted=yes key-usage=digital-sig\
    nature,key-encipherment,data-encipherment,key-cert-sign,crl-sign\r\
    \n\t\t :set arrayRollback ( \$arrayRollback, \":do {/certificate remove [ \
    find name=\\\"CA.\$Hostname\\\"]} on-error={} \" )\r\
    \n\t\t } on-error={\r\
    \n             :put \"Error: Cannot add certificate CA.\$Hostname\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n        }\r\
    \n\r\
    \n    :put \"Signing CA SSL certificate (Certificate Authority)\"\r\
    \n    :delay 1\r\
    \n    :do {/certificate sign \"CA.\$Hostname\"} on-error={\r\
    \n         :put \"Error: Cannot sign CA.\$Hostname\"\r\
    \n         :set err \"true\"\r\
    \n\t\t :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Generating server SSL certificate\"\r\
    \n    :do {/certificate \r\
    \n        add name=\"\$Hostname\" country=\$Country state=\$State locality\
    =\"City\" organization=\"\$Hostname\" common-name=\"\$Hostname\" \\\r\
    \n        subject-alt-name=\"DNS:\$Hostname\" key-size=2048 days-valid=109\
    5 trusted=yes key-usage=tls-server\r\
    \n\t\t:set arrayRollback ( \$arrayRollback, \":do {/certificate remove [ f\
    ind name=\\\"\$Hostname\\\"]} on-error={} \" )\r\
    \n\t\t\t} on-error={\r\
    \n                 :put \"Error: Cannot add certificate \$Hostname\"\r\
    \n                 :set err \"true\"\r\
    \n\t\t         :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Signing server certificate with CA.\$Hostname\"\r\
    \n    :delay 1\r\
    \n    :do {/certificate sign \"\$Hostname\" ca=\"CA.\$Hostname\"} on-error\
    ={\r\
    \n         :put \"Cannot sign \$Hostname with CA.\$Hostname\"\r\
    \n         :set err \"true\"\r\
    \n\t\t :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Creating template for signing clients\"\r\
    \n    :do {/certificate\r\
    \n       add name=\"~client-template@\$Hostname\" country=\$Country state=\
    \$State locality=\"City\" organization=\"\$Hostname\" common-name=\"~clien\
    t-template@\$Hostname\" \\\r\
    \n       subject-alt-name=\"email:~client-template@\$Hostname\" key-size=2\
    048 days-valid=365 trusted=yes key-usage=tls-client\r\
    \n\t   :set arrayRollback ( \$arrayRollback, \":do {/certificate remove [ \
    find name~\\\"~client-template\\\"]} on-error={} \" )\r\
    \n\t\t\t} on-error={\r\
    \n                 :put \"Cannot add client-template@\$Hostname\"\r\
    \n                 :set err \"true\"\r\
    \n\t\t         :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Exporting CA certificate to file CA.\$Hostname\"\r\
    \n    :do {/certificate export-certificate \"CA.\$Hostname\" type=pem file\
    -name=\"CA.\$Hostname\"} on-error={\r\
    \n         :put \"Cannot export-certificate CA.\$Hostname\"\r\
    \n         :set err \"true\"\r\
    \n\t\t :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create IKEv2 server\"\r\
    \n    :do {/interface bridge add name=\"bridge-vpn\"\r\
    \n\t\t:set arrayRollback ( \$arrayRollback, \"/interface bridge remove [fi\
    nd name=\\\"bridge-vpn\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"bridge bridge-vpn already exists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n    :do {/ip address add address=10.0.88.1/24 interface=\"bridge-vpn\" n\
    etwork=10.0.88.0\r\
    \n\t\t:set arrayRollback ( \$arrayRollback, \"/ip address remove [find add\
    ress=\\\"10.0.88.1/24\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"Cannot add ip address (10.0.88.1/24) on interface br\
    idge-vpn\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n    :do {/ip pool add name=\"pool-\$Hostname\" ranges=10.0.88.2-10.0.88.\
    254\r\
    \n\t\t:set arrayRollback ( \$arrayRollback, \"/ip pool remove [find name=\
    \\\"pool-\$Hostname\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"IP pool (10.0.88.2-10.0.88.254) already exists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new IPSec mode config\"\r\
    \n    :do {/ip ipsec mode-config add address-pool=\"pool-\$Hostname\" addr\
    ess-prefix-length=32 name=\"modeconf-\$Hostname\" split-include=0.0.0.0/0 \
    static-dns=10.0.88.1 system-dns=no\r\
    \n\t    :set arrayRollback ( \$arrayRollback, \"/ip ipsec mode-config remo\
    ve [ find name=\\\"modeconf-\$Hostname\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"Cannot create modeconf-\$Hostname or it already exis\
    ts\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new IPSec peer profile (phase 1)\"\r\
    \n    :do {/ip ipsec profile add dh-group=modp2048,modp1536,modp1024 enc-a\
    lgorithm=aes-256,aes-192,aes-128 hash-algorithm=sha256 name=\"profile-\$Ho\
    stname\" nat-traversal=yes proposal-check=obey \r\
    \n\t    :set arrayRollback ( \$arrayRollback, \"/ip ipsec profile remove  \
    [ find name=\\\"profile-\$Hostname\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"Cannot create profile-\$Hostname or it already exist\
    s\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new IPSec peer using public IP address (mode IKE2)\"\r\
    \n    :do {/ip ipsec peer add exchange-mode=ike2 address=0.0.0.0/0 local-a\
    ddress=\"\$IPaddress\" name=\"peer-\$IPaddress\" passive=yes send-initial-\
    contact=yes profile=\"profile-\$Hostname\"\r\
    \n\t   :set arrayRollback ( \$arrayRollback, \"/ip ipsec peer remove  [ fi\
    nd name=\\\"peer-\$IPaddress\\\"]\" )\r\
    \n\t   } on-error={\r\
    \n             :put \"Cannot create ipsec peer-\$IPaddress or it already e\
    xists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new IPSec proposal (phase 2)\"\r\
    \n    :do {/ip ipsec proposal add auth-algorithms=sha512,sha256,sha1 enc-a\
    lgorithms=aes-256-cbc,aes-256-ctr,aes-256-gcm,aes-192-ctr,aes-192-gcm,aes-\
    128-cbc,aes-128-ctr,aes-128-gcm lifetime=8h name=\"proposal-\$Hostname\" p\
    fs-group=none\r\
    \n\t    :set arrayRollback ( \$arrayRollback, \"/ip ipsec proposal remove \
    [find name=\\\"proposal-\$Hostname\\\"]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"Cannot create ipsec proposal-\$Hostname or it alread\
    y exists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new IPSec policy group\"\r\
    \n    :do {/ip ipsec policy group add name=\"group-\$Hostname\"\r\
    \n\t   :set arrayRollback ( \$arrayRollback, \"/ip ipsec policy group remo\
    ve [find name=\\\"group-\$Hostname\\\"]\" )\r\
    \n\t   } on-error={\r\
    \n             :put \"Cannot create policy group-\$Hostname or it already \
    exists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\r\
    \n    :put \"Create new template IPSec policy\"\r\
    \n    :do {/ip ipsec policy add dst-address=10.0.88.0/24 group=\"group-\$H\
    ostname\" proposal=\"proposal-\$Hostname\" src-address=0.0.0.0/0 template=\
    yes\r\
    \n\t    :set arrayRollback ( \$arrayRollback, \"/ip ipsec policy remove [f\
    ind dst-address=10.0.88.0/24 group=\\\"group-\$Hostname\\\" proposal=\\\"p\
    roposal-\$Hostname\\\" src-address=0.0.0.0/0]\" )\r\
    \n\t\t} on-error={\r\
    \n             :put \"Cannot create ipsec policy dst-address=10.0.88.0/24 \
    src-address=0.0.0.0/0 or it already exists\"\r\
    \n             :set err \"true\"\r\
    \n\t\t     :return \"\"\r\
    \n    }\r\
    \n\t\r\
    \n    :local scr\r\
    \n\t:local ln\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":if ([\\\$inputFunc \\\"Contin\
    ue\? [y/n]\\\"]=\\\"n\\\") do={:error \\\"Script stopped by user request\\\
    \"}\" )\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":local inputFunc do={:put \\\$\
    1;:return}\")\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":put \\\"This script will remo\
    ve IPSec IKEv2. Make sure you already removed existing peers.\\\" \" )\r\
    \n\t:for x from=[:len \$arrayRollback] to=0 step=-1 do={\r\
    \n\t     :set ln [:pick \$arrayRollback \$x] \r\
    \n\t\t :if ([:len \$ln]!=0) do={:set scr (\$scr.\"\\r\\n\".\$ln)}\r\
    \n\t}\r\
    \n\t\r\
    \n    /system script remove [find name=\"IKEv2-rollback\"]\r\
    \n    /system script\r\
    \n         add dont-require-permissions=no name=\"IKEv2-rollback\" owner=a\
    dmin policy=\\\r\
    \n         ftp,reboot,read,write,policy,test,password,sniff,sensitive,romo\
    n source=\"\$scr\"\r\
    \n\t:put \"\\r\\nGenerated IKEv2-rollback script.\"\r\
    \n\t}\r\
    \n\r\
    \n:if (variant = 2) do={\r\
    \n    :put \"\"\r\
    \n    :set Hostname  [\$inputFunc \"Input domain name of this server. Leav\
    e it empty if you want to use /ip cloud DNS name\"]\r\
    \n\t:set \$Hostname [\$checkHostnameFunc \$Hostname]\r\
    \n\t:if (\$Hostname = \"\") do={\r\
    \n\t     :put \"Error: cannot get DNS name of this router.\"\r\
    \n         :set err \"true\"\r\
    \n\t    }\r\
    \n\t:put \"\"\r\
    \n\t:do {\r\
    \n\t    :set IPaddress [\$inputFunc \"Input IP address of this server. E.g\
    .: 10.20.30.40. Leave it empty if you want this script to find it out by r\
    esolving Hostname\"]\r\
    \n\t\t:if ([:len \$IPaddress]=0) do={\r\
    \n             do {:set \$IPaddress [:resolve \$Hostname]} on-error={\r\
    \n\t             :put \"Error: cannot resolve DNS name\"\r\
    \n\t            }\r\
    \n            }\r\
    \n\t\t:set IPaddress [\$checkIpAddressFunc \$IPaddress]\r\
    \n\t\t} while=( [:len \$IPaddress]=0 )\r\
    \n    :put \"\"\r\
    \n    :set PeerName [\$inputFunc \"Input peer name.\"]\r\
    \n\t:put \"\"\r\
    \n\t:do {\r\
    \n         :set Password [\$inputFunc \"Input password to encript certific\
    ate file (length should be more than 7 digits).\"]\r\
    \n         } while=( [:len \$Password]<7 )\r\
    \n    :put \"\\r\\nChecking if script can use given parameters\\r\\n\"\r\
    \n\t\r\
    \n\t:if ([/certificate find name=\"\$PeerName@\$Hostname\"] != \"\") do={\
    \r\
    \n             :put \"Error: certificate \$PeerName@\$Hostname already exi\
    sts\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: certificate name \$PeerName@\$Hostname\"\r\
    \n        }\r\
    \n\t:if ([/certificate find name=\"~client-template@\$Hostname\"] = \"\") \
    do={\r\
    \n             :put \"Error: there's no template ~client-template@\$Hostna\
    me\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: template ~client-template@\$Hostname\"\r\
    \n        }\r\
    \n\t:if ([/certificate find name=\"CA.\$Hostname\"] = \"\") do={\r\
    \n             :put \"Error: there's no CA.\$Hostname certificate\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: CA.\$Hostname certificate\"\r\
    \n        }\r\
    \n    :if ([/file find name=\"\$PeerName@\$Hostname.crt\"] != \"\") do={\r\
    \n             :put \"Error: file CA.\$Hostname.crt already exists\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: file name CA.\$Hostname.crt\"\r\
    \n        }\r\
    \n\t:if (\$err = \"true\") do={:error \"\\r\\nPrecheck failed\"} else={:pu\
    t \"\\r\\nPrecheck OK\"}\r\
    \n\t:put \"\\r\\n\"\r\
    \n\t:put \"Hostname is: \$Hostname\"\r\
    \n\t:put \"PeerName is: \$PeerName\"\r\
    \n\t:put \"Password is: \$Password\"\r\
    \n\t:put \"\"\r\
    \n\t:if ([\$inputFunc \"Continue\? [y/n]\"]=\"n\") do={:error \"Script sto\
    pped by user request\"}\r\
    \n    \r\
    \n\t:put \"Creating client certificate from template\"\r\
    \n    :do {/certificate \r\
    \n         add copy-from=\"~client-template@\$Hostname\" name=\"\$PeerName\
    @\$Hostname\" common-name=\"\$PeerName@\$Hostname\" subject-alt-name=\"ema\
    il:\$PeerName@\$Hostname\"\r\
    \n\t\t :set arrayRollback ( \$arrayRollback, \":do {/certificate issued-re\
    voke [ find name=\\\"\$PeerName@\$Hostname\\\"]} on-error={}\" )\r\
    \n        } on-error={\r\
    \n             :put \"Script error: cannot copy-from ~client-template@\$Ho\
    stname certificate\"\r\
    \n             :set err \"true\"\r\
    \n        }    \r\
    \n\t:put \"Signing client certificate with CA.\$Hostname\"\r\
    \n    :do {/certificate sign \"\$PeerName@\$Hostname\" ca=\"CA.\$Hostname\
    \" } on-error={\r\
    \n             :put \"Script error: cannot sign client certificate \$PeerN\
    ame@\$Hostname\"\r\
    \n             :set err \"true\"\r\
    \n        } \r\
    \n    :delay 1\r\
    \n\t:put (\"Exporting client certificate and private key\")\t\t\r\
    \n    :do {/certificate export-certificate \"\$PeerName@\$Hostname\" type=\
    pkcs12 export-passphrase=\"\$Password\" file-name=\"\$PeerName@\$Hostname\
    \"} on-error={\r\
    \n             :put \"Script error: cannot create export-certificate \$Pee\
    rName@\$Hostname\"\r\
    \n             :set err \"true\"\r\
    \n        }\r\
    \n\t:put \"Assembling ipsec identity\"\t\t\r\
    \n    :do {/ip ipsec identity\r\
    \n         add auth-method=digital-signature certificate=\"\$Hostname\" re\
    mote-certificate=\"\$PeerName@\$Hostname\" generate-policy=port-strict \\\
    \r\
    \n         match-by=certificate mode-config=\"modeconf-\$Hostname\" peer=\
    \"peer-\$IPaddress\" policy-template-group=\"group-\$Hostname\" remote-id=\
    \"user-fqdn:\$PeerName@\$Hostname\"\r\
    \n\t\t :set arrayRollback ( \$arrayRollback, \":do {/ip ipsec identity rem\
    ove [find remote-id~\\\"\$PeerName@\$Hostname\\\"]} on-error={}\" )\r\
    \n        } on-error={\r\
    \n\t         :put \"Script error: cannot create ipsec identity\"\r\
    \n             :set err \"true\"\r\
    \n        }\r\
    \n\t:if (\$err=\"true\") do={:put \"\\r\\nThe were errors creating peer.\"\
    }\r\
    \n\t:local scr\r\
    \n\t:local ln\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":if ([\\\$inputFunc \\\"Contin\
    ue\? [y/n]\\\"]=\\\"n\\\") do={:error \\\"Script stopped by user request\\\
    \"}\" )\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":local inputFunc do={:put \\\$\
    1;:return}\")\r\
    \n\t:set arrayRollback ( \$arrayRollback, \":put \\\"This script will remo\
    ve \$PeerName@\$Hostname from this server\\\" \" )\r\
    \n\t:for x from=[:len \$arrayRollback] to=0 step=-1 do={\r\
    \n\t     :set ln [:pick \$arrayRollback \$x] \r\
    \n\t\t :if ([:len \$ln]!=0) do={:set scr (\$scr.\"\\r\\n\".\$ln)}\r\
    \n\t}\r\
    \n\r\
    \n\t/system script remove [find name=\"\$PeerName-rollback\"]\r\
    \n    /system script\r\
    \n         add dont-require-permissions=no name=\"\$PeerName-rollback\" ow\
    ner=admin policy=\\\r\
    \n         ftp,reboot,read,write,policy,test,password,sniff,sensitive,romo\
    n source=\"\$scr\"\r\
    \n\t:put \"\\r\\nGenerated \$PeerName-rollback script.\"\r\
    \n\t:put \"\\r\\nCopy certificate file to a new peer device.\"\r\
    \n\t}\r\
    \n:if (variant = 3) do={\r\
    \n\t:put \"\"\r\
    \n    :set \$Hostname  [\$inputFunc \"Input domain name of this server. Le\
    ave it empty if you want to use /ip cloud DNS name\"]\r\
    \n\t:set \$Hostname [\$checkHostnameFunc \$Hostname]\r\
    \n\t:if (\$Hostname = \"\") do={\r\
    \n\t         :put \"Error: cannot get DNS name of this router.\"\r\
    \n             :set err \"true\"\r\
    \n\t    }\r\
    \n\t:put \"\"\r\
    \n    :set PeerName [\$inputFunc \"Input peer name you want to remove.\"]\
    \r\
    \n\t:put \"\"\r\
    \n\t:put \"\\r\\nChecking if script can use given parameters\\r\\n\"\r\
    \n\t:if ([/certificate find name=\"\$PeerName@\$Hostname\"] = \"\") do={\r\
    \n             :put \"Error: there's no such peer \$PeerName@\$Hostname\"\
    \r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: peer name \$PeerName@\$Hostname\"\r\
    \n        }\r\
    \n\t:if ([/ip ipsec identity find remote-id~\"\$PeerName@\$Hostname\"] = \
    \"\") do={\r\
    \n             :put \"Error: there's no such identity for \$PeerName@\$Hos\
    tname\"\r\
    \n             :set err \"true\"\r\
    \n        } else {\r\
    \n             :put \"OK: identity for peer name \$PeerName@\$Hostname\"\r\
    \n        }\r\
    \n\t\t\r\
    \n\t:if (\$err = \"true\") do={:error \"\\r\\nPrecheck failed\"} else={:pu\
    t \"Precheck OK\"}\r\
    \n\t:put \"\\r\\n\"\r\
    \n\t:if ([\$inputFunc \"Remove peer\? [y/n]\"]=\"n\") do={:error \"Script \
    stopped by user request\"}\r\
    \n\t:do {/certificate issued-revoke [find name=\"\$PeerName@\$Hostname\"]}\
    \_on-error={}\r\
    \n\t:do {/ip ipsec identity remove [find remote-id~\"\$PeerName@\$Hostname\
    \"]} on-error={}\r\
    \n\t}\r\
    \n:if (variant = 4) do={\r\
    \n\t:put \"\\r\\nChecking if script can use given parameters\\r\\n\"\r\
    \n\t:if ([/system script find name=\"IKEv2-rollback\"] = \"\") do={\r\
    \n             :put \"Error: cannot find rollback script IKEv2-rollback\"\
    \r\
    \n        } else {\r\
    \n             :put \"OK: rollback script IKEv2-rollback found.\"\r\
    \n\t\t\t :do {/system script run [find name=\"IKEv2-rollback\"]} on-error=\
    {:error \"Error: script error in IKEv2-rollback\"}\r\
    \n        }\r\
    \n\t}\r\
    \n\t\r\
    \n\t:put \"\\r\\nScript finished.\"\r\
    \n}"


File: /IKEv2-strongswan-peer-autoscript.rsc
/system script
add dont-require-permissions=no name=IKEv2-strongswan-peer-autoscript owner=\
    admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source=":\
    local PeerCertFile\r\
    \n:local Password\r\
    \n:local ServerAddress\r\
    \n:local PeerName\r\
    \n:local variant\r\
    \n:local err \"false\"\r\
    \n:local inputFunc do={:put \$1;:return}\r\
    \n\r\
    \n:put \"#################################################################\
    #############\"\r\
    \n:put \"Welcome to IPSec-Strongswan-auto-script.\"\r\
    \n:put \"This script will setup IPSec IKEv2 StrongSwan peer.\"\r\
    \n:put \"#################################################################\
    #############\\r\\n\"\r\
    \n:put \"What would you like to do\\\?\"\r\
    \n:put \"1. Create peer\"\r\
    \n:put \"2. Remove peer\"\r\
    \n:put \"3. Exit\"\r\
    \n\r\
    \n:set variant [\$inputFunc \"Choose corresponding number.\"]\r\
    \n:if (variant = 1) do={\r\
    \n\t:set ServerAddress  [\$inputFunc \"Input domain name or IP address of \
    IPSec IKEv2 server you want to connect to.\"]\r\
    \n\t:if (\$ServerAddress = \"\") do={:error \"Error: name or IP address ca\
    nnot be empty\"}\r\
    \n\t:set PeerName [\$inputFunc \"Input PeerName. Usually this name indicat\
    es VPN server's name or IP address. E.g.: VPN-server or 1.2.3.4\" ]\r\
    \n\t:if (\$PeerName = \"\") do={:error \"Error: PeerName cannot be empty\"\
    \_} \r\
    \n\t:set PeerCertFile [\$inputFunc \"Input peer certificate filename you u\
    ploaded from server. E.g.: PeerName@ServerAddress.p12\"]\r\
    \n\t:if (\$PeerCertFile = \"\") do={:error \"Error: certificate filename c\
    annot be empty\" } \r\
    \n\t:set Password [\$inputFunc \"Input passphrase to import certificate fr\
    om file\"]\r\
    \n\t:if (\$Password = \"\") do={:error \"Error: Password cannot be empty\"\
    \_} \r\
    \n\t\t \r\
    \n\t:put \"\\r\\nCheck if script can use given parameters\"\r\
    \n\t\t \r\
    \n    :if ([/file find name=\"\$PeerCertFile\"] = \"\") do={\r\
    \n\t\t\t  :put \"Error: cannot find file \$PeerCertFile\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/certificate find name=\"\$PeerCertFile_0\"] != \"\") do={\r\
    \n\t\t\t  :put \"Error: certificate \$PeerCertFile_0 already exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/certificate find name=\"\$PeerCertFile_1\"] != \"\") do={\r\
    \n\t\t\t  :put \"Error: certificate \$PeerCertFile_1 already exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec profile find name=\"prof-\$PeerName-autoscript-vpn\"] \
    != \"\") do={\r\
    \n\t\t      :put \"Error: ipsec profile prof-\$PeerName-autoscript-vpn alr\
    eady exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec proposal find name=\"prop-\$PeerName-autoscript-vpn\"]\
    \_!= \"\") do={\r\
    \n\t\t      :put \"Error: ipsec proposal prop-\$PeerName-autoscript-vpn al\
    ready exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec policy group find name=\"group-\$PeerName-autoscript-v\
    pn\"] != \"\") do={\r\
    \n\t\t      :put \"Error: ipsec policy group group-\$PeerName-autoscript-v\
    pn already exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec policy find dst-address=\"0.0.0.0/0\" src-address=\"0.\
    0.0.0/0\" group=\"group-\$PeerName-autoscript-vpn\"] != \"\") do={\r\
    \n\t\t      :put \"Error: ipsec policy for dst-address=0.0.0.0/0 already e\
    xists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec mode-config find name=\"mconf-\$PeerName-autoscript-vp\
    n\"] != \"\") do={\r\
    \n\t\t\t  :put \"Error: mode-config mconf-\$PeerName-autoscript-vpn alread\
    y exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec peer find name=\"peer-\$PeerName-autoscript-vpn\"] !=\
    \"\") do={\r\
    \n\t\t      :put \"Error: ipsec peer peer-\$PeerName-autoscript-vpn alread\
    y exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if ([/ip ipsec identity find name=\"identity-\$PeerName-autoscript-vp\
    n\"] !=\"\") do={\r\
    \n\t\t      :put \"Error: ipsec identity identity-\$PeerName-autoscript-vp\
    n already exists\"\r\
    \n\t\t\t  :set err \"true\"\r\
    \n\t\t } \r\
    \n\t:if (\$err = \"true\") do={:error \"Precheck failed\"}\r\
    \n\t:put \"Precheck OK\"\r\
    \n\t:put \"\\r\\nStarting script\"\r\
    \n\t \r\
    \n\t:put \"Importing certificates\"\r\
    \n\t:do {/certificate import file-name=\$PeerCertFile passphrase=\$Passwor\
    d } on-error={}\r\
    \n\t:do {/certificate import file-name=\$PeerCertFile passphrase=\$Passwor\
    d } on-error={}\r\
    \n\t\r\
    \n\t:if ([/certificate find name=\"\$PeerCertFile_0\"] = \"\") do={ :error\
    \_\"Error: cannot import \$PeerCertFile_0\" }\r\
    \n\t:if ([/certificate find name=\"\$PeerCertFile_1\"] = \"\") do={ :error\
    \_\"Error: cannot import \$PeerCertFile_1\" }\r\
    \n \r\
    \n\t:do {/ip ipsec profile add name=\"prof-\$PeerName-autoscript-vpn\" } o\
    n-error={\r\
    \n\t     :put \"Error: cannot add profile prof-\$PeerName-autoscript-vpn\"\
    \r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec proposal add name=\"prop-\$PeerName-autoscript-vpn\" pf\
    s-group=none } on-error={\r\
    \n\t     :put \"Error: cannot add proposal prop-\$PeerName-autoscript-vpn\
    \"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec policy group add name=\"group-\$PeerName-autoscript-vpn\
    \" } on-error={\r\
    \n         :put \"Error: cannot add group group-\$PeerName-autoscript-vpn\
    \"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec proposal remove [find name=\"prop-\$PeerName-autoscr\
    ipt-vpn\" pfs-group=none]} on-error={}\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec policy add comment=\"IKEv2-strongswan-autoscript-vpn\" \
    group=\"group-\$PeerName-autoscript-vpn\" proposal=\"prop-\$PeerName-autos\
    cript-vpn\" template=yes dst-address=\"0.0.0.0/0\" src-address=\"0.0.0.0/0\
    \" } on-error={\r\
    \n\t     :put \"Error: cannot add policy\"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec policy group remove [find name=\"group-\$PeerName-au\
    toscript-vpn\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec proposal remove [find name=\"prop-\$PeerName-autoscr\
    ipt-vpn\" pfs-group=none]} on-error={}\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec mode-config add name=\"mconf-\$PeerName-autoscript-vpn\
    \" responder=no } on-error={\r\
    \n\t     :put \"Error: cannot add mode-config mconf-\$PeerName-autoscript-\
    vpn\"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec policy remove [find group=\"group-\$PeerName-autoscr\
    ipt-vpn\" proposal=\"prop-\$PeerName-autoscript-vpn\" template=yes dst-add\
    ress=\"0.0.0.0/0\" src-address=\"0.0.0.0/0\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec policy group remove [find name=\"group-\$PeerName-au\
    toscript-vpn\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec proposal remove [find name=\"prop-\$PeerName-autoscr\
    ipt-vpn\" pfs-group=none]} on-error={}\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec peer add comment=\"IKEv2-strongswan-autoscript-vpn\" ad\
    dress=\$ServerAddress exchange-mode=ike2 name=\"peer-\$PeerName-autoscript\
    -vpn\" profile=\"prof-\$PeerName-autoscript-vpn\" } on-error={\r\
    \n\t     :put \"Error: cannot add peer for \$ServerAddress\"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec mode-config remove [find name=\"mconf-\$PeerName-aut\
    oscript-vpn\" responder=no ] } on-error={}\r\
    \n\t\t :do {/ip ipsec policy remove [find group=\"group-\$PeerName-autoscr\
    ipt-vpn\" proposal=\"prop-\$PeerName-autoscript-vpn\" template=yes dst-add\
    ress=\"0.0.0.0/0\" src-address=\"0.0.0.0/0\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec policy group remove [find name=\"group-\$PeerName-au\
    toscript-vpn\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec proposal remove [find name=\"prop-\$PeerName-autoscr\
    ipt-vpn\" pfs-group=none]} on-error={}\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:do {/ip ipsec identity add comment=\"IKEv2-strongswan-autoscript-vpn\
    \" auth-method=digital-signature certificate=\"\$PeerCertFile_1\" generate\
    -policy=port-strict mode-config=\"mconf-\$PeerName-autoscript-vpn\" peer=\
    \"peer-\$PeerName-autoscript-vpn\" policy-template-group=\"group-\$PeerNam\
    e-autoscript-vpn\" } on-error={\r\
    \n\t     :put \"Error: cannot add identity for peer peer-\$PeerName-autosc\
    ript-vpn\"\r\
    \n\t\t :put \"Rollback previous action\"\r\
    \n\t\t :do {/ip ipsec peer remove [find address=\"\$ServerAddress/32\" exc\
    hange-mode=ike2 name=\"peer-\$PeerName-autoscript-vpn\" profile=\"prof-\$P\
    eerName-autoscript-vpn\" ] } on-error={}\r\
    \n\t\t :do {/ip ipsec mode-config remove [find name=\"mconf-\$PeerName-aut\
    oscript-vpn\" responder=no ] } on-error={}\r\
    \n\t\t :do {/ip ipsec policy remove [find group=\"group-\$PeerName-autoscr\
    ipt-vpn\" proposal=\"prop-\$PeerName-autoscript-vpn\" template=yes dst-add\
    ress=\"0.0.0.0/0\" src-address=\"0.0.0.0/0\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec policy group remove [find name=\"group-\$PeerName-au\
    toscript-vpn\"] } on-error={}\r\
    \n\t\t :do {/ip ipsec proposal remove [find name=\"prop-\$PeerName-autoscr\
    ipt-vpn\" pfs-group=none]} on-error={}\r\
    \n\t\t :do {/ip ipsec profile remove [find name=\"prof-\$PeerName-autoscri\
    pt-vpn\"]} on-error={}\r\
    \n\t     :set err \"true\"}\r\
    \n\t:if (\$err = \"true\") do={:error \"Script finished with errors\"}\r\
    \n\t:put \"Script finished\"\r\
    \n\r\
    \n\t/system script\r\
    \n\t:do {remove [find name=\"remove-peer-\$PeerName\"] } on-error={}\r\
    \n\t:do {add dont-require-permissions=no name=\"remove-peer-\$PeerName\" o\
    wner=admin policy=\\\r\
    \n\t\tftp,reboot,read,write,policy,test,password,sniff,sensitive,romon sou\
    rce=\"\\\r\
    \n\t\t\\n #This script removes automatically created peer\\r\\\r\
    \n\t\t\\n\\r\\\r\
    \n\t\t\\n:put \\\"Starting remove-peer-\$PeerName\\\"\\r\\\r\
    \n\t\t\\n/ip ipsec policy remove [find group=\\\"group-\$PeerName-autoscri\
    pt-vpn\\\" proposal=\\\"prop-\$PeerName-autoscript-vpn\\\" template=yes ds\
    t-address=\\\"0.0.0.0/0\\\" src-address=\\\"0.0.0.0/0\\\"]\\r\\\r\
    \n\t\t\\n/ip ipsec identity remove [find auth-method=digital-signature cer\
    tificate=\\\"\$PeerCertFile_1\\\" generate-policy=port-strict mode-config=\
    \\\"mconf-\$PeerName-autoscript-vpn\\\" peer=\\\"peer-\$PeerName-autoscrip\
    t-vpn\\\" policy-template-group=\\\"group-\$PeerName-autoscript-vpn\\\"]\\\
    r\\\r\
    \n\t\t\\n/ip ipsec peer remove [find address=\\\"\$ServerAddress/32\\\" ex\
    change-mode=ike2 name=\\\"peer-\$PeerName-autoscript-vpn\\\" profile=\\\"p\
    rof-\$PeerName-autoscript-vpn\\\" ]\\r\\\r\
    \n\t\t\\n/ip ipsec proposal remove [find name=\\\"prop-\$PeerName-autoscri\
    pt-vpn\\\" pfs-group=none]\\r\\\r\
    \n\t\t\\n/ip ipsec policy group remove [find name=\\\"group-\$PeerName-aut\
    oscript-vpn\\\"]\\r\\\r\
    \n\t\t\\n/ip ipsec profile remove [find name=\\\"prof-\$PeerName-autoscrip\
    t-vpn\\\"]\\r\\\r\
    \n\t\t\\n/ip ipsec mode-config remove [find name=\\\"mconf-\$PeerName-auto\
    script-vpn\\\" responder=no ]\\r\\\r\
    \n\t\t\\n/certificate remove [find name=\$PeerCertFile_1]\\r\\\r\
    \n\t\t\\n/certificate remove [find name=\$PeerCertFile_0]\\r\\\r\
    \n\t\t\\n/system script remove [find name=\\\"remove-peer-\$PeerName\\\"]\
    \\r\\\r\
    \n        \\n:put \\\"Script finished\\\"\" } on-error={\r\
    \n\t\t     put \"Error: cannot add rollback script removePeer\"}\r\
    \n\t:put \"Rollback script removePeer created\"\r\
    \n}"


File: /README.md
# IPSec-IKE-v2-auto-script
**These scripts create\remove IPsec IKE v2 server and\or peers.**

1. _"IKEv2-server-autoscript.rsc"_ is an interactive script to create and manage IKEv2 server on mikrotik router.
2. _"IKEv2-peer-autoscript.rsc"_ is used on client-side mikrotik to create peer.
3. _"IKEv2-remove-peer-autoscript.rsc"_ is used on client side mikrotik to remove peer.
4. _"IKEv2-strongswan-peer-autoscript.rsc"_ is used on client-side mikrotik to create peer working with [StrongSwan IPSec ikev2 server](https://github.com/hwdsl2/setup-ipsec-vpn).

**HOW TO...**

**How to setup an IKE v2 server and create CA certificate.**
1. Download [IKEv2-server-autoscript.rsc](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-server-autoscript.rsc) on your mikrotik router `/tool fetch url="https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-server-autoscript.rsc" mode=https dst-path=IKEv2-server-autoscript.rsc`. Also you may download [file](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-server-autoscript.rsc) manually and upload it to router.
2. Import script `/import IKEv2-server-autoscript.rsc`. You may also copy content of [this page](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-server-autoscript.rsc) and paste to a newly created script using GUI.
3. Run script via CLI. `/system script run IKEv2`
_**IMPORTANT: Script won't work if you run it via GUI.**_
4. Choose _**1. Install IKE v2 server**_ by typing "1"
5. Follow instructions on CLI

**How to create a client and create client's certificate. (Server-side)**
1. Run script via CLI. `/system script run IKEv2`
2. Choose _**2. Create peer**_ by typing "2"
3. Follow instructions on CLI

**How to setup a peer on client mikrotik router. (Peer-side)**
1. Download [IKEv2-peer-autoscript.rsc](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-peer-autoscript.rsc) on your mikrotik router `/tool fetch url="https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-peer-autoscript.rsc" mode=https dst-path=IKEv2-peer-autoscript.rsc`. Also you may download [file](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-peer-autoscript.rsc) manually and upload it to router.
2. Import script `/import IKEv2-peer-autoscript.rsc`. You may also copy content of [this page](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-peer-autoscript.rsc) and paste to a newly created script using GUI.
3. Run script via CLI. `/system script run IKEv2-peer`
_**IMPORTANT: Script won't work if you run it via GUI.**_
4. Choose _**1. Create peer**_ by typing "1"
5. Follow instructions on CLI

**How to setup strongswan client on mikrotik router.**
1. Download "IKEv2-strongswan-peer-autoscript.rsc" on your mikrotik router `/tool fetch url="https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-strongswan-peer-autoscript.rsc" mode=https dst-path=IKEv2-strongswan-peer-autoscript.rsc`. Also you may download file manually and upload it to router.
2. Import script `/import IKEv2-strongswan-peer-autoscript.rsc`. You may also copy content of [this page](https://raw.githubusercontent.com/mikrotik-user/IPSec-IKE-v2-auto-script/main/IKEv2-strongswan-peer-autoscript.rsc) and paste to a newly created script using GUI.
3. Make sure you uploaded certificate file on you router. Run script `/system script run IKEv2-strongswan-peer-autoscript`
4. Choose _**1. Create peer**_ by typing "1"
5. Script creates new peer and a new rollback script named "remove-peer-<peername>". You can use it to rollback modifications made by "IKEv2-strongswan-peer-autoscript".


