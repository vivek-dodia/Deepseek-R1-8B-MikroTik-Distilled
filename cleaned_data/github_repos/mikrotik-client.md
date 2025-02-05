# Repository Information
Name: mikrotik-client

# Directory Structure
Directory structure:
└── github_repos/mikrotik-client/
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
    │   │       ├── pack-115bacc0cda8df906db4ab95683c53021c9d713e.idx
    │   │       └── pack-115bacc0cda8df906db4ab95683c53021c9d713e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .travis.yml
    ├── Changes
    ├── lib/
    │   └── MikroTik/
    │       ├── Client/
    │       │   ├── Mo.pm
    │       │   ├── Query.pm
    │       │   ├── Response.pm
    │       │   └── Sentence.pm
    │       └── Client.pm
    ├── LICENSE
    ├── Makefile.PL
    ├── MANIFEST.SKIP
    ├── README.md
    └── t/
        ├── certs/
        │   ├── ca.crt
        │   ├── ca.key
        │   ├── client-bundle.crt
        │   ├── client.crt
        │   ├── client.key
        │   ├── server.crt
        │   └── server.key
        ├── lib/
        │   └── MikroTik/
        │       └── Client/
        │           └── Mockup.pm
        ├── mikrotik-online.t
        ├── mikrotik.t
        ├── pod.t
        ├── pod_coverage.t
        ├── promises.t
        ├── query.t
        ├── response.t
        ├── sentence.t
        └── tls.t


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
	url = https://github.com/anparker/mikrotik-client.git
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
0000000000000000000000000000000000000000 bf836ffcdb12120c1e8a7281a102c5d5a7f44e01 vivek-dodia <vivek.dodia@icloud.com> 1738606344 -0500	clone: from https://github.com/anparker/mikrotik-client.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 bf836ffcdb12120c1e8a7281a102c5d5a7f44e01 vivek-dodia <vivek.dodia@icloud.com> 1738606344 -0500	clone: from https://github.com/anparker/mikrotik-client.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 bf836ffcdb12120c1e8a7281a102c5d5a7f44e01 vivek-dodia <vivek.dodia@icloud.com> 1738606344 -0500	clone: from https://github.com/anparker/mikrotik-client.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
bfcb99f2ea9b562eb70e1d39db8d62ddb9e96710 refs/remotes/origin/evloop-ae
9d429692a0ca4362199f2af8064a751cf3c2e352 refs/remotes/origin/evloop-mojo
bf836ffcdb12120c1e8a7281a102c5d5a7f44e01 refs/remotes/origin/master
010cb1e27b94df5cdc4d4df0adeedacc89a3f00a refs/tags/v0.21
^53582ac2e4f4ab8fadac60f07448b4ad7c753970
979a883d658a25eae8fed04f48d4240421fcdc3b refs/tags/v0.22
^3faacded92b3566b3e9297f17c32bd534653b3c4
8d41c57f15ef6832fdcf61592522b2323f273bea refs/tags/v0.23
^e191a4cdd1a8fdea5bc0cc30793df6adf982c528
8f6dc56c82927f52bd7d0cb892bcb965563b6d7b refs/tags/v0.24
^fea28fb5850f122b9f8daaaf03c6f58ce419c1be
84a1d2184e830e8cdc93adef42d503669b2755d1 refs/tags/v0.31
^597d87817d37695ee6fa31e271caca06a65641ae
b2f8ee17a158b6571acc88b4282b70d27e8360e9 refs/tags/v0.520
^f7aa796282dbe5224e6cdd85e45f7a885ddae195


File: /.git\refs\heads\master
bf836ffcdb12120c1e8a7281a102c5d5a7f44e01


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/blib/
/.build/
_build/
cover_db/
inc/
Build
!Build/
Build.bat
.last_cover_stats
/Makefile
/Makefile.old
/MANIFEST.bak
/META.yml
/META.json
/MYMETA.*
nytprof.out
/pm_to_blib
*.o
*.bs
/_eumm/
*.swp
File: /.travis.yml
language: perl
matrix:
    include:
    - perl: "5.30"
    - perl: "5.28"
    - perl: "5.26"
    - perl: "5.24"
    - perl: "5.22"
    - perl: "5.20"
      dist: trusty
    - perl: "5.18"
      dist: trusty
    - perl: "5.16"
      dist: trusty
    - perl: "5.14"
      dist: trusty
    - perl: "5.12"
      dist: trusty
env:
  global:
    - HARNESS_OPTIONS=j4
    - TEST_POD=1
install:
  - cpanm -n Test::Pod Test::Pod::Coverage
  - cpanm -v -n --installdeps .
sudo: false
notifications:
  email: false


File: /Changes
v0.530
    - Fix handling of newlines in responses.
    - Update certificates for TLS tests.

v0.520
    - Add support for PKI certificates.
    - Fail remaining requests on errors.

v0.501
    - Fix connection tests.

v0.500
    - Moved to AnyEvent.

0.31
    - Adopt new namespase. I perfectly aware that's a foul practice, but
      initial name was a realy bad choice.
    - Allow new login scheme introduced in v6.43.

0.24    2018-02-14
    - Updates to a POD.
    - Reuse socket in a mockup object.

0.23    2018-02-12
    - CPAN release.


File: /lib\MikroTik\Client\Mo.pm
package MikroTik::Client::Mo;
# use Mo qw'default import';
#   The following line of code was produced from the previous line by
#   Mo::Inline version 0.40
no warnings;my$M=__PACKAGE__.'::';*{$M.Object::new}=sub{my$c=shift;my$s=bless{@_},$c;my%n=%{$c.'::'.':E'};map{$s->{$_}=$n{$_}->()if!exists$s->{$_}}keys%n;$s};*{$M.import}=sub{import warnings;$^H|=1538;my($P,%e,%o)=caller.'::';shift;eval"no Mo::$_",&{$M.$_.::e}($P,\%e,\%o,\@_)for@_;return if$e{M};%e=(extends,sub{eval"no $_[0]()";@{$P.ISA}=$_[0]},has,sub{my$n=shift;my$m=sub{$#_?do{$_[0]{$n}=$_[1];$_[0]}:$_[0]{$n}};@_=(default,@_)if!($#_%2);$m=$o{$_}->($m,$n,@_)for sort keys%o;*{$P.$n}=$m},%e,);*{$P.$_}=$e{$_}for keys%e;@{$P.ISA}=$M.Object};*{$M.'default::e'}=sub{my($P,$e,$o)=@_;$o->{default}=sub{my($m,$n,%a)=@_;exists$a{default}or return$m;my($d,$r)=$a{default};my$g='HASH'eq($r=ref$d)?sub{+{%$d}}:'ARRAY'eq$r?sub{[@$d]}:'CODE'eq$r?$d:sub{$d};my$i=exists$a{lazy}?$a{lazy}:!${$P.':N'};$i or ${$P.':E'}{$n}=$g and return$m;sub{$#_?$m->(@_):!exists$_[0]{$n}?$_[0]{$n}=$g->(@_):$m->(@_)}}};my$i=\&import;*{$M.import}=sub{(@_==2 and not$_[1])?pop@_:@_==1?push@_,grep!/import/,@f:();goto&$i};@f=qw[default import];use strict;use warnings;
1;

=encoding utf8

=head1 NAME

MikroTik::Client::Mo - Mo inlined

=head1 SYNOPSIS

  package MikroTik::Client::MyModule;
  use MikroTik::Client::Mo;

=head1 DESCRIPTION

Inlined version of L<Mo>. Will use C<default> feature automatically.

=head1 CAVEATS

Attributes behaviour changed in a way, that they will return an invocant
instead of value when called with an argument to allow chaining.

=cut


File: /lib\MikroTik\Client\Query.pm
package MikroTik::Client::Query;
use MikroTik::Client::Mo;

use Exporter 'import';
use Scalar::Util 'blessed';

our @EXPORT_OK = ('build_query');


sub build_query {
    my $query = blessed $_[0] ? $_[1] : $_[0];

    return $$query if ref $query eq 'REF' && ref $$query eq 'ARRAY';

    if (my $type = ref $query) {
        return [_block(_ref_op($type), $query)];
    }
    else { return [] }
}

sub _block {
    my ($logic, $items) = @_;

    @{($items = [])} = map { $_ => $items->{$_} } sort keys %$items
        if ref $items eq 'HASH';
    my ($count, @words) = (0, ());

    while (my $el = shift @$items) {

        my @expr;
        if (ref $el eq 'REF' && ref $$el eq 'ARRAY') {
            @expr = @{$$el};

        }
        elsif (my $type = ref $el) {
            @expr = _block(_ref_op($type), $el);

        }
        elsif ($el =~ /^-(?:and|or)$/) {
            @expr = _block(_ref_op($el), shift @$items);

        }
        elsif ($el =~ /^-has(?:_not)?$/) {
            push @words, '?' . ($el eq '-has_not' ? '-' : '') . (shift @$items);
            $count++;
            next;

        }
        else {
            @expr = _value($el, shift @$items);
        }

        ++$count && push @words, @expr if @expr;
    }

    push @words, '?#' . ($logic x ($count - 1)) if $count > 1;
    return @words;
}

sub _ref_op {
    return
          ($_[0] eq 'HASH'  || $_[0] eq '-and') ? '&'
        : ($_[0] eq 'ARRAY' || $_[0] eq '-or')  ? '|'
        :                                         '';
}

sub _value {
    my ($name, $val) = @_;

    my $type = ref $val;
    if ($type eq 'HASH') {
        return _value_hash($name, $val);

    }
    elsif ($type eq 'ARRAY') {
        return _value_array($name, '=', $val);
    }

    # SCALAR
    return "?$name=" . ($val // '');
}

sub _value_array {
    my ($name, $op, $block) = @_;

    return () unless @$block;

    my $logic = '|';
    $logic = _ref_op(shift @$block)
        if @$block[0] eq '-and' || @$block[0] eq '-or';

    my ($count, @words) = (0, ());
    for (@$block) {
        my @expr
            = ref $_ eq 'HASH'
            ? _value_hash($name, $_)
            : _value_scalar($name, $op, $_);

        ++$count && push @words, @expr if @expr;
    }

    push @words, '?#' . ($logic x ($count - 1)) if $count > 1;
    return @words;
}

sub _value_hash {
    my ($name, $block) = @_;

    my @words = ();

    for my $op (sort keys %$block) {
        my $val = $block->{$op};
        return _value_array($name, $op, $val) if ref $val eq 'ARRAY';
        push @words, _value_scalar($name, $op, $val);
    }

    my $count = keys %$block;
    push @words, '?#' . ('&' x ($count - 1)) if $count > 1;
    return @words;
}

sub _value_scalar {
    my ($name, $op, $val) = (shift, shift, shift // '');

    return ("?$name=$val", '?#!') if $op eq '-not';
    return '?' . $name . $op . $val;
}

1;


=encoding utf8

=head1 NAME

MikroTik::Client::Query - Build MikroTik queries from perl structures

=head1 SYNOPSIS

  use MikroTik::Client::Query qw(build_query);

  # (a = 1 OR a = 2) AND (b = 3 OR c = 4 OR d = 5)
  my $query = {
      a => [1, 2],
      [
        b => 3,
        c => 4,
        d => 5
      ]
  };


  # Some bizarre nested expressions.
  # (a = 1 OR b = 2 OR (e = 5 AND f = 6 AND g = 7))
  #   OR
  # (c = 3 AND d = 4)
  #   OR
  # (h = 8 AND i = 9)
  $query = [
      -or  => {
          a => 1,
          b => 2,
          -and => {e => 5, f => 6, g => 7}
      },

      # OR
      -and => [
          c => 3,
          d => 4
      ],

      # OR
      {h => 8, i => 9}
  ];

=head1 DESCRIPTION

Simple and supposedly intuitive way to build MikroTik API queries. Following
ideas of L<SQL::Abstract>.

=head1 METHODS

=head2 build_query

  use MikroTik::Client::Query qw(build_query);

  # (type = 'ipip-tunnel' OR type = 'gre-tunnel') AND running = 'true'
  # $query
  #     = ['?type=ipip-tunnel', '?type=gre-tunnel', '?#|', '?running=true', '?#&'];
  my $query
      = build_query({type => ['ipip-tunnel', 'gre-tunnel'], running => 'true'});

Builds a query and returns an arrayref with API query words.

=head1 QUERY SYNTAX

Basic idea is that everything in arrayrefs are C<OR>'ed and everything in hashrefs
are C<AND>'ed unless specified otherwise. Another thing is, where a C<value> is
expected, you should be able to use a list to compare against a set of values.

=head2 Key-value pairs

  # type = 'gre-tunnel' AND running = 'true'
  my $query = {type => 'gre-tunnel', running => 'true'};

  # disabled = 'true' OR running = 'false'
  $query = [disabled => 'true', running => 'false'];

Simple attribute value comparison.

=head2 List of values

  # type = 'ether' OR type = 'wlan'
  my $query = {type => ['ether', 'wlan']};

You can use arrayrefs for a list of possible values for an attribute. By default,
it will be expanded into an C<OR> statement.

=head2 Comparison operators

  # comment isn't empty (more than empty string)
  my $query = {comment => {'>', ''}};

  # mtu > 1000 AND mtu < 1500
  $query = {mtu => {'<' => 1500, '>' => 1000}};

Hashrefs can be used for specifying operator for comparison. Well, any of three
of them. :) You can put multiple operator-value pairs in one hashref and they
will be expanded into an C<AND> statement.

  # mtu < 1000 OR mtu > 1500
  $query = {mtu => [{'<', 1000}, {'>', 1500}]};

  # Or like this
  # mtu < 1000 OR (mtu > 1400 AND mtu < 1500)
  $query = {mtu => [{'<', 1000}, {'>', 1400, '<', 1500}]};

Hashrefs can be also put in lists. If you want them combined into an C<OR>
statement, for example.

  # status = 'active' OR status = 'inactive'
  $query = {mtu => {'=', ['active', 'inactive']}};

Or you can use list as a value in a hashref pair. B<CAVEAT>: In this case, every
other pair in the hash will be ignored.

=head2 Negation

  # !(interface = 'ether5')
  my $query = {interface => {-not => 'ether5'}};

  # !(interface = 'ether5') AND !(interface = 'ether1')
  $query = {interface => {-not => [-and => 'ether5', 'ether1']}};

Since MikroTik API does not have 'not equal' operator, it ends up been 'opposite
of a equals b' expressions.

=head2 Checking for an attribute

  my $query = {-has => 'dafault-name'};

  $query = {-has_not => 'dafault-name'};

Checks if an element has an attribute with specific name.

=head2 Literal queries

  my $query = \['?type=ether', '?running=true', '?actual-mtu=1500', '?#&&'];

  $query = [
      type => 'ipip-tunnel',
      \['?type=ether', '?running=true', '?actual-mtu=1500', '?#&&']
  ];

Reference to an arrayref can be used to pass list of prepared words. Those will
be treated as blocks in nested expressions.

=head2 Logic and nesting

  # (mtu = 1460 AND actual-mtu = 1460)
  #   AND
  # (running = 'false' OR disabled = 'true')

  my $query = {
      {mtu     => 1460,    'actual-mtu' => 1460},
      [running => 'false', disabled     => 'true']
  };

Conditions can be grouped and nested if needed. It's like putting brackets around
them.

  # Same thing, but with prefixes
  my $query = {
      -and => [mtu     => 1460,    'actual-mtu' => 1460],
      -or  => {running => 'false', disabled     => 'true'}
  };

You can change logic applied to a block by using keywords. Those keywords
will go outside for blocks that affect multiple attributes, or ...

  # !(type = 'ether') AND !(type = 'wlan')

  # Will produce the same result
  my $query = {type => [-and => {-not => 'ether'}, {-not => 'wlan'}]};
  $query = {type => {-not => [-and => 'ether', 'wlan']}};

  # Wrong, second condition will replace first
  $query = {type => {-not => 'ether', -not => 'wlan'}};

... inside for a list of values of a single attribute.

  # This is wrong
  my $query = [
    -and =>
      {type => 'ether'},
      {running => 'true'}
  ];

  # It will actually results in
  # type = 'ether' OR running = 'true'

C<-and> will be treated as prefix for the first hashref and, since this hash has
only one element, won't affect anything at all.

=cut



File: /lib\MikroTik\Client\Response.pm
package MikroTik::Client::Response;
use MikroTik::Client::Mo;

use MikroTik::Client::Sentence;

has data     => [];
has sentence => sub { MikroTik::Client::Sentence->new() };

sub parse {
    my ($self, $buf) = @_;

    my $data = [];

    my $sentence = $self->sentence;
    while ($$buf) {
        my $words = $sentence->fetch($buf);
        last if $sentence->is_incomplete;

        my $item = {'.tag' => '', '.type' => (shift @$words)};
        push @$data, $item;

        next unless @$words;

        while (my $w = shift @$words) {
            $item->{$1 || $2} = $3 if ($w =~ /^(?:=([^=]+)|(\.tag))=(.*)/s);
        }
    }

    return $self->{data} = $data;
}

1;

=encoding utf8

=head1 NAME

MikroTik::Client::Response - Parse responses from a buffer

=head1 SYNOPSIS

  use MikroTik::Client::Response;

  my $response = MikroTik::Client::Response->new();

  my $list = $response->parse(\$buf);
  for my $re (@$list) {
      my ($type, $tag) = delete @{$re}{'.type'. '.tag'};
      say "$_ => $re->{$_}" for keys %$re;
  }

=head1 DESCRIPTION

Parser for API protocol responses.

=head1 ATTRIBUTES

L<MikroTik::Client::Response> implements the following attributes.

=head2 data

  my $items = $response->data;

Sentences fetched in last operation;

=head2 sentence

  my $sentence = $response->sentence;
  $response->sentence(MikroTik::Client::Sentence->new());

L<MikroTik::Client::Sentence> object used to decode sentences from network buffer.

=head1 METHODS

=head2 parse

  my $list = $response->parse(\$buf);

Parses data from a buffer and returns list of hashrefs with attributes for each
sentence. There are some special attributes:

=over 2

=item '.tag'

  '.tag' => 1

Reply tag.

=item '.type'

  '.type' => '!re'

Reply type.

=back

=head1 SEE ALSO

L<MikroTik::Client>

=cut


File: /lib\MikroTik\Client\Sentence.pm
package MikroTik::Client::Sentence;
use MikroTik::Client::Mo;

use Exporter 'import';
our @EXPORT_OK = qw(encode_sentence);

use MikroTik::Client::Query 'build_query';

has words => [];

sub encode_sentence {
    shift if ref $_[0];
    my ($command, $attr, $query, $tag)
        = (shift // '', shift // {}, shift, shift);

    my $sentence = _encode_word($command);

    $sentence .= _encode_word("=$_=" . ($attr->{$_} // '')) for keys %$attr;

    if ($query) {
        $sentence .= _encode_word($_) for @{build_query($query)};
    }

    $sentence .= _encode_word(".tag=$tag") if $tag;

    # Closing empty word.
    $sentence .= "\x00";

    return $sentence;
}

sub fetch {
    my ($self, $buf) = @_;

    my $words = $self->is_incomplete ? $self->words : ($self->{words} = []);

    while (my $w = $self->_fetch_word($buf)) { push @$words, $w }
    return $words;
}

sub is_incomplete {
    return exists $_[0]->{expecting_bytes} || exists $_[0]->{partial};
}

sub reset {
    delete @{$_[0]}{qw(words expecting_bytes partial)};
    return $_[0];
}

sub _encode_length {
    my $len = shift;

    my $packed;

    # Screw you, mikrotik engineers, just pack length as 4 bytes. >_<
    if ($len < 0x80) {
        $packed = pack 'C', $len;
    }
    elsif ($len < 0x4000) {
        $packed = pack 'n', ($len | 0x8000) & 0xffff;
    }
    elsif ($len < 0x200000) {
        $len |= 0xc00000;
        $packed = pack 'Cn', (($len >> 16) & 0xff), ($len & 0xffff);
    }
    elsif ($len < 0x10000000) {
        $packed = pack 'N', ($len | 0xe0000000);
    }
    else {
        $packed = pack 'CN', 0xf0, $len;
    }

    return $packed;
}

sub _encode_word {
    return _encode_length(length($_[0])) . $_[0];
}

sub _fetch_word {
    my ($self, $buf) = @_;

    return $self->{expecting_bytes} = 0 unless my $buf_bytes = length $$buf;
    if ($buf_bytes < 5 && $$buf ne "\x00") { $self->{partial} = 1; return '' }

    my $len
        = delete $self->{partial}
        ? _strip_length($buf)
        : delete $self->{expecting_bytes} // _strip_length($buf);
    if (length $$buf < $len) { $self->{expecting_bytes} = $len; return '' }

    return substr $$buf, 0, $len, '';
}

sub _strip_length {
    my $buf = shift;

    my $len = unpack 'C', substr $$buf, 0, 1, '';

    if (($len & 0x80) == 0x00) {
        return $len;
    }
    elsif (($len & 0xc0) == 0x80) {
        $len &= ~0x80;
        $len <<= 8;
        $len += unpack 'C', substr $$buf, 0, 1, '';
    }
    elsif (($len & 0xe0) == 0xc0) {
        $len &= ~0xc0;
        $len <<= 16;
        $len += unpack 'n', substr $$buf, 0, 2, '';
    }
    elsif (($len & 0xf0) == 0xe0) {
        $len = unpack 'N', pack('C', ($len & ~0xe0)) . substr($$buf, 0, 3, '');
    }
    elsif (($len & 0xf8) == 0xf0) {
        $len = unpack 'N', substr $$buf, 0, 4, '';
    }

    return $len;
}

1;

=encoding utf8

=head1 NAME

MikroTik::Client::Sentence - Encode and decode API sentences

=head1 SYNOPSIS

  use MikroTik::Client::Sentence qw(encode_sentence);

  my $command = '/interface/print';
  my $attr    = {'.proplist' => '.id,name,type'};
  my $query   = {type => ['ipip-tunnel', 'gre-tunnel'], running => 'true'};
  my $tag     = 1;

  my $bytes = encode_sentence($command, $attr, $query, $tag);

  my $sentence = MikroTik::Client::Sentence->new();
  my $words = $sentence->fetch(\$bytes);
  say $_ for @$words;

=head1 DESCRIPTION

Provides subroutines for encoding API sentences and parsing them back into words.

=head1 METHODS

=head2 encode_sentence

  my $bytes = encode_sentence($command, $attr, $query, $tag);

Encodes sentence. Attributes is a hashref with attribute-value pairs. Query will
be parsed with L<MikroTik::Client::Query/build_query>.

Can be also called as an object method.

=head2 fetch

  my $words = $sentence->fetch(\$buf);

Fetches a sentence from a buffer and parses it into a list of API words. It
will return empty list and set L</is_incomplete> flag if amount of data in
a buffer is unsufficient for parsing full sentence.

=head2 is_incomplete

  my $done = !$sentence->is_incomplete;

Indicates that a processed buffer was incomplete and remaining amount of data was
insufficient to complete a sentence.

=head2 reset

  my $sentence->reset;

Clears an incomplete status and removes data from previous L</fetch> call.

=head1 SEE ALSO

L<MikroTik::Client>

=cut



File: /lib\MikroTik\Client.pm
package MikroTik::Client;
use MikroTik::Client::Mo;

use AnyEvent;
use AnyEvent::Handle;
use Digest::MD5 'md5_hex';
use MikroTik::Client::Response;
use MikroTik::Client::Sentence 'encode_sentence';
use Carp ();
use Scalar::Util 'weaken';

use constant CONN_TIMEOUT => $ENV{MIKROTIK_CLIENT_CONNTIMEOUT};
use constant DEBUG        => $ENV{MIKROTIK_CLIENT_DEBUG} || 0;
use constant PROMISES     => !!(eval { require Promises; 1 });

our $VERSION = "v0.540";

has ca   => sub { $ENV{MIKROTIK_CLIENT_CA} };
has cert => sub { $ENV{MIKROTIK_CLIENT_CERT} };
has error     => '';
has host      => '192.168.88.1';
has insecure  => 0;
has key       => sub { $ENV{MIKROTIK_CLIENT_KEY} };
has new_login => sub { $_[0]->tls || 0 };
has password  => '';
has port      => 0;
has timeout   => 10;
has tls       => 1;
has user      => 'admin';
has _tag      => 0;

# Aliases
{
    no strict 'refs';
    *{__PACKAGE__ . "::cmd"}   = \&command;
    *{__PACKAGE__ . "::cmd_p"} = \&command_p;
    *{__PACKAGE__ . "::_fail"} = \&_finish;
}

sub DESTROY {
    (defined ${^GLOBAL_PHASE} && ${^GLOBAL_PHASE} eq 'DESTRUCT')
        or shift->_cleanup();
}

sub cancel {
    my $cb = ref $_[-1] eq 'CODE' ? pop : sub { };
    return shift->_command('/cancel', {'tag' => shift}, undef, $cb);
}

sub command {
    my $cb = ref $_[-1] eq 'CODE' ? pop : undef;
    my ($self, $cmd, $attr, $query) = @_;

    # non-blocking
    return $self->_command($cmd, $attr, $query, $cb) if $cb;

    # blocking
    my $cv = AnyEvent->condvar;
    $self->_command($cmd, $attr, $query, sub { $cv->send($_[2]) });
    return $cv->recv;
}

sub command_p {
    Carp::croak 'Promises 0.99+ is required for this functionality.'
        unless PROMISES;
    my ($self, $cmd, $attr, $query) = @_;

    my $d = Promises::deferred();
    $self->_command($cmd, $attr, $query,
        sub { $_[1] ? $d->reject(@_[1, 2]) : $d->resolve($_[2]) });

    return $d->promise;
}

sub subscribe {
    do { $_[0]->{error} = 'can\'t subscribe in blocking mode'; return; }
        unless ref $_[-1] eq 'CODE';
    my $cb = pop;
    my ($self, $cmd, $attr, $query) = @_;
    $attr->{'.subscription'} = 1;
    return $self->_command($cmd, $attr, $query, $cb);
}

sub _cleanup {
    my $self = shift;
    delete $_->{timeout} for values %{$self->{requests}};
    delete $self->{handle};
}

sub _close {
    my ($self, $err) = @_;
    $self->_fail_all($err || 'closed prematurely');
    delete @{$self}{qw(handle response requests)};
}

sub _command {
    my ($self, $cmd, $attr, $query, $cb) = @_;

    my $tag = ++$self->{_tag};
    my $r = $self->{requests}{$tag} = {tag => $tag, cb => $cb};
    $r->{subscription} = delete $attr->{'.subscription'};

    warn "-- got request for command '$cmd' (tag: $tag)\n" if DEBUG;

    $r->{sentence} = encode_sentence($cmd, $attr, $query, $tag);
    return $self->_send_request($r);
}

sub _connect {
    my ($self, $r) = @_;

    warn "-- creating new connection\n" if DEBUG;

    my $queue = $self->{queue} = [$r];

    my $tls = $self->tls;
    my $port = $self->port ? $self->{port} : $tls ? 8729 : 8728;

    my $tls_opts = {verify => !$self->insecure, cipher_list => "HIGH"};
    $self->{$_} && ($tls_opts->{$_ . "_file"} = $self->{$_})
        for qw(ca cert key);

    weaken $self;
    $self->{handle} = AnyEvent::Handle->new(
        connect => [$self->host, $port],
        timeout => 60,

        $tls ? (tls => "connect", tls_ctx => $tls_opts) : (),

        on_connect => sub {
            warn "-- connection established\n" if DEBUG;

            delete $self->{queue};

            $self->_login(sub {
                return $self->_close($_[1]) if $_[1];
                $self->_write_sentence($_) for @$queue;
            });
        },

        on_connect_error => sub {
            delete @{$self}{qw(handle queue)};
            $self->_close($_[1]);
        },

        on_eof   => sub { $self && $self->_close },
        on_error => sub { $self && $self->_close($_[2]) },
        on_read    => sub { $self->_read(\$_[0]->{rbuf}) },
        on_prepare => sub {CONN_TIMEOUT},
        on_timeout => sub { $self && $self->_close }
    );

    return $r->{tag};
}

sub _enqueue {
    my ($self, $r) = @_;
    return $self->_connect($r) unless my $queue = $self->{queue};
    push @$queue, $r;
    return $r->{tag};
}

sub _fail_all {
    my @requests = values %{$_[0]->{requests}};
    $_[0]->_fail($_, $_[1]) for @requests;
}

sub _finish {
    my ($self, $r, $err) = @_;
    delete $self->{requests}{$r->{tag}};
    delete $r->{timeout};
    $r->{cb}->($self, ($self->{error} = $err // ''), $r->{data});
}

sub _login {
    my ($self, $cb) = @_;
    warn "-- trying to log in\n" if DEBUG;

    $self->_command(
        '/login',
        (
            $self->new_login
            ? {name => $self->user, password => $self->password}
            : {}
        ),
        undef,
        sub {
            my ($self, $err, $res) = @_;
            return $self->$cb($err) if $err;
            return $self->$cb() if !$res->[0]{ret};    # New style login

            my $secret
                = md5_hex("\x00", $self->password, pack 'H*', $res->[0]{ret});

            $self->_command('/login',
                {name => $self->user, response => "00$secret"},
                undef, $cb);
        }
    );
}

sub _read {
    my ($self, $buf) = @_;

    warn _term_esc("-- read buffer (" . length($$buf) . " bytes)\n$$buf\n")
        if DEBUG;

    my $response = $self->{response} ||= MikroTik::Client::Response->new();
    my $data = $response->parse($buf);

    for (@$data) {
        next unless my $r = $self->{requests}{delete $_->{'.tag'}};
        my $type = delete $_->{'.type'};
        push @{$r->{data} ||= []}, $_ if %$_ && !$r->{subscription};

        if ($type eq '!re' && $r->{subscription}) {
            $r->{cb}->($self, '', $_);

        }
        elsif ($type eq '!done') {
            $r->{data} ||= [];
            $self->_finish($r);

        }
        elsif ($type eq '!trap' || $type eq '!fatal') {
            $self->_fail($r, $_->{message});
        }
    }
}

sub _send_request {
    my ($self, $r) = @_;
    return $self->_enqueue($r) unless $self->{handle};
    return $self->_write_sentence($r);
}

sub _term_esc {
    my $str = shift;
    $str =~ s/([\x00-\x09\x0b-\x1f\x7f\x80-\x9f])/sprintf '\\x%02x', ord $1/ge;
    return $str;
}

sub _write_sentence {
    my ($self, $r) = @_;
    warn _term_esc("-- writing sentence for tag: $r->{tag}\n$r->{sentence}\n")
        if DEBUG;

    $self->{handle}->push_write($r->{sentence});

    return $r->{tag} if $r->{subscription};

    weaken $self;
    $r->{timeout} = AnyEvent->timer(
        after => $self->timeout,
        cb    => sub { $self->_fail($r, 'response timeout') }
    );

    return $r->{tag};
}

1;

=encoding utf8

=head1 NAME

MikroTik::Client - Non-blocking interface to MikroTik API

=head1 SYNOPSIS

  my $api = MikroTik::Client->new();

  # Blocking
  my $list = $api->command(
      '/interface/print',
      {'.proplist' => '.id,name,type'},
      {type        => ['ipip-tunnel', 'gre-tunnel'], running => 'true'}
  );
  if (my $err = $api->error) { die "$err\n" }
  printf "%s: %s\n", $_->{name}, $_->{type} for @$list;


  # Non-blocking
  my $cv  = AE::cv;
  my $tag = $api->command(
      '/system/resource/print',
      {'.proplist' => 'board-name,version,uptime'} => sub {
          my ($api, $err, $list) = @_;
          ...;
          $cv->send;
      }
  );
  $cv->recv;

  # Subscribe
  $tag = $api->subscribe(
      '/interface/listen' => sub {
          my ($api, $err, $el) = @_;
          ...;
      }
  );
  AE::timer 3, 0, cb => sub { $api->cancel($tag) };

  # Errors handling
  $api->command(
      '/random/command' => sub {
          my ($api, $err, $list) = @_;

          if ($err) {
              warn "Error: $err, category: " . $list->[0]{category};
              return;
          }

          ...;
      }
  );
 
  # Promises
  $cv  = AE::cv;
  $api->cmd_p('/interface/print')
      ->then(sub { my $res = shift }, sub { my ($err, $attr) = @_ })
      ->finally($cv);
  $cv->recv;

=head1 DESCRIPTION

Both blocking and non-blocking (don't mix them though) interface to a MikroTik
API service. With queries, command subscriptions and optional Promises.

=head1 ATTRIBUTES

L<MikroTik::Client> implements the following attributes.

=head2 ca

    my $ca = $api->ca;
    $api->ca("/etc/ssl/certs/ca-bundle.crt")

Path to TLS certificate authority file used to verify the peer certificate,
defaults to the value of the C<MIKROTIK_CLIENT_CA> environment variable.

=head2 cert

    my $cert = $api->cert;
    $api->cert("./client.crt")

Path to TLS certificate file used to authenticate against the peer. Can be bundled
with a private key and additional signing certificates. If file contains the private key,
L<key> attribute is optional. Defaults to the value of the C<MIKROTIK_CLIENT_CERT>
environment variable.

=head2 error

  my $last_error = $api->error;

Keeps an error from last L</command> call. Empty string on successful commands.

=head2 host

  my $host = $api->host;
  $api     = $api->host('border-gw.local');

Host name or IP address to connect to. Defaults to C<192.168.88.1>.

=head2 insecure

  my $insecure = $api->insecure;
  $api->insecure(1);

Do not verify TLS certificates I<(highly discouraged)>. Connection will be encrypted,
but a peer certificate won't be validated. Disabled by default.

=head2 key

    my $key = $api->key;
    $api->key("./client.crt")

Path to TLS key file. Optional if a private key bundled with a L<cert> file. Defaults to
the value of the C<MIKROTIK_CLIENT_KEY> environment variable.

=head2 new_login

  my $new_login = $api->new_login;
  $api          = $api->new_login(1);

Use new login scheme introduced in RouterOS C<v6.43> and fallback to previous
one for older systems. Since in this mode a password will be send in clear text,
it will be default only for L</tls> connections.

=head2 password

  my $pass = $api->password;
  $api     = $api->password('secret');

Password for authentication. Empty string by default.

=head2 port

  my $port = $api->port;
  $api     = $api->port(8000);

API service port for connection. Defaults to C<8729> and C<8728> for TLS and
clear text connections respectively.

=head2 timeout

  my $timeout = $api->timeout;
  $api        = $api->timeout(15);

Timeout in seconds for sending request and receiving response before command
will be canceled. Default is C<10> seconds.

=head2 tls

  my $tls = $api->tls;
  $api    = $api->tls(1);

Use TLS for connection. Enabled by default.

=head2 user

  my $user = $api->user;
  $api     = $api->user('admin');

User name for authentication purposes. Defaults to C<admin>.

=head1 METHODS

=head2 cancel

  # subscribe to a command output
  my $tag = $api->subscribe('/ping', {address => '127.0.0.1'} => sub {...});

  # cancel command after 10 seconds
  my $t = AE::timer 10, 0, sub { $api->cancel($tag) };

  # or with callback
  $api->cancel($tag => sub {...});

Cancels background commands. Can accept a callback as last argument.

=head2 cmd

  my $list = $api->cmd('/interface/print');

An alias for L</command>.

=head2 cmd_p

  my $promise = $api->cmd_p('/interface/print');

An alias for L</command_p>.

=head2 command

  my $command = '/interface/print';
  my $attr    = {'.proplist' => '.id,name,type'};
  my $query   = {type => ['ipip-tunnel', 'gre-tunnel'], running => 'true'};

  my $list = $api->command($command, $attr, $query);
  die $api->error if $api->error;
  for (@$list) {...}

  $api->command('/user/set', {'.id' => 'admin', comment => 'System admin'});

  # Non-blocking
  $api->command('/ip/address/print' => sub {
      my ($api, $err, $list) = @_;

      return if $err;

      for (@$list) {...}
  });

  # Omit attributes
  $api->command('/user/print', undef, {name => 'admin'} => sub {...});

  # Errors handling
  $list = $api->command('/random/command');
  if (my $err = $api->error) {
      die "Error: $err, category: " . $list->[0]{category};
  }

Executes a command on a remote host and returns list with hashrefs containing
elements returned by a host. You can append a callback for non-blocking calls.

In a case of error, returned value may keep additional attributes such as category
or an error code. You should never rely on defines of the result to catch errors.

For a query syntax refer to L<MikroTik::Client::Query>.

=head2 command_p

  my $promise = $api->command_p('/interface/print');

  $promise->then(
  sub {
      my $res = shift;
      ...
  })->catch(sub {
      my ($err, $attr) = @_;
  });

Same as L</command>, but always performs requests non-blocking and returns a
promise instead of accepting a callback. L<Promises> v0.99+ is required for
this functionality.

=head2 subscribe

  my $tag = $api->subscribe('/ping',
      {address => '127.0.0.1'} => sub {
        my ($api, $err, $res) = @_;
      });

  AE::timer 3, 0, sub { $api->cancel($tag) };

Subscribe to an output of commands with continuous responses such as C<listen> or
C<ping>. Should be terminated with L</cancel>.

=head1 DEBUGGING

You can set the MIKROTIK_CLIENT_DEBUG environment variable to get some debug output
printed to stderr.

Also, you can change connection timeout with the MIKROTIK_CLIENT_CONNTIMEOUT variable.

=head1 COPYRIGHT AND LICENSE

Andre Parker, 2017-2019.

This program is free software, you can redistribute it and/or modify it under
the terms of the Artistic License version 2.0.

=head1 SEE ALSO

L<https://wiki.mikrotik.com/wiki/Manual:API>, L<https://github.com/anparker/api-mikrotik>

=cut


File: /LICENSE
                       The Artistic License 2.0

            Copyright (c) 2000-2006, The Perl Foundation.

     Everyone is permitted to copy and distribute verbatim copies
      of this license document, but changing it is not allowed.

Preamble

This license establishes the terms under which a given free software
Package may be copied, modified, distributed, and/or redistributed.
The intent is that the Copyright Holder maintains some artistic
control over the development of that Package while still keeping the
Package available as open source and free software.

You are always permitted to make arrangements wholly outside of this
license directly with the Copyright Holder of a given Package.  If the
terms of this license do not permit the full use that you propose to
make of the Package, you should contact the Copyright Holder and seek
a different licensing arrangement.

Definitions

    "Copyright Holder" means the individual(s) or organization(s)
    named in the copyright notice for the entire Package.

    "Contributor" means any party that has contributed code or other
    material to the Package, in accordance with the Copyright Holder's
    procedures.

    "You" and "your" means any person who would like to copy,
    distribute, or modify the Package.

    "Package" means the collection of files distributed by the
    Copyright Holder, and derivatives of that collection and/or of
    those files. A given Package may consist of either the Standard
    Version, or a Modified Version.

    "Distribute" means providing a copy of the Package or making it
    accessible to anyone else, or in the case of a company or
    organization, to others outside of your company or organization.

    "Distributor Fee" means any fee that you charge for Distributing
    this Package or providing support for this Package to another
    party.  It does not mean licensing fees.

    "Standard Version" refers to the Package if it has not been
    modified, or has been modified only in ways explicitly requested
    by the Copyright Holder.

    "Modified Version" means the Package, if it has been changed, and
    such changes were not explicitly requested by the Copyright
    Holder.

    "Original License" means this Artistic License as Distributed with
    the Standard Version of the Package, in its current version or as
    it may be modified by The Perl Foundation in the future.

    "Source" form means the source code, documentation source, and
    configuration files for the Package.

    "Compiled" form means the compiled bytecode, object code, binary,
    or any other form resulting from mechanical transformation or
    translation of the Source form.


Permission for Use and Modification Without Distribution

(1)  You are permitted to use the Standard Version and create and use
Modified Versions for any purpose without restriction, provided that
you do not Distribute the Modified Version.


Permissions for Redistribution of the Standard Version

(2)  You may Distribute verbatim copies of the Source form of the
Standard Version of this Package in any medium without restriction,
either gratis or for a Distributor Fee, provided that you duplicate
all of the original copyright notices and associated disclaimers.  At
your discretion, such verbatim copies may or may not include a
Compiled form of the Package.

(3)  You may apply any bug fixes, portability changes, and other
modifications made available from the Copyright Holder.  The resulting
Package will still be considered the Standard Version, and as such
will be subject to the Original License.


Distribution of Modified Versions of the Package as Source

(4)  You may Distribute your Modified Version as Source (either gratis
or for a Distributor Fee, and with or without a Compiled form of the
Modified Version) provided that you clearly document how it differs
from the Standard Version, including, but not limited to, documenting
any non-standard features, executables, or modules, and provided that
you do at least ONE of the following:

    (a)  make the Modified Version available to the Copyright Holder
    of the Standard Version, under the Original License, so that the
    Copyright Holder may include your modifications in the Standard
    Version.

    (b)  ensure that installation of your Modified Version does not
    prevent the user installing or running the Standard Version. In
    addition, the Modified Version must bear a name that is different
    from the name of the Standard Version.

    (c)  allow anyone who receives a copy of the Modified Version to
    make the Source form of the Modified Version available to others
    under

        (i)  the Original License or

        (ii)  a license that permits the licensee to freely copy,
        modify and redistribute the Modified Version using the same
        licensing terms that apply to the copy that the licensee
        received, and requires that the Source form of the Modified
        Version, and of any works derived from it, be made freely
        available in that license fees are prohibited but Distributor
        Fees are allowed.


Distribution of Compiled Forms of the Standard Version
or Modified Versions without the Source

(5)  You may Distribute Compiled forms of the Standard Version without
the Source, provided that you include complete instructions on how to
get the Source of the Standard Version.  Such instructions must be
valid at the time of your distribution.  If these instructions, at any
time while you are carrying out such distribution, become invalid, you
must provide new instructions on demand or cease further distribution.
If you provide valid instructions or cease distribution within thirty
days after you become aware that the instructions are invalid, then
you do not forfeit any of your rights under this license.

(6)  You may Distribute a Modified Version in Compiled form without
the Source, provided that you comply with Section 4 with respect to
the Source of the Modified Version.


Aggregating or Linking the Package

(7)  You may aggregate the Package (either the Standard Version or
Modified Version) with other packages and Distribute the resulting
aggregation provided that you do not charge a licensing fee for the
Package.  Distributor Fees are permitted, and licensing fees for other
components in the aggregation are permitted. The terms of this license
apply to the use and Distribution of the Standard or Modified Versions
as included in the aggregation.

(8) You are permitted to link Modified and Standard Versions with
other works, to embed the Package in a larger work of your own, or to
build stand-alone binary or bytecode versions of applications that
include the Package, and Distribute the result without restriction,
provided the result does not expose a direct interface to the Package.


Items That are Not Considered Part of a Modified Version

(9) Works (including, but not limited to, modules and scripts) that
merely extend or make use of the Package, do not, by themselves, cause
the Package to be a Modified Version.  In addition, such works are not
considered parts of the Package itself, and are not subject to the
terms of this license.


General Provisions

(10)  Any use, modification, and distribution of the Standard or
Modified Versions is governed by this Artistic License. By using,
modifying or distributing the Package, you accept this license. Do not
use, modify, or distribute the Package, if you do not accept this
license.

(11)  If your Modified Version has been derived from a Modified
Version made by someone other than you, you are nevertheless required
to ensure that your Modified Version complies with the requirements of
this license.

(12)  This license does not grant you the right to use any trademark,
service mark, tradename, or logo of the Copyright Holder.

(13)  This license includes the non-exclusive, worldwide,
free-of-charge patent license to make, have made, use, offer to sell,
sell, import and otherwise transfer the Package with respect to any
patent claims licensable by the Copyright Holder that are necessarily
infringed by the Package. If you institute patent litigation
(including a cross-claim or counterclaim) against any party alleging
that the Package constitutes direct or contributory patent
infringement, then this Artistic License to you shall terminate on the
date that such litigation is filed.

(14)  Disclaimer of Warranty:
THE PACKAGE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS
IS" AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES. THE IMPLIED
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR
NON-INFRINGEMENT ARE DISCLAIMED TO THE EXTENT PERMITTED BY YOUR LOCAL
LAW. UNLESS REQUIRED BY LAW, NO COPYRIGHT HOLDER OR CONTRIBUTOR WILL
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES ARISING IN ANY WAY OUT OF THE USE OF THE PACKAGE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


File: /Makefile.PL
use strict;
use warnings;

use ExtUtils::MakeMaker;

WriteMakefile(
    NAME         => 'MikroTik::Client',
    VERSION_FROM => 'lib/MikroTik/Client.pm',
    ABSTRACT     => 'Non-blocking MikroTik API client',
    AUTHOR       => 'Andre Parker <andreparker@gmail.com>',
    LICENSE      => 'artistic_2',
    META_MERGE   => {
        dynamic_config => 0,
        'meta-spec'    => {version => 2},
        no_index       => {directory => ['t']},
        prereqs        => {runtime => {requires => {perl => '5.012000'}}},
        resources      => {
            bugtracker =>
                {web => 'https://github.com/anparker/mikrotik-client/issues'},
            license =>
                ['http://www.opensource.org/licenses/artistic-license-2.0'],
            repository => {
                type => 'git',
                url  => 'https://github.com/anparker/mikrotik-client.git',
                web  => 'https://github.com/anparker/mikrotik-client',
            },
        },
    },
    PREREQ_PM => {'AnyEvent' => '7.00'},
    test      => {TESTS      => 't/*.t'},
);



File: /MANIFEST.SKIP
^\.(?!perltidyrc)
.*\.old$
\.tar\.gz$
^Makefile$
^MYMETA\.
^blib
^pm_to_blib
File: /README.md
# MikroTik::Client - Non-blocking interface to MikroTik API. [![Build Status](https://travis-ci.com/anparker/mikrotik-client.svg?branch=master)](https://travis-ci.com/anparker/mikrotik-client)

Blocking and non-blocking API interface with queries, command subscriptions
and Promises/A.

```perl
  my $api = MikroTik::Client->new();

  # Blocking
  my $list = $api->command(
      '/interface/print',
      {'.proplist' => '.id,name,type'},
      {type        => ['ipip-tunnel', 'gre-tunnel'], running => 'true'}
  );
  if (my $err = $api->error) { die "$err\n" }
  printf "%s: %s\n", $_->{name}, $_->{type} for @$list;


  # Non-blocking
  my $cv = AE::cv;
  my $tag = $api->command(
      '/system/resource/print',
      {'.proplist' => 'board-name,version,uptime'} => sub {
          my ($api, $err, $list) = @_;
          ...;
          $cv->send;
      }
  );
  $cv->recv;

  # Subscribe
  $tag = $api->subscribe(
      '/interface/listen' => sub {
          my ($api, $err, $res) = @_;
          ...;
      }
  );
  my $t = AE::timer 3, 0, sub { $api->cancel($tag) };

  # Errors handling
  $api->command(
      '/random/command' => sub {
          my ($api, $err, $list) = @_;

          if ($err) {
              warn "Error: $err, category: " . $list->[0]{category};
              return;
          }

          ...;
      }
  );

  # Promises
  $cv  = AE::cv;
  $api->cmd_p('/interface/print')
      ->then(sub { my $res = shift }, sub { my ($err, $attr) = @_ })
      ->finally($cv);
  $cv->recv;
```


File: /t\certs\ca.crt
-----BEGIN CERTIFICATE-----
MIIFFTCCAv2gAwIBAgIUI53QHYwBOiZeyvjaB+esBdg/1bAwDQYJKoZIhvcNAQEL
BQAwGjELMAkGA1UEBhMCVVMxCzAJBgNVBAMMAmNhMB4XDTIxMDUwNjEzMjAzMloX
DTQxMDUwMTEzMjAzMlowGjELMAkGA1UEBhMCVVMxCzAJBgNVBAMMAmNhMIICIjAN
BgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA6YLHJMVSHOry46falwjc4tFRMXuG
ayQ2ev76neLcWqdQyWtSpChjkSlAY2NUBOxuKxuXmEokApoExJEeFXQ3u2Ce+6AT
mQry2sYRZalMnntQa/HNkya+UcBeFZf+TIm3g2uVgCIU60ZSuWNe7wzOuq28umDI
1p+Ee2XHZGiixHCYY6ij1XYhgRLf+YJZJs+OyiWY+pBKvSOUhD8EoTpQvOeKySIJ
Qd9fycfHhfDsMvQZ7XlETkyjfQkN2n6K1GsJwTR9gyNJCf4VSwwndNUqNp0qPdUZ
4k009QeQAfBV2OUwTaCYYO23jKRd0wUtJGQ8wcMMQ+IbF+rZ5ewNhTTFGsAWyddG
Uvg+mS/0jLxR/L0U8iKYV4QkonTdBwxuXZQn9yjWd/xE6Wm9BlLnH8JZyR1PTZmt
Wn7y16lAvspNOKWhjN4Ox6Us0K9RurdlPMIf409XfQxjnAV69dMG09G/+jEFGFc5
7tjOamd+YIjNBXKC5FvY3fSZUA8+5pCf+1Xgc2yD59Y5ALuCaLVS5fhqlWVzoOG0
uuNrQS32h6/vGyfedAR4Scqb9iZlJXfcxzswmqcdrjs9h7ALRhnKRRpmYLjIvDvx
ncn123oyvPYF5vg0B6k5ZenqgP2p1uMVP2OlF/9KFjOvGq70wP5S8quG+r5j+RzU
9rYffemN12Xl5NkCAwEAAaNTMFEwHQYDVR0OBBYEFNJockW5EtRY4cx83PyLUjGD
9UiMMB8GA1UdIwQYMBaAFNJockW5EtRY4cx83PyLUjGD9UiMMA8GA1UdEwEB/wQF
MAMBAf8wDQYJKoZIhvcNAQELBQADggIBAGFHxOEi1bYCUcEflYYKuMoNDeGPkpad
LKjyx+Uvo5rwjLEAdxQiGGBAWfB4tnGPsl51RZWojFH8FDyseo1cbubRHw+3sdIU
uTK8uMc2mG1zgR3Z/z49XBpG0tbYfOBfKMyoypz3CK0KwwFMvrx/Sk2hhD5WfDmW
stxSbBNqTOk5PzqBU9ROx7vdd4YzSItLXR6LOSiiYmN4nvKdXFwIooZEy1jnLJlr
U7OLG6SQSjLzi9go6VDKoA3yNDf+rgLrixrn1skkq76+SwRfyt9T3GqmWPSvyqed
/yommVt3exqMsU8Nfm3DuwXVuWkongaD2/cqwBiXocP41iNlEbQEmvgE9nTyZFa8
Exk0XE7a024ptZ6NktonCdgcG+EMf1uPdfGgq19wXqYwK9yiYBk7wd54vduAuKXw
ocHwqoEBWlp4JpcHBwa6KdhGAi7YPMUYRXxXHXLX/Z0/CUsXRBzPZG1nIce+gR/W
Cmkpuxm7SIBv8tY0tNRnmsYw/q8zf3b1lRcfHH7FsSy1LEO4ch41TPKdCnWuEUfh
5TzQFfvJ4qqzZgBGDMgBAR0ibDTSj5zapGxnNsLak7CGwmTWudrekQLHziGrBHvB
uazhAn49rFlxecLxE3IP4vtnpOvCw3hdJdEEWH0ug/6GTK8wLBzDSsuQ1o0U7FN1
JU1dMrut23uO
-----END CERTIFICATE-----


File: /t\certs\ca.key
-----BEGIN RSA PRIVATE KEY-----
MIIJKAIBAAKCAgEA6YLHJMVSHOry46falwjc4tFRMXuGayQ2ev76neLcWqdQyWtS
pChjkSlAY2NUBOxuKxuXmEokApoExJEeFXQ3u2Ce+6ATmQry2sYRZalMnntQa/HN
kya+UcBeFZf+TIm3g2uVgCIU60ZSuWNe7wzOuq28umDI1p+Ee2XHZGiixHCYY6ij
1XYhgRLf+YJZJs+OyiWY+pBKvSOUhD8EoTpQvOeKySIJQd9fycfHhfDsMvQZ7XlE
TkyjfQkN2n6K1GsJwTR9gyNJCf4VSwwndNUqNp0qPdUZ4k009QeQAfBV2OUwTaCY
YO23jKRd0wUtJGQ8wcMMQ+IbF+rZ5ewNhTTFGsAWyddGUvg+mS/0jLxR/L0U8iKY
V4QkonTdBwxuXZQn9yjWd/xE6Wm9BlLnH8JZyR1PTZmtWn7y16lAvspNOKWhjN4O
x6Us0K9RurdlPMIf409XfQxjnAV69dMG09G/+jEFGFc57tjOamd+YIjNBXKC5FvY
3fSZUA8+5pCf+1Xgc2yD59Y5ALuCaLVS5fhqlWVzoOG0uuNrQS32h6/vGyfedAR4
Scqb9iZlJXfcxzswmqcdrjs9h7ALRhnKRRpmYLjIvDvxncn123oyvPYF5vg0B6k5
ZenqgP2p1uMVP2OlF/9KFjOvGq70wP5S8quG+r5j+RzU9rYffemN12Xl5NkCAwEA
AQKCAgEAyL7CHy13kx604twJwrA+3MugJo8QFwnRwFl18Mf4MgMHI7GdIT0Lo963
2PmqYHU1nN+iqqyKWqY4FRjAqSb5RqAg7SdH0dkkwMloaWJrWQ+gKrx8w9WZ5kQf
XicF2pzGZDfYFYi3PTB+q5vvIEl9a+Uyi3PrFP+b8E2mZf7Cd2hoybxP5JIi6Yjl
feX+aKwlEEnUQwxLBGETK8HVZBnzEQNpP9J/7N5wxdJ3CAH/vSo3I/2NqFagcjyX
aVBCX60JfMx4XoW2I94IRjVTslATc1IX34JVN0SykzgGKHSKCOW3afT3KtUSZ9li
Q6h+j3uQ8+6Pm8hFDIG9A7m0QeEE1H8DhrRZ/dop1FPFCQUUbwuS3cTv38lcHZtb
VZDG2IBg1EeMyBBkV9RTMnTEB5Jr85AalzZ1HdUDRLVj8tiD5OGl+fc/YFBWj8UF
X40iQculO3BzMEGlHfiKGhOzIFQ0KDCYxlBa8DsNGscc12VJ671Qk8ZS219wV4VR
MtXUJny9D33hHG25ZePFcYnmGHpVwI+wrOkNuQSR4sbvAVNDfs6/HyTX946sHCJx
Qird7dHJeaqw1SCpPNzmCDVVmCBKkS6/PADDd6758njYjjOGFEDLwkOB624jpWaJ
NIgepz8pN+xSKgCvGseI1lBUWP3xoXeWX3BBZON0iTRfLjeokIECggEBAPfw/EF4
hj1zC3gZApaSL1jqw1Va6Rll5y/+jtN3ylFtpTDXfOX5oQEWt8CmqjcZg7uJ1nTJ
+M3IFv2NJamMPQHjAZcTTHvZKwAJ4fZyCmmmUqcsn2DeeZjES3FOAwPLEvuo8iWx
KYEgvfSH87Pa4Aj6doXyA7+0wY0a8x3Zvqfi3xvsuuKK+TKt4qxdASYazZBUYbAE
r+FX0obMWibZ2Yz/bUdskGPRzgYv47Vsyx5j8Zx2nkcnw99vgSqAEI3kwwzRNGhl
acE0fTz0qgkWr5kE3HF4I9tEGlXbal35s60awfDpSpoA6cxHERJkcC0XRNG321DO
RMKN+J5dqtStgtECggEBAPEZuPUBky/RC3WhcIUnCl9/rTlBf84Mo5SLS+N3Rqbe
6/bRo+/dmsQVZyFnwbDW1nIdU6ATv6W4hz5hV2VTLTkkz+2M7cnFo/y6eDN3naR0
m4EaFSQXcf8eIh2BawEuSNY34/C5t9fQwuYYGLw9cfk5LlBxsWEsTFyiCiTwl6/n
0E5syj1LRu/2gm4khAFzvYn0HDaBdu9Js4qwo+PfarvmbbkS9MD2TN043cvVYC5X
cWAQXWLPbNQZOylleGRrCSqmTGFeszP0XYELWgogd5W1liwSc2XMifNaSiUaBZ0o
JSYzXYYcJwN1eh5BX3JQuZFOn7WV1P5cy+LPzFqXc4kCggEAKOls1mjKzczz8Yc+
9BV/Fo72WFk96WD1OugoLSCxE6qh/WMxSslcFc/n1jQqFhlxsTpXVsIU+e+wS3pE
4qsvTeZlVsZqcm0tOT5oOMAsk65MKSWlztgm/Fw3jqSuvqt9oGUKP8nx7Uq3zWe5
gM329cROVl/O2o06+sudnilV2mIHKpZvZ/5CjGhA5OwbymvVy6EA1YiQdQCGzpNd
tNdxnGBxab2yPaZa9o5kZoVjJsqbDZRNHbSkD3RYveiP0roSrUS//xHs12KP38UH
YaSKqRcyQM7wK7gbGFuyO3t+eGvX4Ka+Fpdb/MclPAGyuN4EDw7lc3n1wpymj4sp
KxrOYQKCAQB6RSU7e3T9hvJc0WaS4F2uWL2sj78U6+v5ZTszPEYkUmEwZtjQyH24
e3I1yry7xfgzHxRN1jYXASH1TMBZrnj8xeJ9Aj+FWCn1/UsALuVPhaNnMacPCqTR
UKLUe9GcY7CkkuuSJV1KoaB1uDqzHCY00f7e5Qmj0idXwwWJ/kmu98z4OMvHkemD
wGwdF3+qjNvOnnHAYp/CcooPB83VvnQOnql+dlKRmVcZycERokCIv+fLZAE4HyF9
3t3V/JO1uWKIspWBu9j9vCu/SdZ71ENRNSnXZ/QF6Fj9hQidEDlQng9Y9Cu124kd
g/JObbDN9IpnWow8NqQx6zWq7N8iAjShAoIBAErum3zMYgTcukPVJZ6/sDqXwVz0
Bx9Yk3+MuVIYwjW0jOE6OoitdhAyKmyxWiv3xvRA4omEk4KlzTGnaKMpxGBMDlOp
HYeOz0rtbib9NWjl3gEGMidJyvcHBe5a4QuPr6nhIYftJZE6EzRTxwGEBYWnEB93
/cjZZpMg9dY73i7ZHKWykMUvb6FanCPcXfvSJ9AclHzppoot0J/HtOpnbueZfEXf
PVeW9MLTyX0cvVcBPehm3ymK1t4KGPIbXJupZZ55WTRV5Q3ju/FkcSEsR2UHkaBh
WV5ewlW7i2DLTUTyKxQxj+kPuI6fVDPdlznph/1qujja7zmsdfJ9BSntfc4=
-----END RSA PRIVATE KEY-----


File: /t\certs\client-bundle.crt
-----BEGIN CERTIFICATE-----
MIIDwjCCAaoCFF91mb7cKfYXJWfpyU+Me1lBb/1mMA0GCSqGSIb3DQEBCwUAMBox
CzAJBgNVBAYTAlVTMQswCQYDVQQDDAJjYTAeFw0yMTA1MDYxMzIyNDdaFw00MTA1
MDExMzIyNDdaMCExCzAJBgNVBAYTAlVTMRIwEAYDVQQDDAkxMjcuMC4wLjEwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkE8uz1v7r0JhbsSuthSGjCVcB
YHaYx1L/FwsOJ1CN+d6Eg0qxdemGuWGuhFcwcNAFd+7a9D8qWaemJskSpX5l5lOr
9tFXoKr/CdGLLQFw6jjqj7x9jvuywL3caPlF26DkqE+rA9ptyD4DOpW9nJJfRTG0
Hiuq8P7GDYMOFZqfkxNuqjKnRkP/a+QtAx73Vev2cb/0weuX5ldXnC7+6gtfMu4K
ygX+U3PEt535yWV21sAEXbMjzMSp0zVKLE+5AJrq+EoPn7NhMBvEjPA3YAPF4VEk
W9HNNkD23Vd0nPYYRJ2eHyyG3d/wdohA239SUqrirVyNLzIhQxD3FgxNpsCPAgMB
AAEwDQYJKoZIhvcNAQELBQADggIBAMIUKZ/dtkBFCNb5iowV36V/n4ny/UPw/3K2
80ZfdRMdGgi0ntttYvRAMbEpbSIahPi9mjGXW531y1LPKvh1q5rBINzrKiUjNscW
R0Alvh7M/0C3DHab8owsU7KJ7w6ONugi2DIyWXY4YCsqftwFz38PRQ6nQ6zZsTfe
N4AOcOWJaJTLGZQlMANDCTH0nvR/zyAcEhIOp/pMgHf+LlvF6VcMB7n+06Z3LHIk
p5uJfbxxIYFCYbDJK5fsfhRMIQQuBswZIm/PEzmlnoRILs5SB+1eDSQY6Uek4e92
nSP+xD68sDo3tQX59z/SHSJ2C5D7huXdu0EgGB/iUzWgdnyObbCTG1+Km3ggSfTc
CU3FvRYrOkpfzNPG+ie8awHC37/gJpwyPs75qrOFRbx/polYb9batsCA/lVTf+Ne
8LQsEARVzgy8JURrLNPdhxFCAtgBZ6WfL22qrCpJ4I3IcDgaBZEJrv1alWTXX7fd
luCYXiw9y/XazoShWxfbuG8ClWOhfytKG+VYjJuUBe5zG4GCirLjpcPqAc2cWM85
cynvzvoEHl3OqJ+phkC4Uoqb6f7E/h5sPKK9wbaCuFqcowi6xDF76RNCQmgMVHZK
UIbMHwChMLFfPnLRuBSscb8sKrUoUJJFGzw7UuRdGyMj6IUaX2LSl2A116VGUwoO
+jf63uJM
-----END CERTIFICATE-----
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApBPLs9b+69CYW7ErrYUhowlXAWB2mMdS/xcLDidQjfnehINK
sXXphrlhroRXMHDQBXfu2vQ/KlmnpibJEqV+ZeZTq/bRV6Cq/wnRiy0BcOo46o+8
fY77ssC93Gj5Rdug5KhPqwPabcg+AzqVvZySX0UxtB4rqvD+xg2DDhWan5MTbqoy
p0ZD/2vkLQMe91Xr9nG/9MHrl+ZXV5wu/uoLXzLuCsoF/lNzxLed+clldtbABF2z
I8zEqdM1SixPuQCa6vhKD5+zYTAbxIzwN2ADxeFRJFvRzTZA9t1XdJz2GESdnh8s
ht3f8HaIQNt/UlKq4q1cjS8yIUMQ9xYMTabAjwIDAQABAoIBAB7fJqXI3yApmHEw
LcKxWPnfKQK2TrpCTsh2YnsgRJTiHc8bEPPA9taFjO6UMf+ISmus/EEwUa47PkMR
6yVaBCVSKA4kG5F8RpBEHawtJKdFOr5PmyyYuZ0RjOeqzLQrNeOwE4Ve7TtYwOpE
nKYXjqbkUwzL3HWGcLl9E1qUEArUCU29Kg7Q3G9LgPoSF5oC/e010l4KMkKiVi6U
xTWxq4tX/R9t1xpWRwKKs1xbIHQ1jzGwM8fhR5qPaeJCW32qiBx4g5CXknSamHWv
FCkhcpTckrNOLmkn1e7oRDFswl4LPZAyY3Awfu/gKhiMwyYhREFl9D8VGtrTFIx7
/twPYrECgYEA1yl67V98f5yz00Pzr7XgwISdjwprmKu5Cq78LD4CQhIb491k8+Az
aSw/YhnJBFSiRwNq0+I8QgrlkeQtIlhaUci8ETBK7jMLoKoh0y6UuqC1UbzaIur1
XcaT5YucLOMTRniA/V63HilsP5uumVlwS+JpYosPbDOoKpuJQNUb2tkCgYEAwzgo
cdAALPmGoRTX2CLyq1jWllregf2VMJI5qjhoCnf4cxfYknow3wB8mHy8Cgka4xs+
iPkWcrixIeZq2OwugEt5R1HSzq9bHyX4jybH2G3Uv+ZgqKYK2HXvUhx4RJ0Galy9
EBuNEB7gY6kqFMTewDBSeZT6V8tPTWw1omJixacCgYEAx50LF6frt/SofIrhTJWf
Ityl1CvlsKk4Leozt9P7glKMn3UpkHvjFmLfluK3NJZUSy+nb1XHc7nqS9R17xQr
Dw79M7ErAxxGYFMWuHbRsucf8OoVMinrY4m0clR4msg8fLeVa/rwRkJF1ClZ7Zkl
brFp9etvboHqNUVBK+3KPtkCgYAtuJhYV4PDBMnQLiaDO2QkV1Eis7OLNE3dq1GQ
GVfco85vfjU90RpjECUePZB4tTsz12yk/dmREsqBiwqZNW+KoqKL3pEF0TIBMI5v
UIDbopWCQD2BIipGGhDr5TkRsMkQ3hl1jU5TaTfaf4MYjCczUd3vFcIwD7DKDD7f
gjVp3wKBgQDDcD4u1FOMhlu7eUJ7UzddgyH29MSE2B69/Sl7FoWlAMPWaKieVDJX
ZKvOLhfQ3OVBWlMD+rYKjCYH8syF1qKDmgIV2SKy4R3Pnx62kpAZmAUQjzgVDgRx
McHvXbty+16H2QJnJCYuHu1dHXnD6KU8PbFKSBgiAJrUilP8PR6eVQ==
-----END RSA PRIVATE KEY-----


File: /t\certs\client.crt
-----BEGIN CERTIFICATE-----
MIIDwjCCAaoCFF91mb7cKfYXJWfpyU+Me1lBb/1mMA0GCSqGSIb3DQEBCwUAMBox
CzAJBgNVBAYTAlVTMQswCQYDVQQDDAJjYTAeFw0yMTA1MDYxMzIyNDdaFw00MTA1
MDExMzIyNDdaMCExCzAJBgNVBAYTAlVTMRIwEAYDVQQDDAkxMjcuMC4wLjEwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkE8uz1v7r0JhbsSuthSGjCVcB
YHaYx1L/FwsOJ1CN+d6Eg0qxdemGuWGuhFcwcNAFd+7a9D8qWaemJskSpX5l5lOr
9tFXoKr/CdGLLQFw6jjqj7x9jvuywL3caPlF26DkqE+rA9ptyD4DOpW9nJJfRTG0
Hiuq8P7GDYMOFZqfkxNuqjKnRkP/a+QtAx73Vev2cb/0weuX5ldXnC7+6gtfMu4K
ygX+U3PEt535yWV21sAEXbMjzMSp0zVKLE+5AJrq+EoPn7NhMBvEjPA3YAPF4VEk
W9HNNkD23Vd0nPYYRJ2eHyyG3d/wdohA239SUqrirVyNLzIhQxD3FgxNpsCPAgMB
AAEwDQYJKoZIhvcNAQELBQADggIBAMIUKZ/dtkBFCNb5iowV36V/n4ny/UPw/3K2
80ZfdRMdGgi0ntttYvRAMbEpbSIahPi9mjGXW531y1LPKvh1q5rBINzrKiUjNscW
R0Alvh7M/0C3DHab8owsU7KJ7w6ONugi2DIyWXY4YCsqftwFz38PRQ6nQ6zZsTfe
N4AOcOWJaJTLGZQlMANDCTH0nvR/zyAcEhIOp/pMgHf+LlvF6VcMB7n+06Z3LHIk
p5uJfbxxIYFCYbDJK5fsfhRMIQQuBswZIm/PEzmlnoRILs5SB+1eDSQY6Uek4e92
nSP+xD68sDo3tQX59z/SHSJ2C5D7huXdu0EgGB/iUzWgdnyObbCTG1+Km3ggSfTc
CU3FvRYrOkpfzNPG+ie8awHC37/gJpwyPs75qrOFRbx/polYb9batsCA/lVTf+Ne
8LQsEARVzgy8JURrLNPdhxFCAtgBZ6WfL22qrCpJ4I3IcDgaBZEJrv1alWTXX7fd
luCYXiw9y/XazoShWxfbuG8ClWOhfytKG+VYjJuUBe5zG4GCirLjpcPqAc2cWM85
cynvzvoEHl3OqJ+phkC4Uoqb6f7E/h5sPKK9wbaCuFqcowi6xDF76RNCQmgMVHZK
UIbMHwChMLFfPnLRuBSscb8sKrUoUJJFGzw7UuRdGyMj6IUaX2LSl2A116VGUwoO
+jf63uJM
-----END CERTIFICATE-----


File: /t\certs\client.key
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApBPLs9b+69CYW7ErrYUhowlXAWB2mMdS/xcLDidQjfnehINK
sXXphrlhroRXMHDQBXfu2vQ/KlmnpibJEqV+ZeZTq/bRV6Cq/wnRiy0BcOo46o+8
fY77ssC93Gj5Rdug5KhPqwPabcg+AzqVvZySX0UxtB4rqvD+xg2DDhWan5MTbqoy
p0ZD/2vkLQMe91Xr9nG/9MHrl+ZXV5wu/uoLXzLuCsoF/lNzxLed+clldtbABF2z
I8zEqdM1SixPuQCa6vhKD5+zYTAbxIzwN2ADxeFRJFvRzTZA9t1XdJz2GESdnh8s
ht3f8HaIQNt/UlKq4q1cjS8yIUMQ9xYMTabAjwIDAQABAoIBAB7fJqXI3yApmHEw
LcKxWPnfKQK2TrpCTsh2YnsgRJTiHc8bEPPA9taFjO6UMf+ISmus/EEwUa47PkMR
6yVaBCVSKA4kG5F8RpBEHawtJKdFOr5PmyyYuZ0RjOeqzLQrNeOwE4Ve7TtYwOpE
nKYXjqbkUwzL3HWGcLl9E1qUEArUCU29Kg7Q3G9LgPoSF5oC/e010l4KMkKiVi6U
xTWxq4tX/R9t1xpWRwKKs1xbIHQ1jzGwM8fhR5qPaeJCW32qiBx4g5CXknSamHWv
FCkhcpTckrNOLmkn1e7oRDFswl4LPZAyY3Awfu/gKhiMwyYhREFl9D8VGtrTFIx7
/twPYrECgYEA1yl67V98f5yz00Pzr7XgwISdjwprmKu5Cq78LD4CQhIb491k8+Az
aSw/YhnJBFSiRwNq0+I8QgrlkeQtIlhaUci8ETBK7jMLoKoh0y6UuqC1UbzaIur1
XcaT5YucLOMTRniA/V63HilsP5uumVlwS+JpYosPbDOoKpuJQNUb2tkCgYEAwzgo
cdAALPmGoRTX2CLyq1jWllregf2VMJI5qjhoCnf4cxfYknow3wB8mHy8Cgka4xs+
iPkWcrixIeZq2OwugEt5R1HSzq9bHyX4jybH2G3Uv+ZgqKYK2HXvUhx4RJ0Galy9
EBuNEB7gY6kqFMTewDBSeZT6V8tPTWw1omJixacCgYEAx50LF6frt/SofIrhTJWf
Ityl1CvlsKk4Leozt9P7glKMn3UpkHvjFmLfluK3NJZUSy+nb1XHc7nqS9R17xQr
Dw79M7ErAxxGYFMWuHbRsucf8OoVMinrY4m0clR4msg8fLeVa/rwRkJF1ClZ7Zkl
brFp9etvboHqNUVBK+3KPtkCgYAtuJhYV4PDBMnQLiaDO2QkV1Eis7OLNE3dq1GQ
GVfco85vfjU90RpjECUePZB4tTsz12yk/dmREsqBiwqZNW+KoqKL3pEF0TIBMI5v
UIDbopWCQD2BIipGGhDr5TkRsMkQ3hl1jU5TaTfaf4MYjCczUd3vFcIwD7DKDD7f
gjVp3wKBgQDDcD4u1FOMhlu7eUJ7UzddgyH29MSE2B69/Sl7FoWlAMPWaKieVDJX
ZKvOLhfQ3OVBWlMD+rYKjCYH8syF1qKDmgIV2SKy4R3Pnx62kpAZmAUQjzgVDgRx
McHvXbty+16H2QJnJCYuHu1dHXnD6KU8PbFKSBgiAJrUilP8PR6eVQ==
-----END RSA PRIVATE KEY-----


File: /t\certs\server.crt
-----BEGIN CERTIFICATE-----
MIIDwjCCAaoCFF91mb7cKfYXJWfpyU+Me1lBb/1lMA0GCSqGSIb3DQEBCwUAMBox
CzAJBgNVBAYTAlVTMQswCQYDVQQDDAJjYTAeFw0yMTA1MDYxMzIxNTVaFw00MTA1
MDExMzIxNTVaMCExCzAJBgNVBAYTAlVTMRIwEAYDVQQDDAkxMjcuMC4wLjEwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDE4SGXoPU2ZmgNeikw5s3ANtkd
tPCRcNfBnsiKXYnjavu0PH9hTqeaWm1KxrQDbXUP+c+MiDnbEovzfVu3mOoqkLYu
eadQHgRGetWRNREFv3uaDywIW+4d2rrqVGQJBzr/7hmmai7YqKvzpGU8+dggiGgn
8iaEzSH5yoTrHHb+/4zDSvdkg268wgehzWIWTLKrz5NK035nQFAZQhe3hY2/EUsV
elBgFshKt3cXPoFOTBCiOkNHacmRsJGccjGTzU6ebthF461XEtGcFuWdDbYi63St
r7J0n8T4vekD8bswraEgjm21rhsBDBYwAo1V+iErFy+7vouHKYeFD+jyxP3ZAgMB
AAEwDQYJKoZIhvcNAQELBQADggIBAL//kCygA4KDIl6qc7Izfh2cRjqoW6PIIgze
tH5OwIjuAzFTsyfW5N/K/6uxe0TPhROaGHmt/CCqbvLNo26B9EfMXeUxVeE6Me8v
spyep4JFyncFIgt9ISXWSseRGtFZKA5TJRPJPZVPYQKiX4jRwWpaSRioWFc2YUgq
LggqfC3U6HiEwYNI9Rq2uUL8nrbK0Y7UeaMr7YNnFkR3l4bUSiN0jTil4yBoLUNh
c/s6u38q+PQQr2Z0jyT+vOpAYEex8y8nK4Lsikq7auV1cilwsa7NyOiC+J/Dk73g
Vy2bR+/Ujm1CxOsXMwlX90zpAxOogFCy1A0vN0bz720Iuw9fQYnrXBWzI6ufY8md
ZWxF7TDDLU5xH+JI80MJKW0F1HhgtzrO5NwXi5L3RDtjnts9Vz4ohKepYTKN16Sp
QpurcZ4HKmJM2w72btdfTZo4quMKjssXZvSbxQhyYFT4sIlsAQJknA1yp8m+rIQK
3Wd+rHQWWzQlvC92qVfixIku1Q5VaBxUxihcNzirrJcwjlipGfqJUGf1F6OssL4p
WVkDqrvLoNJ+TrhStWtOgT46+B/61ZPS54qpOjOc9V28vwys8v02cjRn0A4RXDSU
BgQIx53Qh1xfPcJjkVWkZBsrCIlIHW3E5FDpiZ/BiPo7H1hgFg3ggoLEn4IfQEcS
ynic0cxw
-----END CERTIFICATE-----


File: /t\certs\server.key
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxOEhl6D1NmZoDXopMObNwDbZHbTwkXDXwZ7Iil2J42r7tDx/
YU6nmlptSsa0A211D/nPjIg52xKL831bt5jqKpC2LnmnUB4ERnrVkTURBb97mg8s
CFvuHdq66lRkCQc6/+4Zpmou2Kir86RlPPnYIIhoJ/ImhM0h+cqE6xx2/v+Mw0r3
ZINuvMIHoc1iFkyyq8+TStN+Z0BQGUIXt4WNvxFLFXpQYBbISrd3Fz6BTkwQojpD
R2nJkbCRnHIxk81Onm7YReOtVxLRnBblnQ22Iut0ra+ydJ/E+L3pA/G7MK2hII5t
ta4bAQwWMAKNVfohKxcvu76LhymHhQ/o8sT92QIDAQABAoIBAQCkrO5tJquUagnE
pBaKGbOlf/sQ1wSVkn5VLFvvKBgqyZRpiGS/XovgFpzt+9AcQdS1nS0WDefert+y
tXse0V+kZNCNhSIGaGUJErtKLsnjNevLy7736vT7sbXARQA7cPnPkjeQM6algEf7
jdlELHKzm4ULTIcdc3tktRmCkpeR53MbJMW3jkl/xeYbA0elbwsVJJwGrD+j2o2G
5ARtGWBK5nwDez9PQi2p2mgWotCbD2AEgP9BCij6qVKFTjGhV11hADGY/05Vf9Gd
O5dxjAPCIK5pAn45w1JRhAhhafH2dQbQJ68bR/AlrBg0bebYkl6kFjUFXh8eZjIb
3nltcSg1AoGBAPkfwGAMpWuSEema9qM6I+2YjFtbwIRcTLg0TnlhkReHFU9L6i5H
NuoTyUarIybCIBUqVxryx5WrAg6z69yk5nrMIpYmBGMm6uSLEEOg5/z1KIgDTokv
ifw1T52ajUP+HpZpmZ++zEzEpmutL3nf4UfKlfWfglNLvZReC+b/RQ0/AoGBAMpQ
O3ilLjKMlJVCULOjnYYxErpsjtloYo/lp36hSMhyv7/LrWbORbRJUiXc78Cu0IhI
AA6hhkyEmDEylGAA5A8zK+McWfd49QpPcf6tFwxsHncHDsxrBbWctaPS2cuIXL02
ujn5aIpK7eb+2iP8jW1tBEOuaH/GfszyNoSS5XbnAoGAEzNCRWTUHv1MCiAaYCwr
9rTqJGRm6wyeERhe7/X4E8MiflEQhG6SqenKenrYI7WUeW0g93+8qClc6Dsvs3q2
FMLE66OUdPvb4K9jGoM9Pf67F/iBRgt27AxDzZbKynG8c8VBxNEUt9n0JZpcbV02
5KyVcC/SAI921geFjVEhRksCgYAmvSg2GML40OxejD0xuKGgIWNpqQHNZWyCC0KA
P9fU8gv/aLvCVLsKI4QEVgLejVrGzaqdIpa5riYKPZolq+X/dxfvO+2KMnIRUFcO
ogwox8cpmYNe5xtHxEMPpH8ptumzHXiZQ0WePWzCb4hLnb9i9Z38a7f8x4BeM/72
cb5YfwKBgQCfwu1l+gFFrtENKk1Dei5ZaKN9QpoWRr2yjD7K9sPWivde9waWfqYQ
dESOcoUg/a8aTLS7ruhRXr/q8dSK1TDkrjB98sA5eHLwlieZtNM69NGozWuUNICk
ILFOi7NStr2nyl1fMkWOiAoZSLbRrFuUL7gtQTrw9m3fmHZ+rPIMHQ==
-----END RSA PRIVATE KEY-----


File: /t\lib\MikroTik\Client\Mockup.pm
package MikroTik::Client::Mockup;
use MikroTik::Client::Mo;

use AE;
use AnyEvent::Handle;
use AnyEvent::Socket;
use MikroTik::Client::Response;
use MikroTik::Client::Sentence qw(encode_sentence);
use Scalar::Util 'weaken';

has 'error';
has port   => undef;
has res    => sub { MikroTik::Client::Response->new() };
has server => sub {
    my $self = shift;
    weaken $self;

    return tcp_server "127.0.0.1", $self->port, sub {
        my $fh = shift;
        $self->{h} = AnyEvent::Handle->new(
            fh => $fh,

            $self->tls_opts
            ? (tls => "accept", tls_ctx => $self->{tls_opts})
            : (),

            on_read => sub {
                my $h    = shift;
                my $data = $self->res->parse(\$h->{rbuf});
                for (@$data) {
                    my $cmd = $_->{'.type'} // '';
                    warn "wrong command \"$cmd\"\n" and next
                        unless $cmd =~ s/^\//cmd_/;
                    $cmd =~ s/\//_/g;

                    eval {
                        my $resp = '';
                        $resp .= encode_sentence(@$_) for ($self->$cmd($_));
                        $h->push_write($resp);
                        1;
                    } or warn "unhandled command \"$cmd\": $@";
                }
            },
            on_eof => sub { delete $self->{timers} },
            on_error => sub { $self->error($_[2]) }
        );
    }, sub { $self->port($_[2]); return 0 };
};
has 'tls_opts';

sub close {
    my $self = shift;
    $self->{h}->destroy();
    delete @{$self}{qw(h server res)};
    return $self;
}

sub cmd_cancel {
    my ($self, $attr) = @_;
    my $tag     = $attr->{'.tag'};
    my $cmd_tag = $attr->{'tag'};

    return ['!trap', {message => 'unknown command'}, undef, $tag]
        unless delete $self->{timers}{$cmd_tag};

    return (
        ['!trap', {category => 2, message => 'interrupted'}, undef, $cmd_tag],
        _done($tag), _done($cmd_tag));
}

sub cmd_close_premature {
    my ($self, $attr) = @_;

    $self->{timers}{_prem} = AE::timer 0.25, 0, sub { $self->{h}->destroy };
    return ();
}

sub cmd_err {
    my (undef, $attr) = @_;
    my $tag = $attr->{'.tag'};
    return ['!trap', {message => 'random error', category => 0}, undef, $tag];
}

sub cmd_login {
    my (undef, $attr) = @_;
    my $tag = $attr->{'.tag'};

    return _done($tag, {ret => '098f6bcd4621d373cade4e832627b4f6'})
        unless $attr->{name};

    return _done($tag) if $attr->{name} eq 'test' && (

        # Pre 6.43
        ($attr->{response} // '') eq '00119ce7e093e33497053e73f37a5d3e15'

        # 6.43+
        or ($attr->{password} // '') eq 'tset'
    );

    return ['!fatal', {message => 'cannot log in'}, undef, $tag];
}

sub cmd_nocmd {
    return ();
}

sub cmd_resp {
    my (undef, $attr) = @_;
    my $tag = $attr->{'.tag'};

    my $resp = ['!re', _gen_attr(@{$attr}{'.proplist', 'count'}), undef, $tag];
    return ($resp, $resp, _done($tag));
}

sub cmd_subs {
    my ($self, $attr) = @_;
    my $tag = $attr->{'.tag'} // 0;
    my $key = $attr->{'key'};

    $self->{timers}{$tag} = AE::timer 0.5, 0.5, sub {
        $self->{h}
            ->push_write(encode_sentence('!re', {key => $key}, undef, $tag));
    };

    return ();
}

sub _done {
    return ['!done', $_[1], undef, $_[0]];
}

sub _gen_attr {
    my $c    = $_[1] // 0;
    my $attr = {};
    $attr->{$_} = 'attr' . ($c++) for split /,/, ($_[0] // 'prop1,prop2,prop0');
    return $attr;
}

1;


File: /t\mikrotik-online.t
#!/usr/bin/env perl

use warnings;
use strict;

use lib './';

use Test::More;

plan skip_all =>
    'On-line tests. Set MIKROTIK_CLIENT_ONLINE to "host:user:pass:tls" to run.'
    unless $ENV{MIKROTIK_CLIENT_ONLINE};

use MikroTik::Client;
use MikroTik::Client::Response;
use MikroTik::Client::Sentence;

my ($h, $u, $p, $tls) = split ':', ($ENV{MIKROTIK_CLIENT_ONLINE} || '');
my $a = MikroTik::Client->new(
    user     => ($u   // 'admin'),
    password => ($p   // ''),
    host     => ($h   // '192.168.88.1'),
    tls      => ($tls // 1),
);

my $res;
$res = $a->cmd(
    '/interface/print',
    {'.proplist' => '.id,name,type,running'},
);
ok !$a->error, 'no error';
my @keys = sort keys %{$res->[0]};
is_deeply [@keys], [qw(.id name running type)], 'right result';

done_testing();



File: /t\mikrotik.t
#!/usr/bin/env perl

use warnings;
use strict;

BEGIN {
    $ENV{MIKROTIK_CLIENT_CONNTIMEOUT} = 0.5;
}

use FindBin;
use lib './';
use lib "$FindBin::Bin/lib";

use Test::More;

use AE;
use Errno qw(ECONNREFUSED);
use MikroTik::Client;
use MikroTik::Client::Mockup;
use Time::HiRes;

# Check for monotonic clock support
use constant MONOTONIC =>
    eval { !!Time::HiRes::clock_gettime(Time::HiRes::CLOCK_MONOTONIC()) };

*steady_time
    = MONOTONIC
    ? sub () { Time::HiRes::clock_gettime(Time::HiRes::CLOCK_MONOTONIC()) }
    : \&Time::HiRes::time;

my $mockup = MikroTik::Client::Mockup->new();
$mockup->server;
my $port = $mockup->port;

my $api = MikroTik::Client->new(
        user     => "test",
        password => "tset",
        host     => "127.0.0.1",
        port     => 0,
        tls      => 0,
    );

# check connection
my $res = $api->cmd('/resp');
ok $! == ECONNREFUSED, 'connection error';
$api->port($port);

# check login
$api->password('');
$res = $api->cmd('/resp');
like $api->error, qr/cannot log/, 'login error';

$api->new_login(1);
$res = $api->cmd('/resp');
like $api->error, qr/cannot log/, 'login error (new style)';
$api->password('tset');

# timeouts
$api->timeout(1);
my $ctime = steady_time();
$res = $api->cmd('/nocmd');
ok((steady_time() - $ctime) < 1.1, 'timeout ok');
$api->timeout(0.5);
$ctime = steady_time();
$res   = $api->cmd('/nocmd');
ok((steady_time() - $ctime) < 0.6, 'timeout ok');
$api->timeout(1);

# close connection prematurely, next command should succeed
$res = $api->cmd('/close/premature');
ok !$res, 'no result';
is $api->error, 'closed prematurely', 'right error';

# also check previous test case on errors
$res = $api->cmd('/resp');
is_deeply $res, _gen_result(), 'right result';

$res = $api->cmd('/resp', {'.proplist' => 'prop0,prop2'});
is_deeply $res, _gen_result('prop0,prop2'), 'right result';

$res = $api->cmd('/resp', {'.proplist' => 'prop0,prop2', count => 3});
is_deeply $res, _gen_result('prop0,prop2', 3), 'right result';

$res = $api->cmd('/err');
is $api->error, 'random error', 'right error';
is_deeply $res, [{message => 'random error', category => 0}],
    'right error attributes';

# Non-blocking call
$api->cmd('/resp', {'.proplist' => 'prop0,prop2', count => 1} => sub {
            is_deeply $_[2], _gen_result('prop0,prop2', 1), 'right result';
});

# subscriptions
my ($err, $tag);
$res = undef;
$tag = $api->subscribe('/subs', {key => 'nnn'} => sub {
            $res = $_[2] unless $err = $_[1];
            $api->cancel($tag);
});

my ($err1, $err2);
$api->cmd('/err' => sub { $err1 = $_[1] . '1' });
$api->cmd('/err' => sub { $err2 = $_[1] . '2' });

my $done = AE::cv;
my $stop_g = AE::timer 1.3, 0, $done;
$done->recv;

is_deeply $res, {
        key => 'nnn'
    },
    'right result';
is $err,  'interrupted',   'right error';
is $err1, 'random error1', 'right error';
is $err2, 'random error2', 'right error';

done_testing();

sub _gen_result {
        my $attr = MikroTik::Client::Mockup::_gen_attr(@_);
        return [$attr, $attr];
}


File: /t\pod.t
use warnings;
use strict;

use Test::More;

plan skip_all => 'set TEST_POD to enable this test (developer only!)'
  unless $ENV{TEST_POD};
plan skip_all => 'Test::Pod 1.14+ required for this test!'
  unless eval 'use Test::Pod 1.14; 1';

all_pod_files_ok();


File: /t\pod_coverage.t
use warnings;
use strict;

use Test::More;

plan skip_all => 'set TEST_POD to enable this test (developer only!)'
  unless $ENV{TEST_POD};
plan skip_all => 'Test::Pod::Coverage 1.04+ required for this test!'
  unless eval 'use Test::Pod::Coverage 1.04; 1';

# DEPRECATED!
all_pod_coverage_ok({also_private => ['data', 'remaining']});


File: /t\promises.t
#!/usr/bin/env perl

use warnings;
use strict;

BEGIN {
    $ENV{MIKROTIK_CLIENT_CONNTIMEOUT} = 0.5;
}

use FindBin;
use lib './';
use lib "$FindBin::Bin/lib";

use AE;
use Errno qw(ECONNREFUSED);
use MikroTik::Client;
use MikroTik::Client::Mockup;
use Test::More;

plan skip_all => 'Promises v0.99+ required for this test.'
    unless MikroTik::Client->PROMISES;

my $mockup = MikroTik::Client::Mockup->new();
$mockup->server;
my $port   = $mockup->port;

my $api    = MikroTik::Client->new(
    user     => 'test',
    password => 'tset',
    host     => '127.0.0.1',
    port     => 0,
    tls      => 0,
);

my $p = $api->cmd_p('/resp');
isa_ok $p, 'Promises::Promise', 'right result type';

# connection errors
my ($cv, $err, $res);
$cv = AE::cv;
$p->catch(sub { ($err, $res) = @_ })->finally($cv);
$cv->recv;
ok $! == ECONNREFUSED, 'connection error';
ok !$res, 'no error attributes';
$api->port($port);

# error
$cv = AE::cv;
$api->cmd_p('/err')->catch(sub { ($err, $res) = @_ })
    ->finally($cv);
$cv->recv;
is $err, 'random error', 'right error';
is_deeply $res, [{message => 'random error', category => 0}],
    'right error attributes';

# request
$cv  = AE::cv;
$api->cmd_p('/resp')->then(sub { $res = $_[0] })
    ->finally($cv);
$cv->recv;
is_deeply $res, _gen_result(), 'right result';

done_testing();

sub _gen_result {
    my $attr = MikroTik::Client::Mockup::_gen_attr(@_);
    return [$attr, $attr];
}


File: /t\query.t
#!/usr/bin/env perl

use warnings;
use strict;

use lib './';

use Test::More;
use MikroTik::Client::Query 'build_query';

my $r = build_query({a => 1, b => 2, c => 3, d => 4});
is_deeply $r, ['?a=1', '?b=2', '?c=3', '?d=4', '?#&&&'], 'simple AND';

$r = build_query([a => 1, b => 2, c => 3]);
is_deeply $r, ['?a=1', '?b=2', '?c=3', '?#||'], 'simple OR';

$r = build_query({-and => [a => 1, b => 2, c => 3]});
is_deeply $r, ['?a=1', '?b=2', '?c=3', '?#&&'], 'specific logic AND';

$r = build_query({-or => {a => 1, b => 2, c => 3, d => 4}});
is_deeply $r, ['?a=1', '?b=2', '?c=3', '?d=4', '?#|||'], 'specific logic OR';

$r = build_query({-or => {a => 1, b => 2}, -and => [c => 3, d => 4, e => 5]});
is_deeply $r, ['?c=3', '?d=4', '?e=5', '?#&&', '?a=1', '?b=2', '?#|', '?#&'],
    'nested ops';

$r = build_query(
    [
        -or  => {a => 1, b => 2, -and => {e => 5, f => 6, g => 7}},
        -and => [c => 3, d => 4],
        {h => 8, i => 9}
    ]
);
is_deeply $r,
    [
    '?e=5', '?f=6', '?g=7', '?#&&', '?a=1', '?b=2', '?#||', '?c=3',
    '?d=4', '?#&',  '?h=8', '?i=9', '?#&',  '?#||'
    ],
    'nested ops 2';

$r = build_query(\['?e=5', '?f=6', '?g=7', '?#&&', '?a=1', '?b=2', '?#||']);
is_deeply $r, ['?e=5', '?f=6', '?g=7', '?#&&', '?a=1', '?b=2', '?#||'],
    'literal query';

$r = build_query();
is_deeply $r, [], 'empty query';

$r = build_query({a => [1, 2, 3]});
is_deeply $r, ['?a=1', '?a=2', '?a=3', '?#||'], 'arrayref value';

$r = build_query([a => [-and => 1, 2, 3]]);
is_deeply $r, ['?a=1', '?a=2', '?a=3', '?#&&'],
    'arrayref value with specific logic';

$r = build_query({a => {'>', [1, 2, 3]}});
is_deeply $r, ['?a>1', '?a>2', '?a>3', '?#||'],
    'arrayref value with specific operator';

$r = build_query({a => {'=', [-and => 1, 2, 3]}});
is_deeply $r, ['?a=1', '?a=2', '?a=3', '?#&&'],
    'arrayref value with logic and operator';

$r = build_query({a => {'<' => 3, '>' => 1}});
is_deeply $r, ['?a<3', '?a>1', '?#&'], 'hashref value';

$r = build_query({a => [-or => {'>', 1}, {'<', 2}, {'>', 3, '<', 4}]});
is_deeply $r, ['?a>1', '?a<2', '?a<4', '?a>3', '?#&', '?#||'],
    'list of hashrefs';

$r = build_query({a => {-not => 1}, -has => 'b', -has_not => 'c'});
is_deeply $r, ['?b', '?-c', '?a=1', '?#!', '?#&&'], 'special cases';

$r = build_query({a => {-not => [-and => 1, 2, 3]}});
is_deeply $r, ['?a=1', '?#!', '?a=2', '?#!', '?a=3', '?#!', '?#&&'],
    '-not with arrayref value';

$r = build_query([[], a => 1, [{}, {}, \[]], b => [], c => 5, d => {}]);
is_deeply $r, ['?a=1', '?c=5', '?#|'], 'ignore empty structs';

$r = build_query([a => [{'=', []}, 2, {}]]);
is_deeply $r, ['?a=2'], 'ignore empty structs';

my $err;
$SIG{__WARN__} = sub { $err = $_[0] };
$r = build_query([a => undef, b => [1, undef, 2], c => {'=', undef}]);
ok !$err, 'no warning';
is_deeply $r, ['?a=', '?b=1', '?b=', '?b=2', '?#||', '?c=', '?#||'],
    'right result';

done_testing();



File: /t\response.t
#!/usr/bin/env perl

use warnings;
use strict;

use lib './';

use Test::More;
use MikroTik::Client::Response;
use MikroTik::Client::Sentence qw(encode_sentence);

my $r = MikroTik::Client::Response->new();

my $packed = encode_sentence('!re', {a => 1, b => 2});
$packed .= encode_sentence('!re', {c => 3, d => 4, e => 5}, undef, 3);
$packed .= encode_sentence('!done');

my $data = $r->parse(\$packed);
is_deeply $data,
  [
  {a      => '1', b       => '2', '.tag' => '', '.type' => '!re'},
  {e      => '5', d       => '4', c => '3', '.tag' => '3', '.type' => '!re'},
  {'.tag' => '',  '.type' => '!done'}
  ],
  'right response';

# reassemble partial buffer
my ($attr, @parts);
$attr->{$_} = $_ x 200 for 1 .. 4;

$packed = encode_sentence('!re', $attr);
$packed .= $packed . $packed . $packed;
push @parts, (substr $packed, 0, $_, '') for (900, 700, 880, 820);

$attr->{'.tag'}  = '';
$attr->{'.type'} = '!re';

my $buf = $parts[0];
my $w   = $r->parse(\$buf);
is_deeply $w, [$attr], 'right result';
ok $r->sentence->is_incomplete, 'incomplete is set';
$buf .= $parts[1];
$w = $r->parse(\$buf);
is_deeply $w, [], 'right result';
ok $r->sentence->is_incomplete, 'incomplete is set';
$buf .= $parts[2];
$w = $r->parse(\$buf);
is_deeply $w, [($attr) x 2], 'right result';
ok $r->sentence->is_incomplete, 'incomplete is set';
$buf .= $parts[3];
$w = $r->parse(\$buf);
is_deeply $w, [$attr], 'right result';
ok !$r->sentence->is_incomplete, 'incomplete is not set';

# newline in response
$packed
  = encode_sentence('!re', {multiline => "This is\nmulti line\nattribute!"});
$data = $r->parse(\$packed);
is_deeply $data,
  [{multiline => "This is\nmulti line\nattribute!", '.tag' => '', '.type' => '!re'
  }], 'right results';

done_testing();


File: /t\sentence.t
#!/usr/bin/env perl

use warnings;
use strict;

use lib './';

use Test::More;
use MikroTik::Client::Sentence qw(encode_sentence);

my $s = MikroTik::Client::Sentence->new();

# length encoding
my ($packed, $len);
for (0x7f, 0x3fff, 0x1fffff, 0xfffffff, 0x10000000) {
    $packed = MikroTik::Client::Sentence::_encode_length($_);
    ($len, undef) = MikroTik::Client::Sentence::_strip_length(\$packed);
    is $len, $_, "length encoding: $_";
}

# encode word
my $encoded = MikroTik::Client::Sentence::_encode_word('bla' x 3);
$encoded .= MikroTik::Client::Sentence::_encode_word('bla' x 50);
is length($encoded), 162, 'right length';
is $s->_fetch_word(\$encoded), 'bla' x 3, 'right decoded word';
is length($encoded), 152, 'right length';
is $s->_fetch_word(\$encoded), 'bla' x 50, 'right decoded word';

$packed = encode_sentence('/cmd/1', {a => 1, b => 2});
$packed
    .= encode_sentence('/cmd/2', {c => 'foo', d => 'bar'}, {e => 'baz'}, 11);
my $words = $s->fetch(\$packed);
is shift @$words, '/cmd/1', 'right command';
is_deeply [sort @$words], ['=a=1', '=b=2'], 'right attributes';
$words = $s->fetch(\$packed);
is shift @$words, '/cmd/2', 'right command';
is_deeply [sort @$words], ['.tag=11', '=c=foo', '=d=bar', '?e=baz'],
    'right attributes';

# buffer ends in the middle of a word
$packed = encode_sentence('/one/two/three', {test => 1, another => 2});
substr $packed, 20, 20, '';
$words = $s->fetch(\$packed);
is_deeply $words, ['/one/two/three'], 'right results';
ok $s->is_incomplete, 'incomplete is set';

# reset
$s->reset;
ok !$s->is_incomplete, 'incomplete is not longer set';

# buffer ends at the end of the word, before an empty closing word
$packed = encode_sentence('/one/two', {three => 'four'});
my $tr = substr $packed, -1, 1, '';
is $tr, "\0", 'trailing empty word';
$words = $s->fetch(\$packed);
is_deeply $words, ['/one/two', '=three=four'], 'right results';
ok $s->is_incomplete, 'incomplete is set';

my $err;
$SIG{__WARN__} = sub { $err = $_[0] };
$packed = encode_sentence('/cmd', {argv => undef});
ok !$err, 'no warning';
$words = $s->reset->fetch(\$packed);
is_deeply $words, ['/cmd', '=argv='], 'right results';

done_testing();



File: /t\tls.t
#!/usr/bin/env perl

use warnings;
use strict;

use FindBin;
use lib './';
use lib "$FindBin::Bin/lib";

use Test::More;

use Errno qw(EPROTO);
use MikroTik::Client;
use MikroTik::Client::Mockup;
use Time::HiRes;


plan skip_all => 'TLS tests. Set TEST_TLS to run.'
    unless $ENV{TEST_TLS};

my $mockup = MikroTik::Client::Mockup->new();
$mockup->tls_opts({
    ca_file                    => "./t/certs/ca.crt",
    cert_file                  => "./t/certs/server.crt",
    key_file                   => "./t/certs/server.key",
    verify                     => 1,
    verify_require_client_cert => 1
});
$mockup->server;
my $port = $mockup->port;

my %client_opts = (
    user     => "test",
    password => "tset",
    host     => "127.0.0.1",
    port     => $port,

);
my $api = MikroTik::Client->new(%client_opts, tls => 0);

# Non-TLS connection to TLS server
$api->cmd("/resp");
ok $api->error eq "closed prematurely", "server requires TSL";
$api->tls(1);

# TLS without certs
$api->cmd("/resp");
ok $! == EPROTO, "can't negotiate TLS";
ok $api->error, "has error";

# TLS certs without CA
$api->cert("./t/certs/client.crt");
$api->key("./t/certs/client.key");
$api->cmd("/resp");
ok $! == EPROTO, "can't negotiate TLS";
ok $api->error, "has error";

# Insecure TLS
$api->insecure(1);
my $res = $api->cmd("/resp");
is_deeply $res, _gen_result(), 'right result';
ok !$api->error, 'no error';

# TLS certs with CA
$api = MikroTik::Client->new(
    %client_opts,
    tls  => 1,
    ca   => "./t/certs/ca.crt",
    cert => "./t/certs/client.crt",
    key  => "./t/certs/client.key"
);
$res = $api->cmd("/resp");
is_deeply $res, _gen_result(), 'right result';
ok !$api->error, 'no error';

# TLS certs bundle
$api = MikroTik::Client->new(
    %client_opts,
    tls  => 1,
    ca   => "./t/certs/ca.crt",
    cert => "./t/certs/client-bundle.crt",
);
$res = $api->cmd("/resp");
is_deeply $res, _gen_result(), 'right result';
ok !$api->error, 'no error';

done_testing();

sub _gen_result {
    my $attr = MikroTik::Client::Mockup::_gen_attr(@_);
    return [$attr, $attr];
}


