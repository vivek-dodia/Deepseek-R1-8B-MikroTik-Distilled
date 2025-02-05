# Repository Information
Name: node-red-contrib-mikrotik

# Directory Structure
Directory structure:
└── github_repos/node-red-contrib-mikrotik/
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
    │   │       ├── pack-2a6ebd3f5a8b4dff4faa1883c167e286aeb55b3d.idx
    │   │       └── pack-2a6ebd3f5a8b4dff4faa1883c167e286aeb55b3d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   ├── dependabot.yml
    │   ├── FUNDING.yml
    │   ├── ISSUE_TEMPLATE/
    │   │   ├── bug_report.md
    │   │   └── feature_request.md
    │   └── workflows/
    │       ├── compile.yml
    │       └── publish.yml
    ├── .gitignore
    ├── .npmignore
    │   └── settings.json
    ├── docs/
    │   ├── api-ssl.md
    │   └── example-flows.md
    ├── LICENSE
    ├── package-lock.json
    ├── package.json
    ├── readme.md
    ├── src/
    │   ├── interfaces.d.ts
    │   ├── mikrotik-device.html
    │   ├── mikrotik-device.html.ts
    │   ├── mikrotik-device.ts
    │   ├── mikrotik.html
    │   ├── mikrotik.html.ts
    │   └── mikrotik.ts
    ├── tool/
    │   └── buildhtml.js
    └── tsconfig.json


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
	url = https://github.com/node-red-contrib/node-red-contrib-mikrotik.git
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
0000000000000000000000000000000000000000 eef12d371026c612aed0f2e5a09ec390af35fdd4 vivek-dodia <vivek.dodia@icloud.com> 1738606002 -0500	clone: from https://github.com/node-red-contrib/node-red-contrib-mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 eef12d371026c612aed0f2e5a09ec390af35fdd4 vivek-dodia <vivek.dodia@icloud.com> 1738606002 -0500	clone: from https://github.com/node-red-contrib/node-red-contrib-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 eef12d371026c612aed0f2e5a09ec390af35fdd4 vivek-dodia <vivek.dodia@icloud.com> 1738606002 -0500	clone: from https://github.com/node-red-contrib/node-red-contrib-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
62138f6aa989c31867c20ded8c036651dcd24527 refs/remotes/origin/0nikola1-docs-changes
b16927b755096a12c29cf55dadc69446afd64518 refs/remotes/origin/dependabot/npm_and_yarn/main/typescript-5.7.3
699080bf9d519c429f1188d90d817b2f41aea053 refs/remotes/origin/development
eef12d371026c612aed0f2e5a09ec390af35fdd4 refs/remotes/origin/main
c13c98520d84f1d93185ac719da11278e992ef3b refs/tags/0.3.1
ee9642f2b196716b89d68163b648d020f5bc7197 refs/tags/0.4.0
98c29240f825fb4105e93899c7c602d23af2ddbd refs/tags/0.5.0
7526ac186e7c5dcbc9f756373ff78f46902e887c refs/tags/0.6.0
1a4c7d5cc50161231ff1e437de3cbe77f30644cf refs/tags/0.7.0


File: /.git\refs\heads\main
eef12d371026c612aed0f2e5a09ec390af35fdd4


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.github\dependabot.yml
version: 2
updates:
- package-ecosystem: npm
  directory: "/"
  schedule:
    interval: daily
    time: "08:00"
    timezone: Europe/Berlin
  open-pull-requests-limit: 10
  target-branch: main

- package-ecosystem: "github-actions"
  open-pull-requests-limit: 100
  directory: "/"
  schedule:
    interval: daily
    time: "08:00"
    timezone: Europe/Berlin
  target-branch: main


File: /.github\FUNDING.yml
# These are supported funding model platforms

github: konne


File: /.github\ISSUE_TEMPLATE\bug_report.md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Version (please complete the following information):**

- OS: [e.g. iOS]
- Browser: [e.g. chrome, safari]
- Node-Red: [e.g. 1.x]

**Additional context**
Add any other context about the problem here.


File: /.github\ISSUE_TEMPLATE\feature_request.md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.


File: /.github\workflows\compile.yml
name: compile

on:
  push:
    branches: [ main ]
    paths:
      - 'src/**'
      - '.github/workflows/compile.yml'

  pull_request:
    branches: [ main ]
    paths:
      - 'src/**'
      - '.github/workflows/compile.yml'

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: 15.x
    - name: compile
      run: |
        npm ci
        npm run build --if-present


File: /.github\workflows\publish.yml
name: Publish

on:
  release:
    types: [ published ]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '14.x'

    - name: npm install & set Version
      run: |
        npm ci
        npm config set git-tag-version false
        npm version ${{ github.event.release.tag_name }}

    - name: build & pack
      run:  |
        npm run build --if-present
        npm pack

    - uses: JS-DevTools/npm-publish@v3
      if: "!github.event.release.prerelease"
      with:
          token: ${{ secrets.NPM_TOKEN }}

    - name: Upload Release Asset
      uses: actions/upload-release-asset@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        upload_url: '${{ github.event.release.upload_url }}'
        asset_path: ./${{ github.event.repository.name }}-${{ github.event.release.tag_name }}.tgz
        asset_name: ${{ github.event.repository.name }}-${{ github.event.release.tag_name }}.tgz
        asset_content_type: application/zip


    - name: Update package.json for NameWith2
      uses: jossef/action-set-json-field@v2
      with:
        file: package.json
        field: name
        value: ${{ github.event.repository.name }}2
  
    - name: pack
      run:  |
        ls -al
        rm -f .npmrc
        npm pack

    - name: Update package.json for NameWith3
      uses: jossef/action-set-json-field@v2
      with:
        file: package.json
        field: name
        value: ${{ github.event.repository.name }}3
  
    - name: pack
      run:  |
        npm pack        


File: /.gitignore
File: /.npmignore
File: /.vscode\settings.json
{
    "files.exclude": {
        "**/.git": true,
File: /docs\api-ssl.md
# api-ssl

Mikrotik allowes to connect through ssl to the api.
You should connect through the port usually 8729
that can be configures together with the corresponding
ssl certificate here:

![IP Service List](mikrotik-api-config.png)

If you have a certificate that is not in the registered
CA list of machine there node-red is running on you can
disable the checking of the SSL certificate via the
settings on the mikrotik device settings.


File: /docs\example-flows.md
# Example Flows

Here are some examples of flows to get faster into the usage of the RAW Mode

## Example of getting interface info

Where ***ETHER1INTERNET*** is name of interface

The injected message is:

```json
[
    "/interface/monitor-traffic",
    "=interface=ETHER1INTERNET",
    "=once=true"
]
```

<details>
<summary>Click to expand the full flow!</summary>
<pre>

```
[
    {
        "id": "34844337.ceefbc",
        "type": "mikrotik",
        "z": "f0d0173f.b4a34",
        "device": "",
        "name": "",
        "action": "9",
        "x": 680,
        "y": 2720,
        "wires": [
            [
                "dd3c5317.fd344"
            ]
        ]
    },
    {
        "id": "630604f7.ccb25c",
        "type": "inject",
        "z": "f0d0173f.b4a34",
        "name": "",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "[\"/interface/monitor-traffic\",\"=interface=ETHER1INTERNET\",\"=once=true\"]",
        "payloadType": "json",
        "x": 550,
        "y": 2720,
        "wires": [
            [
                "34844337.ceefbc"
            ]
        ]
    },
    {
        "id": "dd3c5317.fd344",
        "type": "debug",
        "z": "f0d0173f.b4a34",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 850,
        "y": 2720,
        "wires": []
    }
]
```

</pre>
</details><br>

## Example of getting System/Health

The injected message is:

```json
[
    "/system/health/print"
]
```

<details>
<summary>Click to expand the full flow!</summary>
<pre>

```

[
    {
        "id": "4f3bd278.016564",
        "type": "mikrotik",
        "z": "f0d0173f.b4a34",
        "device": "",
        "name": "",
        "action": "9",
        "x": 760,
        "y": 3160,
        "wires": [
            [
                "712e010d.e3cc38"
            ]
        ]
    },
    {
        "id": "b42e32f5.6ce26",
        "type": "change",
        "z": "f0d0173f.b4a34",
        "name": "HEALTH",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "[\"/system/health/print\"]",
                "tot": "json"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 560,
        "y": 3160,
        "wires": [
            [
                "4f3bd278.016564"
            ]
        ]
    },
    {
        "id": "a0525925.11f17",
        "type": "inject",
        "z": "f0d0173f.b4a34",
        "name": "",
        "props": [
            {
                "p": "payload",
                "v": "",
                "vt": "date"
            },
            {
                "p": "topic",
                "v": "",
                "vt": "string"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "x": 411,
        "y": 3156,
        "wires": [
            [
                "b42e32f5.6ce26"
            ]
        ]
    },
    {
        "id": "712e010d.e3cc38",
        "type": "debug",
        "z": "f0d0173f.b4a34",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 930,
        "y": 3160,
        "wires": []
    }
]

```

</pre>
</details><br>

## Example of running script

Where ***Alarm*** is name of script

The injected message is:

```json
[
    "/system/script/run",
    "=.id=Alarm"
]
```

<details>
<summary>Click to expand the full flow!</summary>
<pre>

```

[
    {
        "id": "aee77086.2d473",
        "type": "change",
        "z": "f0d0173f.b4a34",
        "name": "",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "{\"command\":[\"/system/script/run\",\"=.id=Alarm\"]}",
                "tot": "json"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 680,
        "y": 3300,
        "wires": [
            [
                "378e1896.f530e"
            ]
        ]
    },
    {
        "id": "378e1896.f530e",
        "type": "mikrotik",
        "z": "f0d0173f.b4a34",
        "device": "",
        "name": "",
        "action": "9",
        "x": 900,
        "y": 3300,
        "wires": [
            []
        ]
    },
    {
        "id": "c5467461.d3301",
        "type": "inject",
        "z": "f0d0173f.b4a34",
        "name": "",
        "props": [
            {
                "p": "payload",
                "v": "",
                "vt": "date"
            },
            {
                "p": "topic",
                "v": "",
                "vt": "string"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "x": 500,
        "y": 3300,
        "wires": [
            [
                "aee77086.2d473"
            ]
        ]
    }
]

```

</pre>
</details><br>

## Example of getting all DHCP leases

The injected message is:

```json
[
    "/ip/dhcp-server/lease/getall"
]
```

<details>
<summary>Click to expand the full flow!</summary>
<pre>

```

[
    {
        "id": "8916b5a8.ece7e",
        "type": "mikrotik",
        "z": "f0d0173f.b4a34",
        "device": "",
        "name": "",
        "action": "9",
        "x": 660,
        "y": 3120,
        "wires": [
            [
                "d569810b.f2ac7"
            ]
        ]
    },
    {
        "id": "8f7b1436.a771c8",
        "type": "inject",
        "z": "f0d0173f.b4a34",
        "name": "",
        "props": [
            {
                "p": "payload",
                "v": "{\"command\":[\"/ip/dhcp-server/lease/getall\"]}",
                "vt": "json"
            },
            {
                "p": "topic",
                "v": "",
                "vt": "string"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "[\"/ip/dhcp-server/lease/getall\"]",
        "payloadType": "json",
        "x": 350,
        "y": 3120,
        "wires": [
            [
                "7abcc01e.fcd3e8"
            ]
        ]
    },
    {
        "id": "d569810b.f2ac7",
        "type": "debug",
        "z": "f0d0173f.b4a34",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 810,
        "y": 3120,
        "wires": []
    },
    {
        "id": "7abcc01e.fcd3e8",
        "type": "change",
        "z": "f0d0173f.b4a34",
        "name": "All DHCP/lease",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "[\"/ip/dhcp-server/lease/getall\"]",
                "tot": "json"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 500,
        "y": 3120,
        "wires": [
            [
                "8916b5a8.ece7e"
            ]
        ]
    }
]

```

</pre>
</details><br>

## Example of disableing an Ethernet Interface! -> here ether2

The injected message is:

```json
msg.payload = {
    "command": [
        "/interface/ethernet/set",
        "=.id=*2",
        "=disabled=yes"
    ]
}
```

</pre>
</details><br>


File: /LICENSE
Copyright (c) 2016, Alexander Pivovarov

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted, provided that the above copyright notice and
this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

File: /package-lock.json
{
  "name": "node-red-contrib-mikrotik",
  "version": "0.3.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "version": "0.3.0",
      "license": "ISC",
      "dependencies": {
        "node-routeros": "1.6.9"
      },
      "devDependencies": {
        "@types/node-red": "1.3.5",
        "typescript": "5.6.3"
      }
    },
File: /package.json
{
  "name": "node-red-contrib-mikrotik",
  "version": "0.3.0",
  "description": "Node based on node-red-contrib-mikrotik to work with Mikrotik devices which fixes device configuration problem",
  "scripts": {
    "build": "npm run tsc",
    "postbuild": "node tool/buildhtml.js",
    "nodered": "npm run build && node-red",
    "tsc": "tsc"
  },
  "author": "Alexander Pivovarov <pivovarov@gmail.com>",
  "contributors": [
    {
      "name": "Ahmed Al Hafoudh",
      "email": "alhafoudh@freevision.sk",
      "url": "https://www.freevision.sk"
    },
    {
      "name": "Nikola 0nikola1",
      "email": "n@bobetic.com",
      "url": "https://github.com/0nikola1"
    },
    {
      "name": "Konrad Mattheis",
      "url": "https://github.com/konne"
    }
  ],
  "node-red": {
    "nodes": {
      "mikrotik": "nodes/mikrotik.js",
      "mikrotik-device": "nodes/mikrotik-device.js"
    }
  },
  "keywords": [
    "node-red",
    "mikrotik"
  ],
  "license": "ISC",
  "dependencies": {
    "node-routeros": "1.6.9"
  },
  "main": "mikrotik.js",
  "devDependencies": {
    "@types/node-red": "1.3.5",
    "typescript": "5.6.3"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/node-red-contrib/node-red-contrib-mikrotik.git"
  },
  "bugs": {
    "url": "https://github.com/node-red-contrib/node-red-contrib-mikrotik/issues"
  },
  "homepage": "https://github.com/node-red-contrib/node-red-contrib-mikrotik#readme"
}


File: /readme.md

[![CLA assistant](https://cla-assistant.io/readme/badge/node-red-contrib/node-red-contrib-mikrotik)](https://cla-assistant.io/node-red-contrib/node-red-contrib-mikrotik)
![compile](https://github.com/node-red-contrib/node-red-contrib-mikrotik/workflows/compile/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/node-red-contrib/node-red-contrib-mikrotik/badge)](https://www.codefactor.io/repository/github/node-red-contrib/node-red-contrib-mikrotik)
[![npm version](https://badge.fury.io/js/node-red-contrib-mikrotik.svg)](https://badge.fury.io/js/node-red-contrib-mikrotik)
# node-red-contrib-mikrotik a mikrotik node for Node-RED

## Install
[![NPM](https://nodei.co/npm/node-red-contrib-mikrotik.png?downloads=true)](https://nodei.co/npm/node-red-contrib-mikrotik/)

Install via the palette manage in the Node-RED admin ui (no restart needed).

Alternatively run the following command in your Node-RED user directory (typically `~/.node-red`):

```sh
npm install node-red-contrib-mikrotik
```

then restart Node-RED and add an instance of the mikrotik node.

# Config

Available actions:

- ***log***
- ***resources***
- ***wifi***
- ***connections***
- ***reboot***
- ***raw***

## Usage

Add the node to a flow, add an inject and a debug node, configure your connection and you are ready to go.

If you can override every property with the message object. The names are:

msg. -> username, password, host, port, payload/command, ssl

### SSL

If you like to have a ssl connection between the node and the mikrotik router see the [documentation](docs/api-ssl.md)

### Basic

TBD

-----

### RAW

For the usage of the RAW/Command mode there are [here](docs/example-flows.md) some examples.


File: /src\interfaces.d.ts
import { Node } from "node-red";

export interface Credentials {
    secusername: string;
    secpassword: string;
}

export interface MikrotikDeviceConfig {
    host: string;
    port: number;
    ssl: string

    /**
     * @deprecated replaced by secure usage of Credentials
     */
    username:string;

    /**
     * @deprecated replaced by secure usage of Credentials
     */
    password:string;
}

export interface MikrotikDeviceNode extends Node<Credentials>, MikrotikDeviceConfig {

}

File: /src\mikrotik-device.html
<html type="text/x-red" data-template-name="mikrotik-device">
    <div class="form-row">
        <label for="node-config-input-host"><i class="fa fa-server"></i> Host</label>
        <input type="text" id="node-config-input-host">
    </div>
    <div class="form-row">
        <label for="node-config-input-port"><i class="fa fa-server"></i> Port</label>
        <input type="text" id="node-config-input-port">
    </div>
    <div class="form-row">
        <label for="node-config-input-username"><i class="fa fa-user"></i> Username</label>
        <input type="text" id="node-config-input-secusername">
    </div>
    <div class="form-row">
        <label for="node-config-input-password"><i class="fa fa-key"></i> Password</label>
        <input type="password" id="node-config-input-secpassword">
    </div>
    <div class="form-row">
        <label for="node-config-input-ssl"><i class="fa fa-key"></i> SSL</label>
        <select id="node-config-input-ssl" name="ssl">
            <option value="api">API</option>
            <option value="api-ssl">API-SSL</option>
            <option value="api-ssl-ignore-cert">API-SSL self signed</option>
        </select>
    </div>
</html>

File: /src\mikrotik-device.html.ts
import { EditorRED, EditorNodeDef } from "node-red";
declare var RED: EditorRED;
import { Credentials, MikrotikDeviceConfig } from "./interfaces";

RED.nodes.registerType('mikrotik-device', {
    category: 'config',
    defaults: {
        host: { value: '192.168.0.1', required: true },
        port: { value: 8728, required: true, validate: RED.validators.number() },
        username: { value: 'admin' },
        password: { value: '' },
        ssl: { value: 'api' }
    },
    label: function () {
        if (!!this.username)
            return this.username + '@' + this.host + ':' + this.port;
        else
            return this.host + ':' + this.port;
    },
    credentials: {
        secusername: { type: "text" },
        secpassword: { type: "password" },
    },
    oneditprepare() {
        // migrate old non secure credentials in the form

        if (!this.credentials)
            this.credentials = {} as any;

        if (!this.credentials.secusername) {
            this.credentials.secusername = this.username;
            this.credentials.secpassword = this.password;
            $("#node-config-input-secusername").val(this.username);
            $("#node-config-input-secpassword").val(this.password);
        }
    },
    oneditsave() {
        // take care to fully remove the non secured saved credentials
        this.username = null;
        this.password = null;
    }
} as EditorNodeDef<any, any, MikrotikDeviceConfig & { credentials: Credentials }>);



File: /src\mikrotik-device.ts
import { NodeAPI, Node, NodeDef } from "node-red";

import { MikrotikDeviceNode, MikrotikDeviceConfig } from "./interfaces"

export = function (RED: NodeAPI) {
    function NodeConstructorMikrotikDevice(this: MikrotikDeviceNode, def: NodeDef & MikrotikDeviceConfig) {
        RED.nodes.createNode(this, def);

        this.host = def.host;
        this.port = def.port;
        this.ssl = def.ssl;

        if ((!this.credentials) || (!this.credentials.secusername)) {
            // take care the even non "converted" credentials that
            // are still unsafe stored, can be used.
            this.credentials = {
                secusername: def.username,
                secpassword: def.password
            };
        }
    }

    RED.nodes.registerType("mikrotik-device", NodeConstructorMikrotikDevice, {
        credentials: {
            secusername: { type: "text" },
            secpassword: { type: "password" }
        }
    });
}

File: /src\mikrotik.html
<html type="text/x-red" data-template-name="mikrotik">
<div class="form-row">
    <label for="node-input-device"><i class="fa fa-server"></i> Device</label>
    <select id="node-input-device"></select>
</div>

<div class="form-row">
  <label for="node-input-action"><i class="icon-tasks"></i> Action</label>
  <select id="node-input-action" placeholder="action" style="width: 70%;" >
      <option value="0">Log</option>
      <option value="1">System resources</option>
      <option value="2">Connected WiFi</option>
      <option value="3">Reboot</option>
      <option value="9">Raw Command or (use msg.payload)</option>
  </select>
</div>

<div class="form-row" id="node-input-command-row" >
    <label for="node-input-command">Command</label>
    <input type="text" id="node-input-command">
    <input type="hidden" id="node-input-command-type">
</div>

<div class="form-row">
    <label for="node-input-name"><i class="icon-tag"></i> Name</label>
    <input type="text" id="node-input-name" class="paletteLabel" placeholder="Name">
</div>
  
<div class="form-tips">
    You can override the command properties with <code>msg.payload</code> or <code>msg.command</code><br><br>
    To override connections settings just sent <code>msg.user, msg.password, msg.host, msg.port</code>
</div>  
</html>

<html type="text/x-red" data-help-name="mikrotik">
<p>A node that connect with Mikrotik WiFi routers via the
    <a href="http://wiki.mikrotik.com/wiki/API_command_notes" target="_blank">RouterOs API</a>.
</p>

<h3>Configuration</h3>
<b>Device:</b> Setup Mikrotik settings like host, port (8278 - default), username and pass.<br><br>
<b>Action:</b>
<ul>
    <li><b>Log: </b>returns log as <cod>msg.payload</code>. Mikrotik command: <i>/log/print</i></li>
    <li><b>Connected WiFi: </b>returns list of registered WiFi devices as <code>msg.payload</code>. Mikrotik command:
        <i>/interface/wireless/registration-table/print</i></li>
    <li><b>Reboot: </b>reboots Mikrotik. Mikrotik command: <i>/system/reboot</i></li>
    <li><b>Raw:</b> uses <code>msg.payload</code> as command. To pass command with parametrs use JSON object with
        <i>"command"
        </i> property as <code>msg.payload</code>.
        For example: <i>["/system/script/run","=.id=myscript"]</i>. This example runs script <i>myscript</i>
</ul>

<h3>Output</h3>
<dl class="message-properties">
    <dt>payload <span class="property-type">object</span> </dt>
    <dd>The output/result of the executed command on the Mikrotik device.</dd>
    <dt>command<span class="property-type">object</span> </dt>
    <dd>The executed command.</dd>
    <dt>success<span class="property-type">boolean</span></dt>
    <dd>
        <cod>true</cod> if the command could be successfully executed.
    </dd>
</dl>

<h3>Input</h3>
<dl class="message-properties">
    <dt class="optional">payload / command<span class="property-type">object</span></dt>
    <dd>This override the executed command.</dd>
    <dt class="option">user<span class="property-type">string</span></dt>
    <dd>This overrides the username.</dd>
    <dt class="option">password<span class="property-type">string</span></dt>
    <dd>This overrides the password.</dd>
    <dt class="option">host<span class="property-type">string</span></dt>
    <dd>This overrides the host.</dd>
    <dt class="option">port<span class="property-type">number</span></dt>
    <dd>This overrides the port.</dd>
</dl>

</html>


File: /src\mikrotik.html.ts
import { EditorRED, EditorNodeDef } from "node-red";
declare var RED: EditorRED;

RED.nodes.registerType('mikrotik', {
    category: 'network',
    color: '#E9967A',
    defaults: {
        device: { value: '', type: "mikrotik-device" },
        name: { value: '' },
        action: { value: '0' },
        command: { value: '' },
        "command-type": { value: 'str' }
    },
    inputs: 1,
    outputs: 1,
    icon: "feed.png",
    label: function () {
        return this.name || "mikrotik";
    },
    oneditprepare: function () {
        let node = this;
        $("#node-input-action").on('change', function () {
            let cmd = node.command;
            let newType = 'str';

            const lookUp = ['/log/print', '/system/resource/print', '/interface/wireless/registration-table/print', '/system/reboot'];
            let value = parseInt($("#node-input-action").val() as string, 10);
            if (value < 0 || value > 3) {
                value = -1;
                newType = node["command-type"];
            }
            else
                cmd = lookUp[value];

            $("#node-input-command").typedInput('type', newType);
            $("#node-input-command").typedInput('value', cmd);

            $("#node-input-command-row").find('*').prop("disabled", value != -1);
        });

        $("#node-input-command").typedInput({
            default: "str",
            types: ["str", "json"],
            typeField: "#node-input-command-type"
        } as any)
    },
    oneditsave: function () {
        this.action = null;
    }
});

File: /src\mikrotik.ts
import { NodeAPI, Node, NodeMessageInFlow } from "node-red";
import { MikrotikDeviceNode } from "./interfaces"

import { RouterOSAPI } from "node-routeros";

export = function (RED: NodeAPI) {
    function NodeMikrotik(this: Node, config: any) {
        RED.nodes.createNode(this, config);
        let node = this;

        let device = RED.nodes.getNode(config.device) as MikrotikDeviceNode;
        let deviceConfig = {
            host: device.host,
            port: device.port,
            ssl: device.ssl,
            user: device.credentials.secusername,
            password: device.credentials.secpassword,
        };

        let cmd = config.command;
        // convert action -> command for not migrated nodes, can be removed with a breaking change
        if (!cmd) {
            const lookUp = ['/log/print', '/system/resource/print', '/interface/wireless/registration-table/print', '/system/reboot'];
            let value = parseInt(config.action as string, 10);
            if (-1 < value && value < 4)
                cmd = lookUp[value];
        }

        var connection: RouterOSAPI = null;

        this.on('input', function (msg: NodeMessageInFlow & { command: any, success: boolean } & typeof deviceConfig) {
            // allow override of parameters through properties of the message
            let cfg = { ...deviceConfig, tls: null };
            if (msg.user) cfg.user = msg.user;
            if (msg.password) cfg.password = msg.password;
            if (msg.host) cfg.host = msg.host;
            if (msg.port) cfg.port = msg.port;

            if (!msg.command) msg.command = cmd;
            if (!msg.command) msg.command = msg.payload;
            // for compatibility reasons of old mikrotik node
            if (msg.command.command) msg.command = msg.command.command;

            if (msg.ssl) cfg.ssl = msg.ssl;
            if (cfg.ssl) {
                if (cfg.ssl.startsWith('api-ssl'))
                {
                    cfg.tls = {
                        rejectUnauthorized: cfg.ssl !== 'api-ssl-ignore-cert',
                        ciphers: 'ADH-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384'
                    }
                }
                delete cfg.ssl
            }

            try {
                connection = new RouterOSAPI(cfg);
                connection.connect()
                    .then(() => {
                        return connection.write(msg.command);
                    })
                    .then((data) => {
                        msg.payload = data;
                        msg.success = true;
                        node.send(msg);

                        connection.close();
                    })
                    .catch((err) => {
                        node.error('Error executing cmd[' + JSON.stringify(msg.command) + ']: ' + JSON.stringify(err), msg);
                        connection.close();
                    });
            }
            catch (err) {
                node.error('Error: ' + JSON.stringify(err), msg);
            }
        });

        this.on('close', function () {
            connection && connection.connected && connection.close();
        });
    }

    RED.nodes.registerType("mikrotik", NodeMikrotik);
};


File: /tool\buildhtml.js
const fs =require('fs');
const path = require('path');

function copyFile(filename, joinfiles, srcpath, dstpath){

    let src = path.join(srcpath, filename);
    let dst = path.join(dstpath, filename);

    let content = fs.readFileSync(src, 'utf8').replace(/html/g,'script');

    for (const item of joinfiles) {
        let joincontent = fs.readFileSync(path.join(dstpath, item), 'utf8');

        // add differnt join options css, js, ...
        // add search for <script src -> and include this file
        content = '<script type="text/javascript">\r\n'
            + joincontent.replace('Object.defineProperty(exports, "__esModule", { value: true });','')
            +'\r\n</script>\r\n\r\n'
            + content;
        fs.unlinkSync(path.join(dstpath, item));
    }
    fs.writeFileSync(dst, content, 'utf8')
}

var searchpath = 'src/';
var exportpath = 'nodes/'

var entries = fs.readdirSync(searchpath);
var dstentries = fs.readdirSync(exportpath);

for (i = 0; i < entries.length; i ++)
{
    let item = entries[i];
    let fullpath = path.join(searchpath, item);
    if (!fs.lstatSync(fullpath).isDirectory())
    {
        if (item.toLocaleLowerCase().endsWith('.html'))
        {
            let joinfiles = [];
            for (j = 0; j < dstentries.length; j++){
                let item2 = dstentries[j];
                let fullpath2 = path.join(exportpath, item2);
                
                try
                {
                    if (!fs.lstatSync(fullpath2).isDirectory())
                    {
                        if (item2.toLocaleLowerCase().startsWith(item.toLocaleLowerCase())
                        && item2.toLocaleLowerCase() != item.toLocaleLowerCase()) {
                            console.log("     " + item2);
                            joinfiles.push(item2);
                        }
                    }
                }
                catch {}
            }
            copyFile(item, joinfiles, searchpath, exportpath);
        }
    }
}




File: /tsconfig.json
{
    "compilerOptions": {
        "target": "es2015",
        "module": "commonjs",
        "lib": [
            "es2015",
            "dom"
        ],
        "allowJs": false,
        "declaration": false,
        "sourceMap": false,
        "strict": false,
        "outDir": "./nodes/",
    },

}


