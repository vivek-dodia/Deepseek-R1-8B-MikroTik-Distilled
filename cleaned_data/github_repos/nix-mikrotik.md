# Repository Information
Name: nix-mikrotik

# Directory Structure
Directory structure:
└── github_repos/nix-mikrotik/
    ├── .envrc
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
    │   │       ├── pack-aa7a0ba9264c9d1eddb80c39edab0d3b5aabf18e.idx
    │   │       └── pack-aa7a0ba9264c9d1eddb80c39edab0d3b5aabf18e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── examples/
    │   └── configuration.nix
    ├── LICENSE
    ├── mikrotik.nix
    ├── nix-mikrotik-rs/
    │   ├── .gitignore
    │   ├── Cargo.lock
    │   ├── Cargo.toml
    │   └── src/
    │       └── main.rs
    ├── README.org
    └── shell.nix


# Content
File: /.envrc
use_nix


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/Plommonsorbet/nix-mikrotik.git
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
0000000000000000000000000000000000000000 c6a1ce850ef924953b383eb412a3e8e89df748d0 vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/Plommonsorbet/nix-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c6a1ce850ef924953b383eb412a3e8e89df748d0 vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/Plommonsorbet/nix-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c6a1ce850ef924953b383eb412a3e8e89df748d0 vivek-dodia <vivek.dodia@icloud.com> 1738605970 -0500	clone: from https://github.com/Plommonsorbet/nix-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c6a1ce850ef924953b383eb412a3e8e89df748d0 refs/remotes/origin/master


File: /.git\refs\heads\master
c6a1ce850ef924953b383eb412a3e8e89df748d0


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /examples\configuration.nix
{
  "/interface bridge" = [

    {
      auto-mac = "no";
      comment = "defconf";
      name = "bridge";
    }
    { name = "wifi"; }
  ];
  "/interface list" = [ { name = "LAN"; } { name = "WAN"; } ];

  "/ip pool" = [
    {
      name = "wired-pool";
      ranges = "10.10.10.10-10.10.10.254";
    }
    {
      name = "wifi-pool";
      ranges = "10.10.11.10-10.10.11.254";
    }
  ];

  "/ip dhcp-server" = [
    {
      address-pool = "wired-pool";
      disabled = "no";
      interface = "bridge";
      name = "wired-dhcp";
    }
    {
      address-pool = "wifi-pool";
      disabled = "no";
      interface = "wifi";
      name = "wifi-dhcp";
    }
  ];

  "/interface bridge port" = [
    {
      bridge = "bridge";
      interface = "ether2";
    }
    {
      bridge = "bridge";
      interface = "ether3";
    }
    {
      bridge = "bridge";
      interface = "ether4";
    }
    {
      bridge = "wifi";
      interface = "ether5";
    }
    {
      bridge = "bridge";
      interface = "sfp1";
    }
  ];

  "/ip neighbor discovery-settings" = { discover-interface-list = "none"; };

  "/interface list member" = [
    {
      interface = "bridge";
      list = "LAN";
    }
    {
      interface = "ether1";
      list = "WAN";
    }

  ];

  "/ip address" = [
    {
      address = "10.10.10.1/24";
      interface = "ether2";
      network = "10.10.10.0";
    }
    {
      address = "10.10.11.1/24";
      interface = "wifi";
      network = "10.10.11.0";
    }
  ];
  "/ip cloud" = {
    update-time = "no";

  };

  "/ip dhcp-client" = [{
    disabled = "no";
    interface = "ether1";
  }];
  "/ip dhcp-server network" = [
    {
      address = "10.10.10.0/24";
      gateway = "10.10.10.1";
      netmask = "24";
    }
    {
      address = "10.10.11.0/24";
      gateway = "10.10.11.1";
      netmask = "24";
    }
  ];

  "/ip dns" = {

    no_label = {
      allow-remote-requests = "yes";
      servers = "1.1.1.1,1.0.0.1";
    };
  };
  "/ip dns static" = [{
    address = "10.10.10.1";
    name = "router.lan";
  }];
  "/ip firewall address-list" = [
    {
      address = "10.10.10.10-10.10.10.10.254";
      list = "allowed_to_router";
    }
    {
      action = "accept";
      chain = "input";
      src-address-list = "allowed_to_router";
    }
    {
      action = "accept";
      chain = "input";
      protocol = "icmp";
    }
  ];

  "/ip service" = {
    telnet = { disabled = "yes"; };
    www = { disabled = "yes"; };
    ftp = { disabled = "yes"; };
    winbox = { disabled = "yes"; };
    api-ssl = { disabled = "yes"; };
    api = { disabled = "yes"; };

  };

  "/ip ssh" = { strong-crypto = "yes"; };
  "/system clock" = { time-zone-name = "Europe/Stockholm"; };
  "/system identity" = { name = "nidas"; };
  "/tool bandwidth-server" = { enabled = "no"; };
  "/tool mac-server" = { allowed-interface-list = "none"; };
  "/tool mac-server mac-winbox" = { allowed-interface-list = "none"; };
  "/tool mac-server ping" = { enabled = "no"; };

}


File: /LICENSE
Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION,
AND DISTRIBUTION

   1. Definitions.

      

"License" shall mean the terms and conditions for use, reproduction, and distribution
as defined by Sections 1 through 9 of this document.

      

"Licensor" shall mean the copyright owner or entity authorized by the copyright
owner that is granting the License.

      

"Legal Entity" shall mean the union of the acting entity and all other entities
that control, are controlled by, or are under common control with that entity.
For the purposes of this definition, "control" means (i) the power, direct
or indirect, to cause the direction or management of such entity, whether
by contract or otherwise, or (ii) ownership of fifty percent (50%) or more
of the outstanding shares, or (iii) beneficial ownership of such entity.

      

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions
granted by this License.

      

"Source" form shall mean the preferred form for making modifications, including
but not limited to software source code, documentation source, and configuration
files.

      

"Object" form shall mean any form resulting from mechanical transformation
or translation of a Source form, including but not limited to compiled object
code, generated documentation, and conversions to other media types.

      

"Work" shall mean the work of authorship, whether in Source or Object form,
made available under the License, as indicated by a copyright notice that
is included in or attached to the work (an example is provided in the Appendix
below).

      

"Derivative Works" shall mean any work, whether in Source or Object form,
that is based on (or derived from) the Work and for which the editorial revisions,
annotations, elaborations, or other modifications represent, as a whole, an
original work of authorship. For the purposes of this License, Derivative
Works shall not include works that remain separable from, or merely link (or
bind by name) to the interfaces of, the Work and Derivative Works thereof.

      

"Contribution" shall mean any work of authorship, including the original version
of the Work and any modifications or additions to that Work or Derivative
Works thereof, that is intentionally submitted to Licensor for inclusion in
the Work by the copyright owner or by an individual or Legal Entity authorized
to submit on behalf of the copyright owner. For the purposes of this definition,
"submitted" means any form of electronic, verbal, or written communication
sent to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems, and
issue tracking systems that are managed by, or on behalf of, the Licensor
for the purpose of discussing and improving the Work, but excluding communication
that is conspicuously marked or otherwise designated in writing by the copyright
owner as "Not a Contribution."

      

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf
of whom a Contribution has been received by Licensor and subsequently incorporated
within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this
License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive,
no-charge, royalty-free, irrevocable copyright license to reproduce, prepare
Derivative Works of, publicly display, publicly perform, sublicense, and distribute
the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License,
each Contributor hereby grants to You a perpetual, worldwide, non-exclusive,
no-charge, royalty-free, irrevocable (except as stated in this section) patent
license to make, have made, use, offer to sell, sell, import, and otherwise
transfer the Work, where such license applies only to those patent claims
licensable by such Contributor that are necessarily infringed by their Contribution(s)
alone or by combination of their Contribution(s) with the Work to which such
Contribution(s) was submitted. If You institute patent litigation against
any entity (including a cross-claim or counterclaim in a lawsuit) alleging
that the Work or a Contribution incorporated within the Work constitutes direct
or contributory patent infringement, then any patent licenses granted to You
under this License for that Work shall terminate as of the date such litigation
is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or
Derivative Works thereof in any medium, with or without modifications, and
in Source or Object form, provided that You meet the following conditions:

(a) You must give any other recipients of the Work or Derivative Works a copy
of this License; and

(b) You must cause any modified files to carry prominent notices stating that
You changed the files; and

(c) You must retain, in the Source form of any Derivative Works that You distribute,
all copyright, patent, trademark, and attribution notices from the Source
form of the Work, excluding those notices that do not pertain to any part
of the Derivative Works; and

(d) If the Work includes a "NOTICE" text file as part of its distribution,
then any Derivative Works that You distribute must include a readable copy
of the attribution notices contained within such NOTICE file, excluding those
notices that do not pertain to any part of the Derivative Works, in at least
one of the following places: within a NOTICE text file distributed as part
of the Derivative Works; within the Source form or documentation, if provided
along with the Derivative Works; or, within a display generated by the Derivative
Works, if and wherever such third-party notices normally appear. The contents
of the NOTICE file are for informational purposes only and do not modify the
License. You may add Your own attribution notices within Derivative Works
that You distribute, alongside or as an addendum to the NOTICE text from the
Work, provided that such additional attribution notices cannot be construed
as modifying the License.

You may add Your own copyright statement to Your modifications and may provide
additional or different license terms and conditions for use, reproduction,
or distribution of Your modifications, or for any such Derivative Works as
a whole, provided Your use, reproduction, and distribution of the Work otherwise
complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any
Contribution intentionally submitted for inclusion in the Work by You to the
Licensor shall be under the terms and conditions of this License, without
any additional terms or conditions. Notwithstanding the above, nothing herein
shall supersede or modify the terms of any separate license agreement you
may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names,
trademarks, service marks, or product names of the Licensor, except as required
for reasonable and customary use in describing the origin of the Work and
reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to
in writing, Licensor provides the Work (and each Contributor provides its
Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied, including, without limitation, any warranties
or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR
A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness
of using or redistributing the Work and assume any risks associated with Your
exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether
in tort (including negligence), contract, or otherwise, unless required by
applicable law (such as deliberate and grossly negligent acts) or agreed to
in writing, shall any Contributor be liable to You for damages, including
any direct, indirect, special, incidental, or consequential damages of any
character arising as a result of this License or out of the use or inability
to use the Work (including but not limited to damages for loss of goodwill,
work stoppage, computer failure or malfunction, or any and all other commercial
damages or losses), even if such Contributor has been advised of the possibility
of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work
or Derivative Works thereof, You may choose to offer, and charge a fee for,
acceptance of support, warranty, indemnity, or other liability obligations
and/or rights consistent with this License. However, in accepting such obligations,
You may act only on Your own behalf and on Your sole responsibility, not on
behalf of any other Contributor, and only if You agree to indemnify, defend,
and hold each Contributor harmless for any liability incurred by, or claims
asserted against, such Contributor by reason of your accepting any such warranty
or additional liability. END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

To apply the Apache License to your work, attach the following boilerplate
notice, with the fields enclosed by brackets "[]" replaced with your own identifying
information. (Don't include the brackets!) The text should be enclosed in
the appropriate comment syntax for the file format. We also recommend that
a file or class name and description of purpose be included on the same "printed
page" as the copyright notice for easier identification within third-party
archives.

Copyright 2020 Isak Johansson

Licensed under the Apache License, Version 2.0 (the "License");

you may not use this file except in compliance with the License.

You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software

distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and

limitations under the License.


File: /mikrotik.nix
{ mikrotik-config ? ./examples/configuration.nix }:
with import <nixpkgs> { };
with lib;
with builtins;

let
  rtr = (import mikrotik-config);

  formatValue = key: value:
    if key == "comment" then
      ''${key}="${value}"''
    else if key == "no_label" then
      formatValue null value
      #''${key}="${value}"''
    else if isAttrs value && key != null then
      concatStringsSep " " (["${key}"] ++ (mapAttrsToList (k: v: formatValue k v) value))

    else if isAttrs value then
      concatStringsSep " " (mapAttrsToList (k: v: formatValue k v) value)

    else
      "${key}=${value}";

  formatSection = name: opts:
    [ "${name}" ] ++ (if isAttrs opts then
      (mapAttrsToList (k: v: "set ${formatValue k v}") opts)
    else
      (map (x: "add ${formatValue null x}") opts));

in rec {
  mikrotik-router = stdenv.mkDerivation rec {
    version = "0.0.1";
    name = "mikrotik-router-${version}";

    src = builtins.toFile "router-config.rsc" (concatStringsSep "\n"
      (flatten (mapAttrsToList (key: values: formatSection key values) rtr)));

    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      mkdir $out
      install $src $out/router-config.rsc
    '';
  };
}


File: /nix-mikrotik-rs\.gitignore
/target
/result


File: /nix-mikrotik-rs\Cargo.lock
# This file is automatically @generated by Cargo.
# It is not intended for manual editing.
[[package]]
name = "autocfg"
version = "1.0.1"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "cdb031dd78e28731d87d56cc8ffef4a8f36ca26c38fe2de700543e627f8a464a"

[[package]]
name = "bitflags"
version = "1.2.1"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "cf1de2fe8c75bc145a2f577add951f8134889b4795d47466a54a5c846d691693"

[[package]]
name = "cc"
version = "1.0.66"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "4c0496836a84f8d0495758516b8621a622beb77c0fed418570e50764093ced48"

[[package]]
name = "cfg-if"
version = "0.1.10"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "4785bdd1c96b2a846b2bd7cc02e86b6b3dbf14e7e53446c4f54c92a361040822"

[[package]]
name = "cloudabi"
version = "0.0.3"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "ddfc5b9aa5d4507acaf872de71051dfd0e309860e88966e1051e462a077aac4f"
dependencies = [
 "bitflags",
]

[[package]]
name = "libc"
version = "0.2.81"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "1482821306169ec4d07f6aca392a4681f66c75c9918aa49641a2595db64053cb"

[[package]]
name = "libssh2-sys"
version = "0.2.20"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "df40b13fe7ea1be9b9dffa365a51273816c345fc1811478b57ed7d964fbfc4ce"
dependencies = [
 "cc",
 "libc",
 "libz-sys",
 "openssl-sys",
 "pkg-config",
 "vcpkg",
]

[[package]]
name = "libz-sys"
version = "1.1.2"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "602113192b08db8f38796c4e85c39e960c145965140e918018bcde1952429655"
dependencies = [
 "cc",
 "libc",
 "pkg-config",
 "vcpkg",
]

[[package]]
name = "lock_api"
version = "0.3.4"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "c4da24a77a3d8a6d4862d95f72e6fdb9c09a643ecdb402d754004a557f2bec75"
dependencies = [
 "scopeguard",
]

[[package]]
name = "nix-mikrotik-rs"
version = "0.1.0"
dependencies = [
 "ssh2",
]

[[package]]
name = "openssl-sys"
version = "0.9.59"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "de52d8eabd217311538a39bba130d7dea1f1e118010fee7a033d966845e7d5fe"
dependencies = [
 "autocfg",
 "cc",
 "libc",
 "pkg-config",
 "vcpkg",
]

[[package]]
name = "parking_lot"
version = "0.10.2"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "d3a704eb390aafdc107b0e392f56a82b668e3a71366993b5340f5833fd62505e"
dependencies = [
 "lock_api",
 "parking_lot_core",
]

[[package]]
name = "parking_lot_core"
version = "0.7.2"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "d58c7c768d4ba344e3e8d72518ac13e259d7c7ade24167003b8488e10b6740a3"
dependencies = [
 "cfg-if",
 "cloudabi",
 "libc",
 "redox_syscall",
 "smallvec",
 "winapi",
]

[[package]]
name = "pkg-config"
version = "0.3.19"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "3831453b3449ceb48b6d9c7ad7c96d5ea673e9b470a1dc578c2ce6521230884c"

[[package]]
name = "redox_syscall"
version = "0.1.57"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "41cc0f7e4d5d4544e8861606a285bb08d3e70712ccc7d2b84d7c0ccfaf4b05ce"

[[package]]
name = "scopeguard"
version = "1.1.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "d29ab0c6d3fc0ee92fe66e2d99f700eab17a8d57d1c1d3b748380fb20baa78cd"

[[package]]
name = "smallvec"
version = "1.5.1"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "ae524f056d7d770e174287294f562e95044c68e88dec909a00d2094805db9d75"

[[package]]
name = "ssh2"
version = "0.9.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "ed024de0a5e6944fe3080a3745e7a5649c5517ea2a6cfb16333f94f89c248985"
dependencies = [
 "bitflags",
 "libc",
 "libssh2-sys",
 "parking_lot",
]

[[package]]
name = "vcpkg"
version = "0.2.11"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "b00bca6106a5e23f3eee943593759b7fcddb00554332e856d990c893966879fb"

[[package]]
name = "winapi"
version = "0.3.9"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419"
dependencies = [
 "winapi-i686-pc-windows-gnu",
 "winapi-x86_64-pc-windows-gnu",
]

[[package]]
name = "winapi-i686-pc-windows-gnu"
version = "0.4.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "ac3b87c63620426dd9b991e5ce0329eff545bccbbb34f3be09ff6fb6ab51b7b6"

[[package]]
name = "winapi-x86_64-pc-windows-gnu"
version = "0.4.0"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "712e227841d057c1ee1cd2fb22fa7e5a5461ae8e48fa2ca79ec42cfc1931183f"


File: /nix-mikrotik-rs\Cargo.toml
[package]
name = "nix-mikrotik-rs"
version = "0.1.0"
authors = ["Isak Johansson <isak@irq1.se>"]
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
ssh2 = "0.9.0"

File: /nix-mikrotik-rs\src\main.rs
use ssh2::Session;
use std::io::prelude::*;
use std::net::TcpStream;
use std::path::Path;
use std::env;

fn main() {
    let mut session = connect();
    sftp_upload(session.clone());
    run_command(session.clone());
}

fn connect() -> ssh2::Session {
    // Connect to the local SSH server
    let tcp = TcpStream::connect("127.0.0.1:22").unwrap();
    let mut sess = Session::new().unwrap();
    sess.set_tcp_stream(tcp);
    sess.handshake().unwrap();

    sess.userauth_password(&env::var("SSH_USER").unwrap(), &env::var("SSH_PASSWORD").unwrap()).unwrap();
    sess
}
fn sftp_upload(sess: ssh2::Session) {
    let mut remote_file = sess
        .scp_send(Path::new("hello-remote.txt"), 0o644, 10, None)
        .unwrap();

    remote_file
        .write(b"Hello this is my message! hello!")
        .unwrap();
    // Close the channel and wait for the whole content to be tranferred
    remote_file.send_eof().unwrap();
    remote_file.wait_eof().unwrap();
    remote_file.close().unwrap();
    remote_file.wait_close().unwrap();
}

fn run_command(sess: ssh2::Session) {
    let mut channel = sess.channel_session().unwrap();
    channel.exec("echo running: /system reset-configuration keep-users no-defaults run-after-reset=new-build.rsc").unwrap();
    let mut s = String::new();
    channel.read_to_string(&mut s).unwrap();
    println!("{}", s);
    channel.wait_close();
    println!("{}", channel.exit_status().unwrap());
}


File: /README.org
* Nix Mikrotik
The goal of this project is to create a way to manage Mikrotik RouterOS routers using nix.

I'm not an expert with nix and I have no idea about how to go about creating a new nix project from scratch,
so this project is a learning project.

Very happy to have people get involved in this, Ideas / suggestions / PRs are welcome! You can reach me through github issues / PRs or on email [[mailto:isak@irq1.se][isak@irq1.se]].

* Setup
The usage of this project currently is very basic and something to be improved.

*** Download the repository
#+BEGIN_SRC sh
  git clone https://github.com/Plommonsorbet/nix-mikrotik
  cd nix-mikrotik
#+END_SRC

*** Example usage
**** Generate RouterOS configuration for examples/configuration.nix
#+BEGIN_SRC sh
nix-build mikrotik.nix
#+END_SRC

**** Generate RouterOS configuration for your own config.
#+BEGIN_SRC sh
nix-build mikrotik.nix --arg mikrotik-config ./my-config.nix
#+END_SRC

* Contributing

* Goals
** Mikrotik config(.rsc) parser
This is to be able to parse default router config for your router model or
your current configuration setup as a starting point when migrating.

** Deployment tool
Build a tool for deploying this configuration to devices similar to [[https://github.com/NixOS/nixops][nixops]] or [[https://github.com/DBCDK/morph][morph]].

** Diff tool
Create a diff tool to compare a test build with the active device config.

In the meanwhile a dirty script to just pull the build config and export the config from a device
and run the binary diff would be a start. But I want to have to eventually build a system that
is a bit smarter and can compare each configuration object. However this would need a parser before
it can be done.

** Testing
Some kind of testing that it works. This could be done against a vm running specific versions of RouterOS.

** Good Static Analysis
The config that is generated should be verified with assertions and network relevant types to minimize
the risk of a bad config being generated.

This is especially important since routers are so essential and a small mistake could be catastrophic.


File: /shell.nix
let
  moz_overlay = import (builtins.fetchTarball
    "https://github.com/mozilla/nixpkgs-mozilla/archive/master.tar.gz");
  nixpkgs = import <nixpkgs> { overlays = [ moz_overlay ]; };

  rust_nightly = (nixpkgs.latest.rustChannels.nightly.rust.override {
    extensions = [
      #"rust-src"
      "rust-analysis"
      "clippy-preview"
      "rustfmt-preview"
      "rls-preview"
    ]

    ;
  });
in with nixpkgs;
stdenv.mkDerivation {
  name = "nix-mikrotik";
  buildInputs = [ rust_nightly rustfmt openssl pkg-config];
}


