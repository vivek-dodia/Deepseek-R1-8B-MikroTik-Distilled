# Repository Information
Name: mikrotik-auto-wireguard

# Directory Structure
Directory structure:
└── github_repos/mikrotik-auto-wireguard/
    ├── .dockerignore
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
    │   │       ├── pack-c1a06d16f88384d840cb56f3de11046c1c2dbcf3.idx
    │   │       └── pack-c1a06d16f88384d840cb56f3de11046c1c2dbcf3.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .tools/
    │   └── PhpStan/
    │       └── console-application.php
    ├── bin/
    │   └── console
    ├── composer.json
    ├── composer.lock
    ├── config/
    │   └── services.php
    ├── Dockerfile
    ├── docs/
    │   ├── EXAMPLES.md
    │   └── README.md
    ├── LICENSE
    ├── phpcs.xml.dist
    ├── phpstan.src.neon
    ├── README.md
    ├── resources/
    │   └── template/
    │       ├── advanced.twig
    │       └── text.twig
    ├── src/
    │   ├── Command/
    │   │   └── GenerateCommand.php
    │   ├── ContainerProvider.php
    │   ├── Exception/
    │   │   ├── InvalidArgumentException.php
    │   │   ├── InvalidFieldException.php
    │   │   ├── LogicException.php
    │   │   ├── MissingValueException.php
    │   │   ├── ROSException.php
    │   │   ├── SectionAlreadyExistsException.php
    │   │   └── UnderflowException.php
    │   ├── Factory/
    │   │   └── ROSClientFactory.php
    │   ├── NetworkUtil.php
    │   ├── RouterOS/
    │   │   ├── AbstractApi.php
    │   │   ├── ClientProvider.php
    │   │   ├── IpApi.php
    │   │   ├── ROSUtil.php
    │   │   └── WireGuardApi.php
    │   ├── Struct/
    │   │   ├── InterfaceInterface.php
    │   │   ├── Peer.php
    │   │   ├── ROSStructHelperTrait.php
    │   │   └── WireguardInterface.php
    │   ├── UseCase/
    │   │   ├── AddNewPeers.php
    │   │   └── BuildClientConfiguration.php
    │   └── WireGuard/
    │       ├── Configuration/
    │       │   ├── AbstractSection.php
    │       │   ├── Configuration.php
    │       │   ├── ConfigurationSection.php
    │       │   ├── InterfaceSection.php
    │       │   ├── PeerProjector.php
    │       │   ├── PeerSection.php
    │       │   └── RenderableInterface.php
    │       ├── KeyGenerator.php
    │       └── QrGenerator.php
    └── tests/
        └── .gitkeep


# Content
File: /.dockerignore
var/cache/*
vendor/*


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/kiler129/mikrotik-auto-wireguard.git
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
0000000000000000000000000000000000000000 6e9601bc8bac5cdda0ec3be737573256865c5b72 vivek-dodia <vivek.dodia@icloud.com> 1738605957 -0500	clone: from https://github.com/kiler129/mikrotik-auto-wireguard.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 6e9601bc8bac5cdda0ec3be737573256865c5b72 vivek-dodia <vivek.dodia@icloud.com> 1738605957 -0500	clone: from https://github.com/kiler129/mikrotik-auto-wireguard.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 6e9601bc8bac5cdda0ec3be737573256865c5b72 vivek-dodia <vivek.dodia@icloud.com> 1738605957 -0500	clone: from https://github.com/kiler129/mikrotik-auto-wireguard.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0ff83a6eae930c47149e98f201b6eeeaf7466da6 refs/remotes/origin/dependabot/composer/phpseclib/phpseclib-2.0.41
a04a3f761d9c8ccb2da79b10fe134d4444fcfef6 refs/remotes/origin/dependabot/composer/twig/twig-3.4.3
1b2abe996b683f932ef984e48b1ce787ce33ddd3 refs/remotes/origin/issue-4-add-php8-support
eb7f3d70fdde4de8fd923e8cf7dafef07658df49 refs/remotes/origin/kolorafa-patch-1
6e9601bc8bac5cdda0ec3be737573256865c5b72 refs/remotes/origin/master
a6024344394c121f24f8cd3f8c3a79e28384df52 refs/remotes/origin/modify-endpoint-for-v71b3


File: /.git\refs\heads\master
6e9601bc8bac5cdda0ec3be737573256865c5b72


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.tools\PhpStan\console-application.php
<?php
declare(strict_types=1);

require __DIR__ . '/../../vendor/autoload.php';

use NoFlash\ROSAutoWireGuard\ContainerProvider;
use Symfony\Component\Console\Application;

$container = ContainerProvider::getAppContainer();
return new Application();



File: /bin\console
#!/usr/bin/env php
<?php
declare(strict_types=1);

require __DIR__ . '/../vendor/autoload.php';

use NoFlash\ROSAutoWireGuard\Command\GenerateCommand;
use NoFlash\ROSAutoWireGuard\ContainerProvider;
use Symfony\Component\Console\Application;

$container = ContainerProvider::getAppContainer();
$application = new Application('MikroTik Auto WireGuard', 'v0.2');
$application->addCommands([$container->get(GenerateCommand::class)]);

$application->run();


File: /composer.json
{
    "require": {
        "php": "^7.4|^8.0",
        "ext-sodium": "*",
        "evilfreelancer/routeros-api-php": "^1.4",
        "endroid/qr-code": "^3.9",
        "symfony/console": "^5.1",
        "s1lentium/iptools": "^1.1",
        "symfony/dependency-injection": "^5.1",
        "symfony/config": "^5.1",
        "twig/twig": "^3.0",
        "symfony/proxy-manager-bridge": "^5.1"
    },
    "require-dev": {
        "roave/security-advisories": "dev-master",
        "symfony/var-dumper": "^5.1",
        "object-calisthenics/phpcs-calisthenics-rules": "^3.9",
        "phpstan/phpstan": "^0.12.42",
        "phpstan/phpstan-deprecation-rules": "^0.12.5",
        "phpstan/phpstan-strict-rules": "^0.12.5",
        "phpstan/phpstan-symfony": "^0.12.7",
        "slevomat/coding-standard": "^6.4",
        "sllh/composer-versions-check": "dev-php-8",
        "squizlabs/php_codesniffer": "^3.5"
    },
    "autoload": {
        "psr-4": {
            "NoFlash\\ROSAutoWireGuard\\": "src/"
        }
    },
    "scripts": {
        "check-code-quality": [
            "vendor/bin/phpcs --standard=phpcs.xml.dist --extensions=php ./src",
            "vendor/bin/phpstan analyse src -c phpstan.src.neon"
        ],
        "fix-cs": [
            "vendor/bin/phpcbf --standard=phpcs.xml.dist"
        ],
        "lint": [
            "@composer validate --strict",
            "bin/console lint:yaml config/"
        ]
    },
    "repositories": [
    ]
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "f28a523eada52b19cc17773e21012e67",
    "packages": [
        {
            "name": "bacon/bacon-qr-code",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/Bacon/BaconQrCode.git",
                "reference": "3e9d791b67d0a2912922b7b7c7312f4b37af41e4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Bacon/BaconQrCode/zipball/3e9d791b67d0a2912922b7b7c7312f4b37af41e4",
                "reference": "3e9d791b67d0a2912922b7b7c7312f4b37af41e4",
                "shasum": ""
            },
            "require": {
                "dasprid/enum": "^1.0.3",
                "ext-iconv": "*",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "phly/keep-a-changelog": "^1.4",
                "phpunit/phpunit": "^7 | ^8 | ^9",
                "squizlabs/php_codesniffer": "^3.4"
            },
            "suggest": {
                "ext-imagick": "to generate QR code images"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "BaconQrCode\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "authors": [
                {
                    "name": "Ben Scholzen 'DASPRiD'",
                    "email": "mail@dasprids.de",
                    "homepage": "https://dasprids.de/",
                    "role": "Developer"
                }
            ],
            "description": "BaconQrCode is a QR code generator for PHP.",
            "homepage": "https://github.com/Bacon/BaconQrCode",
            "support": {
                "issues": "https://github.com/Bacon/BaconQrCode/issues",
                "source": "https://github.com/Bacon/BaconQrCode/tree/2.0.3"
            },
            "time": "2020-10-30T02:02:47+00:00"
        },
        {
            "name": "composer/package-versions-deprecated",
            "version": "1.11.99.1",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/package-versions-deprecated.git",
                "reference": "7413f0b55a051e89485c5cb9f765fe24bb02a7b6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/package-versions-deprecated/zipball/7413f0b55a051e89485c5cb9f765fe24bb02a7b6",
                "reference": "7413f0b55a051e89485c5cb9f765fe24bb02a7b6",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.1.0 || ^2.0",
                "php": "^7 || ^8"
            },
            "replace": {
                "ocramius/package-versions": "1.11.99"
            },
            "require-dev": {
                "composer/composer": "^1.9.3 || ^2.0@dev",
                "ext-zip": "^1.13",
                "phpunit/phpunit": "^6.5 || ^7"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "PackageVersions\\Installer",
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PackageVersions\\": "src/PackageVersions"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                },
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be"
                }
            ],
            "description": "Composer plugin that provides efficient querying for installed package versions (no runtime IO)",
            "support": {
                "issues": "https://github.com/composer/package-versions-deprecated/issues",
                "source": "https://github.com/composer/package-versions-deprecated/tree/1.11.99.1"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-11T10:22:58+00:00"
        },
        {
            "name": "dasprid/enum",
            "version": "1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/DASPRiD/Enum.git",
                "reference": "5abf82f213618696dda8e3bf6f64dd042d8542b2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/DASPRiD/Enum/zipball/5abf82f213618696dda8e3bf6f64dd042d8542b2",
                "reference": "5abf82f213618696dda8e3bf6f64dd042d8542b2",
                "shasum": ""
            },
            "require-dev": {
                "phpunit/phpunit": "^7 | ^8 | ^9",
                "squizlabs/php_codesniffer": "^3.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DASPRiD\\Enum\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "authors": [
                {
                    "name": "Ben Scholzen 'DASPRiD'",
                    "email": "mail@dasprids.de",
                    "homepage": "https://dasprids.de/",
                    "role": "Developer"
                }
            ],
            "description": "PHP 7.1 enum implementation",
            "keywords": [
                "enum",
                "map"
            ],
            "support": {
                "issues": "https://github.com/DASPRiD/Enum/issues",
                "source": "https://github.com/DASPRiD/Enum/tree/1.0.3"
            },
            "time": "2020-10-02T16:03:48+00:00"
        },
        {
            "name": "divineomega/php-ssh-connection",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/DivineOmega/php-ssh-connection.git",
                "reference": "d6c8326cf376777df828372e494dc1b6a1be2a89"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/DivineOmega/php-ssh-connection/zipball/d6c8326cf376777df828372e494dc1b6a1be2a89",
                "reference": "d6c8326cf376777df828372e494dc1b6a1be2a89",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1",
                "phpseclib/phpseclib": "^2.0"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.0",
                "phpunit/phpunit": "^7.0||^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DivineOmega\\SSHConnection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-3.0-only"
            ],
            "authors": [
                {
                    "name": "Jordan Hall",
                    "email": "jordan@hall05.co.uk"
                }
            ],
            "description": "Provides an elegant syntax to connect to SSH servers and execute commands.",
            "support": {
                "issues": "https://github.com/DivineOmega/php-ssh-connection/issues",
                "source": "https://github.com/DivineOmega/php-ssh-connection/tree/v2.2.0"
            },
            "time": "2020-05-27T22:58:17+00:00"
        },
        {
            "name": "endroid/qr-code",
            "version": "3.9.6",
            "source": {
                "type": "git",
                "url": "https://github.com/endroid/qr-code.git",
                "reference": "9cdd4f5d609bfc8811ca4a62b4d23eb16976242f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/endroid/qr-code/zipball/9cdd4f5d609bfc8811ca4a62b4d23eb16976242f",
                "reference": "9cdd4f5d609bfc8811ca4a62b4d23eb16976242f",
                "shasum": ""
            },
            "require": {
                "bacon/bacon-qr-code": "^2.0",
                "khanamiryan/qrcode-detector-decoder": "^1.0.2",
                "myclabs/php-enum": "^1.5",
                "php": ">=7.2",
                "symfony/options-resolver": "^3.4||^4.4||^5.0",
                "symfony/property-access": "^3.4||^4.4||^5.0"
            },
            "require-dev": {
                "endroid/quality": "^1.3.7",
                "setasign/fpdf": "^1.8"
            },
            "suggest": {
                "ext-gd": "Required for generating PNG images",
                "roave/security-advisories": "Avoids installation of package versions with vulnerabilities",
                "setasign/fpdf": "Required to use the FPDF writer.",
                "symfony/security-checker": "Checks your composer.lock for vulnerabilities"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Endroid\\QrCode\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeroen van den Enden",
                    "email": "info@endroid.nl"
                }
            ],
            "description": "Endroid QR Code",
            "homepage": "https://github.com/endroid/qr-code",
            "keywords": [
                "bundle",
                "code",
                "endroid",
                "php",
                "qr",
                "qrcode"
            ],
            "support": {
                "issues": "https://github.com/endroid/qr-code/issues",
                "source": "https://github.com/endroid/qr-code/tree/3.9.6"
            },
            "funding": [
                {
                    "url": "https://github.com/endroid",
                    "type": "github"
                }
            ],
            "time": "2020-11-27T14:30:38+00:00"
        },
        {
            "name": "evilfreelancer/routeros-api-php",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/EvilFreelancer/routeros-api-php.git",
                "reference": "dd687894add2bc82c6db6b903022329a3db07641"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/EvilFreelancer/routeros-api-php/zipball/dd687894add2bc82c6db6b903022329a3db07641",
                "reference": "dd687894add2bc82c6db6b903022329a3db07641",
                "shasum": ""
            },
            "require": {
                "divineomega/php-ssh-connection": "^2.2",
                "ext-sockets": "*",
                "php": "^7.2|^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^2.16",
                "larapack/dd": "^1.1",
                "limedeck/phpunit-detailed-printer": "^5.0",
                "orchestra/testbench": "^4.0|^5.0",
                "phpunit/phpunit": "^8.0",
                "rector/rector": "^0.7|^0.8|^0.9",
                "roave/security-advisories": "dev-master",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "laravel": {
                    "providers": [
                        "RouterOS\\Laravel\\ServiceProvider"
                    ],
                    "aliases": {
                        "RouterOS": "RouterOS\\Laravel\\Facade"
                    }
                }
            },
            "autoload": {
                "psr-4": {
                    "RouterOS\\": "./src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paul Rock",
                    "email": "paul@drteam.rocks",
                    "homepage": "http://drteam.rocks/",
                    "role": "Developer"
                }
            ],
            "description": "Modern Mikrotik RouterOS API PHP client for your applications (with Laravel support)",
            "keywords": [
                "PSR-4",
                "facade",
                "laravel",
                "mikrotik",
                "plugin",
                "routeros",
                "socket-client"
            ],
            "support": {
                "issues": "https://github.com/EvilFreelancer/routeros-api-php/issues",
                "source": "https://github.com/EvilFreelancer/routeros-api-php/tree/1.4.0"
            },
            "funding": [
                {
                    "url": "https://streamlabs.com/evilfreelancer/tip",
                    "type": "custom"
                },
                {
                    "url": "https://www.donationalerts.com/r/evilfreelancer",
                    "type": "custom"
                },
                {
                    "url": "https://ko-fi.com/efreelancer",
                    "type": "ko_fi"
                },
                {
                    "url": "https://www.patreon.com/efreelancer",
                    "type": "patreon"
                }
            ],
            "time": "2021-01-30T14:29:35+00:00"
        },
        {
            "name": "friendsofphp/proxy-manager-lts",
            "version": "v1.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfPHP/proxy-manager-lts.git",
                "reference": "121af47c9aee9c03031bdeca3fac0540f59aa5c3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfPHP/proxy-manager-lts/zipball/121af47c9aee9c03031bdeca3fac0540f59aa5c3",
                "reference": "121af47c9aee9c03031bdeca3fac0540f59aa5c3",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-code": "~3.4.1|^4.0",
                "php": ">=7.1",
                "symfony/filesystem": "^4.4.17|^5.0"
            },
            "conflict": {
                "laminas/laminas-stdlib": "<3.2.1",
                "zendframework/zend-stdlib": "<3.2.1"
            },
            "replace": {
                "ocramius/proxy-manager": "^2.1"
            },
            "require-dev": {
                "ext-phar": "*",
                "symfony/phpunit-bridge": "^5.2"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "ocramius/proxy-manager",
                    "url": "https://github.com/Ocramius/ProxyManager"
                }
            },
            "autoload": {
                "psr-4": {
                    "ProxyManager\\": "src/ProxyManager"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "http://ocramius.github.io/"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                }
            ],
            "description": "Adding support for a wider range of PHP versions to ocramius/proxy-manager",
            "homepage": "https://github.com/FriendsOfPHP/proxy-manager-lts",
            "keywords": [
                "aop",
                "lazy loading",
                "proxy",
                "proxy pattern",
                "service proxies"
            ],
            "support": {
                "issues": "https://github.com/FriendsOfPHP/proxy-manager-lts/issues",
                "source": "https://github.com/FriendsOfPHP/proxy-manager-lts/tree/v1.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/Ocramius",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ocramius/proxy-manager",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-14T21:52:44+00:00"
        },
        {
            "name": "khanamiryan/qrcode-detector-decoder",
            "version": "1.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/khanamiryan/php-qrcode-detector-decoder.git",
                "reference": "07fceefb79d895e858e52921afb9c1433d2f3d5e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/khanamiryan/php-qrcode-detector-decoder/zipball/07fceefb79d895e858e52921afb9c1433d2f3d5e",
                "reference": "07fceefb79d895e858e52921afb9c1433d2f3d5e",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Zxing\\": "lib/"
                },
                "files": [
                    "lib/Common/customFunctions.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ashot Khanamiryan",
                    "email": "a.khanamiryan@gmail.com",
                    "homepage": "https://github.com/khanamiryan",
                    "role": "Developer"
                }
            ],
            "description": "QR code decoder / reader",
            "homepage": "https://github.com/khanamiryan/php-qrcode-detector-decoder/",
            "keywords": [
                "barcode",
                "qr",
                "zxing"
            ],
            "support": {
                "issues": "https://github.com/khanamiryan/php-qrcode-detector-decoder/issues",
                "source": "https://github.com/khanamiryan/php-qrcode-detector-decoder/tree/1.0.4"
            },
            "time": "2020-11-29T18:50:26+00:00"
        },
        {
            "name": "laminas/laminas-code",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-code.git",
                "reference": "28a6d70ea8b8bca687d7163300e611ae33baf82a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-code/zipball/28a6d70ea8b8bca687d7163300e611ae33baf82a",
                "reference": "28a6d70ea8b8bca687d7163300e611ae33baf82a",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-eventmanager": "^3.3",
                "php": "^7.4 || ~8.0.0"
            },
            "conflict": {
                "phpspec/prophecy": "<1.9.0"
            },
            "replace": {
                "zendframework/zend-code": "self.version"
            },
            "require-dev": {
                "doctrine/annotations": "^1.10.4",
                "ext-phar": "*",
                "laminas/laminas-coding-standard": "^2.1.4",
                "laminas/laminas-stdlib": "^3.3.0",
                "phpunit/phpunit": "^9.4.2",
                "psalm/plugin-phpunit": "^0.14.0",
                "vimeo/psalm": "^4.3.1"
            },
            "suggest": {
                "doctrine/annotations": "Doctrine\\Common\\Annotations >=1.0 for annotation features",
                "laminas/laminas-stdlib": "Laminas\\Stdlib component",
                "laminas/laminas-zendframework-bridge": "A bridge with Zend Framework"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Laminas\\Code\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Extensions to the PHP Reflection API, static code scanning, and code generation",
            "homepage": "https://laminas.dev",
            "keywords": [
                "code",
                "laminas",
                "laminasframework"
            ],
            "support": {
                "chat": "https://laminas.dev/chat",
                "docs": "https://docs.laminas.dev/laminas-code/",
                "forum": "https://discourse.laminas.dev",
                "issues": "https://github.com/laminas/laminas-code/issues",
                "rss": "https://github.com/laminas/laminas-code/releases.atom",
                "source": "https://github.com/laminas/laminas-code"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-12-30T16:16:14+00:00"
        },
        {
            "name": "laminas/laminas-eventmanager",
            "version": "3.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-eventmanager.git",
                "reference": "1940ccf30e058b2fd66f5a9d696f1b5e0027b082"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-eventmanager/zipball/1940ccf30e058b2fd66f5a9d696f1b5e0027b082",
                "reference": "1940ccf30e058b2fd66f5a9d696f1b5e0027b082",
                "shasum": ""
            },
            "require": {
                "laminas/laminas-zendframework-bridge": "^1.0",
                "php": "^7.3 || ^8.0"
            },
            "replace": {
                "zendframework/zend-eventmanager": "^3.2.1"
            },
            "require-dev": {
                "container-interop/container-interop": "^1.1",
                "laminas/laminas-coding-standard": "~1.0.0",
                "laminas/laminas-stdlib": "^2.7.3 || ^3.0",
                "phpbench/phpbench": "^0.17.1",
                "phpunit/phpunit": "^8.5.8"
            },
            "suggest": {
                "container-interop/container-interop": "^1.1, to use the lazy listeners feature",
                "laminas/laminas-stdlib": "^2.7.3 || ^3.0, to use the FilterChain feature"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.3.x-dev",
                    "dev-develop": "3.4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Laminas\\EventManager\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Trigger and listen to events within a PHP application",
            "homepage": "https://laminas.dev",
            "keywords": [
                "event",
                "eventmanager",
                "events",
                "laminas"
            ],
            "support": {
                "chat": "https://laminas.dev/chat",
                "docs": "https://docs.laminas.dev/laminas-eventmanager/",
                "forum": "https://discourse.laminas.dev",
                "issues": "https://github.com/laminas/laminas-eventmanager/issues",
                "rss": "https://github.com/laminas/laminas-eventmanager/releases.atom",
                "source": "https://github.com/laminas/laminas-eventmanager"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-08-25T11:10:44+00:00"
        },
        {
            "name": "laminas/laminas-zendframework-bridge",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-zendframework-bridge.git",
                "reference": "6ede70583e101030bcace4dcddd648f760ddf642"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-zendframework-bridge/zipball/6ede70583e101030bcace4dcddd648f760ddf642",
                "reference": "6ede70583e101030bcace4dcddd648f760ddf642",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.7 || ^6.5 || ^7.5 || ^8.1 || ^9.3",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "type": "library",
            "extra": {
                "laminas": {
                    "module": "Laminas\\ZendFrameworkBridge"
                }
            },
            "autoload": {
                "files": [
                    "src/autoload.php"
                ],
                "psr-4": {
                    "Laminas\\ZendFrameworkBridge\\": "src//"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Alias legacy ZF class names to Laminas Project equivalents.",
            "keywords": [
                "ZendFramework",
                "autoloading",
                "laminas",
                "zf"
            ],
            "support": {
                "forum": "https://discourse.laminas.dev/",
                "issues": "https://github.com/laminas/laminas-zendframework-bridge/issues",
                "rss": "https://github.com/laminas/laminas-zendframework-bridge/releases.atom",
                "source": "https://github.com/laminas/laminas-zendframework-bridge"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2020-09-14T14:23:00+00:00"
        },
        {
            "name": "myclabs/php-enum",
            "version": "1.7.7",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/php-enum.git",
                "reference": "d178027d1e679832db9f38248fcc7200647dc2b7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/php-enum/zipball/d178027d1e679832db9f38248fcc7200647dc2b7",
                "reference": "d178027d1e679832db9f38248fcc7200647dc2b7",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": ">=7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7",
                "squizlabs/php_codesniffer": "1.*",
                "vimeo/psalm": "^3.8"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "MyCLabs\\Enum\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP Enum contributors",
                    "homepage": "https://github.com/myclabs/php-enum/graphs/contributors"
                }
            ],
            "description": "PHP Enum implementation",
            "homepage": "http://github.com/myclabs/php-enum",
            "keywords": [
                "enum"
            ],
            "support": {
                "issues": "https://github.com/myclabs/php-enum/issues",
                "source": "https://github.com/myclabs/php-enum/tree/1.7.7"
            },
            "funding": [
                {
                    "url": "https://github.com/mnapoli",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/php-enum",
                    "type": "tidelift"
                }
            ],
            "time": "2020-11-14T18:14:52+00:00"
        },
        {
            "name": "phpseclib/phpseclib",
            "version": "2.0.30",
            "source": {
                "type": "git",
                "url": "https://github.com/phpseclib/phpseclib.git",
                "reference": "136b9ca7eebef78be14abf90d65c5e57b6bc5d36"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpseclib/phpseclib/zipball/136b9ca7eebef78be14abf90d65c5e57b6bc5d36",
                "reference": "136b9ca7eebef78be14abf90d65c5e57b6bc5d36",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phing/phing": "~2.7",
                "phpunit/phpunit": "^4.8.35|^5.7|^6.0|^9.4",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "suggest": {
                "ext-gmp": "Install the GMP (GNU Multiple Precision) extension in order to speed up arbitrary precision integer arithmetic operations.",
                "ext-libsodium": "SSH2/SFTP can make use of some algorithms provided by the libsodium-php extension.",
                "ext-mcrypt": "Install the Mcrypt extension in order to speed up a few other cryptographic operations.",
                "ext-openssl": "Install the OpenSSL extension in order to speed up a wide variety of cryptographic operations."
            },
            "type": "library",
            "autoload": {
                "files": [
                    "phpseclib/bootstrap.php"
                ],
                "psr-4": {
                    "phpseclib\\": "phpseclib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jim Wigginton",
                    "email": "terrafrost@php.net",
                    "role": "Lead Developer"
                },
                {
                    "name": "Patrick Monnerat",
                    "email": "pm@datasphere.ch",
                    "role": "Developer"
                },
                {
                    "name": "Andreas Fischer",
                    "email": "bantu@phpbb.com",
                    "role": "Developer"
                },
                {
                    "name": "Hans-Jürgen Petrich",
                    "email": "petrich@tronic-media.com",
                    "role": "Developer"
                },
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com",
                    "role": "Developer"
                }
            ],
            "description": "PHP Secure Communications Library - Pure-PHP implementations of RSA, AES, SSH2, SFTP, X.509 etc.",
            "homepage": "http://phpseclib.sourceforge.net",
            "keywords": [
                "BigInteger",
                "aes",
                "asn.1",
                "asn1",
                "blowfish",
                "crypto",
                "cryptography",
                "encryption",
                "rsa",
                "security",
                "sftp",
                "signature",
                "signing",
                "ssh",
                "twofish",
                "x.509",
                "x509"
            ],
            "support": {
                "issues": "https://github.com/phpseclib/phpseclib/issues",
                "source": "https://github.com/phpseclib/phpseclib/tree/2.0.30"
            },
            "funding": [
                {
                    "url": "https://github.com/terrafrost",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/phpseclib",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpseclib/phpseclib",
                    "type": "tidelift"
                }
            ],
            "time": "2020-12-17T05:42:04+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/master"
            },
            "time": "2017-02-14T16:28:37+00:00"
        },
        {
            "name": "s1lentium/iptools",
            "version": "v1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/S1lentium/IPTools.git",
                "reference": "f6f8ab6132ca7443bd7cced1681f5066d725fd5f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/S1lentium/IPTools/zipball/f6f8ab6132ca7443bd7cced1681f5066d725fd5f",
                "reference": "f6f8ab6132ca7443bd7cced1681f5066d725fd5f",
                "shasum": ""
            },
            "require": {
                "ext-bcmath": "*",
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0",
                "satooshi/php-coveralls": "~1.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "IPTools\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Safarov Alisher",
                    "email": "alisher.safarov@outlook.com",
                    "homepage": "https://github.com/S1lentium"
                }
            ],
            "description": "PHP Library for manipulating network addresses (IPv4 and IPv6)",
            "keywords": [
                "IP",
                "IP-Tools",
                "cidr",
                "ipv4",
                "ipv6",
                "network",
                "subnet"
            ],
            "support": {
                "issues": "https://github.com/S1lentium/IPTools/issues",
                "source": "https://github.com/S1lentium/IPTools/tree/master"
            },
            "time": "2018-09-19T06:15:53+00:00"
        },
        {
            "name": "symfony/config",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/config.git",
                "reference": "50e0e1314a3b2609d32b6a5a0d0fb5342494c4ab"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/config/zipball/50e0e1314a3b2609d32b6a5a0d0fb5342494c4ab",
                "reference": "50e0e1314a3b2609d32b6a5a0d0fb5342494c4ab",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/filesystem": "^4.4|^5.0",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "symfony/finder": "<4.4"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/finder": "^4.4|^5.0",
                "symfony/messenger": "^4.4|^5.0",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/yaml": "To use the yaml reference dumper"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Config\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Helps you find, load, combine, autofill and validate configuration values of any kind",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/config/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:15:41+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "89d4b176d12a2946a1ae4e34906a025b7b6b135a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/89d4b176d12a2946a1ae4e34906a025b7b6b135a",
                "reference": "89d4b176d12a2946a1ae4e34906a025b7b6b135a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php73": "^1.8",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1|^2",
                "symfony/string": "^5.1"
            },
            "conflict": {
                "symfony/dependency-injection": "<4.4",
                "symfony/dotenv": "<5.1",
                "symfony/event-dispatcher": "<4.4",
                "symfony/lock": "<4.4",
                "symfony/process": "<4.4"
            },
            "provide": {
                "psr/log-implementation": "1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/event-dispatcher": "^4.4|^5.0",
                "symfony/lock": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "symfony/var-dumper": "^4.4|^5.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/lock": "",
                "symfony/process": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Eases the creation of beautiful and testable command line interfaces",
            "homepage": "https://symfony.com",
            "keywords": [
                "cli",
                "command line",
                "console",
                "terminal"
            ],
            "support": {
                "source": "https://github.com/symfony/console/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-28T22:06:19+00:00"
        },
        {
            "name": "symfony/dependency-injection",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dependency-injection.git",
                "reference": "62f72187be689540385dce6c68a5d4c16f034139"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dependency-injection/zipball/62f72187be689540385dce6c68a5d4c16f034139",
                "reference": "62f72187be689540385dce6c68a5d4c16f034139",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.0",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.15",
                "symfony/service-contracts": "^1.1.6|^2"
            },
            "conflict": {
                "symfony/config": "<5.1",
                "symfony/finder": "<4.4",
                "symfony/proxy-manager-bridge": "<4.4",
                "symfony/yaml": "<4.4"
            },
            "provide": {
                "psr/container-implementation": "1.0",
                "symfony/service-implementation": "1.0"
            },
            "require-dev": {
                "symfony/config": "^5.1",
                "symfony/expression-language": "^4.4|^5.0",
                "symfony/yaml": "^4.4|^5.0"
            },
            "suggest": {
                "symfony/config": "",
                "symfony/expression-language": "For using expressions in service container configuration",
                "symfony/finder": "For using double-star glob patterns or when GLOB_BRACE portability is required",
                "symfony/proxy-manager-bridge": "Generate service proxies to lazy load them",
                "symfony/yaml": ""
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DependencyInjection\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Allows you to standardize and centralize the way objects are constructed in your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dependency-injection/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T12:56:27+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "5fa56b4074d1ae755beb55617ddafe6f5d78f665"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/5fa56b4074d1ae755beb55617ddafe6f5d78f665",
                "reference": "5fa56b4074d1ae755beb55617ddafe6f5d78f665",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/master"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/filesystem",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/filesystem.git",
                "reference": "262d033b57c73e8b59cd6e68a45c528318b15038"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/filesystem/zipball/262d033b57c73e8b59cd6e68a45c528318b15038",
                "reference": "262d033b57c73e8b59cd6e68a45c528318b15038",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Filesystem\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides basic utilities for the filesystem",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/filesystem/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:01:46+00:00"
        },
        {
            "name": "symfony/options-resolver",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/options-resolver.git",
                "reference": "5d0f633f9bbfcf7ec642a2b5037268e61b0a62ce"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/options-resolver/zipball/5d0f633f9bbfcf7ec642a2b5037268e61b0a62ce",
                "reference": "5d0f633f9bbfcf7ec642a2b5037268e61b0a62ce",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php73": "~1.0",
                "symfony/polyfill-php80": "^1.15"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\OptionsResolver\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides an improved replacement for the array_replace PHP function",
            "homepage": "https://symfony.com",
            "keywords": [
                "config",
                "configuration",
                "options"
            ],
            "support": {
                "source": "https://github.com/symfony/options-resolver/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T12:56:27+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "c6c942b1ac76c82448322025e084cadc56048b4e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/c6c942b1ac76c82448322025e084cadc56048b4e",
                "reference": "c6c942b1ac76c82448322025e084cadc56048b4e",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Ctype\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for ctype functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "ctype",
                "polyfill",
                "portable"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-ctype/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "267a9adeb8ecb8071040a740930e077cdfb987af"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/267a9adeb8ecb8071040a740930e077cdfb987af",
                "reference": "267a9adeb8ecb8071040a740930e077cdfb987af",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Grapheme\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's grapheme_* functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "grapheme",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "6e971c891537eb617a00bb07a43d182a6915faba"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/6e971c891537eb617a00bb07a43d182a6915faba",
                "reference": "6e971c891537eb617a00bb07a43d182a6915faba",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T17:09:11+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "f377a3dd1fde44d37b9831d68dc8dea3ffd28e13"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/f377a3dd1fde44d37b9831d68dc8dea3ffd28e13",
                "reference": "f377a3dd1fde44d37b9831d68dc8dea3ffd28e13",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-php73",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php73.git",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php73/zipball/a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "reference": "a678b42e92f86eca04b7fa4c0f6f19d097fb69e2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php73\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php73/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.22.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "reference": "dc3063ba22c2a1fd2f45ed856374d79114998f91",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "1.22-dev"
                },
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.22.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-07T16:49:33+00:00"
        },
        {
            "name": "symfony/property-access",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-access.git",
                "reference": "3af8ed262bd3217512a13b023981fe68f36ad5f3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-access/zipball/3af8ed262bd3217512a13b023981fe68f36ad5f3",
                "reference": "3af8ed262bd3217512a13b023981fe68f36ad5f3",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.15",
                "symfony/property-info": "^5.2"
            },
            "require-dev": {
                "symfony/cache": "^4.4|^5.0"
            },
            "suggest": {
                "psr/cache-implementation": "To cache access methods."
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyAccess\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides functions to read and write from/to an object or array using a simple string notation",
            "homepage": "https://symfony.com",
            "keywords": [
                "access",
                "array",
                "extraction",
                "index",
                "injection",
                "object",
                "property",
                "property path",
                "reflection"
            ],
            "support": {
                "source": "https://github.com/symfony/property-access/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:15:41+00:00"
        },
        {
            "name": "symfony/property-info",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-info.git",
                "reference": "4e4f368c3737b1c175d66f4fc0b99a5bcd161a77"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-info/zipball/4e4f368c3737b1c175d66f4fc0b99a5bcd161a77",
                "reference": "4e4f368c3737b1c175d66f4fc0b99a5bcd161a77",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.1",
                "symfony/polyfill-php80": "^1.15",
                "symfony/string": "^5.1"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "symfony/dependency-injection": "<4.4"
            },
            "require-dev": {
                "doctrine/annotations": "^1.10.4",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/cache": "^4.4|^5.0",
                "symfony/dependency-injection": "^4.4|^5.0",
                "symfony/serializer": "^4.4|^5.0"
            },
            "suggest": {
                "phpdocumentor/reflection-docblock": "To use the PHPDoc",
                "psr/cache-implementation": "To cache results",
                "symfony/doctrine-bridge": "To use Doctrine metadata",
                "symfony/serializer": "To use Serializer metadata"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyInfo\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Kévin Dunglas",
                    "email": "dunglas@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Extracts information about PHP class' properties using metadata of popular sources",
            "homepage": "https://symfony.com",
            "keywords": [
                "doctrine",
                "phpdoc",
                "property",
                "symfony",
                "type",
                "validator"
            ],
            "support": {
                "source": "https://github.com/symfony/property-info/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:15:41+00:00"
        },
        {
            "name": "symfony/proxy-manager-bridge",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/proxy-manager-bridge.git",
                "reference": "fd6bb40190b1719abbe831be09adf38e0744d5f5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/proxy-manager-bridge/zipball/fd6bb40190b1719abbe831be09adf38e0744d5f5",
                "reference": "fd6bb40190b1719abbe831be09adf38e0744d5f5",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "^1.8",
                "friendsofphp/proxy-manager-lts": "^1.0.2",
                "php": ">=7.2.5",
                "symfony/dependency-injection": "^5.0"
            },
            "require-dev": {
                "symfony/config": "^4.4|^5.0"
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\ProxyManager\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides integration for ProxyManager with various Symfony components",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/proxy-manager-bridge/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:01:46+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "d15da7ba4957ffb8f1747218be9e1a121fd298a1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/d15da7ba4957ffb8f1747218be9e1a121fd298a1",
                "reference": "d15da7ba4957ffb8f1747218be9e1a121fd298a1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "psr/container": "^1.0"
            },
            "suggest": {
                "symfony/service-implementation": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/master"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2020-09-07T11:33:47+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "c95468897f408dd0aca2ff582074423dd0455122"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/c95468897f408dd0aca2ff582074423dd0455122",
                "reference": "c95468897f408dd0aca2ff582074423dd0455122",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.0",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "~1.15"
            },
            "require-dev": {
                "symfony/error-handler": "^4.4|^5.0",
                "symfony/http-client": "^4.4|^5.0",
                "symfony/translation-contracts": "^1.1|^2",
                "symfony/var-exporter": "^4.4|^5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\String\\": ""
                },
                "files": [
                    "Resources/functions.php"
                ],
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides an object-oriented API to strings and deals with bytes, UTF-8 code points and grapheme clusters in a unified way",
            "homepage": "https://symfony.com",
            "keywords": [
                "grapheme",
                "i18n",
                "string",
                "unicode",
                "utf-8",
                "utf8"
            ],
            "support": {
                "source": "https://github.com/symfony/string/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-25T15:14:59+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "f795ca686d38530045859b0350b5352f7d63447d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/f795ca686d38530045859b0350b5352f7d63447d",
                "reference": "f795ca686d38530045859b0350b5352f7d63447d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-mbstring": "^1.3"
            },
            "require-dev": {
                "psr/container": "^1.0",
                "symfony/phpunit-bridge": "^4.4.9|^5.0.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Twig\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com",
                    "homepage": "http://fabien.potencier.org",
                    "role": "Lead Developer"
                },
                {
                    "name": "Twig Team",
                    "role": "Contributors"
                },
                {
                    "name": "Armin Ronacher",
                    "email": "armin.ronacher@active-4.com",
                    "role": "Project Founder"
                }
            ],
            "description": "Twig, the flexible, fast, and secure template language for PHP",
            "homepage": "https://twig.symfony.com",
            "keywords": [
                "templating"
            ],
            "support": {
                "issues": "https://github.com/twigphp/Twig/issues",
                "source": "https://github.com/twigphp/Twig/tree/v3.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/twig/twig",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-05T15:40:36+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "dealerdirect/phpcodesniffer-composer-installer",
            "version": "v0.7.1",
            "source": {
                "type": "git",
                "url": "https://github.com/Dealerdirect/phpcodesniffer-composer-installer.git",
                "reference": "fe390591e0241955f22eb9ba327d137e501c771c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Dealerdirect/phpcodesniffer-composer-installer/zipball/fe390591e0241955f22eb9ba327d137e501c771c",
                "reference": "fe390591e0241955f22eb9ba327d137e501c771c",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.0 || ^2.0",
                "php": ">=5.3",
                "squizlabs/php_codesniffer": "^2.0 || ^3.0 || ^4.0"
            },
            "require-dev": {
                "composer/composer": "*",
                "phpcompatibility/php-compatibility": "^9.0",
                "sensiolabs/security-checker": "^4.1.0"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "Dealerdirect\\Composer\\Plugin\\Installers\\PHPCodeSniffer\\Plugin"
            },
            "autoload": {
                "psr-4": {
                    "Dealerdirect\\Composer\\Plugin\\Installers\\PHPCodeSniffer\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Franck Nijhof",
                    "email": "franck.nijhof@dealerdirect.com",
                    "homepage": "http://www.frenck.nl",
                    "role": "Developer / IT Manager"
                }
            ],
            "description": "PHP_CodeSniffer Standards Composer Installer Plugin",
            "homepage": "http://www.dealerdirect.com",
            "keywords": [
                "PHPCodeSniffer",
                "PHP_CodeSniffer",
                "code quality",
                "codesniffer",
                "composer",
                "installer",
                "phpcs",
                "plugin",
                "qa",
                "quality",
                "standard",
                "standards",
                "style guide",
                "stylecheck",
                "tests"
            ],
            "support": {
                "issues": "https://github.com/dealerdirect/phpcodesniffer-composer-installer/issues",
                "source": "https://github.com/dealerdirect/phpcodesniffer-composer-installer"
            },
            "time": "2020-12-07T18:04:37+00:00"
        },
        {
            "name": "nette/utils",
            "version": "v3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nette/utils.git",
                "reference": "2bc2f58079c920c2ecbb6935645abf6f2f5f94ba"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nette/utils/zipball/2bc2f58079c920c2ecbb6935645abf6f2f5f94ba",
                "reference": "2bc2f58079c920c2ecbb6935645abf6f2f5f94ba",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2 <8.1"
            },
            "conflict": {
                "nette/di": "<3.0.6"
            },
            "require-dev": {
                "nette/tester": "~2.0",
                "phpstan/phpstan": "^0.12",
                "tracy/tracy": "^2.3"
            },
            "suggest": {
                "ext-gd": "to use Image",
                "ext-iconv": "to use Strings::webalize(), toAscii(), chr() and reverse()",
                "ext-intl": "to use Strings::webalize(), toAscii(), normalize() and compare()",
                "ext-json": "to use Nette\\Utils\\Json",
                "ext-mbstring": "to use Strings::lower() etc...",
                "ext-tokenizer": "to use Nette\\Utils\\Reflection::getUseStatements()",
                "ext-xml": "to use Strings::length() etc. when mbstring is not available"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause",
                "GPL-2.0-only",
                "GPL-3.0-only"
            ],
            "authors": [
                {
                    "name": "David Grudl",
                    "homepage": "https://davidgrudl.com"
                },
                {
                    "name": "Nette Community",
                    "homepage": "https://nette.org/contributors"
                }
            ],
            "description": "🛠  Nette Utils: lightweight utilities for string & array manipulation, image handling, safe JSON encoding/decoding, validation, slug or strong password generating etc.",
            "homepage": "https://nette.org",
            "keywords": [
                "array",
                "core",
                "datetime",
                "images",
                "json",
                "nette",
                "paginator",
                "password",
                "slugify",
                "string",
                "unicode",
                "utf-8",
                "utility",
                "validation"
            ],
            "support": {
                "issues": "https://github.com/nette/utils/issues",
                "source": "https://github.com/nette/utils/tree/v3.2.1"
            },
            "time": "2021-01-11T03:05:59+00:00"
        },
        {
            "name": "object-calisthenics/phpcs-calisthenics-rules",
            "version": "v3.9.1",
            "source": {
                "type": "git",
                "url": "https://github.com/object-calisthenics/phpcs-calisthenics-rules.git",
                "reference": "6a4e66767138763839370273b47f1f9da6e0ee5a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/object-calisthenics/phpcs-calisthenics-rules/zipball/6a4e66767138763839370273b47f1f9da6e0ee5a",
                "reference": "6a4e66767138763839370273b47f1f9da6e0ee5a",
                "shasum": ""
            },
            "require": {
                "nette/utils": "^3.1",
                "php": "^7.4|^8.0",
                "slevomat/coding-standard": "^6.3",
                "squizlabs/php_codesniffer": "^3.5"
            },
            "require-dev": {
                "migrify/config-transformer": "^0.3.35",
                "phpstan/phpdoc-parser": "^0.4.9",
                "phpstan/phpstan": "^0.12.38",
                "phpunit/phpunit": "^9.3",
                "rector/rector": "^0.8.6",
                "symplify/changelog-linker": "^8.2",
                "symplify/coding-standard": "^8.2",
                "symplify/easy-coding-standard-tester": "^8.2",
                "symplify/phpstan-extensions": "^8.2",
                "tracy/tracy": "^2.7"
            },
            "type": "phpcodesniffer-standard",
            "autoload": {
                "psr-4": {
                    "ObjectCalisthenics\\": "src/ObjectCalisthenics"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHP CodeSniffer Object Calisthenics rules/sniffs",
            "support": {
                "issues": "https://github.com/object-calisthenics/phpcs-calisthenics-rules/issues",
                "source": "https://github.com/object-calisthenics/phpcs-calisthenics-rules/tree/master"
            },
            "abandoned": "symplify/phpstan-rules",
            "time": "2020-09-08T10:18:44+00:00"
        },
        {
            "name": "phpstan/phpdoc-parser",
            "version": "0.4.9",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpdoc-parser.git",
                "reference": "98a088b17966bdf6ee25c8a4b634df313d8aa531"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpdoc-parser/zipball/98a088b17966bdf6ee25c8a4b634df313d8aa531",
                "reference": "98a088b17966bdf6ee25c8a4b634df313d8aa531",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "consistence/coding-standard": "^3.5",
                "ergebnis/composer-normalize": "^2.0.2",
                "jakub-onderka/php-parallel-lint": "^0.9.2",
                "phing/phing": "^2.16.0",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^0.12.26",
                "phpstan/phpstan-strict-rules": "^0.12",
                "phpunit/phpunit": "^6.3",
                "slevomat/coding-standard": "^4.7.2",
                "symfony/process": "^4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\PhpDocParser\\": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPDoc parser with support for nullable, intersection and generic types",
            "support": {
                "issues": "https://github.com/phpstan/phpdoc-parser/issues",
                "source": "https://github.com/phpstan/phpdoc-parser/tree/master"
            },
            "time": "2020-08-03T20:32:43+00:00"
        },
        {
            "name": "phpstan/phpstan",
            "version": "0.12.71",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan.git",
                "reference": "d508fa3b0ecc5fc91ac70c6c7ac2862f968ba2b5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan/zipball/d508fa3b0ecc5fc91ac70c6c7ac2862f968ba2b5",
                "reference": "d508fa3b0ecc5fc91ac70c6c7ac2862f968ba2b5",
                "shasum": ""
            },
            "require": {
                "php": "^7.1|^8.0"
            },
            "conflict": {
                "phpstan/phpstan-shim": "*"
            },
            "bin": [
                "phpstan",
                "phpstan.phar"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan - PHP Static Analysis Tool",
            "support": {
                "issues": "https://github.com/phpstan/phpstan/issues",
                "source": "https://github.com/phpstan/phpstan/tree/0.12.71"
            },
            "funding": [
                {
                    "url": "https://github.com/ondrejmirtes",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/phpstan",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpstan/phpstan",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-01T18:24:00+00:00"
        },
        {
            "name": "phpstan/phpstan-deprecation-rules",
            "version": "0.12.6",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-deprecation-rules.git",
                "reference": "46dbd43c2db973d2876d6653e53f5c2cc3a01fbb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-deprecation-rules/zipball/46dbd43c2db973d2876d6653e53f5c2cc3a01fbb",
                "reference": "46dbd43c2db973d2876d6653e53f5c2cc3a01fbb",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.60"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12",
                "phpunit/phpunit": "^7.5.20"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan rules for detecting usage of deprecated classes, methods, properties, constants and traits.",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-deprecation-rules/issues",
                "source": "https://github.com/phpstan/phpstan-deprecation-rules/tree/0.12.6"
            },
            "time": "2020-12-13T10:20:54+00:00"
        },
        {
            "name": "phpstan/phpstan-strict-rules",
            "version": "0.12.9",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-strict-rules.git",
                "reference": "0705fefc7c9168529fd130e341428f5f10f4f01d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-strict-rules/zipball/0705fefc7c9168529fd130e341428f5f10f4f01d",
                "reference": "0705fefc7c9168529fd130e341428f5f10f4f01d",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.66"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.16",
                "phpunit/phpunit": "^7.5.20"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Extra strict and opinionated rules for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-strict-rules/issues",
                "source": "https://github.com/phpstan/phpstan-strict-rules/tree/0.12.9"
            },
            "time": "2021-01-13T08:50:28+00:00"
        },
        {
            "name": "phpstan/phpstan-symfony",
            "version": "0.12.16",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan-symfony.git",
                "reference": "c50afb8f4e27d4ab3b47ac370838aefac3c15e9e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan-symfony/zipball/c50afb8f4e27d4ab3b47ac370838aefac3c15e9e",
                "reference": "c50afb8f4e27d4ab3b47ac370838aefac3c15e9e",
                "shasum": ""
            },
            "require": {
                "ext-simplexml": "*",
                "php": "^7.1 || ^8.0",
                "phpstan/phpstan": "^0.12.51"
            },
            "conflict": {
                "symfony/framework-bundle": "<3.0"
            },
            "require-dev": {
                "phing/phing": "^2.16.3",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpstan-phpunit": "^0.12.16",
                "phpstan/phpstan-strict-rules": "^0.12.5",
                "phpunit/phpunit": "^7.5.20",
                "symfony/console": "^4.0",
                "symfony/framework-bundle": "^4.0",
                "symfony/http-foundation": "^4.0",
                "symfony/messenger": "^4.2",
                "symfony/serializer": "^4.0"
            },
            "type": "phpstan-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.12-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon",
                        "rules.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "PHPStan\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Lukáš Unger",
                    "email": "looky.msc@gmail.com",
                    "homepage": "https://lookyman.net"
                }
            ],
            "description": "Symfony Framework extensions and rules for PHPStan",
            "support": {
                "issues": "https://github.com/phpstan/phpstan-symfony/issues",
                "source": "https://github.com/phpstan/phpstan-symfony/tree/0.12.16"
            },
            "time": "2021-01-25T12:30:55+00:00"
        },
        {
            "name": "roave/security-advisories",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/Roave/SecurityAdvisories.git",
                "reference": "f7d723a10c7cb36e11430182f5813ecb1b887da0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Roave/SecurityAdvisories/zipball/f7d723a10c7cb36e11430182f5813ecb1b887da0",
                "reference": "f7d723a10c7cb36e11430182f5813ecb1b887da0",
                "shasum": ""
            },
            "conflict": {
                "3f/pygmentize": "<1.2",
                "adodb/adodb-php": "<5.20.12",
                "alterphp/easyadmin-extension-bundle": ">=1.2,<1.2.11|>=1.3,<1.3.1",
                "amphp/artax": "<1.0.6|>=2,<2.0.6",
                "amphp/http": "<1.0.1",
                "amphp/http-client": ">=4,<4.4",
                "api-platform/core": ">=2.2,<2.2.10|>=2.3,<2.3.6",
                "asymmetricrypt/asymmetricrypt": ">=0,<9.9.99",
                "aws/aws-sdk-php": ">=3,<3.2.1",
                "bagisto/bagisto": "<0.1.5",
                "barrelstrength/sprout-base-email": "<1.2.7",
                "barrelstrength/sprout-forms": "<3.9",
                "baserproject/basercms": ">=4,<=4.3.6|>=4.4,<4.4.1",
                "bolt/bolt": "<3.7.1",
                "brightlocal/phpwhois": "<=4.2.5",
                "buddypress/buddypress": "<5.1.2",
                "bugsnag/bugsnag-laravel": ">=2,<2.0.2",
                "cakephp/cakephp": ">=1.3,<1.3.18|>=2,<2.4.99|>=2.5,<2.5.99|>=2.6,<2.6.12|>=2.7,<2.7.6|>=3,<3.5.18|>=3.6,<3.6.15|>=3.7,<3.7.7",
                "cart2quote/module-quotation": ">=4.1.6,<=4.4.5|>=5,<5.4.4",
                "cartalyst/sentry": "<=2.1.6",
                "centreon/centreon": "<18.10.8|>=19,<19.4.5",
                "cesnet/simplesamlphp-module-proxystatistics": "<3.1",
                "codeigniter/framework": "<=3.0.6",
                "composer/composer": "<=1-alpha.11",
                "contao-components/mediaelement": ">=2.14.2,<2.21.1",
                "contao/core": ">=2,<3.5.39",
                "contao/core-bundle": ">=4,<4.4.52|>=4.5,<4.9.6|= 4.10.0",
                "contao/listing-bundle": ">=4,<4.4.8",
                "datadog/dd-trace": ">=0.30,<0.30.2",
                "david-garcia/phpwhois": "<=4.3.1",
                "derhansen/sf_event_mgt": "<4.3.1|>=5,<5.1.1",
                "doctrine/annotations": ">=1,<1.2.7",
                "doctrine/cache": ">=1,<1.3.2|>=1.4,<1.4.2",
                "doctrine/common": ">=2,<2.4.3|>=2.5,<2.5.1",
                "doctrine/dbal": ">=2,<2.0.8|>=2.1,<2.1.2",
                "doctrine/doctrine-bundle": "<1.5.2",
                "doctrine/doctrine-module": "<=0.7.1",
                "doctrine/mongodb-odm": ">=1,<1.0.2",
                "doctrine/mongodb-odm-bundle": ">=2,<3.0.1",
                "doctrine/orm": ">=2,<2.4.8|>=2.5,<2.5.1",
                "dolibarr/dolibarr": "<11.0.4",
                "dompdf/dompdf": ">=0.6,<0.6.2",
                "drupal/core": ">=7,<7.74|>=8,<8.8.11|>=8.9,<8.9.9|>=9,<9.0.8",
                "drupal/drupal": ">=7,<7.74|>=8,<8.8.11|>=8.9,<8.9.9|>=9,<9.0.8",
                "endroid/qr-code-bundle": "<3.4.2",
                "enshrined/svg-sanitize": "<0.13.1",
                "erusev/parsedown": "<1.7.2",
                "ezsystems/demobundle": ">=5.4,<5.4.6.1",
                "ezsystems/ez-support-tools": ">=2.2,<2.2.3",
                "ezsystems/ezdemo-ls-extension": ">=5.4,<5.4.2.1",
                "ezsystems/ezfind-ls": ">=5.3,<5.3.6.1|>=5.4,<5.4.11.1|>=2017.12,<2017.12.0.1",
                "ezsystems/ezplatform": ">=1.7,<1.7.9.1|>=1.13,<1.13.5.1|>=2.5,<2.5.4",
                "ezsystems/ezplatform-admin-ui": ">=1.3,<1.3.5|>=1.4,<1.4.6",
                "ezsystems/ezplatform-admin-ui-assets": ">=4,<4.2.1|>=5,<5.0.1|>=5.1,<5.1.1",
                "ezsystems/ezplatform-kernel": ">=1,<1.0.2.1",
                "ezsystems/ezplatform-user": ">=1,<1.0.1",
                "ezsystems/ezpublish-kernel": ">=5.3,<5.3.12.1|>=5.4,<5.4.14.2|>=6,<6.7.9.1|>=6.8,<6.13.6.3|>=7,<7.2.4.1|>=7.3,<7.3.2.1|>=7.5,<7.5.7.1",
                "ezsystems/ezpublish-legacy": ">=5.3,<5.3.12.6|>=5.4,<5.4.14.2|>=2011,<2017.12.7.3|>=2018.6,<2018.6.1.4|>=2018.9,<2018.9.1.3|>=2019.3,<2019.3.5.1",
                "ezsystems/platform-ui-assets-bundle": ">=4.2,<4.2.3",
                "ezsystems/repository-forms": ">=2.3,<2.3.2.1",
                "ezyang/htmlpurifier": "<4.1.1",
                "firebase/php-jwt": "<2",
                "flarum/sticky": ">=0.1-beta.14,<=0.1-beta.15",
                "flarum/tags": "<=0.1-beta.13",
                "fooman/tcpdf": "<6.2.22",
                "fossar/tcpdf-parser": "<6.2.22",
                "friendsofsymfony/oauth2-php": "<1.3",
                "friendsofsymfony/rest-bundle": ">=1.2,<1.2.2",
                "friendsofsymfony/user-bundle": ">=1.2,<1.3.5",
                "friendsoftypo3/mediace": ">=7.6.2,<7.6.5",
                "fuel/core": "<1.8.1",
                "getgrav/grav": "<1.7-beta.8",
                "getkirby/cms": ">=3,<3.4.5",
                "getkirby/panel": "<2.5.14",
                "gos/web-socket-bundle": "<1.10.4|>=2,<2.6.1|>=3,<3.3",
                "gree/jose": "<=2.2",
                "gregwar/rst": "<1.0.3",
                "guzzlehttp/guzzle": ">=4-rc.2,<4.2.4|>=5,<5.3.1|>=6,<6.2.1",
                "illuminate/auth": ">=4,<4.0.99|>=4.1,<=4.1.31|>=4.2,<=4.2.22|>=5,<=5.0.35|>=5.1,<=5.1.46|>=5.2,<=5.2.45|>=5.3,<=5.3.31|>=5.4,<=5.4.36|>=5.5,<5.5.10",
                "illuminate/cookie": ">=4,<=4.0.11|>=4.1,<=4.1.99999|>=4.2,<=4.2.99999|>=5,<=5.0.99999|>=5.1,<=5.1.99999|>=5.2,<=5.2.99999|>=5.3,<=5.3.99999|>=5.4,<=5.4.99999|>=5.5,<=5.5.49|>=5.6,<=5.6.99999|>=5.7,<=5.7.99999|>=5.8,<=5.8.99999|>=6,<6.18.31|>=7,<7.22.4",
                "illuminate/database": "<6.20.14|>=7,<7.30.4|>=8,<8.24",
                "illuminate/encryption": ">=4,<=4.0.11|>=4.1,<=4.1.31|>=4.2,<=4.2.22|>=5,<=5.0.35|>=5.1,<=5.1.46|>=5.2,<=5.2.45|>=5.3,<=5.3.31|>=5.4,<=5.4.36|>=5.5,<5.5.40|>=5.6,<5.6.15",
                "illuminate/view": ">=7,<7.1.2",
                "ivankristianto/phpwhois": "<=4.3",
                "james-heinrich/getid3": "<1.9.9",
                "joomla/session": "<1.3.1",
                "jsmitty12/phpwhois": "<5.1",
                "kazist/phpwhois": "<=4.2.6",
                "kitodo/presentation": "<3.1.2",
                "kreait/firebase-php": ">=3.2,<3.8.1",
                "la-haute-societe/tcpdf": "<6.2.22",
                "laravel/framework": "<6.20.14|>=7,<7.30.4|>=8,<8.24",
                "laravel/socialite": ">=1,<1.0.99|>=2,<2.0.10",
                "league/commonmark": "<0.18.3",
                "librenms/librenms": "<1.53",
                "livewire/livewire": ">2.2.4,<2.2.6",
                "magento/community-edition": ">=2,<2.2.10|>=2.3,<2.3.3",
                "magento/magento1ce": "<1.9.4.3",
                "magento/magento1ee": ">=1,<1.14.4.3",
                "magento/product-community-edition": ">=2,<2.2.10|>=2.3,<2.3.2-p.2",
                "marcwillmann/turn": "<0.3.3",
                "mautic/core": "<2.16.5|>=3,<3.2.4|= 2.13.1",
                "mediawiki/core": ">=1.27,<1.27.6|>=1.29,<1.29.3|>=1.30,<1.30.2|>=1.31,<1.31.9|>=1.32,<1.32.6|>=1.32.99,<1.33.3|>=1.33.99,<1.34.3|>=1.34.99,<1.35",
                "mittwald/typo3_forum": "<1.2.1",
                "monolog/monolog": ">=1.8,<1.12",
                "namshi/jose": "<2.2",
                "nette/application": ">=2,<2.0.19|>=2.1,<2.1.13|>=2.2,<2.2.10|>=2.3,<2.3.14|>=2.4,<2.4.16|>=3,<3.0.6",
                "nette/nette": ">=2,<2.0.19|>=2.1,<2.1.13",
                "nystudio107/craft-seomatic": "<3.3",
                "nzo/url-encryptor-bundle": ">=4,<4.3.2|>=5,<5.0.1",
                "october/backend": ">=1.0.319,<1.0.470",
                "october/cms": "= 1.0.469|>=1.0.319,<1.0.469",
                "october/october": ">=1.0.319,<1.0.466",
                "october/rain": ">=1.0.319,<1.0.468",
                "onelogin/php-saml": "<2.10.4",
                "oneup/uploader-bundle": "<1.9.3|>=2,<2.1.5",
                "openid/php-openid": "<2.3",
                "openmage/magento-lts": "<19.4.8|>=20,<20.0.4",
                "orchid/platform": ">=9,<9.4.4",
                "oro/crm": ">=1.7,<1.7.4",
                "oro/platform": ">=1.7,<1.7.4",
                "padraic/humbug_get_contents": "<1.1.2",
                "pagarme/pagarme-php": ">=0,<3",
                "paragonie/random_compat": "<2",
                "passbolt/passbolt_api": "<2.11",
                "paypal/merchant-sdk-php": "<3.12",
                "pear/archive_tar": "<1.4.12",
                "personnummer/personnummer": "<3.0.2",
                "phpfastcache/phpfastcache": ">=5,<5.0.13",
                "phpmailer/phpmailer": "<6.1.6",
                "phpmussel/phpmussel": ">=1,<1.6",
                "phpmyadmin/phpmyadmin": "<4.9.6|>=5,<5.0.3",
                "phpoffice/phpexcel": "<1.8.2",
                "phpoffice/phpspreadsheet": "<1.16",
                "phpunit/phpunit": ">=4.8.19,<4.8.28|>=5.0.10,<5.6.3",
                "phpwhois/phpwhois": "<=4.2.5",
                "phpxmlrpc/extras": "<0.6.1",
                "pimcore/pimcore": "<6.3",
                "pocketmine/pocketmine-mp": "<3.15.4",
                "prestashop/autoupgrade": ">=4,<4.10.1",
                "prestashop/contactform": ">1.0.1,<4.3",
                "prestashop/gamification": "<2.3.2",
                "prestashop/productcomments": ">=4,<4.2.1",
                "prestashop/ps_facetedsearch": "<3.4.1",
                "privatebin/privatebin": "<1.2.2|>=1.3,<1.3.2",
                "propel/propel": ">=2-alpha.1,<=2-alpha.7",
                "propel/propel1": ">=1,<=1.7.1",
                "pterodactyl/panel": "<0.7.19|>=1-rc.0,<=1-rc.6",
                "pusher/pusher-php-server": "<2.2.1",
                "rainlab/debugbar-plugin": "<3.1",
                "robrichards/xmlseclibs": "<3.0.4",
                "sabberworm/php-css-parser": ">=1,<1.0.1|>=2,<2.0.1|>=3,<3.0.1|>=4,<4.0.1|>=5,<5.0.9|>=5.1,<5.1.3|>=5.2,<5.2.1|>=6,<6.0.2|>=7,<7.0.4|>=8,<8.0.1|>=8.1,<8.1.1|>=8.2,<8.2.1|>=8.3,<8.3.1",
                "sabre/dav": ">=1.6,<1.6.99|>=1.7,<1.7.11|>=1.8,<1.8.9",
                "scheb/two-factor-bundle": ">=0,<3.26|>=4,<4.11",
                "sensiolabs/connect": "<4.2.3",
                "serluck/phpwhois": "<=4.2.6",
                "shopware/core": "<=6.3.4",
                "shopware/platform": "<=6.3.4",
                "shopware/shopware": "<5.6.9",
                "silverstripe/admin": ">=1.0.3,<1.0.4|>=1.1,<1.1.1",
                "silverstripe/assets": ">=1,<1.4.7|>=1.5,<1.5.2",
                "silverstripe/cms": "<4.3.6|>=4.4,<4.4.4",
                "silverstripe/comments": ">=1.3,<1.9.99|>=2,<2.9.99|>=3,<3.1.1",
                "silverstripe/forum": "<=0.6.1|>=0.7,<=0.7.3",
                "silverstripe/framework": "<4.4.7|>=4.5,<4.5.4",
                "silverstripe/graphql": ">=2,<2.0.5|>=3,<3.1.2|>=3.2,<3.2.4",
                "silverstripe/registry": ">=2.1,<2.1.2|>=2.2,<2.2.1",
                "silverstripe/restfulserver": ">=1,<1.0.9|>=2,<2.0.4",
                "silverstripe/subsites": ">=2,<2.1.1",
                "silverstripe/taxonomy": ">=1.3,<1.3.1|>=2,<2.0.1",
                "silverstripe/userforms": "<3",
                "simple-updates/phpwhois": "<=1",
                "simplesamlphp/saml2": "<1.10.6|>=2,<2.3.8|>=3,<3.1.4",
                "simplesamlphp/simplesamlphp": "<1.18.6",
                "simplesamlphp/simplesamlphp-module-infocard": "<1.0.1",
                "simplito/elliptic-php": "<1.0.6",
                "slim/slim": "<2.6",
                "smarty/smarty": "<3.1.33",
                "socalnick/scn-social-auth": "<1.15.2",
                "socialiteproviders/steam": "<1.1",
                "spoonity/tcpdf": "<6.2.22",
                "squizlabs/php_codesniffer": ">=1,<2.8.1|>=3,<3.0.1",
                "ssddanbrown/bookstack": "<0.29.2",
                "stormpath/sdk": ">=0,<9.9.99",
                "studio-42/elfinder": "<2.1.49",
                "sulu/sulu": "<1.6.34|>=2,<2.0.10|>=2.1,<2.1.1",
                "swiftmailer/swiftmailer": ">=4,<5.4.5",
                "sylius/admin-bundle": ">=1,<1.0.17|>=1.1,<1.1.9|>=1.2,<1.2.2",
                "sylius/grid": ">=1,<1.1.19|>=1.2,<1.2.18|>=1.3,<1.3.13|>=1.4,<1.4.5|>=1.5,<1.5.1",
                "sylius/grid-bundle": ">=1,<1.1.19|>=1.2,<1.2.18|>=1.3,<1.3.13|>=1.4,<1.4.5|>=1.5,<1.5.1",
                "sylius/resource-bundle": "<1.3.14|>=1.4,<1.4.7|>=1.5,<1.5.2|>=1.6,<1.6.4",
                "sylius/sylius": "<1.6.9|>=1.7,<1.7.9|>=1.8,<1.8.3",
                "symbiote/silverstripe-multivaluefield": ">=3,<3.0.99",
                "symbiote/silverstripe-versionedfiles": "<=2.0.3",
                "symfony/cache": ">=3.1,<3.4.35|>=4,<4.2.12|>=4.3,<4.3.8",
                "symfony/dependency-injection": ">=2,<2.0.17|>=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/error-handler": ">=4.4,<4.4.4|>=5,<5.0.4",
                "symfony/form": ">=2.3,<2.3.35|>=2.4,<2.6.12|>=2.7,<2.7.50|>=2.8,<2.8.49|>=3,<3.4.20|>=4,<4.0.15|>=4.1,<4.1.9|>=4.2,<4.2.1",
                "symfony/framework-bundle": ">=2,<2.3.18|>=2.4,<2.4.8|>=2.5,<2.5.2|>=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/http-foundation": ">=2,<2.8.52|>=3,<3.4.35|>=4,<4.2.12|>=4.3,<4.3.8|>=4.4,<4.4.7|>=5,<5.0.7",
                "symfony/http-kernel": ">=2,<2.8.52|>=3,<3.4.35|>=4,<4.2.12|>=4.3,<4.4.13|>=5,<5.1.5",
                "symfony/intl": ">=2.7,<2.7.38|>=2.8,<2.8.31|>=3,<3.2.14|>=3.3,<3.3.13",
                "symfony/mime": ">=4.3,<4.3.8",
                "symfony/phpunit-bridge": ">=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/polyfill": ">=1,<1.10",
                "symfony/polyfill-php55": ">=1,<1.10",
                "symfony/proxy-manager-bridge": ">=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/routing": ">=2,<2.0.19",
                "symfony/security": ">=2,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7|>=4.4,<4.4.7|>=5,<5.0.7",
                "symfony/security-bundle": ">=2,<2.7.48|>=2.8,<2.8.41|>=3,<3.3.17|>=3.4,<3.4.11|>=4,<4.0.11",
                "symfony/security-core": ">=2.4,<2.6.13|>=2.7,<2.7.9|>=2.7.30,<2.7.32|>=2.8,<2.8.37|>=3,<3.3.17|>=3.4,<3.4.7|>=4,<4.0.7",
                "symfony/security-csrf": ">=2.4,<2.7.48|>=2.8,<2.8.41|>=3,<3.3.17|>=3.4,<3.4.11|>=4,<4.0.11",
                "symfony/security-guard": ">=2.8,<2.8.41|>=3,<3.3.17|>=3.4,<3.4.11|>=4,<4.0.11",
                "symfony/security-http": ">=2.3,<2.3.41|>=2.4,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.2.12|>=4.3,<4.3.8|>=4.4,<4.4.7|>=5,<5.0.7",
                "symfony/serializer": ">=2,<2.0.11",
                "symfony/symfony": ">=2,<2.8.52|>=3,<3.4.35|>=4,<4.2.12|>=4.3,<4.4.13|>=5,<5.1.5",
                "symfony/translation": ">=2,<2.0.17",
                "symfony/validator": ">=2,<2.0.24|>=2.1,<2.1.12|>=2.2,<2.2.5|>=2.3,<2.3.3",
                "symfony/var-exporter": ">=4.2,<4.2.12|>=4.3,<4.3.8",
                "symfony/web-profiler-bundle": ">=2,<2.3.19|>=2.4,<2.4.9|>=2.5,<2.5.4",
                "symfony/yaml": ">=2,<2.0.22|>=2.1,<2.1.7",
                "t3g/svg-sanitizer": "<1.0.3",
                "tecnickcom/tcpdf": "<6.2.22",
                "thelia/backoffice-default-template": ">=2.1,<2.1.2",
                "thelia/thelia": ">=2.1-beta.1,<2.1.3",
                "theonedemon/phpwhois": "<=4.2.5",
                "titon/framework": ">=0,<9.9.99",
                "truckersmp/phpwhois": "<=4.3.1",
                "twig/twig": "<1.38|>=2,<2.7",
                "typo3/cms": ">=6.2,<6.2.30|>=7,<7.6.32|>=8,<8.7.38|>=9,<9.5.23|>=10,<10.4.10",
                "typo3/cms-core": ">=8,<8.7.38|>=9,<9.5.23|>=10,<10.4.10",
                "typo3/flow": ">=1,<1.0.4|>=1.1,<1.1.1|>=2,<2.0.1|>=2.3,<2.3.16|>=3,<3.0.10|>=3.1,<3.1.7|>=3.2,<3.2.7|>=3.3,<3.3.5",
                "typo3/neos": ">=1.1,<1.1.3|>=1.2,<1.2.13|>=2,<2.0.4",
                "typo3/phar-stream-wrapper": ">=1,<2.1.1|>=3,<3.1.1",
                "typo3fluid/fluid": ">=2,<2.0.8|>=2.1,<2.1.7|>=2.2,<2.2.4|>=2.3,<2.3.7|>=2.4,<2.4.4|>=2.5,<2.5.11|>=2.6,<2.6.10",
                "ua-parser/uap-php": "<3.8",
                "usmanhalalit/pixie": "<1.0.3|>=2,<2.0.2",
                "verot/class.upload.php": "<=1.0.3|>=2,<=2.0.4",
                "wallabag/tcpdf": "<6.2.22",
                "willdurand/js-translation-bundle": "<2.1.1",
                "yii2mod/yii2-cms": "<1.9.2",
                "yiisoft/yii": ">=1.1.14,<1.1.15",
                "yiisoft/yii2": "<2.0.38",
                "yiisoft/yii2-bootstrap": "<2.0.4",
                "yiisoft/yii2-dev": "<2.0.15",
                "yiisoft/yii2-elasticsearch": "<2.0.5",
                "yiisoft/yii2-gii": "<2.0.4",
                "yiisoft/yii2-jui": "<2.0.4",
                "yiisoft/yii2-redis": "<2.0.8",
                "yourls/yourls": "<1.7.4",
                "zendframework/zend-cache": ">=2.4,<2.4.8|>=2.5,<2.5.3",
                "zendframework/zend-captcha": ">=2,<2.4.9|>=2.5,<2.5.2",
                "zendframework/zend-crypt": ">=2,<2.4.9|>=2.5,<2.5.2",
                "zendframework/zend-db": ">=2,<2.0.99|>=2.1,<2.1.99|>=2.2,<2.2.10|>=2.3,<2.3.5",
                "zendframework/zend-developer-tools": ">=1.2.2,<1.2.3",
                "zendframework/zend-diactoros": ">=1,<1.8.4",
                "zendframework/zend-feed": ">=1,<2.10.3",
                "zendframework/zend-form": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-http": ">=1,<2.8.1",
                "zendframework/zend-json": ">=2.1,<2.1.6|>=2.2,<2.2.6",
                "zendframework/zend-ldap": ">=2,<2.0.99|>=2.1,<2.1.99|>=2.2,<2.2.8|>=2.3,<2.3.3",
                "zendframework/zend-mail": ">=2,<2.4.11|>=2.5,<2.7.2",
                "zendframework/zend-navigation": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-session": ">=2,<2.0.99|>=2.1,<2.1.99|>=2.2,<2.2.9|>=2.3,<2.3.4",
                "zendframework/zend-validator": ">=2.3,<2.3.6",
                "zendframework/zend-view": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-xmlrpc": ">=2.1,<2.1.6|>=2.2,<2.2.6",
                "zendframework/zendframework": "<2.5.1",
                "zendframework/zendframework1": "<1.12.20",
                "zendframework/zendopenid": ">=2,<2.0.2",
                "zendframework/zendxml": ">=1,<1.0.1",
                "zetacomponents/mail": "<1.8.2",
                "zf-commons/zfc-user": "<1.2.2",
                "zfcampus/zf-apigility-doctrine": ">=1,<1.0.3",
                "zfr/zfr-oauth2-server-module": "<0.1.2"
            },
            "type": "metapackage",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "role": "maintainer"
                },
                {
                    "name": "Ilya Tribusean",
                    "email": "slash3b@gmail.com",
                    "role": "maintainer"
                }
            ],
            "description": "Prevents installation of composer packages with known security vulnerabilities: no API, simply require it",
            "support": {
                "issues": "https://github.com/Roave/SecurityAdvisories/issues",
                "source": "https://github.com/Roave/SecurityAdvisories/tree/latest"
            },
            "funding": [
                {
                    "url": "https://github.com/Ocramius",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/roave/security-advisories",
                    "type": "tidelift"
                }
            ],
            "time": "2021-02-02T10:05:32+00:00"
        },
        {
            "name": "slevomat/coding-standard",
            "version": "6.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/slevomat/coding-standard.git",
                "reference": "696dcca217d0c9da2c40d02731526c1e25b65346"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/slevomat/coding-standard/zipball/696dcca217d0c9da2c40d02731526c1e25b65346",
                "reference": "696dcca217d0c9da2c40d02731526c1e25b65346",
                "shasum": ""
            },
            "require": {
                "dealerdirect/phpcodesniffer-composer-installer": "^0.6.2 || ^0.7",
                "php": "^7.1 || ^8.0",
                "phpstan/phpdoc-parser": "0.4.5 - 0.4.9",
                "squizlabs/php_codesniffer": "^3.5.6"
            },
            "require-dev": {
                "phing/phing": "2.16.3",
                "php-parallel-lint/php-parallel-lint": "1.2.0",
                "phpstan/phpstan": "0.12.48",
                "phpstan/phpstan-deprecation-rules": "0.12.5",
                "phpstan/phpstan-phpunit": "0.12.16",
                "phpstan/phpstan-strict-rules": "0.12.5",
                "phpunit/phpunit": "7.5.20|8.5.5|9.4.0"
            },
            "type": "phpcodesniffer-standard",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "SlevomatCodingStandard\\": "SlevomatCodingStandard"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Slevomat Coding Standard for PHP_CodeSniffer complements Consistence Coding Standard by providing sniffs with additional checks.",
            "support": {
                "issues": "https://github.com/slevomat/coding-standard/issues",
                "source": "https://github.com/slevomat/coding-standard/tree/6.4.1"
            },
            "funding": [
                {
                    "url": "https://github.com/kukulich",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/slevomat/coding-standard",
                    "type": "tidelift"
                }
            ],
            "time": "2020-10-05T12:39:37+00:00"
        },
        {
            "name": "sllh/composer-versions-check",
            "version": "dev-php-8",
            "source": {
                "type": "git",
                "url": "https://github.com/soullivaneuh/composer-versions-check.git",
                "reference": "2d7bf81661ec67c7cd678a2ebcb27430b2201b76"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/soullivaneuh/composer-versions-check/zipball/2d7bf81661ec67c7cd678a2ebcb27430b2201b76",
                "reference": "2d7bf81661ec67c7cd678a2ebcb27430b2201b76",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.0 || ^2.0",
                "php": "^5.3 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "composer/composer": "^1.0 || ^2.0",
                "symfony/phpunit-bridge": "^2.7.4|^3.0"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "SLLH\\ComposerVersionsCheck\\VersionsCheckPlugin",
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "SLLH\\ComposerVersionsCheck\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Sullivan SENECHAL",
                    "email": "soullivaneuh@gmail.com"
                }
            ],
            "description": "Checks if packages are up to date to last major versions after update",
            "keywords": [
                "composer",
                "plugin",
                "update",
                "versions"
            ],
            "support": {
                "issues": "https://github.com/soullivaneuh/composer-versions-check/issues",
                "source": "https://github.com/soullivaneuh/composer-versions-check/tree/php-8"
            },
            "time": "2020-12-16T17:13:29+00:00"
        },
        {
            "name": "squizlabs/php_codesniffer",
            "version": "3.5.8",
            "source": {
                "type": "git",
                "url": "https://github.com/squizlabs/PHP_CodeSniffer.git",
                "reference": "9d583721a7157ee997f235f327de038e7ea6dac4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/squizlabs/PHP_CodeSniffer/zipball/9d583721a7157ee997f235f327de038e7ea6dac4",
                "reference": "9d583721a7157ee997f235f327de038e7ea6dac4",
                "shasum": ""
            },
            "require": {
                "ext-simplexml": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0 || ^7.0"
            },
            "bin": [
                "bin/phpcs",
                "bin/phpcbf"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Greg Sherwood",
                    "role": "lead"
                }
            ],
            "description": "PHP_CodeSniffer tokenizes PHP, JavaScript and CSS files and detects violations of a defined set of coding standards.",
            "homepage": "https://github.com/squizlabs/PHP_CodeSniffer",
            "keywords": [
                "phpcs",
                "standards"
            ],
            "support": {
                "issues": "https://github.com/squizlabs/PHP_CodeSniffer/issues",
                "source": "https://github.com/squizlabs/PHP_CodeSniffer",
                "wiki": "https://github.com/squizlabs/PHP_CodeSniffer/wiki"
            },
            "time": "2020-10-23T02:01:07+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v5.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "72ca213014a92223a5d18651ce79ef441c12b694"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/72ca213014a92223a5d18651ce79ef441c12b694",
                "reference": "72ca213014a92223a5d18651ce79ef441c12b694",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php80": "^1.15"
            },
            "conflict": {
                "phpunit/phpunit": "<5.4.3",
                "symfony/console": "<4.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^4.4|^5.0",
                "symfony/process": "^4.4|^5.0",
                "twig/twig": "^2.13|^3.0.4"
            },
            "suggest": {
                "ext-iconv": "To convert non-UTF-8 strings to UTF-8 (or symfony/polyfill-iconv in case ext-iconv cannot be used).",
                "ext-intl": "To show region name in time zone dump",
                "symfony/console": "To use the ServerDumpCommand and/or the bin/var-dump-server script"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides mechanisms for walking through any arbitrary PHP variable",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/v5.2.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2021-01-27T10:15:41+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": {
        "roave/security-advisories": 20,
        "sllh/composer-versions-check": 20
    },
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": "^7.4|^8.0",
        "ext-sodium": "*"
    },
    "platform-dev": [],
    "plugin-api-version": "2.0.0"
}


File: /config\services.php
<?php
declare(strict_types=1);

namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use BaconQrCode\Renderer\PlainTextRenderer;
use BaconQrCode\Writer;
use NoFlash\ROSAutoWireGuard\Command\GenerateCommand;
use NoFlash\ROSAutoWireGuard\UseCase\AddNewPeers;
use NoFlash\ROSAutoWireGuard\UseCase\BuildClientConfiguration;
use NoFlash\ROSAutoWireGuard\WireGuard\Configuration\PeerProjector;
use NoFlash\ROSAutoWireGuard\WireGuard\QrGenerator;

return function(ContainerConfigurator $configurator) {
    $services = $configurator
        ->services()
            ->defaults()
                ->autowire()
                ->autoconfigure()
    ;

    $services->load('NoFlash\\ROSAutoWireGuard\\', '../src/*')
             ->exclude('../src/{DependencyInjection}');

    $services->set('app.qr_text_renderer')
             ->class(PlainTextRenderer::class);
    $services->set('app.qr_text_writer')
             ->class(Writer::class)
             ->arg(0, service('app.qr_text_renderer'));
    $services->set(QrGenerator::class)
             ->arg('$qrWriter', service('app.qr_text_writer'))
            ->public()
    ;

    $services->set(GenerateCommand::class)->public();
    $services->set(AddNewPeers::class)->public();
    $services->set(BuildClientConfiguration::class)->share(false)->public();
    $services->set(PeerProjector::class)->share(false);
};


File: /Dockerfile
FROM composer:2 AS composer
FROM php:8.0-cli-alpine

RUN apk update
RUN docker-php-ext-install sockets
RUN apk add libsodium-dev && docker-php-ext-install sodium
RUN docker-php-ext-install bcmath

RUN apk add git
COPY --from=composer /usr/bin/composer /usr/bin/composer
COPY . /usr/src/mt-wg-auto
WORKDIR /usr/src/mt-wg-auto
RUN php /usr/bin/composer install -o -a -n

ENTRYPOINT ["php", "./bin/console"]


File: /docs\EXAMPLES.md
## Examples

#### Get help
`bin/console generate --help`

...no, seriously, each option has help ;)

By default, the following options are assumed (and can be changed):
- Advanced/HTML template (with QR code readable in CLI and in a browser)
- Single user is generated
- Peer config routes all traffic via VPN (use `--allowed` to change)
- No pre-shared key (use `--psk` to enable)
- No keep-alive/[NAT helper](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence)
- Use default (`wireguard1`) interface (use `--interface` to change)
- Next free IP is assigned from the WireGuard interface (use `--pool` if you want to use DHCP pool)
- External IP of the VPN server is the same as you use to call the API (use `--vpn-host` to change)
- External WireGuard port is read from the interface (use `--vpn-port` to change)

---

#### Minimal example
Generate a single user without name using default (`wireguard1`) interface:

`bin/console generate router.lan user password`

The generated config for the user will route all traffic through the VPN by default (use `--allowed` to change).

---

#### Multiple unnamed users
Generate 10 users without names:

`bin/console generate --num 10 router.lan user password`

---

#### Multiple named users
Generate 3 users (foo, bar, baz). The example shows both long (`--user`) and short (`-u`) invocation which are
interchangeable:

`bin/console generate --user foo -u bar -u baz router.lan user password`

Names of users will be saved in comments for each of the peers, and also included in printed output.

---

#### Multiple named users from a list file
Create a file `foo.txt` with:
```
foo
bar
baz
```

Then call the command below to generate 3 users (foo, bar, baz):

`bin/console generate --user-list foo.txt router.lan user password`

Names of users will be saved in comments for each of the peers, and also included in printed output.

---

#### Force PSK for users
Generate a single user without name using default (`wireguard1`) interface with pre-shared key enabled:

`bin/console generate --psk router.lan user password`

The generated config for the user will route all traffic through the VPN by default (use `--allowed` to change).

---

#### Change routes/allowed networks
Generate a single user with access two networks via split-tunnel VPN:

`bin/console generate --allowed 10.0.0.1/24 --allowed 10.100.0.1/24 router.lan user password`

---

#### Force a periodic refresh for road-warriors
Generate a single user with forced keep-alive every 60s:

`bin/console generate --keep-alive 60 router.lan user password`


This option is especially useful to [overcome NAT problems](https://www.wireguard.com/quickstart/#nat-and-firewall-traversal-persistence).

---

#### Use custom template
Generate a single user with a text-based template

`bin/console generate --teamplate resources/template/text.twig router.lan user password`

You can make your own templates too - [see docs](README.md#custom-templates).


File: /docs\README.md
# MikroTik WG Auto

### Overview of options
A loose list of currently possible scenarios with the tool:

- generation of text-based configs in CLI
- generation of configs from templates (HTML or text, see `resources/template/` for examples)
- creating QR codes with configs (for mobile apps)  
- assigning IPs from DHCP pools (`/ip pool`) or from interfaces (`/ip address`)
- optionally autogenerating [pre-shared keys](https://www.wireguard.com/protocol/) for extra security
- 

### Examples
See [`EXAMPLES.md`](EXAMPLES.md).

### Custom templates
The tool allows for a custom template to be specified. Templates are using [Twig engine](https://twig.symfony.com/doc/3.x/).
To use a template set option `--teamplate` (`-t` for short). By default [`resources/template/advanced.twig`](../resources/template/advanced.twig) 
full-featured template is used. The code also includes a simpler, text-based template: [`resources/template/text.twig`](../resources/template/text.twig). 



File: /LICENSE
The MIT License (MIT)

Copyright (c) 2020 Grzegorz Zdanowski

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


File: /phpcs.xml.dist
<?xml version="1.0"?>
<ruleset name="SNMP Bridge CS" namespace="NoFlash\ROSAutoWireGuard\CS\Standard">
    <config name="installed_paths" value="../../object-calisthenics/phpcs-calisthenics-rules/src,../../slevomat/coding-standard"/>
    <ini name="memory_limit" value="128M"/>
    <arg name="colors"/>
    <arg name="basepath" value="."/>
    <arg name="parallel" value="8" />

    <autoload>./vendor/autoload.php</autoload>
    <file>src</file>
    <file>tests</file>
    <exclude-pattern>*/src/DependencyInjection/Configuration\.php</exclude-pattern>

    <!-- Don't hide tokenizer exceptions -->
    <rule ref="Internal.Tokenizer.Exception">
        <type>error</type>
    </rule>

    <rule ref="PSR2"/>
    <!-- ############################################################################ -->
    <!--                            PHPCS built-in rules                              -->
    <!-- ############################################################################ -->
    <rule ref="Generic.Files.LineLength.TooLong" />
    <rule ref="Generic.PHP.ForbiddenFunctions">
        <properties>
            <property name="forbiddenFunctions" type="array">
                <!-- Use proper logging facilities -->
                <element key="echo" value="null"/>
                <element key="print" value="null"/>

                <element key="is_null" value="null"/> <!-- Use "$x === null" instead -->

                <element key="die" value="null"/> <!-- Replace by proper code return or exception -->
                <element key="create_function" value="null"/> <!-- Deprecated, use lambdas -->
                <element key="eval" value="null"/> <!-- Does this need a comment? -->
                <element key="goto" value="null"/>  <!-- https://xkcd.com/292/ -->
                <element key="define" value="null"/> <!-- Use const keyword -->

                <!-- Use proper syntax -->
                <element key="extract" value="null"/>
                <element key="call_user_func" value="null"/>
                <element key="call_user_func_array" value="null"/>
            </property>
        </properties>
    </rule>

    <rule ref="Generic.Metrics.CyclomaticComplexity">
        <properties>
            <property name="complexity" value="15" />
            <property name="absoluteComplexity" value="15" />
        </properties>
    </rule>

    <rule ref="Generic.Metrics.NestingLevel" />


    <!-- ############################################################################ -->
    <!-- Sourced from https://github.com/object-calisthenics/phpcs-calisthenics-rules -->
    <!-- ############################################################################ -->
    <rule ref="ObjectCalisthenics.Metrics.MaxNestingLevel">
        <properties>
            <property name="maxNestingLevel" value="3"/>
        </properties>
    </rule>
    <rule ref="ObjectCalisthenics.ControlStructures.NoElse" />
    <rule ref="ObjectCalisthenics.NamingConventions.ElementNameMinimalLength">
        <properties>
            <property name="minLength" value="3"/>
            <!--
              i - iteration
              id - self explanatory
              to - from/to are obvious
              k,v - key/value, very common
              e,t - common in catch for $e(xception) or $t(hrowable)
              _ - common convention to mark variable as not used in loops (e.g. foreach ($foo as $key => $_))
            -->
            <property name="allowedShortNames" type="array" value="i,id,to,k,v,e,t,_,ip,rx,tx"/>
        </properties>
    </rule>
    <rule ref="ObjectCalisthenics.Files.ClassTraitAndInterfaceLength">
        <properties>
            <property name="maxLength" value="300"/>
        </properties>
    </rule>
    <rule ref="ObjectCalisthenics.Files.FunctionLength">
        <properties>
            <property name="maxLength" value="80"/>
        </properties>
    </rule>
    <rule ref="ObjectCalisthenics.Metrics.PropertyPerClassLimit">
        <properties>
            <property name="maxCount" value="10"/>
        </properties>
    </rule>
    <rule ref="ObjectCalisthenics.Metrics.MethodPerClassLimit">
        <properties>
            <property name="maxCount" value="10"/>
        </properties>
    </rule>





    <!-- ############################################################################ -->
    <!--           Sourced from https://github.com/slevomat/coding-standard           -->
    <!-- ############################################################################ -->
    <rule ref="SlevomatCodingStandard.TypeHints.ParameterTypeHint">
        <properties>
            <property name="enableObjectTypeHint" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.TypeHints.PropertyTypeHint">
        <properties>
            <property name="enableNativeTypeHint" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.TypeHints.ReturnTypeHint">
        <properties>
            <property name="enableObjectTypeHint" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.TypeHints.UselessConstantTypeHint" />
    <rule ref="SlevomatCodingStandard.Exceptions.ReferenceThrowableOnly" />
    <rule ref="SlevomatCodingStandard.TypeHints.DeclareStrictTypes">
        <properties>
            <property name="spacesCountAroundEqualsSign" value="0" />
            <property name="newlinesCountBetweenOpenTagAndDeclare" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Arrays.DisallowImplicitArrayCreation" />
<!--    <rule ref="SlevomatCodingStandard.Classes.ClassStructure">-->
<!--        //TODO: configure me according to PSR https://github.com/slevomat/coding-standard#slevomatcodingstandardclassesclassstructure- -->
<!--    </rule>-->
    <rule ref="SlevomatCodingStandard.Classes.UselessLateStaticBinding" />
    <rule ref="SlevomatCodingStandard.ControlStructures.AssignmentInCondition" />
    <rule ref="SlevomatCodingStandard.ControlStructures.DisallowContinueWithoutIntegerOperandInSwitch" />
    <rule ref="SlevomatCodingStandard.ControlStructures.DisallowEmpty" /> <!-- I love it for arrays... but... it's crap -->
    <rule ref="SlevomatCodingStandard.ControlStructures.RequireNullCoalesceOperator" />
    <rule ref="SlevomatCodingStandard.ControlStructures.RequireNullCoalesceEqualOperator" />
    <rule ref="SlevomatCodingStandard.ControlStructures.EarlyExit">
        <properties>
            <property name="ignoreStandaloneIfInScope" value="true" />
            <property name="ignoreOneLineTrailingIf" value="true" />
            <property name="ignoreTrailingIfWithOneInstruction" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Functions.StrictCall" />
    <rule ref="SlevomatCodingStandard.Functions.StaticClosure" />
    <rule ref="SlevomatCodingStandard.PHP.DisallowDirectMagicInvokeCall" /> <!-- no magic methods should be called directly... -->
    <rule ref="SlevomatCodingStandard.Operators.DisallowEqualOperators" />
    <rule ref="SlevomatCodingStandard.Operators.RequireCombinedAssignmentOperator" />
    <rule ref="SlevomatCodingStandard.Classes.UnusedPrivateElements" /> <!-- has options, none used now -->
    <rule ref="SlevomatCodingStandard.Functions.UnusedInheritedVariablePassedToClosure" />
    <rule ref="SlevomatCodingStandard.Functions.UnusedParameter" />
    <rule ref="SlevomatCodingStandard.Functions.UselessParameterDefaultValue" />
    <rule ref="SlevomatCodingStandard.Namespaces.UnusedUses">
        <properties>
            <property name="searchAnnotations" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Namespaces.UseFromSameNamespace" />
    <rule ref="SlevomatCodingStandard.Namespaces.UselessAlias" />
    <rule ref="SlevomatCodingStandard.PHP.DisallowReference" /> <!-- objects should be used instead when such behavior is desired -->
    <rule ref="SlevomatCodingStandard.PHP.UselessParentheses" />
    <rule ref="SlevomatCodingStandard.PHP.OptimizedFunctionsWithoutUnpacking" />
    <rule ref="SlevomatCodingStandard.PHP.UselessSemicolon" />
    <rule ref="SlevomatCodingStandard.Variables.DisallowSuperGlobalVariable" />
    <rule ref="SlevomatCodingStandard.Variables.DuplicateAssignmentToVariable" />
    <rule ref="SlevomatCodingStandard.Variables.UselessVariable">
        <properties>
            <property name="ignoreUnusedValuesWhenOnlyKeysAreUsedInForeach" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Exceptions.DeadCatch" />
    <rule ref="SlevomatCodingStandard.Arrays.TrailingArrayComma" />
    <rule ref="SlevomatCodingStandard.Classes.ClassMemberSpacing">
        <properties>
            <property name="linesCountBetweenMembers" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.ConstantSpacing">
        <properties>
            <property name="minLinesCountBeforeWithComment" value="1" />
            <property name="maxLinesCountBeforeWithComment" value="2" />
            <property name="minLinesCountBeforeWithoutComment" value="0" />
            <property name="maxLinesCountBeforeWithoutComment" value="2" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.DisallowMultiConstantDefinition" /> <!-- this makes a hot mess in git -->
    <rule ref="SlevomatCodingStandard.Classes.DisallowMultiPropertyDefinition" /> <!-- this makes a hot mess in git -->
    <rule ref="SlevomatCodingStandard.Classes.MethodSpacing">
        <properties>
            <property name="minLinesCount" value="1" />
            <property name="maxLinesCount" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.ModernClassNameReference" />
    <rule ref="SlevomatCodingStandard.Classes.PropertySpacing">
        <properties>
            <property name="minLinesCountBeforeWithComment" value="1" />
            <property name="maxLinesCountBeforeWithComment" value="2" />
            <property name="minLinesCountBeforeWithoutComment" value="0" />
            <property name="maxLinesCountBeforeWithoutComment" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.RequireMultiLineMethodSignature">
        <properties>
            <!-- I know PSR, we have wide screens ffs - 120 is STILL within the limits of the standard -->
            <property name="minLineLength" value="120" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.RequireSingleLineMethodSignature">
        <properties>
            <property name="maxLineLength" value="80" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Classes.TraitUseDeclaration" /> <!-- this makes a hot mess in git -->
    <rule ref="SlevomatCodingStandard.Classes.TraitUseSpacing">
        <properties>
            <property name="linesCountBeforeFirstUse" value="0" />
            <property name="linesCountBeforeFirstUseWhenFirstInClass" value="0" />
            <property name="linesCountBetweenUses" value="0" />
            <property name="linesCountAfterLastUse" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.ControlStructures.LanguageConstructWithParentheses" />
    <rule ref="SlevomatCodingStandard.ControlStructures.NewWithParentheses" />
    <rule ref="SlevomatCodingStandard.ControlStructures.RequireShortTernaryOperator" />
    <rule ref="SlevomatCodingStandard.ControlStructures.RequireTernaryOperator">
       <properties>
           <property name="ignoreMultiLine" value="true" />
       </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.ControlStructures.DisallowYodaComparison" />
    <rule ref="SlevomatCodingStandard.Functions.ArrowFunctionDeclaration">
        <properties>
            <property ref="spacesCountAfterKeyword" value="1" />
            <property ref="spacesCountBeforeArrow" value="1" />
            <property ref="spacesCountAfterArrow" value="1" />
            <property ref="allowMultiLine" value="true" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Functions.DisallowEmptyFunction" />
    <rule ref="SlevomatCodingStandard.Functions.RequireArrowFunction">
        <properties>
            <property name="allowNested" value="false" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Namespaces.AlphabeticallySortedUses">
        <properties>
            <property name="psr12Compatible" value="true" />
            <property name="caseSensitive" value="false" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Namespaces.RequireOneNamespaceInFile" />
    <rule ref="SlevomatCodingStandard.Namespaces.NamespaceDeclaration" />
    <rule ref="SlevomatCodingStandard.Namespaces.NamespaceSpacing">
        <properties>
            <property name="linesCountBeforeNamespace" value="1" />
            <property name="linesCountAfterNamespace" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Namespaces.UseSpacing">
        <properties>
            <property name="linesCountBeforeFirstUse" value="1" />
            <property name="linesCountAfterLastUse" value="1" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Numbers.RequireNumericLiteralSeparator">
        <properties>
            <property name="enable" value="true" />
            <property name="minDigitsBeforeDecimalPoint" value="5" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Operators.NegationOperatorSpacing">
        <properties>
            <property name="spacesCount" value="0" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Operators.SpreadOperatorSpacing">
        <properties>
            <property name="spacesCountAfterOperator" value="0" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.TypeHints.DisallowMixedTypeHint" />
    <rule ref="SlevomatCodingStandard.TypeHints.LongTypeHints" />
    <rule ref="SlevomatCodingStandard.TypeHints.NullTypeHintOnLastPosition" />
    <rule ref="SlevomatCodingStandard.PHP.ShortList" />
    <rule ref="SlevomatCodingStandard.PHP.TypeCast" />
    <rule ref="SlevomatCodingStandard.Classes.ClassConstantVisibility" />
    <rule ref="SlevomatCodingStandard.TypeHints.ReturnTypeHintSpacing">
        <properties>
            <property name="spacesCountBeforeColon" value="0" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.TypeHints.NullableTypeForNullDefaultValue" />
    <rule ref="SlevomatCodingStandard.TypeHints.ParameterTypeHintSpacing" />
    <rule ref="SlevomatCodingStandard.TypeHints.PropertyTypeHintSpacing" />
    <rule ref="SlevomatCodingStandard.Namespaces.DisallowGroupUse" />
    <rule ref="SlevomatCodingStandard.Namespaces.FullyQualifiedGlobalConstants" />
    <rule ref="SlevomatCodingStandard.Namespaces.FullyQualifiedGlobalFunctions" />
    <rule ref="SlevomatCodingStandard.Namespaces.MultipleUsesPerLine" />
    <rule ref="SlevomatCodingStandard.Namespaces.UseDoesNotStartWithBackslash" />
    <rule ref="SlevomatCodingStandard.Classes.EmptyLinesAroundClassBraces">
        <properties>
            <property name="linesCountAfterOpeningBrace" value="0" />
            <property name="linesCountBeforeClosingBrace" value="0" />
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Commenting.ForbiddenAnnotations">
        <properties>
            <property name="forbiddenAnnotations" type="array">
                <element value="@author" />
                <element value="@created" />
                <element value="@version" />
                <element value="@package" />
                <element value="@copyright" />
                <element value="@license" />
            </property>
        </properties>
    </rule>
    <rule ref="SlevomatCodingStandard.Commenting.EmptyComment" />
    <rule ref="SlevomatCodingStandard.Commenting.UselessFunctionDocComment" />
    <rule ref="SlevomatCodingStandard.Commenting.UselessInheritDocComment" />
    <rule ref="SlevomatCodingStandard.ControlStructures.UselessIfConditionWithReturn" />
    <rule ref="SlevomatCodingStandard.ControlStructures.UselessTernaryOperator" />
</ruleset>


File: /phpstan.src.neon
includes:
    - vendor/phpstan/phpstan-symfony/extension.neon
    - vendor/phpstan/phpstan-deprecation-rules/rules.neon
    - vendor/phpstan/phpstan-strict-rules/rules.neon

parameters:
    level: 7
    tmpDir: var/cache/_phpstan
    parallel:
        jobSize: 20
        maximumNumberOfProcesses: 16
        minimumNumberOfJobsPerProcess: 2
        processTimeout: 30.0

    symfony:
        #container_xml_path: '%rootDir%/../../../var/cache/dev/NoFlash_SnmpBridge_KernelDevDebugContainer.xml'
        console_application_loader: %rootDir%/../../../.tools/PhpStan/console-application.php
    excludes_analyse:
        - %rootDir%/../../../src/DependencyInjection/Configuration.php # semantic config will never work with static analysis

    tipsOfTheDay: false
    polluteScopeWithLoopInitialAssignments: false
    polluteScopeWithAlwaysIterableForeach: false
    polluteCatchScopeWithTryAssignments: true
    checkAlwaysTrueCheckTypeFunctionCall: true
    checkAlwaysTrueInstanceof: true
    checkAlwaysTrueStrictComparison: true
    checkExplicitMixedMissingReturn: true
    checkFunctionNameCase: true
    checkMissingClosureNativeReturnTypehintRule: true
    reportMaybesInMethodSignatures: true
    reportStaticMethodSignatures: true
    checkTooWideReturnTypesInProtectedAndPublicMethods: true
    treatPhpDocTypesAsCertain: false
    checkMissingIterableValueType: false # handled by PHPCs with more granularity

    ignoreErrors:
        - '/Method RouterOS\\Interfaces\\ClientInterface\:\:query\(\) invoked with 1 parameter, 4 required\./'


File: /README.md
# MikroTik Auto WireGuard

TL;DR: this tool lets you autoconfigure WireGuard clients on a MikroTik RouterOS and generate configs for them without 
hand-assigning any parameters.

## Why?
WireGuard is a static and **simple** [by design](https://www.wireguard.com). Thus, it does not offer any form of:

- automatic IP assignment
- route pushing
- config generation
- DHCP tunneling (or any non-IP traffic)

This is why normally to get a new node/person connection you have to:

- generate keys for the user (or ask the user for its public key)
- add new client
- find the next free IP & assign it statically a client
- create a config for the user
- make a note of which peer is which user

This tool does all that automatically for one or more users at once.

## How to use it?

### Docker
The simplest way is through Docker:

- Build image: `docker build -t mt-wg-auto https://github.com/kiler129/mikrotik-auto-wireguard.git`
- Run: `docker run -it --rm mt-wg-auto generate --help`

For more see [more detailed docs](docs/).

### Without Docker
#### Requirements
- RouterOS v7.1 [beta3 or newer](https://github.com/kiler129/mikrotik-auto-wireguard/issues/2)
- Admin user on the router with API enabled  
- PHP 7.4 or newer

As of now, as the ROS is in beta stage, there are **no promises** of compatibility. In simple terms you should execute
`bin/console generate --help` and configure it as you wish ;)

For more see [more detailed docs](docs/).

## Disclaimer
This is a beta software. As with ROSv7 it's not recommended being used in production. This software nor the author are
affiliated/supported/endorsed by [SIA Mikrotīkls](https://mikrotik.com/aboutus).




File: /resources\template\advanced.twig
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title></title>
        <style>
            @media print {
                section {
                    page-break-after: always;
                }
            }

            .qr {
                display: block;
                font-family: monospace;
                white-space: pre;
                margin: 1em 0px;
                line-height: 100%;
                zoom: 80%;
                font-size: x-large;
                letter-spacing: -1px;
            }
        </style>
    </head>
    <body>
        <section>
            <h1>VPN Configuration for {{ serverPeer.endpoint }}</h1>
            <h4>Generated on {{ "now"|date("Y-m-d H:i:s") }}</h4>
            <hr/>
        </section>

        {% for config in configs %}
            <section>
                {% if config.user is not empty %}
                    <h5>User "{{ config.user }}"</h5>
                {% else %}
                    <h5>Peer #{{ loop.index }}</h5>
                {% endif %}

                <details>
                    <summary>Show config</summary>
                    <pre>{{ config.text }}</pre>
                </details>

                <pre class="qr">{{ config.qr }}</pre><br/>
                <b>Address:</b> {{ config.clientPeer.allowedAddress|first }}<br/>
                <hr/>
            </section>
        {% endfor %}
    </body>
</html>


File: /resources\template\text.twig
**** VPN Configuration for {{ serverPeer.endpoint }} ****
Generated on {{ "now"|date("Y-m-d H:i:s") }}

------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------


{% for config in configs %}
------------------------------------------------------------------------------------------------
     INFO
--------------

    {% if config.user is not empty %}* User "{{ config.user }}"{% else %}* Peer #{{ loop.index }}{% endif %}

    * Address: {{ config.clientPeer.allowedAddress|first }}


    CONFIG
--------------
{{ config.text }}


   SCAN ME
--------------
{{ config.qr }}
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
{% endfor %}


File: /src\Command\GenerateCommand.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Command;

use NoFlash\ROSAutoWireGuard\Factory\ROSClientFactory;
use NoFlash\ROSAutoWireGuard\RouterOS\ClientProvider;
use NoFlash\ROSAutoWireGuard\RouterOS\WireGuardApi;
use NoFlash\ROSAutoWireGuard\Struct\Peer;
use NoFlash\ROSAutoWireGuard\Struct\WireguardInterface;
use NoFlash\ROSAutoWireGuard\UseCase\AddNewPeers;
use NoFlash\ROSAutoWireGuard\UseCase\BuildClientConfiguration;
use NoFlash\ROSAutoWireGuard\WireGuard\QrGenerator;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;
use Twig\Environment;
use Twig\Loader\ArrayLoader;

class GenerateCommand extends Command
{
    /** {@inheritdoc} */
    protected static $defaultName = 'generate';

    private ClientProvider $clientProvider;
    private BuildClientConfiguration $configBuilder;
    private QrGenerator $qrGenerator;
    private AddNewPeers $peersUC;
    private WireGuardApi $wgApi;
    
    private WireguardInterface $wgInterface;

    public function __construct(
        ClientProvider $clientProvider,
        BuildClientConfiguration $configBuilder,
        QrGenerator $qrGenerator,
        AddNewPeers $peersUC,
        WireGuardApi $wgApi
    ) {
        $this->clientProvider = $clientProvider;
        $this->configBuilder = $configBuilder;
        $this->qrGenerator = $qrGenerator;
        $this->peersUC = $peersUC;

        parent::__construct();
        $this->wgApi = $wgApi;
    }

    protected function configure(): void
    {
        $this->setDescription('Generates VPN peers configurations')
             ->addOption(
                 'template',
                 't',
                 InputOption::VALUE_REQUIRED,
                 'Output template',
                 \realpath(__DIR__ . '/../../resources/template/advanced.twig')
             )
             ->addOption('num', '#', InputOption::VALUE_REQUIRED, 'Number of peers to create', 1)
             ->addOption(
                 'user-list',
                 'l',
                 InputOption::VALUE_REQUIRED,
                 'File with list of users. Cannot combine with --num'
             )
             ->addOption(
                 'user',
                 'u',
                 InputOption::VALUE_REQUIRED | InputOption::VALUE_IS_ARRAY,
                 'Add username(s). Cannot combine with --num'
             )
             ->addOption('psk', 's', InputOption::VALUE_NONE, 'Whether to use additional PSKs for peers')
             ->addOption(
                 'allowed',
                 'a',
                 InputOption::VALUE_REQUIRED | InputOption::VALUE_IS_ARRAY,
                 'Network(s) which should be router through VPN',
                 ['0.0.0.0/0', '::/0']
             )
             ->addOption('keep-alive', 'k', InputOption::VALUE_REQUIRED, 'Keep-alive in seconds')
             ->addOption('interface', 'i', InputOption::VALUE_REQUIRED, 'WireGuard interface name', 'wireguard1')
             ->addOption(
                 'pool',
                 'o',
                 InputOption::VALUE_REQUIRED,
                 'IP > Pool to get addresses from. If not set it will use addresses on the interface'
             )
             ->addOption(
                 'vpn-host',
                 null,
                 InputOption::VALUE_REQUIRED,
                 'Externally-accessible VPN gateway host/IP (default: router-host)'
             )
             ->addOption(
                 'vpn-port',
                 null,
                 InputOption::VALUE_REQUIRED,
                 'Externally-accessible VPN gateway port (default: read from interface)'
             )
             ->addOption(
                 'public-key',
                 null,
                 InputOption::VALUE_REQUIRED,
                 'Public key to use (default: read from interface)'
             )
             ->addArgument('router-host', InputArgument::REQUIRED, 'Host/IP of a MikroTik router')
             ->addArgument('router-username', InputArgument::REQUIRED, 'Username for a MikroTik router')
             ->addArgument('router-password', InputArgument::REQUIRED, 'Password for a MikroTik router')
        ;
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $users = $this->createUsersList($input, $output);
        if ($users === null) {
            return self::FAILURE;
        }

        $this->configureClient($input);
        $this->populateServer($input);

        $peers = $this->generatePeers($input, $users);

        /** @var string $tpl */
        $tpl = $input->getOption('template');
        $output->write($this->renderTemplate($tpl, $peers));

        return self::SUCCESS;
    }

    private function configureClient(InputInterface $input): void
    {
        /** @var string|null $host */
        $host = $input->getArgument('router-host');
        /** @var string|null $user */
        $user = $input->getArgument('router-username');
        /** @var string|null $pass */
        $pass = $input->getArgument('router-password');

        $client = ROSClientFactory::createClient((string)$host, (string)$user, (string)$pass);

        $this->clientProvider->setClient($client);
    }

    /**
     * @return array<string|null>|null
     */
    private function createUsersList(InputInterface $input, OutputInterface $output): ?array
    {
        $hasNum = $input->hasParameterOption(['--num', '-#']);
        $hasUsers = $input->hasParameterOption(['--user', '-u']);
        $hasUserList = $input->hasParameterOption(['--user-list', '-l']);

        if ($hasNum && ($hasUsers || $hasUserList)) {
            $output->writeln('<error>Cannot combine --num with either --user or --user-list</error>');

            return null;
        }

        $users = [];
        /** @var string $userListFile */
        $userListFile = $input->getOption('user-list');
        if ($hasUserList && $userListFile !== '') {
            $users = \file($userListFile, \FILE_IGNORE_NEW_LINES|\FILE_SKIP_EMPTY_LINES);
            if ($users === false) {
                $output->writeln('<error>Failed to read --user-list file</error>');

                return null;
            }
        }

        if ($hasUsers) {
            /** @var array<string> $userArg */
            $userArg = $input->getOption('user');
            return \array_merge($users, $userArg);
        }

        if (\count($users) !== 0) {
            return $users;
        }

        //Stupid... but for it will not be 30,000 elements at once but just a couple ;)
        /** @var string|int|null $autoUsers */
        $autoUsers = $input->getOption('num');
        return \array_fill(0, (int)$autoUsers, null);
    }

    private function populateServer(InputInterface $input): void
    {
        /** @var string|null $host */
        $host = $input->getOption('vpn-host');
        if ($host === null || $host === '') {
            /** @var string $host */
            $host = $input->getArgument('router-host');
        }

        /** @var int|string|null $port */
        $port = $input->getOption('vpn-port');
        if ($port === null || $port === '') {
            $port = $this->getWGInterface($input)->listenPort;
        }
        $port = (int)$port;

        /** @var string|null $publicKey */
        $publicKey = $input->getOption('public-key'); //TODO: get from interface
        if ($publicKey === null || $publicKey === '') {
            $publicKey = $this->getWGInterface($input)->publicKey;
        }

        $this->configBuilder
            ->setServerAddress($host, $port)
            ->setServeryKey($publicKey)
        ;

        /** @var string|int|null $keepAliveSeconds */
        $keepAliveSeconds = $input->getOption('keep-alive');
        $keepAliveSeconds = (int)$keepAliveSeconds;
        if ($keepAliveSeconds > 0) {
            $this->configBuilder->setKeepAlive($keepAliveSeconds);
        }

        /** @var string[] $allowedIps */
        $allowedIps = $input->getOption('allowed');
        foreach ($allowedIps as $allowed) {
            $this->configBuilder->addAllowedNetwork($allowed);
        }
    }

    /**
     * @param array<string|null> $users
     *
     * @return \SplObjectStorage<Peer, string|null>
     */
    private function generatePeers(InputInterface $input, array $users): \SplObjectStorage
    {
        /** @var string $interface */
        $interface = $input->getOption('interface');
        /** @var string|null $pool */
        $pool = $input->getOption('pool');
        if ($pool === '') {
            $pool = null;
        }
        /** @var bool $usePsk */
        $usePsk = $input->getOption('psk');

        $comments = [];
        foreach ($users as $username) {
            $comments[] = ($username === null) ? null : \sprintf('User: %s', $username);
        }
        $peers = $this->peersUC->addWithConsecutiveIPs($interface, $pool, $usePsk, \count($users), $comments);
        $out = new \SplObjectStorage();
        $i = 0;
        foreach ($users as $user) {
            $peer = $peers[$i++];
            if ($user !== null) {
                $peer->comment = 'User: ' . $user;
            }
            $out->attach($peer, $user);
        }

        return $out;
    }

    /**
     * @param \SplObjectStorage<Peer, string|null> ...$clients
     *
     */
    private function renderTemplate(string $templateFile, \SplObjectStorage $clients): string
    {
        $configs = [];
        foreach ($clients as $clientPeer) {
            $config = $this->configBuilder->buildForClient($clientPeer);
            $configs[] = [
                'user' => $clients->getInfo(),
                'clientPeer' => $clientPeer,
                'qr' => $this->qrGenerator->generateConfiguration($config),
                'text' => $config->render(),
            ];
        }

        $varsStack = [
            'serverPeer' => $this->configBuilder->getServerPeer(),
            'configs' => $configs,
        ];
        $loader = new ArrayLoader(['template' => \file_get_contents($templateFile),]);
        $twig = new Environment($loader);

        return $twig->render('template', $varsStack);
    }

    private function getWGInterface(InputInterface $input): WireguardInterface
    {
        if (!isset($this->wgInterface)) {
            /** @var string $interface */
            $interface = $input->getOption('interface');
            $this->wgInterface = $this->wgApi->getInterface($interface);
        }

        return $this->wgInterface;
    }
}


File: /src\ContainerProvider.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard;

use Symfony\Bridge\ProxyManager\LazyProxy\Instantiator\RuntimeInstantiator;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\DependencyInjection\Loader\PhpFileLoader;

final class ContainerProvider
{
    private static ContainerInterface $container;

    private function __construct()
    {
        //noop
    }

    public static function getAppContainer(): ContainerInterface
    {
        if (isset(self::$container)) {
            return self::$container;
        }

        self::$container = new ContainerBuilder();
        self::$container->setProxyInstantiator(new RuntimeInstantiator());
        $loader = new PhpFileLoader(self::$container, new FileLocator(__DIR__ . '/../config'));
        $loader->load('services.php');
        self::$container->compile();

        return self::$container;
    }
}


File: /src\Exception\InvalidArgumentException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class InvalidArgumentException extends \InvalidArgumentException
{

}


File: /src\Exception\InvalidFieldException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class InvalidFieldException extends \InvalidArgumentException
{
    public function __construct(string $field)
    {
        parent::__construct(\sprintf('Field "%s" is invalid', $field));
    }
}


File: /src\Exception\LogicException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class LogicException extends \LogicException
{
}


File: /src\Exception\MissingValueException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class MissingValueException extends \RuntimeException
{
}


File: /src\Exception\ROSException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class ROSException extends \RuntimeException
{
}


File: /src\Exception\SectionAlreadyExistsException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

use NoFlash\ROSAutoWireGuard\WireGuard\Configuration\ConfigurationSection;

class SectionAlreadyExistsException extends \OverflowException
{
    public function __construct(ConfigurationSection $section)
    {
        parent::__construct(\sprintf('Section "%s" already exists', $section::getSectionName()));
    }
}


File: /src\Exception\UnderflowException.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Exception;

class UnderflowException extends \UnderflowException
{
}


File: /src\Factory\ROSClientFactory.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Factory;

use RouterOS\Client;

class ROSClientFactory
{
    public static function createClient(string $host, string $user, string $password, bool $useSSL = false): Client
    {
        return new Client(['host' => $host, 'user' => $user, 'pass' => $password, 'ssl' => $useSSL]);
    }
}


File: /src\NetworkUtil.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard;

use IPTools\IP;
use IPTools\Network;
use IPTools\Range;
use NoFlash\ROSAutoWireGuard\Exception\UnderflowException;
use NoFlash\ROSAutoWireGuard\Struct\Peer;

class NetworkUtil
{
    /**
     * @param array<Range> $available
     * @param array<Range> $usedRanges
     *
     * @return array<IP>
     *
     * phpcs:disable ObjectCalisthenics.Metrics.MaxNestingLevel
     */
    public function findNextAddresses(array $available, array $usedRanges, int $howMany = 1): array
    {
        $foundCt = 0;
        $found = [];

        /** @var Range $pool */
        foreach ($available as $pool) {
            foreach ($pool as $newIp) {
                /** @var Range $usedRange */
                foreach ($usedRanges as $usedRange) {
                    if ($usedRange->contains($newIp)) {
                        continue 2;
                    }
                }

                $found[] = $newIp;
                if (++$foundCt === $howMany) { //Found enough, there's still more left in the pool
                    return $found;
                }
            }
        }

        if ($foundCt < $howMany) {
            throw new UnderflowException(
                \sprintf('Not enough addresses available - requested %d, found %d free', $howMany, $foundCt)
            );
        }

        return $found; //Found as many as needed and no more
    }

    /**
     * @return array<Range>
     */
    public function networkToRange(Network ...$networks): array
    {
        $out = [];
        foreach ($networks as $network) {
            $out[] = $network->getHosts();
        }

        return $out;
    }

    public function addressToNetwork(string $address): Network
    {
        if (\strpos($address, '/') === false) {
            $address .= '/32'; //Single address
        }

        return Network::parse($address);
    }

    /**
     * @return array<Range>
     */
    public function getUsedPeersAddresses(Peer ...$peers): array
    {
        $out = [];
        foreach ($peers as $peer) {
            foreach ($peer->allowedAddress as $address) {
                $out[] = $this->addressToNetwork($address)->getHosts();
            }
        }

        return $out;
    }
}


File: /src\RouterOS\AbstractApi.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\RouterOS;

use NoFlash\ROSAutoWireGuard\NetworkUtil;
use RouterOS\Interfaces\ClientInterface;

abstract class AbstractApi
{
    protected ClientProvider $clientProvider;
    protected ROSUtil $rosUtil;
    protected NetworkUtil $networkUtil;

    public function __construct(ClientProvider $clientProvider, ROSUtil $rosUtil, NetworkUtil $networkUtil)
    {
        $this->clientProvider = $clientProvider;
        $this->rosUtil = $rosUtil;
        $this->networkUtil = $networkUtil;
    }

    protected function getClient(): ClientInterface
    {
        return $this->clientProvider->getClient();
    }
}


File: /src\RouterOS\ClientProvider.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\RouterOS;

use NoFlash\ROSAutoWireGuard\Exception\LogicException;
use RouterOS\Interfaces\ClientInterface;

/**
 * Goes around Symfony Container limitations (we need to create client after the app is started)
 */
class ClientProvider
{
    private ClientInterface $client;

    public function setClient(ClientInterface $client): void
    {
        if (isset($this->client)) {
            throw new LogicException('Client is already set - you cannot change it'); //prevent weird bugs...
        }

        $this->client = $client;
    }

    public function getClient(): ClientInterface
    {
        if (isset($this->client)) {
            return $this->client;
        }

        throw new LogicException('Client is not set. Did you forget to call setClient()?');
    }
}


File: /src\RouterOS\IpApi.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\RouterOS;

use IPTools\Network;
use IPTools\Range;
use RouterOS\Query;

class IpApi extends AbstractApi
{
    /**
     * @return array<Network>
     */
    public function getAddressesOnInterface(string $interface): array
    {
        $query = (new Query('/ip/address/print'));
        $query->where('interface', $interface);

        //This is valid in implementation but the interface is broken...
        $result = $this->getClient()->query($query)->read();
        $out = [];
        foreach (\array_column($result, 'address') as $addr) {
            $out[] = $this->networkUtil->addressToNetwork($addr);
        }

        return $out;
    }

    /**
     * @return array<Range>
     */
    public function getIpPool(string $name): array
    {
        $query = (new Query('/ip/pool/print'));
        $query->where('name', $name);

        //This is valid in implementation but the interface is broken...
        $result = $this->getClient()->query($query)->read();
        $out = [];
        foreach (\array_column($result, 'ranges') as $addrList) {
            foreach ($this->rosUtil->listToArray($addrList) as $addr) {
                $out[] = Range::parse($addr);
            }
        }

        return $out;
    }
}


File: /src\RouterOS\ROSUtil.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\RouterOS;

class ROSUtil
{
    /**
     * @return array<string>
     */
    public function listToArray(string $rosList): array
    {
        $out = [];
        foreach (\explode(',', $rosList) as $item) {
            $out[] = \trim($item);
        }
        return $out;
    }
}


File: /src\RouterOS\WireGuardApi.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\RouterOS;

use NoFlash\ROSAutoWireGuard\Exception\ROSException;
use NoFlash\ROSAutoWireGuard\Struct\Peer;
use NoFlash\ROSAutoWireGuard\Struct\WireguardInterface;
use RouterOS\Query;

class WireGuardApi extends AbstractApi
{
    public function addPeer(Peer $peer): void
    {
        $query = (new Query('/interface/wireguard/peers/add'));
        foreach ($peer->asSettableArray() as $k => $v) {
            $query->equal($k, $v);
        }

        //Will return ['after' => ['ret' => 'ROS ID']] on success
        //Will return ['after' => ['message' => 'error']] on failure
        //FYI: While phpStorm complains this is valid in implementation but the interface is broken...
        $result = $this->getClient()->query($query)->read();

        if (isset($result['after']['ret'])) {
            return;
        }

        if (isset($result['after']['message'])) {
            throw new ROSException('RouterOS error while adding peer: ' . $result['after']['message']);
        }

        throw new ROSException('Unexpected RouterOS response while adding peer: ' . \print_r($result, true));
    }

    /**
     * @return array<Peer>
     */
    public function getPeers(?string $interface = null): array
    {
        $query = (new Query('/interface/wireguard/peers/print'));
        if ($interface !== null) {
            $query->where('interface', $interface);
        }

        //FYI: While phpStorm complains this is valid in implementation but the interface is broken...
        $result = $this->getClient()->query($query)->read();
        $out = [];
        foreach ($result as $apiPeer) {
            $out[] = $peer = new Peer();
            $peer->interface = $apiPeer['interface'];
            $peer->publicKey = $apiPeer['public-key'];
            $peer->endpointAddress = ($apiPeer['endpoint-address'] ?? null) ?: null;
            $peer->endpointPort = ($apiPeer['endpoint-port'] ?? null) ?: null;
            $peer->allowedAddress = $this->rosUtil->listToArray($apiPeer['allowed-address'] ?? '') ?: null;
            $peer->presharedKey = ($apiPeer['preshared-key'] ?? null) ?: null;
            $peer->rx = (int)($apiPeer['rx'] ?? 0);
            $peer->tx = (int)($apiPeer['tx'] ?? 0);
            $peer->lastHandshake = ($apiPeer['last-handshake'] ?? null) ?: null;
            $peer->persistentKeepalive = (int)($apiPeer['persistent-keepalive'] ?? null) ?: null;
        }

        return $out;
    }

    public function getInterface(string $interface): WireguardInterface
    {
        $query = (new Query('/interface/wireguard/print'));
        $query->where('name', $interface);

        //FYI: While phpStorm complains this is valid in implementation but the interface is broken...
        $result = $this->getClient()->query($query)->read();
        if (\count($result) < 1) {
            throw new ROSException(\sprintf('There is no wireguard interface named "%s"', $interface));
        }

        $apiInterface = $result[\array_key_first($result)];
        $wgInterface = new WireguardInterface(
            $apiInterface['name'],
            (int)($apiInterface['mtu'] ?? 0),
            (int)($apiInterface['listen-port'] ?? 0),
        );

        $wgInterface->privateKey = $apiInterface['private-key'];
        $wgInterface->publicKey = $apiInterface['public-key'];

        return $wgInterface;
    }
}


File: /src\Struct\InterfaceInterface.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Struct;

interface InterfaceInterface
{
    public function getName(): string;
}


File: /src\Struct\Peer.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Struct;

final class Peer
{
    use ROSStructHelperTrait;

    protected const API_SETTABLE = [
        'interface',
        'publicKey',
        'endpointAddress',
        'endpointPort',
        'allowedAddress',
        'presharedKey',
        'comment',
    ];

    public string $interface;
    public string $publicKey;
    public ?string $privateKey;
    public ?string $endpointAddress = null;
    public ?int $endpointPort = null;
    public ?string $comment = null;

    /** @var array<string> */
    public array $allowedAddress = [];
    public ?string $presharedKey   = null;
    public int $rx             = 0;
    public int $tx             = 0;
    public ?string $lastHandshake  = null;
    public ?int $persistentKeepalive = null;


    protected static function getApiSettableFields(): array
    {
        return self::API_SETTABLE;
    }
}


File: /src\Struct\ROSStructHelperTrait.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Struct;

trait ROSStructHelperTrait
{
    /**
     * @return array<string,string>
     */
    public function asSettableArray(): array
    {
        $out = [];
        foreach (static::getApiSettableFields() as $field) {
            if ($this->$field === null) {
                continue;
            }

            $val = $this->$field;
            if (\is_array($val)) {
                $val = \implode(',', $val);
            }

            $out[\strtolower(\preg_replace('/(?<!^)[A-Z]/', '-$0', $field))] = $val;
        }

        return $out;
    }

    /**
     * @return array<string>
     */
    abstract protected static function getApiSettableFields(): array;
}


File: /src\Struct\WireguardInterface.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\Struct;

class WireguardInterface implements InterfaceInterface
{
    use ROSStructHelperTrait;

    protected const API_SETTABLE = [
        'name',
        'mtu',
        'listenPort',
        'privateKey',
    ];

    public string $name;
    public int $mtu;
    public int $listenPort;
    public ?string $privateKey;
    public ?string $publicKey;

    public function __construct(string $name, int $mtu, int $listenPort)
    {
        $this->name = $name;
        $this->mtu = $mtu;
        $this->listenPort = $listenPort;
    }

    protected static function getApiSettableFields(): array
    {
        return self::API_SETTABLE;
    }

    public function getName(): string
    {
        return $this->name;
    }
}


File: /src\UseCase\AddNewPeers.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\UseCase;

use IPTools\Range;
use NoFlash\ROSAutoWireGuard\Exception\InvalidArgumentException;
use NoFlash\ROSAutoWireGuard\NetworkUtil;
use NoFlash\ROSAutoWireGuard\RouterOS\IpApi;
use NoFlash\ROSAutoWireGuard\RouterOS\WireGuardApi;
use NoFlash\ROSAutoWireGuard\Struct\Peer;
use NoFlash\ROSAutoWireGuard\WireGuard\KeyGenerator;

class AddNewPeers
{
    private IpApi $rosIpApi;
    private WireGuardApi $rosWGApi;
    private NetworkUtil $networkUtil;
    private KeyGenerator $keyGenerator;

    public function __construct(
        IpApi $rosIpApi,
        WireGuardApi $rosWGApi,
        NetworkUtil $networkUtil,
        KeyGenerator $keyGenerator
    ) {
        $this->rosIpApi = $rosIpApi;
        $this->rosWGApi = $rosWGApi;
        $this->networkUtil = $networkUtil;
        $this->keyGenerator = $keyGenerator;
    }

    /**
     * @param array<string> $comments
     *
     * @return array<Peer>
     */
    public function addWithConsecutiveIPs(
        string $interface,
        ?string $usePool = null,
        ?bool $usePsk = false,
        int $howMany = 1,
        ?array $comments = null
    ): array {
        //First get addresses
        $availableIps = $usePool === null
            ? $this->rosIpApi->getAddressesOnInterface($interface) : $this->rosIpApi->getIpPool($usePool);
        $usedIps = $this->networkUtil->getUsedPeersAddresses(...$this->rosWGApi->getPeers($interface));

        foreach ($availableIps as $availableIp) { //Assigning subnet address (e.g. 10.0.0.0) will cause WG to not work
            $net = $availableIp->getNetwork();
            $usedIps[] = new Range($net, $net); //For some reason doing $availableIps->exclude() doesn't work
        }
        $newIps = $this->networkUtil->findNextAddresses($availableIps, $usedIps, $howMany);

        if ($comments !== null) {
            \reset($comments);

            if (\count($comments) !== $howMany) {
                throw new InvalidArgumentException(
                    \sprintf(
                        'Comments array (when present) must be the same length (now %d) as $howMany (now %d) specifies',
                        \count($comments),
                        $howMany
                    )
                );
            }
        }

        //Create new peers
        $newPeers = [];
        foreach ($newIps as $ip) {
            $peer = new Peer();
            $peer->interface = $interface;
            $peer->allowedAddress = [$ip . '/32'];

            //Note: only public key is actually saved, private key is only available on Peer() to print the configs
            ['pub' => $peer->publicKey, 'priv' => $peer->privateKey] = $this->keyGenerator->generateBase64Keypair();
            if ($usePsk) {
                $peer->presharedKey = $this->keyGenerator->generateBase64Psk();
            }

            if ($comments !== null) {
                $peer->comment = \current($comments);
                next($comments);
            }

            $this->rosWGApi->addPeer($peer); //Will throw on error
            $newPeers[] = $peer;
        }

        return $newPeers;
    }
}


File: /src\UseCase\BuildClientConfiguration.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\UseCase;

use IPTools\Network;
use NoFlash\ROSAutoWireGuard\NetworkUtil;
use NoFlash\ROSAutoWireGuard\Struct\Peer;
use NoFlash\ROSAutoWireGuard\WireGuard\Configuration\Configuration;
use NoFlash\ROSAutoWireGuard\WireGuard\Configuration\PeerProjector;

class BuildClientConfiguration
{
    private Peer $serverPeer;
    private PeerProjector $peerProjector;

    private NetworkUtil $networkUtil;

    public function __construct(PeerProjector $peerProjector, NetworkUtil $networkUtil)
    {
        $this->serverPeer = new Peer();
        $this->peerProjector = $peerProjector;
        $this->peerProjector->setServer($this->serverPeer);
        $this->networkUtil = $networkUtil;
    }

    public function setServerAddress(string $host, int $port): self
    {
        if (\filter_var($host, \FILTER_VALIDATE_IP, \FILTER_FLAG_IPV6) !== false) {
            $host = \sprintf('[%s]', $host);
        }

        $this->serverPeer->endpointAddress = $host;
        $this->serverPeer->endpointPort = $port;

        return $this;
    }

    public function setServeryKey(string $publicKey): self
    {
        //TODO: verify it's NOT a private key to prevent accidental leak
        $this->serverPeer->publicKey = $publicKey;

        return $this;
    }

    /**
     * @param Network|string $addressOrNetwork
     */
    public function addAllowedNetwork($addressOrNetwork): self
    {
        if (!($addressOrNetwork instanceof Network)) {
            $addressOrNetwork = $this->networkUtil->addressToNetwork($addressOrNetwork);
        }

        $this->serverPeer->allowedAddress[] = (string)$addressOrNetwork;

        return $this;
    }

    public function setKeepAlive(?int $seconds): self
    {
        $this->serverPeer->persistentKeepalive = $seconds;

        return $this;
    }

    public function buildForClient(Peer $client): Configuration
    {
        return $this->peerProjector->createClientConfiguration($client);
    }

    public function getServerPeer(): Peer
    {
        return $this->serverPeer;
    }
}


File: /src\WireGuard\Configuration\AbstractSection.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

use NoFlash\ROSAutoWireGuard\Exception\InvalidFieldException;

abstract class AbstractSection implements ConfigurationSection
{
    protected const VALID_FIELDS_MAP = [];

    /** @var array<string,string> */
    private array $fields = [];

    public function setField(string $key, string $value): void
    {
        if (!$this->isValidField($key)) {
            throw new InvalidFieldException($key);
        }

        $this->fields[$key] = $value;
    }

    /**
     * @return array<string,string>
     */
    public function getFields(): array
    {
        return $this->fields;
    }

    public function render(): string
    {
        $out = \sprintf("[%s]\n", static::getSectionName());
        foreach ($this->fields as $k => $v) {
            $out .= \sprintf("%s = %s\n", $k, $v);
        }
        $out .= "\n";

        return $out;
    }

    protected function setInsensitiveField(string $name, string $value): void
    {
        $fieldKey = static::VALID_FIELDS_MAP[\strtolower($name)] ?? null;
        if ($fieldKey === null) {
            throw new InvalidFieldException($name);
        }

        $this->setField($fieldKey, $value);
    }

    protected function isValidField(string $name): bool
    {
        return isset(static::VALID_FIELDS_MAP[\strtolower($name)]);
    }

    /**
     * @param string|int|float $value
     */
    public function __set(string $name, $value): void
    {
        $this->setInsensitiveField($name, (string)$value);
    }
}


File: /src\WireGuard\Configuration\Configuration.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

use NoFlash\ROSAutoWireGuard\Exception\SectionAlreadyExistsException;

class Configuration implements RenderableInterface
{
    /**
     * @var ConfigurationSection[]
     */
    private array $sections = [];

    public function addSection(ConfigurationSection $section): void
    {
        $name = $section::getSectionName();
        if (isset($this->sections[$name])) {
            throw new SectionAlreadyExistsException($section);
        }

        $this->sections[$name] = $section;
    }

    public function render(): string
    {
        $out = '';
        foreach ($this->sections as $section) {
            $out .= $section->render();
        }

        return $out;
    }
}


File: /src\WireGuard\Configuration\ConfigurationSection.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

interface ConfigurationSection extends RenderableInterface
{
    public static function getSectionName(): string;

    /**
     * @return array<string,string>
     */
    public function getFields(): array;
}


File: /src\WireGuard\Configuration\InterfaceSection.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

/**
 * @property-write string $privateKey
 * @property-write string $address
 * @property-write string $dns
 */
class InterfaceSection extends AbstractSection
{
    //There's probably more overall, but I wasn't able to find comprehensive list
    protected const VALID_FIELDS_MAP = [
        'privatekey' => 'PrivateKey',
        'address' => 'Address',
        'dns' => 'DNS',
    ];

    public static function getSectionName(): string
    {
        return 'Interface';
    }
}


File: /src\WireGuard\Configuration\PeerProjector.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

use NoFlash\ROSAutoWireGuard\Exception\MissingValueException;
use NoFlash\ROSAutoWireGuard\Struct\Peer;

class PeerProjector
{
    private Peer $server;

    public function createClientConfiguration(Peer $peer): Configuration
    {
        $config = new Configuration();
        $config->addSection($this->createInterface($peer));
        $config->addSection($this->createRemotePeer($peer));

        return $config;
    }

    private function createInterface(Peer $client): InterfaceSection
    {
        $section = new InterfaceSection();

        if (!isset($client->privateKey)) {
            throw new MissingValueException('Unable to generate configuration: "client" peer has no private key');
        }
        $section->privateKey = $client->privateKey;

        if (\count($client->allowedAddress) === 0) {
            throw new MissingValueException('Unable to generate configuration: "client" peer has no address');
        }
        $section->address = $client->allowedAddress[\array_key_first($client->allowedAddress)];
        //TODO: what if there's many?

        return $section;
    }

    private function createRemotePeer(Peer $client): PeerSection
    {
        $section = new PeerSection();

        if (!isset($this->server->publicKey) || $this->server->publicKey === '') {
            throw new MissingValueException('Unable to generate configuration: "server" peer has no public key');
        }
        $section->publicKey = $this->server->publicKey;

        if (isset($client->presharedKey)) {
            $section->presharedKey = $client->presharedKey;
        }

        //Hint: you probably wanted [0.0.0.0/0, ::/0] to send all traffic via tunnel
        if (\count($this->server->allowedAddress) === 0) {
            throw new MissingValueException('Unable to generate configuration: "server" does not have any allowed IPs');
        }
        $section->allowedIPs = \implode(', ', $this->server->allowedAddress);

        if (!isset($this->server->endpointAddress)) {
            throw new MissingValueException('Unable to generate configuration: "server" has no endpoint address');
        }
        if (!isset($this->server->endpointPort)) {
            throw new MissingValueException('Unable to generate configuration: "server" has no endpoint port');
        }
        $section->endpoint = \sprintf('%s:%d', $this->server->endpointAddress, $this->server->endpointPort);

        if (isset($this->server->persistentKeepalive)) {
            $section->persistentKeepalive = $this->server->persistentKeepalive;
        }

        return $section;
    }

    public function setServer(Peer $server): void
    {
        $this->server = $server;
    }
}


File: /src\WireGuard\Configuration\PeerSection.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

/**
 * @property-write string $publicKey
 * @property-write string $presharedKey
 * @property-write string $allowedIPs
 * @property-write string $endpoint
 * @property-write int    $persistentKeepalive
 */
class PeerSection extends AbstractSection
{
    //There's probably more overall, but I wasn't able to find comprehensive list
    protected const VALID_FIELDS_MAP = [
        'publickey' => 'PublicKey',
        'presharedkey' => 'PresharedKey',
        'allowedips' => 'AllowedIPs',
        'endpoint' => 'Endpoint',
        'persistentkeepalive' => 'PersistentKeepalive',
    ];

    public static function getSectionName(): string
    {
        return 'Peer';
    }
}


File: /src\WireGuard\Configuration\RenderableInterface.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard\Configuration;

interface RenderableInterface
{
    public function render(): string;
}


File: /src\WireGuard\KeyGenerator.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard;

class KeyGenerator
{
    /**
     * @return array{priv: string, pub: string}
     */
    public function generateBase64Keypair(): array
    {
        $keypair = \sodium_crypto_kx_keypair();

        return [
            'priv' => \base64_encode(\sodium_crypto_kx_secretkey($keypair)),
            'pub' => \base64_encode(\sodium_crypto_kx_publickey($keypair)),
        ];
    }

    public function generateBase64Psk(): string
    {
        //256 bit is the default (and only) wg psk length
        return \base64_encode(\random_bytes(32));
    }
}


File: /src\WireGuard\QrGenerator.php
<?php
declare(strict_types=1);

namespace NoFlash\ROSAutoWireGuard\WireGuard;

use BaconQrCode\Writer;
use NoFlash\ROSAutoWireGuard\WireGuard\Configuration\Configuration;

class QrGenerator
{
    private Writer $qrWriter;

    public function __construct(Writer $qrWriter)
    {
        $this->qrWriter = $qrWriter;
    }

    public function generateConfiguration(Configuration $config): string
    {
        return $this->qrWriter->writeString($config->render());
    }
}


