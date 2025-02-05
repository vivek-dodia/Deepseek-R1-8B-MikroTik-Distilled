# Repository Information
Name: mikrotik-ip

# Directory Structure
Directory structure:
└── github_repos/mikrotik-ip/
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
    │   │       ├── pack-c5da5cc3db58be867a23b38208403de51376cc36.idx
    │   │       └── pack-c5da5cc3db58be867a23b38208403de51376cc36.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── defaults/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── README.md
    ├── tasks/
    │   ├── address.yml
    │   ├── dns.yml
    │   ├── main.yml
    │   ├── routes.yml
    │   ├── services.yml
    │   └── settings.yml
    ├── templates/
    │   └── addresses.rsc.j2
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml


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
	url = https://github.com/mikrotik-ansible/mikrotik-ip.git
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
0000000000000000000000000000000000000000 acf9bbed3c1828cf34448298a2f4951b3bf5db0d vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-ip.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 acf9bbed3c1828cf34448298a2f4951b3bf5db0d vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-ip.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 acf9bbed3c1828cf34448298a2f4951b3bf5db0d vivek-dodia <vivek.dodia@icloud.com> 1738606375 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-ip.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
acf9bbed3c1828cf34448298a2f4951b3bf5db0d refs/remotes/origin/master


File: /.git\refs\heads\master
acf9bbed3c1828cf34448298a2f4951b3bf5db0d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /defaults\main.yml
---
# defaults file for mikrotik-ip
wan_interface: ether1

mikrotik_ip:
  # That remove all ip addresses you can lost connection
  remove_old_addresses: true
  addresses:
    - address: 192.168.88.1/24
      interface: "{{ wan_interface }}"
      disabled: "yes"
    - address: 10.0.0.129/24
      interface: "{{ wan_interface }}"
      comment: "Main"
      disabled: "no"
    - address: 10.11.11.2/24
      interface: ether12
      disabled: "no"
  # That remove all current routing table, you can lost your connection
  remove_old_routes: true
  routes:
    - gateway: 10.0.0.1
      dst_address: 0.0.0.0/0
      distance: 1
      scope: 30
      target_scope: 10
      check_gateway: ping
      routing_mark: main
    - geteway: 172.30.100.0/24
      dst_address: 10.11.11.254
      type: unicast
      distance: 1
      scope: 30
      target_scope: 10
  services:
    - name: api
      port: 8728
      disabled: "no"
      address: ""

    - name: api-ssl
      port: 8729
      disabled: "yes"
      address: ""

    - name: ftp
      port: 21
      disabled: "no"
      address: ""

    - name: ssh
      port: 22
      disabled: "no"
      address: ""

    - name: telnet
      port: 23
      disabled: "no"
      address: ""

    - name: winbox
      port: 8291
      disabled: "no"
      address: ""

    - name: www
      port: 80
      disabled: "no"
      address: ""

    - name: www-ssl
      port: 443
      disabled: "yes"
      address: ""

  settings:
    accept_redirects: "no"
    accept_source_route: "no"
    allow_fast_path: "yes"
    arp_timeout: "00:01:00"
    icmp_rate_limit: 10
    icmp_rate_mask: "0x1818"
    ip_forward: "yes"
    max_neighbor_entries: 2048
    route_cache: "yes"
    rp_filter: "no"
    secure_redirects: "yes"
    send_redirects: "yes"
    tcp_syncookies: "no"


File: /handlers\main.yml
---
# handlers file for mikrotik-ip

File: /meta\main.yml
galaxy_info:
  author: Martin Dulin
  description: Mikrotik automation
  company: Dulin
  license: MIT

  min_ansible_version: 1.2

  platforms:
    - name: RouterOS
      versions:
        - all

  categories:
    - networking

  galaxy_tags:
    - networking
    - mikrotik
    - routeros

dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.


File: /README.md
Role Name
=========

Complete IP address / Static routing management playbook

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).


File: /tasks\address.yml
---
  - name: Generate addresses-{{inventory_hostname}}.rsc to check and add user
    template: src=addresses.rsc.j2 dest={{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send addresses-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/addresses-{{inventory_hostname}}.rsc
    delegate_to: localhost

  # - name: Delete temporary addresses-{{inventory_hostname}}.rsc file
  #   file: path={{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc state=absent
  #   delegate_to: localhost

  - name: Run addresses-{{inventory_hostname}}.rsc on router
    raw:  "/import addresses-{{inventory_hostname}}.rsc"
    tags: mikrotik_ip_addresses

  - name: Remove addresses-{{inventory_hostname}}.rsc from router
    raw:  "/file remove addresses-{{inventory_hostname}}.rsc"


File: /tasks\dns.yml
---


File: /tasks\main.yml
---
# Address & route should run by script
- include: address.yml
  tags: [ 'role::mikrotik_ip:address']

- include: routes.yml
  tags: [ 'role::mikrotik_ip:routes']

- include: settings.yml
  tags: [ 'role::mikrotik_ip:settings' ]

- include: services.yml
  tags: [ 'role::mikrotik_ip:services' ]


File: /tasks\routes.yml
---


File: /tasks\services.yml
---
- name: Setting services
  raw: :if ([/ip service find where name={{ item.name }} port={{ item.port }} disabled={{ item.disabled }} address="{{ item.address }}"] = "") do={:put "Changed service {{ item.name}}..."; /ip service set {{ item.name }} port={{ item.port }} disabled={{ item.disabled }} address="{{ item.address }}"}
  with_items:
     - "{{ mikrotik_ip.services }}"
  register: mikrotik_out

- name: Print messages if changes was unsuccessful
  debug: msg="{{item.item}}"
  with_items: "{{mikrotik_out.results}}"
  when: item.stdout


File: /tasks\settings.yml
---
- name: "Setting accept-redirects={{ mikrotik_ip.settings.accept_redirects }}"
  raw: :if ([/ip settings get accept-redirects] != {{ mikrotik_ip.settings.accept_redirects }}) do={:put "accept-redirects"; /ip settings set accept-redirects={{ mikrotik_ip.settings.accept_redirects }} }
  when: mikrotik_ip.settings.accept_redirects is defined
  register: accept_redirects
  changed_when: accept_redirects.stdout_lines[0] is defined and accept_redirects.stdout_lines[0] == "accept-redirects"
  failed_when: accept_redirects.stdout_lines[0] is defined and accept_redirects.stdout_lines[0] != "accept-redirects"

- name: Setting accept-source-route={{ mikrotik_ip.settings.accept_source_route }}
  raw: :if ([/ip settings get accept-source-route] != {{ mikrotik_ip.settings.accept_source_route }}) do={:put "accept-source-route"; /ip settings set accept-source-route={{ mikrotik_ip.settings.accept_source_route }} }
  when: mikrotik_ip.settings.accept_source_route is defined
  register: accept_source_route
  changed_when: accept_source_route.stdout_lines[0] is defined and accept_source_route.stdout_lines[0] == "accept-source-route"
  failed_when: accept_source_route.stdout_lines[0] is defined and accept_source_route.stdout_lines[0] != "accept-source-route"

- name: Setting allow-fast-path={{ mikrotik_ip.settings.allow_fast_path }}
  raw: :if ([/ip settings get allow-fast-path] != {{ mikrotik_ip.settings.allow_fast_path }}) do={:put "allow-fast-path"; /ip settings set allow-fast-path={{ mikrotik_ip.settings.allow_fast_path }} }
  when: mikrotik_ip.settings.allow_fast_path is defined
  register: allow_fast_path
  changed_when: allow_fast_path.stdout_lines[0] is defined and allow_fast_path.stdout_lines[0] == "accept-redirects"
  failed_when: allow_fast_path.stdout_lines[0] is defined and allow_fast_path.stdout_lines[0] != "accept-redirects"

- name: Setting to arp-timeout={{ mikrotik_ip.settings.arp_timeout }}
  raw: :if ([/ip settings get arp-timeout] != {{ mikrotik_ip.settings.arp_timeout }}) do={:put "arp-timeout"; /ip settings set arp-timeout={{ mikrotik_ip.settings.arp_timeout }} }
  when: mikrotik_ip.settings.arp_timeout is defined
  register: arp_timeout
  changed_when: arp_timeout.stdout_lines[0] is defined and arp_timeout.stdout_lines[0] == "arp-timeout"
  failed_when: arp_timeout.stdout_lines[0] is defined and arp_timeout.stdout_lines[0] != "arp-timeout"

- name: Setting icmp-rate-limit={{ mikrotik_ip.settings.icmp_rate_limit }}
  raw: :if ([/ip settings get icmp-rate-limit] != {{ mikrotik_ip.settings.icmp_rate_limit }}) do={:put "icmp-rate-limit"; /ip settings set icmp-rate-limit={{ mikrotik_ip.settings.icmp_rate_limit }} }
  when: mikrotik_ip.settings.icmp_rate_limit is defined
  register: icmp_rate_limit
  changed_when: icmp_rate_limit.stdout_lines[0] is defined and icmp_rate_limit.stdout_lines[0] == "icmp-rate-limit"
  failed_when: icmp_rate_limit.stdout_lines[0] is defined and icmp_rate_limit.stdout_lines[0] != "icmp-rate-limit"

- name: Setting icmp-rate-mask={{ mikrotik_ip.settings.icmp_rate_mask }}
  raw: :if ([/ip settings get icmp-rate-mask] != {{ mikrotik_ip.settings.icmp_rate_mask }}) do={:put "icmp-rate-mask"; /ip settings set icmp-rate-mask={{ mikrotik_ip.settings.icmp_rate_mask }} }
  when: mikrotik_ip.settings.icmp_rate_mask is defined
  register: icmp_rate_mask
  changed_when: icmp_rate_mask.stdout_lines[0] is defined and icmp_rate_mask.stdout_lines[0] == "icmp-rate-mask"
  failed_when: icmp_rate_mask.stdout_lines[0] is defined and icmp_rate_mask.stdout_lines[0] != "icmp-rate-mask"

- name: Setting ip-forward={{ mikrotik_ip.settings.ip_forward }}
  raw: :if ([/ip settings get ip-forward] != {{ mikrotik_ip.settings.ip_forward }}) do={:put "ip-forward"; /ip settings set ip-forward={{ mikrotik_ip.settings.ip_forward }} }
  when: mikrotik_ip.settings.ip_forward is defined
  register: ip_forward
  changed_when: ip_forward.stdout_lines[0] is defined and ip_forward.stdout_lines[0] == "ip-forward"
  failed_when: ip_forward.stdout_lines[0] is defined  and ip_forward.stdout_lines[0] != "ip-forward"

- name: Setting max-neighbor-entries={{ mikrotik_ip.settings.max_neighbor_entries }}
  raw: :if ([/ip settings get max-neighbor-entries] != {{ mikrotik_ip.settings.max_neighbor_entries }}) do={:put "max-neighbor-entries"; /ip settings set max-neighbor-entries={{ mikrotik_ip.settings.max_neighbor_entries }} }
  when: mikrotik_ip.settings.max_neighbor_entries is defined
  register: max_neighbor_entries
  changed_when: max_neighbor_entries.stdout_lines[0] is defined and max_neighbor_entries.stdout_lines[0] == "max-neighbor-entries"
  failed_when: max_neighbor_entries.stdout_lines[0] is defined and max_neighbor_entries.stdout_lines[0] != "max-neighbor-entries"

- name: Setting route-cache={{ mikrotik_ip.settings.route_cache }}
  raw: :if ([/ip settings get route-cache] != {{ mikrotik_ip.settings.route_cache }}) do={:put "route-cache"; /ip settings set route-cache={{ mikrotik_ip.settings.route_cache }} }
  when: mikrotik_ip.settings.route_cache is defined
  register: route_cache
  changed_when: route_cache.stdout_lines[0] is defined and route_cache.stdout_lines[0] == "route-cache"
  failed_when: route_cache.stdout_lines[0] is defined and route_cache.stdout_lines[0] != "route-cache"

- name: Setting rp-filter={{ mikrotik_ip.settings.rp_filter }}
  raw: :if ([/ip settings get rp-filter] != "{{ mikrotik_ip.settings.rp_filter }}") do={:put "rp-filter"; /ip settings set rp-filter={{ mikrotik_ip.settings.rp_filter }} }
  when: mikrotik_ip.settings.rp_filter is defined
  register: rp_filter
  changed_when: rp_filter.stdout_lines[0] is defined and rp_filter.stdout_lines[0] == "rp-filter"
  failed_when: rp_filter.stdout_lines[0] is defined and rp_filter.stdout_lines[0] != "rp-filter"

- name: Setting secure-redirects={{ mikrotik_ip.settings.secure_redirects }}
  raw: :if ([/ip settings get secure-redirects] != {{ mikrotik_ip.settings.secure_redirects }}) do={:put "secure-redirects"; /ip settings set secure-redirects={{ mikrotik_ip.settings.secure_redirects }} }
  when: mikrotik_ip.settings.secure_redirects is defined
  register: secure_redirects
  changed_when: secure_redirects.stdout_lines[0] is defined and secure_redirects.stdout_lines[0] == "secure-redirects"
  failed_when: secure_redirects.stdout_lines[0] is defined  and secure_redirects.stdout_lines[0] != "secure-redirects"

- name: Setting send-redirects={{ mikrotik_ip.settings.send_redirects }}
  raw: :if ([/ip settings get send-redirects] != {{ mikrotik_ip.settings.send_redirects }}) do={:put "send-redirects"; /ip settings set send-redirects={{ mikrotik_ip.settings.send_redirects }} }
  when: mikrotik_ip.settings.send_redirects is defined
  register: send_redirects
  changed_when: send_redirects.stdout_lines[0] is defined and send_redirects.stdout_lines[0] == "send-redirects"
  failed_when: send_redirects.stdout_lines[0] is defined  and send_redirects.stdout_lines[0] != "send-redirects"

- name: Setting tcp-syncookies={{ mikrotik_ip.settings.tcp_syncookies }}
  raw: :if ([/ip settings get tcp-syncookies] != {{ mikrotik_ip.settings.tcp_syncookies }}) do={:put "tcp-syncookies"; /ip settings set tcp-syncookies={{ mikrotik_ip.settings.tcp_syncookies }} }
  when: mikrotik_ip.settings.tcp_syncookies is defined
  register: tcp_syncookies
  changed_when: tcp_syncookies.stdout_lines[0] is defined and tcp_syncookies.stdout_lines[0] == "tcp-syncookies"
  failed_when: tcp_syncookies.stdout_lines[0] is defined  and tcp_syncookies.stdout_lines[0] != "tcp-syncookies"


File: /templates\addresses.rsc.j2
{% if  mikrotik_ip.remove_old_addresses == true %}
/ip address remove [/ip address find were dynamic=no]
{% endif %}

/ip address remove [/ip address find where !(\
{% for list in mikrotik_ip.addresses %}
{% if iter is defined %} or {% endif %}(interface={{list.interface}} and disabled={{list.disabled}} and address="{{list.address}}" {% if list.comment is defined %}and comment="Ansible managed: [{{list.comment}}]"{% endif %}) \
{% set iter = true %}
{% endfor %}
) and dynamic=no]

# Add all values
{% for list in mikrotik_ip.addresses %}
:if ([/ip address find interface={{list.interface}} disabled={{list.disabled}} address="{{list.address}}"{% if list.comment is defined %} comment="Ansible managed: [{{list.comment}}]"{% endif %}] = "") do={
:log info "Add address: {{list.address}} to interface: {{list.interface}}..."
/ip address add interface={{list.interface}} {% if list.disabled is defined %}disabled={{list.disabled}} {%endif%}address={{list.address}}\
{% if list.comment is defined %}comment="Ansible managed: [{{list.comment}}]"{% endif %}
}
{% endfor %}


File: /tests\inventory
localhost



File: /tests\test.yml
---
- hosts: localhost
  remote_user: root
  roles:
    - mikrotik-ip

File: /vars\main.yml
---
# vars file for mikrotik-ip

