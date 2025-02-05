# Repository Information
Name: mikrotikapipingutilityapt

# Directory Structure
Directory structure:
└── github_repos/mikrotikapipingutilityapt/
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
    │   │       ├── pack-fb33c8781b0d1e74bf95a0fb2df8726cccb6cbaa.idx
    │   │       └── pack-fb33c8781b0d1e74bf95a0fb2df8726cccb6cbaa.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── conf/
    │   └── distributions
    ├── db/
    │   ├── checksums.db
    │   ├── contents.cache.db
    │   ├── packages.db
    │   ├── references.db
    │   ├── release.caches.db
    │   └── version
    ├── dists/
    │   └── bionic/
    │       ├── InRelease
    │       ├── main/
    │       │   └── binary-amd64/
    │       │       ├── Packages
    │       │       ├── Packages.gz
    │       │       └── Release
    │       ├── Release
    │       └── Release.gpg
    ├── pool/
    │   └── main/
    │       └── m/
    │           └── mikrotikapiping/
    │               └── mikrotikapiping_2.0-0ubuntu1_amd64.deb
    ├── PUBLIC.KEY
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
	url = https://github.com/komalashrafsyed/mikrotikapipingutilityapt.git
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
0000000000000000000000000000000000000000 b8bbc28148b6dd07462decdc05dd3a30e778c2e3 vivek-dodia <vivek.dodia@icloud.com> 1738606394 -0500	clone: from https://github.com/komalashrafsyed/mikrotikapipingutilityapt.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b8bbc28148b6dd07462decdc05dd3a30e778c2e3 vivek-dodia <vivek.dodia@icloud.com> 1738606394 -0500	clone: from https://github.com/komalashrafsyed/mikrotikapipingutilityapt.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b8bbc28148b6dd07462decdc05dd3a30e778c2e3 vivek-dodia <vivek.dodia@icloud.com> 1738606394 -0500	clone: from https://github.com/komalashrafsyed/mikrotikapipingutilityapt.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b8bbc28148b6dd07462decdc05dd3a30e778c2e3 refs/remotes/origin/master


File: /.git\refs\heads\master
b8bbc28148b6dd07462decdc05dd3a30e778c2e3


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /conf\distributions
Origin: MikrotikAPIPing Tool
Label: mikrotikapiping
Codename: bionic
Architectures: amd64
Components: main
Description: Personal repository
SignWith: DE905706E32A1AEB5FF283D717F1848324B9C0F4


File: /db\version
5.1.1
3.3.0
bdb5.3.28
bdb5.3.0


File: /dists\bionic\InRelease
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Origin: MikrotikAPIPing Tool
Label: mikrotikapiping
Codename: bionic
Date: Tue, 31 Dec 2019 21:32:58 UTC
Architectures: amd64
Components: main
Description: Personal repository
MD5Sum:
 a7ec7ab1e9f13991af2c0b1dea905cb2 734 main/binary-amd64/Packages
 826a016a9cc7eb8480b0a5e6a33d17d5 491 main/binary-amd64/Packages.gz
 7984536c85a82c478752372afdbfbf71 121 main/binary-amd64/Release
SHA1:
 c356f12e978cbcd2dc7c2e084153124be036e5b3 734 main/binary-amd64/Packages
 d51b79a1c09a16f9a67eec10ecce3f9cb020da4e 491 main/binary-amd64/Packages.gz
 b7a78e9bb83315bd68037908c23bd6894a5f1b03 121 main/binary-amd64/Release
SHA256:
 09d167a2e69b1e810642124473cd32133bfd183ce318adfceb1d3fd028235c27 734 main/binary-amd64/Packages
 2a4afe1ab291dd96c048a1d9ed1326249c2d97f89a98f83dd03bd5796280aba0 491 main/binary-amd64/Packages.gz
 8549d45e864dced320eae142f11cfce00069dc8e8fb840fa2a3af1efbd9c58f5 121 main/binary-amd64/Release
-----BEGIN PGP SIGNATURE-----

iQGzBAEBCgAdFiEE3pBXBuMqGutf8oPXF/GEgyS5wPQFAl4Lvo4ACgkQF/GEgyS5
wPRk/Qv+MMhpD6TB7wUUvOAMmcT06a6UAQddFV8IlF8t6GlVBFkJcB+/JdLikJ2A
ynx/MFFLvmWG7rfwFHtZ0TGPhpw9gUrHy5MlLfKOzEDBGTUAV4DbWzzT9C21VOM8
rxkWEzNWpNlWKVjH75F8gKkYMUACrNL4sOWzIIde94152P9mqS6LNfUeSgEOAeRb
4m5Fx6Uzqtz0P+6hJVX3jsLACVGoNMygPVz3ZLFKrjQv5fiyfnmRqK5wFIL+MzAO
pCrFnThB2w8Wa8hswF9AzW7JKeIZKAH0SZEiAcG0IhbZ8yoMrq8sLm5S3lWNOsWi
+XoYaTFNl9DoxvxtzdcYYcGzTIh9+XWrXNCDZopK+e08X2Tckkggi4dEhxJkoZYT
6VYLM3b8QroyVaAehlBQE7W7Upm9DfZA6KvtpL1MmJahKGS8l8lg5st8N7tQptlK
HmIDK6FE4yVPN0g0CVZ+cz1tMVFpa7k+/rYhe0WSQ1ax5Ox/TzvRb6f+Ir3lKPEc
rpQvNID7
=8Y+K
-----END PGP SIGNATURE-----


File: /dists\bionic\main\binary-amd64\Packages
Package: mikrotikapiping
Version: 2.0-0ubuntu1
Architecture: amd64
Maintainer: root v-kosyed@microsoft.com
Installed-Size: 76864
Depends: libc6 (>= 2.14), libcurl4 (>= 7.16.2), libgcc1 (>= 1:3.0), libgssapi-krb5-2 (>= 1.14+dfsg), liblttng-ust0 (>= 2.5.0), libstdc++6 (>= 4.8), zlib1g (>= 1:1.1.4)
Homepage: <insert the upstream URL, if relevant>
Priority: optional
Section: unknown
Filename: pool/main/m/mikrotikapiping/mikrotikapiping_2.0-0ubuntu1_amd64.deb
Size: 22406888
SHA256: 1d21f6f2221e0cfe07a569ec92cb9facd74e25af6dbab124400866ba599bd1a8
SHA1: c4c84b5a7c26ea38ad5d4f864ce21139fbfe199b
MD5sum: e4972e18c8bfbb8cab1fedd44c4e0ab6
Description: <insert up to 60 chars description>
 <insert long description, indented with spaces>



File: /dists\bionic\main\binary-amd64\Release
Component: main
Origin: MikrotikAPIPing Tool
Label: mikrotikapiping
Architecture: amd64
Description: Personal repository


File: /dists\bionic\Release
Origin: MikrotikAPIPing Tool
Label: mikrotikapiping
Codename: bionic
Date: Tue, 31 Dec 2019 21:32:58 UTC
Architectures: amd64
Components: main
Description: Personal repository
MD5Sum:
 a7ec7ab1e9f13991af2c0b1dea905cb2 734 main/binary-amd64/Packages
 826a016a9cc7eb8480b0a5e6a33d17d5 491 main/binary-amd64/Packages.gz
 7984536c85a82c478752372afdbfbf71 121 main/binary-amd64/Release
SHA1:
 c356f12e978cbcd2dc7c2e084153124be036e5b3 734 main/binary-amd64/Packages
 d51b79a1c09a16f9a67eec10ecce3f9cb020da4e 491 main/binary-amd64/Packages.gz
 b7a78e9bb83315bd68037908c23bd6894a5f1b03 121 main/binary-amd64/Release
SHA256:
 09d167a2e69b1e810642124473cd32133bfd183ce318adfceb1d3fd028235c27 734 main/binary-amd64/Packages
 2a4afe1ab291dd96c048a1d9ed1326249c2d97f89a98f83dd03bd5796280aba0 491 main/binary-amd64/Packages.gz
 8549d45e864dced320eae142f11cfce00069dc8e8fb840fa2a3af1efbd9c58f5 121 main/binary-amd64/Release


File: /dists\bionic\Release.gpg
-----BEGIN PGP SIGNATURE-----

iQGzBAABCgAdFiEE3pBXBuMqGutf8oPXF/GEgyS5wPQFAl4LvooACgkQF/GEgyS5
wPTDawv9EXZLt8AfL5rKJtzTd/6c/WQiZGf3LDQP9KRsDEhuSF5dP1jmQzIVbWsh
p6Vw86ZBwDFpx5V0FvRAhrr4weZ4f4GK20g1RjVCMoYlWymxvgGORuH7PjxSouMl
KeBv0dHnZkVCZz1OZ0XBqzfCJbxBd3B13fC06/O4n8vAJqDhwa1EoeakMk8R3f6T
k9y+lhPMaSdVrFPwcPWLOR/vYrNyf0tSYQYGuVerTSKh0wIybbR+YTahU2PjyS2D
mhMIaGw0PsZpwoLcma4QswaRcwBEoa5sCToibRDLOLAr2oePK72GXQh3T/37KEc2
76hBFg0mwL2h2TTGRmMYiA69/v5ujmKIaBeQ8CL+Tu8YD9Ta8AjnUFCTAuwV2+Go
dU6hmIIz4HHEalAZ+Zi6htTciozYMw+tv6SvaqMnDsRLUacMW01LapEuQeIZOQ6v
D3Jjj2T6i8zsmDvP4ZenruDgAv5G7IPF/GtskM6EFaNTgbPmKxt92L/UjMWpzrSf
9pZFCaWf
=huhZ
-----END PGP SIGNATURE-----


File: /PUBLIC.KEY
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
qQNMKdA0GtCGrI+BPbrTHW3s0S2d8y82uSXjs4uMgvdyFYBSl8EJxGbK8F3sS3EK
AzPlo/9G2pm+O74o6topc+nMYzmVw4XDfCK63zqr3fv4wyfm97KSVHPkK/Wn1rFc
Ki8fo+yhP30VSkl+NgAw7bIweSM7EWLsVMC6Qx44M/VkX1j6baxJIVx8kM23gJrz
9g2CxBtOw3RRBEaLNqcBcYm/wwOhCaiDntc/eHu7n94LgUwVjVnNDXzNOhcfkRZN
3zXVTa4/Lusn3WQcLU0Dncg66WPPcxcSO46KC/XCAIJW1T/+yxpBopon3HI5eQ20
336S4RNeUlsLE8cROS5EbzHENykXohNlT3CnbQmgg17Y+OfyEJM8dNNcujeeAKXs
JJcLx+m62UagGlP8iV9Po1oUx2CjiC16W3cCW5/CmQGNBF4LvfYBDACofRdMhrHN
0dl3fJCA4n5PIGIK9XAVRBGgDR0ctn2Q/RiTHYpqPu4BV3qAGo9WCwdb16hf5zub
UdSGEEmYXSRtIi6ZCNZ5/J2+A9VruCvj3Y3/hnwtvWq2wB5ja1tZlmOlPSsauwmb
oIf7K/gcZsPQdY17mYH7Ua/ZUjXBFOTl53nmWHai+EDVDeWIv6Pr4sK0dSSFlRFx
79RGSaThbLHWNT/k6rbABl51JF9/W/aArHvGzeyThE+TsPWaAEvLhFG9HEpwZ4Xv
WbEz6YsR4mDZ8XSGWTi2B8bJkV6lJqCXqg4yZ1o3Yri62L+ZrtjT2SuO1YnuTj9L
kL6nHyCHor+nJVtSO5qb/OtlSjeAO2C5XQ0RgaaeJXPQjT9SuEbSF/4xbCuSxNdx
48VEf63VlbFHrok437HMMkDcTbQbNXoEvikibhM4HJtaANE35YVxOB7dNVxJX31J
Kfpzf5ALFPk8HlQyd/jpWDkjWZIGBa82hHyoq8jIjPgeA+8dqZLAMg0AEQEAAbQt
TWlrcm90aWtBUElQaW5nIFRvb2wgPHYta29zeWVkQG1pY3Jvc29mdC5jb20+iQHU
BBMBCgA+FiEE3pBXBuMqGutf8oPXF/GEgyS5wPQFAl4LvfYCGwMFCQPCZwAFCwkI
BwIGFQoJCAsCBBYCAwECHgECF4AACgkQF/GEgyS5wPSM4Av7BbTJcdxe1ZP7Wf8j
FKNea/eL6XTuoBVII7CD9ndF0DVRMJR5dlgBHDbbW95MjPh95DOBOAvK7XM2GIPp
Nu6aWyYdYlnXWMnxtxIb5KCk1CaFBOaujD+oXFCwi0+7JqU7413Sx1w7Qi6sdBDu
jxMMaqEWhKWU0ytXKNfk6j+J4NzQP5T5nTT3pjR62e/SK3aYXBc071ZfwMAQ+O4z
3mUl7TeUgkjzJkj+6VyGrfJQzyMv7VobTleGoBCGdNeTedfAg6rPuqAJ+Z9EAeSx
VwlP1ff2c2Ec1vAk9Qsg6auDppexTmWcG1KPyrHyykvPMhsh226gfi/7uzaNKD3T
COWwYmeIV6g4zZHQRjo8Myj2UEkJx0ZVgpjEtV/ZjWBcSj5mXu/vTHaYpNtO0Po2
LYx/u7MRI75gHb5gR8SeXgZDrQ8BaElJIDVPcbxYc7UuiBY6jDLcxLvQwYZh7aaJ
xla0pdtgYv/TWeIpy50To6PycctVP15w2U0PmnvGKFM4qMsouQGNBF4LvfYBDADn
JjU6C8EE4j9vXN9cykVWTzhf339pJT4JHSgt7ZT0UgKgdskQP1nAIQo5j9xF3BDt
xzdpelZR7UhzsTxIah5L21HUZN/LJVtNN5eNgvcGFX1prsMDL0+2ynXF16KqQNeC
1fk/SirI0p3leFWS+GoNZfnr7O3ep90nxyU5CrZEyblBiBLVetQJTerGWUGU6Gn0
i7eIv4y3x56tD3Lky8qYBF4dsoZe0NhRwLZRwTv60AwyvWRAB4zkk9RlWBr0CGOb
Jq7/oQcjhKzY8xaFxqj4Krg3hMyBazppVslPMGKwYh/xe7S7HPZM/wlwiIfoDzBU
XGJv4pvFsMK4v7kI6R9D+1cl1YFMmDTz7DQyD7XTABqRNA9lTWLPIjOpMeY+YmSP
TkDHgwbX24ZkBni8LbEYFUWGPZuTGKUJznyWXhjr51P07ygRvV+dfVUexz5mmGGI
3hN9Oi0LUW0vxvvTS/rNeW7wGdgYPoCWv6PGKiFWJgeZ/YZSgS6AcPQxQIrtWHMA
EQEAAYkBvAQYAQoAJhYhBN6QVwbjKhrrX/KD1xfxhIMkucD0BQJeC732AhsMBQkD
wmcAAAoJEBfxhIMkucD0/5cL/jDr5n+z0hFWZwDsAqGAFL6JQqxne32fDvQE32Bq
Q1CxAKNi1dYBG5SkIN7shzOru1Wjq4E1fU4zmpZJ/9BeZ6kQoqXo+CIWLPMo9XB3
Jjt/uN3jaBQfRJ2JSxq3tavca/CDoG87jp/o1v2Ox6QRYNce2lmKUlPuYC/KsGH9
1m4kDCI+mYv9IFO//33gySAqjZMH4wxanf6YxzYRsqeLFYP1Aywym5fPmXYgTLnu
npLRcrac+G1bRjDJ9dLkkv+I1hWxNwG/njb837m//2ob5u6b1rLlvxA/Z7YEEZwy
ckJZ3tlCBb2bgM3OLbQVdjWEA11bDpZ48B0SOrVX7KnxaG+NsIDNqs/XSOeUJ7kx
f3YvUTAUGB6c26Tu4jKL8MezVst94cFRcbmayJGjvSuX1TPICppppISkyZbgMZL1
xMe5LkppjSFYwotnmpzq8A0GpvhVq07gNFjF0e9jVi3CkkxXG3HCvFsewZswjEar
/+Nrcry/14NiSLKe6TugjmddFQ==
=yMb9
-----END PGP PUBLIC KEY BLOCK-----


File: /README.md
# mikrotikapipingutilityapt
mikrotikrouterpingutiltiyapt 2.0 upload

In case you have an older version of the utility installed remove that by running the following command

<b>sudo apt-get remove mikrotikapiping</b></br>

Then run the following to install utility tool by running the following

$ wget -qO - https://raw.githubusercontent.com/komalashrafsyed/mikrotikapipingutilityapt/master/PUBLIC.KEY | sudo apt-key add - </br>
$ echo "deb https://raw.githubusercontent.com/komalashrafsyed/mikrotikapipingutilityapt/master bionic main" | sudo tee /etc/apt/sources.list.d/mikrotikapiping.list  </br>
$ sudo apt-get update </br>
$ sudo apt-get install mikrotikapiping </br>
$ export PING_HOME=/opt/ksyed/mikrotikapiping/MikrotikAPIPing.dll </br>

$ sudo dotnet $PING_HOME </br>

At this stage the Mikrotik Ping Utility is installed in your system ready to be used! </br>


