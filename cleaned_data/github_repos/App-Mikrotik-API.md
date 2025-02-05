# Repository Information
Name: App-Mikrotik-API

# Directory Structure
Directory structure:
└── github_repos/App-Mikrotik-API/
    ├── .babelrc
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
    │   │       ├── pack-343e823a9527b988e713fd7c41ec28e9989d7d21.idx
    │   │       └── pack-343e823a9527b988e713fd7c41ec28e9989d7d21.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── client/
    │   ├── config.js
    │   └── src/
    │       ├── App.css
    │       ├── App.js
    │       ├── icons/
    │       ├── index.js
    │       ├── layouts/
    │       │   ├── components/
    │       │   │   ├── Header/
    │       │   │   │   ├── Header.js
    │       │   │   │   ├── Header.scss
    │       │   │   │   └── index.js
    │       │   │   └── Menu/
    │       │   │       ├── index.js
    │       │   │       ├── Menu.js
    │       │   │       └── Menu.scss
    │       │   └── index.js
    │       ├── redux/
    │       │   ├── actions/
    │       │   │   └── dataMikrotik.js
    │       │   ├── constants/
    │       │   │   └── index.js
    │       │   ├── middlewares/
    │       │   │   └── index.js
    │       │   ├── reducers/
    │       │   │   ├── index.js
    │       │   │   └── modules/
    │       │   │       ├── DevicesReduser.js
    │       │   │       └── InterfaceReduser.js
    │       │   └── store/
    │       │       └── createStore.js
    │       ├── routes/
    │       │   ├── DevicesContainer/
    │       │   │   ├── components/
    │       │   │   │   └── ListDevices/
    │       │   │   │       ├── index.js
    │       │   │   │       ├── ListDevices.js
    │       │   │   │       └── ListDevices.scss
    │       │   │   ├── Devices.scss
    │       │   │   ├── DevicesContainer.js
    │       │   │   └── index.js
    │       │   ├── index.js
    │       │   ├── InterfaceContainer/
    │       │   │   ├── components/
    │       │   │   │   └── ListInterface/
    │       │   │   │       ├── index.js
    │       │   │   │       ├── ListInterface.js
    │       │   │   │       └── ListInterface.scss
    │       │   │   ├── index.js
    │       │   │   ├── Interface.scss
    │       │   │   └── InterfaceContainer.js
    │       │   ├── MainContainers/
    │       │   │   ├── index.js
    │       │   │   ├── Main.scss
    │       │   │   └── MainContainer.js
    │       │   ├── RootContainers/
    │       │   │   └── index.js
    │       │   └── TrafficContainers/
    │       │       ├── components/
    │       │       │   └── Graphics/
    │       │       │       ├── Graphics.js
    │       │       │       ├── Graphics.scss
    │       │       │       └── index.js
    │       │       ├── index.js
    │       │       ├── Traffic.scss
    │       │       └── TrafficContainers.js
    │       └── socket-io/
    │           ├── ConnectClient.js
    │           ├── data_mikrotik.js
    │           └── utils/
    │               └── index.js
    ├── config/
    │   ├── client-config.json
    │   └── server-config.json
    ├── constants/
    │   └── envs.js
    ├── package.json
    ├── public/
    │   └── index.html
    ├── README.md
    ├── server/
    │   ├── app.js
    │   ├── config.js
    │   ├── connectors/
    │   │   ├── MikrotikApi/
    │   │   │   ├── index.js
    │   │   │   └── modules/
    │   │   │       ├── dhcpServerChannel/
    │   │   │       │   ├── dhcpClients.js
    │   │   │       │   ├── dhcpServerInfo.js
    │   │   │       │   └── index.js
    │   │   │       ├── interfaceInfo/
    │   │   │       │   ├── index.js
    │   │   │       │   └── interfaceInfo.js
    │   │   │       ├── ipPingChannel/
    │   │   │       │   ├── index.js
    │   │   │       │   └── ipPingChannel.js
    │   │   │       ├── ipScanChannel/
    │   │   │       │   ├── index.js
    │   │   │       │   └── scanInterface.js
    │   │   │       ├── listenChannel/
    │   │   │       │   ├── index.js
    │   │   │       │   └── listenChannel.js
    │   │   │       ├── torchChannel/
    │   │   │       │   ├── index.js
    │   │   │       │   └── torchChannel.js
    │   │   │       └── trafficChannel/
    │   │   │           ├── index.js
    │   │   │           └── trafficChannel.js
    │   │   └── soketIO/
    │   │       ├── index.js
    │   │       └── modules/
    │   │           └── disconnect.js
    │   ├── handlers/
    │   │   ├── error.js
    │   │   └── index.js
    │   └── server.js
    ├── utils/
    │   └── env.js
    └── webpack.config.js


# Content
File: /.babelrc
{
  "presets": ["env", "stage-0", "react", "react-hmre"],
}


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/khamchenko/App-Mikrotik-API.git
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
0000000000000000000000000000000000000000 a3d360b0b2b92759133559d449345e6dec9353b2 vivek-dodia <vivek.dodia@icloud.com> 1738606441 -0500	clone: from https://github.com/khamchenko/App-Mikrotik-API.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 a3d360b0b2b92759133559d449345e6dec9353b2 vivek-dodia <vivek.dodia@icloud.com> 1738606441 -0500	clone: from https://github.com/khamchenko/App-Mikrotik-API.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a3d360b0b2b92759133559d449345e6dec9353b2 vivek-dodia <vivek.dodia@icloud.com> 1738606441 -0500	clone: from https://github.com/khamchenko/App-Mikrotik-API.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
a3d360b0b2b92759133559d449345e6dec9353b2 refs/remotes/origin/master


File: /.git\refs\heads\master
a3d360b0b2b92759133559d449345e6dec9353b2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
File: /client\config.js
import config from '../config/client-config.json';
import envs from 'constants/envs';
import env from 'utils/env';

if (!envs[env]) {
  throw Error(`unknown env '${env}'`);
}

const SOCKET_IO_API = process.env.PORT || config.socketUrl;

export {
  SOCKET_IO_API,
};


File: /client\src\App.css
@import url(https://fonts.googleapis.com/css?family=Caveat|Roboto);

* {
    box-sizing: border-box;
}

body {
    font-size: 16px;
    font-family: Roboto,sans-serif;
    background: #e2f1ff;
    margin: 0;
}

#root {
    min-width: 340px;
}

button:focus{ outline: none;}

input[type="text"]:focus { }

a {
    color: #fff;
    text-decoration: none;
}

textarea{
    border: none;
    resize: none;
    overflow: auto;
}

::-webkit-scrollbar-thumb {
-webkit-border-radius: 0px;
border-radius: 0px;
background-color:#24272a;
}

::-webkit-scrollbar-thumb:hover{
background-color:#56999f;
}

::-webkit-resizer{
background-image:url('');
background-repeat:no-repeat;
width: 2px;
height: 0px
}

::-webkit-scrollbar{
width: 2px;
height: 3px;
}

.root-content {
    width: calc(100% - 220px);
    position: relative;
    left: 220px;
    top: 60px;
}


File: /client\src\App.js
import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { renderRoutes } from 'react-router-config';

import './App.css';

const App = ({ routes }) => (
  <BrowserRouter basename="/">
    {renderRoutes(routes)}
  </BrowserRouter>
);

export default App;


File: /client\src\index.js
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';

import createStore from './redux/store/createStore';
import ConnectClientWS from './socket-io/ConnectClient';
import routes from './routes';

import App from './App';

const rootReact = document.getElementById('root');
const store = createStore();

const { dispatch } = store;

dispatch(ConnectClientWS());

const renderApp = (Component, appRoutes) => {
  render(
    <Provider store={store}>
      <Component routes={appRoutes}/>
    </Provider>, rootReact
  );
};

renderApp(App, routes);;


File: /client\src\layouts\components\Header\Header.js
import React, { Component } from 'react';

import './Header.scss';

const Header = () => (
    <header className="header-root">

    </header>
);

export default Header;


File: /client\src\layouts\components\Header\Header.scss
.header-root {
    position: fixed;
    width: 100%;
    top: 0px;
    z-index: 99;
    left: 220px;
    height: 60px;
    color: #fff;
    display: flex;
    background: #00b4ea;
    .logo {
        width: 400px;
        height: 100px;
    }
    .title {
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }
}


File: /client\src\layouts\components\Header\index.js
import Header from './Header';

export default Header;


File: /client\src\layouts\components\Menu\index.js
import Menu from './Menu';

export default Menu;


File: /client\src\layouts\components\Menu\Menu.js
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import MikrotikLogo from 'icons/mikrotik_logo.png';

import './Menu.scss';

class Menu extends Component {
    render() {
        return (
            <div className="menu">
                <div className="wrapper-logo">
                    <img className="logo" src={MikrotikLogo} alt=''/>
                </div>
                <Link to="/" className="menu-elem">Главная</Link>
                <Link to="/devices" className="menu-elem">Подключенные устройства</Link>
                <Link to="/interface" className="menu-elem">Интерфесы</Link>
                <Link to="/traffic" className="menu-elem">Трафик</Link>
            </div>
        );
    }
}

export default Menu;


File: /client\src\layouts\components\Menu\Menu.scss
.menu {
    position: fixed;
    height: 100vh;
    top: 0;
    width: 220px;
    background: #24272a;
    display: flex;
    font-size: 16px;
    flex-direction: column;
    align-items: flex-start;
    .wrapper-logo {
        margin: 0 auto;
        height: 60px;
        justify-content: center;
        align-items: center;
        display: flex;
        margin-bottom: 20px;
        .logo {
            width: 150px;
            margin: 20px 0;
            background-position: center;
            background-size: cover;
        }
    }
    .menu-elem {
        width: 220px;
        text-align: center;
        padding: 10px 10px;
        color: #fff;
        cursor: pointer;
        text-transform: uppercase;
        &:hover {
            background: #1b1b1b;
        }
    }
}


File: /client\src\layouts\index.js
import React, { Component } from 'react';

import { connect } from 'react-redux';

import Header from './components/Header';
import Menu from './components/Menu';

import { getInterface } from 'socket-io/data_mikrotik';

class Layout extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        this.props.handlerGetInterface();
    }
    render() {
        return (
            <div>
                <Header />
                <Menu />
            </div>
        );
    }
}

const mapDispatchToProps = dispatch => {
    return {
        handlerGetInterface: () => {
            dispatch(getInterface());
        }
    }
};
export default connect(null, mapDispatchToProps)(Layout);


File: /client\src\redux\actions\dataMikrotik.js
import constants from '../constants';

export const ListDevices = (devices) => dispatch => {
    dispatch({
        type: constants.LOAD_DEVICES,
        payload: devices,
    })
};

export const ListInterface = (Interface) => dispatch => {
    dispatch({
        type: constants.LOAD_INTERFACE,
        payload: Interface,
    })
};


File: /client\src\redux\constants\index.js
import keyMirror from 'key-mirror'

export default keyMirror({
	LOAD_DEVICES: null,
	LOAD_INTERFACE: null,
})


File: /client\src\redux\middlewares\index.js
import thunk from 'redux-thunk';
import { apiMiddleware } from 'redux-api-middleware';

export default [
    apiMiddleware,
    thunk
];


File: /client\src\redux\reducers\index.js
import { combineReducers } from 'redux';
import devices from './modules/DevicesReduser';
import Interface from './modules/InterfaceReduser';

const rootReducer = combineReducers({
    devices,
    Interface,
});

export default rootReducer;


File: /client\src\redux\reducers\modules\DevicesReduser.js
import constants from '../../constants'
import { forEach, keys } from 'lodash';

const initialState = {
    data: [],
    isLoading: false,
    error: null,
};

const DevicesReduser = (state = initialState, action) => {
    switch(action.type) {
        case constants.LOAD_DEVICES:
            return {
              ...state,
              data: [...action.payload],
            };
        default:
            return state
    }
};

export default DevicesReduser;


File: /client\src\redux\reducers\modules\InterfaceReduser.js
import constants from '../../constants'
import { forEach, keys } from 'lodash';

const initialState = {
    data: [],
    isLoading: false,
    error: null,
};

const InterfaceReduser = (state = initialState, action) => {
    switch(action.type) {
        case constants.LOAD_INTERFACE:
            return {
              ...state,
              data: [...action.payload],
            };
        default:
            return state
    }
};

export default InterfaceReduser;


File: /client\src\redux\store\createStore.js
import { applyMiddleware, createStore, compose } from 'redux';
import { IS_DEV } from 'utils/env';

import thunk from 'redux-thunk';
import { apiMiddleware } from 'redux-api-middleware';

import redusers from '../reducers';

import middlewares from '../middlewares';

let composeEnhancers = compose;

if (IS_DEV && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) {
    composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__;
}

const enhancer = composeEnhancers(
    applyMiddleware(...middlewares),
);

export default function (initialState = {}) {

  const store = createStore( redusers, initialState, enhancer);

  return store;
}


File: /client\src\routes\DevicesContainer\components\ListDevices\index.js
import ListDevices from './ListDevices';

export default ListDevices


File: /client\src\routes\DevicesContainer\components\ListDevices\ListDevices.js
import React, { Component } from 'react';
import { map } from 'lodash';

import './ListDevices.scss';

class ListDevices extends Component {
    render() {
        const { devices } = this.props;
        return (
            <div className="root-list-devices">
                <div className="header-table">
                    <div className="th-table">Интерфейс</div>
                    <div className="th-table">MAC - адрес</div>
                    <div className="th-table">IP - адрес</div>
                    <div className="th-table th-dns">DNS</div>
                    <div className="th-table">Тип подключения</div>
                    <div className="th-table">Имя хоста</div>
                    <div className="th-table">Статус</div>
                </div>
                <div>
                    {
                        _.map(devices, (elem) => {
                            return (
                                <div className="tr-table" key={`${elem.ip}${elem.mac}`}>
                                    <div className="td-table">{elem.interface || '-'}</div>
                                    <div className="td-table">{elem.mac || '-'}</div>
                                    <div className="td-table">{elem.ip}</div>
                                    <div className="td-table td-dns">{elem.dns || '-'}</div>
                                    <div className="td-table">{elem.type || '-'}</div>
                                    <div className="td-table">{elem.host_name || '-'}</div>
                                    <div className="td-table">{elem.status}</div>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        )
    }
}

export default ListDevices;


File: /client\src\routes\DevicesContainer\components\ListDevices\ListDevices.scss
.root-list-devices {
    background: #fff;
    padding: 0 10px;
    .header-table {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        margin: 10px auto;
        height: 60px;
        border-bottom: 1px solid #24272a;
        .th-table {
            flex-grow: 1;
            padding: 5px 10px;
            text-align: center;
            width: 180px !important;
        }
    }
    .tr-table {
        display: flex;
        justify-content: center;
        margin: 0 auto;
        padding: 5px 0;
        .td-table {
            flex-grow: 1;
            padding: 5px 10px;
            text-align: center;
            width: 180px !important;
        }
    }
}


File: /client\src\routes\DevicesContainer\Devices.scss
.root-devices {
    padding: 10px;
    width: 100%;
    margin: 0 auto;
}


File: /client\src\routes\DevicesContainer\DevicesContainer.js
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { map, forEach } from 'lodash';

import { getDevices } from 'socket-io/data_mikrotik';

import './Devices.scss';

import ListDevices from './components/ListDevices';

class DevicesContainer extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        this.props.handlerGetDevices();
    }
    render() {
        const { devices } = this.props;
        return (
            <div className="root-devices">
                <ListDevices devices={devices}/>
            </div>
        );
    }
}

const mapStateToProps = ({ devices }) => {
    return {
        devices: devices.data
    };
}

const mapDispatchToProps = dispatch => {
    return {
        handlerGetDevices: () => {
            dispatch(getDevices());
        }
    }
};

export default connect(mapStateToProps, mapDispatchToProps)(DevicesContainer);


File: /client\src\routes\DevicesContainer\index.js
import DevicesContainer from './DevicesContainer';

export default DevicesContainer


File: /client\src\routes\index.js
import RootRoutes from './RootContainers';
import MainRoutes from './MainContainers';
import DevicesRoutes from './DevicesContainer';
import InterfaceContainer from './InterfaceContainer';
import TrafficContainers from './TrafficContainers';

const routes = [
    {
        component: RootRoutes,
        routes: [
            {
                path: '/',
                exact: true,
                component: MainRoutes
            },
            {
                path: '/devices',
                exact: true,
                component: DevicesRoutes
            },
            {
                path: '/interface',
                exact: true,
                component: InterfaceContainer
            },
            {
                path: '/traffic',
                exact: true,
                component: TrafficContainers
            },
        ]
    }
];

export default routes;


File: /client\src\routes\InterfaceContainer\components\ListInterface\index.js
import ListInterface from './ListInterface';

export default ListInterface


File: /client\src\routes\InterfaceContainer\components\ListInterface\ListInterface.js
import React, { Component } from 'react';
import { map } from 'lodash';

import './ListInterface.scss';

class ListInterface extends Component {
    render() {
        const { Interface } = this.props;
        return (
            <div className="root-list-devices">
                <div className="header-table">
                    <div className="th-table">Интерфейс</div>
                    <div className="th-table">MAC - адрес</div>
                    <div className="th-table">RX</div>
                    <div className="th-table">TX</div>
                    <div className="th-table">Всего RX</div>
                    <div className="th-table">Всего TX</div>
                    <div className="th-table">Статус</div>
                </div>
                <div>
                    {
                        _.map(Interface, (elem) => {
                            return (
                                <div className="tr-table" key={`${elem.name}`}>
                                    <div className="td-table">{elem.name || '-'}</div>
                                    <div className="td-table">{elem.mac || '-'}</div>
                                    <div className="td-table">{elem.rx || '-'}</div>
                                    <div className="td-table">{elem.tx || '-'}</div>
                                    <div className="td-table">{elem.sum_rx || '-'}</div>
                                    <div className="td-table">{elem.sum_tx || '-'}</div>
                                    <div className="td-table">{elem.status || '-'}</div>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        )
    }
}

export default ListInterface;


File: /client\src\routes\InterfaceContainer\components\ListInterface\ListInterface.scss



File: /client\src\routes\InterfaceContainer\index.js
import InterfaceContainer from './InterfaceContainer';

export default InterfaceContainer


File: /client\src\routes\InterfaceContainer\Interface.scss
.root-interface {
    padding: 10px;
    width: 100%;
    margin: 0 auto;
}


File: /client\src\routes\InterfaceContainer\InterfaceContainer.js
import React, { Component } from 'react';
import { connect } from 'react-redux';

import './Interface.scss';

import ListInterface from './components/ListInterface';

class InterfaceContainer extends Component {
    render() {
        const { Interface } = this.props;
        return (
            <div className="root-interface">
                <ListInterface Interface={Interface}/>
            </div>
        );
    }
}

const mapStateToProps = ({ Interface }) => {
    return {
        Interface: Interface.data
    };
}

export default connect(mapStateToProps, null)(InterfaceContainer);


File: /client\src\routes\MainContainers\index.js
import MainContainer from './MainContainer';

export default MainContainer


File: /client\src\routes\MainContainers\Main.scss
.main {
    position: fixed;
    top: 60px;
    left: 220px;
    height: calc(100%);
    width: 100%;
    min-width: 340px;
    background-size: cover;
    .main-wrapper{
        
    }
}


File: /client\src\routes\MainContainers\MainContainer.js
import React, { Component } from 'react';

import './Main.scss';

class MainContainer extends Component {
  render() {
        return (
            <div className="main">
                <div className="main-wrapper">

                </div>
            </div>
        );
    }
}

export default MainContainer;


File: /client\src\routes\RootContainers\index.js
import React, { Component } from 'react';
import { connect } from 'react-redux';

import { renderRoutes } from 'react-router-config';

import Layout from '../../layouts';

class RootLayout extends Component {
    render() {
        const { route: { routes } } = this.props;
        return (
            <div>
                <Layout />
                <div className="root-content" id="content">{renderRoutes(routes)}</div>
            </div>
        );
    }
}

export default RootLayout;


File: /client\src\routes\TrafficContainers\components\Graphics\Graphics.js
import React, { Component } from 'react';
import _ from 'lodash';
import ReactHighstock from 'react-highcharts/ReactHighstock.src';

import './Graphics.scss';

let config = {
    colors: ['#2f7ed8', '#910000'],
    rangeSelector: {
       buttons: [],
       inputEnabled: false,
       selected: 0
    },
    yAxis: {
        title: {
            text: 'Throughput, (Kbps)'
        }
    },
    navigator: {
        enabled: false
    },
    scrollbar: {
        enabled: false
    },
    chart: {
        height: 300
    },
    title: {
        text: ''
    },
    series: [
        {
            name: 'RX',
            data: [],
            type: 'spline',
            tooltip: {
                valueDecimals: 1,
                valueSuffix: 'Kbps'
            }
        },
        {
            name: 'TX',
            data: [],
            type: 'spline',
            tooltip: {
                valueDecimals: 1,
                valueSuffix: 'Kbps'
            }
        }
    ]
};

class Graphics extends Component {
    constructor(props) {
        super(props);
        this.state = {
            config: config,
            ['eth1-wan']: { rx: [], tx: []},
            ['eth2']: { rx: [], tx: []},
            ['eth3']: { rx: [], tx: []},
            ['eth4']: { rx: [], tx: []},
            ['eth5-master']: {rx: [], tx: []},
            ['bridge1']:{ rx: [], tx: []},
        }
    }
    componentWillReceiveProps() {
        _.forEach(this.props.Interface, (elem) => {
            if (this.state[elem.name].rx.length > 50) {
                this.setState({
                    [elem.name]: {
                        rx: [ ...this.state[elem.name].rx.slice(1), [Number(elem.date), Number(elem.rx)]],
                        tx:  [ ...this.state[elem.name].tx.slice(1), [Number(elem.date), Number(elem.tx)]],
                    }
                })
            } else {
                this.setState({
                    [elem.name]: {
                        rx: [ ...this.state[elem.name].rx, [Number(elem.date), Number(elem.rx)]],
                        tx:  [ ...this.state[elem.name].tx, [Number(elem.date), Number(elem.tx)]],
                    }
                })
            }
        })
    }
    render() {
        const { Interface } = this.props;
        return (
            <div className="root-graphics">
                {
                    <div className="wrapper-graphics-full">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'eth1-wan'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data: this.state['eth1-wan'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data: this.state['eth1-wan'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
                {
                    <div className="wrapper-graphics-full">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'bridge1'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data: this.state['bridge1'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data:  this.state['bridge1'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
                {
                    <div className="wrapper-graphics">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'eth2'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data: this.state['eth2'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data: this.state['eth2'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
                {
                    <div className="wrapper-graphics">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'eth3'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data:  this.state['eth3'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data:  this.state['eth3'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
                {
                    <div className="wrapper-graphics">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'eth4'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data:  this.state['eth4'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data:  this.state['eth4'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
                {
                    <div className="wrapper-graphics">
                        <ReactHighstock
                            config={
                                {
                                    ...config,
                                    title: {
                                        text: 'eth5-master'
                                    },
                                    series: [
                                        {
                                            ...config.series[0],
                                            data:  this.state['eth5-master'].rx
                                        },
                                        {
                                            ...config.series[1],
                                            data: this.state['eth5-master'].tx
                                        },
                                    ]
                                }
                            }
                        />
                    </div>
                }
            </div>
        )
    }
}

export default Graphics;


File: /client\src\routes\TrafficContainers\components\Graphics\Graphics.scss
.root-graphics {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    .wrapper-graphics {
        width: 290px;
        margin: 10px 0;
    }
    .wrapper-graphics-full {
        width: calc(50% - 10px);
        margin: 10px 0;
    }
}


File: /client\src\routes\TrafficContainers\components\Graphics\index.js
import Graphics from './Graphics';

export default Graphics


File: /client\src\routes\TrafficContainers\index.js
import TrafficContainers from './TrafficContainers';

export default TrafficContainers


File: /client\src\routes\TrafficContainers\Traffic.scss
.root-traffic {
    padding: 10px;
    width: 100%;
    margin: 0 auto;
}


File: /client\src\routes\TrafficContainers\TrafficContainers.js
import React, { Component } from 'react';
import { connect } from 'react-redux';

import Graphics from './components/Graphics';

import './Traffic.scss';

class TrafficsContainer extends Component {
    render() {
        const { Interface } = this.props;

        return (
            <div className="root-traffic">
                <Graphics Interface={Interface}/>
            </div>
        );
    }
}

const mapStateToProps = ({ Interface }) => {
    return {
        Interface: Interface.data
    };
}

export default connect(mapStateToProps, null)(TrafficsContainer);


File: /client\src\socket-io\ConnectClient.js
import socket from './utils' ;

export default () => dispatch => {
    socket.on('connect', () => {
        console.log("SUCCESS CONNECT");
    });
}


File: /client\src\socket-io\data_mikrotik.js
import socket from './utils' ;

import { ListDevices, ListInterface, TrafficInterface } from '../redux/actions/dataMikrotik';

export const getDevices = () => dispatch => {
    socket.on('get_devices', (devices) => {
        dispatch(ListDevices(devices));
    });
};

export const getInterface = () => dispatch => {
    socket.on('get_Interface', (Interface) => {
        dispatch(ListInterface(Interface));
    });
};


File: /client\src\socket-io\utils\index.js
import io from 'socket.io-client';
import { SOCKET_IO_API } from '../../../config'
const socket = io.connect(SOCKET_IO_API);

export default socket;


File: /config\client-config.json
{
  "port": "3001",
  "socketUrl": "http://localhost:4000"
}


File: /config\server-config.json
{
    "port": "4000",
    "url": "http://localhost",
    "mikrotik": {
        "api": "192.168.10.1"
    }
}


File: /constants\envs.js
import keyMirror from 'key-mirror';

export default keyMirror({
  development: null,
  production: null,
  test: null,
});


File: /package.json
{
  "name": "Test",
  "version": "1.0.0",
  "description": "Mickrotic-web",
  "main": "index.js",
  "scripts": {
    "build:dev": "webpack --color --progress --mode development",
    "build:prod": "webpack --color --progress --mode production",
    "server": "nodemon --exec babel-node ./server/server",
    "dev": "webpack-dev-server --color --mode development"
  },
  "author": "Dmitry Khamchenko",
  "license": "ISC",
  "dependencies": {
    "asyncinterval": "0.0.7",
    "bootstrap-grid": "^3.0.1",
    "core-decorators": "^0.20.0",
    "cors": "^2.8.4",
    "express": "^4.16.3",
    "highcharts": "^6.1.0",
    "highstock-browserify": "^1.0.6",
    "interval-promise": "^1.1.1",
    "key-mirror": "^1.0.1",
    "lodash": "^4.17.5",
    "mikronode": "^2.3.11",
    "nodemon": "^1.17.3",
    "prismjs": "^1.14.0",
    "react": "^16.2.0",
    "react-dom": "^16.2.0",
    "react-highcharts": "^16.0.2",
    "react-highlight": "^0.12.0",
    "react-highstock": "^1.0.2",
    "react-prism": "^4.3.2",
    "react-prismjs": "^1.0.4",
    "react-redux": "^5.0.7",
    "react-router-config": "^1.0.0-beta.4",
    "react-router-dom": "^4.2.2",
    "react-router-redux": "^4.0.8",
    "react-transition-group": "^2.3.1",
    "redux": "^3.7.2",
    "redux-api-middleware": "^2.3.0",
    "redux-thunk": "^2.2.0",
    "socket.io": "^2.1.0",
    "socket.io-client": "^2.1.0"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-core": "^6.26.0",
    "babel-loader": "^7.1.2",
    "babel-preset-env": "^1.6.1",
    "babel-preset-react": "^6.24.1",
    "babel-preset-react-hmre": "^1.1.1",
    "babel-preset-stage-0": "^6.24.1",
    "clean-webpack-plugin": "^0.1.19",
    "css-loader": "^0.28.10",
    "file-loader": "^1.1.11",
    "html-webpack-plugin": "^3.0.6",
    "node-sass": "^4.7.2",
    "sass-loader": "^6.0.7",
    "style-loader": "^0.20.2",
    "url-loader": "^1.0.1",
    "webpack": "^4.1.1",
    "webpack-cli": "^2.0.10",
    "webpack-dev-server": "^3.1.0"
  }
}


File: /public\index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Copatible" content="ie=edge">
    <title>Mikrotik RouterBoard</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>


File: /README.md
# React App-Mikrotik-API

## Getting started
```sh
# Install dependencies
npm install
```

```sh
# Run dev server
npm run server
npm run dev
```

```sh
# Build application
npm run build-dev
```


File: /server\app.js
import express from 'express';
const path = require('path');
const fs = require('fs');

import initHandlers from './handlers';

const app = express();

initHandlers(app);

// app.use('/', (req, res) => {
//     res.set('Content-Type', 'text/html');
//     res.body = fs.readFileSync(path.resolve(__dirname, '../../../public/index.html'));
// });

app.get('/', function (req, res) {
  res.send('Hello World!');
});

export default app;


File: /server\config.js
import serverConfig from '../config/server-config.json';
import envs from '../constants/envs';
import env from '../utils/env';

if (!envs[env]) {
  throw Error(`unknown env '${env}'`);
}

const PORT = process.env.PORT || serverConfig.port;
const MIKROTIK_API = process.env.PORT || serverConfig.mikrotik.api;

export {
  PORT,
  MIKROTIK_API
};


File: /server\connectors\MikrotikApi\index.js
import mikronode from 'mikronode';

import { MIKROTIK_API } from '../../config';

import listenChannel from './modules/listenChannel';
import ipPingChannel from './modules/ipPingChannel';
import trafficChannel from './modules/trafficChannel';
import ipScanChannel from './modules/ipScanChannel';
import torchChannel from './modules/torchChannel';
import dhcpServerChannel from './modules/dhcpServerChannel';
import interfaceInfo from './modules/interfaceInfo';

const API = new mikronode(MIKROTIK_API);

const MikrotikAPI = (io, devices, Interface) => {
    API.connect()
        .then(([login])=>{
            return login('admin','admin');
        })
        .then(conn => {
            console.log('Logged in');
            conn.closeOnDone(true);

            listenChannel(conn, io, Interface);
            ipScanChannel(conn, io, devices);
            torchChannel(conn, io, devices);
            ipPingChannel(conn, io, devices);
            dhcpServerChannel(conn, io, devices);
            interfaceInfo(conn, io, Interface)
            trafficChannel(conn, io, Interface)

            conn.on('error', (err) => {
                console.log('error', err);
            });
        })
        .catch( err => {
            console.log('ERROR', err);
        });

}

export default MikrotikAPI


File: /server\connectors\MikrotikApi\modules\dhcpServerChannel\dhcpClients.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

const dhcpClients = (conn, io, devices) => {
    let channel = conn.openChannel('dhcp');

    channel.data.subscribe( (item) => {
         let device = resultsToObj(item);
         device = {
             interface: false,
             ip: device.address,
             mac: device['mac-address'] || false,
             dns: device.dns || false,
             type: 'dhcp',
             host_name: device['host-name'],
             status: 'connected'
        }
        let NewDevices = _.find(devices, { ip: device.ip })
        if (!!!NewDevices && (device.mac || device.dns)) {
            devices.push(Object.assign(device))
        }
        if (NewDevices) {
            let index = devices.indexOf(NewDevices)
            devices[index] = {
                ...NewDevices,
                mac: device.mac ? device.mac : NewDevices.mac,
                type: device.type ? device.type : NewDevices.type,
                host_name: device.host_name ? device.host_name : NewDevices.host_name,
            }
        }
    }, error => {
        console.log("Error during ipScanChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/ip/dhcp-server/lease/print', [`=interval=10`])
    .then( result => {
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default dhcpClients


File: /server\connectors\MikrotikApi\modules\dhcpServerChannel\dhcpServerInfo.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

const ipScanChannel = (conn, io, devices) => {
    let channel = conn.openChannel('dhcp-info');

    channel.data.subscribe( (item) => {
         let device = resultsToObj(item);
         device = {
             interface: 'bridge1',
             ip: device.gateway,
             mac: false,
             dns: false,
             type: 'dhcp-server',
             host_name: false,
             status: 'connected'
        }
        let NewDevices = _.find(devices, { ip: device.ip })
        if (!!!NewDevices) {
            devices.push(Object.assign(device))
        }
        if (NewDevices) {
            let index = devices.indexOf(NewDevices)
            devices[index] = {
                ...NewDevices,
                type: device.type ? device.type : NewDevices.type,
            }
        }
    }, error => {
        console.log("Error during ipScanChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/ip/dhcp-server/network/print', [`=interval=10`])
    .then( result => {
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default ipScanChannel


File: /server\connectors\MikrotikApi\modules\dhcpServerChannel\index.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

import dhcpClients from './dhcpClients';
import dhcpServerInfo from './dhcpServerInfo';

const dhcpServerChannel = (conn, io, devices) => {
    console.log('dhcpServerChannel');
    dhcpClients(conn, io, devices);
    dhcpServerInfo(conn, io, devices)
}

export default dhcpServerChannel


File: /server\connectors\MikrotikApi\modules\interfaceInfo\index.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

import Info from './interfaceInfo';

const interfaceInfo = (conn, io, Interface) => {
    console.log('interfaceInfo');
    Info(conn, io, Interface)
}

export default interfaceInfo


File: /server\connectors\MikrotikApi\modules\interfaceInfo\interfaceInfo.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

const dhcpClients = (conn, io, Interface) => {
    let channel = conn.openChannel('interface-info');

    channel.data.subscribe( (item) => {
         let Eth = resultsToObj(item);
         Eth = {
             name: Eth.name,
             mac: Eth['mac-address'],
             rx: false,
             tx:  false,
             sum_rx: Eth['rx-byte'],
             sum_tx: Eth['tx-byte'],
             status: false
        }
        let NewEth = _.find(Interface, { name: Eth.name })
        if (!!!NewEth) {
            Interface.push(Object.assign(Eth))
        }
        if (NewEth) {
            let index = Interface.indexOf(NewEth)
            Interface[index] = {
                ...NewEth,
                sum_rx: Eth.sum_rx ? Eth.sum_rx : NewEth.sum_rx,
                sum_tx: Eth.sum_tx ? Eth.sum_tx : NewEth.sum_tx,
            }
        }
    }, error => {
        console.log("Error during ipScanChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/interface/print', ['=detail', '=interval=1'])
        .then( result => {
            console.log("Listen channel done promise.");
        })
        .catch( error => {
            console.log("Listen channel rejection:", error);
        });
}

export default dhcpClients


File: /server\connectors\MikrotikApi\modules\ipPingChannel\index.js
import { resultsToObj } from 'mikronode';
import ipPing from './ipPingChannel';
import _ from 'lodash';
import asyncInterval from 'asyncinterval';

const ipPingChannel = (conn, io, devices) => {
    console.log('ipPingChannel');

    asyncInterval( function(done){
        if (devices.length == 0) {
            done()
        } else {
            let devicesLength = devices.length;
            let couter = 0;
            const nextDevice = () => {
                couter++
                if (couter == devicesLength) {
                    done();
                }
            }
            _.forEach(devices, (elem, index) => {
                let channelName = `ipPing-${elem.ip.replace(/\./g,'-')}`
                let channel = conn.openChannel(channelName);
                ipPing(channel, io, devices, nextDevice, elem.ip);
            })
        }

    }, 10);
}

export default ipPingChannel


File: /server\connectors\MikrotikApi\modules\ipPingChannel\ipPingChannel.js
import { resultsToObj } from 'mikronode'
import _ from 'lodash';

const ipPingChannel = (channel, io, devices, done, ip_address) => {
    channel.write('/ping', [`=address=${ip_address}`, '=count=5'])
    .then( result => {
        let ping = resultsToObj(result.data);
        let status = _.every(ping, { 'status': 'timeout'})
        let indexDevice = null;
        if (status) {
            _.forEach(devices, (elem, index) => {
                if (elem.ip == ip_address) {
                    indexDevice = index
                }
            })
            devices[indexDevice].status = 'disconnected';
        } else {
            _.forEach(devices, (elem, index) => {
                if (elem.ip == ip_address) {
                    indexDevice = index
                }
            })
            devices[indexDevice].status = 'connected';
        }
        channel.close();
        done();
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default ipPingChannel


File: /server\connectors\MikrotikApi\modules\ipScanChannel\index.js
import scanInterface from './scanInterface';

const ipScanChannel = (conn, io, devices) => {
    console.log('scanInterface');
    scanInterface(conn, io, devices, 'eth1-wan');
    scanInterface(conn, io, devices, 'bridge1');
    scanInterface(conn, io, devices, 'eth2');
    scanInterface(conn, io, devices, 'eth3');
    scanInterface(conn, io, devices, 'eth4');
    scanInterface(conn, io, devices, 'eth5-master');
}

export default ipScanChannel


File: /server\connectors\MikrotikApi\modules\ipScanChannel\scanInterface.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

const ipScanChannel = (conn, io, devices, eth) => {
    let channel = conn.openChannel(`scan-${eth}`);
    channel.data.subscribe( (item) => {
         let device = resultsToObj(item);
         device = {
             interface: eth,
             ip: device.address,
             mac: device['mac-address'] || false,
             dns: device.dns || false,
             type: false,
             host_name:  device.dns || false,
             status: 'connected'
        }
        let NewDevices = _.find(devices, { ip: device.ip })
        if (!!!NewDevices && (device.mac || device.dns) && device.ip !== '0.0.0.0') {
            devices.push(Object.assign(device))
        }
        if (NewDevices) {
            let index = devices.indexOf(NewDevices)
            devices[index] = {
                ...NewDevices,
                interface: device.interface ? device.interface : NewDevices.interface,
                mac: device.mac ? device.mac : NewDevices.mac,
                dns: device.dns ? device.dns : NewDevices.dns,
            }
        }
    }, error => {
        console.log("Error during ipScanChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });


    channel.write('/tool/ip-scan', [`=interface=${eth}`])
    .then( result => {
        console.log(result);
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default ipScanChannel


File: /server\connectors\MikrotikApi\modules\listenChannel\index.js
import status from './listenChannel';

const listenChannel = (conn, io, Interface) => {
    console.log('listenChannel');
    status(conn, io, Interface, 'eth1-wan');
    status(conn, io, Interface, 'eth2');
    status(conn, io, Interface, 'eth3');
    status(conn, io, Interface, 'eth4');
    status(conn, io, Interface, 'eth5-master');
}

export default listenChannel


File: /server\connectors\MikrotikApi\modules\listenChannel\listenChannel.js
import { resultsToObj } from 'mikronode'
import _ from 'lodash';

const listenChannel = (conn, io, Interface, eth) => {
    let channel = conn.openChannel(`listen-${eth}`);

    channel.data.subscribe( (item) => {
        let InterfaceEth = resultsToObj(item.data);
        InterfaceEth = {
            name: eth || false,
            status: InterfaceEth['link-partner-advertising'] ? 'connected' : 'disconnected'
        }
        let NewEth = _.find(Interface, { name: eth })
        if (NewEth) {
            let index = Interface.indexOf(NewEth)
            Interface[index] = {
                ...NewEth,
                status: InterfaceEth.status ? InterfaceEth.status : NewEth.status,
            }
        }

    }, error => {
        console.log("Error during listenChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/interface/ethernet/monitor', [`=numbers=${eth}`, '=interval=1'])
    .then( result => {
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default listenChannel


File: /server\connectors\MikrotikApi\modules\torchChannel\index.js
import torch from './torchChannel';

const torchChannel = (conn, io, devices) => {
    console.log('torchChannel');
    torch(conn, io, devices, 'bridge1')
}

export default torchChannel


File: /server\connectors\MikrotikApi\modules\torchChannel\torchChannel.js
import { resultsToObj } from 'mikronode'
import _ from 'lodash';

const streamChannel = (conn, io, devices, eth) => {
    var channel = conn.openChannel(`torch-${eth}`);

    channel.data.subscribe( (data) => {
         var device = resultsToObj(data);
         if ( device['src-address'] == '104.197.3.80' ) {
             console.log(device);
         }
         device = {
             interface: eth,
             ip: device['src-address'],
             mac: device['mac-address'] || false,
             dns: device.dns || false,
             type: false,
             host_name: false,
             status: 'connected'
        }
        if (!!device.ip && device.ip !== '255.255.255.255' && device.ip !== '0.0.0.0') {
            let NewDevices = _.find(devices, { ip: device.ip })
            if (!!!NewDevices) {
                devices.push(Object.assign(device))
            }
            if (NewDevices) {
                let index = devices.indexOf(NewDevices)
                devices[index] = {
                    ...NewDevices,
                    interface: device.interface ? device.interface : NewDevices.interface,
                }
            }
        }
    }, error => {
        console.log("Error during listenChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/tool/torch', ['=ip-protocol=any', '=src-address=0.0.0.0/0', `=interface=${eth}`])
    .then( result => {
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default streamChannel


File: /server\connectors\MikrotikApi\modules\trafficChannel\index.js
import traffic from './trafficChannel';

const trafficChannel = (conn, io, Interface) => {
    console.log('trafficChannel');
    traffic(conn, io, Interface, 'eth1-wan');
    traffic(conn, io, Interface, 'bridge1');
    traffic(conn, io, Interface, 'eth2');
    traffic(conn, io, Interface, 'eth3');
    traffic(conn, io, Interface, 'eth4');
    traffic(conn, io, Interface, 'eth5-master');
}

export default trafficChannel


File: /server\connectors\MikrotikApi\modules\trafficChannel\trafficChannel.js
import { resultsToObj } from 'mikronode';
import _ from 'lodash';

const trafficChannel = (conn, io, Interface, eth) => {
    let channel = conn.openChannel(`traffic-${eth}`);
    channel.data.subscribe( (item) => {
         let InterfaceEth = resultsToObj(item);
         let date =  Date.now() + Number(10800000);
         InterfaceEth = {
             name: InterfaceEth.name,
             rx: Number(InterfaceEth['rx-bits-per-second'])/1024,
             tx:  Number(InterfaceEth['tx-bits-per-second'])/1024,
             date: date
         }
         let NewEth = _.find(Interface, { name: InterfaceEth.name })
         if (NewEth) {
             let index = Interface.indexOf(NewEth)
             Interface[index] = {
                 ...NewEth,
                 rx:InterfaceEth.rx,
                 tx: InterfaceEth.tx,
                 date: InterfaceEth.date
             }
         }
    }, error => {
        console.log("Error during ipScanChannel subscription",error)
    }, () => {
        console.log("Listen channel done.");
    });

    channel.write('/interface/monitor-traffic', [`=interface=${eth}`])
    .then( result => {
        console.log("Listen channel done promise.");
    })
    .catch( error => {
        console.log("Listen channel rejection:", error);
    });
}

export default trafficChannel


File: /server\connectors\soketIO\index.js
import disconnect from './modules/disconnect';

export default (io, devices) => {

  var connections = [];

  io.on('connection', socket => {

    connections.push(Object.assign(socket, { userID: Date.now() }));

    console.log(`Connect: players ID: ${socket.userID} `);
    console.log(`Connect: ${connections.length} sockets connected`);

    socket.emit('get_devices', devices)

    disconnect(io, socket, connections);
  })
}


File: /server\connectors\soketIO\modules\disconnect.js
export default (io, socket, connections) => {
  socket.on('disconnect', () => {
    console.log(`Disconnected: user ID: ${socket.userID} `);
    connections.splice(connections.indexOf(socket), 1);
  })
}


File: /server\handlers\error.js
export default function (err, req, res, next) {
    let { status = 500, message ="Server Error"} = err
    return res
    .status(status)
    .json({message})
}


File: /server\handlers\index.js
import bodyParser from 'body-parser';
import error from './error.js';
import cors from 'cors';

export default (app) => {
  app.use(error);
  app.use(cors({
    origin: true,
    credentials: true
  }));
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));
};


File: /server\server.js
import { createServer } from 'http';
import socketIO from 'socket.io';

import app from './app';
import SOKET_IO from './connectors/soketIO';
import MikrotikAPI from './connectors/MikrotikApi';

const server = createServer(app);

import { PORT } from './config';

let devices = [];
let Interface = [];

const io = socketIO(server);

SOKET_IO(io, devices, Interface);
MikrotikAPI(io, devices, Interface);

const timerID1 = setInterval(() => {
    io.emit('get_devices', devices)
}, 5000)

const timerID2 = setInterval(() => {
    io.emit('get_Interface', Interface)
}, 1000)

server.listen( PORT, (err) => {
  if (err) throw err;
  console.log(`Server running on port: ${PORT}`);
});

export default server


File: /utils\env.js
import envs from '../constants/envs';

const ENV = process.env.NODE_ENV || 'development';
const IS_DEV = ENV === envs.development;
const IS_PROD = ENV === envs.production;
const IS_TEST = ENV === envs.test;

export {
  IS_DEV,
  IS_PROD,
  IS_TEST,
};

export default ENV;


File: /webpack.config.js
const webpack = require('webpack');
const path = require('path');

const clientConfig = require('./config/client-config.json');
const serverConfig = require('./config/client-config.json');

const CLIENT_PORT = `${clientConfig.port}`;
const SERVER_PORT = `${clientConfig.port}`;
const SERVER_URL = `${clientConfig.url}`;

const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

const config = {
    entry: {
        app: [
			path.resolve(__dirname, './client/src/index.js')
        ]
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, './build'),
        publicPath: "/"
    },
    module: {
        rules: [
            {
                test: /\.css|scss$/,
                use: ['style-loader', 'css-loader', 'sass-loader'],
            },
            {
                test: /\.jsx?$/,