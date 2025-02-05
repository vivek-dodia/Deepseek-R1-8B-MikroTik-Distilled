# Repository Information
Name: MikroTikMiniApi

# Directory Structure
Directory structure:
└── github_repos/MikroTikMiniApi/
    ├── .editorconfig
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
    │   │       ├── pack-2738b4a665ebbc8d5124c308156f3d4cca35fd9d.idx
    │   │       └── pack-2738b4a665ebbc8d5124c308156f3d4cca35fd9d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── MikroTikMiniApi/
    │   ├── AssemblyInfo.cs
    │   ├── Commands/
    │   │   └── ApiCommand.cs
    │   ├── Exceptions/
    │   │   ├── AuthenticationFaultException.cs
    │   │   ├── CommandExecutionFaultException.cs
    │   │   ├── ReceivingModelValueFaultException.cs
    │   │   └── SentenceCreationFaultException.cs
    │   ├── Factories/
    │   │   ├── ApiSentenceFactory.cs
    │   │   └── MicrotikApiFactory.cs
    │   ├── Interfaces/
    │   │   ├── Commands/
    │   │   │   └── IApiCommand.cs
    │   │   ├── Factories/
    │   │   │   ├── IApiFactory.cs
    │   │   │   ├── IApiSentenceFactory.cs
    │   │   │   └── IModelFactory.cs
    │   │   ├── IRouterApi.cs
    │   │   ├── Models/
    │   │   │   └── Settings/
    │   │   │       ├── IConnectionSettings.cs
    │   │   │       └── IExecutionSettings.cs
    │   │   ├── Networking/
    │   │   │   └── IConnection.cs
    │   │   ├── Sentences/
    │   │   │   ├── IApiDoneSentence.cs
    │   │   │   ├── IApiFatalSentence.cs
    │   │   │   ├── IApiReSentence.cs
    │   │   │   ├── IApiSentence.cs
    │   │   │   └── IApiTrapSentence.cs
    │   │   └── Services/
    │   │       ├── IAuthenticationService.cs
    │   │       ├── ICommandExecutionService.cs
    │   │       └── ILocalizationService.cs
    │   ├── MicrotikApi.cs
    │   ├── MikroTikMiniApi.csproj
    │   ├── MikroTikMiniApi.xml
    │   ├── Models/
    │   │   ├── Api/
    │   │   │   ├── Interface.cs
    │   │   │   ├── Log.cs
    │   │   │   ├── ModelBase.cs
    │   │   │   ├── Package.cs
    │   │   │   └── Service.cs
    │   │   └── Settings/
    │   │       ├── ConnectionSettings.cs
    │   │       └── ExecutionSettings.cs
    │   ├── Networking/
    │   │   └── Connection.cs
    │   ├── Parameters/
    │   │   └── ApiCommandParameter.cs
    │   ├── Resources/
    │   │   ├── Strings.Designer.cs
    │   │   ├── Strings.resx
    │   │   └── Strings.ru-RU.resx
    │   ├── Sentences/
    │   │   ├── ApiDoneSentence.cs
    │   │   ├── ApiFatalSentence.cs
    │   │   ├── ApiReSentence.cs
    │   │   ├── ApiSentenceBase.cs
    │   │   └── ApiTrapSentence.cs
    │   ├── Services/
    │   │   ├── AuthenticationService.cs
    │   │   ├── CommandExecutionService.cs
    │   │   └── LocalizationService.cs
    │   └── Utilities/
    │       └── Guard.cs
    ├── MikroTikMiniApi.Demo/
    │   ├── MikroTikMiniApi.Demo.csproj
    │   └── Program.cs
    ├── MikroTikMiniApi.sln
    ├── MikroTikMiniApi.Tests/
    │   ├── Infrastructure/
    │   │   ├── DataReceivingTestFaultException.cs
    │   │   ├── Networking/
    │   │   │   ├── FakeConnectionBase.cs
    │   │   │   ├── FakeConnectionExecuteCommandToListAsync.cs
    │   │   │   ├── FakeConnectionExecuteCommandToListAsyncFlushStream.cs
    │   │   │   ├── FakeConnectionQuitAsync.cs
    │   │   │   ├── FakeConnectionReceiveCommand.cs
    │   │   │   └── FakeConnectionSendCommand.cs
    │   │   └── SentenceConstants.cs
    │   ├── MikroTikMiniApi.Tests.csproj
    │   └── Services/
    │       ├── AuthenticationServiceTests.cs
    │       └── CommandExecutionServiceTests.cs
    └── README.md


# Content
File: /.editorconfig
﻿[*.cs]

# CS1591: Отсутствует комментарий XML для открытого видимого типа или члена
dotnet_diagnostic.CS1591.severity = none


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/ns-88/MikroTikMiniApi.git
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
0000000000000000000000000000000000000000 3a045be6f6979c437cc170d46f46ffb25364e68a vivek-dodia <vivek.dodia@icloud.com> 1738606324 -0500	clone: from https://github.com/ns-88/MikroTikMiniApi.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 3a045be6f6979c437cc170d46f46ffb25364e68a vivek-dodia <vivek.dodia@icloud.com> 1738606324 -0500	clone: from https://github.com/ns-88/MikroTikMiniApi.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3a045be6f6979c437cc170d46f46ffb25364e68a vivek-dodia <vivek.dodia@icloud.com> 1738606324 -0500	clone: from https://github.com/ns-88/MikroTikMiniApi.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e58a4c444f2dba6f426140fc881b5442a18bb44c refs/remotes/origin/develop
3a045be6f6979c437cc170d46f46ffb25364e68a refs/remotes/origin/master
092bb3fcde90af663c7ee6cf0d58f49397109ce1 refs/tags/v1.0
^e8365b2e5bf7db0991896977186321e8365127ae
a1ec173bd9e4fd16ded3f10c865105f36f39cff0 refs/tags/v1.0.1
^fe96745fc23d8f15d9ae9b99448ab50e4f7e659b
898743c6cb44d3e07c2f00eba876e2821c724225 refs/tags/v1.0.2
^3a045be6f6979c437cc170d46f46ffb25364e68a


File: /.git\refs\heads\master
3a045be6f6979c437cc170d46f46ffb25364e68a


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/

# Visual Studio 2015 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUNIT
*.VisualState.xml
TestResult.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# DNX
project.lock.json
artifacts/

*_i.c
*_p.c
*_i.h
*.ilk
*.meta
*.obj
*.pch
*.pdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
File: /MikroTikMiniApi\AssemblyInfo.cs
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

[assembly: ComVisible(false)]

[assembly: Guid("7740d530-fd77-46e3-8c7d-be2d2b450d42")]

[assembly: InternalsVisibleTo("MikroTikMiniApi.Tests")]

File: /MikroTikMiniApi\Commands\ApiCommand.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Parameters;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Commands
{
    ///<inheritdoc cref="IApiCommand"/>
    public class ApiCommand : IApiCommand
    {
        private readonly List<ApiCommandParameter> _parameters;

        ///<inheritdoc/>
        public string Text { get; }

        ///<inheritdoc/>
        public IReadOnlyList<ApiCommandParameter> Parameters { get; }

        private ApiCommand(string text)
        {
            Guard.ThrowIfEmptyString(text, nameof(text));

            _parameters = new List<ApiCommandParameter>();

            Parameters = _parameters;
            Text = text;
        }

        #region Builder

        /// <summary>
        /// Creates a new command.
        /// </summary>
        /// <param name="text">Command text.</param>
        /// <returns>Command builder.</returns>
        public static ApiCommandBuilder New(string text)
        {
            return new ApiCommandBuilder(text);
        }

        /// <summary>
        /// Command builder.
        /// </summary>
        public class ApiCommandBuilder
        {
            private readonly ApiCommand _command;

            internal ApiCommandBuilder(string text)
            {
                _command = new ApiCommand(text);
            }

            /// <inheritdoc cref="ApiCommandParameter(string)"/>
            public ApiCommandBuilder AddParameter(string text)
            {
                _command._parameters.Add(new ApiCommandParameter(text));
                return this;
            }

            /// <inheritdoc cref="ApiCommandParameter(string, string)"/>
            public ApiCommandBuilder AddParameter(string name, string value)
            {
                _command._parameters.Add(new ApiCommandParameter(name, value));
                return this;
            }

            /// <summary>
            /// Returns a ready-to-use command.
            /// </summary>
            /// <returns>Command.</returns>
            public IApiCommand Build()
            {
                return _command;
            }
        }

        #endregion
    }
}

File: /MikroTikMiniApi\Exceptions\AuthenticationFaultException.cs
﻿using System;

namespace MikroTikMiniApi.Exceptions
{
    /// <summary>
    /// An exception thrown in case of an authentication error or logout.
    /// </summary>
    public class AuthenticationFaultException : Exception
    {
        public AuthenticationFaultException(string message)
            : base(message)
        {
        }
    }
}

File: /MikroTikMiniApi\Exceptions\CommandExecutionFaultException.cs
﻿using System;

namespace MikroTikMiniApi.Exceptions
{
    /// <summary>
    /// An exception thrown in case of an error when executing a command.
    /// </summary>
    public class CommandExecutionFaultException : Exception
    {
        public CommandExecutionFaultException(string message)
            : base(message)
        {
        }

        public CommandExecutionFaultException(string message, Exception exception) 
            : base(message, exception)
        {
        }
    }
}

File: /MikroTikMiniApi\Exceptions\ReceivingModelValueFaultException.cs
﻿using System;

namespace MikroTikMiniApi.Exceptions
{
    /// <summary>
    /// The exception that is thrown when an error occurs when getting the value of a model field.
    /// </summary>
    public class ReceivingModelValueFaultException : Exception
    {
        public ReceivingModelValueFaultException(string message)
            : base(message)
        {
        }
    }
}

File: /MikroTikMiniApi\Exceptions\SentenceCreationFaultException.cs
﻿using System;

namespace MikroTikMiniApi.Exceptions
{
    /// <summary>
    /// An exception is thrown if an error occurs when creating an API response sentence.
    /// </summary>
    public class SentenceCreationFaultException : Exception
    {
        public SentenceCreationFaultException(string message)
            : base(message)
        {
        }
    }
}

File: /MikroTikMiniApi\Factories\ApiSentenceFactory.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Exceptions;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Sentences;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Factories
{
    using ILocalizationService = IApiSentenceLocalizationService;
    using static ApiSentenceBase;

    ///<inheritdoc cref="IApiSentenceFactory"/>
    internal class ApiSentenceFactory : IApiSentenceFactory
    {
        private readonly ILocalizationService _localizationService;

        public ApiSentenceFactory(ILocalizationService localizationService)
        {
            Guard.ThrowIfNull(localizationService, out _localizationService, nameof(localizationService));
        }

        ///<inheritdoc/>
        IApiSentence IApiSentenceFactory.Create(string sentenceName, IReadOnlyList<string> words)
        {
            words ??= new List<string>();

            return sentenceName switch
            {
                "!done" => new ApiDoneSentence(words, _localizationService),
                "!trap" => new ApiTrapSentence(words, _localizationService),
                "!re" => new ApiReSentence(words, _localizationService),
                "!fatal" => new ApiFatalSentence(words, _localizationService),
                "" => throw new SentenceCreationFaultException(_localizationService.GetResponseTypeNotReceivedText(GetTextInternal(words, _localizationService))),
                _ => throw new SentenceCreationFaultException(_localizationService.GetUnknownResponseTypeText(sentenceName, GetTextInternal(words, _localizationService)))
            };
        }

        ///<inheritdoc/>
        public IApiDoneSentence CreateDoneSentence(IReadOnlyList<string> words) => new ApiDoneSentence(words, _localizationService);

        ///<inheritdoc/>
        public IApiReSentence CreateReSentence(IReadOnlyList<string> words) => new ApiReSentence(words, _localizationService);

        ///<inheritdoc/>
        public IApiTrapSentence CreateTrapSentence(IReadOnlyList<string> words) => new ApiTrapSentence(words, _localizationService);

        ///<inheritdoc/>
        public IApiFatalSentence CreateFatalSentence(IReadOnlyList<string> words) => new ApiFatalSentence(words, _localizationService);
    }
}

File: /MikroTikMiniApi\Factories\MicrotikApiFactory.cs
﻿using System.Net;
using MikroTikMiniApi.Interfaces;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Networking;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Networking;
using MikroTikMiniApi.Services;

namespace MikroTikMiniApi.Factories
{
    ///<inheritdoc cref="IApiFactory"/>
    public class MicrotikApiFactory : IApiFactory
    {
        private readonly ILocalizationService _localizationService;

        ///<inheritdoc/>
        public IApiSentenceFactory ApiSentenceFactory { get; }

        public MicrotikApiFactory()
        {
            _localizationService = new LocalizationService();
            ApiSentenceFactory = new ApiSentenceFactory(_localizationService);
        }

        ///<inheritdoc/>
        public IControlledConnection CreateConnection(IPEndPoint endPoint)
        {
            return new Connection(endPoint, _localizationService);
        }

        ///<inheritdoc/>
        public IControlledConnection CreateConnection(IConnectionSettings settings)
        {
            return new Connection(settings, _localizationService);
        }

        ///<inheritdoc/>
        public IRouterApi CreateRouterApi(IConnection connection)
        {
            return new MicrotikApi(connection, _localizationService, ApiSentenceFactory);
        }
    }
}

File: /MikroTikMiniApi\Interfaces\Commands\IApiCommand.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Parameters;

namespace MikroTikMiniApi.Interfaces.Commands
{
    /// <summary>
    /// API command.
    /// </summary>
    public interface IApiCommand
    {
        /// <summary>
        /// The text of the command. Must be specified.
        /// </summary>
        public string Text { get; }

        /// <summary>
        /// Command parameters. May not be specified.
        /// </summary>
        IReadOnlyList<ApiCommandParameter> Parameters { get; }
    }
}

File: /MikroTikMiniApi\Interfaces\Factories\IApiFactory.cs
﻿using System.Net;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Networking;

namespace MikroTikMiniApi.Interfaces.Factories
{
    /// <summary>
    /// API component factory.
    /// </summary>
    public interface IApiFactory
    {
        /// <summary>
        /// Returns a factory that creates API sentences.
        /// </summary>
        IApiSentenceFactory ApiSentenceFactory { get; }

        /// <summary>
        /// Creates only the connection object. Connection is not made.
        /// </summary>
        /// <param name="endPoint">The end point. Includes IP address and port.</param>
        /// <returns>Connection object.</returns>
        IControlledConnection CreateConnection(IPEndPoint endPoint);

        /// <summary>
        /// Creates only the connection object. Connection is not made.
        /// </summary>
        /// <param name="settings">Connection settings.</param>
        /// <returns>Connection object.</returns>
        IControlledConnection CreateConnection(IConnectionSettings settings);

        /// <summary>
        /// Creates an object containing all the methods for working with the API.
        /// </summary>
        /// <param name="connection">Connection object. The connection must be established.</param>
        /// <returns>API object.</returns>
        IRouterApi CreateRouterApi(IConnection connection);
    }
}

File: /MikroTikMiniApi\Interfaces\Factories\IApiSentenceFactory.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Interfaces.Factories
{
    /// <summary>
    /// A factory that creates API sentences.
    /// </summary>
    public interface IApiSentenceFactory
    {
        /// <summary>
        /// Creates an API sentence.
        /// </summary>
        /// <param name="sentenceName">Sentence name.</param>
        /// <param name="words">Words that make up a sentence.</param>
        /// <returns>API sentence.</returns>
        internal IApiSentence Create(string sentenceName, IReadOnlyList<string> words);

        /// <summary>
        /// Creates an API sentence of the "Done" type.
        /// </summary>
        /// <param name="words">Words that make up a sentence.</param>
        /// <returns>API sentence.</returns>
        IApiDoneSentence CreateDoneSentence(IReadOnlyList<string> words);

        /// <summary>
        /// Creates an API sentence of the "Re" type.
        /// </summary>
        /// <param name="words">Words that make up a sentence.</param>
        /// <returns>API sentence.</returns>
        IApiReSentence CreateReSentence(IReadOnlyList<string> words);

        /// <summary>
        /// Creates an API sentence of the "Trap" type.
        /// </summary>
        /// <param name="words">Words that make up a sentence.</param>
        /// <returns>API sentence.</returns>
        IApiTrapSentence CreateTrapSentence(IReadOnlyList<string> words);

        /// <summary>
        /// Creates an API sentence of the "Fatal" type.
        /// </summary>
        /// <param name="words">Words that make up a sentence.</param>
        /// <returns>API sentence.</returns>
        IApiFatalSentence CreateFatalSentence(IReadOnlyList<string> words);
    }
}

File: /MikroTikMiniApi\Interfaces\Factories\IModelFactory.cs
﻿using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Interfaces.Factories
{
    /// <summary>
    /// Data model factory.
    /// </summary>
    /// <typeparam name="T">Model type.</typeparam>
    public interface IModelFactory<out T> where T : class
    {
        /// <summary>
        /// Creates a data model.
        /// </summary>
        /// <param name="sentence">The API sentence from which the model is created.</param>
        /// <returns>Data model.</returns>
        T Create(IApiSentence sentence);
    }
}

File: /MikroTikMiniApi\Interfaces\IRouterApi.cs
﻿using System.Collections.Generic;
using System.Threading.Tasks;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Interfaces
{
    /// <summary>
    /// API for interacting with the router - executing commands and receiving data.
    /// </summary>
    public interface IRouterApi
    {
        #region Comment
        /// <inheritdoc cref="Services.IAuthenticationService.AuthenticationAsync"/>
        #endregion
        Task AuthenticationAsync(string name, string password);

        #region Comment
        /// <inheritdoc cref="Services.IAuthenticationService.QuitAsync"/>
        #endregion
        Task QuitAsync();

        #region Comment
        /// <inheritdoc cref="Services.ICommandExecutionService.ExecuteCommandAsync"/>
        #endregion
        Task<IApiSentence> ExecuteCommandAsync(IApiCommand command, IExecutionSettings? settings = null);

        #region Comment
        /// <inheritdoc cref="Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync"/>
        #endregion
        IAsyncEnumerable<IApiSentence> ExecuteCommandToEnumerableAsync(IApiCommand command, IExecutionSettings? settings = null);

        #region Comment
        /// <inheritdoc cref="Services.ICommandExecutionService.ExecuteCommandToListAsync"/>
        #endregion
        Task<IReadOnlyList<IApiSentence>> ExecuteCommandToListAsync(IApiCommand command, IExecutionSettings? settings = null);

        #region Comment
        /// <inheritdoc cref="Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync"/>
        #endregion
        IAsyncEnumerable<T> ExecuteCommandToEnumerableAsync<T>(IApiCommand command, IExecutionSettings? settings = null)
            where T : class, IModelFactory<T>, new();

        #region Comment
        /// <inheritdoc cref="Services.ICommandExecutionService.ExecuteCommandToListAsync"/>
        #endregion
        Task<IReadOnlyList<T>> ExecuteCommandToListAsync<T>(IApiCommand command, IExecutionSettings? settings = null)
            where T : class, IModelFactory<T>, new();
    }
}

File: /MikroTikMiniApi\Interfaces\Models\Settings\IConnectionSettings.cs
﻿using System;
using System.Net;

namespace MikroTikMiniApi.Interfaces.Models.Settings
{
    /// <summary>
    /// Connection settings.
    /// </summary>
    public interface IConnectionSettings
    {
        /// <summary>
        /// End point. Default value: address = 192.168.88.1, port = 8728.
        /// </summary>
        IPEndPoint EndPoint { get; }

        /// <summary>
        /// Connection timeout. Default value: 20 sec.
        /// </summary>
        TimeSpan ConnectionTimeout { get; }

        /// <summary>
        /// Sending timeout. Default value: 30 sec.
        /// </summary>
        TimeSpan SendTimeout { get; }

        /// <summary>
        /// Receiving timeout. Default value: 30 sec.
        /// </summary>
        TimeSpan ReceiveTimeout { get; }
    }
}

File: /MikroTikMiniApi\Interfaces\Models\Settings\IExecutionSettings.cs
﻿namespace MikroTikMiniApi.Interfaces.Models.Settings
{
    /// <summary>
    /// Command execution settings.
    /// </summary>
    public interface IExecutionSettings
    {
        /// <summary>
        /// A sign that it is necessary to clean up the router's response stream.
        /// Clearing is called only if the type of the last API response was ApiTrapSentence.
        /// </summary>
        bool IsFlushResponseStream { get; }

        /// <summary>
        /// The number of sentences in the router's response stream that will be read if cleanup is enabled.
        /// </summary>
        uint AttemptsCount { get; }

        /// <summary>
        /// A sign that the router's response stream should be cleared before the ApiDoneSentence type of offer appears.
        /// If this parameter is "true", the value of the <see cref="AttemptsCount"/> parameter is ignored.
        /// </summary>
        bool FlushBeforeDoneSentence { get; }
    }
}

File: /MikroTikMiniApi\Interfaces\Networking\IConnection.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Interfaces.Networking
{
    /// <summary>
    /// TCP connection.
    /// </summary>
    public interface IConnection
    {
        /// <summary>
        /// Receiving data.
        /// </summary>
        /// <param name="buffer">Buffer to receive.</param>
        /// <returns>A task to wait for.</returns>
        ValueTask ReceiveAsync(Memory<byte> buffer);
        /// <summary>
        /// Sending data.
        /// </summary>
        /// <param name="buffer">Buffer to send.</param>
        /// <returns>A task to wait for.</returns>
        ValueTask SendAsync(ReadOnlyMemory<byte> buffer);
    }

    /// <summary>
    /// TCP connection that allows you to establish a connection and clear resources.
    /// </summary>
    public interface IControlledConnection : IConnection, IDisposable
    {
        /// <summary>
        /// Connecting to a remote host.
        /// </summary>
        /// <returns>A task to wait for.</returns>
        ValueTask ConnectAsync();
    }
}

File: /MikroTikMiniApi\Interfaces\Sentences\IApiDoneSentence.cs
﻿namespace MikroTikMiniApi.Interfaces.Sentences
{
    /// <summary>
    /// API sentence of the "Done" type.
    /// </summary>
    public interface IApiDoneSentence : IApiSentence
    {
    }
}

File: /MikroTikMiniApi\Interfaces\Sentences\IApiFatalSentence.cs
﻿namespace MikroTikMiniApi.Interfaces.Sentences
{
    /// <summary>
    /// API sentence of the "Fatal" type.
    /// </summary>
    public interface IApiFatalSentence : IApiSentence
    {
    }
}

File: /MikroTikMiniApi\Interfaces\Sentences\IApiReSentence.cs
﻿namespace MikroTikMiniApi.Interfaces.Sentences
{
    /// <summary>
    /// API sentence of the "Re" type.
    /// </summary>
    public interface IApiReSentence : IApiSentence
    {
    }
}

File: /MikroTikMiniApi\Interfaces\Sentences\IApiSentence.cs
﻿using System.Collections.Generic;

namespace MikroTikMiniApi.Interfaces.Sentences
{
    /// <summary>
    /// API sentence.
    /// </summary>
    public interface IApiSentence
    {
        /// <summary>
        /// Words that make up sentences.
        /// </summary>
        IReadOnlyList<string> Words { get; }

        /// <summary>
        /// Gets the value of the API word.
        /// </summary>
        /// <param name="word">API word.</param>
        /// <param name="value">Word value.</param>
        /// <returns>A sign that a word has meaning.</returns>
        bool TryGetWordValue(string word, out string value);

        /// <summary>
        /// Returns the words of a sentence as a single string.
        /// </summary>
        /// <returns>Text string.</returns>
        string GetText();
    }
}

File: /MikroTikMiniApi\Interfaces\Sentences\IApiTrapSentence.cs
﻿namespace MikroTikMiniApi.Interfaces.Sentences
{
    /// <summary>
    /// API sentence of the "Trap" type.
    /// </summary>
    public interface IApiTrapSentence : IApiSentence
    {
    }
}

File: /MikroTikMiniApi\Interfaces\Services\IAuthenticationService.cs
﻿using System.Threading.Tasks;

namespace MikroTikMiniApi.Interfaces.Services
{
    /// <summary>
    /// Service for user authentication and logout.
    /// </summary>
    internal interface IAuthenticationService
    {
        /// <summary>
        /// Authentication on the router. Must be performed before calling any other methods.
        /// </summary>
        /// <param name="name">User name.</param>
        /// <param name="password">User password.</param>
        /// <returns>A task to wait for.</returns>
        Task AuthenticationAsync(string name, string password);

        /// <summary>
        /// Log out of the system.
        /// </summary>
        /// <returns>A task to wait for.</returns>
        Task QuitAsync();
    }
}

File: /MikroTikMiniApi\Interfaces\Services\ICommandExecutionService.cs
﻿using System.Collections.Generic;
using System.Threading.Tasks;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Interfaces.Services
{
    /// <summary>
    /// Service for executing API commands.
    /// </summary>
    internal interface ICommandExecutionService
    {
        /// <summary>
        /// Sends an API command to the router.
        /// </summary>
        /// <param name="command">API command.</param>
        /// <returns>A task to wait for.</returns>
        internal ValueTask SendCommandAsync(IApiCommand command);

        /// <summary>
        /// Gets the result of executing the command in the form of a single API sentence.
        /// </summary>
        /// <returns>API sentence.</returns>
        internal ValueTask<IApiSentence> ReceiveSentenceAsync();

        /// <summary>
        /// Clears the router API response stream. Called only if the type of the last API response was ApiTrapSentence.
        /// </summary>
        /// <param name="settings"></param>
        /// <returns>Received sentences from the stream.</returns>
        internal ValueTask<IReadOnlyList<IApiSentence>> FlushResponseStreamAsync(IExecutionSettings settings);

        /// <summary>
        /// Executes the command returning a scalar result.
        /// </summary>
        /// <param name="command">API command.</param>
        /// <param name="settings">Execution settings.</param>
        /// <returns>API sentence.</returns>
        Task<IApiSentence> ExecuteCommandAsync(IApiCommand command, IExecutionSettings? settings = null);

        /// <summary>
        /// Executes a command that returns the result as an asynchronous enumerator of elements of the type <see cref="IApiSentence"/>.
        /// </summary>
        /// <param name="command">API command.</param>
        /// <param name="settings">Execution settings.</param>
        /// <returns>An enumerator for receiving command results asynchronously.</returns>
        IAsyncEnumerable<IApiSentence> ExecuteCommandToEnumerableAsync(IApiCommand command, IExecutionSettings? settings = null);

        /// <summary>
        /// Executes a command that returns the result as a collection of elements of type <see cref="IApiSentence"/>.
        /// </summary>
        /// <param name="command">API command.</param>
        /// <param name="settings">Execution settings.</param>
        /// <returns>Collection of elements.</returns>
        Task<IReadOnlyList<IApiSentence>> ExecuteCommandToListAsync(IApiCommand command, IExecutionSettings? settings = null);

        /// <summary>
        /// Executes a command that returns the result as an asynchronous enumerator of elements of a user-defined type.
        /// </summary>
        /// <typeparam name="T">A data model that is also a factory that creates objects of this type.</typeparam>
        /// <param name="command">API command.</param>
        /// <param name="settings">Execution settings.</param>
        /// <returns>An enumerator for receiving command results asynchronously.</returns>
        IAsyncEnumerable<T> ExecuteCommandToEnumerableAsync<T>(IApiCommand command, IExecutionSettings? settings = null)
            where T : class, IModelFactory<T>, new();

        /// <summary>
        /// Executes a command that returns the result as a collection of elements of a user-defined type.
        /// </summary>
        /// <typeparam name="T">A data model that is also a factory that creates objects of this type.</typeparam>
        /// <param name="command">API command.</param>
        /// <param name="settings">Execution settings.</param>
        /// <returns>Collection of elements.</returns>
        Task<IReadOnlyList<T>> ExecuteCommandToListAsync<T>(IApiCommand command, IExecutionSettings? settings = null)
            where T : class, IModelFactory<T>, new();
    }
}

File: /MikroTikMiniApi\Interfaces\Services\ILocalizationService.cs
﻿using System;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Interfaces.Services
{
    internal interface ILocalizationService : IAuthenticationLocalizationService,
                                              ICommandExecutionLocalizationService,
                                              IConnectionLocalizationService,
                                              IApiSentenceLocalizationService
    {
    }

    internal interface IAuthenticationLocalizationService
    {
        string GetAuthCmdFailedText();

        string GetAuthFailedText(IApiSentence sentence, string response);

        string GetAuthFailedIncorrectAnswerText(IApiSentence sentence);

        string GetLogoutCmdFailedText();

        string GetLogoutFailedText(IApiSentence sentence, string response);
    }

    internal interface ICommandExecutionLocalizationService
    {
        string GetCmdSendingNotCompletedText();

        string GetSendingCmdDataNotCompletedText();

        string GetResponseNotReceivedText();

        string GetResponseStreamNotClearedText();

        string GetResponseWordNotReceivedText();

        string GetSentenceNameNotReceivedText();

        string GetWordLengthValueNotReceivedText();

        string GetRecvSeqNotCompleteUnknownRespTypeText(IApiSentence sentence, string response);

        string GetRecvSeqNotCompleteText(IApiSentence sentence, string response);
    }

    internal interface IConnectionLocalizationService
    {
        string GetConnectionTimeoutText(TimeSpan timeout);

        string GetDataSendingTimeoutText(TimeSpan timeout);

        string GetDataReceivingTimeoutText(TimeSpan timeout);

        string GetConnectionLostText();
    }

    internal interface IApiSentenceLocalizationService
    {
        string GetResponseTypeNotReceivedText(string response);

        string GetUnknownResponseTypeText(string sentenceName, string responce);

        string GetResponseIsEmptyText();
    }
}

File: /MikroTikMiniApi\MicrotikApi.cs
﻿using System.Collections.Generic;
using System.Threading.Tasks;
using MikroTikMiniApi.Interfaces;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Networking;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Services;

namespace MikroTikMiniApi
{
    ///<inheritdoc cref="IRouterApi"/>
    internal class MicrotikApi : IRouterApi
    {
        private readonly IAuthenticationService _authenticationService;
        private readonly ICommandExecutionService _commandExecutionService;

        public MicrotikApi(IConnection connection, ILocalizationService localizationService, IApiSentenceFactory sentenceFactory)
        {
            _commandExecutionService = new CommandExecutionService(connection, localizationService, sentenceFactory);
            _authenticationService = new AuthenticationService(_commandExecutionService, localizationService);
        }

        ///<inheritdoc/>
        public Task AuthenticationAsync(string name, string password)
        {
            return _authenticationService.AuthenticationAsync(name, password);
        }

        ///<inheritdoc/>
        public Task QuitAsync()
        {
            return _authenticationService.QuitAsync();
        }

        ///<inheritdoc/>
        public Task<IApiSentence> ExecuteCommandAsync(IApiCommand command, IExecutionSettings? settings)
        {
            return _commandExecutionService.ExecuteCommandAsync(command, settings);
        }

        ///<inheritdoc/>
        public IAsyncEnumerable<IApiSentence> ExecuteCommandToEnumerableAsync(IApiCommand command, IExecutionSettings? settings)
        {
            return _commandExecutionService.ExecuteCommandToEnumerableAsync(command, settings);
        }

        ///<inheritdoc/>
        public Task<IReadOnlyList<IApiSentence>> ExecuteCommandToListAsync(IApiCommand command, IExecutionSettings? settings)
        {
            return _commandExecutionService.ExecuteCommandToListAsync(command, settings);
        }

        ///<inheritdoc/>
        public IAsyncEnumerable<T> ExecuteCommandToEnumerableAsync<T>(IApiCommand command, IExecutionSettings? settings)
            where T : class, IModelFactory<T>, new()
        {
            return _commandExecutionService.ExecuteCommandToEnumerableAsync<T>(command, settings);
        }

        ///<inheritdoc/>
        public Task<IReadOnlyList<T>> ExecuteCommandToListAsync<T>(IApiCommand command, IExecutionSettings? settings)
            where T : class, IModelFactory<T>, new()
        {
            return _commandExecutionService.ExecuteCommandToListAsync<T>(command, settings);
        }
    }
}

File: /MikroTikMiniApi\MikroTikMiniApi.csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

	<PropertyGroup>
		<TargetFramework>net5.0</TargetFramework>
		<Platforms>x64</Platforms>
		<GeneratePackageOnBuild>false</GeneratePackageOnBuild>
		<Authors>ns-88</Authors>
		<Company />
		<Product>MikroTikMiniApi</Product>
		<PackageLicenseExpression>MIT</PackageLicenseExpression>
		<Description>A small and lightweight library for working with the MikroTik router API in C#.</Description>
		<RepositoryUrl>https://github.com/ns-88/MikroTikMiniApi/</RepositoryUrl>
		<RepositoryType>git</RepositoryType>
		<PackageTags>MikroTik;MikroTikAPI</PackageTags>
		<PackageProjectUrl>https://github.com/ns-88/MikroTikMiniApi/</PackageProjectUrl>
		<NeutralLanguage>en</NeutralLanguage>
		<TreatWarningsAsErrors>true</TreatWarningsAsErrors>
		<Nullable>enable</Nullable>
		<Version>1.0.2</Version>
	</PropertyGroup>

	<PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
	  <DocumentationFile>MikroTikMiniApi.xml</DocumentationFile>
	  <DefineConstants />
	</PropertyGroup>

	<ItemGroup>
	  <None Include="..\.editorconfig" Link=".editorconfig" />
	</ItemGroup>

	<ItemGroup>
		<Compile Update="Resources\Strings.Designer.cs">
			<DesignTime>True</DesignTime>
			<AutoGen>True</AutoGen>
			<DependentUpon>Strings.resx</DependentUpon>
		</Compile>
	</ItemGroup>

	<ItemGroup>
		<EmbeddedResource Update="Resources\Strings.resx">
			<Generator>ResXFileCodeGenerator</Generator>
			<LastGenOutput>Strings.Designer.cs</LastGenOutput>
		</EmbeddedResource>
		<EmbeddedResource Update="Resources\Strings.ru-RU.resx">
			<Generator></Generator>
		</EmbeddedResource>
	</ItemGroup>

</Project>


File: /MikroTikMiniApi\MikroTikMiniApi.xml
<?xml version="1.0"?>
<doc>
    <assembly>
        <name>MikroTikMiniApi</name>
    </assembly>
    <members>
        <member name="T:MikroTikMiniApi.Commands.ApiCommand">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Commands.IApiCommand"/>
        </member>
        <member name="P:MikroTikMiniApi.Commands.ApiCommand.Text">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Commands.ApiCommand.Parameters">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Commands.ApiCommand.New(System.String)">
            <summary>
            Creates a new command.
            </summary>
            <param name="text">Command text.</param>
            <returns>Command builder.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Commands.ApiCommand.ApiCommandBuilder">
            <summary>
            Command builder.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Commands.ApiCommand.ApiCommandBuilder.AddParameter(System.String)">
            <inheritdoc cref="M:MikroTikMiniApi.Parameters.ApiCommandParameter.#ctor(System.String)"/>
        </member>
        <member name="M:MikroTikMiniApi.Commands.ApiCommand.ApiCommandBuilder.AddParameter(System.String,System.String)">
            <inheritdoc cref="M:MikroTikMiniApi.Parameters.ApiCommandParameter.#ctor(System.String,System.String)"/>
        </member>
        <member name="M:MikroTikMiniApi.Commands.ApiCommand.ApiCommandBuilder.Build">
            <summary>
            Returns a ready-to-use command.
            </summary>
            <returns>Command.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Exceptions.AuthenticationFaultException">
            <summary>
            An exception thrown in case of an authentication error or logout.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Exceptions.CommandExecutionFaultException">
            <summary>
            An exception thrown in case of an error when executing a command.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Exceptions.ReceivingModelValueFaultException">
            <summary>
            The exception that is thrown when an error occurs when getting the value of a model field.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Exceptions.SentenceCreationFaultException">
            <summary>
            An exception is thrown if an error occurs when creating an API response sentence.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Factories.ApiSentenceFactory">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory"/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.ApiSentenceFactory.MikroTikMiniApi#Interfaces#Factories#IApiSentenceFactory#Create(System.String,System.Collections.Generic.IReadOnlyList{System.String})">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.ApiSentenceFactory.CreateDoneSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.ApiSentenceFactory.CreateReSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.ApiSentenceFactory.CreateTrapSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.ApiSentenceFactory.CreateFatalSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Factories.MicrotikApiFactory">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Factories.IApiFactory"/>
        </member>
        <member name="P:MikroTikMiniApi.Factories.MicrotikApiFactory.ApiSentenceFactory">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.MicrotikApiFactory.CreateConnection(System.Net.IPEndPoint)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.MicrotikApiFactory.CreateConnection(MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Factories.MicrotikApiFactory.CreateRouterApi(MikroTikMiniApi.Interfaces.Networking.IConnection)">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Commands.IApiCommand">
            <summary>
            API command.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Commands.IApiCommand.Text">
            <summary>
            The text of the command. Must be specified.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Commands.IApiCommand.Parameters">
            <summary>
            Command parameters. May not be specified.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Factories.IApiFactory">
            <summary>
            API component factory.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Factories.IApiFactory.ApiSentenceFactory">
            <summary>
            Returns a factory that creates API sentences.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiFactory.CreateConnection(System.Net.IPEndPoint)">
            <summary>
            Creates only the connection object. Connection is not made.
            </summary>
            <param name="endPoint">The end point. Includes IP address and port.</param>
            <returns>Connection object.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiFactory.CreateConnection(MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings)">
            <summary>
            Creates only the connection object. Connection is not made.
            </summary>
            <param name="settings">Connection settings.</param>
            <returns>Connection object.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiFactory.CreateRouterApi(MikroTikMiniApi.Interfaces.Networking.IConnection)">
            <summary>
            Creates an object containing all the methods for working with the API.
            </summary>
            <param name="connection">Connection object. The connection must be established.</param>
            <returns>API object.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory">
            <summary>
            A factory that creates API sentences.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory.Create(System.String,System.Collections.Generic.IReadOnlyList{System.String})">
            <summary>
            Creates an API sentence.
            </summary>
            <param name="sentenceName">Sentence name.</param>
            <param name="words">Words that make up a sentence.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory.CreateDoneSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <summary>
            Creates an API sentence of the "Done" type.
            </summary>
            <param name="words">Words that make up a sentence.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory.CreateReSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <summary>
            Creates an API sentence of the "Re" type.
            </summary>
            <param name="words">Words that make up a sentence.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory.CreateTrapSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <summary>
            Creates an API sentence of the "Trap" type.
            </summary>
            <param name="words">Words that make up a sentence.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IApiSentenceFactory.CreateFatalSentence(System.Collections.Generic.IReadOnlyList{System.String})">
            <summary>
            Creates an API sentence of the "Fatal" type.
            </summary>
            <param name="words">Words that make up a sentence.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Factories.IModelFactory`1">
            <summary>
            Data model factory.
            </summary>
            <typeparam name="T">Model type.</typeparam>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Factories.IModelFactory`1.Create(MikroTikMiniApi.Interfaces.Sentences.IApiSentence)">
            <summary>
            Creates a data model.
            </summary>
            <param name="sentence">The API sentence from which the model is created.</param>
            <returns>Data model.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.IRouterApi">
            <summary>
            API for interacting with the router - executing commands and receiving data.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.AuthenticationAsync(System.String,System.String)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.IAuthenticationService.AuthenticationAsync(System.String,System.String)"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.QuitAsync">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.IAuthenticationService.QuitAsync"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.ExecuteCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.ExecuteCommandToEnumerableAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)"/>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.IRouterApi.ExecuteCommandToListAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc cref="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)"/>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings">
            <summary>
            Connection settings.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings.EndPoint">
            <summary>
            End point. Default value: address = 192.168.88.1, port = 8728.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings.ConnectionTimeout">
            <summary>
            Connection timeout. Default value: 20 sec.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings.SendTimeout">
            <summary>
            Sending timeout. Default value: 30 sec.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings.ReceiveTimeout">
            <summary>
            Receiving timeout. Default value: 30 sec.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings">
            <summary>
            Command execution settings.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings.IsFlushResponseStream">
            <summary>
            A sign that it is necessary to clean up the router's response stream.
            Clearing is called only if the type of the last API response was ApiTrapSentence.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings.AttemptsCount">
            <summary>
            The number of sentences in the router's response stream that will be read if cleanup is enabled.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings.FlushBeforeDoneSentence">
            <summary>
            A sign that the router's response stream should be cleared before the ApiDoneSentence type of offer appears.
            If this parameter is "true", the value of the <see cref="P:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings.AttemptsCount"/> parameter is ignored.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Networking.IConnection">
            <summary>
            TCP connection.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Networking.IConnection.ReceiveAsync(System.Memory{System.Byte})">
            <summary>
            Receiving data.
            </summary>
            <param name="buffer">Buffer to receive.</param>
            <returns>A task to wait for.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Networking.IConnection.SendAsync(System.ReadOnlyMemory{System.Byte})">
            <summary>
            Sending data.
            </summary>
            <param name="buffer">Buffer to send.</param>
            <returns>A task to wait for.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Networking.IControlledConnection">
            <summary>
            TCP connection that allows you to establish a connection and clear resources.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Networking.IControlledConnection.ConnectAsync">
            <summary>
            Connecting to a remote host.
            </summary>
            <returns>A task to wait for.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Sentences.IApiDoneSentence">
            <summary>
            API sentence of the "Done" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Sentences.IApiFatalSentence">
            <summary>
            API sentence of the "Fatal" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Sentences.IApiReSentence">
            <summary>
            API sentence of the "Re" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Sentences.IApiSentence">
            <summary>
            API sentence.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Interfaces.Sentences.IApiSentence.Words">
            <summary>
            Words that make up sentences.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Sentences.IApiSentence.TryGetWordValue(System.String,System.String@)">
            <summary>
            Gets the value of the API word.
            </summary>
            <param name="word">API word.</param>
            <param name="value">Word value.</param>
            <returns>A sign that a word has meaning.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Sentences.IApiSentence.GetText">
            <summary>
            Returns the words of a sentence as a single string.
            </summary>
            <returns>Text string.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Sentences.IApiTrapSentence">
            <summary>
            API sentence of the "Trap" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Services.IAuthenticationService">
            <summary>
            Service for user authentication and logout.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.IAuthenticationService.AuthenticationAsync(System.String,System.String)">
            <summary>
            Authentication on the router. Must be performed before calling any other methods.
            </summary>
            <param name="name">User name.</param>
            <param name="password">User password.</param>
            <returns>A task to wait for.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.IAuthenticationService.QuitAsync">
            <summary>
            Log out of the system.
            </summary>
            <returns>A task to wait for.</returns>
        </member>
        <member name="T:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService">
            <summary>
            Service for executing API commands.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.SendCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand)">
            <summary>
            Sends an API command to the router.
            </summary>
            <param name="command">API command.</param>
            <returns>A task to wait for.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ReceiveSentenceAsync">
            <summary>
            Gets the result of executing the command in the form of a single API sentence.
            </summary>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.FlushResponseStreamAsync(MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Clears the router API response stream. Called only if the type of the last API response was ApiTrapSentence.
            </summary>
            <param name="settings"></param>
            <returns>Received sentences from the stream.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Executes the command returning a scalar result.
            </summary>
            <param name="command">API command.</param>
            <param name="settings">Execution settings.</param>
            <returns>API sentence.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Executes a command that returns the result as an asynchronous enumerator of elements of the type <see cref="T:MikroTikMiniApi.Interfaces.Sentences.IApiSentence"/>.
            </summary>
            <param name="command">API command.</param>
            <param name="settings">Execution settings.</param>
            <returns>An enumerator for receiving command results asynchronously.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Executes a command that returns the result as a collection of elements of type <see cref="T:MikroTikMiniApi.Interfaces.Sentences.IApiSentence"/>.
            </summary>
            <param name="command">API command.</param>
            <param name="settings">Execution settings.</param>
            <returns>Collection of elements.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToEnumerableAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Executes a command that returns the result as an asynchronous enumerator of elements of a user-defined type.
            </summary>
            <typeparam name="T">A data model that is also a factory that creates objects of this type.</typeparam>
            <param name="command">API command.</param>
            <param name="settings">Execution settings.</param>
            <returns>An enumerator for receiving command results asynchronously.</returns>
        </member>
        <member name="M:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService.ExecuteCommandToListAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <summary>
            Executes a command that returns the result as a collection of elements of a user-defined type.
            </summary>
            <typeparam name="T">A data model that is also a factory that creates objects of this type.</typeparam>
            <param name="command">API command.</param>
            <param name="settings">Execution settings.</param>
            <returns>Collection of elements.</returns>
        </member>
        <member name="T:MikroTikMiniApi.MicrotikApi">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.IRouterApi"/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.AuthenticationAsync(System.String,System.String)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.QuitAsync">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.ExecuteCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.ExecuteCommandToEnumerableAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.MicrotikApi.ExecuteCommandToListAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Models.Settings.ConnectionSettings">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Models.Settings.IConnectionSettings"/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ConnectionSettings.EndPoint">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ConnectionSettings.ConnectionTimeout">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ConnectionSettings.SendTimeout">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ConnectionSettings.ReceiveTimeout">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Models.Settings.ExecutionSettings">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings"/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ExecutionSettings.IsFlushResponseStream">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ExecutionSettings.AttemptsCount">
            <inheritdoc/>
        </member>
        <member name="P:MikroTikMiniApi.Models.Settings.ExecutionSettings.FlushBeforeDoneSentence">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Networking.Connection">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Networking.IControlledConnection"/>
        </member>
        <member name="M:MikroTikMiniApi.Networking.Connection.ConnectAsync">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Networking.Connection.ReceiveAsync(System.Memory{System.Byte})">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Networking.Connection.SendAsync(System.ReadOnlyMemory{System.Byte})">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Parameters.ApiCommandParameter">
            <summary>
            Command parameter.
            </summary>
        </member>
        <member name="M:MikroTikMiniApi.Parameters.ApiCommandParameter.#ctor(System.String)">
            <summary>
            Creates a new parameter with some arbitrary text.
            </summary>
            <param name="text">Arbitrary text.</param>
        </member>
        <member name="M:MikroTikMiniApi.Parameters.ApiCommandParameter.#ctor(System.String,System.String)">
            <summary>
            Creates a new parameter with a name and value.
            </summary>
            <param name="name">Parameter name.</param>
            <param name="value">Parameter value.</param>
        </member>
        <member name="T:MikroTikMiniApi.Resources.Strings">
            <summary>
              Класс ресурса со строгой типизацией для поиска локализованных строк и т.д.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResourceManager">
            <summary>
              Возвращает кэшированный экземпляр ResourceManager, использованный этим классом.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.Culture">
            <summary>
              Перезаписывает свойство CurrentUICulture текущего потока для всех
              обращений к ресурсу с помощью этого класса ресурса со строгой типизацией.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.AuthCmdFailed">
            <summary>
              Ищет локализованную строку, похожую на The authentication command was not executed..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.AuthFailed">
            <summary>
              Ищет локализованную строку, похожую на Authentication was not performed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.AuthFailedIncorrectAnswer">
            <summary>
              Ищет локализованную строку, похожую на Authentication was not performed. The API response &quot;{0}&quot; was expected to be empty..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.CmdSendingNotCompleted">
            <summary>
              Ищет локализованную строку, похожую на The command sending was not completed..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ConnectionLost">
            <summary>
              Ищет локализованную строку, похожую на Communication with the remote host is lost..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ConnectionTimeout">
            <summary>
              Ищет локализованную строку, похожую на The connection was not completed within the specified time period. Timeout: &quot;{0}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.DataReceivingTimeout">
            <summary>
              Ищет локализованную строку, похожую на The data was not received within the specified time period. Timeout: &quot;{0}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.DataSendingTimeout">
            <summary>
              Ищет локализованную строку, похожую на The data was not sent within the specified time period. Timeout: &quot;{0}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.LogoutCmdFailed">
            <summary>
              Ищет локализованную строку, похожую на The logout command was not executed..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.LogoutFailed">
            <summary>
              Ищет локализованную строку, похожую на The logout was not performed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ModelValueNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The value was not received. Expected type: &quot;{0}&quot;, field name: &quot;{1}&quot;, API response value: &quot;{2}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.RecvSeqNotComplete">
            <summary>
              Ищет локализованную строку, похожую на Getting the sequence was not completed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.RecvSeqNotCompleteUnknownRespType">
            <summary>
              Ищет локализованную строку, похожую на Getting the sequence was not completed - unknown type of API response. Response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResponseIsEmpty">
            <summary>
              Ищет локализованную строку, похожую на The response text is empty.
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResponseNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The API response was not received..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResponseStreamNotCleared">
            <summary>
              Ищет локализованную строку, похожую на The API response stream was not cleared..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResponseTypeNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The API response type was not received. Response text: &quot;{0}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.ResponseWordNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The API response word value was not received..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.SendingCmdDataNotCompleted">
            <summary>
              Ищет локализованную строку, похожую на The sending of the command data was not completed..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.SentenceNameNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The name of the sentence type was not received..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.UnknownResponseType">
            <summary>
              Ищет локализованную строку, похожую на Unknown API response type. Response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
            </summary>
        </member>
        <member name="P:MikroTikMiniApi.Resources.Strings.WordLengthValueNotReceived">
            <summary>
              Ищет локализованную строку, похожую на The API word length value was not received..
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Sentences.ApiDoneSentence">
            <summary>
            API sentence of the "Done" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Sentences.ApiFatalSentence">
            <summary>
            API sentence of the "Fatal" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Sentences.ApiReSentence">
            <summary>
            API sentence of the "Re" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Sentences.ApiSentenceBase">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Sentences.IApiSentence"/>
        </member>
        <member name="P:MikroTikMiniApi.Sentences.ApiSentenceBase.Words">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Sentences.ApiSentenceBase.TryGetWordValue(System.String,System.String@)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Sentences.ApiSentenceBase.GetText">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Sentences.ApiTrapSentence">
            <summary>
            API sentence of the "Trap" type.
            </summary>
        </member>
        <member name="T:MikroTikMiniApi.Services.AuthenticationService">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Services.IAuthenticationService"/>
        </member>
        <member name="M:MikroTikMiniApi.Services.AuthenticationService.AuthenticationAsync(System.String,System.String)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.AuthenticationService.QuitAsync">
            <inheritdoc/>
        </member>
        <member name="T:MikroTikMiniApi.Services.CommandExecutionService">
            <inheritdoc cref="T:MikroTikMiniApi.Interfaces.Services.ICommandExecutionService"/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.MikroTikMiniApi#Interfaces#Services#ICommandExecutionService#FlushResponseStreamAsync(MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.MikroTikMiniApi#Interfaces#Services#ICommandExecutionService#SendCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.MikroTikMiniApi#Interfaces#Services#ICommandExecutionService#ReceiveSentenceAsync">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.ExecuteCommandAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.ExecuteCommandToEnumerableAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.ExecuteCommandToListAsync(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.ExecuteCommandToEnumerableAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
        <member name="M:MikroTikMiniApi.Services.CommandExecutionService.ExecuteCommandToListAsync``1(MikroTikMiniApi.Interfaces.Commands.IApiCommand,MikroTikMiniApi.Interfaces.Models.Settings.IExecutionSettings)">
            <inheritdoc/>
        </member>
    </members>
</doc>


File: /MikroTikMiniApi\Models\Api\Interface.cs
﻿using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Models.Api
{
    public class Interface : ModelBase, IModelFactory<Interface>
    {
        public string? Name { get; private set; }
        public string? DefaultName { get; private set; }
        public string? Type { get; private set; }
        public string? Mtu { get; private set; }
        public int? ActualMtu { get; private set; }
        public int? L2Mtu { get; private set; }
        public int? MaxL2Mtu { get; private set; }
        public string? MacAddress { get; private set; }
        public string? LastLinkDownTime { get; private set; }
        public string? LastLinkUpTime { get; private set; }
        public int? LinkDowns { get; private set; }
        public ulong? RxByte { get; private set; }
        public ulong? TxByte { get; private set; }
        public ulong? RxPacket { get; private set; }
        public ulong? TxPacket { get; private set; }
        public ulong? RxDrop { get; private set; }
        public ulong? TxDrop { get; private set; }
        public ulong? TxQueueDrop { get; private set; }
        public ulong? RxError { get; private set; }
        public ulong? TxError { get; private set; }
        public ulong? FpRxByte { get; private set; }
        public ulong? FpTxByte { get; private set; }
        public ulong? FpRxPacket { get; private set; }
        public ulong? FpTxPacket { get; private set; }
        public bool? IsRunning { get; private set; }
        public bool? IsDisabled { get; private set; }

        Interface IModelFactory<Interface>.Create(IApiSentence sentence)
        {
            return new Interface
            {
                Id = GetStringValueOrDefault(".id", sentence),
                Name = GetStringValueOrDefault("name", sentence),
                DefaultName = GetStringValueOrDefault("default-name", sentence),
                Type = GetStringValueOrDefault("type", sentence),
                Mtu = GetStringValueOrDefault("mtu", sentence),
                ActualMtu = GetIntValueOrDefault("actual-mtu", sentence),
                L2Mtu = GetIntValueOrDefault("l2mtu", sentence),
                MaxL2Mtu = GetIntValueOrDefault("max-l2mtu", sentence),
                MacAddress = GetStringValueOrDefault("mac-address", sentence),
                LastLinkDownTime = GetStringValueOrDefault("last-link-down-time", sentence),
                LastLinkUpTime = GetStringValueOrDefault("last-link-up-time", sentence),
                LinkDowns = GetIntValueOrDefault("link-downs", sentence),
                RxByte = GetUlongValueOrDefault("rx-byte", sentence),
                TxByte = GetUlongValueOrDefault("tx-byte", sentence),
                RxPacket = GetUlongValueOrDefault("rx-packet", sentence),
                TxPacket = GetUlongValueOrDefault("tx-packet", sentence),
                RxDrop = GetUlongValueOrDefault("rx-drop", sentence),
                TxDrop = GetUlongValueOrDefault("tx-drop", sentence),
                TxQueueDrop = GetUlongValueOrDefault("tx-queue-drop", sentence),
                RxError = GetUlongValueOrDefault("rx-error", sentence),
                TxError = GetUlongValueOrDefault("tx-error", sentence),
                FpRxByte = GetUlongValueOrDefault("fp-rx-byte", sentence),
                FpTxByte = GetUlongValueOrDefault("fp-tx-byte", sentence),
                FpRxPacket = GetUlongValueOrDefault("fp-rx-packet", sentence),
                FpTxPacket = GetUlongValueOrDefault("fp-tx-packet", sentence),
                IsRunning = GetBoolValueOrDefault("running", sentence),
                IsDisabled = GetBoolValueOrDefault("disabled", sentence)
            };
        }
    }
}

File: /MikroTikMiniApi\Models\Api\Log.cs
﻿using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Models.Api
{
    public class Log : ModelBase, IModelFactory<Log>
    {
        public string? Time { get; private set; }
        public string? Topics { get; private set; }
        public string? Message { get; private set; }

        Log IModelFactory<Log>.Create(IApiSentence sentence)
        {
            return new Log
            {
                Id = GetStringValueOrDefault(".id", sentence),
                Time = GetStringValueOrDefault("time", sentence),
                Topics = GetStringValueOrDefault("topics", sentence),
                Message = GetStringValueOrDefault("message", sentence)
            };
        }
    }
}

File: /MikroTikMiniApi\Models\Api\ModelBase.cs
﻿using System;
using System.Runtime.CompilerServices;
using MikroTikMiniApi.Exceptions;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Resources;

namespace MikroTikMiniApi.Models.Api
{
    public abstract class ModelBase
    {
        public string? Id { get; protected set; }

        private static Exception GetException<TExpectedType>(string name, string value)
        {
            return new ReceivingModelValueFaultException(string.Format(Strings.ModelValueNotReceived, typeof(TExpectedType).Name, name, value));
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        protected static string? GetStringValueOrDefault(string name, IApiSentence sentence)
        {
            return sentence.TryGetWordValue(name, out var value)
                ? value
                : null;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        protected static int? GetIntValueOrDefault(string name, IApiSentence sentence)
        {
            if (!sentence.TryGetWordValue(name, out var textValue))
                return 0;
            
            if (int.TryParse(textValue, out var value))
                return value;

            throw GetException<int>(name, textValue);
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        protected static bool? GetBoolValueOrDefault(string name, IApiSentence sentence)
        {
            if (!sentence.TryGetWordValue(name, out var textValue))
                return null;

            if (bool.TryParse(textValue, out var value))
                return value;

            throw GetException<bool>(name, textValue);
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        protected static ulong? GetUlongValueOrDefault(string name, IApiSentence sentence)
        {
            if (!sentence.TryGetWordValue(name, out var textValue))
                return null;
            
            if (ulong.TryParse(textValue, out var value))
                return value;

            throw GetException<ulong>(name, textValue);
        }
    }
}

File: /MikroTikMiniApi\Models\Api\Package.cs
﻿using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Models.Api
{
    public class Package : ModelBase, IModelFactory<Package>
    {
        public string? Name { get; private set; }
        public string? Version { get; private set; }
        public string? BuildTime { get; private set; }
        public string? Scheduled { get; private set; }
        public bool? IsDisabled { get; private set; }

        Package IModelFactory<Package>.Create(IApiSentence sentence)
        {
            return new Package
            {
                Id = GetStringValueOrDefault(".id", sentence),
                Name = GetStringValueOrDefault("name", sentence),
                Version = GetStringValueOrDefault("version", sentence),
                BuildTime = GetStringValueOrDefault("build-time", sentence),
                Scheduled = GetStringValueOrDefault("scheduled", sentence),
                IsDisabled = GetBoolValueOrDefault("disabled", sentence)
            };
        }
    }
}

File: /MikroTikMiniApi\Models\Api\Service.cs
﻿using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;

namespace MikroTikMiniApi.Models.Api
{
    public class Service : ModelBase, IModelFactory<Service>
    { 
        public string? Name { get; private set; }
        public int? Port { get; private set; }
        public string? Address { get; private set; }
        public bool? IsInvalid { get; private set; }
        public bool? IsDisabled { get; private set; }

        Service IModelFactory<Service>.Create(IApiSentence sentence)
        {
            return new Service
            {
                Id = GetStringValueOrDefault(".id", sentence),
                Name = GetStringValueOrDefault("name", sentence),
                Port = GetIntValueOrDefault("port", sentence),
                Address = GetStringValueOrDefault("address", sentence),
                IsInvalid = GetBoolValueOrDefault("invalid", sentence),
                IsDisabled = GetBoolValueOrDefault("disabled", sentence)
            };
        }
    }
}

File: /MikroTikMiniApi\Models\Settings\ConnectionSettings.cs
﻿using System;
using System.Net;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Models.Settings
{
    ///<inheritdoc cref="IConnectionSettings"/>
    public class ConnectionSettings : IConnectionSettings
    {
        public static readonly ConnectionSettings Default;

        ///<inheritdoc/>
        public IPEndPoint EndPoint { get; private set; }

        ///<inheritdoc/>
        public TimeSpan ConnectionTimeout { get; private set; }

        ///<inheritdoc/>
        public TimeSpan SendTimeout { get; private set; }

        ///<inheritdoc/>
        public TimeSpan ReceiveTimeout { get; private set; }

        static ConnectionSettings()
        {
            Default = new ConnectionSettings(new IPEndPoint(IPAddress.Parse("192.168.88.1"), 8728));
        }

        public ConnectionSettings(IPEndPoint endPoint)
        {
            EndPoint = Guard.ThrowIfNullRet(endPoint, nameof(endPoint));
            ConnectionTimeout = TimeSpan.FromSeconds(20);
            SendTimeout = TimeSpan.FromSeconds(30);
            ReceiveTimeout = TimeSpan.FromSeconds(30);
        }

        #region Builder

        public ConnectionSettingsBuilder Builder => new(this);

        public class ConnectionSettingsBuilder
        {
            private readonly ConnectionSettings _settings;

            public ConnectionSettingsBuilder(IConnectionSettings settings)
            {
                _settings = new ConnectionSettings(settings.EndPoint)
                {
                    ConnectionTimeout = settings.ConnectionTimeout,
                    SendTimeout = settings.SendTimeout,
                    ReceiveTimeout = settings.ReceiveTimeout
                };
            }

            public ConnectionSettingsBuilder WithEndPoint(IPEndPoint endPoint)
            {
                _settings.EndPoint = Guard.ThrowIfNullRet(endPoint, nameof(endPoint));
                return this;
            }

            public ConnectionSettingsBuilder WithConnectionTimeout(TimeSpan timeout)
            {
                _settings.ConnectionTimeout = timeout;
                return this;
            }

            public ConnectionSettingsBuilder WithSendTimeout(TimeSpan timeout)
            {
                _settings.SendTimeout = timeout;
                return this;
            }

            public ConnectionSettingsBuilder WithReceiveTimeout(TimeSpan timeout)
            {
                _settings.ReceiveTimeout = timeout;
                return this;
            }

            public IConnectionSettings Build()
            {
                return _settings;
            }
        }

        #endregion
    }
}

File: /MikroTikMiniApi\Models\Settings\ExecutionSettings.cs
﻿using System.Runtime.CompilerServices;
using MikroTikMiniApi.Interfaces.Models.Settings;

namespace MikroTikMiniApi.Models.Settings
{
    ///<inheritdoc cref="IExecutionSettings"/>
    public class ExecutionSettings : IExecutionSettings
    {
        public static readonly ExecutionSettings Default;

        ///<inheritdoc/>
        public bool IsFlushResponseStream { get; private set; }

        ///<inheritdoc/>
        public uint AttemptsCount { get; private set; }

        ///<inheritdoc/>
        public bool FlushBeforeDoneSentence { get; private set; }

        static ExecutionSettings()
        {
            Default = new ExecutionSettings(true);
        }

        public ExecutionSettings(bool isFlushResponseStream)
        {
            IsFlushResponseStream = isFlushResponseStream;
            AttemptsCount = isFlushResponseStream ? 1U : 0;
            FlushBeforeDoneSentence = true;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        internal static IExecutionSettings GetValueOrDefault(IExecutionSettings? settings) => settings ?? Default;

        #region Builder

        public ExecutionSettingsBuilder Builder => new(this);

        public class ExecutionSettingsBuilder
        {
            private readonly ExecutionSettings _settings;

            public ExecutionSettingsBuilder(IExecutionSettings settings)
            {
                _settings = new ExecutionSettings(settings.IsFlushResponseStream)
                {
                    AttemptsCount = settings.AttemptsCount,
                    FlushBeforeDoneSentence = settings.FlushBeforeDoneSentence
                };
            }

            public ExecutionSettingsBuilder WithIsFlushResponseStream(bool isFlushResponseStream)
            {
                _settings.IsFlushResponseStream = isFlushResponseStream;
                return this;
            }

            public ExecutionSettingsBuilder WithAttemptsCount(uint attemptsCount)
            {
                _settings.AttemptsCount = attemptsCount;
                return this;
            }

            public ExecutionSettingsBuilder WithFlushBeforeDoneSentence(bool flushBeforeDoneSentence)
            {
                _settings.FlushBeforeDoneSentence = flushBeforeDoneSentence;
                return this;
            }

            public IExecutionSettings Build()
            {
                return _settings;
            }
        }

        #endregion
    }
}

File: /MikroTikMiniApi\Networking\Connection.cs
﻿using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Threading.Tasks;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Networking;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Models.Settings;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Networking
{
    using ILocalizationService = IConnectionLocalizationService;

    ///<inheritdoc cref="IControlledConnection"/>
    internal class Connection : IControlledConnection
    {
        private readonly IConnectionSettings _settings;
        private readonly ILocalizationService _localization;
        private readonly Socket _socket;
        private readonly SemaphoreSlim _semaphoreSendLock;
        private readonly SemaphoreSlim _semaphoreReceiveLock;
        private CancellationTokenSource _ctsSend;
        private CancellationTokenSource _ctsReceive;

#nullable disable
        private Connection(ILocalizationService localizationService)
        {
            Guard.ThrowIfNull(localizationService, out _localization, nameof(localizationService));
            
            _semaphoreSendLock = new SemaphoreSlim(1);
            _semaphoreReceiveLock = new SemaphoreSlim(1);
            _ctsSend = new CancellationTokenSource();
            _ctsReceive = new CancellationTokenSource();
        }
#nullable restore
        public Connection(IPEndPoint endPoint, ILocalizationService localizationService)
            : this(localizationService)
        {
            Guard.ThrowIfNull(endPoint, nameof(endPoint));

            _settings = new ConnectionSettings(endPoint);
            _socket = CreateSocket(_settings);
        }

        public Connection(IConnectionSettings settings, ILocalizationService localizationService)
            : this(localizationService)
        {
            Guard.ThrowIfNull(settings, out _settings, nameof(settings));
            _socket = CreateSocket(settings);
        }

        private static Socket CreateSocket(IConnectionSettings settings)
        {
            return new Socket(settings.EndPoint.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
        }

        ///<inheritdoc/>
        public async ValueTask ConnectAsync()
        {
            using var cts = new CancellationTokenSource(_settings.ConnectionTimeout);

            try
            {
                await _socket.ConnectAsync(_settings.EndPoint, cts.Token).ConfigureAwait(false);
            }
            catch (OperationCanceledException)
            {
                throw new TimeoutException(_localization.GetConnectionTimeoutText(_settings.ConnectionTimeout));
            }
        }

        ///<inheritdoc/>
        public async ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            var length = buffer.Length;
            var totalReceived = 0;

            await _semaphoreReceiveLock.WaitAsync().ConfigureAwait(false);

            try
            {
                _ctsReceive.CancelAfter(_settings.ReceiveTimeout);

                try
                {
                    while (true)
                    {
                        var received = await _socket.ReceiveAsync(buffer, SocketFlags.None, _ctsReceive.Token).ConfigureAwait(false);

                        if (received == 0)
                            throw new InvalidOperationException(_localization.GetConnectionLostText());

                        totalReceived += received;

                        if (totalReceived == length)
                            break;

                        buffer = buffer.Slice(received);
                    }
                }
                finally
                {
                    _ctsReceive.CancelAfter(Timeout.InfiniteTimeSpan);
                }
            }
            catch (OperationCanceledException)
            {
                _ctsReceive = new CancellationTokenSource();
                throw new TimeoutException(_localization.GetDataReceivingTimeoutText(_settings.ReceiveTimeout));
            }
            finally
            {
                _semaphoreReceiveLock.Release();
            }
        }

        ///<inheritdoc/>
        public async ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            var length = buffer.Length;
            var totalSent = 0;

            await _semaphoreSendLock.WaitAsync().ConfigureAwait(false);

            try
            {
                _ctsSend.CancelAfter(_settings.SendTimeout);

                try
                {
                    while (true)
                    {
                        var sent = await _socket.SendAsync(buffer, SocketFlags.None).ConfigureAwait(false);

                        totalSent += sent;

                        if (totalSent == length)
                            break;

                        buffer = buffer.Slice(sent);
                    }
                }
                finally
                {
                    _ctsSend.CancelAfter(Timeout.InfiniteTimeSpan);
                }
            }
            catch (OperationCanceledException)
            {
                _ctsSend = new CancellationTokenSource();
                throw new TimeoutException(_localization.GetDataSendingTimeoutText(_settings.SendTimeout));
            }
            finally
            {
                _semaphoreSendLock.Release();
            }
        }

        public void Dispose()
        {
            _socket?.Dispose();
            _semaphoreSendLock?.Dispose();
            _semaphoreReceiveLock?.Dispose();
            _ctsSend?.Dispose();
            _ctsReceive?.Dispose();
        }
    }
}

File: /MikroTikMiniApi\Parameters\ApiCommandParameter.cs
﻿using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Parameters
{
    /// <summary>
    /// Command parameter.
    /// </summary>
    public class ApiCommandParameter
    {
        private readonly string _text;

        /// <summary>
        /// Creates a new parameter with some arbitrary text.
        /// </summary>
        /// <param name="text">Arbitrary text.</param>
        internal ApiCommandParameter(string text)
        {
            Guard.ThrowIfEmptyString(text, out _text, nameof(text));
        }

        /// <summary>
        /// Creates a new parameter with a name and value.
        /// </summary>
        /// <param name="name">Parameter name.</param>
        /// <param name="value">Parameter value.</param>
        internal ApiCommandParameter(string name, string value)
        {
            Guard.ThrowIfEmptyString(name, nameof(name));
            Guard.ThrowIfEmptyString(value, nameof(value));

            _text = $"={name}={value}";
        }
        
        public static implicit operator string(ApiCommandParameter parameter)
        {
            return parameter._text;
        }
    }
}

File: /MikroTikMiniApi\Resources\Strings.Designer.cs
﻿//------------------------------------------------------------------------------
// <auto-generated>
//     Этот код создан программой.
//     Исполняемая версия:4.0.30319.42000
//
//     Изменения в этом файле могут привести к неправильной работе и будут потеряны в случае
//     повторной генерации кода.
// </auto-generated>
//------------------------------------------------------------------------------

namespace MikroTikMiniApi.Resources {
    using System;
    
    
    /// <summary>
    ///   Класс ресурса со строгой типизацией для поиска локализованных строк и т.д.
    /// </summary>
    // Этот класс создан автоматически классом StronglyTypedResourceBuilder
    // с помощью такого средства, как ResGen или Visual Studio.
    // Чтобы добавить или удалить член, измените файл .ResX и снова запустите ResGen
    // с параметром /str или перестройте свой проект VS.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "16.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Strings {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Strings() {
        }
        
        /// <summary>
        ///   Возвращает кэшированный экземпляр ResourceManager, использованный этим классом.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("MikroTikMiniApi.Resources.Strings", typeof(Strings).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Перезаписывает свойство CurrentUICulture текущего потока для всех
        ///   обращений к ресурсу с помощью этого класса ресурса со строгой типизацией.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The authentication command was not executed..
        /// </summary>
        internal static string AuthCmdFailed {
            get {
                return ResourceManager.GetString("AuthCmdFailed", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Authentication was not performed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
        /// </summary>
        internal static string AuthFailed {
            get {
                return ResourceManager.GetString("AuthFailed", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Authentication was not performed. The API response &quot;{0}&quot; was expected to be empty..
        /// </summary>
        internal static string AuthFailedIncorrectAnswer {
            get {
                return ResourceManager.GetString("AuthFailedIncorrectAnswer", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The command sending was not completed..
        /// </summary>
        internal static string CmdSendingNotCompleted {
            get {
                return ResourceManager.GetString("CmdSendingNotCompleted", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Communication with the remote host is lost..
        /// </summary>
        internal static string ConnectionLost {
            get {
                return ResourceManager.GetString("ConnectionLost", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The connection was not completed within the specified time period. Timeout: &quot;{0}&quot;..
        /// </summary>
        internal static string ConnectionTimeout {
            get {
                return ResourceManager.GetString("ConnectionTimeout", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The data was not received within the specified time period. Timeout: &quot;{0}&quot;..
        /// </summary>
        internal static string DataReceivingTimeout {
            get {
                return ResourceManager.GetString("DataReceivingTimeout", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The data was not sent within the specified time period. Timeout: &quot;{0}&quot;..
        /// </summary>
        internal static string DataSendingTimeout {
            get {
                return ResourceManager.GetString("DataSendingTimeout", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The logout command was not executed..
        /// </summary>
        internal static string LogoutCmdFailed {
            get {
                return ResourceManager.GetString("LogoutCmdFailed", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The logout was not performed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
        /// </summary>
        internal static string LogoutFailed {
            get {
                return ResourceManager.GetString("LogoutFailed", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The value was not received. Expected type: &quot;{0}&quot;, field name: &quot;{1}&quot;, API response value: &quot;{2}&quot;..
        /// </summary>
        internal static string ModelValueNotReceived {
            get {
                return ResourceManager.GetString("ModelValueNotReceived", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Getting the sequence was not completed. API response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
        /// </summary>
        internal static string RecvSeqNotComplete {
            get {
                return ResourceManager.GetString("RecvSeqNotComplete", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Getting the sequence was not completed - unknown type of API response. Response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
        /// </summary>
        internal static string RecvSeqNotCompleteUnknownRespType {
            get {
                return ResourceManager.GetString("RecvSeqNotCompleteUnknownRespType", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The response text is empty.
        /// </summary>
        internal static string ResponseIsEmpty {
            get {
                return ResourceManager.GetString("ResponseIsEmpty", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The API response was not received..
        /// </summary>
        internal static string ResponseNotReceived {
            get {
                return ResourceManager.GetString("ResponseNotReceived", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The API response stream was not cleared..
        /// </summary>
        internal static string ResponseStreamNotCleared {
            get {
                return ResourceManager.GetString("ResponseStreamNotCleared", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The API response type was not received. Response text: &quot;{0}&quot;..
        /// </summary>
        internal static string ResponseTypeNotReceived {
            get {
                return ResourceManager.GetString("ResponseTypeNotReceived", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The API response word value was not received..
        /// </summary>
        internal static string ResponseWordNotReceived {
            get {
                return ResourceManager.GetString("ResponseWordNotReceived", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The sending of the command data was not completed..
        /// </summary>
        internal static string SendingCmdDataNotCompleted {
            get {
                return ResourceManager.GetString("SendingCmdDataNotCompleted", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The name of the sentence type was not received..
        /// </summary>
        internal static string SentenceNameNotReceived {
            get {
                return ResourceManager.GetString("SentenceNameNotReceived", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на Unknown API response type. Response type: &quot;{0}&quot;. Response text: &quot;{1}&quot;..
        /// </summary>
        internal static string UnknownResponseType {
            get {
                return ResourceManager.GetString("UnknownResponseType", resourceCulture);
            }
        }
        
        /// <summary>
        ///   Ищет локализованную строку, похожую на The API word length value was not received..
        /// </summary>
        internal static string WordLengthValueNotReceived {
            get {
                return ResourceManager.GetString("WordLengthValueNotReceived", resourceCulture);
            }
        }
    }
}


File: /MikroTikMiniApi\Resources\Strings.resx
﻿<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="AuthCmdFailed" xml:space="preserve">
    <value>The authentication command was not executed.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="AuthFailed" xml:space="preserve">
    <value>Authentication was not performed. API response type: "{0}". Response text: "{1}".</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="AuthFailedIncorrectAnswer" xml:space="preserve">
    <value>Authentication was not performed. The API response "{0}" was expected to be empty.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="CmdSendingNotCompleted" xml:space="preserve">
    <value>The command sending was not completed.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ConnectionLost" xml:space="preserve">
    <value>Communication with the remote host is lost.</value>
    <comment>Connection</comment>
  </data>
  <data name="ConnectionTimeout" xml:space="preserve">
    <value>The connection was not completed within the specified time period. Timeout: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="DataReceivingTimeout" xml:space="preserve">
    <value>The data was not received within the specified time period. Timeout: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="DataSendingTimeout" xml:space="preserve">
    <value>The data was not sent within the specified time period. Timeout: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="LogoutCmdFailed" xml:space="preserve">
    <value>The logout command was not executed.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="LogoutFailed" xml:space="preserve">
    <value>The logout was not performed. API response type: "{0}". Response text: "{1}".</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="ModelValueNotReceived" xml:space="preserve">
    <value>The value was not received. Expected type: "{0}", field name: "{1}", API response value: "{2}".</value>
    <comment>ModelBase</comment>
  </data>
  <data name="RecvSeqNotComplete" xml:space="preserve">
    <value>Getting the sequence was not completed. API response type: "{0}". Response text: "{1}".</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="RecvSeqNotCompleteUnknownRespType" xml:space="preserve">
    <value>Getting the sequence was not completed - unknown type of API response. Response type: "{0}". Response text: "{1}".</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseIsEmpty" xml:space="preserve">
    <value>The response text is empty</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="ResponseNotReceived" xml:space="preserve">
    <value>The API response was not received.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseStreamNotCleared" xml:space="preserve">
    <value>The API response stream was not cleared.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseTypeNotReceived" xml:space="preserve">
    <value>The API response type was not received. Response text: "{0}".</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="ResponseWordNotReceived" xml:space="preserve">
    <value>The API response word value was not received.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="SendingCmdDataNotCompleted" xml:space="preserve">
    <value>The sending of the command data was not completed.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="SentenceNameNotReceived" xml:space="preserve">
    <value>The name of the sentence type was not received.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="UnknownResponseType" xml:space="preserve">
    <value>Unknown API response type. Response type: "{0}". Response text: "{1}".</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="WordLengthValueNotReceived" xml:space="preserve">
    <value>The API word length value was not received.</value>
    <comment>CommandExecutionService</comment>
  </data>
</root>

File: /MikroTikMiniApi\Resources\Strings.ru-RU.resx
﻿<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="AuthCmdFailed" xml:space="preserve">
    <value>Команда аутентификации не была выполнена.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="AuthFailed" xml:space="preserve">
    <value>Аутентификация не была произведена. Тип ответа API: "{0}". Текст ответа: "{1}".</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="AuthFailedIncorrectAnswer" xml:space="preserve">
    <value>Аутентификация не была произведена. Ответ API "{0}" ожидался пустым.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="CmdSendingNotCompleted" xml:space="preserve">
    <value>Передача команды не была завершена.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ConnectionLost" xml:space="preserve">
    <value>Потеряна связь с удаленным хостом.</value>
    <comment>Connection</comment>
  </data>
  <data name="ConnectionTimeout" xml:space="preserve">
    <value>Подключение не было выполнено за установленный период времени. Таймаут: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="DataReceivingTimeout" xml:space="preserve">
    <value>Получение данных не было выполнено за установленный период времени. Таймаут: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="DataSendingTimeout" xml:space="preserve">
    <value>Отправка данных не была выполнена за установленный период времени. Таймаут: "{0}".</value>
    <comment>Connection</comment>
  </data>
  <data name="LogoutCmdFailed" xml:space="preserve">
    <value>Команда выхода не была выполнена.</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="LogoutFailed" xml:space="preserve">
    <value>Выход из системы не был произведен. Тип ответа API: "{0}". Текст ответа: "{1}".</value>
    <comment>AuthenticationLocalizationService</comment>
  </data>
  <data name="ModelValueNotReceived" xml:space="preserve">
    <value>Значение не было получено. Ожидаемый тип: "{0}", наименование поля: "{1}", значение ответа API: "{2}".</value>
    <comment>ModelBase</comment>
  </data>
  <data name="RecvSeqNotComplete" xml:space="preserve">
    <value>Получение последовательности не было завершено. Тип ответа API: "{0}". Текст ответа: "{1}".</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="RecvSeqNotCompleteUnknownRespType" xml:space="preserve">
    <value>Получение последовательности не было завершено - неизвестный тип ответа API. Тип ответа: "{0}". Текст ответа: "{1}".</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseIsEmpty" xml:space="preserve">
    <value>Текст ответа не задан</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="ResponseNotReceived" xml:space="preserve">
    <value>Ответ API не был получен.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseStreamNotCleared" xml:space="preserve">
    <value>Очистка потока ответов API не была произведена.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="ResponseTypeNotReceived" xml:space="preserve">
    <value>Тип ответа API не был получен. Текст ответа: "{0}".</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="ResponseWordNotReceived" xml:space="preserve">
    <value>Значение слова ответа API не было получено.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="SendingCmdDataNotCompleted" xml:space="preserve">
    <value>Передача данных команды не была завершена.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="SentenceNameNotReceived" xml:space="preserve">
    <value>Наименование типа предложения не было получено.</value>
    <comment>CommandExecutionService</comment>
  </data>
  <data name="UnknownResponseType" xml:space="preserve">
    <value>Неизвестный тип ответа API. Тип ответа: "{0}". Текст ответа: "{1}".</value>
    <comment>ApiSentenceFactory</comment>
  </data>
  <data name="WordLengthValueNotReceived" xml:space="preserve">
    <value>Значение длины слова API не было получено.</value>
    <comment>CommandExecutionService</comment>
  </data>
</root>

File: /MikroTikMiniApi\Sentences\ApiDoneSentence.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;

namespace MikroTikMiniApi.Sentences
{
    /// <summary>
    /// API sentence of the "Done" type.
    /// </summary>
    internal class ApiDoneSentence : ApiSentenceBase, IApiDoneSentence
    {
        internal ApiDoneSentence(IReadOnlyList<string> words, IApiSentenceLocalizationService localizationService)
            : base(words, localizationService)
        {
        }
    }
}

File: /MikroTikMiniApi\Sentences\ApiFatalSentence.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;

namespace MikroTikMiniApi.Sentences
{
    /// <summary>
    /// API sentence of the "Fatal" type.
    /// </summary>
    internal class ApiFatalSentence : ApiSentenceBase, IApiFatalSentence
    {
        public ApiFatalSentence(IReadOnlyList<string> words, IApiSentenceLocalizationService localizationService)
            : base(words, localizationService)
        {
        }
    }
}

File: /MikroTikMiniApi\Sentences\ApiReSentence.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;

namespace MikroTikMiniApi.Sentences
{
    /// <summary>
    /// API sentence of the "Re" type.
    /// </summary>
    internal class ApiReSentence : ApiSentenceBase, IApiReSentence
    {
        public ApiReSentence(IReadOnlyList<string> words, IApiSentenceLocalizationService localizationService)
            : base(words, localizationService)
        {
        }
    }
}

File: /MikroTikMiniApi\Sentences\ApiSentenceBase.cs
﻿using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Sentences
{
    using ILocalizationService = IApiSentenceLocalizationService;

    ///<inheritdoc cref="IApiSentence"/>
    internal abstract class ApiSentenceBase : IApiSentence, IEquatable<ApiSentenceBase>
    {
        private readonly int _wordsHashCode;
        private readonly int _typeHashCode;
        private readonly IReadOnlyDictionary<string, string> _wordsValues;
        private readonly ILocalizationService _localizationService;

        ///<inheritdoc/>
        public IReadOnlyList<string> Words { get; }

        protected ApiSentenceBase(IReadOnlyList<string> words, ILocalizationService localizationService)
        {
            Guard.ThrowIfNull(words, nameof(words));
            Guard.ThrowIfNull(localizationService, out _localizationService, nameof(localizationService));

            _wordsValues = GetWordsValues(words, out _wordsHashCode);
            _typeHashCode = GetType().GetHashCode();

            Words = words;
        }

        private static IReadOnlyDictionary<string, string> GetWordsValues(IEnumerable<string> words, out int wordsHashCode)
        {
            var wordsValues = new Dictionary<string, string>();
            var regex = new Regex("^=?(?<KEY>[^=]+)=(?<VALUE>.+)$", RegexOptions.Singleline);

            wordsHashCode = 0;

            foreach (var word in words)
            {
                wordsHashCode ^= word.GetHashCode();

                var match = regex.Match(word);

                if (!match.Success)
                    continue;

                var key = match.Groups["KEY"].Value;
                var value = match.Groups["VALUE"].Value;

                wordsValues.Add(key, value);
            }

            return wordsValues;
        }

        internal static string GetTextInternal(IReadOnlyCollection<string> words, ILocalizationService localizationService)
        {
            if (words.Count == 0)
                return localizationService.GetResponseIsEmptyText();

            var sb = new StringBuilder();

            foreach (var word in words)
                sb.Append(word);

            return sb.ToString();
        }

        ///<inheritdoc/>
        public bool TryGetWordValue(string word, out string value)
        {
            Guard.ThrowIfNull(word, nameof(word));

            return _wordsValues.TryGetValue(word, out value!);
        }

        ///<inheritdoc/>
        public string GetText()
        {
            return GetTextInternal(Words, _localizationService);
        }

        public bool Equals(ApiSentenceBase? other)
        {
            return Equals((object?)other);
        }

        public override bool Equals(object? obj)
        {
            if (obj is not ApiSentenceBase other)
                return false;

            if (ReferenceEquals(this, other))
                return true;

            if (GetType() != other.GetType())
                return false;

            if (Words.Count != other.Words.Count)
                return false;

            for (var i = 0; i < Words.Count; i++)
            {
                if (!Words[i].Equals(other.Words[i], StringComparison.OrdinalIgnoreCase))
                    return false;
            }

            return true;
        }

        public override int GetHashCode()
        {
            return _wordsHashCode ^ _typeHashCode;
        }
    }
}

File: /MikroTikMiniApi\Sentences\ApiTrapSentence.cs
﻿using System.Collections.Generic;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;

namespace MikroTikMiniApi.Sentences
{
    /// <summary>
    /// API sentence of the "Trap" type.
    /// </summary>
    internal class ApiTrapSentence : ApiSentenceBase, IApiTrapSentence
    {
        public ApiTrapSentence(IReadOnlyList<string> words, IApiSentenceLocalizationService localizationService)
            : base(words, localizationService)
        {
        }
    }
}

File: /MikroTikMiniApi\Services\AuthenticationService.cs
﻿using System;
using System.Globalization;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using MikroTikMiniApi.Commands;
using MikroTikMiniApi.Exceptions;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Sentences;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Services
{
    using ILocalizationService = IAuthenticationLocalizationService;

    ///<inheritdoc cref="IAuthenticationService"/>
    internal class AuthenticationService : IAuthenticationService
    {
        private readonly ICommandExecutionService _commandExecutionService;
        private readonly ILocalizationService _localization;

        public AuthenticationService(ICommandExecutionService commandExecutionService, ILocalizationService localizationService)
        {
            Guard.ThrowIfNull(commandExecutionService, out _commandExecutionService, nameof(commandExecutionService));
            Guard.ThrowIfNull(localizationService, out _localization, nameof(localizationService));
        }

        private static string EncodePassword(string password, string hash)
        {
            var hashByteArray = new byte[hash.Length / 2];
            var hashSpan = hash.AsSpan();

            for (var i = 0; i <= hash.Length - 2; i += 2)
            {
                hashByteArray[i / 2] = byte.Parse(hashSpan.Slice(i, 2), NumberStyles.HexNumber, CultureInfo.InvariantCulture);
            }

            var passwordByteArray = Encoding.ASCII.GetBytes(password);
            var buffer = new byte[passwordByteArray.Length + hashByteArray.Length + 1];

            buffer[0] = 0;

            Array.Copy(passwordByteArray, 0, buffer, 1, passwordByteArray.Length);
            Array.Copy(hashByteArray, 0, buffer, passwordByteArray.Length + 1, hashByteArray.Length);

            byte[] hashed;

            using (var md5 = MD5.Create())
            {
                hashed = md5.ComputeHash(buffer);
            }

            var builder = new StringBuilder("00");

            foreach (var b in hashed)
            {
                builder.AppendFormat("{0:x2}", b);
            }

            return builder.ToString();
        }

        private async Task<IApiSentence> ExecuteCommandAsync(IApiCommand command, string errorMessage)
        {
            try
            {
                return await _commandExecutionService.ExecuteCommandAsync(command).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(errorMessage, ex);
            }
        }

        ///<inheritdoc/>
        public async Task AuthenticationAsync(string name, string password)
        {
            Guard.ThrowIfEmptyString(name, nameof(name));
            Guard.ThrowIfEmptyString(password, nameof(password));

            var errorMessage = _localization.GetAuthCmdFailedText();
            var authCommand = ApiCommand.New("/login")
                                        .AddParameter("name", name)
                                        .AddParameter("password", password)
                                        .Build();

            var sentence = await ExecuteCommandAsync(authCommand, errorMessage).ConfigureAwait(false);

            ThrowIfSentenceIsNotDone(sentence, _localization);

            if (!sentence.TryGetWordValue("ret", out var retValue))
            {
                ThrowIfSentenceIsNotEmpty(sentence, _localization);

                return;
            }

            var hashedPassword = EncodePassword(password, retValue);
            var oldAuthCommand = ApiCommand.New("/login")
                                           .AddParameter("name", name)
                                           .AddParameter("response", hashedPassword)
                                           .Build();

            sentence = await ExecuteCommandAsync(oldAuthCommand, errorMessage).ConfigureAwait(false);
            
            ThrowIfSentenceIsNotDone(sentence, _localization);
            ThrowIfSentenceIsNotEmpty(sentence, _localization);

            static void ThrowIfSentenceIsNotDone(IApiSentence sentence, ILocalizationService localization)
            {
                if (sentence is not ApiDoneSentence)
                    throw new AuthenticationFaultException(localization.GetAuthFailedText(sentence, sentence.GetText()));
            }

            static void ThrowIfSentenceIsNotEmpty(IApiSentence sentence, ILocalizationService localization)
            {
                if (sentence.Words.Count != 0)
                    throw new InvalidOperationException(localization.GetAuthFailedIncorrectAnswerText(sentence));
            }
        }

        ///<inheritdoc/>
        public async Task QuitAsync()
        {
            var command = ApiCommand.New("/quit").Build();
            var sentence = await ExecuteCommandAsync(command, _localization.GetLogoutCmdFailedText()).ConfigureAwait(false);

            if (!(sentence is ApiFatalSentence &&
                  sentence.Words.Count == 1 &&
                  sentence.Words[0].Equals("session terminated on request", StringComparison.OrdinalIgnoreCase)))
            {
                throw new AuthenticationFaultException(_localization.GetLogoutFailedText(sentence, sentence.GetText()));
            }
        }
    }
}

File: /MikroTikMiniApi\Services\CommandExecutionService.cs
﻿using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using MikroTikMiniApi.Exceptions;
using MikroTikMiniApi.Interfaces.Commands;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Models.Settings;
using MikroTikMiniApi.Interfaces.Networking;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Parameters;
using MikroTikMiniApi.Sentences;
using MikroTikMiniApi.Utilities;

namespace MikroTikMiniApi.Services
{
    using ILocalizationService = ICommandExecutionLocalizationService;
    using static Models.Settings.ExecutionSettings;

    ///<inheritdoc cref="ICommandExecutionService"/>
    internal class CommandExecutionService : ICommandExecutionService
    {
        private readonly IConnection _connection;
        private readonly ILocalizationService _localization;
        private readonly IApiSentenceFactory _sentenceFactory;

        public CommandExecutionService(IConnection connection, ILocalizationService localizationService, IApiSentenceFactory sentenceFactory)
        {
            Guard.ThrowIfNull(connection, out _connection, nameof(connection));
            Guard.ThrowIfNull(localizationService, out _localization, nameof(localizationService));
            Guard.ThrowIfNull(sentenceFactory, out _sentenceFactory, nameof(sentenceFactory));
        }

        private static byte[] EncodeWordLength(in long length)
        {
            byte[] array;

            switch (length)
            {
                case < 0x80:
                    array = BitConverter.GetBytes(length);
                    return new[] { array[0] };
                case < 0x4000:
                    array = BitConverter.GetBytes(length | 0x8000);
                    return new[] { array[1], array[0] };
                case < 0x200_000:
                    array = BitConverter.GetBytes(length | 0xC00000);
                    return new[] { array[2], array[1], array[0] };
                case < 0x100_000_000:
                    array = BitConverter.GetBytes(length | 0xE0000000);
                    return new[] { array[3], array[2], array[1], array[0] };
                default:
                    array = BitConverter.GetBytes(length);
                    return new byte[] { 0xF0, array[3], array[2], array[1], array[0] };
            }
        }

        private static async ValueTask<long> ReadWordLengthAsync(IConnection connection)
        {
            var buffer = new Memory<byte>(new byte[5]);

            await connection.ReceiveAsync(buffer.Slice(0, 1)).ConfigureAwait(false);

            if ((buffer.Span[0] & 0x80) == 0x00)
            {
                return buffer.Span[0];
            }

            if ((buffer.Span[0] & 0xC0) == 0x80)
            {
                await connection.ReceiveAsync(buffer.Slice(1, 1)).ConfigureAwait(false);

                return ((buffer.Span[0] & 0x3F) << 8) + buffer.Span[1];
            }

            long length;

            if ((buffer.Span[0] & 0xE0) == 0xC0)
            {
                await connection.ReceiveAsync(buffer.Slice(1, 2)).ConfigureAwait(false);

                length = ((buffer.Span[0] & 0x1F) << 8) + buffer.Span[1];
                length = (length << 8) + buffer.Span[2];
            }
            else
            {
                if ((buffer.Span[0] & 0xF0) == 0xE0)
                {
                    await connection.ReceiveAsync(buffer.Slice(1, 3)).ConfigureAwait(false);

                    length = ((buffer.Span[0] & 0xF) << 8) + buffer.Span[1];
                    length = (length << 8) + buffer.Span[2];
                    length = (length << 8) + buffer.Span[3];
                }
                else
                {
                    await connection.ReceiveAsync(buffer.Slice(1, 4)).ConfigureAwait(false);

                    length = buffer.Span[1];
                    length = (length << 8) + buffer.Span[2];
                    length = (length << 8) + buffer.Span[3];
                    length = (length << 8) + buffer.Span[4];
                }
            }

            return length;
        }

        private static async ValueTask<string> ReadWordAsync(IConnection connection, ILocalizationService localization)
        {
            long wordLength;

            try
            {
                wordLength = await ReadWordLengthAsync(connection).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(localization.GetWordLengthValueNotReceivedText(), ex);
            }

            if (wordLength <= 0)
                return string.Empty;

            var buffer = new Memory<byte>(new byte[wordLength]);

            await connection.ReceiveAsync(buffer).ConfigureAwait(false);

            return Encoding.ASCII.GetString(buffer.Span);
        }

        ///<inheritdoc/>
        async ValueTask<IReadOnlyList<IApiSentence>> ICommandExecutionService.FlushResponseStreamAsync(IExecutionSettings settings)
        {
            var list = new List<IApiSentence>();

            Guard.ThrowIfNull(settings, nameof(settings));

            if (!settings.IsFlushResponseStream)
                return list;

            for (var i = 0; i < settings.AttemptsCount;)
            {
                try
                {
                    var sentence = await ((ICommandExecutionService)this).ReceiveSentenceAsync().ConfigureAwait(false);

                    list.Add(sentence);

                    if (settings.FlushBeforeDoneSentence)
                    {
                        if (sentence is ApiDoneSentence)
                            break;
                    }
                    else
                    {
                        i++;
                    }
                }
                catch (Exception ex)
                {
                    throw new CommandExecutionFaultException(_localization.GetResponseNotReceivedText(), ex);
                }
            }

            return list;
        }

        ///<inheritdoc/>
        async ValueTask ICommandExecutionService.SendCommandAsync(IApiCommand command)
        {
            Guard.ThrowIfNull(command, nameof(command));

            byte[] buffer;
            var commandArray = GetWordByteArray(command.Text);
            
            if (command.Parameters.Count != 0)
            {
                var beginIdx = commandArray.Length;
                var parameterArrays = GetParameterByteArrays(command.Parameters, out var totalLength);

                buffer = new byte[commandArray.Length + totalLength + 1];

                Array.Copy(commandArray, buffer, commandArray.Length);

                foreach (var parameterArray in parameterArrays)
                {
                    Array.Copy(parameterArray, 0, buffer, beginIdx, parameterArray.Length);

                    beginIdx += parameterArray.Length;
                }
            }
            else
            {
                buffer = new byte[commandArray.Length + 1];

                Array.Copy(commandArray, buffer, commandArray.Length);
            }

            buffer[^1] = 0;

            var memory = new ReadOnlyMemory<byte>(buffer);

            try
            {
                await _connection.SendAsync(memory).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(_localization.GetSendingCmdDataNotCompletedText(), ex);
            }

            static IEnumerable<byte[]> GetParameterByteArrays(IReadOnlyList<ApiCommandParameter> parameters, out int totalBytesLength)
            {
                var byteArrays = new byte[parameters.Count][];

                totalBytesLength = 0;

                for (var i = 0; i < parameters.Count; i++)
                {
                    var byteArray = GetWordByteArray(parameters[i]);

                    byteArrays[i] = byteArray;
                    totalBytesLength += byteArray.Length;
                }

                return byteArrays;
            }

            static byte[] GetWordByteArray(string word)
            {
                var wordArray = Encoding.ASCII.GetBytes(word);
                var lengthArray = EncodeWordLength(wordArray.Length);
                var buffer = new byte[lengthArray.Length + wordArray.Length];

                Array.Copy(lengthArray, buffer, lengthArray.Length);
                Array.Copy(wordArray, 0, buffer, lengthArray.Length, wordArray.Length);

                return buffer;
            }
        }

        ///<inheritdoc/>
        async ValueTask<IApiSentence> ICommandExecutionService.ReceiveSentenceAsync()
        {
            var words = new List<string>();
            string sentenceName;

            try
            {
                sentenceName = await ReadWordAsync(_connection, _localization).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(_localization.GetSentenceNameNotReceivedText(), ex);
            }

            while (true)
            {
                string word;

                try
                {
                    word = await ReadWordAsync(_connection, _localization).ConfigureAwait(false);
                }
                catch (Exception ex)
                {
                    throw new CommandExecutionFaultException(_localization.GetResponseWordNotReceivedText(), ex);
                }

                if (string.IsNullOrWhiteSpace(word))
                    break;

                words.Add(word);
            }

            return _sentenceFactory.Create(sentenceName, words);
        }

        ///<inheritdoc/>
        public async Task<IApiSentence> ExecuteCommandAsync(IApiCommand command, IExecutionSettings? settings)
        {
            try
            {
                await ((ICommandExecutionService)this).SendCommandAsync(command).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(_localization.GetCmdSendingNotCompletedText(), ex);
            }

            IApiSentence sentence;

            try
            {
                sentence = await ((ICommandExecutionService)this).ReceiveSentenceAsync().ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(_localization.GetResponseNotReceivedText(), ex);
            }

            try
            {
                if (sentence is ApiTrapSentence)
                    await ((ICommandExecutionService)this).FlushResponseStreamAsync(GetValueOrDefault(settings)).ConfigureAwait(false);
            }
            catch (Exception ex)
            {
                throw new CommandExecutionFaultException(_localization.GetResponseStreamNotClearedText(), ex);
            }

            return sentence;
        }

        ///<inheritdoc/>
        public IAsyncEnumerable<IApiSentence> ExecuteCommandToEnumerableAsync(IApiCommand command, IExecutionSettings? settings)
        {
            return new SentenceEnumerableNonGeneric(command, this, _localization, GetValueOrDefault(settings));
        }

        ///<inheritdoc/>
        public async Task<IReadOnlyList<IApiSentence>> ExecuteCommandToListAsync(IApiCommand command, IExecutionSettings? settings)
        {
            var list = new List<IApiSentence>();
            var enumerable = new SentenceEnumerableNonGeneric(command, this, _localization, GetValueOrDefault(settings));

            await foreach (var sentence in enumerable.ConfigureAwait(false))
            {
                list.Add(sentence);
            }

            return list;
        }

        ///<inheritdoc/>
        public IAsyncEnumerable<T> ExecuteCommandToEnumerableAsync<T>(IApiCommand command, IExecutionSettings? settings)
            where T : class, IModelFactory<T>, new()
        {
            return new SentenceEnumerableGeneric<T>(command, this, _localization, new T(), GetValueOrDefault(settings));
        }

        ///<inheritdoc/>
        public async Task<IReadOnlyList<T>> ExecuteCommandToListAsync<T>(IApiCommand command, IExecutionSettings? settings)
            where T : class, IModelFactory<T>, new()
        {
            var list = new List<T>();
            var enumerable = new SentenceEnumerableGeneric<T>(command, this, _localization, new T(), GetValueOrDefault(settings));

            await foreach (var sentence in enumerable.ConfigureAwait(false))
            {
                list.Add(sentence);
            }

            return list;
        }

        #region Nested types

        private abstract class SentenceEnumerableBase<T> : IAsyncEnumerable<T>
        {
            private readonly IApiCommand _command;
            private readonly ICommandExecutionService _commandExecutionService;
            private readonly IExecutionSettings _settings;
            protected readonly ILocalizationService Localization;

            protected SentenceEnumerableBase(IApiCommand command,
                                             ICommandExecutionService commandExecutionService,
                                             ILocalizationService localizationService,
                                             IExecutionSettings settings)
            {
                Guard.ThrowIfNull(command, out _command, nameof(command));
                Guard.ThrowIfNull(localizationService, out Localization, nameof(localizationService));
                Guard.ThrowIfNull(commandExecutionService, out _commandExecutionService, nameof(commandExecutionService));

                _settings = settings;
            }

            protected static void ThrowIfUnknownSentence(IApiSentence sentence, ILocalizationService localization)
            {
                throw new CommandExecutionFaultException(localization.GetRecvSeqNotCompleteUnknownRespTypeText(sentence, sentence.GetText()));
            }

            protected async ValueTask SendCommandAsync()
            {
                try
                {
                    await _commandExecutionService.SendCommandAsync(_command).ConfigureAwait(false);
                }
                catch (Exception ex)
                {
                    throw new CommandExecutionFaultException(Localization.GetCmdSendingNotCompletedText(), ex);
                }
            }

            [MethodImpl(MethodImplOptions.AggressiveInlining)]
            protected async ValueTask<IApiSentence> ReceiveSentenceAsync()
            {
                try
                {
                    return await _commandExecutionService.ReceiveSentenceAsync().ConfigureAwait(false);
                }
                catch (Exception ex)
                {
                    throw new CommandExecutionFaultException(Localization.GetResponseNotReceivedText(), ex);
                }
            }

            protected ValueTask<IReadOnlyList<IApiSentence>> FlushResponseStreamAsync()
            {
                return _commandExecutionService.FlushResponseStreamAsync(_settings);
            }

            public abstract IAsyncEnumerator<T> GetAsyncEnumerator(CancellationToken cancellationToken = new());
        }

        private class SentenceEnumerableGeneric<T> : SentenceEnumerableBase<T>
            where T : class
        {
            private readonly IModelFactory<T> _modelFactory;

            public SentenceEnumerableGeneric(IApiCommand command,
                                             ICommandExecutionService commandExecutionService,
                                             ILocalizationService localizationService,
                                             IModelFactory<T> modelFactory,
                                             IExecutionSettings settings)
                : base(command, commandExecutionService, localizationService, settings)
            {
                Guard.ThrowIfNull(modelFactory, out _modelFactory, nameof(modelFactory));
            }

            private static Exception GetException(IApiSentence sentence, ILocalizationService localization)
            {
                return new CommandExecutionFaultException(localization.GetRecvSeqNotCompleteText(sentence, sentence.GetText()));
            }

            public override async IAsyncEnumerator<T> GetAsyncEnumerator(CancellationToken cancellationToken = default)
            {
                await SendCommandAsync().ConfigureAwait(false);

                while (true)
                {
                    var sentence = await ReceiveSentenceAsync().ConfigureAwait(false);

                    switch (sentence)
                    {
                        case ApiDoneSentence:
                            yield break;
                        case ApiReSentence:
                            yield return _modelFactory.Create(sentence);
                            break;
                        case ApiFatalSentence:
                            throw GetException(sentence, Localization);
                        case ApiTrapSentence:
                            {
                                var exceptions = new List<Exception>();

                                try
                                {
                                    await FlushResponseStreamAsync().ConfigureAwait(false);
                                }
                                catch (Exception ex)
                                {
                                    exceptions.Add(ex);
                                }

                                exceptions.Add(GetException(sentence, Localization));

                                if (exceptions.Count == 2)
                                    throw new AggregateException(exceptions);

                                throw exceptions[0];
                            }
                        default:
                            ThrowIfUnknownSentence(sentence, Localization);
                            break;
                    }
                }
            }
        }

        private class SentenceEnumerableNonGeneric : SentenceEnumerableBase<IApiSentence>
        {
            public SentenceEnumerableNonGeneric(IApiCommand command,
                                                ICommandExecutionService commandExecutionService,
                                                ILocalizationService localizationService,
                                                IExecutionSettings settings)
                : base(command, commandExecutionService, localizationService, settings)
            {
            }

            public override async IAsyncEnumerator<IApiSentence> GetAsyncEnumerator(CancellationToken cancellationToken = default)
            {
                await SendCommandAsync().ConfigureAwait(false);

                while (true)
                {
                    var sentence = await ReceiveSentenceAsync().ConfigureAwait(false);

                    switch (sentence)
                    {
                        case ApiDoneSentence or ApiFatalSentence:
                            yield return sentence;
                            yield break;
                        case ApiReSentence:
                            yield return sentence;
                            break;
                        case ApiTrapSentence:
                            {
                                Exception exception = null!;
                                IReadOnlyList<IApiSentence> sentences = null!;

                                yield return sentence;

                                try
                                {
                                    sentences = await FlushResponseStreamAsync().ConfigureAwait(false);
                                }
                                catch (Exception ex)
                                {
                                    exception = ex;
                                }

                                if (sentences != null!)
                                {
                                    foreach (var item in sentences)
                                        yield return item;
                                }

                                if (exception == null!)
                                    yield break;

                                throw exception;
                            }
                        default:
                            ThrowIfUnknownSentence(sentence, Localization);
                            break;
                    }
                }
            }
        }

        #endregion
    }
}

File: /MikroTikMiniApi\Services\LocalizationService.cs
﻿using System;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Interfaces.Services;
using MikroTikMiniApi.Resources;

namespace MikroTikMiniApi.Services
{
    internal class LocalizationService : ILocalizationService
    {
        private static string GetTypeName(IApiSentence sentence) => sentence.GetType().Name;

        #region IAuthenticationLocalizationService

        public string GetAuthCmdFailedText()
        {
            return Strings.AuthCmdFailed;
        }

        public string GetAuthFailedText(IApiSentence sentence, string response)
        {
            return string.Format(Strings.AuthFailed, GetTypeName(sentence), response);
        }

        public string GetAuthFailedIncorrectAnswerText(IApiSentence sentence)
        {
            return string.Format(Strings.AuthFailedIncorrectAnswer, GetTypeName(sentence));
        }

        public string GetLogoutCmdFailedText()
        {
            return Strings.LogoutCmdFailed;
        }

        public string GetLogoutFailedText(IApiSentence sentence, string response)
        {
            return string.Format(Strings.LogoutFailed, GetTypeName(sentence), response);
        }

        #endregion

        #region ICommandExecutionLocalizationService

        public string GetCmdSendingNotCompletedText()
        {
            return Strings.CmdSendingNotCompleted;
        }

        public string GetSendingCmdDataNotCompletedText()
        {
            return Strings.SendingCmdDataNotCompleted;
        }

        public string GetResponseNotReceivedText()
        {
            return Strings.ResponseNotReceived;
        }

        public string GetResponseStreamNotClearedText()
        {
            return Strings.ResponseStreamNotCleared;
        }

        public string GetResponseWordNotReceivedText()
        {
            return Strings.ResponseWordNotReceived;
        }

        public string GetSentenceNameNotReceivedText()
        {
            return Strings.SentenceNameNotReceived;
        }

        public string GetWordLengthValueNotReceivedText()
        {
            return Strings.WordLengthValueNotReceived;
        }

        public string GetRecvSeqNotCompleteUnknownRespTypeText(IApiSentence sentence, string response)
        {
            return string.Format(Strings.RecvSeqNotCompleteUnknownRespType, sentence, response);
        }

        public string GetRecvSeqNotCompleteText(IApiSentence sentence, string response)
        {
            return string.Format(Strings.RecvSeqNotComplete, GetTypeName(sentence), response);
        }

        #endregion

        #region IConnectionLocalizationService

        public string GetConnectionTimeoutText(TimeSpan timeout)
        {
            return string.Format(Strings.ConnectionTimeout, timeout);
        }

        public string GetDataSendingTimeoutText(TimeSpan timeout)
        {
            return string.Format(Strings.DataSendingTimeout, timeout);
        }

        public string GetDataReceivingTimeoutText(TimeSpan timeout)
        {
            return string.Format(Strings.DataReceivingTimeout, timeout);
        }

        public string GetConnectionLostText()
        {
            return string.Format(Strings.ConnectionLost);
        }

        #endregion

        #region IApiSentenceLocalizationService

        public string GetResponseTypeNotReceivedText(string response)
        {
            return string.Format(Strings.ResponseTypeNotReceived, response);
        }

        public string GetUnknownResponseTypeText(string sentenceName, string responce)
        {
            return string.Format(Strings.UnknownResponseType, sentenceName, responce);
        }

        public string GetResponseIsEmptyText()
        {
            return Strings.ResponseIsEmpty;
        }

        #endregion
    }
}

File: /MikroTikMiniApi\Utilities\Guard.cs
﻿using System;
using System.Runtime.CompilerServices;

namespace MikroTikMiniApi.Utilities
{
    internal static class Guard
    {
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public static void ThrowIfNull<T>(T source, out T target, string paramName) where T : class
        {
            target = source ?? throw new ArgumentNullException(paramName);
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public static void ThrowIfNull<T>(T source, string paramName) where T : class
        {
            if (source == null)
                throw new ArgumentNullException(paramName);
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public static T ThrowIfNullRet<T>(T source, string paramName) where T : class
        {
            if (source == null)
                throw new ArgumentNullException(paramName);

            return source;
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public static void ThrowIfEmptyString(string source, string paramName)
        {
            if (string.IsNullOrWhiteSpace(source))
                throw new ArgumentException(paramName);
        }

        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        public static void ThrowIfEmptyString(string source, out string target, string paramName)
        {
            if (string.IsNullOrWhiteSpace(source))
                throw new ArgumentException(paramName);

            target = source;
        }
    }
}

File: /MikroTikMiniApi.Demo\MikroTikMiniApi.Demo.csproj
﻿<Project Sdk="Microsoft.NET.Sdk">

	<PropertyGroup>
		<OutputType>Exe</OutputType>
		<TargetFramework>net5.0</TargetFramework>
		<Platforms>x64</Platforms>
		<TreatWarningsAsErrors>true</TreatWarningsAsErrors>
		<Nullable>enable</Nullable>
	</PropertyGroup>

	<ItemGroup>
		<ProjectReference Include="..\MikroTikMiniApi\MikroTikMiniApi.csproj" />
	</ItemGroup>

</Project>

File: /MikroTikMiniApi.Demo\Program.cs
﻿using System.Net;
using System.Threading.Tasks;
using MikroTikMiniApi.Commands;
using MikroTikMiniApi.Factories;
using MikroTikMiniApi.Models.Api;

namespace MikroTikMiniApi.Demo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var apiFactory = new MicrotikApiFactory();
            using var connection = apiFactory.CreateConnection(new IPEndPoint(IPAddress.Parse("192.168.88.1"), 8728));
            
            await connection.ConnectAsync();

            var routerApi = apiFactory.CreateRouterApi(connection);

            await routerApi.AuthenticationAsync("name", "password");

            var sentence = await routerApi.ExecuteCommandAsync(ApiCommand.New("/interface/set")
                                                                         .AddParameter("disabled", "true")
                                                                         .AddParameter(".id", "ether1")
                                                                         .Build());

            var logs = await routerApi.ExecuteCommandToListAsync(ApiCommand.New("/log/print").Build());

            var packages = await routerApi.ExecuteCommandToListAsync<Package>(ApiCommand.New("/system/package/print").Build());

            await routerApi.QuitAsync();
        }
    }
}

File: /MikroTikMiniApi.sln
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 16
VisualStudioVersion = 16.0.31624.102
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "MikroTikMiniApi", "MikroTikMiniApi\MikroTikMiniApi.csproj", "{3126EC77-182E-4845-954A-B17DC72417A9}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "MikroTikMiniApi.Tests", "MikroTikMiniApi.Tests\MikroTikMiniApi.Tests.csproj", "{86C76EAD-6216-4E17-ADBF-7A84E8C1D57E}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "MikroTikMiniApi.Demo", "MikroTikMiniApi.Demo\MikroTikMiniApi.Demo.csproj", "{D5D807AF-4EC2-4057-B1C5-A48314596620}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|x64 = Debug|x64
		Release|x64 = Release|x64
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{3126EC77-182E-4845-954A-B17DC72417A9}.Debug|x64.ActiveCfg = Debug|x64
		{3126EC77-182E-4845-954A-B17DC72417A9}.Debug|x64.Build.0 = Debug|x64
		{3126EC77-182E-4845-954A-B17DC72417A9}.Release|x64.ActiveCfg = Release|x64
		{3126EC77-182E-4845-954A-B17DC72417A9}.Release|x64.Build.0 = Release|x64
		{86C76EAD-6216-4E17-ADBF-7A84E8C1D57E}.Debug|x64.ActiveCfg = Debug|x64
		{86C76EAD-6216-4E17-ADBF-7A84E8C1D57E}.Debug|x64.Build.0 = Debug|x64
		{86C76EAD-6216-4E17-ADBF-7A84E8C1D57E}.Release|x64.ActiveCfg = Release|x64
		{86C76EAD-6216-4E17-ADBF-7A84E8C1D57E}.Release|x64.Build.0 = Release|x64
		{D5D807AF-4EC2-4057-B1C5-A48314596620}.Debug|x64.ActiveCfg = Debug|x64
		{D5D807AF-4EC2-4057-B1C5-A48314596620}.Debug|x64.Build.0 = Debug|x64
		{D5D807AF-4EC2-4057-B1C5-A48314596620}.Release|x64.ActiveCfg = Release|x64
		{D5D807AF-4EC2-4057-B1C5-A48314596620}.Release|x64.Build.0 = Release|x64
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {E264DB1B-6297-4F6D-A0DC-178C2984DFE6}
	EndGlobalSection
EndGlobal


File: /MikroTikMiniApi.Tests\Infrastructure\DataReceivingTestFaultException.cs
﻿using System;

namespace MikroTikMiniApi.Tests.Infrastructure
{
    internal class DataReceivingTestFaultException : Exception
    {
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionBase.cs
﻿using System;
using System.Threading.Tasks;
using MikroTikMiniApi.Interfaces.Networking;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal abstract class FakeConnectionBase : IConnection
    {
        protected int InvokeIndex { get; private set; }

        protected static void FillBuffer(byte[] source, Memory<byte> target)
        {
            if (source.Length != target.Length)
                throw new InvalidOperationException();

            for (var i = 0; i < source.Length; i++)
            {
                target.Span[i] = source[i];
            }
        }

        protected void NextInvoke()
        {
            InvokeIndex++;
        }

        public abstract ValueTask ReceiveAsync(Memory<byte> buffer);

        public abstract ValueTask SendAsync(ReadOnlyMemory<byte> buffer);

        public static FakeConnectionSendCommand CreateForSendCommand()
        {
            return new FakeConnectionSendCommand();
        }

        public static FakeConnectionReceiveCommand CreateForReceiveCommand()
        {
            return new FakeConnectionReceiveCommand();
        }

        public static FakeConnectionQuitAsync CreateForQuitAsync()
        {
            return new FakeConnectionQuitAsync();
        }

        public static FakeConnectionExecuteCommandToListAsync CreateForExecuteCommandToListAsync()
        {
            return new FakeConnectionExecuteCommandToListAsync();
        }

        public static FakeConnectionExecuteCommandToListAsyncFlushStream CreateForExecuteCommandToListAsyncFlushStream()
        {
            return new FakeConnectionExecuteCommandToListAsyncFlushStream();
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionExecuteCommandToListAsync.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal class FakeConnectionExecuteCommandToListAsync : FakeConnectionBase
    {
        public override ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            switch (InvokeIndex)
            {
                case 0:
                    buffer.Span[0] = SentenceConstants.ReLength;
                    break;
                case 1:
                    //!re
                    FillBuffer(SentenceConstants.ReArray, buffer);
                    break;
                case 2:
                    buffer.Span[0] = 7;
                    break;
                case 3:
                    //=.id=*0
                    FillBuffer(new byte[] { 61, 46, 105, 100, 61, 42, 48, }, buffer);
                    break;
                case 4:
                    buffer.Span[0] = 12;
                    break;
                case 5:
                    //=name=telnet
                    FillBuffer(new byte[] { 61, 110, 97, 109, 101, 61, 116, 101, 108, 110, 101, 116 }, buffer);
                    break;
                case 6:
                    buffer.Span[0] = 8;
                    break;
                case 7:
                    //=port=23
                    FillBuffer(new byte[]{ 61, 112, 111, 114, 116, 61, 50, 51 }, buffer);
                    break;
                case 8:
                    buffer.Span[0] = 9;
                    break;
                case 9:
                    //=address=
                    FillBuffer(new byte[]{ 61, 97, 100, 100, 114, 101, 115, 115, 61 }, buffer);
                    break;
                case 10:
                    buffer.Span[0] = 13;
                    break;
                case 11:
                    //=invalid=true
                    FillBuffer(new byte[]{ 61, 105, 110, 118, 97, 108, 105, 100, 61, 116, 114, 117, 101 }, buffer);
                    break;
                case 12:
                    buffer.Span[0] = 14;
                    break;
                case 13:
                    //=disabled=true
                    FillBuffer(new byte[] { 61, 100, 105, 115, 97, 98, 108, 101, 100, 61, 116, 114, 117, 101 }, buffer);
                    break;
                case 14:
                    //Completion of the !re sentence.
                    buffer.Span[0] = 0;
                    break;
                case 15:
                    buffer.Span[0] = SentenceConstants.DoneLength;
                    break;
                case 16:
                    //!done
                    FillBuffer(SentenceConstants.DoneArray, buffer);
                    break;
                case 17:
                    //Completion of the !done sentence.
                    buffer.Span[0] = 0;
                    break;
                default:
                    throw new DataReceivingTestFaultException();
            }

            NextInvoke();

            return ValueTask.CompletedTask;
        }

        public override ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            return ValueTask.CompletedTask;
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionExecuteCommandToListAsyncFlushStream.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal class FakeConnectionExecuteCommandToListAsyncFlushStream : FakeConnectionBase
    {
        public override ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            switch (InvokeIndex)
            {
                case 0:
                    buffer.Span[0] = SentenceConstants.TrapLength;
                    break;
                case 1:
                    //!trap
                    FillBuffer(SentenceConstants.TrapArray, buffer);
                    break;
                case 2:
                    //Completion of the !trap sentence.
                    buffer.Span[0] = 0;
                    break;
                case 3:
                    buffer.Span[0] = SentenceConstants.TrapLength;
                    break;
                case 4:
                    //!trap
                    FillBuffer(SentenceConstants.TrapArray, buffer);
                    break;
                case 5:
                    //Completion of the !trap sentence.
                    buffer.Span[0] = 0;
                    break;
                case 6:
                    buffer.Span[0] = SentenceConstants.DoneLength;
                    break;
                case 7:
                    //!done
                    FillBuffer(SentenceConstants.DoneArray, buffer);
                    break;
                case 8:
                    //Completion of the !done sentence.
                    buffer.Span[0] = 0;
                    break;
                default:
                    throw new DataReceivingTestFaultException();
            }

            NextInvoke();

            return ValueTask.CompletedTask;
        }

        public override ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            return ValueTask.CompletedTask;
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionQuitAsync.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal class FakeConnectionQuitAsync : FakeConnectionBase
    {
        public override ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            switch (InvokeIndex)
            {
                case 0:
                    buffer.Span[0] = SentenceConstants.FatalLength;
                    break;
                case 1:
                    //!fatal
                    FillBuffer(SentenceConstants.FatalArray, buffer);
                    break;
                case 2:
                    buffer.Span[0] = 29;
                    break;
                case 3:
                    //session terminated on request
                    var array = new byte[]
                    {
                        115, 101, 115, 115, 105, 111, 110, 32, 116, 101,
                        114, 109, 105, 110, 97, 116, 101, 100, 32,111,
                        110, 32, 114, 101, 113, 117, 101, 115, 116
                    };

                    FillBuffer(array, buffer);
                    break;
                case 4:
                    //Completion of the sentence.
                    buffer.Span[0] = 0;
                    break;
                default:
                    throw new DataReceivingTestFaultException();
            }

            NextInvoke();

            return ValueTask.CompletedTask;
        }

        public override ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            return ValueTask.CompletedTask;
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionReceiveCommand.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal class FakeConnectionReceiveCommand : FakeConnectionBase
    {
        public override ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            byte[] array;

            switch (InvokeIndex)
            {
                case 0:
                    buffer.Span[0] = SentenceConstants.ReLength;
                    break;
                case 1:
                    //!re
                    FillBuffer(SentenceConstants.ReArray, buffer);
                    break;
                case 2:
                    buffer.Span[0] = 7;
                    break;
                case 3:
                    //=.id=*1
                    FillBuffer(new byte[] { 61, 46, 105, 100, 61, 42, 49 }, buffer);
                    break;
                case 4:
                    buffer.Span[0] = 20;
                    break;
                case 5:
                    //=name=routeros-smips
                    array = new byte[]
                    {
                        61, 110, 97, 109, 101, 61, 114, 111,
                        117, 116, 101, 114, 111, 115, 45,
                        115, 109, 105, 112, 115
                    };

                    FillBuffer(array, buffer);
                    break;
                case 6:
                    buffer.Span[0] = 15;
                    break;
                case 7:
                    //=version=6.47.9
                    array = new byte[]
                    {
                        61, 118, 101, 114, 115, 105, 111, 
                        110, 61, 54, 46, 52, 55, 46, 57
                    };

                    FillBuffer(array, buffer);
                    break;
                case 8:
                    //Completion of the sentence.
                    buffer.Span[0] = 0;
                    break;
                default:
                    throw new DataReceivingTestFaultException();
            }

            NextInvoke();

            return ValueTask.CompletedTask;
        }

        public override ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            return ValueTask.CompletedTask;
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\Networking\FakeConnectionSendCommand.cs
﻿using System;
using System.Threading.Tasks;

namespace MikroTikMiniApi.Tests.Infrastructure.Networking
{
    internal class FakeConnectionSendCommand : FakeConnectionBase
    {
        public ReadOnlyMemory<byte> SendBuffer { get; private set; }

        public override ValueTask ReceiveAsync(Memory<byte> buffer)
        {
            switch (InvokeIndex)
            {
                case 0:
                    buffer.Span[0] = SentenceConstants.DoneLength;
                    break;
                case 1:
                    //!done
                    FillBuffer(SentenceConstants.DoneArray, buffer);
                    break;
                case 2:
                    //Completion of the sentence.
                    buffer.Span[0] = 0;
                    break;
                default:
                    throw new DataReceivingTestFaultException();
            }

            NextInvoke();

            return ValueTask.CompletedTask;
        }

        public override ValueTask SendAsync(ReadOnlyMemory<byte> buffer)
        {
            SendBuffer = buffer;

            return ValueTask.CompletedTask;
        }
    }
}

File: /MikroTikMiniApi.Tests\Infrastructure\SentenceConstants.cs
﻿namespace MikroTikMiniApi.Tests.Infrastructure
{
    internal static class SentenceConstants
    {
        public static readonly byte[] DoneArray = { 33, 100, 111, 110, 101 };
        public static readonly byte[] ReArray = { 33, 114, 101 };
        public static readonly byte[] TrapArray = { 33, 116, 114, 97, 112 };
        public static readonly byte[] FatalArray = { 33, 102, 97, 116, 97, 108 };

        public static readonly byte DoneLength = (byte)DoneArray.Length;
        public static readonly byte ReLength = (byte)ReArray.Length;
        public static readonly byte TrapLength = (byte)TrapArray.Length;
        public static readonly byte FatalLength = (byte)FatalArray.Length;
    }
}

File: /MikroTikMiniApi.Tests\MikroTikMiniApi.Tests.csproj
<Project Sdk="Microsoft.NET.Sdk">

	<PropertyGroup>
		<TargetFramework>net5.0</TargetFramework>
		<IsPackable>false</IsPackable>
		<Platforms>x64</Platforms>
		<TreatWarningsAsErrors>true</TreatWarningsAsErrors>
		<Nullable>enable</Nullable>
	</PropertyGroup>

	<ItemGroup>
		<PackageReference Include="Microsoft.NET.Test.Sdk" Version="16.9.4" />
		<PackageReference Include="xunit" Version="2.4.1" />
		<PackageReference Include="xunit.runner.visualstudio" Version="2.4.3">
			<IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
			<PrivateAssets>all</PrivateAssets>
		</PackageReference>
		<PackageReference Include="coverlet.collector" Version="3.0.2">
			<IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
			<PrivateAssets>all</PrivateAssets>
		</PackageReference>
	</ItemGroup>

	<ItemGroup>
		<ProjectReference Include="..\MikroTikMiniApi\MikroTikMiniApi.csproj" />
	</ItemGroup>

</Project>


File: /MikroTikMiniApi.Tests\Services\AuthenticationServiceTests.cs
﻿using System;
using System.Threading.Tasks;
using MikroTikMiniApi.Exceptions;
using MikroTikMiniApi.Factories;
using MikroTikMiniApi.Services;
using MikroTikMiniApi.Tests.Infrastructure.Networking;
using Xunit;

namespace MikroTikMiniApi.Tests.Services
{
    public class AuthenticationServiceTests
    {
        [Fact]
        public async Task AuthenticationAsync_SendCommand_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var commandExecutionService = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var service = new AuthenticationService(commandExecutionService, localizationService);

            //Act
            await service.AuthenticationAsync("name", "password");

            //Assert
            var memory = new ReadOnlyMemory<byte>(new byte[]
            {
                6, 47, 108, 111, 103, 105, 110, 10, 61, 110,
                97, 109, 101, 61, 110, 97, 109, 101, 18, 61,
                112, 97, 115, 115, 119, 111, 114, 100, 61, 112,
                97, 115, 115, 119, 111, 114, 100, 0
            });

            Assert.True(memory.Span.SequenceEqual(connection.SendBuffer.Span));
        }

        [Fact]
        public async Task AuthenticationAsync_ReceiveResponse_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var commandExecutionService = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var service = new AuthenticationService(commandExecutionService, localizationService);

            //Act
            var exception = await Record.ExceptionAsync(() => service.AuthenticationAsync("name", "password"));

            //Assert
            Assert.Null(exception);
        }

        [Fact]
        public async Task QuitAsync_SendCommand_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var commandExecutionService = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var service = new AuthenticationService(commandExecutionService, localizationService);

            //Act
            var exception = await Record.ExceptionAsync(() => service.QuitAsync());

            //Assert
            var memory = new ReadOnlyMemory<byte>(new byte[] { 5, 47, 113, 117, 105, 116, 0 });

            Assert.IsType<AuthenticationFaultException>(exception);
            Assert.True(memory.Span.SequenceEqual(connection.SendBuffer.Span));
        }

        [Fact]
        public async Task QuitAsync_ReceiveResponse_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForQuitAsync();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var commandExecutionService = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var service = new AuthenticationService(commandExecutionService, localizationService);

            //Act
            var exception = await Record.ExceptionAsync(() => service.QuitAsync());

            //Assert
            Assert.Null(exception);
        }
    }
}

File: /MikroTikMiniApi.Tests\Services\CommandExecutionServiceTests.cs
﻿using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using MikroTikMiniApi.Commands;
using MikroTikMiniApi.Factories;
using MikroTikMiniApi.Interfaces.Factories;
using MikroTikMiniApi.Interfaces.Sentences;
using MikroTikMiniApi.Models.Api;
using MikroTikMiniApi.Models.Settings;
using MikroTikMiniApi.Sentences;
using MikroTikMiniApi.Services;
using MikroTikMiniApi.Tests.Infrastructure.Networking;
using Xunit;

namespace MikroTikMiniApi.Tests.Services
{
    public class CommandExecutionServiceTests
    {
        [Fact]
        public async Task ExecuteCommandAsync_SendCommandWithoutParameters_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/system/package/print").Build();

            //Act
            await service.ExecuteCommandAsync(command, null);

            //Assert
            var memory = new ReadOnlyMemory<byte>(new byte[]
            {
                21, 47, 115, 121, 115, 116, 101, 109, 47, 112, 97,
                99, 107, 97, 103, 101, 47, 112, 114, 105, 110, 116, 0
            });

            Assert.True(memory.Span.SequenceEqual(connection.SendBuffer.Span));
        }

        [Fact]
        public async Task ExecuteCommandAsync_SendCommandWithParameters_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/login")
                                    .AddParameter("name", "name")
                                    .AddParameter("password", "password")
                                    .Build();

            //Act
            await service.ExecuteCommandAsync(command, null);

            //Assert
            var memory = new ReadOnlyMemory<byte>(new byte[]
            {
                6, 47, 108, 111, 103, 105, 110, 10, 61, 110,
                97, 109, 101, 61, 110, 97, 109, 101, 18, 61,
                112, 97, 115, 115, 119, 111, 114, 100, 61, 112,
                97, 115, 115, 119, 111, 114, 100, 0
            });

            Assert.True(memory.Span.SequenceEqual(connection.SendBuffer.Span));
        }

        [Fact]
        public async Task ExecuteCommandAsync_ReceiveResponse_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForReceiveCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/system/package/print").Build();

            //Act
            var actualSentence = await service.ExecuteCommandAsync(command, null);

            //Assert
            var expectedSentence = new ApiReSentence(new[] { "=.id=*1", "=name=routeros-smips", "=version=6.47.9" }, localizationService);

            Assert.Equal(expectedSentence, actualSentence);
        }

        [Fact]
        public async Task ExecuteCommandToListAsync_SendCommand_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForSendCommand();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/ip/service/print").Build();

            //Act
            await service.ExecuteCommandToListAsync(command, null);

            //Assert
            var memory = new ReadOnlyMemory<byte>(new byte[]
            {
                17, 47, 105, 112, 47, 115, 101,
                114, 118, 105, 99, 101, 47, 112,
                114, 105, 110, 116, 0
            });

            Assert.True(memory.Span.SequenceEqual(connection.SendBuffer.Span));
        }

        [Fact]
        public async Task ExecuteCommandToListAsync_ReceiveResponse_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForExecuteCommandToListAsync();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/ip/service/print").Build();

            //Act
            var actualList = await service.ExecuteCommandToListAsync(command, null);

            //Assert
            var expectedList = new IApiSentence[]
            {
                new ApiReSentence(new List<string>{"=.id=*0", "=name=telnet", "=port=23", "=address=", "=invalid=true", "=disabled=true"}, localizationService),
                new ApiDoneSentence(new List<string>(), localizationService)
            };

            Assert.Equal(expectedList, actualList);
        }

        [Fact]
        public async Task ExecuteCommandToListAsyncGeneric_ReceiveResponse_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForExecuteCommandToListAsync();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/ip/service/print").Build();

            //Act
            var actualList = await service.ExecuteCommandToListAsync<Service>(command, null);

            //Assert
            Assert.True(actualList[0].Id == "*0" &&
                        actualList[0].Name == "telnet" &&
                        actualList[0].Port == 23 &&
                        actualList[0].Address == null &&
                        actualList[0].IsInvalid == true &&
                        actualList[0].IsDisabled == true);
        }

        [Fact]
        public async Task ExecuteCommandToListAsync_FlushStreamDefaultSettings_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForExecuteCommandToListAsyncFlushStream();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/interface/print1").Build();

            //Act
            var actualList = await service.ExecuteCommandToListAsync(command, null);

            //Assert
            var expectedList = new IApiSentence[]
            {
                new ApiTrapSentence(new List<string>(), localizationService),
                new ApiTrapSentence(new List<string>(), localizationService),
                new ApiDoneSentence(new List<string>(), localizationService)
            };

            Assert.Equal(expectedList, actualList);
        }

        [Fact]
        public async Task ExecuteCommandToListAsync_FlushStreamNonDefaultSettings_Success()
        {
            //Arrange
            var connection = FakeConnectionBase.CreateForExecuteCommandToListAsyncFlushStream();
            var localizationService = new LocalizationService();
            var sentenceFactory = new ApiSentenceFactory(localizationService);
            var service = new CommandExecutionService(connection, localizationService, sentenceFactory);
            var command = ApiCommand.New("/interface/print1").Build();

            //Act
            var actualList = await service.ExecuteCommandToListAsync(command, ExecutionSettings.Default.Builder
                .WithFlushBeforeDoneSentence(false)
                .WithAttemptsCount(2)
                .Build());

            //Assert
            var expectedList = new IApiSentence[]
            {
                new ApiTrapSentence(new List<string>(), localizationService),
                new ApiTrapSentence(new List<string>(), localizationService),
                new ApiDoneSentence(new List<string>(), localizationService)
            };

            Assert.Equal(expectedList, actualList);
        }
    }
}

File: /README.md
# MikroTikMiniApi
A small and lightweight library for working with the MikroTik router API in C#.


