# Repository Information
Name: mikrotik-list-importer

# Directory Structure
Directory structure:
└── github_repos/mikrotik-list-importer/
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
    │   │       ├── pack-3070f49b487841e8f6f65ebdb11932260b4a0a1c.idx
    │   │       └── pack-3070f49b487841e8f6f65ebdb11932260b4a0a1c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   ├── dependabot.yml
    │   └── workflows/
    │       └── build.yml
    ├── .gitignore
    ├── build.sbt
    ├── conf/
    │   └── reference.conf
    ├── deb/
    │   └── mkts.service
    ├── project/
    │   ├── build.properties
    │   └── plugins.sbt
    ├── README.md
    └── src/
        └── main/
            ├── resources/
            │   └── logback.xml
            └── scala/
                ├── backend/
                │   └── MikrotikConnection.scala
                ├── cache/
                │   └── Cache.scala
                ├── ip/
                │   └── IPMerger.scala
                ├── Main.scala
                ├── Models.scala
                └── repo/
                    ├── AddressListRepo.scala
                    └── BackendImplicits.scala


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
	url = https://github.com/Th3Falc0n/mikrotik-list-importer.git
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
0000000000000000000000000000000000000000 40e8d84ce791ffe20bff1fe9c9493fb5f932f277 vivek-dodia <vivek.dodia@icloud.com> 1738606427 -0500	clone: from https://github.com/Th3Falc0n/mikrotik-list-importer.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 40e8d84ce791ffe20bff1fe9c9493fb5f932f277 vivek-dodia <vivek.dodia@icloud.com> 1738606427 -0500	clone: from https://github.com/Th3Falc0n/mikrotik-list-importer.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 40e8d84ce791ffe20bff1fe9c9493fb5f932f277 vivek-dodia <vivek.dodia@icloud.com> 1738606427 -0500	clone: from https://github.com/Th3Falc0n/mikrotik-list-importer.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
bf5c2f892252d0603104a62ff598c4c290de0ff0 refs/remotes/origin/dependabot/github_actions/actions/setup-java-4.2.0
5dbee49cc31ad5c13ded762e4700b0dfda4647fc refs/remotes/origin/dependabot/github_actions/actions/upload-artifact-4
e0997bc44192460ae7abda411f8227786e10c41c refs/remotes/origin/feature/remote-io
40e8d84ce791ffe20bff1fe9c9493fb5f932f277 refs/remotes/origin/master
5e6a8324c1799ef2ab28a0382a9bf54d0e6aacb7 refs/remotes/origin/script-only
01517a8f4f7a70881ac60878dcad21c8f36b43e3 refs/remotes/origin/update/cats-core-2.10.0
67a4b85df48d92ad45aad9a85e681b9d4467a9ea refs/remotes/origin/update/cats-core-2.13.0
16a9cf94348c79aaac9e1913af28496a9da2b411 refs/remotes/origin/update/cats-effect-3.4.10
fc34b25591f7f23b6b66597ea2d03a23e220fa5b refs/remotes/origin/update/cats-effect-3.4.11
7b6ea3fdc55d624e9600bd249f4dec8db43eee82 refs/remotes/origin/update/cats-effect-3.4.5
0b25b115099db693c756249840966454a02410d3 refs/remotes/origin/update/cats-effect-3.4.9
00e43340bbcdc5f995093a6526b3a54d821c3a01 refs/remotes/origin/update/cats-effect-3.5.0
942c805ea50fda3763b565ebde95d6467fe01ff3 refs/remotes/origin/update/cats-effect-3.5.2
fa7e66f04d4f9f6a76f8751badda2134cbe5a56e refs/remotes/origin/update/cats-effect-3.5.7
42aafff8fed3dcad6ee1683fd8d66ad004ca21cc refs/remotes/origin/update/client3-3.7.0
92ee18d8b925e92835798518ad6351f14b55058c refs/remotes/origin/update/client3-3.7.1
5aad86748ba03a66b1906c3331050f7c678cb448 refs/remotes/origin/update/client3-3.7.2
d2fbff0d2928e8dbe5d6bbbf0eda4134a9fdb01d refs/remotes/origin/update/client3-3.7.4
8d9ea38b5d189e984b64f8c6f1dfa9ce77b77a30 refs/remotes/origin/update/client3-3.7.5
8dd5187a6ec02fa5e5c38d14f8ae5e3e6f099fc5 refs/remotes/origin/update/client3-3.7.6
b46dd31011c3d77f77f711dc416346ed67976bf3 refs/remotes/origin/update/http4s-blaze-server-0.23.14
46e1b7d027873835f514eabb6a25ef62db0b2891 refs/remotes/origin/update/http4s-blaze-server-0.23.15
fe44163a94d8d9a99d5d3e5b093e4ad44f5b80fb refs/remotes/origin/update/http4s-blaze-server-0.23.17
88ac23fa2d078dcc890d2a20776e2c361c958fe7 refs/remotes/origin/update/http4s-dsl-0.23.30
1951a9020e8259f49ca64ddda1425f8c8448f5ec refs/remotes/origin/update/http4s-server-0.23.14
bfc886baff49e08cbb8cd1fd41a33310f4a1eccc refs/remotes/origin/update/http4s-server-0.23.15
fa7a6b422e2a6409e8353a617aa88acd5772ba51 refs/remotes/origin/update/logback-classic-1.4.0
b5929e2fb8cb9803c75d644169cb0c687eb4fd56 refs/remotes/origin/update/logback-classic-1.4.1
077f3e9d1a48d2469db8fb9dcdd0ea0c9b720811 refs/remotes/origin/update/logback-classic-1.4.11
377fe257db197877c4b66d00eee930f4944bc411 refs/remotes/origin/update/logback-classic-1.4.13
d3fd32799af2a39a14fcfe1d10c8f800b29715e0 refs/remotes/origin/update/logback-classic-1.4.14
335441551cb795d8ca87d516a5d720dc854f5fa1 refs/remotes/origin/update/logback-classic-1.4.3
71f831d2d81d8b847869e84191d30b2ce79a9cc2 refs/remotes/origin/update/logback-classic-1.4.4
9e0b0f617b594a7406c8136a052769a2162e2924 refs/remotes/origin/update/logback-classic-1.4.6
908db547901e5f4ea025f8970c5ae9d7801ee0c9 refs/remotes/origin/update/logback-classic-1.4.7
675b1882cee2ee35bfdfe520546961ba54d81fd2 refs/remotes/origin/update/mikrotik-3.0.8
c776490d15ad3a7fdd815743840d67f3b27bab75 refs/remotes/origin/update/sbt-1.7.2
21fccdf07f9acbe22873617e9a06b055514d5ec9 refs/remotes/origin/update/sbt-1.7.3
3437153ccee4c9f2304ecb7b163c2441464348b7 refs/remotes/origin/update/sbt-1.8.0
de09a06ab3990ad679fcaebfbb879120415bed9e refs/remotes/origin/update/sbt-1.8.2
663504f3c5d49ac14a6447b669e0c4e70d06cb70 refs/remotes/origin/update/sbt-1.8.3
387060a1a0135d6114141d3ad72206a117095e55 refs/remotes/origin/update/sbt-1.9.4
e1b8c8a326529570cd4401b20473391c96d12b7d refs/remotes/origin/update/sbt-1.9.6
9c62a4cc504fe5cb7ab6ba112a82a9f8a2a9f07c refs/remotes/origin/update/sbt-1.9.7
cc637cc9c21879bb04c1593ff60f510ecd14b24a refs/remotes/origin/update/sbt-1.9.9
a0cf4d48677089b667ade4f39ac953ab125e19ab refs/remotes/origin/update/sbt-assembly-2.1.3
4fd5d10f854a4737e715a3ddc33f7a3fc45463f8 refs/remotes/origin/update/sbt-assembly-2.1.5
716a833450fc73cecc949060d32bd92b11c57328 refs/remotes/origin/update/sbt-assembly-2.3.1
c78e1a9a31c701028951aa4b804f9abca8fc28d3 refs/remotes/origin/update/scala-library-2.13.10
3710ed30ca9b9dab2ee9f3f991f50c45567097be refs/remotes/origin/update/scala-library-2.13.11
53feaa62d454196f445c228d2c6243907d7db66c refs/remotes/origin/update/scala-library-2.13.12
a5647a7cee2534f73f13fe27fdcb2b5dc44e6250 refs/remotes/origin/update/scala-library-2.13.16
7c94f10031e947da7df7f2b928cdbc1d4d72f7be refs/remotes/origin/update/slf4j-api-2.0.16
9db4edd8141f762ebbd8f0d8811875ff4f51c515 refs/remotes/origin/update/slf4j-api-2.0.2
4c27d0b7fed08b794795240b1f00faff56ea32d8 refs/remotes/origin/update/slf4j-api-2.0.3
a16c44787f6cccc600da569fd1a2569d7be6c515 refs/remotes/origin/update/slf4j-api-2.0.7
b2b6781b051cb7f115697ba6f9ae0d07f2ca7055 refs/remotes/origin/update/slf4j-api-2.0.9
0064e77eac9e665eca5cded42e2e38b93386c57c refs/remotes/origin/update/typesafe-1.4.3
730471ae139cc2d07435ca751cdfbe52f2564b52 refs/remotes/origin/webservice
5e4b0125d0efd2be72d6e64ad832a0d89c80d768 refs/tags/working-deb-deployment


File: /.git\refs\heads\master
40e8d84ce791ffe20bff1fe9c9493fb5f932f277


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\dependabot.yml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "daily"


File: /.github\workflows\build.yml
name: build

on:
  push:
    branches:
      - '**'
    tags-ignore:
      - '*.*'
  pull_request:

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4.0.0
        with:
          distribution: 'adopt'
          java-version: '11'
      - name: Build
        run: sbt "; test; assembly"
      - uses: actions/upload-artifact@v3
        with:
          path: 'server/target/scala-*/*.jar'

File: /.gitignore
#Git
.cache

#Gradle
.gradle/
build/
gradle-app.setting

#Other
File: /build.sbt
inThisBuild(Seq(
  scalaVersion := "2.13.12",
  name := "mikrotik-list-importer",
  version := "0.1"
))

name := (ThisBuild / name).value

idePackagePrefix := Some("de.th3falc0n.mkts")

Compile / mainClass := Some("de.th3falc0n.mkts.Main")

assembly / mainClass := Some("de.th3falc0n.mkts.Main")

assembly / assemblyOption := (assembly / assemblyOption).value.withIncludeScala(false)

libraryDependencies ++= Seq(
  "org.typelevel" %% "cats-core" % "2.10.0",
  "org.typelevel" %% "cats-effect" % "3.5.2",
  "me.legrange" % "mikrotik" % "3.0.7",
  "com.typesafe" % "config" % "1.4.3",
  "org.slf4j" % "slf4j-api" % "2.0.9",
  "ch.qos.logback" % "logback-classic" % "1.4.13"
)

val http4sVersion = "0.23.15"

libraryDependencies ++= Seq(
  "org.http4s" %% "http4s-blaze-server" % http4sVersion,
  "org.http4s" %% "http4s-blaze-client" % http4sVersion,
  "org.http4s" %% "http4s-dsl" % http4sVersion
)

ThisBuild / assemblyMergeStrategy := {
  case "module-info.class" => MergeStrategy.discard
  case x =>
    val oldStrategy = (ThisBuild / assemblyMergeStrategy).value
    oldStrategy(x)
}


File: /conf\reference.conf
mikrotik.host = "10.2.1.1"
mikrotik.user = "api"
mikrotik.password = "<YOUR_PASSWORD>"

cacheDuration = "15m"

lists = [
  {
    name: "spamhaus_drop",
    sources: [
      "https://www.spamhaus.org/drop/drop.txt",
      "https://www.spamhaus.org/drop/edrop.txt"
    ],
    update-interval: "1h"
  }
]


File: /deb\mkts.service
[Unit]
Description=Imports IP lists into mikrotik routers

[Service]
Type=simple
ExecStart=scala -Dconfig.file=/opt/mkts/application.conf /opt/mkts/mkts.jar

[Install]
WantedBy=multi-user.target

File: /project\build.properties
sbt.version = 1.9.7

File: /project\plugins.sbt
addSbtPlugin("org.jetbrains" % "sbt-ide-settings" % "1.1.0")
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.1.5")


File: /README.md
# mikrotik-list-importer
Mikrotik List Import is a tool to import any IP blocklists (for example the lists from https://iplists.firehol.org) into an address list in your mikrotik router.

## Example application.conf

```
mikrotik.host = "10.2.1.1"
mikrotik.user = "api"
mikrotik.password = ""

lists = [
  {
    name: "threats",
    sources: [
      "https://www.spamhaus.org/drop/drop.txt",
      "https://www.spamhaus.org/drop/edrop.txt",
      "https://iplists.firehol.org/files/et_block.netset",
      "https://iplists.firehol.org/files/dshield_30d.netset",
      "https://iplists.firehol.org/files/et_tor.ipset",
      "https://iplists.firehol.org/files/et_compromised.ipset",
      "http://cinsscore.com/list/ci-badguys.txt"
    ],
    update-interval: "1h"
  }
]
```

## Example rules
```
chain=prerouting action=drop log=yes log-prefix="THREATS_IN" src-address-list=threats
chain=prerouting action=drop log=yes log-prefix="THREATS_OUT" dst-address-list=threats
```


File: /src\main\resources\logback.xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%date %level %logger - %message%n%xException{full}</pattern>
        </encoder>
    </appender>

    <appender name="ASYNCSTDOUT" class="ch.qos.logback.classic.AsyncAppender">
        <appender-ref ref="STDOUT"/>
    </appender>

    <logger name="org.http4s.blaze.channel" level="WARN"/>

    <root level="INFO">
        <appender-ref ref="ASYNCSTDOUT"/>
    </root>
</configuration>


File: /src\main\scala\backend\MikrotikConnection.scala
package de.th3falc0n.mkts
package backend

import Main.config
import Models.IP

import me.legrange.mikrotik.ApiConnection
import org.slf4j.{ Logger, LoggerFactory }

import scala.jdk.CollectionConverters._

object MikrotikConnection {
  val logger: Logger = LoggerFactory.getLogger(this.getClass)

  def updateList(name: String, ips: Seq[IP]): Unit = {
    logger.info("Connecting to API at {}", config.getString("mikrotik.host"))
    val api = ApiConnection.connect(config.getString("mikrotik.host"))

    logger.info("Logging in with user {}", config.getString("mikrotik.user"))
    api.login(
      config.getString("mikrotik.user"),
      config.getString("mikrotik.password")
    )

    logger.info("Updating list {}", name)
    val ipsAsString = ips.map(_.toString)

    val result = api.execute(s"/ip/firewall/address-list/print where list=$name return address, .id").asScala.toSeq
    val usedIPs = result.map(_.get("address"))

    val toAdd = ipsAsString.diff(usedIPs)
    val toRemove = usedIPs.diff(ipsAsString)

    logger.info("Removing {} IPs from list {}", toRemove.length, name)

    val toRemoveIds = toRemove.map(tr => result.find(_.get("address") == tr).get.get(".id"))

    if (toRemoveIds.nonEmpty) {
      toRemoveIds.grouped(100).foreach(ids => {
        api.execute(s"/ip/firewall/address-list/remove numbers=${ids.mkString(",")}")
      })
    }

    logger.info("Adding {} IPs to list {}", toAdd.length, name)
    toAdd.foreach(ip => api.execute(s"/ip/firewall/address-list/add list=$name address=\"$ip\""))

    api.close()
  }
}


File: /src\main\scala\cache\Cache.scala
package de.th3falc0n.mkts
package cache

import java.time.{ Duration, Instant }
import scala.collection.mutable

object Cache {
  private case class Cached[+T](value: T, time: Instant)

  private val cache = mutable.HashMap.empty[String, Cached[Any]]

  def getOrElseUpdate[T](key: String, value: => T): T = {
    cache.get(key) match {
      case Some(v: Cached[T]) if Duration.between(v.time, Instant.now).compareTo(Main.config.getDuration("cacheDuration")) < 0 =>
        v.value

      case Some(v: Cached[T]) =>
        val newValue = value
        cache -= key
        cache += (key -> Cached(newValue, Instant.now))
        newValue

      case Some(_) =>
        throw new IllegalArgumentException("Cache.getOrElseUpdate: Key was not of type T")

      case None =>
        val newValue = value
        cache += (key -> Cached(newValue, Instant.now))
        newValue
    }
  }

}


File: /src\main\scala\ip\IPMerger.scala
package de.th3falc0n.mkts
package ip

import Models.IP

import org.slf4j.LoggerFactory

object IPMerger {
  private val logger = LoggerFactory.getLogger("IPMerger")

  def mergeIPs(in: Seq[IP], depth: Int = 31): Seq[IP] = {
    val distinct = in.distinct
    val ips = distinct.filterNot(a => distinct.filter(_ != a).exists(b => b.contains(a)))
    logger.debug(ips.mkString(","))

    val atDepth = ips.filter(ip => ip.maskBits == depth + 1)
    logger.debug("Found {} usable IPs at depth {}", atDepth.length, depth)

    val passed = ips.diff(atDepth)
    logger.debug("Ignored {} IPs at depth {}", passed.length, depth)

    val possibleNetworks = atDepth.map(i => IP(i.host, depth)).filter(_.isNetwork)
    logger.debug("{} possible merges at depth {}", possibleNetworks.length, depth)

    val merged = possibleNetworks.filter(_.nextTwoSubs.forall(atDepth.contains(_)))
    logger.debug("{} actual merges at depth {}", merged.length, depth)

    val mergedNets = merged.flatMap(_.nextTwoSubs)
    val notMerged = atDepth.diff(mergedNets)
    logger.debug(" {} not merged at depth {}", notMerged.length, depth)

    val continueToMerge = passed ++ merged

    if(continueToMerge.nonEmpty) {
      notMerged ++ mergeIPs(continueToMerge, depth - 1)
    } else {
      notMerged
    }
  }
}


File: /src\main\scala\Main.scala
package de.th3falc0n.mkts

import Models.{ AddressList, AddressSource }
import repo.AddressListRepo
import repo.BackendImplicits.BackendAddressList

import cats.effect.unsafe.implicits.global
import cats.effect.{ ExitCode, IO, IOApp }
import cats.implicits._
import com.typesafe.config.{ Config, ConfigFactory }
import org.slf4j.LoggerFactory

import java.util.concurrent.TimeUnit
import scala.concurrent.duration.{ Duration, FiniteDuration }
import scala.jdk.CollectionConverters.CollectionHasAsScala

object Main extends IOApp {
  private val logger = LoggerFactory.getLogger(this.getClass)
  logger.info("Initializing")

  val config: Config = ConfigFactory.load()

  val activeRepo: AddressListRepo[IO] = AddressListRepo.inMemImpl

  override def run(args: List[String]): IO[ExitCode] = {
    logger.info("Starting server and background tasks")

    config.getConfigList("lists").forEach(list => {
      val addressList = AddressList(
        list.getString("name"),
        list.getStringList("sources").asScala.toSeq.map(src => AddressSource(src)),
        Duration.apply(list.getDuration("update-interval").toMillis, TimeUnit.MILLISECONDS)
      )
      logger.info("Loaded address list {} from application config", addressList)
      activeRepo.put(addressList).unsafeRunSync()
    })

    activeRepo.list.flatMap { lists =>
      logger.info(s"Found ${lists.size} lists")

      lists.map { list =>
        logger.info("Started for {}", list.toString)

        def update: IO[Unit] = list.update >> IO.sleep(list.updateInterval.asInstanceOf[FiniteDuration]) >> IO.defer(update)

        update
      }.sequence
    }.start.flatMap(_ => IO.never).as(ExitCode.Success)
  }
}


File: /src\main\scala\Models.scala
package de.th3falc0n.mkts

import scala.concurrent.duration.Duration

object Models {
  case class AddressSource(name: String, enabled: Boolean = true)

  case class AddressList(name: String, sources: Seq[AddressSource], updateInterval: Duration)

  case class IP(host: Int, maskBits: Int) {
    def isNetwork: Boolean = (host & (0xFFFFFFFF << (32 - maskBits))) == host

    def nextTwoSubs: Seq[IP] = {
      val subnet = host & (0xFFFFFFFF << (32 - maskBits))
      val a = subnet
      val b = a + (1 << (31 - maskBits))
      Seq(IP(a, maskBits + 1), IP(b, maskBits + 1))
    }

    def contains(other: IP): Boolean = {
      if (!this.isNetwork) throw new IllegalArgumentException("Not a network")

      if (other.maskBits < this.maskBits) return false

      (other.host & (0xFFFFFFFF << (32 - maskBits))) == host
    }

    override def toString: String = {
      val a = host >> 24 & 0xFF
      val b = host >> 16 & 0xFF
      val c = host >> 8 & 0xFF
      val d = host & 0xFF
      if (maskBits < 32) {
        s"$a.$b.$c.$d/$maskBits"
      } else {
        s"$a.$b.$c.$d"
      }
    }
  }

  object IP {
    def fromString(ipString: String): IP = {
      val parts = ipString.split('/')
      val host = parts(0)
      val netmask = if (parts.length == 2) parts(1) else "32"

      IP(host.split('.').map(_.toInt).reduceLeft(_ * 256 + _), netmask.toInt)
    }
  }
}


File: /src\main\scala\repo\AddressListRepo.scala
package de.th3falc0n.mkts
package repo

import Models.AddressList

import cats.effect.{ IO, Ref }

trait AddressListRepo[F[_]] {
  def list: F[Seq[AddressList]]

  def put(addressList: AddressList): F[Unit]

  def delete(addressListName: String): F[Unit]
}

object AddressListRepo {
  def inMemImpl: AddressListRepo[IO] = new AddressListRepo[IO] {
    private val addressLists = Ref.unsafe[IO, Seq[AddressList]](Seq.empty[AddressList])

    override def list: IO[Seq[AddressList]] =
      addressLists.get

    override def put(addressList: AddressList): IO[Unit] =
      addressLists.update(_.filterNot(_.name == addressList.name) :+ addressList)

    override def delete(addressListName: String): IO[Unit] =
      addressLists.update(_.filterNot(_.name == addressListName))
  }
}


File: /src\main\scala\repo\BackendImplicits.scala
package de.th3falc0n.mkts
package repo

import Models.{ AddressList, AddressSource, IP }
import backend.MikrotikConnection
import cache.Cache
import ip.IPMerger

import cats.effect.{ ExitCode, IO }
import cats.implicits.toTraverseOps
import org.http4s.Uri
import org.slf4j.LoggerFactory

import java.time.Duration
import org.http4s.client.blaze._

import scala.concurrent.ExecutionContext.Implicits.global

object BackendImplicits {
  implicit class BackendAddressSource(addressSource: AddressSource) {
    private val uri = Uri.fromString(addressSource.name).toOption.get
    private val logger = LoggerFactory.getLogger(s"iplist-${addressSource.name}")

    def fetch: IO[Seq[IP]] = {
      logger.info("Fetching")

      val ips = Cache.getOrElseUpdate(
        s"fetch-${addressSource.hashCode()}",
        BlazeClientBuilder[IO].resource.use { client =>
          val request = client.expect[String](uri)

          request.map { r =>
            val result = r
              .split("\n")
              .filter(_.nonEmpty)
              .map(_.split(' ').head)
              .filter(ip => "^[0-9][0-9./]*$".r.matches(ip))
              .map(IP.fromString)
              .filter {
                case ip if IP.fromString("10.0.0.0/8").contains(ip) => false
                case ip if IP.fromString("172.16.0.0/12").contains(ip) => false
                case ip if IP.fromString("192.168.0.0/16").contains(ip) => false
                case _ => true
              }

            logger.info("Got {} IPs", result.length, addressSource.name)

            result.toSeq
          }
        }
          .handleErrorWith { error =>
            logger.error("Error while fetching", error)
            IO.pure(Seq.empty)
          }
      )

      ips
    }
  }

  implicit class BackendAddressList(addressList: AddressList) {
    private val logger = LoggerFactory.getLogger("AddressList-" + addressList.name)

    def fetch: IO[Seq[IP]] = {
      for {
        ips <- addressList.sources.map(_.fetch).sequence.map(_.flatten)
      } yield {
        logger.info("Got {} unique IPs", ips.length)
        val merged = IPMerger.mergeIPs(ips)

        logger.info("Reduced to {} unique list entries", merged.length)
        merged
      }
    }

    def update: IO[ExitCode] = {
      for {
        merged <- fetch
      } yield {
        MikrotikConnection.updateList(addressList.name, merged)

        logger.info("Updated list {} with {} unique IPs", addressList.name, merged.length)
        ExitCode.Success
      }
    }
  }
}


