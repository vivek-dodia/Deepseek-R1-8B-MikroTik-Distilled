# Repository Information
Name: vscode_mikrotik_routeros_script

# Directory Structure
Directory structure:
└── github_repos/vscode_mikrotik_routeros_script/
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
    │   │       ├── pack-ad224d8fa883a0aaa1bb2b022d486a91501a97c2.idx
    │   │       └── pack-ad224d8fa883a0aaa1bb2b022d486a91501a97c2.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .res/
    │   └── QR/
    │   ├── launch.json
    │   └── settings.json
    ├── .vscodeignore
    ├── .vsixmanifest
    ├── CHANGELOG.md
    ├── images/
    ├── language-configuration.json
    ├── LICENSE
    ├── package.json
    ├── package.nls.json
    ├── README.md
    ├── snippets/
    │   └── rosScript.json
    └── syntaxes/
        └── rosScript.tmLanguage.json


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
	url = https://github.com/devMikeUA/vscode_mikrotik_routeros_script.git
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
0000000000000000000000000000000000000000 aaf19c0581ffe238850eb42aefe0ce67bb6ed9d8 vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/devMikeUA/vscode_mikrotik_routeros_script.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 aaf19c0581ffe238850eb42aefe0ce67bb6ed9d8 vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/devMikeUA/vscode_mikrotik_routeros_script.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 aaf19c0581ffe238850eb42aefe0ce67bb6ed9d8 vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/devMikeUA/vscode_mikrotik_routeros_script.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
aaf19c0581ffe238850eb42aefe0ce67bb6ed9d8 refs/remotes/origin/master


File: /.git\refs\heads\master
aaf19c0581ffe238850eb42aefe0ce67bb6ed9d8


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
node_modules
*.vsix

File: /.vscode\launch.json
// A launch configuration that launches the extension inside a new window
// Use IntelliSense to learn about possible attributes.
// Hover to view descriptions of existing attributes.
// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
{
	"version": "0.2.0",
    "configurations": [
        {
            "name": "Extension",
            "type": "extensionHost",
            "request": "launch",
            "runtimeExecutable": "${execPath}",
            "args": [
                "--extensionDevelopmentPath=${workspaceFolder}"
            ]
        }
    ]
}

File: /.vscode\settings.json
{
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "ipv4.rosScript",
			    "settings": {
                "foreground": "#cc8b00"
                }
            }
        ]
    }
}

File: /.vscodeignore
.res
.gitignore
vsc-extension-quickstart.md


File: /.vsixmanifest
<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="Mikrotik RouterOs script" Version="2018.8.2" Publisher="devMike"/>
    <DisplayName>Mikrotik RouterOS script.</DisplayName>
    <Description xml:space="preserve">Provides snippets, syntax highlighting, bracket matching in Mikrotik RouterOS script files.</Description>
    <Tags>Mikrotik,RouterOS,MikrotikOS,mros,mross,mrosscript,rosscript,ros,rsc, __ext_.rsc</Tags>
    <Categories>Programming Languages,Snippets,Other</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Badges></Badges>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="0.10.x" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value="" />
      <Property Id="Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown" Value="true" />
    </Properties>
    <Icon>extension/images/icon.png</Icon>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/CHANGELOG.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="extension/images/icon.png" Addressable="true" />
  </Assets>
</PackageManifest>


File: /CHANGELOG.md
# Change Log

### 2022.9.2
- Add some RouterOS 7 syntax highlighting.
- Fix some syntax highlighting.
To be continue ;)

### 2018.8.2
- Modify snippet (add new).

### 2018.8.1
- Fix some syntax highlighting.

### 2018.8.0
- First release.

File: /language-configuration.json
{
    "comments": {
        "lineComment": "#",
        "blockComment": [ "#" ]
    },
    "brackets": [
        ["{", "}"],
        ["[", "]"],
        ["(", ")"]
    ],
    "autoClosingPairs": [
        { "open": "{", "close": "}", "notIn": ["comment"] },
        { "open": "[", "close": "]", "notIn": ["comment"] },
        { "open": "(", "close": ")", "notIn": ["comment"] },
        ["\"", "\""],
        ["'", "'"]
    ],
    "surroundingPairs": [
        { "open": "{", "close": "}" },
        { "open": "[", "close": "]" },
        { "open": "(", "close": ")" },
        { "open": "\"", "close": "\"" },
        { "open": "'", "close": "'" }
    ],
	"folding": {
		"offSide": true,
		"markers": {
			"start": "{",
			"end": "}"
		},
        "wordPattern": "(-?\\d*\\.\\d\\w*)|([^\\`\\~\\!\\@\\#\\%\\^\\&\\*\\(\\)\\-\\=\\+\\[\\{\\]\\}\\\\\\|\\;\\:\\'\\\"\\,\\.\\<\\>\\/\\?\\s]+)"
    }
}

File: /LICENSE
MIT License

Copyright (c) 2018 Mikhail Korzhov

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


File: /package.json
{
    "name": "mikrotik-routeros-script",
	"displayName": "%displayName%",
	"description": "%description%",
    "version": "2022.9.2",
    "publisher": "devMike",
    "license": "MIT",
    "preview": true,
    "icon": "images/icon_ua.png",
    "engines": {
        "vscode": "^1.13.0"
    },
    "categories": [
		"Programming Languages",
        "Snippets",
        "Other"
	],
    "contributes": {
        "languages": [{
            "id": "rosScript",
            "extensions": [".rsc"],
            "aliases": [
                "Mikrotik RouterOS Script",
                "RouterOS Script",
                "Mikrotik Script",
                "Mikrotik",
                "RouterOS", 
                "rsc",
                "mrosscript",
                "ross"
            ],
            "configuration": "./language-configuration.json"
        }],
        "grammars": [{
            "language": "rosScript",
            "scopeName": "source.rsc",
            "path": "./syntaxes/rosScript.tmLanguage.json"
        }],
    "snippets": [{
        "language": "rosScript",
        "path": "./snippets/rosScript.json"
    }]
    },
	"__metadata": {
		"publisherDisplayName": "Korzhov Mikhail"
    },
    "bugs": {
        "url": "https://github.com/devMikeUA/vscode_mikrotik_routeros_script/issues",
        "email": "smteamgroup@gmail.com"
    },
    "repository": {
        "type": "git",
        "url": "https://github.com/devMikeUA/vscode_mikrotik_routeros_script.git"
    },
    "homepage": "https://github.com/devMikeUA/vscode_mikrotik_routeros_script/blob/master/README.md"
}

File: /package.nls.json
{
	"displayName": "Mikrotik RouterOS script",
	"description": "Provides snippets, syntax highlighting, bracket matching for Mikrotik RouterOS script."
}

File: /README.md
# Mikrotik RouterOS script
[![version](https://vsmarketplacebadge.apphb.com/version/devMike.mikrotik-routeros-script.svg)][_1]
[![install](https://vsmarketplacebadge.apphb.com/installs-short/devMike.mikrotik-routeros-script.svg)][_1]
[![Gitter](https://img.shields.io/badge/chat-Gitter-brightgreen.svg)][_2]
[![Discord](https://img.shields.io/badge/chat-Discord-brightgreen.svg)][_3]
[![Telegram](https://img.shields.io/badge/chat-Telegram-brightgreen.svg)][_4]

[_1]:https://marketplace.visualstudio.com/items?itemName=devMike.mikrotik-routeros-script
[_2]:https://gitter.im/Mikrotik-RouterOS-script/LetsTalk?utm_source=share-link&utm_medium=link&utm_campaign=share-link
[_3]:https://discordapp.com/channels/488241725085712385/488241725635035139
[_4]:https://t.me/rosscript

### Support me:
#### Hi all. I live in Ukraine and in these difficult times, you can support our project.

- UAH [Donatello](https://donatello.to/devMikeUA)
- USD EUR (PayPal) - smteamgroup@gmail.com

### Provides:
- snippets
- syntax highlighting
- bracket matching for Mikrotik RouterOS script.

## Snippets

![Snippets](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/images/example.gif)

## Syntax Highlighting

![Syntax](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/images/example.png)

## Let's make writing scripts easier:
- [Download source (.zip file)][1]
- [Label issues][2]
- [Pull requests][3]
- [Tell about in Twitter][4] (#rosScript #RouterOSScript #Mikrotik #RouterOS #devMike)

[1]:https://github.com/devMikeUA/vscode_mikrotik_routeros_script/archive/master.zip
[2]:https://github.com/devMikeUA/vscode_mikrotik_routeros_script/issues
[3]:https://github.com/devMikeUA/vscode_mikrotik_routeros_script/pulls
[4]:https://www.twitter.com/home?status=%20%23rosScript%20%23RouterOSScript%20%23Mikrotik%20%23RouterOS%20%23devMike%20Let's%20make%20writing%20scripts%20easier%20%23VSMarketplace%3A%20https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DdevMike.mikrotik-routeros-script

## Chat

- ![Gitter](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/gitter_24.png) [Gitter][_2]
- ![Discord](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/discord_24.png) [Discord][_3]
- ![Telegram](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/telegram_24.png) [Telegram][_4]

## Contacts
- ![Github](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/github_24.png) [GitHub](https://github.com/devMikeUA/)
- ![Twitter](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/twitter_24.png) [Twitter](https://twitter.com/devMikeUA/)
- ![Linkedin](https://github.com/devMikeUA/vscode_mikrotik_routeros_script/raw/master/.res/linkedin_24.png) [LinkedIn](https://www.linkedin.com/in/devMikeUA/)

## License

MIT © [Korzhov Mikhail](https://github.com/devMikeUA)

## Release Notes

### 2022.9.2
- Add some RouterOS 7 syntax highlighting.
- Fix some syntax highlighting.
To be continue ;)

### 2018.8.2
- Modify snippet (add new).

### 2018.8.1
- Fix some syntax highlighting.

### 2018.8.0
- First release.

File: /snippets\rosScript.json
{
	":global <var> [<value>]":{
		"prefix": ":global",
		"body": ":global ${1:myVar} ${2|0,\"\",[],()|};$0",
		"description": "Define global variable."
	},

	":local <var> [<value>]":{
		"prefix": ":local",
		"body": ":local ${1:myVar} ${2|0,\"\",[],()|};$0",
		"description": "Define local variable."
	},

	":beep <freq> <length>":{
		"prefix": ":beep",
		"body": ":beep ${1:freq} ${2:length};$0",
		"description": "Beep built in speaker."
	},

	":delay <time>":{
		"prefix": ":delay",
		"body": ":delay $1${2|s,m,h|};$0",
		"description": "Do nothing for a given period of time."
	},

	":put <expression>":{
		"prefix": ":put",
		"body": ":put ${1|[],(),\"\"|};$0",
		"description": "Put supplied argument to console."
	},

	":len <expression>":{
		"prefix": ":len",
		"body": ":len ${1:\"length-8\"};$0",
		"description": "Return string length or array element count."
	},

	":typeof <var>":{
		"prefix": ":typeof",
		"body": ":typeof ${1:4};$0",
		"description": "Return data type of variable."
	},

	":pick <var> <start>":{
		"prefix": ":pick",
		"body": ":pick ${1:\"abcde\"} ${2:1} ${3:3};\n$0",
		"description": "Return range of elements or substring. If end position is not specified, will return only one element from an array."
	},

	":log <topic> <message>":{
		"prefix": ":log",
		"body": ":log ${1|debug,error,info,warning|} ${2:\"Hello from script\"};$0",
		"description": "Write message to system log. Available topics are \"debug, error, info and warning\"."
	},

	":time <expression>":{
		"prefix": ":time",
		"body": ":time {$1};$0",
		"description": "Return interval of time needed to execute command."
	},

	":set <var> [<value>]":{
		"prefix": ":set",
		"body": ":set ${1:a} ${2:true};$0",
		"description": "Assign value to declared variable."
	},

	":find <arg> <arg> <start>":{
		"prefix": ":find",
		"body": ":find ${1:\"abc\"} ${2:\"a\"} ${3:-1};$0",
		"description": "Return position of substring or array element."
	},

	":environment print <start>":{
		"prefix": ":environment",
		"body": ":environment ${1:\\$myVar};$0",
		"description": "Print initialized variable information."
	},

	":error <output>":{
		"prefix": ":error",
		"body": ":error ${1:\"error message\"};$0",
		"description": "Generate console error and stop executing the script."
	},

	":execute <expression>":{
		"prefix": ":execute",
		"body": ":execute {$1};$0",
		"description": "Execute the script in background."
	},

	":parse <expression>":{
		"prefix": ":parse",
		"body": ":parse ${1:\":put hello!\"};$0",
		"description": "Parse string and return parsed console commands. Can be used as function."
	},

	":resolve <arg>":{
		"prefix": ":resolve",
		"body": ":resolve ${1:\"www.mikrotik.com\"};$0",
		"description": "Return IP address of given DNS name."
	},

	":toarray <var>":{
		"prefix": ":toarray",
		"body": ":toarray ${1:myVar};$0",
		"description": "Convert variable to array."
	},

	":tobool <var>":{
		"prefix": ":tobool",
		"body": ":tobool ${1:myVar};$0",
		"description": "Convert variable to boolean."
	},

	":toid <var>":{
		"prefix": ":toid",
		"body": ":toid ${1:myVar};$0",
		"description": "Convert variable to internal ID."
	},

	":toip <var>":{
		"prefix": ":toip",
		"body": ":toip ${1:myVar};$0",
		"description": "Convert variable to IP address."
	},

	":toip6 <var>":{
		"prefix": ":toip6",
		"body": ":toip6 ${1:myVar};$0",
		"description": "Convert variable to IPv6 address."
	},

	":tonum <var>":{
		"prefix": ":tonum",
		"body": ":tonum ${1:myVar};$0",
		"description": "Convert variable to integer."
	},

	":tostr <var>":{
		"prefix": ":tostr",
		"body": ":tostr ${1:myVar};$0",
		"description": "Convert variable to string."
	},

	":totime <var>":{
		"prefix": ":totime",
		"body": ":totime ${1:myVar};$0",
		"description": "Convert variable to time."
	},

	"add <param>=<value>..<param>=<value>":{
		"prefix": "add",
		"body": "add $1;$0",
		"description": "Add new item."
	},

	"remove <id>":{
		"prefix": "remove",
		"body": "remove ${1:id};$0",
		"description": "Remove selected item."
	},

	"enable <id>":{
		"prefix": "enable",
		"body": "enable ${1:id};$0",
		"description": "Enable selected item."
	},

	"disable <id>":{
		"prefix": "disable",
		"body": "disable ${1:id};$0",
		"description": "Disable selected item."
	},

	"set <id> <param>=<value>..<param>=<value>":{
		"prefix": "set",
		"body": "set $1;$0",
		"description": "Change selected items parameter, more than one parameter can be specified at the time. Parameter can be unset by specifying '!' before parameter. "
	},

	"get <id> <param>=<value>..<param>=<value>":{
		"prefix": "get",
		"body": "get $1;$0",
		"description": "Get selected items parameter value."
	},

	"print <param><param>=[<value>]":{
		"prefix": "print",
		"body": "print $1;$0",
		"description": "Print menu items. Output depends on print parameters specified."
	},

	"export [file=<value>]":{
		"prefix": "export",
		"body": "export file=${1:config}${2:_}${3:$CURRENT_YEAR$CURRENT_MONTH$CURRENT_DATE$CURRENT_HOUR$CURRENT_MINUTE}.rsc;$0",
		"description": "Export configuration from current menu and its sub-menus (if present). If file parameter is specified output will be written to file with extension '.rsc', otherwise output will be printed to console."
	},

	"edit <id> <param>":{
		"prefix": "edit",
		"body": "edit ${1:id} ${2:param};$0",
		"description": "Edit selected items property in built-in text editor."
	},

	"find <expression>":{
		"prefix": "find",
		"body": "find ${1:expression};$0",
		"description": "Returns list of internal numbers for items that are matched by given expression. For example:  :put [/interface find name~\"ether\"]."
	},

	":if (<condition>) do={<commands>}":{
		"prefix": ":if",
		"body": ":if (${1:true}) do={ $0 }",
		"description": "If a given condition is true then execute commands in the do block."
	},

	":if (<condition>) do={<commands>}\nelse={<commands>} <expression>":{
		"prefix": ":ifelse",
		"body": ":if (${1:true}) do={\n\t$2\n} else={ $0 }",
		"description": "If a given condition is true then execute commands in the do block, otherwise execute commands in the else block if specified."
	},

	":do { <commands> } while=( <conditions> ); :while ( <conditions> ) do={ <commands> };":{
		"prefix": ":dowhile",
		"body": ":do { $1 } while ($0)",
		"description": "Execute commands until given condition is met."
	},
	
	":for <var> from=<int> to=<int> step=<int> do={ <commands> }":{
		"prefix": ":for",
		"body": ":for ${1:i} from=${2:1} to=${3:9} do={ $0 }",
		"description": "Execute commands over a given number of iterations."
	},

	":foreach <var> in=<array> do={ <commands> };":{
		"prefix": ":foreach",
		"body": ":foreach ${1:i} in=${2:array} do={ $0 }",
		"description": "Execute commands for each elements in list."
	},

	"append":{
		"prefix": "append",
		"body": "append$0"
	},

	"print as-value":{
		"prefix": "print as-value",
		"body": "print as-value$0",
		"description": "Print output as array of parameters and its values."
	},

	"print brief":{
		"prefix": "print brief",
		"body": "print brief$0",
		"description": "Print brief description."
	},
	
	"print detail":{
		"prefix": "print detail",
		"body": "print detail$0",
		"description": "Print detailed description, output is not as readable as brief output, but may be useful to view all parameters."
	},

	"print count-only":{
		"prefix": "print count-only",
		"body": "print count-only$0",
		"description": "Print only count of menu items."
	},

	"print file":{
		"prefix": "print file",
		"body": "print file=${1:\"fileName\"}$0",
		"description": "Print output to file."
	},

	"print follow":{
		"prefix": "print follow",
		"body": "print follow$0",
		"description": "Print all current entries and track new entries until ctrl-c is pressed, very useful when viewing log entries."
	},

	"print follow-only":{
		"prefix": "print follow-only",
		"body": "print follow-only$0",
		"description": "Print and track only new entries until ctrl-c is pressed, very useful when viewing log entries."
	},

	"print from":{
		"prefix": "print from",
		"body": "print from=${1:admin}$0",
		"description": "Print parameters only from specified item."
	},

	"print interval":{
		"prefix": "print interval",
		"body": "print interval=${1:2}$0",
		"description": "Continuously print output in selected time interval, useful to track down changes where follow is not acceptable."
	},

	"print terse":{
		"prefix": "print terse",
		"body": "print terse$0",
		"description": "Show details in compact and machine friendly format."
	},

	"print value-list":{
		"prefix": "print value-list",
		"body": "print value-list$0",
		"description": "Show  values one per line (good for parsing purposes)."
	},

	"print without-paging":{
		"prefix": "print without-paging",
		"body": "print without-paging$0",
		"description": "If output do not fit in console screen then do not stop, print all information in one piece."
	},

	"print where":{
		"prefix": "print where",
		"body": "print where $0",
		"description": "Expressions followed by where parameter can be used to filter out matched entries."
	}
}

File: /syntaxes\rosScript.tmLanguage.json
{
  "name": "rosScript",
  "scopeName": "source.rsc",
  "fileTypes": ["rsc"],
  "patterns": [
    {
      "match": "\\b(ipsec-esp|ipsec-ah|idpr-cmtp|iso-tp4|xns-idp|udp-lite|ip-encap|icmp|igmp|ggp|st|tcp|egp|pup|udp|hmp|rdp|dccp|xtp|ddp|rsvp|gre|rspf|vmtp|ospf|ipip|etherip|encap|pim|vrrp|l2tp|sctp)\\b",
      "name": "variable.other.rosScript"
    },
    {
      "match": "(dns|https|http|smb)",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "qwerty",
      "name": "ipv4.rosScript"
    },
    {
      "match": "\\b(system|package|update)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "(?<=\\=)\\b(\\S)*\\b",
      "name": "support.type.rosScript"
    },
    {
      "match": "\\b(ftp|h323|irc|pptp|sip|tftp|updplite|api-ssl|api|ssh|telnet|winbox|www-ssl|www|reboot|read|write|test|sniff|sensitive|romon)\\b",
      "name": "variable.other.rosScript"
    },
    {
      "match": "\\b(up-script|netwatch|watchdog-timer|owner|ntp|on-event|down-script|src-and-dst-addresses|dst-limit|limit|to-ports|silent-boot|routerboard|allow-remote-requests|pptp-server|authentication-types|in-filter|security-profiles|multicast-helper|tx-power|wps-mode|user-manager|access|time-zone-autodetect|time-zone-name)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "\\b(own-routers|own-users|own-profiles|own-limits|config-payment-gw|always-broadcast|cache-max-ttl|discover-interface-list|in-interface)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "(?<=(\\=|\n|\\s|\\,))(input|output|forward|srcnat|dstnat|untracked)",
      "name": "support.type.rosScript"
    },
    {
      "match": "(?<=\\=)(accept|add-dst-to-address-list|add-src-to-address-list|drop|fasttrack-connection|jump|log|passthrough|reject|return|tarpit)",
      "name": "support.type.rosScript"
    },
    {
      "match": "(?<=\\=)(none-dynamic|none-static)",
      "name": "support.type.rosScript"
    },
    {
      "match": "[0-9]{1,3}Mbps|(2|5)ghz",
      "name": "support.type.rosScript"
    },
    {
      "match": "([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})(\\s|-([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}))",
      "name": "support.type.rosScript"
    },
    {
      "match": "([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}/[0-9]{1,2})(\\s|\\-([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}/[0-9]{1,2}))",
      "name": "support.type.rosScript"
    },
    {
      "match": "([0-9A-F]{2}[:-]){5}([0-9A-F]{2})(\\s)",
      "name": "support.type.rosScript"
    },
    {
      "match": "\\b(if|else|for|foreach|do|while)(?=\\s|\\{|\\=|\\[|\\()",
      "name": "keyword.control.rosScript"
    },
    {
      "match": "\\b(and|or|not|in|&&|\\!|\\|\\|)\\b",
      "name": "keyword.operator.logical"
    },
    {
      "match": "~|\\||\\^|&|<<|>>",
      "name": "keyword.operator.logical"
    },
    {
      "match": "\\b(detail|error|file|info|led|nothing|password|time|date)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "captures": {
        "1": {
          "name": "storage.modifier.rosScript"
        },
        "2": {
          "name": "variable.other.rosScript"
        }
      },
      "match": ":(global|local|set)\\s([a-zA-Z0-9-]*)"
    },
    {
      "match": "\\b(from|to|step)\\b",
      "name": "keyword.control"
    },
    {
      "match": "\\$[a-zA-Z0-9-]*",
      "name": "variable.other.rosScript"
    },
    {
      "match": "\\b(radius|routing|snmp|special-login|store|system|tool|user|certificate|driver|file|interface|ip|ipv6|log|mpls|port|queue)\\b",
      "name": "support.function.builtin.rosScript"
    },
    {
      "match": "\\b(len|setup|typeof|toarray|tobool|toid|toip|toip6|tonum|tostr|totime)\\b",
      "name": "support.function.builtin.rosScript"
    },
    {
      "match": "\\b(accept|add|beep|delay|do|drop|execute|export|find|get|import|log|parse|pick|ping|print|put|quit|redirect|redo|resolve|set|undo)\\b",
      "name": "support.function.builtin.rosScript"
    },
    {
      "match": "\\b(true|false|yes|no)\\b",
      "name": "constant.language.boolean.rosScript"
    },
    {
      "begin": "'",
      "end": "'",
      "name": "string.quoted.single.rosScript",
      "patterns": [
        {
          "include": "#string_escaped_char",
          "name": "constant.character.escape.rosScript"
        }
      ]
    },
    {
      "begin": "\"",
      "end": "\"",
      "name": "string.quoted.double.rosScript",
      "patterns": [
        {
          "include": "#string_escaped_char",
          "name": "constant.character.escape.rosScript"
        }
      ]
    },
    {
      "begin": "(^[ \\t]+)?(?=#)",
      "beginCaptures": {
        "1": {
          "name": "punctuation.whitespace.comment.leading.rosScript"
        }
      },
      "end": "(?!\\G)",
      "patterns": [
        {
          "begin": "#",
          "beginCaptures": {
            "0": {
              "name": "punctuation.definition.comment.rosScript"
            }
          },
          "end": "\\n",
          "name": "comment.line.number-sign.rosScript"
        }
      ]
    },
    {
      "match": "<\\=|>\\=|\\=\\=|<|>|\\!\\=",
      "name": "keyword.operator.comparison"
    },
    {
      "match": "\\+|\\-|\\*|\\/",
      "name": "keyword.operator.arithmetic"
    },
    {
      "comment": "Concatenates strings and arrays",
      "match": "\\.|,",
      "name": "keyword.operator.string"
    },
    {
      "match": "\\[|\\(|\\)|\\:|\\[|\\]|\\{|\\||\\}|\\]",
      "name": "punctuation.section"
    },
    {
      "match": "=",
      "name": "keyword.operator.assignment"
    },
    {
      "match": "\\b([1-9]+[0-9]*|0)",
      "name": "constant.numeric.integer.decimal.rosScript"
    },
    {
      "include": "#other_keywords",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "country|band|antenna-gain|hw-protection-mode|wireless-protocol|adaptive-noise-immunity|default-name|basic-rates-a/g|basic-rates|basic-rates-b|frequency|connect-to",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "\\b(debug|error|info|warning)\\b",
      "name": "variable.parameter"
    },
    {
      "match": "\\b(bgp|ip|ipsec|ipv6|ldp|ospf-v3|ppp|rip|snmp)\\b",
      "name": "constant.other.rosScript.protocol"
    },
    {
      "match": "\\b(6to4|bonding|bridge|eoip|eoipv6|ethernet|wireless|gre6|ipipv6|isdn-client|isdn-server|l2tp-client|l2tp-server|lte|mesh|ovpn-client|ovpn-server|ppp-client|pppoe-client|pppoe-server|ppp-server|pptp-client|pptp-server|sstp-client|sstp-server|traffic-eng|vlan|vpls)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "\\b(new|related|established|invalid)\\b",
      "name": "constant.other.rosScript.connection-state"
    },
    {
      "match": "\\b(use-ipsec|user|use-network-apn|listen-port|wireguard|l2tp-client|station-roaming|installation|channel-width|regexp|pcq-classifier|max-limit|packet-mark|ingress-filtering)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "\\b(start-date|start-time|connection-mark|allowed-address|layer7-protocol)\\b",
      "name": "keyword.other.rosScript"
    },
    {
      "match": "\\!([\\w\\d])*",
      "name": "keyword.control.rosScript"
    }
  ],
  "repository": {
    "other_keywords": {
      "patterns": [
        {
          "match": "\\b(fast-forward|dns|cache|aaa|accessible-via-web|accounting|account-local-traffic|ac-name|action|active-flow-timeout|active-mode|add-default-route|ageing-time|align|always-from-cache|area|area-id|arp|as|authenticate|authoritative|automatic-supout|auto-negotiation|autonomous|auto-send-supout|backup-allowed|bandwidth-server|baud-rate|bfd|bidirectional-timeout|blank-interval|bootp-support|bootp-lease-time|bridge-mode|broadcast|broadcast-addresses|cable-settings|cache-administrator|cache-entries|cache-hit-dscp|cache-max-ttl|cache-on-disk|cache-size|chain|channel|channel-time|check-interval|cipher|client|client-to-client-reflection|comment|community|config|connection-state|connection|connection-bytes|connection-idle-timeout|connection-state|console|contact|contrast|cpu|customer|data-bits|default|default-ap-tx-limit|default-client-tx-limit|default-forwarding|default-group|default-profile|default-route-distance|dhcp-options|dhcp-client|dhcp-option|dhcp-server|dh-group|dial-on-demand|directory|disabled|disable-running-check|discovery|disk-file-count|disk-file-name|disk-lines-per-file|disk-stop-on-full|display-time|distance|distribute-default|distribute-for-default-route|domain|dpd-interval|dpd-maximum-failures|dynamic-label-range|eap-methods|e-mail|enabled|enc-algorithm|enc-algorithms|encryption-password|encryption-protocol|engine-id|exchange-mode|exclude-groups|file-limit|file-name|filter|filter-port|filter-stream|firewall|firmware|flow-control|forward-delay|frame-size|frames-per-second|from|full-duplex|garbage-timer|gateway|gateway-class|gateway-keepalive|gateway-selection|generate-policy|generic-timeout|gps|graphing|group|group-ciphers|group-key-update|hardware|hash-algorithm|health|hide-ssid|hop-limit|hotspot|hotspot-address|html-directory|http-cookie-lifetime|http-proxy|icmp-timeout|identity|idle-timeout|igmp-proxy|ignore-as-path-len|inactive-flow-timeout|incoming|in-filter|instance|interface|interfaces|interim-update|interval|ipsec-protocols|irq|jump-target|keepalive-timeout|keep-max-sms|kind|l2mtu|latency-distribution-scale|lcd|lease-time|level|lifebytes|lifetime|line-count|list|local-address|local-proxy-arp|location|logging|login|login-by|log-prefix|loop-detect|lsr-id|managed-address-configuration|management-protection|management-protection-key|mangle|manual|manycast|max-cache-size|max-fresh-time|max-message-age|max-mru|max-mtu|max-sessions|max-station-count|memory-limit|memory-lines|memory-scroll|memory-stop-on-full|metric-connected|metric-default|metric-static|min-rx|mirror|mme|mode|mpls|mpls-mtu|mq-pfifo-limit|mrru|mtu|multicast|multi-cpu|multiple-channels|multiplier|my-id-user-fqdn|name|nat|nat-traversal|nd|neighbor|netmask|network|no-ping-delay|note|on-backup|only-headers|only-one|on-master|origination-interval|other-configuration|out-filter|out-interface|page|page-refresh|parent|parent-proxy|parent-proxy-port|parity|passthrough|password|path-vector-limit|peer|permissions|pfifo-limit|pfs-group|policy|pool|port|ports|preemption-mode|preferred-gateway|preferred-lifetime|prefix|priority|profile|propagate-ttl|proposal|proposal-check|proprietary-extensions|protocol|protocol-mode|proxy|query-interval|query-response-interval|queue|quick-leave|ranges|rate-limit|reachable-time|read-access|read-only|receive-all|receive-enabled|receive-errors|remember|remote|remote-address|remote-port|remote-ipv6-prefix-pool|resource|retransmit-interval|route|router-id|routing|routing-table|sa-dst-address|sa-src-address|scope|screen|script|secret|send-initial-contact|set-system-time|settings|sfq-allot|sfq-perturb|shared-users|shares|show-at-login|show-dummy-rule|signup-allowed|sip-direct-media|skin|sms|sniffer|snooper|socks|source|speed|split-user-domain|ssid|ssid-all|state-after-reboot|status-autorefresh|stop-bits|store-every|store-leases-disk|supplicant-identity|system|target|target-scope|term|test-id|threshold|timeout|timeout-timer|to-addresses|tool|topics|tracking|traffic-flow|traffic-generator|transmit-hold-count|transparent-proxy|transport-address|ttl|tunnel|type|unicast-ciphers|upgrade|upnp|users|v3-protocol|valid-lifetime|vcno|version|vrid|watch-address|watchdog|watchdog-timer|web-access|address|address-list|address-pool|addresses|addresses-per-mac|admin-mac|advertise-mac-address|auto-mac|filter-mac|mac-address|filter-mac-address|filter-mac-protocol|mac-addressmac-server|mac-winbox|advertise-dns|dns-interface|dns-name|dns-server|use-peer-dns|allow|allow-disable-external-interface|allowed-number|allow-guests|audio-max|audio-min|audio-monitor|auth|auth-algorithms|auth-method|authentication|authentication-password|authentication-protocol|authentication-types|default-authentication|bsd-syslog|syslog-facility|syslog-severity|scheduler|clock|time-zone|time-zone-name|new-connection-mark|new-packet-mark|new-routing-mark|routing-mark|dst-address|dst-address-list|dst-delta|dst-end|dst-port|dst-start|max-client-connections|max-connections|max-server-connections|serialize-connections|metric-ospf|metric-other-ospf|redistribute-ospf|redistribute-other-ospf|metric-rip|redistribute-rip|ripng|ntp-server|primary-ntp|secondary-ntp|use-peer-ntp|paypal-accept-pending|paypal-allowed|paypal-secure-response|primary-server|secondary-server|ra-delay|ra-interval|ra-lifetime|radius|radius-eap-accounting|radius-mac-accounting|radius-mac-authentication|radius-mac-caching|radius-mac-format|radius-mac-mode|red-avg-packet|red-burst|red-limit|red-max-threshold|red-min-threshold|redistribute-connected|redistribute-static|require-client-certificate|tls-certificate|tls-mode|verify-client-certificate|security|security-profile|security-profiles|server|servers|service|service-name|service-port|smtp-server|wins-server|src-address|src-address-list|src-port|static-algo-0|static-algo-1|static-algo-2|static-algo-3|static-sta-private-algo|static-key-0|static-key-1|static-key-2|static-key-3|static-sta-private-key|static-transmit-key|streaming-enabled|streaming-max-rate|streaming-server|switch-to-spt|switch-to-spt-bytes|switch-to-spt-interval|trap-generators|trap-target|trap-version|update-stats-interval|update-timer|use-compression|use-encryption|use-explicit-null|use-ipv6|use-mpls|use-radius|use-service-tag|use-vj-compression|wmm-support|wpa-pre-shared-key|wpa2-pre-shared-key|write-access|metric-bgp|redistribute-bgp|redistribute-other-bgp|change-tcp-mss|tcp-close-timeout|tcp-close-wait-timeout|tcp-established-timeout|tcp-fin-wait-timeout|tcp-last-ack-timeout|tcp-syn-received-timeout|tcp-syn-sent-timeout|tcp-syncookie|tcp-time-wait-timeout|allocate-udp-ports-from|max-udp-packet-size|udp-stream-timeout|udp-timeout|use-ip-firewall-for-vlan|vlan-id|filter-ip-address|filter-ip-protocol|use-ip-firewall-for-pppoe|use-ip-firewall|wds-cost-range|wds-default-bridge|wds-default-cost|wds-ignore-ssid|wds-mode|job|environment)\\b",
          "name": "keyword.other.rosScript"
        }
      ]
    },
    "string_escaped_char": {
      "patterns": [
        {
          "match": "\\\\(\\\\|[nrt$?abfv\"?]|[0-9A-F]{2})",
          "name": "constant.character.escape.rosScript"
        },
        {
          "match": "\\\\.",
          "name": "invalid.illegal.unknown-escape.rosScript"
        }
      ]
    }
  }
}

