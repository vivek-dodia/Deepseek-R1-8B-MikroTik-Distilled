# Repository Information
Name: KMITL-Auto-Authen-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/KMITL-Auto-Authen-Mikrotik/
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
    │   │       ├── pack-d11414ee460d56109abc28a3c5ad546bbbd2684d.idx
    │   │       └── pack-d11414ee460d56109abc28a3c5ad546bbbd2684d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── Auto-Login-KMITL
    ├── LICENSE
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
	url = https://github.com/ouoam/KMITL-Auto-Authen-Mikrotik.git
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
0000000000000000000000000000000000000000 dce704abdce6a9e15caceb5d24704bc7d9898b6c vivek-dodia <vivek.dodia@icloud.com> 1738606059 -0500	clone: from https://github.com/ouoam/KMITL-Auto-Authen-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 dce704abdce6a9e15caceb5d24704bc7d9898b6c vivek-dodia <vivek.dodia@icloud.com> 1738606059 -0500	clone: from https://github.com/ouoam/KMITL-Auto-Authen-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 dce704abdce6a9e15caceb5d24704bc7d9898b6c vivek-dodia <vivek.dodia@icloud.com> 1738606059 -0500	clone: from https://github.com/ouoam/KMITL-Auto-Authen-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
dce704abdce6a9e15caceb5d24704bc7d9898b6c refs/remotes/origin/master


File: /.git\refs\heads\master
dce704abdce6a9e15caceb5d24704bc7d9898b6c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /Auto-Login-KMITL
# spell-checker:words totime tonum kmitl mikrotik

################################# Login script ################################
# spell-checker:ignore JSESSIONID Heatbeat
:if ([/system script find name="Auto-Login-KMITL"] != "") do={
  /system script set "Auto-Login-KMITL" name="AutoLogin-Login"; # rename old
}
:if ([/system script find name="AutoLogin-Login"] = "") do={
  /system script add name="AutoLogin-Login";
}
/system script set "AutoLogin-Login" policy=policy,read,test,write source={
:log debug "Auto-Login: Logging in...";
global ParseJSON;
local isRunUtility false;
if (!any $ParseJSON) do={
  /system script run "AutoLogin-Utility";
  :set isRunUtility true;
}
:local config [:parse (":return {" . [/system script get AutoLogin-Config source] . "};")]
:local account [$config];
:local serverIP;
:do {
  :set serverIP [:resolve connect.kmitl.ac.th];
} on-error={
  # when use DoH and not login yet, will no dns record in cache and can not query new
  :set serverIP [:resolve server=1.1.1.1 connect.kmitl.ac.th];
}
:local data "userName=$($account->"username")&password=$($account->"password")";
:local url "http://$serverIP:8080/PortalServer/Webauth/webAuthAction!login.action";
:local content ([/tool fetch http-method=post http-data=$data url=$url host="connect.kmitl.ac.th:8080" as-value output=user]->"data");

:if ([$ParseJSON $content "success" true] = false) do={
  :log error "Auto-Login: Can not login... server-msg: $[$ParseJSON $content "message" true]";
  :return false;
}

:local sessionId [$ParseJSON $content "sessionId"];
:local token [$ParseJSON $content "token" true];
:set token [:pick $token 6 [:len $token]];

# not implement case: external cisco login (httpPortalAuth == true)

:if ([$ParseJSON $content "portalAuth"] && ([$ParseJSON $content "httpPortalAuth"] = false)) do={
  # :delay 1s;
  :local status "sync";

  :do {
    :log debug "Auto-Login: Sync Portal Auth Result... $serverIP";
    :local url "http://$serverIP:8080/PortalServer/Webauth/webAuthAction!syncPortalAuthResult.action";
    :local content2 ([/tool fetch http-method=post url=$url http-header-field="Cookie:JSESSIONID=$sessionId" host="$serverIP:8080" as-value output=user]->"data");

    :if ([$ParseJSON $content2 "message" true] = "EmptySessionId") do={
      :log error "Auto-Login: Can not login... EmptySessionId";
      :return false;
    }

    :if ([$ParseJSON $content2 "success" true] = false) do={
      :log error "Auto-Login: Can not login... Sync not success... msg: $[$ParseJSON $content2 "message" true]";
      :return false;
    }

    :if ([$ParseJSON $content2 "portalAuthStatus"] != 0 && [$ParseJSON $content2 "portalAuthStatus"] != 1) do={
      :if ([$ParseJSON $content2 "portalErrorCode"] = 0) do={
        :log warning "Auto-Login: Can not login... Maybe you already login this device";
      } else={
        :log error "Auto-Login: Can not login... Please recheck your username and password... code:$[$ParseJSON $content2 "portalErrorCode"]";
      }
      :return false;
    }

    # only portal auth status 0 and 1 can be here
    :if ([$ParseJSON $content2 "portalAuthStatus"] = 0) do={
      # Wait for sync again
      :local delayTime [:totime ([$ParseJSON $content2 "webPortalOvertimePeriod"] . "ms")];
      :delay $delayTime;
    } else={
      # success
      :set status "success";
    }
  } while=($status = "sync");
}

# only success status can here
:global LServerIP $serverIP;
:global LAccount [$ParseJSON $content "account"];
:global LSessionId $sessionId;
:global LToken $token;
:local Heartbeat [:totime ([$ParseJSON $content "webHeatbeatPeriod"] . "ms")];

:log info "Auto-Login: Login successful  USER:$LAccount IP:$[$ParseJSON $content "ip"]";
:log debug "Auto-Login: Login info $sessionId $token";

# Set scheduler for heartbeat and AutoReLogin
/system scheduler set "AutoLogin-Heartbeat" interval=$Heartbeat start-date=[/system clock get date] start-time=[/system clock get time];
/system scheduler set "AutoLogin-AutoReLogin" start-date=[/system clock get date] start-time=[/system clock get time];

if ($isRunUtility) do={
  global UnloadUtil; $UnloadUtil;
}

:return true;
};

################################ Utility script ###############################

:if ([/system script find name="AutoLogin-Utility"] = "") do={
  /system script add name="AutoLogin-Utility";
}
/system script set "AutoLogin-Utility" policy=policy,read,test,write source={
:global CheckConnection do={
  :local googleIP;
  :do {
    :set googleIP [:resolve server=1.1.1.1 www.google.com];
  } on-error={
    :log warning "Auto-Login: No Internet...";
    :return "noInternet";
  }

  # detect web portal
  :local detect ([/tool fetch url="http://$googleIP/generate_204" as-value output=user]->"data");

  :if ($detect = "") do={
    :return "logged-in";
  } else={
    :return "notLogin";
  }
}

:global ParseJSON do={
  # mini JSON parser use only with minify JSON
  # will error when have any whitespace character or double object close `}}`
  # not implement array
  # $1 <str> JSON to parse
  # $2 <str> key to find
  # $3 <bool> skip key data object or array if other not skip

  :local start 0;
  :if ($3 = true) do={
    :if ([:pick $1 8] = "{") do={
      :set start ([:find $1 "}"]);
    } else={
      :if ([:pick $1 8] = "[") do={
        :set start ([:find $1 "]"]);
      }
    }
  }
  :set start ([:find $1 $2 $start] + [:len $2] + 2);
  :local end [:find $1 "," $start];
  :if ([:pick $1 ($end-1)] = "}") do={
    :set end ($end-1);
  }
  :local out [:pick $1 $start $end];
  :if ([:pick $out] = "\"") do={
    :return [:pick $1 ($start+1) ($end-1)];
  }
  :if ($out = "null") do={
    :return [];
  }
  :if ($out = "true") do={
    :return true;
  }
  :if ($out = "false") do={
    :return false;
  }
  :if ($out ~ "^[0-9.+-]+\$") do={
    :return [:tonum $out];
  }
  :put "Cannot Parse JSON object";
  :return [];
}

:global UnloadUtil do={
  global CheckConnection; set CheckConnection;
  global ParseJSON; set ParseJSON;
  global UnloadUtil; set UnloadUtil;
}
}

############################# AutoStart scheduler #############################

:if ([/system scheduler find name="AutoLogin-AutoStart"] = "") do={
  /system scheduler add name="AutoLogin-AutoStart";
}
/system scheduler set "AutoLogin-AutoStart" start-time=startup policy=policy,read,test,write on-event={
:delay 10s;
:log debug "Auto-Login: startup...";
/system script run "AutoLogin-Utility";
global CheckConnection;
:while ([$CheckConnection] = "noInternet") do={
  :delay 3s;
  :log debug "Auto-Login: Run Check connection...";
}

/system script run "AutoLogin-Login";
global UnloadUtil; $UnloadUtil;
};

############################ AutoReLogin scheduler ############################

:if ([/system scheduler find name="AutoLogin-AutoReLogin"] = "") do={
  /system scheduler add name="AutoLogin-AutoReLogin";
}
/system scheduler set "AutoLogin-AutoReLogin" interval=[:totime "9h59m55s"] policy=policy,read,test,write on-event={
:log debug "Auto-Login: Will check connection and re-login when login session timeout...";
/system script run "AutoLogin-Utility";
global CheckConnection;
:local loop 0;
:do {
  :local internet [$CheckConnection];
  :if ($internet = "noInternet") do={
    global UnloadUtil; $UnloadUtil;
    :return false;
  }
  :if ($internet = "notLogin") do={
    :set loop 200;
  } else={
    :log debug "Auto-Login: Recheck connection...";
    :set loop ($loop + 1);
    # delay for recheck lost connection
    # :delay 1s; # call CheckConnection already use 1s
  }
} while=($loop < 10);

:if ($loop != 200) do={
  :log warning "Auto-Login: Wait for session timeout is timeout. Not login...";
  global UnloadUtil; $UnloadUtil;
  :return false;
}

/system script run "AutoLogin-Login";
global UnloadUtil; $UnloadUtil;
};

############################# Heartbeat scheduler #############################
# spell-checker:ignore Hearbeat XSRF
:if ([/system scheduler find name="AutoLogin-Hearbeat"] != "") do={
  # change old incorrect spell
  /system scheduler set "AutoLogin-Hearbeat" name="AutoLogin-Heartbeat";
}
:if ([/system scheduler find name="AutoLogin-Heartbeat"] = "") do={
  /system scheduler add name="AutoLogin-Heartbeat";
}
/system scheduler set "AutoLogin-Heartbeat" policy=policy,read,test,write on-event={
/system script run "AutoLogin-Utility";
global CheckConnection; global ParseJSON;
:if ([$CheckConnection] = "notLogin") do={
  :log warning "Auto-Login: Lost Connection, Retry login...";
  /system script run "AutoLogin-Login";
} else={
  global LAccount; global LSessionId; global LToken; global LServerIP;
  if ((any $LAccount) && (any $LSessionId) && (any $LToken) && (any $LServerIP)) do={
    :local data "userName=$LAccount&sessionId=$LSessionId";
    :local url "http://$LServerIP:8080/PortalServer/Webauth/webAuthAction!hearbeat.action";
    :local content ([/tool fetch http-method=post http-data=$data url=$url http-header-field="X-XSRF-TOKEN:$LToken" host="$LServerIP:8080" as-value output=user]->"data");
    :if ([$ParseJSON $content "data"] = "ONLINE") do={
      :log info "Auto-Login: HeartBeat OK...";
    } else={
      :log error "Auto-Login: HeartBeat ERROR... server-msg: $[$ParseJSON $content "message" true]";
      /system script run "AutoLogin-Login";
    }
  }
}

global UnloadUtil; $UnloadUtil;
};

############################# remove old variable #############################
# spell-checker:ignore Lcheck Lhearbeat Linit Llogin
global LcheckConnection; set LcheckConnection;
global Lhearbeat; set Lhearbeat;
global Linit; set Linit;
global Llogin; set Llogin;
global LloginLoop; set LloginLoop;
global loginServer; set loginServer;
global JSONUnload; $JSONUnload; set JSONUnload;

############################### setup new script ##############################
# spell-checker:ignore dont abcdefghijklmnopqrstuvwxyz inkey
:if ([/system script find name="AutoLogin-Config"] = "") do={
  global loginUser; global loginPass;
  :if (!any $loginUser || !any $loginPass) do={
    :local input do={
      :local out "";
      :local mask "";
      :local in "";
      :local ascii " !\"#\$%&'()*+,-./0123456789:;<=>\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
      :if (!any $1) do={
        :set $1 "enter text";
      }
      :put "$1 : ";
      :do {
        /terminal cuu count=1;
        /terminal el;
        :if ($2 = true) do={
          :put "$1 : $mask";
        } else={
          :put "$1 : $out";
        }
        :set in [/terminal inkey timeout=60];
        :if (32 <= $in && $in < 128) do={
          :local char [:pick $ascii ($in-32)]
          :set out ($out . $char);
          :set mask ($mask . "*");
        } else={
          if ($in = 8) do={
            :set out [:pick $out 0 ([:len $out] - 1)]
            :set mask [:pick $mask 0 ([:len $mask] - 1)]
          }
        }
      } while=(in != 13); # enter
      :return $out
    };

    :put "Please enter your username and password to use auto-login";
    :put "Do not enter @kmitl.ac.th in username"
    :set loginUser [$input "Username"];
    :set loginPass [$input "Password" true];
  }
  /system script add name="AutoLogin-Config" dont-require-permissions=yes source="username=\"$loginUser\";\r\npassword=\"$loginPass\";";
  set loginUser; set loginPass;
}

/system script run "AutoLogin-Utility";
:global CheckConnection;
:local internet [$CheckConnection];
:if ($internet = "notLogin") do={
  :put "Let's login. (Watch status in log)";
  /system script run "AutoLogin-Login";
} else={
  :if ($internet = "logged-in") do={
    :put "Now internet is accessible, Do you want to re-login (y/N)";
    :local in [/terminal inkey timeout=60];
    :if (($in %32) = 25) do={
      :put "Let's login. (Watch status in log)";
      /system script run "AutoLogin-Login";
    }
  }
}
global UnloadUtil; $UnloadUtil;

global LAccount; global LSessionId; global LToken; global LServerIP;
if ((!any $LAccount) || (!any $LSessionId) || (!any $LToken) || (!any $LServerIP)) do={
  if ([/system scheduler get AutoLogin-Heartbeat interval] = 00:00:00) do={
    /system scheduler set AutoLogin-Heartbeat interval=1m;
    :put "Use heartbeat to check login session timeout and auto re-login every 1 minute";
  }
}

:put "Finish setup";


File: /LICENSE
MIT License

Copyright (c) 2019 Phumphathai Chansriwong

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
# KMITL-Auto-Authen-Mikrotik

A **_Mikrotik script_** that let you automatically authenticate into KMITL network

## Getting started
### Prerequisites
* Mikrotik RouterOS v.6.43 or later

### Installation & Upgrade
1. Login into Mikrotik and open new terminal
2. Copy and Pase this script (If use terminal in winbox **Don't use Ctrl-V**, use right click and pase)
```
/tool fetch url=https://raw.githubusercontent.com/ouoam/KMITL-Auto-Authen-Mikrotik/master/Auto-Login-KMITL;
/import file-name=Auto-Login-KMITL;
```
3. If first time install, this script will ask for username and password in terminal.

### Usage
When you run this script. This script will create new scheduler for auto Auten.
You can view log for more info. Log from this script is start with `Auto-Login`

### Config
You can change config at System->Scripts and select scripts name AutoLogin-Config.
You **can not** change Heartbeat interval, it will use value form authen server.

| Name | Description |
|:----:|-------------|
| `username` | Username to login _(without **@kmitl.ac.th**)_ |
| `password` | Password to login |

## Credit
* **_Member in Network Laboratory_** for [Auto Authen KMITL](https://gitlab.com/networklab-kmitl/auto-authen-kmitl) written in Python language (and some README.md)
* **_[@mayueeeee](https://github.com/mayueeeee)_** for [KMITL-Auto-Authen](https://github.com/mayueeeee/KMITL-Auto-Authen) written in Go language

## Thank
* **_[Postman](https://www.getpostman.com/)_** for tool to simulate communicate with authen server
* **_[NetCat](https://eternallybored.org/misc/netcat/)_** for tool to simulate as authen server

## Team
* only me

## Disclaimer
This project is only an experiment on KMITL authentication system and it does not provided a bypass for login system


